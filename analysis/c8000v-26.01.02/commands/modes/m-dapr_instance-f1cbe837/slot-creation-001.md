# dapr_instance · 依赖静态建槽的条件安装

[模式索引](README.md) · [总索引](../../README.md)

### static_slot_creation_candidates-004586

```text
(config-dapr-instance)# border-router <cr>
```

Handler ` RVA 0x1AE2BBB0 `；selector ` 1 `；EOL ` RVA 0x36E53120 `。

模式根 ` RVA 0x36E4E208 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-402690e91e181c3e](../../evidence/conditional_registrations-sets-001.md#r-402690e91e181c3e) · [条件 C-9bc952d16efe9dd6](../../evidence/conditions-sets-060.md#c-9bc952d16efe9dd6) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### static_slot_creation_candidates-004588

```text
(config-dapr-instance)# no border-router <cr>
```

Handler ` RVA 0x1AE2BBB0 `；selector ` 1 `；EOL ` RVA 0x36E53120 `。

模式根 ` RVA 0x36E4E208 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-402690e91e181c3e](../../evidence/conditional_registrations-sets-001.md#r-402690e91e181c3e) · [条件 C-9bc952d16efe9dd6](../../evidence/conditions-sets-060.md#c-9bc952d16efe9dd6) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-8a23d61f0268cb39](../../evidence/state_effects-sets-029.md#s-8a23d61f0268cb39)

### static_slot_creation_candidates-004589

```text
(config-dapr-instance)# no route-manager <cr>
```

Handler ` RVA 0x1AE92920 `；selector ` 1 `；EOL ` RVA 0x36E53450 `。

模式根 ` RVA 0x36E4E208 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-fde3c4342f309f41](../../evidence/conditional_registrations-sets-003.md#r-fde3c4342f309f41) · [条件 C-27935d4b23223dba](../../evidence/conditions-sets-016.md#c-27935d4b23223dba) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-8a23d61f0268cb39](../../evidence/state_effects-sets-029.md#s-8a23d61f0268cb39)

### static_slot_creation_candidates-004587

```text
(config-dapr-instance)# route-manager <cr>
```

Handler ` RVA 0x1AE92920 `；selector ` 1 `；EOL ` RVA 0x36E53450 `。

模式根 ` RVA 0x36E4E208 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-fde3c4342f309f41](../../evidence/conditional_registrations-sets-003.md#r-fde3c4342f309f41) · [条件 C-27935d4b23223dba](../../evidence/conditions-sets-016.md#c-27935d4b23223dba) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)
