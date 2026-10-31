# cm-ac · 依赖静态建槽的条件安装

[模式索引](README.md) · [总索引](../../README.md)

### static_slot_creation_candidates-004279

```text
(config-connection)# backup delay <number:0..180> <number:0..180> <cr>
```

Handler ` RVA 0x1A9F9DE0 `；selector ` 12 `；EOL ` RVA 0x369992C8 `。

模式根 ` RVA 0x369980B8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Enable delay；` unsigned_number ` Disable delay。

[候选注册 R-8e7981e23c84363d](../../evidence/conditional_registrations-sets-002.md#r-8e7981e23c84363d) · [条件 C-8602aad3fc8607f1](../../evidence/conditions-sets-052.md#c-8602aad3fc8607f1) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-be06c8071cb8b264](../../evidence/parameters-sets-014.md#p-be06c8071cb8b264) · [状态效果 S-8b700a511dfcff79](../../evidence/state_effects-sets-030.md#s-8b700a511dfcff79)

### static_slot_creation_candidates-004278

```text
(config-connection)# backup peer <address> <number:1..4294967295> <cr>
```

Handler ` RVA 0x1A9F9DE0 `；selector ` 10 `；EOL ` RVA 0x36998F28 `。

模式根 ` RVA 0x369980B8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP address of peer；` unsigned_number ` Peer VC ID value。

