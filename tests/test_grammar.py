import struct
import unittest

from iosd_helper.grammar import TransitionLayout, registration_roots, build_static_graph, extract_profile, to_dot
from test_modules import SparseMemory


def transition(accept=0, alternate=0, opcode=69, payload=0):
    return struct.pack("<QQ", accept, alternate) + struct.pack(">I", opcode) + bytes(4) + struct.pack("<QQ", payload, 0)


class GrammarTests(unittest.TestCase):
    def memory(self):
        return SparseMemory({
            0x1000: struct.pack("<QQQQ", 0x5000, 0x2000, 0x6000, 0),
            0x2000: transition(accept=0x2028, alternate=0x7000, payload=0x3000),
            0x2028: transition(accept=0x2000, opcode=86),
            0x3000: struct.pack("<QQ", 0x4000, 0x4020),
            0x4000: b"record\0", 0x4020: b"Flow record help\0"})

    def test_registration_sentinel_and_conditions(self):
        rows, errors, partial = registration_roots(self.memory(), [{"address": "0x1000", "conditions": ["feature returns true"]}], 0x6000)
        self.assertFalse(errors)
        self.assertFalse(partial)
        self.assertEqual(rows[0]["root"], 0x2000)
        self.assertEqual(rows[0]["conditions"], ["feature returns true"])

    def test_keywords_cycles_and_runtime_links(self):
        graph = build_static_graph(self.memory(), [0x2000], stop_addresses=[0x7000])
        self.assertEqual(len(graph["nodes"]), 3)
        self.assertEqual(graph["nodes"][0]["keyword_candidate"], "record")
        self.assertEqual(graph["nodes"][0]["help_candidate"], "Flow record help")
        self.assertTrue(all(row["handler_candidate"] is None for row in graph["nodes"]))
        self.assertIn("runtime linkage", graph["nodes"][2]["reason"])
        self.assertEqual(graph["completeness"], "partial_static_graph")
        dot = to_dot(graph)
        self.assertIn('"2000" -> "2028"', dot)
        self.assertIn('alternate_link_candidate', dot)

    def test_limits_and_missing_bytes_are_preserved(self):
        graph = build_static_graph(self.memory(), [0x2000], max_nodes=1)
        self.assertEqual(graph["stop_reason"], "node_limit")
        self.assertIn(0x2028, graph["pending_addresses"])
        self.assertIn("unvisited", to_dot(graph))
        graph = build_static_graph(self.memory(), [0xdead])
        self.assertEqual(graph["nodes"][0]["status"], "unresolved")
        self.assertEqual(graph["nodes"][0]["reason"], "unmapped synthetic page")

    def test_profile_pinning_and_unknown_registration(self):
        profile = {"input_md5": "abc", "sentinel": "0x6000", "registration_tables": [{"address": "0x1000"}]}
        with self.assertRaisesRegex(ValueError, "MD5"):
            extract_profile(self.memory(), profile, "def")
        graph = extract_profile(self.memory(), profile, "abc")
        self.assertEqual(len(graph["registrations"]), 1)
        rows, errors, _ = registration_roots(self.memory(), [{"address": "0xdead"}], 0x6000)
        self.assertFalse(rows)
        self.assertEqual(len(errors), 2)

    def test_dynamic_link_definition_seeds_return_anchor_without_faking_heap_address(self):
        profile = {"input_md5": "abc", "sentinel": "0x6000", "registration_tables": [],
                   "dynamic_link_definitions": [{"key": "0x5000", "root": "0x2000", "type": 2,
                                                  "creator": "0x9000", "evidence": "reviewed arguments"}]}
        g = extract_profile(self.memory(), profile, "abc")
        self.assertIn(0x2000, {n["address"] for n in g["nodes"]})
        self.assertIsNone(g["dynamic_link_definitions"][0]["address"])
        self.assertFalse(g["dynamic_link_definitions"][0]["runtime_allocation_verified"])
        profile["dynamic_link_definitions"][0]["type"] = 9
        with self.assertRaisesRegex(ValueError, "type"):
            extract_profile(self.memory(), profile, "abc")

    def test_cancellation_and_layout_validation(self):
        self.assertEqual(build_static_graph(self.memory(), [0x2000], cancelled=lambda: True)["stop_reason"], "cancelled")
        with self.assertRaises(ValueError):
            TransitionLayout(opcode_offset=100)

    def test_predicate_false_branch_is_traversed(self):
        memory = SparseMemory({
            0x2000: transition(opcode=141, payload=0x3000),
            0x3000: struct.pack("<QQQ", 0, 0x4000, 0x5000),
            0x4000: transition(opcode=1)})
        registry = [{"opcode": 141, "name": "testexpr_action", "function": 0x9000, "address": 0x8000}]
        graph = build_static_graph(memory, [0x2000], action_registry=registry)
        self.assertEqual([r["address"] for r in graph["nodes"]], [0x2000, 0x4000])
        self.assertEqual(graph["edges"][0]["kind"], "predicate_false_candidate")
        self.assertEqual(graph["edges"][0]["field_address"], 0x3008)
        self.assertFalse(graph["nodes"][0]["condition"]["evaluated"])

    def test_root_selection_and_overlapping_tables_have_explicit_coverage(self):
        memory = SparseMemory({
            0x1000: struct.pack("<QQQQQQ", 0x5000, 0x2000, 0x5000, 0x2028, 0x6000, 0),
            0x2000: transition(opcode=1), 0x2028: transition(opcode=1)})
        profile = {"input_md5": "abc", "sentinel": "0x6000", "graph_root_limit": 1,
                   "registration_tables": [{"address": "0x1000"}, {"address": "0x1010"}]}
        graph = extract_profile(memory, profile, "abc")
        self.assertEqual(graph["coverage"], {
            "registration_rows": 3, "unique_registration_records": 2, "unique_roots": 2,
            "selected_roots": 1, "unvisited_roots": 1, "processed_roots": 1,
            "pending_nodes": 0, "node_limit_reached": False})
        self.assertEqual(graph["unvisited_roots"], [0x2028])

    def test_all_roots_default_and_limit_still_preserves_frontier(self):
        memory = SparseMemory({
            0x1000: struct.pack("<QQQQQQ", 0x5000, 0x2000, 0x5000, 0x2028, 0x6000, 0),
            0x2000: transition(opcode=1), 0x2028: transition(opcode=1)})
        profile = {"input_md5": "abc", "sentinel": "0x6000", "max_nodes": 200000,
                   "registration_tables": [{"address": "0x1000"}]}
        graph = extract_profile(memory, profile, "abc")
        self.assertEqual(graph["coverage"]["processed_roots"], 2)
        self.assertFalse(graph["unvisited_roots"])
        profile["max_nodes"] = 1
        graph = extract_profile(memory, profile, "abc")
        self.assertEqual(graph["coverage"]["processed_roots"], 1)
        self.assertEqual(graph["coverage"]["pending_nodes"], 1)
        self.assertTrue(graph["coverage"]["node_limit_reached"])
        with self.assertRaises(ValueError):
            build_static_graph(memory, [0x2000], max_nodes=250001)


if __name__ == "__main__":
    unittest.main()
