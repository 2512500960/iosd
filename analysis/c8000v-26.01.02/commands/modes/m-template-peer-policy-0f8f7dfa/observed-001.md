# template-peer-policy · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-004593

```text
(config-router-ptmp)# accept-route-legacy-rt <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 71 `；EOL ` RVA 0x345A9F00 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3b1f652ba27b5bae](../../evidence/conditions-sets-023.md#c-3b1f652ba27b5bae)

### observed_connections-004596

```text
(config-router-ptmp)# activate <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 35 `；EOL ` RVA 0x345AD1B8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-57f098c5222cef48](../../evidence/conditions-sets-034.md#c-57f098c5222cef48)

### observed_connections-004671

```text
(config-router-ptmp)# additional-paths disable <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 79 `；EOL ` RVA 0x345AA8E0 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0a5690d4f18d41f1](../../evidence/conditions-sets-004.md#c-0a5690d4f18d41f1) · [状态效果 S-63d1148776fc9bd7](../../evidence/state_effects-sets-021.md#s-63d1148776fc9bd7)

### observed_connections-004684

```text
(config-router-ptmp)# advertise additional-paths <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 78 `；EOL ` RVA 0x345AAFE8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a53b18a12f143564](../../evidence/conditions-sets-064.md#c-a53b18a12f143564) · [状态效果 S-9a0d3e79641784e0](../../evidence/state_effects-sets-033.md#s-9a0d3e79641784e0)

### observed_connections-004674

```text
(config-router-ptmp)# advertise best-external <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 80 `；EOL ` RVA 0x345AB698 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-13f51add8edb73c9](../../evidence/conditions-sets-008.md#c-13f51add8edb73c9)

### observed_connections-004747

```text
(config-router-ptmp)# advertise diverse-path mpath <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 78 `；EOL ` RVA 0x345AB3B8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-13f51add8edb73c9](../../evidence/conditions-sets-008.md#c-13f51add8edb73c9) · [状态效果 S-281ed0064f02805a](../../evidence/state_effects-sets-009.md#s-281ed0064f02805a)

### observed_connections-004603

```text
(config-router-ptmp)# advertise-gw-ip-disable <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 88 `；EOL ` RVA 0x345B15B0 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2d47db81b834ef19](../../evidence/conditions-sets-018.md#c-2d47db81b834ef19)

### observed_connections-004793

```text
(config-router-ptmp)# advertise-map <string> non-exist-map <string> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 39 `；EOL ` RVA 0x345AD9E8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` advertise route-map name；` string ` condition route-map name。

