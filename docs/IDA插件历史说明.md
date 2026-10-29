# iosd Helper 插件历史说明

本文保存迁移到 skill 之前的插件入口、历史采集和功能说明。后续主入口为仓库中的 `skills/iosd-analysis/SKILL.md`。部分 GUI 显示实验尚未重新完成 IDA 实机验证，不是本次 skill 发布的依赖或稳定性承诺。

**0.6.2 新增整数显示**：在数据/汇编或 Hex-Rays 视图中，光标放到整数上，右键 **iosd Helper → Integer display / BE interpretation...**。提供 BE16/32/64 的十六进制、十进制和独立的 tagged 指针格式；数据/汇编使用原生自定义格式，伪代码保留常量原值并添加解码注解。原始字节不变。操作及 F5 临时注解的边界见 [整数显示与字节序](docs/整数显示与字节序.md)，[IDA 9.1 验证记录](reports/integer-display-ida91-smoke.json)。

当前七条 Linux 线程由谁创建、做什么、与 IOS 内部任务和初始化 `level_*` 有何区别，见 [iosd 的线程 任务与 level](docs/iosd的线程与level.md)。已核对主线程登记、平台运行时中的 pthread 创建、`libthpool.so` 的 Worker 池、内部线程表及数字 level 的栈创建消费者；全部业务回调到线程的归属继续保留为未知。

EHSA 心跳发送、接收、超时、主备状态机及平台边界，见 [iosd 的 EHSA 心跳与主备状态机](docs/iosd的EHSA心跳与主备状态机.md)。本轮保存 91 个不同 RVA 的函数反编译，恢复 14 个状态、224 个完整事件槽、19 个不同动作回调，关联 16 条相关子系统记录；[证据目录](reports/ehsa-implementation-20261029/index.html) 可检索全部表项。七项 GOT 读取将部分接口绑定到 `libchasfs.so`、`libcyan.so`、`libiosd_crb_vxe_unix.so`。状态 7 名称、部分事件来源、接口输出回调和 `stby-request-swo` 的外部消费链继续保留为未知。

离线重建和核验：`python tools/build_ehsa_report.py reports/ehsa-implementation-20261029`，`python tools/check_ehsa_evidence.py reports/ehsa-implementation-20261029`。样本入口保存在 `profiles/ehsa_26_01_02.json`。这些工具不连接 IDA，表项存在不代表现场可达，库范围匹配也不证明回调已执行。

**第一次阅读请从 [iosd 程序架构与分析指南（离线阅读版）](docs/iosd逆向分析教程.html) 开始。** 指南解释系统边界、启动编排、模块与子系统、注册分派和 CLI 等结构，并保留案例、地址速查和旧结论勘误；练习与答案已删除。[Markdown 源稿](docs/iosd逆向分析教程.md) 可直接在编辑器中阅读。下文主要保留实现细节和历史采集记录。

面向 Cisco IOS XE iosd 的 IDAPython 插件原型。分析读取不写目标内存；整数显示功能可按用户选择修改 IDB 的操作数表示属性。分析核心独立于 IDA，界面使用 IDA 原生 Choose，不依赖 Qt、MCP、模型服务或第三方 Python 包。

架构、实际启动链、概念层次与缩写见独立的 [iosd 架构 启动流程与术语说明](docs/iosd架构与术语说明.md)。它包含已核对的启动入口以及旧结论勘误，建议先读该文再看原始分析笔记。

通用注册分析的数据模型、未知分支保留原则，以及 attach、rebase 和首次动态内存读取步骤见 [通用注册分析与调试接入](docs/通用注册分析与调试接入.md)。IDA 忙于 attach/rebase 时先处理已有静态报告，恢复后按 RVA 对齐并重新核验映射。

模块与子系统的具体区别及新核对的初始化关系见 [iosd 模块 子系统与初始化架构](docs/iosd模块与子系统.md)。

配置状态怎样生成文本、NVGEN 与 CLI handler 的关系，以及当前样本的接口配置缓存，见 [iosd 的 NVGEN 与接口配置缓存](docs/iosd的NVGEN与接口配置缓存.md)。已核对显示生成入口、hostname/description 共用 handler、缓存命中/保存及禁用清理；普通接口更新的全部失效触发点与当前启用状态继续保留为未知。

NVGEN 描述符对照可离线复现：`python tools/analyze_nvgen_bindings.py reports/runtime-comparison-20261029/options/tree --output reports/nvgen-implementation-20261029`。输出保留 5,099 个 nvgens 节点、迭代器及与已解码 EOL 的函数/selector 关联；统计范围见同目录 `binding-summary.json`，不是全部组件或可执行命令数。新 profile `profiles/nvgen_26_01_02.json` 绑定当前 MD5，保存已审查入口、字段和缺口。

[NVGEN 与接口缓存证据目录](reports/nvgen-implementation-20261029/index.html) 提供流程、共用 handler 案例、描述符关联及未解析项检索。保存字节的节点关系核验可运行 `python tools/check_nvgen_evidence.py reports/nvgen-implementation-20261029`；这检查证据身份和字段关联，不执行目标函数。该阶段 127 项单元测试通过。

## 当前能力与边界

0.6.1 新增 [初始化组织地图](reports/iosd-architecture-20261029/index.html)，分别浏览 5,692 条 subsystem 候选、15 个 module header 和 11 条 module link。新核对的 module 消费者支持将 10 条 link 标注为前置依赖、1 条标注为分组关系；没有自动生成 module 到 subsystem 的包含边。IDA 菜单 **Architecture: browse saved subsystem/module organization map** 可打开同目录 `architecture.json`，按类别进入候选实体、查看 module 分组和链接并跳转证据。该地图只覆盖已有初始化组织证据，跨库归属及协议报文路径仍需继续恢复。

离线重建：

```powershell
python tools/build_architecture_map.py reports/static-20261028T122305425118Z.json reports/mcp-plugin-module-result.json profiles/architecture_26_01_02.json --output reports/iosd-architecture-20261029
```

- IDB 段概览，双 magic 子系统候选扫描，以及独立的模块 header/link 解析。
- 按现有 IDA 名称列举消息入口、MQIPC、`tbl_*` 和 parser 线索。
- 分块扫描只读数据里的 `VIEW_ROOT/cisco.comp/...` 源码路径；双击显示直接引用。
- 明确选择 IDB、已暂停的 IDA 调试目标、未压缩 ELF64 x86-64 core 三种内存源。
- 内存探针、四种指针解码、PIE 地址映射及 16 字节锚点验证。
- 可配置 72 字节 ICM 候选节点检查、显式链接遍历、环检测、取消、读取失败保留及 JSON 导出。
- 静态 CLI 注册表发现、314 项动作表映射和 40 字节 transition 候选图提取；识别部分关键词、参数、EOL 处理函数及条件分支，支持 IDA 原生图、注册/节点证据列表及 JSON/DOT 导出。
- 配置模式语法候选路径恢复：关联模式入口、关键词、参数、条件、注册来源与 handler，区分普通、`no`、`default` 上下文；未知动作保留为 `<?>`。
- 暂停调试现场的分批动态槽/待绑定链采集、实际连接图重建、静态注册逐项对照和运行时语法示例导出。布局、状态变量与已审查门控由 MD5 绑定的 profile 提供；未知分支保留。

