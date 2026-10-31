"""Verify command-text hashes, every source ID/syntax, local links and evidence anchors."""
import argparse
from collections import Counter
import hashlib,json,re,sys
from pathlib import Path
from urllib.parse import unquote,urlsplit
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from tools.export_cli_textbook import MODELS,rows,verify_sources


def check_book(version,book):
    version=version.resolve();book=book.resolve();identity,hashes=verify_sources(version)
    manifest=json.loads((book/'manifest.json').read_text(encoding='utf-8'))
    if identity!=manifest['identity'] or hashes!=manifest['source_sha256']:raise ValueError('Book source identity/hash mismatch')
    generator=Path(__file__).with_name('export_cli_textbook.py')
    if hashlib.sha256(generator.read_bytes()).hexdigest()!=manifest['generator_sha256']:raise ValueError('Generator changed; rebuild book')
    texts={};plain={};counts=Counter();links_checked=0;anchors={};details={}
    for relative,sha in manifest['artifact_sha256'].items():
        path=(book/relative).resolve();path.relative_to(book)
        raw=path.read_bytes()
        if hashlib.sha256(raw).hexdigest()!=sha:raise ValueError('Changed artifact: '+relative)
        if len(raw)>manifest['page_max_utf8_bytes']:raise ValueError('Oversized page: '+relative)
        text=raw.decode('utf-8');texts[path]=text
        if relative.endswith('.txt'):
            model=re.sub(r'-\d+\.txt$','',path.name)
            if model not in MODELS:raise ValueError('Unknown text model: '+relative)
            for line in text.splitlines():
                if not line or line.startswith('#'):continue
                command,evidence=line.rsplit('    # ',1);key=(model,evidence)
                if key in plain:raise ValueError('Repeated source ID: '+str(key))
                plain[key]=command;counts[model]+=1
        if relative.startswith('modes/') and path.suffix=='.md' and path.name!='README.md':
            model=re.sub(r'-\d+\.md$','',path.name)
            matches=list(re.finditer(r'^### ([a-zA-Z0-9_-]+)\s*$',text,re.MULTILINE))
            for index,match in enumerate(matches):
                key=(model,match[1]);end=matches[index+1].start() if index+1<len(matches) else len(text)
                if key in details:raise ValueError('Repeated detailed source ID: '+str(key))
                details[key]=text[match.end():end]
    source_count=0
    for model,(_,relative) in MODELS.items():
        for row in rows(version/relative):
            key=(model,row['evidence_id']);expected='('+row['prompt']+')# '+row['syntax_candidate']
            if plain.pop(key,None)!=expected:raise ValueError('Missing/changed command text: '+str(key))
            detail=details.pop(key,None)
            if detail is None or expected not in detail:raise ValueError('Missing/changed detailed text: '+str(key))
            source_count+=1
    if plain or details:raise ValueError('Additional text records without source')
    if dict(counts)!=manifest['source_records'] or source_count!=manifest['exported_witnesses']:raise ValueError('Record counts differ')
    checked=set();resolved_paths={}
    for path,text in texts.items():
        if path.suffix!='.md':continue
        for match in re.finditer(r'\[[^\]\n]*\]\(([^)\n]+)\)',text):
            parts=urlsplit(match[1])
            if parts.scheme or parts.netloc:continue
            path_key=(path.parent,parts.path)
            if path_key not in resolved_paths:
                target=(path.parent/unquote(parts.path)).resolve() if parts.path else path
                target.relative_to(version);resolved_paths[path_key]=target
            target=resolved_paths[path_key]
            key=(target,parts.fragment)
            if key not in checked:
                if not target.is_file():raise ValueError('Broken link: '+str(path)+' -> '+match[1])
                if parts.fragment:
                    if target not in anchors:
                        body=texts.get(target)
                        if body is None:body=target.read_text(encoding='utf-8')
                        anchors[target]={m[1].strip().lower() for m in re.finditer(r'^### ([a-zA-Z0-9_-]+)\s*$',body,re.MULTILINE)}
                    if parts.fragment.lower() not in anchors[target]:raise ValueError('Missing evidence anchor: '+match[1])
                checked.add(key)
            links_checked+=1
    return {'witness_records_verified':source_count,'artifact_hashes_verified':len(texts),
        'local_links_verified':links_checked,'distinct_link_targets':len(checked),'passed':True}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--version',type=Path,required=True);p.add_argument('--book',type=Path,required=True)
    a=p.parse_args();print(json.dumps(check_book(a.version,a.book)))


if __name__=='__main__':main()
