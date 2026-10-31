# bdomain-efp-mode · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-009717

```text
(config-bdomain-efp)# default remote circuit id <cr>
```

Handler ` RVA 0xBF84130 `；selector ` 1 `；EOL ` RVA 0x3395BB10 `。

模式根 ` RVA 0x33959F88 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ac98f53878885b42](../../evidence/conditions-sets-067.md#c-ac98f53878885b42) · [状态效果 S-560fb5be0cb4cc94](../../evidence/state_effects-sets-019.md#s-560fb5be0cb4cc94)

### observed_connections-009715

```text
(config-bdomain-efp)# exit <cr>
```

Handler ` RVA 0xBF84650 `；selector ` 0 `；EOL ` RVA 0x3395C708 `。

模式根 ` RVA 0x33959F88 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b02797abace2e64e](../../evidence/conditions-sets-068.md#c-b02797abace2e64e)

### observed_connections-009716

```text
(config-bdomain-efp)# no remote circuit id <cr>
```

Handler ` RVA 0xBF84130 `；selector ` 1 `；EOL ` RVA 0x3395BB10 `。

模式根 ` RVA 0x33959F88 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4441b3908c173c33](../../evidence/conditions-sets-027.md#c-4441b3908c173c33) · [状态效果 S-8ce37fa3d6c7ac64](../../evidence/state_effects-sets-030.md#s-8ce37fa3d6c7ac64)

### observed_connections-009718

```text
(config-bdomain-efp)# remote circuit id <number:dynamic> <cr>
```

Handler ` RVA 0xBF84130 `；selector ` 1 `；EOL ` RVA 0x3395BB10 `。

模式根 ` RVA 0x33959F88 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Remote circuit ID。

[条件 C-45fd9cc46c90dca1](../../evidence/conditions-sets-027.md#c-45fd9cc46c90dca1) · [缺口 G-7fd4d45756b556d9](../../evidence/gaps-sets-005.md#g-7fd4d45756b556d9) · [参数 P-c07f2b539051de22](../../evidence/parameters-sets-015.md#p-c07f2b539051de22) · [状态效果 S-18f004676e434f0d](../../evidence/state_effects-sets-006.md#s-18f004676e434f0d)
