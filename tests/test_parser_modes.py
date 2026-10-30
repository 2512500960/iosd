import unittest
from iosd_helper.parser_modes import recover_mode_definitions,configuration_ancestry,recover_link_creations


class ParserModeTests(unittest.TestCase):
    def fixture(self):
        base=0x10000
        def ptr(rva):return {'kind':'binary','op':'add','left':{'kind':'ref','arg':{'kind':'global','ea':base+rva}},'right':{'kind':'number','value':1<<63}}
        args=[ptr(0x10),ptr(0x20),{'kind':'number','value':0},{'kind':'number','value':1},
              {'kind':'number','value':1},ptr(0x30),{'kind':'number','value':0},{'kind':'number','value':0},ptr(0x200)]
        event={'kind':'call','target':0x100,'site_rva':0x500,'args':args,'guards':[{'kind':'unknown_guard'}]}
        profile={'input_md5':'sample','factory_rvas':['0x100'],'arguments':{'name':0,'prompt':1,'parent':5,'root':8}}
        return base,event,profile

    def test_tagged_addresses_and_parent_names_are_candidates(self):
        base,event,profile=self.fixture()
        result=recover_mode_definitions([{'rva':0x400,'events':[event]}],{'input_md5':'sample','imagebase':base},
            profile,{0x10:'sub',0x20:'config-sub',0x30:'configure'}.__getitem__,[(0,0x1000)])
        mode=result['modes'][0]
        self.assertEqual((mode['name'],mode['prompt'],mode['parent'],mode['root_rva']),('sub','config-sub','configure',0x200))
        self.assertFalse(mode['definition_evidence'][0]['conditions_complete'])
        self.assertTrue(configuration_ancestry(result['modes'])[mode['id']]['configuration_family_candidate'])

    def test_unresolved_root_and_reused_names_are_retained(self):
        base,event,profile=self.fixture();other={**event,'site_rva':0x600,'args':event['args'][:-1]+[{'kind':'var','index':3}]}
        result=recover_mode_definitions([{'rva':0x400,'events':[event,other]}],{'input_md5':'sample','imagebase':base},
            profile,{0x10:'sub',0x20:'config-sub',0x30:'configure'}.__getitem__,[(0,0x1000)])
        self.assertEqual(len(result['modes']),2)
        self.assertIsNone(result['modes'][1]['root_rva'])
        self.assertEqual(result['modes'][1]['definition_evidence'][0]['gaps'][0]['field'],'root')

    def test_parent_cycles_terminate_and_creation_guards_survive(self):
        modes=[{'id':'a','name':'a','parent':'b'},{'id':'b','name':'b','parent':'a'}]
        self.assertFalse(configuration_ancestry(modes)['a']['configuration_family_candidate'])
        base,event,profile=self.fixture();profile['link_creation_apis']=[{'rva':'0x100','key_arg':0,'root_arg':8,'type':1}]
        result=recover_link_creations([{'rva':0x400,'events':[event]}],{'input_md5':'sample','imagebase':base},profile,[(0,0x1000)])
        self.assertEqual((result[0]['key_rva'],result[0]['anchor_rva']),(0x10,0x200))
        self.assertEqual(result[0]['guards'],[{'kind':'unknown_guard'}])
        with self.assertRaises(ValueError):
            recover_link_creations([],{'input_md5':'other','imagebase':base},profile,[(0,0x1000)])

    def test_unknown_mode_name_keeps_explicit_config_parent_evidence(self):
        modes=[{'id':'unknown','name':None,'parent':'configure'}]
        result=configuration_ancestry(modes)['unknown']
        self.assertTrue(result['configuration_family_candidate'])
