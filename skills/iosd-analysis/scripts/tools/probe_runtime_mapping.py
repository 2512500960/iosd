"""Compare saved immutable anchors with IDB and paused debugger bytes."""
import argparse
import json
from pathlib import Path

from ida_mcp_client import McpClient
from validate_ida_backend import tool_result


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url")
    parser.add_argument("--anchors",required=True)
    parser.add_argument("--output",required=True)
    args=parser.parse_args()
    config=json.loads(Path(args.anchors).read_text(encoding="utf-8"))
    if not 1<=len(config["anchors"])<=8:raise ValueError("Anchor count outside 1..8")
    for row in config["anchors"]:
        if not 4<=len(bytes.fromhex(row["expected_hex"]))<=32:raise ValueError("Anchor size outside 4..32")
    source='''import json,ida_nalt,ida_dbg,ida_idd,ida_bytes,ida_segment
config=CONFIG
base=ida_nalt.get_imagebase()
digest=ida_nalt.retrieve_input_file_md5().hex()
if digest!=config["input_md5"]:raise ValueError("Input MD5 mismatch; no target memory read")
expected_base=config.get("expected_idb_base")
if expected_base is not None and base!=expected_base:raise ValueError("IDB base changed; no target memory read")
def guard():
 if ida_dbg.get_process_state()!=ida_dbg.DSTATE_SUSP:raise ValueError("Target not suspended; no further read")
 if ida_nalt.get_imagebase()!=base or ida_nalt.retrieve_input_file_md5().hex()!=digest:raise ValueError("IDA identity/base changed")
guard()
rows=[]
for anchor in config["anchors"]:
 rva=int(anchor["rva"],0) if isinstance(anchor["rva"],str) else anchor["rva"]
 ea=base+rva
 expected=bytes.fromhex(anchor["expected_hex"])
 guard()
 idb=ida_bytes.get_bytes(ea,len(expected),0)
 actual=ida_idd.dbg_read_memory(ea,len(expected))
 seg=ida_segment.getseg(ea)
 row={"name":anchor["name"],"rva":rva,"idb_ea":ea,"runtime_va_candidate":ea,
      "expected_hex":expected.hex(),"idb_hex":bytes(idb).hex() if idb is not None else None,
      "debugger_hex":bytes(actual).hex() if actual is not None else None,
      "idb_matches_expected":idb is not None and bytes(idb)==expected,
      "debugger_matches_expected":actual is not None and bytes(actual)==expected,
      "idb_segment":ida_segment.get_segm_name(seg) if seg else None}
 rows.append(row)
 if not row["debugger_matches_expected"]:break
guard()
result={"input_md5":digest,"idb_base":base,"runtime_base_candidate":base,
 "mapping_verified_at_anchors":len(rows)==len(config["anchors"]) and all(r["debugger_matches_expected"] and r["idb_matches_expected"] for r in rows),
 "anchors":rows,"target_execution_changed":False,"atomic_snapshot":False,
 "scope":"Local immutable anchor correspondence only; no whole-image/runtime identity proof"}
print(json.dumps(result))
'''.replace("CONFIG",repr(config))
    code="import types\nprobe_module=types.ModuleType('_iosd_mapping_probe')\nexec(%r,probe_module.__dict__)\nresult=None"%source
    client=McpClient(args.url,timeout=12);client.initialize()
    result=json.loads(tool_result(client,code))
    output=Path(args.output);output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding="utf-8")
    print(json.dumps({"idb_base":hex(result["idb_base"]),"verified":result["mapping_verified_at_anchors"],
                      "anchors":[{"name":r["name"],"rva":hex(r["rva"]),"idb":r["idb_matches_expected"],"runtime":r["debugger_matches_expected"]} for r in result["anchors"]]},indent=2))


if __name__=="__main__":main()
