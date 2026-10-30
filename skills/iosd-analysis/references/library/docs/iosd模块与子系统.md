# iosd 模块 子系统与初始化架构

> 历史分析资料：保留样本、条件和未知项。原始捕获及 GUI 实验不随 skill 分发；历史材料路径用于定位已有证据，不表示文件已包含。


在当前 C8000v 26.01.02 样本中，**subsystem 和 `module_header/link` 是两套不同的初始化组织机制**。subsystem 以有名称、类别、入口及属性的注册实体组织功能；module 机制用有名称的分组、回调节点和链接组织另一张初始化关系图。启动代码会分别推进两套机制，不能直接画成“每个模块下面包含若干子系统”。

这里的结论绑定输入 MD5 `9eccfd46caadfff9c18557e2a446e19b`。文中函数和数据地址均写作 RVA，rebase 后需加当前映像基址。

## 模块这个词对应三种对象

| 用法 | 实际对象 | 与 subsystem 的关系 |
|---|---|---|
| 功能模块，例如某协议或管理能力 | 研究人员按职责整理的功能集合 | 一个功能可能涉及多个 subsystem、公共设施和库；需要具体证据关联 |
| 文件模块，例如主 ELF 和某个 `.so` | 代码和数据的装载容器 | 一个容器可以提供多条 subsystem 记录；实际 init 和回调所在文件分别定位 |
| `module_header_section` 中的 module | 当前样本的 32 字节描述符及其初始化图节点 | 通过 module link 组织分组和依赖；不能按名字与 subsystem 配成父子关系 |

`level_protocol` 是第三种用法中的一个分组描述符；Protocol 是 subsystem 的类别。两者名称相近，但分别由不同的数据结构和执行入口使用。

线程入口里的 `*_thread_level` 还有另一种具体含义：当前已核对的消费者 `D714A10` 为数字 level 建立 Interrupt Stack 和执行上下文，线程创建侧再设置 pthread 栈。它与 module 的 `level_*` 分组分别记录。七条 Linux 线程的创建者、循环、库边界和编号区别见 [iosd 的线程 任务与 level](iosd的线程与level.md)。

## subsystem 是功能注册与初始化实体

主映像的相关记录区间为 RVA `0x37A014C8` 至 `0x37A86B48`。`sub_D7127D0` 的普通路径按 96 字节步长遍历它们，并把记录交给回调。`sub_D710240` 检查版本、读取类别和属性，把记录加入类别容器或 Pending；`sub_D710BC0` 解析属性中的名字并处理依赖顺序。

当前扫描保留 5,692 条候选记录、5,678 个不同名称。名称与 init 入口有助于找到功能入口，但记录本身没有给出“这个实体拥有从地址 A 到地址 B 的全部代码”。

init 的职责通常需要沿函数逐条确认：它可能注册 CLI 片段、消息处理函数、公共 registry 回调，或者建立业务对象和任务。这些都是不同的关联，不能只因函数可从 init 到达，就把它的全部下游代码独占归给该 subsystem。

分类初始化由 `sub_D711090` 等路径推进。13 个可见类别包括 Kernel、Library、Driver、Protocol、Management、Registry 和 SystemInit。类别编号不是完整的执行顺序，Pending 也不是线程列表。

## module 是分组与回调节点组成的初始化图

当前主映像有 15 条 module header：14 个 `level_*` 和 `memtest`。其中包括 `level_protocol`、`level_driver`、`level_rtl_loader`、`level_pre_config` 等；这组名称和 subsystem 的 13 个类别并不完全相同。

`sub_D771E60` 创建名为 `Module discovery scratch pad list` 的发现容器，并建立 `Root level` 和 `Root child list`。`sub_D772690` 按名字查找或建立运行时节点，其分支揭示了两种对象：

| header 内容 | 已核对的处理方式 | 解释 |
|---|---|---|
| `+0x10` 非零 | 建立 88 字节节点，将 header 的 `+0x10/+0x18` 复制到节点 `+0x48/+0x50` | 带回调的节点；`+0x48` 在初始化路径中被调用 |
| `+0x10` 为零 | 建立 176 字节节点，在节点 `+0x48` 初始化列表 | 分组节点，下面可以组织其他节点 |

`level_*` 的两个字段在当前静态记录中均为零，因此它们属于后一种分组。`memtest` 的字段分别指向 RVA `0xD79CF90` 和 `0xD79D000`，属于带回调的节点。第一个字段已沿复制和调用链确认用于初始化；第二个字段的完整消费路径尚未核对，继续保留为第二回调，不直接命名为析构或退出函数。

