# atm-bm-config · 依赖静态建槽的条件安装

[模式索引](README.md) · [总索引](../../README.md)

### static_slot_creation_candidates-003667

```text
(config-if-atm-member)# abr <number:dynamic> <number:dynamic> <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 8 `；EOL ` RVA 0x371FED20 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Peak Cell Rate(PCR) in Kbps；` unsigned_number_dynamic ` Minimum Cell Rate(MCR) in Kbps。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-d170bb6a36bad0c4](../../evidence/conditions-sets-081.md#c-d170bb6a36bad0c4) · [缺口 G-a3fcc50cedb5bfb7](../../evidence/gaps-sets-006.md#g-a3fcc50cedb5bfb7) · [参数 P-01a65a3ae42ac851](../../evidence/parameters-sets-001.md#p-01a65a3ae42ac851)

### static_slot_creation_candidates-003656

```text
(config-if-atm-member)# bump explicit <number:0..7> <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 54 `；EOL ` RVA 0x37200C50 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` precedence level。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-d792f0287ad60da4](../../evidence/conditions-sets-083.md#c-d792f0287ad60da4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-183d5cc03f26cb4b](../../evidence/parameters-sets-002.md#p-183d5cc03f26cb4b)

### static_slot_creation_candidates-003630

```text
(config-if-atm-member)# bump implicit <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 53 `；EOL ` RVA 0x37200908 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-223dd87d93ae22c3](../../evidence/conditions-sets-013.md#c-223dd87d93ae22c3) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### static_slot_creation_candidates-003626

```text
(config-if-atm-member)# bump traffic <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 52 `；EOL ` RVA 0x37200660 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-223dd87d93ae22c3](../../evidence/conditions-sets-013.md#c-223dd87d93ae22c3) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### static_slot_creation_candidates-003663

```text
(config-if-atm-member)# cbr <number:dynamic> <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 7 `；EOL ` RVA 0x371FF918 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Peak Cell Rate in Kbps。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-2fd99b5f36751505](../../evidence/conditions-sets-019.md#c-2fd99b5f36751505) · [缺口 G-1ad6ef9bcaa29b1c](../../evidence/gaps-sets-001.md#g-1ad6ef9bcaa29b1c) · [参数 P-6cb3527a83703c5a](../../evidence/parameters-sets-009.md#p-6cb3527a83703c5a)

### static_slot_creation_candidates-003604

```text
(config-if-atm-member)# class-vc <string> <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 10 `；EOL ` RVA 0x371FD438 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` ATM vc-class name to use on this VC。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-7dc484dad5f3154c](../../evidence/parameters-sets-010.md#p-7dc484dad5f3154c)

### static_slot_creation_candidates-003602

```text
(config-if-atm-member)# default <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 35 `；EOL ` RVA 0x37201FB8 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-872c952795e9eb49](../../evidence/conditions-sets-052.md#c-872c952795e9eb49) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-75c213dc9a14da5b](../../evidence/state_effects-sets-025.md#s-75c213dc9a14da5b)

### static_slot_creation_candidates-003657

```text
(config-if-atm-member)# default bump explicit <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 54 `；EOL ` RVA 0x37200C50 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-999bae3136afdc29](../../evidence/conditions-sets-059.md#c-999bae3136afdc29) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-75c213dc9a14da5b](../../evidence/state_effects-sets-025.md#s-75c213dc9a14da5b)

### static_slot_creation_candidates-003650

```text
(config-if-atm-member)# default bump implicit <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 53 `；EOL ` RVA 0x37200908 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-223dd87d93ae22c3](../../evidence/conditions-sets-013.md#c-223dd87d93ae22c3) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-75c213dc9a14da5b](../../evidence/state_effects-sets-025.md#s-75c213dc9a14da5b)

### static_slot_creation_candidates-003647

```text
(config-if-atm-member)# default bump traffic <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 52 `；EOL ` RVA 0x37200660 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-223dd87d93ae22c3](../../evidence/conditions-sets-013.md#c-223dd87d93ae22c3) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-75c213dc9a14da5b](../../evidence/state_effects-sets-025.md#s-75c213dc9a14da5b)

