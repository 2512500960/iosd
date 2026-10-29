# iosd 的线程 任务与 level

> 历史分析资料：保留样本、条件和未知项。原始捕获及 GUI 实验不随 skill 分发；历史材料路径用于定位已有证据，不表示文件已包含。


你在 IDA 中看到的是同一个 iosd Linux 进程的七个执行线程。当前现场的线程名、TID 与运行时内部线程表已经对上；它们提供不同的执行环境，通过队列、事件、信号和回调承接工作。subsystem 描述功能的注册与初始化，module 的 `level_*` 描述初始化分组；这些对象需要分别理解。

以下结论绑定 C8000v 26.01.02、输入 MD5 `9eccfd46caadfff9c18557e2a446e19b`。主 ELF 地址使用 RVA；so 地址使用“库名 + 库内偏移”。现场读取没有切换线程、暂停或恢复目标，也没有执行目标函数。运行目标的分次读取不是原子快照。

## 这七行分别是什么

列表中十进制与十六进制两列是同一个线程 ID 的不同表示，例如 `15400 = 0x3C28`。这些 TID 会随重新启动而变化，不能写成插件定位规则。

| 本次 TID | IDA 名称 | 内部角色与已确认的工作 |
|---:|---|---|
| 15352 | `x86_64_crb_linux_iosd_vxe-universalk9-ms` | 内部表命名为 `IOS Thread`；现有主执行线程在创建路径中被登记，承担 IOS 启动与调度环境 |
| 15395 | `Fastpath Thread` | 事件处理线程；入口建立 epoll 设施，分派 IPC、输入/输出就绪事件及相关回调 |
| 15396 | `Packet Thread` | 报文相关 I/O 与事件处理；等待 epoll，读取就绪事件，处理已登记通道和后续回调 |
| 15397 | `Auxiliary Threa` | 内部完整名称 `Auxiliary Thread`；等待辅助请求，出队并调用请求回调，也有日志处理分支 |
| 15398 | `Sim Aux Thread` | 配置模拟相关辅助执行环境；有请求队列、模拟开关、文件操作和错误恢复相关逻辑 |
| 15399 | `Worker thread 1` | 通用工作池的第一个 worker；从工作队列取任务并执行任务函数 |
| 15400 | `Worker thread 2` | 同一工作池的第二个 worker；具体业务由提交的任务决定 |

Fastpath 的已审查入口是一个事件循环。名字不能证明整机所有转发包都由它处理，也不能把它直接等同于独立转发进程或某种硬件转发单元。Packet 的具体报文类型、Fastpath 的每个 I/O 注册者，都还需要从各入口继续追。

辅助线程里的 Sim 与程序中 `llvmclonedsim` 等路径有关；线程存在本身不能证明当前所有处理都处在模拟模式。普通创建函数会在原子配置能力和进程名等条件满足时启动它；是否执行某一模拟分支，需要另查当前状态。

IDA 列表里的 `Running` 是调试器给出的线程状态，不是 CPU 利用率测量。代码中的 `epoll_wait`、`pthread_cond_wait` 都有等待路径；不能据这七行推断七个线程正在持续占用七个 CPU。

## 谁创建它们

主执行线程先进入已有启动链：ELF 入口、libc 启动包装、`__be_pcohort_main_proxy`、应用回调，再到主初始化 `D7B7690`。在 `D7B7690` 中，可以看到：

```text
D7B7690 系统初始化
  → 1583D9A0 平台执行环境准备
    → E8D8040 等内存与运行环境准备
    → E8E8380 IOSXE Process / Queue 结构准备
    → __be_mcp_spawn_threads
        实际绑定 libiosd_crb_vxe_unix.so + 0x98010
```

这个创建调用位于该路径中 module 发现、subsystem 记录遍历及 SystemInit 分类推进之前。线程基础设施先建立，后续功能再把回调和任务接入已有执行设施；不能将每条 subsystem 记录当作一次 Linux 线程创建。

`__be_mcp_spawn_threads` 首先使用 `pthread_self` 登记现有 IOS 主线程，随后准备其他线程。已核对的普通路径包括：

| 线程 | 创建侧函数或设施 | 传给 pthread 的入口 |
|---|---|---|
| IOS 主线程 | `pthread_self` 登记现有线程 | 此处没有再创建一个 IOS 主 pthread |
| Fastpath | `libiosd_crb_vxe_unix.so + 0x98010` 中的 `pthread_create` | 同库 `+0x98660` |
| Packet | `__be_mcp_init_pkt_thread`，同库 `+0xD2DB0` | 同库 `+0xD2F80` |
| Auxiliary | `__be_mcp_init_aux_thread`，同库 `+0xE77A0` | 同库 `+0xE79C0` |
| Sim Aux | `__be_mcp_init_sim_aux_thread`，同库 `+0x119FE0`，受创建条件控制 | 同库 `+0x11A1F0` |
| Worker 1/2 | `binos_init_thread_pool`，本次绑定 `libthpool.so + 0x2530` | `libthpool.so +0x31C0` |

