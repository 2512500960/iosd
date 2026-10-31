# Ingress-class-map · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-009728

```text
(config-ing-class-map)# default exit <cr>
```

Handler ` RVA 0xE943690 `；selector ` 0 `；EOL ` RVA 0x34347708 `。

模式根 ` RVA 0x34347620 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-9a6ec2ec499eda79](../../evidence/state_effects-sets-033.md#s-9a6ec2ec499eda79)

### observed_connections-009731

```text
(config-ing-class-map)# default map ip precedence-based <cr>
```

Handler ` RVA 0xE948AC0 `；selector ` 0 `；EOL ` RVA 0x3434BF88 `。

模式根 ` RVA 0x34347620 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-30b15fefb0cefb81](../../evidence/state_effects-sets-011.md#s-30b15fefb0cefb81)

### observed_connections-009726

```text
(config-ing-class-map)# exit <cr>
```

Handler ` RVA 0xE943690 `；selector ` 0 `；EOL ` RVA 0x34347708 `。

模式根 ` RVA 0x34347620 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-009729

```text
(config-ing-class-map)# map ip precedence-based <cr>
```

Handler ` RVA 0xE948AC0 `；selector ` 0 `；EOL ` RVA 0x3434BF88 `。

模式根 ` RVA 0x34347620 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[状态效果 S-3d463cc315edddd7](../../evidence/state_effects-sets-013.md#s-3d463cc315edddd7)

### observed_connections-009732

```text
(config-ing-class-map)# map ipv6 tc <?common_dscp_value_action@5555898a08e8> <?common_dscp_value_action@5555898a0980> queue 0 <cr>
```

Handler ` RVA 0xE948AC0 `；selector ` 0 `；EOL ` RVA 0x3434BF88 `。

模式根 ` RVA 0x34347620 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[缺口 G-55b08aeeea68d82d](../../evidence/gaps-sets-003.md#g-55b08aeeea68d82d) · [状态效果 S-3373c6c81a7d7798](../../evidence/state_effects-sets-011.md#s-3373c6c81a7d7798)

### observed_connections-009727

```text
(config-ing-class-map)# no exit <cr>
```

Handler ` RVA 0xE943690 `；selector ` 0 `；EOL ` RVA 0x34347708 `。

模式根 ` RVA 0x34347620 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-0e9d5d60cc18e166](../../evidence/state_effects-sets-003.md#s-0e9d5d60cc18e166)

### observed_connections-009730

```text
(config-ing-class-map)# no map ip precedence-based <cr>
```

Handler ` RVA 0xE948AC0 `；selector ` 0 `；EOL ` RVA 0x3434BF88 `。

模式根 ` RVA 0x34347620 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-1c0d20fa1e9e088b](../../evidence/state_effects-sets-006.md#s-1c0d20fa1e9e088b)
