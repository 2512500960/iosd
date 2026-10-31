# ipv6-pmipv6-mag · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-009853

```text
(config-ipv6-pmipv6-mag)# exit <cr>
```

Handler ` RVA 0x1A6CC180 `；selector ` 0 `；EOL ` RVA 0x36CAC060 `。

模式根 ` RVA 0x36CA1AC0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[状态效果 S-83b68330fca8e559](../../evidence/state_effects-sets-028.md#s-83b68330fca8e559)

### observed_connections-009854

```text
(config-ipv6-pmipv6-mag)# no apn <cr>
```

Handler ` RVA 0x1A6CC180 `；selector ` 0 `；EOL ` RVA 0x36CAC060 `。

模式根 ` RVA 0x36CA1AC0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-18c8525388a8be93](../../evidence/conditions-sets-010.md#c-18c8525388a8be93) · [状态效果 S-718ed2021f857006](../../evidence/state_effects-sets-024.md#s-718ed2021f857006)

### observed_connections-009855

```text
(config-ipv6-pmipv6-mag)# tunnel-template <interface> <cr>
```

Handler ` RVA 0x1A6CC180 `；selector ` 0 `；EOL ` RVA 0x36CAC060 `。

模式根 ` RVA 0x36CA1AC0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-cbe611582c9f2440](../../evidence/conditions-sets-078.md#c-cbe611582c9f2440) · [缺口 G-8e01bce8df76fd2d](../../evidence/gaps-sets-005.md#g-8e01bce8df76fd2d) · [参数 P-5156a2b9c311ce4d](../../evidence/parameters-sets-007.md#p-5156a2b9c311ce4d) · [状态效果 S-bfe365f2c6f5136a](../../evidence/state_effects-sets-041.md#s-bfe365f2c6f5136a)
