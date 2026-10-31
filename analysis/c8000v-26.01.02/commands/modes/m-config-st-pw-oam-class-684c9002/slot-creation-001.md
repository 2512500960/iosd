# config-st-pw-oam-class · 依赖静态建槽的条件安装

[模式索引](README.md) · [总索引](../../README.md)

### static_slot_creation_candidates-004422

```text
(config-st-pw-oam-class)# ack enable <cr>
```

Handler ` RVA 0x1A4510F0 `；selector ` 4 `；EOL ` RVA 0x36C68AE0 `。

模式根 ` RVA 0x36C67848 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-9da0bc775972f7c6](../../evidence/conditional_registrations-sets-002.md#r-9da0bc775972f7c6) · [条件 C-c6ff8758295953ce](../../evidence/conditions-sets-077.md#c-c6ff8758295953ce) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### static_slot_creation_candidates-004429

```text
(config-st-pw-oam-class)# default ack enable <cr>
```

Handler ` RVA 0x1A4510F0 `；selector ` 4 `；EOL ` RVA 0x36C68AE0 `。

模式根 ` RVA 0x36C67848 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-9da0bc775972f7c6](../../evidence/conditional_registrations-sets-002.md#r-9da0bc775972f7c6) · [条件 C-c6ff8758295953ce](../../evidence/conditions-sets-077.md#c-c6ff8758295953ce) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-d726bc898dd1a5d7](../../evidence/state_effects-sets-046.md#s-d726bc898dd1a5d7)

### static_slot_creation_candidates-004424

```text
(config-st-pw-oam-class)# default keepalive <cr>
```

Handler ` RVA 0x1A4510F0 `；selector ` 3 `；EOL ` RVA 0x36C687F0 `。

模式根 ` RVA 0x36C67848 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-9da0bc775972f7c6](../../evidence/conditional_registrations-sets-002.md#r-9da0bc775972f7c6) · [条件 C-bdd3edb43cf18c10](../../evidence/conditions-sets-073.md#c-bdd3edb43cf18c10) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-d726bc898dd1a5d7](../../evidence/state_effects-sets-046.md#s-d726bc898dd1a5d7)

### static_slot_creation_candidates-004435

```text
(config-st-pw-oam-class)# default timeout refresh ack <cr>
```

Handler ` RVA 0x1A4510F0 `；selector ` 2 `；EOL ` RVA 0x36C684B0 `。

模式根 ` RVA 0x36C67848 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-9da0bc775972f7c6](../../evidence/conditional_registrations-sets-002.md#r-9da0bc775972f7c6) · [条件 C-68509c8f08e50fea](../../evidence/conditions-sets-040.md#c-68509c8f08e50fea) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-d726bc898dd1a5d7](../../evidence/state_effects-sets-046.md#s-d726bc898dd1a5d7)

### static_slot_creation_candidates-004432

```text
(config-st-pw-oam-class)# default timeout refresh send <cr>
```

Handler ` RVA 0x1A4510F0 `；selector ` 1 `；EOL ` RVA 0x36C681C0 `。

模式根 ` RVA 0x36C67848 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-9da0bc775972f7c6](../../evidence/conditional_registrations-sets-002.md#r-9da0bc775972f7c6) · [条件 C-b623bf1759e73498](../../evidence/conditions-sets-070.md#c-b623bf1759e73498) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-d726bc898dd1a5d7](../../evidence/state_effects-sets-046.md#s-d726bc898dd1a5d7)

### static_slot_creation_candidates-004427

```text
(config-st-pw-oam-class)# default ttl <cr>
```

Handler ` RVA 0x1A4510F0 `；selector ` 5 `；EOL ` RVA 0x36C68DD8 `。

模式根 ` RVA 0x36C67848 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-9da0bc775972f7c6](../../evidence/conditional_registrations-sets-002.md#r-9da0bc775972f7c6) · [条件 C-5eea3ae2154e87a2](../../evidence/conditions-sets-037.md#c-5eea3ae2154e87a2) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-d726bc898dd1a5d7](../../evidence/state_effects-sets-046.md#s-d726bc898dd1a5d7)

### static_slot_creation_candidates-004423

```text
(config-st-pw-oam-class)# keepalive <number:1..4095> <cr>
```

Handler ` RVA 0x1A4510F0 `；selector ` 3 `；EOL ` RVA 0x36C687F0 `。

模式根 ` RVA 0x36C67848 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Seconds, default is 600。

[候选注册 R-9da0bc775972f7c6](../../evidence/conditional_registrations-sets-002.md#r-9da0bc775972f7c6) · [条件 C-09da2f874aeae6b2](../../evidence/conditions-sets-004.md#c-09da2f874aeae6b2) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-426ec6c50cb8aeb0](../../evidence/parameters-sets-006.md#p-426ec6c50cb8aeb0)

### static_slot_creation_candidates-004428

```text
(config-st-pw-oam-class)# no ack enable <cr>
```

Handler ` RVA 0x1A4510F0 `；selector ` 4 `；EOL ` RVA 0x36C68AE0 `。

模式根 ` RVA 0x36C67848 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-9da0bc775972f7c6](../../evidence/conditional_registrations-sets-002.md#r-9da0bc775972f7c6) · [条件 C-c6ff8758295953ce](../../evidence/conditions-sets-077.md#c-c6ff8758295953ce) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-6e7162f2ff96bd3c](../../evidence/state_effects-sets-023.md#s-6e7162f2ff96bd3c)

### static_slot_creation_candidates-004421

```text
(config-st-pw-oam-class)# no keepalive <cr>
```

Handler ` RVA 0x1A4510F0 `；selector ` 3 `；EOL ` RVA 0x36C687F0 `。

模式根 ` RVA 0x36C67848 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-9da0bc775972f7c6](../../evidence/conditional_registrations-sets-002.md#r-9da0bc775972f7c6) · [条件 C-cd0e3dad8cb52def](../../evidence/conditions-sets-079.md#c-cd0e3dad8cb52def) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-6e7162f2ff96bd3c](../../evidence/state_effects-sets-023.md#s-6e7162f2ff96bd3c)

### static_slot_creation_candidates-004433

```text
(config-st-pw-oam-class)# no timeout refresh ack <cr>
```

Handler ` RVA 0x1A4510F0 `；selector ` 2 `；EOL ` RVA 0x36C684B0 `。

模式根 ` RVA 0x36C67848 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-9da0bc775972f7c6](../../evidence/conditional_registrations-sets-002.md#r-9da0bc775972f7c6) · [条件 C-441e05eeb9c0bb39](../../evidence/conditions-sets-027.md#c-441e05eeb9c0bb39) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-6e7162f2ff96bd3c](../../evidence/state_effects-sets-023.md#s-6e7162f2ff96bd3c)

### static_slot_creation_candidates-004430

```text
(config-st-pw-oam-class)# no timeout refresh send <cr>
```

Handler ` RVA 0x1A4510F0 `；selector ` 1 `；EOL ` RVA 0x36C681C0 `。

模式根 ` RVA 0x36C67848 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-9da0bc775972f7c6](../../evidence/conditional_registrations-sets-002.md#r-9da0bc775972f7c6) · [条件 C-34527803516455a6](../../evidence/conditions-sets-020.md#c-34527803516455a6) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-6e7162f2ff96bd3c](../../evidence/state_effects-sets-023.md#s-6e7162f2ff96bd3c)

### static_slot_creation_candidates-004425

```text
(config-st-pw-oam-class)# no ttl <cr>
```

Handler ` RVA 0x1A4510F0 `；selector ` 5 `；EOL ` RVA 0x36C68DD8 `。

模式根 ` RVA 0x36C67848 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-9da0bc775972f7c6](../../evidence/conditional_registrations-sets-002.md#r-9da0bc775972f7c6) · [条件 C-32a217eaa394eb42](../../evidence/conditions-sets-020.md#c-32a217eaa394eb42) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-6e7162f2ff96bd3c](../../evidence/state_effects-sets-023.md#s-6e7162f2ff96bd3c)

### static_slot_creation_candidates-004434

```text
(config-st-pw-oam-class)# timeout refresh ack <number:0..4095> <cr>
```

Handler ` RVA 0x1A4510F0 `；selector ` 2 `；EOL ` RVA 0x36C684B0 `。

模式根 ` RVA 0x36C67848 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Seconds, default is 600。

[候选注册 R-9da0bc775972f7c6](../../evidence/conditional_registrations-sets-002.md#r-9da0bc775972f7c6) · [条件 C-5cd4b78625432fb7](../../evidence/conditions-sets-036.md#c-5cd4b78625432fb7) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-58c938735b88b884](../../evidence/parameters-sets-007.md#p-58c938735b88b884)

### static_slot_creation_candidates-004431

```text
(config-st-pw-oam-class)# timeout refresh send <number:1..4095> <cr>
```

Handler ` RVA 0x1A4510F0 `；selector ` 1 `；EOL ` RVA 0x36C681C0 `。

模式根 ` RVA 0x36C67848 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Seconds, default is 30。

[候选注册 R-9da0bc775972f7c6](../../evidence/conditional_registrations-sets-002.md#r-9da0bc775972f7c6) · [条件 C-6a0485ffba1588cf](../../evidence/conditions-sets-041.md#c-6a0485ffba1588cf) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-e0dd23b7ec84368b](../../evidence/parameters-sets-017.md#p-e0dd23b7ec84368b)

### static_slot_creation_candidates-004426

```text
(config-st-pw-oam-class)# ttl <number:1..255> <cr>
```

Handler ` RVA 0x1A4510F0 `；selector ` 5 `；EOL ` RVA 0x36C68DD8 `。

模式根 ` RVA 0x36C67848 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` TTL, default is 1。

[候选注册 R-9da0bc775972f7c6](../../evidence/conditional_registrations-sets-002.md#r-9da0bc775972f7c6) · [条件 C-fad9d9c540a9239e](../../evidence/conditions-sets-097.md#c-fad9d9c540a9239e) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-daeb4e098811adde](../../evidence/parameters-sets-016.md#p-daeb4e098811adde)

