import struct
import unittest

from iosd_helper.structures import NodeLayout, inspect_node
from test_modules import SparseMemory


class ObservedIcmTests(unittest.TestCase):
    def layout(self, **kw):
        return NodeLayout(pointer_mode="swap_then_mask", text_policy="icm_print_observed", **kw)

    def node(self, flags=0x40, offset=2, end=6):
        raw = bytearray(72)
        struct.pack_into(">Q", raw, 48, 0x8000000000002000)
        struct.pack_into(">I", raw, 56, flags)
        struct.pack_into(">I", raw, 60, offset)
        struct.pack_into(">I", raw, 64, end)
        return raw

    def test_end_offset_is_not_length_and_tag_is_removed(self):
        memory = SparseMemory({0x1000: self.node(), 0x2000: b"xxabc\nNEXT\n"})
        row = inspect_node(memory, 0x1000, self.layout())
        self.assertEqual(row["text_candidate"], "abc")
        self.assertEqual(row["text_address"], 0x2002)
        self.assertIsNone(row["handler_candidate"])

    def test_root_array_requires_explicit_root(self):
        raw = self.node(flags=0xc0)
        struct.pack_into(">H", raw, 68, 1)
        memory = SparseMemory({0x1000: raw, 0x2000: b"WRONG-inline\0"})
        row = inspect_node(memory, 0x1000, self.layout())
        self.assertIn("provide tree_root", row["text_error"])
        memory.blocks[0x3000 + 48 + 8] = (0x8000000000004000).to_bytes(8, "big")
        memory.blocks[0x4000] = b"xxabc\n"
        row = inspect_node(memory, 0x1000, self.layout(tree_root=0x3000))
        self.assertEqual(row["text_candidate"], "abc")

    def test_second_array_and_direct_string(self):
        raw = self.node(flags=0x140)
        memory = SparseMemory({0x1000: raw, 0x3000 + 8240: (0x4000).to_bytes(8, "big"), 0x4000: b"xxabc\n"})
        self.assertEqual(inspect_node(memory, 0x1000, self.layout(tree_root=0x3000))["text_candidate"], "abc")
        raw = self.node(flags=0, offset=999, end=0)
        memory = SparseMemory({0x1000: raw, 0x2000: b"direct\0"})
        self.assertEqual(inspect_node(memory, 0x1000, self.layout())["text_candidate"], "direct")

    def test_invalid_bounds_and_rejected_legacy(self):
        memory = SparseMemory({0x1000: self.node(offset=10, end=2)})
        self.assertIn("Invalid ICM text bounds", inspect_node(memory, 0x1000, self.layout())["text_error"])
        with self.assertRaisesRegex(ValueError, "Rejected layout"):
            NodeLayout(rejected_reason="old handler hypothesis contradicted")


if __name__ == "__main__":
    unittest.main()
