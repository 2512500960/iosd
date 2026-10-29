"""Generic conditional registration, pointer-binding and state dependency analysis.

Consumes saved expression IR. No IDA imports, business handlers or state-machine
constants. Multiple local definitions and incomplete flow remain candidates.
"""
from collections import defaultdict, deque, Counter
import json

from .catalogue import inventory_html


def integer(value):
    return int(value, 0) if isinstance(value, str) else int(value)


def children(expr):
    if isinstance(expr, dict):
        for value in expr.values():
            if isinstance(value, dict):
                yield value
            elif isinstance(value, list):
                yield from (x for x in value if isinstance(x, dict))


def walk(expr):
    if isinstance(expr, dict):
        yield expr
        for child in children(expr):
            yield from walk(child)


def constant(expr):
    if not isinstance(expr, dict):
        return None
    kind = expr.get("kind")
    if kind == "number":
        return expr["value"]
    if kind == "global" and expr.get("is_function"):
        return expr["ea"]
    if kind == "ref":
        arg = expr.get("arg", {})
        if arg.get("kind") == "global":
            return arg["ea"]
        if arg.get("kind") == "member":
            base = constant({"kind": "ref", "arg": arg["base"]})
            return base + arg["offset"] if base is not None else None
    if kind == "cast":
        return constant(expr.get("arg"))
    if kind == "binary":
        left, right = constant(expr.get("left")), constant(expr.get("right"))
        if left is None or right is None:
            return None
        op = expr.get("op")
        return {"add": lambda: left + right, "sub": lambda: left - right,
                "or": lambda: left | right, "and": lambda: left & right,
                "xor": lambda: left ^ right, "mul": lambda: left * right}.get(op, lambda: None)()
    return None


def local_definitions(function):
    result = defaultdict(list)
    for event in function.get("events", []):
        if event["kind"] == "assignment" and event.get("left", {}).get("kind") == "var":
            result[event["left"]["index"]].append(event)
    return result


def expand(expr, definitions, before=None, depth=0, seen=()):
    """Flow-insensitive alternatives, restricted to textually prior assignments.

    Source order is a heuristic, not CFG order. Keep an unresolved alternative
    even with one definition because goto/loops/early exits were not solved.
    """
    if not isinstance(expr, dict) or depth > 10:
        return {"kind": "unknown", "reason": "expression expansion bound", "original": expr}
    if expr.get("kind") == "var":
        index = expr["index"]
        if index in seen:
            return {"kind": "unknown", "reason": "local definition cycle", "index": index}
        matches = [e for e in definitions.get(index, []) if before is None or e["order"] < before]
        if not matches:
            return expr
        values = [expand(e["right"], definitions, e["order"], depth + 1, seen + (index,)) for e in matches[:16]]
        return {"kind": "alternatives", "values": values,
                "guards": [e.get("guards", []) for e in matches[:16]],
                "unknown_possible": True, "truncated_definitions": max(0, len(matches) - 16)}
    result = {}
    for key, value in expr.items():
        if isinstance(value, dict):
            result[key] = expand(value, definitions, before, depth + 1, seen)
        elif isinstance(value, list):
            result[key] = [expand(x, definitions, before, depth + 1, seen) if isinstance(x, dict) else x for x in value]
        else:
            result[key] = value
    return result


def variants(expr, limit=64):
    """Expand alternatives conservatively, with explicit overflow markers."""
    remaining = [limit]
    overflow = [False]
    def visit(value):
        if remaining[0] <= 0:
            return [{"kind": "unknown", "reason": "alternative expansion bound"}]
        if not isinstance(value, dict):
            return [value]
        if value.get("kind") == "alternatives":
            output = []
            for item in value["values"]:
                output.extend(visit(item))
                if len(output) >= limit:
                    overflow[0] = True
                    break
            if value.get("unknown_possible"):
                output.append({"kind": "unknown", "reason": "local control flow unresolved"})
            return output[:limit] + ([{"kind": "unknown", "reason": "alternative expansion bound"}] if len(output) > limit else [])
        rows = [{}]
        for key, child in value.items():
            options = visit(child) if isinstance(child, dict) else [child]
            combined = [{**row, key: option} for row in rows for option in options]
            if len(combined)>limit:overflow[0]=True
            rows = combined[:limit]
        remaining[0] -= 1
        return rows
    result = visit(expr)
    if overflow[0]:result.append({"kind":"unknown","reason":"alternative expansion bound; original expression retained"})
    return result


