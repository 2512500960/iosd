# atm-range-pvc-config · 依赖静态建槽的条件安装

[模式索引](README.md) · [总索引](../../README.md)

### static_slot_creation_candidates-003411

```text
(cfg-if-atm-range-pvc)# aaa connect-info <string> <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 87 `；EOL ` RVA 0x343E7678 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` connect-info。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-3d37d2b7bf29af15](../../evidence/conditions-sets-024.md#c-3d37d2b7bf29af15) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-5ceda37581212584](../../evidence/parameters-sets-007.md#p-5ceda37581212584)

### static_slot_creation_candidates-003434

```text
(cfg-if-atm-range-pvc)# abr <number:dynamic> <number:dynamic> <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 8 `；EOL ` RVA 0x343EB008 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Peak Cell Rate(PCR) in Kbps；` unsigned_number_dynamic ` Minimum Cell Rate(MCR) in Kbps。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-ef783a56e756ed7b](../../evidence/conditions-sets-092.md#c-ef783a56e756ed7b) · [缺口 G-d99bab25d565634d](../../evidence/gaps-sets-008.md#g-d99bab25d565634d) · [参数 P-610711ed6485e79e](../../evidence/parameters-sets-008.md#p-610711ed6485e79e)

### static_slot_creation_candidates-003417

```text
(cfg-if-atm-range-pvc)# ancp neighbor name <string> id <string> client-id <string> <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 88 `；EOL ` RVA 0x343E6C70 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Neighbor name；` string ` ANCP neighbor ID；` string ` ANCP client ID。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-130c925a782eb748](../../evidence/conditions-sets-008.md#c-130c925a782eb748) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-b6abb5e67b0c6e8f](../../evidence/parameters-sets-014.md#p-b6abb5e67b0c6e8f)

### static_slot_creation_candidates-003426

```text
(cfg-if-atm-range-pvc)# bridge-vlan <number:dynamic> <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 63 `；EOL ` RVA 0x343E9B30 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Bridge domain number。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-ae1635337150a124](../../evidence/conditions-sets-067.md#c-ae1635337150a124) · [缺口 G-58a9cae368e5a76f](../../evidence/gaps-sets-004.md#g-58a9cae368e5a76f) · [参数 P-8bc03e9642690283](../../evidence/parameters-sets-011.md#p-8bc03e9642690283)

### static_slot_creation_candidates-003358

```text
(cfg-if-atm-range-pvc)# broadcast <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 27 `；EOL ` RVA 0x343E7278 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-86f999120b1782d4](../../evidence/conditions-sets-052.md#c-86f999120b1782d4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-a678c350bf1c4f5c](../../evidence/state_effects-sets-035.md#s-a678c350bf1c4f5c)

### static_slot_creation_candidates-003428

```text
(cfg-if-atm-range-pvc)# cbr <number:dynamic> <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 7 `；EOL ` RVA 0x343EB7A8 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Peak Cell Rate in Kbps。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-ca57fc083eb19854](../../evidence/conditions-sets-078.md#c-ca57fc083eb19854) · [缺口 G-d174eead9ae2264d](../../evidence/gaps-sets-007.md#g-d174eead9ae2264d) · [参数 P-2bb873ff11c5c79c](../../evidence/parameters-sets-004.md#p-2bb873ff11c5c79c)

### static_slot_creation_candidates-003420

```text
(cfg-if-atm-range-pvc)# cdvt <number:dynamic> <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 82 `；EOL ` RVA 0x343E5838 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` CDVT in units of tenths of a microsecond。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-e58e3ccd3c4691fb](../../evidence/conditions-sets-089.md#c-e58e3ccd3c4691fb) · [缺口 G-b52a4e4c99327d60](../../evidence/gaps-sets-006.md#g-b52a4e4c99327d60) · [参数 P-74c93ee1177c7f00](../../evidence/parameters-sets-009.md#p-74c93ee1177c7f00)

### static_slot_creation_candidates-003373

```text
(cfg-if-atm-range-pvc)# class-vc <string> <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 10 `；EOL ` RVA 0x343E6FF8 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` ATM vc-class name to use on this pvc in range。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-86f999120b1782d4](../../evidence/conditions-sets-052.md#c-86f999120b1782d4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-7b80e9a4ca80845e](../../evidence/parameters-sets-010.md#p-7b80e9a4ca80845e)

### static_slot_creation_candidates-003389

```text
(cfg-if-atm-range-pvc)# dbs enable <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 69 `；EOL ` RVA 0x343E8350 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-14e789ad61f20d85](../../evidence/conditions-sets-008.md#c-14e789ad61f20d85) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-22533a40eb4fd1ed](../../evidence/state_effects-sets-008.md#s-22533a40eb4fd1ed)

### static_slot_creation_candidates-003412

```text
(cfg-if-atm-range-pvc)# default aaa connect-info <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 87 `；EOL ` RVA 0x343E7678 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-e11d5830d9c21022](../../evidence/conditions-sets-087.md#c-e11d5830d9c21022) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-3d7f4656a6ab5b16](../../evidence/state_effects-sets-013.md#s-3d7f4656a6ab5b16)

### static_slot_creation_candidates-003419

```text
(cfg-if-atm-range-pvc)# default ancp neighbor name <string> id <string> client-id <string> <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 88 `；EOL ` RVA 0x343E6C70 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Neighbor name；` string ` ANCP neighbor ID；` string ` ANCP client ID。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-dc7d7de2bcbb427e](../../evidence/conditions-sets-085.md#c-dc7d7de2bcbb427e) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-b6abb5e67b0c6e8f](../../evidence/parameters-sets-014.md#p-b6abb5e67b0c6e8f) · [状态效果 S-3d7f4656a6ab5b16](../../evidence/state_effects-sets-013.md#s-3d7f4656a6ab5b16)

### static_slot_creation_candidates-003398

```text
(cfg-if-atm-range-pvc)# default bridge-vlan <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 63 `；EOL ` RVA 0x343E9B30 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-a131514bb855bf0b](../../evidence/conditions-sets-062.md#c-a131514bb855bf0b) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-3d7f4656a6ab5b16](../../evidence/state_effects-sets-013.md#s-3d7f4656a6ab5b16)

### static_slot_creation_candidates-003374

```text
(cfg-if-atm-range-pvc)# default broadcast <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 27 `；EOL ` RVA 0x343E7278 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-86f999120b1782d4](../../evidence/conditions-sets-052.md#c-86f999120b1782d4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-95264849a1de0a83](../../evidence/state_effects-sets-032.md#s-95264849a1de0a83)

### static_slot_creation_candidates-003403

```text
(cfg-if-atm-range-pvc)# default cbr <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 7 `；EOL ` RVA 0x343EB7A8 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-cedc84b8f518d45b](../../evidence/conditions-sets-080.md#c-cedc84b8f518d45b) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-3d7f4656a6ab5b16](../../evidence/state_effects-sets-013.md#s-3d7f4656a6ab5b16)

### static_slot_creation_candidates-003366

```text
(cfg-if-atm-range-pvc)# default cdvt <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 82 `；EOL ` RVA 0x343E5838 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-a1f2a4e8398a4d64](../../evidence/conditions-sets-063.md#c-a1f2a4e8398a4d64) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-3d7f4656a6ab5b16](../../evidence/state_effects-sets-013.md#s-3d7f4656a6ab5b16)

### static_slot_creation_candidates-003407

```text
(cfg-if-atm-range-pvc)# default class-vc <string> <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 10 `；EOL ` RVA 0x343E6FF8 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` ATM vc-class name to use on this pvc in range。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-86f999120b1782d4](../../evidence/conditions-sets-052.md#c-86f999120b1782d4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-7b80e9a4ca80845e](../../evidence/parameters-sets-010.md#p-7b80e9a4ca80845e) · [状态效果 S-3d7f4656a6ab5b16](../../evidence/state_effects-sets-013.md#s-3d7f4656a6ab5b16)

### static_slot_creation_candidates-003414

```text
(cfg-if-atm-range-pvc)# default dbs enable <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 69 `；EOL ` RVA 0x343E8350 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-71ead158a583cca4](../../evidence/conditions-sets-044.md#c-71ead158a583cca4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-3d7f4656a6ab5b16](../../evidence/state_effects-sets-013.md#s-3d7f4656a6ab5b16)

### static_slot_creation_candidates-003379

```text
(cfg-if-atm-range-pvc)# default encapsulation <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 12 `；EOL ` RVA 0x343E79D8 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-3095efd9cd4ba860](../../evidence/conditions-sets-019.md#c-3095efd9cd4ba860) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-3d7f4656a6ab5b16](../../evidence/state_effects-sets-013.md#s-3d7f4656a6ab5b16)

### static_slot_creation_candidates-003386

```text
(cfg-if-atm-range-pvc)# default idle-timeout <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 26 `；EOL ` RVA 0x343E93B8 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-cb86cd48417ad2b1](../../evidence/conditions-sets-078.md#c-cb86cd48417ad2b1) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-3d7f4656a6ab5b16](../../evidence/state_effects-sets-013.md#s-3d7f4656a6ab5b16)

### static_slot_creation_candidates-003410

```text
(cfg-if-atm-range-pvc)# default ilmi manage <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 15 `；EOL ` RVA 0x343E7FB0 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-86f999120b1782d4](../../evidence/conditions-sets-052.md#c-86f999120b1782d4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-3d7f4656a6ab5b16](../../evidence/state_effects-sets-013.md#s-3d7f4656a6ab5b16)

### static_slot_creation_candidates-003378

```text
(cfg-if-atm-range-pvc)# default inarp <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 13 `；EOL ` RVA 0x343E7CC0 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-86f999120b1782d4](../../evidence/conditions-sets-052.md#c-86f999120b1782d4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-3d7f4656a6ab5b16](../../evidence/state_effects-sets-013.md#s-3d7f4656a6ab5b16)

### static_slot_creation_candidates-003416

```text
(cfg-if-atm-range-pvc)# default oam retry <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 20 `；EOL ` RVA 0x343E8860 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-99eb777fa224e0f5](../../evidence/conditions-sets-059.md#c-99eb777fa224e0f5) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-43cdad6e5216dea4](../../evidence/state_effects-sets-015.md#s-43cdad6e5216dea4)

### static_slot_creation_candidates-003387

```text
(cfg-if-atm-range-pvc)# default oam-pvc <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 16 `；EOL ` RVA 0x343E9020 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-86f999120b1782d4](../../evidence/conditions-sets-052.md#c-86f999120b1782d4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-0dbc2fc60ed789a7](../../evidence/state_effects-sets-003.md#s-0dbc2fc60ed789a7)

### static_slot_creation_candidates-003405

```text
(cfg-if-atm-range-pvc)# default pppoe max-sessions <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 44 `；EOL ` RVA 0x343E66A8 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-c9d35995b4d99c39](../../evidence/conditions-sets-078.md#c-c9d35995b4d99c39) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-3d7f4656a6ab5b16](../../evidence/state_effects-sets-013.md#s-3d7f4656a6ab5b16)

### static_slot_creation_candidates-003371

```text
(cfg-if-atm-range-pvc)# default queue-depth <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 72 `；EOL ` RVA 0x343E5F68 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-d0e3325f461f712b](../../evidence/conditions-sets-080.md#c-d0e3325f461f712b) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-3d7f4656a6ab5b16](../../evidence/state_effects-sets-013.md#s-3d7f4656a6ab5b16)

### static_slot_creation_candidates-003368

```text
(cfg-if-atm-range-pvc)# default rx-speed <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 86 `；EOL ` RVA 0x343E62D8 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-72e8c0c0404d593b](../../evidence/conditions-sets-044.md#c-72e8c0c0404d593b) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-3d7f4656a6ab5b16](../../evidence/state_effects-sets-013.md#s-3d7f4656a6ab5b16)

### static_slot_creation_candidates-003385

```text
(cfg-if-atm-range-pvc)# default shutdown <cr>
```

Handler ` RVA 0xECE8380 `；selector ` 0 `；EOL ` RVA 0x343E96C8 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-86f999120b1782d4](../../evidence/conditions-sets-052.md#c-86f999120b1782d4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-3d7f4656a6ab5b16](../../evidence/state_effects-sets-013.md#s-3d7f4656a6ab5b16)

### static_slot_creation_candidates-003388

```text
(cfg-if-atm-range-pvc)# default tx-ring-limit <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 32 `；EOL ` RVA 0x343E8C68 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-f4bf94c83cc75836](../../evidence/conditions-sets-094.md#c-f4bf94c83cc75836) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-3d7f4656a6ab5b16](../../evidence/state_effects-sets-013.md#s-3d7f4656a6ab5b16)

### static_slot_creation_candidates-003396

```text
(cfg-if-atm-range-pvc)# default ubr <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 3 `；EOL ` RVA 0x343EA7F0 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-8605bbef55d18258](../../evidence/conditions-sets-052.md#c-8605bbef55d18258) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-3d7f4656a6ab5b16](../../evidence/state_effects-sets-013.md#s-3d7f4656a6ab5b16)

### static_slot_creation_candidates-003393

```text
(cfg-if-atm-range-pvc)# default ubr+ <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 4 `；EOL ` RVA 0x343EA410 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-9e243ddbd60c1140](../../evidence/conditions-sets-061.md#c-9e243ddbd60c1140) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-3d7f4656a6ab5b16](../../evidence/state_effects-sets-013.md#s-3d7f4656a6ab5b16)

### static_slot_creation_candidates-003399

```text
(cfg-if-atm-range-pvc)# default vbr-nrt <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 5 `；EOL ` RVA 0x343EABC8 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-4f9e7af1176c8f00](../../evidence/conditions-sets-031.md#c-4f9e7af1176c8f00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-3d7f4656a6ab5b16](../../evidence/state_effects-sets-013.md#s-3d7f4656a6ab5b16)

### static_slot_creation_candidates-003401

```text
(cfg-if-atm-range-pvc)# default vbr-rt <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 6 `；EOL ` RVA 0x343EB378 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-fb5e496e6d8759ed](../../evidence/conditions-sets-097.md#c-fb5e496e6d8759ed) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-3d7f4656a6ab5b16](../../evidence/state_effects-sets-013.md#s-3d7f4656a6ab5b16)

### static_slot_creation_candidates-003369

```text
(cfg-if-atm-range-pvc)# default weight <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 83 `；EOL ` RVA 0x343E5BC8 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-104764f707d569a3](../../evidence/conditions-sets-006.md#c-104764f707d569a3) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-3d7f4656a6ab5b16](../../evidence/state_effects-sets-013.md#s-3d7f4656a6ab5b16)

### static_slot_creation_candidates-003430

```text
(cfg-if-atm-range-pvc)# encapsulation aal5mux <?protoname_action@5555899422d0> <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 12 `；EOL ` RVA 0x343E79D8 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-f7ff7d3d7bb9131f](../../evidence/conditions-sets-096.md#c-f7ff7d3d7bb9131f) · [缺口 G-29ab4a3e305f2917](../../evidence/gaps-sets-002.md#g-29ab4a3e305f2917) · [状态效果 S-21c6cec8db3e2da9](../../evidence/state_effects-sets-008.md#s-21c6cec8db3e2da9)

### static_slot_creation_candidates-003380

```text
(cfg-if-atm-range-pvc)# encapsulation aal5snap <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 12 `；EOL ` RVA 0x343E79D8 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-d73ee5d48e406d06](../../evidence/conditions-sets-083.md#c-d73ee5d48e406d06) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-1c2ad9241bcd13a3](../../evidence/state_effects-sets-006.md#s-1c2ad9241bcd13a3)

### static_slot_creation_candidates-003390

```text
(cfg-if-atm-range-pvc)# idle-timeout <number:0..2000000> <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 26 `；EOL ` RVA 0x343E93B8 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Idle timeout in seconds。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-f92fdd6cbaa151e5](../../evidence/conditions-sets-096.md#c-f92fdd6cbaa151e5) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-130dfa703f4335e8](../../evidence/parameters-sets-002.md#p-130dfa703f4335e8)

### static_slot_creation_candidates-003431

```text
(cfg-if-atm-range-pvc)# idle-timeout <number:0..2000000> <number:dynamic> <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 26 `；EOL ` RVA 0x343E93B8 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Idle timeout in seconds；` unsigned_number_dynamic ` minimum traffic rate (Kbps) to keep the connection。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-bdee6662b2c2cc34](../../evidence/conditions-sets-073.md#c-bdee6662b2c2cc34) · [缺口 G-3a6d9f3d6acc40a4](../../evidence/gaps-sets-003.md#g-3a6d9f3d6acc40a4) · [参数 P-cf56ccac017b055e](../../evidence/parameters-sets-016.md#p-cf56ccac017b055e)

### static_slot_creation_candidates-003377

```text
(cfg-if-atm-range-pvc)# ilmi manage <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 15 `；EOL ` RVA 0x343E7FB0 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-86f999120b1782d4](../../evidence/conditions-sets-052.md#c-86f999120b1782d4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### static_slot_creation_candidates-003359

```text
(cfg-if-atm-range-pvc)# inarp <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 13 `；EOL ` RVA 0x343E7CC0 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-86f999120b1782d4](../../evidence/conditions-sets-052.md#c-86f999120b1782d4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### static_slot_creation_candidates-003409

```text
(cfg-if-atm-range-pvc)# no aaa connect-info <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 87 `；EOL ` RVA 0x343E7678 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-4cd746b1e270ab3b](../../evidence/conditions-sets-030.md#c-4cd746b1e270ab3b) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c201ef8ce993d96f](../../evidence/state_effects-sets-041.md#s-c201ef8ce993d96f)

### static_slot_creation_candidates-003418

```text
(cfg-if-atm-range-pvc)# no ancp neighbor name <string> id <string> client-id <string> <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 88 `；EOL ` RVA 0x343E6C70 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Neighbor name；` string ` ANCP neighbor ID；` string ` ANCP client ID。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-d5bab24c5ed0af6c](../../evidence/conditions-sets-082.md#c-d5bab24c5ed0af6c) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-b6abb5e67b0c6e8f](../../evidence/parameters-sets-014.md#p-b6abb5e67b0c6e8f) · [状态效果 S-c201ef8ce993d96f](../../evidence/state_effects-sets-041.md#s-c201ef8ce993d96f)

### static_slot_creation_candidates-003395

```text
(cfg-if-atm-range-pvc)# no bridge-vlan <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 63 `；EOL ` RVA 0x343E9B30 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-a131514bb855bf0b](../../evidence/conditions-sets-062.md#c-a131514bb855bf0b) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c201ef8ce993d96f](../../evidence/state_effects-sets-041.md#s-c201ef8ce993d96f)

### static_slot_creation_candidates-003372

```text
(cfg-if-atm-range-pvc)# no broadcast <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 27 `；EOL ` RVA 0x343E7278 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-86f999120b1782d4](../../evidence/conditions-sets-052.md#c-86f999120b1782d4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-cc1303ec36a8648e](../../evidence/state_effects-sets-043.md#s-cc1303ec36a8648e)

### static_slot_creation_candidates-003402

```text
(cfg-if-atm-range-pvc)# no cbr <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 7 `；EOL ` RVA 0x343EB7A8 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-3721580da7ce1507](../../evidence/conditions-sets-021.md#c-3721580da7ce1507) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c201ef8ce993d96f](../../evidence/state_effects-sets-041.md#s-c201ef8ce993d96f)

### static_slot_creation_candidates-003364

```text
(cfg-if-atm-range-pvc)# no cdvt <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 82 `；EOL ` RVA 0x343E5838 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-fdb589a1b7a74a36](../../evidence/conditions-sets-098.md#c-fdb589a1b7a74a36) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c201ef8ce993d96f](../../evidence/state_effects-sets-041.md#s-c201ef8ce993d96f)

### static_slot_creation_candidates-003406

```text
(cfg-if-atm-range-pvc)# no class-vc <string> <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 10 `；EOL ` RVA 0x343E6FF8 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` ATM vc-class name to use on this pvc in range。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-86f999120b1782d4](../../evidence/conditions-sets-052.md#c-86f999120b1782d4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-7b80e9a4ca80845e](../../evidence/parameters-sets-010.md#p-7b80e9a4ca80845e) · [状态效果 S-c201ef8ce993d96f](../../evidence/state_effects-sets-041.md#s-c201ef8ce993d96f)

### static_slot_creation_candidates-003413

```text
(cfg-if-atm-range-pvc)# no dbs enable <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 69 `；EOL ` RVA 0x343E8350 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-f7a5ae61fad91418](../../evidence/conditions-sets-096.md#c-f7a5ae61fad91418) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c201ef8ce993d96f](../../evidence/state_effects-sets-041.md#s-c201ef8ce993d96f)

### static_slot_creation_candidates-003376

```text
(cfg-if-atm-range-pvc)# no encapsulation <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 12 `；EOL ` RVA 0x343E79D8 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-b3a98f62bac3911d](../../evidence/conditions-sets-069.md#c-b3a98f62bac3911d) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c201ef8ce993d96f](../../evidence/state_effects-sets-041.md#s-c201ef8ce993d96f)

### static_slot_creation_candidates-003382

```text
(cfg-if-atm-range-pvc)# no idle-timeout <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 26 `；EOL ` RVA 0x343E93B8 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-3cba83bb76300e20](../../evidence/conditions-sets-024.md#c-3cba83bb76300e20) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c201ef8ce993d96f](../../evidence/state_effects-sets-041.md#s-c201ef8ce993d96f)

### static_slot_creation_candidates-003408

```text
(cfg-if-atm-range-pvc)# no ilmi manage <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 15 `；EOL ` RVA 0x343E7FB0 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-86f999120b1782d4](../../evidence/conditions-sets-052.md#c-86f999120b1782d4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c201ef8ce993d96f](../../evidence/state_effects-sets-041.md#s-c201ef8ce993d96f)

### static_slot_creation_candidates-003375

```text
(cfg-if-atm-range-pvc)# no inarp <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 13 `；EOL ` RVA 0x343E7CC0 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-86f999120b1782d4](../../evidence/conditions-sets-052.md#c-86f999120b1782d4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c201ef8ce993d96f](../../evidence/state_effects-sets-041.md#s-c201ef8ce993d96f)

### static_slot_creation_candidates-003415

```text
(cfg-if-atm-range-pvc)# no oam retry <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 20 `；EOL ` RVA 0x343E8860 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-9436a506f941b81e](../../evidence/conditions-sets-057.md#c-9436a506f941b81e) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-8f8687c3a9b14ecc](../../evidence/state_effects-sets-030.md#s-8f8687c3a9b14ecc)

### static_slot_creation_candidates-003383

```text
(cfg-if-atm-range-pvc)# no oam-pvc <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 16 `；EOL ` RVA 0x343E9020 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-86f999120b1782d4](../../evidence/conditions-sets-052.md#c-86f999120b1782d4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-7cc5f305ce905faf](../../evidence/state_effects-sets-026.md#s-7cc5f305ce905faf)

### static_slot_creation_candidates-003404

```text
(cfg-if-atm-range-pvc)# no pppoe max-sessions <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 44 `；EOL ` RVA 0x343E66A8 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-a0a6f9c2c2d7741f](../../evidence/conditions-sets-062.md#c-a0a6f9c2c2d7741f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c201ef8ce993d96f](../../evidence/state_effects-sets-041.md#s-c201ef8ce993d96f)

### static_slot_creation_candidates-003370

```text
(cfg-if-atm-range-pvc)# no queue-depth <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 72 `；EOL ` RVA 0x343E5F68 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-bebc07a4917bbf40](../../evidence/conditions-sets-074.md#c-bebc07a4917bbf40) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c201ef8ce993d96f](../../evidence/state_effects-sets-041.md#s-c201ef8ce993d96f)

### static_slot_creation_candidates-003365

```text
(cfg-if-atm-range-pvc)# no rx-speed <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 86 `；EOL ` RVA 0x343E62D8 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-f5a60eaa975ef020](../../evidence/conditions-sets-095.md#c-f5a60eaa975ef020) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c201ef8ce993d96f](../../evidence/state_effects-sets-041.md#s-c201ef8ce993d96f)

### static_slot_creation_candidates-003381

```text
(cfg-if-atm-range-pvc)# no shutdown <cr>
```

Handler ` RVA 0xECE8380 `；selector ` 0 `；EOL ` RVA 0x343E96C8 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-86f999120b1782d4](../../evidence/conditions-sets-052.md#c-86f999120b1782d4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c201ef8ce993d96f](../../evidence/state_effects-sets-041.md#s-c201ef8ce993d96f)

### static_slot_creation_candidates-003384

```text
(cfg-if-atm-range-pvc)# no tx-ring-limit <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 32 `；EOL ` RVA 0x343E8C68 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-f4bf94c83cc75836](../../evidence/conditions-sets-094.md#c-f4bf94c83cc75836) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c201ef8ce993d96f](../../evidence/state_effects-sets-041.md#s-c201ef8ce993d96f)

### static_slot_creation_candidates-003394

```text
(cfg-if-atm-range-pvc)# no ubr <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 3 `；EOL ` RVA 0x343EA7F0 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-9fe94fb93f92e1e6](../../evidence/conditions-sets-062.md#c-9fe94fb93f92e1e6) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c201ef8ce993d96f](../../evidence/state_effects-sets-041.md#s-c201ef8ce993d96f)

### static_slot_creation_candidates-003392

```text
(cfg-if-atm-range-pvc)# no ubr+ <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 4 `；EOL ` RVA 0x343EA410 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-4f0892bb03807f7a](../../evidence/conditions-sets-031.md#c-4f0892bb03807f7a) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c201ef8ce993d96f](../../evidence/state_effects-sets-041.md#s-c201ef8ce993d96f)

### static_slot_creation_candidates-003397

```text
(cfg-if-atm-range-pvc)# no vbr-nrt <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 5 `；EOL ` RVA 0x343EABC8 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-d92baf587c2525fd](../../evidence/conditions-sets-084.md#c-d92baf587c2525fd) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c201ef8ce993d96f](../../evidence/state_effects-sets-041.md#s-c201ef8ce993d96f)

### static_slot_creation_candidates-003400

```text
(cfg-if-atm-range-pvc)# no vbr-rt <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 6 `；EOL ` RVA 0x343EB378 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-6551f6318b8adbef](../../evidence/conditions-sets-039.md#c-6551f6318b8adbef) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c201ef8ce993d96f](../../evidence/state_effects-sets-041.md#s-c201ef8ce993d96f)

### static_slot_creation_candidates-003367

```text
(cfg-if-atm-range-pvc)# no weight <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 83 `；EOL ` RVA 0x343E5BC8 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-dcee4c7301d730df](../../evidence/conditions-sets-085.md#c-dcee4c7301d730df) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c201ef8ce993d96f](../../evidence/state_effects-sets-041.md#s-c201ef8ce993d96f)

### static_slot_creation_candidates-003391

```text
(cfg-if-atm-range-pvc)# oam retry <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 20 `；EOL ` RVA 0x343E8860 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-11c30dd96b45372f](../../evidence/conditions-sets-007.md#c-11c30dd96b45372f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-4d095b49de47a9ed](../../evidence/state_effects-sets-017.md#s-4d095b49de47a9ed)

### static_slot_creation_candidates-003361

```text
(cfg-if-atm-range-pvc)# oam-pvc <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 16 `；EOL ` RVA 0x343E9020 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-86f999120b1782d4](../../evidence/conditions-sets-052.md#c-86f999120b1782d4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9a9d5b676db3a465](../../evidence/state_effects-sets-033.md#s-9a9d5b676db3a465)

### static_slot_creation_candidates-003429

```text
(cfg-if-atm-range-pvc)# pppoe max-sessions <number:dynamic> <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 44 `；EOL ` RVA 0x343E66A8 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Maximum PPPOE sessions。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-63698ce0ca040bae](../../evidence/conditions-sets-038.md#c-63698ce0ca040bae) · [缺口 G-59e37c7f420f6891](../../evidence/gaps-sets-004.md#g-59e37c7f420f6891) · [参数 P-30cb24ea617dbfd5](../../evidence/parameters-sets-004.md#p-30cb24ea617dbfd5)

### static_slot_creation_candidates-003423

```text
(cfg-if-atm-range-pvc)# protocol <?protoname_action@555589941858> <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 11 `；EOL ` RVA 0x343ED960 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-a6e1b576b2a75a94](../../evidence/conditions-sets-064.md#c-a6e1b576b2a75a94) · [缺口 G-46326218c10da938](../../evidence/gaps-sets-003.md#g-46326218c10da938)

### static_slot_creation_candidates-003424

```text
(cfg-if-atm-range-pvc)# protocol <?protoname_action@555589941858> <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 29 `；EOL ` RVA 0x343EDD20 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-6fb6324fbaa41d23](../../evidence/conditions-sets-043.md#c-6fb6324fbaa41d23) · [缺口 G-46326218c10da938](../../evidence/gaps-sets-003.md#g-46326218c10da938)

### static_slot_creation_candidates-003432

```text
(cfg-if-atm-range-pvc)# queue-depth <number:dynamic> <number:dynamic> <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 72 `；EOL ` RVA 0x343E5F68 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` queue depth high watermark, in cells；` unsigned_number_dynamic ` queue depth low watermark, in cells。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-d6a995e60691a92a](../../evidence/conditions-sets-083.md#c-d6a995e60691a92a) · [缺口 G-ea2ce359e271f8f2](../../evidence/gaps-sets-008.md#g-ea2ce359e271f8f2) · [参数 P-5caa37ef493ffefe](../../evidence/parameters-sets-007.md#p-5caa37ef493ffefe)

### static_slot_creation_candidates-003422

```text
(cfg-if-atm-range-pvc)# rx-speed <number:dynamic> <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 86 `；EOL ` RVA 0x343E62D8 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Incoming Cell Rate for L2TP AVP 38 in Kbps。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-463661cde27c9490](../../evidence/conditions-sets-027.md#c-463661cde27c9490) · [缺口 G-3de06ff404128685](../../evidence/gaps-sets-003.md#g-3de06ff404128685) · [参数 P-1304d24051f7bf95](../../evidence/parameters-sets-002.md#p-1304d24051f7bf95)

### static_slot_creation_candidates-003437

```text
(cfg-if-atm-range-pvc)# service-policy input <string> <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 37 `；EOL ` RVA 0x343EBC18 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Policy-map name。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-972e11207004b7a9](../../evidence/conditions-sets-058.md#c-972e11207004b7a9) · [缺口 G-c98b8d9dcf5dd4de](../../evidence/gaps-sets-007.md#g-c98b8d9dcf5dd4de) · [参数 P-b61f4936603c5a44](../../evidence/parameters-sets-014.md#p-b61f4936603c5a44) · [状态效果 S-7843a2f5ddfa07ce](../../evidence/state_effects-sets-026.md#s-7843a2f5ddfa07ce)

### static_slot_creation_candidates-003360

```text
(cfg-if-atm-range-pvc)# shutdown <cr>
```

Handler ` RVA 0xECE8380 `；selector ` 0 `；EOL ` RVA 0x343E96C8 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-86f999120b1782d4](../../evidence/conditions-sets-052.md#c-86f999120b1782d4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### static_slot_creation_candidates-003362

```text
(cfg-if-atm-range-pvc)# tx-ring-limit <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 32 `；EOL ` RVA 0x343E8C68 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-f4bf94c83cc75836](../../evidence/conditions-sets-094.md#c-f4bf94c83cc75836) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### static_slot_creation_candidates-003425

```text
(cfg-if-atm-range-pvc)# tx-ring-limit <number:dynamic> <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 32 `；EOL ` RVA 0x343E8C68 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Number (ring limit)。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-2ceb124607bc1154](../../evidence/conditions-sets-018.md#c-2ceb124607bc1154) · [缺口 G-a02dc29828e6dab1](../../evidence/gaps-sets-006.md#g-a02dc29828e6dab1) · [参数 P-c1744629b1c28e55](../../evidence/parameters-sets-015.md#p-c1744629b1c28e55)

### static_slot_creation_candidates-003363

```text
(cfg-if-atm-range-pvc)# ubr <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 3 `；EOL ` RVA 0x343EA7F0 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-9322c5fab9024e3a](../../evidence/conditions-sets-057.md#c-9322c5fab9024e3a) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### static_slot_creation_candidates-003427

```text
(cfg-if-atm-range-pvc)# ubr <number:dynamic> <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 3 `；EOL ` RVA 0x343EA7F0 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Peak Cell Rate(PCR) in Kbps。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-6e556ea6279b436e](../../evidence/conditions-sets-043.md#c-6e556ea6279b436e) · [缺口 G-ab72527d060382c3](../../evidence/gaps-sets-006.md#g-ab72527d060382c3) · [参数 P-75dcbc913d414d8f](../../evidence/parameters-sets-009.md#p-75dcbc913d414d8f)

### static_slot_creation_candidates-003433

```text
(cfg-if-atm-range-pvc)# ubr+ <number:dynamic> <number:dynamic> <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 4 `；EOL ` RVA 0x343EA410 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Peak Cell Rate(PCR) in Kbps；` unsigned_number_dynamic ` Minimum Guaranteed Cell Rate(MCR) in Kbps。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-7788bd11a7909e13](../../evidence/conditions-sets-046.md#c-7788bd11a7909e13) · [缺口 G-6234dbe124b3fcb2](../../evidence/gaps-sets-004.md#g-6234dbe124b3fcb2) · [参数 P-9d96bb511db0226f](../../evidence/parameters-sets-012.md#p-9d96bb511db0226f)

### static_slot_creation_candidates-003435

```text
(cfg-if-atm-range-pvc)# vbr-nrt <number:dynamic> <number:dynamic> <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 5 `；EOL ` RVA 0x343EABC8 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Peak Cell Rate(PCR) in Kbps；` unsigned_number_dynamic ` Sustainable Cell Rate(SCR) in Kbps。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-bf29a8916724e3e6](../../evidence/conditions-sets-074.md#c-bf29a8916724e3e6) · [缺口 G-638d30f798723519](../../evidence/gaps-sets-004.md#g-638d30f798723519) · [参数 P-6f566faa6fe2650d](../../evidence/parameters-sets-009.md#p-6f566faa6fe2650d)

### static_slot_creation_candidates-003436

```text
(cfg-if-atm-range-pvc)# vbr-rt <number:dynamic> <number:dynamic> <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 6 `；EOL ` RVA 0x343EB378 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Peak Cell Rate(PCR) in Kbps；` unsigned_number_dynamic ` Average Cell Rate in Kbps。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-47d8d5584513040a](../../evidence/conditions-sets-028.md#c-47d8d5584513040a) · [缺口 G-3d9daff99b7c1df0](../../evidence/gaps-sets-003.md#g-3d9daff99b7c1df0) · [参数 P-bf2f597edf7c4c2e](../../evidence/parameters-sets-015.md#p-bf2f597edf7c4c2e)

### static_slot_creation_candidates-003421

```text
(cfg-if-atm-range-pvc)# weight <number:dynamic> <cr>
```

Handler ` RVA 0xECE81B0 `；selector ` 83 `；EOL ` RVA 0x343E5BC8 `。

模式根 ` RVA 0x343DD508 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` &lt;Range&gt;。

[候选注册 R-6758bc7283c0c796](../../evidence/conditional_registrations-sets-001.md#r-6758bc7283c0c796) · [条件 C-7267cc8f847628a0](../../evidence/conditions-sets-044.md#c-7267cc8f847628a0) · [缺口 G-e5ac8a82c61a069d](../../evidence/gaps-sets-008.md#g-e5ac8a82c61a069d) · [参数 P-837caf3a38eb0242](../../evidence/parameters-sets-010.md#p-837caf3a38eb0242)
