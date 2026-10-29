"""Collect reviewed runtime lists in bounded batches, preserving every frontier."""
import argparse
import json
from pathlib import Path

from capture_debugger_memory import capture
from ida_mcp_client import McpClient


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('url');p.add_argument('--request',required=True);p.add_argument('--anchors',default='reports/runtime-anchors-20261029.json')
    p.add_argument('--output',required=True);p.add_argument('--seed');p.add_argument('--max-batches',type=int,default=20)
    a=p.parse_args()
    request=json.loads(Path(a.request).read_text(encoding='utf-8'))
    anchors=json.loads(Path(a.anchors).read_text(encoding='utf-8'))
    output=Path(a.output);output.mkdir(parents=True,exist_ok=True)
    client=McpClient(a.url,timeout=20);client.initialize()
    result={'lists':[],'batches':[],'atomic_snapshot':False,'continuity':'Head checked per batch; resume/re-stop epoch is not tracked','all_lists_terminated':False}
    seed=json.loads(Path(a.seed).read_text(encoding='utf-8')) if a.seed else None
    count=0
    for layout in request['lists']:
        chain={'name':layout['name'],'nodes':[],'frontiers':[],'terminated_at_null':False}
        result['lists'].append(chain);seen=set();spec=dict(layout)
        initial=next((s for s in seed.get('lists',[]) if s['name']==layout['name']),None) if seed else None
        while count<a.max_batches:
            if initial and initial.get('nodes'):
                part=initial;initial=None;path=str(Path(a.seed).resolve())
            else:
                req={**request,'lists':[spec],'states':[],'ranges':[],'max_nodes':4096,'max_seconds':7,'preserve_cache_blocks':False}
                path=output/('batch-%03d.json'%count)
                snap=capture(client,req,anchors,path)
                path.write_text(json.dumps(snap,ensure_ascii=False,indent=2),encoding='utf-8')
                part=snap['lists'][0];path=str(path.resolve());count+=1
                if snap['errors']:chain['errors']=snap['errors']
            result['batches'].append(path)
            chain['head_raw_hex']=part.get('head_raw_hex')
            repeated=False
            for node in part['nodes']:
                if node['address'] in seen:
                    chain['frontiers']=[{'address':node['address'],'reason':'cycle_across_batches'}];repeated=True;break
                seen.add(node['address']);chain['nodes'].append(node)
            if not repeated:
                chain['frontiers']=part['frontiers']
                chain['terminated_at_null']=part.get('terminated_at_null',False)
                if part['nodes'] and not part['frontiers']:
                    last=bytes.fromhex(part['nodes'][-1]['raw_hex'])
                    chain['terminated_at_null']=(int.from_bytes(last[:8],'big')&0x7fffffffffffffff)==0
            print(json.dumps({'list':chain['name'],'nodes':len(chain['nodes']),'frontiers':chain['frontiers'],'terminated_at_null':chain['terminated_at_null']}),flush=True)
            (output/'lists.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
            if repeated or chain['terminated_at_null'] or chain.get('errors'):break
            if not part['nodes'] or not part['frontiers']:break
            frontier=part['frontiers'][0]
            if frontier['reason'] not in ('Capture time budget reached','node_limit'):break
            spec.update(start_runtime_va=frontier['address'],expected_head_raw_hex=part['head_raw_hex'])
    result['all_lists_terminated']=all(s['terminated_at_null'] for s in result['lists'])
    (output/'lists.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    print('Saved',output/'lists.json',flush=True)


if __name__=='__main__':main()
