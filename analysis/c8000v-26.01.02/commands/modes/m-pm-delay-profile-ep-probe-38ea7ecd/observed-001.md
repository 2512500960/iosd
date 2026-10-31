# pm-delay-profile-ep-probe · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-008933

```text
(config-pm-dm-ep-probe)# burst-interval <number:30..15000> <cr>
```

Handler ` RVA 0x1ACFC440 `；selector ` 0 `；EOL ` RVA 0x36DC98D0 `。

模式根 ` RVA 0x36DC1B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Burst interval (msec)。

[参数 P-f4437d88dc812964](../../evidence/parameters-sets-018.md#p-f4437d88dc812964)

### observed_connections-008935

```text
(config-pm-dm-ep-probe)# computation-interval <number:3..3600> <cr>
```

Handler ` RVA 0x1ACFC0E0 `；selector ` 0 `；EOL ` RVA 0x36DC9C00 `。

模式根 ` RVA 0x36DC1B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Computation interval (seconds)。

[条件 C-a62e985afdf91068](../../evidence/conditions-sets-064.md#c-a62e985afdf91068) · [参数 P-d09a80bed29e4458](../../evidence/parameters-sets-016.md#p-d09a80bed29e4458)

### observed_connections-008932

```text
(config-pm-dm-ep-probe)# default <cr>
```

Handler ` RVA 0x1ACFB040 `；selector ` 0 `；EOL ` RVA 0x36DCAD20 `。

模式根 ` RVA 0x36DC1B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-ebe9312018802a56](../../evidence/state_effects-sets-050.md#s-ebe9312018802a56)

### observed_connections-008941

```text
(config-pm-dm-ep-probe)# default burst-interval <number:30..15000> <cr>
```

Handler ` RVA 0x1ACFC440 `；selector ` 0 `；EOL ` RVA 0x36DC98D0 `。

模式根 ` RVA 0x36DC1B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Burst interval (msec)。

[参数 P-f4437d88dc812964](../../evidence/parameters-sets-018.md#p-f4437d88dc812964) · [状态效果 S-ebe9312018802a56](../../evidence/state_effects-sets-050.md#s-ebe9312018802a56)

### observed_connections-008946

```text
(config-pm-dm-ep-probe)# default computation-interval <number:3..3600> <cr>
```

Handler ` RVA 0x1ACFC0E0 `；selector ` 0 `；EOL ` RVA 0x36DC9C00 `。

模式根 ` RVA 0x36DC1B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Computation interval (seconds)。

[条件 C-a62e985afdf91068](../../evidence/conditions-sets-064.md#c-a62e985afdf91068) · [参数 P-d09a80bed29e4458](../../evidence/parameters-sets-016.md#p-d09a80bed29e4458) · [状态效果 S-ebe9312018802a56](../../evidence/state_effects-sets-050.md#s-ebe9312018802a56)

### observed_connections-008953

```text
(config-pm-dm-ep-probe)# default measurement-mode loopback <cr>
```

Handler ` RVA 0x1ACFC2A0 `；selector ` 0 `；EOL ` RVA 0x36DCAA40 `。

模式根 ` RVA 0x36DC1B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-ebe9312018802a56](../../evidence/state_effects-sets-050.md#s-ebe9312018802a56)

### observed_connections-008949

```text
(config-pm-dm-ep-probe)# default measurement-mode one-way <cr>
```

Handler ` RVA 0x1ACFC370 `；selector ` 0 `；EOL ` RVA 0x36DCA4F0 `。

模式根 ` RVA 0x36DC1B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-ebe9312018802a56](../../evidence/state_effects-sets-050.md#s-ebe9312018802a56)

### observed_connections-008951

```text
(config-pm-dm-ep-probe)# default measurement-mode two-way <cr>
```

Handler ` RVA 0x1ACFCDE0 `；selector ` 0 `；EOL ` RVA 0x36DCA798 `。

模式根 ` RVA 0x36DC1B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-ebe9312018802a56](../../evidence/state_effects-sets-050.md#s-ebe9312018802a56)

### observed_connections-008944

```text
(config-pm-dm-ep-probe)# default padding-size <number:0..8000> <cr>
```

Handler ` RVA 0x1ACFBEC0 `；selector ` 0 `；EOL ` RVA 0x36DC9F38 `。

模式根 ` RVA 0x36DC1B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Padding (bytes) to add to probes。

[参数 P-0f90b03d9cc18eae](../../evidence/parameters-sets-002.md#p-0f90b03d9cc18eae) · [状态效果 S-ebe9312018802a56](../../evidence/state_effects-sets-050.md#s-ebe9312018802a56)

### observed_connections-008947

```text
(config-pm-dm-ep-probe)# default tos-dscp <number:0..63> <cr>
```

Handler ` RVA 0x1ACFBFE0 `；selector ` 0 `；EOL ` RVA 0x36DCA228 `。

模式根 ` RVA 0x36DC1B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` TOS DSCP。

[参数 P-1395f8a7ed87e3f7](../../evidence/parameters-sets-002.md#p-1395f8a7ed87e3f7) · [状态效果 S-ebe9312018802a56](../../evidence/state_effects-sets-050.md#s-ebe9312018802a56)

### observed_connections-008930

```text
(config-pm-dm-ep-probe)# exit <cr>
```

Handler ` RVA 0x1ACFC700 `；selector ` 0 `；EOL ` RVA 0x36DDE638 `。

模式根 ` RVA 0x36DC1B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7e17f7f73e318649](../../evidence/conditions-sets-049.md#c-7e17f7f73e318649)

### observed_connections-008939

```text
(config-pm-dm-ep-probe)# measurement-mode loopback <cr>
```

Handler ` RVA 0x1ACFC2A0 `；selector ` 0 `；EOL ` RVA 0x36DCAA40 `。

模式根 ` RVA 0x36DC1B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-008937

```text
(config-pm-dm-ep-probe)# measurement-mode one-way <cr>
```

Handler ` RVA 0x1ACFC370 `；selector ` 0 `；EOL ` RVA 0x36DCA4F0 `。

模式根 ` RVA 0x36DC1B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-008938

```text
(config-pm-dm-ep-probe)# measurement-mode two-way <cr>
```

Handler ` RVA 0x1ACFCDE0 `；selector ` 0 `；EOL ` RVA 0x36DCA798 `。

模式根 ` RVA 0x36DC1B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-008931

```text
(config-pm-dm-ep-probe)# no <cr>
```

Handler ` RVA 0x1ACFB040 `；selector ` 0 `；EOL ` RVA 0x36DCAD20 `。

模式根 ` RVA 0x36DC1B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-89f0c8402d686e8b](../../evidence/state_effects-sets-029.md#s-89f0c8402d686e8b)

### observed_connections-008940

```text
(config-pm-dm-ep-probe)# no burst-interval <number:30..15000> <cr>
```

Handler ` RVA 0x1ACFC440 `；selector ` 0 `；EOL ` RVA 0x36DC98D0 `。

模式根 ` RVA 0x36DC1B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Burst interval (msec)。

[参数 P-f4437d88dc812964](../../evidence/parameters-sets-018.md#p-f4437d88dc812964) · [状态效果 S-89f0c8402d686e8b](../../evidence/state_effects-sets-029.md#s-89f0c8402d686e8b)

### observed_connections-008943

```text
(config-pm-dm-ep-probe)# no computation-interval <number:3..3600> <cr>
```

Handler ` RVA 0x1ACFC0E0 `；selector ` 0 `；EOL ` RVA 0x36DC9C00 `。

模式根 ` RVA 0x36DC1B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Computation interval (seconds)。

[条件 C-a62e985afdf91068](../../evidence/conditions-sets-064.md#c-a62e985afdf91068) · [参数 P-d09a80bed29e4458](../../evidence/parameters-sets-016.md#p-d09a80bed29e4458) · [状态效果 S-89f0c8402d686e8b](../../evidence/state_effects-sets-029.md#s-89f0c8402d686e8b)

### observed_connections-008952

```text
(config-pm-dm-ep-probe)# no measurement-mode loopback <cr>
```

Handler ` RVA 0x1ACFC2A0 `；selector ` 0 `；EOL ` RVA 0x36DCAA40 `。

模式根 ` RVA 0x36DC1B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-89f0c8402d686e8b](../../evidence/state_effects-sets-029.md#s-89f0c8402d686e8b)

### observed_connections-008948

```text
(config-pm-dm-ep-probe)# no measurement-mode one-way <cr>
```

Handler ` RVA 0x1ACFC370 `；selector ` 0 `；EOL ` RVA 0x36DCA4F0 `。

模式根 ` RVA 0x36DC1B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-89f0c8402d686e8b](../../evidence/state_effects-sets-029.md#s-89f0c8402d686e8b)

### observed_connections-008950

```text
(config-pm-dm-ep-probe)# no measurement-mode two-way <cr>
```

Handler ` RVA 0x1ACFCDE0 `；selector ` 0 `；EOL ` RVA 0x36DCA798 `。

模式根 ` RVA 0x36DC1B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-89f0c8402d686e8b](../../evidence/state_effects-sets-029.md#s-89f0c8402d686e8b)

### observed_connections-008942

```text
(config-pm-dm-ep-probe)# no padding-size <number:0..8000> <cr>
```

Handler ` RVA 0x1ACFBEC0 `；selector ` 0 `；EOL ` RVA 0x36DC9F38 `。

模式根 ` RVA 0x36DC1B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Padding (bytes) to add to probes。

[参数 P-0f90b03d9cc18eae](../../evidence/parameters-sets-002.md#p-0f90b03d9cc18eae) · [状态效果 S-89f0c8402d686e8b](../../evidence/state_effects-sets-029.md#s-89f0c8402d686e8b)

### observed_connections-008945

```text
(config-pm-dm-ep-probe)# no tos-dscp <number:0..63> <cr>
```

Handler ` RVA 0x1ACFBFE0 `；selector ` 0 `；EOL ` RVA 0x36DCA228 `。

模式根 ` RVA 0x36DC1B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` TOS DSCP。

[参数 P-1395f8a7ed87e3f7](../../evidence/parameters-sets-002.md#p-1395f8a7ed87e3f7) · [状态效果 S-89f0c8402d686e8b](../../evidence/state_effects-sets-029.md#s-89f0c8402d686e8b)

### observed_connections-008934

```text
(config-pm-dm-ep-probe)# padding-size <number:0..8000> <cr>
```

Handler ` RVA 0x1ACFBEC0 `；selector ` 0 `；EOL ` RVA 0x36DC9F38 `。

模式根 ` RVA 0x36DC1B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Padding (bytes) to add to probes。

[参数 P-0f90b03d9cc18eae](../../evidence/parameters-sets-002.md#p-0f90b03d9cc18eae)

### observed_connections-008936

```text
(config-pm-dm-ep-probe)# tos-dscp <number:0..63> <cr>
```

Handler ` RVA 0x1ACFBFE0 `；selector ` 0 `；EOL ` RVA 0x36DCA228 `。

模式根 ` RVA 0x36DC1B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` TOS DSCP。

[参数 P-1395f8a7ed87e3f7](../../evidence/parameters-sets-002.md#p-1395f8a7ed87e3f7)

### observed_connections-008929

```text
(config-pm-dm-ep-probe)# <cr>
```

Handler ` RVA 0x1ACFB040 `；selector ` 0 `；EOL ` RVA 0x36DCAD20 `。

模式根 ` RVA 0x36DC1B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

