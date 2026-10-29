# iosd 二进制文件结构描述

> **历史笔记提示**：本文保留了被后续复核纠正的旧正文，不适合按顺序当作当前结论学习。统一讲解、勘误和调试步骤已合并到 [iosd 逆向分析教程](docs/iosd逆向分析教程.html)，另有 [Markdown 源稿](docs/iosd逆向分析教程.md)。

> **启动与注册入口的后续勘误**：ELF start 从 `main` 指针槽 `0x37A93818` 取得 `0xB246530`；后者经 `__be_pcohort_main_proxy` 传入应用回调 `sub_B2464A0`，回调在 `__be_unix_begin` 成功后调用 `sub_D7B7690`。原文的 `sub_D710460=main` 不成立，它实际负责子系统分类与元数据准备；其尾部 `sub_D767810` 是 chunk 清理，不是常驻调度循环。Pending 处理也不能直接解释为创建线程。
>
> `sub_19601E40` 包含 FRR manager 初始化及注册失败诊断，不能仅由“Unable to parser_add_command”把它认定为通用 CLI 注册函数。本轮已找到更直接的注册表消费者 `sub_DEF7870`：16 字节指针对记录，交给 `sub_DEF70B0` 处理；flow 初始化路径向它传入了静态表，并提取出独立的 40 字节 transition 候选图。该图与 72 字节 ICM 配置节点不同，尚未解析全部操作码和 handler。
>
> **0.3.0 静态提取进展**：已确认 `sub_DEFF7A0` 使用 `0x3409EC00` 的 314 项动作表分派，并从部分 EOL 描述符的 `+0` 提取 handler 候选。扩展发现得到 1,319 个候选注册表、4,508 个不同 root；当前只选其中 100 个 root 遍历。部分 handler 可静态定位，不需要先准备 dump；这仍不等于完整命令集合或运行时可达集合。ICM 节点的 `+8` 仍不能当作 handler。
>
> **0.3.1 覆盖更新**：新增全部已发现入口配置，已处理 4,508 / 4,508 个 root，没有达到节点上限，得到 101,521 个节点和 15,049 个 EOL 候选。旧的前 100 个 root 配置保留为基线；全部入口的报告见 `reports/static-cli-all-discovered.json`，可搜索目录见 `reports/static-cli-catalogue.html`。完整命令字符串、模式/权限及其余动作语义仍未全部恢复。
>
> 更新后的概念说明与证据链接见 [iosd 架构 启动流程与术语说明](docs/iosd架构与术语说明.md)。

> **2026-10-28 MCP 静态复核勘误（优先于下文旧结论）**：输入 MD5 `9eccfd46caadfff9c18557e2a446e19b`，IDA 9.1。
>
> - `module_header_section` 的 15 条记录实际名称为 14 个 `level_*` 分类标记及 `memtest`，不应直接称为 15 个业务模块。记录大小 32 字节，原始字节按小端读取的标记为 `0x15055CC1 / 0xAFECAFEC`；link 大小 24 字节，标签为 `0xDFEADFEA` 或 `0xABEFABEF`。消费代码先 byteswap 标签，分派时可见的常量因此不同。
> - `sub_D7127D0` 的反编译支持子系统记录按 96 字节、header 按 32 字节、link 按 24 字节推进；不能因此认定 link 是“子系统→业务模块”的层级关系。
> - 检查 `sub_C2F7B50` 与 `sub_C2FA1D0` 后，**否定 `+0=命令串 / +8=parse_func`**。`+0` 是向下遍历的树链，`+16` 用于向上回溯，`+24` 用于同级遍历，`+8` 在插入时参与树链维护。未找到这里的 handler 字段。
> - 文本由 `+48` 或根的缓冲区数组取得，受 `+56` flags 控制；在 `0x40` 路径下，`+60` 为起始偏移，`+64` 是结束偏移，读取长度应为 `end-start-1`。指针按大端解码再去最高标记位。不能直接用 `+64` 当字符串长度。
> - 此 ICM 打印函数包含 `diff tree` 日志并处理配置文本；主 CLI 分派结构、命令树根、handler 关系仍需独立确认。下文“完全确认”“handler +8 已实锤”等旧句不再作为实现依据。
>
> 复核证据：`reports/mcp-static-verification.json`、`reports/mcp-module-init.json`、`reports/mcp-icm-print.json`、`reports/mcp-icm-add.json`；当前解析代码的 IDA 内验证结果见 `reports/mcp-plugin-module-result.json`。

> 对象：`x86_64_crb_linux_iosd_vxe-universalk9-ms`（iosd 主程序，`linux_iosd-image`）。
> 依据：17.9.04a（IDA imagebase `0x555555554000`）与 26.01.02（imagebase `0x0`，md5 `9eccfd46...`）两个 IDB 的逆向观察。
> 用途：作为**写 IDA 插件辅助逆向 iosd** 的结构基础。只讲结构，不讲破解。

---

