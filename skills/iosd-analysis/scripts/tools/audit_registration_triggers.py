"""Read bounded direct-call ancestry of registration callers from a matching IDA.

Call-graph ancestry is evidence of a possible trigger relationship, not proof
that a command installs a table on a feasible execution path.
"""
import argparse
import ast
import base64
import hashlib
import json
from pathlib import Path
from string import Template
import uuid
import zlib

from ida_mcp_client import McpClient
from validate_ida_backend import tool_result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url")
    parser.add_argument("report", help="Graph JSON accessible at the same absolute path in IDA")
    parser.add_argument("--output", required=True)
    parser.add_argument("--depth", type=int, default=3)
    parser.add_argument("--max-functions", type=int, default=10000)
    parser.add_argument("--max-edges", type=int, default=50000)
    args = parser.parse_args()
    if not 1 <= args.depth <= 5 or not 1 <= args.max_functions <= 50000 or not 1 <= args.max_edges <= 200000:
        parser.error("Audit limits out of range")
    key = "_iosd_registration_audit_" + uuid.uuid4().hex
    source = Template('''import base64,json,zlib,builtins
from collections import deque
import ida_nalt,ida_funcs,ida_name,idautils,idc
with open($path,encoding="utf-8") as stream: report=json.load(stream)
if ida_nalt.retrieve_input_file_md5().hex()!=report["identity"]["input_md5"]: raise ValueError("Input MD5 mismatch")
if ida_nalt.get_imagebase()!=report["identity"]["imagebase"]: raise ValueError("Imagebase mismatch")
graph=report["graph"]
seeds=sorted({site["caller"] for row in graph["registrations"] for site in row.get("source_call_sites",[])})
handlers={row["handler_candidate"] for row in graph["nodes"] if row.get("handler_candidate") and row.get("handler_metadata")}
pending=deque((ea,0) for ea in seeds)
visited,edges,functions,limited_xrefs={},[],{},[]
seen_edges=set()
stop="completed_bounded_ancestry"
while pending:
 ea,depth=pending.popleft()
 if ea in visited: continue
 if len(visited)>=$max_functions:
  stop="function_limit";break
 visited[ea]=depth
 functions[ea]={"address":ea,"name":ida_name.get_name(ea),"known_cli_handler":ea in handlers}
 if depth>=$depth or ea in handlers: continue
 count=0
 for ref in idautils.XrefsTo(ea):
  mnemonic=idc.print_insn_mnem(ref.frm).lower()
  if mnemonic not in ("call","jmp") or idc.get_operand_value(ref.frm,0)!=ea: continue
  func=ida_funcs.get_func(ref.frm)
  if not func: continue
  count+=1
  if count>64:
   limited_xrefs.append(ea);break
  item=(func.start_ea,ea,ref.frm)
  if item not in seen_edges:
   if len(edges)>=$max_edges:
    stop="edge_limit";break
   seen_edges.add(item)
   edges.append({"caller":func.start_ea,"callee":ea,"callsite":ref.frm,"instruction":mnemonic})
  if func.start_ea not in visited: pending.append((func.start_ea,depth+1))
 if stop=="edge_limit":break
result={"identity":report["identity"],"registration_callers":seeds,"known_handlers":sorted(handlers),
 "functions":list(functions.values()),"call_edges":edges,"xref_limited_functions":limited_xrefs,
 "stop_reason":stop,"max_depth":$depth,"max_functions":$max_functions,"max_edges":$max_edges,
 "visited_functions":len(visited),"pending_functions":len(pending),"runtime_feasibility_verified":False,
 "scope":"Direct calls/tail jumps only; stop ancestry at known CLI handlers; indirect calls and dispatch are not resolved"}
payload=base64.b64encode(zlib.compress(json.dumps(result).encode())).decode()
setattr(builtins,$key,payload)
print(json.dumps({"chars":len(payload),"chunks":(len(payload)+7999)//8000,"functions":len(visited),"edges":len(edges),"stop":stop}))
''').substitute(path=repr(str(Path(args.report).resolve())), key=repr(key), depth=args.depth,
                  max_functions=args.max_functions, max_edges=args.max_edges)
    code = "import types\nmodule=types.ModuleType('_iosd_registration_audit')\nexec(%r,module.__dict__)\nresult=None" % source
    ast.parse(code)
    client = McpClient(args.url, timeout=60)
    client.initialize()
    try:
        metadata = json.loads(tool_result(client, code))
        print(json.dumps(metadata), flush=True)
        if metadata["chunks"] > 4096:
            raise ValueError("Audit transfer too large")
        parts = []
        for index in range(metadata["chunks"]):
            parts.append(tool_result(client, "import builtins\nprint(getattr(builtins,%r)[%d:%d])" %
                                     (key, index * 8000, (index + 1) * 8000)).strip())
        packed = "".join(parts)
        if len(packed) != metadata["chars"]:
            raise ValueError("Transfer length mismatch")
        result = json.loads(zlib.decompress(base64.b64decode(packed)))
        result["audit_source_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
        output = Path(args.output)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
        print("Saved", output, flush=True)
    finally:
        tool_result(client, "import builtins\nif hasattr(builtins,%r): delattr(builtins,%r)" % (key, key))


if __name__ == "__main__":
    main()
