"""Import saved decompilations as explicitly heuristic, offline lifecycle IR."""
import argparse
import json
from pathlib import Path
import sys

sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from iosd_helper.cached_ir import lower_cached_function


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("graph")
    parser.add_argument("--evidence-dir",default="reports")
    parser.add_argument("--audit")
    parser.add_argument("--profile",default="profiles/lifecycle_api_26_01_02.json")
    parser.add_argument("--api-capture",help="Optional checkpoint with fresh API references, even if some functions failed")
    parser.add_argument("--output",required=True)
    args=parser.parse_args()
    graph=json.loads(Path(args.graph).read_text(encoding="utf-8"));identity=graph["identity"]
    functions,skipped={},[]
    for path in sorted(Path(args.evidence_dir).glob("*.json")):
        if path.stat().st_size>2*1024*1024:continue
        try:value=json.loads(path.read_text(encoding="utf-8"))
        except (ValueError,OSError):continue
        if not isinstance(value,dict):continue
        candidates=[value,value.get("structuredContent",{}),value.get("result",{}).get("structuredContent",{}) if isinstance(value.get("result"),dict) else {}]
        for item in candidates:
            if not isinstance(item,dict) or not isinstance(item.get("code"),str):continue
            address=item.get("address",item.get("addr"))
            if address is None:continue
            address=int(address,0) if isinstance(address,str) else address
            digest=item.get("input_md5",value.get("identity",{}).get("input_md5"))
            if digest and digest!=identity["input_md5"]:
                skipped.append({"file":str(path),"reason":"cached MD5 mismatch"});continue
            evidence={**item,"address":address,"imagebase":item.get("imagebase",identity["imagebase"]),
                      "identity_verified":digest==identity["input_md5"],"source_file":str(path),
                      "_output_truncated":bool(item.get("_output_truncated") or value.get("_output_truncated") or value.get("result",{}).get("_output_truncated") if isinstance(value.get("result",{}),dict) else item.get("_output_truncated"))}
            previous=functions.get(address)
            quality=(evidence["identity_verified"],not item.get("_output_truncated",False),len(item["code"]))
            if previous is None or quality>previous[0]:functions[address]=(quality,evidence)
    result={"schema_version":1,"identity":identity,"functions":[lower_cached_function(e) for _,e in functions.values()],
            "api_xrefs":[],"call_edges":[],"pending_functions":[],"unknown_inputs":skipped,
            "coverage":{"source":"cached decompilation text, heuristic expression subset",
                        "identity_verified_functions":sum(e["identity_verified"] for _,e in functions.values()),
                        "identity_unverified_functions":sum(not e["identity_verified"] for _,e in functions.values()),
                        "scope":"Only acquired cached functions; no IDA requests or target execution","runtime_read":False}}
    if args.audit:
        audit=json.loads(Path(args.audit).read_text(encoding="utf-8"))
        if audit["identity"]["input_md5"]!=identity["input_md5"]:raise ValueError("Audit identity mismatch")
        base=audit["identity"]["imagebase"]
        result["call_edges"]=[{"caller":e["caller"]-base,"callee":e["callee"]-base,"site_rva":e["callsite"]-base} for e in audit["call_edges"]]
        captured={f["rva"] for f in result["functions"]}
        result["pending_functions"]=sorted({f["address"]-base for f in audit.get("functions",[])}-captured)
    profile=json.loads(Path(args.profile).read_text(encoding="utf-8"))
    if profile["input_md5"]!=identity["input_md5"]:raise ValueError("API profile input mismatch")
    table_api=next(int(a["rva"],0) if isinstance(a["rva"],str) else a["rva"] for a in profile["apis"] if a["role"]=="register_table")
    unique=set()
    for row in graph["graph"]["registrations"]:
        for site in row.get("source_call_sites",[]):
            key=site["caller"]-identity["imagebase"],site["call"]-identity["imagebase"]
            if key not in unique:
                unique.add(key);result["api_xrefs"].append({"caller":key[0],"callee":table_api,"site_rva":key[1]})
    if args.api_capture:
        fresh=json.loads(Path(args.api_capture).read_text(encoding="utf-8"))
        if fresh["identity"]["input_md5"]!=identity["input_md5"]:raise ValueError("API capture input mismatch")
        seen={(r["caller"],r["callee"],r["site_rva"]) for r in result["api_xrefs"]}
        result["api_xrefs"].extend(r for r in fresh.get("api_xrefs",[]) if (r["caller"],r["callee"],r["site_rva"]) not in seen)
        result["call_edges"].extend(fresh.get("api_xrefs",[]))
        result["xref_limits"]=fresh.get("xref_limits",[])
        result["unknown_inputs"].extend({"function":f["rva"],"reason":"structured capture failed: "+f["error"]} for f in fresh.get("functions",[]) if f.get("error"))
        captured={f["rva"] for f in result["functions"]}
        result["pending_functions"]=sorted((set(result["pending_functions"])|set(fresh.get("pending_functions",[])))-captured)
        result["coverage"]["fresh_api_capture"]=args.api_capture
    output=Path(args.output);output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding="utf-8")
    print(json.dumps({"functions":len(result["functions"]),"coverage":result["coverage"]},ensure_ascii=False,indent=2))


if __name__=="__main__":main()
