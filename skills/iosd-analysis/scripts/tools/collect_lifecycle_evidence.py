"""Collect checkpointed read-only registration IR from IDA, in short batches."""
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
    parser.add_argument("graph")
    parser.add_argument("--profile", default="profiles/lifecycle_api_26_01_02.json")
    parser.add_argument("--audit")
    parser.add_argument("--output", required=True)
    parser.add_argument("--functions", type=int, default=24, help="Additional functions this invocation")
    parser.add_argument("--batch-size", type=int, default=4)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--retry-errors",action="store_true",help="With --resume, retry failed functions and preserve previous failures")
    args = parser.parse_args()
    if not 1 <= args.functions <= 2000 or not 1 <= args.batch_size <= 32:
        parser.error("Invalid acquisition bounds")
    root = Path(__file__).resolve().parents[1]
    source = (root / "iosd_helper/ida_lifecycle.py").read_text(encoding="utf-8")
    profile = json.loads(Path(args.profile).read_text(encoding="utf-8"))
    output = Path(args.output).resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    if output.exists() and not args.resume:
        parser.error("Output exists; use --resume or a new output path")
    if args.retry_errors:
        if not args.resume or not output.exists():parser.error("--retry-errors requires an existing --resume checkpoint")
        old=json.loads(output.read_text(encoding="utf-8"))
        failed=[f for f in old["functions"] if f.get("error")]
        old.setdefault("failed_attempts",[]).extend(failed)
        old["functions"]=[f for f in old["functions"] if not f.get("error")]
        old["pending_functions"]=list(dict.fromkeys([f["rva"] for f in failed]+old["pending_functions"]))
        prepared=output.with_suffix(output.suffix+".tmp")
        prepared.write_text(json.dumps(old,ensure_ascii=False,indent=2),encoding="utf-8");prepared.replace(output)
    client = McpClient(args.url, timeout=20)
    client.initialize()
    completed = 0
    while completed < args.functions:
        key = "_iosd_lifecycle_" + uuid.uuid4().hex
        template = '''import types,json,zlib,base64,builtins
with open($graph,encoding="utf-8") as stream: graph=json.load(stream)
checkpoint=None
if $resume:
 with open($output,encoding="utf-8") as stream: checkpoint=json.load(stream)
audit=None
if $audit:
 with open($audit,encoding="utf-8") as stream: audit=json.load(stream)
module=types.ModuleType("_iosd_lifecycle_batch")
exec(compile($source,"<iosd-lifecycle-readonly>","exec"),module.__dict__)
result=module.acquire_batch(graph,$profile,checkpoint,audit,$batch,5)
packed=base64.b64encode(zlib.compress(json.dumps(result).encode())).decode()
setattr(builtins,$key,packed)
print(json.dumps({"chars":len(packed),"chunks":(len(packed)+7999)//8000,"last_batch":result["coverage"]["last_batch_functions"],"pending":len(result["pending_functions"])}))
'''
        code = Template(template).substitute(graph=repr(str(Path(args.graph).resolve())), resume=repr(output.exists()),
                                             output=repr(str(output)), audit=repr(str(Path(args.audit).resolve()) if args.audit else ""),
                                             source=repr(source), profile=repr(profile), batch=min(args.batch_size, args.functions-completed), key=repr(key))
        ast.parse(code)
        metadata = None
        committed = False
        try:
            metadata = json.loads(tool_result(client, code))
            if metadata["chunks"] > 8192:
                raise ValueError("Capture transfer bound")
            chunks = [tool_result(client, "import builtins\nprint(getattr(builtins,%r)[%d:%d])" %
                                  (key, index * 8000, (index + 1) * 8000)).strip() for index in range(metadata["chunks"])]
            packed = "".join(chunks)
            if len(packed) != metadata["chars"]:
                raise ValueError("Transfer length mismatch")
            capture = json.loads(zlib.decompress(base64.b64decode(packed)))
            capture["collector_source_sha256"] = hashlib.sha256(source.encode()).hexdigest()
            temporary = output.with_suffix(output.suffix + ".tmp")
            temporary.write_text(json.dumps(capture, ensure_ascii=False, indent=2), encoding="utf-8")
            temporary.replace(output)
            committed = True
            completed += metadata["last_batch"]
            print(json.dumps({"saved_functions":len(capture["functions"]),"pending":metadata["pending"]}),flush=True)
            if not metadata["last_batch"] or not metadata["pending"]:
                break
        finally:
            # A timed-out IDA request may still be running. Do not queue more
            # work, including cleanup, behind it. Keep the recovery key locally.
            if committed:
                tool_result(client, "import builtins\nif hasattr(builtins,%r): delattr(builtins,%r)" % (key, key))
            else:
                recovery = {"key":key,"reason":"batch response not received; no retry or cleanup request sent",
                            "last_committed_checkpoint":str(output),"target_execution":False,"transfer_metadata":metadata}
                output.with_suffix(output.suffix+".recovery.json").write_text(json.dumps(recovery,indent=2),encoding="utf-8")
    print("Saved", output)


if __name__ == "__main__":
    main()
