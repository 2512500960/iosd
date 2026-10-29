import struct
import unittest

from iosd_helper.memory import MemoryReadError
from iosd_helper.structures import scan_module_records


class SparseMemory:
    source = "synthetic"

    def __init__(self, blocks):
        self.blocks = blocks

    def read(self, address, size):
        for start, data in self.blocks.items():
            offset = address - start
            if 0 <= offset and offset + size <= len(data):
                return data[offset:offset + size]
        raise MemoryReadError("unmapped synthetic page")


class ModuleTests(unittest.TestCase):
    def test_separate_headers_and_link_tags(self):
        headers = (struct.pack("<IIQQQ", 0x15055cc1, 0xafecafec, 0x2000, 0, 0)
                   + struct.pack("<IIQQQ", 0x15055cc1, 0xafecafec, 0x2020, 0x3000, 0x3010))
        links = (struct.pack("<IIQQ", 0x15055cc1, 0xdfeadfea, 0x1020, 0x1000)
                 + struct.pack("<IIQQ", 0x15055cc1, 0xabefabef, 0x1000, 0x1020))
        memory = SparseMemory({0x1000: headers, 0x1100: links,
                              0x2000: b"libiosd_a\0", 0x2020: b"libiosd_b\0"})
        rows, errors, cancelled = scan_module_records(memory, 0x1000, 0x1040)
        self.assertFalse(errors)
        self.assertFalse(cancelled)
        self.assertEqual([r["name"] for r in rows], ["libiosd_a", "libiosd_b"])
        self.assertEqual(rows[1]["field_10_candidate"], 0x3000)
        linked, errors, _ = scan_module_records(memory, 0x1100, 0x1130, links=True,
                                               module_addresses={r["address"] for r in rows})
        self.assertFalse(errors)
        self.assertEqual(len(linked), 2)
        self.assertTrue(all(r["endpoint_a_is_header"] and r["endpoint_b_is_header"] for r in linked))

    def test_unknown_tags_and_trailing_data_are_reported(self):
        memory = SparseMemory({0x1000: bytes(33)})
        rows, errors, _ = scan_module_records(memory, 0x1000, 0x1021)
        self.assertFalse(rows)
        self.assertEqual(len(errors), 2)
        self.assertEqual(errors[-1]["byte_count"], 1)

    def test_partial_name_and_dangling_link_preserve_evidence(self):
        header = struct.pack("<IIQQQ", 0x15055cc1, 0xafecafec, 0xdead, 0, 0)
        memory = SparseMemory({0x1000: header})
        rows, errors, _ = scan_module_records(memory, 0x1000, 0x1020)
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["raw_hex"], header.hex())
        self.assertTrue(errors)
        link = struct.pack("<IIQQ", 0x15055cc1, 0xdfeadfea, 0x1000, 0xdead)
        rows, errors, _ = scan_module_records(SparseMemory({0x2000: link}), 0x2000, 0x2018,
                                             links=True, module_addresses={0x1000})
        self.assertFalse(errors)
        self.assertTrue(rows[0]["endpoint_a_is_header"])
        self.assertFalse(rows[0]["endpoint_b_is_header"])

    def test_cancel_is_explicit(self):
        rows, errors, partial = scan_module_records(SparseMemory({}), 0x1000, 0x1020,
                                                   cancelled=lambda: True)
        self.assertFalse(rows)
        self.assertFalse(errors)
        self.assertTrue(partial)


if __name__ == "__main__":
    unittest.main()
