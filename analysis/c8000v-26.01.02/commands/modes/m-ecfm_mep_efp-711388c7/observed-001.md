# ecfm_mep_efp · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-008797

```text
(config-if-srv-ecfm-mep)# alarm delay <number:2500..10000> <cr>
```

Handler ` RVA 0xBDD0030 `；selector ` 0 `；EOL ` RVA 0x33909A78 `。

模式根 ` RVA 0x33908B10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` msec (default: 2500 msec)。

[条件 C-433939a0391d4ca1](../../evidence/conditions-sets-026.md#c-433939a0391d4ca1) · [参数 P-6df9163f9390433b](../../evidence/parameters-sets-009.md#p-6df9163f9390433b)

### observed_connections-008800

```text
(config-if-srv-ecfm-mep)# alarm notification all <cr>
```

Handler ` RVA 0xBDCFF00 `；selector ` 0 `；EOL ` RVA 0x33909D68 `。

模式根 ` RVA 0x33908B10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8307efddd6583855](../../evidence/conditions-sets-051.md#c-8307efddd6583855) · [状态效果 S-f2e484fcd1769fa1](../../evidence/state_effects-sets-051.md#s-f2e484fcd1769fa1)

### observed_connections-008794

```text
(config-if-srv-ecfm-mep)# alarm reset <number:2500..10000> <cr>
```

Handler ` RVA 0xBDD0180 `；selector ` 0 `；EOL ` RVA 0x33909760 `。

模式根 ` RVA 0x33908B10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` msec (default: 10000 msec)。

[条件 C-67e1d0ea762af26e](../../evidence/conditions-sets-040.md#c-67e1d0ea762af26e) · [参数 P-d7be68c3f452048a](../../evidence/parameters-sets-016.md#p-d7be68c3f452048a)

### observed_connections-008791

```text
(config-if-srv-ecfm-mep)# continuity-check static rmep <cr>
```

Handler ` RVA 0xBDCFA90 `；selector ` 0 `；EOL ` RVA 0x33909050 `。

模式根 ` RVA 0x33908B10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e9dfb055df419c8a](../../evidence/conditions-sets-090.md#c-e9dfb055df419c8a)

### observed_connections-008789

```text
(config-if-srv-ecfm-mep)# cos <number:0..7> <cr>
```

Handler ` RVA 0xBDCF8B0 `；selector ` 0 `；EOL ` RVA 0x33908CE0 `。

模式根 ` RVA 0x33908B10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` CoS value。

[条件 C-438508c12fbe4ce1](../../evidence/conditions-sets-026.md#c-438508c12fbe4ce1) · [参数 P-a4ebedc5530206ba](../../evidence/parameters-sets-013.md#p-a4ebedc5530206ba)

### observed_connections-008798

```text
(config-if-srv-ecfm-mep)# default alarm delay <cr>
```

Handler ` RVA 0xBDD0030 `；selector ` 0 `；EOL ` RVA 0x33909A78 `。

模式根 ` RVA 0x33908B10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3cb3b73e44e7fd1f](../../evidence/conditions-sets-024.md#c-3cb3b73e44e7fd1f) · [状态效果 S-920e91d98ca95512](../../evidence/state_effects-sets-031.md#s-920e91d98ca95512)

### observed_connections-008802

```text
(config-if-srv-ecfm-mep)# default alarm notification <cr>
```

Handler ` RVA 0xBDCFF00 `；selector ` 0 `；EOL ` RVA 0x33909D68 `。

模式根 ` RVA 0x33908B10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7638992a664e29ba](../../evidence/conditions-sets-046.md#c-7638992a664e29ba) · [状态效果 S-920e91d98ca95512](../../evidence/state_effects-sets-031.md#s-920e91d98ca95512)

### observed_connections-008795

```text
(config-if-srv-ecfm-mep)# default alarm reset <cr>
```

Handler ` RVA 0xBDD0180 `；selector ` 0 `；EOL ` RVA 0x33909760 `。

模式根 ` RVA 0x33908B10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-15afb006f396d275](../../evidence/conditions-sets-009.md#c-15afb006f396d275) · [状态效果 S-920e91d98ca95512](../../evidence/state_effects-sets-031.md#s-920e91d98ca95512)

### observed_connections-008804

```text
(config-if-srv-ecfm-mep)# default continuity-check static rmep <cr>
```

Handler ` RVA 0xBDCFA90 `；selector ` 0 `；EOL ` RVA 0x33909050 `。

模式根 ` RVA 0x33908B10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e9dfb055df419c8a](../../evidence/conditions-sets-090.md#c-e9dfb055df419c8a) · [状态效果 S-920e91d98ca95512](../../evidence/state_effects-sets-031.md#s-920e91d98ca95512)

### observed_connections-008790

```text
(config-if-srv-ecfm-mep)# default cos <cr>
```

Handler ` RVA 0xBDCF8B0 `；selector ` 0 `；EOL ` RVA 0x33908CE0 `。

模式根 ` RVA 0x33908B10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9614c29e2d2ca4e5](../../evidence/conditions-sets-058.md#c-9614c29e2d2ca4e5) · [状态效果 S-920e91d98ca95512](../../evidence/state_effects-sets-031.md#s-920e91d98ca95512)

### observed_connections-008811

```text
(config-if-srv-ecfm-mep)# default dmm responder hardware timestamp <cr>
```

Handler ` RVA 0xBDD0660 `；selector ` 0 `；EOL ` RVA 0x3390A718 `。

模式根 ` RVA 0x33908B10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-24f89ab8d149092f](../../evidence/conditions-sets-014.md#c-24f89ab8d149092f) · [状态效果 S-920e91d98ca95512](../../evidence/state_effects-sets-031.md#s-920e91d98ca95512)

### observed_connections-008809

```text
(config-if-srv-ecfm-mep)# default monitor loss counter <cr>
```

Handler ` RVA 0xBDD02D0 `；selector ` 0 `；EOL ` RVA 0x3390A348 `。

模式根 ` RVA 0x33908B10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f8aea23f0bc1493f](../../evidence/conditions-sets-096.md#c-f8aea23f0bc1493f) · [状态效果 S-920e91d98ca95512](../../evidence/state_effects-sets-031.md#s-920e91d98ca95512)

### observed_connections-008806

```text
(config-if-srv-ecfm-mep)# default rmep mpid <number:1..8191> <cr>
```

Handler ` RVA 0xBDCFC00 `；selector ` 0 `；EOL ` RVA 0x339093D0 `。

模式根 ` RVA 0x33908B10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Identifier value。

[条件 C-561f764b8c97b009](../../evidence/conditions-sets-034.md#c-561f764b8c97b009) · [参数 P-f3acb620b94c6777](../../evidence/parameters-sets-018.md#p-f3acb620b94c6777) · [状态效果 S-920e91d98ca95512](../../evidence/state_effects-sets-031.md#s-920e91d98ca95512)

### observed_connections-008808

```text
(config-if-srv-ecfm-mep)# dmm responder hardware timestamp <cr>
```

Handler ` RVA 0xBDD0660 `；selector ` 0 `；EOL ` RVA 0x3390A718 `。

模式根 ` RVA 0x33908B10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-24f89ab8d149092f](../../evidence/conditions-sets-014.md#c-24f89ab8d149092f)

### observed_connections-008787

```text
(config-if-srv-ecfm-mep)# exit <cr>
```

Handler ` RVA 0xBDBECC0 `；selector ` 0 `；EOL ` RVA 0x3390C598 `。

模式根 ` RVA 0x33908B10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1d5d165fdc41219f](../../evidence/conditions-sets-011.md#c-1d5d165fdc41219f)

### observed_connections-008801

```text
(config-if-srv-ecfm-mep)# monitor loss counter <cr>
```

Handler ` RVA 0xBDD02D0 `；selector ` 0 `；EOL ` RVA 0x3390A348 `。

模式根 ` RVA 0x33908B10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f8aea23f0bc1493f](../../evidence/conditions-sets-096.md#c-f8aea23f0bc1493f)

### observed_connections-008796

```text
(config-if-srv-ecfm-mep)# no alarm delay <cr>
```

Handler ` RVA 0xBDD0030 `；selector ` 0 `；EOL ` RVA 0x33909A78 `。

模式根 ` RVA 0x33908B10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0fc6db6afb597560](../../evidence/conditions-sets-006.md#c-0fc6db6afb597560) · [状态效果 S-0f73dde6ad5bfda1](../../evidence/state_effects-sets-004.md#s-0f73dde6ad5bfda1)

### observed_connections-008799

```text
(config-if-srv-ecfm-mep)# no alarm notification <cr>
```

Handler ` RVA 0xBDCFF00 `；selector ` 0 `；EOL ` RVA 0x33909D68 `。

模式根 ` RVA 0x33908B10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-eebd6c3ec98efb9b](../../evidence/conditions-sets-092.md#c-eebd6c3ec98efb9b) · [状态效果 S-0f73dde6ad5bfda1](../../evidence/state_effects-sets-004.md#s-0f73dde6ad5bfda1)

### observed_connections-008793

```text
(config-if-srv-ecfm-mep)# no alarm reset <cr>
```

Handler ` RVA 0xBDD0180 `；selector ` 0 `；EOL ` RVA 0x33909760 `。

模式根 ` RVA 0x33908B10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-9bf011922026231a](../../evidence/conditions-sets-060.md#c-9bf011922026231a) · [状态效果 S-0f73dde6ad5bfda1](../../evidence/state_effects-sets-004.md#s-0f73dde6ad5bfda1)

### observed_connections-008803

```text
(config-if-srv-ecfm-mep)# no continuity-check static rmep <cr>
```

Handler ` RVA 0xBDCFA90 `；selector ` 0 `；EOL ` RVA 0x33909050 `。

模式根 ` RVA 0x33908B10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e9dfb055df419c8a](../../evidence/conditions-sets-090.md#c-e9dfb055df419c8a) · [状态效果 S-0f73dde6ad5bfda1](../../evidence/state_effects-sets-004.md#s-0f73dde6ad5bfda1)

### observed_connections-008788

```text
(config-if-srv-ecfm-mep)# no cos <cr>
```

Handler ` RVA 0xBDCF8B0 `；selector ` 0 `；EOL ` RVA 0x33908CE0 `。

模式根 ` RVA 0x33908B10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d41fe9b0ec56bb75](../../evidence/conditions-sets-082.md#c-d41fe9b0ec56bb75) · [状态效果 S-0f73dde6ad5bfda1](../../evidence/state_effects-sets-004.md#s-0f73dde6ad5bfda1)

### observed_connections-008810

```text
(config-if-srv-ecfm-mep)# no dmm responder hardware timestamp <cr>
```

Handler ` RVA 0xBDD0660 `；selector ` 0 `；EOL ` RVA 0x3390A718 `。

模式根 ` RVA 0x33908B10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-24f89ab8d149092f](../../evidence/conditions-sets-014.md#c-24f89ab8d149092f) · [状态效果 S-0f73dde6ad5bfda1](../../evidence/state_effects-sets-004.md#s-0f73dde6ad5bfda1)

### observed_connections-008807

```text
(config-if-srv-ecfm-mep)# no monitor loss counter <cr>
```

Handler ` RVA 0xBDD02D0 `；selector ` 0 `；EOL ` RVA 0x3390A348 `。

模式根 ` RVA 0x33908B10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f8aea23f0bc1493f](../../evidence/conditions-sets-096.md#c-f8aea23f0bc1493f) · [状态效果 S-0f73dde6ad5bfda1](../../evidence/state_effects-sets-004.md#s-0f73dde6ad5bfda1)

### observed_connections-008805

```text
(config-if-srv-ecfm-mep)# no rmep mpid <number:1..8191> <cr>
```

Handler ` RVA 0xBDCFC00 `；selector ` 0 `；EOL ` RVA 0x339093D0 `。

模式根 ` RVA 0x33908B10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Identifier value。

[条件 C-561f764b8c97b009](../../evidence/conditions-sets-034.md#c-561f764b8c97b009) · [参数 P-f3acb620b94c6777](../../evidence/parameters-sets-018.md#p-f3acb620b94c6777) · [状态效果 S-0f73dde6ad5bfda1](../../evidence/state_effects-sets-004.md#s-0f73dde6ad5bfda1)

### observed_connections-008792

```text
(config-if-srv-ecfm-mep)# rmep mpid <number:1..8191> <cr>
```

Handler ` RVA 0xBDCFC00 `；selector ` 0 `；EOL ` RVA 0x339093D0 `。

模式根 ` RVA 0x33908B10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Identifier value。

[条件 C-561f764b8c97b009](../../evidence/conditions-sets-034.md#c-561f764b8c97b009) · [参数 P-f3acb620b94c6777](../../evidence/parameters-sets-018.md#p-f3acb620b94c6777)

