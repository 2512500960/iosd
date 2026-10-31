# archive · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-009057

```text
(config-archive)# default log config <cr>
```

Handler ` RVA 0xDF0AED0 `；selector ` 0 `；EOL ` RVA 0x340A31E0 `。

模式根 ` RVA 0x34099CB0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-d894d25ec5ef1e9d](../../evidence/state_effects-sets-046.md#s-d894d25ec5ef1e9d)

### observed_connections-009049

```text
(config-archive)# default maximum <cr>
```

Handler ` RVA 0xDEC96A0 `；selector ` 1 `；EOL ` RVA 0x3409ACD8 `。

模式根 ` RVA 0x34099CB0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-047ab60b1063a911](../../evidence/conditions-sets-002.md#c-047ab60b1063a911) · [状态效果 S-d894d25ec5ef1e9d](../../evidence/state_effects-sets-046.md#s-d894d25ec5ef1e9d)

### observed_connections-009047

```text
(config-archive)# default path <cr>
```

Handler ` RVA 0xDEC96A0 `；selector ` 0 `；EOL ` RVA 0x3409A978 `。

模式根 ` RVA 0x34099CB0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-fef01ec817083b39](../../evidence/conditions-sets-098.md#c-fef01ec817083b39) · [状态效果 S-d894d25ec5ef1e9d](../../evidence/state_effects-sets-046.md#s-d894d25ec5ef1e9d)

### observed_connections-009060

```text
(config-archive)# default rollback filter adaptive <cr>
```

Handler ` RVA 0xDEC96A0 `；selector ` 5 `；EOL ` RVA 0x3409B0A8 `。

模式根 ` RVA 0x34099CB0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-d894d25ec5ef1e9d](../../evidence/state_effects-sets-046.md#s-d894d25ec5ef1e9d)

### observed_connections-009063

```text
(config-archive)# default rollback retry timeout <cr>
```

Handler ` RVA 0xDEC96A0 `；selector ` 4 `；EOL ` RVA 0x3409B410 `。

模式根 ` RVA 0x34099CB0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b644bcf8a9fdcf09](../../evidence/conditions-sets-070.md#c-b644bcf8a9fdcf09) · [状态效果 S-d894d25ec5ef1e9d](../../evidence/state_effects-sets-046.md#s-d894d25ec5ef1e9d)

### observed_connections-009055

```text
(config-archive)# default time-period <cr>
```

Handler ` RVA 0xDEC96A0 `；selector ` 3 `；EOL ` RVA 0x3409BA68 `。

模式根 ` RVA 0x34099CB0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-15780f2a068eb59d](../../evidence/conditions-sets-008.md#c-15780f2a068eb59d) · [状态效果 S-d894d25ec5ef1e9d](../../evidence/state_effects-sets-046.md#s-d894d25ec5ef1e9d)

### observed_connections-009052

```text
(config-archive)# default write-memory <cr>
```

Handler ` RVA 0xDEC96A0 `；selector ` 2 `；EOL ` RVA 0x3409B728 `。

模式根 ` RVA 0x34099CB0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-d894d25ec5ef1e9d](../../evidence/state_effects-sets-046.md#s-d894d25ec5ef1e9d)

### observed_connections-009044

```text
(config-archive)# exit <cr>
```

Handler ` RVA 0xDEE92A0 `；selector ` 0 `；EOL ` RVA 0x3409BD48 `。

模式根 ` RVA 0x34099CB0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0ca19b52fd6bc10f](../../evidence/conditions-sets-005.md#c-0ca19b52fd6bc10f)

### observed_connections-009046

```text
(config-archive)# log config <cr>
```

Handler ` RVA 0xDF0AED0 `；selector ` 0 `；EOL ` RVA 0x340A31E0 `。

模式根 ` RVA 0x34099CB0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-009050

```text
(config-archive)# maximum <number:1..14> <cr>
```

Handler ` RVA 0xDEC96A0 `；selector ` 1 `；EOL ` RVA 0x3409ACD8 `。

模式根 ` RVA 0x34099CB0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` maximum number of backup copies。

[条件 C-fcd37bdeb8d341e3](../../evidence/conditions-sets-098.md#c-fcd37bdeb8d341e3) · [参数 P-f25b9ad2a434b44b](../../evidence/parameters-sets-018.md#p-f25b9ad2a434b44b)

### observed_connections-009056

```text
(config-archive)# no log config <cr>
```

Handler ` RVA 0xDF0AED0 `；selector ` 0 `；EOL ` RVA 0x340A31E0 `。

模式根 ` RVA 0x34099CB0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-19b1df979b9b10f7](../../evidence/state_effects-sets-006.md#s-19b1df979b9b10f7)

### observed_connections-009048

```text
(config-archive)# no maximum <cr>
```

Handler ` RVA 0xDEC96A0 `；selector ` 1 `；EOL ` RVA 0x3409ACD8 `。

模式根 ` RVA 0x34099CB0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a91d48a8a28eff01](../../evidence/conditions-sets-065.md#c-a91d48a8a28eff01) · [状态效果 S-19b1df979b9b10f7](../../evidence/state_effects-sets-006.md#s-19b1df979b9b10f7)

### observed_connections-009045

```text
(config-archive)# no path <cr>
```

Handler ` RVA 0xDEC96A0 `；selector ` 0 `；EOL ` RVA 0x3409A978 `。

模式根 ` RVA 0x34099CB0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-19226e9bb9b52d26](../../evidence/conditions-sets-010.md#c-19226e9bb9b52d26) · [状态效果 S-19b1df979b9b10f7](../../evidence/state_effects-sets-006.md#s-19b1df979b9b10f7)

### observed_connections-009059

```text
(config-archive)# no rollback filter adaptive <cr>
```

Handler ` RVA 0xDEC96A0 `；selector ` 5 `；EOL ` RVA 0x3409B0A8 `。

模式根 ` RVA 0x34099CB0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-19b1df979b9b10f7](../../evidence/state_effects-sets-006.md#s-19b1df979b9b10f7)

### observed_connections-009061

```text
(config-archive)# no rollback retry timeout <cr>
```

Handler ` RVA 0xDEC96A0 `；selector ` 4 `；EOL ` RVA 0x3409B410 `。

模式根 ` RVA 0x34099CB0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1ad66554b799c0a1](../../evidence/conditions-sets-010.md#c-1ad66554b799c0a1) · [状态效果 S-19b1df979b9b10f7](../../evidence/state_effects-sets-006.md#s-19b1df979b9b10f7)

### observed_connections-009053

```text
(config-archive)# no time-period <cr>
```

Handler ` RVA 0xDEC96A0 `；selector ` 3 `；EOL ` RVA 0x3409BA68 `。

模式根 ` RVA 0x34099CB0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-111d649f0e7e50f3](../../evidence/conditions-sets-007.md#c-111d649f0e7e50f3) · [状态效果 S-19b1df979b9b10f7](../../evidence/state_effects-sets-006.md#s-19b1df979b9b10f7)

### observed_connections-009051

```text
(config-archive)# no write-memory <cr>
```

Handler ` RVA 0xDEC96A0 `；selector ` 2 `；EOL ` RVA 0x3409B728 `。

模式根 ` RVA 0x34099CB0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-19b1df979b9b10f7](../../evidence/state_effects-sets-006.md#s-19b1df979b9b10f7)

### observed_connections-009064

```text
(config-archive)# path <url:dynamic> <cr>
```

Handler ` RVA 0xDEC96A0 `；selector ` 0 `；EOL ` RVA 0x3409A978 `。

模式根 ` RVA 0x34099CB0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-59cba1b47010086b](../../evidence/conditions-sets-035.md#c-59cba1b47010086b) · [缺口 G-320020c161f57c3c](../../evidence/gaps-sets-002.md#g-320020c161f57c3c) · [参数 P-73309a345add71c7](../../evidence/parameters-sets-009.md#p-73309a345add71c7)

### observed_connections-009058

```text
(config-archive)# rollback filter adaptive <cr>
```

Handler ` RVA 0xDEC96A0 `；selector ` 5 `；EOL ` RVA 0x3409B0A8 `。

模式根 ` RVA 0x34099CB0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-009062

```text
(config-archive)# rollback retry timeout <number:0..1000> <cr>
```

Handler ` RVA 0xDEC96A0 `；selector ` 4 `；EOL ` RVA 0x3409B410 `。

模式根 ` RVA 0x34099CB0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timeout value in seconds。

[条件 C-f5330f9b1f7a4461](../../evidence/conditions-sets-095.md#c-f5330f9b1f7a4461) · [参数 P-dcbe9cface70dd81](../../evidence/parameters-sets-017.md#p-dcbe9cface70dd81)

### observed_connections-009054

```text
(config-archive)# time-period <number:1..525600> <cr>
```

Handler ` RVA 0xDEC96A0 `；selector ` 3 `；EOL ` RVA 0x3409BA68 `。

模式根 ` RVA 0x34099CB0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of minutes to wait between archive creation。

[条件 C-321d19a3991107d5](../../evidence/conditions-sets-020.md#c-321d19a3991107d5) · [参数 P-52187e3468bb9a69](../../evidence/parameters-sets-007.md#p-52187e3468bb9a69)

### observed_connections-009043

```text
(config-archive)# write-memory <cr>
```

Handler ` RVA 0xDEC96A0 `；selector ` 2 `；EOL ` RVA 0x3409B728 `。

模式根 ` RVA 0x34099CB0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。
