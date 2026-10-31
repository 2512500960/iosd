# voiceport · 依赖静态建槽的条件安装

[模式索引](README.md) · [总索引](../../README.md)

### static_slot_creation_candidates-004339

```text
(config-voiceport)# auto-cut-through <cr>
```

Handler ` RVA 0x1BD77260 `；selector ` 0 `；EOL ` RVA 0x377E3F18 `。

模式根 ` RVA 0x3717DBB0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-e29eb30324f61749](../../evidence/conditional_registrations-sets-002.md#r-e29eb30324f61749) · [条件 C-f5657179dc144a6e](../../evidence/conditions-sets-095.md#c-f5657179dc144a6e) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### static_slot_creation_candidates-004341

```text
(config-voiceport)# default auto-cut-through <cr>
```

Handler ` RVA 0x1BD77260 `；selector ` 0 `；EOL ` RVA 0x377E3F18 `。

模式根 ` RVA 0x3717DBB0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-e29eb30324f61749](../../evidence/conditional_registrations-sets-002.md#r-e29eb30324f61749) · [条件 C-f5657179dc144a6e](../../evidence/conditions-sets-095.md#c-f5657179dc144a6e) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-4a134a78b4d7e806](../../evidence/state_effects-sets-016.md#s-4a134a78b4d7e806)

### static_slot_creation_candidates-004346

```text
(config-voiceport)# default lpcor incoming <cr>
```

Handler ` RVA 0x172440D0 `；selector ` 19 `；EOL ` RVA 0x3633A698 `。

模式根 ` RVA 0x3717DBB0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-7fd2fdc9fb37ed9b](../../evidence/conditional_registrations-sets-002.md#r-7fd2fdc9fb37ed9b) · [条件 C-1d4b74e5e21cac58](../../evidence/conditions-sets-011.md#c-1d4b74e5e21cac58) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-4a134a78b4d7e806](../../evidence/state_effects-sets-016.md#s-4a134a78b4d7e806)

### static_slot_creation_candidates-004350

```text
(config-voiceport)# default lpcor outgoing <cr>
```

Handler ` RVA 0x172440D0 `；selector ` 20 `；EOL ` RVA 0x3633A9C0 `。

模式根 ` RVA 0x3717DBB0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-7fd2fdc9fb37ed9b](../../evidence/conditional_registrations-sets-002.md#r-7fd2fdc9fb37ed9b) · [条件 C-85082e80a4b50dd8](../../evidence/conditions-sets-051.md#c-85082e80a4b50dd8) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-4a134a78b4d7e806](../../evidence/state_effects-sets-016.md#s-4a134a78b4d7e806)

### static_slot_creation_candidates-004359

```text
(config-voiceport)# default voice-class busyout <number:1..10000> <cr>
```

Handler ` RVA 0x1BD79FD0 `；selector ` 0 `；EOL ` RVA 0x370B2720 `。

模式根 ` RVA 0x3717DBB0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` The busyout group tag number。

[候选注册 R-ab26b1700832d4a7](../../evidence/conditional_registrations-sets-002.md#r-ab26b1700832d4a7) · [条件 C-ebaf4a1f03f9ee1c](../../evidence/conditions-sets-091.md#c-ebaf4a1f03f9ee1c) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-8023552f6f17d999](../../evidence/parameters-sets-010.md#p-8023552f6f17d999) · [状态效果 S-4a134a78b4d7e806](../../evidence/state_effects-sets-016.md#s-4a134a78b4d7e806)

### static_slot_creation_candidates-004357

```text
(config-voiceport)# default voice-class called-number-pool <cr>
```

Handler ` RVA 0x1BDFB570 `；selector ` 58 `；EOL ` RVA 0x3717E590 `。

模式根 ` RVA 0x3717DBB0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-3a4e1f75f4501427](../../evidence/conditional_registrations-sets-001.md#r-3a4e1f75f4501427) · [条件 C-58607b7ac8f81b4e](../../evidence/conditions-sets-035.md#c-58607b7ac8f81b4e) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-4a134a78b4d7e806](../../evidence/state_effects-sets-016.md#s-4a134a78b4d7e806)

### static_slot_creation_candidates-004347

```text
(config-voiceport)# default voice-class permanent <cr>
```

Handler ` RVA 0x1BD59F10 `；selector ` 0 `；EOL ` RVA 0x370B2370 `。

模式根 ` RVA 0x3717DBB0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-ab26b1700832d4a7](../../evidence/conditional_registrations-sets-002.md#r-ab26b1700832d4a7) · [条件 C-d56aba199d3ab128](../../evidence/conditions-sets-082.md#c-d56aba199d3ab128) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-4a134a78b4d7e806](../../evidence/state_effects-sets-016.md#s-4a134a78b4d7e806)

### static_slot_creation_candidates-004354

```text
(config-voiceport)# default voice-class tone-signal <cr>
```

Handler ` RVA 0x1BD5A150 `；selector ` 0 `；EOL ` RVA 0x370B2A68 `。

模式根 ` RVA 0x3717DBB0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-ab26b1700832d4a7](../../evidence/conditional_registrations-sets-002.md#r-ab26b1700832d4a7) · [条件 C-97d7934d95bbd1f9](../../evidence/conditions-sets-059.md#c-97d7934d95bbd1f9) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-4a134a78b4d7e806](../../evidence/state_effects-sets-016.md#s-4a134a78b4d7e806)

### static_slot_creation_candidates-004344

```text
(config-voiceport)# lpcor incoming <string> <cr>
```

Handler ` RVA 0x172440D0 `；selector ` 19 `；EOL ` RVA 0x3633A698 `。

模式根 ` RVA 0x3717DBB0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` A string representing a lpcor tag。

[候选注册 R-7fd2fdc9fb37ed9b](../../evidence/conditional_registrations-sets-002.md#r-7fd2fdc9fb37ed9b) · [条件 C-54f8bb2df9e18938](../../evidence/conditions-sets-033.md#c-54f8bb2df9e18938) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-092a537f64f095ab](../../evidence/parameters-sets-001.md#p-092a537f64f095ab)

### static_slot_creation_candidates-004349

```text
(config-voiceport)# lpcor outgoing <string> <cr>
```

Handler ` RVA 0x172440D0 `；selector ` 20 `；EOL ` RVA 0x3633A9C0 `。

模式根 ` RVA 0x3717DBB0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` A string representing a lpcor tag。

[候选注册 R-7fd2fdc9fb37ed9b](../../evidence/conditional_registrations-sets-002.md#r-7fd2fdc9fb37ed9b) · [条件 C-f95df76c4c2df490](../../evidence/conditions-sets-096.md#c-f95df76c4c2df490) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-2929585395f66a7d](../../evidence/parameters-sets-004.md#p-2929585395f66a7d)

### static_slot_creation_candidates-004340

```text
(config-voiceport)# no auto-cut-through <cr>
```

Handler ` RVA 0x1BD77260 `；selector ` 0 `；EOL ` RVA 0x377E3F18 `。

模式根 ` RVA 0x3717DBB0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-e29eb30324f61749](../../evidence/conditional_registrations-sets-002.md#r-e29eb30324f61749) · [条件 C-f5657179dc144a6e](../../evidence/conditions-sets-095.md#c-f5657179dc144a6e) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-5fbf86d5f2feed49](../../evidence/state_effects-sets-021.md#s-5fbf86d5f2feed49)

### static_slot_creation_candidates-004342

```text
(config-voiceport)# no lpcor incoming <cr>
```

Handler ` RVA 0x172440D0 `；selector ` 19 `；EOL ` RVA 0x3633A698 `。

模式根 ` RVA 0x3717DBB0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-7fd2fdc9fb37ed9b](../../evidence/conditional_registrations-sets-002.md#r-7fd2fdc9fb37ed9b) · [条件 C-dd09b150722d7912](../../evidence/conditions-sets-085.md#c-dd09b150722d7912) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-5fbf86d5f2feed49](../../evidence/state_effects-sets-021.md#s-5fbf86d5f2feed49)

### static_slot_creation_candidates-004348

```text
(config-voiceport)# no lpcor outgoing <cr>
```

Handler ` RVA 0x172440D0 `；selector ` 20 `；EOL ` RVA 0x3633A9C0 `。

模式根 ` RVA 0x3717DBB0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-7fd2fdc9fb37ed9b](../../evidence/conditional_registrations-sets-002.md#r-7fd2fdc9fb37ed9b) · [条件 C-9911b1496a611569](../../evidence/conditions-sets-059.md#c-9911b1496a611569) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-5fbf86d5f2feed49](../../evidence/state_effects-sets-021.md#s-5fbf86d5f2feed49)

### static_slot_creation_candidates-004358

```text
(config-voiceport)# no voice-class busyout <number:1..10000> <cr>
```

Handler ` RVA 0x1BD79FD0 `；selector ` 0 `；EOL ` RVA 0x370B2720 `。

模式根 ` RVA 0x3717DBB0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` The busyout group tag number。

[候选注册 R-ab26b1700832d4a7](../../evidence/conditional_registrations-sets-002.md#r-ab26b1700832d4a7) · [条件 C-4df23302b2e1f6bb](../../evidence/conditions-sets-030.md#c-4df23302b2e1f6bb) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-8023552f6f17d999](../../evidence/parameters-sets-010.md#p-8023552f6f17d999) · [状态效果 S-5fbf86d5f2feed49](../../evidence/state_effects-sets-021.md#s-5fbf86d5f2feed49)

### static_slot_creation_candidates-004355

```text
(config-voiceport)# no voice-class called-number-pool <cr>
```

Handler ` RVA 0x1BDFB570 `；selector ` 58 `；EOL ` RVA 0x3717E590 `。

模式根 ` RVA 0x3717DBB0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-3a4e1f75f4501427](../../evidence/conditional_registrations-sets-001.md#r-3a4e1f75f4501427) · [条件 C-0902493c97ea90a3](../../evidence/conditions-sets-004.md#c-0902493c97ea90a3) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-5fbf86d5f2feed49](../../evidence/state_effects-sets-021.md#s-5fbf86d5f2feed49)

### static_slot_creation_candidates-004343

```text
(config-voiceport)# no voice-class permanent <cr>
```

Handler ` RVA 0x1BD59F10 `；selector ` 0 `；EOL ` RVA 0x370B2370 `。

模式根 ` RVA 0x3717DBB0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-ab26b1700832d4a7](../../evidence/conditional_registrations-sets-002.md#r-ab26b1700832d4a7) · [条件 C-7e5673aaad6fa00a](../../evidence/conditions-sets-049.md#c-7e5673aaad6fa00a) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-5fbf86d5f2feed49](../../evidence/state_effects-sets-021.md#s-5fbf86d5f2feed49)

### static_slot_creation_candidates-004352

```text
(config-voiceport)# no voice-class tone-signal <cr>
```

Handler ` RVA 0x1BD5A150 `；selector ` 0 `；EOL ` RVA 0x370B2A68 `。

模式根 ` RVA 0x3717DBB0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-ab26b1700832d4a7](../../evidence/conditional_registrations-sets-002.md#r-ab26b1700832d4a7) · [条件 C-f0d410540a7b5ddd](../../evidence/conditions-sets-093.md#c-f0d410540a7b5ddd) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-5fbf86d5f2feed49](../../evidence/state_effects-sets-021.md#s-5fbf86d5f2feed49)

### static_slot_creation_candidates-004351

```text
(config-voiceport)# voice-class busyout <number:1..10000> <cr>
```

Handler ` RVA 0x1BD79FD0 `；selector ` 0 `；EOL ` RVA 0x370B2720 `。

模式根 ` RVA 0x3717DBB0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` The busyout group tag number。

[候选注册 R-ab26b1700832d4a7](../../evidence/conditional_registrations-sets-002.md#r-ab26b1700832d4a7) · [条件 C-b742752b8ef35a3e](../../evidence/conditions-sets-071.md#c-b742752b8ef35a3e) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-8023552f6f17d999](../../evidence/parameters-sets-010.md#p-8023552f6f17d999)

### static_slot_creation_candidates-004356

```text
(config-voiceport)# voice-class called-number-pool <number:1..10000> <cr>
```

Handler ` RVA 0x1BDFB570 `；selector ` 58 `；EOL ` RVA 0x3717E590 `。

模式根 ` RVA 0x3717DBB0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Called Number Pool Tag。

[候选注册 R-3a4e1f75f4501427](../../evidence/conditional_registrations-sets-001.md#r-3a4e1f75f4501427) · [条件 C-f0d5e076e1a0b4aa](../../evidence/conditions-sets-093.md#c-f0d5e076e1a0b4aa) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-89dd1dbc7b19bce7](../../evidence/parameters-sets-011.md#p-89dd1dbc7b19bce7)

### static_slot_creation_candidates-004345

```text
(config-voiceport)# voice-class permanent <number:1..10000> <cr>
```

Handler ` RVA 0x1BD59F10 `；selector ` 0 `；EOL ` RVA 0x370B2370 `。

模式根 ` RVA 0x3717DBB0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` The permanent connection group tag number。

[候选注册 R-ab26b1700832d4a7](../../evidence/conditional_registrations-sets-002.md#r-ab26b1700832d4a7) · [条件 C-f7f9e196c084765c](../../evidence/conditions-sets-096.md#c-f7f9e196c084765c) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-a390ca0bfdae3aab](../../evidence/parameters-sets-012.md#p-a390ca0bfdae3aab)

### static_slot_creation_candidates-004353

```text
(config-voiceport)# voice-class tone-signal <string> <cr>
```

Handler ` RVA 0x1BD5A150 `；selector ` 0 `；EOL ` RVA 0x370B2A68 `。

模式根 ` RVA 0x3717DBB0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` tone signal Name。

[候选注册 R-ab26b1700832d4a7](../../evidence/conditional_registrations-sets-002.md#r-ab26b1700832d4a7) · [条件 C-7f8e11a96d2b8a38](../../evidence/conditions-sets-049.md#c-7f8e11a96d2b8a38) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-3eb9475a1595737b](../../evidence/parameters-sets-005.md#p-3eb9475a1595737b)
