"""Publish derived CLI metadata from saved analysis without captured bytes or code."""
import argparse,collections,gzip,hashlib,json
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from iosd_helper.syntax_paths import raw_links
from tools.recover_saved_cli import evidence_value


def reference(value,base,ranges):
    if not value:return None
    rva=value-base
    return {'space':'image','rva':rva} if any(a<=rva<b for a,b in ranges) else {'space':'captured_runtime','va':value}


def public_node(row,base,ranges):
    omitted={'address','image_rva','payload','action_dispatch_observation','action_function',
             'action_registry_entry','keyword_address','privilege_record_address',
             'privilege_descriptor_address','option_privilege_address','handler_candidate','nvgen_callback_candidate'}
    out=evidence_value({k:v for k,v in row.items() if k not in omitted},base,ranges)
    out['id']=reference(row['address'],base,ranges)
    for key in omitted-{'address','image_rva','payload','action_dispatch_observation'}:
        if row.get(key):out[key]=reference(row[key],base,ranges)
    out['links']={key:reference(value,base,ranges) for key,value in zip(('accept','alternate'),raw_links(row))}
    out['dispatch_verified']=row.get('action_dispatch_observation',{}).get('verified',False)
    return out


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('nodes','refinement','paths','baseline','registrations','layout','output'):
        p.add_argument('--'+name,required=True,type=Path)
    a=p.parse_args();a.output.mkdir(parents=True,exist_ok=True)
    refined=json.loads(a.refinement.read_text(encoding='utf-8'))
    paths=json.loads(a.paths.read_text(encoding='utf-8'));baseline=json.loads(a.baseline.read_text(encoding='utf-8'))
    layout=json.loads(a.layout.read_text(encoding='utf-8'))
    md5=refined['identity']['input_md5']
    if any(x!=md5 for x in (paths['identity']['input_md5'],baseline['identity']['input_md5'],layout['identity']['input_md5'])):
        raise ValueError('Analysis identities differ')
    base=refined['identity']['imagebase'];ranges=[(s['address'],s['address']+s['memory_size']) for s in layout['load_segments']]
    unknown=collections.Counter();config_unknown=collections.Counter();nodes=unbound=0
    with a.nodes.open(encoding='utf-8') as source,gzip.open(a.output/'nodes.jsonl.gz','wt',encoding='utf-8',compresslevel=7) as dest:
        for line in source:
            row=json.loads(line);nodes+=1
            unbound+=not bool(row.get('connected_mode_candidates'))
            if not row.get('path_semantics') or row.get('semantic_error'):
                action=row.get('action_name',row.get('reason','unread'));unknown[action]+=1
                if 'configure' in row.get('connected_mode_candidates',[]):config_unknown[action]+=1
            dest.write(json.dumps(public_node(row,base,ranges),ensure_ascii=False,separators=(',',':'))+'\n')
    registrations=[]
    for line in a.registrations.open(encoding='utf-8'):
        r=json.loads(line)
        registrations.append({k:r.get(k) for k in ('registration_rva','key_rva','root_rva','owner_candidate',
            'conditions','source_call_sites','observed_binding_evidence','unknown','runtime_status',
            'connected_modes','dynamic_key_observed','availability_verified')})
    write=lambda name,data:(a.output/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    with gzip.open(a.output/'registrations.json.gz','wt',encoding='utf-8',compresslevel=7) as dest:
        json.dump({'identity':refined['identity'],'scope':'Historical registration comparison; mode membership from original export',
        'coordinates':'*_rva and source_call_sites use image RVAs; *_va in binding evidence use recorded runtime addresses',
        'records':registrations},dest,ensure_ascii=False,separators=(',',':'))
    # Report frontiers and remaining actions separately from preferred witnesses.
    write('gaps.json',{'opaque_actions_all_nodes':dict(unknown.most_common()),'opaque_actions_configure':dict(config_unknown.most_common()),
        'missing_pages_captured_va':refined['missing_pages'],'page_conflicts':refined['page_conflicts'],
        'unbound_to_six_mode_candidates':unbound,
        'frontiers':{m['mode']:m['frontiers'] for m in paths['modes']},
        'conditions_evaluated':False,'additional_gaps':['64-bit number variants and protocol-specific parameter actions',
        'General keyword storage effects, URL helper constraints and predicate internals',
        'Other parser modes, registration epochs and command variant enumeration']})
    write('summary.json',{'identity':refined['identity'],'atomic_snapshot':False,
        'capture_file_count':refined['capture_file_count'],'captured_utc_range':refined['captured_utc_range'],
        'interpretation_date':'2026-10-30','counts':refined['counts'],'nodes_exported':nodes,
        'edges_original_export':baseline['runtime_edges'],'refinement_modes':refined['modes'],
        'paths':{k:v for k,v in paths.items() if k not in ('modes','mode_roots')},
        'modes':[{k:v for k,v in m.items() if k!='frontiers'} for m in paths['modes']],
        'mode_roots':paths['mode_roots'],'static_registration_status':baseline['static_registration_status'],
        'action_dispatch':baseline['runtime_action_dispatch'],
        'provenance':{'input_sha256':refined['input_sha256'],'source_sha256':refined['source_sha256'],
                      'registration_source_sha256':hashlib.sha256(a.registrations.read_bytes()).hexdigest()},
        'artifact_sha256':{f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in sorted(a.output.iterdir()) if f.is_file() and f.name not in ('summary.json','README.md')}})
    print(json.dumps({'nodes':nodes,'unbound':unbound,'config_opaque':sum(config_unknown.values()),'config_actions':config_unknown.most_common(10)}))


if __name__=='__main__':main()
