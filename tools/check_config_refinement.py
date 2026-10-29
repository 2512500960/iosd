"""Check saved refinement evidence, page closure, source hashes and local links."""
import argparse,hashlib,json
from pathlib import Path
from urllib.parse import unquote
from bs4 import BeautifulSoup


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('directory');a=p.parse_args()
    root=Path(a.directory);out=root/'refinement';summary=json.loads((out/'tree/summary.json').read_text(encoding='utf-8'))
    requested=json.loads((out/'baseline-request-missing-pages.json').read_text(encoding='utf-8'))['ranges']
    acquired={};failures=[]
    for folder in ('pages-round-1','closure-pages','semantic-pages'):
        for f in (out/folder).glob('pages-*.json'):
            snap=json.loads(f.read_text(encoding='utf-8'))
            assert snap['input_md5']==summary['identity']['input_md5']
            assert snap['runtime_base']==summary['identity']['imagebase']
            for row in snap['ranges']:
                if 'error' in row:failures.append(row)
                else:
                    assert len(bytes.fromhex(row['raw_hex']))==row['size']
                    acquired[row['runtime_va']]=row['size']
    assert all(r['runtime_va'] in acquired for r in requested)
    assert not failures
    assert summary['missing_pages']==0
    assert not json.loads((out/'tree/request-missing-pages.json').read_text())['ranges']
    def addresses(file):
        with file.open(encoding='utf-8') as f:return {json.loads(line)['address'] for line in f}
    old=addresses(root/'tree/nodes.jsonl');current=addresses(out/'tree/nodes.jsonl')
    assert old<=current,'Previously acquired nodes lost'
    assert len(current)==summary['runtime_nodes']
    source_root=Path(__file__).resolve().parents[1]
    for name,digest in summary['interpretation_source_sha256'].items():
        assert hashlib.sha256((source_root/name).read_bytes()).hexdigest()==digest,name
    html=out/'index.html';soup=BeautifulSoup(html.read_text(encoding='utf-8'),'html.parser')
    links=[a['href'] for a in soup.select('a[href]') if not a['href'].startswith(('http:','https:','#'))]
    assert all((out/unquote(h.split('#')[0])).exists() for h in links)
    delta=json.loads((out/'config-delta-summary.json').read_text(encoding='utf-8'))
    assert sum(1 for _ in (out/'config-paths.jsonl').open(encoding='utf-8'))==delta['config_witnesses_after']
    checks={'initial_requested_pages':len(requested),'additional_captured_ranges':len(acquired),'captured_bytes':sum(acquired.values()),
        'remaining_missing_pages':0,'baseline_nodes_preserved':len(old),'current_nodes':len(current),
        'local_links_verified':len(links),'source_hashes_verified':len(summary['interpretation_source_sha256']),
        'scope':'Saved evidence verification; no IDA or target access'}
    (out/'verification.json').write_text(json.dumps(checks,indent=2),encoding='utf-8')
    print(json.dumps(checks,indent=2))


if __name__=='__main__':main()
