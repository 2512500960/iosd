"""Offline checks for portable skill files, local links and generated source integrity."""
import ast
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import unquote,urlsplit
import zipfile


def main():
    root=Path(__file__).resolve().parents[1];skill=root/'skills/iosd-analysis'
    manifest=json.loads((skill/'build-manifest.json').read_text(encoding='utf-8'))
    checked=0
    for relative,row in manifest['generated'].items():
        source=root/row['source'];target=skill/relative
        assert hashlib.sha256(source.read_bytes()).hexdigest()==row['source_sha256'],f'Stale source: {source}'
        assert hashlib.sha256(target.read_bytes()).hexdigest()==row['sha256'],f'Stale generated file: {target}'
        checked+=1
    for path in skill.rglob('*.py'):ast.parse(path.read_text(encoding='utf-8'),filename=str(path))
    links=0
    for path in skill.rglob('*.md'):
        text=path.read_text(encoding='utf-8')
        for match in re.finditer(r'(?<!!)\[[^\]]+\]\(([^)\n]+)\)',text):
            target=match[1].strip('<>');parts=urlsplit(target)
            if parts.scheme or parts.netloc or target.startswith('#'):continue
            resolved=(path.parent/unquote(parts.path)).resolve()
            resolved.relative_to(skill.resolve())
            assert resolved.is_file(),f'Missing skill reference: {path}: {target}'
            links+=1
    for name in ('ui.py','integer_ui.py','project_ui.py','protocol_ui.py','graph_view.py'):
        assert not (skill/'scripts/iosd_helper'/name).exists(),'GUI dependency bundled'
    assert '172.16.' not in (skill/'SKILL.md').read_text(encoding='utf-8')
    archive=root/'dist'/('iosd-analysis-skill-'+manifest['version']+'.zip')
    with zipfile.ZipFile(archive) as package:
        assert package.testzip() is None
        for name in package.namelist():
            assert not name.endswith(('.i64','.idb','.core','.so','.bin','.elf','.pyc'))
            assert not name.startswith('/') and '..' not in Path(name).parts
    print(json.dumps({'generated_sources_checked':checked,'local_links_checked':links,'archive_verified':True,
                      'ida_access':False,'mcp_access':False}))


if __name__=='__main__':main()