def slot_keys(expr):
    """Candidate alias keys from the address consumed by a pointer dereference.

    Matching a getter does not prove it returned the same slot at runtime.
    """
    keys = set()
    for variant in variants(expr):
        for item in walk(variant):
            if item.get("kind") != "deref":
                continue
            for address in walk(item.get("arg", {})):
                if address.get("kind") == "call" and address.get("target") is not None:
                    # Only no-argument getters are alias candidates here.
                    if not address.get("args"):
                        keys.add(("getter", address["target"]))
            pointer = constant(item.get("arg"))
            if pointer is not None:
                keys.add(("absolute_slot", pointer & 0x7fffffffffffffff))
    return keys


def function_values(expr):
    # Byte-swap/cast wrappers remain in the evidence; a referenced function is
    # only a binding candidate, never assumed to be the actual encoded value.
    return {item["rva"] for item in walk(expr) if item.get("kind") == "global" and item.get("is_function")}


def image_argument(expr, base):
    values = set()
    for variant in variants(expr):
        value = constant(variant)
        if value is not None:
            value &= 0x7fffffffffffffff
            if value >= base:
                values.add(value - base)
    return sorted(values)


def command_index(graph, graph_base, paths=()):
    result = defaultdict(list)
    syntax = defaultdict(set)
    for path in paths:
        syntax[(path["handler"] - graph_base, path.get("selector_candidate"))].add(path["syntax_candidate"])
    for node in graph["nodes"]:
        handler = node.get("handler_candidate")
        if handler is None:
            continue
        selector = node.get("selector_candidate")
        result[handler - graph_base].append({"eol_rva": node["address"] - graph_base,
                                            "selector": selector, "syntax_witnesses": sorted(syntax[(handler - graph_base, selector)]),
                                            "syntax_is_exhaustive": False})
    return dict(result)


