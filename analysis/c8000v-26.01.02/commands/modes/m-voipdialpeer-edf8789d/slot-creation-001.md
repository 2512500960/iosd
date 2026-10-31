# voipdialpeer · 依赖静态建槽的条件安装

[模式索引](README.md) · [总索引](../../README.md)

### static_slot_creation_candidates-003805

```text
(config-dial-peer)# corlist incoming <string> <cr>
```

Handler ` RVA 0x1BCE8030 `；selector ` 1 `；EOL ` RVA 0x37049128 `。

模式根 ` RVA 0x36FE8A50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` incoming Class of Restriction list name。

[候选注册 R-498e420c932bcf98](../../evidence/conditional_registrations-sets-001.md#r-498e420c932bcf98) · [条件 C-cff42ade7af3e866](../../evidence/conditions-sets-080.md#c-cff42ade7af3e866) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-ef415082e446c378](../../evidence/parameters-sets-018.md#p-ef415082e446c378)

### static_slot_creation_candidates-003808

```text
(config-dial-peer)# corlist outgoing <string> <cr>
```

Handler ` RVA 0x1BCE8030 `；selector ` 0 `；EOL ` RVA 0x37049448 `。

模式根 ` RVA 0x36FE8A50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` outgoing Class of Restriction list name。

[候选注册 R-498e420c932bcf98](../../evidence/conditional_registrations-sets-001.md#r-498e420c932bcf98) · [条件 C-99168c016c92ca93](../../evidence/conditions-sets-059.md#c-99168c016c92ca93) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-710048d8473f6b11](../../evidence/parameters-sets-009.md#p-710048d8473f6b11)

### static_slot_creation_candidates-003806

```text
(config-dial-peer)# default corlist incoming <cr>
```

Handler ` RVA 0x1BCE8030 `；selector ` 1 `；EOL ` RVA 0x37049128 `。

模式根 ` RVA 0x36FE8A50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-498e420c932bcf98](../../evidence/conditional_registrations-sets-001.md#r-498e420c932bcf98) · [条件 C-884021cd4d17b5ee](../../evidence/conditions-sets-053.md#c-884021cd4d17b5ee) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-98fccc1539d3d400](../../evidence/state_effects-sets-033.md#s-98fccc1539d3d400)

### static_slot_creation_candidates-003809

```text
(config-dial-peer)# default corlist outgoing <cr>
```

Handler ` RVA 0x1BCE8030 `；selector ` 0 `；EOL ` RVA 0x37049448 `。

模式根 ` RVA 0x36FE8A50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-498e420c932bcf98](../../evidence/conditional_registrations-sets-001.md#r-498e420c932bcf98) · [条件 C-249058b47a8398b9](../../evidence/conditions-sets-014.md#c-249058b47a8398b9) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-98fccc1539d3d400](../../evidence/state_effects-sets-033.md#s-98fccc1539d3d400)

### static_slot_creation_candidates-003851

```text
(config-dial-peer)# default destination calling e164-pattern-map <cr>
```

Handler ` RVA 0x1BD15CD0 `；selector ` 0 `；EOL ` RVA 0x36FF4918 `。

模式根 ` RVA 0x36FE8A50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-7bad028a6576d3a4](../../evidence/conditional_registrations-sets-002.md#r-7bad028a6576d3a4) · [条件 C-8c8e0c38c9e967c4](../../evidence/conditions-sets-054.md#c-8c8e0c38c9e967c4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-b95b461d4bc2ff4f](../../evidence/state_effects-sets-039.md#s-b95b461d4bc2ff4f)

### static_slot_creation_candidates-003827

```text
(config-dial-peer)# default destination dpg <cr>
```

Handler ` RVA 0x1BD16450 `；selector ` 0 `；EOL ` RVA 0x36FF3E98 `。

模式根 ` RVA 0x36FE8A50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-7bad028a6576d3a4](../../evidence/conditional_registrations-sets-002.md#r-7bad028a6576d3a4) · [条件 C-7be73559bf0b5fd7](../../evidence/conditions-sets-048.md#c-7be73559bf0b5fd7) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-e5f95a288a760ee4](../../evidence/state_effects-sets-049.md#s-e5f95a288a760ee4)

### static_slot_creation_candidates-003833

```text
(config-dial-peer)# default destination e164-pattern-map <cr>
```

Handler ` RVA 0x1BD15CD0 `；selector ` 0 `；EOL ` RVA 0x36FF4238 `。

模式根 ` RVA 0x36FE8A50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-7bad028a6576d3a4](../../evidence/conditional_registrations-sets-002.md#r-7bad028a6576d3a4) · [条件 C-603e16f0de719af3](../../evidence/conditions-sets-037.md#c-603e16f0de719af3) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-99833845cf9e1bc4](../../evidence/state_effects-sets-033.md#s-99833845cf9e1bc4)

### static_slot_creation_candidates-003839

```text
(config-dial-peer)# default destination provision-policy <cr>
```

Handler ` RVA 0x1BD16A30 `；selector ` 0 `；EOL ` RVA 0x36FF4598 `。

模式根 ` RVA 0x36FE8A50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-7bad028a6576d3a4](../../evidence/conditional_registrations-sets-002.md#r-7bad028a6576d3a4) · [条件 C-05d2a2da36602d6a](../../evidence/conditions-sets-003.md#c-05d2a2da36602d6a) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-557ec45871c579ec](../../evidence/state_effects-sets-019.md#s-557ec45871c579ec)

### static_slot_creation_candidates-003813

```text
(config-dial-peer)# default destination route-string <cr>
```

Handler ` RVA 0x1BD12590 `；selector ` 0 `；EOL ` RVA 0x36FF2678 `。

模式根 ` RVA 0x36FE8A50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-7bad028a6576d3a4](../../evidence/conditional_registrations-sets-002.md#r-7bad028a6576d3a4) · [条件 C-4ed269ea2952dfde](../../evidence/conditions-sets-031.md#c-4ed269ea2952dfde) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-98fccc1539d3d400](../../evidence/state_effects-sets-033.md#s-98fccc1539d3d400)

### static_slot_creation_candidates-003821

```text
(config-dial-peer)# default destination uri <cr>
```

Handler ` RVA 0x1BD11270 `；selector ` 0 `；EOL ` RVA 0x36FF3B00 `。

模式根 ` RVA 0x36FE8A50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-7bad028a6576d3a4](../../evidence/conditional_registrations-sets-002.md#r-7bad028a6576d3a4) · [条件 C-0dc867aec8f1d787](../../evidence/conditions-sets-006.md#c-0dc867aec8f1d787) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-fe277ee776793e2e](../../evidence/state_effects-sets-054.md#s-fe277ee776793e2e)

### static_slot_creation_candidates-003820

```text
(config-dial-peer)# default destination uri-diversion <cr>
```

Handler ` RVA 0x1BD11270 `；selector ` 0 `；EOL ` RVA 0x36FF29E0 `。

模式根 ` RVA 0x36FE8A50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-7bad028a6576d3a4](../../evidence/conditional_registrations-sets-002.md#r-7bad028a6576d3a4) · [条件 C-2dee3bf761df119b](../../evidence/conditions-sets-018.md#c-2dee3bf761df119b) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-eda651a90783d28a](../../evidence/state_effects-sets-050.md#s-eda651a90783d28a)

### static_slot_creation_candidates-003826

```text
(config-dial-peer)# default destination uri-from <cr>
```

Handler ` RVA 0x1BD11270 `；selector ` 0 `；EOL ` RVA 0x36FF2D40 `。

模式根 ` RVA 0x36FE8A50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-7bad028a6576d3a4](../../evidence/conditional_registrations-sets-002.md#r-7bad028a6576d3a4) · [条件 C-e3a3ecbcc7316454](../../evidence/conditions-sets-088.md#c-e3a3ecbcc7316454) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-ca07c98b0bf3c0b1](../../evidence/state_effects-sets-043.md#s-ca07c98b0bf3c0b1)

### static_slot_creation_candidates-003832

```text
(config-dial-peer)# default destination uri-referred-by <cr>
```

Handler ` RVA 0x1BD11270 `；selector ` 0 `；EOL ` RVA 0x36FF30A0 `。

模式根 ` RVA 0x36FE8A50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-7bad028a6576d3a4](../../evidence/conditional_registrations-sets-002.md#r-7bad028a6576d3a4) · [条件 C-1d1e4a4ba4708593](../../evidence/conditions-sets-011.md#c-1d1e4a4ba4708593) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-3f04290113cc9752](../../evidence/state_effects-sets-014.md#s-3f04290113cc9752)

### static_slot_creation_candidates-003838

```text
(config-dial-peer)# default destination uri-to <cr>
```

Handler ` RVA 0x1BD11270 `；selector ` 0 `；EOL ` RVA 0x36FF3400 `。

模式根 ` RVA 0x36FE8A50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-7bad028a6576d3a4](../../evidence/conditional_registrations-sets-002.md#r-7bad028a6576d3a4) · [条件 C-c4be6dff9fac8838](../../evidence/conditions-sets-076.md#c-c4be6dff9fac8838) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-1c5c5d27901f5fab](../../evidence/state_effects-sets-006.md#s-1c5c5d27901f5fab)

### static_slot_creation_candidates-003842

```text
(config-dial-peer)# default destination uri-via <cr>
```

Handler ` RVA 0x1BD11270 `；selector ` 0 `；EOL ` RVA 0x36FF3760 `。

模式根 ` RVA 0x36FE8A50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-7bad028a6576d3a4](../../evidence/conditional_registrations-sets-002.md#r-7bad028a6576d3a4) · [条件 C-e8b1eda823f000e4](../../evidence/conditions-sets-090.md#c-e8b1eda823f000e4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-18ff14f079c8e111](../../evidence/state_effects-sets-006.md#s-18ff14f079c8e111)

### static_slot_creation_candidates-003850

```text
(config-dial-peer)# default incoming called e164-pattern-map <cr>
```

Handler ` RVA 0x1BD16100 `；selector ` 0 `；EOL ` RVA 0x36FF5970 `。

模式根 ` RVA 0x36FE8A50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-7bad028a6576d3a4](../../evidence/conditional_registrations-sets-002.md#r-7bad028a6576d3a4) · [条件 C-c70d304d1d827752](../../evidence/conditions-sets-077.md#c-c70d304d1d827752) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-4722d2b0419ae97e](../../evidence/state_effects-sets-016.md#s-4722d2b0419ae97e)

### static_slot_creation_candidates-003819

```text
(config-dial-peer)# default incoming called-number <cr>
```

Handler ` RVA 0x1BCEACC0 `；selector ` 24 `；EOL ` RVA 0x36FF4D80 `。

模式根 ` RVA 0x36FE8A50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-7bad028a6576d3a4](../../evidence/conditional_registrations-sets-002.md#r-7bad028a6576d3a4) · [条件 C-dcb976aefced6503](../../evidence/conditions-sets-085.md#c-dcb976aefced6503) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-98fccc1539d3d400](../../evidence/state_effects-sets-033.md#s-98fccc1539d3d400)

### static_slot_creation_candidates-003847

```text
(config-dial-peer)# default incoming uri request <cr>
```

Handler ` RVA 0x1BD11270 `；selector ` 0 `；EOL ` RVA 0x36FF51C0 `。

模式根 ` RVA 0x36FE8A50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-7bad028a6576d3a4](../../evidence/conditional_registrations-sets-002.md#r-7bad028a6576d3a4) · [条件 C-e4810d813b23c510](../../evidence/conditions-sets-088.md#c-e4810d813b23c510) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-b77a2b77250cf428](../../evidence/state_effects-sets-039.md#s-b77a2b77250cf428)

### static_slot_creation_candidates-003803

```text
(config-dial-peer)# default permission <cr>
```

Handler ` RVA 0x1BCE8460 `；selector ` 0 `；EOL ` RVA 0x37049780 `。

模式根 ` RVA 0x36FE8A50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-498e420c932bcf98](../../evidence/conditional_registrations-sets-001.md#r-498e420c932bcf98) · [条件 C-b9ebd7c4f3b1f178](../../evidence/conditions-sets-072.md#c-b9ebd7c4f3b1f178) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-98fccc1539d3d400](../../evidence/state_effects-sets-033.md#s-98fccc1539d3d400)

### static_slot_creation_candidates-003800

```text
(config-dial-peer)# default phone-proxy <cr>
```

Handler ` RVA 0x1BD189E0 `；selector ` 0 `；EOL ` RVA 0x3779CA50 `。

模式根 ` RVA 0x36FE8A50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-057abf5bd102a470](../../evidence/conditional_registrations-sets-001.md#r-057abf5bd102a470) · [条件 C-637e7bbf3ad057dc](../../evidence/conditions-sets-039.md#c-637e7bbf3ad057dc) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-98fccc1539d3d400](../../evidence/state_effects-sets-033.md#s-98fccc1539d3d400)

### static_slot_creation_candidates-003849

```text
(config-dial-peer)# destination calling e164-pattern-map <number:1..10000> <cr>
```

Handler ` RVA 0x1BD15CD0 `；selector ` 0 `；EOL ` RVA 0x36FF4918 `。

模式根 ` RVA 0x36FE8A50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` The e164-pattern-map group tag number。

[候选注册 R-7bad028a6576d3a4](../../evidence/conditional_registrations-sets-002.md#r-7bad028a6576d3a4) · [条件 C-4e8a8870047b908b](../../evidence/conditions-sets-031.md#c-4e8a8870047b908b) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-76eb0c9c7148268c](../../evidence/parameters-sets-009.md#p-76eb0c9c7148268c) · [状态效果 S-73ccbb475432c3eb](../../evidence/state_effects-sets-025.md#s-73ccbb475432c3eb)

### static_slot_creation_candidates-003825

```text
(config-dial-peer)# destination dpg <number:1..10000> <cr>
```

Handler ` RVA 0x1BD16450 `；selector ` 0 `；EOL ` RVA 0x36FF3E98 `。

模式根 ` RVA 0x36FE8A50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` The voice class dpg tag number。

[候选注册 R-7bad028a6576d3a4](../../evidence/conditional_registrations-sets-002.md#r-7bad028a6576d3a4) · [条件 C-ffc2f2ce2468b135](../../evidence/conditions-sets-099.md#c-ffc2f2ce2468b135) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-9a62a3a20eadd9ab](../../evidence/parameters-sets-012.md#p-9a62a3a20eadd9ab) · [状态效果 S-849be956e81d6321](../../evidence/state_effects-sets-028.md#s-849be956e81d6321)

### static_slot_creation_candidates-003831

```text
(config-dial-peer)# destination e164-pattern-map <number:1..10000> <cr>
```

Handler ` RVA 0x1BD15CD0 `；selector ` 0 `；EOL ` RVA 0x36FF4238 `。

模式根 ` RVA 0x36FE8A50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` The e164-pattern-map group tag number。

[候选注册 R-7bad028a6576d3a4](../../evidence/conditional_registrations-sets-002.md#r-7bad028a6576d3a4) · [条件 C-d80cafb3d0f584b8](../../evidence/conditions-sets-083.md#c-d80cafb3d0f584b8) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-b67ca6a0864264e2](../../evidence/parameters-sets-014.md#p-b67ca6a0864264e2) · [状态效果 S-44e48ac23c6dce74](../../evidence/state_effects-sets-015.md#s-44e48ac23c6dce74)

### static_slot_creation_candidates-003837

```text
(config-dial-peer)# destination provision-policy <number:1..10000> <cr>
```

Handler ` RVA 0x1BD16A30 `；selector ` 0 `；EOL ` RVA 0x36FF4598 `。

模式根 ` RVA 0x36FE8A50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` The voice class dial-peer provision-policy tag number。

[候选注册 R-7bad028a6576d3a4](../../evidence/conditional_registrations-sets-002.md#r-7bad028a6576d3a4) · [条件 C-3d088718ac997d06](../../evidence/conditions-sets-024.md#c-3d088718ac997d06) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-833392c6f492e001](../../evidence/parameters-sets-010.md#p-833392c6f492e001) · [状态效果 S-eb4b2469c2041bb0](../../evidence/state_effects-sets-050.md#s-eb4b2469c2041bb0)

### static_slot_creation_candidates-003811

```text
(config-dial-peer)# destination route-string <number:1..10000> <cr>
```

Handler ` RVA 0x1BD12590 `；selector ` 0 `；EOL ` RVA 0x36FF2678 `。

模式根 ` RVA 0x36FE8A50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Voice class route-string tag。

[候选注册 R-7bad028a6576d3a4](../../evidence/conditional_registrations-sets-002.md#r-7bad028a6576d3a4) · [条件 C-314c14e13787a985](../../evidence/conditions-sets-019.md#c-314c14e13787a985) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-e95d0e9ea65b01a1](../../evidence/parameters-sets-017.md#p-e95d0e9ea65b01a1)

### static_slot_creation_candidates-003818

```text
(config-dial-peer)# destination uri <string> <cr>
```

Handler ` RVA 0x1BD11270 `；selector ` 0 `；EOL ` RVA 0x36FF3B00 `。

模式根 ` RVA 0x36FE8A50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Voice URI class tag。

[候选注册 R-7bad028a6576d3a4](../../evidence/conditional_registrations-sets-002.md#r-7bad028a6576d3a4) · [条件 C-ab90bc072c561fb5](../../evidence/conditions-sets-066.md#c-ab90bc072c561fb5) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-abe61953aeea89f9](../../evidence/parameters-sets-013.md#p-abe61953aeea89f9) · [状态效果 S-d3f1575d19c46b41](../../evidence/state_effects-sets-045.md#s-d3f1575d19c46b41)

### static_slot_creation_candidates-003817

```text
(config-dial-peer)# destination uri-diversion <string> <cr>
```

Handler ` RVA 0x1BD11270 `；selector ` 0 `；EOL ` RVA 0x36FF29E0 `。

模式根 ` RVA 0x36FE8A50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Voice URI class tag。

[候选注册 R-7bad028a6576d3a4](../../evidence/conditional_registrations-sets-002.md#r-7bad028a6576d3a4) · [条件 C-58a51f789530257b](../../evidence/conditions-sets-035.md#c-58a51f789530257b) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-60d9cbe32f3a70d4](../../evidence/parameters-sets-008.md#p-60d9cbe32f3a70d4) · [状态效果 S-e75ae44fa1f2708a](../../evidence/state_effects-sets-049.md#s-e75ae44fa1f2708a)

### static_slot_creation_candidates-003824

```text
(config-dial-peer)# destination uri-from <string> <cr>
```

Handler ` RVA 0x1BD11270 `；selector ` 0 `；EOL ` RVA 0x36FF2D40 `。

模式根 ` RVA 0x36FE8A50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Voice URI class tag。

[候选注册 R-7bad028a6576d3a4](../../evidence/conditional_registrations-sets-002.md#r-7bad028a6576d3a4) · [条件 C-fb70da096cfd535a](../../evidence/conditions-sets-097.md#c-fb70da096cfd535a) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-50f6e084e5a1b451](../../evidence/parameters-sets-007.md#p-50f6e084e5a1b451) · [状态效果 S-97f96b5e62a9be82](../../evidence/state_effects-sets-032.md#s-97f96b5e62a9be82)

### static_slot_creation_candidates-003830

```text
(config-dial-peer)# destination uri-referred-by <string> <cr>
```

Handler ` RVA 0x1BD11270 `；selector ` 0 `；EOL ` RVA 0x36FF30A0 `。

模式根 ` RVA 0x36FE8A50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Voice URI class tag。

[候选注册 R-7bad028a6576d3a4](../../evidence/conditional_registrations-sets-002.md#r-7bad028a6576d3a4) · [条件 C-cef4b12e8f3b068c](../../evidence/conditions-sets-080.md#c-cef4b12e8f3b068c) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-d754e2a29875b0dc](../../evidence/parameters-sets-016.md#p-d754e2a29875b0dc) · [状态效果 S-3903476c8a3e83ad](../../evidence/state_effects-sets-013.md#s-3903476c8a3e83ad)

### static_slot_creation_candidates-003836

```text
(config-dial-peer)# destination uri-to <string> <cr>
```

Handler ` RVA 0x1BD11270 `；selector ` 0 `；EOL ` RVA 0x36FF3400 `。

模式根 ` RVA 0x36FE8A50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Voice URI class tag。

[候选注册 R-7bad028a6576d3a4](../../evidence/conditional_registrations-sets-002.md#r-7bad028a6576d3a4) · [条件 C-c17a9cb14db3dc54](../../evidence/conditions-sets-075.md#c-c17a9cb14db3dc54) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-46678a9aab47ab8c](../../evidence/parameters-sets-006.md#p-46678a9aab47ab8c) · [状态效果 S-b25275e8b5456f0d](../../evidence/state_effects-sets-038.md#s-b25275e8b5456f0d)

### static_slot_creation_candidates-003841

```text
(config-dial-peer)# destination uri-via <string> <cr>
```

Handler ` RVA 0x1BD11270 `；selector ` 0 `；EOL ` RVA 0x36FF3760 `。

模式根 ` RVA 0x36FE8A50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Voice URI class tag。

[候选注册 R-7bad028a6576d3a4](../../evidence/conditional_registrations-sets-002.md#r-7bad028a6576d3a4) · [条件 C-300673a2f18b3b3b](../../evidence/conditions-sets-019.md#c-300673a2f18b3b3b) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-e60f8be1912b9a0c](../../evidence/parameters-sets-017.md#p-e60f8be1912b9a0c) · [状态效果 S-1d81a38e1f7c72e9](../../evidence/state_effects-sets-007.md#s-1d81a38e1f7c72e9)

### static_slot_creation_candidates-003848

```text
(config-dial-peer)# incoming called e164-pattern-map <number:1..10000> <cr>
```

Handler ` RVA 0x1BD16100 `；selector ` 0 `；EOL ` RVA 0x36FF5970 `。

模式根 ` RVA 0x36FE8A50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` The e164-pattern-map voice class tag number。

[候选注册 R-7bad028a6576d3a4](../../evidence/conditional_registrations-sets-002.md#r-7bad028a6576d3a4) · [条件 C-9e33c62d9a546cfb](../../evidence/conditions-sets-061.md#c-9e33c62d9a546cfb) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-1675fa4d3cd5a76c](../../evidence/parameters-sets-002.md#p-1675fa4d3cd5a76c) · [状态效果 S-c149f1986efd7841](../../evidence/state_effects-sets-041.md#s-c149f1986efd7841)

### static_slot_creation_candidates-003816

```text
(config-dial-peer)# incoming called-number <string> <cr>
```

Handler ` RVA 0x1BCEACC0 `；selector ` 24 `；EOL ` RVA 0x36FF4D80 `。

模式根 ` RVA 0x36FE8A50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` A sequence of digits representing a phone number prefix。

[候选注册 R-7bad028a6576d3a4](../../evidence/conditional_registrations-sets-002.md#r-7bad028a6576d3a4) · [条件 C-3ece807b53d05ac3](../../evidence/conditions-sets-024.md#c-3ece807b53d05ac3) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-f40344e85fee244c](../../evidence/parameters-sets-018.md#p-f40344e85fee244c)

### static_slot_creation_candidates-003844

```text
(config-dial-peer)# incoming uri request <string> <cr>
```

Handler ` RVA 0x1BD11270 `；selector ` 0 `；EOL ` RVA 0x36FF51C0 `。

模式根 ` RVA 0x36FE8A50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Voice URI Class tag。

[候选注册 R-7bad028a6576d3a4](../../evidence/conditional_registrations-sets-002.md#r-7bad028a6576d3a4) · [条件 C-c754bd257f270848](../../evidence/conditions-sets-077.md#c-c754bd257f270848) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-8e2436e1bae70eb6](../../evidence/parameters-sets-011.md#p-8e2436e1bae70eb6) · [状态效果 S-7d23e2e7392a097a](../../evidence/state_effects-sets-027.md#s-7d23e2e7392a097a)

### static_slot_creation_candidates-003804

```text
(config-dial-peer)# no corlist incoming <cr>
```

Handler ` RVA 0x1BCE8030 `；selector ` 1 `；EOL ` RVA 0x37049128 `。

模式根 ` RVA 0x36FE8A50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-498e420c932bcf98](../../evidence/conditional_registrations-sets-001.md#r-498e420c932bcf98) · [条件 C-f5fc37548f97cc0e](../../evidence/conditions-sets-095.md#c-f5fc37548f97cc0e) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-debfcf3195c22814](../../evidence/state_effects-sets-047.md#s-debfcf3195c22814)

### static_slot_creation_candidates-003807

```text
(config-dial-peer)# no corlist outgoing <cr>
```

Handler ` RVA 0x1BCE8030 `；selector ` 0 `；EOL ` RVA 0x37049448 `。

模式根 ` RVA 0x36FE8A50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-498e420c932bcf98](../../evidence/conditional_registrations-sets-001.md#r-498e420c932bcf98) · [条件 C-7cf8ec287c47fe49](../../evidence/conditions-sets-048.md#c-7cf8ec287c47fe49) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-debfcf3195c22814](../../evidence/state_effects-sets-047.md#s-debfcf3195c22814)

### static_slot_creation_candidates-003846

```text
(config-dial-peer)# no destination calling e164-pattern-map <cr>
```

Handler ` RVA 0x1BD15CD0 `；selector ` 0 `；EOL ` RVA 0x36FF4918 `。

模式根 ` RVA 0x36FE8A50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-7bad028a6576d3a4](../../evidence/conditional_registrations-sets-002.md#r-7bad028a6576d3a4) · [条件 C-c7e2fd90c5d72b82](../../evidence/conditions-sets-077.md#c-c7e2fd90c5d72b82) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-d2a39daea4b30706](../../evidence/state_effects-sets-045.md#s-d2a39daea4b30706)

### static_slot_creation_candidates-003823

```text
(config-dial-peer)# no destination dpg <cr>
```

Handler ` RVA 0x1BD16450 `；selector ` 0 `；EOL ` RVA 0x36FF3E98 `。

模式根 ` RVA 0x36FE8A50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-7bad028a6576d3a4](../../evidence/conditional_registrations-sets-002.md#r-7bad028a6576d3a4) · [条件 C-73ecf2c4422f8877](../../evidence/conditions-sets-045.md#c-73ecf2c4422f8877) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-f796929d39b55275](../../evidence/state_effects-sets-052.md#s-f796929d39b55275)

### static_slot_creation_candidates-003829

```text
(config-dial-peer)# no destination e164-pattern-map <cr>
```

Handler ` RVA 0x1BD15CD0 `；selector ` 0 `；EOL ` RVA 0x36FF4238 `。

模式根 ` RVA 0x36FE8A50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-7bad028a6576d3a4](../../evidence/conditional_registrations-sets-002.md#r-7bad028a6576d3a4) · [条件 C-270b1d1c705aa622](../../evidence/conditions-sets-015.md#c-270b1d1c705aa622) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-f28187a8010e8f1e](../../evidence/state_effects-sets-051.md#s-f28187a8010e8f1e)

### static_slot_creation_candidates-003835

```text
(config-dial-peer)# no destination provision-policy <cr>
```

Handler ` RVA 0x1BD16A30 `；selector ` 0 `；EOL ` RVA 0x36FF4598 `。

模式根 ` RVA 0x36FE8A50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-7bad028a6576d3a4](../../evidence/conditional_registrations-sets-002.md#r-7bad028a6576d3a4) · [条件 C-2b79ff0ef31c4654](../../evidence/conditions-sets-017.md#c-2b79ff0ef31c4654) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-bee89fc11e9fc18f](../../evidence/state_effects-sets-040.md#s-bee89fc11e9fc18f)

### static_slot_creation_candidates-003810

```text
(config-dial-peer)# no destination route-string <cr>
```

Handler ` RVA 0x1BD12590 `；selector ` 0 `；EOL ` RVA 0x36FF2678 `。

模式根 ` RVA 0x36FE8A50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-7bad028a6576d3a4](../../evidence/conditional_registrations-sets-002.md#r-7bad028a6576d3a4) · [条件 C-74131d10d6951a14](../../evidence/conditions-sets-045.md#c-74131d10d6951a14) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-debfcf3195c22814](../../evidence/state_effects-sets-047.md#s-debfcf3195c22814)

### static_slot_creation_candidates-003815

```text
(config-dial-peer)# no destination uri <cr>
```

Handler ` RVA 0x1BD11270 `；selector ` 0 `；EOL ` RVA 0x36FF3B00 `。

模式根 ` RVA 0x36FE8A50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-7bad028a6576d3a4](../../evidence/conditional_registrations-sets-002.md#r-7bad028a6576d3a4) · [条件 C-1ec650e744c39d02](../../evidence/conditions-sets-012.md#c-1ec650e744c39d02) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-e6654944feca46ce](../../evidence/state_effects-sets-049.md#s-e6654944feca46ce)

### static_slot_creation_candidates-003814

```text
(config-dial-peer)# no destination uri-diversion <cr>
```

Handler ` RVA 0x1BD11270 `；selector ` 0 `；EOL ` RVA 0x36FF29E0 `。

模式根 ` RVA 0x36FE8A50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-7bad028a6576d3a4](../../evidence/conditional_registrations-sets-002.md#r-7bad028a6576d3a4) · [条件 C-10129acc364e2ffb](../../evidence/conditions-sets-006.md#c-10129acc364e2ffb) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9d39bfe1eaa96121](../../evidence/state_effects-sets-033.md#s-9d39bfe1eaa96121)

### static_slot_creation_candidates-003822

```text
(config-dial-peer)# no destination uri-from <cr>
```

Handler ` RVA 0x1BD11270 `；selector ` 0 `；EOL ` RVA 0x36FF2D40 `。

模式根 ` RVA 0x36FE8A50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-7bad028a6576d3a4](../../evidence/conditional_registrations-sets-002.md#r-7bad028a6576d3a4) · [条件 C-aa1054e8b2d8ea99](../../evidence/conditions-sets-066.md#c-aa1054e8b2d8ea99) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-5e0100f3aac06157](../../evidence/state_effects-sets-020.md#s-5e0100f3aac06157)

### static_slot_creation_candidates-003828

```text
(config-dial-peer)# no destination uri-referred-by <cr>
```

Handler ` RVA 0x1BD11270 `；selector ` 0 `；EOL ` RVA 0x36FF30A0 `。

模式根 ` RVA 0x36FE8A50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-7bad028a6576d3a4](../../evidence/conditional_registrations-sets-002.md#r-7bad028a6576d3a4) · [条件 C-6b34e9d86e63b45d](../../evidence/conditions-sets-041.md#c-6b34e9d86e63b45d) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-ccf25c11cbdaa73d](../../evidence/state_effects-sets-043.md#s-ccf25c11cbdaa73d)

### static_slot_creation_candidates-003834

```text
(config-dial-peer)# no destination uri-to <cr>
```

Handler ` RVA 0x1BD11270 `；selector ` 0 `；EOL ` RVA 0x36FF3400 `。

模式根 ` RVA 0x36FE8A50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-7bad028a6576d3a4](../../evidence/conditional_registrations-sets-002.md#r-7bad028a6576d3a4) · [条件 C-9431dbcabf5c70f7](../../evidence/conditions-sets-057.md#c-9431dbcabf5c70f7) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-72ba0b6682db900e](../../evidence/state_effects-sets-024.md#s-72ba0b6682db900e)

### static_slot_creation_candidates-003840

```text
(config-dial-peer)# no destination uri-via <cr>
```

Handler ` RVA 0x1BD11270 `；selector ` 0 `；EOL ` RVA 0x36FF3760 `。

模式根 ` RVA 0x36FE8A50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-7bad028a6576d3a4](../../evidence/conditional_registrations-sets-002.md#r-7bad028a6576d3a4) · [条件 C-efccf62197080ffa](../../evidence/conditions-sets-093.md#c-efccf62197080ffa) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-587f20aba31aadf6](../../evidence/state_effects-sets-019.md#s-587f20aba31aadf6)

### static_slot_creation_candidates-003845

```text
(config-dial-peer)# no incoming called e164-pattern-map <cr>
```

Handler ` RVA 0x1BD16100 `；selector ` 0 `；EOL ` RVA 0x36FF5970 `。

模式根 ` RVA 0x36FE8A50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-7bad028a6576d3a4](../../evidence/conditional_registrations-sets-002.md#r-7bad028a6576d3a4) · [条件 C-37dcd18b13bb8121](../../evidence/conditions-sets-022.md#c-37dcd18b13bb8121) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-a93f78ee5fd9420b](../../evidence/state_effects-sets-036.md#s-a93f78ee5fd9420b)

### static_slot_creation_candidates-003812

```text
(config-dial-peer)# no incoming called-number <cr>
```

Handler ` RVA 0x1BCEACC0 `；selector ` 24 `；EOL ` RVA 0x36FF4D80 `。

模式根 ` RVA 0x36FE8A50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-7bad028a6576d3a4](../../evidence/conditional_registrations-sets-002.md#r-7bad028a6576d3a4) · [条件 C-1f0db3badedd0530](../../evidence/conditions-sets-012.md#c-1f0db3badedd0530) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-debfcf3195c22814](../../evidence/state_effects-sets-047.md#s-debfcf3195c22814)

### static_slot_creation_candidates-003843

```text
(config-dial-peer)# no incoming uri request <cr>
```

Handler ` RVA 0x1BD11270 `；selector ` 0 `；EOL ` RVA 0x36FF51C0 `。

模式根 ` RVA 0x36FE8A50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-7bad028a6576d3a4](../../evidence/conditional_registrations-sets-002.md#r-7bad028a6576d3a4) · [条件 C-e130130944e54bbb](../../evidence/conditions-sets-087.md#c-e130130944e54bbb) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-6b13b26046a83526](../../evidence/state_effects-sets-023.md#s-6b13b26046a83526)

### static_slot_creation_candidates-003801

```text
(config-dial-peer)# no permission <cr>
```

Handler ` RVA 0x1BCE8460 `；selector ` 0 `；EOL ` RVA 0x37049780 `。

模式根 ` RVA 0x36FE8A50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-498e420c932bcf98](../../evidence/conditional_registrations-sets-001.md#r-498e420c932bcf98) · [条件 C-a5a5cd9d9c75aea8](../../evidence/conditions-sets-064.md#c-a5a5cd9d9c75aea8) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-debfcf3195c22814](../../evidence/state_effects-sets-047.md#s-debfcf3195c22814)

### static_slot_creation_candidates-003799

```text
(config-dial-peer)# no phone-proxy <cr>
```

Handler ` RVA 0x1BD189E0 `；selector ` 0 `；EOL ` RVA 0x3779CA50 `。

模式根 ` RVA 0x36FE8A50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-057abf5bd102a470](../../evidence/conditional_registrations-sets-001.md#r-057abf5bd102a470) · [条件 C-b0eed6eef84b6441](../../evidence/conditions-sets-068.md#c-b0eed6eef84b6441) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-debfcf3195c22814](../../evidence/state_effects-sets-047.md#s-debfcf3195c22814)

### static_slot_creation_candidates-003802

```text
(config-dial-peer)# permission both <cr>
```

Handler ` RVA 0x1BCE8460 `；selector ` 0 `；EOL ` RVA 0x37049780 `。

模式根 ` RVA 0x36FE8A50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-498e420c932bcf98](../../evidence/conditional_registrations-sets-001.md#r-498e420c932bcf98) · [条件 C-71da2f498d1efd96](../../evidence/conditions-sets-044.md#c-71da2f498d1efd96) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-20bc694b2a7f88a8](../../evidence/state_effects-sets-007.md#s-20bc694b2a7f88a8)

### static_slot_creation_candidates-003852

```text
(config-dial-peer)# phone-proxy <string> signal-addr ipv4 <address> cucm ipv4 <address> <cr>
```

Handler ` RVA 0x1BD189E0 `；selector ` 0 `；EOL ` RVA 0x3779CA50 `。

模式根 ` RVA 0x36FE8A50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Phone Proxy name；` address ` IPV4 Address；` address ` IPV4 Address。

[候选注册 R-057abf5bd102a470](../../evidence/conditional_registrations-sets-001.md#r-057abf5bd102a470) · [条件 C-e5658b25df770405](../../evidence/conditions-sets-088.md#c-e5658b25df770405) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-44edabc3bf82c195](../../evidence/parameters-sets-006.md#p-44edabc3bf82c195)

