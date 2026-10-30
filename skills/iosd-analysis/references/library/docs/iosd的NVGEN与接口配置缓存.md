# iosd 的 NVGEN 与接口配置缓存

> 样本分析资料：保留适用版本、条件和未知项。原始捕获保留在本地；标注的历史材料路径用于定位来源。


当前 C8000v 26.01.02 样本中，NVGEN 使用专门的解析上下文，沿配置语法和对象迭代路径调用配置生成回调。回调读取各自负责的状态，通过公共输出函数生成文本；入口附近还有生成前后的 registry 钩子。**这里没有观察到一个按 subsystem 清单逐个调用 init 来收集配置的过程。初始化、配置状态保存和配置文本生成是不同职责。**

本样本也有接口配置文本缓存。`parser config cache interface` 的 handler、缓存资格检查、命中后复用文本、生成后保存文本及禁用时清理缓存，都已有代码证据。当前目标是否启用缓存、哪些接口已有缓存，本次没有读取现场验证。

下面的函数和全局对象地址均为 RVA，输入 MD5 为 `9eccfd46caadfff9c18557e2a446e19b`。结论来自匹配 IDB 的反编译、明确范围的 IDB 数据字节及此前保存的语法图；没有执行设备 CLI 或目标回调。当前 IDB 的部分数据记录已经呈现运行时 tagged 大端指针表示，不能与最早零基址静态记录的小端表示混用。

## 设计上的两个方向

```text
配置输入：文字 → 语法匹配和参数 → CLI handler → 状态修改
配置生成：已有状态 → NVGEN 回调 → 输出配置行 → 显示或保存
```

