"""Check exported VPDN paths against a fresh read-only IDA extraction."""
import argparse
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from iosd_helper.syntax_paths import semantic_options, registration_overlays


def read(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("graph")
    parser.add_argument("case")
    args = parser.parse_args()
    report, folder = read(args.graph), Path(args.case)
    graph = report["graph"]
    manifest = read(folder / "manifest.json")
    if report["identity"] != manifest["identity"]:
        raise ValueError("Identity mismatch")
    nodes = {n["address"]: n for n in graph["nodes"]}
    overlays, _, _ = registration_overlays(graph, nodes)
    checked_edges = 0

    def validate_path(path):
        nonlocal checked_edges
        for edge in path["edge_trace"]:
            source = edge["source"]
            options = semantic_options(nodes[source], (None, None, None), graph) + overlays.get(source, [])
            if not any((e["target"], e["kind"], e.get("token"), e.get("key")) ==
                       (edge["target"], edge["kind"], edge.get("token"), edge.get("key")) for e in options):
                raise ValueError("Path edge not supported by fresh graph: " + str(edge))
            checked_edges += 1
        terminal = nodes[path["eol_node"]]
        if (terminal["handler_candidate"], terminal["selector_candidate"]) != (path["handler"], path["selector_candidate"]):
            raise ValueError("Terminal identity mismatch")

    test_paths = [json.loads(s) for s in (folder / "test-paths.jsonl").read_text(encoding="utf-8").splitlines()]
    if len(test_paths) != 19 or {p["selector_candidate"] for p in test_paths} != set(range(14)):
        raise ValueError("Pinned test-fragment coverage changed")
    trace_paths = [json.loads(s)["proof"] for s in (folder / "trace-examples.jsonl").read_text(encoding="utf-8").splitlines()]
    config_paths = [json.loads(s) for s in (folder / "config-path-witnesses.jsonl").read_text(encoding="utf-8").splitlines()]
    prefixes = read(folder / "prefix-witnesses.json")
    for path in test_paths + trace_paths + config_paths + [prefixes["test"]] + [r["mode_prefix_witness"] for r in prefixes["trace"]]:
        validate_path(path)
    if graph["pending_addresses"] or graph["unvisited_roots"] or graph["stop_reason"] != "complete_for_configured_edges":
        raise ValueError("Fresh extraction reached an acquisition bound")
    verification = {"identity": report["identity"], "fresh_ida_acquisition": True,
                    "graph_source_sha256": report["source_sha256"],
                    "nodes": len(nodes), "structural_edges": len(graph["edges"]), "registrations": len(graph["registrations"]),
                    "dynamic_link_definitions": len(graph["dynamic_link_definitions"]),
                    "test_paths": len(test_paths), "trace_examples": len(trace_paths), "config_witnesses": len(config_paths),
                    "checked_path_edges": checked_edges, "runtime_execution_tested": False,
                    "limitations": "Checks graph evidence and terminal association, not path constraint satisfiability or actual registration/state"}
    (folder / "ida-verification.json").write_text(json.dumps(verification, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(verification, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
