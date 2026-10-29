"""Build an evidence-based organization map from explicit saved captures."""
from collections import Counter
from copy import deepcopy

from .catalogue import inventory_html


def build_architecture(static, modules, profile):
    identity = static["identity"]
    expected = profile["input_md5"].lower()
    if any(v.lower() != expected for v in (identity["input_md5"], modules["identity"]["input_md5"])):
        raise ValueError("Architecture evidence/profile binary mismatch")
    base = identity["imagebase"]
    module_base = modules["identity"]["imagebase"]
    steps = {s["name"]: s["result"] for s in static["steps"]}
    runs = steps["subsystem_candidates_all_encodings"]["runs"]
    selected = [run for run in runs if run["section"] == profile["subsystem_section"]
                and run["pointer_mode"] == profile["subsystem_pointer_mode"]]
    if len(selected) != 1:
        raise ValueError("Expected exactly one reviewed subsystem section/encoding run")
    subsystems = []
    for row in selected[0]["rows"]:
        raw = bytes.fromhex(row["raw_hex"])
        category = int.from_bytes(raw[40:42], "big") if len(raw) >= 42 else None
        subsystems.append({"name": row["name"], "record_rva": row["address"] - base,
                           "init_rva": row["init_candidate"] - base if row.get("init_candidate") else None,
                           "category_id": category, "category": profile["categories"].get(str(category), "unknown"),
                           "status": row["status"], "evidence": deepcopy(row)})
    headers = []
    metadata = modules["module_metadata"]
    for row in metadata["headers"]:
        first, second = row["field_10_candidate"], row["field_18_candidate"]
        headers.append({"name": row["name"], "record_rva": row["address"] - module_base,
                        "kind": "callback_node" if first else "group_node",
                        "init_rva": first - module_base if first else None,
                        "second_callback_rva": second - module_base if second else None,
                        "second_callback_semantics": "not_fully_reviewed", "evidence": deepcopy(row)})
    names = {row["record_rva"]: row["name"] for row in headers}
    links = []
    for row in metadata["links"]:
        a, b = row["endpoint_a"] - module_base, row["endpoint_b"] - module_base
        # No inferred edge to subsystems, categories or files.
        role = profile["module_link_roles"].get(hex(row["tag"]), "unknown")
        if a not in names or b not in names:
            role = "unknown"
        links.append({"record_rva": row["address"] - module_base, "a_rva": a, "b_rva": b,
                      "a": names.get(a, hex(a)), "b": names.get(b, hex(b)), "relation": role,
                      "evidence": deepcopy(row)})
    categories = [{"id": int(key), "name": name,
                   "candidate_records": sum(r["category_id"] == int(key) for r in subsystems)}
                  for key, name in profile["categories"].items()]
    return {"schema_version": 1, "kind": "iosd_architecture_map", "input_md5": expected,
            "address_space": "rva", "source_identities": [identity, modules["identity"]],
            "profile": deepcopy(profile), "subsystems": subsystems, "categories": categories,
            "modules": headers, "module_links": links,
            "summary": {"subsystem_candidate_records": len(subsystems), "module_headers": len(headers),
                        "module_links": len(links), "link_roles": dict(Counter(r["relation"] for r in links))},
            "limits": ["不是全量功能归属图；init 可达函数不自动归属该实体。",
                       "module 分组与 subsystem 类别分开；没有据同名词推断包含关系。",
                       "主 ELF/共享库归属和协议报文处理路径仍需独立核对。",
                       "原始扫描记录是候选；本图不证明初始化已在目标运行过。"]}


def architecture_html(model):
    def rva_display(row):
        return {key:(hex(value) if key.endswith("_rva") and isinstance(value,int) else value)
                for key,value in row.items()}
    tables = {"categories": model["categories"],
              "subsystems": [{**{k:v for k,v in row.items() if k != "evidence"},
                              "record_rva": hex(row["record_rva"]),
                              "init_rva": hex(row["init_rva"]) if row["init_rva"] is not None else None}
                             for row in model["subsystems"]],
              "modules": [rva_display(row) for row in model["modules"]],
              "module_links": [rva_display(row) for row in model["module_links"]]}
    return inventory_html({"identity": {"input_md5": model["input_md5"], "address_space":"rva"},
                           "summary": model["summary"], "coverage": {"limits": model["limits"]},
                           "labels": {"categories":"subsystem 类别", "subsystems":"subsystem 候选实体",
                                      "modules":"module 分组与回调节点", "module_links":"module 依赖与分组链接"},
                           "tables": tables}, "iosd 初始化组织地图",
                          "subsystem 和 module 是两套初始化机制。prerequisite 表示 A 的前置依赖包含 B；member_of 表示 A 归入 B 分组。图中没有自动建立 module 到 subsystem 的包含边。",
                          "地址使用 RVA；文件和协议处理归属尚未形成完整地图。结构与证据解释见 docs/iosd模块与子系统.md。")
