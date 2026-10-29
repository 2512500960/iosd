"""Rebuild the pinned VPDN activation case from saved static evidence.

This exports reviewed dataflow facts and grammar projections. It does not infer
arbitrary binary lifecycles automatically or execute IOS/IDA target functions.
"""
import argparse
import hashlib
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from iosd_helper.catalogue import inventory_html
from iosd_helper.fragment_paths import enumerate_fragment
from iosd_helper.syntax_paths import number, registration_overlays


def read(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding="utf-8")


def jsonl(path, rows):
    with path.open("w", encoding="utf-8") as stream:
        for row in rows:
            stream.write(json.dumps(row, ensure_ascii=False) + "\n")


def merge_graph(base, supplement):
    graph = dict(base)
    nodes = {n["address"]: n for n in base["nodes"]}
    for node in supplement["nodes"]:
        if node["address"] in nodes and nodes[node["address"]].get("raw_hex") != node.get("raw_hex"):
            raise ValueError("Different acquired bytes at %#x" % node["address"])
        nodes.setdefault(node["address"], node)
    graph["nodes"] = list(nodes.values())
    regs = {r["address"]: r for r in base["registrations"]}
    for row in supplement["registrations"]:
        if row["address"] in regs and regs[row["address"]]["raw_hex"] != row["raw_hex"]:
            raise ValueError("Conflicting registration evidence")
        regs.setdefault(row["address"], row)
    graph["registrations"] = list(regs.values())
    graph["dynamic_link_definitions"] = supplement["dynamic_link_definitions"]
    return graph


