# config-service-instance · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-006031

```text
(config-if-srv)# bridge-domain <number:dynamic> <cr>
```

Handler ` RVA 0xBF7FCB0 `；selector ` 0 `；EOL ` RVA 0x33958EF8 `。

模式根 ` RVA 0x33967928 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Bridge-domain number。

[条件 C-4e93df83155b5a25](../../evidence/conditions-sets-031.md#c-4e93df83155b5a25) · [缺口 G-b993303d8a3e9924](../../evidence/gaps-sets-007.md#g-b993303d8a3e9924) · [参数 P-735c645cccdd523e](../../evidence/parameters-sets-009.md#p-735c645cccdd523e) · [状态效果 S-59bea50fdc0db030](../../evidence/state_effects-sets-019.md#s-59bea50fdc0db030)

### observed_connections-005935

```text
(config-if-srv)# bridge-domain from-encapsulation <cr>
```

Handler ` RVA 0xBF7FCB0 `；selector ` 0 `；EOL ` RVA 0x33958EF8 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e7f8789eecbd2bd1](../../evidence/conditions-sets-090.md#c-e7f8789eecbd2bd1) · [状态效果 S-bcdc24a59e9ee46e](../../evidence/state_effects-sets-040.md#s-bcdc24a59e9ee46e)

### observed_connections-005985

```text
(config-if-srv)# cfm encapsulation dot1q <number:1..4094> <cr>
```

Handler ` RVA 0xBDD1C90 `；selector ` 0 `；EOL ` RVA 0x3390B6F0 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` VLAN id。

[条件 C-0d63defdb01cc845](../../evidence/conditions-sets-005.md#c-0d63defdb01cc845) · [参数 P-60ce2bae1c879ef7](../../evidence/parameters-sets-008.md#p-60ce2bae1c879ef7) · [状态效果 S-90d6b115dd683d0a](../../evidence/state_effects-sets-031.md#s-90d6b115dd683d0a)

### observed_connections-005979

```text
(config-if-srv)# cfm latching-loopback domain <string> <cr>
```

Handler ` RVA 0xBDD1F90 `；selector ` 0 `；EOL ` RVA 0x3390C200 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` maintenance domain name。

[条件 C-8ea3d43bd8b821e1](../../evidence/conditions-sets-055.md#c-8ea3d43bd8b821e1) · [参数 P-84014ef92ec70cb4](../../evidence/parameters-sets-010.md#p-84014ef92ec70cb4)

### observed_connections-006016

```text
(config-if-srv)# cfm mep domain <string> mpid <number:1..8191> <cr>
```

Handler ` RVA 0xBDD0E80 `；selector ` 0 `；EOL ` RVA 0x3390B328 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` maintenance domain name；` unsigned_number ` Maintenance End Point Identifier。

[条件 C-fba159c420ce3650](../../evidence/conditions-sets-097.md#c-fba159c420ce3650) · [参数 P-0f5c72776aafd3bb](../../evidence/parameters-sets-002.md#p-0f5c72776aafd3bb)

### observed_connections-005975

```text
(config-if-srv)# cfm mip level <number:0..7> <cr>
```

Handler ` RVA 0xBDD19C0 `；selector ` 0 `；EOL ` RVA 0x3390BDF8 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` maintenance level number。

[条件 C-40a4c164022cec19](../../evidence/conditions-sets-025.md#c-40a4c164022cec19) · [参数 P-ae6ae2a599be4341](../../evidence/parameters-sets-013.md#p-ae6ae2a599be4341)

### observed_connections-005951

```text
(config-if-srv)# default bridge-domain from-encapsulation <cr>
```

Handler ` RVA 0xBF7FCB0 `；selector ` 0 `；EOL ` RVA 0x33958EF8 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e7f8789eecbd2bd1](../../evidence/conditions-sets-090.md#c-e7f8789eecbd2bd1) · [状态效果 S-6daf2611ee0d0cdf](../../evidence/state_effects-sets-023.md#s-6daf2611ee0d0cdf)

### observed_connections-005948

```text
(config-if-srv)# default cfm encapsulation <cr>
```

Handler ` RVA 0xBDD1C90 `；selector ` 0 `；EOL ` RVA 0x3390B6F0 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e976863b58a17ad9](../../evidence/conditions-sets-090.md#c-e976863b58a17ad9) · [状态效果 S-b411fde426533d3a](../../evidence/state_effects-sets-038.md#s-b411fde426533d3a)

### observed_connections-006004

```text
(config-if-srv)# default cfm latching-loopback domain <string> <cr>
```

Handler ` RVA 0xBDD1F90 `；selector ` 0 `；EOL ` RVA 0x3390C200 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` maintenance domain name。

[条件 C-8ea3d43bd8b821e1](../../evidence/conditions-sets-055.md#c-8ea3d43bd8b821e1) · [参数 P-84014ef92ec70cb4](../../evidence/parameters-sets-010.md#p-84014ef92ec70cb4) · [状态效果 S-b411fde426533d3a](../../evidence/state_effects-sets-038.md#s-b411fde426533d3a)

### observed_connections-006023

```text
(config-if-srv)# default cfm mep domain <string> mpid <number:1..8191> <cr>
```

Handler ` RVA 0xBDD0E80 `；selector ` 0 `；EOL ` RVA 0x3390B328 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` maintenance domain name；` unsigned_number ` Maintenance End Point Identifier。

[条件 C-fba159c420ce3650](../../evidence/conditions-sets-097.md#c-fba159c420ce3650) · [参数 P-0f5c72776aafd3bb](../../evidence/parameters-sets-002.md#p-0f5c72776aafd3bb) · [状态效果 S-b411fde426533d3a](../../evidence/state_effects-sets-038.md#s-b411fde426533d3a)

### observed_connections-005952

```text
(config-if-srv)# default cfm mip <cr>
```

Handler ` RVA 0xBDD19C0 `；selector ` 0 `；EOL ` RVA 0x3390BDF8 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-14822cf81f9ffea1](../../evidence/conditions-sets-008.md#c-14822cf81f9ffea1) · [状态效果 S-b411fde426533d3a](../../evidence/state_effects-sets-038.md#s-b411fde426533d3a)

### observed_connections-005934

```text
(config-if-srv)# default description <cr>
```

Handler ` RVA 0xC00ACA0 `；selector ` 29 `；EOL ` RVA 0x33968838 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-69e5281cc834c135](../../evidence/conditions-sets-041.md#c-69e5281cc834c135) · [状态效果 S-b411fde426533d3a](../../evidence/state_effects-sets-038.md#s-b411fde426533d3a)

### observed_connections-005933

```text
(config-if-srv)# default encapsulation <cr>
```

Handler ` RVA 0xC008380 `；selector ` 1 `；EOL ` RVA 0x3396A428 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3a12f9a8975d1c37](../../evidence/conditions-sets-022.md#c-3a12f9a8975d1c37) · [状态效果 S-b411fde426533d3a](../../evidence/state_effects-sets-038.md#s-b411fde426533d3a)

### observed_connections-005994

```text
(config-if-srv)# default errdisable recovery cause mac-security <cr>
```

Handler ` RVA 0xC035C70 `；selector ` 0 `；EOL ` RVA 0x339855B8 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-33c550deee4c74da](../../evidence/conditions-sets-020.md#c-33c550deee4c74da) · [状态效果 S-a32cb8ff588bfe8e](../../evidence/state_effects-sets-035.md#s-a32cb8ff588bfe8e)

### observed_connections-005961

```text
(config-if-srv)# default ethernet egress-filter <cr>
```

Handler ` RVA 0xC03E6B0 `；selector ` 14 `；EOL ` RVA 0x339895B0 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8753624b0239f673](../../evidence/conditions-sets-052.md#c-8753624b0239f673) · [状态效果 S-b411fde426533d3a](../../evidence/state_effects-sets-038.md#s-b411fde426533d3a)

### observed_connections-005996

```text
(config-if-srv)# default ethernet loopback permit external <cr>
```

Handler ` RVA 0xBF17F80 `；selector ` 1 `；EOL ` RVA 0x339430C0 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4c50237e7c874690](../../evidence/conditions-sets-030.md#c-4c50237e7c874690) · [状态效果 S-21a4e65b46fdef14](../../evidence/state_effects-sets-008.md#s-21a4e65b46fdef14)

### observed_connections-005998

```text
(config-if-srv)# default ethernet loopback permit internal <cr>
```

Handler ` RVA 0xBF17F80 `；selector ` 2 `；EOL ` RVA 0x339433B0 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4c50237e7c874690](../../evidence/conditions-sets-030.md#c-4c50237e7c874690) · [状态效果 S-68ee60d0941bced3](../../evidence/state_effects-sets-022.md#s-68ee60d0941bced3)

### observed_connections-005922

```text
(config-if-srv)# default exit <cr>
```

Handler ` RVA 0xC00B4C0 `；selector ` 0 `；EOL ` RVA 0x339679C8 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-b411fde426533d3a](../../evidence/state_effects-sets-038.md#s-b411fde426533d3a)

### observed_connections-005987

```text
(config-if-srv)# default ip access-group in <cr>
```

Handler ` RVA 0xEF287D0 `；selector ` 0 `；EOL ` RVA 0x3447C370 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-81dcf23d5e969725](../../evidence/conditions-sets-050.md#c-81dcf23d5e969725) · [状态效果 S-b411fde426533d3a](../../evidence/state_effects-sets-038.md#s-b411fde426533d3a)

### observed_connections-005990

```text
(config-if-srv)# default ip access-group out <cr>
```

Handler ` RVA 0xEF287D0 `；selector ` 1 `；EOL ` RVA 0x3447C618 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-81dcf23d5e969725](../../evidence/conditions-sets-050.md#c-81dcf23d5e969725) · [状态效果 S-b411fde426533d3a](../../evidence/state_effects-sets-038.md#s-b411fde426533d3a)

### observed_connections-006026

```text
(config-if-srv)# default ip dhcp relay information option subscriber-id <cr>
```

Handler ` RVA 0xC008380 `；selector ` 10 `；EOL ` RVA 0x3396E680 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7fc85571929d6f2c](../../evidence/conditions-sets-050.md#c-7fc85571929d6f2c) · [状态效果 S-b411fde426533d3a](../../evidence/state_effects-sets-038.md#s-b411fde426533d3a)

### observed_connections-006021

```text
(config-if-srv)# default ip igmp snooping access-group <number:1..199> <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 49 `；EOL ` RVA 0x33A4D598 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Access list number。

[条件 C-4f3a347418e6011b](../../evidence/conditions-sets-031.md#c-4f3a347418e6011b) · [参数 P-03893a36127cfdb5](../../evidence/parameters-sets-001.md#p-03893a36127cfdb5) · [状态效果 S-b411fde426533d3a](../../evidence/state_effects-sets-038.md#s-b411fde426533d3a)

### observed_connections-006015

```text
(config-if-srv)# default ip igmp snooping limit <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 50 `；EOL ` RVA 0x33A4DAF0 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5f5db7ab7f0b66a8](../../evidence/conditions-sets-037.md#c-5f5db7ab7f0b66a8) · [状态效果 S-e48af32078b952d8](../../evidence/state_effects-sets-048.md#s-e48af32078b952d8)

### observed_connections-006019

```text
(config-if-srv)# default ip igmp snooping tcn flood <cr>
```

Handler ` RVA 0xC30A7A0 `；selector ` 0 `；EOL ` RVA 0x33A4E2C8 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8317c5a2a68495cd](../../evidence/conditions-sets-051.md#c-8317c5a2a68495cd) · [状态效果 S-b411fde426533d3a](../../evidence/state_effects-sets-038.md#s-b411fde426533d3a)

### observed_connections-005980

```text
(config-if-srv)# default ip verify source <cr>
```

Handler ` RVA 0xC008380 `；selector ` 11 `；EOL ` RVA 0x3396EA40 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2572a3a3384a4b80](../../evidence/conditions-sets-015.md#c-2572a3a3384a4b80) · [状态效果 S-b411fde426533d3a](../../evidence/state_effects-sets-038.md#s-b411fde426533d3a)

### observed_connections-006000

```text
(config-if-srv)# default ipv6 traffic-filter <string> in <cr>
```

Handler ` RVA 0xEF287D0 `；selector ` 2 `；EOL ` RVA 0x3447CC60 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` ACL name。

[条件 C-823531dbc725f732](../../evidence/conditions-sets-050.md#c-823531dbc725f732) · [参数 P-a815cd73ebdcbb17](../../evidence/parameters-sets-013.md#p-a815cd73ebdcbb17) · [状态效果 S-10535eb6dcef682f](../../evidence/state_effects-sets-004.md#s-10535eb6dcef682f)

### observed_connections-006003

```text
(config-if-srv)# default ipv6 traffic-filter <string> out <cr>
```

Handler ` RVA 0xEF287D0 `；selector ` 3 `；EOL ` RVA 0x3447CF18 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` ACL name。

[条件 C-823531dbc725f732](../../evidence/conditions-sets-050.md#c-823531dbc725f732) · [参数 P-a815cd73ebdcbb17](../../evidence/parameters-sets-013.md#p-a815cd73ebdcbb17) · [状态效果 S-60ede71473b73804](../../evidence/state_effects-sets-021.md#s-60ede71473b73804)

### observed_connections-005955

```text
(config-if-srv)# default lldp enable <cr>
```

Handler ` RVA 0xC008380 `；selector ` 15 `；EOL ` RVA 0x33970B78 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-fc6548ab4e46f692](../../evidence/conditions-sets-097.md#c-fc6548ab4e46f692) · [状态效果 S-b411fde426533d3a](../../evidence/state_effects-sets-038.md#s-b411fde426533d3a)

### observed_connections-006009

```text
(config-if-srv)# default mac access-group <string> in <cr>
```

Handler ` RVA 0xEF287D0 `；selector ` 6 `；EOL ` RVA 0x3447BC30 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` ACL name。

[条件 C-c3dc22356a421d71](../../evidence/conditions-sets-076.md#c-c3dc22356a421d71) · [参数 P-412d305d445a2b42](../../evidence/parameters-sets-005.md#p-412d305d445a2b42) · [状态效果 S-01a5f61b4f5a698b](../../evidence/state_effects-sets-001.md#s-01a5f61b4f5a698b)

### observed_connections-006011

```text
(config-if-srv)# default mac access-group <string> out <cr>
```

Handler ` RVA 0xEF287D0 `；selector ` 7 `；EOL ` RVA 0x3447BF28 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` ACL name。

[条件 C-aa9a0f673742b015](../../evidence/conditions-sets-066.md#c-aa9a0f673742b015) · [参数 P-412d305d445a2b42](../../evidence/parameters-sets-005.md#p-412d305d445a2b42) · [状态效果 S-4091fafbc5f2b464](../../evidence/state_effects-sets-014.md#s-4091fafbc5f2b464)

### observed_connections-005956

```text
(config-if-srv)# default rewrite ingress <cr>
```

Handler ` RVA 0xC008380 `；selector ` 3 `；EOL ` RVA 0x3396D478 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9ca44849c0fecc23](../../evidence/conditions-sets-061.md#c-9ca44849c0fecc23) · [状态效果 S-704f0788f63cf651](../../evidence/state_effects-sets-024.md#s-704f0788f63cf651)

### observed_connections-005957

```text
(config-if-srv)# default rewrite ingress <cr>
```

Handler ` RVA 0xC008380 `；selector ` 4 `；EOL ` RVA 0x3396D6F8 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9c9b804571a54d05](../../evidence/conditions-sets-060.md#c-9c9b804571a54d05) · [状态效果 S-704f0788f63cf651](../../evidence/state_effects-sets-024.md#s-704f0788f63cf651)

### observed_connections-005971

```text
(config-if-srv)# default service-policy input <string> <cr>
```

Handler ` RVA 0xC005050 `；selector ` 0 `；EOL ` RVA 0x3396DB38 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` input Policy-map name。

[条件 C-2cb5a180716b2b49](../../evidence/conditions-sets-018.md#c-2cb5a180716b2b49) · [参数 P-e2119ec8f663638b](../../evidence/parameters-sets-017.md#p-e2119ec8f663638b) · [状态效果 S-b411fde426533d3a](../../evidence/state_effects-sets-038.md#s-b411fde426533d3a)

### observed_connections-005973

```text
(config-if-srv)# default service-policy output <string> <cr>
```

Handler ` RVA 0xC005050 `；selector ` 1 `；EOL ` RVA 0x3396DE30 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` output Policy-map name。

[条件 C-2cb5a180716b2b49](../../evidence/conditions-sets-018.md#c-2cb5a180716b2b49) · [参数 P-35f3ac45dcb03036](../../evidence/parameters-sets-005.md#p-35f3ac45dcb03036) · [状态效果 S-b411fde426533d3a](../../evidence/state_effects-sets-038.md#s-b411fde426533d3a)

### observed_connections-005924

```text
(config-if-srv)# default shutdown <cr>
```

Handler ` RVA 0xC00ACA0 `；selector ` 27 `；EOL ` RVA 0x33968178 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f73fc5afc58e2a53](../../evidence/conditions-sets-095.md#c-f73fc5afc58e2a53) · [状态效果 S-b411fde426533d3a](../../evidence/state_effects-sets-038.md#s-b411fde426533d3a)

### observed_connections-005969

```text
(config-if-srv)# default snmp ifindex clear <cr>
```

Handler ` RVA 0xC00ACA0 `；selector ` 35 `；EOL ` RVA 0x33969118 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c0861e8690883c89](../../evidence/conditions-sets-074.md#c-c0861e8690883c89) · [状态效果 S-b411fde426533d3a](../../evidence/state_effects-sets-038.md#s-b411fde426533d3a)

### observed_connections-005965

```text
(config-if-srv)# default snmp ifindex persist <cr>
```

Handler ` RVA 0xC00ACA0 `；selector ` 34 `；EOL ` RVA 0x33968E70 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c0861e8690883c89](../../evidence/conditions-sets-074.md#c-c0861e8690883c89) · [状态效果 S-b411fde426533d3a](../../evidence/state_effects-sets-038.md#s-b411fde426533d3a)

### observed_connections-005963

```text
(config-if-srv)# default snmp trap link-status <cr>
```

Handler ` RVA 0xC00ACA0 `；selector ` 33 `；EOL ` RVA 0x33968BA0 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c0861e8690883c89](../../evidence/conditions-sets-074.md#c-c0861e8690883c89) · [状态效果 S-b411fde426533d3a](../../evidence/state_effects-sets-038.md#s-b411fde426533d3a)

### observed_connections-005983

```text
(config-if-srv)# default storm-control action shutdown <cr>
```

Handler ` RVA 0xC069820 `；selector ` 0 `；EOL ` RVA 0x3398CC48 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4b565d085ab24399](../../evidence/conditions-sets-030.md#c-4b565d085ab24399) · [状态效果 S-e77e51ba23674cab](../../evidence/state_effects-sets-049.md#s-e77e51ba23674cab)

### observed_connections-005929

```text
(config-if-srv)# default track <cr>
```

Handler ` RVA 0xC00ACA0 `；selector ` 28 `；EOL ` RVA 0x339684D8 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-59020c22dbefbb2b](../../evidence/conditions-sets-035.md#c-59020c22dbefbb2b) · [状态效果 S-b411fde426533d3a](../../evidence/state_effects-sets-038.md#s-b411fde426533d3a)

### observed_connections-005938

```text
(config-if-srv)# default transparent-cfm <cr>
```

Handler ` RVA 0xBEB3720 `；selector ` 0 `；EOL ` RVA 0x3391EA18 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-702ec7acce632527](../../evidence/conditions-sets-043.md#c-702ec7acce632527) · [状态效果 S-b411fde426533d3a](../../evidence/state_effects-sets-038.md#s-b411fde426533d3a)

### observed_connections-005940

```text
(config-if-srv)# default untagged-cfm <cr>
```

Handler ` RVA 0xBEB3A70 `；selector ` 0 `；EOL ` RVA 0x3391ECD0 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-702ec7acce632527](../../evidence/conditions-sets-043.md#c-702ec7acce632527) · [状态效果 S-b411fde426533d3a](../../evidence/state_effects-sets-038.md#s-b411fde426533d3a)

### observed_connections-005927

```text
(config-if-srv)# default weight <cr>
```

Handler ` RVA 0xC00ACA0 `；selector ` 26 `；EOL ` RVA 0x33967E78 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-16819a5deaf3a797](../../evidence/conditions-sets-009.md#c-16819a5deaf3a797) · [状态效果 S-b411fde426533d3a](../../evidence/state_effects-sets-038.md#s-b411fde426533d3a)

### observed_connections-005932

```text
(config-if-srv)# description <string> <cr>
```

Handler ` RVA 0xC00ACA0 `；selector ` 29 `；EOL ` RVA 0x33968838 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Up to 240 characters describing this service instance。

[条件 C-aa5716ab6f5c595c](../../evidence/conditions-sets-066.md#c-aa5716ab6f5c595c) · [参数 P-4d2abf8d248a388b](../../evidence/parameters-sets-006.md#p-4d2abf8d248a388b)

### observed_connections-006027

```text
(config-if-srv)# encapsulation <cr>
```

Handler ` RVA 0xC00ACA0 `；selector ` 32 `；EOL ` RVA 0x3396B8D0 `。

模式根 ` RVA 0x33967928 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-12a8110d2a0a4e4a](../../evidence/conditions-sets-007.md#c-12a8110d2a0a4e4a) · [缺口 G-fb07d66c49226d87](../../evidence/gaps-sets-009.md#g-fb07d66c49226d87) · [状态效果 S-445500a64f8e4a2a](../../evidence/state_effects-sets-015.md#s-445500a64f8e4a2a)

### observed_connections-006030

```text
(config-if-srv)# encapsulation default <cr>
```

Handler ` RVA 0xC008380 `；selector ` 1 `；EOL ` RVA 0x3396A428 `。

模式根 ` RVA 0x33967928 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-872311046342dfe8](../../evidence/conditions-sets-052.md#c-872311046342dfe8) · [缺口 G-fb07d66c49226d87](../../evidence/gaps-sets-009.md#g-fb07d66c49226d87) · [状态效果 S-cce94e51e5aa7792](../../evidence/state_effects-sets-043.md#s-cce94e51e5aa7792)

### observed_connections-005993

```text
(config-if-srv)# errdisable recovery cause mac-security <number:30..86400> <cr>
```

Handler ` RVA 0xC035C70 `；selector ` 0 `；EOL ` RVA 0x339855B8 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` timer interval(sec)。

[条件 C-7431006d5cc5305c](../../evidence/conditions-sets-045.md#c-7431006d5cc5305c) · [参数 P-362cc750d34bc625](../../evidence/parameters-sets-005.md#p-362cc750d34bc625) · [状态效果 S-a22d987d7472ad1d](../../evidence/state_effects-sets-034.md#s-a22d987d7472ad1d)

### observed_connections-005960

```text
(config-if-srv)# ethernet egress-filter disable <cr>
```

Handler ` RVA 0xC03E6B0 `；selector ` 14 `；EOL ` RVA 0x339895B0 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d1be6c7d7f6ba41c](../../evidence/conditions-sets-081.md#c-d1be6c7d7f6ba41c) · [状态效果 S-5c85aab71f02acf9](../../evidence/state_effects-sets-020.md#s-5c85aab71f02acf9)

### observed_connections-006035

```text
(config-if-srv)# ethernet lmi ce-vlan map <cr>
```

Handler ` RVA 0xC008380 `；selector ` 9 `；EOL ` RVA 0x33969C68 `。

模式根 ` RVA 0x33967928 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6bfca9001e46138f](../../evidence/conditions-sets-042.md#c-6bfca9001e46138f) · [缺口 G-7c3156e820d31579](../../evidence/gaps-sets-005.md#g-7c3156e820d31579) · [状态效果 S-653f92dbfc18787c](../../evidence/state_effects-sets-022.md#s-653f92dbfc18787c)

### observed_connections-005967

```text
(config-if-srv)# ethernet loopback permit external <cr>
```

Handler ` RVA 0xBF17F80 `；selector ` 1 `；EOL ` RVA 0x339430C0 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4c50237e7c874690](../../evidence/conditions-sets-030.md#c-4c50237e7c874690) · [状态效果 S-44242dc6ce4d844e](../../evidence/state_effects-sets-015.md#s-44242dc6ce4d844e)

### observed_connections-005970

```text
(config-if-srv)# ethernet loopback permit internal <cr>
```

Handler ` RVA 0xBF17F80 `；selector ` 2 `；EOL ` RVA 0x339433B0 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4c50237e7c874690](../../evidence/conditions-sets-030.md#c-4c50237e7c874690) · [状态效果 S-03005f0704885239](../../evidence/state_effects-sets-001.md#s-03005f0704885239)

### observed_connections-005917

```text
(config-if-srv)# exit <cr>
```

Handler ` RVA 0xC00B4C0 `；selector ` 0 `；EOL ` RVA 0x339679C8 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-006029

```text
(config-if-srv)# group <number:dynamic> <cr>
```

Handler ` RVA 0xC008380 `；selector ` 0 `；EOL ` RVA 0x3396E1B8 `。

模式根 ` RVA 0x33967928 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Service group ID number。

[条件 C-4df07b303db039bc](../../evidence/conditions-sets-030.md#c-4df07b303db039bc) · [缺口 G-f658b610ef60d3d6](../../evidence/gaps-sets-008.md#g-f658b610ef60d3d6) · [参数 P-cc1fdb925358f619](../../evidence/parameters-sets-015.md#p-cc1fdb925358f619)

### observed_connections-005977

```text
(config-if-srv)# ip access-group <number:1..199> in <cr>
```

Handler ` RVA 0xEF287D0 `；selector ` 0 `；EOL ` RVA 0x3447C370 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` IP access list (standard or extended)。

[条件 C-263551246ce1417a](../../evidence/conditions-sets-015.md#c-263551246ce1417a) · [参数 P-39ee2607d399f61c](../../evidence/parameters-sets-005.md#p-39ee2607d399f61c)

### observed_connections-005982

```text
(config-if-srv)# ip access-group <number:1..199> out <cr>
```

Handler ` RVA 0xEF287D0 `；selector ` 1 `；EOL ` RVA 0x3447C618 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` IP access list (standard or extended)。

[条件 C-263551246ce1417a](../../evidence/conditions-sets-015.md#c-263551246ce1417a) · [参数 P-39ee2607d399f61c](../../evidence/parameters-sets-005.md#p-39ee2607d399f61c)

### observed_connections-006025

```text
(config-if-srv)# ip dhcp relay information option subscriber-id <string> <cr>
```

Handler ` RVA 0xC008380 `；selector ` 10 `；EOL ` RVA 0x3396E680 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` subscriber-id string。

[条件 C-0e53a839f830b5a5](../../evidence/conditions-sets-006.md#c-0e53a839f830b5a5) · [参数 P-7aac72ad791fa12b](../../evidence/parameters-sets-010.md#p-7aac72ad791fa12b)

### observed_connections-006037

```text
(config-if-srv)# ip flow monitor <?option@555588f5efa0> sampler <cr>
```

Handler ` RVA 0xC1F7CA0 `；selector ` 0 `；EOL ` RVA 0x33A0B1C8 `。

模式根 ` RVA 0x33967928 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2680cb17110d020b](../../evidence/conditions-sets-015.md#c-2680cb17110d020b) · [缺口 G-576c1b7539f300fa](../../evidence/gaps-sets-004.md#g-576c1b7539f300fa) · [状态效果 S-0801271744601689](../../evidence/state_effects-sets-002.md#s-0801271744601689)

### observed_connections-006033

```text
(config-if-srv)# ip flow monitor <cr>
```

Handler ` RVA 0xC1F7D50 `；selector ` 0 `；EOL ` RVA 0x33A0B480 `。

模式根 ` RVA 0x33967928 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2fecafea42d2c258](../../evidence/conditions-sets-019.md#c-2fecafea42d2c258) · [缺口 G-df678120ccaad078](../../evidence/gaps-sets-008.md#g-df678120ccaad078) · [状态效果 S-0801271744601689](../../evidence/state_effects-sets-002.md#s-0801271744601689)

### observed_connections-006013

```text
(config-if-srv)# ip igmp snooping access-group <number:1..199> <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 49 `；EOL ` RVA 0x33A4D598 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Access list number。

[条件 C-4f3a347418e6011b](../../evidence/conditions-sets-031.md#c-4f3a347418e6011b) · [参数 P-03893a36127cfdb5](../../evidence/parameters-sets-001.md#p-03893a36127cfdb5)

### observed_connections-005991

```text
(config-if-srv)# ip igmp snooping limit <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 50 `；EOL ` RVA 0x33A4DAF0 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5f5db7ab7f0b66a8](../../evidence/conditions-sets-037.md#c-5f5db7ab7f0b66a8) · [状态效果 S-e40ea164f56a89eb](../../evidence/state_effects-sets-048.md#s-e40ea164f56a89eb)

### observed_connections-006012

```text
(config-if-srv)# ip igmp snooping tcn flood <cr>
```

Handler ` RVA 0xC30A7A0 `；selector ` 0 `；EOL ` RVA 0x33A4E2C8 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8317c5a2a68495cd](../../evidence/conditions-sets-051.md#c-8317c5a2a68495cd)

### observed_connections-006006

```text
(config-if-srv)# ip verify source vlan dhcp-snooping <cr>
```

Handler ` RVA 0xC008380 `；selector ` 11 `；EOL ` RVA 0x3396EB58 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7e9fd2b4dde10e75](../../evidence/conditions-sets-049.md#c-7e9fd2b4dde10e75) · [状态效果 S-2876e5aa946f42c1](../../evidence/state_effects-sets-009.md#s-2876e5aa946f42c1)

### observed_connections-006017

```text
(config-if-srv)# ip verify source vlan dhcp-snooping port-security <cr>
```

Handler ` RVA 0xC008380 `；selector ` 11 `；EOL ` RVA 0x3396EB30 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7e9fd2b4dde10e75](../../evidence/conditions-sets-049.md#c-7e9fd2b4dde10e75) · [状态效果 S-0638fa4426e9f035](../../evidence/state_effects-sets-002.md#s-0638fa4426e9f035)

### observed_connections-006038

```text
(config-if-srv)# ipv6 flow monitor <?option@555588f60368> sampler <cr>
```

Handler ` RVA 0xC1F7CA0 `；selector ` 0 `；EOL ` RVA 0x33A0C590 `。

模式根 ` RVA 0x33967928 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b266e79d8a56d625](../../evidence/conditions-sets-069.md#c-b266e79d8a56d625) · [缺口 G-43bf3f2e95a39d33](../../evidence/gaps-sets-003.md#g-43bf3f2e95a39d33) · [状态效果 S-4cdc4859765332db](../../evidence/state_effects-sets-017.md#s-4cdc4859765332db)

### observed_connections-006034

```text
(config-if-srv)# ipv6 flow monitor <cr>
```

Handler ` RVA 0xC1F7D50 `；selector ` 0 `；EOL ` RVA 0x33A0C848 `。

模式根 ` RVA 0x33967928 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-514b1dbe27318167](../../evidence/conditions-sets-032.md#c-514b1dbe27318167) · [缺口 G-bd9f1399044c9607](../../evidence/gaps-sets-007.md#g-bd9f1399044c9607) · [状态效果 S-4cdc4859765332db](../../evidence/state_effects-sets-017.md#s-4cdc4859765332db)

### observed_connections-005974

```text
(config-if-srv)# ipv6 traffic-filter <string> in <cr>
```

Handler ` RVA 0xEF287D0 `；selector ` 2 `；EOL ` RVA 0x3447CC60 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` ACL name。

[条件 C-823531dbc725f732](../../evidence/conditions-sets-050.md#c-823531dbc725f732) · [参数 P-a815cd73ebdcbb17](../../evidence/parameters-sets-013.md#p-a815cd73ebdcbb17) · [状态效果 S-65edf759217be011](../../evidence/state_effects-sets-022.md#s-65edf759217be011)

### observed_connections-005978

```text
(config-if-srv)# ipv6 traffic-filter <string> out <cr>
```

Handler ` RVA 0xEF287D0 `；selector ` 3 `；EOL ` RVA 0x3447CF18 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` ACL name。

[条件 C-823531dbc725f732](../../evidence/conditions-sets-050.md#c-823531dbc725f732) · [参数 P-a815cd73ebdcbb17](../../evidence/parameters-sets-013.md#p-a815cd73ebdcbb17) · [状态效果 S-e966d382facb092a](../../evidence/state_effects-sets-049.md#s-e966d382facb092a)

### observed_connections-006032

```text
(config-if-srv)# l2protocol forward <cr>
```

Handler ` RVA 0xC008380 `；selector ` 8 `；EOL ` RVA 0x339705A8 `。

模式根 ` RVA 0x33967928 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0ffce339ba18ee99](../../evidence/conditions-sets-006.md#c-0ffce339ba18ee99) · [缺口 G-3cd593744c5e7f9f](../../evidence/gaps-sets-003.md#g-3cd593744c5e7f9f) · [状态效果 S-43e0b3209de9b524](../../evidence/state_effects-sets-015.md#s-43e0b3209de9b524)

### observed_connections-005936

```text
(config-if-srv)# lldp enable <cr>
```

Handler ` RVA 0xC008380 `；selector ` 15 `；EOL ` RVA 0x33970B78 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fc6548ab4e46f692](../../evidence/conditions-sets-097.md#c-fc6548ab4e46f692)

### observed_connections-005986

```text
(config-if-srv)# mac access-group <string> in <cr>
```

Handler ` RVA 0xEF287D0 `；selector ` 6 `；EOL ` RVA 0x3447BC30 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` ACL name。

[条件 C-c3dc22356a421d71](../../evidence/conditions-sets-076.md#c-c3dc22356a421d71) · [参数 P-412d305d445a2b42](../../evidence/parameters-sets-005.md#p-412d305d445a2b42) · [状态效果 S-176bedc2b4cf0dde](../../evidence/state_effects-sets-005.md#s-176bedc2b4cf0dde)

### observed_connections-005989

```text
(config-if-srv)# mac access-group <string> out <cr>
```

Handler ` RVA 0xEF287D0 `；selector ` 7 `；EOL ` RVA 0x3447BF28 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` ACL name。

[条件 C-aa9a0f673742b015](../../evidence/conditions-sets-066.md#c-aa9a0f673742b015) · [参数 P-412d305d445a2b42](../../evidence/parameters-sets-005.md#p-412d305d445a2b42) · [状态效果 S-902240c08c9220e1](../../evidence/state_effects-sets-031.md#s-902240c08c9220e1)

### observed_connections-005946

```text
(config-if-srv)# no bridge-domain from-encapsulation <cr>
```

Handler ` RVA 0xBF7FCB0 `；selector ` 0 `；EOL ` RVA 0x33958EF8 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e7f8789eecbd2bd1](../../evidence/conditions-sets-090.md#c-e7f8789eecbd2bd1) · [状态效果 S-3eee0dd2b3b9fdd0](../../evidence/state_effects-sets-014.md#s-3eee0dd2b3b9fdd0)

### observed_connections-005944

```text
(config-if-srv)# no cfm encapsulation <cr>
```

Handler ` RVA 0xBDD1C90 `；selector ` 0 `；EOL ` RVA 0x3390B6F0 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-75651026e0c10c39](../../evidence/conditions-sets-046.md#c-75651026e0c10c39) · [状态效果 S-7fcbb978a99cf1c9](../../evidence/state_effects-sets-027.md#s-7fcbb978a99cf1c9)

### observed_connections-006002

```text
(config-if-srv)# no cfm latching-loopback domain <string> <cr>
```

Handler ` RVA 0xBDD1F90 `；selector ` 0 `；EOL ` RVA 0x3390C200 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` maintenance domain name。

[条件 C-8ea3d43bd8b821e1](../../evidence/conditions-sets-055.md#c-8ea3d43bd8b821e1) · [参数 P-84014ef92ec70cb4](../../evidence/parameters-sets-010.md#p-84014ef92ec70cb4) · [状态效果 S-7fcbb978a99cf1c9](../../evidence/state_effects-sets-027.md#s-7fcbb978a99cf1c9)

### observed_connections-006022

```text
(config-if-srv)# no cfm mep domain <string> mpid <number:1..8191> <cr>
```

Handler ` RVA 0xBDD0E80 `；selector ` 0 `；EOL ` RVA 0x3390B328 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` maintenance domain name；` unsigned_number ` Maintenance End Point Identifier。

[条件 C-fba159c420ce3650](../../evidence/conditions-sets-097.md#c-fba159c420ce3650) · [参数 P-0f5c72776aafd3bb](../../evidence/parameters-sets-002.md#p-0f5c72776aafd3bb) · [状态效果 S-7fcbb978a99cf1c9](../../evidence/state_effects-sets-027.md#s-7fcbb978a99cf1c9)

### observed_connections-005947

```text
(config-if-srv)# no cfm mip <cr>
```

Handler ` RVA 0xBDD19C0 `；selector ` 0 `；EOL ` RVA 0x3390BDF8 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b5f2ed55419bba1b](../../evidence/conditions-sets-070.md#c-b5f2ed55419bba1b) · [状态效果 S-7fcbb978a99cf1c9](../../evidence/state_effects-sets-027.md#s-7fcbb978a99cf1c9)

### observed_connections-005931

```text
(config-if-srv)# no description <cr>
```

Handler ` RVA 0xC00ACA0 `；selector ` 29 `；EOL ` RVA 0x33968838 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ee08ac2da69f2764](../../evidence/conditions-sets-092.md#c-ee08ac2da69f2764) · [状态效果 S-7fcbb978a99cf1c9](../../evidence/state_effects-sets-027.md#s-7fcbb978a99cf1c9)

### observed_connections-005930

```text
(config-if-srv)# no encapsulation <cr>
```

Handler ` RVA 0xC008380 `；selector ` 1 `；EOL ` RVA 0x3396A428 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7519f0107c0b5270](../../evidence/conditions-sets-045.md#c-7519f0107c0b5270) · [状态效果 S-7fcbb978a99cf1c9](../../evidence/state_effects-sets-027.md#s-7fcbb978a99cf1c9)

### observed_connections-005992

```text
(config-if-srv)# no errdisable recovery cause mac-security <cr>
```

Handler ` RVA 0xC035C70 `；selector ` 0 `；EOL ` RVA 0x339855B8 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c854f0e214bc9db9](../../evidence/conditions-sets-077.md#c-c854f0e214bc9db9) · [状态效果 S-df175c4000a3bcec](../../evidence/state_effects-sets-047.md#s-df175c4000a3bcec)

### observed_connections-005959

```text
(config-if-srv)# no ethernet egress-filter <cr>
```

Handler ` RVA 0xC03E6B0 `；selector ` 14 `；EOL ` RVA 0x339895B0 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-68bb9ff2ac578743](../../evidence/conditions-sets-041.md#c-68bb9ff2ac578743) · [状态效果 S-7fcbb978a99cf1c9](../../evidence/state_effects-sets-027.md#s-7fcbb978a99cf1c9)

### observed_connections-005995

```text
(config-if-srv)# no ethernet loopback permit external <cr>
```

Handler ` RVA 0xBF17F80 `；selector ` 1 `；EOL ` RVA 0x339430C0 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4c50237e7c874690](../../evidence/conditions-sets-030.md#c-4c50237e7c874690) · [状态效果 S-3844f4fd5e7407ad](../../evidence/state_effects-sets-012.md#s-3844f4fd5e7407ad)

### observed_connections-005997

```text
(config-if-srv)# no ethernet loopback permit internal <cr>
```

Handler ` RVA 0xBF17F80 `；selector ` 2 `；EOL ` RVA 0x339433B0 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4c50237e7c874690](../../evidence/conditions-sets-030.md#c-4c50237e7c874690) · [状态效果 S-8cc911f83b7d252c](../../evidence/state_effects-sets-030.md#s-8cc911f83b7d252c)

### observed_connections-005921

```text
(config-if-srv)# no exit <cr>
```

Handler ` RVA 0xC00B4C0 `；selector ` 0 `；EOL ` RVA 0x339679C8 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-7fcbb978a99cf1c9](../../evidence/state_effects-sets-027.md#s-7fcbb978a99cf1c9)

### observed_connections-005984

```text
(config-if-srv)# no ip access-group in <cr>
```

Handler ` RVA 0xEF287D0 `；selector ` 0 `；EOL ` RVA 0x3447C370 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-81dcf23d5e969725](../../evidence/conditions-sets-050.md#c-81dcf23d5e969725) · [状态效果 S-7fcbb978a99cf1c9](../../evidence/state_effects-sets-027.md#s-7fcbb978a99cf1c9)

### observed_connections-005988

```text
(config-if-srv)# no ip access-group out <cr>
```

Handler ` RVA 0xEF287D0 `；selector ` 1 `；EOL ` RVA 0x3447C618 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-81dcf23d5e969725](../../evidence/conditions-sets-050.md#c-81dcf23d5e969725) · [状态效果 S-7fcbb978a99cf1c9](../../evidence/state_effects-sets-027.md#s-7fcbb978a99cf1c9)

### observed_connections-006024

```text
(config-if-srv)# no ip dhcp relay information option subscriber-id <cr>
```

Handler ` RVA 0xC008380 `；selector ` 10 `；EOL ` RVA 0x3396E680 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4fa0a7f66d1876af](../../evidence/conditions-sets-031.md#c-4fa0a7f66d1876af) · [状态效果 S-7fcbb978a99cf1c9](../../evidence/state_effects-sets-027.md#s-7fcbb978a99cf1c9)

### observed_connections-006020

```text
(config-if-srv)# no ip igmp snooping access-group <number:1..199> <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 49 `；EOL ` RVA 0x33A4D598 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Access list number。

[条件 C-4f3a347418e6011b](../../evidence/conditions-sets-031.md#c-4f3a347418e6011b) · [参数 P-03893a36127cfdb5](../../evidence/parameters-sets-001.md#p-03893a36127cfdb5) · [状态效果 S-7fcbb978a99cf1c9](../../evidence/state_effects-sets-027.md#s-7fcbb978a99cf1c9)

### observed_connections-006014

```text
(config-if-srv)# no ip igmp snooping limit <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 50 `；EOL ` RVA 0x33A4DAF0 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5f5db7ab7f0b66a8](../../evidence/conditions-sets-037.md#c-5f5db7ab7f0b66a8) · [状态效果 S-63ef6cd8e20d792e](../../evidence/state_effects-sets-021.md#s-63ef6cd8e20d792e)

### observed_connections-006018

```text
(config-if-srv)# no ip igmp snooping tcn flood <cr>
```

Handler ` RVA 0xC30A7A0 `；selector ` 0 `；EOL ` RVA 0x33A4E2C8 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8317c5a2a68495cd](../../evidence/conditions-sets-051.md#c-8317c5a2a68495cd) · [状态效果 S-7fcbb978a99cf1c9](../../evidence/state_effects-sets-027.md#s-7fcbb978a99cf1c9)

### observed_connections-005976

```text
(config-if-srv)# no ip verify source <cr>
```

Handler ` RVA 0xC008380 `；selector ` 11 `；EOL ` RVA 0x3396EA40 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-6731aeed2ad6c144](../../evidence/conditions-sets-040.md#c-6731aeed2ad6c144) · [状态效果 S-7fcbb978a99cf1c9](../../evidence/state_effects-sets-027.md#s-7fcbb978a99cf1c9)

### observed_connections-005999

```text
(config-if-srv)# no ipv6 traffic-filter <string> in <cr>
```

Handler ` RVA 0xEF287D0 `；selector ` 2 `；EOL ` RVA 0x3447CC60 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` ACL name。

[条件 C-823531dbc725f732](../../evidence/conditions-sets-050.md#c-823531dbc725f732) · [参数 P-a815cd73ebdcbb17](../../evidence/parameters-sets-013.md#p-a815cd73ebdcbb17) · [状态效果 S-27d6f75af7fa3715](../../evidence/state_effects-sets-009.md#s-27d6f75af7fa3715)

### observed_connections-006001

```text
(config-if-srv)# no ipv6 traffic-filter <string> out <cr>
```

Handler ` RVA 0xEF287D0 `；selector ` 3 `；EOL ` RVA 0x3447CF18 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` ACL name。

[条件 C-823531dbc725f732](../../evidence/conditions-sets-050.md#c-823531dbc725f732) · [参数 P-a815cd73ebdcbb17](../../evidence/parameters-sets-013.md#p-a815cd73ebdcbb17) · [状态效果 S-7f156c8b09aaa781](../../evidence/state_effects-sets-027.md#s-7f156c8b09aaa781)

### observed_connections-005949

```text
(config-if-srv)# no lldp enable <cr>
```

Handler ` RVA 0xC008380 `；selector ` 15 `；EOL ` RVA 0x33970B78 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-fc6548ab4e46f692](../../evidence/conditions-sets-097.md#c-fc6548ab4e46f692) · [状态效果 S-7fcbb978a99cf1c9](../../evidence/state_effects-sets-027.md#s-7fcbb978a99cf1c9)

### observed_connections-006005

```text
(config-if-srv)# no mac access-group <string> in <cr>
```

Handler ` RVA 0xEF287D0 `；selector ` 6 `；EOL ` RVA 0x3447BC30 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` ACL name。

[条件 C-c3dc22356a421d71](../../evidence/conditions-sets-076.md#c-c3dc22356a421d71) · [参数 P-412d305d445a2b42](../../evidence/parameters-sets-005.md#p-412d305d445a2b42) · [状态效果 S-c07f8e9b999a142f](../../evidence/state_effects-sets-041.md#s-c07f8e9b999a142f)

### observed_connections-006010

```text
(config-if-srv)# no mac access-group <string> out <cr>
```

Handler ` RVA 0xEF287D0 `；selector ` 7 `；EOL ` RVA 0x3447BF28 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` ACL name。

[条件 C-aa9a0f673742b015](../../evidence/conditions-sets-066.md#c-aa9a0f673742b015) · [参数 P-412d305d445a2b42](../../evidence/parameters-sets-005.md#p-412d305d445a2b42) · [状态效果 S-98a980704d595f0b](../../evidence/state_effects-sets-032.md#s-98a980704d595f0b)

### observed_connections-005953

```text
(config-if-srv)# no rewrite ingress <cr>
```

Handler ` RVA 0xC008380 `；selector ` 3 `；EOL ` RVA 0x3396D478 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-2e3f9c36fc7f584d](../../evidence/conditions-sets-018.md#c-2e3f9c36fc7f584d) · [状态效果 S-22ecfd9d29081b7a](../../evidence/state_effects-sets-008.md#s-22ecfd9d29081b7a)

### observed_connections-005954

```text
(config-if-srv)# no rewrite ingress <cr>
```

Handler ` RVA 0xC008380 `；selector ` 4 `；EOL ` RVA 0x3396D6F8 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1063fee9a984e2f9](../../evidence/conditions-sets-007.md#c-1063fee9a984e2f9) · [状态效果 S-22ecfd9d29081b7a](../../evidence/state_effects-sets-008.md#s-22ecfd9d29081b7a)

### observed_connections-005968

```text
(config-if-srv)# no service-policy input <string> <cr>
```

Handler ` RVA 0xC005050 `；selector ` 0 `；EOL ` RVA 0x3396DB38 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` input Policy-map name。

[条件 C-2cb5a180716b2b49](../../evidence/conditions-sets-018.md#c-2cb5a180716b2b49) · [参数 P-e2119ec8f663638b](../../evidence/parameters-sets-017.md#p-e2119ec8f663638b) · [状态效果 S-7fcbb978a99cf1c9](../../evidence/state_effects-sets-027.md#s-7fcbb978a99cf1c9)

### observed_connections-005972

```text
(config-if-srv)# no service-policy output <string> <cr>
```

Handler ` RVA 0xC005050 `；selector ` 1 `；EOL ` RVA 0x3396DE30 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` output Policy-map name。

[条件 C-2cb5a180716b2b49](../../evidence/conditions-sets-018.md#c-2cb5a180716b2b49) · [参数 P-35f3ac45dcb03036](../../evidence/parameters-sets-005.md#p-35f3ac45dcb03036) · [状态效果 S-7fcbb978a99cf1c9](../../evidence/state_effects-sets-027.md#s-7fcbb978a99cf1c9)

### observed_connections-005923

```text
(config-if-srv)# no shutdown <cr>
```

Handler ` RVA 0xC00ACA0 `；selector ` 27 `；EOL ` RVA 0x33968178 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f73fc5afc58e2a53](../../evidence/conditions-sets-095.md#c-f73fc5afc58e2a53) · [状态效果 S-7fcbb978a99cf1c9](../../evidence/state_effects-sets-027.md#s-7fcbb978a99cf1c9)

### observed_connections-005966

```text
(config-if-srv)# no snmp ifindex clear <cr>
```

Handler ` RVA 0xC00ACA0 `；selector ` 35 `；EOL ` RVA 0x33969118 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c0861e8690883c89](../../evidence/conditions-sets-074.md#c-c0861e8690883c89) · [状态效果 S-7fcbb978a99cf1c9](../../evidence/state_effects-sets-027.md#s-7fcbb978a99cf1c9)

### observed_connections-005964

```text
(config-if-srv)# no snmp ifindex persist <cr>
```

Handler ` RVA 0xC00ACA0 `；selector ` 34 `；EOL ` RVA 0x33968E70 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c0861e8690883c89](../../evidence/conditions-sets-074.md#c-c0861e8690883c89) · [状态效果 S-7fcbb978a99cf1c9](../../evidence/state_effects-sets-027.md#s-7fcbb978a99cf1c9)

### observed_connections-005962

```text
(config-if-srv)# no snmp trap link-status <cr>
```

Handler ` RVA 0xC00ACA0 `；selector ` 33 `；EOL ` RVA 0x33968BA0 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c0861e8690883c89](../../evidence/conditions-sets-074.md#c-c0861e8690883c89) · [状态效果 S-7fcbb978a99cf1c9](../../evidence/state_effects-sets-027.md#s-7fcbb978a99cf1c9)

### observed_connections-005981

```text
(config-if-srv)# no storm-control action shutdown <cr>
```

Handler ` RVA 0xC069820 `；selector ` 0 `；EOL ` RVA 0x3398CC48 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4b565d085ab24399](../../evidence/conditions-sets-030.md#c-4b565d085ab24399) · [状态效果 S-512f718503ad5a45](../../evidence/state_effects-sets-018.md#s-512f718503ad5a45)

### observed_connections-005926

```text
(config-if-srv)# no track <cr>
```

Handler ` RVA 0xC00ACA0 `；selector ` 28 `；EOL ` RVA 0x339684D8 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0d888176abde9aae](../../evidence/conditions-sets-005.md#c-0d888176abde9aae) · [状态效果 S-7fcbb978a99cf1c9](../../evidence/state_effects-sets-027.md#s-7fcbb978a99cf1c9)

### observed_connections-005937

```text
(config-if-srv)# no transparent-cfm <cr>
```

Handler ` RVA 0xBEB3720 `；selector ` 0 `；EOL ` RVA 0x3391EA18 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-702ec7acce632527](../../evidence/conditions-sets-043.md#c-702ec7acce632527) · [状态效果 S-7fcbb978a99cf1c9](../../evidence/state_effects-sets-027.md#s-7fcbb978a99cf1c9)

### observed_connections-005939

```text
(config-if-srv)# no untagged-cfm <cr>
```

Handler ` RVA 0xBEB3A70 `；selector ` 0 `；EOL ` RVA 0x3391ECD0 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-702ec7acce632527](../../evidence/conditions-sets-043.md#c-702ec7acce632527) · [状态效果 S-7fcbb978a99cf1c9](../../evidence/state_effects-sets-027.md#s-7fcbb978a99cf1c9)

### observed_connections-005925

```text
(config-if-srv)# no weight <cr>
```

Handler ` RVA 0xC00ACA0 `；selector ` 26 `；EOL ` RVA 0x33967E78 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-50111413e3af640a](../../evidence/conditions-sets-031.md#c-50111413e3af640a) · [状态效果 S-7fcbb978a99cf1c9](../../evidence/state_effects-sets-027.md#s-7fcbb978a99cf1c9)

### observed_connections-006007

```text
(config-if-srv)# rewrite ingress tag pop 1 <cr>
```

Handler ` RVA 0xC008380 `；selector ` 3 `；EOL ` RVA 0x3396D478 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-943ae9fa73edd571](../../evidence/conditions-sets-057.md#c-943ae9fa73edd571) · [状态效果 S-2c68010c460b797a](../../evidence/state_effects-sets-010.md#s-2c68010c460b797a)

### observed_connections-006008

```text
(config-if-srv)# rewrite ingress tag pop 1 <cr>
```

Handler ` RVA 0xC008380 `；selector ` 4 `；EOL ` RVA 0x3396D6F8 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-228b6bc446981b16](../../evidence/conditions-sets-014.md#c-228b6bc446981b16) · [状态效果 S-2c68010c460b797a](../../evidence/state_effects-sets-010.md#s-2c68010c460b797a)

### observed_connections-005945

```text
(config-if-srv)# service-policy input <string> <cr>
```

Handler ` RVA 0xC005050 `；selector ` 0 `；EOL ` RVA 0x3396DB38 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` input Policy-map name。

[条件 C-2cb5a180716b2b49](../../evidence/conditions-sets-018.md#c-2cb5a180716b2b49) · [参数 P-e2119ec8f663638b](../../evidence/parameters-sets-017.md#p-e2119ec8f663638b)

### observed_connections-005950

```text
(config-if-srv)# service-policy output <string> <cr>
```

Handler ` RVA 0xC005050 `；selector ` 1 `；EOL ` RVA 0x3396DE30 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` output Policy-map name。

[条件 C-2cb5a180716b2b49](../../evidence/conditions-sets-018.md#c-2cb5a180716b2b49) · [参数 P-35f3ac45dcb03036](../../evidence/parameters-sets-005.md#p-35f3ac45dcb03036)

### observed_connections-005918

```text
(config-if-srv)# shutdown <cr>
```

Handler ` RVA 0xC00ACA0 `；selector ` 27 `；EOL ` RVA 0x33968178 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f73fc5afc58e2a53](../../evidence/conditions-sets-095.md#c-f73fc5afc58e2a53)

### observed_connections-005943

```text
(config-if-srv)# snmp ifindex clear <cr>
```

Handler ` RVA 0xC00ACA0 `；selector ` 35 `；EOL ` RVA 0x33969118 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c0861e8690883c89](../../evidence/conditions-sets-074.md#c-c0861e8690883c89)

### observed_connections-005942

```text
(config-if-srv)# snmp ifindex persist <cr>
```

Handler ` RVA 0xC00ACA0 `；selector ` 34 `；EOL ` RVA 0x33968E70 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c0861e8690883c89](../../evidence/conditions-sets-074.md#c-c0861e8690883c89)

### observed_connections-005941

```text
(config-if-srv)# snmp trap link-status <cr>
```

Handler ` RVA 0xC00ACA0 `；selector ` 33 `；EOL ` RVA 0x33968BA0 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c0861e8690883c89](../../evidence/conditions-sets-074.md#c-c0861e8690883c89)

### observed_connections-005958

```text
(config-if-srv)# storm-control action shutdown <cr>
```

Handler ` RVA 0xC069820 `；selector ` 0 `；EOL ` RVA 0x3398CC48 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4b565d085ab24399](../../evidence/conditions-sets-030.md#c-4b565d085ab24399) · [状态效果 S-1bad276c4f6a14a3](../../evidence/state_effects-sets-006.md#s-1bad276c4f6a14a3)

### observed_connections-006036

```text
(config-if-srv)# storm-control unicast cir <?general_to_number_func_action@555588ee10a0> <cr>
```

Handler ` RVA 0xC069820 `；selector ` 0 `；EOL ` RVA 0x3398CC48 `。

模式根 ` RVA 0x33967928 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-81e4e72d927af137](../../evidence/conditions-sets-050.md#c-81e4e72d927af137) · [缺口 G-0787c61e0cde9f17](../../evidence/gaps-sets-001.md#g-0787c61e0cde9f17) · [状态效果 S-e9d4e5737149ddcc](../../evidence/state_effects-sets-049.md#s-e9d4e5737149ddcc)

### observed_connections-005928

```text
(config-if-srv)# track <number:1..32767> <cr>
```

Handler ` RVA 0xC00ACA0 `；selector ` 28 `；EOL ` RVA 0x339684D8 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Track object number。

[条件 C-8a62d9f85b828848](../../evidence/conditions-sets-054.md#c-8a62d9f85b828848) · [参数 P-8b45b58c3012324e](../../evidence/parameters-sets-011.md#p-8b45b58c3012324e)

### observed_connections-005919

```text
(config-if-srv)# transparent-cfm <cr>
```

Handler ` RVA 0xBEB3720 `；selector ` 0 `；EOL ` RVA 0x3391EA18 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-702ec7acce632527](../../evidence/conditions-sets-043.md#c-702ec7acce632527)

### observed_connections-005920

```text
(config-if-srv)# untagged-cfm <cr>
```

Handler ` RVA 0xBEB3A70 `；selector ` 0 `；EOL ` RVA 0x3391ECD0 `。

模式根 ` RVA 0x33967928 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-702ec7acce632527](../../evidence/conditions-sets-043.md#c-702ec7acce632527)

### observed_connections-006028

```text
(config-if-srv)# weight <number:dynamic> <cr>
```

Handler ` RVA 0xC00ACA0 `；selector ` 26 `；EOL ` RVA 0x33967E78 `。

模式根 ` RVA 0x33967928 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Weight value。

[条件 C-204e4d54b83a5e72](../../evidence/conditions-sets-013.md#c-204e4d54b83a5e72) · [缺口 G-183b04a56f43cf5e](../../evidence/gaps-sets-001.md#g-183b04a56f43cf5e) · [参数 P-d1d965eed46776c3](../../evidence/parameters-sets-016.md#p-d1d965eed46776c3)
