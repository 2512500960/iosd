# evpn-all-active-mh · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-009761

```text
(config-evpn-all-active-mh)# default neighbor <cr>
```

Handler ` RVA 0x1252ACB0 `；selector ` 0 `；EOL ` RVA 0x35897DE8 `。

模式根 ` RVA 0x35897130 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-15f47918a36beff7](../../evidence/conditions-sets-009.md#c-15f47918a36beff7) · [状态效果 S-67ea79b7f0d439db](../../evidence/state_effects-sets-022.md#s-67ea79b7f0d439db)

### observed_connections-009759

```text
(config-evpn-all-active-mh)# exit <cr>
```

Handler ` RVA 0x1252ABC0 `；selector ` 0 `；EOL ` RVA 0x35897AD8 `。

模式根 ` RVA 0x35897130 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4dcfc64442ee41dd](../../evidence/conditions-sets-030.md#c-4dcfc64442ee41dd)

### observed_connections-009762

```text
(config-evpn-all-active-mh)# neighbor <address> <number:1..4294967295> <interface> <cr>
```

Handler ` RVA 0x1252ACB0 `；selector ` 0 `；EOL ` RVA 0x35897DE8 `。

模式根 ` RVA 0x35897130 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` ESI mLAG peer switch IPv4 address；` unsigned_number ` iBGP ASN ID。

[条件 C-b144e468dd46d491](../../evidence/conditions-sets-069.md#c-b144e468dd46d491) · [缺口 G-45ce8254b497884c](../../evidence/gaps-sets-003.md#g-45ce8254b497884c) · [参数 P-8f1f3c6901a93576](../../evidence/parameters-sets-011.md#p-8f1f3c6901a93576)

### observed_connections-009760

```text
(config-evpn-all-active-mh)# no neighbor <cr>
```

Handler ` RVA 0x1252ACB0 `；selector ` 0 `；EOL ` RVA 0x35897DE8 `。

模式根 ` RVA 0x35897130 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ace27d5739910793](../../evidence/conditions-sets-067.md#c-ace27d5739910793) · [状态效果 S-75b4dfbdc7439538](../../evidence/state_effects-sets-025.md#s-75b4dfbdc7439538)

