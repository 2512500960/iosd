# ipv6-router · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-004221

```text
(config-rtr)# address-family ipv6 vrf <string> <cr>
```

Handler ` RVA 0x118AFEA0 `；selector ` 0 `；EOL ` RVA 0x35582C90 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` VPN Routing/Forwarding instance name。

[条件 C-03bc8a76470d925b](../../evidence/conditions-sets-002.md#c-03bc8a76470d925b) · [参数 P-a2e6426a52444881](../../evidence/parameters-sets-012.md#p-a2e6426a52444881) · [状态效果 S-58d102527d98a92e](../../evidence/state_effects-sets-019.md#s-58d102527d98a92e)

### observed_connections-004244

```text
(config-rtr)# adjacency stagger none disable <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 30 `；EOL ` RVA 0x35682C90 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d3301cd4a67feb24](../../evidence/conditions-sets-081.md#c-d3301cd4a67feb24) · [状态效果 S-499756c84e48c340](../../evidence/state_effects-sets-016.md#s-499756c84e48c340)

### observed_connections-004294

```text
(config-rtr)# area <address> <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 10 `；EOL ` RVA 0x35690230 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` OSPF area ID in IP address format。

[条件 C-fde7f797e084e680](../../evidence/conditions-sets-098.md#c-fde7f797e084e680) · [缺口 G-9ec84dd2ca8f2c5f](../../evidence/gaps-sets-006.md#g-9ec84dd2ca8f2c5f) · [参数 P-f232dfa7b78071ba](../../evidence/parameters-sets-018.md#p-f232dfa7b78071ba) · [状态效果 S-28363f7d007b33de](../../evidence/state_effects-sets-009.md#s-28363f7d007b33de)

### observed_connections-004305

```text
(config-rtr)# area <address> authentication key-chain <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 9 `；EOL ` RVA 0x3567D390 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` OSPF area ID in IP address format。

[条件 C-2988bd4ec7178a83](../../evidence/conditions-sets-016.md#c-2988bd4ec7178a83) · [缺口 G-9ec84dd2ca8f2c5f](../../evidence/gaps-sets-006.md#g-9ec84dd2ca8f2c5f) · [参数 P-f232dfa7b78071ba](../../evidence/parameters-sets-018.md#p-f232dfa7b78071ba) · [状态效果 S-e38e2179037df5c0](../../evidence/state_effects-sets-048.md#s-e38e2179037df5c0)

### observed_connections-004297

```text
(config-rtr)# area <address> default-cost <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 7 `；EOL ` RVA 0x3567D770 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` OSPF area ID in IP address format。

[条件 C-6745b168916aff06](../../evidence/conditions-sets-040.md#c-6745b168916aff06) · [缺口 G-9ec84dd2ca8f2c5f](../../evidence/gaps-sets-006.md#g-9ec84dd2ca8f2c5f) · [参数 P-f232dfa7b78071ba](../../evidence/parameters-sets-018.md#p-f232dfa7b78071ba) · [状态效果 S-28363f7d007b33de](../../evidence/state_effects-sets-009.md#s-28363f7d007b33de)

### observed_connections-004312

```text
(config-rtr)# area <address> encryption ipsec spi <number:256..4294967295> <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 8 `；EOL ` RVA 0x3567BF10 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` OSPF area ID in IP address format；` unsigned_number ` SPI。

[条件 C-a4d65f2a78bf0534](../../evidence/conditions-sets-064.md#c-a4d65f2a78bf0534) · [缺口 G-9ec84dd2ca8f2c5f](../../evidence/gaps-sets-006.md#g-9ec84dd2ca8f2c5f) · [参数 P-eefb03881ada0e10](../../evidence/parameters-sets-018.md#p-eefb03881ada0e10) · [状态效果 S-dfa6e1fb7ea61dab](../../evidence/state_effects-sets-047.md#s-dfa6e1fb7ea61dab)

### observed_connections-004313

```text
(config-rtr)# area <address> filter-list prefix <string> in <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 11 `；EOL ` RVA 0x3568FEB0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` OSPF area ID in IP address format；` string ` Name of an IPv6 prefix-list。

[条件 C-787206d34347b415](../../evidence/conditions-sets-047.md#c-787206d34347b415) · [缺口 G-9ec84dd2ca8f2c5f](../../evidence/gaps-sets-006.md#g-9ec84dd2ca8f2c5f) · [参数 P-58698db921e01781](../../evidence/parameters-sets-007.md#p-58698db921e01781) · [状态效果 S-099596d06e789eed](../../evidence/state_effects-sets-002.md#s-099596d06e789eed)

### observed_connections-004303

```text
(config-rtr)# area <address> mpls <cr>
```

Handler ` RVA 0x11BC2300 `；selector ` 13 `；EOL ` RVA 0x35CD9040 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` OSPF area ID in IP address format。

[条件 C-d76f2ad6ff0b1281](../../evidence/conditions-sets-083.md#c-d76f2ad6ff0b1281) · [缺口 G-9ec84dd2ca8f2c5f](../../evidence/gaps-sets-006.md#g-9ec84dd2ca8f2c5f) · [参数 P-f232dfa7b78071ba](../../evidence/parameters-sets-018.md#p-f232dfa7b78071ba) · [状态效果 S-28363f7d007b33de](../../evidence/state_effects-sets-009.md#s-28363f7d007b33de)

### observed_connections-004296

```text
(config-rtr)# area <address> no-transit <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 6 `；EOL ` RVA 0x3567DD10 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` OSPF area ID in IP address format。

[条件 C-33bfc65a49764b25](../../evidence/conditions-sets-020.md#c-33bfc65a49764b25) · [缺口 G-9ec84dd2ca8f2c5f](../../evidence/gaps-sets-006.md#g-9ec84dd2ca8f2c5f) · [参数 P-f232dfa7b78071ba](../../evidence/parameters-sets-018.md#p-f232dfa7b78071ba) · [状态效果 S-447586db1c9275d1](../../evidence/state_effects-sets-015.md#s-447586db1c9275d1)

### observed_connections-004300

```text
(config-rtr)# area <address> normal <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 5 `；EOL ` RVA 0x3567E0D0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` OSPF area ID in IP address format。

[条件 C-0756d675c9fc6105](../../evidence/conditions-sets-003.md#c-0756d675c9fc6105) · [缺口 G-9ec84dd2ca8f2c5f](../../evidence/gaps-sets-006.md#g-9ec84dd2ca8f2c5f) · [参数 P-f232dfa7b78071ba](../../evidence/parameters-sets-018.md#p-f232dfa7b78071ba) · [状态效果 S-28363f7d007b33de](../../evidence/state_effects-sets-009.md#s-28363f7d007b33de)

### observed_connections-004304

```text
(config-rtr)# area <address> nssa <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 3 `；EOL ` RVA 0x3567E9D8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` OSPF area ID in IP address format。

[条件 C-da8fa23073125254](../../evidence/conditions-sets-084.md#c-da8fa23073125254) · [缺口 G-9ec84dd2ca8f2c5f](../../evidence/gaps-sets-006.md#g-9ec84dd2ca8f2c5f) · [参数 P-f232dfa7b78071ba](../../evidence/parameters-sets-018.md#p-f232dfa7b78071ba) · [状态效果 S-28363f7d007b33de](../../evidence/state_effects-sets-009.md#s-28363f7d007b33de)

### observed_connections-004298

```text
(config-rtr)# area <address> packet-size <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 14 `；EOL ` RVA 0x3567DA88 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` OSPF area ID in IP address format。

[条件 C-ffe30655b1fa76e8](../../evidence/conditions-sets-099.md#c-ffe30655b1fa76e8) · [缺口 G-9ec84dd2ca8f2c5f](../../evidence/gaps-sets-006.md#g-9ec84dd2ca8f2c5f) · [参数 P-f232dfa7b78071ba](../../evidence/parameters-sets-018.md#p-f232dfa7b78071ba) · [状态效果 S-28363f7d007b33de](../../evidence/state_effects-sets-009.md#s-28363f7d007b33de)

### observed_connections-004311

```text
(config-rtr)# area <address> sham-link <address> <address> <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 12 `；EOL ` RVA 0x3568F978 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` OSPF area ID in IP address format；` address ` IPv6 address associated with sham-link source；` address ` IPv6 address associated with sham-link destination。

[条件 C-8f6322e6213fb3a3](../../evidence/conditions-sets-056.md#c-8f6322e6213fb3a3) · [缺口 G-9ec84dd2ca8f2c5f](../../evidence/gaps-sets-006.md#g-9ec84dd2ca8f2c5f) · [参数 P-162f7002fd5bb514](../../evidence/parameters-sets-002.md#p-162f7002fd5bb514) · [状态效果 S-28363f7d007b33de](../../evidence/state_effects-sets-009.md#s-28363f7d007b33de)

### observed_connections-004301

```text
(config-rtr)# area <address> stub <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 4 `；EOL ` RVA 0x3567E430 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` OSPF area ID in IP address format。

[条件 C-e4ea43482183fde0](../../evidence/conditions-sets-088.md#c-e4ea43482183fde0) · [缺口 G-9ec84dd2ca8f2c5f](../../evidence/gaps-sets-006.md#g-9ec84dd2ca8f2c5f) · [参数 P-f232dfa7b78071ba](../../evidence/parameters-sets-018.md#p-f232dfa7b78071ba) · [状态效果 S-28363f7d007b33de](../../evidence/state_effects-sets-009.md#s-28363f7d007b33de)

### observed_connections-004307

```text
(config-rtr)# area <address> virtual-link <address> <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 1 `；EOL ` RVA 0x3568EA90 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` OSPF area ID in IP address format；` address ` RouterID associated with virtual link neighbor。

[条件 C-613d9b06f1b79756](../../evidence/conditions-sets-038.md#c-613d9b06f1b79756) · [缺口 G-9ec84dd2ca8f2c5f](../../evidence/gaps-sets-006.md#g-9ec84dd2ca8f2c5f) · [参数 P-ed197afca0a5d6d7](../../evidence/parameters-sets-018.md#p-ed197afca0a5d6d7) · [状态效果 S-28363f7d007b33de](../../evidence/state_effects-sets-009.md#s-28363f7d007b33de)

### observed_connections-004232

```text
(config-rtr)# area <number:0..4294967295> authentication null <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 9 `；EOL ` RVA 0x3567D390 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value。

[条件 C-582f67f8ffc2439b](../../evidence/conditions-sets-035.md#c-582f67f8ffc2439b) · [参数 P-82248a455979973d](../../evidence/parameters-sets-010.md#p-82248a455979973d) · [状态效果 S-7cfe0fd6456b73b5](../../evidence/state_effects-sets-027.md#s-7cfe0fd6456b73b5)

### observed_connections-004226

```text
(config-rtr)# area <number:0..4294967295> default-cost <number:0..16777214> <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 7 `；EOL ` RVA 0x3567D770 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value；` unsigned_number ` Stub's advertised external route metric。

[条件 C-b526f02c57a7caf3](../../evidence/conditions-sets-070.md#c-b526f02c57a7caf3) · [参数 P-0d696e682ec4fdd3](../../evidence/parameters-sets-001.md#p-0d696e682ec4fdd3)

### observed_connections-004277

```text
(config-rtr)# area <number:0..4294967295> filter-list prefix <string> in <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 11 `；EOL ` RVA 0x3568FEB0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value；` string ` Name of an IPv6 prefix-list。

[条件 C-787206d34347b415](../../evidence/conditions-sets-047.md#c-787206d34347b415) · [参数 P-70d47677499df79d](../../evidence/parameters-sets-009.md#p-70d47677499df79d) · [状态效果 S-9c6b80052c73c997](../../evidence/state_effects-sets-033.md#s-9c6b80052c73c997)

### observed_connections-004200

```text
(config-rtr)# area <number:0..4294967295> mpls <cr>
```

Handler ` RVA 0x11BC2300 `；selector ` 13 `；EOL ` RVA 0x35CD9040 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value。

[条件 C-d76f2ad6ff0b1281](../../evidence/conditions-sets-083.md#c-d76f2ad6ff0b1281) · [参数 P-82248a455979973d](../../evidence/parameters-sets-010.md#p-82248a455979973d)

### observed_connections-004314

```text
(config-rtr)# area <number:0..4294967295> mpls traffic-engineering tunnel-tail ipv6 <interface> <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 13 `；EOL ` RVA 0x35CD8C80 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value。

[条件 C-f1c2953b4006fad1](../../evidence/conditions-sets-093.md#c-f1c2953b4006fad1) · [缺口 G-dfcdfd1174df2cfb](../../evidence/gaps-sets-008.md#g-dfcdfd1174df2cfb) · [参数 P-e600dd0718248ad9](../../evidence/parameters-sets-017.md#p-e600dd0718248ad9) · [状态效果 S-5243d665f21f002a](../../evidence/state_effects-sets-018.md#s-5243d665f21f002a)

### observed_connections-004160

```text
(config-rtr)# area <number:0..4294967295> no-transit <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 6 `；EOL ` RVA 0x3567DD10 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value。

[条件 C-33bfc65a49764b25](../../evidence/conditions-sets-020.md#c-33bfc65a49764b25) · [参数 P-82248a455979973d](../../evidence/parameters-sets-010.md#p-82248a455979973d) · [状态效果 S-0a39db95de0ecf43](../../evidence/state_effects-sets-003.md#s-0a39db95de0ecf43)

### observed_connections-004178

```text
(config-rtr)# area <number:0..4294967295> normal <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 5 `；EOL ` RVA 0x3567E0D0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value。

[条件 C-0756d675c9fc6105](../../evidence/conditions-sets-003.md#c-0756d675c9fc6105) · [参数 P-82248a455979973d](../../evidence/parameters-sets-010.md#p-82248a455979973d)

### observed_connections-004202

```text
(config-rtr)# area <number:0..4294967295> nssa <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 3 `；EOL ` RVA 0x3567E9D8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value。

[条件 C-da8fa23073125254](../../evidence/conditions-sets-084.md#c-da8fa23073125254) · [参数 P-82248a455979973d](../../evidence/parameters-sets-010.md#p-82248a455979973d)

### observed_connections-004227

```text
(config-rtr)# area <number:0..4294967295> packet-size <number:576..10000> <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 14 `；EOL ` RVA 0x3567DA88 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value；` unsigned_number ` OSPFV3 Area Mode Packet Size。

[条件 C-25be41a833a7297e](../../evidence/conditions-sets-015.md#c-25be41a833a7297e) · [参数 P-6006ae58436d1dba](../../evidence/parameters-sets-008.md#p-6006ae58436d1dba)

### observed_connections-004263

```text
(config-rtr)# area <number:0..4294967295> range <address> <address> <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 2 `；EOL ` RVA 0x3567F058 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value；` address ` IPv4 address to match；` address ` IPv4 mask for address。

[条件 C-5829a63832813ba0](../../evidence/conditions-sets-035.md#c-5829a63832813ba0) · [参数 P-9bb51a77902c1f8a](../../evidence/parameters-sets-012.md#p-9bb51a77902c1f8a)

### observed_connections-004306

```text
(config-rtr)# area <number:0..4294967295> range <prefix:dynamic> <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 2 `；EOL ` RVA 0x3567F058 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value；` prefix_dynamic ` IPv6 prefix to match。

[条件 C-6652131f9eca7103](../../evidence/conditions-sets-040.md#c-6652131f9eca7103) · [缺口 G-e5466db54e535e0b](../../evidence/gaps-sets-008.md#g-e5466db54e535e0b) · [参数 P-53a24dc2e39151cb](../../evidence/parameters-sets-007.md#p-53a24dc2e39151cb)

### observed_connections-004266

```text
(config-rtr)# area <number:0..4294967295> sham-link <address> <address> <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 12 `；EOL ` RVA 0x3568F978 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value；` address ` IPv6 address associated with sham-link source；` address ` IPv6 address associated with sham-link destination。

[条件 C-8f6322e6213fb3a3](../../evidence/conditions-sets-056.md#c-8f6322e6213fb3a3) · [参数 P-64334b8cba0d93ae](../../evidence/parameters-sets-008.md#p-64334b8cba0d93ae)

### observed_connections-004187

```text
(config-rtr)# area <number:0..4294967295> stub <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 4 `；EOL ` RVA 0x3567E430 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value。

[条件 C-e4ea43482183fde0](../../evidence/conditions-sets-088.md#c-e4ea43482183fde0) · [参数 P-82248a455979973d](../../evidence/parameters-sets-010.md#p-82248a455979973d)

### observed_connections-004250

```text
(config-rtr)# area <number:0..4294967295> virtual-link <address> <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 1 `；EOL ` RVA 0x3568EA90 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value；` address ` RouterID associated with virtual link neighbor。

[条件 C-613d9b06f1b79756](../../evidence/conditions-sets-038.md#c-613d9b06f1b79756) · [参数 P-c0370be301cc44d7](../../evidence/parameters-sets-015.md#p-c0370be301cc44d7)

### observed_connections-004213

```text
(config-rtr)# authentication mode strict <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 31 `；EOL ` RVA 0x356852E0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6093751694b20f29](../../evidence/conditions-sets-038.md#c-6093751694b20f29) · [状态效果 S-0519becdfe8ed933](../../evidence/state_effects-sets-002.md#s-0519becdfe8ed933)

### observed_connections-004030

```text
(config-rtr)# auto-cost <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 0 `；EOL ` RVA 0x35683E20 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1beab640885d026c](../../evidence/conditions-sets-011.md#c-1beab640885d026c)

### observed_connections-004077

```text
(config-rtr)# bfd all-interfaces <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 20 `；EOL ` RVA 0x3567A168 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b37999daad8cb800](../../evidence/conditions-sets-069.md#c-b37999daad8cb800)

### observed_connections-004130

```text
(config-rtr)# capability vrf-lite <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 7 `；EOL ` RVA 0x35684EE8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-24d0b108f11123ba](../../evidence/conditions-sets-014.md#c-24d0b108f11123ba) · [状态效果 S-82b3c85b84af0b13](../../evidence/state_effects-sets-028.md#s-82b3c85b84af0b13)

### observed_connections-004064

```text
(config-rtr)# compatible rfc1583 <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 25 `；EOL ` RVA 0x3567A568 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-725b2f0362370d98](../../evidence/conditions-sets-044.md#c-725b2f0362370d98)

### observed_connections-004068

```text
(config-rtr)# compatible rfc1587 <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 26 `；EOL ` RVA 0x3567A860 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2267723558a951c2](../../evidence/conditions-sets-013.md#c-2267723558a951c2)

### observed_connections-004075

```text
(config-rtr)# compatible rfc5243 <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 27 `；EOL ` RVA 0x3567AB30 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3be5f0f80ef64898](../../evidence/conditions-sets-023.md#c-3be5f0f80ef64898)

### observed_connections-004047

```text
(config-rtr)# context <string> <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 0 `；EOL ` RVA 0x33C44A60 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` SNMP Context Name。

[条件 C-9affa1869574e86e](../../evidence/conditions-sets-060.md#c-9affa1869574e86e) · [参数 P-f3e465802edc027f](../../evidence/parameters-sets-018.md#p-f3e465802edc027f) · [状态效果 S-355a44aeb0ea4c7f](../../evidence/state_effects-sets-012.md#s-355a44aeb0ea4c7f)

### observed_connections-004257

```text
(config-rtr)# default address-family ipv6 vrf <string> <cr>
```

Handler ` RVA 0x118AFEA0 `；selector ` 0 `；EOL ` RVA 0x35582C90 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` VPN Routing/Forwarding instance name。

[条件 C-03bc8a76470d925b](../../evidence/conditions-sets-002.md#c-03bc8a76470d925b) · [参数 P-a2e6426a52444881](../../evidence/parameters-sets-012.md#p-a2e6426a52444881) · [状态效果 S-aef0df20c1a08568](../../evidence/state_effects-sets-037.md#s-aef0df20c1a08568)

### observed_connections-004191

```text
(config-rtr)# default adjacency stagger <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 30 `；EOL ` RVA 0x35682C90 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c77fc90849f00aaf](../../evidence/conditions-sets-077.md#c-c77fc90849f00aaf) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004204

```text
(config-rtr)# default area <number:0..4294967295> <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 10 `；EOL ` RVA 0x35690230 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value。

[条件 C-cbf3a90718ad56af](../../evidence/conditions-sets-078.md#c-cbf3a90718ad56af) · [参数 P-82248a455979973d](../../evidence/parameters-sets-010.md#p-82248a455979973d) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004259

```text
(config-rtr)# default area <number:0..4294967295> authentication key-chain <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 9 `；EOL ` RVA 0x3567D390 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value。

[条件 C-f55d7f15f0784b78](../../evidence/conditions-sets-095.md#c-f55d7f15f0784b78) · [参数 P-82248a455979973d](../../evidence/parameters-sets-010.md#p-82248a455979973d) · [状态效果 S-59505107ab982970](../../evidence/state_effects-sets-019.md#s-59505107ab982970)

### observed_connections-004229

```text
(config-rtr)# default area <number:0..4294967295> default-cost <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 7 `；EOL ` RVA 0x3567D770 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value。

[条件 C-c9cf0e71d3c18af5](../../evidence/conditions-sets-078.md#c-c9cf0e71d3c18af5) · [参数 P-82248a455979973d](../../evidence/parameters-sets-010.md#p-82248a455979973d) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004282

```text
(config-rtr)# default area <number:0..4294967295> encryption ipsec spi <number:256..4294967295> <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 8 `；EOL ` RVA 0x3567BF10 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value；` unsigned_number ` SPI。

[条件 C-eb378abd750ac3cd](../../evidence/conditions-sets-091.md#c-eb378abd750ac3cd) · [参数 P-c5f7d5d1a8c77177](../../evidence/parameters-sets-015.md#p-c5f7d5d1a8c77177) · [状态效果 S-e08a069f2bf85b65](../../evidence/state_effects-sets-048.md#s-e08a069f2bf85b65)

### observed_connections-004284

```text
(config-rtr)# default area <number:0..4294967295> filter-list prefix <string> in <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 11 `；EOL ` RVA 0x3568FEB0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value；` string ` Name of an IPv6 prefix-list。

[条件 C-787206d34347b415](../../evidence/conditions-sets-047.md#c-787206d34347b415) · [参数 P-70d47677499df79d](../../evidence/parameters-sets-009.md#p-70d47677499df79d) · [状态效果 S-86d9294a38924486](../../evidence/state_effects-sets-029.md#s-86d9294a38924486)

### observed_connections-004247

```text
(config-rtr)# default area <number:0..4294967295> mpls <cr>
```

Handler ` RVA 0x11BC2300 `；selector ` 13 `；EOL ` RVA 0x35CD9040 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value。

[条件 C-d76f2ad6ff0b1281](../../evidence/conditions-sets-083.md#c-d76f2ad6ff0b1281) · [参数 P-82248a455979973d](../../evidence/parameters-sets-010.md#p-82248a455979973d) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004228

```text
(config-rtr)# default area <number:0..4294967295> no-transit <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 6 `；EOL ` RVA 0x3567DD10 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value。

[条件 C-33bfc65a49764b25](../../evidence/conditions-sets-020.md#c-33bfc65a49764b25) · [参数 P-82248a455979973d](../../evidence/parameters-sets-010.md#p-82248a455979973d) · [状态效果 S-f508caf1b26bfb66](../../evidence/state_effects-sets-052.md#s-f508caf1b26bfb66)

### observed_connections-004235

```text
(config-rtr)# default area <number:0..4294967295> normal <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 5 `；EOL ` RVA 0x3567E0D0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value。

[条件 C-0756d675c9fc6105](../../evidence/conditions-sets-003.md#c-0756d675c9fc6105) · [参数 P-82248a455979973d](../../evidence/parameters-sets-010.md#p-82248a455979973d) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004248

```text
(config-rtr)# default area <number:0..4294967295> nssa <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 3 `；EOL ` RVA 0x3567E9D8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value。

[条件 C-da8fa23073125254](../../evidence/conditions-sets-084.md#c-da8fa23073125254) · [参数 P-82248a455979973d](../../evidence/parameters-sets-010.md#p-82248a455979973d) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004230

```text
(config-rtr)# default area <number:0..4294967295> packet-size <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 14 `；EOL ` RVA 0x3567DA88 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value。

[条件 C-8b7e330a1076da54](../../evidence/conditions-sets-054.md#c-8b7e330a1076da54) · [参数 P-82248a455979973d](../../evidence/parameters-sets-010.md#p-82248a455979973d) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004276

```text
(config-rtr)# default area <number:0..4294967295> range <address> <address> <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 2 `；EOL ` RVA 0x3567F058 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value；` address ` IPv4 address to match；` address ` IPv4 mask for address。

[条件 C-5829a63832813ba0](../../evidence/conditions-sets-035.md#c-5829a63832813ba0) · [参数 P-9bb51a77902c1f8a](../../evidence/parameters-sets-012.md#p-9bb51a77902c1f8a) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004279

```text
(config-rtr)# default area <number:0..4294967295> sham-link <address> <address> <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 12 `；EOL ` RVA 0x3568F978 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value；` address ` IPv6 address associated with sham-link source；` address ` IPv6 address associated with sham-link destination。

[条件 C-8f6322e6213fb3a3](../../evidence/conditions-sets-056.md#c-8f6322e6213fb3a3) · [参数 P-64334b8cba0d93ae](../../evidence/parameters-sets-008.md#p-64334b8cba0d93ae) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004240

```text
(config-rtr)# default area <number:0..4294967295> stub <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 4 `；EOL ` RVA 0x3567E430 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value。

[条件 C-e4ea43482183fde0](../../evidence/conditions-sets-088.md#c-e4ea43482183fde0) · [参数 P-82248a455979973d](../../evidence/parameters-sets-010.md#p-82248a455979973d) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004268

```text
(config-rtr)# default area <number:0..4294967295> virtual-link <address> <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 1 `；EOL ` RVA 0x3568EA90 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value；` address ` RouterID associated with virtual link neighbor。

[条件 C-613d9b06f1b79756](../../evidence/conditions-sets-038.md#c-613d9b06f1b79756) · [参数 P-c0370be301cc44d7](../../evidence/parameters-sets-015.md#p-c0370be301cc44d7) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004251

```text
(config-rtr)# default authentication mode strict <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 31 `；EOL ` RVA 0x356852E0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6093751694b20f29](../../evidence/conditions-sets-038.md#c-6093751694b20f29) · [状态效果 S-fdb265600aa4cab0](../../evidence/state_effects-sets-054.md#s-fdb265600aa4cab0)

### observed_connections-004119

```text
(config-rtr)# default auto-cost <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 0 `；EOL ` RVA 0x35683E20 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1beab640885d026c](../../evidence/conditions-sets-011.md#c-1beab640885d026c) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004169

```text
(config-rtr)# default bfd all-interfaces <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 20 `；EOL ` RVA 0x3567A168 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b37999daad8cb800](../../evidence/conditions-sets-069.md#c-b37999daad8cb800) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004211

```text
(config-rtr)# default capability vrf-lite <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 7 `；EOL ` RVA 0x35684EE8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-24d0b108f11123ba](../../evidence/conditions-sets-014.md#c-24d0b108f11123ba) · [状态效果 S-442d9319bcbec668](../../evidence/state_effects-sets-015.md#s-442d9319bcbec668)

### observed_connections-004152

```text
(config-rtr)# default compatible rfc1583 <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 25 `；EOL ` RVA 0x3567A568 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-725b2f0362370d98](../../evidence/conditions-sets-044.md#c-725b2f0362370d98) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004156

```text
(config-rtr)# default compatible rfc1587 <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 26 `；EOL ` RVA 0x3567A860 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2267723558a951c2](../../evidence/conditions-sets-013.md#c-2267723558a951c2) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004167

```text
(config-rtr)# default compatible rfc5243 <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 27 `；EOL ` RVA 0x3567AB30 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3be5f0f80ef64898](../../evidence/conditions-sets-023.md#c-3be5f0f80ef64898) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004045

```text
(config-rtr)# default context <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 0 `；EOL ` RVA 0x33C44A60 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ada418e0516d363b](../../evidence/conditions-sets-067.md#c-ada418e0516d363b) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004148

```text
(config-rtr)# default default-information originate <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 6 `；EOL ` RVA 0x3558DDA0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-65a80e3c1b49d01e](../../evidence/conditions-sets-039.md#c-65a80e3c1b49d01e) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004060

```text
(config-rtr)# default default-metric <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 12 `；EOL ` RVA 0x3558D7B0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b33567bf1724b9c6](../../evidence/conditions-sets-069.md#c-b33567bf1724b9c6) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004132

```text
(config-rtr)# default default-metric <cr>
```

Handler ` RVA 0xF5756A0 `；selector ` 45 `；EOL ` RVA 0x35471BE8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8e0f324bf7d10362](../../evidence/conditions-sets-055.md#c-8e0f324bf7d10362) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004197

```text
(config-rtr)# default discard-route external <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 11 `；EOL ` RVA 0x356839B8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-38a7650107b27024](../../evidence/conditions-sets-022.md#c-38a7650107b27024) · [状态效果 S-e276564a687201d8](../../evidence/state_effects-sets-048.md#s-e276564a687201d8)

### observed_connections-004080

```text
(config-rtr)# default distance <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 9 `；EOL ` RVA 0x3558C3B8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0f6638009c40211e](../../evidence/conditions-sets-006.md#c-0f6638009c40211e) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004151

```text
(config-rtr)# default distance eigrp <cr>
```

Handler ` RVA 0xF597490 `；selector ` 47 `；EOL ` RVA 0x3546BC50 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-fc4f19cb8b303d88](../../evidence/conditions-sets-097.md#c-fc4f19cb8b303d88) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004192

```text
(config-rtr)# default distance ospf <cr>
```

Handler ` RVA 0x11BCBF10 `；selector ` 0 `；EOL ` RVA 0x35681AC8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-382b5585a4d9475b](../../evidence/conditions-sets-022.md#c-382b5585a4d9475b) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004261

```text
(config-rtr)# default distribute-list prefix-list <string> in <cr>
```

Handler ` RVA 0x112E3690 `；selector ` 29 `；EOL ` RVA 0x3546D4B0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Prefix-list name。

[条件 C-26c4871ffb253cda](../../evidence/conditions-sets-015.md#c-26c4871ffb253cda) · [参数 P-314b4f47fed4f4b0](../../evidence/parameters-sets-004.md#p-314b4f47fed4f4b0) · [状态效果 S-5fb373148f3fca80](../../evidence/state_effects-sets-021.md#s-5fb373148f3fca80)

### observed_connections-004256

```text
(config-rtr)# default distribute-list route-map <string> in <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 14 `；EOL ` RVA 0x3558ECE0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Route-map name。

[条件 C-8775aaf0fcbe5920](../../evidence/conditions-sets-052.md#c-8775aaf0fcbe5920) · [参数 P-95e3798261a43d6d](../../evidence/parameters-sets-012.md#p-95e3798261a43d6d) · [状态效果 S-46e4d3323239e172](../../evidence/state_effects-sets-016.md#s-46e4d3323239e172)

### observed_connections-004067

```text
(config-rtr)# default domain-id <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 9 `；EOL ` RVA 0x35678E68 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f549a2adfee30eeb](../../evidence/conditions-sets-095.md#c-f549a2adfee30eeb) · [状态效果 S-eda78b8862c472ab](../../evidence/state_effects-sets-050.md#s-eda78b8862c472ab)

### observed_connections-004209

```text
(config-rtr)# default eigrp graceful-restart <cr>
```

Handler ` RVA 0xF57EE00 `；selector ` 10 `；EOL ` RVA 0x3546FBC0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3fb2e4309e6a2868](../../evidence/conditions-sets-025.md#c-3fb2e4309e6a2868) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004253

```text
(config-rtr)# default eigrp upgrade-cli <string> <cr>
```

Handler ` RVA 0xF5807E0 `；selector ` 142 `；EOL ` RVA 0x354700A0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` EIGRP Virtual-Instance Name。

[条件 C-b20dc967e98a70fe](../../evidence/conditions-sets-069.md#c-b20dc967e98a70fe) · [参数 P-a86103facdcb1297](../../evidence/parameters-sets-013.md#p-a86103facdcb1297) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004117

```text
(config-rtr)# default event-log <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 19 `；EOL ` RVA 0x35683198 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-490803c624d0035c](../../evidence/conditions-sets-029.md#c-490803c624d0035c) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004121

```text
(config-rtr)# default event-log-size <cr>
```

Handler ` RVA 0xF596700 `；selector ` 35 `；EOL ` RVA 0x3546F7E8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-eb541564a8c8a83e](../../evidence/conditions-sets-091.md#c-eb541564a8c8a83e) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004114

```text
(config-rtr)# default event-logging <cr>
```

Handler ` RVA 0xF596700 `；selector ` 36 `；EOL ` RVA 0x3546F4A8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1ea4acfddc3eabec](../../evidence/conditions-sets-012.md#c-1ea4acfddc3eabec) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004143

```text
(config-rtr)# default graceful-restart <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 22 `；EOL ` RVA 0x3569DA70 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-94abebb1e1370965](../../evidence/conditions-sets-057.md#c-94abebb1e1370965) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004219

```text
(config-rtr)# default graceful-restart helper <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 23 `；EOL ` RVA 0x3569DDF8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4feff3abfdec660b](../../evidence/conditions-sets-031.md#c-4feff3abfdec660b) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004237

```text
(config-rtr)# default ignore lsa mospf <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 4 `；EOL ` RVA 0x356828B0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1beab640885d026c](../../evidence/conditions-sets-011.md#c-1beab640885d026c) · [状态效果 S-262cf9faad97b02a](../../evidence/state_effects-sets-009.md#s-262cf9faad97b02a)

### observed_connections-004165

```text
(config-rtr)# default interface-id snmp-if-index <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 15 `；EOL ` RVA 0x3567AEC8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1beab640885d026c](../../evidence/conditions-sets-011.md#c-1beab640885d026c) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004093

```text
(config-rtr)# default kill-everyone <cr>
```

Handler ` RVA 0xF57B0C0 `；selector ` 15 `；EOL ` RVA 0x3546E750 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1ea4acfddc3eabec](../../evidence/conditions-sets-012.md#c-1ea4acfddc3eabec) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004215

```text
(config-rtr)# default limit retransmissions <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 14 `；EOL ` RVA 0x35684B60 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f7c09dde851bc86e](../../evidence/conditions-sets-096.md#c-f7c09dde851bc86e) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004140

```text
(config-rtr)# default local-rib-criteria <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 6 `；EOL ` RVA 0x35685D58 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7c77db41462fef9d](../../evidence/conditions-sets-048.md#c-7c77db41462fef9d) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004108

```text
(config-rtr)# default log-adjacency-changes <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 3 `；EOL ` RVA 0x35683638 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1beab640885d026c](../../evidence/conditions-sets-011.md#c-1beab640885d026c) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004115

```text
(config-rtr)# default log-event-type <cr>
```

Handler ` RVA 0xF596700 `；selector ` 34 `；EOL ` RVA 0x3546F0C0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-06f2a499a4ee7651](../../evidence/conditions-sets-003.md#c-06f2a499a4ee7651) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004098

```text
(config-rtr)# default log-neighbor-changes <cr>
```

Handler ` RVA 0xF57B3F0 `；selector ` 16 `；EOL ` RVA 0x3546EA30 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1ea4acfddc3eabec](../../evidence/conditions-sets-012.md#c-1ea4acfddc3eabec) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004109

```text
(config-rtr)# default log-neighbor-warnings <cr>
```

Handler ` RVA 0xF57B570 `；selector ` 17 `；EOL ` RVA 0x3546ED70 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-dd349bc91ee3aba8](../../evidence/conditions-sets-085.md#c-dd349bc91ee3aba8) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004124

```text
(config-rtr)# default max-lsa <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 1 `；EOL ` RVA 0x356841E0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-48ee12b6961fb879](../../evidence/conditions-sets-029.md#c-48ee12b6961fb879) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004054

```text
(config-rtr)# default max-metric <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 13 `；EOL ` RVA 0x35679438 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-fffb0405b4e655ad](../../evidence/conditions-sets-099.md#c-fffb0405b4e655ad) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004053

```text
(config-rtr)# default max-metric intra-area <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 8 `；EOL ` RVA 0x35679358 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-19aed9c37a34ce89](../../evidence/conditions-sets-010.md#c-19aed9c37a34ce89) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004061

```text
(config-rtr)# default maximum-paths <cr>
```

Handler ` RVA 0xF5985F0 `；selector ` 37 `；EOL ` RVA 0x3546C008 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8d9d31f58144533a](../../evidence/conditions-sets-055.md#c-8d9d31f58144533a) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004099

```text
(config-rtr)# default maximum-paths <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 8 `；EOL ` RVA 0x3558C990 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5e7aee77ddefdc78](../../evidence/conditions-sets-037.md#c-5e7aee77ddefdc78) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004186

```text
(config-rtr)# default maximum-paths per-prefix-distribution <cr>
```

Handler ` RVA 0x11BCC820 `；selector ` 0 `；EOL ` RVA 0x35682000 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-669f90cfb55384be](../../evidence/conditions-sets-040.md#c-669f90cfb55384be) · [状态效果 S-4318e84240248ef0](../../evidence/state_effects-sets-015.md#s-4318e84240248ef0)

### observed_connections-004161

```text
(config-rtr)# default metric maximum-hops <cr>
```

Handler ` RVA 0xF57D6C0 `；selector ` 31 `；EOL ` RVA 0x3546C6A0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4158e26337136060](../../evidence/conditions-sets-026.md#c-4158e26337136060) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004170

```text
(config-rtr)# default metric weights <cr>
```

Handler ` RVA 0xF57D6C0 `；selector ` 12 `；EOL ` RVA 0x3546C9C8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-bba88989c29c8965](../../evidence/conditions-sets-072.md#c-bba88989c29c8965) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004048

```text
(config-rtr)# default omp-route-tag <cr>
```

Handler ` RVA 0x118A4750 `；selector ` 0 `；EOL ` RVA 0x3557A0F8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-837421aa0ded5ba7](../../evidence/conditions-sets-051.md#c-837421aa0ded5ba7) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004034

```text
(config-rtr)# default packet-size <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 41 `；EOL ` RVA 0x356856A8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-629f8f30b8f22fc1](../../evidence/conditions-sets-038.md#c-629f8f30b8f22fc1) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004166

```text
(config-rtr)# default passive-interface default <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 11 `；EOL ` RVA 0x3558CF78 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0049d72fe609511d](../../evidence/conditions-sets-001.md#c-0049d72fe609511d) · [状态效果 S-b768b1004f321fdc](../../evidence/state_effects-sets-039.md#s-b768b1004f321fdc)

### observed_connections-004181

```text
(config-rtr)# default passive-interface default <cr>
```

Handler ` RVA 0xF58B500 `；selector ` 132 `；EOL ` RVA 0x3546D9A0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ec9b4d713a4e3235](../../evidence/conditions-sets-091.md#c-ec9b4d713a4e3235) · [状态效果 S-43ac0f1eaf08fefd](../../evidence/state_effects-sets-015.md#s-43ac0f1eaf08fefd)

### observed_connections-004052

```text
(config-rtr)# default poison-reverse <cr>
```

Handler ` RVA 0x118A3D80 `；selector ` 0 `；EOL ` RVA 0x3557A3A0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-837421aa0ded5ba7](../../evidence/conditions-sets-051.md#c-837421aa0ded5ba7) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004079

```text
(config-rtr)# default port <cr>
```

Handler ` RVA 0x118A6E70 `；selector ` 0 `；EOL ` RVA 0x3557A718 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0624db314bcbdd70](../../evidence/conditions-sets-003.md#c-0624db314bcbdd70) · [状态效果 S-67e64cf2be27d036](../../evidence/state_effects-sets-022.md#s-67e64cf2be27d036)

### observed_connections-004071

```text
(config-rtr)# default prefix-suppression <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 28 `；EOL ` RVA 0x35679D18 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6a3e394242acd8c5](../../evidence/conditions-sets-041.md#c-6a3e394242acd8c5) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004136

```text
(config-rtr)# default process-min-time percent <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 16 `；EOL ` RVA 0x35686420 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-128da7de5515f0ce](../../evidence/conditions-sets-007.md#c-128da7de5515f0ce) · [状态效果 S-0f463b67e47e9527](../../evidence/state_effects-sets-004.md#s-0f463b67e47e9527)

### observed_connections-004173

```text
(config-rtr)# default queue-depth hello <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 18 `；EOL ` RVA 0x3567B298 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-98f787e9a034b54a](../../evidence/conditions-sets-059.md#c-98f787e9a034b54a) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004179

```text
(config-rtr)# default queue-depth update <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 17 `；EOL ` RVA 0x3567B620 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1060de1fb05d5454](../../evidence/conditions-sets-006.md#c-1060de1fb05d5454) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004185

```text
(config-rtr)# default redistribute maximum-prefix <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 5 `；EOL ` RVA 0x3558AB28 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ab1843c976c5c8da](../../evidence/conditions-sets-066.md#c-ab1843c976c5c8da) · [状态效果 S-329d26d044af3ca2](../../evidence/state_effects-sets-011.md#s-329d26d044af3ca2)

### observed_connections-004212

```text
(config-rtr)# default redistribute maximum-prefix <cr>
```

Handler ` RVA 0xF598EF0 `；selector ` 33 `；EOL ` RVA 0x35470818 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1a65b762fd6d8a46](../../evidence/conditions-sets-010.md#c-1a65b762fd6d8a46) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004046

```text
(config-rtr)# default router-id <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 12 `；EOL ` RVA 0x356789A8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a26938f3455768a2](../../evidence/conditions-sets-063.md#c-a26938f3455768a2) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004088

```text
(config-rtr)# default router-id <cr>
```

Handler ` RVA 0xF57EB20 `；selector ` 5 `；EOL ` RVA 0x3546DD90 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f4112892e904b173](../../evidence/conditions-sets-094.md#c-f4112892e904b173) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004059

```text
(config-rtr)# default shutdown <cr>
```

Handler ` RVA 0xF57D580 `；selector ` 6 `；EOL ` RVA 0x3546C2F8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1ea4acfddc3eabec](../../evidence/conditions-sets-012.md#c-1ea4acfddc3eabec) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004139

```text
(config-rtr)# default shutdown <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 29 `；EOL ` RVA 0x35686118 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9e59e89df3c539ff](../../evidence/conditions-sets-061.md#c-9e59e89df3c539ff) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004171

```text
(config-rtr)# default snmp context <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 0 `；EOL ` RVA 0x33C455F0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7598dc8aeb3669dc](../../evidence/conditions-sets-046.md#c-7598dc8aeb3669dc) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004273

```text
(config-rtr)# default snmp context <string> community <string> <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 2 `；EOL ` RVA 0x33C45118 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Context Name；` string ` SNMP community string。

[条件 C-2573c969c66067b6](../../evidence/conditions-sets-015.md#c-2573c969c66067b6) · [参数 P-9b6eb89831feec60](../../evidence/parameters-sets-012.md#p-9b6eb89831feec60) · [状态效果 S-93414928ecb4b635](../../evidence/state_effects-sets-031.md#s-93414928ecb4b635)

### observed_connections-004272

```text
(config-rtr)# default snmp context <string> user <string> <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 23 `；EOL ` RVA 0x33C456D0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Context Name；` string ` Name of the user。

[条件 C-67e2e80e2c1c144d](../../evidence/conditions-sets-040.md#c-67e2e80e2c1c144d) · [参数 P-cfc42ec8ad667e32](../../evidence/parameters-sets-016.md#p-cfc42ec8ad667e32) · [状态效果 S-ed1acde695aa9906](../../evidence/state_effects-sets-050.md#s-ed1acde695aa9906)

### observed_connections-004043

```text
(config-rtr)# default split-horizon <cr>
```

Handler ` RVA 0x118A4250 `；selector ` 0 `；EOL ` RVA 0x35579E50 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-837421aa0ded5ba7](../../evidence/conditions-sets-051.md#c-837421aa0ded5ba7) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004210

```text
(config-rtr)# default statistics rib-timings <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 5 `；EOL ` RVA 0x356856E8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7c77db41462fef9d](../../evidence/conditions-sets-048.md#c-7c77db41462fef9d) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004095

```text
(config-rtr)# default stub <cr>
```

Handler ` RVA 0xF57E6E0 `；selector ` 18 `；EOL ` RVA 0x3546E0D8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-575478227e3680c1](../../evidence/conditions-sets-034.md#c-575478227e3680c1) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004065

```text
(config-rtr)# default table-map <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 17 `；EOL ` RVA 0x3558D3B0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e4e4faf6de502909](../../evidence/conditions-sets-088.md#c-e4e4faf6de502909) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004090

```text
(config-rtr)# default timers <cr>
```

Handler ` RVA 0x118A33B0 `；selector ` 0 `；EOL ` RVA 0x3557AB28 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c52ff0c82b451ec0](../../evidence/conditions-sets-076.md#c-c52ff0c82b451ec0) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004146

```text
(config-rtr)# default timers active-time <cr>
```

Handler ` RVA 0xF597780 `；selector ` 28 `；EOL ` RVA 0x3546B820 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0a3d300e5b2e01ef](../../evidence/conditions-sets-004.md#c-0a3d300e5b2e01ef) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004182

```text
(config-rtr)# default timers lsa arrival <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 39 `；EOL ` RVA 0x3567FC98 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-fa3c9c9a155c6696](../../evidence/conditions-sets-097.md#c-fa3c9c9a155c6696) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004104

```text
(config-rtr)# default timers lsa-arrival <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 34 `；EOL ` RVA 0x35680250 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f6abd2ba10b3ee5b](../../evidence/conditions-sets-095.md#c-f6abd2ba10b3ee5b) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004096

```text
(config-rtr)# default timers lsa-group-pacing <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 35 `；EOL ` RVA 0x3567FCC0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8cc6f17d7cfd2fde](../../evidence/conditions-sets-055.md#c-8cc6f17d7cfd2fde) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004105

```text
(config-rtr)# default timers lsa-interval <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 33 `；EOL ` RVA 0x35680228 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-fdf14c4c0d709423](../../evidence/conditions-sets-098.md#c-fdf14c4c0d709423) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004198

```text
(config-rtr)# default timers pacing flood <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 36 `；EOL ` RVA 0x356807F8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-df302bc5d4447d72](../../evidence/conditions-sets-086.md#c-df302bc5d4447d72) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004194

```text
(config-rtr)# default timers pacing lsa-group <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 35 `；EOL ` RVA 0x356807B8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1926387444d56df5](../../evidence/conditions-sets-010.md#c-1926387444d56df5) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004201

```text
(config-rtr)# default timers pacing retransmission <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 37 `；EOL ` RVA 0x35680A98 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0f438fe87bf7ce34](../../evidence/conditions-sets-006.md#c-0f438fe87bf7ce34) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004243

```text
(config-rtr)# default timers throttle lsa <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 40 `；EOL ` RVA 0x3567F968 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e5c6ba147c2f8116](../../evidence/conditions-sets-089.md#c-e5c6ba147c2f8116) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004241

```text
(config-rtr)# default timers throttle spf <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 38 `；EOL ` RVA 0x3567F5B0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-699192e91e40676c](../../evidence/conditions-sets-041.md#c-699192e91e40676c) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004128

```text
(config-rtr)# default variance <cr>
```

Handler ` RVA 0xF575390 `；selector ` 39 `；EOL ` RVA 0x35470460 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-90d4898bdbebeb42](../../evidence/conditions-sets-056.md#c-90d4898bdbebeb42) · [状态效果 S-5288bc92d27d8c06](../../evidence/state_effects-sets-018.md#s-5288bc92d27d8c06)

### observed_connections-004056

```text
(config-rtr)# default-information originate <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 6 `；EOL ` RVA 0x3558DDA0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-65a80e3c1b49d01e](../../evidence/conditions-sets-039.md#c-65a80e3c1b49d01e)

### observed_connections-004069

```text
(config-rtr)# default-metric <number:1..16777214> <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 12 `；EOL ` RVA 0x3558D7B0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Default metric。

[条件 C-bd1f77edc3a18da5](../../evidence/conditions-sets-073.md#c-bd1f77edc3a18da5) · [参数 P-4f618901e2460df2](../../evidence/parameters-sets-007.md#p-4f618901e2460df2)

### observed_connections-004280

```text
(config-rtr)# default-metric <number:1..4294967295> <number:0..4294967295> <number:0..255> <number:1..255> <number:1..65535> <cr>
```

Handler ` RVA 0xF5756A0 `；selector ` 45 `；EOL ` RVA 0x35471BE8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Bandwidth in Kbits per second；` unsigned_number ` delay metric in 10 microsecond units；` unsigned_number ` Reliability metric where 255 is 100% reliable；` unsigned_number ` Effective bandwidth metric (Loading) where 255 is 100% loaded；` unsigned_number ` Maximum Transmission Unit metric of the path 。

[条件 C-8b99d2b97f31487f](../../evidence/conditions-sets-054.md#c-8b99d2b97f31487f) · [参数 P-06dd52532ffa5dd6](../../evidence/parameters-sets-001.md#p-06dd52532ffa5dd6)

### observed_connections-004112

```text
(config-rtr)# discard-route external <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 11 `；EOL ` RVA 0x356839B8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-38a7650107b27024](../../evidence/conditions-sets-022.md#c-38a7650107b27024) · [状态效果 S-4887664dc98221c2](../../evidence/state_effects-sets-016.md#s-4887664dc98221c2)

### observed_connections-004019

```text
(config-rtr)# distance <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 9 `；EOL ` RVA 0x3558C3B8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0f6638009c40211e](../../evidence/conditions-sets-006.md#c-0f6638009c40211e)

### observed_connections-004302

```text
(config-rtr)# distance <number:1..254> <prefix:dynamic> <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 9 `；EOL ` RVA 0x3558C3B8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Administrative distance；` prefix_dynamic ` Prefix to match source address。

[条件 C-aaab3b0f22cedc9c](../../evidence/conditions-sets-066.md#c-aaab3b0f22cedc9c) · [缺口 G-ab8058deebcb0752](../../evidence/gaps-sets-006.md#g-ab8058deebcb0752) · [参数 P-13bd2f50496219dd](../../evidence/parameters-sets-002.md#p-13bd2f50496219dd) · [状态效果 S-ac220070234d17ba](../../evidence/state_effects-sets-036.md#s-ac220070234d17ba)

### observed_connections-004222

```text
(config-rtr)# distance eigrp <number:1..255> <number:1..255> <cr>
```

Handler ` RVA 0xF597490 `；selector ` 47 `；EOL ` RVA 0x3546BC50 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Distance for internal routes；` unsigned_number ` Distance for external routes。

[条件 C-7aa006081ddcc377](../../evidence/conditions-sets-048.md#c-7aa006081ddcc377) · [参数 P-0e11c7242a020992](../../evidence/parameters-sets-002.md#p-0e11c7242a020992)

### observed_connections-004123

```text
(config-rtr)# distance ospf <cr>
```

Handler ` RVA 0x11BCBF10 `；selector ` 0 `；EOL ` RVA 0x35681AC8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-01d49310d1fd4685](../../evidence/conditions-sets-001.md#c-01d49310d1fd4685)

### observed_connections-004236

```text
(config-rtr)# distribute-list prefix-list <string> in <cr>
```

Handler ` RVA 0x112E3690 `；selector ` 29 `；EOL ` RVA 0x3546D4B0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Prefix-list name。

[条件 C-26c4871ffb253cda](../../evidence/conditions-sets-015.md#c-26c4871ffb253cda) · [参数 P-314b4f47fed4f4b0](../../evidence/parameters-sets-004.md#p-314b4f47fed4f4b0) · [状态效果 S-36b13799e5f19889](../../evidence/state_effects-sets-012.md#s-36b13799e5f19889)

### observed_connections-004310

```text
(config-rtr)# distribute-list prefix-list <string> in <interface> <cr>
```

Handler ` RVA 0x112E3690 `；selector ` 29 `；EOL ` RVA 0x3546D4B0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Prefix-list name。

[条件 C-dd1dbf3324e7f3d2](../../evidence/conditions-sets-085.md#c-dd1dbf3324e7f3d2) · [缺口 G-585f8a3b154d0acd](../../evidence/gaps-sets-004.md#g-585f8a3b154d0acd) · [参数 P-0c9c6f81abac52f6](../../evidence/parameters-sets-001.md#p-0c9c6f81abac52f6) · [状态效果 S-ea2b193be7632431](../../evidence/state_effects-sets-050.md#s-ea2b193be7632431)

### observed_connections-004220

```text
(config-rtr)# distribute-list route-map <string> in <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 14 `；EOL ` RVA 0x3558ECE0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Route-map name。

[条件 C-8775aaf0fcbe5920](../../evidence/conditions-sets-052.md#c-8775aaf0fcbe5920) · [参数 P-95e3798261a43d6d](../../evidence/parameters-sets-012.md#p-95e3798261a43d6d) · [状态效果 S-405f7a5d17b763e5](../../evidence/state_effects-sets-014.md#s-405f7a5d17b763e5)

### observed_connections-004309

```text
(config-rtr)# distribute-list route-map <string> in <interface> <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 14 `；EOL ` RVA 0x3558ECE0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Route-map name。

[条件 C-ba1d0474a591feaf](../../evidence/conditions-sets-072.md#c-ba1d0474a591feaf) · [缺口 G-da0cd930bc871cca](../../evidence/gaps-sets-008.md#g-da0cd930bc871cca) · [参数 P-24f10f5824c80380](../../evidence/parameters-sets-003.md#p-24f10f5824c80380) · [状态效果 S-c936f988440644e6](../../evidence/state_effects-sets-043.md#s-c936f988440644e6)

### observed_connections-004308

```text
(config-rtr)# domain-id type 0005 value <hex-string> <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 9 `；EOL ` RVA 0x35678E68 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` hexstring ` Six octet Domain ID extended community value in hexadecimal。

[条件 C-03060dd3cccb668d](../../evidence/conditions-sets-002.md#c-03060dd3cccb668d) · [缺口 G-a46774963ffad617](../../evidence/gaps-sets-006.md#g-a46774963ffad617) · [参数 P-d3ec18ef982ee658](../../evidence/parameters-sets-016.md#p-d3ec18ef982ee658) · [状态效果 S-8bc73413896b12c0](../../evidence/state_effects-sets-030.md#s-8bc73413896b12c0)

### observed_connections-004127

```text
(config-rtr)# eigrp graceful-restart <cr>
```

Handler ` RVA 0xF57EE00 `；selector ` 10 `；EOL ` RVA 0x3546FBC0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bd56bbf3c3972ffc](../../evidence/conditions-sets-073.md#c-bd56bbf3c3972ffc)

### observed_connections-004216

```text
(config-rtr)# eigrp upgrade-cli <string> <cr>
```

Handler ` RVA 0xF5807E0 `；selector ` 142 `；EOL ` RVA 0x354700A0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` EIGRP Virtual-Instance Name。

[条件 C-b20dc967e98a70fe](../../evidence/conditions-sets-069.md#c-b20dc967e98a70fe) · [参数 P-a86103facdcb1297](../../evidence/parameters-sets-013.md#p-a86103facdcb1297)

### observed_connections-004029

```text
(config-rtr)# event-log <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 19 `；EOL ` RVA 0x35683198 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-490803c624d0035c](../../evidence/conditions-sets-029.md#c-490803c624d0035c)

### observed_connections-004293

```text
(config-rtr)# event-log-size <number:dynamic> <cr>
```

Handler ` RVA 0xF596700 `；selector ` 35 `；EOL ` RVA 0x3546F7E8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Max event log entries。

[条件 C-69f5f98624832851](../../evidence/conditions-sets-041.md#c-69f5f98624832851) · [缺口 G-db0410c024ab1dd7](../../evidence/gaps-sets-008.md#g-db0410c024ab1dd7) · [参数 P-b2d96bdd7a7ad5c5](../../evidence/parameters-sets-014.md#p-b2d96bdd7a7ad5c5)

### observed_connections-004027

```text
(config-rtr)# event-logging <cr>
```

Handler ` RVA 0xF596700 `；selector ` 36 `；EOL ` RVA 0x3546F4A8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1ea4acfddc3eabec](../../evidence/conditions-sets-012.md#c-1ea4acfddc3eabec)

### observed_connections-004012

```text
(config-rtr)# exit <cr>
```

Handler ` RVA 0x118ADDE0 `；selector ` 0 `；EOL ` RVA 0x3558F320 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-40a73d5b651f029e](../../evidence/conditions-sets-025.md#c-40a73d5b651f029e)

### observed_connections-004038

```text
(config-rtr)# graceful-restart <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 22 `；EOL ` RVA 0x3569DA70 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-94abebb1e1370965](../../evidence/conditions-sets-057.md#c-94abebb1e1370965)

### observed_connections-004142

```text
(config-rtr)# graceful-restart helper <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 23 `；EOL ` RVA 0x3569DDF8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4feff3abfdec660b](../../evidence/conditions-sets-031.md#c-4feff3abfdec660b)

### observed_connections-004180

```text
(config-rtr)# ignore lsa mospf <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 4 `；EOL ` RVA 0x356828B0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1beab640885d026c](../../evidence/conditions-sets-011.md#c-1beab640885d026c) · [状态效果 S-f1b54e72dec767c5](../../evidence/state_effects-sets-051.md#s-f1b54e72dec767c5)

### observed_connections-004073

```text
(config-rtr)# interface-id snmp-if-index <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 15 `；EOL ` RVA 0x3567AEC8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1beab640885d026c](../../evidence/conditions-sets-011.md#c-1beab640885d026c)

### observed_connections-004020

```text
(config-rtr)# kill-everyone <cr>
```

Handler ` RVA 0xF57B0C0 `；selector ` 15 `；EOL ` RVA 0x3546E750 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1ea4acfddc3eabec](../../evidence/conditions-sets-012.md#c-1ea4acfddc3eabec)

### observed_connections-004133

```text
(config-rtr)# limit retransmissions <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 14 `；EOL ` RVA 0x35684B60 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f7c09dde851bc86e](../../evidence/conditions-sets-096.md#c-f7c09dde851bc86e)

### observed_connections-004037

```text
(config-rtr)# local-rib-criteria <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 6 `；EOL ` RVA 0x35685D58 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7c77db41462fef9d](../../evidence/conditions-sets-048.md#c-7c77db41462fef9d)

### observed_connections-004026

```text
(config-rtr)# log-adjacency-changes <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 3 `；EOL ` RVA 0x35683638 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1beab640885d026c](../../evidence/conditions-sets-011.md#c-1beab640885d026c)

### observed_connections-004031

```text
(config-rtr)# log-event-type <cr>
```

Handler ` RVA 0xF596700 `；selector ` 34 `；EOL ` RVA 0x3546F0C0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a8fb44d511f5ddfc](../../evidence/conditions-sets-065.md#c-a8fb44d511f5ddfc)

### observed_connections-004022

```text
(config-rtr)# log-neighbor-changes <cr>
```

Handler ` RVA 0xF57B3F0 `；selector ` 16 `；EOL ` RVA 0x3546EA30 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1ea4acfddc3eabec](../../evidence/conditions-sets-012.md#c-1ea4acfddc3eabec)

### observed_connections-004028

```text
(config-rtr)# log-neighbor-warnings <cr>
```

Handler ` RVA 0xF57B570 `；selector ` 17 `；EOL ` RVA 0x3546ED70 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-89b06a7d65d67ae8](../../evidence/conditions-sets-053.md#c-89b06a7d65d67ae8)

### observed_connections-004134

```text
(config-rtr)# max-lsa <number:1..4294967294> <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 1 `；EOL ` RVA 0x356841E0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Maximum number of non self-generated LSAs to accept。

[条件 C-862694a36915b562](../../evidence/conditions-sets-052.md#c-862694a36915b562) · [参数 P-9f9997e004977d15](../../evidence/parameters-sets-012.md#p-9f9997e004977d15)

### observed_connections-004016

```text
(config-rtr)# max-metric intra-area <number:1..16777214> <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 8 `；EOL ` RVA 0x35679358 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Metric value。

[条件 C-534c89d7ed3f6a1d](../../evidence/conditions-sets-033.md#c-534c89d7ed3f6a1d) · [参数 P-0e28f7d951a5907f](../../evidence/parameters-sets-002.md#p-0e28f7d951a5907f)

### observed_connections-004081

```text
(config-rtr)# max-metric router-lsa <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 13 `；EOL ` RVA 0x35679438 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0a16f19fe114bdf5](../../evidence/conditions-sets-004.md#c-0a16f19fe114bdf5)

### observed_connections-004023

```text
(config-rtr)# maximum-paths <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 8 `；EOL ` RVA 0x3558C990 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5e7aee77ddefdc78](../../evidence/conditions-sets-037.md#c-5e7aee77ddefdc78)

### observed_connections-004289

```text
(config-rtr)# maximum-paths <number:dynamic> <cr>
```

Handler ` RVA 0xF5985F0 `；selector ` 37 `；EOL ` RVA 0x3546C008 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Number of paths。

[条件 C-dd64e8eb9f22e96e](../../evidence/conditions-sets-085.md#c-dd64e8eb9f22e96e) · [缺口 G-52e940346a983377](../../evidence/gaps-sets-003.md#g-52e940346a983377) · [参数 P-7ffad4de8209552f](../../evidence/parameters-sets-010.md#p-7ffad4de8209552f)

### observed_connections-004092

```text
(config-rtr)# maximum-paths per-prefix-distribution <cr>
```

Handler ` RVA 0x11BCC820 `；selector ` 0 `；EOL ` RVA 0x35682000 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-669f90cfb55384be](../../evidence/conditions-sets-040.md#c-669f90cfb55384be) · [状态效果 S-bfa91475675be491](../../evidence/state_effects-sets-041.md#s-bfa91475675be491)

### observed_connections-004155

```text
(config-rtr)# metric maximum-hops <number:1..255> <cr>
```

Handler ` RVA 0xF57D6C0 `；selector ` 31 `；EOL ` RVA 0x3546C6A0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Hop count。

[条件 C-55f9a7f5a4e39fbc](../../evidence/conditions-sets-034.md#c-55f9a7f5a4e39fbc) · [参数 P-5d24f266c1fa4cc5](../../evidence/parameters-sets-007.md#p-5d24f266c1fa4cc5)

### observed_connections-004285

```text
(config-rtr)# metric weights <number:0..8> <number:0..255> <number:0..255> <number:0..255> <number:0..255> <number:0..255> <cr>
```

Handler ` RVA 0xF57D6C0 `；selector ` 12 `；EOL ` RVA 0x3546C9C8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Type (Only TOS 0 supported)；` unsigned_number ` K1；` unsigned_number ` K2；` unsigned_number ` K3；` unsigned_number ` K4；` unsigned_number ` K5。

[条件 C-11aafdb59823875f](../../evidence/conditions-sets-007.md#c-11aafdb59823875f) · [参数 P-58bff656a2df4c6d](../../evidence/parameters-sets-007.md#p-58bff656a2df4c6d)

### observed_connections-004299

```text
(config-rtr)# neighbor <address> <interface> <cr>
```

Handler ` RVA 0xF57C0C0 `；selector ` 4 `；EOL ` RVA 0x3546CFA0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Neighbor address。

[条件 C-88e465257d0a4226](../../evidence/conditions-sets-053.md#c-88e465257d0a4226) · [缺口 G-650607f371c46dec](../../evidence/gaps-sets-004.md#g-650607f371c46dec) · [参数 P-ff86e4ca3de61102](../../evidence/parameters-sets-019.md#p-ff86e4ca3de61102) · [状态效果 S-4d5e8ac1165bb8f1](../../evidence/state_effects-sets-017.md#s-4d5e8ac1165bb8f1)

### observed_connections-004255

```text
(config-rtr)# no address-family ipv6 vrf <string> <cr>
```

Handler ` RVA 0x118AFEA0 `；selector ` 0 `；EOL ` RVA 0x35582C90 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` VPN Routing/Forwarding instance name。

[条件 C-03bc8a76470d925b](../../evidence/conditions-sets-002.md#c-03bc8a76470d925b) · [参数 P-a2e6426a52444881](../../evidence/parameters-sets-012.md#p-a2e6426a52444881) · [状态效果 S-6655048c7feb0b6c](../../evidence/state_effects-sets-022.md#s-6655048c7feb0b6c)

### observed_connections-004188

```text
(config-rtr)# no adjacency stagger <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 30 `；EOL ` RVA 0x35682C90 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a7ee70185389a5d8](../../evidence/conditions-sets-065.md#c-a7ee70185389a5d8) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004203

```text
(config-rtr)# no area <number:0..4294967295> <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 10 `；EOL ` RVA 0x35690230 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value。

[条件 C-cbf3a90718ad56af](../../evidence/conditions-sets-078.md#c-cbf3a90718ad56af) · [参数 P-82248a455979973d](../../evidence/parameters-sets-010.md#p-82248a455979973d) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004258

```text
(config-rtr)# no area <number:0..4294967295> authentication key-chain <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 9 `；EOL ` RVA 0x3567D390 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value。

[条件 C-e7ce9709643955fa](../../evidence/conditions-sets-090.md#c-e7ce9709643955fa) · [参数 P-82248a455979973d](../../evidence/parameters-sets-010.md#p-82248a455979973d) · [状态效果 S-0cbbe14055ffd009](../../evidence/state_effects-sets-003.md#s-0cbbe14055ffd009)

### observed_connections-004224

```text
(config-rtr)# no area <number:0..4294967295> default-cost <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 7 `；EOL ` RVA 0x3567D770 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value。

[条件 C-fcc671e0af922334](../../evidence/conditions-sets-098.md#c-fcc671e0af922334) · [参数 P-82248a455979973d](../../evidence/parameters-sets-010.md#p-82248a455979973d) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004281

```text
(config-rtr)# no area <number:0..4294967295> encryption ipsec spi <number:256..4294967295> <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 8 `；EOL ` RVA 0x3567BF10 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value；` unsigned_number ` SPI。

[条件 C-46adf4b7ad2ba379](../../evidence/conditions-sets-028.md#c-46adf4b7ad2ba379) · [参数 P-c5f7d5d1a8c77177](../../evidence/parameters-sets-015.md#p-c5f7d5d1a8c77177) · [状态效果 S-23cde26cb5658654](../../evidence/state_effects-sets-008.md#s-23cde26cb5658654)

### observed_connections-004283

```text
(config-rtr)# no area <number:0..4294967295> filter-list prefix <string> in <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 11 `；EOL ` RVA 0x3568FEB0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value；` string ` Name of an IPv6 prefix-list。

[条件 C-787206d34347b415](../../evidence/conditions-sets-047.md#c-787206d34347b415) · [参数 P-70d47677499df79d](../../evidence/parameters-sets-009.md#p-70d47677499df79d) · [状态效果 S-cd8a0f35ed99fd02](../../evidence/state_effects-sets-044.md#s-cd8a0f35ed99fd02)

### observed_connections-004245

```text
(config-rtr)# no area <number:0..4294967295> mpls <cr>
```

Handler ` RVA 0x11BC2300 `；selector ` 13 `；EOL ` RVA 0x35CD9040 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value。

[条件 C-d76f2ad6ff0b1281](../../evidence/conditions-sets-083.md#c-d76f2ad6ff0b1281) · [参数 P-82248a455979973d](../../evidence/parameters-sets-010.md#p-82248a455979973d) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004223

```text
(config-rtr)# no area <number:0..4294967295> no-transit <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 6 `；EOL ` RVA 0x3567DD10 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value。

[条件 C-33bfc65a49764b25](../../evidence/conditions-sets-020.md#c-33bfc65a49764b25) · [参数 P-82248a455979973d](../../evidence/parameters-sets-010.md#p-82248a455979973d) · [状态效果 S-565c784ee0ab8ceb](../../evidence/state_effects-sets-019.md#s-565c784ee0ab8ceb)

### observed_connections-004233

```text
(config-rtr)# no area <number:0..4294967295> normal <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 5 `；EOL ` RVA 0x3567E0D0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value。

[条件 C-0756d675c9fc6105](../../evidence/conditions-sets-003.md#c-0756d675c9fc6105) · [参数 P-82248a455979973d](../../evidence/parameters-sets-010.md#p-82248a455979973d) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004246

```text
(config-rtr)# no area <number:0..4294967295> nssa <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 3 `；EOL ` RVA 0x3567E9D8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value。

[条件 C-da8fa23073125254](../../evidence/conditions-sets-084.md#c-da8fa23073125254) · [参数 P-82248a455979973d](../../evidence/parameters-sets-010.md#p-82248a455979973d) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004225

```text
(config-rtr)# no area <number:0..4294967295> packet-size <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 14 `；EOL ` RVA 0x3567DA88 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value。

[条件 C-9465905b93719c18](../../evidence/conditions-sets-057.md#c-9465905b93719c18) · [参数 P-82248a455979973d](../../evidence/parameters-sets-010.md#p-82248a455979973d) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004275

```text
(config-rtr)# no area <number:0..4294967295> range <address> <address> <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 2 `；EOL ` RVA 0x3567F058 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value；` address ` IPv4 address to match；` address ` IPv4 mask for address。

[条件 C-5829a63832813ba0](../../evidence/conditions-sets-035.md#c-5829a63832813ba0) · [参数 P-9bb51a77902c1f8a](../../evidence/parameters-sets-012.md#p-9bb51a77902c1f8a) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004278

```text
(config-rtr)# no area <number:0..4294967295> sham-link <address> <address> <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 12 `；EOL ` RVA 0x3568F978 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value；` address ` IPv6 address associated with sham-link source；` address ` IPv6 address associated with sham-link destination。

[条件 C-8f6322e6213fb3a3](../../evidence/conditions-sets-056.md#c-8f6322e6213fb3a3) · [参数 P-64334b8cba0d93ae](../../evidence/parameters-sets-008.md#p-64334b8cba0d93ae) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004238

```text
(config-rtr)# no area <number:0..4294967295> stub <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 4 `；EOL ` RVA 0x3567E430 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value。

[条件 C-e4ea43482183fde0](../../evidence/conditions-sets-088.md#c-e4ea43482183fde0) · [参数 P-82248a455979973d](../../evidence/parameters-sets-010.md#p-82248a455979973d) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004267

```text
(config-rtr)# no area <number:0..4294967295> virtual-link <address> <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 1 `；EOL ` RVA 0x3568EA90 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value；` address ` RouterID associated with virtual link neighbor。

[条件 C-613d9b06f1b79756](../../evidence/conditions-sets-038.md#c-613d9b06f1b79756) · [参数 P-c0370be301cc44d7](../../evidence/parameters-sets-015.md#p-c0370be301cc44d7) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004249

```text
(config-rtr)# no authentication mode strict <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 31 `；EOL ` RVA 0x356852E0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-6093751694b20f29](../../evidence/conditions-sets-038.md#c-6093751694b20f29) · [状态效果 S-f908ad5ba4581615](../../evidence/state_effects-sets-053.md#s-f908ad5ba4581615)

### observed_connections-004116

```text
(config-rtr)# no auto-cost <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 0 `；EOL ` RVA 0x35683E20 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1beab640885d026c](../../evidence/conditions-sets-011.md#c-1beab640885d026c) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004162

```text
(config-rtr)# no bfd all-interfaces <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 20 `；EOL ` RVA 0x3567A168 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b37999daad8cb800](../../evidence/conditions-sets-069.md#c-b37999daad8cb800) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004207

```text
(config-rtr)# no capability vrf-lite <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 7 `；EOL ` RVA 0x35684EE8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-24d0b108f11123ba](../../evidence/conditions-sets-014.md#c-24d0b108f11123ba) · [状态效果 S-a9a77cd3d3899046](../../evidence/state_effects-sets-036.md#s-a9a77cd3d3899046)

### observed_connections-004150

```text
(config-rtr)# no compatible rfc1583 <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 25 `；EOL ` RVA 0x3567A568 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-725b2f0362370d98](../../evidence/conditions-sets-044.md#c-725b2f0362370d98) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004153

```text
(config-rtr)# no compatible rfc1587 <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 26 `；EOL ` RVA 0x3567A860 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-2267723558a951c2](../../evidence/conditions-sets-013.md#c-2267723558a951c2) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004159

```text
(config-rtr)# no compatible rfc5243 <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 27 `；EOL ` RVA 0x3567AB30 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-3be5f0f80ef64898](../../evidence/conditions-sets-023.md#c-3be5f0f80ef64898) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004040

```text
(config-rtr)# no context <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 0 `；EOL ` RVA 0x33C44A60 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e07495ed56793ecc](../../evidence/conditions-sets-086.md#c-e07495ed56793ecc) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004147

```text
(config-rtr)# no default-information originate <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 6 `；EOL ` RVA 0x3558DDA0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-65a80e3c1b49d01e](../../evidence/conditions-sets-039.md#c-65a80e3c1b49d01e) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004057

```text
(config-rtr)# no default-metric <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 12 `；EOL ` RVA 0x3558D7B0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-85f3454ad03a7d8c](../../evidence/conditions-sets-052.md#c-85f3454ad03a7d8c) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004131

```text
(config-rtr)# no default-metric <cr>
```

Handler ` RVA 0xF5756A0 `；selector ` 45 `；EOL ` RVA 0x35471BE8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-82a1a33572fcbf0c](../../evidence/conditions-sets-051.md#c-82a1a33572fcbf0c) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004193

```text
(config-rtr)# no discard-route external <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 11 `；EOL ` RVA 0x356839B8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-38a7650107b27024](../../evidence/conditions-sets-022.md#c-38a7650107b27024) · [状态效果 S-f041ae8aea8370a1](../../evidence/state_effects-sets-051.md#s-f041ae8aea8370a1)

### observed_connections-004076

```text
(config-rtr)# no distance <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 9 `；EOL ` RVA 0x3558C3B8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0f6638009c40211e](../../evidence/conditions-sets-006.md#c-0f6638009c40211e) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004149

```text
(config-rtr)# no distance eigrp <cr>
```

Handler ` RVA 0xF597490 `；selector ` 47 `；EOL ` RVA 0x3546BC50 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-66085f1d757641e8](../../evidence/conditions-sets-039.md#c-66085f1d757641e8) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004189

```text
(config-rtr)# no distance ospf <cr>
```

Handler ` RVA 0x11BCBF10 `；selector ` 0 `；EOL ` RVA 0x35681AC8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-227e092d0814d35c](../../evidence/conditions-sets-014.md#c-227e092d0814d35c) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004260

```text
(config-rtr)# no distribute-list prefix-list <string> in <cr>
```

Handler ` RVA 0x112E3690 `；selector ` 29 `；EOL ` RVA 0x3546D4B0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Prefix-list name。

[条件 C-26c4871ffb253cda](../../evidence/conditions-sets-015.md#c-26c4871ffb253cda) · [参数 P-314b4f47fed4f4b0](../../evidence/parameters-sets-004.md#p-314b4f47fed4f4b0) · [状态效果 S-571f25a92ebd20e4](../../evidence/state_effects-sets-019.md#s-571f25a92ebd20e4)

### observed_connections-004254

```text
(config-rtr)# no distribute-list route-map <string> in <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 14 `；EOL ` RVA 0x3558ECE0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Route-map name。

[条件 C-8775aaf0fcbe5920](../../evidence/conditions-sets-052.md#c-8775aaf0fcbe5920) · [参数 P-95e3798261a43d6d](../../evidence/parameters-sets-012.md#p-95e3798261a43d6d) · [状态效果 S-03c4a91426fbfbee](../../evidence/state_effects-sets-001.md#s-03c4a91426fbfbee)

### observed_connections-004063

```text
(config-rtr)# no domain-id <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 9 `；EOL ` RVA 0x35678E68 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f549a2adfee30eeb](../../evidence/conditions-sets-095.md#c-f549a2adfee30eeb) · [状态效果 S-eaf8f0a58287d37f](../../evidence/state_effects-sets-050.md#s-eaf8f0a58287d37f)

### observed_connections-004205

```text
(config-rtr)# no eigrp graceful-restart <cr>
```

Handler ` RVA 0xF57EE00 `；selector ` 10 `；EOL ` RVA 0x3546FBC0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d619580f5c9cd5d1](../../evidence/conditions-sets-083.md#c-d619580f5c9cd5d1) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004252

```text
(config-rtr)# no eigrp upgrade-cli <string> <cr>
```

Handler ` RVA 0xF5807E0 `；selector ` 142 `；EOL ` RVA 0x354700A0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` EIGRP Virtual-Instance Name。

[条件 C-b20dc967e98a70fe](../../evidence/conditions-sets-069.md#c-b20dc967e98a70fe) · [参数 P-a86103facdcb1297](../../evidence/parameters-sets-013.md#p-a86103facdcb1297) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004111

```text
(config-rtr)# no event-log <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 19 `；EOL ` RVA 0x35683198 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-490803c624d0035c](../../evidence/conditions-sets-029.md#c-490803c624d0035c) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004120

```text
(config-rtr)# no event-log-size <cr>
```

Handler ` RVA 0xF596700 `；selector ` 35 `；EOL ` RVA 0x3546F7E8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-145bb481d8eb3dd4](../../evidence/conditions-sets-008.md#c-145bb481d8eb3dd4) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004107

```text
(config-rtr)# no event-logging <cr>
```

Handler ` RVA 0xF596700 `；selector ` 36 `；EOL ` RVA 0x3546F4A8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1ea4acfddc3eabec](../../evidence/conditions-sets-012.md#c-1ea4acfddc3eabec) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004141

```text
(config-rtr)# no graceful-restart <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 22 `；EOL ` RVA 0x3569DA70 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-94abebb1e1370965](../../evidence/conditions-sets-057.md#c-94abebb1e1370965) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004218

```text
(config-rtr)# no graceful-restart helper <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 23 `；EOL ` RVA 0x3569DDF8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4feff3abfdec660b](../../evidence/conditions-sets-031.md#c-4feff3abfdec660b) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004234

```text
(config-rtr)# no ignore lsa mospf <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 4 `；EOL ` RVA 0x356828B0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1beab640885d026c](../../evidence/conditions-sets-011.md#c-1beab640885d026c) · [状态效果 S-12d71fbe4246f9aa](../../evidence/state_effects-sets-004.md#s-12d71fbe4246f9aa)

### observed_connections-004157

```text
(config-rtr)# no interface-id snmp-if-index <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 15 `；EOL ` RVA 0x3567AEC8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1beab640885d026c](../../evidence/conditions-sets-011.md#c-1beab640885d026c) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004087

```text
(config-rtr)# no kill-everyone <cr>
```

Handler ` RVA 0xF57B0C0 `；selector ` 15 `；EOL ` RVA 0x3546E750 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1ea4acfddc3eabec](../../evidence/conditions-sets-012.md#c-1ea4acfddc3eabec) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004214

```text
(config-rtr)# no limit retransmissions <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 14 `；EOL ` RVA 0x35684B60 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f7c09dde851bc86e](../../evidence/conditions-sets-096.md#c-f7c09dde851bc86e) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004138

```text
(config-rtr)# no local-rib-criteria <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 6 `；EOL ` RVA 0x35685D58 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7c77db41462fef9d](../../evidence/conditions-sets-048.md#c-7c77db41462fef9d) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004102

```text
(config-rtr)# no log-adjacency-changes <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 3 `；EOL ` RVA 0x35683638 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1beab640885d026c](../../evidence/conditions-sets-011.md#c-1beab640885d026c) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004110

```text
(config-rtr)# no log-event-type <cr>
```

Handler ` RVA 0xF596700 `；selector ` 34 `；EOL ` RVA 0x3546F0C0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4089248e6ae3cf82](../../evidence/conditions-sets-025.md#c-4089248e6ae3cf82) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004094

```text
(config-rtr)# no log-neighbor-changes <cr>
```

Handler ` RVA 0xF57B3F0 `；selector ` 16 `；EOL ` RVA 0x3546EA30 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1ea4acfddc3eabec](../../evidence/conditions-sets-012.md#c-1ea4acfddc3eabec) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004103

```text
(config-rtr)# no log-neighbor-warnings <cr>
```

Handler ` RVA 0xF57B570 `；selector ` 17 `；EOL ` RVA 0x3546ED70 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-66aaf0a15bd18565](../../evidence/conditions-sets-040.md#c-66aaf0a15bd18565) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004122

```text
(config-rtr)# no max-lsa <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 1 `；EOL ` RVA 0x356841E0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-6169f73e0cf47d13](../../evidence/conditions-sets-038.md#c-6169f73e0cf47d13) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004051

```text
(config-rtr)# no max-metric <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 13 `；EOL ` RVA 0x35679438 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7e61889e2cdbaa9c](../../evidence/conditions-sets-049.md#c-7e61889e2cdbaa9c) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004050

```text
(config-rtr)# no max-metric intra-area <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 8 `；EOL ` RVA 0x35679358 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-19aed9c37a34ce89](../../evidence/conditions-sets-010.md#c-19aed9c37a34ce89) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004058

```text
(config-rtr)# no maximum-paths <cr>
```

Handler ` RVA 0xF5985F0 `；selector ` 37 `；EOL ` RVA 0x3546C008 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f33ac34498d8b115](../../evidence/conditions-sets-094.md#c-f33ac34498d8b115) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004097

```text
(config-rtr)# no maximum-paths <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 8 `；EOL ` RVA 0x3558C990 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5e7aee77ddefdc78](../../evidence/conditions-sets-037.md#c-5e7aee77ddefdc78) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004184

```text
(config-rtr)# no maximum-paths per-prefix-distribution <cr>
```

Handler ` RVA 0x11BCC820 `；selector ` 0 `；EOL ` RVA 0x35682000 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-669f90cfb55384be](../../evidence/conditions-sets-040.md#c-669f90cfb55384be) · [状态效果 S-1add840f6d7c7265](../../evidence/state_effects-sets-006.md#s-1add840f6d7c7265)

### observed_connections-004154

```text
(config-rtr)# no metric maximum-hops <cr>
```

Handler ` RVA 0xF57D6C0 `；selector ` 31 `；EOL ` RVA 0x3546C6A0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5e1402624c8efa67](../../evidence/conditions-sets-037.md#c-5e1402624c8efa67) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004163

```text
(config-rtr)# no metric weights <cr>
```

Handler ` RVA 0xF57D6C0 `；selector ` 12 `；EOL ` RVA 0x3546C9C8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b52626e11d851ab0](../../evidence/conditions-sets-070.md#c-b52626e11d851ab0) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004044

```text
(config-rtr)# no omp-route-tag <cr>
```

Handler ` RVA 0x118A4750 `；selector ` 0 `；EOL ` RVA 0x3557A0F8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-837421aa0ded5ba7](../../evidence/conditions-sets-051.md#c-837421aa0ded5ba7) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004033

```text
(config-rtr)# no packet-size <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 41 `；EOL ` RVA 0x356856A8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-629f8f30b8f22fc1](../../evidence/conditions-sets-038.md#c-629f8f30b8f22fc1) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004158

```text
(config-rtr)# no passive-interface default <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 11 `；EOL ` RVA 0x3558CF78 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0049d72fe609511d](../../evidence/conditions-sets-001.md#c-0049d72fe609511d) · [状态效果 S-d2ca2bcf48c027e0](../../evidence/state_effects-sets-045.md#s-d2ca2bcf48c027e0)

### observed_connections-004176

```text
(config-rtr)# no passive-interface default <cr>
```

Handler ` RVA 0xF58B500 `；selector ` 132 `；EOL ` RVA 0x3546D9A0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ec9b4d713a4e3235](../../evidence/conditions-sets-091.md#c-ec9b4d713a4e3235) · [状态效果 S-91e6a3d7148c6b3e](../../evidence/state_effects-sets-031.md#s-91e6a3d7148c6b3e)

### observed_connections-004049

```text
(config-rtr)# no poison-reverse <cr>
```

Handler ` RVA 0x118A3D80 `；selector ` 0 `；EOL ` RVA 0x3557A3A0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-837421aa0ded5ba7](../../evidence/conditions-sets-051.md#c-837421aa0ded5ba7) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004072

```text
(config-rtr)# no port <cr>
```

Handler ` RVA 0x118A6E70 `；selector ` 0 `；EOL ` RVA 0x3557A718 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-37f7204339adf83a](../../evidence/conditions-sets-022.md#c-37f7204339adf83a) · [状态效果 S-1e5de5b47ec7c7bd](../../evidence/state_effects-sets-007.md#s-1e5de5b47ec7c7bd)

### observed_connections-004066

```text
(config-rtr)# no prefix-suppression <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 28 `；EOL ` RVA 0x35679D18 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-6a3e394242acd8c5](../../evidence/conditions-sets-041.md#c-6a3e394242acd8c5) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004135

```text
(config-rtr)# no process-min-time percent <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 16 `；EOL ` RVA 0x35686420 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-128da7de5515f0ce](../../evidence/conditions-sets-007.md#c-128da7de5515f0ce) · [状态效果 S-3475588b22b1ed91](../../evidence/state_effects-sets-012.md#s-3475588b22b1ed91)

### observed_connections-004168

```text
(config-rtr)# no queue-depth hello <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 18 `；EOL ` RVA 0x3567B298 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-735f7d9ffd7410b1](../../evidence/conditions-sets-045.md#c-735f7d9ffd7410b1) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004174

```text
(config-rtr)# no queue-depth update <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 17 `；EOL ` RVA 0x3567B620 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1acc368d7ffe37f1](../../evidence/conditions-sets-010.md#c-1acc368d7ffe37f1) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004183

```text
(config-rtr)# no redistribute maximum-prefix <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 5 `；EOL ` RVA 0x3558AB28 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4316444a30a6d889](../../evidence/conditions-sets-026.md#c-4316444a30a6d889) · [状态效果 S-74ac44c62d842a77](../../evidence/state_effects-sets-025.md#s-74ac44c62d842a77)

### observed_connections-004208

```text
(config-rtr)# no redistribute maximum-prefix <cr>
```

Handler ` RVA 0xF598EF0 `；selector ` 33 `；EOL ` RVA 0x35470818 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1c18f75c91d746e4](../../evidence/conditions-sets-011.md#c-1c18f75c91d746e4) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004041

```text
(config-rtr)# no router-id <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 12 `；EOL ` RVA 0x356789A8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-34bedce5381a81c5](../../evidence/conditions-sets-021.md#c-34bedce5381a81c5) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004082

```text
(config-rtr)# no router-id <cr>
```

Handler ` RVA 0xF57EB20 `；selector ` 5 `；EOL ` RVA 0x3546DD90 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d5c368011ce538f6](../../evidence/conditions-sets-082.md#c-d5c368011ce538f6) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004055

```text
(config-rtr)# no shutdown <cr>
```

Handler ` RVA 0xF57D580 `；selector ` 6 `；EOL ` RVA 0x3546C2F8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1ea4acfddc3eabec](../../evidence/conditions-sets-012.md#c-1ea4acfddc3eabec) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004137

```text
(config-rtr)# no shutdown <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 29 `；EOL ` RVA 0x35686118 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-9e59e89df3c539ff](../../evidence/conditions-sets-061.md#c-9e59e89df3c539ff) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004164

```text
(config-rtr)# no snmp context <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 0 `；EOL ` RVA 0x33C455F0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7598dc8aeb3669dc](../../evidence/conditions-sets-046.md#c-7598dc8aeb3669dc) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004270

```text
(config-rtr)# no snmp context <string> community <string> <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 2 `；EOL ` RVA 0x33C45118 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Context Name；` string ` SNMP community string。

[条件 C-5a416169412196ba](../../evidence/conditions-sets-035.md#c-5a416169412196ba) · [参数 P-9b6eb89831feec60](../../evidence/parameters-sets-012.md#p-9b6eb89831feec60) · [状态效果 S-9ffd0c7f0e6ebd24](../../evidence/state_effects-sets-034.md#s-9ffd0c7f0e6ebd24)

### observed_connections-004269

```text
(config-rtr)# no snmp context <string> user <string> <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 23 `；EOL ` RVA 0x33C456D0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Context Name；` string ` Name of the user。

[条件 C-c27aae31069e8d90](../../evidence/conditions-sets-075.md#c-c27aae31069e8d90) · [参数 P-cfc42ec8ad667e32](../../evidence/parameters-sets-016.md#p-cfc42ec8ad667e32) · [状态效果 S-d74c0634618a02ee](../../evidence/state_effects-sets-046.md#s-d74c0634618a02ee)

### observed_connections-004039

```text
(config-rtr)# no split-horizon <cr>
```

Handler ` RVA 0x118A4250 `；selector ` 0 `；EOL ` RVA 0x35579E50 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-837421aa0ded5ba7](../../evidence/conditions-sets-051.md#c-837421aa0ded5ba7) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004206

```text
(config-rtr)# no statistics rib-timings <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 5 `；EOL ` RVA 0x356856E8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7c77db41462fef9d](../../evidence/conditions-sets-048.md#c-7c77db41462fef9d) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004089

```text
(config-rtr)# no stub <cr>
```

Handler ` RVA 0xF57E6E0 `；selector ` 18 `；EOL ` RVA 0x3546E0D8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad2397debc5bb490](../../evidence/conditions-sets-067.md#c-ad2397debc5bb490) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004062

```text
(config-rtr)# no table-map <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 17 `；EOL ` RVA 0x3558D3B0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-594cbff8cacd0517](../../evidence/conditions-sets-035.md#c-594cbff8cacd0517) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004083

```text
(config-rtr)# no timers <cr>
```

Handler ` RVA 0x118A33B0 `；selector ` 0 `；EOL ` RVA 0x3557AB28 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-33aee0bb24dd08d2](../../evidence/conditions-sets-020.md#c-33aee0bb24dd08d2) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004144

```text
(config-rtr)# no timers active-time <cr>
```

Handler ` RVA 0xF597780 `；selector ` 28 `；EOL ` RVA 0x3546B820 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-02d491baab4f633f](../../evidence/conditions-sets-002.md#c-02d491baab4f633f) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004177

```text
(config-rtr)# no timers lsa arrival <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 39 `；EOL ` RVA 0x3567FC98 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-fa3c9c9a155c6696](../../evidence/conditions-sets-097.md#c-fa3c9c9a155c6696) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004100

```text
(config-rtr)# no timers lsa-arrival <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 34 `；EOL ` RVA 0x35680250 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f6abd2ba10b3ee5b](../../evidence/conditions-sets-095.md#c-f6abd2ba10b3ee5b) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004091

```text
(config-rtr)# no timers lsa-group-pacing <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 35 `；EOL ` RVA 0x3567FCC0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8cc6f17d7cfd2fde](../../evidence/conditions-sets-055.md#c-8cc6f17d7cfd2fde) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004101

```text
(config-rtr)# no timers lsa-interval <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 33 `；EOL ` RVA 0x35680228 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-fdf14c4c0d709423](../../evidence/conditions-sets-098.md#c-fdf14c4c0d709423) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004195

```text
(config-rtr)# no timers pacing flood <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 36 `；EOL ` RVA 0x356807F8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-df302bc5d4447d72](../../evidence/conditions-sets-086.md#c-df302bc5d4447d72) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004190

```text
(config-rtr)# no timers pacing lsa-group <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 35 `；EOL ` RVA 0x356807B8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1926387444d56df5](../../evidence/conditions-sets-010.md#c-1926387444d56df5) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004199

```text
(config-rtr)# no timers pacing retransmission <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 37 `；EOL ` RVA 0x35680A98 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0f438fe87bf7ce34](../../evidence/conditions-sets-006.md#c-0f438fe87bf7ce34) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004242

```text
(config-rtr)# no timers throttle lsa <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 40 `；EOL ` RVA 0x3567F968 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e1d2215af8e1b53b](../../evidence/conditions-sets-087.md#c-e1d2215af8e1b53b) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004239

```text
(config-rtr)# no timers throttle spf <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 38 `；EOL ` RVA 0x3567F5B0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e7c90d0f14df6c05](../../evidence/conditions-sets-089.md#c-e7c90d0f14df6c05) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004125

```text
(config-rtr)# no variance <cr>
```

Handler ` RVA 0xF575390 `；selector ` 39 `；EOL ` RVA 0x35470460 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b4b1a8ffa918b955](../../evidence/conditions-sets-070.md#c-b4b1a8ffa918b955) · [状态效果 S-441bf077a51a7d2a](../../evidence/state_effects-sets-015.md#s-441bf077a51a7d2a)

### observed_connections-004014

```text
(config-rtr)# omp-route-tag <cr>
```

Handler ` RVA 0x118A4750 `；selector ` 0 `；EOL ` RVA 0x3557A0F8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-837421aa0ded5ba7](../../evidence/conditions-sets-051.md#c-837421aa0ded5ba7)

### observed_connections-004011

```text
(config-rtr)# packet-size <number:576..10000> <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 41 `；EOL ` RVA 0x356856A8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` OSPFV3 Router Mode Packet Size。

[条件 C-79afc8f43cc58e10](../../evidence/conditions-sets-047.md#c-79afc8f43cc58e10) · [参数 P-2effdea4c654bdda](../../evidence/parameters-sets-004.md#p-2effdea4c654bdda)

### observed_connections-004290

```text
(config-rtr)# passive-interface <interface> <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 11 `；EOL ` RVA 0x3558CF78 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7db0da5f68866211](../../evidence/conditions-sets-049.md#c-7db0da5f68866211) · [缺口 G-4b80e7d9ca6d5df1](../../evidence/gaps-sets-003.md#g-4b80e7d9ca6d5df1) · [参数 P-e04e59bc347f2ed5](../../evidence/parameters-sets-017.md#p-e04e59bc347f2ed5)

### observed_connections-004291

```text
(config-rtr)# passive-interface <interface> <cr>
```

Handler ` RVA 0xF58B500 `；selector ` 132 `；EOL ` RVA 0x3546D9A0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3b66b9b3323494ff](../../evidence/conditions-sets-023.md#c-3b66b9b3323494ff) · [缺口 G-116dbdb9840956a7](../../evidence/gaps-sets-001.md#g-116dbdb9840956a7) · [参数 P-5a96c86933394151](../../evidence/parameters-sets-007.md#p-5a96c86933394151)

### observed_connections-004074

```text
(config-rtr)# passive-interface default <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 11 `；EOL ` RVA 0x3558CF78 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0049d72fe609511d](../../evidence/conditions-sets-001.md#c-0049d72fe609511d) · [状态效果 S-b0f69d610a2b18dc](../../evidence/state_effects-sets-037.md#s-b0f69d610a2b18dc)

### observed_connections-004085

```text
(config-rtr)# passive-interface default <cr>
```

Handler ` RVA 0xF58B500 `；selector ` 132 `；EOL ` RVA 0x3546D9A0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ec9b4d713a4e3235](../../evidence/conditions-sets-091.md#c-ec9b4d713a4e3235) · [状态效果 S-d6c0b996a970ec1e](../../evidence/state_effects-sets-046.md#s-d6c0b996a970ec1e)

### observed_connections-004015

```text
(config-rtr)# poison-reverse <cr>
```

Handler ` RVA 0x118A3D80 `；selector ` 0 `；EOL ` RVA 0x3557A3A0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-837421aa0ded5ba7](../../evidence/conditions-sets-051.md#c-837421aa0ded5ba7)

### observed_connections-004231

```text
(config-rtr)# port <number:1..65535> multicast-group <address> <cr>
```

Handler ` RVA 0x118A6E70 `；selector ` 0 `；EOL ` RVA 0x3557A718 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` UDP port；` address ` multicast address。

[条件 C-72a2ed41500f230a](../../evidence/conditions-sets-044.md#c-72a2ed41500f230a) · [参数 P-17a33cd029b3d968](../../evidence/parameters-sets-002.md#p-17a33cd029b3d968) · [状态效果 S-3a4b663cd7915355](../../evidence/state_effects-sets-013.md#s-3a4b663cd7915355)

### observed_connections-004018

```text
(config-rtr)# prefix-suppression <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 28 `；EOL ` RVA 0x35679D18 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6a3e394242acd8c5](../../evidence/conditions-sets-041.md#c-6a3e394242acd8c5)

### observed_connections-004035

```text
(config-rtr)# process-min-time percent <number:1..100> <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 16 `；EOL ` RVA 0x35686420 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Minimum CPU quantum。

[条件 C-49f41f68e10b577c](../../evidence/conditions-sets-029.md#c-49f41f68e10b577c) · [参数 P-4630903decefa058](../../evidence/parameters-sets-006.md#p-4630903decefa058) · [状态效果 S-056effa6a7727f0c](../../evidence/state_effects-sets-002.md#s-056effa6a7727f0c)

### observed_connections-004172

```text
(config-rtr)# queue-depth hello unlimited <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 18 `；EOL ` RVA 0x3567B298 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d65db6f829194425](../../evidence/conditions-sets-083.md#c-d65db6f829194425) · [状态效果 S-bf6ed544bf149f2e](../../evidence/state_effects-sets-040.md#s-bf6ed544bf149f2e)

### observed_connections-004175

```text
(config-rtr)# queue-depth update unlimited <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 17 `；EOL ` RVA 0x3567B620 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ea99d891bd4579d6](../../evidence/conditions-sets-091.md#c-ea99d891bd4579d6) · [状态效果 S-864bb9f6d328d21b](../../evidence/state_effects-sets-028.md#s-864bb9f6d328d21b)

### observed_connections-004295

```text
(config-rtr)# redistribute <?ipv6_router_action@55558a9c4dc0> <cr>
```

Handler ` RVA 0x112E4940 `；selector ` 32 `；EOL ` RVA 0x35471880 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-805786012b01cb18](../../evidence/conditions-sets-050.md#c-805786012b01cb18) · [缺口 G-848306eab9c85019](../../evidence/gaps-sets-005.md#g-848306eab9c85019)

### observed_connections-004315

```text
(config-rtr)# redistribute <?ipv6_router_action@55558aadef30> level-1 into level-1 distribute-list <string> <cr>
```

Handler ` RVA 0x1E68EA00 `；selector ` 0 `；EOL ` RVA 0x3558B1E0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` IPv6 prefix-list name。

[条件 C-cba7e1c8451cd0e0](../../evidence/conditions-sets-078.md#c-cba7e1c8451cd0e0) · [缺口 G-be4dbeae2b0fd1b7](../../evidence/gaps-sets-007.md#g-be4dbeae2b0fd1b7) · [参数 P-74def948f9d48d17](../../evidence/parameters-sets-009.md#p-74def948f9d48d17) · [状态效果 S-647fd35bd68106f6](../../evidence/state_effects-sets-021.md#s-647fd35bd68106f6)

### observed_connections-004292

```text
(config-rtr)# redistribute <?ipv6_router_action@55558aae02c0> <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 5 `；EOL ` RVA 0x3558AB28 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5a46ff279e3c5d2d](../../evidence/conditions-sets-035.md#c-5a46ff279e3c5d2d) · [缺口 G-f96b6dd5a462af65](../../evidence/gaps-sets-009.md#g-f96b6dd5a462af65)

### observed_connections-004196

```text
(config-rtr)# redistribute maximum-prefix <number:1..4294967295> <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 5 `；EOL ` RVA 0x3558AB28 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Maximum number of IPv6 prefixes redistributed。

[条件 C-eee819d95fc878d7](../../evidence/conditions-sets-092.md#c-eee819d95fc878d7) · [参数 P-342c15197738e4a8](../../evidence/parameters-sets-004.md#p-342c15197738e4a8) · [状态效果 S-6d0c3b54791c0a2b](../../evidence/state_effects-sets-023.md#s-6d0c3b54791c0a2b)

### observed_connections-004217

```text
(config-rtr)# redistribute maximum-prefix <number:1..4294967295> <cr>
```

Handler ` RVA 0xF598EF0 `；selector ` 33 `；EOL ` RVA 0x35470818 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Maximum number of IP prefixes redistributed。

[条件 C-5bb534836f70fab5](../../evidence/conditions-sets-036.md#c-5bb534836f70fab5) · [参数 P-8aa92ffc57542b6b](../../evidence/parameters-sets-011.md#p-8aa92ffc57542b6b)

### observed_connections-004042

```text
(config-rtr)# router-id <address> <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 12 `；EOL ` RVA 0x356789A8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` OSPF router-id in IP address format。

[条件 C-ac19f4b45999909d](../../evidence/conditions-sets-067.md#c-ac19f4b45999909d) · [参数 P-6b8bbf67b66ee40d](../../evidence/parameters-sets-008.md#p-6b8bbf67b66ee40d)

### observed_connections-004084

```text
(config-rtr)# router-id <address> <cr>
```

Handler ` RVA 0xF57EB20 `；selector ` 5 `；EOL ` RVA 0x3546DD90 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` EIGRP Router-ID in IP address format。

[条件 C-da5ae7c403479def](../../evidence/conditions-sets-084.md#c-da5ae7c403479def) · [参数 P-db107ebd08074547](../../evidence/parameters-sets-016.md#p-db107ebd08074547)

### observed_connections-004017

```text
(config-rtr)# shutdown <cr>
```

Handler ` RVA 0xF57D580 `；selector ` 6 `；EOL ` RVA 0x3546C2F8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1ea4acfddc3eabec](../../evidence/conditions-sets-012.md#c-1ea4acfddc3eabec)

### observed_connections-004036

```text
(config-rtr)# shutdown <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 29 `；EOL ` RVA 0x35686118 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9e59e89df3c539ff](../../evidence/conditions-sets-061.md#c-9e59e89df3c539ff)

### observed_connections-004078

```text
(config-rtr)# snmp context <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 0 `；EOL ` RVA 0x33C455F0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7598dc8aeb3669dc](../../evidence/conditions-sets-046.md#c-7598dc8aeb3669dc)

### observed_connections-004265

```text
(config-rtr)# snmp context <string> community <string> <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 2 `；EOL ` RVA 0x33C45118 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Context Name；` string ` SNMP community string。

[条件 C-7f44ea3d5ff83041](../../evidence/conditions-sets-049.md#c-7f44ea3d5ff83041) · [参数 P-9b6eb89831feec60](../../evidence/parameters-sets-012.md#p-9b6eb89831feec60) · [状态效果 S-8642eb04023b2323](../../evidence/state_effects-sets-028.md#s-8642eb04023b2323)

### observed_connections-004264

```text
(config-rtr)# snmp context <string> user <string> <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 23 `；EOL ` RVA 0x33C456D0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Context Name；` string ` Name of the user。

[条件 C-6568ff0a78495959](../../evidence/conditions-sets-039.md#c-6568ff0a78495959) · [参数 P-cfc42ec8ad667e32](../../evidence/parameters-sets-016.md#p-cfc42ec8ad667e32) · [状态效果 S-42394155f848a6f9](../../evidence/state_effects-sets-014.md#s-42394155f848a6f9)

### observed_connections-004013

```text
(config-rtr)# split-horizon <cr>
```

Handler ` RVA 0x118A4250 `；selector ` 0 `；EOL ` RVA 0x35579E50 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-837421aa0ded5ba7](../../evidence/conditions-sets-051.md#c-837421aa0ded5ba7)

### observed_connections-004129

```text
(config-rtr)# statistics rib-timings <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 5 `；EOL ` RVA 0x356856E8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7c77db41462fef9d](../../evidence/conditions-sets-048.md#c-7c77db41462fef9d)

### observed_connections-004032

```text
(config-rtr)# stub <cr>
```

Handler ` RVA 0xF57E6E0 `；selector ` 18 `；EOL ` RVA 0x3546E0D8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d9e9fb0561286c6e](../../evidence/conditions-sets-084.md#c-d9e9fb0561286c6e)

### observed_connections-004286

```text
(config-rtr)# summary-metric <prefix:dynamic> <cr>
```

Handler ` RVA 0xF599350 `；selector ` 41 `；EOL ` RVA 0x3546B1B0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` Summary to configure static metric。

[条件 C-ba52c7dd7597aa10](../../evidence/conditions-sets-072.md#c-ba52c7dd7597aa10) · [缺口 G-b7be92d188e4f568](../../evidence/gaps-sets-006.md#g-b7be92d188e4f568) · [参数 P-34e479abf6ddc8c3](../../evidence/parameters-sets-004.md#p-34e479abf6ddc8c3)

### observed_connections-004287

```text
(config-rtr)# summary-prefix <prefix:dynamic> <cr>
```

Handler ` RVA 0x11BCD0C0 `；selector ` 0 `；EOL ` RVA 0x35678468 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` IPv6 prefix x:x::y/&lt;z&gt;。

[条件 C-df750e1d44d52f8f](../../evidence/conditions-sets-086.md#c-df750e1d44d52f8f) · [缺口 G-aebef948931d3962](../../evidence/gaps-sets-006.md#g-aebef948931d3962) · [参数 P-5541466a50700e08](../../evidence/parameters-sets-007.md#p-5541466a50700e08)

### observed_connections-004288

```text
(config-rtr)# summary-prefix <prefix:dynamic> <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 7 `；EOL ` RVA 0x3558E5B8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` IPv6 prefix x:x::y/&lt;z&gt;。

[条件 C-602832e54111933d](../../evidence/conditions-sets-037.md#c-602832e54111933d) · [缺口 G-5415c98bb3beea7d](../../evidence/gaps-sets-003.md#g-5415c98bb3beea7d) · [参数 P-524c2669942857d5](../../evidence/parameters-sets-007.md#p-524c2669942857d5)

### observed_connections-004070

```text
(config-rtr)# table-map <string> <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 17 `；EOL ` RVA 0x3558D3B0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` route-map name。

[条件 C-8b098e53b19af504](../../evidence/conditions-sets-054.md#c-8b098e53b19af504) · [参数 P-938b97a9007202b0](../../evidence/parameters-sets-011.md#p-938b97a9007202b0)

### observed_connections-004262

```text
(config-rtr)# timers <number:5..65535> <number:1..65535> <number:0..65535> <number:1..65535> <cr>
```

Handler ` RVA 0x118A33B0 `；selector ` 0 `；EOL ` RVA 0x3557AB28 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Update period；` unsigned_number ` Route timeout period；` unsigned_number ` Route holddown period；` unsigned_number ` Route garbage collection period。

[条件 C-ca554a610df55f4e](../../evidence/conditions-sets-078.md#c-ca554a610df55f4e) · [参数 P-d51807527d246a56](../../evidence/parameters-sets-016.md#p-d51807527d246a56)

### observed_connections-004145

```text
(config-rtr)# timers active-time disabled <cr>
```

Handler ` RVA 0xF597780 `；selector ` 28 `；EOL ` RVA 0x3546B820 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7ac65a448416a133](../../evidence/conditions-sets-048.md#c-7ac65a448416a133)

### observed_connections-004086

```text
(config-rtr)# timers lsa arrival <number:0..600000> <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 39 `；EOL ` RVA 0x3567FC98 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` The minimum interval in milliseconds between accepting the same LSA。

[条件 C-cb9a75bb8197c897](../../evidence/conditions-sets-078.md#c-cb9a75bb8197c897) · [参数 P-cce2480c66974e88](../../evidence/parameters-sets-016.md#p-cce2480c66974e88)

### observed_connections-004024

```text
(config-rtr)# timers lsa-arrival <number:0..600> <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 34 `；EOL ` RVA 0x35680250 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` The minimum interval in sec between accepting the same LSA。

[条件 C-d14c514bd813ca33](../../evidence/conditions-sets-081.md#c-d14c514bd813ca33) · [参数 P-b236508c16bc6a2f](../../evidence/parameters-sets-014.md#p-b236508c16bc6a2f)

### observed_connections-004021

```text
(config-rtr)# timers lsa-group-pacing <number:10..1800> <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 35 `；EOL ` RVA 0x3567FCC0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Interval between group of LSA being refreshed or maxaged。

[条件 C-a2deb4bfd71a27df](../../evidence/conditions-sets-063.md#c-a2deb4bfd71a27df) · [参数 P-293a9a0fa5ea435f](../../evidence/parameters-sets-004.md#p-293a9a0fa5ea435f)

### observed_connections-004025

```text
(config-rtr)# timers lsa-interval <number:0..600> <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 33 `；EOL ` RVA 0x35680228 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` The minimum interval in sec between originating the same LSA。

[条件 C-e1a569d3b7310da0](../../evidence/conditions-sets-087.md#c-e1a569d3b7310da0) · [参数 P-b1de97e74cd91b69](../../evidence/parameters-sets-013.md#p-b1de97e74cd91b69)

### observed_connections-004113

```text
(config-rtr)# timers pacing flood <number:5..100> <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 36 `；EOL ` RVA 0x356807F8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` The minimum interval in msec to pace limit flooding on interface。

[条件 C-29f1585114b0b0c3](../../evidence/conditions-sets-016.md#c-29f1585114b0b0c3) · [参数 P-8843036aeaaafb65](../../evidence/parameters-sets-011.md#p-8843036aeaaafb65)

### observed_connections-004106

```text
(config-rtr)# timers pacing lsa-group <number:10..1800> <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 35 `；EOL ` RVA 0x356807B8 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Interval in sec between group of LSA being refreshed or maxaged。

[条件 C-1b6c12acfb32004c](../../evidence/conditions-sets-011.md#c-1b6c12acfb32004c) · [参数 P-33516692db176a1f](../../evidence/parameters-sets-004.md#p-33516692db176a1f)

### observed_connections-004118

```text
(config-rtr)# timers pacing retransmission <number:5..200> <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 37 `；EOL ` RVA 0x35680A98 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` The minimum interval in msec between neighbor retransmissions。

[条件 C-36144b186064e4d2](../../evidence/conditions-sets-021.md#c-36144b186064e4d2) · [参数 P-5145792a7f94c65c](../../evidence/parameters-sets-007.md#p-5145792a7f94c65c)

### observed_connections-004274

```text
(config-rtr)# timers throttle lsa <number:0..600000> <number:1..600000> <number:1..600000> <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 40 `；EOL ` RVA 0x3567F968 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Delay to generate first occurrence of LSA in milliseconds；` unsigned_number ` Minimum delay between originating the same LSA in milliseconds；` unsigned_number ` Maximum delay between originating the same LSA in milliseconds。

[条件 C-000cedefc16bfcdb](../../evidence/conditions-sets-001.md#c-000cedefc16bfcdb) · [参数 P-f7355f473cab718e](../../evidence/parameters-sets-018.md#p-f7355f473cab718e)

### observed_connections-004271

```text
(config-rtr)# timers throttle spf <number:1..600000> <number:1..600000> <number:1..600000> <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 38 `；EOL ` RVA 0x3567F5B0 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Delay between receiving a change to SPF calculation in milliseconds；` unsigned_number ` Delay between first and second SPF calculation in milliseconds；` unsigned_number ` Maximum wait time in milliseconds for SPF calculations。

[条件 C-65f9c582c583f22c](../../evidence/conditions-sets-039.md#c-65f9c582c583f22c) · [参数 P-ca419c83cd2c2169](../../evidence/parameters-sets-015.md#p-ca419c83cd2c2169)

### observed_connections-004126

```text
(config-rtr)# variance <number:1..128> <cr>
```

Handler ` RVA 0xF575390 `；selector ` 39 `；EOL ` RVA 0x35470460 `。

模式根 ` RVA 0x3558A680 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Metric variance multiplier。

[条件 C-6284279f2d205f1b](../../evidence/conditions-sets-038.md#c-6284279f2d205f1b) · [参数 P-e5d7af4eb9b25e83](../../evidence/parameters-sets-017.md#p-e5d7af4eb9b25e83)
