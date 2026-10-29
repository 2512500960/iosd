"""Verify retained option alternatives, unknown producers and conditional edges."""
import argparse,json,hashlib
from pathlib import Path
from urllib.parse import unquote
from bs4 import BeautifulSoup


def rows(path):
    with path.open(encoding='utf-8') as f:
        for line in f:yield json.loads(line)


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('directory');a=p.parse_args()
    root=Path(a.directory);out=root/'options';tree=out/'tree'
    summary=json.loads((tree/'summary.json').read_text(encoding='utf-8'))
    old={n['address'] for n in rows(root/'refinement/tree/nodes.jsonl')}
    current={n['address'] for n in rows(tree/'nodes.jsonl')}
    assert old<=current
    options=list(rows(tree/'keyword-option-nodes.jsonl'))
    branches=list(rows(tree/'indirect-branches.jsonl'))
    option_edges=set();unknown_edges=set();branch_edges=set()
    branch_sources={n['address'] for n in branches}
    for edge in rows(tree/'conditional-transitions.jsonl'):
        if edge['kind']=='keyword_option_match':option_edges.add((edge['source'],edge['option_index']))
        if edge['kind']=='unresolved_option_match':unknown_edges.add(edge['source'])
        if edge['source'] in branch_sources:branch_edges.add((edge['source'],edge['target'],edge['kind']))
    zero_values=0;entries=0;unknown_sources=0
    for node in options:
        assert node['option_source']['producer_executed'] is False
        accept=int.from_bytes(bytes.fromhex(node['raw_hex'])[:8],'little')
        for i,item in enumerate(node['keyword_options']):
            entries+=1;zero_values+=item['value']==0
            if accept and not item.get('keyword_unparsed'):assert (node['address'],i) in option_edges
        if accept and (not node['option_enumeration_complete'] or node['option_frontiers']):
            unknown_sources+=1;assert node['address'] in unknown_edges
    for node in branches:
        for edge in node['semantic_edges']:
            if edge['target']:assert (node['address'],edge['target'],edge['kind']) in branch_edges
    assert summary['missing_pages']==0
    for name,digest in summary['interpretation_source_sha256'].items():
        assert hashlib.sha256((tree/'interpreter-sources'/Path(name).name).read_bytes()).hexdigest()==digest
    profile=json.loads((tree/'analysis-profile.json').read_text(encoding='utf-8'))
    for model in list(profile['runtime'].get('option_getters',{}).values())+list(profile['runtime'].get('predicate_models',{}).values()):
        proof=model['evidence'];assert hashlib.sha256(Path(proof['file']).read_bytes()).hexdigest()==proof['sha256']
    soup=BeautifulSoup((out/'index.html').read_text(encoding='utf-8'),'html.parser')
    links=[el['href'] for el in soup.select('a[href]') if not el['href'].startswith(('https:','http:','#'))]
    assert all((out/unquote(h.split('#')[0])).exists() for h in links)
    info={'previous_nodes_retained':len(old),'current_nodes':len(current),'option_entries_retained':entries,'zero_valued_entries_retained':zero_values,
        'unresolved_option_sources_with_edges':unknown_sources,'indirect_branch_nodes_checked':len(branches),'missing_pages':0,'local_links_verified':len(links),
        'callbacks_executed_by_validation':False,'scope':'Saved evidence only; all option alternatives and both conditional branches retained'}
    (out/'verification.json').write_text(json.dumps(info,indent=2),encoding='utf-8');print(json.dumps(info,indent=2))


if __name__=='__main__':main()
