# atm-vc-config · 依赖静态建槽的条件安装

[模式索引](README.md) · [总索引](../../README.md)

### static_slot_creation_candidates-003106

```text
(config-if-atm-vc)# aaa connect-info <string> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 87 `；EOL ` RVA 0x336EDE58 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` connect-info。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-9ecf1bd1f2827f3c](../../evidence/conditions-sets-061.md#c-9ecf1bd1f2827f3c) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-667497da54ece39e](../../evidence/parameters-sets-008.md#p-667497da54ece39e)

### static_slot_creation_candidates-003155

```text
(config-if-atm-vc)# abr <number:dynamic> <number:dynamic> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 8 `；EOL ` RVA 0x336EBA88 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Peak Cell Rate(PCR) in Kbps；` unsigned_number_dynamic ` Minimum Cell Rate(MCR) in Kbps。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-7510aea5c174d6e8](../../evidence/conditions-sets-045.md#c-7510aea5c174d6e8) · [缺口 G-2967865facc5c5b5](../../evidence/gaps-sets-002.md#g-2967865facc5c5b5) · [参数 P-eeba2a32aaf22d54](../../evidence/parameters-sets-018.md#p-eeba2a32aaf22d54)

### static_slot_creation_candidates-003159

```text
(config-if-atm-vc)# abr rate-factors <?keyword_option_mm_action@555588c3fdd8> <?keyword_option_mm_action@555588c3fe28> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 34 `；EOL ` RVA 0x336EBE00 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-51715393344a813d](../../evidence/conditions-sets-032.md#c-51715393344a813d) · [缺口 G-a05978c6bbf7d88f](../../evidence/gaps-sets-006.md#g-a05978c6bbf7d88f)

### static_slot_creation_candidates-003045

```text
(config-if-atm-vc)# ancp enable <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 89 `；EOL ` RVA 0x336ECDE8 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-f05252715ccb4620](../../evidence/conditions-sets-093.md#c-f05252715ccb4620) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### static_slot_creation_candidates-003134

```text
(config-if-atm-vc)# ancp neighbor name <string> id <string> client-id <string> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 88 `；EOL ` RVA 0x336ED2E0 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Neighbor name；` string ` ANCP neighbor ID；` string ` ANCP client ID。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-f954a8bd29caef8e](../../evidence/conditions-sets-096.md#c-f954a8bd29caef8e) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-b8558c3e12071398](../../evidence/parameters-sets-014.md#p-b8558c3e12071398)

### static_slot_creation_candidates-003142

```text
(config-if-atm-vc)# bre-connect <number:dynamic> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 64 `；EOL ` RVA 0x336EED30 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` VLAN Number。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-77c6ebe41ae20727](../../evidence/conditions-sets-047.md#c-77c6ebe41ae20727) · [缺口 G-683e733daf7c337d](../../evidence/gaps-sets-004.md#g-683e733daf7c337d) · [参数 P-2c97200e82da00ab](../../evidence/parameters-sets-004.md#p-2c97200e82da00ab)

### static_slot_creation_candidates-003148

```text
(config-if-atm-vc)# bridge-dot1q encap <number:dynamic> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 93 `；EOL ` RVA 0x336EC548 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` vlan id to be inserted in dot1q tag header。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-047adb0178214875](../../evidence/conditions-sets-002.md#c-047adb0178214875) · [缺口 G-98d5137ff60aa511](../../evidence/gaps-sets-006.md#g-98d5137ff60aa511) · [参数 P-f383eead51f3b0ad](../../evidence/parameters-sets-018.md#p-f383eead51f3b0ad)

### static_slot_creation_candidates-003101

```text
(config-if-atm-vc)# bridge-dot1q encap priority-tag <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 93 `；EOL ` RVA 0x336EC548 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-63dad428f9daf41c](../../evidence/conditions-sets-039.md#c-63dad428f9daf41c) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-7894398496f00dae](../../evidence/state_effects-sets-026.md#s-7894398496f00dae)

### static_slot_creation_candidates-003143

```text
(config-if-atm-vc)# bridge-vlan <number:dynamic> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 63 `；EOL ` RVA 0x336EE2E8 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Bridge domain number。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-c7c6ff75d2f1f321](../../evidence/conditions-sets-077.md#c-c7c6ff75d2f1f321) · [缺口 G-580cd7f59d64aed0](../../evidence/gaps-sets-004.md#g-580cd7f59d64aed0) · [参数 P-fd646dd6ab49a9d9](../../evidence/parameters-sets-019.md#p-fd646dd6ab49a9d9)

### static_slot_creation_candidates-003015

```text
(config-if-atm-vc)# broadcast <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 27 `；EOL ` RVA 0x336F6130 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-127058859fbe8d5c](../../evidence/conditions-sets-007.md#c-127058859fbe8d5c) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-cb10445508f52250](../../evidence/state_effects-sets-043.md#s-cb10445508f52250)

### static_slot_creation_candidates-003016

```text
(config-if-atm-vc)# cac_off <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 74 `；EOL ` RVA 0x336ED700 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-eac7ea8d9af2dc34](../../evidence/conditions-sets-091.md#c-eac7ea8d9af2dc34) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### static_slot_creation_candidates-003139

```text
(config-if-atm-vc)# cbr <number:dynamic> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 7 `；EOL ` RVA 0x336EB240 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Peak Cell Rate in Kbps。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-50ce042c8d0e2113](../../evidence/conditions-sets-032.md#c-50ce042c8d0e2113) · [缺口 G-a5a3b9fad953dae6](../../evidence/gaps-sets-006.md#g-a5a3b9fad953dae6) · [参数 P-f1c17a1ccf457a16](../../evidence/parameters-sets-018.md#p-f1c17a1ccf457a16)

### static_slot_creation_candidates-003137

```text
(config-if-atm-vc)# cdvt <number:dynamic> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 82 `；EOL ` RVA 0x336EA740 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` CDVT in units of tenths of a microsecond。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-8cdc98b888988e35](../../evidence/conditions-sets-055.md#c-8cdc98b888988e35) · [缺口 G-6132beefe6633158](../../evidence/gaps-sets-004.md#g-6132beefe6633158) · [参数 P-b537d9b74581f25e](../../evidence/parameters-sets-014.md#p-b537d9b74581f25e)

### static_slot_creation_candidates-003039

```text
(config-if-atm-vc)# class-vc <string> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 10 `；EOL ` RVA 0x336F6498 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` ATM vc-class name to use on this VC。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-68828ed599cf8d7d](../../evidence/conditions-sets-040.md#c-68828ed599cf8d7d) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-c166c02862c48f7d](../../evidence/parameters-sets-015.md#p-c166c02862c48f7d)

### static_slot_creation_candidates-003083

```text
(config-if-atm-vc)# dbs enable <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 69 `；EOL ` RVA 0x336F11F8 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-73938a3131b5f175](../../evidence/conditions-sets-045.md#c-73938a3131b5f175) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-f166def7797fec92](../../evidence/state_effects-sets-051.md#s-f166def7797fec92)

### static_slot_creation_candidates-003025

```text
(config-if-atm-vc)# default <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 35 `；EOL ` RVA 0x336F4FB8 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-fc8024a246166e79](../../evidence/conditions-sets-097.md#c-fc8024a246166e79) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-e493cd2d5e9e8d4b](../../evidence/state_effects-sets-048.md#s-e493cd2d5e9e8d4b)

### static_slot_creation_candidates-003107

```text
(config-if-atm-vc)# default aaa connect-info <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 87 `；EOL ` RVA 0x336EDE58 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-821d034573921417](../../evidence/conditions-sets-050.md#c-821d034573921417) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-e493cd2d5e9e8d4b](../../evidence/state_effects-sets-048.md#s-e493cd2d5e9e8d4b)

### static_slot_creation_candidates-003099

```text
(config-if-atm-vc)# default abr rate-factors <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 34 `；EOL ` RVA 0x336EBE00 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-99a691ebe574098e](../../evidence/conditions-sets-059.md#c-99a691ebe574098e) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-e493cd2d5e9e8d4b](../../evidence/state_effects-sets-048.md#s-e493cd2d5e9e8d4b)

### static_slot_creation_candidates-003104

```text
(config-if-atm-vc)# default ancp enable <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 89 `；EOL ` RVA 0x336ECDE8 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-a494f67e8d32fc7b](../../evidence/conditions-sets-063.md#c-a494f67e8d32fc7b) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-e493cd2d5e9e8d4b](../../evidence/state_effects-sets-048.md#s-e493cd2d5e9e8d4b)

### static_slot_creation_candidates-003136

```text
(config-if-atm-vc)# default ancp neighbor name <string> id <string> client-id <string> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 88 `；EOL ` RVA 0x336ED2E0 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Neighbor name；` string ` ANCP neighbor ID；` string ` ANCP client ID。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-4ed24dd3bb24c7e3](../../evidence/conditions-sets-031.md#c-4ed24dd3bb24c7e3) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-b8558c3e12071398](../../evidence/parameters-sets-014.md#p-b8558c3e12071398) · [状态效果 S-e493cd2d5e9e8d4b](../../evidence/state_effects-sets-048.md#s-e493cd2d5e9e8d4b)

### static_slot_creation_candidates-003056

```text
(config-if-atm-vc)# default bre-connect <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 64 `；EOL ` RVA 0x336EED30 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-c5c92b1b8e547fcf](../../evidence/conditions-sets-076.md#c-c5c92b1b8e547fcf) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-e493cd2d5e9e8d4b](../../evidence/state_effects-sets-048.md#s-e493cd2d5e9e8d4b)

### static_slot_creation_candidates-003098

```text
(config-if-atm-vc)# default bridge-dot1q encap <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 93 `；EOL ` RVA 0x336EC548 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-6cc3fd72cee77cf5](../../evidence/conditions-sets-042.md#c-6cc3fd72cee77cf5) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-e493cd2d5e9e8d4b](../../evidence/state_effects-sets-048.md#s-e493cd2d5e9e8d4b)

### static_slot_creation_candidates-003063

```text
(config-if-atm-vc)# default bridge-vlan <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 63 `；EOL ` RVA 0x336EE2E8 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-1877f4c405a64626](../../evidence/conditions-sets-010.md#c-1877f4c405a64626) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-e493cd2d5e9e8d4b](../../evidence/state_effects-sets-048.md#s-e493cd2d5e9e8d4b)

### static_slot_creation_candidates-003040

```text
(config-if-atm-vc)# default broadcast <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 27 `；EOL ` RVA 0x336F6130 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-127058859fbe8d5c](../../evidence/conditions-sets-007.md#c-127058859fbe8d5c) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-89be17b372d1b879](../../evidence/state_effects-sets-029.md#s-89be17b372d1b879)

### static_slot_creation_candidates-003046

```text
(config-if-atm-vc)# default cac_off <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 74 `；EOL ` RVA 0x336ED700 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-eac7ea8d9af2dc34](../../evidence/conditions-sets-091.md#c-eac7ea8d9af2dc34) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-e493cd2d5e9e8d4b](../../evidence/state_effects-sets-048.md#s-e493cd2d5e9e8d4b)

### static_slot_creation_candidates-003033

```text
(config-if-atm-vc)# default cbr <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 7 `；EOL ` RVA 0x336EB240 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-aaea431cd6e3b230](../../evidence/conditions-sets-066.md#c-aaea431cd6e3b230) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-e493cd2d5e9e8d4b](../../evidence/state_effects-sets-048.md#s-e493cd2d5e9e8d4b)

### static_slot_creation_candidates-003032

```text
(config-if-atm-vc)# default cdvt <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 82 `；EOL ` RVA 0x336EA740 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-977e300bb35710fd](../../evidence/conditions-sets-058.md#c-977e300bb35710fd) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-e493cd2d5e9e8d4b](../../evidence/state_effects-sets-048.md#s-e493cd2d5e9e8d4b)

### static_slot_creation_candidates-003103

```text
(config-if-atm-vc)# default class-vc <string> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 10 `；EOL ` RVA 0x336F6498 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` ATM vc-class name to use on this VC。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-68828ed599cf8d7d](../../evidence/conditions-sets-040.md#c-68828ed599cf8d7d) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-c166c02862c48f7d](../../evidence/parameters-sets-015.md#p-c166c02862c48f7d) · [状态效果 S-e493cd2d5e9e8d4b](../../evidence/state_effects-sets-048.md#s-e493cd2d5e9e8d4b)

### static_slot_creation_candidates-003114

```text
(config-if-atm-vc)# default dbs enable <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 69 `；EOL ` RVA 0x336F11F8 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-75ab2e5aea46c2a2](../../evidence/conditions-sets-046.md#c-75ab2e5aea46c2a2) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-e493cd2d5e9e8d4b](../../evidence/state_effects-sets-048.md#s-e493cd2d5e9e8d4b)

### static_slot_creation_candidates-003043

```text
(config-if-atm-vc)# default description <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 9 `；EOL ` RVA 0x336F67A8 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-59f7f49e88cdb275](../../evidence/conditions-sets-035.md#c-59f7f49e88cdb275) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-e493cd2d5e9e8d4b](../../evidence/state_effects-sets-048.md#s-e493cd2d5e9e8d4b)

### static_slot_creation_candidates-003052

```text
(config-if-atm-vc)# default encapsulation <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 12 `；EOL ` RVA 0x336EDA80 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-3b9a06b36b766da9](../../evidence/conditions-sets-023.md#c-3b9a06b36b766da9) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-e493cd2d5e9e8d4b](../../evidence/state_effects-sets-048.md#s-e493cd2d5e9e8d4b)

### static_slot_creation_candidates-003075

```text
(config-if-atm-vc)# default idle-timeout <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 26 `；EOL ` RVA 0x336F0948 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-66cd8ca46aaa9325](../../evidence/conditions-sets-040.md#c-66cd8ca46aaa9325) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-e493cd2d5e9e8d4b](../../evidence/state_effects-sets-048.md#s-e493cd2d5e9e8d4b)

### static_slot_creation_candidates-003109

```text
(config-if-atm-vc)# default ilmi manage <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 15 `；EOL ` RVA 0x336EF478 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-b678460327662671](../../evidence/conditions-sets-071.md#c-b678460327662671) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-e493cd2d5e9e8d4b](../../evidence/state_effects-sets-048.md#s-e493cd2d5e9e8d4b)

### static_slot_creation_candidates-003064

```text
(config-if-atm-vc)# default inarp <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 13 `；EOL ` RVA 0x336F5748 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-08f8b652a6c7a39f](../../evidence/conditions-sets-004.md#c-08f8b652a6c7a39f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-e493cd2d5e9e8d4b](../../evidence/state_effects-sets-048.md#s-e493cd2d5e9e8d4b)

### static_slot_creation_candidates-003069

```text
(config-if-atm-vc)# default ip <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 61 `；EOL ` RVA 0x336F5A60 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-0c894059423b5016](../../evidence/conditions-sets-005.md#c-0c894059423b5016) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-e493cd2d5e9e8d4b](../../evidence/state_effects-sets-048.md#s-e493cd2d5e9e8d4b)

### static_slot_creation_candidates-003050

```text
(config-if-atm-vc)# default max-reserved-bandwidth <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 66 `；EOL ` RVA 0x336F6ED8 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-a8008fa082c35685](../../evidence/conditions-sets-065.md#c-a8008fa082c35685) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-7d1f2ce185d964c4](../../evidence/state_effects-sets-027.md#s-7d1f2ce185d964c4)

### static_slot_creation_candidates-003060

```text
(config-if-atm-vc)# default mid <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 28 `；EOL ` RVA 0x336EF168 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-b678460327662671](../../evidence/conditions-sets-071.md#c-b678460327662671) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-e493cd2d5e9e8d4b](../../evidence/state_effects-sets-048.md#s-e493cd2d5e9e8d4b)

### static_slot_creation_candidates-003070

```text
(config-if-atm-vc)# default multiqueue <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 33 `；EOL ` RVA 0x336EFBA0 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-234430f941324352](../../evidence/conditions-sets-014.md#c-234430f941324352) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-e493cd2d5e9e8d4b](../../evidence/state_effects-sets-048.md#s-e493cd2d5e9e8d4b)

### static_slot_creation_candidates-003116

```text
(config-if-atm-vc)# default oam ais-rdi <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 23 `；EOL ` RVA 0x336F2518 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-f989cb5046e153a6](../../evidence/conditions-sets-096.md#c-f989cb5046e153a6) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-46dc23f892a33f6e](../../evidence/state_effects-sets-015.md#s-46dc23f892a33f6e)

### static_slot_creation_candidates-003118

```text
(config-if-atm-vc)# default oam retry <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 20 `；EOL ` RVA 0x336F20E0 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-ffa637a87d3188a2](../../evidence/conditions-sets-099.md#c-ffa637a87d3188a2) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-7aa12998e413f60a](../../evidence/state_effects-sets-026.md#s-7aa12998e413f60a)

### static_slot_creation_candidates-003130

```text
(config-if-atm-vc)# default oam retry cc end <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 21 `；EOL ` RVA 0x336F1C78 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-ed0abf0c9ada72e9](../../evidence/conditions-sets-092.md#c-ed0abf0c9ada72e9) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-4420ccd18156781b](../../evidence/state_effects-sets-015.md#s-4420ccd18156781b)

### static_slot_creation_candidates-003127

```text
(config-if-atm-vc)# default oam retry cc segment <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 22 `；EOL ` RVA 0x336F1840 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-ed0abf0c9ada72e9](../../evidence/conditions-sets-092.md#c-ed0abf0c9ada72e9) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-1aef008d3208a37b](../../evidence/state_effects-sets-006.md#s-1aef008d3208a37b)

### static_slot_creation_candidates-003082

```text
(config-if-atm-vc)# default oam-pvc <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 16 `；EOL ` RVA 0x336F3870 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-15c768a8bab1109a](../../evidence/conditions-sets-009.md#c-15c768a8bab1109a) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-5d8e0df8be9cb6ea](../../evidence/state_effects-sets-020.md#s-5d8e0df8be9cb6ea)

### static_slot_creation_candidates-003133

```text
(config-if-atm-vc)# default oam-pvc manage cc end <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 17 `；EOL ` RVA 0x336F3100 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-2e7654761a9362af](../../evidence/conditions-sets-018.md#c-2e7654761a9362af) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-934384907797cf4a](../../evidence/state_effects-sets-031.md#s-934384907797cf4a)

### static_slot_creation_candidates-003131

```text
(config-if-atm-vc)# default oam-pvc manage cc segment <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 18 `；EOL ` RVA 0x336F2A88 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-845c834db06aa063](../../evidence/conditions-sets-051.md#c-845c834db06aa063) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-f0798a6f082be35b](../../evidence/state_effects-sets-051.md#s-f0798a6f082be35b)

### static_slot_creation_candidates-003112

```text
(config-if-atm-vc)# default pppoe max-sessions <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 44 `；EOL ` RVA 0x336F0DB0 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-3f7bbe424ff654a6](../../evidence/conditions-sets-025.md#c-3f7bbe424ff654a6) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-e493cd2d5e9e8d4b](../../evidence/state_effects-sets-048.md#s-e493cd2d5e9e8d4b)

### static_slot_creation_candidates-003095

```text
(config-if-atm-vc)# default queue-depth low-latency <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 73 `；EOL ` RVA 0x336EA0D0 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-99a15bea043eaf19](../../evidence/conditions-sets-059.md#c-99a15bea043eaf19) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-e493cd2d5e9e8d4b](../../evidence/state_effects-sets-048.md#s-e493cd2d5e9e8d4b)

### static_slot_creation_candidates-003125

```text
(config-if-atm-vc)# default radius attribute nas-port-type <number:0..2147483647> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 84 `；EOL ` RVA 0x336F5E38 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` nas-port-type attribute value。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-802f55ea99278dcd](../../evidence/conditions-sets-050.md#c-802f55ea99278dcd) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-7a9af0ace2f705c1](../../evidence/parameters-sets-010.md#p-7a9af0ace2f705c1) · [状态效果 S-e493cd2d5e9e8d4b](../../evidence/state_effects-sets-048.md#s-e493cd2d5e9e8d4b)

### static_slot_creation_candidates-003076

```text
(config-if-atm-vc)# default rx-limit <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 62 `；EOL ` RVA 0x336F02A8 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-0572449c162ed3d7](../../evidence/conditions-sets-002.md#c-0572449c162ed3d7) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-e493cd2d5e9e8d4b](../../evidence/state_effects-sets-048.md#s-e493cd2d5e9e8d4b)

### static_slot_creation_candidates-003037

```text
(config-if-atm-vc)# default rx-speed <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 86 `；EOL ` RVA 0x336EC978 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-c44eecf0600f7603](../../evidence/conditions-sets-076.md#c-c44eecf0600f7603) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-e493cd2d5e9e8d4b](../../evidence/state_effects-sets-048.md#s-e493cd2d5e9e8d4b)

### static_slot_creation_candidates-003065

```text
(config-if-atm-vc)# default transmit-priority <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 30 `；EOL ` RVA 0x336EF7D8 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-abccc28064065794](../../evidence/conditions-sets-066.md#c-abccc28064065794) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-e493cd2d5e9e8d4b](../../evidence/state_effects-sets-048.md#s-e493cd2d5e9e8d4b)

### static_slot_creation_candidates-003072

```text
(config-if-atm-vc)# default tx-limit <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 90 `；EOL ` RVA 0x336EFEF8 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-9f41304d3c2bda7d](../../evidence/conditions-sets-062.md#c-9f41304d3c2bda7d) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-e493cd2d5e9e8d4b](../../evidence/state_effects-sets-048.md#s-e493cd2d5e9e8d4b)

### static_slot_creation_candidates-003079

```text
(config-if-atm-vc)# default tx-ring-limit <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 32 `；EOL ` RVA 0x336F0620 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-e7634201b206c386](../../evidence/conditions-sets-089.md#c-e7634201b206c386) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-e493cd2d5e9e8d4b](../../evidence/state_effects-sets-048.md#s-e493cd2d5e9e8d4b)

### static_slot_creation_candidates-003087

```text
(config-if-atm-vc)# default ubr <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 3 `；EOL ` RVA 0x336F4338 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-d50c79323d4b1584](../../evidence/conditions-sets-082.md#c-d50c79323d4b1584) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-e493cd2d5e9e8d4b](../../evidence/state_effects-sets-048.md#s-e493cd2d5e9e8d4b)

### static_slot_creation_candidates-003084

```text
(config-if-atm-vc)# default ubr+ <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 4 `；EOL ` RVA 0x336F3E88 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-77b28056ceaecbc5](../../evidence/conditions-sets-047.md#c-77b28056ceaecbc5) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-e493cd2d5e9e8d4b](../../evidence/state_effects-sets-048.md#s-e493cd2d5e9e8d4b)

### static_slot_creation_candidates-003088

```text
(config-if-atm-vc)# default vbr-nrt <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 5 `；EOL ` RVA 0x336EACA8 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-88cfadea63a186c8](../../evidence/conditions-sets-053.md#c-88cfadea63a186c8) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-e493cd2d5e9e8d4b](../../evidence/state_effects-sets-048.md#s-e493cd2d5e9e8d4b)

### static_slot_creation_candidates-003030

```text
(config-if-atm-vc)# default vbr-rt <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 6 `；EOL ` RVA 0x336EAAA0 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-ac8bfdfdeb07d194](../../evidence/conditions-sets-067.md#c-ac8bfdfdeb07d194) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-e493cd2d5e9e8d4b](../../evidence/state_effects-sets-048.md#s-e493cd2d5e9e8d4b)

### static_slot_creation_candidates-003093

```text
(config-if-atm-vc)# default vc-hold-queue <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 40 `；EOL ` RVA 0x336F5340 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-1fd9f135697766b7](../../evidence/conditions-sets-012.md#c-1fd9f135697766b7) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-e493cd2d5e9e8d4b](../../evidence/state_effects-sets-048.md#s-e493cd2d5e9e8d4b)

### static_slot_creation_candidates-003053

```text
(config-if-atm-vc)# default vcci <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 36 `；EOL ` RVA 0x336F6B08 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-bc17b5e01e599aed](../../evidence/conditions-sets-073.md#c-bc17b5e01e599aed) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-e493cd2d5e9e8d4b](../../evidence/state_effects-sets-048.md#s-e493cd2d5e9e8d4b)

### static_slot_creation_candidates-003035

```text
(config-if-atm-vc)# default weight <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 83 `；EOL ` RVA 0x336EB690 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-6bf8d1c66f5fad8a](../../evidence/conditions-sets-042.md#c-6bf8d1c66f5fad8a) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-e493cd2d5e9e8d4b](../../evidence/state_effects-sets-048.md#s-e493cd2d5e9e8d4b)

### static_slot_creation_candidates-003042

```text
(config-if-atm-vc)# description <string> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 9 `；EOL ` RVA 0x336F67A8 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` VC description upto 80 characters。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-b3a4f5609690cb5d](../../evidence/conditions-sets-069.md#c-b3a4f5609690cb5d) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-92398f8fe77776b7](../../evidence/parameters-sets-011.md#p-92398f8fe77776b7)

### static_slot_creation_candidates-003149

```text
(config-if-atm-vc)# encapsulation aal5mux <?protoname_action@555588c4b230> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 12 `；EOL ` RVA 0x336EDA80 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-bf4b0d5353afc3b6](../../evidence/conditions-sets-074.md#c-bf4b0d5353afc3b6) · [缺口 G-e17ab9020d85caa0](../../evidence/gaps-sets-008.md#g-e17ab9020d85caa0) · [状态效果 S-e1d6c4332f95c8d0](../../evidence/state_effects-sets-048.md#s-e1d6c4332f95c8d0)

### static_slot_creation_candidates-003152

```text
(config-if-atm-vc)# encapsulation aal5mux <?protoname_action@555588c4b230> frame-relay <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 12 `；EOL ` RVA 0x36D5F8A8 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[候选注册 R-0d08fc7eb5b97a71](../../evidence/conditional_registrations-sets-001.md#r-0d08fc7eb5b97a71) · [条件 C-68df164962200687](../../evidence/conditions-sets-041.md#c-68df164962200687) · [缺口 G-e17ab9020d85caa0](../../evidence/gaps-sets-008.md#g-e17ab9020d85caa0) · [状态效果 S-9244dea9711a32da](../../evidence/state_effects-sets-031.md#s-9244dea9711a32da)

### static_slot_creation_candidates-003055

```text
(config-if-atm-vc)# encapsulation aal5snap <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 12 `；EOL ` RVA 0x336EDA80 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-4876161e4471f91f](../../evidence/conditions-sets-028.md#c-4876161e4471f91f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-3c9e78ecb9141f31](../../evidence/state_effects-sets-013.md#s-3c9e78ecb9141f31)

### static_slot_creation_candidates-003078

```text
(config-if-atm-vc)# idle-timeout <number:0..2000000> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 26 `；EOL ` RVA 0x336F0948 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Idle timeout in seconds。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-965e58b61f08704e](../../evidence/conditions-sets-058.md#c-965e58b61f08704e) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-56d90eca87b816a8](../../evidence/parameters-sets-007.md#p-56d90eca87b816a8)

### static_slot_creation_candidates-003150

```text
(config-if-atm-vc)# idle-timeout <number:0..2000000> <number:dynamic> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 26 `；EOL ` RVA 0x336F0948 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Idle timeout in seconds；` unsigned_number_dynamic ` minimum traffic rate (Kbps) to keep the connection。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-a06e90ffb28835c3](../../evidence/conditions-sets-062.md#c-a06e90ffb28835c3) · [缺口 G-acd295282744284a](../../evidence/gaps-sets-006.md#g-acd295282744284a) · [参数 P-11980dc0a1a5dc17](../../evidence/parameters-sets-002.md#p-11980dc0a1a5dc17)

### static_slot_creation_candidates-003059

```text
(config-if-atm-vc)# ilmi manage <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 15 `；EOL ` RVA 0x336EF478 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-b678460327662671](../../evidence/conditions-sets-071.md#c-b678460327662671) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### static_slot_creation_candidates-003019

```text
(config-if-atm-vc)# inarp <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 13 `；EOL ` RVA 0x336F5748 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-08f8b652a6c7a39f](../../evidence/conditions-sets-004.md#c-08f8b652a6c7a39f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### static_slot_creation_candidates-003110

```text
(config-if-atm-vc)# ip addr inarp <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 61 `；EOL ` RVA 0x336F5A60 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-cbded4b9e0cb5e37](../../evidence/conditions-sets-078.md#c-cbded4b9e0cb5e37) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### static_slot_creation_candidates-003017

```text
(config-if-atm-vc)# max-reserved-bandwidth <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 66 `；EOL ` RVA 0x336F6ED8 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-a8008fa082c35685](../../evidence/conditions-sets-065.md#c-a8008fa082c35685) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-4ba49ff20ed06720](../../evidence/state_effects-sets-017.md#s-4ba49ff20ed06720)

### static_slot_creation_candidates-003018

```text
(config-if-atm-vc)# mid <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 28 `；EOL ` RVA 0x336EF168 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-b678460327662671](../../evidence/conditions-sets-071.md#c-b678460327662671) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### static_slot_creation_candidates-003020

```text
(config-if-atm-vc)# multiqueue <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 33 `；EOL ` RVA 0x336EFBA0 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-234430f941324352](../../evidence/conditions-sets-014.md#c-234430f941324352) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### static_slot_creation_candidates-003024

```text
(config-if-atm-vc)# no <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 35 `；EOL ` RVA 0x336F4FB8 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-fc8024a246166e79](../../evidence/conditions-sets-097.md#c-fc8024a246166e79) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-76878dfef4748c1a](../../evidence/state_effects-sets-025.md#s-76878dfef4748c1a)

### static_slot_creation_candidates-003105

```text
(config-if-atm-vc)# no aaa connect-info <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 87 `；EOL ` RVA 0x336EDE58 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-b9de8c3dbc12e0c5](../../evidence/conditions-sets-072.md#c-b9de8c3dbc12e0c5) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-76878dfef4748c1a](../../evidence/state_effects-sets-025.md#s-76878dfef4748c1a)

### static_slot_creation_candidates-003097

```text
(config-if-atm-vc)# no abr rate-factors <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 34 `；EOL ` RVA 0x336EBE00 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-5e7103e1f0db9ccb](../../evidence/conditions-sets-037.md#c-5e7103e1f0db9ccb) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-76878dfef4748c1a](../../evidence/state_effects-sets-025.md#s-76878dfef4748c1a)

### static_slot_creation_candidates-003102

```text
(config-if-atm-vc)# no ancp enable <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 89 `；EOL ` RVA 0x336ECDE8 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-a8ab938f4e1b862d](../../evidence/conditions-sets-065.md#c-a8ab938f4e1b862d) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-76878dfef4748c1a](../../evidence/state_effects-sets-025.md#s-76878dfef4748c1a)

### static_slot_creation_candidates-003135

```text
(config-if-atm-vc)# no ancp neighbor name <string> id <string> client-id <string> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 88 `；EOL ` RVA 0x336ED2E0 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Neighbor name；` string ` ANCP neighbor ID；` string ` ANCP client ID。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-9fb2210082abcac6](../../evidence/conditions-sets-062.md#c-9fb2210082abcac6) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-b8558c3e12071398](../../evidence/parameters-sets-014.md#p-b8558c3e12071398) · [状态效果 S-76878dfef4748c1a](../../evidence/state_effects-sets-025.md#s-76878dfef4748c1a)

### static_slot_creation_candidates-003054

```text
(config-if-atm-vc)# no bre-connect <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 64 `；EOL ` RVA 0x336EED30 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-0c7341dbc062f634](../../evidence/conditions-sets-005.md#c-0c7341dbc062f634) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-76878dfef4748c1a](../../evidence/state_effects-sets-025.md#s-76878dfef4748c1a)

### static_slot_creation_candidates-003096

```text
(config-if-atm-vc)# no bridge-dot1q encap <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 93 `；EOL ` RVA 0x336EC548 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-12827ddc6ba1e994](../../evidence/conditions-sets-007.md#c-12827ddc6ba1e994) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-76878dfef4748c1a](../../evidence/state_effects-sets-025.md#s-76878dfef4748c1a)

### static_slot_creation_candidates-003058

```text
(config-if-atm-vc)# no bridge-vlan <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 63 `；EOL ` RVA 0x336EE2E8 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-1877f4c405a64626](../../evidence/conditions-sets-010.md#c-1877f4c405a64626) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-76878dfef4748c1a](../../evidence/state_effects-sets-025.md#s-76878dfef4748c1a)

### static_slot_creation_candidates-003038

```text
(config-if-atm-vc)# no broadcast <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 27 `；EOL ` RVA 0x336F6130 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-127058859fbe8d5c](../../evidence/conditions-sets-007.md#c-127058859fbe8d5c) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-0192bca0bf045741](../../evidence/state_effects-sets-001.md#s-0192bca0bf045741)

### static_slot_creation_candidates-003044

```text
(config-if-atm-vc)# no cac_off <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 74 `；EOL ` RVA 0x336ED700 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-eac7ea8d9af2dc34](../../evidence/conditions-sets-091.md#c-eac7ea8d9af2dc34) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-76878dfef4748c1a](../../evidence/state_effects-sets-025.md#s-76878dfef4748c1a)

### static_slot_creation_candidates-003031

```text
(config-if-atm-vc)# no cbr <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 7 `；EOL ` RVA 0x336EB240 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-d020cf3daf433d43](../../evidence/conditions-sets-080.md#c-d020cf3daf433d43) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-76878dfef4748c1a](../../evidence/state_effects-sets-025.md#s-76878dfef4748c1a)

### static_slot_creation_candidates-003029

```text
(config-if-atm-vc)# no cdvt <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 82 `；EOL ` RVA 0x336EA740 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-adaa41dd967bffa2](../../evidence/conditions-sets-067.md#c-adaa41dd967bffa2) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-76878dfef4748c1a](../../evidence/state_effects-sets-025.md#s-76878dfef4748c1a)

### static_slot_creation_candidates-003100

```text
(config-if-atm-vc)# no class-vc <string> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 10 `；EOL ` RVA 0x336F6498 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` ATM vc-class name to use on this VC。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-68828ed599cf8d7d](../../evidence/conditions-sets-040.md#c-68828ed599cf8d7d) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-c166c02862c48f7d](../../evidence/parameters-sets-015.md#p-c166c02862c48f7d) · [状态效果 S-76878dfef4748c1a](../../evidence/state_effects-sets-025.md#s-76878dfef4748c1a)

### static_slot_creation_candidates-003113

```text
(config-if-atm-vc)# no dbs enable <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 69 `；EOL ` RVA 0x336F11F8 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-3f9004be45c64fe4](../../evidence/conditions-sets-025.md#c-3f9004be45c64fe4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-76878dfef4748c1a](../../evidence/state_effects-sets-025.md#s-76878dfef4748c1a)

### static_slot_creation_candidates-003041

```text
(config-if-atm-vc)# no description <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 9 `；EOL ` RVA 0x336F67A8 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-981dda7a8b8a3635](../../evidence/conditions-sets-059.md#c-981dda7a8b8a3635) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-76878dfef4748c1a](../../evidence/state_effects-sets-025.md#s-76878dfef4748c1a)

### static_slot_creation_candidates-003048

```text
(config-if-atm-vc)# no encapsulation <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 12 `；EOL ` RVA 0x336EDA80 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-f32d9bd02ed6ca22](../../evidence/conditions-sets-094.md#c-f32d9bd02ed6ca22) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-76878dfef4748c1a](../../evidence/state_effects-sets-025.md#s-76878dfef4748c1a)

### static_slot_creation_candidates-003073

```text
(config-if-atm-vc)# no idle-timeout <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 26 `；EOL ` RVA 0x336F0948 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-7f5c09c02f33f97c](../../evidence/conditions-sets-049.md#c-7f5c09c02f33f97c) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-76878dfef4748c1a](../../evidence/state_effects-sets-025.md#s-76878dfef4748c1a)

### static_slot_creation_candidates-003108

```text
(config-if-atm-vc)# no ilmi manage <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 15 `；EOL ` RVA 0x336EF478 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-b678460327662671](../../evidence/conditions-sets-071.md#c-b678460327662671) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-76878dfef4748c1a](../../evidence/state_effects-sets-025.md#s-76878dfef4748c1a)

### static_slot_creation_candidates-003061

```text
(config-if-atm-vc)# no inarp <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 13 `；EOL ` RVA 0x336F5748 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-08f8b652a6c7a39f](../../evidence/conditions-sets-004.md#c-08f8b652a6c7a39f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-76878dfef4748c1a](../../evidence/state_effects-sets-025.md#s-76878dfef4748c1a)

### static_slot_creation_candidates-003066

```text
(config-if-atm-vc)# no ip <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 61 `；EOL ` RVA 0x336F5A60 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-194635b98aaf8757](../../evidence/conditions-sets-010.md#c-194635b98aaf8757) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-76878dfef4748c1a](../../evidence/state_effects-sets-025.md#s-76878dfef4748c1a)

### static_slot_creation_candidates-003047

```text
(config-if-atm-vc)# no max-reserved-bandwidth <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 66 `；EOL ` RVA 0x336F6ED8 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-a8008fa082c35685](../../evidence/conditions-sets-065.md#c-a8008fa082c35685) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-261f53af58e77e4e](../../evidence/state_effects-sets-009.md#s-261f53af58e77e4e)

### static_slot_creation_candidates-003057

```text
(config-if-atm-vc)# no mid <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 28 `；EOL ` RVA 0x336EF168 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-b678460327662671](../../evidence/conditions-sets-071.md#c-b678460327662671) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-76878dfef4748c1a](../../evidence/state_effects-sets-025.md#s-76878dfef4748c1a)

### static_slot_creation_candidates-003067

```text
(config-if-atm-vc)# no multiqueue <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 33 `；EOL ` RVA 0x336EFBA0 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-234430f941324352](../../evidence/conditions-sets-014.md#c-234430f941324352) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-76878dfef4748c1a](../../evidence/state_effects-sets-025.md#s-76878dfef4748c1a)

### static_slot_creation_candidates-003115

```text
(config-if-atm-vc)# no oam ais-rdi <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 23 `；EOL ` RVA 0x336F2518 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-d4bb89139b5fc277](../../evidence/conditions-sets-082.md#c-d4bb89139b5fc277) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-52e1d4e8df7d26c7](../../evidence/state_effects-sets-018.md#s-52e1d4e8df7d26c7)

### static_slot_creation_candidates-003117

```text
(config-if-atm-vc)# no oam retry <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 20 `；EOL ` RVA 0x336F20E0 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-450e43e5fc7b2041](../../evidence/conditions-sets-027.md#c-450e43e5fc7b2041) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-5e78fba5482fda0e](../../evidence/state_effects-sets-020.md#s-5e78fba5482fda0e)

### static_slot_creation_candidates-003128

```text
(config-if-atm-vc)# no oam retry cc end <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 21 `；EOL ` RVA 0x336F1C78 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-ed0abf0c9ada72e9](../../evidence/conditions-sets-092.md#c-ed0abf0c9ada72e9) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-bf17aede7b8bd5a7](../../evidence/state_effects-sets-040.md#s-bf17aede7b8bd5a7)

### static_slot_creation_candidates-003126

```text
(config-if-atm-vc)# no oam retry cc segment <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 22 `；EOL ` RVA 0x336F1840 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-ed0abf0c9ada72e9](../../evidence/conditions-sets-092.md#c-ed0abf0c9ada72e9) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-e9506cc284e58c1e](../../evidence/state_effects-sets-049.md#s-e9506cc284e58c1e)

### static_slot_creation_candidates-003080

```text
(config-if-atm-vc)# no oam-pvc <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 16 `；EOL ` RVA 0x336F3870 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-15c768a8bab1109a](../../evidence/conditions-sets-009.md#c-15c768a8bab1109a) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-03f469eb3496809b](../../evidence/state_effects-sets-001.md#s-03f469eb3496809b)

### static_slot_creation_candidates-003132

```text
(config-if-atm-vc)# no oam-pvc manage cc end <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 17 `；EOL ` RVA 0x336F3100 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-2e7654761a9362af](../../evidence/conditions-sets-018.md#c-2e7654761a9362af) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-8aa2653f7d560694](../../evidence/state_effects-sets-029.md#s-8aa2653f7d560694)

### static_slot_creation_candidates-003129

```text
(config-if-atm-vc)# no oam-pvc manage cc segment <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 18 `；EOL ` RVA 0x336F2A88 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-845c834db06aa063](../../evidence/conditions-sets-051.md#c-845c834db06aa063) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-b69340d69ca8ee21](../../evidence/state_effects-sets-039.md#s-b69340d69ca8ee21)

### static_slot_creation_candidates-003111

```text
(config-if-atm-vc)# no pppoe max-sessions <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 44 `；EOL ` RVA 0x336F0DB0 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-bb2a7ccd22b7525e](../../evidence/conditions-sets-072.md#c-bb2a7ccd22b7525e) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-76878dfef4748c1a](../../evidence/state_effects-sets-025.md#s-76878dfef4748c1a)

### static_slot_creation_candidates-003094

```text
(config-if-atm-vc)# no queue-depth low-latency <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 73 `；EOL ` RVA 0x336EA0D0 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-99a15bea043eaf19](../../evidence/conditions-sets-059.md#c-99a15bea043eaf19) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-76878dfef4748c1a](../../evidence/state_effects-sets-025.md#s-76878dfef4748c1a)

### static_slot_creation_candidates-003124

```text
(config-if-atm-vc)# no radius attribute nas-port-type <number:0..2147483647> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 84 `；EOL ` RVA 0x336F5E38 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` nas-port-type attribute value。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-802f55ea99278dcd](../../evidence/conditions-sets-050.md#c-802f55ea99278dcd) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-7a9af0ace2f705c1](../../evidence/parameters-sets-010.md#p-7a9af0ace2f705c1) · [状态效果 S-76878dfef4748c1a](../../evidence/state_effects-sets-025.md#s-76878dfef4748c1a)

### static_slot_creation_candidates-003074

```text
(config-if-atm-vc)# no rx-limit <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 62 `；EOL ` RVA 0x336F02A8 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-0572449c162ed3d7](../../evidence/conditions-sets-002.md#c-0572449c162ed3d7) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-76878dfef4748c1a](../../evidence/state_effects-sets-025.md#s-76878dfef4748c1a)

### static_slot_creation_candidates-003036

```text
(config-if-atm-vc)# no rx-speed <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 86 `；EOL ` RVA 0x336EC978 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-b69af0f1be43a586](../../evidence/conditions-sets-071.md#c-b69af0f1be43a586) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-76878dfef4748c1a](../../evidence/state_effects-sets-025.md#s-76878dfef4748c1a)

### static_slot_creation_candidates-003062

```text
(config-if-atm-vc)# no transmit-priority <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 30 `；EOL ` RVA 0x336EF7D8 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-accf75a1f977b748](../../evidence/conditions-sets-067.md#c-accf75a1f977b748) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-76878dfef4748c1a](../../evidence/state_effects-sets-025.md#s-76878dfef4748c1a)

### static_slot_creation_candidates-003071

```text
(config-if-atm-vc)# no tx-limit <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 90 `；EOL ` RVA 0x336EFEF8 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-cc09026483f9fbb3](../../evidence/conditions-sets-079.md#c-cc09026483f9fbb3) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-76878dfef4748c1a](../../evidence/state_effects-sets-025.md#s-76878dfef4748c1a)

### static_slot_creation_candidates-003077

```text
(config-if-atm-vc)# no tx-ring-limit <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 32 `；EOL ` RVA 0x336F0620 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-e7634201b206c386](../../evidence/conditions-sets-089.md#c-e7634201b206c386) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-76878dfef4748c1a](../../evidence/state_effects-sets-025.md#s-76878dfef4748c1a)

### static_slot_creation_candidates-003085

```text
(config-if-atm-vc)# no ubr <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 3 `；EOL ` RVA 0x336F4338 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-27707cbeff25d6c6](../../evidence/conditions-sets-015.md#c-27707cbeff25d6c6) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-76878dfef4748c1a](../../evidence/state_effects-sets-025.md#s-76878dfef4748c1a)

### static_slot_creation_candidates-003081

```text
(config-if-atm-vc)# no ubr+ <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 4 `；EOL ` RVA 0x336F3E88 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-831cc207f0eb8a47](../../evidence/conditions-sets-051.md#c-831cc207f0eb8a47) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-76878dfef4748c1a](../../evidence/state_effects-sets-025.md#s-76878dfef4748c1a)

### static_slot_creation_candidates-003086

```text
(config-if-atm-vc)# no vbr-nrt <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 5 `；EOL ` RVA 0x336EACA8 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-117748d779a9419c](../../evidence/conditions-sets-007.md#c-117748d779a9419c) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-76878dfef4748c1a](../../evidence/state_effects-sets-025.md#s-76878dfef4748c1a)

### static_slot_creation_candidates-003028

```text
(config-if-atm-vc)# no vbr-rt <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 6 `；EOL ` RVA 0x336EAAA0 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-8aeac9d3ad7c2ec6](../../evidence/conditions-sets-054.md#c-8aeac9d3ad7c2ec6) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-76878dfef4748c1a](../../evidence/state_effects-sets-025.md#s-76878dfef4748c1a)

### static_slot_creation_candidates-003091

```text
(config-if-atm-vc)# no vc-hold-queue <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 40 `；EOL ` RVA 0x336F5340 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-9f67a0736cf26191](../../evidence/conditions-sets-062.md#c-9f67a0736cf26191) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-76878dfef4748c1a](../../evidence/state_effects-sets-025.md#s-76878dfef4748c1a)

### static_slot_creation_candidates-003049

```text
(config-if-atm-vc)# no vcci <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 36 `；EOL ` RVA 0x336F6B08 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-c7b7db1fec2d6336](../../evidence/conditions-sets-077.md#c-c7b7db1fec2d6336) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-76878dfef4748c1a](../../evidence/state_effects-sets-025.md#s-76878dfef4748c1a)

### static_slot_creation_candidates-003034

```text
(config-if-atm-vc)# no weight <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 83 `；EOL ` RVA 0x336EB690 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-13f1acd59614236e](../../evidence/conditions-sets-008.md#c-13f1acd59614236e) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-76878dfef4748c1a](../../evidence/state_effects-sets-025.md#s-76878dfef4748c1a)

### static_slot_creation_candidates-003089

```text
(config-if-atm-vc)# oam ais-rdi <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 23 `；EOL ` RVA 0x336F2518 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-42364211dfdbde8a](../../evidence/conditions-sets-026.md#c-42364211dfdbde8a) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-b1b4c8f9af3e459f](../../evidence/state_effects-sets-038.md#s-b1b4c8f9af3e459f)

### static_slot_creation_candidates-003090

```text
(config-if-atm-vc)# oam retry <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 20 `；EOL ` RVA 0x336F20E0 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-365885758fbbfd24](../../evidence/conditions-sets-021.md#c-365885758fbbfd24) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c7bb5154b25d9a00](../../evidence/state_effects-sets-042.md#s-c7bb5154b25d9a00)

### static_slot_creation_candidates-003121

```text
(config-if-atm-vc)# oam retry cc end <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 21 `；EOL ` RVA 0x336F1C78 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-ed0abf0c9ada72e9](../../evidence/conditions-sets-092.md#c-ed0abf0c9ada72e9) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-62868d0dc70c141a](../../evidence/state_effects-sets-021.md#s-62868d0dc70c141a)

### static_slot_creation_candidates-003120

```text
(config-if-atm-vc)# oam retry cc segment <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 22 `；EOL ` RVA 0x336F1840 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-ed0abf0c9ada72e9](../../evidence/conditions-sets-092.md#c-ed0abf0c9ada72e9) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-2251cfef1cca0cd9](../../evidence/state_effects-sets-008.md#s-2251cfef1cca0cd9)

### static_slot_creation_candidates-003023

```text
(config-if-atm-vc)# oam-pvc <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 16 `；EOL ` RVA 0x336F3870 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-15c768a8bab1109a](../../evidence/conditions-sets-009.md#c-15c768a8bab1109a) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-cd7627c3aa59c278](../../evidence/state_effects-sets-043.md#s-cd7627c3aa59c278)

### static_slot_creation_candidates-003123

```text
(config-if-atm-vc)# oam-pvc manage cc end <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 17 `；EOL ` RVA 0x336F3100 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-2e7654761a9362af](../../evidence/conditions-sets-018.md#c-2e7654761a9362af) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-973295dd2122f7fc](../../evidence/state_effects-sets-032.md#s-973295dd2122f7fc)

### static_slot_creation_candidates-003122

```text
(config-if-atm-vc)# oam-pvc manage cc segment <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 18 `；EOL ` RVA 0x336F2A88 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-845c834db06aa063](../../evidence/conditions-sets-051.md#c-845c834db06aa063) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-a08ae3826eb65545](../../evidence/state_effects-sets-034.md#s-a08ae3826eb65545)

### static_slot_creation_candidates-003151

```text
(config-if-atm-vc)# pppoe max-sessions <number:dynamic> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 44 `；EOL ` RVA 0x336F0DB0 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Maximum PPPOE sessions。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-41d45f407aa095f6](../../evidence/conditions-sets-026.md#c-41d45f407aa095f6) · [缺口 G-66eede1253db906a](../../evidence/gaps-sets-004.md#g-66eede1253db906a) · [参数 P-35735a7f93c18b79](../../evidence/parameters-sets-005.md#p-35735a7f93c18b79)

### static_slot_creation_candidates-003141

```text
(config-if-atm-vc)# protocol <?protoaddr_inarp_action@555588c6ee10> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 11 `；EOL ` RVA 0x3371AF70 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-8c9fcc9da58a7c40](../../evidence/conditions-sets-054.md#c-8c9fcc9da58a7c40) · [缺口 G-8639c3575ef6bfc8](../../evidence/gaps-sets-005.md#g-8639c3575ef6bfc8)

### static_slot_creation_candidates-003153

```text
(config-if-atm-vc)# queue-depth <number:dynamic> <number:dynamic> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 72 `；EOL ` RVA 0x336EA390 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` queue depth high watermark, in cells；` unsigned_number_dynamic ` queue depth low watermark, in cells。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-76dba6f7789b0bec](../../evidence/conditions-sets-046.md#c-76dba6f7789b0bec) · [缺口 G-c7fe79a7f87f8ee8](../../evidence/gaps-sets-007.md#g-c7fe79a7f87f8ee8) · [参数 P-8cb9f3ff6881b084](../../evidence/parameters-sets-011.md#p-8cb9f3ff6881b084)

### static_slot_creation_candidates-003027

```text
(config-if-atm-vc)# queue-depth low-latency <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 73 `；EOL ` RVA 0x336EA0D0 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-99a15bea043eaf19](../../evidence/conditions-sets-059.md#c-99a15bea043eaf19) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### static_slot_creation_candidates-003119

```text
(config-if-atm-vc)# radius attribute nas-port-type <number:0..2147483647> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 84 `；EOL ` RVA 0x336F5E38 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` nas-port-type attribute value。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-802f55ea99278dcd](../../evidence/conditions-sets-050.md#c-802f55ea99278dcd) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-7a9af0ace2f705c1](../../evidence/parameters-sets-010.md#p-7a9af0ace2f705c1)

### static_slot_creation_candidates-003021

```text
(config-if-atm-vc)# rx-limit <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 62 `；EOL ` RVA 0x336F02A8 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-0572449c162ed3d7](../../evidence/conditions-sets-002.md#c-0572449c162ed3d7) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### static_slot_creation_candidates-003140

```text
(config-if-atm-vc)# rx-speed <number:dynamic> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 86 `；EOL ` RVA 0x336EC978 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Incoming Cell Rate for L2TP AVP 38 in Kbps。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-66552cf9de616d09](../../evidence/conditions-sets-040.md#c-66552cf9de616d09) · [缺口 G-599015bc050a37aa](../../evidence/gaps-sets-004.md#g-599015bc050a37aa) · [参数 P-aad5e53adcb57881](../../evidence/parameters-sets-013.md#p-aad5e53adcb57881)

### static_slot_creation_candidates-003158

```text
(config-if-atm-vc)# service-policy input <string> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 37 `；EOL ` RVA 0x336F4AD0 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Policy-map name。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-20aa515106e2710c](../../evidence/conditions-sets-013.md#c-20aa515106e2710c) · [缺口 G-f06c3a4a9fca4126](../../evidence/gaps-sets-008.md#g-f06c3a4a9fca4126) · [参数 P-5589ec0b4a64e290](../../evidence/parameters-sets-007.md#p-5589ec0b4a64e290) · [状态效果 S-6a44130c0efbf2e0](../../evidence/state_effects-sets-023.md#s-6a44130c0efbf2e0)

### static_slot_creation_candidates-003068

```text
(config-if-atm-vc)# transmit-priority <number:1..4> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 30 `；EOL ` RVA 0x336EF7D8 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` priority level。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-7b5383a0b2bd9782](../../evidence/conditions-sets-048.md#c-7b5383a0b2bd9782) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-2274bd91d9986225](../../evidence/parameters-sets-003.md#p-2274bd91d9986225)

### static_slot_creation_candidates-003144

```text
(config-if-atm-vc)# transmit-priority <number:dynamic> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 30 `；EOL ` RVA 0x336EF7D8 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` priority level。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-bd5e7f6efcfedd40](../../evidence/conditions-sets-073.md#c-bd5e7f6efcfedd40) · [缺口 G-bfc4f3a1e93398cf](../../evidence/gaps-sets-007.md#g-bfc4f3a1e93398cf) · [参数 P-d054770189636d67](../../evidence/parameters-sets-016.md#p-d054770189636d67)

### static_slot_creation_candidates-003145

```text
(config-if-atm-vc)# tx-limit <number:dynamic> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 90 `；EOL ` RVA 0x336EFEF8 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Number of tx buffers for this VC。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-2fe641e5adefa076](../../evidence/conditions-sets-019.md#c-2fe641e5adefa076) · [缺口 G-b3fc18415150dc09](../../evidence/gaps-sets-006.md#g-b3fc18415150dc09) · [参数 P-a3f44a4236739092](../../evidence/parameters-sets-012.md#p-a3f44a4236739092)

### static_slot_creation_candidates-003022

```text
(config-if-atm-vc)# tx-ring-limit <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 32 `；EOL ` RVA 0x336F0620 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-e7634201b206c386](../../evidence/conditions-sets-089.md#c-e7634201b206c386) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### static_slot_creation_candidates-003146

```text
(config-if-atm-vc)# tx-ring-limit <number:dynamic> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 32 `；EOL ` RVA 0x336F0620 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Number (ring limit)。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-7f4551358f2f46d8](../../evidence/conditions-sets-049.md#c-7f4551358f2f46d8) · [缺口 G-eccee1cfa8eeafaa](../../evidence/gaps-sets-008.md#g-eccee1cfa8eeafaa) · [参数 P-7a8172f5b154ea39](../../evidence/parameters-sets-010.md#p-7a8172f5b154ea39)

### static_slot_creation_candidates-003026

```text
(config-if-atm-vc)# ubr <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 3 `；EOL ` RVA 0x336F4338 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-fa9e38f7b937105f](../../evidence/conditions-sets-097.md#c-fa9e38f7b937105f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### static_slot_creation_candidates-003147

```text
(config-if-atm-vc)# ubr <number:dynamic> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 3 `；EOL ` RVA 0x336F4338 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Peak Cell Rate (PCR) in Kbps。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-064ddae9df364d47](../../evidence/conditions-sets-003.md#c-064ddae9df364d47) · [缺口 G-901b5fa5cc32bc30](../../evidence/gaps-sets-005.md#g-901b5fa5cc32bc30) · [参数 P-5b27580cdf48c1b0](../../evidence/parameters-sets-007.md#p-5b27580cdf48c1b0)

### static_slot_creation_candidates-003156

```text
(config-if-atm-vc)# ubr+ <number:dynamic> <number:dynamic> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 4 `；EOL ` RVA 0x336F3E88 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Peak Cell Rate(PCR) in Kbps；` unsigned_number_dynamic ` Minimum Guaranteed Cell Rate(MCR) in Kbps。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-63a740055076f55e](../../evidence/conditions-sets-039.md#c-63a740055076f55e) · [缺口 G-842557e22305bfa9](../../evidence/gaps-sets-005.md#g-842557e22305bfa9) · [参数 P-f78839e146c520ee](../../evidence/parameters-sets-018.md#p-f78839e146c520ee)

### static_slot_creation_candidates-003157

```text
(config-if-atm-vc)# vbr-nrt <number:dynamic> <number:dynamic> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 5 `；EOL ` RVA 0x336EACA8 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Peak Cell Rate(PCR) in Kbps；` unsigned_number_dynamic ` Sustainable Cell Rate(SCR) in Kbps。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-36f68820432a2c0d](../../evidence/conditions-sets-021.md#c-36f68820432a2c0d) · [缺口 G-0ae29b2ed06e8d68](../../evidence/gaps-sets-001.md#g-0ae29b2ed06e8d68) · [参数 P-f2b8288aa0b463a9](../../evidence/parameters-sets-018.md#p-f2b8288aa0b463a9)

### static_slot_creation_candidates-003154

```text
(config-if-atm-vc)# vbr-rt <number:dynamic> <number:dynamic> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 6 `；EOL ` RVA 0x336EAAA0 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Peak Cell Rate(PCR) in Kbps；` unsigned_number_dynamic ` Average Cell Rate in Kbps。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-5ce7c4f065ba8978](../../evidence/conditions-sets-036.md#c-5ce7c4f065ba8978) · [缺口 G-f1251e6ff68e0f9d](../../evidence/gaps-sets-008.md#g-f1251e6ff68e0f9d) · [参数 P-6ebcb04a8f2708a1](../../evidence/parameters-sets-009.md#p-6ebcb04a8f2708a1)

### static_slot_creation_candidates-003092

```text
(config-if-atm-vc)# vc-hold-queue <number:5..2048> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 40 `；EOL ` RVA 0x336F5340 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Value of the hold queue size。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-ff5f365a1d3f36c2](../../evidence/conditions-sets-098.md#c-ff5f365a1d3f36c2) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-40145c168d3b6216](../../evidence/parameters-sets-005.md#p-40145c168d3b6216)

### static_slot_creation_candidates-003051

```text
(config-if-atm-vc)# vcci <number:0..32767> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 36 `；EOL ` RVA 0x336F6B08 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` VCCI value。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-3be4f9e9e175ad33](../../evidence/conditions-sets-023.md#c-3be4f9e9e175ad33) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-4cf62c48b27982bf](../../evidence/parameters-sets-006.md#p-4cf62c48b27982bf)

### static_slot_creation_candidates-003138

```text
(config-if-atm-vc)# weight <number:dynamic> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 83 `；EOL ` RVA 0x336EB690 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` &lt;Range&gt;。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-57e80ede789eb358](../../evidence/conditions-sets-034.md#c-57e80ede789eb358) · [缺口 G-b4877f857e9ae82a](../../evidence/gaps-sets-006.md#g-b4877f857e9ae82a) · [参数 P-93f5f207bda12e57](../../evidence/parameters-sets-011.md#p-93f5f207bda12e57)

### static_slot_creation_candidates-003014

```text
(config-if-atm-vc)# <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 35 `；EOL ` RVA 0x336F4FB8 `。

模式根 ` RVA 0x336E9BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-e0615d8318d9de25](../../evidence/conditional_registrations-sets-002.md#r-e0615d8318d9de25) · [条件 C-fc8024a246166e79](../../evidence/conditions-sets-097.md#c-fc8024a246166e79) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

