# pm-loss-profile-intf-probe-clr · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-009211

```text
(config-pm-lm-intf-probe-clr)# default <cr>
```

Handler ` RVA 0x1ACF0550 `；selector ` 0 `；EOL ` RVA 0x36DC65A8 `。

模式根 ` RVA 0x36DC1890 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-e80bfe0921d99874](../../evidence/state_effects-sets-049.md#s-e80bfe0921d99874)

### observed_connections-009217

```text
(config-pm-lm-intf-probe-clr)# default dual-color gre <cr>
```

Handler ` RVA 0x1ACF0B20 `；selector ` 0 `；EOL ` RVA 0x36DC6318 `。

模式根 ` RVA 0x36DC1890 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-e80bfe0921d99874](../../evidence/state_effects-sets-049.md#s-e80bfe0921d99874)

### observed_connections-009214

```text
(config-pm-lm-intf-probe-clr)# default single-color <cr>
```

Handler ` RVA 0x1ACF0700 `；selector ` 0 `；EOL ` RVA 0x36DC6030 `。

模式根 ` RVA 0x36DC1890 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-e80bfe0921d99874](../../evidence/state_effects-sets-049.md#s-e80bfe0921d99874)

### observed_connections-009219

```text
(config-pm-lm-intf-probe-clr)# default single-color max-reordering <number:100..2000> <cr>
```

Handler ` RVA 0x1ACF0A10 `；selector ` 0 `；EOL ` RVA 0x36DC5DA8 `。

模式根 ` RVA 0x36DC1890 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` maximum expected reordering value in miliseconds。

[参数 P-59fd1598f3c3c6cd](../../evidence/parameters-sets-007.md#p-59fd1598f3c3c6cd) · [状态效果 S-e80bfe0921d99874](../../evidence/state_effects-sets-049.md#s-e80bfe0921d99874)

### observed_connections-009212

```text
(config-pm-lm-intf-probe-clr)# dual-color gre <cr>
```

Handler ` RVA 0x1ACF0B20 `；selector ` 0 `；EOL ` RVA 0x36DC6318 `。

模式根 ` RVA 0x36DC1890 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-009208

```text
(config-pm-lm-intf-probe-clr)# exit <cr>
```

Handler ` RVA 0x1ACF0EE0 `；selector ` 0 `；EOL ` RVA 0x36DD9DA8 `。

模式根 ` RVA 0x36DC1890 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9ff6ee056c14f9aa](../../evidence/conditions-sets-062.md#c-9ff6ee056c14f9aa)

### observed_connections-009209

```text
(config-pm-lm-intf-probe-clr)# no <cr>
```

Handler ` RVA 0x1ACF0550 `；selector ` 0 `；EOL ` RVA 0x36DC65A8 `。

模式根 ` RVA 0x36DC1890 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-bfef9c416e065196](../../evidence/state_effects-sets-041.md#s-bfef9c416e065196)

### observed_connections-009215

```text
(config-pm-lm-intf-probe-clr)# no dual-color gre <cr>
```

Handler ` RVA 0x1ACF0B20 `；selector ` 0 `；EOL ` RVA 0x36DC6318 `。

模式根 ` RVA 0x36DC1890 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-bfef9c416e065196](../../evidence/state_effects-sets-041.md#s-bfef9c416e065196)

### observed_connections-009213

```text
(config-pm-lm-intf-probe-clr)# no single-color <cr>
```

Handler ` RVA 0x1ACF0700 `；selector ` 0 `；EOL ` RVA 0x36DC6030 `。

模式根 ` RVA 0x36DC1890 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-bfef9c416e065196](../../evidence/state_effects-sets-041.md#s-bfef9c416e065196)

### observed_connections-009218

```text
(config-pm-lm-intf-probe-clr)# no single-color max-reordering <number:100..2000> <cr>
```

Handler ` RVA 0x1ACF0A10 `；selector ` 0 `；EOL ` RVA 0x36DC5DA8 `。

模式根 ` RVA 0x36DC1890 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` maximum expected reordering value in miliseconds。

[参数 P-59fd1598f3c3c6cd](../../evidence/parameters-sets-007.md#p-59fd1598f3c3c6cd) · [状态效果 S-bfef9c416e065196](../../evidence/state_effects-sets-041.md#s-bfef9c416e065196)

### observed_connections-009210

```text
(config-pm-lm-intf-probe-clr)# single-color <cr>
```

Handler ` RVA 0x1ACF0700 `；selector ` 0 `；EOL ` RVA 0x36DC6030 `。

模式根 ` RVA 0x36DC1890 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-009220

```text
(config-pm-lm-intf-probe-clr)# single-color accuracy <?fixed_number_action@55558c319a48> <cr>
```

Handler ` RVA 0x1ACF08C0 `；selector ` 0 `；EOL ` RVA 0x36DC5AB0 `。

模式根 ` RVA 0x36DC1890 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[缺口 G-79e3bbafef882390](../../evidence/gaps-sets-005.md#g-79e3bbafef882390)

### observed_connections-009216

```text
(config-pm-lm-intf-probe-clr)# single-color max-reordering <number:100..2000> <cr>
```

Handler ` RVA 0x1ACF0A10 `；selector ` 0 `；EOL ` RVA 0x36DC5DA8 `。

模式根 ` RVA 0x36DC1890 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` maximum expected reordering value in miliseconds。

[参数 P-59fd1598f3c3c6cd](../../evidence/parameters-sets-007.md#p-59fd1598f3c3c6cd)

### observed_connections-009207

```text
(config-pm-lm-intf-probe-clr)# <cr>
```

Handler ` RVA 0x1ACF0550 `；selector ` 0 `；EOL ` RVA 0x36DC65A8 `。

模式根 ` RVA 0x36DC1890 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。
