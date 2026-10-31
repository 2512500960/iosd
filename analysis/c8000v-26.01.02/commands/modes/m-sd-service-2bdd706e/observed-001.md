# sd-service · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-009603

```text
(config-sd-service)# controller <cr>
```

Handler ` RVA 0x10F26810 `；selector ` 27 `；EOL ` RVA 0x3525F030 `。

模式根 ` RVA 0x35239600 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-009602

```text
(config-sd-service)# exit <cr>
```

Handler ` RVA 0x10F263D0 `；selector ` 0 `；EOL ` RVA 0x3526FDB0 `。

模式根 ` RVA 0x35239600 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0bf2af05e90701c8](../../evidence/conditions-sets-005.md#c-0bf2af05e90701c8)

### observed_connections-009605

```text
(config-sd-service)# no controller <cr>
```

Handler ` RVA 0x10F26810 `；selector ` 27 `；EOL ` RVA 0x3525F030 `。

模式根 ` RVA 0x35239600 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-0dc50720ad96cf70](../../evidence/state_effects-sets-003.md#s-0dc50720ad96cf70)

### observed_connections-009606

```text
(config-sd-service)# no segment <cr>
```

Handler ` RVA 0x10F34980 `；selector ` 26 `；EOL ` RVA 0x3525EDB0 `。

模式根 ` RVA 0x35239600 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5715572b87f99618](../../evidence/conditions-sets-034.md#c-5715572b87f99618) · [状态效果 S-1bc41b857fc3416c](../../evidence/state_effects-sets-006.md#s-1bc41b857fc3416c)

### observed_connections-009604

```text
(config-sd-service)# segment <string> <cr>
```

Handler ` RVA 0x10F34980 `；selector ` 26 `；EOL ` RVA 0x3525EDB0 `。

模式根 ` RVA 0x35239600 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Enter a segment name. Max - 63 chars。

[条件 C-bbb3ae996fb5ef75](../../evidence/conditions-sets-072.md#c-bbb3ae996fb5ef75) · [参数 P-27ff632f4cd3a8e2](../../evidence/parameters-sets-003.md#p-27ff632f4cd3a8e2) · [状态效果 S-cfd904e7b512cbc3](../../evidence/state_effects-sets-044.md#s-cfd904e7b512cbc3)

