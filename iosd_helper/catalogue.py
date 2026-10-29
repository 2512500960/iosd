"""Searchable static evidence inventories; never concatenate tokens into commands."""
import json
from html import escape


def hx(value):
    return hex(value) if value is not None else ""


def catalogue_rows(graph):
    nodes = graph["nodes"]
    selected = set(graph.get("selected_roots", []))
    return {
        "keywords": [{"address": hx(n["address"]), "keyword": n["keyword_candidate"],
                      "help": n.get("help_candidate", ""), "action": n.get("action_name", ""),
                      "opcode": n.get("opcode"), "descriptor": hx(n.get("payload"))}
                     for n in nodes if "keyword_candidate" in n],
        "terminals": [{"address": hx(n["address"]), "handler": hx(n.get("handler_candidate")),
                       "handler_name": (n.get("handler_metadata") or {}).get("name", ""),
                       "selector_candidate": n.get("selector_candidate"), "action": n.get("action_name", ""),
                       "descriptor": hx(n.get("payload")), "flags_raw_hex": n.get("command_flags_raw_hex", "")}
                      for n in nodes if n.get("semantic_role") in ("command_terminal", "combined_command_terminal")],
        "parameters": [{"address": hx(n["address"]), "parameter": n.get("display_label", ""),
                        "help": n.get("help_candidate", ""), "action": n.get("action_name", ""),
                        "descriptor": hx(n.get("payload")),
                        "details": json.dumps(n.get("parameter", {}), ensure_ascii=False)}
                       for n in nodes if n.get("semantic_role") in ("number_parameter", "string_parameter", "address_parameter", "combined_command_terminal")],
        "actions": [{"opcode": a["opcode"], "action": a["name"], "action_callback": hx(a["function"]),
                     "callback_missing_in_static_file": not bool(a["function"]), "address": hx(a["address"])}
                    for a in graph.get("action_registry", [])],
        "registrations": [{"address": hx(r["address"]), "table": hx(r["table"]),
                           "root": hx(r["root"]), "link_key": hx(r["link_key"]),
                           "owner_candidate": r.get("owner_candidate") or "", "selected": r["root"] in selected,
                           "conditions": " | ".join(r.get("conditions", []))}
                          for r in graph.get("registrations", [])],
        "gaps": [{"address": hx(n["address"]), "action": n.get("action_name", ""),
                  "reason": n.get("semantic_error", n.get("reason", n.get("semantic_status", ""))),
                  "descriptor": hx(n.get("payload")), "unparsed_text": n.get("keyword_text_unparsed", "")}
                 for n in nodes if n["status"] == "unresolved" or n.get("semantic_error") or
                 n.get("semantic_status") == "action registry mapped; payload semantics unresolved"],
        "unresolved_calls": [{"address": hx(r["call"]), "caller": hx(r["caller"]), "reason": r["reason"]}
                             for r in graph.get("discovery", {}).get("unresolved_call_sites", [])]
    }


def catalogue_html(report):
    graph = report["graph"]
    data = {"identity": report.get("identity", {}), "summary": graph.get("summary", {}),
            "coverage": graph.get("coverage", {}), "tables": catalogue_rows(graph)}
    return inventory_html(data, "iosd 静态 CLI 证据目录",
                          "这里列出静态关键词、参数、EOL 终结点和动作编号，不是已恢复的完整命令清单。关键词没有被直接拼接成命令；模式、权限、注册条件和未知动作仍需核对。动作编号 0–313 表示 parser 操作类型，并非同样数量的 CLI 命令。",
                          "点击行查看全部字段。地址为当前 IDB 地址，可复制后在 IDA 中按 G 跳转；搜索框过滤当前类型的所有记录。每页 200 条。")


def inventory_html(data, title, introduction, help_text):
    # Input strings remain text even if they contain HTML or a script closing tag.
    payload = json.dumps(data, ensure_ascii=False).replace("&", "\\u0026").replace("<", "\\u003c").replace(">", "\\u003e")
    return (HTML.replace("__TITLE__", escape(title)).replace("__INTRO__", escape(introduction))
            .replace("__HELP__", escape(help_text)).replace("__CATALOGUE_DATA__", payload))


