---
name: iosd-analysis
description: Investigate Cisco IOS XE iosd architecture, CLI definitions, protocol handlers and runtime state through IDA MCP or compatible analysis MCP tools, reusing evidence parsers and preserving unresolved branches. Supports saved IDB, paused debugger memory and ELF core evidence.
---

# iosd analysis

帮助研究人员从问题出发理解 iosd：组件怎样初始化、CLI 如何定义和注册、协议报文由谁处理、静态候选与运行时状态有什么差别。输出可追溯到字节、函数、RVA、引用及采集来源的解释，同时保留未知和不完整的分支。

这是通过 MCP 驱动的分析 skill，不需要加载 iosd Helper 的 IDA 界面插件。IDA 侧仍需启用提供工具的 MCP 服务。MCP 地址与服务名来自用户或宿主配置，不采用文档中的历史地址作为默认值。

## 开始调查

1. 根据用户问题选择下面的参考资料，先复用已有证据，再采集缺少的部分。
2. 如果用户正在 rebase、attach、批量运行脚本，处理本地材料，等用户确认 IDA 恢复后再发请求。不要自动连接旧地址或打开其他 IDB。
3. 发现实际 MCP 工具和 schema，确认选中的 IDA 实例。取得当前文件 MD5、处理器、位宽、字节序、imagebase、数据库路径和调试状态。新加载的干净 IDB 必须建立新会话，不能沿用旧报告里的 EA 或分析者重命名。
4. 用有界采集回答当前问题。优先使用已有的查询、反编译、字节和引用工具；需要结构化 ctree 或特定编码时，通过 MCP 执行随附的短采集脚本。将较大的解析、索引和报告生成放在 IDA 外部。

skill 可使用宿主已经连接的 MCP 工具；它不自行创建连接、凭据或权限。接口适配见 [MCP 与会话](references/mcp-and-session.md)。没有专用调试工具时，检查是否允许通过 `py_eval` 或等效接口调用 IDA 调试 API；不要将“没有独立工具名”解释成“不能读取调试数据”。

## 选择分析路线

| 用户想了解什么 | 按需阅读 |
|---|---|
| 顶层架构、模块与子系统、线程、初始化类别 | [架构与经验模式](references/architecture.md) |
| 隐藏命令、config 语法、参数、条件、handler、NVGEN | [CLI 与状态依赖](references/cli-and-registration.md) |
| 暂停内存、动态链接槽、待注册链表、共享库绑定或 core | [运行时与 core](references/runtime-and-core.md) |
| CDP、BGP 等协议的收包、解析和处理归属 | [协议调查](references/protocols.md) |
| 选择已有采集、解析、导出或报告脚本 | [脚本目录](references/script-catalogue.md) |

详细的历史分析文档在各参考页链接的 `references/library/` 中。它们记录的是特定样本上的证据及经验；不默认将函数地址、布局和推论推广到其他版本。按当前任务查阅，不一次载入整套文档。

需要先了解有哪些业务入口时，用 `scripts/iosd_mcp.py components --output <work>/components.json` 离线建立保存元数据的类别/词元目录。它保留同名记录和未知项，过滤只选择 ID，不创建组件包含或协议数据流关系。

## 使用随附入口

`scripts/iosd_mcp.py` 使用 Python 3.10+ 和标准库，通过 Streamable HTTP MCP 传输临时采集代码；IDA 主机无需看到客户端脚本路径。主入口需要 MCP 允许 `py_eval`，只使用类型化接口的 MCP 按参考页适配。

```text
python <skill>/scripts/iosd_mcp.py --url <mcp-url> discover --output <work>/capabilities.json
python <skill>/scripts/iosd_mcp.py --url <mcp-url> status --output <work>/session.json
python <skill>/scripts/iosd_mcp.py --url <mcp-url> protocol --session <work>/session.json --query cdp --output <work>/cdp.json
python <skill>/scripts/iosd_mcp.py --url <mcp-url> read --session <work>/session.json --request <work>/read.json --output <work>/memory.json
```

相对路径以实际工作目录为准；示例中的 `<skill>`、`<work>`、`<mcp-url>` 替换为本次环境中的位置。采集文件放在用户工作目录，不写进安装的 skill。完整参数、读取请求和 core 示例见对应参考页。已有解析器、profile 和脚本随 skill 携带；不要为了调用它们重新编写临时解析器。

## 证据规则

- 明确区分 saved IDB、暂停进程内存、core 和历史捕获。IDB 中保存的字节也可能来自以前的运行时快照，不能一概等同原始 ELF 文件。
- 映像内地址保存为有身份的 RVA；堆、外部 so、其他进程地址保留所属地址空间。用当前基址计算 EA，不对所有整数统一加 rebase 偏移。
- 按字段选择字节序和指针编码。当前样本的部分内部指针使用 big-endian 后清除 bit 63；ELF GOT 则使用原生 little-endian。不能对整个二进制统一交换。
- 输出分别标记“观察到的事实”“解释/候选”“未知”“下一步证据”。普通 xref、调用可达性、名称匹配与完整数据流证明不同；子系统类别也不等于模块包含或线程归属。
- 未注册、条件拒绝、尚未取得的节点、未知 opcode、间接目标、循环、深度/数量上限、未读页都保留。路径统计必须带范围；不得用静态候选总量宣称命令全部恢复，或用一次动态快照排除未激活命令。
- 经验模式应给出适用前提和验证办法。怀疑某条模式有研究价值时保留为假设，不因为它未完整解析就丢弃，也不自动升级为已确认实现。

## 采集与操作边界

默认执行本次问题所需的只读分析。不要为了验证可达性而执行 CLI handler、注册函数、谓词或 inferior 调用；也不自动暂停/继续、attach/rebase、修改目标内存或改写 IDB。用户明确授权相应操作时按其范围处理，不重复索要已给出的授权。

MCP 请求在同一 IDA 实例上串行执行，并与用户交互脚本协调。客户端超时不表示 IDA 已取消工作；停止后续请求，保留检查点和 pending 记录，确认 IDA 空闲后再恢复。随附入口只缓存 JSON 和临时源码模块，不安装 Hex-Rays/UI hooks，不跨请求持有 ctree 或 debugger 对象。

暂停状态不自动等于原子快照；说明采集时间段、模块映射、锚点及未追踪的 resume/re-stop 周期。缺页保持缺失，不补零；无法验证映射时先解决映射问题。

暂停链表与状态读取可使用主入口的 `linkage`，按 [运行时与 core](references/runtime-and-core.md) 设置独立锚点、profile 和小批次。协议研究可从 [已复核处理链](references/library/docs/iosd协议处理链与CLI新会话验证.md) 及随附定位摘要继续；保留每条关系的适用样本和未知边界。

报告结构与未知项记录见 [证据与输出](references/evidence.md)。
