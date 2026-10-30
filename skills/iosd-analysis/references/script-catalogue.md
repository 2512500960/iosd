# 脚本目录

主入口 `scripts/iosd_mcp.py` 通过 MCP 采集；旧脚本继续复用现有算法。先运行所选脚本的 `--help`，只提供本次真实存在的输入。

## 常用路线

- 静态 CLI：`validate_ida_backend.py` → `export_cli_catalogue.py` / `recover_iosd_syntax.py` → `build_candidate_space.py`。旧 profile 校验不能跳过。
- 注册与状态：`audit_registration_triggers.py` → `collect_lifecycle_evidence.py` → `analyze_lifecycle.py`。ctree 采集与缓存文本导入的证据强度不同。
- 动态命令图：`probe_ida_debug_state.py` → `probe_runtime_mapping.py` → `capture_debugger_memory.py` / `collect_runtime_pages.py` → `export_runtime_grammar.py` → 选项与报告工具。
- core：`inspect_core.py`；与实时内存来源分开。
- 架构：`build_architecture_map.py`；NVGEN：`analyze_nvgen_bindings.py`；EHSA：`build_ehsa_report.py`。这些使用已保存的输入，不能用缺失的历史路径冒充实机结果。
- CDL：`walk_cdl.py`；作为独立数据源对照，不证明 iosd 命令完整。

## 执行边界

旧脚本在 `scripts/tools/`，核心在 `scripts/iosd_helper/`，profile 在 `scripts/profiles/`。部分默认相对路径以 scripts 为工作目录；使用绝对输入路径和显式 `--profile` 更便于跨目录运行。

旧批量采集器中有通过 IDA 主机文件系统读写 JSON 的实现，运行前核对客户端与 IDA 是否共享这些路径。新入口通过 MCP 传输临时源码和 JSON，无此要求。

样本报告生成/检查工具需要相应原始捕获，仓库和 skill 不捆绑 Cisco 二进制、IDB、core 或大规模运行时转储。HTML 生成工具可能需要 `markdown-it-py`，文档检查可能需要 `beautifulsoup4`；主 MCP 入口和核心解析仅用标准库。

## 已携带工具

| 脚本 | 用途 |
|---|---|
| `analyze_lifecycle.py` | Build generic registration/state dependency inventories from saved IR. |
| `analyze_nvgen_bindings.py` | Compare saved NVGEN descriptors and CLI terminals, without executing callbacks. |
| `analyze_vpdn.py` | Rebuild the pinned VPDN activation case from saved static evidence. |
| `audit_registration_triggers.py` | Read bounded direct-call ancestry of registration callers from a matching IDA. |
| `build_architecture_map.py` | Generate the saved initialization organization map; no IDA access. |
| `build_candidate_space.py` | Export the acquired definition pool independently of bounded path witnesses. |
| `build_config_refinement_report.py` | Compare saved config witnesses, separating new terminals from clearer syntax. |
| `build_ehsa_report.py` | Build a sample-bound EHSA evidence report from saved captures, without IDA. |
| `build_nvgen_report.py` | Build a local NVGEN evidence catalogue; no IDA or target connection. |
| `build_protocol_index.py` | Derive a portable subsystem search index from a reviewed saved architecture map. |
| `build_runtime_report.py` | Build a Chinese runtime/static comparison reader from saved evidence only. |
| `capture_debugger_memory.py` | Bounded, read-only paused debugger captures, guarded by image anchors. |
| `check_config_refinement.py` | Check saved refinement evidence, page closure, source hashes and local links. |
| `check_ehsa_evidence.py` | Verify EHSA evidence identities, table links, retained gaps and GOT range matches. |
| `check_nvgen_evidence.py` | Verify saved NVGEN descriptor links and evidence identities, not target behavior. |
| `check_option_analysis.py` | Verify retained option alternatives, unknown producers and conditional edges. |
| `check_vpdn_case.py` | Check exported VPDN paths against a fresh read-only IDA extraction. |
| `collect_action_evidence.py` | Read bounded action-consumer decompilations from the matching IDA database. |
| `collect_lifecycle_evidence.py` | Collect checkpointed read-only registration IR from IDA, in short batches. |
| `collect_runtime_linkage.py` | Collect reviewed runtime lists in bounded batches, preserving every frontier. |
| `collect_runtime_pages.py` | Read explicit image/heap pages in short batches for offline grammar export. |
| `expand_option_witnesses.py` | Replay a saved prefix, select each known option, and re-solve a bounded suffix. |
| `export_cli_catalogue.py` | Build a standalone searchable HTML inventory from a saved static CLI report. |
| `export_runtime_grammar.py` | Export observed runtime grammar, static comparison and unresolved frontiers. |
| `fill_runtime_frontiers.py` | Follow newly discovered missing grammar pages, retaining limits and failures. |
| `ida_mcp_client.py` | Small Streamable HTTP MCP client for local IDA validation (Python stdlib). |
| `import_cached_lifecycle.py` | Import saved decompilations as explicitly heuristic, offline lifecycle IR. |
| `inspect_core.py` | Inspect one candidate node outside IDA, useful for debugging parser logic. |
| `make_fixtures.py` | Generate a tiny ELF executable + matching core for IDA integration testing. |
| `probe_ida_debug_state.py` | Read IDA identity/base/debugger state only; never read target memory or pause. |
| `probe_runtime_mapping.py` | Compare saved immutable anchors with IDB and paused debugger bytes. |
| `project_worker.py` | CLI entry point for the packaged saved-evidence worker. |
| `read_ida_function.py` | Read a complete decompilation through bounded compressed MCP transfers. |
| `recover_iosd_syntax.py` | Recover mode-scoped syntax witnesses from a saved iosd static graph. |
| `validate_ida_backend.py` | Run current read-only extraction code in IDA via MCP and retrieve bounded chunks. |
| `walk_cdl.py` | Audit CDL and export bounded candidate paths, exact DAG counts and raw graph. |
