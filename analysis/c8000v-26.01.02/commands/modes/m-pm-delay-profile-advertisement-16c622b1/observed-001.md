# pm-delay-profile-advertisement · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-008762

```text
(config-pm-dm-intf-adv)# accelerated <cr>
```

Handler ` RVA 0x1ACF1600 `；selector ` 0 `；EOL ` RVA 0x36DD17A0 `。

模式根 ` RVA 0x36DC1958 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-008770

```text
(config-pm-dm-intf-adv)# accelerated minimum-change <number:0..1000000> <cr>
```

Handler ` RVA 0x1ACF1BE0 `；selector ` 0 `；EOL ` RVA 0x36DD11F0 `。

模式根 ` RVA 0x36DC1958 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Accelerated advertisement minimum change (uSec)。

[参数 P-87f9628a76ee7742](../../evidence/parameters-sets-010.md#p-87f9628a76ee7742)

### observed_connections-008772

```text
(config-pm-dm-intf-adv)# accelerated threshold <number:0..100> <cr>
```

Handler ` RVA 0x1ACF1AB0 `；selector ` 0 `；EOL ` RVA 0x36DD1508 `。

模式根 ` RVA 0x36DC1958 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Accelerated advertisement threshold percentage change。

[参数 P-f0ea66ce03e923ef](../../evidence/parameters-sets-018.md#p-f0ea66ce03e923ef)

### observed_connections-008763

```text
(config-pm-dm-intf-adv)# default <cr>
```

Handler ` RVA 0x1ACF12B0 `；selector ` 0 `；EOL ` RVA 0x36DD28F0 `。

模式根 ` RVA 0x36DC1958 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-d61441a8721f6a98](../../evidence/state_effects-sets-045.md#s-d61441a8721f6a98)

### observed_connections-008766

```text
(config-pm-dm-intf-adv)# default accelerated <cr>
```

Handler ` RVA 0x1ACF1600 `；selector ` 0 `；EOL ` RVA 0x36DD17A0 `。

模式根 ` RVA 0x36DC1958 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-d61441a8721f6a98](../../evidence/state_effects-sets-045.md#s-d61441a8721f6a98)

### observed_connections-008778

```text
(config-pm-dm-intf-adv)# default accelerated minimum-change <number:0..1000000> <cr>
```

Handler ` RVA 0x1ACF1BE0 `；selector ` 0 `；EOL ` RVA 0x36DD11F0 `。

模式根 ` RVA 0x36DC1958 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Accelerated advertisement minimum change (uSec)。

[参数 P-87f9628a76ee7742](../../evidence/parameters-sets-010.md#p-87f9628a76ee7742) · [状态效果 S-d61441a8721f6a98](../../evidence/state_effects-sets-045.md#s-d61441a8721f6a98)

### observed_connections-008782

```text
(config-pm-dm-intf-adv)# default accelerated threshold <number:0..100> <cr>
```

Handler ` RVA 0x1ACF1AB0 `；selector ` 0 `；EOL ` RVA 0x36DD1508 `。

模式根 ` RVA 0x36DC1958 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Accelerated advertisement threshold percentage change。

[参数 P-f0ea66ce03e923ef](../../evidence/parameters-sets-018.md#p-f0ea66ce03e923ef) · [状态效果 S-d61441a8721f6a98](../../evidence/state_effects-sets-045.md#s-d61441a8721f6a98)

### observed_connections-008768

```text
(config-pm-dm-intf-adv)# default periodic <cr>
```

Handler ` RVA 0x1ACF1830 `；selector ` 0 `；EOL ` RVA 0x36DD2670 `。

模式根 ` RVA 0x36DC1958 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-d61441a8721f6a98](../../evidence/state_effects-sets-045.md#s-d61441a8721f6a98)

### observed_connections-008776

```text
(config-pm-dm-intf-adv)# default periodic disabled <cr>
```

Handler ` RVA 0x1ACF1D10 `；selector ` 0 `；EOL ` RVA 0x36DD23C8 `。

模式根 ` RVA 0x36DC1958 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-d61441a8721f6a98](../../evidence/state_effects-sets-045.md#s-d61441a8721f6a98)

### observed_connections-008786

```text
(config-pm-dm-intf-adv)# default periodic interval <number:30..3600> <cr>
```

Handler ` RVA 0x1ACF1DB0 `；selector ` 0 `；EOL ` RVA 0x36DD2140 `。

模式根 ` RVA 0x36DC1958 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number `  Periodic advertisement interval (seconds)。

[参数 P-7083362af6595dd1](../../evidence/parameters-sets-009.md#p-7083362af6595dd1) · [状态效果 S-d61441a8721f6a98](../../evidence/state_effects-sets-045.md#s-d61441a8721f6a98)

### observed_connections-008781

```text
(config-pm-dm-intf-adv)# default periodic minimum-change <number:0..1000000> <cr>
```

Handler ` RVA 0x1ACF2050 `；selector ` 0 `；EOL ` RVA 0x36DD1B10 `。

模式根 ` RVA 0x36DC1958 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Periodic advertisement minimum change (uSec)。

[参数 P-a9f06d097ad720d7](../../evidence/parameters-sets-013.md#p-a9f06d097ad720d7) · [状态效果 S-d61441a8721f6a98](../../evidence/state_effects-sets-045.md#s-d61441a8721f6a98)

### observed_connections-008784

```text
(config-pm-dm-intf-adv)# default periodic threshold <number:0..100> <cr>
```

Handler ` RVA 0x1ACF1EA0 `；selector ` 0 `；EOL ` RVA 0x36DD1E50 `。

模式根 ` RVA 0x36DC1958 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Periodic advertisement threshold percentage change。

[参数 P-870c791c38909c22](../../evidence/parameters-sets-010.md#p-870c791c38909c22) · [状态效果 S-d61441a8721f6a98](../../evidence/state_effects-sets-045.md#s-d61441a8721f6a98)

### observed_connections-008760

```text
(config-pm-dm-intf-adv)# exit <cr>
```

Handler ` RVA 0x1ACF4910 `；selector ` 0 `；EOL ` RVA 0x36DDB1D0 `。

模式根 ` RVA 0x36DC1958 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-26937931704adbc0](../../evidence/conditions-sets-015.md#c-26937931704adbc0)

### observed_connections-008761

```text
(config-pm-dm-intf-adv)# no <cr>
```

Handler ` RVA 0x1ACF12B0 `；selector ` 0 `；EOL ` RVA 0x36DD28F0 `。

模式根 ` RVA 0x36DC1958 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-77970ef0d1f48f18](../../evidence/state_effects-sets-025.md#s-77970ef0d1f48f18)

### observed_connections-008765

```text
(config-pm-dm-intf-adv)# no accelerated <cr>
```

Handler ` RVA 0x1ACF1600 `；selector ` 0 `；EOL ` RVA 0x36DD17A0 `。

模式根 ` RVA 0x36DC1958 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-77970ef0d1f48f18](../../evidence/state_effects-sets-025.md#s-77970ef0d1f48f18)

### observed_connections-008777

```text
(config-pm-dm-intf-adv)# no accelerated minimum-change <number:0..1000000> <cr>
```

Handler ` RVA 0x1ACF1BE0 `；selector ` 0 `；EOL ` RVA 0x36DD11F0 `。

模式根 ` RVA 0x36DC1958 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Accelerated advertisement minimum change (uSec)。

[参数 P-87f9628a76ee7742](../../evidence/parameters-sets-010.md#p-87f9628a76ee7742) · [状态效果 S-77970ef0d1f48f18](../../evidence/state_effects-sets-025.md#s-77970ef0d1f48f18)

### observed_connections-008780

```text
(config-pm-dm-intf-adv)# no accelerated threshold <number:0..100> <cr>
```

Handler ` RVA 0x1ACF1AB0 `；selector ` 0 `；EOL ` RVA 0x36DD1508 `。

模式根 ` RVA 0x36DC1958 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Accelerated advertisement threshold percentage change。

[参数 P-f0ea66ce03e923ef](../../evidence/parameters-sets-018.md#p-f0ea66ce03e923ef) · [状态效果 S-77970ef0d1f48f18](../../evidence/state_effects-sets-025.md#s-77970ef0d1f48f18)

### observed_connections-008767

```text
(config-pm-dm-intf-adv)# no periodic <cr>
```

Handler ` RVA 0x1ACF1830 `；selector ` 0 `；EOL ` RVA 0x36DD2670 `。

模式根 ` RVA 0x36DC1958 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-77970ef0d1f48f18](../../evidence/state_effects-sets-025.md#s-77970ef0d1f48f18)

### observed_connections-008775

```text
(config-pm-dm-intf-adv)# no periodic disabled <cr>
```

Handler ` RVA 0x1ACF1D10 `；selector ` 0 `；EOL ` RVA 0x36DD23C8 `。

模式根 ` RVA 0x36DC1958 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-77970ef0d1f48f18](../../evidence/state_effects-sets-025.md#s-77970ef0d1f48f18)

### observed_connections-008785

```text
(config-pm-dm-intf-adv)# no periodic interval <number:30..3600> <cr>
```

Handler ` RVA 0x1ACF1DB0 `；selector ` 0 `；EOL ` RVA 0x36DD2140 `。

模式根 ` RVA 0x36DC1958 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number `  Periodic advertisement interval (seconds)。

[参数 P-7083362af6595dd1](../../evidence/parameters-sets-009.md#p-7083362af6595dd1) · [状态效果 S-77970ef0d1f48f18](../../evidence/state_effects-sets-025.md#s-77970ef0d1f48f18)

### observed_connections-008779

```text
(config-pm-dm-intf-adv)# no periodic minimum-change <number:0..1000000> <cr>
```

Handler ` RVA 0x1ACF2050 `；selector ` 0 `；EOL ` RVA 0x36DD1B10 `。

模式根 ` RVA 0x36DC1958 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Periodic advertisement minimum change (uSec)。

[参数 P-a9f06d097ad720d7](../../evidence/parameters-sets-013.md#p-a9f06d097ad720d7) · [状态效果 S-77970ef0d1f48f18](../../evidence/state_effects-sets-025.md#s-77970ef0d1f48f18)

### observed_connections-008783

```text
(config-pm-dm-intf-adv)# no periodic threshold <number:0..100> <cr>
```

Handler ` RVA 0x1ACF1EA0 `；selector ` 0 `；EOL ` RVA 0x36DD1E50 `。

模式根 ` RVA 0x36DC1958 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Periodic advertisement threshold percentage change。

[参数 P-870c791c38909c22](../../evidence/parameters-sets-010.md#p-870c791c38909c22) · [状态效果 S-77970ef0d1f48f18](../../evidence/state_effects-sets-025.md#s-77970ef0d1f48f18)

### observed_connections-008764

```text
(config-pm-dm-intf-adv)# periodic <cr>
```

Handler ` RVA 0x1ACF1830 `；selector ` 0 `；EOL ` RVA 0x36DD2670 `。

模式根 ` RVA 0x36DC1958 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-008769

```text
(config-pm-dm-intf-adv)# periodic disabled <cr>
```

Handler ` RVA 0x1ACF1D10 `；selector ` 0 `；EOL ` RVA 0x36DD23C8 `。

模式根 ` RVA 0x36DC1958 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-008774

```text
(config-pm-dm-intf-adv)# periodic interval <number:30..3600> <cr>
```

Handler ` RVA 0x1ACF1DB0 `；selector ` 0 `；EOL ` RVA 0x36DD2140 `。

模式根 ` RVA 0x36DC1958 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number `  Periodic advertisement interval (seconds)。

[参数 P-7083362af6595dd1](../../evidence/parameters-sets-009.md#p-7083362af6595dd1)

### observed_connections-008771

```text
(config-pm-dm-intf-adv)# periodic minimum-change <number:0..1000000> <cr>
```

Handler ` RVA 0x1ACF2050 `；selector ` 0 `；EOL ` RVA 0x36DD1B10 `。

模式根 ` RVA 0x36DC1958 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Periodic advertisement minimum change (uSec)。

[参数 P-a9f06d097ad720d7](../../evidence/parameters-sets-013.md#p-a9f06d097ad720d7)

### observed_connections-008773

```text
(config-pm-dm-intf-adv)# periodic threshold <number:0..100> <cr>
```

Handler ` RVA 0x1ACF1EA0 `；selector ` 0 `；EOL ` RVA 0x36DD1E50 `。

模式根 ` RVA 0x36DC1958 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Periodic advertisement threshold percentage change。

[参数 P-870c791c38909c22](../../evidence/parameters-sets-010.md#p-870c791c38909c22)

### observed_connections-008759

```text
(config-pm-dm-intf-adv)# <cr>
```

Handler ` RVA 0x1ACF12B0 `；selector ` 0 `；EOL ` RVA 0x36DD28F0 `。

模式根 ` RVA 0x36DC1958 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

