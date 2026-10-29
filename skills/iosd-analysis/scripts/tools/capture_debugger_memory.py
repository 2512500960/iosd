"""Bounded, read-only paused debugger captures, guarded by image anchors.

Requests contain reviewed list layouts/states and/or explicit image RVA ranges.
Never calls inferior functions, resumes the target, or falls back to IDB bytes.
"""
import argparse
import base64
import hashlib
import json
from pathlib import Path
import uuid
import zlib

from ida_mcp_client import McpClient
from validate_ida_backend import tool_result


def capture(client, request, anchors, direct_output=None):
    root = Path(__file__).resolve().parents[1]
    sources = {name: (root / 'iosd_helper' / (name + '.py')).read_text(encoding='utf-8')
               for name in ('memory', 'addressing', 'runtime_linkage')}
    key = '_iosd_paused_capture_' + uuid.uuid4().hex
    package = key + '_modules'
    remote = '''import types,sys,json,base64,zlib,builtins,datetime,time
import ida_dbg,ida_idd,ida_nalt,idautils
request=REQUEST
anchors=ANCHORS
base=ida_nalt.get_imagebase()
digest=ida_nalt.retrieve_input_file_md5().hex()
def guard():
 if ida_dbg.get_process_state()!=ida_dbg.DSTATE_SUSP:raise ValueError('Target not suspended')
 if ida_nalt.get_imagebase()!=base or ida_nalt.retrieve_input_file_md5().hex()!=digest:raise ValueError('Image identity/base changed')
guard()
if digest!=anchors['input_md5'] or base!=anchors['expected_idb_base']:raise ValueError('Anchor identity/base mismatch')
main=next(iter(idautils.Modules()),None)
if main is None or main.base!=base or 'iosd' not in main.name.lower():raise ValueError('Debugger main module is not matching iosd')
verified=[]
for a in anchors['anchors']:
 guard()
 rva=int(a['rva'],0) if isinstance(a['rva'],str) else a['rva']
 expected=bytes.fromhex(a['expected_hex'])
 raw=ida_idd.dbg_read_memory(base+rva,len(expected))
 if raw is None or bytes(raw)!=expected:raise ValueError('Runtime anchor mismatch: '+a['name'])
 verified.append(a['name'])
package=PACKAGE
loaded=[]
try:
 pkg=types.ModuleType(package);pkg.__path__=[];sys.modules[package]=pkg;loaded.append(package)
 for name,source in SOURCES.items():
  fullname=package+'.'+name
  module=types.ModuleType(fullname);module.__package__=package
  sys.modules[fullname]=module;loaded.append(fullname)
  exec(compile(source,'<iosd-readonly-'+name+'>','exec'),module.__dict__)
 memory_module=sys.modules[package+'.memory']
 deadline=time.monotonic()+request.get('max_seconds',6)
 cache={};read_stats={'debugger_calls':0,'debugger_bytes':0,'cache_hits':0}
 class Memory:
  source='debugger-suspended'
  def read(self,address,size):
   guard()
   if time.monotonic()>deadline:raise memory_module.MemoryReadError('Capture time budget reached')
   chunks=[];end=address+size
   while address<end:
    start=address&~65535
    raw=cache.get(start)
    if raw is None:
     if time.monotonic()>deadline:raise memory_module.MemoryReadError('Capture time budget reached')
     read_stats['debugger_calls']+=1
     raw=ida_idd.dbg_read_memory(start,65536)
     if raw is not None and len(raw)==65536:
      raw=bytes(raw);cache[start]=raw;read_stats['debugger_bytes']+=65536
     else:
      take=min(end-address,65536-(address-start))
      read_stats['debugger_calls']+=1
      part=ida_idd.dbg_read_memory(address,take)
      if part is None or len(part)!=take:raise memory_module.MemoryReadError('Debugger read failed at %#x (%d bytes)'%(address,take))
      read_stats['debugger_bytes']+=take;chunks.append(bytes(part));address+=take;continue
    else:read_stats['cache_hits']+=1
    take=min(end-address,65536-(address-start));chunks.append(raw[address-start:address-start+take]);address+=take
   return b''.join(chunks)
 memory=Memory()
 coordinates=sys.modules[package+'.addressing'].ImageCoordinates(digest,0,base,base)
 normalize=lambda row:{k:(int(v,0) if isinstance(v,str) and k in ('head_rva','rva') else v) for k,v in row.items()}
 specs=[normalize(s) for s in request.get('lists',[])]
 states=[normalize(s) for s in request.get('states',[])]
 image_ranges=request.get('image_rva_ranges',[(0,main.size)])
 result=sys.modules[package+'.runtime_linkage'].capture_runtime_linkage(memory,coordinates,image_ranges,specs,states,request.get('max_nodes',4),guard)
 result['captured_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
 result['capture_key']=KEY
 result['main_module']={'name':main.name,'base':main.base,'size':main.size}
 result['validated_anchors']=verified
 result['image_rva_ranges']=image_ranges
 result['ranges']=[]
 ranges=request.get('ranges',[])
 if len(ranges)>2048 or sum(r['size'] for r in ranges)>64*1024*1024:raise ValueError('Range budget exceeded')
 for spec in ranges:
  rva=int(spec['rva'],0) if isinstance(spec.get('rva'),str) else spec.get('rva',0)
  size=spec['size']
  if not 0<=rva or not 1<=size<=65536:raise ValueError('Invalid range')
  va=spec.get('runtime_va',base+rva)
  if 'runtime_va' in spec and spec.get('rva') is not None:raise ValueError('Use runtime VA or RVA, not both')
  row={'rva':None if 'runtime_va' in spec else rva,'runtime_va':va,'size':size,'label':spec.get('label','')}
  try:row['raw_hex']=memory.read(va,size).hex()
  except memory_module.MemoryReadError as exc:row['error']=str(exc)
  result['ranges'].append(row)
 guard()
 final=next(iter(idautils.Modules()),None)
 if final is None or (final.base,final.name,final.size)!=(main.base,main.name,main.size):raise ValueError('Debugger main module changed')
 result['target_execution_changed']=False
 result['read_stats']=read_stats
 if request.get('preserve_cache_blocks'):
  result['cache_blocks']=[{'runtime_va':ea,'raw_hex':raw.hex()} for ea,raw in sorted(cache.items())]
 direct_path=DIRECT_OUTPUT
 if direct_path is not None:
  with open(direct_path,'w',encoding='utf-8') as stream:json.dump(result,stream,ensure_ascii=False)
  print(json.dumps({'direct_output':direct_path}))
 else:
  packed=base64.b64encode(zlib.compress(json.dumps(result).encode())).decode()
  setattr(builtins,KEY,packed)
  print(json.dumps({'chars':len(packed),'chunks':(len(packed)+7999)//8000}))
finally:
 for name in reversed(loaded):sys.modules.pop(name,None)
'''.replace('DIRECT_OUTPUT',repr(str(Path(direct_output).resolve()) if direct_output else None)).replace('REQUEST', repr(request)).replace('ANCHORS', repr(anchors)).replace('PACKAGE', repr(package)).replace('SOURCES', repr(sources)).replace('KEY', repr(key))
    code = "import types\nmodule=types.ModuleType('_iosd_paused_capture_request')\nexec(%r,module.__dict__)\nresult=None" % remote
    committed = False
    try:
        stdout=tool_result(client, code)
        if direct_output is not None:
            result=json.loads(Path(direct_output).read_text(encoding='utf-8'))
            if result.get('capture_key')!=key:raise ValueError('Direct output capture key mismatch')
            result['collector_sources_sha256']={name:hashlib.sha256(source.encode()).hexdigest() for name,source in sources.items()}
            result['request']=request
            return result
        meta = json.loads(stdout)
        if 'direct_output' in meta:
            result=json.loads(Path(direct_output).read_text(encoding='utf-8'))
            if result['input_md5']!=anchors['input_md5']:raise ValueError('Direct output identity mismatch')
            result['collector_sources_sha256']={name:hashlib.sha256(source.encode()).hexdigest() for name,source in sources.items()}
            result['request']=request
            return result
        if meta['chunks'] > 8192:
            raise ValueError('Transfer budget exceeded')
        parts = [tool_result(client, "import builtins\nprint(getattr(builtins,%r)[%d:%d])" %
                             (key, i*8000, (i+1)*8000)).strip() for i in range(meta['chunks'])]
        packed = ''.join(parts)
        if len(packed) != meta['chars']:
            raise ValueError('Capture transfer length mismatch')
        result = json.loads(zlib.decompress(base64.b64decode(packed)))
        result['collector_sources_sha256'] = {name: hashlib.sha256(source.encode()).hexdigest() for name, source in sources.items()}
        result['request'] = request
        committed = True
        return result
    except Exception as exc:
        raise RuntimeError('Capture failed; no retry/cleanup queued. Recovery key: %s; %s' % (key, exc)) from exc
    finally:
        if committed:
            tool_result(client, "import builtins\nif hasattr(builtins,%r): delattr(builtins,%r)" % (key, key))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('url')
    parser.add_argument('--request', required=True)
    parser.add_argument('--anchors', default='reports/runtime-anchors-20261029.json')
    parser.add_argument('--output', required=True)
    parser.add_argument('--direct-output',action='store_true',help='IDA host shares the same workspace path; verify returned file locally')
    args = parser.parse_args()
    request = json.loads(Path(args.request).read_text(encoding='utf-8'))
    anchors = json.loads(Path(args.anchors).read_text(encoding='utf-8'))
    client = McpClient(args.url, timeout=20)
    client.initialize()
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    result = capture(client, request, anchors, output if args.direct_output else None)
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({'output':str(output),'lists':[{'name':s['name'],'nodes':len(s['nodes']),'frontiers':s['frontiers']} for s in result['lists']],
                      'states':result['states'],'ranges':len(result['ranges']),'errors':result['errors']}, ensure_ascii=True, indent=2))


if __name__ == '__main__':
    main()
