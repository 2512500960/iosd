"""Build the local iosd architecture guide reader from saved documentation."""
import argparse
import hashlib
from html import escape
import json
from pathlib import Path
import re

from markdown_it import MarkdownIt


def build(markdown_path, output_path):
    source = markdown_path.read_text(encoding="utf-8")
    parser = MarkdownIt("commonmark", {"html": True, "typographer": False}).enable("table")
    tokens = parser.parse(source)
    entries, used = [], set()
    current, subsection = "book", 0
    for index, token in enumerate(tokens):
        if token.type != "heading_open":
            continue
        title = tokens[index + 1].content
        if token.tag == "h1":
            anchor = "book-title"
        elif token.tag == "h2":
            chapter = re.match(r"(?:第(\d+)章|(\d+)\s)", title)
            appendix = re.match(r"附录([A-Z])", title)
            anchor = "ch%02d" % int(chapter.group(1) or chapter.group(2)) if chapter else (
                "appendix-" + appendix.group(1).lower() if appendix else "introduction")
            current, subsection = anchor, 0
            entries.append({"id": anchor, "title": title})
        else:
            subsection += 1
            anchor = current + "-s%02d" % subsection
        if anchor in used:
            raise ValueError("Duplicate heading identity: " + anchor)
        used.add(anchor)
        token.attrSet("id", anchor)
    # Partition at h2 boundaries so reader search filters complete chapters.
    boundaries = [i for i,t in enumerate(tokens) if t.type == "heading_open" and t.tag == "h2"]
    cover = parser.renderer.render(tokens[:boundaries[0]], parser.options, {})
    sections = []
    for number, begin in enumerate(boundaries):
        end = boundaries[number+1] if number+1<len(boundaries) else len(tokens)
        entry = entries[number]
        rendered = parser.renderer.render(tokens[begin:end], parser.options, {})
        sections.append('<section class="chapter" data-chapter="%s">%s</section>' % (entry["id"],rendered))
    navigation = "\n".join('<li data-nav="%s"><a href="#%s">%s</a></li>' %
                            (e["id"],e["id"],escape(e["title"])) for e in entries)
    html = TEMPLATE.replace("__NAVIGATION__",navigation).replace("__COVER__",cover).replace("__CHAPTERS__","\n".join(sections))
    html = html.replace("__SOURCE_FILENAME__",escape(markdown_path.name,quote=True))
    output_path.write_text(html,encoding="utf-8")
    sources = [markdown_path.parent.parent/"README.md", markdown_path.parent.parent/"iosd二进制文件结构描述.md",
               markdown_path.parent/"iosd模块与子系统.md",
               markdown_path.parent/"iosd的NVGEN与接口配置缓存.md",
               markdown_path.parent/"iosd的EHSA心跳与主备状态机.md",
               markdown_path.parent/"iosd的线程与level.md",
               markdown_path.parent/"整数显示与字节序.md",
               markdown_path.parent/"iosd架构与术语说明.md", markdown_path.parent/"通用注册分析与调试接入.md"]
    manifest = {"title":"iosd 程序架构与分析指南","as_of":"2026-10-29","input_md5":"9eccfd46caadfff9c18557e2a446e19b",
                "source":str(markdown_path.resolve()),"output":str(output_path.resolve()),
                "chapter_count":sum(bool(re.match(r"(?:第\d+章|\d+\s)",e["title"])) for e in entries),
                "appendix_count":sum(e["title"].startswith("附录") for e in entries),
                "headings":entries,"answer_blocks":source.count("<details>"),"source_characters":len(source),
                "handbook_sha256":hashlib.sha256(markdown_path.read_bytes()).hexdigest(),
                "source_documents_sha256":{str(p.resolve()):hashlib.sha256(p.read_bytes()).hexdigest() for p in sources},
                "ida_access":False,"mcp_access":False,"network_access":False,
                "note":"Architecture guide built from local documents; original evidence and errata remain linked. Building this reader does not access IDA."}
    output_path.with_suffix(".manifest.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding="utf-8")
    return manifest


TEMPLATE = '''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src 'unsafe-inline'; script-src 'unsafe-inline'; base-uri 'none'; form-action 'none'">
<title>iosd 程序架构与分析指南</title>
<style>
:root{--reading-size:18px;--bg:#f4f2ed;--paper:#fffefb;--text:#242e37;--muted:#5a6670;--border:#deded6;--accent:#135f6c;--code:#f0f3f3;--note:#eaf4f4}
:root[data-theme=dark]{--bg:#141b20;--paper:#1b252c;--text:#e5ecee;--muted:#a7b7bf;--border:#3a4a53;--accent:#82d2d8;--code:#24323b;--note:#20383e}
*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:90px}body{margin:0;background:var(--bg);color:var(--text);font-family:"Microsoft YaHei","PingFang SC",system-ui,sans-serif}
a{color:var(--accent);text-underline-offset:3px}button,input{font:inherit}button{cursor:pointer;border:1px solid var(--border);border-radius:7px;background:var(--paper);color:var(--text);padding:7px 11px}button:hover{border-color:var(--accent)}
aside{position:fixed;inset:0 auto 0 0;width:288px;overflow:auto;border-right:1px solid var(--border);background:var(--paper);padding:28px 18px;z-index:20}aside .label{font-size:12px;letter-spacing:.16em;color:var(--muted)}aside h2{font-size:21px;margin:8px 8px 18px}nav ol{list-style:none;padding:0;margin:0}nav a{display:block;font-size:14px;text-decoration:none;color:var(--text);padding:9px 10px;border-radius:6px;line-height:1.55}nav a:hover{background:var(--note)}aside footer{font-size:13px;color:var(--muted);line-height:1.8;padding:18px 10px}
.workspace{margin-left:288px}.toolbar{position:sticky;top:0;background:var(--paper);border-bottom:1px solid var(--border);padding:12px 24px;display:flex;align-items:center;gap:9px;flex-wrap:wrap;z-index:10}.toolbar input{min-width:180px;flex:1;max-width:520px;background:var(--bg);color:var(--text);border:1px solid var(--border);padding:9px 12px;border-radius:7px;font-size:14px}.toolbar #result-count{font-size:12px;color:var(--muted)}#menu{display:none}
main{max-width:1020px;margin:30px auto 80px;padding:0 36px}.cover,.chapter{background:var(--paper);border:1px solid var(--border);border-radius:12px;padding:42px 48px;margin:0 0 28px;box-shadow:0 5px 18px #00000004;font-size:var(--reading-size);line-height:1.95;overflow-wrap:anywhere}.cover{border-top:5px solid var(--accent)}.cover h1{font-size:2.1em;margin:0 0 8px;line-height:1.35}.cover>p:first-of-type{font-size:1.15em;color:var(--accent);margin-top:5px}.chapter h2{font-size:1.45em;line-height:1.55;border-bottom:1px solid var(--border);padding-bottom:15px;margin:0 0 26px}.chapter h3{font-size:1.1em;margin:32px 0 12px;color:var(--accent)}p{margin:16px 0}li{margin:8px 0}blockquote{margin:24px 0;padding:1px 18px;background:var(--note);border-left:4px solid var(--accent);font-size:.94em}pre{background:var(--code);border:1px solid var(--border);padding:18px 20px;border-radius:8px;overflow:auto;white-space:pre;line-height:1.7;font-size:.83em}code{font-family:Consolas,"SFMono-Regular",monospace;font-size:.87em;background:var(--code);border-radius:3px;padding:1px 4px}pre code{font-size:1em;background:none;padding:0}.table-wrap{overflow:auto;margin:24px 0}table{width:100%;border-collapse:collapse;font-size:.85em;line-height:1.8}th,td{text-align:left;vertical-align:top;padding:10px 12px;border:1px solid var(--border);min-width:90px}th{background:var(--note);font-weight:600}td code{white-space:normal}details{background:var(--note);border:1px solid var(--border);border-radius:8px;padding:12px 18px;margin:18px 0}summary{cursor:pointer;font-size:.93em;color:var(--accent);font-weight:600}details p{margin-bottom:6px}section[hidden],li[hidden]{display:none!important}.bottom-note{color:var(--muted);font-size:13px;text-align:center;line-height:1.8}.back-top{position:fixed;right:20px;bottom:18px;z-index:30}
@media(max-width:1100px){main{padding:0 22px}.cover,.chapter{padding:32px}}
@media(max-width:850px){aside{transform:translateX(-100%);box-shadow:5px 0 24px #0003;transition:transform .15s}body.nav-open aside{transform:translateX(0)}.workspace{margin-left:0}#menu{display:inline-block}.toolbar{padding:10px 12px;gap:6px}.toolbar #result-count{width:100%}main{margin-top:18px;padding:0 12px}.cover,.chapter{padding:24px 20px}.cover h1{font-size:1.7em}pre{padding:14px;font-size:.75em}.back-top{right:12px;bottom:12px}}
@media print{aside,.toolbar,.back-top,.bottom-note{display:none}.workspace{margin:0}main{max-width:none;margin:0;padding:0}.cover,.chapter{border:0;box-shadow:none;border-radius:0;padding:0;margin:0 0 30px;font-size:11pt;line-height:1.8}.chapter{break-before:page}section[hidden]{display:block!important}pre{white-space:pre-wrap}tr{break-inside:avoid}a{color:#222}h2,h3{break-after:avoid}}
</style></head><body>
<aside id="sidebar"><div class="label">IOSD HELPER · 程序架构</div><h2>阅读目录</h2><nav aria-label="主题目录"><ol>__NAVIGATION__</ol></nav><footer>2026 年 10 月 29 日整理<br>架构 · 初始化 · 接口 · 分析案例<br><a href="__SOURCE_FILENAME__">查看 Markdown 源稿</a></footer></aside>
<div class="workspace"><div class="toolbar"><button id="menu" aria-expanded="false">目录</button><input id="search" type="search" aria-label="按关键词筛选主题" placeholder="搜索架构、结构与接口"><button id="clear">全部主题</button><button id="smaller" aria-label="缩小字体">A−</button><button id="larger" aria-label="放大字体">A＋</button><button id="theme">深色</button><span id="result-count" role="status">按主题阅读，或搜索具体结构与接口。</span></div>
<main><header class="cover">__COVER__</header>__CHAPTERS__<p class="bottom-note">本页从项目架构指南生成，完全离线。全文定位可按 Ctrl＋F；筛选后点“全部主题”恢复。</p></main></div>
<button class="back-top" id="top">回到顶部 ↑</button>
<script>
'use strict';
const sections=Array.from(document.querySelectorAll('section.chapter'));
const navigation=Array.from(document.querySelectorAll('li[data-nav]'));
const search=document.getElementById('search');
const count=document.getElementById('result-count');
const root=document.documentElement;
let size=18;
function filterChapters(){const query=search.value.trim().toLowerCase();let matches=0;for(let i=0;i<sections.length;i++){const match=!query||sections[i].textContent.toLowerCase().includes(query);sections[i].hidden=!match;navigation[i].hidden=!match;if(match)matches++;}count.textContent=query?'找到 '+matches+' 个相关主题 / 共 '+sections.length+' 个主题与附录':'按主题阅读，或搜索具体结构与接口。';}
search.addEventListener('input',filterChapters);
document.getElementById('clear').addEventListener('click',()=>{search.value='';filterChapters();});
function resize(value){size=Math.max(14,Math.min(24,value));root.style.setProperty('--reading-size',size+'px');try{localStorage.setItem('iosd-handbook-size',String(size));}catch{}}
document.getElementById('smaller').addEventListener('click',()=>resize(size-1));
document.getElementById('larger').addEventListener('click',()=>resize(size+1));
const theme=document.getElementById('theme');
function setTheme(value){root.dataset.theme=value;theme.textContent=value==='dark'?'浅色':'深色';try{localStorage.setItem('iosd-handbook-theme',value);}catch{}}
theme.addEventListener('click',()=>setTheme(root.dataset.theme==='dark'?'light':'dark'));
document.getElementById('menu').addEventListener('click',()=>{const expanded=document.body.classList.toggle('nav-open');document.getElementById('menu').setAttribute('aria-expanded',String(expanded));});
document.getElementById('sidebar').addEventListener('click',event=>{if(event.target.closest('a'))document.body.classList.remove('nav-open');});
document.getElementById('top').addEventListener('click',()=>window.scrollTo({top:0,behavior:'smooth'}));
try{const saved=Number(localStorage.getItem('iosd-handbook-size'));if(Number.isFinite(saved)&&saved>=14&&saved<=24)resize(saved);const savedTheme=localStorage.getItem('iosd-handbook-theme');if(savedTheme==='dark')setTheme('dark');}catch{}
// Keep tables readable on narrow screens without shrinking the body text.
for(const table of document.querySelectorAll('table')){const wrapper=document.createElement('div');wrapper.className='table-wrap';table.parentNode.insertBefore(wrapper,table);wrapper.appendChild(table);}
</script></body></html>'''


def main():
    cli=argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--source",default="docs/iosd逆向分析教程.md")
    cli.add_argument("--output",default="docs/iosd逆向分析教程.html")
    args=cli.parse_args()
    result=build(Path(args.source),Path(args.output))
    print(json.dumps({key:result[key] for key in ("chapter_count","appendix_count","answer_blocks","source_characters","output")},ensure_ascii=False,indent=2))


if __name__=="__main__":main()
