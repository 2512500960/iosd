import contextlib,io,json,struct,tempfile,unittest
from pathlib import Path
from unittest.mock import patch
from tools.expand_option_witnesses import main
from iosd_helper.syntax_paths import recover_paths


def node(ea,kind,accept=0,alternate=0,**fields):
    return {'address':ea,'status':'transition_candidate','path_semantics':kind,
        'raw_hex':(struct.pack('<QQ',accept,alternate)+bytes(24)).hex(),**fields}


class OptionVariantTests(unittest.TestCase):
    def test_each_option_replays_its_state_effect_before_suffix_recovery(self):
        choices=[{'keyword':word,'value':value,'conditions':[],'effects':[{'kind':'keyword_state_assignment','field_offset':9328,'operation':'assign','value_raw_hex':str(value)}]} for word,value in [('off',0),('on',1)]]
        nodes=[node(0x1000,'keyword',0x1100,keyword_candidate='feature'),
            node(0x1100,'keyword_options',0x1200,keyword_options=choices,option_enumeration_complete=True),
            node(0x1200,'sense_choice',0x1300,0x1400),
            node(0x1300,'parameter',0x1400,parameter={'kind':'unsigned_number','min':1,'max':9}),
            node(0x1400,'terminal',handler_candidate=0x9000,selector_candidate=1)]
        definitions=[{'name':'configure','prompt':'config','root':'0x1000'}]
        settings={'initial_normal_cli_state':[1,0,0]}
        graph={'nodes':nodes,'path_analysis':settings,'mode_definitions':definitions,'registrations':[]}
        seeds=recover_paths(graph,['configure'])['paths']
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            for file,data in [('runtime-path-settings.json',settings),('mode-definitions.json',definitions)]:
                (root/file).write_text(json.dumps(data),encoding='utf-8')
            for file,rows in [('nodes.jsonl',nodes),('paths.jsonl',seeds)]:
                (root/file).write_text(''.join(json.dumps(r)+'\n' for r in rows),encoding='utf-8')
            with patch('sys.argv',['expand',str(root)]),contextlib.redirect_stdout(io.StringIO()):main()
            rows=[json.loads(s) for s in (root/'option-path-variants.jsonl').read_text().splitlines()]
            self.assertEqual({r['syntax_candidate'] for r in rows},{'feature off <cr>','feature on <number:1..9> <cr>'})
            self.assertTrue(all(r['variant_source']['kind']=='bounded_option_variant' for r in rows))
