"""Portable skill CLI: discover IDA MCP, collect saved IDB/paused memory, or read ELF core.

All IDA operations use MCP. Core decoding runs locally. No target execution or
IDA UI hooks; endpoint, session and output files are explicit and portable.
"""
import argparse
import base64
from dataclasses import asdict
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import sys
import uuid
import zlib

ROOT = next(p for p in (Path(__file__).resolve().parent,Path(__file__).resolve().parent.parent)
            if (p/'iosd_helper').is_dir())
sys.path.insert(0,str(ROOT));sys.path.insert(0,str(ROOT/'tools'))
from ida_mcp_client import McpClient
from validate_ida_backend import tool_result
from iosd_helper.memory import ElfCoreMemory, MemoryReadError
from iosd_helper.mcp_runtime import validated_ranges, integer

EXCLUDED = {'ui','integer_ui','project_ui','protocol_ui','graph_view'}


def atomic_json(path, value):
    path = Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    temporary = path.with_name(path.name+'.'+uuid.uuid4().hex+'.tmp')
    temporary.write_text(json.dumps(value,ensure_ascii=False,indent=2),encoding='utf-8');temporary.replace(path)


def runtime_sources():
    return {p.stem:p.read_text(encoding='utf-8') for p in sorted((ROOT/'iosd_helper').glob('*.py')) if p.stem not in EXCLUDED}


def discover_tools(client):
    tools=[];seen=set();cursor=None
    for _ in range(32):
        page=client.send('tools/list',{'cursor':cursor} if cursor else {})
        tools.extend(page['tools']);cursor=page.get('nextCursor')
        if not cursor:return {'tools':tools}
        if cursor in seen:raise ValueError('MCP tool discovery cursor repeated')
        seen.add(cursor)
    raise ValueError('MCP tool discovery exceeded 32 pages')


def remote_code(request):
    """Load approved source modules transiently; imports stay lazy and run in one globals dict."""
    sources = runtime_sources()
    packed = base64.b64encode(zlib.compress(json.dumps(sources).encode())).decode()
    prefix = '_iosd_skill_'+uuid.uuid4().hex
    code = '''import sys,types,json,base64,zlib,importlib,importlib.abc,importlib.util
sources=json.loads(zlib.decompress(base64.b64decode(PACKED)))
prefix=PREFIX
class SourceLoader(importlib.abc.MetaPathFinder,importlib.abc.Loader):
 def find_spec(self,fullname,path=None,target=None):
  if fullname.startswith(prefix+'.') and fullname[len(prefix)+1:] in sources:
   return importlib.util.spec_from_loader(fullname,self)
 def create_module(self,spec):return None
 def exec_module(self,module):
  name=module.__name__[len(prefix)+1:]
  module.__file__='<iosd-skill/'+name+'.py>'
  exec(compile(sources[name],module.__file__,'exec'),module.__dict__)
pkg=types.ModuleType(prefix);pkg.__path__=[];sys.modules[prefix]=pkg
finder=SourceLoader();sys.meta_path.insert(0,finder)
try:
 runtime=importlib.import_module(prefix+'.mcp_runtime')
 result=runtime.run(REQUEST)
 print(json.dumps(result,ensure_ascii=True))
finally:
 sys.meta_path.remove(finder)
 for name in list(sys.modules):
  if name==prefix or name.startswith(prefix+'.'):sys.modules.pop(name,None)
'''.replace('PACKED',repr(packed)).replace('PREFIX',repr(prefix)).replace('REQUEST',repr(request))
    return 'exec('+repr(code)+', {})',hashlib.sha256(json.dumps(sources,sort_keys=True).encode()).hexdigest()


def core_read(core_path, ranges):
    ranges = validated_ranges(ranges)
    if any(r['space']!='runtime' for r in ranges):raise ValueError('Core reads require runtime VAs, not unverified image RVAs')
    result = {'schema_version':1,'source':'elf_core','core_path':str(Path(core_path).resolve()),
              'image_identity_verified':False,'atomic_snapshot':False,'ranges':[],'gaps':[],
              'target_execution_changed':False,'scope':'Captured core file only; PT_LOAD mappings do not prove binary identity or atomicity'}
    with ElfCoreMemory(core_path) as memory:
        result['mappings']=[asdict(s) for s in memory.segments]
        for spec in ranges:
            row=dict(spec);result['ranges'].append(row)
            try:row['raw_hex']=memory.read(spec['va'],spec['size']).hex()
            except MemoryReadError as exc:
                row['error']=str(exc);result['gaps'].append(dict(row))
    return result


def invoke(url, request, session_path, output, confirm_idle=False, timeout=20):
    if not url:raise ValueError('Provide --url or IOSD_IDA_MCP_URL; no endpoint is hardcoded')
    output = Path(output);session_path = Path(session_path) if session_path else output
    pending = session_path.with_suffix(session_path.suffix+'.pending.json')
    if pending.exists():
        if not (confirm_idle and request['operation']=='status'):
            raise ValueError('A previous request is unresolved. Confirm IDA is idle, then run status --confirm-idle; no automatic retry is sent')
        # Preserve the previous request record even when the operator confirms a new idle session.
        pending.replace(pending.with_name(pending.name+'.'+uuid.uuid4().hex+'.resolved'))
    code, source_sha = remote_code(request)
    marker = {'request_id':uuid.uuid4().hex,'started_utc':datetime.now(timezone.utc).isoformat(),
              'operation':request['operation'],'endpoint':url,'request_sha256':hashlib.sha256(code.encode()).hexdigest(),
              'collector_sha256':source_sha,'ida_work_may_continue_after_timeout':True}
    pending.parent.mkdir(parents=True,exist_ok=True)
    # Exclusive creation blocks another CLI using this same session. Interactive IDA work
    # and other clients are outside this lock, so coordinate with the operator too.
    with pending.open('x',encoding='utf-8') as stream:json.dump(marker,stream)
    client = McpClient(url,timeout=timeout)
    committed = False
    try:
        client.initialize()
        catalogue = discover_tools(client)
        if 'py_eval' not in {t['name'] for t in catalogue['tools']}:
            raise ValueError('This helper requires py_eval; use the skill capability adapter for typed-only MCP servers')
        result = json.loads(tool_result(client,code))
        result['collector_sha256']=source_sha
        atomic_json(output,result);committed = True
        return result
    finally:
        if committed:pending.unlink()
        # Leave the pending record after any uncertain failure. No cleanup/retry is
        # queued into IDA; the server may still be running despite client timeout.