### static_slot_creation_candidates-003622

```text
(config-if-atm-member)# default cbr <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 7 `；EOL ` RVA 0x371FF918 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-3092764ad00722e9](../../evidence/conditions-sets-019.md#c-3092764ad00722e9) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-75c213dc9a14da5b](../../evidence/state_effects-sets-025.md#s-75c213dc9a14da5b)

### static_slot_creation_candidates-003643

```text
(config-if-atm-member)# default class-vc <string> <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 10 `；EOL ` RVA 0x371FD438 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` ATM vc-class name to use on this VC。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-7dc484dad5f3154c](../../evidence/parameters-sets-010.md#p-7dc484dad5f3154c) · [状态效果 S-75c213dc9a14da5b](../../evidence/state_effects-sets-025.md#s-75c213dc9a14da5b)

### static_slot_creation_candidates-003645

```text
(config-if-atm-member)# default inarp on <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 51 `；EOL ` RVA 0x37201550 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-97ab934515b3d359](../../evidence/conditions-sets-059.md#c-97ab934515b3d359) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-75c213dc9a14da5b](../../evidence/state_effects-sets-025.md#s-75c213dc9a14da5b)

### static_slot_creation_candidates-003631

```text
(config-if-atm-member)# default inarp-vc <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 57 `；EOL ` RVA 0x37203220 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-af2198e5f2739954](../../evidence/conditions-sets-068.md#c-af2198e5f2739954) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-75c213dc9a14da5b](../../evidence/state_effects-sets-025.md#s-75c213dc9a14da5b)

### static_slot_creation_candidates-003639

```text
(config-if-atm-member)# default max-reserved-bandwidth <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 66 `；EOL ` RVA 0x372018C0 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-4ecc8655230e4ab4](../../evidence/conditions-sets-031.md#c-4ecc8655230e4ab4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-de196b15afee6cd5](../../evidence/state_effects-sets-047.md#s-de196b15afee6cd5)

### static_slot_creation_candidates-003611

```text
(config-if-atm-member)# default multiqueue <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 33 `；EOL ` RVA 0x371FE1F0 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-f9b16deb9d2d392b](../../evidence/conditions-sets-096.md#c-f9b16deb9d2d392b) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-75c213dc9a14da5b](../../evidence/state_effects-sets-025.md#s-75c213dc9a14da5b)

### static_slot_creation_candidates-003632

```text
(config-if-atm-member)# default precedence <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 55 `；EOL ` RVA 0x37200158 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-6fe721773eaf32b4](../../evidence/conditions-sets-043.md#c-6fe721773eaf32b4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-75c213dc9a14da5b](../../evidence/state_effects-sets-025.md#s-75c213dc9a14da5b)

### static_slot_creation_candidates-003651

```text
(config-if-atm-member)# default protect group <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 50 `；EOL ` RVA 0x37200FA8 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-6f3d4f203994a4a4](../../evidence/conditions-sets-043.md#c-6f3d4f203994a4a4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-75c213dc9a14da5b](../../evidence/state_effects-sets-025.md#s-75c213dc9a14da5b)

### static_slot_creation_candidates-003653

```text
(config-if-atm-member)# default protect vc <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 49 `；EOL ` RVA 0x37201250 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-6f3d4f203994a4a4](../../evidence/conditions-sets-043.md#c-6f3d4f203994a4a4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-75c213dc9a14da5b](../../evidence/state_effects-sets-025.md#s-75c213dc9a14da5b)

### static_slot_creation_candidates-003633

```text
(config-if-atm-member)# default qos-group <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 56 `；EOL ` RVA 0x37202748 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-16bacf18b9d663d9](../../evidence/conditions-sets-009.md#c-16bacf18b9d663d9) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-75c213dc9a14da5b](../../evidence/state_effects-sets-025.md#s-75c213dc9a14da5b)

