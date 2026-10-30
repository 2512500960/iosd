"""Bounded read-only runtime linked records and state probes, using typed RVAs."""
import uuid

from .memory import MemoryReadError, decode_pointer


def capture_runtime_linkage(memory, coordinates, module_ranges, specs, states=(), max_nodes=128,
                            session_guard=lambda: None):
    if not 1 <= max_nodes <= 10000:
        raise ValueError("Invalid runtime linkage bound")
    result = {"snapshot_id":uuid.uuid4().hex,"source":memory.source,"input_md5":coordinates.input_md5,
              "idb_base":coordinates.idb_base,"runtime_base":coordinates.runtime_base,
              "lists":[],"states":[],"errors":[],"atomic_snapshot":False,
              "consistency":"Caller guard and memory backend checked per read; resume/re-stop epoch is not tracked",
              "stop_reason":"completed_bounded_reads"}

    def read(ea,size):
        session_guard()
        return memory.read(ea,size)

    def reference(va):
        rva=va-coordinates.runtime_base
        if any(start<=rva<end for start,end in module_ranges):
            return {"space":"image","runtime_va":va,"rva":rva,"current_ea":coordinates.current_ea(rva)}
        return {"space":"runtime_only","runtime_va":va,"rva":None,"current_ea":None}

    try:
        # Probe small state values first, so a long list cannot consume their budget.
        for spec in states:
            size=spec.get("size",4)
            if not 1<=size<=32:raise ValueError("Invalid state probe size")
            row={"rva":spec["rva"],"runtime_va":coordinates.runtime_va(spec["rva"]),"semantic_name":spec.get("name","unclassified")}
            try:
                raw=read(row["runtime_va"],size);row.update(raw_hex=raw.hex(),value=int.from_bytes(raw,spec.get("encoding","big")))
            except MemoryReadError as exc:row["error"]=str(exc)
            result["states"].append(row)
        for spec in specs:
            head=coordinates.runtime_va(spec["head_rva"])
            chain={"name":spec["name"],"head_rva":spec["head_rva"],"head_va":head,"nodes":[],"frontiers":[]}
            result["lists"].append(chain)
            encoding=spec.get("pointer_encoding","swap_then_mask")
            size=spec["record_size"]
            if not 8<=size<=512:
                raise ValueError("Invalid runtime record size")
            for field in spec.get("fields",[]):
                if field["offset"]<0 or field["offset"]+field.get("size",8)>size:
                    raise ValueError("Runtime field outside record")
            try:
                raw_head=read(head,8)
                chain["head_raw_hex"]=raw_head.hex()
                current=decode_pointer(raw_head,encoding)
                if "start_runtime_va" in spec:
                    if spec.get("expected_head_raw_hex") != raw_head.hex():
                        raise ValueError("Continuation head changed; discard chain continuation")
                    current=spec["start_runtime_va"]
                    chain["continuation_start_va"]=current
            except MemoryReadError as exc:
                chain["frontiers"].append({"address":head,"reason":str(exc)});continue
            seen=set()
            while current:
                if current in seen:
                    chain["frontiers"].append({"address":current,"reason":"cycle"});break
                if len(seen)>=max_nodes:
                    chain["frontiers"].append({"address":current,"reason":"node_limit"});break
                seen.add(current)
                try:raw=read(current,size)
                except MemoryReadError as exc:
                    chain["frontiers"].append({"address":current,"reason":str(exc)});break
                node={"address":current,"address_space":"runtime_only","raw_hex":raw.hex(),"fields":{}}
                chain["nodes"].append(node)
                for field in spec.get("fields",[]):
                    chunk=raw[field["offset"]:field["offset"]+field.get("size",8)]
                    value=decode_pointer(chunk,encoding) if field.get("kind")=="pointer" else int.from_bytes(chunk,field.get("encoding","big"))
                    node["fields"][field["name"]]={"value":value,"raw_hex":chunk.hex(),
                                                   "reference":reference(value) if field.get("kind")=="pointer" and value else None}
                current=decode_pointer(raw[spec.get("next_offset",0):spec.get("next_offset",0)+8],encoding)
            chain["terminated_at_null"]=current==0
        session_guard()
    except ValueError as exc:
        result["stop_reason"]="session_or_layout_invalid"
        result["errors"].append(str(exc))
    return result