def parser():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--url',default=os.environ.get('IOSD_IDA_MCP_URL'))
    sub=p.add_subparsers(dest='operation',required=True)
    d=sub.add_parser('discover',help='List MCP capabilities; does not request IDA analysis');d.add_argument('--output',required=True)
    s=sub.add_parser('status',help='Capture a fresh image/base/debugger session after IDA is ready')
    s.add_argument('--output',required=True);s.add_argument('--confirm-idle',action='store_true')
    for name in ('read','function','protocol','relationships','subsystems'):
        q=sub.add_parser(name);q.add_argument('--session',required=True);q.add_argument('--output',required=True)
        if name in ('function','relationships'):q.add_argument('--rva',required=True,type=integer)
        if name=='function':q.add_argument('--max-size',type=int,default=16384)
        if name=='protocol':
            q.add_argument('--query',required=True);q.add_argument('--max-names',type=int,default=200000)
            q.add_argument('--max-bytes',type=int,default=8*1024*1024);q.add_argument('--max-hits',type=int,default=500)
            q.add_argument('--resume',help='Previous protocol capture; continue without overwriting it')
        if name=='subsystems':q.add_argument('--pointer-mode',required=True,choices=('little','big','mask_then_swap','swap_then_mask'))
        if name=='read':
            q.add_argument('--request',required=True,help='JSON with source, ranges, and for debugger runtime_base + anchors')
    c=sub.add_parser('core-read',help='Offline ELF core ranges; never connects to MCP')
    c.add_argument('--core',required=True);c.add_argument('--request',required=True);c.add_argument('--output',required=True)
    return p


def main(argv=None):
    args=parser().parse_args(argv)
    if args.operation=='discover':
        if not args.url:raise ValueError('Provide --url or IOSD_IDA_MCP_URL')
        client=McpClient(args.url,timeout=8);init=client.initialize();result=discover_tools(client)
        atomic_json(args.output,{'initialize':init,'result':result})
        print(json.dumps({'server':init.get('serverInfo'),'tools':[t['name'] for t in result['tools']]}));return 0
    if args.operation=='core-read':
        req=json.loads(Path(args.request).read_text(encoding='utf-8'))
        result=core_read(args.core,req['ranges']);atomic_json(args.output,result)
    else:
        request={'operation':args.operation}
        if args.operation!='status':
            session=json.loads(Path(args.session).read_text(encoding='utf-8'))
            if session.get('kind')!='iosd_mcp_session':raise ValueError('Use a status capture as --session')
            if args.operation=='read':
                request.update(json.loads(Path(args.request).read_text(encoding='utf-8')))
                request['ranges']=validated_ranges(request['ranges'])
            for key in ('rva','max_size','query','max_names','max_bytes','max_hits','pointer_mode'):
                if hasattr(args,key):request[key]=getattr(args,key)
            if args.operation=='protocol':
                from iosd_helper.protocols import match_kind,protocol_query
                request['query']=protocol_query(args.query)
                if args.resume:
                    previous_path=Path(args.resume)
                    if previous_path.resolve()==Path(args.output).resolve():raise ValueError('Write resumed protocol evidence to a new output file')
                    previous=json.loads(previous_path.read_text(encoding='utf-8'))
                    if (previous.get('operation')!='protocol' or not previous.get('identity_stable') or
                            previous.get('identity')!=session['identity']):
                        raise ValueError('Protocol continuation requires the same verified IDA session')
                    page=previous['result']
                    if page.get('protocol')!=args.query.strip().lower() or not page.get('cursor'):
                        raise ValueError('Previous protocol scan is complete or belongs to another query')
                    request['cursor']=page['cursor']
                    request['continuation_from_sha256']=hashlib.sha256(previous_path.read_bytes()).hexdigest()
                path=ROOT/'profiles/subsystems_26_01_02.json'
                if path.is_file():
                    model=json.loads(path.read_text(encoding='utf-8'))
                    if model['input_md5']==session['identity']['input_md5']:
                        model['subsystems']=[r for r in model['subsystems'] if match_kind(r['name'],args.query)]
                        request['subsystem_model']=model
            # Request files cannot substitute the session identity or select another operation.
            request['operation']=args.operation;request['identity']=session['identity']
        result=invoke(args.url,request,getattr(args,'session',None),args.output,getattr(args,'confirm_idle',False))
    print(json.dumps({'saved':str(Path(args.output).resolve()),'kind':result.get('kind',result.get('source')),
                      'gaps':len(result.get('gaps',[]))},ensure_ascii=True))
    return 0


if __name__=='__main__':
    try:raise SystemExit(main())
    except (OSError,ValueError,RuntimeError) as exc:
        print('iosd-analysis: '+str(exc),file=sys.stderr);raise SystemExit(2)
