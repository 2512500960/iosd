# iosd analysis skill

通过 MCP 辅助安全研究人员理解 Cisco IOS XE 的 iosd 大二进制：初始化组织、CLI 定义与条件、动态注册、协议处理入口、NVGEN、EHSA 和线程。复用已有分析代码与文档，保留未知、不完整、未注册及未取得的分支。

仓库围绕三个入口组织：

| 入口 | 内容 |
|---|---|
| [主教程：如何调试 iosd](如何调试iosd.md) | 环境准备、调试流程、程序结构和分析路线；后续在这个文件继续维护 |
| [iosd-analysis skill](skills/iosd-analysis/SKILL.md) | 通过 MCP 调用 IDA 的调查流程、解析核心和按需参考知识 |
| [C8000v 26.01.02 分析结果](analysis/c8000v-26.01.02/README.md) | 一个特定版本的结构说明、协议处理链、CLI 目录、节点图及覆盖范围 |

IDA 侧运行 MCP 服务，AI 客户端连接该服务。skill 组织调查与解释，Python 核心负责确定性解析，MCP 提供当前 IDB 和调试数据。

想先读懂这个大 ELF，可直接打开 [iosd 架构图解](docs/iosd架构图解.html) 或 [配套正文](docs/iosd从大ELF到运行机制.md)。八张图分别解释文件构成、四种结构视角、启动机制、登记与消费、CDP、CLI/NVGEN、线程/task 和 EHSA。支持离线搜索、主题筛选与隐藏地址细节；无需连接 IDA。图和解释区分示意、样本局部证据及未知边界。

## 安装与使用

将整个 `skills/iosd-analysis` 文件夹复制到客户端支持的 skills 目录，保持 `SKILL.md`、`references`、`scripts` 和 `agents` 的相对位置。也可由支持从仓库安装 skill 的客户端安装这个子目录。MCP 连接按客户端配置，地址不写死在 skill 中。

例如向支持该 skill 的客户端提出：

> 使用 $iosd-analysis，分析当前 iosd 的 CDP 报文处理入口，关联子系统、注册回调和解析函数，保留未知分支。

或者：

> 使用 $iosd-analysis，对照静态 CLI 定义和暂停进程中的链接槽，解释 config 模式下哪些命令受状态影响。

附带的 HTTP MCP 入口使用 Python 3.10+ 和标准库：

```text
python skills/iosd-analysis/scripts/iosd_mcp.py --url <mcp-url> discover --output <work>/capabilities.json
python skills/iosd-analysis/scripts/iosd_mcp.py --url <mcp-url> status --output <work>/session.json
python skills/iosd-analysis/scripts/iosd_mcp.py --url <mcp-url> protocol --session <work>/session.json --query cdp --output <work>/cdp.json
```

替换 `<mcp-url>` 和 `<work>`。也可用 `IOSD_IDA_MCP_URL` 配置地址。这个入口需要服务提供 `py_eval`；对于其他 MCP 的类型化接口，skill 会先发现能力再按实际 schema 使用。详细参数见 `--help` 和 [MCP 会话说明](skills/iosd-analysis/references/mcp-and-session.md)。

## 静态与运行时

| 数据源 | 能做什么 | 边界 |
|---|---|---|
| saved IDB | 字节、函数、引用、组织与语法候选 | 保存字节可能来自过去的运行时，不保证等同原始 ELF |
| 已暂停的调试进程 | 动态槽、链表、堆节点、状态及实际库绑定 | 核对身份、运行时基址、不变锚点；不自动暂停或继续 |
| ELF core | 离线读取已捕获映射，复用结构解析 | 当前支持未压缩 ELF64 x86-64；缺页不补零，身份和坐标需独立确认 |

主入口还支持 `read`、`function`、`relationships`、`subsystems`、`linkage` 和 `core-read`。`linkage` 复用现有解码器，分批读取暂停进程中的动态槽、待绑定链表和状态，保留限额、缺页及续读位置。读取格式见 [运行时与 core](skills/iosd-analysis/references/runtime-and-core.md)。大规模命令图、注册与状态分析继续复用 [脚本目录](skills/iosd-analysis/references/script-catalogue.md) 中的工具。

`components --output <文件.json>` 完全离线建立保存元数据的组件目录，提供类别、名称词元、同名记录和未知项检索。可用 `--query ospf` 等任意名称选择调查入口，不限某种协议。默认索引保留 5,692 条记录，包括 15 条同名 `cerrno_init` 和 8 条未记录 init RVA 的实体；不会按名字覆盖记录或把历史 metadata 当成当前运行状态。说明见 [组件索引与协议调查入口](docs/iosd组件索引与协议调查入口.md)。

