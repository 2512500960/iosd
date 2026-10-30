# CLI 与状态依赖

建立所有取得的命令定义候选空间，恢复关键词、参数、条件、handler/selector 和注册关系。未知分支可能含有 undocumented command，不能因无法输出完整字符串就丢弃。

## 静态恢复

从已核对的 action registry、注册表和 mode root 出发，保存 accept/alternate、参数约束、谓词、EOL、动态 link、回调及未解析原始字段。命令字符串是图上的有界投影，不应替代原图。

复用 `grammar`、`grammar_semantics`、`syntax_paths`、`fragment_paths`、`option_tables`、`option_variants` 和 `candidate_space`。旧 `validate_ida_backend.py`、`export_cli_catalogue.py`、`recover_iosd_syntax.py` 对应这些功能；见 [脚本目录](script-catalogue.md)。

部分旧静态 profile 使用 capture base=0 的地址和 little-endian 布局。MD5 相同也不代表它们可直接作用于已 rebase、保存了不同编码字节的 IDB。保留校验；迁移时按地址字段含义转换，并核对原始记录及消费者。不能删校验或给所有整数加偏移。

CDL/XML 提供另一组命令线索，不是 iosd parser 的完整替代。CLI handler 和网络收包 handler 也不同。

当前细化支持 `generic_prefix_action`、`deprecated_action`、`whitespace_action`、general keyword、时间、带符号数、十六进制、动态数值和 URL 类参数。各动作按实际消费者的字段读取建立布局，动态帮助、范围、URL 辅助解析和未复核的状态操作保留约束。`keyword_orset_mm_action` / `keyword_ortest_mm_action` 包装复制后的字段与 minimum-match 也有单独处理。

关键词描述符可能包含 `*`、`,` 或 `test http`。保留完整字面文本、匹配单元、空白与 flags 条件；先检查是否受解码器的单词格式限制，再判断节点语义。新的 `keyword_literal` 规则接受可打印字面文本，异常内容仍保留到未知项。

保存图的增量流程为 `refine_cli_semantics.py` → `recover_saved_cli.py` → `export_cli_analysis.py`。细化器核对 MD5、已验证分发表函数和源页面 SHA256；路径按 EOL/上下文选择一条代表见证，优先较少未知步骤。节点图、条件、未绑定片段和搜索前沿一并保留。`query_cli_catalogue.py --json` 查看见证上的参数、条件、handler、selector 和缺口。

随 skill 的样本目录位于 `references/library/analysis/c8000v-26.01.02/cli/`。可先用 `scripts/tools/query_cli_catalogue.py` 查询它，再根据缺口安排 IDA 请求。2026-10-30 的离线细化解释了 1,771 个原未知节点，config 剩余 482 个；73,159 条记录表示六模式的路径见证。具体范围见 [版本结果](library/analysis/c8000v-26.01.02/README.md)，算法和输入见 [CLI 方法](library/docs/iosd的CLI挖掘方法.md)。

## 注册与状态

复用 `ida_lifecycle.acquire_batch` 采集调用、赋值和条件 IR，由 `lifecycle.analyze_lifecycle` 离线关联。API 角色由 profile 声明，不把 VPDN 特例写进通用推理。

保留：触发 handler/selector → 条件读取 → 状态写入 → 注册/槽写入 → 消费端 → 后续语法片段。分别区分晚注册、已注册但条件拒绝、隐藏帮助输出，以及状态变化与可达性的关系未证实。

历史 VPDN 的 `vpdn enable` 线索包含 selector 28、条件及一次性注册；这是经验模式，不代表每条 enable 都相同。`service internal` 同样需核对本样本的状态写入、谓词和注册变化，不能据公开描述直接判定延迟注册。

普通 write/read 不是解锁命令的证明；`write_may_affect_guard` 中的 may 必须保留。多个 selector 共用 handler 时，不能将函数内全部注册归给每个 selector。

## NVGEN

NVGEN 从各组件状态生成配置文本，可与 CLI 共享 handler，通过 NVGEN 标志、sense 和 selector 进入不同分支。根据节点绑定与消费者确认，不能将 NVGEN 分支当成另一条可输入命令。

接口缓存命中、失效和生成入口分别追踪。初始值、候选字段或单次快照不能证明当前启用状态和全部失效触发器。

详细资料：[通用注册分析](library/docs/通用注册分析与调试接入.md)、[选项与条件回调](library/docs/config关键词选项与条件回调.md)、[NVGEN 与接口缓存](library/docs/iosd的NVGEN与接口配置缓存.md)。
