# iosd 未关联命令与配置子模式

此前六模式统计保留了 9,455 个已识别的终止定义候选，它们尚未归入 exec、configure、interface、subinterface、null-interface、line 的候选集合。本轮固定这批节点逐项调查，恢复额外模式入口、槽位与注册线索，再按不同证据模型生成路径。

样本为 C8000v IOS XE 26.01.02，MD5 `9eccfd46caadfff9c18557e2a446e19b`。模式调用来自 2026-10-30 新 IDB 的只读 ctree 采集；节点连接来自 2026-10-29 的历史页面。地址通过样本身份和 RVA 对齐。本轮读取范围为 saved IDB 与本地历史捕获，会话记录的 `process_state=0`；分析全程保持调试执行状态。

## 1 六个基础入口之外还有配置子模式

基础六模式由公共初始化函数创建。业务组件还会调用同一个 mode factory，提供名称、提示符、父模式和语法根。

已复核的工厂为 `0xDF3BC00`，底层分配器为 `0xDF3B9B0`。第 9 个参数保存到 112 字节模式对象的 `+0x50` 字段，作为语法根；第 1、2、6 个参数分别提供名称、提示符和父模式名称。

本轮采集 481 个直接调用者，取得 1,263 条 factory 调用记录，整理为 **1,220 条模式定义候选**：1,204 条已解析名称，1,205 条取得映像内语法根。按显式父模式名称可为 1,129 条定义找到 configure 祖先线索。相同名称、不同根和不同调用条件分别保留。

其中包括 `router`、`bgp-address-family`、`scope-address-family`、`qospolicymapclass`、`controller`、`ANCP` 等模式。某些模式名仍是变量，但已取得 `config-bs-dg`、`config-dp-group` 等提示符及显式父模式。名称字段保持未知，已有父模式证据仍可参与归类。

## 2 模式根可以从已有页面继续恢复

新增模式涉及 1,116 个不同语法根，其中 49 个已经在原节点图中。其余根大多位于之前捕获过的页面中，只是当时尚未作为调查入口。

复用原来 69 份捕获、校验 SHA256 和页面一致性后，额外解码 **29,580 个记录**。遇到原图节点时复用已有记录；未取得的页、零记录、未知 opcode 和描述符错误保持缺口。扩展中有 334 个未读或未分类记录，另保存缺页和前沿。

这解释了一类先前的关联缺口：模式入口尚未纳入种子集合，命令片段已经存在于已取得图中。补上入口后，可以沿历史页面中保存的连接恢复模式内路径。

## 3 固定候选集合的分类结果

下表是 9,455 个候选的首要解释分组，分组互斥；每个节点同时保留完整的模式与注册候选列表。

| 解释 | 终止候选数 | 取得的证据 |
|---|---:|---|
| 新增 config 模式入口 | **3,057** | 工厂定义及历史节点连接 |
| 已捕获槽位上的候选注册 | **3,556** | 同 key 槽位、片段与已复核安装语义 |
| 依赖静态槽位创建调用 | **1,479** | 初始化代码中的 create-link 调用，再连接候选注册片段 |
| 其他模式入口 | **13** | 已取得模式根；父模式关系另行保留 |
| 已取得注册片段，模式路径待补 | **928** | 注册 root/key 已取得，现有资料中的连接仍有缺口 |
| 历史 pending 片段，模式路径待补 | **92** | 捕获中的 pending 记录及相关片段 |
| 观察到绑定，模式路径待补 | **16** | 绑定证据存在，根到模式的链路仍待恢复 |
| 尚缺模式与注册路径 | **314** | 定义及其局部连接保留，入口关系未知 |

前四类共 **8,105 个**，已经生成模式内路径；其余 **1,350 个**保持未关联状态。13 个其他模式终点中，7 个属于 `filter`，另外 6 个位于 performance-measurement delay-profile 相关模式，带有配置提示符，显式父模式关系仍待补充。

928 个注册片段候选中，859 个的 key 创建点尚未出现在本次 mode-factory 调用者采集中；69 个已找到同 key 的静态创建调用，但模式路径仍有缺口。这是本次采集范围内的解释，其他调用者和间接创建路径继续保留。

## 4 三种 config 路径模型

### 历史连接模型

从静态 factory 提供的模式根出发，使用历史页面中的实际节点指针连接，恢复 **9,880 条路径见证**，覆盖 3,057 个终止节点。模式创建调用的执行条件、运行时模式对象和输入谓词仍按各自来源记录。

例如，`config-router` 中恢复了 `priority <number:0..127> <cr>`，handler RVA 为 `0xFC68900`、selector 为 19；`output-delay <number:8..50> <cr>` 对应 `0xE1F4590`、selector 0。具体协议上下文和路径条件保存在记录中。

QoS policy-map class 的部分路径经过 `dumper_command_func`、`sync_force_action` 等未知前缀，随后到达 `drop`、`fair-queue` 等关键词。未知前缀、回调和条件随路径保留。

