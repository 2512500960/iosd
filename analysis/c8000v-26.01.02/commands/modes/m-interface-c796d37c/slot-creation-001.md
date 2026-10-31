# interface · 依赖静态建槽的条件安装

[模式索引](README.md) · [总索引](../../README.md)

### static_slot_creation_candidates-003749

```text
(config-if)# atm mcpt-timers <cr>
```

Handler ` RVA 0xEC4D100 `；selector ` 89 `；EOL ` RVA 0x33719C68 `。

模式根 ` RVA 0x34116920 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-398ac01bc1f6ffff](../../evidence/conditional_registrations-sets-001.md#r-398ac01bc1f6ffff) · [条件 C-de8f6c5eed7dd48e](../../evidence/conditions-sets-086.md#c-de8f6c5eed7dd48e) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-175a5beb246e20f5](../../evidence/state_effects-sets-005.md#s-175a5beb246e20f5)

### static_slot_creation_candidates-003798

```text
(config-if)# atm mcpt-timers <number:dynamic> <number:dynamic> <number:dynamic> <cr>
```

Handler ` RVA 0xEC4D100 `；selector ` 89 `；EOL ` RVA 0x33719C68 `。

模式根 ` RVA 0x34116920 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` MCPT timer1 value in microsecond；` unsigned_number_dynamic ` MCPT timer2 value in microsecond；` unsigned_number_dynamic ` MCPT timer3 value in microsecond。

[候选注册 R-398ac01bc1f6ffff](../../evidence/conditional_registrations-sets-001.md#r-398ac01bc1f6ffff) · [条件 C-4f331f961bdaf1e4](../../evidence/conditions-sets-031.md#c-4f331f961bdaf1e4) · [缺口 G-a623e5a40d4e99ea](../../evidence/gaps-sets-006.md#g-a623e5a40d4e99ea) · [参数 P-156040d312c55bcb](../../evidence/parameters-sets-002.md#p-156040d312c55bcb)

### static_slot_creation_candidates-003785

```text
(config-if)# atm pppatm link reset <cr>
```

Handler ` RVA 0x1111E590 `；selector ` 1 `；EOL ` RVA 0x35406038 `。

模式根 ` RVA 0x34116920 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-f88686060f6fd0bf](../../evidence/conditional_registrations-sets-003.md#r-f88686060f6fd0bf) · [条件 C-dc1439ed61f097f1](../../evidence/conditions-sets-085.md#c-dc1439ed61f097f1) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### static_slot_creation_candidates-003757

```text
(config-if)# atm pppatm passive <cr>
```

Handler ` RVA 0x1111E590 `；selector ` 0 `；EOL ` RVA 0x35405D50 `。

模式根 ` RVA 0x34116920 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-f88686060f6fd0bf](../../evidence/conditional_registrations-sets-003.md#r-f88686060f6fd0bf) · [条件 C-dc1439ed61f097f1](../../evidence/conditions-sets-085.md#c-dc1439ed61f097f1) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### static_slot_creation_candidates-003759

```text
(config-if)# crypto ipsec df-bit copy <cr>
```

Handler ` RVA 0x18D80E00 `；selector ` 1 `；EOL ` RVA 0x368B5968 `。

模式根 ` RVA 0x34116920 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-4d8c1819baf29d4b](../../evidence/conditional_registrations-sets-001.md#r-4d8c1819baf29d4b) · [条件 C-ff7a8586161e2b05](../../evidence/conditions-sets-098.md#c-ff7a8586161e2b05) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-6fcb7d0cea2d912b](../../evidence/state_effects-sets-024.md#s-6fcb7d0cea2d912b)

### static_slot_creation_candidates-003762

```text
(config-if)# crypto ipsec fragmentation after-encryption <cr>
```

Handler ` RVA 0x18D813B0 `；selector ` 1 `；EOL ` RVA 0x368B5D60 `。

模式根 ` RVA 0x34116920 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-4d8c1819baf29d4b](../../evidence/conditional_registrations-sets-001.md#r-4d8c1819baf29d4b) · [条件 C-7194b9032025c408](../../evidence/conditions-sets-044.md#c-7194b9032025c408) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-2ab32c8851ce41d6](../../evidence/state_effects-sets-010.md#s-2ab32c8851ce41d6)

### static_slot_creation_candidates-003793

```text
(config-if)# default atm pppatm link reset <cr>
```

Handler ` RVA 0x1111E590 `；selector ` 1 `；EOL ` RVA 0x35406038 `。

模式根 ` RVA 0x34116920 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-f88686060f6fd0bf](../../evidence/conditional_registrations-sets-003.md#r-f88686060f6fd0bf) · [条件 C-dc1439ed61f097f1](../../evidence/conditions-sets-085.md#c-dc1439ed61f097f1) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### static_slot_creation_candidates-003784

```text
(config-if)# default atm pppatm passive <cr>
```

Handler ` RVA 0x1111E590 `；selector ` 0 `；EOL ` RVA 0x35405D50 `。

模式根 ` RVA 0x34116920 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-f88686060f6fd0bf](../../evidence/conditional_registrations-sets-003.md#r-f88686060f6fd0bf) · [条件 C-dc1439ed61f097f1](../../evidence/conditions-sets-085.md#c-dc1439ed61f097f1) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### static_slot_creation_candidates-003760

```text
(config-if)# default crypto ipsec df-bit <cr>
```

Handler ` RVA 0x18D80E00 `；selector ` 1 `；EOL ` RVA 0x368B5968 `。

模式根 ` RVA 0x34116920 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-4d8c1819baf29d4b](../../evidence/conditional_registrations-sets-001.md#r-4d8c1819baf29d4b) · [条件 C-ee72a47668e86c99](../../evidence/conditions-sets-092.md#c-ee72a47668e86c99) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### static_slot_creation_candidates-003763

```text
(config-if)# default crypto ipsec fragmentation <cr>
```

Handler ` RVA 0x18D813B0 `；selector ` 1 `；EOL ` RVA 0x368B5D60 `。

模式根 ` RVA 0x34116920 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-4d8c1819baf29d4b](../../evidence/conditional_registrations-sets-001.md#r-4d8c1819baf29d4b) · [条件 C-3431bc7d06bfb531](../../evidence/conditions-sets-020.md#c-3431bc7d06bfb531) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### static_slot_creation_candidates-003797

```text
(config-if)# default otv isis authentication key-chain <string> <cr>
```

Handler ` RVA 0x16B806A0 `；selector ` 7 `；EOL ` RVA 0x36113F98 `。

模式根 ` RVA 0x34116920 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Name of key-chain。

[候选注册 R-1af9cd743aa46bfc](../../evidence/conditional_registrations-sets-001.md#r-1af9cd743aa46bfc) · [条件 C-4a32c2b3f701a342](../../evidence/conditions-sets-029.md#c-4a32c2b3f701a342) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-0f70ef71b9991f7c](../../evidence/parameters-sets-002.md#p-0f70ef71b9991f7c) · [状态效果 S-8814f5c496ec716e](../../evidence/state_effects-sets-029.md#s-8814f5c496ec716e)

### static_slot_creation_candidates-003795

```text
(config-if)# default otv isis authentication mode md5 <cr>
```

Handler ` RVA 0x16B806A0 `；selector ` 6 `；EOL ` RVA 0x36113C00 `。

模式根 ` RVA 0x34116920 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-1af9cd743aa46bfc](../../evidence/conditional_registrations-sets-001.md#r-1af9cd743aa46bfc) · [条件 C-4a32c2b3f701a342](../../evidence/conditions-sets-029.md#c-4a32c2b3f701a342) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-16d8064781be5fe6](../../evidence/state_effects-sets-005.md#s-16d8064781be5fe6)

### static_slot_creation_candidates-003791

```text
(config-if)# default otv isis authentication send-only <cr>
```

Handler ` RVA 0x16B806A0 `；selector ` 8 `；EOL ` RVA 0x36114288 `。

模式根 ` RVA 0x34116920 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-1af9cd743aa46bfc](../../evidence/conditional_registrations-sets-001.md#r-1af9cd743aa46bfc) · [条件 C-4a32c2b3f701a342](../../evidence/conditions-sets-029.md#c-4a32c2b3f701a342) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-3e7ff00ab2f570d8](../../evidence/state_effects-sets-014.md#s-3e7ff00ab2f570d8)

### static_slot_creation_candidates-003772

```text
(config-if)# default otv isis bfd <cr>
```

Handler ` RVA 0x16B806A0 `；selector ` 10 `；EOL ` RVA 0x36114948 `。

模式根 ` RVA 0x34116920 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-1af9cd743aa46bfc](../../evidence/conditional_registrations-sets-001.md#r-1af9cd743aa46bfc) · [条件 C-4a32c2b3f701a342](../../evidence/conditions-sets-029.md#c-4a32c2b3f701a342) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-ad23c49694e6b63c](../../evidence/state_effects-sets-037.md#s-ad23c49694e6b63c)

### static_slot_creation_candidates-003780

```text
(config-if)# default otv isis csnp-interval <cr>
```

Handler ` RVA 0x16B806A0 `；selector ` 12 `；EOL ` RVA 0x361152B8 `。

模式根 ` RVA 0x34116920 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-1af9cd743aa46bfc](../../evidence/conditional_registrations-sets-001.md#r-1af9cd743aa46bfc) · [条件 C-6ff31f8213ed241a](../../evidence/conditions-sets-043.md#c-6ff31f8213ed241a) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-b43c567dd87b8efa](../../evidence/state_effects-sets-038.md#s-b43c567dd87b8efa)

### static_slot_creation_candidates-003787

```text
(config-if)# default otv isis hello padding <cr>
```

Handler ` RVA 0x16B806A0 `；selector ` 5 `；EOL ` RVA 0x361137D8 `。

模式根 ` RVA 0x34116920 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-1af9cd743aa46bfc](../../evidence/conditional_registrations-sets-001.md#r-1af9cd743aa46bfc) · [条件 C-4a32c2b3f701a342](../../evidence/conditions-sets-029.md#c-4a32c2b3f701a342) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-ad23c49694e6b63c](../../evidence/state_effects-sets-037.md#s-ad23c49694e6b63c)

### static_slot_creation_candidates-003773

```text
(config-if)# default otv isis hello-interval <cr>
```

Handler ` RVA 0x16B806A0 `；selector ` 3 `；EOL ` RVA 0x361133F0 `。

模式根 ` RVA 0x34116920 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-1af9cd743aa46bfc](../../evidence/conditional_registrations-sets-001.md#r-1af9cd743aa46bfc) · [条件 C-c04b6e96477d8001](../../evidence/conditions-sets-074.md#c-c04b6e96477d8001) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-77b0f20b0581ac0a](../../evidence/state_effects-sets-025.md#s-77b0f20b0581ac0a)

### static_slot_creation_candidates-003768

```text
(config-if)# default otv isis hello-multiplier <cr>
```

Handler ` RVA 0x16B806A0 `；selector ` 4 `；EOL ` RVA 0x36113030 `。

模式根 ` RVA 0x34116920 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-1af9cd743aa46bfc](../../evidence/conditional_registrations-sets-001.md#r-1af9cd743aa46bfc) · [条件 C-245ce5680e6cf811](../../evidence/conditions-sets-014.md#c-245ce5680e6cf811) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-75fc55f80a0b8250](../../evidence/state_effects-sets-025.md#s-75fc55f80a0b8250)

### static_slot_creation_candidates-003756

```text
(config-if)# default otv isis lsp-interval <cr>
```

Handler ` RVA 0x16B806A0 `；selector ` 13 `；EOL ` RVA 0x36115800 `。

模式根 ` RVA 0x34116920 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-1af9cd743aa46bfc](../../evidence/conditional_registrations-sets-001.md#r-1af9cd743aa46bfc) · [条件 C-426f8f37f7171f55](../../evidence/conditions-sets-026.md#c-426f8f37f7171f55) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-ad23c49694e6b63c](../../evidence/state_effects-sets-037.md#s-ad23c49694e6b63c)

### static_slot_creation_candidates-003782

```text
(config-if)# default otv isis metric <cr>
```

Handler ` RVA 0x16B806A0 `；selector ` 11 `；EOL ` RVA 0x36114DE8 `。

模式根 ` RVA 0x34116920 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-1af9cd743aa46bfc](../../evidence/conditional_registrations-sets-001.md#r-1af9cd743aa46bfc) · [条件 C-cc79bcc844510a27](../../evidence/conditions-sets-079.md#c-cc79bcc844510a27) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-b242c4a3d451f91e](../../evidence/state_effects-sets-038.md#s-b242c4a3d451f91e)

### static_slot_creation_candidates-003776

```text
(config-if)# default otv isis priority <cr>
```

Handler ` RVA 0x16B806A0 `；selector ` 9 `；EOL ` RVA 0x36114638 `。

模式根 ` RVA 0x34116920 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-1af9cd743aa46bfc](../../evidence/conditional_registrations-sets-001.md#r-1af9cd743aa46bfc) · [条件 C-8b80bd9a9a3241e9](../../evidence/conditions-sets-054.md#c-8b80bd9a9a3241e9) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-8c4aed21f382ecdb](../../evidence/state_effects-sets-030.md#s-8c4aed21f382ecdb)

### static_slot_creation_candidates-003754

```text
(config-if)# default otv isis retransmit-interval <cr>
```

Handler ` RVA 0x16B806A0 `；selector ` 14 `；EOL ` RVA 0x36115560 `。

模式根 ` RVA 0x34116920 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-1af9cd743aa46bfc](../../evidence/conditional_registrations-sets-001.md#r-1af9cd743aa46bfc) · [条件 C-ef1c925f0f5b2ded](../../evidence/conditions-sets-092.md#c-ef1c925f0f5b2ded) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-ad23c49694e6b63c](../../evidence/state_effects-sets-037.md#s-ad23c49694e6b63c)

### static_slot_creation_candidates-003752

```text
(config-if)# default otv isis retransmit-throttle-interval <cr>
```

Handler ` RVA 0x16B806A0 `；selector ` 15 `；EOL ` RVA 0x361151D0 `。

模式根 ` RVA 0x34116920 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-1af9cd743aa46bfc](../../evidence/conditional_registrations-sets-001.md#r-1af9cd743aa46bfc) · [条件 C-ddcfb541fd6c9f03](../../evidence/conditions-sets-085.md#c-ddcfb541fd6c9f03) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-ad23c49694e6b63c](../../evidence/state_effects-sets-037.md#s-ad23c49694e6b63c)

### static_slot_creation_candidates-003792

```text
(config-if)# no atm pppatm link reset <cr>
```

Handler ` RVA 0x1111E590 `；selector ` 1 `；EOL ` RVA 0x35406038 `。

模式根 ` RVA 0x34116920 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-f88686060f6fd0bf](../../evidence/conditional_registrations-sets-003.md#r-f88686060f6fd0bf) · [条件 C-dc1439ed61f097f1](../../evidence/conditions-sets-085.md#c-dc1439ed61f097f1) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-a763f0b283e40fef](../../evidence/state_effects-sets-035.md#s-a763f0b283e40fef)

### static_slot_creation_candidates-003783

```text
(config-if)# no atm pppatm passive <cr>
```

Handler ` RVA 0x1111E590 `；selector ` 0 `；EOL ` RVA 0x35405D50 `。

模式根 ` RVA 0x34116920 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-f88686060f6fd0bf](../../evidence/conditional_registrations-sets-003.md#r-f88686060f6fd0bf) · [条件 C-dc1439ed61f097f1](../../evidence/conditions-sets-085.md#c-dc1439ed61f097f1) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-a763f0b283e40fef](../../evidence/state_effects-sets-035.md#s-a763f0b283e40fef)

### static_slot_creation_candidates-003758

```text
(config-if)# no crypto ipsec df-bit <cr>
```

Handler ` RVA 0x18D80E00 `；selector ` 1 `；EOL ` RVA 0x368B5968 `。

模式根 ` RVA 0x34116920 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-4d8c1819baf29d4b](../../evidence/conditional_registrations-sets-001.md#r-4d8c1819baf29d4b) · [条件 C-03bdb141d5296d37](../../evidence/conditions-sets-002.md#c-03bdb141d5296d37) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-a763f0b283e40fef](../../evidence/state_effects-sets-035.md#s-a763f0b283e40fef)

### static_slot_creation_candidates-003761

```text
(config-if)# no crypto ipsec fragmentation <cr>
```

Handler ` RVA 0x18D813B0 `；selector ` 1 `；EOL ` RVA 0x368B5D60 `。

模式根 ` RVA 0x34116920 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-4d8c1819baf29d4b](../../evidence/conditional_registrations-sets-001.md#r-4d8c1819baf29d4b) · [条件 C-75546e07b7bf0918](../../evidence/conditions-sets-046.md#c-75546e07b7bf0918) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-a763f0b283e40fef](../../evidence/state_effects-sets-035.md#s-a763f0b283e40fef)

### static_slot_creation_candidates-003796

```text
(config-if)# no otv isis authentication key-chain <string> <cr>
```

Handler ` RVA 0x16B806A0 `；selector ` 7 `；EOL ` RVA 0x36113F98 `。

模式根 ` RVA 0x34116920 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Name of key-chain。

[候选注册 R-1af9cd743aa46bfc](../../evidence/conditional_registrations-sets-001.md#r-1af9cd743aa46bfc) · [条件 C-4a32c2b3f701a342](../../evidence/conditions-sets-029.md#c-4a32c2b3f701a342) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-0f70ef71b9991f7c](../../evidence/parameters-sets-002.md#p-0f70ef71b9991f7c) · [状态效果 S-8ef855361c0729a9](../../evidence/state_effects-sets-030.md#s-8ef855361c0729a9)

### static_slot_creation_candidates-003794

```text
(config-if)# no otv isis authentication mode md5 <cr>
```

Handler ` RVA 0x16B806A0 `；selector ` 6 `；EOL ` RVA 0x36113C00 `。

模式根 ` RVA 0x34116920 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-1af9cd743aa46bfc](../../evidence/conditional_registrations-sets-001.md#r-1af9cd743aa46bfc) · [条件 C-4a32c2b3f701a342](../../evidence/conditions-sets-029.md#c-4a32c2b3f701a342) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-e5fb55f83d4b04e4](../../evidence/state_effects-sets-049.md#s-e5fb55f83d4b04e4)

### static_slot_creation_candidates-003790

```text
(config-if)# no otv isis authentication send-only <cr>
```

Handler ` RVA 0x16B806A0 `；selector ` 8 `；EOL ` RVA 0x36114288 `。

模式根 ` RVA 0x34116920 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-1af9cd743aa46bfc](../../evidence/conditional_registrations-sets-001.md#r-1af9cd743aa46bfc) · [条件 C-4a32c2b3f701a342](../../evidence/conditions-sets-029.md#c-4a32c2b3f701a342) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-a7c684797a16cd26](../../evidence/state_effects-sets-035.md#s-a7c684797a16cd26)

### static_slot_creation_candidates-003769

```text
(config-if)# no otv isis bfd <cr>
```

Handler ` RVA 0x16B806A0 `；selector ` 10 `；EOL ` RVA 0x36114948 `。

模式根 ` RVA 0x34116920 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-1af9cd743aa46bfc](../../evidence/conditional_registrations-sets-001.md#r-1af9cd743aa46bfc) · [条件 C-4a32c2b3f701a342](../../evidence/conditions-sets-029.md#c-4a32c2b3f701a342) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-a432309068c1f923](../../evidence/state_effects-sets-035.md#s-a432309068c1f923)

### static_slot_creation_candidates-003779

```text
(config-if)# no otv isis csnp-interval <cr>
```

Handler ` RVA 0x16B806A0 `；selector ` 12 `；EOL ` RVA 0x361152B8 `。

模式根 ` RVA 0x34116920 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-1af9cd743aa46bfc](../../evidence/conditional_registrations-sets-001.md#r-1af9cd743aa46bfc) · [条件 C-6ff31f8213ed241a](../../evidence/conditions-sets-043.md#c-6ff31f8213ed241a) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-be3ce8ee50d8b617](../../evidence/state_effects-sets-040.md#s-be3ce8ee50d8b617)

### static_slot_creation_candidates-003786

```text
(config-if)# no otv isis hello padding <cr>
```

Handler ` RVA 0x16B806A0 `；selector ` 5 `；EOL ` RVA 0x361137D8 `。

模式根 ` RVA 0x34116920 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-1af9cd743aa46bfc](../../evidence/conditional_registrations-sets-001.md#r-1af9cd743aa46bfc) · [条件 C-4a32c2b3f701a342](../../evidence/conditions-sets-029.md#c-4a32c2b3f701a342) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-a432309068c1f923](../../evidence/state_effects-sets-035.md#s-a432309068c1f923)

### static_slot_creation_candidates-003770

```text
(config-if)# no otv isis hello-interval <cr>
```

Handler ` RVA 0x16B806A0 `；selector ` 3 `；EOL ` RVA 0x361133F0 `。

模式根 ` RVA 0x34116920 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-1af9cd743aa46bfc](../../evidence/conditional_registrations-sets-001.md#r-1af9cd743aa46bfc) · [条件 C-c04b6e96477d8001](../../evidence/conditions-sets-074.md#c-c04b6e96477d8001) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-4f6a39961dec134c](../../evidence/state_effects-sets-017.md#s-4f6a39961dec134c)

### static_slot_creation_candidates-003766

```text
(config-if)# no otv isis hello-multiplier <cr>
```

Handler ` RVA 0x16B806A0 `；selector ` 4 `；EOL ` RVA 0x36113030 `。

模式根 ` RVA 0x34116920 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-1af9cd743aa46bfc](../../evidence/conditional_registrations-sets-001.md#r-1af9cd743aa46bfc) · [条件 C-245ce5680e6cf811](../../evidence/conditions-sets-014.md#c-245ce5680e6cf811) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-5a09c2d3e363c054](../../evidence/state_effects-sets-019.md#s-5a09c2d3e363c054)

### static_slot_creation_candidates-003755

```text
(config-if)# no otv isis lsp-interval <cr>
```

Handler ` RVA 0x16B806A0 `；selector ` 13 `；EOL ` RVA 0x36115800 `。

模式根 ` RVA 0x34116920 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-1af9cd743aa46bfc](../../evidence/conditional_registrations-sets-001.md#r-1af9cd743aa46bfc) · [条件 C-426f8f37f7171f55](../../evidence/conditions-sets-026.md#c-426f8f37f7171f55) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-a432309068c1f923](../../evidence/state_effects-sets-035.md#s-a432309068c1f923)

### static_slot_creation_candidates-003781

```text
(config-if)# no otv isis metric <cr>
```

Handler ` RVA 0x16B806A0 `；selector ` 11 `；EOL ` RVA 0x36114DE8 `。

模式根 ` RVA 0x34116920 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-1af9cd743aa46bfc](../../evidence/conditional_registrations-sets-001.md#r-1af9cd743aa46bfc) · [条件 C-cc79bcc844510a27](../../evidence/conditions-sets-079.md#c-cc79bcc844510a27) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-96769d714525f338](../../evidence/state_effects-sets-032.md#s-96769d714525f338)

### static_slot_creation_candidates-003775

```text
(config-if)# no otv isis priority <cr>
```

Handler ` RVA 0x16B806A0 `；selector ` 9 `；EOL ` RVA 0x36114638 `。

模式根 ` RVA 0x34116920 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-1af9cd743aa46bfc](../../evidence/conditional_registrations-sets-001.md#r-1af9cd743aa46bfc) · [条件 C-8b80bd9a9a3241e9](../../evidence/conditions-sets-054.md#c-8b80bd9a9a3241e9) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-41fe9b60318326c0](../../evidence/state_effects-sets-014.md#s-41fe9b60318326c0)

### static_slot_creation_candidates-003753

```text
(config-if)# no otv isis retransmit-interval <cr>
```

Handler ` RVA 0x16B806A0 `；selector ` 14 `；EOL ` RVA 0x36115560 `。

模式根 ` RVA 0x34116920 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-1af9cd743aa46bfc](../../evidence/conditional_registrations-sets-001.md#r-1af9cd743aa46bfc) · [条件 C-ef1c925f0f5b2ded](../../evidence/conditions-sets-092.md#c-ef1c925f0f5b2ded) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-a432309068c1f923](../../evidence/state_effects-sets-035.md#s-a432309068c1f923)

### static_slot_creation_candidates-003751

```text
(config-if)# no otv isis retransmit-throttle-interval <cr>
```

Handler ` RVA 0x16B806A0 `；selector ` 15 `；EOL ` RVA 0x361151D0 `。

模式根 ` RVA 0x34116920 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-1af9cd743aa46bfc](../../evidence/conditional_registrations-sets-001.md#r-1af9cd743aa46bfc) · [条件 C-ddcfb541fd6c9f03](../../evidence/conditions-sets-085.md#c-ddcfb541fd6c9f03) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-a432309068c1f923](../../evidence/state_effects-sets-035.md#s-a432309068c1f923)

### static_slot_creation_candidates-003789

```text
(config-if)# otv isis authentication key-chain <string> <cr>
```

Handler ` RVA 0x16B806A0 `；selector ` 7 `；EOL ` RVA 0x36113F98 `。

模式根 ` RVA 0x34116920 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of key-chain。

[候选注册 R-1af9cd743aa46bfc](../../evidence/conditional_registrations-sets-001.md#r-1af9cd743aa46bfc) · [条件 C-4a32c2b3f701a342](../../evidence/conditions-sets-029.md#c-4a32c2b3f701a342) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-0f70ef71b9991f7c](../../evidence/parameters-sets-002.md#p-0f70ef71b9991f7c) · [状态效果 S-9cb976e7822fb352](../../evidence/state_effects-sets-033.md#s-9cb976e7822fb352)

### static_slot_creation_candidates-003788

```text
(config-if)# otv isis authentication mode md5 <cr>
```

Handler ` RVA 0x16B806A0 `；selector ` 6 `；EOL ` RVA 0x36113C00 `。

模式根 ` RVA 0x34116920 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-1af9cd743aa46bfc](../../evidence/conditional_registrations-sets-001.md#r-1af9cd743aa46bfc) · [条件 C-4a32c2b3f701a342](../../evidence/conditions-sets-029.md#c-4a32c2b3f701a342) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-796926443f60457c](../../evidence/state_effects-sets-026.md#s-796926443f60457c)

### static_slot_creation_candidates-003774

```text
(config-if)# otv isis authentication send-only <cr>
```

Handler ` RVA 0x16B806A0 `；selector ` 8 `；EOL ` RVA 0x36114288 `。

模式根 ` RVA 0x34116920 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-1af9cd743aa46bfc](../../evidence/conditional_registrations-sets-001.md#r-1af9cd743aa46bfc) · [条件 C-4a32c2b3f701a342](../../evidence/conditions-sets-029.md#c-4a32c2b3f701a342) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-b85d38ee6ecce1d7](../../evidence/state_effects-sets-039.md#s-b85d38ee6ecce1d7)

### static_slot_creation_candidates-003750

```text
(config-if)# otv isis bfd <cr>
```

Handler ` RVA 0x16B806A0 `；selector ` 10 `；EOL ` RVA 0x36114948 `。

模式根 ` RVA 0x34116920 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-1af9cd743aa46bfc](../../evidence/conditional_registrations-sets-001.md#r-1af9cd743aa46bfc) · [条件 C-4a32c2b3f701a342](../../evidence/conditions-sets-029.md#c-4a32c2b3f701a342) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-a84a8b25d3111eb7](../../evidence/state_effects-sets-036.md#s-a84a8b25d3111eb7)

### static_slot_creation_candidates-003777

```text
(config-if)# otv isis csnp-interval <number:0..65535> <cr>
```

Handler ` RVA 0x16B806A0 `；selector ` 12 `；EOL ` RVA 0x361152B8 `。

模式根 ` RVA 0x34116920 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` CSNP interval value。

[候选注册 R-1af9cd743aa46bfc](../../evidence/conditional_registrations-sets-001.md#r-1af9cd743aa46bfc) · [条件 C-44395d6bc061ada3](../../evidence/conditions-sets-027.md#c-44395d6bc061ada3) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-734fbdf45db80cca](../../evidence/parameters-sets-009.md#p-734fbdf45db80cca) · [状态效果 S-57df016d2623589b](../../evidence/state_effects-sets-019.md#s-57df016d2623589b)

### static_slot_creation_candidates-003767

```text
(config-if)# otv isis hello padding <cr>
```

Handler ` RVA 0x16B806A0 `；selector ` 5 `；EOL ` RVA 0x361137D8 `。

模式根 ` RVA 0x34116920 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-1af9cd743aa46bfc](../../evidence/conditional_registrations-sets-001.md#r-1af9cd743aa46bfc) · [条件 C-4a32c2b3f701a342](../../evidence/conditions-sets-029.md#c-4a32c2b3f701a342) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-a84a8b25d3111eb7](../../evidence/state_effects-sets-036.md#s-a84a8b25d3111eb7)

### static_slot_creation_candidates-003765

```text
(config-if)# otv isis hello-interval <number:1..65535> <cr>
```

Handler ` RVA 0x16B806A0 `；selector ` 3 `；EOL ` RVA 0x361133F0 `。

模式根 ` RVA 0x34116920 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Hello interval value。

[候选注册 R-1af9cd743aa46bfc](../../evidence/conditional_registrations-sets-001.md#r-1af9cd743aa46bfc) · [条件 C-4a32c2b3f701a342](../../evidence/conditions-sets-029.md#c-4a32c2b3f701a342) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-b40ffed31bbc7cbc](../../evidence/parameters-sets-014.md#p-b40ffed31bbc7cbc) · [状态效果 S-dfae9919630fa915](../../evidence/state_effects-sets-047.md#s-dfae9919630fa915)

### static_slot_creation_candidates-003764

```text
(config-if)# otv isis hello-multiplier <number:3..1000> <cr>
```

Handler ` RVA 0x16B806A0 `；selector ` 4 `；EOL ` RVA 0x36113030 `。

模式根 ` RVA 0x34116920 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Hello multiplier value。

[候选注册 R-1af9cd743aa46bfc](../../evidence/conditional_registrations-sets-001.md#r-1af9cd743aa46bfc) · [条件 C-4a32c2b3f701a342](../../evidence/conditions-sets-029.md#c-4a32c2b3f701a342) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-65f525302449487b](../../evidence/parameters-sets-008.md#p-65f525302449487b) · [状态效果 S-c61dc860625b55ad](../../evidence/state_effects-sets-042.md#s-c61dc860625b55ad)

### static_slot_creation_candidates-003748

```text
(config-if)# otv isis lsp-interval <number:1..4294967295> <cr>
```

Handler ` RVA 0x16B806A0 `；selector ` 13 `；EOL ` RVA 0x36115800 `。

模式根 ` RVA 0x34116920 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` LSP transmission interval (milliseconds)。

[候选注册 R-1af9cd743aa46bfc](../../evidence/conditional_registrations-sets-001.md#r-1af9cd743aa46bfc) · [条件 C-3ba5801957af692b](../../evidence/conditions-sets-023.md#c-3ba5801957af692b) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-f91bec73d40ba6be](../../evidence/parameters-sets-019.md#p-f91bec73d40ba6be) · [状态效果 S-a84a8b25d3111eb7](../../evidence/state_effects-sets-036.md#s-a84a8b25d3111eb7)

### static_slot_creation_candidates-003778

```text
(config-if)# otv isis metric <number:1..16777214> <cr>
```

Handler ` RVA 0x16B806A0 `；selector ` 11 `；EOL ` RVA 0x36114DE8 `。

模式根 ` RVA 0x34116920 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Default metric。

[候选注册 R-1af9cd743aa46bfc](../../evidence/conditional_registrations-sets-001.md#r-1af9cd743aa46bfc) · [条件 C-44395d6bc061ada3](../../evidence/conditions-sets-027.md#c-44395d6bc061ada3) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-2dffe833f3eb4040](../../evidence/parameters-sets-004.md#p-2dffe833f3eb4040) · [状态效果 S-ea338d2e86ae1e9b](../../evidence/state_effects-sets-050.md#s-ea338d2e86ae1e9b)

### static_slot_creation_candidates-003771

```text
(config-if)# otv isis priority <number:0..127> <cr>
```

Handler ` RVA 0x16B806A0 `；selector ` 9 `；EOL ` RVA 0x36114638 `。

模式根 ` RVA 0x34116920 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Priority value。

[候选注册 R-1af9cd743aa46bfc](../../evidence/conditional_registrations-sets-001.md#r-1af9cd743aa46bfc) · [条件 C-4a32c2b3f701a342](../../evidence/conditions-sets-029.md#c-4a32c2b3f701a342) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-fccd3f21b9acc8df](../../evidence/parameters-sets-019.md#p-fccd3f21b9acc8df) · [状态效果 S-27a485b9dcf1160b](../../evidence/state_effects-sets-009.md#s-27a485b9dcf1160b)

### static_slot_creation_candidates-003747

```text
(config-if)# otv isis retransmit-interval <number:0..65535> <cr>
```

Handler ` RVA 0x16B806A0 `；selector ` 14 `；EOL ` RVA 0x36115560 `。

模式根 ` RVA 0x34116920 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Interval between retransmissions of the same LSP (seconds)。

[候选注册 R-1af9cd743aa46bfc](../../evidence/conditional_registrations-sets-001.md#r-1af9cd743aa46bfc) · [条件 C-602b7a0a3e923358](../../evidence/conditions-sets-037.md#c-602b7a0a3e923358) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-5324c07ff2ca1159](../../evidence/parameters-sets-007.md#p-5324c07ff2ca1159) · [状态效果 S-a84a8b25d3111eb7](../../evidence/state_effects-sets-036.md#s-a84a8b25d3111eb7)

### static_slot_creation_candidates-003746

```text
(config-if)# otv isis retransmit-throttle-interval <number:0..65535> <cr>
```

Handler ` RVA 0x16B806A0 `；selector ` 15 `；EOL ` RVA 0x361151D0 `。

模式根 ` RVA 0x34116920 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Delay between retransmitted LSPs (milliseconds)。

[候选注册 R-1af9cd743aa46bfc](../../evidence/conditional_registrations-sets-001.md#r-1af9cd743aa46bfc) · [条件 C-a47e04b30138fe02](../../evidence/conditions-sets-063.md#c-a47e04b30138fe02) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-cf5654999156e23e](../../evidence/parameters-sets-016.md#p-cf5654999156e23e) · [状态效果 S-a84a8b25d3111eb7](../../evidence/state_effects-sets-036.md#s-a84a8b25d3111eb7)

