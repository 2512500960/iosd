import importlib.util
from pathlib import Path
import unittest

spec=importlib.util.spec_from_file_location('ehsa_report',Path(__file__).resolve().parents[1]/'tools/build_ehsa_report.py')
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)


def fixture():
    base=0x555555554000
    states=[]
    for state in range(1,15):
        rva=0x1000+384*(state-1)
        descriptor=(base+rva|0x8000000000000000).to_bytes(8,'big')+(base+0xd51aea0).to_bytes(8,'big')
        states.append({'state':state,'rva':rva,'raw_hex':bytes(384).hex(),'mask_hex':(b'\xff'*48).hex(),
                       'descriptor_raw_hex':descriptor.hex(),'descriptor_mask_hex':'ffff'})
    return {'input_md5':module.MD5,'base':base,'state_count':14,'entry_size':24,'event_count':16,'states':states}


class EhsaEvidenceTests(unittest.TestCase):
    def test_null_and_unknown_labels_are_retained(self):
        rows=module.decode(fixture())
        self.assertEqual(len(rows),224)
        self.assertEqual(sum(r['state_name'] is None for r in rows),16)
        self.assertIsNone(rows[4]['event_name'])
        self.assertIsNone(rows[4]['callback_rva'])
        self.assertEqual(rows[4]['next_state'],1)
        self.assertEqual(rows[4]['major'],1)
        self.assertEqual(rows[4]['minor'],3)

    def test_tagged_action_and_nonordinary_next_values_survive(self):
        capture=fixture();raw=bytearray.fromhex(capture['states'][0]['raw_hex'])
        raw[:8]=(capture['base']+0x2222|0x8000000000000000).to_bytes(8,'big')
        for event,nxt in enumerate((-2,-1,99)):
            raw[event*24+16:event*24+20]=nxt.to_bytes(4,'big',signed=True)
        capture['states'][0]['raw_hex']=raw.hex();rows=module.decode(capture)
        self.assertEqual(rows[0]['callback_rva'],0x2222)
        self.assertEqual(rows[0]['next_semantics'],'special_keep_state')
        self.assertEqual(rows[1]['next_semantics'],'error')
        self.assertEqual(rows[2]['next_semantics'],'unresolved')
        self.assertEqual(rows[2]['next_state_raw'],99)

    def test_incomplete_table_or_wrong_descriptor_is_rejected(self):
        capture=fixture();capture['states'][0]['mask_hex']='00'*48
        with self.assertRaises(AssertionError):module.decode(capture)
        capture=fixture();capture['states'][0]['descriptor_raw_hex']='00'*16
        with self.assertRaises(AssertionError):module.decode(capture)

    def test_other_image_cannot_reuse_this_sample_layout(self):
        capture=fixture();capture['input_md5']='0'*32
        with self.assertRaises(AssertionError):module.decode(capture)


if __name__=='__main__':unittest.main()
