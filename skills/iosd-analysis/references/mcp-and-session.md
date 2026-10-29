# MCP 与会话

先使用宿主配置中实际可用的 MCP。独立 HTTP helper 是同一条工作流的另一种入口，不要求在 MCP 内再启动 MCP 客户端。服务名、地址和工具名可配置；当前实现基于已使用过的 ida-pro-mcp，但不假定每个服务器有完全相同的工具。

## 能力映射

| 能力 | 已观察到的工具名示例 | 缺少时如何处理 |
|---|---|---|
| 实例与身份 | `list_instances`、`server_health`、`survey_binary` | 读取允许的 Python API；缺少身份信息就不套样本 profile |
| 函数、字符串、数据 | `func_query`、`entity_query`、`find_regex` | 分页搜索；必要时进行有界只读采集 |
| 反编译与 CFG | `decompile`、`disasm`、`basic_blocks` | 没有 Hex-Rays 时保留汇编证据 |
| 引用和调用 | `xref_query`、`callees`、`callgraph` | 明确方向、类型、边界和 truncation；xref 不是完整数据流 |
| 精确字节 | `get_bytes`、`get_int` | 先核对来源；保证 saved IDB 时用 `get_bytes_and_mask(ea,n,0)` |
| 调试内存/ctree | `py_eval`、`py_exec_file` 或专用调试接口 | 不能静默改成读取 IDB |

这些名称来自历史发现清单，不是运行时已连接的证明。运行时重新探测。`trace_data_flow` 等名称也应核对实际语义；若只是多跳 xref 遍历，不应描述成完整的符号执行或污点分析。

## 会话入口

```text
python <skill>/scripts/iosd_mcp.py --url <url> discover --output <work>/capabilities.json
python <skill>/scripts/iosd_mcp.py --url <url> status --output <work>/session.json
```

也可设置 `IOSD_IDA_MCP_URL`，不要发布历史机器地址作为默认值。`status` 记录身份、基址、IDA 进程/数据库上下文、自动分析状态以及可取得的模块和线程信息，不读取目标内存。

当前独立 helper 面向可直接访问的 Streamable HTTP 服务，不实现 OAuth 登录。需要鉴权时使用宿主已连接并授权的 MCP，或在明确配置的传输层增加认证；不要将令牌写入 skill、请求文件或报告。

随后每个新 helper 请求使用 `--session <work>/session.json`。IDB 更换、IDA 重启或 rebase 后重新取得状态，不修改旧捕获里的 identity 来冒充新采集。

## 干净 IDB 和 rebase

已有报告中的 `sub_...`、`dword_...` 可能是旧基址生成的 IDA 名称，分析者重命名也可能不在新 IDB 中。结合原始符号、字符串、引用、字节锚点和有身份的 RVA 找回入口。

先前某版 MCP 的字符串缓存曾返回旧零基址地址；这是待核查的兼容性经验，不是所有服务器的规则。在当前段中读回字符串核验，再决定地址是 EA 还是 RVA，不给全部结果统一加基址。

## 请求失败

主入口为同一 session 文件建立 `.pending.json`。成功落盘后删除；异常时保留，阻止同一会话继续派发。该锁不覆盖其他客户端或交互脚本，因此仍需协调。

客户端超时后确认 IDA 空闲，再显式运行：

```text
python <skill>/scripts/iosd_mcp.py --url <url> status --output <work>/session.json --confirm-idle
```

这个参数表示操作者已经确认空闲，不是取消请求。旧 pending 记录留存为 resolved 文件。不要仅凭等待时间推断请求已经停止。

helper 通过 MCP 发送源码，不依赖双方共享文件系统。部分旧脚本会让 IDA 主机打开 JSON 或输出文件；远程部署时检查该约束，或使用新 helper 的传输方式。
