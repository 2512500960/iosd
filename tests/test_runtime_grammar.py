import unittest
from iosd_helper.runtime_grammar import CapturedPages,reconstruct_runtime_graph,observe_slot_bindings
from iosd_helper.memory import MemoryReadError
from iosd_helper.syntax_paths import raw_links,state_after,semantic_options


def ptr(value):return (value|0x8000000000000000).to_bytes(8,'big') if value else bytes(8)


class RuntimeGrammarTests(unittest.TestCase):
    def test_reviewed_global_predicate_is_read_without_pruning_the_other_branch(self):
        base=0x104000;page=bytearray(65536)
        page[0x20:0x28]=ptr(base+0x600);page[0x28:0x30]=ptr(base+0x700);page[0x30:0x34]=(99).to_bytes(4,'big')
        page[0x700:0x711]=b'test_func_action\0'
        page[0x110:0x114]=(99).to_bytes(4,'big');page[0x118:0x120]=ptr(base+0x300)
        page[0x300:0x308]=ptr(base+0x500);page[0x308:0x310]=ptr(base+0x200);page[0x310:0x318]=ptr(base+0x240)
        page[0x800:0x804]=(1).to_bytes(4,'big')
        memory=CapturedPages([{'ranges':[{'runtime_va':base,'raw_hex':page.hex()}]}])
        g=reconstruct_runtime_graph(memory,{'nodes':[{'address':0x100}],
            'action_registry':[{'opcode':99,'name':'test_func_action','address':0x20,'function':0x600}],'mode_definitions':[]},
            base,{'lists':[]},predicate_models={'0x500':{'kind':'global_comparison','variable_rva':'0x800','encoding':'big','equals':1}})
        n=next(n for n in g['nodes'] if n['address']==base+0x100)
        self.assertEqual(n['condition']['observed_value'],1);self.assertTrue(n['condition']['snapshot_result'])
        self.assertEqual({e['target'] for e in semantic_options(n,(1,0,0),g)},{base+0x200,base+0x240})
        self.assertNotIn('branch_gap',n)

    def test_unaligned_image_page_and_cross_range_read(self):
        m=CapturedPages([{'ranges':[{'runtime_va':0x104000,'raw_hex':(b'A'*65536).hex()},
                                   {'runtime_va':0x114000,'raw_hex':(b'B'*65536).hex()}]}])
        self.assertEqual(m.read(0x113ffe,4),b'AABB')
        with self.assertRaises(MemoryReadError):m.read(0x103fff,1)
        self.assertIn(0x100000,m.missing_pages)

    def test_runtime_endian_links_handlers_and_unknown_are_preserved(self):
        base=0x104000;page=bytearray(65536)
        def header(off,accept,alternate,op,payload):
            raw=bytearray(40);raw[:8]=ptr(accept);raw[8:16]=ptr(alternate)
            raw[16:20]=op.to_bytes(4,'big');raw[24:32]=ptr(payload);page[off:off+40]=raw
        header(0x100,base+0x128,base+0x180,69,base+0x200)
        header(0x128,0,0,1,base+0x240)
        header(0x180,0,0,900,0)
        page[0x200:0x208]=ptr(base+0x300);page[0x300:0x305]=b'test\0'
        page[0x210:0x218]=ptr(base+0x360);page[0x361]=1
        page[0x240:0x248]=ptr(base+0x500)
        def dispatch(off,fn,name_off,opcode,name):
            page[off:off+8]=ptr(fn);page[off+8:off+16]=ptr(base+name_off)
            page[off+16:off+20]=opcode.to_bytes(4,'big');page[name_off:name_off+len(name)+1]=name.encode()+b'\0'
        dispatch(0x10,base+0x20,0x700,69,'keyword_action')
        dispatch(0x30,base+0x40,0x740,1,'eolns_action')
        memory=CapturedPages([{'ranges':[{'runtime_va':base,'raw_hex':page.hex()}]}])
        graph=reconstruct_runtime_graph(memory,{'nodes':[{'address':0x100}],
            'action_registry':[{'opcode':69,'name':'keyword_action','address':0x10,'function':0x20},
                               {'opcode':1,'name':'eolns_action','address':0x30,'function':0x40}],
            'mode_definitions':[],'path_analysis':{'reviewed_normal_cli_callbacks':['0x500'],'initial_normal_cli_state':[1,0,0]}},base,{'lists':[]},keyword_gates=[{'name':'fixture gate',
              'descriptor_native_u64_mask':'0x100','variable_rva':'0x600','variable_size':4,'variable_encoding':'big'}])
        nodes={n['address']:n for n in graph['nodes']}
        self.assertEqual(nodes[base+0x100]['keyword_candidate'],'test')
        self.assertEqual(raw_links(nodes[base+0x100]),[base+0x128,base+0x180])
        self.assertEqual(nodes[base+0x128]['handler_candidate'],base+0x500)
        self.assertEqual(nodes[base+0x180]['status'],'unresolved')
        self.assertEqual(graph['registrations'],[])
        self.assertEqual(nodes[base+0x100]['runtime_raw_hex'][:16],ptr(base+0x128).hex())
        self.assertFalse(nodes[base+0x100]['keyword_access_gates'][0]['direct_gate_passes'])
        self.assertEqual(nodes[base+0x100]['keyword_access_gates'][0]['value'],0)
        self.assertTrue(nodes[base+0x100]['action_dispatch_observation']['verified'])
        self.assertEqual(nodes[base+0x100]['action_function'],base+0x20)
        self.assertEqual(graph['path_analysis']['reviewed_normal_cli_callbacks'],[hex(base+0x500)])
        self.assertEqual(graph['path_analysis']['initial_normal_cli_state'],[1,0,0])
        callback={'effects':[{'kind':'context_callback','function_candidate':base+0x500}]}
        self.assertEqual(state_after(callback,(1,0,0),graph['path_analysis']),(1,0,0))

    def test_observed_binding_requires_the_matching_key_and_chain(self):
        base=0x104000;page=bytearray(65536)
        page[0x100:0x108]=ptr(base+0x200);page[0x110:0x118]=ptr(base+0x300)
        page[0x118:0x11c]=(1).to_bytes(4,'big')
        page[0x308:0x310]=ptr(base+0x400);page[0x408:0x410]=ptr(base+0x800)
        memory=CapturedPages([{'ranges':[{'runtime_va':base,'raw_hex':page.hex()}]}])
        graph={'nodes':[],'link_registry':[{'address':0x100}],
               'registrations':[{'address':0x20,'link_key':0x200,'root':0x400},
                                {'address':0x30,'link_key':0x201,'root':0x400}]}
        slots,rows=observe_slot_bindings(memory,graph,base,{'lists':[]},0x800)
        self.assertTrue(slots[0]['reached_sentinel'])
        self.assertTrue(rows[0]['observed_binding_evidence'])
        self.assertFalse(rows[1]['observed_binding_evidence'])
        self.assertFalse(rows[1]['absence_proven'])
