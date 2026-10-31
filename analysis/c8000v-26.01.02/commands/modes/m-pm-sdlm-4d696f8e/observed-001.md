# pm-sdlm · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-009355

```text
(config-pm-sdlm)# default <cr>
```

Handler ` RVA 0x1ACEF690 `；selector ` 0 `；EOL ` RVA 0x36DD6BA0 `。

模式根 ` RVA 0x36DC1D40 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-302b6eba441412ca](../../evidence/state_effects-sets-011.md#s-302b6eba441412ca)

### observed_connections-009359

```text
(config-pm-sdlm)# default measurement loss <cr>
```

Handler ` RVA 0x1ACF35D0 `；selector ` 0 `；EOL ` RVA 0x36DD6920 `。

模式根 ` RVA 0x36DC1D40 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-302b6eba441412ca](../../evidence/state_effects-sets-011.md#s-302b6eba441412ca)

### observed_connections-009361

```text
(config-pm-sdlm)# default measurement loss unauthenticated <cr>
```

Handler ` RVA 0x1ACF36F0 `；selector ` 0 `；EOL ` RVA 0x36DD62E0 `。

模式根 ` RVA 0x36DC1D40 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-302b6eba441412ca](../../evidence/state_effects-sets-011.md#s-302b6eba441412ca)

### observed_connections-009364

```text
(config-pm-sdlm)# default measurement loss unauthenticated querier-dst-port <number:1024..14999> <cr>
```

Handler ` RVA 0x1ACF3ED0 `；selector ` 0 `；EOL ` RVA 0x36DD6608 `。

模式根 ` RVA 0x36DC1D40 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Port number。

[条件 C-54a4bb218b1fa20d](../../evidence/conditions-sets-033.md#c-54a4bb218b1fa20d) · [参数 P-4ec43d1805d651a6](../../evidence/parameters-sets-006.md#p-4ec43d1805d651a6) · [状态效果 S-141a4188c9e7f9a3](../../evidence/state_effects-sets-005.md#s-141a4188c9e7f9a3)

### observed_connections-009353

```text
(config-pm-sdlm)# exit <cr>
```

Handler ` RVA 0x1ACF3680 `；selector ` 0 `；EOL ` RVA 0x36DE1698 `。

模式根 ` RVA 0x36DC1D40 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-020c72f89689fe11](../../evidence/conditions-sets-001.md#c-020c72f89689fe11)

### observed_connections-009356

```text
(config-pm-sdlm)# measurement loss <cr>
```

Handler ` RVA 0x1ACF35D0 `；selector ` 0 `；EOL ` RVA 0x36DD6920 `。

模式根 ` RVA 0x36DC1D40 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-009358

```text
(config-pm-sdlm)# measurement loss unauthenticated <cr>
```

Handler ` RVA 0x1ACF36F0 `；selector ` 0 `；EOL ` RVA 0x36DD62E0 `。

模式根 ` RVA 0x36DC1D40 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-009362

```text
(config-pm-sdlm)# measurement loss unauthenticated querier-dst-port <number:1024..14999> <cr>
```

Handler ` RVA 0x1ACF3ED0 `；selector ` 0 `；EOL ` RVA 0x36DD6608 `。

模式根 ` RVA 0x36DC1D40 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Port number。

[条件 C-54a4bb218b1fa20d](../../evidence/conditions-sets-033.md#c-54a4bb218b1fa20d) · [参数 P-4ec43d1805d651a6](../../evidence/parameters-sets-006.md#p-4ec43d1805d651a6) · [状态效果 S-54849f31e65277c5](../../evidence/state_effects-sets-018.md#s-54849f31e65277c5)

### observed_connections-009354

```text
(config-pm-sdlm)# no <cr>
```

Handler ` RVA 0x1ACEF690 `；selector ` 0 `；EOL ` RVA 0x36DD6BA0 `。

模式根 ` RVA 0x36DC1D40 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-35f771c23c66be9d](../../evidence/state_effects-sets-012.md#s-35f771c23c66be9d)

### observed_connections-009357

```text
(config-pm-sdlm)# no measurement loss <cr>
```

Handler ` RVA 0x1ACF35D0 `；selector ` 0 `；EOL ` RVA 0x36DD6920 `。

模式根 ` RVA 0x36DC1D40 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-35f771c23c66be9d](../../evidence/state_effects-sets-012.md#s-35f771c23c66be9d)

### observed_connections-009360

```text
(config-pm-sdlm)# no measurement loss unauthenticated <cr>
```

Handler ` RVA 0x1ACF36F0 `；selector ` 0 `；EOL ` RVA 0x36DD62E0 `。

模式根 ` RVA 0x36DC1D40 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-35f771c23c66be9d](../../evidence/state_effects-sets-012.md#s-35f771c23c66be9d)

### observed_connections-009363

```text
(config-pm-sdlm)# no measurement loss unauthenticated querier-dst-port <number:1024..14999> <cr>
```

Handler ` RVA 0x1ACF3ED0 `；selector ` 0 `；EOL ` RVA 0x36DD6608 `。

模式根 ` RVA 0x36DC1D40 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Port number。

[条件 C-54a4bb218b1fa20d](../../evidence/conditions-sets-033.md#c-54a4bb218b1fa20d) · [参数 P-4ec43d1805d651a6](../../evidence/parameters-sets-006.md#p-4ec43d1805d651a6) · [状态效果 S-d7d7bb7249bb291c](../../evidence/state_effects-sets-046.md#s-d7d7bb7249bb291c)

### observed_connections-009352

```text
(config-pm-sdlm)# <cr>
```

Handler ` RVA 0x1ACEF690 `；selector ` 0 `；EOL ` RVA 0x36DD6BA0 `。

模式根 ` RVA 0x36DC1D40 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。