### static_slot_creation_candidates-003625

```text
(config-if-atm-member)# default queue-depth <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 72 `；EOL ` RVA 0x371FFCF0 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-93ef6d1fa3b4cc97](../../evidence/conditions-sets-057.md#c-93ef6d1fa3b4cc97) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-75c213dc9a14da5b](../../evidence/state_effects-sets-025.md#s-75c213dc9a14da5b)

### static_slot_creation_candidates-003614

```text
(config-if-atm-member)# default rx-limit <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 62 `；EOL ` RVA 0x371FDEB0 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-6905a3c16895c4be](../../evidence/conditions-sets-041.md#c-6905a3c16895c4be) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-75c213dc9a14da5b](../../evidence/state_effects-sets-025.md#s-75c213dc9a14da5b)

### static_slot_creation_candidates-003659

```text
(config-if-atm-member)# default service-policy input <string> <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 37 `；EOL ` RVA 0x37201CF0 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Policy-map name。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-91906bfbc06dbb5b](../../evidence/conditions-sets-056.md#c-91906bfbc06dbb5b) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-40f4190f47969647](../../evidence/parameters-sets-005.md#p-40f4190f47969647) · [状态效果 S-e32b669ee2bdff24](../../evidence/state_effects-sets-048.md#s-e32b669ee2bdff24)

### static_slot_creation_candidates-003606

```text
(config-if-atm-member)# default tx-limit <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 90 `；EOL ` RVA 0x371FD788 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-9e366ff270023508](../../evidence/conditions-sets-061.md#c-9e366ff270023508) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-75c213dc9a14da5b](../../evidence/state_effects-sets-025.md#s-75c213dc9a14da5b)

### static_slot_creation_candidates-003609

```text
(config-if-atm-member)# default tx-ring-limit <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 32 `；EOL ` RVA 0x371FDB38 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-2a7bf8fee9166ce5](../../evidence/conditions-sets-017.md#c-2a7bf8fee9166ce5) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-75c213dc9a14da5b](../../evidence/state_effects-sets-025.md#s-75c213dc9a14da5b)

### static_slot_creation_candidates-003615

```text
(config-if-atm-member)# default ubr <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 3 `；EOL ` RVA 0x371FE900 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-58c9db711437d98c](../../evidence/conditions-sets-035.md#c-58c9db711437d98c) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-75c213dc9a14da5b](../../evidence/state_effects-sets-025.md#s-75c213dc9a14da5b)

### static_slot_creation_candidates-003616

```text
(config-if-atm-member)# default ubr+ <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 4 `；EOL ` RVA 0x371FE550 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-f75bce75af8d6e88](../../evidence/conditions-sets-096.md#c-f75bce75af8d6e88) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-75c213dc9a14da5b](../../evidence/state_effects-sets-025.md#s-75c213dc9a14da5b)

### static_slot_creation_candidates-003618

```text
(config-if-atm-member)# default vbr-nrt <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 5 `；EOL ` RVA 0x371FF0B0 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-0e47651cc715ac10](../../evidence/conditions-sets-006.md#c-0e47651cc715ac10) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-75c213dc9a14da5b](../../evidence/state_effects-sets-025.md#s-75c213dc9a14da5b)

### static_slot_creation_candidates-003620

```text
(config-if-atm-member)# default vbr-rt <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 6 `；EOL ` RVA 0x371FF4E8 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-4ae01f406d95fe9e](../../evidence/conditions-sets-029.md#c-4ae01f406d95fe9e) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-75c213dc9a14da5b](../../evidence/state_effects-sets-025.md#s-75c213dc9a14da5b)

### static_slot_creation_candidates-003641

```text
(config-if-atm-member)# default vc-hold-queue <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 40 `；EOL ` RVA 0x37202300 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-abe8c005b7417039](../../evidence/conditions-sets-066.md#c-abe8c005b7417039) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-75c213dc9a14da5b](../../evidence/state_effects-sets-025.md#s-75c213dc9a14da5b)