HTML = '''<!doctype html>
<html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width">
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; script-src 'unsafe-inline'; style-src 'unsafe-inline'">
<title>__TITLE__</title>
<style>
body{font:15px/1.55 system-ui,sans-serif;background:#f4f6fa;color:#172337;margin:28px}
h1{font-size:26px;margin-bottom:8px}p{max-width:1100px}button,input,select{font:inherit;padding:8px;border:1px solid #b8c4d6;border-radius:5px;background:white}
input{min-width:340px}button{cursor:pointer}.toolbar{display:flex;gap:10px;flex-wrap:wrap;align-items:center;margin:20px 0 12px}
.scroll{overflow:auto;background:white;border:1px solid #d9e0eb;border-radius:6px;max-height:66vh}
table{border-collapse:collapse;white-space:nowrap;width:100%;font-size:13px}td,th{text-align:left;padding:9px 12px;border-bottom:1px solid #e6eaf0;max-width:650px;overflow:hidden;text-overflow:ellipsis}th{position:sticky;top:0;background:#eaf0f9}td{font-family:ui-monospace,monospace}#count{margin-left:auto}summary{cursor:pointer}pre{white-space:pre-wrap}#details{background:#fff;padding:12px;border:1px solid #d9e0eb}tr:hover{background:#f0f5ff}
</style>
<h1>__TITLE__</h1>
<p>__INTRO__</p>
<p id="identity"></p>
<details><summary>覆盖范围与未解析数量</summary><pre id="coverage"></pre></details>
<div class="toolbar"><select id="kind" aria-label="目录类型"></select><input id="query" type="search" placeholder="搜索文本、标识或字段值" aria-label="搜索"><button id="prev">上一页</button><button id="next">下一页</button><span id="count"></span></div>
<div class="scroll"><table><thead id="head"></thead><tbody id="body"></tbody></table></div>
<p>__HELP__</p>
<pre id="details">选择一行查看字段。</pre>
<script id="catalogue-data" type="application/json">__CATALOGUE_DATA__</script>
<script>
'use strict';
const data=JSON.parse(document.getElementById('catalogue-data').textContent);
const el=id=>document.getElementById(id);
const labels=data.labels||{keywords:'关键词节点',terminals:'EOL 终结点 / handler',parameters:'参数节点',actions:'parser 动作编号',registrations:'注册记录',gaps:'未解析节点 / 载荷',unresolved_calls:'未解析注册调用'};
for(const [value,label] of Object.entries(labels)){const option=document.createElement('option');option.value=value;option.textContent=label+' ('+data.tables[value].length+')';el('kind').append(option);}
el('identity').textContent=data.identity_text||('MD5: '+(data.identity.input_md5||'unknown')+' | IDA: '+(data.identity.ida_version||'unknown'));
el('coverage').textContent=JSON.stringify({summary:data.summary,coverage:data.coverage},null,2);
let page=0,filtered=[],columns=[];const size=200;
function render(){el('head').replaceChildren();el('body').replaceChildren();const header=document.createElement('tr');for(const key of columns){const th=document.createElement('th');th.textContent=key;header.append(th);}el('head').append(header);
for(const row of filtered.slice(page*size,(page+1)*size)){const tr=document.createElement('tr');for(const key of columns){const td=document.createElement('td');td.textContent=String(row[key]??'');tr.append(td);}tr.onclick=()=>{el('details').textContent=JSON.stringify(row,null,2);};el('body').append(tr);}
el('count').textContent=filtered.length+' 条 / 第 '+(page+1)+' 页，共 '+Math.max(1,Math.ceil(filtered.length/size))+' 页';el('prev').disabled=page===0;el('next').disabled=(page+1)*size>=filtered.length;}
function filter(){page=0;const rows=data.tables[el('kind').value];columns=rows.length?Object.keys(rows[0]).filter(key=>!(data.hidden_columns||[]).includes(key)):[];const q=el('query').value.toLowerCase().trim();filtered=q?rows.filter(row=>Object.values(row).some(value=>String(value??'').toLowerCase().includes(q))):rows;el('details').textContent='选择一行查看字段。';render();}
let timer;el('query').oninput=()=>{clearTimeout(timer);timer=setTimeout(filter,150);};el('kind').onchange=filter;el('prev').onclick=()=>{if(page>0){--page;render();}};el('next').onclick=()=>{if((page+1)*size<filtered.length){++page;render();}};filter();
</script></html>'''
