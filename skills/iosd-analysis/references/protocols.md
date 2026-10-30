# 协议调查

先回答“从哪里开始看”，再逐条确认处理链。不要凭协议名、日志或 subsystem init 给函数指定报文解析角色。

当前样本的复核摘要在 [协议处理链与新会话验证](library/docs/iosd协议处理链与CLI新会话验证.md)，机器可读定位在 `scripts/profiles/protocol_paths_26_01_02.json`。先核对 MD5，再复核 RVA；这是局部静态证据，不是当前运行轨迹。CDP 已核对队列、内部 task、头/TLV 与缓存处理；BGP、OSPF、UDP 的部分分发/处理已核对；LLDP、IS-IS 保留入口与缺口。不要把这些覆盖范围扩写成全部协议已分析完成。

主入口在样本匹配时随 `protocol` 结果附上 `prior_reviewed_paths`，与本次候选分开，明确 `verified_in_this_capture=false`、`runtime_execution_proven=false`。未收录某协议只表示索引尚缺，不表示实现不存在。此附带逻辑完成离线边界测试，并在用户确认 IDA 空闲后完成有界实机复测；索引中的每条关系仍是待按问题重新复核的历史局部证据。

## 入口与跟进

尚不知道要调查哪个协议时，先用不连接 MCP 的 `components` 命令查看已保存组件目录，再按名称词元或类别选择入口。该目录支持任何输入索引中的名称，不限 CDP/BGP；词元命中只表示搜索相关，不能替代报文处理关系证明。用 `--match contains` 扩大名称搜索时同时保留可能误匹配的候选。

```text
python <skill>/scripts/iosd_mcp.py --url <url> protocol --session <work>/session.json --query bgp --output <work>/bgp.json
python <skill>/scripts/iosd_mcp.py --url <url> relationships --session <work>/session.json --rva <function-rva> --output <work>/refs.json
python <skill>/scripts/iosd_mcp.py --url <url> function --session <work>/session.json --rva <function-rva> --output <work>/function.json
```

扫描当前 IDB 名称和有界只读数据，结合身份匹配的历史 metadata，输出初始化/注册、接收/分发、解析、状态/结果、代码归属五阶段计划。名称分 token 与 substring 候选，例如 `ipcdp` 不会静默归为 CDP。

默认限制为 200000 个名称、8 MiB 字节、500 条结果；先检查 coverage。函数反编译默认不超过 16 KiB，超限保存缺口，不自动展开超大函数。

达到名称、字节、结果或时间限制时，检查 `result.cursor` 和 `coverage.has_more`，从上一页继续，而不是反复重扫最前面的范围：

```text
python <skill>/scripts/iosd_mcp.py --url <url> protocol --session <work>/session.json --query bgp --resume <work>/bgp.json --output <work>/bgp-page-2.json
```

继续采集使用同一会话和查询，输出到新文件。cursor 保存名称索引以及字符串窗口内的位置，结果达到上限也不跳过窗口里剩余命中。IDA 提供 nlist 索引时直接从对应项继续；基址、段布局、名称总数或游标边界变化时拒绝旧游标。游标不是数据库快照，其他位置的同数量改名仍可能改变结果，应在分析稳定时采集并保留每页证据。

字符串窗口包含边界前字节和最多 2048 字节 lookahead，避免跨窗口字符串丢失或以尾部片段重复出现。如果字节预算不够读取下一完整窗口，返回 `minimum_next_read_bytes`，不静默跳过它；适当提高预算再继续。`has_more=false` 仅指所选名称和字符串范围的游标已走完，仍需检查 faults，不代表所有编码字符串或完整协议实现均已取得。

`relationships` 展开一跳，分别记录直接调用、数据引用、代码指针候选、跨函数转移候选、间接槽和未解析调用，不执行回调，也不自动推出数据流或所有权。

## CDP

从 `cdp` subsystem init、相关 registry、路径和日志引用交叉追踪：二层接收与分发 → CDP 头/TLV 检查 → 邻居状态及定时器。`CDP Protocol` 等 task 名只作线索，不是 Linux 线程归属证明。

## BGP

从 `bgp`、地址族 subsystem 和 TCP 读入线索出发：会话/字节流 → 消息组装与头校验 → OPEN/UPDATE/KEEPALIVE/NOTIFICATION 分发 → 属性解析 → 邻居状态、策略与 RIB 更新。不要把 `router bgp` CLI handler 当成 UPDATE 解析器。

这些路线给出完整调查目标，本轮已验证的局部关系及尚缺环节按上述复核摘要判断。协议规范帮助解释字段，具体实现仍需函数和字节证据。

## 初始化图与报文处理图

初始化解决“谁把某种处理能力放到哪里”，收包路径解决“这份输入如何到达某个处理函数”。例如一种需要验证的模式是：

```text
初始化：init → register(key, callback)
运行时：接收入口 → 根据 key 分发 → callback(buffer, length) → 状态更新
```

直接从 init 展开调用图通常只能看到注册者；callback 的地址可能作为数据参数传递，因此调用图不一定包含它作为真正报文处理函数的那条边。应同时找注册的写入端和运行时的消费端，再核对 key、槽位、参数和条件。这也解释了为何“某 subsystem 初始化完成”不能单独证明某协议当前能接收或解析报文。

这是调查方法和设计解释，不能据此假定每个协议都走同一 registry、线程或队列。不同协议可能在 TCP 流、包队列、IOS task、外部库或 IPC 边界上采用不同机制；确认边界后再组织成可读的处理图。

## 关系证据

记录缓冲区和长度来源、传参、类型/长度/状态检查，以及错误处理。回调记录注册 API、槽位、覆盖者、安装条件和消费端；无法求出的目标保留表达式/指令及下一步取证办法。

遇到 extern/PLT/GOT，按 [运行时与 core](runtime-and-core.md) 核对绑定；遇到 IPC，区分本进程发送、外部接收和未知进程边界。