## 1. iosd 是什么

IOS-XE = **Linux 内核 + 一组用户态进程**。iosd（IOS daemon）是其中最大的一个进程，承载 IOS 的：

- CLI 命令解析与配置（config / exec）；
- 路由/交换协议（BGP、ISIS、OSPF、EIGRP、RIP……）；
- 许可判定（CSL / Smart License）；
- 平台/数据面的控制面逻辑（通过 fman 与转发面交互）。

其它进程（`cmand`、`fman_rp`、`fman_fp`、`confd`、`nginx`、`pubd`、`vtyc`……）各司其职，与 iosd 通过 IPC 通信（见 §7、§8）。

### 1.1 启动方式

由进程管理器拉起（实测 17.16 `ps`）：

```
/usr/bin/pman -p linux_iosd-image -l linux_iosd_image_pman -i 0 -- \
    /usr/binos/bin/linux_iosd-image -n 32768 -m 1024 -c /config
```

`-n` 线程/对象数、`-m` 内存、`-c` 配置目录。

### 1.1.1 启动流程（start → main → 子系统分类 init → 模块 init → 线程 → 调度循环）

ELF 入口 `0xb2463a0` = `start`（标准 glibc `_start`），反汇编：

```asm
start:
  xor ebp, ebp
  mov rdi, cs:main           ; main
  xor ecx, ecx               ; init = NULL
  xor r8d, r8d               ; fini = NULL
  call cs:__libc_start_main_ptr
  hlt
```

即 `start → __libc_start_main(main, argc, argv, NULL, NULL, ...) → main`。**注意 init/fini 传的是 NULL**，印证 `.init_array` 是空的（见 §1.2 后的段说明）。

`main`（`sub_D710460`，0x757）的启动流程（实测反推）：

1. **初始化子系统分类表**：按 13 个**子系统分类（category）** 依次初始化，顺序固定：

   ```
   1 Kernel   2 Library   3 Driver   4 Protocol   5 Management   6 Registry
   7 SystemInit  8 EHSA  9 Pre-Driver  10 IFS  11 Microcode  12 Pre-EHSA  13 License
   ```

   每个分类调用回调 `(off_33EDF670, category_id, "分类名")` 把该分类下的子系统初始化。

2. **建子系统 init 队列**：`"Subsys Pending"` / `"Subsys Init Malloc List"` / `"Subsys Init Loadtime List"`（`sub_D6FD8F0`）。

3. **模块 init 分发**：`sub_D7127D0(sub_D710240)` —— 遍历 `subsys_header_section` / `module_header_section`（模块名带 `libiosd_shr_` / `libiosd_crb_shr_` 前缀、magic `0x15055cc1`），逐个调用模块 init 回调（这就是替代 `.init_array` 的自定义模块初始化）。

4. **进程/线程启动**：遍历 "Subsys Pending" 队列，逐个 `sub_D710BC0(entry, ...)` 启动各子系统的线程/进程。

5. **进入调度循环**：`sub_D767810(v11)` —— 进入主调度器（job 队列 + 定时器轮），此后 iosd 进入常驻的消息/调度循环。

### 1.1.2 运行态（线程 + 协作式调度器 + vtcp 虚拟进程）

- 底层是 Linux **pthread**；之上叠一层 iosd 自己的**协作式调度器**（`schedulerJobList` + mutex、`Timer Wheel ... scheduler mode`）。
- 仍保留 IOS 经典的**虚拟进程/线程**抽象：`vtcp`（`alg_vtcp_service_msg_*`）、`__be_process_*`。
- 权限用 **`priv_level`（1-15）** 数据结构，挂在 CLI 会话与命令节点上。

### 1.2 二进制规模

| 项 | 17.9.04a | 26.01.02 |
|---|---|---|
| 文件大小 | ~482 MB | ~938 MB |
| 格式 | ELF64 x86-64 **PIE (DYN)**，stripped | 同左 |
| 函数总数 | — | 1,163,528（有名字 ~83K，无名字 ~108 万） |
| 字符串数 | ~110 万 | ~125 万 |
| 段数 | — | 13,163 |
| imagebase | `0x555555554000` | `0x0` |

stripped 后只剩 `.dynsym`（导入符号，~45K）和少量保留符号，绝大多数函数是 `sub_XXXX`。

---

## 2. 编译单元与源码组织（有 .c 编译单元概念）

**结论：有编译单元概念。** 二进制里嵌入了源码路径字符串，格式统一：

```
../VIEW_ROOT/cisco.comp/<component>/<module>/src/<file>.c
```

实测采样（26.01.02 的 `.rodata` 区）：