这说明 `level_protocol` 更接近初始化图中的分组入口；`memtest` 则提供实际工作回调。它们都不等于一个独立 Linux 进程或一段连续代码。

## 两种 module link 的含义

24 字节 link 的 `+8/+16` 分别是端点 A 和 B。这里区分“原始字节按小端显示的 tag”和“消费者字节交换后用于 switch 的逻辑 tag”，避免把两个表示误认成两套记录。

| 原始 tag 小端读数 | 消费者逻辑 tag | 消费代码支持的关系 |
|---|---|---|
| `0xDFEADFEA` | `0xEADFEADF` | A 的前置依赖列表加入 B |
| `0xABEFABEF` | `0xEFABEFAB` | A 的分组指针设为 B；B 必须是分组对象 |

第一类由 `sub_D7705B0` 处理，第二类由 `sub_D7703A0` 处理。随后 `sub_D772AA0` 递归处理依赖、检查冲突和环相关状态，并把节点加入相应分组的子列表。这里可以确认初始化组织中的依赖和分组关系，不能据此推出业务调用关系或报文流向。

当前 11 条 link 中，10 条是前置依赖。例如原始记录的 A=`level_protocol`、B=`level_driver`，表示前者的依赖列表引用后者。另 1 条是 `memtest` 到 `level_protocol` 的分组关系，因此**可以确认 memtest module 节点归入 level_protocol module 分组**。这句话说的是 module 图内部关系，没有把任何 subsystem 放到该分组下面。

`sub_D771350` 按给定 header 的名字查找分组节点，准备 `Module init scratch pad list`，再调用 `sub_D7715A0`。后者在相应路径上调用带回调节点的 `+0x48`。这条链把静态 header、运行时节点和实际初始化回调关联起来。

## 两套机制怎样共同出现在启动过程中

主初始化的一段已核对路径为：

```text
准备 module 发现容器                     D771E60
    ↓
发现 subsystem，并分派 module 描述符     D710460 → D7127D0
    ↓
整理 module 发现结果                    D772050
    ↓
推进 subsystem 的 SystemInit 类别       D711090(7)
    ↓
后续初始化路径分别推进类别与 module 分组
```

`sub_D7127D0` 在同一次元数据发现过程中做了不同的事：subsystem 记录交给传入回调；module header/link 交给 `sub_D771FA0` 按 tag 分派。共享一个发现入口，并不代表它们共享同一记录布局或存在包含关系。

后续 `sub_E0E33E0` 有更直接的例子：调用 `sub_D711090(4)` 推进 Protocol 类别后，调用 `sub_D771350`，参数为 `level_protocol` header；Driver、Library 等也有相似的配合点。它表达的是启动流程中两套机制的协调，具体路径仍受外层条件控制。

因此，可以画出这样的关系：

```text
启动编排
  ├─ subsystem 机制：类别 → 候选注册实体 → init
  └─ module 机制：分组 + 依赖 → 回调节点 → init 回调

同一启动阶段可依次推进两者；不是模块包含子系统的目录树。
```

目前尚未建立每个 subsystem 与 module 节点的完整交叉关系。若某 subsystem init 实际注册或调用了某 module，应新增有调用位置的关系；不能凭 `protocol`、`driver` 等同名词生成这种关联。

## 从这些机制理解 iosd 的组织方式

从已观察实现可以归纳出三个设计特点：

首先是**用元数据驱动发现和初始化**。功能入口不必全部写进一个巨大的直接调用列表；程序通过记录、回调和依赖来组织它们。其次是**将启动编排与具体业务工作分开**。类别、分组和依赖用于安排工作，协议解析和状态更新还要继续进入具体回调。第三是**用注册和分派连接功能**。CLI、消息、registry 和协议处理入口可以是不同接口，分析时需要保留它们各自的类型。

这些是对当前样本机制的归纳，不是对厂商源代码设计目标的引用。它们解释了为什么“找到所有名字”仍不足以理解整个程序：真正需要恢复的是对象之间的关系及其条件。

## 协议处理代码位于哪里

subsystem 的类别和 module 的分组都不能直接回答报文由谁解析。需要从输入接收、消息分派或注册表定位实际回调，再核对缓冲区、长度、消息类型和状态更新的使用路径。

