# iosd 的 EHSA 心跳与主备状态机

> 样本分析资料：保留适用版本、条件和未知项。原始捕获保留在本地；标注的历史材料路径用于定位来源。


当前 C8000v 26.01.02 样本中，EHSA 的核心心跳、消息分派、监测任务和主备协商状态机都在 iosd 主 ELF 内。它通过 registry 回调接入平台策略，通过外部库访问 Chasfs 和平台设施。理解它需要同时看三件事：**对端是否还活着、当前协商处于哪一步、平台允许采取什么动作**。

Cisco 在冗余调试命令说明中将 EHSA 展开为 Enhanced High System Availability，并将其放在 Redundancy Facility（RF）的语境下。这能解释术语，不能替代当前版本的实现证据。[Cisco debug redundancy RP](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/debug/command/m1/db-m1-cr-book/db-q1.html)

这里所有主 ELF 地址均为 RVA，绑定输入 MD5 `9eccfd46caadfff9c18557e2a446e19b`。当前 IDB 基址为 `0x555555554000`；在 IDA 中跳转时使用基址加 RVA。分析使用保存的 IDB 字节、反编译和原 ELF 元数据，另对七个 GOT 槽各补读八字节，核对本次 attach 的库绑定。没有暂停、恢复目标或执行目标回调，也没有进行故障注入。

## 从整体看各部分怎样协作

```text
对端发来的 bootstrap 消息
  → iosd 的接收分派 D51E0E0
    ├─ 类型 30 KEEPALIVE → registry → D512810
    │                       → 重置监测 / 排入 peer monitor 队列
    └─ BOOT、ACK、INITED 等 → FSM 事件队列

peer monitor D510B80
  ├─ 定时发送类型 30 → D51CE00 → 传输回调 → 接口输出回调
  └─ 检测失联 → raw event 7 → D50F450 过滤和平台策略
                                → D5194D0 → FSM 队列

FSM 任务 D519FC0 → D51A4E0 → D51A800 → 通用表驱动引擎
  → 当前状态 + major/minor → 动作回调 + 后续状态
  → 必要时进入主备切换编排 D5156E0

平台适配 platform_ehsa
  ├─ 安装策略、故障和角色回调
  ├─ 条件满足时发布 notification / stby-request-swo
  └─ 消费 rfrole 等平台事件和属性
        ↔ libchasfs.so / 平台运行时 ↔ 外部消费者（尚未闭合）
```

这条结构说明了为何心跳日志不能直接等同于最终切换结果。发出报文、收到回应、检测到失联、将事件提交给状态机、完成平台切换，是不同步骤。每一步都可能有状态条件、排队或外部回调。

## 对应哪些子系统和 module

子系统记录给出初始化入口；它不天然拥有入口所调用的全部代码。下面把记录直接证实的关系与后续调用链分开理解。

| 子系统 | 类别 | init RVA | 已核对的具体连接 |
|---|---|---|---|
| `ehsa_background_monitor` | 8 EHSA | `D511200` | 创建 peer monitor 队列、定时器和任务；将 `D512810` 注册到消息类型 30 |
| `ehsa_common` | 8 EHSA | `D516930` | 安装通用 EHSA 回调，包括原始故障原因记录回调 `D517460` |
| `ehsa_fsm` | 8 EHSA | `D519D30` | 创建 FSM IPC、peer monitor、NPLUSM_B2B 队列和 `D519FC0` 任务 |
| `ehsa_ha` | 8 EHSA | `D51C8E0` | 注册角色查询和 CLI/TTY 相关 HA 回调；不能单凭名字把它当作全部切换逻辑 |
| `platform_ehsa` | 8 EHSA | `D52C3A0` | 安装平台策略和故障接口；有条件地注册 `D52D8D0` |
| `mcprp_ehsa_chain` | 5 Management | `D5287E0` | 提交解析器链，并安装其他平台回调 |
| `mcprp_peer_timeout` | 12 Pre-EHSA | `E949490` | 注册一组 CLI 描述符；关联的设置处理函数为 `E9492B0` |
| `cmanrp` | 8 EHSA | `E34FAC0` | 平台初始化及部分分支中的 `CMAN RP Msg Process` 内部任务创建 |
| `mcprp_red` | 8 EHSA | `15853F60` | 初始化冗余调试和 CLI 相关入口；`rfrole` 消费函数另有调用点证据，不按地址相邻自动归属 |

