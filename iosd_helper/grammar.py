"""Partial static parser graphs, separate from ICM configuration/diff nodes.

Only bytes and explicitly configured layout assumptions become graph edges.
Unknown opcodes, missing runtime links and registration conditions stay visible.
"""
from collections import deque
from dataclasses import dataclass, asdict
import json
import re

from .memory import MemoryReadError, decode_pointer, read_cstring
from .grammar_semantics import read_action_registry, decode_action_payload, summarize_graph, node_title
from .grammar_registry import read_link_registry


def address(value):
    return int(value, 0) if isinstance(value, str) else int(value)


@dataclass(frozen=True)
class TransitionLayout:
    size: int = 40
    pointer_mode: str = "little"
    opcode_order: str = "big"
    opcode_offset: int = 16
    accept_offset: int = 0
    alternate_offset: int = 8
    payload_offset: int = 24
    keyword_candidate_opcode: int = 69

    def __post_init__(self):
        if self.size < 32 or self.size > 256:
            raise ValueError("Transition size outside 32..256")
        if self.opcode_order not in ("little", "big"):
            raise ValueError("Invalid opcode order")
        decode_pointer(bytes(8), self.pointer_mode)
        for offset in (self.accept_offset, self.alternate_offset, self.payload_offset):
            if offset < 0 or offset + 8 > self.size:
                raise ValueError("Transition pointer outside record")
        if self.opcode_offset < 0 or self.opcode_offset + 4 > self.size:
            raise ValueError("Opcode outside record")


def registration_roots(memory, tables, sentinel, pointer_mode="little", max_entries=128,
                       cancelled=lambda: False):
    """Observed consumer advances by 16 and compares first pointer with sentinel."""
    if not 1 <= max_entries <= 4096:
        raise ValueError("Invalid registration entry limit")
    rows, unresolved = [], []
    for table in tables:
        base = address(table["address"])
        terminated = False
        for index in range(max_entries):
            if cancelled():
                return rows, unresolved, True
            ea = base + index * 16
            try:
                raw = memory.read(ea, 16)
            except MemoryReadError as exc:
                unresolved.append({"address": ea, "reason": str(exc), "kind": "registration_read_failure"})
                break
            link = decode_pointer(raw[:8], pointer_mode)
            root = decode_pointer(raw[8:], pointer_mode)
            if link == sentinel:
                terminated = True
                break
            if not root or not link:
                unresolved.append({"address": ea, "reason": "NULL registration pair before sentinel",
                                   "kind": "invalid_registration_pair", "raw_hex": raw.hex()})
                break
            rows.append({"address": ea, "table": base, "link_key": link, "root": root,
                         "owner_candidate": table.get("owner_candidate"),
                         "conditions": table.get("conditions", []), "raw_hex": raw.hex(),
                         "source_call_sites": table.get("source_call_sites", [])})
        else:
            unresolved.append({"address": base, "reason": "Registration entry limit before sentinel",
                               "kind": "registration_limit"})
        if not terminated:
            unresolved.append({"address": base, "reason": "Table termination not established",
                               "kind": "unterminated_registration_table"})
    return rows, unresolved, False


