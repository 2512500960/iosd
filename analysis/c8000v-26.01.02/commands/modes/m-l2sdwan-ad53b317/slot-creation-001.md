# l2sdwan · 依赖静态建槽的条件安装

[模式索引](README.md) · [总索引](../../README.md)

### static_slot_creation_candidates-004467

```text
(config-l2sdwan)# default ip duplication <cr>
```

Handler ` RVA 0x16BB5210 `；selector ` 0 `；EOL ` RVA 0x36128E70 `。

模式根 ` RVA 0x36125000 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-faffec974c8835e8](../../evidence/conditional_registrations-sets-003.md#r-faffec974c8835e8) · [条件 C-7d8d84abb4b55215](../../evidence/conditions-sets-049.md#c-7d8d84abb4b55215) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9c8abc04c4ed1f21](../../evidence/state_effects-sets-033.md#s-9c8abc04c4ed1f21)

### static_slot_creation_candidates-004474

```text
(config-l2sdwan)# default ip local-learning limit per-mac ipv4 <cr>
```

Handler ` RVA 0x16BB5190 `；selector ` 0 `；EOL ` RVA 0x36128618 `。

模式根 ` RVA 0x36125000 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-faffec974c8835e8](../../evidence/conditional_registrations-sets-003.md#r-faffec974c8835e8) · [条件 C-0d0c1307d879a40c](../../evidence/conditions-sets-005.md#c-0d0c1307d879a40c) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-32ba4eb8848e4874](../../evidence/state_effects-sets-011.md#s-32ba4eb8848e4874)

### static_slot_creation_candidates-004470

```text
(config-l2sdwan)# default ip local-learning time down <cr>
```

Handler ` RVA 0x16BB51D0 `；selector ` 0 `；EOL ` RVA 0x361289F8 `。

模式根 ` RVA 0x36125000 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-faffec974c8835e8](../../evidence/conditional_registrations-sets-003.md#r-faffec974c8835e8) · [条件 C-67f5e6ca2f18cd48](../../evidence/conditions-sets-040.md#c-67f5e6ca2f18cd48) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9eb806b63e8de7fa](../../evidence/state_effects-sets-034.md#s-9eb806b63e8de7fa)

### static_slot_creation_candidates-004465

```text
(config-l2sdwan)# default mac duplication <cr>
```

Handler ` RVA 0x16BB52A0 `；selector ` 0 `；EOL ` RVA 0x36129298 `。

模式根 ` RVA 0x36125000 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-faffec974c8835e8](../../evidence/conditional_registrations-sets-003.md#r-faffec974c8835e8) · [条件 C-ad90d97b1d694e23](../../evidence/conditions-sets-067.md#c-ad90d97b1d694e23) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9c8abc04c4ed1f21](../../evidence/state_effects-sets-033.md#s-9c8abc04c4ed1f21)

### static_slot_creation_candidates-004475

```text
(config-l2sdwan)# ip duplication limit <number:2..1000> time <number:10..36000> <cr>
```

Handler ` RVA 0x16BB5210 `；selector ` 0 `；EOL ` RVA 0x36128E70 `。

模式根 ` RVA 0x36125000 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of IP moves within specified time interval；` unsigned_number ` Seconds。

[候选注册 R-faffec974c8835e8](../../evidence/conditional_registrations-sets-003.md#r-faffec974c8835e8) · [条件 C-54b0481c27863f1b](../../evidence/conditions-sets-033.md#c-54b0481c27863f1b) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-a892d256b84e9a64](../../evidence/parameters-sets-013.md#p-a892d256b84e9a64)

### static_slot_creation_candidates-004473

```text
(config-l2sdwan)# ip local-learning limit per-mac ipv4 <number:0..32000> <cr>
```

Handler ` RVA 0x16BB5190 `；selector ` 0 `；EOL ` RVA 0x36128618 `。

模式根 ` RVA 0x36125000 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Maximum number of addresses。

[候选注册 R-faffec974c8835e8](../../evidence/conditional_registrations-sets-003.md#r-faffec974c8835e8) · [条件 C-727fbbf7c8d9ebbf](../../evidence/conditions-sets-044.md#c-727fbbf7c8d9ebbf) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-f5a4770a5a88821f](../../evidence/parameters-sets-018.md#p-f5a4770a5a88821f) · [状态效果 S-e0e5b32de79e2323](../../evidence/state_effects-sets-048.md#s-e0e5b32de79e2323)

### static_slot_creation_candidates-004469

```text
(config-l2sdwan)# ip local-learning time down <number:1..1440> <cr>
```

Handler ` RVA 0x16BB51D0 `；selector ` 0 `；EOL ` RVA 0x361289F8 `。

模式根 ` RVA 0x36125000 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of minutes。

[候选注册 R-faffec974c8835e8](../../evidence/conditional_registrations-sets-003.md#r-faffec974c8835e8) · [条件 C-65cc678dc326c217](../../evidence/conditions-sets-039.md#c-65cc678dc326c217) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-2a11a0e19e1ee399](../../evidence/parameters-sets-004.md#p-2a11a0e19e1ee399) · [状态效果 S-161132c49d3ced5d](../../evidence/state_effects-sets-005.md#s-161132c49d3ced5d)

### static_slot_creation_candidates-004472

```text
(config-l2sdwan)# mac duplication limit <number:2..1000> time <number:10..36000> <cr>
```

Handler ` RVA 0x16BB52A0 `；selector ` 0 `；EOL ` RVA 0x36129298 `。

模式根 ` RVA 0x36125000 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of MAC moves within specified time interval；` unsigned_number ` Seconds。

[候选注册 R-faffec974c8835e8](../../evidence/conditional_registrations-sets-003.md#r-faffec974c8835e8) · [条件 C-f054b439fb8331c3](../../evidence/conditions-sets-093.md#c-f054b439fb8331c3) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-ce68a61850983296](../../evidence/parameters-sets-016.md#p-ce68a61850983296)

### static_slot_creation_candidates-004466

```text
(config-l2sdwan)# no ip duplication <cr>
```

Handler ` RVA 0x16BB5210 `；selector ` 0 `；EOL ` RVA 0x36128E70 `。

模式根 ` RVA 0x36125000 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-faffec974c8835e8](../../evidence/conditional_registrations-sets-003.md#r-faffec974c8835e8) · [条件 C-c79c46c4b750b01c](../../evidence/conditions-sets-077.md#c-c79c46c4b750b01c) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-5542db2cdbc0841a](../../evidence/state_effects-sets-019.md#s-5542db2cdbc0841a)

### static_slot_creation_candidates-004471

```text
(config-l2sdwan)# no ip local-learning limit per-mac ipv4 <cr>
```

Handler ` RVA 0x16BB5190 `；selector ` 0 `；EOL ` RVA 0x36128618 `。

模式根 ` RVA 0x36125000 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-faffec974c8835e8](../../evidence/conditional_registrations-sets-003.md#r-faffec974c8835e8) · [条件 C-15e3d900a750f3b9](../../evidence/conditions-sets-009.md#c-15e3d900a750f3b9) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-409b40c2c51528cd](../../evidence/state_effects-sets-014.md#s-409b40c2c51528cd)

### static_slot_creation_candidates-004468

```text
(config-l2sdwan)# no ip local-learning time down <cr>
```

Handler ` RVA 0x16BB51D0 `；selector ` 0 `；EOL ` RVA 0x361289F8 `。

模式根 ` RVA 0x36125000 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-faffec974c8835e8](../../evidence/conditional_registrations-sets-003.md#r-faffec974c8835e8) · [条件 C-8d51538fce87cf08](../../evidence/conditions-sets-055.md#c-8d51538fce87cf08) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-a4d6ee1cf6d2b2b8](../../evidence/state_effects-sets-035.md#s-a4d6ee1cf6d2b2b8)

### static_slot_creation_candidates-004464

```text
(config-l2sdwan)# no mac duplication <cr>
```

Handler ` RVA 0x16BB52A0 `；selector ` 0 `；EOL ` RVA 0x36129298 `。

模式根 ` RVA 0x36125000 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-faffec974c8835e8](../../evidence/conditional_registrations-sets-003.md#r-faffec974c8835e8) · [条件 C-67d6b4f85621a28c](../../evidence/conditions-sets-040.md#c-67d6b4f85621a28c) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-5542db2cdbc0841a](../../evidence/state_effects-sets-019.md#s-5542db2cdbc0841a)