def analyze_lifecycle(capture, graph_report, profile, paths=()):
    identities = (capture["identity"], graph_report["identity"])
    if any(identity["input_md5"] != profile["input_md5"] for identity in identities):
        raise ValueError("Lifecycle input MD5 mismatch")
    base = capture["identity"]["imagebase"]
    api = {integer(a["rva"]): a for a in profile["apis"]}
    commands = command_index(graph_report["graph"], graph_report["identity"]["imagebase"], paths)
    functions = {f["rva"]: f for f in capture.get("functions", [])}
    calls, registrations, links, bindings, indirect, accesses, unknown = [], [], [], [], [], [], []
    callback_members = []
    for function in functions.values():
        caller, definitions = function["rva"], local_definitions(function)
        if function.get("identity_verified") is False:
            unknown.append({"function":caller,"reason":"cached function has no independently verified input identity; candidate only"})
        if function.get("source_truncated"):
            unknown.append({"function":caller,"reason":"cached decompilation truncated; all acquired source retained"})
        if function.get("error"):
            unknown.append({"function": caller, "reason": function["error"]})
        if function.get("truncated"):
            unknown.append({"function": caller, "reason": "function expression limit; unvisited events remain unknown"})
        opaque=sum(1 for event in function.get("events",[]) for item in walk(event) if item.get("kind") in ("unknown","unknown_guard"))
        if opaque:
            unknown.append({"function":caller,"reason":"unsupported expressions/guards retained in function IR and source","expression_occurrences":opaque})
        for event in function.get("events", []):
            context = {"caller": caller, "site_rva": event.get("site_rva"), "guards": event.get("guards", []),
                       "path_conditions_complete": False, "evidence_order": event.get("order"),
                       "source_offset":event.get("source_offset"),"evidence_source":function.get("evidence_source"),
                       "identity_verified":function.get("identity_verified",True)}
            if event["kind"] == "global_access":
                accesses.append({**context, **event})
            elif event["kind"] == "assignment":
                lhs = expand(event["left"], definitions, event["order"])
                rhs = expand(event["right"], definitions, event["order"])
                for slot in slot_keys(lhs):
                    for target in function_values(rhs):
                        bindings.append({**context, "slot": list(slot), "target": target,
                                         "left_expression": lhs, "right_expression": rhs,
                                         "precision": "getter/slot expression candidate; runtime alias and encoding unverified"})
            elif event["kind"] == "call":
                target = event.get("target")
                if target is not None:
                    calls.append({**context, "callee": target, "kind": "direct_call"})
                else:
                    expression = expand(event.get("target_expression", {}), definitions, event["order"])
                    indirect.append({**context, "target_expression": expression,
                                     "slot_candidates": [list(k) for k in sorted(slot_keys(expression))]})
                spec = api.get(target)
                if not spec:
                    continue
                arguments = [expand(arg, definitions, event["order"]) for arg in event.get("args", [])]
                def argument(name):
                    index = spec.get(name)
                    return arguments[index] if index is not None and index < len(arguments) else {"kind": "unknown", "reason": "API argument absent"}
                record = {**context, "api_rva": target, "role": spec["role"], "arguments": arguments,
                          "api_semantics_evidence": spec["evidence"], "installed": "unknown"}
                if spec["role"] in ("register_table", "register_fragment"):
                    record["tables"] = image_argument(argument("table_arg"), base) if spec["role"] == "register_table" else []
                    record["keys"] = image_argument(argument("key_arg"), base) if spec["role"] == "register_fragment" else []
                    record["roots"] = image_argument(argument("root_arg"), base) if spec["role"] == "register_fragment" else []
                    record["arguments_resolved"] = bool(record["tables"] or (record["keys"] and record["roots"]))
                    registrations.append(record)
                elif spec["role"] == "create_link":
                    links.append({**record, "keys": image_argument(argument("key_arg"), base),
                                  "anchors": image_argument(argument("root_arg"), base), "type": spec["type"],
                                  "heap_address": None, "allocation_verified": False})
                elif spec["role"] == "register_callback":
                    callback_members.append({**record, "function_candidates": sorted(function_values(argument("function_arg"))),
                                             "registry_expression": argument("registry_arg")})
    binding_index = defaultdict(list)
    for binding in bindings:
        binding_index[tuple(binding["slot"])].append(binding)
    for call in indirect:
        candidates = []
        for key in call["slot_candidates"]:
            for binding in binding_index[tuple(key)]:
                candidates.append(binding)
                calls.append({**call, "callee": binding["target"], "kind": "indirect_binding_candidate", "binding": binding})
        call["binding_candidates"] = candidates
        call["resolved_at_runtime"] = False
        if not candidates:
            unknown.append({**call, "reason": "indirect target unresolved; retained"})
    # Include all acquired direct xrefs, even functions not decompiled this batch.
    seen_calls = {(e["caller"], e["callee"], e.get("site_rva")) for e in calls}
    for edge in capture.get("call_edges", []):
        key = edge["caller"], edge["callee"], edge.get("site_rva")
        if key not in seen_calls:
            calls.append({**edge, "kind": "direct_xref", "guards": [], "path_conditions_complete": False})
    seen_reg_sites = {(r["caller"], r.get("site_rva"), r["api_rva"]) for r in registrations + links + callback_members}
    graph_base = graph_report["identity"]["imagebase"]
    acquired_tables = defaultdict(set)
    for row in graph_report["graph"].get("registrations",[]):
        for site in row.get("source_call_sites",[]):
            acquired_tables[(site["caller"]-graph_base,site["call"]-graph_base)].add(row["table"]-graph_base)
    for edge in capture.get("api_xrefs", []):
        if (edge["caller"], edge.get("site_rva"), edge["callee"]) not in seen_reg_sites:
            unknown.append({**edge, "reason": "API reference retained; arguments/function not acquired", "api_role": api[edge["callee"]]["role"]})
            spec = api[edge["callee"]]
            record = {"caller":edge["caller"],"site_rva":edge.get("site_rva"),"api_rva":edge["callee"],
                      "role":spec["role"],"arguments":[],"guards":[],"path_conditions_complete":False,
                      "api_semantics_evidence":spec["evidence"],"installed":"unknown",
                      "evidence_source":"direct API xref; function expressions not acquired"}
            if spec["role"] in ("register_table","register_fragment"):
                tables = sorted(acquired_tables[(edge["caller"],edge.get("site_rva"))]) if spec["role"]=="register_table" else []
                registrations.append({**record,"tables":tables,"keys":[],"roots":[],"arguments_resolved":False,
                                      "table_source":"prior static argument-recovery candidate" if tables else "unknown"})
            elif spec["role"]=="create_link":
                links.append({**record,"keys":[],"anchors":[],"type":spec["type"],"heap_address":None,"allocation_verified":False})
            elif spec["role"]=="register_callback":
                callback_members.append({**record,"function_candidates":[],"registry_expression":{"kind":"unknown","reason":"arguments not acquired"}})
    reverse = defaultdict(list)
    for call in calls:
        reverse[call["callee"]].append(call)
    max_depth = profile.get("limits", {}).get("max_depth", 4)
    max_relations = profile.get("limits", {}).get("max_relations", 20000)
    ancestor_cache = {}
    ancestry_frontiers = []
    def ancestors(caller):
        if caller in ancestor_cache:
            return ancestor_cache[caller]
        pending, seen = deque([(caller, [])]), {caller}
        result = []
        while pending:
            current, chain = pending.popleft()
            if current in commands:
                result.append({"handler": current, "commands": commands[current], "call_chain": list(reversed(chain)),
                               "selector_status": "unresolved; command group retained", "feasibility_verified": False})
                continue
            if len(chain) >= max_depth:
                ancestry_frontiers.append({"origin":caller,"function":current,"reason":"ancestry depth bound"})
                continue
            for edge in reverse[current]:
                if edge["caller"] not in seen:
                    seen.add(edge["caller"])
                    pending.append((edge["caller"], chain + [edge]))
        ancestor_cache[caller] = result
        return result
    triggers = []
    for index, registration in enumerate(registrations):
        for relation in ancestors(registration["caller"]):
            if len(triggers) >= max_relations:
                unknown.append({"registration_index":index,"reason":"trigger relation bound; event and all acquired call edges retained"})
                break
            triggers.append({**relation, "registration_index": index, "registration": registration,
                             "status": "conditional trigger candidate; selector and all path conditions not yet proven"})
    writers, readers = defaultdict(list), defaultdict(list)
    for access in accesses:
        (writers if access["access"] == "write" else readers)[access["global_rva"]].append(access)
    dependencies = []
    deferred_dependency_groups = []
    for variable, writes in writers.items():
        for write in writes:
            origin = ancestors(write["caller"])
            if not origin:
                continue
            for read in readers[variable]:
                if len(dependencies) >= max_relations:
                    deferred_dependency_groups.append({"global_rva": variable, "writer": write, "readers": readers[variable], "reason": "relation limit"})
                    break
                dependencies.append({"global_rva": variable, "writer": write, "reader": read,
                                     "writer_command_candidates": origin, "reader_commands": commands.get(read["caller"], []),
                                     "kind": "write_may_affect_guard" if read.get("in_guard") else "write_may_affect_read",
                                     "predicate_truth_evaluated": False, "state_name": "unclassified"})
    unknown.extend({"function": rva, "reason": "function pending acquisition"} for rva in capture.get("pending_functions", []))
    unknown.extend(capture.get("unknown_inputs",[]))
    unknown.extend(capture.get("xref_limits",[]))
    trigger_limit = len(triggers) >= max_relations
    summary = {"scope": "Generic conditional evidence analysis; not a CFG feasibility proof or command enumeration",
               "functions": len(functions), "api_references": len(capture.get("api_xrefs", [])),
               "registration_events": len(registrations), "dynamic_link_events": len(links),
               "indirect_calls": len(indirect), "binding_candidates": len(bindings), "callback_memberships": len(callback_members),
               "trigger_relations": len(triggers), "trigger_limit_reached": trigger_limit,
               "state_accesses": len(accesses), "state_dependencies": len(dependencies),
               "unknown_records": len(unknown), "acquisition": capture.get("coverage", {}),
               "address_space": "RVA for image references; original expressions retain actual capture EA",
               "runtime_verified": False, "deferred_dependency_groups": len(deferred_dependency_groups),
               "trigger_ancestry_scope": "One short witness per ancestor handler; all acquired call edges retained separately"}
    return {"identity": capture["identity"], "graph_identity": graph_report["identity"], "summary": summary,
            "functions": list(functions.values()), "registrations": registrations, "dynamic_links": links,
            "bindings": bindings, "indirect_calls": indirect, "callback_memberships": callback_members,
            "call_edges": calls, "trigger_candidates": triggers, "state_accesses": accesses,
            "state_dependencies": dependencies, "unknown": unknown, "deferred_dependency_groups": deferred_dependency_groups,
            "ancestry_frontiers":ancestry_frontiers}