def build_static_graph(memory, roots, layout=None, max_nodes=500, stop_addresses=(),
                       cancelled=lambda: False, action_registry=(), function_resolver=None):
    layout = layout or TransitionLayout()
    if not isinstance(max_nodes, int) or isinstance(max_nodes, bool) or not 1 <= max_nodes <= 250000:
        raise ValueError("Node limit outside 1..250000")
    stop = {address(value) for value in stop_addresses}
    pending, queued = deque(), set()
    for root in roots:
        root = address(root)
        if root and root not in queued:
            pending.append(root)
            queued.add(root)
    nodes, edges = [], []
    actions = {entry["opcode"]: entry for entry in action_registry}
    reason = "complete_for_configured_edges"
    while pending:
        if cancelled():
            reason = "cancelled"
            break
        if len(nodes) >= max_nodes:
            reason = "node_limit"
            break
        ea = pending.popleft()
        row = {"address": ea, "status": "unresolved", "handler_candidate": None}
        nodes.append(row)
        if ea in stop:
            row["reason"] = "Configured runtime linkage placeholder; not a proven command terminator"
            continue
        try:
            raw = memory.read(ea, layout.size)
        except MemoryReadError as exc:
            row["reason"] = str(exc)
            continue
        row["raw_hex"] = raw.hex()
        if not any(raw):
            row["reason"] = "Zero record; initialization/terminal semantics unresolved"
            continue
        opcode = int.from_bytes(raw[layout.opcode_offset:layout.opcode_offset + 4], layout.opcode_order)
        row["opcode"] = opcode
        if opcode > 1024:
            row["reason"] = "Opcode outside configured research bound; may not be a transition"
            continue
        ptr = lambda off: decode_pointer(raw[off:off + 8], layout.pointer_mode)
        row.update(status="transition_candidate", payload=ptr(layout.payload_offset),
                   condition_semantics="unresolved", handler_candidate=None)
        if opcode in actions:
            decode_action_payload(memory, row, actions[opcode], layout.pointer_mode, function_resolver)
        if not actions and opcode == layout.keyword_candidate_opcode and row["payload"]:
            try:
                descriptor = memory.read(row["payload"], 16)
                token_ptr = decode_pointer(descriptor[:8], layout.pointer_mode)
                help_ptr = decode_pointer(descriptor[8:], layout.pointer_mode)
                token = read_cstring(memory, token_ptr, 96)
                if not re.fullmatch(r"[A-Za-z0-9_.:/+<>-]{1,80}", token):
                    raise MemoryReadError("Descriptor text is not a simple keyword")
                row.update(keyword_candidate=token, keyword_address=token_ptr,
                           keyword_evidence="opcode/payload pattern; interpreter semantics not yet established",
                           descriptor_raw_hex=descriptor.hex())
                try:
                    row["help_candidate"] = read_cstring(memory, help_ptr, 512) if help_ptr else ""
                except MemoryReadError as exc:
                    row["help_error"] = str(exc)
            except MemoryReadError as exc:
                row["descriptor_error"] = str(exc)
        for offset, kind in ((layout.accept_offset, "accept_candidate"),
                             (layout.alternate_offset, "alternate_link_candidate")):
            target = ptr(offset)
            if not target:
                continue
            edges.append({"source": ea, "target": target, "kind": kind,
                          "field_address": ea + offset, "raw_hex": raw[offset:offset + 8].hex()})
            if target not in queued:
                queued.add(target)
                pending.append(target)
        for edge in row.get("semantic_edges", []):
            target = edge["target"]
            if not target:
                continue
            edges.append({"source": ea, **edge})
            if target not in queued:
                queued.add(target)
                pending.append(target)
    for row in nodes:
        row["display_label"] = node_title(row)
    return {"source": memory.source, "layout": asdict(layout), "nodes": nodes, "edges": edges,
            "pending_addresses": list(pending), "stop_reason": reason,
            "completeness": "partial_static_graph", "mode": "unresolved",
            "warning": "No command paths, hidden flags or handlers are asserted for unknown opcodes/links."}