| 源码路径 | component | module |
|---|---|---|
| `../VIEW_ROOT/cisco.comp/cfc_cefmpls/cef/src/ipv4/ipv4fib_rp_stats.c` | cfc_cefmpls | cef |
| `../VIEW_ROOT/cisco.comp/parser/src/parser_chunk_malloc.c` | parser | parser |
| `../VIEW_ROOT/cisco.comp/fnf/config/model/field_spec/src/fnf_cm_field_spec.c` | fnf | config/model/field_spec |
| `../VIEW_ROOT/cisco.comp/ethernet-efp/core/src/ether_infra.c` | ethernet-efp | core |
| `../VIEW_ROOT/cisco.comp/ngdns/src/validator/autotrust.c` | ngdns | validator |

- `cisco.comp` = 组件根目录；
- `<component>` ≈ **子系统**（cfc_cefmpls、parser、fnf、ngdns……）；
- `<module>` ≈ **模块**（cef、config、validator……）；
- `src/*.c` = 编译单元。

> 对 IDA 插件意义：这些 `.c` 路径字符串可以当作"编译单元/组件"的标签，把函数、字符串按组件聚簇；甚至可以据此反推一个函数属于哪个 component（靠附近的 `.c` 路径引用或 `.btrace` 段相邻性）。

---

## 3. 子系统与模块（自定义 ELF 段）

iosd 用三个**自定义 ELF 段**描述子系统/模块结构：

| 段 | 位置（26.01.02） | 大小 | 含义 |
|---|---|---|---|
| `subsys_header_section` | `0x37a014c8` | 546 KB | **子系统表** |
| `module_header_section` | `0x37a8f8a0` | 480 B | **模块表** |
| `module_link_section` | `0x37a8fa80` | 264 B | **模块链接表** |

条目头结构（从 `module_header_section` 采样）：

```
c1 5c 05 15   ← magic 0x15055cc1（固定）
c1 5c 05 15   ← 同上（重复）
00 00 00 01 00 00 00 01
00 00 00 00 00 00 00 00
XX XX XX XX   ← 指针（子系统/模块名或元数据）
...
```

即：固定 magic（0x15055cc1 ×2）+ 一组指针。**子系统（subsys）是更高层的分组，模块（module）是下一层**，二者由 `module_link_section` 串联。这是 Cisco 自研的"模块化链接布局"——每个子系统的代码+数据+元数据被打成一个"模块"，靠这些头组织。

**subsys 条目的实测结构**（以 `generic_atom` 子系统为例，name 指针落在 `0x37a674e0`）：

```
偏移        内容
+0x00  flags（0x01000000 ×2 等）
+0x10  name 指针 → "generic_atom" 字符串（0x058164ec）
+0x18  指针（→ 代码/数据，如 init 函数或代码区间）
+0x20  数值（0x400，疑似 size）
+0x28  指针（→ 另一结构）
...
```

即每个 subsystem 条目 = flags + **名字符串指针** + 代码/数据指针 + 大小等元数据。子系统名（"generic_atom"、"chasfs"、"mcast"、"parser"、"ipv4fib"……）都是独立字符串，被这些表引用。

配套的查找函数：**`subsys_find_by_name(name)`**（出现在调试断言串里 `subsys_find_by_name("generic_atom")`），按名字查子系统。

> **IDA 插件价值最高的一块**：解析 `subsys_header_section` / `module_header_section` / `module_link_section` 的条目，就能 dump 出完整"子系统→模块→地址区间"清单，得到真正意义上的模块划分（比靠函数名前缀猜完整得多）。

### 3.1 靠函数名前缀也能划出子系统（近似）

保留符号的前缀是子系统线索：

| 前缀 | 子系统 | 说明 |
|---|---|---|
| `__be_*` | be 运行时库 | 大端内存/printf/字符串/buginf |
| `__be_dbal_*` | DBAL | 数据模型抽象层 |
| `csl_*` | CSL | 本地许可 |
| `sl_*` / `smart_*` / `tbl_smart_license_*` | Smart License | SL + confd 表 |
| `chasfs_*` | chasfs | chassis 文件系统（运行时 KV） |
| `cyan_*` | CDB | chassis 属性数据库 |
| `vxe_*` | VXE 平台 | 虚拟化平台抽象 |
| `cman_*` / `fman_*` / `hmann_*` | 管理器 | chassis/forwarding/host 管理器 |
| `mqipc_*` | MQIPC | 消息队列 IPC |
| `vty_*` | VTY | CLI 会话 |
| `.` 前缀（如 `.__be_malloc`） | .plt 导入 | 外部库 thunk（size 0x6） |

---

## 4. 运行时约定（读懂反汇编必须知道）

### 4.1 be 指针（big-endian pointer）

大量指针按大端存储/传递，高位 `0x8000000000000000` 标记：

```c
v = *(slot) & 0x7FFFFFFFFFFFFFFFLL;   // 去 be 标记
v = _byteswap_uint64(v);               // 大端 → 小端
```

- `| 0x8000000000000000` = 标记 be 指针；
- `& 0x7FFFFFFFFFFFFFFF` = 取真实地址；
- `_byteswap_ulong/uint64` = 数据大端存储，读时换序；
- `off_XXX` 命名 = "XXX 处存的是指针"。

