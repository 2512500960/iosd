import unittest
from iosd_helper.unbound_cli import classify_cohort,registration_edges,restore_node
from iosd_helper.parser_modes import configuration_ancestry
from iosd_helper.runtime_grammar import CapturedPages,reconstruct_runtime_graph
from tools.export_cli_analysis import public_node


def node(ea,kind,accept=0,alternate=0,**fields):
    return {'address':ea,'path_semantics':kind,'status':'transition_candidate',
        'raw_hex':accept.to_bytes(8,'little').hex()+alternate.to_bytes(8,'little').hex(),**fields}


class UnboundCliTests(unittest.TestCase):
    def test_distinguishes_observed_installation_and_uncreated_slot_models(self):
        nodes=[node(0x1100,'keyword',0x1300,keyword_candidate='foo'),node(0x1200,'epsilon_both')]
        nodes += [node(ea,'terminal',handler_candidate=0x9000) for ea in (0x1300,0x1400,0x1500,0x1600)]
        modes=[{'id':'sub','name':'sub','prompt':'config-sub','parent':'configure','root_rva':0x100},
               {'id':'cfg','name':'configure','prompt':'config','parent':None,'root_rva':0x200}]
        regs=[{'registration_rva':r,'key_rva':key,'root_rva':root,'runtime_status':'not_observed_connected'}
              for r,key,root in ((1,0x20,0x400),(2,0x30,0x500))]
        result=classify_cohort({'nodes':nodes},modes,configuration_ancestry(modes),{0x1300,0x1400,0x1500,0x1600},regs,
            [{'key':0x1020,'anchor':0x1200,'type':1}],0x1000,
            static_link_creations=[{'key_rva':0x30,'anchor_rva':0x200,'type':1,'call_rva':0x800}])
        categories={r['eol_va']:r['category'] for r in result['records']}
        self.assertEqual(categories,{0x1300:'additional_config_mode_root',0x1400:'config_candidate_registration_edge',
            0x1500:'config_static_slot_creation_candidate',0x1600:'no_acquired_mode_or_registration_path'})
        self.assertEqual(len(result['records']),4)

    def test_type_two_requires_observed_sentinel(self):
        reg=[{'registration_rva':1,'key_rva':0x20,'root_rva':0x500,'runtime_status':'observed_pending'}]
        slots=[{'key':0x1020,'anchor':0x1200,'type':2}]
        edges,gaps=registration_edges(reg,slots,{0x1500:node(0x1500,'epsilon_both')},0x1000,0x800)
        self.assertFalse(edges);self.assertIn('precondition',gaps[0]['reason'])
        edges,_=registration_edges(reg,slots,{0x1500:node(0x1500,'epsilon_both',alternate=0x1800)},0x1000,0x800)
        self.assertEqual(edges[0x1500][0]['target'],0x1200)

    def test_compact_graph_roundtrip_restores_links_and_state_fields(self):
        original=node(0x1100,'keyword',0x1200,keyword_candidate='bar',handler_candidate=None,
            effects=[{'field_offset':9328,'value_raw_hex':'00000001'}],
            condition={'predicate_candidate':0x1800})
        compact=public_node(original,0x1000,[(0,0x1000)])
        restored=restore_node(compact,0x1000)
        self.assertEqual(restored['condition']['predicate_candidate'],0x1800)
        self.assertEqual(restored['effects'][0]['value_raw_hex'],'00000001')
        self.assertEqual(restored['raw_hex'],original['raw_hex'])

    def test_saved_root_extension_reuses_known_nodes_without_fake_missing_reads(self):
        base=0x104000;data=bytearray(65536)
        ptr=lambda value:(value|(1<<63)).to_bytes(8,'big')
        data[0x10:0x18]=ptr(base+0x600);data[0x18:0x20]=ptr(base+0x40);data[0x20:0x24]=(1).to_bytes(4,'big')
        data[0x40:0x4b]=b'NOP_action\0';data[0x100:0x108]=ptr(base+0x200);data[0x110:0x114]=(1).to_bytes(4,'big')
        memory=CapturedPages([{'ranges':[{'runtime_va':base,'raw_hex':data.hex()}]}])
        graph=reconstruct_runtime_graph(memory,{'nodes':[{'address':0x100}],
            'action_registry':[{'opcode':1,'name':'NOP_action','address':0x10,'function':0x600}],
            'mode_definitions':[]},base,{'lists':[]},stop_node_addresses={base+0x200})
        self.assertEqual([n['address'] for n in graph['nodes']],[base+0x100])
        self.assertEqual(graph['reused_existing_node_addresses'],[base+0x200])
        self.assertFalse(memory.missing_pages)
