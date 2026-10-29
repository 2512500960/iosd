import unittest

from iosd_helper.candidate_space import build_candidate_space, activation_candidates
from test_syntax_paths import graph, node, terminal


class CandidateSpaceTests(unittest.TestCase):
    def test_unknown_context_keeps_both_sense_branches_and_structural_evidence(self):
        edges = [{"source": 0x1000, "target": 0x2000, "kind": "raw_accept"},
                 {"source": 0x1000, "target": 0x2100, "kind": "raw_alternate"}]
        g = graph([node(0x1000, "sense_choice", 0x2000, 0x2100), terminal(), terminal(0x2100)], edges=edges)
        space = build_candidate_space(g)
        self.assertEqual(space["structural_edges"], edges)
        self.assertEqual({e["target"] for e in space["transitions"]}, {0x2000, 0x2100})
        self.assertTrue(all(not e["condition"]["evaluated"] for e in space["transitions"]))

    def test_unbound_unknown_fragment_and_mode_unknown_terminal_are_never_excluded(self):
        g = graph([node(0x1000, "stop"), node(0x3000, None, 0x2000, action_name="unknown"), terminal()],
                  registrations=[{"address": 0x4000, "root": 0x3000, "link_key": 99, "conditions": ["runtime trigger unknown"]}])
        space = build_candidate_space(g)
        self.assertEqual(space["summary"]["preserved_nodes"], 3)
        self.assertEqual(space["summary"]["definition_excluded_for_incompleteness"], 0)
        self.assertEqual(space["fragments"][0]["binding_status"], "core_slot_missing")
        self.assertTrue(space["fragments"][0]["retained"])
        self.assertEqual(space["terminals"][0]["mode_candidates"], [])
        self.assertEqual(space["summary"]["handler_definitions_without_known_mode"], 1)
        self.assertIn(0x3000, [n["address"] for n in space["unknown_nodes"]])

    def test_cycles_are_preserved_as_grammar_without_path_enumeration(self):
        g = graph([node(0x1000, "epsilon_both", 0x1000, 0x2000), terminal()])
        space = build_candidate_space(g)
        self.assertIn((0x1000, 0x1000), {(e["source"], e["target"]) for e in space["transitions"]})
        self.assertEqual(space["terminals"][0]["mode_candidates"], ["configure"])

    def test_combined_terminal_preserves_numeric_and_omission_rules(self):
        n = node(0x1000, "parameter_terminal", keyword_candidate="mtu", handler_candidate=0x9000,
                 parameter={"kind": "unsigned_number", "min": 68, "max": 9216}, omit_parameter_when_negative=True)
        space = build_candidate_space(graph([n]))
        self.assertEqual(len(space["terminal_rules"]), 2)
        self.assertEqual(space["terminal_rules"][1]["tokens"], ["mtu", "<cr>"])

    def test_call_ancestry_is_a_candidate_and_retains_a_registration_relation(self):
        g = graph([], input_md5="abc", registrations=[{"address": 0x5000, "root": 0x6000, "link_key": 1,
                  "source_call_sites": [{"caller": 0x3000, "call": 0x3010}]}])
        audit = {"identity": {"input_md5": "abc"}, "known_handlers": [0x1000], "max_depth": 3,
                 "call_edges": [{"caller": 0x1000, "callee": 0x2000, "callsite": 0x1010},
                                {"caller": 0x2000, "callee": 0x3000, "callsite": 0x2010}]}
        rows = activation_candidates(g, audit)
        self.assertEqual(rows[0]["handler"], 0x1000)
        self.assertEqual(rows[0]["registration_records"], [0x5000])
        self.assertEqual([e["caller"] for e in rows[0]["call_chain"]], [0x1000, 0x2000])
        self.assertFalse(rows[0]["activation_order_proven"])
        audit["identity"]["input_md5"] = "different"
        with self.assertRaisesRegex(ValueError, "MD5"):
            activation_candidates(g, audit)


if __name__ == "__main__":
    unittest.main()
