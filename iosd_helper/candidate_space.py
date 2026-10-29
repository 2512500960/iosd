"""Lossless acquired evidence plus an unpruned, conditional grammar projection.

This pool is deliberately independent of bounded syntax witnesses. No mode,
runtime state, missing handler, unknown action or unresolved binding excludes a
definition. 'Preserved' refers to acquired evidence, never the entire binary.
"""
from collections import Counter, defaultdict, deque
import json

from .syntax_paths import semantic_options, registration_overlays, number
from .catalogue import inventory_html


def activation_candidates(graph, audit):
    if not audit:
        return []
    if graph.get("input_md5") and graph["input_md5"] != audit.get("identity", {}).get("input_md5"):
        raise ValueError("Trigger audit input MD5 mismatch")
    reverse = defaultdict(list)
    for edge in audit.get("call_edges", []):
        reverse[edge["callee"]].append(edge)
    registrations = defaultdict(list)
    for row in graph.get("registrations", []):
        for site in row.get("source_call_sites", []):
            registrations[site["caller"]].append(row["address"])
    handlers = set(audit.get("known_handlers", []))
    results = []
    for seed, records in registrations.items():
        pending, seen = deque([(seed, [])]), {seed}
        while pending:
            ea, chain = pending.popleft()
            if ea in handlers:
                results.append({"handler": ea, "registration_caller": seed,
                                "registration_records": sorted(set(records)), "call_chain": list(reversed(chain)),
                                "evidence_kind": "handler_contains_registration" if not chain else "direct_call_ancestry",
                                "runtime_feasibility_verified": False, "activation_order_proven": False})
                continue
            if len(chain) >= audit.get("max_depth", 0):
                continue
            for edge in reverse[ea]:
                caller = edge["caller"]
                if caller not in seen:
                    seen.add(caller)
                    pending.append((caller, chain + [edge]))
    return results


