# l2 · 依赖静态建槽的条件安装

[模式索引](README.md) · [总索引](../../README.md)

### static_slot_creation_candidates-004010

```text
(config-vfi)# auto-route-target <cr>
```

Handler ` RVA 0x1AA3B390 `；selector ` 7 `；EOL ` RVA 0x36D4F9D8 `。

模式根 ` RVA 0x36D4BC20 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-fa3e3b684ff5492e](../../evidence/conditional_registrations-sets-003.md#r-fa3e3b684ff5492e) · [条件 C-94cf47bdc927f26b](../../evidence/conditions-sets-058.md#c-94cf47bdc927f26b) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### static_slot_creation_candidates-004030

```text
(config-vfi)# bridge-domain <number:1..4094> vlan <cr>
```

Handler ` RVA 0x1AA3B390 `；selector ` 4 `；EOL ` RVA 0x36D4E708 `。

模式根 ` RVA 0x36D4BC20 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Bridge Domain vlan ID value。

[候选注册 R-fa3e3b684ff5492e](../../evidence/conditional_registrations-sets-003.md#r-fa3e3b684ff5492e) · [条件 C-0ba0c38a5a63c5e1](../../evidence/conditions-sets-005.md#c-0ba0c38a5a63c5e1) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-060a18f73160f0c5](../../evidence/parameters-sets-001.md#p-060a18f73160f0c5)

### static_slot_creation_candidates-004035

```text
(config-vfi)# bridge-domain <number:dynamic> <cr>
```

Handler ` RVA 0x1AA3B390 `；selector ` 4 `；EOL ` RVA 0x36D4E708 `。

模式根 ` RVA 0x36D4BC20 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Bridge Domain ID value。

[候选注册 R-fa3e3b684ff5492e](../../evidence/conditional_registrations-sets-003.md#r-fa3e3b684ff5492e) · [条件 C-9ed8b0a3c565aecd](../../evidence/conditions-sets-061.md#c-9ed8b0a3c565aecd) · [缺口 G-a87b2b0e3f0cfb19](../../evidence/gaps-sets-006.md#g-a87b2b0e3f0cfb19) · [参数 P-6746756a1f83df13](../../evidence/parameters-sets-008.md#p-6746756a1f83df13)

### static_slot_creation_candidates-004022

```text
(config-vfi)# default auto-route-target <cr>
```

Handler ` RVA 0x1AA3B390 `；selector ` 7 `；EOL ` RVA 0x36D4F9D8 `。

模式根 ` RVA 0x36D4BC20 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-fa3e3b684ff5492e](../../evidence/conditional_registrations-sets-003.md#r-fa3e3b684ff5492e) · [条件 C-94cf47bdc927f26b](../../evidence/conditions-sets-058.md#c-94cf47bdc927f26b) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-ea1bc92bafd27520](../../evidence/state_effects-sets-050.md#s-ea1bc92bafd27520)

### static_slot_creation_candidates-004015

```text
(config-vfi)# default bridge-domain <cr>
```

Handler ` RVA 0x1AA3B390 `；selector ` 4 `；EOL ` RVA 0x36D4E708 `。

模式根 ` RVA 0x36D4BC20 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-fa3e3b684ff5492e](../../evidence/conditional_registrations-sets-003.md#r-fa3e3b684ff5492e) · [条件 C-792785f54da76f9d](../../evidence/conditions-sets-047.md#c-792785f54da76f9d) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-ea1bc92bafd27520](../../evidence/state_effects-sets-050.md#s-ea1bc92bafd27520)

### static_slot_creation_candidates-004021

```text
(config-vfi)# default description <cr>
```

Handler ` RVA 0x1AA3B390 `；selector ` 12 `；EOL ` RVA 0x36D4F430 `。

模式根 ` RVA 0x36D4BC20 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-fa3e3b684ff5492e](../../evidence/conditional_registrations-sets-003.md#r-fa3e3b684ff5492e) · [条件 C-3df8d51b2ad15460](../../evidence/conditions-sets-024.md#c-3df8d51b2ad15460) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-ea1bc92bafd27520](../../evidence/state_effects-sets-050.md#s-ea1bc92bafd27520)

### static_slot_creation_candidates-004034

```text
(config-vfi)# default forward permit l2protocol all <cr>
```

Handler ` RVA 0x1AA3B390 `；selector ` 11 `；EOL ` RVA 0x36D50500 `。

模式根 ` RVA 0x36D4BC20 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-fa3e3b684ff5492e](../../evidence/conditional_registrations-sets-003.md#r-fa3e3b684ff5492e) · [条件 C-f628b35577d8a23c](../../evidence/conditions-sets-095.md#c-f628b35577d8a23c) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-ea1bc92bafd27520](../../evidence/state_effects-sets-050.md#s-ea1bc92bafd27520)

### static_slot_creation_candidates-004017

```text
(config-vfi)# default mtu <cr>
```

Handler ` RVA 0x1AA3B390 `；selector ` 9 `；EOL ` RVA 0x36D4EB38 `。

模式根 ` RVA 0x36D4BC20 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-fa3e3b684ff5492e](../../evidence/conditional_registrations-sets-003.md#r-fa3e3b684ff5492e) · [条件 C-c440a08d64a7d60e](../../evidence/conditions-sets-076.md#c-c440a08d64a7d60e) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-ea1bc92bafd27520](../../evidence/state_effects-sets-050.md#s-ea1bc92bafd27520)

### static_slot_creation_candidates-004029

```text
(config-vfi)# default neighbor <address> <cr>
```

Handler ` RVA 0x1AA3B390 `；selector ` 3 `；EOL ` RVA 0x36D4E0F8 `。

模式根 ` RVA 0x36D4BC20 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` VFI neighbor's router id。

[候选注册 R-fa3e3b684ff5492e](../../evidence/conditional_registrations-sets-003.md#r-fa3e3b684ff5492e) · [条件 C-a5d4775c6c39c53c](../../evidence/conditions-sets-064.md#c-a5d4775c6c39c53c) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-435c1f55ede7304c](../../evidence/parameters-sets-006.md#p-435c1f55ede7304c) · [状态效果 S-e8170a3bb90549f1](../../evidence/state_effects-sets-049.md#s-e8170a3bb90549f1)

### static_slot_creation_candidates-004014

```text
(config-vfi)# default shutdown <cr>
```

Handler ` RVA 0x1AA3B390 `；selector ` 1 `；EOL ` RVA 0x36D4F0B8 `。

模式根 ` RVA 0x36D4BC20 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-fa3e3b684ff5492e](../../evidence/conditional_registrations-sets-003.md#r-fa3e3b684ff5492e) · [条件 C-2046bb31c695d061](../../evidence/conditions-sets-013.md#c-2046bb31c695d061) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-ea1bc92bafd27520](../../evidence/state_effects-sets-050.md#s-ea1bc92bafd27520)

### static_slot_creation_candidates-004027

```text
(config-vfi)# default status decoupled <cr>
```

Handler ` RVA 0x1AA3B390 `；selector ` 10 `；EOL ` RVA 0x36D4EE28 `。

模式根 ` RVA 0x36D4BC20 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-fa3e3b684ff5492e](../../evidence/conditional_registrations-sets-003.md#r-fa3e3b684ff5492e) · [条件 C-2046bb31c695d061](../../evidence/conditions-sets-013.md#c-2046bb31c695d061) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-ea1bc92bafd27520](../../evidence/state_effects-sets-050.md#s-ea1bc92bafd27520)

### static_slot_creation_candidates-004026

```text
(config-vfi)# default vpn id <cr>
```

Handler ` RVA 0x1AA3B390 `；selector ` 2 `；EOL ` RVA 0x36D4DC68 `。

模式根 ` RVA 0x36D4BC20 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-fa3e3b684ff5492e](../../evidence/conditional_registrations-sets-003.md#r-fa3e3b684ff5492e) · [条件 C-2cac2b7f0d7ed83d](../../evidence/conditions-sets-018.md#c-2cac2b7f0d7ed83d) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-ea1bc92bafd27520](../../evidence/state_effects-sets-050.md#s-ea1bc92bafd27520)

### static_slot_creation_candidates-004019

```text
(config-vfi)# description <string> <cr>
```

Handler ` RVA 0x1AA3B390 `；selector ` 12 `；EOL ` RVA 0x36D4F430 `。

模式根 ` RVA 0x36D4BC20 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` description string。

[候选注册 R-fa3e3b684ff5492e](../../evidence/conditional_registrations-sets-003.md#r-fa3e3b684ff5492e) · [条件 C-668ddfe475322374](../../evidence/conditions-sets-040.md#c-668ddfe475322374) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-b2339ac92541f92e](../../evidence/parameters-sets-014.md#p-b2339ac92541f92e)

### static_slot_creation_candidates-004032

```text
(config-vfi)# forward permit l2protocol all <cr>
```

Handler ` RVA 0x1AA3B390 `；selector ` 11 `；EOL ` RVA 0x36D50500 `。

模式根 ` RVA 0x36D4BC20 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-fa3e3b684ff5492e](../../evidence/conditional_registrations-sets-003.md#r-fa3e3b684ff5492e) · [条件 C-f628b35577d8a23c](../../evidence/conditions-sets-095.md#c-f628b35577d8a23c) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### static_slot_creation_candidates-004009

```text
(config-vfi)# mtu <cr>
```

Handler ` RVA 0x1AA3B390 `；selector ` 9 `；EOL ` RVA 0x36D4EB38 `。

模式根 ` RVA 0x36D4BC20 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-fa3e3b684ff5492e](../../evidence/conditional_registrations-sets-003.md#r-fa3e3b684ff5492e) · [条件 C-419e19048dc764a0](../../evidence/conditions-sets-026.md#c-419e19048dc764a0) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### static_slot_creation_candidates-004031

```text
(config-vfi)# neighbor <address> encapsulation mpls <cr>
```

Handler ` RVA 0x1AA3B390 `；selector ` 3 `；EOL ` RVA 0x36D4E0F8 `。

模式根 ` RVA 0x36D4BC20 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` VFI neighbor's router id。

[候选注册 R-fa3e3b684ff5492e](../../evidence/conditional_registrations-sets-003.md#r-fa3e3b684ff5492e) · [条件 C-03226f3396a7ff2f](../../evidence/conditions-sets-002.md#c-03226f3396a7ff2f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-435c1f55ede7304c](../../evidence/parameters-sets-006.md#p-435c1f55ede7304c) · [状态效果 S-815f4398313b1e2e](../../evidence/state_effects-sets-027.md#s-815f4398313b1e2e)

### static_slot_creation_candidates-004020

```text
(config-vfi)# no auto-route-target <cr>
```

Handler ` RVA 0x1AA3B390 `；selector ` 7 `；EOL ` RVA 0x36D4F9D8 `。

模式根 ` RVA 0x36D4BC20 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-fa3e3b684ff5492e](../../evidence/conditional_registrations-sets-003.md#r-fa3e3b684ff5492e) · [条件 C-94cf47bdc927f26b](../../evidence/conditions-sets-058.md#c-94cf47bdc927f26b) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-dc88a5ffbf7f5ddc](../../evidence/state_effects-sets-047.md#s-dc88a5ffbf7f5ddc)

### static_slot_creation_candidates-004013

```text
(config-vfi)# no bridge-domain <cr>
```

Handler ` RVA 0x1AA3B390 `；selector ` 4 `；EOL ` RVA 0x36D4E708 `。

模式根 ` RVA 0x36D4BC20 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-fa3e3b684ff5492e](../../evidence/conditional_registrations-sets-003.md#r-fa3e3b684ff5492e) · [条件 C-e931b2102269ce2f](../../evidence/conditions-sets-090.md#c-e931b2102269ce2f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-dc88a5ffbf7f5ddc](../../evidence/state_effects-sets-047.md#s-dc88a5ffbf7f5ddc)

### static_slot_creation_candidates-004018

```text
(config-vfi)# no description <cr>
```

Handler ` RVA 0x1AA3B390 `；selector ` 12 `；EOL ` RVA 0x36D4F430 `。

模式根 ` RVA 0x36D4BC20 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-fa3e3b684ff5492e](../../evidence/conditional_registrations-sets-003.md#r-fa3e3b684ff5492e) · [条件 C-a744bf5a093c66ab](../../evidence/conditions-sets-065.md#c-a744bf5a093c66ab) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-dc88a5ffbf7f5ddc](../../evidence/state_effects-sets-047.md#s-dc88a5ffbf7f5ddc)

### static_slot_creation_candidates-004033

```text
(config-vfi)# no forward permit l2protocol all <cr>
```

Handler ` RVA 0x1AA3B390 `；selector ` 11 `；EOL ` RVA 0x36D50500 `。

模式根 ` RVA 0x36D4BC20 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-fa3e3b684ff5492e](../../evidence/conditional_registrations-sets-003.md#r-fa3e3b684ff5492e) · [条件 C-f628b35577d8a23c](../../evidence/conditions-sets-095.md#c-f628b35577d8a23c) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-dc88a5ffbf7f5ddc](../../evidence/state_effects-sets-047.md#s-dc88a5ffbf7f5ddc)

### static_slot_creation_candidates-004016

```text
(config-vfi)# no mtu <cr>
```

Handler ` RVA 0x1AA3B390 `；selector ` 9 `；EOL ` RVA 0x36D4EB38 `。

模式根 ` RVA 0x36D4BC20 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-fa3e3b684ff5492e](../../evidence/conditional_registrations-sets-003.md#r-fa3e3b684ff5492e) · [条件 C-dfa1dcd454d01896](../../evidence/conditions-sets-086.md#c-dfa1dcd454d01896) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-dc88a5ffbf7f5ddc](../../evidence/state_effects-sets-047.md#s-dc88a5ffbf7f5ddc)

### static_slot_creation_candidates-004028

```text
(config-vfi)# no neighbor <address> <cr>
```

Handler ` RVA 0x1AA3B390 `；selector ` 3 `；EOL ` RVA 0x36D4E0F8 `。

模式根 ` RVA 0x36D4BC20 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` VFI neighbor's router id。

[候选注册 R-fa3e3b684ff5492e](../../evidence/conditional_registrations-sets-003.md#r-fa3e3b684ff5492e) · [条件 C-64d000a14da86f05](../../evidence/conditions-sets-039.md#c-64d000a14da86f05) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-435c1f55ede7304c](../../evidence/parameters-sets-006.md#p-435c1f55ede7304c) · [状态效果 S-cb8551856a78fc56](../../evidence/state_effects-sets-043.md#s-cb8551856a78fc56)

### static_slot_creation_candidates-004012

```text
(config-vfi)# no shutdown <cr>
```

Handler ` RVA 0x1AA3B390 `；selector ` 1 `；EOL ` RVA 0x36D4F0B8 `。

模式根 ` RVA 0x36D4BC20 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-fa3e3b684ff5492e](../../evidence/conditional_registrations-sets-003.md#r-fa3e3b684ff5492e) · [条件 C-2046bb31c695d061](../../evidence/conditions-sets-013.md#c-2046bb31c695d061) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-dc88a5ffbf7f5ddc](../../evidence/state_effects-sets-047.md#s-dc88a5ffbf7f5ddc)

### static_slot_creation_candidates-004024

```text
(config-vfi)# no status decoupled <cr>
```

Handler ` RVA 0x1AA3B390 `；selector ` 10 `；EOL ` RVA 0x36D4EE28 `。

模式根 ` RVA 0x36D4BC20 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-fa3e3b684ff5492e](../../evidence/conditional_registrations-sets-003.md#r-fa3e3b684ff5492e) · [条件 C-2046bb31c695d061](../../evidence/conditions-sets-013.md#c-2046bb31c695d061) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-dc88a5ffbf7f5ddc](../../evidence/state_effects-sets-047.md#s-dc88a5ffbf7f5ddc)

### static_slot_creation_candidates-004023

```text
(config-vfi)# no vpn id <cr>
```

Handler ` RVA 0x1AA3B390 `；selector ` 2 `；EOL ` RVA 0x36D4DC68 `。

模式根 ` RVA 0x36D4BC20 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-fa3e3b684ff5492e](../../evidence/conditional_registrations-sets-003.md#r-fa3e3b684ff5492e) · [条件 C-d3d864a95316ad98](../../evidence/conditions-sets-082.md#c-d3d864a95316ad98) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-dc88a5ffbf7f5ddc](../../evidence/state_effects-sets-047.md#s-dc88a5ffbf7f5ddc)

### static_slot_creation_candidates-004036

```text
(config-vfi)# rd <?vrf_rd_action@55558c2a36f0> <cr>
```

Handler ` RVA 0x1AA3B390 `；selector ` 5 `；EOL ` RVA 0x36D4F758 `。

模式根 ` RVA 0x36D4BC20 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[候选注册 R-fa3e3b684ff5492e](../../evidence/conditional_registrations-sets-003.md#r-fa3e3b684ff5492e) · [条件 C-94cf47bdc927f26b](../../evidence/conditions-sets-058.md#c-94cf47bdc927f26b) · [缺口 G-acdf5a6debba3c64](../../evidence/gaps-sets-006.md#g-acdf5a6debba3c64)

### static_slot_creation_candidates-004038

```text
(config-vfi)# route-target <?bgp_extcomm_action@55558c2a3d68> <cr>
```

Handler ` RVA 0x1AA3B390 `；selector ` 8 `；EOL ` RVA 0x36D4FDA0 `。

模式根 ` RVA 0x36D4BC20 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[候选注册 R-fa3e3b684ff5492e](../../evidence/conditional_registrations-sets-003.md#r-fa3e3b684ff5492e) · [条件 C-94cf47bdc927f26b](../../evidence/conditions-sets-058.md#c-94cf47bdc927f26b) · [缺口 G-eaaf0e54cef766a9](../../evidence/gaps-sets-008.md#g-eaaf0e54cef766a9) · [状态效果 S-bd2c92785a33f7ac](../../evidence/state_effects-sets-040.md#s-bd2c92785a33f7ac)

### static_slot_creation_candidates-004008

```text
(config-vfi)# shutdown <cr>
```

Handler ` RVA 0x1AA3B390 `；selector ` 1 `；EOL ` RVA 0x36D4F0B8 `。

模式根 ` RVA 0x36D4BC20 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-fa3e3b684ff5492e](../../evidence/conditional_registrations-sets-003.md#r-fa3e3b684ff5492e) · [条件 C-2046bb31c695d061](../../evidence/conditions-sets-013.md#c-2046bb31c695d061) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### static_slot_creation_candidates-004011

```text
(config-vfi)# status decoupled <cr>
```

Handler ` RVA 0x1AA3B390 `；selector ` 10 `；EOL ` RVA 0x36D4EE28 `。

模式根 ` RVA 0x36D4BC20 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-fa3e3b684ff5492e](../../evidence/conditional_registrations-sets-003.md#r-fa3e3b684ff5492e) · [条件 C-2046bb31c695d061](../../evidence/conditions-sets-013.md#c-2046bb31c695d061) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### static_slot_creation_candidates-004037

```text
(config-vfi)# vpls-id <?bgp_extcomm_action@55558c2a40b0> <cr>
```

Handler ` RVA 0x1AA3B390 `；selector ` 6 `；EOL ` RVA 0x36D500E8 `。

模式根 ` RVA 0x36D4BC20 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[候选注册 R-fa3e3b684ff5492e](../../evidence/conditional_registrations-sets-003.md#r-fa3e3b684ff5492e) · [条件 C-94cf47bdc927f26b](../../evidence/conditions-sets-058.md#c-94cf47bdc927f26b) · [缺口 G-c17b158b2f24fb8f](../../evidence/gaps-sets-007.md#g-c17b158b2f24fb8f) · [状态效果 S-139f2f558ccc2d4a](../../evidence/state_effects-sets-005.md#s-139f2f558ccc2d4a)

### static_slot_creation_candidates-004025

```text
(config-vfi)# vpn id <number:1..4294967295> <cr>
```

Handler ` RVA 0x1AA3B390 `；selector ` 2 `；EOL ` RVA 0x36D4DC68 `。

模式根 ` RVA 0x36D4BC20 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` VPN id value。

[候选注册 R-fa3e3b684ff5492e](../../evidence/conditional_registrations-sets-003.md#r-fa3e3b684ff5492e) · [条件 C-d8512f54cef2ac44](../../evidence/conditions-sets-083.md#c-d8512f54cef2ac44) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-1ced6523ee633a81](../../evidence/parameters-sets-003.md#p-1ced6523ee633a81)
