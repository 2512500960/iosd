import struct
from pathlib import Path
import tempfile
import unittest

from iosd_helper.memory import AddressMap, ElfCoreMemory, MemoryReadError, decode_pointer, read_cstring
from iosd_helper.structures import NodeLayout, inspect_node, scan_subsystems, walk_nodes
from tools.make_fixtures import core_bytes, make, IDB_BASE, RUNTIME_BASE


class BufferMemory:
    source = "synthetic"

    def __init__(self, data, base=0x1000):
        self.data, self.base = data, base

    def read(self, address, size):
        offset = address - self.base
        if offset < 0 or size < 0 or offset + size > len(self.data):
            raise MemoryReadError("unmapped")
        return bytes(self.data[offset:offset + size])


class AnalysisTests(unittest.TestCase):
    def test_subsystem_budget_is_checked_between_records_in_same_block(self):
        data=bytearray(256)
        for offset in (0,56):
            data[offset:offset+8]=bytes.fromhex('c15c0515c15c0515')
            struct.pack_into('<QQ',data,offset+24,0x10c0,0x1100)
        data[192:197]=b'test\0'
        checks=[]
        def cancelled():
            checks.append(True)
            return len(checks)>=3  # block, first candidate, second candidate
        rows,errors,partial=scan_subsystems(BufferMemory(data),0x1000,0x1100,cancelled=cancelled)
        self.assertEqual(len(rows),1)
        self.assertEqual(rows[0]['name'],'test')
        self.assertTrue(partial)
        self.assertFalse(errors)

    def test_pointer_modes_order_matters(self):
        data = bytes.fromhex("0102030405060788")
        self.assertEqual(decode_pointer(data, "little"), 0x8807060504030201)
        self.assertEqual(decode_pointer(data, "big"), 0x0102030405060788)
        self.assertEqual(decode_pointer(data, "mask_then_swap"), 0x0102030405060708)
        self.assertEqual(decode_pointer(data, "swap_then_mask"), 0x0102030405060788)
        with self.assertRaises(ValueError):
            decode_pointer(data, "automatic")

    def test_address_mapping(self):
        mapping = AddressMap(IDB_BASE, RUNTIME_BASE)
        self.assertEqual(mapping.to_runtime(IDB_BASE + 0x123), RUNTIME_BASE + 0x123)
        self.assertEqual(mapping.to_idb(RUNTIME_BASE + 0x123), IDB_BASE + 0x123)

    def test_cstring_at_boundary(self):
        memory = BufferMemory(b"hello\0")
        self.assertEqual(read_cstring(memory, 0x1000), "hello")
        with self.assertRaises(MemoryReadError):
            read_cstring(BufferMemory(b"hello"), 0x1000)

    def test_core_adjacent_mappings_and_missing_pages(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "a.core"
            path.write_bytes(core_bytes([(0x1000, b"abcd", 4), (0x1004, b"ef", 8)]))
            with ElfCoreMemory(path) as memory:
                self.assertEqual(memory.read(0x1002, 4), b"cdef")
                with self.assertRaisesRegex(MemoryReadError, "not captured"):
                    memory.read(0x1006, 1)
                with self.assertRaises(MemoryReadError):
                    memory.read(0x900, 1)
                with self.assertRaises(MemoryReadError):
                    memory.read(0x1004, 3)
            with self.assertRaises(MemoryReadError):
                memory.read(0x1000, 1)

    def test_core_rejects_truncation_and_ambiguous_mapping(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "a.core"
            for data in [b"gzip", core_bytes([(0x1000, b"abc", 3)])[:-1],
                         core_bytes([(0x1000, b"abcd", 4), (0x1002, b"ef", 2)])]:
                path.write_bytes(data)
                with self.assertRaises(ValueError):
                    ElfCoreMemory(path)

    def test_generated_static_and_core(self):
        with tempfile.TemporaryDirectory() as directory:
            image, path = make(directory)
            memory = BufferMemory(image.read_bytes(), IDB_BASE)
            rows, errors, partial = scan_subsystems(memory, IDB_BASE + 0x2200, IDB_BASE + 0x2238)
            self.assertEqual(len(rows), 1)
            self.assertFalse(errors)
            self.assertFalse(partial)
            self.assertEqual(rows[0]["name"], "fixture_subsystem")
            self.assertEqual(rows[0]["init_candidate"], IDB_BASE + 0x1000)
            with ElfCoreMemory(path) as core:
                result = walk_nodes(core, RUNTIME_BASE + 0x10000)
                node = result["nodes"][0]
                self.assertEqual(node["text_candidate"], "show fixture")
                self.assertIsNone(node["handler_candidate"])
                self.assertEqual(len(node["raw_hex"]), 144)

    def test_cycle_limit_partial_errors_and_cancel(self):
        data = bytearray(512)
        struct.pack_into(">Q", data, 24, 0x1080)
        struct.pack_into(">Q", data, 0x80 + 24, 0x1000)
        memory = BufferMemory(data)
        layout = NodeLayout(links=(24,))
        result = walk_nodes(memory, 0x1000, layout)
        self.assertEqual(len(result["nodes"]), 2)
        self.assertEqual(result["stop_reason"], "complete_for_configured_links")
        self.assertEqual(walk_nodes(memory, 0x1000, layout, 1)["stop_reason"], "node_limit")
        self.assertEqual(walk_nodes(memory, 0x1000, layout, cancelled=lambda: True)["stop_reason"], "cancelled")
        struct.pack_into(">Q", data, 24, 0xdead)
        result = walk_nodes(memory, 0x1000, layout)
        self.assertEqual(result["stop_reason"], "partial_read_errors")
        self.assertEqual(result["errors"][0]["address"], 0xdead)
        self.assertEqual(len(result["nodes"]), 1)

    def test_bounded_text_and_layout_validation(self):
        data = bytearray(72)
        struct.pack_into(">Q", data, 48, 0x1000)
        struct.pack_into(">I", data, 64, 1000000)
        row = inspect_node(BufferMemory(data), 0x1000, NodeLayout())
        self.assertIn("exceeds", row["text_error"])
        for config in [{"command_pointer": 68}, {"links": [-1]}, {"scalar_order": "auto"},
                       {"command_offset": -1}, {"pointer_mode": "auto"}]:
            with self.assertRaises(ValueError):
                NodeLayout(**config)


if __name__ == "__main__":
    unittest.main()
