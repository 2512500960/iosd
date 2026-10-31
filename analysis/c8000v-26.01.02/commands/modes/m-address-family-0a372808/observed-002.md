# address-family · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-002606

```text
(config-router-af)# no area <number:0..4294967295> encryption ipsec spi <number:256..4294967295> <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 8 `；EOL ` RVA 0x35655E88 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value；` unsigned_number ` SPI。

[条件 C-85cbc6207a57f0b0](../../evidence/conditions-sets-052.md#c-85cbc6207a57f0b0) · [参数 P-0a7db9ba82254141](../../evidence/parameters-sets-001.md#p-0a7db9ba82254141) · [状态效果 S-2eb95c9de1585f15](../../evidence/state_effects-sets-010.md#s-2eb95c9de1585f15)

### observed_connections-002608

```text
(config-router-af)# no area <number:0..4294967295> filter-list prefix <string> in <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 11 `；EOL ` RVA 0x356337E0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value；` string ` Name of an IPv6 prefix-list。

[条件 C-9cb0ef452e442b39](../../evidence/conditions-sets-061.md#c-9cb0ef452e442b39) · [参数 P-1a54c6728906f31d](../../evidence/parameters-sets-002.md#p-1a54c6728906f31d) · [状态效果 S-78cbf250aee3a968](../../evidence/state_effects-sets-026.md#s-78cbf250aee3a968)

### observed_connections-002483

```text
(config-router-af)# no area <number:0..4294967295> mpls <cr>
```

Handler ` RVA 0x11BC2300 `；selector ` 13 `；EOL ` RVA 0x35CD9040 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value。

[条件 C-f21fbf794eb9d102](../../evidence/conditions-sets-093.md#c-f21fbf794eb9d102) · [参数 P-c94ae0b4e794f02b](../../evidence/parameters-sets-015.md#p-c94ae0b4e794f02b) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002428

```text
(config-router-af)# no area <number:0..4294967295> no-transit <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 6 `；EOL ` RVA 0x35657C88 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value。

[条件 C-808a5cf139aab098](../../evidence/conditions-sets-050.md#c-808a5cf139aab098) · [参数 P-c94ae0b4e794f02b](../../evidence/parameters-sets-015.md#p-c94ae0b4e794f02b) · [状态效果 S-1933dc789af50395](../../evidence/state_effects-sets-006.md#s-1933dc789af50395)

### observed_connections-002445

```text
(config-router-af)# no area <number:0..4294967295> normal <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 5 `；EOL ` RVA 0x35658048 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value。

[条件 C-4b378348630822f0](../../evidence/conditions-sets-030.md#c-4b378348630822f0) · [参数 P-c94ae0b4e794f02b](../../evidence/parameters-sets-015.md#p-c94ae0b4e794f02b) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002478

```text
(config-router-af)# no area <number:0..4294967295> nssa <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 3 `；EOL ` RVA 0x35658950 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value。

[条件 C-0e4af2a70b6f1d5b](../../evidence/conditions-sets-006.md#c-0e4af2a70b6f1d5b) · [参数 P-c94ae0b4e794f02b](../../evidence/parameters-sets-015.md#p-c94ae0b4e794f02b) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002430

```text
(config-router-af)# no area <number:0..4294967295> packet-size <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 14 `；EOL ` RVA 0x35657A00 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value。

[条件 C-c178e735279e2658](../../evidence/conditions-sets-075.md#c-c178e735279e2658) · [参数 P-c94ae0b4e794f02b](../../evidence/parameters-sets-015.md#p-c94ae0b4e794f02b) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002595

```text
(config-router-af)# no area <number:0..4294967295> range <address> <address> <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 2 `；EOL ` RVA 0x35658FF8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value；` address ` IPv4 address to match；` address ` IPv4 mask for address。

[条件 C-11df995e14425fe0](../../evidence/conditions-sets-007.md#c-11df995e14425fe0) · [参数 P-2c00c8203e3403e9](../../evidence/parameters-sets-004.md#p-2c00c8203e3403e9) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002599

```text
(config-router-af)# no area <number:0..4294967295> sham-link <address> <address> <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 12 `；EOL ` RVA 0x356332A8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value；` address ` IPv6 address associated with sham-link source；` address ` IPv6 address associated with sham-link destination。

[条件 C-bf70eecc980b528a](../../evidence/conditions-sets-074.md#c-bf70eecc980b528a) · [参数 P-fbd2b1040e5ac880](../../evidence/parameters-sets-019.md#p-fbd2b1040e5ac880) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002458

```text
(config-router-af)# no area <number:0..4294967295> stub <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 4 `；EOL ` RVA 0x356583A8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value。

[条件 C-f1cc348c6cb09d27](../../evidence/conditions-sets-093.md#c-f1cc348c6cb09d27) · [参数 P-c94ae0b4e794f02b](../../evidence/parameters-sets-015.md#p-c94ae0b4e794f02b) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002561

```text
(config-router-af)# no area <number:0..4294967295> virtual-link <address> <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 1 `；EOL ` RVA 0x356323C0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value；` address ` RouterID associated with virtual link neighbor。

[条件 C-57286b1644c65375](../../evidence/conditions-sets-034.md#c-57286b1644c65375) · [参数 P-509320e887af2bfc](../../evidence/parameters-sets-007.md#p-509320e887af2bfc) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002491

```text
(config-router-af)# no authentication mode strict <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 31 `；EOL ` RVA 0x356368F8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7d3c2e1bb6f2b317](../../evidence/conditions-sets-049.md#c-7d3c2e1bb6f2b317) · [状态效果 S-ef2c13a71630aab2](../../evidence/state_effects-sets-051.md#s-ef2c13a71630aab2)

### observed_connections-002163

```text
(config-router-af)# no auto-cost <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 0 `；EOL ` RVA 0x35635438 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-67c55366e9607aca](../../evidence/conditions-sets-040.md#c-67c55366e9607aca) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002145

```text
(config-router-af)# no auto-summary <cr>
```

Handler ` RVA 0xE1FA6B0 `；selector ` 0 `；EOL ` RVA 0x34270F08 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d09ca02f517d25b9](../../evidence/conditions-sets-080.md#c-d09ca02f517d25b9) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002218

```text
(config-router-af)# no bfd all-interfaces <cr>
```

Handler ` RVA 0x11A9ADD0 `；selector ` 0 `；EOL ` RVA 0x355D71B8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5aa50fbc9e8e7678](../../evidence/conditions-sets-035.md#c-5aa50fbc9e8e7678) · [状态效果 S-0d22d27551325b23](../../evidence/state_effects-sets-003.md#s-0d22d27551325b23)

### observed_connections-002271

```text
(config-router-af)# no bfd all-interfaces <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 20 `；EOL ` RVA 0x356540B8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-15283135ebae1046](../../evidence/conditions-sets-008.md#c-15283135ebae1046) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002244

```text
(config-router-af)# no bfd check-ctrl-plane-failure <cr>
```

Handler ` RVA 0xE1FA610 `；selector ` 0 `；EOL ` RVA 0x3426CED8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b11f0f912f682171](../../evidence/conditions-sets-068.md#c-b11f0f912f682171) · [状态效果 S-f0994dc510e749bd](../../evidence/state_effects-sets-051.md#s-f0994dc510e749bd)

### observed_connections-002457

```text
(config-router-af)# no bgp additional-paths install <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 69 `；EOL ` RVA 0x35649B40 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e5e6e021d2e6e084](../../evidence/conditions-sets-089.md#c-e5e6e021d2e6e084) · [状态效果 S-7985a14192c71a69](../../evidence/state_effects-sets-026.md#s-7985a14192c71a69)

### observed_connections-002468

```text
(config-router-af)# no bgp additional-paths select <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 71 `；EOL ` RVA 0x356497E8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5a7dca4852e6c561](../../evidence/conditions-sets-035.md#c-5a7dca4852e6c561) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002288

```text
(config-router-af)# no bgp advertise-best-external <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 70 `；EOL ` RVA 0x3564A990 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a6f686622702fc65](../../evidence/conditions-sets-064.md#c-a6f686622702fc65) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002369

```text
(config-router-af)# no bgp advertisement startup-delay <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 95 `；EOL ` RVA 0x35642800 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-de9157a35f1292a2](../../evidence/conditions-sets-086.md#c-de9157a35f1292a2) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002469

```text
(config-router-af)# no bgp aggregate-timer <number:6..60> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 58 `；EOL ` RVA 0x356509E0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Timer interval。

[条件 C-0dc3d46e141a1f5e](../../evidence/conditions-sets-006.md#c-0dc3d46e141a1f5e) · [参数 P-229a5aa224238f9f](../../evidence/parameters-sets-003.md#p-229a5aa224238f9f) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002399

```text
(config-router-af)# no bgp aigp-rib-metric <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 91 `；EOL ` RVA 0x35647280 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4a3c3ec86f257c8a](../../evidence/conditions-sets-029.md#c-4a3c3ec86f257c8a) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002268

```text
(config-router-af)# no bgp always-compare-med <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 5 `；EOL ` RVA 0x3563E0E8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8d3b3c9e2a55f0b9](../../evidence/conditions-sets-055.md#c-8d3b3c9e2a55f0b9) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002440

```text
(config-router-af)# no bgp asnotation dot <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 64 `；EOL ` RVA 0x3563E3F8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8d3b3c9e2a55f0b9](../../evidence/conditions-sets-055.md#c-8d3b3c9e2a55f0b9) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002575

```text
(config-router-af)# no bgp bestpath aigp ignore <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 43 `；EOL ` RVA 0x35645FA8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d76469a1f7a4873d](../../evidence/conditions-sets-083.md#c-d76469a1f7a4873d) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002568

```text
(config-router-af)# no bgp bestpath as-path ignore <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 17 `；EOL ` RVA 0x35645718 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4a3c3ec86f257c8a](../../evidence/conditions-sets-029.md#c-4a3c3ec86f257c8a) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002570

```text
(config-router-af)# no bgp bestpath as-path multipath-relax <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 51 `；EOL ` RVA 0x356459C0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4a3c3ec86f257c8a](../../evidence/conditions-sets-029.md#c-4a3c3ec86f257c8a) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002511

```text
(config-router-af)# no bgp bestpath compare-routerid <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 24 `；EOL ` RVA 0x35645C58 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4a3c3ec86f257c8a](../../evidence/conditions-sets-029.md#c-4a3c3ec86f257c8a) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002574

```text
(config-router-af)# no bgp bestpath cost-community ignore <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 41 `；EOL ` RVA 0x35646280 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4a3c3ec86f257c8a](../../evidence/conditions-sets-029.md#c-4a3c3ec86f257c8a) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002527

```text
(config-router-af)# no bgp bestpath igp-metric ignore <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 42 `；EOL ` RVA 0x3564A070 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5150ea47e3f03165](../../evidence/conditions-sets-032.md#c-5150ea47e3f03165) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002571

```text
(config-router-af)# no bgp bestpath med missing-as-worst <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 18 `；EOL ` RVA 0x35645408 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4a3c3ec86f257c8a](../../evidence/conditions-sets-029.md#c-4a3c3ec86f257c8a) · [状态效果 S-5d8928fd37312452](../../evidence/state_effects-sets-020.md#s-5d8928fd37312452)

### observed_connections-002535

```text
(config-router-af)# no bgp bestpath prefix-validate allow-invalid <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 78 `；EOL ` RVA 0x3564A380 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8904f4b1b978efe3](../../evidence/conditions-sets-053.md#c-8904f4b1b978efe3) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002537

```text
(config-router-af)# no bgp bestpath prefix-validate disable <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 77 `；EOL ` RVA 0x3564A628 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8904f4b1b978efe3](../../evidence/conditions-sets-053.md#c-8904f4b1b978efe3) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002463

```text
(config-router-af)# no bgp client-to-client reflection <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 9 `；EOL ` RVA 0x3563F288 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-607bcdd6d486da42](../../evidence/conditions-sets-038.md#c-607bcdd6d486da42) · [状态效果 S-de520d4597ea0202](../../evidence/state_effects-sets-047.md#s-de520d4597ea0202)

### observed_connections-002312

```text
(config-router-af)# no bgp cluster-id <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 7 `；EOL ` RVA 0x3563EE50 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-279fa4de4ea80b69](../../evidence/conditions-sets-016.md#c-279fa4de4ea80b69) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002323

```text
(config-router-af)# no bgp consistency-checker <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 3 `；EOL ` RVA 0x3563E7D0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-41bc1b3c560cce95](../../evidence/conditions-sets-026.md#c-41bc1b3c560cce95) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002273

```text
(config-router-af)# no bgp dampening <cr>
```

Handler ` RVA 0xF1B85B0 `；selector ` 0 `；EOL ` RVA 0x35648C08 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-20c07d66b5366bf4](../../evidence/conditions-sets-013.md#c-20c07d66b5366bf4) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002528

```text
(config-router-af)# no bgp default inter-as-hybrid advertise-source-routes <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 57 `；EOL ` RVA 0x35648240 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c666987e1ff102fc](../../evidence/conditions-sets-076.md#c-c666987e1ff102fc) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002424

```text
(config-router-af)# no bgp default ipv4-unicast <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 19 `；EOL ` RVA 0x35647998 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-833065ca9d9b5b4a](../../evidence/conditions-sets-051.md#c-833065ca9d9b5b4a) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002427

```text
(config-router-af)# no bgp default ipv6-nexthop <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 75 `；EOL ` RVA 0x35647C90 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-01297021f866bd84](../../evidence/conditions-sets-001.md#c-01297021f866bd84) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002275

```text
(config-router-af)# no bgp default local-preference <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 0 `；EOL ` RVA 0x35647F20 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-bac9553258d6e58a](../../evidence/conditions-sets-072.md#c-bac9553258d6e58a) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002521

```text
(config-router-af)# no bgp default route-target filter <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 25 `；EOL ` RVA 0x356485A8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-2127c24ec9e7cb8b](../../evidence/conditions-sets-013.md#c-2127c24ec9e7cb8b) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002522

```text
(config-router-af)# no bgp default route-target filter <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 25 `；EOL ` RVA 0x35648848 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-49c39aa546553d15](../../evidence/conditions-sets-029.md#c-49c39aa546553d15) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002343

```text
(config-router-af)# no bgp deterministic-med <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 10 `；EOL ` RVA 0x35640908 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8d3b3c9e2a55f0b9](../../evidence/conditions-sets-055.md#c-8d3b3c9e2a55f0b9) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002309

```text
(config-router-af)# no bgp dmzlink-bw <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 31 `；EOL ` RVA 0x3564BF40 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-795d3aa0c1de4631](../../evidence/conditions-sets-047.md#c-795d3aa0c1de4631) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002168

```text
(config-router-af)# no bgp dynamic-med-interval <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 21 `；EOL ` RVA 0x35640930 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-72fea9477916ed01](../../evidence/conditions-sets-044.md#c-72fea9477916ed01) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002317

```text
(config-router-af)# no bgp enforce-first-as <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 20 `；EOL ` RVA 0x3563FB38 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8d3b3c9e2a55f0b9](../../evidence/conditions-sets-055.md#c-8d3b3c9e2a55f0b9) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002373

```text
(config-router-af)# no bgp enhanced-error <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 82 `；EOL ` RVA 0x35642578 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-9bda20e03b0de16c](../../evidence/conditions-sets-060.md#c-9bda20e03b0de16c) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002239

```text
(config-router-af)# no bgp fast-external-fallover <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 1 `；EOL ` RVA 0x3563D820 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8d3b3c9e2a55f0b9](../../evidence/conditions-sets-055.md#c-8d3b3c9e2a55f0b9) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002385

```text
(config-router-af)# no bgp graceful-restart <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 35 `；EOL ` RVA 0x356433E8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8d3b3c9e2a55f0b9](../../evidence/conditions-sets-055.md#c-8d3b3c9e2a55f0b9) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002379

```text
(config-router-af)# no bgp graceful-restart restart-time <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 36 `；EOL ` RVA 0x35642DB8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c4d273e835f8e73f](../../evidence/conditions-sets-076.md#c-c4d273e835f8e73f) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002381

```text
(config-router-af)# no bgp graceful-restart stalepath-time <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 37 `；EOL ` RVA 0x35642E20 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-cc349caed8a74471](../../evidence/conditions-sets-079.md#c-cc349caed8a74471) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002602

```text
(config-router-af)# no bgp graceful-shutdown all vrfs activate <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 79 `；EOL ` RVA 0x35643850 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0d112354600b2460](../../evidence/conditions-sets-005.md#c-0d112354600b2460) · [状态效果 S-2c8b1f01413948e1](../../evidence/state_effects-sets-010.md#s-2c8b1f01413948e1)

### observed_connections-002598

```text
(config-router-af)# no bgp inject-map <string> exist-map <string> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 32 `；EOL ` RVA 0x3564DAB8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` route-map name；` string ` route-map name。

[条件 C-e56cedc33997c1c6](../../evidence/conditions-sets-088.md#c-e56cedc33997c1c6) · [参数 P-82a88d349cb24e9e](../../evidence/parameters-sets-010.md#p-82a88d349cb24e9e) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002520

```text
(config-router-af)# no bgp label-allocation-batch <number:0..4294967295> <number:0..4294967295> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 53 `；EOL ` RVA 0x3563DBB0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Timer value in milliseconds；` unsigned_number ` Batch Size。

[条件 C-8d3b3c9e2a55f0b9](../../evidence/conditions-sets-055.md#c-8d3b3c9e2a55f0b9) · [参数 P-590ffc4a862cdd5b](../../evidence/parameters-sets-007.md#p-590ffc4a862cdd5b) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002547

```text
(config-router-af)# no bgp listen block <address> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 93 `；EOL ` RVA 0x3564B950 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` IPv4 Dynamic Peering Address。

[条件 C-91f187ee957ea16a](../../evidence/conditions-sets-056.md#c-91f187ee957ea16a) · [参数 P-ff1855d12fccf3a2](../../evidence/parameters-sets-019.md#p-ff1855d12fccf3a2) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002564

```text
(config-router-af)# no bgp listen block <address> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 93 `；EOL ` RVA 0x356418B0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` IPv4 Dynamic Peering Address。

[条件 C-861d4f86f990b125](../../evidence/conditions-sets-052.md#c-861d4f86f990b125) · [参数 P-8e142a50b5d2fd9e](../../evidence/parameters-sets-011.md#p-8e142a50b5d2fd9e) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002329

```text
(config-router-af)# no bgp listen limit <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 61 `；EOL ` RVA 0x3564B898 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a77cb16fa3be3af0](../../evidence/conditions-sets-065.md#c-a77cb16fa3be3af0) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002374

```text
(config-router-af)# no bgp listen limit <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 61 `；EOL ` RVA 0x356417D0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ed662d13ec07b594](../../evidence/conditions-sets-092.md#c-ed662d13ec07b594) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002495

```text
(config-router-af)# no bgp listen persistent <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 94 `；EOL ` RVA 0x35641BE8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-861d4f86f990b125](../../evidence/conditions-sets-052.md#c-861d4f86f990b125) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002326

```text
(config-router-af)# no bgp log-neighbor-changes <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 11 `；EOL ` RVA 0x3563FDE0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8d3b3c9e2a55f0b9](../../evidence/conditions-sets-055.md#c-8d3b3c9e2a55f0b9) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002405

```text
(config-router-af)# no bgp maxas-limit <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 26 `；EOL ` RVA 0x35646FF8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-3136a06c2f3edd07](../../evidence/conditions-sets-019.md#c-3136a06c2f3edd07) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002394

```text
(config-router-af)# no bgp maxcommunity-limit <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 27 `；EOL ` RVA 0x35646608 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8fb6e74c9ab347cd](../../evidence/conditions-sets-056.md#c-8fb6e74c9ab347cd) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002401

```text
(config-router-af)# no bgp maxextcommunity-limit <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 29 `；EOL ` RVA 0x35646CA8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7e56ab847abf6d47](../../evidence/conditions-sets-049.md#c-7e56ab847abf6d47) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002397

```text
(config-router-af)# no bgp maxlargecommunity-limit <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 28 `；EOL ` RVA 0x35646958 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c8e73245453feb79](../../evidence/conditions-sets-077.md#c-c8e73245453feb79) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002364

```text
(config-router-af)# no bgp mpls-local-label <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 81 `；EOL ` RVA 0x3564DE30 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-92af687f7671312c](../../evidence/conditions-sets-057.md#c-92af687f7671312c) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002552

```text
(config-router-af)# no bgp nexthop route-map <string> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 56 `；EOL ` RVA 0x3564C6A8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` route-map name。

[条件 C-c23de0d6427bd68a](../../evidence/conditions-sets-075.md#c-c23de0d6427bd68a) · [参数 P-2fa3aa6823f1ec72](../../evidence/parameters-sets-004.md#p-2fa3aa6823f1ec72) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002484

```text
(config-router-af)# no bgp nexthop trigger critical-delay <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 48 `；EOL ` RVA 0x3564CC10 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e1ae81c6bb832a17](../../evidence/conditions-sets-087.md#c-e1ae81c6bb832a17) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002476

```text
(config-router-af)# no bgp nexthop trigger delay <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 47 `；EOL ` RVA 0x3564C990 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-89ddc69738a7fa09](../../evidence/conditions-sets-053.md#c-89ddc69738a7fa09) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002546

```text
(config-router-af)# no bgp nexthop trigger enable <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 49 `；EOL ` RVA 0x3564C968 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-03a7874e9a6887cf](../../evidence/conditions-sets-002.md#c-03a7874e9a6887cf) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002560

```text
(config-router-af)# no bgp nopeerup-delay cold-boot <number:1..3600> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 74 `；EOL ` RVA 0x35642210 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Delay in seconds。

[条件 C-23578c788649caa5](../../evidence/conditions-sets-014.md#c-23578c788649caa5) · [参数 P-5c73c5e1db17e48e](../../evidence/parameters-sets-007.md#p-5c73c5e1db17e48e) · [状态效果 S-7227adfb1d3467cb](../../evidence/state_effects-sets-024.md#s-7227adfb1d3467cb)

### observed_connections-002449

```text
(config-router-af)# no bgp recursion host <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 72 `；EOL ` RVA 0x3564AD08 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8f08c4361e706b21](../../evidence/conditions-sets-055.md#c-8f08c4361e706b21) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002289

```text
(config-router-af)# no bgp redistribute-internal <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 2 `；EOL ` RVA 0x3564F030 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5182e528ca172aef](../../evidence/conditions-sets-032.md#c-5182e528ca172aef) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002505

```text
(config-router-af)# no bgp refresh max-eor-time <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 16 `；EOL ` RVA 0x356445E0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d8398869011dd515](../../evidence/conditions-sets-083.md#c-d8398869011dd515) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002500

```text
(config-router-af)# no bgp refresh stalepath-time <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 15 `；EOL ` RVA 0x35644270 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-735f38d87ce4c8bb](../../evidence/conditions-sets-045.md#c-735f38d87ce4c8bb) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002501

```text
(config-router-af)# no bgp regexp deterministic <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 44 `；EOL ` RVA 0x35644FF8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4a3c3ec86f257c8a](../../evidence/conditions-sets-029.md#c-4a3c3ec86f257c8a) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002450

```text
(config-router-af)# no bgp route-map priority <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 59 `；EOL ` RVA 0x356501C0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e552582f99054ab0](../../evidence/conditions-sets-088.md#c-e552582f99054ab0) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002254

```text
(config-router-af)# no bgp route-map-cache <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 34 `；EOL ` RVA 0x3563DE38 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8d3b3c9e2a55f0b9](../../evidence/conditions-sets-055.md#c-8d3b3c9e2a55f0b9) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002274

```text
(config-router-af)# no bgp router-id <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 4 `；EOL ` RVA 0x3563D1F0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-04a593b02bd9882f](../../evidence/conditions-sets-002.md#c-04a593b02bd9882f) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002332

```text
(config-router-af)# no bgp router-id <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 4 `；EOL ` RVA 0x3564B3B8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c8ae3b2a54702fba](../../evidence/conditions-sets-077.md#c-c8ae3b2a54702fba) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002612

```text
(config-router-af)# no bgp rpki server tcp <address> port <number:1..65535> refresh <number:1..65535> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 76 `；EOL ` RVA 0x35650FD8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` IPv6 address of RPKI cache server；` unsigned_number ` Port number；` unsigned_number ` Refresh time in seconds。

[条件 C-403177562c0694ce](../../evidence/conditions-sets-025.md#c-403177562c0694ce) · [参数 P-8c5c351bae1730a5](../../evidence/parameters-sets-011.md#p-8c5c351bae1730a5) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002348

```text
(config-router-af)# no bgp rr-group <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 23 `；EOL ` RVA 0x3564D650 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-2037c5a6f0a68497](../../evidence/conditions-sets-013.md#c-2037c5a6f0a68497) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002407

```text
(config-router-af)# no bgp safe-ebgp-policy <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 92 `；EOL ` RVA 0x35647590 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ffea2d982084ee65](../../evidence/conditions-sets-099.md#c-ffea2d982084ee65) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002481

```text
(config-router-af)# no bgp scan-time <number:5..60> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 22 `；EOL ` RVA 0x3564D2E0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Scanner interval (seconds)。

[条件 C-8b3598aecea70031](../../evidence/conditions-sets-054.md#c-8b3598aecea70031) · [参数 P-d09d1b488454b2d8](../../evidence/parameters-sets-016.md#p-d09d1b488454b2d8) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002452

```text
(config-router-af)# no bgp slow-peer detection <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 67 `；EOL ` RVA 0x3564E300 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7b9ff71979c8ced8](../../evidence/conditions-sets-048.md#c-7b9ff71979c8ced8) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002538

```text
(config-router-af)# no bgp slow-peer split-update-group dynamic <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 68 `；EOL ` RVA 0x3564E8D0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-147aff615d14f1bc](../../evidence/conditions-sets-008.md#c-147aff615d14f1bc) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002556

```text
(config-router-af)# no bgp snmp traps add-type <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 90 `；EOL ` RVA 0x35640EF8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8d3b3c9e2a55f0b9](../../evidence/conditions-sets-055.md#c-8d3b3c9e2a55f0b9) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002327

```text
(config-router-af)# no bgp soft-reconfig-backup <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 52 `；EOL ` RVA 0x3564C290 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-6b8a08d64cffcc48](../../evidence/conditions-sets-042.md#c-6b8a08d64cffcc48) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002593

```text
(config-router-af)# no bgp sourced-paths per-net isis all <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 89 `；EOL ` RVA 0x3564FE40 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ff436232114b2225](../../evidence/conditions-sets-098.md#c-ff436232114b2225) · [状态效果 S-cc259b00c6a1bd9f](../../evidence/state_effects-sets-043.md#s-cc259b00c6a1bd9f)

### observed_connections-002589

```text
(config-router-af)# no bgp sourced-paths per-net ospf all <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 87 `；EOL ` RVA 0x3564F7E0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ff436232114b2225](../../evidence/conditions-sets-098.md#c-ff436232114b2225) · [状态效果 S-c9373dd4f06fc749](../../evidence/state_effects-sets-043.md#s-c9373dd4f06fc749)

### observed_connections-002591

```text
(config-router-af)# no bgp sourced-paths per-net ospfv3 all <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 88 `；EOL ` RVA 0x3564FB28 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ff436232114b2225](../../evidence/conditions-sets-098.md#c-ff436232114b2225) · [状态效果 S-ec22d812780b384f](../../evidence/state_effects-sets-050.md#s-ec22d812780b384f)

### observed_connections-002587

```text
(config-router-af)# no bgp sourced-paths per-net static all <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 86 `；EOL ` RVA 0x3564F498 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ff436232114b2225](../../evidence/conditions-sets-098.md#c-ff436232114b2225) · [状态效果 S-19358cec9cb2594e](../../evidence/state_effects-sets-006.md#s-19358cec9cb2594e)

### observed_connections-002496

```text
(config-router-af)# no bgp sso route-refresh-enable <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 38 `；EOL ` RVA 0x35643EB0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4a3c3ec86f257c8a](../../evidence/conditions-sets-029.md#c-4a3c3ec86f257c8a) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002297

```text
(config-router-af)# no bgp suppress-inactive <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 45 `；EOL ` RVA 0x3564B008 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-488f3c121a9ac3ba](../../evidence/conditions-sets-028.md#c-488f3c121a9ac3ba) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002073

```text
(config-router-af)# no bgp tid <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 55 `；EOL ` RVA 0x3563CA30 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b48bc5c154b06025](../../evidence/conditions-sets-070.md#c-b48bc5c154b06025) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002460

```text
(config-router-af)# no bgp transport path-mtu-discovery <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 50 `；EOL ` RVA 0x3563F8A8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8d3b3c9e2a55f0b9](../../evidence/conditions-sets-055.md#c-8d3b3c9e2a55f0b9) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002185

```text
(config-router-af)# no bgp update-delay <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 30 `；EOL ` RVA 0x35642828 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-23705696ae5a3223](../../evidence/conditions-sets-014.md#c-23705696ae5a3223) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002531

```text
(config-router-af)# no bgp update-group split as-override <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 73 `；EOL ` RVA 0x3564ECA0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-779c8c2bed6dd3fc](../../evidence/conditions-sets-047.md#c-779c8c2bed6dd3fc) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002246

```text
(config-router-af)# no bgp upgrade-cli <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 33 `；EOL ` RVA 0x3563CE48 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-054935b640257f09](../../evidence/conditions-sets-002.md#c-054935b640257f09) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002319

```text
(config-router-af)# no bgp va <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 80 `；EOL ` RVA 0x35650568 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f0bbb147fbc528e4](../../evidence/conditions-sets-093.md#c-f0bbb147fbc528e4) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002499

```text
(config-router-af)# no bgp vrf-update-optimisation off <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 66 `；EOL ` RVA 0x35644968 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4a3c3ec86f257c8a](../../evidence/conditions-sets-029.md#c-4a3c3ec86f257c8a) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002389

```text
(config-router-af)# no bgp write-limit <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 40 `；EOL ` RVA 0x35644CC0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1bcc9c3f0635808c](../../evidence/conditions-sets-011.md#c-1bcc9c3f0635808c) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002363

```text
(config-router-af)# no capability vrf-lite <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 7 `；EOL ` RVA 0x35636500 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-57adb160f929a25e](../../evidence/conditions-sets-034.md#c-57adb160f929a25e) · [状态效果 S-dd73ff2b471d1b47](../../evidence/state_effects-sets-047.md#s-dd73ff2b471d1b47)

### observed_connections-002243

```text
(config-router-af)# no compatible rfc1583 <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 25 `；EOL ` RVA 0x356544B8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-cc5aafa1a170d7f5](../../evidence/conditions-sets-079.md#c-cc5aafa1a170d7f5) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002252

```text
(config-router-af)# no compatible rfc1587 <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 26 `；EOL ` RVA 0x356547B0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0a4ff46fd3afc43d](../../evidence/conditions-sets-004.md#c-0a4ff46fd3afc43d) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002265

```text
(config-router-af)# no compatible rfc5243 <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 27 `；EOL ` RVA 0x35654A80 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7ac4b67371877306](../../evidence/conditions-sets-048.md#c-7ac4b67371877306) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002054

```text
(config-router-af)# no context <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 0 `；EOL ` RVA 0x33C44A60 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e07495ed56793ecc](../../evidence/conditions-sets-086.md#c-e07495ed56793ecc) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002233

```text
(config-router-af)# no default-information originate <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 6 `；EOL ` RVA 0x35639DE0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f938ce7057554709](../../evidence/conditions-sets-096.md#c-f938ce7057554709) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002311

```text
(config-router-af)# no default-information originate <cr>
```

Handler ` RVA 0xE1F1F70 `；selector ` 0 `；EOL ` RVA 0x3426ED60 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-db74cc03fbb4a097](../../evidence/conditions-sets-084.md#c-db74cc03fbb4a097) · [状态效果 S-9fe91d556ca6f5cf](../../evidence/state_effects-sets-034.md#s-9fe91d556ca6f5cf)

### observed_connections-002368

```text
(config-router-af)# no default-information originate <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 6 `；EOL ` RVA 0x355DCEA8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-366c48c6f37882be](../../evidence/conditions-sets-021.md#c-366c48c6f37882be) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002099

```text
(config-router-af)# no default-metric <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 12 `；EOL ` RVA 0x3563A578 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4cbdc72f1b023cd3](../../evidence/conditions-sets-030.md#c-4cbdc72f1b023cd3) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002146

```text
(config-router-af)# no default-metric <cr>
```

Handler ` RVA 0xE1F35A0 `；selector ` 0 `；EOL ` RVA 0x3426F628 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f9a8947cff7fe304](../../evidence/conditions-sets-096.md#c-f9a8947cff7fe304) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002184

```text
(config-router-af)# no default-metric <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 12 `；EOL ` RVA 0x355DD640 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ca8180878d1e0e46](../../evidence/conditions-sets-078.md#c-ca8180878d1e0e46) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002335

```text
(config-router-af)# no discard-route external <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 11 `；EOL ` RVA 0x35634FD0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8d1015de0df3837e](../../evidence/conditions-sets-055.md#c-8d1015de0df3837e) · [状态效果 S-500033bba2f70425](../../evidence/state_effects-sets-017.md#s-500033bba2f70425)

### observed_connections-002066

```text
(config-router-af)# no distance <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 9 `；EOL ` RVA 0x35630608 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e9f55346791e7a61](../../evidence/conditions-sets-090.md#c-e9f55346791e7a61) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002167

```text
(config-router-af)# no distance <cr>
```

Handler ` RVA 0xE1E3290 `；selector ` 1 `；EOL ` RVA 0x34270758 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-93e02ac49bb69a67](../../evidence/conditions-sets-057.md#c-93e02ac49bb69a67) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002177

```text
(config-router-af)# no distance <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 9 `；EOL ` RVA 0x355DDF30 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e0bb4bd73a45a762](../../evidence/conditions-sets-087.md#c-e0bb4bd73a45a762) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002344

```text
(config-router-af)# no distance nhrp <cr>
```

Handler ` RVA 0x108B0C70 `；selector ` 1 `；EOL ` RVA 0x34BE80E0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-80e66e65486dfde7](../../evidence/conditions-sets-050.md#c-80e66e65486dfde7) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002248

```text
(config-router-af)# no distance ospf <cr>
```

Handler ` RVA 0x11BCBF10 `；selector ` 0 `；EOL ` RVA 0x35659D80 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-3013555f355388cb](../../evidence/conditions-sets-019.md#c-3013555f355388cb) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002350

```text
(config-router-af)# no distance ospf <cr>
```

Handler ` RVA 0x11BCBF10 `；selector ` 0 `；EOL ` RVA 0x356594B8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7c5e00ccfdcef2d7](../../evidence/conditions-sets-048.md#c-7c5e00ccfdcef2d7) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002354

```text
(config-router-af)# no distribute-list in <cr>
```

Handler ` RVA 0xE1EE180 `；selector ` 0 `；EOL ` RVA 0x3426FD18 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-6d3dd57b54b1c820](../../evidence/conditions-sets-042.md#c-6d3dd57b54b1c820) · [状态效果 S-786567c4869161fd](../../evidence/state_effects-sets-026.md#s-786567c4869161fd)

### observed_connections-002549

```text
(config-router-af)# no distribute-list prefix-list <string> in <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 14 `；EOL ` RVA 0x355DA6F8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Prefix-list name。

[条件 C-a715b9c71b95a342](../../evidence/conditions-sets-064.md#c-a715b9c71b95a342) · [参数 P-adfe4ef17dd0436d](../../evidence/parameters-sets-013.md#p-adfe4ef17dd0436d) · [状态效果 S-6caba6e37f08e1d9](../../evidence/state_effects-sets-023.md#s-6caba6e37f08e1d9)

### observed_connections-002518

```text
(config-router-af)# no distribute-list route-map <string> in <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 14 `；EOL ` RVA 0x35639688 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Route-map name。

[条件 C-8a18c282ba969e4e](../../evidence/conditions-sets-053.md#c-8a18c282ba969e4e) · [参数 P-34975ce9a874ca41](../../evidence/parameters-sets-004.md#p-34975ce9a874ca41) · [状态效果 S-23e07b7266590de8](../../evidence/state_effects-sets-008.md#s-23e07b7266590de8)

### observed_connections-002106

```text
(config-router-af)# no domain-id <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 9 `；EOL ` RVA 0x35652DB8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-2361a282694be0b9](../../evidence/conditions-sets-014.md#c-2361a282694be0b9) · [状态效果 S-a8ac305e408bcbc0](../../evidence/state_effects-sets-036.md#s-a8ac305e408bcbc0)

### observed_connections-002160

```text
(config-router-af)# no event-log <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 19 `；EOL ` RVA 0x356347B0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-9a321beb23b08158](../../evidence/conditions-sets-060.md#c-9a321beb23b08158) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002034

```text
(config-router-af)# no flash-update-threshold <cr>
```

Handler ` RVA 0xE1F7ED0 `；selector ` 0 `；EOL ` RVA 0x3426E850 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-6f8054bc55cf8cc0](../../evidence/conditions-sets-043.md#c-6f8054bc55cf8cc0) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002206

```text
(config-router-af)# no graceful-restart <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 22 `；EOL ` RVA 0x3569DA70 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-2c70dea2cb2c798f](../../evidence/conditions-sets-017.md#c-2c70dea2cb2c798f) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002391

```text
(config-router-af)# no graceful-restart helper <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 23 `；EOL ` RVA 0x3569DDF8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-12975865b37b3794](../../evidence/conditions-sets-007.md#c-12975865b37b3794) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002447

```text
(config-router-af)# no ignore lsa mospf <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 4 `；EOL ` RVA 0x35633EC8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-67c55366e9607aca](../../evidence/conditions-sets-040.md#c-67c55366e9607aca) · [状态效果 S-56e7bc37c688662a](../../evidence/state_effects-sets-019.md#s-56e7bc37c688662a)

### observed_connections-002214

```text
(config-router-af)# no import bgp <cr>
```

Handler ` RVA 0x108B2FF0 `；selector ` 0 `；EOL ` RVA 0x34BE7790 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-677e9c0608947bd9](../../evidence/conditions-sets-040.md#c-677e9c0608947bd9) · [状态效果 S-309bb0818f25dbcf](../../evidence/state_effects-sets-011.md#s-309bb0818f25dbcf)

### observed_connections-002032

```text
(config-router-af)# no input-queue <cr>
```

Handler ` RVA 0xE1F8060 `；selector ` 0 `；EOL ` RVA 0x3426E560 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-480be9c7b4e80e0a](../../evidence/conditions-sets-028.md#c-480be9c7b4e80e0a) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002263

```text
(config-router-af)# no interface-id snmp-if-index <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 15 `；EOL ` RVA 0x35654E18 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-67c55366e9607aca](../../evidence/conditions-sets-040.md#c-67c55366e9607aca) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002584

```text
(config-router-af)# no ipv6 route priority high tag <cr>
```

Handler ` RVA 0x11A9B140 `；selector ` 0 `；EOL ` RVA 0x355D83F8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e3887c19682da74d](../../evidence/conditions-sets-088.md#c-e3887c19682da74d) · [状态效果 S-861e8c0ae6276257](../../evidence/state_effects-sets-028.md#s-861e8c0ae6276257)

### observed_connections-002375

```text
(config-router-af)# no limit retransmissions <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 14 `；EOL ` RVA 0x35636178 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f3d98f9bd00b4882](../../evidence/conditions-sets-094.md#c-f3d98f9bd00b4882) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002201

```text
(config-router-af)# no local-rib-criteria <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 6 `；EOL ` RVA 0x35637370 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4f35057ca9207cf3](../../evidence/conditions-sets-031.md#c-4f35057ca9207cf3) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002155

```text
(config-router-af)# no log-adjacency-changes <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 3 `；EOL ` RVA 0x35634C50 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-67c55366e9607aca](../../evidence/conditions-sets-040.md#c-67c55366e9607aca) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002169

```text
(config-router-af)# no max-lsa <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 1 `；EOL ` RVA 0x356357F8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-38ee2a0952d2964f](../../evidence/conditions-sets-022.md#c-38ee2a0952d2964f) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002086

```text
(config-router-af)# no max-metric <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 13 `；EOL ` RVA 0x35653388 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e1f06c4138942f0d](../../evidence/conditions-sets-087.md#c-e1f06c4138942f0d) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002085

```text
(config-router-af)# no max-metric intra-area <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 8 `；EOL ` RVA 0x356532A8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e33251f679d1f25e](../../evidence/conditions-sets-087.md#c-e33251f679d1f25e) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002125

```text
(config-router-af)# no maximum-paths <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 8 `；EOL ` RVA 0x3563B130 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-372a5047c80eaed4](../../evidence/conditions-sets-021.md#c-372a5047c80eaed4) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002191

```text
(config-router-af)# no maximum-paths <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 8 `；EOL ` RVA 0x355DC998 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-2ca9638361f739f2](../../evidence/conditions-sets-018.md#c-2ca9638361f739f2) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002257

```text
(config-router-af)# no maximum-paths per-prefix-distribution <cr>
```

Handler ` RVA 0x11BCC820 `；selector ` 0 `；EOL ` RVA 0x3565A2B8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-2f42a0cb8b96205c](../../evidence/conditions-sets-018.md#c-2f42a0cb8b96205c) · [状态效果 S-fb48fae1e02a5f1e](../../evidence/state_effects-sets-053.md#s-fb48fae1e02a5f1e)

### observed_connections-002298

```text
(config-router-af)# no maximum-paths per-prefix-distribution <cr>
```

Handler ` RVA 0x11BCC820 `；selector ` 0 `；EOL ` RVA 0x356599F0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-78bb5629f4361cdc](../../evidence/conditions-sets-047.md#c-78bb5629f4361cdc) · [状态效果 S-124cd43032abc1ac](../../evidence/state_effects-sets-004.md#s-124cd43032abc1ac)

### observed_connections-002147

```text
(config-router-af)# no metric <cr>
```

Handler ` RVA 0x11A9E030 `；selector ` 0 `；EOL ` RVA 0x355D9B78 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5c43f340217e302b](../../evidence/conditions-sets-036.md#c-5c43f340217e302b) · [状态效果 S-2bcd40aeef590362](../../evidence/state_effects-sets-010.md#s-2bcd40aeef590362)

### observed_connections-002234

```text
(config-router-af)# no metric holddown <cr>
```

Handler ` RVA 0xE1F32D0 `；selector ` 1 `；EOL ` RVA 0x3426D3C8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ccc6cf9a6fedcd66](../../evidence/conditions-sets-079.md#c-ccc6cf9a6fedcd66) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002096

```text
(config-router-af)# no metric maximum-hops <cr>
```

Handler ` RVA 0xE1F32D0 `；selector ` 2 `；EOL ` RVA 0x3426D3F0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-9ad7b35ee187dc59](../../evidence/conditions-sets-060.md#c-9ad7b35ee187dc59) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002272

```text
(config-router-af)# no metric weights <cr>
```

Handler ` RVA 0xE1F32D0 `；selector ` 0 `；EOL ` RVA 0x3426D9B0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4816d0b45e8a295c](../../evidence/conditions-sets-028.md#c-4816d0b45e8a295c) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002604

```text
(config-router-af)# no mpls traffic-engineering autoroute-exclude prefix-list <string> <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 32 `；EOL ` RVA 0x35CD8788 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Name of a prefix-list。

[条件 C-20863a65a135cf8c](../../evidence/conditions-sets-013.md#c-20863a65a135cf8c) · [参数 P-bb9aae7e316bf097](../../evidence/parameters-sets-014.md#p-bb9aae7e316bf097) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002063

```text
(config-router-af)# no multi-topology <cr>
```

Handler ` RVA 0x11A9A2A0 `；selector ` 0 `；EOL ` RVA 0x355D74F8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a40c29f771cfb7a9](../../evidence/conditions-sets-063.md#c-a40c29f771cfb7a9) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002412

```text
(config-router-af)# no nhrp redirect interest <cr>
```

Handler ` RVA 0x108B1190 `；selector ` 19 `；EOL ` RVA 0x34BE7C48 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-aba1df4791efff49](../../evidence/conditions-sets-066.md#c-aba1df4791efff49) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002423

```text
(config-router-af)# no offset-list <number:0..99> in <cr>
```

Handler ` RVA 0xE1F1330 `；selector ` 0 `；EOL ` RVA 0x3426BED8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Access list of networks to apply offset (0 selects all networks)。

[条件 C-cca70eeca648cd6c](../../evidence/conditions-sets-079.md#c-cca70eeca648cd6c) · [参数 P-701ad9f9b6d2f431](../../evidence/parameters-sets-009.md#p-701ad9f9b6d2f431) · [状态效果 S-f57d80170307ea8f](../../evidence/state_effects-sets-052.md#s-f57d80170307ea8f)

### observed_connections-002141

```text
(config-router-af)# no omp-route-tag <cr>
```

Handler ` RVA 0xE1F7FD0 `；selector ` 0 `；EOL ` RVA 0x342712A8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-24312fafa4a6145a](../../evidence/conditions-sets-014.md#c-24312fafa4a6145a) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002021

```text
(config-router-af)# no output-delay <cr>
```

Handler ` RVA 0xE1F4590 `；selector ` 0 `；EOL ` RVA 0x3426B930 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7e81ff4b1bf9e6ec](../../evidence/conditions-sets-049.md#c-7e81ff4b1bf9e6ec) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002045

```text
(config-router-af)# no packet-size <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 41 `；EOL ` RVA 0x35636CC0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad034e533e076c35](../../evidence/conditions-sets-067.md#c-ad034e533e076c35) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002229

```text
(config-router-af)# no passive-interface default <cr>
```

Handler ` RVA 0xE1F3960 `；selector ` 0 `；EOL ` RVA 0x3426B520 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-84bb3022e130a597](../../evidence/conditions-sets-051.md#c-84bb3022e130a597) · [状态效果 S-ee2990d92b01b3f9](../../evidence/state_effects-sets-050.md#s-ee2990d92b01b3f9)

### observed_connections-002097

```text
(config-router-af)# no prc-interval <cr>
```

Handler ` RVA 0x11A9D490 `；selector ` 0 `；EOL ` RVA 0x355D8CB8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-39b0d31514ba81ef](../../evidence/conditions-sets-022.md#c-39b0d31514ba81ef) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002113

```text
(config-router-af)# no prefix-suppression <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 28 `；EOL ` RVA 0x35653C68 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-bc2b2736fc868929](../../evidence/conditions-sets-073.md#c-bc2b2736fc868929) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002194

```text
(config-router-af)# no process-min-time percent <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 16 `；EOL ` RVA 0x35637A38 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c3955e88f8b9f7b5](../../evidence/conditions-sets-075.md#c-c3955e88f8b9f7b5) · [状态效果 S-39095cebaedeeddf](../../evidence/state_effects-sets-013.md#s-39095cebaedeeddf)

### observed_connections-002280

```text
(config-router-af)# no queue-depth hello <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 18 `；EOL ` RVA 0x35655210 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-327e80b3620d3c1f](../../evidence/conditions-sets-020.md#c-327e80b3620d3c1f) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002292

```text
(config-router-af)# no queue-depth update <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 17 `；EOL ` RVA 0x35655598 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-2d498fcaf179e440](../../evidence/conditions-sets-018.md#c-2d498fcaf179e440) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002227

```text
(config-router-af)# no redistribute maximum-prefix <cr>
```

Handler ` RVA 0xE1E4550 `；selector ` 0 `；EOL ` RVA 0x34268518 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-585aee2847e70820](../../evidence/conditions-sets-035.md#c-585aee2847e70820) · [状态效果 S-3274c67e33c84b55](../../evidence/state_effects-sets-011.md#s-3274c67e33c84b55)

### observed_connections-002255

```text
(config-router-af)# no redistribute maximum-prefix <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 5 `；EOL ` RVA 0x35638F60 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-96cc87fa61f4d60f](../../evidence/conditions-sets-058.md#c-96cc87fa61f4d60f) · [状态效果 S-6886a9def1abde85](../../evidence/state_effects-sets-022.md#s-6886a9def1abde85)

### observed_connections-002068

```text
(config-router-af)# no router-id <cr>
```

Handler ` RVA 0x11A9F520 `；selector ` 0 `；EOL ` RVA 0x355D7868 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d2ed12a2e69b97ae](../../evidence/conditions-sets-081.md#c-d2ed12a2e69b97ae) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002075

```text
(config-router-af)# no router-id <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 12 `；EOL ` RVA 0x356528F8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b521df84fa17c565](../../evidence/conditions-sets-070.md#c-b521df84fa17c565) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002112

```text
(config-router-af)# no set-attached-bit <cr>
```

Handler ` RVA 0x11A9D130 `；selector ` 0 `；EOL ` RVA 0x355D9720 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c15e7e3fa471f0b4](../../evidence/conditions-sets-075.md#c-c15e7e3fa471f0b4) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002114

```text
(config-router-af)# no set-overload-bit <cr>
```

Handler ` RVA 0x11A9D2E0 `；selector ` 0 `；EOL ` RVA 0x355D9140 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-67ca4245f43307d7](../../evidence/conditions-sets-040.md#c-67ca4245f43307d7) · [状态效果 S-69d60448dc149398](../../evidence/state_effects-sets-023.md#s-69d60448dc149398)

### observed_connections-002200

```text
(config-router-af)# no shutdown <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 29 `；EOL ` RVA 0x35637730 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b1c8e1c934e6cb27](../../evidence/conditions-sets-069.md#c-b1c8e1c934e6cb27) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002223

```text
(config-router-af)# no snmp context <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 0 `；EOL ` RVA 0x33C455F0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7598dc8aeb3669dc](../../evidence/conditions-sets-046.md#c-7598dc8aeb3669dc) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002581

```text
(config-router-af)# no snmp context <string> community <string> <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 2 `；EOL ` RVA 0x33C45118 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Context Name；` string ` SNMP community string。

[条件 C-5a416169412196ba](../../evidence/conditions-sets-035.md#c-5a416169412196ba) · [参数 P-9b6eb89831feec60](../../evidence/parameters-sets-012.md#p-9b6eb89831feec60) · [状态效果 S-031c53bc2bf032b8](../../evidence/state_effects-sets-001.md#s-031c53bc2bf032b8)

### observed_connections-002580

```text
(config-router-af)# no snmp context <string> user <string> <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 23 `；EOL ` RVA 0x33C456D0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Context Name；` string ` Name of the user。

[条件 C-c27aae31069e8d90](../../evidence/conditions-sets-075.md#c-c27aae31069e8d90) · [参数 P-cfc42ec8ad667e32](../../evidence/parameters-sets-016.md#p-cfc42ec8ad667e32) · [状态效果 S-e2680dfbbe0df7b6](../../evidence/state_effects-sets-048.md#s-e2680dfbbe0df7b6)

### observed_connections-002116

```text
(config-router-af)# no spf-interval <cr>
```

Handler ` RVA 0x11A9D640 `；selector ` 0 `；EOL ` RVA 0x355D8820 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5e1691961acba8d4](../../evidence/conditions-sets-037.md#c-5e1691961acba8d4) · [状态效果 S-191bfde089e4b869](../../evidence/state_effects-sets-006.md#s-191bfde089e4b869)

### observed_connections-002362

```text
(config-router-af)# no statistics rib-timings <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 5 `；EOL ` RVA 0x35636D00 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4f35057ca9207cf3](../../evidence/conditions-sets-031.md#c-4f35057ca9207cf3) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002415

```text
(config-router-af)# no summary-prefix <address> <address> <cr>
```

Handler ` RVA 0xE1DF4C0 `；selector ` 0 `；EOL ` RVA 0x34267798 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` IP summary address；` address ` Summary mask。

[条件 C-f2a4b45f057f85a6](../../evidence/conditions-sets-094.md#c-f2a4b45f057f85a6) · [参数 P-d8789ea12de23037](../../evidence/parameters-sets-016.md#p-d8789ea12de23037) · [状态效果 S-8b5e79de14dc6f87](../../evidence/state_effects-sets-030.md#s-8b5e79de14dc6f87)

### observed_connections-002222

```text
(config-router-af)# no summary-prefix <address> <cr>
```

Handler ` RVA 0xE1DF4C0 `；selector ` 21 `；EOL ` RVA 0x34267D78 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` IP summary address。

[条件 C-e6b39bc8143fdcae](../../evidence/conditions-sets-089.md#c-e6b39bc8143fdcae) · [参数 P-53019655abc62157](../../evidence/parameters-sets-007.md#p-53019655abc62157) · [状态效果 S-8b5e79de14dc6f87](../../evidence/state_effects-sets-030.md#s-8b5e79de14dc6f87)

### observed_connections-002081

```text
(config-router-af)# no table-map <cr>
```

Handler ` RVA 0xE1F4690 `；selector ` 0 `；EOL ` RVA 0x3563C698 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e1d4efeb7a797491](../../evidence/conditions-sets-087.md#c-e1d4efeb7a797491) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002098

```text
(config-router-af)# no table-map <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 17 `；EOL ` RVA 0x3563AB08 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-fa8578ceaa01653e](../../evidence/conditions-sets-097.md#c-fa8578ceaa01653e) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002183

```text
(config-router-af)# no table-map <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 17 `；EOL ` RVA 0x355DDBD0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-2ca1c5ff0d602694](../../evidence/conditions-sets-017.md#c-2ca1c5ff0d602694) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002217

```text
(config-router-af)# no timers basic <cr>
```

Handler ` RVA 0xE1F2D60 `；selector ` 0 `；EOL ` RVA 0x34266D98 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a212333c9404b844](../../evidence/conditions-sets-063.md#c-a212333c9404b844) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002221

```text
(config-router-af)# no timers lsa arrival <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 39 `；EOL ` RVA 0x3565ADC0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e7d2f045f74d1960](../../evidence/conditions-sets-090.md#c-e7d2f045f74d1960) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002082

```text
(config-router-af)# no timers lsa-arrival <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 34 `；EOL ` RVA 0x3565B378 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-63ef0bf002bf640e](../../evidence/conditions-sets-039.md#c-63ef0bf002bf640e) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002070

```text
(config-router-af)# no timers lsa-group-pacing <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 35 `；EOL ` RVA 0x3565ADE8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c2f6f639ed527ac4](../../evidence/conditions-sets-075.md#c-c2f6f639ed527ac4) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002083

```text
(config-router-af)# no timers lsa-interval <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 33 `；EOL ` RVA 0x3565B350 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a7f39ac4c44c904d](../../evidence/conditions-sets-065.md#c-a7f39ac4c44c904d) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002241

```text
(config-router-af)# no timers pacing flood <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 36 `；EOL ` RVA 0x3565B948 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c69e66ab3b52c9e9](../../evidence/conditions-sets-077.md#c-c69e66ab3b52c9e9) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002235

```text
(config-router-af)# no timers pacing lsa-group <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 35 `；EOL ` RVA 0x3565B8E0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-955d8380395fc37d](../../evidence/conditions-sets-058.md#c-955d8380395fc37d) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002249

```text
(config-router-af)# no timers pacing retransmission <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 37 `；EOL ` RVA 0x3565BBE8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-699b0070eaf5149c](../../evidence/conditions-sets-041.md#c-699b0070eaf5149c) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002419

```text
(config-router-af)# no timers throttle lsa <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 40 `；EOL ` RVA 0x3565AA90 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-9e8514aade83a6a2](../../evidence/conditions-sets-061.md#c-9e8514aade83a6a2) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002417

```text
(config-router-af)# no timers throttle spf <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 38 `；EOL ` RVA 0x3565A6D8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a67ebb5390f8f9d6](../../evidence/conditions-sets-064.md#c-a67ebb5390f8f9d6) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002211

```text
(config-router-af)# no topology base <cr>
```

Handler ` RVA 0xE1FE420 `；selector ` 0 `；EOL ` RVA 0x34276FB0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-aaa6798a83870932](../../evidence/conditions-sets-066.md#c-aaa6798a83870932) · [状态效果 S-bd8bd92091e4bc02](../../evidence/state_effects-sets-040.md#s-bd8bd92091e4bc02)

### observed_connections-002410

```text
(config-router-af)# no traffic-share min across-interfaces <cr>
```

Handler ` RVA 0xE1FA2E0 `；selector ` 0 `；EOL ` RVA 0x342668D8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c42a533f81769524](../../evidence/conditions-sets-076.md#c-c42a533f81769524) · [状态效果 S-b19df422ba00788d](../../evidence/state_effects-sets-038.md#s-b19df422ba00788d)

### observed_connections-002279

```text
(config-router-af)# no ucmp local <cr>
```

Handler ` RVA 0x11A9D7F0 `；selector ` 0 `；EOL ` RVA 0x355DA020 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-16ab5bc2f25fa705](../../evidence/conditions-sets-009.md#c-16ab5bc2f25fa705) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002056

```text
(config-router-af)# no validate-update-source <cr>
```

Handler ` RVA 0xE1FA930 `；selector ` 0 `；EOL ` RVA 0x34267288 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-3d6ebdf7688aabe1](../../evidence/conditions-sets-024.md#c-3d6ebdf7688aabe1) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002060

```text
(config-router-af)# no version <cr>
```

Handler ` RVA 0xFB4F020 `；selector ` 0 `；EOL ` RVA 0x348210B0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ea1aee812a1acbb0](../../evidence/conditions-sets-090.md#c-ea1aee812a1acbb0) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002422

```text
(config-router-af)# offset-list <number:0..99> in <number:0..16> <cr>
```

Handler ` RVA 0xE1F1330 `；selector ` 0 `；EOL ` RVA 0x3426BED8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Access list of networks to apply offset (0 selects all networks)；` unsigned_number ` Offset。

[条件 C-88037b3171be58a4](../../evidence/conditions-sets-053.md#c-88037b3171be58a4) · [参数 P-814e2ed4cd2a86ee](../../evidence/parameters-sets-010.md#p-814e2ed4cd2a86ee) · [状态效果 S-9d4837426d6dab71](../../evidence/state_effects-sets-033.md#s-9d4837426d6dab71)

### observed_connections-002645

```text
(config-router-af)# offset-list <number:0..99> in <number:0..16> <interface> <cr>
```

Handler ` RVA 0xE1F1330 `；selector ` 0 `；EOL ` RVA 0x3426BED8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Access list of networks to apply offset (0 selects all networks)；` unsigned_number ` Offset。

[条件 C-5ad69b524f480142](../../evidence/conditions-sets-036.md#c-5ad69b524f480142) · [缺口 G-1417f9cd945e58da](../../evidence/gaps-sets-001.md#g-1417f9cd945e58da) · [参数 P-d0438f0a9801cf59](../../evidence/parameters-sets-016.md#p-d0438f0a9801cf59) · [状态效果 S-9d4837426d6dab71](../../evidence/state_effects-sets-033.md#s-9d4837426d6dab71)

### observed_connections-002039

```text
(config-router-af)# omp-route-tag <cr>
```

Handler ` RVA 0xE1F7FD0 `；selector ` 0 `；EOL ` RVA 0x342712A8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-24312fafa4a6145a](../../evidence/conditions-sets-014.md#c-24312fafa4a6145a)

### observed_connections-002015

```text
(config-router-af)# output-delay <number:8..50> <cr>
```

Handler ` RVA 0xE1F4590 `；selector ` 0 `；EOL ` RVA 0x3426B930 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Delay in milliseconds。

[条件 C-a1b29672199001a2](../../evidence/conditions-sets-062.md#c-a1b29672199001a2) · [参数 P-050e744f1f0a0679](../../evidence/parameters-sets-001.md#p-050e744f1f0a0679)

### observed_connections-002018

```text
(config-router-af)# packet-size <number:576..10000> <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 41 `；EOL ` RVA 0x35636CC0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` OSPFV3 Router Mode Packet Size。

[条件 C-f2e6d294f197372a](../../evidence/conditions-sets-094.md#c-f2e6d294f197372a) · [参数 P-6946bf835de0f2aa](../../evidence/parameters-sets-008.md#p-6946bf835de0f2aa)

### observed_connections-002616

```text
(config-router-af)# passive-interface <interface> <cr>
```

Handler ` RVA 0xE1F3960 `；selector ` 0 `；EOL ` RVA 0x3426B520 `。

模式根 ` RVA 0x34265950 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-036807abb994d30d](../../evidence/conditions-sets-002.md#c-036807abb994d30d) · [缺口 G-f3696827bfe36b06](../../evidence/gaps-sets-008.md#g-f3696827bfe36b06) · [参数 P-6c7df7ddba6b4979](../../evidence/parameters-sets-009.md#p-6c7df7ddba6b4979)

### observed_connections-002078

```text
(config-router-af)# passive-interface default <cr>
```

Handler ` RVA 0xE1F3960 `；selector ` 0 `；EOL ` RVA 0x3426B520 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-84bb3022e130a597](../../evidence/conditions-sets-051.md#c-84bb3022e130a597) · [状态效果 S-629ee0e040faa4eb](../../evidence/state_effects-sets-021.md#s-629ee0e040faa4eb)

### observed_connections-002129

```text
(config-router-af)# prc-interval <number:1..120> <cr>
```

Handler ` RVA 0x11A9D490 `；selector ` 0 `；EOL ` RVA 0x355D8CB8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Minimum PRC interval in seconds。

[条件 C-eca953328184c75a](../../evidence/conditions-sets-091.md#c-eca953328184c75a) · [参数 P-e1c1d572f52ad97c](../../evidence/parameters-sets-017.md#p-e1c1d572f52ad97c) · [状态效果 S-a61a8a62b976eb40](../../evidence/state_effects-sets-035.md#s-a61a8a62b976eb40)

### observed_connections-002035

```text
(config-router-af)# prefix-suppression <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 28 `；EOL ` RVA 0x35653C68 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bc2b2736fc868929](../../evidence/conditions-sets-073.md#c-bc2b2736fc868929)

### observed_connections-002050

```text
(config-router-af)# process-min-time percent <number:1..100> <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 16 `；EOL ` RVA 0x35637A38 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Minimum CPU quantum。

[条件 C-6312b9247298b8c7](../../evidence/conditions-sets-038.md#c-6312b9247298b8c7) · [参数 P-404a699d9eda5bb0](../../evidence/parameters-sets-005.md#p-404a699d9eda5bb0) · [状态效果 S-14d7bffd6a303558](../../evidence/state_effects-sets-005.md#s-14d7bffd6a303558)

### observed_connections-002287

```text
(config-router-af)# queue-depth hello unlimited <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 18 `；EOL ` RVA 0x35655210 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b8c3903a57d7978a](../../evidence/conditions-sets-071.md#c-b8c3903a57d7978a) · [状态效果 S-93780a8c63c8d342](../../evidence/state_effects-sets-031.md#s-93780a8c63c8d342)

### observed_connections-002293

```text
(config-router-af)# queue-depth update unlimited <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 17 `；EOL ` RVA 0x35655598 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c4de9a16142c414f](../../evidence/conditions-sets-076.md#c-c4de9a16142c414f) · [状态效果 S-43671c3d7762809d](../../evidence/state_effects-sets-015.md#s-43671c3d7762809d)

### observed_connections-002657

```text
(config-router-af)# redistribute <?ipv6_router_action@55558ab2eab8> <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 5 `；EOL ` RVA 0x355DBD88 `。

模式根 ` RVA 0x34265950 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-224c44699e2a7704](../../evidence/conditions-sets-013.md#c-224c44699e2a7704) · [缺口 G-5ef9c772fb7a6527](../../evidence/gaps-sets-004.md#g-5ef9c772fb7a6527) · [状态效果 S-61a6319fef3b7602](../../evidence/state_effects-sets-021.md#s-61a6319fef3b7602)

### observed_connections-002660

```text
(config-router-af)# redistribute <?ipv6_router_action@55558ab2eab8> level-1 into level-1 distribute-list <string> <cr>
```

Handler ` RVA 0x1E68EA00 `；selector ` 0 `；EOL ` RVA 0x355DAD58 `。

模式根 ` RVA 0x34265950 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` IPv6 prefix-list name。

[条件 C-d4b487275a5f739f](../../evidence/conditions-sets-082.md#c-d4b487275a5f739f) · [缺口 G-5ef9c772fb7a6527](../../evidence/gaps-sets-004.md#g-5ef9c772fb7a6527) · [参数 P-7a893ac9f52dea46](../../evidence/parameters-sets-010.md#p-7a893ac9f52dea46) · [状态效果 S-b95fb255b9eebeb1](../../evidence/state_effects-sets-039.md#s-b95fb255b9eebeb1)

### observed_connections-002659

```text
(config-router-af)# redistribute <?ipv6_router_action@55558ab8fd78> level-1 into level-1 distribute-list <string> <cr>
```

Handler ` RVA 0x1E68EA00 `；selector ` 0 `；EOL ` RVA 0x3563C028 `。

模式根 ` RVA 0x34265950 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` IPv6 prefix-list name。

[条件 C-9fe5e0871051ba8e](../../evidence/conditions-sets-062.md#c-9fe5e0871051ba8e) · [缺口 G-f3b9e44d72ce54ed](../../evidence/gaps-sets-008.md#g-f3b9e44d72ce54ed) · [参数 P-7c19476ba7e53e5d](../../evidence/parameters-sets-010.md#p-7c19476ba7e53e5d) · [状态效果 S-788f5b47d77c796b](../../evidence/state_effects-sets-026.md#s-788f5b47d77c796b)

### observed_connections-002620

```text
(config-router-af)# redistribute <?ipv6_router_action@55558ab90458> <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 5 `；EOL ` RVA 0x35638F60 `。

模式根 ` RVA 0x34265950 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f5697915d9ddcfb9](../../evidence/conditions-sets-095.md#c-f5697915d9ddcfb9) · [缺口 G-cd90f1a02cb918b0](../../evidence/gaps-sets-007.md#g-cd90f1a02cb918b0)

### observed_connections-002619

```text
(config-router-af)# redistribute <?router_action_proc_vpn@5555897bc948> <cr>
```

Handler ` RVA 0xE1E4550 `；selector ` 0 `；EOL ` RVA 0x34268518 `。

模式根 ` RVA 0x34265950 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c5669f12f2f053f4](../../evidence/conditions-sets-076.md#c-c5669f12f2f053f4) · [缺口 G-a0f21e837d8bd010](../../evidence/gaps-sets-006.md#g-a0f21e837d8bd010) · [状态效果 S-8352c635fee45823](../../evidence/state_effects-sets-028.md#s-8352c635fee45823)

### observed_connections-002661

```text
(config-router-af)# redistribute <?router_action_proc_vpn@5555897bc948> ip level-1 into level-1 route-map <string> <cr>
```

Handler ` RVA 0xCF982D0 `；selector ` 0 `；EOL ` RVA 0x3426AC88 `。

模式根 ` RVA 0x34265950 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Name of the route-map。

[条件 C-c289509269a99163](../../evidence/conditions-sets-075.md#c-c289509269a99163) · [缺口 G-b6105bf3dfb76fd0](../../evidence/gaps-sets-006.md#g-b6105bf3dfb76fd0) · [参数 P-bb4bba824f6da565](../../evidence/parameters-sets-014.md#p-bb4bba824f6da565) · [状态效果 S-10ad62f5527d9a92](../../evidence/state_effects-sets-004.md#s-10ad62f5527d9a92)

### observed_connections-002242

```text
(config-router-af)# redistribute maximum-prefix <number:1..4294967295> <cr>
```

Handler ` RVA 0xE1E4550 `；selector ` 0 `；EOL ` RVA 0x34268518 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Maximum number of IP prefixes redistributed。

[条件 C-00d44d05e220f661](../../evidence/conditions-sets-001.md#c-00d44d05e220f661) · [参数 P-01f351a1fdd1b68d](../../evidence/parameters-sets-001.md#p-01f351a1fdd1b68d) · [状态效果 S-6f2062dc2f61c040](../../evidence/state_effects-sets-024.md#s-6f2062dc2f61c040)

### observed_connections-002301

```text
(config-router-af)# redistribute maximum-prefix <number:1..4294967295> <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 5 `；EOL ` RVA 0x35638F60 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Maximum number of IPv6 prefixes redistributed。

[条件 C-3ebcbdb7e8a5b5a2](../../evidence/conditions-sets-024.md#c-3ebcbdb7e8a5b5a2) · [参数 P-9960a0f502201988](../../evidence/parameters-sets-012.md#p-9960a0f502201988) · [状态效果 S-8e47993621c800c3](../../evidence/state_effects-sets-030.md#s-8e47993621c800c3)

### observed_connections-002077

```text
(config-router-af)# router-id <address> <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 12 `；EOL ` RVA 0x356528F8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` OSPF router-id in IP address format。

[条件 C-2aeac0a432f0ec9b](../../evidence/conditions-sets-017.md#c-2aeac0a432f0ec9b) · [参数 P-6ece20d7591b40c9](../../evidence/parameters-sets-009.md#p-6ece20d7591b40c9)

### observed_connections-002617

```text
(config-router-af)# router-id <interface> <cr>
```

Handler ` RVA 0x11A9F520 `；selector ` 0 `；EOL ` RVA 0x355D7868 `。

模式根 ` RVA 0x34265950 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ea20369e128bbfae](../../evidence/conditions-sets-090.md#c-ea20369e128bbfae) · [缺口 G-d4958bbf2d83a217](../../evidence/gaps-sets-007.md#g-d4958bbf2d83a217) · [参数 P-a788c3067362ad1d](../../evidence/parameters-sets-013.md#p-a788c3067362ad1d)

### observed_connections-002261

```text
(config-router-af)# set-attached-bit route-map <string> <cr>
```

Handler ` RVA 0x11A9D130 `；selector ` 0 `；EOL ` RVA 0x355D9720 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Route map name。

[条件 C-02c4f008d525dc09](../../evidence/conditions-sets-002.md#c-02c4f008d525dc09) · [参数 P-3264bcfd15ffd820](../../evidence/parameters-sets-004.md#p-3264bcfd15ffd820)

### observed_connections-002038

```text
(config-router-af)# set-overload-bit <cr>
```

Handler ` RVA 0x11A9D2E0 `；selector ` 0 `；EOL ` RVA 0x355D9140 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-13aeb38be1d77a21](../../evidence/conditions-sets-008.md#c-13aeb38be1d77a21) · [状态效果 S-a0b117e577d89dc4](../../evidence/state_effects-sets-034.md#s-a0b117e577d89dc4)

### observed_connections-002051

```text
(config-router-af)# shutdown <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 29 `；EOL ` RVA 0x35637730 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b1c8e1c934e6cb27](../../evidence/conditions-sets-069.md#c-b1c8e1c934e6cb27)

### observed_connections-002069

```text
(config-router-af)# snmp context <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 0 `；EOL ` RVA 0x33C455F0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7598dc8aeb3669dc](../../evidence/conditions-sets-046.md#c-7598dc8aeb3669dc)

### observed_connections-002539

```text
(config-router-af)# snmp context <string> community <string> <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 2 `；EOL ` RVA 0x33C45118 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Context Name；` string ` SNMP community string。

[条件 C-7f44ea3d5ff83041](../../evidence/conditions-sets-049.md#c-7f44ea3d5ff83041) · [参数 P-9b6eb89831feec60](../../evidence/parameters-sets-012.md#p-9b6eb89831feec60) · [状态效果 S-8642eb04023b2323](../../evidence/state_effects-sets-028.md#s-8642eb04023b2323)

### observed_connections-002533

```text
(config-router-af)# snmp context <string> user <string> <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 23 `；EOL ` RVA 0x33C456D0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Context Name；` string ` Name of the user。

[条件 C-6568ff0a78495959](../../evidence/conditions-sets-039.md#c-6568ff0a78495959) · [参数 P-cfc42ec8ad667e32](../../evidence/parameters-sets-016.md#p-cfc42ec8ad667e32) · [状态效果 S-42394155f848a6f9](../../evidence/state_effects-sets-014.md#s-42394155f848a6f9)

### observed_connections-002136

```text
(config-router-af)# spf-interval <number:1..120> <cr>
```

Handler ` RVA 0x11A9D640 `；selector ` 0 `；EOL ` RVA 0x355D8820 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Minimum interval between consecutive SPFs in seconds。

[条件 C-f8cfc25e270987de](../../evidence/conditions-sets-096.md#c-f8cfc25e270987de) · [参数 P-ba906f0620e2ba31](../../evidence/parameters-sets-014.md#p-ba906f0620e2ba31) · [状态效果 S-1284734b3e23047f](../../evidence/state_effects-sets-004.md#s-1284734b3e23047f)

### observed_connections-002174

```text
(config-router-af)# statistics rib-timings <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 5 `；EOL ` RVA 0x35636D00 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4f35057ca9207cf3](../../evidence/conditions-sets-031.md#c-4f35057ca9207cf3)

### observed_connections-002225

```text
(config-router-af)# summary-prefix <address> <address> <cr>
```

Handler ` RVA 0xE1DF4C0 `；selector ` 0 `；EOL ` RVA 0x34267798 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP summary address；` address ` Summary mask。

[条件 C-f2a4b45f057f85a6](../../evidence/conditions-sets-094.md#c-f2a4b45f057f85a6) · [参数 P-d8789ea12de23037](../../evidence/parameters-sets-016.md#p-d8789ea12de23037) · [状态效果 S-40b38fba9068c658](../../evidence/state_effects-sets-014.md#s-40b38fba9068c658)

### observed_connections-002260

```text
(config-router-af)# summary-prefix <address> <address> <cr>
```

Handler ` RVA 0xE1DF4C0 `；selector ` 21 `；EOL ` RVA 0x34267D78 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP summary address；` address ` Summary mask。

[条件 C-78fc8789490487f3](../../evidence/conditions-sets-047.md#c-78fc8789490487f3) · [参数 P-9603a342d7ba9758](../../evidence/parameters-sets-012.md#p-9603a342d7ba9758) · [状态效果 S-36ffdcdc01e56410](../../evidence/state_effects-sets-012.md#s-36ffdcdc01e56410)

### observed_connections-002618

```text
(config-router-af)# summary-prefix <prefix:dynamic> <cr>
```

Handler ` RVA 0xE1DF4C0 `；selector ` 0 `；EOL ` RVA 0x34267798 `。

模式根 ` RVA 0x34265950 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` IP prefix &lt;network&gt;/&lt;length&gt;, e.g., 35.0.0.0/8。

[条件 C-a9ed48cb009e298f](../../evidence/conditions-sets-066.md#c-a9ed48cb009e298f) · [缺口 G-67786ad1f380b0c3](../../evidence/gaps-sets-004.md#g-67786ad1f380b0c3) · [参数 P-b0376545f9ff7bed](../../evidence/parameters-sets-013.md#p-b0376545f9ff7bed) · [状态效果 S-923d44d1a2180087](../../evidence/state_effects-sets-031.md#s-923d44d1a2180087)

### observed_connections-002621

```text
(config-router-af)# summary-prefix <prefix:dynamic> <cr>
```

Handler ` RVA 0x11BCD0C0 `；selector ` 0 `；EOL ` RVA 0x3563B638 `。

模式根 ` RVA 0x34265950 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` IPv6 prefix x:x::y/&lt;z&gt;。

[条件 C-f6508ab2d1cb8664](../../evidence/conditions-sets-095.md#c-f6508ab2d1cb8664) · [缺口 G-912360226c9d9418](../../evidence/gaps-sets-005.md#g-912360226c9d9418) · [参数 P-e5e6f93fe0b28759](../../evidence/parameters-sets-017.md#p-e5e6f93fe0b28759)

### observed_connections-002625

```text
(config-router-af)# summary-prefix <prefix:dynamic> <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 7 `；EOL ` RVA 0x355DC1F8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` IPv6 prefix x:x::y/&lt;z&gt;。

[条件 C-74169b3566e9c017](../../evidence/conditions-sets-045.md#c-74169b3566e9c017) · [缺口 G-225f39b010c3bb36](../../evidence/gaps-sets-002.md#g-225f39b010c3bb36) · [参数 P-010fd57c8b24426b](../../evidence/parameters-sets-001.md#p-010fd57c8b24426b)

### observed_connections-002093

```text
(config-router-af)# table-map <string> <cr>
```

Handler ` RVA 0xE1F4690 `；selector ` 0 `；EOL ` RVA 0x3563C698 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` route-map name。

[条件 C-a396a84ae57842f8](../../evidence/conditions-sets-063.md#c-a396a84ae57842f8) · [参数 P-89045b7c9889d8ad](../../evidence/parameters-sets-011.md#p-89045b7c9889d8ad)

### observed_connections-002109

```text
(config-router-af)# table-map <string> <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 17 `；EOL ` RVA 0x3563AB08 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` route-map name。

[条件 C-528b05915ee6cdae](../../evidence/conditions-sets-032.md#c-528b05915ee6cdae) · [参数 P-fc09c1735744be15](../../evidence/parameters-sets-019.md#p-fc09c1735744be15)

### observed_connections-002193

```text
(config-router-af)# table-map <string> <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 17 `；EOL ` RVA 0x355DDBD0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` route-map name。

[条件 C-0933513b628e608f](../../evidence/conditions-sets-004.md#c-0933513b628e608f) · [参数 P-2a2fec35e013d036](../../evidence/parameters-sets-004.md#p-2a2fec35e013d036)

### observed_connections-002517

```text
(config-router-af)# timers basic <number:1..2147483> <number:1..2147483> <number:0..2147483> <cr>
```

Handler ` RVA 0xE1F2D60 `；selector ` 0 `；EOL ` RVA 0x34266D98 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Interval between updates for RIP；` unsigned_number ` Invalid；` unsigned_number ` Holddown。

[条件 C-01197904dc525329](../../evidence/conditions-sets-001.md#c-01197904dc525329) · [参数 P-ec74659f805dd4da](../../evidence/parameters-sets-018.md#p-ec74659f805dd4da)

### observed_connections-002064

```text
(config-router-af)# timers lsa arrival <number:0..600000> <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 39 `；EOL ` RVA 0x3565ADC0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` The minimum interval in milliseconds between accepting the same LSA。

[条件 C-56c8edc1751cf287](../../evidence/conditions-sets-034.md#c-56c8edc1751cf287) · [参数 P-ec651a7091bede5d](../../evidence/parameters-sets-018.md#p-ec651a7091bede5d)

### observed_connections-002028

```text
(config-router-af)# timers lsa-arrival <number:0..600> <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 34 `；EOL ` RVA 0x3565B378 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` The minimum interval in sec between accepting the same LSA。

[条件 C-8298fa01eafa3019](../../evidence/conditions-sets-051.md#c-8298fa01eafa3019) · [参数 P-3e68484743c0ba47](../../evidence/parameters-sets-005.md#p-3e68484743c0ba47)

### observed_connections-002026

```text
(config-router-af)# timers lsa-group-pacing <number:10..1800> <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 35 `；EOL ` RVA 0x3565ADE8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Interval between group of LSA being refreshed or maxaged。

[条件 C-89dea12f696d06b4](../../evidence/conditions-sets-053.md#c-89dea12f696d06b4) · [参数 P-acc696baa070d206](../../evidence/parameters-sets-013.md#p-acc696baa070d206)

### observed_connections-002029

```text
(config-router-af)# timers lsa-interval <number:0..600> <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 33 `；EOL ` RVA 0x3565B350 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` The minimum interval in sec between originating the same LSA。

[条件 C-fa463c0bca204391](../../evidence/conditions-sets-097.md#c-fa463c0bca204391) · [参数 P-68ee749a3d4e2344](../../evidence/parameters-sets-008.md#p-68ee749a3d4e2344)

### observed_connections-002101

```text
(config-router-af)# timers pacing flood <number:5..100> <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 36 `；EOL ` RVA 0x3565B948 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` The minimum interval in msec to pace limit flooding on interface。

[条件 C-f33d3934aa538655](../../evidence/conditions-sets-094.md#c-f33d3934aa538655) · [参数 P-7a6944025c6d221b](../../evidence/parameters-sets-010.md#p-7a6944025c6d221b)

### observed_connections-002092

```text
(config-router-af)# timers pacing lsa-group <number:10..1800> <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 35 `；EOL ` RVA 0x3565B8E0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Interval in sec between group of LSA being refreshed or maxaged。

[条件 C-eede209bfcd8cf82](../../evidence/conditions-sets-092.md#c-eede209bfcd8cf82) · [参数 P-adc54e873f1490c4](../../evidence/parameters-sets-013.md#p-adc54e873f1490c4)

### observed_connections-002111

```text
(config-router-af)# timers pacing retransmission <number:5..200> <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 37 `；EOL ` RVA 0x3565BBE8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` The minimum interval in msec between neighbor retransmissions。

[条件 C-2c2d2d536fbe3ece](../../evidence/conditions-sets-017.md#c-2c2d2d536fbe3ece) · [参数 P-1e536f51d6e60db1](../../evidence/parameters-sets-003.md#p-1e536f51d6e60db1)

### observed_connections-002579

```text
(config-router-af)# timers throttle lsa <number:0..600000> <number:1..600000> <number:1..600000> <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 40 `；EOL ` RVA 0x3565AA90 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Delay to generate first occurrence of LSA in milliseconds；` unsigned_number ` Minimum delay between originating the same LSA in milliseconds；` unsigned_number ` Maximum delay between originating the same LSA in milliseconds。

[条件 C-ab22c7f16484ebd4](../../evidence/conditions-sets-066.md#c-ab22c7f16484ebd4) · [参数 P-1bea570352ad6be2](../../evidence/parameters-sets-003.md#p-1bea570352ad6be2)

### observed_connections-002578

```text
(config-router-af)# timers throttle spf <number:1..600000> <number:1..600000> <number:1..600000> <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 38 `；EOL ` RVA 0x3565A6D8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Delay between receiving a change to SPF calculation in milliseconds；` unsigned_number ` Delay between first and second SPF calculation in milliseconds；` unsigned_number ` Maximum wait time in milliseconds for SPF calculations。

[条件 C-38ffc9ed564aceb3](../../evidence/conditions-sets-022.md#c-38ffc9ed564aceb3) · [参数 P-5584b872328420bb](../../evidence/parameters-sets-007.md#p-5584b872328420bb)

### observed_connections-002637

```text
(config-router-af)# topology <string> tid <number:dynamic> <cr>
```

Handler ` RVA 0xE1FE420 `；selector ` 0 `；EOL ` RVA 0x34276FB0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Routing topology instance name；` unsigned_number_dynamic ` Routing topology tid。

[条件 C-ad9715bef8018850](../../evidence/conditions-sets-067.md#c-ad9715bef8018850) · [缺口 G-2bcf422352738b6d](../../evidence/gaps-sets-002.md#g-2bcf422352738b6d) · [参数 P-05f2b081a6bdba27](../../evidence/parameters-sets-001.md#p-05f2b081a6bdba27)

### observed_connections-002055

```text
(config-router-af)# topology base <cr>
```

Handler ` RVA 0xE1FE420 `；selector ` 0 `；EOL ` RVA 0x34276FB0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-aaa6798a83870932](../../evidence/conditions-sets-066.md#c-aaa6798a83870932) · [状态效果 S-4f0bc9234c67f83b](../../evidence/state_effects-sets-017.md#s-4f0bc9234c67f83b)

### observed_connections-002212

```text
(config-router-af)# traffic-share min across-interfaces <cr>
```

Handler ` RVA 0xE1FA2E0 `；selector ` 0 `；EOL ` RVA 0x342668D8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c42a533f81769524](../../evidence/conditions-sets-076.md#c-c42a533f81769524) · [状态效果 S-1028a5a981775501](../../evidence/state_effects-sets-004.md#s-1028a5a981775501)

### observed_connections-002137

```text
(config-router-af)# ucmp local <cr>
```

Handler ` RVA 0x11A9D7F0 `；selector ` 0 `；EOL ` RVA 0x355DA020 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-666b12af492907f5](../../evidence/conditions-sets-040.md#c-666b12af492907f5)

### observed_connections-002020

```text
(config-router-af)# validate-update-source <cr>
```

Handler ` RVA 0xE1FA930 `；selector ` 0 `；EOL ` RVA 0x34267288 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3d6ebdf7688aabe1](../../evidence/conditions-sets-024.md#c-3d6ebdf7688aabe1)

### observed_connections-002615

```text
(config-router-af)# version <number:1..2> <cr>
```

Handler ` RVA 0xFB4F020 `；selector ` 0 `；EOL ` RVA 0x348210B0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` rip version 1 or 2。

[条件 C-b879943f5f93addc](../../evidence/conditions-sets-071.md#c-b879943f5f93addc) · [缺口 G-9edadab1339c0e36](../../evidence/gaps-sets-006.md#g-9edadab1339c0e36) · [参数 P-5e744d5e0002072c](../../evidence/parameters-sets-008.md#p-5e744d5e0002072c) · [状态效果 S-57b9695adb26233c](../../evidence/state_effects-sets-019.md#s-57b9695adb26233c)

