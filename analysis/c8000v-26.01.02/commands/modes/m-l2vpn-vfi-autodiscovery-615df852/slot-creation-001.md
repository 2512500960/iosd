# l2vpn-vfi-autodiscovery · 依赖静态建槽的条件安装

[模式索引](README.md) · [总索引](../../README.md)

### static_slot_creation_candidates-004328

```text
(config-vfi-autodiscovery)# auto-route-target <cr>
```

Handler ` RVA 0x1AA42B60 `；selector ` 0 `；EOL ` RVA 0x36D53E58 `。

模式根 ` RVA 0x36D4BC70 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-63e12ea590b0e743](../../evidence/conditional_registrations-sets-001.md#r-63e12ea590b0e743) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### static_slot_creation_candidates-004333

```text
(config-vfi-autodiscovery)# control-word include <cr>
```

Handler ` RVA 0x1AA42080 `；selector ` 0 `；EOL ` RVA 0x36D54580 `。

模式根 ` RVA 0x36D4BC70 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-63e12ea590b0e743](../../evidence/conditional_registrations-sets-001.md#r-63e12ea590b0e743) · [条件 C-d0ae2749ef0898a1](../../evidence/conditions-sets-080.md#c-d0ae2749ef0898a1) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-750880b162253b02](../../evidence/state_effects-sets-025.md#s-750880b162253b02)

### static_slot_creation_candidates-004330

```text
(config-vfi-autodiscovery)# default auto-route-target <cr>
```

Handler ` RVA 0x1AA42B60 `；selector ` 0 `；EOL ` RVA 0x36D53E58 `。

模式根 ` RVA 0x36D4BC70 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-63e12ea590b0e743](../../evidence/conditional_registrations-sets-001.md#r-63e12ea590b0e743) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-15dc4cce93da71a8](../../evidence/state_effects-sets-005.md#s-15dc4cce93da71a8)

### static_slot_creation_candidates-004332

```text
(config-vfi-autodiscovery)# default control-word <cr>
```

Handler ` RVA 0x1AA42080 `；selector ` 0 `；EOL ` RVA 0x36D54580 `。

模式根 ` RVA 0x36D4BC70 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-63e12ea590b0e743](../../evidence/conditional_registrations-sets-001.md#r-63e12ea590b0e743) · [条件 C-516c341151625b2d](../../evidence/conditions-sets-032.md#c-516c341151625b2d) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-15dc4cce93da71a8](../../evidence/state_effects-sets-005.md#s-15dc4cce93da71a8)

### static_slot_creation_candidates-004329

```text
(config-vfi-autodiscovery)# no auto-route-target <cr>
```

Handler ` RVA 0x1AA42B60 `；selector ` 0 `；EOL ` RVA 0x36D53E58 `。

模式根 ` RVA 0x36D4BC70 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-63e12ea590b0e743](../../evidence/conditional_registrations-sets-001.md#r-63e12ea590b0e743) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-00206406d073ddbd](../../evidence/state_effects-sets-001.md#s-00206406d073ddbd)

### static_slot_creation_candidates-004331

```text
(config-vfi-autodiscovery)# no control-word <cr>
```

Handler ` RVA 0x1AA42080 `；selector ` 0 `；EOL ` RVA 0x36D54580 `。

模式根 ` RVA 0x36D4BC70 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-63e12ea590b0e743](../../evidence/conditional_registrations-sets-001.md#r-63e12ea590b0e743) · [条件 C-48e411e63435f2d4](../../evidence/conditions-sets-029.md#c-48e411e63435f2d4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-00206406d073ddbd](../../evidence/state_effects-sets-001.md#s-00206406d073ddbd)

### static_slot_creation_candidates-004336

```text
(config-vfi-autodiscovery)# rd <?vrf_rd_action@55558c2a9038> <cr>
```

Handler ` RVA 0x1AA41730 `；selector ` 0 `；EOL ` RVA 0x36D55078 `。

模式根 ` RVA 0x36D4BC70 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[候选注册 R-63e12ea590b0e743](../../evidence/conditional_registrations-sets-001.md#r-63e12ea590b0e743) · [条件 C-eead044137d8bbc4](../../evidence/conditions-sets-092.md#c-eead044137d8bbc4) · [缺口 G-e0467f969816013a](../../evidence/gaps-sets-008.md#g-e0467f969816013a)

### static_slot_creation_candidates-004335

```text
(config-vfi-autodiscovery)# route-target <?bgp_extcomm_action@55558c2a81e8> <cr>
```

Handler ` RVA 0x1AA428C0 `；selector ` 0 `；EOL ` RVA 0x36D54220 `。

模式根 ` RVA 0x36D4BC70 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[候选注册 R-63e12ea590b0e743](../../evidence/conditional_registrations-sets-001.md#r-63e12ea590b0e743) · [缺口 G-5758baeeb4ac5b41](../../evidence/gaps-sets-004.md#g-5758baeeb4ac5b41) · [状态效果 S-b6e2327eefb65e6c](../../evidence/state_effects-sets-039.md#s-b6e2327eefb65e6c)

### static_slot_creation_candidates-004337

```text
(config-vfi-autodiscovery)# ve id <cr>
```

Handler ` RVA 0x1AA41D30 `；selector ` 0 `；EOL ` RVA 0x36D54A68 `。

模式根 ` RVA 0x36D4BC70 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[候选注册 R-63e12ea590b0e743](../../evidence/conditional_registrations-sets-001.md#r-63e12ea590b0e743) · [条件 C-6346c8e5073f1ab9](../../evidence/conditions-sets-038.md#c-6346c8e5073f1ab9) · [缺口 G-0eb0d3f3399b3724](../../evidence/gaps-sets-001.md#g-0eb0d3f3399b3724) · [状态效果 S-24937c6e34bd02f8](../../evidence/state_effects-sets-008.md#s-24937c6e34bd02f8)

### static_slot_creation_candidates-004338

```text
(config-vfi-autodiscovery)# ve range <cr>
```

Handler ` RVA 0x1AA419E0 `；selector ` 0 `；EOL ` RVA 0x36D54D58 `。

模式根 ` RVA 0x36D4BC70 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[候选注册 R-63e12ea590b0e743](../../evidence/conditional_registrations-sets-001.md#r-63e12ea590b0e743) · [条件 C-7e9c0fb927d77489](../../evidence/conditions-sets-049.md#c-7e9c0fb927d77489) · [缺口 G-0eb0d3f3399b3724](../../evidence/gaps-sets-001.md#g-0eb0d3f3399b3724) · [状态效果 S-24937c6e34bd02f8](../../evidence/state_effects-sets-008.md#s-24937c6e34bd02f8)

### static_slot_creation_candidates-004334

```text
(config-vfi-autodiscovery)# vpls-id <?bgp_extcomm_action@55558c2a9388> <cr>
```

Handler ` RVA 0x1AA42370 `；selector ` 0 `；EOL ` RVA 0x36D553C0 `。

模式根 ` RVA 0x36D4BC70 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[候选注册 R-63e12ea590b0e743](../../evidence/conditional_registrations-sets-001.md#r-63e12ea590b0e743) · [条件 C-1b1aeb32e0984fba](../../evidence/conditions-sets-011.md#c-1b1aeb32e0984fba) · [缺口 G-516473c9439c8ad7](../../evidence/gaps-sets-003.md#g-516473c9439c8ad7) · [状态效果 S-6bc069f9b589a33e](../../evidence/state_effects-sets-023.md#s-6bc069f9b589a33e)

