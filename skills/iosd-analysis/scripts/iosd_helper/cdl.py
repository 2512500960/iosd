"""Read BinOS CDL as evidence, keeping explicit edges separate from filter links.

Explicit-edge paths are syntactic candidates. Conditions, CLI modes, request
dispatch and parameter domains are not evaluated by this module.
"""
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
import xml.etree.ElementTree as ET


@dataclass
class CdlGraph:
    nodes: dict
    requests: list
    edges: list
    adjacency: dict
    edge_evidence: dict
    declared_node_count: int
    errors: list


def local_tag(tag):
    return tag.rsplit("}", 1)[-1]


def metadata(element):
    record = {"kind": local_tag(element.tag), "attributes": dict(element.attrib)}
    if list(element):
        record["children"] = [metadata(child) for child in element]
    if element.text and element.text.strip():
        record["text"] = element.text.strip()
    return record


def load_cdl(path):
    """Honor the XML encoding declaration; reject malformed XML/duplicate GUIDs."""
    nodes, requests, edges, errors = {}, [], [], []
    declared, stack = None, []
    for event, element in ET.iterparse(path, events=("start", "end")):
        if event == "start":
            stack.append(element)
            continue
        kind, attrs = local_tag(element.tag), dict(element.attrib)
        parent = stack[-2] if len(stack) > 1 else None
        parent_kind = local_tag(parent.tag) if parent is not None else None
        if kind == "nodes":
            if attrs.get("node-num") is not None:
                declared = int(attrs["node-num"])
        elif parent_kind == "edges" and kind == "edge":
            if not attrs.get("from-guid") or not attrs.get("to-guid"):
                errors.append({"kind": "edge_without_guid", "attributes": attrs})
            else:
                edges.append({"source": int(attrs["from-guid"]), "target": int(attrs["to-guid"]),
                              "attributes": attrs, "metadata": [metadata(child) for child in element]})
        elif parent_kind == "nodes" and kind == "request":
            requests.append(metadata(element))
        elif parent_kind == "nodes" and "guid" in attrs:
            guid = int(attrs["guid"])
            if guid in nodes:
                raise ValueError("Duplicate CDL GUID %d" % guid)
            nodes[guid] = {"guid": guid, **metadata(element)}
        if parent_kind in ("nodes", "edges"):
            element.clear()
            parent.remove(element)
        stack.pop()
    adjacency, evidence, pairs = defaultdict(list), defaultdict(list), set()
    for edge in edges:
        pair = edge["source"], edge["target"]
        if any(guid not in nodes for guid in pair):
            errors.append({"kind": "dangling_edge", "source": pair[0], "target": pair[1]})
            continue
        evidence[pair].append(edge)
        if pair not in pairs:
            pairs.add(pair)
            adjacency[pair[0]].append(pair[1])
    return CdlGraph(nodes, requests, edges, dict(adjacency), dict(evidence), declared, errors)


def resolve_roots(graph, selectors=()):
    if selectors:
        roots = []
        for selector in selectors:
            text = str(selector)
            matches = [guid for guid, node in graph.nodes.items()
                       if node["attributes"].get("name") == text]
            if not matches:
                try:
                    guid = int(text, 0)
                except ValueError:
                    raise ValueError("No root named %r" % text)
                matches = [guid] if guid in graph.nodes else []
            if len(matches) != 1:
                raise ValueError("Root selector %r has %d matches; use an exact GUID" % (text, len(matches)))
            if matches[0] not in roots:
                roots.append(matches[0])
        return roots
    roots = [guid for guid, node in graph.nodes.items()
             if node["attributes"].get("name") == "NODE_DAG_ROOT"]
    if not roots:
        targets = {target for values in graph.adjacency.values() for target in values}
        roots = [guid for guid in graph.adjacency if guid not in targets]
    if not roots:
        raise ValueError("No explicit root discovered; supply --root GUID or internal name")
    return roots


def successors(graph, guid):
    # An EOL is a terminal for this analysis even if a future file has out-edges.
    return () if graph.nodes[guid]["kind"] == "eol" else graph.adjacency.get(guid, ())


def reachable_parents(graph, root):
    parents, pending = {root: None}, deque([root])
    while pending:
        guid = pending.popleft()
        for target in successors(graph, guid):
            if target not in parents:
                parents[target] = guid
                pending.append(target)
    return parents


