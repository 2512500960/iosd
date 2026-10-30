"""Classify a fixed unassigned-EOL cohort using additional mode roots and registration evidence."""
import argparse,gzip,hashlib,json
from collections import Counter,defaultdict
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from iosd_helper.unbound_cli import restore_node,reference_va,classify_cohort
from tools.export_cli_analysis import public_node,reference


def jsonl(path):
    opener=gzip.open if path.suffix=='.gz' else open
    with opener(path,'rt',encoding='utf-8') as stream:
        for line in stream:
            if line.strip():yield json.loads(line)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('nodes','extra','modes','registrations','slots','identity','layout','output'):
        p.add_argument('--'+name,required=True,type=Path)
    a=p.parse_args();meta=json.loads(a.identity.read_text(encoding='utf-8'));mode_data=json.loads(a.modes.read_text(encoding='utf-8'))
    base=meta['identity']['imagebase'];layout=json.loads(a.layout.read_text(encoding='utf-8'))
    if mode_data['identity']['input_md5']!=meta['identity']['input_md5'] or layout['identity']['input_md5']!=meta['identity']['input_md5']:
        raise ValueError('Unbound/mode/layout identities differ')
    if hashlib.sha256(a.nodes.read_bytes()).hexdigest()!=meta['artifact_sha256'][a.nodes.name]:raise ValueError('Baseline node hash differs')
    old=[restore_node(n,base) for n in jsonl(a.nodes)]
    cohort={n['address'] for n in old if n.get('path_semantics') in ('terminal','parameter_terminal') and not n.get('semantic_error') and not n.get('connected_mode_candidates')}
    nodes={n['address']:n for n in old}
    extra=[]
    for row in jsonl(a.extra):
        node=restore_node(row,base)
        if node['address'] not in nodes:extra.append(node);nodes[node['address']]=node
    with gzip.open(a.registrations,'rt',encoding='utf-8') as stream:registrations=json.load(stream)['records']
    if a.slots.suffix=='.gz':
        with gzip.open(a.slots,'rt',encoding='utf-8') as stream:slot_data=json.load(stream)
        slots=[{'source':s['source'],'record_va':reference_va(s['record'],base),
            'key':reference_va(s['key'],base),'anchor':reference_va(s['anchor'],base),'type':s['type'],'frontiers':s['frontiers']} for s in slot_data['records']]
    else:slots=list(jsonl(a.slots))
    graph={'nodes':list(nodes.values())}
    print(json.dumps({'nodes':len(nodes),'cohort':len(cohort),'modes':len(mode_data['modes']),'stage':'projecting'}),flush=True)
    result=classify_cohort(graph,mode_data['modes'],mode_data['configuration_ancestry'],cohort,registrations,slots,base,
        static_link_creations=mode_data.get('static_link_creations',[]))
    a.output.mkdir(parents=True,exist_ok=True)
    ranges=[(s['address'],s['address']+s['memory_size']) for s in layout['load_segments']]
    def write(name,data):(a.output/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    write('mode-coverage.json',result['mode_summary'])
    write('registration-gaps.json',result['registration_gaps'])
    write('static-link-gaps.json',result['static_slot_creation_gaps'])
    with gzip.open(a.output/'terminals.jsonl.gz','wt',encoding='utf-8') as stream:
        for row in result['records']:
            row['eol']=reference(row.pop('eol_va'),base,ranges);row['handler']=reference(row.pop('handler_va'),base,ranges)
            stream.write(json.dumps(row,ensure_ascii=False,separators=(',',':'))+'\n')
    with gzip.open(a.output/'extra-nodes.jsonl.gz','wt',encoding='utf-8') as stream:
        for row in extra:stream.write(json.dumps(public_node(row,base,ranges),ensure_ascii=False,separators=(',',':'))+'\n')
    with gzip.open(a.output/'slots.json.gz','wt',encoding='utf-8') as stream:
        json.dump({'identity':meta['identity'],'source':'Historical slot observations; actual activation conditions unresolved',
            'records':[{'source':s.get('source'),'record':reference(s.get('record_va',0),base,ranges),
                'key':reference(s.get('key',0),base,ranges),'anchor':reference(s.get('anchor',0),base,ranges),
                'type':s.get('type'),'frontiers':s.get('frontiers',[])} for s in slots if 'key' in s and 'anchor' in s]},stream,ensure_ascii=False)
    summary={'identity':meta['identity'],'baseline_cohort':len(cohort),'extended_nodes':len(extra),'categories':result['categories'],
        'mode_definitions':len(mode_data['modes']),'mode_roots_in_graph':sum(base+m['root_rva'] in nodes for m in mode_data['modes'] if m.get('root_rva') is not None),
        'mode_projection_limits':sum(m['projection_limited'] for m in result['mode_summary']),
        'candidate_registration_edges':sum(map(len,result['registration_candidate_edges'].values())),
        'static_slot_creation_candidate_edges':sum(map(len,result['static_slot_creation_edges'].values())),
        'graph_sources':'Baseline acquired graph plus historical-page root extension; static mode factory candidates from fresh IDB',
        'conditions_evaluated':False,'scope':result['scope'],
        'input_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (a.nodes,a.extra,a.modes,a.registrations,a.slots)}}
    write('summary.json',summary)
    print(json.dumps(summary),flush=True)


if __name__=='__main__':main()
