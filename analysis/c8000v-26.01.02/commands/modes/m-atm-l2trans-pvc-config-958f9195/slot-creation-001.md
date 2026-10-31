# atm-l2trans-pvc-config · 依赖静态建槽的条件安装

[模式索引](README.md) · [总索引](../../README.md)

### static_slot_creation_candidates-003591

```text
(cfg-if-atm-l2trans-pvc)# abr <number:dynamic> <number:dynamic> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 8 `；EOL ` RVA 0x35FAB7C0 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Peak Cell Rate(PCR) in Kbps；` unsigned_number_dynamic ` Minimum Cell Rate(MCR) in Kbps。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-d097a8e74994cc1c](../../evidence/conditions-sets-080.md#c-d097a8e74994cc1c) · [缺口 G-69e923554084df4c](../../evidence/gaps-sets-004.md#g-69e923554084df4c) · [参数 P-ff29e180e41eda89](../../evidence/parameters-sets-019.md#p-ff29e180e41eda89)

### static_slot_creation_candidates-003595

```text
(cfg-if-atm-l2trans-pvc)# abr rate-factors <?keyword_option_mm_action@55558b4ffb10> <?keyword_option_mm_action@55558b4ffb60> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 34 `；EOL ` RVA 0x35FABB38 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-16791b77a7874527](../../evidence/conditions-sets-009.md#c-16791b77a7874527) · [缺口 G-c7b8dff5d57d3c0b](../../evidence/gaps-sets-007.md#g-c7b8dff5d57d3c0b)

### static_slot_creation_candidates-003586

