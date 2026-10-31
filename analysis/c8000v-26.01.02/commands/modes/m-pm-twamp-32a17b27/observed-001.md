# pm-twamp · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-009342

```text
(config-pm-twamp)# default <cr>
```

Handler ` RVA 0x1ACEF5A0 `；selector ` 0 `；EOL ` RVA 0x36DD78D8 `。

模式根 ` RVA 0x36DC1CC8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-de4d777728585d80](../../evidence/state_effects-sets-047.md#s-de4d777728585d80)

### observed_connections-009346

```text
(config-pm-twamp)# default measurement delay <cr>
```

Handler ` RVA 0x1ACF31D0 `；selector ` 0 `；EOL ` RVA 0x36DD7658 `。

模式根 ` RVA 0x36DC1CC8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-de4d777728585d80](../../evidence/state_effects-sets-047.md#s-de4d777728585d80)

### observed_connections-009348

```text
(config-pm-twamp)# default measurement delay unauthenticated <cr>
```

Handler ` RVA 0x1ACF3310 `；selector ` 0 `；EOL ` RVA 0x36DD6FB8 `。

模式根 ` RVA 0x36DC1CC8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-de4d777728585d80](../../evidence/state_effects-sets-047.md#s-de4d777728585d80)

### observed_connections-009351

```text
(config-pm-twamp)# default measurement delay unauthenticated querier-dst-port <number:1024..14999> <cr>
```

Handler ` RVA 0x1ACF3BA0 `；selector ` 0 `；EOL ` RVA 0x36DD7308 `。

模式根 ` RVA 0x36DC1CC8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Port number。

[条件 C-d77803c57e1f22d5](../../evidence/conditions-sets-083.md#c-d77803c57e1f22d5) · [参数 P-3c1718846fb39911](../../evidence/parameters-sets-005.md#p-3c1718846fb39911) · [状态效果 S-c41bafd1c97b3cb9](../../evidence/state_effects-sets-042.md#s-c41bafd1c97b3cb9)

### observed_connections-009340

```text
(config-pm-twamp)# exit <cr>
```

Handler ` RVA 0x1ACF32A0 `；selector ` 0 `；EOL ` RVA 0x36DE0A80 `。

模式根 ` RVA 0x36DC1CC8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-832a8defdfe88c82](../../evidence/conditions-sets-051.md#c-832a8defdfe88c82)

### observed_connections-009343

```text
(config-pm-twamp)# measurement delay <cr>
```

Handler ` RVA 0x1ACF31D0 `；selector ` 0 `；EOL ` RVA 0x36DD7658 `。

模式根 ` RVA 0x36DC1CC8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-009345

```text
(config-pm-twamp)# measurement delay unauthenticated <cr>
```

Handler ` RVA 0x1ACF3310 `；selector ` 0 `；EOL ` RVA 0x36DD6FB8 `。

模式根 ` RVA 0x36DC1CC8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-009349

```text
(config-pm-twamp)# measurement delay unauthenticated querier-dst-port <number:1024..14999> <cr>
```

Handler ` RVA 0x1ACF3BA0 `；selector ` 0 `；EOL ` RVA 0x36DD7308 `。

模式根 ` RVA 0x36DC1CC8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Port number。

[条件 C-d77803c57e1f22d5](../../evidence/conditions-sets-083.md#c-d77803c57e1f22d5) · [参数 P-3c1718846fb39911](../../evidence/parameters-sets-005.md#p-3c1718846fb39911) · [状态效果 S-04e0e993f9b84a80](../../evidence/state_effects-sets-001.md#s-04e0e993f9b84a80)

### observed_connections-009341

```text
(config-pm-twamp)# no <cr>
```

Handler ` RVA 0x1ACEF5A0 `；selector ` 0 `；EOL ` RVA 0x36DD78D8 `。

模式根 ` RVA 0x36DC1CC8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-e437855c057e5256](../../evidence/state_effects-sets-048.md#s-e437855c057e5256)

### observed_connections-009344

```text
(config-pm-twamp)# no measurement delay <cr>
```

Handler ` RVA 0x1ACF31D0 `；selector ` 0 `；EOL ` RVA 0x36DD7658 `。

模式根 ` RVA 0x36DC1CC8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-e437855c057e5256](../../evidence/state_effects-sets-048.md#s-e437855c057e5256)

### observed_connections-009347

```text
(config-pm-twamp)# no measurement delay unauthenticated <cr>
```

Handler ` RVA 0x1ACF3310 `；selector ` 0 `；EOL ` RVA 0x36DD6FB8 `。

模式根 ` RVA 0x36DC1CC8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-e437855c057e5256](../../evidence/state_effects-sets-048.md#s-e437855c057e5256)

### observed_connections-009350

```text
(config-pm-twamp)# no measurement delay unauthenticated querier-dst-port <number:1024..14999> <cr>
```

Handler ` RVA 0x1ACF3BA0 `；selector ` 0 `；EOL ` RVA 0x36DD7308 `。

模式根 ` RVA 0x36DC1CC8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Port number。

[条件 C-d77803c57e1f22d5](../../evidence/conditions-sets-083.md#c-d77803c57e1f22d5) · [参数 P-3c1718846fb39911](../../evidence/parameters-sets-005.md#p-3c1718846fb39911) · [状态效果 S-9512b682d5c9f167](../../evidence/state_effects-sets-032.md#s-9512b682d5c9f167)

### observed_connections-009339

```text
(config-pm-twamp)# <cr>
```

Handler ` RVA 0x1ACEF5A0 `；selector ` 0 `；EOL ` RVA 0x36DD78D8 `。

模式根 ` RVA 0x36DC1CC8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。
