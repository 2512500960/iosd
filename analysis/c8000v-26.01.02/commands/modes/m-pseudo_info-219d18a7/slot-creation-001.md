# pseudo_info · 依赖静态建槽的条件安装

[模式索引](README.md) · [总索引](../../README.md)

### static_slot_creation_candidates-004236

```text
(config-pseudo)# abort <cr>
```

Handler ` RVA 0x174A4E20 `；selector ` 10 `；EOL ` RVA 0x363F9500 `。

模式根 ` RVA 0x363F9190 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-0778f1ad10c8b037](../../evidence/conditional_registrations-sets-001.md#r-0778f1ad10c8b037) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### static_slot_creation_candidates-004240

```text
(config-pseudo)# mst <string> cost <number:0..200000000> <cr>
```

Handler ` RVA 0x174A4E20 `；selector ` 6 `；EOL ` RVA 0x363F9930 `。

模式根 ` RVA 0x363F9190 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` MST instance list, example 0, 2-4,6,8-12；` unsigned_number ` change the pseudo-info path cost for an instance。

[候选注册 R-0778f1ad10c8b037](../../evidence/conditional_registrations-sets-001.md#r-0778f1ad10c8b037) · [条件 C-3806fdbf12679a14](../../evidence/conditions-sets-022.md#c-3806fdbf12679a14) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-0d108864af2d4e10](../../evidence/parameters-sets-001.md#p-0d108864af2d4e10)

### static_slot_creation_candidates-004242

```text
(config-pseudo)# mst <string> root <number:0..61440> <address> <cr>
```

Handler ` RVA 0x174A4E20 `；selector ` 5 `；EOL ` RVA 0x363F9CD0 `。

模式根 ` RVA 0x363F9190 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` MST instance list, example 0, 2-4,6,8-12；` unsigned_number ` root-bridge priority in increments of 4096；` address ` MAC Address。

[候选注册 R-0778f1ad10c8b037](../../evidence/conditional_registrations-sets-001.md#r-0778f1ad10c8b037) · [条件 C-fffa8082e812b45d](../../evidence/conditions-sets-099.md#c-fffa8082e812b45d) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-018a0f01669941c0](../../evidence/parameters-sets-001.md#p-018a0f01669941c0)

### static_slot_creation_candidates-004243

```text
(config-pseudo)# mst <string> root mac-address <address> <cr>
```

Handler ` RVA 0x174A4E20 `；selector ` 4 `；EOL ` RVA 0x363F9FB8 `。

模式根 ` RVA 0x363F9190 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` MST instance list, example 0, 2-4,6,8-12；` address ` MAC Address。

[候选注册 R-0778f1ad10c8b037](../../evidence/conditional_registrations-sets-001.md#r-0778f1ad10c8b037) · [条件 C-fffa8082e812b45d](../../evidence/conditions-sets-099.md#c-fffa8082e812b45d) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-e57f5d83b64ae926](../../evidence/parameters-sets-017.md#p-e57f5d83b64ae926)

### static_slot_creation_candidates-004244

```text
(config-pseudo)# mst <string> root priority <number:0..61440> <cr>
```

Handler ` RVA 0x174A4E20 `；selector ` 3 `；EOL ` RVA 0x363FA2A0 `。

模式根 ` RVA 0x363F9190 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` MST instance list, example 0, 2-4,6,8-12；` unsigned_number ` limited to the range of 0 to 61440 in increments of 4096。

[候选注册 R-0778f1ad10c8b037](../../evidence/conditional_registrations-sets-001.md#r-0778f1ad10c8b037) · [条件 C-1eddab3eea670fc1](../../evidence/conditions-sets-012.md#c-1eddab3eea670fc1) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-534ba542b2bf014a](../../evidence/parameters-sets-007.md#p-534ba542b2bf014a)

### static_slot_creation_candidates-004237

```text
(config-pseudo)# mst region-id <number:0..255> <cr>
```

Handler ` RVA 0x174A4E20 `；selector ` 2 `；EOL ` RVA 0x363F98B0 `。

模式根 ` RVA 0x363F9190 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` assign the MST region of the pseudo-info。

[候选注册 R-0778f1ad10c8b037](../../evidence/conditional_registrations-sets-001.md#r-0778f1ad10c8b037) · [条件 C-080c961a9b96e66c](../../evidence/conditions-sets-003.md#c-080c961a9b96e66c) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-58fca4f7b6cbaa3c](../../evidence/parameters-sets-007.md#p-58fca4f7b6cbaa3c)

### static_slot_creation_candidates-004241

```text
(config-pseudo)# no mst <string> <cr>
```

Handler ` RVA 0x174A4E20 `；selector ` 7 `；EOL ` RVA 0x363F9958 `。

模式根 ` RVA 0x363F9190 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` MST instance list, example 0, 2-4,6,8-12。

[候选注册 R-0778f1ad10c8b037](../../evidence/conditional_registrations-sets-001.md#r-0778f1ad10c8b037) · [条件 C-687d32b36c1e5ffe](../../evidence/conditions-sets-040.md#c-687d32b36c1e5ffe) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-bb585cbe28a210f9](../../evidence/parameters-sets-014.md#p-bb585cbe28a210f9) · [状态效果 S-0cdeb7841778186d](../../evidence/state_effects-sets-003.md#s-0cdeb7841778186d)

### static_slot_creation_candidates-004239

```text
(config-pseudo)# no mst region-id <cr>
```

Handler ` RVA 0x174A4E20 `；selector ` 2 `；EOL ` RVA 0x363F98B0 `。

模式根 ` RVA 0x363F9190 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-0778f1ad10c8b037](../../evidence/conditional_registrations-sets-001.md#r-0778f1ad10c8b037) · [条件 C-909bff585137c05b](../../evidence/conditions-sets-056.md#c-909bff585137c05b) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-0cdeb7841778186d](../../evidence/state_effects-sets-003.md#s-0cdeb7841778186d)

### static_slot_creation_candidates-004238

```text
(config-pseudo)# no remote-id <cr>
```

Handler ` RVA 0x174A4E20 `；selector ` 1 `；EOL ` RVA 0x363F9848 `。

模式根 ` RVA 0x363F9190 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-0778f1ad10c8b037](../../evidence/conditional_registrations-sets-001.md#r-0778f1ad10c8b037) · [条件 C-9c6e7cee8b50c339](../../evidence/conditions-sets-060.md#c-9c6e7cee8b50c339) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-0cdeb7841778186d](../../evidence/state_effects-sets-003.md#s-0cdeb7841778186d)

### static_slot_creation_candidates-004235

```text
(config-pseudo)# remote-id <number:1..256> <cr>
```

Handler ` RVA 0x174A4E20 `；selector ` 1 `；EOL ` RVA 0x363F9848 `。

模式根 ` RVA 0x363F9190 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` config the remote pseudo-info ID paired with this pseudo ID。

[候选注册 R-0778f1ad10c8b037](../../evidence/conditional_registrations-sets-001.md#r-0778f1ad10c8b037) · [条件 C-82e810a75100e4f3](../../evidence/conditions-sets-051.md#c-82e810a75100e4f3) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-c87e26d6ff7e2520](../../evidence/parameters-sets-015.md#p-c87e26d6ff7e2520)
