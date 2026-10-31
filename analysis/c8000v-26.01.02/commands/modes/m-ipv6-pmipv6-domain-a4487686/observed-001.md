# ipv6-pmipv6-domain · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-009819

```text
(config-ipv6-pmipv6-domain)# auth-option spi <number:100..4294967295> key hex <hex-string> <cr>
```

Handler ` RVA 0x1A6CE800 `；selector ` 0 `；EOL ` RVA 0x36CA1F68 `。

模式根 ` RVA 0x36CA17F0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` SPI hex value；` hexstring ` Hex string。

[条件 C-aba800a6f6ae403e](../../evidence/conditions-sets-066.md#c-aba800a6f6ae403e) · [缺口 G-064f98edc357a8a0](../../evidence/gaps-sets-001.md#g-064f98edc357a8a0) · [参数 P-a5609f82ae52e3fb](../../evidence/parameters-sets-013.md#p-a5609f82ae52e3fb) · [状态效果 S-1be6808ab6b7eb3d](../../evidence/state_effects-sets-006.md#s-1be6808ab6b7eb3d)

### observed_connections-009817

```text
(config-ipv6-pmipv6-domain)# exit <cr>
```

Handler ` RVA 0x1A6CE800 `；selector ` 0 `；EOL ` RVA 0x36CA1F68 `。

模式根 ` RVA 0x36CA17F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[状态效果 S-24ed50d7b0f0046e](../../evidence/state_effects-sets-008.md#s-24ed50d7b0f0046e)

### observed_connections-009818

```text
(config-ipv6-pmipv6-domain)# no auth-option <cr>
```

Handler ` RVA 0x1A6CE800 `；selector ` 0 `；EOL ` RVA 0x36CA1F68 `。

模式根 ` RVA 0x36CA17F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4f31888812e960c8](../../evidence/conditions-sets-031.md#c-4f31888812e960c8) · [状态效果 S-0f5ee07902868c7e](../../evidence/state_effects-sets-004.md#s-0f5ee07902868c7e)
