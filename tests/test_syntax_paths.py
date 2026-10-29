import struct
import unittest

from iosd_helper.syntax_paths import recover_paths, state_after, registration_overlays,semantic_options,parameter_label
from iosd_helper.grammar_registry import read_link_registry
from test_modules import SparseMemory


def node(ea, kind, accept=0, alternate=0, **values):
    return {"address": ea, "status": "transition_candidate", "path_semantics": kind,
            "raw_hex": (struct.pack("<QQ", accept, alternate) + bytes(24)).hex(), **values}


def graph(nodes, **values):
    return {"nodes": nodes, "registrations": [], "mode_definitions": [
        {"name": "configure", "prompt": "config", "root": "0x1000", "evidence_call": "0x9000"}], **values}


def terminal(ea=0x2000):
    return node(ea, "terminal", handler_candidate=0x9000, selector_candidate=7)


class SyntaxPathTests(unittest.TestCase):
    def test_ortest_rejects_known_repeated_bit_but_keeps_unresolved_branch(self):
        n=node(0x1000,'keyword',0x2000,0x3000,keyword_candidate='x',
               keyword_state_precondition={'field_offset':9328,'mask_raw_hex':'01','kind':'parser_state_mask_zero'})
        self.assertEqual([e['target'] for e in semantic_options(n,(1,0,0),{})],[0x3000])
        options=semantic_options(n,(None,0,0),{})
        self.assertEqual({e['target'] for e in options},{0x2000,0x3000})
        self.assertFalse(options[0]['condition']['evaluated'])

    def test_normal_cli_iterator_adds_no_token_and_does_not_invoke_callback(self):
        g=graph([node(0x1000,'iterator',0x1100,iterator={'callback':0xDEAD}),
            node(0x1100,'keyword',0x2000,keyword_candidate='hostname'),terminal()])
        r=recover_paths(g,['configure'])
        self.assertEqual(r['paths'][0]['syntax_candidate'],'hostname <cr>')
        self.assertFalse(r['paths'][0]['gaps'])
        self.assertEqual(parameter_label({'kind':'interface'}),'<interface>')
        self.assertEqual(parameter_label({'kind':'unsigned_number_dynamic'}),'<number:dynamic>')

    def test_dynamic_entry_and_return_bindings_keep_creation_evidence(self):
        definitions = [
            {"address": None, "key": 3, "root": 0x1100, "type": 1, "creator": 0x8000, "evidence": "entry"},
            {"address": None, "key": 4, "root": 0x2000, "type": 2, "creator": 0x8000, "evidence": "return"}]
        g = graph([node(0x1000, "keyword", 0x1100, keyword_candidate="monitor"),
                   node(0x1100, "epsilon_links"), node(0x1200, "keyword", 0x1300, keyword_candidate="subscriber"),
                   node(0x1300, "epsilon_links", alternate=0x3CB665C8), terminal()],
                  dynamic_link_definitions=definitions,
                  registrations=[{"address": 0x3000, "link_key": 3, "root": 0x1200},
                                 {"address": 0x3010, "link_key": 4, "root": 0x1300}])
        path = recover_paths(g, ["configure"])["paths"][0]
        self.assertEqual(path["syntax_candidate"], "monitor subscriber <cr>")
        self.assertIsNone(path["registration_candidates"][0]["slot"])
        self.assertEqual(path["registration_candidates"][0]["slot_definition"]["creator"], 0x8000)

    def test_same_key_multiple_creation_candidates_do_not_overwrite_each_other(self):
        g = graph([], dynamic_link_definitions=[{"address": None, "key": 3, "root": root, "type": 1}
                                               for root in (0x1000, 0x1100)],
                  registrations=[{"link_key": 3, "root": 0x1200}])
        overlays, unmatched, rejected = registration_overlays(g, {})
        self.assertEqual(set(overlays), {0x1000, 0x1100})
        self.assertEqual((unmatched, rejected), ([], []))
    def test_keyword_alternative_does_not_consume_failed_keyword(self):
        g = graph([node(0x1000, "keyword", 0x2000, 0x1100, keyword_candidate="alpha"),
                   node(0x1100, "keyword", 0x2100, keyword_candidate="beta"), terminal(), terminal(0x2100)])
        result = recover_paths(g, ["configure"])
        self.assertEqual({p["syntax_candidate"] for p in result["paths"]}, {"alpha <cr>", "beta <cr>"})

    def test_no_default_and_positive_parameter_paths_are_not_confused(self):
        g = graph([
            node(0x1000, "epsilon_both", 0x1200, 0x1100),
            node(0x1100, "keyword", 0x1120, 0x1140, keyword_candidate="no"),
            node(0x1120, "epsilon_accept", 0x1200, effects=[{"kind": "parser_state_assignment", "field_offset": 9328, "value_raw_hex": "0000000000000000"}]),
            node(0x1140, "keyword", 0x1200, keyword_candidate="default", effects=[{"kind": "keyword_state_assignment", "field_offset": 9332, "value_raw_hex": "0000000000000001"}]),
            node(0x1200, "keyword", 0x1300, keyword_candidate="hostname"),
            node(0x1300, "sense_choice", 0x1400, 0x2000),
            node(0x1400, "parameter", 0x2000, parameter={"kind": "string"}), terminal()])
        result = recover_paths(g, ["configure"])
        self.assertEqual({p["syntax_candidate"] for p in result["paths"]}, {
            "hostname <string> <cr>", "no hostname <cr>", "default hostname <cr>"})
        self.assertTrue(all(p["handler"] == 0x9000 for p in result["paths"]))

    def test_predicate_targets_are_distinct_and_never_evaluated(self):
        g = graph([node(0x1000, "predicate", 0x1100, condition={"predicate_candidate": 0x7000, "false_target_candidate": 0x1200}),
                   node(0x1100, "keyword", 0x2000, keyword_candidate="true-path"),
                   node(0x1200, "keyword", 0x2100, keyword_candidate="false-path"), terminal(), terminal(0x2100)])
        result = recover_paths(g, ["configure"])
        self.assertEqual({p["conditions"][0]["expected"] for p in result["paths"]}, {True, False})
        self.assertTrue(all(not p["conditions"][0]["evaluated"] for p in result["paths"]))

    def test_registered_fragment_inherits_mode_and_prefix_with_provenance(self):
        g = graph([node(0x1000, "keyword", 0x1100, keyword_candidate="logging"),
                   node(0x1100, "epsilon_links"), node(0x1200, "keyword", 0x2000, keyword_candidate="buffered"), terminal()],
                  link_registry=[{"address": 0x8000, "key": 3, "root": 0x1100, "type": 1}],
                  registrations=[{"address": 0x3000, "link_key": 3, "root": 0x1200, "conditions": ["feature unresolved"]}])
        result = recover_paths(g, ["configure"])
        path = result["paths"][0]
        self.assertEqual(path["syntax_candidate"], "logging buffered <cr>")
        self.assertEqual(path["registration_candidates"][0]["address"], 0x3000)
        self.assertEqual(path["mode_evidence_call"], "0x9000")

    def test_unknown_action_stays_visible_and_limits_are_reported(self):
        g = graph([node(0x1000, None, 0x2000, action_name="unreviewed"), terminal()])
        result = recover_paths(g, ["configure"])
        self.assertIn("<?unreviewed", result["paths"][0]["syntax_candidate"])
        self.assertEqual(result["paths"][0]["syntax_status"], "partial_syntax_candidate")
        limited = recover_paths(g, ["configure"], max_states_per_mode=1)
        self.assertEqual(limited["summary"]["modes"][0]["stop_reason"], "state_limit")
        self.assertFalse(limited["paths"])
        with self.assertRaisesRegex(ValueError, "missing"):
            recover_paths(g, ["interface"])

    def test_link_registry_layout_and_sentinel(self):
        record = struct.pack("<QQQ", 3, 0, 0x2000) + struct.pack(">II", 1, 0) + bytes(16)
        sentinel = struct.pack("<Q", 9) + bytes(40)
        rows, errors = read_link_registry(SparseMemory({0x1000: record + sentinel}), 0x1000, 9)
        self.assertFalse(errors)
        self.assertEqual(rows[0]["root"], 0x2000)
        self.assertEqual(rows[0]["type"], 1)

    def test_combined_terminal_owns_its_keyword_and_preserves_alternatives(self):
        g = graph([
            node(0x1000, "epsilon_both", 0x1200, 0x1100),
            node(0x1100, "keyword", 0x1120, keyword_candidate="no"),
            node(0x1120, "epsilon_accept", 0x1200, effects=[{"kind": "parser_state_assignment", "field_offset": 9328, "value_raw_hex": "0"}]),
            node(0x1200, "parameter_terminal", alternate=0x1400, keyword_candidate="mtu", handler_candidate=0x9000,
                 selector_candidate=1, parameter={"kind": "unsigned_number", "min": 68, "max": 9216},
                 omit_parameter_when_negative=True),
            node(0x1400, "keyword", 0x2000, keyword_candidate="other"), terminal()])
        result = recover_paths(g, ["configure"])
        syntaxes = {p["syntax_candidate"] for p in result["paths"]}
        self.assertIn("mtu <number:68..9216> <cr>", syntaxes)
        self.assertIn("no mtu <cr>", syntaxes)
        self.assertIn("other <cr>", syntaxes)
        self.assertNotIn("mtu other <cr>", syntaxes)

    def test_symbolic_or_assignment_does_not_clear_existing_sense(self):
        n = {"effects": [{"kind": "parser_state_assignment", "field_offset": 9328,
                           "operation": "or", "value_raw_hex": "0"}]}
        self.assertEqual(state_after(n, (1, 0, 0), {}), (1, 0, 0))
        self.assertEqual(state_after(n, (None, 0, 0), {}), (None, 0, 0))

    def test_shorter_input_is_preferred_over_fewer_graph_hops(self):
        g = graph([node(0x1000, "keyword", 0x1100, keyword_candidate="shutdown"),
                   node(0x1100, "epsilon_both", 0x1200, 0x1500),
                   node(0x1200, "epsilon_accept", 0x1300), node(0x1300, "epsilon_accept", 0x2000),
                   node(0x1500, "keyword", 0x2000, keyword_candidate="forced"), terminal()])
        result = recover_paths(g, ["configure"])
        self.assertEqual(result["paths"][0]["syntax_candidate"], "shutdown <cr>")


if __name__ == "__main__":
    unittest.main()
