# ipv6-pmipv6-lma-svc · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-009836

```text
(config-ipv6-pmipv6-lma-svc)# exit <cr>
```

Handler ` RVA 0x1A6C9470 `；selector ` 0 `；EOL ` RVA 0x36CA46E8 `。

模式根 ` RVA 0x36CA1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[状态效果 S-6d225787ac66c388](../../evidence/state_effects-sets-023.md#s-6d225787ac66c388)

### observed_connections-009837

```text
(config-ipv6-pmipv6-lma-svc)# no customer <string> vrf <string> <cr>
```

Handler ` RVA 0x1A6C9470 `；selector ` 0 `；EOL ` RVA 0x36CA46E8 `。

模式根 ` RVA 0x36CA1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Customer identifier；` string ` VRF name for this Customer。

[参数 P-1058208f50df2e7f](../../evidence/parameters-sets-002.md#p-1058208f50df2e7f) · [状态效果 S-3e5447d57c82ebae](../../evidence/state_effects-sets-014.md#s-3e5447d57c82ebae)