def analyze_root(graph, root):
    parents = reachable_parents(graph, root)
    reached = set(parents)
    indegree = dict.fromkeys(reached, 0)
    reverse = defaultdict(list)
    for guid in reached:
        for target in successors(graph, guid):
            indegree[target] += 1
            reverse[target].append(guid)
    pending = deque(guid for guid, degree in indegree.items() if degree == 0)
    order = []
    while pending:
        guid = pending.popleft()
        order.append(guid)
        for target in successors(graph, guid):
            indegree[target] -= 1
            if indegree[target] == 0:
                pending.append(target)
    terminals = sorted(guid for guid in reached if graph.nodes[guid]["kind"] == "eol")
    productive, pending = set(terminals), deque(terminals)
    while pending:
        guid = pending.popleft()
        for source in reverse[guid]:
            if source not in productive:
                productive.add(source)
                pending.append(source)
    counts, forward, depth = {}, {root: 1}, {}
    acyclic = len(order) == len(reached)
    if acyclic:
        for guid in order:
            for target in successors(graph, guid):
                forward[target] = forward.get(target, 0) + forward.get(guid, 0)
        for guid in reversed(order):
            if graph.nodes[guid]["kind"] == "eol":
                counts[guid], depth[guid] = 1, 0
            else:
                counts[guid] = sum(counts[target] for target in successors(graph, guid))
                depth[guid] = max((depth[target] + 1 for target in successors(graph, guid)
                                   if counts[target]), default=0)
    branches = [{"guid": target, "kind": graph.nodes[target]["kind"],
                 "name": graph.nodes[target]["attributes"].get("name", ""),
                 "keyword": graph.nodes[target]["attributes"].get("str", ""),
                 "path_count": str(counts[target]) if acyclic else None}
                for target in successors(graph, root)]
    summary = {"root_guid": root, "root_name": graph.nodes[root]["attributes"].get("name", ""),
               "reachable_nodes": len(reached), "reachable_types": dict(Counter(graph.nodes[g]["kind"] for g in reached)),
               "reachable_eols": len(terminals), "acyclic": acyclic,
               "topological_residual_nodes": len(reached) - len(order),
               "explicit_edge_path_count": str(counts[root]) if acyclic else None,
               "longest_eol_path_edges": depth.get(root), "branches": branches,
               "unreachable_eol_guids": sorted(g for g, n in graph.nodes.items()
                                               if n["kind"] == "eol" and g not in reached)}
    return {"summary": summary, "parents": parents, "terminals": terminals,
            "productive": productive, "counts": counts, "forward_counts": forward}


def candidate_paths(graph, start, productive, limit=25, max_depth=128, max_steps=1000000):
    """Iterative, path-local cycle detection. Shared suffixes remain reusable."""
    stats = {"emitted": 0, "steps": 0, "cycle_edges_skipped": 0,
             "depth_edges_skipped": 0, "stop_reason": "exhausted"}
    def generate():
        if start not in productive:
            return
        path, active = [start], {start}
        stack = [None]
        while stack:
            guid = path[-1]
            if graph.nodes[guid]["kind"] == "eol":
                stats["emitted"] += 1
                yield list(path)
                active.remove(path.pop())
                stack.pop()
                if stats["emitted"] >= limit:
                    stats["stop_reason"] = "path_limit"
                    return
                continue
            if stack[-1] is None:
                stack[-1] = iter(successors(graph, guid))
            target = next(stack[-1], None)
            if target is None:
                active.remove(path.pop())
                stack.pop()
                continue
            stats["steps"] += 1
            if stats["steps"] > max_steps:
                stats["stop_reason"] = "step_limit"
                return
            if target not in productive:
                continue
            if target in active:
                stats["cycle_edges_skipped"] += 1
                continue
            if len(path) >= max_depth:
                stats["depth_edges_skipped"] += 1
                continue
            path.append(target)
            active.add(target)
            stack.append(None)
    return generate(), stats


def witness_path(parents, terminal):
    path = []
    while terminal is not None:
        path.append(terminal)
        terminal = parents[terminal]
    return list(reversed(path))


def path_record(graph, root, path, source):
    tokens, unknown = [], []
    for guid in path:
        node = graph.nodes[guid]
        attrs, kind = node["attributes"], node["kind"]
        if kind == "keyword" and attrs.get("name") == "NODE_DAG_ROOT":
            continue
        if kind == "keyword":
            tokens.append(attrs.get("str", "<?keyword:%d>" % guid))
        elif kind == "value":
            tokens.append("<%s:%s>" % (attrs.get("macro", "value"), attrs.get("name", str(guid))))
        elif kind == "eol":
            tokens.append("<cr>")
        else:
            tokens.append("<?%s:%s>" % (kind, attrs.get("name", str(guid))))
            unknown.append(guid)
    annotations = []
    for a, b in zip(path, path[1:]):
        alternatives = [edge["metadata"] for edge in graph.edge_evidence[a, b]]
        if any(alternatives):
            annotations.append({"source": a, "target": b, "metadata_alternatives": alternatives})
    return {"root_guid": root, "node_guids": path, "syntax_candidate": " ".join(tokens),
            "eol_guid": path[-1], "eol_name": graph.nodes[path[-1]]["attributes"].get("name", ""),
            "source": source, "conditions_evaluated": False, "mode": "unresolved",
            "edge_annotations": annotations,
            "unknown_node_guids": unknown}