### 4.2 入口计数器

几乎每个函数开头：

```c
++qword_45165FE0;   // profiling 埋点，无逻辑含义
```

### 4.3 btrace / buginf（崩溃回溯埋点）

`ios_BTf_0/1/5`、`_be_btrace_intercept_buginf`、`_be_get_ios_buginf_id` 是崩溃回溯系统。函数里的 `"\nVXE-CSL-DBG:..."` 这类调试串 + `ios_BTf_*` 调用，是**定位函数用途的绝佳锚点**。每个函数配一个 `.btrace_*` 段（GUID）做 buginf 追踪 ID。

### 4.4 模拟环境变体

`_mock` / `_llvmclonedsim` / `_system` 后缀是测试/模拟分支。真实逻辑在：

```c
if (_be_is_g_ngc_simulation_env && _be_is_ngconfig_simulation_enable(1))
    return sub_XXX_sim(...);   // 模拟分支，忽略
// ↓ 真实逻辑
```

---

## 5. 核心架构：消息传递（message handler / dispatch）

**iosd 内部是消息驱动的**——各子系统通过"消息"通信，而不是直接函数调用。命名规律：

| 后缀 | 含义 |
|---|---|
| `_message_handler` | 单个消息处理器 |
| `_message_dispatch` | 消息分发（把消息路由到 handler） |
| `_message_dispatch_init` | 注册本子系统的 handler（初始化） |
| `_message_create` / `_message_destroy` | 消息分配/释放 |
| `_message_len` | 消息长度 |

实测例子：

```
csl_license_message_dispatch / csl_license_message_dispatch_init
csl_license_csl_license_request_msg_message_handler
csl_license_csl_license_release_msg_message_handler
ofa_message_dispatch / ofa_message_dispatch_init
fman_rp_message_dispatch / fman_rp_message_dispatch_init
vty_mgt_vty_req_message_handler
```

> 对 IDA 插件：按 `_message_dispatch_init` 就能找到"每个子系统注册了哪些 handler"；按 `_message_handler` 能枚举所有消息入口。这是理解 iosd 模块交互的主线。

---

## 6. confd 数据模型（tbl_*）

每个特性（BGP、ISIS、OSPF、许可……）都有一套 **confd 数据模型**，对应一组 `tbl_*` 访问函数（由 YANG 生成）：

```
tbl_bgp_state_bgp_state_singleton_id_get_first/get_next/search
tbl_isis_instance_isis_tag_type_tag_get_first/...
tbl_ospf_static_neighbor_ospf_static_neighbor_address_get_first/...
tbl_eigrp_ios_oper_instance_..._search
tbl_smart_license_authorization_list_table_...
```

- `tbl_<feature>_<table>_<field>_get/set/search` = 配置/状态数据的 getter/setter。
- 这些是 iosd 内的数据模型层（confd 库 `libsmart_lic_oper.so` 等提供底层）。

> 对 IDA 插件：`tbl_` 前缀直接给出"哪个特性、哪张表、哪个字段"，是理解"配置存在哪、怎么读写"的入口。

---

## 7. 进程间通信（MQIPC）

iosd 与其它进程通过 **MQIPC（Message Queue IPC）** 通信：

```
mqipc_enqueue
__be_iosd_init_and_open_mqipc_writer
__be_iosd_write_one_mqipc_msg
__be_wsman_iosd_init_mqipc          ← wsman 进程 ↔ iosd
__be_lman_init_mqipc                ← lman ↔ iosd
```

即：**跨进程也是"消息"**，走 MQIPC 队列。iosd 内的 `_message_dispatch` 和跨进程 MQIPC 是同一套消息模型的内外两个边界。

---

## 8. CLI 执行流（VTY）

CLI 输入（telnet/SSH/console）不是直接进 iosd，而是：

```
用户 → vtyc/vty 会话 → vty_req_message → iosd → parser 子系统 → 命令 handler
```

关键符号：

```
vty_mgt_vty_req_message_handler
vty_req_message_vty_req_type_get / vty_req_message_vty_msg_get
```

- CLI 请求被封装成 `vty_req_message`（消息），由 iosd 的 `vty_mgt_*` handler 接收；
- 命令字符串交给 **parser 子系统**（component `parser`，源码 `cisco.comp/parser/src/...`）解析；
- 解析结果分发到对应命令的处理函数（parse chain / command table）。

### 8.1 parser 命令注册表（命令 → handler 的关键）

parser 子系统的核心是三个函数/结构：

| 符号 | 地址（26.01.02） | 作用 |
|---|---|---|
| `parser_add_command`（`sub_19601E40`，0x471） | 命令注册；根结构在 `off_36A365F8`（初始化 magic `0x78563412`） |
| `parse_cmd`（`sub_F3B6FF0`，0x85d） | 执行一条命令；解析命令串后**通过函数指针表分发到 handler** |
| `parse_chain` / `parse_cmd_syntax` | 命令解析树结构（`cfc_uid_parse_chain`、`flow_exp_ios_code_parse_chain`、`rbm_parse_cmd` 等都是它的实例） |

