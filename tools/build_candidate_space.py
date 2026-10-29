"""Export the acquired definition pool independently of bounded path witnesses."""
import argparse
import hashlib
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from iosd_helper.candidate_space import build_candidate_space, candidate_space_html


def write_jsonl(path, rows):
    with path.open("w", encoding="utf-8") as stream:
        for row in rows:
            stream.write(json.dumps(row, ensure_ascii=False) + "\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report")
    parser.add_argument("--trigger-audit")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    report = json.loads(Path(args.report).read_text(encoding="utf-8"))
    audit = json.loads(Path(args.trigger_audit).read_text(encoding="utf-8")) if args.trigger_audit else None
    space = build_candidate_space(report["graph"], audit)
    output = Path(args.output)
    output.mkdir(parents=True, exist_ok=True)
    summary = {"identity": report.get("identity", {}), **space["summary"],
               "acquisition_source_sha256": report.get("source_sha256", {})}
    root = Path(__file__).resolve().parents[1]
    summary["pool_source_sha256"] = {name: hashlib.sha256((root / name).read_bytes()).hexdigest()
                                      for name in ("iosd_helper/candidate_space.py", "iosd_helper/syntax_paths.py", "tools/build_candidate_space.py")}
    (output / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    for key in ("nodes", "structural_edges", "transitions", "terminal_rules", "fragments", "terminals",
                "unknown_nodes", "conditions", "activation_candidates", "registration_call_graph", "unresolved_calls", "dynamic_link_definitions"):
        rows = space[key]
        if key == "nodes":
            rows = ({**node, "mode_candidates": space["mode_candidates"].get(node["address"], [])} for node in rows)
        write_jsonl(output / (key + ".jsonl"), rows)
    (output / "index.html").write_text(candidate_space_html(report.get("identity", {}), space), encoding="utf-8")
    print(json.dumps({key: value for key, value in space["summary"].items() if key not in ("mode_projection", "notes")}, ensure_ascii=False, indent=2))
    print("Saved", output.resolve())


if __name__ == "__main__":
    main()
