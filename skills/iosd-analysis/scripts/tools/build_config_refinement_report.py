"""Compare saved config witnesses, separating new terminals from clearer syntax."""
import argparse,json
from collections import Counter,defaultdict
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from iosd_helper.catalogue import inventory_html


def lines(path):
    with path.open(encoding='utf-8') as f:
        for line in f:yield json.loads(line)


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('directory');p.add_argument('--phase',default='refinement');a=p.parse_args()
    root=Path(a.directory);out=root/a.phase;tree=out/'tree'
    old_summary=json.loads((out/'baseline-summary.json').read_text(encoding='utf-8'))
    summary=json.loads((tree/'summary.json').read_text(encoding='utf-8'))
    before=list(lines(out/'baseline-config-paths.jsonl'));current=[r for r in lines(tree/'paths.jsonl') if r['mode']=='configure']
    old_by=defaultdict(list)
    def context(r):
        s=r['syntax_candidate'];return 'no' if s.startswith('no ') else 'default' if s.startswith('default ') else 'positive_or_other'
    for row in before:old_by[(row['eol_node'],context(row))].append(row)
    old_eols={r['eol_node'] for r in before};new_eols={r['eol_node'] for r in current}
    changed=[];all_rows=[];changes=[]
    def route(s):
        return 'exec_via_do_exec' if s.startswith(('do-exec ','no do-exec ','default do-exec ')) else 'native_config_candidate'
    for line_number,row in enumerate(current,1):
        old=old_by[(row['eol_node'],context(row))]
        old_strings={r['syntax_candidate'] for r in old}
        kind='new_eol_witness' if row['eol_node'] not in old_eols else ('new_context_witness' if not old else
            'syntax_changed' if row['syntax_candidate'] not in old_strings else 'same_syntax')
        old_best=min(old,key=lambda r:(r['syntax_candidate'].count('<?'),len(r['syntax_candidate']))) if old else None
        clearer=bool(old_best and row['syntax_candidate'].count('<?')<old_best['syntax_candidate'].count('<?'))
        compact={'syntax':row['syntax_candidate'],'route':route(row['syntax_candidate']),'change':kind,'opaque_steps_reduced':clearer,
            'handler_rva':hex(row['handler_rva']) if row['handler_rva'] is not None else hex(row['handler']),
            'selector':row['selector_candidate'],'eol_va':hex(row['eol_node']),'syntax_status':row['syntax_status'],
            'availability':row['availability'],'baseline_example':old_best['syntax_candidate'][:400] if old_best else '',
            'condition_count':len(row['conditions']),'remaining_gaps':len(row['gaps']),
            'evidence_config_jsonl_line':line_number}
        all_rows.append(compact)
        if kind!='same_syntax':
            changed.append(compact);changes.append({'change_kind':kind,'opaque_steps_reduced':clearer,'baseline_example':old_best,
                'current_path':row,'proves_new_registration':False,'availability_verified':False})
    unknown=[n for n in lines(tree/'unknown-nodes.jsonl') if 'configure' in n.get('connected_mode_candidates',[])]
    opaque=Counter(n.get('action_name') or n.get('reason') for n in unknown if not n.get('path_semantics') or n.get('semantic_error'))
    all_uncertainties=Counter(reason for n in unknown for reason in n['remaining_uncertainties'])
    action_rows=[]
    config_action_counts=Counter(n.get('action_name') for n in lines(tree/'nodes.jsonl') if 'configure' in n.get('connected_mode_candidates',[]))
    for f in sorted((out/'action-evidence').glob('*_action.json')):
        e=json.loads(f.read_text(encoding='utf-8'))
        affected=config_action_counts[e['name']]
        action_rows.append({'action':e['name'],'consumer_rva':hex(e['rva']),'consumer_bytes':e['size'],'config_nodes':affected,
            'evidence_file':'action-evidence/'+f.name})
    before_mode=next(m for m in old_summary['modes'] if m['mode']=='configure')
    after_mode=next(m for m in summary['modes'] if m['mode']=='configure')
    stats={'baseline_nodes':old_summary['runtime_nodes'],'runtime_nodes':summary['runtime_nodes'],'runtime_edges':summary['runtime_edges'],
        'baseline_missing_pages':old_summary['missing_pages'],'missing_pages':summary['missing_pages'],
        'config_terminal_nodes_before':before_mode['terminal_nodes'],'config_terminal_nodes_after':after_mode['terminal_nodes'],
        'config_opaque_nodes_before':before_mode['unknown_or_unread_nodes'],'config_opaque_nodes_after':after_mode['unknown_or_unread_nodes'],
        'config_witnesses_before':len(before),'config_witnesses_after':len(current),'new_config_eol_witnesses':len(new_eols-old_eols),
        'new_native_config_eol_witnesses':len({r['current_path']['eol_node'] for r in changes if r['change_kind']=='new_eol_witness' and route(r['current_path']['syntax_candidate'])=='native_config_candidate'}),
        'new_do_exec_eol_witnesses':len({r['current_path']['eol_node'] for r in changes if r['change_kind']=='new_eol_witness' and route(r['current_path']['syntax_candidate'])=='exec_via_do_exec'}),
        'config_witnesses_without_opaque_token_before':sum('<?' not in r['syntax_candidate'] for r in before),
        'config_witnesses_without_opaque_token_after':sum('<?' not in r['syntax_candidate'] for r in current),
        'changed_witnesses':len(changed),'change_categories':dict(Counter(r['change'] for r in changed)),
        'opaque_steps_reduced_witnesses':sum(r['opaque_steps_reduced'] for r in changed),
        'config_nodes_with_remaining_uncertainty':len(unknown),'remaining_config_categories':dict(opaque),
        'remaining_config_uncertainty_categories':dict(all_uncertainties),'atomic_snapshot':False,
        'interpretation':'New/clearer witnesses in the analysis; no command was executed and no new device registration is claimed',
        'baseline_correction':'Previous runtime reconstruction did not relocate reviewed callback RVAs; restored local sense/default tracking changes witnesses and contexts. Original graph evidence is retained.' if a.phase=='refinement' else 'Baseline is the corrected refinement report; option alternatives and conditional branches are added in this phase.'}
    (out/'config-delta-summary.json').write_text(json.dumps(stats,ensure_ascii=False,indent=2),encoding='utf-8')
    with (out/'config-changes.jsonl').open('w',encoding='utf-8') as f:
        for row in changes:f.write(json.dumps(row,ensure_ascii=False)+'\n')
    with (out/'config-paths.jsonl').open('w',encoding='utf-8') as f:
        for row in current:f.write(json.dumps(row,ensure_ascii=False)+'\n')
    with (out/'config-commands.txt').open('w',encoding='utf-8') as f:
        f.write('# Conditional config syntax witnesses; not exhaustive, not guaranteed executable.\n')
        for row in all_rows:f.write('(config)# %s | handler=%s | selector=%s | %s | %s\n'%(row['syntax'],row['handler_rva'],row['selector'],row['syntax_status'],row['availability']))
    changed.sort(key=lambda r:(r['change']!='new_eol_witness',not r['opaque_steps_reduced'],'<?' in r['syntax'],len(r['syntax'])))
    # These are display examples, not a completeness filter.
    examples=[];families=Counter()
    for row in changed:
        s=row['syntax'];family=s.split()[0] if s else ''
        if '<?' in s or family in ('no','default','do-exec') or len(s)>170:continue
        if families[family]>=3:continue
        families[family]+=1;examples.append(row)
        if len(examples)>=24:break
    (out/'examples.json').write_text(json.dumps(examples,ensure_ascii=False,indent=2),encoding='utf-8')
    data={'identity':summary['identity'],'identity_text':'MD5 '+summary['identity']['input_md5']+' | 运行时基址 '+hex(summary['identity']['imagebase']),
        'summary':stats,'coverage':{'runtime_scope':summary['syntax']['scope'],'atomic_snapshot':False,
            'unknown_branches_retained':True,'dispatch':summary['runtime_action_dispatch'],'notes':summary['syntax']['notes']},
        'labels':{'examples':'先看：原生 config 恢复示例','native_changes':'原生 config 候选路径变化','exec_changes':'do-exec 分支变化','all_config':'所有已导出的 config 路径示例',
            'actions':'本轮核对的动作消费函数','dispatch':'静态为空、运行时已绑定的动作','unknown':'剩余 config 不透明动作','uncertainty':'剩余状态／参数不确定项'},
        'hidden_columns':['evidence_file'],'tables':{'examples':examples,'native_changes':[r for r in changed if r['route']=='native_config_candidate'],
            'exec_changes':[r for r in changed if r['route']=='exec_via_do_exec'],
            'all_config':[{k:r[k] for k in ('syntax','route','handler_rva','selector','syntax_status','availability','remaining_gaps','evidence_config_jsonl_line')} for r in all_rows],
            'actions':action_rows,'dispatch':[{'action':r['name'],'opcode':r['opcode'],'runtime_function_va':hex(r['runtime_function_va']),
                'name_opcode_verified':r['verified']} for r in lines(tree/'runtime-action-dispatch.jsonl') if not r['static_function_va'] and r.get('runtime_function_va')],
            'unknown':[{'action_or_reason':k,'nodes':v} for k,v in opaque.most_common()],
            'uncertainty':[{'uncertainty':k,'nodes':v} for k,v in all_uncertainties.most_common()]}}
    if a.phase!='refinement':
        from iosd_helper.syntax_view import condition_text
        option_nodes=[n for n in lines(tree/'keyword-option-nodes.jsonl') if 'configure' in n.get('connected_mode_candidates',[])]
        option_rows=[];source_rows=[]
        for n in option_nodes:
            source=n.get('option_source',{});storage=n.get('option_storage',{})
            source_rows.append({'node_va':hex(n['address']),'action':n['action_name'],'getter_va':hex(source['getter']) if source.get('getter') else '',
                'producer_model':source.get('reviewed_model',{}).get('kind','unresolved' if source.get('getter') else 'direct_array'),
                'release_callback_va':hex(source['release_callback']) if source.get('release_callback') else '',
                'known_options':len(n['keyword_options']),'enumeration_complete':n['option_enumeration_complete'],
                'frontiers':' | '.join(f.get('reason','') for f in n.get('option_frontiers',[])),
                'state_field':storage.get('field_offset'),'operation':storage.get('operation')})
            for item in n['keyword_options']:
                option_rows.append({'keyword':item['keyword'],'value':item['value'],'node_va':hex(n['address']),
                    'field_offset':storage.get('field_offset'),'operation':storage.get('operation'),'minimum_match':item.get('minimum_match'),
                    'conditions':' | '.join(condition_text(c) for c in item.get('conditions',[])),'keyword_unparsed':item.get('keyword_unparsed',False)})
        branches=[n for n in lines(tree/'indirect-branches.jsonl') if 'configure' in n.get('connected_mode_candidates',[])]
        branch_rows=[{'node_va':hex(n['address']),'action':n['action_name'],'callback_va':hex(n['condition']['callback']) if n['condition'].get('callback') else '',
            'condition':condition_text(n['condition']),'snapshot_result':n['condition'].get('snapshot_result'),
            'observed_value':n['condition'].get('observed_value'),'observed_fallback_target':hex(n['condition']['observed_fallback_target']) if 'observed_fallback_target' in n['condition'] else '',
            'condition_details':json.dumps(n['condition'],ensure_ascii=False),'targets':json.dumps(n.get('semantic_edges'),ensure_ascii=False)} for n in branches]
        data['labels'].update(option_choices='全部已取得选项（不受路径示例裁剪）',option_sources='选项表与未解析生成器',indirect_conditions='条件回调与额外分支')
        data['tables'].update(option_choices=option_rows,option_sources=source_rows,indirect_conditions=branch_rows)
        data['hidden_columns']+=['condition_details','targets']
        if (tree/'option-path-variants.jsonl').exists():
            variants=list(lines(tree/'option-path-variants.jsonl'))
            data['labels']['option_variants']='选项逐项展开的有界路径示例'
            data['tables']['option_variants']=[{'syntax':r['syntax_candidate'],'handler_va':hex(r['handler']),
                'selector':r['selector_candidate'],'availability':r['availability'],'status':r['syntax_status'],
                'option_node':hex(r['variant_source']['source_node']),'option_index':r['variant_source']['option_index']} for r in variants]
        stats.update(config_option_nodes=len(option_nodes),known_config_option_entries=len(option_rows),config_indirect_branch_nodes=len(branches))
        (out/'config-delta-summary.json').write_text(json.dumps(stats,ensure_ascii=False,indent=2),encoding='utf-8')
    intro=('原来的 26 个页位置全部补齐，并沿后续引用继续读取；当前已知图的缺页队列为 %d。config 投影 EOL 节点 %d → %d；不透明语法节点 %d → %d。'
        '同时修正了已审查公共回调的 RVA→VA 换算，重新区分正向/no/default 上下文；因此路径变化也含纠错。'
        '投影数量含 do-exec 进入的 EXEC 分支；本轮新增终点归属该类，未当成原生 config 新命令。'
        '表中每个 EOL/跟踪上下文只有一条优先示例，不是所有语法。接口验证、动态数字范围、权限和回调条件仍保留；没有执行目标命令或函数。')%(
        summary['missing_pages'],before_mode['terminal_nodes'],after_mode['terminal_nodes'],before_mode['unknown_or_unread_nodes'],after_mode['unknown_or_unread_nodes'])
    if a.phase!='refinement':
        intro=('本轮核对关键词选项表、生成回调和间接条件分支。config 不透明语法节点 %d → %d，当前已知图缺页为 %d。'
            '所有已取得选项另表保留，包括值为 0 的选项；未解析生成器、额外分支及状态条件保留，未执行任何目标回调。'
            '普通路径表每个 EOL/上下文仅给一条优先示例；选项逐项展开表也是有界示例，完整条件边另存。')%(
            before_mode['unknown_or_unread_nodes'],after_mode['unknown_or_unread_nodes'],summary['missing_pages'])
    html=inventory_html(data,'config 关键词选项与间接条件分支' if a.phase!='refinement' else 'config 模式补读与未知分支恢复',intro,
        '搜索覆盖所选表全部记录，每页 200 条；行中给出 config-paths.jsonl 的证据行号，完整条件、gaps 与轨迹保存在该文件，旧示例长文本在本页最多显示 400 字符。没有 <?> 不等于条件全部已验证。新 EOL、上下文新增和文字修正分别标记。')
    links='<p><a href="tree/syntax.html">多模式路径表</a> · <a href="config-commands.txt">config 路径文本</a> · <a href="config-paths.jsonl">config 完整路径证据</a> · <a href="config-changes.jsonl">完整变化与原始证据</a> · <a href="tree/nodes.jsonl">完整节点</a> · <a href="tree/unknown-nodes.jsonl">保留的不完整节点</a> · <a href="tree/summary.json">来源哈希与范围</a> · <a href="../index.html">上一轮报告</a></p>'
    if a.phase!='refinement':links+='<p><a href="tree/conditional-transitions.jsonl">全部带条件语法边</a> · <a href="tree/keyword-option-nodes.jsonl">全部选项表原始证据</a> · <a href="tree/indirect-branches.jsonl">全部间接条件分支</a> · <a href="tree/option-path-variants.jsonl">选项变体完整轨迹</a> · <a href="../refinement/index.html">本轮基线</a></p>'
    if a.phase=='refinement' and (root/'options/index.html').exists():links='<p><a href="../options/index.html">最新：关键词选项与间接条件分支</a>；本页保留补读阶段的基线。</p>'+links
    if a.phase!='refinement':links+='<p><a href="../../../docs/config关键词选项与条件回调.md">概念与方法说明</a></p>'
    html=html.replace('<p id="identity"></p>',links+'<p id="identity"></p>')
    (out/'index.html').write_text(html,encoding='utf-8')
    print(json.dumps({k:v for k,v in stats.items() if k not in ('remaining_config_categories','remaining_config_uncertainty_categories')},ensure_ascii=True,indent=2),flush=True)
    print('Examples:',json.dumps([{k:r[k] for k in ('syntax','handler_rva','change','baseline_example')} for r in examples[:12]],ensure_ascii=True),flush=True)


if __name__=='__main__':main()