本次实机结果从 [运行时命令图与静态对照](reports/runtime-comparison-20261029/index.html) 阅读，包含 `service internal` 与 VPDN 的对照、模式路径树、原始图和所有待绑定记录。方法与复现入口见 [运行时命令图导出说明](docs/运行时命令图导出说明.md)。动态槽与状态读取可使用插件原生入口；大图分批采集、离线重建及报告导出使用命令行工具。

最新补读见 [config 模式恢复与新旧对照](reports/runtime-comparison-20261029/refinement/index.html)。原 26 个缺页范围及其后续引用已补读，当前模型缺页队列为 0；新增普通 CLI 动作解释，并修正已审查回调在 rebase 后的地址换算。该页分开列出原生 config 路径与经 `do-exec` 进入的 EXEC 分支，不把后者计作原生 config 新命令。

后续的 [关键词选项与间接条件报告](reports/runtime-comparison-20261029/options/index.html) 单独保留每个选项的值、状态效果、生成来源和所有已取得的条件边，并恢复 `multiple_funcs`、`test_func` 的载荷分支。生成器不执行，未解析入口继续保留。概念说明见 [config 关键词选项与条件回调](docs/config关键词选项与条件回调.md)。

**尚未实现**：自动定位并合并主命令树根、全部动作和注册条件的解释、完整命令语法恢复、hidden/undocumented 判定、全量子系统代码归属、日志调用参数分析与函数名恢复、跨版本差异、自动识别 core 对应的可执行文件。部分 EOL handler 字段已经由消费代码确认，但设备上的可达性、模式与权限尚未验证。

扫描结果保留为候选；插件不自动重命名、修改类型/注释、修改目标内存或执行设备命令。运行时读取失败不回退到 IDB，以免把静态内容混成快照内容。

## 分析项目与磁盘索引 0.6.0

新增第一阶段的项目工作流：创建/打开项目、后台建立磁盘索引、取消后续建、分页搜索候选、按需读取完整证据，以及按当前 IDB 基址跳转。无需 MCP 或模型服务。当前导入格式为 `tools/export_runtime_grammar.py` 生成的 `tree/`，不是任意 HTML 或旧版静态扫描 JSON。静态采集、动态采集及重建的一键任务编排仍待接入；此版先打通已有结果的持久化和 IDA 浏览。

本工作区已准备好 `projects/iosd-26.01.02-options/project.json`，引用本次 options 的完整证据。使用方法：

1. IDA 9.1 打开同一 iosd IDB，Alt+F7 运行 `dev_load.py`。不要同时启用已安装版。
2. 选择 **Project: open existing analysis project**，打开上述 `project.json`。
3. 重新打开菜单：`import builtins; builtins._iosd_helper_dev.menu()`。选择 **Project: browse/search candidates, conditions and unknown evidence**。
4. 数据类型中，`paths` 是普通有界路径示例，`variants` 是展开的选项示例，`nodes` 为完整节点，`unknown` 为未知/不完整节点，`registrations`、`slots`、`pending` 分别保存注册对照、动态槽、待绑定记录；`options` 和 `branches` 保留选项源及间接条件。
5. 双击类型，输入搜索词，如 `platform broadband`、`nbar`、动作名或 `0x` 开头的 RVA。模式填写内部名 `configure`、`interface`、`exec`；留空表示全部。每页 200 行，分页行可继续浏览全部已索引结果。
6. 双击结果打开字段列表和地址列表。字段中的 `conditions`、`gaps`、`edge_trace` 可逐项展开到 Output；地址列表中的 `image` 按当前 IDB 基址换算，`capture_va` 保留历史 VA、不重定位。未知分支与当前拒绝路径继续保留。历史快照的条件值不会当作当前目标状态。

