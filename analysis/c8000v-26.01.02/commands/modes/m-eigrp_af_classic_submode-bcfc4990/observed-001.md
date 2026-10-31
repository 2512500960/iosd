# eigrp_af_classic_submode · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-006526

```text
(config-router-af)# auto-summary <cr>
```

Handler ` RVA 0xF575B20 `；selector ` 42 `；EOL ` RVA 0x346D03B8 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1f9a30c4f2fba0b7](../../evidence/conditions-sets-012.md#c-1f9a30c4f2fba0b7)

### observed_connections-006554

```text
(config-router-af)# autonomous-system <number:1..65535> <cr>
```

Handler ` RVA 0xF5DF260 `；selector ` 120 `；EOL ` RVA 0x346D2C90 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Autonomous System。

[条件 C-978995009b28b8a8](../../evidence/conditions-sets-058.md#c-978995009b28b8a8) · [参数 P-3e9285c714b1f8b6](../../evidence/parameters-sets-005.md#p-3e9285c714b1f8b6)

### observed_connections-006535

```text
(config-router-af)# bfd all-interfaces <cr>
```

Handler ` RVA 0xF57A660 `；selector ` 52 `；EOL ` RVA 0x346CB9F8 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[状态效果 S-4dcf5ec7b3539b83](../../evidence/state_effects-sets-017.md#s-4dcf5ec7b3539b83)

### observed_connections-006639

```text
(config-router-af)# bfd interface <interface> <cr>
```

Handler ` RVA 0xF57A660 `；selector ` 52 `；EOL ` RVA 0x346CB9F8 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8b24c11f71f8c63c](../../evidence/conditions-sets-054.md#c-8b24c11f71f8c63c) · [缺口 G-54111a107ae269a9](../../evidence/gaps-sets-003.md#g-54111a107ae269a9) · [参数 P-490412d66079d477](../../evidence/parameters-sets-006.md#p-490412d66079d477)

### observed_connections-006550

```text
(config-router-af)# default auto-summary <cr>
```

Handler ` RVA 0xF575B20 `；selector ` 42 `；EOL ` RVA 0x346D03B8 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1f9a30c4f2fba0b7](../../evidence/conditions-sets-012.md#c-1f9a30c4f2fba0b7) · [状态效果 S-1d47f709e5271186](../../evidence/state_effects-sets-007.md#s-1d47f709e5271186)

### observed_connections-006602

```text
(config-router-af)# default autonomous-system <number:1..65535> <cr>
```

Handler ` RVA 0xF5DF260 `；selector ` 120 `；EOL ` RVA 0x346D2C90 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Autonomous System。

[条件 C-978995009b28b8a8](../../evidence/conditions-sets-058.md#c-978995009b28b8a8) · [参数 P-3e9285c714b1f8b6](../../evidence/parameters-sets-005.md#p-3e9285c714b1f8b6) · [状态效果 S-1d47f709e5271186](../../evidence/state_effects-sets-007.md#s-1d47f709e5271186)

### observed_connections-006581

```text
(config-router-af)# default bfd all-interfaces <cr>
```

Handler ` RVA 0xF57A660 `；selector ` 52 `；EOL ` RVA 0x346CB9F8 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-22a9b305cf7de680](../../evidence/state_effects-sets-008.md#s-22a9b305cf7de680)

### observed_connections-006590

```text
(config-router-af)# default default-information in <cr>
```

Handler ` RVA 0xF5DB530 `；selector ` 48 `；EOL ` RVA 0x346CD108 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-71343b056e770d34](../../evidence/conditions-sets-044.md#c-71343b056e770d34) · [状态效果 S-d42a60e4cd4f9b89](../../evidence/state_effects-sets-045.md#s-d42a60e4cd4f9b89)

### observed_connections-006546

```text
(config-router-af)# default default-metric <cr>
```

Handler ` RVA 0xF5756A0 `；selector ` 45 `；EOL ` RVA 0x346CCC00 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6e01e373500c9981](../../evidence/conditions-sets-043.md#c-6e01e373500c9981) · [状态效果 S-1d47f709e5271186](../../evidence/state_effects-sets-007.md#s-1d47f709e5271186)

### observed_connections-006630

```text
(config-router-af)# default distance <number:1..255> <address> <address> <cr>
```

Handler ` RVA 0xF596F40 `；selector ` 46 `；EOL ` RVA 0x346CFC58 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Set route administrative distance；` address ` IP Source address；` address ` Wildcard bits。

[条件 C-f2c2efe52d48e891](../../evidence/conditions-sets-094.md#c-f2c2efe52d48e891) · [参数 P-1c0e581156a7a813](../../evidence/parameters-sets-003.md#p-1c0e581156a7a813) · [状态效果 S-1d47f709e5271186](../../evidence/state_effects-sets-007.md#s-1d47f709e5271186)

### observed_connections-006592

```text
(config-router-af)# default distance eigrp <cr>
```

Handler ` RVA 0xF597490 `；selector ` 47 `；EOL ` RVA 0x346D0028 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a632e49a6760a01e](../../evidence/conditions-sets-064.md#c-a632e49a6760a01e) · [状态效果 S-1d47f709e5271186](../../evidence/state_effects-sets-007.md#s-1d47f709e5271186)

### observed_connections-006607

```text
(config-router-af)# default distribute-list in <cr>
```

Handler ` RVA 0xF5DBC30 `；selector ` 29 `；EOL ` RVA 0x346D2570 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-52c6f4d562348d21](../../evidence/conditions-sets-032.md#c-52c6f4d562348d21) · [状态效果 S-1ce7fa3fa224d772](../../evidence/state_effects-sets-007.md#s-1ce7fa3fa224d772)

### observed_connections-006609

```text
(config-router-af)# default eigrp graceful-restart <cr>
```

Handler ` RVA 0xF57EE00 `；selector ` 10 `；EOL ` RVA 0x346D4E18 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-30d87459b7313ee5](../../evidence/conditions-sets-019.md#c-30d87459b7313ee5) · [状态效果 S-1d47f709e5271186](../../evidence/state_effects-sets-007.md#s-1d47f709e5271186)

### observed_connections-006628

```text
(config-router-af)# default eigrp upgrade-cli <string> <cr>
```

Handler ` RVA 0xF5807E0 `；selector ` 142 `；EOL ` RVA 0x346D52F8 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` EIGRP Virtual-Instance Name。

[条件 C-cc9b20bf7f82427f](../../evidence/conditions-sets-079.md#c-cc9b20bf7f82427f) · [参数 P-3bb7808def1d39b2](../../evidence/parameters-sets-005.md#p-3bb7808def1d39b2) · [状态效果 S-1d47f709e5271186](../../evidence/state_effects-sets-007.md#s-1d47f709e5271186)

### observed_connections-006574

```text
(config-router-af)# default event-log-size <cr>
```

Handler ` RVA 0xF596700 `；selector ` 35 `；EOL ` RVA 0x346D4A40 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d7cbeb1b12fce1be](../../evidence/conditions-sets-083.md#c-d7cbeb1b12fce1be) · [状态效果 S-1d47f709e5271186](../../evidence/state_effects-sets-007.md#s-1d47f709e5271186)

### observed_connections-006569

```text
(config-router-af)# default event-logging <cr>
```

Handler ` RVA 0xF596700 `；selector ` 36 `；EOL ` RVA 0x346D4700 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-978995009b28b8a8](../../evidence/conditions-sets-058.md#c-978995009b28b8a8) · [状态效果 S-1d47f709e5271186](../../evidence/state_effects-sets-007.md#s-1d47f709e5271186)

### observed_connections-006560

```text
(config-router-af)# default kill-everyone <cr>
```

Handler ` RVA 0xF57B0C0 `；selector ` 15 `；EOL ` RVA 0x346D39A8 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-978995009b28b8a8](../../evidence/conditions-sets-058.md#c-978995009b28b8a8) · [状态效果 S-1d47f709e5271186](../../evidence/state_effects-sets-007.md#s-1d47f709e5271186)

### observed_connections-006570

```text
(config-router-af)# default log-event-type <cr>
```

Handler ` RVA 0xF596700 `；selector ` 34 `；EOL ` RVA 0x346D4318 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6420c94472c02760](../../evidence/conditions-sets-039.md#c-6420c94472c02760) · [状态效果 S-1d47f709e5271186](../../evidence/state_effects-sets-007.md#s-1d47f709e5271186)

### observed_connections-006564

```text
(config-router-af)# default log-neighbor-changes <cr>
```

Handler ` RVA 0xF57B3F0 `；selector ` 16 `；EOL ` RVA 0x346D3C88 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-978995009b28b8a8](../../evidence/conditions-sets-058.md#c-978995009b28b8a8) · [状态效果 S-1d47f709e5271186](../../evidence/state_effects-sets-007.md#s-1d47f709e5271186)

### observed_connections-006567

```text
(config-router-af)# default log-neighbor-warnings <cr>
```

Handler ` RVA 0xF57B570 `；selector ` 17 `；EOL ` RVA 0x346D3FC8 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-324c8ed36a6689f1](../../evidence/conditions-sets-020.md#c-324c8ed36a6689f1) · [状态效果 S-1d47f709e5271186](../../evidence/state_effects-sets-007.md#s-1d47f709e5271186)

### observed_connections-006541

```text
(config-router-af)# default maximum-paths <cr>
```

Handler ` RVA 0xF5985F0 `；selector ` 37 `；EOL ` RVA 0x346CC558 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f2cc1bdf76721bd1](../../evidence/conditions-sets-094.md#c-f2cc1bdf76721bd1) · [状态效果 S-1d47f709e5271186](../../evidence/state_effects-sets-007.md#s-1d47f709e5271186)

### observed_connections-006552

```text
(config-router-af)# default maximum-prefix <cr>
```

Handler ` RVA 0xF579E30 `；selector ` 20 `；EOL ` RVA 0x346D06F8 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-29f2824e95071986](../../evidence/conditions-sets-016.md#c-29f2824e95071986) · [状态效果 S-1d47f709e5271186](../../evidence/state_effects-sets-007.md#s-1d47f709e5271186)

### observed_connections-006540

```text
(config-router-af)# default maximum-secondary-paths <cr>
```

Handler ` RVA 0xF5987B0 `；selector ` 38 `；EOL ` RVA 0x346CC200 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-622eeade40ac6608](../../evidence/conditions-sets-038.md#c-622eeade40ac6608) · [状态效果 S-1d47f709e5271186](../../evidence/state_effects-sets-007.md#s-1d47f709e5271186)

### observed_connections-006595

```text
(config-router-af)# default metric maximum-hops <cr>
```

Handler ` RVA 0xF57D6C0 `；selector ` 31 `；EOL ` RVA 0x346D0DD0 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-84f61044791bdb93](../../evidence/conditions-sets-051.md#c-84f61044791bdb93) · [状态效果 S-1d47f709e5271186](../../evidence/state_effects-sets-007.md#s-1d47f709e5271186)

### observed_connections-006598

```text
(config-router-af)# default metric weights <cr>
```

Handler ` RVA 0xF57D6C0 `；selector ` 12 `；EOL ` RVA 0x346D10F8 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-24b0e59c8db0bb56](../../evidence/conditions-sets-014.md#c-24b0e59c8db0bb56) · [状态效果 S-1d47f709e5271186](../../evidence/state_effects-sets-007.md#s-1d47f709e5271186)

### observed_connections-006604

```text
(config-router-af)# default neighbor maximum-prefix <cr>
```

Handler ` RVA 0xF57C0C0 `；selector ` 4 `；EOL ` RVA 0x346D1B38 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6299a59a2de6a376](../../evidence/conditions-sets-038.md#c-6299a59a2de6a376) · [状态效果 S-e06aa7c5f7f2d7b9](../../evidence/state_effects-sets-047.md#s-e06aa7c5f7f2d7b9)

### observed_connections-006588

```text
(config-router-af)# default network <address> <cr>
```

Handler ` RVA 0xF5DEBE0 `；selector ` 22 `；EOL ` RVA 0x346CF7E0 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` Network number。

[条件 C-e1df9b02321472ff](../../evidence/conditions-sets-087.md#c-e1df9b02321472ff) · [参数 P-ad268811cce82193](../../evidence/parameters-sets-013.md#p-ad268811cce82193) · [状态效果 S-1d47f709e5271186](../../evidence/state_effects-sets-007.md#s-1d47f709e5271186)

### observed_connections-006536

```text
(config-router-af)# default nsf <cr>
```

Handler ` RVA 0xDB16C50 `；selector ` 7 `；EOL ` RVA 0x33FCD810 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9e98ed7f30e87844](../../evidence/conditions-sets-061.md#c-9e98ed7f30e87844) · [状态效果 S-1d47f709e5271186](../../evidence/state_effects-sets-007.md#s-1d47f709e5271186)

### observed_connections-006624

```text
(config-router-af)# default offset-list <number:0..99> in <cr>
```

Handler ` RVA 0xF597D70 `；selector ` 30 `；EOL ` RVA 0x346CD738 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Access list of networks to apply offset (0 selects all networks)。

[条件 C-ee931fe9c3dae017](../../evidence/conditions-sets-092.md#c-ee931fe9c3dae017) · [参数 P-f621da43fce7846d](../../evidence/parameters-sets-018.md#p-f621da43fce7846d) · [状态效果 S-b7696d9dd1669373](../../evidence/state_effects-sets-039.md#s-b7696d9dd1669373)

### observed_connections-006600

```text
(config-router-af)# default passive-interface default <cr>
```

Handler ` RVA 0xF58B500 `；selector ` 132 `；EOL ` RVA 0x346D1620 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-721aa60b8ea83258](../../evidence/conditions-sets-044.md#c-721aa60b8ea83258) · [状态效果 S-1541d0b61ae414a1](../../evidence/state_effects-sets-005.md#s-1541d0b61ae414a1)

### observed_connections-006587

```text
(config-router-af)# default redistribute maximum-prefix <cr>
```

Handler ` RVA 0xF598EF0 `；selector ` 33 `；EOL ` RVA 0x346CDC88 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7848752736b6a86f](../../evidence/conditions-sets-047.md#c-7848752736b6a86f) · [状态效果 S-1d47f709e5271186](../../evidence/state_effects-sets-007.md#s-1d47f709e5271186)

### observed_connections-006558

```text
(config-router-af)# default router-id <cr>
```

Handler ` RVA 0xF57EB20 `；selector ` 5 `；EOL ` RVA 0x346D2FE8 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a08385127823e9e5](../../evidence/conditions-sets-062.md#c-a08385127823e9e5) · [状态效果 S-1d47f709e5271186](../../evidence/state_effects-sets-007.md#s-1d47f709e5271186)

### observed_connections-006575

```text
(config-router-af)# default shutdown <cr>
```

Handler ` RVA 0xF57D580 `；selector ` 6 `；EOL ` RVA 0x346D5630 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-978995009b28b8a8](../../evidence/conditions-sets-058.md#c-978995009b28b8a8) · [状态效果 S-1d47f709e5271186](../../evidence/state_effects-sets-007.md#s-1d47f709e5271186)

### observed_connections-006562

```text
(config-router-af)# default stub <cr>
```

Handler ` RVA 0xF57E6E0 `；selector ` 18 `；EOL ` RVA 0x346D3330 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4445ce1f00976b49](../../evidence/conditions-sets-027.md#c-4445ce1f00976b49) · [状态效果 S-1d47f709e5271186](../../evidence/state_effects-sets-007.md#s-1d47f709e5271186)

### observed_connections-006612

```text
(config-router-af)# default summary-metric <address> <address> <cr>
```

Handler ` RVA 0xF599350 `；selector ` 41 `；EOL ` RVA 0x346CAA88 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` Summary to configure static metric；` address ` Network mask。

[条件 C-f32c5ac9a61871bf](../../evidence/conditions-sets-094.md#c-f32c5ac9a61871bf) · [参数 P-ffbf6e322bcc3d15](../../evidence/parameters-sets-019.md#p-ffbf6e322bcc3d15) · [状态效果 S-1d47f709e5271186](../../evidence/state_effects-sets-007.md#s-1d47f709e5271186)

### observed_connections-006580

```text
(config-router-af)# default timers active-time <cr>
```

Handler ` RVA 0xF597780 `；selector ` 28 `；EOL ` RVA 0x346CB170 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3588538deeab9233](../../evidence/conditions-sets-021.md#c-3588538deeab9233) · [状态效果 S-1d47f709e5271186](../../evidence/state_effects-sets-007.md#s-1d47f709e5271186)

### observed_connections-006621

```text
(config-router-af)# default timers nsf converge <cr>
```

Handler ` RVA 0xDB171D0 `；selector ` 9 `；EOL ` RVA 0x33FCDF20 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-58305b406546624a](../../evidence/conditions-sets-035.md#c-58305b406546624a) · [状态效果 S-1d47f709e5271186](../../evidence/state_effects-sets-007.md#s-1d47f709e5271186)

### observed_connections-006615

```text
(config-router-af)# default timers nsf route-hold <cr>
```

Handler ` RVA 0xF57F070 `；selector ` 11 `；EOL ` RVA 0x346CB550 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-af1a06344e8a6c61](../../evidence/conditions-sets-068.md#c-af1a06344e8a6c61) · [状态效果 S-1d47f709e5271186](../../evidence/state_effects-sets-007.md#s-1d47f709e5271186)

### observed_connections-006618

```text
(config-router-af)# default timers nsf signal <cr>
```

Handler ` RVA 0xDB16EC0 `；selector ` 8 `；EOL ` RVA 0x33FCDBF8 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-abc51d127ba6eb2c](../../evidence/conditions-sets-066.md#c-abc51d127ba6eb2c) · [状态效果 S-1d47f709e5271186](../../evidence/state_effects-sets-007.md#s-1d47f709e5271186)

### observed_connections-006583

```text
(config-router-af)# default traffic-share balanced <cr>
```

Handler ` RVA 0xF575880 `；selector ` 40 `；EOL ` RVA 0x346CBE10 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-97b62125ffd7c81a](../../evidence/state_effects-sets-032.md#s-97b62125ffd7c81a)

### observed_connections-006544

```text
(config-router-af)# default variance <cr>
```

Handler ` RVA 0xF575390 `；selector ` 39 `；EOL ` RVA 0x346CC8A8 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-78c09ac2b80f5267](../../evidence/conditions-sets-047.md#c-78c09ac2b80f5267) · [状态效果 S-1d47f709e5271186](../../evidence/state_effects-sets-007.md#s-1d47f709e5271186)

### observed_connections-006549

```text
(config-router-af)# default-information in <cr>
```

Handler ` RVA 0xF5DB530 `；selector ` 48 `；EOL ` RVA 0x346CD108 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-71343b056e770d34](../../evidence/conditions-sets-044.md#c-71343b056e770d34) · [状态效果 S-cdeb3cd6bee4904e](../../evidence/state_effects-sets-044.md#s-cdeb3cd6bee4904e)

### observed_connections-006631

```text
(config-router-af)# default-metric <number:1..4294967295> <number:0..4294967295> <number:0..255> <number:1..255> <number:1..65535> <cr>
```

Handler ` RVA 0xF5756A0 `；selector ` 45 `；EOL ` RVA 0x346CCC00 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Bandwidth in Kbits per second；` unsigned_number ` delay metric in 10 microsecond units；` unsigned_number ` Reliability metric where 255 is 100% reliable；` unsigned_number ` Effective bandwidth metric (Loading) where 255 is 100% loaded；` unsigned_number ` Maximum Transmission Unit metric of the path 。

[条件 C-615952f593f413c7](../../evidence/conditions-sets-038.md#c-615952f593f413c7) · [参数 P-b0aaa7895f2f6f40](../../evidence/parameters-sets-013.md#p-b0aaa7895f2f6f40)

### observed_connections-006626

```text
(config-router-af)# distance <number:1..255> <address> <address> <cr>
```

Handler ` RVA 0xF596F40 `；selector ` 46 `；EOL ` RVA 0x346CFC58 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Set route administrative distance；` address ` IP Source address；` address ` Wildcard bits。

[条件 C-919be1682e67bb3d](../../evidence/conditions-sets-056.md#c-919be1682e67bb3d) · [参数 P-1c0e581156a7a813](../../evidence/parameters-sets-003.md#p-1c0e581156a7a813)

### observed_connections-006625

```text
(config-router-af)# distance eigrp <number:1..255> <number:1..255> <cr>
```

Handler ` RVA 0xF597490 `；selector ` 47 `；EOL ` RVA 0x346D0028 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Distance for internal routes；` unsigned_number ` Distance for external routes。

[条件 C-cad7eb994af203c6](../../evidence/conditions-sets-078.md#c-cad7eb994af203c6) · [参数 P-583853da37e9e87e](../../evidence/parameters-sets-007.md#p-583853da37e9e87e)

### observed_connections-006573

```text
(config-router-af)# distribute-list in <cr>
```

Handler ` RVA 0xF5DBC30 `；selector ` 29 `；EOL ` RVA 0x346D2570 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-52c6f4d562348d21](../../evidence/conditions-sets-032.md#c-52c6f4d562348d21) · [状态效果 S-5cf131a992e68877](../../evidence/state_effects-sets-020.md#s-5cf131a992e68877)

### observed_connections-006642

```text
(config-router-af)# distribute-list out <?router_action_proc_vpn@555589c264f8> <cr>
```

Handler ` RVA 0xF5DBC30 `；selector ` 29 `；EOL ` RVA 0x346D2570 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-272c63e20fc62c76](../../evidence/conditions-sets-015.md#c-272c63e20fc62c76) · [缺口 G-1de964a94f655214](../../evidence/gaps-sets-002.md#g-1de964a94f655214) · [状态效果 S-13becc71d98d66f6](../../evidence/state_effects-sets-005.md#s-13becc71d98d66f6)

### observed_connections-006576

```text
(config-router-af)# eigrp graceful-restart <cr>
```

Handler ` RVA 0xF57EE00 `；selector ` 10 `；EOL ` RVA 0x346D4E18 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c88fe7d57831e9ab](../../evidence/conditions-sets-077.md#c-c88fe7d57831e9ab)

### observed_connections-006610

```text
(config-router-af)# eigrp upgrade-cli <string> <cr>
```

Handler ` RVA 0xF5807E0 `；selector ` 142 `；EOL ` RVA 0x346D52F8 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` EIGRP Virtual-Instance Name。

[条件 C-cc9b20bf7f82427f](../../evidence/conditions-sets-079.md#c-cc9b20bf7f82427f) · [参数 P-3bb7808def1d39b2](../../evidence/parameters-sets-005.md#p-3bb7808def1d39b2)

### observed_connections-006638

```text
(config-router-af)# event-log-size <number:dynamic> <cr>
```

Handler ` RVA 0xF596700 `；selector ` 35 `；EOL ` RVA 0x346D4A40 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Max event log entries。

[条件 C-49a72522d7b14ad1](../../evidence/conditions-sets-029.md#c-49a72522d7b14ad1) · [缺口 G-05c332c96550f22d](../../evidence/gaps-sets-001.md#g-05c332c96550f22d) · [参数 P-e344e02ae5874950](../../evidence/parameters-sets-017.md#p-e344e02ae5874950)

### observed_connections-006529

```text
(config-router-af)# event-logging <cr>
```

Handler ` RVA 0xF596700 `；selector ` 36 `；EOL ` RVA 0x346D4700 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-978995009b28b8a8](../../evidence/conditions-sets-058.md#c-978995009b28b8a8)

### observed_connections-006524

```text
(config-router-af)# exit-address-family <cr>
```

Handler ` RVA 0xF579A40 `；selector ` 0 `；EOL ` RVA 0x346CA648 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-605391f07cb24622](../../evidence/conditions-sets-037.md#c-605391f07cb24622)

### observed_connections-006527

```text
(config-router-af)# kill-everyone <cr>
```

Handler ` RVA 0xF57B0C0 `；selector ` 15 `；EOL ` RVA 0x346D39A8 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-978995009b28b8a8](../../evidence/conditions-sets-058.md#c-978995009b28b8a8)

### observed_connections-006532

```text
(config-router-af)# log-event-type <cr>
```

Handler ` RVA 0xF596700 `；selector ` 34 `；EOL ` RVA 0x346D4318 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2a667990c4157681](../../evidence/conditions-sets-017.md#c-2a667990c4157681)

### observed_connections-006528

```text
(config-router-af)# log-neighbor-changes <cr>
```

Handler ` RVA 0xF57B3F0 `；selector ` 16 `；EOL ` RVA 0x346D3C88 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-978995009b28b8a8](../../evidence/conditions-sets-058.md#c-978995009b28b8a8)

### observed_connections-006530

```text
(config-router-af)# log-neighbor-warnings <cr>
```

Handler ` RVA 0xF57B570 `；selector ` 17 `；EOL ` RVA 0x346D3FC8 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0262bb3723a41334](../../evidence/conditions-sets-001.md#c-0262bb3723a41334)

### observed_connections-006635

```text
(config-router-af)# maximum-paths <number:dynamic> <cr>
```

Handler ` RVA 0xF5985F0 `；selector ` 37 `；EOL ` RVA 0x346CC558 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Number of paths。

[条件 C-a0452f002707aea4](../../evidence/conditions-sets-062.md#c-a0452f002707aea4) · [缺口 G-7d39694c7479a898](../../evidence/gaps-sets-005.md#g-7d39694c7479a898) · [参数 P-8ec0ed4e81dec53f](../../evidence/parameters-sets-011.md#p-8ec0ed4e81dec53f)

### observed_connections-006563

```text
(config-router-af)# maximum-prefix <number:1..4294967295> <cr>
```

Handler ` RVA 0xF579E30 `；selector ` 20 `；EOL ` RVA 0x346D06F8 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of prefixes for maximum-prefix limit。

[条件 C-b9eab30c9794ff9d](../../evidence/conditions-sets-072.md#c-b9eab30c9794ff9d) · [参数 P-5e4d9bca5700fe4e](../../evidence/parameters-sets-008.md#p-5e4d9bca5700fe4e)

### observed_connections-006634

```text
(config-router-af)# maximum-secondary-paths <number:dynamic> <cr>
```

Handler ` RVA 0xF5987B0 `；selector ` 38 `；EOL ` RVA 0x346CC200 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Number of paths。

[条件 C-9c366722867ecbc8](../../evidence/conditions-sets-060.md#c-9c366722867ecbc8) · [缺口 G-4904c5a25f49632f](../../evidence/gaps-sets-003.md#g-4904c5a25f49632f) · [参数 P-0d18ccfb4bbe67ff](../../evidence/parameters-sets-001.md#p-0d18ccfb4bbe67ff)

### observed_connections-006594

```text
(config-router-af)# metric maximum-hops <number:1..255> <cr>
```

Handler ` RVA 0xF57D6C0 `；selector ` 31 `；EOL ` RVA 0x346D0DD0 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Hop count。

[条件 C-9f1a564236cfbaf5](../../evidence/conditions-sets-062.md#c-9f1a564236cfbaf5) · [参数 P-f18340336ee46ce3](../../evidence/parameters-sets-018.md#p-f18340336ee46ce3)

### observed_connections-006632

```text
(config-router-af)# metric weights <number:0..8> <number:0..255> <number:0..255> <number:0..255> <number:0..255> <number:0..255> <cr>
```

Handler ` RVA 0xF57D6C0 `；selector ` 12 `；EOL ` RVA 0x346D10F8 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Type (Only TOS 0 supported)；` unsigned_number ` K1；` unsigned_number ` K2；` unsigned_number ` K3；` unsigned_number ` K4；` unsigned_number ` K5。

[条件 C-8fa0953858a22340](../../evidence/conditions-sets-056.md#c-8fa0953858a22340) · [参数 P-30eaf2a156546f5f](../../evidence/parameters-sets-004.md#p-30eaf2a156546f5f)

### observed_connections-006641

```text
(config-router-af)# neighbor <address> <interface> <cr>
```

Handler ` RVA 0xF57C0C0 `；selector ` 4 `；EOL ` RVA 0x346D1B38 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Neighbor address。

[条件 C-e18171519787d4e5](../../evidence/conditions-sets-087.md#c-e18171519787d4e5) · [缺口 G-aaad3487d5160c59](../../evidence/gaps-sets-006.md#g-aaad3487d5160c59) · [参数 P-4c255435163c9597](../../evidence/parameters-sets-006.md#p-4c255435163c9597) · [状态效果 S-d69c7856f5bdcf7d](../../evidence/state_effects-sets-045.md#s-d69c7856f5bdcf7d)

### observed_connections-006605

```text
(config-router-af)# neighbor maximum-prefix <number:1..4294967295> <cr>
```

Handler ` RVA 0xF57C0C0 `；selector ` 4 `；EOL ` RVA 0x346D1B38 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of prefixs for maximum-prefix limit。

[条件 C-2f311b2a63ff95e8](../../evidence/conditions-sets-018.md#c-2f311b2a63ff95e8) · [参数 P-40bd1d97d8cc4246](../../evidence/parameters-sets-005.md#p-40bd1d97d8cc4246) · [状态效果 S-67f30c0506230bc3](../../evidence/state_effects-sets-022.md#s-67f30c0506230bc3)

### observed_connections-006547

```text
(config-router-af)# network <address> <cr>
```

Handler ` RVA 0xF5DEBE0 `；selector ` 22 `；EOL ` RVA 0x346CF7E0 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Network number。

[条件 C-e1df9b02321472ff](../../evidence/conditions-sets-087.md#c-e1df9b02321472ff) · [参数 P-ad268811cce82193](../../evidence/parameters-sets-013.md#p-ad268811cce82193)

### observed_connections-006548

```text
(config-router-af)# no auto-summary <cr>
```

Handler ` RVA 0xF575B20 `；selector ` 42 `；EOL ` RVA 0x346D03B8 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1f9a30c4f2fba0b7](../../evidence/conditions-sets-012.md#c-1f9a30c4f2fba0b7) · [状态效果 S-1bebc37b48b22b7b](../../evidence/state_effects-sets-006.md#s-1bebc37b48b22b7b)

### observed_connections-006599

```text
(config-router-af)# no autonomous-system <number:1..65535> <cr>
```

Handler ` RVA 0xF5DF260 `；selector ` 120 `；EOL ` RVA 0x346D2C90 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Autonomous System。

[条件 C-978995009b28b8a8](../../evidence/conditions-sets-058.md#c-978995009b28b8a8) · [参数 P-3e9285c714b1f8b6](../../evidence/parameters-sets-005.md#p-3e9285c714b1f8b6) · [状态效果 S-1bebc37b48b22b7b](../../evidence/state_effects-sets-006.md#s-1bebc37b48b22b7b)

### observed_connections-006579

```text
(config-router-af)# no bfd all-interfaces <cr>
```

Handler ` RVA 0xF57A660 `；selector ` 52 `；EOL ` RVA 0x346CB9F8 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-ce1db4af11f4d02c](../../evidence/state_effects-sets-044.md#s-ce1db4af11f4d02c)

### observed_connections-006589

```text
(config-router-af)# no default-information in <cr>
```

Handler ` RVA 0xF5DB530 `；selector ` 48 `；EOL ` RVA 0x346CD108 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-71343b056e770d34](../../evidence/conditions-sets-044.md#c-71343b056e770d34) · [状态效果 S-ea86fa10112e32e1](../../evidence/state_effects-sets-050.md#s-ea86fa10112e32e1)

### observed_connections-006545

```text
(config-router-af)# no default-metric <cr>
```

Handler ` RVA 0xF5756A0 `；selector ` 45 `；EOL ` RVA 0x346CCC00 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7f68d15bf2977465](../../evidence/conditions-sets-049.md#c-7f68d15bf2977465) · [状态效果 S-1bebc37b48b22b7b](../../evidence/state_effects-sets-006.md#s-1bebc37b48b22b7b)

### observed_connections-006629

```text
(config-router-af)# no distance <number:1..255> <address> <address> <cr>
```

Handler ` RVA 0xF596F40 `；selector ` 46 `；EOL ` RVA 0x346CFC58 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Set route administrative distance；` address ` IP Source address；` address ` Wildcard bits。

[条件 C-2643c4dff09adc42](../../evidence/conditions-sets-015.md#c-2643c4dff09adc42) · [参数 P-1c0e581156a7a813](../../evidence/parameters-sets-003.md#p-1c0e581156a7a813) · [状态效果 S-1bebc37b48b22b7b](../../evidence/state_effects-sets-006.md#s-1bebc37b48b22b7b)

### observed_connections-006591

```text
(config-router-af)# no distance eigrp <cr>
```

Handler ` RVA 0xF597490 `；selector ` 47 `；EOL ` RVA 0x346D0028 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d32cb02667355857](../../evidence/conditions-sets-081.md#c-d32cb02667355857) · [状态效果 S-1bebc37b48b22b7b](../../evidence/state_effects-sets-006.md#s-1bebc37b48b22b7b)

### observed_connections-006606

```text
(config-router-af)# no distribute-list in <cr>
```

Handler ` RVA 0xF5DBC30 `；selector ` 29 `；EOL ` RVA 0x346D2570 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-52c6f4d562348d21](../../evidence/conditions-sets-032.md#c-52c6f4d562348d21) · [状态效果 S-d8a1c5311886b01d](../../evidence/state_effects-sets-046.md#s-d8a1c5311886b01d)

### observed_connections-006608

```text
(config-router-af)# no eigrp graceful-restart <cr>
```

Handler ` RVA 0xF57EE00 `；selector ` 10 `；EOL ` RVA 0x346D4E18 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4cef9241756ec533](../../evidence/conditions-sets-030.md#c-4cef9241756ec533) · [状态效果 S-1bebc37b48b22b7b](../../evidence/state_effects-sets-006.md#s-1bebc37b48b22b7b)

### observed_connections-006627

```text
(config-router-af)# no eigrp upgrade-cli <string> <cr>
```

Handler ` RVA 0xF5807E0 `；selector ` 142 `；EOL ` RVA 0x346D52F8 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` EIGRP Virtual-Instance Name。

[条件 C-cc9b20bf7f82427f](../../evidence/conditions-sets-079.md#c-cc9b20bf7f82427f) · [参数 P-3bb7808def1d39b2](../../evidence/parameters-sets-005.md#p-3bb7808def1d39b2) · [状态效果 S-1bebc37b48b22b7b](../../evidence/state_effects-sets-006.md#s-1bebc37b48b22b7b)

### observed_connections-006571

```text
(config-router-af)# no event-log-size <cr>
```

Handler ` RVA 0xF596700 `；selector ` 35 `；EOL ` RVA 0x346D4A40 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-581d5e4de9cf698f](../../evidence/conditions-sets-035.md#c-581d5e4de9cf698f) · [状态效果 S-1bebc37b48b22b7b](../../evidence/state_effects-sets-006.md#s-1bebc37b48b22b7b)

### observed_connections-006566

```text
(config-router-af)# no event-logging <cr>
```

Handler ` RVA 0xF596700 `；selector ` 36 `；EOL ` RVA 0x346D4700 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-978995009b28b8a8](../../evidence/conditions-sets-058.md#c-978995009b28b8a8) · [状态效果 S-1bebc37b48b22b7b](../../evidence/state_effects-sets-006.md#s-1bebc37b48b22b7b)

### observed_connections-006557

```text
(config-router-af)# no kill-everyone <cr>
```

Handler ` RVA 0xF57B0C0 `；selector ` 15 `；EOL ` RVA 0x346D39A8 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-978995009b28b8a8](../../evidence/conditions-sets-058.md#c-978995009b28b8a8) · [状态效果 S-1bebc37b48b22b7b](../../evidence/state_effects-sets-006.md#s-1bebc37b48b22b7b)

### observed_connections-006568

```text
(config-router-af)# no log-event-type <cr>
```

Handler ` RVA 0xF596700 `；selector ` 34 `；EOL ` RVA 0x346D4318 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7419cd001ef9998e](../../evidence/conditions-sets-045.md#c-7419cd001ef9998e) · [状态效果 S-1bebc37b48b22b7b](../../evidence/state_effects-sets-006.md#s-1bebc37b48b22b7b)

### observed_connections-006561

```text
(config-router-af)# no log-neighbor-changes <cr>
```

Handler ` RVA 0xF57B3F0 `；selector ` 16 `；EOL ` RVA 0x346D3C88 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-978995009b28b8a8](../../evidence/conditions-sets-058.md#c-978995009b28b8a8) · [状态效果 S-1bebc37b48b22b7b](../../evidence/state_effects-sets-006.md#s-1bebc37b48b22b7b)

### observed_connections-006565

```text
(config-router-af)# no log-neighbor-warnings <cr>
```

Handler ` RVA 0xF57B570 `；selector ` 17 `；EOL ` RVA 0x346D3FC8 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b803cc4e8b80fe34](../../evidence/conditions-sets-071.md#c-b803cc4e8b80fe34) · [状态效果 S-1bebc37b48b22b7b](../../evidence/state_effects-sets-006.md#s-1bebc37b48b22b7b)

### observed_connections-006539

```text
(config-router-af)# no maximum-paths <cr>
```

Handler ` RVA 0xF5985F0 `；selector ` 37 `；EOL ` RVA 0x346CC558 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-6b0391e88770c702](../../evidence/conditions-sets-041.md#c-6b0391e88770c702) · [状态效果 S-1bebc37b48b22b7b](../../evidence/state_effects-sets-006.md#s-1bebc37b48b22b7b)

### observed_connections-006551

```text
(config-router-af)# no maximum-prefix <cr>
```

Handler ` RVA 0xF579E30 `；selector ` 20 `；EOL ` RVA 0x346D06F8 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d036696adb8bd71b](../../evidence/conditions-sets-080.md#c-d036696adb8bd71b) · [状态效果 S-1bebc37b48b22b7b](../../evidence/state_effects-sets-006.md#s-1bebc37b48b22b7b)

### observed_connections-006538

```text
(config-router-af)# no maximum-secondary-paths <cr>
```

Handler ` RVA 0xF5987B0 `；selector ` 38 `；EOL ` RVA 0x346CC200 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5ed01fa3dbab0930](../../evidence/conditions-sets-037.md#c-5ed01fa3dbab0930) · [状态效果 S-1bebc37b48b22b7b](../../evidence/state_effects-sets-006.md#s-1bebc37b48b22b7b)

### observed_connections-006593

```text
(config-router-af)# no metric maximum-hops <cr>
```

Handler ` RVA 0xF57D6C0 `；selector ` 31 `；EOL ` RVA 0x346D0DD0 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b82482c2c105d354](../../evidence/conditions-sets-071.md#c-b82482c2c105d354) · [状态效果 S-1bebc37b48b22b7b](../../evidence/state_effects-sets-006.md#s-1bebc37b48b22b7b)

### observed_connections-006596

```text
(config-router-af)# no metric weights <cr>
```

Handler ` RVA 0xF57D6C0 `；selector ` 12 `；EOL ` RVA 0x346D10F8 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0031b4951b7e24d2](../../evidence/conditions-sets-001.md#c-0031b4951b7e24d2) · [状态效果 S-1bebc37b48b22b7b](../../evidence/state_effects-sets-006.md#s-1bebc37b48b22b7b)

### observed_connections-006603

```text
(config-router-af)# no neighbor maximum-prefix <cr>
```

Handler ` RVA 0xF57C0C0 `；selector ` 4 `；EOL ` RVA 0x346D1B38 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a2be6c5ee1a93db5](../../evidence/conditions-sets-063.md#c-a2be6c5ee1a93db5) · [状态效果 S-cef542364ee08acf](../../evidence/state_effects-sets-044.md#s-cef542364ee08acf)

### observed_connections-006586

```text
(config-router-af)# no network <address> <cr>
```

Handler ` RVA 0xF5DEBE0 `；selector ` 22 `；EOL ` RVA 0x346CF7E0 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` Network number。

[条件 C-e1df9b02321472ff](../../evidence/conditions-sets-087.md#c-e1df9b02321472ff) · [参数 P-ad268811cce82193](../../evidence/parameters-sets-013.md#p-ad268811cce82193) · [状态效果 S-1bebc37b48b22b7b](../../evidence/state_effects-sets-006.md#s-1bebc37b48b22b7b)

### observed_connections-006534

```text
(config-router-af)# no nsf <cr>
```

Handler ` RVA 0xDB16C50 `；selector ` 7 `；EOL ` RVA 0x33FCD810 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ebb493205511d74b](../../evidence/conditions-sets-091.md#c-ebb493205511d74b) · [状态效果 S-1bebc37b48b22b7b](../../evidence/state_effects-sets-006.md#s-1bebc37b48b22b7b)

### observed_connections-006623

```text
(config-router-af)# no offset-list <number:0..99> in <cr>
```

Handler ` RVA 0xF597D70 `；selector ` 30 `；EOL ` RVA 0x346CD738 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Access list of networks to apply offset (0 selects all networks)。

[条件 C-ee931fe9c3dae017](../../evidence/conditions-sets-092.md#c-ee931fe9c3dae017) · [参数 P-f621da43fce7846d](../../evidence/parameters-sets-018.md#p-f621da43fce7846d) · [状态效果 S-d71816bd46f80ee7](../../evidence/state_effects-sets-046.md#s-d71816bd46f80ee7)

### observed_connections-006597

```text
(config-router-af)# no passive-interface default <cr>
```

Handler ` RVA 0xF58B500 `；selector ` 132 `；EOL ` RVA 0x346D1620 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-721aa60b8ea83258](../../evidence/conditions-sets-044.md#c-721aa60b8ea83258) · [状态效果 S-c492525af0a989a3](../../evidence/state_effects-sets-042.md#s-c492525af0a989a3)

### observed_connections-006585

```text
(config-router-af)# no redistribute maximum-prefix <cr>
```

Handler ` RVA 0xF598EF0 `；selector ` 33 `；EOL ` RVA 0x346CDC88 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-9dd9365adfbf6839](../../evidence/conditions-sets-061.md#c-9dd9365adfbf6839) · [状态效果 S-1bebc37b48b22b7b](../../evidence/state_effects-sets-006.md#s-1bebc37b48b22b7b)

### observed_connections-006555

```text
(config-router-af)# no router-id <cr>
```

Handler ` RVA 0xF57EB20 `；selector ` 5 `；EOL ` RVA 0x346D2FE8 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-035f0d2d16954070](../../evidence/conditions-sets-002.md#c-035f0d2d16954070) · [状态效果 S-1bebc37b48b22b7b](../../evidence/state_effects-sets-006.md#s-1bebc37b48b22b7b)

### observed_connections-006572

```text
(config-router-af)# no shutdown <cr>
```

Handler ` RVA 0xF57D580 `；selector ` 6 `；EOL ` RVA 0x346D5630 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-978995009b28b8a8](../../evidence/conditions-sets-058.md#c-978995009b28b8a8) · [状态效果 S-1bebc37b48b22b7b](../../evidence/state_effects-sets-006.md#s-1bebc37b48b22b7b)

### observed_connections-006559

```text
(config-router-af)# no stub <cr>
```

Handler ` RVA 0xF57E6E0 `；selector ` 18 `；EOL ` RVA 0x346D3330 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-fdb6a6c8541ffc03](../../evidence/conditions-sets-098.md#c-fdb6a6c8541ffc03) · [状态效果 S-1bebc37b48b22b7b](../../evidence/state_effects-sets-006.md#s-1bebc37b48b22b7b)

### observed_connections-006611

```text
(config-router-af)# no summary-metric <address> <address> <cr>
```

Handler ` RVA 0xF599350 `；selector ` 41 `；EOL ` RVA 0x346CAA88 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` Summary to configure static metric；` address ` Network mask。

[条件 C-62b23b2f16f04661](../../evidence/conditions-sets-038.md#c-62b23b2f16f04661) · [参数 P-ffbf6e322bcc3d15](../../evidence/parameters-sets-019.md#p-ffbf6e322bcc3d15) · [状态效果 S-1bebc37b48b22b7b](../../evidence/state_effects-sets-006.md#s-1bebc37b48b22b7b)

### observed_connections-006577

```text
(config-router-af)# no timers active-time <cr>
```

Handler ` RVA 0xF597780 `；selector ` 28 `；EOL ` RVA 0x346CB170 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7368eddfc3aecc2c](../../evidence/conditions-sets-045.md#c-7368eddfc3aecc2c) · [状态效果 S-1bebc37b48b22b7b](../../evidence/state_effects-sets-006.md#s-1bebc37b48b22b7b)

### observed_connections-006619

```text
(config-router-af)# no timers nsf converge <cr>
```

Handler ` RVA 0xDB171D0 `；selector ` 9 `；EOL ` RVA 0x33FCDF20 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5b0ed19d6abf7a5e](../../evidence/conditions-sets-036.md#c-5b0ed19d6abf7a5e) · [状态效果 S-1bebc37b48b22b7b](../../evidence/state_effects-sets-006.md#s-1bebc37b48b22b7b)

### observed_connections-006613

```text
(config-router-af)# no timers nsf route-hold <cr>
```

Handler ` RVA 0xF57F070 `；selector ` 11 `；EOL ` RVA 0x346CB550 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-186a8cf629ac62ba](../../evidence/conditions-sets-010.md#c-186a8cf629ac62ba) · [状态效果 S-1bebc37b48b22b7b](../../evidence/state_effects-sets-006.md#s-1bebc37b48b22b7b)

### observed_connections-006616

```text
(config-router-af)# no timers nsf signal <cr>
```

Handler ` RVA 0xDB16EC0 `；selector ` 8 `；EOL ` RVA 0x33FCDBF8 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-88ccafae0f02a838](../../evidence/conditions-sets-053.md#c-88ccafae0f02a838) · [状态效果 S-1bebc37b48b22b7b](../../evidence/state_effects-sets-006.md#s-1bebc37b48b22b7b)

### observed_connections-006582

```text
(config-router-af)# no traffic-share balanced <cr>
```

Handler ` RVA 0xF575880 `；selector ` 40 `；EOL ` RVA 0x346CBE10 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-7394583d28e51f6e](../../evidence/state_effects-sets-025.md#s-7394583d28e51f6e)

### observed_connections-006542

```text
(config-router-af)# no variance <cr>
```

Handler ` RVA 0xF575390 `；selector ` 39 `；EOL ` RVA 0x346CC8A8 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-398320f55d04e1e4](../../evidence/conditions-sets-022.md#c-398320f55d04e1e4) · [状态效果 S-1bebc37b48b22b7b](../../evidence/state_effects-sets-006.md#s-1bebc37b48b22b7b)

### observed_connections-006525

```text
(config-router-af)# nsf <cr>
```

Handler ` RVA 0xDB16C50 `；selector ` 7 `；EOL ` RVA 0x33FCD810 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1f7281957fe3bcc7](../../evidence/conditions-sets-012.md#c-1f7281957fe3bcc7)

### observed_connections-006622

```text
(config-router-af)# offset-list <number:0..99> in <number:0..2147483647> <cr>
```

Handler ` RVA 0xF597D70 `；selector ` 30 `；EOL ` RVA 0x346CD738 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Access list of networks to apply offset (0 selects all networks)；` unsigned_number ` Offset。

[条件 C-68f4d25db430dbd3](../../evidence/conditions-sets-041.md#c-68f4d25db430dbd3) · [参数 P-382b678163cf2a8c](../../evidence/parameters-sets-005.md#p-382b678163cf2a8c) · [状态效果 S-93d78da23924c88b](../../evidence/state_effects-sets-031.md#s-93d78da23924c88b)

### observed_connections-006640

```text
(config-router-af)# offset-list <string> in <cr>
```

Handler ` RVA 0xF597D70 `；selector ` 30 `；EOL ` RVA 0x346CD738 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Access-list name。

[条件 C-2f34f34b6c62d15e](../../evidence/conditions-sets-018.md#c-2f34f34b6c62d15e) · [缺口 G-95e827cc0a1e2ad5](../../evidence/gaps-sets-005.md#g-95e827cc0a1e2ad5) · [参数 P-1d943678e194c909](../../evidence/parameters-sets-003.md#p-1d943678e194c909) · [状态效果 S-66c502c23ccd0cdc](../../evidence/state_effects-sets-022.md#s-66c502c23ccd0cdc)

### observed_connections-006636

```text
(config-router-af)# passive-interface <interface> <cr>
```

Handler ` RVA 0xF58B500 `；selector ` 132 `；EOL ` RVA 0x346D1620 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4676f1ffa5220cc1](../../evidence/conditions-sets-028.md#c-4676f1ffa5220cc1) · [缺口 G-a90882d2a05ae97e](../../evidence/gaps-sets-006.md#g-a90882d2a05ae97e) · [参数 P-da81fb2114df2bdf](../../evidence/parameters-sets-016.md#p-da81fb2114df2bdf)

### observed_connections-006553

```text
(config-router-af)# passive-interface default <cr>
```

Handler ` RVA 0xF58B500 `；selector ` 132 `；EOL ` RVA 0x346D1620 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-721aa60b8ea83258](../../evidence/conditions-sets-044.md#c-721aa60b8ea83258) · [状态效果 S-71625b164ed8db5b](../../evidence/state_effects-sets-024.md#s-71625b164ed8db5b)

### observed_connections-006637

```text
(config-router-af)# redistribute <?router_action_no_proc_vpn@555589c222d0> <cr>
```

Handler ` RVA 0xF5DE550 `；selector ` 32 `；EOL ` RVA 0x346CF2B8 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-41582289683133f5](../../evidence/conditions-sets-026.md#c-41582289683133f5) · [缺口 G-e1d5cfa140560a1e](../../evidence/gaps-sets-008.md#g-e1d5cfa140560a1e)

### observed_connections-006601

```text
(config-router-af)# redistribute maximum-prefix <number:1..4294967295> <cr>
```

Handler ` RVA 0xF598EF0 `；selector ` 33 `；EOL ` RVA 0x346CDC88 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Maximum number of IP prefixes redistributed。

[条件 C-57ce2c3b00857337](../../evidence/conditions-sets-034.md#c-57ce2c3b00857337) · [参数 P-f2043ae1a7988118](../../evidence/parameters-sets-018.md#p-f2043ae1a7988118)

### observed_connections-006556

```text
(config-router-af)# router-id <address> <cr>
```

Handler ` RVA 0xF57EB20 `；selector ` 5 `；EOL ` RVA 0x346D2FE8 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` EIGRP Router-ID in IP address format。

[条件 C-4a4b81a09dbf177e](../../evidence/conditions-sets-029.md#c-4a4b81a09dbf177e) · [参数 P-76007312b0a6a8c2](../../evidence/parameters-sets-009.md#p-76007312b0a6a8c2)

### observed_connections-006531

```text
(config-router-af)# shutdown <cr>
```

Handler ` RVA 0xF57D580 `；selector ` 6 `；EOL ` RVA 0x346D5630 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-978995009b28b8a8](../../evidence/conditions-sets-058.md#c-978995009b28b8a8)

### observed_connections-006533

```text
(config-router-af)# stub <cr>
```

Handler ` RVA 0xF57E6E0 `；selector ` 18 `；EOL ` RVA 0x346D3330 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-21e8b0dce2cfddc3](../../evidence/conditions-sets-013.md#c-21e8b0dce2cfddc3)

### observed_connections-006584

```text
(config-router-af)# summary-metric <address> <address> <cr>
```

Handler ` RVA 0xF599350 `；selector ` 41 `；EOL ` RVA 0x346CAA88 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Summary to configure static metric；` address ` Network mask。

[条件 C-45bddeaca999b8de](../../evidence/conditions-sets-027.md#c-45bddeaca999b8de) · [参数 P-ffbf6e322bcc3d15](../../evidence/parameters-sets-019.md#p-ffbf6e322bcc3d15)

### observed_connections-006633

```text
(config-router-af)# summary-metric <prefix:dynamic> <cr>
```

Handler ` RVA 0xF599350 `；selector ` 41 `；EOL ` RVA 0x346CAA88 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` Summary &lt;network&gt;/&lt;length&gt;, e.g., 192.168.0.0/16。

[条件 C-d723895a328f267b](../../evidence/conditions-sets-083.md#c-d723895a328f267b) · [缺口 G-c6f0d57bb5a4a48e](../../evidence/gaps-sets-007.md#g-c6f0d57bb5a4a48e) · [参数 P-2f8b88910a28a310](../../evidence/parameters-sets-004.md#p-2f8b88910a28a310) · [状态效果 S-eb60c028b3af1616](../../evidence/state_effects-sets-050.md#s-eb60c028b3af1616)

### observed_connections-006578

```text
(config-router-af)# timers active-time disabled <cr>
```

Handler ` RVA 0xF597780 `；selector ` 28 `；EOL ` RVA 0x346CB170 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ccd9c6cc6cdc4993](../../evidence/conditions-sets-079.md#c-ccd9c6cc6cdc4993)

### observed_connections-006620

```text
(config-router-af)# timers nsf converge <number:60..180> <cr>
```

Handler ` RVA 0xDB171D0 `；selector ` 9 `；EOL ` RVA 0x33FCDF20 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Seconds。

[条件 C-7ffc079031c2d581](../../evidence/conditions-sets-050.md#c-7ffc079031c2d581) · [参数 P-9b5a8fb4a495e6ef](../../evidence/parameters-sets-012.md#p-9b5a8fb4a495e6ef)

### observed_connections-006614

```text
(config-router-af)# timers nsf route-hold <number:20..300> <cr>
```

Handler ` RVA 0xF57F070 `；selector ` 11 `；EOL ` RVA 0x346CB550 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Seconds。

[条件 C-3ec2c5e383c41d00](../../evidence/conditions-sets-024.md#c-3ec2c5e383c41d00) · [参数 P-81e8e76343891e60](../../evidence/parameters-sets-010.md#p-81e8e76343891e60)

### observed_connections-006617

```text
(config-router-af)# timers nsf signal <number:10..30> <cr>
```

Handler ` RVA 0xDB16EC0 `；selector ` 8 `；EOL ` RVA 0x33FCDBF8 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Seconds。

[条件 C-6afcad8b24851671](../../evidence/conditions-sets-041.md#c-6afcad8b24851671) · [参数 P-25430a659809aae2](../../evidence/parameters-sets-003.md#p-25430a659809aae2)

### observed_connections-006537

```text
(config-router-af)# traffic-share balanced <cr>
```

Handler ` RVA 0xF575880 `；selector ` 40 `；EOL ` RVA 0x346CBE10 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[状态效果 S-eeae82b66408ff02](../../evidence/state_effects-sets-050.md#s-eeae82b66408ff02)

### observed_connections-006543

```text
(config-router-af)# variance <number:1..128> <cr>
```

Handler ` RVA 0xF575390 `；selector ` 39 `；EOL ` RVA 0x346CC8A8 `。

模式根 ` RVA 0x346CA120 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Metric variance multiplier。

[条件 C-210610960fc4139a](../../evidence/conditions-sets-013.md#c-210610960fc4139a) · [参数 P-e77add1096b7997c](../../evidence/parameters-sets-017.md#p-e77add1096b7997c)