这里区分了两个阶段：iosd 调用线程基础设施，以及外部库实际调用 pthread API。主要线程入口在 so 中；这不妨碍它们通过导入、队列或函数指针执行主 ELF 中的业务回调。

还发现一个不同场景的入口：主 ELF `16580C40` 在原子配置的子进程准备路径中调用 `__be_mcp_spawn_child_threads`。它与普通启动函数分别记录，不用它解释当前七个线程全部的来源。

## Fastpath Packet 与辅助线程如何接工作

Fastpath 入口 `libiosd_crb_vxe_unix.so +0x98660` 创建和使用 epoll 对象，调用 `__be_iosd_process_ipc_entry_epollq`、`__be_iosd_process_epollin_ret_fds`、`__be_iosd_process_epollout_ret_fds` 等分派入口。另有 `__be_iosd_signal_fastpath_thread` 使用 write 唤醒相关设施。这些证据支持“事件处理与分派环境”的解释，尚未穷尽其全部消费者。

Packet 入口 `+0xD2F80` 同样使用 epoll、唤醒 FD、通道状态和平台 select loop 相关接口。它与 Fastpath 各有统计和控制结构，不是同一个线程的两个别名。捕获的是有限代码范围；不能据此宣布全部报文接收、发送或协议解析路径都已恢复。

Auxiliary 入口 `+0xE79C0` 等待条件变量，检查请求队列和日志相关标志。它通过 `__be_mcp_auxthd_req_dequeue` 从主 ELF 的队列接口出队，取得请求记录中的函数指针，再执行请求并通知等待者。主 ELF 对应的出队/入队入口为 `E923660`、`E9236B0`。因此“线程循环在 so，队列操作和业务回调可以在 iosd”是本样本中可观察的协作方式。

Sim Aux 使用另一套队列。主 ELF 的出队/入队入口为 `1653D220`、`1653D270`，与 Auxiliary 分别记录。库中的请求提交和执行路径还使用模拟开关与 parser 错误跳转设施，出现文件操作失败的专门处理。具体请求类型与全部提交者仍未枚举。

Worker 1/2 的池初始化参数包含两个 worker 和一组 iosd 平台运行时回调。`libthpool.so +0x31C0` 入口用 `Worker thread %d` 设置线程名，调用初始化钩子，随后等待条件变量、取队列任务并调用任务处理函数。创建侧通过 `libiosd_crb_vxe_unix.so +0x998E0`、`+0x99A40` 等钩子准备栈和登记每个 worker 的上下文。

当前没有证据把 Worker 1 固定归给一种协议、Worker 2 固定归给另一种协议。需要保留“提交者 → job 处理函数 → 实际执行线程”的关系，才能说明某次工作由谁处理。

## IOS 内部任务与 Linux 线程的区别

前面 EHSA 分析中出现的 `REDUNDANCY FSM`、`REDUNDANCY peer monitor`，以及 `iosd_shim` 创建的 `IOSD ipc task`、`IOSD chasfs task`，来自 IOS 内部任务创建设施 `D792920`。这与上面的 `pthread_create` 是不同的创建路径。

```text
subsystem init
  ├─ 注册处理函数 → 消息或事件分派 → 某个 Linux 线程执行
  ├─ 创建 IOS 内部任务 → IOS 调度设施执行
  └─ 提交辅助请求或 worker job → 对应队列与线程执行
```

一个子系统可以参与多条路径，一条线程也可以执行多个子系统的回调。初始化时在哪条线程调用 init，不等于以后所有业务回调都只在那条线程执行。当前还没有把所有 IOS 内部任务的实际调度位置映射到每个 Linux TID。

例如 `iosd_shim` 的 init `E8FA440` 在类别 8 EHSA 中，却会创建 IPC/Chasfs 内部任务，并为 IOS 与 Fastpath 分别准备 TDL 相关上下文。类别 8 因而不能解释成“这个 subsystem 专属于一条 EHSA Linux 线程”。当前七条 Linux 线程中也没有单独名为 EHSA 的线程。

## level 在这里至少有两种具体含义

### module 名字中的 level

`level_kernel`、`level_driver`、`level_protocol`、`level_ehsa` 等，是 module 初始化图中的分组描述符。当前保存了 14 个 `level_*` 分组和带回调的 `memtest` 节点。

