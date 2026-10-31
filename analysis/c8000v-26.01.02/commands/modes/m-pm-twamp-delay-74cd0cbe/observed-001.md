# pm-twamp-delay · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-009493

```text
(config-pm-twamp-delay)# default <cr>
```

Handler ` RVA 0x1ACF31D0 `；selector ` 0 `；EOL ` RVA 0x36DD7658 `。

模式根 ` RVA 0x36DC1CF0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-9206449c181d3975](../../evidence/state_effects-sets-031.md#s-9206449c181d3975)

### observed_connections-009495

```text
(config-pm-twamp-delay)# default unauthenticated <cr>
```

Handler ` RVA 0x1ACF3310 `；selector ` 0 `；EOL ` RVA 0x36DD6FB8 `。

模式根 ` RVA 0x36DC1CF0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-9206449c181d3975](../../evidence/state_effects-sets-031.md#s-9206449c181d3975)

### observed_connections-009498

```text
(config-pm-twamp-delay)# default unauthenticated querier-dst-port <number:1024..14999> <cr>
```

Handler ` RVA 0x1ACF3BA0 `；selector ` 0 `；EOL ` RVA 0x36DD7308 `。

模式根 ` RVA 0x36DC1CF0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Port number。

[条件 C-d77803c57e1f22d5](../../evidence/conditions-sets-083.md#c-d77803c57e1f22d5) · [参数 P-3c1718846fb39911](../../evidence/parameters-sets-005.md#p-3c1718846fb39911) · [状态效果 S-2cdad9bae9d82caa](../../evidence/state_effects-sets-010.md#s-2cdad9bae9d82caa)

### observed_connections-009490

```text
(config-pm-twamp-delay)# exit <cr>
```

Handler ` RVA 0x1ACF3560 `；selector ` 0 `；EOL ` RVA 0x36DE0E88 `。

模式根 ` RVA 0x36DC1CF0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8b358e80e3c5a871](../../evidence/conditions-sets-054.md#c-8b358e80e3c5a871)

### observed_connections-009491

```text
(config-pm-twamp-delay)# no <cr>
```

Handler ` RVA 0x1ACF31D0 `；selector ` 0 `；EOL ` RVA 0x36DD7658 `。

模式根 ` RVA 0x36DC1CF0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-2fd9774e70835732](../../evidence/state_effects-sets-011.md#s-2fd9774e70835732)

### observed_connections-009494

```text
(config-pm-twamp-delay)# no unauthenticated <cr>
```

Handler ` RVA 0x1ACF3310 `；selector ` 0 `；EOL ` RVA 0x36DD6FB8 `。

模式根 ` RVA 0x36DC1CF0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-2fd9774e70835732](../../evidence/state_effects-sets-011.md#s-2fd9774e70835732)

### observed_connections-009497

```text
(config-pm-twamp-delay)# no unauthenticated querier-dst-port <number:1024..14999> <cr>
```

Handler ` RVA 0x1ACF3BA0 `；selector ` 0 `；EOL ` RVA 0x36DD7308 `。

模式根 ` RVA 0x36DC1CF0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Port number。

[条件 C-d77803c57e1f22d5](../../evidence/conditions-sets-083.md#c-d77803c57e1f22d5) · [参数 P-3c1718846fb39911](../../evidence/parameters-sets-005.md#p-3c1718846fb39911) · [状态效果 S-8914f7e63c060e51](../../evidence/state_effects-sets-029.md#s-8914f7e63c060e51)

### observed_connections-009492

```text
(config-pm-twamp-delay)# unauthenticated <cr>
```

Handler ` RVA 0x1ACF3310 `；selector ` 0 `；EOL ` RVA 0x36DD6FB8 `。

模式根 ` RVA 0x36DC1CF0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-009496

```text
(config-pm-twamp-delay)# unauthenticated querier-dst-port <number:1024..14999> <cr>
```

Handler ` RVA 0x1ACF3BA0 `；selector ` 0 `；EOL ` RVA 0x36DD7308 `。

模式根 ` RVA 0x36DC1CF0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Port number。

[条件 C-d77803c57e1f22d5](../../evidence/conditions-sets-083.md#c-d77803c57e1f22d5) · [参数 P-3c1718846fb39911](../../evidence/parameters-sets-005.md#p-3c1718846fb39911) · [状态效果 S-04e0e993f9b84a80](../../evidence/state_effects-sets-001.md#s-04e0e993f9b84a80)

### observed_connections-009489

```text
(config-pm-twamp-delay)# <cr>
```

Handler ` RVA 0x1ACF31D0 `；selector ` 0 `；EOL ` RVA 0x36DD7658 `。

模式根 ` RVA 0x36DC1CF0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。
