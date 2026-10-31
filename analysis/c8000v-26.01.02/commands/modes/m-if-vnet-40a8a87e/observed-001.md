# if-vnet · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-009652

```text
(config-if-vnet)# bandwidth <number:1..10000000> <cr>
```

Handler ` RVA 0xE40BD30 `；selector ` 0 `；EOL ` RVA 0x341499B0 `。

模式根 ` RVA 0x35874330 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Bandwidth in kilobits。

[条件 C-0b3f9062179a0dbb](../../evidence/conditions-sets-005.md#c-0b3f9062179a0dbb) · [参数 P-742a391ac073861d](../../evidence/parameters-sets-009.md#p-742a391ac073861d)

### observed_connections-009653

```text
(config-if-vnet)# default bandwidth <cr>
```

Handler ` RVA 0xE40BD30 `；selector ` 0 `；EOL ` RVA 0x341499B0 `。

模式根 ` RVA 0x35874330 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-00451fd826a3cfac](../../evidence/conditions-sets-001.md#c-00451fd826a3cfac) · [状态效果 S-b22138913a5da97e](../../evidence/state_effects-sets-038.md#s-b22138913a5da97e)

### observed_connections-009648

```text
(config-if-vnet)# default delay <cr>
```

Handler ` RVA 0xE40C610 `；selector ` 1 `；EOL ` RVA 0x34149C48 `。

模式根 ` RVA 0x35874330 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-24fddb6d6a512b2d](../../evidence/conditions-sets-014.md#c-24fddb6d6a512b2d) · [状态效果 S-b22138913a5da97e](../../evidence/state_effects-sets-038.md#s-b22138913a5da97e)

### observed_connections-009650

```text
(config-if-vnet)# default exit-if-vnet <cr>
```

Handler ` RVA 0x12467600 `；selector ` 0 `；EOL ` RVA 0x35876760 `。

模式根 ` RVA 0x35874330 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-457532ab776bf8d3](../../evidence/conditions-sets-027.md#c-457532ab776bf8d3) · [状态效果 S-b22138913a5da97e](../../evidence/state_effects-sets-038.md#s-b22138913a5da97e)

### observed_connections-009645

```text
(config-if-vnet)# delay <number:1..16777215> <cr>
```

Handler ` RVA 0xE40C610 `；selector ` 1 `；EOL ` RVA 0x34149C48 `。

模式根 ` RVA 0x35874330 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Throughput delay (tens of microseconds)。

[条件 C-34b10e1f21edf77d](../../evidence/conditions-sets-020.md#c-34b10e1f21edf77d) · [参数 P-89ee4bfed8a1e4a3](../../evidence/parameters-sets-011.md#p-89ee4bfed8a1e4a3)

### observed_connections-009646

```text
(config-if-vnet)# exit-if-vnet <cr>
```

Handler ` RVA 0x12467600 `；selector ` 0 `；EOL ` RVA 0x35876760 `。

模式根 ` RVA 0x35874330 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-457532ab776bf8d3](../../evidence/conditions-sets-027.md#c-457532ab776bf8d3)

### observed_connections-009651

```text
(config-if-vnet)# no bandwidth <cr>
```

Handler ` RVA 0xE40BD30 `；selector ` 0 `；EOL ` RVA 0x341499B0 `。

模式根 ` RVA 0x35874330 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-749dcaeb097cebc8](../../evidence/conditions-sets-045.md#c-749dcaeb097cebc8) · [状态效果 S-35570e6b4147866c](../../evidence/state_effects-sets-012.md#s-35570e6b4147866c)

### observed_connections-009647

```text
(config-if-vnet)# no delay <cr>
```

Handler ` RVA 0xE40C610 `；selector ` 1 `；EOL ` RVA 0x34149C48 `。

模式根 ` RVA 0x35874330 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-24fddb6d6a512b2d](../../evidence/conditions-sets-014.md#c-24fddb6d6a512b2d) · [状态效果 S-35570e6b4147866c](../../evidence/state_effects-sets-012.md#s-35570e6b4147866c)

### observed_connections-009649

```text
(config-if-vnet)# no exit-if-vnet <cr>
```

Handler ` RVA 0x12467600 `；selector ` 0 `；EOL ` RVA 0x35876760 `。

模式根 ` RVA 0x35874330 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-457532ab776bf8d3](../../evidence/conditions-sets-027.md#c-457532ab776bf8d3) · [状态效果 S-35570e6b4147866c](../../evidence/state_effects-sets-012.md#s-35570e6b4147866c)
