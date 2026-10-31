# interface-dlci · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-009192

```text
(config-fr-dlci)# bridge-domain <number:dynamic> <cr>
```

Handler ` RVA 0xBF7FCB0 `；selector ` 0 `；EOL ` RVA 0x33958EF8 `。

模式根 ` RVA 0x346FACF0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Bridge-domain number。

[条件 C-786c610659a3bacb](../../evidence/conditions-sets-047.md#c-786c610659a3bacb) · [缺口 G-b993303d8a3e9924](../../evidence/gaps-sets-007.md#g-b993303d8a3e9924) · [参数 P-735c645cccdd523e](../../evidence/parameters-sets-009.md#p-735c645cccdd523e) · [状态效果 S-81c0f83f21c5ffe1](../../evidence/state_effects-sets-028.md#s-81c0f83f21c5ffe1)

### observed_connections-009185

```text
(config-fr-dlci)# bridge-domain from-encapsulation <cr>
```

Handler ` RVA 0xBF7FCB0 `；selector ` 0 `；EOL ` RVA 0x33958EF8 `。

模式根 ` RVA 0x346FACF0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8e0e6f885175a68f](../../evidence/conditions-sets-055.md#c-8e0e6f885175a68f) · [状态效果 S-2e286579a5ad4927](../../evidence/state_effects-sets-010.md#s-2e286579a5ad4927)

### observed_connections-009180

```text
(config-fr-dlci)# class <string> <cr>
```

Handler ` RVA 0xF620810 `；selector ` 84 `；EOL ` RVA 0x3471D4C8 `。

模式根 ` RVA 0x346FACF0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` map class name。

[条件 C-64c4731960275c46](../../evidence/conditions-sets-039.md#c-64c4731960275c46) · [参数 P-8ee36c36c9fe4554](../../evidence/parameters-sets-011.md#p-8ee36c36c9fe4554) · [状态效果 S-5b4b6520b9fb307d](../../evidence/state_effects-sets-020.md#s-5b4b6520b9fb307d)

### observed_connections-009191

```text
(config-fr-dlci)# default bridge-domain from-encapsulation <cr>
```

Handler ` RVA 0xBF7FCB0 `；selector ` 0 `；EOL ` RVA 0x33958EF8 `。

模式根 ` RVA 0x346FACF0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8e0e6f885175a68f](../../evidence/conditions-sets-055.md#c-8e0e6f885175a68f) · [状态效果 S-7277b3927a172288](../../evidence/state_effects-sets-024.md#s-7277b3927a172288)

### observed_connections-009181

```text
(config-fr-dlci)# default class <cr>
```

Handler ` RVA 0xF620810 `；selector ` 84 `；EOL ` RVA 0x3471D4C8 `。

模式根 ` RVA 0x346FACF0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-47afe0ab920e44c1](../../evidence/conditions-sets-028.md#c-47afe0ab920e44c1) · [状态效果 S-21793251671ddae9](../../evidence/state_effects-sets-008.md#s-21793251671ddae9)

### observed_connections-009177

```text
(config-fr-dlci)# default exit <cr>
```

Handler ` RVA 0xF5F2350 `；selector ` 0 `；EOL ` RVA 0x34705F68 `。

模式根 ` RVA 0x346FACF0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-a056786e20cecded](../../evidence/state_effects-sets-034.md#s-a056786e20cecded)

### observed_connections-009184

```text
(config-fr-dlci)# default vofr <cr>
```

Handler ` RVA 0x113866F0 `；selector ` 102 `；EOL ` RVA 0x3549E8A0 `。

模式根 ` RVA 0x346FACF0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ec01560a606de398](../../evidence/conditions-sets-091.md#c-ec01560a606de398) · [状态效果 S-a056786e20cecded](../../evidence/state_effects-sets-034.md#s-a056786e20cecded)

### observed_connections-009187

```text
(config-fr-dlci)# default vofr cisco <cr>
```

Handler ` RVA 0x113866F0 `；selector ` 101 `；EOL ` RVA 0x3549E548 `。

模式根 ` RVA 0x346FACF0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ec01560a606de398](../../evidence/conditions-sets-091.md#c-ec01560a606de398) · [状态效果 S-a056786e20cecded](../../evidence/state_effects-sets-034.md#s-a056786e20cecded)

### observed_connections-009189

```text
(config-fr-dlci)# default x25-profile <string> <cr>
```

Handler ` RVA 0xEF2B0B0 `；selector ` 1 `；EOL ` RVA 0x3447E568 `。

模式根 ` RVA 0x346FACF0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Name of the X.25 profile。

[条件 C-ac7fcce6b5d766d6](../../evidence/conditions-sets-067.md#c-ac7fcce6b5d766d6) · [参数 P-39674fe2c4d39631](../../evidence/parameters-sets-005.md#p-39674fe2c4d39631) · [状态效果 S-a056786e20cecded](../../evidence/state_effects-sets-034.md#s-a056786e20cecded)

### observed_connections-009174

```text
(config-fr-dlci)# exit <cr>
```

Handler ` RVA 0xF5F2350 `；selector ` 0 `；EOL ` RVA 0x34705F68 `。

模式根 ` RVA 0x346FACF0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-009190

```text
(config-fr-dlci)# no bridge-domain from-encapsulation <cr>
```

Handler ` RVA 0xBF7FCB0 `；selector ` 0 `；EOL ` RVA 0x33958EF8 `。

模式根 ` RVA 0x346FACF0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8e0e6f885175a68f](../../evidence/conditions-sets-055.md#c-8e0e6f885175a68f) · [状态效果 S-b62be1dba21d9a9d](../../evidence/state_effects-sets-039.md#s-b62be1dba21d9a9d)

### observed_connections-009178

```text
(config-fr-dlci)# no class <cr>
```

Handler ` RVA 0xF620810 `；selector ` 84 `；EOL ` RVA 0x3471D4C8 `。

模式根 ` RVA 0x346FACF0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f29f8c4fb42f33c7](../../evidence/conditions-sets-094.md#c-f29f8c4fb42f33c7) · [状态效果 S-161cdab47f090068](../../evidence/state_effects-sets-005.md#s-161cdab47f090068)

### observed_connections-009176

```text
(config-fr-dlci)# no exit <cr>
```

Handler ` RVA 0xF5F2350 `；selector ` 0 `；EOL ` RVA 0x34705F68 `。

模式根 ` RVA 0x346FACF0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-1ddd2f13e2f25cf4](../../evidence/state_effects-sets-007.md#s-1ddd2f13e2f25cf4)

### observed_connections-009182

```text
(config-fr-dlci)# no vofr <cr>
```

Handler ` RVA 0x113866F0 `；selector ` 102 `；EOL ` RVA 0x3549E8A0 `。

模式根 ` RVA 0x346FACF0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ec01560a606de398](../../evidence/conditions-sets-091.md#c-ec01560a606de398) · [状态效果 S-1ddd2f13e2f25cf4](../../evidence/state_effects-sets-007.md#s-1ddd2f13e2f25cf4)

### observed_connections-009186

```text
(config-fr-dlci)# no vofr cisco <cr>
```

Handler ` RVA 0x113866F0 `；selector ` 101 `；EOL ` RVA 0x3549E548 `。

模式根 ` RVA 0x346FACF0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ec01560a606de398](../../evidence/conditions-sets-091.md#c-ec01560a606de398) · [状态效果 S-1ddd2f13e2f25cf4](../../evidence/state_effects-sets-007.md#s-1ddd2f13e2f25cf4)

### observed_connections-009188

```text
(config-fr-dlci)# no x25-profile <string> <cr>
```

Handler ` RVA 0xEF2B0B0 `；selector ` 1 `；EOL ` RVA 0x3447E568 `。

模式根 ` RVA 0x346FACF0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Name of the X.25 profile。

[条件 C-ac7fcce6b5d766d6](../../evidence/conditions-sets-067.md#c-ac7fcce6b5d766d6) · [参数 P-39674fe2c4d39631](../../evidence/parameters-sets-005.md#p-39674fe2c4d39631) · [状态效果 S-1ddd2f13e2f25cf4](../../evidence/state_effects-sets-007.md#s-1ddd2f13e2f25cf4)

### observed_connections-009175

```text
(config-fr-dlci)# vofr <cr>
```

Handler ` RVA 0x113866F0 `；selector ` 102 `；EOL ` RVA 0x3549E8A0 `。

模式根 ` RVA 0x346FACF0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ec01560a606de398](../../evidence/conditions-sets-091.md#c-ec01560a606de398)

### observed_connections-009179

```text
(config-fr-dlci)# vofr cisco <cr>
```

Handler ` RVA 0x113866F0 `；selector ` 101 `；EOL ` RVA 0x3549E548 `。

模式根 ` RVA 0x346FACF0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ec01560a606de398](../../evidence/conditions-sets-091.md#c-ec01560a606de398)

### observed_connections-009183

```text
(config-fr-dlci)# x25-profile <string> <cr>
```

Handler ` RVA 0xEF2B0B0 `；selector ` 1 `；EOL ` RVA 0x3447E568 `。

模式根 ` RVA 0x346FACF0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of the X.25 profile。

[条件 C-ac7fcce6b5d766d6](../../evidence/conditions-sets-067.md#c-ac7fcce6b5d766d6) · [参数 P-39674fe2c4d39631](../../evidence/parameters-sets-005.md#p-39674fe2c4d39631)