[候选注册 R-8e7981e23c84363d](../../evidence/conditional_registrations-sets-002.md#r-8e7981e23c84363d) · [条件 C-1411db15b9b2f479](../../evidence/conditions-sets-008.md#c-1411db15b9b2f479) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-99b680913e44a416](../../evidence/parameters-sets-012.md#p-99b680913e44a416) · [状态效果 S-73916753dc1f5794](../../evidence/state_effects-sets-025.md#s-73916753dc1f5794)

### static_slot_creation_candidates-004274

```text
(config-connection)# default backup delay <cr>
```

Handler ` RVA 0x1A9F9DE0 `；selector ` 12 `；EOL ` RVA 0x369992C8 `。

模式根 ` RVA 0x369980B8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-8e7981e23c84363d](../../evidence/conditional_registrations-sets-002.md#r-8e7981e23c84363d) · [条件 C-ea80063d42ed6e8d](../../evidence/conditions-sets-091.md#c-ea80063d42ed6e8d) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-6779985181a2d8f4](../../evidence/state_effects-sets-022.md#s-6779985181a2d8f4)

### static_slot_creation_candidates-004283

```text
(config-connection)# default backup peer <address> <number:1..4294967295> <cr>
```

Handler ` RVA 0x1A9F9DE0 `；selector ` 10 `；EOL ` RVA 0x36998F28 `。

模式根 ` RVA 0x369980B8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IP address of peer；` unsigned_number ` Peer VC ID value。

[候选注册 R-8e7981e23c84363d](../../evidence/conditional_registrations-sets-002.md#r-8e7981e23c84363d) · [条件 C-1411db15b9b2f479](../../evidence/conditions-sets-008.md#c-1411db15b9b2f479) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-99b680913e44a416](../../evidence/parameters-sets-012.md#p-99b680913e44a416) · [状态效果 S-25574240953033d9](../../evidence/state_effects-sets-008.md#s-25574240953033d9)

### static_slot_creation_candidates-004276

```text
(config-connection)# default match protocol ipv6 <cr>
```

Handler ` RVA 0x1A9F9DE0 `；selector ` 8 `；EOL ` RVA 0x369989D8 `。

模式根 ` RVA 0x369980B8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-8e7981e23c84363d](../../evidence/conditional_registrations-sets-002.md#r-8e7981e23c84363d) · [条件 C-2e206f7f1164066f](../../evidence/conditions-sets-018.md#c-2e206f7f1164066f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-6779985181a2d8f4](../../evidence/state_effects-sets-022.md#s-6779985181a2d8f4)

### static_slot_creation_candidates-004268

```text
(config-connection)# default mtu <cr>
```

Handler ` RVA 0x1A9F9DE0 `；selector ` 14 `；EOL ` RVA 0x36999AE8 `。

模式根 ` RVA 0x369980B8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-8e7981e23c84363d](../../evidence/conditional_registrations-sets-002.md#r-8e7981e23c84363d) · [条件 C-ba523bd78330783c](../../evidence/conditions-sets-072.md#c-ba523bd78330783c) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-6779985181a2d8f4](../../evidence/state_effects-sets-022.md#s-6779985181a2d8f4)

### static_slot_creation_candidates-004272

```text
(config-connection)# default redundancy all-active <cr>
```

Handler ` RVA 0x1A9F9DE0 `；selector ` 13 `；EOL ` RVA 0x369997A0 `。

模式根 ` RVA 0x369980B8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-8e7981e23c84363d](../../evidence/conditional_registrations-sets-002.md#r-8e7981e23c84363d) · [条件 C-9fd94dca2c0b8d48](../../evidence/conditions-sets-062.md#c-9fd94dca2c0b8d48) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-6779985181a2d8f4](../../evidence/state_effects-sets-022.md#s-6779985181a2d8f4)

### static_slot_creation_candidates-004281

```text
(config-connection)# default remote link failure notification <cr>
```

Handler ` RVA 0x1A9F9DE0 `；selector ` 9 `；EOL ` RVA 0x36998640 `。

模式根 ` RVA 0x369980B8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-8e7981e23c84363d](../../evidence/conditional_registrations-sets-002.md#r-8e7981e23c84363d) · [条件 C-e94e4434a857d886](../../evidence/conditions-sets-090.md#c-e94e4434a857d886) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-6779985181a2d8f4](../../evidence/state_effects-sets-022.md#s-6779985181a2d8f4)

### static_slot_creation_candidates-004269

```text
(config-connection)# match protocol ipv6 <cr>
```

Handler ` RVA 0x1A9F9DE0 `；selector ` 8 `；EOL ` RVA 0x369989D8 `。

模式根 ` RVA 0x369980B8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-8e7981e23c84363d](../../evidence/conditional_registrations-sets-002.md#r-8e7981e23c84363d) · [条件 C-2e206f7f1164066f](../../evidence/conditions-sets-018.md#c-2e206f7f1164066f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### static_slot_creation_candidates-004284

```text
(config-connection)# mtu <?number_help_func_action@55558beedac0> <cr>
```

Handler ` RVA 0x1A9F9DE0 `；selector ` 14 `；EOL ` RVA 0x36999AE8 `。

模式根 ` RVA 0x369980B8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[候选注册 R-8e7981e23c84363d](../../evidence/conditional_registrations-sets-002.md#r-8e7981e23c84363d) · [条件 C-d9fae7f04721c5e1](../../evidence/conditions-sets-084.md#c-d9fae7f04721c5e1) · [缺口 G-8c36f96e15748e9e](../../evidence/gaps-sets-005.md#g-8c36f96e15748e9e)

### static_slot_creation_candidates-004273

```text
(config-connection)# no backup delay <cr>
```

Handler ` RVA 0x1A9F9DE0 `；selector ` 12 `；EOL ` RVA 0x369992C8 `。

模式根 ` RVA 0x369980B8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-8e7981e23c84363d](../../evidence/conditional_registrations-sets-002.md#r-8e7981e23c84363d) · [条件 C-aba8060ca174c415](../../evidence/conditions-sets-066.md#c-aba8060ca174c415) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-6dbe0067bc4c2181](../../evidence/state_effects-sets-023.md#s-6dbe0067bc4c2181)

### static_slot_creation_candidates-004282

```text
(config-connection)# no backup peer <address> <number:1..4294967295> <cr>
```

Handler ` RVA 0x1A9F9DE0 `；selector ` 10 `；EOL ` RVA 0x36998F28 `。

模式根 ` RVA 0x369980B8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` IP address of peer；` unsigned_number ` Peer VC ID value。

[候选注册 R-8e7981e23c84363d](../../evidence/conditional_registrations-sets-002.md#r-8e7981e23c84363d) · [条件 C-1411db15b9b2f479](../../evidence/conditions-sets-008.md#c-1411db15b9b2f479) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-99b680913e44a416](../../evidence/parameters-sets-012.md#p-99b680913e44a416) · [状态效果 S-c08b4427223e0826](../../evidence/state_effects-sets-041.md#s-c08b4427223e0826)

### static_slot_creation_candidates-004275

```text
(config-connection)# no match protocol ipv6 <cr>
```

Handler ` RVA 0x1A9F9DE0 `；selector ` 8 `；EOL ` RVA 0x369989D8 `。

模式根 ` RVA 0x369980B8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-8e7981e23c84363d](../../evidence/conditional_registrations-sets-002.md#r-8e7981e23c84363d) · [条件 C-2e206f7f1164066f](../../evidence/conditions-sets-018.md#c-2e206f7f1164066f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-6dbe0067bc4c2181](../../evidence/state_effects-sets-023.md#s-6dbe0067bc4c2181)

### static_slot_creation_candidates-004267

```text
(config-connection)# no mtu <cr>
```

Handler ` RVA 0x1A9F9DE0 `；selector ` 14 `；EOL ` RVA 0x36999AE8 `。

模式根 ` RVA 0x369980B8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-8e7981e23c84363d](../../evidence/conditional_registrations-sets-002.md#r-8e7981e23c84363d) · [条件 C-f83aef29d5b78492](../../evidence/conditions-sets-096.md#c-f83aef29d5b78492) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-6dbe0067bc4c2181](../../evidence/state_effects-sets-023.md#s-6dbe0067bc4c2181)

### static_slot_creation_candidates-004270

```text
(config-connection)# no redundancy all-active <cr>
```

Handler ` RVA 0x1A9F9DE0 `；selector ` 13 `；EOL ` RVA 0x369997A0 `。

模式根 ` RVA 0x369980B8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-8e7981e23c84363d](../../evidence/conditional_registrations-sets-002.md#r-8e7981e23c84363d) · [条件 C-b445b6a5f0ce14c4](../../evidence/conditions-sets-070.md#c-b445b6a5f0ce14c4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-6dbe0067bc4c2181](../../evidence/state_effects-sets-023.md#s-6dbe0067bc4c2181)

### static_slot_creation_candidates-004280

```text
(config-connection)# no remote link failure notification <cr>
```

Handler ` RVA 0x1A9F9DE0 `；selector ` 9 `；EOL ` RVA 0x36998640 `。

模式根 ` RVA 0x369980B8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-8e7981e23c84363d](../../evidence/conditional_registrations-sets-002.md#r-8e7981e23c84363d) · [条件 C-e94e4434a857d886](../../evidence/conditions-sets-090.md#c-e94e4434a857d886) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-6dbe0067bc4c2181](../../evidence/state_effects-sets-023.md#s-6dbe0067bc4c2181)

### static_slot_creation_candidates-004271

```text
(config-connection)# redundancy all-active replicate <cr>
```

Handler ` RVA 0x1A9F9DE0 `；selector ` 13 `；EOL ` RVA 0x369997A0 `。

模式根 ` RVA 0x369980B8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-8e7981e23c84363d](../../evidence/conditional_registrations-sets-002.md#r-8e7981e23c84363d) · [条件 C-96884d61f94af477](../../evidence/conditions-sets-058.md#c-96884d61f94af477) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### static_slot_creation_candidates-004285

```text
(config-connection)# remote circuit id <number:dynamic> <cr>
```

Handler ` RVA 0x1A9F9DE0 `；selector ` 7 `；EOL ` RVA 0x369982E8 `。

模式根 ` RVA 0x369980B8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Remote circuit ID。

[候选注册 R-8e7981e23c84363d](../../evidence/conditional_registrations-sets-002.md#r-8e7981e23c84363d) · [条件 C-9deef6c929ff1708](../../evidence/conditions-sets-061.md#c-9deef6c929ff1708) · [缺口 G-c17b7dfae3b71841](../../evidence/gaps-sets-007.md#g-c17b7dfae3b71841) · [参数 P-d3eda7fc2b83442c](../../evidence/parameters-sets-016.md#p-d3eda7fc2b83442c)

### static_slot_creation_candidates-004277

```text
(config-connection)# remote link failure notification <cr>
```

Handler ` RVA 0x1A9F9DE0 `；selector ` 9 `；EOL ` RVA 0x36998640 `。

模式根 ` RVA 0x369980B8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-8e7981e23c84363d](../../evidence/conditional_registrations-sets-002.md#r-8e7981e23c84363d) · [条件 C-e94e4434a857d886](../../evidence/conditions-sets-090.md#c-e94e4434a857d886) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