def lifecycle_html(result):
    hx = lambda x: hex(x) if x is not None else "unknown"
    triggers = []
    for row in result["trigger_candidates"]:
        syntax = sorted({s for command in row["commands"] for s in command["syntax_witnesses"]})
        triggers.append({"handler_rva": hx(row["handler"]), "selector_candidates": " | ".join(map(str,sorted({c["selector"] for c in row["commands"]},key=str))),
                             "syntax_witnesses": " | ".join(syntax[:20]) or "语法未知，定义保留",
                             "syntax_display_limited":len(syntax)>20,
                             "registration_caller_rva": hx(row["registration"]["caller"]),
                             "api_rva": hx(row["registration"]["api_rva"]),
                             "status": "触发候选组；尚未证明各 selector 必定执行注册", "proof": row})
    tables = {"triggers": triggers,
              "links": [{"caller_rva": hx(r["caller"]), "site_rva": hx(r["site_rva"]), "type": r["type"],
                         "keys_rva": " | ".join(map(hx, r["keys"])) or "unknown",
                         "anchors_rva": " | ".join(map(hx, r["anchors"])) or "unknown", "heap_address": "未验证", "proof": r} for r in result["dynamic_links"]],
              "indirect": [{"caller_rva": hx(r["caller"]), "site_rva": hx(r["site_rva"]),
                            "bindings": len(r["binding_candidates"]), "status": "候选绑定" if r["binding_candidates"] else "未知，保留", "proof": r} for r in result["indirect_calls"]],
              "states": [{"global_rva": hx(r["global_rva"]), "writer_rva": hx(r["writer"]["caller"]),
                          "reader_rva": hx(r["reader"]["caller"]), "relation": r["kind"], "status": "未求值", "proof": r} for r in result["state_dependencies"]],
              "registrations": [{"caller_rva": hx(r["caller"]), "api_rva": hx(r["api_rva"]),
                                 "table_rva": " | ".join(map(hx, r["tables"])) or "unknown / key-root API",
                                 "arguments_resolved": r["arguments_resolved"], "proof": r} for r in result["registrations"]],
              "unknown": [{"reason": r["reason"], "function_rva": hx(r.get("function", r.get("caller"))), "proof": r} for r in result["unknown"]]}
    return inventory_html({"identity": result["identity"], "summary": result["summary"],
                           "coverage": {"notes": ["未知与未采集函数保留；带条件的关系不等于真实执行顺序。", "所有地址列均为 RVA，重定位时加当前 IDB imagebase；堆地址不能如此换算。", "selector 未完成控制流判定，同 handler 的命令显示为候选组。"]},
                           "labels": {"triggers": "命令到注册的候选关系", "links": "动态链接创建调用", "indirect": "间接调用与候选绑定", "states": "状态写读依赖", "registrations": "注册提交事件", "unknown": "未知与未采集项"},
                           "hidden_columns": ["proof"], "tables": tables},
                          "iosd 通用注册和状态依赖分析",
                          "规则依据注册 API、表达式、调用关系和状态访问，不按业务名称筛选。共享 handler 的 selector 保留为候选组，未解析参数、间接调用和未采集函数单独列出。条件来自局部语法上下文，尚未覆盖所有早返回、goto 和跨函数状态约束。",
                          "点击行查看完整证据；同目录 JSONL 保留完整调用边、状态访问和未知项。RVA 只能用于同一输入映像，实际注册和内存状态需独立快照验证。")
