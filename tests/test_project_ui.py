"""Project browsing and worker boundary with IDA services replaced by stubs."""
import importlib
import json
from pathlib import Path
import sys
import tempfile
from types import ModuleType, SimpleNamespace
import unittest
from unittest.mock import Mock, patch

from iosd_helper.project import atomic_json, build_index, create_project


class BrowserTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        tree = self.root / "tree"
        tree.mkdir()
        current = {"input_md5": "abc", "imagebase": 0x1000}
        atomic_json(tree / "summary.json", {"identity": current})
        row = {"mode": "configure", "syntax_candidate": "test candidate <cr>", "handler_rva": 0x100,
               "conditions": [{"kind": "predicate", "function": 0x1100, "expected": True}], "gaps": ["unknown"]}
        (tree / "paths.jsonl").write_text("".join(json.dumps(row) + "\n" for _ in range(201)), encoding="utf-8")
        self.project = create_project(self.root / "project", tree, current, [(0, 0x1000)])
        build_index(self.project)
        kernel = ModuleType("ida_kernwin")
        kernel.msg = Mock()
        adapter = ModuleType("iosd_helper.ida_adapter")
        adapter.identity = Mock(return_value=current)
        adapter.segments = Mock(return_value=[])
        segment = ModuleType("ida_segment")
        self.modules = patch.dict(sys.modules, {"ida_kernwin": kernel, "ida_segment": segment,
                                              "iosd_helper.ida_adapter": adapter})
        self.modules.start()
        self.addCleanup(self.modules.stop)
        sys.modules.pop("iosd_helper.project_ui", None)
        self.addCleanup(lambda: sys.modules.pop("iosd_helper.project_ui", None))
        self.ui = importlib.import_module("iosd_helper.project_ui")
        self.app = SimpleNamespace(tables=[], evidence=Mock(), guard=lambda action: action())
        self.app.table = lambda title, columns, rows, select=None: self.app.tables.append(SimpleNamespace(
            title=title, columns=columns, rows=rows, select=select))
        self.browser = self.ui.ProjectBrowser(self.app)
        self.browser.project = self.project

    def test_page_navigation_details_readable_conditions_and_rebased_jump(self):
        self.browser.page("paths", "test", "configure")
        self.assertEqual(len(self.app.tables[0].rows), 201)  # 200 records + next-page control
        self.app.tables[0].select(200)
        self.assertEqual(len(self.app.tables[1].rows), 2)  # last record + previous-page control
        self.app.tables[1].select(0)
        fields, addresses = self.app.tables[2:4]
        conditions_index = next(i for i, row in enumerate(fields.rows) if row[0] == "conditions")
        fields.select(conditions_index)
        self.assertIn("未执行", self.app.tables[4].rows[0][1])
        self.ui.identity.return_value = {"input_md5": "abc", "imagebase": 0x5000}
        addresses.select(0)
        self.assertEqual(self.app.evidence.call_args.args[1], 0x5100)

    def test_old_window_cannot_read_a_different_project(self):
        self.browser.page("paths", "", "")
        self.browser.project = type(self.project)(self.project.folder)
        with self.assertRaisesRegex(ValueError, "different project"):
            self.app.tables[0].select(0)

    def test_worker_is_external_packaged_and_has_no_shell_or_inferior_calls(self):
        self.ui.kw.ask_str = Mock(return_value=sys.executable)
        with patch.object(self.ui.subprocess, "Popen") as launch:
            launch.return_value.pid = 123
            self.browser.start()
            args, kwargs = launch.call_args
            self.assertEqual(args[0][0], sys.executable)
            self.assertTrue(Path(args[0][1]).is_file())
            self.assertEqual(args[0][2:], ["index", str(self.project.folder)])
            self.assertNotIn("shell", kwargs)
            self.assertEqual(kwargs["stdin"], self.ui.subprocess.DEVNULL)

    def test_create_dialog_builds_named_directory_and_excludes_debugger_segments(self):
        target = self.root / "named.iosd-project"
        summary = self.root / "tree" / "summary.json"
        self.ui.kw.ask_file = Mock(side_effect=[str(target), str(summary)])
        self.ui.segments.return_value = [{"address": 0x1000, "end": 0x2000, "name": ".text"},
                                         {"address": 0x9000, "end": 0xa000, "name": "heap"}]
        self.ui.ida_segment.SFL_DEBUG = 1
        self.ui.ida_segment.getseg = Mock(side_effect=lambda ea: SimpleNamespace(flags=0 if ea == 0x1000 else 1))
        with patch.object(self.browser, "start"):
            self.browser.create()
        self.assertTrue((self.root / "named" / "project.json").is_file())
        self.assertEqual(self.browser.project.manifest["image_rva_ranges"], [[0, 0x1000]])


if __name__ == "__main__":
    unittest.main()
