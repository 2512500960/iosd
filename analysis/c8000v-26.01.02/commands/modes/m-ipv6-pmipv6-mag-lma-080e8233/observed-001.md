# ipv6-pmipv6-mag-lma · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-009856

```text
(config-ipv6-pmipv6mag-lma)# exit <cr>
```

Handler ` RVA 0x1A6CC180 `；selector ` 0 `；EOL ` RVA 0x36CAC060 `。

模式根 ` RVA 0x36CA1AE8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[状态效果 S-9046b3c181c325e9](../../evidence/state_effects-sets-031.md#s-9046b3c181c325e9)

### observed_connections-009857

```text
(config-ipv6-pmipv6mag-lma)# no ipv4-address <cr>
```

Handler ` RVA 0x1A6CC180 `；selector ` 0 `；EOL ` RVA 0x36CAC060 `。

模式根 ` RVA 0x36CA1AE8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7eed8e3a349abe94](../../evidence/conditions-sets-049.md#c-7eed8e3a349abe94) · [状态效果 S-8bb78c2ad97b7c7b](../../evidence/state_effects-sets-030.md#s-8bb78c2ad97b7c7b)

### observed_connections-009858

```text
(config-ipv6-pmipv6mag-lma)# tunnel-template <interface> <cr>
```

Handler ` RVA 0x1A6CC180 `；selector ` 0 `；EOL ` RVA 0x36CAC060 `。

模式根 ` RVA 0x36CA1AE8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4a5d047949587672](../../evidence/conditions-sets-029.md#c-4a5d047949587672) · [缺口 G-88ac9bf79e3be396](../../evidence/gaps-sets-005.md#g-88ac9bf79e3be396) · [参数 P-f43a97023e67f64e](../../evidence/parameters-sets-018.md#p-f43a97023e67f64e) · [状态效果 S-5de571beff688734](../../evidence/state_effects-sets-020.md#s-5de571beff688734)

