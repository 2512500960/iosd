# address-family · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-002471

```text
(config-router-af)# adjacency stagger none disable <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 30 `；EOL ` RVA 0x356342A8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8d48960d36f6aeca](../../evidence/conditions-sets-055.md#c-8d48960d36f6aeca) · [状态效果 S-cbf6739612685c1b](../../evidence/state_effects-sets-043.md#s-cbf6739612685c1b)

### observed_connections-002024

```text
(config-router-af)# adjacency-check <cr>
```

Handler ` RVA 0x11A9B7D0 `；selector ` 0 `；EOL ` RVA 0x355D7C10 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a40c29f771cfb7a9](../../evidence/conditions-sets-063.md#c-a40c29f771cfb7a9)

### observed_connections-002084

```text
(config-router-af)# advertise passive-only <cr>
```

Handler ` RVA 0x11A9B4A0 `；selector ` 0 `；EOL ` RVA 0x355D7F70 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b0e43fe1b5b61dff](../../evidence/conditions-sets-068.md#c-b0e43fe1b5b61dff)

### observed_connections-002345

```text
(config-router-af)# aggregate-address <address> <address> <cr>
```

Handler ` RVA 0xF1B7BE0 `；selector ` 0 `；EOL ` RVA 0x356522E8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Aggregate address；` address ` Aggregate mask。

[条件 C-7d6f5f8bd8be27f9](../../evidence/conditions-sets-049.md#c-7d6f5f8bd8be27f9) · [参数 P-91466a4f32e65520](../../evidence/parameters-sets-011.md#p-91466a4f32e65520)

### observed_connections-002624

```text
(config-router-af)# area <address> <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 10 `；EOL ` RVA 0x35633B60 `。

模式根 ` RVA 0x34265950 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` OSPF area ID in IP address format。

[条件 C-d9bd6bceabba345e](../../evidence/conditions-sets-084.md#c-d9bd6bceabba345e) · [缺口 G-61692f9c73c92803](../../evidence/gaps-sets-004.md#g-61692f9c73c92803) · [参数 P-b7e0a72dd7aeec31](../../evidence/parameters-sets-014.md#p-b7e0a72dd7aeec31) · [状态效果 S-4af4dade414855c0](../../evidence/state_effects-sets-016.md#s-4af4dade414855c0)

### observed_connections-002638

```text
(config-router-af)# area <address> authentication key-chain <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 9 `；EOL ` RVA 0x35657308 `。

模式根 ` RVA 0x34265950 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` OSPF area ID in IP address format。

[条件 C-04f0fb8de6f15795](../../evidence/conditions-sets-002.md#c-04f0fb8de6f15795) · [缺口 G-61692f9c73c92803](../../evidence/gaps-sets-004.md#g-61692f9c73c92803) · [参数 P-b7e0a72dd7aeec31](../../evidence/parameters-sets-014.md#p-b7e0a72dd7aeec31) · [状态效果 S-04532ed679121afc](../../evidence/state_effects-sets-001.md#s-04532ed679121afc)

### observed_connections-002628

```text
(config-router-af)# area <address> default-cost <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 7 `；EOL ` RVA 0x356576E8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` OSPF area ID in IP address format。

[条件 C-95eebd05c91730ab](../../evidence/conditions-sets-058.md#c-95eebd05c91730ab) · [缺口 G-61692f9c73c92803](../../evidence/gaps-sets-004.md#g-61692f9c73c92803) · [参数 P-b7e0a72dd7aeec31](../../evidence/parameters-sets-014.md#p-b7e0a72dd7aeec31) · [状态效果 S-4af4dade414855c0](../../evidence/state_effects-sets-016.md#s-4af4dade414855c0)

### observed_connections-002651

```text
(config-router-af)# area <address> encryption ipsec spi <number:256..4294967295> <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 8 `；EOL ` RVA 0x35655E88 `。

模式根 ` RVA 0x34265950 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` OSPF area ID in IP address format；` unsigned_number ` SPI。

[条件 C-9981035b5de47c2a](../../evidence/conditions-sets-059.md#c-9981035b5de47c2a) · [缺口 G-61692f9c73c92803](../../evidence/gaps-sets-004.md#g-61692f9c73c92803) · [参数 P-805ac423394e1f6e](../../evidence/parameters-sets-010.md#p-805ac423394e1f6e) · [状态效果 S-9efa482782dac859](../../evidence/state_effects-sets-034.md#s-9efa482782dac859)

### observed_connections-002652

```text
(config-router-af)# area <address> filter-list prefix <string> in <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 11 `；EOL ` RVA 0x356337E0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` OSPF area ID in IP address format；` string ` Name of an IPv6 prefix-list。

[条件 C-9cb0ef452e442b39](../../evidence/conditions-sets-061.md#c-9cb0ef452e442b39) · [缺口 G-61692f9c73c92803](../../evidence/gaps-sets-004.md#g-61692f9c73c92803) · [参数 P-52a3505aed00b7bc](../../evidence/parameters-sets-007.md#p-52a3505aed00b7bc) · [状态效果 S-da3c34a53c83cc38](../../evidence/state_effects-sets-046.md#s-da3c34a53c83cc38)

### observed_connections-002635

```text
(config-router-af)# area <address> mpls <cr>
```

Handler ` RVA 0x11BC2300 `；selector ` 13 `；EOL ` RVA 0x35CD9040 `。

模式根 ` RVA 0x34265950 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` OSPF area ID in IP address format。

[条件 C-f21fbf794eb9d102](../../evidence/conditions-sets-093.md#c-f21fbf794eb9d102) · [缺口 G-61692f9c73c92803](../../evidence/gaps-sets-004.md#g-61692f9c73c92803) · [参数 P-b7e0a72dd7aeec31](../../evidence/parameters-sets-014.md#p-b7e0a72dd7aeec31) · [状态效果 S-4af4dade414855c0](../../evidence/state_effects-sets-016.md#s-4af4dade414855c0)

### observed_connections-002627

```text
(config-router-af)# area <address> no-transit <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 6 `；EOL ` RVA 0x35657C88 `。

模式根 ` RVA 0x34265950 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` OSPF area ID in IP address format。

[条件 C-808a5cf139aab098](../../evidence/conditions-sets-050.md#c-808a5cf139aab098) · [缺口 G-61692f9c73c92803](../../evidence/gaps-sets-004.md#g-61692f9c73c92803) · [参数 P-b7e0a72dd7aeec31](../../evidence/parameters-sets-014.md#p-b7e0a72dd7aeec31) · [状态效果 S-308a34e4d01c972d](../../evidence/state_effects-sets-011.md#s-308a34e4d01c972d)

### observed_connections-002631

```text
(config-router-af)# area <address> normal <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 5 `；EOL ` RVA 0x35658048 `。

模式根 ` RVA 0x34265950 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` OSPF area ID in IP address format。

[条件 C-4b378348630822f0](../../evidence/conditions-sets-030.md#c-4b378348630822f0) · [缺口 G-61692f9c73c92803](../../evidence/gaps-sets-004.md#g-61692f9c73c92803) · [参数 P-b7e0a72dd7aeec31](../../evidence/parameters-sets-014.md#p-b7e0a72dd7aeec31) · [状态效果 S-4af4dade414855c0](../../evidence/state_effects-sets-016.md#s-4af4dade414855c0)

### observed_connections-002633

```text
(config-router-af)# area <address> nssa <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 3 `；EOL ` RVA 0x35658950 `。

模式根 ` RVA 0x34265950 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` OSPF area ID in IP address format。

[条件 C-0e4af2a70b6f1d5b](../../evidence/conditions-sets-006.md#c-0e4af2a70b6f1d5b) · [缺口 G-61692f9c73c92803](../../evidence/gaps-sets-004.md#g-61692f9c73c92803) · [参数 P-b7e0a72dd7aeec31](../../evidence/parameters-sets-014.md#p-b7e0a72dd7aeec31) · [状态效果 S-4af4dade414855c0](../../evidence/state_effects-sets-016.md#s-4af4dade414855c0)

### observed_connections-002629

```text
(config-router-af)# area <address> packet-size <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 14 `；EOL ` RVA 0x35657A00 `。

模式根 ` RVA 0x34265950 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` OSPF area ID in IP address format。

[条件 C-6590a23fec90949c](../../evidence/conditions-sets-039.md#c-6590a23fec90949c) · [缺口 G-61692f9c73c92803](../../evidence/gaps-sets-004.md#g-61692f9c73c92803) · [参数 P-b7e0a72dd7aeec31](../../evidence/parameters-sets-014.md#p-b7e0a72dd7aeec31) · [状态效果 S-4af4dade414855c0](../../evidence/state_effects-sets-016.md#s-4af4dade414855c0)

### observed_connections-002649

```text
(config-router-af)# area <address> sham-link <address> <address> <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 12 `；EOL ` RVA 0x356332A8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` OSPF area ID in IP address format；` address ` IPv6 address associated with sham-link source；` address ` IPv6 address associated with sham-link destination。

[条件 C-bf70eecc980b528a](../../evidence/conditions-sets-074.md#c-bf70eecc980b528a) · [缺口 G-61692f9c73c92803](../../evidence/gaps-sets-004.md#g-61692f9c73c92803) · [参数 P-dc0c151599058369](../../evidence/parameters-sets-017.md#p-dc0c151599058369) · [状态效果 S-4af4dade414855c0](../../evidence/state_effects-sets-016.md#s-4af4dade414855c0)

### observed_connections-002632

```text
(config-router-af)# area <address> stub <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 4 `；EOL ` RVA 0x356583A8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` OSPF area ID in IP address format。

[条件 C-f1cc348c6cb09d27](../../evidence/conditions-sets-093.md#c-f1cc348c6cb09d27) · [缺口 G-61692f9c73c92803](../../evidence/gaps-sets-004.md#g-61692f9c73c92803) · [参数 P-b7e0a72dd7aeec31](../../evidence/parameters-sets-014.md#p-b7e0a72dd7aeec31) · [状态效果 S-4af4dade414855c0](../../evidence/state_effects-sets-016.md#s-4af4dade414855c0)

### observed_connections-002644

```text
(config-router-af)# area <address> virtual-link <address> <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 1 `；EOL ` RVA 0x356323C0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` OSPF area ID in IP address format；` address ` RouterID associated with virtual link neighbor。

[条件 C-57286b1644c65375](../../evidence/conditions-sets-034.md#c-57286b1644c65375) · [缺口 G-61692f9c73c92803](../../evidence/gaps-sets-004.md#g-61692f9c73c92803) · [参数 P-5332058f8a7ee0e0](../../evidence/parameters-sets-007.md#p-5332058f8a7ee0e0) · [状态效果 S-4af4dade414855c0](../../evidence/state_effects-sets-016.md#s-4af4dade414855c0)

### observed_connections-002444

```text
(config-router-af)# area <number:0..4294967295> authentication null <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 9 `；EOL ` RVA 0x35657308 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value。

[条件 C-a65ead456a7bc118](../../evidence/conditions-sets-064.md#c-a65ead456a7bc118) · [参数 P-c94ae0b4e794f02b](../../evidence/parameters-sets-015.md#p-c94ae0b4e794f02b) · [状态效果 S-e9874238df6d22ae](../../evidence/state_effects-sets-049.md#s-e9874238df6d22ae)

### observed_connections-002432

```text
(config-router-af)# area <number:0..4294967295> default-cost <number:0..16777214> <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 7 `；EOL ` RVA 0x356576E8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value；` unsigned_number ` Stub's advertised external route metric。

[条件 C-33cac9e550f6dfb8](../../evidence/conditions-sets-020.md#c-33cac9e550f6dfb8) · [参数 P-2bc9e7a51280783c](../../evidence/parameters-sets-004.md#p-2bc9e7a51280783c)

### observed_connections-002597

```text
(config-router-af)# area <number:0..4294967295> filter-list prefix <string> in <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 11 `；EOL ` RVA 0x356337E0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value；` string ` Name of an IPv6 prefix-list。

[条件 C-9cb0ef452e442b39](../../evidence/conditions-sets-061.md#c-9cb0ef452e442b39) · [参数 P-1a54c6728906f31d](../../evidence/parameters-sets-002.md#p-1a54c6728906f31d) · [状态效果 S-b6e0de29090c7a7e](../../evidence/state_effects-sets-039.md#s-b6e0de29090c7a7e)

### observed_connections-002355

```text
(config-router-af)# area <number:0..4294967295> mpls <cr>
```

Handler ` RVA 0x11BC2300 `；selector ` 13 `；EOL ` RVA 0x35CD9040 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value。

[条件 C-f21fbf794eb9d102](../../evidence/conditions-sets-093.md#c-f21fbf794eb9d102) · [参数 P-c94ae0b4e794f02b](../../evidence/parameters-sets-015.md#p-c94ae0b4e794f02b)

### observed_connections-002654

```text
(config-router-af)# area <number:0..4294967295> mpls traffic-engineering tunnel-tail ipv6 <interface> <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 13 `；EOL ` RVA 0x35CD8C80 `。

模式根 ` RVA 0x34265950 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value。

[条件 C-e8495af5e6387704](../../evidence/conditions-sets-090.md#c-e8495af5e6387704) · [缺口 G-dfcdfd1174df2cfb](../../evidence/gaps-sets-008.md#g-dfcdfd1174df2cfb) · [参数 P-ad136dbcac2f28cc](../../evidence/parameters-sets-013.md#p-ad136dbcac2f28cc) · [状态效果 S-5243d665f21f002a](../../evidence/state_effects-sets-018.md#s-5243d665f21f002a)

### observed_connections-002266

```text
(config-router-af)# area <number:0..4294967295> no-transit <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 6 `；EOL ` RVA 0x35657C88 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value。

[条件 C-808a5cf139aab098](../../evidence/conditions-sets-050.md#c-808a5cf139aab098) · [参数 P-c94ae0b4e794f02b](../../evidence/parameters-sets-015.md#p-c94ae0b4e794f02b) · [状态效果 S-6e7b8cb5c10bcec9](../../evidence/state_effects-sets-023.md#s-6e7b8cb5c10bcec9)

### observed_connections-002294

```text
(config-router-af)# area <number:0..4294967295> normal <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 5 `；EOL ` RVA 0x35658048 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value。

[条件 C-4b378348630822f0](../../evidence/conditions-sets-030.md#c-4b378348630822f0) · [参数 P-c94ae0b4e794f02b](../../evidence/parameters-sets-015.md#p-c94ae0b4e794f02b)

### observed_connections-002351

```text
(config-router-af)# area <number:0..4294967295> nssa <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 3 `；EOL ` RVA 0x35658950 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value。

[条件 C-0e4af2a70b6f1d5b](../../evidence/conditions-sets-006.md#c-0e4af2a70b6f1d5b) · [参数 P-c94ae0b4e794f02b](../../evidence/parameters-sets-015.md#p-c94ae0b4e794f02b)

### observed_connections-002433

```text
(config-router-af)# area <number:0..4294967295> packet-size <number:576..10000> <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 14 `；EOL ` RVA 0x35657A00 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value；` unsigned_number ` OSPFV3 Area Mode Packet Size。

[条件 C-d5ddeebfba4c225e](../../evidence/conditions-sets-083.md#c-d5ddeebfba4c225e) · [参数 P-1d792daa46ec43c6](../../evidence/parameters-sets-003.md#p-1d792daa46ec43c6)

### observed_connections-002554

```text
(config-router-af)# area <number:0..4294967295> range <address> <address> <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 2 `；EOL ` RVA 0x35658FF8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value；` address ` IPv4 address to match；` address ` IPv4 mask for address。

[条件 C-11df995e14425fe0](../../evidence/conditions-sets-007.md#c-11df995e14425fe0) · [参数 P-2c00c8203e3403e9](../../evidence/parameters-sets-004.md#p-2c00c8203e3403e9)

### observed_connections-002641

```text
(config-router-af)# area <number:0..4294967295> range <prefix:dynamic> <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 2 `；EOL ` RVA 0x35658FF8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value；` prefix_dynamic ` IPv6 prefix to match。

[条件 C-3f7e2fb209a59b5f](../../evidence/conditions-sets-025.md#c-3f7e2fb209a59b5f) · [缺口 G-cbd0d5eb33e7d81c](../../evidence/gaps-sets-007.md#g-cbd0d5eb33e7d81c) · [参数 P-54b0c62fa42a3fe9](../../evidence/parameters-sets-007.md#p-54b0c62fa42a3fe9)

### observed_connections-002559

```text
(config-router-af)# area <number:0..4294967295> sham-link <address> <address> <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 12 `；EOL ` RVA 0x356332A8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value；` address ` IPv6 address associated with sham-link source；` address ` IPv6 address associated with sham-link destination。

[条件 C-bf70eecc980b528a](../../evidence/conditions-sets-074.md#c-bf70eecc980b528a) · [参数 P-fbd2b1040e5ac880](../../evidence/parameters-sets-019.md#p-fbd2b1040e5ac880)

### observed_connections-002310

```text
(config-router-af)# area <number:0..4294967295> stub <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 4 `；EOL ` RVA 0x356583A8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value。

[条件 C-f1cc348c6cb09d27](../../evidence/conditions-sets-093.md#c-f1cc348c6cb09d27) · [参数 P-c94ae0b4e794f02b](../../evidence/parameters-sets-015.md#p-c94ae0b4e794f02b)

### observed_connections-002492

```text
(config-router-af)# area <number:0..4294967295> virtual-link <address> <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 1 `；EOL ` RVA 0x356323C0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value；` address ` RouterID associated with virtual link neighbor。

[条件 C-57286b1644c65375](../../evidence/conditions-sets-034.md#c-57286b1644c65375) · [参数 P-509320e887af2bfc](../../evidence/parameters-sets-007.md#p-509320e887af2bfc)

### observed_connections-002371

```text
(config-router-af)# authentication mode strict <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 31 `；EOL ` RVA 0x356368F8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7d3c2e1bb6f2b317](../../evidence/conditions-sets-049.md#c-7d3c2e1bb6f2b317) · [状态效果 S-41e8094b43a838ca](../../evidence/state_effects-sets-014.md#s-41e8094b43a838ca)

### observed_connections-002043

```text
(config-router-af)# auto-cost <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 0 `；EOL ` RVA 0x35635438 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-67c55366e9607aca](../../evidence/conditions-sets-040.md#c-67c55366e9607aca)

### observed_connections-002040

```text
(config-router-af)# auto-summary <cr>
```

Handler ` RVA 0xE1FA6B0 `；selector ` 0 `；EOL ` RVA 0x34270F08 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d09ca02f517d25b9](../../evidence/conditions-sets-080.md#c-d09ca02f517d25b9)

### observed_connections-002062

```text
(config-router-af)# bfd all-interfaces <cr>
```

Handler ` RVA 0x11A9ADD0 `；selector ` 0 `；EOL ` RVA 0x355D71B8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5aa50fbc9e8e7678](../../evidence/conditions-sets-035.md#c-5aa50fbc9e8e7678) · [状态效果 S-8c817b6d79c7038c](../../evidence/state_effects-sets-030.md#s-8c817b6d79c7038c)

### observed_connections-002130

```text
(config-router-af)# bfd all-interfaces <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 20 `；EOL ` RVA 0x356540B8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-15283135ebae1046](../../evidence/conditions-sets-008.md#c-15283135ebae1046)

### observed_connections-002108

```text
(config-router-af)# bfd check-ctrl-plane-failure <cr>
```

Handler ` RVA 0xE1FA610 `；selector ` 0 `；EOL ` RVA 0x3426CED8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b11f0f912f682171](../../evidence/conditions-sets-068.md#c-b11f0f912f682171) · [状态效果 S-f6920612f45686b8](../../evidence/state_effects-sets-052.md#s-f6920612f45686b8)

### observed_connections-002626

```text
(config-router-af)# bfd interface <interface> <cr>
```

Handler ` RVA 0xE1FA610 `；selector ` 0 `；EOL ` RVA 0x3426CED8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0bd449cdca7c60e2](../../evidence/conditions-sets-005.md#c-0bd449cdca7c60e2) · [缺口 G-f944427a1e594c0a](../../evidence/gaps-sets-009.md#g-f944427a1e594c0a) · [参数 P-61da23e59e024890](../../evidence/parameters-sets-008.md#p-61da23e59e024890)

### observed_connections-002308

```text
(config-router-af)# bgp additional-paths install <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 69 `；EOL ` RVA 0x35649B40 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e5e6e021d2e6e084](../../evidence/conditions-sets-089.md#c-e5e6e021d2e6e084) · [状态效果 S-8fd9c53d6f48eaab](../../evidence/state_effects-sets-031.md#s-8fd9c53d6f48eaab)

### observed_connections-002333

```text
(config-router-af)# bgp additional-paths select <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 71 `；EOL ` RVA 0x356497E8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5a7dca4852e6c561](../../evidence/conditions-sets-035.md#c-5a7dca4852e6c561)

### observed_connections-002134

```text
(config-router-af)# bgp advertise-best-external <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 70 `；EOL ` RVA 0x3564A990 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a6f686622702fc65](../../evidence/conditions-sets-064.md#c-a6f686622702fc65)

### observed_connections-002182

```text
(config-router-af)# bgp advertisement startup-delay <number:1..3600> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 95 `；EOL ` RVA 0x35642800 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` value (seconds)。

[条件 C-0f8d4ee386e0314b](../../evidence/conditions-sets-006.md#c-0f8d4ee386e0314b) · [参数 P-cb3fb324d51d65f2](../../evidence/parameters-sets-015.md#p-cb3fb324d51d65f2)

### observed_connections-002334

```text
(config-router-af)# bgp aggregate-timer <number:6..60> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 58 `；EOL ` RVA 0x356509E0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timer interval。

[条件 C-0dc3d46e141a1f5e](../../evidence/conditions-sets-006.md#c-0dc3d46e141a1f5e) · [参数 P-229a5aa224238f9f](../../evidence/parameters-sets-003.md#p-229a5aa224238f9f)

### observed_connections-002209

```text
(config-router-af)# bgp aigp-rib-metric <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 91 `；EOL ` RVA 0x35647280 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4a3c3ec86f257c8a](../../evidence/conditions-sets-029.md#c-4a3c3ec86f257c8a)

### observed_connections-002128

```text
(config-router-af)# bgp always-compare-med <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 5 `；EOL ` RVA 0x3563E0E8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8d3b3c9e2a55f0b9](../../evidence/conditions-sets-055.md#c-8d3b3c9e2a55f0b9)

### observed_connections-002286

```text
(config-router-af)# bgp asnotation dot <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 64 `；EOL ` RVA 0x3563E3F8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8d3b3c9e2a55f0b9](../../evidence/conditions-sets-055.md#c-8d3b3c9e2a55f0b9)

### observed_connections-002516

```text
(config-router-af)# bgp bestpath aigp ignore <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 43 `；EOL ` RVA 0x35645FA8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d76469a1f7a4873d](../../evidence/conditions-sets-083.md#c-d76469a1f7a4873d)

### observed_connections-002510

```text
(config-router-af)# bgp bestpath as-path ignore <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 17 `；EOL ` RVA 0x35645718 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4a3c3ec86f257c8a](../../evidence/conditions-sets-029.md#c-4a3c3ec86f257c8a)

### observed_connections-002512

```text
(config-router-af)# bgp bestpath as-path multipath-relax <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 51 `；EOL ` RVA 0x356459C0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4a3c3ec86f257c8a](../../evidence/conditions-sets-029.md#c-4a3c3ec86f257c8a)

### observed_connections-002392

```text
(config-router-af)# bgp bestpath compare-routerid <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 24 `；EOL ` RVA 0x35645C58 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4a3c3ec86f257c8a](../../evidence/conditions-sets-029.md#c-4a3c3ec86f257c8a)

### observed_connections-002515

```text
(config-router-af)# bgp bestpath cost-community ignore <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 41 `；EOL ` RVA 0x35646280 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4a3c3ec86f257c8a](../../evidence/conditions-sets-029.md#c-4a3c3ec86f257c8a)

### observed_connections-002441

```text
(config-router-af)# bgp bestpath igp-metric ignore <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 42 `；EOL ` RVA 0x3564A070 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5150ea47e3f03165](../../evidence/conditions-sets-032.md#c-5150ea47e3f03165)

### observed_connections-002513

```text
(config-router-af)# bgp bestpath med missing-as-worst <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 18 `；EOL ` RVA 0x35645408 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4a3c3ec86f257c8a](../../evidence/conditions-sets-029.md#c-4a3c3ec86f257c8a) · [状态效果 S-96c63bcb4f5b69e9](../../evidence/state_effects-sets-032.md#s-96c63bcb4f5b69e9)

### observed_connections-002454

```text
(config-router-af)# bgp bestpath prefix-validate allow-invalid <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 78 `；EOL ` RVA 0x3564A380 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8904f4b1b978efe3](../../evidence/conditions-sets-053.md#c-8904f4b1b978efe3)

### observed_connections-002461

```text
(config-router-af)# bgp bestpath prefix-validate disable <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 77 `；EOL ` RVA 0x3564A628 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8904f4b1b978efe3](../../evidence/conditions-sets-053.md#c-8904f4b1b978efe3)

### observed_connections-002318

```text
(config-router-af)# bgp client-to-client reflection <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 9 `；EOL ` RVA 0x3563F288 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-607bcdd6d486da42](../../evidence/conditions-sets-038.md#c-607bcdd6d486da42) · [状态效果 S-8df3a139ed50eb1b](../../evidence/state_effects-sets-030.md#s-8df3a139ed50eb1b)

### observed_connections-002650

```text
(config-router-af)# bgp client-to-client reflection intra-cluster cluster-id <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 9 `；EOL ` RVA 0x3563F288 `。

模式根 ` RVA 0x34265950 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c872aae957b41798](../../evidence/conditions-sets-077.md#c-c872aae957b41798) · [缺口 G-ebc5ca518716d68e](../../evidence/gaps-sets-008.md#g-ebc5ca518716d68e) · [状态效果 S-d63fcc78ecd5c08d](../../evidence/state_effects-sets-045.md#s-d63fcc78ecd5c08d)

### observed_connections-002315

```text
(config-router-af)# bgp cluster-id <number:1..4294967294> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 7 `；EOL ` RVA 0x3563EE50 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Route-Reflector Cluster-id as 32 bit quantity。

[条件 C-ef3bb0248fc1b3bf](../../evidence/conditions-sets-092.md#c-ef3bb0248fc1b3bf) · [参数 P-0206e231c2f58b45](../../evidence/parameters-sets-001.md#p-0206e231c2f58b45)

### observed_connections-002642

```text
(config-router-af)# bgp confederation identifier <?bgp_as4_action@55558ab94158> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 6 `；EOL ` RVA 0x35640190 `。

模式根 ` RVA 0x34265950 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8d3b3c9e2a55f0b9](../../evidence/conditions-sets-055.md#c-8d3b3c9e2a55f0b9) · [缺口 G-1f53d6dece303b85](../../evidence/gaps-sets-002.md#g-1f53d6dece303b85)

### observed_connections-002643

```text
(config-router-af)# bgp confederation peers <?bgp_as4_action@55558ab944c8> <cr>
```

Handler ` RVA 0xF1C67F0 `；selector ` 0 `；EOL ` RVA 0x35640608 `。

模式根 ` RVA 0x34265950 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-310af470451b2b8d](../../evidence/conditions-sets-019.md#c-310af470451b2b8d) · [缺口 G-8104d63552ebc1ea](../../evidence/gaps-sets-005.md#g-8104d63552ebc1ea) · [状态效果 S-c617a9a04576da1b](../../evidence/state_effects-sets-042.md#s-c617a9a04576da1b)

### observed_connections-002338

```text
(config-router-af)# bgp consistency-checker error-message <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 3 `；EOL ` RVA 0x3563E7D0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f9f6c57ee795c533](../../evidence/conditions-sets-097.md#c-f9f6c57ee795c533) · [状态效果 S-ca7cec4db722797e](../../evidence/state_effects-sets-043.md#s-ca7cec4db722797e)

### observed_connections-002324

```text
(config-router-af)# bgp consistency-checker error-message interval <number:5..1440> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 3 `；EOL ` RVA 0x3563E7F8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Interval (minutes)。

[条件 C-614a0897ad403b7f](../../evidence/conditions-sets-038.md#c-614a0897ad403b7f) · [参数 P-d35cf81a5b3705ca](../../evidence/parameters-sets-016.md#p-d35cf81a5b3705ca) · [状态效果 S-ca7cec4db722797e](../../evidence/state_effects-sets-043.md#s-ca7cec4db722797e)

### observed_connections-002138

```text
(config-router-af)# bgp dampening <cr>
```

Handler ` RVA 0xF1B85B0 `；selector ` 0 `；EOL ` RVA 0x35648C08 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-860ab3778ec6df21](../../evidence/conditions-sets-052.md#c-860ab3778ec6df21)

### observed_connections-002448

```text
(config-router-af)# bgp dampening route-map <string> <cr>
```

Handler ` RVA 0xF1B85B0 `；selector ` 8 `；EOL ` RVA 0x35648DD0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` route-map name。

[条件 C-2b82c88f4b4f2ef7](../../evidence/conditions-sets-017.md#c-2b82c88f4b4f2ef7) · [参数 P-ff9c86b08d367315](../../evidence/parameters-sets-019.md#p-ff9c86b08d367315)

### observed_connections-002442

```text
(config-router-af)# bgp default inter-as-hybrid advertise-source-routes <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 57 `；EOL ` RVA 0x35648240 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c666987e1ff102fc](../../evidence/conditions-sets-076.md#c-c666987e1ff102fc)

### observed_connections-002251

```text
(config-router-af)# bgp default ipv4-unicast <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 19 `；EOL ` RVA 0x35647998 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-833065ca9d9b5b4a](../../evidence/conditions-sets-051.md#c-833065ca9d9b5b4a)

### observed_connections-002264

```text
(config-router-af)# bgp default ipv6-nexthop <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 75 `；EOL ` RVA 0x35647C90 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-01297021f866bd84](../../evidence/conditions-sets-001.md#c-01297021f866bd84)

### observed_connections-002131

```text
(config-router-af)# bgp default local-preference <number:0..4294967295> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 0 `；EOL ` RVA 0x35647F20 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Configure default local preference value。

[条件 C-49183d6572cd9b57](../../evidence/conditions-sets-029.md#c-49183d6572cd9b57) · [参数 P-ed3f3f6cd1f560d5](../../evidence/parameters-sets-018.md#p-ed3f3f6cd1f560d5)

### observed_connections-002438

```text
(config-router-af)# bgp default route-target filter <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 25 `；EOL ` RVA 0x356485A8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2127c24ec9e7cb8b](../../evidence/conditions-sets-013.md#c-2127c24ec9e7cb8b)

### observed_connections-002439

```text
(config-router-af)# bgp default route-target filter <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 25 `；EOL ` RVA 0x35648848 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-49c39aa546553d15](../../evidence/conditions-sets-029.md#c-49c39aa546553d15)

### observed_connections-002165

```text
(config-router-af)# bgp deterministic-med <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 10 `；EOL ` RVA 0x35640908 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8d3b3c9e2a55f0b9](../../evidence/conditions-sets-055.md#c-8d3b3c9e2a55f0b9)

### observed_connections-002148

```text
(config-router-af)# bgp dmzlink-bw <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 31 `；EOL ` RVA 0x3564BF40 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-795d3aa0c1de4631](../../evidence/conditions-sets-047.md#c-795d3aa0c1de4631)

### observed_connections-002044

```text
(config-router-af)# bgp dynamic-med-interval <number:60..4294967295> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 21 `；EOL ` RVA 0x35640930 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Interval value (seconds)。

[条件 C-f0a2a08d4cf2c8b9](../../evidence/conditions-sets-093.md#c-f0a2a08d4cf2c8b9) · [参数 P-729ec843f96b20d3](../../evidence/parameters-sets-009.md#p-729ec843f96b20d3)

### observed_connections-002154

```text
(config-router-af)# bgp enforce-first-as <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 20 `；EOL ` RVA 0x3563FB38 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8d3b3c9e2a55f0b9](../../evidence/conditions-sets-055.md#c-8d3b3c9e2a55f0b9)

### observed_connections-002195

```text
(config-router-af)# bgp enhanced-error <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 82 `；EOL ` RVA 0x35642578 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9ca1f8a968e46463](../../evidence/conditions-sets-060.md#c-9ca1f8a968e46463)

### observed_connections-002100

```text
(config-router-af)# bgp fast-external-fallover <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 1 `；EOL ` RVA 0x3563D820 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8d3b3c9e2a55f0b9](../../evidence/conditions-sets-055.md#c-8d3b3c9e2a55f0b9)

### observed_connections-002205

```text
(config-router-af)# bgp graceful-restart <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 35 `；EOL ` RVA 0x356433E8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8d3b3c9e2a55f0b9](../../evidence/conditions-sets-055.md#c-8d3b3c9e2a55f0b9)

### observed_connections-002198

```text
(config-router-af)# bgp graceful-restart restart-time <number:1..3600> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 36 `；EOL ` RVA 0x35642DB8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Delay value (seconds)。

[条件 C-febcd0e7b236c9c4](../../evidence/conditions-sets-098.md#c-febcd0e7b236c9c4) · [参数 P-c0baaaa5aa926bc5](../../evidence/parameters-sets-015.md#p-c0baaaa5aa926bc5)

### observed_connections-002202

```text
(config-router-af)# bgp graceful-restart stalepath-time <number:1..3600> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 37 `；EOL ` RVA 0x35642E20 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Delay value (seconds)。

[条件 C-71b49adea8afffe5](../../evidence/conditions-sets-044.md#c-71b49adea8afffe5) · [参数 P-67feb0ceacbad203](../../evidence/parameters-sets-008.md#p-67feb0ceacbad203)

### observed_connections-002655

```text
(config-router-af)# bgp graceful-shutdown all vrfs <number:30..65535> community <?bgp_community_action@55558ab97d00> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 79 `；EOL ` RVA 0x35643850 `。

模式根 ` RVA 0x34265950 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` time in seconds。

[条件 C-bacbfb4ad03bcdd2](../../evidence/conditions-sets-072.md#c-bacbfb4ad03bcdd2) · [缺口 G-2b3899ca81bf8732](../../evidence/gaps-sets-002.md#g-2b3899ca81bf8732) · [参数 P-f5df2d4cb571c45c](../../evidence/parameters-sets-018.md#p-f5df2d4cb571c45c) · [状态效果 S-2232aa3b142d87ea](../../evidence/state_effects-sets-008.md#s-2232aa3b142d87ea)

### observed_connections-002566

```text
(config-router-af)# bgp graceful-shutdown all vrfs activate <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 79 `；EOL ` RVA 0x35643850 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0d112354600b2460](../../evidence/conditions-sets-005.md#c-0d112354600b2460) · [状态效果 S-f60e4b4c7f60197b](../../evidence/state_effects-sets-052.md#s-f60e4b4c7f60197b)

### observed_connections-002558

```text
(config-router-af)# bgp inject-map <string> exist-map <string> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 32 `；EOL ` RVA 0x3564DAB8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` route-map name；` string ` route-map name。

[条件 C-e56cedc33997c1c6](../../evidence/conditions-sets-088.md#c-e56cedc33997c1c6) · [参数 P-82a88d349cb24e9e](../../evidence/parameters-sets-010.md#p-82a88d349cb24e9e)

### observed_connections-002431

```text
(config-router-af)# bgp label-allocation-batch <number:0..4294967295> <number:0..4294967295> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 53 `；EOL ` RVA 0x3563DBB0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timer value in milliseconds；` unsigned_number ` Batch Size。

[条件 C-8d3b3c9e2a55f0b9](../../evidence/conditions-sets-055.md#c-8d3b3c9e2a55f0b9) · [参数 P-590ffc4a862cdd5b](../../evidence/parameters-sets-007.md#p-590ffc4a862cdd5b)

### observed_connections-002475

```text
(config-router-af)# bgp listen block <address> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 93 `；EOL ` RVA 0x3564B950 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IPv4 Dynamic Peering Address。

[条件 C-91f187ee957ea16a](../../evidence/conditions-sets-056.md#c-91f187ee957ea16a) · [参数 P-ff1855d12fccf3a2](../../evidence/parameters-sets-019.md#p-ff1855d12fccf3a2)

### observed_connections-002494

```text
(config-router-af)# bgp listen block <address> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 93 `；EOL ` RVA 0x356418B0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IPv4 Dynamic Peering Address。

[条件 C-861d4f86f990b125](../../evidence/conditions-sets-052.md#c-861d4f86f990b125) · [参数 P-8e142a50b5d2fd9e](../../evidence/parameters-sets-011.md#p-8e142a50b5d2fd9e)

### observed_connections-002158

```text
(config-router-af)# bgp listen limit <number:1..10000> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 61 `；EOL ` RVA 0x3564B898 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` max number。

[条件 C-8f67e1ab2d2cd115](../../evidence/conditions-sets-056.md#c-8f67e1ab2d2cd115) · [参数 P-3c6db21ba95b7577](../../evidence/parameters-sets-005.md#p-3c6db21ba95b7577)

### observed_connections-002186

```text
(config-router-af)# bgp listen limit <number:1..10000> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 61 `；EOL ` RVA 0x356417D0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` max number。

[条件 C-f1dc1f7b63338041](../../evidence/conditions-sets-093.md#c-f1dc1f7b63338041) · [参数 P-1d3cec81a4ef5dfc](../../evidence/parameters-sets-003.md#p-1d3cec81a4ef5dfc)

### observed_connections-002383

```text
(config-router-af)# bgp listen persistent <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 94 `；EOL ` RVA 0x35641BE8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-861d4f86f990b125](../../evidence/conditions-sets-052.md#c-861d4f86f990b125)

### observed_connections-002653

```text
(config-router-af)# bgp listen range <prefix:dynamic> peer-group <string> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 60 `；EOL ` RVA 0x35641428 `。

模式根 ` RVA 0x34265950 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` IPv4 subnet range；` string ` peer-group name。

[条件 C-55df07743a55828e](../../evidence/conditions-sets-034.md#c-55df07743a55828e) · [缺口 G-f55557118197c234](../../evidence/gaps-sets-008.md#g-f55557118197c234) · [参数 P-de0589aebb3010d3](../../evidence/parameters-sets-017.md#p-de0589aebb3010d3)

### observed_connections-002156

```text
(config-router-af)# bgp log-neighbor-changes <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 11 `；EOL ` RVA 0x3563FDE0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8d3b3c9e2a55f0b9](../../evidence/conditions-sets-055.md#c-8d3b3c9e2a55f0b9)

### observed_connections-002406

```text
(config-router-af)# bgp maxas-limit <number:1..254> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 26 `；EOL ` RVA 0x35646FF8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of ASes in the AS-PATH attribute(max 254)。

[条件 C-db3f9424cc68ac9b](../../evidence/conditions-sets-084.md#c-db3f9424cc68ac9b) · [参数 P-027af16bb5166596](../../evidence/parameters-sets-001.md#p-027af16bb5166596)

### observed_connections-002395

```text
(config-router-af)# bgp maxcommunity-limit <number:1..1018> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 27 `；EOL ` RVA 0x35646608 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of communities in the COMMUNITY attribute。

[条件 C-16692c1918b3d5c9](../../evidence/conditions-sets-009.md#c-16692c1918b3d5c9) · [参数 P-e38df3a125b13f4c](../../evidence/parameters-sets-017.md#p-e38df3a125b13f4c)

### observed_connections-002402

```text
(config-router-af)# bgp maxextcommunity-limit <number:1..509> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 29 `；EOL ` RVA 0x35646CA8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of extended communities in the EXTENDED COMMUNITY attribute。

[条件 C-052771cef4c40a9d](../../evidence/conditions-sets-002.md#c-052771cef4c40a9d) · [参数 P-80c5832a78a55dea](../../evidence/parameters-sets-010.md#p-80c5832a78a55dea)

### observed_connections-002398

```text
(config-router-af)# bgp maxlargecommunity-limit <number:1..339> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 28 `；EOL ` RVA 0x35646958 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of large communities in the LARGE COMMUNITY attribute。

[条件 C-b597d574afbd0eeb](../../evidence/conditions-sets-070.md#c-b597d574afbd0eeb) · [参数 P-00753c1aa9cc411e](../../evidence/parameters-sets-001.md#p-00753c1aa9cc411e)

### observed_connections-002176

```text
(config-router-af)# bgp mpls-local-label <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 81 `；EOL ` RVA 0x3564DE30 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-92af687f7671312c](../../evidence/conditions-sets-057.md#c-92af687f7671312c)

### observed_connections-002480

```text
(config-router-af)# bgp nexthop route-map <string> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 56 `；EOL ` RVA 0x3564C6A8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` route-map name。

[条件 C-c23de0d6427bd68a](../../evidence/conditions-sets-075.md#c-c23de0d6427bd68a) · [参数 P-2fa3aa6823f1ec72](../../evidence/parameters-sets-004.md#p-2fa3aa6823f1ec72)

### observed_connections-002357

```text
(config-router-af)# bgp nexthop trigger critical-delay <number:0..100> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 48 `；EOL ` RVA 0x3564CC10 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Critical delay value (seconds)。

[条件 C-c41e13de93250ad9](../../evidence/conditions-sets-076.md#c-c41e13de93250ad9) · [参数 P-0454172f6a68b5f1](../../evidence/parameters-sets-001.md#p-0454172f6a68b5f1)

### observed_connections-002347

```text
(config-router-af)# bgp nexthop trigger delay <number:0..100> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 47 `；EOL ` RVA 0x3564C990 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Delay value (seconds)。

[条件 C-55abbe9aff56dcfa](../../evidence/conditions-sets-034.md#c-55abbe9aff56dcfa) · [参数 P-a04cd2c05724bc5e](../../evidence/parameters-sets-012.md#p-a04cd2c05724bc5e)

### observed_connections-002474

```text
(config-router-af)# bgp nexthop trigger enable <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 49 `；EOL ` RVA 0x3564C968 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-03a7874e9a6887cf](../../evidence/conditions-sets-002.md#c-03a7874e9a6887cf)

### observed_connections-002490

```text
(config-router-af)# bgp nopeerup-delay cold-boot <number:1..3600> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 74 `；EOL ` RVA 0x35642210 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Delay in seconds。

[条件 C-23578c788649caa5](../../evidence/conditions-sets-014.md#c-23578c788649caa5) · [参数 P-5c73c5e1db17e48e](../../evidence/parameters-sets-007.md#p-5c73c5e1db17e48e) · [状态效果 S-ab05ffe73364fd70](../../evidence/state_effects-sets-036.md#s-ab05ffe73364fd70)

### observed_connections-002303

```text
(config-router-af)# bgp recursion host <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 72 `；EOL ` RVA 0x3564AD08 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8f08c4361e706b21](../../evidence/conditions-sets-055.md#c-8f08c4361e706b21)

### observed_connections-002135

```text
(config-router-af)# bgp redistribute-internal <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 2 `；EOL ` RVA 0x3564F030 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5182e528ca172aef](../../evidence/conditions-sets-032.md#c-5182e528ca172aef)

### observed_connections-002507

```text
(config-router-af)# bgp refresh max-eor-time <number:600..3600> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 16 `；EOL ` RVA 0x356445E0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timer interval (seconds)。

[条件 C-6b3d2345721c168f](../../evidence/conditions-sets-041.md#c-6b3d2345721c168f) · [参数 P-47ff83c601a5f5de](../../evidence/parameters-sets-006.md#p-47ff83c601a5f5de)

### observed_connections-002503

```text
(config-router-af)# bgp refresh stalepath-time <number:600..3600> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 15 `；EOL ` RVA 0x35644270 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timer interval (seconds)。

[条件 C-e45991795b8d3d7a](../../evidence/conditions-sets-088.md#c-e45991795b8d3d7a) · [参数 P-27b4d8382265e706](../../evidence/parameters-sets-003.md#p-27b4d8382265e706)

### observed_connections-002388

```text
(config-router-af)# bgp regexp deterministic <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 44 `；EOL ` RVA 0x35644FF8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4a3c3ec86f257c8a](../../evidence/conditions-sets-029.md#c-4a3c3ec86f257c8a)

### observed_connections-002304

```text
(config-router-af)# bgp route-map priority <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 59 `；EOL ` RVA 0x356501C0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e552582f99054ab0](../../evidence/conditions-sets-088.md#c-e552582f99054ab0)

### observed_connections-002119

```text
(config-router-af)# bgp route-map-cache <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 34 `；EOL ` RVA 0x3563DE38 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8d3b3c9e2a55f0b9](../../evidence/conditions-sets-055.md#c-8d3b3c9e2a55f0b9)

### observed_connections-002299

```text
(config-router-af)# bgp router-id <address> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 4 `；EOL ` RVA 0x3563D1F0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Manually configured router identifier。

[条件 C-3f4bb428451e2836](../../evidence/conditions-sets-025.md#c-3f4bb428451e2836) · [参数 P-2501d206ad14b878](../../evidence/parameters-sets-003.md#p-2501d206ad14b878)

### observed_connections-002342

```text
(config-router-af)# bgp router-id auto-assign <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 4 `；EOL ` RVA 0x3564B3B8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b4abec82dea04a74](../../evidence/conditions-sets-070.md#c-b4abec82dea04a74) · [状态效果 S-bb32953739388e15](../../evidence/state_effects-sets-040.md#s-bb32953739388e15)

### observed_connections-002639

```text
(config-router-af)# bgp router-id interface <interface> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 4 `；EOL ` RVA 0x3563D1F0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4c47c8313f2ea6f4](../../evidence/conditions-sets-030.md#c-4c47c8313f2ea6f4) · [缺口 G-d9c72ce8d8ccdb9e](../../evidence/gaps-sets-008.md#g-d9c72ce8d8ccdb9e) · [参数 P-d25bc0f7ca325112](../../evidence/parameters-sets-016.md#p-d25bc0f7ca325112)

### observed_connections-002640

```text
(config-router-af)# bgp router-id interface <interface> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 4 `；EOL ` RVA 0x3564B3B8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3c1cc8b9421f5096](../../evidence/conditions-sets-023.md#c-3c1cc8b9421f5096) · [缺口 G-34ce5a1260a71a57](../../evidence/gaps-sets-002.md#g-34ce5a1260a71a57) · [参数 P-ef76a9e633be9205](../../evidence/parameters-sets-018.md#p-ef76a9e633be9205)

### observed_connections-002611

```text
(config-router-af)# bgp rpki server tcp <address> port <number:1..65535> refresh <number:1..65535> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 76 `；EOL ` RVA 0x35650FD8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IPv6 address of RPKI cache server；` unsigned_number ` Port number；` unsigned_number ` Refresh time in seconds。

[条件 C-403177562c0694ce](../../evidence/conditions-sets-025.md#c-403177562c0694ce) · [参数 P-8c5c351bae1730a5](../../evidence/parameters-sets-011.md#p-8c5c351bae1730a5)

### observed_connections-002360

```text
(config-router-af)# bgp rr-group <string> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 23 `；EOL ` RVA 0x3564D650 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Extended community-list name。

[条件 C-7ef6c35fd5d4df5a](../../evidence/conditions-sets-049.md#c-7ef6c35fd5d4df5a) · [参数 P-fa7b8fb8f893a458](../../evidence/parameters-sets-019.md#p-fa7b8fb8f893a458)

### observed_connections-002210

```text
(config-router-af)# bgp safe-ebgp-policy <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 92 `；EOL ` RVA 0x35647590 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ffea2d982084ee65](../../evidence/conditions-sets-099.md#c-ffea2d982084ee65)

### observed_connections-002353

```text
(config-router-af)# bgp scan-time <number:5..60> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 22 `；EOL ` RVA 0x3564D2E0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Scanner interval (seconds)。

[条件 C-8b3598aecea70031](../../evidence/conditions-sets-054.md#c-8b3598aecea70031) · [参数 P-d09d1b488454b2d8](../../evidence/parameters-sets-016.md#p-d09d1b488454b2d8)

### observed_connections-002313

```text
(config-router-af)# bgp slow-peer detection <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 67 `；EOL ` RVA 0x3564E300 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a6d72067809bcaf7](../../evidence/conditions-sets-064.md#c-a6d72067809bcaf7)

### observed_connections-002307

```text
(config-router-af)# bgp slow-peer detection threshold <number:120..3600> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 67 `；EOL ` RVA 0x3564E2D8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Threshold value (seconds)。

[条件 C-99bb36fbe1242f81](../../evidence/conditions-sets-059.md#c-99bb36fbe1242f81) · [参数 P-c2b7ec5ec51dc8c1](../../evidence/parameters-sets-015.md#p-c2b7ec5ec51dc8c1)

### observed_connections-002467

```text
(config-router-af)# bgp slow-peer split-update-group dynamic <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 68 `；EOL ` RVA 0x3564E8D0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-23fdd7ebef9a3ebf](../../evidence/conditions-sets-014.md#c-23fdd7ebef9a3ebf)

### observed_connections-002489

```text
(config-router-af)# bgp snmp traps add-type <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 90 `；EOL ` RVA 0x35640EF8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8d3b3c9e2a55f0b9](../../evidence/conditions-sets-055.md#c-8d3b3c9e2a55f0b9)

### observed_connections-002157

```text
(config-router-af)# bgp soft-reconfig-backup <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 52 `；EOL ` RVA 0x3564C290 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6b8a08d64cffcc48](../../evidence/conditions-sets-042.md#c-6b8a08d64cffcc48)

### observed_connections-002548

```text
(config-router-af)# bgp sourced-paths per-net isis all <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 89 `；EOL ` RVA 0x3564FE40 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff436232114b2225](../../evidence/conditions-sets-098.md#c-ff436232114b2225) · [状态效果 S-96634b6566867e17](../../evidence/state_effects-sets-032.md#s-96634b6566867e17)

### observed_connections-002543

```text
(config-router-af)# bgp sourced-paths per-net ospf all <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 87 `；EOL ` RVA 0x3564F7E0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff436232114b2225](../../evidence/conditions-sets-098.md#c-ff436232114b2225) · [状态效果 S-964fb723ec600af5](../../evidence/state_effects-sets-032.md#s-964fb723ec600af5)

### observed_connections-002544

```text
(config-router-af)# bgp sourced-paths per-net ospfv3 all <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 88 `；EOL ` RVA 0x3564FB28 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff436232114b2225](../../evidence/conditions-sets-098.md#c-ff436232114b2225) · [状态效果 S-c40dd3ca93c646e4](../../evidence/state_effects-sets-041.md#s-c40dd3ca93c646e4)

### observed_connections-002540

```text
(config-router-af)# bgp sourced-paths per-net static all <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 86 `；EOL ` RVA 0x3564F498 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff436232114b2225](../../evidence/conditions-sets-098.md#c-ff436232114b2225) · [状态效果 S-151694b269970eaa](../../evidence/state_effects-sets-005.md#s-151694b269970eaa)

### observed_connections-002384

```text
(config-router-af)# bgp sso route-refresh-enable <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 38 `；EOL ` RVA 0x35643EB0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4a3c3ec86f257c8a](../../evidence/conditions-sets-029.md#c-4a3c3ec86f257c8a)

### observed_connections-002140

```text
(config-router-af)# bgp suppress-inactive <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 45 `；EOL ` RVA 0x3564B008 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-488f3c121a9ac3ba](../../evidence/conditions-sets-028.md#c-488f3c121a9ac3ba)

### observed_connections-002027

```text
(config-router-af)# bgp tid <number:1..255> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 55 `；EOL ` RVA 0x3563CA30 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Tolology identifier value。

[条件 C-eb6a5d7f60e93fc9](../../evidence/conditions-sets-091.md#c-eb6a5d7f60e93fc9) · [参数 P-b823d9b17a444eae](../../evidence/parameters-sets-014.md#p-b823d9b17a444eae)

### observed_connections-002314

```text
(config-router-af)# bgp transport path-mtu-discovery <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 50 `；EOL ` RVA 0x3563F8A8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8d3b3c9e2a55f0b9](../../evidence/conditions-sets-055.md#c-8d3b3c9e2a55f0b9)

### observed_connections-002048

```text
(config-router-af)# bgp update-delay <number:1..3600> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 30 `；EOL ` RVA 0x35642828 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Delay value (seconds)。

[条件 C-56db78740a3d571e](../../evidence/conditions-sets-034.md#c-56db78740a3d571e) · [参数 P-508be89c30de91b2](../../evidence/parameters-sets-007.md#p-508be89c30de91b2)

### observed_connections-002446

```text
(config-router-af)# bgp update-group split as-override <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 73 `；EOL ` RVA 0x3564ECA0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-779c8c2bed6dd3fc](../../evidence/conditions-sets-047.md#c-779c8c2bed6dd3fc)

### observed_connections-002110

```text
(config-router-af)# bgp upgrade-cli <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 33 `；EOL ` RVA 0x3563CE48 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-054935b640257f09](../../evidence/conditions-sets-002.md#c-054935b640257f09)

### observed_connections-002545

```text
(config-router-af)# bgp va <address> mask <address> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 80 `；EOL ` RVA 0x35650568 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` BGP VA ip address；` address ` BGP VA mask address。

[条件 C-d4d68cc832b0bf25](../../evidence/conditions-sets-082.md#c-d4d68cc832b0bf25) · [参数 P-aa96ac06c7a0d6a9](../../evidence/parameters-sets-013.md#p-aa96ac06c7a0d6a9)

### observed_connections-002386

```text
(config-router-af)# bgp vrf-update-optimisation off <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 66 `；EOL ` RVA 0x35644968 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4a3c3ec86f257c8a](../../evidence/conditions-sets-029.md#c-4a3c3ec86f257c8a)

### observed_connections-002509

```text
(config-router-af)# bgp write-limit <number:500..2147483647> <number:500..2147483647> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 40 `；EOL ` RVA 0x35644CC0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of messages to be formatted per neighbor/peergroup；` unsigned_number ` Number of messages that can be enqueued in total。

[条件 C-be81dd3c5c11623c](../../evidence/conditions-sets-074.md#c-be81dd3c5c11623c) · [参数 P-617439e95c19a450](../../evidence/parameters-sets-008.md#p-617439e95c19a450)

### observed_connections-002175

```text
(config-router-af)# capability vrf-lite <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 7 `；EOL ` RVA 0x35636500 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-57adb160f929a25e](../../evidence/conditions-sets-034.md#c-57adb160f929a25e) · [状态效果 S-fecc9a9150e082b9](../../evidence/state_effects-sets-054.md#s-fecc9a9150e082b9)

### observed_connections-002107

```text
(config-router-af)# compatible rfc1583 <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 25 `；EOL ` RVA 0x356544B8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cc5aafa1a170d7f5](../../evidence/conditions-sets-079.md#c-cc5aafa1a170d7f5)

### observed_connections-002117

```text
(config-router-af)# compatible rfc1587 <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 26 `；EOL ` RVA 0x356547B0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0a4ff46fd3afc43d](../../evidence/conditions-sets-004.md#c-0a4ff46fd3afc43d)

### observed_connections-002127

```text
(config-router-af)# compatible rfc5243 <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 27 `；EOL ` RVA 0x35654A80 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7ac4b67371877306](../../evidence/conditions-sets-048.md#c-7ac4b67371877306)

### observed_connections-002058

```text
(config-router-af)# context <string> <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 0 `；EOL ` RVA 0x33C44A60 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` SNMP Context Name。

[条件 C-9affa1869574e86e](../../evidence/conditions-sets-060.md#c-9affa1869574e86e) · [参数 P-f3e465802edc027f](../../evidence/parameters-sets-018.md#p-f3e465802edc027f) · [状态效果 S-355a44aeb0ea4c7f](../../evidence/state_effects-sets-012.md#s-355a44aeb0ea4c7f)

### observed_connections-002330

```text
(config-router-af)# default adjacency stagger <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 30 `；EOL ` RVA 0x356342A8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e471dfa03386fccc](../../evidence/conditions-sets-088.md#c-e471dfa03386fccc) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002071

```text
(config-router-af)# default adjacency-check <cr>
```

Handler ` RVA 0x11A9B7D0 `；selector ` 0 `；EOL ` RVA 0x355D7C10 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a40c29f771cfb7a9](../../evidence/conditions-sets-063.md#c-a40c29f771cfb7a9) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002236

```text
(config-router-af)# default advertise passive-only <cr>
```

Handler ` RVA 0x11A9B4A0 `；selector ` 0 `；EOL ` RVA 0x355D7F70 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b0e43fe1b5b61dff](../../evidence/conditions-sets-068.md#c-b0e43fe1b5b61dff) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002479

```text
(config-router-af)# default aggregate-address <address> <address> <cr>
```

Handler ` RVA 0xF1B7BE0 `；selector ` 0 `；EOL ` RVA 0x356522E8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` Aggregate address；` address ` Aggregate mask。

[条件 C-7d6f5f8bd8be27f9](../../evidence/conditions-sets-049.md#c-7d6f5f8bd8be27f9) · [参数 P-91466a4f32e65520](../../evidence/parameters-sets-011.md#p-91466a4f32e65520) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002359

```text
(config-router-af)# default area <number:0..4294967295> <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 10 `；EOL ` RVA 0x35633B60 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value。

[条件 C-bf798629afb2a8e4](../../evidence/conditions-sets-074.md#c-bf798629afb2a8e4) · [参数 P-c94ae0b4e794f02b](../../evidence/parameters-sets-015.md#p-c94ae0b4e794f02b) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002529

```text
(config-router-af)# default area <number:0..4294967295> authentication key-chain <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 9 `；EOL ` RVA 0x35657308 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value。

[条件 C-e9a22099a1020c67](../../evidence/conditions-sets-090.md#c-e9a22099a1020c67) · [参数 P-c94ae0b4e794f02b](../../evidence/parameters-sets-015.md#p-c94ae0b4e794f02b) · [状态效果 S-c8066037281d4919](../../evidence/state_effects-sets-042.md#s-c8066037281d4919)

### observed_connections-002436

```text
(config-router-af)# default area <number:0..4294967295> default-cost <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 7 `；EOL ` RVA 0x356576E8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value。

[条件 C-232964ccc640fe9d](../../evidence/conditions-sets-014.md#c-232964ccc640fe9d) · [参数 P-c94ae0b4e794f02b](../../evidence/parameters-sets-015.md#p-c94ae0b4e794f02b) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002607

```text
(config-router-af)# default area <number:0..4294967295> encryption ipsec spi <number:256..4294967295> <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 8 `；EOL ` RVA 0x35655E88 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value；` unsigned_number ` SPI。

[条件 C-3a62b8a7fce9e98b](../../evidence/conditions-sets-023.md#c-3a62b8a7fce9e98b) · [参数 P-0a7db9ba82254141](../../evidence/parameters-sets-001.md#p-0a7db9ba82254141) · [状态效果 S-2c7465159513186b](../../evidence/state_effects-sets-010.md#s-2c7465159513186b)

### observed_connections-002609

```text
(config-router-af)# default area <number:0..4294967295> filter-list prefix <string> in <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 11 `；EOL ` RVA 0x356337E0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value；` string ` Name of an IPv6 prefix-list。

[条件 C-9cb0ef452e442b39](../../evidence/conditions-sets-061.md#c-9cb0ef452e442b39) · [参数 P-1a54c6728906f31d](../../evidence/parameters-sets-002.md#p-1a54c6728906f31d) · [状态效果 S-6f4491bc6e397016](../../evidence/state_effects-sets-024.md#s-6f4491bc6e397016)

### observed_connections-002487

```text
(config-router-af)# default area <number:0..4294967295> mpls <cr>
```

Handler ` RVA 0x11BC2300 `；selector ` 13 `；EOL ` RVA 0x35CD9040 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value。

[条件 C-f21fbf794eb9d102](../../evidence/conditions-sets-093.md#c-f21fbf794eb9d102) · [参数 P-c94ae0b4e794f02b](../../evidence/parameters-sets-015.md#p-c94ae0b4e794f02b) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002435

```text
(config-router-af)# default area <number:0..4294967295> no-transit <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 6 `；EOL ` RVA 0x35657C88 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value。

[条件 C-808a5cf139aab098](../../evidence/conditions-sets-050.md#c-808a5cf139aab098) · [参数 P-c94ae0b4e794f02b](../../evidence/parameters-sets-015.md#p-c94ae0b4e794f02b) · [状态效果 S-770e99f342da5e32](../../evidence/state_effects-sets-025.md#s-770e99f342da5e32)

### observed_connections-002451

```text
(config-router-af)# default area <number:0..4294967295> normal <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 5 `；EOL ` RVA 0x35658048 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value。

[条件 C-4b378348630822f0](../../evidence/conditions-sets-030.md#c-4b378348630822f0) · [参数 P-c94ae0b4e794f02b](../../evidence/parameters-sets-015.md#p-c94ae0b4e794f02b) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002485

```text
(config-router-af)# default area <number:0..4294967295> nssa <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 3 `；EOL ` RVA 0x35658950 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value。

[条件 C-0e4af2a70b6f1d5b](../../evidence/conditions-sets-006.md#c-0e4af2a70b6f1d5b) · [参数 P-c94ae0b4e794f02b](../../evidence/parameters-sets-015.md#p-c94ae0b4e794f02b) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002437

```text
(config-router-af)# default area <number:0..4294967295> packet-size <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 14 `；EOL ` RVA 0x35657A00 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value。

[条件 C-ca91280e4d32a77d](../../evidence/conditions-sets-078.md#c-ca91280e4d32a77d) · [参数 P-c94ae0b4e794f02b](../../evidence/parameters-sets-015.md#p-c94ae0b4e794f02b) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002596

```text
(config-router-af)# default area <number:0..4294967295> range <address> <address> <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 2 `；EOL ` RVA 0x35658FF8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value；` address ` IPv4 address to match；` address ` IPv4 mask for address。

[条件 C-11df995e14425fe0](../../evidence/conditions-sets-007.md#c-11df995e14425fe0) · [参数 P-2c00c8203e3403e9](../../evidence/parameters-sets-004.md#p-2c00c8203e3403e9) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002601

```text
(config-router-af)# default area <number:0..4294967295> sham-link <address> <address> <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 12 `；EOL ` RVA 0x356332A8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value；` address ` IPv6 address associated with sham-link source；` address ` IPv6 address associated with sham-link destination。

[条件 C-bf70eecc980b528a](../../evidence/conditions-sets-074.md#c-bf70eecc980b528a) · [参数 P-fbd2b1040e5ac880](../../evidence/parameters-sets-019.md#p-fbd2b1040e5ac880) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002464

```text
(config-router-af)# default area <number:0..4294967295> stub <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 4 `；EOL ` RVA 0x356583A8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value。

[条件 C-f1cc348c6cb09d27](../../evidence/conditions-sets-093.md#c-f1cc348c6cb09d27) · [参数 P-c94ae0b4e794f02b](../../evidence/parameters-sets-015.md#p-c94ae0b4e794f02b) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002563

```text
(config-router-af)# default area <number:0..4294967295> virtual-link <address> <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 1 `；EOL ` RVA 0x356323C0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value；` address ` RouterID associated with virtual link neighbor。

[条件 C-57286b1644c65375](../../evidence/conditions-sets-034.md#c-57286b1644c65375) · [参数 P-509320e887af2bfc](../../evidence/parameters-sets-007.md#p-509320e887af2bfc) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002493

```text
(config-router-af)# default authentication mode strict <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 31 `；EOL ` RVA 0x356368F8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7d3c2e1bb6f2b317](../../evidence/conditions-sets-049.md#c-7d3c2e1bb6f2b317) · [状态效果 S-e42044f354c8de27](../../evidence/state_effects-sets-048.md#s-e42044f354c8de27)

### observed_connections-002166

```text
(config-router-af)# default auto-cost <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 0 `；EOL ` RVA 0x35635438 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-67c55366e9607aca](../../evidence/conditions-sets-040.md#c-67c55366e9607aca) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002149

```text
(config-router-af)# default auto-summary <cr>
```

Handler ` RVA 0xE1FA6B0 `；selector ` 0 `；EOL ` RVA 0x34270F08 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d09ca02f517d25b9](../../evidence/conditions-sets-080.md#c-d09ca02f517d25b9) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002220

```text
(config-router-af)# default bfd all-interfaces <cr>
```

Handler ` RVA 0x11A9ADD0 `；selector ` 0 `；EOL ` RVA 0x355D71B8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5aa50fbc9e8e7678](../../evidence/conditions-sets-035.md#c-5aa50fbc9e8e7678) · [状态效果 S-262b1679496f7cf8](../../evidence/state_effects-sets-009.md#s-262b1679496f7cf8)

### observed_connections-002281

```text
(config-router-af)# default bfd all-interfaces <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 20 `；EOL ` RVA 0x356540B8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-15283135ebae1046](../../evidence/conditions-sets-008.md#c-15283135ebae1046) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002253

```text
(config-router-af)# default bfd check-ctrl-plane-failure <cr>
```

Handler ` RVA 0xE1FA610 `；selector ` 0 `；EOL ` RVA 0x3426CED8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b11f0f912f682171](../../evidence/conditions-sets-068.md#c-b11f0f912f682171) · [状态效果 S-a3e46328eaa3e7dc](../../evidence/state_effects-sets-035.md#s-a3e46328eaa3e7dc)

### observed_connections-002462

```text
(config-router-af)# default bgp additional-paths install <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 69 `；EOL ` RVA 0x35649B40 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e5e6e021d2e6e084](../../evidence/conditions-sets-089.md#c-e5e6e021d2e6e084) · [状态效果 S-a83b8fd870f4ca3b](../../evidence/state_effects-sets-036.md#s-a83b8fd870f4ca3b)

### observed_connections-002470

```text
(config-router-af)# default bgp additional-paths select <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 71 `；EOL ` RVA 0x356497E8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5a7dca4852e6c561](../../evidence/conditions-sets-035.md#c-5a7dca4852e6c561) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002295

```text
(config-router-af)# default bgp advertise-best-external <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 70 `；EOL ` RVA 0x3564A990 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a6f686622702fc65](../../evidence/conditions-sets-064.md#c-a6f686622702fc65) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002372

```text
(config-router-af)# default bgp advertisement startup-delay <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 95 `；EOL ` RVA 0x35642800 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-de9157a35f1292a2](../../evidence/conditions-sets-086.md#c-de9157a35f1292a2) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002472

```text
(config-router-af)# default bgp aggregate-timer <number:6..60> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 58 `；EOL ` RVA 0x356509E0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Timer interval。

[条件 C-0dc3d46e141a1f5e](../../evidence/conditions-sets-006.md#c-0dc3d46e141a1f5e) · [参数 P-229a5aa224238f9f](../../evidence/parameters-sets-003.md#p-229a5aa224238f9f) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002403

```text
(config-router-af)# default bgp aigp-rib-metric <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 91 `；EOL ` RVA 0x35647280 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4a3c3ec86f257c8a](../../evidence/conditions-sets-029.md#c-4a3c3ec86f257c8a) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002278

```text
(config-router-af)# default bgp always-compare-med <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 5 `；EOL ` RVA 0x3563E0E8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8d3b3c9e2a55f0b9](../../evidence/conditions-sets-055.md#c-8d3b3c9e2a55f0b9) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002443

```text
(config-router-af)# default bgp asnotation dot <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 64 `；EOL ` RVA 0x3563E3F8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8d3b3c9e2a55f0b9](../../evidence/conditions-sets-055.md#c-8d3b3c9e2a55f0b9) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002577

```text
(config-router-af)# default bgp bestpath aigp ignore <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 43 `；EOL ` RVA 0x35645FA8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d76469a1f7a4873d](../../evidence/conditions-sets-083.md#c-d76469a1f7a4873d) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002569

```text
(config-router-af)# default bgp bestpath as-path ignore <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 17 `；EOL ` RVA 0x35645718 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4a3c3ec86f257c8a](../../evidence/conditions-sets-029.md#c-4a3c3ec86f257c8a) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002572

```text
(config-router-af)# default bgp bestpath as-path multipath-relax <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 51 `；EOL ` RVA 0x356459C0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4a3c3ec86f257c8a](../../evidence/conditions-sets-029.md#c-4a3c3ec86f257c8a) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002514

```text
(config-router-af)# default bgp bestpath compare-routerid <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 24 `；EOL ` RVA 0x35645C58 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4a3c3ec86f257c8a](../../evidence/conditions-sets-029.md#c-4a3c3ec86f257c8a) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002576

```text
(config-router-af)# default bgp bestpath cost-community ignore <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 41 `；EOL ` RVA 0x35646280 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4a3c3ec86f257c8a](../../evidence/conditions-sets-029.md#c-4a3c3ec86f257c8a) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002530

```text
(config-router-af)# default bgp bestpath igp-metric ignore <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 42 `；EOL ` RVA 0x3564A070 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5150ea47e3f03165](../../evidence/conditions-sets-032.md#c-5150ea47e3f03165) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002573

```text
(config-router-af)# default bgp bestpath med missing-as-worst <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 18 `；EOL ` RVA 0x35645408 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4a3c3ec86f257c8a](../../evidence/conditions-sets-029.md#c-4a3c3ec86f257c8a) · [状态效果 S-67464c28f0c5b407](../../evidence/state_effects-sets-022.md#s-67464c28f0c5b407)

### observed_connections-002536

```text
(config-router-af)# default bgp bestpath prefix-validate allow-invalid <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 78 `；EOL ` RVA 0x3564A380 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8904f4b1b978efe3](../../evidence/conditions-sets-053.md#c-8904f4b1b978efe3) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002541

```text
(config-router-af)# default bgp bestpath prefix-validate disable <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 77 `；EOL ` RVA 0x3564A628 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8904f4b1b978efe3](../../evidence/conditions-sets-053.md#c-8904f4b1b978efe3) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002466

```text
(config-router-af)# default bgp client-to-client reflection <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 9 `；EOL ` RVA 0x3563F288 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-607bcdd6d486da42](../../evidence/conditions-sets-038.md#c-607bcdd6d486da42) · [状态效果 S-c81e2c8cf2573810](../../evidence/state_effects-sets-042.md#s-c81e2c8cf2573810)

### observed_connections-002322

```text
(config-router-af)# default bgp cluster-id <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 7 `；EOL ` RVA 0x3563EE50 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6bb428152d11756d](../../evidence/conditions-sets-042.md#c-6bb428152d11756d) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002331

```text
(config-router-af)# default bgp consistency-checker <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 3 `；EOL ` RVA 0x3563E7D0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8ae99f1745a6061b](../../evidence/conditions-sets-054.md#c-8ae99f1745a6061b) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002283

```text
(config-router-af)# default bgp dampening <cr>
```

Handler ` RVA 0xF1B85B0 `；selector ` 0 `；EOL ` RVA 0x35648C08 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ce46379bd6d09927](../../evidence/conditions-sets-079.md#c-ce46379bd6d09927) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002532

```text
(config-router-af)# default bgp default inter-as-hybrid advertise-source-routes <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 57 `；EOL ` RVA 0x35648240 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c666987e1ff102fc](../../evidence/conditions-sets-076.md#c-c666987e1ff102fc) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002426

```text
(config-router-af)# default bgp default ipv4-unicast <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 19 `；EOL ` RVA 0x35647998 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-833065ca9d9b5b4a](../../evidence/conditions-sets-051.md#c-833065ca9d9b5b4a) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002434

```text
(config-router-af)# default bgp default ipv6-nexthop <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 75 `；EOL ` RVA 0x35647C90 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-01297021f866bd84](../../evidence/conditions-sets-001.md#c-01297021f866bd84) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002285

```text
(config-router-af)# default bgp default local-preference <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 0 `；EOL ` RVA 0x35647F20 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-bac9553258d6e58a](../../evidence/conditions-sets-072.md#c-bac9553258d6e58a) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002525

```text
(config-router-af)# default bgp default route-target filter <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 25 `；EOL ` RVA 0x356485A8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2127c24ec9e7cb8b](../../evidence/conditions-sets-013.md#c-2127c24ec9e7cb8b) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002526

```text
(config-router-af)# default bgp default route-target filter <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 25 `；EOL ` RVA 0x35648848 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-49c39aa546553d15](../../evidence/conditions-sets-029.md#c-49c39aa546553d15) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002346

```text
(config-router-af)# default bgp deterministic-med <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 10 `；EOL ` RVA 0x35640908 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8d3b3c9e2a55f0b9](../../evidence/conditions-sets-055.md#c-8d3b3c9e2a55f0b9) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002316

```text
(config-router-af)# default bgp dmzlink-bw <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 31 `；EOL ` RVA 0x3564BF40 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-795d3aa0c1de4631](../../evidence/conditions-sets-047.md#c-795d3aa0c1de4631) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002171

```text
(config-router-af)# default bgp dynamic-med-interval <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 21 `；EOL ` RVA 0x35640930 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-72fea9477916ed01](../../evidence/conditions-sets-044.md#c-72fea9477916ed01) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002325

```text
(config-router-af)# default bgp enforce-first-as <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 20 `；EOL ` RVA 0x3563FB38 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8d3b3c9e2a55f0b9](../../evidence/conditions-sets-055.md#c-8d3b3c9e2a55f0b9) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002376

```text
(config-router-af)# default bgp enhanced-error <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 82 `；EOL ` RVA 0x35642578 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9c6c65b28014d4ea](../../evidence/conditions-sets-060.md#c-9c6c65b28014d4ea) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002245

```text
(config-router-af)# default bgp fast-external-fallover <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 1 `；EOL ` RVA 0x3563D820 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8d3b3c9e2a55f0b9](../../evidence/conditions-sets-055.md#c-8d3b3c9e2a55f0b9) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002387

```text
(config-router-af)# default bgp graceful-restart <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 35 `；EOL ` RVA 0x356433E8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8d3b3c9e2a55f0b9](../../evidence/conditions-sets-055.md#c-8d3b3c9e2a55f0b9) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002380

```text
(config-router-af)# default bgp graceful-restart restart-time <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 36 `；EOL ` RVA 0x35642DB8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c4d273e835f8e73f](../../evidence/conditions-sets-076.md#c-c4d273e835f8e73f) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002382

```text
(config-router-af)# default bgp graceful-restart stalepath-time <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 37 `；EOL ` RVA 0x35642E20 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-cc349caed8a74471](../../evidence/conditions-sets-079.md#c-cc349caed8a74471) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002603

```text
(config-router-af)# default bgp graceful-shutdown all vrfs activate <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 79 `；EOL ` RVA 0x35643850 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0d112354600b2460](../../evidence/conditions-sets-005.md#c-0d112354600b2460) · [状态效果 S-5df6e3bb75d1014e](../../evidence/state_effects-sets-020.md#s-5df6e3bb75d1014e)

### observed_connections-002600

```text
(config-router-af)# default bgp inject-map <string> exist-map <string> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 32 `；EOL ` RVA 0x3564DAB8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` route-map name；` string ` route-map name。

[条件 C-e56cedc33997c1c6](../../evidence/conditions-sets-088.md#c-e56cedc33997c1c6) · [参数 P-82a88d349cb24e9e](../../evidence/parameters-sets-010.md#p-82a88d349cb24e9e) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002523

```text
(config-router-af)# default bgp label-allocation-batch <number:0..4294967295> <number:0..4294967295> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 53 `；EOL ` RVA 0x3563DBB0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Timer value in milliseconds；` unsigned_number ` Batch Size。

[条件 C-8d3b3c9e2a55f0b9](../../evidence/conditions-sets-055.md#c-8d3b3c9e2a55f0b9) · [参数 P-590ffc4a862cdd5b](../../evidence/parameters-sets-007.md#p-590ffc4a862cdd5b) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002551

```text
(config-router-af)# default bgp listen block <address> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 93 `；EOL ` RVA 0x3564B950 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IPv4 Dynamic Peering Address。

[条件 C-91f187ee957ea16a](../../evidence/conditions-sets-056.md#c-91f187ee957ea16a) · [参数 P-ff1855d12fccf3a2](../../evidence/parameters-sets-019.md#p-ff1855d12fccf3a2) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002565

```text
(config-router-af)# default bgp listen block <address> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 93 `；EOL ` RVA 0x356418B0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IPv4 Dynamic Peering Address。

[条件 C-861d4f86f990b125](../../evidence/conditions-sets-052.md#c-861d4f86f990b125) · [参数 P-8e142a50b5d2fd9e](../../evidence/parameters-sets-011.md#p-8e142a50b5d2fd9e) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002339

```text
(config-router-af)# default bgp listen limit <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 61 `；EOL ` RVA 0x3564B898 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a77cb16fa3be3af0](../../evidence/conditions-sets-065.md#c-a77cb16fa3be3af0) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002377

```text
(config-router-af)# default bgp listen limit <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 61 `；EOL ` RVA 0x356417D0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ed662d13ec07b594](../../evidence/conditions-sets-092.md#c-ed662d13ec07b594) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002497

```text
(config-router-af)# default bgp listen persistent <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 94 `；EOL ` RVA 0x35641BE8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-861d4f86f990b125](../../evidence/conditions-sets-052.md#c-861d4f86f990b125) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002336

```text
(config-router-af)# default bgp log-neighbor-changes <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 11 `；EOL ` RVA 0x3563FDE0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8d3b3c9e2a55f0b9](../../evidence/conditions-sets-055.md#c-8d3b3c9e2a55f0b9) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002408

```text
(config-router-af)# default bgp maxas-limit <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 26 `；EOL ` RVA 0x35646FF8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-fa1610783a36d411](../../evidence/conditions-sets-097.md#c-fa1610783a36d411) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002396

```text
(config-router-af)# default bgp maxcommunity-limit <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 27 `；EOL ` RVA 0x35646608 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3ed5e3c40c159de4](../../evidence/conditions-sets-024.md#c-3ed5e3c40c159de4) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002404

```text
(config-router-af)# default bgp maxextcommunity-limit <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 29 `；EOL ` RVA 0x35646CA8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2065e20a78f715e1](../../evidence/conditions-sets-013.md#c-2065e20a78f715e1) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002400

```text
(config-router-af)# default bgp maxlargecommunity-limit <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 28 `；EOL ` RVA 0x35646958 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-493790945e0ef947](../../evidence/conditions-sets-029.md#c-493790945e0ef947) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002367

```text
(config-router-af)# default bgp mpls-local-label <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 81 `；EOL ` RVA 0x3564DE30 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-92af687f7671312c](../../evidence/conditions-sets-057.md#c-92af687f7671312c) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002555

```text
(config-router-af)# default bgp nexthop route-map <string> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 56 `；EOL ` RVA 0x3564C6A8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` route-map name。

[条件 C-c23de0d6427bd68a](../../evidence/conditions-sets-075.md#c-c23de0d6427bd68a) · [参数 P-2fa3aa6823f1ec72](../../evidence/parameters-sets-004.md#p-2fa3aa6823f1ec72) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002488

```text
(config-router-af)# default bgp nexthop trigger critical-delay <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 48 `；EOL ` RVA 0x3564CC10 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e1ae81c6bb832a17](../../evidence/conditions-sets-087.md#c-e1ae81c6bb832a17) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002482

```text
(config-router-af)# default bgp nexthop trigger delay <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 47 `；EOL ` RVA 0x3564C990 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-89ddc69738a7fa09](../../evidence/conditions-sets-053.md#c-89ddc69738a7fa09) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002550

```text
(config-router-af)# default bgp nexthop trigger enable <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 49 `；EOL ` RVA 0x3564C968 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-03a7874e9a6887cf](../../evidence/conditions-sets-002.md#c-03a7874e9a6887cf) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002562

```text
(config-router-af)# default bgp nopeerup-delay cold-boot <number:1..3600> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 74 `；EOL ` RVA 0x35642210 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Delay in seconds。

[条件 C-23578c788649caa5](../../evidence/conditions-sets-014.md#c-23578c788649caa5) · [参数 P-5c73c5e1db17e48e](../../evidence/parameters-sets-007.md#p-5c73c5e1db17e48e) · [状态效果 S-bc36a01d505b3a40](../../evidence/state_effects-sets-040.md#s-bc36a01d505b3a40)

### observed_connections-002455

```text
(config-router-af)# default bgp recursion host <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 72 `；EOL ` RVA 0x3564AD08 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8f08c4361e706b21](../../evidence/conditions-sets-055.md#c-8f08c4361e706b21) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002296

```text
(config-router-af)# default bgp redistribute-internal <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 2 `；EOL ` RVA 0x3564F030 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5182e528ca172aef](../../evidence/conditions-sets-032.md#c-5182e528ca172aef) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002508

```text
(config-router-af)# default bgp refresh max-eor-time <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 16 `；EOL ` RVA 0x356445E0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-abe165c336c0e089](../../evidence/conditions-sets-066.md#c-abe165c336c0e089) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002504

```text
(config-router-af)# default bgp refresh stalepath-time <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 15 `；EOL ` RVA 0x35644270 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-57004814acdac152](../../evidence/conditions-sets-034.md#c-57004814acdac152) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002506

```text
(config-router-af)# default bgp regexp deterministic <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 44 `；EOL ` RVA 0x35644FF8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4a3c3ec86f257c8a](../../evidence/conditions-sets-029.md#c-4a3c3ec86f257c8a) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002456

```text
(config-router-af)# default bgp route-map priority <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 59 `；EOL ` RVA 0x356501C0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e552582f99054ab0](../../evidence/conditions-sets-088.md#c-e552582f99054ab0) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002267

```text
(config-router-af)# default bgp route-map-cache <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 34 `；EOL ` RVA 0x3563DE38 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8d3b3c9e2a55f0b9](../../evidence/conditions-sets-055.md#c-8d3b3c9e2a55f0b9) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002284

```text
(config-router-af)# default bgp router-id <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 4 `；EOL ` RVA 0x3563D1F0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7a12ffdc140b6038](../../evidence/conditions-sets-047.md#c-7a12ffdc140b6038) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002340

```text
(config-router-af)# default bgp router-id <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 4 `；EOL ` RVA 0x3564B3B8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-fb364036e11f69ff](../../evidence/conditions-sets-097.md#c-fb364036e11f69ff) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002613

```text
(config-router-af)# default bgp rpki server tcp <address> port <number:1..65535> refresh <number:1..65535> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 76 `；EOL ` RVA 0x35650FD8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IPv6 address of RPKI cache server；` unsigned_number ` Port number；` unsigned_number ` Refresh time in seconds。

[条件 C-403177562c0694ce](../../evidence/conditions-sets-025.md#c-403177562c0694ce) · [参数 P-8c5c351bae1730a5](../../evidence/parameters-sets-011.md#p-8c5c351bae1730a5) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002356

```text
(config-router-af)# default bgp rr-group <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 23 `；EOL ` RVA 0x3564D650 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-685645e4b29c4335](../../evidence/conditions-sets-040.md#c-685645e4b29c4335) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002409

```text
(config-router-af)# default bgp safe-ebgp-policy <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 92 `；EOL ` RVA 0x35647590 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ffea2d982084ee65](../../evidence/conditions-sets-099.md#c-ffea2d982084ee65) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002486

```text
(config-router-af)# default bgp scan-time <number:5..60> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 22 `；EOL ` RVA 0x3564D2E0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Scanner interval (seconds)。

[条件 C-8b3598aecea70031](../../evidence/conditions-sets-054.md#c-8b3598aecea70031) · [参数 P-d09d1b488454b2d8](../../evidence/parameters-sets-016.md#p-d09d1b488454b2d8) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002459

```text
(config-router-af)# default bgp slow-peer detection <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 67 `；EOL ` RVA 0x3564E300 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-cea01910f76c5f02](../../evidence/conditions-sets-080.md#c-cea01910f76c5f02) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002542

```text
(config-router-af)# default bgp slow-peer split-update-group dynamic <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 68 `；EOL ` RVA 0x3564E8D0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3becab12392242d4](../../evidence/conditions-sets-023.md#c-3becab12392242d4) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002557

```text
(config-router-af)# default bgp snmp traps add-type <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 90 `；EOL ` RVA 0x35640EF8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8d3b3c9e2a55f0b9](../../evidence/conditions-sets-055.md#c-8d3b3c9e2a55f0b9) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002337

```text
(config-router-af)# default bgp soft-reconfig-backup <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 52 `；EOL ` RVA 0x3564C290 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6b8a08d64cffcc48](../../evidence/conditions-sets-042.md#c-6b8a08d64cffcc48) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002594

```text
(config-router-af)# default bgp sourced-paths per-net isis all <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 89 `；EOL ` RVA 0x3564FE40 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ff436232114b2225](../../evidence/conditions-sets-098.md#c-ff436232114b2225) · [状态效果 S-f5317e67827a7de2](../../evidence/state_effects-sets-052.md#s-f5317e67827a7de2)

### observed_connections-002590

```text
(config-router-af)# default bgp sourced-paths per-net ospf all <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 87 `；EOL ` RVA 0x3564F7E0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ff436232114b2225](../../evidence/conditions-sets-098.md#c-ff436232114b2225) · [状态效果 S-e39ffdfadfbfd122](../../evidence/state_effects-sets-048.md#s-e39ffdfadfbfd122)

### observed_connections-002592

```text
(config-router-af)# default bgp sourced-paths per-net ospfv3 all <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 88 `；EOL ` RVA 0x3564FB28 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ff436232114b2225](../../evidence/conditions-sets-098.md#c-ff436232114b2225) · [状态效果 S-f490df6081d95d0a](../../evidence/state_effects-sets-052.md#s-f490df6081d95d0a)

### observed_connections-002588

```text
(config-router-af)# default bgp sourced-paths per-net static all <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 86 `；EOL ` RVA 0x3564F498 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ff436232114b2225](../../evidence/conditions-sets-098.md#c-ff436232114b2225) · [状态效果 S-5c0508a660e5ca30](../../evidence/state_effects-sets-020.md#s-5c0508a660e5ca30)

### observed_connections-002498

```text
(config-router-af)# default bgp sso route-refresh-enable <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 38 `；EOL ` RVA 0x35643EB0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4a3c3ec86f257c8a](../../evidence/conditions-sets-029.md#c-4a3c3ec86f257c8a) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002305

```text
(config-router-af)# default bgp suppress-inactive <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 45 `；EOL ` RVA 0x3564B008 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-488f3c121a9ac3ba](../../evidence/conditions-sets-028.md#c-488f3c121a9ac3ba) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002079

```text
(config-router-af)# default bgp tid <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 55 `；EOL ` RVA 0x3563CA30 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b48bc5c154b06025](../../evidence/conditions-sets-070.md#c-b48bc5c154b06025) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002465

```text
(config-router-af)# default bgp transport path-mtu-discovery <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 50 `；EOL ` RVA 0x3563F8A8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8d3b3c9e2a55f0b9](../../evidence/conditions-sets-055.md#c-8d3b3c9e2a55f0b9) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002192

```text
(config-router-af)# default bgp update-delay <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 30 `；EOL ` RVA 0x35642828 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-23705696ae5a3223](../../evidence/conditions-sets-014.md#c-23705696ae5a3223) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002534

```text
(config-router-af)# default bgp update-group split as-override <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 73 `；EOL ` RVA 0x3564ECA0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-779c8c2bed6dd3fc](../../evidence/conditions-sets-047.md#c-779c8c2bed6dd3fc) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002256

```text
(config-router-af)# default bgp upgrade-cli <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 33 `；EOL ` RVA 0x3563CE48 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-054935b640257f09](../../evidence/conditions-sets-002.md#c-054935b640257f09) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002328

```text
(config-router-af)# default bgp va <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 80 `；EOL ` RVA 0x35650568 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2c42a9e2b639038f](../../evidence/conditions-sets-017.md#c-2c42a9e2b639038f) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002502

```text
(config-router-af)# default bgp vrf-update-optimisation off <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 66 `；EOL ` RVA 0x35644968 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4a3c3ec86f257c8a](../../evidence/conditions-sets-029.md#c-4a3c3ec86f257c8a) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002390

```text
(config-router-af)# default bgp write-limit <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 40 `；EOL ` RVA 0x35644CC0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-75ed824815fcf3c3](../../evidence/conditions-sets-046.md#c-75ed824815fcf3c3) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002366

```text
(config-router-af)# default capability vrf-lite <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 7 `；EOL ` RVA 0x35636500 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-57adb160f929a25e](../../evidence/conditions-sets-034.md#c-57adb160f929a25e) · [状态效果 S-918d67bd4b2415c3](../../evidence/state_effects-sets-031.md#s-918d67bd4b2415c3)

### observed_connections-002250

```text
(config-router-af)# default compatible rfc1583 <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 25 `；EOL ` RVA 0x356544B8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-cc5aafa1a170d7f5](../../evidence/conditions-sets-079.md#c-cc5aafa1a170d7f5) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002262

```text
(config-router-af)# default compatible rfc1587 <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 26 `；EOL ` RVA 0x356547B0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0a4ff46fd3afc43d](../../evidence/conditions-sets-004.md#c-0a4ff46fd3afc43d) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002277

```text
(config-router-af)# default compatible rfc5243 <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 27 `；EOL ` RVA 0x35654A80 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7ac4b67371877306](../../evidence/conditions-sets-048.md#c-7ac4b67371877306) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002057

```text
(config-router-af)# default context <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 0 `；EOL ` RVA 0x33C44A60 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ada418e0516d363b](../../evidence/conditions-sets-067.md#c-ada418e0516d363b) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002237

```text
(config-router-af)# default default-information originate <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 6 `；EOL ` RVA 0x35639DE0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f938ce7057554709](../../evidence/conditions-sets-096.md#c-f938ce7057554709) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002320

```text
(config-router-af)# default default-information originate <cr>
```

Handler ` RVA 0xE1F1F70 `；selector ` 0 `；EOL ` RVA 0x3426ED60 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db74cc03fbb4a097](../../evidence/conditions-sets-084.md#c-db74cc03fbb4a097) · [状态效果 S-2d15cf91b1b1f6ba](../../evidence/state_effects-sets-010.md#s-2d15cf91b1b1f6ba)

### observed_connections-002370

```text
(config-router-af)# default default-information originate <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 6 `；EOL ` RVA 0x355DCEA8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-366c48c6f37882be](../../evidence/conditions-sets-021.md#c-366c48c6f37882be) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002105

```text
(config-router-af)# default default-metric <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 12 `；EOL ` RVA 0x3563A578 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-050a0ab411eeef66](../../evidence/conditions-sets-002.md#c-050a0ab411eeef66) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002151

```text
(config-router-af)# default default-metric <cr>
```

Handler ` RVA 0xE1F35A0 `；selector ` 0 `；EOL ` RVA 0x3426F628 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e31835e52b32a2b6](../../evidence/conditions-sets-087.md#c-e31835e52b32a2b6) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002188

```text
(config-router-af)# default default-metric <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 12 `；EOL ` RVA 0x355DD640 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-78327182356c9551](../../evidence/conditions-sets-047.md#c-78327182356c9551) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002341

```text
(config-router-af)# default discard-route external <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 11 `；EOL ` RVA 0x35634FD0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8d1015de0df3837e](../../evidence/conditions-sets-055.md#c-8d1015de0df3837e) · [状态效果 S-8847a27a3fb20cec](../../evidence/state_effects-sets-029.md#s-8847a27a3fb20cec)

### observed_connections-002072

```text
(config-router-af)# default distance <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 9 `；EOL ` RVA 0x35630608 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e9f55346791e7a61](../../evidence/conditions-sets-090.md#c-e9f55346791e7a61) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002170

```text
(config-router-af)# default distance <cr>
```

Handler ` RVA 0xE1E3290 `；selector ` 1 `；EOL ` RVA 0x34270758 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-93e02ac49bb69a67](../../evidence/conditions-sets-057.md#c-93e02ac49bb69a67) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002179

```text
(config-router-af)# default distance <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 9 `；EOL ` RVA 0x355DDF30 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e0bb4bd73a45a762](../../evidence/conditions-sets-087.md#c-e0bb4bd73a45a762) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002349

```text
(config-router-af)# default distance nhrp <cr>
```

Handler ` RVA 0x108B0C70 `；selector ` 1 `；EOL ` RVA 0x34BE80E0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-74a31d3eb0170b61](../../evidence/conditions-sets-045.md#c-74a31d3eb0170b61) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002258

```text
(config-router-af)# default distance ospf <cr>
```

Handler ` RVA 0x11BCBF10 `；selector ` 0 `；EOL ` RVA 0x35659D80 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a57234791bcfc72e](../../evidence/conditions-sets-064.md#c-a57234791bcfc72e) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002358

```text
(config-router-af)# default distance ospf <cr>
```

Handler ` RVA 0x11BCBF10 `；selector ` 0 `；EOL ` RVA 0x356594B8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-30ff1c10d8dbde6e](../../evidence/conditions-sets-019.md#c-30ff1c10d8dbde6e) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002361

```text
(config-router-af)# default distribute-list in <cr>
```

Handler ` RVA 0xE1EE180 `；selector ` 0 `；EOL ` RVA 0x3426FD18 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6d3dd57b54b1c820](../../evidence/conditions-sets-042.md#c-6d3dd57b54b1c820) · [状态效果 S-415a0d9cbb3c4264](../../evidence/state_effects-sets-014.md#s-415a0d9cbb3c4264)

### observed_connections-002553

```text
(config-router-af)# default distribute-list prefix-list <string> in <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 14 `；EOL ` RVA 0x355DA6F8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Prefix-list name。

[条件 C-a715b9c71b95a342](../../evidence/conditions-sets-064.md#c-a715b9c71b95a342) · [参数 P-adfe4ef17dd0436d](../../evidence/parameters-sets-013.md#p-adfe4ef17dd0436d) · [状态效果 S-c4effd752d68612b](../../evidence/state_effects-sets-042.md#s-c4effd752d68612b)

### observed_connections-002519

```text
(config-router-af)# default distribute-list route-map <string> in <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 14 `；EOL ` RVA 0x35639688 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Route-map name。

[条件 C-8a18c282ba969e4e](../../evidence/conditions-sets-053.md#c-8a18c282ba969e4e) · [参数 P-34975ce9a874ca41](../../evidence/parameters-sets-004.md#p-34975ce9a874ca41) · [状态效果 S-3c76189faae3bc19](../../evidence/state_effects-sets-013.md#s-3c76189faae3bc19)

### observed_connections-002115

```text
(config-router-af)# default domain-id <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 9 `；EOL ` RVA 0x35652DB8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2361a282694be0b9](../../evidence/conditions-sets-014.md#c-2361a282694be0b9) · [状态效果 S-639300b191c1366c](../../evidence/state_effects-sets-021.md#s-639300b191c1366c)

### observed_connections-002164

```text
(config-router-af)# default event-log <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 19 `；EOL ` RVA 0x356347B0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9a321beb23b08158](../../evidence/conditions-sets-060.md#c-9a321beb23b08158) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002036

```text
(config-router-af)# default flash-update-threshold <cr>
```

Handler ` RVA 0xE1F7ED0 `；selector ` 0 `；EOL ` RVA 0x3426E850 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6f8054bc55cf8cc0](../../evidence/conditions-sets-043.md#c-6f8054bc55cf8cc0) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002208

```text
(config-router-af)# default graceful-restart <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 22 `；EOL ` RVA 0x3569DA70 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2c70dea2cb2c798f](../../evidence/conditions-sets-017.md#c-2c70dea2cb2c798f) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002393

```text
(config-router-af)# default graceful-restart helper <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 23 `；EOL ` RVA 0x3569DDF8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-12975865b37b3794](../../evidence/conditions-sets-007.md#c-12975865b37b3794) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002453

```text
(config-router-af)# default ignore lsa mospf <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 4 `；EOL ` RVA 0x35633EC8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-67c55366e9607aca](../../evidence/conditions-sets-040.md#c-67c55366e9607aca) · [状态效果 S-134e39febf8ba94b](../../evidence/state_effects-sets-005.md#s-134e39febf8ba94b)

### observed_connections-002215

```text
(config-router-af)# default import bgp <cr>
```

Handler ` RVA 0x108B2FF0 `；selector ` 0 `；EOL ` RVA 0x34BE7790 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e06b676efe11b94e](../../evidence/conditions-sets-086.md#c-e06b676efe11b94e) · [状态效果 S-1de746f4f3c5c051](../../evidence/state_effects-sets-007.md#s-1de746f4f3c5c051)

### observed_connections-002033

```text
(config-router-af)# default input-queue <cr>
```

Handler ` RVA 0xE1F8060 `；selector ` 0 `；EOL ` RVA 0x3426E560 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-480be9c7b4e80e0a](../../evidence/conditions-sets-028.md#c-480be9c7b4e80e0a) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002276

```text
(config-router-af)# default interface-id snmp-if-index <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 15 `；EOL ` RVA 0x35654E18 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-67c55366e9607aca](../../evidence/conditions-sets-040.md#c-67c55366e9607aca) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002586

```text
(config-router-af)# default ipv6 route priority high tag <cr>
```

Handler ` RVA 0x11A9B140 `；selector ` 0 `；EOL ` RVA 0x355D83F8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-633546c9184006f7](../../evidence/conditions-sets-038.md#c-633546c9184006f7) · [状态效果 S-d176b37a32d76c2e](../../evidence/state_effects-sets-044.md#s-d176b37a32d76c2e)

### observed_connections-002378

```text
(config-router-af)# default limit retransmissions <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 14 `；EOL ` RVA 0x35636178 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f3d98f9bd00b4882](../../evidence/conditions-sets-094.md#c-f3d98f9bd00b4882) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002204

```text
(config-router-af)# default local-rib-criteria <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 6 `；EOL ` RVA 0x35637370 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4f35057ca9207cf3](../../evidence/conditions-sets-031.md#c-4f35057ca9207cf3) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002159

```text
(config-router-af)# default log-adjacency-changes <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 3 `；EOL ` RVA 0x35634C50 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-67c55366e9607aca](../../evidence/conditions-sets-040.md#c-67c55366e9607aca) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002173

```text
(config-router-af)# default max-lsa <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 1 `；EOL ` RVA 0x356357F8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-13b6a4961e37f1ad](../../evidence/conditions-sets-008.md#c-13b6a4961e37f1ad) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002095

```text
(config-router-af)# default max-metric <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 13 `；EOL ` RVA 0x35653388 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-72af978b4bf5b7c2](../../evidence/conditions-sets-044.md#c-72af978b4bf5b7c2) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002094

```text
(config-router-af)# default max-metric intra-area <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 8 `；EOL ` RVA 0x356532A8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e33251f679d1f25e](../../evidence/conditions-sets-087.md#c-e33251f679d1f25e) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002132

```text
(config-router-af)# default maximum-paths <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 8 `；EOL ` RVA 0x3563B130 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-372a5047c80eaed4](../../evidence/conditions-sets-021.md#c-372a5047c80eaed4) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002196

```text
(config-router-af)# default maximum-paths <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 8 `；EOL ` RVA 0x355DC998 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2ca9638361f739f2](../../evidence/conditions-sets-018.md#c-2ca9638361f739f2) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002270

```text
(config-router-af)# default maximum-paths per-prefix-distribution <cr>
```

Handler ` RVA 0x11BCC820 `；selector ` 0 `；EOL ` RVA 0x3565A2B8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2f42a0cb8b96205c](../../evidence/conditions-sets-018.md#c-2f42a0cb8b96205c) · [状态效果 S-6aacfa0b6e36fbef](../../evidence/state_effects-sets-023.md#s-6aacfa0b6e36fbef)

### observed_connections-002306

```text
(config-router-af)# default maximum-paths per-prefix-distribution <cr>
```

Handler ` RVA 0x11BCC820 `；selector ` 0 `；EOL ` RVA 0x356599F0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-78bb5629f4361cdc](../../evidence/conditions-sets-047.md#c-78bb5629f4361cdc) · [状态效果 S-40516c0981fe67d6](../../evidence/state_effects-sets-014.md#s-40516c0981fe67d6)

### observed_connections-002152

```text
(config-router-af)# default metric <cr>
```

Handler ` RVA 0x11A9E030 `；selector ` 0 `；EOL ` RVA 0x355D9B78 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5c43f340217e302b](../../evidence/conditions-sets-036.md#c-5c43f340217e302b) · [状态效果 S-04f9a942ed349389](../../evidence/state_effects-sets-002.md#s-04f9a942ed349389)

### observed_connections-002238

```text
(config-router-af)# default metric holddown <cr>
```

Handler ` RVA 0xE1F32D0 `；selector ` 1 `；EOL ` RVA 0x3426D3C8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ccc6cf9a6fedcd66](../../evidence/conditions-sets-079.md#c-ccc6cf9a6fedcd66) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002102

```text
(config-router-af)# default metric maximum-hops <cr>
```

Handler ` RVA 0xE1F32D0 `；selector ` 2 `；EOL ` RVA 0x3426D3F0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9ad7b35ee187dc59](../../evidence/conditions-sets-060.md#c-9ad7b35ee187dc59) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002282

```text
(config-router-af)# default metric weights <cr>
```

Handler ` RVA 0xE1F32D0 `；selector ` 0 `；EOL ` RVA 0x3426D9B0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-984e84cf7553dc4b](../../evidence/conditions-sets-059.md#c-984e84cf7553dc4b) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002605

```text
(config-router-af)# default mpls traffic-engineering autoroute-exclude prefix-list <string> <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 32 `；EOL ` RVA 0x35CD8788 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Name of a prefix-list。

[条件 C-20863a65a135cf8c](../../evidence/conditions-sets-013.md#c-20863a65a135cf8c) · [参数 P-bb9aae7e316bf097](../../evidence/parameters-sets-014.md#p-bb9aae7e316bf097) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002067

```text
(config-router-af)# default multi-topology <cr>
```

Handler ` RVA 0x11A9A2A0 `；selector ` 0 `；EOL ` RVA 0x355D74F8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a40c29f771cfb7a9](../../evidence/conditions-sets-063.md#c-a40c29f771cfb7a9) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002414

```text
(config-router-af)# default nhrp redirect interest <cr>
```

Handler ` RVA 0x108B1190 `；selector ` 19 `；EOL ` RVA 0x34BE7C48 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-34bc055dbb59a36d](../../evidence/conditions-sets-020.md#c-34bc055dbb59a36d) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002425

```text
(config-router-af)# default offset-list <number:0..99> in <cr>
```

Handler ` RVA 0xE1F1330 `；selector ` 0 `；EOL ` RVA 0x3426BED8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Access list of networks to apply offset (0 selects all networks)。

[条件 C-cca70eeca648cd6c](../../evidence/conditions-sets-079.md#c-cca70eeca648cd6c) · [参数 P-701ad9f9b6d2f431](../../evidence/parameters-sets-009.md#p-701ad9f9b6d2f431) · [状态效果 S-7f8d67fe346a4f4c](../../evidence/state_effects-sets-027.md#s-7f8d67fe346a4f4c)

### observed_connections-002144

```text
(config-router-af)# default omp-route-tag <cr>
```

Handler ` RVA 0xE1F7FD0 `；selector ` 0 `；EOL ` RVA 0x342712A8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-24312fafa4a6145a](../../evidence/conditions-sets-014.md#c-24312fafa4a6145a) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002022

```text
(config-router-af)# default output-delay <cr>
```

Handler ` RVA 0xE1F4590 `；selector ` 0 `；EOL ` RVA 0x3426B930 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7e81ff4b1bf9e6ec](../../evidence/conditions-sets-049.md#c-7e81ff4b1bf9e6ec) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002047

```text
(config-router-af)# default packet-size <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 41 `；EOL ` RVA 0x35636CC0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad034e533e076c35](../../evidence/conditions-sets-067.md#c-ad034e533e076c35) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002231

```text
(config-router-af)# default passive-interface default <cr>
```

Handler ` RVA 0xE1F3960 `；selector ` 0 `；EOL ` RVA 0x3426B520 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-84bb3022e130a597](../../evidence/conditions-sets-051.md#c-84bb3022e130a597) · [状态效果 S-839a5c9413a56ae3](../../evidence/state_effects-sets-028.md#s-839a5c9413a56ae3)

### observed_connections-002103

```text
(config-router-af)# default prc-interval <cr>
```

Handler ` RVA 0x11A9D490 `；selector ` 0 `；EOL ` RVA 0x355D8CB8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6839c52b1456cb1c](../../evidence/conditions-sets-040.md#c-6839c52b1456cb1c) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002122

```text
(config-router-af)# default prefix-suppression <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 28 `；EOL ` RVA 0x35653C68 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-bc2b2736fc868929](../../evidence/conditions-sets-073.md#c-bc2b2736fc868929) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002199

```text
(config-router-af)# default process-min-time percent <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 16 `；EOL ` RVA 0x35637A38 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c3955e88f8b9f7b5](../../evidence/conditions-sets-075.md#c-c3955e88f8b9f7b5) · [状态效果 S-ac7012f10df91736](../../evidence/state_effects-sets-036.md#s-ac7012f10df91736)

### observed_connections-002291

```text
(config-router-af)# default queue-depth hello <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 18 `；EOL ` RVA 0x35655210 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3977cd49a88b71a3](../../evidence/conditions-sets-022.md#c-3977cd49a88b71a3) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002300

```text
(config-router-af)# default queue-depth update <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 17 `；EOL ` RVA 0x35655598 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-dca66d33883829e8](../../evidence/conditions-sets-085.md#c-dca66d33883829e8) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002230

```text
(config-router-af)# default redistribute maximum-prefix <cr>
```

Handler ` RVA 0xE1E4550 `；selector ` 0 `；EOL ` RVA 0x34268518 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b74e7af2d6136249](../../evidence/conditions-sets-071.md#c-b74e7af2d6136249) · [状态效果 S-4d6eba641807e1d0](../../evidence/state_effects-sets-017.md#s-4d6eba641807e1d0)

### observed_connections-002269

```text
(config-router-af)# default redistribute maximum-prefix <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 5 `；EOL ` RVA 0x35638F60 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ae7eec5cfd5bc182](../../evidence/conditions-sets-067.md#c-ae7eec5cfd5bc182) · [状态效果 S-4b36741c4d943e4e](../../evidence/state_effects-sets-016.md#s-4b36741c4d943e4e)

### observed_connections-002074

```text
(config-router-af)# default router-id <cr>
```

Handler ` RVA 0x11A9F520 `；selector ` 0 `；EOL ` RVA 0x355D7868 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-24e1af47320d909f](../../evidence/conditions-sets-014.md#c-24e1af47320d909f) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002080

```text
(config-router-af)# default router-id <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 12 `；EOL ` RVA 0x356528F8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7d9de416b780da4f](../../evidence/conditions-sets-049.md#c-7d9de416b780da4f) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002121

```text
(config-router-af)# default set-attached-bit <cr>
```

Handler ` RVA 0x11A9D130 `；selector ` 0 `；EOL ` RVA 0x355D9720 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8e79975d630e485f](../../evidence/conditions-sets-055.md#c-8e79975d630e485f) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002123

```text
(config-router-af)# default set-overload-bit <cr>
```

Handler ` RVA 0x11A9D2E0 `；selector ` 0 `；EOL ` RVA 0x355D9140 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e4d2b02a9777c155](../../evidence/conditions-sets-088.md#c-e4d2b02a9777c155) · [状态效果 S-4cbd21d820987765](../../evidence/state_effects-sets-017.md#s-4cbd21d820987765)

### observed_connections-002203

```text
(config-router-af)# default shutdown <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 29 `；EOL ` RVA 0x35637730 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b1c8e1c934e6cb27](../../evidence/conditions-sets-069.md#c-b1c8e1c934e6cb27) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002228

```text
(config-router-af)# default snmp context <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 0 `；EOL ` RVA 0x33C455F0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7598dc8aeb3669dc](../../evidence/conditions-sets-046.md#c-7598dc8aeb3669dc) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002583

```text
(config-router-af)# default snmp context <string> community <string> <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 2 `；EOL ` RVA 0x33C45118 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Context Name；` string ` SNMP community string。

[条件 C-2573c969c66067b6](../../evidence/conditions-sets-015.md#c-2573c969c66067b6) · [参数 P-9b6eb89831feec60](../../evidence/parameters-sets-012.md#p-9b6eb89831feec60) · [状态效果 S-bb5faee37d44fc93](../../evidence/state_effects-sets-040.md#s-bb5faee37d44fc93)

### observed_connections-002582

```text
(config-router-af)# default snmp context <string> user <string> <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 23 `；EOL ` RVA 0x33C456D0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Context Name；` string ` Name of the user。

[条件 C-67e2e80e2c1c144d](../../evidence/conditions-sets-040.md#c-67e2e80e2c1c144d) · [参数 P-cfc42ec8ad667e32](../../evidence/parameters-sets-016.md#p-cfc42ec8ad667e32) · [状态效果 S-745d36dbb54971a9](../../evidence/state_effects-sets-025.md#s-745d36dbb54971a9)

### observed_connections-002124

```text
(config-router-af)# default spf-interval <cr>
```

Handler ` RVA 0x11A9D640 `；selector ` 0 `；EOL ` RVA 0x355D8820 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-58181a35319b1af1](../../evidence/conditions-sets-035.md#c-58181a35319b1af1) · [状态效果 S-65b25e7315c3a940](../../evidence/state_effects-sets-022.md#s-65b25e7315c3a940)

### observed_connections-002365

```text
(config-router-af)# default statistics rib-timings <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 5 `；EOL ` RVA 0x35636D00 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4f35057ca9207cf3](../../evidence/conditions-sets-031.md#c-4f35057ca9207cf3) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002416

```text
(config-router-af)# default summary-prefix <address> <address> <cr>
```

Handler ` RVA 0xE1DF4C0 `；selector ` 0 `；EOL ` RVA 0x34267798 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IP summary address；` address ` Summary mask。

[条件 C-f2a4b45f057f85a6](../../evidence/conditions-sets-094.md#c-f2a4b45f057f85a6) · [参数 P-d8789ea12de23037](../../evidence/parameters-sets-016.md#p-d8789ea12de23037) · [状态效果 S-6e9e97c0fb4747f3](../../evidence/state_effects-sets-024.md#s-6e9e97c0fb4747f3)

### observed_connections-002226

```text
(config-router-af)# default summary-prefix <address> <cr>
```

Handler ` RVA 0xE1DF4C0 `；selector ` 21 `；EOL ` RVA 0x34267D78 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IP summary address。

[条件 C-9322f540df8968af](../../evidence/conditions-sets-057.md#c-9322f540df8968af) · [参数 P-53019655abc62157](../../evidence/parameters-sets-007.md#p-53019655abc62157) · [状态效果 S-6e9e97c0fb4747f3](../../evidence/state_effects-sets-024.md#s-6e9e97c0fb4747f3)

### observed_connections-002088

```text
(config-router-af)# default table-map <cr>
```

Handler ` RVA 0xE1F4690 `；selector ` 0 `；EOL ` RVA 0x3563C698 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a2debac14b6fe94f](../../evidence/conditions-sets-063.md#c-a2debac14b6fe94f) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002104

```text
(config-router-af)# default table-map <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 17 `；EOL ` RVA 0x3563AB08 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-637e625f8f6a46c9](../../evidence/conditions-sets-039.md#c-637e625f8f6a46c9) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002187

```text
(config-router-af)# default table-map <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 17 `；EOL ` RVA 0x355DDBD0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6a319846906a93ba](../../evidence/conditions-sets-041.md#c-6a319846906a93ba) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002219

```text
(config-router-af)# default timers basic <cr>
```

Handler ` RVA 0xE1F2D60 `；selector ` 0 `；EOL ` RVA 0x34266D98 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c826ec3d359b7a5a](../../evidence/conditions-sets-077.md#c-c826ec3d359b7a5a) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002224

```text
(config-router-af)# default timers lsa arrival <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 39 `；EOL ` RVA 0x3565ADC0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e7d2f045f74d1960](../../evidence/conditions-sets-090.md#c-e7d2f045f74d1960) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002089

```text
(config-router-af)# default timers lsa-arrival <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 34 `；EOL ` RVA 0x3565B378 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-63ef0bf002bf640e](../../evidence/conditions-sets-039.md#c-63ef0bf002bf640e) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002076

```text
(config-router-af)# default timers lsa-group-pacing <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 35 `；EOL ` RVA 0x3565ADE8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c2f6f639ed527ac4](../../evidence/conditions-sets-075.md#c-c2f6f639ed527ac4) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002090

```text
(config-router-af)# default timers lsa-interval <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 33 `；EOL ` RVA 0x3565B350 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a7f39ac4c44c904d](../../evidence/conditions-sets-065.md#c-a7f39ac4c44c904d) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002247

```text
(config-router-af)# default timers pacing flood <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 36 `；EOL ` RVA 0x3565B948 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c69e66ab3b52c9e9](../../evidence/conditions-sets-077.md#c-c69e66ab3b52c9e9) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002240

```text
(config-router-af)# default timers pacing lsa-group <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 35 `；EOL ` RVA 0x3565B8E0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-955d8380395fc37d](../../evidence/conditions-sets-058.md#c-955d8380395fc37d) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002259

```text
(config-router-af)# default timers pacing retransmission <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 37 `；EOL ` RVA 0x3565BBE8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-699b0070eaf5149c](../../evidence/conditions-sets-041.md#c-699b0070eaf5149c) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002421

```text
(config-router-af)# default timers throttle lsa <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 40 `；EOL ` RVA 0x3565AA90 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-103e41e80329d978](../../evidence/conditions-sets-006.md#c-103e41e80329d978) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002418

```text
(config-router-af)# default timers throttle spf <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 38 `；EOL ` RVA 0x3565A6D8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-951e2fd89988a4eb](../../evidence/conditions-sets-058.md#c-951e2fd89988a4eb) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002213

```text
(config-router-af)# default topology base <cr>
```

Handler ` RVA 0xE1FE420 `；selector ` 0 `；EOL ` RVA 0x34276FB0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-aaa6798a83870932](../../evidence/conditions-sets-066.md#c-aaa6798a83870932) · [状态效果 S-7cee1aa2a61885e8](../../evidence/state_effects-sets-026.md#s-7cee1aa2a61885e8)

### observed_connections-002411

```text
(config-router-af)# default traffic-share min across-interfaces <cr>
```

Handler ` RVA 0xE1FA2E0 `；selector ` 0 `；EOL ` RVA 0x342668D8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c42a533f81769524](../../evidence/conditions-sets-076.md#c-c42a533f81769524) · [状态效果 S-ae48b7a9d6388be5](../../evidence/state_effects-sets-037.md#s-ae48b7a9d6388be5)

### observed_connections-002290

```text
(config-router-af)# default ucmp local <cr>
```

Handler ` RVA 0x11A9D7F0 `；selector ` 0 `；EOL ` RVA 0x355DA020 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d1a07b26ec659149](../../evidence/conditions-sets-081.md#c-d1a07b26ec659149) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002059

```text
(config-router-af)# default validate-update-source <cr>
```

Handler ` RVA 0xE1FA930 `；selector ` 0 `；EOL ` RVA 0x34267288 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3d6ebdf7688aabe1](../../evidence/conditions-sets-024.md#c-3d6ebdf7688aabe1) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002061

```text
(config-router-af)# default version <cr>
```

Handler ` RVA 0xFB4F020 `；selector ` 0 `；EOL ` RVA 0x348210B0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5de66c159e833b6e](../../evidence/conditions-sets-037.md#c-5de66c159e833b6e) · [状态效果 S-5b3ee3c63d93a564](../../evidence/state_effects-sets-020.md#s-5b3ee3c63d93a564)

### observed_connections-002087

```text
(config-router-af)# default-information originate <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 6 `；EOL ` RVA 0x35639DE0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f938ce7057554709](../../evidence/conditions-sets-096.md#c-f938ce7057554709)

### observed_connections-002150

```text
(config-router-af)# default-information originate <cr>
```

Handler ` RVA 0xE1F1F70 `；selector ` 0 `；EOL ` RVA 0x3426ED60 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-db74cc03fbb4a097](../../evidence/conditions-sets-084.md#c-db74cc03fbb4a097) · [状态效果 S-35e17ffb1ff01ddd](../../evidence/state_effects-sets-012.md#s-35e17ffb1ff01ddd)

### observed_connections-002180

```text
(config-router-af)# default-information originate <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 6 `；EOL ` RVA 0x355DCEA8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-366c48c6f37882be](../../evidence/conditions-sets-021.md#c-366c48c6f37882be)

### observed_connections-002118

```text
(config-router-af)# default-metric <number:1..16777214> <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 12 `；EOL ` RVA 0x3563A578 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Default metric。

[条件 C-821ecc844e885d5e](../../evidence/conditions-sets-050.md#c-821ecc844e885d5e) · [参数 P-005d629e7faf2d53](../../evidence/parameters-sets-001.md#p-005d629e7faf2d53)

### observed_connections-002153

```text
(config-router-af)# default-metric <number:1..16777214> <cr>
```

Handler ` RVA 0xE1F35A0 `；selector ` 0 `；EOL ` RVA 0x3426F628 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` OSPF default metric。

[条件 C-b568f0ac34dcae42](../../evidence/conditions-sets-070.md#c-b568f0ac34dcae42) · [参数 P-f87c9f88670f1c3c](../../evidence/parameters-sets-019.md#p-f87c9f88670f1c3c)

### observed_connections-002197

```text
(config-router-af)# default-metric <number:1..16777214> <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 12 `；EOL ` RVA 0x355DD640 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Default metric。

[条件 C-26bb8be187278337](../../evidence/conditions-sets-015.md#c-26bb8be187278337) · [参数 P-c3338eb7006f1569](../../evidence/parameters-sets-015.md#p-c3338eb7006f1569)

### observed_connections-002161

```text
(config-router-af)# discard-route external <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 11 `；EOL ` RVA 0x35634FD0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8d1015de0df3837e](../../evidence/conditions-sets-055.md#c-8d1015de0df3837e) · [状态效果 S-41c393276a0a4f76](../../evidence/state_effects-sets-014.md#s-41c393276a0a4f76)

### observed_connections-002025

```text
(config-router-af)# distance <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 9 `；EOL ` RVA 0x35630608 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e9f55346791e7a61](../../evidence/conditions-sets-090.md#c-e9f55346791e7a61)

### observed_connections-002046

```text
(config-router-af)# distance <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 9 `；EOL ` RVA 0x355DDF30 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e0bb4bd73a45a762](../../evidence/conditions-sets-087.md#c-e0bb4bd73a45a762)

### observed_connections-002630

```text
(config-router-af)# distance <number:1..254> <prefix:dynamic> <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 9 `；EOL ` RVA 0x35630608 `。

模式根 ` RVA 0x34265950 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Administrative distance；` prefix_dynamic ` Prefix to match source address。

[条件 C-1b0fd9716d478105](../../evidence/conditions-sets-011.md#c-1b0fd9716d478105) · [缺口 G-7126636ba3acce05](../../evidence/gaps-sets-004.md#g-7126636ba3acce05) · [参数 P-cf62c68b4330a61a](../../evidence/parameters-sets-016.md#p-cf62c68b4330a61a) · [状态效果 S-5500e6b2875d57e3](../../evidence/state_effects-sets-018.md#s-5500e6b2875d57e3)

### observed_connections-002636

```text
(config-router-af)# distance <number:1..254> <prefix:dynamic> <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 9 `；EOL ` RVA 0x355DDF30 `。

模式根 ` RVA 0x34265950 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Administrative distance；` prefix_dynamic ` Prefix to match source address。

[条件 C-fe2ca7fc49efa7d4](../../evidence/conditions-sets-098.md#c-fe2ca7fc49efa7d4) · [缺口 G-edbe4dbb4a83774a](../../evidence/gaps-sets-008.md#g-edbe4dbb4a83774a) · [参数 P-609ddb0d38d760a2](../../evidence/parameters-sets-008.md#p-609ddb0d38d760a2) · [状态效果 S-14f9d5f558e0919f](../../evidence/state_effects-sets-005.md#s-14f9d5f558e0919f)

### observed_connections-002162

```text
(config-router-af)# distance <number:1..255> <cr>
```

Handler ` RVA 0xE1E3290 `；selector ` 1 `；EOL ` RVA 0x34270758 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Administrative distance。

[条件 C-84f97c0c1ffe0451](../../evidence/conditions-sets-051.md#c-84f97c0c1ffe0451) · [参数 P-0c2ddd6e8bfb9ef3](../../evidence/parameters-sets-001.md#p-0c2ddd6e8bfb9ef3)

### observed_connections-002178

```text
(config-router-af)# distance nhrp <cr>
```

Handler ` RVA 0x108B0C70 `；selector ` 1 `；EOL ` RVA 0x34BE80E0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cbe66e9d6f07d533](../../evidence/conditions-sets-078.md#c-cbe66e9d6f07d533)

### observed_connections-002139

```text
(config-router-af)# distance ospf <cr>
```

Handler ` RVA 0x11BCBF10 `；selector ` 0 `；EOL ` RVA 0x35659D80 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1018bbdbd4491c07](../../evidence/conditions-sets-006.md#c-1018bbdbd4491c07)

### observed_connections-002181

```text
(config-router-af)# distance ospf <cr>
```

Handler ` RVA 0x11BCBF10 `；selector ` 0 `；EOL ` RVA 0x356594B8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9a9325e04a69ff81](../../evidence/conditions-sets-060.md#c-9a9325e04a69ff81)

### observed_connections-002172

```text
(config-router-af)# distribute-list in <cr>
```

Handler ` RVA 0xE1EE180 `；selector ` 0 `；EOL ` RVA 0x3426FD18 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6d3dd57b54b1c820](../../evidence/conditions-sets-042.md#c-6d3dd57b54b1c820) · [状态效果 S-3046a16312158b74](../../evidence/state_effects-sets-011.md#s-3046a16312158b74)

### observed_connections-002634

```text
(config-router-af)# distribute-list out <?router_action_proc_vpn@5555897c3ca0> <cr>
```

Handler ` RVA 0xE1EE180 `；selector ` 0 `；EOL ` RVA 0x3426FD18 `。

模式根 ` RVA 0x34265950 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6d3bc019e3512781](../../evidence/conditions-sets-042.md#c-6d3bc019e3512781) · [缺口 G-a1eff63f2f499c8d](../../evidence/gaps-sets-006.md#g-a1eff63f2f499c8d) · [状态效果 S-cc6a2927543a656b](../../evidence/state_effects-sets-043.md#s-cc6a2927543a656b)

### observed_connections-002477

```text
(config-router-af)# distribute-list prefix-list <string> in <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 14 `；EOL ` RVA 0x355DA6F8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Prefix-list name。

[条件 C-a715b9c71b95a342](../../evidence/conditions-sets-064.md#c-a715b9c71b95a342) · [参数 P-adfe4ef17dd0436d](../../evidence/parameters-sets-013.md#p-adfe4ef17dd0436d) · [状态效果 S-974f492931d33bb6](../../evidence/state_effects-sets-032.md#s-974f492931d33bb6)

### observed_connections-002648

```text
(config-router-af)# distribute-list prefix-list <string> in <interface> <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 14 `；EOL ` RVA 0x355DA6F8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Prefix-list name。

[条件 C-c62f99ec75e952ac](../../evidence/conditions-sets-076.md#c-c62f99ec75e952ac) · [缺口 G-2f2022053f41571f](../../evidence/gaps-sets-002.md#g-2f2022053f41571f) · [参数 P-9404691879ebd8fc](../../evidence/parameters-sets-011.md#p-9404691879ebd8fc) · [状态效果 S-5d6e2fea11282687](../../evidence/state_effects-sets-020.md#s-5d6e2fea11282687)

### observed_connections-002420

```text
(config-router-af)# distribute-list route-map <string> in <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 14 `；EOL ` RVA 0x35639688 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Route-map name。

[条件 C-8a18c282ba969e4e](../../evidence/conditions-sets-053.md#c-8a18c282ba969e4e) · [参数 P-34975ce9a874ca41](../../evidence/parameters-sets-004.md#p-34975ce9a874ca41) · [状态效果 S-77c5b741b44ccdf9](../../evidence/state_effects-sets-025.md#s-77c5b741b44ccdf9)

### observed_connections-002647

```text
(config-router-af)# distribute-list route-map <string> in <interface> <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 14 `；EOL ` RVA 0x35639688 `。

模式根 ` RVA 0x34265950 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Route-map name。

[条件 C-becf37e7a47d1383](../../evidence/conditions-sets-074.md#c-becf37e7a47d1383) · [缺口 G-536b12fd02e7e67e](../../evidence/gaps-sets-003.md#g-536b12fd02e7e67e) · [参数 P-56c8b232cdbed7e2](../../evidence/parameters-sets-007.md#p-56c8b232cdbed7e2) · [状态效果 S-ed6d820e206c3aeb](../../evidence/state_effects-sets-050.md#s-ed6d820e206c3aeb)

### observed_connections-002646

```text
(config-router-af)# domain-id type 0005 value <hex-string> <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 9 `；EOL ` RVA 0x35652DB8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` hexstring ` Six octet Domain ID extended community value in hexadecimal。

[条件 C-006b56755f3ee49e](../../evidence/conditions-sets-001.md#c-006b56755f3ee49e) · [缺口 G-2fa374da1fea7ea3](../../evidence/gaps-sets-002.md#g-2fa374da1fea7ea3) · [参数 P-db2ce8fc2ccd36a8](../../evidence/parameters-sets-016.md#p-db2ce8fc2ccd36a8) · [状态效果 S-16b3c84ff5a991d2](../../evidence/state_effects-sets-005.md#s-16b3c84ff5a991d2)

### observed_connections-002042

```text
(config-router-af)# event-log <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 19 `；EOL ` RVA 0x356347B0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9a321beb23b08158](../../evidence/conditions-sets-060.md#c-9a321beb23b08158)

### observed_connections-002019

```text
(config-router-af)# exit-address-family <cr>
```

Handler ` RVA 0xE1A0ED0 `；selector ` 0 `；EOL ` RVA 0x34265FA0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6b6fdb27a185ebe3](../../evidence/conditions-sets-042.md#c-6b6fdb27a185ebe3)

### observed_connections-002017

```text
(config-router-af)# flash-update-threshold <number:0..30> <cr>
```

Handler ` RVA 0xE1F7ED0 `；selector ` 0 `；EOL ` RVA 0x3426E850 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` threshold in seconds。

[条件 C-0fa3fd7ed226436a](../../evidence/conditions-sets-006.md#c-0fa3fd7ed226436a) · [参数 P-7db259c085793fff](../../evidence/parameters-sets-010.md#p-7db259c085793fff)

### observed_connections-002053

```text
(config-router-af)# graceful-restart <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 22 `；EOL ` RVA 0x3569DA70 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2c70dea2cb2c798f](../../evidence/conditions-sets-017.md#c-2c70dea2cb2c798f)

### observed_connections-002207

```text
(config-router-af)# graceful-restart helper <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 23 `；EOL ` RVA 0x3569DDF8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-12975865b37b3794](../../evidence/conditions-sets-007.md#c-12975865b37b3794)

### observed_connections-002302

```text
(config-router-af)# ignore lsa mospf <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 4 `；EOL ` RVA 0x35633EC8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-67c55366e9607aca](../../evidence/conditions-sets-040.md#c-67c55366e9607aca) · [状态效果 S-3efee8a9e2a2f847](../../evidence/state_effects-sets-014.md#s-3efee8a9e2a2f847)

### observed_connections-002216

```text
(config-router-af)# import bgp <number:1..4294967295> <cr>
```

Handler ` RVA 0x108B2FF0 `；selector ` 0 `；EOL ` RVA 0x34BE7790 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Autonomous system number。

[条件 C-f810c0997581d29e](../../evidence/conditions-sets-096.md#c-f810c0997581d29e) · [参数 P-08fa0189d9fa98c6](../../evidence/parameters-sets-001.md#p-08fa0189d9fa98c6) · [状态效果 S-8dc3856a28817def](../../evidence/state_effects-sets-030.md#s-8dc3856a28817def)

### observed_connections-002016

```text
(config-router-af)# input-queue <number:0..1024> <cr>
```

Handler ` RVA 0xE1F8060 `；selector ` 0 `；EOL ` RVA 0x3426E560 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` queue depth。

[条件 C-d28f952809c19ab7](../../evidence/conditions-sets-081.md#c-d28f952809c19ab7) · [参数 P-ac9eabe976c82c5a](../../evidence/parameters-sets-013.md#p-ac9eabe976c82c5a)

### observed_connections-002126

```text
(config-router-af)# interface-id snmp-if-index <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 15 `；EOL ` RVA 0x35654E18 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-67c55366e9607aca](../../evidence/conditions-sets-040.md#c-67c55366e9607aca)

### observed_connections-002585

```text
(config-router-af)# ipv6 route priority high tag <number:1..4294967295> <cr>
```

Handler ` RVA 0x11A9B140 `；selector ` 0 `；EOL ` RVA 0x355D83F8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` tag value。

[条件 C-48645ab68b3aa8d4](../../evidence/conditions-sets-028.md#c-48645ab68b3aa8d4) · [参数 P-d8b14ae3acaeed97](../../evidence/parameters-sets-016.md#p-d8b14ae3acaeed97) · [状态效果 S-508c0ce1b6cace53](../../evidence/state_effects-sets-018.md#s-508c0ce1b6cace53)

### observed_connections-002189

```text
(config-router-af)# limit retransmissions <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 14 `；EOL ` RVA 0x35636178 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f3d98f9bd00b4882](../../evidence/conditions-sets-094.md#c-f3d98f9bd00b4882)

### observed_connections-002052

```text
(config-router-af)# local-rib-criteria <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 6 `；EOL ` RVA 0x35637370 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4f35057ca9207cf3](../../evidence/conditions-sets-031.md#c-4f35057ca9207cf3)

### observed_connections-002041

```text
(config-router-af)# log-adjacency-changes <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 3 `；EOL ` RVA 0x35634C50 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-67c55366e9607aca](../../evidence/conditions-sets-040.md#c-67c55366e9607aca)

### observed_connections-002190

```text
(config-router-af)# max-lsa <number:1..4294967294> <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 1 `；EOL ` RVA 0x356357F8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Maximum number of non self-generated LSAs to accept。

[条件 C-d4089114a30f2f56](../../evidence/conditions-sets-082.md#c-d4089114a30f2f56) · [参数 P-35981549e895b10c](../../evidence/parameters-sets-005.md#p-35981549e895b10c)

### observed_connections-002030

```text
(config-router-af)# max-metric intra-area <number:1..16777214> <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 8 `；EOL ` RVA 0x356532A8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Metric value。

[条件 C-d7abf9194562cd57](../../evidence/conditions-sets-083.md#c-d7abf9194562cd57) · [参数 P-6381faba51d956ee](../../evidence/parameters-sets-008.md#p-6381faba51d956ee)

### observed_connections-002133

```text
(config-router-af)# max-metric router-lsa <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 13 `；EOL ` RVA 0x35653388 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1a4213fdb9bc29fc](../../evidence/conditions-sets-010.md#c-1a4213fdb9bc29fc)

### observed_connections-002037

```text
(config-router-af)# maximum-paths <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 8 `；EOL ` RVA 0x3563B130 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-372a5047c80eaed4](../../evidence/conditions-sets-021.md#c-372a5047c80eaed4)

### observed_connections-002049

```text
(config-router-af)# maximum-paths <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 8 `；EOL ` RVA 0x355DC998 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2ca9638361f739f2](../../evidence/conditions-sets-018.md#c-2ca9638361f739f2)

### observed_connections-002623

```text
(config-router-af)# maximum-paths <number:dynamic> <cr>
```

Handler ` RVA 0xE1E26B0 `；selector ` 0 `；EOL ` RVA 0x3426E078 `。

模式根 ` RVA 0x34265950 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Number of paths。

[条件 C-6495de06ed86c14a](../../evidence/conditions-sets-039.md#c-6495de06ed86c14a) · [缺口 G-5dbf855da4cc9685](../../evidence/gaps-sets-004.md#g-5dbf855da4cc9685) · [参数 P-6facf001e0067ec2](../../evidence/parameters-sets-009.md#p-6facf001e0067ec2)

### observed_connections-002120

```text
(config-router-af)# maximum-paths per-prefix-distribution <cr>
```

Handler ` RVA 0x11BCC820 `；selector ` 0 `；EOL ` RVA 0x3565A2B8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2f42a0cb8b96205c](../../evidence/conditions-sets-018.md#c-2f42a0cb8b96205c) · [状态效果 S-d350c2ae929bdde3](../../evidence/state_effects-sets-045.md#s-d350c2ae929bdde3)

### observed_connections-002142

```text
(config-router-af)# maximum-paths per-prefix-distribution <cr>
```

Handler ` RVA 0x11BCC820 `；selector ` 0 `；EOL ` RVA 0x356599F0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-78bb5629f4361cdc](../../evidence/conditions-sets-047.md#c-78bb5629f4361cdc) · [状态效果 S-7cf5b90427a1ebd3](../../evidence/state_effects-sets-026.md#s-7cf5b90427a1ebd3)

### observed_connections-002143

```text
(config-router-af)# metric <number:1..16777214> <cr>
```

Handler ` RVA 0x11A9E030 `；selector ` 0 `；EOL ` RVA 0x355D9B78 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Default metric。

[条件 C-091709af6ca45c52](../../evidence/conditions-sets-004.md#c-091709af6ca45c52) · [参数 P-b958f845e614b0cf](../../evidence/parameters-sets-014.md#p-b958f845e614b0cf) · [状态效果 S-ad65d0a55e84736d](../../evidence/state_effects-sets-037.md#s-ad65d0a55e84736d)

### observed_connections-002091

```text
(config-router-af)# metric holddown <cr>
```

Handler ` RVA 0xE1F32D0 `；selector ` 1 `；EOL ` RVA 0x3426D3C8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ccc6cf9a6fedcd66](../../evidence/conditions-sets-079.md#c-ccc6cf9a6fedcd66)

### observed_connections-002031

```text
(config-router-af)# metric maximum-hops <number:1..255> <cr>
```

Handler ` RVA 0xE1F32D0 `；selector ` 2 `；EOL ` RVA 0x3426D3F0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Hop count。

[条件 C-449b83756609309c](../../evidence/conditions-sets-027.md#c-449b83756609309c) · [参数 P-154636f1eeb7da11](../../evidence/parameters-sets-002.md#p-154636f1eeb7da11)

### observed_connections-002610

```text
(config-router-af)# metric weights <number:0..8> <number:0..255> <number:0..255> <number:0..255> <number:0..255> <number:0..255> <cr>
```

Handler ` RVA 0xE1F32D0 `；selector ` 0 `；EOL ` RVA 0x3426D9B0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Type Of Service (Only TOS 0 supported)；` unsigned_number ` K1；` unsigned_number ` K2；` unsigned_number ` K3；` unsigned_number ` K4；` unsigned_number ` K5。

[条件 C-fc1de76ac793dec5](../../evidence/conditions-sets-097.md#c-fc1de76ac793dec5) · [参数 P-84199f41c0c5a5ae](../../evidence/parameters-sets-010.md#p-84199f41c0c5a5ae)

### observed_connections-002567

```text
(config-router-af)# mpls traffic-engineering autoroute-exclude prefix-list <string> <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 32 `；EOL ` RVA 0x35CD8788 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of a prefix-list。

[条件 C-20863a65a135cf8c](../../evidence/conditions-sets-013.md#c-20863a65a135cf8c) · [参数 P-bb9aae7e316bf097](../../evidence/parameters-sets-014.md#p-bb9aae7e316bf097)

### observed_connections-002023

```text
(config-router-af)# multi-topology <cr>
```

Handler ` RVA 0x11A9A2A0 `；selector ` 0 `；EOL ` RVA 0x355D74F8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a40c29f771cfb7a9](../../evidence/conditions-sets-063.md#c-a40c29f771cfb7a9)

### observed_connections-002614

```text
(config-router-af)# neighbor <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 0 `；EOL ` RVA 0x342662B0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-64980f9de8f79016](../../evidence/conditions-sets-039.md#c-64980f9de8f79016) · [缺口 G-38f41042f674eac1](../../evidence/gaps-sets-002.md#g-38f41042f674eac1) · [状态效果 S-778a371eba615d3b](../../evidence/state_effects-sets-025.md#s-778a371eba615d3b)

### observed_connections-002658

```text
(config-router-af)# neighbor nhs <interface> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 0 `；EOL ` RVA 0x34BE7338 `。

模式根 ` RVA 0x34265950 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f07fde0e110aaa0d](../../evidence/conditions-sets-093.md#c-f07fde0e110aaa0d) · [缺口 G-905a8913b8165543](../../evidence/gaps-sets-005.md#g-905a8913b8165543) · [参数 P-35bc863c0770d7ea](../../evidence/parameters-sets-005.md#p-35bc863c0770d7ea) · [状态效果 S-8a5e2bd2542f721f](../../evidence/state_effects-sets-029.md#s-8a5e2bd2542f721f)

### observed_connections-002622

```text
(config-router-af)# network <address> <cr>
```

Handler ` RVA 0xF190B70 `；selector ` 0 `；EOL ` RVA 0x35651940 `。

模式根 ` RVA 0x34265950 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` NSAP prefix。

[条件 C-b9dc5dd026d47baf](../../evidence/conditions-sets-072.md#c-b9dc5dd026d47baf) · [缺口 G-10cf14566525c887](../../evidence/gaps-sets-001.md#g-10cf14566525c887) · [参数 P-4417b380cea130f7](../../evidence/parameters-sets-006.md#p-4417b380cea130f7) · [状态效果 S-03d65d2257b07f3c](../../evidence/state_effects-sets-001.md#s-03d65d2257b07f3c)

### observed_connections-002656

```text
(config-router-af)# network <address> <cr>
```

Handler ` RVA 0xE1E04C0 `；selector ` 0 `；EOL ` RVA 0x3426C4E0 `。

模式根 ` RVA 0x34265950 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Network number。

[条件 C-a4e51cb3326c79f2](../../evidence/conditions-sets-064.md#c-a4e51cb3326c79f2) · [缺口 G-ecbe60e7a60e3164](../../evidence/gaps-sets-008.md#g-ecbe60e7a60e3164) · [参数 P-c67a56f2bf554dc2](../../evidence/parameters-sets-015.md#p-c67a56f2bf554dc2) · [状态效果 S-21962d6bb9f3a32f](../../evidence/state_effects-sets-008.md#s-21962d6bb9f3a32f)

### observed_connections-002413

```text
(config-router-af)# nhrp redirect interest <number:1..199> <cr>
```

Handler ` RVA 0x108B1190 `；selector ` 19 `；EOL ` RVA 0x34BE7C48 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` IP access list number。

[条件 C-dd84b9ff875cf6a1](../../evidence/conditions-sets-085.md#c-dd84b9ff875cf6a1) · [参数 P-0e64524a6087594a](../../evidence/parameters-sets-002.md#p-0e64524a6087594a)

### observed_connections-002321

```text
(config-router-af)# no adjacency stagger <cr>
```

Handler ` RVA 0x11BC2D20 `；selector ` 30 `；EOL ` RVA 0x356342A8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b64ec0f07b703954](../../evidence/conditions-sets-070.md#c-b64ec0f07b703954) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002065

```text
(config-router-af)# no adjacency-check <cr>
```

Handler ` RVA 0x11A9B7D0 `；selector ` 0 `；EOL ` RVA 0x355D7C10 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a40c29f771cfb7a9](../../evidence/conditions-sets-063.md#c-a40c29f771cfb7a9) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002232

```text
(config-router-af)# no advertise passive-only <cr>
```

Handler ` RVA 0x11A9B4A0 `；selector ` 0 `；EOL ` RVA 0x355D7F70 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b0e43fe1b5b61dff](../../evidence/conditions-sets-068.md#c-b0e43fe1b5b61dff) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002473

```text
(config-router-af)# no aggregate-address <address> <address> <cr>
```

Handler ` RVA 0xF1B7BE0 `；selector ` 0 `；EOL ` RVA 0x356522E8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` Aggregate address；` address ` Aggregate mask。

[条件 C-7d6f5f8bd8be27f9](../../evidence/conditions-sets-049.md#c-7d6f5f8bd8be27f9) · [参数 P-91466a4f32e65520](../../evidence/parameters-sets-011.md#p-91466a4f32e65520) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002352

```text
(config-router-af)# no area <number:0..4294967295> <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 10 `；EOL ` RVA 0x35633B60 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value。

[条件 C-bf798629afb2a8e4](../../evidence/conditions-sets-074.md#c-bf798629afb2a8e4) · [参数 P-c94ae0b4e794f02b](../../evidence/parameters-sets-015.md#p-c94ae0b4e794f02b) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

### observed_connections-002524

```text
(config-router-af)# no area <number:0..4294967295> authentication key-chain <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 9 `；EOL ` RVA 0x35657308 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value。

[条件 C-e7ddb303ba7a7676](../../evidence/conditions-sets-090.md#c-e7ddb303ba7a7676) · [参数 P-c94ae0b4e794f02b](../../evidence/parameters-sets-015.md#p-c94ae0b4e794f02b) · [状态效果 S-560a472a0449d732](../../evidence/state_effects-sets-019.md#s-560a472a0449d732)

### observed_connections-002429

```text
(config-router-af)# no area <number:0..4294967295> default-cost <cr>
```

Handler ` RVA 0x11BBFB00 `；selector ` 7 `；EOL ` RVA 0x356576E8 `。

模式根 ` RVA 0x34265950 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` OSPF area ID as a decimal value。

[条件 C-b31591444cb6622f](../../evidence/conditions-sets-069.md#c-b31591444cb6622f) · [参数 P-c94ae0b4e794f02b](../../evidence/parameters-sets-015.md#p-c94ae0b4e794f02b) · [状态效果 S-c0c869d04d0ad5c6](../../evidence/state_effects-sets-041.md#s-c0c869d04d0ad5c6)