配套调试串确认了执行链：

```
"\nCall parse_cmd '%s'"          ← parse_cmd 入口（sub_F3B6FF0）
"Unable to parser_add_command"   ← parser_add_command 失败（sub_19601E40）
"\nWSMA-exec: parse_cmd.rc=%d"   ← WSMA 也走 parse_cmd
```

`parse_cmd` 内部通过函数指针把命令路由到具体 handler（实测 `sub_F3B4580` 被注册为某个命令的 handler）。也就是说：**CLI 命令 = parse_chain 树上的一个节点，节点上挂 handler 函数指针**。

### 8.1.1 真正的命令注册：`icm_add_node_to_parse_tree`

进一步定位到主 CLI parser 的命令注册函数（比 `parser_add_command` 更底层）：

| 符号 | 地址 | 作用 |
|---|---|---|
| `icm_add_node_to_parse_tree`（`sub_C2FA1D0`，0xccd） | 0xC2FA1D0 | 向 parse 树加节点（命令注册的核心） |
| `icm_update_cli_parser_tree_info` | 字符串 0x687b25a | 更新 parse 树信息 |

调试串实锤了节点分配：

```
"First Node allocated: %p level:%d line:%s"   ← 节点 = (指针, level, 命令行字符串)
```

**parse 树节点结构（72 字节，经 `icm_print_cli_tree` 反汇编实锤）**：

节点由 `sub_1E53E600(72)` 分配。真实字段（disasm 确认）：

```
+0x00 (0)   指针0（be 指针，大端，byteswap）
+0x08 (8)   指针1（be 指针）
+0x10 (16)  指针2（be 指针）
+0x18 (24)  指针3（be 指针）
+0x20 (32)  指针4（be 指针）      ← 共 5 个指针（Ptr[%p:%p:%p:%p:%p]）
+0x28 (40)  level（DWORD，大端）
+0x2C (44)  （4 字节填充）
+0x30 (48)  命令串指针（be 指针，指向字符串缓冲区）
+0x38 (56)  flags（DWORD）
+0x3C (60)  offset（命令串在缓冲区内的偏移）
+0x40 (64)  size（命令串长度）
+0x44 (68)  WORD 索引（大端）
+0x46 (70)  （2 字节填充）
```

**5 个指针（+0/+8/+16/+24/+32）是树链**（前驱/next/child 等），**命令串在 +48（指针）+offset(+60)/size(+64)**，**parse_func 是 5 个指针之一（还需定点是哪个）**。

**节点数组**：树根结构里有两个节点指针数组（`root + 8*index + 48` 与 `root + 8*index + 8240`），`index` = 节点里的 WORD(+68)。

**icm（IOS Command Manager，命令树子系统）关键函数**（`subsys_header_section` 里的 `icm_main` 入口）：

> icm 就是**管理 CLI 命令树（parse 树）+ 配置操作（diff/save/replay）的子系统**。整个程序的 CLI 命令树**只有一棵**，由 icm 维护。它通过 **DMI（Data Model Interface）** 回调处理配置操作（op=1 save / op=2 diff / op=3 / op=12），这些回调里反复调用 `sub_C2F4C80(op, "DMI", ...)`。之前以为的"多棵树"是错的——`qword_37B5323C` 是 **config diff 时临时构建的 diff 结构**（用完即删），不是第二棵命令树。

**subsys 条目结构（实锤，以 icm_main 为例，0x37a10528 起）**：

```
+0x28  magic 0x15055cc1 ×2
+0x30  flags (0x01000000 ×2)
+0x40  name 指针 → "icm_main" 字符串 (0x4fffa5f)
+0x48  函数指针 → icm_main 函数 (0xC2F5700)
+0x50  大小 (0x400)
+0x58  另一指针/偏移
```

| 函数 | 地址 | 作用 |
|---|---|---|
| `icm_main` | `sub_C2F5700` (0x8f) | icm 子系统主入口，注册 DMI 回调（sub_C2F5790/sub_C2F5890/sub_C2F5AB0） |
| `icm_print_cli_tree` | `sub_C2F7B50` | **打印 CLI 树**（调试，遍历树结构；输入 a1=树根、a2=起始节点） |
| `icm_populate_diff_tree` | 0x4fffade | 填充 diff 树 |
| `icm_delete_parser_tree` | 0x53a5f49 | 删除 parse 树 |
| `icm_add_cli_str_to_parser_tree` | `sub_C2FA1D0` | 命令串入树 |

> 节点结构已 100% 确认，可据此写运行时 dump/遍历逻辑。剩下的只是"树根全局"的精确地址。

**handler 叫 `parse_func`**（IOS 约定，命令处理函数）：字符串证据 `"Parser nvgen a parse_func"`、`"Parser test nvgen a parse_func"`、`*_parse_func`、`*_cmd_handler`（如 `clear_aaa_counters_cmd_handler`、`pubfn_command_handler`）。

