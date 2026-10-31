# pm-endpoint-seglist · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-009512

```text
(config-pm-ep-sl)# default <cr>
```

Handler ` RVA 0x1ACFA770 `；selector ` 0 `；EOL ` RVA 0x36DC3988 `。

模式根 ` RVA 0x36DC1DE0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-6a2fe903f9928757](../../evidence/state_effects-sets-023.md#s-6a2fe903f9928757)

### observed_connections-009516

```text
(config-pm-ep-sl)# default forward-path <string> <cr>
```

Handler ` RVA 0x1ACFAB50 `；selector ` 0 `；EOL ` RVA 0x36DC3420 `。

模式根 ` RVA 0x36DC1DE0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Identifying name for segment-list。

[参数 P-ad1fa3ff5e2c2b78](../../evidence/parameters-sets-013.md#p-ad1fa3ff5e2c2b78) · [状态效果 S-6a2fe903f9928757](../../evidence/state_effects-sets-023.md#s-6a2fe903f9928757)

### observed_connections-009518

```text
(config-pm-ep-sl)# default reverse-path <string> <cr>
```

Handler ` RVA 0x1ACFACB0 `；selector ` 0 `；EOL ` RVA 0x36DC3708 `。

模式根 ` RVA 0x36DC1DE0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Identifying name for reverse path segment-list。

[参数 P-1d628917302bc153](../../evidence/parameters-sets-003.md#p-1d628917302bc153) · [状态效果 S-6a2fe903f9928757](../../evidence/state_effects-sets-023.md#s-6a2fe903f9928757)

### observed_connections-009510

```text
(config-pm-ep-sl)# exit <cr>
```

Handler ` RVA 0x1ACF3A30 `；selector ` 0 `；EOL ` RVA 0x36DE26B8 `。

模式根 ` RVA 0x36DC1DE0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4242e3119cbd7e7c](../../evidence/conditions-sets-026.md#c-4242e3119cbd7e7c)

### observed_connections-009513

```text
(config-pm-ep-sl)# forward-path <string> <cr>
```

Handler ` RVA 0x1ACFAB50 `；selector ` 0 `；EOL ` RVA 0x36DC3420 `。

模式根 ` RVA 0x36DC1DE0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Identifying name for segment-list。

[参数 P-ad1fa3ff5e2c2b78](../../evidence/parameters-sets-013.md#p-ad1fa3ff5e2c2b78)

### observed_connections-009511

```text
(config-pm-ep-sl)# no <cr>
```

Handler ` RVA 0x1ACFA770 `；selector ` 0 `；EOL ` RVA 0x36DC3988 `。

模式根 ` RVA 0x36DC1DE0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-71f5a019618013b1](../../evidence/state_effects-sets-024.md#s-71f5a019618013b1)

### observed_connections-009515

```text
(config-pm-ep-sl)# no forward-path <string> <cr>
```

Handler ` RVA 0x1ACFAB50 `；selector ` 0 `；EOL ` RVA 0x36DC3420 `。

模式根 ` RVA 0x36DC1DE0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Identifying name for segment-list。

[参数 P-ad1fa3ff5e2c2b78](../../evidence/parameters-sets-013.md#p-ad1fa3ff5e2c2b78) · [状态效果 S-71f5a019618013b1](../../evidence/state_effects-sets-024.md#s-71f5a019618013b1)

### observed_connections-009517

```text
(config-pm-ep-sl)# no reverse-path <string> <cr>
```

Handler ` RVA 0x1ACFACB0 `；selector ` 0 `；EOL ` RVA 0x36DC3708 `。

模式根 ` RVA 0x36DC1DE0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Identifying name for reverse path segment-list。

[参数 P-1d628917302bc153](../../evidence/parameters-sets-003.md#p-1d628917302bc153) · [状态效果 S-71f5a019618013b1](../../evidence/state_effects-sets-024.md#s-71f5a019618013b1)

### observed_connections-009514

```text
(config-pm-ep-sl)# reverse-path <string> <cr>
```

Handler ` RVA 0x1ACFACB0 `；selector ` 0 `；EOL ` RVA 0x36DC3708 `。

模式根 ` RVA 0x36DC1DE0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Identifying name for reverse path segment-list。

[参数 P-1d628917302bc153](../../evidence/parameters-sets-003.md#p-1d628917302bc153)

### observed_connections-009509

```text
(config-pm-ep-sl)# <cr>
```

Handler ` RVA 0x1ACFA770 `；selector ` 0 `；EOL ` RVA 0x36DC3988 `。

模式根 ` RVA 0x36DC1DE0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。
