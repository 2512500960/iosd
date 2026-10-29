"""Searchable mode-scoped IOS parser syntax candidates."""
from collections import Counter
import json
from .catalogue import inventory_html


def condition_text(condition):
    kind, expected = condition.get("kind"), condition.get("expected")
    if kind=='keyword_constraints':return '；'.join(condition_text(c) for c in condition['constraints'])
    if kind=='parser_state_mask_zero':return '状态+%s & %s 必须为 0（%s）'%(condition['field_offset'],condition['mask_raw_hex'],'符号求值' if condition.get('evaluated') else '未求值')
    if kind=='dynamic_number_bounds':return '数字上下界回调未执行'
    if kind=='interface_registry_and_validation':return '接口类型、编号与验证回调条件未求值'
    if kind=='exact_input_character':return '匹配字符 %#x；前后空白未推断'%condition['code']
    if kind=='iterator_nvgen_gate':return 'NVGEN=%s 的迭代分支（%s）'%(condition['expected_nvgen'],'符号求值' if condition.get('evaluated') else '未求值')
    if kind=='parser_ambiguity_or_remaining_input':return '歧义／剩余输入检查%s（依赖解析上下文，未执行）'%(' → %s'%expected if expected is not None else '')
    if kind=='no_argument_predicate':
        observed='；快照推导结果=%s'%condition['snapshot_result'] if 'snapshot_result' in condition else '；结果未知'
        return '回调 %#x%s%s（未调用）'%(condition.get('callback',0),' → %s'%expected if expected is not None else '',observed)
    if kind=='keyword_option_match':return '选项值=%s，最短匹配=%s；权限和歧义条件未验证'%(condition['value'],condition['minimum_match'])
    if kind=='parser_field_mask_zero':return '解析状态+%#x & %#x 必须为 0（未求值）'%(condition['field_offset'],condition['mask'])
    if kind=='global_option_membership':return '选项注册／启用槽 %s=%s（仅快照）'%(condition['variable_rva'],condition.get('value','未知'))
    if kind=='reviewed_option_producer':return '选项由已审查生成器 %#x 枚举，序号 %s'%(condition['getter'],condition['index'])
    if kind=='unresolved_option_source':return '其余选项依赖未解析的生成回调或未读表项'
    if kind == "predicate":
        function = condition.get("function")
        return "谓词 %s → %s（未执行）" % (condition.get("function_name") or (hex(function) if function else "未知"), expected)
    if kind == "privilege_gate":
        return "权限检查%s（未验证）" % ("通过" if expected else "不通过")
    if kind == "interface_status_mask":
        return "接口状态 & %#x %s 0（未读取）" % (condition.get("mask_candidate", 0), "≠" if expected else "=")
    if kind == "runtime_boolean":
        return "运行时变量 %#x → %s（未读取）" % (condition.get("variable_address", 0), expected)
    if kind == "normal_cli_noprefix":
        return "普通参数分支" if condition.get("expected_positive") else "no/default 参数省略分支"
    if kind == "parser_state_comparison":
        field = {9328: "sense", 9332: "default", 9636: "NVGEN"}.get(condition.get("field_offset"), "状态+%s" % condition.get("field_offset"))
        return "%s %s %s（%s）" % (field, condition.get("relation"), condition.get("comparison_value_raw_hex"),
                                   "符号状态判断" if condition.get("evaluated") else "未求值")
    if kind == "combined_keyword_parameter_terminal":
        return "组合宏：数字参数" + ("省略" if condition.get("parameter_omitted") else "保留")
    if kind == "keyword_access_gates":
        return " | ".join("%s：快照值=%s，此项检查%s（其余条件未验证）" %
            (g['name'],g.get('value','未知'),'放行' if g.get('direct_gate_passes') else ('拒绝' if g.get('evaluated') else '未知'))
            for g in condition['gates'])
    return str(kind)


