# configure · 六个基础模式的历史连接

[模式索引](README.md) · [总索引](../../README.md)

### path-039094

```text
(config)# do-exec show subscriber disconnect stats <cr>
```

Handler ` RVA 0x10A1B320 `；selector ` 0 `；EOL ` RVA 0x34BFD988 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031566

```text
(config)# do-exec show subscriber lite-session <cr>
```

Handler ` RVA 0x10A1C1B0 `；selector ` 0 `；EOL ` RVA 0x34BFDF10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-048425

```text
(config)# do-exec show subscriber log ip <address> <cr>
```

Handler ` RVA 0x10A1C7B0 `；selector ` 0 `；EOL ` RVA 0x34C05C08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IPV4 address。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-c86367971b47c6d5](../../evidence/parameters-sets-015.md#p-c86367971b47c6d5) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061518

```text
(config)# do-exec show subscriber log ip <prefix:dynamic> <cr>
```

Handler ` RVA 0x10A1C7B0 `；selector ` 0 `；EOL ` RVA 0x34C05C08 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` IPV6 destination prefix x:x::y/&lt;z&gt;。

[条件 C-7eae74236cb06f75](../../evidence/conditions-sets-049.md#c-7eae74236cb06f75) · [缺口 G-579add57dadb252f](../../evidence/gaps-sets-004.md#g-579add57dadb252f) · [参数 P-6035135b1c37f8e4](../../evidence/parameters-sets-008.md#p-6035135b1c37f8e4) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-048321

```text
(config)# do-exec show subscriber log mac-address <string> <cr>
```

Handler ` RVA 0x10A1C9D0 `；selector ` 0 `；EOL ` RVA 0x34C05590 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` subscriber log。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-afcbeeb897d62eac](../../evidence/parameters-sets-013.md#p-afcbeeb897d62eac) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-058194

```text
(config)# do-exec show subscriber log vrf <string> ip <address> <cr>
```

Handler ` RVA 0x10A1C680 `；selector ` 0 `；EOL ` RVA 0x34C058F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string `  vrf name ；` address ` IPV4 address。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-4101573dad634c18](../../evidence/parameters-sets-005.md#p-4101573dad634c18) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031480

```text
(config)# do-exec show subscriber memory <cr>
```

Handler ` RVA 0x10542A80 `；selector ` 0 `；EOL ` RVA 0x34BFC220 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-054830

```text
(config)# do-exec show subscriber per-session debug sessions-hit end-code <cr>
```

Handler ` RVA 0x10A1C930 `；selector ` 0 `；EOL ` RVA 0x34C04CC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-054788

```text
(config)# do-exec show subscriber per-session debug sessions-hit start-code <cr>
```

Handler ` RVA 0x10A1C980 `；selector ` 0 `；EOL ` RVA 0x34C04A20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-054870

```text
(config)# do-exec show subscriber per-session debug sessions-hit unexpected-disconnect <cr>
```

Handler ` RVA 0x10A1C8E0 `；selector ` 0 `；EOL ` RVA 0x34C04F70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-048335

```text
(config)# do-exec show subscriber per-session debug statistics <cr>
```

Handler ` RVA 0x10A1C890 `；selector ` 0 `；EOL ` RVA 0x34C05218 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-039262

```text
(config)# do-exec show subscriber policy conditions <cr>
```

Handler ` RVA 0x10A5CCE0 `；selector ` 0 `；EOL ` RVA 0x34C73DA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-039359

```text
(config)# do-exec show subscriber policy pACLs <cr>
```

Handler ` RVA 0x106830F0 `；selector ` 0 `；EOL ` RVA 0x34BDD320 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-039411

```text
(config)# do-exec show subscriber policy pClasses <cr>
```

