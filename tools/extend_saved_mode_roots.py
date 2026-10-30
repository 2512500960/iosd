"""Decode new mode roots from the original saved pages, stopping at known nodes."""
import argparse,hashlib,json
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from iosd_helper.runtime_grammar import CapturedPages,reconstruct_runtime_graph


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('nodes','summary','modes','dispatch','profile','output'):p.add_argument('--'+name,type=Path,required=True)
    a=p.parse_args();summary=json.loads(a.summary.read_text(encoding='utf-8'));modes=json.loads(a.modes.read_text(encoding='utf-8'))
    identity=summary['identity'];base=identity['imagebase']
    if modes['identity']['input_md5']!=identity['input_md5']:raise ValueError('Mode/root image identity differs')
    existing=set()
    with a.nodes.open(encoding='utf-8') as stream:
        for line in stream:existing.add(json.loads(line)['address'])
    roots={m['root_rva'] for m in modes['modes'] if m.get('root_rva') is not None}
    def captures():
        for spec in summary['source_files']:
            path=Path(spec['path'])
            if hashlib.sha256(path.read_bytes()).hexdigest()!=spec['sha256']:raise ValueError('Capture hash differs')
            capture=json.loads(path.read_text(encoding='utf-8'))
            if capture['input_md5']!=identity['input_md5'] or capture['runtime_base']!=base:raise ValueError('Capture identity/base differs')
            yield capture
    memory=CapturedPages(captures())
    if memory.conflicts:raise ValueError('Historical capture conflicts; retain separate sources')
    actions=[]
    for line in a.dispatch.open(encoding='utf-8'):
        row=json.loads(line);actions.append({'opcode':row['opcode'],'name':row['name'],
            'address':row['entry_va']-base,'function':row['static_function_va']-base if row['static_function_va'] else 0})
    profile=json.loads(a.profile.read_text(encoding='utf-8'))
    graph=reconstruct_runtime_graph(memory,{'nodes':[{'address':rva} for rva in sorted(roots)],
        'action_registry':actions,'mode_definitions':[]},base,{'lists':[]},max_nodes=100000,
        keyword_gates=profile['runtime'].get('keyword_privilege_gates',[]),
        option_getters=profile['runtime'].get('option_getters',{}),predicate_models=profile['runtime'].get('predicate_models',{}),
        stop_node_addresses=existing)
    a.output.mkdir(parents=True,exist_ok=True)
    with (a.output/'new-nodes.jsonl').open('w',encoding='utf-8') as out:
        for row in graph['nodes']:
            row['remaining_uncertainties']=list(row.get('remaining_uncertainties',[]))
            if row.get('status')=='unresolved':row['remaining_uncertainties'].append('unread_or_unclassified_record')
            if not row.get('path_semantics'):row['remaining_uncertainties'].append('action_semantics_unresolved')
            if row.get('semantic_error'):row['remaining_uncertainties'].append('descriptor_decode_error')
            out.write(json.dumps(row,ensure_ascii=False)+'\n')
    result={'identity':identity,'source':'Original historical capture series; no current memory/IDB substitution',
        'roots':len(roots),'roots_already_in_graph':sum(base+r in existing for r in roots),
        'new_nodes':len(graph['nodes']),'reused_node_addresses':graph['reused_existing_node_addresses'],
        'unread_nodes':sum(n['status']=='unresolved' for n in graph['nodes']),
        'missing_pages_captured_va':sorted(memory.missing_pages),'pending_addresses':graph['pending_addresses'],
        'stop_reason':graph['stop_reason'],'capture_files':summary['source_files']}
    (a.output/'summary.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ('reused_node_addresses','capture_files','missing_pages_captured_va','pending_addresses')}),flush=True)


if __name__=='__main__':main()
