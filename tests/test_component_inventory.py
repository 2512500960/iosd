import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import io
from contextlib import redirect_stdout

from iosd_helper.component_inventory import build_component_inventory
from test_skill_mcp import cli


def fixture():
    return {'kind':'protocol_subsystem_index','address_space':'rva','input_md5':'abc','subsystems':[
        {'name':'bgp_ipv4','category':'Protocol','record_rva':0x100,'init_rva':0},
        {'name':'bgp_ipv4','category':'Registry','record_rva':0x200,'init_rva':0x300},
        {'name':'ipcdp','category':'Protocol','record_rva':0x400,'init_rva':0x300},
        {'name':None,'record_rva':None,'init_rva':None,'opaque_branch':{'raw_hex':'ffaa'}},
    ]}


class ComponentInventoryTests(unittest.TestCase):
    def test_every_record_and_unknown_survives_filter_without_name_based_merging(self):
        result=build_component_inventory(fixture(),'ABC',query='bgp')
        self.assertEqual(result['summary']['source_records'],4)
        self.assertEqual(result['summary']['selected_records'],2)
        self.assertEqual(len(result['entities']),4)
        self.assertEqual(len(result['duplicate_names']),1)
        self.assertEqual(len(result['duplicate_names'][0]['entity_ids']),2)
        self.assertEqual(len(result['shared_init']),1)
        self.assertEqual(result['entities'][0]['init_rva'],0)  # RVA zero is not missing
        self.assertEqual(result['entities'][3]['source_record']['opaque_branch']['raw_hex'],'ffaa')
        self.assertTrue(result['entities'][3]['gaps'])
        self.assertFalse(result['current_idb_verified'])

    def test_token_and_contains_filters_differ_without_changing_metadata(self):
        exact=build_component_inventory(fixture(),query='cdp')
        substring=build_component_inventory(fixture(),query='cdp',match='contains')
        self.assertEqual(exact['summary']['selected_records'],0)
        self.assertEqual(substring['summary']['selected_records'],1)
        self.assertEqual(exact['entities'],substring['entities'])
        selected=build_component_inventory(fixture(),query='bgp',category='registry')
        self.assertEqual(len(selected['selection']['entity_ids']),1)

    def test_duplicate_addresses_and_invalid_fields_are_not_silently_collapsed(self):
        model=fixture();model['subsystems'][1]['record_rva']=0x100
        model['subsystems'][2]['init_rva']=-1
        result=build_component_inventory(model)
        self.assertEqual(len({r['id'] for r in result['entities']}),4)
        self.assertTrue(any(g['reason']=='duplicate_record_rva' for g in result['unknown']))
        self.assertTrue(any(g['reason']=='invalid_init_rva' and g['raw_value']==-1 for g in result['unknown']))

    def test_other_image_or_address_space_is_rejected(self):
        with self.assertRaisesRegex(ValueError,'MD5'):build_component_inventory(fixture(),'other')
        model=fixture();model['address_space']='runtime_va'
        with self.assertRaisesRegex(ValueError,'RVA'):build_component_inventory(model)

    def test_missing_source_identity_stays_explicit_and_cannot_satisfy_expected_md5(self):
        model=fixture();model['input_md5']=None
        result=build_component_inventory(model)
        self.assertTrue(any(g['reason']=='source_input_identity_not_recorded' for g in result['unknown']))
        with self.assertRaisesRegex(ValueError,'MD5'):build_component_inventory(model,'abc')

    def test_offline_cli_never_invokes_mcp_even_if_an_endpoint_is_configured(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);source=root/'index.json';output=root/'catalogue.json'
            source.write_text(json.dumps(fixture()))
            with patch.object(cli,'McpClient',side_effect=AssertionError('Offline command must not connect')),redirect_stdout(io.StringIO()):
                self.assertEqual(cli.main(['--url','http://unused/mcp','components','--index',str(source),
                                           '--query','bgp','--md5','abc','--output',str(output)]),0)
            result=json.loads(output.read_text())
            self.assertEqual(result['summary']['selected_records'],2)
            self.assertEqual(len(result['source_index_sha256']),64)


if __name__=='__main__':unittest.main()
