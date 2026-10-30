# 架构与经验模式

从 ELF/so/进程边界开始，分别建立初始化组织、协议/CLI 入口、执行上下文和状态关系。不要拼成缺少证据的单一包含树。

用户首先需要看懂程序时，按 [讲解与图解](explaining-iosd.md) 给出关系地图与实际案例。入口文档是 [从大 ELF 到运行机制](library/docs/iosd从大ELF到运行机制.md)，附八张 SVG 和 [可离线阅读的图解](library/docs/iosd架构图解.html)。先讲职责，地址作为复核路标。

## 优先建立什么

- ELF 段、导入、源码路径和函数入口；路径只提示 source component，不证明编译单元归属。
- subsystem metadata 的名字、init、类别和依赖证据；module header/link 作为另一种机制解释。
- 从 init 追踪注册、任务创建、队列与回调；调用可达的函数不能全部归属于这个组件。
- 区分 Linux pthread、IOS 内部 task、事件循环和回调。协议处理可能跨上下文，线程名不能替代映射证据。

## 可复用但需要验证的模式

当前已分析样本 MD5 为 `9eccfd46caadfff9c18557e2a446e19b`。随附 profile 按此样本约束。

| 观察模式 | 用途 | 验证办法 |
|---|---|---|
| subsystem double magic、名称和 init | 找候选实体和初始化入口 | 读回记录，验证编码、消费者及目标函数 |
| module header/link tag | 找分组、依赖、回调节点 | 核对 tag 分派与消费者，不能只看相邻记录 |
| 条件性安装回调/创建 task | 查初始化和激活条件 | 追条件来源、消费端及失败/撤销路径 |
| thread_level 与 Interrupt Stack | 理解该样本的线程栈初始化 | 查看构造函数及 pthread_attr_setstack，不等同 Linux 优先级 |

该样本的 module 分组 `level_*`、subsystem 类别、thread_level 和 CLI privilege 是不同概念。类别 8/EHSA 也不意味着该类别全部代码运行在一个 EHSA 线程中。

`scripts/iosd_mcp.py subsystems --pointer-mode <encoding>` 采集观察布局下的候选；显式选择编码，失败记录继续保留。`scripts/profiles/subsystems_26_01_02.json` 是历史 metadata 搜索索引，不是当前运行激活表。

IDA 忙碌或不可连接时，可先用 `scripts/iosd_mcp.py components --output <work>/components.json` 建立离线目录；用 `--query`、`--category` 和 `--match token|contains` 选择调查入口。目录保留每条记录、原始字段和未知项，过滤仅选择实体 ID。词元不是协议分类，也不生成 module/subsystem/线程的包含关系。

已保存索引中有 15 条不同记录同名 `cerrno_init`，因此名称不能用作实体唯一键。相关统计、协议搜索入口和证据解释见 [组件索引与协议调查入口](library/docs/iosd组件索引与协议调查入口.md)。

按问题选择详细资料：

- [协议处理链与新会话验证](library/docs/iosd协议处理链与CLI新会话验证.md)：通过多种机制解释 init、registry、队列、task 与报文字段处理的关系，保留外部边界和设计推断。
- [模块与子系统](library/docs/iosd模块与子系统.md)
- [架构与术语](library/docs/iosd架构与术语说明.md)
- [线程与 level](library/docs/iosd的线程与level.md)
- [EHSA 心跳与主备状态机](library/docs/iosd的EHSA心跳与主备状态机.md)
- [完整架构指南](library/docs/iosd逆向分析教程.md)
- [二进制结构记录](library/iosd二进制文件结构描述.md)