这类 level 可以理解为“初始化层次或阶段分组”。真正顺序还取决于依赖和启动条件。例如 `level_protocol` 需要 `level_driver`，`level_ehsa` 需要 `level_pre_ehsa`；`memtest` 的 module 成员关系指向 `level_protocol`。这些分组不会因名字中有 level 就各自对应一条线程。

### thread_level 与数字 level

主 ELF 的线程初始化函数调用 `D714C40 → D714A10`。消费者会分配名称为 `Interrupt Stack` 的栈，并更新按 56 字节步长组织的栈/上下文描述符；线程创建函数取回栈地址和长度，再调用 `pthread_attr_setstack`。

所以这里的数字用于 IOS 执行环境的栈与 level 登记，不能直接解释为 Linux 线程优先级、CPU 编号、CLI 权限等级或 module 编号。

| 角色 | 内部线程表索引 | thread level | 主 ELF 的 level 初始化入口 RVA |
|---|---:|---:|---|
| IOS | 0 | 本轮未核对 | — |
| Fastpath | 1 | 3 | `E8D86C0` |
| Packet | 2 | 2 | `E8D8960` |
| Auxiliary | 3 | 4 | `E8D87A0` |
| Worker 1 | 4 | 5 | `E8D8A40` |
| Worker 2 | 5 | 6 | `E8D8B20` |
| Sim Aux | 6 | 7 | `E8D8880` |

这里已经能看到不同编号空间：Fastpath 的线程表索引是 1，thread level 是 3；subsystem 类别 3 则叫 Driver。它们不能按数值连接。

`raise_interrupt_level` 等函数又涉及执行时的中断 level 控制。它们与这套执行环境有关，但完整同步、屏蔽及线程交互实现尚未闭合，不能仅凭名字将数字当成硬件 IRQ 优先级。日志 level、CLI privilege level 也需按各自消费者解释。

## 当前现场与程序归属

内部 `__be_thread_tab` 的七条记录显示如下。记录中的 pthread handle、syspage index 与 Linux TID 分别保存，没有将它们当成同一个整数。

| 表索引 | 内部名称 | 本次 syspage index |
|---:|---|---:|
| 0 | IOS Thread | 25 |
| 1 | Fastpath Thread | 26 |
| 2 | Packet Thread | 27 |
| 3 | Auxiliary Thread | 28 |
| 4 | Worker Thread 1 | 30 |
| 5 | Worker Thread 2 | 31 |
| 6 | Sim Aux Thread | 29 |

数字只是本次现场。功能定位应使用符号、调用关系及经过版本校验的数据布局。静态初始化分组和这次线程清单仍没有逐一归属关系。

本轮保存了运行时库的动态符号、指定函数字节、有限入口范围和反汇编关联。标成 bounded span 的范围没有声称是准确函数边界，其中可能包含相邻代码；没有对整段范围中的每一行都作语义归属。也没有取得每条线程的当前堆栈、正在执行的 job、全部业务注册者或所有回调目标。

## 证据入口

- 当前七条调试器线程与内部线程表（历史材料路径：`../reports/threads-and-levels-20261029/runtime-thread-table.json`）。
- 系统初始化 D7B7690（历史材料路径：`../reports/threads-and-levels-20261029/startup/rva_d7b7690.json`）、创建调用 1583D9A0（历史材料路径：`../reports/threads-and-levels-20261029/startup/rva_1583d9a0.json`）。
- 创建接口实际 GOT 绑定（历史材料路径：`../reports/threads-and-levels-20261029/runtime-got-bindings.json`）、线程池接口绑定到 libthpool（历史材料路径：`../reports/threads-and-levels-20261029/thread-pool-binding.json`）。
- 平台运行时符号与函数字节（历史材料路径：`../reports/threads-and-levels-20261029/runtime-library.json`）、入口有限范围（历史材料路径：`../reports/threads-and-levels-20261029/runtime-entry-spans.json`）、注释反汇编（历史材料路径：`../reports/threads-and-levels-20261029/runtime-library-disassembly.txt`）。
- 线程池动态符号与初始化函数（历史材料路径：`../reports/threads-and-levels-20261029/runtime-pool-library.json`）、worker 入口有限范围（历史材料路径：`../reports/threads-and-levels-20261029/pool-entry-spans.json`）、线程池注释反汇编（历史材料路径：`../reports/threads-and-levels-20261029/pool-library-disassembly.txt`）。
- level 创建消费者 D714A10（历史材料路径：`../reports/threads-and-levels-20261029/startup/rva_d714a10.json`）、[module 与 subsystem 的独立初始化机制](iosd模块与子系统.md)。
