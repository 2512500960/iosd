import struct
import unittest

from iosd_helper.grammar_semantics import read_action_registry, decode_action_payload, node_title
from test_modules import SparseMemory


class SemanticsTests(unittest.TestCase):
    def test_deprecated_marks_accept_even_without_descriptor(self):
        row = {"payload": 0}
        decode_action_payload(SparseMemory({}), row,
                              {"name": "deprecated_action", "function": 0x9000, "address": 0x8000})
        self.assertEqual(row['path_semantics'], 'epsilon_accept')
        self.assertEqual(row['effects'][0]['field_offset'], 0x301c)
        self.assertEqual(row['effects'][0]['value_raw_hex'], '00000001')
        self.assertFalse(row['effects'][0]['consumes_input'])

    def test_prefix_preserves_signed_offsets_unknown_family_and_missing_help(self):
        raw = struct.pack('>hhI', -32, 120, 0) + struct.pack('<Q', 0xdead) + struct.pack('>II', 7, 0x1234)
        row = self.decode('generic_prefix_action', raw)
        self.assertEqual(row['parameter']['storage_offset'], -32)
        self.assertEqual(row['parameter']['prefix_length_storage_offset'], 120)
        self.assertEqual(row['parameter']['address_type_candidate'], 7)
        self.assertEqual(row['parameter']['flags_raw_hex'], '00001234')
        self.assertFalse(row['parameter_condition']['evaluated'])
        self.assertIn('parameter_gap', row)
        self.assertIn('help_error', row)

    def test_whitespace_is_input_dependent_and_has_no_payload(self):
        row = {"payload": 0}
        decode_action_payload(SparseMemory({}), row,
                              {"name": "whitespace_action", "function": 0x9000, "address": 0x8000})
        self.assertEqual(row['path_semantics'], 'whitespace')
        self.assertEqual(row['whitespace']['boundary_codes'], [0, 33, 59])
        self.assertNotIn('keyword_candidate', row)

    def decode(self, name, raw, blocks=None):
        memory = SparseMemory({0x1000: raw, **(blocks or {})})
        row = {"payload": 0x1000, "handler_candidate": None}
        decode_action_payload(memory, row, {"name": name, "function": 0x9000, "address": 0x8000},
                              function_resolver=lambda ea: {"address": ea, "name": "test_handler"})
        return row

    def test_registry_function_name_opcode_offsets(self):
        raw = struct.pack("<QQ", 0x7000, 0x2000) + struct.pack(">I", 0) + bytes(4)
        raw += struct.pack("<QQ", 0, 0x2020) + struct.pack(">I", 1) + bytes(4)
        memory = SparseMemory({0x1000: raw, 0x2000: b"NONE_action\0", 0x2020: b"dynamic_action\0"})
        rows, errors = read_action_registry(memory, 0x1000, 2)
        self.assertFalse(errors)
        self.assertEqual(rows[0]["function"], 0x7000)
        self.assertTrue(rows[1]["runtime_function_required"])
        wrong = bytearray(raw)
        wrong[16:20] = (3).to_bytes(4, "big")
        rows, errors = read_action_registry(SparseMemory({0x1000: wrong, 0x2020: b"dynamic_action\0"}), 0x1000, 2)
        self.assertEqual(len(errors), 1)

    def test_keyword_id_and_help(self):
        raw = struct.pack("<QQ", 0x2000, 0x2020) + bytes(24)
        row = self.decode("keyword_id_action", raw, {0x2000: b"statistics\0", 0x2020: b"Show stats\0"})
        self.assertEqual(row["semantic_role"], "keyword")
        self.assertEqual(row["keyword_candidate"], "statistics")
        self.assertEqual(row["help_candidate"], "Show stats")

    def test_eol_handler_and_nvgen_are_separate(self):
        raw = struct.pack("<Q", 0x123400) + struct.pack(">II", 7, 0)
        terminal = self.decode("eols_command_action", raw)
        self.assertEqual(terminal["handler_candidate"], 0x123400)
        self.assertEqual(terminal["selector_candidate"], 7)
        self.assertEqual(node_title(terminal), "<cr> -> 0x123400")
        nvgen = self.decode("nvgens_action", raw)
        self.assertEqual(nvgen["semantic_role"], "configuration_generation")
        self.assertIsNone(nvgen["handler_candidate"])

    def test_eolns_command_flags_use_offset_eight(self):
        raw = struct.pack("<Q", 0x123400) + struct.pack(">II", 0x11223344, 0x55667788)
        command = self.decode("eolns_command_action", raw)
        ordinary = self.decode("eolns_action", raw)
        self.assertEqual(command["command_flags_raw_hex"], "11223344")
        self.assertEqual(command["command_flags_field"], 0x1008)
        self.assertEqual(ordinary["command_flags_raw_hex"], "55667788")

    def test_parameter_bounds_and_string_flags_remain_raw(self):
        raw = struct.pack(">III", 88, 1, 4096) + bytes(4) + struct.pack("<Q", 0) + struct.pack(">I", 0x123)
        row = self.decode("general_number_action", raw)
        self.assertEqual(row["parameter"]["min"], 1)
        self.assertEqual(row["parameter"]["max"], 4096)
        self.assertEqual(node_title(row), "<number 1..4096>")
        row = self.decode("general_string_action", struct.pack(">HHI", 32, 64, 0) + bytes(8) + struct.pack(">I", 0x100))
        self.assertEqual(row["parameter"]["size_candidate"], 64)
        self.assertEqual(row["parameter"]["flags_raw_hex"], "00000100")

    def test_predicate_is_recorded_without_execution_and_errors_preserved(self):
        row = self.decode("testexpr_action", struct.pack("<QQQ", 0, 0x4000, 0x5000))
        self.assertFalse(row["condition"]["evaluated"])
        self.assertEqual(row["condition"]["false_target_candidate"], 0x4000)
        row = self.decode("eols_action", bytes(8))
        self.assertIn("semantic_error", row)

    def test_comparison_and_boolean_keep_all_descriptor_branches(self):
        raw = struct.pack(">HHI", 9328, 4, 0) + struct.pack(">Q", 0) + struct.pack("<QQQQ", 0x4000, 0x5000, 0x6000, 0x7000)
        row = self.decode("test_action", raw)
        self.assertEqual([e["target"] for e in row["semantic_edges"]], [0x4000, 0x5000, 0x6000, 0x7000])
        self.assertEqual(row["condition"]["field_offset"], 9328)
        row = self.decode("test_boolean_action", struct.pack("<QQQ", 0xdead, 0x4000, 0x5000))
        self.assertEqual(row["condition"]["variable_address"], 0xdead)
        self.assertFalse(row["condition"]["evaluated"])
        self.assertEqual([e["expected"] for e in row["semantic_edges"]], [False, True])

    def test_params_macro_contains_keyword_numeric_parameter_and_own_handler(self):
        raw = bytearray(76)
        struct.pack_into("<Q", raw, 0, 0x2000)
        struct.pack_into(">III", raw, 8, 100, 68, 9216)
        struct.pack_into("<Q", raw, 24, 0x123400)
        struct.pack_into(">I", raw, 32, 7)
        struct.pack_into(">I", raw, 64, 8)
        row = self.decode("params_command_action", bytes(raw), {0x2000: b"mtu\0"})
        self.assertEqual(row["keyword_candidate"], "mtu")
        self.assertEqual(row["parameter"]["min"], 68)
        self.assertEqual(row["handler_candidate"], 0x123400)
        self.assertEqual(row["handler_field"], 0x1018)
        self.assertTrue(row["omit_parameter_when_negative"])
        self.assertEqual(row["path_semantics"], "parameter_terminal")

    def test_constant_string_and_decoder_do_not_consume_cli_words(self):
        row=self.decode('set_string_action',struct.pack('>I',100)+bytes(4)+struct.pack('<Q',0x2000),{0x2000:b'constant\0'})
        self.assertEqual(row['path_semantics'],'epsilon_accept')
        self.assertEqual(row['effects'][0]['value'],'constant')
        self.assertFalse(row['effects'][0]['consumes_input'])
        row=self.decode('set_decoder_action',struct.pack('<Q',0x9000))
        self.assertEqual(row['effects'][0]['decoder_address'],0x9000)
        self.assertTrue(row['effects'][0]['decoder_semantics_unresolved'])

    def test_keyword_ortest_has_mask_guard_and_or_assignment(self):
        raw=bytearray(40);struct.pack_into('<Q',raw,0,0x2000)
        struct.pack_into('>HH',raw,24,9328,4);struct.pack_into('>Q',raw,32,1)
        row=self.decode('keyword_ortest_action',raw,{0x2000:b'choice\0'})
        self.assertEqual(row['keyword_state_precondition']['field_offset'],9328)
        self.assertEqual(row['effects'][0]['operation'],'or')
        self.assertEqual(row['keyword_candidate'],'choice')

    def test_dynamic_bounds_are_not_reported_as_evaluated_and_character_is_literal(self):
        row=self.decode('number_func_action',struct.pack('>I',12)+bytes(4)+struct.pack('<QQ',0x9000,0))
        self.assertEqual(node_title(row),'<number:dynamic>')
        self.assertFalse(row['parameter']['bounds_evaluated'])
        self.assertTrue(row['parameter_gap'])
        row=self.decode('char_action',struct.pack('>I',ord(':')))
        self.assertEqual(row['literal_character'],':')
        self.assertEqual(row['path_semantics'],'literal_character')

    def test_interface_type_flag_keeps_validation_unresolved(self):
        raw=bytearray(60);struct.pack_into('>I',raw,0,100);struct.pack_into('>I',raw,16,0x80)
        row=self.decode('interface_action',raw)
        self.assertEqual(row['parameter']['kind'],'interface_type')
        self.assertEqual(row['parameter']['storage_offset'],100)
        self.assertTrue(row['parameter_gap'])


if __name__ == "__main__":
    unittest.main()
