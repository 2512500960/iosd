# configure · 六个基础模式的历史连接

[模式索引](README.md) · [总索引](../../README.md)

### path-039205

```text
(config)# no do-exec show vlans summary <cr>
```

Handler ` RVA 0x11D1F260 `；selector ` 0 `；EOL ` RVA 0x356CF5D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-039257

```text
(config)# no do-exec show vlans tokenring <cr>
```

Handler ` RVA 0x11D1F1E0 `；selector ` 0 `；EOL ` RVA 0x356CF880 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-039302

```text
(config)# no do-exec show vlans tr-isl <cr>
```

Handler ` RVA 0x11D1ED50 `；selector ` 0 `；EOL ` RVA 0x356CFB28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-032876

```text
(config)# no do-exec show vnet <cr>
```

Handler ` RVA 0x12467AB0 `；selector ` 0 `；EOL ` RVA 0x358759D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-874daff06cabb1a9](../../evidence/conditions-sets-052.md#c-874daff06cabb1a9) · [状态效果 S-ec7350c37a1c9fca](../../evidence/state_effects-sets-050.md#s-ec7350c37a1c9fca)

### path-050635

```text
(config)# no do-exec show vpdn dead-cache all <cr>
```

Handler ` RVA 0x11DB8630 `；selector ` 1 `；EOL ` RVA 0x3570B978 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-bf4a7ea8d83414fc](../../evidence/state_effects-sets-040.md#s-bf4a7ea8d83414fc)

### path-056139

```text
(config)# no do-exec show vpdn dead-cache group <string> <cr>
```

Handler ` RVA 0x11DB8630 `；selector ` 2 `；EOL ` RVA 0x3570B6F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Name of VPDN group。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-ab5305a87287f44c](../../evidence/parameters-sets-013.md#p-ab5305a87287f44c) · [状态效果 S-bf4a7ea8d83414fc](../../evidence/state_effects-sets-040.md#s-bf4a7ea8d83414fc)

### path-041711

```text
(config)# no do-exec show vpdn domain <cr>
```

Handler ` RVA 0x11D45010 `；selector ` 0 `；EOL ` RVA 0x3570AB50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-041717

```text
(config)# no do-exec show vpdn group <cr>
```

Handler ` RVA 0x11DB8260 `；selector ` 0 `；EOL ` RVA 0x3570A128 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-050554

```text
(config)# no do-exec show vpdn group <string> <cr>
```

Handler ` RVA 0x11DB9580 `；selector ` 20 `；EOL ` RVA 0x3570A438 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Name of VPDN group。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-aaf221e0011cb9dd](../../evidence/parameters-sets-013.md#p-aaf221e0011cb9dd) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-056077

```text
(config)# no do-exec show vpdn group <string> domain <cr>
```

Handler ` RVA 0x11DB9580 `；selector ` 22 `；EOL ` RVA 0x3570A410 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Name of VPDN group。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-aaf221e0011cb9dd](../../evidence/parameters-sets-013.md#p-aaf221e0011cb9dd) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-056060

```text
(config)# no do-exec show vpdn group <string> endpoint <cr>
```

Handler ` RVA 0x11DB9580 `；selector ` 21 `；EOL ` RVA 0x3570A168 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Name of VPDN group。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-aaf221e0011cb9dd](../../evidence/parameters-sets-013.md#p-aaf221e0011cb9dd) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-050675

```text
(config)# no do-exec show vpdn group-select Default <cr>
```

Handler ` RVA 0x11DBAB80 `；selector ` 138 `；EOL ` RVA 0x3570CC18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-41c5afc31b95e7b6](../../evidence/conditions-sets-026.md#c-41c5afc31b95e7b6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-050652

```text
(config)# no do-exec show vpdn group-select Summary <cr>
```

Handler ` RVA 0x11DBAB80 `；selector ` 139 `；EOL ` RVA 0x3570C970 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-41c5afc31b95e7b6](../../evidence/conditions-sets-026.md#c-41c5afc31b95e7b6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-059926

```text
(config)# no do-exec show vpdn group-select keys hostname <string> source-ip <address> <cr>
```

Handler ` RVA 0x11DBAB80 `；selector ` 140 `；EOL ` RVA 0x3570D028 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Hostname of user；` address ` Source IP of user。

[条件 C-41c5afc31b95e7b6](../../evidence/conditions-sets-026.md#c-41c5afc31b95e7b6) · [参数 P-9c6a85d6ffef3c2d](../../evidence/parameters-sets-012.md#p-9c6a85d6ffef3c2d) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-050507

```text
(config)# no do-exec show vpdn history failure <cr>
```

Handler ` RVA 0x11DC0FF0 `；selector ` 0 `；EOL ` RVA 0x35709B80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-050500

```text
(config)# no do-exec show vpdn history fsm <cr>
```

Handler ` RVA 0x11D81400 `；selector ` 0 `；EOL ` RVA 0x35709E00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-050658

```text
(config)# no do-exec show vpdn lsg all <cr>
```

Handler ` RVA 0x11DB8630 `；selector ` 1 `；EOL ` RVA 0x3570BF98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-2d0f80354e9e0544](../../evidence/state_effects-sets-010.md#s-2d0f80354e9e0544)

### path-056155

```text
(config)# no do-exec show vpdn lsg group <string> <cr>
```

Handler ` RVA 0x11DB8630 `；selector ` 2 `；EOL ` RVA 0x3570BD18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Name of VPDN group。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-c7153b712117ee31](../../evidence/parameters-sets-015.md#p-c7153b712117ee31) · [状态效果 S-2d0f80354e9e0544](../../evidence/state_effects-sets-010.md#s-2d0f80354e9e0544)

### path-041763

```text
(config)# no do-exec show vpdn multilink <cr>
```

Handler ` RVA 0x11DB8470 `；selector ` 0 `；EOL ` RVA 0x3570B0A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-041732

```text
(config)# no do-exec show vpdn redirect <cr>
```

Handler ` RVA 0x11DB8520 `；selector ` 0 `；EOL ` RVA 0x3570ADF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-041982

```text
(config)# no do-exec show vpdn redundancy <cr>
```

Handler ` RVA 0x11DC5470 `；selector ` 1 `；EOL ` RVA 0x3570C378 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b11a9c5ffaa11052](../../evidence/conditions-sets-068.md#c-b11a9c5ffaa11052) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-050674

```text
(config)# no do-exec show vpdn redundancy all <cr>
```

Handler ` RVA 0x11DC5470 `；selector ` 4 `；EOL ` RVA 0x3570C410 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b11a9c5ffaa11052](../../evidence/conditions-sets-068.md#c-b11a9c5ffaa11052) · [状态效果 S-6f588e2dffb89a24](../../evidence/state_effects-sets-024.md#s-6f588e2dffb89a24)

### path-041790

```text
(config)# no do-exec show vpdn scalability <cr>
```

Handler ` RVA 0x11DE4800 `；selector ` 0 `；EOL ` RVA 0x3570B348 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-6a240251bfde7090](../../evidence/conditions-sets-041.md#c-6a240251bfde7090) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-056031

```text
(config)# no do-exec show vpdn statistics call fsm <cr>
```

Handler ` RVA 0x11D9C160 `；selector ` 0 `；EOL ` RVA 0x357091F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-056040

```text
(config)# no do-exec show vpdn statistics mgr fsm <cr>
```

Handler ` RVA 0x11DA0AF0 `；selector ` 0 `；EOL ` RVA 0x357094C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-056038

```text
(config)# no do-exec show vpdn subscriber statistics fsm <cr>
```

Handler ` RVA 0x11E16260 `；selector ` 0 `；EOL ` RVA 0x35709818 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-032110

```text
(config)# no do-exec show vrf <cr>
```

Handler ` RVA 0xDC3F530 `；selector ` 0 `；EOL ` RVA 0x34014230 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-6e776e3b9bfd73fc](../../evidence/conditions-sets-043.md#c-6e776e3b9bfd73fc) · [状态效果 S-25d851da5fe74c04](../../evidence/state_effects-sets-008.md#s-25d851da5fe74c04)

### path-040756

```text
(config)# no do-exec show vrf list <cr>
```

Handler ` RVA 0x12465980 `；selector ` 0 `；EOL ` RVA 0x35872DF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-84330cfd5eae4219](../../evidence/conditions-sets-051.md#c-84330cfd5eae4219) · [状态效果 S-25d851da5fe74c04](../../evidence/state_effects-sets-008.md#s-25d851da5fe74c04)

### path-040624

```text
(config)# no do-exec show vrf select <cr>
```

Handler ` RVA 0xFADE7A0 `；selector ` 0 `；EOL ` RVA 0x34808200 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-bfbccc878ae22b6c](../../evidence/conditions-sets-074.md#c-bfbccc878ae22b6c) · [状态效果 S-25d851da5fe74c04](../../evidence/state_effects-sets-008.md#s-25d851da5fe74c04)

### path-032008

```text
(config)# no do-exec show vrrp <cr>
```

Handler ` RVA 0x133C8FB0 `；selector ` 0 `；EOL ` RVA 0x35A80120 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1d72f7c2e0fb4355](../../evidence/conditions-sets-011.md#c-1d72f7c2e0fb4355) · [状态效果 S-565881dd795703e3](../../evidence/state_effects-sets-019.md#s-565881dd795703e3)

### path-038505

```text
(config)# no do-exec show vrrs accounting <cr>
```

Handler ` RVA 0xE2FD270 `；selector ` 0 `；EOL ` RVA 0x342A3250 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-61e5893443b8636b](../../evidence/conditions-sets-038.md#c-61e5893443b8636b) · [状态效果 S-256d39dfcbb889ed](../../evidence/state_effects-sets-008.md#s-256d39dfcbb889ed)

### path-040030

```text
(config)# no do-exec show vrrs client <cr>
```

Handler ` RVA 0x133F9730 `；selector ` 0 `；EOL ` RVA 0x35A8A930 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-20e24cf3a0e61aa9](../../evidence/conditions-sets-013.md#c-20e24cf3a0e61aa9) · [状态效果 S-2e1c1f7d1d55cb50](../../evidence/state_effects-sets-010.md#s-2e1c1f7d1d55cb50)

### path-038487

```text
(config)# no do-exec show vrrs clients <cr>
```

Handler ` RVA 0xE2F9FA0 `；selector ` 1 `；EOL ` RVA 0x3429FE60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-cbfca79d665be9c8](../../evidence/conditions-sets-078.md#c-cbfca79d665be9c8) · [状态效果 S-36acd0c72de4c366](../../evidence/state_effects-sets-012.md#s-36acd0c72de4c366)

### path-038510

```text
(config)# no do-exec show vrrs group <cr>
```

Handler ` RVA 0xE2F9FA0 `；selector ` 2 `；EOL ` RVA 0x3429FBE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-cbfca79d665be9c8](../../evidence/conditions-sets-078.md#c-cbfca79d665be9c8) · [状态效果 S-36acd0c72de4c366](../../evidence/state_effects-sets-012.md#s-36acd0c72de4c366)

### path-038593

```text
(config)# no do-exec show vrrs internal <cr>
```

Handler ` RVA 0xE2F9FA0 `；selector ` 4 `；EOL ` RVA 0x342A0148 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-dd79ce7347f4b389](../../evidence/conditions-sets-085.md#c-dd79ce7347f4b389) · [状态效果 S-36acd0c72de4c366](../../evidence/state_effects-sets-012.md#s-36acd0c72de4c366)

### path-040113

```text
(config)# no do-exec show vrrs pathway <cr>
```

Handler ` RVA 0x133F94F0 `；selector ` 0 `；EOL ` RVA 0x35A8B1B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-09af84b0ed28b07e](../../evidence/conditions-sets-004.md#c-09af84b0ed28b07e) · [状态效果 S-2e1c1f7d1d55cb50](../../evidence/state_effects-sets-010.md#s-2e1c1f7d1d55cb50)

### path-049088

```text
(config)# no do-exec show vrrs pathway address <cr>
```

Handler ` RVA 0x133F9490 `；selector ` 0 `；EOL ` RVA 0x35A8B460 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-09af84b0ed28b07e](../../evidence/conditions-sets-004.md#c-09af84b0ed28b07e) · [状态效果 S-2e1c1f7d1d55cb50](../../evidence/state_effects-sets-010.md#s-2e1c1f7d1d55cb50)

### path-044290

```text
(config)# no do-exec show vrrs plugin database <cr>
```

Handler ` RVA 0xE2FEDD0 `；selector ` 2 `；EOL ` RVA 0x342A6228 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-57c5b16611c0637c](../../evidence/conditions-sets-034.md#c-57c5b16611c0637c) · [状态效果 S-b10d7ea98d315d8d](../../evidence/state_effects-sets-038.md#s-b10d7ea98d315d8d)

### path-040114

```text
(config)# no do-exec show vrrs server <cr>
```

Handler ` RVA 0x133F97D0 `；selector ` 0 `；EOL ` RVA 0x35A8ADD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d5af9483c87d3242](../../evidence/conditions-sets-082.md#c-d5af9483c87d3242) · [状态效果 S-c31482f7e4484e34](../../evidence/state_effects-sets-041.md#s-c31482f7e4484e34)

### path-038393

```text
(config)# no do-exec show vrrs summary <cr>
```

Handler ` RVA 0xE2F9FA0 `；selector ` 3 `；EOL ` RVA 0x3429F8D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-cbfca79d665be9c8](../../evidence/conditions-sets-078.md#c-cbfca79d665be9c8) · [状态效果 S-36acd0c72de4c366](../../evidence/state_effects-sets-012.md#s-36acd0c72de4c366)

### path-039864

```text
(config)# no do-exec show vrrs tag <cr>
```

Handler ` RVA 0x133F9880 `；selector ` 0 `；EOL ` RVA 0x35A8A648 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d5af9483c87d3242](../../evidence/conditions-sets-082.md#c-d5af9483c87d3242) · [状态效果 S-2e1c1f7d1d55cb50](../../evidence/state_effects-sets-010.md#s-2e1c1f7d1d55cb50)

### path-033033

```text
(config)# no do-exec show vtemplate <cr>
```

Handler ` RVA 0x105C73D0 `；selector ` 0 `；EOL ` RVA 0x34BB1770 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-869564b610b8b12c](../../evidence/conditions-sets-052.md#c-869564b610b8b12c) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-042231

```text
(config)# no do-exec show vtemplate queue <cr>
```

Handler ` RVA 0x105C73D0 `；selector ` 1 `；EOL ` RVA 0x34BB14D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-22436537f02c5c24](../../evidence/conditions-sets-013.md#c-22436537f02c5c24) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-040048

```text
(config)# no do-exec show vtp counters <cr>
```

Handler ` RVA 0x15C743A0 `；selector ` 4 `；EOL ` RVA 0x35DFAAE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-040146

```text
(config)# no do-exec show vtp devices <cr>
```

Handler ` RVA 0x15C743A0 `；selector ` 17 `；EOL ` RVA 0x35DFAE20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-049114

```text
(config)# no do-exec show vtp devices conflicts <cr>
```

Handler ` RVA 0x15C743A0 `；selector ` 18 `；EOL ` RVA 0x35DFADF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-040108

```text
(config)# no do-exec show vtp interface <cr>
```

Handler ` RVA 0x15C743A0 `；selector ` 16 `；EOL ` RVA 0x35DFA828 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-35eb97e8264076bc](../../evidence/conditions-sets-021.md#c-35eb97e8264076bc) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-040137

```text
(config)# no do-exec show vtp password <cr>
```

Handler ` RVA 0x15C743A0 `；selector ` 15 `；EOL ` RVA 0x35DFB2F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-040023

```text
(config)# no do-exec show vtp status <cr>
```

Handler ` RVA 0x15C743A0 `；selector ` 7 `；EOL ` RVA 0x35E03BF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-040235

```text
(config)# no do-exec show vtp trunks <cr>
```

Handler ` RVA 0x15C743A0 `；selector ` 5 `；EOL ` RVA 0x35DFB600 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-049213

```text
(config)# no do-exec show vtp trunks all <cr>
```

Handler ` RVA 0x15C743A0 `；selector ` 6 `；EOL ` RVA 0x35DFB5D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-031612

```text
(config)# no do-exec show wccp <cr>
```

Handler ` RVA 0x10AD36D0 `；selector ` 0 `；EOL ` RVA 0x34C9FC18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8ced8bdbc4811d5e](../../evidence/conditions-sets-055.md#c-8ced8bdbc4811d5e) · [状态效果 S-b815b427be693b42](../../evidence/state_effects-sets-039.md#s-b815b427be693b42)

### path-039135

```text
(config)# no do-exec show wccp capabilities <cr>
```

Handler ` RVA 0x10AD36D0 `；selector ` 14 `；EOL ` RVA 0x34C9D3D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-720871d41476383a](../../evidence/conditions-sets-044.md#c-720871d41476383a) · [状态效果 S-b815b427be693b42](../../evidence/state_effects-sets-039.md#s-b815b427be693b42)

### path-048190

```text
(config)# no do-exec show wccp capabilities internal <cr>
```

Handler ` RVA 0x10AD36D0 `；selector ` 15 `；EOL ` RVA 0x34C9D440 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1f6646a9c1f3445e](../../evidence/conditions-sets-012.md#c-1f6646a9c1f3445e) · [状态效果 S-b815b427be693b42](../../evidence/state_effects-sets-039.md#s-b815b427be693b42)

### path-054708

```text
(config)# no do-exec show wccp capabilities internal data <cr>
```

Handler ` RVA 0x10AD36D0 `；selector ` 16 `；EOL ` RVA 0x34C9D418 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e9500134c9e33aa6](../../evidence/conditions-sets-090.md#c-e9500134c9e33aa6) · [状态效果 S-b815b427be693b42](../../evidence/state_effects-sets-039.md#s-b815b427be693b42)

### path-048064

```text
(config)# no do-exec show wccp global counters <cr>
```

Handler ` RVA 0x10AD36D0 `；selector ` 3 `；EOL ` RVA 0x34C9C2E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-b815b427be693b42](../../evidence/state_effects-sets-039.md#s-b815b427be693b42)

### path-047944

```text
(config)# no do-exec show wccp global internal <cr>
```

Handler ` RVA 0x10AB5B50 `；selector ` 0 `；EOL ` RVA 0x34C9BFD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-614a53ba8084353a](../../evidence/conditions-sets-038.md#c-614a53ba8084353a) · [状态效果 S-b815b427be693b42](../../evidence/state_effects-sets-039.md#s-b815b427be693b42)

### path-039145

```text
(config)# no do-exec show wccp interfaces <cr>
```

Handler ` RVA 0x10AD36D0 `；selector ` 10 `；EOL ` RVA 0x34C9CB78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-b815b427be693b42](../../evidence/state_effects-sets-039.md#s-b815b427be693b42)

### path-048092

```text
(config)# no do-exec show wccp interfaces cef <cr>
```

Handler ` RVA 0x10AD36D0 `；selector ` 13 `；EOL ` RVA 0x34C9CB50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-b815b427be693b42](../../evidence/state_effects-sets-039.md#s-b815b427be693b42)

### path-048043

```text
(config)# no do-exec show wccp interfaces counts <cr>
```

Handler ` RVA 0x10AD36D0 `；selector ` 12 `；EOL ` RVA 0x34C9C8A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-b815b427be693b42](../../evidence/state_effects-sets-039.md#s-b815b427be693b42)

### path-047991

```text
(config)# no do-exec show wccp interfaces detail <cr>
```

Handler ` RVA 0x10AD36D0 `；selector ` 11 `；EOL ` RVA 0x34C9C600 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-b815b427be693b42](../../evidence/state_effects-sets-039.md#s-b815b427be693b42)

### path-039014

```text
(config)# no do-exec show wccp summary <cr>
```

Handler ` RVA 0x10AD36D0 `；selector ` 17 `；EOL ` RVA 0x34C9D060 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-b815b427be693b42](../../evidence/state_effects-sets-039.md#s-b815b427be693b42)

### path-048462

```text
(config)# no do-exec show wccp web-cache assignment <cr>
```

Handler ` RVA 0x10AD36D0 `；selector ` 18 `；EOL ` RVA 0x34C9E3D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-bcb311f10c26b5b8](../../evidence/conditions-sets-073.md#c-bcb311f10c26b5b8) · [状态效果 S-3dab0119c994d617](../../evidence/state_effects-sets-014.md#s-3dab0119c994d617)

### path-048300

```text
(config)# no do-exec show wccp web-cache buckets <cr>
```

Handler ` RVA 0x10AD36D0 `；selector ` 18 `；EOL ` RVA 0x34C9DDF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-bcb311f10c26b5b8](../../evidence/conditions-sets-073.md#c-bcb311f10c26b5b8) · [状态效果 S-3dab0119c994d617](../../evidence/state_effects-sets-014.md#s-3dab0119c994d617)

### path-048670

```text
(config)# no do-exec show wccp web-cache clients <cr>
```

Handler ` RVA 0x10AD36D0 `；selector ` 2 `；EOL ` RVA 0x34C9F370 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-bcb311f10c26b5b8](../../evidence/conditions-sets-073.md#c-bcb311f10c26b5b8) · [状态效果 S-3dab0119c994d617](../../evidence/state_effects-sets-014.md#s-3dab0119c994d617)

### path-048676

```text
(config)# no do-exec show wccp web-cache counters <cr>
```

Handler ` RVA 0x10AD36D0 `；selector ` 4 `；EOL ` RVA 0x34C9F0D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-bcb311f10c26b5b8](../../evidence/conditions-sets-073.md#c-bcb311f10c26b5b8) · [状态效果 S-3dab0119c994d617](../../evidence/state_effects-sets-014.md#s-3dab0119c994d617)

### path-048808

```text
(config)# no do-exec show wccp web-cache detail <cr>
```

Handler ` RVA 0x10AD36D0 `；selector ` 1 `；EOL ` RVA 0x34C9F6A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-bcb311f10c26b5b8](../../evidence/conditions-sets-073.md#c-bcb311f10c26b5b8) · [状态效果 S-3dab0119c994d617](../../evidence/state_effects-sets-014.md#s-3dab0119c994d617)

### path-059882

```text
(config)# no do-exec show wccp web-cache hash <address> <address> <number:0..65535> <number:0..65535> <cr>
```

Handler ` RVA 0x10AD36D0 `；selector ` 7 `；EOL ` RVA 0x34C9E7E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` Destination IPv4 address；` address ` Source IPv4 address；` unsigned_number ` Destination port；` unsigned_number ` Source Port。

[条件 C-cf8d65cc7d285454](../../evidence/conditions-sets-080.md#c-cf8d65cc7d285454) · [参数 P-32263aafb6e585c0](../../evidence/parameters-sets-004.md#p-32263aafb6e585c0) · [状态效果 S-3dab0119c994d617](../../evidence/state_effects-sets-014.md#s-3dab0119c994d617)

### path-048793

```text
(config)# no do-exec show wccp web-cache internal <cr>
```

Handler ` RVA 0x10AD36D0 `；selector ` 5 `；EOL ` RVA 0x34C9F948 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-2c1dea74e6184d25](../../evidence/conditions-sets-017.md#c-2c1dea74e6184d25) · [状态效果 S-3dab0119c994d617](../../evidence/state_effects-sets-014.md#s-3dab0119c994d617)

### path-048349

```text
(config)# no do-exec show wccp web-cache mask-acl <cr>
```

Handler ` RVA 0x10AD36D0 `；selector ` 18 `；EOL ` RVA 0x34C9E0A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-bcb311f10c26b5b8](../../evidence/conditions-sets-073.md#c-bcb311f10c26b5b8) · [状态效果 S-3dab0119c994d617](../../evidence/state_effects-sets-014.md#s-3dab0119c994d617)

### path-048862

```text
(config)# no do-exec show wccp web-cache merged-acl <cr>
```

Handler ` RVA 0x10AD36D0 `；selector ` 9 `；EOL ` RVA 0x34C9FBF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-bcb311f10c26b5b8](../../evidence/conditions-sets-073.md#c-bcb311f10c26b5b8) · [状态效果 S-3dab0119c994d617](../../evidence/state_effects-sets-014.md#s-3dab0119c994d617)

### path-048497

```text
(config)# no do-exec show wccp web-cache service <cr>
```

Handler ` RVA 0x10AD36D0 `；selector ` 8 `；EOL ` RVA 0x34C9EAF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-bcb311f10c26b5b8](../../evidence/conditions-sets-073.md#c-bcb311f10c26b5b8) · [状态效果 S-3dab0119c994d617](../../evidence/state_effects-sets-014.md#s-3dab0119c994d617)

### path-048560

```text
(config)# no do-exec show wccp web-cache view <cr>
```

Handler ` RVA 0x10AD36D0 `；selector ` 6 `；EOL ` RVA 0x34C9ED98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-bcb311f10c26b5b8](../../evidence/conditions-sets-073.md#c-bcb311f10c26b5b8) · [状态效果 S-3dab0119c994d617](../../evidence/state_effects-sets-014.md#s-3dab0119c994d617)

### path-037092

```text
(config)# no do-exec show wrr-queue bandwidth <cr>
```

Handler ` RVA 0x15F29A20 `；selector ` 0 `；EOL ` RVA 0x35E6D2A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-037150

```text
(config)# no do-exec show wrr-queue cos-map <cr>
```

Handler ` RVA 0x15F29700 `；selector ` 0 `；EOL ` RVA 0x35E6D550 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-051721

```text
(config)# no do-exec show wsma agent counters <cr>
```

Handler ` RVA 0xF3E9DD0 `；selector ` 0 `；EOL ` RVA 0x3463A978 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-bb7353449a4757e4](../../evidence/state_effects-sets-040.md#s-bb7353449a4757e4)

### path-051736

```text
(config)# no do-exec show wsma agent profiles <cr>
```

Handler ` RVA 0xF3E9DD0 `；selector ` 0 `；EOL ` RVA 0x3463AC30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-ea15ddea8ae66db7](../../evidence/state_effects-sets-050.md#s-ea15ddea8ae66db7)

### path-051751

```text
(config)# no do-exec show wsma agent schema <cr>
```

Handler ` RVA 0xF3E9DD0 `；selector ` 0 `；EOL ` RVA 0x3463AEE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-fdf8469deffbc346](../../evidence/state_effects-sets-054.md#s-fdf8469deffbc346)

### path-043277

```text
(config)# no do-exec show wsma history <cr>
```

Handler ` RVA 0xF3EBEA0 `；selector ` 0 `；EOL ` RVA 0x3463B2F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-043242

```text
(config)# no do-exec show wsma id <cr>
```

Handler ` RVA 0xF403170 `；selector ` 0 `；EOL ` RVA 0x3463A5F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-051743

```text
(config)# no do-exec show wsma profile connections <cr>
```

Handler ` RVA 0xF3D6160 `；selector ` 0 `；EOL ` RVA 0x3462DC70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-c1505682ddd4c21e](../../evidence/state_effects-sets-041.md#s-c1505682ddd4c21e)

### path-043296

```text
(config)# no do-exec show wsma summary <cr>
```

Handler ` RVA 0xF3EC0F0 `；selector ` 0 `；EOL ` RVA 0x3463B5A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-043317

```text
(config)# no do-exec show wsma tech-support <cr>
```

Handler ` RVA 0xF3EC200 `；selector ` 0 `；EOL ` RVA 0x3463B848 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-033143

```text
(config)# no do-exec show x25 <cr>
```

Handler ` RVA 0x105F32F0 `；selector ` 8 `；EOL ` RVA 0x34BC8BF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-854c3491d5994616](../../evidence/conditions-sets-052.md#c-854c3491d5994616) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-042366

```text
(config)# no do-exec show x25 context <cr>
```

Handler ` RVA 0x105F32F0 `；selector ` 10 `；EOL ` RVA 0x34BC7228 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8e131be32c9f616d](../../evidence/conditions-sets-055.md#c-8e131be32c9f616d) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-050987

```text
(config)# no do-exec show x25 context xot <cr>
```

Handler ` RVA 0x105F32F0 `；selector ` 7 `；EOL ` RVA 0x34BC6ED8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-051083

```text
(config)# no do-exec show x25 cug local-cug <cr>
```

Handler ` RVA 0x105F32F0 `；selector ` 11 `；EOL ` RVA 0x34BC8860 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-854c3491d5994616](../../evidence/conditions-sets-052.md#c-854c3491d5994616) · [状态效果 S-0bc9df7f7fada87c](../../evidence/state_effects-sets-003.md#s-0bc9df7f7fada87c)

### path-042288

```text
(config)# no do-exec show x25 hunt-group <cr>
```

Handler ` RVA 0x10618C60 `；selector ` 12 `；EOL ` RVA 0x34BC6948 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-042237

```text
(config)# no do-exec show x25 map <cr>
```

Handler ` RVA 0x105F30D0 `；selector ` 1 `；EOL ` RVA 0x34BC6638 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-042388

```text
(config)# no do-exec show x25 profile <cr>
```

Handler ` RVA 0x105F32F0 `；selector ` 9 `；EOL ` RVA 0x34BC7D38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-854c3491d5994616](../../evidence/conditions-sets-052.md#c-854c3491d5994616) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-042488

```text
(config)# no do-exec show x25 remote-red <cr>
```

Handler ` RVA 0x1061D4F0 `；selector ` 0 `；EOL ` RVA 0x34BD4A70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-854c3491d5994616](../../evidence/conditions-sets-052.md#c-854c3491d5994616) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-042278

```text
(config)# no do-exec show x25 route <cr>
```

Handler ` RVA 0x1060FFA0 `；selector ` 3 `；EOL ` RVA 0x34BC6BC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-042391

```text
(config)# no do-exec show x25 vc <cr>
```

Handler ` RVA 0x105F32F0 `；selector ` 4 `；EOL ` RVA 0x34BC7880 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-854c3491d5994616](../../evidence/conditions-sets-052.md#c-854c3491d5994616) · [状态效果 S-d00588379449a8d5](../../evidence/state_effects-sets-044.md#s-d00588379449a8d5)

### path-042440

```text
(config)# no do-exec show x25 xot <cr>
```

Handler ` RVA 0x105F32F0 `；selector ` 5 `；EOL ` RVA 0x34BC8450 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-854c3491d5994616](../../evidence/conditions-sets-052.md#c-854c3491d5994616) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-051063

```text
(config)# no do-exec show x25 xot access-group <cr>
```

Handler ` RVA 0x105F32F0 `；selector ` 6 `；EOL ` RVA 0x34BC8088 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-854c3491d5994616](../../evidence/conditions-sets-052.md#c-854c3491d5994616) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-041294

```text
(config)# no do-exec show x28 hunt-group <cr>
```

Handler ` RVA 0xFE6C310 `；selector ` 0 `；EOL ` RVA 0x34900498 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-f22b26b3fb147d91](../../evidence/state_effects-sets-051.md#s-f22b26b3fb147d91)

### path-041288

```text
(config)# no do-exec show x29 access-lists <cr>
```

Handler ` RVA 0xFE717E0 `；selector ` 0 `；EOL ` RVA 0x349007E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-049309

```text
(config)# no do-exec show xdr client all <cr>
```

Handler ` RVA 0x10C95110 `；selector ` 0 `；EOL ` RVA 0x34CF50F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0ccfba415f8b0b4f](../../evidence/state_effects-sets-003.md#s-0ccfba415f8b0b4f)

### path-040315

```text
(config)# no do-exec show xdr linecard <cr>
```

Handler ` RVA 0x10C95780 `；selector ` 0 `；EOL ` RVA 0x34D003F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c9662fe75da19290](../../evidence/conditions-sets-078.md#c-c9662fe75da19290) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-040276

```text
(config)# no do-exec show xdr memory <cr>
```

Handler ` RVA 0x10C96910 `；selector ` 0 `；EOL ` RVA 0x34CF56C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-040145

```text
(config)# no do-exec show xdr multicast-group <cr>
```

Handler ` RVA 0x10C95720 `；selector ` 0 `；EOL ` RVA 0x34CF4D28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-049211

```text
(config)# no do-exec show xdr statistics timers <cr>
```

Handler ` RVA 0xB319600 `；selector ` 0 `；EOL ` RVA 0x33738C60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-16e2e6ace51625ba](../../evidence/state_effects-sets-005.md#s-16e2e6ace51625ba)

### path-040176

```text
(config)# no do-exec show xdr timers <cr>
```

Handler ` RVA 0x10C96830 `；selector ` 0 `；EOL ` RVA 0x34CF53D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-051871

```text
(config)# no do-exec show xmpp profile connections <cr>
```

Handler ` RVA 0x12618B60 `；selector ` 0 `；EOL ` RVA 0x358C6178 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-08fafd3d8baf7876](../../evidence/conditions-sets-004.md#c-08fafd3d8baf7876) · [状态效果 S-7a314c78ab52b2b8](../../evidence/state_effects-sets-026.md#s-7a314c78ab52b2b8)

### path-033352

```text
(config)# no do-exec show xos <cr>
```

Handler ` RVA 0xDC718E0 `；selector ` 12 `；EOL ` RVA 0x340254E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-042730

```text
(config)# no do-exec show xos errors <cr>
```

Handler ` RVA 0xDC718E0 `；selector ` 2 `；EOL ` RVA 0x34023508 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-051348

```text
(config)# no do-exec show xos info xdm <cr>
```

Handler ` RVA 0xDCA7840 `；selector ` 0 `；EOL ` RVA 0x34026700 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-042997

```text
(config)# no do-exec show xos traces <cr>
```

Handler ` RVA 0xDC718E0 `；selector ` 1 `；EOL ` RVA 0x34025028 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-051412

```text
(config)# no do-exec show xos traces address <cr>
```

Handler ` RVA 0xDC718E0 `；selector ` 8 `；EOL ` RVA 0x34024AB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-051430

```text
(config)# no do-exec show xos traces interface <cr>
```

Handler ` RVA 0xDC718E0 `；selector ` 7 `；EOL ` RVA 0x34024D58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-051276

```text
(config)# no do-exec show xos traces ipc <cr>
```

Handler ` RVA 0xDC718E0 `；selector ` 4 `；EOL ` RVA 0x34023818 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-051299

```text
(config)# no do-exec show xos traces mgd <cr>
```

Handler ` RVA 0xDC718E0 `；selector ` 5 `；EOL ` RVA 0x34023AC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-051369

```text
(config)# no do-exec show xos traces packet <cr>
```

Handler ` RVA 0xDC718E0 `；selector ` 11 `；EOL ` RVA 0x340242B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-051381

```text
(config)# no do-exec show xos traces policy <cr>
```

Handler ` RVA 0xDC718E0 `；selector ` 10 `；EOL ` RVA 0x34024560 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-051398

```text
(config)# no do-exec show xos traces routing <cr>
```

Handler ` RVA 0xDC718E0 `；selector ` 9 `；EOL ` RVA 0x34024808 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-051325

```text
(config)# no do-exec show xos traces time <cr>
```

Handler ` RVA 0xDC718E0 `；selector ` 6 `；EOL ` RVA 0x34023D68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-051351

```text
(config)# no do-exec show xos traces utils <cr>
```

Handler ` RVA 0xDC718E0 `；selector ` 3 `；EOL ` RVA 0x34024010 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-051453

```text
(config)# no do-exec show xos traces xdm <cr>
```

Handler ` RVA 0xDC718E0 `；selector ` 13 `；EOL ` RVA 0x34025000 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-051667

```text
(config)# no do-exec show xsd-format cli <string> <cr>
```

Handler ` RVA 0xF414F30 `；selector ` 0 `；EOL ` RVA 0x34641B90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Enter the fully expanded command to display。

[条件 C-bb535702d0316d4b](../../evidence/conditions-sets-072.md#c-bb535702d0316d4b) · [参数 P-5385741c6a902cd0](../../evidence/parameters-sets-007.md#p-5385741c6a902cd0) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-027101

```text
(config)# no do-exec slip <cr>
```

Handler ` RVA 0xFF404B0 `；selector ` 0 `；EOL ` RVA 0x34933EE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-059335

```text
(config)# no do-exec snmp get-next v1 <string> <string> oid <string> <cr>
```

Handler ` RVA 0x10527C60 `；selector ` 0 `；EOL ` RVA 0x34B535A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` IP/IPv6 address or hostname of SNMP destination；` string ` SNMP community string；` string ` Object identifier value。

[条件 C-ea8b03e003992892](../../evidence/conditions-sets-091.md#c-ea8b03e003992892) · [参数 P-a202ce2166e2659e](../../evidence/parameters-sets-012.md#p-a202ce2166e2659e) · [状态效果 S-44490f5f65a00e12](../../evidence/state_effects-sets-015.md#s-44490f5f65a00e12)

### path-030085

```text
(config)# no do-exec ssh <string> <cr>
```

Handler ` RVA 0x1239B530 `；selector ` 0 `；EOL ` RVA 0x35829648 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` IP address or hostname of a remote system。

[条件 C-9b886337a61fd34b](../../evidence/conditions-sets-060.md#c-9b886337a61fd34b) · [参数 P-4f9aee87c0358682](../../evidence/parameters-sets-007.md#p-4f9aee87c0358682) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-026445

```text
(config)# no do-exec systat <cr>
```

Handler ` RVA 0xDFE03B0 `；selector ` 0 `；EOL ` RVA 0x3415D448 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-9626c53f680f99e8](../../evidence/conditions-sets-058.md#c-9626c53f680f99e8) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-027846

```text
(config)# no do-exec system kexecreload <cr>
```

Handler ` RVA 0xEA264C0 `；selector ` 0 `；EOL ` RVA 0x34391FD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-bc366d020d79028c](../../evidence/conditions-sets-073.md#c-bc366d020d79028c) · [状态效果 S-0108c77946749f46](../../evidence/state_effects-sets-001.md#s-0108c77946749f46)

### path-027237

```text
(config)# no do-exec tclquit <cr>
```

Handler ` RVA 0x11148A70 `；selector ` 0 `；EOL ` RVA 0x3540BD00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-027242

```text
(config)# no do-exec tclsh <cr>
```

Handler ` RVA 0x11148210 `；selector ` 0 `；EOL ` RVA 0x3540BA48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-026953

```text
(config)# no do-exec telnet <cr>
```

Handler ` RVA 0xDE84C20 `；selector ` 1 `；EOL ` RVA 0x33CF53F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-2e9ac9867a1896cc](../../evidence/conditions-sets-018.md#c-2e9ac9867a1896cc) · [状态效果 S-62bacb89ef74ea91](../../evidence/state_effects-sets-021.md#s-62bacb89ef74ea91)

### path-026974

```text
(config)# no do-exec telnet <cr>
```

Handler ` RVA 0xDE84C20 `；selector ` 0 `；EOL ` RVA 0x33CF56B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-bf79bfe0e43c8657](../../evidence/conditions-sets-074.md#c-bf79bfe0e43c8657) · [状态效果 S-62bacb89ef74ea91](../../evidence/state_effects-sets-021.md#s-62bacb89ef74ea91)

### path-026975

```text
(config)# no do-exec telnet <cr>
```

Handler ` RVA 0xCE631F0 `；selector ` 0 `；EOL ` RVA 0x33CF56E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-2835b6697c1b4758](../../evidence/conditions-sets-016.md#c-2835b6697c1b4758) · [状态效果 S-62bacb89ef74ea91](../../evidence/state_effects-sets-021.md#s-62bacb89ef74ea91)

### path-052165

```text
(config)# no do-exec test aaa accounting giga <number:0..4294967295> <cr>
```

Handler ` RVA 0xDD442B0 `；selector ` 0 `；EOL ` RVA 0x341ABD68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Number of false octets to inject。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-65993c2a8a783504](../../evidence/parameters-sets-008.md#p-65993c2a8a783504) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-044187

```text
(config)# no do-exec test aaa accounting init <cr>
```

Handler ` RVA 0xDD65930 `；selector ` 0 `；EOL ` RVA 0x341ABFF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-36cd69487a314fdb](../../evidence/state_effects-sets-012.md#s-36cd69487a314fdb)

### path-056789

```text
(config)# no do-exec test aaa accounting inject <number:0..4294967295> <number:0..4294967295> <cr>
```

Handler ` RVA 0xDD44310 `；selector ` 0 `；EOL ` RVA 0x341ABA78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` AAA unique ID；` unsigned_number ` Number of false octets to inject。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-9be70d404a095c21](../../evidence/parameters-sets-012.md#p-9be70d404a095c21) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-058999

```text
(config)# no do-exec test aaa accounting service auth-proxy <string> <string> <cr>
```

Handler ` RVA 0xDD179E0 `；selector ` 0 `；EOL ` RVA 0x341AC978 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Accounting Methodlist；` string ` username。

[条件 C-40315ef3a97af7fa](../../evidence/conditions-sets-025.md#c-40315ef3a97af7fa) · [参数 P-c06389cf0a4bcf06](../../evidence/parameters-sets-015.md#p-c06389cf0a4bcf06) · [状态效果 S-c55d9feaee9a3bc0](../../evidence/state_effects-sets-042.md#s-c55d9feaee9a3bc0)

### path-044182

```text
(config)# no do-exec test aaa authentication abort <cr>
```

Handler ` RVA 0xDD4D8B0 `；selector ` 0 `；EOL ` RVA 0x341AE288 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-87c7f8659cad5537](../../evidence/state_effects-sets-029.md#s-87c7f8659cad5537)

### path-052614

```text
(config)# no do-exec test aaa authentication attrlist <string> <cr>
```

Handler ` RVA 0xDD4DC50 `；selector ` 0 `；EOL ` RVA 0x341ADFA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Attribute list name。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-87a952c7d9a64896](../../evidence/parameters-sets-010.md#p-87a952c7d9a64896) · [状态效果 S-182a6e87dc6f8fdf](../../evidence/state_effects-sets-006.md#s-182a6e87dc6f8fdf)

### path-052556

```text
(config)# no do-exec test aaa authorization attrlist <string> <cr>
```

Handler ` RVA 0xDD4DC50 `；selector ` 0 `；EOL ` RVA 0x341AF0C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Attribute list name。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-79484ab68c124330](../../evidence/parameters-sets-009.md#p-79484ab68c124330) · [状态效果 S-f8284655fad365e5](../../evidence/state_effects-sets-053.md#s-f8284655fad365e5)

### path-056885

```text
(config)# no do-exec test aaa group diameter dcca <number:0..99> <cr>
```

Handler ` RVA 0xDD18270 `；selector ` 0 `；EOL ` RVA 0x341AFE28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Enter the diameter attribute list number。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-b0bda376f013743d](../../evidence/parameters-sets-013.md#p-b0bda376f013743d) · [状态效果 S-1c26be0d1924cb71](../../evidence/state_effects-sets-006.md#s-1c26be0d1924cb71)

### path-052125

```text
(config)# no do-exec test aaa radius inject <string> <cr>
```

Handler ` RVA 0xDD18CA0 `；selector ` 0 `；EOL ` RVA 0x341AB6D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Radius server group name。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-f574301c58aa9b22](../../evidence/parameters-sets-018.md#p-f574301c58aa9b22) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-034488

```text
(config)# no do-exec test aaa stop <cr>
```

Handler ` RVA 0xDD18270 `；selector ` 0 `；EOL ` RVA 0x341B0808 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-330c70eb7adb7e2c](../../evidence/state_effects-sets-011.md#s-330c70eb7adb7e2c)

### path-034885

```text
(config)# no do-exec test adj disable <cr>
```

Handler ` RVA 0xB56AF80 `；selector ` 0 `；EOL ` RVA 0x3379D968 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-2c941e45617bd836](../../evidence/conditions-sets-017.md#c-2c941e45617bd836) · [状态效果 S-cd49305b38bb7dca](../../evidence/state_effects-sets-043.md#s-cd49305b38bb7dca)

### path-045055

```text
(config)# no do-exec test adj epoch begin <cr>
```

Handler ` RVA 0xB56B6A0 `；selector ` 0 `；EOL ` RVA 0x3379E8B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-179a036f55ef2963](../../evidence/conditions-sets-009.md#c-179a036f55ef2963) · [状态效果 S-664a0da111c57403](../../evidence/state_effects-sets-022.md#s-664a0da111c57403)

### path-034948

```text
(config)# no do-exec test adj offset <cr>
```

Handler ` RVA 0xB56B070 `；selector ` 0 `；EOL ` RVA 0x3379DC20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f6f434259b142a2d](../../evidence/conditions-sets-095.md#c-f6f434259b142a2d) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-044735

```text
(config)# no do-exec test adj sev enable <cr>
```

Handler ` RVA 0xB564D50 `；selector ` 0 `；EOL ` RVA 0x3379DF70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a0a17499c63538f5](../../evidence/conditions-sets-062.md#c-a0a17499c63538f5) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-052664

```text
(config)# no do-exec test adj sev epoch <number:0..4294967295> <cr>
```

Handler ` RVA 0xB564CF0 `；selector ` 0 `；EOL ` RVA 0x3379E500 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Global sev epoch。

[条件 C-12b6d3341fbd681a](../../evidence/conditions-sets-007.md#c-12b6d3341fbd681a) · [参数 P-b3f3ee3cbe2fa639](../../evidence/parameters-sets-014.md#p-b3f3ee3cbe2fa639) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-044785

```text
(config)# no do-exec test adj sev oneshot <cr>
```

Handler ` RVA 0xB564DB0 `；selector ` 0 `；EOL ` RVA 0x3379E218 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-57f0e224494491d5](../../evidence/conditions-sets-034.md#c-57f0e224494491d5) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-028959

```text
(config)# no do-exec test ancp <cr>
```

Handler ` RVA 0xB259720 `；selector ` 2 `；EOL ` RVA 0x336DC4E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-0d3a603023ab964f](../../evidence/state_effects-sets-003.md#s-0d3a603023ab964f)

### path-037765

```text
(config)# no do-exec test application init <cr>
```

Handler ` RVA 0x1280FE90 `；selector ` 0 `；EOL ` RVA 0x358DB1B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-f6e84698a24dd2e2](../../evidence/state_effects-sets-052.md#s-f6e84698a24dd2e2)

### path-045000

```text
(config)# no do-exec test arp_retry add <address> <cr>
```

Handler ` RVA 0xCF70010 `；selector ` 0 `；EOL ` RVA 0x33D43BB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` ip address。

[条件 C-b0985c6bbeae9f7b](../../evidence/conditions-sets-068.md#c-b0985c6bbeae9f7b) · [参数 P-082fb47dada915b1](../../evidence/parameters-sets-001.md#p-082fb47dada915b1) · [状态效果 S-511133ebf08d2cf0](../../evidence/state_effects-sets-018.md#s-511133ebf08d2cf0)

### path-047260

```text
(config)# no do-exec test autoip fail control <cr>
```

Handler ` RVA 0xB2864E0 `；selector ` 0 `；EOL ` RVA 0x3372C400 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-047301

```text
(config)# no do-exec test autoip fail noncontrol <cr>
```

Handler ` RVA 0xB286660 `；selector ` 0 `；EOL ` RVA 0x3372C6A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-037906

```text
(config)# no do-exec test autoip start <cr>
```

Handler ` RVA 0xB2862B0 `；selector ` 0 `；EOL ` RVA 0x3372B8C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-037946

```text
(config)# no do-exec test autoip stop <cr>
```

Handler ` RVA 0xB286360 `；selector ` 0 `；EOL ` RVA 0x3372BB70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-047230

```text
(config)# no do-exec test autoip success control <cr>
```

Handler ` RVA 0xB286420 `；selector ` 0 `；EOL ` RVA 0x3372BE80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-047267

```text
(config)# no do-exec test autoip success noncontrol <cr>
```

Handler ` RVA 0xB2865A0 `；selector ` 0 `；EOL ` RVA 0x3372C128 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-057845

```text
(config)# no do-exec test avc sd-service auto-config is-bypass no <cr>
```

Handler ` RVA 0x10F47930 `；selector ` 18 `；EOL ` RVA 0x3526A0E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-057869

```text
(config)# no do-exec test avc sd-service auto-config is-bypass yes <cr>
```

Handler ` RVA 0x10F47930 `；selector ` 19 `；EOL ` RVA 0x3526A390 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-059299

```text
(config)# no do-exec test avc sd-service auto-config override-non-nbar-probes cdp no <cr>
```

Handler ` RVA 0x10F47930 `；selector ` 21 `；EOL ` RVA 0x3526A6D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-059305

```text
(config)# no do-exec test avc sd-service auto-config override-non-nbar-probes cdp yes <cr>
```

Handler ` RVA 0x10F47930 `；selector ` 20 `；EOL ` RVA 0x3526A978 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-059308

```text
(config)# no do-exec test avc sd-service auto-config override-non-nbar-probes dhcpv4 no <cr>
```

Handler ` RVA 0x10F47930 `；selector ` 25 `；EOL ` RVA 0x3526B220 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-059318

```text
(config)# no do-exec test avc sd-service auto-config override-non-nbar-probes dhcpv4 yes <cr>
```

Handler ` RVA 0x10F47930 `；selector ` 24 `；EOL ` RVA 0x3526B4C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-059316

```text
(config)# no do-exec test avc sd-service auto-config override-non-nbar-probes dhcpv6 no <cr>
```

Handler ` RVA 0x10F47930 `；selector ` 27 `；EOL ` RVA 0x3526B7A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-059326

```text
(config)# no do-exec test avc sd-service auto-config override-non-nbar-probes dhcpv6 yes <cr>
```

Handler ` RVA 0x10F47930 `；selector ` 26 `；EOL ` RVA 0x3526BA48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-059304

```text
(config)# no do-exec test avc sd-service auto-config override-non-nbar-probes lldp no <cr>
```

Handler ` RVA 0x10F47930 `；selector ` 23 `；EOL ` RVA 0x3526AC78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-059310

```text
(config)# no do-exec test avc sd-service auto-config override-non-nbar-probes lldp yes <cr>
```

Handler ` RVA 0x10F47930 `；selector ` 22 `；EOL ` RVA 0x3526AF20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-054092

```text
(config)# no do-exec test avc sd-service auto-config trigger <cr>
```

Handler ` RVA 0x10F47930 `；selector ` 17 `；EOL ` RVA 0x35269DD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-046814

```text
(config)# no do-exec test avc sd-service clear-all-export-caches <cr>
```

Handler ` RVA 0x10F47930 `；selector ` 28 `；EOL ` RVA 0x3526BD38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-053998

```text
(config)# no do-exec test avc sd-service cloud-config unload <cr>
```

Handler ` RVA 0x10F47930 `；selector ` 41 `；EOL ` RVA 0x352673B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-057632

```text
(config)# no do-exec test avc sd-service custom-id set <string> <cr>
```

Handler ` RVA 0x10F47930 `；selector ` 39 `；EOL ` RVA 0x35266270 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` custom ID string。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-9e40af97664c71c9](../../evidence/parameters-sets-012.md#p-9e40af97664c71c9) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-054260

```text
(config)# no do-exec test avc sd-service device-table-set-seq <number:0..65535> <cr>
```

Handler ` RVA 0x10F47930 `；selector ` 32 `；EOL ` RVA 0x3526E800 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Device table sequence number to set。

[条件 C-9a09478491f6b107](../../evidence/conditions-sets-060.md#c-9a09478491f6b107) · [参数 P-e3e5b21d608e0229](../../evidence/parameters-sets-017.md#p-e3e5b21d608e0229) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-059241

```text
(config)# no do-exec test avc sd-service ent device-health export trigger <cr>
```

Handler ` RVA 0x10F47930 `；selector ` 61 `；EOL ` RVA 0x35264A80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-053707

```text
(config)# no do-exec test avc sd-service ent disable <cr>
```

Handler ` RVA 0x10F47930 `；selector ` 55 `；EOL ` RVA 0x35262E28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-053667

```text
(config)# no do-exec test avc sd-service ent enable <cr>
```

Handler ` RVA 0x10F47930 `；selector ` 54 `；EOL ` RVA 0x35262B80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-057811

```text
(config)# no do-exec test avc sd-service ent export clear <cr>
```

Handler ` RVA 0x10F47930 `；selector ` 57 `；EOL ` RVA 0x35264738 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-057784

```text
(config)# no do-exec test avc sd-service ent export dump <cr>
```

Handler ` RVA 0x10F47930 `；selector ` 58 `；EOL ` RVA 0x35264490 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-057759

```text
(config)# no do-exec test avc sd-service ent export interfaces-db <cr>
```

Handler ` RVA 0x10F47930 `；selector ` 70 `；EOL ` RVA 0x352641E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-057766

```text
(config)# no do-exec test avc sd-service ent export protocols-db <cr>
```

Handler ` RVA 0x10F47930 `；selector ` 59 `；EOL ` RVA 0x35263D18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-059255

```text
(config)# no do-exec test avc sd-service ent export protocols-db size <cr>
```

Handler ` RVA 0x10F47930 `；selector ` 60 `；EOL ` RVA 0x35263CF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-057659

```text
(config)# no do-exec test avc sd-service ent export trigger <cr>
```

Handler ` RVA 0x10F47930 `；selector ` 53 `；EOL ` RVA 0x352636E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-053784

```text
(config)# no do-exec test avc sd-service ent unload <cr>
```

Handler ` RVA 0x10F47930 `；selector ` 52 `；EOL ` RVA 0x352633D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-054221

```text
(config)# no do-exec test avc sd-service flow-counters disable <cr>
```

Handler ` RVA 0x10F47930 `；selector ` 50 `；EOL ` RVA 0x3526D150 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-054201

```text
(config)# no do-exec test avc sd-service flow-counters enable <cr>
```

Handler ` RVA 0x10F47930 `；selector ` 49 `；EOL ` RVA 0x3526CEA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-054281

```text
(config)# no do-exec test avc sd-service force-using-binos-process no <cr>
```

Handler ` RVA 0x10F47930 `；selector ` 63 `；EOL ` RVA 0x3526ED98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a6ebeb1775300f4e](../../evidence/conditions-sets-064.md#c-a6ebeb1775300f4e) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-054271

```text
(config)# no do-exec test avc sd-service force-using-binos-process yes <cr>
```

Handler ` RVA 0x10F47930 `；selector ` 62 `；EOL ` RVA 0x3526EAF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a6ebeb1775300f4e](../../evidence/conditions-sets-064.md#c-a6ebeb1775300f4e) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-046868

```text
(config)# no do-exec test avc sd-service ftp-private-ip <cr>
```

Handler ` RVA 0x10F47930 `；selector ` 30 `；EOL ` RVA 0x3526C070 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-83466e608216da88](../../evidence/conditions-sets-051.md#c-83466e608216da88) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-046501

```text
(config)# no do-exec test avc sd-service load-telemetry <cr>
```

Handler ` RVA 0x10F47930 `；selector ` 4 `；EOL ` RVA 0x35266800 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-053778

```text
(config)# no do-exec test avc sd-service opaque-json get <cr>
```

Handler ` RVA 0x10F47930 `；selector ` 38 `；EOL ` RVA 0x35265F30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-060063

```text
(config)# no do-exec test avc sd-service packets-tx send payload-length <number:1..8192> packets-num <number:1..10000000> <cr>
```

Handler ` RVA 0x10F47930 `；selector ` 5 `；EOL ` RVA 0x352677C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Payload length of sent packets；` unsigned_number ` Number of packets to send。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-89ff9d125403462c](../../evidence/parameters-sets-011.md#p-89ff9d125403462c) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-054261

```text
(config)# no do-exec test avc sd-service permit-apps disable <cr>
```

Handler ` RVA 0x10F47930 `；selector ` 48 `；EOL ` RVA 0x3526E500 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-88d06c5c201bd48f](../../evidence/conditions-sets-053.md#c-88d06c5c201bd48f) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-054246

```text
(config)# no do-exec test avc sd-service permit-apps enable <cr>
```

Handler ` RVA 0x10F47930 `；selector ` 47 `；EOL ` RVA 0x3526E258 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-6814c4b058034c3c](../../evidence/conditions-sets-040.md#c-6814c4b058034c3c) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-054182

```text
(config)# no do-exec test avc sd-service persistency no <cr>
```

Handler ` RVA 0x10F47930 `；selector ` 34 `；EOL ` RVA 0x3526C900 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-054205

```text
(config)# no do-exec test avc sd-service persistency yes <cr>
```

Handler ` RVA 0x10F47930 `；selector ` 33 `；EOL ` RVA 0x3526CBA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-054155

```text
(config)# no do-exec test avc sd-service ppack-mode allow <cr>
```

Handler ` RVA 0x10F47930 `；selector ` 35 `；EOL ` RVA 0x3526C358 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-054186

```text
(config)# no do-exec test avc sd-service ppack-mode disallow <cr>
```

Handler ` RVA 0x10F47930 `；selector ` 36 `；EOL ` RVA 0x3526C600 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-059300

```text
(config)# no do-exec test avc sd-service scheduled-export debug-header length <number:0..4096> <cr>
```

Handler ` RVA 0x10F47930 `；selector ` 31 `；EOL ` RVA 0x35268EF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Length of debug element added to header of every message。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-e03dea87d80e8909](../../evidence/parameters-sets-017.md#p-e03dea87d80e8909) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-057819

```text
(config)# no do-exec test avc sd-service scheduled-export is-bypass no <cr>
```

Handler ` RVA 0x10F47930 `；selector ` 7 `；EOL ` RVA 0x35267DE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-057834

```text
(config)# no do-exec test avc sd-service scheduled-export is-bypass yes <cr>
```

Handler ` RVA 0x10F47930 `；selector ` 8 `；EOL ` RVA 0x35268090 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-057872

```text
(config)# no do-exec test avc sd-service scheduled-export rate-control Disable <cr>
```

Handler ` RVA 0x10F47930 `；selector ` 12 `；EOL ` RVA 0x35268BE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-057850

```text
(config)# no do-exec test avc sd-service scheduled-export rate-control Enable <cr>
```

Handler ` RVA 0x10F47930 `；selector ` 11 `；EOL ` RVA 0x35268938 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-057832

```text
(config)# no do-exec test avc sd-service scheduled-export transport http <cr>
```

Handler ` RVA 0x10F47930 `；selector ` 10 `；EOL ` RVA 0x35268390 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-057854

```text
(config)# no do-exec test avc sd-service scheduled-export transport udp <cr>
```

Handler ` RVA 0x10F47930 `；selector ` 9 `；EOL ` RVA 0x35268638 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-054031

```text
(config)# no do-exec test avc sd-service scheduled-export trigger <cr>
```

Handler ` RVA 0x10F47930 `；selector ` 6 `；EOL ` RVA 0x35267AD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-057831

```text
(config)# no do-exec test avc sd-service scheduled-import is-bypass no <cr>
```

Handler ` RVA 0x10F47930 `；selector ` 14 `；EOL ` RVA 0x35269540 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-057853

```text
(config)# no do-exec test avc sd-service scheduled-import is-bypass yes <cr>
```

Handler ` RVA 0x10F47930 `；selector ` 15 `；EOL ` RVA 0x352697E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-057849

```text
(config)# no do-exec test avc sd-service scheduled-import time-to-keep-files <number:0..10000000> <cr>
```

Handler ` RVA 0x10F47930 `；selector ` 16 `；EOL ` RVA 0x35269AC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Time in seconds to keep files。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-736053c924a8b930](../../evidence/parameters-sets-009.md#p-736053c924a8b930) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-054067

```text
(config)# no do-exec test avc sd-service scheduled-import trigger <cr>
```

Handler ` RVA 0x10F47930 `；selector ` 13 `；EOL ` RVA 0x35269230 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-053957

```text
(config)# no do-exec test avc sd-service telemetry off <cr>
```

Handler ` RVA 0x10F47930 `；selector ` 3 `；EOL ` RVA 0x35266DB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-053894

```text
(config)# no do-exec test avc sd-service telemetry on <cr>
```

Handler ` RVA 0x10F47930 `；selector ` 2 `；EOL ` RVA 0x35266B10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-046976

```text
(config)# no do-exec test avc sd-service testbench <cr>
```

Handler ` RVA 0x10F47930 `；selector ` 29 `；EOL ` RVA 0x3526DF48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-053743

```text
(config)# no do-exec test avc sd-service tls-fp disable <cr>
```

Handler ` RVA 0x10F47930 `；selector ` 66 `；EOL ` RVA 0x35265070 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0d9b2739f32355ca](../../evidence/conditions-sets-006.md#c-0d9b2739f32355ca) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-053701

```text
(config)# no do-exec test avc sd-service tls-fp enable <cr>
```

Handler ` RVA 0x10F47930 `；selector ` 65 `；EOL ` RVA 0x35264DC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b11d8b416460af1c](../../evidence/conditions-sets-068.md#c-b11d8b416460af1c) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-053817

```text
(config)# no do-exec test avc sd-service tls-fp unload <cr>
```

Handler ` RVA 0x10F47930 `；selector ` 69 `；EOL ` RVA 0x35265918 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0d9b2739f32355ca](../../evidence/conditions-sets-006.md#c-0d9b2739f32355ca) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-054234

```text
(config)# no do-exec test avc sd-service unclassified-domains disable <cr>
```

Handler ` RVA 0x10F47930 `；selector ` 44 `；EOL ` RVA 0x3526D6F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-054216

```text
(config)# no do-exec test avc sd-service unclassified-domains enable <cr>
```

Handler ` RVA 0x10F47930 `；selector ` 43 `；EOL ` RVA 0x3526D450 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-057928

```text
(config)# no do-exec test avc sd-service unclassified-domains local disable <cr>
```

Handler ` RVA 0x10F47930 `；selector ` 46 `；EOL ` RVA 0x3526DC88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-057924

```text
(config)# no do-exec test avc sd-service unclassified-domains local enable <cr>
```

Handler ` RVA 0x10F47930 `；selector ` 45 `；EOL ` RVA 0x3526D9E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-048368

```text
(config)# no do-exec test beep basic <string> <cr>
```

Handler ` RVA 0xEF96A40 `；selector ` 0 `；EOL ` RVA 0x3448D2D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` BEEP session to connect with。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-b36e6e16e0954e4a](../../evidence/parameters-sets-014.md#p-b36e6e16e0954e4a) · [状态效果 S-9b4b86925ea497ac](../../evidence/state_effects-sets-033.md#s-9b4b86925ea497ac)

### path-054804

```text
(config)# no do-exec test beep raw bing data <cr>
```

Handler ` RVA 0xEF95AF0 `；selector ` 0 `；EOL ` RVA 0x3448D6C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-47fa96d6e8cc5c53](../../evidence/state_effects-sets-016.md#s-47fa96d6e8cc5c53)

### path-044801

```text
(config)# no do-exec test bridge-domain api vni <cr>
```

Handler ` RVA 0xBF38E00 `；selector ` 4 `；EOL ` RVA 0x339547C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-044590

```text
(config)# no do-exec test bridge-domain ipc all-slots <cr>
```

Handler ` RVA 0xBF38E00 `；selector ` 0 `；EOL ` RVA 0x339543F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-c1a3e6099fdc4b96](../../evidence/state_effects-sets-041.md#s-c1a3e6099fdc4b96)

### path-035031

```text
(config)# no do-exec test bridge-domain other <cr>
```

Handler ` RVA 0xBF38E00 `；selector ` 1 `；EOL ` RVA 0x33954F50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-059020

```text
(config)# no do-exec test bridge-domain pw-reconciliation pp peer <address> <number:1..4294967295> <cr>
```

Handler ` RVA 0xBF38E00 `；selector ` 2 `；EOL ` RVA 0x33955348 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` Peer IP address；` unsigned_number ` VC ID。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-4b6f8228caddc150](../../evidence/parameters-sets-006.md#p-4b6f8228caddc150) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-059028

```text
(config)# no do-exec test bridge-domain pw-reconciliation static-mac peer <address> <number:1..4294967295> <cr>
```

Handler ` RVA 0xBF38E00 `；selector ` 3 `；EOL ` RVA 0x339556A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` VFI neighbor's router id；` unsigned_number ` Enter VC ID value。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-33c23e217a8c152f](../../evidence/parameters-sets-004.md#p-33c23e217a8c152f) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-052692

```text
(config)# no do-exec test bridge-domain tcn receive <number:1..4096> <cr>
```

Handler ` RVA 0xBF38E00 `；selector ` 5 `；EOL ` RVA 0x33955A18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` BD ID value。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-93c1740f5d8dff1c](../../evidence/parameters-sets-011.md#p-93c1740f5d8dff1c) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-057955

```text
(config)# no do-exec test buffer get <string> <string> <number:0..4294967294> <cr>
```

Handler ` RVA 0xD79D0B0 `；selector ` 0 `；EOL ` RVA 0x33EEB328 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` RU name；` string ` name of the pool；` unsigned_number ` Number of buffers to allocate。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-3031423b01501369](../../evidence/parameters-sets-004.md#p-3031423b01501369) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-047232

```text
(config)# no do-exec test buffer tuning elements <cr>
```

Handler ` RVA 0xD79D4B0 `；selector ` 0 `；EOL ` RVA 0x33EEBC20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-054428

```text
(config)# no do-exec test buffer tuning pool <string> <cr>
```

Handler ` RVA 0xD79D340 `；selector ` 0 `；EOL ` RVA 0x33EEBF48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` name of the pool。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-4b7e32a76f1a1c6b](../../evidence/parameters-sets-006.md#p-4b7e32a76f1a1c6b) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-034247

```text
(config)# no do-exec test c3pl stop <cr>
```

Handler ` RVA 0xD8A8F00 `；selector ` 0 `；EOL ` RVA 0x33F2B720 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5830026eb3068fca](../../evidence/conditions-sets-035.md#c-5830026eb3068fca) · [状态效果 S-4bf96def9d729c34](../../evidence/state_effects-sets-017.md#s-4bf96def9d729c34)

### path-029505

```text
(config)# no do-exec test cce <cr>
```

Handler ` RVA 0xDCBDBD0 `；selector ` 0 `；EOL ` RVA 0x34038A08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c0551e683ee64503](../../evidence/conditions-sets-074.md#c-c0551e683ee64503) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-052233

```text
(config)# no do-exec test cdna register <string> <number:0..4294967295> <cr>
```

Handler ` RVA 0xB7C8320 `；selector ` 1 `；EOL ` RVA 0x3380D468 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` throughput license name string；` unsigned_number ` throughput in MB。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-60aef765e41606f8](../../evidence/parameters-sets-008.md#p-60aef765e41606f8) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-044298

```text
(config)# no do-exec test cdna release <string> <cr>
```

Handler ` RVA 0xB7C8320 `；selector ` 3 `；EOL ` RVA 0x3380DA40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` release registed feature。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-9e8a28d3829903f6](../../evidence/parameters-sets-012.md#p-9e8a28d3829903f6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-044267

```text
(config)# no do-exec test cdna request <string> <cr>
```

Handler ` RVA 0xB7C8320 `；selector ` 2 `；EOL ` RVA 0x3380D758 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` request registed feature。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-efe1450a01da611b](../../evidence/parameters-sets-018.md#p-efe1450a01da611b) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-034561

```text
(config)# no do-exec test cdna reset <cr>
```

Handler ` RVA 0xB7C8320 `；selector ` 4 `；EOL ` RVA 0x3380DCC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-045032

```text
(config)# no do-exec test cef crimson-oper-db add <cr>
```

Handler ` RVA 0xB369C80 `；selector ` 0 `；EOL ` RVA 0x337520E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-10b1979508e04de9](../../evidence/conditions-sets-007.md#c-10b1979508e04de9) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-045076

```text
(config)# no do-exec test cef crimson-oper-db del <cr>
```

Handler ` RVA 0xB369CF0 `；selector ` 0 `；EOL ` RVA 0x33752388 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-fd0f47df170f1d69](../../evidence/conditions-sets-098.md#c-fd0f47df170f1d69) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-044950

```text
(config)# no do-exec test cef crimson-oper-db disable <cr>
```

Handler ` RVA 0xB369B50 `；selector ` 0 `；EOL ` RVA 0x33751830 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f945adc87c8d7315](../../evidence/conditions-sets-096.md#c-f945adc87c8d7315) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-044914

```text
(config)# no do-exec test cef crimson-oper-db enable <cr>
```

Handler ` RVA 0xB369AE0 `；selector ` 0 `；EOL ` RVA 0x33751588 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-344052f2725b19c4](../../evidence/conditions-sets-020.md#c-344052f2725b19c4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-052805

```text
(config)# no do-exec test cef crimson-oper-db oc-nh-grp-db IPv4 <cr>
```

Handler ` RVA 0xB369BC0 `；selector ` 0 `；EOL ` RVA 0x33751C08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-9857a820d2e2129e](../../evidence/conditions-sets-059.md#c-9857a820d2e2129e) · [状态效果 S-ee413d1d0114aeee](../../evidence/state_effects-sets-050.md#s-ee413d1d0114aeee)

### path-034891

```text
(config)# no do-exec test cef enable <cr>
```

Handler ` RVA 0xB480BC0 `；selector ` 0 `；EOL ` RVA 0x3374CCE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-71e289f25df36c27](../../evidence/conditions-sets-044.md#c-71e289f25df36c27) · [状态效果 S-7353509732e9f4b7](../../evidence/state_effects-sets-025.md#s-7353509732e9f4b7)

### path-052811

```text
(config)# no do-exec test cef event-trace IPv4 <string> <cr>
```

Handler ` RVA 0xB47E360 `；selector ` 0 `；EOL ` RVA 0x33764268 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` String to insert into event log。

[条件 C-f85779ff9a12c23c](../../evidence/conditions-sets-096.md#c-f85779ff9a12c23c) · [参数 P-c31ab8da975e92c0](../../evidence/parameters-sets-015.md#p-c31ab8da975e92c0) · [状态效果 S-f6613869a3ec52e4](../../evidence/state_effects-sets-052.md#s-f6613869a3ec52e4)

### path-044986

```text
(config)# no do-exec test cef ext-lb disable <cr>
```

Handler ` RVA 0xB3F0520 `；selector ` 1 `；EOL ` RVA 0x33753078 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7e674079c9d5e5bf](../../evidence/conditions-sets-049.md#c-7e674079c9d5e5bf) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-044985

```text
(config)# no do-exec test cef ext-lb enable <cr>
```

Handler ` RVA 0xB3F0520 `；selector ` 0 `；EOL ` RVA 0x33752DC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-bcd4bc85b21c9ac8](../../evidence/conditions-sets-073.md#c-bcd4bc85b21c9ac8) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-053013

```text
(config)# no do-exec test cef get-nexthop-adj IPv4 <address> <cr>
```

Handler ` RVA 0xB419330 `；selector ` 0 `；EOL ` RVA 0x33755FA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` Prefix of interest。

[条件 C-e1152de66941f30f](../../evidence/conditions-sets-087.md#c-e1152de66941f30f) · [参数 P-cec27e68cf98fe44](../../evidence/parameters-sets-016.md#p-cec27e68cf98fe44) · [状态效果 S-fce4f60abae833d0](../../evidence/state_effects-sets-054.md#s-fce4f60abae833d0)

### path-045097

```text
(config)# no do-exec test cef idb consistency <cr>
```

Handler ` RVA 0xB3DD800 `；selector ` 0 `；EOL ` RVA 0x33754490 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-6da3a09591ea7b95](../../evidence/conditions-sets-042.md#c-6da3a09591ea7b95) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-059701

```text
(config)# no do-exec test cef lisp l2instance create <number:0..65520> <number:0..65520> <number:1..4094> <cr>
```

Handler ` RVA 0xB369280 `；selector ` 0 `；EOL ` RVA 0x3374F290 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Topology ID；` unsigned_number ` Instance ID；` unsigned_number ` L2 Domain ID。

[条件 C-939762f2d506bdf0](../../evidence/conditions-sets-057.md#c-939762f2d506bdf0) · [参数 P-418c739674d1ed69](../../evidence/parameters-sets-006.md#p-418c739674d1ed69) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-059707

```text
(config)# no do-exec test cef lisp map-req IPv4 <address> <address> r-eid <cr>
```

Handler ` RVA 0xB368BF0 `；selector ` 0 `；EOL ` RVA 0x3374EC28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` Src Addr；` address ` Dst Addr。

[条件 C-eb7803fd2758bcb1](../../evidence/conditions-sets-091.md#c-eb7803fd2758bcb1) · [参数 P-a9fceed457be317e](../../evidence/parameters-sets-013.md#p-a9fceed457be317e) · [状态效果 S-498ac363dea4519d](../../evidence/state_effects-sets-016.md#s-498ac363dea4519d)

### path-057079

```text
(config)# no do-exec test cef lisp stats IPv4 clear <cr>
```

Handler ` RVA 0xB367480 `；selector ` 0 `；EOL ` RVA 0x3374FDD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-05c741388770c820](../../evidence/conditions-sets-003.md#c-05c741388770c820) · [状态效果 S-532e10f3c44dcd45](../../evidence/state_effects-sets-018.md#s-532e10f3c44dcd45)

### path-057097

```text
(config)# no do-exec test cef lisp sw-fw eid-detection enable <cr>
```

Handler ` RVA 0xB3696E0 `；selector ` 0 `；EOL ` RVA 0x33750950 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-767e2026818adc87](../../evidence/conditions-sets-046.md#c-767e2026818adc87) · [状态效果 S-cdb169309d1ce504](../../evidence/state_effects-sets-044.md#s-cdb169309d1ce504)

### path-059054

```text
(config)# no do-exec test cef lisp unnum-if top-id <number:0..65520> clear-v4 <cr>
```

Handler ` RVA 0xB3693E0 `；selector ` 0 `；EOL ` RVA 0x3374F7E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Topology ID。

[条件 C-a27f76df5f88e7bd](../../evidence/conditions-sets-063.md#c-a27f76df5f88e7bd) · [参数 P-05b6f7fd71866fd1](../../evidence/parameters-sets-001.md#p-05b6f7fd71866fd1) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-044774

```text
(config)# no do-exec test cef lisp_samecable <address> <cr>
```

Handler ` RVA 0xB368A00 `；selector ` 0 `；EOL ` RVA 0x3374E5B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` IPv4 Address。

[条件 C-b280d06b9c450e6d](../../evidence/conditions-sets-069.md#c-b280d06b9c450e6d) · [参数 P-7cbacb70d6c94687](../../evidence/parameters-sets-010.md#p-7cbacb70d6c94687) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-052982

```text
(config)# no do-exec test cef oce-explore IPv4 <address> <cr>
```

Handler ` RVA 0xB419590 `；selector ` 0 `；EOL ` RVA 0x337558B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` Prefix of interest。

[条件 C-3ad4c58cf1ded92b](../../evidence/conditions-sets-023.md#c-3ad4c58cf1ded92b) · [参数 P-8b695f8397dd7da3](../../evidence/parameters-sets-011.md#p-8b695f8397dd7da3) · [状态效果 S-8761ad4d9a506896](../../evidence/state_effects-sets-029.md#s-8761ad4d9a506896)

### path-035033

```text
(config)# no do-exec test cef offset <cr>
```

Handler ` RVA 0xB35E1A0 `；selector ` 0 `；EOL ` RVA 0x3374E258 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-dc4fa007aa084224](../../evidence/conditions-sets-085.md#c-dc4fa007aa084224) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-045133

```text
(config)# no do-exec test cef register-interest show <cr>
```

Handler ` RVA 0xB3A90C0 `；selector ` 0 `；EOL ` RVA 0x33754D20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8d2d1f1a717981c2](../../evidence/conditions-sets-055.md#c-8d2d1f1a717981c2) · [状态效果 S-f0ad12e00d0f7876](../../evidence/state_effects-sets-051.md#s-f0ad12e00d0f7876)

### path-045014

```text
(config)# no do-exec test cef sadr-oce <address> <cr>
```

Handler ` RVA 0xB369F40 `；selector ` 0 `；EOL ` RVA 0x33753C20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` IPv4 Address。

[条件 C-5987672af60d653c](../../evidence/conditions-sets-035.md#c-5987672af60d653c) · [参数 P-ae52a741803cbe9b](../../evidence/parameters-sets-013.md#p-ae52a741803cbe9b) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-052650

```text
(config)# no do-exec test cef switching IPv4 clear <cr>
```

Handler ` RVA 0xB4561F0 `；selector ` 0 `；EOL ` RVA 0x3374D358 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-2b81d13bff9f87c3](../../evidence/conditions-sets-017.md#c-2b81d13bff9f87c3) · [状态效果 S-49b247eb4d4c15b8](../../evidence/state_effects-sets-016.md#s-49b247eb4d4c15b8)

### path-053129

```text
(config)# no do-exec test cef track-destination IPv4 local-label <cr>
```

Handler ` RVA 0xB418EB0 `；selector ` 0 `；EOL ` RVA 0x33756740 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7b041c77c77a89b0](../../evidence/conditions-sets-048.md#c-7b041c77c77a89b0) · [状态效果 S-b66a00066634551a](../../evidence/state_effects-sets-039.md#s-b66a00066634551a)

### path-045427

```text
(config)# no do-exec test cef user-command <number:1..255> <cr>
```

Handler ` RVA 0xB485500 `；selector ` 0 `；EOL ` RVA 0x33756D08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` User-command command number。

[条件 C-007620b9fa604aea](../../evidence/conditions-sets-001.md#c-007620b9fa604aea) · [参数 P-991dea8e01a30443](../../evidence/parameters-sets-012.md#p-991dea8e01a30443) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-034741

```text
(config)# no do-exec test checkpoint add <cr>
```

Handler ` RVA 0xCDD0C40 `；selector ` 0 `；EOL ` RVA 0x33CF0A50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-ea6f119509d8a56a](../../evidence/state_effects-sets-050.md#s-ea6f119509d8a56a)

### path-035103

```text
(config)# no do-exec test cisp disable <cr>
```

Handler ` RVA 0xCB25570 `；selector ` 0 `；EOL ` RVA 0x33BB54C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7568087aa5df99c9](../../evidence/conditions-sets-046.md#c-7568087aa5df99c9) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-035104

```text
(config)# no do-exec test cisp enable <cr>
```

Handler ` RVA 0xCB254F0 `；selector ` 0 `；EOL ` RVA 0x33BB67C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7826896257e4387c](../../evidence/conditions-sets-047.md#c-7826896257e4387c) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-038997

```text
(config)# no do-exec test clear-nvram local-lock <cr>
```

Handler ` RVA 0xE0E2710 `；selector ` 0 `；EOL ` RVA 0x341FA0D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-052336

```text
(config)# no do-exec test cli-agent config-accounting test-mode disable <cr>
```

Handler ` RVA 0x143F2DB0 `；selector ` 1 `；EOL ` RVA 0x35D5DCE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f42a4947ee5384e5](../../evidence/conditions-sets-094.md#c-f42a4947ee5384e5) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-052303

```text
(config)# no do-exec test cli-agent config-accounting test-mode enable <cr>
```

Handler ` RVA 0x143F2DB0 `；selector ` 0 `；EOL ` RVA 0x35D5DA40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d854b211a95e2849](../../evidence/conditions-sets-083.md#c-d854b211a95e2849) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-039349

```text
(config)# no do-exec test cns history <cr>
```

Handler ` RVA 0xF338C70 `；selector ` 1 `；EOL ` RVA 0x34612D00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-039468

```text
(config)# no do-exec test cns inventory <cr>
```

Handler ` RVA 0xF338C70 `；selector ` 2 `；EOL ` RVA 0x34613250 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-039400

```text
(config)# no do-exec test cns summary <cr>
```

Handler ` RVA 0xF338C70 `；selector ` 3 `；EOL ` RVA 0x34612FA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-053926

```text
(config)# no do-exec test cops start-listen <address> <number:0..65535> <cr>
```

Handler ` RVA 0xF44A4B0 `；selector ` 1 `；EOL ` RVA 0x3464CA28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` IP address to listen for；` unsigned_number ` port number。

[条件 C-c804a50dadac8b22](../../evidence/conditions-sets-077.md#c-c804a50dadac8b22) · [参数 P-1c899d9a6cba1e7a](../../evidence/parameters-sets-003.md#p-1c899d9a6cba1e7a) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-053980

```text
(config)# no do-exec test cops stop-listen <address> <number:0..65535> <cr>
```

Handler ` RVA 0xF44A4B0 `；selector ` 2 `；EOL ` RVA 0x3464CD30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` IP address to stop listening for；` unsigned_number ` port number。

[条件 C-c804a50dadac8b22](../../evidence/conditions-sets-077.md#c-c804a50dadac8b22) · [参数 P-365bcbc13d07ba46](../../evidence/parameters-sets-005.md#p-365bcbc13d07ba46) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-044907

```text
(config)# no do-exec test cot set def-params <cr>
```

Handler ` RVA 0x161B8850 `；selector ` 0 `；EOL ` RVA 0x35F0AB88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-e5f931e40d0a640d](../../evidence/state_effects-sets-049.md#s-e5f931e40d0a640d)

### path-044138

```text
(config)# no do-exec test cpuaccounting debug dump <cr>
```

Handler ` RVA 0xE0822D0 `；selector ` 0 `；EOL ` RVA 0x341DCE10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-b8b07ff2aec1aa72](../../evidence/state_effects-sets-039.md#s-b8b07ff2aec1aa72)

### path-044045

```text
(config)# no do-exec test cpurmi hog complex <cr>
```

Handler ` RVA 0xD6D2410 `；selector ` 2 `；EOL ` RVA 0x33ECD828 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-052093

```text
(config)# no do-exec test cpurmi hog simple <number:1..5000> <cr>
```

Handler ` RVA 0xD6D2410 `；selector ` 1 `；EOL ` RVA 0x33ECD5A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Slot Number。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-8683939829a6685a](../../evidence/parameters-sets-010.md#p-8683939829a6685a) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-028556

```text
(config)# no do-exec test crash <cr>
```

Handler ` RVA 0xE8F5540 `；selector ` 0 `；EOL ` RVA 0x3433F780 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-060080

```text
(config)# no do-exec test crypto kgs-test perf controller <number:1..300> <number:1..300> <number:1..10000> <number:1..300> <cr>
```

Handler ` RVA 0x12132450 `；selector ` 0 `；EOL ` RVA 0x357A1208 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Starting k-value；` unsigned_number ` Ending k-value；` unsigned_number ` Number of trials for timing；` unsigned_number ` K-value interval size。

[条件 C-f6a17afdfb05f914](../../evidence/conditions-sets-095.md#c-f6a17afdfb05f914) · [参数 P-720889cf2f064708](../../evidence/parameters-sets-009.md#p-720889cf2f064708) · [状态效果 S-45e7400bd16de706](../../evidence/state_effects-sets-015.md#s-45e7400bd16de706)

### path-047821

```text
(config)# no do-exec test crypto modexp perf-test <cr>
```

Handler ` RVA 0x120E8FF0 `；selector ` 0 `；EOL ` RVA 0x357A0AD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f6a17afdfb05f914](../../evidence/conditions-sets-095.md#c-f6a17afdfb05f914) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-047877

```text
(config)# no do-exec test crypto modexp self-test <cr>
```

Handler ` RVA 0x120E8C60 `；selector ` 0 `；EOL ` RVA 0x357A0D78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f6a17afdfb05f914](../../evidence/conditions-sets-095.md#c-f6a17afdfb05f914) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-047978

```text
(config)# no do-exec test crypto nist-tests cfb8 <cr>
```

Handler ` RVA 0x120E8B50 `；selector ` 0 `；EOL ` RVA 0x357A1650 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f6a17afdfb05f914](../../evidence/conditions-sets-095.md#c-f6a17afdfb05f914) · [状态效果 S-c6ff5d0d7855a2c3](../../evidence/state_effects-sets-042.md#s-c6ff5d0d7855a2c3)

### path-054900

```text
(config)# no do-exec test crypto pki api <string> <cr>
```

Handler ` RVA 0x11F35250 `；selector ` 9 `；EOL ` RVA 0x3575A2F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` API name。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-56e00e3d600f8fae](../../evidence/parameters-sets-007.md#p-56e00e3d600f8fae) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-054722

```text
(config)# no do-exec test crypto pki benchmark rsa <cr>
```

Handler ` RVA 0x11F35250 `；selector ` 4 `；EOL ` RVA 0x35757D78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-058160

```text
(config)# no do-exec test crypto pki benchmark validate-peer <string> <cr>
```

Handler ` RVA 0x11F35250 `；selector ` 6 `；EOL ` RVA 0x35758420 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` URL。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-e5897f7a7dfdc707](../../evidence/parameters-sets-017.md#p-e5897f7a7dfdc707) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-058152

```text
(config)# no do-exec test crypto pki benchmark validate-router <string> <cr>
```

Handler ` RVA 0x11F35250 `；selector ` 5 `；EOL ` RVA 0x35758120 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Trustpoint to validate。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-a79f40b9c7686186](../../evidence/parameters-sets-013.md#p-a79f40b9c7686186) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-054754

```text
(config)# no do-exec test crypto pki cache on <cr>
```

Handler ` RVA 0x11F35250 `；selector ` 10 `；EOL ` RVA 0x357590F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-c0ce8bdec0e71cbb](../../evidence/state_effects-sets-041.md#s-c0ce8bdec0e71cbb)

### path-047893

```text
(config)# no do-exec test crypto pki cert-attributes <cr>
```

Handler ` RVA 0x11F35250 `；selector ` 1 `；EOL ` RVA 0x35757150 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-054526

```text
(config)# no do-exec test crypto pki config-update-notify <string> <cr>
```

Handler ` RVA 0x11F3D8C0 `；selector ` 0 `；EOL ` RVA 0x35756438 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` HA request string。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-cace0a1b6548127a](../../evidence/parameters-sets-015.md#p-cace0a1b6548127a) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-058066

```text
(config)# no do-exec test crypto pki crl request <string> <cr>
```

Handler ` RVA 0x11F35250 `；selector ` 18 `；EOL ` RVA 0x35756760 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` URL for the CRL request。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-823609e6f38dac50](../../evidence/parameters-sets-010.md#p-823609e6f38dac50) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-058135

```text
(config)# no do-exec test crypto pki csr <string> nb <cr>
```

Handler ` RVA 0x11F35250 `；selector ` 8 `；EOL ` RVA 0x35758788 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Trustpoint for new certificate。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-9385614f2d1b8c51](../../evidence/parameters-sets-011.md#p-9385614f2d1b8c51) · [状态效果 S-98932a6f12dd5538](../../evidence/state_effects-sets-032.md#s-98932a6f12dd5538)

### path-048514

```text
(config)# no do-exec test crypto pki enrollment-proxy-api <cr>
```

Handler ` RVA 0x11F35250 `；selector ` 12 `；EOL ` RVA 0x3575A6F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-054868

```text
(config)# no do-exec test crypto pki expiry-alerts reset <cr>
```

Handler ` RVA 0x1202AFD0 `；selector ` 0 `；EOL ` RVA 0x35759F90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-054827

```text
(config)# no do-exec test crypto pki expiry-alerts shrink-periodicity <cr>
```

Handler ` RVA 0x1202AF70 `；selector ` 0 `；EOL ` RVA 0x35759CE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-054656

```text
(config)# no do-exec test crypto pki new-cert <string> <cr>
```

Handler ` RVA 0x11F35250 `；selector ` 7 `；EOL ` RVA 0x357579B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Trustpoint to se for new certificate (shadow) operations。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-c90f6fedf1b7f7ab](../../evidence/parameters-sets-015.md#p-c90f6fedf1b7f7ab) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-059398

```text
(config)# no do-exec test crypto pki ocsp-get-staple <string> chain blocking-test <cr>
```

Handler ` RVA 0x11F35250 `；selector ` 16 `；EOL ` RVA 0x35756DC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Trustpoint label。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-a0283f60f8b05691](../../evidence/parameters-sets-012.md#p-a0283f60f8b05691) · [状态效果 S-89e1f7867ffdd428](../../evidence/state_effects-sets-029.md#s-89e1f7867ffdd428)

### path-048149

```text
(config)# no do-exec test crypto pki openssl <cr>
```

Handler ` RVA 0x11F35250 `；selector ` 19 `；EOL ` RVA 0x35758A80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-047755

```text
(config)# no do-exec test crypto pki pkcs7verify <cr>
```

Handler ` RVA 0x11F35250 `；selector ` 0 `；EOL ` RVA 0x357569F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-054733

```text
(config)# no do-exec test crypto pki safemode on <cr>
```

Handler ` RVA 0x11F35250 `；selector ` 11 `；EOL ` RVA 0x35758D90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-06c918f8c1093907](../../evidence/state_effects-sets-002.md#s-06c918f8c1093907)

### path-047973

```text
(config)# no do-exec test crypto pki self-signed-certificate <cr>
```

Handler ` RVA 0x11F35250 `；selector ` 3 `；EOL ` RVA 0x357576A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-054773

```text
(config)# no do-exec test crypto pki session <number:1..60> <cr>
```

Handler ` RVA 0x11F35250 `；selector ` 15 `；EOL ` RVA 0x35759450 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Session Lifetime。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-d9270027cf31aba6](../../evidence/parameters-sets-016.md#p-d9270027cf31aba6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-054838

```text
(config)# no do-exec test crypto pki trustpool remove <cr>
```

Handler ` RVA 0x11F35250 `；selector ` 14 `；EOL ` RVA 0x357599E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-054802

```text
(config)# no do-exec test crypto pki trustpool reset <cr>
```

Handler ` RVA 0x11F35250 `；selector ` 13 `；EOL ` RVA 0x35759740 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-047928

```text
(config)# no do-exec test crypto pki verify-certificate <cr>
```

Handler ` RVA 0x11F35250 `；selector ` 2 `；EOL ` RVA 0x357573F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-047791

```text
(config)# no do-exec test crypto replay <number:1..4294967295> <cr>
```

Handler ` RVA 0x120E8740 `；selector ` 0 `；EOL ` RVA 0x357A0528 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Replay counter value。

[条件 C-b8190406c976fefd](../../evidence/conditions-sets-071.md#c-b8190406c976fefd) · [参数 P-17461aa5dd937e32](../../evidence/parameters-sets-002.md#p-17461aa5dd937e32) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-054587

```text
(config)# no do-exec test crypto replay time <number:1..42949672> <cr>
```

Handler ` RVA 0x120E88B0 `；selector ` 0 `；EOL ` RVA 0x357A0280 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Replay time value (seconds)。

[条件 C-3d196f218cec6a7d](../../evidence/conditions-sets-024.md#c-3d196f218cec6a7d) · [参数 P-b5994b27a0bb9e74](../../evidence/parameters-sets-014.md#p-b5994b27a0bb9e74) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-038621

```text
(config)# no do-exec test crypto rng-tests <cr>
```

Handler ` RVA 0x120E8C00 `；selector ` 0 `；EOL ` RVA 0x3579FE88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f6a17afdfb05f914](../../evidence/conditions-sets-095.md#c-f6a17afdfb05f914) · [状态效果 S-90654af3641e93ed](../../evidence/state_effects-sets-031.md#s-90654af3641e93ed)

### path-038732

```text
(config)# no do-exec test crypto self-test <cr>
```

Handler ` RVA 0x12953C40 `；selector ` 0 `；EOL ` RVA 0x357A07C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f6a17afdfb05f914](../../evidence/conditions-sets-095.md#c-f6a17afdfb05f914) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-054540

```text
(config)# no do-exec test crypto wui tti petitioner <cr>
```

Handler ` RVA 0x12E03210 `；selector ` 0 `；EOL ` RVA 0x359E4640 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-038773

```text
(config)# no do-exec test cts enable <cr>
```

Handler ` RVA 0x13026640 `；selector ` 0 `；EOL ` RVA 0x35A121F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-6c46600dafa2c63f](../../evidence/conditions-sets-042.md#c-6c46600dafa2c63f) · [状态效果 S-5a0b081f2e2671be](../../evidence/state_effects-sets-019.md#s-5a0b081f2e2671be)

### path-054705

```text
(config)# no do-exec test cts event trace enable <cr>
```

Handler ` RVA 0x131020F0 `；selector ` 0 `；EOL ` RVA 0x35A48190 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-242c7a679db4d255](../../evidence/conditions-sets-014.md#c-242c7a679db4d255) · [状态效果 S-82de56624b0d48f3](../../evidence/state_effects-sets-028.md#s-82de56624b0d48f3)

### path-058305

```text
(config)# no do-exec test cts role-based cgc qlist sort <cr>
```

Handler ` RVA 0x1423AAA0 `；selector ` 0 `；EOL ` RVA 0x35D07930 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-74b8a98d68b9d9da](../../evidence/conditions-sets-045.md#c-74b8a98d68b9d9da) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-060096

```text
(config)# no do-exec test cts role-based counters from <number:2..65521> to <number:2..65521> hw <cr>
```

Handler ` RVA 0x1414C4D0 `；selector ` 6 `；EOL ` RVA 0x35CFEF68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Security Group Tag；` unsigned_number ` Security Group Tag。

[条件 C-555d92626230ac57](../../evidence/conditions-sets-034.md#c-555d92626230ac57) · [参数 P-efb1785cb7b80b9c](../../evidence/parameters-sets-018.md#p-efb1785cb7b80b9c) · [状态效果 S-3427280b61ef26a5](../../evidence/state_effects-sets-012.md#s-3427280b61ef26a5)

### path-058250

```text
(config)# no do-exec test cts role-based dump ipsgt <address> <cr>
```

Handler ` RVA 0x1404B8A0 `；selector ` 3 `；EOL ` RVA 0x35CEAD98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` IPv4 host address。

[条件 C-01cac479efb307bb](../../evidence/conditions-sets-001.md#c-01cac479efb307bb) · [参数 P-b80a5b0d81b8ff65](../../evidence/parameters-sets-014.md#p-b80a5b0d81b8ff65) · [状态效果 S-bf8a7e2a0834d7b4](../../evidence/state_effects-sets-041.md#s-bf8a7e2a0834d7b4)

### path-055134

```text
(config)# no do-exec test cts role-based dump permissions <cr>
```

Handler ` RVA 0x1414C4D0 `；selector ` 1 `；EOL ` RVA 0x35D028E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-74b8a98d68b9d9da](../../evidence/conditions-sets-045.md#c-74b8a98d68b9d9da) · [状态效果 S-c093108d82e70d48](../../evidence/state_effects-sets-041.md#s-c093108d82e70d48)

### path-058319

```text
(config)# no do-exec test cts role-based dump policy dynamic <cr>
```

Handler ` RVA 0x1414C4D0 `；selector ` 0 `；EOL ` RVA 0x35D020E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e103ddfcec73277d](../../evidence/conditions-sets-087.md#c-e103ddfcec73277d) · [状态效果 S-4c741017ce645022](../../evidence/state_effects-sets-017.md#s-4c741017ce645022)

### path-055061

```text
(config)# no do-exec test cts role-based dump sg-info <cr>
```

Handler ` RVA 0x1414C4D0 `；selector ` 11 `；EOL ` RVA 0x35D02C70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-74b8a98d68b9d9da](../../evidence/conditions-sets-045.md#c-74b8a98d68b9d9da) · [状态效果 S-f48e7ceb77a484fb](../../evidence/state_effects-sets-052.md#s-f48e7ceb77a484fb)

### path-058415

```text
(config)# no do-exec test cts role-based echo cli <string> <cr>
```

Handler ` RVA 0x1404B8A0 `；selector ` 14 `；EOL ` RVA 0x35CEDD88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Text line to print in selected context。

[条件 C-97473c061a130e0e](../../evidence/conditions-sets-058.md#c-97473c061a130e0e) · [参数 P-f304f9509e72a317](../../evidence/parameters-sets-018.md#p-f304f9509e72a317) · [状态效果 S-6add8ad62e160efb](../../evidence/state_effects-sets-023.md#s-6add8ad62e160efb)

### path-055318

```text
(config)# no do-exec test cts role-based enforcement enable <cr>
```

Handler ` RVA 0x1414C4D0 `；selector ` 13 `；EOL ` RVA 0x35D01AE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-74b8a98d68b9d9da](../../evidence/conditions-sets-045.md#c-74b8a98d68b9d9da) · [状态效果 S-79e85ca1686f0943](../../evidence/state_effects-sets-026.md#s-79e85ca1686f0943)

### path-055092

```text
(config)# no do-exec test cts role-based ipsgt refresh <cr>
```

Handler ` RVA 0x1404B8A0 `；selector ` 2 `；EOL ` RVA 0x35CEB560 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-74b8a98d68b9d9da](../../evidence/conditions-sets-045.md#c-74b8a98d68b9d9da) · [状态效果 S-c1cae47a9c5506d2](../../evidence/state_effects-sets-041.md#s-c1cae47a9c5506d2)

### path-048755

```text
(config)# no do-exec test cts role-based ping <cr>
```

Handler ` RVA 0x1404B8A0 `；selector ` 12 `；EOL ` RVA 0x35CED858 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-74b8a98d68b9d9da](../../evidence/conditions-sets-045.md#c-74b8a98d68b9d9da) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-055317

```text
(config)# no do-exec test cts role-based policy close <cr>
```

Handler ` RVA 0x1414C4D0 `；selector ` 4 `；EOL ` RVA 0x35CFF6C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-74b8a98d68b9d9da](../../evidence/conditions-sets-045.md#c-74b8a98d68b9d9da) · [状态效果 S-e3d74bee58f87d85](../../evidence/state_effects-sets-048.md#s-e3d74bee58f87d85)

### path-055315

```text
(config)# no do-exec test cts role-based rbacl save <cr>
```

Handler ` RVA 0x1414C4D0 `；selector ` 5 `；EOL ` RVA 0x35D01258 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-74b8a98d68b9d9da](../../evidence/conditions-sets-045.md#c-74b8a98d68b9d9da) · [状态效果 S-a7630deaa5e24159](../../evidence/state_effects-sets-035.md#s-a7630deaa5e24159)

### path-048577

```text
(config)# no do-exec test cts role-based sgacl-log <cr>
```

Handler ` RVA 0x1404B8A0 `；selector ` 15 `；EOL ` RVA 0x35CED318 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-74b8a98d68b9d9da](../../evidence/conditions-sets-045.md#c-74b8a98d68b9d9da) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-058297

```text
(config)# no do-exec test cts role-based snmp mapping first <cr>
```

Handler ` RVA 0x1407C2C0 `；selector ` 5 `；EOL ` RVA 0x35CF4950 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-18488cd3b28704ab](../../evidence/conditions-sets-009.md#c-18488cd3b28704ab) · [状态效果 S-1132eed54461f0b7](../../evidence/state_effects-sets-004.md#s-1132eed54461f0b7)

### path-058318

```text
(config)# no do-exec test cts role-based snmp mapping first <cr>
```

Handler ` RVA 0x1407C2C0 `；selector ` 4 `；EOL ` RVA 0x35CF4E38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1ca591f5cbabee00](../../evidence/conditions-sets-011.md#c-1ca591f5cbabee00) · [状态效果 S-1132eed54461f0b7](../../evidence/state_effects-sets-004.md#s-1132eed54461f0b7)

### path-058332

```text
(config)# no do-exec test cts role-based snmp mapping first <cr>
```

Handler ` RVA 0x1407C2C0 `；selector ` 3 `；EOL ` RVA 0x35CF5168 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-2b932facf861018e](../../evidence/conditions-sets-017.md#c-2b932facf861018e) · [状态效果 S-1132eed54461f0b7](../../evidence/state_effects-sets-004.md#s-1132eed54461f0b7)

### path-058346

```text
(config)# no do-exec test cts role-based snmp mapping first <cr>
```

Handler ` RVA 0x1407C2C0 `；selector ` 2 `；EOL ` RVA 0x35CF5840 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e0c8a1607dafcbaf](../../evidence/conditions-sets-087.md#c-e0c8a1607dafcbaf) · [状态效果 S-1132eed54461f0b7](../../evidence/state_effects-sets-004.md#s-1132eed54461f0b7)

### path-058363

```text
(config)# no do-exec test cts role-based snmp mapping first <cr>
```

Handler ` RVA 0x1407C2C0 `；selector ` 1 `；EOL ` RVA 0x35CF5FB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5bcef35116645995](../../evidence/conditions-sets-036.md#c-5bcef35116645995) · [状态效果 S-1132eed54461f0b7](../../evidence/state_effects-sets-004.md#s-1132eed54461f0b7)

### path-058381

```text
(config)# no do-exec test cts role-based snmp mapping first <cr>
```

Handler ` RVA 0x1407C2C0 `；selector ` 0 `；EOL ` RVA 0x35CF6688 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c85c43e1b66083b8](../../evidence/conditions-sets-077.md#c-c85c43e1b66083b8) · [状态效果 S-1132eed54461f0b7](../../evidence/state_effects-sets-004.md#s-1132eed54461f0b7)

### path-055215

```text
(config)# no do-exec test cts role-based sw-dp enable <cr>
```

Handler ` RVA 0x142353B0 `；selector ` 0 `；EOL ` RVA 0x35D069B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-74b8a98d68b9d9da](../../evidence/conditions-sets-045.md#c-74b8a98d68b9d9da) · [状态效果 S-91e03245044f2206](../../evidence/state_effects-sets-031.md#s-91e03245044f2206)

### path-054821

```text
(config)# no do-exec test cts role-based sync <number:1..2147483647> <cr>
```

Handler ` RVA 0x1404B8A0 `；selector ` 8 `；EOL ` RVA 0x35CECA58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Number of times to synchronize。

[条件 C-74b8a98d68b9d9da](../../evidence/conditions-sets-045.md#c-74b8a98d68b9d9da) · [参数 P-d4f39e730e109d93](../../evidence/parameters-sets-016.md#p-d4f39e730e109d93) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-048081

```text
(config)# no do-exec test cts sap enable <cr>
```

Handler ` RVA 0x13060720 `；selector ` 0 `；EOL ` RVA 0x35A1DD18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d6d417ef00db0b16](../../evidence/conditions-sets-083.md#c-d6d417ef00db0b16) · [状态效果 S-7852a81db6759637](../../evidence/state_effects-sets-026.md#s-7852a81db6759637)

### path-054720

```text
(config)# no do-exec test cts slist_mib del ste <cr>
```

Handler ` RVA 0x130F3EA0 `；selector ` 0 `；EOL ` RVA 0x35A46768 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-30ba82477e81d434](../../evidence/conditions-sets-019.md#c-30ba82477e81d434) · [状态效果 S-d61ba153afb4df18](../../evidence/state_effects-sets-045.md#s-d61ba153afb4df18)

### path-058185

```text
(config)# no do-exec test cts sxp ipsgt action <number:0..2> <cr>
```

Handler ` RVA 0x13279440 `；selector ` 0 `；EOL ` RVA 0x35A53288 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` SNMP Action value。

[条件 C-c2e9c3decb32dd82](../../evidence/conditions-sets-075.md#c-c2e9c3decb32dd82) · [参数 P-09cbcd616efb3894](../../evidence/parameters-sets-001.md#p-09cbcd616efb3894) · [状态效果 S-99e00bfd8dae279f](../../evidence/state_effects-sets-033.md#s-99e00bfd8dae279f)

### path-044637

```text
(config)# no do-exec test cwoir incr_sync on <cr>
```

Handler ` RVA 0xED96790 `；selector ` 0 `；EOL ` RVA 0x34430918 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-36f590d9b51500f0](../../evidence/state_effects-sets-012.md#s-36f590d9b51500f0)

### path-052406

```text
(config)# no do-exec test cwoir insert <number:1..13> <number:1..99> <cr>
```

Handler ` RVA 0xEDAEE90 `；selector ` 0 `；EOL ` RVA 0x3442F710 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` slot number；` unsigned_number ` card type (cwpa=15, cwatm=16, cwpos=17)。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-bb83453e04561a3a](../../evidence/parameters-sets-014.md#p-bb83453e04561a3a) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-056953

```text
(config)# no do-exec test cwoir iosrunning <number:1..13> <number:0..1> <number:1..99> <cr>
```

Handler ` RVA 0xEDAEDD0 `；selector ` 0 `；EOL ` RVA 0x3442FE10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` slot number；` unsigned_number ` cpu number；` unsigned_number ` card type (cwpa=15, cwatm=16, cwpos=17)。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-041e16eff84e84cf](../../evidence/parameters-sets-001.md#p-041e16eff84e84cf) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-056937

```text
(config)# no do-exec test cwoir ipcready <number:1..13> <number:0..1> <number:0..3> <cr>
```

Handler ` RVA 0xEDAED10 `；selector ` 0 `；EOL ` RVA 0x3442FA90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` slot number；` unsigned_number ` cpu number；` unsigned_number ` swichover type。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-a6eb3d08caf0a08c](../../evidence/parameters-sets-013.md#p-a6eb3d08caf0a08c) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-034849

```text
(config)# no do-exec test cwoir read <cr>
```

Handler ` RVA 0xEDAEFB0 `；selector ` 0 `；EOL ` RVA 0x34430388 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-044529

```text
(config)# no do-exec test cwoir remove <number:1..13> <cr>
```

Handler ` RVA 0xEDAEF30 `；selector ` 0 `；EOL ` RVA 0x34430100 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` slot number。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-9ca06d371d94a736](../../evidence/parameters-sets-012.md#p-9ca06d371d94a736) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-034902

```text
(config)# no do-exec test cwoir show <cr>
```

Handler ` RVA 0xEDAEFF0 `；selector ` 0 `；EOL ` RVA 0x34430630 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-031387

```text
(config)# no do-exec test data-descriptor <cr>
```

Handler ` RVA 0xD550170 `；selector ` 0 `；EOL ` RVA 0x33E7FB68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c78521e4c567f81f](../../evidence/conditions-sets-077.md#c-c78521e4c567f81f) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-038785

```text
(config)# no do-exec test dhcp ns <cr>
```

Handler ` RVA 0xF4743A0 `；selector ` 0 `；EOL ` RVA 0x34652410 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-038689

```text
(config)# no do-exec test dhcp release <cr>
```

Handler ` RVA 0xF4733F0 `；selector ` 0 `；EOL ` RVA 0x346518B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-f44c1dd0ba208538](../../evidence/state_effects-sets-052.md#s-f44c1dd0ba208538)

### path-046875

```text
(config)# no do-exec test dmtm <number:0..64> cmd <cr>
```

Handler ` RVA 0x10C43D50 `；selector ` 0 `；EOL ` RVA 0x34CEBE60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` slot numbers (specify 0+ slots)。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-0e7af595ea053c84](../../evidence/parameters-sets-002.md#p-0e7af595ea053c84) · [状态效果 S-6547cf0ae07b3a25](../../evidence/state_effects-sets-022.md#s-6547cf0ae07b3a25)

### path-053311

```text
(config)# no do-exec test dtp switch crash <number:0..3> <cr>
```

Handler ` RVA 0x15F15700 `；selector ` 0 `；EOL ` RVA 0x35E68DE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` crash point:0-nocrash 1-reneg 2-compl 3-oper。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-576c7c500f9d549b](../../evidence/parameters-sets-007.md#p-576c7c500f9d549b) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-035964

```text
(config)# no do-exec test dwnld_mgr <string> <cr>
```

Handler ` RVA 0x10656760 `；selector ` 0 `；EOL ` RVA 0x34BDA0D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` profile name。

[条件 C-59bebd9794d844b9](../../evidence/conditions-sets-035.md#c-59bebd9794d844b9) · [参数 P-0dadb8908436ba2e](../../evidence/parameters-sets-001.md#p-0dadb8908436ba2e) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-044293

```text
(config)# no do-exec test eci add <string> <cr>
```

Handler ` RVA 0xDF98570 `；selector ` 0 `；EOL ` RVA 0x340E2DE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` file containing eci chain input。

[条件 C-b209e9867ab93018](../../evidence/conditions-sets-069.md#c-b209e9867ab93018) · [参数 P-87f51bdf5a11fcb0](../../evidence/parameters-sets-010.md#p-87f51bdf5a11fcb0) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-044263

```text
(config)# no do-exec test eci delete <string> <cr>
```

Handler ` RVA 0xDF97EA0 `；selector ` 0 `；EOL ` RVA 0x340E2AF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` file containing eci chain input。

[条件 C-b209e9867ab93018](../../evidence/conditions-sets-069.md#c-b209e9867ab93018) · [参数 P-b0019edcb90aef5f](../../evidence/parameters-sets-013.md#p-b0019edcb90aef5f) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-034594

```text
(config)# no do-exec test eci scan <cr>
```

Handler ` RVA 0xDF986D0 `；selector ` 0 `；EOL ` RVA 0x340E30C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b209e9867ab93018](../../evidence/conditions-sets-069.md#c-b209e9867ab93018) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-052324

```text
(config)# no do-exec test eci set timeout <number:0..1000> <cr>
```

Handler ` RVA 0xDF988A0 `；selector ` 0 `；EOL ` RVA 0x340E33F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` seconds to wait。

[条件 C-b209e9867ab93018](../../evidence/conditions-sets-069.md#c-b209e9867ab93018) · [参数 P-5e273781dbffcb2e](../../evidence/parameters-sets-008.md#p-5e273781dbffcb2e) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-034657

```text
(config)# no do-exec test eci show <cr>
```

Handler ` RVA 0xDF985D0 `；selector ` 0 `；EOL ` RVA 0x340E36C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b209e9867ab93018](../../evidence/conditions-sets-069.md#c-b209e9867ab93018) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-031711

```text
(config)# no do-exec test eem <cr>
```

Handler ` RVA 0x1107A0B0 `；selector ` 0 `；EOL ` RVA 0x35386950 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-037649

```text
(config)# no do-exec test eigrp SIA <cr>
```

Handler ` RVA 0xF590F90 `；selector ` 105 `；EOL ` RVA 0x3469D878 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f7298c1a9645892c](../../evidence/conditions-sets-095.md#c-f7298c1a9645892c) · [状态效果 S-a3fc693d7ded95ea](../../evidence/state_effects-sets-035.md#s-a3fc693d7ded95ea)

### path-054295

```text
(config)# no do-exec test eigrp address-family ipv4 ack <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 108 `；EOL ` RVA 0x346B9888 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-41f8139d1c26a2b9](../../evidence/conditions-sets-026.md#c-41f8139d1c26a2b9) · [状态效果 S-4e45bf9231652ca7](../../evidence/state_effects-sets-017.md#s-4e45bf9231652ca7)

### path-058022

```text
(config)# no do-exec test eigrp address-family ipv4 error-percent <number:0..100> <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 107 `；EOL ` RVA 0x346B9F98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Error percentage。

[条件 C-567eebbcb0aad439](../../evidence/conditions-sets-034.md#c-567eebbcb0aad439) · [参数 P-f2279363519f3eb4](../../evidence/parameters-sets-018.md#p-f2279363519f3eb4) · [状态效果 S-d45690276a5aaaa4](../../evidence/state_effects-sets-045.md#s-d45690276a5aaaa4)

### path-054282

```text
(config)# no do-exec test eigrp address-family ipv6 ack <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 108 `；EOL ` RVA 0x35457E08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-dffd991031595cab](../../evidence/conditions-sets-086.md#c-dffd991031595cab) · [状态效果 S-1920af5e84a8e280](../../evidence/state_effects-sets-006.md#s-1920af5e84a8e280)

### path-058016

```text
(config)# no do-exec test eigrp address-family ipv6 error-percent <number:0..100> <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 107 `；EOL ` RVA 0x35458518 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Error percentage。

[条件 C-332e7febc4848829](../../evidence/conditions-sets-020.md#c-332e7febc4848829) · [参数 P-9704e8c7268e4d69](../../evidence/parameters-sets-012.md#p-9704e8c7268e4d69) · [状态效果 S-f7de967e69ea14b6](../../evidence/state_effects-sets-052.md#s-f7de967e69ea14b6)

### path-037422

```text
(config)# no do-exec test eigrp crimson <cr>
```

Handler ` RVA 0xF590F90 `；selector ` 106 `；EOL ` RVA 0x3469D428 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d930ca6119535a50](../../evidence/conditions-sets-084.md#c-d930ca6119535a50) · [状态效果 S-a3fc693d7ded95ea](../../evidence/state_effects-sets-035.md#s-a3fc693d7ded95ea)

### path-057631

```text
(config)# no do-exec test ethernet errdisable recovery-timer unit second <cr>
```

Handler ` RVA 0xC037E10 `；selector ` 0 `；EOL ` RVA 0x339882A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b8edb4566933087f](../../evidence/conditions-sets-071.md#c-b8edb4566933087f) · [状态效果 S-50514e8aba70beeb](../../evidence/state_effects-sets-018.md#s-50514e8aba70beeb)

### path-053695

```text
(config)# no do-exec test ethernet mirp-rcv isid <number:1..16777215> <cr>
```

Handler ` RVA 0xC037E10 `；selector ` 2 `；EOL ` RVA 0x33987DA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` isid id。

[条件 C-df35fc317e2776ad](../../evidence/conditions-sets-086.md#c-df35fc317e2776ad) · [参数 P-e964ebd939a67768](../../evidence/parameters-sets-017.md#p-e964ebd939a67768) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-046120

```text
(config)# no do-exec test ethernet safe-iteration <number:0..5> <cr>
```

Handler ` RVA 0xC037E10 `；selector ` 5 `；EOL ` RVA 0x33986DF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Test case number。

[条件 C-fa740d3d754318cc](../../evidence/conditions-sets-097.md#c-fa740d3d754318cc) · [参数 P-bd87e469a1d0f0e7](../../evidence/parameters-sets-014.md#p-bd87e469a1d0f0e7) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-054447

```text
(config)# no do-exec test event manager ged define <cr>
```

Handler ` RVA 0x110CDE30 `；selector ` 0 `；EOL ` RVA 0x353A63D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5d3923f222a3ef82](../../evidence/conditions-sets-036.md#c-5d3923f222a3ef82) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-054459

```text
(config)# no do-exec test event manager ged publish <cr>
```

Handler ` RVA 0x110CDC70 `；selector ` 0 `；EOL ` RVA 0x353A6678 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-05ffda84a3a2a421](../../evidence/conditions-sets-003.md#c-05ffda84a3a2a421) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-054474

```text
(config)# no do-exec test event manager ged subscribe <cr>
```

Handler ` RVA 0x110CDD70 `；selector ` 0 `；EOL ` RVA 0x353A6920 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b16be1f54ae86ae2](../../evidence/conditions-sets-069.md#c-b16be1f54ae86ae2) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-058036

```text
(config)# no do-exec test event manager ged unsubscribe <number:0..2147483647> <cr>
```

Handler ` RVA 0x110CDDD0 `；selector ` 0 `；EOL ` RVA 0x353A6C08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` subscription id。

[条件 C-b4cefe565a8a17d8](../../evidence/conditions-sets-070.md#c-b4cefe565a8a17d8) · [参数 P-e54fd61c119df86e](../../evidence/parameters-sets-017.md#p-e54fd61c119df86e) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-048655

```text
(config)# no do-exec test flowspec client stop <cr>
```

Handler ` RVA 0x134655F0 `；selector ` 1 `；EOL ` RVA 0x35A9B978 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b71df096cc2567e3](../../evidence/conditions-sets-071.md#c-b71df096cc2567e3) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-048523

```text
(config)# no do-exec test flowspec client xos <cr>
```

Handler ` RVA 0x134655F0 `；selector ` 0 `；EOL ` RVA 0x35A9B670 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f56987fb75cd6a8b](../../evidence/conditions-sets-095.md#c-f56987fb75cd6a8b) · [状态效果 S-563ec921d0291b1e](../../evidence/state_effects-sets-019.md#s-563ec921d0291b1e)

### path-039821

```text
(config)# no do-exec test flowspec rt-dump <cr>
```

Handler ` RVA 0x134655F0 `；selector ` 4 `；EOL ` RVA 0x35A9C2F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b01bef5386753493](../../evidence/conditions-sets-068.md#c-b01bef5386753493) · [状态效果 S-11b5906030e87a81](../../evidence/state_effects-sets-004.md#s-11b5906030e87a81)

### path-039735

```text
(config)# no do-exec test flowspec txlist-dump <cr>
```

Handler ` RVA 0x134655F0 `；selector ` 5 `；EOL ` RVA 0x35A9C5F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f802aac3afb08c4a](../../evidence/conditions-sets-096.md#c-f802aac3afb08c4a) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-039880

```text
(config)# no do-exec test flowspec xtf <cr>
```

Handler ` RVA 0x134655F0 `；selector ` 2 `；EOL ` RVA 0x35A9BFE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-29b6b000659bdeff](../../evidence/conditions-sets-016.md#c-29b6b000659bdeff) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-048582

```text
(config)# no do-exec test flowspec xtf print <cr>
```

Handler ` RVA 0x134655F0 `；selector ` 3 `；EOL ` RVA 0x35A9BC88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-092e5569d02a3416](../../evidence/conditions-sets-004.md#c-092e5569d02a3416) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-037941

```text
(config)# no do-exec test fqdn <number:0..14> <cr>
```

Handler ` RVA 0xC2E4050 `；selector ` 5 `；EOL ` RVA 0x33A3DF48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` 0 to disable ut test flag, 1-14 to execute different ut cases。

[条件 C-e48d1444c828648f](../../evidence/conditions-sets-088.md#c-e48d1444c828648f) · [参数 P-c9a94d867a4371a2](../../evidence/parameters-sets-015.md#p-c9a94d867a4371a2) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-045045

```text
(config)# no do-exec test garp_retry add <address> <cr>
```

Handler ` RVA 0xCF73340 `；selector ` 0 `；EOL ` RVA 0x33D441B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` ip address。

[条件 C-3cbae58812f0e31a](../../evidence/conditions-sets-024.md#c-3cbae58812f0e31a) · [参数 P-e55458f9b27c5030](../../evidence/parameters-sets-017.md#p-e55458f9b27c5030) · [状态效果 S-2c54b5180b30e336](../../evidence/state_effects-sets-010.md#s-2c54b5180b30e336)

### path-053799

```text
(config)# no do-exec test glbp redundancy events enable <cr>
```

Handler ` RVA 0xE169F90 `；selector ` 50 `；EOL ` RVA 0x34224F60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-9df4e9bf44d1b62c](../../evidence/state_effects-sets-034.md#s-9df4e9bf44d1b62c)

### path-058243

```text
(config)# no do-exec test gsi httpc <number:0..9> debug off <cr>
```

Handler ` RVA 0xF3B0380 `；selector ` 0 `；EOL ` RVA 0x346228C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` instance number。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-98b65764ba5cdb09](../../evidence/parameters-sets-012.md#p-98b65764ba5cdb09) · [状态效果 S-b82d7ea78274a145](../../evidence/state_effects-sets-039.md#s-b82d7ea78274a145)

### path-054949

```text
(config)# no do-exec test gsi httpc <number:0..9> show <cr>
```

Handler ` RVA 0xF3B0610 `；selector ` 0 `；EOL ` RVA 0x346225B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` instance number。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-98b65764ba5cdb09](../../evidence/parameters-sets-012.md#p-98b65764ba5cdb09) · [状态效果 S-a2b298f3d0944ac2](../../evidence/state_effects-sets-034.md#s-a2b298f3d0944ac2)

### path-059443

```text
(config)# no do-exec test gsi httpc <number:0..9> start <string> post <cr>
```

Handler ` RVA 0xF3B2930 `；selector ` 0 `；EOL ` RVA 0x34621F40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` instance number；` string ` URL to use。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-a85c754192468da0](../../evidence/parameters-sets-013.md#p-a85c754192468da0) · [状态效果 S-61a74d77df74b84b](../../evidence/state_effects-sets-021.md#s-61a74d77df74b84b)

### path-055012

```text
(config)# no do-exec test gsi httpc <number:0..9> xml-header <cr>
```

Handler ` RVA 0xF3B09C0 `；selector ` 0 `；EOL ` RVA 0x34622BB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` instance number。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-98b65764ba5cdb09](../../evidence/parameters-sets-012.md#p-98b65764ba5cdb09) · [状态效果 S-0c832b9738ff3ae4](../../evidence/state_effects-sets-003.md#s-0c832b9738ff3ae4)

### path-048490

```text
(config)# no do-exec test gsi httpc stop <cr>
```

Handler ` RVA 0xF3B0E90 `；selector ` 0 `；EOL ` RVA 0x34622280 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-a2b298f3d0944ac2](../../evidence/state_effects-sets-034.md#s-a2b298f3d0944ac2)

### path-058228

```text
(config)# no do-exec test gsi https <number:0..9> debug off <cr>
```

Handler ` RVA 0xF3B0380 `；selector ` 1 `；EOL ` RVA 0x346215E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` instance number。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-85bb7d9d00437dea](../../evidence/parameters-sets-010.md#p-85bb7d9d00437dea) · [状态效果 S-c61d02809237b1a7](../../evidence/state_effects-sets-042.md#s-c61d02809237b1a7)

### path-054922

```text
(config)# no do-exec test gsi https <number:0..9> show <cr>
```

Handler ` RVA 0xF3B0610 `；selector ` 1 `；EOL ` RVA 0x346212D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` instance number。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-85bb7d9d00437dea](../../evidence/parameters-sets-010.md#p-85bb7d9d00437dea) · [状态效果 S-0551eb6ab7b6ab56](../../evidence/state_effects-sets-002.md#s-0551eb6ab7b6ab56)

### path-059881

```text
(config)# no do-exec test gsi https <number:0..9> start <string> encrypt post <cr>
```

Handler ` RVA 0xF3B2A20 `；selector ` 0 `；EOL ` RVA 0x34620AD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` instance number；` string ` URL to use。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-49005321df5f5cf4](../../evidence/parameters-sets-006.md#p-49005321df5f5cf4) · [状态效果 S-a270fdf47b3b5d24](../../evidence/state_effects-sets-034.md#s-a270fdf47b3b5d24)

### path-054980

```text
(config)# no do-exec test gsi https <number:0..9> xml-header <cr>
```

Handler ` RVA 0xF3B09C0 `；selector ` 1 `；EOL ` RVA 0x346218E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` instance number。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-85bb7d9d00437dea](../../evidence/parameters-sets-010.md#p-85bb7d9d00437dea) · [状态效果 S-9b432970a35a6a89](../../evidence/state_effects-sets-033.md#s-9b432970a35a6a89)

### path-048445

```text
(config)# no do-exec test gsi https stop <cr>
```

Handler ` RVA 0xF3B0E90 `；selector ` 1 `；EOL ` RVA 0x34620FA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-0551eb6ab7b6ab56](../../evidence/state_effects-sets-002.md#s-0551eb6ab7b6ab56)

### path-058216

```text
(config)# no do-exec test gsi sshc <number:0..9> debug off <cr>
```

Handler ` RVA 0xF3B0380 `；selector ` 2 `；EOL ` RVA 0x34620068 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` instance number。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-db878564e0d39553](../../evidence/parameters-sets-017.md#p-db878564e0d39553) · [状态效果 S-0f9c33924108a38d](../../evidence/state_effects-sets-004.md#s-0f9c33924108a38d)

### path-054896

```text
(config)# no do-exec test gsi sshc <number:0..9> show <cr>
```

Handler ` RVA 0xF3B0610 `；selector ` 2 `；EOL ` RVA 0x3461FD58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` instance number。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-db878564e0d39553](../../evidence/parameters-sets-017.md#p-db878564e0d39553) · [状态效果 S-dfc1af421a3197a0](../../evidence/state_effects-sets-047.md#s-dfc1af421a3197a0)

### path-059440

```text
(config)# no do-exec test gsi sshc <number:0..9> start <string> wsma <cr>
```

Handler ` RVA 0xF3B10E0 `；selector ` 0 `；EOL ` RVA 0x3461F6E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` instance number；` string ` URL to use。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-0608e1b131dc833a](../../evidence/parameters-sets-001.md#p-0608e1b131dc833a) · [状态效果 S-ed73e29d608d1d9e](../../evidence/state_effects-sets-050.md#s-ed73e29d608d1d9e)

### path-054952

```text
(config)# no do-exec test gsi sshc <number:0..9> xml-header <cr>
```

Handler ` RVA 0xF3B09C0 `；selector ` 2 `；EOL ` RVA 0x34620360 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` instance number。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-db878564e0d39553](../../evidence/parameters-sets-017.md#p-db878564e0d39553) · [状态效果 S-fc3590085eb3ad8d](../../evidence/state_effects-sets-053.md#s-fc3590085eb3ad8d)

### path-048389

```text
(config)# no do-exec test gsi sshc stop <cr>
```

Handler ` RVA 0xF3B0E90 `；selector ` 2 `；EOL ` RVA 0x3461FA28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-dfc1af421a3197a0](../../evidence/state_effects-sets-047.md#s-dfc1af421a3197a0)

### path-047228

```text
(config)# no do-exec test gssapi init_sec_context <string> <cr>
```

Handler ` RVA 0xC3DCF70 `；selector ` 1 `；EOL ` RVA 0x33A66FE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` The server name or target name。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-43e4e0daf266aaf3](../../evidence/parameters-sets-006.md#p-43e4e0daf266aaf3) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-057991

```text
(config)# no do-exec test gssapi token_exchange no_wrap <address> <string> <cr>
```

Handler ` RVA 0xC3DCF70 `；selector ` 2 `；EOL ` RVA 0x33A673D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` Remote hostname or IP address；` string ` The server name or target name。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-fd7d94e1b385dba2](../../evidence/parameters-sets-019.md#p-fd7d94e1b385dba2) · [状态效果 S-16511d91f57b4979](../../evidence/state_effects-sets-005.md#s-16511d91f57b4979)

### path-055540

```text
(config)# no do-exec test gx access-accept service <string> <cr>
```

Handler ` RVA 0xBD23280 `；selector ` 1 `；EOL ` RVA 0x338C3BA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Service name。

[条件 C-8294c28eb72c34ec](../../evidence/conditions-sets-051.md#c-8294c28eb72c34ec) · [参数 P-62d5f9834b5f4036](../../evidence/parameters-sets-008.md#p-62d5f9834b5f4036) · [状态效果 S-0af20cb4b94e6bca](../../evidence/state_effects-sets-003.md#s-0af20cb4b94e6bca)

### path-040408

```text
(config)# no do-exec test gx access-reject <cr>
```

Handler ` RVA 0xBD23380 `；selector ` 1 `；EOL ` RVA 0x338C3E38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8294c28eb72c34ec](../../evidence/conditions-sets-051.md#c-8294c28eb72c34ec) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-055521

```text
(config)# no do-exec test gx delete-session ip <address> <cr>
```

Handler ` RVA 0xBD21FF0 `；selector ` 1 `；EOL ` RVA 0x338C2DE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` IP address of the subscriber。

[条件 C-8294c28eb72c34ec](../../evidence/conditions-sets-051.md#c-8294c28eb72c34ec) · [参数 P-e8e8b1f79c8c540d](../../evidence/parameters-sets-017.md#p-e8e8b1f79c8c540d) · [状态效果 S-db6e0598b2044555](../../evidence/state_effects-sets-046.md#s-db6e0598b2044555)

### path-040173

```text
(config)# no do-exec test gx enable <cr>
```

Handler ` RVA 0xBD20610 `；selector ` 0 `；EOL ` RVA 0x338C2268 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c4e3cbe498bf9eaa](../../evidence/conditions-sets-076.md#c-c4e3cbe498bf9eaa) · [状态效果 S-effaa378d35f9f24](../../evidence/state_effects-sets-051.md#s-effaa378d35f9f24)

### path-059509

```text
(config)# no do-exec test gx rar-sb session-id <number:1..4294967295> install-service <string> <cr>
```

Handler ` RVA 0xBD23560 `；selector ` 1 `；EOL ` RVA 0x338C4328 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Session id；` string ` Service name。

[条件 C-8294c28eb72c34ec](../../evidence/conditions-sets-051.md#c-8294c28eb72c34ec) · [参数 P-b0c10cbbfe902699](../../evidence/parameters-sets-013.md#p-b0c10cbbfe902699) · [状态效果 S-a369abbd7ca70b9a](../../evidence/state_effects-sets-035.md#s-a369abbd7ca70b9a)

### path-057084

```text
(config)# no do-exec test hsrp ha sync mac enable <cr>
```

Handler ` RVA 0xD321940 `；selector ` 50 `；EOL ` RVA 0x33E15B98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-4b1548d1bf1c6d25](../../evidence/state_effects-sets-016.md#s-4b1548d1bf1c6d25)

### path-038122

```text
(config)# no do-exec test idmgr init <cr>
```

Handler ` RVA 0xE1926E0 `；selector ` 0 `；EOL ` RVA 0x3422BCB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-5d5205fa3f3d5912](../../evidence/state_effects-sets-020.md#s-5d5205fa3f3d5912)

### path-059365

```text
(config)# no do-exec test idmgr req-type session-assert key-list <string> data-list <cr>
```

Handler ` RVA 0xE1926E0 `；selector ` 0 `；EOL ` RVA 0x3422C0E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Name of Attribute list。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-04fef1596abad51d](../../evidence/parameters-sets-001.md#p-04fef1596abad51d) · [状态效果 S-22d3003ad5342a19](../../evidence/state_effects-sets-008.md#s-22d3003ad5342a19)

### path-058098

```text
(config)# no do-exec test ifs appn read <address> <string> <cr>
```

Handler ` RVA 0xD65FD60 `；selector ` 1 `；EOL ` RVA 0x33EC2460 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` Destination address；` string ` Filename only。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-727d586e085e9dc5](../../evidence/parameters-sets-009.md#p-727d586e085e9dc5) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-058106

```text
(config)# no do-exec test ifs appn write <address> <string> <cr>
```

Handler ` RVA 0xD65FD60 `；selector ` 2 `；EOL ` RVA 0x33EC2760 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` Destination address；` string ` Filename only。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-9696f29e228907e8](../../evidence/parameters-sets-012.md#p-9696f29e228907e8) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-047900

```text
(config)# no do-exec test ifs boot <string> <cr>
```

Handler ` RVA 0xD65FD60 `；selector ` 3 `；EOL ` RVA 0x33EC2A60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Remainder of the bootstrap 'boot' command。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-f0def853533d3d07](../../evidence/parameters-sets-018.md#p-f0def853533d3d07) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-038899

```text
(config)# no do-exec test ifs defaults <cr>
```

Handler ` RVA 0xD65FD60 `；selector ` 4 `；EOL ` RVA 0x33EC2CE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-054707

```text
(config)# no do-exec test ifs disk cluster <string> <cr>
```

Handler ` RVA 0xD65FD60 `；selector ` 8 `；EOL ` RVA 0x33EC39F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` URL for disk file。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-efdb0d55b0727b4f](../../evidence/parameters-sets-018.md#p-efdb0d55b0727b4f) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

