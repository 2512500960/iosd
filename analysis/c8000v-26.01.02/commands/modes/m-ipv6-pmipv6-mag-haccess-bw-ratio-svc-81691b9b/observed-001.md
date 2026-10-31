# ipv6-pmipv6-mag-haccess-bw-ratio-svc · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-009877

```text
(config-ipv6-pmipv6-mag-haccess-bw-ratio-svc)# exit <cr>
```

Handler ` RVA 0x1A6CC180 `；selector ` 0 `；EOL ` RVA 0x36CAC060 `。

模式根 ` RVA 0x36CA1C50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[状态效果 S-8073643da2d7d098](../../evidence/state_effects-sets-027.md#s-8073643da2d7d098)

### observed_connections-009878

```text
(config-ipv6-pmipv6-mag-haccess-bw-ratio-svc)# no label <string> bandwidth-ratio <number:1..15> <cr>
```

Handler ` RVA 0x1A6CC180 `；selector ` 0 `；EOL ` RVA 0x36CAC060 `。

模式根 ` RVA 0x36CA1C50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Label name；` unsigned_number ` bandwidth ratio value。

[参数 P-f15ee0457ca924c5](../../evidence/parameters-sets-018.md#p-f15ee0457ca924c5) · [状态效果 S-810efd6bf6ffd138](../../evidence/state_effects-sets-027.md#s-810efd6bf6ffd138)
