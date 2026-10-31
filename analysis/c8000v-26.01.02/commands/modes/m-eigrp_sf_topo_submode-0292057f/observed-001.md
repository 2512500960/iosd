# eigrp_sf_topo_submode · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-008857

```text
(config-router-sf-topology)# default eigrp event-log-size <cr>
```

Handler ` RVA 0xF596700 `；selector ` 35 `；EOL ` RVA 0x346ABC28 `。

模式根 ` RVA 0x346A8F60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-61ffa406706fdaaa](../../evidence/conditions-sets-038.md#c-61ffa406706fdaaa) · [状态效果 S-ea5465eca18a7b7f](../../evidence/state_effects-sets-050.md#s-ea5465eca18a7b7f)

### observed_connections-008853

```text
(config-router-sf-topology)# default eigrp event-logging <cr>
```

Handler ` RVA 0xF596700 `；selector ` 36 `；EOL ` RVA 0x346AB910 `。

模式根 ` RVA 0x346A8F60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-fbe022245a9bfc94](../../evidence/conditions-sets-097.md#c-fbe022245a9bfc94) · [状态效果 S-ea5465eca18a7b7f](../../evidence/state_effects-sets-050.md#s-ea5465eca18a7b7f)

### observed_connections-008854

```text
(config-router-sf-topology)# default eigrp log-event-type <cr>
```

Handler ` RVA 0xF596700 `；selector ` 34 `；EOL ` RVA 0x346AB528 `。

模式根 ` RVA 0x346A8F60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-09227093872ece7b](../../evidence/conditions-sets-004.md#c-09227093872ece7b) · [状态效果 S-ea5465eca18a7b7f](../../evidence/state_effects-sets-050.md#s-ea5465eca18a7b7f)

### observed_connections-008842

```text
(config-router-sf-topology)# default external-client <string> <cr>
```

Handler ` RVA 0xF594330 `；selector ` 0 `；EOL ` RVA 0x346A9D00 `。

模式根 ` RVA 0x346A8F60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Client Label (max 64 characters)。

[条件 C-6de4c90ae191c524](../../evidence/conditions-sets-042.md#c-6de4c90ae191c524) · [参数 P-83fa09c2d6099b4b](../../evidence/parameters-sets-010.md#p-83fa09c2d6099b4b) · [状态效果 S-ea5465eca18a7b7f](../../evidence/state_effects-sets-050.md#s-ea5465eca18a7b7f)

### observed_connections-008845

```text
(config-router-sf-topology)# default metric maximum-hops <cr>
```

Handler ` RVA 0xF57D6C0 `；selector ` 31 `；EOL ` RVA 0x346AA088 `。

模式根 ` RVA 0x346A8F60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f0d3b524fb3ba4f1](../../evidence/conditions-sets-093.md#c-f0d3b524fb3ba4f1) · [状态效果 S-ea5465eca18a7b7f](../../evidence/state_effects-sets-050.md#s-ea5465eca18a7b7f)

### observed_connections-008860

```text
(config-router-sf-topology)# default redistribute eigrp <number:1..65535> <cr>
```

Handler ` RVA 0xF593E60 `；selector ` 32 `；EOL ` RVA 0x346AACE8 `。

模式根 ` RVA 0x346A8F60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Autonomous-System number。

[条件 C-142dec5a99cd43e6](../../evidence/conditions-sets-008.md#c-142dec5a99cd43e6) · [参数 P-3d447b0d15c9b3cf](../../evidence/parameters-sets-005.md#p-3d447b0d15c9b3cf) · [状态效果 S-ea5465eca18a7b7f](../../evidence/state_effects-sets-050.md#s-ea5465eca18a7b7f)

### observed_connections-008847

```text
(config-router-sf-topology)# default redistribute maximum-service <cr>
```

Handler ` RVA 0xF598EF0 `；selector ` 33 `；EOL ` RVA 0x346AA450 `。

模式根 ` RVA 0x346A8F60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4c6f2f8cd9d8040b](../../evidence/conditions-sets-030.md#c-4c6f2f8cd9d8040b) · [状态效果 S-ea5465eca18a7b7f](../../evidence/state_effects-sets-050.md#s-ea5465eca18a7b7f)

### observed_connections-008851

```text
(config-router-sf-topology)# default timers active-time <cr>
```

Handler ` RVA 0xF597780 `；selector ` 28 `；EOL ` RVA 0x346AB138 `。

模式根 ` RVA 0x346A8F60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-fd5b346fd689c01c](../../evidence/conditions-sets-098.md#c-fd5b346fd689c01c) · [状态效果 S-ea5465eca18a7b7f](../../evidence/state_effects-sets-050.md#s-ea5465eca18a7b7f)

### observed_connections-008861

```text
(config-router-sf-topology)# eigrp event-log-size <number:dynamic> <cr>
```

Handler ` RVA 0xF596700 `；selector ` 35 `；EOL ` RVA 0x346ABC28 `。

模式根 ` RVA 0x346A8F60 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Max event log entries。

[条件 C-0f99cc150c070617](../../evidence/conditions-sets-006.md#c-0f99cc150c070617) · [缺口 G-01cbe7ba8ca34cc8](../../evidence/gaps-sets-001.md#g-01cbe7ba8ca34cc8) · [参数 P-dc360257de90eb31](../../evidence/parameters-sets-017.md#p-dc360257de90eb31)

### observed_connections-008839

```text
(config-router-sf-topology)# eigrp event-logging <cr>
```

Handler ` RVA 0xF596700 `；selector ` 36 `；EOL ` RVA 0x346AB910 `。

模式根 ` RVA 0x346A8F60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fbe022245a9bfc94](../../evidence/conditions-sets-097.md#c-fbe022245a9bfc94)

### observed_connections-008840

```text
(config-router-sf-topology)# eigrp log-event-type <cr>
```

Handler ` RVA 0xF596700 `；selector ` 34 `；EOL ` RVA 0x346AB528 `。

模式根 ` RVA 0x346A8F60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fcdacbbf7b656eac](../../evidence/conditions-sets-098.md#c-fcdacbbf7b656eac)

### observed_connections-008837

```text
(config-router-sf-topology)# exit-sf-topology <cr>
```

Handler ` RVA 0xF5939F0 `；selector ` 0 `；EOL ` RVA 0x346A91B0 `。

模式根 ` RVA 0x346A8F60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5ec666f7492a14f4](../../evidence/conditions-sets-037.md#c-5ec666f7492a14f4)

### observed_connections-008838

```text
(config-router-sf-topology)# external-client <string> <cr>
```

Handler ` RVA 0xF594330 `；selector ` 0 `；EOL ` RVA 0x346A9D00 `。

模式根 ` RVA 0x346A8F60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Client Label (max 64 characters)。

[条件 C-6de4c90ae191c524](../../evidence/conditions-sets-042.md#c-6de4c90ae191c524) · [参数 P-83fa09c2d6099b4b](../../evidence/parameters-sets-010.md#p-83fa09c2d6099b4b)

### observed_connections-008844

```text
(config-router-sf-topology)# metric maximum-hops <number:1..255> <cr>
```

Handler ` RVA 0xF57D6C0 `；selector ` 31 `；EOL ` RVA 0x346AA088 `。

模式根 ` RVA 0x346A8F60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Hop count。

[条件 C-f7930de887c19add](../../evidence/conditions-sets-096.md#c-f7930de887c19add) · [参数 P-8c7e0970dea39215](../../evidence/parameters-sets-011.md#p-8c7e0970dea39215)

### observed_connections-008855

```text
(config-router-sf-topology)# no eigrp event-log-size <cr>
```

Handler ` RVA 0xF596700 `；selector ` 35 `；EOL ` RVA 0x346ABC28 `。

模式根 ` RVA 0x346A8F60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-47e4fda0da7c2870](../../evidence/conditions-sets-028.md#c-47e4fda0da7c2870) · [状态效果 S-25c0f08c9bf5e645](../../evidence/state_effects-sets-008.md#s-25c0f08c9bf5e645)

### observed_connections-008850

```text
(config-router-sf-topology)# no eigrp event-logging <cr>
```

Handler ` RVA 0xF596700 `；selector ` 36 `；EOL ` RVA 0x346AB910 `。

模式根 ` RVA 0x346A8F60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-fbe022245a9bfc94](../../evidence/conditions-sets-097.md#c-fbe022245a9bfc94) · [状态效果 S-25c0f08c9bf5e645](../../evidence/state_effects-sets-008.md#s-25c0f08c9bf5e645)

### observed_connections-008852

```text
(config-router-sf-topology)# no eigrp log-event-type <cr>
```

Handler ` RVA 0xF596700 `；selector ` 34 `；EOL ` RVA 0x346AB528 `。

模式根 ` RVA 0x346A8F60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4746f95ea7679bbb](../../evidence/conditions-sets-028.md#c-4746f95ea7679bbb) · [状态效果 S-25c0f08c9bf5e645](../../evidence/state_effects-sets-008.md#s-25c0f08c9bf5e645)

### observed_connections-008841

```text
(config-router-sf-topology)# no external-client <string> <cr>
```

Handler ` RVA 0xF594330 `；selector ` 0 `；EOL ` RVA 0x346A9D00 `。

模式根 ` RVA 0x346A8F60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Client Label (max 64 characters)。

[条件 C-6de4c90ae191c524](../../evidence/conditions-sets-042.md#c-6de4c90ae191c524) · [参数 P-83fa09c2d6099b4b](../../evidence/parameters-sets-010.md#p-83fa09c2d6099b4b) · [状态效果 S-25c0f08c9bf5e645](../../evidence/state_effects-sets-008.md#s-25c0f08c9bf5e645)

### observed_connections-008843

```text
(config-router-sf-topology)# no metric maximum-hops <cr>
```

Handler ` RVA 0xF57D6C0 `；selector ` 31 `；EOL ` RVA 0x346AA088 `。

模式根 ` RVA 0x346A8F60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5defd3a1030812bd](../../evidence/conditions-sets-037.md#c-5defd3a1030812bd) · [状态效果 S-25c0f08c9bf5e645](../../evidence/state_effects-sets-008.md#s-25c0f08c9bf5e645)

### observed_connections-008859

```text
(config-router-sf-topology)# no redistribute eigrp <number:1..65535> <cr>
```

Handler ` RVA 0xF593E60 `；selector ` 32 `；EOL ` RVA 0x346AACE8 `。

模式根 ` RVA 0x346A8F60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Autonomous-System number。

[条件 C-142dec5a99cd43e6](../../evidence/conditions-sets-008.md#c-142dec5a99cd43e6) · [参数 P-3d447b0d15c9b3cf](../../evidence/parameters-sets-005.md#p-3d447b0d15c9b3cf) · [状态效果 S-25c0f08c9bf5e645](../../evidence/state_effects-sets-008.md#s-25c0f08c9bf5e645)

### observed_connections-008846

```text
(config-router-sf-topology)# no redistribute maximum-service <cr>
```

Handler ` RVA 0xF598EF0 `；selector ` 33 `；EOL ` RVA 0x346AA450 `。

模式根 ` RVA 0x346A8F60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-3fe8ab449157ffaf](../../evidence/conditions-sets-025.md#c-3fe8ab449157ffaf) · [状态效果 S-25c0f08c9bf5e645](../../evidence/state_effects-sets-008.md#s-25c0f08c9bf5e645)

### observed_connections-008848

```text
(config-router-sf-topology)# no timers active-time <cr>
```

Handler ` RVA 0xF597780 `；selector ` 28 `；EOL ` RVA 0x346AB138 `。

模式根 ` RVA 0x346A8F60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4792bf5e37715ba8](../../evidence/conditions-sets-028.md#c-4792bf5e37715ba8) · [状态效果 S-25c0f08c9bf5e645](../../evidence/state_effects-sets-008.md#s-25c0f08c9bf5e645)

### observed_connections-008856

```text
(config-router-sf-topology)# redistribute eigrp <number:1..65535> <cr>
```

Handler ` RVA 0xF593E60 `；selector ` 32 `；EOL ` RVA 0x346AACE8 `。

模式根 ` RVA 0x346A8F60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Autonomous-System number。

[条件 C-142dec5a99cd43e6](../../evidence/conditions-sets-008.md#c-142dec5a99cd43e6) · [参数 P-3d447b0d15c9b3cf](../../evidence/parameters-sets-005.md#p-3d447b0d15c9b3cf)

### observed_connections-008858

```text
(config-router-sf-topology)# redistribute maximum-service <number:1..4294967295> <cr>
```

Handler ` RVA 0xF598EF0 `；selector ` 33 `；EOL ` RVA 0x346AA450 `。

模式根 ` RVA 0x346A8F60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Maximum number of services redisted。

[条件 C-36f52c16571bb84f](../../evidence/conditions-sets-021.md#c-36f52c16571bb84f) · [参数 P-10003bc41a017332](../../evidence/parameters-sets-002.md#p-10003bc41a017332)

### observed_connections-008849

```text
(config-router-sf-topology)# timers active-time disabled <cr>
```

Handler ` RVA 0xF597780 `；selector ` 28 `；EOL ` RVA 0x346AB138 `。

模式根 ` RVA 0x346A8F60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-62593d5d88de3a8e](../../evidence/conditions-sets-038.md#c-62593d5d88de3a8e)
