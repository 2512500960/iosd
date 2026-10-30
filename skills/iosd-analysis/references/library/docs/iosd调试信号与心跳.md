# iosd 调试信号与心跳代码复核

> 样本分析资料：保留适用版本、条件和未知项。原始捕获保留在本地；标注的历史材料路径用于定位来源。


本记录对应 C8000v IOS XE 26.01.02，MD5 `9eccfd46caadfff9c18557e2a446e19b`。2026-10-30 通过 IDA 9.1 MCP 读取 saved IDB，目标保持运行。本轮检查了六个主 ELF 函数以及相关导入和引用，操作范围为只读静态分析。

## 现场记录与处理设置

操作者的实验记录是：暂停 iosd 一段时间后，IDA 出现定时信号提示。现有输出截图记录了 `SIGVTALRM`。操作者回忆，将信号 `Pass to program` 后目标曾崩溃退出；信号编号、当时线程状态及退出栈尚待重新核对。

截图中 `SIGALRM` 与 `SIGVTALRM` 都采用 `Suspend=No`、`Passed to=Debugger`、`Report=Log`。这记录了本次实验的信号处理策略。`Passed to=Debugger` 由调试器处理该信号，`Passed to=Application` 则将其交给程序，分别影响目标的信号处理路径。选项含义见 [IDA 文档](https://docs.hex-rays.com/9.0/user-guide/user-interface/menu-bar/debugger/exceptions)。

Linux 的常规 interval timer 中，`SIGALRM` 对应实时时间，`SIGVTALRM` 对应进程用户态 CPU 时间。信号来源调查还包括外部发送者、已经 pending 的信号和各线程的停止情况；进程完全停止执行期间，虚拟 CPU 时间计时器的计时条件与实时时间计时器不同。语义见 [GNU C Library](https://sourceware.org/glibc/manual/2.24/html_node/Setting-an-Alarm.html)。

## 主 ELF 中已经复核的入口

地址为本样本 RVA，分析者自动生成的函数名按地址重定位。

| RVA | 已取得的消费代码关系 |
|---|---|
| `0xE8FD510` | 准备相关上下文与统计，创建名称为 `IOSXE heartbeat process` 的内部任务，最后调用 `__be_mcp_init_watchdog`；任务创建失败路径调用 `_be_crashdump(0)` |
| `0xE8FD700` | 条件成立时调用 `__be_mcp_emit_heartbeat`，返回失败时进入日志路径 |
| `0xE8FD790` | 心跳任务入口，准备计时/事件对象，调用 `__be_unix_start_hogcheck_periodic(1000)`；循环处理事件、发送心跳并维护统计，包含 `_be_crashdump(0)` 失败分支 |
| `0xE8FEF60` | 准备 `IOSXE signals IOS cmd boolean` 相关对象，有条件创建另一内部任务，调用 `__be_mcp_get_watchdog` 并保存返回值，随后登记 `0xE8FFED0` 回调 |
| `0xE8FF050` | 检查 `MCP_STARTUP_DEBUG` 相关启动配置，在相应分支调用 `__be_iosd_signal_ios_thread(1)` |
| `0xE8FFED0` | 读取保存的 watchdog 值，传给 `__be_mcp_set_watchdog_off` |

`0xE8FD790` 中，周期检查启动返回失败、心跳发送失败及异常事件分支分别通向日志/崩溃处理。调用参数 `1000`、`2000` 目前按原始整数保留，单位和完整调度语义继续由消费者确认。

这些入口表明 iosd 在启动后维护心跳，并通过执行环境接口连接 watchdog 与 hogcheck。命名中的 heartbeat、watchdog 和 hogcheck 分别按其具体调用职责记录。

## 当前证据边界

所检查的主 ELF 函数中，已经确认心跳任务及主动崩溃分支。`SIGVTALRM` 的注册入口、发送方式、信号处理函数和现场退出之间的完整链路仍待核对。

相关导入经 PLT/GOT 调用。此次 saved IDB 中，`__be_mcp_init_watchdog`、`__be_mcp_emit_heartbeat`、`__be_unix_start_hogcheck_periodic` 和 `__be_simulation_signal_handler` 对应 GOT 保存值均为零，当前库绑定尚未从这些数据库字节取得。后续可在目标已暂停且映射验证后单独采集绑定，再沿实际实现定位信号注册与处理。本轮保留现有调试执行状态。

教程中的信号设置因此以现场经验说明，代码部分以已经取得的主 ELF 调用链说明。进程间监督、周期调度检查和主备协议心跳，各自按照发送端与消费端证据解释。

本地复核材料在 `reports/signal-review/`，包括新会话身份、导入表、引用、六个函数捕获和 GOT 检查。完整反编译与原始数据库留在本地；本文保存派生关系和适用范围。
