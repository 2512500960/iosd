# template · 已捕获槽位上的条件安装

[模式索引](README.md) · [总索引](../../README.md)

### conditional_registration_candidates-011017

```text
(config-template)# aaa session-mib disconnect <cr>
```

Handler ` RVA 0x1B13BFA0 `；selector ` 0 `；EOL ` RVA 0x36F02618 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-b7bc10c4d3aba4b7](../../evidence/conditional_registrations-sets-002.md#r-b7bc10c4d3aba4b7) · [条件 C-d99f5772c5fd88c5](../../evidence/conditions-sets-084.md#c-d99f5772c5fd88c5) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### conditional_registration_candidates-011030

```text
(config-template)# aaa session-mib populate start <cr>
```

Handler ` RVA 0x1B13C060 `；selector ` 0 `；EOL ` RVA 0x36F02900 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-b7bc10c4d3aba4b7](../../evidence/conditional_registrations-sets-002.md#r-b7bc10c4d3aba4b7) · [条件 C-d99f5772c5fd88c5](../../evidence/conditions-sets-084.md#c-d99f5772c5fd88c5) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-ba6fdf7a76085007](../../evidence/state_effects-sets-039.md#s-ba6fdf7a76085007)

### conditional_registration_candidates-011029

```text
(config-template)# default aaa session-mib disconnect <cr>
```

Handler ` RVA 0x1B13BFA0 `；selector ` 0 `；EOL ` RVA 0x36F02618 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-b7bc10c4d3aba4b7](../../evidence/conditional_registrations-sets-002.md#r-b7bc10c4d3aba4b7) · [条件 C-d99f5772c5fd88c5](../../evidence/conditions-sets-084.md#c-d99f5772c5fd88c5) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-8f20c6f8152a82e1](../../evidence/state_effects-sets-030.md#s-8f20c6f8152a82e1)

### conditional_registration_candidates-011037

```text
(config-template)# default aaa session-mib populate start <cr>
```

Handler ` RVA 0x1B13C060 `；selector ` 0 `；EOL ` RVA 0x36F02900 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-b7bc10c4d3aba4b7](../../evidence/conditional_registrations-sets-002.md#r-b7bc10c4d3aba4b7) · [条件 C-d99f5772c5fd88c5](../../evidence/conditions-sets-084.md#c-d99f5772c5fd88c5) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-b1bf97831e8bf055](../../evidence/state_effects-sets-038.md#s-b1bf97831e8bf055)

### conditional_registration_candidates-011041

```text
(config-template)# default ip inspect <string> in <cr>
```

Handler ` RVA 0x16A451A0 `；selector ` 120 `；EOL ` RVA 0x36075AE8 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Name of inspection defined。

[候选注册 R-15d56c64aef2d583](../../evidence/conditional_registrations-sets-001.md#r-15d56c64aef2d583) · [条件 C-0fc38b8887b4eea7](../../evidence/conditions-sets-006.md#c-0fc38b8887b4eea7) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-36dac899c1a11b63](../../evidence/parameters-sets-005.md#p-36dac899c1a11b63) · [状态效果 S-40b386c53e159ff3](../../evidence/state_effects-sets-014.md#s-40b386c53e159ff3)

### conditional_registration_candidates-011039

```text
(config-template)# default ip media-pool <address> <address> <cr>
```

Handler ` RVA 0x1D583FD0 `；selector ` 0 `；EOL ` RVA 0x3759D118 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` Starting IPv4 media address；` address ` Ending IPv4 media address。

[候选注册 R-8e79e6bf2b224962](../../evidence/conditional_registrations-sets-002.md#r-8e79e6bf2b224962) · [条件 C-0fc38b8887b4eea7](../../evidence/conditions-sets-006.md#c-0fc38b8887b4eea7) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-21a8823b3e57578a](../../evidence/parameters-sets-003.md#p-21a8823b3e57578a) · [状态效果 S-c05dbc159733d9f8](../../evidence/state_effects-sets-041.md#s-c05dbc159733d9f8)

### conditional_registration_candidates-011034

```text
(config-template)# default ip mobile arp <cr>
```

Handler ` RVA 0x193EC6D0 `；selector ` 0 `；EOL ` RVA 0x369E0040 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-35d910da6c18cad2](../../evidence/conditional_registrations-sets-001.md#r-35d910da6c18cad2) · [条件 C-f2992048ee270dda](../../evidence/conditions-sets-094.md#c-f2992048ee270dda) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-52e838fd658a0a53](../../evidence/state_effects-sets-018.md#s-52e838fd658a0a53)

### conditional_registration_candidates-011043

```text
(config-template)# default ip mobile router-service roam <cr>
```

Handler ` RVA 0x1944F080 `；selector ` 0 `；EOL ` RVA 0x369E06A8 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-35d910da6c18cad2](../../evidence/conditional_registrations-sets-001.md#r-35d910da6c18cad2) · [条件 C-8219e1c3951581e2](../../evidence/conditions-sets-050.md#c-8219e1c3951581e2) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-e05fe3894cf78729](../../evidence/state_effects-sets-047.md#s-e05fe3894cf78729)

### conditional_registration_candidates-011009

```text
(config-template)# default spanning-tree <cr>
```

Handler ` RVA 0x17496930 `；selector ` 15 `；EOL ` RVA 0x363EBBF8 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-711556eec5af8b46](../../evidence/conditional_registrations-sets-001.md#r-711556eec5af8b46) · [条件 C-0fc945488fa6910c](../../evidence/conditions-sets-006.md#c-0fc945488fa6910c) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-8f20c6f8152a82e1](../../evidence/state_effects-sets-030.md#s-8f20c6f8152a82e1)

### conditional_registration_candidates-011020

```text
(config-template)# default spanning-tree bpdufilter <cr>
```

Handler ` RVA 0x17496930 `；selector ` 12 `；EOL ` RVA 0x363EB060 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-711556eec5af8b46](../../evidence/conditional_registrations-sets-001.md#r-711556eec5af8b46) · [条件 C-37e45e0a25aad04e](../../evidence/conditions-sets-022.md#c-37e45e0a25aad04e) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-cdcdb173f19e0607](../../evidence/state_effects-sets-044.md#s-cdcdb173f19e0607)

### conditional_registration_candidates-011024

```text
(config-template)# default spanning-tree bpduguard <cr>
```

Handler ` RVA 0x17496930 `；selector ` 11 `；EOL ` RVA 0x363EB458 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-711556eec5af8b46](../../evidence/conditional_registrations-sets-001.md#r-711556eec5af8b46) · [条件 C-b1ababbbe13393ec](../../evidence/conditions-sets-069.md#c-b1ababbbe13393ec) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-10a9ee471e7f1e3e](../../evidence/state_effects-sets-004.md#s-10a9ee471e7f1e3e)

### conditional_registration_candidates-011012

```text
(config-template)# default spanning-tree cost <cr>
```

Handler ` RVA 0x17496930 `；selector ` 3 `；EOL ` RVA 0x363E6958 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-711556eec5af8b46](../../evidence/conditional_registrations-sets-001.md#r-711556eec5af8b46) · [条件 C-31b656e25076f728](../../evidence/conditions-sets-019.md#c-31b656e25076f728) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-8f20c6f8152a82e1](../../evidence/state_effects-sets-030.md#s-8f20c6f8152a82e1)

### conditional_registration_candidates-011023

```text
(config-template)# default spanning-tree link-type <cr>
```

Handler ` RVA 0x17496930 `；selector ` 9 `；EOL ` RVA 0x363EB800 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-711556eec5af8b46](../../evidence/conditional_registrations-sets-001.md#r-711556eec5af8b46) · [条件 C-927e88f56ea2b042](../../evidence/conditions-sets-056.md#c-927e88f56ea2b042) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-8f20c6f8152a82e1](../../evidence/state_effects-sets-030.md#s-8f20c6f8152a82e1)

### conditional_registration_candidates-011026

```text
(config-template)# default spanning-tree port-priority <cr>
```

Handler ` RVA 0x17496930 `；selector ` 4 `；EOL ` RVA 0x363E69F8 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-711556eec5af8b46](../../evidence/conditional_registrations-sets-001.md#r-711556eec5af8b46) · [条件 C-f850cd0804abb9b4](../../evidence/conditions-sets-096.md#c-f850cd0804abb9b4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-8f20c6f8152a82e1](../../evidence/state_effects-sets-030.md#s-8f20c6f8152a82e1)

### conditional_registration_candidates-011014

```text
(config-template)# default spanning-tree portfast <cr>
```

Handler ` RVA 0x17496930 `；selector ` 1 `；EOL ` RVA 0x363EAAE0 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-711556eec5af8b46](../../evidence/conditional_registrations-sets-001.md#r-711556eec5af8b46) · [条件 C-90d3577c48f84f3c](../../evidence/conditions-sets-056.md#c-90d3577c48f84f3c) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-48f2e8bc9b56f1d3](../../evidence/state_effects-sets-016.md#s-48f2e8bc9b56f1d3)

### conditional_registration_candidates-011044

```text
(config-template)# ip flow egress <cr>
```

Handler ` RVA 0x10BD9030 `；selector ` 0 `；EOL ` RVA 0x34CD2FC8 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[候选注册 R-d9537b3caa9ca0b2](../../evidence/conditional_registrations-sets-002.md#r-d9537b3caa9ca0b2) · [条件 C-816bc21178b615bf](../../evidence/conditions-sets-050.md#c-816bc21178b615bf) · [缺口 G-adeed7d022b34bfb](../../evidence/gaps-sets-006.md#g-adeed7d022b34bfb) · [状态效果 S-3727c8a0b4eff033](../../evidence/state_effects-sets-012.md#s-3727c8a0b4eff033)

### conditional_registration_candidates-011045

```text
(config-template)# ip flow ingress <cr>
```

Handler ` RVA 0x10BD8F30 `；selector ` 0 `；EOL ` RVA 0x34CD57A0 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[候选注册 R-d9537b3caa9ca0b2](../../evidence/conditional_registrations-sets-002.md#r-d9537b3caa9ca0b2) · [条件 C-816bc21178b615bf](../../evidence/conditions-sets-050.md#c-816bc21178b615bf) · [缺口 G-faa21daf91cc6168](../../evidence/gaps-sets-009.md#g-faa21daf91cc6168) · [状态效果 S-6f26ab3a670161ae](../../evidence/state_effects-sets-024.md#s-6f26ab3a670161ae)

### conditional_registration_candidates-011033

```text
(config-template)# ip inspect <string> in <cr>
```

Handler ` RVA 0x16A451A0 `；selector ` 120 `；EOL ` RVA 0x36075AE8 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of inspection defined。

[候选注册 R-15d56c64aef2d583](../../evidence/conditional_registrations-sets-001.md#r-15d56c64aef2d583) · [条件 C-0fc38b8887b4eea7](../../evidence/conditions-sets-006.md#c-0fc38b8887b4eea7) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-36dac899c1a11b63](../../evidence/parameters-sets-005.md#p-36dac899c1a11b63) · [状态效果 S-056d2cdac298f83b](../../evidence/state_effects-sets-002.md#s-056d2cdac298f83b)

### conditional_registration_candidates-011031

```text
(config-template)# ip media-pool <address> <address> <cr>
```

Handler ` RVA 0x1D583FD0 `；selector ` 0 `；EOL ` RVA 0x3759D118 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Starting IPv4 media address；` address ` Ending IPv4 media address。

[候选注册 R-8e79e6bf2b224962](../../evidence/conditional_registrations-sets-002.md#r-8e79e6bf2b224962) · [条件 C-0fc38b8887b4eea7](../../evidence/conditions-sets-006.md#c-0fc38b8887b4eea7) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-21a8823b3e57578a](../../evidence/parameters-sets-003.md#p-21a8823b3e57578a) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### conditional_registration_candidates-011027

```text
(config-template)# ip mobile prefix-length <cr>
```

Handler ` RVA 0x193EC6D0 `；selector ` 0 `；EOL ` RVA 0x369E0040 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-35d910da6c18cad2](../../evidence/conditional_registrations-sets-001.md#r-35d910da6c18cad2) · [条件 C-8219e1c3951581e2](../../evidence/conditions-sets-050.md#c-8219e1c3951581e2) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-25899580d6e0d22b](../../evidence/state_effects-sets-008.md#s-25899580d6e0d22b)

### conditional_registration_candidates-011035

```text
(config-template)# ip mobile router-service roam <cr>
```

Handler ` RVA 0x1944F080 `；selector ` 0 `；EOL ` RVA 0x369E06A8 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-35d910da6c18cad2](../../evidence/conditional_registrations-sets-001.md#r-35d910da6c18cad2) · [条件 C-8219e1c3951581e2](../../evidence/conditions-sets-050.md#c-8219e1c3951581e2) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-3337cc5ce03d055e](../../evidence/state_effects-sets-011.md#s-3337cc5ce03d055e)

### conditional_registration_candidates-011028

```text
(config-template)# no aaa session-mib disconnect <cr>
```

Handler ` RVA 0x1B13BFA0 `；selector ` 0 `；EOL ` RVA 0x36F02618 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-b7bc10c4d3aba4b7](../../evidence/conditional_registrations-sets-002.md#r-b7bc10c4d3aba4b7) · [条件 C-d99f5772c5fd88c5](../../evidence/conditions-sets-084.md#c-d99f5772c5fd88c5) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-75c356b17da2c4f1](../../evidence/state_effects-sets-025.md#s-75c356b17da2c4f1)

### conditional_registration_candidates-011036

```text
(config-template)# no aaa session-mib populate start <cr>
```

Handler ` RVA 0x1B13C060 `；selector ` 0 `；EOL ` RVA 0x36F02900 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-b7bc10c4d3aba4b7](../../evidence/conditional_registrations-sets-002.md#r-b7bc10c4d3aba4b7) · [条件 C-d99f5772c5fd88c5](../../evidence/conditions-sets-084.md#c-d99f5772c5fd88c5) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-bd0628145ca94f21](../../evidence/state_effects-sets-040.md#s-bd0628145ca94f21)

### conditional_registration_candidates-011040

```text
(config-template)# no ip inspect <string> in <cr>
```

Handler ` RVA 0x16A451A0 `；selector ` 120 `；EOL ` RVA 0x36075AE8 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Name of inspection defined。

[候选注册 R-15d56c64aef2d583](../../evidence/conditional_registrations-sets-001.md#r-15d56c64aef2d583) · [条件 C-0fc38b8887b4eea7](../../evidence/conditions-sets-006.md#c-0fc38b8887b4eea7) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-36dac899c1a11b63](../../evidence/parameters-sets-005.md#p-36dac899c1a11b63) · [状态效果 S-b15af0d12b578fb1](../../evidence/state_effects-sets-038.md#s-b15af0d12b578fb1)

### conditional_registration_candidates-011038

```text
(config-template)# no ip media-pool <address> <address> <cr>
```

Handler ` RVA 0x1D583FD0 `；selector ` 0 `；EOL ` RVA 0x3759D118 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` Starting IPv4 media address；` address ` Ending IPv4 media address。

[候选注册 R-8e79e6bf2b224962](../../evidence/conditional_registrations-sets-002.md#r-8e79e6bf2b224962) · [条件 C-0fc38b8887b4eea7](../../evidence/conditions-sets-006.md#c-0fc38b8887b4eea7) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-21a8823b3e57578a](../../evidence/parameters-sets-003.md#p-21a8823b3e57578a) · [状态效果 S-c9dacd4be143ae27](../../evidence/state_effects-sets-043.md#s-c9dacd4be143ae27)

### conditional_registration_candidates-011032

```text
(config-template)# no ip mobile arp <cr>
```

Handler ` RVA 0x193EC6D0 `；selector ` 0 `；EOL ` RVA 0x369E0040 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-35d910da6c18cad2](../../evidence/conditional_registrations-sets-001.md#r-35d910da6c18cad2) · [条件 C-8689ef8498caa62a](../../evidence/conditions-sets-052.md#c-8689ef8498caa62a) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-f1d4c2cd01538eef](../../evidence/state_effects-sets-051.md#s-f1d4c2cd01538eef)

### conditional_registration_candidates-011042

```text
(config-template)# no ip mobile router-service roam <cr>
```

Handler ` RVA 0x1944F080 `；selector ` 0 `；EOL ` RVA 0x369E06A8 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-35d910da6c18cad2](../../evidence/conditional_registrations-sets-001.md#r-35d910da6c18cad2) · [条件 C-8219e1c3951581e2](../../evidence/conditions-sets-050.md#c-8219e1c3951581e2) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-b148d78c081093f2](../../evidence/state_effects-sets-038.md#s-b148d78c081093f2)

### conditional_registration_candidates-011008

```text
(config-template)# no spanning-tree <cr>
```

Handler ` RVA 0x17496930 `；selector ` 15 `；EOL ` RVA 0x363EBBF8 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-711556eec5af8b46](../../evidence/conditional_registrations-sets-001.md#r-711556eec5af8b46) · [条件 C-0fc945488fa6910c](../../evidence/conditions-sets-006.md#c-0fc945488fa6910c) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-75c356b17da2c4f1](../../evidence/state_effects-sets-025.md#s-75c356b17da2c4f1)

### conditional_registration_candidates-011016

```text
(config-template)# no spanning-tree bpdufilter <cr>
```

Handler ` RVA 0x17496930 `；selector ` 12 `；EOL ` RVA 0x363EB060 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-711556eec5af8b46](../../evidence/conditional_registrations-sets-001.md#r-711556eec5af8b46) · [条件 C-969c5fe303d57b71](../../evidence/conditions-sets-058.md#c-969c5fe303d57b71) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-77014633f29235fa](../../evidence/state_effects-sets-025.md#s-77014633f29235fa)

### conditional_registration_candidates-011021

```text
(config-template)# no spanning-tree bpduguard <cr>
```

Handler ` RVA 0x17496930 `；selector ` 11 `；EOL ` RVA 0x363EB458 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-711556eec5af8b46](../../evidence/conditional_registrations-sets-001.md#r-711556eec5af8b46) · [条件 C-f656dc7fca2cc651](../../evidence/conditions-sets-095.md#c-f656dc7fca2cc651) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-61303208cd872f21](../../evidence/state_effects-sets-021.md#s-61303208cd872f21)

### conditional_registration_candidates-011011

```text
(config-template)# no spanning-tree cost <cr>
```

Handler ` RVA 0x17496930 `；selector ` 3 `；EOL ` RVA 0x363E6958 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-711556eec5af8b46](../../evidence/conditional_registrations-sets-001.md#r-711556eec5af8b46) · [条件 C-31b656e25076f728](../../evidence/conditions-sets-019.md#c-31b656e25076f728) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-75c356b17da2c4f1](../../evidence/state_effects-sets-025.md#s-75c356b17da2c4f1)

### conditional_registration_candidates-011019

```text
(config-template)# no spanning-tree link-type <cr>
```

Handler ` RVA 0x17496930 `；selector ` 9 `；EOL ` RVA 0x363EB800 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-711556eec5af8b46](../../evidence/conditional_registrations-sets-001.md#r-711556eec5af8b46) · [条件 C-479971a140ed9e96](../../evidence/conditions-sets-028.md#c-479971a140ed9e96) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-75c356b17da2c4f1](../../evidence/state_effects-sets-025.md#s-75c356b17da2c4f1)

### conditional_registration_candidates-011025

```text
(config-template)# no spanning-tree port-priority <cr>
```

Handler ` RVA 0x17496930 `；selector ` 4 `；EOL ` RVA 0x363E69F8 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-711556eec5af8b46](../../evidence/conditional_registrations-sets-001.md#r-711556eec5af8b46) · [条件 C-36b8478b1b785b22](../../evidence/conditions-sets-021.md#c-36b8478b1b785b22) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-75c356b17da2c4f1](../../evidence/state_effects-sets-025.md#s-75c356b17da2c4f1)

### conditional_registration_candidates-011013

```text
(config-template)# no spanning-tree portfast <cr>
```

Handler ` RVA 0x17496930 `；selector ` 1 `；EOL ` RVA 0x363EAAE0 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-711556eec5af8b46](../../evidence/conditional_registrations-sets-001.md#r-711556eec5af8b46) · [条件 C-e7434403decdd237](../../evidence/conditions-sets-089.md#c-e7434403decdd237) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-a659f98bc4f0532f](../../evidence/state_effects-sets-035.md#s-a659f98bc4f0532f)

### conditional_registration_candidates-011006

```text
(config-template)# spanning-tree <cr>
```

Handler ` RVA 0x17496930 `；selector ` 15 `；EOL ` RVA 0x363EBBF8 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-711556eec5af8b46](../../evidence/conditional_registrations-sets-001.md#r-711556eec5af8b46) · [条件 C-0fc945488fa6910c](../../evidence/conditions-sets-006.md#c-0fc945488fa6910c) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### conditional_registration_candidates-011015

```text
(config-template)# spanning-tree bpdufilter disable <cr>
```

Handler ` RVA 0x17496930 `；selector ` 12 `；EOL ` RVA 0x363EB060 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-711556eec5af8b46](../../evidence/conditional_registrations-sets-001.md#r-711556eec5af8b46) · [条件 C-5e3a64967d3a753d](../../evidence/conditions-sets-037.md#c-5e3a64967d3a753d) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-94e044a2a1652cfa](../../evidence/state_effects-sets-032.md#s-94e044a2a1652cfa)

### conditional_registration_candidates-011018

```text
(config-template)# spanning-tree bpduguard disable <cr>
```

Handler ` RVA 0x17496930 `；selector ` 11 `；EOL ` RVA 0x363EB458 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-711556eec5af8b46](../../evidence/conditional_registrations-sets-001.md#r-711556eec5af8b46) · [条件 C-2cc16e4d89306b2c](../../evidence/conditions-sets-018.md#c-2cc16e4d89306b2c) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-419ff80acdc3fb72](../../evidence/state_effects-sets-014.md#s-419ff80acdc3fb72)

### conditional_registration_candidates-011007

```text
(config-template)# spanning-tree cost <number:1..200000000> <cr>
```

Handler ` RVA 0x17496930 `；selector ` 3 `；EOL ` RVA 0x363E6958 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` port path cost。

[候选注册 R-711556eec5af8b46](../../evidence/conditional_registrations-sets-001.md#r-711556eec5af8b46) · [条件 C-4bff05517e984483](../../evidence/conditions-sets-030.md#c-4bff05517e984483) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-9d85541da89ebe6a](../../evidence/parameters-sets-012.md#p-9d85541da89ebe6a)

### conditional_registration_candidates-011022

```text
(config-template)# spanning-tree link-type point-to-point <cr>
```

Handler ` RVA 0x17496930 `；selector ` 9 `；EOL ` RVA 0x363EB800 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-711556eec5af8b46](../../evidence/conditional_registrations-sets-001.md#r-711556eec5af8b46) · [条件 C-c34de96998a3184b](../../evidence/conditions-sets-075.md#c-c34de96998a3184b) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-e501fbf46fffd0c8](../../evidence/state_effects-sets-048.md#s-e501fbf46fffd0c8)

### conditional_registration_candidates-011046

```text
(config-template)# spanning-tree port-priority <?number_help_func_action@55558b93a9d0> <cr>
```

Handler ` RVA 0x17496930 `；selector ` 4 `；EOL ` RVA 0x363E69F8 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[候选注册 R-711556eec5af8b46](../../evidence/conditional_registrations-sets-001.md#r-711556eec5af8b46) · [条件 C-93a29336def3f2a3](../../evidence/conditions-sets-057.md#c-93a29336def3f2a3) · [缺口 G-71a2e4c0afee7f88](../../evidence/gaps-sets-004.md#g-71a2e4c0afee7f88)

### conditional_registration_candidates-011010

```text
(config-template)# spanning-tree portfast <cr>
```

Handler ` RVA 0x17496930 `；selector ` 1 `；EOL ` RVA 0x363EAAE0 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-711556eec5af8b46](../../evidence/conditional_registrations-sets-001.md#r-711556eec5af8b46) · [条件 C-59126b9115087de2](../../evidence/conditions-sets-035.md#c-59126b9115087de2) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-265650c0979d87d8](../../evidence/state_effects-sets-009.md#s-265650c0979d87d8)

