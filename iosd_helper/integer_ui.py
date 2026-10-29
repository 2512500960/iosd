"""IDA 9.1 native formats and persistent, display-only Hex-Rays interpretations."""
import hashlib
import json
import re
import ida_bytes as ib
import ida_ida
import ida_idaapi
import ida_kernwin as kw
import ida_lines
import ida_ua

from .integer_display import FORMATS, literal_bytes, code_mask

ACTION = 'iosd_helper:integer_display'
_manager = None


class NativeFormat(ib.data_format_t):
    def __init__(self, spec):
        super().__init__(spec.name, spec.width, spec.label)
        self.spec = spec

    def printf(self, value, current_ea, operand_num, dtid):
        try:
            if ib.is_code(ib.get_full_flags(current_ea)):
                insn = ida_ua.insn_t()
                if operand_num < 0 or operand_num >= len(insn.ops) or not ida_ua.decode_insn(insn, current_ea):return None
                op = insn.ops[operand_num]
                if op.type != ida_ua.o_imm:return None
                value = literal_bytes(int(op.value), self.spec.width, 'big' if ida_ida.inf_is_be() else 'little')
            return self.spec.render(bytes(value))
        except (ValueError, TypeError):
            return None


class FormatChoice(kw.Choose):
    def __init__(self, raw=None, pseudocode=False, value=None):
        super().__init__('iosd | integer interpretation', [['Display format', 53], ['Preview', 44]])
        self.specs = [];self.raws = [];self.rows = []
        for spec in FORMATS:
            if raw is not None and spec.width != len(raw):continue
            try:
                data = raw if raw is not None else literal_bytes(value, spec.width, 'big' if ida_ida.inf_is_be() else 'little')
            except ValueError:continue
            self.specs.append(spec);self.raws.append(data);self.rows.append([spec.label, spec.render(data)])
        self.rows.append(['Restore original pseudocode integer (remove saved interpretation)' if pseudocode else 'Restore standard hexadecimal display', ''])

    def OnGetSize(self):return len(self.rows)
    def OnGetLine(self, n):return self.rows[n]


class Action(kw.action_handler_t):
    def __init__(self, manager):
        super().__init__();self.manager = manager

    def activate(self, ctx):
        try:self.manager.show(ctx.widget)
        except Exception as exc:kw.warning('iosd integer display: %s' % exc)
        return 1

    def update(self, ctx):
        return kw.AST_ENABLE_FOR_WIDGET if ctx.widget_type in (kw.BWN_DISASM, kw.BWN_PSEUDOCODE) else kw.AST_DISABLE_FOR_WIDGET


class Popup(kw.UI_Hooks):
    def populating_widget_popup(self, widget, popup):
        if kw.get_widget_type(widget) in (kw.BWN_DISASM, kw.BWN_PSEUDOCODE):
            kw.attach_action_to_popup(widget, popup, ACTION, 'iosd Helper/')


class IDBDisplayStore:
    """One private, bounded netnode blob per IDB; addresses inside it are RVAs."""
    NODE = '$ iosd_helper integer display v2'

    def identity(self):
        import ida_nalt
        return ida_nalt.retrieve_input_file_md5().hex(), ida_nalt.get_imagebase()

    def node(self, create=False):
        import ida_netnode
        return ida_netnode.netnode(self.NODE, 0, create)

    def load(self):
        import ida_netnode
        if not ida_netnode.netnode.exist(self.NODE):
            return {'schema': 2, 'md5': self.identity()[0], 'functions': {}}
        node = self.node()
        size = node.blobsize(0, 'I')
        if size < 0 or size > 4*1024*1024:raise ValueError('Invalid saved integer interpretation size')
        raw = node.getblob(0, 'I') if size else None
        data = json.loads(raw) if raw else {'schema': 2, 'md5': self.identity()[0], 'functions': {}}
        if data.get('schema') != 2 or data.get('md5') != self.identity()[0]:
            raise ValueError('Saved integer interpretations belong to a different input/schema')
        return data

    def read(self, rva):
        return self.load()['functions'].get(str(rva), [])

    def write(self, rva, entries):
        data = self.load()
        if entries:data['functions'][str(rva)] = entries
        else:data['functions'].pop(str(rva), None)
        raw = json.dumps(data, separators=(',', ':')).encode()
        if len(raw) > 4*1024*1024:raise ValueError('Too many saved integer interpretations')
        node = self.node(True)
        if not data['functions']:
            node.delblob(0, 'I')
        elif not node.setblob(raw, 0, 'I'):
            raise ValueError('Could not save integer interpretations in the IDB')


