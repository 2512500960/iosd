# pm-loss-profile-intf · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-008284

```text
(config-pm-lm-intf)# advertisement <cr>
```

Handler ` RVA 0x1ACEFAF0 `；selector ` 0 `；EOL ` RVA 0x36DC5670 `。

模式根 ` RVA 0x36DC17C8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-008290

```text
(config-pm-lm-intf)# advertisement anomaly-check <cr>
```

Handler ` RVA 0x1ACEFE40 `；selector ` 0 `；EOL ` RVA 0x36DC5010 `。

模式根 ` RVA 0x36DC17C8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-008317

```text
(config-pm-lm-intf)# advertisement anomaly-check lower-bound <?fixed_number_action@55558c319278> <cr>
```

Handler ` RVA 0x1ACF0FC0 `；selector ` 0 `；EOL ` RVA 0x36DC5340 `。

模式根 ` RVA 0x36DC17C8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-91246437bc3cd7b8](../../evidence/conditions-sets-056.md#c-91246437bc3cd7b8) · [缺口 G-130b4b6e18f5e19b](../../evidence/gaps-sets-001.md#g-130b4b6e18f5e19b) · [状态效果 S-c580c67c997b0624](../../evidence/state_effects-sets-042.md#s-c580c67c997b0624)

### observed_connections-008288

```text
(config-pm-lm-intf)# advertisement periodic <cr>
```

Handler ` RVA 0x1ACEFD90 `；selector ` 0 `；EOL ` RVA 0x36DC4CB8 `。

模式根 ` RVA 0x36DC17C8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-008302

```text
(config-pm-lm-intf)# advertisement periodic interval <number:30..3600> <cr>
```

Handler ` RVA 0x1ACF01C0 `；selector ` 0 `；EOL ` RVA 0x36DC4400 `。

模式根 ` RVA 0x36DC17C8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` interval value in sec。