Handler ` RVA 0x10687FC0 `；selector ` 0 `；EOL ` RVA 0x34BDD068 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-048680

```text
(config)# do-exec show subscriber policy peer all <cr>
```

Handler ` RVA 0xFE8BEF0 `；selector ` 2 `；EOL ` RVA 0x34906950 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-e48925152890e49d](../../evidence/state_effects-sets-048.md#s-e48925152890e49d)

### path-039307

```text
(config)# do-exec show subscriber policy ppm-shim-db <cr>
```

Handler ` RVA 0x10564A40 `；selector ` 0 `；EOL ` RVA 0x34BDD5D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-054703

```text
(config)# do-exec show subscriber policy preauth handle <number:0..4294967295> <cr>
```

Handler ` RVA 0x109A64A0 `；selector ` 1 `；EOL ` RVA 0x34C4FCC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Enter Policy Handle。

[条件 C-913097b51c64cb25](../../evidence/conditions-sets-056.md#c-913097b51c64cb25) · [参数 P-e4ac79d46ca7cfea](../../evidence/parameters-sets-017.md#p-e4ac79d46ca7cfea) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-039163

```text
(config)# do-exec show subscriber policy profile <cr>
```

Handler ` RVA 0x10A47290 `；selector ` 0 `；EOL ` RVA 0x34C6DD90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-039215

```text
(config)# do-exec show subscriber policy rules <cr>
```

Handler ` RVA 0x10A70140 `；selector ` 0 `；EOL ` RVA 0x34C73AF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031595

```text
(config)# do-exec show subscriber service <cr>
```

Handler ` RVA 0x10A12F40 `；selector ` 0 `；EOL ` RVA 0x34C5EAB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031815

```text
(config)# do-exec show subscriber session <cr>
```

Handler ` RVA 0x10A1CB50 `；selector ` 0 `；EOL ` RVA 0x34BFE688 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1f9652d71e1f472e](../../evidence/state_effects-sets-007.md#s-1f9652d71e1f472e)

### path-061532

```text
(config)# do-exec show subscriber session feature <?option@55558a152cd8> <cr>
```

Handler ` RVA 0x10A1CB50 `；selector ` 0 `；EOL ` RVA 0x34BFE688 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a28f18f74db43d89](../../evidence/conditions-sets-063.md#c-a28f18f74db43d89) · [缺口 G-17772ad21ab504c3](../../evidence/gaps-sets-001.md#g-17772ad21ab504c3) · [状态效果 S-e2bb7dcbed050e58](../../evidence/state_effects-sets-048.md#s-e2bb7dcbed050e58)

### path-048323

```text
(config)# do-exec show subscriber session queuing display <cr>
```

Handler ` RVA 0x10A1CB50 `；selector ` 1 `；EOL ` RVA 0x34BFEEE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-5959f2c01199df14](../../evidence/state_effects-sets-019.md#s-5959f2c01199df14)

### path-054899

```text
(config)# do-exec show subscriber session queuing enable <number:0..4294967295> <cr>
```

Handler ` RVA 0x10A1CB50 `；selector ` 2 `；EOL ` RVA 0x34BFF280 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Subscriber session Unique ID。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-d8fc5bf063c7793b](../../evidence/parameters-sets-016.md#p-d8fc5bf063c7793b) · [状态效果 S-4c3e057bacb2a2ef](../../evidence/state_effects-sets-017.md#s-4c3e057bacb2a2ef)

### path-031553

```text
(config)# do-exec show subscriber statistics <cr>
```

Handler ` RVA 0x10A1DBA0 `；selector ` 0 `；EOL ` RVA 0x34C39980 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-052b8b74308d0d15](../../evidence/state_effects-sets-002.md#s-052b8b74308d0d15)

### path-061505

```text
(config)# do-exec show subscriber statistics identifier resource-type-determined <cr>
```

Handler ` RVA 0x10A1DBA0 `；selector ` 0 `；EOL ` RVA 0x34C39980 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7489f37b3846f946](../../evidence/conditions-sets-045.md#c-7489f37b3846f946) · [缺口 G-81921d217a8bd8e5](../../evidence/gaps-sets-005.md#g-81921d217a8bd8e5) · [状态效果 S-f47e145253bcd518](../../evidence/state_effects-sets-052.md#s-f47e145253bcd518)

### path-031473

```text
(config)# do-exec show subscriber tech-support <cr>
```

Handler ` RVA 0x10A2A830 `；selector ` 0 `；EOL ` RVA 0x34BFC528 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031610

```text
(config)# do-exec show subscriber template <cr>
```

Handler ` RVA 0x10A24180 `；selector ` 0 `；EOL ` RVA 0x34BFD3E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-039102

```text
(config)# do-exec show subscriber template active <cr>
```

Handler ` RVA 0x10A242B0 `；selector ` 0 `；EOL ` RVA 0x34BFCE70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-048204

```text
(config)# do-exec show subscriber template id <number:1..30500> <cr>
```

Handler ` RVA 0x10A24240 `；selector ` 0 `；EOL ` RVA 0x34BFD428 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Template Id。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-52180e6f7d2d8585](../../evidence/parameters-sets-007.md#p-52180e6f7d2d8585) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-054680

```text
(config)# do-exec show subscriber template key tmpl_id <number:1..30500> <cr>
```

Handler ` RVA 0x10A24720 `；selector ` 0 `；EOL ` RVA 0x34BFCBD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Template Id。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-08c72fd3e4c76054](../../evidence/parameters-sets-001.md#p-08c72fd3e4c76054) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-039158

```text
(config)# do-exec show subscriber template state <cr>
```

Handler ` RVA 0x10A241E0 `；selector ` 0 `；EOL ` RVA 0x34BFD118 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027762

```text
(config)# do-exec show subscriber-policy <cr>
```

Handler ` RVA 0xF282120 `；selector ` 0 `；EOL ` RVA 0x345E7448 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027755

```text
(config)# do-exec show subsys <cr>
```

Handler ` RVA 0xE0898A0 `；selector ` 0 `；EOL ` RVA 0x34177930 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-c7276f26f63bdc75](../../evidence/state_effects-sets-042.md#s-c7276f26f63bdc75)

### path-033476

```text
(config)# do-exec show subsys boottime <cr>
```

Handler ` RVA 0xE04C950 `；selector ` 0 `；EOL ` RVA 0x341764F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-043003

```text
(config)# do-exec show subsys boottime class <cr>
```

Handler ` RVA 0xE04C8F0 `；selector ` 0 `；EOL ` RVA 0x341764C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042974

```text
(config)# do-exec show subsys boottime init <cr>
```

Handler ` RVA 0xE04C8A0 `；selector ` 0 `；EOL ` RVA 0x34176220 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042999

```text
(config)# do-exec show subsys class kernel <cr>
```

Handler ` RVA 0xE089910 `；selector ` 0 `；EOL ` RVA 0x34176A30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-08bc92496c60f5ba](../../evidence/state_effects-sets-002.md#s-08bc92496c60f5ba)

### path-033494

```text
(config)# do-exec show subsys memory <cr>
```

Handler ` RVA 0xE04CA60 `；selector ` 0 `；EOL ` RVA 0x34177458 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-043052

```text
(config)# do-exec show subsys memory class <cr>
```

Handler ` RVA 0xE04CA00 `；selector ` 0 `；EOL ` RVA 0x34177430 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-043025

```text
(config)# do-exec show subsys memory init <cr>
```

Handler ` RVA 0xE04C9B0 `；selector ` 0 `；EOL ` RVA 0x34177188 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042949

```text
(config)# do-exec show subsys name <string> <cr>
```

Handler ` RVA 0xE0898A0 `；selector ` 0 `；EOL ` RVA 0x34175F38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Subsystem to list; trailing * is a wildcard。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-421db8a73cf5a5ea](../../evidence/parameters-sets-006.md#p-421db8a73cf5a5ea) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-026417

```text
(config)# do-exec show sum <cr>
```

Handler ` RVA 0xD7C05F0 `；selector ` 0 `；EOL ` RVA 0x34126EA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042040

```text
(config)# do-exec show system insecure configuration <cr>
```

Handler ` RVA 0xE030B60 `；selector ` 0 `；EOL ` RVA 0x3416F2E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042063

```text
(config)# do-exec show system insecure profile <cr>
```

Handler ` RVA 0xE030E30 `；selector ` 0 `；EOL ` RVA 0x3416F588 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042061

```text
(config)# do-exec show system security mode <cr>
```

Handler ` RVA 0xE031A40 `；selector ` 0 `；EOL ` RVA 0x3416F860 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027672

```text
(config)# do-exec show table-map <cr>
```

Handler ` RVA 0xDA4A5C0 `；selector ` 2 `；EOL ` RVA 0x33FB4538 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d590c45d0dd007f7](../../evidence/conditions-sets-082.md#c-d590c45d0dd007f7) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027674

```text
(config)# do-exec show table-map <cr>
```

Handler ` RVA 0xDA4A5C0 `；selector ` 1 `；EOL ` RVA 0x33FB47E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1efe1eaa710870cf](../../evidence/conditions-sets-012.md#c-1efe1eaa710870cf) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032644

```text
(config)# do-exec show table-map enabled <cr>
```

Handler ` RVA 0xDA4A5C0 `；selector ` 3 `；EOL ` RVA 0x33FB2FF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1433c41bb93b8ca8](../../evidence/conditions-sets-008.md#c-1433c41bb93b8ca8) · [状态效果 S-703dbfcf5f72c556](../../evidence/state_effects-sets-024.md#s-703dbfcf5f72c556)

### path-040368

```text
(config)# do-exec show tableid ha statistics <cr>
```

Handler ` RVA 0x123AFC60 `；selector ` 0 `；EOL ` RVA 0x35842D80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8e998093e8a7ad18](../../evidence/conditions-sets-055.md#c-8e998093e8a7ad18) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027702

```text
(config)# do-exec show tacacs <cr>
```

Handler ` RVA 0xDBA8B50 `；selector ` 0 `；EOL ` RVA 0x33FFBC08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1a4c8f7fe1ec0938](../../evidence/state_effects-sets-006.md#s-1a4c8f7fe1ec0938)

### path-033040

```text
(config)# do-exec show tcl mem <cr>
```

Handler ` RVA 0x11144430 `；selector ` 0 `；EOL ` RVA 0x3540C060 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cda7adc3f25abc32](../../evidence/conditions-sets-079.md#c-cda7adc3f25abc32) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042254

```text
(config)# do-exec show tcl mem contents <cr>
```

Handler ` RVA 0x11143D30 `；selector ` 0 `；EOL ` RVA 0x3540C038 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a854d136acb40b52](../../evidence/conditions-sets-065.md#c-a854d136acb40b52) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-060717

```text
(config)# do-exec show tcp <?ttyline_action@55558924a1c8> <cr>
```

Handler ` RVA 0xCE26730 `；selector ` 0 `；EOL ` RVA 0x33CF6710 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [缺口 G-58d729ae0ec40eb5](../../evidence/gaps-sets-004.md#g-58d729ae0ec40eb5) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061618

```text
(config)# do-exec show tcp <?ttyline_action@55558924a1c8> ha connections <cr>
```

Handler ` RVA 0x123C5860 `；selector ` 0 `；EOL ` RVA 0x35844B80 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [缺口 G-58d729ae0ec40eb5](../../evidence/gaps-sets-004.md#g-58d729ae0ec40eb5) · [状态效果 S-7f99f435d6cc83e3](../../evidence/state_effects-sets-027.md#s-7f99f435d6cc83e3)

### path-032019

```text
(config)# do-exec show tcp statistics <cr>
```

Handler ` RVA 0xCE261A0 `；selector ` 0 `；EOL ` RVA 0x33CF6230 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040321

```text
(config)# do-exec show tcp statistics ingress <cr>
```

Handler ` RVA 0xCE27BF0 `；selector ` 0 `；EOL ` RVA 0x33CF6208 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9a8b9b50af9e9d91](../../evidence/conditions-sets-060.md#c-9a8b9b50af9e9d91) · [状态效果 S-924b29aadb3f7828](../../evidence/state_effects-sets-031.md#s-924b29aadb3f7828)

### path-045719

```text
(config)# do-exec show tdm connections aim <number:0..4294967295> <cr>
```

Handler ` RVA 0x15B0E440 `；selector ` 0 `；EOL ` RVA 0x35DECD60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` AIM slot number。

[条件 C-361279f06d757b8f](../../evidence/conditions-sets-021.md#c-361279f06d757b8f) · [参数 P-aa2ea22ca29461eb](../../evidence/parameters-sets-013.md#p-aa2ea22ca29461eb) · [状态效果 S-707364cc2f2c6865](../../evidence/state_effects-sets-024.md#s-707364cc2f2c6865)

### path-027748

```text
(config)# do-exec show tech-support <cr>
```

Handler ` RVA 0xDE9E120 `；selector ` 0 `；EOL ` RVA 0x34086880 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-927f4ee285f43a9d](../../evidence/conditions-sets-057.md#c-927f4ee285f43a9d) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-043556

```text
(config)# do-exec show tech-support mfib ipv4 <cr>
```

Handler ` RVA 0x1197EB10 `；selector ` 0 `；EOL ` RVA 0x355C02B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-927f4ee285f43a9d](../../evidence/conditions-sets-057.md#c-927f4ee285f43a9d) · [状态效果 S-f8eb12851e75cfbc](../../evidence/state_effects-sets-053.md#s-f8eb12851e75cfbc)

### path-043548

```text
(config)# do-exec show tech-support mfib ipv6 <cr>
```

Handler ` RVA 0x1197E970 `；selector ` 0 `；EOL ` RVA 0x355C0570 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-927f4ee285f43a9d](../../evidence/conditions-sets-057.md#c-927f4ee285f43a9d) · [状态效果 S-32be9d13a6863555](../../evidence/state_effects-sets-011.md#s-32be9d13a6863555)

### path-061787

```text
(config)# do-exec show tech-support mvpn vrf <?option@555589ceafd0> <cr>
```

Handler ` RVA 0xDE9E120 `；selector ` 0 `；EOL ` RVA 0x34086880 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3f3a14429b8c7e44](../../evidence/conditions-sets-025.md#c-3f3a14429b8c7e44) · [缺口 G-d4cb1cb4dc8b62a0](../../evidence/gaps-sets-007.md#g-d4cb1cb4dc8b62a0) · [状态效果 S-1ebc426dafbf12ec](../../evidence/state_effects-sets-007.md#s-1ebc426dafbf12ec)

### path-043498

```text
(config)# do-exec show tech-support vrrp ipv4 <cr>
```

Handler ` RVA 0x133CAB60 `；selector ` 0 `；EOL ` RVA 0x35A85C08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-927f4ee285f43a9d](../../evidence/conditions-sets-057.md#c-927f4ee285f43a9d) · [状态效果 S-e9431a6fdf8b6cc2](../../evidence/state_effects-sets-049.md#s-e9431a6fdf8b6cc2)

### path-043514

```text
(config)# do-exec show tech-support vrrp ipv6 <cr>
```

Handler ` RVA 0x133CADF0 `；selector ` 0 `；EOL ` RVA 0x35A85EC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-927f4ee285f43a9d](../../evidence/conditions-sets-057.md#c-927f4ee285f43a9d) · [状态效果 S-1c5998cfe1762ba5](../../evidence/state_effects-sets-006.md#s-1c5998cfe1762ba5)

### path-027709

```text
(config)# do-exec show template <cr>
```

Handler ` RVA 0xD6D2EC0 `；selector ` 0 `；EOL ` RVA 0x33ED7618 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f652ba47bad0a6b9](../../evidence/conditions-sets-095.md#c-f652ba47bad0a6b9) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061761

```text
(config)# do-exec show template binding target <interface> <cr>
```

Handler ` RVA 0xD6D34F0 `；selector ` 21 `；EOL ` RVA 0x33ED72E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-edd39368084635b4](../../evidence/conditions-sets-092.md#c-edd39368084635b4) · [缺口 G-3917b3499f61b494](../../evidence/gaps-sets-002.md#g-3917b3499f61b494) · [参数 P-f4311544c64277ae](../../evidence/parameters-sets-018.md#p-f4311544c64277ae) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-050825

```text
(config)# do-exec show template binding target interface_global <cr>
```

Handler ` RVA 0xD6D3670 `；selector ` 10 `；EOL ` RVA 0x33ED6FB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032911

```text
(config)# do-exec show template brief <cr>
```

Handler ` RVA 0xD6D2EC0 `；selector ` 16 `；EOL ` RVA 0x33ED6968 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032936

```text
(config)# do-exec show template detail <cr>
```

Handler ` RVA 0xD6D2EC0 `；selector ` 3 `；EOL ` RVA 0x33ED6C88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6adaea3be23eacff](../../evidence/conditions-sets-041.md#c-6adaea3be23eacff) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032965

```text
(config)# do-exec show template global <cr>
```

Handler ` RVA 0xD6DC3B0 `；selector ` 0 `；EOL ` RVA 0x33ED3688 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-887dbb81b1157877](../../evidence/conditions-sets-053.md#c-887dbb81b1157877) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042008

```text
(config)# do-exec show template global all <cr>
```

Handler ` RVA 0xD6DC3B0 `；selector ` 25 `；EOL ` RVA 0x33ED21D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-050785

```text
(config)# do-exec show template global binding all <cr>
```

Handler ` RVA 0xD6DC3B0 `；selector ` 23 `；EOL ` RVA 0x33ED3010 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-041986

```text
(config)# do-exec show template global brief <cr>
```

Handler ` RVA 0xD6DC3B0 `；selector ` 22 `；EOL ` RVA 0x33ED1F28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042100

```text
(config)# do-exec show template global detail <cr>
```

Handler ` RVA 0xD6DC3B0 `；selector ` 24 `；EOL ` RVA 0x33ED33B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-23fa1ad94a077e42](../../evidence/conditions-sets-014.md#c-23fa1ad94a077e42) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-056240

```text
(config)# do-exec show template global source built-in all <cr>
```

Handler ` RVA 0xD6DC3B0 `；selector ` 26 `；EOL ` RVA 0x33ED28B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-058767

```text
(config)# do-exec show template global source built-in original all <cr>
```

Handler ` RVA 0xD6DC3B0 `；selector ` 27 `；EOL ` RVA 0x33ED2BD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-056227

```text
(config)# do-exec show template global source user all <cr>
```

Handler ` RVA 0xD6DC3B0 `；selector ` 28 `；EOL ` RVA 0x33ED2548 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042069

```text
(config)# do-exec show template interface all <cr>
```

Handler ` RVA 0xD6D3670 `；selector ` 7 `；EOL ` RVA 0x33ED5198 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-050766

```text
(config)# do-exec show template interface binding all <cr>
```

Handler ` RVA 0xD6D3670 `；selector ` 4 `；EOL ` RVA 0x33ED4088 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062198

```text
(config)# do-exec show template interface binding target <interface> <cr>
```

Handler ` RVA 0xD6D3670 `；selector ` 9 `；EOL ` RVA 0x33ED3DB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3636176e96da53de](../../evidence/conditions-sets-021.md#c-3636176e96da53de) · [缺口 G-4f731d551b104bd9](../../evidence/gaps-sets-003.md#g-4f731d551b104bd9) · [参数 P-8a1f2938c849533f](../../evidence/parameters-sets-011.md#p-8a1f2938c849533f) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-056215

```text
(config)# do-exec show template interface binding target interface_global <cr>
```

Handler ` RVA 0xD6D3670 `；selector ` 10 `；EOL ` RVA 0x33ED3A88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042024

```text
(config)# do-exec show template interface brief <cr>
```

Handler ` RVA 0xD6D3670 `；selector ` 2 `；EOL ` RVA 0x33ED43C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-058766

```text
(config)# do-exec show template interface source built-in Original all <cr>
```

Handler ` RVA 0xD6D3670 `；selector ` 19 `；EOL ` RVA 0x33ED4B18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-056264

```text
(config)# do-exec show template interface source built-in all <cr>
```

Handler ` RVA 0xD6D3670 `；selector ` 5 `；EOL ` RVA 0x33ED4E48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-056238

```text
(config)# do-exec show template interface source user all <cr>
```

Handler ` RVA 0xD6D3670 `；selector ` 6 `；EOL ` RVA 0x33ED4740 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042044

```text
(config)# do-exec show template service all <cr>
```

Handler ` RVA 0xD6D44E0 `；selector ` 15 `；EOL ` RVA 0x33ED5FF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062202

```text
(config)# do-exec show template service binding target <interface> <cr>
```

Handler ` RVA 0xD6D44E0 `；selector ` 20 `；EOL ` RVA 0x33ED63E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d63893537805343b](../../evidence/conditions-sets-083.md#c-d63893537805343b) · [缺口 G-cd52c74062bddf68](../../evidence/gaps-sets-007.md#g-cd52c74062bddf68) · [参数 P-94a0821823af067d](../../evidence/parameters-sets-011.md#p-94a0821823af067d) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042092

```text
(config)# do-exec show template service brief <cr>
```

Handler ` RVA 0xD6D44E0 `；selector ` 14 `；EOL ` RVA 0x33ED66B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-056226

```text
(config)# do-exec show template service source aaa all <cr>
```

Handler ` RVA 0xD6D44E0 `；selector ` 13 `；EOL ` RVA 0x33ED55A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-056250

```text
(config)# do-exec show template service source built-in all <cr>
```

Handler ` RVA 0xD6D44E0 `；selector ` 11 `；EOL ` RVA 0x33ED5CA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-056239

```text
(config)# do-exec show template service source user all <cr>
```

Handler ` RVA 0xD6D44E0 `；selector ` 12 `；EOL ` RVA 0x33ED5938 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-060732

```text
(config)# do-exec show tenant <string> <cr>
```

Handler ` RVA 0x123E0080 `；selector ` 0 `；EOL ` RVA 0x35848AF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Tenant name。

[条件 C-bf7f4c0b1efeaabb](../../evidence/conditions-sets-074.md#c-bf7f4c0b1efeaabb) · [缺口 G-3a54b45ae19722a9](../../evidence/gaps-sets-003.md#g-3a54b45ae19722a9) · [参数 P-4849b754023d8640](../../evidence/parameters-sets-006.md#p-4849b754023d8640) · [状态效果 S-0621ab259e6d2c36](../../evidence/state_effects-sets-002.md#s-0621ab259e6d2c36)

### path-032721

```text
(config)# do-exec show tenant all <cr>
```

Handler ` RVA 0x123E0800 `；selector ` 0 `；EOL ` RVA 0x35847D08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5a26eccb1056e52c](../../evidence/conditions-sets-035.md#c-5a26eccb1056e52c) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061123

```text
(config)# do-exec show tenant mapping <string> <cr>
```

Handler ` RVA 0x123DF9C0 `；selector ` 0 `；EOL ` RVA 0x35848428 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Tenant name。

[条件 C-d1107cf8c9b4beaa](../../evidence/conditions-sets-081.md#c-d1107cf8c9b4beaa) · [缺口 G-fb1f8ef62f12c9da](../../evidence/gaps-sets-009.md#g-fb1f8ef62f12c9da) · [参数 P-c27fb50a72fd9cfc](../../evidence/parameters-sets-015.md#p-c27fb50a72fd9cfc) · [状态效果 S-d77e81a77911bd05](../../evidence/state_effects-sets-046.md#s-d77e81a77911bd05)

### path-062186

```text
(config)# do-exec show tenant mapping <string> vpn-id <string> <cr>
```

Handler ` RVA 0x123DF580 `；selector ` 0 `；EOL ` RVA 0x35848468 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Tenant name；` string ` Tenant VPN ID。

[条件 C-d1107cf8c9b4beaa](../../evidence/conditions-sets-081.md#c-d1107cf8c9b4beaa) · [缺口 G-fb1f8ef62f12c9da](../../evidence/gaps-sets-009.md#g-fb1f8ef62f12c9da) · [参数 P-3eb06e70527b3e65](../../evidence/parameters-sets-005.md#p-3eb06e70527b3e65) · [状态效果 S-d77e81a77911bd05](../../evidence/state_effects-sets-046.md#s-d77e81a77911bd05)

### path-041721

```text
(config)# do-exec show tenant mapping table <cr>
```

Handler ` RVA 0x123DFFF0 `；selector ` 0 `；EOL ` RVA 0x35848020 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5a26eccb1056e52c](../../evidence/conditions-sets-035.md#c-5a26eccb1056e52c) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027815

```text
(config)# do-exec show terminal <cr>
```

Handler ` RVA 0xE2CE600 `；selector ` 0 `；EOL ` RVA 0x3417D680 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033197

```text
(config)# do-exec show test_rib_access get_all_ipv4_protos <cr>
```

Handler ` RVA 0xDC10DD0 `；selector ` 1 `；EOL ` RVA 0x34010958 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-058852

```text
(config)# do-exec show test_rib_access get_proto_pdb <string> <number:1..2> <number:0..1> <string> <cr>
```

Handler ` RVA 0xDC10B50 `；selector ` 1 `；EOL ` RVA 0x34010640 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` router protocol name；` unsigned_number `  Protocol Type 1:IP 2:OSI ；` unsigned_number `  Address Family 0:IPv4 1:IPv6 ；` string ` Topology name。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-7afb3a264d306520](../../evidence/parameters-sets-010.md#p-7afb3a264d306520) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-060187

```text
(config)# do-exec show test_rib_access get_route <address> <number:0..6> <number:0..128> <string> <number:0..2> <number:0..65535> <number:0..65535> exact <cr>
```

Handler ` RVA 0xDC0FD90 `；selector ` 0 `；EOL ` RVA 0x3400F6A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP address of prefix；` unsigned_number `  Address Family 0:IPv4 6:IPv4Mcast ；` unsigned_number `  prefix len；` string ` Topology name；` unsigned_number `  NH Type 0:ANY 1:DEF  2:ALT；` unsigned_number `  NH Include Flter 0:No Incl Filter；` unsigned_number `  NH Exclude Flter 0:No Excl Fltr。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-2565c5ac010af90c](../../evidence/parameters-sets-003.md#p-2565c5ac010af90c) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-060191

```text
(config)# do-exec show test_rib_access get_route <address> <number:0..6> <number:0..128> <string> <number:0..2> <number:0..65535> <number:0..65535> long <cr>
```

Handler ` RVA 0xDC0FD90 `；selector ` 1 `；EOL ` RVA 0x3400F9B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP address of prefix；` unsigned_number `  Address Family 0:IPv4 6:IPv4Mcast ；` unsigned_number `  prefix len；` string ` Topology name；` unsigned_number `  NH Type 0:ANY 1:DEF  2:ALT；` unsigned_number `  NH Include Flter 0:No Incl Filter；` unsigned_number `  NH Exclude Flter 0:No Excl Fltr。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-2565c5ac010af90c](../../evidence/parameters-sets-003.md#p-2565c5ac010af90c) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-060210

```text
(config)# do-exec show test_rib_access get_route <address> <number:0..6> <number:0..128> <string> <number:0..2> <number:0..65535> <number:0..65535> long del_nh <cr>
```

Handler ` RVA 0xDC0FD90 `；selector ` 2 `；EOL ` RVA 0x3400F988 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP address of prefix；` unsigned_number `  Address Family 0:IPv4 6:IPv4Mcast ；` unsigned_number `  prefix len；` string ` Topology name；` unsigned_number `  NH Type 0:ANY 1:DEF  2:ALT；` unsigned_number `  NH Include Flter 0:No Incl Filter；` unsigned_number `  NH Exclude Flter 0:No Excl Fltr。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-2565c5ac010af90c](../../evidence/parameters-sets-003.md#p-2565c5ac010af90c) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-051176

```text
(config)# do-exec show test_rib_access walk_rib <number:0..7> <string> <cr>
```

Handler ` RVA 0xDC10910 `；selector ` 1 `；EOL ` RVA 0x340100A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number `  Address Family 0:IPv4 1:IPv6 6:IPv4Mcast 7:IPv6Mcast；` string ` Topology name。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-97593609663d590a](../../evidence/parameters-sets-012.md#p-97593609663d590a) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027703

```text
(config)# do-exec show time-range <cr>
```

Handler ` RVA 0xDBCCA30 `；selector ` 0 `；EOL ` RVA 0x33FFE8D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-17d35222846743bf](../../evidence/conditions-sets-009.md#c-17d35222846743bf) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032896

```text
(config)# do-exec show time-range ipc <cr>
```

Handler ` RVA 0xDBCA310 `；selector ` 0 `；EOL ` RVA 0x33FFE5D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-026724

```text
(config)# do-exec show timers <cr>
```

Handler ` RVA 0xDE91470 `；selector ` 0 `；EOL ` RVA 0x34175290 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027585

```text
(config)# do-exec show topology <cr>
```

Handler ` RVA 0xDB67370 `；selector ` 14 `；EOL ` RVA 0x33FE09D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-12d2c9312a09443a](../../evidence/conditions-sets-007.md#c-12d2c9312a09443a) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027586

```text
(config)# do-exec show topology <cr>
```

Handler ` RVA 0xDB67370 `；selector ` 0 `；EOL ` RVA 0x33FE0C58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f6c853a51173f873](../../evidence/conditions-sets-095.md#c-f6c853a51173f873) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031298

```text
(config)# do-exec show topology clients <cr>
```

Handler ` RVA 0xDB67370 `；selector ` 10 `；EOL ` RVA 0x33FE11F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031341

```text
(config)# do-exec show topology ha <cr>
```

Handler ` RVA 0xDB67370 `；selector ` 9 `；EOL ` RVA 0x33FE14E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1a8298fd1b24b055](../../evidence/conditions-sets-010.md#c-1a8298fd1b24b055) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027602

```text
(config)# do-exec show track <cr>
```

Handler ` RVA 0xE14F330 `；selector ` 1 `；EOL ` RVA 0x34214690 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a69f35cfdb7e6c5b](../../evidence/conditions-sets-064.md#c-a69f35cfdb7e6c5b) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-038993

```text
(config)# do-exec show track <number:1..32767> map <cr>
```

Handler ` RVA 0xE14F330 `；selector ` 11 `；EOL ` RVA 0x342159B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Track number。

[条件 C-2e2ab8ab0b73e4a6](../../evidence/conditions-sets-018.md#c-2e2ab8ab0b73e4a6) · [参数 P-c147d1fcc7a3b437](../../evidence/parameters-sets-015.md#p-c147d1fcc7a3b437) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031322

```text
(config)# do-exec show track map <cr>
```

Handler ` RVA 0xE14F330 `；selector ` 11 `；EOL ` RVA 0x34215278 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031347

```text
(config)# do-exec show track resolution <cr>
```

Handler ` RVA 0xE14F330 `；selector ` 3 `；EOL ` RVA 0x34214F38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-46131d030f6fe1b5](../../evidence/conditions-sets-027.md#c-46131d030f6fe1b5) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031270

```text
(config)# do-exec show track summary <cr>
```

Handler ` RVA 0xE14F330 `；selector ` 9 `；EOL ` RVA 0x34214C28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031242

```text
(config)# do-exec show track timers <cr>
```

Handler ` RVA 0xE14F330 `；selector ` 2 `；EOL ` RVA 0x34214980 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027403

```text
(config)# do-exec show traffic-shape <cr>
```

Handler ` RVA 0xDBD17C0 `；selector ` 0 `；EOL ` RVA 0x34001338 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ba475c145057a88a](../../evidence/conditions-sets-072.md#c-ba475c145057a88a) · [状态效果 S-11476af58488862d](../../evidence/state_effects-sets-004.md#s-11476af58488862d)

### path-060652

```text
(config)# do-exec show traffic-shape <interface> <cr>
```

Handler ` RVA 0xDBD17C0 `；selector ` 0 `；EOL ` RVA 0x34001338 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7e4de75612b26e4d](../../evidence/conditions-sets-049.md#c-7e4de75612b26e4d) · [缺口 G-726e7c502cb3ea5f](../../evidence/gaps-sets-004.md#g-726e7c502cb3ea5f) · [参数 P-a97d5a047ab507db](../../evidence/parameters-sets-013.md#p-a97d5a047ab507db) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-030517

```text
(config)# do-exec show traffic-shape queue <cr>
```

Handler ` RVA 0xDBD7140 `；selector ` 0 `；EOL ` RVA 0x34000FE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1a0ce2c47f6aef60](../../evidence/conditions-sets-010.md#c-1a0ce2c47f6aef60) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-060903

```text
(config)# do-exec show traffic-shape queue <interface> <cr>
```

Handler ` RVA 0xDBD7140 `；selector ` 0 `；EOL ` RVA 0x34000FE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7375da9cea985aee](../../evidence/conditions-sets-045.md#c-7375da9cea985aee) · [缺口 G-e8c3e147a59b7992](../../evidence/gaps-sets-008.md#g-e8c3e147a59b7992) · [参数 P-c3a0513750ad55b8](../../evidence/parameters-sets-015.md#p-c3a0513750ad55b8) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-030520

```text
(config)# do-exec show traffic-shape statistics <cr>
```

Handler ` RVA 0xDBD13D0 `；selector ` 0 `；EOL ` RVA 0x34000BD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8a38a26c3b4fd13d](../../evidence/conditions-sets-053.md#c-8a38a26c3b4fd13d) · [状态效果 S-ae76e74b6e20226e](../../evidence/state_effects-sets-037.md#s-ae76e74b6e20226e)

### path-060897

```text
(config)# do-exec show traffic-shape statistics <interface> <cr>
```

Handler ` RVA 0xDBD13D0 `；selector ` 0 `；EOL ` RVA 0x34000BD8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-72be1661e7afef05](../../evidence/conditions-sets-044.md#c-72be1661e7afef05) · [缺口 G-5f2590667b1d47f9](../../evidence/gaps-sets-004.md#g-5f2590667b1d47f9) · [参数 P-8d8a83d1f427d567](../../evidence/parameters-sets-011.md#p-8d8a83d1f427d567) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-029366

```text
(config)# do-exec show transport-map all <cr>
```

Handler ` RVA 0xDBDB160 `；selector ` 0 `；EOL ` RVA 0x34003AB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-42d47df7b5366e92](../../evidence/conditions-sets-026.md#c-42d47df7b5366e92) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-035562

```text
(config)# do-exec show transport-map name <string> <cr>
```

Handler ` RVA 0xDBDB160 `；selector ` 1 `；EOL ` RVA 0x34003DC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Transport map name。

[条件 C-42d47df7b5366e92](../../evidence/conditions-sets-026.md#c-42d47df7b5366e92) · [参数 P-a22277e8b6222397](../../evidence/parameters-sets-012.md#p-a22277e8b6222397) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-035680

```text
(config)# do-exec show transport-map type console <cr>
```

Handler ` RVA 0xDBDB160 `；selector ` 2 `；EOL ` RVA 0x340040C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-005d4dca99f087dd](../../evidence/conditions-sets-001.md#c-005d4dca99f087dd) · [状态效果 S-116756b7e5536e74](../../evidence/state_effects-sets-004.md#s-116756b7e5536e74)

### path-061160

```text
(config)# do-exec show trunk group <?show_tg_cmd@55558ce57110> <cr>
```

Handler ` RVA 0x1E3C0C60 `；selector ` 0 `；EOL ` RVA 0x379031A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [缺口 G-f527f1d381618282](../../evidence/gaps-sets-008.md#g-f527f1d381618282) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033738

```text
(config)# do-exec show tunnel 6rd <cr>
```

Handler ` RVA 0xFBB81A0 `；selector ` 2 `；EOL ` RVA 0x3483CDE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5c1e016e6af2523a](../../evidence/conditions-sets-036.md#c-5c1e016e6af2523a) · [状态效果 S-a88e27dec3c6a8ac](../../evidence/state_effects-sets-036.md#s-a88e27dec3c6a8ac)

### path-061187

```text
(config)# do-exec show tunnel 6rd <interface> <cr>
```

Handler ` RVA 0xFBB81A0 `；selector ` 2 `；EOL ` RVA 0x3483CDE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c863e53397a1f1b4](../../evidence/conditions-sets-077.md#c-c863e53397a1f1b4) · [缺口 G-8b5c34aee0764754](../../evidence/gaps-sets-005.md#g-8b5c34aee0764754) · [参数 P-4d056672b39c0306](../../evidence/parameters-sets-006.md#p-4d056672b39c0306) · [状态效果 S-a88e27dec3c6a8ac](../../evidence/state_effects-sets-036.md#s-a88e27dec3c6a8ac)

### path-043497

```text
(config)# do-exec show tunnel bgp host-addr <cr>
```

Handler ` RVA 0x1436C2A0 `；selector ` 0 `；EOL ` RVA 0x35D49618 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-c77829efae1daa63](../../evidence/state_effects-sets-042.md#s-c77829efae1daa63)

### path-061796

```text
(config)# do-exec show tunnel capabilities feature <?option@555589d7a340> <cr>
```

Handler ` RVA 0xFB75B00 `；selector ` 0 `；EOL ` RVA 0x34826380 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-798e8732f3f50469](../../evidence/conditions-sets-047.md#c-798e8732f3f50469) · [缺口 G-d2b8df8c78767d3f](../../evidence/gaps-sets-007.md#g-d2b8df8c78767d3f) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-051836

```text
(config)# do-exec show tunnel capabilities feature gre-checksum <cr>
```

Handler ` RVA 0xFB75B00 `；selector ` 0 `；EOL ` RVA 0x34826380 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cc81b3409b92ce21](../../evidence/conditions-sets-079.md#c-cc81b3409b92ce21) · [状态效果 S-bf23248e4f3bc252](../../evidence/state_effects-sets-040.md#s-bf23248e4f3bc252)

### path-061794

```text
(config)# do-exec show tunnel capabilities mode <?option@555589d7a040> <cr>
```

Handler ` RVA 0xFB75990 `；selector ` 0 `；EOL ` RVA 0x348260A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-476340e4bacf860b](../../evidence/conditions-sets-028.md#c-476340e4bacf860b) · [缺口 G-86d3c76898c40d7c](../../evidence/gaps-sets-005.md#g-86d3c76898c40d7c) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-051828

```text
(config)# do-exec show tunnel capabilities mode uninitialized <cr>
```

Handler ` RVA 0xFB75990 `；selector ` 0 `；EOL ` RVA 0x348260A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e5e74c02dad737e8](../../evidence/conditions-sets-089.md#c-e5e74c02dad737e8) · [状态效果 S-7c154af7ea42aefe](../../evidence/state_effects-sets-026.md#s-7c154af7ea42aefe)

### path-033717

```text
(config)# do-exec show tunnel endpoints <cr>
```

Handler ` RVA 0xFBB81A0 `；selector ` 1 `；EOL ` RVA 0x3483D7A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-109cc137e9bf92db](../../evidence/conditions-sets-007.md#c-109cc137e9bf92db) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061185

```text
(config)# do-exec show tunnel endpoints <interface> <cr>
```

Handler ` RVA 0xFBB81A0 `；selector ` 1 `；EOL ` RVA 0x3483D7A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-902280cc9212c7ca](../../evidence/conditions-sets-056.md#c-902280cc9212c7ca) · [缺口 G-062e9a7a324e8c06](../../evidence/gaps-sets-001.md#g-062e9a7a324e8c06) · [参数 P-c2c2d5c45829e780](../../evidence/parameters-sets-015.md#p-c2c2d5c45829e780) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033745

```text
(config)# do-exec show tunnel groups <cr>
```

Handler ` RVA 0xB50F790 `；selector ` 0 `；EOL ` RVA 0x3483DEE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-9d6ffa18eb5e4ec5](../../evidence/state_effects-sets-033.md#s-9d6ffa18eb5e4ec5)

### path-033718

```text
(config)# do-exec show tunnel interface <cr>
```

Handler ` RVA 0xFBB81A0 `；selector ` 0 `；EOL ` RVA 0x3483D3A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e6c488d28ee8ebdd](../../evidence/conditions-sets-089.md#c-e6c488d28ee8ebdd) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061183

```text
(config)# do-exec show tunnel interface <interface> <cr>
```

Handler ` RVA 0xFBB81A0 `；selector ` 0 `；EOL ` RVA 0x3483D3A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-22360008b917af0a](../../evidence/conditions-sets-013.md#c-22360008b917af0a) · [缺口 G-1514780e4ec0d669](../../evidence/gaps-sets-001.md#g-1514780e4ec0d669) · [参数 P-35a23436c45ca2e2](../../evidence/parameters-sets-005.md#p-35a23436c45ca2e2) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061186

```text
(config)# do-exec show tunnel keys-database <interface> <cr>
```

Handler ` RVA 0xFBB81A0 `；selector ` 4 `；EOL ` RVA 0x3483DB50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7e735dac9bd564ea](../../evidence/conditions-sets-049.md#c-7e735dac9bd564ea) · [缺口 G-d53e370aeb1eeb95](../../evidence/gaps-sets-007.md#g-d53e370aeb1eeb95) · [参数 P-70d4e663699eeff0](../../evidence/parameters-sets-009.md#p-70d4e663699eeff0) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-043521

```text
(config)# do-exec show tunnel source tracking <cr>
```

Handler ` RVA 0xFB7E400 `；selector ` 0 `；EOL ` RVA 0x34827370 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-18a11fd3d6c3c8ef](../../evidence/conditions-sets-010.md#c-18a11fd3d6c3c8ef) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061793

```text
(config)# do-exec show tunnel source tracking <interface> <cr>
```

Handler ` RVA 0xFB7E400 `；selector ` 0 `；EOL ` RVA 0x34827370 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-74216d799a42430d](../../evidence/conditions-sets-045.md#c-74216d799a42430d) · [缺口 G-cf6a9ae180078563](../../evidence/gaps-sets-007.md#g-cf6a9ae180078563) · [参数 P-8b64eab9791c0132](../../evidence/parameters-sets-011.md#p-8b64eab9791c0132) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033861

```text
(config)# do-exec show tunnel tunnel-to <cr>
```

Handler ` RVA 0xB51A1B0 `；selector ` 0 `；EOL ` RVA 0x33793B58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-151e63e012bbff1e](../../evidence/conditions-sets-008.md#c-151e63e012bbff1e) · [状态效果 S-8025a677d116ab36](../../evidence/state_effects-sets-027.md#s-8025a677d116ab36)

### path-061799

```text
(config)# do-exec show tunnel tunnel-to client <?option@555588ce7730> <cr>
```

Handler ` RVA 0xB51A1B0 `；selector ` 0 `；EOL ` RVA 0x33793B58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-44514afecd93975f](../../evidence/conditions-sets-027.md#c-44514afecd93975f) · [缺口 G-8de01f82fd743e83](../../evidence/gaps-sets-005.md#g-8de01f82fd743e83) · [状态效果 S-a802e9b73f5fb0b7](../../evidence/state_effects-sets-035.md#s-a802e9b73f5fb0b7)

### path-027773

```text
(config)# do-exec show udf <cr>
```

Handler ` RVA 0xF9FDE00 `；selector ` 0 `；EOL ` RVA 0x347B8B20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027506

```text
(config)# do-exec show udp <cr>
```

Handler ` RVA 0xCE472D0 `；selector ` 0 `；EOL ` RVA 0x33D07AF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033847

```text
(config)# do-exec show uidp statistics <cr>
```

Handler ` RVA 0x1599CF10 `；selector ` 0 `；EOL ` RVA 0x35DCFE58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-4c126032e38541c7](../../evidence/state_effects-sets-017.md#s-4c126032e38541c7)

### path-062223

```text
(config)# do-exec show uidp user all write <url:dynamic> <cr>
```

Handler ` RVA 0x1599CF10 `；selector ` 0 `；EOL ` RVA 0x35DCFE58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-820f41906721db02](../../evidence/conditions-sets-050.md#c-820f41906721db02) · [缺口 G-15b117230d2ab06c](../../evidence/gaps-sets-001.md#g-15b117230d2ab06c) · [参数 P-d734191a594bdd59](../../evidence/parameters-sets-016.md#p-d734191a594bdd59) · [状态效果 S-fad0a5a3c0afb7e0](../../evidence/state_effects-sets-053.md#s-fad0a5a3c0afb7e0)

### path-033867

```text
(config)# do-exec show usb-devices summary <cr>
```

Handler ` RVA 0x1581A670 `；selector ` 0 `；EOL ` RVA 0x3435D8A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-026907

```text
(config)# do-exec show users <cr>
```

Handler ` RVA 0xDFE03B0 `；selector ` 0 `；EOL ` RVA 0x3415C2C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-039429

```text
(config)# do-exec show vasi pair status <cr>
```

Handler ` RVA 0x1243B640 `；selector ` 0 `；EOL ` RVA 0x358694C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-048320

```text
(config)# do-exec show vasi pair status <number:1..2000> <cr>
```

Handler ` RVA 0x1243B640 `；selector ` 1 `；EOL ` RVA 0x35869498 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` VASI pair number。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-81163eb070625975](../../evidence/parameters-sets-010.md#p-81163eb070625975) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-026849

```text
(config)# do-exec show version <cr>
```

Handler ` RVA 0xE0065E0 `；selector ` 0 `；EOL ` RVA 0x341644A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f0aca990aed40166](../../evidence/conditions-sets-093.md#c-f0aca990aed40166) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027816

```text
(config)# do-exec show virtual-service <cr>
```

Handler ` RVA 0x1590BC10 `；selector ` 1 `；EOL ` RVA 0x35DBD988 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-e5175b3fe9fe3b0f](../../evidence/state_effects-sets-048.md#s-e5175b3fe9fe3b0f)

### path-033903

```text
(config)# do-exec show virtual-service detail <cr>
```

Handler ` RVA 0x1590BC10 `；selector ` 3 `；EOL ` RVA 0x35DBB840 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-e5175b3fe9fe3b0f](../../evidence/state_effects-sets-048.md#s-e5175b3fe9fe3b0f)

### path-033898

```text
(config)# do-exec show virtual-service list <cr>
```

Handler ` RVA 0x1590BC10 `；selector ` 2 `；EOL ` RVA 0x35DBB4C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-e5175b3fe9fe3b0f](../../evidence/state_effects-sets-048.md#s-e5175b3fe9fe3b0f)

### path-052013

```text
(config)# do-exec show virtual-service profile name <string> <cr>
```

Handler ` RVA 0x1590BC10 `；selector ` 4 `；EOL ` RVA 0x35DBBC70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of the appliance。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-0e8111368fd0d6e2](../../evidence/parameters-sets-002.md#p-0e8111368fd0d6e2) · [状态效果 S-e5175b3fe9fe3b0f](../../evidence/state_effects-sets-048.md#s-e5175b3fe9fe3b0f)

### path-052016

```text
(config)# do-exec show virtual-service storage pool list <cr>
```

Handler ` RVA 0x1590BC10 `；selector ` 8 `；EOL ` RVA 0x35DBCAF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-e5175b3fe9fe3b0f](../../evidence/state_effects-sets-048.md#s-e5175b3fe9fe3b0f)

### path-058876

```text
(config)# do-exec show virtual-service storage volume detail volume-name <string> <cr>
```

Handler ` RVA 0x1590BC10 `；selector ` 10 `；EOL ` RVA 0x35DBD128 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of the Storage volume。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-6e223a80f24a1d3d](../../evidence/parameters-sets-009.md#p-6e223a80f24a1d3d) · [状态效果 S-6eecbe6f1c58d278](../../evidence/state_effects-sets-024.md#s-6eecbe6f1c58d278)

### path-052019

```text
(config)# do-exec show virtual-service storage volume list <cr>
```

Handler ` RVA 0x1590BC10 `；selector ` 9 `；EOL ` RVA 0x35DBCDC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-e5175b3fe9fe3b0f](../../evidence/state_effects-sets-048.md#s-e5175b3fe9fe3b0f)

### path-033918

```text
(config)# do-exec show virtual-service tech-support <cr>
```

Handler ` RVA 0x1590BC10 `；selector ` 11 `；EOL ` RVA 0x35DBD3E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-e5175b3fe9fe3b0f](../../evidence/state_effects-sets-048.md#s-e5175b3fe9fe3b0f)

### path-043780

```text
(config)# do-exec show virtual-service trace message <cr>
```

Handler ` RVA 0x1590BC10 `；selector ` 12 `；EOL ` RVA 0x35DBD6F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-e5175b3fe9fe3b0f](../../evidence/state_effects-sets-048.md#s-e5175b3fe9fe3b0f)

### path-052012

```text
(config)# do-exec show virtual-service utilization name <string> <cr>
```

Handler ` RVA 0x1590BC10 `；selector ` 5 `；EOL ` RVA 0x35DBBFE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of the appliance。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-d0cc9b246329dddd](../../evidence/parameters-sets-016.md#p-d0cc9b246329dddd) · [状态效果 S-e5175b3fe9fe3b0f](../../evidence/state_effects-sets-048.md#s-e5175b3fe9fe3b0f)

### path-052015

```text
(config)# do-exec show virtual-service utilization statistics CPU <cr>
```

Handler ` RVA 0x1590BC10 `；selector ` 6 `；EOL ` RVA 0x35DBC2A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-95ae9fb6ffa0da3e](../../evidence/conditions-sets-058.md#c-95ae9fb6ffa0da3e) · [状态效果 S-e5175b3fe9fe3b0f](../../evidence/state_effects-sets-048.md#s-e5175b3fe9fe3b0f)

### path-043775

```text
(config)# do-exec show virtual-service version installed <cr>
```

Handler ` RVA 0x1590BC10 `；selector ` 7 `；EOL ` RVA 0x35DBC700 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-e5175b3fe9fe3b0f](../../evidence/state_effects-sets-048.md#s-e5175b3fe9fe3b0f)

### path-027633

```text
(config)# do-exec show vlan <cr>
```

Handler ` RVA 0x15C743A0 `；selector ` 0 `；EOL ` RVA 0x35E03988 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-982b293faaab1b0d](../../evidence/conditions-sets-059.md#c-982b293faaab1b0d) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031883

```text
(config)# do-exec show vlan brief <cr>
```

Handler ` RVA 0x15C743A0 `；selector ` 3 `；EOL ` RVA 0x35DFBB58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031958

```text
(config)# do-exec show vlan counters <cr>
```

Handler ` RVA 0x15C743A0 `；selector ` 12 `；EOL ` RVA 0x35DFCA78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fa9261170ca1853a](../../evidence/conditions-sets-097.md#c-fa9261170ca1853a) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-049698

```text
(config)# do-exec show vlan dot1q tag native <cr>
```

Handler ` RVA 0x15FEB9E0 `；selector ` 3 `；EOL ` RVA 0x35E93C90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-982b293faaab1b0d](../../evidence/conditions-sets-059.md#c-982b293faaab1b0d) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032081

```text
(config)# do-exec show vlan group <cr>
```

Handler ` RVA 0x15EB6910 `；selector ` 0 `；EOL ` RVA 0x35E60DD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-982b293faaab1b0d](../../evidence/conditions-sets-059.md#c-982b293faaab1b0d) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-049718

```text
(config)# do-exec show vlan group group-name <string> <cr>
```

Handler ` RVA 0x15EB6910 `；selector ` 1 `；EOL ` RVA 0x35E60E78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` VLAN group name。

[条件 C-982b293faaab1b0d](../../evidence/conditions-sets-059.md#c-982b293faaab1b0d) · [参数 P-b285a6d56a666287](../../evidence/parameters-sets-014.md#p-b285a6d56a666287) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-055597

```text
(config)# do-exec show vlan group group-name <string> user-count <cr>
```

Handler ` RVA 0x15EB6910 `；selector ` 2 `；EOL ` RVA 0x35E60E50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` VLAN group name。

[条件 C-982b293faaab1b0d](../../evidence/conditions-sets-059.md#c-982b293faaab1b0d) · [参数 P-b285a6d56a666287](../../evidence/parameters-sets-014.md#p-b285a6d56a666287) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040432

```text
(config)# do-exec show vlan id <string> <cr>
```

Handler ` RVA 0x15C743A0 `；selector ` 2 `；EOL ` RVA 0x35DFC568 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` ISL VLAN IDs 1-1005。

[条件 C-1b68772819e4472f](../../evidence/conditions-sets-011.md#c-1b68772819e4472f) · [参数 P-cf337acc24838790](../../evidence/parameters-sets-016.md#p-cf337acc24838790) · [状态效果 S-472db9235c3ce8b2](../../evidence/state_effects-sets-016.md#s-472db9235c3ce8b2)

### path-049333

```text
(config)# do-exec show vlan id <string> counters <cr>
```

Handler ` RVA 0x15C743A0 `；selector ` 11 `；EOL ` RVA 0x35DFC248 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` ISL VLAN IDs 1-1005。

[条件 C-920684b806c09ca2](../../evidence/conditions-sets-056.md#c-920684b806c09ca2) · [参数 P-cf337acc24838790](../../evidence/parameters-sets-016.md#p-cf337acc24838790) · [状态效果 S-472db9235c3ce8b2](../../evidence/state_effects-sets-016.md#s-472db9235c3ce8b2)

### path-032016

```text
(config)# do-exec show vlan ifindex <cr>
```

Handler ` RVA 0x15C743A0 `；selector ` 9 `；EOL ` RVA 0x35DFDB58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0a94af0c78f9c696](../../evidence/conditions-sets-004.md#c-0a94af0c78f9c696) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040521

```text
(config)# do-exec show vlan internal usage <cr>
```

Handler ` RVA 0x15C743A0 `；selector ` 13 `；EOL ` RVA 0x35DFE1A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-15a8f99ee7bc8d9a](../../evidence/conditions-sets-009.md#c-15a8f99ee7bc8d9a) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031902

```text
(config)# do-exec show vlan mtu <cr>
```

Handler ` RVA 0x15C743A0 `；selector ` 19 `；EOL ` RVA 0x35DFBE00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040354

```text
(config)# do-exec show vlan name <string> <cr>
```

Handler ` RVA 0x15C743A0 `；selector ` 1 `；EOL ` RVA 0x35DFCE40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` A VTP VLAN name。

[条件 C-aec9831c7b46259a](../../evidence/conditions-sets-068.md#c-aec9831c7b46259a) · [参数 P-453f1d4b5b291239](../../evidence/parameters-sets-006.md#p-453f1d4b5b291239) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032004

```text
(config)# do-exec show vlan private-vlan <cr>
```

Handler ` RVA 0x15C743A0 `；selector ` 8 `；EOL ` RVA 0x35DFD288 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0906827d33e6635f](../../evidence/conditions-sets-004.md#c-0906827d33e6635f) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031999

```text
(config)# do-exec show vlan remote-span <cr>
```

Handler ` RVA 0x15C743A0 `；selector ` 14 `；EOL ` RVA 0x35DFD568 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8ae6793ebd38621b](../../evidence/conditions-sets-054.md#c-8ae6793ebd38621b) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032041

```text
(config)# do-exec show vlan summary <cr>
```

Handler ` RVA 0x15C743A0 `；selector ` 10 `；EOL ` RVA 0x35DFDE40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-11932791c89a4afb](../../evidence/conditions-sets-007.md#c-11932791c89a4afb) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032031

```text
(config)# do-exec show vlan uni-vlan <cr>
```

Handler ` RVA 0x15C743A0 `；selector ` 20 `；EOL ` RVA 0x35DFD8B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-793ff42330b67aa7](../../evidence/conditions-sets-047.md#c-793ff42330b67aa7) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031562

```text
(config)# do-exec show vlan-autoconfig access-interface <cr>
```

Handler ` RVA 0x112BC900 `；selector ` 2 `；EOL ` RVA 0x3544F380 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031511

```text
(config)# do-exec show vlan-autoconfig error-history <cr>
```

Handler ` RVA 0x112BC900 `；selector ` 3 `；EOL ` RVA 0x3544EE30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031535

```text
(config)# do-exec show vlan-autoconfig statistics <cr>
```

Handler ` RVA 0x112BC900 `；selector ` 5 `；EOL ` RVA 0x3544F0D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031486

```text
(config)# do-exec show vlan-autoconfig summary <cr>
```

Handler ` RVA 0x112BC900 `；selector ` 4 `；EOL ` RVA 0x3544EB88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031650

```text
(config)# do-exec show vlan-autoconfig vlan-interface <cr>
```

Handler ` RVA 0x112BC900 `；selector ` 1 `；EOL ` RVA 0x3544F9B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-85bcce34e1701c89](../../evidence/conditions-sets-052.md#c-85bcce34e1701c89) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061511

```text
(config)# do-exec show vlan-autoconfig vlan-interface <interface> <number:0..4294967295> <cr>
```

Handler ` RVA 0x112BC900 `；selector ` 8 `；EOL ` RVA 0x3544F9F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` sub-interface id。

[条件 C-168fd9af341d272a](../../evidence/conditions-sets-009.md#c-168fd9af341d272a) · [缺口 G-bad69a13442c1000](../../evidence/gaps-sets-007.md#g-bad69a13442c1000) · [参数 P-ab58a1db618dfaf0](../../evidence/parameters-sets-013.md#p-ab58a1db618dfaf0) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062535

```text
(config)# do-exec show vlan-autoconfig vlan-interface <interface> s-vlan <number:0..4096> c-vlan <number:0..4096> <cr>
```

Handler ` RVA 0x112BC900 `；selector ` 7 `；EOL ` RVA 0x3544FD70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` s-vlan number；` unsigned_number ` c-vlan number 。

[条件 C-168fd9af341d272a](../../evidence/conditions-sets-009.md#c-168fd9af341d272a) · [缺口 G-bad69a13442c1000](../../evidence/gaps-sets-007.md#g-bad69a13442c1000) · [参数 P-b269bc407099256b](../../evidence/parameters-sets-014.md#p-b269bc407099256b) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-039195

```text
(config)# do-exec show vlan-autoconfig vlan-interface detailed <cr>
```

Handler ` RVA 0x112BC900 `；selector ` 6 `；EOL ` RVA 0x3544F668 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027604

```text
(config)# do-exec show vlan-range <cr>
```

Handler ` RVA 0x11D3AEA0 `；selector ` 11 `；EOL ` RVA 0x356D3F18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027608

```text
(config)# do-exec show vlans <cr>
```

Handler ` RVA 0x11D205F0 `；selector ` 0 `；EOL ` RVA 0x356CFDF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-060711

```text
(config)# do-exec show vlans <number:dynamic> <cr>
```

Handler ` RVA 0x11D205F0 `；selector ` 1 `；EOL ` RVA 0x356CF328 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Display configuration for a particular vLAN ID.。

[条件 C-0c69725ab6b30c39](../../evidence/conditions-sets-005.md#c-0c69725ab6b30c39) · [缺口 G-102f8880eb878ea2](../../evidence/gaps-sets-001.md#g-102f8880eb878ea2) · [参数 P-b6261e18de676cbc](../../evidence/parameters-sets-014.md#p-b6261e18de676cbc) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031773

```text
(config)# do-exec show vlans dot1q <cr>
```

Handler ` RVA 0x11D21620 `；selector ` 0 `；EOL ` RVA 0x356D0578 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d6f3a85c60faed4b](../../evidence/conditions-sets-083.md#c-d6f3a85c60faed4b) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031814

```text
(config)# do-exec show vlans dot1q <cr>
```

Handler ` RVA 0x11D21620 `；selector ` 1 `；EOL ` RVA 0x356CFEA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5558c1df010f959c](../../evidence/conditions-sets-033.md#c-5558c1df010f959c) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-060991

```text
(config)# do-exec show vlans dot1q <interface> <cr>
```

Handler ` RVA 0x11D21620 `；selector ` 0 `；EOL ` RVA 0x356D0578 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e82843110f44264b](../../evidence/conditions-sets-090.md#c-e82843110f44264b) · [缺口 G-b49f4956e4b6fa5b](../../evidence/gaps-sets-006.md#g-b49f4956e4b6fa5b) · [参数 P-0b4ec55f07728ed1](../../evidence/parameters-sets-001.md#p-0b4ec55f07728ed1) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-060995

```text
(config)# do-exec show vlans dot1q <interface> <cr>
```

Handler ` RVA 0x11D21620 `；selector ` 1 `；EOL ` RVA 0x356CFEA8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ec18f698f525218c](../../evidence/conditions-sets-091.md#c-ec18f698f525218c) · [缺口 G-007052556d9325c0](../../evidence/gaps-sets-001.md#g-007052556d9325c0) · [参数 P-e73ce4515344fc5c](../../evidence/parameters-sets-017.md#p-e73ce4515344fc5c) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031598

```text
(config)# do-exec show vlans summary <cr>
```

Handler ` RVA 0x11D1F260 `；selector ` 0 `；EOL ` RVA 0x356CF5D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031616

```text
(config)# do-exec show vlans tokenring <cr>
```

Handler ` RVA 0x11D1F1E0 `；selector ` 0 `；EOL ` RVA 0x356CF880 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031635

```text
(config)# do-exec show vlans tr-isl <cr>
```

Handler ` RVA 0x11D1ED50 `；selector ` 0 `；EOL ` RVA 0x356CFB28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027697

```text
(config)# do-exec show vnet <cr>
```

Handler ` RVA 0x12467AB0 `；selector ` 0 `；EOL ` RVA 0x358759D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-874daff06cabb1a9](../../evidence/conditions-sets-052.md#c-874daff06cabb1a9) · [状态效果 S-229131454854c87a](../../evidence/state_effects-sets-008.md#s-229131454854c87a)

### path-060735

```text
(config)# do-exec show vnet <string> <cr>
```

Handler ` RVA 0x12467AB0 `；selector ` 0 `；EOL ` RVA 0x358759D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` VRF name。

[条件 C-4f4767f5b3bb44a8](../../evidence/conditions-sets-031.md#c-4f4767f5b3bb44a8) · [缺口 G-d519d462d25fd1d7](../../evidence/gaps-sets-007.md#g-d519d462d25fd1d7) · [参数 P-72392b9319620dff](../../evidence/parameters-sets-009.md#p-72392b9319620dff) · [状态效果 S-99ed74ca6cde6619](../../evidence/state_effects-sets-033.md#s-99ed74ca6cde6619)

### path-041887

```text
(config)# do-exec show vpdn dead-cache all <cr>
```

Handler ` RVA 0x11DB8630 `；selector ` 1 `；EOL ` RVA 0x3570B978 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-5b74ade2176a0e3a](../../evidence/state_effects-sets-020.md#s-5b74ade2176a0e3a)

### path-050627

```text
(config)# do-exec show vpdn dead-cache group <string> <cr>
```

Handler ` RVA 0x11DB8630 `；selector ` 2 `；EOL ` RVA 0x3570B6F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of VPDN group。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-ab5305a87287f44c](../../evidence/parameters-sets-013.md#p-ab5305a87287f44c) · [状态效果 S-5b74ade2176a0e3a](../../evidence/state_effects-sets-020.md#s-5b74ade2176a0e3a)

### path-032736

```text
(config)# do-exec show vpdn domain <cr>
```

Handler ` RVA 0x11D45010 `；selector ` 0 `；EOL ` RVA 0x3570AB50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032741

```text
(config)# do-exec show vpdn group <cr>
```

Handler ` RVA 0x11DB8260 `；selector ` 0 `；EOL ` RVA 0x3570A128 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-041772

```text
(config)# do-exec show vpdn group <string> <cr>
```

Handler ` RVA 0x11DB9580 `；selector ` 20 `；EOL ` RVA 0x3570A438 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of VPDN group。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-aaf221e0011cb9dd](../../evidence/parameters-sets-013.md#p-aaf221e0011cb9dd) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-050543

```text
(config)# do-exec show vpdn group <string> domain <cr>
```

Handler ` RVA 0x11DB9580 `；selector ` 22 `；EOL ` RVA 0x3570A410 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of VPDN group。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-aaf221e0011cb9dd](../../evidence/parameters-sets-013.md#p-aaf221e0011cb9dd) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-050512

```text
(config)# do-exec show vpdn group <string> endpoint <cr>
```

Handler ` RVA 0x11DB9580 `；selector ` 21 `；EOL ` RVA 0x3570A168 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of VPDN group。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-aaf221e0011cb9dd](../../evidence/parameters-sets-013.md#p-aaf221e0011cb9dd) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-041942

```text
(config)# do-exec show vpdn group-select Default <cr>
```

Handler ` RVA 0x11DBAB80 `；selector ` 138 `；EOL ` RVA 0x3570CC18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-41c5afc31b95e7b6](../../evidence/conditions-sets-026.md#c-41c5afc31b95e7b6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-041910

```text
(config)# do-exec show vpdn group-select Summary <cr>
```

Handler ` RVA 0x11DBAB80 `；selector ` 139 `；EOL ` RVA 0x3570C970 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-41c5afc31b95e7b6](../../evidence/conditions-sets-026.md#c-41c5afc31b95e7b6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-059581

```text
(config)# do-exec show vpdn group-select keys hostname <string> source-ip <address> <cr>
```

Handler ` RVA 0x11DBAB80 `；selector ` 140 `；EOL ` RVA 0x3570D028 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Hostname of user；` address ` Source IP of user。

[条件 C-41c5afc31b95e7b6](../../evidence/conditions-sets-026.md#c-41c5afc31b95e7b6) · [参数 P-9c6a85d6ffef3c2d](../../evidence/parameters-sets-012.md#p-9c6a85d6ffef3c2d) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-041716

```text
(config)# do-exec show vpdn history failure <cr>
```

Handler ` RVA 0x11DC0FF0 `；selector ` 0 `；EOL ` RVA 0x35709B80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-041705

```text
(config)# do-exec show vpdn history fsm <cr>
```

Handler ` RVA 0x11D81400 `；selector ` 0 `；EOL ` RVA 0x35709E00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-041914

```text
(config)# do-exec show vpdn lsg all <cr>
```

Handler ` RVA 0x11DB8630 `；selector ` 1 `；EOL ` RVA 0x3570BF98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-9e7abe1b5a0caf55](../../evidence/state_effects-sets-034.md#s-9e7abe1b5a0caf55)

### path-050649

```text
(config)# do-exec show vpdn lsg group <string> <cr>
```

Handler ` RVA 0x11DB8630 `；selector ` 2 `；EOL ` RVA 0x3570BD18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of VPDN group。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-c7153b712117ee31](../../evidence/parameters-sets-015.md#p-c7153b712117ee31) · [状态效果 S-9e7abe1b5a0caf55](../../evidence/state_effects-sets-034.md#s-9e7abe1b5a0caf55)

### path-032763

```text
(config)# do-exec show vpdn multilink <cr>
```

Handler ` RVA 0x11DB8470 `；selector ` 0 `；EOL ` RVA 0x3570B0A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032747

```text
(config)# do-exec show vpdn redirect <cr>
```

Handler ` RVA 0x11DB8520 `；selector ` 0 `；EOL ` RVA 0x3570ADF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032884

```text
(config)# do-exec show vpdn redundancy <cr>
```

Handler ` RVA 0x11DC5470 `；selector ` 1 `；EOL ` RVA 0x3570C378 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b11a9c5ffaa11052](../../evidence/conditions-sets-068.md#c-b11a9c5ffaa11052) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-041941

```text
(config)# do-exec show vpdn redundancy all <cr>
```

Handler ` RVA 0x11DC5470 `；selector ` 4 `；EOL ` RVA 0x3570C410 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b11a9c5ffaa11052](../../evidence/conditions-sets-068.md#c-b11a9c5ffaa11052) · [状态效果 S-d028a75a778605b6](../../evidence/state_effects-sets-044.md#s-d028a75a778605b6)

### path-032780

```text
(config)# do-exec show vpdn scalability <cr>
```

Handler ` RVA 0x11DE4800 `；selector ` 0 `；EOL ` RVA 0x3570B348 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6a240251bfde7090](../../evidence/conditions-sets-041.md#c-6a240251bfde7090) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-050465

```text
(config)# do-exec show vpdn statistics call fsm <cr>
```

Handler ` RVA 0x11D9C160 `；selector ` 0 `；EOL ` RVA 0x357091F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-050480

```text
(config)# do-exec show vpdn statistics mgr fsm <cr>
```

Handler ` RVA 0x11DA0AF0 `；selector ` 0 `；EOL ` RVA 0x357094C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-050478

```text
(config)# do-exec show vpdn subscriber statistics fsm <cr>
```

Handler ` RVA 0x11E16260 `；selector ` 0 `；EOL ` RVA 0x35709818 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027641

```text
(config)# do-exec show vrf <cr>
```

Handler ` RVA 0xDC3F530 `；selector ` 0 `；EOL ` RVA 0x34014230 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6e776e3b9bfd73fc](../../evidence/conditions-sets-043.md#c-6e776e3b9bfd73fc) · [状态效果 S-7dfa8160e54e924c](../../evidence/state_effects-sets-027.md#s-7dfa8160e54e924c)

### path-060723

```text
(config)# do-exec show vrf <string> <cr>
```

Handler ` RVA 0xDC3F530 `；selector ` 0 `；EOL ` RVA 0x34014230 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` VRF name。

[条件 C-b8fd266fc6ae9979](../../evidence/conditions-sets-071.md#c-b8fd266fc6ae9979) · [缺口 G-33d2f7627fcb3c97](../../evidence/gaps-sets-002.md#g-33d2f7627fcb3c97) · [参数 P-518a8315ad3a6c95](../../evidence/parameters-sets-007.md#p-518a8315ad3a6c95) · [状态效果 S-b69f3c41d21202fc](../../evidence/state_effects-sets-039.md#s-b69f3c41d21202fc)

### path-061645

```text
(config)# do-exec show vrf ipv4 <?option@555589568980> list <cr>
```

Handler ` RVA 0x12465980 `；selector ` 0 `；EOL ` RVA 0x35872DF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-cd775b5e82665974](../../evidence/conditions-sets-079.md#c-cd775b5e82665974) · [缺口 G-485edfc0f2732772](../../evidence/gaps-sets-003.md#g-485edfc0f2732772) · [状态效果 S-302f6abd97ea92f7](../../evidence/state_effects-sets-011.md#s-302f6abd97ea92f7)

### path-061626

```text
(config)# do-exec show vrf ipv4 <?option@555589568980> select <cr>
```

Handler ` RVA 0xFADE7A0 `；selector ` 0 `；EOL ` RVA 0x34808200 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5745206f701b2f08](../../evidence/conditions-sets-034.md#c-5745206f701b2f08) · [缺口 G-485edfc0f2732772](../../evidence/gaps-sets-003.md#g-485edfc0f2732772) · [状态效果 S-302f6abd97ea92f7](../../evidence/state_effects-sets-011.md#s-302f6abd97ea92f7)

### path-032208

```text
(config)# do-exec show vrf list <cr>
```

Handler ` RVA 0x12465980 `；selector ` 0 `；EOL ` RVA 0x35872DF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-84330cfd5eae4219](../../evidence/conditions-sets-051.md#c-84330cfd5eae4219) · [状态效果 S-7dfa8160e54e924c](../../evidence/state_effects-sets-027.md#s-7dfa8160e54e924c)

### path-061030

```text
(config)# do-exec show vrf list <string> <cr>
```

Handler ` RVA 0x12465860 `；selector ` 0 `；EOL ` RVA 0x35872B00 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` VRF list name。

[条件 C-84330cfd5eae4219](../../evidence/conditions-sets-051.md#c-84330cfd5eae4219) · [缺口 G-49a5f97795ac397a](../../evidence/gaps-sets-003.md#g-49a5f97795ac397a) · [参数 P-3abb58713749cce3](../../evidence/parameters-sets-005.md#p-3abb58713749cce3) · [状态效果 S-dca5c88ec904a606](../../evidence/state_effects-sets-047.md#s-dca5c88ec904a606)

### path-032138

```text
(config)# do-exec show vrf select <cr>
```

Handler ` RVA 0xFADE7A0 `；selector ` 0 `；EOL ` RVA 0x34808200 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bfbccc878ae22b6c](../../evidence/conditions-sets-074.md#c-bfbccc878ae22b6c) · [状态效果 S-7dfa8160e54e924c](../../evidence/state_effects-sets-027.md#s-7dfa8160e54e924c)

### path-027629

```text
(config)# do-exec show vrrp <cr>
```

Handler ` RVA 0x133C8FB0 `；selector ` 0 `；EOL ` RVA 0x35A80120 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1d72f7c2e0fb4355](../../evidence/conditions-sets-011.md#c-1d72f7c2e0fb4355) · [状态效果 S-dccdcb41f9b13737](../../evidence/state_effects-sets-047.md#s-dccdcb41f9b13737)

### path-062715

```text
(config)# do-exec show vrrp <cr>
```

Handler ` RVA 0xE2E3990 `；selector ` 0 `；EOL ` RVA 0x3429CC50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e190a029af721344](../../evidence/conditions-sets-087.md#c-e190a029af721344) · [缺口 G-a03dbb0ecc97c08a](../../evidence/gaps-sets-006.md#g-a03dbb0ecc97c08a) · [状态效果 S-619c2160dbd0c384](../../evidence/state_effects-sets-021.md#s-619c2160dbd0c384)

### path-060720

```text
(config)# do-exec show vrrp <interface> <cr>
```

Handler ` RVA 0x133C8FB0 `；selector ` 0 `；EOL ` RVA 0x35A80120 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3a7c38de9c9d198a](../../evidence/conditions-sets-023.md#c-3a7c38de9c9d198a) · [缺口 G-ccd625fe52c5b187](../../evidence/gaps-sets-007.md#g-ccd625fe52c5b187) · [参数 P-bb962e0c6c6e61f4](../../evidence/parameters-sets-014.md#p-bb962e0c6c6e61f4) · [状态效果 S-dccdcb41f9b13737](../../evidence/state_effects-sets-047.md#s-dccdcb41f9b13737)

### path-062777

```text
(config)# do-exec show vrrp internal summary <cr>
```

Handler ` RVA 0xE2E4790 `；selector ` 0 `；EOL ` RVA 0x3429C728 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a92c2545fecf1691](../../evidence/conditions-sets-065.md#c-a92c2545fecf1691) · [缺口 G-a03dbb0ecc97c08a](../../evidence/gaps-sets-006.md#g-a03dbb0ecc97c08a) · [状态效果 S-619c2160dbd0c384](../../evidence/state_effects-sets-021.md#s-619c2160dbd0c384)

### path-031301

```text
(config)# do-exec show vrrs accounting <cr>
```

Handler ` RVA 0xE2FD270 `；selector ` 0 `；EOL ` RVA 0x342A3250 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-61e5893443b8636b](../../evidence/conditions-sets-038.md#c-61e5893443b8636b) · [状态效果 S-bad82f326e5edf57](../../evidence/state_effects-sets-039.md#s-bad82f326e5edf57)

### path-031897

```text
(config)# do-exec show vrrs client <cr>
```

Handler ` RVA 0x133F9730 `；selector ` 0 `；EOL ` RVA 0x35A8A930 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-20e24cf3a0e61aa9](../../evidence/conditions-sets-013.md#c-20e24cf3a0e61aa9) · [状态效果 S-cbb571fdedfb2fc1](../../evidence/state_effects-sets-043.md#s-cbb571fdedfb2fc1)

### path-031289

```text
(config)# do-exec show vrrs clients <cr>
```

Handler ` RVA 0xE2F9FA0 `；selector ` 1 `；EOL ` RVA 0x3429FE60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cbfca79d665be9c8](../../evidence/conditions-sets-078.md#c-cbfca79d665be9c8) · [状态效果 S-3192f249f575fcb0](../../evidence/state_effects-sets-011.md#s-3192f249f575fcb0)

### path-060773

```text
(config)# do-exec show vrrs fwd <interface> <cr>
```

Handler ` RVA 0xE2FEDD0 `；selector ` 3 `；EOL ` RVA 0x342A6578 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9e274b9366edd6bc](../../evidence/conditions-sets-061.md#c-9e274b9366edd6bc) · [缺口 G-f55dde22fb03d0e8](../../evidence/gaps-sets-008.md#g-f55dde22fb03d0e8) · [参数 P-33c6df16a4fbcdae](../../evidence/parameters-sets-004.md#p-33c6df16a4fbcdae) · [状态效果 S-3c27c3debc29351e](../../evidence/state_effects-sets-013.md#s-3c27c3debc29351e)

### path-031304

```text
(config)# do-exec show vrrs group <cr>
```

Handler ` RVA 0xE2F9FA0 `；selector ` 2 `；EOL ` RVA 0x3429FBE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cbfca79d665be9c8](../../evidence/conditions-sets-078.md#c-cbfca79d665be9c8) · [状态效果 S-3192f249f575fcb0](../../evidence/state_effects-sets-011.md#s-3192f249f575fcb0)

### path-031344

```text
(config)# do-exec show vrrs internal <cr>
```

Handler ` RVA 0xE2F9FA0 `；selector ` 4 `；EOL ` RVA 0x342A0148 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-dd79ce7347f4b389](../../evidence/conditions-sets-085.md#c-dd79ce7347f4b389) · [状态效果 S-3192f249f575fcb0](../../evidence/state_effects-sets-011.md#s-3192f249f575fcb0)

### path-031929

```text
(config)# do-exec show vrrs pathway <cr>
```

Handler ` RVA 0x133F94F0 `；selector ` 0 `；EOL ` RVA 0x35A8B1B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-09af84b0ed28b07e](../../evidence/conditions-sets-004.md#c-09af84b0ed28b07e) · [状态效果 S-cbb571fdedfb2fc1](../../evidence/state_effects-sets-043.md#s-cbb571fdedfb2fc1)

### path-060999

```text
(config)# do-exec show vrrs pathway <interface> <cr>
```

Handler ` RVA 0x133F94F0 `；selector ` 0 `；EOL ` RVA 0x35A8B1B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a19eb5682d32c6ad](../../evidence/conditions-sets-062.md#c-a19eb5682d32c6ad) · [缺口 G-8f85f7232cc80b9c](../../evidence/gaps-sets-005.md#g-8f85f7232cc80b9c) · [参数 P-836e2c13e1d6e67b](../../evidence/parameters-sets-010.md#p-836e2c13e1d6e67b) · [状态效果 S-cbb571fdedfb2fc1](../../evidence/state_effects-sets-043.md#s-cbb571fdedfb2fc1)

### path-040084

```text
(config)# do-exec show vrrs pathway address <cr>
```

Handler ` RVA 0x133F9490 `；selector ` 0 `；EOL ` RVA 0x35A8B460 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-09af84b0ed28b07e](../../evidence/conditions-sets-004.md#c-09af84b0ed28b07e) · [状态效果 S-cbb571fdedfb2fc1](../../evidence/state_effects-sets-043.md#s-cbb571fdedfb2fc1)

### path-034548

```text
(config)# do-exec show vrrs plugin database <cr>
```

Handler ` RVA 0xE2FEDD0 `；selector ` 2 `；EOL ` RVA 0x342A6228 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-57c5b16611c0637c](../../evidence/conditions-sets-034.md#c-57c5b16611c0637c) · [状态效果 S-3c27c3debc29351e](../../evidence/state_effects-sets-013.md#s-3c27c3debc29351e)

### path-031930

```text
(config)# do-exec show vrrs server <cr>
```

Handler ` RVA 0x133F97D0 `；selector ` 0 `；EOL ` RVA 0x35A8ADD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d5af9483c87d3242](../../evidence/conditions-sets-082.md#c-d5af9483c87d3242) · [状态效果 S-40a0ef3a4a2a1294](../../evidence/state_effects-sets-014.md#s-40a0ef3a4a2a1294)

### path-031237

```text
(config)# do-exec show vrrs summary <cr>
```

Handler ` RVA 0xE2F9FA0 `；selector ` 3 `；EOL ` RVA 0x3429F8D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cbfca79d665be9c8](../../evidence/conditions-sets-078.md#c-cbfca79d665be9c8) · [状态效果 S-3192f249f575fcb0](../../evidence/state_effects-sets-011.md#s-3192f249f575fcb0)

### path-031845

```text
(config)# do-exec show vrrs tag <cr>
```

Handler ` RVA 0x133F9880 `；selector ` 0 `；EOL ` RVA 0x35A8A648 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d5af9483c87d3242](../../evidence/conditions-sets-082.md#c-d5af9483c87d3242) · [状态效果 S-cbb571fdedfb2fc1](../../evidence/state_effects-sets-043.md#s-cbb571fdedfb2fc1)

### path-027718

```text
(config)# do-exec show vtemplate <cr>
```

Handler ` RVA 0x105C73D0 `；selector ` 0 `；EOL ` RVA 0x34BB1770 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-869564b610b8b12c](../../evidence/conditions-sets-052.md#c-869564b610b8b12c) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-060737

```text
(config)# do-exec show vtemplate <number:dynamic> <cr>
```

Handler ` RVA 0x105C73D0 `；selector ` 0 `；EOL ` RVA 0x34BB1770 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Virtual Template interface number。

[条件 C-25ecbac06ef52793](../../evidence/conditions-sets-015.md#c-25ecbac06ef52793) · [缺口 G-4b3792125a15a6b9](../../evidence/gaps-sets-003.md#g-4b3792125a15a6b9) · [参数 P-2a1bda5a5cc7e281](../../evidence/parameters-sets-004.md#p-2a1bda5a5cc7e281) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033018

```text
(config)# do-exec show vtemplate queue <cr>
```

Handler ` RVA 0x105C73D0 `；selector ` 1 `；EOL ` RVA 0x34BB14D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-22436537f02c5c24](../../evidence/conditions-sets-013.md#c-22436537f02c5c24) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031904

```text
(config)# do-exec show vtp counters <cr>
```

Handler ` RVA 0x15C743A0 `；selector ` 4 `；EOL ` RVA 0x35DFAAE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031943

```text
(config)# do-exec show vtp devices <cr>
```

Handler ` RVA 0x15C743A0 `；selector ` 17 `；EOL ` RVA 0x35DFAE20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040121

```text
(config)# do-exec show vtp devices conflicts <cr>
```

Handler ` RVA 0x15C743A0 `；selector ` 18 `；EOL ` RVA 0x35DFADF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031928

```text
(config)# do-exec show vtp interface <cr>
```

Handler ` RVA 0x15C743A0 `；selector ` 16 `；EOL ` RVA 0x35DFA828 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-35eb97e8264076bc](../../evidence/conditions-sets-021.md#c-35eb97e8264076bc) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061002

```text
(config)# do-exec show vtp interface <interface> <cr>
```

Handler ` RVA 0x15C743A0 `；selector ` 16 `；EOL ` RVA 0x35DFA828 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5911aae7da7fc648](../../evidence/conditions-sets-035.md#c-5911aae7da7fc648) · [缺口 G-b7b609c0cc5c9ccd](../../evidence/gaps-sets-006.md#g-b7b609c0cc5c9ccd) · [参数 P-c3c390b5204c77dc](../../evidence/parameters-sets-015.md#p-c3c390b5204c77dc) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031939

```text
(config)# do-exec show vtp password <cr>
```

Handler ` RVA 0x15C743A0 `；selector ` 15 `；EOL ` RVA 0x35DFB2F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031892

```text
(config)# do-exec show vtp status <cr>
```

Handler ` RVA 0x15C743A0 `；selector ` 7 `；EOL ` RVA 0x35E03BF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031980

```text
(config)# do-exec show vtp trunks <cr>
```

Handler ` RVA 0x15C743A0 `；selector ` 5 `；EOL ` RVA 0x35DFB600 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040203

```text
(config)# do-exec show vtp trunks all <cr>
```

Handler ` RVA 0x15C743A0 `；selector ` 6 `；EOL ` RVA 0x35DFB5D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027606

```text
(config)# do-exec show wccp <cr>
```

Handler ` RVA 0x10AD36D0 `；selector ` 0 `；EOL ` RVA 0x34C9FC18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8ced8bdbc4811d5e](../../evidence/conditions-sets-055.md#c-8ced8bdbc4811d5e) · [状态效果 S-024fd6f0d4045b94](../../evidence/state_effects-sets-001.md#s-024fd6f0d4045b94)

### path-031571

```text
(config)# do-exec show wccp capabilities <cr>
```

Handler ` RVA 0x10AD36D0 `；selector ` 14 `；EOL ` RVA 0x34C9D3D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-720871d41476383a](../../evidence/conditions-sets-044.md#c-720871d41476383a) · [状态效果 S-024fd6f0d4045b94](../../evidence/state_effects-sets-001.md#s-024fd6f0d4045b94)

### path-039233

```text
(config)# do-exec show wccp capabilities internal <cr>
```

Handler ` RVA 0x10AD36D0 `；selector ` 15 `；EOL ` RVA 0x34C9D440 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1f6646a9c1f3445e](../../evidence/conditions-sets-012.md#c-1f6646a9c1f3445e) · [状态效果 S-024fd6f0d4045b94](../../evidence/state_effects-sets-001.md#s-024fd6f0d4045b94)

### path-048161

```text
(config)# do-exec show wccp capabilities internal data <cr>
```

Handler ` RVA 0x10AD36D0 `；selector ` 16 `；EOL ` RVA 0x34C9D418 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e9500134c9e33aa6](../../evidence/conditions-sets-090.md#c-e9500134c9e33aa6) · [状态效果 S-024fd6f0d4045b94](../../evidence/state_effects-sets-001.md#s-024fd6f0d4045b94)

### path-039076

```text
(config)# do-exec show wccp global counters <cr>
```

Handler ` RVA 0x10AD36D0 `；selector ` 3 `；EOL ` RVA 0x34C9C2E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-024fd6f0d4045b94](../../evidence/state_effects-sets-001.md#s-024fd6f0d4045b94)

### path-038937

```text
(config)# do-exec show wccp global internal <cr>
```

Handler ` RVA 0x10AB5B50 `；selector ` 0 `；EOL ` RVA 0x34C9BFD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-614a53ba8084353a](../../evidence/conditions-sets-038.md#c-614a53ba8084353a) · [状态效果 S-024fd6f0d4045b94](../../evidence/state_effects-sets-001.md#s-024fd6f0d4045b94)

### path-031574

```text
(config)# do-exec show wccp interfaces <cr>
```

Handler ` RVA 0x10AD36D0 `；selector ` 10 `；EOL ` RVA 0x34C9CB78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-024fd6f0d4045b94](../../evidence/state_effects-sets-001.md#s-024fd6f0d4045b94)

### path-039107

```text
(config)# do-exec show wccp interfaces cef <cr>
```

Handler ` RVA 0x10AD36D0 `；selector ` 13 `；EOL ` RVA 0x34C9CB50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-024fd6f0d4045b94](../../evidence/state_effects-sets-001.md#s-024fd6f0d4045b94)

### path-039050

```text
(config)# do-exec show wccp interfaces counts <cr>
```

Handler ` RVA 0x10AD36D0 `；selector ` 12 `；EOL ` RVA 0x34C9C8A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-024fd6f0d4045b94](../../evidence/state_effects-sets-001.md#s-024fd6f0d4045b94)

### path-038990

```text
(config)# do-exec show wccp interfaces detail <cr>
```

Handler ` RVA 0x10AD36D0 `；selector ` 11 `；EOL ` RVA 0x34C9C600 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-024fd6f0d4045b94](../../evidence/state_effects-sets-001.md#s-024fd6f0d4045b94)

### path-031517

```text
(config)# do-exec show wccp summary <cr>
```

Handler ` RVA 0x10AD36D0 `；selector ` 17 `；EOL ` RVA 0x34C9D060 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-024fd6f0d4045b94](../../evidence/state_effects-sets-001.md#s-024fd6f0d4045b94)

### path-039532

```text
(config)# do-exec show wccp web-cache assignment <cr>
```

Handler ` RVA 0x10AD36D0 `；selector ` 18 `；EOL ` RVA 0x34C9E3D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bcb311f10c26b5b8](../../evidence/conditions-sets-073.md#c-bcb311f10c26b5b8) · [状态效果 S-ea7df80850c2ae94](../../evidence/state_effects-sets-050.md#s-ea7df80850c2ae94)

### path-039351

```text
(config)# do-exec show wccp web-cache buckets <cr>
```

Handler ` RVA 0x10AD36D0 `；selector ` 18 `；EOL ` RVA 0x34C9DDF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bcb311f10c26b5b8](../../evidence/conditions-sets-073.md#c-bcb311f10c26b5b8) · [状态效果 S-ea7df80850c2ae94](../../evidence/state_effects-sets-050.md#s-ea7df80850c2ae94)

### path-039748

```text
(config)# do-exec show wccp web-cache clients <cr>
```

Handler ` RVA 0x10AD36D0 `；selector ` 2 `；EOL ` RVA 0x34C9F370 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bcb311f10c26b5b8](../../evidence/conditions-sets-073.md#c-bcb311f10c26b5b8) · [状态效果 S-ea7df80850c2ae94](../../evidence/state_effects-sets-050.md#s-ea7df80850c2ae94)

### path-039761

```text
(config)# do-exec show wccp web-cache counters <cr>
```

Handler ` RVA 0x10AD36D0 `；selector ` 4 `；EOL ` RVA 0x34C9F0D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bcb311f10c26b5b8](../../evidence/conditions-sets-073.md#c-bcb311f10c26b5b8) · [状态效果 S-ea7df80850c2ae94](../../evidence/state_effects-sets-050.md#s-ea7df80850c2ae94)

### path-039873

```text
(config)# do-exec show wccp web-cache detail <cr>
```

Handler ` RVA 0x10AD36D0 `；selector ` 1 `；EOL ` RVA 0x34C9F6A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bcb311f10c26b5b8](../../evidence/conditions-sets-073.md#c-bcb311f10c26b5b8) · [状态效果 S-ea7df80850c2ae94](../../evidence/state_effects-sets-050.md#s-ea7df80850c2ae94)

### path-059444

```text
(config)# do-exec show wccp web-cache hash <address> <address> <number:0..65535> <number:0..65535> <cr>
```

Handler ` RVA 0x10AD36D0 `；selector ` 7 `；EOL ` RVA 0x34C9E7E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Destination IPv4 address；` address ` Source IPv4 address；` unsigned_number ` Destination port；` unsigned_number ` Source Port。

[条件 C-cf8d65cc7d285454](../../evidence/conditions-sets-080.md#c-cf8d65cc7d285454) · [参数 P-32263aafb6e585c0](../../evidence/parameters-sets-004.md#p-32263aafb6e585c0) · [状态效果 S-ea7df80850c2ae94](../../evidence/state_effects-sets-050.md#s-ea7df80850c2ae94)

### path-039856

```text
(config)# do-exec show wccp web-cache internal <cr>
```

Handler ` RVA 0x10AD36D0 `；selector ` 5 `；EOL ` RVA 0x34C9F948 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2c1dea74e6184d25](../../evidence/conditions-sets-017.md#c-2c1dea74e6184d25) · [状态效果 S-ea7df80850c2ae94](../../evidence/state_effects-sets-050.md#s-ea7df80850c2ae94)

### path-039401

```text
(config)# do-exec show wccp web-cache mask-acl <cr>
```

Handler ` RVA 0x10AD36D0 `；selector ` 18 `；EOL ` RVA 0x34C9E0A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bcb311f10c26b5b8](../../evidence/conditions-sets-073.md#c-bcb311f10c26b5b8) · [状态效果 S-ea7df80850c2ae94](../../evidence/state_effects-sets-050.md#s-ea7df80850c2ae94)

### path-039910

```text
(config)# do-exec show wccp web-cache merged-acl <cr>
```

Handler ` RVA 0x10AD36D0 `；selector ` 9 `；EOL ` RVA 0x34C9FBF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bcb311f10c26b5b8](../../evidence/conditions-sets-073.md#c-bcb311f10c26b5b8) · [状态效果 S-ea7df80850c2ae94](../../evidence/state_effects-sets-050.md#s-ea7df80850c2ae94)

### path-039574

```text
(config)# do-exec show wccp web-cache service <cr>
```

Handler ` RVA 0x10AD36D0 `；selector ` 8 `；EOL ` RVA 0x34C9EAF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bcb311f10c26b5b8](../../evidence/conditions-sets-073.md#c-bcb311f10c26b5b8) · [状态效果 S-ea7df80850c2ae94](../../evidence/state_effects-sets-050.md#s-ea7df80850c2ae94)

### path-039638

```text
(config)# do-exec show wccp web-cache view <cr>
```

Handler ` RVA 0x10AD36D0 `；selector ` 6 `；EOL ` RVA 0x34C9ED98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bcb311f10c26b5b8](../../evidence/conditions-sets-073.md#c-bcb311f10c26b5b8) · [状态效果 S-ea7df80850c2ae94](../../evidence/state_effects-sets-050.md#s-ea7df80850c2ae94)

### path-030497

```text
(config)# do-exec show wrr-queue bandwidth <cr>
```

Handler ` RVA 0x15F29A20 `；selector ` 0 `；EOL ` RVA 0x35E6D2A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-030530

```text
(config)# do-exec show wrr-queue cos-map <cr>
```

Handler ` RVA 0x15F29700 `；selector ` 0 `；EOL ` RVA 0x35E6D550 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-043371

```text
(config)# do-exec show wsma agent counters <cr>
```

Handler ` RVA 0xF3E9DD0 `；selector ` 0 `；EOL ` RVA 0x3463A978 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-d720098502ba5ba7](../../evidence/state_effects-sets-046.md#s-d720098502ba5ba7)

### path-043394

```text
(config)# do-exec show wsma agent profiles <cr>
```

Handler ` RVA 0xF3E9DD0 `；selector ` 0 `；EOL ` RVA 0x3463AC30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-08d151478e279293](../../evidence/state_effects-sets-002.md#s-08d151478e279293)

### path-043414

```text
(config)# do-exec show wsma agent schema <cr>
```

Handler ` RVA 0xF3E9DD0 `；selector ` 0 `；EOL ` RVA 0x3463AEE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-069b6537d254b6ae](../../evidence/state_effects-sets-002.md#s-069b6537d254b6ae)

### path-033613

```text
(config)# do-exec show wsma history <cr>
```

Handler ` RVA 0xF3EBEA0 `；selector ` 0 `；EOL ` RVA 0x3463B2F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033594

```text
(config)# do-exec show wsma id <cr>
```

Handler ` RVA 0xF403170 `；selector ` 0 `；EOL ` RVA 0x3463A5F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-043408

```text
(config)# do-exec show wsma profile connections <cr>
```

Handler ` RVA 0xF3D6160 `；selector ` 0 `；EOL ` RVA 0x3462DC70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-4735d3625f28ceb9](../../evidence/state_effects-sets-016.md#s-4735d3625f28ceb9)

### path-033623

```text
(config)# do-exec show wsma summary <cr>
```

Handler ` RVA 0xF3EC0F0 `；selector ` 0 `；EOL ` RVA 0x3463B5A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033637

```text
(config)# do-exec show wsma tech-support <cr>
```

Handler ` RVA 0xF3EC200 `；selector ` 0 `；EOL ` RVA 0x3463B848 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027729

```text
(config)# do-exec show x25 <cr>
```

Handler ` RVA 0x105F32F0 `；selector ` 8 `；EOL ` RVA 0x34BC8BF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-854c3491d5994616](../../evidence/conditions-sets-052.md#c-854c3491d5994616) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-060739

```text
(config)# do-exec show x25 <interface> <cr>
```

Handler ` RVA 0x105F32F0 `；selector ` 4 `；EOL ` RVA 0x34BC7880 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-75fb3c13adec357b](../../evidence/conditions-sets-046.md#c-75fb3c13adec357b) · [缺口 G-a2ed1aaa19d162ad](../../evidence/gaps-sets-006.md#g-a2ed1aaa19d162ad) · [参数 P-3161178624dba688](../../evidence/parameters-sets-004.md#p-3161178624dba688) · [状态效果 S-014cb59605b9794b](../../evidence/state_effects-sets-001.md#s-014cb59605b9794b)

### path-033100

```text
(config)# do-exec show x25 context <cr>
```

Handler ` RVA 0x105F32F0 `；selector ` 10 `；EOL ` RVA 0x34BC7228 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8e131be32c9f616d](../../evidence/conditions-sets-055.md#c-8e131be32c9f616d) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061157

```text
(config)# do-exec show x25 context <interface> <cr>
```

Handler ` RVA 0x105F32F0 `；selector ` 10 `；EOL ` RVA 0x34BC7228 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-092eaeeae414db23](../../evidence/conditions-sets-004.md#c-092eaeeae414db23) · [缺口 G-03c58402525bfde1](../../evidence/gaps-sets-001.md#g-03c58402525bfde1) · [参数 P-51aaa7213a6b75c6](../../evidence/parameters-sets-007.md#p-51aaa7213a6b75c6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042315

```text
(config)# do-exec show x25 context xot <cr>
```

Handler ` RVA 0x105F32F0 `；selector ` 7 `；EOL ` RVA 0x34BC6ED8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042454

```text
(config)# do-exec show x25 cug local-cug <cr>
```

Handler ` RVA 0x105F32F0 `；selector ` 11 `；EOL ` RVA 0x34BC8860 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-854c3491d5994616](../../evidence/conditions-sets-052.md#c-854c3491d5994616) · [状态效果 S-3b37089e0edd4569](../../evidence/state_effects-sets-013.md#s-3b37089e0edd4569)

### path-033056

```text
(config)# do-exec show x25 hunt-group <cr>
```

Handler ` RVA 0x10618C60 `；selector ` 12 `；EOL ` RVA 0x34BC6948 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033024

```text
(config)# do-exec show x25 map <cr>
```

Handler ` RVA 0x105F30D0 `；selector ` 1 `；EOL ` RVA 0x34BC6638 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061164

```text
(config)# do-exec show x25 pad <?ttyline_action@555589e54ac0> <cr>
```

Handler ` RVA 0xFE6B820 `；selector ` 2 `；EOL ` RVA 0x34900B00 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-854c3491d5994616](../../evidence/conditions-sets-052.md#c-854c3491d5994616) · [缺口 G-1e832e78984a1c35](../../evidence/gaps-sets-002.md#g-1e832e78984a1c35) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033117

```text
(config)# do-exec show x25 profile <cr>
```

Handler ` RVA 0x105F32F0 `；selector ` 9 `；EOL ` RVA 0x34BC7D38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-854c3491d5994616](../../evidence/conditions-sets-052.md#c-854c3491d5994616) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033169

```text
(config)# do-exec show x25 remote-red <cr>
```

Handler ` RVA 0x1061D4F0 `；selector ` 0 `；EOL ` RVA 0x34BD4A70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-854c3491d5994616](../../evidence/conditions-sets-052.md#c-854c3491d5994616) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033048

```text
(config)# do-exec show x25 route <cr>
```

Handler ` RVA 0x1060FFA0 `；selector ` 3 `；EOL ` RVA 0x34BC6BC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033119

```text
(config)# do-exec show x25 vc <cr>
```

Handler ` RVA 0x105F32F0 `；selector ` 4 `；EOL ` RVA 0x34BC7880 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-854c3491d5994616](../../evidence/conditions-sets-052.md#c-854c3491d5994616) · [状态效果 S-fb9ad934297f836b](../../evidence/state_effects-sets-053.md#s-fb9ad934297f836b)

### path-033142

```text
(config)# do-exec show x25 xot <cr>
```

Handler ` RVA 0x105F32F0 `；selector ` 5 `；EOL ` RVA 0x34BC8450 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-854c3491d5994616](../../evidence/conditions-sets-052.md#c-854c3491d5994616) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042418

```text
(config)# do-exec show x25 xot access-group <cr>
```

Handler ` RVA 0x105F32F0 `；selector ` 6 `；EOL ` RVA 0x34BC8088 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-854c3491d5994616](../../evidence/conditions-sets-052.md#c-854c3491d5994616) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032504

```text
(config)# do-exec show x28 hunt-group <cr>
```

Handler ` RVA 0xFE6C310 `；selector ` 0 `；EOL ` RVA 0x34900498 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-4917594e6be55740](../../evidence/state_effects-sets-016.md#s-4917594e6be55740)

### path-032499

```text
(config)# do-exec show x29 access-lists <cr>
```

Handler ` RVA 0xFE717E0 `；selector ` 0 `；EOL ` RVA 0x349007E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040280

```text
(config)# do-exec show xdr client all <cr>
```

Handler ` RVA 0x10C95110 `；selector ` 0 `；EOL ` RVA 0x34CF50F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-fce3ff0ab74b0936](../../evidence/state_effects-sets-054.md#s-fce3ff0ab74b0936)

### path-032006

```text
(config)# do-exec show xdr linecard <cr>
```

Handler ` RVA 0x10C95780 `；selector ` 0 `；EOL ` RVA 0x34D003F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c9662fe75da19290](../../evidence/conditions-sets-078.md#c-c9662fe75da19290) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061009

```text
(config)# do-exec show xdr linecard <number:dynamic> <cr>
```

Handler ` RVA 0x10C95780 `；selector ` 0 `；EOL ` RVA 0x34D003F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` XDR linecard slot number。

[条件 C-c5f6a656c25f731a](../../evidence/conditions-sets-076.md#c-c5f6a656c25f731a) · [缺口 G-5f3e9891eab701cc](../../evidence/gaps-sets-004.md#g-5f3e9891eab701cc) · [参数 P-2a5889744c896e48](../../evidence/parameters-sets-004.md#p-2a5889744c896e48) · [状态效果 S-b43c514ddb6f4bf9](../../evidence/state_effects-sets-038.md#s-b43c514ddb6f4bf9)

### path-031992

```text
(config)# do-exec show xdr memory <cr>
```

Handler ` RVA 0x10C96910 `；selector ` 0 `；EOL ` RVA 0x34CF56C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031942

```text
(config)# do-exec show xdr multicast-group <cr>
```

Handler ` RVA 0x10C95720 `；selector ` 0 `；EOL ` RVA 0x34CF4D28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061598

```text
(config)# do-exec show xdr statistics client * <cr>
```

Handler ` RVA 0xB319600 `；selector ` 0 `；EOL ` RVA 0x33738C60 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7be397b92c1477ec](../../evidence/conditions-sets-048.md#c-7be397b92c1477ec) · [缺口 G-030c3f8f2ed0f195](../../evidence/gaps-sets-001.md#g-030c3f8f2ed0f195) · [状态效果 S-0ee1c60d66c190d4](../../evidence/state_effects-sets-004.md#s-0ee1c60d66c190d4)

### path-040202

```text
(config)# do-exec show xdr statistics timers <cr>
```

Handler ` RVA 0xB319600 `；selector ` 0 `；EOL ` RVA 0x33738C60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-d2aad9afbc45194b](../../evidence/state_effects-sets-045.md#s-d2aad9afbc45194b)

### path-031955

```text
(config)# do-exec show xdr timers <cr>
```

Handler ` RVA 0x10C96830 `；selector ` 0 `；EOL ` RVA 0x34CF53D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-043590

```text
(config)# do-exec show xmpp profile connections <cr>
```

Handler ` RVA 0x12618B60 `；selector ` 0 `；EOL ` RVA 0x358C6178 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08fafd3d8baf7876](../../evidence/conditions-sets-004.md#c-08fafd3d8baf7876) · [状态效果 S-ec0daa41e73384bc](../../evidence/state_effects-sets-050.md#s-ec0daa41e73384bc)

### path-027744

```text
(config)# do-exec show xos <cr>
```

Handler ` RVA 0xDC718E0 `；selector ` 12 `；EOL ` RVA 0x340254E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033317

```text
(config)# do-exec show xos errors <cr>
```

Handler ` RVA 0xDC718E0 `；selector ` 2 `；EOL ` RVA 0x34023508 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042856

```text
(config)# do-exec show xos info xdm <cr>
```

Handler ` RVA 0xDCA7840 `；selector ` 0 `；EOL ` RVA 0x34026700 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033464

```text
(config)# do-exec show xos traces <cr>
```

Handler ` RVA 0xDC718E0 `；selector ` 1 `；EOL ` RVA 0x34025028 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042939

```text
(config)# do-exec show xos traces address <cr>
```

Handler ` RVA 0xDC718E0 `；selector ` 8 `；EOL ` RVA 0x34024AB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042965

```text
(config)# do-exec show xos traces interface <cr>
```

Handler ` RVA 0xDC718E0 `；selector ` 7 `；EOL ` RVA 0x34024D58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042777

```text
(config)# do-exec show xos traces ipc <cr>
```

Handler ` RVA 0xDC718E0 `；selector ` 4 `；EOL ` RVA 0x34023818 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042803

```text
(config)# do-exec show xos traces mgd <cr>
```

Handler ` RVA 0xDC718E0 `；selector ` 5 `；EOL ` RVA 0x34023AC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042881

```text
(config)# do-exec show xos traces packet <cr>
```

Handler ` RVA 0xDC718E0 `；selector ` 11 `；EOL ` RVA 0x340242B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042901

```text
(config)# do-exec show xos traces policy <cr>
```

Handler ` RVA 0xDC718E0 `；selector ` 10 `；EOL ` RVA 0x34024560 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042919

```text
(config)# do-exec show xos traces routing <cr>
```

Handler ` RVA 0xDC718E0 `；selector ` 9 `；EOL ` RVA 0x34024808 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042830

```text
(config)# do-exec show xos traces time <cr>
```

Handler ` RVA 0xDC718E0 `；selector ` 6 `；EOL ` RVA 0x34023D68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042857

```text
(config)# do-exec show xos traces utils <cr>
```

Handler ` RVA 0xDC718E0 `；selector ` 3 `；EOL ` RVA 0x34024010 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042991

```text
(config)# do-exec show xos traces xdm <cr>
```

Handler ` RVA 0xDC718E0 `；selector ` 13 `；EOL ` RVA 0x34025000 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061788

```text
(config)# do-exec show xsd-format <url:dynamic> cli <string> <cr>
```

Handler ` RVA 0xF414F30 `；selector ` 0 `；EOL ` RVA 0x34641B90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Enter the fully expanded command to display。

[条件 C-7a7508583caef901](../../evidence/conditions-sets-047.md#c-7a7508583caef901) · [缺口 G-531a6089b273fbf0](../../evidence/gaps-sets-003.md#g-531a6089b273fbf0) · [参数 P-6d7658018c70e8b6](../../evidence/parameters-sets-009.md#p-6d7658018c70e8b6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-043285

```text
(config)# do-exec show xsd-format cli <string> <cr>
```

Handler ` RVA 0xF414F30 `；selector ` 0 `；EOL ` RVA 0x34641B90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Enter the fully expanded command to display。

[条件 C-bb535702d0316d4b](../../evidence/conditions-sets-072.md#c-bb535702d0316d4b) · [参数 P-5385741c6a902cd0](../../evidence/parameters-sets-007.md#p-5385741c6a902cd0) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-025837

```text
(config)# do-exec slip <cr>
```

Handler ` RVA 0xFF404B0 `；selector ` 0 `；EOL ` RVA 0x34933EE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-060409

```text
(config)# do-exec slip <string> <cr>
```

Handler ` RVA 0xFF404B0 `；selector ` 0 `；EOL ` RVA 0x34933EE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Desired IP address or hostname。

[条件 C-8a99fee1900fc7ab](../../evidence/conditions-sets-054.md#c-8a99fee1900fc7ab) · [缺口 G-6e87cf4b61f2564e](../../evidence/gaps-sets-004.md#g-6e87cf4b61f2564e) · [参数 P-ceb486da596ed987](../../evidence/parameters-sets-016.md#p-ceb486da596ed987) · [状态效果 S-d133bd06764c270e](../../evidence/state_effects-sets-044.md#s-d133bd06764c270e)

### path-057934

```text
(config)# do-exec snmp get-next v1 <string> <string> oid <string> <cr>
```

Handler ` RVA 0x10527C60 `；selector ` 0 `；EOL ` RVA 0x34B535A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` IP/IPv6 address or hostname of SNMP destination；` string ` SNMP community string；` string ` Object identifier value。

[条件 C-ea8b03e003992892](../../evidence/conditions-sets-091.md#c-ea8b03e003992892) · [参数 P-a202ce2166e2659e](../../evidence/parameters-sets-012.md#p-a202ce2166e2659e) · [状态效果 S-a04543ffe74ad86e](../../evidence/state_effects-sets-034.md#s-a04543ffe74ad86e)

### path-062619

```text
(config)# do-exec snmp get-next v1 <string> idb <interface> <string> oid <string> <cr>
```

Handler ` RVA 0x10527C60 `；selector ` 0 `；EOL ` RVA 0x34B535A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` IP/IPv6 address or hostname of SNMP destination；` string ` SNMP community string；` string ` Object identifier value。

[条件 C-9970501220f5dbe5](../../evidence/conditions-sets-059.md#c-9970501220f5dbe5) · [缺口 G-1b4b478f0fabc516](../../evidence/gaps-sets-001.md#g-1b4b478f0fabc516) · [参数 P-c1f9fc216da78703](../../evidence/parameters-sets-015.md#p-c1f9fc216da78703) · [状态效果 S-a04543ffe74ad86e](../../evidence/state_effects-sets-034.md#s-a04543ffe74ad86e)

### path-062879

```text
(config)# do-exec spec-file install <url:dynamic> add-entry <url:dynamic> <string> <cr>
```

Handler ` RVA 0xF411650 `；selector ` 0 `；EOL ` RVA 0x34641480 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` fully expanded command。

[条件 C-38948a46ca448c67](../../evidence/conditions-sets-022.md#c-38948a46ca448c67) · [缺口 G-3d9bea75510ef237](../../evidence/gaps-sets-003.md#g-3d9bea75510ef237) · [参数 P-7e3e9656bcfd601c](../../evidence/parameters-sets-010.md#p-7e3e9656bcfd601c) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-060915

```text
(config)# do-exec spec-file install <url:dynamic> built-in <cr>
```

Handler ` RVA 0xF411C40 `；selector ` 0 `；EOL ` RVA 0x34640E18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2f47022550495305](../../evidence/conditions-sets-018.md#c-2f47022550495305) · [缺口 G-b4056f875657e407](../../evidence/gaps-sets-006.md#g-b4056f875657e407) · [参数 P-bb2fb97a40631c3e](../../evidence/parameters-sets-014.md#p-bb2fb97a40631c3e) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062833

```text
(config)# do-exec spec-file install <url:dynamic> file <url:dynamic> <cr>
```

Handler ` RVA 0xF4116D0 `；selector ` 0 `；EOL ` RVA 0x34641128 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-554cd8ff74eaba15](../../evidence/conditions-sets-033.md#c-554cd8ff74eaba15) · [缺口 G-ed1818414cab63d0](../../evidence/gaps-sets-008.md#g-ed1818414cab63d0) · [参数 P-9fb813d1992d070b](../../evidence/parameters-sets-012.md#p-9fb813d1992d070b) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061422

```text
(config)# do-exec spec-file install <url:dynamic> remove-entry <string> <cr>
```

Handler ` RVA 0xF4107C0 `；selector ` 0 `；EOL ` RVA 0x34641740 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` fully expanded command。

[条件 C-2f47022550495305](../../evidence/conditions-sets-018.md#c-2f47022550495305) · [缺口 G-b4056f875657e407](../../evidence/gaps-sets-006.md#g-b4056f875657e407) · [参数 P-9fada1185b7ecbfb](../../evidence/parameters-sets-012.md#p-9fada1185b7ecbfb) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-060913

```text
(config)# do-exec spec-file install <url:dynamic> restore <cr>
```

Handler ` RVA 0xF412240 `；selector ` 0 `；EOL ` RVA 0x34640B70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2f47022550495305](../../evidence/conditions-sets-018.md#c-2f47022550495305) · [缺口 G-b4056f875657e407](../../evidence/gaps-sets-006.md#g-b4056f875657e407) · [参数 P-bb2fb97a40631c3e](../../evidence/parameters-sets-014.md#p-bb2fb97a40631c3e) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-060429

```text
(config)# do-exec squeeze <url:dynamic> <cr>
```

Handler ` RVA 0xD65ADE0 `；selector ` 0 `；EOL ` RVA 0x33EB6140 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` url_dynamic ` Filesystem to be squeezed。

[条件 C-2a75ca95639d45d3](../../evidence/conditions-sets-017.md#c-2a75ca95639d45d3) · [缺口 G-c6333e3c8c7a4c7a](../../evidence/gaps-sets-007.md#g-c6333e3c8c7a4c7a) · [参数 P-4e7fe20d6770dc7e](../../evidence/parameters-sets-006.md#p-4e7fe20d6770dc7e) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-060882

```text
(config)# do-exec ssh -c chacha20-poly1305@openssh.com <string> <cr>
```

Handler ` RVA 0x1239B530 `；selector ` 0 `；EOL ` RVA 0x35829648 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` IP address or hostname of a remote system。

[条件 C-07d92f54b5805f6a](../../evidence/conditions-sets-003.md#c-07d92f54b5805f6a) · [缺口 G-898db49408fc2054](../../evidence/gaps-sets-005.md#g-898db49408fc2054) · [参数 P-4f9aee87c0358682](../../evidence/parameters-sets-007.md#p-4f9aee87c0358682) · [状态效果 S-2f4e10453f53dde5](../../evidence/state_effects-sets-010.md#s-2f4e10453f53dde5)

### path-027219

```text
(config)# do-exec ssh <string> <cr>
```

Handler ` RVA 0x1239B530 `；selector ` 0 `；EOL ` RVA 0x35829648 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` IP address or hostname of a remote system。

[条件 C-9b886337a61fd34b](../../evidence/conditions-sets-060.md#c-9b886337a61fd34b) · [参数 P-4f9aee87c0358682](../../evidence/parameters-sets-007.md#p-4f9aee87c0358682) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-060633

```text
(config)# do-exec start-chat <string> <?ttyline_action@555589b55640> <cr>
```

Handler ` RVA 0xF2F0F90 `；selector ` 0 `；EOL ` RVA 0x34601700 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Chat Script name or regular expression。

[条件 C-ae3730a6a52c08e4](../../evidence/conditions-sets-067.md#c-ae3730a6a52c08e4) · [缺口 G-8833ce7b452d6ee1](../../evidence/gaps-sets-005.md#g-8833ce7b452d6ee1) · [参数 P-836dba1d4f2dfa89](../../evidence/parameters-sets-010.md#p-836dba1d4f2dfa89) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-025661

```text
(config)# do-exec systat <cr>
```

Handler ` RVA 0xDFE03B0 `；selector ` 0 `；EOL ` RVA 0x3415D448 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9626c53f680f99e8](../../evidence/conditions-sets-058.md#c-9626c53f680f99e8) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-026037

```text
(config)# do-exec system kexecreload <cr>
```

Handler ` RVA 0xEA264C0 `；selector ` 0 `；EOL ` RVA 0x34391FD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bc366d020d79028c](../../evidence/conditions-sets-073.md#c-bc366d020d79028c) · [状态效果 S-c371e247b6b5659f](../../evidence/state_effects-sets-041.md#s-c371e247b6b5659f)

### path-025880

```text
(config)# do-exec tclquit <cr>
```

Handler ` RVA 0x11148A70 `；selector ` 0 `；EOL ` RVA 0x3540BD00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-025883

```text
(config)# do-exec tclsh <cr>
```

Handler ` RVA 0x11148210 `；selector ` 0 `；EOL ` RVA 0x3540BA48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-025794

```text
(config)# do-exec telnet <cr>
```

Handler ` RVA 0xDE84C20 `；selector ` 1 `；EOL ` RVA 0x33CF53F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2e9ac9867a1896cc](../../evidence/conditions-sets-018.md#c-2e9ac9867a1896cc) · [状态效果 S-34c98a0ed57f0e64](../../evidence/state_effects-sets-012.md#s-34c98a0ed57f0e64)

### path-025800

```text
(config)# do-exec telnet <cr>
```

Handler ` RVA 0xDE84C20 `；selector ` 0 `；EOL ` RVA 0x33CF56B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bf79bfe0e43c8657](../../evidence/conditions-sets-074.md#c-bf79bfe0e43c8657) · [状态效果 S-34c98a0ed57f0e64](../../evidence/state_effects-sets-012.md#s-34c98a0ed57f0e64)

### path-025801

```text
(config)# do-exec telnet <cr>
```

Handler ` RVA 0xCE631F0 `；selector ` 0 `；EOL ` RVA 0x33CF56E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2835b6697c1b4758](../../evidence/conditions-sets-016.md#c-2835b6697c1b4758) · [状态效果 S-34c98a0ed57f0e64](../../evidence/state_effects-sets-012.md#s-34c98a0ed57f0e64)

### path-028691

```text
(config)# do-exec terminal absolute-timeout <number:0..10000> <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 140 `；EOL ` RVA 0x33C641B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Absolute timeout interval in minutes。

[条件 C-134a3ceb5bce1b4a](../../evidence/conditions-sets-008.md#c-134a3ceb5bce1b4a) · [参数 P-267260ddd09478b7](../../evidence/parameters-sets-003.md#p-267260ddd09478b7) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-034194

```text
(config)# do-exec terminal access-class <number:1..199> out <cr>
```

Handler ` RVA 0xE059390 `；selector ` 10 `；EOL ` RVA 0x3412B368 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` IP access list。

[条件 C-c3f4600a80eec1e4](../../evidence/conditions-sets-076.md#c-c3f4600a80eec1e4) · [参数 P-b42407ad4477584d](../../evidence/parameters-sets-014.md#p-b42407ad4477584d) · [状态效果 S-dc93a2471c5c4cd0](../../evidence/state_effects-sets-047.md#s-dc93a2471c5c4cd0)

### path-034805

```text
(config)# do-exec terminal accounting resource default <cr>
```

Handler ` RVA 0xE056B50 `；selector ` 28 `；EOL ` RVA 0x34181488 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8bd2cb58a4f9a2dc](../../evidence/conditions-sets-054.md#c-8bd2cb58a4f9a2dc) · [状态效果 S-630453c8a67d99d8](../../evidence/state_effects-sets-021.md#s-630453c8a67d99d8)

### path-060542

```text
(config)# do-exec terminal activation-character <?char_number_action@5555891b7498> <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 110 `；EOL ` RVA 0x33C634C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8e1a80e579c1a566](../../evidence/conditions-sets-055.md#c-8e1a80e579c1a566) · [缺口 G-f2c45d2da9feca49](../../evidence/gaps-sets-008.md#g-f2c45d2da9feca49) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-034764

```text
(config)# do-exec terminal authorization reverse-access default <cr>
```

Handler ` RVA 0xE056B50 `；selector ` 27 `；EOL ` RVA 0x34180E68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-14cb3a8c4d7cfbde](../../evidence/conditions-sets-008.md#c-14cb3a8c4d7cfbde) · [状态效果 S-2903f37661f1d4e7](../../evidence/state_effects-sets-009.md#s-2903f37661f1d4e7)

### path-026643

```text
(config)# do-exec terminal autobaud <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 106 `；EOL ` RVA 0x33C654B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bd3f2cb1c891bd0a](../../evidence/conditions-sets-073.md#c-bd3f2cb1c891bd0a) · [状态效果 S-e7ce11cd020ca5ed](../../evidence/state_effects-sets-049.md#s-e7ce11cd020ca5ed)

### path-028983

```text
(config)# do-exec terminal autocommand <string> <cr>
```

Handler ` RVA 0xE059390 `；selector ` 130 `；EOL ` RVA 0x34180340 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Appropriate EXEC command。

[条件 C-ec5594d2412338de](../../evidence/conditions-sets-091.md#c-ec5594d2412338de) · [参数 P-1da426af8757be3b](../../evidence/parameters-sets-003.md#p-1da426af8757be3b) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-060812

```text
(config)# do-exec terminal autocommand-options abort-character <?char_number_action@5555896d4808> <cr>
```

Handler ` RVA 0xE059390 `；selector ` 144 `；EOL ` RVA 0x34180720 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-659ed4e5c29592db](../../evidence/conditions-sets-039.md#c-659ed4e5c29592db) · [缺口 G-563171475adf2a58](../../evidence/gaps-sets-003.md#g-563171475adf2a58) · [状态效果 S-51278dcfaaf368d4](../../evidence/state_effects-sets-018.md#s-51278dcfaaf368d4)

### path-029079

```text
(config)# do-exec terminal autocommand-options nohangup <cr>
```

Handler ` RVA 0xE059390 `；selector ` 144 `；EOL ` RVA 0x34180720 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-641bb419e449797c](../../evidence/conditions-sets-039.md#c-641bb419e449797c) · [状态效果 S-e63785af01dd8e12](../../evidence/state_effects-sets-049.md#s-e63785af01dd8e12)

### path-026672

```text
(config)# do-exec terminal autohangup <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 111 `；EOL ` RVA 0x33C61BC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cd4d3448e3cd0877](../../evidence/conditions-sets-079.md#c-cd4d3448e3cd0877) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-028647

```text
(config)# do-exec terminal autohangup session-timeout <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 165 `；EOL ` RVA 0x33C61B98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cd4d3448e3cd0877](../../evidence/conditions-sets-079.md#c-cd4d3448e3cd0877) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-028724

```text
(config)# do-exec terminal autohost <string> <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 131 `；EOL ` RVA 0x33C64500 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Host to automatically connect to。

[条件 C-0f05a557ed2ab519](../../evidence/conditions-sets-006.md#c-0f05a557ed2ab519) · [参数 P-0c16133141743476](../../evidence/parameters-sets-001.md#p-0c16133141743476) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-026736

```text
(config)# do-exec terminal autoselect <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 143 `；EOL ` RVA 0x33C611E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cd4d3448e3cd0877](../../evidence/conditions-sets-079.md#c-cd4d3448e3cd0877) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-028571

```text
(config)# do-exec terminal autoselect arap <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 142 `；EOL ` RVA 0x33C60DC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cd4d3448e3cd0877](../../evidence/conditions-sets-079.md#c-cd4d3448e3cd0877) · [状态效果 S-d7dd937cfcf8448f](../../evidence/state_effects-sets-046.md#s-d7dd937cfcf8448f)

### path-025669

```text
(config)# do-exec terminal buffer-length <number:16..1536> <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 146 `；EOL ` RVA 0x33C62AF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` buffer length in bytes。

[条件 C-6c49f313ae3fa1ad](../../evidence/conditions-sets-042.md#c-6c49f313ae3fa1ad) · [参数 P-c1be88f0a8e29c00](../../evidence/parameters-sets-015.md#p-c1be88f0a8e29c00) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-025617

```text
(config)# do-exec terminal data-character-bits <number:7..8> <cr>
```

Handler ` RVA 0xE059390 `；selector ` 132 `；EOL ` RVA 0x34127948 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Bits per character。

[条件 C-93460ef5e1ee9b1f](../../evidence/conditions-sets-057.md#c-93460ef5e1ee9b1f) · [参数 P-8925e9101d554722](../../evidence/parameters-sets-011.md#p-8925e9101d554722) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-028822

```text
(config)# do-exec terminal databits 5 <cr>
```

Handler ` RVA 0xE059390 `；selector ` 102 `；EOL ` RVA 0x34181EA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-52e0c247c92e84ff](../../evidence/conditions-sets-032.md#c-52e0c247c92e84ff) · [状态效果 S-f2079c00354678d9](../../evidence/state_effects-sets-051.md#s-f2079c00354678d9)

### path-028705

```text
(config)# do-exec terminal default absolute-timeout <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 140 `；EOL ` RVA 0x33C641B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d70b1ef127791f01](../../evidence/conditions-sets-083.md#c-d70b1ef127791f01) · [状态效果 S-540c7785c8f812e2](../../evidence/state_effects-sets-018.md#s-540c7785c8f812e2)

### path-034284

```text
(config)# do-exec terminal default access-class out <cr>
```

Handler ` RVA 0xE059390 `；selector ` 10 `；EOL ` RVA 0x3412B368 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c51915e29650ef6a](../../evidence/conditions-sets-076.md#c-c51915e29650ef6a) · [状态效果 S-a175180bb8f0f558](../../evidence/state_effects-sets-034.md#s-a175180bb8f0f558)

### path-034824

```text
(config)# do-exec terminal default accounting resource <cr>
```

Handler ` RVA 0xE056B50 `；selector ` 28 `；EOL ` RVA 0x34181488 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-336a1df3fbc3717e](../../evidence/conditions-sets-020.md#c-336a1df3fbc3717e) · [状态效果 S-3c3f23e7ff7e5414](../../evidence/state_effects-sets-013.md#s-3c3f23e7ff7e5414)

### path-028539

```text
(config)# do-exec terminal default activation-character <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 110 `；EOL ` RVA 0x33C634C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-522821d40b4c626d](../../evidence/conditions-sets-032.md#c-522821d40b4c626d) · [状态效果 S-540c7785c8f812e2](../../evidence/state_effects-sets-018.md#s-540c7785c8f812e2)

### path-034781

```text
(config)# do-exec terminal default authorization reverse-access <cr>
```

Handler ` RVA 0xE056B50 `；selector ` 27 `；EOL ` RVA 0x34180E68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-88119331598bbfeb](../../evidence/conditions-sets-053.md#c-88119331598bbfeb) · [状态效果 S-f70cb1d5d3ba1cbf](../../evidence/state_effects-sets-052.md#s-f70cb1d5d3ba1cbf)

### path-028641

```text
(config)# do-exec terminal default autobaud <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 106 `；EOL ` RVA 0x33C654B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-bd3f2cb1c891bd0a](../../evidence/conditions-sets-073.md#c-bd3f2cb1c891bd0a) · [状态效果 S-42e9b17795a8e947](../../evidence/state_effects-sets-015.md#s-42e9b17795a8e947)

### path-028902

```text
(config)# do-exec terminal default autocommand <cr>
```

Handler ` RVA 0xE059390 `；selector ` 130 `；EOL ` RVA 0x34180340 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-41a829ba591f2526](../../evidence/conditions-sets-026.md#c-41a829ba591f2526) · [状态效果 S-540c7785c8f812e2](../../evidence/state_effects-sets-018.md#s-540c7785c8f812e2)

### path-028951

```text
(config)# do-exec terminal default autocommand-options <cr>
```

Handler ` RVA 0xE059390 `；selector ` 144 `；EOL ` RVA 0x34180720 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2397afbfdfe08a4e](../../evidence/conditions-sets-014.md#c-2397afbfdfe08a4e) · [状态效果 S-540c7785c8f812e2](../../evidence/state_effects-sets-018.md#s-540c7785c8f812e2)

### path-028704

```text
(config)# do-exec terminal default autohangup <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 111 `；EOL ` RVA 0x33C61BC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-cd4d3448e3cd0877](../../evidence/conditions-sets-079.md#c-cd4d3448e3cd0877) · [状态效果 S-540c7785c8f812e2](../../evidence/state_effects-sets-018.md#s-540c7785c8f812e2)

### path-034751

```text
(config)# do-exec terminal default autohangup session-timeout <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 165 `；EOL ` RVA 0x33C61B98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-cd4d3448e3cd0877](../../evidence/conditions-sets-079.md#c-cd4d3448e3cd0877) · [状态效果 S-540c7785c8f812e2](../../evidence/state_effects-sets-018.md#s-540c7785c8f812e2)

### path-028749

```text
(config)# do-exec terminal default autohost <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 131 `；EOL ` RVA 0x33C64500 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a205d270ab42a157](../../evidence/conditions-sets-063.md#c-a205d270ab42a157) · [状态效果 S-540c7785c8f812e2](../../evidence/state_effects-sets-018.md#s-540c7785c8f812e2)

### path-028867

```text
(config)# do-exec terminal default autoselect <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 143 `；EOL ` RVA 0x33C611E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-cd4d3448e3cd0877](../../evidence/conditions-sets-079.md#c-cd4d3448e3cd0877) · [状态效果 S-540c7785c8f812e2](../../evidence/state_effects-sets-018.md#s-540c7785c8f812e2)

### path-034670

```text
(config)# do-exec terminal default autoselect arap <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 142 `；EOL ` RVA 0x33C60DC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-cd4d3448e3cd0877](../../evidence/conditions-sets-079.md#c-cd4d3448e3cd0877) · [状态效果 S-e3f04664cf645541](../../evidence/state_effects-sets-048.md#s-e3f04664cf645541)

### path-026499

```text
(config)# do-exec terminal default buffer-length <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 146 `；EOL ` RVA 0x33C62AF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e703bf4d066e21b0](../../evidence/conditions-sets-089.md#c-e703bf4d066e21b0) · [状态效果 S-540c7785c8f812e2](../../evidence/state_effects-sets-018.md#s-540c7785c8f812e2)

### path-026303

```text
(config)# do-exec terminal default data-character-bits <cr>
```

Handler ` RVA 0xE059390 `；selector ` 132 `；EOL ` RVA 0x34127948 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-32d897df1c228de4](../../evidence/conditions-sets-020.md#c-32d897df1c228de4) · [状态效果 S-540c7785c8f812e2](../../evidence/state_effects-sets-018.md#s-540c7785c8f812e2)

### path-028907

```text
(config)# do-exec terminal default databits <cr>
```

Handler ` RVA 0xE059390 `；selector ` 102 `；EOL ` RVA 0x34181EA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-08f5d4e86cfd5611](../../evidence/conditions-sets-004.md#c-08f5d4e86cfd5611) · [状态效果 S-b744a32944cd354b](../../evidence/state_effects-sets-039.md#s-b744a32944cd354b)

### path-028565

```text
(config)# do-exec terminal default disconnect-character <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 113 `；EOL ` RVA 0x33C63810 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-387f0bf228e2113e](../../evidence/conditions-sets-022.md#c-387f0bf228e2113e) · [状态效果 S-540c7785c8f812e2](../../evidence/state_effects-sets-018.md#s-540c7785c8f812e2)

### path-028856

```text
(config)# do-exec terminal default dispatch-character <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 121 `；EOL ` RVA 0x33C624E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-591034220e940a26](../../evidence/conditions-sets-035.md#c-591034220e940a26) · [状态效果 S-540c7785c8f812e2](../../evidence/state_effects-sets-018.md#s-540c7785c8f812e2)

### path-028540

```text
(config)# do-exec terminal default dispatch-machine <cr>
```

Handler ` RVA 0xDE9D520 `；selector ` 0 `；EOL ` RVA 0x33C63168 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a28f11e8b6856f01](../../evidence/conditions-sets-063.md#c-a28f11e8b6856f01) · [状态效果 S-540c7785c8f812e2](../../evidence/state_effects-sets-018.md#s-540c7785c8f812e2)

### path-026679

```text
(config)# do-exec terminal default dispatch-timeout <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 114 `；EOL ` RVA 0x33C61B58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-29ddd3b200f8fe97](../../evidence/conditions-sets-016.md#c-29ddd3b200f8fe97) · [状态效果 S-540c7785c8f812e2](../../evidence/state_effects-sets-018.md#s-540c7785c8f812e2)

### path-028212

```text
(config)# do-exec terminal default domain-lookup <cr>
```

Handler ` RVA 0xE059390 `；selector ` 2 `；EOL ` RVA 0x34128800 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-cd4d3448e3cd0877](../../evidence/conditions-sets-079.md#c-cd4d3448e3cd0877) · [状态效果 S-540c7785c8f812e2](../../evidence/state_effects-sets-018.md#s-540c7785c8f812e2)

### path-028163

```text
(config)# do-exec terminal default download <cr>
```

Handler ` RVA 0xE05E330 `；selector ` 138 `；EOL ` RVA 0x3417D940 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4692e7a2b28250a0](../../evidence/conditions-sets-028.md#c-4692e7a2b28250a0) · [状态效果 S-540c7785c8f812e2](../../evidence/state_effects-sets-018.md#s-540c7785c8f812e2)

### path-028360

```text
(config)# do-exec terminal default editing <cr>
```

Handler ` RVA 0xE059390 `；selector ` 137 `；EOL ` RVA 0x3412A1F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-cd4d3448e3cd0877](../../evidence/conditions-sets-079.md#c-cd4d3448e3cd0877) · [状态效果 S-540c7785c8f812e2](../../evidence/state_effects-sets-018.md#s-540c7785c8f812e2)

### path-028711

```text
(config)# do-exec terminal default escape-character <cr>
```

Handler ` RVA 0xDFE2380 `；selector ` 5 `；EOL ` RVA 0x341607F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6ef2d7731beb77a7](../../evidence/conditions-sets-043.md#c-6ef2d7731beb77a7) · [状态效果 S-540c7785c8f812e2](../../evidence/state_effects-sets-018.md#s-540c7785c8f812e2)

### path-028277

```text
(config)# do-exec terminal default exec <cr>
```

Handler ` RVA 0xE059390 `；selector ` 125 `；EOL ` RVA 0x34129088 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-11c01e0c696e74b7](../../evidence/conditions-sets-007.md#c-11c01e0c696e74b7) · [状态效果 S-540c7785c8f812e2](../../evidence/state_effects-sets-018.md#s-540c7785c8f812e2)

### path-044057

```text
(config)# do-exec terminal default exec prompt expand <cr>
```

Handler ` RVA 0xE059390 `；selector ` 40 `；EOL ` RVA 0x34128B48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-cd4d3448e3cd0877](../../evidence/conditions-sets-079.md#c-cd4d3448e3cd0877) · [状态效果 S-540c7785c8f812e2](../../evidence/state_effects-sets-018.md#s-540c7785c8f812e2)

### path-044096

```text
(config)# do-exec terminal default exec prompt timestamp <cr>
```

Handler ` RVA 0xE059390 `；selector ` 38 `；EOL ` RVA 0x34128DF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-cd4d3448e3cd0877](../../evidence/conditions-sets-079.md#c-cd4d3448e3cd0877) · [状态效果 S-540c7785c8f812e2](../../evidence/state_effects-sets-018.md#s-540c7785c8f812e2)

### path-028164

```text
(config)# do-exec terminal default exec-banner <cr>
```

Handler ` RVA 0xE059390 `；selector ` 11 `；EOL ` RVA 0x3412B998 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c3f4600a80eec1e4](../../evidence/conditions-sets-076.md#c-c3f4600a80eec1e4) · [状态效果 S-540c7785c8f812e2](../../evidence/state_effects-sets-018.md#s-540c7785c8f812e2)

### path-028192

```text
(config)# do-exec terminal default exec-character-bits <cr>
```

Handler ` RVA 0xE059390 `；selector ` 134 `；EOL ` RVA 0x34128270 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-bb4f76119c8d8581](../../evidence/conditions-sets-072.md#c-bb4f76119c8d8581) · [状态效果 S-540c7785c8f812e2](../../evidence/state_effects-sets-018.md#s-540c7785c8f812e2)

### path-028241

```text
(config)# do-exec terminal default exec-timeout <cr>
```

Handler ` RVA 0xE059390 `；selector ` 13 `；EOL ` RVA 0x3412BD18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ac9bb926ccf1e4c4](../../evidence/conditions-sets-067.md#c-ac9bb926ccf1e4c4) · [状态效果 S-540c7785c8f812e2](../../evidence/state_effects-sets-018.md#s-540c7785c8f812e2)
