"""Show a saved partial graph in the matching IDA via MCP without editing the IDB."""
import argparse
import ast
import base64
import json
from pathlib import Path
from string import Template
import zlib

from ida_mcp_client import McpClient
from validate_ida_backend import tool_result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url")
    parser.add_argument("report")
    parser.add_argument("--limit", type=int, default=400)
    args = parser.parse_args()
    if not 1 <= args.limit <= 400:
        parser.error("Preview limit must be between 1 and 400")
    root = Path(__file__).resolve().parents[1]
    report = json.loads(Path(args.report).read_text(encoding="utf-8"))
    graph = report["graph"]
    nodes = graph["nodes"][:args.limit]
    addresses = {row["address"] for row in nodes}
    preview = {"nodes": nodes, "edges": [edge for edge in graph["edges"] if edge["source"] in addresses]}
    packed = base64.b64encode(zlib.compress(json.dumps(preview).encode())).decode()
    source = (root / "iosd_helper" / "graph_view.py").read_text(encoding="utf-8")
    code = Template('''import builtins,types,json,zlib,base64
import ida_nalt
if ida_nalt.retrieve_input_file_md5().hex() != $digest: raise RuntimeError("Input hash mismatch")
if ida_nalt.get_imagebase() != $imagebase: raise RuntimeError("IDB imagebase mismatch")
module=types.ModuleType("_iosd_helper_graph_preview")
exec($source,module.__dict__)
exec("def evidence(row,ea):\\n import json,ida_kernwin,ida_segment\\n ida_kernwin.msg('[iosd-helper] Evidence: '+json.dumps(row,ensure_ascii=False,indent=2)+'\\\\n')\\n if ida_segment.getseg(ea): ida_kernwin.jumpto(ea)\\n",module.__dict__)
previous=getattr(builtins,"_iosd_helper_static_graph_preview",None)
if previous is not None: previous.Close()
graph=json.loads(zlib.decompress(base64.b64decode($packed)))
viewer=module.StaticParserGraph("iosd Helper 0.3.0 | Partial static CLI preview",graph,module.evidence)
builtins._iosd_helper_static_graph_preview=viewer
print(json.dumps({"graph_show_return":bool(viewer.Show()),"visible_nodes":len(graph["nodes"]),"edges":len(graph["edges"])}))
result=None
''').substitute(digest=repr(report["identity"]["input_md5"]), imagebase=repr(report["identity"]["imagebase"]),
                  source=repr(source), packed=repr(packed))
    ast.parse(code)
    client = McpClient(args.url)
    client.initialize()
    print(tool_result(client, code))


if __name__ == "__main__":
    main()
