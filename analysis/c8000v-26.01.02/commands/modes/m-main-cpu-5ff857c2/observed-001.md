# main-cpu · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-009145

```text
(config-r-mc)# default failover timeout <cr>
```

Handler ` RVA 0xD513820 `；selector ` 0 `；EOL ` RVA 0x33E740B0 `。

模式根 ` RVA 0x33E72DF8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-cb4ceb8519ec3eb1](../../evidence/conditions-sets-078.md#c-cb4ceb8519ec3eb1) · [状态效果 S-9f2c499e1d25efa2](../../evidence/state_effects-sets-034.md#s-9f2c499e1d25efa2)

### observed_connections-009144

```text
(config-r-mc)# default secondary aux <cr>
```

Handler ` RVA 0xD513E00 `；selector ` 0 `；EOL ` RVA 0x33E73798 `。

模式根 ` RVA 0x33E72DF8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2868d12c302a345d](../../evidence/conditions-sets-016.md#c-2868d12c302a345d) · [状态效果 S-9f2c499e1d25efa2](../../evidence/state_effects-sets-034.md#s-9f2c499e1d25efa2)

### observed_connections-009148

```text
(config-r-mc)# default secondary console enable <cr>
```

Handler ` RVA 0xD527840 `；selector ` 0 `；EOL ` RVA 0x33E7A040 `。

模式根 ` RVA 0x33E72DF8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-9f2c499e1d25efa2](../../evidence/state_effects-sets-034.md#s-9f2c499e1d25efa2)

### observed_connections-009152

```text
(config-r-mc)# default secondary console lock <cr>
```

Handler ` RVA 0xD527990 `；selector ` 0 `；EOL ` RVA 0x33E7A2F8 `。

模式根 ` RVA 0x33E72DF8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-9f2c499e1d25efa2](../../evidence/state_effects-sets-034.md#s-9f2c499e1d25efa2)

### observed_connections-009149

```text
(config-r-mc)# default standby initialization delay <cr>
```

Handler ` RVA 0xD5277D0 `；selector ` 0 `；EOL ` RVA 0x33E79C68 `。

模式根 ` RVA 0x33E72DF8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ce8a489961cd0d07](../../evidence/conditions-sets-080.md#c-ce8a489961cd0d07) · [状态效果 S-9f2c499e1d25efa2](../../evidence/state_effects-sets-034.md#s-9f2c499e1d25efa2)

### observed_connections-009153

```text
(config-r-mc)# default switchover pxf restart <cr>
```

Handler ` RVA 0xD513970 `；selector ` 0 `；EOL ` RVA 0x33E73CA8 `。

模式根 ` RVA 0x33E72DF8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a1f9218abd65762f](../../evidence/conditions-sets-063.md#c-a1f9218abd65762f) · [状态效果 S-9f2c499e1d25efa2](../../evidence/state_effects-sets-034.md#s-9f2c499e1d25efa2)

### observed_connections-009154

```text
(config-r-mc)# failover timeout <number:dynamic> <cr>
```

Handler ` RVA 0xD513820 `；selector ` 0 `；EOL ` RVA 0x33E740B0 `。

模式根 ` RVA 0x33E72DF8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Timeout &lt;milliseconds&gt; (zero is no timeout)。

[条件 C-6fe842fb125954e8](../../evidence/conditions-sets-043.md#c-6fe842fb125954e8) · [缺口 G-27727504674f1d14](../../evidence/gaps-sets-002.md#g-27727504674f1d14) · [参数 P-ae4ce9bf934b3108](../../evidence/parameters-sets-013.md#p-ae4ce9bf934b3108)

### observed_connections-009143

```text
(config-r-mc)# no failover timeout <cr>
```

Handler ` RVA 0xD513820 `；selector ` 0 `；EOL ` RVA 0x33E740B0 `。

模式根 ` RVA 0x33E72DF8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-489ed1f596fa9b48](../../evidence/conditions-sets-028.md#c-489ed1f596fa9b48) · [状态效果 S-3dc602875966bc96](../../evidence/state_effects-sets-014.md#s-3dc602875966bc96)

### observed_connections-009141

```text
(config-r-mc)# no secondary aux <cr>
```

Handler ` RVA 0xD513E00 `；selector ` 0 `；EOL ` RVA 0x33E73798 `。

模式根 ` RVA 0x33E72DF8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-2868d12c302a345d](../../evidence/conditions-sets-016.md#c-2868d12c302a345d) · [状态效果 S-3dc602875966bc96](../../evidence/state_effects-sets-014.md#s-3dc602875966bc96)

### observed_connections-009146

```text
(config-r-mc)# no secondary console enable <cr>
```

Handler ` RVA 0xD527840 `；selector ` 0 `；EOL ` RVA 0x33E7A040 `。

模式根 ` RVA 0x33E72DF8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-3dc602875966bc96](../../evidence/state_effects-sets-014.md#s-3dc602875966bc96)

### observed_connections-009150

```text
(config-r-mc)# no secondary console lock <cr>
```

Handler ` RVA 0xD527990 `；selector ` 0 `；EOL ` RVA 0x33E7A2F8 `。

模式根 ` RVA 0x33E72DF8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-3dc602875966bc96](../../evidence/state_effects-sets-014.md#s-3dc602875966bc96)

### observed_connections-009147

```text
(config-r-mc)# no standby initialization delay <cr>
```

Handler ` RVA 0xD5277D0 `；selector ` 0 `；EOL ` RVA 0x33E79C68 `。

模式根 ` RVA 0x33E72DF8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ac57efae77d9e2ee](../../evidence/conditions-sets-067.md#c-ac57efae77d9e2ee) · [状态效果 S-3dc602875966bc96](../../evidence/state_effects-sets-014.md#s-3dc602875966bc96)

### observed_connections-009151

```text
(config-r-mc)# no switchover pxf restart <cr>
```

Handler ` RVA 0xD513970 `；selector ` 0 `；EOL ` RVA 0x33E73CA8 `。

模式根 ` RVA 0x33E72DF8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-9d464490db57db07](../../evidence/conditions-sets-061.md#c-9d464490db57db07) · [状态效果 S-3dc602875966bc96](../../evidence/state_effects-sets-014.md#s-3dc602875966bc96)

### observed_connections-009139

```text
(config-r-mc)# secondary aux <cr>
```

Handler ` RVA 0xD513E00 `；selector ` 0 `；EOL ` RVA 0x33E73798 `。

模式根 ` RVA 0x33E72DF8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2868d12c302a345d](../../evidence/conditions-sets-016.md#c-2868d12c302a345d)

### observed_connections-009140

```text
(config-r-mc)# secondary console enable <cr>
```

Handler ` RVA 0xD527840 `；selector ` 0 `；EOL ` RVA 0x33E7A040 `。

模式根 ` RVA 0x33E72DF8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-009142

```text
(config-r-mc)# secondary console lock <cr>
```

Handler ` RVA 0xD527990 `；selector ` 0 `；EOL ` RVA 0x33E7A2F8 `。

模式根 ` RVA 0x33E72DF8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-009155

```text
(config-r-mc)# standby initialization delay <number:dynamic> <cr>
```

Handler ` RVA 0xD5277D0 `；selector ` 0 `；EOL ` RVA 0x33E79C68 `。

模式根 ` RVA 0x33E72DF8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Delay value in seconds。

[条件 C-d5d5f912a4295957](../../evidence/conditions-sets-082.md#c-d5d5f912a4295957) · [缺口 G-74dccae3a471b3a2](../../evidence/gaps-sets-004.md#g-74dccae3a471b3a2) · [参数 P-7662de5ed69dd9a4](../../evidence/parameters-sets-009.md#p-7662de5ed69dd9a4)

### observed_connections-009156

```text
(config-r-mc)# switchover pxf restart <number:dynamic> <number:dynamic> <cr>
```

Handler ` RVA 0xD513970 `；selector ` 0 `；EOL ` RVA 0x33E73CA8 `。

模式根 ` RVA 0x33E72DF8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Number of PXF restarts before a switchover；` unsigned_number_dynamic ` Interval (in hours) over which restart count is accumulated。

[条件 C-3338602186f7c8e7](../../evidence/conditions-sets-020.md#c-3338602186f7c8e7) · [缺口 G-0bd1f4628bbe396c](../../evidence/gaps-sets-001.md#g-0bd1f4628bbe396c) · [参数 P-62b98721f8f221a9](../../evidence/parameters-sets-008.md#p-62b98721f8f221a9) · [状态效果 S-dcde5634427c8054](../../evidence/state_effects-sets-047.md#s-dcde5634427c8054)
