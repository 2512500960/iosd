# evpn-vpws · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-009205

```text
(config-evpn-vpws)# default preferred-path segment-routing traffic-eng policy <string> <cr>
```

Handler ` RVA 0x12520D40 `；selector ` 0 `；EOL ` RVA 0x35882F28 `。

模式根 ` RVA 0x3587BB50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Name of SR TE policy。

[条件 C-22003148a9c5c7ed](../../evidence/conditions-sets-013.md#c-22003148a9c5c7ed) · [参数 P-b22c35c781d7d4e7](../../evidence/parameters-sets-014.md#p-b22c35c781d7d4e7) · [状态效果 S-0064f6e292347faf](../../evidence/state_effects-sets-001.md#s-0064f6e292347faf)

### observed_connections-009200

```text
(config-evpn-vpws)# default remote link failure notification <cr>
```

Handler ` RVA 0x125211D0 `；selector ` 0 `；EOL ` RVA 0x358832E0 `。

模式根 ` RVA 0x3587BB50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-49c4dfcf6688952d](../../evidence/state_effects-sets-016.md#s-49c4dfcf6688952d)

### observed_connections-009203

```text
(config-evpn-vpws)# default service target <number:1..16777215> source <number:1..16777215> <cr>
```

Handler ` RVA 0x1251FF20 `；selector ` 0 `；EOL ` RVA 0x35882628 `。

模式根 ` RVA 0x3587BB50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Target VPWS Service Instance identifier value；` unsigned_number ` Source VPWS Service Instance identifier value。

[参数 P-940eb30653854822](../../evidence/parameters-sets-011.md#p-940eb30653854822) · [状态效果 S-49c4dfcf6688952d](../../evidence/state_effects-sets-016.md#s-49c4dfcf6688952d)

### observed_connections-009196

```text
(config-evpn-vpws)# default shutdown <cr>
```

Handler ` RVA 0x12521380 `；selector ` 0 `；EOL ` RVA 0x35883588 `。

模式根 ` RVA 0x3587BB50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-49c4dfcf6688952d](../../evidence/state_effects-sets-016.md#s-49c4dfcf6688952d)

### observed_connections-009193

```text
(config-evpn-vpws)# exit <cr>
```

Handler ` RVA 0x1251A570 `；selector ` 0 `；EOL ` RVA 0x3587BFE8 `。

模式根 ` RVA 0x3587BB50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-21721f01db5114c6](../../evidence/conditions-sets-013.md#c-21721f01db5114c6)

### observed_connections-009206

```text
(config-evpn-vpws)# member <interface> <cr>
```

Handler ` RVA 0x12520250 `；selector ` 0 `；EOL ` RVA 0x35882A58 `。

模式根 ` RVA 0x3587BB50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-01334b6b4c9e6c9f](../../evidence/conditions-sets-001.md#c-01334b6b4c9e6c9f) · [缺口 G-59d171f57f19d2d8](../../evidence/gaps-sets-004.md#g-59d171f57f19d2d8) · [参数 P-ec6fdaf95b2be319](../../evidence/parameters-sets-018.md#p-ec6fdaf95b2be319)

### observed_connections-009204

```text
(config-evpn-vpws)# no preferred-path segment-routing traffic-eng policy <string> <cr>
```

Handler ` RVA 0x12520D40 `；selector ` 0 `；EOL ` RVA 0x35882F28 `。

模式根 ` RVA 0x3587BB50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Name of SR TE policy。

[条件 C-22003148a9c5c7ed](../../evidence/conditions-sets-013.md#c-22003148a9c5c7ed) · [参数 P-b22c35c781d7d4e7](../../evidence/parameters-sets-014.md#p-b22c35c781d7d4e7) · [状态效果 S-351e538ebcc5b258](../../evidence/state_effects-sets-012.md#s-351e538ebcc5b258)

### observed_connections-009199

```text
(config-evpn-vpws)# no remote link failure notification <cr>
```

Handler ` RVA 0x125211D0 `；selector ` 0 `；EOL ` RVA 0x358832E0 `。

模式根 ` RVA 0x3587BB50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-e1c0fcbd6d826e1a](../../evidence/state_effects-sets-048.md#s-e1c0fcbd6d826e1a)

### observed_connections-009202

```text
(config-evpn-vpws)# no service target <number:1..16777215> source <number:1..16777215> <cr>
```

Handler ` RVA 0x1251FF20 `；selector ` 0 `；EOL ` RVA 0x35882628 `。

模式根 ` RVA 0x3587BB50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Target VPWS Service Instance identifier value；` unsigned_number ` Source VPWS Service Instance identifier value。

[参数 P-940eb30653854822](../../evidence/parameters-sets-011.md#p-940eb30653854822) · [状态效果 S-e1c0fcbd6d826e1a](../../evidence/state_effects-sets-048.md#s-e1c0fcbd6d826e1a)

### observed_connections-009195

```text
(config-evpn-vpws)# no shutdown <cr>
```

Handler ` RVA 0x12521380 `；selector ` 0 `；EOL ` RVA 0x35883588 `。

模式根 ` RVA 0x3587BB50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-e1c0fcbd6d826e1a](../../evidence/state_effects-sets-048.md#s-e1c0fcbd6d826e1a)

### observed_connections-009201

```text
(config-evpn-vpws)# preferred-path segment-routing traffic-eng policy <string> <cr>
```

Handler ` RVA 0x12520D40 `；selector ` 0 `；EOL ` RVA 0x35882F28 `。

模式根 ` RVA 0x3587BB50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of SR TE policy。

[条件 C-22003148a9c5c7ed](../../evidence/conditions-sets-013.md#c-22003148a9c5c7ed) · [参数 P-b22c35c781d7d4e7](../../evidence/parameters-sets-014.md#p-b22c35c781d7d4e7) · [状态效果 S-b9aebd0d1e05ad74](../../evidence/state_effects-sets-039.md#s-b9aebd0d1e05ad74)

### observed_connections-009197

```text
(config-evpn-vpws)# remote link failure notification <cr>
```

Handler ` RVA 0x125211D0 `；selector ` 0 `；EOL ` RVA 0x358832E0 `。

模式根 ` RVA 0x3587BB50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-009198

```text
(config-evpn-vpws)# service target <number:1..16777215> source <number:1..16777215> <cr>
```

Handler ` RVA 0x1251FF20 `；selector ` 0 `；EOL ` RVA 0x35882628 `。

模式根 ` RVA 0x3587BB50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Target VPWS Service Instance identifier value；` unsigned_number ` Source VPWS Service Instance identifier value。

[参数 P-940eb30653854822](../../evidence/parameters-sets-011.md#p-940eb30653854822)

### observed_connections-009194

```text
(config-evpn-vpws)# shutdown <cr>
```

Handler ` RVA 0x12521380 `；selector ` 0 `；EOL ` RVA 0x35883588 `。

模式根 ` RVA 0x3587BB50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