Cisco 对早期 IOS 的公开说明指出，配置状态分布在各组件中，由 NVGEN 汇总生成 running configuration。文档中的接口缓存是这条生成路径的性能优化，而不是 NVGEN 的全部含义。[Cisco Configuration Generation Performance Enhancement](https://www.cisco.com/c/en/us/td/docs/ios/fundamentals/configuration/guide/12_2sr/cf_12_2sr_book/config_cache.html)

当前样本的具体入口、字段和缓存流程由下面的二进制证据确认，没有从旧版文档套用结构偏移。NVGEN 体现的是状态到文本的生成能力，并不能反向穷尽所有可输入命令；EXEC、默认未输出状态、未注册路径和自定义生成逻辑都需要分别研究。

## 从 show running-config 到生成引擎

已取得的命令路径中，`show running-config <cr>` 对应 handler RVA `0xDFE9DB0`，继续进入 `0xDFE8DD0`。后者处理显示选项、接口或其他筛选对象，调用 `0xE0D71A0`，相应失败分支可回退到 `0xE0D6360`。

这两个入口都进入 `0xE0D6470` 创建生成请求并调用 `0xE0DE210`。显示路径既有输出句柄的处理，也有取得文本缓冲区的分支，因此不能把某一个局部缓冲区当成 NVGEN 的唯一输出方式。

```text
show running-config
  → DFE9DB0 → DFE8DD0
    → E0D71A0 或回退 E0D6360
      → E0D6470 → E0DE210
        → 创建 NV Parser CSB
        → 设置 NVGEN 状态、模式与输出目标
        → registry 钩子 + 语法路径遍历或指定回调
        → 完成配置输出并清理上下文
```

`write memory` 的已取得路径对应 `0xDFEA900 → 0xDFEA390`；普通分支进入 `0xE0DFE10` 的保存编排，其中也有调用 `0xE0DE210` 的分支。显示和保存可以共用生成引擎，但保存还涉及目的对象、锁和其他回调，不能把 write handler 简化成单纯打印文本。此轮重点核对的是上面的显示生成主路径。

## 生成引擎如何调度各个组件

`sub_E0DE210` 先进行生成资格和锁相关检查，申请名称为 `NV Parser CSB` 的上下文，然后设置：

| CSB 字段 | 当前样本偏移 | 已确认用途 |
|---|---:|---|
| NVGEN 标志 | `0x25A4` / 9636 | 写逻辑值 1，供动作与业务 handler 区分生成路径 |
| sense | `0x2470` / 9328 | 生成上下文中设为逻辑值 1 |
| 当前模式 | `0x2D10` / 11536 | 生成路径选择所用模式对象 |
| 命令前缀文字 | 10481 起 | 回调用于输出当前配置命令的文字前缀 |
| 输出句柄 | 13216、13220 等 | 从生成请求复制到上下文，供公共输出路径使用 |

引擎把当前生成 CSB 放到全局槽 RVA `0x381E2E30`。这解释了为什么某些输出封装没有继续传递完整 CSB，却仍能找到输出目标。该槽是生成过程的上下文连接点，不是所有组件配置状态的统一数据库。

没有指定专门生成回调时，引擎通过 `sub_DF3CA50` 取得当前 mode 对象 `+0x50` 的语法起点，调用 `sub_DEE5040` 排入节点，再由 `sub_DEE5E30` 遍历。后者调用动作分派 `sub_DEFF7A0`。指定筛选回调时，引擎另有直接调用该回调的分支。

因此，已核对的一条收集机制是**沿注册后的配置语法和模式进入生成节点，再让相应回调读取自身状态**。接口和其他多实例对象还需要迭代器提供对象上下文。例如禁用接口缓存的专用生成链，会使用 `sub_DF2D060` 的接口迭代逻辑，而不是只访问一个静态接口描述符。

引擎在生成前后调用多个 registry 列表，包括 `DF3E290` 和 `DF3E2E0` 返回的列表；其中的成员和副作用尚未全部恢复。它们表明生成过程还有扩展接口，不能把已知语法回调说成唯一来源。

## nvgens 动作怎样调用业务函数

`nvgens_action` 的消费函数是 RVA `0xE39D8F0`。描述符的主要字段为：

| 载荷偏移 | 用途 |
|---|---|
| `+0` | 生成回调指针 |
| `+8` | selector，同时复制到 CSB 的 9364 和 9356 |
| `+12` | 生成调度相关 flags，原始值保留 |

消费者进入 `sub_E39D9B0`。这个公共门控函数根据解析状态、模式和其他标志决定继续普通语法，还是调用生成回调；回调调用附近还存在 AFS 获取/释放路径。它不是在所有状态下无条件执行回调。

同一个描述符关联的函数也可以被普通 CLI 的 EOL 节点引用。函数内部再检查 NVGEN 标志，选择读取状态并输出，或者处理用户输入。这是共用函数的两条执行方向，不表示两种调用的全部效果相同。

## 实例一 hostname 的状态保存和生成

已取得的记录把 NVGEN 节点 `0x34147FF8` 与 CLI EOL `0x34148098` 都关联到 `0xE0E6A00`，selector 均为 0。

该 handler 检查 CSB `+0x25A4`。生成分支读取主机名状态，经 `sub_E0D9CD0` 输出命令前缀及主机名，并根据条件采用带引号的格式。普通分支读取输入字符串，做空格、字符及 RFC1123 相关检查，正常修改路径调用 `sub_E0E5A20`。两条路径还有不同的 registry 查询/回调，可能接管相应处理。

因此，hostname 的“可配置”与“可生成”并不需要两个独立业务实现：语法记录可以引用同一个 handler，由上下文区分方向。也不能把 NVGEN 分支中的输出函数当作输入处理时的必经步骤。

## 实例二接口 description

NVGEN 节点 `0x34149080` 与 EOL `0x34149120` 指向相同回调 `0xE40C850`，selector 均为 3。这个入口继续调用 `sub_E400E90`。

普通配置分支为描述分配并保存字符串，处理删除，并通过 `sub_E43E130` 等路径提交对象更新。生成分支读取保存的描述对象及有效状态，使用 `%s %s` 格式输出配置；代码还有从接口对象另一字段取得描述的回退分支。

这说明组件的配置状态可以存在具体对象中，而不是保留为最初输入的整行文字。NVGEN 回调理解该对象的表示，公共生成框架负责调度和输出。当前尚未恢复 description 更新到所有缓存失效通知之间的完整链路。

## 公共输出如何汇总成文本

hostname、description 等路径调用 `sub_E0D9CD0`。该封装在输出条件成立时，通过全局生成 CSB 查找输出目标，进入 `sub_E0D8B20`。

`sub_E0D8B20` 的诊断字符串直接包含 `nv_write_internal`。它根据模式计算缩进，准备换行及格式化缓冲区，再进入 `sub_E0E1B20`，由后者写入输出句柄或相关输出设施，并处理可选的 registry 通知。

框架不必理解每个协议的配置字段，只需要约定上下文、回调和输出接口。组件负责解释自己的状态并决定是否输出；公共设施负责把这些片段组织到输出目标中。这是当前代码呈现的职责划分，不代表所有自定义动作都已解释。

## 接口配置缓存的开关和资格条件

当前已取得路径包含正向、`no` 和 `default parser config cache interface`。EOL 为 `0x340BC398`，handler 为 `0xDEF9650`；载荷后面的名字是 `int_config_cache_cmd`。

普通分支将 sense 保存到全局变量 RVA `0x381C05B0`；NVGEN 分支则根据该变量输出开关配置。此处证明 handler 具有生成分支，尚未仅凭这段代码确认它在所有配置生成路径中的调用来源。

缓存不是只检查这个开关。`sub_DEF9790` 还检查输出上下文标志、接口和硬件对象类型、额外输出选项及 registry 回调。部分标志的完整业务名称未恢复，原始表达式保留；不能把“开关为 1”当作任何接口、任何显示方式都必然使用缓存。

两个包装分别调用这个资格函数：`sub_DEF99C0` 用于已有缓存的复用检查，`sub_DEF9740` 用于生成后保存缓存的路径准备。

## 缓存如何命中 保存和清理

已核对的两个接口处理函数 `0xE3FC690`、`0xE406010` 都包含 NVGEN 分支，并检查接口对象 `+0x220`，即十进制 544 的文本指针。

```text
进入接口配置生成路径
  ├─ 已有缓存 + 资格检查通过
  │    → DEF9A20 分段输出已有文本
  │    → 跳过相应的继续生成路径
  └─ 未使用缓存
       → 记录输出起点及当前接口
       → 进入接口模式的语法生成路径
       → 已排入的回调节点调用 E3FC1B0
       → 从输出缓冲区截取本接口片段并保存
```

保存回调由节点 `0x342BE680` 或 `0x342BE950` 的 `func_action` 关联，回调都是 `sub_E3FC1B0`。这两个描述符的 flags=4；`func_action` 消费者 `0xE39A0D0` 允许相应回调在 NVGEN 上下文执行。接口处理路径先排入该节点，再排入接口模式语法；框架排队及遍历顺序决定后续调用。`sub_E3FC1B0` 根据输出起止位置分配文本空间，将指针写到接口对象 `+544`，再调用 `sub_E0D5E90` 复制生成片段。

`sub_DEF9A20` 以不超过 2037 字节的片段输出缓存，避免把整段配置直接作为单个超长格式化参数。它调用输出封装，不重新执行每条普通配置命令。

已经确认两种清理路径：

1. **禁用缓存后的遍历清理。** `sub_DEF9650` 在开关变为 0 时尝试调用 `sub_DF331E0`。后者创建 `interface config csb`，设 NVGEN=1，从 `0x340A86A0` 的专用链开始遍历。链中有接口迭代动作和 `sub_DF34330`；后者释放当前接口 `+544` 的文本并清零该字段。分配失败和特殊条件的处理仍按实际分支保留。
2. **复制阶段的标志清理。** `sub_E0D5E90` 在相应 CSB 标志成立时释放当前接口的缓存、清零指针并清除该标志；另一分支从生成输出中复制文本。这里证明了清理行为，没有把该标志的所有设置来源都解释为同一种配置变化。

另外，`sub_E8F2D50` 在开关开启的相应路径上调用 registry 分派 `sub_1E73F7D0`，传入接口相关对象。该列表的完整成员尚未恢复，不能仅凭这个通知就断言缓存已被清除。**普通接口配置改变如何覆盖所有失效触发点，仍是保留的分析缺口。**

## 与 CLI handler 的关联统计

对已有 194,435 个节点的保存图进行了离线对照：

| 统计项 | 数量 |
|---|---:|
| 已解码的 nvgens 节点 | 5,099 |
| 非零回调地址去重 | 1,995 |
| 与已解码 CLI EOL 共用函数的 nvgens 节点 | 4,432 |
| 同时共用函数和 selector 的 nvgens 节点 | 4,174 |
| 已取得的迭代器节点 | 1,606 |

这些是节点和指针关联数，不是组件数、配置行数或可执行命令数。CLI 对照只纳入解释为 `command_terminal` 的 EOL 节点，组合终结宏及自定义动作不在此统计范围。描述符字段齐全也不等于回调语义已经全部理解。

工具仅比较保存的描述符，不调用回调、不求值未知条件、不枚举接口实例。生成链的条件、未知动作、未解析的 registry 成员及调用效果继续保留在原图和分析材料中。

## 与其他缓存和配置树的区别

这里的接口缓存保存已生成的配置文本。样本中还存在 `parser cache` 的输入匹配缓存线索，两者不能因为都包含 parser/cache 字样而合并。是否命中输入解析缓存、是否复用接口生成文本，属于不同阶段的问题。

同样，NVGEN 是从状态到文本的生成过程；ICM 配置文本树和 diff 是文本组织或差异处理结构。当前没有把它们视为同一张命令语法图，也没有从一个名称推断全部连接关系。

## 证据与复现

可搜索的 NVGEN 与接口缓存证据目录（历史材料路径：`../reports/nvgen-implementation-20261029/index.html`） 分别列出流程、案例、全部已解码的 nvgens 描述符关联和保留缺口。

- 生成入口 E0DE210（历史材料路径：`../reports/nvgen-implementation-20261029/engine/rva_e0de210.json`）、动作消费者 E39D8F0（历史材料路径：`../reports/nvgen-implementation-20261029/entry-functions/rva_e39d8f0.json`）、回调门控 E39D9B0（历史材料路径：`../reports/nvgen-implementation-20261029/entry-functions/rva_e39d9b0.json`）。
- hostname handler（历史材料路径：`../reports/nvgen-implementation-20261029/entry-functions/rva_e0e6a00.json`）、description 实现（历史材料路径：`../reports/nvgen-implementation-20261029/core-functions/rva_e400e90.json`）、描述符关联案例（历史材料路径：`../reports/nvgen-implementation-20261029/case-associations.json`）。
- 缓存开关 handler（历史材料路径：`../reports/nvgen-implementation-20261029/entry-functions/rva_def9650.json`）、资格检查（历史材料路径：`../reports/nvgen-implementation-20261029/cache-and-walk/rva_def9790.json`）、接口生成路径（历史材料路径：`../reports/nvgen-implementation-20261029/interface-generation/rva_e3fc690.json`）、保存回调（历史材料路径：`../reports/nvgen-implementation-20261029/cache-save/rva_e3fc1b0.json`）。
- 专用 parser 节点原始字节（历史材料路径：`../reports/nvgen-implementation-20261029/special-parser-nodes.json`）、禁用清理链的迭代节点（历史材料路径：`../reports/nvgen-implementation-20261029/disable-cache-root.json`）、清理回调节点（历史材料路径：`../reports/nvgen-implementation-20261029/disable-cache-leaf.json`）、逐接口释放函数（历史材料路径：`../reports/nvgen-implementation-20261029/disable-cache-walk/rva_df34330.json`）。
- 公共输出 nv_write_internal（历史材料路径：`../reports/nvgen-implementation-20261029/generation-functions/rva_e0d8b20.json`）、生成片段复制和清理分支（历史材料路径：`../reports/nvgen-implementation-20261029/cache-invalidations/rva_e0d5e90.json`）、关联统计与范围（历史材料路径：`../reports/nvgen-implementation-20261029/binding-summary.json`）。

离线复现描述符关联：

```powershell
python tools/analyze_nvgen_bindings.py reports/runtime-comparison-20261029/options/tree --output reports/nvgen-implementation-20261029
```

规则配置为 [当前样本的 NVGEN profile](../../../scripts/profiles/nvgen_26_01_02.json)。它保存已经审查的入口、字段和明确缺口，不是可执行的 NVGEN 模拟器，也不提供跨构建自动定位。
