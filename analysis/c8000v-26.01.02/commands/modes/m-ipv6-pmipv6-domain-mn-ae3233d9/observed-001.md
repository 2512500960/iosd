# ipv6-pmipv6-domain-mn · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-009828

```text
(config-ipv6-pmipv6-domain-mn)# auth-option spi <number:100..4294967295> key hex <hex-string> <cr>
```

Handler ` RVA 0x1A6CE800 `；selector ` 0 `；EOL ` RVA 0x36CA1F68 `。

模式根 ` RVA 0x36CA1890 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` SPI hex value；` hexstring ` Hex string。

[条件 C-783823f2d6be8585](../../evidence/conditions-sets-047.md#c-783823f2d6be8585) · [缺口 G-8a78a5e006e299d1](../../evidence/gaps-sets-005.md#g-8a78a5e006e299d1) · [参数 P-9e1dc1bce17f6416](../../evidence/parameters-sets-012.md#p-9e1dc1bce17f6416) · [状态效果 S-9b9c103809874814](../../evidence/state_effects-sets-033.md#s-9b9c103809874814)

### observed_connections-009826

```text
(config-ipv6-pmipv6-domain-mn)# exit <cr>
```

Handler ` RVA 0x1A6CE800 `；selector ` 0 `；EOL ` RVA 0x36CA1F68 `。

模式根 ` RVA 0x36CA1890 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[状态效果 S-8d8a78c6e9dce71a](../../evidence/state_effects-sets-030.md#s-8d8a78c6e9dce71a)

### observed_connections-009827

```text
(config-ipv6-pmipv6-domain-mn)# no multi-homed <cr>
```

Handler ` RVA 0x1A6CE800 `；selector ` 0 `；EOL ` RVA 0x36CA1F68 `。

模式根 ` RVA 0x36CA1890 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-2d62811e2b0e1c67](../../evidence/state_effects-sets-010.md#s-2d62811e2b0e1c67)
