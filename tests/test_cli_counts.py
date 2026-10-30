import unittest
from tools.count_cli_catalogue import count_catalogue,count_nodes


class CliCountTests(unittest.TestCase):
    def test_shared_eol_modes_and_duplicate_text_keep_separate_measures(self):
        shared={'eol_node':{'node_rva':123},'handler':{'space':'image','rva':456},'syntax_candidate':'foo <cr>','gaps':[]}
        rows=[{'mode':'configure',**shared},{'mode':'configure',**shared,'gaps':[{'reason':'context'}]},
              {'mode':'exec',**shared}]
        result=count_catalogue(rows)
        self.assertEqual(result['witness_records'],3)
        self.assertEqual(result['unique_eol_nodes_across_modes'],1)
        self.assertEqual(result['distinct_mode_template_text_pairs'],2)
        self.assertEqual(result['modes']['configure']['distinct_template_texts'],1)
        self.assertEqual(result['records_with_gaps'],1)

    def test_nvgen_and_bad_descriptors_do_not_become_terminal_definitions(self):
        good={'path_semantics':'terminal','id':{'space':'image','rva':10},'handler_candidate':{'rva':99},
              'dispatch_verified':True,'connected_mode_candidates':['exec','configure']}
        rows=[good,{**good,'id':{'space':'captured_runtime','va':1234},'connected_mode_candidates':[]},
              {**good,'path_semantics':'epsilon_accept','semantic_role':'nvgen_callback'},
              {**good,'semantic_error':'missing descriptor'}]
        result=count_nodes(rows)
        self.assertEqual(result['recognized_terminal_candidates'],2)
        self.assertEqual(result['terminal_candidates_without_selected_mode_membership'],1)
        self.assertEqual(result['terminal_coordinate_spaces'],{'image':1,'captured_runtime':1})
        self.assertEqual(result['terminal_mode_membership_from_source_graph'],{'exec':1,'configure':1})
        self.assertEqual(result['opaque_or_unread_nodes'],1)
