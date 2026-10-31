# pm-loss-profile-intf-adv-ac · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-009666

```text
(config-pm-lm-intf-adv-ac)# default <cr>
```

Handler ` RVA 0x1ACEFE40 `；selector ` 0 `；EOL ` RVA 0x36DC5010 `。

模式根 ` RVA 0x36DC1840 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-f0c143ce938b056d](../../evidence/state_effects-sets-051.md#s-f0c143ce938b056d)

### observed_connections-009664

```text
(config-pm-lm-intf-adv-ac)# exit <cr>
```

Handler ` RVA 0x1ACF0E00 `；selector ` 0 `；EOL ` RVA 0x36DD9598 `。

模式根 ` RVA 0x36DC1840 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6f3318d2094aa85d](../../evidence/conditions-sets-043.md#c-6f3318d2094aa85d)

### observed_connections-009667

```text
(config-pm-lm-intf-adv-ac)# lower-bound <?fixed_number_action@55558c319278> <cr>
```

Handler ` RVA 0x1ACF0FC0 `；selector ` 0 `；EOL ` RVA 0x36DC5340 `。

模式根 ` RVA 0x36DC1840 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-91246437bc3cd7b8](../../evidence/conditions-sets-056.md#c-91246437bc3cd7b8) · [缺口 G-130b4b6e18f5e19b](../../evidence/gaps-sets-001.md#g-130b4b6e18f5e19b) · [状态效果 S-c580c67c997b0624](../../evidence/state_effects-sets-042.md#s-c580c67c997b0624)

### observed_connections-009665

```text
(config-pm-lm-intf-adv-ac)# no <cr>
```

Handler ` RVA 0x1ACEFE40 `；selector ` 0 `；EOL ` RVA 0x36DC5010 `。

模式根 ` RVA 0x36DC1840 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-dc6ee80ab9fdce40](../../evidence/state_effects-sets-047.md#s-dc6ee80ab9fdce40)

### observed_connections-009663

```text
(config-pm-lm-intf-adv-ac)# <cr>
```

Handler ` RVA 0x1ACEFE40 `；selector ` 0 `；EOL ` RVA 0x36DC5010 `。

模式根 ` RVA 0x36DC1840 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。
