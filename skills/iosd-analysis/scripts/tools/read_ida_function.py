"""Read a complete decompilation through bounded compressed MCP transfers."""
import argparse
import ast
import base64
import json
from pathlib import Path
import uuid
import zlib

from ida_mcp_client import McpClient
from validate_ida_backend import tool_result


def read_function(client, address, expected_md5):
    key = "_iosd_function_evidence_" + uuid.uuid4().hex
    source = '''import json,zlib,base64,builtins
import ida_nalt,ida_hexrays,ida_funcs,ida_name
digest=ida_nalt.retrieve_input_file_md5().hex()
if digest!=EXPECTED: raise ValueError("Input MD5 mismatch")
function=ida_funcs.get_func(ADDRESS)
if function is None or function.start_ea!=ADDRESS: raise ValueError("Not an IDA function entry")
cfunc=ida_hexrays.decompile(ADDRESS)
if cfunc is None: raise ValueError("Decompilation unavailable")
evidence={"input_md5":digest,"imagebase":ida_nalt.get_imagebase(),"address":ADDRESS,
 "name":ida_name.get_name(ADDRESS),"end":function.end_ea,"code":str(cfunc)}
packed=base64.b64encode(zlib.compress(json.dumps(evidence).encode())).decode()
setattr(builtins,KEY,packed)
print(json.dumps({"chars":len(packed),"chunks":(len(packed)+7999)//8000}))
'''.replace("EXPECTED", repr(expected_md5)).replace("ADDRESS", str(address)).replace("KEY", repr(key))
    code = "import types\nmodule=types.ModuleType('_iosd_function_evidence')\nexec(%r,module.__dict__)\nresult=None" % source
    ast.parse(code)
    committed = False
    try:
        metadata = json.loads(tool_result(client, code))
        if metadata["chunks"] > 4096:
            raise ValueError("Function evidence exceeds transfer bound")
        parts = []
        for index in range(metadata["chunks"]):
            parts.append(tool_result(client, "import builtins\nprint(getattr(builtins,%r)[%d:%d])" %
                                     (key, index * 8000, (index + 1) * 8000)).strip())
        packed = "".join(parts)
        if len(packed) != metadata["chars"]:
            raise ValueError("Transfer length mismatch")
        result = json.loads(zlib.decompress(base64.b64decode(packed)))
        committed = True
        return result
    finally:
        if committed:
            tool_result(client, "import builtins\nif hasattr(builtins,%r): delattr(builtins,%r)" % (key, key))
        # Timeout does not cancel server execution. Never queue cleanup/retry behind
        # an unresolved request; the transient transfer key may remain until IDA exits.


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url")
    parser.add_argument("address", type=lambda value: int(value, 0))
    parser.add_argument("--md5", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    client = McpClient(args.url)
    client.initialize()
    evidence = read_function(client, args.address, args.md5)
    path = Path(args.output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(evidence, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Saved %s: %s, %d characters" % (path, hex(args.address), len(evidence["code"])))


if __name__ == "__main__":
    main()
