"""Run current read-only extraction code in IDA via MCP and retrieve bounded chunks."""
import argparse
import ast
import base64
import hashlib
import json
from pathlib import Path
import uuid
import zlib
from string import Template

from ida_mcp_client import McpClient


def tool_result(client, code):
    result = client.send("tools/call", {"name": "py_eval", "arguments": {"code": code}})
    structured = result.get("structuredContent")
    if structured is None:
        structured = json.loads(result["content"][0]["text"])
    if structured.get('_output_truncated') and not result.get('isError'):
        structured=client.download_output(structured['_download_url'],structured['_output_id'])
    if result.get("isError") or structured.get("stderr") or structured.get("_output_truncated"):
        raise RuntimeError(json.dumps(structured, ensure_ascii=False)[:4000])
    return structured.get("stdout", "")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url")
    parser.add_argument("profile")
    parser.add_argument("output")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    names = ("memory", "locators", "structures", "option_tables", "grammar_semantics", "grammar_registry", "grammar", "ida_adapter")
    sources = [(name, (root / "iosd_helper" / (name + ".py")).read_text(encoding="utf-8")) for name in names]
    profile = json.loads(Path(args.profile).read_text(encoding="utf-8"))
    hashes = {name: hashlib.sha256(source.encode()).hexdigest() for name, source in sources}
    key = "_iosd_helper_extract_" + uuid.uuid4().hex
    code = '''import sys,types,json,uuid,zlib,base64,builtins
import ida_nalt
if ida_nalt.retrieve_input_file_md5().hex() != $expected_hash: raise RuntimeError("Input hash mismatch")
prefix="_iosd_readonly_"+uuid.uuid4().hex
pkg=types.ModuleType(prefix)
pkg.__path__=[]
sys.modules[prefix]=pkg
try:
    for name,source in $sources:
        module=types.ModuleType(prefix+"."+name)
        module.__package__=prefix
        sys.modules[module.__name__]=module
        exec(compile(source,"<readonly-validation-"+name+">","exec"),module.__dict__)
    adapter=sys.modules[prefix+".ida_adapter"]
    graph=adapter.extract_static_cli($profile)
    result={"identity":adapter.identity(),"source_sha256":$hashes,"graph":graph}
    payload=base64.b64encode(zlib.compress(json.dumps(result).encode())).decode()
    setattr(builtins,$key,payload)
    discovery=graph.get("discovery",{})
    summary={"summary":graph["summary"],"stop_reason":graph["stop_reason"],"registration_count":len(graph["registrations"]),"payload_chars":len(payload),"chunks":(len(payload)+7999)//8000,"discovery_calls":discovery.get("call_sites_seen"),"discovery_tables":len(discovery.get("tables",[])),"unresolved_calls":len(discovery.get("unresolved_call_sites",[]))}
    result=None
    print(json.dumps(summary))
finally:
    for name in list(sys.modules):
        if name==prefix or name.startswith(prefix+"."): del sys.modules[name]
'''
    # repr embeds values as Python data, not shell commands.
    code = Template(code).substitute(expected_hash=repr(profile["input_md5"]),
                                     sources=repr(sources), profile=repr(profile),
                                     hashes=repr(hashes), key=repr(key))
    ast.parse(code)
    client = McpClient(args.url, timeout=60)
    client.initialize()
    try:
        summary = json.loads(tool_result(client, code))
        print(json.dumps(summary, ensure_ascii=False), flush=True)
        if summary["chunks"] > 16384:
            raise ValueError("Extraction too large for bounded transfer")
        chunks = []
        for index in range(summary["chunks"]):
            start = index * 8000
            text = tool_result(client, "import builtins\nprint(getattr(builtins,%r)[%d:%d])" % (key, start, start + 8000))
            chunks.append(text.strip())
            if (index + 1) % 100 == 0:
                print("Transferred %d/%d chunks" % (index + 1, summary["chunks"]), flush=True)
        packed = "".join(chunks)
        if len(packed) != summary["payload_chars"]:
            raise ValueError("Chunk transfer length mismatch")
        output = json.loads(zlib.decompress(base64.b64decode(packed)))
        path = Path(args.output)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
        from sys import path as module_path
        module_path.insert(0, str(root))
        from iosd_helper.grammar import to_dot
        path.with_suffix(".dot").write_text(to_dot(output["graph"]), encoding="utf-8")
        print("Saved", path, flush=True)
    finally:
        tool_result(client, "import builtins\nif hasattr(builtins,%r): delattr(builtins,%r)" % (key, key))


if __name__ == "__main__":
    main()
