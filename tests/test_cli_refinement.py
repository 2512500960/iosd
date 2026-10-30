import unittest
from iosd_helper.cli_refinement import refine_node
from test_modules import SparseMemory


class CliRefinementTests(unittest.TestCase):
    def inputs(self):
        profile={'input_md5':'abc','reviewed_actions':{'deprecated_action':{'function_rva':'0x100'}}}
        source={'action_name':'deprecated_action','action_function':0x1100,'action_registry_entry':0x1300,
                'payload':0,'address':0x1200,'raw_hex':'aabb','remaining_uncertainties':['action_semantics_unresolved','unbound_static_definition'],
                'action_dispatch_observation':{'verified':True},'connected_mode_candidates':['configure']}
        return source,profile,{'input_md5':'abc','imagebase':0x1000}

    def test_resolved_control_keeps_raw_input_and_unrelated_gaps(self):
        old,profile,identity=self.inputs();row=refine_node(SparseMemory({}),old,profile,identity)
        self.assertEqual(row['path_semantics'],'epsilon_accept')
        self.assertEqual(row['raw_hex'],old['raw_hex'])
        self.assertEqual(row['remaining_uncertainties'],['unbound_static_definition'])
        self.assertIn('action_semantics_unresolved',old['remaining_uncertainties'])

    def test_dispatch_and_sample_mismatch_do_not_apply_semantics(self):
        old,profile,identity=self.inputs();old['action_function']=0x9999
        row=refine_node(SparseMemory({}),old,profile,identity)
        self.assertIn('refinement_skipped',row);self.assertNotIn('path_semantics',row)
        with self.assertRaises(ValueError):refine_node(SparseMemory({}),old,profile,{'input_md5':'wrong','imagebase':0})
