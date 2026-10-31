# pm-interface · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-008958

```text
(config-pm-intf)# default <cr>
```

Handler ` RVA 0x1ACEF2B0 `；selector ` 0 `；EOL ` RVA 0x36DD5DA0 `。

模式根 ` RVA 0x36DC1C50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d1c728283b813ece](../../evidence/conditions-sets-081.md#c-d1c728283b813ece) · [状态效果 S-868f6290b8674820](../../evidence/state_effects-sets-029.md#s-868f6290b8674820)

### observed_connections-008961

```text
(config-pm-intf)# default delay-measurement <cr>
```

Handler ` RVA 0x1ACF29F0 `；selector ` 0 `；EOL ` RVA 0x36DD4DC0 `。

模式根 ` RVA 0x36DC1C50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-868f6290b8674820](../../evidence/state_effects-sets-029.md#s-868f6290b8674820)

### observed_connections-008969

```text
(config-pm-intf)# default delay-measurement advertise-delay <number:0..16777214> <cr>
```

Handler ` RVA 0x1ACF2F90 `；selector ` 0 `；EOL ` RVA 0x36DD4850 `。

模式根 ` RVA 0x36DC1C50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` advertisement delay (uSec)。

[参数 P-b0a8164462c3603d](../../evidence/parameters-sets-013.md#p-b0a8164462c3603d) · [状态效果 S-868f6290b8674820](../../evidence/state_effects-sets-029.md#s-868f6290b8674820)

### observed_connections-008973

```text
(config-pm-intf)# default delay-measurement profile <string> <cr>
```

Handler ` RVA 0x1ACF30B0 `；selector ` 0 `；EOL ` RVA 0x36DD4B40 `。

模式根 ` RVA 0x36DC1C50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Profile Name。

[参数 P-fd8c75268723115c](../../evidence/parameters-sets-019.md#p-fd8c75268723115c) · [状态效果 S-868f6290b8674820](../../evidence/state_effects-sets-029.md#s-868f6290b8674820)

### observed_connections-008963

```text
(config-pm-intf)# default loss-measurement <cr>
```

Handler ` RVA 0x1ACF28B0 `；selector ` 0 `；EOL ` RVA 0x36DD5B20 `。

模式根 ` RVA 0x36DC1C50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-bf5b9af19848000c](../../evidence/conditions-sets-074.md#c-bf5b9af19848000c) · [状态效果 S-868f6290b8674820](../../evidence/state_effects-sets-029.md#s-868f6290b8674820)

### observed_connections-008975

```text
(config-pm-intf)# default loss-measurement profile <string> <cr>
```

Handler ` RVA 0x1ACF2E70 `；selector ` 0 `；EOL ` RVA 0x36DD58A0 `。

模式根 ` RVA 0x36DC1C50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Profile Name。

[条件 C-bf5b9af19848000c](../../evidence/conditions-sets-074.md#c-bf5b9af19848000c) · [参数 P-56e1e875cdc7e3da](../../evidence/parameters-sets-007.md#p-56e1e875cdc7e3da) · [状态效果 S-868f6290b8674820](../../evidence/state_effects-sets-029.md#s-868f6290b8674820)

### observed_connections-008972

```text
(config-pm-intf)# default next-hop ipv4 <address> <cr>
```

Handler ` RVA 0x1ACF4200 `；selector ` 0 `；EOL ` RVA 0x36DD5110 `。

模式根 ` RVA 0x36DC1C50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IPv4 address。

[参数 P-d0bb918d3a98d057](../../evidence/parameters-sets-016.md#p-d0bb918d3a98d057) · [状态效果 S-868f6290b8674820](../../evidence/state_effects-sets-029.md#s-868f6290b8674820)

### observed_connections-008956

```text
(config-pm-intf)# delay-measurement <cr>
```

Handler ` RVA 0x1ACF29F0 `；selector ` 0 `；EOL ` RVA 0x36DD4DC0 `。

模式根 ` RVA 0x36DC1C50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-008964

```text
(config-pm-intf)# delay-measurement advertise-delay <number:0..16777214> <cr>
```

Handler ` RVA 0x1ACF2F90 `；selector ` 0 `；EOL ` RVA 0x36DD4850 `。

模式根 ` RVA 0x36DC1C50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` advertisement delay (uSec)。

[参数 P-b0a8164462c3603d](../../evidence/parameters-sets-013.md#p-b0a8164462c3603d)

### observed_connections-008966

```text
(config-pm-intf)# delay-measurement profile <string> <cr>
```

Handler ` RVA 0x1ACF30B0 `；selector ` 0 `；EOL ` RVA 0x36DD4B40 `。

模式根 ` RVA 0x36DC1C50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Profile Name。

[参数 P-fd8c75268723115c](../../evidence/parameters-sets-019.md#p-fd8c75268723115c)

### observed_connections-008955

```text
(config-pm-intf)# exit <cr>
```

Handler ` RVA 0x1ACF4360 `；selector ` 0 `；EOL ` RVA 0x36DDFE68 `。

模式根 ` RVA 0x36DC1C50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ce72351e725fcf40](../../evidence/conditions-sets-079.md#c-ce72351e725fcf40)

### observed_connections-008959

```text
(config-pm-intf)# loss-measurement <cr>
```

Handler ` RVA 0x1ACF28B0 `；selector ` 0 `；EOL ` RVA 0x36DD5B20 `。

模式根 ` RVA 0x36DC1C50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bf5b9af19848000c](../../evidence/conditions-sets-074.md#c-bf5b9af19848000c)

### observed_connections-008976

```text
(config-pm-intf)# loss-measurement advertise-loss <?fixed_number_action@55558c3294a8> <cr>
```

Handler ` RVA 0x1ACF2C80 `；selector ` 0 `；EOL ` RVA 0x36DD5560 `。

模式根 ` RVA 0x36DC1C50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-bf5b9af19848000c](../../evidence/conditions-sets-074.md#c-bf5b9af19848000c) · [缺口 G-d98b01aaf1fdfd83](../../evidence/gaps-sets-008.md#g-d98b01aaf1fdfd83) · [状态效果 S-022a2d825be81fda](../../evidence/state_effects-sets-001.md#s-022a2d825be81fda)

### observed_connections-008967

```text
(config-pm-intf)# loss-measurement profile <string> <cr>
```

Handler ` RVA 0x1ACF2E70 `；selector ` 0 `；EOL ` RVA 0x36DD58A0 `。

模式根 ` RVA 0x36DC1C50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Profile Name。

[条件 C-bf5b9af19848000c](../../evidence/conditions-sets-074.md#c-bf5b9af19848000c) · [参数 P-56e1e875cdc7e3da](../../evidence/parameters-sets-007.md#p-56e1e875cdc7e3da)

### observed_connections-008965

```text
(config-pm-intf)# next-hop ipv4 <address> <cr>
```

Handler ` RVA 0x1ACF4200 `；selector ` 0 `；EOL ` RVA 0x36DD5110 `。

模式根 ` RVA 0x36DC1C50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IPv4 address。

[参数 P-d0bb918d3a98d057](../../evidence/parameters-sets-016.md#p-d0bb918d3a98d057)

### observed_connections-008957

```text
(config-pm-intf)# no <cr>
```

Handler ` RVA 0x1ACEF2B0 `；selector ` 0 `；EOL ` RVA 0x36DD5DA0 `。

模式根 ` RVA 0x36DC1C50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d1c728283b813ece](../../evidence/conditions-sets-081.md#c-d1c728283b813ece) · [状态效果 S-7a91b56c459d6ca5](../../evidence/state_effects-sets-026.md#s-7a91b56c459d6ca5)

### observed_connections-008960

```text
(config-pm-intf)# no delay-measurement <cr>
```

Handler ` RVA 0x1ACF29F0 `；selector ` 0 `；EOL ` RVA 0x36DD4DC0 `。

模式根 ` RVA 0x36DC1C50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-7a91b56c459d6ca5](../../evidence/state_effects-sets-026.md#s-7a91b56c459d6ca5)

### observed_connections-008968

```text
(config-pm-intf)# no delay-measurement advertise-delay <number:0..16777214> <cr>
```

Handler ` RVA 0x1ACF2F90 `；selector ` 0 `；EOL ` RVA 0x36DD4850 `。

模式根 ` RVA 0x36DC1C50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` advertisement delay (uSec)。

[参数 P-b0a8164462c3603d](../../evidence/parameters-sets-013.md#p-b0a8164462c3603d) · [状态效果 S-7a91b56c459d6ca5](../../evidence/state_effects-sets-026.md#s-7a91b56c459d6ca5)

### observed_connections-008971

```text
(config-pm-intf)# no delay-measurement profile <string> <cr>
```

Handler ` RVA 0x1ACF30B0 `；selector ` 0 `；EOL ` RVA 0x36DD4B40 `。

模式根 ` RVA 0x36DC1C50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Profile Name。

[参数 P-fd8c75268723115c](../../evidence/parameters-sets-019.md#p-fd8c75268723115c) · [状态效果 S-7a91b56c459d6ca5](../../evidence/state_effects-sets-026.md#s-7a91b56c459d6ca5)

### observed_connections-008962

```text
(config-pm-intf)# no loss-measurement <cr>
```

Handler ` RVA 0x1ACF28B0 `；selector ` 0 `；EOL ` RVA 0x36DD5B20 `。

模式根 ` RVA 0x36DC1C50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-bf5b9af19848000c](../../evidence/conditions-sets-074.md#c-bf5b9af19848000c) · [状态效果 S-7a91b56c459d6ca5](../../evidence/state_effects-sets-026.md#s-7a91b56c459d6ca5)

### observed_connections-008974

```text
(config-pm-intf)# no loss-measurement profile <string> <cr>
```

Handler ` RVA 0x1ACF2E70 `；selector ` 0 `；EOL ` RVA 0x36DD58A0 `。

模式根 ` RVA 0x36DC1C50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Profile Name。

[条件 C-bf5b9af19848000c](../../evidence/conditions-sets-074.md#c-bf5b9af19848000c) · [参数 P-56e1e875cdc7e3da](../../evidence/parameters-sets-007.md#p-56e1e875cdc7e3da) · [状态效果 S-7a91b56c459d6ca5](../../evidence/state_effects-sets-026.md#s-7a91b56c459d6ca5)

### observed_connections-008970

```text
(config-pm-intf)# no next-hop ipv4 <address> <cr>
```

Handler ` RVA 0x1ACF4200 `；selector ` 0 `；EOL ` RVA 0x36DD5110 `。

模式根 ` RVA 0x36DC1C50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` IPv4 address。

[参数 P-d0bb918d3a98d057](../../evidence/parameters-sets-016.md#p-d0bb918d3a98d057) · [状态效果 S-7a91b56c459d6ca5](../../evidence/state_effects-sets-026.md#s-7a91b56c459d6ca5)

### observed_connections-008954

```text
(config-pm-intf)# <cr>
```

Handler ` RVA 0x1ACEF2B0 `；selector ` 0 `；EOL ` RVA 0x36DD5DA0 `。

模式根 ` RVA 0x36DC1C50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d1c728283b813ece](../../evidence/conditions-sets-081.md#c-d1c728283b813ece)