def build_candidate_space(graph, audit=None):
    nodes = {node["address"]: node for node in graph["nodes"]}
    overlays, unmatched, rejected = registration_overlays(graph, nodes)
    transitions, terminal_rules = [], []
    for node in graph["nodes"]:
        # Unknown context means both sense/default branches, every comparison
        # target and every predicate outcome remain in the grammar projection.
        for edge in semantic_options(node, (None, None, None), graph):
            transitions.append({"source": node["address"], "projection": "reviewed_normal_cli_or_opaque",
                                **edge})
        if node.get("path_semantics") in ("terminal", "parameter_terminal"):
            base = {"node": node["address"], "handler": node.get("handler_candidate"),
                    "selector_candidate": node.get("selector_candidate"), "availability": "unverified"}
            if node["path_semantics"] == "parameter_terminal":
                parameter = node["parameter"]
                terminal_rules.append({**base, "tokens": [node["keyword_candidate"],
                    "<number:%s..%s>" % (parameter["min"], parameter["max"]), "<cr>"],
                    "condition": "numeric parse succeeds and (sense != 0 or omission flag not set); privilege/other flags unresolved"})
                if node.get("omit_parameter_when_negative"):
                    terminal_rules.append({**base, "tokens": [node["keyword_candidate"], "<cr>"],
                                           "condition": "sense == 0 and omission flag set; other gates unresolved"})
            else:
                terminal_rules.append({**base, "tokens": ["<cr>"], "condition": "EOL runtime gates unresolved"})
    for source, edges in overlays.items():
        transitions.extend({"source": source, "projection": "candidate_registration_installation", **edge}
                           for edge in edges)
    adjacency, reverse = defaultdict(list), defaultdict(list)
    for edge in transitions:
        adjacency[edge["source"]].append(edge["target"])
        reverse[edge["target"]].append(edge["source"])
    mode_candidates = defaultdict(list)
    mode_coverage = []
    for mode in graph.get("mode_definitions", []):
        root = number(mode["root"])
        pending, seen = deque([root]), {root}
        while pending:
            ea = pending.popleft()
            mode_candidates[ea].append(mode["name"])
            for target in adjacency[ea]:
                if target not in seen:
                    seen.add(target)
                    pending.append(target)
        mode_coverage.append({"mode": mode["name"], "root": root, "possible_nodes_in_projection": len(seen),
                              "conditions_evaluated": False, "actual_reachability_proven": False})
    unknown = [node for node in graph["nodes"] if not node.get("path_semantics")
               or node.get("semantic_error") or node.get("status") == "unresolved"
               or node.get("semantic_status") == "action registry mapped; payload semantics unresolved"
               or any(effect.get("effects_unresolved") for effect in node.get("effects", []))]
    conditions = [{"node": node["address"], "condition": node.get("condition"), "effects": node.get("effects", []),
                   "privilege_descriptor_raw_hex": node.get("privilege_descriptor_raw_hex"),
                   "parameter": node.get("parameter"), "command_flags_raw_hex": node.get("command_flags_raw_hex")}
                  for node in graph["nodes"] if node.get("condition") or node.get("effects")
                  or node.get("privilege_descriptor_raw_hex") or node.get("parameter") or node.get("command_flags_raw_hex")]
    unmatched, rejected = set(unmatched), set(rejected)
    dynamic_keys = {slot["key"] for slot in graph.get("dynamic_link_definitions", [])}
    fragments = []
    for index, row in enumerate(graph.get("registrations", [])):
        fragments.append({**row, "mode_candidates": mode_candidates.get(row["root"], []),
                          "binding_status": "core_slot_missing" if index in unmatched else (
                              "static_binding_precondition_unresolved" if index in rejected else (
                                  "dynamic_slot_candidate" if row["link_key"] in dynamic_keys else "core_slot_candidate")),
                          "retained": True, "runtime_registration_proven": False})
    terminals = []
    for node in graph["nodes"]:
        if node.get("handler_candidate") is None:
            continue
        # Nearby words are search hints, never assembled into a purported command.
        words, pending, seen = set(), deque([(node["address"], 0)]), {node["address"]}
        while pending and len(seen) <= 128 and len(words) < 8:
            ea, depth = pending.popleft()
            candidate = nodes.get(ea, {})
            if candidate.get("keyword_candidate"):
                words.add(candidate["keyword_candidate"])
            if depth < 4:
                for source in reverse[ea]:
                    if source not in seen:
                        seen.add(source)
                        pending.append((source, depth + 1))
        terminals.append({"node": node["address"], "action": node.get("action_name"),
                          "handler": node["handler_candidate"], "handler_metadata": node.get("handler_metadata"),
                          "selector_candidate": node.get("selector_candidate"),
                          "mode_candidates": mode_candidates.get(node["address"], []),
                          "nearby_keyword_hints": sorted(words), "hint_is_command_syntax": False,
                          "runtime_available": "unknown"})
    activations = activation_candidates(graph, audit)
    summary = {"scope": "All acquired definitions retained; binary-wide completeness is unproven",
               "preserved_nodes": len(graph["nodes"]), "preserved_structural_edges": len(graph.get("edges", [])),
               "conditional_or_opaque_transitions": len(transitions), "terminal_alternatives": len(terminal_rules),
               "known_handler_definitions": len(terminals),
               "handler_definitions_without_known_mode": sum(not row["mode_candidates"] for row in terminals),
               "registrations_retained": len(fragments), "core_slot_missing": len(unmatched),
               "dynamic_slot_definitions": len(graph.get("dynamic_link_definitions", [])),
               "binding_precondition_unresolved": len(rejected), "unknown_nodes_retained": len(unknown),
               "condition_or_state_records_retained": len(conditions),
               "unresolved_registration_calls_retained": len(graph.get("discovery", {}).get("unresolved_call_sites", [])),
               "mode_projection": mode_coverage, "activation_candidates": len(activations),
               "trigger_audit": {key: audit.get(key) for key in ("scope", "stop_reason", "max_depth", "visited_functions", "pending_functions", "xref_limited_functions", "audit_source_sha256")} if audit else "not provided",
               "registration_call_edges_retained": len(audit.get("call_edges", [])) if audit else 0,
               "runtime_conditions_evaluated": False, "definition_excluded_for_incompleteness": 0,
               "notes": ["No current-mode or normal-initial-state filter is applied to the definition pool.",
                         "All structural edges are retained separately; grammar projection only interprets reviewed normal-CLI semantics and opaque alternatives.",
                         "Unbound fragments, unknown payloads, incomplete token sequences and missing conditions are retained, not classified as absent.",
                         "Cycles, alternatives and conditions stay in the graph; bounded witnesses are a separate presentation layer.",
                         "Handler ancestry is a possible activation clue; it does not prove registration occurs after a user command or that conditions are feasible.",
                         "Computed strings/registrations, indirect calls, external code and unresolved action payload links remain coverage gaps."]}
    return {"summary": summary, "nodes": graph["nodes"], "structural_edges": graph.get("edges", []),
            "transitions": transitions, "terminal_rules": terminal_rules, "fragments": fragments,
            "dynamic_link_definitions": graph.get("dynamic_link_definitions", []),
            "terminals": terminals, "unknown_nodes": unknown, "conditions": conditions, "mode_candidates": dict(mode_candidates),
            "activation_candidates": activations,
            "registration_call_graph": audit.get("call_edges", []) if audit else [],
            "unresolved_calls": graph.get("discovery", {}).get("unresolved_call_sites", [])}


