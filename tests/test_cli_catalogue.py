import gzip,json
from pathlib import Path
import tempfile,unittest
from tools.query_cli_catalogue import iter_matches
from tools.recover_saved_cli import evidence_value
from tools.export_cli_analysis import public_node


class CliCatalogueTests(unittest.TestCase):
    def test_node_export_retains_unbound_opaque_branches_without_raw_records(self):
        row={'address':0x1100,'raw_hex':(0x1200).to_bytes(8,'little').hex()+(0x9000).to_bytes(8,'little').hex(),
             'runtime_raw_hex':'deadbeef','descriptor_raw_hex':'1234','action_function':0x1300,
             'connected_mode_candidates':[],'remaining_uncertainties':['unknown callback'],'path_semantics':None}
        result=public_node(row,0x1000,[(0,0x1000)])
        self.assertEqual(result['links']['accept'],{'space':'image','rva':0x200})
        self.assertEqual(result['links']['alternate'],{'space':'captured_runtime','va':0x9000})
        self.assertEqual(result['connected_mode_candidates'],[])
        self.assertEqual(result['remaining_uncertainties'],['unknown callback'])
        self.assertFalse(any(k.endswith('raw_hex') for k in result))

    def test_address_fields_use_mapped_image_ranges_and_leave_scalar_values(self):
        row={'node':0x1100,'callback':0x9000,'field_offset':0x1100,'value_raw_hex':'00000001','raw_hex':'deadbeef'}
        result=evidence_value(row,0x1000,[(0,0x1000)])
        self.assertEqual(result['node_rva'],0x100)
        self.assertEqual(result['callback_captured_va'],0x9000)
        self.assertEqual(result['field_offset'],0x1100)
        self.assertEqual(result['value_encoded_hex'],'00000001')
        self.assertNotIn('raw_hex',result)

    def test_gzip_queries_keep_condition_and_gap_records(self):
        with tempfile.TemporaryDirectory() as directory:
            path=Path(directory)/'catalogue.jsonl.gz'
            rows=[{'mode':'configure','syntax_candidate':'service internal <cr>','conditions':[{'evaluated':False}],'gaps':['unknown']},
                  {'mode':'exec','syntax_candidate':'show version <cr>','conditions':[],'gaps':[]}]
            with gzip.open(path,'wt',encoding='utf-8') as stream:
                for row in rows:stream.write(json.dumps(row)+'\n')
            result=list(iter_matches(path,'configure','INTERNAL'))
            self.assertEqual(result,[rows[0]])