### static_slot_creation_candidates-003624

```text
(config-if-atm-member)# inarp on <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 51 `；EOL ` RVA 0x37201550 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-97ab934515b3d359](../../evidence/conditions-sets-059.md#c-97ab934515b3d359) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### static_slot_creation_candidates-003600

```text
(config-if-atm-member)# inarp-vc <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 57 `；EOL ` RVA 0x37203220 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-af2198e5f2739954](../../evidence/conditions-sets-068.md#c-af2198e5f2739954) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### static_slot_creation_candidates-003603

```text
(config-if-atm-member)# max-reserved-bandwidth <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 66 `；EOL ` RVA 0x372018C0 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-4ecc8655230e4ab4](../../evidence/conditions-sets-031.md#c-4ecc8655230e4ab4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c629a043dfe87c2e](../../evidence/state_effects-sets-042.md#s-c629a043dfe87c2e)

### static_slot_creation_candidates-003598

```text
(config-if-atm-member)# multiqueue <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 33 `；EOL ` RVA 0x371FE1F0 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-f9b16deb9d2d392b](../../evidence/conditions-sets-096.md#c-f9b16deb9d2d392b) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### static_slot_creation_candidates-003601

```text
(config-if-atm-member)# no <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 35 `；EOL ` RVA 0x37201FB8 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-872c952795e9eb49](../../evidence/conditions-sets-052.md#c-872c952795e9eb49) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-a9c2ad503af98f30](../../evidence/state_effects-sets-036.md#s-a9c2ad503af98f30)

### static_slot_creation_candidates-003655

```text
(config-if-atm-member)# no bump explicit <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 54 `；EOL ` RVA 0x37200C50 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-40f6b265e1e01a5f](../../evidence/conditions-sets-025.md#c-40f6b265e1e01a5f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-a9c2ad503af98f30](../../evidence/state_effects-sets-036.md#s-a9c2ad503af98f30)

### static_slot_creation_candidates-003648

```text
(config-if-atm-member)# no bump implicit <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 53 `；EOL ` RVA 0x37200908 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-223dd87d93ae22c3](../../evidence/conditions-sets-013.md#c-223dd87d93ae22c3) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-a9c2ad503af98f30](../../evidence/state_effects-sets-036.md#s-a9c2ad503af98f30)

### static_slot_creation_candidates-003646

```text
(config-if-atm-member)# no bump traffic <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 52 `；EOL ` RVA 0x37200660 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-223dd87d93ae22c3](../../evidence/conditions-sets-013.md#c-223dd87d93ae22c3) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-a9c2ad503af98f30](../../evidence/state_effects-sets-036.md#s-a9c2ad503af98f30)

### static_slot_creation_candidates-003621

```text
(config-if-atm-member)# no cbr <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 7 `；EOL ` RVA 0x371FF918 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-6e86af7cbab0ebd7](../../evidence/conditions-sets-043.md#c-6e86af7cbab0ebd7) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-a9c2ad503af98f30](../../evidence/state_effects-sets-036.md#s-a9c2ad503af98f30)

### static_slot_creation_candidates-003642

```text
(config-if-atm-member)# no class-vc <string> <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 10 `；EOL ` RVA 0x371FD438 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` ATM vc-class name to use on this VC。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-7dc484dad5f3154c](../../evidence/parameters-sets-010.md#p-7dc484dad5f3154c) · [状态效果 S-a9c2ad503af98f30](../../evidence/state_effects-sets-036.md#s-a9c2ad503af98f30)

### static_slot_creation_candidates-003644