**两条命令相关路径**（重要区分）：

| 路径 | 函数 | 作用 | 是否写 handler |
|---|---|---|---|
| **命令注册**（模块 init） | 未完全定位 | keyword + parse_func → 建树节点，填 +0/+8 | ✅ 写 handler |
| **命令解析/入树**（运行时） | `sub_C2F6BD0`("Generate CLI command")、`sub_C2FA1D0`(`icm_add_cli_str_to_parser_tree`) | 命令串匹配进树 | ❌ 不写 handler |

**树根全局**（供插件定位）：调用链 `sub_C2F4C80 → sub_C2F60B0(icm_check_and_create_diff_tree) → sub_C2F6BD0 → sub_C2FA1D0` 用的树根来自全局：

```
qword_37B5323C（0x37B5323C）= diff 结构根指针（运行时 heap/bss，静态为 0，config diff 时临时用）
unk_37B53230（0x37B53230）  = 相关标志
```

调试串 `"Generate CLI command is_old:%d root_cli:%p"` 里的 `root_cli` 就是这个根。

> **澄清（之前"多棵树"说法有误）**：整个 CLI 命令树**只有一个**，`qword_37B5323C` 是 **config diff 的临时结构**（不是第二棵命令树）。命令树根与 diff 结构根是两个东西。命令树根还需在 icm/parser 注册路径里定位（已定位到 `icm_main` 入口，见上）。

**handler = parse_func 在节点 +0x08（已实锤）**：`icm_print_cli_tree` 打印 `Ptr[%p:%p:%p:%p:%p]` 的 5 个指针即节点 +0/+8/+16/+24/+32，其中 +0=命令串、+8=parse_func（handler）、+16=前驱、+24=next、+32=child。

> **IDA 插件"定位某条 CLI 命令执行流"的做法（运行时）**：
> 1. 静态拿到树根全局（icm_main 初始化链里）；
> 2. IDA 调试器 attach 到 iosd 进程（或 `request platform software process core ios rp active` 生成 core / `memdump -p PID -a addr -s size` 读内存）；
> 3. 读树根 → 按节点数组（`root + 8*index + 48` / `+8240`）遍历 72 字节节点 → 读 +0（命令串）+8（parse_func）→ dump "命令 → handler" 全表。

### 8.1.2 命令数据结构不止一套（cdl.xml 勘误）

**2026-10-29 复核**：结构表示相似不等于同一套命令集合。CDL、iosd 静态语法图、ICM 配置文本树需要分别分析：

| 结构 | 是什么 | 规模 | 内容 |
|---|---|---|---|
| **iosd 静态 transition 图** | 子系统注册的 40 字节候选语法节点 | 当前发现入口的图有 101,521 节点 | 部分关键词、参数、条件、EOL 和 handler；尚未恢复全部模式与命令路径 |
| **ICM 配置文本树**（`icm_*` 相关观察） | 72 字节配置/差异节点 | 未枚举全 | 不应继续当成主 CLI 语法定义树；`+8` 不是已确认 handler |
| **cdl.xml**（"BinOS Command Set"） | XML 定义及带注解的连接图 | 78,381 个 GUID 节点，另有 4,375 个 request | keyword 44,424 / value 6,993 / eol 4,373 / filter 22,591；主根可达 4,372 个 EOL |

cdl.xml 头部：`<!-- BinOS Command Set. Auto Generated XML File. Do Not Edit. July 2026. BinOS CDL Compiler. -->`

- `<request name="auth_mgr_test_*_eol_auto_req" bundle="..."/>` —— 保留请求名称与 bundle；不能仅凭名称后缀认定为“自动化命令”或建立 handler 映射；
- `<eol guid="..." name="..._eol_auto_eol"/>` —— eol（end-of-line）节点带 GUID。

这份 XML 有 152,098 条显式边，其中 89,904 条含 `set`、`filter-ref` 或 `set-tdl` 元数据。过滤器定义不直接作为显式边端点，但边上存在 46,895 个 `filter-ref`，不能在遍历时丢弃这些条件线索。

先前通过 `name="interface"` 的计数认定没有配置命令，依据不充分：`name` 是内部名称，`str` 才是输入关键词；本文件有 171 个 `str="interface"` 节点。主根的 `config` 子图完整遍历仅有 `config hw-obfl dummy <cr>` 与 `config sdm dummy <cr>`，这里不能等同于通常的全局/接口配置模式，也不能据此推断所有版本 CDL 的覆盖范围。

新版遍历器 `tools/walk_cdl.py` 保留完整图及注解，修正旧 C++ DFS 错误屏蔽共享后缀的问题。主根显式图有 652,569,212 条结构路径，默认输出 4,772 条示例，覆盖全部 4,372 个可达 EOL；条件未求值，这不是可执行命令总数。结果见 `reports/cdl-walk-20261029/index.html` 和 `summary.json`。CDL 可作为比对来源，iosd 自身的命令集合仍需由其注册、解析和分派代码独立验证；未出现在 CDL 中不能直接判为 undocumented。

