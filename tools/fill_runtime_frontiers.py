"""Follow newly discovered missing grammar pages, retaining limits and failures."""
import argparse,json
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from iosd_helper.runtime_grammar import CapturedPages,reconstruct_runtime_graph,observe_slot_bindings
from capture_debugger_memory import capture
from ida_mcp_client import McpClient


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('url');p.add_argument('static_graph');p.add_argument('--pages',action='append',required=True)
    p.add_argument('--cache-capture',action='append',default=[]);p.add_argument('--linkage',required=True)
    p.add_argument('--output',required=True);p.add_argument('--max-rounds',type=int,default=12)
    p.add_argument('--profile',default='profiles/lifecycle_api_26_01_02.json')
    p.add_argument('--anchors',default='reports/runtime-anchors-20261029.json')
    a=p.parse_args();out=Path(a.output);out.mkdir(parents=True,exist_ok=True)
    report=json.loads(Path(a.static_graph).read_text(encoding='utf-8'));profile=json.loads(Path(a.profile).read_text(encoding='utf-8'))
    linkage=json.loads(Path(a.linkage).read_text(encoding='utf-8'));anchors=json.loads(Path(a.anchors).read_text(encoding='utf-8'))
    files=[f for folder in a.pages for f in sorted(Path(folder).glob('pages-*.json'))]+[Path(f) for f in a.cache_capture]
    captures=[json.loads(f.read_text(encoding='utf-8')) for f in files]
    captures.extend(json.loads(f.read_text(encoding='utf-8')) for f in sorted(out.glob('pages-*.json')))
    if {(c['input_md5'],c['runtime_base']) for c in captures}!={(anchors['input_md5'],anchors['expected_idb_base'])}:raise ValueError('Capture identity/base mismatch')
    base=anchors['expected_idb_base'];memory=CapturedPages(captures);del captures
    c=McpClient(a.url,timeout=20);c.initialize();attempted=set();rounds=[];batch=0;failures=[]
    for round_index in range(a.max_rounds+1):
        memory.missing_pages.clear()
        g=reconstruct_runtime_graph(memory,report['graph'],base,linkage,keyword_gates=profile['runtime'].get('keyword_privilege_gates',[]),
            option_getters=profile['runtime'].get('option_getters',{}),predicate_models=profile['runtime'].get('predicate_models',{}))
        observe_slot_bindings(memory,report['graph'],base,linkage,int(profile['runtime']['link_sentinel_rva'],0))
        missing={va for va in memory.missing_pages if 0x10000<=va<0x800000000000}
        fresh=sorted(missing-attempted)
        row={'round':round_index,'nodes':len(g['nodes']),'missing_pages':len(missing),'new_pages':len(fresh),'graph_stop':g['stop_reason']};rounds.append(row)
        print(json.dumps(row),flush=True)
        (out/'closure-progress.json').write_text(json.dumps({'rounds':rounds,'failures':failures,'remaining':sorted(missing),'atomic_snapshot':False},indent=2),encoding='utf-8')
        if not fresh or round_index==a.max_rounds:break
        for start in range(0,len(fresh),16):
            ranges=[{'runtime_va':va,'size':65536,'label':'newly-discovered-grammar-frontier'} for va in fresh[start:start+16]]
            req={'ranges':ranges,'lists':[],'states':[],'max_seconds':7}
            dest=out/('pages-%04d.json'%batch)
            if dest.exists():raise ValueError('Use a new output directory; batch already exists')
            snap=capture(c,req,anchors,dest);snap['request']=req
            dest.write_text(json.dumps(snap,ensure_ascii=False),encoding='utf-8');batch+=1
            part=CapturedPages([snap]);memory.blocks.update(part.blocks);memory.starts=sorted(memory.blocks)
            for r in snap['ranges']:
                attempted.add(r['runtime_va'])
                if 'error' in r:failures.append(r)
    print('Saved closure progress',out/'closure-progress.json',flush=True)


if __name__=='__main__':main()
