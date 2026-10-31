# pm-loss-profile-intf-adv-per · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-009307

```text
(config-pm-lm-intf-adv-per)# default <cr>
```

Handler ` RVA 0x1ACEFD90 `；selector ` 0 `；EOL ` RVA 0x36DC4CB8 `。

模式根 ` RVA 0x36DC1818 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-c8da82e5bd697a9e](../../evidence/state_effects-sets-043.md#s-c8da82e5bd697a9e)

### observed_connections-009310

```text
(config-pm-lm-intf-adv-per)# default interval <number:30..3600> <cr>
```

Handler ` RVA 0x1ACF01C0 `；selector ` 0 `；EOL ` RVA 0x36DC4400 `。

模式根 ` RVA 0x36DC1818 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` interval value in sec。

[参数 P-22673dbf4dd5bf85](../../evidence/parameters-sets-003.md#p-22673dbf4dd5bf85) · [状态效果 S-c8da82e5bd697a9e](../../evidence/state_effects-sets-043.md#s-c8da82e5bd697a9e)

### observed_connections-009305

```text
(config-pm-lm-intf-adv-per)# exit <cr>
```

Handler ` RVA 0x1ACF0D90 `；selector ` 0 `；EOL ` RVA 0x36DD9190 `。

模式根 ` RVA 0x36DC1818 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a983dffe2799fcae](../../evidence/conditions-sets-065.md#c-a983dffe2799fcae)

### observed_connections-009308

```text
(config-pm-lm-intf-adv-per)# interval <number:30..3600> <cr>
```

Handler ` RVA 0x1ACF01C0 `；selector ` 0 `；EOL ` RVA 0x36DC4400 `。

模式根 ` RVA 0x36DC1818 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` interval value in sec。

[参数 P-22673dbf4dd5bf85](../../evidence/parameters-sets-003.md#p-22673dbf4dd5bf85)

### observed_connections-009312

```text
(config-pm-lm-intf-adv-per)# minimum-change <?fixed_number_action@55558c3189d0> <cr>
```

Handler ` RVA 0x1ACEFEE0 `；selector ` 0 `；EOL ` RVA 0x36DC4A10 `。

模式根 ` RVA 0x36DC1818 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[缺口 G-a015f8c397cac157](../../evidence/gaps-sets-006.md#g-a015f8c397cac157)

### observed_connections-009306

```text
(config-pm-lm-intf-adv-per)# no <cr>
```

Handler ` RVA 0x1ACEFD90 `；selector ` 0 `；EOL ` RVA 0x36DC4CB8 `。

模式根 ` RVA 0x36DC1818 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-afdd54795b3052d6](../../evidence/state_effects-sets-037.md#s-afdd54795b3052d6)

### observed_connections-009309

```text
(config-pm-lm-intf-adv-per)# no interval <number:30..3600> <cr>
```

Handler ` RVA 0x1ACF01C0 `；selector ` 0 `；EOL ` RVA 0x36DC4400 `。

模式根 ` RVA 0x36DC1818 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` interval value in sec。

[参数 P-22673dbf4dd5bf85](../../evidence/parameters-sets-003.md#p-22673dbf4dd5bf85) · [状态效果 S-afdd54795b3052d6](../../evidence/state_effects-sets-037.md#s-afdd54795b3052d6)

### observed_connections-009311

```text
(config-pm-lm-intf-adv-per)# threshold <?fixed_number_action@55558c3186d8> <cr>
```

Handler ` RVA 0x1ACF0050 `；selector ` 0 `；EOL ` RVA 0x36DC4740 `。

模式根 ` RVA 0x36DC1818 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[缺口 G-d23069531a7cddcc](../../evidence/gaps-sets-007.md#g-d23069531a7cddcc)

### observed_connections-009304

```text
(config-pm-lm-intf-adv-per)# <cr>
```

Handler ` RVA 0x1ACEFD90 `；selector ` 0 `；EOL ` RVA 0x36DC4CB8 `。

模式根 ` RVA 0x36DC1818 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。