创建新项目时，先在保存对话框中选择位置、填写项目名，例如 `D:\work\my-analysis.iosd-project`，再选择导出的 `tree/summary.json`。插件会新建 `D:\work\my-analysis\` 并保存其中的 `project.json`；项目文件夹已存在时拒绝覆盖。插件校验 MD5，保存采集基址和 IDA loader 段的 RVA 范围；调试器临时创建的段不纳入镜像地址范围。项目目录必须与证据文件位于同一磁盘，以便使用相对路径。项目复制后需保持与证据目录的相对关系。

后台索引需要独立的 **Python 3.10+**，只使用标准库。首次启动时填写解释器路径，例如本机的 `C:\Python312\python.exe`；不要填写 `ida.exe`。索引不访问 IDA、不读取目标，不阻塞 IDA 等待计算。菜单 **Project: task status / progress** 查看状态；**cancel indexing** 在批次边界停止，已提交批次保留；**start/resume** 重新校验数据后继续。插件关闭后，纯本地索引任务仍可完成。

项目保存 `project.json`、元数据副本、`index.sqlite`、`task.json` 和可选 `worker.log`。JSONL 大文件不复制；索引只保存摘要、偏移和逐记录哈希，选中时再读取原始行。源文件变化、二进制不匹配或行哈希不一致会拒绝读取。续建会核验完整文件 SHA-256；普通搜索先校验大小/时间，详细记录再校验行哈希。索引不是完整语法枚举，也不判断 undocumented。

若外部进程被强制结束，`worker.lock` 可能遗留。先检查 `task.json` 中 PID、`worker.log` 和任务管理器，确认旧进程已退出，再删除项目中的这个锁文件并续建；禁止在旧进程仍工作时删除。正常取消或异常退出会释放锁。

命令行也可操作同一项目：

```powershell
python tools/project_worker.py status projects/iosd-26.01.02-options
python tools/project_worker.py index projects/iosd-26.01.02-options
python tools/project_worker.py search projects/iosd-26.01.02-options "platform broadband" --collection variants --mode configure
python tools/project_worker.py verify projects/iosd-26.01.02-options
```

生成可分发代码包：`python tools/build_plugin_release.py`，输出 `dist/iosd-helper-0.6.0.zip`，包含插件、完整 Python 包（含 worker）、profiles 与 Markdown 文档，不含 iosd 二进制、IDB、内存或项目结果。解压后可运行同目录 `dev_load.py`；普通安装时复制插件文件、整个包和 profiles 到用户插件目录。原有功能无需外部 Python，后台索引才需要独立解释器。

本阶段验证：121 项单元测试通过；当前完整输入的 282,810 条索引记录逐文件计数一致，含全部 194,435 个节点、11,886 个未知/不完整节点与 245 条待绑定记录。SQLite 完整性、全部输入 SHA-256 和解压后的独立 worker 均验证通过。IDA 9.1 已实测原生结果列表、字段列表、中文条件列表和镜像地址跳转；测试前后目标运行状态均为 running，没有读取目标内存。验收记录见 `reports/project-index-validation.json` 与 `reports/project-browser-ida-smoke.json`。正常安装后重启 IDA 的完整生命周期、真实 core 采集任务和调试事件失效管理尚待下一阶段实测。

## 通用注册与状态依赖分析 0.5.0

新增业务无关的注册分析核心、保存证据的离线分析菜单、RVA 地址坐标，以及运行时动态链接/待绑定链表读取入口。API 地址和 ABI 放在样本 profile 中；通用算法不使用 VPDN 命令名称、handler 或状态地址。直接和间接调用、槽写入、局部变量多个来源、状态写读、未知参数和待采集函数分开保存，不自动把同一 handler 的全部 selector 宣布为注册触发器。

本轮保留 10,479 条新取得的 API 引用，结合 132 个缓存函数生成 [通用候选报告](reports/lifecycle-candidates-20261029/index.html)。61 组触发关系涉及 31 个 handler，包含 `segment-routing mpls`、`metadata flow` 及公共模式创建链上的其他命令。59 个函数缓存附带匹配身份，73 个缺独立身份字段并明确标记。文本分析是启发式表达式子集；原文、未解析项和未采集函数均保存。证据记录数不等于唯一调用、槽或命令数。

结构化 ctree 采集在接口兼容修正后的请求发生超时，目前停止继续向 IDA 派发。入口已增加检查点、数量/时间边界、失败重试记录和超时恢复信息，完整实机采集仍需 IDA 恢复后验证。92 项单元测试和结果页搜索检查通过；真实运行时链表读取尚未验证。

完整步骤、命令、输入格式和 rebase 注意事项见 [通用注册分析与调试接入](docs/通用注册分析与调试接入.md)。旧零基址语法 profile 仍会拒绝 rebased IDB；新生命周期 API profile 使用 RVA，可以和保留的旧语法报告关联。重新建立映射后再读取动态槽，禁止把堆 VA 当 RVA，也不能用 IDB 补齐缺失的运行时页面。

## VPDN 激活链与动态链接候选：0.4.2

只读追踪结果见 [VPDN 命令、条件与注册链报告](reports/vpdn-activation-20261029/index.html)。当前样本已确认 `(config)# vpdn enable` 的 selector 28：普通非 NVGEN 路径在资源列表没有活动回调否决后写启用状态；测试初始化尝试标志为 0 时调用 `11DE2440`，提交表 `3570F660`，向 EXEC `test` 下挂接片段。该片段恢复 14 个 EOL、19 条已建模无环语法模板，完整路径及 25 条边界路线另存，未丢弃未知链接。

同一 handler 的其他配置 selector 在启用状态为 0 时返回错误 201。`no/default vpdn enable` 的已审查分支只清启用状态，不复位测试初始化尝试标志；再次 enable 可跳过该初始化。调用方不检查注册/进程创建结果，因此“一次性标志=1”不能当作成功安装的证明。测试 handler 也没有相同的直接启用状态检查；消息型命令、直接设置测试状态的命令、scalability 批处理状态和对象查找分别保留依赖。

额外确认了共享 SSS 回调的间接注册：`109FB180` 返回槽的已知赋值候选为 `10973010`，其首次分支经 `1098D6F0` 提交 `34C49EC0` 的 6 个 subscriber 跟踪片段。共享初始化还定义 9 个相关动态链接候选，接到 `show monitor event-trace ...`、EXEC `monitor event-trace ...` 和配置模式 `monitor event-trace ...`。这些片段并非 VPDN 专有，实际槽绑定和初始化先后仍需快照验证。

槽未出现时，`DEF70B0` 可先排入 `3CB561E8` 并返回 1；动态创建槽清 `3CB561C8`，`DEE9E10` 在后续 parser 入口重试绑定。这说明片段可在首次注册之后才接入，无需假设第二条命令专门注册它。静态投影保留这种可能性，不模拟实际内存或断言绑定一定成功。

插件 profile 新增 `dynamic_link_definitions`：显式记录已审查的 key、入口/返回 anchor、type、creator 和证据，提取时同时采集返回 anchor。静态候选边携带槽创建证据，不伪造堆槽地址；同一个 key 的多个创建候选全部保留。自动注册表发现与手工补充表合并，避免本轮找到的尾跳注册表再次被自动发现结果覆盖。这仍不是通用的间接调用或数据流自动恢复器。

IDA 9.1 中重新运行 `dev_load.py`，提取静态图时选择 `reports/vpdn-activation-20261029/ida-profile.json`，然后使用原有语法恢复或候选池菜单。该 profile 绑定当前 MD5 和 imagebase=0，其他二进制必须重新定位。共享 trace 的时间、循环等动作仍有不透明步骤，不能把最短路径或示例当成命令全集。

离线复现：

```powershell
python tools/validate_ida_backend.py http://172.16.100.165:13338/mcp profiles/static_vpdn_supplement_26_01_02.json reports/vpdn-supplement-graph.json
python tools/analyze_vpdn.py reports/static-cli-config-graph.json --supplement reports/vpdn-supplement-graph.json --config-paths reports/iosd-config-paths-20261029/paths.jsonl --output reports/vpdn-activation-20261029
```

第一步只读 IDB，第二步重建已审查案例，不自动推导其他样本的状态机。`reviewed-lifecycle.json` 保存结论和边界，`function-evidence.json` 保存完整反编译证据，`dynamic-link-definitions.json`、`supplement-graph.json` 与 `prefix-witnesses.json` 保存槽、图和模式前缀，`manifest.json` 记录身份和输入/源码哈希。

0.4.2 的 79 项测试通过。新增完整 profile 已在同一 IDA 9.1 中只读提取：113,523 个节点、197,858 条结构边、4,564 条注册记录，均未触及采集上限；不是整个二进制的完整性证明。`tools/check_vpdn_case.py reports/vpdn-full-graph.json reports/vpdn-activation-20261029` 将报告中的 19 条 test 路径、104 条配置示例、24 条跟踪示例及模式前缀与新图核对，生成 `ida-verification.json`，本次复核 5,852 条路径边及对应 EOL/handler。未执行设备命令或验证运行时可用性。

## 静态候选定义池：0.4.1

分析目标是尽量覆盖潜在命令定义，未知内容、不完整语法、当前未安装的注册片段、运行时条件尚不成立，均不能作为排除依据。路径示例与候选定义池分开：0.4.0 的优先路径用于浏览，不承担全集覆盖。原始结构、未求值的条件、循环和所有已提取分支保存成图；不以某一次启动状态或普通 CLI 初始值缩小定义池。

