# exec · 六个基础模式的历史连接

[模式索引](README.md) · [总索引](../../README.md)

### path-008785

```text
(exec)# debug hw-module all oir plugin <cr>
```

Handler ` RVA 0xEEDD100 `；selector ` 0 `；EOL ` RVA 0x34464A78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-80a286e5bfdfe0fc](../../evidence/conditions-sets-050.md#c-80a286e5bfdfe0fc) · [状态效果 S-fc0c4cf3f417d495](../../evidence/state_effects-sets-053.md#s-fc0c4cf3f417d495)

### path-008772

```text
(exec)# debug hw-module all oir redundancy <cr>
```

Handler ` RVA 0xEEDCE50 `；selector ` 2 `；EOL ` RVA 0x34463FD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-45df1014545f4430](../../evidence/conditions-sets-027.md#c-45df1014545f4430) · [状态效果 S-7914ff0d56b05a52](../../evidence/state_effects-sets-026.md#s-7914ff0d56b05a52)

### path-008736

```text
(exec)# debug hw-module all oir state-machine <cr>
```

Handler ` RVA 0xEEDD8F0 `；selector ` 2 `；EOL ` RVA 0x34464280 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-80a286e5bfdfe0fc](../../evidence/conditions-sets-050.md#c-80a286e5bfdfe0fc) · [状态效果 S-7914ff0d56b05a52](../../evidence/state_effects-sets-026.md#s-7914ff0d56b05a52)

### path-021449

```text
(exec)# debug hw-module subslot <?slotcard_func_action@5555899c1038> all environment <cr>
```

Handler ` RVA 0xEEDAF60 `；selector ` 0 `；EOL ` RVA 0x34462FB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ea93032ebc3c4eb0](../../evidence/conditions-sets-091.md#c-ea93032ebc3c4eb0) · [缺口 G-104a49d9e711f8c3](../../evidence/gaps-sets-001.md#g-104a49d9e711f8c3) · [状态效果 S-ca71d5840b775e59](../../evidence/state_effects-sets-043.md#s-ca71d5840b775e59)

### path-021435

```text
(exec)# debug hw-module subslot <?slotcard_func_action@5555899c1038> all errors <cr>
```

Handler ` RVA 0xEEDD100 `；selector ` 0 `；EOL ` RVA 0x34475E88 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-fcdf6a2bb3dc9e95](../../evidence/conditions-sets-098.md#c-fcdf6a2bb3dc9e95) · [缺口 G-104a49d9e711f8c3](../../evidence/gaps-sets-001.md#g-104a49d9e711f8c3) · [状态效果 S-7cc2679ee7f4d0db](../../evidence/state_effects-sets-026.md#s-7cc2679ee7f4d0db)

### path-024678

```text
(exec)# debug hw-module subslot <?slotcard_func_action@5555899c1038> all ipcshim <number:0..15> <number:0..255> <cr>
```

Handler ` RVA 0xEE948B0 `；selector ` 0 `；EOL ` RVA 0x34453538 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Shim IPC application id；` unsigned_number ` Debug level bitmask。

[条件 C-5297218c8dbc9326](../../evidence/conditions-sets-032.md#c-5297218c8dbc9326) · [缺口 G-104a49d9e711f8c3](../../evidence/gaps-sets-001.md#g-104a49d9e711f8c3) · [参数 P-ac1f0522a3cc46fd](../../evidence/parameters-sets-013.md#p-ac1f0522a3cc46fd) · [状态效果 S-ca71d5840b775e59](../../evidence/state_effects-sets-043.md#s-ca71d5840b775e59)

### path-023717

```text
(exec)# debug hw-module subslot <?slotcard_func_action@5555899c1038> all oir entity <cr>
```

Handler ` RVA 0xEEDD8F0 `；selector ` 4 `；EOL ` RVA 0x34464528 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c42b6e9a2abf661e](../../evidence/conditions-sets-076.md#c-c42b6e9a2abf661e) · [缺口 G-104a49d9e711f8c3](../../evidence/gaps-sets-001.md#g-104a49d9e711f8c3) · [状态效果 S-9cf7ca86e20d602a](../../evidence/state_effects-sets-033.md#s-9cf7ca86e20d602a)

### path-023718

```text
(exec)# debug hw-module subslot <?slotcard_func_action@5555899c1038> all oir error <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x34463D30 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-46d99af4ed3654c0](../../evidence/conditions-sets-028.md#c-46d99af4ed3654c0) · [缺口 G-104a49d9e711f8c3](../../evidence/gaps-sets-001.md#g-104a49d9e711f8c3) · [状态效果 S-9cf7ca86e20d602a](../../evidence/state_effects-sets-033.md#s-9cf7ca86e20d602a)

### path-023735

```text
(exec)# debug hw-module subslot <?slotcard_func_action@5555899c1038> all oir failure <cr>
```

Handler ` RVA 0xEEDD8F0 `；selector ` 8 `；EOL ` RVA 0x344647D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c42b6e9a2abf661e](../../evidence/conditions-sets-076.md#c-c42b6e9a2abf661e) · [缺口 G-104a49d9e711f8c3](../../evidence/gaps-sets-001.md#g-104a49d9e711f8c3) · [状态效果 S-9cf7ca86e20d602a](../../evidence/state_effects-sets-033.md#s-9cf7ca86e20d602a)

### path-023694

```text
(exec)# debug hw-module subslot <?slotcard_func_action@5555899c1038> all oir message <cr>
```

Handler ` RVA 0xEEDCE50 `；selector ` 0 `；EOL ` RVA 0x34463A88 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-46d99af4ed3654c0](../../evidence/conditions-sets-028.md#c-46d99af4ed3654c0) · [缺口 G-104a49d9e711f8c3](../../evidence/gaps-sets-001.md#g-104a49d9e711f8c3) · [状态效果 S-9cf7ca86e20d602a](../../evidence/state_effects-sets-033.md#s-9cf7ca86e20d602a)

### path-023749

```text
(exec)# debug hw-module subslot <?slotcard_func_action@5555899c1038> all oir plugin <cr>
```

Handler ` RVA 0xEEDD100 `；selector ` 0 `；EOL ` RVA 0x34464A78 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c42b6e9a2abf661e](../../evidence/conditions-sets-076.md#c-c42b6e9a2abf661e) · [缺口 G-104a49d9e711f8c3](../../evidence/gaps-sets-001.md#g-104a49d9e711f8c3) · [状态效果 S-c4d564f40e9eb99a](../../evidence/state_effects-sets-042.md#s-c4d564f40e9eb99a)

### path-023736

```text
(exec)# debug hw-module subslot <?slotcard_func_action@5555899c1038> all oir redundancy <cr>
```

Handler ` RVA 0xEEDCE50 `；selector ` 2 `；EOL ` RVA 0x34463FD8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-46d99af4ed3654c0](../../evidence/conditions-sets-028.md#c-46d99af4ed3654c0) · [缺口 G-104a49d9e711f8c3](../../evidence/gaps-sets-001.md#g-104a49d9e711f8c3) · [状态效果 S-9cf7ca86e20d602a](../../evidence/state_effects-sets-033.md#s-9cf7ca86e20d602a)

### path-023693

```text
(exec)# debug hw-module subslot <?slotcard_func_action@5555899c1038> all oir state-machine <cr>
```

Handler ` RVA 0xEEDD8F0 `；selector ` 2 `；EOL ` RVA 0x34464280 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c42b6e9a2abf661e](../../evidence/conditions-sets-076.md#c-c42b6e9a2abf661e) · [缺口 G-104a49d9e711f8c3](../../evidence/gaps-sets-001.md#g-104a49d9e711f8c3) · [状态效果 S-9cf7ca86e20d602a](../../evidence/state_effects-sets-033.md#s-9cf7ca86e20d602a)

### path-002368

```text
(exec)# debug icm all <cr>
```

Handler ` RVA 0xC2FB130 `；selector ` 0 `；EOL ` RVA 0x33A40B48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-0279132cf9e6b9e3](../../evidence/state_effects-sets-001.md#s-0279132cf9e6b9e3)

### path-000471

```text
(exec)# debug idbgroup <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x33C2A760 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-880107879ba67e17](../../evidence/state_effects-sets-029.md#s-880107879ba67e17)

### path-000420

```text
(exec)# debug identity <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x33BE3F00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-33194f9548f922d3](../../evidence/state_effects-sets-011.md#s-33194f9548f922d3)

### path-003135

```text
(exec)# debug idmgr core <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x34229340 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-364653217fe2d032](../../evidence/state_effects-sets-012.md#s-364653217fe2d032)

### path-003090

```text
(exec)# debug idmgr data <cr>
```

Handler ` RVA 0xE002120 `；selector ` 4 `；EOL ` RVA 0x34228DF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-364653217fe2d032](../../evidence/state_effects-sets-012.md#s-364653217fe2d032)

### path-003109

```text
(exec)# debug idmgr db <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x34229098 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-364653217fe2d032](../../evidence/state_effects-sets-012.md#s-364653217fe2d032)

### path-003169

```text
(exec)# debug idmgr elog <cr>
```

Handler ` RVA 0xE002120 `；selector ` 3 `；EOL ` RVA 0x342298E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-364653217fe2d032](../../evidence/state_effects-sets-012.md#s-364653217fe2d032)

### path-007167

```text
(exec)# debug idmgr flow local <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x34229650 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-364653217fe2d032](../../evidence/state_effects-sets-012.md#s-364653217fe2d032)

### path-004765

```text
(exec)# debug if-mgr errors acp <cr>
```

Handler ` RVA 0xE002120 `；selector ` 4 `；EOL ` RVA 0x33A31690 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-e94322cd34c279d8](../../evidence/state_effects-sets-049.md#s-e94322cd34c279d8)

### path-004724

```text
(exec)# debug if-mgr errors all <cr>
```

Handler ` RVA 0xC2B19B0 `；selector ` 0 `；EOL ` RVA 0x33A31140 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-e94322cd34c279d8](../../evidence/state_effects-sets-049.md#s-e94322cd34c279d8)

### path-004977

```text
(exec)# debug if-mgr errors caim <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x33A33670 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-e94322cd34c279d8](../../evidence/state_effects-sets-049.md#s-e94322cd34c279d8)

### path-004813

```text
(exec)# debug if-mgr errors client <cr>
```

Handler ` RVA 0xE002120 `；selector ` 7 `；EOL ` RVA 0x33A31E88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-e94322cd34c279d8](../../evidence/state_effects-sets-049.md#s-e94322cd34c279d8)

### path-004747

```text
(exec)# debug if-mgr errors db <cr>
```

Handler ` RVA 0xE002120 `；selector ` 3 `；EOL ` RVA 0x33A313E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-e94322cd34c279d8](../../evidence/state_effects-sets-049.md#s-e94322cd34c279d8)

### path-004782

```text
(exec)# debug if-mgr errors driver <cr>
```

Handler ` RVA 0xE002120 `；selector ` 5 `；EOL ` RVA 0x33A31938 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-e94322cd34c279d8](../../evidence/state_effects-sets-049.md#s-e94322cd34c279d8)

### path-005035

```text
(exec)# debug if-mgr errors efp-ext <cr>
```

Handler ` RVA 0xE002120 `；selector ` 17 `；EOL ` RVA 0x33A33E68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-e94322cd34c279d8](../../evidence/state_effects-sets-049.md#s-e94322cd34c279d8)

### path-004844

```text
(exec)# debug if-mgr errors enet-ext <cr>
```

Handler ` RVA 0xE002120 `；selector ` 10 `；EOL ` RVA 0x33A323D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-e94322cd34c279d8](../../evidence/state_effects-sets-049.md#s-e94322cd34c279d8)

### path-004941

```text
(exec)# debug if-mgr errors event <cr>
```

Handler ` RVA 0xE002120 `；selector ` 15 `；EOL ` RVA 0x33A33120 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-e94322cd34c279d8](../../evidence/state_effects-sets-049.md#s-e94322cd34c279d8)

### path-004796

```text
(exec)# debug if-mgr errors extension <cr>
```

Handler ` RVA 0xE002120 `；selector ` 6 `；EOL ` RVA 0x33A31BE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-e94322cd34c279d8](../../evidence/state_effects-sets-049.md#s-e94322cd34c279d8)

### path-004828

```text
(exec)# debug if-mgr errors ifIndex <cr>
```

Handler ` RVA 0xE002120 `；selector ` 8 `；EOL ` RVA 0x33A32130 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-e94322cd34c279d8](../../evidence/state_effects-sets-049.md#s-e94322cd34c279d8)

### path-005077

```text
(exec)# debug if-mgr errors legacy <cr>
```

Handler ` RVA 0xE002120 `；selector ` 18 `；EOL ` RVA 0x33AE2DB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-e94322cd34c279d8](../../evidence/state_effects-sets-049.md#s-e94322cd34c279d8)

### path-005017

```text
(exec)# debug if-mgr errors otn-ext <cr>
```

Handler ` RVA 0xE002120 `；selector ` 9 `；EOL ` RVA 0x33A33BC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-e94322cd34c279d8](../../evidence/state_effects-sets-049.md#s-e94322cd34c279d8)

### path-004880

```text
(exec)# debug if-mgr errors port-channel-ext <cr>
```

Handler ` RVA 0xE002120 `；selector ` 12 `；EOL ` RVA 0x33A32928 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-e94322cd34c279d8](../../evidence/state_effects-sets-049.md#s-e94322cd34c279d8)

### path-004905

```text
(exec)# debug if-mgr errors sig <cr>
```

Handler ` RVA 0xE002120 `；selector ` 13 `；EOL ` RVA 0x33A32BD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-e94322cd34c279d8](../../evidence/state_effects-sets-049.md#s-e94322cd34c279d8)

### path-004926

```text
(exec)# debug if-mgr errors stack <cr>
```

Handler ` RVA 0xE002120 `；selector ` 14 `；EOL ` RVA 0x33A32E78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-e94322cd34c279d8](../../evidence/state_effects-sets-049.md#s-e94322cd34c279d8)

### path-004962

```text
(exec)# debug if-mgr errors table-db <cr>
```

Handler ` RVA 0xE002120 `；selector ` 16 `；EOL ` RVA 0x33A333C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-e94322cd34c279d8](../../evidence/state_effects-sets-049.md#s-e94322cd34c279d8)

### path-005000

```text
(exec)# debug if-mgr errors tunnel-ext <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x33A33918 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-e94322cd34c279d8](../../evidence/state_effects-sets-049.md#s-e94322cd34c279d8)

### path-004858

```text
(exec)# debug if-mgr errors vlan-ext <cr>
```

Handler ` RVA 0xE002120 `；selector ` 11 `；EOL ` RVA 0x33A32680 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-e94322cd34c279d8](../../evidence/state_effects-sets-049.md#s-e94322cd34c279d8)

### path-004750

```text
(exec)# debug if-mgr trace acp <cr>
```

Handler ` RVA 0xE002120 `；selector ` 4 `；EOL ` RVA 0x33A2E5C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-add2fd384ba2c22f](../../evidence/state_effects-sets-037.md#s-add2fd384ba2c22f)

### path-004705

```text
(exec)# debug if-mgr trace all <cr>
```

Handler ` RVA 0xC2B1910 `；selector ` 0 `；EOL ` RVA 0x33A2E070 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-add2fd384ba2c22f](../../evidence/state_effects-sets-037.md#s-add2fd384ba2c22f)

### path-004963

```text
(exec)# debug if-mgr trace caim <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x33A305A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-add2fd384ba2c22f](../../evidence/state_effects-sets-037.md#s-add2fd384ba2c22f)

### path-004797

```text
(exec)# debug if-mgr trace client <cr>
```

Handler ` RVA 0xE002120 `；selector ` 7 `；EOL ` RVA 0x33A2EDB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-add2fd384ba2c22f](../../evidence/state_effects-sets-037.md#s-add2fd384ba2c22f)

### path-004730

```text
(exec)# debug if-mgr trace db <cr>
```

Handler ` RVA 0xE002120 `；selector ` 3 `；EOL ` RVA 0x33A2E318 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-add2fd384ba2c22f](../../evidence/state_effects-sets-037.md#s-add2fd384ba2c22f)

### path-004766

```text
(exec)# debug if-mgr trace driver <cr>
```

Handler ` RVA 0xE002120 `；selector ` 5 `；EOL ` RVA 0x33A2E868 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-add2fd384ba2c22f](../../evidence/state_effects-sets-037.md#s-add2fd384ba2c22f)

### path-005018

```text
(exec)# debug if-mgr trace efp-ext <cr>
```

Handler ` RVA 0xE002120 `；selector ` 17 `；EOL ` RVA 0x33A30D98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-add2fd384ba2c22f](../../evidence/state_effects-sets-037.md#s-add2fd384ba2c22f)

### path-004829

```text
(exec)# debug if-mgr trace enet-ext <cr>
```

Handler ` RVA 0xE002120 `；selector ` 10 `；EOL ` RVA 0x33A2F308 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-add2fd384ba2c22f](../../evidence/state_effects-sets-037.md#s-add2fd384ba2c22f)

### path-004927

```text
(exec)# debug if-mgr trace event <cr>
```

Handler ` RVA 0xE002120 `；selector ` 15 `；EOL ` RVA 0x33A30050 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-add2fd384ba2c22f](../../evidence/state_effects-sets-037.md#s-add2fd384ba2c22f)

### path-004783

```text
(exec)# debug if-mgr trace extension <cr>
```

Handler ` RVA 0xE002120 `；selector ` 6 `；EOL ` RVA 0x33A2EB10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-add2fd384ba2c22f](../../evidence/state_effects-sets-037.md#s-add2fd384ba2c22f)

### path-004814

```text
(exec)# debug if-mgr trace ifIndex <cr>
```

Handler ` RVA 0xE002120 `；selector ` 8 `；EOL ` RVA 0x33A2F060 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-add2fd384ba2c22f](../../evidence/state_effects-sets-037.md#s-add2fd384ba2c22f)

### path-005082

```text
(exec)# debug if-mgr trace legacy <cr>
```

Handler ` RVA 0xE002120 `；selector ` 18 `；EOL ` RVA 0x33AE30D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-add2fd384ba2c22f](../../evidence/state_effects-sets-037.md#s-add2fd384ba2c22f)

### path-008719

```text
(exec)# debug if-mgr trace legacy pkts <cr>
```

Handler ` RVA 0xE002120 `；selector ` 19 `；EOL ` RVA 0x33AE30B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-add2fd384ba2c22f](../../evidence/state_effects-sets-037.md#s-add2fd384ba2c22f)

### path-005001

```text
(exec)# debug if-mgr trace otn-ext <cr>
```

Handler ` RVA 0xE002120 `；selector ` 9 `；EOL ` RVA 0x33A30AF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-add2fd384ba2c22f](../../evidence/state_effects-sets-037.md#s-add2fd384ba2c22f)

### path-004859

```text
(exec)# debug if-mgr trace port-channel-ext <cr>
```

Handler ` RVA 0xE002120 `；selector ` 12 `；EOL ` RVA 0x33A2F858 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-add2fd384ba2c22f](../../evidence/state_effects-sets-037.md#s-add2fd384ba2c22f)

### path-004881

```text
(exec)# debug if-mgr trace sig <cr>
```

Handler ` RVA 0xE002120 `；selector ` 13 `；EOL ` RVA 0x33A2FB00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-add2fd384ba2c22f](../../evidence/state_effects-sets-037.md#s-add2fd384ba2c22f)

### path-004906

```text
(exec)# debug if-mgr trace stack <cr>
```

Handler ` RVA 0xE002120 `；selector ` 14 `；EOL ` RVA 0x33A2FDA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-add2fd384ba2c22f](../../evidence/state_effects-sets-037.md#s-add2fd384ba2c22f)

### path-004942

```text
(exec)# debug if-mgr trace table-db <cr>
```

Handler ` RVA 0xE002120 `；selector ` 16 `；EOL ` RVA 0x33A302F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-add2fd384ba2c22f](../../evidence/state_effects-sets-037.md#s-add2fd384ba2c22f)

### path-004978

```text
(exec)# debug if-mgr trace tunnel-ext <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x33A30848 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-add2fd384ba2c22f](../../evidence/state_effects-sets-037.md#s-add2fd384ba2c22f)

### path-004845

```text
(exec)# debug if-mgr trace vlan-ext <cr>
```

Handler ` RVA 0xE002120 `；selector ` 11 `；EOL ` RVA 0x33A2F5B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-add2fd384ba2c22f](../../evidence/state_effects-sets-037.md#s-add2fd384ba2c22f)

### path-003581

```text
(exec)# debug ifs agent <cr>
```

Handler ` RVA 0xE002120 `；selector ` 4 `；EOL ` RVA 0x33EB4B78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-eca29c2b5f02cc6e](../../evidence/state_effects-sets-050.md#s-eca29c2b5f02cc6e)

### path-007501

```text
(exec)# debug ifs agent detail <cr>
```

Handler ` RVA 0xE002120 `；selector ` 5 `；EOL ` RVA 0x33EB4B50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-eca29c2b5f02cc6e](../../evidence/state_effects-sets-050.md#s-eca29c2b5f02cc6e)

### path-003552

```text
(exec)# debug ifs file <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x33EB4598 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-eca29c2b5f02cc6e](../../evidence/state_effects-sets-050.md#s-eca29c2b5f02cc6e)

### path-003541

```text
(exec)# debug ifs fs <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x33EB42F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-eca29c2b5f02cc6e](../../evidence/state_effects-sets-050.md#s-eca29c2b5f02cc6e)

### path-003588

```text
(exec)# debug ifs image <cr>
```

Handler ` RVA 0xE002120 `；selector ` 7 `；EOL ` RVA 0x33EB52F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-eca29c2b5f02cc6e](../../evidence/state_effects-sets-050.md#s-eca29c2b5f02cc6e)

### path-003578

```text
(exec)# debug ifs rfs <cr>
```

Handler ` RVA 0xE002120 `；selector ` 6 `；EOL ` RVA 0x33EB5048 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-eca29c2b5f02cc6e](../../evidence/state_effects-sets-050.md#s-eca29c2b5f02cc6e)

### path-003560

```text
(exec)# debug ifs verbose <cr>
```

Handler ` RVA 0xE002120 `；selector ` 3 `；EOL ` RVA 0x33EB4840 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-eca29c2b5f02cc6e](../../evidence/state_effects-sets-050.md#s-eca29c2b5f02cc6e)

### path-001264

```text
(exec)# debug ilpower ILP <cr>
```

Handler ` RVA 0xE002120 `；selector ` 12 `；EOL ` RVA 0x35E9BD18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d024f7175a476058](../../evidence/conditions-sets-080.md#c-d024f7175a476058) · [状态效果 S-75a40fcf6a58b121](../../evidence/state_effects-sets-025.md#s-75a40fcf6a58b121)

### path-001237

```text
(exec)# debug ilpower cdp <cr>
```

Handler ` RVA 0xE002120 `；selector ` 6 `；EOL ` RVA 0x35E9BA30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-75a40fcf6a58b121](../../evidence/state_effects-sets-025.md#s-75a40fcf6a58b121)

### path-001211

```text
(exec)# debug ilpower controller <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x35E9B4E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-75a40fcf6a58b121](../../evidence/state_effects-sets-025.md#s-75a40fcf6a58b121)

### path-001226

```text
(exec)# debug ilpower event <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x35E9B788 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-75a40fcf6a58b121](../../evidence/state_effects-sets-025.md#s-75a40fcf6a58b121)

### path-001265

```text
(exec)# debug ilpower ha <cr>
```

Handler ` RVA 0xE002120 `；selector ` 7 `；EOL ` RVA 0x35E9BFC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b4277f20c247eb6e](../../evidence/conditions-sets-070.md#c-b4277f20c247eb6e) · [状态效果 S-75a40fcf6a58b121](../../evidence/state_effects-sets-025.md#s-75a40fcf6a58b121)

### path-001341

```text
(exec)# debug ilpower ipc <cr>
```

Handler ` RVA 0xE002120 `；selector ` 11 `；EOL ` RVA 0x35E9CE60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b1625af7310decf7](../../evidence/conditions-sets-069.md#c-b1625af7310decf7) · [状态效果 S-75a40fcf6a58b121](../../evidence/state_effects-sets-025.md#s-75a40fcf6a58b121)

### path-001318

```text
(exec)# debug ilpower police <cr>
```

Handler ` RVA 0xE002120 `；selector ` 8 `；EOL ` RVA 0x35E9C590 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-56a537c07cf9516d](../../evidence/conditions-sets-034.md#c-56a537c07cf9516d) · [状态效果 S-75a40fcf6a58b121](../../evidence/state_effects-sets-025.md#s-75a40fcf6a58b121)

### path-001178

```text
(exec)# debug ilpower port <cr>
```

Handler ` RVA 0xE002120 `；selector ` 3 `；EOL ` RVA 0x35E9AF90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-75a40fcf6a58b121](../../evidence/state_effects-sets-025.md#s-75a40fcf6a58b121)

### path-001294

```text
(exec)# debug ilpower powerman <cr>
```

Handler ` RVA 0xE002120 `；selector ` 5 `；EOL ` RVA 0x35E9C2A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9b4dd3f9b220cfe1](../../evidence/conditions-sets-060.md#c-9b4dd3f9b220cfe1) · [状态效果 S-75a40fcf6a58b121](../../evidence/state_effects-sets-025.md#s-75a40fcf6a58b121)

### path-001163

```text
(exec)# debug ilpower registries <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x35E9ACE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-75a40fcf6a58b121](../../evidence/state_effects-sets-025.md#s-75a40fcf6a58b121)

### path-001195

```text
(exec)# debug ilpower scp <cr>
```

Handler ` RVA 0xE002120 `；selector ` 4 `；EOL ` RVA 0x35E9B238 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-75a40fcf6a58b121](../../evidence/state_effects-sets-025.md#s-75a40fcf6a58b121)

### path-001325

```text
(exec)# debug ilpower sense <cr>
```

Handler ` RVA 0xE002120 `；selector ` 9 `；EOL ` RVA 0x35E9C878 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-85c5e9d6f33c9f1f](../../evidence/conditions-sets-052.md#c-85c5e9d6f33c9f1f) · [状态效果 S-75a40fcf6a58b121](../../evidence/state_effects-sets-025.md#s-75a40fcf6a58b121)

### path-001352

```text
(exec)# debug ilpower upoe <cr>
```

Handler ` RVA 0xE002120 `；selector ` 10 `；EOL ` RVA 0x35E9CB60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-60c2e83aa34e1868](../../evidence/conditions-sets-038.md#c-60c2e83aa34e1868) · [状态效果 S-75a40fcf6a58b121](../../evidence/state_effects-sets-025.md#s-75a40fcf6a58b121)

### path-000099

```text
(exec)# debug inform_feature_msg <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x3419B818 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-5ddbfe9c6bf82493](../../evidence/state_effects-sets-020.md#s-5ddbfe9c6bf82493)

### path-012733

```text
(exec)# debug interface <interface> <cr>
```

Handler ` RVA 0xE015DB0 `；selector ` 0 `；EOL ` RVA 0x3416B1D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-07723650ee35b0fe](../../evidence/conditions-sets-003.md#c-07723650ee35b0fe) · [缺口 G-5d4bf1807b318ee6](../../evidence/gaps-sets-004.md#g-5d4bf1807b318ee6) · [参数 P-8e73074b682e06f5](../../evidence/parameters-sets-011.md#p-8e73074b682e06f5) · [状态效果 S-077766f1be4a182c](../../evidence/state_effects-sets-002.md#s-077766f1be4a182c)

### path-025408

```text
(exec)# debug interface <interface> vc <?number_func_nows_action@5555896bf580> <number:dynamic> <cr>
```

Handler ` RVA 0xE016CE0 `；selector ` 0 `；EOL ` RVA 0x3416B670 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` VCI。

[条件 C-4c8ee5660f07d62c](../../evidence/conditions-sets-030.md#c-4c8ee5660f07d62c) · [缺口 G-a747c70d32a9d133](../../evidence/gaps-sets-006.md#g-a747c70d32a9d133) · [参数 P-3320fcba27c4fff6](../../evidence/parameters-sets-004.md#p-3320fcba27c4fff6) · [状态效果 S-c532df47ddc81098](../../evidence/state_effects-sets-042.md#s-c532df47ddc81098)

### path-020200

```text
(exec)# debug interface <interface> vc all <cr>
```

Handler ` RVA 0xE016CE0 `；selector ` 1 `；EOL ` RVA 0x3416B978 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-42089d70ff409ae1](../../evidence/conditions-sets-026.md#c-42089d70ff409ae1) · [缺口 G-7fd03e31a30c6acf](../../evidence/gaps-sets-005.md#g-7fd03e31a30c6acf) · [参数 P-b9d84ec980aa16ea](../../evidence/parameters-sets-014.md#p-b9d84ec980aa16ea) · [状态效果 S-077766f1be4a182c](../../evidence/state_effects-sets-002.md#s-077766f1be4a182c)

### path-007529

```text
(exec)# debug interface counters exceptions <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x341D03B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-077766f1be4a182c](../../evidence/state_effects-sets-002.md#s-077766f1be4a182c)

### path-010230

```text
(exec)# debug interface counters protocol memory <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x341D06A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-077766f1be4a182c](../../evidence/state_effects-sets-002.md#s-077766f1be4a182c)

### path-007533

```text
(exec)# debug interface management etherchannel <cr>
```

Handler ` RVA 0xE002120 `；selector ` 3 `；EOL ` RVA 0x35E698E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-cbcf36ba3c550711](../../evidence/state_effects-sets-043.md#s-cbcf36ba3c550711)

### path-007559

```text
(exec)# debug interface management iif <cr>
```

Handler ` RVA 0xE002120 `；selector ` 6 `；EOL ` RVA 0x35E6A928 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-cbcf36ba3c550711](../../evidence/state_effects-sets-043.md#s-cbcf36ba3c550711)

### path-007545

```text
(exec)# debug interface management private-vlan <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x35E69E30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-cbcf36ba3c550711](../../evidence/state_effects-sets-043.md#s-cbcf36ba3c550711)

### path-007567

```text
(exec)# debug interface management provision <cr>
```

Handler ` RVA 0xE002120 `；selector ` 7 `；EOL ` RVA 0x35E6ABD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-cbcf36ba3c550711](../../evidence/state_effects-sets-043.md#s-cbcf36ba3c550711)

### path-007539

```text
(exec)# debug interface management snmp <cr>
```

Handler ` RVA 0xE002120 `；selector ` 4 `；EOL ` RVA 0x35E69B88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-cbcf36ba3c550711](../../evidence/state_effects-sets-043.md#s-cbcf36ba3c550711)

### path-010239

```text
(exec)# debug interface management switchport layer-2 <cr>
```

Handler ` RVA 0xE002120 `；selector ` 5 `；EOL ` RVA 0x35E6A140 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-cbcf36ba3c550711](../../evidence/state_effects-sets-043.md#s-cbcf36ba3c550711)

### path-010244

```text
(exec)# debug interface management switchport layer-3 <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x35E6A3E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-cbcf36ba3c550711](../../evidence/state_effects-sets-043.md#s-cbcf36ba3c550711)

### path-007552

```text
(exec)# debug interface management vlan <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x35E6A680 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-cbcf36ba3c550711](../../evidence/state_effects-sets-043.md#s-cbcf36ba3c550711)

### path-003604

```text
(exec)# debug interface states <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x341D0948 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-077766f1be4a182c](../../evidence/state_effects-sets-002.md#s-077766f1be4a182c)

### path-003611

```text
(exec)# debug interface subif-deleted <cr>
```

Handler ` RVA 0xE002120 `；selector ` 3 `；EOL ` RVA 0x341D0BF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-077766f1be4a182c](../../evidence/state_effects-sets-002.md#s-077766f1be4a182c)

### path-000404

```text
(exec)# debug iosp-server <cr>
```

Handler ` RVA 0xE8C4560 `；selector ` 0 `；EOL ` RVA 0x3433BCC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-a9219f5179bb46f2](../../evidence/state_effects-sets-036.md#s-a9219f5179bb46f2)

### path-005546

```text
(exec)# debug ip access-list compiled <cr>
```

Handler ` RVA 0xCF05BD0 `；selector ` 5 `；EOL ` RVA 0x33D61730 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-af9eb92c8872b9da](../../evidence/conditions-sets-068.md#c-af9eb92c8872b9da) · [状态效果 S-b3295956924cf560](../../evidence/state_effects-sets-038.md#s-b3295956924cf560)

### path-011071

```text
(exec)# debug ip access-list compiled context deletions <cr>
```

Handler ` RVA 0xE002120 `；selector ` 17 `；EOL ` RVA 0x33D61770 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-af9eb92c8872b9da](../../evidence/conditions-sets-068.md#c-af9eb92c8872b9da) · [状态效果 S-b3295956924cf560](../../evidence/state_effects-sets-038.md#s-b3295956924cf560)

### path-011075

```text
(exec)# debug ip access-list compiled reuse all <cr>
```

Handler ` RVA 0xCF06180 `；selector ` 0 `；EOL ` RVA 0x33D5D130 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-af9eb92c8872b9da](../../evidence/conditions-sets-068.md#c-af9eb92c8872b9da) · [状态效果 S-b3295956924cf560](../../evidence/state_effects-sets-038.md#s-b3295956924cf560)

### path-011068

```text
(exec)# debug ip access-list compiled reuse backpointers <cr>
```

Handler ` RVA 0xE002120 `；selector ` 36 `；EOL ` RVA 0x33D5CE88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-af9eb92c8872b9da](../../evidence/conditions-sets-068.md#c-af9eb92c8872b9da) · [状态效果 S-b3295956924cf560](../../evidence/state_effects-sets-038.md#s-b3295956924cf560)

### path-011784

```text
(exec)# debug ip access-list compiled reuse eligibility all <cr>
```

Handler ` RVA 0xCF06100 `；selector ` 0 `；EOL ` RVA 0x33D5D440 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-af9eb92c8872b9da](../../evidence/conditions-sets-068.md#c-af9eb92c8872b9da) · [状态效果 S-b3295956924cf560](../../evidence/state_effects-sets-038.md#s-b3295956924cf560)

### path-011796

```text
(exec)# debug ip access-list compiled reuse eligibility frees <cr>
```

Handler ` RVA 0xE002120 `；selector ` 33 `；EOL ` RVA 0x33D5DC38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-af9eb92c8872b9da](../../evidence/conditions-sets-068.md#c-af9eb92c8872b9da) · [状态效果 S-b3295956924cf560](../../evidence/state_effects-sets-038.md#s-b3295956924cf560)

### path-011792

```text
(exec)# debug ip access-list compiled reuse eligibility lost <cr>
```

Handler ` RVA 0xE002120 `；selector ` 34 `；EOL ` RVA 0x33D5D990 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-af9eb92c8872b9da](../../evidence/conditions-sets-068.md#c-af9eb92c8872b9da) · [状态效果 S-b3295956924cf560](../../evidence/state_effects-sets-038.md#s-b3295956924cf560)

### path-011787

```text
(exec)# debug ip access-list compiled reuse eligibility missing <cr>
```

Handler ` RVA 0xE002120 `；selector ` 35 `；EOL ` RVA 0x33D5D6E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-af9eb92c8872b9da](../../evidence/conditions-sets-068.md#c-af9eb92c8872b9da) · [状态效果 S-b3295956924cf560](../../evidence/state_effects-sets-038.md#s-b3295956924cf560)

### path-012026

```text
(exec)# debug ip access-list compiled reuse memory failures all <cr>
```

Handler ` RVA 0xCF06080 `；selector ` 0 `；EOL ` RVA 0x33D5DF90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-af9eb92c8872b9da](../../evidence/conditions-sets-068.md#c-af9eb92c8872b9da) · [状态效果 S-b3295956924cf560](../../evidence/state_effects-sets-038.md#s-b3295956924cf560)

### path-012027

```text
(exec)# debug ip access-list compiled reuse memory failures back-pointer <cr>
```

Handler ` RVA 0xE002120 `；selector ` 32 `；EOL ` RVA 0x33D5E238 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-af9eb92c8872b9da](../../evidence/conditions-sets-068.md#c-af9eb92c8872b9da) · [状态效果 S-b3295956924cf560](../../evidence/state_effects-sets-038.md#s-b3295956924cf560)

### path-012121

```text
(exec)# debug ip access-list compiled reuse memory failures deferred entry <cr>
```

Handler ` RVA 0xE002120 `；selector ` 30 `；EOL ` RVA 0x33D5E7C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-af9eb92c8872b9da](../../evidence/conditions-sets-068.md#c-af9eb92c8872b9da) · [状态效果 S-b3295956924cf560](../../evidence/state_effects-sets-038.md#s-b3295956924cf560)

### path-012119

```text
(exec)# debug ip access-list compiled reuse memory failures deferred row <cr>
```

Handler ` RVA 0xE002120 `；selector ` 31 `；EOL ` RVA 0x33D5E520 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-af9eb92c8872b9da](../../evidence/conditions-sets-068.md#c-af9eb92c8872b9da) · [状态效果 S-b3295956924cf560](../../evidence/state_effects-sets-038.md#s-b3295956924cf560)

### path-011790

```text
(exec)# debug ip access-list compiled reuse selection all <cr>
```

Handler ` RVA 0xCF06000 `；selector ` 0 `；EOL ` RVA 0x33D5EAD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-af9eb92c8872b9da](../../evidence/conditions-sets-068.md#c-af9eb92c8872b9da) · [状态效果 S-b3295956924cf560](../../evidence/state_effects-sets-038.md#s-b3295956924cf560)

### path-011801

```text
(exec)# debug ip access-list compiled reuse selection errors <cr>
```

Handler ` RVA 0xE002120 `；selector ` 27 `；EOL ` RVA 0x33D5F2C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-af9eb92c8872b9da](../../evidence/conditions-sets-068.md#c-af9eb92c8872b9da) · [状态效果 S-b3295956924cf560](../../evidence/state_effects-sets-038.md#s-b3295956924cf560)

### path-011798

```text
(exec)# debug ip access-list compiled reuse selection rows <cr>
```

Handler ` RVA 0xE002120 `；selector ` 28 `；EOL ` RVA 0x33D5F020 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-af9eb92c8872b9da](../../evidence/conditions-sets-068.md#c-af9eb92c8872b9da) · [状态效果 S-b3295956924cf560](../../evidence/state_effects-sets-038.md#s-b3295956924cf560)

### path-011794

```text
(exec)# debug ip access-list compiled reuse selection throttling <cr>
```

Handler ` RVA 0xE002120 `；selector ` 29 `；EOL ` RVA 0x33D5ED78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-af9eb92c8872b9da](../../evidence/conditions-sets-068.md#c-af9eb92c8872b9da) · [状态效果 S-b3295956924cf560](../../evidence/state_effects-sets-038.md#s-b3295956924cf560)

### path-011062

```text
(exec)# debug ip access-list compiled reuse unallocated <cr>
```

Handler ` RVA 0xE002120 `；selector ` 37 `；EOL ` RVA 0x33D5CBE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-af9eb92c8872b9da](../../evidence/conditions-sets-068.md#c-af9eb92c8872b9da) · [状态效果 S-b3295956924cf560](../../evidence/state_effects-sets-038.md#s-b3295956924cf560)

### path-011066

```text
(exec)# debug ip access-list compiled update all <cr>
```

Handler ` RVA 0xCF05F10 `；selector ` 0 `；EOL ` RVA 0x33D5F628 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-af9eb92c8872b9da](../../evidence/conditions-sets-068.md#c-af9eb92c8872b9da) · [状态效果 S-b3295956924cf560](../../evidence/state_effects-sets-038.md#s-b3295956924cf560)

### path-011078

```text
(exec)# debug ip access-list compiled update compilations <cr>
```

Handler ` RVA 0xE002120 `；selector ` 25 `；EOL ` RVA 0x33D5FB78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-af9eb92c8872b9da](../../evidence/conditions-sets-068.md#c-af9eb92c8872b9da) · [状态效果 S-b3295956924cf560](../../evidence/state_effects-sets-038.md#s-b3295956924cf560)

### path-011789

```text
(exec)# debug ip access-list compiled update entries all <cr>
```

Handler ` RVA 0xCF05DF0 `；selector ` 0 `；EOL ` RVA 0x33D60ED8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-af9eb92c8872b9da](../../evidence/conditions-sets-068.md#c-af9eb92c8872b9da) · [状态效果 S-b3295956924cf560](../../evidence/state_effects-sets-038.md#s-b3295956924cf560)

### path-011797

```text
(exec)# debug ip access-list compiled update entries available <cr>
```

Handler ` RVA 0xE002120 `；selector ` 18 `；EOL ` RVA 0x33D61428 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-af9eb92c8872b9da](../../evidence/conditions-sets-068.md#c-af9eb92c8872b9da) · [状态效果 S-b3295956924cf560](../../evidence/state_effects-sets-038.md#s-b3295956924cf560)

### path-011793

```text
(exec)# debug ip access-list compiled update entries unavailable <cr>
```

Handler ` RVA 0xE002120 `；selector ` 19 `；EOL ` RVA 0x33D61180 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-af9eb92c8872b9da](../../evidence/conditions-sets-068.md#c-af9eb92c8872b9da) · [状态效果 S-b3295956924cf560](../../evidence/state_effects-sets-038.md#s-b3295956924cf560)

### path-011073

```text
(exec)# debug ip access-list compiled update instance <cr>
```

Handler ` RVA 0xE002120 `；selector ` 26 `；EOL ` RVA 0x33D5F8D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-af9eb92c8872b9da](../../evidence/conditions-sets-068.md#c-af9eb92c8872b9da) · [状态效果 S-b3295956924cf560](../../evidence/state_effects-sets-038.md#s-b3295956924cf560)

### path-011786

```text
(exec)# debug ip access-list compiled update rows all <cr>
```

Handler ` RVA 0xCF05E60 `；selector ` 0 `；EOL ` RVA 0x33D5FE88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-af9eb92c8872b9da](../../evidence/conditions-sets-068.md#c-af9eb92c8872b9da) · [状态效果 S-b3295956924cf560](../../evidence/state_effects-sets-038.md#s-b3295956924cf560)

### path-011804

```text
(exec)# debug ip access-list compiled update rows available <cr>
```

Handler ` RVA 0xE002120 `；selector ` 20 `；EOL ` RVA 0x33D60BD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-af9eb92c8872b9da](../../evidence/conditions-sets-068.md#c-af9eb92c8872b9da) · [状态效果 S-b3295956924cf560](../../evidence/state_effects-sets-038.md#s-b3295956924cf560)

### path-011802

```text
(exec)# debug ip access-list compiled update rows discard <cr>
```

Handler ` RVA 0xE002120 `；selector ` 21 `；EOL ` RVA 0x33D60928 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-af9eb92c8872b9da](../../evidence/conditions-sets-068.md#c-af9eb92c8872b9da) · [状态效果 S-b3295956924cf560](../../evidence/state_effects-sets-038.md#s-b3295956924cf560)

### path-011799

```text
(exec)# debug ip access-list compiled update rows ignored <cr>
```

Handler ` RVA 0xE002120 `；selector ` 22 `；EOL ` RVA 0x33D60680 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-af9eb92c8872b9da](../../evidence/conditions-sets-068.md#c-af9eb92c8872b9da) · [状态效果 S-b3295956924cf560](../../evidence/state_effects-sets-038.md#s-b3295956924cf560)

### path-011795

```text
(exec)# debug ip access-list compiled update rows requeue <cr>
```

Handler ` RVA 0xE002120 `；selector ` 23 `；EOL ` RVA 0x33D603D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-af9eb92c8872b9da](../../evidence/conditions-sets-068.md#c-af9eb92c8872b9da) · [状态效果 S-b3295956924cf560](../../evidence/state_effects-sets-038.md#s-b3295956924cf560)

### path-011791

```text
(exec)# debug ip access-list compiled update rows unavailable <cr>
```

Handler ` RVA 0xE002120 `；selector ` 24 `；EOL ` RVA 0x33D60130 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-af9eb92c8872b9da](../../evidence/conditions-sets-068.md#c-af9eb92c8872b9da) · [状态效果 S-b3295956924cf560](../../evidence/state_effects-sets-038.md#s-b3295956924cf560)

### path-005458

```text
(exec)# debug ip access-list dynamic <cr>
```

Handler ` RVA 0xCF05BD0 `；selector ` 3 `；EOL ` RVA 0x33D62DD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ee62e68385945ed2](../../evidence/conditions-sets-092.md#c-ee62e68385945ed2) · [状态效果 S-b3295956924cf560](../../evidence/state_effects-sets-038.md#s-b3295956924cf560)

### path-009029

```text
(exec)# debug ip access-list fqdn all <cr>
```

Handler ` RVA 0xCF05BD0 `；selector ` 16 `；EOL ` RVA 0x33D61D98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-b3295956924cf560](../../evidence/state_effects-sets-038.md#s-b3295956924cf560)

### path-009038

```text
(exec)# debug ip access-list fqdn errors <cr>
```

Handler ` RVA 0xCF05BD0 `；selector ` 15 `；EOL ` RVA 0x33D62040 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-b3295956924cf560](../../evidence/state_effects-sets-038.md#s-b3295956924cf560)

### path-009043

```text
(exec)# debug ip access-list fqdn events <cr>
```

Handler ` RVA 0xCF05BD0 `；selector ` 14 `；EOL ` RVA 0x33D622E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-b3295956924cf560](../../evidence/state_effects-sets-038.md#s-b3295956924cf560)

### path-009050

```text
(exec)# debug ip access-list fqdn verbose <cr>
```

Handler ` RVA 0xCF05BD0 `；selector ` 13 `；EOL ` RVA 0x33D62590 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-b3295956924cf560](../../evidence/state_effects-sets-038.md#s-b3295956924cf560)

### path-005433

```text
(exec)# debug ip access-list hash-generation <cr>
```

Handler ` RVA 0xCF05BD0 `；selector ` 1 `；EOL ` RVA 0x33D62AE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-b3295956924cf560](../../evidence/state_effects-sets-038.md#s-b3295956924cf560)

### path-005459

```text
(exec)# debug ip access-list internal <cr>
```

Handler ` RVA 0xCF05BD0 `；selector ` 4 `；EOL ` RVA 0x33D63078 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-af9eb92c8872b9da](../../evidence/conditions-sets-068.md#c-af9eb92c8872b9da) · [状态效果 S-b3295956924cf560](../../evidence/state_effects-sets-038.md#s-b3295956924cf560)

### path-005477

```text
(exec)# debug ip access-list intstats <cr>
```

Handler ` RVA 0xCF05BD0 `；selector ` 0 `；EOL ` RVA 0x33D635C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-af9eb92c8872b9da](../../evidence/conditions-sets-068.md#c-af9eb92c8872b9da) · [状态效果 S-b3295956924cf560](../../evidence/state_effects-sets-038.md#s-b3295956924cf560)

### path-005470

```text
(exec)# debug ip access-list ipc <cr>
```

Handler ` RVA 0xCF05BD0 `；selector ` 6 `；EOL ` RVA 0x33D63320 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-af9eb92c8872b9da](../../evidence/conditions-sets-068.md#c-af9eb92c8872b9da) · [状态效果 S-b3295956924cf560](../../evidence/state_effects-sets-038.md#s-b3295956924cf560)

### path-005423

```text
(exec)# debug ip access-list peruser <cr>
```

Handler ` RVA 0xCF05BD0 `；selector ` 7 `；EOL ` RVA 0x33D62840 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-b3295956924cf560](../../evidence/state_effects-sets-038.md#s-b3295956924cf560)

### path-005512

```text
(exec)# debug ip access-list template <cr>
```

Handler ` RVA 0xCF05BD0 `；selector ` 12 `；EOL ` RVA 0x33D63918 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-af9eb92c8872b9da](../../evidence/conditions-sets-068.md#c-af9eb92c8872b9da) · [状态效果 S-b3295956924cf560](../../evidence/state_effects-sets-038.md#s-b3295956924cf560)

### path-009070

```text
(exec)# debug ip access-list template CRC <cr>
```

Handler ` RVA 0xCF05BD0 `；selector ` 11 `；EOL ` RVA 0x33D638F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-af9eb92c8872b9da](../../evidence/conditions-sets-068.md#c-af9eb92c8872b9da) · [状态效果 S-b3295956924cf560](../../evidence/state_effects-sets-038.md#s-b3295956924cf560)

### path-001518

```text
(exec)# debug ip address <cr>
```

Handler ` RVA 0xCF57D40 `；selector ` 34 `；EOL ` RVA 0x33D2EE88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-005612

```text
(exec)# debug ip admission all <cr>
```

Handler ` RVA 0xCBA2540 `；selector ` 19 `；EOL ` RVA 0x33BFE7B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-c5e27dba08aef8a3](../../evidence/state_effects-sets-042.md#s-c5e27dba08aef8a3)

### path-009116

```text
(exec)# debug ip amt gateway event <cr>
```

Handler ` RVA 0xBB7FAB0 `；selector ` 2 `；EOL ` RVA 0x3386C588 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a979007ddda540d8](../../evidence/conditions-sets-065.md#c-a979007ddda540d8) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-009119

```text
(exec)# debug ip amt gateway packet <cr>
```

Handler ` RVA 0xBB7FAB0 `；selector ` 0 `；EOL ` RVA 0x3386C2E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a979007ddda540d8](../../evidence/conditions-sets-065.md#c-a979007ddda540d8) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-009110

```text
(exec)# debug ip amt relay event <cr>
```

Handler ` RVA 0xBB7FAB0 `；selector ` 5 `；EOL ` RVA 0x3386BFA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a979007ddda540d8](../../evidence/conditions-sets-065.md#c-a979007ddda540d8) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-009112

```text
(exec)# debug ip amt relay packet <cr>
```

Handler ` RVA 0xBB7FAB0 `；selector ` 3 `；EOL ` RVA 0x3386BD08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a979007ddda540d8](../../evidence/conditions-sets-065.md#c-a979007ddda540d8) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-009275

```text
(exec)# debug ip bgp <address> updates <cr>
```

Handler ` RVA 0xF0453F0 `；selector ` 26 `；EOL ` RVA 0x344B9D08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` BGP neighbor address。

[条件 C-82fd5deb1bac53d4](../../evidence/conditions-sets-051.md#c-82fd5deb1bac53d4) · [参数 P-2b174f874fd916b6](../../evidence/parameters-sets-004.md#p-2b174f874fd916b6) · [状态效果 S-71e30b735b178706](../../evidence/state_effects-sets-024.md#s-71e30b735b178706)

### path-002061

```text
(exec)# debug ip bgp <cr>
```

Handler ` RVA 0xF0453F0 `；selector ` 0 `；EOL ` RVA 0x344B8C48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ed5a0510f9260a0c](../../evidence/conditions-sets-092.md#c-ed5a0510f9260a0c) · [状态效果 S-d5169b4b418ac1af](../../evidence/state_effects-sets-045.md#s-d5169b4b418ac1af)

### path-002168

```text
(exec)# debug ip bgp <cr>
```

Handler ` RVA 0xDC4B130 `；selector ` 0 `；EOL ` RVA 0x3401CB28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0afbdc993259e4de](../../evidence/conditions-sets-005.md#c-0afbdc993259e4de) · [状态效果 S-d74913909a591f60](../../evidence/state_effects-sets-046.md#s-d74913909a591f60)

### path-002217

```text
(exec)# debug ip bgp <cr>
```

Handler ` RVA 0xF0453F0 `；selector ` 0 `；EOL ` RVA 0x35530870 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08d7ba8e38806edc](../../evidence/conditions-sets-004.md#c-08d7ba8e38806edc) · [状态效果 S-d5169b4b418ac1af](../../evidence/state_effects-sets-045.md#s-d5169b4b418ac1af)

### path-005580

```text
(exec)# debug ip bgp addpath <cr>
```

Handler ` RVA 0xF0453F0 `；selector ` 1 `；EOL ` RVA 0x344B3630 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c2bd35ca257248ad](../../evidence/conditions-sets-075.md#c-c2bd35ca257248ad) · [状态效果 S-d5169b4b418ac1af](../../evidence/state_effects-sets-045.md#s-d5169b4b418ac1af)

### path-005558

```text
(exec)# debug ip bgp autordrt <cr>
```

Handler ` RVA 0xF0453F0 `；selector ` 48 `；EOL ` RVA 0x344B3C68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c2bd35ca257248ad](../../evidence/conditions-sets-075.md#c-c2bd35ca257248ad) · [状态效果 S-d5169b4b418ac1af](../../evidence/state_effects-sets-045.md#s-d5169b4b418ac1af)

### path-005974

```text
(exec)# debug ip bgp csc <cr>
```

Handler ` RVA 0xDC4B130 `；selector ` 1 `；EOL ` RVA 0x3401C858 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0afbdc993259e4de](../../evidence/conditions-sets-005.md#c-0afbdc993259e4de) · [状态效果 S-d74913909a591f60](../../evidence/state_effects-sets-046.md#s-d74913909a591f60)

### path-005979

```text
(exec)# debug ip bgp dampening <cr>
```

Handler ` RVA 0xF0453F0 `；selector ` 30 `；EOL ` RVA 0x344B9618 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-82fd5deb1bac53d4](../../evidence/conditions-sets-051.md#c-82fd5deb1bac53d4) · [状态效果 S-f22ab6fd7b679d75](../../evidence/state_effects-sets-051.md#s-f22ab6fd7b679d75)

### path-006049

```text
(exec)# debug ip bgp dampening <cr>
```

Handler ` RVA 0xF0453F0 `；selector ` 30 `；EOL ` RVA 0x3552FE18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cef0e2069a94f03b](../../evidence/conditions-sets-080.md#c-cef0e2069a94f03b) · [状态效果 S-fe84841ca81a5832](../../evidence/state_effects-sets-054.md#s-fe84841ca81a5832)

### path-005561

```text
(exec)# debug ip bgp diversepath <cr>
```

Handler ` RVA 0xF0453F0 `；selector ` 4 `；EOL ` RVA 0x344B39C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c2bd35ca257248ad](../../evidence/conditions-sets-075.md#c-c2bd35ca257248ad) · [状态效果 S-d5169b4b418ac1af](../../evidence/state_effects-sets-045.md#s-d5169b4b418ac1af)

### path-006051

```text
(exec)# debug ip bgp events <cr>
```

Handler ` RVA 0xF0453F0 `；selector ` 13 `；EOL ` RVA 0x344B8698 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c0a4b355a4470f79](../../evidence/conditions-sets-074.md#c-c0a4b355a4470f79) · [状态效果 S-d5169b4b418ac1af](../../evidence/state_effects-sets-045.md#s-d5169b4b418ac1af)

### path-009206

```text
(exec)# debug ip bgp events api <cr>
```

Handler ` RVA 0xF0453F0 `；selector ` 19 `；EOL ` RVA 0x344B6818 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-aa1509b387e49174](../../evidence/conditions-sets-066.md#c-aa1509b387e49174) · [状态效果 S-d5169b4b418ac1af](../../evidence/state_effects-sets-045.md#s-d5169b4b418ac1af)

### path-012038

```text
(exec)# debug ip bgp events crimson emulation address-family route <cr>
```

Handler ` RVA 0xF0453F0 `；selector ` 24 `；EOL ` RVA 0x344B83D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c0a4b355a4470f79](../../evidence/conditions-sets-074.md#c-c0a4b355a4470f79) · [状态效果 S-d5169b4b418ac1af](../../evidence/state_effects-sets-045.md#s-d5169b4b418ac1af)

### path-012036

```text
(exec)# debug ip bgp events crimson emulation address-family summary <cr>
```

Handler ` RVA 0xF0453F0 `；selector ` 23 `；EOL ` RVA 0x344B8130 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c0a4b355a4470f79](../../evidence/conditions-sets-074.md#c-c0a4b355a4470f79) · [状态效果 S-d5169b4b418ac1af](../../evidence/state_effects-sets-045.md#s-d5169b4b418ac1af)

### path-011836

```text
(exec)# debug ip bgp events crimson emulation neighbor <cr>
```

Handler ` RVA 0xF0453F0 `；selector ` 22 `；EOL ` RVA 0x344B7E48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c0a4b355a4470f79](../../evidence/conditions-sets-074.md#c-c0a4b355a4470f79) · [状态效果 S-d5169b4b418ac1af](../../evidence/state_effects-sets-045.md#s-d5169b4b418ac1af)

### path-009236

```text
(exec)# debug ip bgp events encap <cr>
```

Handler ` RVA 0xF0453F0 `；selector ` 17 `；EOL ` RVA 0x344B72B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-aa1509b387e49174](../../evidence/conditions-sets-066.md#c-aa1509b387e49174) · [状态效果 S-d5169b4b418ac1af](../../evidence/state_effects-sets-045.md#s-d5169b4b418ac1af)

### path-009198

```text
(exec)# debug ip bgp events nexthop <cr>
```

Handler ` RVA 0xF0453F0 `；selector ` 14 `；EOL ` RVA 0x344B6AB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-aa1509b387e49174](../../evidence/conditions-sets-066.md#c-aa1509b387e49174) · [状态效果 S-d5169b4b418ac1af](../../evidence/state_effects-sets-045.md#s-d5169b4b418ac1af)

### path-009252

```text
(exec)# debug ip bgp events overlay <cr>
```

Handler ` RVA 0xF0453F0 `；selector ` 18 `；EOL ` RVA 0x344B7598 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6daa7c2031d5b0b5](../../evidence/conditions-sets-042.md#c-6daa7c2031d5b0b5) · [状态效果 S-d5169b4b418ac1af](../../evidence/state_effects-sets-045.md#s-d5169b4b418ac1af)

### path-009266

```text
(exec)# debug ip bgp events rpki <cr>
```

Handler ` RVA 0xF0453F0 `；selector ` 20 `；EOL ` RVA 0x344B78D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c0a4b355a4470f79](../../evidence/conditions-sets-074.md#c-c0a4b355a4470f79) · [状态效果 S-d5169b4b418ac1af](../../evidence/state_effects-sets-045.md#s-d5169b4b418ac1af)

### path-011129

```text
(exec)# debug ip bgp events rpki detail <cr>
```

Handler ` RVA 0xF0453F0 `；selector ` 21 `；EOL ` RVA 0x344B78A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7758d9afcbb73a67](../../evidence/conditions-sets-046.md#c-7758d9afcbb73a67) · [状态效果 S-d5169b4b418ac1af](../../evidence/state_effects-sets-045.md#s-d5169b4b418ac1af)

### path-009220

```text
(exec)# debug ip bgp events update-source <cr>
```

Handler ` RVA 0xF0453F0 `；selector ` 16 `；EOL ` RVA 0x344B7008 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-aa1509b387e49174](../../evidence/conditions-sets-066.md#c-aa1509b387e49174) · [状态效果 S-d5169b4b418ac1af](../../evidence/state_effects-sets-045.md#s-d5169b4b418ac1af)

### path-009213

```text
(exec)# debug ip bgp events va <cr>
```

Handler ` RVA 0xF0453F0 `；selector ` 15 `；EOL ` RVA 0x344B6D60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-aa1509b387e49174](../../evidence/conditions-sets-066.md#c-aa1509b387e49174) · [状态效果 S-d5169b4b418ac1af](../../evidence/state_effects-sets-045.md#s-d5169b4b418ac1af)

### path-005752

```text
(exec)# debug ip bgp evi <cr>
```

Handler ` RVA 0xF0453F0 `；selector ` 9 `；EOL ` RVA 0x344B58E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8d2fb13f07dd0ee5](../../evidence/conditions-sets-055.md#c-8d2fb13f07dd0ee5) · [状态效果 S-d5169b4b418ac1af](../../evidence/state_effects-sets-045.md#s-d5169b4b418ac1af)

### path-009150

```text
(exec)# debug ip bgp evi context <cr>
```

Handler ` RVA 0xF0453F0 `；selector ` 8 `；EOL ` RVA 0x344B5618 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8d2fb13f07dd0ee5](../../evidence/conditions-sets-055.md#c-8d2fb13f07dd0ee5) · [状态效果 S-d5169b4b418ac1af](../../evidence/state_effects-sets-045.md#s-d5169b4b418ac1af)

### path-005827

```text
(exec)# debug ip bgp gr <cr>
```

Handler ` RVA 0xF0453F0 `；selector ` 7 `；EOL ` RVA 0x344BA170 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-dc025a4872a3cb12](../../evidence/conditions-sets-085.md#c-dc025a4872a3cb12) · [状态效果 S-d5169b4b418ac1af](../../evidence/state_effects-sets-045.md#s-d5169b4b418ac1af)

### path-005977

```text
(exec)# debug ip bgp groups <cr>
```

Handler ` RVA 0xF0453F0 `；selector ` 28 `；EOL ` RVA 0x344B99C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-82fd5deb1bac53d4](../../evidence/conditions-sets-051.md#c-82fd5deb1bac53d4) · [状态效果 S-d5169b4b418ac1af](../../evidence/state_effects-sets-045.md#s-d5169b4b418ac1af)

### path-014215

```text
(exec)# debug ip bgp igp-metric ignore <cr>
```

Handler ` RVA 0xF0453F0 `；selector ` 5 `；EOL ` RVA 0x344B4968 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-594884bdbefacfc9](../../evidence/conditions-sets-035.md#c-594884bdbefacfc9) · [缺口 G-86121c6d9b0aa295](../../evidence/gaps-sets-005.md#g-86121c6d9b0aa295) · [状态效果 S-d5169b4b418ac1af](../../evidence/state_effects-sets-045.md#s-d5169b4b418ac1af)

### path-009155

```text
(exec)# debug ip bgp import events <cr>
```

Handler ` RVA 0xF0453F0 `；selector ` 35 `；EOL ` RVA 0x344BA480 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9632b0f3fe95b24b](../../evidence/conditions-sets-058.md#c-9632b0f3fe95b24b) · [状态效果 S-d5169b4b418ac1af](../../evidence/state_effects-sets-045.md#s-d5169b4b418ac1af)

### path-009182

```text
(exec)# debug ip bgp import updates <cr>
```

Handler ` RVA 0xF0453F0 `；selector ` 36 `；EOL ` RVA 0x344BA768 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b7fb808b01907f39](../../evidence/conditions-sets-071.md#c-b7fb808b01907f39) · [状态效果 S-d5169b4b418ac1af](../../evidence/state_effects-sets-045.md#s-d5169b4b418ac1af)

### path-005826

```text
(exec)# debug ip bgp internal <cr>
```

Handler ` RVA 0xF0453F0 `；selector ` 12 `；EOL ` RVA 0x344B8998 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-dc025a4872a3cb12](../../evidence/conditions-sets-085.md#c-dc025a4872a3cb12) · [状态效果 S-d5169b4b418ac1af](../../evidence/state_effects-sets-045.md#s-d5169b4b418ac1af)

### path-005575

```text
(exec)# debug ip bgp iosp <cr>
```

Handler ` RVA 0xF0453F0 `；selector ` 50 `；EOL ` RVA 0x344B3F10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c2bd35ca257248ad](../../evidence/conditions-sets-075.md#c-c2bd35ca257248ad) · [状态效果 S-d5169b4b418ac1af](../../evidence/state_effects-sets-045.md#s-d5169b4b418ac1af)

### path-005685

```text
(exec)# debug ip bgp keepalives <cr>
```

Handler ` RVA 0xF0453F0 `；selector ` 25 `；EOL ` RVA 0x344B4C70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-37a4396cea8d6900](../../evidence/conditions-sets-022.md#c-37a4396cea8d6900) · [状态效果 S-d5169b4b418ac1af](../../evidence/state_effects-sets-045.md#s-d5169b4b418ac1af)

### path-005997

```text
(exec)# debug ip bgp labelmode <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x3401CB00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0afbdc993259e4de](../../evidence/conditions-sets-005.md#c-0afbdc993259e4de) · [状态效果 S-d74913909a591f60](../../evidence/state_effects-sets-046.md#s-d74913909a591f60)

### path-005874

```text
(exec)# debug ip bgp mpls <cr>
```

Handler ` RVA 0xF0453F0 `；selector ` 31 `；EOL ` RVA 0x344B92D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-82fd5deb1bac53d4](../../evidence/conditions-sets-051.md#c-82fd5deb1bac53d4) · [状态效果 S-d5169b4b418ac1af](../../evidence/state_effects-sets-045.md#s-d5169b4b418ac1af)

### path-005627

```text
(exec)# debug ip bgp nhrp <cr>
```

Handler ` RVA 0xF0453F0 `；selector ` 46 `；EOL ` RVA 0x344B41F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-539955c9b0c16288](../../evidence/conditions-sets-033.md#c-539955c9b0c16288) · [状态效果 S-d5169b4b418ac1af](../../evidence/state_effects-sets-045.md#s-d5169b4b418ac1af)

### path-005751

```text
(exec)# debug ip bgp nve <cr>
```

Handler ` RVA 0xF0453F0 `；selector ` 6 `；EOL ` RVA 0x344B5C58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f7d532b808ce7575](../../evidence/conditions-sets-096.md#c-f7d532b808ce7575) · [状态效果 S-d5169b4b418ac1af](../../evidence/state_effects-sets-045.md#s-d5169b4b418ac1af)

### path-005738

```text
(exec)# debug ip bgp range <cr>
```

Handler ` RVA 0xF0453F0 `；selector ` 10 `；EOL ` RVA 0x344B5260 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9cd8447714094b30](../../evidence/conditions-sets-061.md#c-9cd8447714094b30) · [状态效果 S-d5169b4b418ac1af](../../evidence/state_effects-sets-045.md#s-d5169b4b418ac1af)

### path-009137

```text
(exec)# debug ip bgp range indepth <cr>
```

Handler ` RVA 0xF0453F0 `；selector ` 11 `；EOL ` RVA 0x344B4FB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f6121fb00fd1af12](../../evidence/conditions-sets-095.md#c-f6121fb00fd1af12) · [状态效果 S-d5169b4b418ac1af](../../evidence/state_effects-sets-045.md#s-d5169b4b418ac1af)

### path-005852

```text
(exec)# debug ip bgp rib-filter <cr>
```

Handler ` RVA 0xF0453F0 `；selector ` 29 `；EOL ` RVA 0x344B9028 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-82fd5deb1bac53d4](../../evidence/conditions-sets-051.md#c-82fd5deb1bac53d4) · [状态效果 S-d5169b4b418ac1af](../../evidence/state_effects-sets-045.md#s-d5169b4b418ac1af)

### path-009247

```text
(exec)# debug ip bgp sso events <cr>
```

Handler ` RVA 0xF0453F0 `；selector ` 32 `；EOL ` RVA 0x3372D580 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-696f8ff881d0137c](../../evidence/conditions-sets-041.md#c-696f8ff881d0137c) · [状态效果 S-d5169b4b418ac1af](../../evidence/state_effects-sets-045.md#s-d5169b4b418ac1af)

### path-009255

```text
(exec)# debug ip bgp sso scale <cr>
```

Handler ` RVA 0xF0453F0 `；selector ` 34 `；EOL ` RVA 0x3372D8B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-696f8ff881d0137c](../../evidence/conditions-sets-041.md#c-696f8ff881d0137c) · [状态效果 S-d5169b4b418ac1af](../../evidence/state_effects-sets-045.md#s-d5169b4b418ac1af)

### path-009265

```text
(exec)# debug ip bgp sso transactions <cr>
```

Handler ` RVA 0xF0453F0 `；selector ` 33 `；EOL ` RVA 0x3372DB88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-696f8ff881d0137c](../../evidence/conditions-sets-041.md#c-696f8ff881d0137c) · [状态效果 S-d5169b4b418ac1af](../../evidence/state_effects-sets-045.md#s-d5169b4b418ac1af)

### path-018012

```text
(exec)# debug ip bgp topology * <cr>
```

Handler ` RVA 0xF0453F0 `；selector ` 37 `；EOL ` RVA 0x344B3268 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b205ab3c8690bbbf](../../evidence/conditions-sets-069.md#c-b205ab3c8690bbbf) · [缺口 G-8e250c5cc884ce8d](../../evidence/gaps-sets-005.md#g-8e250c5cc884ce8d) · [状态效果 S-ffa56e5e32e245ac](../../evidence/state_effects-sets-054.md#s-ffa56e5e32e245ac)

### path-009100

```text
(exec)# debug ip bgp topology <string> <cr>
```

Handler ` RVA 0xF0453F0 `；selector ` 37 `；EOL ` RVA 0x344B3268 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Routing topology instance name。

[条件 C-ef2cc05221f76016](../../evidence/conditions-sets-092.md#c-ef2cc05221f76016) · [参数 P-a4f479bee8c209f0](../../evidence/parameters-sets-013.md#p-a4f479bee8c209f0) · [状态效果 S-81105805d9a49f76](../../evidence/state_effects-sets-027.md#s-81105805d9a49f76)

### path-009125

```text
(exec)# debug ip bgp trace <number:1..65535> <cr>
```

Handler ` RVA 0xF0453F0 `；selector ` 3 `；EOL ` RVA 0x344B4530 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Specify trace buffer size in kbytes。

[条件 C-525ee75dcad8bddc](../../evidence/conditions-sets-032.md#c-525ee75dcad8bddc) · [参数 P-7d7c6c64164108ff](../../evidence/parameters-sets-010.md#p-7d7c6c64164108ff) · [状态效果 S-d5169b4b418ac1af](../../evidence/state_effects-sets-045.md#s-d5169b4b418ac1af)

### path-005954

```text
(exec)# debug ip bgp updates <cr>
```

Handler ` RVA 0xF0453F0 `；selector ` 26 `；EOL ` RVA 0x344B63F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-431b155e91917646](../../evidence/conditions-sets-026.md#c-431b155e91917646) · [状态效果 S-d5169b4b418ac1af](../../evidence/state_effects-sets-045.md#s-d5169b4b418ac1af)

### path-006177

```text
(exec)# debug ip bgp updates <cr>
```

Handler ` RVA 0xF0453F0 `；selector ` 26 `；EOL ` RVA 0x35530578 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c4586245340b356e](../../evidence/conditions-sets-076.md#c-c4586245340b356e) · [状态效果 S-d5169b4b418ac1af](../../evidence/state_effects-sets-045.md#s-d5169b4b418ac1af)

### path-009177

```text
(exec)# debug ip bgp updates events <cr>
```

Handler ` RVA 0xF0453F0 `；selector ` 27 `；EOL ` RVA 0x344B6058 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-431b155e91917646](../../evidence/conditions-sets-026.md#c-431b155e91917646) · [状态效果 S-c66da1efc5a23fe8](../../evidence/state_effects-sets-042.md#s-c66da1efc5a23fe8)

### path-009282

```text
(exec)# debug ip bgp updates events <cr>
```

Handler ` RVA 0xF0453F0 `；selector ` 27 `；EOL ` RVA 0x355301C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c4586245340b356e](../../evidence/conditions-sets-076.md#c-c4586245340b356e) · [状态效果 S-1549ce7a840359dd](../../evidence/state_effects-sets-005.md#s-1549ce7a840359dd)

### path-001729

```text
(exec)# debug ip cache <cr>
```

Handler ` RVA 0xE19E1C0 `；selector ` 51 `；EOL ` RVA 0x3423F298 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-006034

```text
(exec)# debug ip casa affinities <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x35497DC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-e2171d05ac806027](../../evidence/state_effects-sets-048.md#s-e2171d05ac806027)

### path-006110

```text
(exec)# debug ip casa errors <cr>
```

Handler ` RVA 0xE002120 `；selector ` 4 `；EOL ` RVA 0x354985B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-e2171d05ac806027](../../evidence/state_effects-sets-048.md#s-e2171d05ac806027)

### path-006156

```text
(exec)# debug ip casa interest-timeouts <cr>
```

Handler ` RVA 0xE002120 `；selector ` 3 `；EOL ` RVA 0x35498B08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-e2171d05ac806027](../../evidence/state_effects-sets-048.md#s-e2171d05ac806027)

### path-006087

```text
(exec)# debug ip casa packets <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x35498310 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-e2171d05ac806027](../../evidence/state_effects-sets-048.md#s-e2171d05ac806027)

### path-006137

```text
(exec)# debug ip casa plevel <cr>
```

Handler ` RVA 0xE002120 `；selector ` 5 `；EOL ` RVA 0x35498860 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-e2171d05ac806027](../../evidence/state_effects-sets-048.md#s-e2171d05ac806027)

### path-006060

```text
(exec)# debug ip casa wildcards <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x35498068 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-e2171d05ac806027](../../evidence/state_effects-sets-048.md#s-e2171d05ac806027)

### path-001533

```text
(exec)# debug ip cca <cr>
```

Handler ` RVA 0xE002120 `；selector ` 38 `；EOL ` RVA 0x33D2F130 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-8d5323186eacbf22](../../evidence/state_effects-sets-030.md#s-8d5323186eacbf22)

### path-001780

```text
(exec)# debug ip cgmp <cr>
```

Handler ` RVA 0xF6D8660 `；selector ` 2 `；EOL ` RVA 0x3472A248 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-006103

```text
(exec)# debug ip ddns update <cr>
```

Handler ` RVA 0xF481CC0 `；selector ` 0 `；EOL ` RVA 0x3465B9B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-006009

```text
(exec)# debug ip dfp agent <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x35445658 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-f808f34250675bb9](../../evidence/state_effects-sets-052.md#s-f808f34250675bb9)

### path-009536

```text
(exec)# debug ip dhcp server binding-store <cr>
```

Handler ` RVA 0xD24F070 `；selector ` 7 `；EOL ` RVA 0x33DD8E18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-009469

```text
(exec)# debug ip dhcp server class <cr>
```

Handler ` RVA 0xD24F070 `；selector ` 3 `；EOL ` RVA 0x33DD85C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-009403

```text
(exec)# debug ip dhcp server events <cr>
```

Handler ` RVA 0xD24F070 `；selector ` 0 `；EOL ` RVA 0x33DD7B10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-009446

```text
(exec)# debug ip dhcp server linkage <cr>
```

Handler ` RVA 0xD24F070 `；selector ` 2 `；EOL ` RVA 0x33DD8318 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-009456

```text
(exec)# debug ip dhcp server packet <cr>
```

Handler ` RVA 0xD24F070 `；selector ` 1 `；EOL ` RVA 0x33DD7E48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-011223

```text
(exec)# debug ip dhcp server packet detail <cr>
```

Handler ` RVA 0xD24F070 `；selector ` 4 `；EOL ` RVA 0x33DD7E20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-009518

```text
(exec)# debug ip dhcp server redundancy <cr>
```

Handler ` RVA 0xD24F070 `；selector ` 5 `；EOL ` RVA 0x33DD88D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-009512

```text
(exec)# debug ip dhcp server snmp <cr>
```

Handler ` RVA 0xD24F070 `；selector ` 6 `；EOL ` RVA 0x33DD8B70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-009534

```text
(exec)# debug ip dhcp sip all <cr>
```

Handler ` RVA 0xE002120 `；selector ` 4 `；EOL ` RVA 0x35448C80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-9373d972f8a4fec8](../../evidence/state_effects-sets-031.md#s-9373d972f8a4fec8)

### path-009509

```text
(exec)# debug ip dhcp sip api <cr>
```

Handler ` RVA 0xE002120 `；selector ` 3 `；EOL ` RVA 0x354489D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-9373d972f8a4fec8](../../evidence/state_effects-sets-031.md#s-9373d972f8a4fec8)

### path-009464

```text
(exec)# debug ip dhcp sip error <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x35448488 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-9373d972f8a4fec8](../../evidence/state_effects-sets-031.md#s-9373d972f8a4fec8)

### path-009440

```text
(exec)# debug ip dhcp sip event <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x354481E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-9373d972f8a4fec8](../../evidence/state_effects-sets-031.md#s-9373d972f8a4fec8)

### path-009489

```text
(exec)# debug ip dhcp sip redundancy <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x35448730 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-9373d972f8a4fec8](../../evidence/state_effects-sets-031.md#s-9373d972f8a4fec8)

### path-009491

```text
(exec)# debug ip dhcp snooping <address> <cr>
```

Handler ` RVA 0x15FA95E0 `；selector ` 0 `；EOL ` RVA 0x35E7EBC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` DHCP packet MAC address。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [参数 P-253cca93e1be63e4](../../evidence/parameters-sets-003.md#p-253cca93e1be63e4) · [状态效果 S-26560aa411aafdfc](../../evidence/state_effects-sets-009.md#s-26560aa411aafdfc)

### path-009468

```text
(exec)# debug ip dhcp snooping agent <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x35E7E918 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-26560aa411aafdfc](../../evidence/state_effects-sets-009.md#s-26560aa411aafdfc)

### path-009421

```text
(exec)# debug ip dhcp snooping event <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x35E7E3C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-26560aa411aafdfc](../../evidence/state_effects-sets-009.md#s-26560aa411aafdfc)

### path-009444

```text
(exec)# debug ip dhcp snooping packet <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x35E7E670 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-26560aa411aafdfc](../../evidence/state_effects-sets-009.md#s-26560aa411aafdfc)

### path-005691

```text
(exec)# debug ip dns name-list <cr>
```

Handler ` RVA 0xD16CC80 `；selector ` 2 `；EOL ` RVA 0x33D9BEE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-005711

```text
(exec)# debug ip dns view <cr>
```

Handler ` RVA 0xD16CC80 `；selector ` 0 `；EOL ` RVA 0x33D9C188 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-005745

```text
(exec)# debug ip dns view-list <cr>
```

Handler ` RVA 0xD16CC80 `；selector ` 1 `；EOL ` RVA 0x33D9C488 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c270a28d6364a5e2](../../evidence/conditions-sets-075.md#c-c270a28d6364a5e2) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-002010

```text
(exec)# debug ip domain <cr>
```

Handler ` RVA 0xD135EB0 `；selector ` 0 `；EOL ` RVA 0x33D97C40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-9a48ec697f5903a8](../../evidence/state_effects-sets-033.md#s-9a48ec697f5903a8)

### path-014326

```text
(exec)# debug ip domain <number:0..6> <cr>
```

Handler ` RVA 0xD135EB0 `；selector ` 0 `；EOL ` RVA 0x33D97C40 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` debugging severity level。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-b057543e84daf859](../../evidence/gaps-sets-006.md#g-b057543e84daf859) · [参数 P-96a6b5465d8c11d1](../../evidence/parameters-sets-012.md#p-96a6b5465d8c11d1) · [状态效果 S-4ba05fe6af62d1c5](../../evidence/state_effects-sets-017.md#s-4ba05fe6af62d1c5)

### path-001658

```text
(exec)# debug ip drp <cr>
```

Handler ` RVA 0xF4F1F30 `；selector ` 0 `；EOL ` RVA 0x3467AAF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-002145

```text
(exec)# debug ip eigrp <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 74 `；EOL ` RVA 0x346DA210 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e4889a16d87ee0b](../../evidence/conditions-sets-006.md#c-0e4889a16d87ee0b) · [状态效果 S-872cd1c75bad1686](../../evidence/state_effects-sets-029.md#s-872cd1c75bad1686)

### path-001572

```text
(exec)# debug ip elog <cr>
```

Handler ` RVA 0xCF57D40 `；selector ` 39 `；EOL ` RVA 0x33D2F690 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6c68018c6ae61eb3](../../evidence/conditions-sets-042.md#c-6c68018c6ae61eb3) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-001511

```text
(exec)# debug ip error <cr>
```

Handler ` RVA 0xCF57D40 `；selector ` 31 `；EOL ` RVA 0x33D2E3A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-469f4ef1a00a9850](../../evidence/conditions-sets-028.md#c-469f4ef1a00a9850) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-009486

```text
(exec)# debug ip forwarding accounting non-recursive <cr>
```

Handler ` RVA 0xB5EC0A0 `；selector ` 7 `；EOL ` RVA 0x337B39E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3e7ea930668f4ef4](../../evidence/conditions-sets-024.md#c-3e7ea930668f4ef4) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-006588

```text
(exec)# debug ip forwarding drops <cr>
```

Handler ` RVA 0xB5EC0A0 `；selector ` 1 `；EOL ` RVA 0x337B4098 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3e7ea930668f4ef4](../../evidence/conditions-sets-024.md#c-3e7ea930668f4ef4) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-009538

```text
(exec)# debug ip forwarding drops rpf <cr>
```

Handler ` RVA 0xB5EC0A0 `；selector ` 2 `；EOL ` RVA 0x337B3D40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3e7ea930668f4ef4](../../evidence/conditions-sets-024.md#c-3e7ea930668f4ef4) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-006351

```text
(exec)# debug ip forwarding events <cr>
```

Handler ` RVA 0xB5EC0A0 `；selector ` 3 `；EOL ` RVA 0x337B3110 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3e7ea930668f4ef4](../../evidence/conditions-sets-024.md#c-3e7ea930668f4ef4) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-006241

```text
(exec)# debug ip forwarding ipc <cr>
```

Handler ` RVA 0xB5EC0A0 `；selector ` 6 `；EOL ` RVA 0x337B29B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3e7ea930668f4ef4](../../evidence/conditions-sets-024.md#c-3e7ea930668f4ef4) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-006387

```text
(exec)# debug ip forwarding local <cr>
```

Handler ` RVA 0xB5EC0A0 `；selector ` 8 `；EOL ` RVA 0x337B3400 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3e7ea930668f4ef4](../../evidence/conditions-sets-024.md#c-3e7ea930668f4ef4) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-006586

```text
(exec)# debug ip forwarding packet <cr>
```

Handler ` RVA 0xB5EC0A0 `；selector ` 0 `；EOL ` RVA 0x337B45A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-42ffc3acbfeb06c4](../../evidence/conditions-sets-026.md#c-42ffc3acbfeb06c4) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-019184

```text
(exec)# debug ip forwarding packet <interface> <cr>
```

Handler ` RVA 0xB5EC0A0 `；selector ` 0 `；EOL ` RVA 0x337B45A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f4008cabbd572992](../../evidence/conditions-sets-094.md#c-f4008cabbd572992) · [缺口 G-c242418a0f3a50a8](../../evidence/gaps-sets-007.md#g-c242418a0f3a50a8) · [参数 P-e37e556e3ef6a665](../../evidence/parameters-sets-017.md#p-e37e556e3ef6a665) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-006430

```text
(exec)# debug ip forwarding receive <cr>
```

Handler ` RVA 0xB5EC0A0 `；selector ` 4 `；EOL ` RVA 0x337B2D98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3e7ea930668f4ef4](../../evidence/conditions-sets-024.md#c-3e7ea930668f4ef4) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-006422

```text
(exec)# debug ip forwarding redirect <cr>
```

Handler ` RVA 0xB5EC0A0 `；selector ` 9 `；EOL ` RVA 0x337B36F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3e7ea930668f4ef4](../../evidence/conditions-sets-024.md#c-3e7ea930668f4ef4) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-006297

```text
(exec)# debug ip forwarding subblock <cr>
```

Handler ` RVA 0xB5EC0A0 `；selector ` 5 `；EOL ` RVA 0x337B2578 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3e7ea930668f4ef4](../../evidence/conditions-sets-024.md#c-3e7ea930668f4ef4) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-001890

```text
(exec)# debug ip ftp <cr>
```

Handler ` RVA 0xCDF03D0 `；selector ` 2 `；EOL ` RVA 0x33D86930 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-005709

```text
(exec)# debug ip html forms <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x33DC4150 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-08700a3a1d8c294d](../../evidence/state_effects-sets-002.md#s-08700a3a1d8c294d)

### path-005726

```text
(exec)# debug ip html pages <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x33DC43F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-08700a3a1d8c294d](../../evidence/state_effects-sets-002.md#s-08700a3a1d8c294d)

### path-005744

```text
(exec)# debug ip html ssi <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x33DC46A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-08700a3a1d8c294d](../../evidence/state_effects-sets-002.md#s-08700a3a1d8c294d)

### path-005763

```text
(exec)# debug ip html tokens <cr>
```

Handler ` RVA 0xE002120 `；selector ` 3 `；EOL ` RVA 0x33DC4948 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-08700a3a1d8c294d](../../evidence/state_effects-sets-002.md#s-08700a3a1d8c294d)

### path-005768

```text
(exec)# debug ip http all <cr>
```

Handler ` RVA 0xD1EF660 `；selector ` 222 `；EOL ` RVA 0x33DB7898 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-8bd641b9e1218149](../../evidence/state_effects-sets-030.md#s-8bd641b9e1218149)

### path-005851

```text
(exec)# debug ip http appdetail <cr>
```

Handler ` RVA 0xE002120 `；selector ` 7 `；EOL ` RVA 0x33DB9128 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-8bd641b9e1218149](../../evidence/state_effects-sets-030.md#s-8bd641b9e1218149)

### path-005825

```text
(exec)# debug ip http appinout <cr>
```

Handler ` RVA 0xE002120 `；selector ` 6 `；EOL ` RVA 0x33DB8E80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-8bd641b9e1218149](../../evidence/state_effects-sets-030.md#s-8bd641b9e1218149)

### path-005586

```text
(exec)# debug ip http authentication <cr>
```

Handler ` RVA 0xE002120 `；selector ` 4 `；EOL ` RVA 0x33DB6060 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-8bd641b9e1218149](../../evidence/state_effects-sets-030.md#s-8bd641b9e1218149)

### path-009246

```text
(exec)# debug ip http client all <cr>
```

Handler ` RVA 0xD1EF660 `；selector ` 111 `；EOL ` RVA 0x33DB8BA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-4504041b08db87a8](../../evidence/state_effects-sets-015.md#s-4504041b08db87a8)

### path-009174

```text
(exec)# debug ip http client api <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x33DB7BB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-4504041b08db87a8](../../evidence/state_effects-sets-015.md#s-4504041b08db87a8)

### path-009189

```text
(exec)# debug ip http client cache <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x33DB7E60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-4504041b08db87a8](../../evidence/state_effects-sets-015.md#s-4504041b08db87a8)

### path-009199

```text
(exec)# debug ip http client error <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x33DB8108 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-4504041b08db87a8](../../evidence/state_effects-sets-015.md#s-4504041b08db87a8)

### path-009221

```text
(exec)# debug ip http client main <cr>
```

Handler ` RVA 0xE002120 `；selector ` 4 `；EOL ` RVA 0x33DB8658 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-4504041b08db87a8](../../evidence/state_effects-sets-015.md#s-4504041b08db87a8)

### path-009214

```text
(exec)# debug ip http client msg <cr>
```

Handler ` RVA 0xE002120 `；selector ` 3 `；EOL ` RVA 0x33DB83B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-4504041b08db87a8](../../evidence/state_effects-sets-015.md#s-4504041b08db87a8)

### path-009237

```text
(exec)# debug ip http client socket <cr>
```

Handler ` RVA 0xE002120 `；selector ` 5 `；EOL ` RVA 0x33DB8900 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-4504041b08db87a8](../../evidence/state_effects-sets-015.md#s-4504041b08db87a8)

### path-005732

```text
(exec)# debug ip http error <cr>
```

Handler ` RVA 0xE002120 `；selector ` 8 `；EOL ` RVA 0x33DB72F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-8bd641b9e1218149](../../evidence/state_effects-sets-030.md#s-8bd641b9e1218149)

### path-005617

```text
(exec)# debug ip http ezsetup <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x33DB6308 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-8bd641b9e1218149](../../evidence/state_effects-sets-030.md#s-8bd641b9e1218149)

### path-005665

```text
(exec)# debug ip http session <cr>
```

Handler ` RVA 0xE002120 `；selector ` 12 `；EOL ` RVA 0x33DB6858 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-8bd641b9e1218149](../../evidence/state_effects-sets-030.md#s-8bd641b9e1218149)

### path-005717

```text
(exec)# debug ip http ssi <cr>
```

Handler ` RVA 0xE002120 `；selector ` 5 `；EOL ` RVA 0x33DB7050 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-8bd641b9e1218149](../../evidence/state_effects-sets-030.md#s-8bd641b9e1218149)

### path-009154

```text
(exec)# debug ip http ssl error <cr>
```

Handler ` RVA 0xE002120 `；selector ` 9 `；EOL ` RVA 0x33DB7608 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-8bd641b9e1218149](../../evidence/state_effects-sets-030.md#s-8bd641b9e1218149)

### path-005641

```text
(exec)# debug ip http tokens <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x33DB65B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-8bd641b9e1218149](../../evidence/state_effects-sets-030.md#s-8bd641b9e1218149)

### path-009231

```text
(exec)# debug ip http tps error <cr>
```

Handler ` RVA 0xE002120 `；selector ` 14 `；EOL ` RVA 0x35D90C00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-8bd641b9e1218149](../../evidence/state_effects-sets-030.md#s-8bd641b9e1218149)

### path-009243

```text
(exec)# debug ip http tps trace <cr>
```

Handler ` RVA 0xE002120 `；selector ` 13 `；EOL ` RVA 0x35D90EA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-8bd641b9e1218149](../../evidence/state_effects-sets-030.md#s-8bd641b9e1218149)

### path-005682

```text
(exec)# debug ip http transactions <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x33DB6B00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-8bd641b9e1218149](../../evidence/state_effects-sets-030.md#s-8bd641b9e1218149)

### path-005698

```text
(exec)# debug ip http url <cr>
```

Handler ` RVA 0xE002120 `；selector ` 3 `；EOL ` RVA 0x33DB6DA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-8bd641b9e1218149](../../evidence/state_effects-sets-030.md#s-8bd641b9e1218149)

### path-005948

```text
(exec)# debug ip http wsman <cr>
```

Handler ` RVA 0xE002120 `；selector ` 15 `；EOL ` RVA 0x35D91940 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-8bd641b9e1218149](../../evidence/state_effects-sets-030.md#s-8bd641b9e1218149)

### path-001441

```text
(exec)# debug ip icmp <cr>
```

Handler ` RVA 0xCF57D40 `；selector ` 28 `；EOL ` RVA 0x33D2D9C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-001818

```text
(exec)# debug ip igmp <cr>
```

Handler ` RVA 0xF6D8660 `；selector ` 0 `；EOL ` RVA 0x34729FB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b82861a6c70c7d67](../../evidence/conditions-sets-071.md#c-b82861a6c70c7d67) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-005556

```text
(exec)# debug ip igmp filter <cr>
```

Handler ` RVA 0xE7B08A0 `；selector ` 0 `；EOL ` RVA 0x34339780 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-0f967518d42a9c63](../../evidence/state_effects-sets-004.md#s-0f967518d42a9c63)

### path-009126

```text
(exec)# debug ip igmp snooping <address> <cr>
```

Handler ` RVA 0xC30B020 `；selector ` 0 `；EOL ` RVA 0x33A4B638 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IPv4 group address。

[条件 C-de9e367c3a18de77](../../evidence/conditions-sets-086.md#c-de9e367c3a18de77) · [参数 P-b484bae55e3063bd](../../evidence/parameters-sets-014.md#p-b484bae55e3063bd) · [状态效果 S-a2beb4b9b80a051b](../../evidence/state_effects-sets-034.md#s-a2beb4b9b80a051b)

### path-005705

```text
(exec)# debug ip igmp snooping <cr>
```

Handler ` RVA 0xC30B020 `；selector ` 11 `；EOL ` RVA 0x33A4BC30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2333efa19389db85](../../evidence/conditions-sets-014.md#c-2333efa19389db85) · [状态效果 S-a2beb4b9b80a051b](../../evidence/state_effects-sets-034.md#s-a2beb4b9b80a051b)

### path-009120

```text
(exec)# debug ip igmp snooping filter <cr>
```

Handler ` RVA 0xC30B020 `；selector ` 7 `；EOL ` RVA 0x33A4A840 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fe0788b981867761](../../evidence/conditions-sets-098.md#c-fe0788b981867761) · [状态效果 S-6e89b1d099d60b14](../../evidence/state_effects-sets-023.md#s-6e89b1d099d60b14)

### path-009098

```text
(exec)# debug ip igmp snooping group <cr>
```

Handler ` RVA 0xC30B020 `；selector ` 6 `；EOL ` RVA 0x33A4AB98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-de9e367c3a18de77](../../evidence/conditions-sets-086.md#c-de9e367c3a18de77) · [状态效果 S-a2beb4b9b80a051b](../../evidence/state_effects-sets-034.md#s-a2beb4b9b80a051b)

### path-009111

```text
(exec)# debug ip igmp snooping management <cr>
```

Handler ` RVA 0xC30B020 `；selector ` 3 `；EOL ` RVA 0x33A4B0E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-de9e367c3a18de77](../../evidence/conditions-sets-086.md#c-de9e367c3a18de77) · [状态效果 S-a2beb4b9b80a051b](../../evidence/state_effects-sets-034.md#s-a2beb4b9b80a051b)

### path-009138

```text
(exec)# debug ip igmp snooping querier <cr>
```

Handler ` RVA 0xC30B020 `；selector ` 5 `；EOL ` RVA 0x33A4BC08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e30c64bfbe4bdf9b](../../evidence/conditions-sets-087.md#c-e30c64bfbe4bdf9b) · [状态效果 S-a2beb4b9b80a051b](../../evidence/state_effects-sets-034.md#s-a2beb4b9b80a051b)

### path-009132

```text
(exec)# debug ip igmp snooping redundancy <cr>
```

Handler ` RVA 0xC30B020 `；selector ` 1 `；EOL ` RVA 0x33A4B920 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fae52416ba6e2386](../../evidence/conditions-sets-097.md#c-fae52416ba6e2386) · [状态效果 S-a2beb4b9b80a051b](../../evidence/state_effects-sets-034.md#s-a2beb4b9b80a051b)

### path-009107

```text
(exec)# debug ip igmp snooping router <cr>
```

Handler ` RVA 0xC30B020 `；selector ` 4 `；EOL ` RVA 0x33A4AE40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-de9e367c3a18de77](../../evidence/conditions-sets-086.md#c-de9e367c3a18de77) · [状态效果 S-a2beb4b9b80a051b](../../evidence/state_effects-sets-034.md#s-a2beb4b9b80a051b)

### path-009118

```text
(exec)# debug ip igmp snooping timer <cr>
```

Handler ` RVA 0xC30B020 `；selector ` 2 `；EOL ` RVA 0x33A4B390 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-de9e367c3a18de77](../../evidence/conditions-sets-086.md#c-de9e367c3a18de77) · [状态效果 S-a2beb4b9b80a051b](../../evidence/state_effects-sets-034.md#s-a2beb4b9b80a051b)

### path-005543

```text
(exec)# debug ip igmp timer <cr>
```

Handler ` RVA 0xF6D8660 `；selector ` 1 `；EOL ` RVA 0x34729CD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-005388

```text
(exec)# debug ip interface route-cache <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x33D41858 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-eeea04b0864963ad](../../evidence/state_effects-sets-050.md#s-eeea04b0864963ad)

### path-001830

```text
(exec)# debug ip mcache <cr>
```

Handler ` RVA 0xF6D8660 `；selector ` 13 `；EOL ` RVA 0x3474B0A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-182902e200fab825](../../evidence/conditions-sets-009.md#c-182902e200fab825) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-006012

```text
(exec)# debug ip mfib init <cr>
```

Handler ` RVA 0x11978F70 `；selector ` 0 `；EOL ` RVA 0x355B3318 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-c35015232c8ce567](../../evidence/state_effects-sets-041.md#s-c35015232c8ce567)

### path-022265

```text
(exec)# debug ip mfib vrf <?option@55558ab07890> pak <cr>
```

Handler ` RVA 0x11978F70 `；selector ` 0 `；EOL ` RVA 0x355B3318 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9914844d7dce6ba8](../../evidence/conditions-sets-059.md#c-9914844d7dce6ba8) · [缺口 G-2efb33856dc64774](../../evidence/gaps-sets-002.md#g-2efb33856dc64774) · [状态效果 S-a828244872dace9b](../../evidence/state_effects-sets-036.md#s-a828244872dace9b)

### path-001839

```text
(exec)# debug ip mhbeat <cr>
```

Handler ` RVA 0xF6D8660 `；selector ` 25 `；EOL ` RVA 0x3474BD80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-001551

```text
(exec)# debug ip mib <cr>
```

Handler ` RVA 0xCF57D40 `；selector ` 35 `；EOL ` RVA 0x33D2F3E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-001896

```text
(exec)# debug ip mpacket <cr>
```

Handler ` RVA 0xF6D8660 `；selector ` 15 `；EOL ` RVA 0x3474B8F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8f22c3b9fefd61af](../../evidence/conditions-sets-055.md#c-8f22c3b9fefd61af) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-005600

```text
(exec)# debug ip mpacket fastswitch <cr>
```

Handler ` RVA 0xF6D8660 `；selector ` 14 `；EOL ` RVA 0x3474B470 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-006319

```text
(exec)# debug ip mrib bundle <cr>
```

Handler ` RVA 0x119AD4B0 `；selector ` 7 `；EOL ` RVA 0x355C51F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d8f0c4284bb9d23b](../../evidence/conditions-sets-084.md#c-d8f0c4284bb9d23b) · [状态效果 S-4813b109b2f0de93](../../evidence/state_effects-sets-016.md#s-4813b109b2f0de93)

### path-006161

```text
(exec)# debug ip mrib client <cr>
```

Handler ` RVA 0x119AD4B0 `；selector ` 2 `；EOL ` RVA 0x355C44B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d8f0c4284bb9d23b](../../evidence/conditions-sets-084.md#c-d8f0c4284bb9d23b) · [状态效果 S-4813b109b2f0de93](../../evidence/state_effects-sets-016.md#s-4813b109b2f0de93)

### path-006256

```text
(exec)# debug ip mrib filter <cr>
```

Handler ` RVA 0x119AD4B0 `；selector ` 4 `；EOL ` RVA 0x355C4CA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d8f0c4284bb9d23b](../../evidence/conditions-sets-084.md#c-d8f0c4284bb9d23b) · [状态效果 S-4813b109b2f0de93](../../evidence/state_effects-sets-016.md#s-4813b109b2f0de93)

### path-006221

```text
(exec)# debug ip mrib io <cr>
```

Handler ` RVA 0x119AD4B0 `；selector ` 5 `；EOL ` RVA 0x355C4A00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d8f0c4284bb9d23b](../../evidence/conditions-sets-084.md#c-d8f0c4284bb9d23b) · [状态效果 S-4813b109b2f0de93](../../evidence/state_effects-sets-016.md#s-4813b109b2f0de93)

### path-006141

```text
(exec)# debug ip mrib issu <cr>
```

Handler ` RVA 0x119AD4B0 `；selector ` 10 `；EOL ` RVA 0x355C5AA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-99c93a842883c90c](../../evidence/conditions-sets-059.md#c-99c93a842883c90c) · [状态效果 S-4813b109b2f0de93](../../evidence/state_effects-sets-016.md#s-4813b109b2f0de93)

### path-006347

```text
(exec)# debug ip mrib malloc <cr>
```

Handler ` RVA 0x119AD4B0 `；selector ` 6 `；EOL ` RVA 0x355C54A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d8f0c4284bb9d23b](../../evidence/conditions-sets-084.md#c-d8f0c4284bb9d23b) · [状态效果 S-4813b109b2f0de93](../../evidence/state_effects-sets-016.md#s-4813b109b2f0de93)

### path-006090

```text
(exec)# debug ip mrib proxy <cr>
```

Handler ` RVA 0x119AD4B0 `；selector ` 9 `；EOL ` RVA 0x355C57C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ae34a104b9fc4bb9](../../evidence/conditions-sets-067.md#c-ae34a104b9fc4bb9) · [状态效果 S-4813b109b2f0de93](../../evidence/state_effects-sets-016.md#s-4813b109b2f0de93)

### path-009333

```text
(exec)# debug ip mrib route <address> <cr>
```

Handler ` RVA 0x119AD4B0 `；selector ` 1 `；EOL ` RVA 0x355C3FC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Multicast group。

[条件 C-d8f0c4284bb9d23b](../../evidence/conditions-sets-084.md#c-d8f0c4284bb9d23b) · [参数 P-8a538e0d7488589c](../../evidence/parameters-sets-011.md#p-8a538e0d7488589c) · [状态效果 S-4813b109b2f0de93](../../evidence/state_effects-sets-016.md#s-4813b109b2f0de93)

### path-006172

```text
(exec)# debug ip mrib route <cr>
```

Handler ` RVA 0x119AD4B0 `；selector ` 0 `；EOL ` RVA 0x355C3FF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d8f0c4284bb9d23b](../../evidence/conditions-sets-084.md#c-d8f0c4284bb9d23b) · [状态效果 S-4813b109b2f0de93](../../evidence/state_effects-sets-016.md#s-4813b109b2f0de93)

### path-006197

```text
(exec)# debug ip mrib table <cr>
```

Handler ` RVA 0x119AD4B0 `；selector ` 3 `；EOL ` RVA 0x355C4758 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d8f0c4284bb9d23b](../../evidence/conditions-sets-084.md#c-d8f0c4284bb9d23b) · [状态效果 S-4813b109b2f0de93](../../evidence/state_effects-sets-016.md#s-4813b109b2f0de93)

### path-006115

```text
(exec)# debug ip mrib test <cr>
```

Handler ` RVA 0x119AD4B0 `；selector ` 14 `；EOL ` RVA 0x355C3CB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d8f0c4284bb9d23b](../../evidence/conditions-sets-084.md#c-d8f0c4284bb9d23b) · [状态效果 S-4813b109b2f0de93](../../evidence/state_effects-sets-016.md#s-4813b109b2f0de93)

### path-006292

```text
(exec)# debug ip mrib timer <cr>
```

Handler ` RVA 0x119AD4B0 `；selector ` 8 `；EOL ` RVA 0x355C4F50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d8f0c4284bb9d23b](../../evidence/conditions-sets-084.md#c-d8f0c4284bb9d23b) · [状态效果 S-4813b109b2f0de93](../../evidence/state_effects-sets-016.md#s-4813b109b2f0de93)

### path-009319

```text
(exec)# debug ip mrib trans <address> <cr>
```

Handler ` RVA 0x119AD4B0 `；selector ` 12 `；EOL ` RVA 0x355C37D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Multicast group。

[条件 C-a9d2845ab7fff50a](../../evidence/conditions-sets-066.md#c-a9d2845ab7fff50a) · [参数 P-5a495ef8e8f1c89e](../../evidence/parameters-sets-007.md#p-5a495ef8e8f1c89e) · [状态效果 S-4813b109b2f0de93](../../evidence/state_effects-sets-016.md#s-4813b109b2f0de93)

### path-006146

```text
(exec)# debug ip mrib trans <cr>
```

Handler ` RVA 0x119AD4B0 `；selector ` 11 `；EOL ` RVA 0x355C37F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a9d2845ab7fff50a](../../evidence/conditions-sets-066.md#c-a9d2845ab7fff50a) · [状态效果 S-4813b109b2f0de93](../../evidence/state_effects-sets-016.md#s-4813b109b2f0de93)

### path-005780

```text
(exec)# debug ip mrm events <cr>
```

Handler ` RVA 0xF666CA0 `；selector ` 0 `；EOL ` RVA 0x3471ED08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-005812

```text
(exec)# debug ip mrm packets <cr>
```

Handler ` RVA 0xF666CA0 `；selector ` 1 `；EOL ` RVA 0x3471EFB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-014235

```text
(exec)# debug ip mrouting <address> <cr>
```

Handler ` RVA 0xF6D8660 `；selector ` 9 `；EOL ` RVA 0x34749978 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` IP source or group address。

[条件 C-c4938fe1088d8ac2](../../evidence/conditions-sets-076.md#c-c4938fe1088d8ac2) · [缺口 G-bbd1c1f88c236f31](../../evidence/gaps-sets-007.md#g-bbd1c1f88c236f31) · [参数 P-80c415ceacfd2cea](../../evidence/parameters-sets-010.md#p-80c415ceacfd2cea) · [状态效果 S-5f5abc7dfc18825f](../../evidence/state_effects-sets-020.md#s-5f5abc7dfc18825f)

### path-001857

```text
(exec)# debug ip mrouting <cr>
```

Handler ` RVA 0xF6D8660 `；selector ` 9 `；EOL ` RVA 0x34749978 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-85d089de04f2be85](../../evidence/conditions-sets-052.md#c-85d089de04f2be85) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-005578

```text
(exec)# debug ip mrouting limits <cr>
```

Handler ` RVA 0xF6D8660 `；selector ` 28 `；EOL ` RVA 0x347493B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ba5a745772b36846](../../evidence/conditions-sets-072.md#c-ba5a745772b36846) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-005542

```text
(exec)# debug ip mrouting rpf-events <cr>
```

Handler ` RVA 0xF6D8660 `；selector ` 10 `；EOL ` RVA 0x34748DA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-005577

```text
(exec)# debug ip mrouting rsvp <cr>
```

Handler ` RVA 0xF6D8660 `；selector ` 29 `；EOL ` RVA 0x347490D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d53de9e57d26a76a](../../evidence/conditions-sets-082.md#c-d53de9e57d26a76a) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-005599

```text
(exec)# debug ip mrouting timers <cr>
```

Handler ` RVA 0xF6D8660 `；selector ` 26 `；EOL ` RVA 0x347496A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ba5a745772b36846](../../evidence/conditions-sets-072.md#c-ba5a745772b36846) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-005572

```text
(exec)# debug ip msdp detail <cr>
```

Handler ` RVA 0xF6D8660 `；selector ` 19 `；EOL ` RVA 0x3473B108 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-93755047260ea849](../../evidence/state_effects-sets-031.md#s-93755047260ea849)

### path-005555

```text
(exec)# debug ip msdp peer <cr>
```

Handler ` RVA 0xF6D8660 `；selector ` 18 `；EOL ` RVA 0x3473AE50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-018b308e2278b64a](../../evidence/state_effects-sets-001.md#s-018b308e2278b64a)

### path-005536

```text
(exec)# debug ip msdp resets <cr>
```

Handler ` RVA 0xF6D8660 `；selector ` 21 `；EOL ` RVA 0x3473AB98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-8896c3ebaf58d71a](../../evidence/state_effects-sets-029.md#s-8896c3ebaf58d71a)

### path-005596

```text
(exec)# debug ip msdp routes <cr>
```

Handler ` RVA 0xF6D8660 `；selector ` 20 `；EOL ` RVA 0x3473B3C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-7e49b26aaadc5018](../../evidence/state_effects-sets-027.md#s-7e49b26aaadc5018)

### path-009424

```text
(exec)# debug ip mtrie leaf add <cr>
```

Handler ` RVA 0xB53BCB0 `；selector ` 1 `；EOL ` RVA 0x33798FF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-009402

```text
(exec)# debug ip mtrie leaf bucket-walk <cr>
```

Handler ` RVA 0xB53BCB0 `；selector ` 2 `；EOL ` RVA 0x33798D50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-009445

```text
(exec)# debug ip mtrie leaf lock <cr>
```

Handler ` RVA 0xB53BCB0 `；selector ` 0 `；EOL ` RVA 0x337992A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-005535

```text
(exec)# debug ip multicast bt <cr>
```

Handler ` RVA 0xF6D8660 `；selector ` 32 `；EOL ` RVA 0x3474A1D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad7423dafecc0a98](../../evidence/conditions-sets-067.md#c-ad7423dafecc0a98) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-005649

```text
(exec)# debug ip multicast gir <cr>
```

Handler ` RVA 0xF6D8660 `；selector ` 31 `；EOL ` RVA 0x3474ACD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d8a56cb9d769e14b](../../evidence/conditions-sets-083.md#c-d8a56cb9d769e14b) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-005720

```text
(exec)# debug ip multicast redundancy <cr>
```

Handler ` RVA 0xD490F50 `；selector ` 0 `；EOL ` RVA 0x33E50238 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cb4da5bf332828a0](../../evidence/conditions-sets-078.md#c-cb4da5bf332828a0) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-009136

```text
(exec)# debug ip multicast redundancy verbose <cr>
```

Handler ` RVA 0xD490F50 `；selector ` 1 `；EOL ` RVA 0x33E50210 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cb4da5bf332828a0](../../evidence/conditions-sets-078.md#c-cb4da5bf332828a0) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-009083

```text
(exec)# debug ip multicast rpf tracked <cr>
```

Handler ` RVA 0xF6D8660 `；selector ` 11 `；EOL ` RVA 0x34749F48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-005595

```text
(exec)# debug ip multicast topology <cr>
```

Handler ` RVA 0xF6D8660 `；selector ` 12 `；EOL ` RVA 0x3474A9E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7b355785c4835443](../../evidence/conditions-sets-048.md#c-7b355785c4835443) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-018161

```text
(exec)# debug ip multicast trace-point <address> <cr>
```

Handler ` RVA 0xF6D8660 `；selector ` 34 `；EOL ` RVA 0x3474A590 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` IP source or group address。

[条件 C-6d07cabcbdd27b7d](../../evidence/conditions-sets-042.md#c-6d07cabcbdd27b7d) · [缺口 G-b1856853270599d6](../../evidence/gaps-sets-006.md#g-b1856853270599d6) · [参数 P-a93f546632b0afc6](../../evidence/parameters-sets-013.md#p-a93f546632b0afc6) · [状态效果 S-56ceeb5ad8aa5a90](../../evidence/state_effects-sets-019.md#s-56ceeb5ad8aa5a90)

### path-005602

```text
(exec)# debug ip multicast trace-point <cr>
```

Handler ` RVA 0xF6D8660 `；selector ` 34 `；EOL ` RVA 0x3474A590 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-30157f1675e8569b](../../evidence/conditions-sets-019.md#c-30157f1675e8569b) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-002312

```text
(exec)# debug ip nat <cr>
```

Handler ` RVA 0xCF57D40 `；selector ` 0 `；EOL ` RVA 0x347C29A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-059598a4b44529be](../../evidence/conditions-sets-003.md#c-059598a4b44529be) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-002366

```text
(exec)# debug ip nat <cr>
```

Handler ` RVA 0xCF57D40 `；selector ` 25 `；EOL ` RVA 0x347C2CF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7a2841e0d520278f](../../evidence/conditions-sets-047.md#c-7a2841e0d520278f) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-006068

```text
(exec)# debug ip nat alg <cr>
```

Handler ` RVA 0xCF57D40 `；selector ` 24 `；EOL ` RVA 0x347C0F78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-46e7b7d0bbcb913a](../../evidence/conditions-sets-028.md#c-46e7b7d0bbcb913a) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-006383

```text
(exec)# debug ip nat bind <cr>
```

Handler ` RVA 0xCF57D40 `；selector ` 6 `；EOL ` RVA 0x347C1E80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-66b2496659f18af1](../../evidence/conditions-sets-040.md#c-66b2496659f18af1) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-006223

```text
(exec)# debug ip nat detailed <cr>
```

Handler ` RVA 0xCF57D40 `；selector ` 1 `；EOL ` RVA 0x347C0340 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-910b8bebd4e7f072](../../evidence/conditions-sets-056.md#c-910b8bebd4e7f072) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-006076

```text
(exec)# debug ip nat drop <cr>
```

Handler ` RVA 0xCF57D40 `；selector ` 23 `；EOL ` RVA 0x347C0C88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e77e88d1e6db4370](../../evidence/conditions-sets-089.md#c-e77e88d1e6db4370) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-006222

```text
(exec)# debug ip nat h323 <cr>
```

Handler ` RVA 0xCF57D40 `；selector ` 16 `；EOL ` RVA 0x347C4138 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e8d4e415631e3e29](../../evidence/conditions-sets-090.md#c-e8d4e415631e3e29) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-005952

```text
(exec)# debug ip nat ha <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x34CE8EC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-7ea0da5d3d101042](../../evidence/state_effects-sets-027.md#s-7ea0da5d3d101042)

### path-009216

```text
(exec)# debug ip nat ha event <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x34CE8BF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-7ea0da5d3d101042](../../evidence/state_effects-sets-027.md#s-7ea0da5d3d101042)

### path-009233

```text
(exec)# debug ip nat ha issu <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x34CE8E98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-7ea0da5d3d101042](../../evidence/state_effects-sets-027.md#s-7ea0da5d3d101042)

### path-009407

```text
(exec)# debug ip nat ha-sso detail <cr>
```

Handler ` RVA 0xCF57D40 `；selector ` 26 `；EOL ` RVA 0x347C2D30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7a2841e0d520278f](../../evidence/conditions-sets-047.md#c-7a2841e0d520278f) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-009425

```text
(exec)# debug ip nat ha-sso error <cr>
```

Handler ` RVA 0xCF57D40 `；selector ` 27 `；EOL ` RVA 0x347C2FD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7a2841e0d520278f](../../evidence/conditions-sets-047.md#c-7a2841e0d520278f) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-006092

```text
(exec)# debug ip nat ipsec <cr>
```

Handler ` RVA 0xCF57D40 `；selector ` 15 `；EOL ` RVA 0x347C14C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-257a5368425470ca](../../evidence/conditions-sets-015.md#c-257a5368425470ca) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-006487

```text
(exec)# debug ip nat limit <cr>
```

Handler ` RVA 0xCF57D40 `；selector ` 3 `；EOL ` RVA 0x347C2410 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3fac813bf1c99103](../../evidence/conditions-sets-025.md#c-3fac813bf1c99103) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-006415

```text
(exec)# debug ip nat mapping <cr>
```

Handler ` RVA 0xCF57D40 `；selector ` 5 `；EOL ` RVA 0x347C2128 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-66b2496659f18af1](../../evidence/conditions-sets-040.md#c-66b2496659f18af1) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-006022

```text
(exec)# debug ip nat pap <cr>
```

Handler ` RVA 0xCF57D40 `；selector ` 22 `；EOL ` RVA 0x347C0910 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f95aa5da1ceb0c6e](../../evidence/conditions-sets-096.md#c-f95aa5da1ceb0c6e) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-006294

```text
(exec)# debug ip nat pool <cr>
```

Handler ` RVA 0xCF57D40 `；selector ` 9 `；EOL ` RVA 0x347C18F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-09c9eff3dab583b7](../../evidence/conditions-sets-004.md#c-09c9eff3dab583b7) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-005943

```text
(exec)# debug ip nat port <cr>
```

Handler ` RVA 0xCF57D40 `；selector ` 13 `；EOL ` RVA 0x347C05E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-44d5514076babc64](../../evidence/conditions-sets-027.md#c-44d5514076babc64) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-005995

```text
(exec)# debug ip nat pptp <cr>
```

Handler ` RVA 0xCF57D40 `；selector ` 11 `；EOL ` RVA 0x347C49D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a20d03080d25d044](../../evidence/conditions-sets-063.md#c-a20d03080d25d044) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-006069

```text
(exec)# debug ip nat route <cr>
```

Handler ` RVA 0xCF57D40 `；selector ` 10 `；EOL ` RVA 0x347C1220 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-257a5368425470ca](../../evidence/conditions-sets-015.md#c-257a5368425470ca) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-006384

```text
(exec)# debug ip nat route-map <cr>
```

Handler ` RVA 0xCF57D40 `；selector ` 7 `；EOL ` RVA 0x347C38F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-573d2896352e3111](../../evidence/conditions-sets-034.md#c-573d2896352e3111) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-006321

```text
(exec)# debug ip nat session <cr>
```

Handler ` RVA 0xCF57D40 `；selector ` 8 `；EOL ` RVA 0x347C1B98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-09c9eff3dab583b7](../../evidence/conditions-sets-004.md#c-09c9eff3dab583b7) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-006166

```text
(exec)# debug ip nat sg <cr>
```

Handler ` RVA 0xCF57D40 `；selector ` 19 `；EOL ` RVA 0x347C43F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-02953dcb5e37c91c](../../evidence/conditions-sets-001.md#c-02953dcb5e37c91c) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-006295

```text
(exec)# debug ip nat sip <cr>
```

Handler ` RVA 0xCF57D40 `；selector ` 17 `；EOL ` RVA 0x347C3BC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1b19d9831470c623](../../evidence/conditions-sets-011.md#c-1b19d9831470c623) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-006258

```text
(exec)# debug ip nat skinny <cr>
```

Handler ` RVA 0xCF57D40 `；selector ` 12 `；EOL ` RVA 0x347C3E80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-595c5fa9038e980f](../../evidence/conditions-sets-035.md#c-595c5fa9038e980f) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-006488

```text
(exec)# debug ip nat timeout <cr>
```

Handler ` RVA 0xCF57D40 `；selector ` 4 `；EOL ` RVA 0x347C3620 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8507fc64a8797023](../../evidence/conditions-sets-051.md#c-8507fc64a8797023) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-006167

```text
(exec)# debug ip nat vrf <cr>
```

Handler ` RVA 0xCF57D40 `；selector ` 18 `；EOL ` RVA 0x347C46E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2920036afa90eb66](../../evidence/conditions-sets-016.md#c-2920036afa90eb66) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-006538

```text
(exec)# debug ip nat wlan-nat <cr>
```

Handler ` RVA 0xCF57D40 `；selector ` 2 `；EOL ` RVA 0x347C26F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-727af62e57b9d972](../../evidence/conditions-sets-044.md#c-727af62e57b9d972) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-005806

```text
(exec)# debug ip nat-route all <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x35C0F818 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-078a2188bb239cd5](../../evidence/state_effects-sets-002.md#s-078a2188bb239cd5)

### path-009105

```text
(exec)# debug ip nbar control-plane low <cr>
```

Handler ` RVA 0x10F3B120 `；selector ` 46 `；EOL ` RVA 0x3527CD50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0350417991cd7477](../../evidence/conditions-sets-002.md#c-0350417991cd7477) · [状态效果 S-ad87cb459ce6299e](../../evidence/state_effects-sets-037.md#s-ad87cb459ce6299e)

### path-005914

```text
(exec)# debug ip omp adjacency <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x35C14970 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-ae1ba175b93e7ca6](../../evidence/state_effects-sets-037.md#s-ae1ba175b93e7ca6)

### path-005971

```text
(exec)# debug ip omp all <cr>
```

Handler ` RVA 0x13741FF0 `；selector ` 0 `；EOL ` RVA 0x35C15178 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-ae1ba175b93e7ca6](../../evidence/state_effects-sets-037.md#s-ae1ba175b93e7ca6)

### path-005844

```text
(exec)# debug ip omp forwarding <cr>
```

Handler ` RVA 0xE002120 `；selector ` 12 `；EOL ` RVA 0x35C14178 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-ae1ba175b93e7ca6](../../evidence/state_effects-sets-037.md#s-ae1ba175b93e7ca6)

### path-005975

```text
(exec)# debug ip omp gw-tracking <cr>
```

Handler ` RVA 0xE002120 `；selector ` 4 `；EOL ` RVA 0x35C14CA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-ae1ba175b93e7ca6](../../evidence/state_effects-sets-037.md#s-ae1ba175b93e7ca6)

### path-009240

```text
(exec)# debug ip omp gw-tracking detail <cr>
```

Handler ` RVA 0xE002120 `；selector ` 3 `；EOL ` RVA 0x35C14C80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-ae1ba175b93e7ca6](../../evidence/state_effects-sets-037.md#s-ae1ba175b93e7ca6)

### path-005820

```text
(exec)# debug ip omp multi-tenant <cr>
```

Handler ` RVA 0xE002120 `；selector ` 11 `；EOL ` RVA 0x35C13ED0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-ae1ba175b93e7ca6](../../evidence/state_effects-sets-037.md#s-ae1ba175b93e7ca6)

### path-005894

```text
(exec)# debug ip omp multicast <cr>
```

Handler ` RVA 0xE002120 `；selector ` 9 `；EOL ` RVA 0x35C146C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-ae1ba175b93e7ca6](../../evidence/state_effects-sets-037.md#s-ae1ba175b93e7ca6)

### path-005787

```text
(exec)# debug ip omp network <cr>
```

Handler ` RVA 0xE002120 `；selector ` 10 `；EOL ` RVA 0x35C13C28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-ae1ba175b93e7ca6](../../evidence/state_effects-sets-037.md#s-ae1ba175b93e7ca6)

### path-005794

```text
(exec)# debug ip omp redistribute <cr>
```

Handler ` RVA 0xE002120 `；selector ` 5 `；EOL ` RVA 0x35C13758 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-ae1ba175b93e7ca6](../../evidence/state_effects-sets-037.md#s-ae1ba175b93e7ca6)

### path-009166

```text
(exec)# debug ip omp redistribute detail <cr>
```

Handler ` RVA 0xE002120 `；selector ` 6 `；EOL ` RVA 0x35C13730 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-ae1ba175b93e7ca6](../../evidence/state_effects-sets-037.md#s-ae1ba175b93e7ca6)

### path-005769

```text
(exec)# debug ip omp routes <cr>
```

Handler ` RVA 0xE002120 `；selector ` 8 `；EOL ` RVA 0x35C131F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-ae1ba175b93e7ca6](../../evidence/state_effects-sets-037.md#s-ae1ba175b93e7ca6)

### path-009152

```text
(exec)# debug ip omp routes detail <cr>
```

Handler ` RVA 0xE002120 `；selector ` 7 `；EOL ` RVA 0x35C131D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-ae1ba175b93e7ca6](../../evidence/state_effects-sets-037.md#s-ae1ba175b93e7ca6)

### path-005871

```text
(exec)# debug ip omp rwatch <cr>
```

Handler ` RVA 0x13741FF0 `；selector ` 1 `；EOL ` RVA 0x35C14420 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-ae1ba175b93e7ca6](../../evidence/state_effects-sets-037.md#s-ae1ba175b93e7ca6)

### path-005761

```text
(exec)# debug ip ospf adj <cr>
```

Handler ` RVA 0xFCEAFF0 `；selector ` 5 `；EOL ` RVA 0x34875858 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-009335

```text
(exec)# debug ip ospf capability advertisements <cr>
```

Handler ` RVA 0xFCEAFF0 `；selector ` 36 `；EOL ` RVA 0x3489B768 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-009188

```text
(exec)# debug ip ospf crimson notification <cr>
```

Handler ` RVA 0xFCEAFF0 `；selector ` 59 `；EOL ` RVA 0x34875E48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-009194

```text
(exec)# debug ip ospf crimson oper <cr>
```

Handler ` RVA 0xFCEAFF0 `；selector ` 60 `；EOL ` RVA 0x34875BA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-006123

```text
(exec)# debug ip ospf database-timer <cr>
```

Handler ` RVA 0xFCEAFF0 `；selector ` 11 `；EOL ` RVA 0x3489A8F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-009346

```text
(exec)# debug ip ospf database-timer rate-limit <cr>
```

Handler ` RVA 0xFCEAFF0 `；selector ` 12 `；EOL ` RVA 0x3489A938 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-005947

```text
(exec)# debug ip ospf demand-circuit <cr>
```

Handler ` RVA 0xFCEAFF0 `；selector ` 13 `；EOL ` RVA 0x348974E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-005972

```text
(exec)# debug ip ospf events <cr>
```

Handler ` RVA 0xFCEAFF0 `；selector ` 14 `；EOL ` RVA 0x34897788 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-009495

```text
(exec)# debug ip ospf fast-reroute rib <cr>
```

Handler ` RVA 0xFCEAFF0 `；selector ` 25 `；EOL ` RVA 0x3489EE10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8a0e6453256798aa](../../evidence/conditions-sets-053.md#c-8a0e6453256798aa) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-009455

```text
(exec)# debug ip ospf fast-reroute spf <cr>
```

Handler ` RVA 0xFCEAFF0 `；selector ` 24 `；EOL ` RVA 0x3489EB08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8a0e6453256798aa](../../evidence/conditions-sets-053.md#c-8a0e6453256798aa) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-011283

```text
(exec)# debug ip ospf fast-reroute ti-lfa rib <cr>
```

Handler ` RVA 0xFCEAFF0 `；selector ` 27 `；EOL ` RVA 0x3489F538 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3a4af3e729a03027](../../evidence/conditions-sets-023.md#c-3a4af3e729a03027) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-011284

```text
(exec)# debug ip ospf fast-reroute ti-lfa spf <cr>
```

Handler ` RVA 0xFCEAFF0 `；selector ` 26 `；EOL ` RVA 0x3489F218 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3a4af3e729a03027](../../evidence/conditions-sets-023.md#c-3a4af3e729a03027) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-006523

```text
(exec)# debug ip ospf flex-algo <cr>
```

Handler ` RVA 0xFCEAFF0 `；selector ` 68 `；EOL ` RVA 0x348A1EE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7cceac04a47a1fe5](../../evidence/conditions-sets-048.md#c-7cceac04a47a1fe5) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-006079

```text
(exec)# debug ip ospf flood <cr>
```

Handler ` RVA 0xFCEAFF0 `；selector ` 6 `；EOL ` RVA 0x34897B08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-005920

```text
(exec)# debug ip ospf ha <cr>
```

Handler ` RVA 0xFCEAFF0 `；selector ` 28 `；EOL ` RVA 0x34896F98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-005915

```text
(exec)# debug ip ospf hello <cr>
```

Handler ` RVA 0xFCEAFF0 `；selector ` 1 `；EOL ` RVA 0x34897238 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-006229

```text
(exec)# debug ip ospf lsa-generation <cr>
```

Handler ` RVA 0xFCEAFF0 `；selector ` 9 `；EOL ` RVA 0x3489BA60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-006266

```text
(exec)# debug ip ospf lsa-maxage <cr>
```

Handler ` RVA 0xFCEAFF0 `；selector ` 8 `；EOL ` RVA 0x3489BD98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-006099

```text
(exec)# debug ip ospf monitor <cr>
```

Handler ` RVA 0xFCEAFF0 `；selector ` 20 `；EOL ` RVA 0x34897E58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-06f6f8a6538e6cb7](../../evidence/conditions-sets-003.md#c-06f6f8a6538e6cb7) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-009363

```text
(exec)# debug ip ospf mpls traffic-eng <cr>
```

Handler ` RVA 0xFCEAFF0 `；selector ` 33 `；EOL ` RVA 0x3489B1D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-011189

```text
(exec)# debug ip ospf mpls traffic-eng advertisements <cr>
```

Handler ` RVA 0xFCEAFF0 `；selector ` 34 `；EOL ` RVA 0x3489B210 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-011167

```text
(exec)# debug ip ospf mpls traffic-eng signaling <cr>
```

Handler ` RVA 0xFCEAFF0 `；selector ` 35 `；EOL ` RVA 0x3489AF00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-005897

```text
(exec)# debug ip ospf nsf <cr>
```

Handler ` RVA 0xFCEAFF0 `；selector ` 29 `；EOL ` RVA 0x34896C90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-005875

```text
(exec)# debug ip ospf nsr <cr>
```

Handler ` RVA 0xFCEAFF0 `；selector ` 32 `；EOL ` RVA 0x34896988 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-006077

```text
(exec)# debug ip ospf packet <cr>
```

Handler ` RVA 0xFCEAFF0 `；selector ` 0 `；EOL ` RVA 0x34898480 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-006460

```text
(exec)# debug ip ospf performance-measurement <cr>
```

Handler ` RVA 0xFCEAFF0 `；selector ` 58 `；EOL ` RVA 0x348A1B98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-874fa0e73430b187](../../evidence/conditions-sets-052.md#c-874fa0e73430b187) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-006465

```text
(exec)# debug ip ospf rib <cr>
```

Handler ` RVA 0xFCEAFF0 `；selector ` 23 `；EOL ` RVA 0x3489DBD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4124aa4d65c0e0ca](../../evidence/conditions-sets-025.md#c-4124aa4d65c0e0ca) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-006496

```text
(exec)# debug ip ospf rib <cr>
```

Handler ` RVA 0xFCEAFF0 `；selector ` 7 `；EOL ` RVA 0x3489DE78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-373fef37a7fd999f](../../evidence/conditions-sets-021.md#c-373fef37a7fd999f) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-006524

```text
(exec)# debug ip ospf rib <cr>
```

Handler ` RVA 0xFCEAFF0 `；selector ` 22 `；EOL ` RVA 0x3489E120 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a810a3e565531737](../../evidence/conditions-sets-065.md#c-a810a3e565531737) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-006525

```text
(exec)# debug ip ospf rib <cr>
```

Handler ` RVA 0xFCEAFF0 `；selector ` 21 `；EOL ` RVA 0x3489E3A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ec80fefa6d803180](../../evidence/conditions-sets-091.md#c-ec80fefa6d803180) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)

### path-009434

```text
(exec)# debug ip ospf scheduler hello <cr>
```

Handler ` RVA 0xFCEAFF0 `；selector ` 42 `；EOL ` RVA 0x3489C6B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [状态效果 S-73e386460f2edac2](../../evidence/state_effects-sets-025.md#s-73e386460f2edac2)