def extract_profile(memory, profile, input_md5, cancelled=lambda: False, function_resolver=None):
    expected = profile.get("input_md5")
    if not expected or input_md5.lower() != expected.lower():
        raise ValueError("Static grammar profile is pinned to a different input MD5")
    registrations, unresolved, partial = registration_roots(
        memory, profile["registration_tables"], address(profile["sentinel"]),
        max_entries=profile.get("max_registration_entries", 128), cancelled=cancelled)
    registry, registry_errors = [], []
    if profile.get("action_registry"):
        config = profile["action_registry"]
        registry, registry_errors = read_action_registry(memory, address(config["address"]), config["count"])
    roots = list(dict.fromkeys(r["root"] for r in registrations))
    limit = profile.get("graph_root_limit", len(roots))
    if not isinstance(limit, int) or limit < 0:
        raise ValueError("Invalid graph root limit")
    selected_roots = roots[:limit]
    links, link_errors = [], []
    if profile.get("link_registry"):
        config = profile["link_registry"]
        links, link_errors = read_link_registry(memory, address(config["address"]), address(profile["sentinel"]),
                                                 config.get("max_entries", 512))
    modes = profile.get("mode_definitions", [])
    dynamic_links = []
    for definition in profile.get("dynamic_link_definitions", []):
        if definition.get("type") not in (1, 2):
            raise ValueError("Dynamic linkage candidate type must be 1 or 2")
        if not definition.get("evidence") or not definition.get("creator"):
            raise ValueError("Dynamic linkage candidate needs creator and evidence")
        dynamic_links.append({**definition, "key": address(definition["key"]),
                              "root": address(definition["root"]), "creator": address(definition["creator"]),
                              "address": None, "runtime_allocation_verified": False,
                              "origin": "reviewed_dynamic_creation_arguments"})
    extra_roots = list(dict.fromkeys([address(m["root"]) for m in modes] + [r["root"] for r in links]
                                    + [r["root"] for r in dynamic_links]))
    graph = build_static_graph(memory, selected_roots + extra_roots,
                               TransitionLayout(**profile.get("node_layout", {})),
                               max_nodes=profile.get("max_nodes", 500),
                               stop_addresses=profile.get("stop_addresses", []),
                               cancelled=cancelled, action_registry=registry,
                               function_resolver=function_resolver)
    graph.update(registrations=registrations, unresolved_registrations=unresolved,
                 input_md5=input_md5, profile_name=profile.get("name"),
                 cancelled=partial or graph["stop_reason"] == "cancelled")
    graph["action_registry"] = registry
    graph["action_registry_errors"] = registry_errors
    graph["link_registry"] = links
    graph["link_registry_errors"] = link_errors
    graph["dynamic_link_definitions"] = dynamic_links
    graph["mode_definitions"] = modes
    graph["mode_evidence"] = profile.get("mode_evidence", {})
    graph["path_analysis"] = profile.get("path_analysis", {})
    graph["additional_seed_roots"] = extra_roots
    graph["summary"] = summarize_graph(graph)
    graph["selected_roots"] = selected_roots
    graph["unvisited_roots"] = roots[limit:]
    graph["coverage"] = {"registration_rows": len(registrations),
                         "unique_registration_records": len({r["address"] for r in registrations}),
                         "unique_roots": len(roots), "selected_roots": len(selected_roots),
                         "unvisited_roots": len(roots[limit:]),
                         "processed_roots": len(set(selected_roots) & {r["address"] for r in graph["nodes"]}),
                         "pending_nodes": len(graph["pending_addresses"]),
                         "node_limit_reached": graph["stop_reason"] == "node_limit"}
    return graph


def to_dot(graph):
    """Small portable directed graph, with uncertainty preserved in labels."""
    lines = ['digraph iosd_static_parser {', 'rankdir=LR;', 'node [shape=box];']
    known = set()
    for row in graph["nodes"]:
        ea = row["address"]
        known.add(ea)
        label = "%#x\n%s\n%s" % (ea, row.get("keyword_candidate", "op_%s" % row.get("opcode", "?")),
                                    row.get("reason", row.get("semantic_status", row["status"])))
        if row.get("display_label"):
            label = "%#x\n%s\n%s" % (ea, row["display_label"], row.get("reason", row.get("action_name", row["status"])))
        lines.append('"%x" [label=%s];' % (ea, json.dumps(label, ensure_ascii=False)))
    for edge in graph["edges"]:
        target = edge["target"]
        if target not in known:
            known.add(target)
            lines.append('"%x" [label=%s,style=dashed];' % (target, json.dumps("%#x\nunvisited" % target)))
        lines.append('"%x" -> "%x" [label=%s];' % (edge["source"], target, json.dumps(edge["kind"])))
    lines.append('}')
    return "\n".join(lines)