此外，`ehsa_reg`、`platform_ehsa_registry` 等记录属于 Registry 类别，`ehsa_issu` 与 RF 相关实体还承担其他协作职责。类别 8 的含义是初始化编排中的 EHSA 类别，里面并不全是心跳组件。已有架构图保存了该类别 138 条候选记录、Pre-EHSA 类别 45 条候选记录。

module 是另一套初始化机制。`level_ehsa` header 在 `0x37A8F980`，`level_pre_ehsa` 在 `0x37A8FA20`。已核对的依赖表示：`level_ehsa` 需要 `level_pre_ehsa`，后者需要 `level_ucode`；`level_pre_driver` 又需要 `level_ehsa`。启动编排 `E0E33E0` 在相应条件下分别推进类别 12、类别 8，再推进对应 module 分组。

这些是阶段协调和依赖关系，不能改画成“level_ehsa 包含上表所有子系统”的目录树。类别、module、函数所在 ELF、Linux 进程和 IOS 内部任务需要分别标注。

## 心跳怎样发送

`D510590` 是启用心跳的一处入口。它在参数允许时调用 `D51CE00(30, 0, 0, 1)`，并启动发送定时器；`D510B80` 的定时器事件分支负责后续周期发送。其他路径如 `D512240` 也有受门控的发送，不能把唯一出现的调用位置当成全部发送者。

消息类型 30 的含义由接收分派中的 `KEEPALIVE` 字符串和对应分支共同确认。这个数字属于 EHSA bootstrap 消息域，不是用户 CLI 的命令编号。

`D51CE00` 分配 packet，准备 bootstrap 头，设置消息类型、长度及标志，然后调用传输槽 `0x381459E0 + 0x10`。错误分支中还有 `send_ipc_bootstrap` 的诊断文字。`D51D780` 在槽为空时装入默认发送函数 `D51DBC0`；保存的 IDB 槽也指向它，但这不代替一次新的现场槽快照。

默认函数 `D51DBC0` 在 iosd 中准备二层封装、地址和输出相关字段，之后调用接口对象的 `+0x638` 和 `+0x618` 回调。这两个具体运行时目标还没有恢复。因此目前能追到**iosd 的报文输出接口**，尚不能指定最终驱动、虚拟接口实现或硬件出口。

日志 `Sent keepalive` 出现在发送调用之前，发送封装也有分配失败和传输丢弃路径。仅见这条日志不能证明报文已经离开设备。

## 心跳怎样接收并刷新监测

初始化 `D51D780` 将 `D51E0E0` 安装到 bootstrap 接收分派接口。分派器按消息类型处理 RESTART、BOOT、INITED 和相应 ACK，其他类型还可以通过 registry 找回调。

`D511200` 通过 `D517EF0` 返回的索引注册设施，将 `D512810` 挂到类型 30。于是类型 30 形成这条间接但可核对的连接：

```text
D51E0E0 → 读取类型 30 → registry 查找 → D512810
```

`D512810` 的一条分支直接调用 `D511EE0`；另一条调用 `D510060(0, packet, free_callback, 2)`，提交 peer monitor 事件。队列消费者 `D5116F0` 在事件值 0 时也调用 `D511EE0`。这里传给队列的事件值与网络消息类型属于不同编号空间。

`D511EE0` 对计数器方式写入哨兵值 `-1`，或停止当前等待定时器；在相应分支中发送类型 30 回应，并按启用状态重新建立等待窗口。它不是无条件执行所有这些动作。停止心跳的 `D5104C0` 也会设置计数器哨兵或停止定时器。

peer monitor 还通过类型 20 `MASTER PARAMS`、类型 21 `MASTER PARAMS ACK` 交换参数。`D5116F0` 的参数处理分支会改写等待计数和间隔，例如将报文中的一个字段乘以 2 写入 `0x3C8A1228`，将另一字段写入 `0x3C8A122C`。因此默认常量不能代表最终协商结果。

## 超时检测和故障处理

可以把检测过程理解为“发送时建立等待窗口，回应时刷新监测，窗口到期后产生失联事件”。当前代码有两种具体实现分支：

