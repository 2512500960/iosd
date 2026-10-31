# OFA-config · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-009779

```text
(config-ofa)# default service vxlan-evpn <cr>
```

Handler ` RVA 0xC488F90 `；selector ` 0 `；EOL ` RVA 0x33A960D0 `。

模式根 ` RVA 0x33A92B10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-1b6c04e30b48cb9f](../../evidence/state_effects-sets-006.md#s-1b6c04e30b48cb9f)

### observed_connections-009778

```text
(config-ofa)# no service vxlan-evpn <cr>
```

Handler ` RVA 0xC488F90 `；selector ` 0 `；EOL ` RVA 0x33A960D0 `。

模式根 ` RVA 0x33A92B10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-68ff9af0a7393598](../../evidence/state_effects-sets-022.md#s-68ff9af0a7393598)

### observed_connections-009777

```text
(config-ofa)# service vxlan-evpn <cr>
```

Handler ` RVA 0xC488F90 `；selector ` 0 `；EOL ` RVA 0x33A960D0 `。

模式根 ` RVA 0x33A92B10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。
