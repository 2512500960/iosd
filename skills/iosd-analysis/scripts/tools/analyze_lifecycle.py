"""Build generic registration/state dependency inventories from saved IR."""
import argparse
import hashlib
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from iosd_helper.lifecycle import analyze_lifecycle, lifecycle_html


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("capture")
    parser.add_argument("graph")
    parser.add_argument("--profile", default="profiles/lifecycle_api_26_01_02.json")
    parser.add_argument("--syntax-paths", action="append", default=[])
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    read = lambda p: json.loads(Path(p).read_text(encoding="utf-8"))
    paths = []
    for path in args.syntax_paths:
        with Path(path).open(encoding="utf-8") as stream:
            paths.extend(json.loads(line) for line in stream)
    result = analyze_lifecycle(read(args.capture), read(args.graph), read(args.profile), paths)
    output = Path(args.output)
    output.mkdir(parents=True, exist_ok=True)
    root = Path(__file__).resolve().parents[1]
    result["summary"]["source_sha256"] = {name: hashlib.sha256((root/name).read_bytes()).hexdigest()
                                             for name in ("iosd_helper/lifecycle.py","iosd_helper/ida_lifecycle.py","iosd_helper/cached_ir.py","tools/analyze_lifecycle.py")}
    result["summary"]["input_sha256"]={str(Path(p).resolve()):hashlib.sha256(Path(p).read_bytes()).hexdigest()
                                         for p in [args.capture,args.graph,args.profile]+args.syntax_paths}
    for key, value in result.items():
        if isinstance(value, list):
            with (output/(key+".jsonl")).open("w",encoding="utf-8") as stream:
                for row in value:
                    stream.write(json.dumps(row, ensure_ascii=False)+"\n")
    (output/"summary.json").write_text(json.dumps({"identity":result["identity"],**result["summary"]},ensure_ascii=False,indent=2),encoding="utf-8")
    (output/"index.html").write_text(lifecycle_html(result),encoding="utf-8")
    print(json.dumps(result["summary"],ensure_ascii=False,indent=2))
    print("Saved",output.resolve())


if __name__ == "__main__":
    main()
