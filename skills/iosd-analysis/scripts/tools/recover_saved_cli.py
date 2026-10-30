"""Recover saved CLI witnesses as a stream and export a compact evidence catalogue."""
import argparse,gzip,hashlib,json
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from iosd_helper.syntax_paths import recover_paths


def evidence_value(value,base,image_ranges):
    """Remove full raw records; name image references explicitly, keep other scalars."""
    if isinstance(value,list):return [evidence_value(x,base,image_ranges) for x in value]
    if not isinstance(value,dict):return value
    out={}
    for key,item in value.items():
        if key in ('raw_hex','descriptor_raw_hex','runtime_raw_hex'):continue
        references=('node','source','target','function','variable_address','function_candidate','callback',
                    'source_address','decoder_address','predicate_candidate','false_target_candidate','bounds_callback','validation_callback')
        if key in references and isinstance(item,int) and item>=base:
            if any(lo<=item-base<hi for lo,hi in image_ranges):out[key+'_rva']=item-base
            else:out[key+'_captured_va']=item
        elif key.endswith('_raw_hex') and isinstance(item,str):
            # Encoded flags/constant fields remain useful evidence, rather than whole descriptors.
            if len(item)<=16:out[key[:-8]+'_encoded_hex']=item
        else:out[key]=evidence_value(item,base,image_ranges)
    return out


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--nodes',required=True,type=Path);p.add_argument('--modes',required=True,type=Path)
    p.add_argument('--settings',required=True,type=Path);p.add_argument('--identity',required=True,type=Path)
    p.add_argument('--layout',required=True,type=Path)
    p.add_argument('--output',required=True,type=Path);p.add_argument('--catalogue',required=True,type=Path)
    p.add_argument('--max-states',type=int,default=500000);p.add_argument('--max-paths',type=int,default=150000)
    a=p.parse_args();meta=json.loads(a.identity.read_text(encoding='utf-8'))
    identity=meta['identity'];base=identity['imagebase'];a.output.mkdir(parents=True,exist_ok=True)
    layout=json.loads(a.layout.read_text(encoding='utf-8'))
    if layout['identity']['input_md5']!=identity['input_md5']:raise ValueError('ELF layout and graph identity differ')
    a.catalogue.parent.mkdir(parents=True,exist_ok=True)
    graph={'nodes':[json.loads(line) for line in a.nodes.open(encoding='utf-8')],
           'mode_definitions':json.loads(a.modes.read_text(encoding='utf-8')),
           'path_analysis':json.loads(a.settings.read_text(encoding='utf-8')),'registrations':[]}
    names=[m['name'] for m in graph['mode_definitions']]
    code_ranges=[(s['address'],s['address']+s['memory_size']) for s in layout['load_segments'] if 'X' in s['permissions']]
    image_ranges=[(s['address'],s['address']+s['memory_size']) for s in layout['load_segments']]
    count=0
    with gzip.open(a.output/'paths.jsonl.gz','wt',encoding='utf-8',compresslevel=5) as raw,\
         gzip.open(a.catalogue,'wt',encoding='utf-8',compresslevel=7) as public:
        def emit(row):
            nonlocal count
            count+=1
            raw.write(json.dumps(row,ensure_ascii=False)+'\n')
            handler=row['handler'];rva=handler-base
            compact={k:row[k] for k in ('mode','prompt','syntax_candidate','selector_candidate','syntax_status','final_tracked_state')}
            compact['handler']={'space':'image','rva':rva} if any(lo<=rva<hi for lo,hi in code_ranges) else {'space':'captured_runtime','va':handler}
            compact.update(conditions=evidence_value(row['conditions'],base,image_ranges),
                state_effects=evidence_value(row['state_effects'],base,image_ranges),parameters=evidence_value(row['parameters'],base,image_ranges),
                gaps=evidence_value(row['gaps'],base,image_ranges),eol_node=evidence_value({'node':row['eol_node']},base,image_ranges),
                evidence_id='path-%06d'%count,
                availability='Observed graph connection with symbolic conditions from the recorded capture series')
            public.write(json.dumps(compact,ensure_ascii=False,separators=(',',':'))+'\n')
        result=recover_paths(graph,names,a.max_states,a.max_paths,record_sink=emit)
    result['summary'].update(identity=identity,source='Saved capture series interpreted offline',
        node_refinement_sha256=hashlib.sha256(a.identity.read_bytes()).hexdigest(),
        catalogue_sha256=hashlib.sha256(a.catalogue.read_bytes()).hexdigest(),
        handler_image_executable_rva_ranges=code_ranges,
        catalogue_records=count,catalogue_bytes=a.catalogue.stat().st_size)
    (a.output/'summary.json').write_text(json.dumps(result['summary'],ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'paths':count,'catalogue_bytes':a.catalogue.stat().st_size,
                     'modes':[{k:v for k,v in m.items() if k!='frontiers'} for m in result['summary']['modes']]}),flush=True)


if __name__=='__main__':main()
