"""Exercise the IDA boundary with stubs; not a substitute for an IDA smoke test."""
import importlib
import struct
import sys
from types import ModuleType
from types import SimpleNamespace
import unittest
from unittest.mock import Mock, patch

from iosd_helper.memory import MemoryReadError
from test_modules import SparseMemory


class AdapterTests(unittest.TestCase):
    def setUp(self):
        self.modules = {name: ModuleType(name) for name in (
            "ida_bytes", "ida_dbg", "ida_idaapi", "ida_idd", "ida_kernwin",
            "ida_nalt", "ida_segment", "idautils", "ida_funcs", "ida_loader", "ida_name", "idc")}
        self.modules["ida_idaapi"].BADADDR = 0xffffffffffffffff
        self.modules["ida_dbg"].DSTATE_SUSP = -1
        self.modules["ida_dbg"].get_process_state = Mock(return_value=-1)
        self.modules["ida_dbg"].invalidate_dbgmem_contents = Mock()
        self.modules["ida_idd"].dbg_read_memory = Mock(return_value=b"hello")
        self.modules["ida_bytes"].get_bytes_and_mask = Mock()
        self.modules["ida_funcs"].FUNC_THUNK = 0x80
        self.patcher = patch.dict(sys.modules, self.modules)
        self.patcher.start()
        sys.modules.pop("iosd_helper.ida_adapter", None)
        self.adapter = importlib.import_module("iosd_helper.ida_adapter")

    def tearDown(self):
        sys.modules.pop("iosd_helper.ida_adapter", None)
        self.patcher.stop()

    def test_idb_requires_all_bytes_and_disables_debugger_fallback(self):
        read = self.modules["ida_bytes"].get_bytes_and_mask
        memory = self.adapter.IDBMemory()
        for size in (1, 7, 8, 9, 16):
            read.return_value = (b"a" * size, b"\xff" * ((size + 7) // 8))
            self.assertEqual(memory.read(0x1000, size), b"a" * size)
            read.assert_called_with(0x1000, size, 0)
        for result in (None, (bytes(8), b"\xfe"), (bytes(9), b"\xff\x00"), (bytes(8), b"")):
            read.return_value = result
            with self.assertRaises(MemoryReadError):
                memory.read(0x1000, 8 if result is None else len(result[0]))

    def test_debugger_checks_suspended_state_on_each_read(self):
        memory = self.adapter.DebugMemory()
        self.assertEqual(memory.read(0x1000, 5), b"hello")
        self.modules["ida_dbg"].get_process_state.return_value = 1
        with self.assertRaises(MemoryReadError):
            memory.read(0x1000, 5)
        with self.assertRaises(MemoryReadError):
            self.adapter.DebugMemory()

    def test_debugger_short_reads_fail_without_idb_fallback(self):
        memory = self.adapter.DebugMemory()
        with self.assertRaises(MemoryReadError):
            memory.read(0x1000, 6)
        self.modules["ida_bytes"].get_bytes_and_mask.assert_not_called()

    def test_named_locators_do_not_use_old_addresses(self):
        self.modules["ida_name"].get_name_ea = Mock(side_effect=lambda _, name: 0x1234 if name == "icm_main" else 0xffffffffffffffff)
        rows = self.adapter.named_locators()
        self.assertEqual(rows[0]["address"], 0x1234)
        self.assertEqual(rows[1]["status"], "missing")
        self.assertIsNone(rows[1]["address"])

    def test_symbol_classification_rejects_data_and_interior_labels(self):
        self.modules["idautils"].Names = Mock(return_value=[
            (0x1000, "vty_message_handler"), (0x2000, "tbl_bgp_name"),
            (0x3008, "icm_interior"), (0x4000, "icm_main")])
        funcs = {0x1000: SimpleNamespace(start_ea=0x1000),
                 0x3008: SimpleNamespace(start_ea=0x3000),
                 0x4000: SimpleNamespace(start_ea=0x4000)}
        self.modules["ida_funcs"].get_func = Mock(side_effect=lambda ea: funcs.get(ea))
        rows, cancelled = self.adapter.symbol_candidates()
        self.assertFalse(cancelled)
        self.assertEqual([r["address"] for r in rows], [0x1000, 0x4000])

    def discovery_fixture(self, barrier=False):
        memory = SparseMemory({
            0x3000: struct.pack("<QQQQ", 0x5000, 0x4000, 0x6000, 0),
            0x4000: bytes(16) + struct.pack(">I", 69) + bytes(20)})
        self.modules["ida_segment"].SEGPERM_EXEC = 1
        self.modules["ida_segment"].getseg = Mock(return_value=SimpleNamespace(perm=4))
        self.modules["idautils"].Segments = Mock(return_value=[])
        self.modules["idautils"].XrefsTo = Mock(return_value=[SimpleNamespace(frm=0x1020), SimpleNamespace(frm=0x1030)])
        self.modules["ida_funcs"].get_func = Mock(return_value=SimpleNamespace(start_ea=0x1000))
        previous = {0x1030: 0x1028, 0x1028: 0x1020, 0x1020: 0x1010, 0x1010: 0x1000}
        self.modules["ida_bytes"].prev_head = Mock(side_effect=lambda ea, _: previous.get(ea, 0xffffffffffffffff))
        self.modules["idc"].print_insn_mnem = Mock(side_effect=lambda ea: {
            0x1020: "call", 0x1030: "call", 0x1028: "jmp" if barrier else "lea", 0x1010: "lea"}[ea])
        self.modules["idc"].get_operand_value = Mock(return_value=0x9000)
        self.modules["idc"].print_operand = Mock(side_effect=lambda ea, n: "rdi" if n == 0 else "table")
        self.modules["idautils"].DataRefsFrom = Mock(return_value=[0x3000])
        self.modules["ida_name"].get_name = Mock(return_value="init_test")
        return memory

    def test_registration_discovery_deduplicates_tables_and_preserves_calls(self):
        memory = self.discovery_fixture()
        with patch.object(self.adapter, "IDBMemory", return_value=memory):
            result = self.adapter.discover_registration_tables(0x9000, 0x6000)
        self.assertEqual(result["call_sites_seen"], 2)
        self.assertEqual(len(result["tables"]), 1)
        self.assertEqual(len(result["tables"][0]["source_call_sites"]), 2)
        self.assertFalse(result["unresolved_call_sites"])

    def test_registration_discovery_stops_at_control_flow_barrier(self):
        memory = self.discovery_fixture(barrier=True)
        with patch.object(self.adapter, "IDBMemory", return_value=memory):
            result = self.adapter.discover_registration_tables(0x9000, 0x6000)
        self.assertEqual(len(result["tables"][0]["source_call_sites"]), 1)
        self.assertEqual(result["unresolved_call_sites"][0]["call"], 0x1030)

    def test_static_profile_rejects_rebased_database(self):
        with patch.object(self.adapter, "identity", return_value={"input_md5": "abc", "imagebase": 0x400000}):
            with self.assertRaisesRegex(ValueError, "imagebase"):
                self.adapter.extract_static_cli({"input_md5": "abc", "idb_imagebase": "0x0"})

    def test_cancelled_discovery_cannot_report_complete(self):
        discovery = {"tables": [], "unresolved_call_sites": [], "limited": False, "cancelled": True}
        result = {"coverage": {}, "cancelled": False, "stop_reason": "complete_for_configured_edges"}
        with patch.object(self.adapter, "identity", return_value={"input_md5": "abc", "imagebase": 0}), \
             patch.object(self.adapter, "discover_registration_tables", return_value=discovery), \
             patch("iosd_helper.grammar.extract_profile", return_value=result):
            graph = self.adapter.extract_static_cli({"input_md5": "abc", "sentinel": "0x6000",
                                                     "discovery": {"consumer": "0x9000"}})
        self.assertTrue(graph["cancelled"])
        self.assertEqual(graph["stop_reason"], "cancelled")

    def test_manual_registration_supplements_survive_automatic_discovery(self):
        discovery = {"tables": [{"address": 0x3000}], "unresolved_call_sites": [], "limited": False, "cancelled": False}
        result = {"coverage": {}}
        with patch.object(self.adapter, "identity", return_value={"input_md5": "abc", "imagebase": 0}), \
             patch.object(self.adapter, "discover_registration_tables", return_value=discovery), \
             patch("iosd_helper.grammar.extract_profile", return_value=result) as extract:
            self.adapter.extract_static_cli({"input_md5": "abc", "sentinel": "0x6000",
                                             "registration_tables": [{"address": "0x3000"}, {"address": "0x4000"}],
                                             "discovery": {"consumer": "0x9000"}})
        self.assertEqual([int(t["address"], 0) if isinstance(t["address"], str) else t["address"]
                          for t in extract.call_args.args[1]["registration_tables"]], [0x3000, 0x4000])


if __name__ == "__main__":
    unittest.main()
