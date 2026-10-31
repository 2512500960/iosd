# ecfm_mep_int · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-009009

```text
(config-if-ecfm-mep)# alarm delay <number:2500..10000> <cr>
```

Handler ` RVA 0xBDD0030 `；selector ` 0 `；EOL ` RVA 0x338F30E8 `。

模式根 ` RVA 0x338CA0D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` msec (default 2500 msec)。

[条件 C-4ae73e88dc4d889b](../../evidence/conditions-sets-029.md#c-4ae73e88dc4d889b) · [参数 P-8e80f7b575f3efa2](../../evidence/parameters-sets-011.md#p-8e80f7b575f3efa2)

### observed_connections-009012

```text
(config-if-ecfm-mep)# alarm notification all <cr>
```

Handler ` RVA 0xBDCFF00 `；selector ` 0 `；EOL ` RVA 0x338F33D8 `。

模式根 ` RVA 0x338CA0D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-57a2e82985979e4b](../../evidence/conditions-sets-034.md#c-57a2e82985979e4b) · [状态效果 S-f52cb6921f082bf8](../../evidence/state_effects-sets-052.md#s-f52cb6921f082bf8)

### observed_connections-009006

```text
(config-if-ecfm-mep)# alarm reset <number:2500..10000> <cr>
```

Handler ` RVA 0xBDD0180 `；selector ` 0 `；EOL ` RVA 0x338F2DD0 `。

模式根 ` RVA 0x338CA0D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` msec (default 10000 msec)。

[条件 C-f3514959eed75e16](../../evidence/conditions-sets-094.md#c-f3514959eed75e16) · [参数 P-f4a8e913ebbf1c3a](../../evidence/parameters-sets-018.md#p-f4a8e913ebbf1c3a)

### observed_connections-009003

```text
(config-if-ecfm-mep)# continuity-check static rmep <cr>
```

Handler ` RVA 0xBDCFA90 `；selector ` 0 `；EOL ` RVA 0x338F26C0 `。

模式根 ` RVA 0x338CA0D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-03fc550e183c5a19](../../evidence/conditions-sets-002.md#c-03fc550e183c5a19)

### observed_connections-009001

```text
(config-if-ecfm-mep)# cos <number:0..7> <cr>
```

Handler ` RVA 0xBDCF8B0 `；selector ` 0 `；EOL ` RVA 0x338F2350 `。

模式根 ` RVA 0x338CA0D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` CoS value。

[条件 C-9306b99a216f6ba2](../../evidence/conditions-sets-057.md#c-9306b99a216f6ba2) · [参数 P-7c2fca43ab38e566](../../evidence/parameters-sets-010.md#p-7c2fca43ab38e566)

### observed_connections-009010

```text
(config-if-ecfm-mep)# default alarm delay <cr>
```

Handler ` RVA 0xBDD0030 `；selector ` 0 `；EOL ` RVA 0x338F30E8 `。

模式根 ` RVA 0x338CA0D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-653973aed62816e2](../../evidence/conditions-sets-039.md#c-653973aed62816e2) · [状态效果 S-012aa64cc0bbd5de](../../evidence/state_effects-sets-001.md#s-012aa64cc0bbd5de)

### observed_connections-009014

```text
(config-if-ecfm-mep)# default alarm notification <cr>
```

Handler ` RVA 0xBDCFF00 `；selector ` 0 `；EOL ` RVA 0x338F33D8 `。

模式根 ` RVA 0x338CA0D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7237cbe2a66731d0](../../evidence/conditions-sets-044.md#c-7237cbe2a66731d0) · [状态效果 S-012aa64cc0bbd5de](../../evidence/state_effects-sets-001.md#s-012aa64cc0bbd5de)

### observed_connections-009007

```text
(config-if-ecfm-mep)# default alarm reset <cr>
```

Handler ` RVA 0xBDD0180 `；selector ` 0 `；EOL ` RVA 0x338F2DD0 `。

模式根 ` RVA 0x338CA0D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-52ee08e5db5c2f8d](../../evidence/conditions-sets-032.md#c-52ee08e5db5c2f8d) · [状态效果 S-012aa64cc0bbd5de](../../evidence/state_effects-sets-001.md#s-012aa64cc0bbd5de)

### observed_connections-009016

```text
(config-if-ecfm-mep)# default continuity-check static rmep <cr>
```

Handler ` RVA 0xBDCFA90 `；selector ` 0 `；EOL ` RVA 0x338F26C0 `。

模式根 ` RVA 0x338CA0D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-03fc550e183c5a19](../../evidence/conditions-sets-002.md#c-03fc550e183c5a19) · [状态效果 S-012aa64cc0bbd5de](../../evidence/state_effects-sets-001.md#s-012aa64cc0bbd5de)

### observed_connections-009002

```text
(config-if-ecfm-mep)# default cos <cr>
```

Handler ` RVA 0xBDCF8B0 `；selector ` 0 `；EOL ` RVA 0x338F2350 `。

模式根 ` RVA 0x338CA0D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-11f7e6dd9236f917](../../evidence/conditions-sets-007.md#c-11f7e6dd9236f917) · [状态效果 S-012aa64cc0bbd5de](../../evidence/state_effects-sets-001.md#s-012aa64cc0bbd5de)

### observed_connections-009020

```text
(config-if-ecfm-mep)# default monitor loss counter <cr>
```

Handler ` RVA 0xBDD02D0 `；selector ` 0 `；EOL ` RVA 0x338F3990 `。

模式根 ` RVA 0x338CA0D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-664420acf998ba20](../../evidence/conditions-sets-039.md#c-664420acf998ba20) · [状态效果 S-012aa64cc0bbd5de](../../evidence/state_effects-sets-001.md#s-012aa64cc0bbd5de)

### observed_connections-009018

```text
(config-if-ecfm-mep)# default rmep mpid <number:1..8191> <cr>
```

Handler ` RVA 0xBDCFC00 `；selector ` 0 `；EOL ` RVA 0x338F2A40 `。

模式根 ` RVA 0x338CA0D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Identifier value。

[条件 C-027fb8288ed0cf67](../../evidence/conditions-sets-001.md#c-027fb8288ed0cf67) · [参数 P-0f7c8ff859711fc2](../../evidence/parameters-sets-002.md#p-0f7c8ff859711fc2) · [状态效果 S-012aa64cc0bbd5de](../../evidence/state_effects-sets-001.md#s-012aa64cc0bbd5de)

### observed_connections-008999

```text
(config-if-ecfm-mep)# exit <cr>
```

Handler ` RVA 0xBDBEAC0 `；selector ` 0 `；EOL ` RVA 0x338CA8B8 `。

模式根 ` RVA 0x338CA0D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1d25a7181d29167b](../../evidence/conditions-sets-011.md#c-1d25a7181d29167b)

### observed_connections-009013

```text
(config-if-ecfm-mep)# monitor loss counter <cr>
```

Handler ` RVA 0xBDD02D0 `；selector ` 0 `；EOL ` RVA 0x338F3990 `。

模式根 ` RVA 0x338CA0D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-664420acf998ba20](../../evidence/conditions-sets-039.md#c-664420acf998ba20)

### observed_connections-009008

```text
(config-if-ecfm-mep)# no alarm delay <cr>
```

Handler ` RVA 0xBDD0030 `；selector ` 0 `；EOL ` RVA 0x338F30E8 `。

模式根 ` RVA 0x338CA0D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-85d58bede8015f98](../../evidence/conditions-sets-052.md#c-85d58bede8015f98) · [状态效果 S-c9100573f7ed45e8](../../evidence/state_effects-sets-043.md#s-c9100573f7ed45e8)

### observed_connections-009011

```text
(config-if-ecfm-mep)# no alarm notification <cr>
```

Handler ` RVA 0xBDCFF00 `；selector ` 0 `；EOL ` RVA 0x338F33D8 `。

模式根 ` RVA 0x338CA0D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-6d4a918dda874372](../../evidence/conditions-sets-042.md#c-6d4a918dda874372) · [状态效果 S-c9100573f7ed45e8](../../evidence/state_effects-sets-043.md#s-c9100573f7ed45e8)

### observed_connections-009005

```text
(config-if-ecfm-mep)# no alarm reset <cr>
```

Handler ` RVA 0xBDD0180 `；selector ` 0 `；EOL ` RVA 0x338F2DD0 `。

模式根 ` RVA 0x338CA0D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4ebdc3feccde2fc2](../../evidence/conditions-sets-031.md#c-4ebdc3feccde2fc2) · [状态效果 S-c9100573f7ed45e8](../../evidence/state_effects-sets-043.md#s-c9100573f7ed45e8)

### observed_connections-009015

```text
(config-if-ecfm-mep)# no continuity-check static rmep <cr>
```

Handler ` RVA 0xBDCFA90 `；selector ` 0 `；EOL ` RVA 0x338F26C0 `。

模式根 ` RVA 0x338CA0D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-03fc550e183c5a19](../../evidence/conditions-sets-002.md#c-03fc550e183c5a19) · [状态效果 S-c9100573f7ed45e8](../../evidence/state_effects-sets-043.md#s-c9100573f7ed45e8)

### observed_connections-009000

```text
(config-if-ecfm-mep)# no cos <cr>
```

Handler ` RVA 0xBDCF8B0 `；selector ` 0 `；EOL ` RVA 0x338F2350 `。

模式根 ` RVA 0x338CA0D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f93a517ae729708f](../../evidence/conditions-sets-096.md#c-f93a517ae729708f) · [状态效果 S-c9100573f7ed45e8](../../evidence/state_effects-sets-043.md#s-c9100573f7ed45e8)

### observed_connections-009019

```text
(config-if-ecfm-mep)# no monitor loss counter <cr>
```

Handler ` RVA 0xBDD02D0 `；selector ` 0 `；EOL ` RVA 0x338F3990 `。

模式根 ` RVA 0x338CA0D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-664420acf998ba20](../../evidence/conditions-sets-039.md#c-664420acf998ba20) · [状态效果 S-c9100573f7ed45e8](../../evidence/state_effects-sets-043.md#s-c9100573f7ed45e8)

### observed_connections-009017

```text
(config-if-ecfm-mep)# no rmep mpid <number:1..8191> <cr>
```

Handler ` RVA 0xBDCFC00 `；selector ` 0 `；EOL ` RVA 0x338F2A40 `。

模式根 ` RVA 0x338CA0D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Identifier value。

[条件 C-027fb8288ed0cf67](../../evidence/conditions-sets-001.md#c-027fb8288ed0cf67) · [参数 P-0f7c8ff859711fc2](../../evidence/parameters-sets-002.md#p-0f7c8ff859711fc2) · [状态效果 S-c9100573f7ed45e8](../../evidence/state_effects-sets-043.md#s-c9100573f7ed45e8)

### observed_connections-009004

```text
(config-if-ecfm-mep)# rmep mpid <number:1..8191> <cr>
```

Handler ` RVA 0xBDCFC00 `；selector ` 0 `；EOL ` RVA 0x338F2A40 `。

模式根 ` RVA 0x338CA0D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Identifier value。

[条件 C-027fb8288ed0cf67](../../evidence/conditions-sets-001.md#c-027fb8288ed0cf67) · [参数 P-0f7c8ff859711fc2](../../evidence/parameters-sets-002.md#p-0f7c8ff859711fc2)

