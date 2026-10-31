# pm-twamp-delay-unauth · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-009678

```text
(config-pm-twamp-delay-unauth)# default <cr>
```

Handler ` RVA 0x1ACF3310 `；selector ` 0 `；EOL ` RVA 0x36DD6FB8 `。

模式根 ` RVA 0x36DC1D18 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-d738438698651db7](../../evidence/state_effects-sets-046.md#s-d738438698651db7)

### observed_connections-009681

```text
(config-pm-twamp-delay-unauth)# default querier-dst-port <number:1024..14999> <cr>
```

Handler ` RVA 0x1ACF3BA0 `；selector ` 0 `；EOL ` RVA 0x36DD7308 `。

模式根 ` RVA 0x36DC1D18 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Port number。

[条件 C-d77803c57e1f22d5](../../evidence/conditions-sets-083.md#c-d77803c57e1f22d5) · [参数 P-3c1718846fb39911](../../evidence/parameters-sets-005.md#p-3c1718846fb39911) · [状态效果 S-cf09605c92839cec](../../evidence/state_effects-sets-044.md#s-cf09605c92839cec)

### observed_connections-009676

```text
(config-pm-twamp-delay-unauth)# exit <cr>
```

Handler ` RVA 0x1ACF3E60 `；selector ` 0 `；EOL ` RVA 0x36DE1290 `。

模式根 ` RVA 0x36DC1D18 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-349d7fa6e22c8936](../../evidence/conditions-sets-020.md#c-349d7fa6e22c8936)

### observed_connections-009677

```text
(config-pm-twamp-delay-unauth)# no <cr>
```

Handler ` RVA 0x1ACF3310 `；selector ` 0 `；EOL ` RVA 0x36DD6FB8 `。

模式根 ` RVA 0x36DC1D18 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-ca644efe4288469b](../../evidence/state_effects-sets-043.md#s-ca644efe4288469b)

### observed_connections-009680

```text
(config-pm-twamp-delay-unauth)# no querier-dst-port <number:1024..14999> <cr>
```

Handler ` RVA 0x1ACF3BA0 `；selector ` 0 `；EOL ` RVA 0x36DD7308 `。

模式根 ` RVA 0x36DC1D18 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Port number。

[条件 C-d77803c57e1f22d5](../../evidence/conditions-sets-083.md#c-d77803c57e1f22d5) · [参数 P-3c1718846fb39911](../../evidence/parameters-sets-005.md#p-3c1718846fb39911) · [状态效果 S-8bb163bff656da2f](../../evidence/state_effects-sets-030.md#s-8bb163bff656da2f)

### observed_connections-009679

```text
(config-pm-twamp-delay-unauth)# querier-dst-port <number:1024..14999> <cr>
```

Handler ` RVA 0x1ACF3BA0 `；selector ` 0 `；EOL ` RVA 0x36DD7308 `。

模式根 ` RVA 0x36DC1D18 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Port number。

[条件 C-d77803c57e1f22d5](../../evidence/conditions-sets-083.md#c-d77803c57e1f22d5) · [参数 P-3c1718846fb39911](../../evidence/parameters-sets-005.md#p-3c1718846fb39911) · [状态效果 S-04e0e993f9b84a80](../../evidence/state_effects-sets-001.md#s-04e0e993f9b84a80)

### observed_connections-009675

```text
(config-pm-twamp-delay-unauth)# <cr>
```

Handler ` RVA 0x1ACF3310 `；selector ` 0 `；EOL ` RVA 0x36DD6FB8 `。

模式根 ` RVA 0x36DC1D18 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。
