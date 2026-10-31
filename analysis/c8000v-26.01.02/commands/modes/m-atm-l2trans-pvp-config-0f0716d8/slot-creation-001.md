# atm-l2trans-pvp-config · 依赖静态建槽的条件安装

[模式索引](README.md) · [总索引](../../README.md)

### static_slot_creation_candidates-004142

```text
(cfg-if-atm-l2trans-pvp)# abr <number:dynamic> <number:dynamic> <cr>
```

Handler ` RVA 0x1660E520 `；selector ` 8 `；EOL ` RVA 0x35FB7250 `。

模式根 ` RVA 0x35FB60F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Peak Cell Rate(PCR) in Kbps；` unsigned_number_dynamic ` Minimum Cell Rate(MCR) in Kbps。

[候选注册 R-35d9d9efc15f3484](../../evidence/conditional_registrations-sets-001.md#r-35d9d9efc15f3484) · [条件 C-cc42e6c2cac9ac16](../../evidence/conditions-sets-079.md#c-cc42e6c2cac9ac16) · [缺口 G-92783bc1814ea3fd](../../evidence/gaps-sets-005.md#g-92783bc1814ea3fd) · [参数 P-1305fe641d4007e4](../../evidence/parameters-sets-002.md#p-1305fe641d4007e4)

### static_slot_creation_candidates-004138

```text
(cfg-if-atm-l2trans-pvp)# cbr <number:dynamic> <cr>
```

Handler ` RVA 0x1660E520 `；selector ` 5 `；EOL ` RVA 0x35FB7630 `。

模式根 ` RVA 0x35FB60F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Peak Cell Rate in Kbps。