def candidate_space_html(identity, space):
    terminals = [{"node": hex(row["node"]), "handler": hex(row["handler"]),
                  "handler_name": (row.get("handler_metadata") or {}).get("name", ""),
                  "mode_candidates": " | ".join(row["mode_candidates"]) or "模式绑定未知：保留",
                  "nearby_words_not_syntax": " | ".join(row["nearby_keyword_hints"]),
                  "selector": row["selector_candidate"], "availability": "未验证"} for row in space["terminals"]]
    fragments = [{"record": hex(row["address"]), "root": hex(row["root"]), "key": hex(row["link_key"]),
                  "owner": row.get("owner_candidate") or "", "binding": row["binding_status"],
                  "mode_candidates": " | ".join(row["mode_candidates"]) or "未知：不排除",
                  "conditions": " | ".join(row.get("conditions", []))} for row in space["fragments"]]
    unknown = [{"node": hex(row["address"]), "action": row.get("action_name", ""),
                "payload": hex(row.get("payload", 0)),
                "reason": row.get("semantic_error", row.get("reason", "语义未解释：定义保留"))}
               for row in space["unknown_nodes"]]
    activations = [{"handler": hex(row["handler"]), "registration_caller": hex(row["registration_caller"]),
                    "registration_records": " | ".join(hex(ea) for ea in row["registration_records"]),
                    "call_chain": " | ".join("%#x @ %#x → %#x" % (edge["caller"], edge["callsite"], edge["callee"]) for edge in row["call_chain"]) or "handler 内直接含注册调用",
                    "status": "静态调用关系候选；触发顺序和条件未证明"} for row in space["activation_candidates"]]
    calls = [{"call": hex(row["call"]), "caller": hex(row["caller"]), "reason": row["reason"]}
             for row in space["unresolved_calls"]]
    data = {"identity": identity, "labels": {"terminals": "全部已知 handler 定义（含未知模式）",
            "fragments": "全部注册片段", "unknown": "未知／不完整节点：保留", "activation": "可能的注册触发关系", "calls": "未解析注册调用"},
            "summary": {key: value for key, value in space["summary"].items() if key not in ("mode_projection", "notes")},
            "coverage": {"modes": space["summary"]["mode_projection"], "notes": space["summary"]["notes"]},
            "tables": {"terminals": terminals, "fragments": fragments, "unknown": unknown, "activation": activations, "calls": calls}}
    return inventory_html(data, "iosd 静态候选定义池",
                          "这是已提取证据的保留层，不以当前模式、是否完整、是否注册或某次运行状态排除定义。模式未知的片段、未知动作、所有已取得的结构边及条件均另行保留。邻近关键词仅供检索，不是完整语法。优先路径示例是独立浏览摘要，不能代替本候选池。",
                          "每页 200 条，搜索覆盖当前表全部记录。完整节点、结构边、未求值语法分支、组合终结规则、注册和触发候选分别保存在同目录 JSONL。已提取证据全部保留不等于已发现整个二进制的所有定义。")
