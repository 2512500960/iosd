"""Bounded IDB-only protocol clues and one-hop relationships. No target execution."""
import json
from pathlib import Path
import re

import ida_bytes
import ida_funcs
import ida_idaapi
import ida_idp
import ida_name
import ida_segment
import ida_ua
import ida_xref
import idautils
import idc

from .ida_adapter import IDBMemory, identity, segments
from .memory import MemoryReadError
from .protocols import protocol_query, match_kind, subsystem_seeds, investigation_plan


def default_subsystems(current):
    path = Path(__file__).resolve().parents[1]/'profiles'/'subsystems_26_01_02.json'
    if not path.is_file():return None
    model = json.loads(path.read_text(encoding='utf-8'))
    return model if model['input_md5'].lower() == current['input_md5'].lower() else None


def location(ea, base):
    seg = ida_segment.getseg(ea)
    if seg is None:return {'ea': ea, 'rva': None, 'location': 'unmapped', 'segment': None}
    name = ida_segment.get_segm_name(seg)
    debug = getattr(ida_segment, 'SFL_DEBUG', None)
    if debug is None or seg.flags & debug:kind = 'debugger_or_unclassified_segment'
    elif name == 'extern':kind = 'external_symbol_not_implementation'
    elif seg.perm & ida_segment.SEGPERM_EXEC:kind = 'idb_image_code'
    else:kind = 'idb_image_data'
    return {'ea': ea, 'rva': ea-base if kind.startswith('idb_image_') and ea >= base else None,
            'location': kind, 'segment': name}


def collect_protocol(query, model=None, cancelled=lambda: False, max_names=1_000_000,
                     max_bytes=64*1024*1024, max_hits=2000):
    query = protocol_query(query);current = identity();base = current['imagebase']
    if not (1 <= max_names <= 2_000_000 and 0 <= max_bytes <= 512*1024*1024 and 1 <= max_hits <= 10000):
        raise ValueError('Protocol scan limits out of range')
    model = model if model is not None else default_subsystems(current)
    seeds = subsystem_seeds(model, current, query) if model else []
    rows = [];faults = [];coverage = {'names_seen': 0, 'bytes_attempted': 0, 'bytes_read': 0,
        'name_limit_reached': False, 'byte_limit_reached': False, 'hit_limit_reached': False,
        'cancelled': False, 'scanned_ranges': [], 'subsystem_index_loaded': model is not None}
    for i, (ea, name) in enumerate(idautils.Names()):
        if i >= max_names:coverage['name_limit_reached'] = True;break
        if i % 256 == 0 and cancelled():coverage['cancelled'] = True;break
        coverage['names_seen'] += 1
        kind = match_kind(name, query)
        if not kind:continue
        func = ida_funcs.get_func(ea)
        rows.append({'kind': 'function_name' if func and func.start_ea == ea else 'data_or_import_name',
                     'name': name, 'match': kind, **location(ea, base),
                     'evidence': 'IDA name; may be analyst-assigned; packet role unverified'})
        if len(rows) >= max_hits:coverage['hit_limit_reached'] = True;break
    memory = IDBMemory();printable = re.compile(rb'[\x20-\x7e]{3,2048}\x00')
    needle = query.encode('ascii')
    for segment in segments():
        if coverage['cancelled'] or coverage['hit_limit_reached']:break
        if segment['permissions'] & (ida_segment.SEGPERM_EXEC | ida_segment.SEGPERM_WRITE):continue
        if location(segment['address'], base)['location'] != 'idb_image_data':continue
        for start in range(segment['address'], segment['end'], 65536):
            if cancelled():coverage['cancelled'] = True;break
            budget = max_bytes-coverage['bytes_attempted']
            size = min(65536+2048, segment['end']-start, budget)
            if size <= 0:coverage['byte_limit_reached'] = True;break
            coverage['bytes_attempted'] += size
            try:data = memory.read(start, size)
            except MemoryReadError as exc:
                faults.append({'ea': start, 'size': size, 'error': str(exc)});continue
            coverage['bytes_read'] += len(data)
            ranges = coverage['scanned_ranges']
            if ranges and ranges[-1]['end_ea'] >= start and ranges[-1]['segment'] == segment['name']:
                ranges[-1]['end_ea'] = max(ranges[-1]['end_ea'], start+size)
            else:ranges.append({'start_ea': start, 'end_ea': start+size, 'segment': segment['name']})
            for match in printable.finditer(data):
                if match.start() >= 65536 or needle not in match[0].lower():continue
                text = match[0][:-1].decode('ascii')
                rows.append({'kind': 'source_path_literal' if ('/' in text or '\\' in text) and '.c' in text else 'literal',
                             'name': text, 'match': match_kind(text, query), **location(start+match.start(), base),
                             'evidence': 'bounded NUL-terminated printable fragment in saved IDB; not compilation-unit ownership'})
                if len(rows) >= max_hits:coverage['hit_limit_reached'] = True;break
            if coverage['hit_limit_reached']:break
        if coverage['byte_limit_reached']:break
    return {'schema_version': 1, 'kind': 'protocol_investigation', 'identity': current, 'protocol': query,
            'source': 'saved_idb_only', 'subsystems': seeds, 'candidates': rows, 'coverage': coverage,
            'faults': faults, 'plan': investigation_plan(query), 'packet_path_verified': False}


