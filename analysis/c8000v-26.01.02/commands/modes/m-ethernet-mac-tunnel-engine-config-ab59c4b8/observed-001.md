# ethernet-mac-tunnel-engine-config · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-009537

```text
(config-tunnel-eng)# default exit <cr>
```

Handler ` RVA 0xC010CB0 `；selector ` 0 `；EOL ` RVA 0x339845B0 `。

模式根 ` RVA 0x33984560 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-89fd68b32af81c3c](../../evidence/state_effects-sets-029.md#s-89fd68b32af81c3c)

### observed_connections-009540

```text
(config-tunnel-eng)# default mac-address source <address> <cr>
```

Handler ` RVA 0xC010D20 `；selector ` 5 `；EOL ` RVA 0x33984968 `。

模式根 ` RVA 0x33984560 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` User defined source mac address for tunnel engine。

[参数 P-86b39006dd52578f](../../evidence/parameters-sets-010.md#p-86b39006dd52578f) · [状态效果 S-89fd68b32af81c3c](../../evidence/state_effects-sets-029.md#s-89fd68b32af81c3c)

### observed_connections-009535

```text
(config-tunnel-eng)# exit <cr>
```

Handler ` RVA 0xC010CB0 `；selector ` 0 `；EOL ` RVA 0x339845B0 `。

模式根 ` RVA 0x33984560 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-009538

```text
(config-tunnel-eng)# mac-address source <address> <cr>
```

Handler ` RVA 0xC010D20 `；selector ` 5 `；EOL ` RVA 0x33984968 `。

模式根 ` RVA 0x33984560 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` User defined source mac address for tunnel engine。

[参数 P-86b39006dd52578f](../../evidence/parameters-sets-010.md#p-86b39006dd52578f)

### observed_connections-009541

```text
(config-tunnel-eng)# mac-address source <address> interface <interface> <cr>
```

Handler ` RVA 0xC010D20 `；selector ` 6 `；EOL ` RVA 0x33984A28 `。

模式根 ` RVA 0x33984560 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` User defined source mac address for tunnel engine。

[条件 C-55a7376431766c9c](../../evidence/conditions-sets-034.md#c-55a7376431766c9c) · [缺口 G-46c9362499eda7d1](../../evidence/gaps-sets-003.md#g-46c9362499eda7d1) · [参数 P-059d77cdd4ad10a3](../../evidence/parameters-sets-001.md#p-059d77cdd4ad10a3)

### observed_connections-009536

```text
(config-tunnel-eng)# no exit <cr>
```

Handler ` RVA 0xC010CB0 `；selector ` 0 `；EOL ` RVA 0x339845B0 `。

模式根 ` RVA 0x33984560 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-b426d666d20aea21](../../evidence/state_effects-sets-038.md#s-b426d666d20aea21)

### observed_connections-009539

```text
(config-tunnel-eng)# no mac-address source <address> <cr>
```

Handler ` RVA 0xC010D20 `；selector ` 5 `；EOL ` RVA 0x33984968 `。

模式根 ` RVA 0x33984560 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` User defined source mac address for tunnel engine。

[参数 P-86b39006dd52578f](../../evidence/parameters-sets-010.md#p-86b39006dd52578f) · [状态效果 S-b426d666d20aea21](../../evidence/state_effects-sets-038.md#s-b426d666d20aea21)
