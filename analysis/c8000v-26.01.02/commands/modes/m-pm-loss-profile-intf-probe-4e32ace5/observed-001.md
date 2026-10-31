# pm-loss-profile-intf-probe · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-009084

```text
(config-pm-lm-intf-probe)# color-type <cr>
```

Handler ` RVA 0x1ACF0550 `；selector ` 0 `；EOL ` RVA 0x36DC65A8 `。

模式根 ` RVA 0x36DC1868 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-009091

```text
(config-pm-lm-intf-probe)# color-type dual-color gre <cr>
```

Handler ` RVA 0x1ACF0B20 `；selector ` 0 `；EOL ` RVA 0x36DC6318 `。

模式根 ` RVA 0x36DC1868 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-009088

```text
(config-pm-lm-intf-probe)# color-type single-color <cr>
```

Handler ` RVA 0x1ACF0700 `；selector ` 0 `；EOL ` RVA 0x36DC6030 `。

模式根 ` RVA 0x36DC1868 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-009100

```text
(config-pm-lm-intf-probe)# color-type single-color accuracy <?fixed_number_action@55558c319a48> <cr>
```

Handler ` RVA 0x1ACF08C0 `；selector ` 0 `；EOL ` RVA 0x36DC5AB0 `。

模式根 ` RVA 0x36DC1868 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[缺口 G-79e3bbafef882390](../../evidence/gaps-sets-005.md#g-79e3bbafef882390)

### observed_connections-009096

```text
(config-pm-lm-intf-probe)# color-type single-color max-reordering <number:100..2000> <cr>
```

Handler ` RVA 0x1ACF0A10 `；selector ` 0 `；EOL ` RVA 0x36DC5DA8 `。

模式根 ` RVA 0x36DC1868 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` maximum expected reordering value in miliseconds。

[参数 P-59fd1598f3c3c6cd](../../evidence/parameters-sets-007.md#p-59fd1598f3c3c6cd)

### observed_connections-009085

```text
(config-pm-lm-intf-probe)# default <cr>
```

Handler ` RVA 0x1ACEFC30 `；selector ` 0 `；EOL ` RVA 0x36DC6B18 `。

模式根 ` RVA 0x36DC1868 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-263a5a1845c1f232](../../evidence/state_effects-sets-009.md#s-263a5a1845c1f232)

### observed_connections-009089

```text
(config-pm-lm-intf-probe)# default color-type <cr>
```

Handler ` RVA 0x1ACF0550 `；selector ` 0 `；EOL ` RVA 0x36DC65A8 `。

模式根 ` RVA 0x36DC1868 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-263a5a1845c1f232](../../evidence/state_effects-sets-009.md#s-263a5a1845c1f232)

### observed_connections-009097

```text
(config-pm-lm-intf-probe)# default color-type dual-color gre <cr>
```

Handler ` RVA 0x1ACF0B20 `；selector ` 0 `；EOL ` RVA 0x36DC6318 `。

模式根 ` RVA 0x36DC1868 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-263a5a1845c1f232](../../evidence/state_effects-sets-009.md#s-263a5a1845c1f232)

### observed_connections-009094

```text
(config-pm-lm-intf-probe)# default color-type single-color <cr>
```

Handler ` RVA 0x1ACF0700 `；selector ` 0 `；EOL ` RVA 0x36DC6030 `。

模式根 ` RVA 0x36DC1868 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-263a5a1845c1f232](../../evidence/state_effects-sets-009.md#s-263a5a1845c1f232)

### observed_connections-009099

```text
(config-pm-lm-intf-probe)# default color-type single-color max-reordering <number:100..2000> <cr>
```

Handler ` RVA 0x1ACF0A10 `；selector ` 0 `；EOL ` RVA 0x36DC5DA8 `。

模式根 ` RVA 0x36DC1868 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` maximum expected reordering value in miliseconds。

[参数 P-59fd1598f3c3c6cd](../../evidence/parameters-sets-007.md#p-59fd1598f3c3c6cd) · [状态效果 S-263a5a1845c1f232](../../evidence/state_effects-sets-009.md#s-263a5a1845c1f232)

### observed_connections-009092

```text
(config-pm-lm-intf-probe)# default tx-interval <number:10..1000> <cr>
```

Handler ` RVA 0x1ACF05F0 `；selector ` 0 `；EOL ` RVA 0x36DC6890 `。

模式根 ` RVA 0x36DC1868 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Transmit interval value in sec。

[参数 P-1741a8166c9b6621](../../evidence/parameters-sets-002.md#p-1741a8166c9b6621) · [状态效果 S-263a5a1845c1f232](../../evidence/state_effects-sets-009.md#s-263a5a1845c1f232)

### observed_connections-009082

```text
(config-pm-lm-intf-probe)# exit <cr>
```

Handler ` RVA 0x1ACF0E70 `；selector ` 0 `；EOL ` RVA 0x36DD99A0 `。

模式根 ` RVA 0x36DC1868 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-377967361d929075](../../evidence/conditions-sets-022.md#c-377967361d929075)

### observed_connections-009083

```text
(config-pm-lm-intf-probe)# no <cr>
```

Handler ` RVA 0x1ACEFC30 `；selector ` 0 `；EOL ` RVA 0x36DC6B18 `。

模式根 ` RVA 0x36DC1868 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-228c1a817a8d57e2](../../evidence/state_effects-sets-008.md#s-228c1a817a8d57e2)

### observed_connections-009087

```text
(config-pm-lm-intf-probe)# no color-type <cr>
```

Handler ` RVA 0x1ACF0550 `；selector ` 0 `；EOL ` RVA 0x36DC65A8 `。

模式根 ` RVA 0x36DC1868 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-228c1a817a8d57e2](../../evidence/state_effects-sets-008.md#s-228c1a817a8d57e2)

### observed_connections-009095

```text
(config-pm-lm-intf-probe)# no color-type dual-color gre <cr>
```

Handler ` RVA 0x1ACF0B20 `；selector ` 0 `；EOL ` RVA 0x36DC6318 `。

模式根 ` RVA 0x36DC1868 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-228c1a817a8d57e2](../../evidence/state_effects-sets-008.md#s-228c1a817a8d57e2)

### observed_connections-009093

```text
(config-pm-lm-intf-probe)# no color-type single-color <cr>
```

Handler ` RVA 0x1ACF0700 `；selector ` 0 `；EOL ` RVA 0x36DC6030 `。

模式根 ` RVA 0x36DC1868 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-228c1a817a8d57e2](../../evidence/state_effects-sets-008.md#s-228c1a817a8d57e2)

### observed_connections-009098

```text
(config-pm-lm-intf-probe)# no color-type single-color max-reordering <number:100..2000> <cr>
```

Handler ` RVA 0x1ACF0A10 `；selector ` 0 `；EOL ` RVA 0x36DC5DA8 `。

模式根 ` RVA 0x36DC1868 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` maximum expected reordering value in miliseconds。

[参数 P-59fd1598f3c3c6cd](../../evidence/parameters-sets-007.md#p-59fd1598f3c3c6cd) · [状态效果 S-228c1a817a8d57e2](../../evidence/state_effects-sets-008.md#s-228c1a817a8d57e2)

### observed_connections-009090

```text
(config-pm-lm-intf-probe)# no tx-interval <number:10..1000> <cr>
```

Handler ` RVA 0x1ACF05F0 `；selector ` 0 `；EOL ` RVA 0x36DC6890 `。

模式根 ` RVA 0x36DC1868 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Transmit interval value in sec。

[参数 P-1741a8166c9b6621](../../evidence/parameters-sets-002.md#p-1741a8166c9b6621) · [状态效果 S-228c1a817a8d57e2](../../evidence/state_effects-sets-008.md#s-228c1a817a8d57e2)

### observed_connections-009086

```text
(config-pm-lm-intf-probe)# tx-interval <number:10..1000> <cr>
```

Handler ` RVA 0x1ACF05F0 `；selector ` 0 `；EOL ` RVA 0x36DC6890 `。

模式根 ` RVA 0x36DC1868 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Transmit interval value in sec。

[参数 P-1741a8166c9b6621](../../evidence/parameters-sets-002.md#p-1741a8166c9b6621)

### observed_connections-009081

```text
(config-pm-lm-intf-probe)# <cr>
```

Handler ` RVA 0x1ACEFC30 `；selector ` 0 `；EOL ` RVA 0x36DC6B18 `。

模式根 ` RVA 0x36DC1868 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