[候选注册 R-35d9d9efc15f3484](../../evidence/conditional_registrations-sets-001.md#r-35d9d9efc15f3484) · [条件 C-23d2bdae8e153259](../../evidence/conditions-sets-014.md#c-23d2bdae8e153259) · [缺口 G-b6de4cba6d46c553](../../evidence/gaps-sets-006.md#g-b6de4cba6d46c553) · [参数 P-b277177f87e06394](../../evidence/parameters-sets-014.md#p-b277177f87e06394)

### static_slot_creation_candidates-004112

```text
(cfg-if-atm-l2trans-pvp)# cell-packing <cr>
```

Handler ` RVA 0x1660E520 `；selector ` 1 `；EOL ` RVA 0x35FB7D50 `。

模式根 ` RVA 0x35FB60F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-35d9d9efc15f3484](../../evidence/conditional_registrations-sets-001.md#r-35d9d9efc15f3484) · [条件 C-e871fbbbc7785f17](../../evidence/conditions-sets-090.md#c-e871fbbbc7785f17) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### static_slot_creation_candidates-004137

```text
(cfg-if-atm-l2trans-pvp)# cell-packing <number:dynamic> <cr>
```

Handler ` RVA 0x1660E520 `；selector ` 1 `；EOL ` RVA 0x35FB7D50 `。

模式根 ` RVA 0x35FB60F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Maximum number of Cells in a packet。

[候选注册 R-35d9d9efc15f3484](../../evidence/conditional_registrations-sets-001.md#r-35d9d9efc15f3484) · [条件 C-968ed2f11441b1dc](../../evidence/conditions-sets-058.md#c-968ed2f11441b1dc) · [缺口 G-cbc6e542bc101ee8](../../evidence/gaps-sets-007.md#g-cbc6e542bc101ee8) · [参数 P-e203122884160e2b](../../evidence/parameters-sets-017.md#p-e203122884160e2b) · [状态效果 S-b35362e8840a9c56](../../evidence/state_effects-sets-038.md#s-b35362e8840a9c56)

### static_slot_creation_candidates-004127

```text
(cfg-if-atm-l2trans-pvp)# default abr <cr>
```

Handler ` RVA 0x1660E520 `；selector ` 8 `；EOL ` RVA 0x35FB7250 `。

模式根 ` RVA 0x35FB60F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-35d9d9efc15f3484](../../evidence/conditional_registrations-sets-001.md#r-35d9d9efc15f3484) · [条件 C-be0840371ab9e253](../../evidence/conditions-sets-073.md#c-be0840371ab9e253) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-15861ff6767dbc6d](../../evidence/state_effects-sets-005.md#s-15861ff6767dbc6d)

### static_slot_creation_candidates-004130

```text
(cfg-if-atm-l2trans-pvp)# default cbr <cr>
```

Handler ` RVA 0x1660E520 `；selector ` 5 `；EOL ` RVA 0x35FB7630 `。

模式根 ` RVA 0x35FB60F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-35d9d9efc15f3484](../../evidence/conditional_registrations-sets-001.md#r-35d9d9efc15f3484) · [条件 C-454246b4f91aa6b3](../../evidence/conditions-sets-027.md#c-454246b4f91aa6b3) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-15861ff6767dbc6d](../../evidence/state_effects-sets-005.md#s-15861ff6767dbc6d)

### static_slot_creation_candidates-004126

```text
(cfg-if-atm-l2trans-pvp)# default cell-packing <cr>
```

Handler ` RVA 0x1660E520 `；selector ` 1 `；EOL ` RVA 0x35FB7D50 `。

模式根 ` RVA 0x35FB60F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-35d9d9efc15f3484](../../evidence/conditional_registrations-sets-001.md#r-35d9d9efc15f3484) · [条件 C-6ef683cecdff9dba](../../evidence/conditions-sets-043.md#c-6ef683cecdff9dba) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-15861ff6767dbc6d](../../evidence/state_effects-sets-005.md#s-15861ff6767dbc6d)

### static_slot_creation_candidates-004118

```text
(cfg-if-atm-l2trans-pvp)# default epd <cr>
```

Handler ` RVA 0x1660E520 `；selector ` 9 `；EOL ` RVA 0x35FB79C0 `。

模式根 ` RVA 0x35FB60F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-35d9d9efc15f3484](../../evidence/conditional_registrations-sets-001.md#r-35d9d9efc15f3484) · [条件 C-bcfd33491d0dc80a](../../evidence/conditions-sets-073.md#c-bcfd33491d0dc80a) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-15861ff6767dbc6d](../../evidence/state_effects-sets-005.md#s-15861ff6767dbc6d)

### static_slot_creation_candidates-004134

```text
(cfg-if-atm-l2trans-pvp)# default service-policy input <string> <cr>
```

Handler ` RVA 0x1660E520 `；selector ` 2 `；EOL ` RVA 0x35FB8218 `。

模式根 ` RVA 0x35FB60F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Policy-map name。

[候选注册 R-35d9d9efc15f3484](../../evidence/conditional_registrations-sets-001.md#r-35d9d9efc15f3484) · [条件 C-11fe8c4f588e4b71](../../evidence/conditions-sets-007.md#c-11fe8c4f588e4b71) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-e980a6bbdbe90eac](../../evidence/parameters-sets-017.md#p-e980a6bbdbe90eac) · [状态效果 S-6e8b550ed167dcb7](../../evidence/state_effects-sets-023.md#s-6e8b550ed167dcb7)

### static_slot_creation_candidates-004114

```text
(cfg-if-atm-l2trans-pvp)# default ubr <cr>
```

Handler ` RVA 0x1660E520 `；selector ` 3 `；EOL ` RVA 0x35FB6248 `。

模式根 ` RVA 0x35FB60F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-35d9d9efc15f3484](../../evidence/conditional_registrations-sets-001.md#r-35d9d9efc15f3484) · [条件 C-41580ee16ebfbcab](../../evidence/conditions-sets-026.md#c-41580ee16ebfbcab) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-15861ff6767dbc6d](../../evidence/state_effects-sets-005.md#s-15861ff6767dbc6d)

### static_slot_creation_candidates-004117

```text
(cfg-if-atm-l2trans-pvp)# default ubr+ <cr>
```

Handler ` RVA 0x1660E520 `；selector ` 4 `；EOL ` RVA 0x35FB6620 `。

模式根 ` RVA 0x35FB60F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-35d9d9efc15f3484](../../evidence/conditional_registrations-sets-001.md#r-35d9d9efc15f3484) · [条件 C-b69bed8f9a42a1fa](../../evidence/conditions-sets-071.md#c-b69bed8f9a42a1fa) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-15861ff6767dbc6d](../../evidence/state_effects-sets-005.md#s-15861ff6767dbc6d)

### static_slot_creation_candidates-004120

```text
(cfg-if-atm-l2trans-pvp)# default vbr-nrt <cr>
```

Handler ` RVA 0x1660E520 `；selector ` 7 `；EOL ` RVA 0x35FB6A00 `。

模式根 ` RVA 0x35FB60F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-35d9d9efc15f3484](../../evidence/conditional_registrations-sets-001.md#r-35d9d9efc15f3484) · [条件 C-26846ece043bc547](../../evidence/conditions-sets-015.md#c-26846ece043bc547) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-15861ff6767dbc6d](../../evidence/state_effects-sets-005.md#s-15861ff6767dbc6d)

### static_slot_creation_candidates-004123

```text
(cfg-if-atm-l2trans-pvp)# default vbr-rt <cr>
```

Handler ` RVA 0x1660E520 `；selector ` 6 `；EOL ` RVA 0x35FB6E28 `。

模式根 ` RVA 0x35FB60F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-35d9d9efc15f3484](../../evidence/conditional_registrations-sets-001.md#r-35d9d9efc15f3484) · [条件 C-e936d1998f422976](../../evidence/conditions-sets-090.md#c-e936d1998f422976) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-15861ff6767dbc6d](../../evidence/state_effects-sets-005.md#s-15861ff6767dbc6d)

### static_slot_creation_candidates-004128

```text
(cfg-if-atm-l2trans-pvp)# default xconnect <cr>
```

Handler ` RVA 0x1A9E4100 `；selector ` 0 `；EOL ` RVA 0x35FB8590 `。

模式根 ` RVA 0x35FB60F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-35d9d9efc15f3484](../../evidence/conditional_registrations-sets-001.md#r-35d9d9efc15f3484) · [条件 C-5f3cb5c53cbf1fe8](../../evidence/conditions-sets-037.md#c-5f3cb5c53cbf1fe8) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-15861ff6767dbc6d](../../evidence/state_effects-sets-005.md#s-15861ff6767dbc6d)

### static_slot_creation_candidates-004111

```text
(cfg-if-atm-l2trans-pvp)# epd <cr>
```

Handler ` RVA 0x1660E520 `；selector ` 9 `；EOL ` RVA 0x35FB79C0 `。

模式根 ` RVA 0x35FB60F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-35d9d9efc15f3484](../../evidence/conditional_registrations-sets-001.md#r-35d9d9efc15f3484) · [条件 C-c8178ff5feaa7e10](../../evidence/conditions-sets-077.md#c-c8178ff5feaa7e10) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### static_slot_creation_candidates-004124

```text
(cfg-if-atm-l2trans-pvp)# no abr <cr>
```

Handler ` RVA 0x1660E520 `；selector ` 8 `；EOL ` RVA 0x35FB7250 `。

模式根 ` RVA 0x35FB60F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-35d9d9efc15f3484](../../evidence/conditional_registrations-sets-001.md#r-35d9d9efc15f3484) · [条件 C-278f812c55b41939](../../evidence/conditions-sets-016.md#c-278f812c55b41939) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-bb3ceef30dbe412a](../../evidence/state_effects-sets-040.md#s-bb3ceef30dbe412a)

### static_slot_creation_candidates-004129

```text
(cfg-if-atm-l2trans-pvp)# no cbr <cr>
```

Handler ` RVA 0x1660E520 `；selector ` 5 `；EOL ` RVA 0x35FB7630 `。

模式根 ` RVA 0x35FB60F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-35d9d9efc15f3484](../../evidence/conditional_registrations-sets-001.md#r-35d9d9efc15f3484) · [条件 C-b5327b377c55e389](../../evidence/conditions-sets-070.md#c-b5327b377c55e389) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-bb3ceef30dbe412a](../../evidence/state_effects-sets-040.md#s-bb3ceef30dbe412a)

### static_slot_creation_candidates-004122

```text
(cfg-if-atm-l2trans-pvp)# no cell-packing <cr>
```

Handler ` RVA 0x1660E520 `；selector ` 1 `；EOL ` RVA 0x35FB7D50 `。

模式根 ` RVA 0x35FB60F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-35d9d9efc15f3484](../../evidence/conditional_registrations-sets-001.md#r-35d9d9efc15f3484) · [条件 C-585250fb0e176d4e](../../evidence/conditions-sets-035.md#c-585250fb0e176d4e) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-bb3ceef30dbe412a](../../evidence/state_effects-sets-040.md#s-bb3ceef30dbe412a)

### static_slot_creation_candidates-004116

```text
(cfg-if-atm-l2trans-pvp)# no epd <cr>
```

Handler ` RVA 0x1660E520 `；selector ` 9 `；EOL ` RVA 0x35FB79C0 `。

模式根 ` RVA 0x35FB60F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-35d9d9efc15f3484](../../evidence/conditional_registrations-sets-001.md#r-35d9d9efc15f3484) · [条件 C-33ab94ba76e93f66](../../evidence/conditions-sets-020.md#c-33ab94ba76e93f66) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-bb3ceef30dbe412a](../../evidence/state_effects-sets-040.md#s-bb3ceef30dbe412a)

### static_slot_creation_candidates-004133

```text
(cfg-if-atm-l2trans-pvp)# no service-policy input <string> <cr>
```

Handler ` RVA 0x1660E520 `；selector ` 2 `；EOL ` RVA 0x35FB8218 `。

模式根 ` RVA 0x35FB60F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Policy-map name。

[候选注册 R-35d9d9efc15f3484](../../evidence/conditional_registrations-sets-001.md#r-35d9d9efc15f3484) · [条件 C-11fe8c4f588e4b71](../../evidence/conditions-sets-007.md#c-11fe8c4f588e4b71) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-e980a6bbdbe90eac](../../evidence/parameters-sets-017.md#p-e980a6bbdbe90eac) · [状态效果 S-c7ce92c56486accb](../../evidence/state_effects-sets-042.md#s-c7ce92c56486accb)

### static_slot_creation_candidates-004113

```text
(cfg-if-atm-l2trans-pvp)# no ubr <cr>
```

Handler ` RVA 0x1660E520 `；selector ` 3 `；EOL ` RVA 0x35FB6248 `。

模式根 ` RVA 0x35FB60F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-35d9d9efc15f3484](../../evidence/conditional_registrations-sets-001.md#r-35d9d9efc15f3484) · [条件 C-93239501fcd21616](../../evidence/conditions-sets-057.md#c-93239501fcd21616) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-bb3ceef30dbe412a](../../evidence/state_effects-sets-040.md#s-bb3ceef30dbe412a)

### static_slot_creation_candidates-004115

```text
(cfg-if-atm-l2trans-pvp)# no ubr+ <cr>
```

Handler ` RVA 0x1660E520 `；selector ` 4 `；EOL ` RVA 0x35FB6620 `。

模式根 ` RVA 0x35FB60F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-35d9d9efc15f3484](../../evidence/conditional_registrations-sets-001.md#r-35d9d9efc15f3484) · [条件 C-f61956b7834b20ed](../../evidence/conditions-sets-095.md#c-f61956b7834b20ed) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-bb3ceef30dbe412a](../../evidence/state_effects-sets-040.md#s-bb3ceef30dbe412a)

### static_slot_creation_candidates-004119

```text
(cfg-if-atm-l2trans-pvp)# no vbr-nrt <cr>
```

Handler ` RVA 0x1660E520 `；selector ` 7 `；EOL ` RVA 0x35FB6A00 `。

模式根 ` RVA 0x35FB60F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-35d9d9efc15f3484](../../evidence/conditional_registrations-sets-001.md#r-35d9d9efc15f3484) · [条件 C-f8dc625acb481827](../../evidence/conditions-sets-096.md#c-f8dc625acb481827) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-bb3ceef30dbe412a](../../evidence/state_effects-sets-040.md#s-bb3ceef30dbe412a)

### static_slot_creation_candidates-004121

```text
(cfg-if-atm-l2trans-pvp)# no vbr-rt <cr>
```

Handler ` RVA 0x1660E520 `；selector ` 6 `；EOL ` RVA 0x35FB6E28 `。

模式根 ` RVA 0x35FB60F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-35d9d9efc15f3484](../../evidence/conditional_registrations-sets-001.md#r-35d9d9efc15f3484) · [条件 C-bc58b384a663f58a](../../evidence/conditions-sets-073.md#c-bc58b384a663f58a) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-bb3ceef30dbe412a](../../evidence/state_effects-sets-040.md#s-bb3ceef30dbe412a)

### static_slot_creation_candidates-004125

```text
(cfg-if-atm-l2trans-pvp)# no xconnect <cr>
```

Handler ` RVA 0x1A9E4100 `；selector ` 0 `；EOL ` RVA 0x35FB8590 `。

模式根 ` RVA 0x35FB60F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-35d9d9efc15f3484](../../evidence/conditional_registrations-sets-001.md#r-35d9d9efc15f3484) · [条件 C-fe3a0a6b9695478e](../../evidence/conditions-sets-098.md#c-fe3a0a6b9695478e) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-bb3ceef30dbe412a](../../evidence/state_effects-sets-040.md#s-bb3ceef30dbe412a)

### static_slot_creation_candidates-004139

```text
(cfg-if-atm-l2trans-pvp)# pseudowire <address> <number:1..4294967295> encapsulation mpls <cr>
```

Handler ` RVA 0x1A9E4100 `；selector ` 0 `；EOL ` RVA 0x35FB8590 `。

模式根 ` RVA 0x35FB60F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` IP address of peer；` unsigned_number ` Enter VC ID value。

[候选注册 R-35d9d9efc15f3484](../../evidence/conditional_registrations-sets-001.md#r-35d9d9efc15f3484) · [条件 C-fc1fb21c50562b74](../../evidence/conditions-sets-097.md#c-fc1fb21c50562b74) · [缺口 G-f6b8ce36e8f6e414](../../evidence/gaps-sets-008.md#g-f6b8ce36e8f6e414) · [参数 P-2344c0418d39210a](../../evidence/parameters-sets-003.md#p-2344c0418d39210a) · [状态效果 S-0d72790d44a54ea3](../../evidence/state_effects-sets-003.md#s-0d72790d44a54ea3)

### static_slot_creation_candidates-004135

```text
(cfg-if-atm-l2trans-pvp)# pseudowire <address> <number:1..4294967295> pw-class <string> <cr>
```

Handler ` RVA 0x1A9E4100 `；selector ` 0 `；EOL ` RVA 0x35FB8590 `。

模式根 ` RVA 0x35FB60F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP address of peer；` unsigned_number ` Enter VC ID value；` string ` Pseudowire-class name。

[候选注册 R-35d9d9efc15f3484](../../evidence/conditional_registrations-sets-001.md#r-35d9d9efc15f3484) · [条件 C-42ed6e7109ecfa53](../../evidence/conditions-sets-026.md#c-42ed6e7109ecfa53) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-c6d0d405e03ea978](../../evidence/parameters-sets-015.md#p-c6d0d405e03ea978) · [状态效果 S-c3ebe7740a6c487b](../../evidence/state_effects-sets-041.md#s-c3ebe7740a6c487b)

### static_slot_creation_candidates-004131

```text
(cfg-if-atm-l2trans-pvp)# service-policy input <string> <cr>
```

Handler ` RVA 0x1660E520 `；selector ` 2 `；EOL ` RVA 0x35FB8218 `。

模式根 ` RVA 0x35FB60F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Policy-map name。

[候选注册 R-35d9d9efc15f3484](../../evidence/conditional_registrations-sets-001.md#r-35d9d9efc15f3484) · [条件 C-11fe8c4f588e4b71](../../evidence/conditions-sets-007.md#c-11fe8c4f588e4b71) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-e980a6bbdbe90eac](../../evidence/parameters-sets-017.md#p-e980a6bbdbe90eac) · [状态效果 S-858735a260aff7c8](../../evidence/state_effects-sets-028.md#s-858735a260aff7c8)

### static_slot_creation_candidates-004136

```text
(cfg-if-atm-l2trans-pvp)# ubr <number:dynamic> <cr>
```

Handler ` RVA 0x1660E520 `；selector ` 3 `；EOL ` RVA 0x35FB6248 `。

模式根 ` RVA 0x35FB60F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Peak Cell Rate(PCR) in Kbps。

[候选注册 R-35d9d9efc15f3484](../../evidence/conditional_registrations-sets-001.md#r-35d9d9efc15f3484) · [条件 C-ab699d90edf2e60c](../../evidence/conditions-sets-066.md#c-ab699d90edf2e60c) · [缺口 G-e0e9438777407002](../../evidence/gaps-sets-008.md#g-e0e9438777407002) · [参数 P-6993d81e3ee71c0a](../../evidence/parameters-sets-008.md#p-6993d81e3ee71c0a)

### static_slot_creation_candidates-004140

```text
(cfg-if-atm-l2trans-pvp)# ubr+ <number:dynamic> <number:dynamic> <cr>
```

Handler ` RVA 0x1660E520 `；selector ` 4 `；EOL ` RVA 0x35FB6620 `。

模式根 ` RVA 0x35FB60F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Peak Cell Rate(PCR) in Kbps；` unsigned_number_dynamic ` Minimum Guaranteed Cell Rate(MCR) in Kbps。

[候选注册 R-35d9d9efc15f3484](../../evidence/conditional_registrations-sets-001.md#r-35d9d9efc15f3484) · [条件 C-dbd938c62b98754a](../../evidence/conditions-sets-085.md#c-dbd938c62b98754a) · [缺口 G-3340bd220f3f7975](../../evidence/gaps-sets-002.md#g-3340bd220f3f7975) · [参数 P-7c1fe6a6adae96d5](../../evidence/parameters-sets-010.md#p-7c1fe6a6adae96d5)

### static_slot_creation_candidates-004141

```text
(cfg-if-atm-l2trans-pvp)# vbr-nrt <number:dynamic> <number:dynamic> <cr>
```

Handler ` RVA 0x1660E520 `；selector ` 7 `；EOL ` RVA 0x35FB6A00 `。

模式根 ` RVA 0x35FB60F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Peak Cell Rate(PCR) in Kbps；` unsigned_number_dynamic ` Sustainable Cell Rate(SCR) in Kbps。

[候选注册 R-35d9d9efc15f3484](../../evidence/conditional_registrations-sets-001.md#r-35d9d9efc15f3484) · [条件 C-4a965e57354c02ae](../../evidence/conditions-sets-029.md#c-4a965e57354c02ae) · [缺口 G-10c2218bd38ce7f8](../../evidence/gaps-sets-001.md#g-10c2218bd38ce7f8) · [参数 P-42d1c4af541995c8](../../evidence/parameters-sets-006.md#p-42d1c4af541995c8)

### static_slot_creation_candidates-004143

```text
(cfg-if-atm-l2trans-pvp)# vbr-rt <number:dynamic> <number:dynamic> <cr>
```

Handler ` RVA 0x1660E520 `；selector ` 6 `；EOL ` RVA 0x35FB6E28 `。

模式根 ` RVA 0x35FB60F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Peak Cell Rate(PCR) in Kbps；` unsigned_number_dynamic ` Sustainable Cell Rate(SCR) in Kbps。

[候选注册 R-35d9d9efc15f3484](../../evidence/conditional_registrations-sets-001.md#r-35d9d9efc15f3484) · [条件 C-ea196b0af075850e](../../evidence/conditions-sets-090.md#c-ea196b0af075850e) · [缺口 G-a35829a37fa8139a](../../evidence/gaps-sets-006.md#g-a35829a37fa8139a) · [参数 P-5e4d2ca843a81581](../../evidence/parameters-sets-008.md#p-5e4d2ca843a81581)

### static_slot_creation_candidates-004132

```text
(cfg-if-atm-l2trans-pvp)# xconnect vfi <string> <cr>
```

Handler ` RVA 0x1A9E4100 `；selector ` 1 `；EOL ` RVA 0x35FB8698 `。

模式根 ` RVA 0x35FB60F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` VFI name。

[候选注册 R-35d9d9efc15f3484](../../evidence/conditional_registrations-sets-001.md#r-35d9d9efc15f3484) · [条件 C-1048030157c98523](../../evidence/conditions-sets-006.md#c-1048030157c98523) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-f230d2b6efeb38ec](../../evidence/parameters-sets-018.md#p-f230d2b6efeb38ec)

