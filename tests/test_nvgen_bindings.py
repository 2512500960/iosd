import importlib.util
from pathlib import Path
import unittest

spec=importlib.util.spec_from_file_location('nvgen_bindings',Path(__file__).resolve().parents[1]/'tools/analyze_nvgen_bindings.py')
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)


class NvgenTests(unittest.TestCase):
    def test_same_function_is_not_same_selector_or_reachability(self):
        raw=bytes(8)+(3).to_bytes(4,'big')+bytes(4)
        rows=[{'address':0x1100,'semantic_role':'configuration_generation','nvgen_callback_candidate':0x1200,'descriptor_raw_hex':raw.hex()},
              {'address':0x1140,'semantic_role':'command_terminal','handler_candidate':0x1200,'selector_candidate':3},
              {'address':0x1180,'semantic_role':'command_terminal','handler_candidate':0x1200,'selector_candidate':4}]
        result=module.analyze(rows,0x1000)
        link=result['associations'][0]
        self.assertEqual(link['callback_rva'],0x200)
        self.assertEqual(len(link['cli_terminal_matches']),2)
        self.assertEqual(len(link['same_function_and_selector_matches']),1)

    def test_unknown_and_unverified_descriptors_survive(self):
        rows=[{'address':0x1100,'semantic_role':'configuration_generation','nvgen_callback_candidate':0},
              {'address':0x1200,'semantic_role':'configuration_generation','nvgen_callback_candidate':0x1300,
               'descriptor_raw_hex':bytes(16).hex(),'dispatch_semantics_unverified':True},
              {'address':0x1400,'semantic_role':'command_terminal','handler_candidate':0x1300,'selector_candidate':0}]
        result=module.analyze(rows,0x1000)
        self.assertEqual(len(result['gaps']),2)
        self.assertEqual(len(result['associations']),2)
        self.assertFalse(result['associations'][1]['same_function_and_selector_matches'])

    def test_named_action_with_unread_or_malformed_payload_is_retained(self):
        rows=[{'address':0x1100,'action_name':'nvgens_action','semantic_error':'missing page'},
              {'address':0x1200,'semantic_role':'configuration_generation','descriptor_raw_hex':'not hex'}]
        result=module.analyze(rows,0x1000)
        self.assertEqual(len(result['nvgen']),2)
        self.assertEqual(len(result['gaps']),2)
        self.assertEqual(result['nvgen'][1]['descriptor_raw_hex'],'not hex')
        self.assertTrue(result['nvgen'][1]['descriptor_decode_error'])


if __name__=='__main__':unittest.main()
