# iosd analysis skill

通过 MCP 辅助安全研究人员理解 Cisco IOS XE 的 iosd 大二进制：初始化组织、CLI 定义与条件、动态注册、协议处理入口、NVGEN、EHSA 和线程。复用已有分析代码与文档，保留未知、不完整、未注册及未取得的分支。

**主要入口：[iosd-analysis skill](skills/iosd-analysis/SKILL.md)。** 不需要安装 iosd Helper 的 IDA 界面插件；IDA 侧需要运行 MCP 服务，AI 客户端需要连接该服务。skill 提供调查流程、经验模式和资料，Python 核心负责确定性解析，MCP 提供当前 IDB/调试数据。

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

主入口还支持 `read`、`function`、`relationships`、`subsystems` 和 `core-read`。读取格式见 [运行时与 core](skills/iosd-analysis/references/runtime-and-core.md)。大规模命令图、注册与状态分析继续复用 [脚本目录](skills/iosd-analysis/references/script-catalogue.md) 中的工具。

IDA 正在 rebase、attach 或执行其他脚本时先处理离线材料。新 IDB 或 rebase 后重新采集 session，不沿用旧 EA。客户端超时不会自动取消 IDA 工作，入口会保留 pending 记录并阻止同一 session 的自动重试。

## 代码与参考资料

- `skills/iosd-analysis/`：可单独复制安装的 skill，含必要代码、profile 和按需参考文档。
- `iosd_helper/`：维护中的解析核心；`ui.py` 等是保留的插件原型，不随 skill 的运行时代码加载。
- `tools/`：维护中的 MCP 采集、离线解析和报告工具。
- `profiles/`：带样本约束的布局、入口和语义 profile，不是通用 IOS XE 格式保证。
- `docs/`：既有架构与分析记录；[架构指南](docs/iosd逆向分析教程.md)、[模块与子系统](docs/iosd模块与子系统.md)、[NVGEN](docs/iosd的NVGEN与接口配置缓存.md)、[EHSA](docs/iosd的EHSA心跳与主备状态机.md)、[线程与 level](docs/iosd的线程与level.md)。

已深入分析的样本 MD5 为 `9eccfd46caadfff9c18557e2a446e19b`。经验模式可帮助其他版本寻找入口，但地址、字段和推论必须重新验证。静态定义不等于当前可执行命令；一次运行快照不覆盖全部激活状态。协议入口搜索也不等于已经完整证明报文数据流。

既有原始捕获和大报告保留在本地，不随仓库分发。skill 内的参考副本会将未携带的报告链接标成历史材料路径，并记录来源摘要。保留文档中的历史统计及未知项，不能将它们当成当前 IDB 的采集结果。

## 开发和验证

修改 `iosd_helper/`、`tools/`、`profiles/` 或 `docs/` 后，重新构建 skill 内的生成副本：

```text
python -X utf8 tools/build_skill_release.py
python -m unittest discover -s tests -q
```

构建产物在 `dist/iosd-analysis-skill-0.1.0.zip`，生成来源和 SHA256 记录在 skill 的 `build-manifest.json`。构建过程不连接 IDA。主入口和核心只用标准库；部分 HTML 报告工具及对应测试需要 `pip install -r requirements-docs.txt`。

当前新 skill 入口完成离线验证；新加载、正在 rebase 的干净 IDB 尚未做本轮实机复测。此前采集记录和插件验证不能替代这项复测。插件原型的历史说明保存在 [历史文档](docs/IDA插件历史说明.md)，不作为本次 skill 的必需安装步骤。
