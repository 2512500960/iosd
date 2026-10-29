"""Readable evidence tables for the CDL walker's bounded output."""
import json
from .catalogue import inventory_html


def cdl_html(graph, report, records):
    paths = []
    for record in records:
        filters, agents, requests = set(), set(), set()
        for edge in record["edge_annotations"]:
            for alternative in edge["metadata_alternatives"]:
                for item in alternative:
                    attrs = item["attributes"]
                    if item["kind"] == "filter-ref":
                        filters.add(attrs.get("name", attrs.get("guid", "")))
                    if item["kind"] == "set" and attrs.get("param") == "BINOS-AGENT":
                        agents.add(attrs.get("value", ""))
                    if item["kind"] == "set" and attrs.get("param") == "BINOS-REQUEST":
                        requests.add(attrs.get("value", ""))
        paths.append({"syntax_candidate": record["syntax_candidate"], "eol_guid": record["eol_guid"],
                      "eol_name": record["eol_name"], "source": record["source"],
                      "agent_values": " | ".join(sorted(agents)), "request_values": " | ".join(sorted(requests)),
                      "filter_refs": " | ".join(sorted(filters)), "mode": record["mode"],
                      "node_guids": " → ".join(map(str, record["node_guids"])),
                      "edge_annotations": json.dumps(record["edge_annotations"], ensure_ascii=False)})
    branches = [{"root_guid": root["root_guid"], **branch} for root in report["roots"] for branch in root["branches"]]
    comparisons = [{"eol_name": row["eol_name"], "eol_guid": row["eol_guid"],
                    "exact_graph_paths": row["exact_explicit_edge_paths"],
                    "legacy_emitted_paths": row["legacy_algorithm_emulation"]["emitted_paths"],
                    "legacy_status": row["legacy_algorithm_emulation"]["stop_reason"]}
                   for row in report["legacy_comparison"]]
    requests = [{**row["attributes"]} for row in graph.requests]
    filters = [{"guid": node["guid"], "name": node["attributes"].get("name", ""),
                "macro": node["attributes"].get("macro", ""),
                "definition": json.dumps(node, ensure_ascii=False)}
               for node in graph.nodes.values() if node["kind"] == "filter"]
    labels = {"paths": "候选语法路径（示例／限量）", "branches": "顶层分支与精确图路径数",
              "legacy": "旧算法对照（模拟）", "requests": "请求与 bundle", "filters": "过滤器定义"}
    data = {"labels": labels, "identity_text": "输入 SHA-256: " + report["input"]["sha256"],
            "summary": {key: report[key] for key in ("node_types", "guid_nodes", "explicit_edges", "edges_with_metadata", "edge_metadata_types")},
            "coverage": {"roots": report["roots"], "conditions_evaluated": False,
                         "runtime_commands_confirmed": False},
            "tables": {"paths": paths, "branches": branches, "legacy": comparisons,
                       "requests": requests, "filters": filters}}
    return inventory_html(data, "BinOS CDL 遍历结果",
                          "候选语法来自 XML 的显式 edges，不代表设备上可执行的命令全集。图路径数量与命令条数不同；参数保留为占位符。已保留边上的 filter-ref、set 和 set-tdl；条件真值、字段覆盖关系及 CLI 模式尚未解释。大分支只输出每个 EOL 的示例与限量路径，完整图保存在 JSONL。",
                          "搜索覆盖当前类型的全部记录，每页 200 条；点击行查看详细字段。GUID 是 XML 标识，不能作为 IDA 地址。要查看 config 分支，可搜索 config hw-obfl 或 config sdm。dummy 为 XML 中的原始关键词，未作替换。")
