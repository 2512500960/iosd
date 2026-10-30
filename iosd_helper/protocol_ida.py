"""Bounded IDB-only protocol clues and one-hop relationships. No target execution."""
import json
import hashlib
from pathlib import Path

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
from .protocols import protocol_query, match_kind, subsystem_seeds, investigation_plan
from .protocol_scan import literal_windows


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
                     max_bytes=64*1024*1024, max_hits=2000, cursor=None):
    query = protocol_query(query);current = identity();base = current['imagebase']
    if not (1 <= max_names <= 2_000_000 and 0 <= max_bytes <= 512*1024*1024 and 1 <= max_hits <= 10000):
        raise ValueError('Protocol scan limits out of range')
    model = model if model is not None else default_subsystems(current)
    seeds = subsystem_seeds(model, current, query) if model else []
    selected = [s for s in segments() if not s['permissions'] & (ida_segment.SEGPERM_EXEC | ida_segment.SEGPERM_WRITE)
                and location(s['address'],base)['location']=='idb_image_data']
    signature = hashlib.sha256(json.dumps(selected,sort_keys=True).encode()).hexdigest()
    keys = ('input_md5','imagebase','idb_path')
    indexed = all(callable(getattr(ida_name,name,None)) for name in ('get_nlist_size','get_nlist_ea','get_nlist_name'))
    total = ida_name.get_nlist_size() if indexed else None
    if cursor:
        if (cursor.get('schema_version')!=1 or cursor.get('query')!=query or
                cursor.get('segment_signature')!=signature or
                any(cursor['identity'].get(k)!=current.get(k) for k in keys)):
            raise ValueError('Protocol cursor belongs to a different query/IDB/base/segment layout')
        state = dict(cursor)
        if indexed and state.get('names_total') is not None and state['names_total']!=total:
            raise ValueError('IDA name table changed; begin a fresh protocol scan')
    else:
        state = {'schema_version':1,'query':query,'identity':{k:current.get(k) for k in keys},
                 'segment_signature':signature,'phase':'names','name_index':0,'names_total':total,
                 'names_boundary':None,'literal':None}
    if state['phase'] not in ('names','literals') or state['name_index']<0:
        raise ValueError('Invalid protocol cursor phase/index')
    rows = [];faults = [];coverage = {'names_seen': 0, 'name_start_index':state['name_index'], 'bytes_attempted': 0, 'bytes_read': 0,
        'name_limit_reached': False, 'byte_limit_reached': False, 'hit_limit_reached': False,
        'cancelled': False, 'scanned_ranges': [], 'subsystem_index_loaded': model is not None}
    if state['phase']=='names':
        start = state['name_index'];boundary = state.get('names_boundary')
        boundary_checked = not boundary
        if indexed:
            if start>total:raise ValueError('Protocol name cursor exceeds current table')
            if boundary and start==0:raise ValueError('Protocol cursor has an invalid name boundary')
            if boundary and [ida_name.get_nlist_ea(start-1),ida_name.get_nlist_name(start-1)]!=boundary:
                raise ValueError('IDA name table boundary changed; begin a fresh scan')
            boundary_checked=True
            iterator = ((i,ida_name.get_nlist_ea(i),ida_name.get_nlist_name(i)) for i in range(start,total))
        else:
            iterator = ((i,ea,name) for i,(ea,name) in enumerate(idautils.Names()))
        for i,ea,name in iterator:
            if i<start:
                if i==start-1 and boundary and [ea,name]!=boundary:raise ValueError('IDA name cursor boundary changed')
                if i==start-1:boundary_checked=True
                if i%256==0 and cancelled():coverage['cancelled']=True;break
                continue
            if coverage['names_seen']>=max_names:coverage['name_limit_reached']=True;break
            if coverage['names_seen']%256==0 and cancelled():coverage['cancelled']=True;break
            coverage['names_seen']+=1;state['name_index']=i+1;state['names_boundary']=[ea,name]
            kind = match_kind(name,query)
            if kind:
                func = ida_funcs.get_func(ea)
                rows.append({'kind':'function_name' if func and func.start_ea==ea else 'data_or_import_name',
                             'name':name,'match':kind,**location(ea,base),
                             'evidence':'IDA name; may be analyst-assigned; packet role unverified'})
                if len(rows)>=max_hits:coverage['hit_limit_reached']=True;break
        else:
            if not boundary_checked:raise ValueError('IDA name cursor no longer exists')
            state['phase']='literals'
        if indexed and state['name_index']==total:state['phase']='literals'
    if state['phase']=='literals' and not coverage['cancelled'] and not coverage['hit_limit_reached']:
        scanned = literal_windows(IDBMemory().read,selected,query,state['literal'],max_bytes,max_hits-len(rows),cancelled)
        faults.extend(scanned['faults']);coverage.update(scanned['coverage']);state['literal']=scanned['cursor']
        for row in scanned['rows']:
            text = row['text']
            rows.append({'kind':'source_path_literal' if ('/' in text or '\\' in text) and '.c' in text else 'literal',
                         'name':text,'match':match_kind(text,query),**location(row['ea'],base),
                         'evidence':'bounded NUL-terminated printable string in saved IDB; not compilation-unit ownership'})
        coverage['literal_scope']=scanned['scope']
        if scanned['cursor'] is None:state=None
    coverage['has_more']=state is not None
    return {'schema_version': 1, 'kind': 'protocol_investigation', 'identity': current, 'protocol': query,
            'source': 'saved_idb_only', 'subsystems': seeds, 'candidates': rows, 'coverage': coverage,
            'cursor':state,'faults': faults, 'plan': investigation_plan(query), 'packet_path_verified': False}


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
