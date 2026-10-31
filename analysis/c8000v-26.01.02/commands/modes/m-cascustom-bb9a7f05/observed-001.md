# cascustom · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-009698

```text
(config-ctrl-cas)# auto-cut-through <cr>
```

Handler ` RVA 0x1E134D70 `；selector ` 22 `；EOL ` RVA 0x378E6190 `。

模式根 ` RVA 0x378DA128 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b4543296e5ce0fbc](../../evidence/conditions-sets-070.md#c-b4543296e5ce0fbc) · [状态效果 S-17a6b1e2cce5c502](../../evidence/state_effects-sets-005.md#s-17a6b1e2cce5c502)

### observed_connections-009702

```text
(config-ctrl-cas)# default auto-cut-through <cr>
```

Handler ` RVA 0x1E134D70 `；selector ` 22 `；EOL ` RVA 0x378E6190 `。

模式根 ` RVA 0x378DA128 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b4543296e5ce0fbc](../../evidence/conditions-sets-070.md#c-b4543296e5ce0fbc) · [状态效果 S-37c373ffa3569dfe](../../evidence/state_effects-sets-012.md#s-37c373ffa3569dfe)

### observed_connections-009701

```text
(config-ctrl-cas)# default metering <cr>
```

Handler ` RVA 0x1E138840 `；selector ` 116 `；EOL ` RVA 0x378E3CF8 `。

模式根 ` RVA 0x378DA128 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1909ca031b0d334c](../../evidence/conditions-sets-010.md#c-1909ca031b0d334c) · [状态效果 S-d840be6dc2e0ba75](../../evidence/state_effects-sets-046.md#s-d840be6dc2e0ba75)

### observed_connections-009696

```text
(config-ctrl-cas)# exit <cr>
```

Handler ` RVA 0x1615B420 `；selector ` 0 `；EOL ` RVA 0x378E3768 `。

模式根 ` RVA 0x378DA128 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-05ca7a1c49bf3416](../../evidence/conditions-sets-003.md#c-05ca7a1c49bf3416)

### observed_connections-009704

```text
(config-ctrl-cas)# invert-abcd <number:0..1> <number:0..1> <number:0..1> <number:0..1> <cr>
```

Handler ` RVA 0x1E134D70 `；selector ` 22 `；EOL ` RVA 0x378E6190 `。

模式根 ` RVA 0x378DA128 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` A bit value；` unsigned_number ` B bit value；` unsigned_number ` C bit value；` unsigned_number ` D bit value。

[条件 C-b4543296e5ce0fbc](../../evidence/conditions-sets-070.md#c-b4543296e5ce0fbc) · [缺口 G-2a192a39e52b4c69](../../evidence/gaps-sets-002.md#g-2a192a39e52b4c69) · [参数 P-c7ea8cc4b647688b](../../evidence/parameters-sets-015.md#p-c7ea8cc4b647688b) · [状态效果 S-618376cb04d0f74c](../../evidence/state_effects-sets-021.md#s-618376cb04d0f74c)

### observed_connections-009697

```text
(config-ctrl-cas)# metering <cr>
```

Handler ` RVA 0x1E138840 `；selector ` 116 `；EOL ` RVA 0x378E3CF8 `。

模式根 ` RVA 0x378DA128 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1909ca031b0d334c](../../evidence/conditions-sets-010.md#c-1909ca031b0d334c) · [状态效果 S-314d9a25c5c7df97](../../evidence/state_effects-sets-011.md#s-314d9a25c5c7df97)

### observed_connections-009700

```text
(config-ctrl-cas)# no auto-cut-through <cr>
```

Handler ` RVA 0x1E134D70 `；selector ` 22 `；EOL ` RVA 0x378E6190 `。

模式根 ` RVA 0x378DA128 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b4543296e5ce0fbc](../../evidence/conditions-sets-070.md#c-b4543296e5ce0fbc) · [状态效果 S-a35b47974279dc68](../../evidence/state_effects-sets-035.md#s-a35b47974279dc68)

### observed_connections-009699

```text
(config-ctrl-cas)# no metering <cr>
```

Handler ` RVA 0x1E138840 `；selector ` 116 `；EOL ` RVA 0x378E3CF8 `。

模式根 ` RVA 0x378DA128 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1909ca031b0d334c](../../evidence/conditions-sets-010.md#c-1909ca031b0d334c) · [状态效果 S-c0b1ac4321031769](../../evidence/state_effects-sets-041.md#s-c0b1ac4321031769)

### observed_connections-009703

```text
(config-ctrl-cas)# unused-abcd <number:0..1> <number:0..1> <number:0..1> <number:0..1> <cr>
```

Handler ` RVA 0x1E138840 `；selector ` 116 `；EOL ` RVA 0x378E3CF8 `。

模式根 ` RVA 0x378DA128 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` A bit value；` unsigned_number ` B bit value；` unsigned_number ` C bit value；` unsigned_number ` D bit value。

[条件 C-62266caeb948f889](../../evidence/conditions-sets-038.md#c-62266caeb948f889) · [缺口 G-d0a3f6bf8ef4046e](../../evidence/gaps-sets-007.md#g-d0a3f6bf8ef4046e) · [参数 P-7afd08846ff062a5](../../evidence/parameters-sets-010.md#p-7afd08846ff062a5) · [状态效果 S-f771939ebed9d2d5](../../evidence/state_effects-sets-052.md#s-f771939ebed9d2d5)
