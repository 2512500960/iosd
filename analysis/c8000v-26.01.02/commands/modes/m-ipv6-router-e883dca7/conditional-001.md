# ipv6-router · 已捕获槽位上的条件安装

[模式索引](README.md) · [总索引](../../README.md)

### conditional_registration_candidates-010789

```text
(config-rtr)# dag-id <address> <cr>
```

Handler ` RVA 0x1854F060 `；selector ` 11 `；EOL ` RVA 0x3677A620 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` &lt;enter the dag-id&gt;。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-9f62e76256d670aa](../../evidence/conditions-sets-062.md#c-9f62e76256d670aa) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-db5e3b3858e9b7bd](../../evidence/parameters-sets-017.md#p-db5e3b3858e9b7bd)

### conditional_registration_candidates-010872

```text
(config-rtr)# dag-id unnumbered <interface> <cr>
```

Handler ` RVA 0x1854F060 `；selector ` 11 `；EOL ` RVA 0x3677A620 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-2a999b3bcf94bb82](../../evidence/conditions-sets-017.md#c-2a999b3bcf94bb82) · [缺口 G-45d37eff3656cddc](../../evidence/gaps-sets-003.md#g-45d37eff3656cddc) · [参数 P-00971ed1d3fdbfe7](../../evidence/parameters-sets-001.md#p-00971ed1d3fdbfe7) · [状态效果 S-de639fe4f6c8a492](../../evidence/state_effects-sets-047.md#s-de639fe4f6c8a492)

### conditional_registration_candidates-010851

```text
(config-rtr)# dao delay <number:1..255> <cr>
```

Handler ` RVA 0x1854F3F0 `；selector ` 35 `；EOL ` RVA 0x36776B68 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` &lt;delay-value&gt;。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-4a1f32db47028eb0](../../evidence/conditions-sets-029.md#c-4a1f32db47028eb0) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-e3791920cda8aa3b](../../evidence/parameters-sets-017.md#p-e3791920cda8aa3b)

### conditional_registration_candidates-010808

```text
(config-rtr)# dao enable <cr>
```

Handler ` RVA 0x1854F3F0 `；selector ` 33 `；EOL ` RVA 0x36776E30 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-1673371d7a0521bb](../../evidence/conditions-sets-009.md#c-1673371d7a0521bb) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### conditional_registration_candidates-010847

```text
(config-rtr)# dao latency <number:20..100> <cr>
```

Handler ` RVA 0x1854F3F0 `；selector ` 34 `；EOL ` RVA 0x36776818 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` &lt;latency-value&gt;。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-e3f725d6a5f58efd](../../evidence/conditions-sets-088.md#c-e3f725d6a5f58efd) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-7f1a96b98f657aa6](../../evidence/parameters-sets-010.md#p-7f1a96b98f657aa6)

### conditional_registration_candidates-010786

```text
(config-rtr)# default dag-id <cr>
```

Handler ` RVA 0x1854F060 `；selector ` 11 `；EOL ` RVA 0x3677A620 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-8731ae4f578a7252](../../evidence/conditions-sets-052.md#c-8731ae4f578a7252) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### conditional_registration_candidates-010853

```text
(config-rtr)# default dao delay <cr>
```

Handler ` RVA 0x1854F3F0 `；selector ` 35 `；EOL ` RVA 0x36776B68 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-50663ad7a34b736e](../../evidence/conditions-sets-031.md#c-50663ad7a34b736e) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### conditional_registration_candidates-010852

```text
(config-rtr)# default dao enable <cr>
```

Handler ` RVA 0x1854F3F0 `；selector ` 33 `；EOL ` RVA 0x36776E30 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-1673371d7a0521bb](../../evidence/conditions-sets-009.md#c-1673371d7a0521bb) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### conditional_registration_candidates-010849

```text
(config-rtr)# default dao latency <cr>
```

Handler ` RVA 0x1854F3F0 `；selector ` 34 `；EOL ` RVA 0x36776818 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-998ddbb91b44fc1c](../../evidence/conditions-sets-059.md#c-998ddbb91b44fc1c) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### conditional_registration_candidates-010816

```text
(config-rtr)# default definition node <cr>
```

Handler ` RVA 0x1854E680 `；selector ` 10 `；EOL ` RVA 0x3677A258 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-73036f8c00241a0d](../../evidence/conditions-sets-044.md#c-73036f8c00241a0d) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### conditional_registration_candidates-010814

```text
(config-rtr)# default definition root <cr>
```

Handler ` RVA 0x1854E680 `；selector ` 9 `；EOL ` RVA 0x36779FB0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-73036f8c00241a0d](../../evidence/conditions-sets-044.md#c-73036f8c00241a0d) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### conditional_registration_candidates-010795

```text
(config-rtr)# default fast-connect <cr>
```

Handler ` RVA 0x1854F3F0 `；selector ` 31 `；EOL ` RVA 0x36778608 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-39e528ca60509322](../../evidence/conditions-sets-022.md#c-39e528ca60509322) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### conditional_registration_candidates-010794

```text
(config-rtr)# default floating <cr>
```

Handler ` RVA 0x1854F3F0 `；selector ` 19 `；EOL ` RVA 0x3677BB48 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-f4369925ad515fca](../../evidence/conditions-sets-094.md#c-f4369925ad515fca) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### conditional_registration_candidates-010828

```text
(config-rtr)# default global-repair interval <cr>
```

Handler ` RVA 0x1854F3F0 `；selector ` 18 `；EOL ` RVA 0x3677B8B0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-5e22106bbbe0e557](../../evidence/conditions-sets-037.md#c-5e22106bbbe0e557) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### conditional_registration_candidates-010801

```text
(config-rtr)# default instance-id <cr>
```

Handler ` RVA 0x1854F060 `；selector ` 24 `；EOL ` RVA 0x36775CD0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-e7950448b7972c0a](../../evidence/conditions-sets-089.md#c-e7950448b7972c0a) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### conditional_registration_candidates-010819

```text
(config-rtr)# default link-check all <cr>
```

Handler ` RVA 0x1854F3F0 `；selector ` 23 `；EOL ` RVA 0x36777FB0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-4d1a2ca1ea2a7804](../../evidence/conditions-sets-030.md#c-4d1a2ca1ea2a7804) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### conditional_registration_candidates-010798

```text
(config-rtr)# default load-balance <cr>
```

Handler ` RVA 0x1854F3F0 `；selector ` 36 `；EOL ` RVA 0x367782D0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-8d014d5d3f1d8c76](../../evidence/conditions-sets-055.md#c-8d014d5d3f1d8c76) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### conditional_registration_candidates-010862

```text
(config-rtr)# default manet cache acknowledgement <cr>
```

Handler ` RVA 0x1B088650 `；selector ` 2 `；EOL ` RVA 0x36EEF158 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-f3b1aa145b477a9e](../../evidence/conditional_registrations-sets-003.md#r-f3b1aa145b477a9e) · [条件 C-a7d4e8dc39b76f3c](../../evidence/conditions-sets-065.md#c-a7d4e8dc39b76f3c) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### conditional_registration_candidates-010858

```text
(config-rtr)# default manet cache update <cr>
```

Handler ` RVA 0x1B088650 `；selector ` 1 `；EOL ` RVA 0x36EEEE30 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-f3b1aa145b477a9e](../../evidence/conditional_registrations-sets-003.md#r-f3b1aa145b477a9e) · [条件 C-877c8a2490da0585](../../evidence/conditions-sets-052.md#c-877c8a2490da0585) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### conditional_registration_candidates-010866

```text
(config-rtr)# default manet hello unicast <cr>
```

Handler ` RVA 0x1B088650 `；selector ` 5 `；EOL ` RVA 0x36EF0240 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-f3b1aa145b477a9e](../../evidence/conditional_registrations-sets-003.md#r-f3b1aa145b477a9e) · [条件 C-7315de189623d2a8](../../evidence/conditions-sets-045.md#c-7315de189623d2a8) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-08b15919e2011615](../../evidence/state_effects-sets-002.md#s-08b15919e2011615)

### conditional_registration_candidates-010869

```text
(config-rtr)# default manet peering selective <cr>
```

Handler ` RVA 0x1B088650 `；selector ` 4 `；EOL ` RVA 0x36EEFDD8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-f3b1aa145b477a9e](../../evidence/conditional_registrations-sets-003.md#r-f3b1aa145b477a9e) · [条件 C-7315de189623d2a8](../../evidence/conditions-sets-045.md#c-7315de189623d2a8) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### conditional_registration_candidates-010864

```text
(config-rtr)# default manet timers ackwait <cr>
```

Handler ` RVA 0x1B0895B0 `；selector ` 0 `；EOL ` RVA 0x36EEF888 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-f3b1aa145b477a9e](../../evidence/conditional_registrations-sets-003.md#r-f3b1aa145b477a9e) · [条件 C-8963d0fce0ebac21](../../evidence/conditions-sets-053.md#c-8963d0fce0ebac21) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-27bbc321331abe0d](../../evidence/state_effects-sets-009.md#s-27bbc321331abe0d)

### conditional_registration_candidates-010846

```text
(config-rtr)# default manet willingness <cr>
```

Handler ` RVA 0x1B088650 `；selector ` 3 `；EOL ` RVA 0x36EEF4C0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-f3b1aa145b477a9e](../../evidence/conditional_registrations-sets-003.md#r-f3b1aa145b477a9e) · [条件 C-da496e7918302422](../../evidence/conditions-sets-084.md#c-da496e7918302422) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### conditional_registration_candidates-010812

```text
(config-rtr)# default nsr <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 21 `；EOL ` RVA 0x36771250 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-457ce8e189c6074d](../../evidence/conditional_registrations-sets-001.md#r-457ce8e189c6074d) · [条件 C-837cb51a3e942acd](../../evidence/conditions-sets-051.md#c-837cb51a3e942acd) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### conditional_registration_candidates-010805

```text
(config-rtr)# default ocp <cr>
```

Handler ` RVA 0x1854F060 `；selector ` 27 `；EOL ` RVA 0x36776080 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-6e411342f7991734](../../evidence/conditions-sets-043.md#c-6e411342f7991734) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### conditional_registration_candidates-010792

```text
(config-rtr)# default preference <cr>
```

Handler ` RVA 0x1854F3F0 `；selector ` 14 `；EOL ` RVA 0x3677AAC8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-4d973263d6e1fb96](../../evidence/conditions-sets-030.md#c-4d973263d6e1fb96) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### conditional_registration_candidates-010836

```text
(config-rtr)# default probe count <cr>
```

Handler ` RVA 0x1854F3F0 `；selector ` 21 `；EOL ` RVA 0x36777970 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-e98830209fd34109](../../evidence/conditions-sets-090.md#c-e98830209fd34109) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### conditional_registration_candidates-010829

```text
(config-rtr)# default probe interval <cr>
```

Handler ` RVA 0x1854F3F0 `；selector ` 20 `；EOL ` RVA 0x36777620 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-58c046a45056fb8d](../../evidence/conditions-sets-035.md#c-58c046a45056fb8d) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### conditional_registration_candidates-010842

```text
(config-rtr)# default probe payload <cr>
```

Handler ` RVA 0x1854F3F0 `；selector ` 22 `；EOL ` RVA 0x36777C98 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-bb4136d9922a2307](../../evidence/conditions-sets-072.md#c-bb4136d9922a2307) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### conditional_registration_candidates-010841

```text
(config-rtr)# default rank maximum-increase <cr>
```

Handler ` RVA 0x1854F3F0 `；selector ` 32 `；EOL ` RVA 0x3677BEF8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-0ef348e3b70b431e](../../evidence/conditions-sets-006.md#c-0ef348e3b70b431e) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### conditional_registration_candidates-010803

```text
(config-rtr)# default send-dis <cr>
```

Handler ` RVA 0x1854F3F0 `；selector ` 30 `；EOL ` RVA 0x36776440 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-bb16146841475736](../../evidence/conditions-sets-072.md#c-bb16146841475736) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### conditional_registration_candidates-010809

```text
(config-rtr)# default step-of-rank <cr>
```

Handler ` RVA 0x1854F3F0 `；selector ` 37 `；EOL ` RVA 0x36777178 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-0b5ac9788a7af26a](../../evidence/conditions-sets-005.md#c-0b5ac9788a7af26a) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### conditional_registration_candidates-010871

```text
(config-rtr)# default timers manet ackwait <cr>
```

Handler ` RVA 0x1B0895B0 `；selector ` 0 `；EOL ` RVA 0x36EF1430 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-79d83dfe57d9f285](../../evidence/conditional_registrations-sets-002.md#r-79d83dfe57d9f285) · [条件 C-de5040443987b86f](../../evidence/conditions-sets-086.md#c-de5040443987b86f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-8c827fed3d520b39](../../evidence/state_effects-sets-030.md#s-8c827fed3d520b39)

### conditional_registration_candidates-010830

```text
(config-rtr)# default trickle-timer doubling <cr>
```

Handler ` RVA 0x1854F3F0 `；selector ` 16 `；EOL ` RVA 0x3677B1D0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-ae4bcb109bd59294](../../evidence/conditions-sets-067.md#c-ae4bcb109bd59294) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### conditional_registration_candidates-010821

```text
(config-rtr)# default trickle-timer minimum <cr>
```

Handler ` RVA 0x1854F3F0 `；selector ` 15 `；EOL ` RVA 0x3677AE80 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-67de3aa55cf64268](../../evidence/conditions-sets-040.md#c-67de3aa55cf64268) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### conditional_registration_candidates-010837

```text
(config-rtr)# default trickle-timer redundancy-count <cr>
```

Handler ` RVA 0x1854F3F0 `；selector ` 17 `；EOL ` RVA 0x3677B4F8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-453019c1fe587bfa](../../evidence/conditions-sets-027.md#c-453019c1fe587bfa) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### conditional_registration_candidates-010784

```text
(config-rtr)# definition node <cr>
```

Handler ` RVA 0x1854E680 `；selector ` 10 `；EOL ` RVA 0x3677A258 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-73036f8c00241a0d](../../evidence/conditions-sets-044.md#c-73036f8c00241a0d) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### conditional_registration_candidates-010783

```text
(config-rtr)# definition root <cr>
```

Handler ` RVA 0x1854E680 `；selector ` 9 `；EOL ` RVA 0x36779FB0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-73036f8c00241a0d](../../evidence/conditions-sets-044.md#c-73036f8c00241a0d) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### conditional_registration_candidates-010780

```text
(config-rtr)# fast-connect <cr>
```

Handler ` RVA 0x1854F3F0 `；selector ` 31 `；EOL ` RVA 0x36778608 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-39e528ca60509322](../../evidence/conditions-sets-022.md#c-39e528ca60509322) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### conditional_registration_candidates-010779

```text
(config-rtr)# floating <cr>
```

Handler ` RVA 0x1854F3F0 `；selector ` 19 `；EOL ` RVA 0x3677BB48 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-f4369925ad515fca](../../evidence/conditions-sets-094.md#c-f4369925ad515fca) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### conditional_registration_candidates-010825

```text
(config-rtr)# global-repair interval <number:1..255> <cr>
```

Handler ` RVA 0x1854F3F0 `；selector ` 18 `；EOL ` RVA 0x3677B8B0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` &lt;interval-value&gt;。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-143eadd424797036](../../evidence/conditions-sets-008.md#c-143eadd424797036) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-ce4a22c1cff0b9ab](../../evidence/parameters-sets-016.md#p-ce4a22c1cff0b9ab)

### conditional_registration_candidates-010804

```text
(config-rtr)# instance-id <number:0..127> <cr>
```

Handler ` RVA 0x1854F060 `；selector ` 24 `；EOL ` RVA 0x36775CD0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` &lt;inst-id&gt;。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-73c2ddc29d67c88b](../../evidence/conditions-sets-045.md#c-73c2ddc29d67c88b) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-5dae60dee21c3d88](../../evidence/parameters-sets-007.md#p-5dae60dee21c3d88)

### conditional_registration_candidates-010793

```text
(config-rtr)# link-check all <cr>
```

Handler ` RVA 0x1854F3F0 `；selector ` 23 `；EOL ` RVA 0x36777FB0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-4d1a2ca1ea2a7804](../../evidence/conditions-sets-030.md#c-4d1a2ca1ea2a7804) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### conditional_registration_candidates-010797

```text
(config-rtr)# load-balance mp2p <cr>
```

Handler ` RVA 0x1854F3F0 `；selector ` 36 `；EOL ` RVA 0x367782D0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-4481fecea73b46eb](../../evidence/conditions-sets-027.md#c-4481fecea73b46eb) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-0e3eddbfd3eaaf21](../../evidence/state_effects-sets-003.md#s-0e3eddbfd3eaaf21)

### conditional_registration_candidates-010860

```text
(config-rtr)# manet cache acknowledgement <number:0..4294967295> <cr>
```

Handler ` RVA 0x1B088650 `；selector ` 2 `；EOL ` RVA 0x36EEF158 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Maximum number of acknowledgements in cache。

[候选注册 R-f3b1aa145b477a9e](../../evidence/conditional_registrations-sets-003.md#r-f3b1aa145b477a9e) · [条件 C-768e17e1d9d85aae](../../evidence/conditions-sets-046.md#c-768e17e1d9d85aae) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-53a41ecb657a0cd4](../../evidence/parameters-sets-007.md#p-53a41ecb657a0cd4)

### conditional_registration_candidates-010857

```text
(config-rtr)# manet cache update <number:0..4294967295> <cr>
```

Handler ` RVA 0x1B088650 `；selector ` 1 `；EOL ` RVA 0x36EEEE30 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Maximum number of LSAs in cache。

[候选注册 R-f3b1aa145b477a9e](../../evidence/conditional_registrations-sets-003.md#r-f3b1aa145b477a9e) · [条件 C-f9e8228dc8cfdf9e](../../evidence/conditions-sets-097.md#c-f9e8228dc8cfdf9e) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-ba39bafa2874b2d4](../../evidence/parameters-sets-014.md#p-ba39bafa2874b2d4)

### conditional_registration_candidates-010854

```text
(config-rtr)# manet hello unicast <cr>
```

Handler ` RVA 0x1B088650 `；selector ` 5 `；EOL ` RVA 0x36EF0240 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-f3b1aa145b477a9e](../../evidence/conditional_registrations-sets-003.md#r-f3b1aa145b477a9e) · [条件 C-7315de189623d2a8](../../evidence/conditions-sets-045.md#c-7315de189623d2a8) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-a21475c7f74c9428](../../evidence/state_effects-sets-034.md#s-a21475c7f74c9428)

### conditional_registration_candidates-010855

```text
(config-rtr)# manet peering selective <cr>
```

Handler ` RVA 0x1B088650 `；selector ` 4 `；EOL ` RVA 0x36EEFDD8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-f3b1aa145b477a9e](../../evidence/conditional_registrations-sets-003.md#r-f3b1aa145b477a9e) · [条件 C-7315de189623d2a8](../../evidence/conditions-sets-045.md#c-7315de189623d2a8) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### conditional_registration_candidates-010863

```text
(config-rtr)# manet timers ackwait <number:0..10000> <cr>
```

Handler ` RVA 0x1B0895B0 `；selector ` 0 `；EOL ` RVA 0x36EEF888 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Acknowledgement delay timer value in milliseconds。

[候选注册 R-f3b1aa145b477a9e](../../evidence/conditional_registrations-sets-003.md#r-f3b1aa145b477a9e) · [条件 C-85ae1b575886d5b0](../../evidence/conditions-sets-052.md#c-85ae1b575886d5b0) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-17d285d3fd2e5178](../../evidence/parameters-sets-002.md#p-17d285d3fd2e5178) · [状态效果 S-2fb854cb20ffdf34](../../evidence/state_effects-sets-011.md#s-2fb854cb20ffdf34)

### conditional_registration_candidates-010844

```text
(config-rtr)# manet willingness <number:0..255> <cr>
```

Handler ` RVA 0x1B088650 `；selector ` 3 `；EOL ` RVA 0x36EEF4C0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Relay willingness value。

[候选注册 R-f3b1aa145b477a9e](../../evidence/conditional_registrations-sets-003.md#r-f3b1aa145b477a9e) · [条件 C-5c9afb45c91fed04](../../evidence/conditions-sets-036.md#c-5c9afb45c91fed04) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-e77f4690b004a563](../../evidence/parameters-sets-017.md#p-e77f4690b004a563)

### conditional_registration_candidates-010785

```text
(config-rtr)# no dag-id <cr>
```

Handler ` RVA 0x1854F060 `；selector ` 11 `；EOL ` RVA 0x3677A620 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-a142b62f102c56ec](../../evidence/conditions-sets-062.md#c-a142b62f102c56ec) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### conditional_registration_candidates-010850

```text
(config-rtr)# no dao delay <cr>
```

Handler ` RVA 0x1854F3F0 `；selector ` 35 `；EOL ` RVA 0x36776B68 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-3d56b257a290324f](../../evidence/conditions-sets-024.md#c-3d56b257a290324f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### conditional_registration_candidates-010848

```text
(config-rtr)# no dao enable <cr>
```

Handler ` RVA 0x1854F3F0 `；selector ` 33 `；EOL ` RVA 0x36776E30 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-1673371d7a0521bb](../../evidence/conditions-sets-009.md#c-1673371d7a0521bb) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### conditional_registration_candidates-010845

```text
(config-rtr)# no dao latency <cr>
```

Handler ` RVA 0x1854F3F0 `；selector ` 34 `；EOL ` RVA 0x36776818 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-a38daa5c55e6b84c](../../evidence/conditions-sets-063.md#c-a38daa5c55e6b84c) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### conditional_registration_candidates-010815

```text
(config-rtr)# no definition node <cr>
```

Handler ` RVA 0x1854E680 `；selector ` 10 `；EOL ` RVA 0x3677A258 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-73036f8c00241a0d](../../evidence/conditions-sets-044.md#c-73036f8c00241a0d) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### conditional_registration_candidates-010813

```text
(config-rtr)# no definition root <cr>
```

Handler ` RVA 0x1854E680 `；selector ` 9 `；EOL ` RVA 0x36779FB0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-73036f8c00241a0d](../../evidence/conditions-sets-044.md#c-73036f8c00241a0d) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### conditional_registration_candidates-010791

```text
(config-rtr)# no fast-connect <cr>
```

Handler ` RVA 0x1854F3F0 `；selector ` 31 `；EOL ` RVA 0x36778608 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-39e528ca60509322](../../evidence/conditions-sets-022.md#c-39e528ca60509322) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### conditional_registration_candidates-010790

```text
(config-rtr)# no floating <cr>
```

Handler ` RVA 0x1854F3F0 `；selector ` 19 `；EOL ` RVA 0x3677BB48 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-f4369925ad515fca](../../evidence/conditions-sets-094.md#c-f4369925ad515fca) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### conditional_registration_candidates-010822

```text
(config-rtr)# no global-repair interval <cr>
```

Handler ` RVA 0x1854F3F0 `；selector ` 18 `；EOL ` RVA 0x3677B8B0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-e97ffbb928a9a84d](../../evidence/conditions-sets-090.md#c-e97ffbb928a9a84d) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### conditional_registration_candidates-010799

```text
(config-rtr)# no instance-id <cr>
```

Handler ` RVA 0x1854F060 `；selector ` 24 `；EOL ` RVA 0x36775CD0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-80f0dc1ab880bcb8](../../evidence/conditions-sets-050.md#c-80f0dc1ab880bcb8) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### conditional_registration_candidates-010817

```text
(config-rtr)# no link-check all <cr>
```

Handler ` RVA 0x1854F3F0 `；selector ` 23 `；EOL ` RVA 0x36777FB0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-4d1a2ca1ea2a7804](../../evidence/conditions-sets-030.md#c-4d1a2ca1ea2a7804) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### conditional_registration_candidates-010796

```text
(config-rtr)# no load-balance <cr>
```

Handler ` RVA 0x1854F3F0 `；selector ` 36 `；EOL ` RVA 0x367782D0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-f55af1d639cc0646](../../evidence/conditions-sets-095.md#c-f55af1d639cc0646) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### conditional_registration_candidates-010859

```text
(config-rtr)# no manet cache acknowledgement <cr>
```

Handler ` RVA 0x1B088650 `；selector ` 2 `；EOL ` RVA 0x36EEF158 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-f3b1aa145b477a9e](../../evidence/conditional_registrations-sets-003.md#r-f3b1aa145b477a9e) · [条件 C-775aebac1f503191](../../evidence/conditions-sets-046.md#c-775aebac1f503191) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### conditional_registration_candidates-010856

```text
(config-rtr)# no manet cache update <cr>
```

Handler ` RVA 0x1B088650 `；selector ` 1 `；EOL ` RVA 0x36EEEE30 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-f3b1aa145b477a9e](../../evidence/conditional_registrations-sets-003.md#r-f3b1aa145b477a9e) · [条件 C-8cad35f94624e140](../../evidence/conditions-sets-054.md#c-8cad35f94624e140) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### conditional_registration_candidates-010865

```text
(config-rtr)# no manet hello unicast <cr>
```

Handler ` RVA 0x1B088650 `；selector ` 5 `；EOL ` RVA 0x36EF0240 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-f3b1aa145b477a9e](../../evidence/conditional_registrations-sets-003.md#r-f3b1aa145b477a9e) · [条件 C-7315de189623d2a8](../../evidence/conditions-sets-045.md#c-7315de189623d2a8) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-0bb68758c1ac87ba](../../evidence/state_effects-sets-003.md#s-0bb68758c1ac87ba)

### conditional_registration_candidates-010867

```text
(config-rtr)# no manet peering selective <cr>
```

Handler ` RVA 0x1B088650 `；selector ` 4 `；EOL ` RVA 0x36EEFDD8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-f3b1aa145b477a9e](../../evidence/conditional_registrations-sets-003.md#r-f3b1aa145b477a9e) · [条件 C-7315de189623d2a8](../../evidence/conditions-sets-045.md#c-7315de189623d2a8) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### conditional_registration_candidates-010861

```text
(config-rtr)# no manet timers ackwait <cr>
```

Handler ` RVA 0x1B0895B0 `；selector ` 0 `；EOL ` RVA 0x36EEF888 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-f3b1aa145b477a9e](../../evidence/conditional_registrations-sets-003.md#r-f3b1aa145b477a9e) · [条件 C-97f01eff0f016cc6](../../evidence/conditions-sets-059.md#c-97f01eff0f016cc6) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-a1f1e1873e906988](../../evidence/state_effects-sets-034.md#s-a1f1e1873e906988)

### conditional_registration_candidates-010843

```text
(config-rtr)# no manet willingness <cr>
```

Handler ` RVA 0x1B088650 `；selector ` 3 `；EOL ` RVA 0x36EEF4C0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-f3b1aa145b477a9e](../../evidence/conditional_registrations-sets-003.md#r-f3b1aa145b477a9e) · [条件 C-a235b65734216d86](../../evidence/conditions-sets-063.md#c-a235b65734216d86) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### conditional_registration_candidates-010811

```text
(config-rtr)# no nsr <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 21 `；EOL ` RVA 0x36771250 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-457ce8e189c6074d](../../evidence/conditional_registrations-sets-001.md#r-457ce8e189c6074d) · [条件 C-837cb51a3e942acd](../../evidence/conditions-sets-051.md#c-837cb51a3e942acd) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### conditional_registration_candidates-010802

```text
(config-rtr)# no ocp <cr>
```

Handler ` RVA 0x1854F060 `；selector ` 27 `；EOL ` RVA 0x36776080 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-fdfa329a529f9703](../../evidence/conditions-sets-098.md#c-fdfa329a529f9703) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### conditional_registration_candidates-010787

```text
(config-rtr)# no preference <cr>
```

Handler ` RVA 0x1854F3F0 `；selector ` 14 `；EOL ` RVA 0x3677AAC8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-1a22dc6d428efc81](../../evidence/conditions-sets-010.md#c-1a22dc6d428efc81) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### conditional_registration_candidates-010831

```text
(config-rtr)# no probe count <cr>
```

Handler ` RVA 0x1854F3F0 `；selector ` 21 `；EOL ` RVA 0x36777970 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-7c7836c358e7b5b9](../../evidence/conditions-sets-048.md#c-7c7836c358e7b5b9) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### conditional_registration_candidates-010823

```text
(config-rtr)# no probe interval <cr>
```

Handler ` RVA 0x1854F3F0 `；selector ` 20 `；EOL ` RVA 0x36777620 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-3523e8b57ed90c02](../../evidence/conditions-sets-021.md#c-3523e8b57ed90c02) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### conditional_registration_candidates-010838

```text
(config-rtr)# no probe payload <cr>
```

Handler ` RVA 0x1854F3F0 `；selector ` 22 `；EOL ` RVA 0x36777C98 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-2e2e9e42418568e0](../../evidence/conditions-sets-018.md#c-2e2e9e42418568e0) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### conditional_registration_candidates-010835

```text
(config-rtr)# no rank maximum-increase <cr>
```

Handler ` RVA 0x1854F3F0 `；selector ` 32 `；EOL ` RVA 0x3677BEF8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-21f978d0d5beec9a](../../evidence/conditions-sets-013.md#c-21f978d0d5beec9a) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### conditional_registration_candidates-010800

```text
(config-rtr)# no send-dis <cr>
```

Handler ` RVA 0x1854F3F0 `；selector ` 30 `；EOL ` RVA 0x36776440 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-bb16146841475736](../../evidence/conditions-sets-072.md#c-bb16146841475736) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### conditional_registration_candidates-010807

```text
(config-rtr)# no step-of-rank <cr>
```

Handler ` RVA 0x1854F3F0 `；selector ` 37 `；EOL ` RVA 0x36777178 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-2019661fe55b7fb6](../../evidence/conditions-sets-013.md#c-2019661fe55b7fb6) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### conditional_registration_candidates-010868

```text
(config-rtr)# no timers manet ackwait <cr>
```

Handler ` RVA 0x1B0895B0 `；selector ` 0 `；EOL ` RVA 0x36EF1430 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-79d83dfe57d9f285](../../evidence/conditional_registrations-sets-002.md#r-79d83dfe57d9f285) · [条件 C-44de93f64a79c81f](../../evidence/conditions-sets-027.md#c-44de93f64a79c81f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-d27f81c606b6652a](../../evidence/state_effects-sets-045.md#s-d27f81c606b6652a)

### conditional_registration_candidates-010824

```text
(config-rtr)# no trickle-timer doubling <cr>
```

Handler ` RVA 0x1854F3F0 `；selector ` 16 `；EOL ` RVA 0x3677B1D0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-28be30b0379a58f5](../../evidence/conditions-sets-016.md#c-28be30b0379a58f5) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### conditional_registration_candidates-010818

```text
(config-rtr)# no trickle-timer minimum <cr>
```

Handler ` RVA 0x1854F3F0 `；selector ` 15 `；EOL ` RVA 0x3677AE80 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-e715b23d806f1262](../../evidence/conditions-sets-089.md#c-e715b23d806f1262) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### conditional_registration_candidates-010832

```text
(config-rtr)# no trickle-timer redundancy-count <cr>
```

Handler ` RVA 0x1854F3F0 `；selector ` 17 `；EOL ` RVA 0x3677B4F8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-f0957925b5319396](../../evidence/conditions-sets-093.md#c-f0957925b5319396) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### conditional_registration_candidates-010782

```text
(config-rtr)# nsr <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 21 `；EOL ` RVA 0x36771250 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-457ce8e189c6074d](../../evidence/conditional_registrations-sets-001.md#r-457ce8e189c6074d) · [条件 C-837cb51a3e942acd](../../evidence/conditions-sets-051.md#c-837cb51a3e942acd) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### conditional_registration_candidates-010806

```text
(config-rtr)# ocp <number:0..1> <cr>
```

Handler ` RVA 0x1854F060 `；selector ` 27 `；EOL ` RVA 0x36776080 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` &lt;ocp-value&gt;。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-e7e1487fde1cacfe](../../evidence/conditions-sets-090.md#c-e7e1487fde1cacfe) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-7d80a596db9718c7](../../evidence/parameters-sets-010.md#p-7d80a596db9718c7)

### conditional_registration_candidates-010788

```text
(config-rtr)# preference <number:0..7> <cr>
```

Handler ` RVA 0x1854F3F0 `；selector ` 14 `；EOL ` RVA 0x3677AAC8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` &lt;preference&gt;。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-d299844d3c24e6e3](../../evidence/conditions-sets-081.md#c-d299844d3c24e6e3) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-549776919b02be2d](../../evidence/parameters-sets-007.md#p-549776919b02be2d)

### conditional_registration_candidates-010833

```text
(config-rtr)# probe count <number:1..10> <cr>
```

Handler ` RVA 0x1854F3F0 `；selector ` 21 `；EOL ` RVA 0x36777970 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` &lt;probe-count&gt;。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-6efca57e7569e7d8](../../evidence/conditions-sets-043.md#c-6efca57e7569e7d8) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-688c5748074a589c](../../evidence/parameters-sets-008.md#p-688c5748074a589c)

### conditional_registration_candidates-010826

```text
(config-rtr)# probe interval <number:1..60> <cr>
```

Handler ` RVA 0x1854F3F0 `；selector ` 20 `；EOL ` RVA 0x36777620 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` &lt;probe-interval&gt;。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-02aaeb6177dad51b](../../evidence/conditions-sets-002.md#c-02aaeb6177dad51b) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-3ad48eb9d010b569](../../evidence/parameters-sets-005.md#p-3ad48eb9d010b569)

### conditional_registration_candidates-010840

```text
(config-rtr)# probe payload <number:0..100> <cr>
```

Handler ` RVA 0x1854F3F0 `；selector ` 22 `；EOL ` RVA 0x36777C98 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` &lt;probe-payload&gt;。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-75f40cfa85aec9e7](../../evidence/conditions-sets-046.md#c-75f40cfa85aec9e7) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-e1f76ce9bf2ce6d2](../../evidence/parameters-sets-017.md#p-e1f76ce9bf2ce6d2)

### conditional_registration_candidates-010839

```text
(config-rtr)# rank maximum-increase <number:0..64> <cr>
```

Handler ` RVA 0x1854F3F0 `；selector ` 32 `；EOL ` RVA 0x3677BEF8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` &lt;max-incr&gt;。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-d1b5353af6bcfe12](../../evidence/conditions-sets-081.md#c-d1b5353af6bcfe12) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-e8beae8869f376d5](../../evidence/parameters-sets-017.md#p-e8beae8869f376d5)

### conditional_registration_candidates-010781

```text
(config-rtr)# send-dis <cr>
```

Handler ` RVA 0x1854F3F0 `；selector ` 30 `；EOL ` RVA 0x36776440 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-bb16146841475736](../../evidence/conditions-sets-072.md#c-bb16146841475736) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### conditional_registration_candidates-010810

```text
(config-rtr)# step-of-rank <number:1..16> <cr>
```

Handler ` RVA 0x1854F3F0 `；selector ` 37 `；EOL ` RVA 0x36777178 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` &lt;step-of-rank-value&gt;。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-16f44f8792a7a1a1](../../evidence/conditions-sets-009.md#c-16f44f8792a7a1a1) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-2ae53647c45a367c](../../evidence/parameters-sets-004.md#p-2ae53647c45a367c)

### conditional_registration_candidates-010870

```text
(config-rtr)# timers manet ackwait <number:0..10000> <cr>
```

Handler ` RVA 0x1B0895B0 `；selector ` 0 `；EOL ` RVA 0x36EF1430 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Acknowledgement delay timer value in milliseconds。

[候选注册 R-79d83dfe57d9f285](../../evidence/conditional_registrations-sets-002.md#r-79d83dfe57d9f285) · [条件 C-840b32a7411e240c](../../evidence/conditions-sets-051.md#c-840b32a7411e240c) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-7647b41b27b6ba45](../../evidence/parameters-sets-009.md#p-7647b41b27b6ba45) · [状态效果 S-a9c0e06fe058214b](../../evidence/state_effects-sets-036.md#s-a9c0e06fe058214b)

### conditional_registration_candidates-010827

```text
(config-rtr)# trickle-timer doubling <number:1..26> <cr>
```

Handler ` RVA 0x1854F3F0 `；selector ` 16 `；EOL ` RVA 0x3677B1D0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` &lt;doubling-value&gt;。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-179ea7d73cbb498a](../../evidence/conditions-sets-009.md#c-179ea7d73cbb498a) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-e60ee4667bb182dc](../../evidence/parameters-sets-017.md#p-e60ee4667bb182dc)

### conditional_registration_candidates-010820

```text
(config-rtr)# trickle-timer minimum <number:8..26> <cr>
```

Handler ` RVA 0x1854F3F0 `；selector ` 15 `；EOL ` RVA 0x3677AE80 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` &lt;minimum-value&gt;。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-6aca19d4110e6df1](../../evidence/conditions-sets-041.md#c-6aca19d4110e6df1) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-0a91ce8eb52e7d18](../../evidence/parameters-sets-001.md#p-0a91ce8eb52e7d18)

### conditional_registration_candidates-010834

```text
(config-rtr)# trickle-timer redundancy-count <number:1..64> <cr>
```

Handler ` RVA 0x1854F3F0 `；selector ` 17 `；EOL ` RVA 0x3677B4F8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` &lt;redundancy-count&gt;。

[候选注册 R-ae1ed84ce4a3799c](../../evidence/conditional_registrations-sets-002.md#r-ae1ed84ce4a3799c) · [条件 C-62b225f5ad7c206d](../../evidence/conditions-sets-038.md#c-62b225f5ad7c206d) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-1ad04a6edce27c5c](../../evidence/parameters-sets-003.md#p-1ad04a6edce27c5c)

