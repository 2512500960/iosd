# router · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-000999

```text
(config-router)# address-family <?option@5555897b9978> <cr>
```

Handler ` RVA 0xE1FD070 `；selector ` 0 `；EOL ` RVA 0x34265BE8 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5063844706e86dab](../../evidence/conditions-sets-031.md#c-5063844706e86dab) · [缺口 G-6c97a00936c9a69a](../../evidence/gaps-sets-004.md#g-6c97a00936c9a69a) · [状态效果 S-dc2cda9dd2cb5917](../../evidence/state_effects-sets-047.md#s-dc2cda9dd2cb5917)

### observed_connections-001000

```text
(config-router)# address-family <?option@555589a1fe18> <cr>
```

Handler ` RVA 0xF12CFC0 `；selector ` 0 `；EOL ` RVA 0x344CC060 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-18c5ff671af6db82](../../evidence/conditions-sets-010.md#c-18c5ff671af6db82) · [缺口 G-48a29f9232ec20ca](../../evidence/gaps-sets-003.md#g-48a29f9232ec20ca) · [状态效果 S-cfa21c2c3f269a33](../../evidence/state_effects-sets-044.md#s-cfa21c2c3f269a33)

### observed_connections-000164

```text
(config-router)# adjacency stagger <cr>
```

Handler ` RVA 0xFD324F0 `；selector ` 80 `；EOL ` RVA 0x34B87228 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a359f8913da3971d](../../evidence/conditions-sets-063.md#c-a359f8913da3971d)

### observed_connections-000693

```text
(config-router)# adjacency stagger none <number:1..65535> <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 25 `；EOL ` RVA 0x34885408 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Maximum number of adjacencies allowed to be forming。

[条件 C-4c11e1493b3dfdb8](../../evidence/conditions-sets-030.md#c-4c11e1493b3dfdb8) · [参数 P-3cc69d946850ba83](../../evidence/parameters-sets-005.md#p-3cc69d946850ba83) · [状态效果 S-4f38cf40b896bdca](../../evidence/state_effects-sets-017.md#s-4f38cf40b896bdca)

### observed_connections-000724

```text
(config-router)# adjacency stagger none disable <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 30 `；EOL ` RVA 0x35682C90 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d3301cd4a67feb24](../../evidence/conditions-sets-081.md#c-d3301cd4a67feb24) · [状态效果 S-499756c84e48c340](../../evidence/state_effects-sets-016.md#s-499756c84e48c340)

### observed_connections-000053

```text
(config-router)# adjacency-check <cr>
```

Handler ` RVA 0xFD324F0 `；selector ` 79 `；EOL ` RVA 0x34B8B568 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d320464e5add632e](../../evidence/conditions-sets-081.md#c-d320464e5add632e)

### observed_connections-000481

```text
(config-router)# advertise link attributes <cr>
```

Handler ` RVA 0x106AEEE0 `；selector ` 119 `；EOL ` RVA 0x34B92228 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-393f8aba960de147](../../evidence/conditions-sets-022.md#c-393f8aba960de147)

### observed_connections-000153

```text
(config-router)# advertise passive-only <cr>
```

Handler ` RVA 0xFD324F0 `；selector ` 84 `；EOL ` RVA 0x34B875B0 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d320464e5add632e](../../evidence/conditions-sets-081.md#c-d320464e5add632e)

### observed_connections-000501

```text
(config-router)# aggregate-address <address> <address> <cr>
```

Handler ` RVA 0xF1B7BE0 `；selector ` 0 `；EOL ` RVA 0x344E0440 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Aggregate address；` address ` Aggregate mask。

[条件 C-1b4ad12700da4b0a](../../evidence/conditions-sets-011.md#c-1b4ad12700da4b0a) · [参数 P-fcbb55161a16b08b](../../evidence/parameters-sets-019.md#p-fcbb55161a16b08b)

### observed_connections-000897

```text
(config-router)# area <address> <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 10 `；EOL ` RVA 0x35690230 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` OSPF area ID in IP address format。

[条件 C-fde7f797e084e680](../../evidence/conditions-sets-098.md#c-fde7f797e084e680) · [缺口 G-9ec84dd2ca8f2c5f](../../evidence/gaps-sets-006.md#g-9ec84dd2ca8f2c5f) · [参数 P-f232dfa7b78071ba](../../evidence/parameters-sets-018.md#p-f232dfa7b78071ba) · [状态效果 S-28363f7d007b33de](../../evidence/state_effects-sets-009.md#s-28363f7d007b33de)

### observed_connections-000353

```text
(config-router)# area <address> authentication <cr>
```

Handler ` RVA 0xFC633D0 `；selector ` 6 `；EOL ` RVA 0x34888F58 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` OSPF area ID in IP address format。

[条件 C-8b749948a983d77d](../../evidence/conditions-sets-054.md#c-8b749948a983d77d) · [参数 P-8e1f7faf24b67167](../../evidence/parameters-sets-011.md#p-8e1f7faf24b67167) · [状态效果 S-277fb1be935020a4](../../evidence/state_effects-sets-009.md#s-277fb1be935020a4)

### observed_connections-000966

```text
(config-router)# area <address> authentication key-chain <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 9 `；EOL ` RVA 0x3567D390 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` OSPF area ID in IP address format。

[条件 C-2988bd4ec7178a83](../../evidence/conditions-sets-016.md#c-2988bd4ec7178a83) · [缺口 G-9ec84dd2ca8f2c5f](../../evidence/gaps-sets-006.md#g-9ec84dd2ca8f2c5f) · [参数 P-f232dfa7b78071ba](../../evidence/parameters-sets-018.md#p-f232dfa7b78071ba) · [状态效果 S-e38e2179037df5c0](../../evidence/state_effects-sets-048.md#s-e38e2179037df5c0)

### observed_connections-000628

```text
(config-router)# area <address> capability default-exclusion <cr>
```

Handler ` RVA 0xFC633D0 `；selector ` 14 `；EOL ` RVA 0x34889260 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` OSPF area ID in IP address format。

[条件 C-9b0786cb32af9587](../../evidence/conditions-sets-060.md#c-9b0786cb32af9587) · [参数 P-8e1f7faf24b67167](../../evidence/parameters-sets-011.md#p-8e1f7faf24b67167) · [状态效果 S-9f0e6cf7d90d8c59](../../evidence/state_effects-sets-034.md#s-9f0e6cf7d90d8c59)

### observed_connections-000933

```text
(config-router)# area <address> default-cost <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 7 `；EOL ` RVA 0x3567D770 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` OSPF area ID in IP address format。

[条件 C-6745b168916aff06](../../evidence/conditions-sets-040.md#c-6745b168916aff06) · [缺口 G-9ec84dd2ca8f2c5f](../../evidence/gaps-sets-006.md#g-9ec84dd2ca8f2c5f) · [参数 P-f232dfa7b78071ba](../../evidence/parameters-sets-018.md#p-f232dfa7b78071ba) · [状态效果 S-28363f7d007b33de](../../evidence/state_effects-sets-009.md#s-28363f7d007b33de)

### observed_connections-000629

```text
(config-router)# area <address> default-cost <number:0..16777214> <cr>
```

Handler ` RVA 0xFC633D0 `；selector ` 5 `；EOL ` RVA 0x34889590 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` OSPF area ID in IP address format；` unsigned_number ` Stub's advertised external route metric。

[条件 C-351dcafc284d6f2e](../../evidence/conditions-sets-021.md#c-351dcafc284d6f2e) · [参数 P-247a59f038f31c43](../../evidence/parameters-sets-003.md#p-247a59f038f31c43)

### observed_connections-000993

```text
(config-router)# area <address> encryption ipsec spi <number:256..4294967295> <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 8 `；EOL ` RVA 0x3567BF10 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` OSPF area ID in IP address format；` unsigned_number ` SPI。

[条件 C-a4d65f2a78bf0534](../../evidence/conditions-sets-064.md#c-a4d65f2a78bf0534) · [缺口 G-9ec84dd2ca8f2c5f](../../evidence/gaps-sets-006.md#g-9ec84dd2ca8f2c5f) · [参数 P-eefb03881ada0e10](../../evidence/parameters-sets-018.md#p-eefb03881ada0e10) · [状态效果 S-dfa6e1fb7ea61dab](../../evidence/state_effects-sets-047.md#s-dfa6e1fb7ea61dab)

### observed_connections-000838

```text
(config-router)# area <address> filter-list prefix <string> in <cr>
```

Handler ` RVA 0xFC633D0 `；selector ` 12 `；EOL ` RVA 0x3488ADA0 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` OSPF area ID in IP address format；` string ` Name of an IP prefix-list。

[条件 C-b8714fed2a38de00](../../evidence/conditions-sets-071.md#c-b8714fed2a38de00) · [参数 P-00f8b12482475330](../../evidence/parameters-sets-001.md#p-00f8b12482475330) · [状态效果 S-e386ba4cab1077d4](../../evidence/state_effects-sets-048.md#s-e386ba4cab1077d4)

### observed_connections-000995

```text
(config-router)# area <address> filter-list prefix <string> in <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 11 `；EOL ` RVA 0x3568FEB0 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` OSPF area ID in IP address format；` string ` Name of an IPv6 prefix-list。

[条件 C-787206d34347b415](../../evidence/conditions-sets-047.md#c-787206d34347b415) · [缺口 G-9ec84dd2ca8f2c5f](../../evidence/gaps-sets-006.md#g-9ec84dd2ca8f2c5f) · [参数 P-58698db921e01781](../../evidence/parameters-sets-007.md#p-58698db921e01781) · [状态效果 S-099596d06e789eed](../../evidence/state_effects-sets-002.md#s-099596d06e789eed)

### observed_connections-000942

```text
(config-router)# area <address> mpls <cr>
```

Handler ` RVA 0x11BC2300 `；selector ` 13 `；EOL ` RVA 0x35CD9040 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` OSPF area ID in IP address format。

[条件 C-d76f2ad6ff0b1281](../../evidence/conditions-sets-083.md#c-d76f2ad6ff0b1281) · [缺口 G-9ec84dd2ca8f2c5f](../../evidence/gaps-sets-006.md#g-9ec84dd2ca8f2c5f) · [参数 P-f232dfa7b78071ba](../../evidence/parameters-sets-018.md#p-f232dfa7b78071ba) · [状态效果 S-28363f7d007b33de](../../evidence/state_effects-sets-009.md#s-28363f7d007b33de)

### observed_connections-000932

```text
(config-router)# area <address> no-transit <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 6 `；EOL ` RVA 0x3567DD10 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` OSPF area ID in IP address format。

[条件 C-33bfc65a49764b25](../../evidence/conditions-sets-020.md#c-33bfc65a49764b25) · [缺口 G-9ec84dd2ca8f2c5f](../../evidence/gaps-sets-006.md#g-9ec84dd2ca8f2c5f) · [参数 P-f232dfa7b78071ba](../../evidence/parameters-sets-018.md#p-f232dfa7b78071ba) · [状态效果 S-447586db1c9275d1](../../evidence/state_effects-sets-015.md#s-447586db1c9275d1)

### observed_connections-000935

```text
(config-router)# area <address> normal <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 5 `；EOL ` RVA 0x3567E0D0 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` OSPF area ID in IP address format。

[条件 C-0756d675c9fc6105](../../evidence/conditions-sets-003.md#c-0756d675c9fc6105) · [缺口 G-9ec84dd2ca8f2c5f](../../evidence/gaps-sets-006.md#g-9ec84dd2ca8f2c5f) · [参数 P-f232dfa7b78071ba](../../evidence/parameters-sets-018.md#p-f232dfa7b78071ba) · [状态效果 S-28363f7d007b33de](../../evidence/state_effects-sets-009.md#s-28363f7d007b33de)

### observed_connections-000437

```text
(config-router)# area <address> nssa <cr>
```

Handler ` RVA 0xFC633D0 `；selector ` 3 `；EOL ` RVA 0x3488A4F8 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` OSPF area ID in IP address format。

[条件 C-239fdba0b0f44db3](../../evidence/conditions-sets-014.md#c-239fdba0b0f44db3) · [参数 P-8e1f7faf24b67167](../../evidence/parameters-sets-011.md#p-8e1f7faf24b67167)

### observed_connections-000943

```text
(config-router)# area <address> nssa <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 3 `；EOL ` RVA 0x3567E9D8 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` OSPF area ID in IP address format。

[条件 C-da8fa23073125254](../../evidence/conditions-sets-084.md#c-da8fa23073125254) · [缺口 G-9ec84dd2ca8f2c5f](../../evidence/gaps-sets-006.md#g-9ec84dd2ca8f2c5f) · [参数 P-f232dfa7b78071ba](../../evidence/parameters-sets-018.md#p-f232dfa7b78071ba) · [状态效果 S-28363f7d007b33de](../../evidence/state_effects-sets-009.md#s-28363f7d007b33de)

### observed_connections-000934

```text
(config-router)# area <address> packet-size <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 14 `；EOL ` RVA 0x3567DA88 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` OSPF area ID in IP address format。

[条件 C-ffe30655b1fa76e8](../../evidence/conditions-sets-099.md#c-ffe30655b1fa76e8) · [缺口 G-9ec84dd2ca8f2c5f](../../evidence/gaps-sets-006.md#g-9ec84dd2ca8f2c5f) · [参数 P-f232dfa7b78071ba](../../evidence/parameters-sets-018.md#p-f232dfa7b78071ba) · [状态效果 S-28363f7d007b33de](../../evidence/state_effects-sets-009.md#s-28363f7d007b33de)

### observed_connections-000633

```text
(config-router)# area <address> packet-size <number:576..10000> <cr>
```

Handler ` RVA 0xFC633D0 `；selector ` 16 `；EOL ` RVA 0x348898A8 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` OSPF area ID in IP address format；` unsigned_number ` OSPF Area Mode Packet Size。

[条件 C-cc09b63a85380783](../../evidence/conditions-sets-079.md#c-cc09b63a85380783) · [参数 P-9df8d7df1363662a](../../evidence/parameters-sets-012.md#p-9df8d7df1363662a)

### observed_connections-000788

```text
(config-router)# area <address> range <address> <address> <cr>
```

Handler ` RVA 0xFC633D0 `；selector ` 2 `；EOL ` RVA 0x3488A918 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` OSPF area ID in IP address format；` address ` IP address to match；` address ` IP mask for address。

[条件 C-73748f78e2e08247](../../evidence/conditions-sets-045.md#c-73748f78e2e08247) · [参数 P-fcec4044b4e285ae](../../evidence/parameters-sets-019.md#p-fcec4044b4e285ae)

### observed_connections-000797

```text
(config-router)# area <address> sham-link <address> <address> <cr>
```

Handler ` RVA 0xFC633D0 `；selector ` 13 `；EOL ` RVA 0x3488C368 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` OSPF area ID in IP address format；` address ` IP addr associated with sham-link source；` address ` IP addr associated with sham-link destination。

[条件 C-d45f0223a2bb888a](../../evidence/conditions-sets-082.md#c-d45f0223a2bb888a) · [参数 P-e1a3aabfad815899](../../evidence/parameters-sets-017.md#p-e1a3aabfad815899)

### observed_connections-000988

```text
(config-router)# area <address> sham-link <address> <address> <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 12 `；EOL ` RVA 0x3568F978 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` OSPF area ID in IP address format；` address ` IPv6 address associated with sham-link source；` address ` IPv6 address associated with sham-link destination。

[条件 C-8f6322e6213fb3a3](../../evidence/conditions-sets-056.md#c-8f6322e6213fb3a3) · [缺口 G-9ec84dd2ca8f2c5f](../../evidence/gaps-sets-006.md#g-9ec84dd2ca8f2c5f) · [参数 P-162f7002fd5bb514](../../evidence/parameters-sets-002.md#p-162f7002fd5bb514) · [状态效果 S-28363f7d007b33de](../../evidence/state_effects-sets-009.md#s-28363f7d007b33de)

### observed_connections-000397

```text
(config-router)# area <address> stub <cr>
```

Handler ` RVA 0xFC633D0 `；selector ` 4 `；EOL ` RVA 0x34889C50 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` OSPF area ID in IP address format。

[条件 C-e5eb87120876d832](../../evidence/conditions-sets-089.md#c-e5eb87120876d832) · [参数 P-8e1f7faf24b67167](../../evidence/parameters-sets-011.md#p-8e1f7faf24b67167)

### observed_connections-000939

```text
(config-router)# area <address> stub <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 4 `；EOL ` RVA 0x3567E430 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` OSPF area ID in IP address format。

[条件 C-e4ea43482183fde0](../../evidence/conditions-sets-088.md#c-e4ea43482183fde0) · [缺口 G-9ec84dd2ca8f2c5f](../../evidence/gaps-sets-006.md#g-9ec84dd2ca8f2c5f) · [参数 P-f232dfa7b78071ba](../../evidence/parameters-sets-018.md#p-f232dfa7b78071ba) · [状态效果 S-28363f7d007b33de](../../evidence/state_effects-sets-009.md#s-28363f7d007b33de)

### observed_connections-000691

```text
(config-router)# area <address> virtual-link <address> <cr>
```

Handler ` RVA 0xFC633D0 `；selector ` 1 `；EOL ` RVA 0x3488BA80 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` OSPF area ID in IP address format；` address ` ID (IP addr) associated with virtual link neighbor。

[条件 C-7a08ce155b775fe2](../../evidence/conditions-sets-047.md#c-7a08ce155b775fe2) · [参数 P-949ca1915ecefddd](../../evidence/parameters-sets-011.md#p-949ca1915ecefddd)

### observed_connections-000975

```text
(config-router)# area <address> virtual-link <address> <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 1 `；EOL ` RVA 0x3568EA90 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` OSPF area ID in IP address format；` address ` RouterID associated with virtual link neighbor。

[条件 C-613d9b06f1b79756](../../evidence/conditions-sets-038.md#c-613d9b06f1b79756) · [缺口 G-9ec84dd2ca8f2c5f](../../evidence/gaps-sets-006.md#g-9ec84dd2ca8f2c5f) · [参数 P-ed197afca0a5d6d7](../../evidence/parameters-sets-018.md#p-ed197afca0a5d6d7) · [状态效果 S-28363f7d007b33de](../../evidence/state_effects-sets-009.md#s-28363f7d007b33de)

### observed_connections-000695

```text
(config-router)# area <number:0..4294967295> authentication null <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 9 `；EOL ` RVA 0x3567D390 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value。

[条件 C-582f67f8ffc2439b](../../evidence/conditions-sets-035.md#c-582f67f8ffc2439b) · [参数 P-82248a455979973d](../../evidence/parameters-sets-010.md#p-82248a455979973d) · [状态效果 S-7cfe0fd6456b73b5](../../evidence/state_effects-sets-027.md#s-7cfe0fd6456b73b5)

### observed_connections-000681

```text
(config-router)# area <number:0..4294967295> default-cost <number:0..16777214> <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 7 `；EOL ` RVA 0x3567D770 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value；` unsigned_number ` Stub's advertised external route metric。

[条件 C-b526f02c57a7caf3](../../evidence/conditions-sets-070.md#c-b526f02c57a7caf3) · [参数 P-0d696e682ec4fdd3](../../evidence/parameters-sets-001.md#p-0d696e682ec4fdd3)

### observed_connections-000863

```text
(config-router)# area <number:0..4294967295> filter-list prefix <string> in <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 11 `；EOL ` RVA 0x3568FEB0 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value；` string ` Name of an IPv6 prefix-list。

[条件 C-787206d34347b415](../../evidence/conditions-sets-047.md#c-787206d34347b415) · [参数 P-70d47677499df79d](../../evidence/parameters-sets-009.md#p-70d47677499df79d) · [状态效果 S-9c6b80052c73c997](../../evidence/state_effects-sets-033.md#s-9c6b80052c73c997)

### observed_connections-000540

```text
(config-router)# area <number:0..4294967295> mpls <cr>
```

Handler ` RVA 0x11BC2300 `；selector ` 13 `；EOL ` RVA 0x35CD9040 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value。

[条件 C-d76f2ad6ff0b1281](../../evidence/conditions-sets-083.md#c-d76f2ad6ff0b1281) · [参数 P-82248a455979973d](../../evidence/parameters-sets-010.md#p-82248a455979973d)

### observed_connections-000996

```text
(config-router)# area <number:0..4294967295> mpls traffic-engineering tunnel-tail ipv6 <interface> <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 13 `；EOL ` RVA 0x35CD8C80 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value。

[条件 C-f1c2953b4006fad1](../../evidence/conditions-sets-093.md#c-f1c2953b4006fad1) · [缺口 G-dfcdfd1174df2cfb](../../evidence/gaps-sets-008.md#g-dfcdfd1174df2cfb) · [参数 P-e600dd0718248ad9](../../evidence/parameters-sets-017.md#p-e600dd0718248ad9) · [状态效果 S-5243d665f21f002a](../../evidence/state_effects-sets-018.md#s-5243d665f21f002a)

### observed_connections-000445

```text
(config-router)# area <number:0..4294967295> no-transit <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 6 `；EOL ` RVA 0x3567DD10 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value。

[条件 C-33bfc65a49764b25](../../evidence/conditions-sets-020.md#c-33bfc65a49764b25) · [参数 P-82248a455979973d](../../evidence/parameters-sets-010.md#p-82248a455979973d) · [状态效果 S-0a39db95de0ecf43](../../evidence/state_effects-sets-003.md#s-0a39db95de0ecf43)

### observed_connections-000495

```text
(config-router)# area <number:0..4294967295> normal <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 5 `；EOL ` RVA 0x3567E0D0 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value。

[条件 C-0756d675c9fc6105](../../evidence/conditions-sets-003.md#c-0756d675c9fc6105) · [参数 P-82248a455979973d](../../evidence/parameters-sets-010.md#p-82248a455979973d)

### observed_connections-000544

```text
(config-router)# area <number:0..4294967295> nssa <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 3 `；EOL ` RVA 0x3567E9D8 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value。

[条件 C-da8fa23073125254](../../evidence/conditions-sets-084.md#c-da8fa23073125254) · [参数 P-82248a455979973d](../../evidence/parameters-sets-010.md#p-82248a455979973d)

### observed_connections-000682

```text
(config-router)# area <number:0..4294967295> packet-size <number:576..10000> <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 14 `；EOL ` RVA 0x3567DA88 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value；` unsigned_number ` OSPFV3 Area Mode Packet Size。

[条件 C-25be41a833a7297e](../../evidence/conditions-sets-015.md#c-25be41a833a7297e) · [参数 P-6006ae58436d1dba](../../evidence/parameters-sets-008.md#p-6006ae58436d1dba)

### observed_connections-000818

```text
(config-router)# area <number:0..4294967295> range <address> <address> <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 2 `；EOL ` RVA 0x3567F058 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value；` address ` IPv4 address to match；` address ` IPv4 mask for address。

[条件 C-5829a63832813ba0](../../evidence/conditions-sets-035.md#c-5829a63832813ba0) · [参数 P-9bb51a77902c1f8a](../../evidence/parameters-sets-012.md#p-9bb51a77902c1f8a)

### observed_connections-000970

```text
(config-router)# area <number:0..4294967295> range <prefix:dynamic> <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 2 `；EOL ` RVA 0x3567F058 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value；` prefix_dynamic ` IPv6 prefix to match。

[条件 C-6652131f9eca7103](../../evidence/conditions-sets-040.md#c-6652131f9eca7103) · [缺口 G-e5466db54e535e0b](../../evidence/gaps-sets-008.md#g-e5466db54e535e0b) · [参数 P-53a24dc2e39151cb](../../evidence/parameters-sets-007.md#p-53a24dc2e39151cb)

### observed_connections-000821

```text
(config-router)# area <number:0..4294967295> sham-link <address> <address> <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 12 `；EOL ` RVA 0x3568F978 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value；` address ` IPv6 address associated with sham-link source；` address ` IPv6 address associated with sham-link destination。

[条件 C-8f6322e6213fb3a3](../../evidence/conditions-sets-056.md#c-8f6322e6213fb3a3) · [参数 P-64334b8cba0d93ae](../../evidence/parameters-sets-008.md#p-64334b8cba0d93ae)

### observed_connections-000510

```text
(config-router)# area <number:0..4294967295> stub <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 4 `；EOL ` RVA 0x3567E430 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value。

[条件 C-e4ea43482183fde0](../../evidence/conditions-sets-088.md#c-e4ea43482183fde0) · [参数 P-82248a455979973d](../../evidence/parameters-sets-010.md#p-82248a455979973d)

### observed_connections-000740

```text
(config-router)# area <number:0..4294967295> virtual-link <address> <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 1 `；EOL ` RVA 0x3568EA90 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value；` address ` RouterID associated with virtual link neighbor。

[条件 C-613d9b06f1b79756](../../evidence/conditions-sets-038.md#c-613d9b06f1b79756) · [参数 P-c0370be301cc44d7](../../evidence/parameters-sets-015.md#p-c0370be301cc44d7)

### observed_connections-000221

```text
(config-router)# area-password <string> <cr>
```

Handler ` RVA 0xFD324F0 `；selector ` 16 `；EOL ` RVA 0x34B882A8 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Area password。

[条件 C-02b087fb5111fd25](../../evidence/conditions-sets-002.md#c-02b087fb5111fd25) · [参数 P-a311607d5a8743ec](../../evidence/parameters-sets-012.md#p-a311607d5a8743ec) · [状态效果 S-e1b6a535c21b7e7c](../../evidence/state_effects-sets-048.md#s-e1b6a535c21b7e7c)

### observed_connections-000523

```text
(config-router)# authentication key-chain <string> <cr>
```

Handler ` RVA 0xFD324F0 `；selector ` 19 `；EOL ` RVA 0x34B88E88 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of key-chain。

[条件 C-d320464e5add632e](../../evidence/conditions-sets-081.md#c-d320464e5add632e) · [参数 P-fce79716c6cb8231](../../evidence/parameters-sets-019.md#p-fce79716c6cb8231) · [状态效果 S-10422c2411533ae3](../../evidence/state_effects-sets-004.md#s-10422c2411533ae3)

### observed_connections-000516

```text
(config-router)# authentication mode md5 <cr>
```

Handler ` RVA 0xFD324F0 `；selector ` 18 `；EOL ` RVA 0x34B889D8 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ebd7ed1765266083](../../evidence/conditions-sets-091.md#c-ebd7ed1765266083) · [状态效果 S-d64674211567544c](../../evidence/state_effects-sets-045.md#s-d64674211567544c)

### observed_connections-000562

```text
(config-router)# authentication mode strict <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 31 `；EOL ` RVA 0x356852E0 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6093751694b20f29](../../evidence/conditions-sets-038.md#c-6093751694b20f29) · [状态效果 S-0519becdfe8ed933](../../evidence/state_effects-sets-002.md#s-0519becdfe8ed933)

### observed_connections-000226

```text
(config-router)# authentication send-only <cr>
```

Handler ` RVA 0xFD324F0 `；selector ` 20 `；EOL ` RVA 0x34B89218 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d320464e5add632e](../../evidence/conditions-sets-081.md#c-d320464e5add632e) · [状态效果 S-215a69fd55751153](../../evidence/state_effects-sets-008.md#s-215a69fd55751153)

### observed_connections-000035

```text
(config-router)# auto-cost <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 0 `；EOL ` RVA 0x34886C40 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-94a7180cc2a0954e](../../evidence/conditions-sets-057.md#c-94a7180cc2a0954e)

### observed_connections-000051

```text
(config-router)# auto-cost <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 0 `；EOL ` RVA 0x35683E20 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1beab640885d026c](../../evidence/conditions-sets-011.md#c-1beab640885d026c)

### observed_connections-000040

```text
(config-router)# auto-summary <cr>
```

Handler ` RVA 0xE1FA6B0 `；selector ` 0 `；EOL ` RVA 0x34257468 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-dfc9b807534948c3](../../evidence/conditions-sets-086.md#c-dfc9b807534948c3)

### observed_connections-000552

```text
(config-router)# autoroute-exclude prefix-list <string> <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 48 `；EOL ` RVA 0x348947F8 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of an IP prefix-list。

[条件 C-f28ec2e7da96fd84](../../evidence/conditions-sets-094.md#c-f28ec2e7da96fd84) · [参数 P-3b14d41ad5441eb2](../../evidence/parameters-sets-005.md#p-3b14d41ad5441eb2)

### observed_connections-000182

```text
(config-router)# bfd all-interfaces <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 20 `；EOL ` RVA 0x3567A168 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b37999daad8cb800](../../evidence/conditions-sets-069.md#c-b37999daad8cb800)

### observed_connections-000203

```text
(config-router)# bfd check-ctrl-plane-failure <cr>
```

Handler ` RVA 0xE1FA610 `；selector ` 0 `；EOL ` RVA 0x34256F50 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-aa5ec25db4a05959](../../evidence/conditions-sets-066.md#c-aa5ec25db4a05959) · [状态效果 S-9b75c3a4a4a27589](../../evidence/state_effects-sets-033.md#s-9b75c3a4a4a27589)

### observed_connections-000936

```text
(config-router)# bfd interface <interface> <cr>
```

Handler ` RVA 0xE1FA610 `；selector ` 0 `；EOL ` RVA 0x34256F50 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ba011fa51c5c0d1f](../../evidence/conditions-sets-072.md#c-ba011fa51c5c0d1f) · [缺口 G-a69c3c217e9d3c29](../../evidence/gaps-sets-006.md#g-a69c3c217e9d3c29) · [参数 P-a376c6dae0f3d48b](../../evidence/parameters-sets-012.md#p-a376c6dae0f3d48b)

### observed_connections-000429

```text
(config-router)# bgp additional-paths install <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 69 `；EOL ` RVA 0x344D7E18 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ac9fbf82cf234df3](../../evidence/conditions-sets-067.md#c-ac9fbf82cf234df3) · [状态效果 S-34d06e26a91b7846](../../evidence/state_effects-sets-012.md#s-34d06e26a91b7846)

### observed_connections-000476

```text
(config-router)# bgp additional-paths select <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 71 `；EOL ` RVA 0x344D7AC0 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c25c0eae29e38b9b](../../evidence/conditions-sets-075.md#c-c25c0eae29e38b9b)

### observed_connections-000137

```text
(config-router)# bgp advertise-best-external <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 70 `；EOL ` RVA 0x344D8C68 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0aa0ca38535d7e8f](../../evidence/conditions-sets-004.md#c-0aa0ca38535d7e8f)

### observed_connections-000242

```text
(config-router)# bgp advertisement startup-delay <number:1..3600> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 95 `；EOL ` RVA 0x344D5480 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` value (seconds)。

[条件 C-75228d1d5b59b476](../../evidence/conditions-sets-045.md#c-75228d1d5b59b476) · [参数 P-2f4e89207dad2c19](../../evidence/parameters-sets-004.md#p-2f4e89207dad2c19)

### observed_connections-000477

```text
(config-router)# bgp aggregate-timer <number:6..60> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 58 `；EOL ` RVA 0x344DECB8 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timer interval。

[条件 C-e17ed17447bf4f15](../../evidence/conditions-sets-087.md#c-e17ed17447bf4f15) · [参数 P-1e21d132041b5c35](../../evidence/parameters-sets-003.md#p-1e21d132041b5c35)

### observed_connections-000303

```text
(config-router)# bgp aigp-rib-metric <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 91 `；EOL ` RVA 0x344FF8E8 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d8e7f4b3ece00a9c](../../evidence/conditions-sets-083.md#c-d8e7f4b3ece00a9c)

### observed_connections-000120

```text
(config-router)# bgp always-compare-med <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 5 `；EOL ` RVA 0x344D0D68 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-64ac03fc4a2fa258](../../evidence/conditions-sets-039.md#c-64ac03fc4a2fa258)

### observed_connections-000387

```text
(config-router)# bgp asnotation dot <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 64 `；EOL ` RVA 0x344D1078 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-64ac03fc4a2fa258](../../evidence/conditions-sets-039.md#c-64ac03fc4a2fa258)

### observed_connections-000761

```text
(config-router)# bgp bestpath aigp ignore <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 43 `；EOL ` RVA 0x344FE610 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-429806c5c1eb838e](../../evidence/conditions-sets-026.md#c-429806c5c1eb838e)

### observed_connections-000755

```text
(config-router)# bgp bestpath as-path ignore <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 17 `；EOL ` RVA 0x344FDD80 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d8e7f4b3ece00a9c](../../evidence/conditions-sets-083.md#c-d8e7f4b3ece00a9c)

### observed_connections-000757

```text
(config-router)# bgp bestpath as-path multipath-relax <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 51 `；EOL ` RVA 0x344FE028 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d8e7f4b3ece00a9c](../../evidence/conditions-sets-083.md#c-d8e7f4b3ece00a9c)

### observed_connections-000573

```text
(config-router)# bgp bestpath compare-routerid <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 24 `；EOL ` RVA 0x344FE2C0 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d8e7f4b3ece00a9c](../../evidence/conditions-sets-083.md#c-d8e7f4b3ece00a9c)

### observed_connections-000760

```text
(config-router)# bgp bestpath cost-community ignore <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 41 `；EOL ` RVA 0x344FE8E8 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d8e7f4b3ece00a9c](../../evidence/conditions-sets-083.md#c-d8e7f4b3ece00a9c)

### observed_connections-000655

```text
(config-router)# bgp bestpath igp-metric ignore <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 42 `；EOL ` RVA 0x344D8348 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d991eb087fde87d6](../../evidence/conditions-sets-084.md#c-d991eb087fde87d6)

### observed_connections-000758

```text
(config-router)# bgp bestpath med missing-as-worst <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 18 `；EOL ` RVA 0x344FDA70 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d8e7f4b3ece00a9c](../../evidence/conditions-sets-083.md#c-d8e7f4b3ece00a9c) · [状态效果 S-bb7c2799c54caa43](../../evidence/state_effects-sets-040.md#s-bb7c2799c54caa43)

### observed_connections-000666

```text
(config-router)# bgp bestpath prefix-validate allow-invalid <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 78 `；EOL ` RVA 0x344D8658 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1dee027f507a8808](../../evidence/conditions-sets-012.md#c-1dee027f507a8808)

### observed_connections-000673

```text
(config-router)# bgp bestpath prefix-validate disable <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 77 `；EOL ` RVA 0x344D8900 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1dee027f507a8808](../../evidence/conditions-sets-012.md#c-1dee027f507a8808)

### observed_connections-000450

```text
(config-router)# bgp client-to-client reflection <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 9 `；EOL ` RVA 0x344D1F08 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-47cc66e217ba6921](../../evidence/conditions-sets-028.md#c-47cc66e217ba6921) · [状态效果 S-8a7ec42bea3e87e0](../../evidence/state_effects-sets-029.md#s-8a7ec42bea3e87e0)

### observed_connections-000987

```text
(config-router)# bgp client-to-client reflection intra-cluster cluster-id <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 9 `；EOL ` RVA 0x344D1F08 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d5e0cf2955ca1934](../../evidence/conditions-sets-083.md#c-d5e0cf2955ca1934) · [缺口 G-fd6f1c66016d5403](../../evidence/gaps-sets-009.md#g-fd6f1c66016d5403) · [状态效果 S-c625337892b0b550](../../evidence/state_effects-sets-042.md#s-c625337892b0b550)

### observed_connections-000441

```text
(config-router)# bgp cluster-id <number:1..4294967294> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 7 `；EOL ` RVA 0x344D1AD0 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Route-Reflector Cluster-id as 32 bit quantity。

[条件 C-15fb7522ff3280f4](../../evidence/conditions-sets-009.md#c-15fb7522ff3280f4) · [参数 P-7fc1f526457bb512](../../evidence/parameters-sets-010.md#p-7fc1f526457bb512)

### observed_connections-000968

```text
(config-router)# bgp confederation identifier <?bgp_as4_action@555589a26dd8> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 6 `；EOL ` RVA 0x344D2E10 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-64ac03fc4a2fa258](../../evidence/conditions-sets-039.md#c-64ac03fc4a2fa258) · [缺口 G-60bbe62157f0e79d](../../evidence/gaps-sets-004.md#g-60bbe62157f0e79d)

### observed_connections-000969

```text
(config-router)# bgp confederation peers <?bgp_as4_action@555589a27148> <cr>
```

Handler ` RVA 0xF1C67F0 `；selector ` 0 `；EOL ` RVA 0x344D3288 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-940a3679fc075efb](../../evidence/conditions-sets-057.md#c-940a3679fc075efb) · [缺口 G-d8748d5211b19a8c](../../evidence/gaps-sets-008.md#g-d8748d5211b19a8c) · [状态效果 S-ce2cef7882e87522](../../evidence/state_effects-sets-044.md#s-ce2cef7882e87522)

### observed_connections-000482

```text
(config-router)# bgp consistency-checker error-message <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 3 `；EOL ` RVA 0x344D1450 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0411c814712884d0](../../evidence/conditions-sets-002.md#c-0411c814712884d0) · [状态效果 S-c52eeb9e92267035](../../evidence/state_effects-sets-042.md#s-c52eeb9e92267035)

### observed_connections-000459

```text
(config-router)# bgp consistency-checker error-message interval <number:5..1440> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 3 `；EOL ` RVA 0x344D1478 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Interval (minutes)。

[条件 C-e485f0ae28149763](../../evidence/conditions-sets-088.md#c-e485f0ae28149763) · [参数 P-d418b8dc0a480816](../../evidence/parameters-sets-016.md#p-d418b8dc0a480816) · [状态效果 S-c52eeb9e92267035](../../evidence/state_effects-sets-042.md#s-c52eeb9e92267035)

### observed_connections-000146

```text
(config-router)# bgp dampening <cr>
```

Handler ` RVA 0xF1B85B0 `；selector ` 0 `；EOL ` RVA 0x344D6EE0 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a52b5d31e05a36c4](../../evidence/conditions-sets-064.md#c-a52b5d31e05a36c4)

### observed_connections-000662

```text
(config-router)# bgp dampening route-map <string> <cr>
```

Handler ` RVA 0xF1B85B0 `；selector ` 8 `；EOL ` RVA 0x344D70A8 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` route-map name。

[条件 C-d06af2cef4d91ed5](../../evidence/conditions-sets-080.md#c-d06af2cef4d91ed5) · [参数 P-cefb8bd3af0f3611](../../evidence/parameters-sets-016.md#p-cefb8bd3af0f3611)

### observed_connections-000657

```text
(config-router)# bgp default inter-as-hybrid advertise-source-routes <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 57 `；EOL ` RVA 0x344D6518 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-81b58dd2cbd358f4](../../evidence/conditions-sets-050.md#c-81b58dd2cbd358f4)

### observed_connections-000365

```text
(config-router)# bgp default ipv4-unicast <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 19 `；EOL ` RVA 0x344D5C70 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f2ea3e11587f1d00](../../evidence/conditions-sets-094.md#c-f2ea3e11587f1d00)

### observed_connections-000373

```text
(config-router)# bgp default ipv6-nexthop <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 75 `；EOL ` RVA 0x344D5F68 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-529ce920fc162503](../../evidence/conditions-sets-032.md#c-529ce920fc162503)

### observed_connections-000123

```text
(config-router)# bgp default local-preference <number:0..4294967295> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 0 `；EOL ` RVA 0x344D61F8 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Configure default local preference value。

[条件 C-eeb07e6c887bfa15](../../evidence/conditions-sets-092.md#c-eeb07e6c887bfa15) · [参数 P-bbaa795371be4929](../../evidence/parameters-sets-014.md#p-bbaa795371be4929)

### observed_connections-000644

```text
(config-router)# bgp default route-target filter <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 25 `；EOL ` RVA 0x344D6880 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7c5541307ffb6273](../../evidence/conditions-sets-048.md#c-7c5541307ffb6273)

### observed_connections-000645

```text
(config-router)# bgp default route-target filter <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 25 `；EOL ` RVA 0x344D6B20 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8e6e17167ac37ffa](../../evidence/conditions-sets-055.md#c-8e6e17167ac37ffa)

### observed_connections-000205

```text
(config-router)# bgp deterministic-med <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 10 `；EOL ` RVA 0x344D3588 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-64ac03fc4a2fa258](../../evidence/conditions-sets-039.md#c-64ac03fc4a2fa258)

### observed_connections-000167

```text
(config-router)# bgp dmzlink-bw <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 31 `；EOL ` RVA 0x344DA218 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9541beb5318b281b](../../evidence/conditions-sets-058.md#c-9541beb5318b281b)

### observed_connections-000044

```text
(config-router)# bgp dynamic-med-interval <number:60..4294967295> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 21 `；EOL ` RVA 0x344D35B0 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Interval value (seconds)。

[条件 C-38ce5019a2c1772b](../../evidence/conditions-sets-022.md#c-38ce5019a2c1772b) · [参数 P-46229203881d92f3](../../evidence/parameters-sets-006.md#p-46229203881d92f3)

### observed_connections-000177

```text
(config-router)# bgp enforce-first-as <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 20 `；EOL ` RVA 0x344D27B8 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-64ac03fc4a2fa258](../../evidence/conditions-sets-039.md#c-64ac03fc4a2fa258)

### observed_connections-000258

```text
(config-router)# bgp enhanced-error <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 82 `；EOL ` RVA 0x344D51F8 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-118bc45c73923a21](../../evidence/conditions-sets-007.md#c-118bc45c73923a21)

### observed_connections-000091

```text
(config-router)# bgp fast-external-fallover <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 1 `；EOL ` RVA 0x344D04A0 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-64ac03fc4a2fa258](../../evidence/conditions-sets-039.md#c-64ac03fc4a2fa258)

### observed_connections-000282

```text
(config-router)# bgp graceful-restart <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 35 `；EOL ` RVA 0x344FBA50 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-64ac03fc4a2fa258](../../evidence/conditions-sets-039.md#c-64ac03fc4a2fa258)

### observed_connections-000261

```text
(config-router)# bgp graceful-restart restart-time <number:1..3600> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 36 `；EOL ` RVA 0x344FB420 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Delay value (seconds)。

[条件 C-522f9ddb9087f36c](../../evidence/conditions-sets-032.md#c-522f9ddb9087f36c) · [参数 P-9a658d0255f3f336](../../evidence/parameters-sets-012.md#p-9a658d0255f3f336)

### observed_connections-000266

```text
(config-router)# bgp graceful-restart stalepath-time <number:1..3600> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 37 `；EOL ` RVA 0x344FB488 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Delay value (seconds)。

[条件 C-cfc55c673eee80e6](../../evidence/conditions-sets-080.md#c-cfc55c673eee80e6) · [参数 P-19e237cca67521b5](../../evidence/parameters-sets-002.md#p-19e237cca67521b5)

### observed_connections-000997

```text
(config-router)# bgp graceful-shutdown all vrfs <number:30..65535> community <?bgp_community_action@555589a50368> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 79 `；EOL ` RVA 0x344FBEB8 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` time in seconds。

[条件 C-72c6652d205c2de8](../../evidence/conditions-sets-044.md#c-72c6652d205c2de8) · [缺口 G-948a76544295c135](../../evidence/gaps-sets-005.md#g-948a76544295c135) · [参数 P-dd4a2c52a38fd0cf](../../evidence/parameters-sets-017.md#p-dd4a2c52a38fd0cf) · [状态效果 S-4fddde17c0eeb24b](../../evidence/state_effects-sets-017.md#s-4fddde17c0eeb24b)

### observed_connections-000824

```text
(config-router)# bgp graceful-shutdown all vrfs activate <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 79 `；EOL ` RVA 0x344FBEB8 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-491cf7fd66a513cc](../../evidence/conditions-sets-029.md#c-491cf7fd66a513cc) · [状态效果 S-6383fad906de3647](../../evidence/state_effects-sets-021.md#s-6383fad906de3647)

### observed_connections-000564

```text
(config-router)# bgp ha-mode sso <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 83 `；EOL ` RVA 0x3372E840 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-155396da89bd2248](../../evidence/conditions-sets-008.md#c-155396da89bd2248)

### observed_connections-000812

```text
(config-router)# bgp inject-map <string> exist-map <string> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 32 `；EOL ` RVA 0x344DBD90 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` route-map name；` string ` route-map name。

[条件 C-c8f87fd8a243e819](../../evidence/conditions-sets-077.md#c-c8f87fd8a243e819) · [参数 P-5b20d3d4cbc8fc0d](../../evidence/parameters-sets-007.md#p-5b20d3d4cbc8fc0d)

### observed_connections-000642

```text
(config-router)# bgp label-allocation-batch <number:0..4294967295> <number:0..4294967295> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 53 `；EOL ` RVA 0x344D0830 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timer value in milliseconds；` unsigned_number ` Batch Size。

[条件 C-64ac03fc4a2fa258](../../evidence/conditions-sets-039.md#c-64ac03fc4a2fa258) · [参数 P-e29c6d656430799f](../../evidence/parameters-sets-017.md#p-e29c6d656430799f)

### observed_connections-000701

```text
(config-router)# bgp listen block <address> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 93 `；EOL ` RVA 0x344D9C28 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IPv4 Dynamic Peering Address。

[条件 C-dbffccb945e1d51c](../../evidence/conditions-sets-085.md#c-dbffccb945e1d51c) · [参数 P-68f33430087a596b](../../evidence/parameters-sets-008.md#p-68f33430087a596b)

### observed_connections-000732

```text
(config-router)# bgp listen block <address> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 93 `；EOL ` RVA 0x344D4530 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IPv4 Dynamic Peering Address。

[条件 C-e40f970c215acb98](../../evidence/conditions-sets-088.md#c-e40f970c215acb98) · [参数 P-31e77b4f9b27b0d8](../../evidence/parameters-sets-004.md#p-31e77b4f9b27b0d8)

### observed_connections-000189

```text
(config-router)# bgp listen limit <number:1..10000> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 61 `；EOL ` RVA 0x344D9B70 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` max number。

[条件 C-41459af2af8f0f91](../../evidence/conditions-sets-026.md#c-41459af2af8f0f91) · [参数 P-37c1504a4795b709](../../evidence/parameters-sets-005.md#p-37c1504a4795b709)

### observed_connections-000252

```text
(config-router)# bgp listen limit <number:1..10000> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 61 `；EOL ` RVA 0x344D4450 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` max number。

[条件 C-14e69c3469d3fa95](../../evidence/conditions-sets-008.md#c-14e69c3469d3fa95) · [参数 P-7c98df76ac336c5d](../../evidence/parameters-sets-010.md#p-7c98df76ac336c5d)

### observed_connections-000559

```text
(config-router)# bgp listen persistent <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 94 `；EOL ` RVA 0x344D4868 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e40f970c215acb98](../../evidence/conditions-sets-088.md#c-e40f970c215acb98)

### observed_connections-000994

```text
(config-router)# bgp listen range <prefix:dynamic> peer-group <string> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 60 `；EOL ` RVA 0x344D40A8 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` IPv4 subnet range；` string ` peer-group name。

[条件 C-50b4011adaa3409b](../../evidence/conditions-sets-031.md#c-50b4011adaa3409b) · [缺口 G-1eaced7a5aa1f6c1](../../evidence/gaps-sets-002.md#g-1eaced7a5aa1f6c1) · [参数 P-fa942e58211b6360](../../evidence/parameters-sets-019.md#p-fa942e58211b6360)

### observed_connections-000185

```text
(config-router)# bgp log-neighbor-changes <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 11 `；EOL ` RVA 0x344D2A60 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-64ac03fc4a2fa258](../../evidence/conditions-sets-039.md#c-64ac03fc4a2fa258)

### observed_connections-000590

```text
(config-router)# bgp maxas-limit <number:1..254> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 26 `；EOL ` RVA 0x344FF660 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of ASes in the AS-PATH attribute(max 254)。

[条件 C-c1ceaf09e04ddde0](../../evidence/conditions-sets-075.md#c-c1ceaf09e04ddde0) · [参数 P-f9a4c71e563aca29](../../evidence/parameters-sets-019.md#p-f9a4c71e563aca29)

### observed_connections-000576

```text
(config-router)# bgp maxcommunity-limit <number:1..1018> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 27 `；EOL ` RVA 0x344FEC70 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of communities in the COMMUNITY attribute。

[条件 C-3d9eccdfd45be7b4](../../evidence/conditions-sets-024.md#c-3d9eccdfd45be7b4) · [参数 P-fd415a945e159c69](../../evidence/parameters-sets-019.md#p-fd415a945e159c69)

### observed_connections-000585

```text
(config-router)# bgp maxextcommunity-limit <number:1..509> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 29 `；EOL ` RVA 0x344FF310 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of extended communities in the EXTENDED COMMUNITY attribute。

[条件 C-b1db4cb1e0874509](../../evidence/conditions-sets-069.md#c-b1db4cb1e0874509) · [参数 P-5c5750b2d8ef73fa](../../evidence/parameters-sets-007.md#p-5c5750b2d8ef73fa)

### observed_connections-000580

```text
(config-router)# bgp maxlargecommunity-limit <number:1..339> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 28 `；EOL ` RVA 0x344FEFC0 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of large communities in the LARGE COMMUNITY attribute。

[条件 C-71184f59b2bed114](../../evidence/conditions-sets-044.md#c-71184f59b2bed114) · [参数 P-ba05587ebb4b8c12](../../evidence/parameters-sets-014.md#p-ba05587ebb4b8c12)

### observed_connections-000229

```text
(config-router)# bgp mpls-local-label <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 81 `；EOL ` RVA 0x344DC108 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b623378aebd31bce](../../evidence/conditions-sets-070.md#c-b623378aebd31bce)

### observed_connections-000706

```text
(config-router)# bgp nexthop route-map <string> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 56 `；EOL ` RVA 0x344DA980 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` route-map name。

[条件 C-cc63c701ccfa00a9](../../evidence/conditions-sets-079.md#c-cc63c701ccfa00a9) · [参数 P-b7fdbd999a56cccb](../../evidence/parameters-sets-014.md#p-b7fdbd999a56cccb)

### observed_connections-000512

```text
(config-router)# bgp nexthop trigger critical-delay <number:0..100> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 48 `；EOL ` RVA 0x344DAEE8 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Critical delay value (seconds)。

[条件 C-48b1a618eb7c3c6c](../../evidence/conditions-sets-029.md#c-48b1a618eb7c3c6c) · [参数 P-2d652965ca057df0](../../evidence/parameters-sets-004.md#p-2d652965ca057df0)

### observed_connections-000505

```text
(config-router)# bgp nexthop trigger delay <number:0..100> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 47 `；EOL ` RVA 0x344DAC68 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Delay value (seconds)。

[条件 C-b11bbf5113bd3dd3](../../evidence/conditions-sets-068.md#c-b11bbf5113bd3dd3) · [参数 P-5e2421d364aa6d27](../../evidence/parameters-sets-008.md#p-5e2421d364aa6d27)

### observed_connections-000699

```text
(config-router)# bgp nexthop trigger enable <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 49 `；EOL ` RVA 0x344DAC40 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4bbac4809370bed7](../../evidence/conditions-sets-030.md#c-4bbac4809370bed7)

### observed_connections-000725

```text
(config-router)# bgp nopeerup-delay cold-boot <number:1..3600> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 74 `；EOL ` RVA 0x344D4E90 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Delay in seconds。

[条件 C-e11b57e562cf8a08](../../evidence/conditions-sets-087.md#c-e11b57e562cf8a08) · [参数 P-8c48ec9f765274d0](../../evidence/parameters-sets-011.md#p-8c48ec9f765274d0) · [状态效果 S-6ba0cf1b16eaba35](../../evidence/state_effects-sets-023.md#s-6ba0cf1b16eaba35)

### observed_connections-000415

```text
(config-router)# bgp recursion host <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 72 `；EOL ` RVA 0x344D8FE0 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d98c72b0fe073701](../../evidence/conditions-sets-084.md#c-d98c72b0fe073701)

### observed_connections-000138

```text
(config-router)# bgp redistribute-internal <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 2 `；EOL ` RVA 0x344DD308 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bce48006f0ed90c0](../../evidence/conditions-sets-073.md#c-bce48006f0ed90c0)

### observed_connections-000752

```text
(config-router)# bgp refresh max-eor-time <number:600..3600> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 16 `；EOL ` RVA 0x344FCC48 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timer interval (seconds)。

[条件 C-419ac227ad356f7f](../../evidence/conditions-sets-026.md#c-419ac227ad356f7f) · [参数 P-b98ca3d59cd768b4](../../evidence/parameters-sets-014.md#p-b98ca3d59cd768b4)

### observed_connections-000748

```text
(config-router)# bgp refresh stalepath-time <number:600..3600> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 15 `；EOL ` RVA 0x344FC8D8 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timer interval (seconds)。

[条件 C-4acded672b13a09a](../../evidence/conditions-sets-029.md#c-4acded672b13a09a) · [参数 P-98649614cfc8ab83](../../evidence/parameters-sets-012.md#p-98649614cfc8ab83)

### observed_connections-000569

```text
(config-router)# bgp regexp deterministic <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 44 `；EOL ` RVA 0x344FD660 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d8e7f4b3ece00a9c](../../evidence/conditions-sets-083.md#c-d8e7f4b3ece00a9c)

### observed_connections-000416

```text
(config-router)# bgp route-map priority <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 59 `；EOL ` RVA 0x344DE498 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3197f81b43032438](../../evidence/conditions-sets-019.md#c-3197f81b43032438)

### observed_connections-000109

```text
(config-router)# bgp route-map-cache <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 34 `；EOL ` RVA 0x344D0AB8 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-64ac03fc4a2fa258](../../evidence/conditions-sets-039.md#c-64ac03fc4a2fa258)

### observed_connections-000409

```text
(config-router)# bgp router-id <address> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 4 `；EOL ` RVA 0x344CFE70 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Manually configured router identifier。

[条件 C-8c4a286bed9fd0a3](../../evidence/conditions-sets-054.md#c-8c4a286bed9fd0a3) · [参数 P-58b9649a72b68d9e](../../evidence/parameters-sets-007.md#p-58b9649a72b68d9e)

### observed_connections-000493

```text
(config-router)# bgp router-id auto-assign <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 4 `；EOL ` RVA 0x344D9690 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-568e431f752ff985](../../evidence/conditions-sets-034.md#c-568e431f752ff985) · [状态效果 S-54b133fd6413f039](../../evidence/state_effects-sets-018.md#s-54b133fd6413f039)

### observed_connections-000965

```text
(config-router)# bgp router-id interface <interface> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 4 `；EOL ` RVA 0x344CFE70 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c3104cdb94d20190](../../evidence/conditions-sets-075.md#c-c3104cdb94d20190) · [缺口 G-1a0d6ca12b1acc2d](../../evidence/gaps-sets-001.md#g-1a0d6ca12b1acc2d) · [参数 P-f595f8f0cf0ed9c5](../../evidence/parameters-sets-018.md#p-f595f8f0cf0ed9c5)

### observed_connections-000967

```text
(config-router)# bgp router-id interface <interface> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 4 `；EOL ` RVA 0x344D9690 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a7da7aee03806090](../../evidence/conditions-sets-065.md#c-a7da7aee03806090) · [缺口 G-edfbc3d8f7e2dcac](../../evidence/gaps-sets-008.md#g-edfbc3d8f7e2dcac) · [参数 P-4c423966f8292e68](../../evidence/parameters-sets-006.md#p-4c423966f8292e68)

### observed_connections-000875

```text
(config-router)# bgp rpki server tcp <address> port <number:1..65535> refresh <number:1..65535> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 76 `；EOL ` RVA 0x344DF2B0 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IPv6 address of RPKI cache server；` unsigned_number ` Port number；` unsigned_number ` Refresh time in seconds。

[条件 C-5febe211e9716279](../../evidence/conditions-sets-037.md#c-5febe211e9716279) · [参数 P-4a188ed7711f531c](../../evidence/parameters-sets-006.md#p-4a188ed7711f531c)

### observed_connections-000513

```text
(config-router)# bgp rr-group <string> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 23 `；EOL ` RVA 0x344DB928 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Extended community-list name。

[条件 C-70615f1a79ffece3](../../evidence/conditions-sets-043.md#c-70615f1a79ffece3) · [参数 P-fc5dfd7bd2592171](../../evidence/parameters-sets-019.md#p-fc5dfd7bd2592171)

### observed_connections-000308

```text
(config-router)# bgp safe-ebgp-policy <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 92 `；EOL ` RVA 0x344FFBD0 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e43c8b205f2ad28a](../../evidence/conditions-sets-088.md#c-e43c8b205f2ad28a)

### observed_connections-000508

```text
(config-router)# bgp scan-time <number:5..60> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 22 `；EOL ` RVA 0x344DB5B8 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Scanner interval (seconds)。

[条件 C-794d044414bb19c5](../../evidence/conditions-sets-047.md#c-794d044414bb19c5) · [参数 P-874d7de800ad4c96](../../evidence/parameters-sets-010.md#p-874d7de800ad4c96)

### observed_connections-000436

```text
(config-router)# bgp slow-peer detection <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 67 `；EOL ` RVA 0x344DC5D8 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0f8827204ebde490](../../evidence/conditions-sets-006.md#c-0f8827204ebde490)

### observed_connections-000423

```text
(config-router)# bgp slow-peer detection threshold <number:120..3600> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 67 `；EOL ` RVA 0x344DC5B0 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Threshold value (seconds)。

[条件 C-986f507bae68a9c0](../../evidence/conditions-sets-059.md#c-986f507bae68a9c0) · [参数 P-ee916788f3d18216](../../evidence/parameters-sets-018.md#p-ee916788f3d18216)

### observed_connections-000687

```text
(config-router)# bgp slow-peer split-update-group dynamic <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 68 `；EOL ` RVA 0x344DCBA8 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-79cfbdd25ea94e06](../../evidence/conditions-sets-047.md#c-79cfbdd25ea94e06)

### observed_connections-000719

```text
(config-router)# bgp snmp traps add-type <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 90 `；EOL ` RVA 0x344D3B78 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-64ac03fc4a2fa258](../../evidence/conditions-sets-039.md#c-64ac03fc4a2fa258)

### observed_connections-000186

```text
(config-router)# bgp soft-reconfig-backup <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 52 `；EOL ` RVA 0x344DA568 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fb214f36bef7fbc3](../../evidence/conditions-sets-097.md#c-fb214f36bef7fbc3)

### observed_connections-000802

```text
(config-router)# bgp sourced-paths per-net isis all <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 89 `；EOL ` RVA 0x344DE118 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-265131b45ecc5879](../../evidence/conditions-sets-015.md#c-265131b45ecc5879) · [状态效果 S-c9d45bd423a9f244](../../evidence/state_effects-sets-043.md#s-c9d45bd423a9f244)

### observed_connections-000792

```text
(config-router)# bgp sourced-paths per-net ospf all <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 87 `；EOL ` RVA 0x344DDAB8 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-265131b45ecc5879](../../evidence/conditions-sets-015.md#c-265131b45ecc5879) · [状态效果 S-8b2b81009df7c087](../../evidence/state_effects-sets-030.md#s-8b2b81009df7c087)

### observed_connections-000795

```text
(config-router)# bgp sourced-paths per-net ospfv3 all <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 88 `；EOL ` RVA 0x344DDE00 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-265131b45ecc5879](../../evidence/conditions-sets-015.md#c-265131b45ecc5879) · [状态效果 S-d6d8d21c13e7c014](../../evidence/state_effects-sets-046.md#s-d6d8d21c13e7c014)

### observed_connections-000789

```text
(config-router)# bgp sourced-paths per-net static all <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 86 `；EOL ` RVA 0x344DD770 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-265131b45ecc5879](../../evidence/conditions-sets-015.md#c-265131b45ecc5879) · [状态效果 S-94bdbb36eed947d5](../../evidence/state_effects-sets-032.md#s-94bdbb36eed947d5)

### observed_connections-000560

```text
(config-router)# bgp sso route-refresh-enable <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 38 `；EOL ` RVA 0x344FC518 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d8e7f4b3ece00a9c](../../evidence/conditions-sets-083.md#c-d8e7f4b3ece00a9c)

### observed_connections-000151

```text
(config-router)# bgp suppress-inactive <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 45 `；EOL ` RVA 0x344D92E0 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b766a61000b7d48b](../../evidence/conditions-sets-071.md#c-b766a61000b7d48b)

### observed_connections-000014

```text
(config-router)# bgp tid <number:1..255> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 55 `；EOL ` RVA 0x344CF6B0 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Tolology identifier value。

[条件 C-209d149d3bc4fa04](../../evidence/conditions-sets-013.md#c-209d149d3bc4fa04) · [参数 P-fc9b4d47129dbf7b](../../evidence/parameters-sets-019.md#p-fc9b4d47129dbf7b)

### observed_connections-000439

```text
(config-router)# bgp transport path-mtu-discovery <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 50 `；EOL ` RVA 0x344D2528 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-64ac03fc4a2fa258](../../evidence/conditions-sets-039.md#c-64ac03fc4a2fa258)

### observed_connections-000054

```text
(config-router)# bgp update-delay <number:1..3600> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 30 `；EOL ` RVA 0x344D54A8 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Delay value (seconds)。

[条件 C-e8f423ffb89995eb](../../evidence/conditions-sets-090.md#c-e8f423ffb89995eb) · [参数 P-1da0d11406d296fe](../../evidence/parameters-sets-003.md#p-1da0d11406d296fe)

### observed_connections-000660

```text
(config-router)# bgp update-group split as-override <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 73 `；EOL ` RVA 0x344DCF78 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2f7cc0c0004615a7](../../evidence/conditions-sets-019.md#c-2f7cc0c0004615a7)

### observed_connections-000099

```text
(config-router)# bgp upgrade-cli <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 33 `；EOL ` RVA 0x344CFAC8 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a96fcf0a2319bbf7](../../evidence/conditions-sets-065.md#c-a96fcf0a2319bbf7)

### observed_connections-000799

```text
(config-router)# bgp va <address> mask <address> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 80 `；EOL ` RVA 0x344DE840 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` BGP VA ip address；` address ` BGP VA mask address。

[条件 C-0f519ba12c6ed934](../../evidence/conditions-sets-006.md#c-0f519ba12c6ed934) · [参数 P-bc1fb7204f51531e](../../evidence/parameters-sets-014.md#p-bc1fb7204f51531e)

### observed_connections-000567

```text
(config-router)# bgp vrf-update-optimisation off <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 66 `；EOL ` RVA 0x344FCFD0 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d8e7f4b3ece00a9c](../../evidence/conditions-sets-083.md#c-d8e7f4b3ece00a9c)

### observed_connections-000754

```text
(config-router)# bgp write-limit <number:500..2147483647> <number:500..2147483647> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 40 `；EOL ` RVA 0x344FD328 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of messages to be formatted per neighbor/peergroup；` unsigned_number ` Number of messages that can be enqueued in total。

[条件 C-70654b5dcbc951d6](../../evidence/conditions-sets-043.md#c-70654b5dcbc951d6) · [参数 P-bff2d23c76299582](../../evidence/parameters-sets-015.md#p-bff2d23c76299582)

### observed_connections-000247

```text
(config-router)# capability opaque <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 4 `；EOL ` RVA 0x34894378 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-88acc362b84bd124](../../evidence/conditions-sets-053.md#c-88acc362b84bd124) · [状态效果 S-24874c80957bbea3](../../evidence/state_effects-sets-008.md#s-24874c80957bbea3)

### observed_connections-000265

```text
(config-router)# capability vrf-lite <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 7 `；EOL ` RVA 0x35684EE8 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-24d0b108f11123ba](../../evidence/conditions-sets-014.md#c-24d0b108f11123ba) · [状态效果 S-82b3c85b84af0b13](../../evidence/state_effects-sets-028.md#s-82b3c85b84af0b13)

### observed_connections-000118

```text
(config-router)# compatible rfc1583 <cr>
```

Handler ` RVA 0xFC6DF20 `；selector ` 6 `；EOL ` RVA 0x34884168 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-89e1cc66ca5c3c37](../../evidence/conditions-sets-053.md#c-89e1cc66ca5c3c37)

### observed_connections-000159

```text
(config-router)# compatible rfc1583 <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 25 `；EOL ` RVA 0x3567A568 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-725b2f0362370d98](../../evidence/conditions-sets-044.md#c-725b2f0362370d98)

### observed_connections-000136

```text
(config-router)# compatible rfc1587 <cr>
```

Handler ` RVA 0xFC6DF20 `；selector ` 7 `；EOL ` RVA 0x34884478 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-957ae969613136d1](../../evidence/conditions-sets-058.md#c-957ae969613136d1)

### observed_connections-000166

```text
(config-router)# compatible rfc1587 <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 26 `；EOL ` RVA 0x3567A860 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2267723558a951c2](../../evidence/conditions-sets-013.md#c-2267723558a951c2)

### observed_connections-000149

```text
(config-router)# compatible rfc5243 <cr>
```

Handler ` RVA 0xFC6DF20 `；selector ` 8 `；EOL ` RVA 0x34884748 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-93db37c576c8c4dc](../../evidence/conditions-sets-057.md#c-93db37c576c8c4dc)

### observed_connections-000176

```text
(config-router)# compatible rfc5243 <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 27 `；EOL ` RVA 0x3567AB30 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3be5f0f80ef64898](../../evidence/conditions-sets-023.md#c-3be5f0f80ef64898)

### observed_connections-000075

```text
(config-router)# context <string> <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 0 `；EOL ` RVA 0x33C44A60 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` SNMP Context Name。

[条件 C-9affa1869574e86e](../../evidence/conditions-sets-060.md#c-9affa1869574e86e) · [参数 P-f3e465802edc027f](../../evidence/parameters-sets-018.md#p-f3e465802edc027f) · [状态效果 S-355a44aeb0ea4c7f](../../evidence/state_effects-sets-012.md#s-355a44aeb0ea4c7f)

### observed_connections-000424

```text
(config-router)# default adjacency stagger <cr>
```

Handler ` RVA 0xFD324F0 `；selector ` 80 `；EOL ` RVA 0x34B87228 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-579cb5100bc33cb4](../../evidence/conditions-sets-034.md#c-579cb5100bc33cb4) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000485

```text
(config-router)# default adjacency stagger <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 25 `；EOL ` RVA 0x34885408 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-18c3cdbbba24aeed](../../evidence/conditions-sets-010.md#c-18c3cdbbba24aeed) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000520

```text
(config-router)# default adjacency stagger <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 30 `；EOL ` RVA 0x35682C90 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c77fc90849f00aaf](../../evidence/conditions-sets-077.md#c-c77fc90849f00aaf) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000249

```text
(config-router)# default adjacency-check <cr>
```

Handler ` RVA 0xFD324F0 `；selector ` 79 `；EOL ` RVA 0x34B8B568 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d320464e5add632e](../../evidence/conditions-sets-081.md#c-d320464e5add632e) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000697

```text
(config-router)# default advertise link attributes <cr>
```

Handler ` RVA 0x106AEEE0 `；selector ` 119 `；EOL ` RVA 0x34B92228 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-393f8aba960de147](../../evidence/conditions-sets-022.md#c-393f8aba960de147) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000420

```text
(config-router)# default advertise passive-only <cr>
```

Handler ` RVA 0xFD324F0 `；selector ` 84 `；EOL ` RVA 0x34B875B0 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d320464e5add632e](../../evidence/conditions-sets-081.md#c-d320464e5add632e) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000704

```text
(config-router)# default aggregate-address <address> <address> <cr>
```

Handler ` RVA 0xF1B7BE0 `；selector ` 0 `；EOL ` RVA 0x344E0440 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` Aggregate address；` address ` Aggregate mask。

[条件 C-1b4ad12700da4b0a](../../evidence/conditions-sets-011.md#c-1b4ad12700da4b0a) · [参数 P-fcbb55161a16b08b](../../evidence/parameters-sets-019.md#p-fcbb55161a16b08b) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000457

```text
(config-router)# default area <address> <cr>
```

Handler ` RVA 0xFC633D0 `；selector ` 11 `；EOL ` RVA 0x3488C708 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` OSPF area ID in IP address format。

[条件 C-bbb12605a8b30299](../../evidence/conditions-sets-072.md#c-bbb12605a8b30299) · [参数 P-8e1f7faf24b67167](../../evidence/parameters-sets-011.md#p-8e1f7faf24b67167) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000630

```text
(config-router)# default area <address> authentication <cr>
```

Handler ` RVA 0xFC633D0 `；selector ` 6 `；EOL ` RVA 0x34888F58 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` OSPF area ID in IP address format。

[条件 C-8b749948a983d77d](../../evidence/conditions-sets-054.md#c-8b749948a983d77d) · [参数 P-8e1f7faf24b67167](../../evidence/parameters-sets-011.md#p-8e1f7faf24b67167) · [状态效果 S-0341b15bddccf208](../../evidence/state_effects-sets-001.md#s-0341b15bddccf208)

### observed_connections-000770

```text
(config-router)# default area <address> capability default-exclusion <cr>
```

Handler ` RVA 0xFC633D0 `；selector ` 14 `；EOL ` RVA 0x34889260 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` OSPF area ID in IP address format。

[条件 C-9b0786cb32af9587](../../evidence/conditions-sets-060.md#c-9b0786cb32af9587) · [参数 P-8e1f7faf24b67167](../../evidence/parameters-sets-011.md#p-8e1f7faf24b67167) · [状态效果 S-e81b7297ca95be2c](../../evidence/state_effects-sets-049.md#s-e81b7297ca95be2c)

### observed_connections-000631

```text
(config-router)# default area <address> default-cost <cr>
```

Handler ` RVA 0xFC633D0 `；selector ` 5 `；EOL ` RVA 0x34889590 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` OSPF area ID in IP address format。

[条件 C-94181568b37f1b51](../../evidence/conditions-sets-057.md#c-94181568b37f1b51) · [参数 P-8e1f7faf24b67167](../../evidence/parameters-sets-011.md#p-8e1f7faf24b67167) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000869

```text
(config-router)# default area <address> filter-list prefix <string> in <cr>
```

Handler ` RVA 0xFC633D0 `；selector ` 12 `；EOL ` RVA 0x3488ADA0 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` OSPF area ID in IP address format；` string ` Name of an IP prefix-list。

[条件 C-b8714fed2a38de00](../../evidence/conditions-sets-071.md#c-b8714fed2a38de00) · [参数 P-00f8b12482475330](../../evidence/parameters-sets-001.md#p-00f8b12482475330) · [状态效果 S-ca4040d47d9fdbd2](../../evidence/state_effects-sets-043.md#s-ca4040d47d9fdbd2)

### observed_connections-000679

```text
(config-router)# default area <address> nssa <cr>
```

Handler ` RVA 0xFC633D0 `；selector ` 3 `；EOL ` RVA 0x3488A4F8 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` OSPF area ID in IP address format。

[条件 C-239fdba0b0f44db3](../../evidence/conditions-sets-014.md#c-239fdba0b0f44db3) · [参数 P-8e1f7faf24b67167](../../evidence/parameters-sets-011.md#p-8e1f7faf24b67167) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000635

```text
(config-router)# default area <address> packet-size <cr>
```

Handler ` RVA 0xFC633D0 `；selector ` 16 `；EOL ` RVA 0x348898A8 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` OSPF area ID in IP address format。

[条件 C-1b1eeaadf671f1e1](../../evidence/conditions-sets-011.md#c-1b1eeaadf671f1e1) · [参数 P-8e1f7faf24b67167](../../evidence/parameters-sets-011.md#p-8e1f7faf24b67167) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000840

```text
(config-router)# default area <address> range <address> <address> <cr>
```

Handler ` RVA 0xFC633D0 `；selector ` 2 `；EOL ` RVA 0x3488A918 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` OSPF area ID in IP address format；` address ` IP address to match；` address ` IP mask for address。

[条件 C-2e241c19ac1a2507](../../evidence/conditions-sets-018.md#c-2e241c19ac1a2507) · [参数 P-fcec4044b4e285ae](../../evidence/parameters-sets-019.md#p-fcec4044b4e285ae) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000854

```text
(config-router)# default area <address> sham-link <address> <address> <cr>
```

Handler ` RVA 0xFC633D0 `；selector ` 13 `；EOL ` RVA 0x3488C368 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` OSPF area ID in IP address format；` address ` IP addr associated with sham-link source；` address ` IP addr associated with sham-link destination。

[条件 C-d45f0223a2bb888a](../../evidence/conditions-sets-082.md#c-d45f0223a2bb888a) · [参数 P-e1a3aabfad815899](../../evidence/parameters-sets-017.md#p-e1a3aabfad815899) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000659

```text
(config-router)# default area <address> stub <cr>
```

Handler ` RVA 0xFC633D0 `；selector ` 4 `；EOL ` RVA 0x34889C50 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` OSPF area ID in IP address format。

[条件 C-e5eb87120876d832](../../evidence/conditions-sets-089.md#c-e5eb87120876d832) · [参数 P-8e1f7faf24b67167](../../evidence/parameters-sets-011.md#p-8e1f7faf24b67167) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000798

```text
(config-router)# default area <address> virtual-link <address> <cr>
```

Handler ` RVA 0xFC633D0 `；selector ` 1 `；EOL ` RVA 0x3488BA80 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` OSPF area ID in IP address format；` address ` ID (IP addr) associated with virtual link neighbor。

[条件 C-7a08ce155b775fe2](../../evidence/conditions-sets-047.md#c-7a08ce155b775fe2) · [参数 P-949ca1915ecefddd](../../evidence/parameters-sets-011.md#p-949ca1915ecefddd) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000549

```text
(config-router)# default area <number:0..4294967295> <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 10 `；EOL ` RVA 0x35690230 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value。

[条件 C-cbf3a90718ad56af](../../evidence/conditions-sets-078.md#c-cbf3a90718ad56af) · [参数 P-82248a455979973d](../../evidence/parameters-sets-010.md#p-82248a455979973d) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000796

```text
(config-router)# default area <number:0..4294967295> authentication key-chain <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 9 `；EOL ` RVA 0x3567D390 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value。

[条件 C-f55d7f15f0784b78](../../evidence/conditions-sets-095.md#c-f55d7f15f0784b78) · [参数 P-82248a455979973d](../../evidence/parameters-sets-010.md#p-82248a455979973d) · [状态效果 S-7425e4ce34436b92](../../evidence/state_effects-sets-025.md#s-7425e4ce34436b92)

### observed_connections-000685

```text
(config-router)# default area <number:0..4294967295> default-cost <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 7 `；EOL ` RVA 0x3567D770 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value。

[条件 C-c9cf0e71d3c18af5](../../evidence/conditions-sets-078.md#c-c9cf0e71d3c18af5) · [参数 P-82248a455979973d](../../evidence/parameters-sets-010.md#p-82248a455979973d) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000871

```text
(config-router)# default area <number:0..4294967295> encryption ipsec spi <number:256..4294967295> <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 8 `；EOL ` RVA 0x3567BF10 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value；` unsigned_number ` SPI。

[条件 C-eb378abd750ac3cd](../../evidence/conditions-sets-091.md#c-eb378abd750ac3cd) · [参数 P-c5f7d5d1a8c77177](../../evidence/parameters-sets-015.md#p-c5f7d5d1a8c77177) · [状态效果 S-2397a3c8150442ff](../../evidence/state_effects-sets-008.md#s-2397a3c8150442ff)

### observed_connections-000873

```text
(config-router)# default area <number:0..4294967295> filter-list prefix <string> in <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 11 `；EOL ` RVA 0x3568FEB0 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value；` string ` Name of an IPv6 prefix-list。

[条件 C-787206d34347b415](../../evidence/conditions-sets-047.md#c-787206d34347b415) · [参数 P-70d47677499df79d](../../evidence/parameters-sets-009.md#p-70d47677499df79d) · [状态效果 S-635aa964c0c88acf](../../evidence/state_effects-sets-021.md#s-635aa964c0c88acf)

### observed_connections-000729

```text
(config-router)# default area <number:0..4294967295> mpls <cr>
```

Handler ` RVA 0x11BC2300 `；selector ` 13 `；EOL ` RVA 0x35CD9040 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value。

[条件 C-d76f2ad6ff0b1281](../../evidence/conditions-sets-083.md#c-d76f2ad6ff0b1281) · [参数 P-82248a455979973d](../../evidence/parameters-sets-010.md#p-82248a455979973d) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000683

```text
(config-router)# default area <number:0..4294967295> no-transit <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 6 `；EOL ` RVA 0x3567DD10 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value。

[条件 C-33bfc65a49764b25](../../evidence/conditions-sets-020.md#c-33bfc65a49764b25) · [参数 P-82248a455979973d](../../evidence/parameters-sets-010.md#p-82248a455979973d) · [状态效果 S-4a3b32c1bd7fad6c](../../evidence/state_effects-sets-016.md#s-4a3b32c1bd7fad6c)

### observed_connections-000702

```text
(config-router)# default area <number:0..4294967295> normal <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 5 `；EOL ` RVA 0x3567E0D0 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value。

[条件 C-0756d675c9fc6105](../../evidence/conditions-sets-003.md#c-0756d675c9fc6105) · [参数 P-82248a455979973d](../../evidence/parameters-sets-010.md#p-82248a455979973d) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000730

```text
(config-router)# default area <number:0..4294967295> nssa <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 3 `；EOL ` RVA 0x3567E9D8 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value。

[条件 C-da8fa23073125254](../../evidence/conditions-sets-084.md#c-da8fa23073125254) · [参数 P-82248a455979973d](../../evidence/parameters-sets-010.md#p-82248a455979973d) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000686

```text
(config-router)# default area <number:0..4294967295> packet-size <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 14 `；EOL ` RVA 0x3567DA88 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value。

[条件 C-8b7e330a1076da54](../../evidence/conditions-sets-054.md#c-8b7e330a1076da54) · [参数 P-82248a455979973d](../../evidence/parameters-sets-010.md#p-82248a455979973d) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000860

```text
(config-router)# default area <number:0..4294967295> range <address> <address> <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 2 `；EOL ` RVA 0x3567F058 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value；` address ` IPv4 address to match；` address ` IPv4 mask for address。

[条件 C-5829a63832813ba0](../../evidence/conditions-sets-035.md#c-5829a63832813ba0) · [参数 P-9bb51a77902c1f8a](../../evidence/parameters-sets-012.md#p-9bb51a77902c1f8a) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000865

```text
(config-router)# default area <number:0..4294967295> sham-link <address> <address> <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 12 `；EOL ` RVA 0x3568F978 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value；` address ` IPv6 address associated with sham-link source；` address ` IPv6 address associated with sham-link destination。

[条件 C-8f6322e6213fb3a3](../../evidence/conditions-sets-056.md#c-8f6322e6213fb3a3) · [参数 P-64334b8cba0d93ae](../../evidence/parameters-sets-008.md#p-64334b8cba0d93ae) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000716

```text
(config-router)# default area <number:0..4294967295> stub <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 4 `；EOL ` RVA 0x3567E430 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value。

[条件 C-e4ea43482183fde0](../../evidence/conditions-sets-088.md#c-e4ea43482183fde0) · [参数 P-82248a455979973d](../../evidence/parameters-sets-010.md#p-82248a455979973d) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000823

```text
(config-router)# default area <number:0..4294967295> virtual-link <address> <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 1 `；EOL ` RVA 0x3568EA90 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value；` address ` RouterID associated with virtual link neighbor。

[条件 C-613d9b06f1b79756](../../evidence/conditions-sets-038.md#c-613d9b06f1b79756) · [参数 P-c0370be301cc44d7](../../evidence/parameters-sets-015.md#p-c0370be301cc44d7) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000191

```text
(config-router)# default area-password <cr>
```

Handler ` RVA 0xFD324F0 `；selector ` 16 `；EOL ` RVA 0x34B882A8 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6aa5acf11bb026e2](../../evidence/conditions-sets-041.md#c-6aa5acf11bb026e2) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000723

```text
(config-router)# default authentication key-chain <string> <cr>
```

Handler ` RVA 0xFD324F0 `；selector ` 19 `；EOL ` RVA 0x34B88E88 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Name of key-chain。

[条件 C-d320464e5add632e](../../evidence/conditions-sets-081.md#c-d320464e5add632e) · [参数 P-fce79716c6cb8231](../../evidence/parameters-sets-019.md#p-fce79716c6cb8231) · [状态效果 S-3c3e7b23510736cf](../../evidence/state_effects-sets-013.md#s-3c3e7b23510736cf)

### observed_connections-000721

```text
(config-router)# default authentication mode md5 <cr>
```

Handler ` RVA 0xFD324F0 `；selector ` 18 `；EOL ` RVA 0x34B889D8 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ebd7ed1765266083](../../evidence/conditions-sets-091.md#c-ebd7ed1765266083) · [状态效果 S-3661653af8fce366](../../evidence/state_effects-sets-012.md#s-3661653af8fce366)

### observed_connections-000741

```text
(config-router)# default authentication mode strict <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 31 `；EOL ` RVA 0x356852E0 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6093751694b20f29](../../evidence/conditions-sets-038.md#c-6093751694b20f29) · [状态效果 S-fe6d60197f4f308c](../../evidence/state_effects-sets-054.md#s-fe6d60197f4f308c)

### observed_connections-000524

```text
(config-router)# default authentication send-only <cr>
```

Handler ` RVA 0xFD324F0 `；selector ` 20 `；EOL ` RVA 0x34B89218 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d320464e5add632e](../../evidence/conditions-sets-081.md#c-d320464e5add632e) · [状态效果 S-52e2a855a0c72b3f](../../evidence/state_effects-sets-018.md#s-52e2a855a0c72b3f)

### observed_connections-000156

```text
(config-router)# default auto-cost <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 0 `；EOL ` RVA 0x34886C40 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-94a7180cc2a0954e](../../evidence/conditions-sets-057.md#c-94a7180cc2a0954e) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000245

```text
(config-router)# default auto-cost <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 0 `；EOL ` RVA 0x35683E20 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1beab640885d026c](../../evidence/conditions-sets-011.md#c-1beab640885d026c) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000206

```text
(config-router)# default auto-summary <cr>
```

Handler ` RVA 0xE1FA6B0 `；selector ` 0 `；EOL ` RVA 0x34257468 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-dfc9b807534948c3](../../evidence/conditions-sets-086.md#c-dfc9b807534948c3) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000256

```text
(config-router)# default autoroute-exclude <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 48 `；EOL ` RVA 0x348947F8 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f82c231deab65e2a](../../evidence/conditions-sets-096.md#c-f82c231deab65e2a) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000472

```text
(config-router)# default bfd all-interfaces <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 20 `；EOL ` RVA 0x3567A168 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b37999daad8cb800](../../evidence/conditions-sets-069.md#c-b37999daad8cb800) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000503

```text
(config-router)# default bfd check-ctrl-plane-failure <cr>
```

Handler ` RVA 0xE1FA610 `；selector ` 0 `；EOL ` RVA 0x34256F50 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-aa5ec25db4a05959](../../evidence/conditions-sets-066.md#c-aa5ec25db4a05959) · [状态效果 S-c77ed14a1495ad18](../../evidence/state_effects-sets-042.md#s-c77ed14a1495ad18)

### observed_connections-000675

```text
(config-router)# default bgp additional-paths install <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 69 `；EOL ` RVA 0x344D7E18 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ac9fbf82cf234df3](../../evidence/conditions-sets-067.md#c-ac9fbf82cf234df3) · [状态效果 S-f250f9414599db4a](../../evidence/state_effects-sets-051.md#s-f250f9414599db4a)

### observed_connections-000692

```text
(config-router)# default bgp additional-paths select <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 71 `；EOL ` RVA 0x344D7AC0 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c25c0eae29e38b9b](../../evidence/conditions-sets-075.md#c-c25c0eae29e38b9b) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000403

```text
(config-router)# default bgp advertise-best-external <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 70 `；EOL ` RVA 0x344D8C68 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0aa0ca38535d7e8f](../../evidence/conditions-sets-004.md#c-0aa0ca38535d7e8f) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000539

```text
(config-router)# default bgp advertisement startup-delay <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 95 `；EOL ` RVA 0x344D5480 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-28fc7961706462a6](../../evidence/conditions-sets-016.md#c-28fc7961706462a6) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000694

```text
(config-router)# default bgp aggregate-timer <number:6..60> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 58 `；EOL ` RVA 0x344DECB8 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Timer interval。

[条件 C-e17ed17447bf4f15](../../evidence/conditions-sets-087.md#c-e17ed17447bf4f15) · [参数 P-1e21d132041b5c35](../../evidence/parameters-sets-003.md#p-1e21d132041b5c35) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000586

```text
(config-router)# default bgp aigp-rib-metric <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 91 `；EOL ` RVA 0x344FF8E8 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d8e7f4b3ece00a9c](../../evidence/conditions-sets-083.md#c-d8e7f4b3ece00a9c) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000382

```text
(config-router)# default bgp always-compare-med <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 5 `；EOL ` RVA 0x344D0D68 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-64ac03fc4a2fa258](../../evidence/conditions-sets-039.md#c-64ac03fc4a2fa258) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000658

```text
(config-router)# default bgp asnotation dot <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 64 `；EOL ` RVA 0x344D1078 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-64ac03fc4a2fa258](../../evidence/conditions-sets-039.md#c-64ac03fc4a2fa258) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000834

```text
(config-router)# default bgp bestpath aigp ignore <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 43 `；EOL ` RVA 0x344FE610 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-429806c5c1eb838e](../../evidence/conditions-sets-026.md#c-429806c5c1eb838e) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000826

```text
(config-router)# default bgp bestpath as-path ignore <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 17 `；EOL ` RVA 0x344FDD80 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d8e7f4b3ece00a9c](../../evidence/conditions-sets-083.md#c-d8e7f4b3ece00a9c) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000829

```text
(config-router)# default bgp bestpath as-path multipath-relax <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 51 `；EOL ` RVA 0x344FE028 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d8e7f4b3ece00a9c](../../evidence/conditions-sets-083.md#c-d8e7f4b3ece00a9c) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000759

```text
(config-router)# default bgp bestpath compare-routerid <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 24 `；EOL ` RVA 0x344FE2C0 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d8e7f4b3ece00a9c](../../evidence/conditions-sets-083.md#c-d8e7f4b3ece00a9c) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000833

```text
(config-router)# default bgp bestpath cost-community ignore <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 41 `；EOL ` RVA 0x344FE8E8 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d8e7f4b3ece00a9c](../../evidence/conditions-sets-083.md#c-d8e7f4b3ece00a9c) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000780

```text
(config-router)# default bgp bestpath igp-metric ignore <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 42 `；EOL ` RVA 0x344D8348 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d991eb087fde87d6](../../evidence/conditions-sets-084.md#c-d991eb087fde87d6) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000830

```text
(config-router)# default bgp bestpath med missing-as-worst <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 18 `；EOL ` RVA 0x344FDA70 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d8e7f4b3ece00a9c](../../evidence/conditions-sets-083.md#c-d8e7f4b3ece00a9c) · [状态效果 S-8696519a11deeca1](../../evidence/state_effects-sets-029.md#s-8696519a11deeca1)

### observed_connections-000785

```text
(config-router)# default bgp bestpath prefix-validate allow-invalid <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 78 `；EOL ` RVA 0x344D8658 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1dee027f507a8808](../../evidence/conditions-sets-012.md#c-1dee027f507a8808) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000790

```text
(config-router)# default bgp bestpath prefix-validate disable <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 77 `；EOL ` RVA 0x344D8900 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1dee027f507a8808](../../evidence/conditions-sets-012.md#c-1dee027f507a8808) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000684

```text
(config-router)# default bgp client-to-client reflection <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 9 `；EOL ` RVA 0x344D1F08 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-47cc66e217ba6921](../../evidence/conditions-sets-028.md#c-47cc66e217ba6921) · [状态效果 S-6bff6852f8d7066c](../../evidence/state_effects-sets-023.md#s-6bff6852f8d7066c)

### observed_connections-000455

```text
(config-router)# default bgp cluster-id <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 7 `；EOL ` RVA 0x344D1AD0 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-378eb5be272ce0b3](../../evidence/conditions-sets-022.md#c-378eb5be272ce0b3) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000473

```text
(config-router)# default bgp consistency-checker <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 3 `；EOL ` RVA 0x344D1450 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9ad20451116826d1](../../evidence/conditions-sets-060.md#c-9ad20451116826d1) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000384

```text
(config-router)# default bgp dampening <cr>
```

Handler ` RVA 0xF1B85B0 `；selector ` 0 `；EOL ` RVA 0x344D6EE0 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-059f8fa3309a989a](../../evidence/conditions-sets-003.md#c-059f8fa3309a989a) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000782

```text
(config-router)# default bgp default inter-as-hybrid advertise-source-routes <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 57 `；EOL ` RVA 0x344D6518 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-81b58dd2cbd358f4](../../evidence/conditions-sets-050.md#c-81b58dd2cbd358f4) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000637

```text
(config-router)# default bgp default ipv4-unicast <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 19 `；EOL ` RVA 0x344D5C70 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f2ea3e11587f1d00](../../evidence/conditions-sets-094.md#c-f2ea3e11587f1d00) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000643

```text
(config-router)# default bgp default ipv6-nexthop <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 75 `；EOL ` RVA 0x344D5F68 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-529ce920fc162503](../../evidence/conditions-sets-032.md#c-529ce920fc162503) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000386

```text
(config-router)# default bgp default local-preference <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 0 `；EOL ` RVA 0x344D61F8 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f056381385aef411](../../evidence/conditions-sets-093.md#c-f056381385aef411) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000776

```text
(config-router)# default bgp default route-target filter <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 25 `；EOL ` RVA 0x344D6880 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7c5541307ffb6273](../../evidence/conditions-sets-048.md#c-7c5541307ffb6273) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000777

```text
(config-router)# default bgp default route-target filter <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 25 `；EOL ` RVA 0x344D6B20 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8e6e17167ac37ffa](../../evidence/conditions-sets-055.md#c-8e6e17167ac37ffa) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000504

```text
(config-router)# default bgp deterministic-med <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 10 `；EOL ` RVA 0x344D3588 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-64ac03fc4a2fa258](../../evidence/conditions-sets-039.md#c-64ac03fc4a2fa258) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000446

```text
(config-router)# default bgp dmzlink-bw <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 31 `；EOL ` RVA 0x344DA218 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9541beb5318b281b](../../evidence/conditions-sets-058.md#c-9541beb5318b281b) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000220

```text
(config-router)# default bgp dynamic-med-interval <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 21 `；EOL ` RVA 0x344D35B0 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-383b50c3c341632b](../../evidence/conditions-sets-022.md#c-383b50c3c341632b) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000462

```text
(config-router)# default bgp enforce-first-as <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 20 `；EOL ` RVA 0x344D27B8 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-64ac03fc4a2fa258](../../evidence/conditions-sets-039.md#c-64ac03fc4a2fa258) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000547

```text
(config-router)# default bgp enhanced-error <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 82 `；EOL ` RVA 0x344D51F8 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c468c124bf4916aa](../../evidence/conditions-sets-076.md#c-c468c124bf4916aa) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000358

```text
(config-router)# default bgp fast-external-fallover <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 1 `；EOL ` RVA 0x344D04A0 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-64ac03fc4a2fa258](../../evidence/conditions-sets-039.md#c-64ac03fc4a2fa258) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000568

```text
(config-router)# default bgp graceful-restart <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 35 `；EOL ` RVA 0x344FBA50 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-64ac03fc4a2fa258](../../evidence/conditions-sets-039.md#c-64ac03fc4a2fa258) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000554

```text
(config-router)# default bgp graceful-restart restart-time <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 36 `；EOL ` RVA 0x344FB420 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-83950d49091b748c](../../evidence/conditions-sets-051.md#c-83950d49091b748c) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000558

```text
(config-router)# default bgp graceful-restart stalepath-time <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 37 `；EOL ` RVA 0x344FB488 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-99d6f079e95363bc](../../evidence/conditions-sets-059.md#c-99d6f079e95363bc) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000867

```text
(config-router)# default bgp graceful-shutdown all vrfs activate <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 79 `；EOL ` RVA 0x344FBEB8 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-491cf7fd66a513cc](../../evidence/conditions-sets-029.md#c-491cf7fd66a513cc) · [状态效果 S-e63872904bf361ef](../../evidence/state_effects-sets-049.md#s-e63872904bf361ef)

### observed_connections-000744

```text
(config-router)# default bgp ha-mode sso <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 83 `；EOL ` RVA 0x3372E840 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-155396da89bd2248](../../evidence/conditions-sets-008.md#c-155396da89bd2248) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000857

```text
(config-router)# default bgp inject-map <string> exist-map <string> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 32 `；EOL ` RVA 0x344DBD90 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` route-map name；` string ` route-map name。

[条件 C-c8f87fd8a243e819](../../evidence/conditions-sets-077.md#c-c8f87fd8a243e819) · [参数 P-5b20d3d4cbc8fc0d](../../evidence/parameters-sets-007.md#p-5b20d3d4cbc8fc0d) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000775

```text
(config-router)# default bgp label-allocation-batch <number:0..4294967295> <number:0..4294967295> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 53 `；EOL ` RVA 0x344D0830 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Timer value in milliseconds；` unsigned_number ` Batch Size。

[条件 C-64ac03fc4a2fa258](../../evidence/conditions-sets-039.md#c-64ac03fc4a2fa258) · [参数 P-e29c6d656430799f](../../evidence/parameters-sets-017.md#p-e29c6d656430799f) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000805

```text
(config-router)# default bgp listen block <address> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 93 `；EOL ` RVA 0x344D9C28 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IPv4 Dynamic Peering Address。

[条件 C-dbffccb945e1d51c](../../evidence/conditions-sets-085.md#c-dbffccb945e1d51c) · [参数 P-68f33430087a596b](../../evidence/parameters-sets-008.md#p-68f33430087a596b) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000820

```text
(config-router)# default bgp listen block <address> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 93 `；EOL ` RVA 0x344D4530 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IPv4 Dynamic Peering Address。

[条件 C-e40f970c215acb98](../../evidence/conditions-sets-088.md#c-e40f970c215acb98) · [参数 P-31e77b4f9b27b0d8](../../evidence/parameters-sets-004.md#p-31e77b4f9b27b0d8) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000483

```text
(config-router)# default bgp listen limit <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 61 `；EOL ` RVA 0x344D9B70 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-82e81262d46f775e](../../evidence/conditions-sets-051.md#c-82e81262d46f775e) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000548

```text
(config-router)# default bgp listen limit <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 61 `；EOL ` RVA 0x344D4450 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7a5c875ff32aeca6](../../evidence/conditions-sets-047.md#c-7a5c875ff32aeca6) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000737

```text
(config-router)# default bgp listen persistent <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 94 `；EOL ` RVA 0x344D4868 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e40f970c215acb98](../../evidence/conditions-sets-088.md#c-e40f970c215acb98) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000479

```text
(config-router)# default bgp log-neighbor-changes <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 11 `；EOL ` RVA 0x344D2A60 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-64ac03fc4a2fa258](../../evidence/conditions-sets-039.md#c-64ac03fc4a2fa258) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000592

```text
(config-router)# default bgp maxas-limit <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 26 `；EOL ` RVA 0x344FF660 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0264cad87242264e](../../evidence/conditions-sets-001.md#c-0264cad87242264e) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000578

```text
(config-router)# default bgp maxcommunity-limit <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 27 `；EOL ` RVA 0x344FEC70 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-cc5cd22d53d222e6](../../evidence/conditions-sets-079.md#c-cc5cd22d53d222e6) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000587

```text
(config-router)# default bgp maxextcommunity-limit <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 29 `；EOL ` RVA 0x344FF310 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-275dd2dcf65a146c](../../evidence/conditions-sets-015.md#c-275dd2dcf65a146c) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000583

```text
(config-router)# default bgp maxlargecommunity-limit <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 28 `；EOL ` RVA 0x344FEFC0 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-459c8ae47f03e497](../../evidence/conditions-sets-027.md#c-459c8ae47f03e497) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000528

```text
(config-router)# default bgp mpls-local-label <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 81 `；EOL ` RVA 0x344DC108 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b623378aebd31bce](../../evidence/conditions-sets-070.md#c-b623378aebd31bce) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000807

```text
(config-router)# default bgp nexthop route-map <string> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 56 `；EOL ` RVA 0x344DA980 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` route-map name。

[条件 C-cc63c701ccfa00a9](../../evidence/conditions-sets-079.md#c-cc63c701ccfa00a9) · [参数 P-b7fdbd999a56cccb](../../evidence/parameters-sets-014.md#p-b7fdbd999a56cccb) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000717

```text
(config-router)# default bgp nexthop trigger critical-delay <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 48 `；EOL ` RVA 0x344DAEE8 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-66396fd9ed9000b9](../../evidence/conditions-sets-039.md#c-66396fd9ed9000b9) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000710

```text
(config-router)# default bgp nexthop trigger delay <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 47 `；EOL ` RVA 0x344DAC68 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-87ba72aec3ac8bf4](../../evidence/conditions-sets-052.md#c-87ba72aec3ac8bf4) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000804

```text
(config-router)# default bgp nexthop trigger enable <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 49 `；EOL ` RVA 0x344DAC40 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4bbac4809370bed7](../../evidence/conditions-sets-030.md#c-4bbac4809370bed7) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000816

```text
(config-router)# default bgp nopeerup-delay cold-boot <number:1..3600> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 74 `；EOL ` RVA 0x344D4E90 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Delay in seconds。

[条件 C-e11b57e562cf8a08](../../evidence/conditions-sets-087.md#c-e11b57e562cf8a08) · [参数 P-8c48ec9f765274d0](../../evidence/parameters-sets-011.md#p-8c48ec9f765274d0) · [状态效果 S-7694cb0923a644a0](../../evidence/state_effects-sets-025.md#s-7694cb0923a644a0)

### observed_connections-000667

```text
(config-router)# default bgp recursion host <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 72 `；EOL ` RVA 0x344D8FE0 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d98c72b0fe073701](../../evidence/conditions-sets-084.md#c-d98c72b0fe073701) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000404

```text
(config-router)# default bgp redistribute-internal <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 2 `；EOL ` RVA 0x344DD308 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-bce48006f0ed90c0](../../evidence/conditions-sets-073.md#c-bce48006f0ed90c0) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000753

```text
(config-router)# default bgp refresh max-eor-time <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 16 `；EOL ` RVA 0x344FCC48 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-947353e0bfb04690](../../evidence/conditions-sets-057.md#c-947353e0bfb04690) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000749

```text
(config-router)# default bgp refresh stalepath-time <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 15 `；EOL ` RVA 0x344FC8D8 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c464f2fce3c36811](../../evidence/conditions-sets-076.md#c-c464f2fce3c36811) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000751

```text
(config-router)# default bgp regexp deterministic <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 44 `；EOL ` RVA 0x344FD660 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d8e7f4b3ece00a9c](../../evidence/conditions-sets-083.md#c-d8e7f4b3ece00a9c) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000668

```text
(config-router)# default bgp route-map priority <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 59 `；EOL ` RVA 0x344DE498 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3197f81b43032438](../../evidence/conditions-sets-019.md#c-3197f81b43032438) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000374

```text
(config-router)# default bgp route-map-cache <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 34 `；EOL ` RVA 0x344D0AB8 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-64ac03fc4a2fa258](../../evidence/conditions-sets-039.md#c-64ac03fc4a2fa258) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000385

```text
(config-router)# default bgp router-id <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 4 `；EOL ` RVA 0x344CFE70 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-78dba1aee74242a6](../../evidence/conditions-sets-047.md#c-78dba1aee74242a6) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000490

```text
(config-router)# default bgp router-id <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 4 `；EOL ` RVA 0x344D9690 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-51e307c213717775](../../evidence/conditions-sets-032.md#c-51e307c213717775) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000877

```text
(config-router)# default bgp rpki server tcp <address> port <number:1..65535> refresh <number:1..65535> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 76 `；EOL ` RVA 0x344DF2B0 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IPv6 address of RPKI cache server；` unsigned_number ` Port number；` unsigned_number ` Refresh time in seconds。

[条件 C-5febe211e9716279](../../evidence/conditions-sets-037.md#c-5febe211e9716279) · [参数 P-4a188ed7711f531c](../../evidence/parameters-sets-006.md#p-4a188ed7711f531c) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000511

```text
(config-router)# default bgp rr-group <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 23 `；EOL ` RVA 0x344DB928 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d7405223ef555db8](../../evidence/conditions-sets-083.md#c-d7405223ef555db8) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000595

```text
(config-router)# default bgp safe-ebgp-policy <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 92 `；EOL ` RVA 0x344FFBD0 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e43c8b205f2ad28a](../../evidence/conditions-sets-088.md#c-e43c8b205f2ad28a) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000713

```text
(config-router)# default bgp scan-time <number:5..60> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 22 `；EOL ` RVA 0x344DB5B8 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Scanner interval (seconds)。

[条件 C-794d044414bb19c5](../../evidence/conditions-sets-047.md#c-794d044414bb19c5) · [参数 P-874d7de800ad4c96](../../evidence/parameters-sets-010.md#p-874d7de800ad4c96) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000670

```text
(config-router)# default bgp slow-peer detection <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 67 `；EOL ` RVA 0x344DC5D8 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d0cb6df1edd5ff6d](../../evidence/conditions-sets-080.md#c-d0cb6df1edd5ff6d) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000791

```text
(config-router)# default bgp slow-peer split-update-group dynamic <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 68 `；EOL ` RVA 0x344DCBA8 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a821010eeb2d50f5](../../evidence/conditions-sets-065.md#c-a821010eeb2d50f5) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000810

```text
(config-router)# default bgp snmp traps add-type <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 90 `；EOL ` RVA 0x344D3B78 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-64ac03fc4a2fa258](../../evidence/conditions-sets-039.md#c-64ac03fc4a2fa258) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000480

```text
(config-router)# default bgp soft-reconfig-backup <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 52 `；EOL ` RVA 0x344DA568 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-fb214f36bef7fbc3](../../evidence/conditions-sets-097.md#c-fb214f36bef7fbc3) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000855

```text
(config-router)# default bgp sourced-paths per-net isis all <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 89 `；EOL ` RVA 0x344DE118 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-265131b45ecc5879](../../evidence/conditions-sets-015.md#c-265131b45ecc5879) · [状态效果 S-b4f98ce54d5858f9](../../evidence/state_effects-sets-038.md#s-b4f98ce54d5858f9)

### observed_connections-000849

```text
(config-router)# default bgp sourced-paths per-net ospf all <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 87 `；EOL ` RVA 0x344DDAB8 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-265131b45ecc5879](../../evidence/conditions-sets-015.md#c-265131b45ecc5879) · [状态效果 S-464bf541493194a2](../../evidence/state_effects-sets-015.md#s-464bf541493194a2)

### observed_connections-000852

```text
(config-router)# default bgp sourced-paths per-net ospfv3 all <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 88 `；EOL ` RVA 0x344DDE00 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-265131b45ecc5879](../../evidence/conditions-sets-015.md#c-265131b45ecc5879) · [状态效果 S-1be2f0d6fac576b0](../../evidence/state_effects-sets-006.md#s-1be2f0d6fac576b0)

### observed_connections-000847

```text
(config-router)# default bgp sourced-paths per-net static all <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 86 `；EOL ` RVA 0x344DD770 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-265131b45ecc5879](../../evidence/conditions-sets-015.md#c-265131b45ecc5879) · [状态效果 S-71def6ebc90e719d](../../evidence/state_effects-sets-024.md#s-71def6ebc90e719d)

### observed_connections-000738

```text
(config-router)# default bgp sso route-refresh-enable <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 38 `；EOL ` RVA 0x344FC518 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d8e7f4b3ece00a9c](../../evidence/conditions-sets-083.md#c-d8e7f4b3ece00a9c) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000419

```text
(config-router)# default bgp suppress-inactive <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 45 `；EOL ` RVA 0x344D92E0 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b766a61000b7d48b](../../evidence/conditions-sets-071.md#c-b766a61000b7d48b) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000077

```text
(config-router)# default bgp tid <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 55 `；EOL ` RVA 0x344CF6B0 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6f4b93226fc5c4c1](../../evidence/conditions-sets-043.md#c-6f4b93226fc5c4c1) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000680

```text
(config-router)# default bgp transport path-mtu-discovery <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 50 `；EOL ` RVA 0x344D2528 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-64ac03fc4a2fa258](../../evidence/conditions-sets-039.md#c-64ac03fc4a2fa258) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000254

```text
(config-router)# default bgp update-delay <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 30 `；EOL ` RVA 0x344D54A8 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1ea9be6fd3359bfa](../../evidence/conditions-sets-012.md#c-1ea9be6fd3359bfa) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000783

```text
(config-router)# default bgp update-group split as-override <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 73 `；EOL ` RVA 0x344DCF78 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2f7cc0c0004615a7](../../evidence/conditions-sets-019.md#c-2f7cc0c0004615a7) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000370

```text
(config-router)# default bgp upgrade-cli <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 33 `；EOL ` RVA 0x344CFAC8 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a96fcf0a2319bbf7](../../evidence/conditions-sets-065.md#c-a96fcf0a2319bbf7) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000466

```text
(config-router)# default bgp va <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 80 `；EOL ` RVA 0x344DE840 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-acfbd7e8a3346d19](../../evidence/conditions-sets-067.md#c-acfbd7e8a3346d19) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000747

```text
(config-router)# default bgp vrf-update-optimisation off <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 66 `；EOL ` RVA 0x344FCFD0 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d8e7f4b3ece00a9c](../../evidence/conditions-sets-083.md#c-d8e7f4b3ece00a9c) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000571

```text
(config-router)# default bgp write-limit <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 40 `；EOL ` RVA 0x344FD328 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-70688c87f1e0d670](../../evidence/conditions-sets-043.md#c-70688c87f1e0d670) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000546

```text
(config-router)# default capability opaque <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 4 `；EOL ` RVA 0x34894378 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-88acc362b84bd124](../../evidence/conditions-sets-053.md#c-88acc362b84bd124) · [状态效果 S-29a2868e9d8f1ae9](../../evidence/state_effects-sets-009.md#s-29a2868e9d8f1ae9)

### observed_connections-000557

```text
(config-router)# default capability vrf-lite <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 7 `；EOL ` RVA 0x35684EE8 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-24d0b108f11123ba](../../evidence/conditions-sets-014.md#c-24d0b108f11123ba) · [状态效果 S-a05e4ea9f62cca85](../../evidence/state_effects-sets-034.md#s-a05e4ea9f62cca85)

### observed_connections-000380

```text
(config-router)# default compatible rfc1583 <cr>
```

Handler ` RVA 0xFC6DF20 `；selector ` 6 `；EOL ` RVA 0x34884168 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-89e1cc66ca5c3c37](../../evidence/conditions-sets-053.md#c-89e1cc66ca5c3c37) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000427

```text
(config-router)# default compatible rfc1583 <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 25 `；EOL ` RVA 0x3567A568 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-725b2f0362370d98](../../evidence/conditions-sets-044.md#c-725b2f0362370d98) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000401

```text
(config-router)# default compatible rfc1587 <cr>
```

Handler ` RVA 0xFC6DF20 `；selector ` 7 `；EOL ` RVA 0x34884478 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-957ae969613136d1](../../evidence/conditions-sets-058.md#c-957ae969613136d1) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000442

```text
(config-router)# default compatible rfc1587 <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 26 `；EOL ` RVA 0x3567A860 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2267723558a951c2](../../evidence/conditions-sets-013.md#c-2267723558a951c2) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000418

```text
(config-router)# default compatible rfc5243 <cr>
```

Handler ` RVA 0xFC6DF20 `；selector ` 8 `；EOL ` RVA 0x34884748 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-93db37c576c8c4dc](../../evidence/conditions-sets-057.md#c-93db37c576c8c4dc) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000461

```text
(config-router)# default compatible rfc5243 <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 27 `；EOL ` RVA 0x3567AB30 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3be5f0f80ef64898](../../evidence/conditions-sets-023.md#c-3be5f0f80ef64898) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000074

```text
(config-router)# default context <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 0 `；EOL ` RVA 0x33C44A60 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ada418e0516d363b](../../evidence/conditions-sets-067.md#c-ada418e0516d363b) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000497

```text
(config-router)# default default-information originate <cr>
```

Handler ` RVA 0xE1F1F70 `；selector ` 0 `；EOL ` RVA 0x34254C70 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5aba8d29c2a2dc01](../../evidence/conditions-sets-036.md#c-5aba8d29c2a2dc01) · [状态效果 S-43257c2b704f5445](../../evidence/state_effects-sets-015.md#s-43257c2b704f5445)

### observed_connections-000199

```text
(config-router)# default default-metric <cr>
```

Handler ` RVA 0xE1F35A0 `；selector ` 0 `；EOL ` RVA 0x34255538 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-cc6872be30f1e076](../../evidence/conditions-sets-079.md#c-cc6872be30f1e076) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000532

```text
(config-router)# default discard-route external <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 11 `；EOL ` RVA 0x356839B8 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-38a7650107b27024](../../evidence/conditions-sets-022.md#c-38a7650107b27024) · [状态效果 S-01c24b921ec4f9be](../../evidence/state_effects-sets-001.md#s-01c24b921ec4f9be)

### observed_connections-000309

```text
(config-router)# default display-route-detail <cr>
```

Handler ` RVA 0xFD324F0 `；selector ` 41 `；EOL ` RVA 0x34B8F4C0 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d320464e5add632e](../../evidence/conditions-sets-081.md#c-d320464e5add632e) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000234

```text
(config-router)# default distance <cr>
```

Handler ` RVA 0xE1E3290 `；selector ` 1 `；EOL ` RVA 0x34256668 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0ccc7e3c99f594a8](../../evidence/conditions-sets-005.md#c-0ccc7e3c99f594a8) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000521

```text
(config-router)# default distance bgp <cr>
```

Handler ` RVA 0xF1B8400 `；selector ` 1 `；EOL ` RVA 0x344E1458 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-126038513ff31fca](../../evidence/conditions-sets-007.md#c-126038513ff31fca) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000535

```text
(config-router)# default distance mbgp <cr>
```

Handler ` RVA 0xF1B8400 `；selector ` 2 `；EOL ` RVA 0x344E1850 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d33fbaaaaddc9d7e](../../evidence/conditions-sets-081.md#c-d33fbaaaaddc9d7e) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000536

```text
(config-router)# default distance nhrp <cr>
```

Handler ` RVA 0x108B0C70 `；selector ` 1 `；EOL ` RVA 0x34BE80E0 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-54e1a604ef8f3e5b](../../evidence/conditions-sets-033.md#c-54e1a604ef8f3e5b) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000529

```text
(config-router)# default distance ospf <cr>
```

Handler ` RVA 0xFC6D2A0 `；selector ` 0 `；EOL ` RVA 0x3488EDD8 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2f72cab24d36fc7b](../../evidence/conditions-sets-019.md#c-2f72cab24d36fc7b) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000542

```text
(config-router)# default distance ospf <cr>
```

Handler ` RVA 0x11BCBF10 `；selector ` 0 `；EOL ` RVA 0x356594B8 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-adc699fb18bf6224](../../evidence/conditions-sets-067.md#c-adc699fb18bf6224) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000534

```text
(config-router)# default distribute-list in <cr>
```

Handler ` RVA 0xE1EE180 `；selector ` 0 `；EOL ` RVA 0x34255C28 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a8685a6e7d0c6d43](../../evidence/conditions-sets-065.md#c-a8685a6e7d0c6d43) · [状态效果 S-356871eb63431f31](../../evidence/state_effects-sets-012.md#s-356871eb63431f31)

### observed_connections-000148

```text
(config-router)# default domain-id <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 9 `；EOL ` RVA 0x34882B30 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0632cfbfc3cdf8ba](../../evidence/conditions-sets-003.md#c-0632cfbfc3cdf8ba) · [状态效果 S-2a2175e612aa4741](../../evidence/state_effects-sets-009.md#s-2a2175e612aa4741)

### observed_connections-000165

```text
(config-router)# default domain-id <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 9 `；EOL ` RVA 0x35678E68 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f549a2adfee30eeb](../../evidence/conditions-sets-095.md#c-f549a2adfee30eeb) · [状态效果 S-f0f66644c7c35a94](../../evidence/state_effects-sets-051.md#s-f0f66644c7c35a94)

### observed_connections-000183

```text
(config-router)# default domain-password <cr>
```

Handler ` RVA 0xFD324F0 `；selector ` 17 `；EOL ` RVA 0x34B87D38 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-066773791493a477](../../evidence/conditions-sets-003.md#c-066773791493a477) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000019

```text
(config-router)# default domain-tag <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 10 `；EOL ` RVA 0x34882A50 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f93a9432380f5ceb](../../evidence/conditions-sets-096.md#c-f93a9432380f5ceb) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000213

```text
(config-router)# default event-log <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 22 `；EOL ` RVA 0x34885870 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b2b19b77d066d241](../../evidence/conditions-sets-069.md#c-b2b19b77d066d241) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000241

```text
(config-router)# default event-log <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 19 `；EOL ` RVA 0x35683198 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-490803c624d0035c](../../evidence/conditions-sets-029.md#c-490803c624d0035c) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000230

```text
(config-router)# default fast-flood <cr>
```

Handler ` RVA 0xFD324F0 `；selector ` 51 `；EOL ` RVA 0x34B8A6D0 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-94af5d2bb68be62c](../../evidence/conditions-sets-057.md#c-94af5d2bb68be62c) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000033

```text
(config-router)# default flash-update-threshold <cr>
```

Handler ` RVA 0xE1F7ED0 `；selector ` 0 `；EOL ` RVA 0x34254760 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-29d36b004a445d7a](../../evidence/conditions-sets-016.md#c-29d36b004a445d7a) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000715

```text
(config-router)# default flood parallel suppression <cr>
```

Handler ` RVA 0xFD324F0 `；selector ` 52 `；EOL ` RVA 0x34B8A090 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d320464e5add632e](../../evidence/conditions-sets-081.md#c-d320464e5add632e) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000316

```text
(config-router)# default graceful-restart <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 22 `；EOL ` RVA 0x3569DA70 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-94abebb1e1370965](../../evidence/conditions-sets-057.md#c-94abebb1e1370965) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000598

```text
(config-router)# default graceful-restart helper <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 23 `；EOL ` RVA 0x3569DDF8 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4feff3abfdec660b](../../evidence/conditions-sets-031.md#c-4feff3abfdec660b) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000597

```text
(config-router)# default hello padding <cr>
```

Handler ` RVA 0xFD324F0 `；selector ` 32 `；EOL ` RVA 0x34B8ED88 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d320464e5add632e](../../evidence/conditions-sets-081.md#c-d320464e5add632e) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000582

```text
(config-router)# default hostname dynamic <cr>
```

Handler ` RVA 0xFD324F0 `；selector ` 37 `；EOL ` RVA 0x34B8EA20 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d320464e5add632e](../../evidence/conditions-sets-081.md#c-d320464e5add632e) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000661

```text
(config-router)# default ignore lsa mospf <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 3 `；EOL ` RVA 0x34884D80 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-89e1cc66ca5c3c37](../../evidence/conditions-sets-053.md#c-89e1cc66ca5c3c37) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000705

```text
(config-router)# default ignore lsa mospf <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 4 `；EOL ` RVA 0x356828B0 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1beab640885d026c](../../evidence/conditions-sets-011.md#c-1beab640885d026c) · [状态效果 S-dad669e9e33a10fc](../../evidence/state_effects-sets-046.md#s-dad669e9e33a10fc)

### observed_connections-000275

```text
(config-router)# default ignore-attached-bit <cr>
```

Handler ` RVA 0xFD324F0 `；selector ` 27 `；EOL ` RVA 0x34B8BB68 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d320464e5add632e](../../evidence/conditions-sets-081.md#c-d320464e5add632e) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000296

```text
(config-router)# default ignore-lsp-errors <cr>
```

Handler ` RVA 0xFD324F0 `；selector ` 34 `；EOL ` RVA 0x34B8E6D0 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d320464e5add632e](../../evidence/conditions-sets-081.md#c-d320464e5add632e) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000030

```text
(config-router)# default input-queue <cr>
```

Handler ` RVA 0xE1F8060 `；selector ` 0 `；EOL ` RVA 0x34254470 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-59b9b8e89e170543](../../evidence/conditions-sets-035.md#c-59b9b8e89e170543) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000388

```text
(config-router)# default interface-id snmp-if-index <cr>
```

Handler ` RVA 0xFC6E310 `；selector ` 0 `；EOL ` RVA 0x34884A48 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-89e1cc66ca5c3c37](../../evidence/conditions-sets-053.md#c-89e1cc66ca5c3c37) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000460

```text
(config-router)# default interface-id snmp-if-index <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 15 `；EOL ` RVA 0x3567AEC8 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1beab640885d026c](../../evidence/conditions-sets-011.md#c-1beab640885d026c) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000862

```text
(config-router)# default ip route priority high tag <cr>
```

Handler ` RVA 0xFD324F0 `；selector ` 66 `；EOL ` RVA 0x34B8AB90 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-351f5e0042b0f6f3](../../evidence/conditions-sets-021.md#c-351f5e0042b0f6f3) · [状态效果 S-7dc2a945da3de5bd](../../evidence/state_effects-sets-027.md#s-7dc2a945da3de5bd)

### observed_connections-000103

```text
(config-router)# default is-type <cr>
```

Handler ` RVA 0x1058D180 `；selector ` 0 `；EOL ` RVA 0x34B85FB0 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-bee74b8df555af8d](../../evidence/conditions-sets-074.md#c-bee74b8df555af8d) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000152

```text
(config-router)# default ispf <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 16 `；EOL ` RVA 0x34885018 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-89e1cc66ca5c3c37](../../evidence/conditions-sets-053.md#c-89e1cc66ca5c3c37) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000209

```text
(config-router)# default ispf <cr>
```

Handler ` RVA 0xFD324F0 `；selector ` 86 `；EOL ` RVA 0x34B89608 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f6813efdceeec175](../../evidence/conditions-sets-095.md#c-f6813efdceeec175) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000507

```text
(config-router)# default limit retransmissions <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 13 `；EOL ` RVA 0x34887940 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3f7fda91dc4bffe5](../../evidence/conditions-sets-025.md#c-3f7fda91dc4bffe5) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000565

```text
(config-router)# default limit retransmissions <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 14 `；EOL ` RVA 0x35684B60 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f7c09dde851bc86e](../../evidence/conditions-sets-096.md#c-f7c09dde851bc86e) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000293

```text
(config-router)# default local-rib-criteria <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 6 `；EOL ` RVA 0x35685D58 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7c77db41462fef9d](../../evidence/conditions-sets-048.md#c-7c77db41462fef9d) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000208

```text
(config-router)# default log-adjacency-changes <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 2 `；EOL ` RVA 0x34886008 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-89e1cc66ca5c3c37](../../evidence/conditions-sets-053.md#c-89e1cc66ca5c3c37) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000231

```text
(config-router)# default log-adjacency-changes <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 3 `；EOL ` RVA 0x35683638 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1beab640885d026c](../../evidence/conditions-sets-011.md#c-1beab640885d026c) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000315

```text
(config-router)# default log-adjacency-changes <cr>
```

Handler ` RVA 0xFD324F0 `；selector ` 36 `；EOL ` RVA 0x34B8F1B8 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9991793f2af77035](../../evidence/conditions-sets-059.md#c-9991793f2af77035) · [状态效果 S-7f33912b07b456e1](../../evidence/state_effects-sets-027.md#s-7f33912b07b456e1)

### observed_connections-000817

```text
(config-router)# default lsp queue priority high <cr>
```

Handler ` RVA 0xFD324F0 `；selector ` 81 `；EOL ` RVA 0x34B8AF70 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d320464e5add632e](../../evidence/conditions-sets-081.md#c-d320464e5add632e) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000222

```text
(config-router)# default lsp-fast-flooding <cr>
```

Handler ` RVA 0xFD324F0 `；selector ` 53 `；EOL ` RVA 0x34B8A390 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d320464e5add632e](../../evidence/conditions-sets-081.md#c-d320464e5add632e) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000327

```text
(config-router)# default lsp-full <cr>
```

Handler ` RVA 0xFD324F0 `；selector ` 74 `；EOL ` RVA 0x34B904F8 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2e434b376014cc66](../../evidence/conditions-sets-018.md#c-2e434b376014cc66) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000304

```text
(config-router)# default lsp-gen-interval <cr>
```

Handler ` RVA 0xFD324F0 `；selector ` 31 `；EOL ` RVA 0x34B8DFD0 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-972f39419892ce09](../../evidence/conditions-sets-058.md#c-972f39419892ce09) · [状态效果 S-d710be947098c814](../../evidence/state_effects-sets-046.md#s-d710be947098c814)

### observed_connections-000325

```text
(config-router)# default lsp-mtu <cr>
```

Handler ` RVA 0xFD324F0 `；selector ` 38 `；EOL ` RVA 0x34B901A0 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-336a09903715e631](../../evidence/conditions-sets-020.md#c-336a09903715e631) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000292

```text
(config-router)# default lsp-refresh-interval <cr>
```

Handler ` RVA 0xFD324F0 `；selector ` 43 `；EOL ` RVA 0x34B8D240 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-bce2626af8c43963](../../evidence/conditions-sets-073.md#c-bce2626af8c43963) · [状态效果 S-0fd95b95117f3f7d](../../evidence/state_effects-sets-004.md#s-0fd95b95117f3f7d)

### observed_connections-000114

```text
(config-router)# default max-area-addresses <cr>
```

Handler ` RVA 0xFD324F0 `；selector ` 45 `；EOL ` RVA 0x34B85760 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-75584a09dfc061f4](../../evidence/conditions-sets-046.md#c-75584a09dfc061f4) · [状态效果 S-8228d24f1f2f53cb](../../evidence/state_effects-sets-028.md#s-8228d24f1f2f53cb)

### observed_connections-000171

```text
(config-router)# default max-lsa <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 18 `；EOL ` RVA 0x34887000 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7ba8a7121ceb7441](../../evidence/conditions-sets-048.md#c-7ba8a7121ceb7441) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000259

```text
(config-router)# default max-lsa <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 1 `；EOL ` RVA 0x356841E0 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-48ee12b6961fb879](../../evidence/conditions-sets-029.md#c-48ee12b6961fb879) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000286

```text
(config-router)# default max-lsp-lifetime <cr>
```

Handler ` RVA 0xFD324F0 `；selector ` 42 `；EOL ` RVA 0x34B8CEB0 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4305330d5116c61d](../../evidence/conditions-sets-026.md#c-4305330d5116c61d) · [状态效果 S-2cc7e17bd2a1db56](../../evidence/state_effects-sets-010.md#s-2cc7e17bd2a1db56)

### observed_connections-000143

```text
(config-router)# default max-metric <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 13 `；EOL ` RVA 0x35679438 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-fffb0405b4e655ad](../../evidence/conditions-sets-099.md#c-fffb0405b4e655ad) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000086

```text
(config-router)# default max-metric intra-area <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 5 `；EOL ` RVA 0x34883380 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6c236630566ae6a5](../../evidence/conditions-sets-042.md#c-6c236630566ae6a5) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000142

```text
(config-router)# default max-metric intra-area <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 8 `；EOL ` RVA 0x35679358 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-19aed9c37a34ce89](../../evidence/conditions-sets-010.md#c-19aed9c37a34ce89) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000414

```text
(config-router)# default max-metric router-lsa <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 12 `；EOL ` RVA 0x348838A8 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-28d9afc9ed3f49f6](../../evidence/conditions-sets-016.md#c-28d9afc9ed3f49f6) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000451

```text
(config-router)# default maximum-paths per-prefix-distribution <cr>
```

Handler ` RVA 0xFC6D730 `；selector ` 0 `；EOL ` RVA 0x3488F310 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-daf1a1ae608cea05](../../evidence/conditions-sets-084.md#c-daf1a1ae608cea05) · [状态效果 S-595cf0876a400646](../../evidence/state_effects-sets-019.md#s-595cf0876a400646)

### observed_connections-000335

```text
(config-router)# default metric <cr>
```

Handler ` RVA 0xFD324F0 `；selector ` 89 `；EOL ` RVA 0x34B90DA0 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7b913d1eff403c6a](../../evidence/conditions-sets-048.md#c-7b913d1eff403c6a) · [状态效果 S-07c5328508efe3c0](../../evidence/state_effects-sets-002.md#s-07c5328508efe3c0)

### observed_connections-000364

```text
(config-router)# default metric holddown <cr>
```

Handler ` RVA 0xE1F32D0 `；selector ` 1 `；EOL ` RVA 0x34252DE0 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5aa4dd3ba27a4b59](../../evidence/conditions-sets-035.md#c-5aa4dd3ba27a4b59) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000110

```text
(config-router)# default metric maximum-hops <cr>
```

Handler ` RVA 0xE1F32D0 `；selector ` 2 `；EOL ` RVA 0x34252E08 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3bf67daa5744001f](../../evidence/conditions-sets-023.md#c-3bf67daa5744001f) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000413

```text
(config-router)# default metric weights <cr>
```

Handler ` RVA 0xE1F32D0 `；selector ` 0 `；EOL ` RVA 0x342533C8 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8e6bb3c970c244f1](../../evidence/conditions-sets-055.md#c-8e6bb3c970c244f1) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000218

```text
(config-router)# default metric-style <cr>
```

Handler ` RVA 0xFD324F0 `；selector ` 48 `；EOL ` RVA 0x34B89AD8 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2a8677662d775d26](../../evidence/conditions-sets-017.md#c-2a8677662d775d26) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000611

```text
(config-router)# default multi-part-tlv disable <cr>
```

Handler ` RVA 0xFD324F0 `；selector ` 148 `；EOL ` RVA 0x34B91BF0 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6320dcc464a32a59](../../evidence/conditions-sets-038.md#c-6320dcc464a32a59) · [状态效果 S-08b73d5682bf2f6b](../../evidence/state_effects-sets-002.md#s-08b73d5682bf2f6b)

### observed_connections-000111

```text
(config-router)# default multicast-intact <cr>
```

Handler ` RVA 0xFD324F0 `；selector ` 121 `；EOL ` RVA 0x34B86700 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d320464e5add632e](../../evidence/conditions-sets-081.md#c-d320464e5add632e) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000255

```text
(config-router)# default multicast-intact <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 49 `；EOL ` RVA 0x34894B00 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-94a7180cc2a0954e](../../evidence/conditions-sets-057.md#c-94a7180cc2a0954e) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000369

```text
(config-router)# default net <address> <cr>
```

Handler ` RVA 0x1058BD60 `；selector ` 0 `；EOL ` RVA 0x34B85AD8 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` Network entity title (NET)。

[条件 C-fb77614134868d61](../../evidence/conditions-sets-097.md#c-fb77614134868d61) · [参数 P-3bebc72df8ee109e](../../evidence/parameters-sets-005.md#p-3bebc72df8ee109e) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000257

```text
(config-router)# default never-set-attached-bit <cr>
```

Handler ` RVA 0xFD324F0 `；selector ` 28 `；EOL ` RVA 0x34B8B850 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d320464e5add632e](../../evidence/conditions-sets-081.md#c-d320464e5add632e) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000734

```text
(config-router)# default nhrp redirect interest <cr>
```

Handler ` RVA 0x108B1190 `；selector ` 19 `；EOL ` RVA 0x34BE7C48 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-34bc055dbb59a36d](../../evidence/conditions-sets-020.md#c-34bc055dbb59a36d) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000268

```text
(config-router)# default nsf <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 15 `；EOL ` RVA 0x348B1250 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-cdf8c915453f94d2](../../evidence/conditions-sets-079.md#c-cdf8c915453f94d2) · [状态效果 S-165a77b4824ae971](../../evidence/state_effects-sets-005.md#s-165a77b4824ae971)

### observed_connections-000768

```text
(config-router)# default nsf advertise holdtime <cr>
```

Handler ` RVA 0xFD324F0 `；selector ` 72 `；EOL ` RVA 0x33FCC490 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7894c75603a78cfa](../../evidence/conditions-sets-047.md#c-7894c75603a78cfa) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000605

```text
(config-router)# default nsf cisco <cr>
```

Handler ` RVA 0xFD324F0 `；selector ` 67 `；EOL ` RVA 0x33FCAF00 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-484d755f8f11ff34](../../evidence/conditions-sets-028.md#c-484d755f8f11ff34) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000607

```text
(config-router)# default nsf ietf <cr>
```

Handler ` RVA 0xFD324F0 `；selector ` 68 `；EOL ` RVA 0x33FCB1E0 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-484d755f8f11ff34](../../evidence/conditions-sets-028.md#c-484d755f8f11ff34) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000613

```text
(config-router)# default nsf interface <cr>
```

Handler ` RVA 0xFD324F0 `；selector ` 70 `；EOL ` RVA 0x33FCB838 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-27169ac6d88eebe5](../../evidence/conditions-sets-015.md#c-27169ac6d88eebe5) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000614

```text
(config-router)# default nsf interval <cr>
```

Handler ` RVA 0xFD324F0 `；selector ` 69 `；EOL ` RVA 0x33FCB520 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0f3c8c9aae56882f](../../evidence/conditions-sets-006.md#c-0f3c8c9aae56882f) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000765

```text
(config-router)# default nsf sync wait <cr>
```

Handler ` RVA 0xFD324F0 `；selector ` 92 `；EOL ` RVA 0x33FCBC90 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ce08819ebe86b001](../../evidence/conditions-sets-079.md#c-ce08819ebe86b001) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000616

```text
(config-router)# default nsf t3 <cr>
```

Handler ` RVA 0xFD324F0 `；selector ` 71 `；EOL ` RVA 0x33FCC070 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-bf594c558847071b](../../evidence/conditions-sets-074.md#c-bf594c558847071b) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000238

```text
(config-router)# default nsr <cr>
```

Handler ` RVA 0xDACC520 `；selector ` 14 `；EOL ` RVA 0x33FC94A0 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-94a7180cc2a0954e](../../evidence/conditions-sets-057.md#c-94a7180cc2a0954e) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000653

```text
(config-router)# default offset-list <number:0..99> in <cr>
```

Handler ` RVA 0xE1F1330 `；selector ` 0 `；EOL ` RVA 0x34251F40 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Access list of networks to apply offset (0 selects all networks)。

[条件 C-42fffe653e74bf6b](../../evidence/conditions-sets-026.md#c-42fffe653e74bf6b) · [参数 P-a571645a38661abf](../../evidence/parameters-sets-013.md#p-a571645a38661abf) · [状态效果 S-39aaf21307bc8d1f](../../evidence/state_effects-sets-013.md#s-39aaf21307bc8d1f)

### observed_connections-000195

```text
(config-router)# default omp-route-tag <cr>
```

Handler ` RVA 0xE1F7FD0 `；selector ` 0 `；EOL ` RVA 0x34257808 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-419ea8affe919e81](../../evidence/conditions-sets-026.md#c-419ea8affe919e81) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000015

```text
(config-router)# default output-delay <cr>
```

Handler ` RVA 0xE1F4590 `；selector ` 0 `；EOL ` RVA 0x34251998 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-10fd6630d64244ff](../../evidence/conditions-sets-007.md#c-10fd6630d64244ff) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000016

```text
(config-router)# default packet-size <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 50 `；EOL ` RVA 0x348824A8 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-638987074904c348](../../evidence/conditions-sets-039.md#c-638987074904c348) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000059

```text
(config-router)# default packet-size <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 41 `；EOL ` RVA 0x356856A8 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-629f8f30b8f22fc1](../../evidence/conditions-sets-038.md#c-629f8f30b8f22fc1) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000594

```text
(config-router)# default partition avoidance <cr>
```

Handler ` RVA 0xFD324F0 `；selector ` 40 `；EOL ` RVA 0x34B8F7A0 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d320464e5add632e](../../evidence/conditions-sets-081.md#c-d320464e5add632e) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000357

```text
(config-router)# default passive-interface default <cr>
```

Handler ` RVA 0xE1F3960 `；selector ` 0 `；EOL ` RVA 0x34251588 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4d9b0ceacde3e575](../../evidence/conditions-sets-030.md#c-4d9b0ceacde3e575) · [状态效果 S-435773af04c86eab](../../evidence/state_effects-sets-015.md#s-435773af04c86eab)

### observed_connections-000295

```text
(config-router)# default prc-interval <cr>
```

Handler ` RVA 0xFD324F0 `；selector ` 30 `；EOL ` RVA 0x34B8DAD0 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-435cf018eaae1c7a](../../evidence/conditions-sets-026.md#c-435cf018eaae1c7a) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000714

```text
(config-router)# default prefix-priority high route-map <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 28 `；EOL ` RVA 0x348886F0 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0879c777fb4b4eda](../../evidence/conditions-sets-004.md#c-0879c777fb4b4eda) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000172

```text
(config-router)# default prefix-suppression <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 28 `；EOL ` RVA 0x35679D18 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6a3e394242acd8c5](../../evidence/conditions-sets-041.md#c-6a3e394242acd8c5) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000207

```text
(config-router)# default prefix-suppression <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 27 `；EOL ` RVA 0x348889D0 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-94a7180cc2a0954e](../../evidence/conditions-sets-057.md#c-94a7180cc2a0954e) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000011

```text
(config-router)# default priority <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 19 `；EOL ` RVA 0x34882028 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-10b5afb4ba61ab77](../../evidence/conditions-sets-007.md#c-10b5afb4ba61ab77) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000157

```text
(config-router)# default priority <cr>
```

Handler ` RVA 0xFD324F0 `；selector ` 85 `；EOL ` RVA 0x34B86E90 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5b0af54a70ad603e](../../evidence/conditions-sets-036.md#c-5b0af54a70ad603e) · [状态效果 S-fac1f19b061aabc5](../../evidence/state_effects-sets-053.md#s-fac1f19b061aabc5)

### observed_connections-000181

```text
(config-router)# default process-min-time percent <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 21 `；EOL ` RVA 0x34887C50 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-49cf6635b5edd144](../../evidence/conditions-sets-029.md#c-49cf6635b5edd144) · [状态效果 S-f05897896e208a92](../../evidence/state_effects-sets-051.md#s-f05897896e208a92)

### observed_connections-000284

```text
(config-router)# default process-min-time percent <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 16 `；EOL ` RVA 0x35686420 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-128da7de5515f0ce](../../evidence/conditions-sets-007.md#c-128da7de5515f0ce) · [状态效果 S-ee2cda24a5645a40](../../evidence/state_effects-sets-050.md#s-ee2cda24a5645a40)

### observed_connections-000319

```text
(config-router)# default psnp-interval <cr>
```

Handler ` RVA 0xFD324F0 `；selector ` 64 `；EOL ` RVA 0x34B8FAF8 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d0e154f8d3204c23](../../evidence/conditions-sets-080.md#c-d0e154f8d3204c23) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000491

```text
(config-router)# default purge-transmit strict <cr>
```

Handler ` RVA 0xFD324F0 `；selector ` 118 `；EOL ` RVA 0x34B87960 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d320464e5add632e](../../evidence/conditions-sets-081.md#c-d320464e5add632e) · [状态效果 S-2b3c32bbd2e8a6a7](../../evidence/state_effects-sets-010.md#s-2b3c32bbd2e8a6a7)

### observed_connections-000395

```text
(config-router)# default queue-depth hello <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 20 `；EOL ` RVA 0x34883DD8 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6df36a1f578269a1](../../evidence/conditions-sets-043.md#c-6df36a1f578269a1) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000486

```text
(config-router)# default queue-depth hello <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 18 `；EOL ` RVA 0x3567B298 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-98f787e9a034b54a](../../evidence/conditions-sets-059.md#c-98f787e9a034b54a) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000499

```text
(config-router)# default queue-depth update <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 17 `；EOL ` RVA 0x3567B620 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1060de1fb05d5454](../../evidence/conditions-sets-006.md#c-1060de1fb05d5454) · [状态效果 S-8f5728a770f73b40](../../evidence/state_effects-sets-030.md#s-8f5728a770f73b40)

### observed_connections-000354

```text
(config-router)# default redistribute maximum-prefix <cr>
```

Handler ` RVA 0xE1E4550 `；selector ` 0 `；EOL ` RVA 0x3424E580 `。

模式根 ` RVA 0x3422CD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8f87d19f95b6f242](../../evidence/conditions-sets-056.md#c-8f87d19f95b6f242) · [状态效果 S-030c64370b163b7d](../../evidence/state_effects-sets-001.md#s-030c64370b163b7d)
