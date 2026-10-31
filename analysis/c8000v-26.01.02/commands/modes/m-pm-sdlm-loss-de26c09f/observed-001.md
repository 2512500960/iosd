# pm-sdlm-loss · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-009503

```text
(config-pm-sdlm-loss)# default <cr>
```

Handler ` RVA 0x1ACF35D0 `；selector ` 0 `；EOL ` RVA 0x36DD6920 `。

模式根 ` RVA 0x36DC1D68 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-400f33616daee2ae](../../evidence/state_effects-sets-014.md#s-400f33616daee2ae)

### observed_connections-009505

```text
(config-pm-sdlm-loss)# default unauthenticated <cr>
```

Handler ` RVA 0x1ACF36F0 `；selector ` 0 `；EOL ` RVA 0x36DD62E0 `。

模式根 ` RVA 0x36DC1D68 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-400f33616daee2ae](../../evidence/state_effects-sets-014.md#s-400f33616daee2ae)

### observed_connections-009508

```text
(config-pm-sdlm-loss)# default unauthenticated querier-dst-port <number:1024..14999> <cr>
```

Handler ` RVA 0x1ACF3ED0 `；selector ` 0 `；EOL ` RVA 0x36DD6608 `。

模式根 ` RVA 0x36DC1D68 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Port number。

[条件 C-54a4bb218b1fa20d](../../evidence/conditions-sets-033.md#c-54a4bb218b1fa20d) · [参数 P-4ec43d1805d651a6](../../evidence/parameters-sets-006.md#p-4ec43d1805d651a6) · [状态效果 S-5ab6ecb173901e5f](../../evidence/state_effects-sets-020.md#s-5ab6ecb173901e5f)

### observed_connections-009500

```text
(config-pm-sdlm-loss)# exit <cr>
```

Handler ` RVA 0x1ACF3910 `；selector ` 0 `；EOL ` RVA 0x36DE1AA0 `。

模式根 ` RVA 0x36DC1D68 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-aa84deb40fe50881](../../evidence/conditions-sets-066.md#c-aa84deb40fe50881)

### observed_connections-009501

```text
(config-pm-sdlm-loss)# no <cr>
```

Handler ` RVA 0x1ACF35D0 `；selector ` 0 `；EOL ` RVA 0x36DD6920 `。

模式根 ` RVA 0x36DC1D68 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-05b69b13150a71ba](../../evidence/state_effects-sets-002.md#s-05b69b13150a71ba)

### observed_connections-009504

```text
(config-pm-sdlm-loss)# no unauthenticated <cr>
```

Handler ` RVA 0x1ACF36F0 `；selector ` 0 `；EOL ` RVA 0x36DD62E0 `。

模式根 ` RVA 0x36DC1D68 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-05b69b13150a71ba](../../evidence/state_effects-sets-002.md#s-05b69b13150a71ba)

### observed_connections-009507

```text
(config-pm-sdlm-loss)# no unauthenticated querier-dst-port <number:1024..14999> <cr>
```

Handler ` RVA 0x1ACF3ED0 `；selector ` 0 `；EOL ` RVA 0x36DD6608 `。

模式根 ` RVA 0x36DC1D68 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Port number。

[条件 C-54a4bb218b1fa20d](../../evidence/conditions-sets-033.md#c-54a4bb218b1fa20d) · [参数 P-4ec43d1805d651a6](../../evidence/parameters-sets-006.md#p-4ec43d1805d651a6) · [状态效果 S-aefbc403282e1862](../../evidence/state_effects-sets-037.md#s-aefbc403282e1862)

### observed_connections-009502

```text
(config-pm-sdlm-loss)# unauthenticated <cr>
```

Handler ` RVA 0x1ACF36F0 `；selector ` 0 `；EOL ` RVA 0x36DD62E0 `。

模式根 ` RVA 0x36DC1D68 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-009506

```text
(config-pm-sdlm-loss)# unauthenticated querier-dst-port <number:1024..14999> <cr>
```

Handler ` RVA 0x1ACF3ED0 `；selector ` 0 `；EOL ` RVA 0x36DD6608 `。

模式根 ` RVA 0x36DC1D68 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Port number。

[条件 C-54a4bb218b1fa20d](../../evidence/conditions-sets-033.md#c-54a4bb218b1fa20d) · [参数 P-4ec43d1805d651a6](../../evidence/parameters-sets-006.md#p-4ec43d1805d651a6) · [状态效果 S-54849f31e65277c5](../../evidence/state_effects-sets-018.md#s-54849f31e65277c5)

### observed_connections-009499

```text
(config-pm-sdlm-loss)# <cr>
```

Handler ` RVA 0x1ACF35D0 `；selector ` 0 `；EOL ` RVA 0x36DD6920 `。

模式根 ` RVA 0x36DC1D68 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。
