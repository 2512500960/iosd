# C8000v IOS XE 26.01.02：iosd 分析结果

这里保存一个特定 iosd 样本的结构说明、处理链索引和 CLI 派生元数据。阅读顺序可以从 [调试与分析教程](../../如何调试iosd.md) 开始，再结合 [架构图解](../../docs/iosd架构图解.html) 查看代码与运行机制。

## 样本与证据范围

| 项目 | 记录 |
|---|---|
| 文件 | `x86_64_crb_linux_iosd_vxe-universalk9-ms` |
| 平台与版本 | C8000v，IOS XE 26.01.02 |
| 架构 | ELF64，x86-64，小端 |
| 文件大小 | 938,319,552 字节 |
| MD5 | `9eccfd46caadfff9c18557e2a446e19b` |
| SHA256 | `d5e06304dff08dcf1dec0bc80b98df8e70ea78b546a6602c5f8c875e84bd3d99` |
| IDA | 9.1 |
| 历史捕获基址 | `0x555555554000` |
| CLI 页面采集 | 2026-10-29 14:27–17:15，北京时间，69 份捕获 |
| 本轮消费者复核与离线解释 | 2026-10-30 |

历史页面分批取得，结果记录跨批次时间范围。10 月 30 日的新 IDB 用于复核动作消费者；本轮保持目标运行，仅通过 saved IDB 读取函数。CLI 图仍来自上表的历史捕获系列。

## 文件怎样组织

ELF 包含 8,906 个节。其中 8,866 个 `.btrace*` 命名节合计约 5.54 MiB；代码、只读数据和可写数据构成主要文件占用。节和装载段帮助定位存储范围，业务组织继续由 subsystem、module、registry 和回调体现。具体数字及装载段见 [ELF 布局](../../profiles/elf_layout_26_01_02.json)。

本样本保存的 subsystem 元数据共有 5,692 条记录，记录中包含名称、类别、初始化及依赖线索。module 记录参与另一层初始化编排。协议处理由初始化登记、输入回调、队列和 task 等关系连接起来。完整讲解见 [文件结构与运行机制](../../docs/iosd从大ELF到运行机制.md)、[模块与子系统](../../docs/iosd模块与子系统.md) 与 [组件索引](../../docs/iosd组件索引与协议调查入口.md)。

## 已取得的处理链

| 主题 | 当前已经复核的内容 | 位置 |
|---|---|---|
| CDP | 接收登记、队列、IOS task、头/TLV 检查、邻居缓存 | [协议处理链](../../docs/iosd协议处理链与CLI新会话验证.md) |
| BGP | 消息类型和会话状态参与分发、UPDATE 局部入口 | [函数定位摘要](../../profiles/protocol_paths_26_01_02.json) |
| OSPF / UDP | OSPF 消息类型取得与处理，UDP 入队和通知局部关系 | [协议处理链](../../docs/iosd协议处理链与CLI新会话验证.md) |
| LLDP / IS-IS | 组件和名称线索，接收链中的未知关系 | [函数定位摘要](../../profiles/protocol_paths_26_01_02.json) |
| 配置生成 | CLI、NVGEN、hostname/description、接口缓存入口 | [NVGEN](../../docs/iosd的NVGEN与接口配置缓存.md) |
| 主备 | 心跳、超时、状态事件、EHSA 与平台边界 | [EHSA](../../docs/iosd的EHSA心跳与主备状态机.md) |
| 执行环境 | pthread、IOS task、调度及 level 的具体语境 | [线程与 level](../../docs/iosd的线程与level.md) |
| 调试信号与心跳 | 心跳任务、watchdog/hogcheck 接口、崩溃分支与信号现场记录 | [代码复核](../../docs/iosd调试信号与心跳.md) |

各处理链保留函数、RVA、调用或字段证据，以及外部绑定和中间数据流的待确认部分。设计意图中的推断在正文单独标明。

## CLI 恢复结果

源图含 **194,435 个节点、342,907 条原始边**。本轮复核 1,778 个节点，为其中 1,771 个补充动作解释，保留完整原图中的候选与未知项。路径目录共 **73,159 条见证、5,146 个不同 handler 地址**。

