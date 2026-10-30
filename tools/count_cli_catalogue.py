"""Count acquired CLI definitions, EOL/context witnesses and distinct template text."""
import argparse
from collections import Counter,defaultdict
import gzip,hashlib,json
from pathlib import Path


def rows(path):
    opener=gzip.open if path.suffix=='.gz' else open
    with opener(path,'rt',encoding='utf-8') as stream:
        for line in stream:
            if line.strip():yield json.loads(line)


def key(value):return json.dumps(value,sort_keys=True,separators=(',',':'))


def count_catalogue(records):
    counts=Counter();eols=set();handlers=set();texts=set();per_mode=defaultdict(lambda:{'records':0,'eols':set(),'handlers':set(),'texts':set()})
    for row in records:
        mode=row['mode'];eol=key(row['eol_node']);handler=key(row['handler']);text=row['syntax_candidate']
        counts['witness_records']+=1;counts['records_with_gaps']+=bool(row.get('gaps'))
        eols.add(eol);handlers.add(handler);texts.add((mode,text))
        item=per_mode[mode];item['records']+=1;item['eols'].add(eol);item['handlers'].add(handler);item['texts'].add(text)
    return {**counts,'unique_eol_nodes_across_modes':len(eols),'unique_handler_references':len(handlers),
        'distinct_mode_template_text_pairs':len(texts),'modes':{mode:{'witness_records':item['records'],
        'unique_eol_nodes':len(item['eols']),'unique_handler_references':len(item['handlers']),
        'distinct_template_texts':len(item['texts'])} for mode,item in per_mode.items()}}


def count_nodes(records):
    counts=Counter();spaces=Counter();semantics=Counter();mode_terminals=Counter()
    for row in records:
        counts['acquired_nodes']+=1
        if not row.get('path_semantics') or row.get('semantic_error'):counts['opaque_or_unread_nodes']+=1
        if row.get('path_semantics') not in ('terminal','parameter_terminal') or row.get('semantic_error'):continue
        counts['recognized_terminal_candidates']+=1;semantics[row['path_semantics']]+=1
        spaces[row['id']['space']]+=1
        if not row.get('connected_mode_candidates'):counts['terminal_candidates_without_selected_mode_membership']+=1
        if not row.get('handler_candidate'):counts['terminal_candidates_without_handler']+=1
        if not row.get('dispatch_verified'):counts['terminal_candidates_with_unverified_dispatch']+=1
        mode_terminals.update(row.get('connected_mode_candidates',[]))
    return {**counts,'terminal_coordinate_spaces':dict(spaces),'terminal_semantics':dict(semantics),
            'terminal_mode_membership_from_source_graph':dict(mode_terminals)}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('catalogue','nodes','identity','output'):p.add_argument('--'+name,type=Path,required=True)
    a=p.parse_args();meta=json.loads(a.identity.read_text(encoding='utf-8'));hashes={}
    for path in (a.catalogue,a.nodes):
        digest=hashlib.sha256(path.read_bytes()).hexdigest()
        if meta['artifact_sha256'].get(path.name)!=digest:raise ValueError('Input differs from recorded artifact: '+str(path))
        hashes[path.name]=digest
    result={'schema_version':1,'identity':meta['identity'],'capture_utc_range':meta['captured_utc_range'],
        'scope':'Acquired graph and six-mode preferred witnesses from saved capture series; whole ELF command total remains undetermined',
        'definitions':count_nodes(rows(a.nodes)),'catalogue':count_catalogue(rows(a.catalogue)),
        'input_sha256':hashes,
        'counting_rules':['Terminal means recognized terminal/parameter_terminal action, with no descriptor decode error.',
        'Global EOL and handler counts deduplicate address-space-qualified references across modes.',
        'Text counts use exact mode/template text; parameter values, aliases and unselected graph variants are not enumerated.',
        'Mode membership on nodes is inherited from the source graph; path counts follow the symbolic state model.',
        'Nodes, definitions, template text and actual executable command availability are separate measures.']}
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,ensure_ascii=False))


if __name__=='__main__':main()
