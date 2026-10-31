# l2vpn-vfi · 依赖静态建槽的条件安装

[模式索引](README.md) · [总索引](../../README.md)

### static_slot_creation_candidates-004230

```text
(config-vfi)# autodiscovery bgp signaling bgp <cr>
```

Handler ` RVA 0x1AA432F0 `；selector ` 0 `；EOL ` RVA 0x36D53A68 `。

模式根 ` RVA 0x36D4BC48 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-9c0cd6f0b935cb6a](../../evidence/conditional_registrations-sets-002.md#r-9c0cd6f0b935cb6a) · [条件 C-b4f26f9e2e312dee](../../evidence/conditions-sets-070.md#c-b4f26f9e2e312dee) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-25dea22d6f0a9180](../../evidence/state_effects-sets-008.md#s-25dea22d6f0a9180)

### static_slot_creation_candidates-004234

```text
(config-vfi)# default autodiscovery bgp signaling bgp <cr>
```

Handler ` RVA 0x1AA432F0 `；selector ` 0 `；EOL ` RVA 0x36D53A68 `。

模式根 ` RVA 0x36D4BC48 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-9c0cd6f0b935cb6a](../../evidence/conditional_registrations-sets-002.md#r-9c0cd6f0b935cb6a) · [条件 C-b4f26f9e2e312dee](../../evidence/conditions-sets-070.md#c-b4f26f9e2e312dee) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-65d93ecff847245c](../../evidence/state_effects-sets-022.md#s-65d93ecff847245c)

### static_slot_creation_candidates-004223

```text
(config-vfi)# default evc <string> <cr>
```

Handler ` RVA 0x1AA48BB0 `；selector ` 0 `；EOL ` RVA 0x36D53110 `。

模式根 ` RVA 0x36D4BC48 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` EVC name (Max size 32)。

[候选注册 R-9c0cd6f0b935cb6a](../../evidence/conditional_registrations-sets-002.md#r-9c0cd6f0b935cb6a) · [条件 C-6a4d202b5c0c2c88](../../evidence/conditions-sets-041.md#c-6a4d202b5c0c2c88) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-f583b448c6723b09](../../evidence/parameters-sets-018.md#p-f583b448c6723b09) · [状态效果 S-41ac6db0fa248b7e](../../evidence/state_effects-sets-014.md#s-41ac6db0fa248b7e)

### static_slot_creation_candidates-004219

```text
(config-vfi)# default evpn ethernet-segment <cr>
```

Handler ` RVA 0x1AA42FC0 `；selector ` 0 `；EOL ` RVA 0x36D50CE8 `。

模式根 ` RVA 0x36D4BC48 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-9c0cd6f0b935cb6a](../../evidence/conditional_registrations-sets-002.md#r-9c0cd6f0b935cb6a) · [条件 C-c25c40def5c05b3f](../../evidence/conditions-sets-075.md#c-c25c40def5c05b3f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-41ac6db0fa248b7e](../../evidence/state_effects-sets-014.md#s-41ac6db0fa248b7e)

### static_slot_creation_candidates-004232

```text
(config-vfi)# default forward permit l2protocol all <cr>
```

Handler ` RVA 0x1AA3FF90 `；selector ` 0 `；EOL ` RVA 0x36D510A8 `。

模式根 ` RVA 0x36D4BC48 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-9c0cd6f0b935cb6a](../../evidence/conditional_registrations-sets-002.md#r-9c0cd6f0b935cb6a) · [条件 C-0fcce061d805f5cd](../../evidence/conditions-sets-006.md#c-0fcce061d805f5cd) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-41ac6db0fa248b7e](../../evidence/state_effects-sets-014.md#s-41ac6db0fa248b7e)

### static_slot_creation_candidates-004226

```text
(config-vfi)# default l2protocol forward <cr>
```

Handler ` RVA 0x1AA40040 `；selector ` 0 `；EOL ` RVA 0x36D522D0 `。

模式根 ` RVA 0x36D4BC48 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-9c0cd6f0b935cb6a](../../evidence/conditional_registrations-sets-002.md#r-9c0cd6f0b935cb6a) · [条件 C-8b07c420795f7b5a](../../evidence/conditions-sets-054.md#c-8b07c420795f7b5a) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-4fb3505bbb0d8864](../../evidence/state_effects-sets-017.md#s-4fb3505bbb0d8864)

### static_slot_creation_candidates-004229

```text
(config-vfi)# default member pseudowire <number:1..100000> <cr>
```

Handler ` RVA 0x1AA415B0 `；selector ` 0 `；EOL ` RVA 0x36D534D0 `。

模式根 ` RVA 0x36D4BC48 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Pseudowire interface number。

[候选注册 R-9c0cd6f0b935cb6a](../../evidence/conditional_registrations-sets-002.md#r-9c0cd6f0b935cb6a) · [条件 C-6a4d202b5c0c2c88](../../evidence/conditions-sets-041.md#c-6a4d202b5c0c2c88) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-09d1945b011960eb](../../evidence/parameters-sets-001.md#p-09d1945b011960eb) · [状态效果 S-41ac6db0fa248b7e](../../evidence/state_effects-sets-014.md#s-41ac6db0fa248b7e)

### static_slot_creation_candidates-004211

```text
(config-vfi)# default mtu <cr>
```

Handler ` RVA 0x1AA42D90 `；selector ` 0 `；EOL ` RVA 0x36D52880 `。

模式根 ` RVA 0x36D4BC48 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-9c0cd6f0b935cb6a](../../evidence/conditional_registrations-sets-002.md#r-9c0cd6f0b935cb6a) · [条件 C-39b3f7c6589cc363](../../evidence/conditions-sets-022.md#c-39b3f7c6589cc363) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-41ac6db0fa248b7e](../../evidence/state_effects-sets-014.md#s-41ac6db0fa248b7e)

### static_slot_creation_candidates-004210

```text
(config-vfi)# default shutdown <cr>
```

Handler ` RVA 0x1AA3FBD0 `；selector ` 0 `；EOL ` RVA 0x36D52E00 `。

模式根 ` RVA 0x36D4BC48 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-9c0cd6f0b935cb6a](../../evidence/conditional_registrations-sets-002.md#r-9c0cd6f0b935cb6a) · [条件 C-6a4d202b5c0c2c88](../../evidence/conditions-sets-041.md#c-6a4d202b5c0c2c88) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-41ac6db0fa248b7e](../../evidence/state_effects-sets-014.md#s-41ac6db0fa248b7e)

### static_slot_creation_candidates-004221

```text
(config-vfi)# default status decoupled <cr>
```

Handler ` RVA 0x1AA40880 `；selector ` 0 `；EOL ` RVA 0x36D52B70 `。

模式根 ` RVA 0x36D4BC48 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-9c0cd6f0b935cb6a](../../evidence/conditional_registrations-sets-002.md#r-9c0cd6f0b935cb6a) · [条件 C-6a4d202b5c0c2c88](../../evidence/conditions-sets-041.md#c-6a4d202b5c0c2c88) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-41ac6db0fa248b7e](../../evidence/state_effects-sets-014.md#s-41ac6db0fa248b7e)

### static_slot_creation_candidates-004216

```text
(config-vfi)# default vpn id <cr>
```

Handler ` RVA 0x1AA40990 `；selector ` 0 `；EOL ` RVA 0x36D50900 `。

模式根 ` RVA 0x36D4BC48 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-9c0cd6f0b935cb6a](../../evidence/conditional_registrations-sets-002.md#r-9c0cd6f0b935cb6a) · [条件 C-22f4b3881bc1945c](../../evidence/conditions-sets-014.md#c-22f4b3881bc1945c) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-41ac6db0fa248b7e](../../evidence/state_effects-sets-014.md#s-41ac6db0fa248b7e)

### static_slot_creation_candidates-004212

```text
(config-vfi)# evc <string> <cr>
```

Handler ` RVA 0x1AA48BB0 `；selector ` 0 `；EOL ` RVA 0x36D53110 `。

模式根 ` RVA 0x36D4BC48 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` EVC name (Max size 32)。

[候选注册 R-9c0cd6f0b935cb6a](../../evidence/conditional_registrations-sets-002.md#r-9c0cd6f0b935cb6a) · [条件 C-6a4d202b5c0c2c88](../../evidence/conditions-sets-041.md#c-6a4d202b5c0c2c88) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-f583b448c6723b09](../../evidence/parameters-sets-018.md#p-f583b448c6723b09)

### static_slot_creation_candidates-004218

```text
(config-vfi)# evpn ethernet-segment <number:1..65535> <cr>
```

Handler ` RVA 0x1AA42FC0 `；selector ` 0 `；EOL ` RVA 0x36D50CE8 `。

模式根 ` RVA 0x36D4BC48 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Ethernet segment local discriminator value。

[候选注册 R-9c0cd6f0b935cb6a](../../evidence/conditional_registrations-sets-002.md#r-9c0cd6f0b935cb6a) · [条件 C-e95b0ccbffe17170](../../evidence/conditions-sets-090.md#c-e95b0ccbffe17170) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-6551d60327e029ba](../../evidence/parameters-sets-008.md#p-6551d60327e029ba)

### static_slot_creation_candidates-004227

```text
(config-vfi)# forward permit l2protocol all <cr>
```

Handler ` RVA 0x1AA3FF90 `；selector ` 0 `；EOL ` RVA 0x36D510A8 `。

模式根 ` RVA 0x36D4BC48 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-9c0cd6f0b935cb6a](../../evidence/conditional_registrations-sets-002.md#r-9c0cd6f0b935cb6a) · [条件 C-0fcce061d805f5cd](../../evidence/conditions-sets-006.md#c-0fcce061d805f5cd) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### static_slot_creation_candidates-004213

```text
(config-vfi)# l2protocol forward <cr>
```

Handler ` RVA 0x1AA40040 `；selector ` 0 `；EOL ` RVA 0x36D522D0 `。

模式根 ` RVA 0x36D4BC48 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-9c0cd6f0b935cb6a](../../evidence/conditional_registrations-sets-002.md#r-9c0cd6f0b935cb6a) · [条件 C-8b07c420795f7b5a](../../evidence/conditions-sets-054.md#c-8b07c420795f7b5a) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-08d8315d63ce1f9e](../../evidence/state_effects-sets-002.md#s-08d8315d63ce1f9e)

### static_slot_creation_candidates-004224

```text
(config-vfi)# member pseudowire <number:1..100000> <cr>
```

Handler ` RVA 0x1AA415B0 `；selector ` 0 `；EOL ` RVA 0x36D534D0 `。

模式根 ` RVA 0x36D4BC48 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Pseudowire interface number。

[候选注册 R-9c0cd6f0b935cb6a](../../evidence/conditional_registrations-sets-002.md#r-9c0cd6f0b935cb6a) · [条件 C-6a4d202b5c0c2c88](../../evidence/conditions-sets-041.md#c-6a4d202b5c0c2c88) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-09d1945b011960eb](../../evidence/parameters-sets-001.md#p-09d1945b011960eb)

### static_slot_creation_candidates-004209

```text
(config-vfi)# mtu <number:1500..9180> <cr>
```

Handler ` RVA 0x1AA42D90 `；selector ` 0 `；EOL ` RVA 0x36D52880 `。

模式根 ` RVA 0x36D4BC48 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Maximum Transmission Unit value。

[候选注册 R-9c0cd6f0b935cb6a](../../evidence/conditional_registrations-sets-002.md#r-9c0cd6f0b935cb6a) · [条件 C-d942160f92d63d42](../../evidence/conditions-sets-084.md#c-d942160f92d63d42) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-4cca8e02f2d72281](../../evidence/parameters-sets-006.md#p-4cca8e02f2d72281)

### static_slot_creation_candidates-004233

```text
(config-vfi)# no autodiscovery bgp signaling bgp <cr>
```

Handler ` RVA 0x1AA432F0 `；selector ` 0 `；EOL ` RVA 0x36D53A68 `。

模式根 ` RVA 0x36D4BC48 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-9c0cd6f0b935cb6a](../../evidence/conditional_registrations-sets-002.md#r-9c0cd6f0b935cb6a) · [条件 C-b4f26f9e2e312dee](../../evidence/conditions-sets-070.md#c-b4f26f9e2e312dee) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-440afc3dcf181473](../../evidence/state_effects-sets-015.md#s-440afc3dcf181473)

### static_slot_creation_candidates-004222

```text
(config-vfi)# no evc <string> <cr>
```

Handler ` RVA 0x1AA48BB0 `；selector ` 0 `；EOL ` RVA 0x36D53110 `。

模式根 ` RVA 0x36D4BC48 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` EVC name (Max size 32)。

[候选注册 R-9c0cd6f0b935cb6a](../../evidence/conditional_registrations-sets-002.md#r-9c0cd6f0b935cb6a) · [条件 C-6a4d202b5c0c2c88](../../evidence/conditions-sets-041.md#c-6a4d202b5c0c2c88) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-f583b448c6723b09](../../evidence/parameters-sets-018.md#p-f583b448c6723b09) · [状态效果 S-e18bd6d98de31e0f](../../evidence/state_effects-sets-048.md#s-e18bd6d98de31e0f)

### static_slot_creation_candidates-004217

```text
(config-vfi)# no evpn ethernet-segment <cr>
```

Handler ` RVA 0x1AA42FC0 `；selector ` 0 `；EOL ` RVA 0x36D50CE8 `。

模式根 ` RVA 0x36D4BC48 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-9c0cd6f0b935cb6a](../../evidence/conditional_registrations-sets-002.md#r-9c0cd6f0b935cb6a) · [条件 C-07d1f2f14009b915](../../evidence/conditions-sets-003.md#c-07d1f2f14009b915) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-e18bd6d98de31e0f](../../evidence/state_effects-sets-048.md#s-e18bd6d98de31e0f)

### static_slot_creation_candidates-004231

```text
(config-vfi)# no forward permit l2protocol all <cr>
```

Handler ` RVA 0x1AA3FF90 `；selector ` 0 `；EOL ` RVA 0x36D510A8 `。

模式根 ` RVA 0x36D4BC48 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-9c0cd6f0b935cb6a](../../evidence/conditional_registrations-sets-002.md#r-9c0cd6f0b935cb6a) · [条件 C-0fcce061d805f5cd](../../evidence/conditions-sets-006.md#c-0fcce061d805f5cd) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-e18bd6d98de31e0f](../../evidence/state_effects-sets-048.md#s-e18bd6d98de31e0f)

### static_slot_creation_candidates-004225

```text
(config-vfi)# no l2protocol forward <cr>
```

Handler ` RVA 0x1AA40040 `；selector ` 0 `；EOL ` RVA 0x36D522D0 `。

模式根 ` RVA 0x36D4BC48 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-9c0cd6f0b935cb6a](../../evidence/conditional_registrations-sets-002.md#r-9c0cd6f0b935cb6a) · [条件 C-8b07c420795f7b5a](../../evidence/conditions-sets-054.md#c-8b07c420795f7b5a) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-71162877873a7938](../../evidence/state_effects-sets-024.md#s-71162877873a7938)

### static_slot_creation_candidates-004228

```text
(config-vfi)# no member pseudowire <number:1..100000> <cr>
```

Handler ` RVA 0x1AA415B0 `；selector ` 0 `；EOL ` RVA 0x36D534D0 `。

模式根 ` RVA 0x36D4BC48 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Pseudowire interface number。

[候选注册 R-9c0cd6f0b935cb6a](../../evidence/conditional_registrations-sets-002.md#r-9c0cd6f0b935cb6a) · [条件 C-6a4d202b5c0c2c88](../../evidence/conditions-sets-041.md#c-6a4d202b5c0c2c88) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-09d1945b011960eb](../../evidence/parameters-sets-001.md#p-09d1945b011960eb) · [状态效果 S-e18bd6d98de31e0f](../../evidence/state_effects-sets-048.md#s-e18bd6d98de31e0f)

### static_slot_creation_candidates-004208

```text
(config-vfi)# no mtu <cr>
```

Handler ` RVA 0x1AA42D90 `；selector ` 0 `；EOL ` RVA 0x36D52880 `。

模式根 ` RVA 0x36D4BC48 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-9c0cd6f0b935cb6a](../../evidence/conditional_registrations-sets-002.md#r-9c0cd6f0b935cb6a) · [条件 C-dd6ddb549ddef5fd](../../evidence/conditions-sets-085.md#c-dd6ddb549ddef5fd) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-e18bd6d98de31e0f](../../evidence/state_effects-sets-048.md#s-e18bd6d98de31e0f)

### static_slot_creation_candidates-004207

```text
(config-vfi)# no shutdown <cr>
```

Handler ` RVA 0x1AA3FBD0 `；selector ` 0 `；EOL ` RVA 0x36D52E00 `。

模式根 ` RVA 0x36D4BC48 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-9c0cd6f0b935cb6a](../../evidence/conditional_registrations-sets-002.md#r-9c0cd6f0b935cb6a) · [条件 C-6a4d202b5c0c2c88](../../evidence/conditions-sets-041.md#c-6a4d202b5c0c2c88) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-e18bd6d98de31e0f](../../evidence/state_effects-sets-048.md#s-e18bd6d98de31e0f)

### static_slot_creation_candidates-004220

```text
(config-vfi)# no status decoupled <cr>
```

Handler ` RVA 0x1AA40880 `；selector ` 0 `；EOL ` RVA 0x36D52B70 `。

模式根 ` RVA 0x36D4BC48 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-9c0cd6f0b935cb6a](../../evidence/conditional_registrations-sets-002.md#r-9c0cd6f0b935cb6a) · [条件 C-6a4d202b5c0c2c88](../../evidence/conditions-sets-041.md#c-6a4d202b5c0c2c88) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-e18bd6d98de31e0f](../../evidence/state_effects-sets-048.md#s-e18bd6d98de31e0f)

### static_slot_creation_candidates-004214

```text
(config-vfi)# no vpn id <cr>
```

Handler ` RVA 0x1AA40990 `；selector ` 0 `；EOL ` RVA 0x36D50900 `。

模式根 ` RVA 0x36D4BC48 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-9c0cd6f0b935cb6a](../../evidence/conditional_registrations-sets-002.md#r-9c0cd6f0b935cb6a) · [条件 C-e54d69d2c2cba296](../../evidence/conditions-sets-088.md#c-e54d69d2c2cba296) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-e18bd6d98de31e0f](../../evidence/state_effects-sets-048.md#s-e18bd6d98de31e0f)

### static_slot_creation_candidates-004205

```text
(config-vfi)# shutdown <cr>
```

Handler ` RVA 0x1AA3FBD0 `；selector ` 0 `；EOL ` RVA 0x36D52E00 `。

模式根 ` RVA 0x36D4BC48 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-9c0cd6f0b935cb6a](../../evidence/conditional_registrations-sets-002.md#r-9c0cd6f0b935cb6a) · [条件 C-6a4d202b5c0c2c88](../../evidence/conditions-sets-041.md#c-6a4d202b5c0c2c88) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### static_slot_creation_candidates-004206

```text
(config-vfi)# status decoupled <cr>
```

Handler ` RVA 0x1AA40880 `；selector ` 0 `；EOL ` RVA 0x36D52B70 `。

模式根 ` RVA 0x36D4BC48 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-9c0cd6f0b935cb6a](../../evidence/conditional_registrations-sets-002.md#r-9c0cd6f0b935cb6a) · [条件 C-6a4d202b5c0c2c88](../../evidence/conditions-sets-041.md#c-6a4d202b5c0c2c88) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### static_slot_creation_candidates-004215

```text
(config-vfi)# vpn id <number:1..4294967295> <cr>
```

Handler ` RVA 0x1AA40990 `；selector ` 0 `；EOL ` RVA 0x36D50900 `。

模式根 ` RVA 0x36D4BC48 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` VPN id value。

[候选注册 R-9c0cd6f0b935cb6a](../../evidence/conditional_registrations-sets-002.md#r-9c0cd6f0b935cb6a) · [条件 C-ed02f815175f930f](../../evidence/conditions-sets-092.md#c-ed02f815175f930f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-8b2db15bde260a2f](../../evidence/parameters-sets-011.md#p-8b2db15bde260a2f)