[条件 C-b93d06816a29c292](../../evidence/conditions-sets-072.md#c-b93d06816a29c292) · [参数 P-948a86beed6fd9ec](../../evidence/parameters-sets-011.md#p-948a86beed6fd9ec) · [状态效果 S-83aac9888957f5de](../../evidence/state_effects-sets-028.md#s-83aac9888957f5de)

### observed_connections-004635

```text
(config-router-ptmp)# advertisement-interval <number:0..600> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 40 `；EOL ` RVA 0x345A5470 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` time in seconds。

[条件 C-8dcf3ef3b99a7587](../../evidence/conditions-sets-055.md#c-8dcf3ef3b99a7587) · [参数 P-ace004c29c81ea95](../../evidence/parameters-sets-013.md#p-ace004c29c81ea95)

### observed_connections-004594

```text
(config-router-ptmp)# aigp <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 50 `；EOL ` RVA 0x345A9B00 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3539c9553c518c8a](../../evidence/conditions-sets-021.md#c-3539c9553c518c8a) · [状态效果 S-1b6266e3e5f91549](../../evidence/state_effects-sets-006.md#s-1b6266e3e5f91549)

### observed_connections-004813

```text
(config-router-ptmp)# aigp send cost-community <number:0..255> poi igp-cost <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 50 `；EOL ` RVA 0x345A9B00 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Community ID。

[条件 C-3539c9553c518c8a](../../evidence/conditions-sets-021.md#c-3539c9553c518c8a) · [缺口 G-20423952136d1c8e](../../evidence/gaps-sets-002.md#g-20423952136d1c8e) · [参数 P-eaa29377c7d8e194](../../evidence/parameters-sets-018.md#p-eaa29377c7d8e194) · [状态效果 S-a373128c547c7de3](../../evidence/state_effects-sets-035.md#s-a373128c547c7de3)

### observed_connections-004595

```text
(config-router-ptmp)# allow-policy <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 51 `；EOL ` RVA 0x345AA530 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e8fbca347712cd67](../../evidence/conditions-sets-090.md#c-e8fbca347712cd67)

### observed_connections-004581

```text
(config-router-ptmp)# allowas-in <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 60 `；EOL ` RVA 0x345A4210 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2efb4a45ec1093db](../../evidence/conditions-sets-018.md#c-2efb4a45ec1093db) · [状态效果 S-3991f3552aa23492](../../evidence/state_effects-sets-013.md#s-3991f3552aa23492)

### observed_connections-004728

```text
(config-router-ptmp)# announce rpki state <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 77 `；EOL ` RVA 0x345A49F8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-47496888dc91b329](../../evidence/conditions-sets-028.md#c-47496888dc91b329)

### observed_connections-004701

```text
(config-router-ptmp)# ao <string> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 22 `；EOL ` RVA 0x345B0600 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Keychain name。

[条件 C-2173407f5d5c0a2a](../../evidence/conditions-sets-013.md#c-2173407f5d5c0a2a) · [参数 P-5b8d7ea6b5cf663a](../../evidence/parameters-sets-007.md#p-5b8d7ea6b5cf663a)

### observed_connections-004598

```text
(config-router-ptmp)# as-override <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 61 `；EOL ` RVA 0x345AE498 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f721f6e9763e5885](../../evidence/conditions-sets-095.md#c-f721f6e9763e5885)

### observed_connections-004794

```text
(config-router-ptmp)# capability orf prefix-list send <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 65 `；EOL ` RVA 0x345AE8E0 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-78ad2cac013dfb1b](../../evidence/conditions-sets-047.md#c-78ad2cac013dfb1b) · [状态效果 S-41ee10a60893e991](../../evidence/state_effects-sets-014.md#s-41ee10a60893e991)

### observed_connections-004697

```text
(config-router-ptmp)# cluster-id <number:1..4294967294> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 23 `；EOL ` RVA 0x345B09C8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Route-Reflector Cluster-id as 32 bit quantity。

[条件 C-5ff8bd07b6e9ae90](../../evidence/conditions-sets-037.md#c-5ff8bd07b6e9ae90) · [参数 P-fb4fb988bd818062](../../evidence/parameters-sets-019.md#p-fb4fb988bd818062)

### observed_connections-004601

```text
(config-router-ptmp)# default <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 0 `；EOL ` RVA 0x345AF110 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b9edc2fb9fefc7e0](../../evidence/conditions-sets-072.md#c-b9edc2fb9fefc7e0) · [状态效果 S-0fdf32c40bd8ff0a](../../evidence/state_effects-sets-004.md#s-0fdf32c40bd8ff0a)

### observed_connections-004665

```text
(config-router-ptmp)# default accept-route-legacy-rt <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 71 `；EOL ` RVA 0x345A9F00 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3b1f652ba27b5bae](../../evidence/conditions-sets-023.md#c-3b1f652ba27b5bae) · [状态效果 S-0fdf32c40bd8ff0a](../../evidence/state_effects-sets-004.md#s-0fdf32c40bd8ff0a)

### observed_connections-004682

```text
(config-router-ptmp)# default activate <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 35 `；EOL ` RVA 0x345AD1B8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-57f098c5222cef48](../../evidence/conditions-sets-034.md#c-57f098c5222cef48) · [状态效果 S-0fdf32c40bd8ff0a](../../evidence/state_effects-sets-004.md#s-0fdf32c40bd8ff0a)

### observed_connections-004672

```text
(config-router-ptmp)# default additional-paths <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 79 `；EOL ` RVA 0x345AA8E0 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-801298a7901687a0](../../evidence/conditions-sets-050.md#c-801298a7901687a0) · [状态效果 S-e41d4c65920eff0f](../../evidence/state_effects-sets-048.md#s-e41d4c65920eff0f)

### observed_connections-004752

```text
(config-router-ptmp)# default advertise additional-paths <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 78 `；EOL ` RVA 0x345AAFE8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a53b18a12f143564](../../evidence/conditions-sets-064.md#c-a53b18a12f143564) · [状态效果 S-c2e4b6db11f32d20](../../evidence/state_effects-sets-041.md#s-c2e4b6db11f32d20)

### observed_connections-004748

```text
(config-router-ptmp)# default advertise best-external <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 80 `；EOL ` RVA 0x345AB698 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-13f51add8edb73c9](../../evidence/conditions-sets-008.md#c-13f51add8edb73c9) · [状态效果 S-0fdf32c40bd8ff0a](../../evidence/state_effects-sets-004.md#s-0fdf32c40bd8ff0a)

### observed_connections-004792

```text
(config-router-ptmp)# default advertise diverse-path mpath <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 78 `；EOL ` RVA 0x345AB3B8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-13f51add8edb73c9](../../evidence/conditions-sets-008.md#c-13f51add8edb73c9) · [状态效果 S-3edc6f8ab1ef15aa](../../evidence/state_effects-sets-014.md#s-3edc6f8ab1ef15aa)

### observed_connections-004705

```text
(config-router-ptmp)# default advertise-gw-ip-disable <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 88 `；EOL ` RVA 0x345B15B0 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2d47db81b834ef19](../../evidence/conditions-sets-018.md#c-2d47db81b834ef19) · [状态效果 S-0fdf32c40bd8ff0a](../../evidence/state_effects-sets-004.md#s-0fdf32c40bd8ff0a)

### observed_connections-004801

```text
(config-router-ptmp)# default advertise-map <string> non-exist-map <string> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 39 `；EOL ` RVA 0x345AD9E8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` advertise route-map name；` string ` condition route-map name。

[条件 C-b93d06816a29c292](../../evidence/conditions-sets-072.md#c-b93d06816a29c292) · [参数 P-948a86beed6fd9ec](../../evidence/parameters-sets-011.md#p-948a86beed6fd9ec) · [状态效果 S-d85f03d4698ceabf](../../evidence/state_effects-sets-046.md#s-d85f03d4698ceabf)

### observed_connections-004642

```text
(config-router-ptmp)# default advertisement-interval <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 40 `；EOL ` RVA 0x345A5470 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d842d517150efc60](../../evidence/conditions-sets-083.md#c-d842d517150efc60) · [状态效果 S-0fdf32c40bd8ff0a](../../evidence/state_effects-sets-004.md#s-0fdf32c40bd8ff0a)

### observed_connections-004668

```text
(config-router-ptmp)# default aigp <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 50 `；EOL ` RVA 0x345A9B00 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3539c9553c518c8a](../../evidence/conditions-sets-021.md#c-3539c9553c518c8a) · [状态效果 S-92430a122e9fa64d](../../evidence/state_effects-sets-031.md#s-92430a122e9fa64d)

### observed_connections-004669

```text
(config-router-ptmp)# default allow-policy <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 51 `；EOL ` RVA 0x345AA530 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e8fbca347712cd67](../../evidence/conditions-sets-090.md#c-e8fbca347712cd67) · [状态效果 S-0fdf32c40bd8ff0a](../../evidence/state_effects-sets-004.md#s-0fdf32c40bd8ff0a)

### observed_connections-004630

```text
(config-router-ptmp)# default allowas-in <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 60 `；EOL ` RVA 0x345A4210 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c259915e262fc587](../../evidence/conditions-sets-075.md#c-c259915e262fc587) · [状态效果 S-0fdf32c40bd8ff0a](../../evidence/state_effects-sets-004.md#s-0fdf32c40bd8ff0a)

### observed_connections-004780

```text
(config-router-ptmp)# default announce rpki state <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 77 `；EOL ` RVA 0x345A49F8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-47496888dc91b329](../../evidence/conditions-sets-028.md#c-47496888dc91b329) · [状态效果 S-0fdf32c40bd8ff0a](../../evidence/state_effects-sets-004.md#s-0fdf32c40bd8ff0a)

### observed_connections-004762

```text
(config-router-ptmp)# default ao <string> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 22 `；EOL ` RVA 0x345B0600 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Keychain name。

[条件 C-2173407f5d5c0a2a](../../evidence/conditions-sets-013.md#c-2173407f5d5c0a2a) · [参数 P-5b8d7ea6b5cf663a](../../evidence/parameters-sets-007.md#p-5b8d7ea6b5cf663a) · [状态效果 S-0fdf32c40bd8ff0a](../../evidence/state_effects-sets-004.md#s-0fdf32c40bd8ff0a)

### observed_connections-004691

```text
(config-router-ptmp)# default as-override <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 61 `；EOL ` RVA 0x345AE498 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f721f6e9763e5885](../../evidence/conditions-sets-095.md#c-f721f6e9763e5885) · [状态效果 S-0fdf32c40bd8ff0a](../../evidence/state_effects-sets-004.md#s-0fdf32c40bd8ff0a)

### observed_connections-004803

```text
(config-router-ptmp)# default capability orf prefix-list send <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 65 `；EOL ` RVA 0x345AE8E0 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-78ad2cac013dfb1b](../../evidence/conditions-sets-047.md#c-78ad2cac013dfb1b) · [状态效果 S-02abecd54b9243c0](../../evidence/state_effects-sets-001.md#s-02abecd54b9243c0)

### observed_connections-004699

```text
(config-router-ptmp)# default cluster-id <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 23 `；EOL ` RVA 0x345B09C8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-041cafddbce17313](../../evidence/conditions-sets-002.md#c-041cafddbce17313) · [状态效果 S-0fdf32c40bd8ff0a](../../evidence/state_effects-sets-004.md#s-0fdf32c40bd8ff0a)

### observed_connections-004653

```text
(config-router-ptmp)# default default-originate <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 52 `；EOL ` RVA 0x345A7F30 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d73ec397125c786e](../../evidence/conditions-sets-083.md#c-d73ec397125c786e) · [状态效果 S-0fdf32c40bd8ff0a](../../evidence/state_effects-sets-004.md#s-0fdf32c40bd8ff0a)

### observed_connections-004680

```text
(config-router-ptmp)# default description <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 8 `；EOL ` RVA 0x345ACE80 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-38c37be2d0d5da4a](../../evidence/conditions-sets-022.md#c-38c37be2d0d5da4a) · [状态效果 S-0fdf32c40bd8ff0a](../../evidence/state_effects-sets-004.md#s-0fdf32c40bd8ff0a)

### observed_connections-004627

```text
(config-router-ptmp)# default disable-connected-check <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 13 `；EOL ` RVA 0x345A3580 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c0fca8e83773218b](../../evidence/conditions-sets-075.md#c-c0fca8e83773218b) · [状态效果 S-61d81f85ee33ea4a](../../evidence/state_effects-sets-021.md#s-61d81f85ee33ea4a)

### observed_connections-004772

```text
(config-router-ptmp)# default distribute-list <number:1..199> in <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 45 `；EOL ` RVA 0x345A0708 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` IP access list number。

[条件 C-cf9cd4bf8eae2940](../../evidence/conditions-sets-080.md#c-cf9cd4bf8eae2940) · [参数 P-ef95a01c961a4d37](../../evidence/parameters-sets-018.md#p-ef95a01c961a4d37) · [状态效果 S-0cbbe9f0cf50c948](../../evidence/state_effects-sets-003.md#s-0cbbe9f0cf50c948)

### observed_connections-004621

```text
(config-router-ptmp)# default dmzlink-bw <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 63 `；EOL ` RVA 0x345A2008 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ef7d296238bbbdef](../../evidence/conditions-sets-092.md#c-ef7d296238bbbdef) · [状态效果 S-edd1b1d8f7bceefc](../../evidence/state_effects-sets-050.md#s-edd1b1d8f7bceefc)

### observed_connections-004613

```text
(config-router-ptmp)# default dont-capability-negotiate <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 16 `；EOL ` RVA 0x3459F2C8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d78a8a3a8ea10084](../../evidence/conditions-sets-083.md#c-d78a8a3a8ea10084) · [状态效果 S-0fdf32c40bd8ff0a](../../evidence/state_effects-sets-004.md#s-0fdf32c40bd8ff0a)

### observed_connections-004717

```text
(config-router-ptmp)# default dont-capability-negotiate enhanced-refresh <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 18 `；EOL ` RVA 0x3459F2A0 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d78a8a3a8ea10084](../../evidence/conditions-sets-083.md#c-d78a8a3a8ea10084) · [状态效果 S-0fdf32c40bd8ff0a](../../evidence/state_effects-sets-004.md#s-0fdf32c40bd8ff0a)

### observed_connections-004714

```text
(config-router-ptmp)# default dont-capability-negotiate four-octets-as <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 17 `；EOL ` RVA 0x3459EFF8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d78a8a3a8ea10084](../../evidence/conditions-sets-083.md#c-d78a8a3a8ea10084) · [状态效果 S-0fdf32c40bd8ff0a](../../evidence/state_effects-sets-004.md#s-0fdf32c40bd8ff0a)

### observed_connections-004651

```text
(config-router-ptmp)# default ebgp-multihop <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 6 `；EOL ` RVA 0x345A7B08 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0eb8c2565a64d50d](../../evidence/conditions-sets-006.md#c-0eb8c2565a64d50d) · [状态效果 S-1400b78dd90ebcf6](../../evidence/state_effects-sets-005.md#s-1400b78dd90ebcf6)

### observed_connections-004765

```text
(config-router-ptmp)# default encap srv6 <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 86 `；EOL ` RVA 0x345B19D8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-cd5e33ea8dcb7cd3](../../evidence/conditions-sets-079.md#c-cd5e33ea8dcb7cd3) · [状态效果 S-9747a04c7eb3a632](../../evidence/state_effects-sets-032.md#s-9747a04c7eb3a632)

### observed_connections-004633

```text
(config-router-ptmp)# default fall-over <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 26 `；EOL ` RVA 0x345A38D8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-beffd627c228829b](../../evidence/conditions-sets-074.md#c-beffd627c228829b) · [状态效果 S-160e350b9750cce9](../../evidence/state_effects-sets-005.md#s-160e350b9750cce9)

### observed_connections-004778

```text
(config-router-ptmp)# default filter-list <number:1..500> in <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 44 `；EOL ` RVA 0x345A14E8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` AS path access list。

[条件 C-b4ba027c7200d029](../../evidence/conditions-sets-070.md#c-b4ba027c7200d029) · [参数 P-38a4ff862bc4d4c2](../../evidence/parameters-sets-005.md#p-38a4ff862bc4d4c2) · [状态效果 S-1e67b016c27f5f6c](../../evidence/state_effects-sets-007.md#s-1e67b016c27f5f6c)

### observed_connections-004612

```text
(config-router-ptmp)# default force-open-collision <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 15 `；EOL ` RVA 0x3459F858 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-33a8c0691bb825f5](../../evidence/conditions-sets-020.md#c-33a8c0691bb825f5) · [状态效果 S-0fdf32c40bd8ff0a](../../evidence/state_effects-sets-004.md#s-0fdf32c40bd8ff0a)

### observed_connections-004768

```text
(config-router-ptmp)# default ha-mode graceful-restart <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 28 `；EOL ` RVA 0x3459E900 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-901645a8d31c3600](../../evidence/conditions-sets-056.md#c-901645a8d31c3600) · [状态效果 S-0fdf32c40bd8ff0a](../../evidence/state_effects-sets-004.md#s-0fdf32c40bd8ff0a)

### observed_connections-004770

```text
(config-router-ptmp)# default ha-mode sso <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 29 `；EOL ` RVA 0x3372E478 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-901645a8d31c3600](../../evidence/conditions-sets-056.md#c-901645a8d31c3600) · [状态效果 S-0fdf32c40bd8ff0a](../../evidence/state_effects-sets-004.md#s-0fdf32c40bd8ff0a)

### observed_connections-004791

```text
(config-router-ptmp)# default inherit peer-policy <string> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 36 `；EOL ` RVA 0x345ABB10 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Template name。

[条件 C-e6bb9b084507b3f2](../../evidence/conditions-sets-089.md#c-e6bb9b084507b3f2) · [参数 P-c8bcde829a191531](../../evidence/parameters-sets-015.md#p-c8bcde829a191531) · [状态效果 S-0fdf32c40bd8ff0a](../../evidence/state_effects-sets-004.md#s-0fdf32c40bd8ff0a)

### observed_connections-004789

```text
(config-router-ptmp)# default inherit peer-session <string> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 19 `；EOL ` RVA 0x345ABE28 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Template name。

[条件 C-be894983d25dd983](../../evidence/conditions-sets-074.md#c-be894983d25dd983) · [参数 P-13ad4b14a3a89da2](../../evidence/parameters-sets-002.md#p-13ad4b14a3a89da2) · [状态效果 S-0fdf32c40bd8ff0a](../../evidence/state_effects-sets-004.md#s-0fdf32c40bd8ff0a)

### observed_connections-004660

```text
(config-router-ptmp)# default inter-as-hybrid <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 72 `；EOL ` RVA 0x345A94E0 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-988f0292facf8cd9](../../evidence/conditions-sets-059.md#c-988f0292facf8cd9) · [状态效果 S-0fdf32c40bd8ff0a](../../evidence/state_effects-sets-004.md#s-0fdf32c40bd8ff0a)

### observed_connections-004689

```text
(config-router-ptmp)# default internal-vpn-client <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 82 `；EOL ` RVA 0x345AE0E0 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-593b70c1226d4d3d](../../evidence/conditions-sets-035.md#c-593b70c1226d4d3d) · [状态效果 S-0fdf32c40bd8ff0a](../../evidence/state_effects-sets-004.md#s-0fdf32c40bd8ff0a)

### observed_connections-004628

```text
(config-router-ptmp)# default local-as <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 11 `；EOL ` RVA 0x345A3108 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e0bb58e7a2b5d309](../../evidence/conditions-sets-087.md#c-e0bb58e7a2b5d309) · [状态效果 S-0fdf32c40bd8ff0a](../../evidence/state_effects-sets-004.md#s-0fdf32c40bd8ff0a)

### observed_connections-004711

```text
(config-router-ptmp)# default log-neighbor-changes <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 32 `；EOL ` RVA 0x345B2210 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c22607b97d03956e](../../evidence/conditions-sets-075.md#c-c22607b97d03956e) · [状态效果 S-0fdf32c40bd8ff0a](../../evidence/state_effects-sets-004.md#s-0fdf32c40bd8ff0a)

### observed_connections-004704

```text
(config-router-ptmp)# default long-lived-graceful-restart <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 85 `；EOL ` RVA 0x345B0DE8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1987282da6ebda40](../../evidence/conditions-sets-010.md#c-1987282da6ebda40) · [状态效果 S-0fdf32c40bd8ff0a](../../evidence/state_effects-sets-004.md#s-0fdf32c40bd8ff0a)

### observed_connections-004750

```text
(config-router-ptmp)# default maximum-prefix <number:1..2147483647> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 59 `；EOL ` RVA 0x345AC988 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` maximum no. of prefix limit。

[条件 C-fd969a8da4fd8491](../../evidence/conditions-sets-098.md#c-fd969a8da4fd8491) · [参数 P-191b055ddb98a361](../../evidence/parameters-sets-002.md#p-191b055ddb98a361) · [状态效果 S-0fdf32c40bd8ff0a](../../evidence/state_effects-sets-004.md#s-0fdf32c40bd8ff0a)

### observed_connections-004645

```text
(config-router-ptmp)# default next-hop-self <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 42 `；EOL ` RVA 0x345A66D8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3cc2906d189aa33d](../../evidence/conditions-sets-024.md#c-3cc2906d189aa33d) · [状态效果 S-0fdf32c40bd8ff0a](../../evidence/state_effects-sets-004.md#s-0fdf32c40bd8ff0a)

### observed_connections-004647

```text
(config-router-ptmp)# default next-hop-unchanged <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 43 `；EOL ` RVA 0x345A7798 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-aa406845aba91741](../../evidence/conditions-sets-066.md#c-aa406845aba91741) · [状态效果 S-0fdf32c40bd8ff0a](../../evidence/state_effects-sets-004.md#s-0fdf32c40bd8ff0a)

### observed_connections-004724

```text
(config-router-ptmp)# default orf rt-import-list <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 70 `；EOL ` RVA 0x345A10C8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-418cd2855f0401bd](../../evidence/conditions-sets-026.md#c-418cd2855f0401bd) · [状态效果 S-9312108ce5bf5b40](../../evidence/state_effects-sets-031.md#s-9312108ce5bf5b40)

### observed_connections-004615

```text
(config-router-ptmp)# default override-capability-neg <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 62 `；EOL ` RVA 0x345A0320 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b817ba1ecc562077](../../evidence/conditions-sets-071.md#c-b817ba1ecc562077) · [状态效果 S-0fdf32c40bd8ff0a](../../evidence/state_effects-sets-004.md#s-0fdf32c40bd8ff0a)

### observed_connections-004677

```text
(config-router-ptmp)# default password <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 7 `；EOL ` RVA 0x345AC540 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8c2a1ee23f3e0ee7](../../evidence/conditions-sets-054.md#c-8c2a1ee23f3e0ee7) · [状态效果 S-0fdf32c40bd8ff0a](../../evidence/state_effects-sets-004.md#s-0fdf32c40bd8ff0a)

### observed_connections-004805

```text
(config-router-ptmp)# default path-attribute treat-as-withdraw <number:1..255> in <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 27 `；EOL ` RVA 0x345AFDE0 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` path attribute type。

[条件 C-cd5e6fbd0bb23f22](../../evidence/conditions-sets-079.md#c-cd5e6fbd0bb23f22) · [参数 P-ce24450e99a47fbc](../../evidence/parameters-sets-016.md#p-ce24450e99a47fbc) · [状态效果 S-b657cd0bed55d06d](../../evidence/state_effects-sets-039.md#s-b657cd0bed55d06d)

### observed_connections-004609

```text
(config-router-ptmp)# default peer-group <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 10 `；EOL ` RVA 0x345B3398 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-cc5eca777bce2284](../../evidence/conditions-sets-079.md#c-cc5eca777bce2284) · [状态效果 S-0fdf32c40bd8ff0a](../../evidence/state_effects-sets-004.md#s-0fdf32c40bd8ff0a)

### observed_connections-004744

```text
(config-router-ptmp)# default peer-group <string> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 20 `；EOL ` RVA 0x345AC1A8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` peer-group name。

[条件 C-16f9dfd652106e63](../../evidence/conditions-sets-009.md#c-16f9dfd652106e63) · [参数 P-b044166d77593cf1](../../evidence/parameters-sets-013.md#p-b044166d77593cf1) · [状态效果 S-0fdf32c40bd8ff0a](../../evidence/state_effects-sets-004.md#s-0fdf32c40bd8ff0a)

### observed_connections-004725

```text
(config-router-ptmp)# default prefix-length-size <number:1..2> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 68 `；EOL ` RVA 0x345A1CC8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Storage size in bytes。

[条件 C-b40ff8c03848d66e](../../evidence/conditions-sets-070.md#c-b40ff8c03848d66e) · [参数 P-28a5ce03beeb709e](../../evidence/parameters-sets-004.md#p-28a5ce03beeb709e) · [状态效果 S-0fdf32c40bd8ff0a](../../evidence/state_effects-sets-004.md#s-0fdf32c40bd8ff0a)

### observed_connections-004774

```text
(config-router-ptmp)# default prefix-list <string> in <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 58 `；EOL ` RVA 0x345A0BF0 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Name of a prefix list。

[条件 C-68bc7d14c06ce41b](../../evidence/conditions-sets-041.md#c-68bc7d14c06ce41b) · [参数 P-3ba5cb7712b4d450](../../evidence/parameters-sets-005.md#p-3ba5cb7712b4d450) · [状态效果 S-51031bf2a4196f1b](../../evidence/state_effects-sets-018.md#s-51031bf2a4196f1b)

### observed_connections-004625

```text
(config-router-ptmp)# default remote-as <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 3 `；EOL ` RVA 0x345A26F0 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-92cd436f1e2bacc5](../../evidence/conditions-sets-057.md#c-92cd436f1e2bacc5) · [状态效果 S-0fdf32c40bd8ff0a](../../evidence/state_effects-sets-004.md#s-0fdf32c40bd8ff0a)

### observed_connections-004659

```text
(config-router-ptmp)# default remove-private-as <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 55 `；EOL ` RVA 0x345A8CA8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d51cc31133008bdd](../../evidence/conditions-sets-082.md#c-d51cc31133008bdd) · [状态效果 S-0fdf32c40bd8ff0a](../../evidence/state_effects-sets-004.md#s-0fdf32c40bd8ff0a)

### observed_connections-004741

```text
(config-router-ptmp)# default remove-private-as all <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 56 `；EOL ` RVA 0x345A8D10 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-331da96fb8c28112](../../evidence/conditions-sets-020.md#c-331da96fb8c28112) · [状态效果 S-0fdf32c40bd8ff0a](../../evidence/state_effects-sets-004.md#s-0fdf32c40bd8ff0a)

### observed_connections-004786

```text
(config-router-ptmp)# default remove-private-as all replace-as <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 57 `；EOL ` RVA 0x345A8CE8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-331da96fb8c28112](../../evidence/conditions-sets-020.md#c-331da96fb8c28112) · [状态效果 S-0fdf32c40bd8ff0a](../../evidence/state_effects-sets-004.md#s-0fdf32c40bd8ff0a)

### observed_connections-004777

```text
(config-router-ptmp)# default route-map <string> in <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 47 `；EOL ` RVA 0x345A18D8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Name of route map。

[条件 C-8b870d549f7da0b5](../../evidence/conditions-sets-054.md#c-8b870d549f7da0b5) · [参数 P-ceca94b6cb65eb98](../../evidence/parameters-sets-016.md#p-ceca94b6cb65eb98) · [状态效果 S-7fe74d5f6fa3b1b6](../../evidence/state_effects-sets-027.md#s-7fe74d5f6fa3b1b6)

### observed_connections-004664

```text
(config-router-ptmp)# default route-reflector-client <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 49 `；EOL ` RVA 0x345AA1F8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-619f85b0cdd0e481](../../evidence/conditions-sets-038.md#c-619f85b0cdd0e481) · [状态效果 S-0fdf32c40bd8ff0a](../../evidence/state_effects-sets-004.md#s-0fdf32c40bd8ff0a)

### observed_connections-004640

```text
(config-router-ptmp)# default send-community <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 46 `；EOL ` RVA 0x345A5C08 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-83f40b955213680f](../../evidence/conditions-sets-051.md#c-83f40b955213680f) · [状态效果 S-0fdf32c40bd8ff0a](../../evidence/state_effects-sets-004.md#s-0fdf32c40bd8ff0a)

### observed_connections-004693

```text
(config-router-ptmp)# default send-label <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 64 `；EOL ` RVA 0x345AEDE0 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-91b95d4fc7519899](../../evidence/conditions-sets-056.md#c-91b95d4fc7519899) · [状态效果 S-0fdf32c40bd8ff0a](../../evidence/state_effects-sets-004.md#s-0fdf32c40bd8ff0a)

### observed_connections-004643

```text
(config-router-ptmp)# default shutdown <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 5 `；EOL ` RVA 0x345A60A8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7e0f15475668cba2](../../evidence/conditions-sets-049.md#c-7e0f15475668cba2) · [状态效果 S-0fdf32c40bd8ff0a](../../evidence/state_effects-sets-004.md#s-0fdf32c40bd8ff0a)

### observed_connections-004731

```text
(config-router-ptmp)# default slow-peer detection <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 74 `；EOL ` RVA 0x345A7158 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8ae2f853249d83dd](../../evidence/conditions-sets-054.md#c-8ae2f853249d83dd) · [状态效果 S-0fdf32c40bd8ff0a](../../evidence/state_effects-sets-004.md#s-0fdf32c40bd8ff0a)

### observed_connections-004784

```text
(config-router-ptmp)# default slow-peer split-update-group dynamic <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 75 `；EOL ` RVA 0x345A6DE0 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-fb60e13036cbb54d](../../evidence/conditions-sets-097.md#c-fb60e13036cbb54d) · [状态效果 S-0fdf32c40bd8ff0a](../../evidence/state_effects-sets-004.md#s-0fdf32c40bd8ff0a)

### observed_connections-004782

```text
(config-router-ptmp)# default slow-peer split-update-group static <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 73 `；EOL ` RVA 0x345A6AD0 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9b1b131ec0b35441](../../evidence/conditions-sets-060.md#c-9b1b131ec0b35441) · [状态效果 S-0fdf32c40bd8ff0a](../../evidence/state_effects-sets-004.md#s-0fdf32c40bd8ff0a)

### observed_connections-004733

```text
(config-router-ptmp)# default soft-reconfiguration inbound <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 54 `；EOL ` RVA 0x345A82C8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8e6bd7ed8050822f](../../evidence/conditions-sets-055.md#c-8e6bd7ed8050822f) · [状态效果 S-0fdf32c40bd8ff0a](../../evidence/state_effects-sets-004.md#s-0fdf32c40bd8ff0a)

### observed_connections-004767

```text
(config-router-ptmp)# default suppress-signaling-protocol ldp <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 81 `；EOL ` RVA 0x345B1ED0 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4803174ef6add6b1](../../evidence/conditions-sets-028.md#c-4803174ef6add6b1) · [状态效果 S-0fdf32c40bd8ff0a](../../evidence/state_effects-sets-004.md#s-0fdf32c40bd8ff0a)

### observed_connections-004702

```text
(config-router-ptmp)# default suppress-sr <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 87 `；EOL ` RVA 0x345B1278 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5017ae8787d3759e](../../evidence/conditions-sets-031.md#c-5017ae8787d3759e) · [状态效果 S-0fdf32c40bd8ff0a](../../evidence/state_effects-sets-004.md#s-0fdf32c40bd8ff0a)

### observed_connections-004685

```text
(config-router-ptmp)# default timers <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 9 `；EOL ` RVA 0x345AD518 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-64fc80d1b9204618](../../evidence/conditions-sets-039.md#c-64fc80d1b9204618) · [状态效果 S-0fdf32c40bd8ff0a](../../evidence/state_effects-sets-004.md#s-0fdf32c40bd8ff0a)

### observed_connections-004715

```text
(config-router-ptmp)# default translate-topology <number:1..4095> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 67 `；EOL ` RVA 0x3459ECB8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Topology id。

[条件 C-f7386af78419fa98](../../evidence/conditions-sets-095.md#c-f7386af78419fa98) · [参数 P-30a41913e146154b](../../evidence/parameters-sets-004.md#p-30a41913e146154b) · [状态效果 S-0fdf32c40bd8ff0a](../../evidence/state_effects-sets-004.md#s-0fdf32c40bd8ff0a)

### observed_connections-004618

```text
(config-router-ptmp)# default translate-update <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 66 `；EOL ` RVA 0x3459FCB8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ace0427610e5d65a](../../evidence/conditions-sets-067.md#c-ace0427610e5d65a) · [状态效果 S-2a834a1a2ea09e73](../../evidence/state_effects-sets-010.md#s-2a834a1a2ea09e73)

### observed_connections-004760

```text
(config-router-ptmp)# default transport multi-session <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 25 `；EOL ` RVA 0x345AF858 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a5f9f132d9176900](../../evidence/conditions-sets-064.md#c-a5f9f132d9176900) · [状态效果 S-2e9ff55c45bc5dda](../../evidence/state_effects-sets-010.md#s-2e9ff55c45bc5dda)

### observed_connections-004758

```text
(config-router-ptmp)# default transport path-mtu-discovery <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 24 `；EOL ` RVA 0x345AF4B0 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a5f9f132d9176900](../../evidence/conditions-sets-064.md#c-a5f9f132d9176900) · [状态效果 S-5584498e9f59dcf0](../../evidence/state_effects-sets-019.md#s-5584498e9f59dcf0)

### observed_connections-004796

```text
(config-router-ptmp)# default ttl-security hops <number:1..254> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 21 `；EOL ` RVA 0x345B01E8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` maximum number of hops。

[条件 C-f0d336a8d254b40b](../../evidence/conditions-sets-093.md#c-f0d336a8d254b40b) · [参数 P-758b48736f7d1a30](../../evidence/parameters-sets-009.md#p-758b48736f7d1a30) · [状态效果 S-0fdf32c40bd8ff0a](../../evidence/state_effects-sets-004.md#s-0fdf32c40bd8ff0a)

### observed_connections-004727

```text
(config-router-ptmp)# default unsuppress-map <string> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 53 `；EOL ` RVA 0x345A2390 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Name of route map。

[条件 C-0e0a9002a8432d6f](../../evidence/conditions-sets-006.md#c-0e0a9002a8432d6f) · [参数 P-8965946866e4fcdf](../../evidence/parameters-sets-011.md#p-8965946866e4fcdf) · [状态效果 S-0fdf32c40bd8ff0a](../../evidence/state_effects-sets-004.md#s-0fdf32c40bd8ff0a)

### observed_connections-004807

```text
(config-router-ptmp)# default update in labeled-unicast unique <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 33 `；EOL ` RVA 0x345B2630 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7cda7f9a73e4e09e](../../evidence/conditions-sets-048.md#c-7cda7f9a73e4e09e) · [状态效果 S-af4663394c83a37e](../../evidence/state_effects-sets-037.md#s-af4663394c83a37e)

### observed_connections-004755

```text
(config-router-ptmp)# default use nexthop-attribute <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 37 `；EOL ` RVA 0x345ADDA0 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ed1f096b95dca6d9](../../evidence/conditions-sets-092.md#c-ed1f096b95dca6d9) · [状态效果 S-0fdf32c40bd8ff0a](../../evidence/state_effects-sets-004.md#s-0fdf32c40bd8ff0a)

### observed_connections-004736

```text
(config-router-ptmp)# default validation off <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 83 `；EOL ` RVA 0x345A8648 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7672f21443040657](../../evidence/conditions-sets-046.md#c-7672f21443040657) · [状态效果 S-0fdf32c40bd8ff0a](../../evidence/state_effects-sets-004.md#s-0fdf32c40bd8ff0a)

### observed_connections-004739

```text
(config-router-ptmp)# default validation redirect-off <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 84 `；EOL ` RVA 0x345A88F0 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7672f21443040657](../../evidence/conditions-sets-046.md#c-7672f21443040657) · [状态效果 S-0fdf32c40bd8ff0a](../../evidence/state_effects-sets-004.md#s-0fdf32c40bd8ff0a)

### observed_connections-004583

```text
(config-router-ptmp)# default version <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 2 `；EOL ` RVA 0x345A4CA0 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-36b667bdc6f1a8e6](../../evidence/conditions-sets-021.md#c-36b667bdc6f1a8e6) · [状态效果 S-0fdf32c40bd8ff0a](../../evidence/state_effects-sets-004.md#s-0fdf32c40bd8ff0a)

### observed_connections-004637

```text
(config-router-ptmp)# default weight <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 41 `；EOL ` RVA 0x345A5098 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9afc061bdb4d36a2](../../evidence/conditions-sets-060.md#c-9afc061bdb4d36a2) · [状态效果 S-0fdf32c40bd8ff0a](../../evidence/state_effects-sets-004.md#s-0fdf32c40bd8ff0a)

### observed_connections-004589

```text
(config-router-ptmp)# default-originate <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 52 `；EOL ` RVA 0x345A7F30 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d73ec397125c786e](../../evidence/conditions-sets-083.md#c-d73ec397125c786e)

### observed_connections-004678

```text
(config-router-ptmp)# description <string> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 8 `；EOL ` RVA 0x345ACE80 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Up to 80 characters describing this neighbor。

[条件 C-01481cd5b19748ba](../../evidence/conditions-sets-001.md#c-01481cd5b19748ba) · [参数 P-5dafc886c4b95dc2](../../evidence/parameters-sets-007.md#p-5dafc886c4b95dc2)

### observed_connections-004579

```text
(config-router-ptmp)# disable-connected-check <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 13 `；EOL ` RVA 0x345A3580 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c0fca8e83773218b](../../evidence/conditions-sets-075.md#c-c0fca8e83773218b) · [状态效果 S-2a8f4cac9f62bb06](../../evidence/state_effects-sets-010.md#s-2a8f4cac9f62bb06)

### observed_connections-004718

```text
(config-router-ptmp)# distribute-list <number:1..199> in <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 45 `；EOL ` RVA 0x345A0708 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` IP access list number。

[条件 C-cf9cd4bf8eae2940](../../evidence/conditions-sets-080.md#c-cf9cd4bf8eae2940) · [参数 P-ef95a01c961a4d37](../../evidence/parameters-sets-018.md#p-ef95a01c961a4d37) · [状态效果 S-3ced0711d5d71c47](../../evidence/state_effects-sets-013.md#s-3ced0711d5d71c47)

### observed_connections-004578

```text
(config-router-ptmp)# dmzlink-bw <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 63 `；EOL ` RVA 0x345A2008 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ef7d296238bbbdef](../../evidence/conditions-sets-092.md#c-ef7d296238bbbdef) · [状态效果 S-bc82b63a97dbc73b](../../evidence/state_effects-sets-040.md#s-bc82b63a97dbc73b)

### observed_connections-004575

```text
(config-router-ptmp)# dont-capability-negotiate <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 16 `；EOL ` RVA 0x3459F2C8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d78a8a3a8ea10084](../../evidence/conditions-sets-083.md#c-d78a8a3a8ea10084)

### observed_connections-004608

```text
(config-router-ptmp)# dont-capability-negotiate enhanced-refresh <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 18 `；EOL ` RVA 0x3459F2A0 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d78a8a3a8ea10084](../../evidence/conditions-sets-083.md#c-d78a8a3a8ea10084)

### observed_connections-004605

```text
(config-router-ptmp)# dont-capability-negotiate four-octets-as <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 17 `；EOL ` RVA 0x3459EFF8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d78a8a3a8ea10084](../../evidence/conditions-sets-083.md#c-d78a8a3a8ea10084)

### observed_connections-004588

```text
(config-router-ptmp)# ebgp-multihop <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 6 `；EOL ` RVA 0x345A7B08 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0eb8c2565a64d50d](../../evidence/conditions-sets-006.md#c-0eb8c2565a64d50d) · [状态效果 S-65b8475f5344d73b](../../evidence/state_effects-sets-022.md#s-65b8475f5344d73b)

### observed_connections-004706

```text
(config-router-ptmp)# encap srv6 <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 86 `；EOL ` RVA 0x345B19D8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cd5e33ea8dcb7cd3](../../evidence/conditions-sets-079.md#c-cd5e33ea8dcb7cd3) · [状态效果 S-91fa1a504adadeb5](../../evidence/state_effects-sets-031.md#s-91fa1a504adadeb5)

### observed_connections-004572

```text
(config-router-ptmp)# exit-peer-policy <cr>
```

Handler ` RVA 0xF140960 `；selector ` 0 `；EOL ` RVA 0x3459E598 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-225e2188293f4225](../../evidence/conditions-sets-013.md#c-225e2188293f4225)

### observed_connections-004582

```text
(config-router-ptmp)# fall-over <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 26 `；EOL ` RVA 0x345A38D8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-beffd627c228829b](../../evidence/conditions-sets-074.md#c-beffd627c228829b) · [状态效果 S-fff5b73715c5a70e](../../evidence/state_effects-sets-054.md#s-fff5b73715c5a70e)

### observed_connections-004721

```text
(config-router-ptmp)# filter-list <number:1..500> in <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 44 `；EOL ` RVA 0x345A14E8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` AS path access list。

[条件 C-b4ba027c7200d029](../../evidence/conditions-sets-070.md#c-b4ba027c7200d029) · [参数 P-38a4ff862bc4d4c2](../../evidence/parameters-sets-005.md#p-38a4ff862bc4d4c2) · [状态效果 S-b9ab703409324b3a](../../evidence/state_effects-sets-039.md#s-b9ab703409324b3a)

### observed_connections-004574

```text
(config-router-ptmp)# force-open-collision <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 15 `；EOL ` RVA 0x3459F858 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-33a8c0691bb825f5](../../evidence/conditions-sets-020.md#c-33a8c0691bb825f5)

### observed_connections-004708

```text
(config-router-ptmp)# ha-mode graceful-restart <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 28 `；EOL ` RVA 0x3459E900 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-901645a8d31c3600](../../evidence/conditions-sets-056.md#c-901645a8d31c3600)

### observed_connections-004710

```text
(config-router-ptmp)# ha-mode sso <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 29 `；EOL ` RVA 0x3372E478 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-901645a8d31c3600](../../evidence/conditions-sets-056.md#c-901645a8d31c3600)

### observed_connections-004746

```text
(config-router-ptmp)# inherit peer-policy <string> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 36 `；EOL ` RVA 0x345ABB10 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Template name。

[条件 C-e6bb9b084507b3f2](../../evidence/conditions-sets-089.md#c-e6bb9b084507b3f2) · [参数 P-c8bcde829a191531](../../evidence/parameters-sets-015.md#p-c8bcde829a191531)

### observed_connections-004743

```text
(config-router-ptmp)# inherit peer-session <string> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 19 `；EOL ` RVA 0x345ABE28 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Template name。

[条件 C-be894983d25dd983](../../evidence/conditions-sets-074.md#c-be894983d25dd983) · [参数 P-13ad4b14a3a89da2](../../evidence/parameters-sets-002.md#p-13ad4b14a3a89da2)

### observed_connections-004591

```text
(config-router-ptmp)# inter-as-hybrid <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 72 `；EOL ` RVA 0x345A94E0 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-988f0292facf8cd9](../../evidence/conditions-sets-059.md#c-988f0292facf8cd9)

### observed_connections-004597

```text
(config-router-ptmp)# internal-vpn-client <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 82 `；EOL ` RVA 0x345AE0E0 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-593b70c1226d4d3d](../../evidence/conditions-sets-035.md#c-593b70c1226d4d3d)

### observed_connections-004808

```text
(config-router-ptmp)# local-as <?bgp_as4_action@555589af7158> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 11 `；EOL ` RVA 0x345A3108 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-cbcb34a4a800be06](../../evidence/conditions-sets-078.md#c-cbcb34a4a800be06) · [缺口 G-108ced964223b8a8](../../evidence/gaps-sets-001.md#g-108ced964223b8a8)

### observed_connections-004631

```text
(config-router-ptmp)# local-as <number:1..4294967295> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 11 `；EOL ` RVA 0x345A3108 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` AS number used as local AS。

[条件 C-736c068f66e351e1](../../evidence/conditions-sets-045.md#c-736c068f66e351e1) · [参数 P-fa5a0dad5c6cd828](../../evidence/parameters-sets-019.md#p-fa5a0dad5c6cd828)

### observed_connections-004604

```text
(config-router-ptmp)# log-neighbor-changes <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 32 `；EOL ` RVA 0x345B2210 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c22607b97d03956e](../../evidence/conditions-sets-075.md#c-c22607b97d03956e)

### observed_connections-004798

```text
(config-router-ptmp)# long-lived-graceful-restart stale-time accept <number:0..4294967> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 85 `；EOL ` RVA 0x345B0DE8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Max time in seconds。

[条件 C-90ea5855d5b260cf](../../evidence/conditions-sets-056.md#c-90ea5855d5b260cf) · [参数 P-8d3e26e4fe2fb31d](../../evidence/parameters-sets-011.md#p-8d3e26e4fe2fb31d) · [状态效果 S-bc133d7bf7cc3089](../../evidence/state_effects-sets-040.md#s-bc133d7bf7cc3089)

### observed_connections-004686

```text
(config-router-ptmp)# maximum-prefix <number:1..2147483647> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 59 `；EOL ` RVA 0x345AC988 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` maximum no. of prefix limit。

[条件 C-68c6b70a6496ebf8](../../evidence/conditions-sets-041.md#c-68c6b70a6496ebf8) · [参数 P-191b055ddb98a361](../../evidence/parameters-sets-002.md#p-191b055ddb98a361)

### observed_connections-004586

```text
(config-router-ptmp)# next-hop-self <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 42 `；EOL ` RVA 0x345A66D8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3cc2906d189aa33d](../../evidence/conditions-sets-024.md#c-3cc2906d189aa33d)

### observed_connections-004587

```text
(config-router-ptmp)# next-hop-unchanged <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 43 `；EOL ` RVA 0x345A7798 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-aa406845aba91741](../../evidence/conditions-sets-066.md#c-aa406845aba91741)

### observed_connections-004599

```text
(config-router-ptmp)# no <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 0 `；EOL ` RVA 0x345AF110 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b9edc2fb9fefc7e0](../../evidence/conditions-sets-072.md#c-b9edc2fb9fefc7e0) · [状态效果 S-96edead9ed6a1a58](../../evidence/state_effects-sets-032.md#s-96edead9ed6a1a58)

### observed_connections-004663

```text
(config-router-ptmp)# no accept-route-legacy-rt <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 71 `；EOL ` RVA 0x345A9F00 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-3b1f652ba27b5bae](../../evidence/conditions-sets-023.md#c-3b1f652ba27b5bae) · [状态效果 S-96edead9ed6a1a58](../../evidence/state_effects-sets-032.md#s-96edead9ed6a1a58)

### observed_connections-004679

```text
(config-router-ptmp)# no activate <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 35 `；EOL ` RVA 0x345AD1B8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-57f098c5222cef48](../../evidence/conditions-sets-034.md#c-57f098c5222cef48) · [状态效果 S-96edead9ed6a1a58](../../evidence/state_effects-sets-032.md#s-96edead9ed6a1a58)

### observed_connections-004670

```text
(config-router-ptmp)# no additional-paths <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 79 `；EOL ` RVA 0x345AA8E0 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ac2542186e9f57ca](../../evidence/conditions-sets-067.md#c-ac2542186e9f57ca) · [状态效果 S-c07c862e4fa5cca0](../../evidence/state_effects-sets-041.md#s-c07c862e4fa5cca0)

### observed_connections-004751

```text
(config-router-ptmp)# no advertise additional-paths <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 78 `；EOL ` RVA 0x345AAFE8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a53b18a12f143564](../../evidence/conditions-sets-064.md#c-a53b18a12f143564) · [状态效果 S-fa6af5cbf18d0f22](../../evidence/state_effects-sets-053.md#s-fa6af5cbf18d0f22)

### observed_connections-004745

```text
(config-router-ptmp)# no advertise best-external <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 80 `；EOL ` RVA 0x345AB698 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-13f51add8edb73c9](../../evidence/conditions-sets-008.md#c-13f51add8edb73c9) · [状态效果 S-96edead9ed6a1a58](../../evidence/state_effects-sets-032.md#s-96edead9ed6a1a58)

### observed_connections-004790

```text
(config-router-ptmp)# no advertise diverse-path mpath <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 78 `；EOL ` RVA 0x345AB3B8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-13f51add8edb73c9](../../evidence/conditions-sets-008.md#c-13f51add8edb73c9) · [状态效果 S-daf03b09b9300a11](../../evidence/state_effects-sets-046.md#s-daf03b09b9300a11)

### observed_connections-004703

```text
(config-router-ptmp)# no advertise-gw-ip-disable <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 88 `；EOL ` RVA 0x345B15B0 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-2d47db81b834ef19](../../evidence/conditions-sets-018.md#c-2d47db81b834ef19) · [状态效果 S-96edead9ed6a1a58](../../evidence/state_effects-sets-032.md#s-96edead9ed6a1a58)

### observed_connections-004800

```text
(config-router-ptmp)# no advertise-map <string> non-exist-map <string> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 39 `；EOL ` RVA 0x345AD9E8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` advertise route-map name；` string ` condition route-map name。

[条件 C-b93d06816a29c292](../../evidence/conditions-sets-072.md#c-b93d06816a29c292) · [参数 P-948a86beed6fd9ec](../../evidence/parameters-sets-011.md#p-948a86beed6fd9ec) · [状态效果 S-c3cabc64b0001164](../../evidence/state_effects-sets-041.md#s-c3cabc64b0001164)

### observed_connections-004639

```text
(config-router-ptmp)# no advertisement-interval <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 40 `；EOL ` RVA 0x345A5470 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d842d517150efc60](../../evidence/conditions-sets-083.md#c-d842d517150efc60) · [状态效果 S-96edead9ed6a1a58](../../evidence/state_effects-sets-032.md#s-96edead9ed6a1a58)

### observed_connections-004666

```text
(config-router-ptmp)# no aigp <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 50 `；EOL ` RVA 0x345A9B00 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-3539c9553c518c8a](../../evidence/conditions-sets-021.md#c-3539c9553c518c8a) · [状态效果 S-fef9abbea9b4fafc](../../evidence/state_effects-sets-054.md#s-fef9abbea9b4fafc)

### observed_connections-004667

```text
(config-router-ptmp)# no allow-policy <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 51 `；EOL ` RVA 0x345AA530 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e8fbca347712cd67](../../evidence/conditions-sets-090.md#c-e8fbca347712cd67) · [状态效果 S-96edead9ed6a1a58](../../evidence/state_effects-sets-032.md#s-96edead9ed6a1a58)

### observed_connections-004629

```text
(config-router-ptmp)# no allowas-in <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 60 `；EOL ` RVA 0x345A4210 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-bc7652112c908451](../../evidence/conditions-sets-073.md#c-bc7652112c908451) · [状态效果 S-96edead9ed6a1a58](../../evidence/state_effects-sets-032.md#s-96edead9ed6a1a58)

### observed_connections-004779

```text
(config-router-ptmp)# no announce rpki state <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 77 `；EOL ` RVA 0x345A49F8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-47496888dc91b329](../../evidence/conditions-sets-028.md#c-47496888dc91b329) · [状态效果 S-96edead9ed6a1a58](../../evidence/state_effects-sets-032.md#s-96edead9ed6a1a58)

### observed_connections-004761

```text
(config-router-ptmp)# no ao <string> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 22 `；EOL ` RVA 0x345B0600 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Keychain name。

[条件 C-2173407f5d5c0a2a](../../evidence/conditions-sets-013.md#c-2173407f5d5c0a2a) · [参数 P-5b8d7ea6b5cf663a](../../evidence/parameters-sets-007.md#p-5b8d7ea6b5cf663a) · [状态效果 S-96edead9ed6a1a58](../../evidence/state_effects-sets-032.md#s-96edead9ed6a1a58)

### observed_connections-004690

```text
(config-router-ptmp)# no as-override <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 61 `；EOL ` RVA 0x345AE498 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f721f6e9763e5885](../../evidence/conditions-sets-095.md#c-f721f6e9763e5885) · [状态效果 S-96edead9ed6a1a58](../../evidence/state_effects-sets-032.md#s-96edead9ed6a1a58)

### observed_connections-004802

```text
(config-router-ptmp)# no capability orf prefix-list send <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 65 `；EOL ` RVA 0x345AE8E0 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-78ad2cac013dfb1b](../../evidence/conditions-sets-047.md#c-78ad2cac013dfb1b) · [状态效果 S-b9819489b23f2925](../../evidence/state_effects-sets-039.md#s-b9819489b23f2925)

### observed_connections-004696

```text
(config-router-ptmp)# no cluster-id <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 23 `；EOL ` RVA 0x345B09C8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-45c010911bbb3250](../../evidence/conditions-sets-027.md#c-45c010911bbb3250) · [状态效果 S-96edead9ed6a1a58](../../evidence/state_effects-sets-032.md#s-96edead9ed6a1a58)

### observed_connections-004649

```text
(config-router-ptmp)# no default-originate <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 52 `；EOL ` RVA 0x345A7F30 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d73ec397125c786e](../../evidence/conditions-sets-083.md#c-d73ec397125c786e) · [状态效果 S-96edead9ed6a1a58](../../evidence/state_effects-sets-032.md#s-96edead9ed6a1a58)

### observed_connections-004676

```text
(config-router-ptmp)# no description <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 8 `；EOL ` RVA 0x345ACE80 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-80529fe87b1e031e](../../evidence/conditions-sets-050.md#c-80529fe87b1e031e) · [状态效果 S-96edead9ed6a1a58](../../evidence/state_effects-sets-032.md#s-96edead9ed6a1a58)

### observed_connections-004624

```text
(config-router-ptmp)# no disable-connected-check <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 13 `；EOL ` RVA 0x345A3580 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c0fca8e83773218b](../../evidence/conditions-sets-075.md#c-c0fca8e83773218b) · [状态效果 S-7fa9de5d64324f23](../../evidence/state_effects-sets-027.md#s-7fa9de5d64324f23)

### observed_connections-004771

```text
(config-router-ptmp)# no distribute-list <number:1..199> in <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 45 `；EOL ` RVA 0x345A0708 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` IP access list number。

[条件 C-cf9cd4bf8eae2940](../../evidence/conditions-sets-080.md#c-cf9cd4bf8eae2940) · [参数 P-ef95a01c961a4d37](../../evidence/parameters-sets-018.md#p-ef95a01c961a4d37) · [状态效果 S-3fbfe0ae68a2c1d3](../../evidence/state_effects-sets-014.md#s-3fbfe0ae68a2c1d3)

### observed_connections-004620

```text
(config-router-ptmp)# no dmzlink-bw <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 63 `；EOL ` RVA 0x345A2008 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ef7d296238bbbdef](../../evidence/conditions-sets-092.md#c-ef7d296238bbbdef) · [状态效果 S-f658a8d5c187ab6a](../../evidence/state_effects-sets-052.md#s-f658a8d5c187ab6a)

### observed_connections-004611

```text
(config-router-ptmp)# no dont-capability-negotiate <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 16 `；EOL ` RVA 0x3459F2C8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d78a8a3a8ea10084](../../evidence/conditions-sets-083.md#c-d78a8a3a8ea10084) · [状态效果 S-96edead9ed6a1a58](../../evidence/state_effects-sets-032.md#s-96edead9ed6a1a58)

### observed_connections-004716

```text
(config-router-ptmp)# no dont-capability-negotiate enhanced-refresh <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 18 `；EOL ` RVA 0x3459F2A0 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d78a8a3a8ea10084](../../evidence/conditions-sets-083.md#c-d78a8a3a8ea10084) · [状态效果 S-96edead9ed6a1a58](../../evidence/state_effects-sets-032.md#s-96edead9ed6a1a58)

### observed_connections-004712

```text
(config-router-ptmp)# no dont-capability-negotiate four-octets-as <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 17 `；EOL ` RVA 0x3459EFF8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d78a8a3a8ea10084](../../evidence/conditions-sets-083.md#c-d78a8a3a8ea10084) · [状态效果 S-96edead9ed6a1a58](../../evidence/state_effects-sets-032.md#s-96edead9ed6a1a58)

### observed_connections-004648

```text
(config-router-ptmp)# no ebgp-multihop <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 6 `；EOL ` RVA 0x345A7B08 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0eb8c2565a64d50d](../../evidence/conditions-sets-006.md#c-0eb8c2565a64d50d) · [状态效果 S-a476902470ef20cd](../../evidence/state_effects-sets-035.md#s-a476902470ef20cd)

### observed_connections-004763

```text
(config-router-ptmp)# no encap srv6 <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 86 `；EOL ` RVA 0x345B19D8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-cd5e33ea8dcb7cd3](../../evidence/conditions-sets-079.md#c-cd5e33ea8dcb7cd3) · [状态效果 S-de39ddf5214a2378](../../evidence/state_effects-sets-047.md#s-de39ddf5214a2378)

### observed_connections-004632

```text
(config-router-ptmp)# no fall-over <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 26 `；EOL ` RVA 0x345A38D8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-beffd627c228829b](../../evidence/conditions-sets-074.md#c-beffd627c228829b) · [状态效果 S-97a2cac4f7542d92](../../evidence/state_effects-sets-032.md#s-97a2cac4f7542d92)

### observed_connections-004776

```text
(config-router-ptmp)# no filter-list <number:1..500> in <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 44 `；EOL ` RVA 0x345A14E8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` AS path access list。

[条件 C-b4ba027c7200d029](../../evidence/conditions-sets-070.md#c-b4ba027c7200d029) · [参数 P-38a4ff862bc4d4c2](../../evidence/parameters-sets-005.md#p-38a4ff862bc4d4c2) · [状态效果 S-74b60d7dbaddec28](../../evidence/state_effects-sets-025.md#s-74b60d7dbaddec28)

### observed_connections-004610

```text
(config-router-ptmp)# no force-open-collision <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 15 `；EOL ` RVA 0x3459F858 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-33a8c0691bb825f5](../../evidence/conditions-sets-020.md#c-33a8c0691bb825f5) · [状态效果 S-96edead9ed6a1a58](../../evidence/state_effects-sets-032.md#s-96edead9ed6a1a58)

### observed_connections-004766

```text
(config-router-ptmp)# no ha-mode graceful-restart <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 28 `；EOL ` RVA 0x3459E900 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-901645a8d31c3600](../../evidence/conditions-sets-056.md#c-901645a8d31c3600) · [状态效果 S-96edead9ed6a1a58](../../evidence/state_effects-sets-032.md#s-96edead9ed6a1a58)

### observed_connections-004769

```text
(config-router-ptmp)# no ha-mode sso <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 29 `；EOL ` RVA 0x3372E478 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-901645a8d31c3600](../../evidence/conditions-sets-056.md#c-901645a8d31c3600) · [状态效果 S-96edead9ed6a1a58](../../evidence/state_effects-sets-032.md#s-96edead9ed6a1a58)

### observed_connections-004788

```text
(config-router-ptmp)# no inherit peer-policy <string> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 36 `；EOL ` RVA 0x345ABB10 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Template name。

[条件 C-e6bb9b084507b3f2](../../evidence/conditions-sets-089.md#c-e6bb9b084507b3f2) · [参数 P-c8bcde829a191531](../../evidence/parameters-sets-015.md#p-c8bcde829a191531) · [状态效果 S-96edead9ed6a1a58](../../evidence/state_effects-sets-032.md#s-96edead9ed6a1a58)

### observed_connections-004787

```text
(config-router-ptmp)# no inherit peer-session <string> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 19 `；EOL ` RVA 0x345ABE28 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Template name。

[条件 C-be894983d25dd983](../../evidence/conditions-sets-074.md#c-be894983d25dd983) · [参数 P-13ad4b14a3a89da2](../../evidence/parameters-sets-002.md#p-13ad4b14a3a89da2) · [状态效果 S-96edead9ed6a1a58](../../evidence/state_effects-sets-032.md#s-96edead9ed6a1a58)

### observed_connections-004658

```text
(config-router-ptmp)# no inter-as-hybrid <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 72 `；EOL ` RVA 0x345A94E0 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-988f0292facf8cd9](../../evidence/conditions-sets-059.md#c-988f0292facf8cd9) · [状态效果 S-96edead9ed6a1a58](../../evidence/state_effects-sets-032.md#s-96edead9ed6a1a58)

### observed_connections-004688

```text
(config-router-ptmp)# no internal-vpn-client <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 82 `；EOL ` RVA 0x345AE0E0 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-593b70c1226d4d3d](../../evidence/conditions-sets-035.md#c-593b70c1226d4d3d) · [状态效果 S-96edead9ed6a1a58](../../evidence/state_effects-sets-032.md#s-96edead9ed6a1a58)

### observed_connections-004626

```text
(config-router-ptmp)# no local-as <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 11 `；EOL ` RVA 0x345A3108 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f324df8bd6556efc](../../evidence/conditions-sets-094.md#c-f324df8bd6556efc) · [状态效果 S-96edead9ed6a1a58](../../evidence/state_effects-sets-032.md#s-96edead9ed6a1a58)

### observed_connections-004709

```text
(config-router-ptmp)# no log-neighbor-changes <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 32 `；EOL ` RVA 0x345B2210 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c22607b97d03956e](../../evidence/conditions-sets-075.md#c-c22607b97d03956e) · [状态效果 S-96edead9ed6a1a58](../../evidence/state_effects-sets-032.md#s-96edead9ed6a1a58)

### observed_connections-004700

```text
(config-router-ptmp)# no long-lived-graceful-restart <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 85 `；EOL ` RVA 0x345B0DE8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-9ae129c4fbd347be](../../evidence/conditions-sets-060.md#c-9ae129c4fbd347be) · [状态效果 S-96edead9ed6a1a58](../../evidence/state_effects-sets-032.md#s-96edead9ed6a1a58)

### observed_connections-004749

```text
(config-router-ptmp)# no maximum-prefix <number:1..2147483647> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 59 `；EOL ` RVA 0x345AC988 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` maximum no. of prefix limit。

[条件 C-1e7efb2bd446ff6a](../../evidence/conditions-sets-012.md#c-1e7efb2bd446ff6a) · [参数 P-191b055ddb98a361](../../evidence/parameters-sets-002.md#p-191b055ddb98a361) · [状态效果 S-96edead9ed6a1a58](../../evidence/state_effects-sets-032.md#s-96edead9ed6a1a58)

### observed_connections-004644

```text
(config-router-ptmp)# no next-hop-self <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 42 `；EOL ` RVA 0x345A66D8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-3cc2906d189aa33d](../../evidence/conditions-sets-024.md#c-3cc2906d189aa33d) · [状态效果 S-96edead9ed6a1a58](../../evidence/state_effects-sets-032.md#s-96edead9ed6a1a58)

### observed_connections-004646

```text
(config-router-ptmp)# no next-hop-unchanged <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 43 `；EOL ` RVA 0x345A7798 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-aa406845aba91741](../../evidence/conditions-sets-066.md#c-aa406845aba91741) · [状态效果 S-96edead9ed6a1a58](../../evidence/state_effects-sets-032.md#s-96edead9ed6a1a58)

### observed_connections-004722

```text
(config-router-ptmp)# no orf rt-import-list <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 70 `；EOL ` RVA 0x345A10C8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-418cd2855f0401bd](../../evidence/conditions-sets-026.md#c-418cd2855f0401bd) · [状态效果 S-81bf4818205bb857](../../evidence/state_effects-sets-028.md#s-81bf4818205bb857)

### observed_connections-004614

```text
(config-router-ptmp)# no override-capability-neg <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 62 `；EOL ` RVA 0x345A0320 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b817ba1ecc562077](../../evidence/conditions-sets-071.md#c-b817ba1ecc562077) · [状态效果 S-96edead9ed6a1a58](../../evidence/state_effects-sets-032.md#s-96edead9ed6a1a58)

### observed_connections-004675

```text
(config-router-ptmp)# no password <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 7 `；EOL ` RVA 0x345AC540 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a9e1a619fb347e2a](../../evidence/conditions-sets-066.md#c-a9e1a619fb347e2a) · [状态效果 S-96edead9ed6a1a58](../../evidence/state_effects-sets-032.md#s-96edead9ed6a1a58)

### observed_connections-004804

```text
(config-router-ptmp)# no path-attribute treat-as-withdraw <number:1..255> in <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 27 `；EOL ` RVA 0x345AFDE0 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` path attribute type。

[条件 C-cd5e6fbd0bb23f22](../../evidence/conditions-sets-079.md#c-cd5e6fbd0bb23f22) · [参数 P-ce24450e99a47fbc](../../evidence/parameters-sets-016.md#p-ce24450e99a47fbc) · [状态效果 S-97149c1cb40bf8b2](../../evidence/state_effects-sets-032.md#s-97149c1cb40bf8b2)

### observed_connections-004607

```text
(config-router-ptmp)# no peer-group <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 10 `；EOL ` RVA 0x345B3398 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-cc5eca777bce2284](../../evidence/conditions-sets-079.md#c-cc5eca777bce2284) · [状态效果 S-96edead9ed6a1a58](../../evidence/state_effects-sets-032.md#s-96edead9ed6a1a58)

### observed_connections-004742

```text
(config-router-ptmp)# no peer-group <string> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 20 `；EOL ` RVA 0x345AC1A8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` peer-group name。

[条件 C-16f9dfd652106e63](../../evidence/conditions-sets-009.md#c-16f9dfd652106e63) · [参数 P-b044166d77593cf1](../../evidence/parameters-sets-013.md#p-b044166d77593cf1) · [状态效果 S-96edead9ed6a1a58](../../evidence/state_effects-sets-032.md#s-96edead9ed6a1a58)

### observed_connections-004723

```text
(config-router-ptmp)# no prefix-length-size <number:1..2> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 68 `；EOL ` RVA 0x345A1CC8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Storage size in bytes。

[条件 C-b40ff8c03848d66e](../../evidence/conditions-sets-070.md#c-b40ff8c03848d66e) · [参数 P-28a5ce03beeb709e](../../evidence/parameters-sets-004.md#p-28a5ce03beeb709e) · [状态效果 S-96edead9ed6a1a58](../../evidence/state_effects-sets-032.md#s-96edead9ed6a1a58)

### observed_connections-004773

```text
(config-router-ptmp)# no prefix-list <string> in <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 58 `；EOL ` RVA 0x345A0BF0 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Name of a prefix list。

[条件 C-68bc7d14c06ce41b](../../evidence/conditions-sets-041.md#c-68bc7d14c06ce41b) · [参数 P-3ba5cb7712b4d450](../../evidence/parameters-sets-005.md#p-3ba5cb7712b4d450) · [状态效果 S-341bd7949ff94ccf](../../evidence/state_effects-sets-012.md#s-341bd7949ff94ccf)

### observed_connections-004623

```text
(config-router-ptmp)# no remote-as <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 3 `；EOL ` RVA 0x345A26F0 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-fa5cefa33f31c306](../../evidence/conditions-sets-097.md#c-fa5cefa33f31c306) · [状态效果 S-96edead9ed6a1a58](../../evidence/state_effects-sets-032.md#s-96edead9ed6a1a58)

### observed_connections-004656

```text
(config-router-ptmp)# no remove-private-as <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 55 `；EOL ` RVA 0x345A8CA8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d51cc31133008bdd](../../evidence/conditions-sets-082.md#c-d51cc31133008bdd) · [状态效果 S-96edead9ed6a1a58](../../evidence/state_effects-sets-032.md#s-96edead9ed6a1a58)

### observed_connections-004740

```text
(config-router-ptmp)# no remove-private-as all <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 56 `；EOL ` RVA 0x345A8D10 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-331da96fb8c28112](../../evidence/conditions-sets-020.md#c-331da96fb8c28112) · [状态效果 S-96edead9ed6a1a58](../../evidence/state_effects-sets-032.md#s-96edead9ed6a1a58)

### observed_connections-004785

```text
(config-router-ptmp)# no remove-private-as all replace-as <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 57 `；EOL ` RVA 0x345A8CE8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-331da96fb8c28112](../../evidence/conditions-sets-020.md#c-331da96fb8c28112) · [状态效果 S-96edead9ed6a1a58](../../evidence/state_effects-sets-032.md#s-96edead9ed6a1a58)

### observed_connections-004775

```text
(config-router-ptmp)# no route-map <string> in <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 47 `；EOL ` RVA 0x345A18D8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Name of route map。

[条件 C-8b870d549f7da0b5](../../evidence/conditions-sets-054.md#c-8b870d549f7da0b5) · [参数 P-ceca94b6cb65eb98](../../evidence/parameters-sets-016.md#p-ceca94b6cb65eb98) · [状态效果 S-130cd5c4df0828e9](../../evidence/state_effects-sets-004.md#s-130cd5c4df0828e9)

### observed_connections-004662

```text
(config-router-ptmp)# no route-reflector-client <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 49 `；EOL ` RVA 0x345AA1F8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-619f85b0cdd0e481](../../evidence/conditions-sets-038.md#c-619f85b0cdd0e481) · [状态效果 S-96edead9ed6a1a58](../../evidence/state_effects-sets-032.md#s-96edead9ed6a1a58)

### observed_connections-004638

```text
(config-router-ptmp)# no send-community <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 46 `；EOL ` RVA 0x345A5C08 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-83f40b955213680f](../../evidence/conditions-sets-051.md#c-83f40b955213680f) · [状态效果 S-96edead9ed6a1a58](../../evidence/state_effects-sets-032.md#s-96edead9ed6a1a58)

### observed_connections-004692

```text
(config-router-ptmp)# no send-label <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 64 `；EOL ` RVA 0x345AEDE0 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-91b95d4fc7519899](../../evidence/conditions-sets-056.md#c-91b95d4fc7519899) · [状态效果 S-96edead9ed6a1a58](../../evidence/state_effects-sets-032.md#s-96edead9ed6a1a58)

### observed_connections-004641

```text
(config-router-ptmp)# no shutdown <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 5 `；EOL ` RVA 0x345A60A8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7e0f15475668cba2](../../evidence/conditions-sets-049.md#c-7e0f15475668cba2) · [状态效果 S-96edead9ed6a1a58](../../evidence/state_effects-sets-032.md#s-96edead9ed6a1a58)

### observed_connections-004730

```text
(config-router-ptmp)# no slow-peer detection <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 74 `；EOL ` RVA 0x345A7158 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-98c82ac1fea72e90](../../evidence/conditions-sets-059.md#c-98c82ac1fea72e90) · [状态效果 S-96edead9ed6a1a58](../../evidence/state_effects-sets-032.md#s-96edead9ed6a1a58)

### observed_connections-004783

```text
(config-router-ptmp)# no slow-peer split-update-group dynamic <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 75 `；EOL ` RVA 0x345A6DE0 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b034c65cc7a95ca3](../../evidence/conditions-sets-068.md#c-b034c65cc7a95ca3) · [状态效果 S-96edead9ed6a1a58](../../evidence/state_effects-sets-032.md#s-96edead9ed6a1a58)

### observed_connections-004781

```text
(config-router-ptmp)# no slow-peer split-update-group static <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 73 `；EOL ` RVA 0x345A6AD0 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-9b1b131ec0b35441](../../evidence/conditions-sets-060.md#c-9b1b131ec0b35441) · [状态效果 S-96edead9ed6a1a58](../../evidence/state_effects-sets-032.md#s-96edead9ed6a1a58)

### observed_connections-004732

```text
(config-router-ptmp)# no soft-reconfiguration inbound <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 54 `；EOL ` RVA 0x345A82C8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8e6bd7ed8050822f](../../evidence/conditions-sets-055.md#c-8e6bd7ed8050822f) · [状态效果 S-96edead9ed6a1a58](../../evidence/state_effects-sets-032.md#s-96edead9ed6a1a58)

### observed_connections-004764

```text
(config-router-ptmp)# no suppress-signaling-protocol ldp <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 81 `；EOL ` RVA 0x345B1ED0 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4803174ef6add6b1](../../evidence/conditions-sets-028.md#c-4803174ef6add6b1) · [状态效果 S-96edead9ed6a1a58](../../evidence/state_effects-sets-032.md#s-96edead9ed6a1a58)

### observed_connections-004698

```text
(config-router-ptmp)# no suppress-sr <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 87 `；EOL ` RVA 0x345B1278 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5017ae8787d3759e](../../evidence/conditions-sets-031.md#c-5017ae8787d3759e) · [状态效果 S-96edead9ed6a1a58](../../evidence/state_effects-sets-032.md#s-96edead9ed6a1a58)

### observed_connections-004683

```text
(config-router-ptmp)# no timers <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 9 `；EOL ` RVA 0x345AD518 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-04a7c737dc63f8dc](../../evidence/conditions-sets-002.md#c-04a7c737dc63f8dc) · [状态效果 S-96edead9ed6a1a58](../../evidence/state_effects-sets-032.md#s-96edead9ed6a1a58)

### observed_connections-004713

```text
(config-router-ptmp)# no translate-topology <number:1..4095> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 67 `；EOL ` RVA 0x3459ECB8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Topology id。

[条件 C-f7386af78419fa98](../../evidence/conditions-sets-095.md#c-f7386af78419fa98) · [参数 P-30a41913e146154b](../../evidence/parameters-sets-004.md#p-30a41913e146154b) · [状态效果 S-96edead9ed6a1a58](../../evidence/state_effects-sets-032.md#s-96edead9ed6a1a58)

### observed_connections-004616

```text
(config-router-ptmp)# no translate-update <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 66 `；EOL ` RVA 0x3459FCB8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ace0427610e5d65a](../../evidence/conditions-sets-067.md#c-ace0427610e5d65a) · [状态效果 S-ea333f3c688a0642](../../evidence/state_effects-sets-050.md#s-ea333f3c688a0642)

### observed_connections-004757

```text
(config-router-ptmp)# no transport multi-session <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 25 `；EOL ` RVA 0x345AF858 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a5f9f132d9176900](../../evidence/conditions-sets-064.md#c-a5f9f132d9176900) · [状态效果 S-05adb40d3255b259](../../evidence/state_effects-sets-002.md#s-05adb40d3255b259)

### observed_connections-004756

```text
(config-router-ptmp)# no transport path-mtu-discovery <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 24 `；EOL ` RVA 0x345AF4B0 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a5f9f132d9176900](../../evidence/conditions-sets-064.md#c-a5f9f132d9176900) · [状态效果 S-0d00f3056c9b6e98](../../evidence/state_effects-sets-003.md#s-0d00f3056c9b6e98)

### observed_connections-004795

```text
(config-router-ptmp)# no ttl-security hops <number:1..254> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 21 `；EOL ` RVA 0x345B01E8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` maximum number of hops。

[条件 C-f0d336a8d254b40b](../../evidence/conditions-sets-093.md#c-f0d336a8d254b40b) · [参数 P-758b48736f7d1a30](../../evidence/parameters-sets-009.md#p-758b48736f7d1a30) · [状态效果 S-96edead9ed6a1a58](../../evidence/state_effects-sets-032.md#s-96edead9ed6a1a58)

### observed_connections-004726

```text
(config-router-ptmp)# no unsuppress-map <string> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 53 `；EOL ` RVA 0x345A2390 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Name of route map。

[条件 C-0e0a9002a8432d6f](../../evidence/conditions-sets-006.md#c-0e0a9002a8432d6f) · [参数 P-8965946866e4fcdf](../../evidence/parameters-sets-011.md#p-8965946866e4fcdf) · [状态效果 S-96edead9ed6a1a58](../../evidence/state_effects-sets-032.md#s-96edead9ed6a1a58)

### observed_connections-004806

```text
(config-router-ptmp)# no update in labeled-unicast unique <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 33 `；EOL ` RVA 0x345B2630 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7cda7f9a73e4e09e](../../evidence/conditions-sets-048.md#c-7cda7f9a73e4e09e) · [状态效果 S-2fa20bfcd8906f90](../../evidence/state_effects-sets-011.md#s-2fa20bfcd8906f90)

### observed_connections-004753

```text
(config-router-ptmp)# no use nexthop-attribute <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 37 `；EOL ` RVA 0x345ADDA0 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ed1f096b95dca6d9](../../evidence/conditions-sets-092.md#c-ed1f096b95dca6d9) · [状态效果 S-96edead9ed6a1a58](../../evidence/state_effects-sets-032.md#s-96edead9ed6a1a58)

### observed_connections-004734

```text
(config-router-ptmp)# no validation off <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 83 `；EOL ` RVA 0x345A8648 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7672f21443040657](../../evidence/conditions-sets-046.md#c-7672f21443040657) · [状态效果 S-96edead9ed6a1a58](../../evidence/state_effects-sets-032.md#s-96edead9ed6a1a58)

### observed_connections-004737

```text
(config-router-ptmp)# no validation redirect-off <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 84 `；EOL ` RVA 0x345A88F0 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7672f21443040657](../../evidence/conditions-sets-046.md#c-7672f21443040657) · [状态效果 S-96edead9ed6a1a58](../../evidence/state_effects-sets-032.md#s-96edead9ed6a1a58)

### observed_connections-004580

```text
(config-router-ptmp)# no version <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 2 `；EOL ` RVA 0x345A4CA0 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-36b667bdc6f1a8e6](../../evidence/conditions-sets-021.md#c-36b667bdc6f1a8e6) · [状态效果 S-96edead9ed6a1a58](../../evidence/state_effects-sets-032.md#s-96edead9ed6a1a58)

### observed_connections-004634

```text
(config-router-ptmp)# no weight <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 41 `；EOL ` RVA 0x345A5098 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ff85a9b5860eb006](../../evidence/conditions-sets-098.md#c-ff85a9b5860eb006) · [状态效果 S-96edead9ed6a1a58](../../evidence/state_effects-sets-032.md#s-96edead9ed6a1a58)

### observed_connections-004617

```text
(config-router-ptmp)# orf rt-import-list <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 70 `；EOL ` RVA 0x345A10C8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-418cd2855f0401bd](../../evidence/conditions-sets-026.md#c-418cd2855f0401bd) · [状态效果 S-73145b420d816f96](../../evidence/state_effects-sets-024.md#s-73145b420d816f96)

### observed_connections-004576

```text
(config-router-ptmp)# override-capability-neg <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 62 `；EOL ` RVA 0x345A0320 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b817ba1ecc562077](../../evidence/conditions-sets-071.md#c-b817ba1ecc562077)

### observed_connections-004681

```text
(config-router-ptmp)# password <string> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 7 `；EOL ` RVA 0x345AC540 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` The password。

[条件 C-9595248599f849b8](../../evidence/conditions-sets-058.md#c-9595248599f849b8) · [参数 P-a7c781b2f5f62e87](../../evidence/parameters-sets-013.md#p-a7c781b2f5f62e87)

### observed_connections-004797

```text
(config-router-ptmp)# path-attribute treat-as-withdraw <number:1..255> in <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 27 `；EOL ` RVA 0x345AFDE0 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` path attribute type。

[条件 C-cd5e6fbd0bb23f22](../../evidence/conditions-sets-079.md#c-cd5e6fbd0bb23f22) · [参数 P-ce24450e99a47fbc](../../evidence/parameters-sets-016.md#p-ce24450e99a47fbc) · [状态效果 S-53082e6384563dba](../../evidence/state_effects-sets-018.md#s-53082e6384563dba)

### observed_connections-004573

```text
(config-router-ptmp)# peer-group <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 10 `；EOL ` RVA 0x345B3398 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cc5eca777bce2284](../../evidence/conditions-sets-079.md#c-cc5eca777bce2284)

### observed_connections-004673

```text
(config-router-ptmp)# peer-group <string> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 20 `；EOL ` RVA 0x345AC1A8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` peer-group name。

[条件 C-16f9dfd652106e63](../../evidence/conditions-sets-009.md#c-16f9dfd652106e63) · [参数 P-b044166d77593cf1](../../evidence/parameters-sets-013.md#p-b044166d77593cf1)

### observed_connections-004619

```text
(config-router-ptmp)# prefix-length-size <number:1..2> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 68 `；EOL ` RVA 0x345A1CC8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Storage size in bytes。

[条件 C-b40ff8c03848d66e](../../evidence/conditions-sets-070.md#c-b40ff8c03848d66e) · [参数 P-28a5ce03beeb709e](../../evidence/parameters-sets-004.md#p-28a5ce03beeb709e)

### observed_connections-004719

```text
(config-router-ptmp)# prefix-list <string> in <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 58 `；EOL ` RVA 0x345A0BF0 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of a prefix list。

[条件 C-68bc7d14c06ce41b](../../evidence/conditions-sets-041.md#c-68bc7d14c06ce41b) · [参数 P-3ba5cb7712b4d450](../../evidence/parameters-sets-005.md#p-3ba5cb7712b4d450) · [状态效果 S-2df678a344067b07](../../evidence/state_effects-sets-010.md#s-2df678a344067b07)

### observed_connections-004809

```text
(config-router-ptmp)# remote-as <?bgp_as4_action@555589af66c8> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 3 `；EOL ` RVA 0x345A26F0 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e8dbf57ffaa2204f](../../evidence/conditions-sets-090.md#c-e8dbf57ffaa2204f) · [缺口 G-b12180a7b603c3b2](../../evidence/gaps-sets-006.md#g-b12180a7b603c3b2)

### observed_connections-004590

```text
(config-router-ptmp)# remove-private-as <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 55 `；EOL ` RVA 0x345A8CA8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d51cc31133008bdd](../../evidence/conditions-sets-082.md#c-d51cc31133008bdd)

### observed_connections-004661

```text
(config-router-ptmp)# remove-private-as all <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 56 `；EOL ` RVA 0x345A8D10 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-331da96fb8c28112](../../evidence/conditions-sets-020.md#c-331da96fb8c28112)

### observed_connections-004738

```text
(config-router-ptmp)# remove-private-as all replace-as <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 57 `；EOL ` RVA 0x345A8CE8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-331da96fb8c28112](../../evidence/conditions-sets-020.md#c-331da96fb8c28112)

### observed_connections-004720

```text
(config-router-ptmp)# route-map <string> in <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 47 `；EOL ` RVA 0x345A18D8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of route map。

[条件 C-8b870d549f7da0b5](../../evidence/conditions-sets-054.md#c-8b870d549f7da0b5) · [参数 P-ceca94b6cb65eb98](../../evidence/parameters-sets-016.md#p-ceca94b6cb65eb98) · [状态效果 S-bb2b5d4f061dc6b2](../../evidence/state_effects-sets-040.md#s-bb2b5d4f061dc6b2)

### observed_connections-004592

```text
(config-router-ptmp)# route-reflector-client <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 49 `；EOL ` RVA 0x345AA1F8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-619f85b0cdd0e481](../../evidence/conditions-sets-038.md#c-619f85b0cdd0e481)

### observed_connections-004584

```text
(config-router-ptmp)# send-community <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 46 `；EOL ` RVA 0x345A5C08 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-83f40b955213680f](../../evidence/conditions-sets-051.md#c-83f40b955213680f)

### observed_connections-004600

```text
(config-router-ptmp)# send-label <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 64 `；EOL ` RVA 0x345AEDE0 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-91b95d4fc7519899](../../evidence/conditions-sets-056.md#c-91b95d4fc7519899)

### observed_connections-004585

```text
(config-router-ptmp)# shutdown <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 5 `；EOL ` RVA 0x345A60A8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7e0f15475668cba2](../../evidence/conditions-sets-049.md#c-7e0f15475668cba2)

### observed_connections-004812

```text
(config-router-ptmp)# shutdown graceful <number:30..65535> community <?bgp_community_action@555589afa2f0> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 5 `；EOL ` RVA 0x345A60A8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` time in seconds。

[条件 C-06f90d55037b9556](../../evidence/conditions-sets-003.md#c-06f90d55037b9556) · [缺口 G-5522ad4020c154e2](../../evidence/gaps-sets-003.md#g-5522ad4020c154e2) · [参数 P-5f3dcbe0197cd0fa](../../evidence/parameters-sets-008.md#p-5f3dcbe0197cd0fa) · [状态效果 S-f5bb31fb2e706fb2](../../evidence/state_effects-sets-052.md#s-f5bb31fb2e706fb2)

### observed_connections-004654

```text
(config-router-ptmp)# slow-peer detection <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 74 `；EOL ` RVA 0x345A7158 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-479c3cb68f261c36](../../evidence/conditions-sets-028.md#c-479c3cb68f261c36)

### observed_connections-004650

```text
(config-router-ptmp)# slow-peer detection threshold <number:120..3600> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 74 `；EOL ` RVA 0x345A7180 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Threshold value (seconds)。

[条件 C-ecdb836a8721f1eb](../../evidence/conditions-sets-092.md#c-ecdb836a8721f1eb) · [参数 P-b7da68f577065233](../../evidence/parameters-sets-014.md#p-b7da68f577065233)

### observed_connections-004735

```text
(config-router-ptmp)# slow-peer split-update-group dynamic <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 75 `；EOL ` RVA 0x345A6DE0 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9221110fa4443875](../../evidence/conditions-sets-056.md#c-9221110fa4443875)

### observed_connections-004729

```text
(config-router-ptmp)# slow-peer split-update-group static <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 73 `；EOL ` RVA 0x345A6AD0 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9b1b131ec0b35441](../../evidence/conditions-sets-060.md#c-9b1b131ec0b35441)

### observed_connections-004652

```text
(config-router-ptmp)# soft-reconfiguration inbound <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 54 `；EOL ` RVA 0x345A82C8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8e6bd7ed8050822f](../../evidence/conditions-sets-055.md#c-8e6bd7ed8050822f)

### observed_connections-004810

```text
(config-router-ptmp)# soo <?bgp_extcomm_action@555589af8588> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 69 `；EOL ` RVA 0x345A45D0 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-315763bcc27f71fc](../../evidence/conditions-sets-019.md#c-315763bcc27f71fc) · [缺口 G-02c5c7cea60bc0d6](../../evidence/gaps-sets-001.md#g-02c5c7cea60bc0d6) · [状态效果 S-4711c96c8f89d734](../../evidence/state_effects-sets-016.md#s-4711c96c8f89d734)

### observed_connections-004707

```text
(config-router-ptmp)# suppress-signaling-protocol ldp <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 81 `；EOL ` RVA 0x345B1ED0 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4803174ef6add6b1](../../evidence/conditions-sets-028.md#c-4803174ef6add6b1)

### observed_connections-004602

```text
(config-router-ptmp)# suppress-sr <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 87 `；EOL ` RVA 0x345B1278 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5017ae8787d3759e](../../evidence/conditions-sets-031.md#c-5017ae8787d3759e)

### observed_connections-004754

```text
(config-router-ptmp)# timers <number:0..65535> <number:0..65535> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 9 `；EOL ` RVA 0x345AD518 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Keepalive interval；` unsigned_number ` Holdtime。

[条件 C-5329904497a13e15](../../evidence/conditions-sets-033.md#c-5329904497a13e15) · [参数 P-f1e10f7ff88c4e36](../../evidence/parameters-sets-018.md#p-f1e10f7ff88c4e36)

### observed_connections-004606

```text
(config-router-ptmp)# translate-topology <number:1..4095> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 67 `；EOL ` RVA 0x3459ECB8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Topology id。

[条件 C-f7386af78419fa98](../../evidence/conditions-sets-095.md#c-f7386af78419fa98) · [参数 P-30a41913e146154b](../../evidence/parameters-sets-004.md#p-30a41913e146154b)

### observed_connections-004577

```text
(config-router-ptmp)# translate-update <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 66 `；EOL ` RVA 0x3459FCB8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ace0427610e5d65a](../../evidence/conditions-sets-067.md#c-ace0427610e5d65a) · [状态效果 S-0e15d0d3841efa0c](../../evidence/state_effects-sets-003.md#s-0e15d0d3841efa0c)

### observed_connections-004695

```text
(config-router-ptmp)# transport multi-session <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 25 `；EOL ` RVA 0x345AF858 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a5f9f132d9176900](../../evidence/conditions-sets-064.md#c-a5f9f132d9176900) · [状态效果 S-909d8991439ef91a](../../evidence/state_effects-sets-031.md#s-909d8991439ef91a)

### observed_connections-004694

```text
(config-router-ptmp)# transport path-mtu-discovery <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 24 `；EOL ` RVA 0x345AF4B0 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a5f9f132d9176900](../../evidence/conditions-sets-064.md#c-a5f9f132d9176900) · [状态效果 S-c5ed6f5c16bd0dc4](../../evidence/state_effects-sets-042.md#s-c5ed6f5c16bd0dc4)

### observed_connections-004759

```text
(config-router-ptmp)# ttl-security hops <number:1..254> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 21 `；EOL ` RVA 0x345B01E8 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` maximum number of hops。

[条件 C-f0d336a8d254b40b](../../evidence/conditions-sets-093.md#c-f0d336a8d254b40b) · [参数 P-758b48736f7d1a30](../../evidence/parameters-sets-009.md#p-758b48736f7d1a30)

### observed_connections-004622

```text
(config-router-ptmp)# unsuppress-map <string> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 53 `；EOL ` RVA 0x345A2390 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of route map。

[条件 C-0e0a9002a8432d6f](../../evidence/conditions-sets-006.md#c-0e0a9002a8432d6f) · [参数 P-8965946866e4fcdf](../../evidence/parameters-sets-011.md#p-8965946866e4fcdf)

### observed_connections-004799

```text
(config-router-ptmp)# update in labeled-unicast unique <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 33 `；EOL ` RVA 0x345B2630 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7cda7f9a73e4e09e](../../evidence/conditions-sets-048.md#c-7cda7f9a73e4e09e) · [状态效果 S-426a6ac0b58dddcc](../../evidence/state_effects-sets-015.md#s-426a6ac0b58dddcc)

### observed_connections-004811

```text
(config-router-ptmp)# update-source <interface> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 4 `；EOL ` RVA 0x345A5890 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-da733ca6b1b7fee9](../../evidence/conditions-sets-084.md#c-da733ca6b1b7fee9) · [缺口 G-5831209d780282a0](../../evidence/gaps-sets-004.md#g-5831209d780282a0) · [参数 P-32fb03ad581dcf08](../../evidence/parameters-sets-004.md#p-32fb03ad581dcf08)

### observed_connections-004687

```text
(config-router-ptmp)# use nexthop-attribute <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 37 `；EOL ` RVA 0x345ADDA0 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ed1f096b95dca6d9](../../evidence/conditions-sets-092.md#c-ed1f096b95dca6d9)

### observed_connections-004655

```text
(config-router-ptmp)# validation off <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 83 `；EOL ` RVA 0x345A8648 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7672f21443040657](../../evidence/conditions-sets-046.md#c-7672f21443040657)

### observed_connections-004657

```text
(config-router-ptmp)# validation redirect-off <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 84 `；EOL ` RVA 0x345A88F0 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7672f21443040657](../../evidence/conditions-sets-046.md#c-7672f21443040657)

### observed_connections-004570

```text
(config-router-ptmp)# version <number:4..4> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 2 `；EOL ` RVA 0x345A4CA0 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Neighbor's BGP version。

[条件 C-e9762d1a4ca99f68](../../evidence/conditions-sets-090.md#c-e9762d1a4ca99f68) · [参数 P-f8e3c1bbfcdf99ec](../../evidence/parameters-sets-019.md#p-f8e3c1bbfcdf99ec)

### observed_connections-004636

```text
(config-router-ptmp)# weight <number:0..65535> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 41 `；EOL ` RVA 0x345A5098 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` default weight。

[条件 C-c78292a78588bb94](../../evidence/conditions-sets-077.md#c-c78292a78588bb94) · [参数 P-93cdadeb11c2f108](../../evidence/parameters-sets-011.md#p-93cdadeb11c2f108)

### observed_connections-004571

```text
(config-router-ptmp)# <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 0 `；EOL ` RVA 0x345AF110 `。

模式根 ` RVA 0x3459E460 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b9edc2fb9fefc7e0](../../evidence/conditions-sets-072.md#c-b9edc2fb9fefc7e0)