当前候选池保留全部已取得的 **113,280 个节点、197,384 条结构边、4,555 条注册记录**；另外导出 198,725 条带条件或未知动作的语法投影边。3,199 条缺少核心链接槽匹配的注册片段、21,061 个未知/不完整节点、378 处未解析注册调用均保留。16,679 个已知 handler 定义中，有 9,294 个尚无已知模式绑定，也没有因模式或路径未知而排除。

“全部”只描述已取得证据的保留范围，不能宣称二进制里的所有定义已经发现。原始结构边和语法投影分别保存；后者只解释已复核的普通 CLI 语义，条件均保留为未求值，未知动作使用不透明步骤。组合宏的数字参数分支和负向省略分支也分别保留，不固定在正向输入状态。节点的条件、状态写入、权限描述符及参数 flags 另存 `conditions.jsonl`。

可搜索结果在 `reports/iosd-candidate-space-20261029/index.html`。它列出所有已知 handler 定义（包括模式未知）、全部注册片段、未知节点、可能的注册触发关系及未解析注册调用。邻近关键词只是检索提示，不拼成命令。完整数据在同目录的 `nodes.jsonl`、`structural_edges.jsonl`、`transitions.jsonl`、`terminal_rules.jsonl`、`fragments.jsonl` 等文件中，示例裁剪不会删除这些定义。

本轮还只读检查了注册调用者三层内的直接调用/尾跳祖先，取得 1,885 个函数、1,368 条调用边，找到 **36 组已知 handler 到注册例程的候选关系**。每组保留一条较短调用链用于展示，全部已采集调用边另存 `registration_call_graph.jsonl`。4 个函数触及每函数 64 个引用的边界；间接调用、消息分发、函数指针和更深调用尚未覆盖。调用链存在不等于可行触发路径，也不证明必须先执行某条命令。

0.4.1 当时将 VPDN handler `0x11D48420 → 0x11DE2440 → 0xDEF7870` 记为待核对线索；0.4.2 已进一步定位触发 selector 28、状态写入及条件，见上节。仍不能把同 handler 的每条命令都标为注册触发器。另有通过创建/切换模式的辅助函数到达注册例程的候选，尚须分别核对。

复现：

```powershell
python tools/audit_registration_triggers.py http://172.16.100.165:13338/mcp reports/static-cli-config-graph.json --output reports/registration-trigger-audit.json
python tools/build_candidate_space.py reports/static-cli-config-graph.json --trigger-audit reports/registration-trigger-audit.json --output reports/iosd-candidate-space-20261029
```

第一条只读匹配的 IDA；第二条处理保存的图，不连接设备。省略 `--trigger-audit` 也能构建定义池，报告会明确表示未提供触发审计。插件中先提取静态图，再选择 **Build acquired candidate pool (keep unknown / unbound definitions)**；可用 **Export last candidate pool as searchable HTML** 导出。原生菜单默认不发起调用关系审计；带审计的结果使用上述离线命令生成。

后续覆盖工作包括：未解析注册参数和动态链接槽、状态变量的读写依赖、命令执行前后改变解析条件的关系、间接分派及未解释载荷中的额外链接。运行时快照用来补充和验证，不能因快照里没出现某个定义而删去静态候选。最终应保留“可能定义—条件—注册来源—状态/触发依赖—handler”的证据关系，而非仅输出当前可执行命令或一组较完整的字符串。

## 配置模式语法路径：0.4.0

本轮直接分析 iosd，不以 CDL 为语法来源。`sub_DFF1CF0` 的模式注册调用确认了以下静态起点，`sub_DF3B9B0` 将第 9 个参数写入 mode 对象的 `+0x50`：

| 内部模式名 | 提示符部分 | 语法起点 |
|---|---|---|
| `exec` | EXEC | `0x341168D0` |
| `configure` | `config` | `0x341168F8` |
| `interface` | `config-if` | `0x34116920` |
| `subinterface` | `config-subif` | `0x34116920` |
| `null-interface` | `config-if` | `0x34116948` |
| `line` | `config-line` | `0x34116970` |

默认先恢复 `configure` 和 `interface` 两种模式。操作顺序：

1. IDA 9.1 保持当前 IDB 打开，Alt+F7 运行 `dev_load.py`。
2. 选择 **Static CLI graph (experimental profile)**，加载 `profiles/static_cli_config_paths_26_01_02.json`。此前的旧图 profile 不含模式证据和核心链接槽，不能用于此步骤。
3. 再打开菜单（`import builtins; builtins._iosd_helper_dev.menu()`），选择 **Recover config / config-if syntax paths (experimental)**。
4. 在候选列表中搜索、双击查看完整条件、参数、边轨迹和 handler 地址。通过 **Export last syntax paths as searchable HTML** 保存可搜索结果；通用 JSON 导出保存该次路径结果。

已经生成的结果页为 `reports/iosd-config-paths-20261029/index.html`，完整路径证据为同目录 `paths.jsonl`，语法文本为 `commands.txt`，覆盖报告为 `summary.json`。

当前实测结果：

| 模式 | 候选路径示例数 | 不同终结点数 | 无不透明动作/回调步骤的示例数 |
|---|---:|---:|---:|
| `config` | 19,056 | 6,525 | 17,337 |
| `config-if` | 2,357 | 859 | 2,150 |

合计 21,413 条示例，对应 2,589 个不同 handler；全部 handler 都落在当前 IDA 的函数入口。两种模式均遍历完当前模型可达的状态，没有达到状态/路径上限。这不是命令总数：普通、`no`、`default` 会形成不同上下文示例；相同终结点和上下文的多个别名/可选路径只保留一条优先示例。

例如已恢复：

```text
(config)# hostname <string> <cr>       → 0xE0E6A00
(config)# no hostname <cr>            → 0xE0E6A00
(config)# default hostname <cr>       → 0xE0E6A00
(config-if)# description <string> <cr> → 0xE40C850
(config-if)# shutdown <cr>             → 0xE40CF20
(config-if)# no shutdown <cr>          → 0xE40CF20
```

路径恢复按节点消费者区分“消耗输入”和“换一个选择”：关键词 alternate 不附带当前关键词；参数 alternate 不附带参数；help 只走 alternate；NVGEN 在当前普通 CLI 假设下沿 accept 继续，并与终结 handler 分开。`testexpr`、比较、权限、接口状态和布尔条件保留分支证据，不执行谓词、不读取运行时变量。`params_action` / `params_command_action` 还会在单个节点中同时定义关键词、数值参数和 handler，新版会将它们作为组合终结点处理。

路径只符号跟踪本样本的三个字段：sense (`9328`)、default (`9332`)、NVGEN (`9636`)。初始 `[1,0,0]` 是“普通正向 CLI 输入”的显式分析假设；`no`、`default` 对这些字段的常量赋值来自静态描述符。未知回调会使相关状态不确定，未知动作产生 `<?>`；回调、权限、数值/字符串 flags 和未建模状态仍可能影响真实行为。谓词从不执行，`evaluated=true` 仅用于这些局部符号常量的比较。

