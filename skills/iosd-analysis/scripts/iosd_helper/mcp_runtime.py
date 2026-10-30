"""Short-lived IDA collectors for the iosd-analysis skill; return JSON values only.

No hooks, smart-pointer construction, target execution or database annotations.
Importing this module outside IDA is supported for request validation and tests.
"""
from datetime import datetime, timezone
import os
import time

from .memory import MemoryReadError


def integer(value):
    if isinstance(value, bool):raise ValueError('Boolean is not an address/size')
    return int(value, 0) if isinstance(value, str) else int(value)


def utc():return datetime.now(timezone.utc).isoformat()


def identity():
    import ida_nalt, ida_loader, ida_ida, ida_kernwin
    return {'input_md5':ida_nalt.retrieve_input_file_md5().hex(), 'imagebase':ida_nalt.get_imagebase(),
            'idb_path':ida_loader.get_path(ida_loader.PATH_TYPE_IDB), 'input_path':ida_nalt.get_input_file_path(),
            'processor':ida_ida.inf_get_procname(), 'bits':64 if ida_ida.inf_is_64bit() else 32 if ida_ida.inf_is_32bit_exactly() else 16,
            'byteorder':'big' if ida_ida.inf_is_be() else 'little', 'ida_version':ida_kernwin.get_kernel_version(),
            'ida_pid':os.getpid(), 'dbctx_id':ida_ida.get_dbctx_id()}


def guard(expected, suspended=False):
    current = identity()
    keys = ('input_md5','imagebase','idb_path','processor','bits','byteorder','ida_pid','dbctx_id')
    if not expected or any(current.get(key) != expected.get(key) for key in keys):
        raise ValueError('IDA identity/base/session changed; take a new status capture before continuing')
    if suspended:
        import ida_dbg
        if ida_dbg.get_process_state() != ida_dbg.DSTATE_SUSP:
            raise ValueError('Debugger target is not suspended; no automatic suspend/resume is performed')
    return current


def status():
    import ida_dbg, ida_auto, idautils
    state = ida_dbg.get_process_state();modules = [];threads = [];gaps = []
    if state in (ida_dbg.DSTATE_SUSP, ida_dbg.DSTATE_RUN):
        try:
            for i, module in enumerate(idautils.Modules()):
                if i >= 512:gaps.append({'reason':'module_limit'});break
                modules.append({'name':module.name,'base':module.base,'size':module.size})
        except Exception as exc:gaps.append({'reason':'module_enumeration_failed','detail':str(exc)})
        try:
            for i in range(min(ida_dbg.get_thread_qty(),512)):
                threads.append({'tid':ida_dbg.getn_thread(i),'name':ida_dbg.getn_thread_name(i)})
        except Exception as exc:gaps.append({'reason':'thread_enumeration_failed','detail':str(exc)})
    return {'schema_version':1,'kind':'iosd_mcp_session','identity':identity(),'captured_utc':utc(),
            'process_state':state,'suspended':state==ida_dbg.DSTATE_SUSP,'auto_analysis_ready':ida_auto.auto_is_ok(),
            'modules':modules,'threads':threads,'gaps':gaps,'target_memory_read':False,'target_execution_changed':False}


def validated_ranges(ranges):
    if not isinstance(ranges,list) or not 1 <= len(ranges) <= 64:raise ValueError('Supply 1..64 ranges')
    normalized = [];total = 0
    for item in ranges:
        space = item.get('space','image');size = integer(item['size'])
        if space not in ('image','runtime') or not 1 <= size <= 65536:raise ValueError('Invalid range space/size')
        field = 'rva' if space=='image' else 'va'
        if ('va' if field=='rva' else 'rva') in item:raise ValueError('Use RVA or runtime VA, never both')
        address = integer(item[field])
        if address < 0 or address+size > (1<<64):raise ValueError('Range outside 64-bit address space')
        total += size;normalized.append({'space':space,field:address,'size':size,'name':str(item.get('name',''))})
    if total > 1024*1024:raise ValueError('Batch read limit is 1 MiB')
    return normalized