| 模式 | 路径见证 | 覆盖的不同 EOL | 不同 handler | 处理的符号状态 | 剩余未知/未读节点¹ |
|---|---:|---:|---:|---:|---:|
| exec | 25,423 | 9,234 | 3,430 | 204,987 | 344 |
| configure | 37,815 | 11,985 | 4,614 | 328,504 | 482 |
| interface | 4,806 | 1,702 | 554 | 32,314 | 77 |
| subinterface | 4,806 | 1,702 | 554 | 32,314 | 77 |
| null-interface | 11 | 5 | 5 | 80 | 2 |
| line | 298 | 103 | 31 | 1,588 | 15 |

¹ 未知节点统计沿用源图记录的模式成员关系；模式之间共用节点。interface 和 subinterface 在本样本共用根，业务差异还受上下文控制。

本次搜索对每个 EOL/跟踪上下文选择一条代表路径，六种模式均处理完模型发现的状态。目录中的条件保留符号形式，另有未知动作和零记录终止前沿。其他关键词组合和未激活片段继续保存在节点图与注册对照中。

### 本轮补充的内容

- general keyword 的文字、minimum-match、存储与 flags 线索。
- ORSET/ORTEST minimum-match 包装的状态条件与效果。
- 时间、带符号数、十六进制输入、动态数值范围和 URL 类参数。
- `*`、`,` 和 `test http` 等描述符字面文本，以及对应匹配条件。
- 流式路径生成、按条件查询和派生节点图导出。

例如，`service internal <cr>`、`no service internal <cr>` 和 `default service internal <cr>` 对应 handler RVA `0xDE9A730`、selector 20。其路径包含待解释谓词及上下文回调。时间参数出现在 `issu set rollback-timer <hh:mm:ss> <cr>` 等候选中；十六进制参数出现在 `device-tracking unit-test transport <hex-string> <cr>` 等候选中。这些是路径记录，可继续查看各自条件和缺口。

### 注册及剩余语义

历史静态注册对照共 4,564 条：2,302 条根在所选模式中条件连接，149 条观察到 pending，2,113 条在该捕获与模式范围内尚未观察到连接。节点图中保留 **66,827 个未归入这六个模式候选集合的节点**。

config 的 482 个未知/未读节点中，主要包括 64 位数值 50、slot/card 函数 37、IPv4/IPv6 地址 29、VRF RD 25、IPv6 zone 21、动态数值帮助 19。general keyword 仍有 7 个描述符缺页。共 3 个请求页在该历史捕获中缺失，地址和动作分布见 [缺口清单](cli/gaps.json)。通用 URL 辅助解析、general keyword 状态操作和更多协议专用参数继续保留符号约束。

## 查询和文件格式

在仓库根目录运行：

```text
python tools/query_cli_catalogue.py analysis/c8000v-26.01.02/cli/catalogue.jsonl.gz --mode configure --contains "service internal" --limit 10
python tools/query_cli_catalogue.py analysis/c8000v-26.01.02/cli/catalogue.jsonl.gz --mode configure --contains "<hh:mm" --limit 5 --json
```

| 文件 | 内容 |
|---|---|
| [summary.json](cli/summary.json) | 身份、时间、模式统计、源代码与输入摘要、产物 SHA256 |
| [catalogue.jsonl.gz](cli/catalogue.jsonl.gz) | 每行一个路径见证，包含参数、条件、效果、EOL、handler 和缺口 |
| [nodes.jsonl.gz](cli/nodes.jsonl.gz) | 全部已取得节点及 accept/alternate、动作语义、模式线索、未知项 |
| [registrations.json.gz](cli/registrations.json.gz) | 静态注册与历史运行时绑定对照 |
| [gaps.json](cli/gaps.json) | 剩余动作、缺页、模式前沿和解释范围 |

gzip 文件可用 Python 标准库读取。映像内引用带 `rva`，历史堆/外部引用带 `captured_runtime` 或 `*_captured_va`；节点中其他历史地址字段以采集基址和字段名解释。`selector_candidate`、字段偏移和数值常量保留整数含义。文件只保存派生分析元数据，原始 ELF、IDB、core 和页面字节留在本地。

方法和复现流程见 [CLI 挖掘方法](../../docs/iosd的CLI挖掘方法.md)，后续维护从 [iosd-analysis skill](../../skills/iosd-analysis/SKILL.md) 进入。