| 路径 | 已确认的检测逻辑 | 条件与限制 |
|---|---|---|
| 定时器方式 | `3C8A1390` 的类型 3 到期，向 `D524BD0` 取得的回调传入 `1000 × (N−1) × I`；回调不放行抑制时产生 raw event 7 | 等待窗口通常按 `1000 × N × I` 建立；N、I 还受协商和状态影响 |
| 计数器方式 | `D510B80` 的周期分支读取 `33E72DA0`，逻辑值大于 `33E72D90` 时产生 raw event 7 | 另有 `-1` 哨兵、接收重置和锁保护；这里不是简单的每包时间戳比较 |

其中 N 对应 `0x3C8A1228`，I 对应 `0x3C8A122C`；init 默认写逻辑值 18 和 1。它们是已审查代码中的初始值，当前运行值、任务调度延迟及协商后的有效时间均没有在本次采样。

`E9492B0` 还可以设置 peer EHSA timeout，更新 `0x3D22DEC4` 和计数阈值，并注册比较回调 `E949440`。后者比较 `1000 × 配置值 >= 传入值`，返回结果供检测路径决定是否继续。恢复默认的分支使用 18。精确 CLI 完整路径尚未在这一轮恢复；也不能只凭比较公式推算所有模式下的实际故障触发时刻。

raw event 7 的名字在 `D50F450` 中明确是 `KEEPALIVE_FAILURE`。此外还有 PEER_CRASHED、PEER_DOWN、PEER_WATCHDOG_INTERRUPT 等独立事件。`D512490`、`D512520`、`D5125B0` 分别对应 crash、watchdog、down 的致命对端中断入口，不能全部解释成普通心跳超时。

`D50F450` 会先通知过滤回调，再根据过滤后的事件与角色相关分支记录原因、调用平台动作，必要时通过 `D5194D0` 提交 `(major=2, minor=过滤后的 peer 状态)`。**进入过滤器的 raw event 7 不等于直接将数字 7 当成 FSM 事件索引。**

平台初始化 `D52C3A0` 有一个特别清晰的条件：当 `cyan_get_boolean(0, "CYANKEY_CHASSIS_ATTRS_EHSA_KEEPALIVE_FAILURE", 0)` 为真时，向相应 registry 槽安装 `D52D8D0`，并初始化 Chasfs 上下文。过滤器在相应失联分支会取这个槽的回调。

`D52D8D0` 检查并在需要时创建 Chasfs 属性：对象 `notification`，属性 `stby-request-swo`。这是平台切换请求的具体线索；发布属性本身不能证明外部消费者已经接收、批准或完成切换。

## 主备状态机怎样工作

外层 `D51A800` 将 EHSA 状态变量 `0x3C8A15B0`、表 `0x33E76820` 和 major/minor 事件交给通用引擎 `1E3F7360`。引擎先按当前状态选描述符，再通过 `D51AEA0` 将事件映射到槽位：

```text
(0,0)               → 索引 0
(1, minor 0..9)     → 索引 minor + 1
(2, minor 0..4)     → 索引 minor + 11
```

每个状态描述符 16 字节，指向 16 个事件表项；每项 24 字节，包含动作回调、动作参数、后续状态字段及保留字节。当前保存的描述符和动作表使用大端 tagged 指针；不能把它套用成 ELF 原生 GOT 的小端指针格式。

这一轮保留了全部 **14 × 16 = 224 个表项**，关联到 **19 个不同动作回调**。下一状态为 0 表示保持当前状态；null 动作也有意义，不会删掉。解码器还保留错误、特殊和不认识的值，不把所有非普通状态一律解释为不可达。

| 状态编号 | 代码中的名称 | 阅读含义 |
|---|---|---|
| 1 | `REDUNDANCY_SYSTEM_START` | 开始协商 |
| 2 | `REDUNDANCY_WAIT_ACTIVE_RESTART_ACK` | 等待 Active 的 restart ACK |
| 3 | `REDUNDANCY_WAIT_ACTIVE_BOOTACK` | 等待 boot ACK |
| 4 | `REDUNDANCY_WAIT_ACTIVE_INITEDACK` | 等待初始化完成 ACK |
| 5 | `REDUNDANCY_WAIT_STDBY_EHSA_ISSU_VERSIONING` | 等待 EHSA / ISSU 版本相关进度 |
| 6 | `REDUNDANCY_WAIT_SWITCHOVER` | 等待切换事件 |
| 7 | 名称未知 | 描述符和 16 个事件项仍保留 |
| 8 | `REDUNDANCY_PEERSTANDBY_NONOPERATIONAL` | 对端 Standby 尚不可工作 |
| 9 | `REDUNDANCY_PEERSTANDBY_DETECTED` | 检测到 Standby |
| 10 | `REDUNDANCY_PEERSTANDBY_INITWAIT` | 等待 Standby 初始化 |
| 11 | `REDUNDANCY_EHSA_ISSU_VERSIONING` | EHSA / ISSU 版本阶段 |
| 12 | `REDUNDANCY_PEERSTANDBY_INITED` | Standby 已初始化 |
| 13 | `REDUNDANCY_PEERSTANDBY_NOTPRESENT` | 未检测到 Standby |
| 14 | `ACTIVE_DONOT_RESPOND` | 代码原名；不能据名称推断全部拒绝条件 |

