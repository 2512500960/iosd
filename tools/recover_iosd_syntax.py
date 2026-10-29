"""Recover mode-scoped syntax witnesses from a saved iosd static graph."""
import argparse
import hashlib
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from iosd_helper.syntax_paths import recover_paths
from iosd_helper.syntax_view import syntax_html


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report")
    parser.add_argument("--output", required=True)
    parser.add_argument("--mode", action="append")
    parser.add_argument("--max-states", type=int, default=250000)
    parser.add_argument("--max-paths", type=int, default=30000)
    args = parser.parse_args()
    source = Path(args.report).resolve()
    print("Loading", source, flush=True)
    report = json.loads(source.read_text(encoding="utf-8"))
    result = recover_paths(report["graph"], args.mode or ("configure", "interface"), args.max_states, args.max_paths)
    result["summary"]["identity"] = report.get("identity", {})
    result["summary"]["acquisition_source_sha256"] = report.get("source_sha256", {})
    root = Path(__file__).resolve().parents[1]
    result["summary"]["recovery_source_sha256"] = {name: hashlib.sha256((root / name).read_bytes()).hexdigest()
                                                  for name in ("iosd_helper/syntax_paths.py", "iosd_helper/syntax_view.py",
                                                               "iosd_helper/catalogue.py", "tools/recover_iosd_syntax.py")}
    output = Path(args.output)
    output.mkdir(parents=True, exist_ok=True)
    (output / "summary.json").write_text(json.dumps(result["summary"], ensure_ascii=False, indent=2), encoding="utf-8")
    with (output / "paths.jsonl").open("w", encoding="utf-8") as stream:
        for path in result["paths"]:
            stream.write(json.dumps(path, ensure_ascii=False) + "\n")
    with (output / "commands.txt").open("w", encoding="utf-8") as stream:
        for path in result["paths"]:
            stream.write("(%s)# %s | handler=%#x | %s\n" % (path["prompt"], path["syntax_candidate"], path["handler"], path["syntax_status"]))
    (output / "index.html").write_text(syntax_html(report.get("identity", {}), result), encoding="utf-8")
    print(json.dumps({"modes": [{k: v for k, v in mode.items() if k != "frontiers"} for mode in result["summary"]["modes"]],
                      "paths": len(result["paths"]), "unmatched_registration_records": len(result["summary"]["registrations_without_static_slot"])},
                     ensure_ascii=False, indent=2), flush=True)
    print("Saved", output.resolve(), flush=True)


if __name__ == "__main__":
    main()