协议线索扫描支持 `protocol --resume <上一页.json>`，可在名称索引和字符串窗口内部继续，保留各页结果、限额与未读范围。它不会因为反复扫描前面的范围而把后面的协议线索遗漏掉。继续方式及“初始化图为何不同于报文处理图”的说明见 [协议调查](skills/iosd-analysis/references/protocols.md)。

IDA 正在 rebase、attach 或执行其他脚本时先处理离线材料。新 IDB 或 rebase 后重新采集 session，不沿用旧 EA。客户端超时不会自动取消 IDA 工作，入口会保留 pending 记录并阻止同一 session 的自动重试。

## 代码与参考资料

- `skills/iosd-analysis/`：可单独复制安装的 skill，含必要代码、profile 和按需参考文档。
- `iosd_helper/`：维护中的解析核心；`ui.py` 等是保留的插件原型，不随 skill 的运行时代码加载。
- `tools/`：维护中的 MCP 采集、离线解析和报告工具。
- `profiles/`：带样本约束的布局、入口和语义 profile，不是通用 IOS XE 格式保证。
- `docs/`：既有架构与分析记录；[架构指南](docs/iosd逆向分析教程.md)、[模块与子系统](docs/iosd模块与子系统.md)、[NVGEN](docs/iosd的NVGEN与接口配置缓存.md)、[EHSA](docs/iosd的EHSA心跳与主备状态机.md)、[线程与 level](docs/iosd的线程与level.md)。

已深入分析的样本 MD5 为 `9eccfd46caadfff9c18557e2a446e19b`。经验模式帮助其他版本寻找入口，地址和字段按新样本重新验证。结果分别记录定义、观察到的连接、条件和执行证据，协议处理链按已经复核的数据流范围讲解。

既有原始捕获和大报告保留在本地，不随仓库分发。skill 内的参考副本会将未携带的报告链接标成历史材料路径，并记录来源摘要。保留文档中的历史统计及未知项，不能将它们当成当前 IDB 的采集结果。

## 开发和验证

修改 `iosd_helper/`、`tools/`、`profiles/` 或 `docs/` 后，重新构建 skill 内的生成副本：

```text
python -X utf8 tools/build_skill_release.py
python -m unittest discover -s tests -q
```

构建产物在 `dist/iosd-analysis-skill-0.3.0.zip`，生成来源和 SHA256 记录在 skill 的 `build-manifest.json`。主教程在仓库根目录维护，构建时复制到 skill；原文件保留供继续编辑。主入口和核心只用标准库；部分 HTML 报告工具及对应测试需要 `pip install -r requirements-docs.txt`。

新增 `inspect_elf_layout.py` 可离线解析原始 ELF64 的节、装载段、文件占用与 NOBITS。当前样本的文件布局已独立校验 MD5/SHA256，并整理为 [布局摘要](profiles/elf_layout_26_01_02.json)。大小和节名只用于容器导航，不自动赋予协议或组件所有权。图解先复用既有局部证据；用户确认 IDA 空闲后，已安全恢复 MCP，并补查 OSPF 类型取得、BGP UPDATE 入口和 UDP 入队/通知路径。

2026-10-30 已在完成 rebase 的 IDA 9.1 新 IDB 上保存数据库并建立新会话，实测通过 saved-IDB 字节、带原始 ELF 锚点的暂停内存、函数/引用与两批动态链表读取。重新验证了 12 个 CLI 节点及三类动作，补充 CDP、BGP、OSPF、UDP 的局部处理链；LLDP、IS-IS 保留线索和未知项。详见 [协议处理链与 CLI 新会话验证](docs/iosd协议处理链与CLI新会话验证.md)，定位摘要在 [协议证据索引](profiles/protocol_paths_26_01_02.json)。

CLI 已复核 69 份保存捕获，重新生成六模式共 73,159 条路径见证、194,435 个节点的派生图与注册对照。config 覆盖 11,985 个 EOL，未知/未读节点由 1,557 降至 482，参数与符号条件保留到目录中。方法见 [CLI 挖掘](docs/iosd的CLI挖掘方法.md)，数据见版本结果。后续沿剩余动作、条件和片段继续细化。

本轮目标运行期间只读取 saved IDB。既有链表仍有 frontiers，模块枚举达到 512 上限；子系统分批采集返回 683 条并标记 partial。插件原型的历史说明保存在 [历史文档](docs/IDA插件历史说明.md)。