```text
(config-if-atm-member)# no inarp on <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 51 `；EOL ` RVA 0x37201550 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-97ab934515b3d359](../../evidence/conditions-sets-059.md#c-97ab934515b3d359) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-a9c2ad503af98f30](../../evidence/state_effects-sets-036.md#s-a9c2ad503af98f30)

### static_slot_creation_candidates-003627

```text
(config-if-atm-member)# no inarp-vc <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 57 `；EOL ` RVA 0x37203220 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-af2198e5f2739954](../../evidence/conditions-sets-068.md#c-af2198e5f2739954) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-a9c2ad503af98f30](../../evidence/state_effects-sets-036.md#s-a9c2ad503af98f30)

### static_slot_creation_candidates-003637

```text
(config-if-atm-member)# no max-reserved-bandwidth <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 66 `；EOL ` RVA 0x372018C0 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-4ecc8655230e4ab4](../../evidence/conditions-sets-031.md#c-4ecc8655230e4ab4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-2ad1939f8772fb6d](../../evidence/state_effects-sets-010.md#s-2ad1939f8772fb6d)

### static_slot_creation_candidates-003608

```text
(config-if-atm-member)# no multiqueue <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 33 `；EOL ` RVA 0x371FE1F0 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-f9b16deb9d2d392b](../../evidence/conditions-sets-096.md#c-f9b16deb9d2d392b) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-a9c2ad503af98f30](../../evidence/state_effects-sets-036.md#s-a9c2ad503af98f30)

### static_slot_creation_candidates-003628

```text
(config-if-atm-member)# no precedence <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 55 `；EOL ` RVA 0x37200158 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-036f1b49c6bc98a8](../../evidence/conditions-sets-002.md#c-036f1b49c6bc98a8) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-a9c2ad503af98f30](../../evidence/state_effects-sets-036.md#s-a9c2ad503af98f30)

### static_slot_creation_candidates-003649

```text
(config-if-atm-member)# no protect group <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 50 `；EOL ` RVA 0x37200FA8 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-6f3d4f203994a4a4](../../evidence/conditions-sets-043.md#c-6f3d4f203994a4a4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-a9c2ad503af98f30](../../evidence/state_effects-sets-036.md#s-a9c2ad503af98f30)

### static_slot_creation_candidates-003652

```text
(config-if-atm-member)# no protect vc <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 49 `；EOL ` RVA 0x37201250 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-6f3d4f203994a4a4](../../evidence/conditions-sets-043.md#c-6f3d4f203994a4a4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-a9c2ad503af98f30](../../evidence/state_effects-sets-036.md#s-a9c2ad503af98f30)

### static_slot_creation_candidates-003629

```text
(config-if-atm-member)# no qos-group <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 56 `；EOL ` RVA 0x37202748 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-12d7804a52c5269f](../../evidence/conditions-sets-007.md#c-12d7804a52c5269f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-a9c2ad503af98f30](../../evidence/state_effects-sets-036.md#s-a9c2ad503af98f30)

### static_slot_creation_candidates-003623

```text
(config-if-atm-member)# no queue-depth <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 72 `；EOL ` RVA 0x371FFCF0 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-daf5d2059387c42d](../../evidence/conditions-sets-084.md#c-daf5d2059387c42d) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-a9c2ad503af98f30](../../evidence/state_effects-sets-036.md#s-a9c2ad503af98f30)

### static_slot_creation_candidates-003610

```text
(config-if-atm-member)# no rx-limit <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 62 `；EOL ` RVA 0x371FDEB0 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-6905a3c16895c4be](../../evidence/conditions-sets-041.md#c-6905a3c16895c4be) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-a9c2ad503af98f30](../../evidence/state_effects-sets-036.md#s-a9c2ad503af98f30)

### static_slot_creation_candidates-003658

