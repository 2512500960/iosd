# 运行时与 core

运行时读取用于验证当前链接槽、链表、状态、模块绑定和语法节点。它补充静态证据，不代表所有配置状态下的命令都已注册。

## 精确读取

saved IDB 请求 `read.json`：

```json
{"source":"idb","ranges":[{"space":"image","rva":"0x1000","size":32,"name":"selected bytes"}]}
```

```text
python <skill>/scripts/iosd_mcp.py --url <url> read --session <work>/session.json --request <work>/read.json --output <work>/idb-bytes.json
```

`source=idb` 读取保存的数据库字节并核对初始化 mask，不使用 debugger fallback。它并不证明字节仍与原始 ELF 完全相同。

Debugger 请求在目标已经暂停、运行时基址独立确认后使用：

```json
{
  "source":"debugger",
  "runtime_base":"0x80000000",
  "anchors":{
    "input_md5":"本次会话的MD5",
    "anchors":[{"rva":"0x1000","expected_hex":"由已核对的不变代码字节填写"}]
  },
  "ranges":[
    {"space":"image","rva":"0x2000","size":32,"name":"global slot"},
    {"space":"runtime","va":"0x90000000","size":64,"name":"heap record"}
  ]
}
```

这是填写格式，不是可直接发送的地址或字节。使用 1–8 个独立选择的、每个 4–32 字节的非重定位不变锚点。helper 同时核对 saved IDB 和 debugger 字节，以及主映像名称和运行时基址。允许 IDB 基址和运行时基址不同；全局 RVA 与堆 VA 明确区分。

每批 1–64 个 range，单 range 最多 64 KiB，总计最多 1 MiB。不可读、时间预算耗尽和身份变化保留为 gap，不补零。收集前后检查暂停状态和模块表，但不能检测所有 resume/re-stop 周期，因此 `atomic_snapshot=false`。

## 链表与命令图

先核对头、记录大小、next 字段和编码，再使用 `scripts/tools/capture_debugger_memory.py`、`collect_runtime_linkage.py`、`collect_runtime_pages.py` 和离线 `export_runtime_grammar.py`。这些旧采集器的锚点、当前 IDB 基址、主模块顺序和文件系统要求按其参数检查，不将它们当作通用远程接口。

复用 `runtime_linkage.capture_runtime_linkage`、`runtime_grammar.CapturedPages` 和 `reconstruct_runtime_graph`。保留 accept/alternate、动态 slot、pending record、未绑定静态定义及所有 frontiers。链表到 null 只表示本次模型下完成该链。

## 外部实现

extern stub 不是 so 内部实现。核对 ELF 重定位、原生 GOT、当前模块映射和必要时的运行时导出符号后再给归属。模块范围可能不包含 BSS，不能仅因地址超出 IDA 报告的 size 就否认其归属；也不能凭名字认定属于某个库。

历史线程调查中 `binos_init_thread_pool` 绑定到 `libthpool.so`，这是“名字不能替代绑定证据”的实例，不是所有版本的固定绑定。IPC 发送端不能证明接收进程或 PID。

## ELF core

当前 core 解析器支持未压缩的 ELF64 x86-64 ET_CORE；其他架构需增加后端，不能套用当前布局。core 在本机解析，不连接 IDA。请求使用 runtime VA：

```json
{"ranges":[{"space":"runtime","va":"0x90000000","size":64}]}
```

```text
python <skill>/scripts/iosd_mcp.py core-read --core <dump.core> --request <work>/core-read.json --output <work>/core-bytes.json
python <skill>/scripts/tools/inspect_core.py <dump.core> <node-runtime-va> --layout <layout.json> --max-nodes 100
```

`ElfCoreMemory` 区分 PT_LOAD 的 memory_size 与 file_size；未捕获页报缺失，不制造 BSS 零值。core 地址与 RVA 的关系需单独确认；PT_LOAD 映射不证明它属于当前 IDB，也不证明快照原子性。

进一步资料：[通用注册与调试接入](library/docs/通用注册分析与调试接入.md)、[运行时命令图](library/docs/运行时命令图导出说明.md)。
