# pm-delay-profile-ep-advertisement-periodic · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-009240

```text
(config-pm-dm-ep-adv-per)# default <cr>
```

Handler ` RVA 0x1ACFB520 `；selector ` 0 `；EOL ` RVA 0x36DC9258 `。

模式根 ` RVA 0x36DC1AE8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-1c43dcce535fda4d](../../evidence/state_effects-sets-006.md#s-1c43dcce535fda4d)

### observed_connections-009246

```text
(config-pm-dm-ep-adv-per)# default disabled <cr>
```

Handler ` RVA 0x1ACFB9C0 `；selector ` 0 `；EOL ` RVA 0x36DC8FB0 `。

模式根 ` RVA 0x36DC1AE8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-1c43dcce535fda4d](../../evidence/state_effects-sets-006.md#s-1c43dcce535fda4d)

### observed_connections-009252

```text
(config-pm-dm-ep-adv-per)# default interval <number:30..3600> <cr>
```

Handler ` RVA 0x1ACFBA60 `；selector ` 0 `；EOL ` RVA 0x36DC8D28 `。

模式根 ` RVA 0x36DC1AE8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number `  Periodic advertisement interval (seconds)。

[参数 P-9239b3dae0fed22a](../../evidence/parameters-sets-011.md#p-9239b3dae0fed22a) · [状态效果 S-1c43dcce535fda4d](../../evidence/state_effects-sets-006.md#s-1c43dcce535fda4d)

### observed_connections-009248

```text
(config-pm-dm-ep-adv-per)# default minimum-change <number:0..1000000> <cr>
```

Handler ` RVA 0x1ACFBD00 `；selector ` 0 `；EOL ` RVA 0x36DC86F8 `。

模式根 ` RVA 0x36DC1AE8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Periodic advertisement minimum change (uSec)。

[参数 P-ca7c92d34181e004](../../evidence/parameters-sets-015.md#p-ca7c92d34181e004) · [状态效果 S-1c43dcce535fda4d](../../evidence/state_effects-sets-006.md#s-1c43dcce535fda4d)

### observed_connections-009250

```text
(config-pm-dm-ep-adv-per)# default threshold <number:0..100> <cr>
```

Handler ` RVA 0x1ACFBB50 `；selector ` 0 `；EOL ` RVA 0x36DC8A38 `。

模式根 ` RVA 0x36DC1AE8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Periodic advertisement threshold percentage change。

[参数 P-0f8747ef381467d2](../../evidence/parameters-sets-002.md#p-0f8747ef381467d2) · [状态效果 S-1c43dcce535fda4d](../../evidence/state_effects-sets-006.md#s-1c43dcce535fda4d)

### observed_connections-009241

```text
(config-pm-dm-ep-adv-per)# disabled <cr>
```

Handler ` RVA 0x1ACFB9C0 `；selector ` 0 `；EOL ` RVA 0x36DC8FB0 `。

模式根 ` RVA 0x36DC1AE8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-009238

```text
(config-pm-dm-ep-adv-per)# exit <cr>
```

Handler ` RVA 0x1ACFC850 `；selector ` 0 `；EOL ` RVA 0x36DDDA20 `。

模式根 ` RVA 0x36DC1AE8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-02a3afc1950475cf](../../evidence/conditions-sets-001.md#c-02a3afc1950475cf)

### observed_connections-009244

```text
(config-pm-dm-ep-adv-per)# interval <number:30..3600> <cr>
```

Handler ` RVA 0x1ACFBA60 `；selector ` 0 `；EOL ` RVA 0x36DC8D28 `。

模式根 ` RVA 0x36DC1AE8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number `  Periodic advertisement interval (seconds)。

[参数 P-9239b3dae0fed22a](../../evidence/parameters-sets-011.md#p-9239b3dae0fed22a)

### observed_connections-009242

```text
(config-pm-dm-ep-adv-per)# minimum-change <number:0..1000000> <cr>
```

Handler ` RVA 0x1ACFBD00 `；selector ` 0 `；EOL ` RVA 0x36DC86F8 `。

模式根 ` RVA 0x36DC1AE8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Periodic advertisement minimum change (uSec)。

[参数 P-ca7c92d34181e004](../../evidence/parameters-sets-015.md#p-ca7c92d34181e004)

### observed_connections-009239

```text
(config-pm-dm-ep-adv-per)# no <cr>
```

Handler ` RVA 0x1ACFB520 `；selector ` 0 `；EOL ` RVA 0x36DC9258 `。

模式根 ` RVA 0x36DC1AE8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-48f5552db6bf7844](../../evidence/state_effects-sets-016.md#s-48f5552db6bf7844)

### observed_connections-009245

```text
(config-pm-dm-ep-adv-per)# no disabled <cr>
```

Handler ` RVA 0x1ACFB9C0 `；selector ` 0 `；EOL ` RVA 0x36DC8FB0 `。

模式根 ` RVA 0x36DC1AE8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-48f5552db6bf7844](../../evidence/state_effects-sets-016.md#s-48f5552db6bf7844)

### observed_connections-009251

```text
(config-pm-dm-ep-adv-per)# no interval <number:30..3600> <cr>
```

Handler ` RVA 0x1ACFBA60 `；selector ` 0 `；EOL ` RVA 0x36DC8D28 `。

模式根 ` RVA 0x36DC1AE8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number `  Periodic advertisement interval (seconds)。

[参数 P-9239b3dae0fed22a](../../evidence/parameters-sets-011.md#p-9239b3dae0fed22a) · [状态效果 S-48f5552db6bf7844](../../evidence/state_effects-sets-016.md#s-48f5552db6bf7844)

### observed_connections-009247

```text
(config-pm-dm-ep-adv-per)# no minimum-change <number:0..1000000> <cr>
```

Handler ` RVA 0x1ACFBD00 `；selector ` 0 `；EOL ` RVA 0x36DC86F8 `。

模式根 ` RVA 0x36DC1AE8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Periodic advertisement minimum change (uSec)。

[参数 P-ca7c92d34181e004](../../evidence/parameters-sets-015.md#p-ca7c92d34181e004) · [状态效果 S-48f5552db6bf7844](../../evidence/state_effects-sets-016.md#s-48f5552db6bf7844)

### observed_connections-009249

```text
(config-pm-dm-ep-adv-per)# no threshold <number:0..100> <cr>
```

Handler ` RVA 0x1ACFBB50 `；selector ` 0 `；EOL ` RVA 0x36DC8A38 `。

模式根 ` RVA 0x36DC1AE8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Periodic advertisement threshold percentage change。

[参数 P-0f8747ef381467d2](../../evidence/parameters-sets-002.md#p-0f8747ef381467d2) · [状态效果 S-48f5552db6bf7844](../../evidence/state_effects-sets-016.md#s-48f5552db6bf7844)

### observed_connections-009243

```text
(config-pm-dm-ep-adv-per)# threshold <number:0..100> <cr>
```

Handler ` RVA 0x1ACFBB50 `；selector ` 0 `；EOL ` RVA 0x36DC8A38 `。

模式根 ` RVA 0x36DC1AE8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Periodic advertisement threshold percentage change。

[参数 P-0f8747ef381467d2](../../evidence/parameters-sets-002.md#p-0f8747ef381467d2)

### observed_connections-009237

```text
(config-pm-dm-ep-adv-per)# <cr>
```

Handler ` RVA 0x1ACFB520 `；selector ` 0 `；EOL ` RVA 0x36DC9258 `。

模式根 ` RVA 0x36DC1AE8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

