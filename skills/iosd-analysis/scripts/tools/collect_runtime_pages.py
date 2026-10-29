"""Read explicit image/heap pages in short batches for offline grammar export."""
import argparse
import json
from pathlib import Path
from capture_debugger_memory import capture
from ida_mcp_client import McpClient


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('url');p.add_argument('--request',required=True);p.add_argument('--output',required=True)
    p.add_argument('--anchors',default='reports/runtime-anchors-20261029.json');p.add_argument('--batch-size',type=int,default=40)
    a=p.parse_args()
    req=json.loads(Path(a.request).read_text(encoding='utf-8'));anchors=json.loads(Path(a.anchors).read_text(encoding='utf-8'))
    out=Path(a.output);out.mkdir(parents=True,exist_ok=True)
    client=McpClient(a.url,timeout=20);client.initialize()
    count=0;failed=[];paths=[]
    for index in range(0,len(req['ranges']),a.batch_size):
        part={**req,'ranges':req['ranges'][index:index+a.batch_size],'lists':[],'states':[],'max_seconds':8,'preserve_cache_blocks':False}
        dest=out/('pages-%04d.json'%(index//a.batch_size))
        if dest.exists():
            snap=json.loads(dest.read_text(encoding='utf-8'))
            if snap.get('request',{}).get('ranges')!=part['ranges']:raise ValueError('Existing page request differs')
        else:
            snap=capture(client,part,anchors,dest)
            dest.write_text(json.dumps(snap,ensure_ascii=False),encoding='utf-8')
        paths.append(str(dest.resolve()))
        count+=sum('raw_hex' in r for r in snap['ranges'])
        failed.extend(r for r in snap['ranges'] if 'error' in r)
        print(json.dumps({'pages_read':count,'total_pages':len(req['ranges']),'failed':len(failed)}),flush=True)
    (out/'manifest.json').write_text(json.dumps({'files':paths,'pages_read':count,'failed':failed,'atomic_snapshot':False,'request':str(Path(a.request).resolve())},indent=2),encoding='utf-8')


if __name__=='__main__':main()
