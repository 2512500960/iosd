"""Build a standalone searchable HTML inventory from a saved static CLI report."""
import argparse
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from iosd_helper.catalogue import catalogue_html


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report")
    parser.add_argument("output")
    args = parser.parse_args()
    report = json.loads(Path(args.report).read_text(encoding="utf-8"))
    Path(args.output).write_text(catalogue_html(report), encoding="utf-8")
    print("Saved", args.output)


if __name__ == "__main__":
    main()
