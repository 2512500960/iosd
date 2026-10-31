# pm-delay-profile-ep-advertisement-accelerated · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-009454

```text
(config-pm-dm-ep-adv-acc)# default <cr>
```

Handler ` RVA 0x1ACFB3D0 `；selector ` 0 `；EOL ` RVA 0x36DC83D8 `。

模式根 ` RVA 0x36DC1A20 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-19cc024a3b2e3e8b](../../evidence/state_effects-sets-006.md#s-19cc024a3b2e3e8b)

### observed_connections-009458

```text
(config-pm-dm-ep-adv-acc)# default minimum-change <number:0..1000000> <cr>
```

Handler ` RVA 0x1ACFB890 `；selector ` 0 `；EOL ` RVA 0x36DC7E28 `。

模式根 ` RVA 0x36DC1A20 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Accelerated advertisement minimum change (uSec)。

[参数 P-9f6f6ba2d130deb9](../../evidence/parameters-sets-012.md#p-9f6f6ba2d130deb9) · [状态效果 S-19cc024a3b2e3e8b](../../evidence/state_effects-sets-006.md#s-19cc024a3b2e3e8b)

### observed_connections-009460

```text
(config-pm-dm-ep-adv-acc)# default threshold <number:0..100> <cr>
```

Handler ` RVA 0x1ACFB760 `；selector ` 0 `；EOL ` RVA 0x36DC8140 `。

模式根 ` RVA 0x36DC1A20 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Accelerated advertisement threshold percentage change。

[参数 P-2bf284102dc3b5f7](../../evidence/parameters-sets-004.md#p-2bf284102dc3b5f7) · [状态效果 S-19cc024a3b2e3e8b](../../evidence/state_effects-sets-006.md#s-19cc024a3b2e3e8b)

### observed_connections-009452

```text
(config-pm-dm-ep-adv-acc)# exit <cr>
```

Handler ` RVA 0x1ACFC770 `；selector ` 0 `；EOL ` RVA 0x36DDC5F8 `。

模式根 ` RVA 0x36DC1A20 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ac21d465a81fa178](../../evidence/conditions-sets-067.md#c-ac21d465a81fa178)

### observed_connections-009455

```text
(config-pm-dm-ep-adv-acc)# minimum-change <number:0..1000000> <cr>
```

Handler ` RVA 0x1ACFB890 `；selector ` 0 `；EOL ` RVA 0x36DC7E28 `。

模式根 ` RVA 0x36DC1A20 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Accelerated advertisement minimum change (uSec)。

[参数 P-9f6f6ba2d130deb9](../../evidence/parameters-sets-012.md#p-9f6f6ba2d130deb9)

### observed_connections-009453

```text
(config-pm-dm-ep-adv-acc)# no <cr>
```

Handler ` RVA 0x1ACFB3D0 `；selector ` 0 `；EOL ` RVA 0x36DC83D8 `。

模式根 ` RVA 0x36DC1A20 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-549465386868d75f](../../evidence/state_effects-sets-018.md#s-549465386868d75f)

### observed_connections-009457

```text
(config-pm-dm-ep-adv-acc)# no minimum-change <number:0..1000000> <cr>
```

Handler ` RVA 0x1ACFB890 `；selector ` 0 `；EOL ` RVA 0x36DC7E28 `。

模式根 ` RVA 0x36DC1A20 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Accelerated advertisement minimum change (uSec)。

[参数 P-9f6f6ba2d130deb9](../../evidence/parameters-sets-012.md#p-9f6f6ba2d130deb9) · [状态效果 S-549465386868d75f](../../evidence/state_effects-sets-018.md#s-549465386868d75f)

### observed_connections-009459

```text
(config-pm-dm-ep-adv-acc)# no threshold <number:0..100> <cr>
```

Handler ` RVA 0x1ACFB760 `；selector ` 0 `；EOL ` RVA 0x36DC8140 `。

模式根 ` RVA 0x36DC1A20 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Accelerated advertisement threshold percentage change。

[参数 P-2bf284102dc3b5f7](../../evidence/parameters-sets-004.md#p-2bf284102dc3b5f7) · [状态效果 S-549465386868d75f](../../evidence/state_effects-sets-018.md#s-549465386868d75f)

### observed_connections-009456

```text
(config-pm-dm-ep-adv-acc)# threshold <number:0..100> <cr>
```

Handler ` RVA 0x1ACFB760 `；selector ` 0 `；EOL ` RVA 0x36DC8140 `。

模式根 ` RVA 0x36DC1A20 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Accelerated advertisement threshold percentage change。

[参数 P-2bf284102dc3b5f7](../../evidence/parameters-sets-004.md#p-2bf284102dc3b5f7)

### observed_connections-009451

```text
(config-pm-dm-ep-adv-acc)# <cr>
```

Handler ` RVA 0x1ACFB3D0 `；selector ` 0 `；EOL ` RVA 0x36DC83D8 `。

模式根 ` RVA 0x36DC1A20 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