> **命令数据结构的完整清单待办**：iosd 里至少存在 ① IOS CLI parse 树（icm_*）② cdl.xml（BinOS 命令集）③ WSMA/mcp 的命令映射 ④ confd 数据模型（YANG 定义的 CLI 命令）。要完整找全，需逐个逆向。

---

## 9. Web UI 执行流（nginx → WSMA → CLI → iosd）

Web UI 的操作绝大多数会转成 CLI 命令，经 **WSMA（Web Services Management Agent）** 传导进 iosd：

```
浏览器 → nginx → WSMA(wsman 进程) → MQIPC → iosd
                                    └─ 内部转成 CLI 命令 / 配置写 confd
```

关键符号：

```
__be_wsman_iosd_init_mqipc          ← wsman 用 MQIPC 连 iosd
```

Lua 层（Web UI 后端，`var/scripts/lua/features/*.lua`）里的 `WSMAGetData("show ...")` / `WSMAApplyCmd(...)` 就是把前端操作变成 CLI 命令/配置，再经 wsman → MQIPC → iosd 执行。

> 对 IDA 插件：从 wsman 的 MQIPC 消息类型，可以追到"哪些 CLI 命令是被 Web UI 触发的"，反之从 CLI 命令反查 Web UI 入口。

---

## 10. 数据平面交互（fman_rp / fman_fp / QFP / punt）

iosd 是**控制面**，数据面是 QFP（Quantum Flow Processor，由 `fman_fp` 进程承载）。交互链路：

```
iosd（控制面） ↔ fman_rp（RP 侧转发管理器） ↔ fman_fp（FP 侧） ↔ QFP 硬件/虚拟转发
```

关键符号：

```
fman_rp_message_dispatch / fman_rp_message_dispatch_init
fman_rp_message_get_info
fman_fp_fwd_caps_*                  ← 转发能力（FP 上报）
qfpmib_stats_tdl_*                  ← QFP 统计（MIB）
```

**"从数据平面拿数据"** 的方式：控制面要数据时，通过 `fman_rp_message_*` 发消息给 fman_fp，fman_fp 从 QFP 读回，再以消息回报。需要上送控制面的报文走 **punt**（从数据面"punt"到控制面）：

```
tbl_ipv4_swi_punt_feat_*            ← punt 特性表
```

> 归属：fman（forwarding manager）是独立的子系统（`cisco.comp` 里的 component），不是协议的一部分。数据面交互统一走 fman 这条消息通道。

---

## 11. 协议子系统（BGP / ISIS / OSPF / EIGRP ……）

每个协议都是**独立子系统/组件**，有自己的：

1. confd 数据模型（`tbl_bgp_*`、`tbl_isis_*`、`tbl_ospf_*`、`tbl_eigrp_*`）；
2. 消息处理器（协议报文收发、邻居状态机）；
3. 源码 component（如 `cisco.comp/.../bgp/...`）。

即：**协议 = component（子系统）+ confd 表 + 消息 handler**，三者对应同一套东西。`ping`、`ssh` 这类"服务型"功能也类似（`ping` 走数据面/控制面消息，`ssh` 是独立子系统）。

---

## 12. 函数表清单（供 IDA 插件枚举）

| 表 | 位置/命名 | 作用 |
|---|---|---|
| `subsys_header_section` | `0x37a014c8`（546KB） | 子系统表 |
| `module_header_section` | `0x37a8f8a0`（480B，magic `0x15055cc1`） | 模块表 |
| `module_link_section` | `0x37a8fa80`（264B） | 模块链接 |
| `CRFT_func` | `0x44e3c398`（7.7MB，静态全 `0xFF`） | 运行时函数表（运行时填充，函数地址↔元数据） |
| 函数指针注册表 | `off_XXX + offset` 的 get-helper | 回调/检查函数槽（许可等） |
| `.plt` / `.got` | 标准 ELF | 外部导入（`.dynsym` ~45K） |
| `liData` / `liDummy` | 小段 | 库信息 |

---

## 13. 面向 IDA 插件的落点清单

写插件时，这些是可以程序化提取的结构信息：

1. **模块划分**：解析 `subsys/module/link` 三个段 → 子系统清单（名字+地址区间）。
2. **组件标签**：抓 `.c` 路径字符串 → 把函数/字符串按 `cisco.comp/<component>/<module>` 聚簇。
3. **消息入口**：枚举 `_message_handler` / `_message_dispatch_init` → 每个子系统的消息接口。
4. **数据模型**：枚举 `tbl_*` → 特性/表/字段三层结构。
5. **CLI 命令**：遍历 parse 树（72 字节节点：+0 命令串 / +8 parse_func / +16 前驱 / +24 next / +32 child / +68 index），dump "命令串 → handler" 映射（节点结构已确认，树根待钉）。
6. **be 指针**：识别 `|0x8000...`/`&0x7FFF...`/`byteswap` 模式，自动解析跨大端指针引用。
7. **函数语义标注**：用调试串（`\nVXE-CSL-DBG:` 等）+ `ios_BTf_*` 锚点给函数打标签。
8. **子系统分类**：main 里的 13 个 init 分类（Kernel/Library/Driver/Protocol/Management/Registry/SystemInit/EHSA/Pre-Driver/IFS/Microcode/Pre-EHSA/License）可给每个子系统打"分类"标签。

