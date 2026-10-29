"""Export observed runtime grammar, static comparison and unresolved frontiers."""
import argparse
from collections import Counter,defaultdict,deque
import hashlib
import json
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from iosd_helper.runtime_grammar import CapturedPages,reconstruct_runtime_graph,observe_slot_bindings
from iosd_helper.syntax_paths import recover_paths,semantic_options,flatten_conditions
from iosd_helper.syntax_view import syntax_html


def jsonl(path,rows):
    with path.open('w',encoding='utf-8') as f:
        for row in rows:f.write(json.dumps(row,ensure_ascii=False)+'\n')


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('static_graph');p.add_argument('--pages',action='append',required=True)
    p.add_argument('--cache-capture',action='append',default=[]);p.add_argument('--linkage',required=True);p.add_argument('--output',required=True)
    p.add_argument('--profile',default='profiles/lifecycle_api_26_01_02.json')
    a=p.parse_args();out=Path(a.output);out.mkdir(parents=True,exist_ok=True)
    static=json.loads(Path(a.static_graph).read_text(encoding='utf-8'))
    if static['identity'].get('imagebase')!=0:raise ValueError('Runtime reconstruction currently requires the saved RVA graph at capture base zero')
    linkage=json.loads(Path(a.linkage).read_text(encoding='utf-8'))
    captures=[];files=[]
    for folder in a.pages:
        files.extend(sorted(Path(folder).glob('pages-*.json')))
    files.extend(Path(f) for f in a.cache_capture)
    for file in files:
        captures.append(json.loads(file.read_text(encoding='utf-8')))
    identities={(c['input_md5'],c['runtime_base']) for c in captures}
    if len(identities)!=1:raise ValueError('Capture identities/bases differ')
    digest,base=next(iter(identities))
    if digest!=static['identity']['input_md5']:raise ValueError('Static/runtime identity mismatch')
    memory=CapturedPages(captures);del captures
    profile=json.loads(Path(a.profile).read_text(encoding='utf-8'))
    if profile['input_md5']!=digest:raise ValueError('Runtime profile identity mismatch')
    graph=reconstruct_runtime_graph(memory,static['graph'],base,linkage,keyword_gates=profile['runtime'].get('keyword_privilege_gates',[]),
        option_getters=profile['runtime'].get('option_getters',{}),predicate_models=profile['runtime'].get('predicate_models',{}))
    print('Decoded',len(graph['nodes']),'nodes; missing pages',len(memory.missing_pages),flush=True)
    nodes={n['address']:n for n in graph['nodes']}
    (out/'runtime-path-settings.json').write_text(json.dumps(graph['path_analysis'],ensure_ascii=False,indent=2),encoding='utf-8')
    (out/'mode-definitions.json').write_text(json.dumps(graph['mode_definitions'],ensure_ascii=False,indent=2),encoding='utf-8')
    for node in graph['nodes']:
        reasons=[]
        if node['status']=='unresolved':reasons.append('unread_or_unclassified_record')
        if not node.get('path_semantics'):reasons.append('action_semantics_unresolved')
        if node.get('semantic_error'):reasons.append('descriptor_decode_error')
        if node.get('privilege_record_error'):reasons.append('privilege_record_unread')
        if node.get('parameter_gap'):reasons.append('parameter_validation_unresolved')
        if node.get('constant_string_error'):reasons.append('constant_string_unread')
        if any(e.get('effects_unresolved') for e in node.get('effects',[])):reasons.append('callback_effects_unresolved')
        if any(e.get('decoder_semantics_unresolved') for e in node.get('effects',[])):reasons.append('assigned_decoder_unresolved')
        if node.get('iterator',{}).get('callback'):reasons.append('nvgen_iterator_callback_unresolved')
        if node.get('action_function_requires_runtime'):reasons.append('action_function_requires_runtime')
        if node.get('dispatch_semantics_unverified'):reasons.append('runtime_dispatch_unverified')
        if node.get('option_frontiers'):reasons.append('option_source_or_entries_unresolved')
        if node.get('condition',{}).get('kind') in ('no_argument_predicate','parser_ambiguity_or_remaining_input') and not node['condition'].get('evaluated'):reasons.append('branch_condition_unresolved')
        node['remaining_uncertainties']=reasons
    adjacency=defaultdict(list)
    for n in graph['nodes']:
        for e in semantic_options(n,(None,None,None),graph):adjacency[n['address']].append(e['target'])
    reach={};mode_summaries=[]
    for mode in graph['mode_definitions']:
        root=int(mode['root'],0);seen={root};pending=deque([root])
        while pending:
            for target in adjacency[pending.popleft()]:
                if target not in seen:seen.add(target);pending.append(target)
        reach[mode['name']]=seen
        mode_summaries.append({'mode':mode['name'],'connected_projection_nodes':len(seen),
            'terminal_nodes':sum(nodes.get(ea,{}).get('path_semantics') in ('terminal','parameter_terminal') for ea in seen),
            'nodes_with_remaining_uncertainty':sum(bool(nodes.get(ea,{}).get('remaining_uncertainties')) for ea in seen),
            'unknown_or_unread_nodes':sum(not nodes.get(ea,{}).get('path_semantics') or bool(nodes.get(ea,{}).get('semantic_error')) for ea in seen)})
    for node in graph['nodes']:
        node['connected_mode_candidates']=[name for name,seen in reach.items() if node['address'] in seen]
    jsonl(out/'nodes.jsonl',graph['nodes']);jsonl(out/'edges.jsonl',graph['edges'])
    jsonl(out/'conditional-transitions.jsonl',({'source':n['address'],**edge} for n in graph['nodes'] for edge in semantic_options(n,(None,None,None),graph)))
    jsonl(out/'keyword-option-nodes.jsonl',(n for n in graph['nodes'] if n.get('path_semantics')=='keyword_options'))
    jsonl(out/'indirect-branches.jsonl',(n for n in graph['nodes'] if n.get('condition',{}).get('kind') in ('no_argument_predicate','parser_ambiguity_or_remaining_input')))
    jsonl(out/'runtime-action-dispatch.jsonl',graph['runtime_action_dispatch'])
    unknown=[n for n in graph['nodes'] if n['remaining_uncertainties']]
    jsonl(out/'unknown-nodes.jsonl',unknown)
    pending_pairs={(n['fields']['key']['value'],n['fields']['fragment']['value']) for s in linkage['lists'] if s['name']=='pending_parser_bindings' for n in s['nodes']}
    dynamic_keys={n['fields']['key']['value'] for s in linkage['lists'] if s['name']=='dynamic_parser_linkage' for n in s['nodes']}
    comparisons=[]
    slots,binding_records=observe_slot_bindings(memory,static['graph'],base,linkage,int(profile['runtime']['link_sentinel_rva'],0))
    binding_index={r['registration_rva']:r for r in binding_records}
    jsonl(out/'observed-slot-bindings.jsonl',slots)
    for reg in static['graph']['registrations']:
        root=base+reg['root'];key=base+reg['link_key']
        modes=[name for name,seen in reach.items() if root in seen]
        status='observed_pending' if (key,root) in pending_pairs else ('root_connected_conditionally' if modes else 'not_observed_connected')
        binding=binding_index[reg['address']]
        comparisons.append({**reg,**binding,'addresses':'legacy fields are RVAs; runtime_* are VAs','runtime_root':root,'runtime_key':key,
            'runtime_status':status,'connected_modes':modes,'dynamic_key_observed':key in dynamic_keys,
            'absence_proven':False,'availability_verified':False})
    jsonl(out/'static-registration-comparison.jsonl',comparisons)
    jsonl(out/'pending-records.jsonl',[n for s in linkage['lists'] if s['name']=='pending_parser_bindings' for n in s['nodes']])
    jsonl(out/'dynamic-slots.jsonl',[n for s in linkage['lists'] if s['name']=='dynamic_parser_linkage' for n in s['nodes']])
    missing=[{'runtime_va':ea,'size':65536,'label':'unresolved-runtime-target-or-descriptor'} for ea in sorted(memory.missing_pages) if 0x10000<=ea<0x800000000000]
    (out/'request-missing-pages.json').write_text(json.dumps({'ranges':missing},indent=2),encoding='utf-8')
    identity={'input_md5':digest,'imagebase':base,'source':'saved paused debugger memory'}
    result=recover_paths(graph,tuple(m['name'] for m in graph['mode_definitions']),max_paths=120000)
    for path in result['paths']:
        gates=[g for c in flatten_conditions(path['conditions']) if c.get('kind')=='keyword_access_gates' for g in c['gates']]
        constraints=list(flatten_conditions(path['conditions']))
        blocked_predicate=any(c.get('evaluated') and 'snapshot_result' in c and c.get('expected',True)!=c['snapshot_result'] for c in constraints)
        path['availability']=('blocked_by_observed_keyword_gate' if any(g.get('evaluated') and not g.get('direct_gate_passes') for g in gates)
            else 'blocked_by_observed_predicate' if blocked_predicate else 'observed_connection_other_conditions_unresolved')
        path['handler_rva']=path['handler']-base if base<=path['handler']<base+0x50000000 else None
        path['eol_rva']=path['eol_node']-base if base<=path['eol_node']<base+0x50000000 else None
    result['summary']['scope']='One bounded syntax witness per EOL/context in observed runtime connections; not exhaustive syntax enumeration'
    result['summary']['runtime_conditions_evaluated']='Only configured direct keyword gates, where captured; no arbitrary predicates executed'
    result['summary']['notes']=['No static registration overlay added.','Unknown actions and unread branches retained in nodes/edges/unknown-nodes files.',
        'Configured direct keyword gates are annotated without pruning; all other conditions stay symbolic. No predicate or handler executed.','Cross-batch resume/re-stop epoch is not tracked; this is not an atomic process snapshot.']
    jsonl(out/'paths.jsonl',result['paths'])
    with (out/'commands.txt').open('w',encoding='utf-8') as f:
        f.write('# Bounded syntax witnesses in observed runtime connections; not an exhaustive or executable command list.\n')
        for path in result['paths']:
            f.write('(%s)# %s | handler=%s | %s | %s\n'%(path['prompt'],path['syntax_candidate'],hex(path['handler_rva']) if path['handler_rva'] is not None else hex(path['handler']),path['syntax_status'],path['availability']))
    (out/'syntax.html').write_text(syntax_html(identity,result,title='iosd 运行时连接图：带条件的语法路径示例',compact=True,
        description='来自暂停调试内存中的实际指针连接，不添加静态候选注册边。每个 EOL 与跟踪上下文保留一条路径示例；这些不是全部语法，也不保证当前可执行。未知动作、条件和未读取分支保存在完整图中。',
        footer='地址为本次运行时 VA；handler_rva 和 eol_rva 另存 paths.jsonl。service internal 的部分直接门控按已读取状态标注，仍保留被拒绝的候选路径。普通 CLI 初始状态是分析假设，权限、上下文、其他谓词及 handler 内部拒绝条件尚未全部验证。'),encoding='utf-8')
    summary={'identity':identity,'lists':[{'name':s['name'],'records':len(s['nodes']),'terminated_at_null':s['terminated_at_null'],'frontiers':s['frontiers']} for s in linkage['lists']],
        'runtime_nodes':len(graph['nodes']),'runtime_edges':len(graph['edges']),'unknown_nodes_retained':len(unknown),'missing_pages':len(missing),
        'static_registrations_with_direct_binding_evidence':sum(bool(r['observed_binding_evidence']) for r in comparisons),
        'page_conflicts':memory.conflicts,'modes':mode_summaries,'static_registration_status':dict(Counter(r['runtime_status'] for r in comparisons)),
        'unknown_categories':dict(Counter(reason for n in unknown for reason in n['remaining_uncertainties'])),
        'runtime_action_dispatch':{'verified_entries':sum(r['verified'] for r in graph['runtime_action_dispatch']),
            'initialized_entries':sum(bool(r.get('runtime_function_va')) for r in graph['runtime_action_dispatch']),
            'newly_resolved_from_static_zero':sum(r['verified'] and not r['static_function_va'] and bool(r.get('runtime_function_va')) for r in graph['runtime_action_dispatch'])},
        'syntax':result['summary'],'atomic_snapshot':False,'definition_excluded_for_incompleteness':0,
        'source_files':[{'path':str(f.resolve()),'sha256':hashlib.sha256(f.read_bytes()).hexdigest()} for f in files]}
    source_root=Path(__file__).resolve().parents[1]
    summary['interpretation_source_sha256']={name:hashlib.sha256((source_root/name).read_bytes()).hexdigest() for name in
        ('iosd_helper/runtime_grammar.py','iosd_helper/grammar_semantics.py','iosd_helper/option_tables.py','iosd_helper/syntax_paths.py','iosd_helper/syntax_view.py','tools/export_runtime_grammar.py')}
    (out/'analysis-profile.json').write_text(json.dumps(profile,ensure_ascii=False,indent=2),encoding='utf-8')
    summary['analysis_profile_sha256']=hashlib.sha256(Path(a.profile).read_bytes()).hexdigest()
    archived=out/'interpreter-sources';archived.mkdir(exist_ok=True)
    for name in summary['interpretation_source_sha256']:(archived/Path(name).name).write_bytes((source_root/name).read_bytes())
    (out/'summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in summary.items() if k not in ('syntax','source_files')},ensure_ascii=True,indent=2),flush=True)


if __name__=='__main__':main()
