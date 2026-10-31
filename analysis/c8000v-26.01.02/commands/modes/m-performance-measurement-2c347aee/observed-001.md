# performance-measurement · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-003694

```text
(config-perf-meas)# default <cr>
```

Handler ` RVA 0x1ACEEE70 `；selector ` 0 `；EOL ` RVA 0x36DD8220 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-16edb078860859dd](../../evidence/conditions-sets-009.md#c-16edb078860859dd) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003711

```text
(config-perf-meas)# default delay-profile endpoint <cr>
```

Handler ` RVA 0x1ACF9DE0 `；selector ` 0 `；EOL ` RVA 0x36DCB5B0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c1637be6fab92cfb](../../evidence/conditions-sets-075.md#c-c1637be6fab92cfb) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003739

```text
(config-perf-meas)# default delay-profile endpoint advertisement <cr>
```

Handler ` RVA 0x1ACFAE10 `；selector ` 0 `；EOL ` RVA 0x36DC94E8 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c1637be6fab92cfb](../../evidence/conditions-sets-075.md#c-c1637be6fab92cfb) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003813

```text
(config-perf-meas)# default delay-profile endpoint advertisement accelerated <cr>
```

Handler ` RVA 0x1ACFB3D0 `；selector ` 0 `；EOL ` RVA 0x36DC83D8 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c1637be6fab92cfb](../../evidence/conditions-sets-075.md#c-c1637be6fab92cfb) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003957

```text
(config-perf-meas)# default delay-profile endpoint advertisement accelerated minimum-change <number:0..1000000> <cr>
```

Handler ` RVA 0x1ACFB890 `；selector ` 0 `；EOL ` RVA 0x36DC7E28 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Accelerated advertisement minimum change (uSec)。

[条件 C-c1637be6fab92cfb](../../evidence/conditions-sets-075.md#c-c1637be6fab92cfb) · [参数 P-9f6f6ba2d130deb9](../../evidence/parameters-sets-012.md#p-9f6f6ba2d130deb9) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003971

```text
(config-perf-meas)# default delay-profile endpoint advertisement accelerated threshold <number:0..100> <cr>
```

Handler ` RVA 0x1ACFB760 `；selector ` 0 `；EOL ` RVA 0x36DC8140 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Accelerated advertisement threshold percentage change。

[条件 C-c1637be6fab92cfb](../../evidence/conditions-sets-075.md#c-c1637be6fab92cfb) · [参数 P-2bf284102dc3b5f7](../../evidence/parameters-sets-004.md#p-2bf284102dc3b5f7) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003819

```text
(config-perf-meas)# default delay-profile endpoint advertisement periodic <cr>
```

Handler ` RVA 0x1ACFB520 `；selector ` 0 `；EOL ` RVA 0x36DC9258 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c1637be6fab92cfb](../../evidence/conditions-sets-075.md#c-c1637be6fab92cfb) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003926

```text
(config-perf-meas)# default delay-profile endpoint advertisement periodic disabled <cr>
```

Handler ` RVA 0x1ACFB9C0 `；selector ` 0 `；EOL ` RVA 0x36DC8FB0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c1637be6fab92cfb](../../evidence/conditions-sets-075.md#c-c1637be6fab92cfb) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003984

```text
(config-perf-meas)# default delay-profile endpoint advertisement periodic interval <number:30..3600> <cr>
```

Handler ` RVA 0x1ACFBA60 `；selector ` 0 `；EOL ` RVA 0x36DC8D28 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number `  Periodic advertisement interval (seconds)。

[条件 C-c1637be6fab92cfb](../../evidence/conditions-sets-075.md#c-c1637be6fab92cfb) · [参数 P-9239b3dae0fed22a](../../evidence/parameters-sets-011.md#p-9239b3dae0fed22a) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003962

```text
(config-perf-meas)# default delay-profile endpoint advertisement periodic minimum-change <number:0..1000000> <cr>
```

Handler ` RVA 0x1ACFBD00 `；selector ` 0 `；EOL ` RVA 0x36DC86F8 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Periodic advertisement minimum change (uSec)。

[条件 C-c1637be6fab92cfb](../../evidence/conditions-sets-075.md#c-c1637be6fab92cfb) · [参数 P-ca7c92d34181e004](../../evidence/parameters-sets-015.md#p-ca7c92d34181e004) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003978

```text
(config-perf-meas)# default delay-profile endpoint advertisement periodic threshold <number:0..100> <cr>
```

Handler ` RVA 0x1ACFBB50 `；selector ` 0 `；EOL ` RVA 0x36DC8A38 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Periodic advertisement threshold percentage change。

[条件 C-c1637be6fab92cfb](../../evidence/conditions-sets-075.md#c-c1637be6fab92cfb) · [参数 P-0f8747ef381467d2](../../evidence/parameters-sets-002.md#p-0f8747ef381467d2) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003804

```text
(config-perf-meas)# default delay-profile endpoint advertisement threshold-check <cr>
```

Handler ` RVA 0x1ACFB6B0 `；selector ` 0 `；EOL ` RVA 0x36DC7A78 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c1637be6fab92cfb](../../evidence/conditions-sets-075.md#c-c1637be6fab92cfb) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003859

```text
(config-perf-meas)# default delay-profile endpoint advertisement threshold-check average-delay <cr>
```

Handler ` RVA 0x1ACFCC80 `；selector ` 0 `；EOL ` RVA 0x36DC7280 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c1637be6fab92cfb](../../evidence/conditions-sets-075.md#c-c1637be6fab92cfb) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003865

```text
(config-perf-meas)# default delay-profile endpoint advertisement threshold-check maximum-delay <cr>
```

Handler ` RVA 0x1ACFCB30 `；selector ` 0 `；EOL ` RVA 0x36DC7528 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c1637be6fab92cfb](../../evidence/conditions-sets-075.md#c-c1637be6fab92cfb) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003874

```text
(config-perf-meas)# default delay-profile endpoint advertisement threshold-check minimum-delay <cr>
```

Handler ` RVA 0x1ACFC9E0 `；selector ` 0 `；EOL ` RVA 0x36DC77D0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c1637be6fab92cfb](../../evidence/conditions-sets-075.md#c-c1637be6fab92cfb) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003762

```text
(config-perf-meas)# default delay-profile endpoint liveness-detection <cr>
```

Handler ` RVA 0x1ACFB2C0 `；selector ` 0 `；EOL ` RVA 0x36DCB330 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-97664056404981c7](../../evidence/conditions-sets-058.md#c-97664056404981c7) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003899

```text
(config-perf-meas)# default delay-profile endpoint liveness-detection multiplier <number:2..10> <cr>
```

Handler ` RVA 0x1ACFCEA0 `；selector ` 0 `；EOL ` RVA 0x36DCB098 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Detect Multiplier。

[条件 C-97664056404981c7](../../evidence/conditions-sets-058.md#c-97664056404981c7) · [参数 P-832a3c41773baa51](../../evidence/parameters-sets-010.md#p-832a3c41773baa51) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003745

```text
(config-perf-meas)# default delay-profile endpoint probe <cr>
```

Handler ` RVA 0x1ACFB040 `；selector ` 0 `；EOL ` RVA 0x36DCAD20 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c1637be6fab92cfb](../../evidence/conditions-sets-075.md#c-c1637be6fab92cfb) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003878

```text
(config-perf-meas)# default delay-profile endpoint probe burst-interval <number:30..15000> <cr>
```

Handler ` RVA 0x1ACFC440 `；selector ` 0 `；EOL ` RVA 0x36DC98D0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Burst interval (msec)。

[条件 C-c1637be6fab92cfb](../../evidence/conditions-sets-075.md#c-c1637be6fab92cfb) · [参数 P-f4437d88dc812964](../../evidence/parameters-sets-018.md#p-f4437d88dc812964) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003903

```text
(config-perf-meas)# default delay-profile endpoint probe computation-interval <number:3..3600> <cr>
```

Handler ` RVA 0x1ACFC0E0 `；selector ` 0 `；EOL ` RVA 0x36DC9C00 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Computation interval (seconds)。

[条件 C-0b907c9f8f450fdb](../../evidence/conditions-sets-005.md#c-0b907c9f8f450fdb) · [参数 P-d09a80bed29e4458](../../evidence/parameters-sets-016.md#p-d09a80bed29e4458) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003941

```text
(config-perf-meas)# default delay-profile endpoint probe measurement-mode loopback <cr>
```

Handler ` RVA 0x1ACFC2A0 `；selector ` 0 `；EOL ` RVA 0x36DCAA40 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c1637be6fab92cfb](../../evidence/conditions-sets-075.md#c-c1637be6fab92cfb) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003919

```text
(config-perf-meas)# default delay-profile endpoint probe measurement-mode one-way <cr>
```

Handler ` RVA 0x1ACFC370 `；selector ` 0 `；EOL ` RVA 0x36DCA4F0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c1637be6fab92cfb](../../evidence/conditions-sets-075.md#c-c1637be6fab92cfb) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003933

```text
(config-perf-meas)# default delay-profile endpoint probe measurement-mode two-way <cr>
```

Handler ` RVA 0x1ACFCDE0 `；selector ` 0 `；EOL ` RVA 0x36DCA798 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c1637be6fab92cfb](../../evidence/conditions-sets-075.md#c-c1637be6fab92cfb) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003901

```text
(config-perf-meas)# default delay-profile endpoint probe padding-size <number:0..8000> <cr>
```

Handler ` RVA 0x1ACFBEC0 `；selector ` 0 `；EOL ` RVA 0x36DC9F38 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Padding (bytes) to add to probes。

[条件 C-c1637be6fab92cfb](../../evidence/conditions-sets-075.md#c-c1637be6fab92cfb) · [参数 P-0f90b03d9cc18eae](../../evidence/parameters-sets-002.md#p-0f90b03d9cc18eae) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003909

```text
(config-perf-meas)# default delay-profile endpoint probe tos-dscp <number:0..63> <cr>
```

Handler ` RVA 0x1ACFBFE0 `；selector ` 0 `；EOL ` RVA 0x36DCA228 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` TOS DSCP。

[条件 C-c1637be6fab92cfb](../../evidence/conditions-sets-075.md#c-c1637be6fab92cfb) · [参数 P-1395f8a7ed87e3f7](../../evidence/parameters-sets-002.md#p-1395f8a7ed87e3f7) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003724

```text
(config-perf-meas)# default delay-profile interfaces <cr>
```

Handler ` RVA 0x1ACEF410 `；selector ` 0 `；EOL ` RVA 0x36DD4378 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-41295089077dc321](../../evidence/conditions-sets-025.md#c-41295089077dc321) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003757

```text
(config-perf-meas)# default delay-profile interfaces advertisement <cr>
```

Handler ` RVA 0x1ACF12B0 `；selector ` 0 `；EOL ` RVA 0x36DD28F0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-41295089077dc321](../../evidence/conditions-sets-025.md#c-41295089077dc321) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003811

```text
(config-perf-meas)# default delay-profile interfaces advertisement accelerated <cr>
```

Handler ` RVA 0x1ACF1600 `；selector ` 0 `；EOL ` RVA 0x36DD17A0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-41295089077dc321](../../evidence/conditions-sets-025.md#c-41295089077dc321) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003956

```text
(config-perf-meas)# default delay-profile interfaces advertisement accelerated minimum-change <number:0..1000000> <cr>
```

Handler ` RVA 0x1ACF1BE0 `；selector ` 0 `；EOL ` RVA 0x36DD11F0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Accelerated advertisement minimum change (uSec)。

[条件 C-41295089077dc321](../../evidence/conditions-sets-025.md#c-41295089077dc321) · [参数 P-87f9628a76ee7742](../../evidence/parameters-sets-010.md#p-87f9628a76ee7742) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003970

```text
(config-perf-meas)# default delay-profile interfaces advertisement accelerated threshold <number:0..100> <cr>
```

Handler ` RVA 0x1ACF1AB0 `；selector ` 0 `；EOL ` RVA 0x36DD1508 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Accelerated advertisement threshold percentage change。

[条件 C-41295089077dc321](../../evidence/conditions-sets-025.md#c-41295089077dc321) · [参数 P-f0ea66ce03e923ef](../../evidence/parameters-sets-018.md#p-f0ea66ce03e923ef) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003827

```text
(config-perf-meas)# default delay-profile interfaces advertisement periodic <cr>
```

Handler ` RVA 0x1ACF1830 `；selector ` 0 `；EOL ` RVA 0x36DD2670 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-41295089077dc321](../../evidence/conditions-sets-025.md#c-41295089077dc321) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003935

```text
(config-perf-meas)# default delay-profile interfaces advertisement periodic disabled <cr>
```

Handler ` RVA 0x1ACF1D10 `；selector ` 0 `；EOL ` RVA 0x36DD23C8 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-41295089077dc321](../../evidence/conditions-sets-025.md#c-41295089077dc321) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003986

```text
(config-perf-meas)# default delay-profile interfaces advertisement periodic interval <number:30..3600> <cr>
```

Handler ` RVA 0x1ACF1DB0 `；selector ` 0 `；EOL ` RVA 0x36DD2140 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number `  Periodic advertisement interval (seconds)。

[条件 C-41295089077dc321](../../evidence/conditions-sets-025.md#c-41295089077dc321) · [参数 P-7083362af6595dd1](../../evidence/parameters-sets-009.md#p-7083362af6595dd1) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003968

```text
(config-perf-meas)# default delay-profile interfaces advertisement periodic minimum-change <number:0..1000000> <cr>
```

Handler ` RVA 0x1ACF2050 `；selector ` 0 `；EOL ` RVA 0x36DD1B10 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Periodic advertisement minimum change (uSec)。

[条件 C-41295089077dc321](../../evidence/conditions-sets-025.md#c-41295089077dc321) · [参数 P-a9f06d097ad720d7](../../evidence/parameters-sets-013.md#p-a9f06d097ad720d7) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003981

```text
(config-perf-meas)# default delay-profile interfaces advertisement periodic threshold <number:0..100> <cr>
```

Handler ` RVA 0x1ACF1EA0 `；selector ` 0 `；EOL ` RVA 0x36DD1E50 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Periodic advertisement threshold percentage change。

[条件 C-41295089077dc321](../../evidence/conditions-sets-025.md#c-41295089077dc321) · [参数 P-870c791c38909c22](../../evidence/parameters-sets-010.md#p-870c791c38909c22) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003761

```text
(config-perf-meas)# default delay-profile interfaces probe <cr>
```

Handler ` RVA 0x1ACF1390 `；selector ` 0 `；EOL ` RVA 0x36DD4100 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-41295089077dc321](../../evidence/conditions-sets-025.md#c-41295089077dc321) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003898

```text
(config-perf-meas)# default delay-profile interfaces probe burst-interval <number:30..15000> <cr>
```

Handler ` RVA 0x1ACF2620 `；selector ` 0 `；EOL ` RVA 0x36DD2CB0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Burst interval (msec)。

[条件 C-41295089077dc321](../../evidence/conditions-sets-025.md#c-41295089077dc321) · [参数 P-03cdf0ceed35889a](../../evidence/parameters-sets-001.md#p-03cdf0ceed35889a) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003921

```text
(config-perf-meas)# default delay-profile interfaces probe computation-interval <number:3..3600> <cr>
```

Handler ` RVA 0x1ACF2200 `；selector ` 0 `；EOL ` RVA 0x36DD2FE0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Computation interval (seconds)。

[条件 C-0de0fccfc6b61de9](../../evidence/conditions-sets-006.md#c-0de0fccfc6b61de9) · [参数 P-539c95aaebc2a4a7](../../evidence/parameters-sets-007.md#p-539c95aaebc2a4a7) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003930

```text
(config-perf-meas)# default delay-profile interfaces probe measurement-mode one-way <cr>
```

Handler ` RVA 0x1ACF23D0 `；selector ` 0 `；EOL ` RVA 0x36DD3358 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-04fe53a4531f50fe](../../evidence/conditions-sets-002.md#c-04fe53a4531f50fe) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003931

```text
(config-perf-meas)# default delay-profile interfaces probe measurement-mode two-way <cr>
```

Handler ` RVA 0x1ACF4AA0 `；selector ` 0 `；EOL ` RVA 0x36DD3600 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7abfd7972d30e72c](../../evidence/conditions-sets-048.md#c-7abfd7972d30e72c) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003843

```text
(config-perf-meas)# default delay-profile interfaces probe protocol <cr>
```

Handler ` RVA 0x1ACF2470 `；selector ` 0 `；EOL ` RVA 0x36DD3E68 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-41295089077dc321](../../evidence/conditions-sets-025.md#c-41295089077dc321) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003946

```text
(config-perf-meas)# default delay-profile interfaces probe protocol pm-mpls <cr>
```

Handler ` RVA 0x1ACF46B0 `；selector ` 0 `；EOL ` RVA 0x36DD3BD0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-41295089077dc321](../../evidence/conditions-sets-025.md#c-41295089077dc321) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003937

```text
(config-perf-meas)# default delay-profile interfaces probe protocol twamp-light <cr>
```

Handler ` RVA 0x1ACF45A0 `；selector ` 0 `；EOL ` RVA 0x36DD3928 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-41295089077dc321](../../evidence/conditions-sets-025.md#c-41295089077dc321) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003723

```text
(config-perf-meas)# default delay-profile sr-policy <cr>
```

Handler ` RVA 0x1ACF7130 `；selector ` 0 `；EOL ` RVA 0x36DD0D50 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-bc60556e9da521b4](../../evidence/conditions-sets-073.md#c-bc60556e9da521b4) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003756

```text
(config-perf-meas)# default delay-profile sr-policy advertisement <cr>
```

Handler ` RVA 0x1ACF7470 `；selector ` 0 `；EOL ` RVA 0x36DCDCB8 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-bc60556e9da521b4](../../evidence/conditions-sets-073.md#c-bc60556e9da521b4) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003826

```text
(config-perf-meas)# default delay-profile sr-policy advertisement accelerated <cr>
```

Handler ` RVA 0x1ACF7990 `；selector ` 0 `；EOL ` RVA 0x36DCCBA8 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-bc60556e9da521b4](../../evidence/conditions-sets-073.md#c-bc60556e9da521b4) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003967

```text
(config-perf-meas)# default delay-profile sr-policy advertisement accelerated minimum-change <number:0..1000000> <cr>
```

Handler ` RVA 0x1ACF7EB0 `；selector ` 0 `；EOL ` RVA 0x36DCC5F8 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Accelerated advertisement minimum change (uSec)。

[条件 C-bc60556e9da521b4](../../evidence/conditions-sets-073.md#c-bc60556e9da521b4) · [参数 P-4895a79d21238df7](../../evidence/parameters-sets-006.md#p-4895a79d21238df7) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003980

```text
(config-perf-meas)# default delay-profile sr-policy advertisement accelerated threshold <number:0..100> <cr>
```

Handler ` RVA 0x1ACF7D80 `；selector ` 0 `；EOL ` RVA 0x36DCC910 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Accelerated advertisement threshold percentage change。

[条件 C-bc60556e9da521b4](../../evidence/conditions-sets-073.md#c-bc60556e9da521b4) · [参数 P-812a14f19936cf48](../../evidence/parameters-sets-010.md#p-812a14f19936cf48) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003835

```text
(config-perf-meas)# default delay-profile sr-policy advertisement periodic <cr>
```

Handler ` RVA 0x1ACF7B10 `；selector ` 0 `；EOL ` RVA 0x36DCDA28 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-bc60556e9da521b4](../../evidence/conditions-sets-073.md#c-bc60556e9da521b4) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003942

```text
(config-perf-meas)# default delay-profile sr-policy advertisement periodic disabled <cr>
```

Handler ` RVA 0x1ACF7FE0 `；selector ` 0 `；EOL ` RVA 0x36DCD780 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-bc60556e9da521b4](../../evidence/conditions-sets-073.md#c-bc60556e9da521b4) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003988

```text
(config-perf-meas)# default delay-profile sr-policy advertisement periodic interval <number:30..3600> <cr>
```

Handler ` RVA 0x1ACF8080 `；selector ` 0 `；EOL ` RVA 0x36DCD4F8 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number `  Periodic advertisement interval (seconds)。

[条件 C-bc60556e9da521b4](../../evidence/conditions-sets-073.md#c-bc60556e9da521b4) · [参数 P-70306a4f9901803d](../../evidence/parameters-sets-009.md#p-70306a4f9901803d) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003975

```text
(config-perf-meas)# default delay-profile sr-policy advertisement periodic minimum-change <number:0..1000000> <cr>
```

Handler ` RVA 0x1ACF8320 `；selector ` 0 `；EOL ` RVA 0x36DCCEC8 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Periodic advertisement minimum change (uSec)。

[条件 C-bc60556e9da521b4](../../evidence/conditions-sets-073.md#c-bc60556e9da521b4) · [参数 P-ebd32062bdb101ca](../../evidence/parameters-sets-018.md#p-ebd32062bdb101ca) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003985

```text
(config-perf-meas)# default delay-profile sr-policy advertisement periodic threshold <number:0..100> <cr>
```

Handler ` RVA 0x1ACF8170 `；selector ` 0 `；EOL ` RVA 0x36DCD208 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Periodic advertisement threshold percentage change。

[条件 C-bc60556e9da521b4](../../evidence/conditions-sets-073.md#c-bc60556e9da521b4) · [参数 P-c357520640169781](../../evidence/parameters-sets-015.md#p-c357520640169781) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003820

```text
(config-perf-meas)# default delay-profile sr-policy advertisement threshold-check <cr>
```

Handler ` RVA 0x1ACF7CB0 `；selector ` 0 `；EOL ` RVA 0x36DCC248 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-bc60556e9da521b4](../../evidence/conditions-sets-073.md#c-bc60556e9da521b4) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003868

```text
(config-perf-meas)# default delay-profile sr-policy advertisement threshold-check average-delay <cr>
```

Handler ` RVA 0x1ACF9A00 `；selector ` 0 `；EOL ` RVA 0x36DCBA50 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-bc60556e9da521b4](../../evidence/conditions-sets-073.md#c-bc60556e9da521b4) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003879

```text
(config-perf-meas)# default delay-profile sr-policy advertisement threshold-check maximum-delay <cr>
```

Handler ` RVA 0x1ACF98A0 `；selector ` 0 `；EOL ` RVA 0x36DCBCF8 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-bc60556e9da521b4](../../evidence/conditions-sets-073.md#c-bc60556e9da521b4) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003892

```text
(config-perf-meas)# default delay-profile sr-policy advertisement threshold-check minimum-delay <cr>
```

Handler ` RVA 0x1ACF9740 `；selector ` 0 `；EOL ` RVA 0x36DCBFA0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-bc60556e9da521b4](../../evidence/conditions-sets-073.md#c-bc60556e9da521b4) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003768

```text
(config-perf-meas)# default delay-profile sr-policy liveness-detection <cr>
```

Handler ` RVA 0x1ACF7870 `；selector ` 0 `；EOL ` RVA 0x36DD0AD0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2fff4e5560a73f26](../../evidence/conditions-sets-019.md#c-2fff4e5560a73f26) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003914

```text
(config-perf-meas)# default delay-profile sr-policy liveness-detection multiplier <number:2..10> <cr>
```

Handler ` RVA 0x1ACF9C40 `；selector ` 0 `；EOL ` RVA 0x36DD0838 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Detect Multiplier。

[条件 C-2fff4e5560a73f26](../../evidence/conditions-sets-019.md#c-2fff4e5560a73f26) · [参数 P-ba32c970d6d47746](../../evidence/parameters-sets-014.md#p-ba32c970d6d47746) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003760

```text
(config-perf-meas)# default delay-profile sr-policy probe <cr>
```

Handler ` RVA 0x1ACF75A0 `；selector ` 0 `；EOL ` RVA 0x36DD04C0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-bc60556e9da521b4](../../evidence/conditions-sets-073.md#c-bc60556e9da521b4) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003897

```text
(config-perf-meas)# default delay-profile sr-policy probe burst-interval <number:30..15000> <cr>
```

Handler ` RVA 0x1ACF8B20 `；selector ` 0 `；EOL ` RVA 0x36DCE0A0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Burst interval (msec)。

[条件 C-bc60556e9da521b4](../../evidence/conditions-sets-073.md#c-bc60556e9da521b4) · [参数 P-e0e3f07438fe2b70](../../evidence/parameters-sets-017.md#p-e0e3f07438fe2b70) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003920

```text
(config-perf-meas)# default delay-profile sr-policy probe computation-interval <number:3..3600> <cr>
```

Handler ` RVA 0x1ACF84E0 `；selector ` 0 `；EOL ` RVA 0x36DCE3D0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Computation interval (seconds)。

[条件 C-b07e8095d7e5a931](../../evidence/conditions-sets-068.md#c-b07e8095d7e5a931) · [参数 P-83a40acd71f437c6](../../evidence/parameters-sets-010.md#p-83a40acd71f437c6) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003949

```text
(config-perf-meas)# default delay-profile sr-policy probe measurement-mode loopback <cr>
```

Handler ` RVA 0x1ACF88C0 `；selector ` 0 `；EOL ` RVA 0x36DCF2B8 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-adf7844092e5694c](../../evidence/conditions-sets-067.md#c-adf7844092e5694c) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003943

```text
(config-perf-meas)# default delay-profile sr-policy probe measurement-mode one-way <cr>
```

Handler ` RVA 0x1ACF8990 `；selector ` 0 `；EOL ` RVA 0x36DCED68 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-356dee1b0f10a12f](../../evidence/conditions-sets-021.md#c-356dee1b0f10a12f) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003944

```text
(config-perf-meas)# default delay-profile sr-policy probe measurement-mode two-way <cr>
```

Handler ` RVA 0x1ACF9B60 `；selector ` 0 `；EOL ` RVA 0x36DCF010 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-adf7844092e5694c](../../evidence/conditions-sets-067.md#c-adf7844092e5694c) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003928

```text
(config-perf-meas)# default delay-profile sr-policy probe padding-size <number:0..8000> <cr>
```

Handler ` RVA 0x1ACF8620 `；selector ` 0 `；EOL ` RVA 0x36DCE748 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Padding (bytes) to add to probes。

[条件 C-7fd6f1b4ba602c18](../../evidence/conditions-sets-050.md#c-7fd6f1b4ba602c18) · [参数 P-8b71d0a5c6717335](../../evidence/parameters-sets-011.md#p-8b71d0a5c6717335) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003848

```text
(config-perf-meas)# default delay-profile sr-policy probe protocol <cr>
```

Handler ` RVA 0x1ACF8A60 `；selector ` 0 `；EOL ` RVA 0x36DCFB58 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8b55d0da06b70929](../../evidence/conditions-sets-054.md#c-8b55d0da06b70929) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003951

```text
(config-perf-meas)# default delay-profile sr-policy probe protocol pm-mpls <cr>
```

Handler ` RVA 0x1ACF8E00 `；selector ` 0 `；EOL ` RVA 0x36DCF8C0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8b55d0da06b70929](../../evidence/conditions-sets-054.md#c-8b55d0da06b70929) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003948

```text
(config-perf-meas)# default delay-profile sr-policy probe protocol twamp-light <cr>
```

Handler ` RVA 0x1ACF8C90 `；selector ` 0 `；EOL ` RVA 0x36DCF618 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8b55d0da06b70929](../../evidence/conditions-sets-054.md#c-8b55d0da06b70929) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003850

```text
(config-perf-meas)# default delay-profile sr-policy probe sweep <cr>
```

Handler ` RVA 0x1ACF8F70 `；selector ` 0 `；EOL ` RVA 0x36DD0200 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8b55d0da06b70929](../../evidence/conditions-sets-054.md#c-8b55d0da06b70929) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003997

```text
(config-perf-meas)# default delay-profile sr-policy probe sweep destination ipv4 <address> range <number:0..128> <cr>
```

Handler ` RVA 0x1ACF9020 `；selector ` 0 `；EOL ` RVA 0x36DCFF50 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IPv4 address (Required to be a 127.0.0.0/8 address)；` unsigned_number ` Sweeping range (Should fully be in the 127.0.0.0/8 space)。

[条件 C-8b55d0da06b70929](../../evidence/conditions-sets-054.md#c-8b55d0da06b70929) · [参数 P-3dd866ae41e7e577](../../evidence/parameters-sets-005.md#p-3dd866ae41e7e577) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003929

```text
(config-perf-meas)# default delay-profile sr-policy probe tos-dscp <number:0..63> <cr>
```

Handler ` RVA 0x1ACF8740 `；selector ` 0 `；EOL ` RVA 0x36DCEA38 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` TOS DSCP。

[条件 C-8b55d0da06b70929](../../evidence/conditions-sets-054.md#c-8b55d0da06b70929) · [参数 P-e1cfa9d140cff418](../../evidence/parameters-sets-017.md#p-e1cfa9d140cff418) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003794

```text
(config-perf-meas)# default dual-color gre bit-position <number:9..12> <cr>
```

Handler ` RVA 0x1ACF3B10 `；selector ` 0 `；EOL ` RVA 0x36DD7F80 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` bit-position value。

[条件 C-e0f33479f97c1ab8](../../evidence/conditions-sets-087.md#c-e0f33479f97c1ab8) · [参数 P-e08eb5e7b4635707](../../evidence/parameters-sets-017.md#p-e08eb5e7b4635707) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003719

```text
(config-perf-meas)# default endpoint <string> <cr>
```

Handler ` RVA 0x1ACFA0B0 `；selector ` 0 `；EOL ` RVA 0x36DC3EB0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Endpoint Name。

[参数 P-214ba9e98f3de846](../../evidence/parameters-sets-003.md#p-214ba9e98f3de846) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003731

```text
(config-perf-meas)# default endpoint <string> delay-measurement <cr>
```

Handler ` RVA 0x1ACFA820 `；selector ` 0 `；EOL ` RVA 0x36DC2A30 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Endpoint Name。

[参数 P-214ba9e98f3de846](../../evidence/parameters-sets-003.md#p-214ba9e98f3de846) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003854

```text
(config-perf-meas)# default endpoint <string> delay-measurement profile <string> <cr>
```

Handler ` RVA 0x1ACFAA20 `；selector ` 0 `；EOL ` RVA 0x36DC27B0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Endpoint Name；` string ` Profile name。

[参数 P-4e504d294400b577](../../evidence/parameters-sets-006.md#p-4e504d294400b577) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003852

```text
(config-perf-meas)# default endpoint <string> destination-address ipv4 <address> <cr>
```

Handler ` RVA 0x1ACFA520 `；selector ` 0 `；EOL ` RVA 0x36DC23F0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Endpoint Name；` address ` IPv4 endpoint address。

[参数 P-02c0cdf85ff294f8](../../evidence/parameters-sets-001.md#p-02c0cdf85ff294f8) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003749

```text
(config-perf-meas)# default endpoint <string> segment-list <cr>
```

Handler ` RVA 0x1ACFA770 `；selector ` 0 `；EOL ` RVA 0x36DC3988 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Endpoint Name。

[参数 P-214ba9e98f3de846](../../evidence/parameters-sets-003.md#p-214ba9e98f3de846) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003863

```text
(config-perf-meas)# default endpoint <string> segment-list forward-path <string> <cr>
```

Handler ` RVA 0x1ACFAB50 `；selector ` 0 `；EOL ` RVA 0x36DC3420 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Endpoint Name；` string ` Identifying name for segment-list。

[参数 P-cfd0a0cac03a746e](../../evidence/parameters-sets-016.md#p-cfd0a0cac03a746e) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003872

```text
(config-perf-meas)# default endpoint <string> segment-list reverse-path <string> <cr>
```

Handler ` RVA 0x1ACFACB0 `；selector ` 0 `；EOL ` RVA 0x36DC3708 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Endpoint Name；` string ` Identifying name for reverse path segment-list。

[参数 P-fd63338fb07cefeb](../../evidence/parameters-sets-019.md#p-fd63338fb07cefeb) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003733

```text
(config-perf-meas)# default endpoint <string> shutdown <cr>
```

Handler ` RVA 0x1ACFA990 `；selector ` 0 `；EOL ` RVA 0x36DC3C08 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Endpoint Name。

[参数 P-214ba9e98f3de846](../../evidence/parameters-sets-003.md#p-214ba9e98f3de846) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003857

```text
(config-perf-meas)# default endpoint <string> source-address ipv4 <address> <cr>
```

Handler ` RVA 0x1ACFA400 `；selector ` 0 `；EOL ` RVA 0x36DC2D78 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Endpoint Name；` address ` IPv4 source address。

[参数 P-27a7405fba1b69b4](../../evidence/parameters-sets-003.md#p-27a7405fba1b69b4) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003778

```text
(config-perf-meas)# default endpoint <string> vrf <string> <cr>
```

Handler ` RVA 0x1ACFA640 `；selector ` 0 `；EOL ` RVA 0x36DC30D0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Endpoint Name；` string ` VRF Name。

[参数 P-6fc9a77829f84728](../../evidence/parameters-sets-009.md#p-6fc9a77829f84728) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003710

```text
(config-perf-meas)# default loss-profile interfaces <cr>
```

Handler ` RVA 0x1ACEF800 `；selector ` 0 `；EOL ` RVA 0x36DC6DA8 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-606b89fe7872f8c5](../../evidence/conditions-sets-037.md#c-606b89fe7872f8c5) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003738

```text
(config-perf-meas)# default loss-profile interfaces advertisement <cr>
```

Handler ` RVA 0x1ACEFAF0 `；selector ` 0 `；EOL ` RVA 0x36DC5670 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-606b89fe7872f8c5](../../evidence/conditions-sets-037.md#c-606b89fe7872f8c5) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003800

```text
(config-perf-meas)# default loss-profile interfaces advertisement anomaly-check <cr>
```

Handler ` RVA 0x1ACEFE40 `；selector ` 0 `；EOL ` RVA 0x36DC5010 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-606b89fe7872f8c5](../../evidence/conditions-sets-037.md#c-606b89fe7872f8c5) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003792

```text
(config-perf-meas)# default loss-profile interfaces advertisement periodic <cr>
```

Handler ` RVA 0x1ACEFD90 `；selector ` 0 `；EOL ` RVA 0x36DC4CB8 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-606b89fe7872f8c5](../../evidence/conditions-sets-037.md#c-606b89fe7872f8c5) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003953

```text
(config-perf-meas)# default loss-profile interfaces advertisement periodic interval <number:30..3600> <cr>
```

Handler ` RVA 0x1ACF01C0 `；selector ` 0 `；EOL ` RVA 0x36DC4400 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` interval value in sec。

[条件 C-606b89fe7872f8c5](../../evidence/conditions-sets-037.md#c-606b89fe7872f8c5) · [参数 P-22673dbf4dd5bf85](../../evidence/parameters-sets-003.md#p-22673dbf4dd5bf85) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003759

```text
(config-perf-meas)# default loss-profile interfaces probe <cr>
```

Handler ` RVA 0x1ACEFC30 `；selector ` 0 `；EOL ` RVA 0x36DC6B18 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-606b89fe7872f8c5](../../evidence/conditions-sets-037.md#c-606b89fe7872f8c5) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003812

```text
(config-perf-meas)# default loss-profile interfaces probe color-type <cr>
```

Handler ` RVA 0x1ACF0550 `；selector ` 0 `；EOL ` RVA 0x36DC65A8 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-606b89fe7872f8c5](../../evidence/conditions-sets-037.md#c-606b89fe7872f8c5) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003964

```text
(config-perf-meas)# default loss-profile interfaces probe color-type dual-color gre <cr>
```

Handler ` RVA 0x1ACF0B20 `；selector ` 0 `；EOL ` RVA 0x36DC6318 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-606b89fe7872f8c5](../../evidence/conditions-sets-037.md#c-606b89fe7872f8c5) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003904

```text
(config-perf-meas)# default loss-profile interfaces probe color-type single-color <cr>
```

Handler ` RVA 0x1ACF0700 `；selector ` 0 `；EOL ` RVA 0x36DC6030 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-606b89fe7872f8c5](../../evidence/conditions-sets-037.md#c-606b89fe7872f8c5) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003990

```text
(config-perf-meas)# default loss-profile interfaces probe color-type single-color max-reordering <number:100..2000> <cr>
```

Handler ` RVA 0x1ACF0A10 `；selector ` 0 `；EOL ` RVA 0x36DC5DA8 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` maximum expected reordering value in miliseconds。

[条件 C-606b89fe7872f8c5](../../evidence/conditions-sets-037.md#c-606b89fe7872f8c5) · [参数 P-59fd1598f3c3c6cd](../../evidence/parameters-sets-007.md#p-59fd1598f3c3c6cd) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003877

```text
(config-perf-meas)# default loss-profile interfaces probe tx-interval <number:10..1000> <cr>
```

Handler ` RVA 0x1ACF05F0 `；selector ` 0 `；EOL ` RVA 0x36DC6890 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Transmit interval value in sec。

[条件 C-606b89fe7872f8c5](../../evidence/conditions-sets-037.md#c-606b89fe7872f8c5) · [参数 P-1741a8166c9b6621](../../evidence/parameters-sets-002.md#p-1741a8166c9b6621) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003713

```text
(config-perf-meas)# default protocol sdlm-light <cr>
```

Handler ` RVA 0x1ACEF690 `；selector ` 0 `；EOL ` RVA 0x36DD6BA0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-88ca28e64264fc2c](../../evidence/conditions-sets-053.md#c-88ca28e64264fc2c) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003798

```text
(config-perf-meas)# default protocol sdlm-light measurement loss <cr>
```

Handler ` RVA 0x1ACF35D0 `；selector ` 0 `；EOL ` RVA 0x36DD6920 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-88ca28e64264fc2c](../../evidence/conditions-sets-053.md#c-88ca28e64264fc2c) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003893

```text
(config-perf-meas)# default protocol sdlm-light measurement loss unauthenticated <cr>
```

Handler ` RVA 0x1ACF36F0 `；selector ` 0 `；EOL ` RVA 0x36DD62E0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-88ca28e64264fc2c](../../evidence/conditions-sets-053.md#c-88ca28e64264fc2c) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003993

```text
(config-perf-meas)# default protocol sdlm-light measurement loss unauthenticated querier-dst-port <number:1024..14999> <cr>
```

Handler ` RVA 0x1ACF3ED0 `；selector ` 0 `；EOL ` RVA 0x36DD6608 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Port number。

[条件 C-44f9b47a32de3af8](../../evidence/conditions-sets-027.md#c-44f9b47a32de3af8) · [参数 P-4ec43d1805d651a6](../../evidence/parameters-sets-006.md#p-4ec43d1805d651a6) · [状态效果 S-03a0508c58e28878](../../evidence/state_effects-sets-001.md#s-03a0508c58e28878)

### observed_connections-003714

```text
(config-perf-meas)# default protocol twamp-light <cr>
```

Handler ` RVA 0x1ACEF5A0 `；selector ` 0 `；EOL ` RVA 0x36DD78D8 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-25db707dca9abfe1](../../evidence/conditions-sets-015.md#c-25db707dca9abfe1) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003799

```text
(config-perf-meas)# default protocol twamp-light measurement delay <cr>
```

Handler ` RVA 0x1ACF31D0 `；selector ` 0 `；EOL ` RVA 0x36DD7658 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-25db707dca9abfe1](../../evidence/conditions-sets-015.md#c-25db707dca9abfe1) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003894

```text
(config-perf-meas)# default protocol twamp-light measurement delay unauthenticated <cr>
```

Handler ` RVA 0x1ACF3310 `；selector ` 0 `；EOL ` RVA 0x36DD6FB8 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-25db707dca9abfe1](../../evidence/conditions-sets-015.md#c-25db707dca9abfe1) · [状态效果 S-3f44b00038732d08](../../evidence/state_effects-sets-014.md#s-3f44b00038732d08)

### observed_connections-003994

```text
(config-perf-meas)# default protocol twamp-light measurement delay unauthenticated querier-dst-port <number:1024..14999> <cr>
```

Handler ` RVA 0x1ACF3BA0 `；selector ` 0 `；EOL ` RVA 0x36DD7308 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Port number。

[条件 C-701c7f308097b0b4](../../evidence/conditions-sets-043.md#c-701c7f308097b0b4) · [参数 P-3c1718846fb39911](../../evidence/parameters-sets-005.md#p-3c1718846fb39911) · [状态效果 S-3e7b6dd43b715f17](../../evidence/state_effects-sets-014.md#s-3e7b6dd43b715f17)

### observed_connections-003696

```text
(config-perf-meas)# delay-profile endpoint <cr>
```

Handler ` RVA 0x1ACF9DE0 `；selector ` 0 `；EOL ` RVA 0x36DCB5B0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c1637be6fab92cfb](../../evidence/conditions-sets-075.md#c-c1637be6fab92cfb)

### observed_connections-003709

```text
(config-perf-meas)# delay-profile endpoint advertisement <cr>
```

Handler ` RVA 0x1ACFAE10 `；selector ` 0 `；EOL ` RVA 0x36DC94E8 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c1637be6fab92cfb](../../evidence/conditions-sets-075.md#c-c1637be6fab92cfb)

### observed_connections-003758

```text
(config-perf-meas)# delay-profile endpoint advertisement accelerated <cr>
```

Handler ` RVA 0x1ACFB3D0 `；selector ` 0 `；EOL ` RVA 0x36DC83D8 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c1637be6fab92cfb](../../evidence/conditions-sets-075.md#c-c1637be6fab92cfb)

### observed_connections-003869

```text
(config-perf-meas)# delay-profile endpoint advertisement accelerated minimum-change <number:0..1000000> <cr>
```

Handler ` RVA 0x1ACFB890 `；selector ` 0 `；EOL ` RVA 0x36DC7E28 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Accelerated advertisement minimum change (uSec)。

[条件 C-c1637be6fab92cfb](../../evidence/conditions-sets-075.md#c-c1637be6fab92cfb) · [参数 P-9f6f6ba2d130deb9](../../evidence/parameters-sets-012.md#p-9f6f6ba2d130deb9)

### observed_connections-003889

```text
(config-perf-meas)# delay-profile endpoint advertisement accelerated threshold <number:0..100> <cr>
```

Handler ` RVA 0x1ACFB760 `；selector ` 0 `；EOL ` RVA 0x36DC8140 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Accelerated advertisement threshold percentage change。

[条件 C-c1637be6fab92cfb](../../evidence/conditions-sets-075.md#c-c1637be6fab92cfb) · [参数 P-2bf284102dc3b5f7](../../evidence/parameters-sets-004.md#p-2bf284102dc3b5f7)

### observed_connections-003763

```text
(config-perf-meas)# delay-profile endpoint advertisement periodic <cr>
```

Handler ` RVA 0x1ACFB520 `；selector ` 0 `；EOL ` RVA 0x36DC9258 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c1637be6fab92cfb](../../evidence/conditions-sets-075.md#c-c1637be6fab92cfb)

### observed_connections-003825

```text
(config-perf-meas)# delay-profile endpoint advertisement periodic disabled <cr>
```

Handler ` RVA 0x1ACFB9C0 `；selector ` 0 `；EOL ` RVA 0x36DC8FB0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c1637be6fab92cfb](../../evidence/conditions-sets-075.md#c-c1637be6fab92cfb)

### observed_connections-003908

```text
(config-perf-meas)# delay-profile endpoint advertisement periodic interval <number:30..3600> <cr>
```

Handler ` RVA 0x1ACFBA60 `；selector ` 0 `；EOL ` RVA 0x36DC8D28 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number `  Periodic advertisement interval (seconds)。

[条件 C-c1637be6fab92cfb](../../evidence/conditions-sets-075.md#c-c1637be6fab92cfb) · [参数 P-9239b3dae0fed22a](../../evidence/parameters-sets-011.md#p-9239b3dae0fed22a)

### observed_connections-003875

```text
(config-perf-meas)# delay-profile endpoint advertisement periodic minimum-change <number:0..1000000> <cr>
```

Handler ` RVA 0x1ACFBD00 `；selector ` 0 `；EOL ` RVA 0x36DC86F8 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Periodic advertisement minimum change (uSec)。

[条件 C-c1637be6fab92cfb](../../evidence/conditions-sets-075.md#c-c1637be6fab92cfb) · [参数 P-ca7c92d34181e004](../../evidence/parameters-sets-015.md#p-ca7c92d34181e004)

### observed_connections-003900

```text
(config-perf-meas)# delay-profile endpoint advertisement periodic threshold <number:0..100> <cr>
```

Handler ` RVA 0x1ACFBB50 `；selector ` 0 `；EOL ` RVA 0x36DC8A38 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Periodic advertisement threshold percentage change。

[条件 C-c1637be6fab92cfb](../../evidence/conditions-sets-075.md#c-c1637be6fab92cfb) · [参数 P-0f8747ef381467d2](../../evidence/parameters-sets-002.md#p-0f8747ef381467d2)

### observed_connections-003750

```text
(config-perf-meas)# delay-profile endpoint advertisement threshold-check <cr>
```

Handler ` RVA 0x1ACFB6B0 `；selector ` 0 `；EOL ` RVA 0x36DC7A78 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c1637be6fab92cfb](../../evidence/conditions-sets-075.md#c-c1637be6fab92cfb)

### observed_connections-003777

```text
(config-perf-meas)# delay-profile endpoint advertisement threshold-check average-delay <cr>
```

Handler ` RVA 0x1ACFCC80 `；selector ` 0 `；EOL ` RVA 0x36DC7280 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c1637be6fab92cfb](../../evidence/conditions-sets-075.md#c-c1637be6fab92cfb)

### observed_connections-003780

```text
(config-perf-meas)# delay-profile endpoint advertisement threshold-check maximum-delay <cr>
```

Handler ` RVA 0x1ACFCB30 `；selector ` 0 `；EOL ` RVA 0x36DC7528 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c1637be6fab92cfb](../../evidence/conditions-sets-075.md#c-c1637be6fab92cfb)

### observed_connections-003783

```text
(config-perf-meas)# delay-profile endpoint advertisement threshold-check minimum-delay <cr>
```

Handler ` RVA 0x1ACFC9E0 `；selector ` 0 `；EOL ` RVA 0x36DC77D0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c1637be6fab92cfb](../../evidence/conditions-sets-075.md#c-c1637be6fab92cfb)

### observed_connections-003727

```text
(config-perf-meas)# delay-profile endpoint liveness-detection <cr>
```

Handler ` RVA 0x1ACFB2C0 `；selector ` 0 `；EOL ` RVA 0x36DCB330 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97664056404981c7](../../evidence/conditions-sets-058.md#c-97664056404981c7)

### observed_connections-003807

```text
(config-perf-meas)# delay-profile endpoint liveness-detection multiplier <number:2..10> <cr>
```

Handler ` RVA 0x1ACFCEA0 `；selector ` 0 `；EOL ` RVA 0x36DCB098 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Detect Multiplier。

[条件 C-97664056404981c7](../../evidence/conditions-sets-058.md#c-97664056404981c7) · [参数 P-832a3c41773baa51](../../evidence/parameters-sets-010.md#p-832a3c41773baa51)

### observed_connections-003715

```text
(config-perf-meas)# delay-profile endpoint probe <cr>
```

Handler ` RVA 0x1ACFB040 `；selector ` 0 `；EOL ` RVA 0x36DCAD20 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c1637be6fab92cfb](../../evidence/conditions-sets-075.md#c-c1637be6fab92cfb)

### observed_connections-003787

```text
(config-perf-meas)# delay-profile endpoint probe burst-interval <number:30..15000> <cr>
```

Handler ` RVA 0x1ACFC440 `；selector ` 0 `；EOL ` RVA 0x36DC98D0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Burst interval (msec)。

[条件 C-c1637be6fab92cfb](../../evidence/conditions-sets-075.md#c-c1637be6fab92cfb) · [参数 P-f4437d88dc812964](../../evidence/parameters-sets-018.md#p-f4437d88dc812964)

### observed_connections-003809

```text
(config-perf-meas)# delay-profile endpoint probe computation-interval <number:3..3600> <cr>
```

Handler ` RVA 0x1ACFC0E0 `；selector ` 0 `；EOL ` RVA 0x36DC9C00 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Computation interval (seconds)。

[条件 C-0b907c9f8f450fdb](../../evidence/conditions-sets-005.md#c-0b907c9f8f450fdb) · [参数 P-d09a80bed29e4458](../../evidence/parameters-sets-016.md#p-d09a80bed29e4458)

### observed_connections-003837

```text
(config-perf-meas)# delay-profile endpoint probe measurement-mode loopback <cr>
```

Handler ` RVA 0x1ACFC2A0 `；selector ` 0 `；EOL ` RVA 0x36DCAA40 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c1637be6fab92cfb](../../evidence/conditions-sets-075.md#c-c1637be6fab92cfb)

### observed_connections-003822

```text
(config-perf-meas)# delay-profile endpoint probe measurement-mode one-way <cr>
```

Handler ` RVA 0x1ACFC370 `；selector ` 0 `；EOL ` RVA 0x36DCA4F0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c1637be6fab92cfb](../../evidence/conditions-sets-075.md#c-c1637be6fab92cfb)

### observed_connections-003833

```text
(config-perf-meas)# delay-profile endpoint probe measurement-mode two-way <cr>
```

Handler ` RVA 0x1ACFCDE0 `；selector ` 0 `；EOL ` RVA 0x36DCA798 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c1637be6fab92cfb](../../evidence/conditions-sets-075.md#c-c1637be6fab92cfb)

### observed_connections-003808

```text
(config-perf-meas)# delay-profile endpoint probe padding-size <number:0..8000> <cr>
```

Handler ` RVA 0x1ACFBEC0 `；selector ` 0 `；EOL ` RVA 0x36DC9F38 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Padding (bytes) to add to probes。

[条件 C-c1637be6fab92cfb](../../evidence/conditions-sets-075.md#c-c1637be6fab92cfb) · [参数 P-0f90b03d9cc18eae](../../evidence/parameters-sets-002.md#p-0f90b03d9cc18eae)

### observed_connections-003816

```text
(config-perf-meas)# delay-profile endpoint probe tos-dscp <number:0..63> <cr>
```

Handler ` RVA 0x1ACFBFE0 `；selector ` 0 `；EOL ` RVA 0x36DCA228 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` TOS DSCP。

[条件 C-c1637be6fab92cfb](../../evidence/conditions-sets-075.md#c-c1637be6fab92cfb) · [参数 P-1395f8a7ed87e3f7](../../evidence/parameters-sets-002.md#p-1395f8a7ed87e3f7)

### observed_connections-003701

```text
(config-perf-meas)# delay-profile interfaces <cr>
```

Handler ` RVA 0x1ACEF410 `；selector ` 0 `；EOL ` RVA 0x36DD4378 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-41295089077dc321](../../evidence/conditions-sets-025.md#c-41295089077dc321)

### observed_connections-003721

```text
(config-perf-meas)# delay-profile interfaces advertisement <cr>
```

Handler ` RVA 0x1ACF12B0 `；selector ` 0 `；EOL ` RVA 0x36DD28F0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-41295089077dc321](../../evidence/conditions-sets-025.md#c-41295089077dc321)

### observed_connections-003754

```text
(config-perf-meas)# delay-profile interfaces advertisement accelerated <cr>
```

Handler ` RVA 0x1ACF1600 `；selector ` 0 `；EOL ` RVA 0x36DD17A0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-41295089077dc321](../../evidence/conditions-sets-025.md#c-41295089077dc321)

### observed_connections-003867

```text
(config-perf-meas)# delay-profile interfaces advertisement accelerated minimum-change <number:0..1000000> <cr>
```

Handler ` RVA 0x1ACF1BE0 `；selector ` 0 `；EOL ` RVA 0x36DD11F0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Accelerated advertisement minimum change (uSec)。

[条件 C-41295089077dc321](../../evidence/conditions-sets-025.md#c-41295089077dc321) · [参数 P-87f9628a76ee7742](../../evidence/parameters-sets-010.md#p-87f9628a76ee7742)

### observed_connections-003888

```text
(config-perf-meas)# delay-profile interfaces advertisement accelerated threshold <number:0..100> <cr>
```

Handler ` RVA 0x1ACF1AB0 `；selector ` 0 `；EOL ` RVA 0x36DD1508 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Accelerated advertisement threshold percentage change。

[条件 C-41295089077dc321](../../evidence/conditions-sets-025.md#c-41295089077dc321) · [参数 P-f0ea66ce03e923ef](../../evidence/parameters-sets-018.md#p-f0ea66ce03e923ef)

### observed_connections-003767

```text
(config-perf-meas)# delay-profile interfaces advertisement periodic <cr>
```

Handler ` RVA 0x1ACF1830 `；selector ` 0 `；EOL ` RVA 0x36DD2670 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-41295089077dc321](../../evidence/conditions-sets-025.md#c-41295089077dc321)

### observed_connections-003834

```text
(config-perf-meas)# delay-profile interfaces advertisement periodic disabled <cr>
```

Handler ` RVA 0x1ACF1D10 `；selector ` 0 `；EOL ` RVA 0x36DD23C8 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-41295089077dc321](../../evidence/conditions-sets-025.md#c-41295089077dc321)

### observed_connections-003916

```text
(config-perf-meas)# delay-profile interfaces advertisement periodic interval <number:30..3600> <cr>
```

Handler ` RVA 0x1ACF1DB0 `；selector ` 0 `；EOL ` RVA 0x36DD2140 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number `  Periodic advertisement interval (seconds)。

[条件 C-41295089077dc321](../../evidence/conditions-sets-025.md#c-41295089077dc321) · [参数 P-7083362af6595dd1](../../evidence/parameters-sets-009.md#p-7083362af6595dd1)

### observed_connections-003884

```text
(config-perf-meas)# delay-profile interfaces advertisement periodic minimum-change <number:0..1000000> <cr>
```

Handler ` RVA 0x1ACF2050 `；selector ` 0 `；EOL ` RVA 0x36DD1B10 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Periodic advertisement minimum change (uSec)。

[条件 C-41295089077dc321](../../evidence/conditions-sets-025.md#c-41295089077dc321) · [参数 P-a9f06d097ad720d7](../../evidence/parameters-sets-013.md#p-a9f06d097ad720d7)

### observed_connections-003907

```text
(config-perf-meas)# delay-profile interfaces advertisement periodic threshold <number:0..100> <cr>
```

Handler ` RVA 0x1ACF1EA0 `；selector ` 0 `；EOL ` RVA 0x36DD1E50 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Periodic advertisement threshold percentage change。

[条件 C-41295089077dc321](../../evidence/conditions-sets-025.md#c-41295089077dc321) · [参数 P-870c791c38909c22](../../evidence/parameters-sets-010.md#p-870c791c38909c22)

### observed_connections-003726

```text
(config-perf-meas)# delay-profile interfaces probe <cr>
```

Handler ` RVA 0x1ACF1390 `；selector ` 0 `；EOL ` RVA 0x36DD4100 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-41295089077dc321](../../evidence/conditions-sets-025.md#c-41295089077dc321)

### observed_connections-003806

```text
(config-perf-meas)# delay-profile interfaces probe burst-interval <number:30..15000> <cr>
```

Handler ` RVA 0x1ACF2620 `；selector ` 0 `；EOL ` RVA 0x36DD2CB0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Burst interval (msec)。

[条件 C-41295089077dc321](../../evidence/conditions-sets-025.md#c-41295089077dc321) · [参数 P-03cdf0ceed35889a](../../evidence/parameters-sets-001.md#p-03cdf0ceed35889a)

### observed_connections-003824

```text
(config-perf-meas)# delay-profile interfaces probe computation-interval <number:3..3600> <cr>
```

Handler ` RVA 0x1ACF2200 `；selector ` 0 `；EOL ` RVA 0x36DD2FE0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Computation interval (seconds)。

[条件 C-0de0fccfc6b61de9](../../evidence/conditions-sets-006.md#c-0de0fccfc6b61de9) · [参数 P-539c95aaebc2a4a7](../../evidence/parameters-sets-007.md#p-539c95aaebc2a4a7)

### observed_connections-003831

```text
(config-perf-meas)# delay-profile interfaces probe measurement-mode one-way <cr>
```

Handler ` RVA 0x1ACF23D0 `；selector ` 0 `；EOL ` RVA 0x36DD3358 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-04fe53a4531f50fe](../../evidence/conditions-sets-002.md#c-04fe53a4531f50fe)

### observed_connections-003832

```text
(config-perf-meas)# delay-profile interfaces probe measurement-mode two-way <cr>
```

Handler ` RVA 0x1ACF4AA0 `；selector ` 0 `；EOL ` RVA 0x36DD3600 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7abfd7972d30e72c](../../evidence/conditions-sets-048.md#c-7abfd7972d30e72c)

### observed_connections-003770

```text
(config-perf-meas)# delay-profile interfaces probe protocol <cr>
```

Handler ` RVA 0x1ACF2470 `；selector ` 0 `；EOL ` RVA 0x36DD3E68 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-41295089077dc321](../../evidence/conditions-sets-025.md#c-41295089077dc321)

### observed_connections-003842

```text
(config-perf-meas)# delay-profile interfaces probe protocol pm-mpls <cr>
```

Handler ` RVA 0x1ACF46B0 `；selector ` 0 `；EOL ` RVA 0x36DD3BD0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-41295089077dc321](../../evidence/conditions-sets-025.md#c-41295089077dc321)

### observed_connections-003836

```text
(config-perf-meas)# delay-profile interfaces probe protocol twamp-light <cr>
```

Handler ` RVA 0x1ACF45A0 `；selector ` 0 `；EOL ` RVA 0x36DD3928 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-41295089077dc321](../../evidence/conditions-sets-025.md#c-41295089077dc321)

### observed_connections-003700

```text
(config-perf-meas)# delay-profile sr-policy <cr>
```

Handler ` RVA 0x1ACF7130 `；selector ` 0 `；EOL ` RVA 0x36DD0D50 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bc60556e9da521b4](../../evidence/conditions-sets-073.md#c-bc60556e9da521b4)

### observed_connections-003720

```text
(config-perf-meas)# delay-profile sr-policy advertisement <cr>
```

Handler ` RVA 0x1ACF7470 `；selector ` 0 `；EOL ` RVA 0x36DCDCB8 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bc60556e9da521b4](../../evidence/conditions-sets-073.md#c-bc60556e9da521b4)

### observed_connections-003766

```text
(config-perf-meas)# delay-profile sr-policy advertisement accelerated <cr>
```

Handler ` RVA 0x1ACF7990 `；selector ` 0 `；EOL ` RVA 0x36DCCBA8 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bc60556e9da521b4](../../evidence/conditions-sets-073.md#c-bc60556e9da521b4)

### observed_connections-003883

```text
(config-perf-meas)# delay-profile sr-policy advertisement accelerated minimum-change <number:0..1000000> <cr>
```

Handler ` RVA 0x1ACF7EB0 `；selector ` 0 `；EOL ` RVA 0x36DCC5F8 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Accelerated advertisement minimum change (uSec)。

[条件 C-bc60556e9da521b4](../../evidence/conditions-sets-073.md#c-bc60556e9da521b4) · [参数 P-4895a79d21238df7](../../evidence/parameters-sets-006.md#p-4895a79d21238df7)

### observed_connections-003906

```text
(config-perf-meas)# delay-profile sr-policy advertisement accelerated threshold <number:0..100> <cr>
```

Handler ` RVA 0x1ACF7D80 `；selector ` 0 `；EOL ` RVA 0x36DCC910 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Accelerated advertisement threshold percentage change。

[条件 C-bc60556e9da521b4](../../evidence/conditions-sets-073.md#c-bc60556e9da521b4) · [参数 P-812a14f19936cf48](../../evidence/parameters-sets-010.md#p-812a14f19936cf48)

### observed_connections-003769

```text
(config-perf-meas)# delay-profile sr-policy advertisement periodic <cr>
```

Handler ` RVA 0x1ACF7B10 `；selector ` 0 `；EOL ` RVA 0x36DCDA28 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bc60556e9da521b4](../../evidence/conditions-sets-073.md#c-bc60556e9da521b4)

### observed_connections-003838

```text
(config-perf-meas)# delay-profile sr-policy advertisement periodic disabled <cr>
```

Handler ` RVA 0x1ACF7FE0 `；selector ` 0 `；EOL ` RVA 0x36DCD780 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bc60556e9da521b4](../../evidence/conditions-sets-073.md#c-bc60556e9da521b4)

### observed_connections-003927

```text
(config-perf-meas)# delay-profile sr-policy advertisement periodic interval <number:30..3600> <cr>
```

Handler ` RVA 0x1ACF8080 `；selector ` 0 `；EOL ` RVA 0x36DCD4F8 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number `  Periodic advertisement interval (seconds)。

[条件 C-bc60556e9da521b4](../../evidence/conditions-sets-073.md#c-bc60556e9da521b4) · [参数 P-70306a4f9901803d](../../evidence/parameters-sets-009.md#p-70306a4f9901803d)

### observed_connections-003896

```text
(config-perf-meas)# delay-profile sr-policy advertisement periodic minimum-change <number:0..1000000> <cr>
```

Handler ` RVA 0x1ACF8320 `；selector ` 0 `；EOL ` RVA 0x36DCCEC8 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Periodic advertisement minimum change (uSec)。

[条件 C-bc60556e9da521b4](../../evidence/conditions-sets-073.md#c-bc60556e9da521b4) · [参数 P-ebd32062bdb101ca](../../evidence/parameters-sets-018.md#p-ebd32062bdb101ca)

### observed_connections-003915

```text
(config-perf-meas)# delay-profile sr-policy advertisement periodic threshold <number:0..100> <cr>
```

Handler ` RVA 0x1ACF8170 `；selector ` 0 `；EOL ` RVA 0x36DCD208 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Periodic advertisement threshold percentage change。

[条件 C-bc60556e9da521b4](../../evidence/conditions-sets-073.md#c-bc60556e9da521b4) · [参数 P-c357520640169781](../../evidence/parameters-sets-015.md#p-c357520640169781)

### observed_connections-003764

```text
(config-perf-meas)# delay-profile sr-policy advertisement threshold-check <cr>
```

Handler ` RVA 0x1ACF7CB0 `；selector ` 0 `；EOL ` RVA 0x36DCC248 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bc60556e9da521b4](../../evidence/conditions-sets-073.md#c-bc60556e9da521b4)

### observed_connections-003781

```text
(config-perf-meas)# delay-profile sr-policy advertisement threshold-check average-delay <cr>
```

Handler ` RVA 0x1ACF9A00 `；selector ` 0 `；EOL ` RVA 0x36DCBA50 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bc60556e9da521b4](../../evidence/conditions-sets-073.md#c-bc60556e9da521b4)

### observed_connections-003788

```text
(config-perf-meas)# delay-profile sr-policy advertisement threshold-check maximum-delay <cr>
```

Handler ` RVA 0x1ACF98A0 `；selector ` 0 `；EOL ` RVA 0x36DCBCF8 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bc60556e9da521b4](../../evidence/conditions-sets-073.md#c-bc60556e9da521b4)

### observed_connections-003795

```text
(config-perf-meas)# delay-profile sr-policy advertisement threshold-check minimum-delay <cr>
```

Handler ` RVA 0x1ACF9740 `；selector ` 0 `；EOL ` RVA 0x36DCBFA0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bc60556e9da521b4](../../evidence/conditions-sets-073.md#c-bc60556e9da521b4)

### observed_connections-003728

```text
(config-perf-meas)# delay-profile sr-policy liveness-detection <cr>
```

Handler ` RVA 0x1ACF7870 `；selector ` 0 `；EOL ` RVA 0x36DD0AD0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2fff4e5560a73f26](../../evidence/conditions-sets-019.md#c-2fff4e5560a73f26)

### observed_connections-003821

```text
(config-perf-meas)# delay-profile sr-policy liveness-detection multiplier <number:2..10> <cr>
```

Handler ` RVA 0x1ACF9C40 `；selector ` 0 `；EOL ` RVA 0x36DD0838 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Detect Multiplier。

[条件 C-2fff4e5560a73f26](../../evidence/conditions-sets-019.md#c-2fff4e5560a73f26) · [参数 P-ba32c970d6d47746](../../evidence/parameters-sets-014.md#p-ba32c970d6d47746)

### observed_connections-003725

```text
(config-perf-meas)# delay-profile sr-policy probe <cr>
```

Handler ` RVA 0x1ACF75A0 `；selector ` 0 `；EOL ` RVA 0x36DD04C0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bc60556e9da521b4](../../evidence/conditions-sets-073.md#c-bc60556e9da521b4)

### observed_connections-003805

```text
(config-perf-meas)# delay-profile sr-policy probe burst-interval <number:30..15000> <cr>
```

Handler ` RVA 0x1ACF8B20 `；selector ` 0 `；EOL ` RVA 0x36DCE0A0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Burst interval (msec)。

[条件 C-bc60556e9da521b4](../../evidence/conditions-sets-073.md#c-bc60556e9da521b4) · [参数 P-e0e3f07438fe2b70](../../evidence/parameters-sets-017.md#p-e0e3f07438fe2b70)

### observed_connections-003823

```text
(config-perf-meas)# delay-profile sr-policy probe computation-interval <number:3..3600> <cr>
```

Handler ` RVA 0x1ACF84E0 `；selector ` 0 `；EOL ` RVA 0x36DCE3D0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Computation interval (seconds)。

[条件 C-b07e8095d7e5a931](../../evidence/conditions-sets-068.md#c-b07e8095d7e5a931) · [参数 P-83a40acd71f437c6](../../evidence/parameters-sets-010.md#p-83a40acd71f437c6)

### observed_connections-003845

```text
(config-perf-meas)# delay-profile sr-policy probe measurement-mode loopback <cr>
```

Handler ` RVA 0x1ACF88C0 `；selector ` 0 `；EOL ` RVA 0x36DCF2B8 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-adf7844092e5694c](../../evidence/conditions-sets-067.md#c-adf7844092e5694c)

### observed_connections-003840

```text
(config-perf-meas)# delay-profile sr-policy probe measurement-mode one-way <cr>
```

Handler ` RVA 0x1ACF8990 `；selector ` 0 `；EOL ` RVA 0x36DCED68 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-356dee1b0f10a12f](../../evidence/conditions-sets-021.md#c-356dee1b0f10a12f)

### observed_connections-003841

```text
(config-perf-meas)# delay-profile sr-policy probe measurement-mode two-way <cr>
```

Handler ` RVA 0x1ACF9B60 `；selector ` 0 `；EOL ` RVA 0x36DCF010 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-adf7844092e5694c](../../evidence/conditions-sets-067.md#c-adf7844092e5694c)

### observed_connections-003829

```text
(config-perf-meas)# delay-profile sr-policy probe padding-size <number:0..8000> <cr>
```

Handler ` RVA 0x1ACF8620 `；selector ` 0 `；EOL ` RVA 0x36DCE748 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Padding (bytes) to add to probes。

[条件 C-7fd6f1b4ba602c18](../../evidence/conditions-sets-050.md#c-7fd6f1b4ba602c18) · [参数 P-8b71d0a5c6717335](../../evidence/parameters-sets-011.md#p-8b71d0a5c6717335)

### observed_connections-003771

```text
(config-perf-meas)# delay-profile sr-policy probe protocol <cr>
```

Handler ` RVA 0x1ACF8A60 `；selector ` 0 `；EOL ` RVA 0x36DCFB58 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8b55d0da06b70929](../../evidence/conditions-sets-054.md#c-8b55d0da06b70929)

### observed_connections-003847

```text
(config-perf-meas)# delay-profile sr-policy probe protocol pm-mpls <cr>
```

Handler ` RVA 0x1ACF8E00 `；selector ` 0 `；EOL ` RVA 0x36DCF8C0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8b55d0da06b70929](../../evidence/conditions-sets-054.md#c-8b55d0da06b70929)

### observed_connections-003844

```text
(config-perf-meas)# delay-profile sr-policy probe protocol twamp-light <cr>
```

Handler ` RVA 0x1ACF8C90 `；selector ` 0 `；EOL ` RVA 0x36DCF618 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8b55d0da06b70929](../../evidence/conditions-sets-054.md#c-8b55d0da06b70929)

### observed_connections-003772

```text
(config-perf-meas)# delay-profile sr-policy probe sweep <cr>
```

Handler ` RVA 0x1ACF8F70 `；selector ` 0 `；EOL ` RVA 0x36DD0200 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8b55d0da06b70929](../../evidence/conditions-sets-054.md#c-8b55d0da06b70929)

### observed_connections-003995

```text
(config-perf-meas)# delay-profile sr-policy probe sweep destination ipv4 <address> range <number:0..128> <cr>
```

Handler ` RVA 0x1ACF9020 `；selector ` 0 `；EOL ` RVA 0x36DCFF50 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IPv4 address (Required to be a 127.0.0.0/8 address)；` unsigned_number ` Sweeping range (Should fully be in the 127.0.0.0/8 space)。

[条件 C-8b55d0da06b70929](../../evidence/conditions-sets-054.md#c-8b55d0da06b70929) · [参数 P-3dd866ae41e7e577](../../evidence/parameters-sets-005.md#p-3dd866ae41e7e577)

### observed_connections-003830

```text
(config-perf-meas)# delay-profile sr-policy probe tos-dscp <number:0..63> <cr>
```

Handler ` RVA 0x1ACF8740 `；selector ` 0 `；EOL ` RVA 0x36DCEA38 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` TOS DSCP。

[条件 C-8b55d0da06b70929](../../evidence/conditions-sets-054.md#c-8b55d0da06b70929) · [参数 P-e1cfa9d140cff418](../../evidence/parameters-sets-017.md#p-e1cfa9d140cff418)

### observed_connections-003741

```text
(config-perf-meas)# dual-color gre bit-position <number:9..12> <cr>
```

Handler ` RVA 0x1ACF3B10 `；selector ` 0 `；EOL ` RVA 0x36DD7F80 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` bit-position value。

[条件 C-e0f33479f97c1ab8](../../evidence/conditions-sets-087.md#c-e0f33479f97c1ab8) · [参数 P-e08eb5e7b4635707](../../evidence/parameters-sets-017.md#p-e08eb5e7b4635707)

### observed_connections-003699

```text
(config-perf-meas)# endpoint <string> <cr>
```

Handler ` RVA 0x1ACFA0B0 `；selector ` 0 `；EOL ` RVA 0x36DC3EB0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Endpoint Name。

[参数 P-214ba9e98f3de846](../../evidence/parameters-sets-003.md#p-214ba9e98f3de846)

### observed_connections-003702

```text
(config-perf-meas)# endpoint <string> delay-measurement <cr>
```

Handler ` RVA 0x1ACFA820 `；selector ` 0 `；EOL ` RVA 0x36DC2A30 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Endpoint Name。

[参数 P-214ba9e98f3de846](../../evidence/parameters-sets-003.md#p-214ba9e98f3de846)

### observed_connections-003774

```text
(config-perf-meas)# endpoint <string> delay-measurement profile <string> <cr>
```

Handler ` RVA 0x1ACFAA20 `；selector ` 0 `；EOL ` RVA 0x36DC27B0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Endpoint Name；` string ` Profile name。

[参数 P-4e504d294400b577](../../evidence/parameters-sets-006.md#p-4e504d294400b577)

### observed_connections-003773

```text
(config-perf-meas)# endpoint <string> destination-address ipv4 <address> <cr>
```

Handler ` RVA 0x1ACFA520 `；selector ` 0 `；EOL ` RVA 0x36DC23F0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Endpoint Name；` address ` IPv4 endpoint address。

[参数 P-02c0cdf85ff294f8](../../evidence/parameters-sets-001.md#p-02c0cdf85ff294f8)

### observed_connections-003716

```text
(config-perf-meas)# endpoint <string> segment-list <cr>
```

Handler ` RVA 0x1ACFA770 `；selector ` 0 `；EOL ` RVA 0x36DC3988 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Endpoint Name。

[参数 P-214ba9e98f3de846](../../evidence/parameters-sets-003.md#p-214ba9e98f3de846)

### observed_connections-003779

```text
(config-perf-meas)# endpoint <string> segment-list forward-path <string> <cr>
```

Handler ` RVA 0x1ACFAB50 `；selector ` 0 `；EOL ` RVA 0x36DC3420 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Endpoint Name；` string ` Identifying name for segment-list。

[参数 P-cfd0a0cac03a746e](../../evidence/parameters-sets-016.md#p-cfd0a0cac03a746e)

### observed_connections-003782

```text
(config-perf-meas)# endpoint <string> segment-list reverse-path <string> <cr>
```

Handler ` RVA 0x1ACFACB0 `；selector ` 0 `；EOL ` RVA 0x36DC3708 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Endpoint Name；` string ` Identifying name for reverse path segment-list。

[参数 P-fd63338fb07cefeb](../../evidence/parameters-sets-019.md#p-fd63338fb07cefeb)

### observed_connections-003703

```text
(config-perf-meas)# endpoint <string> shutdown <cr>
```

Handler ` RVA 0x1ACFA990 `；selector ` 0 `；EOL ` RVA 0x36DC3C08 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Endpoint Name。

[参数 P-214ba9e98f3de846](../../evidence/parameters-sets-003.md#p-214ba9e98f3de846)

### observed_connections-003775

```text
(config-perf-meas)# endpoint <string> source-address ipv4 <address> <cr>
```

Handler ` RVA 0x1ACFA400 `；selector ` 0 `；EOL ` RVA 0x36DC2D78 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Endpoint Name；` address ` IPv4 source address。

[参数 P-27a7405fba1b69b4](../../evidence/parameters-sets-003.md#p-27a7405fba1b69b4)

### observed_connections-003730

```text
(config-perf-meas)# endpoint <string> vrf <string> <cr>
```

Handler ` RVA 0x1ACFA640 `；selector ` 0 `；EOL ` RVA 0x36DC30D0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Endpoint Name；` string ` VRF Name。

[参数 P-6fc9a77829f84728](../../evidence/parameters-sets-009.md#p-6fc9a77829f84728)

### observed_connections-003692

```text
(config-perf-meas)# exit <cr>
```

Handler ` RVA 0x1ACF4A30 `；selector ` 0 `；EOL ` RVA 0x36DD8578 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-00a02443d55b8bd6](../../evidence/conditions-sets-001.md#c-00a02443d55b8bd6)

### observed_connections-004003

```text
(config-perf-meas)# interface <interface> <cr>
```

Handler ` RVA 0x1ACEF2B0 `；selector ` 0 `；EOL ` RVA 0x36DD5DA0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d60fcf71cb9e6816](../../evidence/conditions-sets-083.md#c-d60fcf71cb9e6816) · [缺口 G-5d5a1fd9de6ab334](../../evidence/gaps-sets-004.md#g-5d5a1fd9de6ab334) · [参数 P-b4fdd841ec67042e](../../evidence/parameters-sets-014.md#p-b4fdd841ec67042e) · [状态效果 S-e4dc0035c8ffaca9](../../evidence/state_effects-sets-048.md#s-e4dc0035c8ffaca9)

### observed_connections-004004

```text
(config-perf-meas)# interface <interface> delay-measurement <cr>
```

Handler ` RVA 0x1ACF29F0 `；selector ` 0 `；EOL ` RVA 0x36DD4DC0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d82f1cfaba3ccd05](../../evidence/conditions-sets-083.md#c-d82f1cfaba3ccd05) · [缺口 G-5d5a1fd9de6ab334](../../evidence/gaps-sets-004.md#g-5d5a1fd9de6ab334) · [参数 P-b4fdd841ec67042e](../../evidence/parameters-sets-014.md#p-b4fdd841ec67042e) · [状态效果 S-e4dc0035c8ffaca9](../../evidence/state_effects-sets-048.md#s-e4dc0035c8ffaca9)

### observed_connections-004006

```text
(config-perf-meas)# interface <interface> delay-measurement advertise-delay <number:0..16777214> <cr>
```

Handler ` RVA 0x1ACF2F90 `；selector ` 0 `；EOL ` RVA 0x36DD4850 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` advertisement delay (uSec)。

[条件 C-d82f1cfaba3ccd05](../../evidence/conditions-sets-083.md#c-d82f1cfaba3ccd05) · [缺口 G-5d5a1fd9de6ab334](../../evidence/gaps-sets-004.md#g-5d5a1fd9de6ab334) · [参数 P-9ac8e57ed4221f43](../../evidence/parameters-sets-012.md#p-9ac8e57ed4221f43) · [状态效果 S-e4dc0035c8ffaca9](../../evidence/state_effects-sets-048.md#s-e4dc0035c8ffaca9)

### observed_connections-004008

```text
(config-perf-meas)# interface <interface> delay-measurement profile <string> <cr>
```

Handler ` RVA 0x1ACF30B0 `；selector ` 0 `；EOL ` RVA 0x36DD4B40 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Profile Name。

[条件 C-d82f1cfaba3ccd05](../../evidence/conditions-sets-083.md#c-d82f1cfaba3ccd05) · [缺口 G-5d5a1fd9de6ab334](../../evidence/gaps-sets-004.md#g-5d5a1fd9de6ab334) · [参数 P-8fd70458ab202502](../../evidence/parameters-sets-011.md#p-8fd70458ab202502) · [状态效果 S-e4dc0035c8ffaca9](../../evidence/state_effects-sets-048.md#s-e4dc0035c8ffaca9)

### observed_connections-004005

```text
(config-perf-meas)# interface <interface> loss-measurement <cr>
```

Handler ` RVA 0x1ACF28B0 `；selector ` 0 `；EOL ` RVA 0x36DD5B20 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4a8019719dad5022](../../evidence/conditions-sets-029.md#c-4a8019719dad5022) · [缺口 G-5d5a1fd9de6ab334](../../evidence/gaps-sets-004.md#g-5d5a1fd9de6ab334) · [参数 P-b4fdd841ec67042e](../../evidence/parameters-sets-014.md#p-b4fdd841ec67042e) · [状态效果 S-e4dc0035c8ffaca9](../../evidence/state_effects-sets-048.md#s-e4dc0035c8ffaca9)

### observed_connections-004010

```text
(config-perf-meas)# interface <interface> loss-measurement advertise-loss <?fixed_number_action@55558c3294a8> <cr>
```

Handler ` RVA 0x1ACF2C80 `；selector ` 0 `；EOL ` RVA 0x36DD5560 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4a8019719dad5022](../../evidence/conditions-sets-029.md#c-4a8019719dad5022) · [缺口 G-f9e1f8637097a92b](../../evidence/gaps-sets-009.md#g-f9e1f8637097a92b) · [参数 P-b4fdd841ec67042e](../../evidence/parameters-sets-014.md#p-b4fdd841ec67042e) · [状态效果 S-6571193fd6bfc52d](../../evidence/state_effects-sets-022.md#s-6571193fd6bfc52d)

### observed_connections-004009

```text
(config-perf-meas)# interface <interface> loss-measurement profile <string> <cr>
```

Handler ` RVA 0x1ACF2E70 `；selector ` 0 `；EOL ` RVA 0x36DD58A0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Profile Name。

[条件 C-4a8019719dad5022](../../evidence/conditions-sets-029.md#c-4a8019719dad5022) · [缺口 G-5d5a1fd9de6ab334](../../evidence/gaps-sets-004.md#g-5d5a1fd9de6ab334) · [参数 P-b10e2eb5a7a92b3a](../../evidence/parameters-sets-013.md#p-b10e2eb5a7a92b3a) · [状态效果 S-e4dc0035c8ffaca9](../../evidence/state_effects-sets-048.md#s-e4dc0035c8ffaca9)

### observed_connections-004007

```text
(config-perf-meas)# interface <interface> next-hop ipv4 <address> <cr>
```

Handler ` RVA 0x1ACF4200 `；selector ` 0 `；EOL ` RVA 0x36DD5110 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` IPv4 address。

[条件 C-d82f1cfaba3ccd05](../../evidence/conditions-sets-083.md#c-d82f1cfaba3ccd05) · [缺口 G-5d5a1fd9de6ab334](../../evidence/gaps-sets-004.md#g-5d5a1fd9de6ab334) · [参数 P-9f505a8bbc96c3e4](../../evidence/parameters-sets-012.md#p-9f505a8bbc96c3e4) · [状态效果 S-e4dc0035c8ffaca9](../../evidence/state_effects-sets-048.md#s-e4dc0035c8ffaca9)

### observed_connections-003695

```text
(config-perf-meas)# loss-profile interfaces <cr>
```

Handler ` RVA 0x1ACEF800 `；selector ` 0 `；EOL ` RVA 0x36DC6DA8 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-606b89fe7872f8c5](../../evidence/conditions-sets-037.md#c-606b89fe7872f8c5)

### observed_connections-003708

```text
(config-perf-meas)# loss-profile interfaces advertisement <cr>
```

Handler ` RVA 0x1ACEFAF0 `；selector ` 0 `；EOL ` RVA 0x36DC5670 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-606b89fe7872f8c5](../../evidence/conditions-sets-037.md#c-606b89fe7872f8c5)

### observed_connections-003744

```text
(config-perf-meas)# loss-profile interfaces advertisement anomaly-check <cr>
```

Handler ` RVA 0x1ACEFE40 `；selector ` 0 `；EOL ` RVA 0x36DC5010 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-606b89fe7872f8c5](../../evidence/conditions-sets-037.md#c-606b89fe7872f8c5)

### observed_connections-004001

```text
(config-perf-meas)# loss-profile interfaces advertisement anomaly-check lower-bound <?fixed_number_action@55558c319278> <cr>
```

Handler ` RVA 0x1ACF0FC0 `；selector ` 0 `；EOL ` RVA 0x36DC5340 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7a1d40baaef7bca0](../../evidence/conditions-sets-047.md#c-7a1d40baaef7bca0) · [缺口 G-130b4b6e18f5e19b](../../evidence/gaps-sets-001.md#g-130b4b6e18f5e19b) · [状态效果 S-c580c67c997b0624](../../evidence/state_effects-sets-042.md#s-c580c67c997b0624)

### observed_connections-003737

```text
(config-perf-meas)# loss-profile interfaces advertisement periodic <cr>
```

Handler ` RVA 0x1ACEFD90 `；selector ` 0 `；EOL ` RVA 0x36DC4CB8 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-606b89fe7872f8c5](../../evidence/conditions-sets-037.md#c-606b89fe7872f8c5)

### observed_connections-003858

```text
(config-perf-meas)# loss-profile interfaces advertisement periodic interval <number:30..3600> <cr>
```

Handler ` RVA 0x1ACF01C0 `；selector ` 0 `；EOL ` RVA 0x36DC4400 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` interval value in sec。

[条件 C-606b89fe7872f8c5](../../evidence/conditions-sets-037.md#c-606b89fe7872f8c5) · [参数 P-22673dbf4dd5bf85](../../evidence/parameters-sets-003.md#p-22673dbf4dd5bf85)

### observed_connections-004000

```text
(config-perf-meas)# loss-profile interfaces advertisement periodic minimum-change <?fixed_number_action@55558c3189d0> <cr>
```

Handler ` RVA 0x1ACEFEE0 `；selector ` 0 `；EOL ` RVA 0x36DC4A10 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-606b89fe7872f8c5](../../evidence/conditions-sets-037.md#c-606b89fe7872f8c5) · [缺口 G-a015f8c397cac157](../../evidence/gaps-sets-006.md#g-a015f8c397cac157)

### observed_connections-003999

```text
(config-perf-meas)# loss-profile interfaces advertisement periodic threshold <?fixed_number_action@55558c3186d8> <cr>
```

Handler ` RVA 0x1ACF0050 `；selector ` 0 `；EOL ` RVA 0x36DC4740 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-606b89fe7872f8c5](../../evidence/conditions-sets-037.md#c-606b89fe7872f8c5) · [缺口 G-d23069531a7cddcc](../../evidence/gaps-sets-007.md#g-d23069531a7cddcc)

### observed_connections-003722

```text
(config-perf-meas)# loss-profile interfaces probe <cr>
```

Handler ` RVA 0x1ACEFC30 `；selector ` 0 `；EOL ` RVA 0x36DC6B18 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-606b89fe7872f8c5](../../evidence/conditions-sets-037.md#c-606b89fe7872f8c5)

### observed_connections-003755

```text
(config-perf-meas)# loss-profile interfaces probe color-type <cr>
```

Handler ` RVA 0x1ACF0550 `；selector ` 0 `；EOL ` RVA 0x36DC65A8 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-606b89fe7872f8c5](../../evidence/conditions-sets-037.md#c-606b89fe7872f8c5)

### observed_connections-003876

```text
(config-perf-meas)# loss-profile interfaces probe color-type dual-color gre <cr>
```

Handler ` RVA 0x1ACF0B20 `；selector ` 0 `；EOL ` RVA 0x36DC6318 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-606b89fe7872f8c5](../../evidence/conditions-sets-037.md#c-606b89fe7872f8c5)

### observed_connections-003810

```text
(config-perf-meas)# loss-profile interfaces probe color-type single-color <cr>
```

Handler ` RVA 0x1ACF0700 `；selector ` 0 `；EOL ` RVA 0x36DC6030 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-606b89fe7872f8c5](../../evidence/conditions-sets-037.md#c-606b89fe7872f8c5)

### observed_connections-004002

```text
(config-perf-meas)# loss-profile interfaces probe color-type single-color accuracy <?fixed_number_action@55558c319a48> <cr>
```

Handler ` RVA 0x1ACF08C0 `；selector ` 0 `；EOL ` RVA 0x36DC5AB0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-606b89fe7872f8c5](../../evidence/conditions-sets-037.md#c-606b89fe7872f8c5) · [缺口 G-79e3bbafef882390](../../evidence/gaps-sets-005.md#g-79e3bbafef882390)

### observed_connections-003963

```text
(config-perf-meas)# loss-profile interfaces probe color-type single-color max-reordering <number:100..2000> <cr>
```

Handler ` RVA 0x1ACF0A10 `；selector ` 0 `；EOL ` RVA 0x36DC5DA8 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` maximum expected reordering value in miliseconds。

[条件 C-606b89fe7872f8c5](../../evidence/conditions-sets-037.md#c-606b89fe7872f8c5) · [参数 P-59fd1598f3c3c6cd](../../evidence/parameters-sets-007.md#p-59fd1598f3c3c6cd)

### observed_connections-003786

```text
(config-perf-meas)# loss-profile interfaces probe tx-interval <number:10..1000> <cr>
```

Handler ` RVA 0x1ACF05F0 `；selector ` 0 `；EOL ` RVA 0x36DC6890 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Transmit interval value in sec。

[条件 C-606b89fe7872f8c5](../../evidence/conditions-sets-037.md#c-606b89fe7872f8c5) · [参数 P-1741a8166c9b6621](../../evidence/parameters-sets-002.md#p-1741a8166c9b6621)

### observed_connections-003998

```text
(config-perf-meas)# max-pps <number:dynamic> <cr>
```

Handler ` RVA 0x1ACEF770 `；selector ` 0 `；EOL ` RVA 0x36DD7BD0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` packets-per-second。

[条件 C-46d366f528489dea](../../evidence/conditions-sets-028.md#c-46d366f528489dea) · [缺口 G-490c04eaafc957e2](../../evidence/gaps-sets-003.md#g-490c04eaafc957e2) · [参数 P-44da61e6d3a30498](../../evidence/parameters-sets-006.md#p-44da61e6d3a30498)

### observed_connections-003693

```text
(config-perf-meas)# no <cr>
```

Handler ` RVA 0x1ACEEE70 `；selector ` 0 `；EOL ` RVA 0x36DD8220 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-16edb078860859dd](../../evidence/conditions-sets-009.md#c-16edb078860859dd) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003705

```text
(config-perf-meas)# no delay-profile endpoint <cr>
```

Handler ` RVA 0x1ACF9DE0 `；selector ` 0 `；EOL ` RVA 0x36DCB5B0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c1637be6fab92cfb](../../evidence/conditions-sets-075.md#c-c1637be6fab92cfb) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003735

```text
(config-perf-meas)# no delay-profile endpoint advertisement <cr>
```

Handler ` RVA 0x1ACFAE10 `；selector ` 0 `；EOL ` RVA 0x36DC94E8 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c1637be6fab92cfb](../../evidence/conditions-sets-075.md#c-c1637be6fab92cfb) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003803

```text
(config-perf-meas)# no delay-profile endpoint advertisement accelerated <cr>
```

Handler ` RVA 0x1ACFB3D0 `；selector ` 0 `；EOL ` RVA 0x36DC83D8 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c1637be6fab92cfb](../../evidence/conditions-sets-075.md#c-c1637be6fab92cfb) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003955

```text
(config-perf-meas)# no delay-profile endpoint advertisement accelerated minimum-change <number:0..1000000> <cr>
```

Handler ` RVA 0x1ACFB890 `；selector ` 0 `；EOL ` RVA 0x36DC7E28 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Accelerated advertisement minimum change (uSec)。

[条件 C-c1637be6fab92cfb](../../evidence/conditions-sets-075.md#c-c1637be6fab92cfb) · [参数 P-9f6f6ba2d130deb9](../../evidence/parameters-sets-012.md#p-9f6f6ba2d130deb9) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003966

```text
(config-perf-meas)# no delay-profile endpoint advertisement accelerated threshold <number:0..100> <cr>
```

Handler ` RVA 0x1ACFB760 `；selector ` 0 `；EOL ` RVA 0x36DC8140 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Accelerated advertisement threshold percentage change。

[条件 C-c1637be6fab92cfb](../../evidence/conditions-sets-075.md#c-c1637be6fab92cfb) · [参数 P-2bf284102dc3b5f7](../../evidence/parameters-sets-004.md#p-2bf284102dc3b5f7) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003814

```text
(config-perf-meas)# no delay-profile endpoint advertisement periodic <cr>
```

Handler ` RVA 0x1ACFB520 `；selector ` 0 `；EOL ` RVA 0x36DC9258 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c1637be6fab92cfb](../../evidence/conditions-sets-075.md#c-c1637be6fab92cfb) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003913

```text
(config-perf-meas)# no delay-profile endpoint advertisement periodic disabled <cr>
```

Handler ` RVA 0x1ACFB9C0 `；selector ` 0 `；EOL ` RVA 0x36DC8FB0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c1637be6fab92cfb](../../evidence/conditions-sets-075.md#c-c1637be6fab92cfb) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003979

```text
(config-perf-meas)# no delay-profile endpoint advertisement periodic interval <number:30..3600> <cr>
```

Handler ` RVA 0x1ACFBA60 `；selector ` 0 `；EOL ` RVA 0x36DC8D28 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number `  Periodic advertisement interval (seconds)。

[条件 C-c1637be6fab92cfb](../../evidence/conditions-sets-075.md#c-c1637be6fab92cfb) · [参数 P-9239b3dae0fed22a](../../evidence/parameters-sets-011.md#p-9239b3dae0fed22a) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003958

```text
(config-perf-meas)# no delay-profile endpoint advertisement periodic minimum-change <number:0..1000000> <cr>
```

Handler ` RVA 0x1ACFBD00 `；selector ` 0 `；EOL ` RVA 0x36DC86F8 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Periodic advertisement minimum change (uSec)。

[条件 C-c1637be6fab92cfb](../../evidence/conditions-sets-075.md#c-c1637be6fab92cfb) · [参数 P-ca7c92d34181e004](../../evidence/parameters-sets-015.md#p-ca7c92d34181e004) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003972

```text
(config-perf-meas)# no delay-profile endpoint advertisement periodic threshold <number:0..100> <cr>
```

Handler ` RVA 0x1ACFBB50 `；selector ` 0 `；EOL ` RVA 0x36DC8A38 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Periodic advertisement threshold percentage change。

[条件 C-c1637be6fab92cfb](../../evidence/conditions-sets-075.md#c-c1637be6fab92cfb) · [参数 P-0f8747ef381467d2](../../evidence/parameters-sets-002.md#p-0f8747ef381467d2) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003793

```text
(config-perf-meas)# no delay-profile endpoint advertisement threshold-check <cr>
```

Handler ` RVA 0x1ACFB6B0 `；selector ` 0 `；EOL ` RVA 0x36DC7A78 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c1637be6fab92cfb](../../evidence/conditions-sets-075.md#c-c1637be6fab92cfb) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003856

```text
(config-perf-meas)# no delay-profile endpoint advertisement threshold-check average-delay <cr>
```

Handler ` RVA 0x1ACFCC80 `；selector ` 0 `；EOL ` RVA 0x36DC7280 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c1637be6fab92cfb](../../evidence/conditions-sets-075.md#c-c1637be6fab92cfb) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003861

```text
(config-perf-meas)# no delay-profile endpoint advertisement threshold-check maximum-delay <cr>
```

Handler ` RVA 0x1ACFCB30 `；selector ` 0 `；EOL ` RVA 0x36DC7528 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c1637be6fab92cfb](../../evidence/conditions-sets-075.md#c-c1637be6fab92cfb) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003866

```text
(config-perf-meas)# no delay-profile endpoint advertisement threshold-check minimum-delay <cr>
```

Handler ` RVA 0x1ACFC9E0 `；selector ` 0 `；EOL ` RVA 0x36DC77D0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c1637be6fab92cfb](../../evidence/conditions-sets-075.md#c-c1637be6fab92cfb) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003753

```text
(config-perf-meas)# no delay-profile endpoint liveness-detection <cr>
```

Handler ` RVA 0x1ACFB2C0 `；selector ` 0 `；EOL ` RVA 0x36DCB330 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-97664056404981c7](../../evidence/conditions-sets-058.md#c-97664056404981c7) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003887

```text
(config-perf-meas)# no delay-profile endpoint liveness-detection multiplier <number:2..10> <cr>
```

Handler ` RVA 0x1ACFCEA0 `；selector ` 0 `；EOL ` RVA 0x36DCB098 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Detect Multiplier。

[条件 C-97664056404981c7](../../evidence/conditions-sets-058.md#c-97664056404981c7) · [参数 P-832a3c41773baa51](../../evidence/parameters-sets-010.md#p-832a3c41773baa51) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003736

```text
(config-perf-meas)# no delay-profile endpoint probe <cr>
```

Handler ` RVA 0x1ACFB040 `；selector ` 0 `；EOL ` RVA 0x36DCAD20 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c1637be6fab92cfb](../../evidence/conditions-sets-075.md#c-c1637be6fab92cfb) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003871

```text
(config-perf-meas)# no delay-profile endpoint probe burst-interval <number:30..15000> <cr>
```

Handler ` RVA 0x1ACFC440 `；selector ` 0 `；EOL ` RVA 0x36DC98D0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Burst interval (msec)。

[条件 C-c1637be6fab92cfb](../../evidence/conditions-sets-075.md#c-c1637be6fab92cfb) · [参数 P-f4437d88dc812964](../../evidence/parameters-sets-018.md#p-f4437d88dc812964) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003891

```text
(config-perf-meas)# no delay-profile endpoint probe computation-interval <number:3..3600> <cr>
```

Handler ` RVA 0x1ACFC0E0 `；selector ` 0 `；EOL ` RVA 0x36DC9C00 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Computation interval (seconds)。

[条件 C-0b907c9f8f450fdb](../../evidence/conditions-sets-005.md#c-0b907c9f8f450fdb) · [参数 P-d09a80bed29e4458](../../evidence/parameters-sets-016.md#p-d09a80bed29e4458) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003934

```text
(config-perf-meas)# no delay-profile endpoint probe measurement-mode loopback <cr>
```

Handler ` RVA 0x1ACFC2A0 `；selector ` 0 `；EOL ` RVA 0x36DCAA40 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c1637be6fab92cfb](../../evidence/conditions-sets-075.md#c-c1637be6fab92cfb) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003910

```text
(config-perf-meas)# no delay-profile endpoint probe measurement-mode one-way <cr>
```

Handler ` RVA 0x1ACFC370 `；selector ` 0 `；EOL ` RVA 0x36DCA4F0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c1637be6fab92cfb](../../evidence/conditions-sets-075.md#c-c1637be6fab92cfb) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003924

```text
(config-perf-meas)# no delay-profile endpoint probe measurement-mode two-way <cr>
```

Handler ` RVA 0x1ACFCDE0 `；selector ` 0 `；EOL ` RVA 0x36DCA798 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c1637be6fab92cfb](../../evidence/conditions-sets-075.md#c-c1637be6fab92cfb) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003890

```text
(config-perf-meas)# no delay-profile endpoint probe padding-size <number:0..8000> <cr>
```

Handler ` RVA 0x1ACFBEC0 `；selector ` 0 `；EOL ` RVA 0x36DC9F38 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Padding (bytes) to add to probes。

[条件 C-c1637be6fab92cfb](../../evidence/conditions-sets-075.md#c-c1637be6fab92cfb) · [参数 P-0f90b03d9cc18eae](../../evidence/parameters-sets-002.md#p-0f90b03d9cc18eae) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003902

```text
(config-perf-meas)# no delay-profile endpoint probe tos-dscp <number:0..63> <cr>
```

Handler ` RVA 0x1ACFBFE0 `；selector ` 0 `；EOL ` RVA 0x36DCA228 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` TOS DSCP。

[条件 C-c1637be6fab92cfb](../../evidence/conditions-sets-075.md#c-c1637be6fab92cfb) · [参数 P-1395f8a7ed87e3f7](../../evidence/parameters-sets-002.md#p-1395f8a7ed87e3f7) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003718

```text
(config-perf-meas)# no delay-profile interfaces <cr>
```

Handler ` RVA 0x1ACEF410 `；selector ` 0 `；EOL ` RVA 0x36DD4378 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-41295089077dc321](../../evidence/conditions-sets-025.md#c-41295089077dc321) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003747

```text
(config-perf-meas)# no delay-profile interfaces advertisement <cr>
```

Handler ` RVA 0x1ACF12B0 `；selector ` 0 `；EOL ` RVA 0x36DD28F0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-41295089077dc321](../../evidence/conditions-sets-025.md#c-41295089077dc321) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003801

```text
(config-perf-meas)# no delay-profile interfaces advertisement accelerated <cr>
```

Handler ` RVA 0x1ACF1600 `；selector ` 0 `；EOL ` RVA 0x36DD17A0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-41295089077dc321](../../evidence/conditions-sets-025.md#c-41295089077dc321) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003954

```text
(config-perf-meas)# no delay-profile interfaces advertisement accelerated minimum-change <number:0..1000000> <cr>
```

Handler ` RVA 0x1ACF1BE0 `；selector ` 0 `；EOL ` RVA 0x36DD11F0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Accelerated advertisement minimum change (uSec)。

[条件 C-41295089077dc321](../../evidence/conditions-sets-025.md#c-41295089077dc321) · [参数 P-87f9628a76ee7742](../../evidence/parameters-sets-010.md#p-87f9628a76ee7742) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003965

```text
(config-perf-meas)# no delay-profile interfaces advertisement accelerated threshold <number:0..100> <cr>
```

Handler ` RVA 0x1ACF1AB0 `；selector ` 0 `；EOL ` RVA 0x36DD1508 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Accelerated advertisement threshold percentage change。

[条件 C-41295089077dc321](../../evidence/conditions-sets-025.md#c-41295089077dc321) · [参数 P-f0ea66ce03e923ef](../../evidence/parameters-sets-018.md#p-f0ea66ce03e923ef) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003818

```text
(config-perf-meas)# no delay-profile interfaces advertisement periodic <cr>
```

Handler ` RVA 0x1ACF1830 `；selector ` 0 `；EOL ` RVA 0x36DD2670 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-41295089077dc321](../../evidence/conditions-sets-025.md#c-41295089077dc321) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003925

```text
(config-perf-meas)# no delay-profile interfaces advertisement periodic disabled <cr>
```

Handler ` RVA 0x1ACF1D10 `；selector ` 0 `；EOL ` RVA 0x36DD23C8 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-41295089077dc321](../../evidence/conditions-sets-025.md#c-41295089077dc321) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003983

```text
(config-perf-meas)# no delay-profile interfaces advertisement periodic interval <number:30..3600> <cr>
```

Handler ` RVA 0x1ACF1DB0 `；selector ` 0 `；EOL ` RVA 0x36DD2140 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number `  Periodic advertisement interval (seconds)。

[条件 C-41295089077dc321](../../evidence/conditions-sets-025.md#c-41295089077dc321) · [参数 P-7083362af6595dd1](../../evidence/parameters-sets-009.md#p-7083362af6595dd1) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003961

```text
(config-perf-meas)# no delay-profile interfaces advertisement periodic minimum-change <number:0..1000000> <cr>
```

Handler ` RVA 0x1ACF2050 `；selector ` 0 `；EOL ` RVA 0x36DD1B10 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Periodic advertisement minimum change (uSec)。

[条件 C-41295089077dc321](../../evidence/conditions-sets-025.md#c-41295089077dc321) · [参数 P-a9f06d097ad720d7](../../evidence/parameters-sets-013.md#p-a9f06d097ad720d7) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003977

```text
(config-perf-meas)# no delay-profile interfaces advertisement periodic threshold <number:0..100> <cr>
```

Handler ` RVA 0x1ACF1EA0 `；selector ` 0 `；EOL ` RVA 0x36DD1E50 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Periodic advertisement threshold percentage change。

[条件 C-41295089077dc321](../../evidence/conditions-sets-025.md#c-41295089077dc321) · [参数 P-870c791c38909c22](../../evidence/parameters-sets-010.md#p-870c791c38909c22) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003752

```text
(config-perf-meas)# no delay-profile interfaces probe <cr>
```

Handler ` RVA 0x1ACF1390 `；selector ` 0 `；EOL ` RVA 0x36DD4100 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-41295089077dc321](../../evidence/conditions-sets-025.md#c-41295089077dc321) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003886

```text
(config-perf-meas)# no delay-profile interfaces probe burst-interval <number:30..15000> <cr>
```

Handler ` RVA 0x1ACF2620 `；selector ` 0 `；EOL ` RVA 0x36DD2CB0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Burst interval (msec)。

[条件 C-41295089077dc321](../../evidence/conditions-sets-025.md#c-41295089077dc321) · [参数 P-03cdf0ceed35889a](../../evidence/parameters-sets-001.md#p-03cdf0ceed35889a) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003912

```text
(config-perf-meas)# no delay-profile interfaces probe computation-interval <number:3..3600> <cr>
```

Handler ` RVA 0x1ACF2200 `；selector ` 0 `；EOL ` RVA 0x36DD2FE0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Computation interval (seconds)。

[条件 C-0de0fccfc6b61de9](../../evidence/conditions-sets-006.md#c-0de0fccfc6b61de9) · [参数 P-539c95aaebc2a4a7](../../evidence/parameters-sets-007.md#p-539c95aaebc2a4a7) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003922

```text
(config-perf-meas)# no delay-profile interfaces probe measurement-mode one-way <cr>
```

Handler ` RVA 0x1ACF23D0 `；selector ` 0 `；EOL ` RVA 0x36DD3358 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-04fe53a4531f50fe](../../evidence/conditions-sets-002.md#c-04fe53a4531f50fe) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003923

```text
(config-perf-meas)# no delay-profile interfaces probe measurement-mode two-way <cr>
```

Handler ` RVA 0x1ACF4AA0 `；selector ` 0 `；EOL ` RVA 0x36DD3600 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7abfd7972d30e72c](../../evidence/conditions-sets-048.md#c-7abfd7972d30e72c) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003839

```text
(config-perf-meas)# no delay-profile interfaces probe protocol <cr>
```

Handler ` RVA 0x1ACF2470 `；selector ` 0 `；EOL ` RVA 0x36DD3E68 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-41295089077dc321](../../evidence/conditions-sets-025.md#c-41295089077dc321) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003940

```text
(config-perf-meas)# no delay-profile interfaces probe protocol pm-mpls <cr>
```

Handler ` RVA 0x1ACF46B0 `；selector ` 0 `；EOL ` RVA 0x36DD3BD0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-41295089077dc321](../../evidence/conditions-sets-025.md#c-41295089077dc321) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003932

```text
(config-perf-meas)# no delay-profile interfaces probe protocol twamp-light <cr>
```

Handler ` RVA 0x1ACF45A0 `；selector ` 0 `；EOL ` RVA 0x36DD3928 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-41295089077dc321](../../evidence/conditions-sets-025.md#c-41295089077dc321) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003717

```text
(config-perf-meas)# no delay-profile sr-policy <cr>
```

Handler ` RVA 0x1ACF7130 `；selector ` 0 `；EOL ` RVA 0x36DD0D50 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-bc60556e9da521b4](../../evidence/conditions-sets-073.md#c-bc60556e9da521b4) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003746

```text
(config-perf-meas)# no delay-profile sr-policy advertisement <cr>
```

Handler ` RVA 0x1ACF7470 `；selector ` 0 `；EOL ` RVA 0x36DCDCB8 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-bc60556e9da521b4](../../evidence/conditions-sets-073.md#c-bc60556e9da521b4) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003817

```text
(config-perf-meas)# no delay-profile sr-policy advertisement accelerated <cr>
```

Handler ` RVA 0x1ACF7990 `；selector ` 0 `；EOL ` RVA 0x36DCCBA8 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-bc60556e9da521b4](../../evidence/conditions-sets-073.md#c-bc60556e9da521b4) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003960

```text
(config-perf-meas)# no delay-profile sr-policy advertisement accelerated minimum-change <number:0..1000000> <cr>
```

Handler ` RVA 0x1ACF7EB0 `；selector ` 0 `；EOL ` RVA 0x36DCC5F8 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Accelerated advertisement minimum change (uSec)。

[条件 C-bc60556e9da521b4](../../evidence/conditions-sets-073.md#c-bc60556e9da521b4) · [参数 P-4895a79d21238df7](../../evidence/parameters-sets-006.md#p-4895a79d21238df7) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003976

```text
(config-perf-meas)# no delay-profile sr-policy advertisement accelerated threshold <number:0..100> <cr>
```

Handler ` RVA 0x1ACF7D80 `；selector ` 0 `；EOL ` RVA 0x36DCC910 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Accelerated advertisement threshold percentage change。

[条件 C-bc60556e9da521b4](../../evidence/conditions-sets-073.md#c-bc60556e9da521b4) · [参数 P-812a14f19936cf48](../../evidence/parameters-sets-010.md#p-812a14f19936cf48) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003828

```text
(config-perf-meas)# no delay-profile sr-policy advertisement periodic <cr>
```

Handler ` RVA 0x1ACF7B10 `；selector ` 0 `；EOL ` RVA 0x36DCDA28 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-bc60556e9da521b4](../../evidence/conditions-sets-073.md#c-bc60556e9da521b4) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003936

```text
(config-perf-meas)# no delay-profile sr-policy advertisement periodic disabled <cr>
```

Handler ` RVA 0x1ACF7FE0 `；selector ` 0 `；EOL ` RVA 0x36DCD780 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-bc60556e9da521b4](../../evidence/conditions-sets-073.md#c-bc60556e9da521b4) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003987

```text
(config-perf-meas)# no delay-profile sr-policy advertisement periodic interval <number:30..3600> <cr>
```

Handler ` RVA 0x1ACF8080 `；selector ` 0 `；EOL ` RVA 0x36DCD4F8 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number `  Periodic advertisement interval (seconds)。

[条件 C-bc60556e9da521b4](../../evidence/conditions-sets-073.md#c-bc60556e9da521b4) · [参数 P-70306a4f9901803d](../../evidence/parameters-sets-009.md#p-70306a4f9901803d) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003969

```text
(config-perf-meas)# no delay-profile sr-policy advertisement periodic minimum-change <number:0..1000000> <cr>
```

Handler ` RVA 0x1ACF8320 `；selector ` 0 `；EOL ` RVA 0x36DCCEC8 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Periodic advertisement minimum change (uSec)。

[条件 C-bc60556e9da521b4](../../evidence/conditions-sets-073.md#c-bc60556e9da521b4) · [参数 P-ebd32062bdb101ca](../../evidence/parameters-sets-018.md#p-ebd32062bdb101ca) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003982

```text
(config-perf-meas)# no delay-profile sr-policy advertisement periodic threshold <number:0..100> <cr>
```

Handler ` RVA 0x1ACF8170 `；selector ` 0 `；EOL ` RVA 0x36DCD208 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Periodic advertisement threshold percentage change。

[条件 C-bc60556e9da521b4](../../evidence/conditions-sets-073.md#c-bc60556e9da521b4) · [参数 P-c357520640169781](../../evidence/parameters-sets-015.md#p-c357520640169781) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003815

```text
(config-perf-meas)# no delay-profile sr-policy advertisement threshold-check <cr>
```

Handler ` RVA 0x1ACF7CB0 `；selector ` 0 `；EOL ` RVA 0x36DCC248 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-bc60556e9da521b4](../../evidence/conditions-sets-073.md#c-bc60556e9da521b4) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003862

```text
(config-perf-meas)# no delay-profile sr-policy advertisement threshold-check average-delay <cr>
```

Handler ` RVA 0x1ACF9A00 `；selector ` 0 `；EOL ` RVA 0x36DCBA50 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-bc60556e9da521b4](../../evidence/conditions-sets-073.md#c-bc60556e9da521b4) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003873

```text
(config-perf-meas)# no delay-profile sr-policy advertisement threshold-check maximum-delay <cr>
```

Handler ` RVA 0x1ACF98A0 `；selector ` 0 `；EOL ` RVA 0x36DCBCF8 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-bc60556e9da521b4](../../evidence/conditions-sets-073.md#c-bc60556e9da521b4) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003880

```text
(config-perf-meas)# no delay-profile sr-policy advertisement threshold-check minimum-delay <cr>
```

Handler ` RVA 0x1ACF9740 `；selector ` 0 `；EOL ` RVA 0x36DCBFA0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-bc60556e9da521b4](../../evidence/conditions-sets-073.md#c-bc60556e9da521b4) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003765

```text
(config-perf-meas)# no delay-profile sr-policy liveness-detection <cr>
```

Handler ` RVA 0x1ACF7870 `；selector ` 0 `；EOL ` RVA 0x36DD0AD0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-2fff4e5560a73f26](../../evidence/conditions-sets-019.md#c-2fff4e5560a73f26) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003905

```text
(config-perf-meas)# no delay-profile sr-policy liveness-detection multiplier <number:2..10> <cr>
```

Handler ` RVA 0x1ACF9C40 `；selector ` 0 `；EOL ` RVA 0x36DD0838 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Detect Multiplier。

[条件 C-2fff4e5560a73f26](../../evidence/conditions-sets-019.md#c-2fff4e5560a73f26) · [参数 P-ba32c970d6d47746](../../evidence/parameters-sets-014.md#p-ba32c970d6d47746) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003751

```text
(config-perf-meas)# no delay-profile sr-policy probe <cr>
```

Handler ` RVA 0x1ACF75A0 `；selector ` 0 `；EOL ` RVA 0x36DD04C0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-bc60556e9da521b4](../../evidence/conditions-sets-073.md#c-bc60556e9da521b4) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003885

```text
(config-perf-meas)# no delay-profile sr-policy probe burst-interval <number:30..15000> <cr>
```

Handler ` RVA 0x1ACF8B20 `；selector ` 0 `；EOL ` RVA 0x36DCE0A0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Burst interval (msec)。

[条件 C-bc60556e9da521b4](../../evidence/conditions-sets-073.md#c-bc60556e9da521b4) · [参数 P-e0e3f07438fe2b70](../../evidence/parameters-sets-017.md#p-e0e3f07438fe2b70) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003911

```text
(config-perf-meas)# no delay-profile sr-policy probe computation-interval <number:3..3600> <cr>
```

Handler ` RVA 0x1ACF84E0 `；selector ` 0 `；EOL ` RVA 0x36DCE3D0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Computation interval (seconds)。

[条件 C-b07e8095d7e5a931](../../evidence/conditions-sets-068.md#c-b07e8095d7e5a931) · [参数 P-83a40acd71f437c6](../../evidence/parameters-sets-010.md#p-83a40acd71f437c6) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003947

```text
(config-perf-meas)# no delay-profile sr-policy probe measurement-mode loopback <cr>
```

Handler ` RVA 0x1ACF88C0 `；selector ` 0 `；EOL ` RVA 0x36DCF2B8 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-adf7844092e5694c](../../evidence/conditions-sets-067.md#c-adf7844092e5694c) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003938

```text
(config-perf-meas)# no delay-profile sr-policy probe measurement-mode one-way <cr>
```

Handler ` RVA 0x1ACF8990 `；selector ` 0 `；EOL ` RVA 0x36DCED68 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-356dee1b0f10a12f](../../evidence/conditions-sets-021.md#c-356dee1b0f10a12f) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003939

```text
(config-perf-meas)# no delay-profile sr-policy probe measurement-mode two-way <cr>
```

Handler ` RVA 0x1ACF9B60 `；selector ` 0 `；EOL ` RVA 0x36DCF010 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-adf7844092e5694c](../../evidence/conditions-sets-067.md#c-adf7844092e5694c) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003917

```text
(config-perf-meas)# no delay-profile sr-policy probe padding-size <number:0..8000> <cr>
```

Handler ` RVA 0x1ACF8620 `；selector ` 0 `；EOL ` RVA 0x36DCE748 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Padding (bytes) to add to probes。

[条件 C-7fd6f1b4ba602c18](../../evidence/conditions-sets-050.md#c-7fd6f1b4ba602c18) · [参数 P-8b71d0a5c6717335](../../evidence/parameters-sets-011.md#p-8b71d0a5c6717335) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003846

```text
(config-perf-meas)# no delay-profile sr-policy probe protocol <cr>
```

Handler ` RVA 0x1ACF8A60 `；selector ` 0 `；EOL ` RVA 0x36DCFB58 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8b55d0da06b70929](../../evidence/conditions-sets-054.md#c-8b55d0da06b70929) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003950

```text
(config-perf-meas)# no delay-profile sr-policy probe protocol pm-mpls <cr>
```

Handler ` RVA 0x1ACF8E00 `；selector ` 0 `；EOL ` RVA 0x36DCF8C0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8b55d0da06b70929](../../evidence/conditions-sets-054.md#c-8b55d0da06b70929) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003945

```text
(config-perf-meas)# no delay-profile sr-policy probe protocol twamp-light <cr>
```

Handler ` RVA 0x1ACF8C90 `；selector ` 0 `；EOL ` RVA 0x36DCF618 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8b55d0da06b70929](../../evidence/conditions-sets-054.md#c-8b55d0da06b70929) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003849

```text
(config-perf-meas)# no delay-profile sr-policy probe sweep <cr>
```

Handler ` RVA 0x1ACF8F70 `；selector ` 0 `；EOL ` RVA 0x36DD0200 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8b55d0da06b70929](../../evidence/conditions-sets-054.md#c-8b55d0da06b70929) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003996

```text
(config-perf-meas)# no delay-profile sr-policy probe sweep destination ipv4 <address> range <number:0..128> <cr>
```

Handler ` RVA 0x1ACF9020 `；selector ` 0 `；EOL ` RVA 0x36DCFF50 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` IPv4 address (Required to be a 127.0.0.0/8 address)；` unsigned_number ` Sweeping range (Should fully be in the 127.0.0.0/8 space)。

[条件 C-8b55d0da06b70929](../../evidence/conditions-sets-054.md#c-8b55d0da06b70929) · [参数 P-3dd866ae41e7e577](../../evidence/parameters-sets-005.md#p-3dd866ae41e7e577) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003918

```text
(config-perf-meas)# no delay-profile sr-policy probe tos-dscp <number:0..63> <cr>
```

Handler ` RVA 0x1ACF8740 `；selector ` 0 `；EOL ` RVA 0x36DCEA38 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` TOS DSCP。

[条件 C-8b55d0da06b70929](../../evidence/conditions-sets-054.md#c-8b55d0da06b70929) · [参数 P-e1cfa9d140cff418](../../evidence/parameters-sets-017.md#p-e1cfa9d140cff418) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003785

```text
(config-perf-meas)# no dual-color gre bit-position <number:9..12> <cr>
```

Handler ` RVA 0x1ACF3B10 `；selector ` 0 `；EOL ` RVA 0x36DD7F80 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` bit-position value。

[条件 C-e0f33479f97c1ab8](../../evidence/conditions-sets-087.md#c-e0f33479f97c1ab8) · [参数 P-e08eb5e7b4635707](../../evidence/parameters-sets-017.md#p-e08eb5e7b4635707) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003712

```text
(config-perf-meas)# no endpoint <string> <cr>
```

Handler ` RVA 0x1ACFA0B0 `；selector ` 0 `；EOL ` RVA 0x36DC3EB0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Endpoint Name。

[参数 P-214ba9e98f3de846](../../evidence/parameters-sets-003.md#p-214ba9e98f3de846) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003729

```text
(config-perf-meas)# no endpoint <string> delay-measurement <cr>
```

Handler ` RVA 0x1ACFA820 `；selector ` 0 `；EOL ` RVA 0x36DC2A30 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Endpoint Name。

[参数 P-214ba9e98f3de846](../../evidence/parameters-sets-003.md#p-214ba9e98f3de846) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003853

```text
(config-perf-meas)# no endpoint <string> delay-measurement profile <string> <cr>
```

Handler ` RVA 0x1ACFAA20 `；selector ` 0 `；EOL ` RVA 0x36DC27B0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Endpoint Name；` string ` Profile name。

[参数 P-4e504d294400b577](../../evidence/parameters-sets-006.md#p-4e504d294400b577) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003851

```text
(config-perf-meas)# no endpoint <string> destination-address ipv4 <address> <cr>
```

Handler ` RVA 0x1ACFA520 `；selector ` 0 `；EOL ` RVA 0x36DC23F0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Endpoint Name；` address ` IPv4 endpoint address。

[参数 P-02c0cdf85ff294f8](../../evidence/parameters-sets-001.md#p-02c0cdf85ff294f8) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003740

```text
(config-perf-meas)# no endpoint <string> segment-list <cr>
```

Handler ` RVA 0x1ACFA770 `；selector ` 0 `；EOL ` RVA 0x36DC3988 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Endpoint Name。

[参数 P-214ba9e98f3de846](../../evidence/parameters-sets-003.md#p-214ba9e98f3de846) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003860

```text
(config-perf-meas)# no endpoint <string> segment-list forward-path <string> <cr>
```

Handler ` RVA 0x1ACFAB50 `；selector ` 0 `；EOL ` RVA 0x36DC3420 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Endpoint Name；` string ` Identifying name for segment-list。

[参数 P-cfd0a0cac03a746e](../../evidence/parameters-sets-016.md#p-cfd0a0cac03a746e) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003864

```text
(config-perf-meas)# no endpoint <string> segment-list reverse-path <string> <cr>
```

Handler ` RVA 0x1ACFACB0 `；selector ` 0 `；EOL ` RVA 0x36DC3708 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Endpoint Name；` string ` Identifying name for reverse path segment-list。

[参数 P-fd63338fb07cefeb](../../evidence/parameters-sets-019.md#p-fd63338fb07cefeb) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003732

```text
(config-perf-meas)# no endpoint <string> shutdown <cr>
```

Handler ` RVA 0x1ACFA990 `；selector ` 0 `；EOL ` RVA 0x36DC3C08 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Endpoint Name。

[参数 P-214ba9e98f3de846](../../evidence/parameters-sets-003.md#p-214ba9e98f3de846) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003855

```text
(config-perf-meas)# no endpoint <string> source-address ipv4 <address> <cr>
```

Handler ` RVA 0x1ACFA400 `；selector ` 0 `；EOL ` RVA 0x36DC2D78 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Endpoint Name；` address ` IPv4 source address。

[参数 P-27a7405fba1b69b4](../../evidence/parameters-sets-003.md#p-27a7405fba1b69b4) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003776

```text
(config-perf-meas)# no endpoint <string> vrf <string> <cr>
```

Handler ` RVA 0x1ACFA640 `；selector ` 0 `；EOL ` RVA 0x36DC30D0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Endpoint Name；` string ` VRF Name。

[参数 P-6fc9a77829f84728](../../evidence/parameters-sets-009.md#p-6fc9a77829f84728) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003704

```text
(config-perf-meas)# no loss-profile interfaces <cr>
```

Handler ` RVA 0x1ACEF800 `；selector ` 0 `；EOL ` RVA 0x36DC6DA8 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-606b89fe7872f8c5](../../evidence/conditions-sets-037.md#c-606b89fe7872f8c5) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003734

```text
(config-perf-meas)# no loss-profile interfaces advertisement <cr>
```

Handler ` RVA 0x1ACEFAF0 `；selector ` 0 `；EOL ` RVA 0x36DC5670 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-606b89fe7872f8c5](../../evidence/conditions-sets-037.md#c-606b89fe7872f8c5) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003791

```text
(config-perf-meas)# no loss-profile interfaces advertisement anomaly-check <cr>
```

Handler ` RVA 0x1ACEFE40 `；selector ` 0 `；EOL ` RVA 0x36DC5010 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-606b89fe7872f8c5](../../evidence/conditions-sets-037.md#c-606b89fe7872f8c5) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003784

```text
(config-perf-meas)# no loss-profile interfaces advertisement periodic <cr>
```

Handler ` RVA 0x1ACEFD90 `；selector ` 0 `；EOL ` RVA 0x36DC4CB8 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-606b89fe7872f8c5](../../evidence/conditions-sets-037.md#c-606b89fe7872f8c5) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003952

```text
(config-perf-meas)# no loss-profile interfaces advertisement periodic interval <number:30..3600> <cr>
```

Handler ` RVA 0x1ACF01C0 `；selector ` 0 `；EOL ` RVA 0x36DC4400 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` interval value in sec。

[条件 C-606b89fe7872f8c5](../../evidence/conditions-sets-037.md#c-606b89fe7872f8c5) · [参数 P-22673dbf4dd5bf85](../../evidence/parameters-sets-003.md#p-22673dbf4dd5bf85) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003748

```text
(config-perf-meas)# no loss-profile interfaces probe <cr>
```

Handler ` RVA 0x1ACEFC30 `；selector ` 0 `；EOL ` RVA 0x36DC6B18 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-606b89fe7872f8c5](../../evidence/conditions-sets-037.md#c-606b89fe7872f8c5) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003802

```text
(config-perf-meas)# no loss-profile interfaces probe color-type <cr>
```

Handler ` RVA 0x1ACF0550 `；selector ` 0 `；EOL ` RVA 0x36DC65A8 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-606b89fe7872f8c5](../../evidence/conditions-sets-037.md#c-606b89fe7872f8c5) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003959

```text
(config-perf-meas)# no loss-profile interfaces probe color-type dual-color gre <cr>
```

Handler ` RVA 0x1ACF0B20 `；selector ` 0 `；EOL ` RVA 0x36DC6318 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-606b89fe7872f8c5](../../evidence/conditions-sets-037.md#c-606b89fe7872f8c5) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003895

```text
(config-perf-meas)# no loss-profile interfaces probe color-type single-color <cr>
```

Handler ` RVA 0x1ACF0700 `；selector ` 0 `；EOL ` RVA 0x36DC6030 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-606b89fe7872f8c5](../../evidence/conditions-sets-037.md#c-606b89fe7872f8c5) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003989

```text
(config-perf-meas)# no loss-profile interfaces probe color-type single-color max-reordering <number:100..2000> <cr>
```

Handler ` RVA 0x1ACF0A10 `；selector ` 0 `；EOL ` RVA 0x36DC5DA8 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` maximum expected reordering value in miliseconds。

[条件 C-606b89fe7872f8c5](../../evidence/conditions-sets-037.md#c-606b89fe7872f8c5) · [参数 P-59fd1598f3c3c6cd](../../evidence/parameters-sets-007.md#p-59fd1598f3c3c6cd) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003870

```text
(config-perf-meas)# no loss-profile interfaces probe tx-interval <number:10..1000> <cr>
```

Handler ` RVA 0x1ACF05F0 `；selector ` 0 `；EOL ` RVA 0x36DC6890 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Transmit interval value in sec。

[条件 C-606b89fe7872f8c5](../../evidence/conditions-sets-037.md#c-606b89fe7872f8c5) · [参数 P-1741a8166c9b6621](../../evidence/parameters-sets-002.md#p-1741a8166c9b6621) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003706

```text
(config-perf-meas)# no protocol sdlm-light <cr>
```

Handler ` RVA 0x1ACEF690 `；selector ` 0 `；EOL ` RVA 0x36DD6BA0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-88ca28e64264fc2c](../../evidence/conditions-sets-053.md#c-88ca28e64264fc2c) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003789

```text
(config-perf-meas)# no protocol sdlm-light measurement loss <cr>
```

Handler ` RVA 0x1ACF35D0 `；selector ` 0 `；EOL ` RVA 0x36DD6920 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-88ca28e64264fc2c](../../evidence/conditions-sets-053.md#c-88ca28e64264fc2c) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003881

```text
(config-perf-meas)# no protocol sdlm-light measurement loss unauthenticated <cr>
```

Handler ` RVA 0x1ACF36F0 `；selector ` 0 `；EOL ` RVA 0x36DD62E0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-88ca28e64264fc2c](../../evidence/conditions-sets-053.md#c-88ca28e64264fc2c) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003991

```text
(config-perf-meas)# no protocol sdlm-light measurement loss unauthenticated querier-dst-port <number:1024..14999> <cr>
```

Handler ` RVA 0x1ACF3ED0 `；selector ` 0 `；EOL ` RVA 0x36DD6608 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Port number。

[条件 C-44f9b47a32de3af8](../../evidence/conditions-sets-027.md#c-44f9b47a32de3af8) · [参数 P-4ec43d1805d651a6](../../evidence/parameters-sets-006.md#p-4ec43d1805d651a6) · [状态效果 S-242855354dbca68f](../../evidence/state_effects-sets-008.md#s-242855354dbca68f)

### observed_connections-003707

```text
(config-perf-meas)# no protocol twamp-light <cr>
```

Handler ` RVA 0x1ACEF5A0 `；selector ` 0 `；EOL ` RVA 0x36DD78D8 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-25db707dca9abfe1](../../evidence/conditions-sets-015.md#c-25db707dca9abfe1) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003790

```text
(config-perf-meas)# no protocol twamp-light measurement delay <cr>
```

Handler ` RVA 0x1ACF31D0 `；selector ` 0 `；EOL ` RVA 0x36DD7658 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-25db707dca9abfe1](../../evidence/conditions-sets-015.md#c-25db707dca9abfe1) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003882

```text
(config-perf-meas)# no protocol twamp-light measurement delay unauthenticated <cr>
```

Handler ` RVA 0x1ACF3310 `；selector ` 0 `；EOL ` RVA 0x36DD6FB8 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-25db707dca9abfe1](../../evidence/conditions-sets-015.md#c-25db707dca9abfe1) · [状态效果 S-f0440739f74d2cd2](../../evidence/state_effects-sets-051.md#s-f0440739f74d2cd2)

### observed_connections-003992

```text
(config-perf-meas)# no protocol twamp-light measurement delay unauthenticated querier-dst-port <number:1024..14999> <cr>
```

Handler ` RVA 0x1ACF3BA0 `；selector ` 0 `；EOL ` RVA 0x36DD7308 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Port number。

[条件 C-701c7f308097b0b4](../../evidence/conditions-sets-043.md#c-701c7f308097b0b4) · [参数 P-3c1718846fb39911](../../evidence/parameters-sets-005.md#p-3c1718846fb39911) · [状态效果 S-034543f3e319f452](../../evidence/state_effects-sets-001.md#s-034543f3e319f452)

### observed_connections-003697

```text
(config-perf-meas)# protocol sdlm-light <cr>
```

Handler ` RVA 0x1ACEF690 `；selector ` 0 `；EOL ` RVA 0x36DD6BA0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-88ca28e64264fc2c](../../evidence/conditions-sets-053.md#c-88ca28e64264fc2c)

### observed_connections-003742

```text
(config-perf-meas)# protocol sdlm-light measurement loss <cr>
```

Handler ` RVA 0x1ACF35D0 `；selector ` 0 `；EOL ` RVA 0x36DD6920 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-88ca28e64264fc2c](../../evidence/conditions-sets-053.md#c-88ca28e64264fc2c)

### observed_connections-003796

```text
(config-perf-meas)# protocol sdlm-light measurement loss unauthenticated <cr>
```

Handler ` RVA 0x1ACF36F0 `；selector ` 0 `；EOL ` RVA 0x36DD62E0 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-88ca28e64264fc2c](../../evidence/conditions-sets-053.md#c-88ca28e64264fc2c)

### observed_connections-003973

```text
(config-perf-meas)# protocol sdlm-light measurement loss unauthenticated querier-dst-port <number:1024..14999> <cr>
```

Handler ` RVA 0x1ACF3ED0 `；selector ` 0 `；EOL ` RVA 0x36DD6608 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Port number。

[条件 C-44f9b47a32de3af8](../../evidence/conditions-sets-027.md#c-44f9b47a32de3af8) · [参数 P-4ec43d1805d651a6](../../evidence/parameters-sets-006.md#p-4ec43d1805d651a6) · [状态效果 S-54849f31e65277c5](../../evidence/state_effects-sets-018.md#s-54849f31e65277c5)

### observed_connections-003698

```text
(config-perf-meas)# protocol twamp-light <cr>
```

Handler ` RVA 0x1ACEF5A0 `；selector ` 0 `；EOL ` RVA 0x36DD78D8 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-25db707dca9abfe1](../../evidence/conditions-sets-015.md#c-25db707dca9abfe1)

### observed_connections-003743

```text
(config-perf-meas)# protocol twamp-light measurement delay <cr>
```

Handler ` RVA 0x1ACF31D0 `；selector ` 0 `；EOL ` RVA 0x36DD7658 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-25db707dca9abfe1](../../evidence/conditions-sets-015.md#c-25db707dca9abfe1)

### observed_connections-003797

```text
(config-perf-meas)# protocol twamp-light measurement delay unauthenticated <cr>
```

Handler ` RVA 0x1ACF3310 `；selector ` 0 `；EOL ` RVA 0x36DD6FB8 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-25db707dca9abfe1](../../evidence/conditions-sets-015.md#c-25db707dca9abfe1)

### observed_connections-003974

```text
(config-perf-meas)# protocol twamp-light measurement delay unauthenticated querier-dst-port <number:1024..14999> <cr>
```

Handler ` RVA 0x1ACF3BA0 `；selector ` 0 `；EOL ` RVA 0x36DD7308 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Port number。

[条件 C-701c7f308097b0b4](../../evidence/conditions-sets-043.md#c-701c7f308097b0b4) · [参数 P-3c1718846fb39911](../../evidence/parameters-sets-005.md#p-3c1718846fb39911) · [状态效果 S-04e0e993f9b84a80](../../evidence/state_effects-sets-001.md#s-04e0e993f9b84a80)

### observed_connections-003691

```text
(config-perf-meas)# <cr>
```

Handler ` RVA 0x1ACEEE70 `；selector ` 0 `；EOL ` RVA 0x36DD8220 `。

模式根 ` RVA 0x36DC17A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-16edb078860859dd](../../evidence/conditions-sets-009.md#c-16edb078860859dd)