可以核对的一条表驱动链是：状态 2 收到 `(1,0)` 的 RESTART ACK 进入 3；状态 3 收到 `(1,1)` 的 BOOT ACK 进入 4；状态 4 收到 `(1,2)` 的 INITED ACK 进入 5。后续事件来源和动作条件需要继续沿生产者追踪，不能把这张表画成无条件顺序执行。

状态 1 至 7 的 `(2,0)` 表项会选中 `D51AF30` 并将状态字段设为 8。该动作进入 `D5156E0` 的 Standby→Active 编排。后者先检查准备条件，再通知多个 registry 和平台接口；准备不足的分支会报告 `Standby not capable of switchover yet` 并进入 reload 路径。**表项写入后续状态与切换最终成功是两件事**：通用引擎会在调用动作前更新表指定的状态字段。

状态 8 收到 RESTART 对应的 `(1,5)`，经 `D51B680` 进入 9；状态 9 收到 BOOT 消息对应的 `(1,6)`，通过 `D51BA00` 处理 BOOT ACK 并进入 10；状态 10 收到 INITED 对应的 `(1,7)`，经 `D51BCE0` 进入 11；状态 11 的 `(1,8)` 项经 `D51BE10` 进入 12，但 `(1,8)` 的完整事件生产链尚未闭合。

还存在表外的状态修改：`D51A4E0` 消费 NPLUSM_B2B connect ACK 的分支可以直接写状态 8。外层在状态变化后也会通知一组 registry 订阅者。故完整主备行为必须包含**状态表、事件生产者、动作中的条件、表外写入和外部平台状态**；只导出状态表仍不等于完整状态机证明。

## 哪些在 iosd 哪些在 so 和其他进程

| 层次 | 当前证据 | 能确认到哪里 |
|---|---|---|
| iosd 主 ELF | 本文列出的心跳、队列、过滤器、FSM 引擎和动作函数均有 `.text` 函数体 | 不是只根据函数名推断实现位置 |
| 同一进程的 Chasfs 库 | 四个 GOT 槽绑定到 `libchasfs.so` | 确认库范围和入口偏移；库内部及服务端尚未分析 |
| 同一进程的平台能力库 | `cyan_get_boolean` 绑定到 `libcyan.so` | 只确定此次绑定位置，未采样该能力键的实际返回值 |
| 同一进程的 iosd 平台运行时 | `__be_mcp_get_failover_reason`、`__be_mcp_stop_nplusm_b2b_fd` 绑定到 `libiosd_crb_vxe_unix.so` | 这两项入口已定位，不能据此把所有 MCP 函数都归入该库 |
| IOS 内部任务 | `REDUNDANCY peer monitor`、`REDUNDANCY FSM`，以及特定分支中的 `CMAN RP Msg Process` 经任务创建设施建立 | 任务入口在主 ELF；到 Linux 线程/TID 的完整映射尚未建立 |
| 外部管理与对端系统 | Chasfs 属性、CMAN/PMAN 时间戳和对端消息提供交互线索 | 精确消费者进程、PID、外部状态机与对端代码仍未知 |

此次 GOT 绑定的库内偏移为：

| 导入符号 | 实际模块范围 | 库内偏移 |
|---|---|---|
| `cyan_get_boolean` | `libcyan.so` | `0x2E20` |
| `chasfs_initialize` | `libchasfs.so` | `0x54D0` |
| `chasfs_property_get_string` | `libchasfs.so` | `0x7EE0` |
| `chasfs_property_present` | `libchasfs.so` | `0x6D30` |
| `chasfs_property_create` | `libchasfs.so` | `0x6730` |
| `__be_mcp_get_failover_reason` | `libiosd_crb_vxe_unix.so` | `0x9E690` |
| `__be_mcp_stop_nplusm_b2b_fd` | `libiosd_crb_vxe_unix.so` | `0xAA190` |