```text
(config-if-atm-member)# no service-policy input <string> <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 37 `；EOL ` RVA 0x37201CF0 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Policy-map name。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-91906bfbc06dbb5b](../../evidence/conditions-sets-056.md#c-91906bfbc06dbb5b) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-40f4190f47969647](../../evidence/parameters-sets-005.md#p-40f4190f47969647) · [状态效果 S-f55627d3ae514bab](../../evidence/state_effects-sets-052.md#s-f55627d3ae514bab)

### static_slot_creation_candidates-003605

```text
(config-if-atm-member)# no tx-limit <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 90 `；EOL ` RVA 0x371FD788 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-f7b747c9f8e7732b](../../evidence/conditions-sets-096.md#c-f7b747c9f8e7732b) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-a9c2ad503af98f30](../../evidence/state_effects-sets-036.md#s-a9c2ad503af98f30)

### static_slot_creation_candidates-003607

```text
(config-if-atm-member)# no tx-ring-limit <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 32 `；EOL ` RVA 0x371FDB38 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-2a7bf8fee9166ce5](../../evidence/conditions-sets-017.md#c-2a7bf8fee9166ce5) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-a9c2ad503af98f30](../../evidence/state_effects-sets-036.md#s-a9c2ad503af98f30)

### static_slot_creation_candidates-003612

```text
(config-if-atm-member)# no ubr <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 3 `；EOL ` RVA 0x371FE900 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-42a626c440d26e97](../../evidence/conditions-sets-026.md#c-42a626c440d26e97) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-a9c2ad503af98f30](../../evidence/state_effects-sets-036.md#s-a9c2ad503af98f30)

### static_slot_creation_candidates-003613

```text
(config-if-atm-member)# no ubr+ <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 4 `；EOL ` RVA 0x371FE550 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-4b680a95a0cb470b](../../evidence/conditions-sets-030.md#c-4b680a95a0cb470b) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-a9c2ad503af98f30](../../evidence/state_effects-sets-036.md#s-a9c2ad503af98f30)

### static_slot_creation_candidates-003617

```text
(config-if-atm-member)# no vbr-nrt <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 5 `；EOL ` RVA 0x371FF0B0 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-1377073835a5ae39](../../evidence/conditions-sets-008.md#c-1377073835a5ae39) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-a9c2ad503af98f30](../../evidence/state_effects-sets-036.md#s-a9c2ad503af98f30)

### static_slot_creation_candidates-003619

```text
(config-if-atm-member)# no vbr-rt <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 6 `；EOL ` RVA 0x371FF4E8 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-aa82a46cb5fa5f49](../../evidence/conditions-sets-066.md#c-aa82a46cb5fa5f49) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-a9c2ad503af98f30](../../evidence/state_effects-sets-036.md#s-a9c2ad503af98f30)

### static_slot_creation_candidates-003638

```text
(config-if-atm-member)# no vc-hold-queue <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 40 `；EOL ` RVA 0x37202300 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-6af81cba7135fcb2](../../evidence/conditions-sets-041.md#c-6af81cba7135fcb2) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-a9c2ad503af98f30](../../evidence/state_effects-sets-036.md#s-a9c2ad503af98f30)

### static_slot_creation_candidates-003665

