"""Enumerate bounded fragment paths without collapsing shared suffixes.

Conditions remain symbolic. Cycles, unknown steps and truncated work stay
visible; this is a projection of acquired evidence, not a CLI emulator.
"""
from collections import Counter

from .syntax_paths import number, semantic_options


def enumerate_fragment(graph, root, prefix=(), max_expansions=100000,
                       max_records=20000, max_depth=256, overlays=None):
    if min(max_expansions, max_records, max_depth) < 1:
        raise ValueError("Fragment bounds must be positive")
    root = number(root)
    nodes = {n["address"]: n for n in graph["nodes"]}
    pending = [(root, (), ())]
    paths, frontiers, visited, deferred_terminals = [], [], set(), []
    expansions = 0
    stop = "exhausted_acyclic_projection"

    def record(address, chain, trace):
        tokens, parameters, conditions, effects, gaps, descriptors = list(prefix), [], [], [], [], []
        for edge in trace:
            source = nodes[edge["source"]]
            if "token" in edge:
                tokens.append(edge["token"])
            if edge.get("condition"):
                conditions.append(edge["condition"])
            if edge.get("gap"):
                gaps.append({"node": source["address"], "reason": edge["gap"]})
            if edge.get("apply_effects"):
                effects.extend({"node": source["address"], **e} for e in source.get("effects", []))
                for effect in source.get("effects", []):
                    if effect.get("kind") == "context_callback":
                        gaps.append({"node": source["address"], "reason": "Context callback effects unresolved",
                                     "function": effect.get("function_candidate")})
            if edge.get("kind") == "parameter_match":
                parameters.append({"node": source["address"], **source.get("parameter", {}),
                                   "help": source.get("help_candidate", "")})
            if "token" in edge:
                descriptors.append({"node": source["address"], "action": source.get("action_name"),
                                    "privilege_raw_hex": source.get("privilege_descriptor_raw_hex"),
                                    "payload": source.get("payload")})
        return {"fragment_root": root, "syntax_candidate": " ".join(tokens),
                "node_addresses": list(chain) + [address], "edge_trace": list(trace),
                "parameters": parameters, "conditions": conditions, "state_effects": effects,
                "gaps": gaps, "token_descriptors": descriptors}

    def frontier(address, chain, trace, reason):
        frontiers.append({**record(address, chain, trace), "address": address, "reason": reason})

    while pending:
        if expansions >= max_expansions or len(paths) + len(frontiers) >= max_records:
            stop = "expansion_limit" if expansions >= max_expansions else "record_limit"
            break
        address, chain, trace = pending.pop()
        expansions += 1
        visited.add(address)
        if address in chain:
            frontier(address, chain, trace, "cycle; repetitions not unrolled")
            continue
        if len(chain) >= max_depth:
            frontier(address, chain, trace, "depth_limit")
            continue
        node = nodes.get(address)
        if not node or node.get("status") == "unresolved":
            frontier(address, chain, trace, (node or {}).get("reason", "target absent from acquired graph"))
            continue
        kind = node.get("path_semantics") if not node.get("semantic_error") else None
        if kind in ("terminal", "parameter_terminal"):
            base = record(address, chain, trace)
            variants = [((), None)]
            if kind == "parameter_terminal":
                parameter = node["parameter"]
                variants = [((node["keyword_candidate"], "<number:%s..%s>" % (parameter["min"], parameter["max"])), False)]
                if node.get("omit_parameter_when_negative"):
                    variants.append(((node["keyword_candidate"],), True))
            for suffix, omitted in variants:
                row = {**base, "syntax_candidate": " ".join(filter(None, [base["syntax_candidate"], *suffix, "<cr>"])),
                       "handler": node.get("handler_candidate"), "eol_node": address,
                       "selector_candidate": node.get("selector_candidate"),
                       "conditions": list(base["conditions"]), "parameters": list(base["parameters"]),
                       "availability": "registration, predicates, parser state, privilege and operation outcomes unverified"}
                if omitted is not None:
                    row["conditions"].append({"node": address, "kind": "combined_terminal_parameter_omission",
                                              "omitted": omitted, "evaluated": False})
                    if not omitted:
                        row["parameters"].append({"node": address, **node["parameter"]})
                if len(paths) + len(frontiers) < max_records:
                    paths.append(row)
                else:
                    deferred_terminals.append(row)
                    stop = "record_limit"
            if kind == "terminal":
                continue
        options = semantic_options(node, (None, None, None), graph) + (overlays or {}).get(address, [])
        if not options and kind not in ("terminal", "parameter_terminal"):
            frontier(address, chain, trace, "parser_stop" if kind == "stop" else "no modeled continuation")
        for edge in reversed(options):
            pending.append((edge["target"], chain + (address,), trace + ({"source": address, **edge},)))

    # Retain every not-yet-expanded route at a bound, rather than silently dropping it.
    deferred = [{"address": ea, "node_addresses": list(chain), "edge_trace": list(trace)}
                for ea, chain, trace in pending]
    deferred.extend({"terminal_variant": row} for row in deferred_terminals)
    acquired = [nodes[ea] for ea in sorted(visited) if ea in nodes]
    edges = [edge for edge in graph.get("edges", []) if edge.get("source") in visited]
    return {"summary": {"root": root, "paths": len(paths), "unique_eols": len({p["eol_node"] for p in paths}),
                        "visited_addresses": len(visited), "expansions": expansions, "stop_reason": stop,
                        "frontiers": len(frontiers), "frontier_reasons": dict(Counter(f["reason"] for f in frontiers)),
                        "deferred_routes": len(deferred), "conditions_evaluated": False,
                        "limits": {"max_expansions": max_expansions, "max_records": max_records, "max_depth": max_depth},
                        "scope": "All explored acyclic projected routes, not all CLI strings or satisfiable paths; explicit candidate overlays only"},
            "paths": paths, "frontiers": frontiers, "deferred_routes": deferred,
            "nodes": acquired, "structural_edges": edges}
