# l2-pw-rtg · 依赖静态建槽的条件安装

[模式索引](README.md) · [总索引](../../README.md)

### static_slot_creation_candidates-004577

```text
(config-l2-pw-rtg)# default switching-point vcid <cr>
```

Handler ` RVA 0x1AA21420 `；selector ` 1 `；EOL ` RVA 0x36D4AE68 `。

模式根 ` RVA 0x36D4A9D0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-b34df342b9a0a35f](../../evidence/conditional_registrations-sets-002.md#r-b34df342b9a0a35f) · [条件 C-f0901c0602164ec4](../../evidence/conditions-sets-093.md#c-f0901c0602164ec4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-db34c57f851cf1c0](../../evidence/state_effects-sets-046.md#s-db34c57f851cf1c0)

### static_slot_creation_candidates-004575

```text
(config-l2-pw-rtg)# default terminating-pe <cr>
```

Handler ` RVA 0x1AA21420 `；selector ` 2 `；EOL ` RVA 0x36D4B1B0 `。

模式根 ` RVA 0x36D4A9D0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-b34df342b9a0a35f](../../evidence/conditional_registrations-sets-002.md#r-b34df342b9a0a35f) · [条件 C-10dab96e5f331a61](../../evidence/conditions-sets-007.md#c-10dab96e5f331a61) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-db34c57f851cf1c0](../../evidence/state_effects-sets-046.md#s-db34c57f851cf1c0)

### static_slot_creation_candidates-004576

```text
(config-l2-pw-rtg)# no switching-point vcid <cr>
```

Handler ` RVA 0x1AA21420 `；selector ` 1 `；EOL ` RVA 0x36D4AE68 `。

模式根 ` RVA 0x36D4A9D0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-b34df342b9a0a35f](../../evidence/conditional_registrations-sets-002.md#r-b34df342b9a0a35f) · [条件 C-500c6e7e46b23894](../../evidence/conditions-sets-031.md#c-500c6e7e46b23894) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-0c57ed62a261f309](../../evidence/state_effects-sets-003.md#s-0c57ed62a261f309)

### static_slot_creation_candidates-004573

```text
(config-l2-pw-rtg)# no terminating-pe <cr>
```

Handler ` RVA 0x1AA21420 `；selector ` 2 `；EOL ` RVA 0x36D4B1B0 `。

模式根 ` RVA 0x36D4A9D0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-b34df342b9a0a35f](../../evidence/conditional_registrations-sets-002.md#r-b34df342b9a0a35f) · [条件 C-e9efc284ac0adb28](../../evidence/conditions-sets-090.md#c-e9efc284ac0adb28) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-0c57ed62a261f309](../../evidence/state_effects-sets-003.md#s-0c57ed62a261f309)

### static_slot_creation_candidates-004578

```text
(config-l2-pw-rtg)# switching-point vcid <number:1..2147483647> <number:1..2147483647> <cr>
```

Handler ` RVA 0x1AA21420 `；selector ` 1 `；EOL ` RVA 0x36D4AE68 `。

模式根 ` RVA 0x36D4A9D0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Minimum VCID value；` unsigned_number ` Maximum VCID value。

[候选注册 R-b34df342b9a0a35f](../../evidence/conditional_registrations-sets-002.md#r-b34df342b9a0a35f) · [条件 C-28dbc4ffdd88173c](../../evidence/conditions-sets-016.md#c-28dbc4ffdd88173c) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-3c2b2914ca9b8c86](../../evidence/parameters-sets-005.md#p-3c2b2914ca9b8c86)

### static_slot_creation_candidates-004574

```text
(config-l2-pw-rtg)# terminating-pe tie-breaker <cr>
```

Handler ` RVA 0x1AA21420 `；selector ` 2 `；EOL ` RVA 0x36D4B1B0 `。

模式根 ` RVA 0x36D4A9D0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-b34df342b9a0a35f](../../evidence/conditional_registrations-sets-002.md#r-b34df342b9a0a35f) · [条件 C-f1807956e682ca36](../../evidence/conditions-sets-093.md#c-f1807956e682ca36) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