```text
(config-if-atm-member)# precedence <number:0..7> <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 55 `；EOL ` RVA 0x37200158 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` precedence or mpls experimental level。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-f6b3fb3e400e477f](../../evidence/conditions-sets-095.md#c-f6b3fb3e400e477f) · [缺口 G-37e812d36720276a](../../evidence/gaps-sets-002.md#g-37e812d36720276a) · [参数 P-85a28d5dbbe40a6e](../../evidence/parameters-sets-010.md#p-85a28d5dbbe40a6e) · [状态效果 S-e539c210513500dd](../../evidence/state_effects-sets-048.md#s-e539c210513500dd)

### static_slot_creation_candidates-003635

```text
(config-if-atm-member)# precedence other <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 55 `；EOL ` RVA 0x37200158 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-f6b3fb3e400e477f](../../evidence/conditions-sets-095.md#c-f6b3fb3e400e477f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-7bd61ce4f6d9cb45](../../evidence/state_effects-sets-026.md#s-7bd61ce4f6d9cb45)

### static_slot_creation_candidates-003634

```text
(config-if-atm-member)# protect group <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 50 `；EOL ` RVA 0x37200FA8 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-6f3d4f203994a4a4](../../evidence/conditions-sets-043.md#c-6f3d4f203994a4a4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### static_slot_creation_candidates-003636

```text
(config-if-atm-member)# protect vc <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 49 `；EOL ` RVA 0x37201250 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-6f3d4f203994a4a4](../../evidence/conditions-sets-043.md#c-6f3d4f203994a4a4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### static_slot_creation_candidates-003664

```text
(config-if-atm-member)# qos-group other <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 56 `；EOL ` RVA 0x37202748 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-ff73910308d31c96](../../evidence/conditions-sets-098.md#c-ff73910308d31c96) · [缺口 G-2ee6efdaf73bea02](../../evidence/gaps-sets-002.md#g-2ee6efdaf73bea02) · [状态效果 S-532475028f06e819](../../evidence/state_effects-sets-018.md#s-532475028f06e819)

### static_slot_creation_candidates-003670

```text
(config-if-atm-member)# queue-depth <number:dynamic> <number:dynamic> <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 72 `；EOL ` RVA 0x371FFCF0 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` queue depth high watermark, in cells；` unsigned_number_dynamic ` queue depth low watermark, in cells。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-32e32ea582e0dd5b](../../evidence/conditions-sets-020.md#c-32e32ea582e0dd5b) · [缺口 G-703aef2c75baf519](../../evidence/gaps-sets-004.md#g-703aef2c75baf519) · [参数 P-11e0f5960a09492a](../../evidence/parameters-sets-002.md#p-11e0f5960a09492a)

### static_slot_creation_candidates-003599

```text
(config-if-atm-member)# rx-limit <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 62 `；EOL ` RVA 0x371FDEB0 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-6905a3c16895c4be](../../evidence/conditions-sets-041.md#c-6905a3c16895c4be) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### static_slot_creation_candidates-003654

```text
(config-if-atm-member)# service-policy input <string> <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 37 `；EOL ` RVA 0x37201CF0 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Policy-map name。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-91906bfbc06dbb5b](../../evidence/conditions-sets-056.md#c-91906bfbc06dbb5b) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-40f4190f47969647](../../evidence/parameters-sets-005.md#p-40f4190f47969647) · [状态效果 S-ae0e322c15a61618](../../evidence/state_effects-sets-037.md#s-ae0e322c15a61618)

### static_slot_creation_candidates-003661

```text
(config-if-atm-member)# tx-limit <number:dynamic> <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 90 `；EOL ` RVA 0x371FD788 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Number of tx buffers for this VC。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-730a8813a7b8cdfc](../../evidence/conditions-sets-044.md#c-730a8813a7b8cdfc) · [缺口 G-66a83e4f017aa70d](../../evidence/gaps-sets-004.md#g-66a83e4f017aa70d) · [参数 P-d357aa8d908ac1da](../../evidence/parameters-sets-016.md#p-d357aa8d908ac1da)

### static_slot_creation_candidates-003597

```text
(config-if-atm-member)# tx-ring-limit <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 32 `；EOL ` RVA 0x371FDB38 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-2a7bf8fee9166ce5](../../evidence/conditions-sets-017.md#c-2a7bf8fee9166ce5) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### static_slot_creation_candidates-003660

```text
(config-if-atm-member)# tx-ring-limit <number:dynamic> <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 32 `；EOL ` RVA 0x371FDB38 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Number (ring limit)。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-3a5ea646783c677d](../../evidence/conditions-sets-023.md#c-3a5ea646783c677d) · [缺口 G-4a7776bffbf479fc](../../evidence/gaps-sets-003.md#g-4a7776bffbf479fc) · [参数 P-2bd08e564ef00a8a](../../evidence/parameters-sets-004.md#p-2bd08e564ef00a8a)

### static_slot_creation_candidates-003662

```text
(config-if-atm-member)# ubr <number:dynamic> <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 3 `；EOL ` RVA 0x371FE900 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Peak Cell Rate(PCR) in Kbps。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-224e08d130d7e41f](../../evidence/conditions-sets-013.md#c-224e08d130d7e41f) · [缺口 G-117531eeeb4276de](../../evidence/gaps-sets-001.md#g-117531eeeb4276de) · [参数 P-44b26355289a8235](../../evidence/parameters-sets-006.md#p-44b26355289a8235)

### static_slot_creation_candidates-003666

```text
(config-if-atm-member)# ubr+ <number:dynamic> <number:dynamic> <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 4 `；EOL ` RVA 0x371FE550 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Peak Cell Rate(PCR) in Kbps；` unsigned_number_dynamic ` Minimum Guaranteed Cell Rate(MCR) in Kbps。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-aa10f4a7b6033812](../../evidence/conditions-sets-066.md#c-aa10f4a7b6033812) · [缺口 G-1685bfb594a2b170](../../evidence/gaps-sets-001.md#g-1685bfb594a2b170) · [参数 P-984f7e4173782e08](../../evidence/parameters-sets-012.md#p-984f7e4173782e08)

### static_slot_creation_candidates-003668

```text
(config-if-atm-member)# vbr-nrt <number:dynamic> <number:dynamic> <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 5 `；EOL ` RVA 0x371FF0B0 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Peak Cell Rate(PCR) in Kbps；` unsigned_number_dynamic ` Sustainable Cell Rate(SCR) in Kbps。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-d2bd9fd65da92893](../../evidence/conditions-sets-081.md#c-d2bd9fd65da92893) · [缺口 G-23f0f355846163a7](../../evidence/gaps-sets-002.md#g-23f0f355846163a7) · [参数 P-93ae02e58a3aead8](../../evidence/parameters-sets-011.md#p-93ae02e58a3aead8)

### static_slot_creation_candidates-003669

```text
(config-if-atm-member)# vbr-rt <number:dynamic> <number:dynamic> <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 6 `；EOL ` RVA 0x371FF4E8 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Peak Cell Rate(PCR) in Kbps；` unsigned_number_dynamic ` Average Cell Rate in Kbps。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-a546252177332a83](../../evidence/conditions-sets-064.md#c-a546252177332a83) · [缺口 G-fe9b976d8757b1b6](../../evidence/gaps-sets-009.md#g-fe9b976d8757b1b6) · [参数 P-e1c90f3c671ca025](../../evidence/parameters-sets-017.md#p-e1c90f3c671ca025)

### static_slot_creation_candidates-003640

```text
(config-if-atm-member)# vc-hold-queue <number:5..1024> <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 40 `；EOL ` RVA 0x37202300 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Value of the hold queue size。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-fd9e6251aaf8e198](../../evidence/conditions-sets-098.md#c-fd9e6251aaf8e198) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-dc5bc940d34a1c90](../../evidence/parameters-sets-017.md#p-dc5bc940d34a1c90)

### static_slot_creation_candidates-003596

```text
(config-if-atm-member)# <cr>
```

Handler ` RVA 0x1BF93940 `；selector ` 35 `；EOL ` RVA 0x37201FB8 `。

模式根 ` RVA 0x371F5648 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-7637673f7edc66f9](../../evidence/conditional_registrations-sets-002.md#r-7637673f7edc66f9) · [条件 C-872c952795e9eb49](../../evidence/conditions-sets-052.md#c-872c952795e9eb49) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