### 已捕获槽位上的候选注册

按 key 匹配已捕获槽位和静态注册片段，为安装操作建立附带条件的候选边，恢复 **11,138 条路径见证**，覆盖 3,556 个终止节点。例如候选路径包含 `aqm-register-fnf <cr>`、`dial-control-mib retain-timer <number:0..35791> <cr>`。

type-1 安装按已复核消费者连接 slot anchor 与 fragment root；type-2 需要另外核对 sentinel 前置条件。槽位创建、安装顺序、调用者条件和目标状态保留为约束。

### 静态槽位创建模型

同一批函数中还取得 **1,084 条可解析的 create-link 调用**。通过 `0xDEF7BB0`、`0xDEF7D10`、`0xDEF7E60` 的 key、anchor 和类型参数，建立另一层条件候选。由此恢复 **4,622 条路径见证**，覆盖 1,479 个终止节点，例如 `atm svc-drain-count <number:1..500> <cr>`。

这些路径同时记录创建调用位置和安装候选。它们描述“创建槽位并满足安装与解析条件后的候选关系”。本轮没有执行创建接口、注册函数、谓词或 CLI handler。

三种 config 模型合计 **25,640 条见证、8,092 个不同终止候选**。另外为 13 个其他模式终点保存了 13 条路径。每个 EOL/局部跟踪上下文选择代表路径；其他写法与共享片段继续保存在节点图中。

初次搜索有一个根触及终止记录上限。提高该上限并重新计算后，最终 307 个“模式根/模型”组合均处理完本次模型发现的状态。前沿中的零记录、缺页和未知分支仍随文件保存。

## 5 查看结果

模式定义在 [parser-modes.json](../analysis/c8000v-26.01.02/parser-modes.json)，调查数据位于 [unbound-cli](../analysis/c8000v-26.01.02/unbound-cli/summary.json)。

```text
python tools/query_cli_catalogue.py analysis/c8000v-26.01.02/unbound-cli/observed_connections.jsonl.gz --mode router --contains "output-delay" --json
python tools/query_cli_catalogue.py analysis/c8000v-26.01.02/unbound-cli/conditional_registration_candidates.jsonl.gz --mode configure --limit 10 --json
python tools/query_cli_catalogue.py analysis/c8000v-26.01.02/unbound-cli/static_slot_creation_candidates.jsonl.gz --contains "atm svc" --limit 10 --json
```

| 文件 | 用途 |
|---|---|
| `terminals.jsonl.gz` | 全部 9,455 个候选的分类、模式、注册关联和未知项 |
| `extra-nodes.jsonl.gz` | 历史页面扩展出的节点语义与连接，包含未读记录 |
| `mode-coverage.json` | 每个模式的范围、配置祖先候选和三种图投影计数 |
| `observed_connections.jsonl.gz` | 历史连接模型的 config 路径 |
| `conditional_registration_candidates.jsonl.gz` | 已捕获槽位上的条件安装路径 |
| `static_slot_creation_candidates.jsonl.gz` | 还依赖静态槽位创建调用的路径 |
| `other_mode_connections.jsonl.gz` | 其余已识别模式中的路径 |
| `slots.json.gz` | 去除页面字节的历史槽位元数据 |
| `path-summary.json`、`path-frontiers.jsonl.gz` | 搜索范围、状态计数、缺口和限额 |
| `registration-gaps.json`、`static-link-gaps.json` | 未匹配 key、类型和 sentinel 前置条件缺口 |
| `diagnostics.json`、`manifest.json` | 剩余候选诊断、计数核对和来源摘要 |

## 6 可复用的方法

先固定原未关联节点集合，保留其 ID 和来源。入口恢复从 factory 消费者与调用参数展开；模式名、提示符、父模式、根及条件分别保存。使用父模式关系识别配置家族，名称字段未知时仍保留明确的父模式证据。

接着从同一捕获系列补取模式根，遇到已有节点即复用，缺失页另列。模式缺失、安装候选、槽位尚待创建和局部断链分别统计。静态创建调用与已观察槽位属于不同证据层，输出时分别标记。

`recover_parser_modes.py` 复用 `parser_modes` 解释调用 IR；`extend_saved_mode_roots.py` 复用运行时解码器补根；`analyze_unbound_cli.py` 进行候选分类；`recover_unbound_paths.py` 生成分模型路径；`finalize_cli_investigation.py` 核对固定集合、覆盖计数和摘要。各工具支持 `--help`。

MCP 采集复用 `ida_lifecycle.acquire_batch`，本轮按每批最多 8 个函数、约 4 秒预算串行执行；超时停止规则沿用会话机制。getter 扩展可以按任务关闭，空 ctree parent 保留为未知条件。个别遍历受限函数单独复核，早期不完整记录保留在本地证据中。

进入某个模式的 CLI 命令、创建调用的执行时机及条件状态，继续按对应 handler、注册者和消费者的证据关联。此处的 parent 是模式组织关系，路径按各自提示符和解析上下文展示。
