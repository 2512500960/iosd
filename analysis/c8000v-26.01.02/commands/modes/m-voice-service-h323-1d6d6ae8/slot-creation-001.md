# voice-service-h323 · 依赖静态建槽的条件安装

[模式索引](README.md) · [总索引](../../README.md)

### static_slot_creation_candidates-004622

```text
(conf-serv-h323)# default h450 h450-2 timeout T1 <cr>
```

Handler ` RVA 0x167EF6D0 `；selector ` 0 `；EOL ` RVA 0x35FC19B8 `。

模式根 ` RVA 0x370ACD40 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-4dc726095e9ccd70](../../evidence/conditional_registrations-sets-001.md#r-4dc726095e9ccd70) · [条件 C-a4f5a4315de43751](../../evidence/conditions-sets-064.md#c-a4f5a4315de43751) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-2c1caf6de92b7238](../../evidence/state_effects-sets-010.md#s-2c1caf6de92b7238)

### static_slot_creation_candidates-004621

```text
(conf-serv-h323)# h450 h450-2 timeout T1 <number:500..60000> <cr>
```

Handler ` RVA 0x167EF6D0 `；selector ` 0 `；EOL ` RVA 0x35FC19B8 `。

模式根 ` RVA 0x370ACD40 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` milliseconds。

[候选注册 R-4dc726095e9ccd70](../../evidence/conditional_registrations-sets-001.md#r-4dc726095e9ccd70) · [条件 C-926b4a2c7b521510](../../evidence/conditions-sets-056.md#c-926b4a2c7b521510) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-aeea974fce71d03c](../../evidence/parameters-sets-013.md#p-aeea974fce71d03c) · [状态效果 S-3f9884b2d0a449dd](../../evidence/state_effects-sets-014.md#s-3f9884b2d0a449dd)

### static_slot_creation_candidates-004620

```text
(conf-serv-h323)# no h450 h450-2 timeout T1 <cr>
```

Handler ` RVA 0x167EF6D0 `；selector ` 0 `；EOL ` RVA 0x35FC19B8 `。

模式根 ` RVA 0x370ACD40 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-4dc726095e9ccd70](../../evidence/conditional_registrations-sets-001.md#r-4dc726095e9ccd70) · [条件 C-41fa6c8af5adc286](../../evidence/conditions-sets-026.md#c-41fa6c8af5adc286) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-e4f35054ce294467](../../evidence/state_effects-sets-048.md#s-e4f35054ce294467)
