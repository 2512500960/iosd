# pm-endpoint-delaymeasurement · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-009692

```text
(config-pm-ep-dm)# default <cr>
```

Handler ` RVA 0x1ACFA820 `；selector ` 0 `；EOL ` RVA 0x36DC2A30 `。

模式根 ` RVA 0x36DC1E08 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-94d7c881fec600fc](../../evidence/state_effects-sets-032.md#s-94d7c881fec600fc)

### observed_connections-009695

```text
(config-pm-ep-dm)# default profile <string> <cr>
```

Handler ` RVA 0x1ACFAA20 `；selector ` 0 `；EOL ` RVA 0x36DC27B0 `。

模式根 ` RVA 0x36DC1E08 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Profile name。

[参数 P-b695e46c7785141e](../../evidence/parameters-sets-014.md#p-b695e46c7785141e) · [状态效果 S-94d7c881fec600fc](../../evidence/state_effects-sets-032.md#s-94d7c881fec600fc)

### observed_connections-009690

```text
(config-pm-ep-dm)# exit <cr>
```

Handler ` RVA 0x1ACF3AA0 `；selector ` 0 `；EOL ` RVA 0x36DE2AC0 `。

模式根 ` RVA 0x36DC1E08 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9adbc2f72e45d227](../../evidence/conditions-sets-060.md#c-9adbc2f72e45d227)

### observed_connections-009691

```text
(config-pm-ep-dm)# no <cr>
```

Handler ` RVA 0x1ACFA820 `；selector ` 0 `；EOL ` RVA 0x36DC2A30 `。

模式根 ` RVA 0x36DC1E08 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-8ee0e331fa5d400b](../../evidence/state_effects-sets-030.md#s-8ee0e331fa5d400b)

### observed_connections-009694

```text
(config-pm-ep-dm)# no profile <string> <cr>
```

Handler ` RVA 0x1ACFAA20 `；selector ` 0 `；EOL ` RVA 0x36DC27B0 `。

模式根 ` RVA 0x36DC1E08 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Profile name。

[参数 P-b695e46c7785141e](../../evidence/parameters-sets-014.md#p-b695e46c7785141e) · [状态效果 S-8ee0e331fa5d400b](../../evidence/state_effects-sets-030.md#s-8ee0e331fa5d400b)

### observed_connections-009693

```text
(config-pm-ep-dm)# profile <string> <cr>
```

Handler ` RVA 0x1ACFAA20 `；selector ` 0 `；EOL ` RVA 0x36DC27B0 `。

模式根 ` RVA 0x36DC1E08 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Profile name。

[参数 P-b695e46c7785141e](../../evidence/parameters-sets-014.md#p-b695e46c7785141e)

### observed_connections-009689

```text
(config-pm-ep-dm)# <cr>
```

Handler ` RVA 0x1ACFA820 `；selector ` 0 `；EOL ` RVA 0x36DC2A30 `。

模式根 ` RVA 0x36DC1E08 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。