def prefix_witness(paths, root):
    candidates = []
    for path in paths:
        tokens = []
        for edge in path["edge_trace"]:
            if edge["kind"] == "candidate_registration_installation" and edge["target"] == root:
                if "do-exec" not in tokens and not any(t in tokens for t in ("no", "default")):
                    candidates.append((len(path["gaps"]), len(tokens), path, list(tokens)))
                break
            if "token" in edge:
                tokens.append(edge["token"])
    if not candidates:
        raise ValueError("No cached native-mode prefix evidence for %#x" % root)
    _, _, path, tokens = min(candidates, key=lambda item: item[:2])
    return path, tokens


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("graph")
    parser.add_argument("--supplement", required=True)
    parser.add_argument("--config-paths", required=True)
    parser.add_argument("--evidence-dir", default="reports")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    project = Path(__file__).resolve().parents[1]
    facts_path = project / "profiles/vpdn_lifecycle_26_01_02.json"
    facts = read(facts_path)
    base, supplement = read(args.graph), read(args.supplement)
    for report in (base, supplement):
        identity = report["identity"]
        if identity["input_md5"] != facts["input_md5"] or identity["imagebase"] != facts["idb_imagebase"]:
            raise ValueError("VPDN case input identity mismatch")
    graph = merge_graph(base["graph"], supplement["graph"])
    evidence_dir, output = Path(args.evidence_dir), Path(args.output)
    output.mkdir(parents=True, exist_ok=True)

    test_witnesses_path = evidence_dir / "vpdn-exec-witnesses.json"
    mode_witnesses_path = evidence_dir / "vpdn-trace-exec-witnesses.json"
    trace_samples_path = evidence_dir / "vpdn-trace-samples.json"
    mode_witnesses = read(mode_witnesses_path)["paths"]
    test_prefix, prefix = prefix_witness(read(test_witnesses_path)["paths"], number(facts["test_fragment"]))
    fragment = enumerate_fragment(graph, facts["test_fragment"], prefix)
    if {p["handler"] for p in fragment["paths"]} != {number(facts["test_handler"])}:
        raise ValueError("Unexpected test fragment handler")
    commands = []
    for path in fragment["paths"]:
        selector = path["selector_candidate"]
        dispatch = "直接设置测试状态；有效 RADIUS code 集合另见条件表" if selector in (9, 10) else (
            "直接查找/重置对象" if selector == 13 else "消息 3855 → PID 38B15798 → worker 11DE26B0")
        commands.append({"mode": "exec", "syntax": path["syntax_candidate"], "selector": selector,
                         "handler": hex(path["handler"]), "dispatch": dispatch,
                         "status": "静态语法候选，实际注册/权限未验证", "proof": path})

    config_paths = []
    with Path(args.config_paths).open(encoding="utf-8") as stream:
        for line in stream:
            row = json.loads(line)
            if row["handler"] == number(facts["trigger_handler"]):
                config_paths.append(row)
    trace_rows, trace_proofs = [], []
    for sample in read(trace_samples_path):
        witness, tokens = prefix_witness(mode_witnesses, sample["parent_root"])
        trace_proofs.append({"parent_root": sample["parent_root"], "mode_prefix_witness": witness,
                             "bounded_enumeration": sample["enumeration_summary"]})
        for path in sample["examples"]:
            trace_rows.append({"mode": witness["mode"], "syntax": " ".join(tokens + [path["syntax_candidate"]]),
                               "handler": hex(path["handler"]), "status": "共享 SSS 片段候选示例；非 VPDN 专有",
                               "prefix_gaps": witness["gaps"], "proof": path})
    gates = [{"mode": p["mode"], "syntax": p["syntax_candidate"], "selector": p["selector_candidate"],
              "handler": hex(p["handler"]),
              "dependency": "触发/关闭启用状态" if p["selector_candidate"] == 28 else "E=0 时 handler 在分派前拒绝",
              "proof": p} for p in config_paths]
    definitions = [n for n in graph["nodes"] if n.get("handler_candidate") == number(facts["trigger_handler"])]
    jsonl(output / "test-paths.jsonl", fragment["paths"])
    jsonl(output / "test-frontiers.jsonl", fragment["frontiers"])
    jsonl(output / "config-handler-definitions.jsonl", definitions)
    jsonl(output / "config-path-witnesses.jsonl", config_paths)
    jsonl(output / "trace-examples.jsonl", trace_rows)
    write_json(output / "test-fragment.json", fragment)
    write_json(output / "reviewed-lifecycle.json", facts)
    write_json(output / "dynamic-link-definitions.json", graph["dynamic_link_definitions"])
    write_json(output / "supplement-graph.json", supplement)
    ida_profile = read(project / "profiles/static_cli_config_paths_26_01_02.json")
    extra_profile = read(project / "profiles/static_vpdn_supplement_26_01_02.json")
    ida_profile.update(name="Core modes plus reviewed VPDN dynamic linkage 26.01.02",
                       registration_tables=extra_profile["registration_tables"],
                       dynamic_link_definitions=extra_profile["dynamic_link_definitions"])
    write_json(output / "ida-profile.json", ida_profile)
    write_json(output / "prefix-witnesses.json", {"test": test_prefix, "trace": trace_proofs})

    code_evidence = {}
    for path in evidence_dir.glob("vpdn-*.json"):
        if path.stat().st_size > 2000000:
            continue
        value = read(path)
        if isinstance(value, dict) and "code" in value and "address" in value:
            if value.get("input_md5") != facts["input_md5"] or value.get("imagebase") != 0:
                raise ValueError("Function evidence identity mismatch: " + str(path))
            code_evidence[path.name] = value
    write_json(output / "function-evidence.json", code_evidence)
    support_names = ("trigger-vpdn_registration.json", "vpdn-state-xrefs.json", "vpdn-indirect-xrefs.json",
                     "vpdn-dynamic-slot-xrefs.json", "vpdn-slot-creator-xrefs.json", "vpdn-parent-slot-xrefs.json")
    support_files = [evidence_dir / name for name in support_names if (evidence_dir / name).exists()]
    write_json(output / "supporting-evidence.json", {p.name: read(p) for p in support_files})
    inputs = [Path(args.graph), Path(args.supplement), Path(args.config_paths), facts_path,
              test_witnesses_path, mode_witnesses_path, trace_samples_path] + support_files
    inputs.extend(evidence_dir / name for name in code_evidence)
    source_files = [project / name for name in ("iosd_helper/fragment_paths.py", "iosd_helper/syntax_paths.py",
                    "iosd_helper/grammar.py", "tools/analyze_vpdn.py")]
    manifest = {"identity": base["identity"], "test_enumeration": fragment["summary"],
                "merged_definition_counts": {"nodes": len(graph["nodes"]), "registrations": len(graph["registrations"]),
                                             "dynamic_slot_candidates": len(graph["dynamic_link_definitions"])},
                "test_templates": len(commands), "config_witnesses": len(gates),
                "trace_display_examples": len(trace_rows), "function_evidence_files": len(code_evidence),
                "input_sha256": {str(p.resolve()): hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs},
                "source_sha256": {str(p.relative_to(project)): hashlib.sha256(p.read_bytes()).hexdigest() for p in source_files},
                "scope": "Reviewed activation case; complete acquired test-fragment acyclic projection; shared trace examples only; no runtime verification"}
    write_json(output / "manifest.json", manifest)
    dynamic = [{"key": hex(s["key"]), "type": s["type"], "anchor": hex(s["root"]),
                "creator": hex(s["creator"]), "heap_address": "未知", "evidence": s["evidence"]}
               for s in graph["dynamic_link_definitions"]]
    overlay_graph = {**graph, "registrations": supplement["graph"]["registrations"]}
    overlays, unmatched, rejected = registration_overlays(overlay_graph, {n["address"]: n for n in graph["nodes"]})
    write_json(output / "supplement-binding-projection.json", {"edges": overlays, "unmatched": unmatched, "precondition_rejected": rejected})
    tables = {"commands": commands, "conditions": facts["transitions"], "states": facts["states"],
              "chains": facts["chains"], "dynamic": dynamic, "config": gates, "trace": trace_rows,
              "frontiers": [{"syntax_prefix": f["syntax_candidate"], "address": hex(f["address"]), "reason": f["reason"], "proof": f}
                            for f in fragment["frontiers"]], "gaps": [{"reason": s} for s in facts["gaps"]]}
    data = {"identity": base["identity"], "summary": manifest,
            "coverage": {"notes": facts["gaps"], "supported_radius_codes": facts["radius_codes"]},
            "labels": {"commands": "直接挂接：19 条 test 语法模板", "conditions": "满足什么条件，发生什么变化",
                       "states": "状态变量说明", "chains": "调用与间接注册证据链", "dynamic": "动态链接定义（堆地址未知）",
                       "config": "受启用状态约束的配置路径示例", "trace": "共享 subscriber 跟踪语法示例",
                       "frontiers": "test 片段未绑定／未读取分支", "gaps": "尚未证明的内容"},
            "hidden_columns": ["proof", "prefix_gaps"], "tables": tables}
    html = inventory_html(data, "VPDN：命令触发、动态链接与状态依赖",
        "当前样本中，(config)# vpdn enable 的 selector 28 在资源回调未否决后写入启用状态；首次测试初始化会尝试注册 EXEC 的 test vpn / test vpdn 片段。另一路通过共享 SSS 回调提交 subscriber 跟踪片段。下表先列 test 的 19 条模板，切换目录可看条件、配置命令、动态槽与未知分支。",
        "点击一行展开原始路径证据。<cr> 表示模型走到终结点；不是设备可执行性证明。完整静态定义在 supplement-graph.json 和原始图中保留，日期时间/循环等共享语法没有展开成命令全集。")
    card = '<div style="background:#fff;padding:16px;border:1px solid #d9e0eb;border-radius:6px;max-width:1100px">' \
           '<p><b>三件事分别看：</b>语法定义存在 → 链接槽安装成功 → handler/运行条件允许。启用状态 E、注册尝试标志 R 和 test 工作进程 PID 是不同状态。</p>' \
           '<p><b>关闭之后：</b>已审查的 no/default vpdn enable 分支只清 E，不复位 R/T，也没有注销测试片段。同一配置 handler 会因 E=0 拒绝其他 selector；test handler 没有同样的直接 E 检查，业务操作仍可能失败。</p>' \
           '<p><b>动态安装还可延后：</b>找不到槽时片段可进入待绑定表；后续创建槽后，parser 入口再重试。注册返回 1 也可能只是排队成功。</p>' \
           '<p><b>这次的覆盖：</b>test 片段 58 个地址、14 个 EOL、19 条无环投影路径；25 条边界路线保留，其中 24 条指向 IDB 未初始化地址，1 条为 parser stop。共享跟踪新增证据包含 9 个动态槽定义；示例不承担全集覆盖。</p></div>'
    html = html.replace('<div class="toolbar">', card + '<div class="toolbar">', 1)
    (output / "index.html").write_text(html, encoding="utf-8")
    print(json.dumps({key: manifest[key] for key in ("test_templates", "config_witnesses", "trace_display_examples", "merged_definition_counts", "function_evidence_files")}, ensure_ascii=False, indent=2))
    print("Saved", output.resolve())


if __name__ == "__main__":
    main()
