"""Inspect one candidate node outside IDA, useful for debugging parser logic."""
import argparse
from dataclasses import asdict
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from iosd_helper.memory import ElfCoreMemory
from iosd_helper.structures import NodeLayout, walk_nodes


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("core")
    parser.add_argument("node", type=lambda value: int(value, 0), help="Runtime VA of first node")
    parser.add_argument("--layout", help="NodeLayout JSON profile")
    parser.add_argument("--max-nodes", type=int, default=1000)
    args = parser.parse_args()
    config = {}
    if args.layout:
        with open(args.layout, encoding="utf-8") as stream:
            config = json.load(stream)
    with ElfCoreMemory(args.core) as core:
        result = walk_nodes(core, args.node, NodeLayout(**config), args.max_nodes)
        result["core_path"] = core.path
        result["mappings"] = [asdict(seg) for seg in core.segments]
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if result["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