def relationships(ea, cancelled=lambda: False, max_items=20000, max_refs=2000):
    if not 1 <= max_items <= 100000 or not 1 <= max_refs <= 10000:raise ValueError('Relationship limits out of range')
    current = identity();base = current['imagebase'];rows = [];sites = 0;limited = False;stopped = False
    for i, ref in enumerate(idautils.XrefsTo(ea)):
        if i >= max_refs:limited = True;break
        if cancelled():stopped = True;break
        func = ida_funcs.get_func(ref.frm)
        rows.append({'kind': 'incoming_code_xref' if ref.iscode else 'incoming_data_xref',
                     'site': location(ref.frm, base), 'target': location(ea, base),
                     'function_ea': func.start_ea if func else None, 'xref_type': ref.type,
                     'evidence': 'IDA xref; incoming code can be call or jump, data can be a callback/table candidate'})
    function = ida_funcs.get_func(ea)
    if function and not stopped:
        for i, site in enumerate(idautils.FuncItems(function.start_ea)):
            if i >= max_items or len(rows) >= max_refs:limited = True;break
            if i % 128 == 0 and cancelled():stopped = True;break
            sites += 1;insn = ida_ua.insn_t()
            if not ida_ua.decode_insn(insn, site):continue
            is_call = ida_idp.is_call_insn(insn);direct = False
            for ref in idautils.XrefsFrom(site):
                if ref.type == ida_xref.fl_F:continue
                target_func = ida_funcs.get_func(ref.to)
                if is_call and ref.type in (ida_xref.fl_CN, ida_xref.fl_CF):
                    kind = 'direct_call';direct = True
                elif not ref.iscode and target_func and target_func.start_ea == ref.to:
                    kind = 'code_pointer_reference_candidate'
                elif ref.iscode and target_func and target_func.start_ea != function.start_ea:
                    kind = 'cross_function_code_transfer_candidate'
                elif not ref.iscode:kind = 'indirect_call_slot_candidate' if is_call else 'data_reference'
                else:continue
                rows.append({'kind': kind, 'site': location(site, base), 'target': location(ref.to, base),
                             'name': ida_name.get_name(ref.to), 'xref_type': ref.type,
                             'evidence': 'IDA instruction/xref; function-pointer argument, binding and execution conditions require review'})
                if len(rows) >= max_refs:limited = True;break
            if is_call and not direct and len(rows) < max_refs:
                rows.append({'kind': 'unresolved_indirect_call', 'site': location(site, base), 'target': None,
                             'expression': idc.generate_disasm_line(site, 0),
                             'evidence': 'No direct-call xref; target/registration/state constraints remain unknown'})
            if limited:break
    return {'identity': current, 'query': location(ea, base), 'function_ea': function.start_ea if function else None,
            'rows': rows, 'coverage': {'instruction_items_seen': sites, 'limited': limited, 'cancelled': stopped},
            'limits': ['One hop only; no automatic transitive ownership or packet-flow inference.',
                       'IDA xrefs may omit encoded pointers, dynamic bindings, unresolved code and data references.']}