def syntax_html(identity, result, title=None, description=None, footer=None,compact=False):
    summary = result["summary"]
    rows, gaps = [], Counter()
    for path in result["paths"]:
        for gap in path["gaps"]:
            gaps[(gap.get("action", "context_callback"), gap["node"], gap["reason"])] += 1
        registration_conditions = sorted({condition for registration in path["registration_candidates"]
                                          for condition in registration.get("conditions", [])})
        readable_conditions = [condition_text(c) for c in path["conditions"]]
        if registration_conditions:
            readable_conditions.append("注册调用条件未验证")
        rows.append({"mode": path["mode"], "prompt": path["prompt"], "syntax_candidate": path["syntax_candidate"],
                     "handler": hex(path["handler"]), "handler_name": (path.get("handler_metadata") or {}).get("name", ""),
                     "eol": hex(path["eol_node"]), "selector": path["selector_candidate"],
                     "status": path["syntax_status"], "unresolved_steps": len(path["gaps"]),
                     "condition_summary": " | ".join(readable_conditions),
                     "parameters": json.dumps(path["parameters"], ensure_ascii=False),
                     "registration_records": " | ".join(hex(r["address"]) for r in path["registration_candidates"]),
                     "registration_conditions": " | ".join(registration_conditions),
                     "nodes": " → ".join(hex(ea) for ea in path["node_addresses"]),
                     "gaps": json.dumps(path["gaps"], ensure_ascii=False)})
        if path.get('availability'):rows[-1]['availability']=path['availability']
        if compact:
            row=rows[-1]
            for field in ('parameters','nodes','gaps','registration_conditions'):row.pop(field,None)
            row['condition_summary']=row['condition_summary'][:400]
            row['evidence_paths_jsonl_line']=len(rows)
    modes = [{**mode, "root": hex(mode["root"])} for mode in summary["modes"]]
    for mode in modes:
        mode["frontiers"] = len(mode["frontiers"])
    unmatched = [{"record": hex(r["address"]), "key": hex(r["link_key"]), "root": hex(r["root"]),
                  "owner_candidate": r.get("owner_candidate") or ""}
                 for r in summary["registrations_without_static_slot"]]
    gap_rows = [{"action": action, "node": hex(ea), "reason": reason, "affected_witnesses": affected}
                for (action, ea, reason), affected in gaps.most_common()]
    data = {"identity": identity, "hidden_columns": ["parameters", "registration_conditions", "nodes", "gaps"],
            "labels": {"paths": "配置模式语法候选路径", "modes": "模式与覆盖",
                                             "gaps": "路径中的未解析动作／回调", "unmatched": "未匹配核心链接槽的注册记录"},
            "summary": {"paths": summary["paths"], "unique_handlers": summary["unique_handlers"],
                        "registration_overlay_edges": summary["registration_overlay_edges"],
                        "scope": summary["scope"]},
            "coverage": {"modes": modes, "unprocessed_modes": summary["unprocessed_modes"],
                         "unmatched_registrations": len(unmatched), "initial_state_assumption": summary["initial_state_assumption"],
                         "notes": summary["notes"]},
            "tables": {"paths": rows, "modes": modes, "gaps": gap_rows, "unmatched": unmatched}}
    return inventory_html(data, title or "iosd 配置模式语法路径",
                          description or "路径来自 iosd 自身的模式初始化、语法节点和注册候选，不使用 CDL。每个 EOL 与跟踪上下文只保留一条较短、未解析步骤较少的示例，不是所有命令语法。<?> 明确标出未知动作；没有此标记也仍需验证权限、参数 flags、注册条件及谓词。候选注册连接不代表实际启动安装顺序。",
                          footer or "搜索覆盖当前表的全部记录。点击行查看条件摘要、参数、注册条件及节点地址；完整条件字段、状态赋值、边轨迹和注册来源保存在 paths.jsonl。模式名来自已确认的注册调用。普通正向 CLI 初始状态是显式分析假设；仅符号跟踪 sense/default/NVGEN，不读取运行时状态或执行谓词。")