核心链接表由 `sub_DFF1C10` 返回，当前为 `0x341146E0`、48 字节步长、180 个有效槽，消费代码为 `sub_DEF70B0`。路径层构造 1,356 条候选安装边，并附带原注册记录、调用位置和条件，**不修改 IDB，也不声称恢复实际启动顺序**。仍有 3,199 条注册记录未匹配这张核心表，可能需要继续分析动态链接槽注册；它们单独列在结果页中。已有的 378 处未解析注册调用、其余动作和路径中的不透明步骤也继续保留。因此模式内的“遍历完成”仅针对当前模型，不能视作完整 CLI 恢复。

选择示例时优先减少未知步骤，再减少输入 token，最后减少图边数。这样会优先显示 `shutdown`，而不是仅因图上距离较短就选中 `shutdown forced`。仍不枚举所有等价路径，也不证明约束组合在实际设备上可满足。无 `<?>` 也不等于已验证运行时可用，更不能据此判断 undocumented。

离线复现及选择其他已知模式：

```powershell
python tools/validate_ida_backend.py http://172.16.100.165:13338/mcp profiles/static_cli_config_paths_26_01_02.json reports/static-cli-config-graph.json
python tools/recover_iosd_syntax.py reports/static-cli-config-graph.json --output reports/iosd-config-paths-20261029
python tools/recover_iosd_syntax.py reports/static-cli-config-graph.json --mode line --output reports/iosd-line-paths
```

第一步已在同一 IDA 9.1 内用当前提取代码验证；第二步只读保存的 JSON。图报告记录输入身份和提取源码 SHA-256；路径报告记录提取与路径恢复代码的 SHA-256。IDA 中也已用 0.4.0 原生界面成功显示 21,413 行结果。本机 62 项测试通过，新增测试覆盖关键词分支不错误拼词、`no/default` 参数省略、组合终结宏、局部 OR 状态赋值、注册片段继承模式及前缀、未知动作、限制与示例选择顺序。

## 查看全部已发现入口：0.3.1 基线

现在可以遍历全部已发现的静态 root，不再只处理前 100 个。Alt+F7 运行 `dev_load.py`，选择 **Static CLI graph (experimental profile)**，加载 `profiles/static_cli_all_discovered_26_01_02.json`。该配置不设 root 数量限制，保留 200,000 个节点的保护上限；原生图仍只预览前 400 个节点及其出边。

当前 IDA 9.1 实测：**4,508 / 4,508 个已发现 root 均处理完毕，待遍历节点为 0，没有触及节点上限**。得到 101,521 个节点、169,625 条边、37,718 个关键词节点（9,302 种不同文本）、9,593 个参数节点、15,049 个 EOL 终结节点和 5,287 个不同 handler 候选。15,049 个 EOL 的候选 handler 都对应 IDA 函数入口。

查看方式：

1. 直接打开已生成的 `reports/static-cli-catalogue.html`，选择关键词、EOL、参数、动作编号、注册记录或未解析项，输入文本或 `0x` 地址搜索。按 200 条分页，过滤覆盖当前类型的全部记录；点击行显示字段。
2. 插件完成扫描后，重新打开菜单，选择 **Browse last static CLI catalogue: keywords / EOL / actions**，在 IDA 中打开三个独立列表。双击跳转并打印证据，使用 IDA 列表自带的搜索功能定位。
3. 选择 **Export last static CLI catalogue as searchable HTML** 生成当前扫描的离线目录；JSON/DOT 导出仍保留完整的已提取图。

这里的“全部”仅指已发现入口和已配置边的遍历覆盖。仍有 **378 处注册调用未解析、26,808 个节点的载荷语义未解释、176 个描述符解码/校验错误、13 个节点读取或链接缺口**，另有 399 个节点对应静态回调为空的动作槽。错误保留原始证据，不能据此判为不存在的命令。

目录没有直接把关键词拼成完整命令，也没有执行谓词或判断 hidden/undocumented。parser 动作编号 0–313 表示解析操作类型；关键词数、EOL 数、handler 数也都不能换算成完整命令条数。后续恢复命令语法路径，需要解释剩余动作、选项列表、模式/权限及动态链接，继续追踪未解析注册来源。

实测报告为 `reports/static-cli-all-discovered.json/.dot`，可搜索目录为 `reports/static-cli-catalogue.html`。本轮在 IDA 中用当前 UI 代码成功显示了关键词、EOL 和动作编号三张列表；本机 44 项 Python 测试通过，并检查了 HTML 目录的搜索、切换类型、分页及行详情行为。

复现命令：

```powershell
python tools/validate_ida_backend.py http://172.16.100.165:13338/mcp profiles/static_cli_all_discovered_26_01_02.json reports/static-cli-all-discovered.json
python tools/export_cli_catalogue.py reports/static-cli-all-discovered.json reports/static-cli-catalogue.html
```

## CDL XML 遍历器

新增 Python 标准库版 `tools/walk_cdl.py`，原 `cdl_walk.cpp` 保留。CDL 属于另一条分析来源：文件头标为 BinOS Command Set；不能直接把它当作 iosd 全部命令的 XML 版本。Shell Manager 的 XML 加载及 IOS 侧消息通信关系见 [Cisco 系统消息说明](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/16_xe/smg/xe-16-10/b-sem-16-10-1/b-sem-16-10-1_chapter_0110.pdf)，这不证明 iosd 本身读取 CDL。

新版按 XML 自己声明的编码严格解析，以当前路径内的环检测替代旧 DFS 的全局屏蔽规则。显式 `edges` 与节点中的 `accept/alternate/nonzero/zero` 属性分别保留；边上的 `filter-ref`、`set`、`set-tdl` 不丢弃，也不擅自求值。request/bundle 原样保留，不根据名称推断 handler。

运行：

```powershell
python tools/walk_cdl.py c8kv-26.01.02/cdl.xml --output reports/cdl-walk-20261029
python tools/walk_cdl.py c8kv-26.01.02/cdl.xml --root config --output reports/cdl-config-20261029
```

每个输出目录包含 `index.html`（可搜索结果）、`summary.json`（覆盖及路径计数）、`paths.jsonl`（候选路径和边注解）、`commands.txt`（候选语法文本）、`nodes.jsonl`、`edges.jsonl`、`requests.jsonl`（完整原始图记录）。`--root` 接受 GUID 或精确内部名称，不使用输入关键词猜测节点。默认根据 `NODE_DAG_ROOT` 定位根。

2026-10-29 对当前文件的结果：

