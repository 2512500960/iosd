# pm-delay-ep-profile-advertisement · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-008500

```text
(config-pm-dm-ep-adv)# accelerated <cr>
```

Handler ` RVA 0x1ACFB3D0 `；selector ` 0 `；EOL ` RVA 0x36DC83D8 `。

模式根 ` RVA 0x36DC19A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-008517

```text
(config-pm-dm-ep-adv)# accelerated minimum-change <number:0..1000000> <cr>
```

Handler ` RVA 0x1ACFB890 `；selector ` 0 `；EOL ` RVA 0x36DC7E28 `。

模式根 ` RVA 0x36DC19A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Accelerated advertisement minimum change (uSec)。

[参数 P-9f6f6ba2d130deb9](../../evidence/parameters-sets-012.md#p-9f6f6ba2d130deb9)

### observed_connections-008520

```text
(config-pm-dm-ep-adv)# accelerated threshold <number:0..100> <cr>
```

Handler ` RVA 0x1ACFB760 `；selector ` 0 `；EOL ` RVA 0x36DC8140 `。

模式根 ` RVA 0x36DC19A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Accelerated advertisement threshold percentage change。

[参数 P-2bf284102dc3b5f7](../../evidence/parameters-sets-004.md#p-2bf284102dc3b5f7)

### observed_connections-008498

```text
(config-pm-dm-ep-adv)# default <cr>
```

Handler ` RVA 0x1ACFAE10 `；selector ` 0 `；EOL ` RVA 0x36DC94E8 `。

模式根 ` RVA 0x36DC19A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-45acc1ae7126293d](../../evidence/state_effects-sets-015.md#s-45acc1ae7126293d)

### observed_connections-008508

```text
(config-pm-dm-ep-adv)# default accelerated <cr>
```

Handler ` RVA 0x1ACFB3D0 `；selector ` 0 `；EOL ` RVA 0x36DC83D8 `。

模式根 ` RVA 0x36DC19A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-45acc1ae7126293d](../../evidence/state_effects-sets-015.md#s-45acc1ae7126293d)

### observed_connections-008526

```text
(config-pm-dm-ep-adv)# default accelerated minimum-change <number:0..1000000> <cr>
```

Handler ` RVA 0x1ACFB890 `；selector ` 0 `；EOL ` RVA 0x36DC7E28 `。

模式根 ` RVA 0x36DC19A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Accelerated advertisement minimum change (uSec)。

[参数 P-9f6f6ba2d130deb9](../../evidence/parameters-sets-012.md#p-9f6f6ba2d130deb9) · [状态效果 S-45acc1ae7126293d](../../evidence/state_effects-sets-015.md#s-45acc1ae7126293d)

### observed_connections-008530

```text
(config-pm-dm-ep-adv)# default accelerated threshold <number:0..100> <cr>
```

Handler ` RVA 0x1ACFB760 `；selector ` 0 `；EOL ` RVA 0x36DC8140 `。

模式根 ` RVA 0x36DC19A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Accelerated advertisement threshold percentage change。

[参数 P-2bf284102dc3b5f7](../../evidence/parameters-sets-004.md#p-2bf284102dc3b5f7) · [状态效果 S-45acc1ae7126293d](../../evidence/state_effects-sets-015.md#s-45acc1ae7126293d)

### observed_connections-008510

```text
(config-pm-dm-ep-adv)# default periodic <cr>
```

Handler ` RVA 0x1ACFB520 `；selector ` 0 `；EOL ` RVA 0x36DC9258 `。

模式根 ` RVA 0x36DC19A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-45acc1ae7126293d](../../evidence/state_effects-sets-015.md#s-45acc1ae7126293d)

### observed_connections-008524

```text
(config-pm-dm-ep-adv)# default periodic disabled <cr>
```

Handler ` RVA 0x1ACFB9C0 `；selector ` 0 `；EOL ` RVA 0x36DC8FB0 `。

模式根 ` RVA 0x36DC19A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-45acc1ae7126293d](../../evidence/state_effects-sets-015.md#s-45acc1ae7126293d)

### observed_connections-008534

```text
(config-pm-dm-ep-adv)# default periodic interval <number:30..3600> <cr>
```

Handler ` RVA 0x1ACFBA60 `；selector ` 0 `；EOL ` RVA 0x36DC8D28 `。

模式根 ` RVA 0x36DC19A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number `  Periodic advertisement interval (seconds)。

[参数 P-9239b3dae0fed22a](../../evidence/parameters-sets-011.md#p-9239b3dae0fed22a) · [状态效果 S-45acc1ae7126293d](../../evidence/state_effects-sets-015.md#s-45acc1ae7126293d)

### observed_connections-008528

```text
(config-pm-dm-ep-adv)# default periodic minimum-change <number:0..1000000> <cr>
```

Handler ` RVA 0x1ACFBD00 `；selector ` 0 `；EOL ` RVA 0x36DC86F8 `。

模式根 ` RVA 0x36DC19A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Periodic advertisement minimum change (uSec)。

[参数 P-ca7c92d34181e004](../../evidence/parameters-sets-015.md#p-ca7c92d34181e004) · [状态效果 S-45acc1ae7126293d](../../evidence/state_effects-sets-015.md#s-45acc1ae7126293d)

### observed_connections-008532

```text
(config-pm-dm-ep-adv)# default periodic threshold <number:0..100> <cr>
```

Handler ` RVA 0x1ACFBB50 `；selector ` 0 `；EOL ` RVA 0x36DC8A38 `。

模式根 ` RVA 0x36DC19A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Periodic advertisement threshold percentage change。

[参数 P-0f8747ef381467d2](../../evidence/parameters-sets-002.md#p-0f8747ef381467d2) · [状态效果 S-45acc1ae7126293d](../../evidence/state_effects-sets-015.md#s-45acc1ae7126293d)

### observed_connections-008507

```text
(config-pm-dm-ep-adv)# default threshold-check <cr>
```

Handler ` RVA 0x1ACFB6B0 `；selector ` 0 `；EOL ` RVA 0x36DC7A78 `。

模式根 ` RVA 0x36DC19A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-45acc1ae7126293d](../../evidence/state_effects-sets-015.md#s-45acc1ae7126293d)

### observed_connections-008513

```text
(config-pm-dm-ep-adv)# default threshold-check average-delay <cr>
```

Handler ` RVA 0x1ACFCC80 `；selector ` 0 `；EOL ` RVA 0x36DC7280 `。

模式根 ` RVA 0x36DC19A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-45acc1ae7126293d](../../evidence/state_effects-sets-015.md#s-45acc1ae7126293d)

### observed_connections-008515

```text
(config-pm-dm-ep-adv)# default threshold-check maximum-delay <cr>
```

Handler ` RVA 0x1ACFCB30 `；selector ` 0 `；EOL ` RVA 0x36DC7528 `。

模式根 ` RVA 0x36DC19A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-45acc1ae7126293d](../../evidence/state_effects-sets-015.md#s-45acc1ae7126293d)

### observed_connections-008518

```text
(config-pm-dm-ep-adv)# default threshold-check minimum-delay <cr>
```

Handler ` RVA 0x1ACFC9E0 `；selector ` 0 `；EOL ` RVA 0x36DC77D0 `。

模式根 ` RVA 0x36DC19A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-45acc1ae7126293d](../../evidence/state_effects-sets-015.md#s-45acc1ae7126293d)

### observed_connections-008496

```text
(config-pm-dm-ep-adv)# exit <cr>
```

Handler ` RVA 0x1ACFC8C0 `；selector ` 0 `；EOL ` RVA 0x36DDB9E0 `。

模式根 ` RVA 0x36DC19A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-611f1b2e28c2c701](../../evidence/conditions-sets-038.md#c-611f1b2e28c2c701)

### observed_connections-008497

```text
(config-pm-dm-ep-adv)# no <cr>
```

Handler ` RVA 0x1ACFAE10 `；selector ` 0 `；EOL ` RVA 0x36DC94E8 `。

模式根 ` RVA 0x36DC19A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-340ed20119b33037](../../evidence/state_effects-sets-012.md#s-340ed20119b33037)

### observed_connections-008506

```text
(config-pm-dm-ep-adv)# no accelerated <cr>
```

Handler ` RVA 0x1ACFB3D0 `；selector ` 0 `；EOL ` RVA 0x36DC83D8 `。

模式根 ` RVA 0x36DC19A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-340ed20119b33037](../../evidence/state_effects-sets-012.md#s-340ed20119b33037)

### observed_connections-008525

```text
(config-pm-dm-ep-adv)# no accelerated minimum-change <number:0..1000000> <cr>
```

Handler ` RVA 0x1ACFB890 `；selector ` 0 `；EOL ` RVA 0x36DC7E28 `。

模式根 ` RVA 0x36DC19A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Accelerated advertisement minimum change (uSec)。

[参数 P-9f6f6ba2d130deb9](../../evidence/parameters-sets-012.md#p-9f6f6ba2d130deb9) · [状态效果 S-340ed20119b33037](../../evidence/state_effects-sets-012.md#s-340ed20119b33037)

### observed_connections-008529

```text
(config-pm-dm-ep-adv)# no accelerated threshold <number:0..100> <cr>
```

Handler ` RVA 0x1ACFB760 `；selector ` 0 `；EOL ` RVA 0x36DC8140 `。

模式根 ` RVA 0x36DC19A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Accelerated advertisement threshold percentage change。

[参数 P-2bf284102dc3b5f7](../../evidence/parameters-sets-004.md#p-2bf284102dc3b5f7) · [状态效果 S-340ed20119b33037](../../evidence/state_effects-sets-012.md#s-340ed20119b33037)

### observed_connections-008509

```text
(config-pm-dm-ep-adv)# no periodic <cr>
```

Handler ` RVA 0x1ACFB520 `；selector ` 0 `；EOL ` RVA 0x36DC9258 `。

模式根 ` RVA 0x36DC19A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-340ed20119b33037](../../evidence/state_effects-sets-012.md#s-340ed20119b33037)

### observed_connections-008523

```text
(config-pm-dm-ep-adv)# no periodic disabled <cr>
```

Handler ` RVA 0x1ACFB9C0 `；selector ` 0 `；EOL ` RVA 0x36DC8FB0 `。

模式根 ` RVA 0x36DC19A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-340ed20119b33037](../../evidence/state_effects-sets-012.md#s-340ed20119b33037)

### observed_connections-008533

```text
(config-pm-dm-ep-adv)# no periodic interval <number:30..3600> <cr>
```

Handler ` RVA 0x1ACFBA60 `；selector ` 0 `；EOL ` RVA 0x36DC8D28 `。

模式根 ` RVA 0x36DC19A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number `  Periodic advertisement interval (seconds)。

[参数 P-9239b3dae0fed22a](../../evidence/parameters-sets-011.md#p-9239b3dae0fed22a) · [状态效果 S-340ed20119b33037](../../evidence/state_effects-sets-012.md#s-340ed20119b33037)

### observed_connections-008527

```text
(config-pm-dm-ep-adv)# no periodic minimum-change <number:0..1000000> <cr>
```

Handler ` RVA 0x1ACFBD00 `；selector ` 0 `；EOL ` RVA 0x36DC86F8 `。

模式根 ` RVA 0x36DC19A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Periodic advertisement minimum change (uSec)。

[参数 P-ca7c92d34181e004](../../evidence/parameters-sets-015.md#p-ca7c92d34181e004) · [状态效果 S-340ed20119b33037](../../evidence/state_effects-sets-012.md#s-340ed20119b33037)

### observed_connections-008531

```text
(config-pm-dm-ep-adv)# no periodic threshold <number:0..100> <cr>
```

Handler ` RVA 0x1ACFBB50 `；selector ` 0 `；EOL ` RVA 0x36DC8A38 `。

模式根 ` RVA 0x36DC19A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Periodic advertisement threshold percentage change。

[参数 P-0f8747ef381467d2](../../evidence/parameters-sets-002.md#p-0f8747ef381467d2) · [状态效果 S-340ed20119b33037](../../evidence/state_effects-sets-012.md#s-340ed20119b33037)

### observed_connections-008505

```text
(config-pm-dm-ep-adv)# no threshold-check <cr>
```

Handler ` RVA 0x1ACFB6B0 `；selector ` 0 `；EOL ` RVA 0x36DC7A78 `。

模式根 ` RVA 0x36DC19A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-340ed20119b33037](../../evidence/state_effects-sets-012.md#s-340ed20119b33037)

### observed_connections-008512

```text
(config-pm-dm-ep-adv)# no threshold-check average-delay <cr>
```

Handler ` RVA 0x1ACFCC80 `；selector ` 0 `；EOL ` RVA 0x36DC7280 `。

模式根 ` RVA 0x36DC19A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-340ed20119b33037](../../evidence/state_effects-sets-012.md#s-340ed20119b33037)

### observed_connections-008514

```text
(config-pm-dm-ep-adv)# no threshold-check maximum-delay <cr>
```

Handler ` RVA 0x1ACFCB30 `；selector ` 0 `；EOL ` RVA 0x36DC7528 `。

模式根 ` RVA 0x36DC19A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-340ed20119b33037](../../evidence/state_effects-sets-012.md#s-340ed20119b33037)

### observed_connections-008516

```text
(config-pm-dm-ep-adv)# no threshold-check minimum-delay <cr>
```

Handler ` RVA 0x1ACFC9E0 `；selector ` 0 `；EOL ` RVA 0x36DC77D0 `。

模式根 ` RVA 0x36DC19A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-340ed20119b33037](../../evidence/state_effects-sets-012.md#s-340ed20119b33037)

### observed_connections-008501

```text
(config-pm-dm-ep-adv)# periodic <cr>
```

Handler ` RVA 0x1ACFB520 `；selector ` 0 `；EOL ` RVA 0x36DC9258 `。

模式根 ` RVA 0x36DC19A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-008511

```text
(config-pm-dm-ep-adv)# periodic disabled <cr>
```

Handler ` RVA 0x1ACFB9C0 `；selector ` 0 `；EOL ` RVA 0x36DC8FB0 `。

模式根 ` RVA 0x36DC19A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-008522

```text
(config-pm-dm-ep-adv)# periodic interval <number:30..3600> <cr>
```

Handler ` RVA 0x1ACFBA60 `；selector ` 0 `；EOL ` RVA 0x36DC8D28 `。

模式根 ` RVA 0x36DC19A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number `  Periodic advertisement interval (seconds)。

[参数 P-9239b3dae0fed22a](../../evidence/parameters-sets-011.md#p-9239b3dae0fed22a)

### observed_connections-008519

```text
(config-pm-dm-ep-adv)# periodic minimum-change <number:0..1000000> <cr>
```

Handler ` RVA 0x1ACFBD00 `；selector ` 0 `；EOL ` RVA 0x36DC86F8 `。

模式根 ` RVA 0x36DC19A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Periodic advertisement minimum change (uSec)。

[参数 P-ca7c92d34181e004](../../evidence/parameters-sets-015.md#p-ca7c92d34181e004)

### observed_connections-008521

```text
(config-pm-dm-ep-adv)# periodic threshold <number:0..100> <cr>
```

Handler ` RVA 0x1ACFBB50 `；selector ` 0 `；EOL ` RVA 0x36DC8A38 `。

模式根 ` RVA 0x36DC19A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Periodic advertisement threshold percentage change。

[参数 P-0f8747ef381467d2](../../evidence/parameters-sets-002.md#p-0f8747ef381467d2)

### observed_connections-008499

```text
(config-pm-dm-ep-adv)# threshold-check <cr>
```

Handler ` RVA 0x1ACFB6B0 `；selector ` 0 `；EOL ` RVA 0x36DC7A78 `。

模式根 ` RVA 0x36DC19A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-008502

```text
(config-pm-dm-ep-adv)# threshold-check average-delay <cr>
```

Handler ` RVA 0x1ACFCC80 `；selector ` 0 `；EOL ` RVA 0x36DC7280 `。

模式根 ` RVA 0x36DC19A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-008503

```text
(config-pm-dm-ep-adv)# threshold-check maximum-delay <cr>
```

Handler ` RVA 0x1ACFCB30 `；selector ` 0 `；EOL ` RVA 0x36DC7528 `。

模式根 ` RVA 0x36DC19A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-008504

```text
(config-pm-dm-ep-adv)# threshold-check minimum-delay <cr>
```

Handler ` RVA 0x1ACFC9E0 `；selector ` 0 `；EOL ` RVA 0x36DC77D0 `。

模式根 ` RVA 0x36DC19A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-008495

```text
(config-pm-dm-ep-adv)# <cr>
```

Handler ` RVA 0x1ACFAE10 `；selector ` 0 `；EOL ` RVA 0x36DC94E8 `。

模式根 ` RVA 0x36DC19A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。