[参数 P-22673dbf4dd5bf85](../../evidence/parameters-sets-003.md#p-22673dbf4dd5bf85)

### observed_connections-008316

```text
(config-pm-lm-intf)# advertisement periodic minimum-change <?fixed_number_action@55558c3189d0> <cr>
```

Handler ` RVA 0x1ACEFEE0 `；selector ` 0 `；EOL ` RVA 0x36DC4A10 `。

模式根 ` RVA 0x36DC17C8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[缺口 G-a015f8c397cac157](../../evidence/gaps-sets-006.md#g-a015f8c397cac157)

### observed_connections-008315

```text
(config-pm-lm-intf)# advertisement periodic threshold <?fixed_number_action@55558c3186d8> <cr>
```

Handler ` RVA 0x1ACF0050 `；selector ` 0 `；EOL ` RVA 0x36DC4740 `。

模式根 ` RVA 0x36DC17C8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[缺口 G-d23069531a7cddcc](../../evidence/gaps-sets-007.md#g-d23069531a7cddcc)

### observed_connections-008285

```text
(config-pm-lm-intf)# default <cr>
```

Handler ` RVA 0x1ACEF800 `；selector ` 0 `；EOL ` RVA 0x36DC6DA8 `。

模式根 ` RVA 0x36DC17C8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-7b3cfcb494aa334c](../../evidence/state_effects-sets-026.md#s-7b3cfcb494aa334c)

### observed_connections-008289

```text
(config-pm-lm-intf)# default advertisement <cr>
```

Handler ` RVA 0x1ACEFAF0 `；selector ` 0 `；EOL ` RVA 0x36DC5670 `。

模式根 ` RVA 0x36DC17C8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-7b3cfcb494aa334c](../../evidence/state_effects-sets-026.md#s-7b3cfcb494aa334c)

### observed_connections-008298

```text
(config-pm-lm-intf)# default advertisement anomaly-check <cr>
```

Handler ` RVA 0x1ACEFE40 `；selector ` 0 `；EOL ` RVA 0x36DC5010 `。

模式根 ` RVA 0x36DC17C8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-7b3cfcb494aa334c](../../evidence/state_effects-sets-026.md#s-7b3cfcb494aa334c)

### observed_connections-008297

```text
(config-pm-lm-intf)# default advertisement periodic <cr>
```

Handler ` RVA 0x1ACEFD90 `；selector ` 0 `；EOL ` RVA 0x36DC4CB8 `。

模式根 ` RVA 0x36DC17C8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-7b3cfcb494aa334c](../../evidence/state_effects-sets-026.md#s-7b3cfcb494aa334c)

### observed_connections-008309

```text
(config-pm-lm-intf)# default advertisement periodic interval <number:30..3600> <cr>
```

Handler ` RVA 0x1ACF01C0 `；selector ` 0 `；EOL ` RVA 0x36DC4400 `。

模式根 ` RVA 0x36DC17C8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` interval value in sec。

[参数 P-22673dbf4dd5bf85](../../evidence/parameters-sets-003.md#p-22673dbf4dd5bf85) · [状态效果 S-7b3cfcb494aa334c](../../evidence/state_effects-sets-026.md#s-7b3cfcb494aa334c)

### observed_connections-008293

```text
(config-pm-lm-intf)# default probe <cr>
```

Handler ` RVA 0x1ACEFC30 `；selector ` 0 `；EOL ` RVA 0x36DC6B18 `。

模式根 ` RVA 0x36DC17C8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-7b3cfcb494aa334c](../../evidence/state_effects-sets-026.md#s-7b3cfcb494aa334c)

### observed_connections-008301

```text
(config-pm-lm-intf)# default probe color-type <cr>
```

Handler ` RVA 0x1ACF0550 `；selector ` 0 `；EOL ` RVA 0x36DC65A8 `。

模式根 ` RVA 0x36DC17C8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-7b3cfcb494aa334c](../../evidence/state_effects-sets-026.md#s-7b3cfcb494aa334c)

### observed_connections-008312

```text
(config-pm-lm-intf)# default probe color-type dual-color gre <cr>
```

Handler ` RVA 0x1ACF0B20 `；selector ` 0 `；EOL ` RVA 0x36DC6318 `。

模式根 ` RVA 0x36DC17C8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-7b3cfcb494aa334c](../../evidence/state_effects-sets-026.md#s-7b3cfcb494aa334c)

### observed_connections-008307

```text
(config-pm-lm-intf)# default probe color-type single-color <cr>
```

Handler ` RVA 0x1ACF0700 `；selector ` 0 `；EOL ` RVA 0x36DC6030 `。

模式根 ` RVA 0x36DC17C8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-7b3cfcb494aa334c](../../evidence/state_effects-sets-026.md#s-7b3cfcb494aa334c)

### observed_connections-008314

```text
(config-pm-lm-intf)# default probe color-type single-color max-reordering <number:100..2000> <cr>
```

Handler ` RVA 0x1ACF0A10 `；selector ` 0 `；EOL ` RVA 0x36DC5DA8 `。

模式根 ` RVA 0x36DC17C8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` maximum expected reordering value in miliseconds。

[参数 P-59fd1598f3c3c6cd](../../evidence/parameters-sets-007.md#p-59fd1598f3c3c6cd) · [状态效果 S-7b3cfcb494aa334c](../../evidence/state_effects-sets-026.md#s-7b3cfcb494aa334c)

### observed_connections-008305

```text
(config-pm-lm-intf)# default probe tx-interval <number:10..1000> <cr>
```

Handler ` RVA 0x1ACF05F0 `；selector ` 0 `；EOL ` RVA 0x36DC6890 `。

模式根 ` RVA 0x36DC17C8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Transmit interval value in sec。

[参数 P-1741a8166c9b6621](../../evidence/parameters-sets-002.md#p-1741a8166c9b6621) · [状态效果 S-7b3cfcb494aa334c](../../evidence/state_effects-sets-026.md#s-7b3cfcb494aa334c)

### observed_connections-008282

```text
(config-pm-lm-intf)# exit <cr>
```

Handler ` RVA 0x1ACF0C70 `；selector ` 0 `；EOL ` RVA 0x36DD8980 `。

模式根 ` RVA 0x36DC17C8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-72e5e6072228a7e9](../../evidence/conditions-sets-044.md#c-72e5e6072228a7e9)

### observed_connections-008283

```text
(config-pm-lm-intf)# no <cr>
```

Handler ` RVA 0x1ACEF800 `；selector ` 0 `；EOL ` RVA 0x36DC6DA8 `。

模式根 ` RVA 0x36DC17C8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-e0746ea675a8735d](../../evidence/state_effects-sets-048.md#s-e0746ea675a8735d)

### observed_connections-008287

```text
(config-pm-lm-intf)# no advertisement <cr>
```

Handler ` RVA 0x1ACEFAF0 `；selector ` 0 `；EOL ` RVA 0x36DC5670 `。

模式根 ` RVA 0x36DC17C8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-e0746ea675a8735d](../../evidence/state_effects-sets-048.md#s-e0746ea675a8735d)

### observed_connections-008296

```text
(config-pm-lm-intf)# no advertisement anomaly-check <cr>
```

Handler ` RVA 0x1ACEFE40 `；selector ` 0 `；EOL ` RVA 0x36DC5010 `。

模式根 ` RVA 0x36DC17C8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-e0746ea675a8735d](../../evidence/state_effects-sets-048.md#s-e0746ea675a8735d)

### observed_connections-008294

```text
(config-pm-lm-intf)# no advertisement periodic <cr>
```

Handler ` RVA 0x1ACEFD90 `；selector ` 0 `；EOL ` RVA 0x36DC4CB8 `。

模式根 ` RVA 0x36DC17C8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-e0746ea675a8735d](../../evidence/state_effects-sets-048.md#s-e0746ea675a8735d)

### observed_connections-008308

```text
(config-pm-lm-intf)# no advertisement periodic interval <number:30..3600> <cr>
```

Handler ` RVA 0x1ACF01C0 `；selector ` 0 `；EOL ` RVA 0x36DC4400 `。

模式根 ` RVA 0x36DC17C8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` interval value in sec。

[参数 P-22673dbf4dd5bf85](../../evidence/parameters-sets-003.md#p-22673dbf4dd5bf85) · [状态效果 S-e0746ea675a8735d](../../evidence/state_effects-sets-048.md#s-e0746ea675a8735d)

### observed_connections-008291

```text
(config-pm-lm-intf)# no probe <cr>
```

Handler ` RVA 0x1ACEFC30 `；selector ` 0 `；EOL ` RVA 0x36DC6B18 `。

模式根 ` RVA 0x36DC17C8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-e0746ea675a8735d](../../evidence/state_effects-sets-048.md#s-e0746ea675a8735d)

### observed_connections-008299

```text
(config-pm-lm-intf)# no probe color-type <cr>
```

Handler ` RVA 0x1ACF0550 `；selector ` 0 `；EOL ` RVA 0x36DC65A8 `。

模式根 ` RVA 0x36DC17C8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-e0746ea675a8735d](../../evidence/state_effects-sets-048.md#s-e0746ea675a8735d)

### observed_connections-008310

```text
(config-pm-lm-intf)# no probe color-type dual-color gre <cr>
```

Handler ` RVA 0x1ACF0B20 `；selector ` 0 `；EOL ` RVA 0x36DC6318 `。

模式根 ` RVA 0x36DC17C8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-e0746ea675a8735d](../../evidence/state_effects-sets-048.md#s-e0746ea675a8735d)

### observed_connections-008306

```text
(config-pm-lm-intf)# no probe color-type single-color <cr>
```

Handler ` RVA 0x1ACF0700 `；selector ` 0 `；EOL ` RVA 0x36DC6030 `。

模式根 ` RVA 0x36DC17C8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-e0746ea675a8735d](../../evidence/state_effects-sets-048.md#s-e0746ea675a8735d)

### observed_connections-008313

```text
(config-pm-lm-intf)# no probe color-type single-color max-reordering <number:100..2000> <cr>
```

Handler ` RVA 0x1ACF0A10 `；selector ` 0 `；EOL ` RVA 0x36DC5DA8 `。

模式根 ` RVA 0x36DC17C8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` maximum expected reordering value in miliseconds。

[参数 P-59fd1598f3c3c6cd](../../evidence/parameters-sets-007.md#p-59fd1598f3c3c6cd) · [状态效果 S-e0746ea675a8735d](../../evidence/state_effects-sets-048.md#s-e0746ea675a8735d)

### observed_connections-008303

```text
(config-pm-lm-intf)# no probe tx-interval <number:10..1000> <cr>
```

Handler ` RVA 0x1ACF05F0 `；selector ` 0 `；EOL ` RVA 0x36DC6890 `。

模式根 ` RVA 0x36DC17C8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Transmit interval value in sec。

[参数 P-1741a8166c9b6621](../../evidence/parameters-sets-002.md#p-1741a8166c9b6621) · [状态效果 S-e0746ea675a8735d](../../evidence/state_effects-sets-048.md#s-e0746ea675a8735d)

### observed_connections-008286

```text
(config-pm-lm-intf)# probe <cr>
```

Handler ` RVA 0x1ACEFC30 `；selector ` 0 `；EOL ` RVA 0x36DC6B18 `。

模式根 ` RVA 0x36DC17C8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-008292

```text
(config-pm-lm-intf)# probe color-type <cr>
```

Handler ` RVA 0x1ACF0550 `；selector ` 0 `；EOL ` RVA 0x36DC65A8 `。

模式根 ` RVA 0x36DC17C8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-008304

```text
(config-pm-lm-intf)# probe color-type dual-color gre <cr>
```

Handler ` RVA 0x1ACF0B20 `；selector ` 0 `；EOL ` RVA 0x36DC6318 `。

模式根 ` RVA 0x36DC17C8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-008300

```text
(config-pm-lm-intf)# probe color-type single-color <cr>
```

Handler ` RVA 0x1ACF0700 `；selector ` 0 `；EOL ` RVA 0x36DC6030 `。

模式根 ` RVA 0x36DC17C8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-008318

```text
(config-pm-lm-intf)# probe color-type single-color accuracy <?fixed_number_action@55558c319a48> <cr>
```

Handler ` RVA 0x1ACF08C0 `；selector ` 0 `；EOL ` RVA 0x36DC5AB0 `。

模式根 ` RVA 0x36DC17C8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[缺口 G-79e3bbafef882390](../../evidence/gaps-sets-005.md#g-79e3bbafef882390)

### observed_connections-008311

```text
(config-pm-lm-intf)# probe color-type single-color max-reordering <number:100..2000> <cr>
```

Handler ` RVA 0x1ACF0A10 `；selector ` 0 `；EOL ` RVA 0x36DC5DA8 `。

模式根 ` RVA 0x36DC17C8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` maximum expected reordering value in miliseconds。

[参数 P-59fd1598f3c3c6cd](../../evidence/parameters-sets-007.md#p-59fd1598f3c3c6cd)

### observed_connections-008295

```text
(config-pm-lm-intf)# probe tx-interval <number:10..1000> <cr>
```

Handler ` RVA 0x1ACF05F0 `；selector ` 0 `；EOL ` RVA 0x36DC6890 `。

模式根 ` RVA 0x36DC17C8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Transmit interval value in sec。

[参数 P-1741a8166c9b6621](../../evidence/parameters-sets-002.md#p-1741a8166c9b6621)

### observed_connections-008281

```text
(config-pm-lm-intf)# <cr>
```

Handler ` RVA 0x1ACEF800 `；selector ` 0 `；EOL ` RVA 0x36DC6DA8 `。

模式根 ` RVA 0x36DC17C8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

