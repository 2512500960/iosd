"""Audit CDL and export bounded candidate paths, exact DAG counts and raw graph."""
import argparse
import hashlib
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from iosd_helper.cdl import load_cdl, resolve_roots, walk_cdl
from iosd_helper.cdl_view import cdl_html


def write_jsonl(path, rows):
    with path.open("w", encoding="utf-8") as stream:
        for row in rows:
            stream.write(json.dumps(row, ensure_ascii=False) + "\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("xml")
    parser.add_argument("--output", required=True, help="Dedicated output directory")
    parser.add_argument("--root", action="append", default=[], help="GUID or exact internal name; repeatable")
    parser.add_argument("--max-paths", type=int, default=10000)
    parser.add_argument("--sample-per-branch", type=int, default=25)
    parser.add_argument("--max-depth", type=int, default=128)
    parser.add_argument("--max-steps", type=int, default=1000000)
    parser.add_argument("--compare-legacy", type=int, default=3, help="Emulate old rule for N highly shared EOLs")
    args = parser.parse_args()
    if not 0 <= args.compare_legacy <= 100:
        parser.error("--compare-legacy must be 0..100")
    path, output = Path(args.xml).resolve(), Path(args.output).resolve()
    print("Parsing", path, flush=True)
    graph = load_cdl(path)
    roots = resolve_roots(graph, args.root)
    print("Analyzing %d GUID nodes, %d explicit edges, roots=%s" % (len(graph.nodes), len(graph.edges), roots), flush=True)
    report, records = walk_cdl(graph, roots, args.max_paths, args.sample_per_branch,
                               args.max_depth, args.max_steps, args.compare_legacy)
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    report["input"] = {"path": str(path), "sha256": digest.hexdigest(), "bytes": path.stat().st_size}
    project = Path(__file__).resolve().parents[1]
    report["source_sha256"] = {name: hashlib.sha256((project / name).read_bytes()).hexdigest()
                               for name in ("iosd_helper/cdl.py", "tools/walk_cdl.py")}
    output.mkdir(parents=True, exist_ok=True)
    write_jsonl(output / "nodes.jsonl", graph.nodes.values())
    write_jsonl(output / "requests.jsonl", graph.requests)
    write_jsonl(output / "edges.jsonl", graph.edges)
    write_jsonl(output / "paths.jsonl", records)
    with (output / "commands.txt").open("w", encoding="utf-8") as stream:
        for record in records:
            stream.write(record["syntax_candidate"] + "\n")
    (output / "summary.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    (output / "index.html").write_text(cdl_html(graph, report, records), encoding="utf-8")
    compact_roots = [{key: root[key] for key in ("root_guid", "reachable_nodes", "reachable_eols",
                     "acyclic", "explicit_edge_path_count", "emitted_paths", "witnessed_eols",
                     "all_explicit_edge_paths_emitted")} for root in report["roots"]]
    print(json.dumps({"roots": compact_roots, "emitted_paths": report["emitted_paths"],
                      "legacy_comparison": report["legacy_comparison"]}, ensure_ascii=False, indent=2), flush=True)
    print("Saved", output, flush=True)


if __name__ == "__main__":
    main()
