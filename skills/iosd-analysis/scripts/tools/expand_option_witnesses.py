"""Replay a saved prefix, select each known option, and re-solve a bounded suffix."""
import argparse,json
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from iosd_helper.syntax_paths import semantic_options,state_after,recover_mode,raw_links,flatten_conditions


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('tree');p.add_argument('--max-nodes',type=int,default=16)
    p.add_argument('--max-options',type=int,default=16);p.add_argument('--max-states',type=int,default=6000);a=p.parse_args();root=Path(a.tree)
    with (root/'nodes.jsonl').open(encoding='utf-8') as stream:nodes={n['address']:n for n in map(json.loads,stream)}
    settings=json.loads((root/'runtime-path-settings.json').read_text(encoding='utf-8'))
    definition=next(d for d in json.loads((root/'mode-definitions.json').read_text(encoding='utf-8')) if d['name']=='configure')
    graph={'nodes':list(nodes.values()),'path_analysis':settings,'registrations':[]}
    seeds={}
    with (root/'paths.jsonl').open(encoding='utf-8') as stream:
        for path in map(json.loads,stream):
            if path['mode']!='configure' or path['syntax_candidate'].startswith(('no ','default ','do-exec ')):continue
            for edge in path['edge_trace']:
                n=nodes[edge['source']]
                if edge['kind']=='keyword_option_match' and 1<len(n.get('keyword_options',[]))<=a.max_options and n['address'] not in seeds:
                    seeds[n['address']]=path
                    if len(seeds)>=a.max_nodes:break
            if len(seeds)>=a.max_nodes:break
    variants=[];frontiers=[];dedup=set()
    for ea,seed in seeds.items():
        state=tuple(settings.get('initial_normal_cli_state',[1,0,0]));prefix=[];tokens=[];conditions=[];effects=[];gaps=[];parameters=[]
        for edge in seed['edge_trace']:
            if edge['source']==ea:break
            n=nodes[edge['source']];prefix.append(edge)
            if edge.get('token') is not None:tokens.append(edge['token'])
            if edge.get('condition'):conditions.append(edge['condition'])
            if edge.get('apply_effects'):
                effects.extend({'node':n['address'],**e} for e in n.get('effects',[]));state=state_after(n,state,settings)
                reviewed={int(v,0) if isinstance(v,str) else v for v in settings.get('reviewed_normal_cli_callbacks',[])}
                for effect in n.get('effects',[]):
                    if effect.get('kind')=='context_callback' and effect.get('function_candidate') not in reviewed:gaps.append({'node':n['address'],'reason':'Context callback effects unresolved'})
            if edge.get('option_effects'):
                effects.extend({'node':n['address'],**e} for e in edge['option_effects']);state=state_after({'effects':edge['option_effects']},state,settings)
            if edge.get('gap'):gaps.append({'node':n['address'],'reason':edge['gap']});state=(None,None,state[2])
            if edge['kind']=='parameter_match':parameters.append({'node':n['address'],**n.get('parameter',{})})
        n=nodes[ea]
        for option in semantic_options(n,state,graph):
            if option['kind']!='keyword_option_match':continue
            after=state_after({'effects':option.get('option_effects',[])},state,settings)
            local={**graph,'path_analysis':{**settings,'initial_normal_cli_state':list(after)}}
            local_def={**definition,'root':option['target']}
            stats,suffixes=recover_mode(local,local_def,{},a.max_states,2,lambda:False)
            if not suffixes or stats['stop_reason']=='state_limit':frontiers.append({'node':ea,'option_index':option['option_index'],'reason':stats['stop_reason'],'retained_in_node_and_conditional_graph':True})
            for suffix in suffixes:
                syntax=' '.join(tokens+[option['token'],suffix['syntax_candidate']])
                key=(syntax,suffix['eol_node'],tuple(suffix['final_tracked_state']))
                if key in dedup:continue
                dedup.add(key);all_conditions=conditions+[option['condition']]+suffix['conditions'];all_gaps=gaps+suffix['gaps']
                constraints=list(flatten_conditions(all_conditions))
                blocked=any(c.get('evaluated') and 'snapshot_result' in c and c.get('expected',True)!=c['snapshot_result'] for c in constraints)
                blocked_gate=any(g.get('evaluated') and not g.get('direct_gate_passes') for c in constraints if c.get('kind')=='keyword_access_gates' for g in c['gates'])
                variants.append({**suffix,'mode':'configure','prompt':'config','mode_root':int(definition['root'],0),'syntax_candidate':syntax,
                    'conditions':all_conditions,'state_effects':effects+option.get('option_effects',[])+suffix['state_effects'],'parameters':parameters+suffix['parameters'],
                    'gaps':all_gaps,'syntax_status':'partial_syntax_candidate' if all_gaps else 'syntax_candidate',
                    'availability':'blocked_by_observed_keyword_gate' if blocked_gate else 'blocked_by_observed_predicate' if blocked else 'observed_connection_other_conditions_unresolved',
                    'node_addresses':[e['source'] for e in prefix]+[ea]+suffix['node_addresses'],'edge_trace':prefix+[{'source':ea,**option}]+suffix['edge_trace'],
                    'variant_source':{'kind':'bounded_option_variant','source_node':ea,'option_index':option['option_index'],'seed_eol':seed['eol_node'],
                        'scope':'Existing prefix replay plus selected option effects and freshly solved suffix; not exhaustive combinations'}})
    for filename,rows in [('option-path-variants.jsonl',variants),('option-variant-frontiers.jsonl',frontiers)]:
        with (root/filename).open('w',encoding='utf-8') as f:
            for row in rows:f.write(json.dumps(row,ensure_ascii=False)+'\n')
    info={'option_nodes_sampled':len(seeds),'variants':len(variants),'frontiers':len(frontiers),'max_states_per_suffix':a.max_states,
          'all_options_preserved_separately':True,'target_functions_executed':False}
    (root/'option-variant-summary.json').write_text(json.dumps(info,indent=2),encoding='utf-8')
    print(json.dumps(info),flush=True)


if __name__=='__main__':main()