- 78,381 个 GUID 节点，另有 4,375 个 request；152,098 条显式边，解析错误为 0。
- 主根 3840 可达 55,756 个节点、4,372 个 EOL；有 1 个 EOL 不可达。图无环。
- 显式图精确计数为 652,569,212 条 root→EOL 路径。这是结构路径数，包含共享分支组合，不是不同可执行命令的数量，也未展开数值/字符串参数的全部输入。
- 默认输出 4,772 条路径：每个可达 EOL 的最短示例，以及每个顶层分支最多 25 条样例；覆盖全部 4,372 个可达 EOL。未输出全部 6.53 亿条路径，报告明确标记 `all_explicit_edge_paths_emitted=false`。
- 89,904 条边含元数据，保留 119,318 个 `set`、46,895 个 `filter-ref` 和 3,811 个 `set-tdl`。22,591 个 filter 定义保存在节点记录中；显式边端点不直接指向 filter，不代表过滤器不存在。
- `config` 子图只有两条完整显式路径：`config hw-obfl dummy <cr>`、`config sdm dummy <cr>`。`dummy` 为原始关键词，不能据此当作设备上可用的配置命令；这里没有展示通常的 `(config)#`／`(config-if)#` 模式切换。

旧算法对照为源码规则模拟，没有执行原 C++ 程序。例如 `set_trace_eol_auto_eol` 的显式路径有 892,560 条，旧 DFS 规则模拟只输出 9 条，说明共享后缀被错误屏蔽。新算法的共享路径、循环、数量/深度/步数限制、XML 编码、重复 GUID、悬空边及边注解均有测试。

`--max-paths` 默认为 10,000，`--sample-per-branch` 默认为 25；也可指定 `--max-depth` 和 `--max-steps`。对于小子图，会在限制允许时完整枚举；大图使用精确 DAG 计数与有边界的示例输出。限制影响、不可达 EOL、每批停止原因都保存在 `summary.json`。所有候选路径的条件真值和 CLI 模式仍未确认。

## 小图与前 100 个入口配置（0.3.0 基线）

IDA 9.1 打开当前 iosd IDB，Alt+F7 执行 `D:\cisco\iosd_helper\dev_load.py`，选择 **Static CLI graph (experimental profile)**，按用途选择：

| Profile | 用途 | 当前 IDB 实测 |
|---|---|---|
| `profiles/static_cli_flow_26_01_02.json` | 先检查较小的 flow 示例图 | 6 条注册记录、70 个节点、102 条边、25 个关键词节点、14 个 EOL 节点、11 个不同 handler 候选、3 个参数节点 |
| `profiles/static_cli_discovery_26_01_02.json` | 发现通用注册函数的更多直接调用及注册表 | 检查 1,720 处调用，发现 1,319 个候选表、4,555 条不同注册记录、4,508 个不同 root；其中先遍历 100 个 root |

扩展配置遍历的 100 个 root 得到 **2,847 个节点、5,001 条边、1,004 个关键词节点、197 个参数节点、299 个 EOL 节点和 126 个不同 handler 候选**。所有这些 EOL handler 候选都对应当前 IDA 的函数入口。共 453 个候选表的调用者可与子系统 init 入口精确匹配，这仅提供注册来源线索。

这不是完整命令数：还剩 **4,408 个 root 未选入遍历、378 处直接调用的参数未解析、932 个节点的载荷语义未解释**，另有 3 个链接缺口、2 个关键词描述符未通过简单 token 校验。报告保留其原始字节、地址和失败原因；后两项不能据此判为坏数据。注册路径的运行时条件没有求值，间接调用、包装函数和动态注册也可能未被覆盖。

动作表共 314 个有名称的编号槽位，186 个在静态文件中有函数指针；编号 186 是 `LAST_INTERNAL_ENUM`，187..313 的动作回调需要继续追踪运行时注册代码。空回调槽不表示对应命令不存在。已解释的部分动作包含 `keyword_action`、`keyword_id_action`、四类 EOL、`general_number_action`、`general_string_action`、`testexpr_action` 和 `nvgens_action`。数字/字符串 flags、权限描述符仍保留原始字节，不据此判断 hidden。

图中关键词显示文本，数字显示范围，字符串显示 `<string>`，EOL 显示绿色的 `<cr> → handler 地址`。`testexpr_action` 记录谓词地址并沿静态 false 分支提取，不执行谓词；NVGEN 标为配置生成回调。已知编号显示动作名称，未知编号保留 `op_N`。图超过 400 个节点时只预览前 400 个及其出边，节点列表、JSON 和 DOT 保留全部已提取数据。

两个 profile 都绑定输入 MD5 和 IDB imagebase=0，地址不适用于其他构建；rebase 后会拒绝运行。`complete_for_configured_edges` 只表示选定起点和已配置边已遍历完。结果中的 `coverage`、`unvisited_roots`、`discovery.unresolved_call_sites`、`semantic_error` 和 `summary.unresolved_payload_nodes` 需要一起查看。

通过 **Export last result as JSON** 保存地址、原始字节、注册条件与缺口，或选择 **Export last static CLI graph as DOT** 输出带边标签的图。双击图节点或列表行可跳转 IDA 并打印证据。重新打开插件菜单可在 IDA Python 控制台执行 `builtins._iosd_helper_dev.menu()`（先 `import builtins`）。

本轮已通过用户提供的 MCP 在同一个 IDA 9.1 数据库执行当前源代码，并成功显示新版原生图。真实结果保存为 `reports/static-cli-flow-semantic.json/.dot` 和 `reports/static-cli-discovery-semantic.json/.dot`，JSON 包含输入身份和源码 SHA-256。旧 `static-cli-flow-graph` 文件保留为历史结果。

开发者可用同样的只读验证方式复现，无需安装 MCP 依赖到插件中：

```powershell
python tools/validate_ida_backend.py http://172.16.100.165:13338/mcp profiles/static_cli_discovery_26_01_02.json reports/static-cli-discovery-semantic.json
python tools/preview_ida_graph.py http://172.16.100.165:13338/mcp reports/static-cli-flow-semantic.json
```

第一条读取当前 IDB 并写本地报告，第二条显示匹配报告的图。均不修改 IDB 的名称、类型、注释或目标内存。

## 环境

0.1.1 的真实 IDA 9.1 报告（`reports/static-20261028T122305425118Z.json`）中，7 项扫描均完成。模块段原始记录显示：header 为 32 字节，签名 `0x15055CC1 + 0xAFECAFEC`，候选名称指针 +8；link 为 24 字节，标签为 `0xDFEADFEA` 或 `0xABEFABEF`，两个候选端点位于 +8/+16。0.1.2 已据此增加独立解析器；端点方向、层级/依赖语义，以及 header +16/+24 的含义仍未确认。

已通过用户提供的 Streamable HTTP MCP 在同一个 IDA 9.1 数据库内执行当前模块解析代码，得到 **15 条 header、11 条 link、0 个读取错误**；结果见 `reports/mcp-plugin-module-result.json`，包含源码 SHA-256。名称为 14 个 `level_*` 分类标记与 `memtest`，不能据此宣称恢复了 15 个业务模块。界面可通过 Alt+F7 执行 `dev_load.py`，选择 **Module headers / links (IDB)** 查看。

