"""Read bounded action-consumer decompilations from the matching IDA database."""
import argparse,json
from pathlib import Path
from ida_mcp_client import McpClient
from validate_ida_backend import tool_result


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('url');p.add_argument('static_graph');p.add_argument('--action',action='append',default=[])
    p.add_argument('--rva',action='append',type=lambda value:int(value,0),default=[])
    p.add_argument('--output',required=True);p.add_argument('--max-size',type=int,default=6000)
    a=p.parse_args();out=Path(a.output);out.mkdir(parents=True,exist_ok=True)
    graph=json.loads(Path(a.static_graph).read_text(encoding='utf-8'))
    md5=graph['identity']['input_md5'];oldbase=graph['identity']['imagebase']
    jobs=[{'name':row['name'],'rva':row['function']-oldbase} for row in graph['graph']['action_registry'] if row['name'] in a.action]
    jobs.extend({'name':'rva_%x'%rva,'rva':rva} for rva in a.rva)
    if not jobs:p.error('Select at least one action or function RVA')
    c=McpClient(a.url,timeout=20);c.initialize()
    source='''import json,ida_funcs,ida_nalt
if ida_nalt.retrieve_input_file_md5().hex()!=MD5:raise ValueError('Image mismatch')
base=ida_nalt.get_imagebase();rows=[]
for job in JOBS:
 f=ida_funcs.get_func(base+job['rva'])
 rows.append({**job,'base':base,'size':f.end_ea-f.start_ea if f and f.start_ea==base+job['rva'] else None})
print(json.dumps(rows))
'''.replace('MD5',repr(md5)).replace('JOBS',repr(jobs))
    rows=json.loads(tool_result(c,source))
    (out/'functions.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
    print(json.dumps(rows),flush=True)
    for row in rows:
        if row['size'] is None or row['size']>a.max_size:continue
        path=out/(row['name']+'.json')
        source='''import json,ida_nalt,ida_hexrays
row=ROW
if ida_nalt.retrieve_input_file_md5().hex()!=MD5 or ida_nalt.get_imagebase()!=row['base']:raise ValueError('Image changed')
cf=ida_hexrays.decompile(row['base']+row['rva'])
if cf is None:raise ValueError('No decompilation')
e={**row,'input_md5':MD5,'code':str(cf)}
with open(OUTPUT,'w',encoding='utf-8') as f:json.dump(e,f,ensure_ascii=False,indent=2)
print(json.dumps({'name':row['name'],'characters':len(e['code'])}))
'''.replace('ROW',repr(row)).replace('MD5',repr(md5)).replace('OUTPUT',repr(str(path.resolve())))
        print(tool_result(c,source),flush=True)


if __name__=='__main__':main()
