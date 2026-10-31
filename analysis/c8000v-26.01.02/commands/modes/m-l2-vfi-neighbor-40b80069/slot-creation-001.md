# l2-vfi-neighbor · 依赖静态建槽的条件安装

[模式索引](README.md) · [总索引](../../README.md)

### static_slot_creation_candidates-004527

```text
(config-vfi-neighbor)# default local interface <number:1..4097> <cr>
```

Handler ` RVA 0x1AA4A080 `；selector ` 15 `；EOL ` RVA 0x36D5A858 `。

模式根 ` RVA 0x36D59FC8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-5b89493e4a0a5e7b](../../evidence/conditional_registrations-sets-001.md#r-5b89493e4a0a5e7b) · [条件 C-a496b8928128ac7d](../../evidence/conditions-sets-063.md#c-a496b8928128ac7d) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-10054a2f3c7a22ea](../../evidence/parameters-sets-002.md#p-10054a2f3c7a22ea) · [状态效果 S-380c5240a808ddb0](../../evidence/state_effects-sets-012.md#s-380c5240a808ddb0)

### static_slot_creation_candidates-004525

```text
(config-vfi-neighbor)# default mpls control-word <cr>
```

Handler ` RVA 0x1AA05AC0 `；selector ` 6 `；EOL ` RVA 0x36D5A4C8 `。

模式根 ` RVA 0x36D59FC8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-44de6186c8774ee9](../../evidence/conditional_registrations-sets-001.md#r-44de6186c8774ee9) · [条件 C-073122115cae37c4](../../evidence/conditions-sets-003.md#c-073122115cae37c4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-380c5240a808ddb0](../../evidence/state_effects-sets-012.md#s-380c5240a808ddb0)

### static_slot_creation_candidates-004524

```text
(config-vfi-neighbor)# default mpls label <cr>
```

Handler ` RVA 0x1AA05AC0 `；selector ` 5 `；EOL ` RVA 0x36D5A1B8 `。

模式根 ` RVA 0x36D59FC8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-44de6186c8774ee9](../../evidence/conditional_registrations-sets-001.md#r-44de6186c8774ee9) · [条件 C-fc87ec6d7110d48d](../../evidence/conditions-sets-097.md#c-fc87ec6d7110d48d) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-380c5240a808ddb0](../../evidence/state_effects-sets-012.md#s-380c5240a808ddb0)

### static_slot_creation_candidates-004521

```text
(config-vfi-neighbor)# local interface <number:1..4097> <cr>
```

Handler ` RVA 0x1AA4A080 `；selector ` 15 `；EOL ` RVA 0x36D5A858 `。

模式根 ` RVA 0x36D59FC8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-5b89493e4a0a5e7b](../../evidence/conditional_registrations-sets-001.md#r-5b89493e4a0a5e7b) · [条件 C-a496b8928128ac7d](../../evidence/conditions-sets-063.md#c-a496b8928128ac7d) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-10054a2f3c7a22ea](../../evidence/parameters-sets-002.md#p-10054a2f3c7a22ea)

### static_slot_creation_candidates-004520

```text
(config-vfi-neighbor)# mpls control-word <cr>
```

Handler ` RVA 0x1AA05AC0 `；selector ` 6 `；EOL ` RVA 0x36D5A4C8 `。

模式根 ` RVA 0x36D59FC8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-44de6186c8774ee9](../../evidence/conditional_registrations-sets-001.md#r-44de6186c8774ee9) · [条件 C-073122115cae37c4](../../evidence/conditions-sets-003.md#c-073122115cae37c4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### static_slot_creation_candidates-004528

```text
(config-vfi-neighbor)# mpls label <number:dynamic> <number:16..1048575> <cr>
```

Handler ` RVA 0x1AA05AC0 `；selector ` 5 `；EOL ` RVA 0x36D5A1B8 `。

模式根 ` RVA 0x36D59FC8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Local pseudowire label；` unsigned_number ` Remote pseudowire label。

[候选注册 R-44de6186c8774ee9](../../evidence/conditional_registrations-sets-001.md#r-44de6186c8774ee9) · [条件 C-0703c50d61cdd074](../../evidence/conditions-sets-003.md#c-0703c50d61cdd074) · [缺口 G-2f8eb5c6ad81acca](../../evidence/gaps-sets-002.md#g-2f8eb5c6ad81acca) · [参数 P-3b6bc9806581be5f](../../evidence/parameters-sets-005.md#p-3b6bc9806581be5f)

### static_slot_creation_candidates-004526

```text
(config-vfi-neighbor)# no local interface <number:1..4097> <cr>
```

Handler ` RVA 0x1AA4A080 `；selector ` 15 `；EOL ` RVA 0x36D5A858 `。

模式根 ` RVA 0x36D59FC8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-5b89493e4a0a5e7b](../../evidence/conditional_registrations-sets-001.md#r-5b89493e4a0a5e7b) · [条件 C-a496b8928128ac7d](../../evidence/conditions-sets-063.md#c-a496b8928128ac7d) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-10054a2f3c7a22ea](../../evidence/parameters-sets-002.md#p-10054a2f3c7a22ea) · [状态效果 S-17d337b8a850652f](../../evidence/state_effects-sets-005.md#s-17d337b8a850652f)

### static_slot_creation_candidates-004523

```text
(config-vfi-neighbor)# no mpls control-word <cr>
```

Handler ` RVA 0x1AA05AC0 `；selector ` 6 `；EOL ` RVA 0x36D5A4C8 `。

模式根 ` RVA 0x36D59FC8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-44de6186c8774ee9](../../evidence/conditional_registrations-sets-001.md#r-44de6186c8774ee9) · [条件 C-073122115cae37c4](../../evidence/conditions-sets-003.md#c-073122115cae37c4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-17d337b8a850652f](../../evidence/state_effects-sets-005.md#s-17d337b8a850652f)

### static_slot_creation_candidates-004522

```text
(config-vfi-neighbor)# no mpls label <cr>
```

Handler ` RVA 0x1AA05AC0 `；selector ` 5 `；EOL ` RVA 0x36D5A1B8 `。

模式根 ` RVA 0x36D59FC8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-44de6186c8774ee9](../../evidence/conditional_registrations-sets-001.md#r-44de6186c8774ee9) · [条件 C-94f8e86968740cf5](../../evidence/conditions-sets-058.md#c-94f8e86968740cf5) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-17d337b8a850652f](../../evidence/state_effects-sets-005.md#s-17d337b8a850652f)