### 13.1 函数名恢复方法（stripped 二进制最可靠的一招）

函数名（如 `icm_add_node_to_parse_tree`）不是靠 btrace 猜的，而是靠**调试日志里的 `__func__` 字符串字面量**：

```c
// 源码里
dbg("\n%s(%d)-INFO-DET: ", __func__, __LINE__, ...);
// 编译器把 __func__ 内联成字符串
sub_C2FB830("\n%s(%d)-INFO-DET: ", "icm_add_node_to_parse_tree", 537, ...);
```

**识别规则**：搜 `"%s(%d)-..."` 这类格式串，其相邻的字符串字面量 = 函数名，紧跟的整数 = 源码行号。此法对 iosd 命中率极高（几乎所有带调试日志的函数都能恢复名字）。三种手段对比：

| 手段 | 是什么 | 是否明文 | 用途 |
|---|---|---|---|
| `%s(%d)` 调试串 | `__func__` 字符串字面量 | ✅ 明文 | 静态直接恢复函数名 |
| `.c` 源码路径 | `VIEW_ROOT/.../xxx.c` | ✅ 明文 | 恢复编译单元/组件归属 |
| `.btrace` LUID | GUID | ❌ 非明文 | 崩溃回溯（需运行时符号化） |

### 13.2 运行时内存 dump 方法（B 方案，供插件/动态分析）

在设备上直接读 iosd 进程内存（26.01.02 实测）：

| 手段 | 用法 | 说明 |
|---|---|---|
| **memdump**（Cisco 自带） | `memdump -p <pid> -a <addr> -s <size> [-x/-c/-w]` | 逐地址读进程内存，输出 hex/char |
| `/proc/PID/mem` | `dd if=/proc/<pid>/mem bs=1 skip=<addr>` | 直接读进程内存 |
| **core dump** | `request platform software process core ios rp active` | 生成 iosd core（`write core` 在 26.x 是 not implemented） |

**地址映射**：`runtime = 0x555555554000 + IDB地址`（26.01.02 实测验证；`hseck9` 字符串 IDB `0x74bfc98` → runtime `0x55555ca13c98`）。设备上有 python3（3.12），可写脚本扫描堆/遍历树。

> iosd 的 `iosd PID` 用 `ps aux | grep linux_iosd-image | grep -v grep | grep -v pman` 取。

---

## 14. 待补充（下一步深挖）

- [x] ~~子系统表条目结构~~ —— 已确认（以 icm_main 为例）：magic 0x15055cc1 + flags + name 指针 + 函数指针 + size（`subsys_find_by_name` 配套）。
- [x] ~~parse 节点结构~~ —— **完全确认**（`icm_print_cli_tree` 实锤）：72 字节，+0 命令串 / +8 parse_func / +16 前驱 / +24 next / +32 child / +40 level / +56 flags / +68 index；节点数组 `root+8*index+48`、`+8240`。
- [x] ~~handler 字段偏移~~ —— 确认 = **+8（parse_func）**。
- [x] ~~启动流程~~ —— 已定位 main（`sub_D710460`）：13 个 init 分类 → 模块 init 分发（`sub_D7127D0`）→ 线程启动 → 调度循环；`.init_array` 为空。
- [x] ~~运行时 dump 工具~~ —— 确认：`memdump -p PID -a addr -s size`（Cisco 自带）、`/proc/PID/mem` 可读、地址映射 `runtime = 0x555555554000 + IDB地址`（用 `hseck9` 字符串验证）、`request platform software process core ios rp active`（生成 core，`write core` 在 26.x 是 not implemented）。
- [ ] **树根全局精确定位** —— icm 子系统入口 `icm_main(0xC2F5700)` 已找到；沿它注册的 DMI 回调 + 注册路径把命令树根全局钉死。
- [ ] **完整 dump 子系统→模块清单**（`subsys_header_section` 546KB 全表解析成列表）。
- [ ] **命令数据结构全清单**（① IOS CLI parse 树 ② cdl.xml ③ WSMA/mcp ④ confd YANG CLI）——逐个逆向。
- [ ] `CRFT_func` 运行时格式（崩溃回溯如何符号化）。
- [ ] WSMA 的 MQIPC 消息类型 → CLI 命令映射。
- [ ] fman_rp/fp 消息类型清单（控制面↔数据面的完整消息集）。
