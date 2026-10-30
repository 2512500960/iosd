"""Verify a retained-cohort investigation and record derived diagnostics and hashes."""
import argparse
from collections import Counter,defaultdict
import gzip,hashlib,json
from pathlib import Path


def records(path):
    with gzip.open(path,'rt',encoding='utf-8') as stream:
        for line in stream:yield json.loads(line)


def key(value):return json.dumps(value,sort_keys=True,separators=(',',':'))


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--version',required=True,type=Path);a=p.parse_args()
    root=Path(__file__).resolve().parents[1];version=a.version;folder=version/'unbound-cli'
    modes=json.loads((version/'parser-modes.json').read_text(encoding='utf-8'))
    baseline=json.loads((version/'cli-counts.json').read_text(encoding='utf-8'))
    summary=json.loads((folder/'summary.json').read_text(encoding='utf-8'))
    paths=json.loads((folder/'path-summary.json').read_text(encoding='utf-8'))
    assert modes['identity']['input_md5']==baseline['identity']['input_md5']==summary['identity']['input_md5']==paths['identity']['input_md5']
    by_id={m['id']:m for m in modes['modes']};keys={c['key_rva'] for c in modes['static_link_creations'] if c.get('key_rva') is not None}
    cohort=set();categories=Counter();missing=Counter();other=Counter()
    for row in records(folder/'terminals.jsonl.gz'):
        ref=key(row['eol']);assert ref not in cohort;cohort.add(ref);categories[row['category']]+=1
        if row['category']=='registration_fragment_without_acquired_mode_path':
            missing['static_key_creation_seen_without_mode_path' if any(r['key_rva'] in keys for r in row['registration_root_associations'])
                    else 'key_creation_not_in_this_mode_caller_acquisition']+=1
        if row['category']=='additional_other_mode_root':
            for mode_id in row['observed_mode_candidates']:
                mode=by_id[mode_id];other[(mode['name'],mode['prompt'],mode['parent'])]+=1
    assert len(cohort)==summary['baseline_cohort']==baseline['definitions']['terminal_candidates_without_selected_mode_membership']
    assert dict(categories)==summary['categories']
    covered=set();models={}
    for name,data in paths['models'].items():
        count=0;seen=set()
        for row in records(folder/(name+'.jsonl.gz')):
            count+=1;node=row['eol_node']
            ref={'space':'image','rva':node['node_rva']} if 'node_rva' in node else {'space':'captured_runtime','va':node['node_captured_va']}
            refkey=key(ref);assert refkey in cohort;seen.add(refkey)
            assert row['model']==name
            if name not in ('observed_connections','other_mode_connections'):
                assert row['conditional_registrations'] and row['syntax_status']=='partial_syntax_candidate'
        assert count==data['records'] and len(seen)==data['cohort_eols_recovered']
        covered.update(seen)
        models[name]={'records':count,'covered_eols':len(seen),'target_eols':data['cohort_target_eols'],
            'stop_reasons':dict(Counter(s['stop_reason'] for s in data['root_summaries'])),
            'dropped_records':data['dropped_records'],'unprocessed_roots':len(data['unprocessed_root_rvas'])}
    diagnostics={'identity':summary['identity'],'unresolved_registration_subgroups':dict(missing),
        'other_mode_candidates':[{'name':n,'prompt':pr,'parent':pa,'cohort_eols':c} for (n,pr,pa),c in other.items()],
        'notes':['These are cohort subgroup counts, not the total runtime pending list or actual availability.',
                 'Static creation sites are limited to the acquired mode-factory callers; other callers remain uninspected.']}
    (folder/'diagnostics.json').write_text(json.dumps(diagnostics,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    sources=['iosd_helper/parser_modes.py','iosd_helper/unbound_cli.py','iosd_helper/ida_lifecycle.py',
        'iosd_helper/runtime_grammar.py','iosd_helper/grammar_semantics.py','iosd_helper/syntax_paths.py',
        'tools/recover_parser_modes.py','tools/extend_saved_mode_roots.py','tools/analyze_unbound_cli.py',
        'tools/recover_unbound_paths.py','tools/finalize_cli_investigation.py','profiles/parser_modes_26_01_02.json']
    artifacts=[version/'parser-modes.json',*sorted(p for p in folder.iterdir() if p.is_file() and p.name!='manifest.json')]
    manifest={'identity':summary['identity'],'verified_cohort':len(cohort),'categories':dict(categories),
        'models':models,'covered_original_cohort_eols':len(covered),'cohort_without_mode_local_witness':len(cohort-covered),
        'artifact_sha256':{p.relative_to(version.resolve()).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in (x.resolve() for x in artifacts)},
        'interpretation_source_sha256':{name:hashlib.sha256((root/name).read_bytes()).hexdigest() for name in sources},
        'scope':'Source/hash and exact cohort/count checks; conditions and target code were not executed'}
    (folder/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in manifest.items() if k not in ('artifact_sha256','interpretation_source_sha256')}))


if __name__=='__main__':main()
