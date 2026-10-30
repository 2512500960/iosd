"""Refine a saved CLI graph using hash-verified capture pages; runs entirely offline."""
import argparse
from collections import Counter,defaultdict
import hashlib,json
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from iosd_helper.cli_refinement import refine_node
from iosd_helper.runtime_grammar import CapturedPages


def digest(path):
    result=hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda:stream.read(8*1024*1024),b''):result.update(block)
    return result.hexdigest()


def opaque(node):return not node.get('path_semantics') or bool(node.get('semantic_error'))


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--nodes',type=Path,required=True)
    p.add_argument('--summary',type=Path,required=True);p.add_argument('--profile',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    a=p.parse_args();baseline=json.loads(a.summary.read_text(encoding='utf-8'));profile=json.loads(a.profile.read_text(encoding='utf-8'))
    identity=baseline['identity'];base=identity['imagebase']
    if identity['input_md5']!=profile['input_md5']:raise ValueError('Profile and saved graph MD5 differ')
    a.output.mkdir(parents=True,exist_ok=True)
    if a.nodes.resolve()==(a.output/'nodes.jsonl').resolve():raise ValueError('Write refined nodes to a new directory')
    capture_dates=[]
    def captures():
        for spec in baseline['source_files']:
            path=Path(spec['path'])
            if digest(path)!=spec['sha256']:raise ValueError('Capture SHA256 differs: '+str(path))
            capture=json.loads(path.read_text(encoding='utf-8'))
            if capture.get('input_md5')!=identity['input_md5'] or capture.get('runtime_base')!=base:
                raise ValueError('Saved page image identity/base differs')
            if capture.get('captured_utc'):capture_dates.append(capture['captured_utc'])
            yield capture
    memory=CapturedPages(captures())
    if memory.conflicts:raise ValueError('Conflicting captured pages: retain separate snapshots')
    counts=Counter();actions=defaultdict(Counter);modes=defaultdict(Counter);unknown=Counter()
    with a.nodes.open(encoding='utf-8') as source,(a.output/'nodes.jsonl').open('w',encoding='utf-8') as target,\
         (a.output/'updates.jsonl').open('w',encoding='utf-8') as updates:
        for line in source:
            old=json.loads(line);new=refine_node(memory,old,profile,identity);row=new or old
            target.write(json.dumps(row,ensure_ascii=False)+'\n' if new is not None else line)
            counts['nodes']+=1
            if new is not None:
                counts['reviewed_nodes']+=1;actions[old['action_name']]['nodes']+=1
                promoted=opaque(old) and not opaque(row)
                actions[old['action_name']]['opaque_resolved']+=int(promoted)
                counts['opaque_resolved']+=int(promoted)
                if row.get('semantic_error'):actions[old['action_name']]['decode_errors']+=1
                if row.get('refinement_skipped'):actions[old['action_name']]['dispatch_skipped']+=1
                updates.write(json.dumps(row,ensure_ascii=False)+'\n')
            for mode in old.get('connected_mode_candidates',[]):
                c=modes[mode];c['nodes']+=1;c['opaque_before']+=int(opaque(old));c['opaque_after']+=int(opaque(row))
                c['nodes_with_uncertainty_after']+=bool(row.get('remaining_uncertainties'))
                if new is not None:c['reviewed_nodes']+=1
            if opaque(row):unknown[row.get('action_name',row.get('reason','unclassified'))]+=1
    summary={'schema_version':1,'kind':'cli_semantic_refinement','identity':identity,'source':'saved capture series',
        'counts':dict(counts),'actions':dict(actions),'modes':dict(modes),'remaining_opaque_by_action':dict(unknown),
        'missing_pages':sorted(memory.missing_pages),'page_conflicts':memory.conflicts,
        'input_sha256':{'nodes':digest(a.nodes),'summary':digest(a.summary),'profile':digest(a.profile)},
        'source_sha256':{name:digest(Path(__file__).resolve().parents[1]/name) for name in
            ('iosd_helper/grammar_semantics.py','iosd_helper/syntax_paths.py','iosd_helper/cli_refinement.py')},
        'path_recovery_rerun':False,'atomic_snapshot':False,
        'capture_file_count':len(baseline['source_files']),
        'captured_utc_range':[min(capture_dates),max(capture_dates)] if capture_dates else [],
        'scope':'Node interpretation over the source graph membership; conditions, unbound fragments and raw records retained'}
    (a.output/'summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'counts':summary['counts'],'modes':summary['modes'],'missing_pages':len(memory.missing_pages)},ensure_ascii=False))


if __name__=='__main__':main()
