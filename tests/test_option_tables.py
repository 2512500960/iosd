import struct,unittest
from iosd_helper.grammar_semantics import decode_action_payload
from iosd_helper.syntax_paths import semantic_options,flatten_conditions
from test_modules import SparseMemory


def header(accept=0x5000,alternate=0x6000):return (struct.pack('<QQ',accept,alternate)+bytes(24)).hex()


class OptionTableTests(unittest.TestCase):
    def decode(self,name,raw,blocks,models=None):
        row={'address':0x900,'payload':0x1000,'status':'transition_candidate','raw_hex':header()}
        decode_action_payload(SparseMemory({0x1000:raw,**blocks}),row,{'name':name,'function':0x8000,'address':0x8100},option_models=models)
        return row

    def descriptor(self,first=0x2000,offset=9328,flags=0):
        raw=bytearray(28);struct.pack_into('<Q',raw,0,first);struct.pack_into('>I',raw,8,offset);struct.pack_into('>I',raw,24,flags)
        return raw

    def test_array_zero_value_is_option_and_missing_help_does_not_drop_words(self):
        table=struct.pack('<QQ',0x3000,0xdead)+struct.pack('>II',0,1)+struct.pack('<QQ',0x3020,0)+struct.pack('>II',1,1)+bytes(8)
        row=self.decode('keyword_option_action',self.descriptor(),{0x2000:table,0x3000:b'alpha\0',0x3020:b'beta\0'})
        self.assertTrue(row['option_enumeration_complete'])
        self.assertEqual([(i['keyword'],i['value']) for i in row['keyword_options']],[('alpha',0),('beta',1)])
        self.assertIn('help_error',row['keyword_options'][0])
        options=semantic_options(row,(0,0,0),{})
        self.assertEqual({e.get('token') for e in options},{None,'alpha','beta'})

    def test_unresolved_generator_keeps_opaque_branch_instead_of_executing(self):
        row=self.decode('keyword_option_func_action',self.descriptor(first=0x8000),{})
        self.assertFalse(row['option_source']['producer_executed'])
        opts=semantic_options(row,(1,0,0),{})
        self.assertTrue(any(e.get('gap') for e in opts))
        self.assertTrue(any(e['target']==0x6000 for e in opts))

    def test_ortest_masks_are_option_specific_and_zero_value_remains_possible(self):
        table=struct.pack('<QQ',0x3000,0)+struct.pack('>II',0,0)+struct.pack('<QQ',0x3020,0)+struct.pack('>II',1,0)+bytes(8)
        row=self.decode('keyword_option_action',self.descriptor(flags=0xC000000),{0x2000:table,0x3000:b'zero\0',0x3020:b'one\0'})
        opts=semantic_options(row,(1,0,0),{})
        self.assertIn('zero',[e.get('token') for e in opts]);self.assertNotIn('one',[e.get('token') for e in opts])
        row['raw_hex']=header(0,0x6000)
        opts=semantic_options(row,(None,0,0),{})
        self.assertEqual(len(opts),1);self.assertNotIn('option_effects',opts[0])

    def test_multiple_and_test_func_branch_targets_are_payload_transitions(self):
        row=self.decode('multiple_funcs_action',bytes(16)+struct.pack('<QQ',0x7100,0x7200),{})
        self.assertEqual({e['target'] for e in semantic_options(row,(1,0,0),{})},{0x6000,0x7100,0x7200})
        row=self.decode('test_func_action',struct.pack('<QQQ',0x8000,0x7300,0x7400),{})
        self.assertEqual({e['target'] for e in semantic_options(row,(1,0,0),{})},{0x6000,0x7300,0x7400})
        self.assertTrue(all(not e.get('condition',{}).get('evaluated') for e in semantic_options(row,(1,0,0),{})))

    def test_indexed_model_does_not_read_a_reused_scratch_entry(self):
        raw=bytearray(28);struct.pack_into('<Q',raw,0,0x8000);struct.pack_into('>HH',raw,8,9328,4)
        model={'0x8000':{'kind':'indexed_strings','count':2,'names_rva':'0x4000'}}
        row=self.decode('keyword_option_list_action',raw,{0x4000:struct.pack('<QQ',0x3000,0x3020),0x3000:b'first\0',0x3020:b'second\0'},model)
        self.assertEqual([o['keyword'] for o in row['keyword_options']],['first','second'])
        self.assertEqual([o['value'] for o in row['keyword_options']],[0,1])
        self.assertTrue(row['option_enumeration_complete'])
        model['0x8000']['increment_previous_index']=True
        dynamic=self.decode('keyword_option_list_dynamic_action',raw,{0x4000:struct.pack('<QQ',0x3000,0x3020),0x3000:b'first\0',0x3020:b'second\0'},model)
        self.assertEqual([o['keyword'] for o in dynamic['keyword_options']],['second'])
