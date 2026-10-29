"""Compare saved NVGEN descriptors and CLI terminals, without executing callbacks."""
import argparse
from collections import Counter, defaultdict
import json
from pathlib import Path


def analyze(rows, base):
    nvgen, terminals, iterators, gaps = [], defaultdict(list), [], []
    for row in rows:
        address = row.get('address')
        if row.get('semantic_role') == 'command_terminal':
            callback = row.get('handler_candidate')
            if callback:
                terminals[callback].append({'node':address,'selector':row.get('selector_candidate'),
                    'action':row.get('action_name'),'dispatch_verified':not row.get('dispatch_semantics_unverified',False)})
        if row.get('semantic_role') == 'configuration_generation' or row.get('action_name') == 'nvgens_action':
            encoded = row.get('descriptor_raw_hex') or ''
            error = None
            try:
                raw = bytes.fromhex(encoded)
            except (TypeError,ValueError) as exc:
                raw = b''
                error = str(exc)
            record={'node':address,'callback':row.get('nvgen_callback_candidate'),
                    'selector':int.from_bytes(raw[8:12],'big') if len(raw)>=12 else None,
                    'flags_raw_hex':raw[12:16].hex() if len(raw)>=16 else None,
                    'descriptor_raw_hex':encoded,'descriptor_decode_error':error,
                    'dispatch_verified':not row.get('dispatch_semantics_unverified',False)}
            nvgen.append(record)
            if len(raw)<16 or not record['callback'] or not record['dispatch_verified']:
                gaps.append({'node':address,'reason':'NVGEN descriptor/callback/dispatch incompletely resolved','record':record})
        if row.get('iterator',{}).get('callback'):
            iterators.append({'node':address,**row['iterator']})
    associations=[]
    for row in nvgen:
        callback=row['callback']
        matches=terminals.get(callback,[]) if callback else []
        exact=[r for r in matches if r['selector']==row['selector'] and r['selector'] is not None
               and row['dispatch_verified'] and r['dispatch_verified']]
        associations.append({**row,'callback_rva':callback-base if callback and base<=callback<base+0x50000000 else None,
                             'cli_terminal_matches':matches,'same_function_and_selector_matches':exact,
                             'meaning':'Descriptor identity only; does not prove equivalent behavior or current reachability'})
    return {'summary':{'nvgen_nodes':len(nvgen),'nvgen_distinct_nonzero_callbacks':len({r['callback'] for r in nvgen if r['callback']}),
                      'cli_terminal_nodes':sum(map(len,terminals.values())),
                      'nvgen_nodes_sharing_cli_function':sum(bool(r['cli_terminal_matches']) for r in associations),
                      'nvgen_nodes_sharing_cli_function_and_selector':sum(bool(r['same_function_and_selector_matches']) for r in associations),
                      'iterator_nodes':len(iterators),'unresolved_nvgen_descriptors':len(gaps)},
            'nvgen':nvgen,'associations':associations,'iterators':iterators,'gaps':gaps}


def main():
    cli=argparse.ArgumentParser(description=__doc__)
    cli.add_argument('tree');cli.add_argument('--output',required=True)
    args=cli.parse_args();tree=Path(args.tree);out=Path(args.output);out.mkdir(parents=True,exist_ok=True)
    identity=json.loads((tree/'summary.json').read_text(encoding='utf-8'))['identity']
    with (tree/'nodes.jsonl').open(encoding='utf-8') as stream:
        result=analyze((json.loads(line) for line in stream),identity['imagebase'])
    for key,name in [('nvgen','nvgen-nodes'),('associations','cli-nvgen-associations'),('iterators','iterator-nodes'),('gaps','unresolved-nvgen')]:
        with (out/(name+'.jsonl')).open('w',encoding='utf-8') as stream:
            for row in result[key]:stream.write(json.dumps(row,ensure_ascii=False)+'\n')
    summary={'identity':identity,**result['summary'],
             'scope':'All acquired nodes in supplied saved graph; not all components or all configuration lines',
             'cli_terminal_scope':'Decoded command_terminal records only; combined/custom terminal actions are outside this comparison',
             'descriptor_scope':'Zero descriptor gaps does not mean callback bodies, predicates or generated objects are fully understood',
             'target_callbacks_executed':False,'unknown_records_retained':True}
    (out/'binding-summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(summary,ensure_ascii=False))


if __name__=='__main__':main()
