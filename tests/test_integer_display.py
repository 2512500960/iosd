import importlib
import sys
from types import ModuleType, SimpleNamespace as NS
import unittest
from unittest.mock import Mock, patch

from iosd_helper.integer_display import IntegerFormat, FORMATS, literal_bytes, append_notes


class IntegerTests(unittest.TestCase):
    def test_byte_order_is_explicit_and_plain_numbers_keep_the_tag_bit(self):
        self.assertEqual(IntegerFormat(4).render(bytes.fromhex('00000001')), 'BE32(0x00000001)')
        self.assertEqual(IntegerFormat(4).render(bytes.fromhex('01020304')), 'BE32(0x01020304)')
        raw=bytes.fromhex('8000000000000001')
        self.assertEqual(IntegerFormat(8).render(raw), 'BE64(0x8000000000000001)')
        self.assertEqual(IntegerFormat(8,10,True).render(raw), 'BE64s(-9223372036854775807)')
        self.assertEqual(IntegerFormat(8,tagged=True).render(raw), 'IOSD_BE64_PTR(0x0000000000000001)')

    def test_wrong_width_or_unrepresentable_literal_is_rejected(self):
        with self.assertRaises(ValueError):IntegerFormat(4).render(bytes(8))
        with self.assertRaises(ValueError):IntegerFormat(4,tagged=True).render(bytes(4))
        for value,width in ((0x10000,2),(0xffffffff01000000,4),(-32769,2),(1,3)):
            with self.assertRaises(ValueError):literal_bytes(value,width,'little')
        self.assertEqual(literal_bytes(0xffffffffffffffff,4,'little'),bytes.fromhex('ffffffff'))
        self.assertEqual(literal_bytes(0x1000000,4,'little'),bytes.fromhex('00000001'))
        self.assertEqual(literal_bytes(0x1000000,4,'big'),bytes.fromhex('01000000'))

    def test_only_selected_anchor_gets_a_note_even_when_literals_repeat(self):
        lines=['a=0x1000000; "0x1000000"; // existing user comment','b=0x1000000;']
        result=append_notes(lines,{7:'BE32(1)'},lambda line:[7,7] if line.startswith('a=') else [9])
        self.assertEqual(result[1],lines[1])
        self.assertTrue(result[0].startswith(lines[0]));self.assertEqual(result[0].count('BE32(1)'),1)


