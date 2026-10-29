# 协议调查

先回答“从哪里开始看”，再逐条确认处理链。不要凭协议名、日志或 subsystem init 给函数指定报文解析角色。

## 入口与跟进

```text
python <skill>/scripts/iosd_mcp.py --url <url> protocol --session <work>/session.json --query bgp --output <work>/bgp.json
python <skill>/scripts/iosd_mcp.py --url <url> relationships --session <work>/session.json --rva <function-rva> --output <work>/refs.json
python <skill>/scripts/iosd_mcp.py --url <url> function --session <work>/session.json --rva <function-rva> --output <work>/function.json
```

扫描当前 IDB 名称和有界只读数据，结合身份匹配的历史 metadata，输出初始化/注册、接收/分发、解析、状态/结果、代码归属五阶段计划。名称分 token 与 substring 候选，例如 `ipcdp` 不会静默归为 CDP。

默认限制为 200000 个名称、8 MiB 字节、500 条结果；先检查 coverage。函数反编译默认不超过 16 KiB，超限保存缺口，不自动展开超大函数。

`relationships` 展开一跳，分别记录直接调用、数据引用、代码指针候选、跨函数转移候选、间接槽和未解析调用，不执行回调，也不自动推出数据流或所有权。

## CDP

从 `cdp` subsystem init、相关 registry、路径和日志引用交叉追踪：二层接收与分发 → CDP 头/TLV 检查 → 邻居状态及定时器。`CDP Protocol` 等 task 名只作线索，不是 Linux 线程归属证明。

## BGP

从 `bgp`、地址族 subsystem 和 TCP 读入线索出发：会话/字节流 → 消息组装与头校验 → OPEN/UPDATE/KEEPALIVE/NOTIFICATION 分发 → 属性解析 → 邻居状态、策略与 RIB 更新。不要把 `router bgp` CLI handler 当成 UPDATE 解析器。

这些路线来自协议知识和组织线索，不表示当前样本已完成整条链验证。协议规范帮助解释字段，具体实现仍需函数和字节证据。

## 关系证据

记录缓冲区和长度来源、传参、类型/长度/状态检查，以及错误处理。回调记录注册 API、槽位、覆盖者、安装条件和消费端；无法求出的目标保留表达式/指令及下一步取证办法。

遇到 extern/PLT/GOT，按 [运行时与 core](runtime-and-core.md) 核对绑定；遇到 IPC，区分本进程发送、外部接收和未知进程边界。