def idb_reader():
    from .ida_adapter import IDBMemory
    return IDBMemory()


def debugger_mapping(request, expected):
    import ida_idd, idautils
    guard(expected,True)
    runtime_base = integer(request['runtime_base']);config = request.get('anchors',{})
    if config.get('input_md5','').lower() != expected['input_md5'].lower():raise ValueError('Runtime anchor MD5 mismatch')
    anchors = config.get('anchors',[])
    if not 1 <= len(anchors) <= 8:raise ValueError('Debugger reads require 1..8 independently selected immutable anchors')
    modules = [{'name':m.name,'base':m.base,'size':m.size} for m in idautils.Modules()]
    basename = expected['input_path'].replace('\\','/').rsplit('/',1)[-1].lower()
    if not any(m['base']==runtime_base and m['name'].replace('\\','/').rsplit('/',1)[-1].lower()==basename for m in modules):
        raise ValueError('Runtime base does not identify the expected main image module')
    memory = idb_reader();verified = []
    # Validate every specification before making any debugger-memory read.
    checks = []
    for anchor in anchors:
        rva = integer(anchor['rva']);raw = bytes.fromhex(anchor['expected_hex'])
        if rva < 0 or not 4 <= len(raw) <= 32:raise ValueError('Anchor must contain 4..32 immutable bytes at a nonnegative RVA')
        if memory.read(expected['imagebase']+rva,len(raw)) != raw:raise ValueError('Anchor differs from saved IDB bytes')
        checks.append((rva,raw))
    for rva, raw in checks:
        guard(expected,True)
        actual = ida_idd.dbg_read_memory(runtime_base+rva,len(raw))
        if actual is None or bytes(actual) != raw:raise ValueError('Debugger anchor mismatch; range reads were not started')
        verified.append({'rva':rva,'raw_hex':raw.hex()})
    return runtime_base, modules, verified


def read_ranges(request, expected):
    ranges = validated_ranges(request['ranges']);source = request.get('source','idb')
    if source not in ('idb','debugger'):raise ValueError('Use idb/debugger here; core reads run outside IDA')
    if source=='idb' and any(r['space']!='image' for r in ranges):raise ValueError('Saved IDB reads use image RVAs only')
    guard(expected,source=='debugger');started = utc();deadline = time.monotonic()+min(10,max(0.1,float(request.get('seconds',5))))
    result = {'source':source,'identity':expected,'ranges':[],'gaps':[],'started_utc':started,
              'atomic_snapshot':False,'target_execution_changed':False,
              'consistency':'Identity/base and stopped state checked per read; resume/re-stop epochs are not tracked'}
    if source=='debugger':
        import ida_idd, idautils
        runtime_base, modules, anchors = debugger_mapping(request,expected)
        result.update(runtime_base=runtime_base,modules=modules,verified_anchors=anchors)
        def read(ea,size):
            raw = ida_idd.dbg_read_memory(ea,size)
            if raw is None or len(raw)!=size:raise MemoryReadError('Debugger range is unreadable or incomplete')
            return bytes(raw)
    else:
        runtime_base = None;memory = idb_reader();read = memory.read
    for spec in ranges:
        row = dict(spec);result['ranges'].append(row)
        if time.monotonic() >= deadline:
            row['error']='time_budget';result['gaps'].append(dict(row));continue
        address = ((runtime_base if source=='debugger' else expected['imagebase'])+spec['rva']) if spec['space']=='image' else spec['va']
        row['address']=address
        try:
            guard(expected,source=='debugger');raw = read(address,spec['size']);guard(expected,source=='debugger')
            row['raw_hex']=raw.hex()
        except (MemoryReadError,ValueError) as exc:
            row['error']=str(exc);result['gaps'].append({k:v for k,v in row.items() if k!='raw_hex'})
    try:
        guard(expected,source=='debugger')
        if source=='debugger':
            now = [{'name':m.name,'base':m.base,'size':m.size} for m in idautils.Modules()]
            if now != modules:raise ValueError('Debugger module map changed during capture')
    except ValueError as exc:result['gaps'].append({'reason':'session_changed','detail':str(exc)})
    result['finished_utc']=utc();result['complete_requested_ranges']=not result['gaps']
    return result