这是 GOT 原生小端地址与模块范围的匹配，目标读取时仍在运行，并非原子快照或导出符号反汇编证明。它不证明这些入口当时被执行，也不保证其他版本的偏移相同。

iosd 中的 `158531C0` 会消费 Chasfs `rfrole`，识别 `peer_active`、`peer_standby`、`become_active`、`became_active` 和 `undefined` 等值。它更新平台状态、调用相关 registry 和后续动作，但不是这张 EHSA 状态表的同义替代。它的回调引用位于 `E3374B0`；该大函数的完整注册和事件循环本轮没有全部展开。

`E3887B0` 的诊断输出还会读取 `ts_cman_rcv_rpswitch_ehsa`、`ts_pman_rcv_sigusr1` 等时间戳。它们证明诊断设施区分这些阶段，不能单独证明哪个 PID 消费 `stby-request-swo`，也不能证明外部进程代码就在 iosd 中。

## 保留的未知关系与继续分析的入口

状态 7 的名称、部分 major/minor 事件的完整来源、registry 中全部订阅者，以及默认发送函数里的两个接口回调，仍保留为未解析。RF 状态、EHSA 状态、ISSU 进度和平台角色字段也分别保留，没有按数值强行合成一个枚举。

若要闭合跨进程切换链，需要取得与当前运行版本对应的 `libchasfs.so`、平台运行时和 Chasfs 属性消费者，沿 `notification/stby-request-swo` 查到接收、仲裁和结果发布代码。若要核对当前设备的实际 EHSA 状态，需要在合适的暂停现场读取状态变量、任务、定时器和 registry，再与这些静态可能性对照。状态表里的零项、未知项及表外写入都应继续保留。

用户之前给出的 CSCvt29004 讨论涉及其他平台/版本，不能用来认定本样本存在同一缺陷，也不能从本样本的单条超时分支解释那次故障的根因。

## 证据和离线复核

- 可检索的完整状态事件表（历史材料路径：`../reports/ehsa-implementation-20261029/index.html`）、224 个表项 JSON（历史材料路径：`../reports/ehsa-implementation-20261029/fsm-cells.json`）。
- 原始状态表字节和 mask（历史材料路径：`../reports/ehsa-implementation-20261029/fsm-tables.json`）、描述符、传输槽和导入元数据（历史材料路径：`../reports/ehsa-implementation-20261029/tables-and-imports.json`）。
- 心跳字符串与函数交叉引用（历史材料路径：`../reports/ehsa-implementation-20261029/heartbeat-string-xrefs.json`）、peer monitor（历史材料路径：`../reports/ehsa-implementation-20261029/heartbeat/rva_d510b80.json`）、消息分派（历史材料路径：`../reports/ehsa-implementation-20261029/actions/rva_d51e0e0.json`）。
- 故障过滤（历史材料路径：`../reports/ehsa-implementation-20261029/dispatch/rva_d50f450.json`）、FSM 通用引擎（历史材料路径：`../reports/ehsa-implementation-20261029/dispatch/rva_1e3f7360.json`）、切换编排（历史材料路径：`../reports/ehsa-implementation-20261029/heartbeat/rva_d5156e0.json`）。
- 平台条件注册（历史材料路径：`../reports/ehsa-implementation-20261029/init/rva_d52c3a0.json`）、Chasfs 请求发布（历史材料路径：`../reports/ehsa-implementation-20261029/dispatch/rva_d52d8d0.json`）。
- 原 ELF 依赖与重定位（历史材料路径：`../reports/ehsa-implementation-20261029/elf-boundaries-indexed.json`）、七项 GOT 实际绑定（历史材料路径：`../reports/ehsa-implementation-20261029/runtime-got-bindings.json`）、已加载模块清单（历史材料路径：`../reports/ehsa-implementation-20261029/loaded-modules.json`）。

离线重建：`python tools/build_ehsa_report.py reports/ehsa-implementation-20261029`。它校验样本身份、完整字节 mask、描述符指针与动作函数证据，并保留全部表项；不会连接 IDA，也不会运行目标。样本知识入口另存 `profiles/ehsa_26_01_02.json`，不声称是跨版本通用运行时检测器。
