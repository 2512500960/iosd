"""Recover static mode candidates from saved ctree batches and a verified ELF."""
import argparse,hashlib,json,mmap
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from iosd_helper.parser_modes import recover_mode_definitions,configuration_ancestry,recover_link_creations


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('batches','profile','layout','elf','output'):p.add_argument('--'+name,required=True,type=Path)
    a=p.parse_args();profile=json.loads(a.profile.read_text(encoding='utf-8'));layout=json.loads(a.layout.read_text(encoding='utf-8'))
    digest=hashlib.md5();sha=hashlib.sha256()
    with a.elf.open('rb') as stream:
        for block in iter(lambda:stream.read(8*1024*1024),b''):digest.update(block);sha.update(block)
    if digest.hexdigest()!=profile['input_md5'] or sha.hexdigest()!=layout['identity']['sha256']:
        raise ValueError('Original ELF differs from mode consumer/layout identity')
    functions=[];identity=None;sources={}
    for path in sorted(a.batches.rglob('*.json')):
        batch=json.loads(path.read_text(encoding='utf-8'))
        if identity is not None and batch['identity']!=identity:raise ValueError('Mode batches belong to different sessions')
        identity=batch['identity'];functions.extend(batch['functions']);sources[path.relative_to(a.batches).as_posix()]=hashlib.sha256(path.read_bytes()).hexdigest()
    superseded=sum(bool(f.get('error') or f.get('truncated')) for f in functions)
    preferred={}
    for function in functions:
        old=preferred.get(function['rva'])
        if old is None or (bool(old.get('error') or old.get('truncated')) and not (function.get('error') or function.get('truncated'))):
            preferred[function['rva']]=function
    functions=list(preferred.values())
    segments=layout['load_segments'];ranges=[(s['address'],s['address']+s['memory_size']) for s in segments]
    with a.elf.open('rb') as stream,mmap.mmap(stream.fileno(),0,access=mmap.ACCESS_READ) as raw:
        def read_string(rva):
            for segment in segments:
                if segment['address']<=rva<segment['address']+segment['file_size']:
                    start=segment['file_offset']+rva-segment['address'];limit=min(512,segment['file_size']-(rva-segment['address']))
                    data=raw[start:start+limit];end=data.find(b'\0')
                    if end<0:raise ValueError('String not terminated within file-backed range')
                    value=data[:end].decode('ascii')
                    if any(ord(c)<32 or ord(c)>=127 for c in value):raise ValueError('Non-printable mode string')
                    return value
            raise ValueError('String outside file-backed ELF segments')
        result=recover_mode_definitions(functions,identity,profile,read_string,ranges)
    result.update(identity={'input_md5':identity['input_md5'],'imagebase':identity['imagebase']},
        string_source={'source':'original ELF file','md5':digest.hexdigest(),'sha256':sha.hexdigest()},
        capture_source={'source':'saved IDB ctree; no live target memory acquired','functions':len(functions),
                        'incomplete_function_attempts_retained_in_sources':superseded,'batch_sha256':sources},
        configuration_ancestry=configuration_ancestry(result['modes']),
        static_link_creations=recover_link_creations(functions,identity,profile,ranges))
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'functions':len(functions),'calls':result['calls'],'modes':len(result['modes']),
        'named_modes':sum(bool(m['name']) for m in result['modes']),'rooted_modes':sum(m.get('root_rva') is not None for m in result['modes']),
        'config_family':sum(x['configuration_family_candidate'] for x in result['configuration_ancestry'].values()),
        'errors':result['functions_with_errors']}))


if __name__=='__main__':main()
