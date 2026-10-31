# if-topo · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-008816

```text
(config-if-topology)# default ip ospf cost <cr>
```

Handler ` RVA 0xFCEEEF0 `；selector ` 0 `；EOL ` RVA 0x348B2E38 `。

模式根 ` RVA 0x33FDD4E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-cf32f199e980c167](../../evidence/conditions-sets-080.md#c-cf32f199e980c167) · [状态效果 S-07d25737e268fb0b](../../evidence/state_effects-sets-002.md#s-07d25737e268fb0b)

### observed_connections-008834

```text
(config-if-topology)# default ip ospf topology disable <cr>
```

Handler ` RVA 0xFCEEEF0 `；selector ` 19 `；EOL ` RVA 0x348B2E78 `。

模式根 ` RVA 0x33FDD4E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-07d25737e268fb0b](../../evidence/state_effects-sets-002.md#s-07d25737e268fb0b)

### observed_connections-008829

```text
(config-if-topology)# default isis advertise prefix <cr>
```

Handler ` RVA 0xFD2A2C0 `；selector ` 82 `；EOL ` RVA 0x34B99708 `。

模式根 ` RVA 0x33FDD4E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f293d7711e69498a](../../evidence/conditions-sets-094.md#c-f293d7711e69498a) · [状态效果 S-07d25737e268fb0b](../../evidence/state_effects-sets-002.md#s-07d25737e268fb0b)

### observed_connections-008822

```text
(config-if-topology)# default isis metric <cr>
```

Handler ` RVA 0xFD2A2C0 `；selector ` 7 `；EOL ` RVA 0x34B989B0 `。

模式根 ` RVA 0x33FDD4E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e9cef10f9464840a](../../evidence/conditions-sets-090.md#c-e9cef10f9464840a) · [状态效果 S-df261292e764b600](../../evidence/state_effects-sets-047.md#s-df261292e764b600)

### observed_connections-008832

```text
(config-if-topology)# default isis prefix-attributes n-flag-clear <cr>
```

Handler ` RVA 0xFD2A2C0 `；selector ` 83 `；EOL ` RVA 0x34B99B08 `。

模式根 ` RVA 0x33FDD4E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e04706837e526737](../../evidence/conditions-sets-086.md#c-e04706837e526737) · [状态效果 S-edbfb301066022f4](../../evidence/state_effects-sets-050.md#s-edbfb301066022f4)

### observed_connections-008825

```text
(config-if-topology)# default isis tag <number:1..4294967295> <cr>
```

Handler ` RVA 0xFD2A2C0 `；selector ` 33 `；EOL ` RVA 0x34B99340 `。

模式根 ` RVA 0x33FDD4E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Admin tag number。

[条件 C-f293d7711e69498a](../../evidence/conditions-sets-094.md#c-f293d7711e69498a) · [参数 P-5c58e35d2b2453f6](../../evidence/parameters-sets-007.md#p-5c58e35d2b2453f6) · [状态效果 S-07d25737e268fb0b](../../evidence/state_effects-sets-002.md#s-07d25737e268fb0b)

### observed_connections-008836

```text
(config-if-topology)# default isis te-metric flex-algo <number:1..16777214> <cr>
```

Handler ` RVA 0xFD2A2C0 `；selector ` 8 `；EOL ` RVA 0x34B98F90 `。

模式根 ` RVA 0x33FDD4E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` te-metric value。

[条件 C-be467b92f55b0f5c](../../evidence/conditions-sets-073.md#c-be467b92f55b0f5c) · [参数 P-9606c1711a30efd9](../../evidence/parameters-sets-012.md#p-9606c1711a30efd9) · [状态效果 S-23ae47a20cb939e6](../../evidence/state_effects-sets-008.md#s-23ae47a20cb939e6)

### observed_connections-008828

```text
(config-if-topology)# default isis topology disable <cr>
```

Handler ` RVA 0xFD2A2C0 `；selector ` 91 `；EOL ` RVA 0x34B99E50 `。

模式根 ` RVA 0x33FDD4E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-bc702eb282aa4c91](../../evidence/conditions-sets-073.md#c-bc702eb282aa4c91) · [状态效果 S-07d25737e268fb0b](../../evidence/state_effects-sets-002.md#s-07d25737e268fb0b)

### observed_connections-008812

```text
(config-if-topology)# exit-if-topo <cr>
```

Handler ` RVA 0xDB7A0B0 `；selector ` 0 `；EOL ` RVA 0x33FDD628 `。

模式根 ` RVA 0x33FDD4E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0debeb42cf12fd09](../../evidence/conditions-sets-006.md#c-0debeb42cf12fd09)

### observed_connections-008813

```text
(config-if-topology)# ip ospf cost <number:1..65535> <cr>
```

Handler ` RVA 0xFCEEEF0 `；selector ` 0 `；EOL ` RVA 0x348B2E38 `。

模式根 ` RVA 0x33FDD4E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Cost。

[条件 C-57bf56a76aad45be](../../evidence/conditions-sets-034.md#c-57bf56a76aad45be) · [参数 P-2020c1ba4108c9d1](../../evidence/parameters-sets-003.md#p-2020c1ba4108c9d1)

### observed_connections-008824

```text
(config-if-topology)# ip ospf topology disable <cr>
```

Handler ` RVA 0xFCEEEF0 `；selector ` 19 `；EOL ` RVA 0x348B2E78 `。

模式根 ` RVA 0x33FDD4E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-008818

```text
(config-if-topology)# isis advertise prefix <cr>
```

Handler ` RVA 0xFD2A2C0 `；selector ` 82 `；EOL ` RVA 0x34B99708 `。

模式根 ` RVA 0x33FDD4E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f293d7711e69498a](../../evidence/conditions-sets-094.md#c-f293d7711e69498a)

### observed_connections-008819

```text
(config-if-topology)# isis metric <number:1..16777214> <cr>
```

Handler ` RVA 0xFD2A2C0 `；selector ` 7 `；EOL ` RVA 0x34B989B0 `。

模式根 ` RVA 0x33FDD4E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Default metric。

[条件 C-f293d7711e69498a](../../evidence/conditions-sets-094.md#c-f293d7711e69498a) · [参数 P-46ee8adbb0a6fad7](../../evidence/parameters-sets-006.md#p-46ee8adbb0a6fad7) · [状态效果 S-9cba59a1c94e16ea](../../evidence/state_effects-sets-033.md#s-9cba59a1c94e16ea)

### observed_connections-008821

```text
(config-if-topology)# isis prefix-attributes n-flag-clear <cr>
```

Handler ` RVA 0xFD2A2C0 `；selector ` 83 `；EOL ` RVA 0x34B99B08 `。

模式根 ` RVA 0x33FDD4E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e04706837e526737](../../evidence/conditions-sets-086.md#c-e04706837e526737) · [状态效果 S-cd34c5f76e396622](../../evidence/state_effects-sets-043.md#s-cd34c5f76e396622)

### observed_connections-008814

```text
(config-if-topology)# isis tag <number:1..4294967295> <cr>
```

Handler ` RVA 0xFD2A2C0 `；selector ` 33 `；EOL ` RVA 0x34B99340 `。

模式根 ` RVA 0x33FDD4E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Admin tag number。

[条件 C-f293d7711e69498a](../../evidence/conditions-sets-094.md#c-f293d7711e69498a) · [参数 P-5c58e35d2b2453f6](../../evidence/parameters-sets-007.md#p-5c58e35d2b2453f6)

### observed_connections-008830

```text
(config-if-topology)# isis te-metric flex-algo <number:1..16777214> <cr>
```

Handler ` RVA 0xFD2A2C0 `；selector ` 8 `；EOL ` RVA 0x34B98F90 `。

模式根 ` RVA 0x33FDD4E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` te-metric value。

[条件 C-be467b92f55b0f5c](../../evidence/conditions-sets-073.md#c-be467b92f55b0f5c) · [参数 P-9606c1711a30efd9](../../evidence/parameters-sets-012.md#p-9606c1711a30efd9) · [状态效果 S-c3889aca96342559](../../evidence/state_effects-sets-041.md#s-c3889aca96342559)

### observed_connections-008817

```text
(config-if-topology)# isis topology disable <cr>
```

Handler ` RVA 0xFD2A2C0 `；selector ` 91 `；EOL ` RVA 0x34B99E50 `。

模式根 ` RVA 0x33FDD4E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bc702eb282aa4c91](../../evidence/conditions-sets-073.md#c-bc702eb282aa4c91)

### observed_connections-008815

```text
(config-if-topology)# no ip ospf cost <cr>
```

Handler ` RVA 0xFCEEEF0 `；selector ` 0 `；EOL ` RVA 0x348B2E38 `。

模式根 ` RVA 0x33FDD4E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-cf32f199e980c167](../../evidence/conditions-sets-080.md#c-cf32f199e980c167) · [状态效果 S-29aa1259591abe64](../../evidence/state_effects-sets-009.md#s-29aa1259591abe64)

### observed_connections-008833

```text
(config-if-topology)# no ip ospf topology disable <cr>
```

Handler ` RVA 0xFCEEEF0 `；selector ` 19 `；EOL ` RVA 0x348B2E78 `。

模式根 ` RVA 0x33FDD4E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-29aa1259591abe64](../../evidence/state_effects-sets-009.md#s-29aa1259591abe64)

### observed_connections-008827

```text
(config-if-topology)# no isis advertise prefix <cr>
```

Handler ` RVA 0xFD2A2C0 `；selector ` 82 `；EOL ` RVA 0x34B99708 `。

模式根 ` RVA 0x33FDD4E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f293d7711e69498a](../../evidence/conditions-sets-094.md#c-f293d7711e69498a) · [状态效果 S-29aa1259591abe64](../../evidence/state_effects-sets-009.md#s-29aa1259591abe64)

### observed_connections-008820

```text
(config-if-topology)# no isis metric <cr>
```

Handler ` RVA 0xFD2A2C0 `；selector ` 7 `；EOL ` RVA 0x34B989B0 `。

模式根 ` RVA 0x33FDD4E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e9cef10f9464840a](../../evidence/conditions-sets-090.md#c-e9cef10f9464840a) · [状态效果 S-60f346a0afa708d5](../../evidence/state_effects-sets-021.md#s-60f346a0afa708d5)

### observed_connections-008831

```text
(config-if-topology)# no isis prefix-attributes n-flag-clear <cr>
```

Handler ` RVA 0xFD2A2C0 `；selector ` 83 `；EOL ` RVA 0x34B99B08 `。

模式根 ` RVA 0x33FDD4E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e04706837e526737](../../evidence/conditions-sets-086.md#c-e04706837e526737) · [状态效果 S-e4f2274754497d8f](../../evidence/state_effects-sets-048.md#s-e4f2274754497d8f)

### observed_connections-008823

```text
(config-if-topology)# no isis tag <number:1..4294967295> <cr>
```

Handler ` RVA 0xFD2A2C0 `；selector ` 33 `；EOL ` RVA 0x34B99340 `。

模式根 ` RVA 0x33FDD4E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Admin tag number。

[条件 C-f293d7711e69498a](../../evidence/conditions-sets-094.md#c-f293d7711e69498a) · [参数 P-5c58e35d2b2453f6](../../evidence/parameters-sets-007.md#p-5c58e35d2b2453f6) · [状态效果 S-29aa1259591abe64](../../evidence/state_effects-sets-009.md#s-29aa1259591abe64)

### observed_connections-008835

```text
(config-if-topology)# no isis te-metric flex-algo <number:1..16777214> <cr>
```

Handler ` RVA 0xFD2A2C0 `；selector ` 8 `；EOL ` RVA 0x34B98F90 `。

模式根 ` RVA 0x33FDD4E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` te-metric value。

[条件 C-be467b92f55b0f5c](../../evidence/conditions-sets-073.md#c-be467b92f55b0f5c) · [参数 P-9606c1711a30efd9](../../evidence/parameters-sets-012.md#p-9606c1711a30efd9) · [状态效果 S-e4b50d50a69abe53](../../evidence/state_effects-sets-048.md#s-e4b50d50a69abe53)

### observed_connections-008826

```text
(config-if-topology)# no isis topology disable <cr>
```

Handler ` RVA 0xFD2A2C0 `；selector ` 91 `；EOL ` RVA 0x34B99E50 `。

模式根 ` RVA 0x33FDD4E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-bc702eb282aa4c91](../../evidence/conditions-sets-073.md#c-bc702eb282aa4c91) · [状态效果 S-29aa1259591abe64](../../evidence/state_effects-sets-009.md#s-29aa1259591abe64)