class PseudocodeNotes:
    """Replace only anchored numeric tokens; never write to ctree or user_numforms."""
    NUMBER = re.compile(r'(?<![\w.\'\"])[+-]?(?:0[xX][0-9a-fA-F]+|[0-9]+)(?:[uUlL]+|i64)?(?![\w.])')

    def __init__(self, hr, store=None):
        self.hr = hr;self.store = store if store is not None else IDBDisplayStore()
        self.rendered = {};self.busy = set();self.skipped = {}
        owner = self
        class Hooks(hr.Hexrays_Hooks):
            def func_printed(self, cfunc):
                try:owner.apply(cfunc)
                except Exception as exc:kw.msg('[iosd-helper] Integer display skipped: %s\n' % exc)
                return 0
        self.hooks = Hooks();self.hooks.hook()

    def visible(self, line):
        """Map visible characters back to tagged text and the last real ctree anchor."""
        chars = [];positions = [];anchors = [];colors = [];i = 0;current = None;color = None
        while i < len(line):
            ch = line[i]
            if ch == ida_lines.SCOLOR_ON and i+1 < len(line) and line[i+1] == ida_lines.SCOLOR_ADDR:
                stop = i+2+ida_lines.COLOR_ADDR_SIZE
                anchor = self.hr.ctree_anchor_t();anchor.value = int(line[i+2:stop], 16)
                current = anchor.get_index() if anchor.is_citem_anchor() else None
                i = stop;continue
            if ch in (ida_lines.SCOLOR_ON, ida_lines.SCOLOR_OFF):
                if i+1 >= len(line):raise ValueError('Incomplete pseudocode color tag')
                color = line[i+1] if ch == ida_lines.SCOLOR_ON else None
                i += 2;continue
            if ch == ida_lines.SCOLOR_INV:i += 1;continue
            if ch == ida_lines.SCOLOR_ESC:
                i += 1
                if i >= len(line):raise ValueError('Incomplete escaped pseudocode character')
                ch = line[i]
            chars.append(ch);positions.append(i);anchors.append(current);colors.append(color);i += 1
        return ''.join(chars), positions, anchors, colors

    def clean_lines(self, cfunc):
        previous = self.rendered.get((ida_ida.get_dbctx_id(), cfunc.entry_ea), {})
        return [previous.get(sl.line, sl.line) for sl in cfunc.get_pseudocode()]

    def tokens(self, cfunc, lines):
        base = self.store.identity()[1];result = []
        def context(text):
            # IDA's autogenerated address names change on rebase; analyst names remain literal.
            def name(match):
                ea = int(match[2], 16)
                return match[1]+'_rva%X' % (ea-base) if ea >= base else match[0]
            text = re.sub(r'\b(sub|loc|off|unk|byte|word|dword|qword)_([0-9A-Fa-f]{8,16})\b', name, text)
            return ' '.join(text.split())
        in_block = False
        for row, line in enumerate(lines):
            visible, pos, anchors, colors = self.visible(line)
            code, in_block = code_mask(visible, in_block)
            for match in self.NUMBER.finditer(visible):
                start, stop = match.span();index = anchors[start]
                if not all(code[start:stop]):continue
                if index is None or not 0 <= index < len(cfunc.treeitems):continue
                item = cfunc.treeitems[index]
                if item.op != self.hr.cot_num:continue
                if any(anchors[n] != index or pos[n] != pos[start]+n-start for n in range(start,stop)):continue
                # All characters, including a printed sign, must belong to the numeric item.
                expr = item.cexpr
                signature = {'value': int(expr.n._value), 'size': int(expr.type.get_size()),
                             'expr_rva': int(expr.ea)-base if expr.ea != ida_idaapi.BADADDR else None,
                             'context': hashlib.sha256((context(visible[:start])+'\0'+match[0]+'\0'+context(visible[stop:])).encode()).hexdigest()}
                result.append({'index': index, 'row': row, 'start': pos[start], 'stop': pos[stop-1]+1,
                               'signature': signature})
        return result

    def put(self, cfunc, expr, spec, raw):
        originals = self.clean_lines(cfunc);tokens = self.tokens(cfunc, originals)
        selected = [t for t in tokens if t['index'] == expr.index]
        if len(selected) != 1:raise ValueError('Select a plain printed integer literal with a unique ctree anchor')
        sig = selected[0]['signature']
        if sum(t['signature'] == sig for t in tokens) != 1:
            raise ValueError('Ambiguous integer context; interpretation was not saved')
        rva = cfunc.entry_ea-self.store.identity()[1]
        entries = [e for e in self.store.read(rva) if e['signature'] != sig]
        if spec:
            expected = literal_bytes(sig['value'], spec.width, 'big' if ida_ida.inf_is_be() else 'little')
            if expected != raw:raise ValueError('Integer preview no longer matches the original value')
            entries.append({'signature': sig, 'format': spec.name, 'byteorder': 'big' if ida_ida.inf_is_be() else 'little'})
        self.store.write(rva, entries)
        self.apply(cfunc)

    def apply(self, cfunc):
        key = (ida_ida.get_dbctx_id(), cfunc.entry_ea)
        if key in self.busy:return
        self.busy.add(key)
        try:
            entries = self.store.read(cfunc.entry_ea-self.store.identity()[1])
            if not entries and key not in self.rendered:return
            originals = self.clean_lines(cfunc);tokens = self.tokens(cfunc, originals);changes = {};skipped = 0
            for entry in entries:
                matches = [t for t in tokens if t['signature'] == entry['signature']]
                spec = next((s for s in FORMATS if s.name == entry['format']), None)
                if len(matches) != 1 or spec is None or entry['byteorder'] != ('big' if ida_ida.inf_is_be() else 'little'):
                    skipped += 1;continue
                t = matches[0]
                raw = literal_bytes(t['signature']['value'], spec.width, entry['byteorder'])
                changes.setdefault(t['row'], []).append((t['start'], t['stop'], spec.render(raw)))
            updated = list(originals)
            for row, replacements in changes.items():
                for start, stop, text in sorted(replacements, reverse=True):
                    updated[row] = updated[row][:start]+text+updated[row][stop:]
            self.rendered[key] = {new: old for old, new in zip(originals, updated) if new != old}
            # func_printed supplies a borrowed cfunc_t. Never construct an owning smart
            # pointer from it, or retain it beyond this callback. Only strings are cached.
            for sl, line in zip(cfunc.get_pseudocode(), updated):sl.line = line
            self.skipped[key] = skipped
            if skipped:kw.msg('[iosd-helper] %d saved integer display(s) could not be uniquely matched in %X; original numbers retained.\n' % (skipped, cfunc.entry_ea))
        finally:self.busy.remove(key)

    def clear(self, cfunc):
        self.store.write(cfunc.entry_ea-self.store.identity()[1], [])
        self.apply(cfunc)
        self.clear_key((ida_ida.get_dbctx_id(), cfunc.entry_ea))

    def clear_key(self, key):
        self.rendered.pop(key, None);self.skipped.pop(key, None)

    def clear_database(self, dbid):
        for key in list(self.rendered):
            if key[0] == dbid:self.clear_key(key)

    def close(self):
        self.hooks.unhook()
        # Cached text is owned by Hex-Rays. A later F5 with the hook removed prints
        # the original literals. Unload never dereferences stale/borrowed objects.
        self.rendered.clear();self.skipped.clear()


