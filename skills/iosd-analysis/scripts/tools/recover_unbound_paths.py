"""Recover mode-local witnesses for the retained EOL cohort; candidate installations stay separate."""
import argparse,gzip,json
from collections import defaultdict
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from iosd_helper.unbound_cli import restore_node,reference_va,registration_edges
from iosd_helper.syntax_paths import recover_mode
from tools.export_cli_analysis import reference
from tools.recover_saved_cli import evidence_value
from tools.analyze_unbound_cli import jsonl


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('nodes','extra','modes','registrations','slots','classification','identity','layout','settings','output'):
        p.add_argument('--'+name,required=True,type=Path)
    p.add_argument('--max-states',type=int,default=500000);p.add_argument('--max-records',type=int,default=200000)
    p.add_argument('--max-terminals',type=int,default=100000)
    a=p.parse_args()
    if not 1<=a.max_states<=1000000 or not 1<=a.max_terminals<=200000 or not 1<=a.max_records<=200000:
        p.error('Bounds: states 1..1000000; terminals/records 1..200000')
    meta=json.loads(a.identity.read_text(encoding='utf-8'));base=meta['identity']['imagebase']
    modes=json.loads(a.modes.read_text(encoding='utf-8'));layout=json.loads(a.layout.read_text(encoding='utf-8'))
    if modes['identity']['input_md5']!=meta['identity']['input_md5'] or layout['identity']['input_md5']!=meta['identity']['input_md5']:
        raise ValueError('Path inputs have different image identities')
    nodes={n['address']:n for n in (restore_node(row,base) for row in jsonl(a.nodes))}
    for row in jsonl(a.extra):
        n=restore_node(row,base);nodes.setdefault(n['address'],n)
    graph={'nodes':list(nodes.values()),'_nodes_by_address':nodes,'path_analysis':json.loads(a.settings.read_text(encoding='utf-8')),'registrations':[]}
    with gzip.open(a.registrations,'rt',encoding='utf-8') as stream:registrations=json.load(stream)['records']
    with gzip.open(a.slots,'rt',encoding='utf-8') as stream:
        slots=[{'key':reference_va(s['key'],base),'anchor':reference_va(s['anchor'],base),'type':s['type']} for s in json.load(stream)['records']]
    overlays,_=registration_edges(registrations,slots,nodes,base,0x3cb665c8)
    static_slots=[{'key':base+s['key_rva'],'anchor':base+s['anchor_rva'],'type':s['type'],
        'source':'static_link_creation_candidate','creation_call_rva':s['call_rva']} for s in modes.get('static_link_creations',[])
        if s.get('key_rva') is not None and s.get('anchor_rva') is not None]
    static_edges,_=registration_edges(registrations,static_slots,nodes,base,0x3cb665c8)
    combined_overlays={source:list(items) for source,items in overlays.items()}
    for source,items in static_edges.items():combined_overlays.setdefault(source,[]).extend(items)
    definitions={m['id']:m for m in modes['modes']};targets=defaultdict(lambda:defaultdict(set))
    for record in jsonl(a.classification):
        eol=reference_va(record['eol'],base)
        steps=[('observed_connections','observed_mode_candidates'),('conditional_registration_candidates','registration_overlay_mode_candidates'),
               ('static_slot_creation_candidates','static_slot_creation_mode_candidates')]
        if record['category']=='additional_other_mode_root':steps.append(('other_mode_connections','observed_mode_candidates'))
        for model,field in steps:
            if model=='conditional_registration_candidates' and record['category']!='config_candidate_registration_edge':continue
            if model=='static_slot_creation_candidates' and record['category']!='config_static_slot_creation_candidate':continue
            for mode_id in record[field]:
                mode=definitions[mode_id]
                if (modes['configuration_ancestry'][mode_id]['configuration_family_candidate'] or model=='other_mode_connections') and mode.get('root_rva') is not None:
                    targets[model][mode['root_rva']].add(eol)
    aliases=defaultdict(list)
    for mode in definitions.values():
        if mode.get('root_rva') is not None:aliases[mode['root_rva']].append(mode)
    ranges=[(s['address'],s['address']+s['memory_size']) for s in layout['load_segments']]
    a.output.mkdir(parents=True,exist_ok=True)
    stats={};frontier_stream=gzip.open(a.output/'path-frontiers.jsonl.gz','wt',encoding='utf-8')
    for model,roots in targets.items():
        seen=set();count=0;dropped=0;summaries=[];unprocessed=[]
        with gzip.open(a.output/(model+'.jsonl.gz'),'wt',encoding='utf-8',compresslevel=7) as output:
            for index,(root,wanted) in enumerate(sorted(roots.items(),key=lambda item:(-len(item[1]),item[0]))):
                if count>=a.max_records:unprocessed.append(root);continue
                choices=aliases[root];first=choices[0]
                definition={'name':first['name'] or first['id'],'prompt':first['prompt'] or first['name'] or first['id'],
                    'root':base+root,'evidence_call':first['definition_evidence'][0].get('call_rva')}
                local_count=0;local_seen=set()
                def emit(row):
                    nonlocal count,local_count,dropped
                    if row['eol_node'] not in wanted:return
                    registrations=[e for e in row['edge_trace'] if e['kind']=='candidate_registration_installation']
                    if model=='conditional_registration_candidates' and not registrations:return
                    if model=='static_slot_creation_candidates' and not any(e.get('slot_source')=='static_link_creation_candidate' for e in registrations):return
                    if count>=a.max_records:dropped+=1;return
                    count+=1;local_count+=1;seen.add(row['eol_node']);local_seen.add(row['eol_node'])
                    result={k:row[k] for k in ('mode','prompt','syntax_candidate','selector_candidate','syntax_status','final_tracked_state')}
                    result.update(handler=reference(row['handler'],base,ranges),eol_node=evidence_value({'node':row['eol_node']},base,ranges),
                        conditions=evidence_value(row['conditions'],base,ranges),parameters=evidence_value(row['parameters'],base,ranges),
                        state_effects=evidence_value(row['state_effects'],base,ranges),gaps=evidence_value(row['gaps'],base,ranges),
                        conditional_registrations=evidence_value(registrations,base,ranges),model=model,mode_root_rva=root,
                        mode_candidates=[{'id':m['id'],'name':m['name'],'prompt':m['prompt'],'parent':m['parent']} for m in choices],
                        mode_aliases=sorted({m['name'] for m in choices if m['name']}),
                        evidence_id=model+'-%06d'%count,
                        availability='Static mode definition and historical connections; runtime mode activation and predicates unresolved' if model in ('observed_connections','other_mode_connections')
                            else 'Conditional installation candidate; slot creation, trigger, order and input/context conditions unresolved')
                    if registrations:
                        result['gaps'].append({'reason':'Candidate registration installations remain conditional','evaluated':False})
                        result['syntax_status']='partial_syntax_candidate'
                    output.write(json.dumps(result,ensure_ascii=False,separators=(',',':'))+'\n')
                summary,_=recover_mode(graph,definition,{} if model in ('observed_connections','other_mode_connections') else overlays if model=='conditional_registration_candidates' else combined_overlays,
                    a.max_states,a.max_terminals,lambda:False,record_sink=emit)
                frontier_stream.write(json.dumps({'model':model,'root_rva':root,'frontiers':evidence_value(summary['frontiers'],base,ranges),
                    'frontier_list_truncated':summary['frontier_list_truncated']})+'\n')
                summaries.append({k:v for k,v in summary.items() if k!='frontiers'})
                summaries[-1].update(root_rva=root,cohort_target_eols=len(wanted),cohort_witnesses=local_count,cohort_eols_recovered=len(local_seen))
                if index%20==0:print(json.dumps({'model':model,'roots_processed':index+1,'roots':len(roots),'records':count,'cohort_eols':len(seen)}),flush=True)
        all_targets=set().union(*roots.values()) if roots else set()
        stats[model]={'roots':len(roots),'records':count,'cohort_target_eols':len(all_targets),'cohort_eols_recovered':len(seen),
            'eols_without_witness':[reference(ea,base,ranges) for ea in sorted(all_targets-seen)],'dropped_records':dropped,
            'unprocessed_root_rvas':unprocessed,'root_summaries':summaries}
    frontier_stream.close()
    (a.output/'path-summary.json').write_text(json.dumps({'identity':meta['identity'],'models':stats,
        'scope':'Config-family mode-local witnesses for the original retained EOL cohort; observed and installation-candidate models separate',
        'limits':{'max_states_per_mode':a.max_states,'max_terminals_per_mode':a.max_terminals,'max_records_per_model':a.max_records}},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({name:{k:v for k,v in data.items() if k not in ('root_summaries','eols_without_witness')} for name,data in stats.items()}))


if __name__=='__main__':main()
