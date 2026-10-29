import unittest

from iosd_helper.fragment_paths import enumerate_fragment
from test_syntax_paths import graph, node, terminal


class FragmentPathsTests(unittest.TestCase):
    def test_shared_terminal_preserves_optional_argument_and_alias_paths(self):
        g = graph([node(0x1000, "keyword", 0x1100, 0x1200, keyword_candidate="first"),
                   node(0x1200, "keyword", 0x2000, keyword_candidate="alias"),
                   node(0x1100, "parameter", 0x2000, 0x2000, parameter={"kind": "string"}), terminal()])
        r = enumerate_fragment(g, 0x1000, ["test"])
        self.assertEqual({p["syntax_candidate"] for p in r["paths"]},
                         {"test first <string> <cr>", "test first <cr>", "test alias <cr>"})
        self.assertEqual(r["summary"]["unique_eols"], 1)

    def test_unsolved_predicate_both_branches_are_retained(self):
        g = graph([node(0x1000, "predicate", 0x2000, condition={"predicate_candidate": 0x6000, "false_target_candidate": 0x2000}), terminal()])
        r = enumerate_fragment(g, 0x1000)
        self.assertEqual({p["conditions"][0]["expected"] for p in r["paths"]}, {True, False})
        self.assertTrue(all(not p["conditions"][0]["evaluated"] for p in r["paths"]))

    def test_unknown_action_and_unread_target_remain_visible(self):
        g = graph([node(0x1000, None, 0x2000, 0x9999, action_name="unknown"), terminal()])
        r = enumerate_fragment(g, 0x1000)
        self.assertTrue(r["paths"][0]["gaps"])
        self.assertIn("<?unknown", r["paths"][0]["syntax_candidate"])
        self.assertEqual(r["frontiers"][0]["address"], 0x9999)

    def test_cycle_is_a_frontier_not_an_infinite_loop(self):
        g = graph([node(0x1000, "epsilon_both", 0x1000, 0x2000), terminal()])
        r = enumerate_fragment(g, 0x1000)
        self.assertEqual(len(r["paths"]), 1)
        self.assertIn("cycle", r["frontiers"][0]["reason"])

    def test_expansion_bound_preserves_unexpanded_routes(self):
        g = graph([node(0x1000, "epsilon_both", 0x1100, 0x2000), node(0x1100, "epsilon_accept", 0x2000), terminal()])
        r = enumerate_fragment(g, 0x1000, max_expansions=1)
        self.assertEqual(r["summary"]["stop_reason"], "expansion_limit")
        self.assertEqual({p["address"] for p in r["deferred_routes"]}, {0x1100, 0x2000})
        self.assertEqual(r["summary"]["deferred_routes"], 2)

    def test_combined_terminal_keeps_parameter_and_negative_forms_and_alternative(self):
        g = graph([node(0x1000, "parameter_terminal", alternate=0x2000, keyword_candidate="limit",
                       handler_candidate=0x9000, selector_candidate=1, omit_parameter_when_negative=True,
                       parameter={"kind": "unsigned_number", "min": 1, "max": 20}), terminal()])
        r = enumerate_fragment(g, 0x1000)
        self.assertEqual({p["syntax_candidate"] for p in r["paths"]}, {"limit <number:1..20> <cr>", "limit <cr>", "<cr>"})
        self.assertTrue(all(not c["evaluated"] for p in r["paths"] for c in p["conditions"]))

    def test_invalid_bounds(self):
        with self.assertRaises(ValueError):
            enumerate_fragment(graph([]), 1, max_expansions=0)

    def test_terminal_variants_respect_record_limit_without_losing_deferred_form(self):
        g = graph([node(0x1000, "parameter_terminal", keyword_candidate="mtu", handler_candidate=0x9000,
                       omit_parameter_when_negative=True, parameter={"kind": "unsigned_number", "min": 1, "max": 20})])
        r = enumerate_fragment(g, 0x1000, max_records=1)
        self.assertEqual(len(r["paths"]), 1)
        self.assertEqual(r["summary"]["stop_reason"], "record_limit")
        self.assertEqual(r["deferred_routes"][0]["terminal_variant"]["syntax_candidate"], "mtu <cr>")