class Manager:
    def __init__(self):
        self.users = 0;self.formats = [];self.popup = None;self.pseudocode = None;self.action = None
        self.action_registered = False
        try:
            for spec in FORMATS:
                if ib.find_custom_data_format(spec.name) >= 0:
                    raise ValueError('Format already owned by another loaded copy: '+spec.name)
                fmt = NativeFormat(spec)
                if ib.register_custom_data_format(fmt) < 0:raise ValueError('Cannot register '+spec.name)
                self.formats.append(fmt)
                if not ib.attach_custom_data_format(0, fmt.id):raise ValueError('Cannot attach '+spec.name)
            self.action = Action(self)
            if not kw.register_action(kw.action_desc_t(ACTION, 'Integer display / BE interpretation...', self.action)):
                raise ValueError('Integer display action already registered')
            self.action_registered = True
            self.popup = Popup();self.popup.hook()
            try:
                import ida_hexrays as hr
                if hr.init_hexrays_plugin():self.pseudocode = PseudocodeNotes(hr)
            except ImportError:pass
        except Exception:
            self.close();raise

    def show(self, widget=None):
        widget = widget or kw.get_current_widget()
        if kw.get_widget_type(widget) == kw.BWN_PSEUDOCODE:
            if self.pseudocode is None:raise ValueError('Hex-Rays is not available')
            hr = self.pseudocode.hr;vu = hr.get_widget_vdui(widget)
            if not vu or not vu.get_current_item(hr.USE_KEYBOARD) or not vu.item.is_citem():
                raise ValueError('Place the cursor on an integer literal')
            expr = vu.item.e
            if expr is None or expr.op != hr.cot_num:raise ValueError('Select an integer literal, not a variable or whole expression')
            choice = FormatChoice(pseudocode=True, value=int(expr.n._value));selected = choice.Show(True)
            if selected < 0:return
            spec = choice.specs[selected] if selected < len(choice.specs) else None
            self.pseudocode.put(vu.cfunc, expr, spec, choice.raws[selected] if spec else None)
            kw.refresh_custom_viewer(widget)
            return
        if kw.get_widget_type(widget) != kw.BWN_DISASM:
            raise ValueError('Open a disassembly/data or Hex-Rays view, then use its iosd Helper context menu')
        ea = kw.get_screen_ea();head = ib.get_item_head(ea);flags = ib.get_full_flags(head)
        operand = 0
        if ib.is_code(flags):
            operand = kw.get_opnum();insn = ida_ua.insn_t()
            if operand < 0 or not ida_ua.decode_insn(insn, head) or insn.ops[operand].type != ida_ua.o_imm:
                raise ValueError('Place the cursor on an immediate integer operand')
            choice = FormatChoice(value=int(insn.ops[operand].value))
        else:
            if not any(check(flags) for check in (ib.is_word, ib.is_dword, ib.is_qword)):
                raise ValueError('Define a WORD/DWORD/QWORD first; this action does not redefine bytes')
            width = ib.get_data_elsize(head, flags)
            if width not in (2,4,8):raise ValueError('Only 16/32/64-bit integer elements are supported')
            # Arrays keep their shape; apply the format to the existing item.
            from .ida_adapter import IDBMemory
            raw = IDBMemory().read(head, width)
            choice = FormatChoice(raw)
        selected = choice.Show(True)
        if selected < 0:return
        if selected == len(choice.specs):ok = ib.op_hex(head, operand)
        else:
            spec = choice.specs[selected]
            fmt = next(f for f in self.formats if f.spec == spec)
            ok = ib.op_custfmt(head, operand, fmt.id)
        if not ok:raise ValueError('IDA rejected the operand display format')
        kw.refresh_idaview_anyway()

    def close(self):
        if self.popup:self.popup.unhook();self.popup = None
        if self.pseudocode:self.pseudocode.close();self.pseudocode = None
        if self.action_registered:kw.unregister_action(ACTION);self.action_registered = False
        self.action = None
        for fmt in reversed(self.formats):ib.unregister_custom_data_format(fmt.id)
        self.formats.clear()


class IntegerDisplaySession:
    def __init__(self):
        global _manager
        if _manager is None:_manager = Manager()
        _manager.users += 1;self.manager = _manager;self.dbid = ida_ida.get_dbctx_id()

    def show(self):self.manager.show()

    def close(self):
        global _manager
        if self.manager is None:return
        if self.manager.pseudocode:self.manager.pseudocode.clear_database(self.dbid)
        self.manager.users -= 1
        if not self.manager.users:
            self.manager.close();_manager = None
        self.manager = None
