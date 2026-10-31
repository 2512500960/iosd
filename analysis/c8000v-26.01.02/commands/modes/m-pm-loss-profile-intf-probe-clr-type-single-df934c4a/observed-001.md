# pm-loss-profile-intf-probe-clr-type-single · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-009440

```text
(config-pm-lm-intf-probe-clr-single)# accuracy <?fixed_number_action@55558c319a48> <cr>
```

Handler ` RVA 0x1ACF08C0 `；selector ` 0 `；EOL ` RVA 0x36DC5AB0 `。

模式根 ` RVA 0x36DC18B8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[缺口 G-79e3bbafef882390](../../evidence/gaps-sets-005.md#g-79e3bbafef882390)

### observed_connections-009436

```text
(config-pm-lm-intf-probe-clr-single)# default <cr>
```

Handler ` RVA 0x1ACF0700 `；selector ` 0 `；EOL ` RVA 0x36DC6030 `。

模式根 ` RVA 0x36DC18B8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-7e6119d516de51b4](../../evidence/state_effects-sets-027.md#s-7e6119d516de51b4)

### observed_connections-009439

```text
(config-pm-lm-intf-probe-clr-single)# default max-reordering <number:100..2000> <cr>
```

Handler ` RVA 0x1ACF0A10 `；selector ` 0 `；EOL ` RVA 0x36DC5DA8 `。

模式根 ` RVA 0x36DC18B8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` maximum expected reordering value in miliseconds。

[参数 P-59fd1598f3c3c6cd](../../evidence/parameters-sets-007.md#p-59fd1598f3c3c6cd) · [状态效果 S-7e6119d516de51b4](../../evidence/state_effects-sets-027.md#s-7e6119d516de51b4)

### observed_connections-009434

```text
(config-pm-lm-intf-probe-clr-single)# exit <cr>
```

Handler ` RVA 0x1ACF0F50 `；selector ` 0 `；EOL ` RVA 0x36DDA1B0 `。

模式根 ` RVA 0x36DC18B8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3bb23ed9f886d2ce](../../evidence/conditions-sets-023.md#c-3bb23ed9f886d2ce)

### observed_connections-009437

```text
(config-pm-lm-intf-probe-clr-single)# max-reordering <number:100..2000> <cr>
```

Handler ` RVA 0x1ACF0A10 `；selector ` 0 `；EOL ` RVA 0x36DC5DA8 `。

模式根 ` RVA 0x36DC18B8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` maximum expected reordering value in miliseconds。

[参数 P-59fd1598f3c3c6cd](../../evidence/parameters-sets-007.md#p-59fd1598f3c3c6cd)

### observed_connections-009435

```text
(config-pm-lm-intf-probe-clr-single)# no <cr>
```

Handler ` RVA 0x1ACF0700 `；selector ` 0 `；EOL ` RVA 0x36DC6030 `。

模式根 ` RVA 0x36DC18B8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-e441cb1605825129](../../evidence/state_effects-sets-048.md#s-e441cb1605825129)

### observed_connections-009438

```text
(config-pm-lm-intf-probe-clr-single)# no max-reordering <number:100..2000> <cr>
```

Handler ` RVA 0x1ACF0A10 `；selector ` 0 `；EOL ` RVA 0x36DC5DA8 `。

模式根 ` RVA 0x36DC18B8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` maximum expected reordering value in miliseconds。

[参数 P-59fd1598f3c3c6cd](../../evidence/parameters-sets-007.md#p-59fd1598f3c3c6cd) · [状态效果 S-e441cb1605825129](../../evidence/state_effects-sets-048.md#s-e441cb1605825129)

### observed_connections-009433

```text
(config-pm-lm-intf-probe-clr-single)# <cr>
```

Handler ` RVA 0x1ACF0700 `；selector ` 0 `；EOL ` RVA 0x36DC6030 `。

模式根 ` RVA 0x36DC18B8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

