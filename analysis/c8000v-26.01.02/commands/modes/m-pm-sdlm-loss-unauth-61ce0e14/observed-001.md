# pm-sdlm-loss-unauth · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-009685

```text
(config-pm-sdlm-loss-unauth)# default <cr>
```

Handler ` RVA 0x1ACF36F0 `；selector ` 0 `；EOL ` RVA 0x36DD62E0 `。

模式根 ` RVA 0x36DC1D90 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-8660e12ebbd96d47](../../evidence/state_effects-sets-028.md#s-8660e12ebbd96d47)

### observed_connections-009688

```text
(config-pm-sdlm-loss-unauth)# default querier-dst-port <number:1024..14999> <cr>
```

Handler ` RVA 0x1ACF3ED0 `；selector ` 0 `；EOL ` RVA 0x36DD6608 `。

模式根 ` RVA 0x36DC1D90 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Port number。

[条件 C-54a4bb218b1fa20d](../../evidence/conditions-sets-033.md#c-54a4bb218b1fa20d) · [参数 P-4ec43d1805d651a6](../../evidence/parameters-sets-006.md#p-4ec43d1805d651a6) · [状态效果 S-13c37181f4205793](../../evidence/state_effects-sets-005.md#s-13c37181f4205793)

### observed_connections-009683

```text
(config-pm-sdlm-loss-unauth)# exit <cr>
```

Handler ` RVA 0x1ACF4190 `；selector ` 0 `；EOL ` RVA 0x36DE1EA8 `。

模式根 ` RVA 0x36DC1D90 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d5518f10556e6ca9](../../evidence/conditions-sets-082.md#c-d5518f10556e6ca9)

### observed_connections-009684

```text
(config-pm-sdlm-loss-unauth)# no <cr>
```

Handler ` RVA 0x1ACF36F0 `；selector ` 0 `；EOL ` RVA 0x36DD62E0 `。

模式根 ` RVA 0x36DC1D90 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-221e07b22662196e](../../evidence/state_effects-sets-008.md#s-221e07b22662196e)

### observed_connections-009687

```text
(config-pm-sdlm-loss-unauth)# no querier-dst-port <number:1024..14999> <cr>
```

Handler ` RVA 0x1ACF3ED0 `；selector ` 0 `；EOL ` RVA 0x36DD6608 `。

模式根 ` RVA 0x36DC1D90 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Port number。

[条件 C-54a4bb218b1fa20d](../../evidence/conditions-sets-033.md#c-54a4bb218b1fa20d) · [参数 P-4ec43d1805d651a6](../../evidence/parameters-sets-006.md#p-4ec43d1805d651a6) · [状态效果 S-620be4ceabc73df0](../../evidence/state_effects-sets-021.md#s-620be4ceabc73df0)

### observed_connections-009686

```text
(config-pm-sdlm-loss-unauth)# querier-dst-port <number:1024..14999> <cr>
```

Handler ` RVA 0x1ACF3ED0 `；selector ` 0 `；EOL ` RVA 0x36DD6608 `。

模式根 ` RVA 0x36DC1D90 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Port number。

[条件 C-54a4bb218b1fa20d](../../evidence/conditions-sets-033.md#c-54a4bb218b1fa20d) · [参数 P-4ec43d1805d651a6](../../evidence/parameters-sets-006.md#p-4ec43d1805d651a6) · [状态效果 S-54849f31e65277c5](../../evidence/state_effects-sets-018.md#s-54849f31e65277c5)

### observed_connections-009682

```text
(config-pm-sdlm-loss-unauth)# <cr>
```

Handler ` RVA 0x1ACF36F0 `；selector ` 0 `；EOL ` RVA 0x36DD62E0 `。

模式根 ` RVA 0x36DC1D90 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。