0.1.2 的函数候选增加 `dot_prefixed_name` 和 IDA `is_thunk` 标志。0.1.1 的 14,407 条候选包含 3,882 条带点前缀名称，不能直接视为同等数量的独立功能实现。

已收到真实样本的 IDA 9.1 静态报告（`reports/static-20261028T121642876142Z.json`，插件 0.1.0）：6 项扫描均执行完成，总耗时约 31 秒。识别到 13,163 个段、5,692 条子系统候选记录（5,678 个不同名称）、3,542 条源码路径和 14 处字符串锚点。子系统指针按 little 解码时可读，记录头间隔均为 96 字节；这仅是当前样本的观察。

同一报告显示：模块段没有命中当前双 magic 规则；源码/锚点扫描各有 2 个不可读块。旧符号分类混入了非代码名称，0.1.1 已改为只收录 IDA 函数入口，并增加模块/link 段原始字节采样。修订代码的真实 IDA 测试仍需重新运行 `static_test.py`；原始报告保留不变。

- Python 3.8+；IDA 必须使用 Python 3。设计面向 IDA 7.5+ 的插件/Choose API，后续版本兼容性仍需实测。
- 不要求反编译器。实时调试需要你先在 IDA 中连接对应调试后端并暂停 iosd。
- 本项目已用本机 IDA 7.5 的 Python 包核对所用接口；**这不等同于真实 IDA 加载测试**。
- core 独立解析 PT_LOAD，所以可以打开原 iosd 的 IDB，再由插件选择 core；无需把 core 当作可执行文件重新分析。支持未压缩 ELF64 x86-64 ET_CORE；暂不支持扩展 program-header 数量、压缩/厂商私有转储格式。`.core.gz` 先解压。

## 开发时如何调测（推荐）

### IDA 9.1：当前 iosd IDB 的静态测试

在 IDA 9.1 中打开 `c8kv-26.01.02/x86_64_crb_linux_iosd_vxe-universalk9-ms.i64`，按 Alt+F7 运行项目根目录下的 **`static_test.py`**。数据库若已打开就直接使用，不要重复加载 `.id0/.id1` 分片。

脚本依次运行段枚举、已知名称定位、符号分类、四种编码的子系统候选扫描、源码路径扫描和日志字符串锚点扫描。结果写到 `reports/static-时间戳.json`，并弹出步骤摘要。每步保存一次；取消会保留部分结果并跳过后续扫描。`completed` 只表示代码执行完毕，命中数量和候选语义还需核实；零命中不一定是插件错误。

测试只读 IDB，不连接目标、加载 core、启动新分析或保存数据库。若 IDA 自身仍在自动分析，当前结果可能不完整，报告记录其状态。插件原型与常规安装不要同时加载。测试后可用下文的 Python 控制台命令打开插件菜单，逐项查看列表；此操作会重新运行所选扫描。

报告对象也保存在 `builtins._iosd_helper_static_report`，可以在 IDA Python 控制台检查：

```python
import builtins
r = builtins._iosd_helper_static_report
print(r['identity'])
print([(s['name'], s['status']) for s in r['steps']])
```

### 哪些定位线索可以跨二进制复用

| 对象 | 静态定位方式 | 边界 |
|---|---|---|
| `subsys_header_section` / `module_header_section` / `module_link_section` | 枚举 IDA 段名 | 段名保留时可直接定位；子系统和 module/link 使用不同解析器，link 方向和层级含义待确认 |
| `.plt` / `.got` / `.btrace_*` / `CRFT_func` | 段名或已有 IDA 名称 | ELF section 与 IDA segment 不一定一一对应；找不到名称不能断言对象不存在 |
| `icm_main` / `parser_add_command` / `parse_cmd` 等 | 先查已有 IDA 名称，再查日志/`__func__` 字符串的直接引用 | stripped 文件可能只保留字符串。数据库名称可能来自之前的人工重命名 |
| `_message_handler` / `_message_dispatch_init` / `mqipc` / `tbl_*` | 按已有 IDA 名称分类 | 名称暗示功能；不等于证明真实注册关系或字段边界 |
| `VIEW_ROOT/cisco.comp/...` | 静态字节扫描 | 表示源码路径线索，不等于恢复了编译单元或完整函数归属 |
| 主 CLI 树根全局 | 尚无已验证的通用定位规则 | 需要从已确认代码的数据引用/初始化路径继续推导 |
| `qword_37B5323C` 等自动名 | 不能作为跨构建稳定名称 | 名称中的地址来自当前 IDB；文档将其识别为 diff 临时结构 |

同一份二进制仅 IDB rebase 时，相关地址通常随同一个基址差迁移；换版本/平台/构建时，代码与数据布局都可能改变，旧 RVA 也不保证有效。运行时还存在 ASLR 和动态堆地址。结构字段偏移与 magic 是另外一类可复用的**规则候选**，也需要跨样本验证。

通用扫描以符号/段名、字符串和 magic 为定位线索；静态 CLI 实验 profile 另外使用与 MD5/imagebase 绑定的样本地址。字符串直接交叉引用可能指向包装函数或共享日志代码，不能自动将引用者重命名为字符串中的函数名。

### 开发热加载

1. 在 IDA 中打开 iosd 的 IDB。
2. `File → Script file`（通常 Alt+F7）运行 `D:\cisco\iosd_helper\dev_load.py`。
3. 弹出主菜单，选择概览或扫描。双击结果可跳转/打印依据；IDA Output 中日志以 `[iosd-helper]` 开头。
4. 修改代码后再次运行 `dev_load.py`：关闭旧结果窗口、释放 core、卸载本包模块并加载新代码。开发会话数据会重置；需要保留结果时先导出 JSON。
5. 不改代码时，在 IDA 的 Python 控制台再次打开菜单：

```python
import builtins
builtins._iosd_helper_dev.menu()
```

查看完整异常堆栈也在 Output。调试核心解析时可直接用本机 Python 下断点，不必进入 IDA。

例如先生成下面的 fixture，再在项目目录执行：

```powershell
python tools/inspect_core.py tests/fixtures/generated/fixture-iosd.core 0x555555564000 --layout profiles/icm_conservative.json
```

这会把候选节点和原始字节打印为 JSON。也可以用 IDE 的 Python 调试器在 `iosd_helper/structures.py` 下断点后启动该脚本，独立排查 core 读取/布局问题。

开发热加载入口不要与已安装插件同时使用，也不要在开发热加载期间打开多个 IDB 窗口。正式插件通过 PLUGIN_MULTI 为各数据库建立独立实例。

### 安装为普通插件

在 IDA Python 控制台查询用户目录：

```python
import ida_diskio
print(ida_diskio.get_user_idadir())
```