如果处理函数的机器码在 iosd 的代码区，实际实现就在当前 ELF；即使其源码最初属于一个库，静态链接后仍是当前文件里的代码。若经过导入或间接调用，则继续核对重定位、GOT 和运行时目标所属 `.so`。PLT 跳板位于主 ELF，不代表最终实现也在主 ELF。若路径跨越 IPC，发送方只能解释接口的一半，接收进程中的分派和处理代码需要另外取得。

`sub_D7127D0` 还检查名字中含 `libiosd_shr_` 或 `libiosd_crb_shr_` 的已登记对象，并检查其中的记录。这说明发现机制具备从相关外部对象取得注册记录的路径；它不证明这些对象在每次运行中都存在，更没有说明某个协议一定由某个 `.so` 实现。

面向研究者的程序应分别显示文件归属、初始化归属、功能关联和输入处理路径，并保留未知边界。当前 CLI 恢复结果可以挂在“注册接口”下面，不能代表子系统的全部职责。

配置生成也体现这种职责区分：subsystem/module 负责的初始化组织，不等于 NVGEN 遍历的对象清单。当前已沿配置模式语法、对象迭代器和生成回调找到状态到文本的路径，并确认部分 CLI handler 同时承担生成职责。具体实现及接口配置缓存见 [iosd 的 NVGEN 与接口配置缓存](iosd的NVGEN与接口配置缓存.md)。

## EHSA 的实际例子

`ehsa_background_monitor` 的 init 创建 peer monitor 任务并注册 KEEPALIVE 接收回调；`ehsa_fsm` 的 init 创建状态机任务和消息队列；`platform_ehsa` 的 init 安装平台策略，其中一项切换请求回调受能力键控制。这些是明确的初始化与注册连接，不代表其中一个 init 拥有全部共享函数。

`level_ehsa` 和 `level_pre_ehsa` 则是 module 分组。已审查依赖表示 `level_ehsa` 需要 `level_pre_ehsa`，后者需要 `level_ucode`；启动编排分别推进类别与分组。不能据此生成“level_ehsa 包含所有 EHSA 类别子系统”的成员边。

心跳和状态机函数体已定位于主 ELF；Chasfs 的部分实际绑定入口位于 `libchasfs.so`。同时，名为 `REDUNDANCY FSM` 或 `CMAN RP Msg Process` 的对象经 IOS 任务创建设施建立，名称中的 Process 不足以证明它是一个独立 Linux PID。完整调用、条件和跨进程未知边界见 [iosd 的 EHSA 心跳与主备状态机](iosd的EHSA心跳与主备状态机.md)。

## 原始证据

- module header 和 link 原始记录（历史材料路径：`../reports/mcp-plugin-module-result.json`）。
- 元数据发现 D7127D0（历史材料路径：`../reports/mcp-module-init.json`） 与 tag 分派 D771FA0（历史材料路径：`../reports/mcp-module-dispatch.json`）。
- subsystem 分类 D710240（历史材料路径：`../reports/mcp-start-callback.json`） 与 属性依赖 D710BC0（历史材料路径：`../reports/mcp-subsys-pending.json`）。
- module header 消费者（历史材料路径：`../reports/architecture-module-review-20261029/rva_d770200.json`）、分组链接消费者（历史材料路径：`../reports/architecture-module-review-20261029/rva_d7703a0.json`）、依赖链接消费者（历史材料路径：`../reports/architecture-module-review-20261029/rva_d7705b0.json`）。
- 运行时节点构造 D772690（历史材料路径：`../reports/architecture-module-review-20261029/consumers/rva_d772690.json`）、发现容器 D771E60（历史材料路径：`../reports/architecture-module-review-20261029/consumers/rva_d771e60.json`） 与 发现结果处理 D772050（历史材料路径：`../reports/architecture-module-review-20261029/consumers/rva_d772050.json`）。
- 按分组初始化 D771350（历史材料路径：`../reports/architecture-module-review-20261029/execution/rva_d771350.json`）、实际初始化回调 D7715A0（历史材料路径：`../reports/architecture-module-review-20261029/callbacks/rva_d7715a0.json`） 与 依赖及分组整理 D772AA0（历史材料路径：`../reports/architecture-module-review-20261029/callbacks/rva_d772aa0.json`）。
- 启动路径中的两套初始化调用 E0E33E0（历史材料路径：`../reports/architecture-module-review-20261029/consumers/rva_e0e33e0.json`）。新采集仅查询匹配 IDB 的小函数反编译，没有执行目标函数或读取目标动态内存。
