# l2sdwan-inst · 依赖静态建槽的条件安装

[模式索引](README.md) · [总索引](../../README.md)

### static_slot_creation_candidates-004417

```text
(config-l2sdwan-sdi)# active-election wait-time <number:1..3600> <cr>
```

Handler ` RVA 0x16BB44D0 `；selector ` 0 `；EOL ` RVA 0x36126E00 `。

模式根 ` RVA 0x36125028 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of seconds to wait before electing a designated forwarder。

[候选注册 R-cb3a9af7a50957fc](../../evidence/conditional_registrations-sets-002.md#r-cb3a9af7a50957fc) · [条件 C-85af470bdae01d6f](../../evidence/conditions-sets-052.md#c-85af470bdae01d6f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-3c5eab9b37f1232e](../../evidence/parameters-sets-005.md#p-3c5eab9b37f1232e)

### static_slot_creation_candidates-004418

```text
(config-l2sdwan-sdi)# default active-election wait-time <cr>
```

Handler ` RVA 0x16BB44D0 `；selector ` 0 `；EOL ` RVA 0x36126E00 `。

模式根 ` RVA 0x36125028 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-cb3a9af7a50957fc](../../evidence/conditional_registrations-sets-002.md#r-cb3a9af7a50957fc) · [条件 C-a9b2c888c3d16ece](../../evidence/conditions-sets-065.md#c-a9b2c888c3d16ece) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-d53bc41499afaabf](../../evidence/state_effects-sets-045.md#s-d53bc41499afaabf)

### static_slot_creation_candidates-004408

```text
(config-l2sdwan-sdi)# default flooding-suppression <cr>
```

Handler ` RVA 0x16BB4450 `；selector ` 0 `；EOL ` RVA 0x361266D8 `。

模式根 ` RVA 0x36125028 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-cb3a9af7a50957fc](../../evidence/conditional_registrations-sets-002.md#r-cb3a9af7a50957fc) · [条件 C-7792e41646b83f1d](../../evidence/conditions-sets-046.md#c-7792e41646b83f1d) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-d53bc41499afaabf](../../evidence/state_effects-sets-045.md#s-d53bc41499afaabf)

### static_slot_creation_candidates-004415

```text
(config-l2sdwan-sdi)# default ip local-learning <cr>
```

Handler ` RVA 0x16BB4410 `；selector ` 0 `；EOL ` RVA 0x36126300 `。

模式根 ` RVA 0x36125028 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-cb3a9af7a50957fc](../../evidence/conditional_registrations-sets-002.md#r-cb3a9af7a50957fc) · [条件 C-52850a78a0a38807](../../evidence/conditions-sets-032.md#c-52850a78a0a38807) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-d53bc41499afaabf](../../evidence/state_effects-sets-045.md#s-d53bc41499afaabf)

### static_slot_creation_candidates-004420

```text
(config-l2sdwan-sdi)# default l2protocol forward <cr>
```

Handler ` RVA 0x16BB16A0 `；selector ` 0 `；EOL ` RVA 0x36127E98 `。

模式根 ` RVA 0x36125028 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-071fb9500c3a1c4c](../../evidence/conditional_registrations-sets-001.md#r-071fb9500c3a1c4c) · [条件 C-64bdfe9192aef85a](../../evidence/conditions-sets-039.md#c-64bdfe9192aef85a) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-5528c8a262cc29eb](../../evidence/state_effects-sets-018.md#s-5528c8a262cc29eb)

### static_slot_creation_candidates-004411

```text
(config-l2sdwan-sdi)# default redundancy <cr>
```

Handler ` RVA 0x16BB4490 `；selector ` 0 `；EOL ` RVA 0x36126A60 `。

模式根 ` RVA 0x36125028 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-cb3a9af7a50957fc](../../evidence/conditional_registrations-sets-002.md#r-cb3a9af7a50957fc) · [条件 C-17be74750044057e](../../evidence/conditions-sets-009.md#c-17be74750044057e) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-d53bc41499afaabf](../../evidence/state_effects-sets-045.md#s-d53bc41499afaabf)

### static_slot_creation_candidates-004407

```text
(config-l2sdwan-sdi)# flooding-suppression enable <cr>
```

Handler ` RVA 0x16BB4450 `；selector ` 0 `；EOL ` RVA 0x361266D8 `。

模式根 ` RVA 0x36125028 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-cb3a9af7a50957fc](../../evidence/conditional_registrations-sets-002.md#r-cb3a9af7a50957fc) · [条件 C-dcdf71c5c563b35b](../../evidence/conditions-sets-085.md#c-dcdf71c5c563b35b) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-6a5a82f84a1a5141](../../evidence/state_effects-sets-023.md#s-6a5a82f84a1a5141)

### static_slot_creation_candidates-004414

```text
(config-l2sdwan-sdi)# ip local-learning enable <cr>
```

Handler ` RVA 0x16BB4410 `；selector ` 0 `；EOL ` RVA 0x36126300 `。

模式根 ` RVA 0x36125028 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-cb3a9af7a50957fc](../../evidence/conditional_registrations-sets-002.md#r-cb3a9af7a50957fc) · [条件 C-5f2df1ec56f7f7f3](../../evidence/conditions-sets-037.md#c-5f2df1ec56f7f7f3) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-4ec896d4f5823268](../../evidence/state_effects-sets-017.md#s-4ec896d4f5823268)

### static_slot_creation_candidates-004412

```text
(config-l2sdwan-sdi)# l2protocol forward <cr>
```

Handler ` RVA 0x16BB16A0 `；selector ` 0 `；EOL ` RVA 0x36127E98 `。

模式根 ` RVA 0x36125028 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-071fb9500c3a1c4c](../../evidence/conditional_registrations-sets-001.md#r-071fb9500c3a1c4c) · [条件 C-64bdfe9192aef85a](../../evidence/conditions-sets-039.md#c-64bdfe9192aef85a) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c37b9ba61a23bc71](../../evidence/state_effects-sets-041.md#s-c37b9ba61a23bc71)

### static_slot_creation_candidates-004416

```text
(config-l2sdwan-sdi)# no active-election wait-time <cr>
```

Handler ` RVA 0x16BB44D0 `；selector ` 0 `；EOL ` RVA 0x36126E00 `。

模式根 ` RVA 0x36125028 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-cb3a9af7a50957fc](../../evidence/conditional_registrations-sets-002.md#r-cb3a9af7a50957fc) · [条件 C-34196cc3db782d8b](../../evidence/conditions-sets-020.md#c-34196cc3db782d8b) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-d1f5eab02caa5d6c](../../evidence/state_effects-sets-044.md#s-d1f5eab02caa5d6c)

### static_slot_creation_candidates-004406

```text
(config-l2sdwan-sdi)# no flooding-suppression <cr>
```

Handler ` RVA 0x16BB4450 `；selector ` 0 `；EOL ` RVA 0x361266D8 `。

模式根 ` RVA 0x36125028 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-cb3a9af7a50957fc](../../evidence/conditional_registrations-sets-002.md#r-cb3a9af7a50957fc) · [条件 C-d1ac356480772251](../../evidence/conditions-sets-081.md#c-d1ac356480772251) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-d1f5eab02caa5d6c](../../evidence/state_effects-sets-044.md#s-d1f5eab02caa5d6c)

### static_slot_creation_candidates-004413

```text
(config-l2sdwan-sdi)# no ip local-learning <cr>
```

Handler ` RVA 0x16BB4410 `；selector ` 0 `；EOL ` RVA 0x36126300 `。

模式根 ` RVA 0x36125028 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-cb3a9af7a50957fc](../../evidence/conditional_registrations-sets-002.md#r-cb3a9af7a50957fc) · [条件 C-d641f68cb9d3c0e2](../../evidence/conditions-sets-083.md#c-d641f68cb9d3c0e2) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-d1f5eab02caa5d6c](../../evidence/state_effects-sets-044.md#s-d1f5eab02caa5d6c)

### static_slot_creation_candidates-004419

```text
(config-l2sdwan-sdi)# no l2protocol forward <cr>
```

Handler ` RVA 0x16BB16A0 `；selector ` 0 `；EOL ` RVA 0x36127E98 `。

模式根 ` RVA 0x36125028 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-071fb9500c3a1c4c](../../evidence/conditional_registrations-sets-001.md#r-071fb9500c3a1c4c) · [条件 C-64bdfe9192aef85a](../../evidence/conditions-sets-039.md#c-64bdfe9192aef85a) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-b28f2b48feed5098](../../evidence/state_effects-sets-038.md#s-b28f2b48feed5098)

### static_slot_creation_candidates-004409

```text
(config-l2sdwan-sdi)# no redundancy <cr>
```

Handler ` RVA 0x16BB4490 `；selector ` 0 `；EOL ` RVA 0x36126A60 `。

模式根 ` RVA 0x36125028 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-cb3a9af7a50957fc](../../evidence/conditional_registrations-sets-002.md#r-cb3a9af7a50957fc) · [条件 C-fa36712beef28b62](../../evidence/conditions-sets-097.md#c-fa36712beef28b62) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-d1f5eab02caa5d6c](../../evidence/state_effects-sets-044.md#s-d1f5eab02caa5d6c)

### static_slot_creation_candidates-004410

```text
(config-l2sdwan-sdi)# redundancy all-active <cr>
```

Handler ` RVA 0x16BB4490 `；selector ` 0 `；EOL ` RVA 0x36126A60 `。

模式根 ` RVA 0x36125028 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-cb3a9af7a50957fc](../../evidence/conditional_registrations-sets-002.md#r-cb3a9af7a50957fc) · [条件 C-7966bc46f2d39315](../../evidence/conditions-sets-047.md#c-7966bc46f2d39315) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-2017c66d7d966a3a](../../evidence/state_effects-sets-007.md#s-2017c66d7d966a3a)
