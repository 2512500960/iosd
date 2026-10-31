# suppsrvcvp · 依赖静态建槽的条件安装

[模式索引](README.md) · [总索引](../../README.md)

### static_slot_creation_candidates-004361

```text
(config-stcapp-suppl-serv-port)# cbarge <cr>
```

Handler ` RVA 0x18720250 `；selector ` 0 `；EOL ` RVA 0x367CA5B0 `。

模式根 ` RVA 0x367C0CE8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-f2ffe00b93db640c](../../evidence/conditional_registrations-sets-003.md#r-f2ffe00b93db640c) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-5ddedc02c0c81b6d](../../evidence/state_effects-sets-020.md#s-5ddedc02c0c81b6d)

### static_slot_creation_candidates-004374

```text
(config-stcapp-suppl-serv-port)# cptone call-waiting repetition interval <number:0..30> <cr>
```

Handler ` RVA 0x18720250 `；selector ` 0 `；EOL ` RVA 0x367C9BA0 `。

模式根 ` RVA 0x367C0CE8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Call waiting tone repetition interval in seconds。

[候选注册 R-f2ffe00b93db640c](../../evidence/conditional_registrations-sets-003.md#r-f2ffe00b93db640c) · [条件 C-e99c8efca4f06d98](../../evidence/conditions-sets-090.md#c-e99c8efca4f06d98) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-3411104ded078d59](../../evidence/parameters-sets-004.md#p-3411104ded078d59) · [状态效果 S-3fcc712f7bbd869f](../../evidence/state_effects-sets-014.md#s-3fcc712f7bbd869f)

### static_slot_creation_candidates-004367

```text
(config-stcapp-suppl-serv-port)# default cbarge <cr>
```

Handler ` RVA 0x18720250 `；selector ` 0 `；EOL ` RVA 0x367CA5B0 `。

模式根 ` RVA 0x367C0CE8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-f2ffe00b93db640c](../../evidence/conditional_registrations-sets-003.md#r-f2ffe00b93db640c) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9f65cc429887c904](../../evidence/state_effects-sets-034.md#s-9f65cc429887c904)

### static_slot_creation_candidates-004375

```text
(config-stcapp-suppl-serv-port)# default cptone call-waiting repetition interval <cr>
```

Handler ` RVA 0x18720250 `；selector ` 0 `；EOL ` RVA 0x367C9BA0 `。

模式根 ` RVA 0x367C0CE8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-f2ffe00b93db640c](../../evidence/conditional_registrations-sets-003.md#r-f2ffe00b93db640c) · [条件 C-824f52a67abe8b4b](../../evidence/conditions-sets-050.md#c-824f52a67abe8b4b) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-11f51613438f633c](../../evidence/state_effects-sets-004.md#s-11f51613438f633c)

### static_slot_creation_candidates-004372

```text
(config-stcapp-suppl-serv-port)# default fallback-dn <string> <cr>
```

Handler ` RVA 0x18720250 `；selector ` 0 `；EOL ` RVA 0x367C9EC8 `。

模式根 ` RVA 0x367C0CE8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-f2ffe00b93db640c](../../evidence/conditional_registrations-sets-003.md#r-f2ffe00b93db640c) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-e67ead7230e1ffb3](../../evidence/parameters-sets-017.md#p-e67ead7230e1ffb3) · [状态效果 S-ee1537eb988b872a](../../evidence/state_effects-sets-050.md#s-ee1537eb988b872a)

### static_slot_creation_candidates-004365

```text
(config-stcapp-suppl-serv-port)# default hold-resume <cr>
```

Handler ` RVA 0x18720250 `；selector ` 0 `；EOL ` RVA 0x367CA1F8 `。

模式根 ` RVA 0x367C0CE8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-f2ffe00b93db640c](../../evidence/conditional_registrations-sets-003.md#r-f2ffe00b93db640c) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-edc26e1d062e7ca4](../../evidence/state_effects-sets-050.md#s-edc26e1d062e7ca4)

### static_slot_creation_candidates-004370

```text
(config-stcapp-suppl-serv-port)# default privacy <cr>
```

Handler ` RVA 0x18720250 `；selector ` 0 `；EOL ` RVA 0x367CA920 `。

模式根 ` RVA 0x367C0CE8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-f2ffe00b93db640c](../../evidence/conditional_registrations-sets-003.md#r-f2ffe00b93db640c) · [条件 C-2f7e1425d3edd04b](../../evidence/conditions-sets-019.md#c-2f7e1425d3edd04b) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-6d3ff664a1684335](../../evidence/state_effects-sets-023.md#s-6d3ff664a1684335)

### static_slot_creation_candidates-004362

```text
(config-stcapp-suppl-serv-port)# exit <cr>
```

Handler ` RVA 0x18720A60 `；selector ` 0 `；EOL ` RVA 0x367CAC80 `。

模式根 ` RVA 0x367C0CE8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-f2ffe00b93db640c](../../evidence/conditional_registrations-sets-003.md#r-f2ffe00b93db640c) · [条件 C-5271411adc172bd7](../../evidence/conditions-sets-032.md#c-5271411adc172bd7) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### static_slot_creation_candidates-004363

```text
(config-stcapp-suppl-serv-port)# fallback-dn <string> <cr>
```

Handler ` RVA 0x18720250 `；selector ` 0 `；EOL ` RVA 0x367C9EC8 `。

模式根 ` RVA 0x367C0CE8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-f2ffe00b93db640c](../../evidence/conditional_registrations-sets-003.md#r-f2ffe00b93db640c) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-e67ead7230e1ffb3](../../evidence/parameters-sets-017.md#p-e67ead7230e1ffb3) · [状态效果 S-2a3a5715e90b28ed](../../evidence/state_effects-sets-009.md#s-2a3a5715e90b28ed)

### static_slot_creation_candidates-004360

```text
(config-stcapp-suppl-serv-port)# hold-resume <cr>
```

Handler ` RVA 0x18720250 `；selector ` 0 `；EOL ` RVA 0x367CA1F8 `。

模式根 ` RVA 0x367C0CE8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-f2ffe00b93db640c](../../evidence/conditional_registrations-sets-003.md#r-f2ffe00b93db640c) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-f700f16fc23229b2](../../evidence/state_effects-sets-052.md#s-f700f16fc23229b2)

### static_slot_creation_candidates-004366

```text
(config-stcapp-suppl-serv-port)# no cbarge <cr>
```

Handler ` RVA 0x18720250 `；selector ` 0 `；EOL ` RVA 0x367CA5B0 `。

模式根 ` RVA 0x367C0CE8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-f2ffe00b93db640c](../../evidence/conditional_registrations-sets-003.md#r-f2ffe00b93db640c) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-fa1501089e215953](../../evidence/state_effects-sets-053.md#s-fa1501089e215953)

### static_slot_creation_candidates-004373

```text
(config-stcapp-suppl-serv-port)# no cptone call-waiting repetition interval <cr>
```

Handler ` RVA 0x18720250 `；selector ` 0 `；EOL ` RVA 0x367C9BA0 `。

模式根 ` RVA 0x367C0CE8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-f2ffe00b93db640c](../../evidence/conditional_registrations-sets-003.md#r-f2ffe00b93db640c) · [条件 C-0823f51b62f3415e](../../evidence/conditions-sets-004.md#c-0823f51b62f3415e) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c0cfb4bb5b1e56b8](../../evidence/state_effects-sets-041.md#s-c0cfb4bb5b1e56b8)

### static_slot_creation_candidates-004371

```text
(config-stcapp-suppl-serv-port)# no fallback-dn <string> <cr>
```

Handler ` RVA 0x18720250 `；selector ` 0 `；EOL ` RVA 0x367C9EC8 `。

模式根 ` RVA 0x367C0CE8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-f2ffe00b93db640c](../../evidence/conditional_registrations-sets-003.md#r-f2ffe00b93db640c) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-e67ead7230e1ffb3](../../evidence/parameters-sets-017.md#p-e67ead7230e1ffb3) · [状态效果 S-2b2301bd6c791c2b](../../evidence/state_effects-sets-010.md#s-2b2301bd6c791c2b)

### static_slot_creation_candidates-004364

```text
(config-stcapp-suppl-serv-port)# no hold-resume <cr>
```

Handler ` RVA 0x18720250 `；selector ` 0 `；EOL ` RVA 0x367CA1F8 `。

模式根 ` RVA 0x367C0CE8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-f2ffe00b93db640c](../../evidence/conditional_registrations-sets-003.md#r-f2ffe00b93db640c) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-02d65ac87a7f1196](../../evidence/state_effects-sets-001.md#s-02d65ac87a7f1196)

### static_slot_creation_candidates-004369

```text
(config-stcapp-suppl-serv-port)# no privacy <cr>
```

Handler ` RVA 0x18720250 `；selector ` 0 `；EOL ` RVA 0x367CA920 `。

模式根 ` RVA 0x367C0CE8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-f2ffe00b93db640c](../../evidence/conditional_registrations-sets-003.md#r-f2ffe00b93db640c) · [条件 C-c6c57f83060ad2a7](../../evidence/conditions-sets-077.md#c-c6c57f83060ad2a7) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-cfdb75e4aaf40280](../../evidence/state_effects-sets-044.md#s-cfdb75e4aaf40280)

### static_slot_creation_candidates-004368

```text
(config-stcapp-suppl-serv-port)# privacy on <cr>
```

Handler ` RVA 0x18720250 `；selector ` 0 `；EOL ` RVA 0x367CA920 `。

模式根 ` RVA 0x367C0CE8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-f2ffe00b93db640c](../../evidence/conditional_registrations-sets-003.md#r-f2ffe00b93db640c) · [条件 C-9427c58fe786ae43](../../evidence/conditions-sets-057.md#c-9427c58fe786ae43) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-ac717aec1f2bcec4](../../evidence/state_effects-sets-036.md#s-ac717aec1f2bcec4)