def legacy_count_for_terminal(graph, root, terminal, max_steps=1000000):
    """Emulate the old C++ blocking rule; do not execute the old program."""
    blocked, active, path = set(), {root}, [root]
    stack, count, steps = [None], 0, 0
    while stack:
        guid = path[-1]
        if guid == terminal:
            count += 1
            active.remove(path.pop())
            stack.pop()
            continue
        if stack[-1] is None:
            stack[-1] = iter(graph.adjacency.get(guid, ()))
        target = next(stack[-1], None)
        if target is None:
            blocked.add(guid)
            active.remove(path.pop())
            stack.pop()
            continue
        steps += 1
        if steps > max_steps:
            return {"emitted_paths": count, "steps": steps, "stop_reason": "step_limit"}
        if target in blocked:
            continue
        if target in active:
            return {"emitted_paths": count, "steps": steps, "stop_reason": "cycle_old_program_would_exit"}
        active.add(target)
        path.append(target)
        stack.append(None)
    return {"emitted_paths": count, "steps": steps, "stop_reason": "exhausted"}


def walk_cdl(graph, roots, max_paths=10000, sample_per_branch=25, max_depth=128,
             max_steps=1000000, compare_legacy=0):
    if not 1 <= max_paths <= 1000000 or not 1 <= sample_per_branch <= 10000:
        raise ValueError("Invalid path/sample limit")
    if not 2 <= max_depth <= 4096 or not 1 <= max_steps <= 100000000:
        raise ValueError("Invalid depth/step limit")
    records, seen, summaries, comparisons = [], set(), [], []
    batches = []
    for root in roots:
        analysis = analyze_root(graph, root)
        summary = analysis["summary"]
        summaries.append(summary)
        def add(path, source):
            key = (root, tuple(path))
            if key not in seen and len(records) < max_paths:
                seen.add(key)
                records.append(path_record(graph, root, path, source))
        count = analysis["counts"].get(root)
        if count is not None and count <= max_paths - len(records):
            paths, stats = candidate_paths(graph, root, analysis["productive"], max_paths,
                                           max_depth, max_steps)
            for path in paths:
                add(path, "all_explicit_edge_paths")
            batches.append({"root_guid": root, "kind": "enumeration", **stats})
        else:
            for terminal in analysis["terminals"]:
                path = witness_path(analysis["parents"], terminal)
                if len(path) <= max_depth:
                    add(path, "shortest_eol_witness")
            for branch in successors(graph, root):
                if len(records) >= max_paths:
                    break
                paths, stats = candidate_paths(graph, branch, analysis["productive"], sample_per_branch,
                                               max_depth - 1, max_steps)
                for suffix in paths:
                    add([root] + suffix, "branch_sample")
                batches.append({"root_guid": root, "branch_guid": branch, "kind": "sample", **stats})
        emitted = [record for record in records if record["root_guid"] == root]
        summary["emitted_paths"] = len(emitted)
        summary["emitted_unique_syntaxes"] = len({r["syntax_candidate"] for r in emitted})
        summary["witnessed_eols"] = len({r["eol_guid"] for r in emitted})
        summary["all_explicit_edge_paths_emitted"] = count is not None and len(emitted) == count
        if compare_legacy and summary["acyclic"]:
            targets = sorted(analysis["terminals"], key=lambda g: (-analysis["forward_counts"].get(g, 0), g))
            for target in targets[:compare_legacy]:
                comparisons.append({"root_guid": root, "eol_guid": target,
                                    "eol_name": graph.nodes[target]["attributes"].get("name", ""),
                                    "exact_explicit_edge_paths": str(analysis["forward_counts"].get(target, 0)),
                                    "legacy_algorithm_emulation": legacy_count_for_terminal(graph, root, target, max_steps)})
    types = Counter(node["kind"] for node in graph.nodes.values())
    types["request"] += len(graph.requests)
    report = {"schema_version": 1, "node_types": dict(types), "guid_nodes": len(graph.nodes),
              "declared_guid_nodes": graph.declared_node_count,
              "guid_node_count_matches_header": graph.declared_node_count == len(graph.nodes),
              "explicit_edges": len(graph.edges), "unique_valid_edges": sum(map(len, graph.adjacency.values())),
              "edges_with_metadata": sum(bool(e["metadata"]) for e in graph.edges),
              "edge_metadata_types": dict(Counter(m["kind"] for e in graph.edges for m in e["metadata"])),
              "filter_nodes": types["filter"],
              "explicit_edges_touching_filters": sum(any(graph.nodes.get(e[side], {}).get("kind") == "filter"
                                                            for side in ("source", "target")) for e in graph.edges),
              "errors": graph.errors, "roots": summaries, "emitted_paths": len(records),
              "max_paths": max_paths, "sample_per_branch": sample_per_branch,
              "max_depth": max_depth, "max_steps_per_batch": max_steps,
              "traversal_batches": batches, "legacy_comparison": comparisons,
              "conditions_evaluated": False, "runtime_commands_confirmed": False,
              "notes": ["Counts refer to paths in explicit XML edges, not runnable or distinct CLI commands.",
                        "Filter definitions and edge filter-ref/set/set-tdl metadata are retained, not evaluated.",
                        "Request/bundle entries are retained without inferring a handler or an EOL association.",
                        "CLI modes are unresolved; a keyword named config does not establish a configuration mode."]}
    return report, records
