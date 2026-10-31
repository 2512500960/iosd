# ipv6-pmipv6-mag-logicalmn · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-009859

```text
(config-ipv6-pmipv6mag-logicalmn)# exit <cr>
```

Handler ` RVA 0x1A6CC180 `；selector ` 0 `；EOL ` RVA 0x36CAC060 `。

模式根 ` RVA 0x36CA1B10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[状态效果 S-5671211a8ee646da](../../evidence/state_effects-sets-019.md#s-5671211a8ee646da)

### observed_connections-009861

```text
(config-ipv6-pmipv6mag-logicalmn)# home interface <interface> <cr>
```

Handler ` RVA 0x1A6CC180 `；selector ` 0 `；EOL ` RVA 0x36CAC060 `。

模式根 ` RVA 0x36CA1B10 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6ad215df40a82088](../../evidence/conditions-sets-041.md#c-6ad215df40a82088) · [缺口 G-44fda583be54a9ee](../../evidence/gaps-sets-003.md#g-44fda583be54a9ee) · [参数 P-9561d318511137bf](../../evidence/parameters-sets-011.md#p-9561d318511137bf) · [状态效果 S-84b932430687e1c8](../../evidence/state_effects-sets-028.md#s-84b932430687e1c8)

### observed_connections-009860

```text
(config-ipv6-pmipv6mag-logicalmn)# no mobile-map <string> <cr>
```

Handler ` RVA 0x1A6CC180 `；selector ` 0 `；EOL ` RVA 0x36CAC060 `。

模式根 ` RVA 0x36CA1B10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` MOBILE MAP name。

[参数 P-5fd1aaebabfb9ced](../../evidence/parameters-sets-008.md#p-5fd1aaebabfb9ced) · [状态效果 S-03e98f2aa14035dd](../../evidence/state_effects-sets-001.md#s-03e98f2aa14035dd)
