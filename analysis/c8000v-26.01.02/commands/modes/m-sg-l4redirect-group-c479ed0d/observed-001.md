# sg-l4redirect-group · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-009752

```text
(config-sg-l4redirect-group)# default server ip <address> <cr>
```

Handler ` RVA 0x11AA6D50 `；selector ` 6 `；EOL ` RVA 0x355E2F50 `。

模式根 ` RVA 0x355E12C8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IPv4 address。

[参数 P-d977217eeb57c25e](../../evidence/parameters-sets-016.md#p-d977217eeb57c25e) · [状态效果 S-8e366834bcfe9e8c](../../evidence/state_effects-sets-030.md#s-8e366834bcfe9e8c)

### observed_connections-009749

```text
(config-sg-l4redirect-group)# exit <cr>
```

Handler ` RVA 0x11AA2550 `；selector ` 5 `；EOL ` RVA 0x355E4B78 `。

模式根 ` RVA 0x355E12C8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c4e6aea51c596de9](../../evidence/conditions-sets-076.md#c-c4e6aea51c596de9)

### observed_connections-009751

```text
(config-sg-l4redirect-group)# no server ip <address> <cr>
```

Handler ` RVA 0x11AA6D50 `；selector ` 6 `；EOL ` RVA 0x355E2F50 `。

模式根 ` RVA 0x355E12C8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` IPv4 address。

[参数 P-d977217eeb57c25e](../../evidence/parameters-sets-016.md#p-d977217eeb57c25e) · [状态效果 S-e03070af5cf48b4a](../../evidence/state_effects-sets-047.md#s-e03070af5cf48b4a)

### observed_connections-009750

```text
(config-sg-l4redirect-group)# server ip <address> <cr>
```

Handler ` RVA 0x11AA6D50 `；selector ` 6 `；EOL ` RVA 0x355E2F50 `。

模式根 ` RVA 0x355E12C8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IPv4 address。

[参数 P-d977217eeb57c25e](../../evidence/parameters-sets-016.md#p-d977217eeb57c25e)