```text
(cfg-if-atm-l2trans-pvc)# cbr <number:dynamic> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 7 `；EOL ` RVA 0x35FAC9F0 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Peak Cell Rate in Kbps。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-7baa9978f1ef0b21](../../evidence/conditions-sets-048.md#c-7baa9978f1ef0b21) · [缺口 G-ed41c87385a79a95](../../evidence/gaps-sets-008.md#g-ed41c87385a79a95) · [参数 P-1f506d0245674732](../../evidence/parameters-sets-003.md#p-1f506d0245674732)

### static_slot_creation_candidates-003524

```text
(cfg-if-atm-l2trans-pvc)# cell-packing <cr>
```

Handler ` RVA 0x1660C500 `；selector ` 79 `；EOL ` RVA 0x35FAF5D0 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-c556c01ded43f829](../../evidence/conditions-sets-076.md#c-c556c01ded43f829) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### static_slot_creation_candidates-003588

```text
(cfg-if-atm-l2trans-pvc)# cell-packing <number:dynamic> <cr>
```

Handler ` RVA 0x1660C500 `；selector ` 79 `；EOL ` RVA 0x35FAF5D0 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Maximum number of Cells in a packet。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-25df77305a37150c](../../evidence/conditions-sets-015.md#c-25df77305a37150c) · [缺口 G-1e418baf4c560c21](../../evidence/gaps-sets-002.md#g-1e418baf4c560c21) · [参数 P-2f7c0a0898935e1c](../../evidence/parameters-sets-004.md#p-2f7c0a0898935e1c) · [状态效果 S-11b9c1b22a4529f8](../../evidence/state_effects-sets-004.md#s-11b9c1b22a4529f8)

### static_slot_creation_candidates-003537

```text
(cfg-if-atm-l2trans-pvc)# class-vc <string> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 10 `；EOL ` RVA 0x35FAE140 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` ATM vc-class name to use on this VC。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-feb69d17ce9be303](../../evidence/conditions-sets-098.md#c-feb69d17ce9be303) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-b4eae2a4ffd0b41f](../../evidence/parameters-sets-014.md#p-b4eae2a4ffd0b41f)

### static_slot_creation_candidates-003554

```text
(cfg-if-atm-l2trans-pvc)# default abr rate-factors <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 34 `；EOL ` RVA 0x35FABB38 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-dc52b9461fcaf7ba](../../evidence/conditions-sets-085.md#c-dc52b9461fcaf7ba) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-64a08d06a0d3569b](../../evidence/state_effects-sets-022.md#s-64a08d06a0d3569b)

### static_slot_creation_candidates-003529

```text
(cfg-if-atm-l2trans-pvc)# default cbr <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 7 `；EOL ` RVA 0x35FAC9F0 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-09e849723fc16164](../../evidence/conditions-sets-004.md#c-09e849723fc16164) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-64a08d06a0d3569b](../../evidence/state_effects-sets-022.md#s-64a08d06a0d3569b)

### static_slot_creation_candidates-003545

```text
(cfg-if-atm-l2trans-pvc)# default cell-packing <cr>
```

Handler ` RVA 0x1660C500 `；selector ` 79 `；EOL ` RVA 0x35FAF5D0 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-e92b0e624adb37a4](../../evidence/conditions-sets-090.md#c-e92b0e624adb37a4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-64a08d06a0d3569b](../../evidence/state_effects-sets-022.md#s-64a08d06a0d3569b)

### static_slot_creation_candidates-003556

```text
(cfg-if-atm-l2trans-pvc)# default class-vc <string> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 10 `；EOL ` RVA 0x35FAE140 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` ATM vc-class name to use on this VC。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-feb69d17ce9be303](../../evidence/conditions-sets-098.md#c-feb69d17ce9be303) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-b4eae2a4ffd0b41f](../../evidence/parameters-sets-014.md#p-b4eae2a4ffd0b41f) · [状态效果 S-64a08d06a0d3569b](../../evidence/state_effects-sets-022.md#s-64a08d06a0d3569b)

### static_slot_creation_candidates-003540

```text
(cfg-if-atm-l2trans-pvc)# default encapsulation <cr>
```

Handler ` RVA 0x1660C500 `；selector ` 12 `；EOL ` RVA 0x35FAE8A0 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-cd5346b9b3e2e8cd](../../evidence/conditions-sets-079.md#c-cd5346b9b3e2e8cd) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-64a08d06a0d3569b](../../evidence/state_effects-sets-022.md#s-64a08d06a0d3569b)

### static_slot_creation_candidates-003538

```text
(cfg-if-atm-l2trans-pvc)# default epd <cr>
```

Handler ` RVA 0x1660C500 `；selector ` 91 `；EOL ` RVA 0x35FADE18 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-7cb42421f8d9959d](../../evidence/conditions-sets-048.md#c-7cb42421f8d9959d) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-64a08d06a0d3569b](../../evidence/state_effects-sets-022.md#s-64a08d06a0d3569b)

### static_slot_creation_candidates-003567

```text
(cfg-if-atm-l2trans-pvc)# default mpls l2transport route <cr>
```

Handler ` RVA 0x1660C500 `；selector ` 70 `；EOL ` RVA 0x35FADA20 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-01a371f9c3809e72](../../evidence/conditions-sets-001.md#c-01a371f9c3809e72) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-64a08d06a0d3569b](../../evidence/state_effects-sets-022.md#s-64a08d06a0d3569b)

### static_slot_creation_candidates-003563

```text
(cfg-if-atm-l2trans-pvc)# default oam ais-rdi <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 23 `；EOL ` RVA 0x35FB1C10 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-8c2aac2dbdf05bd1](../../evidence/conditions-sets-054.md#c-8c2aac2dbdf05bd1) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-d352a274954d6432](../../evidence/state_effects-sets-045.md#s-d352a274954d6432)

### static_slot_creation_candidates-003565

```text
(cfg-if-atm-l2trans-pvc)# default oam retry <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 20 `；EOL ` RVA 0x35FB17D8 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-a82740f5da13a6a8](../../evidence/conditions-sets-065.md#c-a82740f5da13a6a8) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-99c97de037756080](../../evidence/state_effects-sets-033.md#s-99c97de037756080)

### static_slot_creation_candidates-003582

```text
(cfg-if-atm-l2trans-pvc)# default oam retry cc end <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 21 `；EOL ` RVA 0x35FB1370 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-de70d81489d82bd4](../../evidence/conditions-sets-086.md#c-de70d81489d82bd4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-2bc168b9b0fb8992](../../evidence/state_effects-sets-010.md#s-2bc168b9b0fb8992)

### static_slot_creation_candidates-003579

```text
(cfg-if-atm-l2trans-pvc)# default oam retry cc segment <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 22 `；EOL ` RVA 0x35FB0F38 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-de70d81489d82bd4](../../evidence/conditions-sets-086.md#c-de70d81489d82bd4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-fa0367c9730ccf31](../../evidence/state_effects-sets-053.md#s-fa0367c9730ccf31)

### static_slot_creation_candidates-003559

```text
(cfg-if-atm-l2trans-pvc)# default oam-ac emulation-enable <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 80 `；EOL ` RVA 0x35FAEEE0 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-15feac237b9d42e6](../../evidence/conditions-sets-009.md#c-15feac237b9d42e6) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-5614d97f567c6778](../../evidence/state_effects-sets-019.md#s-5614d97f567c6778)

### static_slot_creation_candidates-003571

```text
(cfg-if-atm-l2trans-pvc)# default oam-ac segment endpoint <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 81 `；EOL ` RVA 0x35FAF228 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-697b91cac20087da](../../evidence/conditions-sets-041.md#c-697b91cac20087da) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-913a1e9fb9d96fbd](../../evidence/state_effects-sets-031.md#s-913a1e9fb9d96fbd)

### static_slot_creation_candidates-003550

```text
(cfg-if-atm-l2trans-pvc)# default oam-pvc <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 16 `；EOL ` RVA 0x35FB2F40 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-faed6814f6cd9719](../../evidence/conditions-sets-097.md#c-faed6814f6cd9719) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-a78536469961778a](../../evidence/state_effects-sets-035.md#s-a78536469961778a)

### static_slot_creation_candidates-003585

```text
(cfg-if-atm-l2trans-pvc)# default oam-pvc manage cc end <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 17 `；EOL ` RVA 0x35FB27D0 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-b97dc354eb725ecf](../../evidence/conditions-sets-072.md#c-b97dc354eb725ecf) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9405c128997208f1](../../evidence/state_effects-sets-031.md#s-9405c128997208f1)

### static_slot_creation_candidates-003583

```text
(cfg-if-atm-l2trans-pvc)# default oam-pvc manage cc segment <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 18 `；EOL ` RVA 0x35FB2158 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-98945c5e4c73a861](../../evidence/conditions-sets-059.md#c-98945c5e4c73a861) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-32249932c4d927b7](../../evidence/state_effects-sets-011.md#s-32249932c4d927b7)

### static_slot_creation_candidates-003569

```text
(cfg-if-atm-l2trans-pvc)# default service-policy input <string> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 37 `；EOL ` RVA 0x35FAE520 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Policy-map name。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-351aaa575c6a23ea](../../evidence/conditions-sets-021.md#c-351aaa575c6a23ea) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-35f0357ba5c82a0f](../../evidence/parameters-sets-005.md#p-35f0357ba5c82a0f) · [状态效果 S-9ea3f267d0a9f880](../../evidence/state_effects-sets-034.md#s-9ea3f267d0a9f880)

### static_slot_creation_candidates-003548

```text
(cfg-if-atm-l2trans-pvc)# default tx-limit <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 90 `；EOL ` RVA 0x35FB0938 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-9ce5f1a1185eaca5](../../evidence/conditions-sets-061.md#c-9ce5f1a1185eaca5) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-64a08d06a0d3569b](../../evidence/state_effects-sets-022.md#s-64a08d06a0d3569b)

### static_slot_creation_candidates-003534

```text
(cfg-if-atm-l2trans-pvc)# default ubr <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 3 `；EOL ` RVA 0x35FAD300 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-1c4fcbd59772ee49](../../evidence/conditions-sets-011.md#c-1c4fcbd59772ee49) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-64a08d06a0d3569b](../../evidence/state_effects-sets-022.md#s-64a08d06a0d3569b)

### static_slot_creation_candidates-003531

```text
(cfg-if-atm-l2trans-pvc)# default ubr+ <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 4 `；EOL ` RVA 0x35FACE50 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-813504adf84acfef](../../evidence/conditions-sets-050.md#c-813504adf84acfef) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-64a08d06a0d3569b](../../evidence/state_effects-sets-022.md#s-64a08d06a0d3569b)

### static_slot_creation_candidates-003535

```text
(cfg-if-atm-l2trans-pvc)# default vbr-nrt <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 5 `；EOL ` RVA 0x35FAC458 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-b6c3038da65430fc](../../evidence/conditions-sets-071.md#c-b6c3038da65430fc) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-64a08d06a0d3569b](../../evidence/state_effects-sets-022.md#s-64a08d06a0d3569b)

### static_slot_creation_candidates-003527

```text
(cfg-if-atm-l2trans-pvc)# default vbr-rt <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 6 `；EOL ` RVA 0x35FAC250 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-e294b5052a7b7800](../../evidence/conditions-sets-087.md#c-e294b5052a7b7800) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-64a08d06a0d3569b](../../evidence/state_effects-sets-022.md#s-64a08d06a0d3569b)

### static_slot_creation_candidates-003544

```text
(cfg-if-atm-l2trans-pvc)# default xconnect <cr>
```

Handler ` RVA 0x1A9E4100 `；selector ` 0 `；EOL ` RVA 0x35FAFA10 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-f7a05da8bbcf44a8](../../evidence/conditions-sets-096.md#c-f7a05da8bbcf44a8) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-64a08d06a0d3569b](../../evidence/state_effects-sets-022.md#s-64a08d06a0d3569b)

### static_slot_creation_candidates-003541

```text
(cfg-if-atm-l2trans-pvc)# encapsulation aal5 <cr>
```

Handler ` RVA 0x1660C500 `；selector ` 12 `；EOL ` RVA 0x35FAE8A0 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-61b08d6a7f8b2903](../../evidence/conditions-sets-038.md#c-61b08d6a7f8b2903) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-1f6720c8694f330b](../../evidence/state_effects-sets-007.md#s-1f6720c8694f330b)

### static_slot_creation_candidates-003523

```text
(cfg-if-atm-l2trans-pvc)# epd <cr>
```

Handler ` RVA 0x1660C500 `；selector ` 91 `；EOL ` RVA 0x35FADE18 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-39a92d3a9382f679](../../evidence/conditions-sets-022.md#c-39a92d3a9382f679) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### static_slot_creation_candidates-003576

```text
(cfg-if-atm-l2trans-pvc)# mpls l2transport route <address> <number:1..4294967295> <cr>
```

Handler ` RVA 0x1660C500 `；selector ` 70 `；EOL ` RVA 0x35FADA20 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP address of Peer；` unsigned_number ` Enter VC ID value。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-7e990336d27075bb](../../evidence/conditions-sets-049.md#c-7e990336d27075bb) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-fe7f8aaa57b7f090](../../evidence/parameters-sets-019.md#p-fe7f8aaa57b7f090)

### static_slot_creation_candidates-003553

```text
(cfg-if-atm-l2trans-pvc)# no abr rate-factors <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 34 `；EOL ` RVA 0x35FABB38 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-f9f44f9e1616f80c](../../evidence/conditions-sets-097.md#c-f9f44f9e1616f80c) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-bab78880c5dfb4b9](../../evidence/state_effects-sets-039.md#s-bab78880c5dfb4b9)

### static_slot_creation_candidates-003528

```text
(cfg-if-atm-l2trans-pvc)# no cbr <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 7 `；EOL ` RVA 0x35FAC9F0 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-3412d2b00e01d7d2](../../evidence/conditions-sets-020.md#c-3412d2b00e01d7d2) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-bab78880c5dfb4b9](../../evidence/state_effects-sets-039.md#s-bab78880c5dfb4b9)

### static_slot_creation_candidates-003543

```text
(cfg-if-atm-l2trans-pvc)# no cell-packing <cr>
```

Handler ` RVA 0x1660C500 `；selector ` 79 `；EOL ` RVA 0x35FAF5D0 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-d0e225758aaaa8bd](../../evidence/conditions-sets-080.md#c-d0e225758aaaa8bd) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-bab78880c5dfb4b9](../../evidence/state_effects-sets-039.md#s-bab78880c5dfb4b9)

### static_slot_creation_candidates-003555

```text
(cfg-if-atm-l2trans-pvc)# no class-vc <string> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 10 `；EOL ` RVA 0x35FAE140 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` ATM vc-class name to use on this VC。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-feb69d17ce9be303](../../evidence/conditions-sets-098.md#c-feb69d17ce9be303) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-b4eae2a4ffd0b41f](../../evidence/parameters-sets-014.md#p-b4eae2a4ffd0b41f) · [状态效果 S-bab78880c5dfb4b9](../../evidence/state_effects-sets-039.md#s-bab78880c5dfb4b9)

### static_slot_creation_candidates-003539

```text
(cfg-if-atm-l2trans-pvc)# no encapsulation <cr>
```

Handler ` RVA 0x1660C500 `；selector ` 12 `；EOL ` RVA 0x35FAE8A0 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-457c7069e416a7fa](../../evidence/conditions-sets-027.md#c-457c7069e416a7fa) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-bab78880c5dfb4b9](../../evidence/state_effects-sets-039.md#s-bab78880c5dfb4b9)

### static_slot_creation_candidates-003536

```text
(cfg-if-atm-l2trans-pvc)# no epd <cr>
```

Handler ` RVA 0x1660C500 `；selector ` 91 `；EOL ` RVA 0x35FADE18 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-acb5ee18f2e619e1](../../evidence/conditions-sets-067.md#c-acb5ee18f2e619e1) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-bab78880c5dfb4b9](../../evidence/state_effects-sets-039.md#s-bab78880c5dfb4b9)

### static_slot_creation_candidates-003566

```text
(cfg-if-atm-l2trans-pvc)# no mpls l2transport route <cr>
```

Handler ` RVA 0x1660C500 `；selector ` 70 `；EOL ` RVA 0x35FADA20 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-4e1fa1074d840626](../../evidence/conditions-sets-031.md#c-4e1fa1074d840626) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-bab78880c5dfb4b9](../../evidence/state_effects-sets-039.md#s-bab78880c5dfb4b9)

### static_slot_creation_candidates-003562

```text
(cfg-if-atm-l2trans-pvc)# no oam ais-rdi <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 23 `；EOL ` RVA 0x35FB1C10 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-64cd3fa7d58a5d1c](../../evidence/conditions-sets-039.md#c-64cd3fa7d58a5d1c) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-6e3ddbb5c6895e37](../../evidence/state_effects-sets-023.md#s-6e3ddbb5c6895e37)

### static_slot_creation_candidates-003564

```text
(cfg-if-atm-l2trans-pvc)# no oam retry <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 20 `；EOL ` RVA 0x35FB17D8 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-a9212029b0d44c99](../../evidence/conditions-sets-065.md#c-a9212029b0d44c99) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-327374f2ccaf7b09](../../evidence/state_effects-sets-011.md#s-327374f2ccaf7b09)

### static_slot_creation_candidates-003580

```text
(cfg-if-atm-l2trans-pvc)# no oam retry cc end <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 21 `；EOL ` RVA 0x35FB1370 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-de70d81489d82bd4](../../evidence/conditions-sets-086.md#c-de70d81489d82bd4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-13266b3af18f9272](../../evidence/state_effects-sets-004.md#s-13266b3af18f9272)

### static_slot_creation_candidates-003578

```text
(cfg-if-atm-l2trans-pvc)# no oam retry cc segment <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 22 `；EOL ` RVA 0x35FB0F38 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-de70d81489d82bd4](../../evidence/conditions-sets-086.md#c-de70d81489d82bd4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-3411893979a95fc4](../../evidence/state_effects-sets-012.md#s-3411893979a95fc4)

### static_slot_creation_candidates-003558

```text
(cfg-if-atm-l2trans-pvc)# no oam-ac emulation-enable <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 80 `；EOL ` RVA 0x35FAEEE0 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-1db5ceee7c260f3e](../../evidence/conditions-sets-012.md#c-1db5ceee7c260f3e) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-18ce06915cf27c70](../../evidence/state_effects-sets-006.md#s-18ce06915cf27c70)

### static_slot_creation_candidates-003570

```text
(cfg-if-atm-l2trans-pvc)# no oam-ac segment endpoint <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 81 `；EOL ` RVA 0x35FAF228 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-697b91cac20087da](../../evidence/conditions-sets-041.md#c-697b91cac20087da) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-661bf5be5989d172](../../evidence/state_effects-sets-022.md#s-661bf5be5989d172)

### static_slot_creation_candidates-003549

```text
(cfg-if-atm-l2trans-pvc)# no oam-pvc <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 16 `；EOL ` RVA 0x35FB2F40 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-faed6814f6cd9719](../../evidence/conditions-sets-097.md#c-faed6814f6cd9719) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9becaf1e45e86049](../../evidence/state_effects-sets-033.md#s-9becaf1e45e86049)

### static_slot_creation_candidates-003584

```text
(cfg-if-atm-l2trans-pvc)# no oam-pvc manage cc end <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 17 `；EOL ` RVA 0x35FB27D0 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-b97dc354eb725ecf](../../evidence/conditions-sets-072.md#c-b97dc354eb725ecf) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-3e9215e2fc67a5aa](../../evidence/state_effects-sets-014.md#s-3e9215e2fc67a5aa)

### static_slot_creation_candidates-003581

```text
(cfg-if-atm-l2trans-pvc)# no oam-pvc manage cc segment <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 18 `；EOL ` RVA 0x35FB2158 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-98945c5e4c73a861](../../evidence/conditions-sets-059.md#c-98945c5e4c73a861) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-4a6b20616c715b92](../../evidence/state_effects-sets-016.md#s-4a6b20616c715b92)

### static_slot_creation_candidates-003568

```text
(cfg-if-atm-l2trans-pvc)# no service-policy input <string> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 37 `；EOL ` RVA 0x35FAE520 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Policy-map name。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-351aaa575c6a23ea](../../evidence/conditions-sets-021.md#c-351aaa575c6a23ea) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-35f0357ba5c82a0f](../../evidence/parameters-sets-005.md#p-35f0357ba5c82a0f) · [状态效果 S-44cdd77817297846](../../evidence/state_effects-sets-015.md#s-44cdd77817297846)

### static_slot_creation_candidates-003547

```text
(cfg-if-atm-l2trans-pvc)# no tx-limit <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 90 `；EOL ` RVA 0x35FB0938 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-d12074a22f64a928](../../evidence/conditions-sets-081.md#c-d12074a22f64a928) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-bab78880c5dfb4b9](../../evidence/state_effects-sets-039.md#s-bab78880c5dfb4b9)

### static_slot_creation_candidates-003532

```text
(cfg-if-atm-l2trans-pvc)# no ubr <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 3 `；EOL ` RVA 0x35FAD300 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-e42530c6b0b9b1c0](../../evidence/conditions-sets-088.md#c-e42530c6b0b9b1c0) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-bab78880c5dfb4b9](../../evidence/state_effects-sets-039.md#s-bab78880c5dfb4b9)

### static_slot_creation_candidates-003530

```text
(cfg-if-atm-l2trans-pvc)# no ubr+ <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 4 `；EOL ` RVA 0x35FACE50 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-6b70837954bf18ef](../../evidence/conditions-sets-042.md#c-6b70837954bf18ef) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-bab78880c5dfb4b9](../../evidence/state_effects-sets-039.md#s-bab78880c5dfb4b9)

### static_slot_creation_candidates-003533

```text
(cfg-if-atm-l2trans-pvc)# no vbr-nrt <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 5 `；EOL ` RVA 0x35FAC458 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-61c82e3187b106a9](../../evidence/conditions-sets-038.md#c-61c82e3187b106a9) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-bab78880c5dfb4b9](../../evidence/state_effects-sets-039.md#s-bab78880c5dfb4b9)

### static_slot_creation_candidates-003526

```text
(cfg-if-atm-l2trans-pvc)# no vbr-rt <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 6 `；EOL ` RVA 0x35FAC250 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-6712041e0796d36d](../../evidence/conditions-sets-040.md#c-6712041e0796d36d) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-bab78880c5dfb4b9](../../evidence/state_effects-sets-039.md#s-bab78880c5dfb4b9)

### static_slot_creation_candidates-003542

```text
(cfg-if-atm-l2trans-pvc)# no xconnect <cr>
```

Handler ` RVA 0x1A9E4100 `；selector ` 0 `；EOL ` RVA 0x35FAFA10 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-d1e2fc73bb6a2b85](../../evidence/conditions-sets-081.md#c-d1e2fc73bb6a2b85) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-bab78880c5dfb4b9](../../evidence/state_effects-sets-039.md#s-bab78880c5dfb4b9)

### static_slot_creation_candidates-003551

```text
(cfg-if-atm-l2trans-pvc)# oam ais-rdi <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 23 `；EOL ` RVA 0x35FB1C10 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-d4c5297b5c2b224e](../../evidence/conditions-sets-082.md#c-d4c5297b5c2b224e) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-ca4a82398f4e9ffb](../../evidence/state_effects-sets-043.md#s-ca4a82398f4e9ffb)

### static_slot_creation_candidates-003552

```text
(cfg-if-atm-l2trans-pvc)# oam retry <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 20 `；EOL ` RVA 0x35FB17D8 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-f7d82b8cd43393ea](../../evidence/conditions-sets-096.md#c-f7d82b8cd43393ea) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-8e60437bcd28bc83](../../evidence/state_effects-sets-030.md#s-8e60437bcd28bc83)

### static_slot_creation_candidates-003573

```text
(cfg-if-atm-l2trans-pvc)# oam retry cc end <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 21 `；EOL ` RVA 0x35FB1370 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-de70d81489d82bd4](../../evidence/conditions-sets-086.md#c-de70d81489d82bd4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-88fa05a34a21726d](../../evidence/state_effects-sets-029.md#s-88fa05a34a21726d)

### static_slot_creation_candidates-003572

```text
(cfg-if-atm-l2trans-pvc)# oam retry cc segment <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 22 `；EOL ` RVA 0x35FB0F38 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-de70d81489d82bd4](../../evidence/conditions-sets-086.md#c-de70d81489d82bd4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-68eab5f278388e79](../../evidence/state_effects-sets-022.md#s-68eab5f278388e79)

### static_slot_creation_candidates-003546

```text
(cfg-if-atm-l2trans-pvc)# oam-ac emulation-enable <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 80 `；EOL ` RVA 0x35FAEEE0 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-14ecc30ae6b1dccb](../../evidence/conditions-sets-008.md#c-14ecc30ae6b1dccb) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-2f56f9645dccb168](../../evidence/state_effects-sets-010.md#s-2f56f9645dccb168)

### static_slot_creation_candidates-003560

```text
(cfg-if-atm-l2trans-pvc)# oam-ac segment endpoint <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 81 `；EOL ` RVA 0x35FAF228 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-697b91cac20087da](../../evidence/conditions-sets-041.md#c-697b91cac20087da) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-e91c6b6e3122038f](../../evidence/state_effects-sets-049.md#s-e91c6b6e3122038f)

### static_slot_creation_candidates-003525

```text
(cfg-if-atm-l2trans-pvc)# oam-pvc <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 16 `；EOL ` RVA 0x35FB2F40 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-faed6814f6cd9719](../../evidence/conditions-sets-097.md#c-faed6814f6cd9719) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-aa9ff1bf0f9bcf8c](../../evidence/state_effects-sets-036.md#s-aa9ff1bf0f9bcf8c)

### static_slot_creation_candidates-003575

```text
(cfg-if-atm-l2trans-pvc)# oam-pvc manage cc end <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 17 `；EOL ` RVA 0x35FB27D0 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-b97dc354eb725ecf](../../evidence/conditions-sets-072.md#c-b97dc354eb725ecf) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-54b82ec06dd0b503](../../evidence/state_effects-sets-018.md#s-54b82ec06dd0b503)

### static_slot_creation_candidates-003574

```text
(cfg-if-atm-l2trans-pvc)# oam-pvc manage cc segment <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 18 `；EOL ` RVA 0x35FB2158 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-98945c5e4c73a861](../../evidence/conditions-sets-059.md#c-98945c5e4c73a861) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-fac7158a64415c48](../../evidence/state_effects-sets-053.md#s-fac7158a64415c48)

### static_slot_creation_candidates-003590

```text
(cfg-if-atm-l2trans-pvc)# pseudowire <address> <number:1..4294967295> encapsulation mpls <cr>
```

Handler ` RVA 0x1A9E4100 `；selector ` 0 `；EOL ` RVA 0x35FAFA10 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` IP address of peer；` unsigned_number ` Enter VC ID value。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-f3d15c0bd7449141](../../evidence/conditions-sets-094.md#c-f3d15c0bd7449141) · [缺口 G-0ac79cfff8079e14](../../evidence/gaps-sets-001.md#g-0ac79cfff8079e14) · [参数 P-7520e3e1ee3336a8](../../evidence/parameters-sets-009.md#p-7520e3e1ee3336a8) · [状态效果 S-ea2cd2e5accf7cf5](../../evidence/state_effects-sets-050.md#s-ea2cd2e5accf7cf5)

### static_slot_creation_candidates-003577

```text
(cfg-if-atm-l2trans-pvc)# pseudowire <address> <number:1..4294967295> pw-class <string> <cr>
```

Handler ` RVA 0x1A9E4100 `；selector ` 0 `；EOL ` RVA 0x35FAFA10 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP address of peer；` unsigned_number ` Enter VC ID value；` string ` Pseudowire-class name。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-d0850480f93b9895](../../evidence/conditions-sets-080.md#c-d0850480f93b9895) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-5cd228ab233b647c](../../evidence/parameters-sets-007.md#p-5cd228ab233b647c) · [状态效果 S-8255fb174c6c0683](../../evidence/state_effects-sets-028.md#s-8255fb174c6c0683)

### static_slot_creation_candidates-003557

```text
(cfg-if-atm-l2trans-pvc)# service-policy input <string> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 37 `；EOL ` RVA 0x35FAE520 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Policy-map name。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-351aaa575c6a23ea](../../evidence/conditions-sets-021.md#c-351aaa575c6a23ea) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-35f0357ba5c82a0f](../../evidence/parameters-sets-005.md#p-35f0357ba5c82a0f) · [状态效果 S-85e9134a314853d9](../../evidence/state_effects-sets-028.md#s-85e9134a314853d9)

### static_slot_creation_candidates-003589

```text
(cfg-if-atm-l2trans-pvc)# tx-limit <number:dynamic> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 90 `；EOL ` RVA 0x35FB0938 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Number of tx buffers for this VC。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-5b79533c0835da2e](../../evidence/conditions-sets-036.md#c-5b79533c0835da2e) · [缺口 G-aac63c4fb9c0dcdd](../../evidence/gaps-sets-006.md#g-aac63c4fb9c0dcdd) · [参数 P-87adf9237d914ac7](../../evidence/parameters-sets-010.md#p-87adf9237d914ac7)

### static_slot_creation_candidates-003522

```text
(cfg-if-atm-l2trans-pvc)# ubr <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 3 `；EOL ` RVA 0x35FAD300 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-0249aaee8b68be3b](../../evidence/conditions-sets-001.md#c-0249aaee8b68be3b) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### static_slot_creation_candidates-003587

```text
(cfg-if-atm-l2trans-pvc)# ubr <number:dynamic> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 3 `；EOL ` RVA 0x35FAD300 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Peak Cell Rate (PCR) in Kbps。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-2b20fc010e09fe02](../../evidence/conditions-sets-017.md#c-2b20fc010e09fe02) · [缺口 G-3e9ac5e806ef7f8c](../../evidence/gaps-sets-003.md#g-3e9ac5e806ef7f8c) · [参数 P-9b6f2415f88e7ed0](../../evidence/parameters-sets-012.md#p-9b6f2415f88e7ed0)

### static_slot_creation_candidates-003593

```text
(cfg-if-atm-l2trans-pvc)# ubr+ <number:dynamic> <number:dynamic> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 4 `；EOL ` RVA 0x35FACE50 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Peak Cell Rate(PCR) in Kbps；` unsigned_number_dynamic ` Minimum Guaranteed Cell Rate(MCR) in Kbps。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-d98ca3a63e26b889](../../evidence/conditions-sets-084.md#c-d98ca3a63e26b889) · [缺口 G-52aed21262e64900](../../evidence/gaps-sets-003.md#g-52aed21262e64900) · [参数 P-38d19ba98000d447](../../evidence/parameters-sets-005.md#p-38d19ba98000d447)

### static_slot_creation_candidates-003594

```text
(cfg-if-atm-l2trans-pvc)# vbr-nrt <number:dynamic> <number:dynamic> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 5 `；EOL ` RVA 0x35FAC458 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Peak Cell Rate(PCR) in Kbps；` unsigned_number_dynamic ` Sustainable Cell Rate(SCR) in Kbps。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-5094c97a24699ee2](../../evidence/conditions-sets-031.md#c-5094c97a24699ee2) · [缺口 G-1161ba6a46b676e1](../../evidence/gaps-sets-001.md#g-1161ba6a46b676e1) · [参数 P-91799771e79aa237](../../evidence/parameters-sets-011.md#p-91799771e79aa237)

### static_slot_creation_candidates-003592

```text
(cfg-if-atm-l2trans-pvc)# vbr-rt <number:dynamic> <number:dynamic> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 6 `；EOL ` RVA 0x35FAC250 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Peak Cell Rate(PCR) in Kbps；` unsigned_number_dynamic ` Average Cell Rate in Kbps。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-7ffcc7a188938637](../../evidence/conditions-sets-050.md#c-7ffcc7a188938637) · [缺口 G-b16608ad03d90f0d](../../evidence/gaps-sets-006.md#g-b16608ad03d90f0d) · [参数 P-225d177959742928](../../evidence/parameters-sets-003.md#p-225d177959742928)

### static_slot_creation_candidates-003561

```text
(cfg-if-atm-l2trans-pvc)# xconnect vfi <string> <cr>
```

Handler ` RVA 0x1A9E4100 `；selector ` 1 `；EOL ` RVA 0x35FAFB18 `。

模式根 ` RVA 0x35FAB5E8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` VFI name。

[候选注册 R-cbcca096c2808632](../../evidence/conditional_registrations-sets-002.md#r-cbcca096c2808632) · [条件 C-9ace82b635eaf9f9](../../evidence/conditions-sets-060.md#c-9ace82b635eaf9f9) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-de9400a6e30b869a](../../evidence/parameters-sets-017.md#p-de9400a6e30b869a)
