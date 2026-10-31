# pm-delay-srpol-profile-advertisement · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-008460

```text
(config-pm-dm-srpol-adv)# accelerated <cr>
```

Handler ` RVA 0x1ACF7990 `；selector ` 0 `；EOL ` RVA 0x36DCCBA8 `。

模式根 ` RVA 0x36DC1980 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-008477

```text
(config-pm-dm-srpol-adv)# accelerated minimum-change <number:0..1000000> <cr>
```

Handler ` RVA 0x1ACF7EB0 `；selector ` 0 `；EOL ` RVA 0x36DCC5F8 `。

模式根 ` RVA 0x36DC1980 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Accelerated advertisement minimum change (uSec)。

[参数 P-4895a79d21238df7](../../evidence/parameters-sets-006.md#p-4895a79d21238df7)

### observed_connections-008480

```text
(config-pm-dm-srpol-adv)# accelerated threshold <number:0..100> <cr>
```

Handler ` RVA 0x1ACF7D80 `；selector ` 0 `；EOL ` RVA 0x36DCC910 `。

模式根 ` RVA 0x36DC1980 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Accelerated advertisement threshold percentage change。

[参数 P-812a14f19936cf48](../../evidence/parameters-sets-010.md#p-812a14f19936cf48)

### observed_connections-008458

```text
(config-pm-dm-srpol-adv)# default <cr>
```

Handler ` RVA 0x1ACF7470 `；selector ` 0 `；EOL ` RVA 0x36DCDCB8 `。

模式根 ` RVA 0x36DC1980 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-609643bb9082b0d4](../../evidence/state_effects-sets-021.md#s-609643bb9082b0d4)

### observed_connections-008468

```text
(config-pm-dm-srpol-adv)# default accelerated <cr>
```

Handler ` RVA 0x1ACF7990 `；selector ` 0 `；EOL ` RVA 0x36DCCBA8 `。

模式根 ` RVA 0x36DC1980 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-609643bb9082b0d4](../../evidence/state_effects-sets-021.md#s-609643bb9082b0d4)

### observed_connections-008486

```text
(config-pm-dm-srpol-adv)# default accelerated minimum-change <number:0..1000000> <cr>
```

Handler ` RVA 0x1ACF7EB0 `；selector ` 0 `；EOL ` RVA 0x36DCC5F8 `。

模式根 ` RVA 0x36DC1980 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Accelerated advertisement minimum change (uSec)。

[参数 P-4895a79d21238df7](../../evidence/parameters-sets-006.md#p-4895a79d21238df7) · [状态效果 S-609643bb9082b0d4](../../evidence/state_effects-sets-021.md#s-609643bb9082b0d4)

### observed_connections-008490

```text
(config-pm-dm-srpol-adv)# default accelerated threshold <number:0..100> <cr>
```

Handler ` RVA 0x1ACF7D80 `；selector ` 0 `；EOL ` RVA 0x36DCC910 `。

模式根 ` RVA 0x36DC1980 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Accelerated advertisement threshold percentage change。

[参数 P-812a14f19936cf48](../../evidence/parameters-sets-010.md#p-812a14f19936cf48) · [状态效果 S-609643bb9082b0d4](../../evidence/state_effects-sets-021.md#s-609643bb9082b0d4)

### observed_connections-008470

```text
(config-pm-dm-srpol-adv)# default periodic <cr>
```

Handler ` RVA 0x1ACF7B10 `；selector ` 0 `；EOL ` RVA 0x36DCDA28 `。

模式根 ` RVA 0x36DC1980 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-609643bb9082b0d4](../../evidence/state_effects-sets-021.md#s-609643bb9082b0d4)

### observed_connections-008484

```text
(config-pm-dm-srpol-adv)# default periodic disabled <cr>
```

Handler ` RVA 0x1ACF7FE0 `；selector ` 0 `；EOL ` RVA 0x36DCD780 `。

模式根 ` RVA 0x36DC1980 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-609643bb9082b0d4](../../evidence/state_effects-sets-021.md#s-609643bb9082b0d4)

### observed_connections-008494

```text
(config-pm-dm-srpol-adv)# default periodic interval <number:30..3600> <cr>
```

Handler ` RVA 0x1ACF8080 `；selector ` 0 `；EOL ` RVA 0x36DCD4F8 `。

模式根 ` RVA 0x36DC1980 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number `  Periodic advertisement interval (seconds)。

[参数 P-70306a4f9901803d](../../evidence/parameters-sets-009.md#p-70306a4f9901803d) · [状态效果 S-609643bb9082b0d4](../../evidence/state_effects-sets-021.md#s-609643bb9082b0d4)

### observed_connections-008488

```text
(config-pm-dm-srpol-adv)# default periodic minimum-change <number:0..1000000> <cr>
```

Handler ` RVA 0x1ACF8320 `；selector ` 0 `；EOL ` RVA 0x36DCCEC8 `。

模式根 ` RVA 0x36DC1980 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Periodic advertisement minimum change (uSec)。

[参数 P-ebd32062bdb101ca](../../evidence/parameters-sets-018.md#p-ebd32062bdb101ca) · [状态效果 S-609643bb9082b0d4](../../evidence/state_effects-sets-021.md#s-609643bb9082b0d4)

### observed_connections-008492

```text
(config-pm-dm-srpol-adv)# default periodic threshold <number:0..100> <cr>
```

Handler ` RVA 0x1ACF8170 `；selector ` 0 `；EOL ` RVA 0x36DCD208 `。

模式根 ` RVA 0x36DC1980 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Periodic advertisement threshold percentage change。

[参数 P-c357520640169781](../../evidence/parameters-sets-015.md#p-c357520640169781) · [状态效果 S-609643bb9082b0d4](../../evidence/state_effects-sets-021.md#s-609643bb9082b0d4)

### observed_connections-008467

```text
(config-pm-dm-srpol-adv)# default threshold-check <cr>
```

Handler ` RVA 0x1ACF7CB0 `；selector ` 0 `；EOL ` RVA 0x36DCC248 `。

模式根 ` RVA 0x36DC1980 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-609643bb9082b0d4](../../evidence/state_effects-sets-021.md#s-609643bb9082b0d4)

### observed_connections-008473

```text
(config-pm-dm-srpol-adv)# default threshold-check average-delay <cr>
```

Handler ` RVA 0x1ACF9A00 `；selector ` 0 `；EOL ` RVA 0x36DCBA50 `。

模式根 ` RVA 0x36DC1980 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-609643bb9082b0d4](../../evidence/state_effects-sets-021.md#s-609643bb9082b0d4)

### observed_connections-008475

```text
(config-pm-dm-srpol-adv)# default threshold-check maximum-delay <cr>
```

Handler ` RVA 0x1ACF98A0 `；selector ` 0 `；EOL ` RVA 0x36DCBCF8 `。

模式根 ` RVA 0x36DC1980 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-609643bb9082b0d4](../../evidence/state_effects-sets-021.md#s-609643bb9082b0d4)

### observed_connections-008478

```text
(config-pm-dm-srpol-adv)# default threshold-check minimum-delay <cr>
```

Handler ` RVA 0x1ACF9740 `；selector ` 0 `；EOL ` RVA 0x36DCBFA0 `。

模式根 ` RVA 0x36DC1980 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-609643bb9082b0d4](../../evidence/state_effects-sets-021.md#s-609643bb9082b0d4)

### observed_connections-008456

```text
(config-pm-dm-srpol-adv)# exit <cr>
```

Handler ` RVA 0x1ACF9620 `；selector ` 0 `；EOL ` RVA 0x36DDB5D8 `。

模式根 ` RVA 0x36DC1980 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9c562570116bdf59](../../evidence/conditions-sets-060.md#c-9c562570116bdf59)

### observed_connections-008457

```text
(config-pm-dm-srpol-adv)# no <cr>
```

Handler ` RVA 0x1ACF7470 `；selector ` 0 `；EOL ` RVA 0x36DCDCB8 `。

模式根 ` RVA 0x36DC1980 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-45b889c6191970a0](../../evidence/state_effects-sets-015.md#s-45b889c6191970a0)

### observed_connections-008466

```text
(config-pm-dm-srpol-adv)# no accelerated <cr>
```

Handler ` RVA 0x1ACF7990 `；selector ` 0 `；EOL ` RVA 0x36DCCBA8 `。

模式根 ` RVA 0x36DC1980 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-45b889c6191970a0](../../evidence/state_effects-sets-015.md#s-45b889c6191970a0)

### observed_connections-008485

```text
(config-pm-dm-srpol-adv)# no accelerated minimum-change <number:0..1000000> <cr>
```

Handler ` RVA 0x1ACF7EB0 `；selector ` 0 `；EOL ` RVA 0x36DCC5F8 `。

模式根 ` RVA 0x36DC1980 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Accelerated advertisement minimum change (uSec)。

[参数 P-4895a79d21238df7](../../evidence/parameters-sets-006.md#p-4895a79d21238df7) · [状态效果 S-45b889c6191970a0](../../evidence/state_effects-sets-015.md#s-45b889c6191970a0)

### observed_connections-008489

```text
(config-pm-dm-srpol-adv)# no accelerated threshold <number:0..100> <cr>
```

Handler ` RVA 0x1ACF7D80 `；selector ` 0 `；EOL ` RVA 0x36DCC910 `。

模式根 ` RVA 0x36DC1980 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Accelerated advertisement threshold percentage change。

[参数 P-812a14f19936cf48](../../evidence/parameters-sets-010.md#p-812a14f19936cf48) · [状态效果 S-45b889c6191970a0](../../evidence/state_effects-sets-015.md#s-45b889c6191970a0)

### observed_connections-008469

```text
(config-pm-dm-srpol-adv)# no periodic <cr>
```

Handler ` RVA 0x1ACF7B10 `；selector ` 0 `；EOL ` RVA 0x36DCDA28 `。

模式根 ` RVA 0x36DC1980 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-45b889c6191970a0](../../evidence/state_effects-sets-015.md#s-45b889c6191970a0)

### observed_connections-008483

```text
(config-pm-dm-srpol-adv)# no periodic disabled <cr>
```

Handler ` RVA 0x1ACF7FE0 `；selector ` 0 `；EOL ` RVA 0x36DCD780 `。

模式根 ` RVA 0x36DC1980 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-45b889c6191970a0](../../evidence/state_effects-sets-015.md#s-45b889c6191970a0)

### observed_connections-008493

```text
(config-pm-dm-srpol-adv)# no periodic interval <number:30..3600> <cr>
```

Handler ` RVA 0x1ACF8080 `；selector ` 0 `；EOL ` RVA 0x36DCD4F8 `。

模式根 ` RVA 0x36DC1980 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number `  Periodic advertisement interval (seconds)。

[参数 P-70306a4f9901803d](../../evidence/parameters-sets-009.md#p-70306a4f9901803d) · [状态效果 S-45b889c6191970a0](../../evidence/state_effects-sets-015.md#s-45b889c6191970a0)

### observed_connections-008487

```text
(config-pm-dm-srpol-adv)# no periodic minimum-change <number:0..1000000> <cr>
```

Handler ` RVA 0x1ACF8320 `；selector ` 0 `；EOL ` RVA 0x36DCCEC8 `。

模式根 ` RVA 0x36DC1980 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Periodic advertisement minimum change (uSec)。

[参数 P-ebd32062bdb101ca](../../evidence/parameters-sets-018.md#p-ebd32062bdb101ca) · [状态效果 S-45b889c6191970a0](../../evidence/state_effects-sets-015.md#s-45b889c6191970a0)

### observed_connections-008491

```text
(config-pm-dm-srpol-adv)# no periodic threshold <number:0..100> <cr>
```

Handler ` RVA 0x1ACF8170 `；selector ` 0 `；EOL ` RVA 0x36DCD208 `。

模式根 ` RVA 0x36DC1980 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Periodic advertisement threshold percentage change。

[参数 P-c357520640169781](../../evidence/parameters-sets-015.md#p-c357520640169781) · [状态效果 S-45b889c6191970a0](../../evidence/state_effects-sets-015.md#s-45b889c6191970a0)

### observed_connections-008465

```text
(config-pm-dm-srpol-adv)# no threshold-check <cr>
```

Handler ` RVA 0x1ACF7CB0 `；selector ` 0 `；EOL ` RVA 0x36DCC248 `。

模式根 ` RVA 0x36DC1980 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-45b889c6191970a0](../../evidence/state_effects-sets-015.md#s-45b889c6191970a0)

### observed_connections-008472

```text
(config-pm-dm-srpol-adv)# no threshold-check average-delay <cr>
```

Handler ` RVA 0x1ACF9A00 `；selector ` 0 `；EOL ` RVA 0x36DCBA50 `。

模式根 ` RVA 0x36DC1980 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-45b889c6191970a0](../../evidence/state_effects-sets-015.md#s-45b889c6191970a0)

### observed_connections-008474

```text
(config-pm-dm-srpol-adv)# no threshold-check maximum-delay <cr>
```

Handler ` RVA 0x1ACF98A0 `；selector ` 0 `；EOL ` RVA 0x36DCBCF8 `。

模式根 ` RVA 0x36DC1980 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-45b889c6191970a0](../../evidence/state_effects-sets-015.md#s-45b889c6191970a0)

### observed_connections-008476

```text
(config-pm-dm-srpol-adv)# no threshold-check minimum-delay <cr>
```

Handler ` RVA 0x1ACF9740 `；selector ` 0 `；EOL ` RVA 0x36DCBFA0 `。

模式根 ` RVA 0x36DC1980 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-45b889c6191970a0](../../evidence/state_effects-sets-015.md#s-45b889c6191970a0)

### observed_connections-008461

```text
(config-pm-dm-srpol-adv)# periodic <cr>
```

Handler ` RVA 0x1ACF7B10 `；selector ` 0 `；EOL ` RVA 0x36DCDA28 `。

模式根 ` RVA 0x36DC1980 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-008471

```text
(config-pm-dm-srpol-adv)# periodic disabled <cr>
```

Handler ` RVA 0x1ACF7FE0 `；selector ` 0 `；EOL ` RVA 0x36DCD780 `。

模式根 ` RVA 0x36DC1980 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-008482

```text
(config-pm-dm-srpol-adv)# periodic interval <number:30..3600> <cr>
```

Handler ` RVA 0x1ACF8080 `；selector ` 0 `；EOL ` RVA 0x36DCD4F8 `。

模式根 ` RVA 0x36DC1980 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number `  Periodic advertisement interval (seconds)。

[参数 P-70306a4f9901803d](../../evidence/parameters-sets-009.md#p-70306a4f9901803d)

### observed_connections-008479

```text
(config-pm-dm-srpol-adv)# periodic minimum-change <number:0..1000000> <cr>
```

Handler ` RVA 0x1ACF8320 `；selector ` 0 `；EOL ` RVA 0x36DCCEC8 `。

模式根 ` RVA 0x36DC1980 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Periodic advertisement minimum change (uSec)。

[参数 P-ebd32062bdb101ca](../../evidence/parameters-sets-018.md#p-ebd32062bdb101ca)

### observed_connections-008481

```text
(config-pm-dm-srpol-adv)# periodic threshold <number:0..100> <cr>
```

Handler ` RVA 0x1ACF8170 `；selector ` 0 `；EOL ` RVA 0x36DCD208 `。

模式根 ` RVA 0x36DC1980 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Periodic advertisement threshold percentage change。

[参数 P-c357520640169781](../../evidence/parameters-sets-015.md#p-c357520640169781)

### observed_connections-008459

```text
(config-pm-dm-srpol-adv)# threshold-check <cr>
```

Handler ` RVA 0x1ACF7CB0 `；selector ` 0 `；EOL ` RVA 0x36DCC248 `。

模式根 ` RVA 0x36DC1980 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-008462

```text
(config-pm-dm-srpol-adv)# threshold-check average-delay <cr>
```

Handler ` RVA 0x1ACF9A00 `；selector ` 0 `；EOL ` RVA 0x36DCBA50 `。

模式根 ` RVA 0x36DC1980 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-008463

```text
(config-pm-dm-srpol-adv)# threshold-check maximum-delay <cr>
```

Handler ` RVA 0x1ACF98A0 `；selector ` 0 `；EOL ` RVA 0x36DCBCF8 `。

模式根 ` RVA 0x36DC1980 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-008464

```text
(config-pm-dm-srpol-adv)# threshold-check minimum-delay <cr>
```

Handler ` RVA 0x1ACF9740 `；selector ` 0 `；EOL ` RVA 0x36DCBFA0 `。

模式根 ` RVA 0x36DC1980 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-008455

```text
(config-pm-dm-srpol-adv)# <cr>
```

Handler ` RVA 0x1ACF7470 `；selector ` 0 `；EOL ` RVA 0x36DCDCB8 `。

模式根 ` RVA 0x36DC1980 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。
