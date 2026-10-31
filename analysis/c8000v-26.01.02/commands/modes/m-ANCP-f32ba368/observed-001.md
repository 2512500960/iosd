# ANCP · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-007473

```text
(config-ancp)# access-loop-encapsulation data-link <number:0..1> encap1 <number:0..2> encap2 <number:0..8> <cr>
```

Handler ` RVA 0xB25F6B0 `；selector ` 19 `；EOL ` RVA 0x336E4CA0 `。

模式根 ` RVA 0x336DF2F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` 0 ATM 1 Ethernet；` unsigned_number ` 0 Not-Avail 1/2 Untagged/Single-Tagged Eth；` unsigned_number ` 0 Not-Avail 1/2 PPPoA LLC/Null 3/4 IPoA LLC/Null5/6 Ethernet over AAL5 LLC FCS/no FCS7/8 Ethernet over AAL5 Null FCS/no FCS。

[条件 C-6e0734d7d6efb05f](../../evidence/conditions-sets-043.md#c-6e0734d7d6efb05f) · [参数 P-3a45c0d9188f4005](../../evidence/parameters-sets-005.md#p-3a45c0d9188f4005)

### observed_connections-007477

```text
(config-ancp)# actual-data-rate-downstream <number:dynamic> <cr>
```

Handler ` RVA 0xB25F6B0 `；selector ` 4 `；EOL ` RVA 0x336E4520 `。

模式根 ` RVA 0x336DF2F0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Actual Data Rate Downstream (kbps)。

[条件 C-49700c81ebf48f04](../../evidence/conditions-sets-029.md#c-49700c81ebf48f04) · [缺口 G-17c85c88dcf87f67](../../evidence/gaps-sets-001.md#g-17c85c88dcf87f67) · [参数 P-2adcfbca5ec90202](../../evidence/parameters-sets-004.md#p-2adcfbca5ec90202)

### observed_connections-007478

```text
(config-ancp)# actual-data-rate-upstream <number:dynamic> <cr>
```

Handler ` RVA 0xB25F6B0 `；selector ` 3 `；EOL ` RVA 0x336E4838 `。

模式根 ` RVA 0x336DF2F0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Actual Data Rate Upstream (kbps)。

[条件 C-3a70d3af520785be](../../evidence/conditions-sets-023.md#c-3a70d3af520785be) · [缺口 G-eed6f29fc238bbf8](../../evidence/gaps-sets-008.md#g-eed6f29fc238bbf8) · [参数 P-2903a82290dbf244](../../evidence/parameters-sets-004.md#p-2903a82290dbf244)

### observed_connections-007427

```text
(config-ancp)# actual-interleaving-delay-downstream <number:0..4294967295> <cr>
```

Handler ` RVA 0xB25F6B0 `；selector ` 16 `；EOL ` RVA 0x336E2000 `。

模式根 ` RVA 0x336DF2F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Actual Interleaving Delay Downstream (ms)。

[条件 C-9733fc64b2f07d6f](../../evidence/conditions-sets-058.md#c-9733fc64b2f07d6f) · [参数 P-cbe8540cb9afea2f](../../evidence/parameters-sets-015.md#p-cbe8540cb9afea2f)

### observed_connections-007429

```text
(config-ancp)# actual-interleaving-delay-upstream <number:0..4294967295> <cr>
```

Handler ` RVA 0xB25F6B0 `；selector ` 15 `；EOL ` RVA 0x336E2630 `。

模式根 ` RVA 0x336DF2F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Actual Interleaving Delay Upstream (ms)。

[条件 C-931134732fed4475](../../evidence/conditions-sets-057.md#c-931134732fed4475) · [参数 P-11c34e7057c536db](../../evidence/parameters-sets-002.md#p-11c34e7057c536db)

### observed_connections-007435

```text
(config-ancp)# attainable-data-rate-downstream <number:0..4294967295> <cr>
```

Handler ` RVA 0xB25F6B0 `；selector ` 8 `；EOL ` RVA 0x336E38C0 `。

模式根 ` RVA 0x336DF2F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Attainable Data Rate Downstream (kbps)。

[条件 C-76888c33b06175e2](../../evidence/conditions-sets-046.md#c-76888c33b06175e2) · [参数 P-a6c9de7525de9ea5](../../evidence/parameters-sets-013.md#p-a6c9de7525de9ea5)

### observed_connections-007436

```text
(config-ancp)# attainable-data-rate-upstream <number:0..4294967295> <cr>
```

Handler ` RVA 0xB25F6B0 `；selector ` 7 `；EOL ` RVA 0x336E3BD8 `。

模式根 ` RVA 0x336DF2F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Attainable Data Rate Upstream (kbps)。

[条件 C-926300bef7d8d47e](../../evidence/conditions-sets-056.md#c-926300bef7d8d47e) · [参数 P-175df01877d278cb](../../evidence/parameters-sets-002.md#p-175df01877d278cb)

### observed_connections-007475

```text
(config-ancp)# default access-loop-encapsulation data-link <number:0..1> encap1 <number:0..2> encap2 <number:0..8> <cr>
```

Handler ` RVA 0xB25F6B0 `；selector ` 19 `；EOL ` RVA 0x336E4CA0 `。

模式根 ` RVA 0x336DF2F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` 0 ATM 1 Ethernet；` unsigned_number ` 0 Not-Avail 1/2 Untagged/Single-Tagged Eth；` unsigned_number ` 0 Not-Avail 1/2 PPPoA LLC/Null 3/4 IPoA LLC/Null5/6 Ethernet over AAL5 LLC FCS/no FCS7/8 Ethernet over AAL5 Null FCS/no FCS。

[条件 C-46b42acf537b04c8](../../evidence/conditions-sets-028.md#c-46b42acf537b04c8) · [参数 P-3a45c0d9188f4005](../../evidence/parameters-sets-005.md#p-3a45c0d9188f4005) · [状态效果 S-b2c028ae8f5631fb](../../evidence/state_effects-sets-038.md#s-b2c028ae8f5631fb)

### observed_connections-007445

```text
(config-ancp)# default actual-interleaving-delay-downstream <number:0..4294967295> <cr>
```

Handler ` RVA 0xB25F6B0 `；selector ` 16 `；EOL ` RVA 0x336E2000 `。

模式根 ` RVA 0x336DF2F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Actual Interleaving Delay Downstream (ms)。

[条件 C-4a16f73bd7dfc45a](../../evidence/conditions-sets-029.md#c-4a16f73bd7dfc45a) · [参数 P-cbe8540cb9afea2f](../../evidence/parameters-sets-015.md#p-cbe8540cb9afea2f) · [状态效果 S-b2c028ae8f5631fb](../../evidence/state_effects-sets-038.md#s-b2c028ae8f5631fb)

### observed_connections-007449

```text
(config-ancp)# default actual-interleaving-delay-upstream <number:0..4294967295> <cr>
```

Handler ` RVA 0xB25F6B0 `；selector ` 15 `；EOL ` RVA 0x336E2630 `。

模式根 ` RVA 0x336DF2F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Actual Interleaving Delay Upstream (ms)。

[条件 C-acbd877862a54953](../../evidence/conditions-sets-067.md#c-acbd877862a54953) · [参数 P-11c34e7057c536db](../../evidence/parameters-sets-002.md#p-11c34e7057c536db) · [状态效果 S-b2c028ae8f5631fb](../../evidence/state_effects-sets-038.md#s-b2c028ae8f5631fb)

### observed_connections-007461

```text
(config-ancp)# default attainable-data-rate-downstream <number:0..4294967295> <cr>
```

Handler ` RVA 0xB25F6B0 `；selector ` 8 `；EOL ` RVA 0x336E38C0 `。

模式根 ` RVA 0x336DF2F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Attainable Data Rate Downstream (kbps)。

[条件 C-f66cf955ed88390b](../../evidence/conditions-sets-095.md#c-f66cf955ed88390b) · [参数 P-a6c9de7525de9ea5](../../evidence/parameters-sets-013.md#p-a6c9de7525de9ea5) · [状态效果 S-b2c028ae8f5631fb](../../evidence/state_effects-sets-038.md#s-b2c028ae8f5631fb)

### observed_connections-007463

```text
(config-ancp)# default attainable-data-rate-upstream <number:0..4294967295> <cr>
```

Handler ` RVA 0xB25F6B0 `；selector ` 7 `；EOL ` RVA 0x336E3BD8 `。

模式根 ` RVA 0x336DF2F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Attainable Data Rate Upstream (kbps)。

[条件 C-c3df90f1495dd28c](../../evidence/conditions-sets-076.md#c-c3df90f1495dd28c) · [参数 P-175df01877d278cb](../../evidence/parameters-sets-002.md#p-175df01877d278cb) · [状态效果 S-b2c028ae8f5631fb](../../evidence/state_effects-sets-038.md#s-b2c028ae8f5631fb)

### observed_connections-007472

```text
(config-ancp)# default dot1q <number:1..4094> client-ID <string> <cr>
```

Handler ` RVA 0xB25F6B0 `；selector ` 2 `；EOL ` RVA 0x336E1088 `。

模式根 ` RVA 0x336DF2F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` IEEE 802.1Q VLAN ID；` string ` DSLAM client ID。

[条件 C-3a579422cbf8f00a](../../evidence/conditions-sets-023.md#c-3a579422cbf8f00a) · [参数 P-f2cd23ee0a374bc8](../../evidence/parameters-sets-018.md#p-f2cd23ee0a374bc8) · [状态效果 S-b1072ef5a42e2338](../../evidence/state_effects-sets-037.md#s-b1072ef5a42e2338)

### observed_connections-007443

```text
(config-ancp)# default dsl-line-state <number:1..3> <cr>
```

Handler ` RVA 0xB25F6B0 `；selector ` 17 `；EOL ` RVA 0x336E1CE8 `。

模式根 ` RVA 0x336DF2F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` 1 SHOWTIME 2 IDLE 3 SILENT。

[条件 C-48fbb42c97e44d34](../../evidence/conditions-sets-029.md#c-48fbb42c97e44d34) · [参数 P-a552bf669ba7d0ba](../../evidence/parameters-sets-013.md#p-a552bf669ba7d0ba) · [状态效果 S-b2c028ae8f5631fb](../../evidence/state_effects-sets-038.md#s-b2c028ae8f5631fb)

### observed_connections-007441

```text
(config-ancp)# default dsl-type <number:1..6> <cr>
```

Handler ` RVA 0xB25F6B0 `；selector ` 18 `；EOL ` RVA 0x336E19D0 `。

模式根 ` RVA 0x336DF2F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` 1/2/3 ADSL1/2/2-Plus 4/5 VDSL1/2 6 SDSL。

[条件 C-d3c952124df876e2](../../evidence/conditions-sets-082.md#c-d3c952124df876e2) · [参数 P-2611181ccbef04cd](../../evidence/parameters-sets-003.md#p-2611181ccbef04cd) · [状态效果 S-b2c028ae8f5631fb](../../evidence/state_effects-sets-038.md#s-b2c028ae8f5631fb)

### observed_connections-007469

```text
(config-ancp)# default inter-working-function <number:0..1> <cr>
```

Handler ` RVA 0xB25F6B0 `；selector ` 20 `；EOL ` RVA 0x336E4FB8 `。

模式根 ` RVA 0x336DF2F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` 0 Not-Performed 1 Performed。

[条件 C-b0a855fd0b317e44](../../evidence/conditions-sets-068.md#c-b0a855fd0b317e44) · [参数 P-32c7af806e61b39b](../../evidence/parameters-sets-004.md#p-32c7af806e61b39b) · [状态效果 S-b2c028ae8f5631fb](../../evidence/state_effects-sets-038.md#s-b2c028ae8f5631fb)

### observed_connections-007457

```text
(config-ancp)# default maximum-data-rate-downstream <number:0..4294967295> <cr>
```

Handler ` RVA 0xB25F6B0 `；selector ` 10 `；EOL ` RVA 0x336E3290 `。

模式根 ` RVA 0x336DF2F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Maximum Data Rate Downstream (kbps)。

[条件 C-2edc0361b4622472](../../evidence/conditions-sets-018.md#c-2edc0361b4622472) · [参数 P-2ed0eec4405a5305](../../evidence/parameters-sets-004.md#p-2ed0eec4405a5305) · [状态效果 S-b2c028ae8f5631fb](../../evidence/state_effects-sets-038.md#s-b2c028ae8f5631fb)

### observed_connections-007459

```text
(config-ancp)# default maximum-data-rate-upstream <number:0..4294967295> <cr>
```

Handler ` RVA 0xB25F6B0 `；selector ` 9 `；EOL ` RVA 0x336E35A8 `。

模式根 ` RVA 0x336DF2F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Maximum Data Rate Upstream (kbps)。

[条件 C-d8710fd471619f29](../../evidence/conditions-sets-083.md#c-d8710fd471619f29) · [参数 P-ccb285a146b2bbc1](../../evidence/parameters-sets-016.md#p-ccb285a146b2bbc1) · [状态效果 S-b2c028ae8f5631fb](../../evidence/state_effects-sets-038.md#s-b2c028ae8f5631fb)

### observed_connections-007447

```text
(config-ancp)# default maximum-interleaving-delay-downstream <number:0..4294967295> <cr>
```

Handler ` RVA 0xB25F6B0 `；selector ` 14 `；EOL ` RVA 0x336E2318 `。

模式根 ` RVA 0x336DF2F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Maximum Interleaving Delay Downstream (ms)。

[条件 C-8c3d59e727fd3687](../../evidence/conditions-sets-054.md#c-8c3d59e727fd3687) · [参数 P-4ec6b1970b5a51d1](../../evidence/parameters-sets-006.md#p-4ec6b1970b5a51d1) · [状态效果 S-b2c028ae8f5631fb](../../evidence/state_effects-sets-038.md#s-b2c028ae8f5631fb)

### observed_connections-007451

```text
(config-ancp)# default maximum-interleaving-delay-upstream <number:0..4294967295> <cr>
```

Handler ` RVA 0xB25F6B0 `；selector ` 13 `；EOL ` RVA 0x336E2948 `。

模式根 ` RVA 0x336DF2F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Maximum Interleaving Delay Upstream (ms)。

[条件 C-f26e342de7f081e4](../../evidence/conditions-sets-094.md#c-f26e342de7f081e4) · [参数 P-8bc032375e6d7801](../../evidence/parameters-sets-011.md#p-8bc032375e6d7801) · [状态效果 S-b2c028ae8f5631fb](../../evidence/state_effects-sets-038.md#s-b2c028ae8f5631fb)

### observed_connections-007465

```text
(config-ancp)# default minimum-data-rate-downstream <number:0..4294967295> <cr>
```

Handler ` RVA 0xB25F6B0 `；selector ` 6 `；EOL ` RVA 0x336E3EF0 `。

模式根 ` RVA 0x336DF2F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Minimum Data Rate Downstream (kbps)。

[条件 C-b7f80ed51bdcc918](../../evidence/conditions-sets-071.md#c-b7f80ed51bdcc918) · [参数 P-3ca9991b5b7e5fd6](../../evidence/parameters-sets-005.md#p-3ca9991b5b7e5fd6) · [状态效果 S-b2c028ae8f5631fb](../../evidence/state_effects-sets-038.md#s-b2c028ae8f5631fb)

### observed_connections-007467

```text
(config-ancp)# default minimum-data-rate-upstream <number:0..4294967295> <cr>
```

Handler ` RVA 0xB25F6B0 `；selector ` 5 `；EOL ` RVA 0x336E4208 `。

模式根 ` RVA 0x336DF2F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Minimum Data Rate Upstream (kbps)。

[条件 C-b53e0bfbaa0dd1d9](../../evidence/conditions-sets-070.md#c-b53e0bfbaa0dd1d9) · [参数 P-f88ccd4abd0a6bb9](../../evidence/parameters-sets-019.md#p-f88ccd4abd0a6bb9) · [状态效果 S-b2c028ae8f5631fb](../../evidence/state_effects-sets-038.md#s-b2c028ae8f5631fb)

### observed_connections-007453

```text
(config-ancp)# default minimum-low-power-data-rate-downstream <number:0..4294967295> <cr>
```

Handler ` RVA 0xB25F6B0 `；selector ` 12 `；EOL ` RVA 0x336E2C60 `。

模式根 ` RVA 0x336DF2F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Minimum Low Power Data Rate Downstream (kbps)。

[条件 C-a5671874c446c697](../../evidence/conditions-sets-064.md#c-a5671874c446c697) · [参数 P-9c2e32eeea38ffb0](../../evidence/parameters-sets-012.md#p-9c2e32eeea38ffb0) · [状态效果 S-b2c028ae8f5631fb](../../evidence/state_effects-sets-038.md#s-b2c028ae8f5631fb)

### observed_connections-007455

```text
(config-ancp)# default minimum-low-power-data-rate-upstream <number:0..4294967295> <cr>
```

Handler ` RVA 0xB25F6B0 `；selector ` 11 `；EOL ` RVA 0x336E2F78 `。

模式根 ` RVA 0x336DF2F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Minimum Low Power Data Rate Upstream (kbps)。

[条件 C-3ae437f0c6afff66](../../evidence/conditions-sets-023.md#c-3ae437f0c6afff66) · [参数 P-ec887cacb0bd963c](../../evidence/parameters-sets-018.md#p-ec887cacb0bd963c) · [状态效果 S-b2c028ae8f5631fb](../../evidence/state_effects-sets-038.md#s-b2c028ae8f5631fb)

### observed_connections-007470

```text
(config-ancp)# dot1q <number:1..4094> client-ID <string> <cr>
```

Handler ` RVA 0xB25F6B0 `；selector ` 2 `；EOL ` RVA 0x336E1088 `。

模式根 ` RVA 0x336DF2F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` IEEE 802.1Q VLAN ID；` string ` DSLAM client ID。

[条件 C-b2dac1514dc87056](../../evidence/conditions-sets-069.md#c-b2dac1514dc87056) · [参数 P-f2cd23ee0a374bc8](../../evidence/parameters-sets-018.md#p-f2cd23ee0a374bc8) · [状态效果 S-a4d29e660b15acf9](../../evidence/state_effects-sets-035.md#s-a4d29e660b15acf9)

### observed_connections-007479

```text
(config-ancp)# dot1q <number:1..4094> interface <interface> client-ID <string> <cr>
```

Handler ` RVA 0xB25F6B0 `；selector ` 2 `；EOL ` RVA 0x336E1088 `。

模式根 ` RVA 0x336DF2F0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` IEEE 802.1Q VLAN ID；` string ` DSLAM client ID。

[条件 C-c452139caa30161b](../../evidence/conditions-sets-076.md#c-c452139caa30161b) · [缺口 G-4c1a00417fa3a127](../../evidence/gaps-sets-003.md#g-4c1a00417fa3a127) · [参数 P-9fe9710641ba78b2](../../evidence/parameters-sets-012.md#p-9fe9710641ba78b2) · [状态效果 S-a4d29e660b15acf9](../../evidence/state_effects-sets-035.md#s-a4d29e660b15acf9)

### observed_connections-007426

```text
(config-ancp)# dsl-line-state <number:1..3> <cr>
```

Handler ` RVA 0xB25F6B0 `；selector ` 17 `；EOL ` RVA 0x336E1CE8 `。

模式根 ` RVA 0x336DF2F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` 1 SHOWTIME 2 IDLE 3 SILENT。

[条件 C-333be4d1f02ab5c0](../../evidence/conditions-sets-020.md#c-333be4d1f02ab5c0) · [参数 P-a552bf669ba7d0ba](../../evidence/parameters-sets-013.md#p-a552bf669ba7d0ba)

### observed_connections-007425

```text
(config-ancp)# dsl-type <number:1..6> <cr>
```

Handler ` RVA 0xB25F6B0 `；selector ` 18 `；EOL ` RVA 0x336E19D0 `。

模式根 ` RVA 0x336DF2F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` 1/2/3 ADSL1/2/2-Plus 4/5 VDSL1/2 6 SDSL。

[条件 C-abd9dabec982cc9f](../../evidence/conditions-sets-066.md#c-abd9dabec982cc9f) · [参数 P-2611181ccbef04cd](../../evidence/parameters-sets-003.md#p-2611181ccbef04cd)

### observed_connections-007424

```text
(config-ancp)# exit <cr>
```

Handler ` RVA 0xB25D870 `；selector ` 0 `；EOL ` RVA 0x336E54E0 `。

模式根 ` RVA 0x336DF2F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fc1dc3ca8f17641c](../../evidence/conditions-sets-097.md#c-fc1dc3ca8f17641c)

### observed_connections-007439

```text
(config-ancp)# inter-working-function <number:0..1> <cr>
```

Handler ` RVA 0xB25F6B0 `；selector ` 20 `；EOL ` RVA 0x336E4FB8 `。

模式根 ` RVA 0x336DF2F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` 0 Not-Performed 1 Performed。

[条件 C-c48d944164e4b33c](../../evidence/conditions-sets-076.md#c-c48d944164e4b33c) · [参数 P-32c7af806e61b39b](../../evidence/parameters-sets-004.md#p-32c7af806e61b39b)

### observed_connections-007476

```text
(config-ancp)# mac-address <hex-string> <cr>
```

Handler ` RVA 0xB25F6B0 `；selector ` 1 `；EOL ` RVA 0x336E1678 `。

模式根 ` RVA 0x336DF2F0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` hexstring ` Neighbor's MAC。

[条件 C-c1d820555a7c81f4](../../evidence/conditions-sets-075.md#c-c1d820555a7c81f4) · [缺口 G-b33c037b122286dc](../../evidence/gaps-sets-006.md#g-b33c037b122286dc) · [参数 P-267ad468b4645cb2](../../evidence/parameters-sets-003.md#p-267ad468b4645cb2)

### observed_connections-007433

```text
(config-ancp)# maximum-data-rate-downstream <number:0..4294967295> <cr>
```

Handler ` RVA 0xB25F6B0 `；selector ` 10 `；EOL ` RVA 0x336E3290 `。

模式根 ` RVA 0x336DF2F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Maximum Data Rate Downstream (kbps)。

[条件 C-22644f28e3bac59b](../../evidence/conditions-sets-013.md#c-22644f28e3bac59b) · [参数 P-2ed0eec4405a5305](../../evidence/parameters-sets-004.md#p-2ed0eec4405a5305)

### observed_connections-007434

```text
(config-ancp)# maximum-data-rate-upstream <number:0..4294967295> <cr>
```

Handler ` RVA 0xB25F6B0 `；selector ` 9 `；EOL ` RVA 0x336E35A8 `。

模式根 ` RVA 0x336DF2F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Maximum Data Rate Upstream (kbps)。

[条件 C-1a3865b1fbb893a8](../../evidence/conditions-sets-010.md#c-1a3865b1fbb893a8) · [参数 P-ccb285a146b2bbc1](../../evidence/parameters-sets-016.md#p-ccb285a146b2bbc1)

### observed_connections-007428

```text
(config-ancp)# maximum-interleaving-delay-downstream <number:0..4294967295> <cr>
```

Handler ` RVA 0xB25F6B0 `；selector ` 14 `；EOL ` RVA 0x336E2318 `。

模式根 ` RVA 0x336DF2F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Maximum Interleaving Delay Downstream (ms)。

[条件 C-afb18b1f3c8479c6](../../evidence/conditions-sets-068.md#c-afb18b1f3c8479c6) · [参数 P-4ec6b1970b5a51d1](../../evidence/parameters-sets-006.md#p-4ec6b1970b5a51d1)

### observed_connections-007430

```text
(config-ancp)# maximum-interleaving-delay-upstream <number:0..4294967295> <cr>
```

Handler ` RVA 0xB25F6B0 `；selector ` 13 `；EOL ` RVA 0x336E2948 `。

模式根 ` RVA 0x336DF2F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Maximum Interleaving Delay Upstream (ms)。

[条件 C-fac8dd4482680310](../../evidence/conditions-sets-097.md#c-fac8dd4482680310) · [参数 P-8bc032375e6d7801](../../evidence/parameters-sets-011.md#p-8bc032375e6d7801)

### observed_connections-007437

```text
(config-ancp)# minimum-data-rate-downstream <number:0..4294967295> <cr>
```

Handler ` RVA 0xB25F6B0 `；selector ` 6 `；EOL ` RVA 0x336E3EF0 `。

模式根 ` RVA 0x336DF2F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Minimum Data Rate Downstream (kbps)。

[条件 C-74c0c98008715de4](../../evidence/conditions-sets-045.md#c-74c0c98008715de4) · [参数 P-3ca9991b5b7e5fd6](../../evidence/parameters-sets-005.md#p-3ca9991b5b7e5fd6)

### observed_connections-007438

```text
(config-ancp)# minimum-data-rate-upstream <number:0..4294967295> <cr>
```

Handler ` RVA 0xB25F6B0 `；selector ` 5 `；EOL ` RVA 0x336E4208 `。

模式根 ` RVA 0x336DF2F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Minimum Data Rate Upstream (kbps)。

[条件 C-fe366438eda24387](../../evidence/conditions-sets-098.md#c-fe366438eda24387) · [参数 P-f88ccd4abd0a6bb9](../../evidence/parameters-sets-019.md#p-f88ccd4abd0a6bb9)

### observed_connections-007431

```text
(config-ancp)# minimum-low-power-data-rate-downstream <number:0..4294967295> <cr>
```

Handler ` RVA 0xB25F6B0 `；selector ` 12 `；EOL ` RVA 0x336E2C60 `。

模式根 ` RVA 0x336DF2F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Minimum Low Power Data Rate Downstream (kbps)。

[条件 C-423a5a7149c1b722](../../evidence/conditions-sets-026.md#c-423a5a7149c1b722) · [参数 P-9c2e32eeea38ffb0](../../evidence/parameters-sets-012.md#p-9c2e32eeea38ffb0)

### observed_connections-007432

```text
(config-ancp)# minimum-low-power-data-rate-upstream <number:0..4294967295> <cr>
```

Handler ` RVA 0xB25F6B0 `；selector ` 11 `；EOL ` RVA 0x336E2F78 `。

模式根 ` RVA 0x336DF2F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Minimum Low Power Data Rate Upstream (kbps)。

[条件 C-a115778ee723e523](../../evidence/conditions-sets-062.md#c-a115778ee723e523) · [参数 P-ec887cacb0bd963c](../../evidence/parameters-sets-018.md#p-ec887cacb0bd963c)

### observed_connections-007474

```text
(config-ancp)# no access-loop-encapsulation data-link <number:0..1> encap1 <number:0..2> encap2 <number:0..8> <cr>
```

Handler ` RVA 0xB25F6B0 `；selector ` 19 `；EOL ` RVA 0x336E4CA0 `。

模式根 ` RVA 0x336DF2F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` 0 ATM 1 Ethernet；` unsigned_number ` 0 Not-Avail 1/2 Untagged/Single-Tagged Eth；` unsigned_number ` 0 Not-Avail 1/2 PPPoA LLC/Null 3/4 IPoA LLC/Null5/6 Ethernet over AAL5 LLC FCS/no FCS7/8 Ethernet over AAL5 Null FCS/no FCS。

[条件 C-634cd3f62960f53d](../../evidence/conditions-sets-038.md#c-634cd3f62960f53d) · [参数 P-3a45c0d9188f4005](../../evidence/parameters-sets-005.md#p-3a45c0d9188f4005) · [状态效果 S-45f69076ef331c76](../../evidence/state_effects-sets-015.md#s-45f69076ef331c76)

### observed_connections-007444

```text
(config-ancp)# no actual-interleaving-delay-downstream <number:0..4294967295> <cr>
```

Handler ` RVA 0xB25F6B0 `；selector ` 16 `；EOL ` RVA 0x336E2000 `。

模式根 ` RVA 0x336DF2F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Actual Interleaving Delay Downstream (ms)。

[条件 C-412a1c263bcadd91](../../evidence/conditions-sets-025.md#c-412a1c263bcadd91) · [参数 P-cbe8540cb9afea2f](../../evidence/parameters-sets-015.md#p-cbe8540cb9afea2f) · [状态效果 S-45f69076ef331c76](../../evidence/state_effects-sets-015.md#s-45f69076ef331c76)

### observed_connections-007448

```text
(config-ancp)# no actual-interleaving-delay-upstream <number:0..4294967295> <cr>
```

Handler ` RVA 0xB25F6B0 `；selector ` 15 `；EOL ` RVA 0x336E2630 `。

模式根 ` RVA 0x336DF2F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Actual Interleaving Delay Upstream (ms)。

[条件 C-2a7116adf986dfcc](../../evidence/conditions-sets-017.md#c-2a7116adf986dfcc) · [参数 P-11c34e7057c536db](../../evidence/parameters-sets-002.md#p-11c34e7057c536db) · [状态效果 S-45f69076ef331c76](../../evidence/state_effects-sets-015.md#s-45f69076ef331c76)

### observed_connections-007460

```text
(config-ancp)# no attainable-data-rate-downstream <number:0..4294967295> <cr>
```

Handler ` RVA 0xB25F6B0 `；selector ` 8 `；EOL ` RVA 0x336E38C0 `。

模式根 ` RVA 0x336DF2F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Attainable Data Rate Downstream (kbps)。

[条件 C-cf2c57366223b4be](../../evidence/conditions-sets-080.md#c-cf2c57366223b4be) · [参数 P-a6c9de7525de9ea5](../../evidence/parameters-sets-013.md#p-a6c9de7525de9ea5) · [状态效果 S-45f69076ef331c76](../../evidence/state_effects-sets-015.md#s-45f69076ef331c76)

### observed_connections-007462

```text
(config-ancp)# no attainable-data-rate-upstream <number:0..4294967295> <cr>
```

Handler ` RVA 0xB25F6B0 `；selector ` 7 `；EOL ` RVA 0x336E3BD8 `。

模式根 ` RVA 0x336DF2F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Attainable Data Rate Upstream (kbps)。

[条件 C-e795552b8782d2d1](../../evidence/conditions-sets-089.md#c-e795552b8782d2d1) · [参数 P-175df01877d278cb](../../evidence/parameters-sets-002.md#p-175df01877d278cb) · [状态效果 S-45f69076ef331c76](../../evidence/state_effects-sets-015.md#s-45f69076ef331c76)

### observed_connections-007471

```text
(config-ancp)# no dot1q <number:1..4094> client-ID <string> <cr>
```

Handler ` RVA 0xB25F6B0 `；selector ` 2 `；EOL ` RVA 0x336E1088 `。

模式根 ` RVA 0x336DF2F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` IEEE 802.1Q VLAN ID；` string ` DSLAM client ID。

[条件 C-a8f245651058fcbd](../../evidence/conditions-sets-065.md#c-a8f245651058fcbd) · [参数 P-f2cd23ee0a374bc8](../../evidence/parameters-sets-018.md#p-f2cd23ee0a374bc8) · [状态效果 S-294b58d4c277cdfe](../../evidence/state_effects-sets-009.md#s-294b58d4c277cdfe)

### observed_connections-007442

```text
(config-ancp)# no dsl-line-state <number:1..3> <cr>
```

Handler ` RVA 0xB25F6B0 `；selector ` 17 `；EOL ` RVA 0x336E1CE8 `。

模式根 ` RVA 0x336DF2F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` 1 SHOWTIME 2 IDLE 3 SILENT。

[条件 C-531a0c42b51d2c7d](../../evidence/conditions-sets-032.md#c-531a0c42b51d2c7d) · [参数 P-a552bf669ba7d0ba](../../evidence/parameters-sets-013.md#p-a552bf669ba7d0ba) · [状态效果 S-45f69076ef331c76](../../evidence/state_effects-sets-015.md#s-45f69076ef331c76)

### observed_connections-007440

```text
(config-ancp)# no dsl-type <number:1..6> <cr>
```

Handler ` RVA 0xB25F6B0 `；selector ` 18 `；EOL ` RVA 0x336E19D0 `。

模式根 ` RVA 0x336DF2F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` 1/2/3 ADSL1/2/2-Plus 4/5 VDSL1/2 6 SDSL。

[条件 C-2475fcbc49698d38](../../evidence/conditions-sets-014.md#c-2475fcbc49698d38) · [参数 P-2611181ccbef04cd](../../evidence/parameters-sets-003.md#p-2611181ccbef04cd) · [状态效果 S-45f69076ef331c76](../../evidence/state_effects-sets-015.md#s-45f69076ef331c76)

### observed_connections-007468

```text
(config-ancp)# no inter-working-function <number:0..1> <cr>
```

Handler ` RVA 0xB25F6B0 `；selector ` 20 `；EOL ` RVA 0x336E4FB8 `。

模式根 ` RVA 0x336DF2F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` 0 Not-Performed 1 Performed。

[条件 C-605dff83304168c2](../../evidence/conditions-sets-037.md#c-605dff83304168c2) · [参数 P-32c7af806e61b39b](../../evidence/parameters-sets-004.md#p-32c7af806e61b39b) · [状态效果 S-45f69076ef331c76](../../evidence/state_effects-sets-015.md#s-45f69076ef331c76)

### observed_connections-007456

```text
(config-ancp)# no maximum-data-rate-downstream <number:0..4294967295> <cr>
```

Handler ` RVA 0xB25F6B0 `；selector ` 10 `；EOL ` RVA 0x336E3290 `。

模式根 ` RVA 0x336DF2F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Maximum Data Rate Downstream (kbps)。

[条件 C-f21a82e5c627eb5c](../../evidence/conditions-sets-093.md#c-f21a82e5c627eb5c) · [参数 P-2ed0eec4405a5305](../../evidence/parameters-sets-004.md#p-2ed0eec4405a5305) · [状态效果 S-45f69076ef331c76](../../evidence/state_effects-sets-015.md#s-45f69076ef331c76)

### observed_connections-007458

```text
(config-ancp)# no maximum-data-rate-upstream <number:0..4294967295> <cr>
```

Handler ` RVA 0xB25F6B0 `；selector ` 9 `；EOL ` RVA 0x336E35A8 `。

模式根 ` RVA 0x336DF2F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Maximum Data Rate Upstream (kbps)。

[条件 C-cd04405c607723cd](../../evidence/conditions-sets-079.md#c-cd04405c607723cd) · [参数 P-ccb285a146b2bbc1](../../evidence/parameters-sets-016.md#p-ccb285a146b2bbc1) · [状态效果 S-45f69076ef331c76](../../evidence/state_effects-sets-015.md#s-45f69076ef331c76)

### observed_connections-007446

```text
(config-ancp)# no maximum-interleaving-delay-downstream <number:0..4294967295> <cr>
```

Handler ` RVA 0xB25F6B0 `；selector ` 14 `；EOL ` RVA 0x336E2318 `。

模式根 ` RVA 0x336DF2F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Maximum Interleaving Delay Downstream (ms)。

[条件 C-c3594ec0b17f53c8](../../evidence/conditions-sets-075.md#c-c3594ec0b17f53c8) · [参数 P-4ec6b1970b5a51d1](../../evidence/parameters-sets-006.md#p-4ec6b1970b5a51d1) · [状态效果 S-45f69076ef331c76](../../evidence/state_effects-sets-015.md#s-45f69076ef331c76)

### observed_connections-007450

```text
(config-ancp)# no maximum-interleaving-delay-upstream <number:0..4294967295> <cr>
```

Handler ` RVA 0xB25F6B0 `；selector ` 13 `；EOL ` RVA 0x336E2948 `。

模式根 ` RVA 0x336DF2F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Maximum Interleaving Delay Upstream (ms)。

[条件 C-54e1b4eb5ebb3755](../../evidence/conditions-sets-033.md#c-54e1b4eb5ebb3755) · [参数 P-8bc032375e6d7801](../../evidence/parameters-sets-011.md#p-8bc032375e6d7801) · [状态效果 S-45f69076ef331c76](../../evidence/state_effects-sets-015.md#s-45f69076ef331c76)

### observed_connections-007464

```text
(config-ancp)# no minimum-data-rate-downstream <number:0..4294967295> <cr>
```

Handler ` RVA 0xB25F6B0 `；selector ` 6 `；EOL ` RVA 0x336E3EF0 `。

模式根 ` RVA 0x336DF2F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Minimum Data Rate Downstream (kbps)。

[条件 C-0a51b809b513904e](../../evidence/conditions-sets-004.md#c-0a51b809b513904e) · [参数 P-3ca9991b5b7e5fd6](../../evidence/parameters-sets-005.md#p-3ca9991b5b7e5fd6) · [状态效果 S-45f69076ef331c76](../../evidence/state_effects-sets-015.md#s-45f69076ef331c76)

### observed_connections-007466

```text
(config-ancp)# no minimum-data-rate-upstream <number:0..4294967295> <cr>
```

Handler ` RVA 0xB25F6B0 `；selector ` 5 `；EOL ` RVA 0x336E4208 `。

模式根 ` RVA 0x336DF2F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Minimum Data Rate Upstream (kbps)。

[条件 C-fa0921ecc623b1de](../../evidence/conditions-sets-097.md#c-fa0921ecc623b1de) · [参数 P-f88ccd4abd0a6bb9](../../evidence/parameters-sets-019.md#p-f88ccd4abd0a6bb9) · [状态效果 S-45f69076ef331c76](../../evidence/state_effects-sets-015.md#s-45f69076ef331c76)

### observed_connections-007452

```text
(config-ancp)# no minimum-low-power-data-rate-downstream <number:0..4294967295> <cr>
```

Handler ` RVA 0xB25F6B0 `；selector ` 12 `；EOL ` RVA 0x336E2C60 `。

模式根 ` RVA 0x336DF2F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Minimum Low Power Data Rate Downstream (kbps)。

[条件 C-5af0df612cdd446e](../../evidence/conditions-sets-036.md#c-5af0df612cdd446e) · [参数 P-9c2e32eeea38ffb0](../../evidence/parameters-sets-012.md#p-9c2e32eeea38ffb0) · [状态效果 S-45f69076ef331c76](../../evidence/state_effects-sets-015.md#s-45f69076ef331c76)

### observed_connections-007454

```text
(config-ancp)# no minimum-low-power-data-rate-upstream <number:0..4294967295> <cr>
```

Handler ` RVA 0xB25F6B0 `；selector ` 11 `；EOL ` RVA 0x336E2F78 `。

模式根 ` RVA 0x336DF2F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Minimum Low Power Data Rate Upstream (kbps)。

[条件 C-6a532cd9d03aedfa](../../evidence/conditions-sets-041.md#c-6a532cd9d03aedfa) · [参数 P-ec887cacb0bd963c](../../evidence/parameters-sets-018.md#p-ec887cacb0bd963c) · [状态效果 S-45f69076ef331c76](../../evidence/state_effects-sets-015.md#s-45f69076ef331c76)