def function(request, expected):
    import ida_funcs, ida_name, ida_hexrays as hr
    ea = expected['imagebase']+integer(request['rva']);f = ida_funcs.get_func(ea)
    if f is None or f.start_ea!=ea:raise ValueError('RVA is not a defined function entry')
    limit = integer(request.get('max_size',16384))
    if not 1 <= limit <= 262144:raise ValueError('Invalid function-size bound')
    row = {'rva':integer(request['rva']),'ea':ea,'name':ida_name.get_name(ea),'size':ida_funcs.calc_func_size(f),'gaps':[]}
    if row['size'] > limit:row['gaps'].append({'reason':'function_size_limit','limit':limit});return row
    if not hr.init_hexrays_plugin():row['gaps'].append({'reason':'decompiler_unavailable'});return row
    # Own only the pointer returned by decompile; never construct one from a borrowed hook argument.
    cf = hr.decompile(ea)
    if cf is None:row['gaps'].append({'reason':'decompile_failed'});return row
    text = str(cf);row['pseudocode']=text[:200000]
    if len(text)>200000:row['gaps'].append({'reason':'text_limit','characters':len(text)})
    return row


def run(request):
    op = request.get('operation')
    if op=='status':return status()
    expected = request.get('identity');guard(expected)
    started = utc()
    if op=='read':result = read_ranges(request,expected)
    elif op=='function':result = function(request,expected)
    elif op=='protocol':
        from .protocol_ida import collect_protocol
        deadline = time.monotonic()+5
        result = collect_protocol(request['query'],model=request.get('subsystem_model'),cancelled=lambda:time.monotonic()>deadline,
            max_names=integer(request.get('max_names',200000)),max_bytes=integer(request.get('max_bytes',8*1024*1024)),
            max_hits=integer(request.get('max_hits',500)),cursor=request.get('cursor'))
    elif op=='relationships':
        from .protocol_ida import relationships
        deadline = time.monotonic()+5
        result = relationships(expected['imagebase']+integer(request['rva']),lambda:time.monotonic()>deadline,
                               max_items=integer(request.get('max_items',10000)),max_refs=integer(request.get('max_refs',500)))
    elif op=='subsystems':
        from .ida_adapter import segments
        from .structures import scan_subsystems
        memory = idb_reader();rows = [];errors = [];partial = False;deadline = time.monotonic()+5
        sections = [s for s in segments() if 'subsys_header_section' in s['name']]
        for segment in sections:
            found,faults,stopped = scan_subsystems(memory,segment['address'],segment['end'],request['pointer_mode'],lambda:time.monotonic()>deadline)
            rows.extend(found);errors.extend(faults);partial |= stopped
            if stopped:break
        result = {'rows':rows,'errors':errors,'partial':partial,'sections':sections,
                  'gaps':[] if sections else [{'reason':'subsystem_section_not_found'}],
                  'scope':'Observed double-magic candidate schema; not a universal format or runtime execution proof'}
    else:raise ValueError('Unsupported collector operation')
    final_gaps = []
    try:guard(expected)
    except ValueError as exc:final_gaps.append({'reason':'session_changed_after_capture','detail':str(exc)})
    return {'schema_version':1,'kind':'iosd_mcp_capture','identity':expected,'operation':op,
            'started_utc':started,'finished_utc':utc(),'result':result,'gaps':final_gaps,
            'continuation_from_sha256':request.get('continuation_from_sha256'),
            'identity_stable':not final_gaps,'target_execution_changed':False}
