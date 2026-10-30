# iosd 组件索引与协议调查入口

理解 iosd 可以先从“二进制里声明了哪些组件”开始，再追这些组件怎样安装功能、接收输入和维护状态。组件名称索引适合提供调查入口；它不能单独回答报文最终由谁解析，也不能证明组件当前已经激活。

本页从已经保存的 subsystem metadata 重新建立索引，没有连接当前 IDA，也没有读取当前进程内存。来源是 `profiles/subsystems_26_01_02.json`，绑定样本 MD5 `9eccfd46caadfff9c18557e2a446e19b`；原始组织机制及消费者解释见 [模块与子系统](iosd模块与子系统.md)。

## 先看组织类别 再找具体业务

当前保存索引包含 5,692 条候选记录、5,678 个不同名称和 13 个初始化类别：

| 类别 | 索引记录数 |
|---|---:|
| Protocol | 2,016 |
| Registry | 1,731 |
| Management | 696 |
| Library | 399 |
| Kernel | 335 |
| Driver | 262 |
| EHSA | 138 |
| Pre-EHSA | 45 |
| Pre-Driver | 43 |
| License | 20 |
| IFS | 3 |
| SystemInit | 2 |
| Microcode | 2 |

这些是记录及其初始化分类，不是网络协议种类、线程数或独立功能数。一个协议可能同时涉及 Protocol 类实体、Registry 类注册设施、Management 类展示与配置，以及库和驱动接口。它们是否构成实际调用或数据关系，仍需查看函数和注册消费者。

这里的设计解释是：从元数据中可以观察到多种初始化责任并存，因此研究一个业务时，按单一类别截断会丢掉相关线索。不能据类别数量直接推断哪部分占用更多 CPU、包含更多业务代码，或当前承担更多流量。

## 同名记录为什么不能合并

5,692 条记录只对应 5,678 个不同名称，并非索引自动去重后的误差。当前数据中有 15 条记录都叫 `cerrno_init`，分别记录不同的 init RVA。以下是其中三条：

| 记录 RVA | 名称 | 类别 | 索引中的 init RVA |
|---|---|---|---|
| `0x37A0B728` | `cerrno_init` | Registry | `0x0BD94090` |
| `0x37A0B9C8` | `cerrno_init` | Registry | `0x0BE5E070` |
| `0x37A69508` | `cerrno_init` | Registry | `0x1A875DE0` |

这说明名称不是实体唯一键。若用 `name → 单个函数` 的字典组织结果，后面的记录会覆盖前面的记录，研究入口就会消失。索引以记录地址区分实体，将同名关系另列出来，而不是提前合并。

同名、不同 init 可能来自分组件编译或生成的初始化入口，这是待验证解释。要判断这些入口的作用是否相似，需要比较初始化函数的参数、写入表和注册消费端，不能仅凭 `cerrno_init` 这个名字断言它们等价或互相包含。

另外有 8 条记录未记下 init RVA，例如 `all_oces`、`ipc`、`red_facility` 和 `ipsec_trace`。它们仍保留在索引和未知项中；缺少这个字段不等于该功能在运行时没有初始化。

## 不限协议的搜索入口

主入口可以完全离线建立组件目录：

```text
python skills/iosd-analysis/scripts/iosd_mcp.py components --output <work>/components.json
python skills/iosd-analysis/scripts/iosd_mcp.py components --query ospf --output <work>/ospf-components.json
python skills/iosd-analysis/scripts/iosd_mcp.py components --query bgp --match contains --output <work>/bgp-related.json
```

也可以通过 `--index` 使用另一份已保存的 RVA 组织地图，或通过 `--md5` 核对预期样本身份。这种核对只针对输入文件声明的身份，不会把历史索引冒充当前 IDB。

目录将名称拆成词元，建立类别和名称词元两个检索维度，算法没有写死 CDP、BGP 或其他协议名单。当前索引中，一些词元的命中数如下：

| 词元 | 精确词元匹配的记录数 |
|---|---:|
| bgp | 71 |
| cdp | 6 |
| ospf | 25 |
| isis | 29 |
| eigrp | 26 |
| pim | 26 |
| igmp | 11 |
| lldp | 6 |
| ldp | 4 |
| rsvp | 19 |
| tcp | 8 |
| udp | 7 |

这些仍是名称线索数，不能当作协议实现数量或协议全部组件数。默认词元匹配可以减少 `cdp` 与 `ipcdp` 之类的混淆；但 `bgpmib` 等连接在一起的名字也不会自动命中 `bgp` 词元。需要更广的线索时选择 `--match contains`，再人工核对关系。

过滤只生成 `selection.entity_ids`，不从 `entities` 删除其他记录或未知项。同名记录、空入口和原始字段继续保存。阅读大目录时先看 summary、facets 和 selection，再按实体 ID 读取详细内容，不必把整个 JSON 一次交给模型。

## 从调查入口走到报文处理链

搜索结果里会同时出现初始化、registry、协议主体、地址族扩展、展示与管理接口。下一步不是把这些名字画成包含树，而是核对两类关系：

```text
安装关系：哪个 init 把 callback 安装到哪个 key 或 slot，受什么条件控制
消费关系：哪个接收入口使用这个 key 或 slot，怎样把 buffer 和 length 交给 callback
```

只有将安装端和消费端关联起来，才能逐步解释某类输入为何到达某个解析函数。接着追踪报文头、类型与长度检查、字段解析、状态更新和错误路径，并确认实现位于主 ELF、外部 so 还是其他进程。

因此，组件目录回答的是“有哪些可调查的入口”，函数和注册证据回答的是“入口之间有什么关系”，运行时内存回答的是“这次状态下哪些关系已经安装或放行”。把这三个问题分别解释，通常比直接给出一棵看似完整的协议模块树更容易复核，也更能保留隐藏或按需激活的功能。