class IntegerUIBoundaryTests(unittest.TestCase):
    def setUp(self):
        self.mods={n:ModuleType(n) for n in ('ida_bytes','ida_ida','ida_idaapi','ida_kernwin','ida_lines','ida_ua','ida_hexrays')}
        ib=self.mods['ida_bytes'];kw=self.mods['ida_kernwin'];self.registry={};self.nextid=1
        class DataFormat:
            def __init__(this,name,width,label):this.name=name;this.id=-1
        ib.data_format_t=DataFormat
        ib.find_custom_data_format=lambda name:next((i for i,f in self.registry.items() if f.name==name),-1)
        def register(f):
            f.id=self.nextid;self.nextid+=1;self.registry[f.id]=f;return f.id
        ib.register_custom_data_format=Mock(side_effect=register)
        ib.unregister_custom_data_format=Mock(side_effect=lambda fid:self.registry.pop(fid,None))
        ib.attach_custom_data_format=Mock(return_value=True)
        ib.get_full_flags=Mock(return_value=0);ib.is_code=Mock(return_value=False)
        class Hooks:
            def hook(this):return True
            def unhook(this):return True
        kw.action_handler_t=Hooks;kw.UI_Hooks=Hooks;kw.Choose=type('Choose',(),{})
        kw.register_action=Mock(return_value=True);kw.unregister_action=Mock()
        kw.action_desc_t=lambda *args:args
        kw.msg=Mock();self.mods['ida_ida'].inf_is_be=lambda:False
        self.mods['ida_ida'].get_dbctx_id=Mock(return_value=0)
        hr=self.mods['ida_hexrays'];hr.init_hexrays_plugin=lambda:False;hr.Hexrays_Hooks=Hooks;hr.cot_num=7
        class Anchor:
            value=0
            def is_citem_anchor(this):return this.value<0x10000000
            def get_index(this):return this.value
        hr.ctree_anchor_t=Anchor;hr.cfuncptr_t=Mock(side_effect=AssertionError('Do not own a borrowed cfunc'))
        self.mods['ida_lines'].SCOLOR_ON='\x01';self.mods['ida_lines'].SCOLOR_ADDR='('
        self.mods['ida_lines'].COLOR_ADDR_SIZE=16
        self.mods['ida_lines'].SCOLOR_OFF='\x02';self.mods['ida_lines'].SCOLOR_ESC='\x03'
        self.mods['ida_lines'].SCOLOR_INV='\x04';self.mods['ida_lines'].SCOLOR_DNUM=' '
        self.mods['ida_idaapi'].BADADDR=0xffffffffffffffff
        self.patch=patch.dict(sys.modules,self.mods);self.patch.start();self.addCleanup(self.patch.stop)
        sys.modules.pop('iosd_helper.integer_ui',None)
        self.ui=importlib.import_module('iosd_helper.integer_ui')
        self.addCleanup(lambda:sys.modules.pop('iosd_helper.integer_ui',None))

    def test_multiple_sessions_share_registration_and_last_close_cleans_up(self):
        a=self.ui.IntegerDisplaySession();b=self.ui.IntegerDisplaySession()
        self.assertEqual(len(self.registry),len(FORMATS))
        a.close();a.close();self.assertEqual(len(self.registry),len(FORMATS))
        b.close();self.assertFalse(self.registry)
        self.mods['ida_kernwin'].unregister_action.assert_called_once()

    def test_partial_failure_and_foreign_action_do_not_leak_or_unregister_another_owner(self):
        self.mods['ida_bytes'].attach_custom_data_format.side_effect=[True,False]
        with self.assertRaises(ValueError):self.ui.IntegerDisplaySession()
        self.assertFalse(self.registry)
        self.mods['ida_kernwin'].unregister_action.assert_not_called()
        self.mods['ida_bytes'].attach_custom_data_format.side_effect=None
        self.mods['ida_kernwin'].register_action.return_value=False
        with self.assertRaises(ValueError):self.ui.IntegerDisplaySession()
        self.assertFalse(self.registry)
        self.mods['ida_kernwin'].unregister_action.assert_not_called()

    def test_native_immediate_has_explicit_width_even_if_ida_passes_eight_bytes(self):
        ib=self.mods['ida_bytes'];ib.is_code.return_value=True
        ua=self.mods['ida_ua'];ua.o_imm=1
        ua.insn_t=lambda:NS(ops=[NS(type=1,value=0x1000000)])
        ua.decode_insn=lambda insn,ea:1
        fmt=self.ui.NativeFormat(IntegerFormat(4))
        self.assertEqual(fmt.printf(bytes(8),0x1000,0,0),'BE32(0x00000001)')
        ib.is_code.return_value=False
        self.assertIsNone(fmt.printf(bytes(8),0x1000,0,0))

    def display_store(self):
        data={};identity=['abc',0x1000]
        def read(rva):return data.get((self.mods['ida_ida'].get_dbctx_id(),rva),[])
        def write(rva,entries):data[(self.mods['ida_ida'].get_dbctx_id(),rva)]=entries
        return NS(read=read,write=write,identity=lambda:identity),identity

    def function(self,index=0,base=0x1000,text='x = ',tail='; // user'):
        expr=NS(index=index,ea=base+0x10,n=NS(_value=0x1000000),type=NS(get_size=lambda:4))
        original=text+'\x01(%016X\x01 0x1000000\x02 '%index+tail
        lines=[NS(line=original)]
        cf=NS(entry_ea=base,treeitems=[NS(op=0)]*index+[NS(op=7,cexpr=expr)],get_pseudocode=lambda:lines)
        return cf,expr,original

    def test_direct_display_preserves_ctree_and_survives_new_indices_f5_and_reload(self):
        store,_=self.display_store();notes=self.ui.PseudocodeNotes(self.mods['ida_hexrays'],store)
        cf,expr,original=self.function()
        notes.put(cf,expr,IntegerFormat(4,10),bytes.fromhex('00000001'))
        self.assertIn('x = \x01(0000000000000000\x01 BE32(1)\x02 ; // user',cf.get_pseudocode()[0].line)
        notes.apply(cf);self.assertEqual(cf.get_pseudocode()[0].line.count('BE32(1)'),1)
        self.assertEqual(expr.n._value,0x1000000)
        new,other,_=self.function(index=5)
        notes.hooks.func_printed(new)
        self.assertIn('BE32(1)',new.get_pseudocode()[0].line)
        notes.close()
        # F5 provides fresh text on reload; unload never accesses borrowed cfuncs.
        new,other,_=self.function(index=5)
        fresh=self.ui.PseudocodeNotes(self.mods['ida_hexrays'],store)
        fresh.hooks.func_printed(new);self.assertIn('BE32(1)',new.get_pseudocode()[0].line)
        fresh.put(new,other,None,None)
        self.assertEqual(new.get_pseudocode()[0].line,self.function(index=5)[2]);fresh.close()
        self.mods['ida_hexrays'].cfuncptr_t.assert_not_called()

    def test_changed_context_or_ambiguous_match_keeps_original_and_saved_rule(self):
        store,_=self.display_store();notes=self.ui.PseudocodeNotes(self.mods['ida_hexrays'],store)
        cf,expr,_=self.function();notes.put(cf,expr,IntegerFormat(4,10),bytes.fromhex('00000001'))
        new,_,original=self.function(index=5,text='renamed = ')
        notes.hooks.func_printed(new);self.assertEqual(new.get_pseudocode()[0].line,original)
        self.assertEqual(notes.skipped[(0,0x1000)],1);self.assertTrue(store.read(0))
        dup,e,original=self.function(index=5)
        dup.get_pseudocode().append(NS(line=original))
        notes.hooks.func_printed(dup)
        self.assertTrue(all('BE32' not in s.line for s in dup.get_pseudocode()))
        with self.assertRaisesRegex(ValueError,'unique'):notes.put(dup,e,IntegerFormat(4,10),bytes.fromhex('00000001'))
        notes.close()

    def test_same_value_elsewhere_and_string_or_user_comment_are_untouched(self):
        store,_=self.display_store();notes=self.ui.PseudocodeNotes(self.mods['ida_hexrays'],store)
        cf,e,original=self.function(tail='; f("0x1000000"); // 0x1000000')
        other,_,otherline=self.function(index=1,text='y = ')
        cf.treeitems+=other.treeitems[1:];cf.get_pseudocode().append(other.get_pseudocode()[0])
        notes.put(cf,e,IntegerFormat(4,10),bytes.fromhex('00000001'))
        self.assertTrue(cf.get_pseudocode()[0].line.endswith('; f("0x1000000"); // 0x1000000'))
        self.assertEqual(cf.get_pseudocode()[1].line,otherline);notes.close()

    def test_rva_and_generated_names_survive_rebase_without_widening_selection(self):
        store,identity=self.display_store();notes=self.ui.PseudocodeNotes(self.mods['ida_hexrays'],store)
        cf,e,_=self.function(text='dword_00001020 = ')
        notes.put(cf,e,IntegerFormat(4,10),bytes.fromhex('00000001'));notes.close()
        identity[1]=0x5000
        new,e,original=self.function(base=0x5000,index=3,text='dword_00005020 = ')
        fresh=self.ui.PseudocodeNotes(self.mods['ida_hexrays'],store);fresh.hooks.func_printed(new)
        self.assertIn('BE32(1)',new.get_pseudocode()[0].line);fresh.close()

    def test_two_databases_at_the_same_ea_do_not_share_notes(self):
        store,_=self.display_store();notes=self.ui.PseudocodeNotes(self.mods['ida_hexrays'],store);functions=[]
        for dbid in (0,1):
            self.mods['ida_ida'].get_dbctx_id.return_value=dbid
            cf,expr,original=self.function()
            notes.put(cf,expr,IntegerFormat(4,10),bytes.fromhex('00000001'));functions.append(cf)
        notes.clear_database(1)
        self.assertIn('BE32(1)',functions[0].get_pseudocode()[0].line)
        self.assertNotIn((1,0x1000),notes.rendered)
        # Forgetting a closed database only removes text caches, never its saved rules.
        self.assertTrue(store.read(0));notes.close();self.assertFalse(notes.rendered)


if __name__=='__main__':unittest.main()
