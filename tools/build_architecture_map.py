"""Generate the saved initialization organization map; no IDA access."""
import argparse
import hashlib
import json
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from iosd_helper.architecture import build_architecture, architecture_html


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("static_capture")
    parser.add_argument("module_capture")
    parser.add_argument("profile")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    read = lambda path: json.loads(Path(path).read_text(encoding="utf-8"))
    model = build_architecture(read(args.static_capture),read(args.module_capture),read(args.profile))
    model["source_sha256"] = {str(Path(path).resolve()):hashlib.sha256(Path(path).read_bytes()).hexdigest()
                              for path in (args.static_capture,args.module_capture,args.profile)}
    output = Path(args.output)
    output.mkdir(parents=True,exist_ok=True)
    (output/"architecture.json").write_text(json.dumps(model,ensure_ascii=False,indent=2),encoding="utf-8")
    (output/"index.html").write_text(architecture_html(model),encoding="utf-8")
    print(json.dumps(model["summary"],ensure_ascii=False))


if __name__ == "__main__":
    main()
