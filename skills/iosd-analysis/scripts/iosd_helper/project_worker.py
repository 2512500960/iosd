"""Local saved-evidence indexing worker. Never connects to IDA or a device."""
import argparse
from contextlib import closing
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from iosd_helper.project import Project, build_index, create_project


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    create = sub.add_parser("create")
    create.add_argument("folder")
    create.add_argument("tree")
    create.add_argument("--identity", required=True, help="Saved IDA identity JSON")
    create.add_argument("--ranges", help="JSON array of image [start RVA,end RVA) pairs")
    for name in ("index", "status", "cancel", "verify"):
        sub.add_parser(name).add_argument("project")
    search = sub.add_parser("search")
    search.add_argument("project")
    search.add_argument("query", nargs="?", default="")
    search.add_argument("--collection", default="paths")
    search.add_argument("--mode", default="")
    args = parser.parse_args()
    if args.command == "create":
        identity = json.loads(Path(args.identity).read_text(encoding="utf-8-sig"))
        ranges = json.loads(Path(args.ranges).read_text(encoding="utf-8-sig")) if args.ranges else []
        project = create_project(args.folder, args.tree, identity, ranges)
        print(project.folder / "project.json")
        return
    project = Project(args.project)
    if args.command == "index":
        if (project.folder / "worker.lock").exists():
            raise ValueError("Project worker lock exists; do not start two workers. Check the recorded PID before recovering a crashed job.")
        (project.folder / "cancel.request").unlink(missing_ok=True)
        build_index(project)
    elif args.command == "status":
        print(json.dumps(project.status(), ensure_ascii=False, indent=2))
    elif args.command == "cancel":
        (project.folder / "cancel.request").touch()
    elif args.command == "verify":
        project.validate_sources()
        with closing(project.connect()) as connection:
            for key, sha, complete in connection.execute("SELECT collection,source_sha256,complete FROM checkpoints"):
                from iosd_helper.project import digest
                if digest(project.source(key)) != sha:
                    raise ValueError("Source hash mismatch: " + key)
                print(key, "complete" if complete else "partial", sha)
    elif args.command == "search":
        count, rows = project.search(args.collection, args.query, args.mode)
        print(json.dumps({"total": count, "rows": rows}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
