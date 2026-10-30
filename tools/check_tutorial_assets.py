"""Check tutorial images on disk, in the skill copy and in a selected Git revision."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
from urllib.parse import unquote,urlsplit

ROOT=Path(__file__).resolve().parents[1]


def git(*args):
    return subprocess.check_output(['git','-c','safe.directory='+ROOT.as_posix(),*args],cwd=ROOT)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--git-ref',help='Check committed image bytes, e.g. HEAD or origin/main after fetching')
    p.add_argument('--bundle',action='store_true',help='Also compare images carried by the generated skill')
    p.add_argument('--output',type=Path)
    a=p.parse_args();document=ROOT/'如何调试iosd.md';assets=ROOT/'assets/如何调试iosd'
    refs=[]
    for target in re.findall(r'!\[[^\]]*\]\(([^)\n]+)\)',document.read_text(encoding='utf-8')):
        parts=urlsplit(target.strip('<>'))
        if parts.scheme or parts.netloc:continue
        image=(document.parent/unquote(parts.path)).resolve()
        image.relative_to(assets.resolve())
        if image not in refs:refs.append(image)
    files=sorted(path for path in assets.rglob('*') if path.is_file())
    result={'referenced_images':len(refs),'image_directory_files':len(files),
            'unused_assets':[p.relative_to(ROOT).as_posix() for p in files if p not in refs],
            'missing_images':[p.relative_to(ROOT).as_posix() for p in refs if not p.is_file()],
            'git_ref':a.git_ref,'uncommitted_assets':[],'revision_byte_mismatches':[],
            'bundle_checked':a.bundle,'bundle_mismatches':[]}
    if a.git_ref:
        result['git_commit']=git('rev-parse','--verify',a.git_ref+'^{commit}').decode().strip()
        committed=set(git('ls-tree','-r','-z','--name-only',a.git_ref,'--','assets/如何调试iosd').decode('utf-8').split('\0'))
        for path in files:
            name=path.relative_to(ROOT).as_posix()
            if name not in committed:result['uncommitted_assets'].append(name)
            elif hashlib.sha256(path.read_bytes()).digest()!=hashlib.sha256(git('cat-file','blob',a.git_ref+':'+name)).digest():
                result['revision_byte_mismatches'].append(name)
    if a.bundle:
        for image in refs:
            bundled=ROOT/'skills/iosd-analysis/references/library'/image.relative_to(ROOT)
            if not image.is_file() or not bundled.is_file() or image.read_bytes()!=bundled.read_bytes():
                result['bundle_mismatches'].append(image.relative_to(ROOT).as_posix())
    result['passed']=not any(result[k] for k in ('missing_images','uncommitted_assets','revision_byte_mismatches','bundle_mismatches'))
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True)
        a.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,ensure_ascii=False))
    return 0 if result['passed'] else 1


if __name__=='__main__':raise SystemExit(main())