把 `iosd_helper_plugin.py` 和整个 `iosd_helper/` 包一起复制到该目录的 `plugins/` 下，重启 IDA。入口为 `Edit → Plugins → iosd Helper`，快捷键 `Alt+Shift+I`。JSON profiles 可留在项目目录，需要时从插件选择。无需安装 Python 依赖。

## 不用真实 iosd 的集成调测

在项目目录运行：

```powershell
python -m unittest discover -s tests -v
python tools/make_fixtures.py
```

第二条生成微型 ELF 与 core：`tests/fixtures/generated/fixture-iosd.elf` 和 `fixture-iosd.core`。不含 Cisco 代码。

1. 用 IDA 打开 `fixture-iosd.elf`，运行 `dev_load.py`。
2. 概览应显示 `.text`、`.rodata` 和 `subsys_header_section`（具体段名由 ELF loader 决定）。
3. 运行子系统扫描，指针编码选 `little`：应有 `fixture_subsystem`，init 候选地址 `0x401000`。若 loader 没保留自定义段名，可手工指定 `[0x402200, 0x402238)`。
4. 源码路径扫描应找到 `VIEW_ROOT/cisco.comp/parser/src/fixture.c`。
5. 切换内存源到 `core`，选择生成的 core。
6. 设置映射：IDB RVA 0 基址 `0x400000`，运行时 RVA 0 基址 `0x555555554000`，锚点 IDB 地址 `0x402040`。应验证通过。若 IDA 自行 rebase，使用实际 IDB 基址和锚点。
7. 节点检查的起点填写 **运行时节点地址** `0x555555564000`，布局选 `profiles/icm_conservative.json`。应得到文本 `show fixture`；handler 显示 `unresolved`。
8. 内存读取 `0x555555565000`，应提示 core 页面没有被收录，而不是读出零。
9. 导出 JSON，检查 `raw_hex`、layout、mapping 和读取错误。这个 fixture 不包含消息模型符号，因此符号分类结果为空是正常的。

## 真实 iosd 实时调试

1. 打开匹配的 iosd IDB，配置你现有的远程调试连接并 attach；插件不代替调试服务器，也不自行 attach。
2. 暂停目标。选择 `debugger` 内存源；未暂停时插件拒绝读取。
3. 核对 iosd 的实际加载映射，然后设置地址映射并使用已知字符串验证。文档中的 `0x555555554000` 只是一次观察，插件不硬编码该值。
4. 先用 Memory probe 比较 IDA debugger memory view 与插件输出的同一段 72 字节。
5. 已知树根槽时，先读取槽并选择正确编码；根结构仍不等于第一个节点。通过已验证的数组/链字段找到第一个节点后，再进行节点检查。
6. 先检查一个节点，再验证下一个节点，最后才开启多节点遍历。暂停期间采集；跨线程状态与 attach 前已发生的变化仍需研究者判断。

## 真实 core 调测

1. 保存设备提供的 core 与准确对应的 iosd 文件/版本信息；解压 core。
2. IDA 打开该 iosd 的 IDB；切换插件内存源为 `core`。
3. 检查 core 映射列表。映射列表里的地址都是运行时 VA，`Captured < Mem size` 表示有未收录的内存范围。
4. 手工设置加载基址并完成锚点验证。它只验证一个局部位置，**不证明整个文件与 core 完全匹配**。
5. 读取已知全局槽、节点，再进行有边界的遍历。若树根为零，应先判断抓取时机和结构生命周期；不自动扫描堆猜根。

core 的堆 VA 不一定在静态 IDB 里有对应地址，因此双击堆节点主要打印原始证据，不会伪造 IDB 段。转换后的地址只有落在现有 IDA 段中才尝试跳转。

## CLI 布局与文档冲突

2026-10-28 经 MCP 读取当前 IDB，并检查 `sub_C2F7B50` 和 `sub_C2FA1D0`，已否定旧布局中的 `+0=命令串`、`+8=handler` 假设。`+0` 用于下降到子节点，`+16` 用于向上回溯，`+24` 用于同级遍历，`+8` 在插入过程中参与树链维护。这里没有建立主 CLI 命令到处理函数的映射。

文本指针为大端存储的 tagged pointer，应先按大端解码再去掉最高标记位，即 `swap_then_mask`。`+56` 标志没有 `0x40` 时，打印函数将 `+48` 作为直接 C 字符串；有 `0x40` 时结合 `+60` 起始偏移与 `+64` 结束偏移，文本长度为 `end - start - 1`，不写入原程序打印时临时更改的换行字节。若还设置 `0x80`/`0x100`，缓冲区指针分别来自根结构 `+48`/`+8240` 的索引数组，不能盲读节点的 `+48`。

对应 profile：

- `icm_conservative.json`：使用上述打印路径语义检查单个节点，handler 保持未解析，不跟随链接。
- `icm_print_observed.json`：同样的文本策略，另外沿 `+0/+24` 遍历。指向这里的树根和起点仍需单独确认。
- `icm_hypothesis_legacy.json`：已停用，选择后明确报错，保留文件仅用于追溯旧假设。

需要数组间接取文本时，在 profile 中填写 `tree_root` 为所选数据源中的实际根地址；缺失时返回明确的 `text_error`，不回退到错误的 inline 指针。这些字段规则由静态代码支持，但尚未在真实运行时快照中验证。

通用布局仍支持 `little`、`big`、`mask_then_swap`、`swap_then_mask` 四种指针编码和自定义字段。`icm_print_observed` 策略专门用于上述 ICM 结构，不代表其他表也使用相同字节序。文本长度上限、节点上限、环检测和读取错误会限制错误布局造成的影响。

ICM 扫描以**第一个节点地址**为输入，不把文档里的 diff 临时根 `0x37B5323C` 自动当成主命令树根。静态 CLI 提取使用单独的注册表/transition 入口；全量命令恢复仍需要更多动作、链接关系、注册路径和模式语义。

## 测试覆盖与后续验证

本机单元测试覆盖合成 ELF/core、跨 PT_LOAD 读取、未捕获页面、截断文件、重叠映射、地址转换、字节序和 mask 顺序、节点循环/数量上限/取消/部分失败、子系统候选、静态动作表布局、EOL/NVGEN 区分、参数范围、谓词 false 边、注册参数发现的控制流边界、root 覆盖统计及 rebase 拒绝。0.3.0 当前 41 项测试通过。

真实 IDA 界面、实时调试后端及 Cisco 实际 core 需要按上述步骤实测。本机测试通过不代表已验证完整 iosd 结构。插件每次只导出最近一次操作结果；当前不提供跨会话结果缓存。

API 参考：[IDA 插件接口](https://python.docs.hex-rays.com/ida_idaapi/index.html)、[原生界面](https://python.docs.hex-rays.com/ida_kernwin/index.html)、[调试内存读取](https://python.docs.hex-rays.com/ida_idd/index.html)。
