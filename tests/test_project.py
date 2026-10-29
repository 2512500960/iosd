import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from iosd_helper.project import Project, atomic_json, build_index, create_project


class ProjectTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.tree = self.root / "tree"
        self.tree.mkdir()
        self.identity = {"input_md5": "abc", "imagebase": 0x1000}
        atomic_json(self.tree / "summary.json", {"identity": self.identity})
        self.rows = [{"mode": "configure", "syntax_candidate": "测试 100%_ <cr>", "handler_rva": 0x100,
                      "handler": 0x1100, "eol_node": 0x1200, "conditions": [{"kind": "unknown", "function": 0x9000}],
                      "gaps": ["callback"], "availability": "unknown"},
                     {"mode": "exec", "syntax_candidate": "show version <cr>", "handler_rva": 0x101}]
        self.write("paths.jsonl", self.rows)
        self.write("unknown-nodes.jsonl", [{"address": 0x9000, "display_label": "opaque", "remaining_uncertainties": ["unknown"]}])
        self.project = create_project(self.root / "project", self.tree, self.identity, [(0, 0x1000)])

    def write(self, name, rows):
        (self.tree / name).write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows), encoding="utf-8")

    def test_read_only_evidence_pagination_and_unicode_literal_search(self):
        before = (self.tree / "paths.jsonl").read_bytes()
        build_index(self.project, batch_size=1)
        count, rows = self.project.search("paths", "100%_", "configure", limit=1)
        self.assertEqual(count, 1)
        self.assertEqual(self.project.detail(rows[0]), self.rows[0])
        self.assertEqual(rows[0]["gaps"], 1)
        self.assertEqual(self.project.search("paths", mode="config")[0], 0)
        self.assertEqual(self.project.search("paths", offset=1, limit=1)[1][0]["label"], "show version <cr>")
        self.assertEqual(before, (self.tree / "paths.jsonl").read_bytes())

    def test_cancel_and_resume_checkpoints_without_dropping_unknown(self):
        calls = []
        def cancel():
            calls.append(1)
            return len(calls) == 2
        build_index(self.project, cancelled=cancel, batch_size=1)
        self.assertEqual(self.project.status()["state"], "cancelled")
        self.assertEqual(self.project.search()[0], 1)
        build_index(Project(self.project.folder), batch_size=1)
        self.assertEqual(self.project.search()[0], 2)
        self.assertEqual(self.project.search("unknown")[0], 1)
        self.assertEqual(self.project.status()["state"], "complete")

    def test_rebase_relocates_only_image_addresses_and_checks_identity(self):
        refs = self.project.references("paths", self.rows[0])
        current = {"input_md5": "abc", "imagebase": 0x4000}
        handler = next(r for r in refs if r["label"] == "handler")
        self.assertEqual(self.project.jump_address(handler, current), 0x4100)
        callback = next(r for r in refs if r["label"] == "condition function")
        self.assertEqual(callback["capture_va"], 0x9000)
        self.assertIsNone(self.project.jump_address(callback, current))
        with self.assertRaises(ValueError):
            self.project.jump_address(handler, {"input_md5": "other", "imagebase": 0x4000})

    def test_detects_changed_evidence_even_when_timestamp_and_size_restored(self):
        build_index(self.project)
        record = self.project.search()[1][0]
        path = self.tree / "paths.jsonl"
        stat = path.stat()
        path.write_bytes(path.read_bytes().replace(b"100%_", b"200%_"))
        os.utime(path, ns=(stat.st_atime_ns, stat.st_mtime_ns))
        with self.assertRaisesRegex(ValueError, "record changed"):
            self.project.detail(record)
        with self.assertRaisesRegex(ValueError, "hash changed"):
            build_index(self.project)
        self.assertEqual(self.project.status()["state"], "failed")

    def test_failure_preserves_committed_records_and_refuses_changed_source(self):
        build_index(self.project)
        self.write("paths.jsonl", self.rows + self.rows)
        with self.assertRaisesRegex(ValueError, "Evidence changed"):
            self.project.search()
        with self.assertRaises(ValueError):
            create_project(self.root / "wrong", self.tree, {"input_md5": "wrong"})
        self.assertFalse((self.root / "wrong").exists())

    def test_lock_and_non_overwrite(self):
        (self.project.folder / "worker.lock").write_text("123", encoding="ascii")
        with self.assertRaises(FileExistsError):
            build_index(self.project)
        with self.assertRaises(FileExistsError):
            create_project(self.project.folder, self.tree, self.identity)

    def test_registration_legacy_rvas_not_reinterpreted_as_capture_vas(self):
        refs = self.project.references("registrations", {"address": 0x120, "registration_rva": 0x120, "runtime_root": 0x9000})
        self.assertEqual(len(refs), 1)
        self.assertEqual(refs[0]["rva"], 0x120)

    def test_atomic_status_retries_windows_reader_sharing_violation(self):
        replace = os.replace
        calls = []
        def sharing(source, target):
            calls.append(1)
            if len(calls) == 1:
                raise PermissionError("Windows reader still holds old status file")
            replace(source, target)
        with patch("iosd_helper.project.os.replace", side_effect=sharing):
            atomic_json(self.root / "status.json", {"state": "complete"})
        self.assertEqual(json.loads((self.root / "status.json").read_text())["state"], "complete")


if __name__ == "__main__":
    unittest.main()
