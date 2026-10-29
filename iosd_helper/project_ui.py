"""Native IDA project browser. Only the final jump accesses IDA addresses."""
import json
from pathlib import Path
import shutil
import subprocess

import ida_kernwin as kw
import ida_segment

from .ida_adapter import identity, segments
from .project import Project, atomic_json, create_project
from .syntax_view import condition_text


class ProjectBrowser:
    def __init__(self, application):
        self.app = application
        self.project = None
        self.process = None

    def create(self):
        target = kw.ask_file(True, "iosd-analysis.iosd-project", "Choose project name/location; a NEW folder with that name will be created")
        if not target:
            return
        summary = kw.ask_file(False, "summary.json", "Select runtime export tree/summary.json")
        if not summary:
            return
        current = identity()
        # Loader segments only. Debugger-created memory regions are not image RVAs.
        ranges = []
        debug_flag = getattr(ida_segment, "SFL_DEBUG", None)
        if debug_flag is None:
            raise ValueError("Cannot distinguish debugger segments on this IDA build")
        for segment in segments():
            native = ida_segment.getseg(segment["address"])
            if (native is not None and not (native.flags & debug_flag)
                    and segment["address"] >= current["imagebase"] and segment["name"] != "extern"):
                ranges.append((segment["address"] - current["imagebase"], segment["end"] - current["imagebase"]))
        folder = Path(target).with_suffix("")
        self.project = create_project(folder, Path(summary).parent, current, ranges)
        kw.msg("[iosd-helper] Project created: %s\n" % self.project.folder)
        self.start()

    def open(self):
        target = kw.ask_file(False, "project.json", "Open iosd Helper analysis project")
        if not target:
            return
        project = Project(target)
        project.assert_identity(identity())
        project.validate_sources()
        self.project = project
        self.status()

    def require(self):
        if self.project is None:
            raise ValueError("Create or open an analysis project first")
        self.project.assert_identity(identity())
        return self.project

    def require_same(self, expected):
        if self.require() is not expected:
            raise ValueError("This results window belongs to a different project; reopen the browser")

    def start(self):
        project = self.require()
        worker = Path(__file__).resolve().with_name("project_worker.py")
        if not worker.is_file():
            raise ValueError("Packaged project_worker.py is missing; reinstall the complete iosd_helper package")
        if (project.folder / "worker.lock").exists() or (self.process and self.process.poll() is None):
            self.status()
            raise ValueError("An indexing worker is already active, or its crash lock remains. Inspect task status/PID.")
        config_path = project.folder / "local-settings.json"
        config = json.loads(config_path.read_text(encoding="utf-8")) if config_path.exists() else {}
        executable = config.get("python_executable") or shutil.which("python") or ""
        executable = kw.ask_str(executable, 0, "External Python 3.10+ executable (not ida.exe); local indexing only")
        if not executable:
            return
        if not Path(executable).is_file():
            raise ValueError("Python executable does not exist")
        project.validate_sources()
        atomic_json(config_path, {"python_executable": executable})
        (project.folder / "cancel.request").unlink(missing_ok=True)
        with (project.folder / "worker.log").open("ab") as log:
            self.process = subprocess.Popen([executable, str(worker), "index", str(project.folder)],
                cwd=str(worker.parent.parent), stdin=subprocess.DEVNULL, stdout=log, stderr=log,
                creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
        kw.msg("[iosd-helper] Local worker started (PID %d). IDA remains available. Use Project task status; Cancel preserves committed batches.\n" % self.process.pid)

    def status(self):
        project = self.require()
        task = project.status()
        if self.process and self.process.poll() not in (None, 0):
            task = {**task, "worker_exit_code": self.process.returncode, "log": str(project.folder / "worker.log")}
        kw.msg("[iosd-helper] Saved-evidence project: %s\n%s\n" % (project.folder, json.dumps(task, ensure_ascii=False, indent=2)))
        return task

    def cancel(self):
        project = self.require()
        (project.folder / "cancel.request").touch()
        kw.msg("[iosd-helper] Cancellation requested; worker stops at a batch boundary. Resume with Start/resume project index.\n")

    def browse(self):
        project = self.require()
        collections = list(project.manifest["files"])
        labels = {"paths": "有界语法路径示例", "variants": "关键词选项路径示例", "nodes": "全部已取得节点",
                  "unknown": "未知或不完整节点", "registrations": "静态注册与快照绑定对照",
                  "options": "关键词选项源", "branches": "间接条件分支", "pending": "快照待绑定记录", "slots": "快照动态链接槽"}
        def select(index):
            self.require_same(project)
            self.query(collections[index])
        self.app.table("项目数据类型 / saved evidence", [("Collection", 24), ("说明", 45)],
                       [[key, labels[key]] for key in collections],
                       lambda index: self.app.guard(lambda: select(index)))

    def query(self, collection):
        query = kw.ask_str("", 0, "Search all indexed records: syntax / action / RVA / condition; empty = all")
        if query is None:
            return
        mode = kw.ask_str("", 0, "Exact internal mode: configure / interface / exec; empty = all")
        if mode is None:
            return
        self.page(collection, query, mode)

    def page(self, collection, query, mode, offset=0):
        project = self.require()
        count, records = project.search(collection, query, mode, offset)
        rows = [[r["mode"], r["label"], r["state"], r["gaps"], r["addresses"]] for r in records]
        previous, next_page = offset > 0, offset + len(records) < count
        if previous:
            rows.append(["", "← Previous 200", "", "", ""])
        if next_page:
            rows.append(["", "Next 200 →", "", "", ""])
        def select(index):
            self.require_same(project)
            if index < len(records):
                self.detail(records[index])
            elif previous and index == len(records):
                self.page(collection, query, mode, max(0, offset - 200))
            else:
                self.page(collection, query, mode, offset + 200)
        kw.msg("[iosd-helper] %s: %d indexed matches; page %d. Partial indexes are allowed. Snapshot values are historical.\n" % (collection, count, offset // 200 + 1))
        self.app.table("%s %d–%d / %d" % (collection, offset + 1 if count else 0, offset + len(records), count),
                       [("Mode", 18), ("Candidate / node", 85), ("Status", 45), ("Gaps", 8), ("RVA / capture VA", 55)], rows,
                       lambda index: self.app.guard(lambda: select(index)))

    def detail(self, record):
        project = self.require()
        row = project.detail(record)
        # Each entry opens a focused evidence section instead of flooding Output with full traces.
        keys = list(row)
        def section(index):
            self.require_same(project)
            key = keys[index]
            if key in ("conditions", "gaps", "parameters", "state_effects") and isinstance(row[key], list):
                values = row[key]
                def readable(value):
                    if key == "conditions" and isinstance(value, dict):
                        try:
                            return condition_text(value)
                        except (KeyError, TypeError, ValueError):
                            pass
                    return json.dumps(value, ensure_ascii=False)
                def show_value(selected):
                    self.require_same(project)
                    self.app.evidence({"field": key, "value": values[selected], "scope": project.manifest["scope"]})
                self.app.table("%s（保存的证据）" % key, [("序号", 8), ("条件 / 未知内容", 130)],
                               [[i + 1, readable(value)] for i, value in enumerate(values)],
                               lambda selected: self.app.guard(lambda: show_value(selected)))
                return
            self.app.evidence({"collection": record["collection"], "field": key, "value": row[key],
                               "source": str(project.source(record["collection"])), "byte_offset": record["byte_offset"],
                               "scope": project.manifest["scope"]})
        self.app.table("Evidence fields: " + record["label"][:70], [("Field", 35), ("Value / entries", 110)],
                       [[key, ("%d entries" % len(row[key])) if isinstance(row[key], (dict, list)) else str(row[key])[:500]] for key in keys],
                       lambda index: self.app.guard(lambda: section(index)))
        refs = project.references(record["collection"], row)
        def jump(index):
            self.require_same(project)
            self.app.evidence(refs[index], project.jump_address(refs[index], identity()))
        self.app.table("Evidence addresses (capture VA is not relocated)", [("Meaning", 28), ("Space", 18), ("RVA / capture VA", 22)],
                       [[r["label"], r["space"], hex(r.get("rva", r.get("capture_va", 0)))] for r in refs],
                       lambda index: self.app.guard(lambda: jump(index)))

    def close(self):
        # A local index job may finish after its browser closes; it never accesses IDA.
        self.project = None
