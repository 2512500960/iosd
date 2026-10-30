"""Assemble the self-contained skill from canonical code/docs, then verify a ZIP."""
import ast
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
from urllib.parse import unquote,urlsplit
import zipfile

ROOT=Path(__file__).resolve().parents[1]
SKILL=ROOT/'skills/iosd-analysis'
VERSION='0.3.3'
NO_UI={'ui','integer_ui','project_ui','protocol_ui','graph_view'}
NO_TOOLS={'build_skill_release.py','check_skill_release.py','check_tutorial_assets.py','build_plugin_release.py','build_iosd_handbook.py','check_iosd_handbook.py',
          'preview_ida_graph.py','preview_ida_catalogue.py','iosd_mcp.py'}


def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()


def assemble():
    copies={}
    copies[ROOT/'tools/iosd_mcp.py']=SKILL/'scripts/iosd_mcp.py'
    for source in (ROOT/'iosd_helper').glob('*.py'):
        if source.stem not in NO_UI:copies[source]=SKILL/'scripts/iosd_helper'/source.name
    for source in (ROOT/'tools').glob('*.py'):
        if source.name not in NO_TOOLS:copies[source]=SKILL/'scripts/tools'/source.name
    for source in (ROOT/'profiles').glob('*.json'):copies[source]=SKILL/'scripts/profiles'/source.name
    # Diagram sources and the self-contained reader are part of the architecture experience.
    for source in (ROOT/'docs/assets/iosd-atlas').glob('*.svg'):
        copies[source]=SKILL/'references/library/docs/assets/iosd-atlas'/source.name
    atlas=ROOT/'docs/iosd架构图解.html'
    if atlas.exists():copies[atlas]=SKILL/'references/library/docs'/atlas.name
    tutorial=ROOT/'如何调试iosd.md'
    for target in re.findall(r'!\[[^\]]*\]\(([^)\n]+)\)',tutorial.read_text(encoding='utf-8')):
        parts=urlsplit(target.strip('<>'))
        if parts.scheme or parts.netloc:continue
        source=(ROOT/unquote(parts.path)).resolve()
        source.relative_to((ROOT/'assets').resolve())
        if not source.is_file():raise ValueError('Tutorial image missing: '+str(source))
        copies[source]=SKILL/'references/library'/source.relative_to(ROOT)
    for source in (ROOT/'analysis/c8000v-26.01.02/cli').iterdir():
        if source.is_file():copies[source]=SKILL/'references/library/analysis/c8000v-26.01.02/cli'/source.name
    for source in (ROOT/'analysis/c8000v-26.01.02').glob('*.json'):
        copies[source]=SKILL/'references/library/analysis/c8000v-26.01.02'/source.name
    docs={p:SKILL/'references/library/docs'/p.name for p in (ROOT/'docs').glob('*.md')}
    docs[ROOT/'iosd二进制文件结构描述.md']=SKILL/'references/library/iosd二进制文件结构描述.md'
    docs[ROOT/'如何调试iosd.md']=SKILL/'references/library/如何调试iosd.md'
    docs[ROOT/'analysis/c8000v-26.01.02/README.md']=SKILL/'references/library/analysis/c8000v-26.01.02/README.md'
    # Hand-maintained skill references already live at their final destinations.
    link_targets={p:p for p in SKILL.rglob('*.md') if 'library' not in p.relative_to(SKILL).parts}
    link_targets.update({**copies,**docs})
    allowed=set(copies.values())|set(docs.values())
    # Remove only obsolete generated files enumerated by the previous manifest.
    previous=SKILL/'build-manifest.json'
    if previous.exists():
        for relative in json.loads(previous.read_text(encoding='utf-8')).get('generated',{}):
            target=(SKILL/relative).resolve()
            target.relative_to(SKILL.resolve())
            if target not in allowed and target.is_file():target.unlink()
    for source,destination in copies.items():
        destination.parent.mkdir(parents=True,exist_ok=True)
        if source.suffix=='.html':
            targets=link_targets
            def html_link(match):
                parts=urlsplit(match[2])
                if parts.scheme or parts.netloc or match[2].startswith('#'):return match[0]
                target=(source.parent/unquote(parts.path)).resolve()
                if target not in targets:raise ValueError('HTML link not bundled: '+str(target))
                relative=Path(os.path.relpath(targets[target],destination.parent)).as_posix()
                if parts.fragment:relative+='#'+parts.fragment
                return match[1]+relative+match[3]
            text=re.sub(r'(href=")([^"\n]+)(")',html_link,source.read_text(encoding='utf-8'))
            destination.write_text(text,encoding='utf-8',newline='\n')
        else:shutil.copyfile(source,destination)
    links=re.compile(r'(!?)\[([^\]]+)\]\(([^)\n]+)\)')
    for source,destination in docs.items():
        text=source.read_text(encoding='utf-8')
        def replace(match):
            target=match[3].strip('<>');parts=urlsplit(target)
            if parts.scheme in ('http','https','mailto') or target.startswith('#'):return match[0]
            path=(source.parent/unquote(parts.path)).resolve()
            targets=link_targets
            if path in targets:
                relative=Path(os.path.relpath(targets[path],destination.parent)).as_posix()
                if parts.fragment:relative+='#'+parts.fragment
                return match[1]+'['+match[2]+']('+relative+')'
            return match[2]+'（历史材料路径：`'+target+'`）'
        text=links.sub(replace,text)
        lines=text.splitlines()
        if source.name=='如何调试iosd.md':
            lines[1:1]=['','> 本文维护于仓库根目录；此处是随 skill 携带的参考副本。环境示例、版本结果和操作说明分别标明来源。','']
        else:
            lines[1:1]=['','> 样本分析资料：保留适用版本、条件和未知项。原始捕获保留在本地；标注的历史材料路径用于定位来源。','']
        destination.parent.mkdir(parents=True,exist_ok=True);destination.write_text('\n'.join(lines)+'\n',encoding='utf-8',newline='\n')
    tools=sorted((SKILL/'scripts/tools').glob('*.py'))
    catalogue=['# 脚本目录','','主入口 `scripts/iosd_mcp.py` 通过 MCP 采集；旧脚本继续复用现有算法。先运行所选脚本的 `--help`，只提供本次真实存在的输入。',
               '', '## 常用路线','',
               '- 静态 CLI：`validate_ida_backend.py` → `export_cli_catalogue.py` / `recover_iosd_syntax.py` → `build_candidate_space.py`。旧 profile 校验不能跳过。',
               '- 注册与状态：`audit_registration_triggers.py` → `collect_lifecycle_evidence.py` → `analyze_lifecycle.py`。ctree 采集与缓存文本导入的证据强度不同。',
               '- 动态命令图：`probe_ida_debug_state.py` → `probe_runtime_mapping.py` → `capture_debugger_memory.py` / `collect_runtime_pages.py` → `export_runtime_grammar.py` → 选项与报告工具。',
               '- 保存图的语义细化：`refine_cli_semantics.py` → `recover_saved_cli.py` → `export_cli_analysis.py`；查询现有目录使用 `query_cli_catalogue.py`。',
               '- core：`inspect_core.py`；与实时内存来源分开。',
               '- 架构：`build_architecture_map.py`；NVGEN：`analyze_nvgen_bindings.py`；EHSA：`build_ehsa_report.py`。这些使用已保存的输入，不能用缺失的历史路径冒充实机结果。',
               '- CDL：`walk_cdl.py`；作为独立数据源对照，不证明 iosd 命令完整。',
               '', '## 执行边界','',
               '旧脚本在 `scripts/tools/`，核心在 `scripts/iosd_helper/`，profile 在 `scripts/profiles/`。部分默认相对路径以 scripts 为工作目录；使用绝对输入路径和显式 `--profile` 更便于跨目录运行。',
               '', '旧批量采集器中有通过 IDA 主机文件系统读写 JSON 的实现，运行前核对客户端与 IDA 是否共享这些路径。新入口通过 MCP 传输临时源码和 JSON，无此要求。',
               '', '样本报告生成/检查工具需要相应原始捕获，仓库和 skill 不捆绑 Cisco 二进制、IDB、core 或大规模运行时转储。HTML 生成工具可能需要 `markdown-it-py`，文档检查可能需要 `beautifulsoup4`；主 MCP 入口和核心解析仅用标准库。',
               '', '## 已携带工具','', '| 脚本 | 用途 |','|---|---|']
    for path in tools:
        description=(ast.get_docstring(ast.parse(path.read_text(encoding='utf-8'))) or path.stem).splitlines()[0]
        catalogue.append('| `'+path.name+'` | '+description.replace('|','/')+' |')
    (SKILL/'references/script-catalogue.md').write_text('\n'.join(catalogue)+'\n',encoding='utf-8',newline='\n')
    generated={dest.relative_to(SKILL).as_posix():{'source':src.relative_to(ROOT).as_posix(),'source_sha256':sha(src),'sha256':sha(dest)}
               for src,dest in {**copies,**docs}.items()}
    manifest={'version':VERSION,'generated':generated,'notes':'Generated code/docs copies; edit canonical sources and rebuild. No IDA/MCP connection is made by this build.'}
    previous.write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8',newline='\n')
    files=sorted(p for p in SKILL.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc')
    destination=ROOT/'dist'/('iosd-analysis-skill-'+VERSION+'.zip');destination.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(destination,'w',zipfile.ZIP_DEFLATED) as archive:
        for path in files:archive.write(path,'iosd-analysis/'+path.relative_to(SKILL).as_posix())
    with zipfile.ZipFile(destination) as archive:
        assert archive.testzip() is None
        for path in files:assert hashlib.sha256(archive.read('iosd-analysis/'+path.relative_to(SKILL).as_posix())).hexdigest()==sha(path)
    return {'version':VERSION,'files':len(files),'archive':str(destination),'bytes':destination.stat().st_size}


if __name__=='__main__':print(json.dumps(assemble(),ensure_ascii=True))
