import contextlib,gzip,hashlib,io,json,re,tempfile,unittest
from pathlib import Path
from tools.export_cli_textbook import MODELS,build_book,paginate,slug
from tools.check_cli_textbook import check_book


class CliTextbookTests(unittest.TestCase):
    def fixture(self,version):
        identity={'input_md5':'fixture','imagebase':0x10000}
        record={'mode':'CON / <a>','prompt':'config-test','syntax_candidate':'set <number:1..8> `quoted` <cr>',
            'selector_candidate':7,'handler':{'space':'image','rva':0x120},'eol_node':{'node_rva':0x220},
            'syntax_status':'partial_syntax_candidate','final_tracked_state':[1,None,0],
            'conditions':[{'kind':'predicate','function_rva':0x340,'expected':False,'evaluated':False}],
            'parameters':[{'kind':'number','help':'Range <1..8>','min':1,'max':8}],
            'gaps':[{'reason':'unknown callback'}]}
        hashes={}
        for model,(_,relative) in MODELS.items():
            path=version/relative;path.parent.mkdir(parents=True,exist_ok=True)
            with gzip.open(path,'wt',encoding='utf-8') as stream:
                for index in range(2):stream.write(json.dumps({**record,'evidence_id':model+'-'+str(index),'final_tracked_state':[1,index,0]})+'\n')
            hashes[relative]=hashlib.sha256(path.read_bytes()).hexdigest()
        terminals=version/'unbound-cli/terminals.jsonl.gz'
        with gzip.open(terminals,'wt',encoding='utf-8') as stream:
            stream.write(json.dumps({'category':'new_unknown_category','eol':{'space':'image','rva':0x230},'handler':None,
                'selector_candidate':None,'remaining_uncertainties':['missing page']})+'\n')
        hashes['unbound-cli/terminals.jsonl.gz']=hashlib.sha256(terminals.read_bytes()).hexdigest()
        (version/'cli/summary.json').write_text(json.dumps({'identity':identity,'artifact_sha256':{'catalogue.jsonl.gz':hashes['cli/catalogue.jsonl.gz']}}),encoding='utf-8')
        (version/'unbound-cli/manifest.json').write_text(json.dumps({'identity':identity,'artifact_sha256':hashes}),encoding='utf-8')
        (version/'README.md').write_text('# Fixture version\n',encoding='utf-8')
        (version/'unbound-cli/path-summary.json').write_text('{}\n',encoding='utf-8')
        return hashes

    def test_book_retains_each_context_deduplicates_evidence_and_handles_unknown_categories(self):
        with tempfile.TemporaryDirectory() as temporary:
            version=Path(temporary);self.fixture(version)
            with contextlib.redirect_stdout(io.StringIO()):result=build_book(version,version/'commands')
            self.assertEqual(result['exported_witnesses'],10)
            self.assertEqual(result['unique_eol_references'],1)
            self.assertEqual(result['atom_records'],3)
            self.assertEqual(result['unresolved_candidates'],{'new_unknown_category':1})
            folder=version/'commands/modes'/slug('CON / <a>')
            plain=(folder/'baseline-001.txt').read_text(encoding='utf-8')
            self.assertIn('(config-test)# set <number:1..8> `quoted` <cr>',plain)
            self.assertIn('baseline-0',plain);self.assertIn('baseline-1',plain)
            detail=(folder/'baseline-001.md').read_text(encoding='utf-8')
            self.assertIn('Range &lt;1..8&gt;',detail)
            self.assertIn('[1,0,0]',detail);self.assertIn('[1,1,0]',detail)
            self.assertEqual(check_book(version,version/'commands')['witness_records_verified'],10)
            first_hashes=result['artifact_sha256']
            with contextlib.redirect_stdout(io.StringIO()):second=build_book(version,version/'commands')
            self.assertEqual(first_hashes,second['artifact_sha256'])

    def test_hash_mismatch_prevents_export_and_output_must_be_a_child(self):
        with tempfile.TemporaryDirectory() as temporary:
            version=Path(temporary);self.fixture(version)
            with self.assertRaises(ValueError):build_book(version,version)
            with (version/'cli/catalogue.jsonl.gz').open('ab') as stream:stream.write(b'changed')
            with self.assertRaisesRegex(ValueError,'hash differs'):build_book(version,version/'commands')

    def test_pagination_retains_whole_entries_and_enforces_utf8_bytes(self):
        blocks=[('one','一'*4+'\n'),('two','二'*4+'\n')]
        pages=list(paginate(blocks,'#\n',20))
        self.assertEqual([p[2] for p in pages],[['one'],['two']])
        self.assertTrue(all(len(p[1].encode())<=20 for p in pages))
        with self.assertRaisesRegex(ValueError,'Single entry'):list(paginate([('big','大'*20)],'#\n',20))


if __name__=='__main__':unittest.main()
