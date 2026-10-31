# scope-address-family · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-001705

```text
(config-router-scope-af)# aggregate-address <address> <address> <cr>
```

Handler ` RVA 0xF1B7BE0 `；selector ` 0 `；EOL ` RVA 0x34552F40 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Aggregate address；` address ` Aggregate mask。

[条件 C-f7ab9ff3c35afc8e](../../evidence/conditions-sets-096.md#c-f7ab9ff3c35afc8e) · [参数 P-9fe0ddf3e4cc9517](../../evidence/parameters-sets-012.md#p-9fe0ddf3e4cc9517)

### observed_connections-001545

```text
(config-router-scope-af)# auto-summary <cr>
```

Handler ` RVA 0xE1FA6B0 `；selector ` 0 `；EOL ` RVA 0x344F7B28 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-892cb3702bd56b94](../../evidence/conditions-sets-053.md#c-892cb3702bd56b94)

### observed_connections-001674

```text
(config-router-scope-af)# bgp additional-paths install <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 69 `；EOL ` RVA 0x3454A798 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8586360bd6d1b906](../../evidence/conditions-sets-052.md#c-8586360bd6d1b906) · [状态效果 S-04ed00a751b1d9c6](../../evidence/state_effects-sets-001.md#s-04ed00a751b1d9c6)

### observed_connections-001696

```text
(config-router-scope-af)# bgp additional-paths select <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 71 `；EOL ` RVA 0x3454A440 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0982d1ddadb45b04](../../evidence/conditions-sets-004.md#c-0982d1ddadb45b04)

### observed_connections-001585

```text
(config-router-scope-af)# bgp advertise-best-external <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 70 `；EOL ` RVA 0x3454B5E8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-57bb992185c04f5b](../../evidence/conditions-sets-034.md#c-57bb992185c04f5b)

### observed_connections-001607

```text
(config-router-scope-af)# bgp advertisement startup-delay <number:1..3600> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 95 `；EOL ` RVA 0x34543458 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` value (seconds)。

[条件 C-8085e5e4da124cf9](../../evidence/conditions-sets-050.md#c-8085e5e4da124cf9) · [参数 P-1ae39d27f31fcce5](../../evidence/parameters-sets-003.md#p-1ae39d27f31fcce5)

### observed_connections-001697

```text
(config-router-scope-af)# bgp aggregate-timer <number:6..60> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 58 `；EOL ` RVA 0x34551638 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timer interval。

[条件 C-e75e44fc50bad466](../../evidence/conditions-sets-089.md#c-e75e44fc50bad466) · [参数 P-2e3330fde6070f01](../../evidence/parameters-sets-004.md#p-2e3330fde6070f01)

### observed_connections-001619

```text
(config-router-scope-af)# bgp aigp-rib-metric <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 91 `；EOL ` RVA 0x34547ED8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f311201ce1b8ec9e](../../evidence/conditions-sets-094.md#c-f311201ce1b8ec9e)

### observed_connections-001581

```text
(config-router-scope-af)# bgp always-compare-med <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 5 `；EOL ` RVA 0x3453ED40 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d038dabf7ea3a128](../../evidence/conditions-sets-080.md#c-d038dabf7ea3a128)

### observed_connections-001661

```text
(config-router-scope-af)# bgp asnotation dot <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 64 `；EOL ` RVA 0x3453F050 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d038dabf7ea3a128](../../evidence/conditions-sets-080.md#c-d038dabf7ea3a128)

### observed_connections-001834

```text
(config-router-scope-af)# bgp bestpath aigp ignore <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 43 `；EOL ` RVA 0x34546C00 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d1964220dc649b09](../../evidence/conditions-sets-081.md#c-d1964220dc649b09)

### observed_connections-001828

```text
(config-router-scope-af)# bgp bestpath as-path ignore <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 17 `；EOL ` RVA 0x34546370 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f311201ce1b8ec9e](../../evidence/conditions-sets-094.md#c-f311201ce1b8ec9e)

### observed_connections-001830

```text
(config-router-scope-af)# bgp bestpath as-path multipath-relax <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 51 `；EOL ` RVA 0x34546618 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f311201ce1b8ec9e](../../evidence/conditions-sets-094.md#c-f311201ce1b8ec9e)

### observed_connections-001741

```text
(config-router-scope-af)# bgp bestpath compare-routerid <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 24 `；EOL ` RVA 0x345468B0 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f311201ce1b8ec9e](../../evidence/conditions-sets-094.md#c-f311201ce1b8ec9e)

### observed_connections-001833

```text
(config-router-scope-af)# bgp bestpath cost-community ignore <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 41 `；EOL ` RVA 0x34546ED8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f311201ce1b8ec9e](../../evidence/conditions-sets-094.md#c-f311201ce1b8ec9e)

### observed_connections-001775

```text
(config-router-scope-af)# bgp bestpath igp-metric ignore <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 42 `；EOL ` RVA 0x3454ACC8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9eb32499553e628d](../../evidence/conditions-sets-061.md#c-9eb32499553e628d)

### observed_connections-001831

```text
(config-router-scope-af)# bgp bestpath med missing-as-worst <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 18 `；EOL ` RVA 0x34546060 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f311201ce1b8ec9e](../../evidence/conditions-sets-094.md#c-f311201ce1b8ec9e) · [状态效果 S-2f2bb73e19fe250a](../../evidence/state_effects-sets-010.md#s-2f2bb73e19fe250a)

### observed_connections-001783

```text
(config-router-scope-af)# bgp bestpath prefix-validate allow-invalid <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 78 `；EOL ` RVA 0x3454AFD8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6111a0a7e8a7ea86](../../evidence/conditions-sets-038.md#c-6111a0a7e8a7ea86)

### observed_connections-001789

```text
(config-router-scope-af)# bgp bestpath prefix-validate disable <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 77 `；EOL ` RVA 0x3454B280 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6111a0a7e8a7ea86](../../evidence/conditions-sets-038.md#c-6111a0a7e8a7ea86)

### observed_connections-001682

```text
(config-router-scope-af)# bgp client-to-client reflection <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 9 `；EOL ` RVA 0x3453FEE0 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c76e7c8e33177186](../../evidence/conditions-sets-077.md#c-c76e7c8e33177186) · [状态效果 S-69e446c1d88bcd0a](../../evidence/state_effects-sets-023.md#s-69e446c1d88bcd0a)

### observed_connections-002003

```text
(config-router-scope-af)# bgp client-to-client reflection intra-cluster cluster-id <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 9 `；EOL ` RVA 0x3453FEE0 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d0b9dafc6b791a9e](../../evidence/conditions-sets-080.md#c-d0b9dafc6b791a9e) · [缺口 G-9616791a01b03a5f](../../evidence/gaps-sets-005.md#g-9616791a01b03a5f) · [状态效果 S-0c8985c3a4de2b96](../../evidence/state_effects-sets-003.md#s-0c8985c3a4de2b96)

### observed_connections-001679

```text
(config-router-scope-af)# bgp cluster-id <number:1..4294967294> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 7 `；EOL ` RVA 0x3453FAA8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Route-Reflector Cluster-id as 32 bit quantity。

[条件 C-4241334bd8d5bf0a](../../evidence/conditions-sets-026.md#c-4241334bd8d5bf0a) · [参数 P-7164e0959f79f2cd](../../evidence/parameters-sets-009.md#p-7164e0959f79f2cd)

### observed_connections-001988

```text
(config-router-scope-af)# bgp confederation identifier <?bgp_as4_action@555589a94db0> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 6 `；EOL ` RVA 0x34540DE8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d038dabf7ea3a128](../../evidence/conditions-sets-080.md#c-d038dabf7ea3a128) · [缺口 G-5994d454ce325f15](../../evidence/gaps-sets-004.md#g-5994d454ce325f15)

### observed_connections-001989

```text
(config-router-scope-af)# bgp confederation peers <?bgp_as4_action@555589a95120> <cr>
```

Handler ` RVA 0xF1C67F0 `；selector ` 0 `；EOL ` RVA 0x34541260 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6b1c562e633733d3](../../evidence/conditions-sets-041.md#c-6b1c562e633733d3) · [缺口 G-5f901783163481cd](../../evidence/gaps-sets-004.md#g-5f901783163481cd) · [状态效果 S-fcd1414342f223b7](../../evidence/state_effects-sets-054.md#s-fcd1414342f223b7)

### observed_connections-001700

```text
(config-router-scope-af)# bgp consistency-checker error-message <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 3 `；EOL ` RVA 0x3453F428 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3ee5c1c524e1d7b0](../../evidence/conditions-sets-024.md#c-3ee5c1c524e1d7b0) · [状态效果 S-ce60b0b5c4c6bbdc](../../evidence/state_effects-sets-044.md#s-ce60b0b5c4c6bbdc)

### observed_connections-001687

```text
(config-router-scope-af)# bgp consistency-checker error-message interval <number:5..1440> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 3 `；EOL ` RVA 0x3453F450 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Interval (minutes)。

[条件 C-002f26a219c00caa](../../evidence/conditions-sets-001.md#c-002f26a219c00caa) · [参数 P-68b3104b719d414f](../../evidence/parameters-sets-008.md#p-68b3104b719d414f) · [状态效果 S-ce60b0b5c4c6bbdc](../../evidence/state_effects-sets-044.md#s-ce60b0b5c4c6bbdc)

### observed_connections-001588

```text
(config-router-scope-af)# bgp dampening <cr>
```

Handler ` RVA 0xF1B85B0 `；selector ` 0 `；EOL ` RVA 0x34549860 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c539de778f448c6d](../../evidence/conditions-sets-076.md#c-c539de778f448c6d)

### observed_connections-001779

```text
(config-router-scope-af)# bgp dampening route-map <string> <cr>
```

Handler ` RVA 0xF1B85B0 `；selector ` 8 `；EOL ` RVA 0x34549A28 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` route-map name。

[条件 C-ca8c34c69012573b](../../evidence/conditions-sets-078.md#c-ca8c34c69012573b) · [参数 P-59832b8c359da52a](../../evidence/parameters-sets-007.md#p-59832b8c359da52a)

### observed_connections-001776

```text
(config-router-scope-af)# bgp default inter-as-hybrid advertise-source-routes <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 57 `；EOL ` RVA 0x34548E98 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ec6dfe448cb8b3b0](../../evidence/conditions-sets-091.md#c-ec6dfe448cb8b3b0)

### observed_connections-001643

```text
(config-router-scope-af)# bgp default ipv4-unicast <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 19 `；EOL ` RVA 0x345485F0 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad3543d5e8c8e02b](../../evidence/conditions-sets-067.md#c-ad3543d5e8c8e02b)

### observed_connections-001649

```text
(config-router-scope-af)# bgp default ipv6-nexthop <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 75 `；EOL ` RVA 0x345488E8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4cf911d362de1ddd](../../evidence/conditions-sets-030.md#c-4cf911d362de1ddd)

### observed_connections-001582

```text
(config-router-scope-af)# bgp default local-preference <number:0..4294967295> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 0 `；EOL ` RVA 0x34548B78 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Configure default local preference value。

[条件 C-30664b0a06aa0bdb](../../evidence/conditions-sets-019.md#c-30664b0a06aa0bdb) · [参数 P-9c57d57f1e570b0d](../../evidence/parameters-sets-012.md#p-9c57d57f1e570b0d)

### observed_connections-001771

```text
(config-router-scope-af)# bgp default route-target filter <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 25 `；EOL ` RVA 0x34549200 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-65e0de238ef95f31](../../evidence/conditions-sets-039.md#c-65e0de238ef95f31)

### observed_connections-001772

```text
(config-router-scope-af)# bgp default route-target filter <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 25 `；EOL ` RVA 0x345494A0 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0fb94622c94e5967](../../evidence/conditions-sets-006.md#c-0fb94622c94e5967)

### observed_connections-001597

```text
(config-router-scope-af)# bgp deterministic-med <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 10 `；EOL ` RVA 0x34541560 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d038dabf7ea3a128](../../evidence/conditions-sets-080.md#c-d038dabf7ea3a128)

### observed_connections-001592

```text
(config-router-scope-af)# bgp dmzlink-bw <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 31 `；EOL ` RVA 0x3454CB98 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e60672eeace3f616](../../evidence/conditions-sets-089.md#c-e60672eeace3f616)

### observed_connections-001544

```text
(config-router-scope-af)# bgp dynamic-med-interval <number:60..4294967295> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 21 `；EOL ` RVA 0x34541588 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Interval value (seconds)。

[条件 C-fee7abd2d50f1292](../../evidence/conditions-sets-098.md#c-fee7abd2d50f1292) · [参数 P-b84805645c6b61f1](../../evidence/parameters-sets-014.md#p-b84805645c6b61f1)

### observed_connections-001593

```text
(config-router-scope-af)# bgp enforce-first-as <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 20 `；EOL ` RVA 0x34540790 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d038dabf7ea3a128](../../evidence/conditions-sets-080.md#c-d038dabf7ea3a128)

### observed_connections-001613

```text
(config-router-scope-af)# bgp enhanced-error <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 82 `；EOL ` RVA 0x345431D0 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-955c985d0afc3030](../../evidence/conditions-sets-058.md#c-955c985d0afc3030)

### observed_connections-001570

```text
(config-router-scope-af)# bgp fast-external-fallover <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 1 `；EOL ` RVA 0x3453E478 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d038dabf7ea3a128](../../evidence/conditions-sets-080.md#c-d038dabf7ea3a128)

### observed_connections-001618

```text
(config-router-scope-af)# bgp graceful-restart <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 35 `；EOL ` RVA 0x34544040 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d038dabf7ea3a128](../../evidence/conditions-sets-080.md#c-d038dabf7ea3a128)

### observed_connections-001615

```text
(config-router-scope-af)# bgp graceful-restart restart-time <number:1..3600> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 36 `；EOL ` RVA 0x34543A10 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Delay value (seconds)。

[条件 C-9a11879786d565ab](../../evidence/conditions-sets-060.md#c-9a11879786d565ab) · [参数 P-a11e205d94f83ef0](../../evidence/parameters-sets-012.md#p-a11e205d94f83ef0)

### observed_connections-001617

```text
(config-router-scope-af)# bgp graceful-restart stalepath-time <number:1..3600> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 37 `；EOL ` RVA 0x34543A78 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Delay value (seconds)。

[条件 C-55124de04c01fca4](../../evidence/conditions-sets-033.md#c-55124de04c01fca4) · [参数 P-a93ac316db3c47a6](../../evidence/parameters-sets-013.md#p-a93ac316db3c47a6)

### observed_connections-002009

```text
(config-router-scope-af)# bgp graceful-shutdown all vrfs <number:30..65535> community <?bgp_community_action@555589a98958> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 79 `；EOL ` RVA 0x345444A8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` time in seconds。

[条件 C-ccbdbdb85e5e9818](../../evidence/conditions-sets-079.md#c-ccbdbdb85e5e9818) · [缺口 G-3b227aa838a399dc](../../evidence/gaps-sets-003.md#g-3b227aa838a399dc) · [参数 P-1d04b102cfaba259](../../evidence/parameters-sets-003.md#p-1d04b102cfaba259) · [状态效果 S-f80b6f9e769971af](../../evidence/state_effects-sets-052.md#s-f80b6f9e769971af)

### observed_connections-001875

```text
(config-router-scope-af)# bgp graceful-shutdown all vrfs activate <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 79 `；EOL ` RVA 0x345444A8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-66f3816b6a249c29](../../evidence/conditions-sets-040.md#c-66f3816b6a249c29) · [状态效果 S-0088dd7468db8f8f](../../evidence/state_effects-sets-001.md#s-0088dd7468db8f8f)

### observed_connections-001868

```text
(config-router-scope-af)# bgp inject-map <string> exist-map <string> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 32 `；EOL ` RVA 0x3454E710 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` route-map name；` string ` route-map name。

[条件 C-f8673071a7ce23a7](../../evidence/conditions-sets-096.md#c-f8673071a7ce23a7) · [参数 P-72ba39e577f273d6](../../evidence/parameters-sets-009.md#p-72ba39e577f273d6)

### observed_connections-001769

```text
(config-router-scope-af)# bgp label-allocation-batch <number:0..4294967295> <number:0..4294967295> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 53 `；EOL ` RVA 0x3453E808 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timer value in milliseconds；` unsigned_number ` Batch Size。

[条件 C-d038dabf7ea3a128](../../evidence/conditions-sets-080.md#c-d038dabf7ea3a128) · [参数 P-675aa1ff414c4c13](../../evidence/parameters-sets-008.md#p-675aa1ff414c4c13)

### observed_connections-001801

```text
(config-router-scope-af)# bgp listen block <address> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 93 `；EOL ` RVA 0x3454C5A8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IPv4 Dynamic Peering Address。

[条件 C-88fc52820904d643](../../evidence/conditions-sets-053.md#c-88fc52820904d643) · [参数 P-d42b5fda11d4d375](../../evidence/parameters-sets-016.md#p-d42b5fda11d4d375)

### observed_connections-001812

```text
(config-router-scope-af)# bgp listen block <address> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 93 `；EOL ` RVA 0x34542508 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IPv4 Dynamic Peering Address。

[条件 C-9af955235c91b53a](../../evidence/conditions-sets-060.md#c-9af955235c91b53a) · [参数 P-3fcb738a2abc9e2d](../../evidence/parameters-sets-005.md#p-3fcb738a2abc9e2d)

### observed_connections-001596

```text
(config-router-scope-af)# bgp listen limit <number:1..10000> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 61 `；EOL ` RVA 0x3454C4F0 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` max number。

[条件 C-f8cd7ded6cd631ca](../../evidence/conditions-sets-096.md#c-f8cd7ded6cd631ca) · [参数 P-86dcee520cd741e9](../../evidence/parameters-sets-010.md#p-86dcee520cd741e9)

### observed_connections-001610

```text
(config-router-scope-af)# bgp listen limit <number:1..10000> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 61 `；EOL ` RVA 0x34542428 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` max number。

[条件 C-e44f38411de16df4](../../evidence/conditions-sets-088.md#c-e44f38411de16df4) · [参数 P-b9da6a27850b7e7c](../../evidence/parameters-sets-014.md#p-b9da6a27850b7e7c)

### observed_connections-001733

```text
(config-router-scope-af)# bgp listen persistent <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 94 `；EOL ` RVA 0x34542840 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9af955235c91b53a](../../evidence/conditions-sets-060.md#c-9af955235c91b53a)

### observed_connections-002008

```text
(config-router-scope-af)# bgp listen range <prefix:dynamic> peer-group <string> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 60 `；EOL ` RVA 0x34542080 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` IPv4 subnet range；` string ` peer-group name。

[条件 C-6cef626152e6105c](../../evidence/conditions-sets-042.md#c-6cef626152e6105c) · [缺口 G-c1447d811f6e6e21](../../evidence/gaps-sets-007.md#g-c1447d811f6e6e21) · [参数 P-19f225df6eab1fb7](../../evidence/parameters-sets-002.md#p-19f225df6eab1fb7)

### observed_connections-001594

```text
(config-router-scope-af)# bgp log-neighbor-changes <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 11 `；EOL ` RVA 0x34540A38 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d038dabf7ea3a128](../../evidence/conditions-sets-080.md#c-d038dabf7ea3a128)

### observed_connections-001754

```text
(config-router-scope-af)# bgp maxas-limit <number:1..254> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 26 `；EOL ` RVA 0x34547C50 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of ASes in the AS-PATH attribute(max 254)。

[条件 C-1c1d876d1e4937a9](../../evidence/conditions-sets-011.md#c-1c1d876d1e4937a9) · [参数 P-6207ef4dd6f5c2c7](../../evidence/parameters-sets-008.md#p-6207ef4dd6f5c2c7)

### observed_connections-001743

```text
(config-router-scope-af)# bgp maxcommunity-limit <number:1..1018> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 27 `；EOL ` RVA 0x34547260 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of communities in the COMMUNITY attribute。

[条件 C-304ca74779d22fed](../../evidence/conditions-sets-019.md#c-304ca74779d22fed) · [参数 P-1bb36e7dc4785ac6](../../evidence/parameters-sets-003.md#p-1bb36e7dc4785ac6)

### observed_connections-001750

```text
(config-router-scope-af)# bgp maxextcommunity-limit <number:1..509> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 29 `；EOL ` RVA 0x34547900 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of extended communities in the EXTENDED COMMUNITY attribute。

[条件 C-72b292d9b4572858](../../evidence/conditions-sets-044.md#c-72b292d9b4572858) · [参数 P-18b19054df736e67](../../evidence/parameters-sets-002.md#p-18b19054df736e67)

### observed_connections-001746

```text
(config-router-scope-af)# bgp maxlargecommunity-limit <number:1..339> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 28 `；EOL ` RVA 0x345475B0 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of large communities in the LARGE COMMUNITY attribute。

[条件 C-ae3ce536204d30b4](../../evidence/conditions-sets-067.md#c-ae3ce536204d30b4) · [参数 P-3d5c5e73bf1baa9f](../../evidence/parameters-sets-005.md#p-3d5c5e73bf1baa9f)

### observed_connections-001606

```text
(config-router-scope-af)# bgp mpls-local-label <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 81 `；EOL ` RVA 0x3454EA88 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8cfe7e0e372db70a](../../evidence/conditions-sets-055.md#c-8cfe7e0e372db70a)

### observed_connections-001804

```text
(config-router-scope-af)# bgp nexthop route-map <string> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 56 `；EOL ` RVA 0x3454D300 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` route-map name。

[条件 C-e7fae0a1d2b836dc](../../evidence/conditions-sets-090.md#c-e7fae0a1d2b836dc) · [参数 P-018cf62f945dd9fb](../../evidence/parameters-sets-001.md#p-018cf62f945dd9fb)

### observed_connections-001711

```text
(config-router-scope-af)# bgp nexthop trigger critical-delay <number:0..100> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 48 `；EOL ` RVA 0x3454D868 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Critical delay value (seconds)。

[条件 C-1d442c813c4e35a2](../../evidence/conditions-sets-011.md#c-1d442c813c4e35a2) · [参数 P-16ab074120228b36](../../evidence/parameters-sets-002.md#p-16ab074120228b36)

### observed_connections-001707

```text
(config-router-scope-af)# bgp nexthop trigger delay <number:0..100> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 47 `；EOL ` RVA 0x3454D5E8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Delay value (seconds)。

[条件 C-9de3c87b5a2847d7](../../evidence/conditions-sets-061.md#c-9de3c87b5a2847d7) · [参数 P-8c91de2d00abb365](../../evidence/parameters-sets-011.md#p-8c91de2d00abb365)

### observed_connections-001800

```text
(config-router-scope-af)# bgp nexthop trigger enable <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 49 `；EOL ` RVA 0x3454D5C0 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-71809c74616618a3](../../evidence/conditions-sets-044.md#c-71809c74616618a3)

### observed_connections-001811

```text
(config-router-scope-af)# bgp nopeerup-delay cold-boot <number:1..3600> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 74 `；EOL ` RVA 0x34542E68 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Delay in seconds。

[条件 C-a4057e89490d6056](../../evidence/conditions-sets-063.md#c-a4057e89490d6056) · [参数 P-06d763f31c291b7c](../../evidence/parameters-sets-001.md#p-06d763f31c291b7c) · [状态效果 S-69f69610e6b9ce89](../../evidence/state_effects-sets-023.md#s-69f69610e6b9ce89)

### observed_connections-001670

```text
(config-router-scope-af)# bgp recursion host <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 72 `；EOL ` RVA 0x3454B960 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d87b32e4fbe61c8b](../../evidence/conditions-sets-083.md#c-d87b32e4fbe61c8b)

### observed_connections-001586

```text
(config-router-scope-af)# bgp redistribute-internal <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 2 `；EOL ` RVA 0x3454FC88 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-af02a502302afa3f](../../evidence/conditions-sets-068.md#c-af02a502302afa3f)

### observed_connections-001825

```text
(config-router-scope-af)# bgp refresh max-eor-time <number:600..3600> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 16 `；EOL ` RVA 0x34545238 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timer interval (seconds)。

[条件 C-60224413d06eeeb9](../../evidence/conditions-sets-037.md#c-60224413d06eeeb9) · [参数 P-9a750bd667ac620c](../../evidence/parameters-sets-012.md#p-9a750bd667ac620c)

### observed_connections-001821

```text
(config-router-scope-af)# bgp refresh stalepath-time <number:600..3600> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 15 `；EOL ` RVA 0x34544EC8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timer interval (seconds)。

[条件 C-0e94deaaa5b8439c](../../evidence/conditions-sets-006.md#c-0e94deaaa5b8439c) · [参数 P-82df222e5c1b4adc](../../evidence/parameters-sets-010.md#p-82df222e5c1b4adc)

### observed_connections-001738

```text
(config-router-scope-af)# bgp regexp deterministic <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 44 `；EOL ` RVA 0x34545C50 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f311201ce1b8ec9e](../../evidence/conditions-sets-094.md#c-f311201ce1b8ec9e)

### observed_connections-001671

```text
(config-router-scope-af)# bgp route-map priority <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 59 `；EOL ` RVA 0x34550E18 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-11589918a9054012](../../evidence/conditions-sets-007.md#c-11589918a9054012)

### observed_connections-001578

```text
(config-router-scope-af)# bgp route-map-cache <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 34 `；EOL ` RVA 0x3453EA90 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d038dabf7ea3a128](../../evidence/conditions-sets-080.md#c-d038dabf7ea3a128)

### observed_connections-001669

```text
(config-router-scope-af)# bgp router-id <address> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 4 `；EOL ` RVA 0x3453DE48 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Manually configured router identifier。

[条件 C-d58eab91ac243e0d](../../evidence/conditions-sets-082.md#c-d58eab91ac243e0d) · [参数 P-dcb40423ba26ad8d](../../evidence/parameters-sets-017.md#p-dcb40423ba26ad8d)

### observed_connections-001703

```text
(config-router-scope-af)# bgp router-id auto-assign <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 4 `；EOL ` RVA 0x3454C010 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e28c35188f06b69c](../../evidence/conditions-sets-087.md#c-e28c35188f06b69c) · [状态效果 S-5865e20a41a27365](../../evidence/state_effects-sets-019.md#s-5865e20a41a27365)

### observed_connections-001986

```text
(config-router-scope-af)# bgp router-id interface <interface> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 4 `；EOL ` RVA 0x3453DE48 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-78577eab165298d8](../../evidence/conditions-sets-047.md#c-78577eab165298d8) · [缺口 G-89a10bccc96c14a6](../../evidence/gaps-sets-005.md#g-89a10bccc96c14a6) · [参数 P-30cec06ebc832bab](../../evidence/parameters-sets-004.md#p-30cec06ebc832bab)

### observed_connections-001987

```text
(config-router-scope-af)# bgp router-id interface <interface> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 4 `；EOL ` RVA 0x3454C010 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6b69898e36eba479](../../evidence/conditions-sets-042.md#c-6b69898e36eba479) · [缺口 G-d3a6a252eda34abe](../../evidence/gaps-sets-007.md#g-d3a6a252eda34abe) · [参数 P-e1449851398819da](../../evidence/parameters-sets-017.md#p-e1449851398819da)

### observed_connections-001903

```text
(config-router-scope-af)# bgp rpki server tcp <address> port <number:1..65535> refresh <number:1..65535> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 76 `；EOL ` RVA 0x34551C30 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IPv6 address of RPKI cache server；` unsigned_number ` Port number；` unsigned_number ` Refresh time in seconds。

[条件 C-dc3fc388f0c7095d](../../evidence/conditions-sets-085.md#c-dc3fc388f0c7095d) · [参数 P-6ddc8c613ed3413e](../../evidence/parameters-sets-009.md#p-6ddc8c613ed3413e)

### observed_connections-001712

```text
(config-router-scope-af)# bgp rr-group <string> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 23 `；EOL ` RVA 0x3454E2A8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Extended community-list name。

[条件 C-b43ee9ccd7abc162](../../evidence/conditions-sets-070.md#c-b43ee9ccd7abc162) · [参数 P-42b146a760d19083](../../evidence/parameters-sets-006.md#p-42b146a760d19083)

### observed_connections-001620

```text
(config-router-scope-af)# bgp safe-ebgp-policy <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 92 `；EOL ` RVA 0x345481E8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4123e929cf76e12f](../../evidence/conditions-sets-025.md#c-4123e929cf76e12f)

### observed_connections-001709

```text
(config-router-scope-af)# bgp scan-time <number:5..60> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 22 `；EOL ` RVA 0x3454DF38 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Scanner interval (seconds)。

[条件 C-5699db3668bbc500](../../evidence/conditions-sets-034.md#c-5699db3668bbc500) · [参数 P-8a5b54a14f207a55](../../evidence/parameters-sets-011.md#p-8a5b54a14f207a55)

### observed_connections-001677

```text
(config-router-scope-af)# bgp slow-peer detection <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 67 `；EOL ` RVA 0x3454EF58 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3908d3c47bafd420](../../evidence/conditions-sets-022.md#c-3908d3c47bafd420)

### observed_connections-001673

```text
(config-router-scope-af)# bgp slow-peer detection threshold <number:120..3600> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 67 `；EOL ` RVA 0x3454EF30 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Threshold value (seconds)。

[条件 C-6a169fde7a4ec9ab](../../evidence/conditions-sets-041.md#c-6a169fde7a4ec9ab) · [参数 P-f58f4a1603943441](../../evidence/parameters-sets-018.md#p-f58f4a1603943441)

### observed_connections-001794

```text
(config-router-scope-af)# bgp slow-peer split-update-group dynamic <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 68 `；EOL ` RVA 0x3454F528 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2b46341ff292d998](../../evidence/conditions-sets-017.md#c-2b46341ff292d998)

### observed_connections-001810

```text
(config-router-scope-af)# bgp snmp traps add-type <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 90 `；EOL ` RVA 0x34541B50 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d038dabf7ea3a128](../../evidence/conditions-sets-080.md#c-d038dabf7ea3a128)

### observed_connections-001595

```text
(config-router-scope-af)# bgp soft-reconfig-backup <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 52 `；EOL ` RVA 0x3454CEE8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-49d83a5d33e818c0](../../evidence/conditions-sets-029.md#c-49d83a5d33e818c0)

### observed_connections-001860

```text
(config-router-scope-af)# bgp sourced-paths per-net isis all <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 89 `；EOL ` RVA 0x34550A98 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6159d8ad545642ce](../../evidence/conditions-sets-038.md#c-6159d8ad545642ce) · [状态效果 S-11bc14f5f5d0139e](../../evidence/state_effects-sets-004.md#s-11bc14f5f5d0139e)

### observed_connections-001854

```text
(config-router-scope-af)# bgp sourced-paths per-net ospf all <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 87 `；EOL ` RVA 0x34550438 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6159d8ad545642ce](../../evidence/conditions-sets-038.md#c-6159d8ad545642ce) · [状态效果 S-41c90156a3bf8ab9](../../evidence/state_effects-sets-014.md#s-41c90156a3bf8ab9)

### observed_connections-001855

```text
(config-router-scope-af)# bgp sourced-paths per-net ospfv3 all <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 88 `；EOL ` RVA 0x34550780 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6159d8ad545642ce](../../evidence/conditions-sets-038.md#c-6159d8ad545642ce) · [状态效果 S-44c3ff3487b15629](../../evidence/state_effects-sets-015.md#s-44c3ff3487b15629)

### observed_connections-001851

```text
(config-router-scope-af)# bgp sourced-paths per-net static all <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 86 `；EOL ` RVA 0x345500F0 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6159d8ad545642ce](../../evidence/conditions-sets-038.md#c-6159d8ad545642ce) · [状态效果 S-01683be9314eea66](../../evidence/state_effects-sets-001.md#s-01683be9314eea66)

### observed_connections-001734

```text
(config-router-scope-af)# bgp sso route-refresh-enable <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 38 `；EOL ` RVA 0x34544B08 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f311201ce1b8ec9e](../../evidence/conditions-sets-094.md#c-f311201ce1b8ec9e)

### observed_connections-001590

```text
(config-router-scope-af)# bgp suppress-inactive <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 45 `；EOL ` RVA 0x3454BC60 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a18c8bfcf986468c](../../evidence/conditions-sets-062.md#c-a18c8bfcf986468c)

### observed_connections-001534

```text
(config-router-scope-af)# bgp tid <number:1..255> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 55 `；EOL ` RVA 0x3453D688 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Tolology identifier value。

[条件 C-3a3ff49b9b4b4655](../../evidence/conditions-sets-023.md#c-3a3ff49b9b4b4655) · [参数 P-05e8d95ab14e5a02](../../evidence/parameters-sets-001.md#p-05e8d95ab14e5a02)

### observed_connections-001678

```text
(config-router-scope-af)# bgp transport path-mtu-discovery <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 50 `；EOL ` RVA 0x34540500 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d038dabf7ea3a128](../../evidence/conditions-sets-080.md#c-d038dabf7ea3a128)

### observed_connections-001546

```text
(config-router-scope-af)# bgp update-delay <number:1..3600> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 30 `；EOL ` RVA 0x34543480 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Delay value (seconds)。

[条件 C-fb8bffe97d65509f](../../evidence/conditions-sets-097.md#c-fb8bffe97d65509f) · [参数 P-208d953f8f3256be](../../evidence/parameters-sets-003.md#p-208d953f8f3256be)

### observed_connections-001778

```text
(config-router-scope-af)# bgp update-group split as-override <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 73 `；EOL ` RVA 0x3454F8F8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1f2cd0608d0fe1e4](../../evidence/conditions-sets-012.md#c-1f2cd0608d0fe1e4)

### observed_connections-001575

```text
(config-router-scope-af)# bgp upgrade-cli <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 33 `；EOL ` RVA 0x3453DAA0 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-99a615dc14da7261](../../evidence/conditions-sets-059.md#c-99a615dc14da7261)

### observed_connections-001857

```text
(config-router-scope-af)# bgp va <address> mask <address> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 80 `；EOL ` RVA 0x345511C0 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` BGP VA ip address；` address ` BGP VA mask address。

[条件 C-ca1b796c0cbc6cf3](../../evidence/conditions-sets-078.md#c-ca1b796c0cbc6cf3) · [参数 P-463fadf5bebfec05](../../evidence/parameters-sets-006.md#p-463fadf5bebfec05)

### observed_connections-001736

```text
(config-router-scope-af)# bgp vrf-update-optimisation off <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 66 `；EOL ` RVA 0x345455C0 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f311201ce1b8ec9e](../../evidence/conditions-sets-094.md#c-f311201ce1b8ec9e)

### observed_connections-001827

```text
(config-router-scope-af)# bgp write-limit <number:500..2147483647> <number:500..2147483647> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 40 `；EOL ` RVA 0x34545918 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of messages to be formatted per neighbor/peergroup；` unsigned_number ` Number of messages that can be enqueued in total。

[条件 C-0b7ddf1a3096eee1](../../evidence/conditions-sets-005.md#c-0b7ddf1a3096eee1) · [参数 P-59b6e726ec98b8a8](../../evidence/parameters-sets-007.md#p-59b6e726ec98b8a8)

### observed_connections-001553

```text
(config-router-scope-af)# context <string> <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 0 `；EOL ` RVA 0x33C44A60 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` SNMP Context Name。

[条件 C-9affa1869574e86e](../../evidence/conditions-sets-060.md#c-9affa1869574e86e) · [参数 P-f3e465802edc027f](../../evidence/parameters-sets-018.md#p-f3e465802edc027f) · [状态效果 S-355a44aeb0ea4c7f](../../evidence/state_effects-sets-012.md#s-355a44aeb0ea4c7f)

### observed_connections-001803

```text
(config-router-scope-af)# default aggregate-address <address> <address> <cr>
```

Handler ` RVA 0xF1B7BE0 `；selector ` 0 `；EOL ` RVA 0x34552F40 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` Aggregate address；` address ` Aggregate mask。

[条件 C-f7ab9ff3c35afc8e](../../evidence/conditions-sets-096.md#c-f7ab9ff3c35afc8e) · [参数 P-9fe0ddf3e4cc9517](../../evidence/parameters-sets-012.md#p-9fe0ddf3e4cc9517) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001602

```text
(config-router-scope-af)# default auto-summary <cr>
```

Handler ` RVA 0xE1FA6B0 `；selector ` 0 `；EOL ` RVA 0x344F7B28 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-892cb3702bd56b94](../../evidence/conditions-sets-053.md#c-892cb3702bd56b94) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001790

```text
(config-router-scope-af)# default bgp additional-paths install <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 69 `；EOL ` RVA 0x3454A798 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8586360bd6d1b906](../../evidence/conditions-sets-052.md#c-8586360bd6d1b906) · [状态效果 S-5f46d3f624730c5e](../../evidence/state_effects-sets-020.md#s-5f46d3f624730c5e)

### observed_connections-001797

```text
(config-router-scope-af)# default bgp additional-paths select <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 71 `；EOL ` RVA 0x3454A440 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0982d1ddadb45b04](../../evidence/conditions-sets-004.md#c-0982d1ddadb45b04) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001666

```text
(config-router-scope-af)# default bgp advertise-best-external <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 70 `；EOL ` RVA 0x3454B5E8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-57bb992185c04f5b](../../evidence/conditions-sets-034.md#c-57bb992185c04f5b) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001718

```text
(config-router-scope-af)# default bgp advertisement startup-delay <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 95 `；EOL ` RVA 0x34543458 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a4b6ac0490741a56](../../evidence/conditions-sets-063.md#c-a4b6ac0490741a56) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001798

```text
(config-router-scope-af)# default bgp aggregate-timer <number:6..60> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 58 `；EOL ` RVA 0x34551638 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Timer interval。

[条件 C-e75e44fc50bad466](../../evidence/conditions-sets-089.md#c-e75e44fc50bad466) · [参数 P-2e3330fde6070f01](../../evidence/parameters-sets-004.md#p-2e3330fde6070f01) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001751

```text
(config-router-scope-af)# default bgp aigp-rib-metric <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 91 `；EOL ` RVA 0x34547ED8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f311201ce1b8ec9e](../../evidence/conditions-sets-094.md#c-f311201ce1b8ec9e) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001656

```text
(config-router-scope-af)# default bgp always-compare-med <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 5 `；EOL ` RVA 0x3453ED40 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d038dabf7ea3a128](../../evidence/conditions-sets-080.md#c-d038dabf7ea3a128) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001777

```text
(config-router-scope-af)# default bgp asnotation dot <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 64 `；EOL ` RVA 0x3453F050 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d038dabf7ea3a128](../../evidence/conditions-sets-080.md#c-d038dabf7ea3a128) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001885

```text
(config-router-scope-af)# default bgp bestpath aigp ignore <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 43 `；EOL ` RVA 0x34546C00 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d1964220dc649b09](../../evidence/conditions-sets-081.md#c-d1964220dc649b09) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001877

```text
(config-router-scope-af)# default bgp bestpath as-path ignore <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 17 `；EOL ` RVA 0x34546370 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f311201ce1b8ec9e](../../evidence/conditions-sets-094.md#c-f311201ce1b8ec9e) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001880

```text
(config-router-scope-af)# default bgp bestpath as-path multipath-relax <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 51 `；EOL ` RVA 0x34546618 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f311201ce1b8ec9e](../../evidence/conditions-sets-094.md#c-f311201ce1b8ec9e) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001832

```text
(config-router-scope-af)# default bgp bestpath compare-routerid <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 24 `；EOL ` RVA 0x345468B0 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f311201ce1b8ec9e](../../evidence/conditions-sets-094.md#c-f311201ce1b8ec9e) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001884

```text
(config-router-scope-af)# default bgp bestpath cost-community ignore <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 41 `；EOL ` RVA 0x34546ED8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f311201ce1b8ec9e](../../evidence/conditions-sets-094.md#c-f311201ce1b8ec9e) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001843

```text
(config-router-scope-af)# default bgp bestpath igp-metric ignore <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 42 `；EOL ` RVA 0x3454ACC8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9eb32499553e628d](../../evidence/conditions-sets-061.md#c-9eb32499553e628d) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001881

```text
(config-router-scope-af)# default bgp bestpath med missing-as-worst <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 18 `；EOL ` RVA 0x34546060 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f311201ce1b8ec9e](../../evidence/conditions-sets-094.md#c-f311201ce1b8ec9e) · [状态效果 S-8c9743e50e647fa7](../../evidence/state_effects-sets-030.md#s-8c9743e50e647fa7)

### observed_connections-001848

```text
(config-router-scope-af)# default bgp bestpath prefix-validate allow-invalid <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 78 `；EOL ` RVA 0x3454AFD8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6111a0a7e8a7ea86](../../evidence/conditions-sets-038.md#c-6111a0a7e8a7ea86) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001852

```text
(config-router-scope-af)# default bgp bestpath prefix-validate disable <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 77 `；EOL ` RVA 0x3454B280 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6111a0a7e8a7ea86](../../evidence/conditions-sets-038.md#c-6111a0a7e8a7ea86) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001793

```text
(config-router-scope-af)# default bgp client-to-client reflection <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 9 `；EOL ` RVA 0x3453FEE0 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c76e7c8e33177186](../../evidence/conditions-sets-077.md#c-c76e7c8e33177186) · [状态效果 S-1a7f2a6b7625ca41](../../evidence/state_effects-sets-006.md#s-1a7f2a6b7625ca41)

### observed_connections-001685

```text
(config-router-scope-af)# default bgp cluster-id <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 7 `；EOL ` RVA 0x3453FAA8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d71d23f47cf3fd0b](../../evidence/conditions-sets-083.md#c-d71d23f47cf3fd0b) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001694

```text
(config-router-scope-af)# default bgp consistency-checker <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 3 `；EOL ` RVA 0x3453F428 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d44cb6b6900bc63e](../../evidence/conditions-sets-082.md#c-d44cb6b6900bc63e) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001657

```text
(config-router-scope-af)# default bgp dampening <cr>
```

Handler ` RVA 0xF1B85B0 `；selector ` 0 `；EOL ` RVA 0x34549860 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9b0c31630ef8201a](../../evidence/conditions-sets-060.md#c-9b0c31630ef8201a) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001845

```text
(config-router-scope-af)# default bgp default inter-as-hybrid advertise-source-routes <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 57 `；EOL ` RVA 0x34548E98 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ec6dfe448cb8b3b0](../../evidence/conditions-sets-091.md#c-ec6dfe448cb8b3b0) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001766

```text
(config-router-scope-af)# default bgp default ipv4-unicast <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 19 `；EOL ` RVA 0x345485F0 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad3543d5e8c8e02b](../../evidence/conditions-sets-067.md#c-ad3543d5e8c8e02b) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001770

```text
(config-router-scope-af)# default bgp default ipv6-nexthop <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 75 `；EOL ` RVA 0x345488E8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4cf911d362de1ddd](../../evidence/conditions-sets-030.md#c-4cf911d362de1ddd) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001659

```text
(config-router-scope-af)# default bgp default local-preference <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 0 `；EOL ` RVA 0x34548B78 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1d4792eedfd8b981](../../evidence/conditions-sets-011.md#c-1d4792eedfd8b981) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001839

```text
(config-router-scope-af)# default bgp default route-target filter <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 25 `；EOL ` RVA 0x34549200 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-65e0de238ef95f31](../../evidence/conditions-sets-039.md#c-65e0de238ef95f31) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001840

```text
(config-router-scope-af)# default bgp default route-target filter <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 25 `；EOL ` RVA 0x345494A0 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0fb94622c94e5967](../../evidence/conditions-sets-006.md#c-0fb94622c94e5967) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001706

```text
(config-router-scope-af)# default bgp deterministic-med <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 10 `；EOL ` RVA 0x34541560 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d038dabf7ea3a128](../../evidence/conditions-sets-080.md#c-d038dabf7ea3a128) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001680

```text
(config-router-scope-af)# default bgp dmzlink-bw <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 31 `；EOL ` RVA 0x3454CB98 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e60672eeace3f616](../../evidence/conditions-sets-089.md#c-e60672eeace3f616) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001599

```text
(config-router-scope-af)# default bgp dynamic-med-interval <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 21 `；EOL ` RVA 0x34541588 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9846d934a45ff2aa](../../evidence/conditions-sets-059.md#c-9846d934a45ff2aa) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001688

```text
(config-router-scope-af)# default bgp enforce-first-as <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 20 `；EOL ` RVA 0x34540790 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d038dabf7ea3a128](../../evidence/conditions-sets-080.md#c-d038dabf7ea3a128) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001722

```text
(config-router-scope-af)# default bgp enhanced-error <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 82 `；EOL ` RVA 0x345431D0 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d76b3b8dda018a78](../../evidence/conditions-sets-083.md#c-d76b3b8dda018a78) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001640

```text
(config-router-scope-af)# default bgp fast-external-fallover <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 1 `；EOL ` RVA 0x3453E478 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d038dabf7ea3a128](../../evidence/conditions-sets-080.md#c-d038dabf7ea3a128) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001737

```text
(config-router-scope-af)# default bgp graceful-restart <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 35 `；EOL ` RVA 0x34544040 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d038dabf7ea3a128](../../evidence/conditions-sets-080.md#c-d038dabf7ea3a128) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001728

```text
(config-router-scope-af)# default bgp graceful-restart restart-time <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 36 `；EOL ` RVA 0x34543A10 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-258c387f51a1d7ce](../../evidence/conditions-sets-015.md#c-258c387f51a1d7ce) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001732

```text
(config-router-scope-af)# default bgp graceful-restart stalepath-time <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 37 `；EOL ` RVA 0x34543A78 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8d73d81d3f3ac40c](../../evidence/conditions-sets-055.md#c-8d73d81d3f3ac40c) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001901

```text
(config-router-scope-af)# default bgp graceful-shutdown all vrfs activate <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 79 `；EOL ` RVA 0x345444A8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-66f3816b6a249c29](../../evidence/conditions-sets-040.md#c-66f3816b6a249c29) · [状态效果 S-b1f7f09edfec0ce1](../../evidence/state_effects-sets-038.md#s-b1f7f09edfec0ce1)

### observed_connections-001899

```text
(config-router-scope-af)# default bgp inject-map <string> exist-map <string> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 32 `；EOL ` RVA 0x3454E710 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` route-map name；` string ` route-map name。

[条件 C-f8673071a7ce23a7](../../evidence/conditions-sets-096.md#c-f8673071a7ce23a7) · [参数 P-72ba39e577f273d6](../../evidence/parameters-sets-009.md#p-72ba39e577f273d6) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001838

```text
(config-router-scope-af)# default bgp label-allocation-batch <number:0..4294967295> <number:0..4294967295> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 53 `；EOL ` RVA 0x3453E808 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Timer value in milliseconds；` unsigned_number ` Batch Size。

[条件 C-d038dabf7ea3a128](../../evidence/conditions-sets-080.md#c-d038dabf7ea3a128) · [参数 P-675aa1ff414c4c13](../../evidence/parameters-sets-008.md#p-675aa1ff414c4c13) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001862

```text
(config-router-scope-af)# default bgp listen block <address> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 93 `；EOL ` RVA 0x3454C5A8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IPv4 Dynamic Peering Address。

[条件 C-88fc52820904d643](../../evidence/conditions-sets-053.md#c-88fc52820904d643) · [参数 P-d42b5fda11d4d375](../../evidence/parameters-sets-016.md#p-d42b5fda11d4d375) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001873

```text
(config-router-scope-af)# default bgp listen block <address> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 93 `；EOL ` RVA 0x34542508 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IPv4 Dynamic Peering Address。

[条件 C-9af955235c91b53a](../../evidence/conditions-sets-060.md#c-9af955235c91b53a) · [参数 P-3fcb738a2abc9e2d](../../evidence/parameters-sets-005.md#p-3fcb738a2abc9e2d) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001701

```text
(config-router-scope-af)# default bgp listen limit <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 61 `；EOL ` RVA 0x3454C4F0 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a1df8462dd54d10c](../../evidence/conditions-sets-063.md#c-a1df8462dd54d10c) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001724

```text
(config-router-scope-af)# default bgp listen limit <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 61 `；EOL ` RVA 0x34542428 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-23d23a5efd0b8f90](../../evidence/conditions-sets-014.md#c-23d23a5efd0b8f90) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001815

```text
(config-router-scope-af)# default bgp listen persistent <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 94 `；EOL ` RVA 0x34542840 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9af955235c91b53a](../../evidence/conditions-sets-060.md#c-9af955235c91b53a) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001698

```text
(config-router-scope-af)# default bgp log-neighbor-changes <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 11 `；EOL ` RVA 0x34540A38 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d038dabf7ea3a128](../../evidence/conditions-sets-080.md#c-d038dabf7ea3a128) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001756

```text
(config-router-scope-af)# default bgp maxas-limit <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 26 `；EOL ` RVA 0x34547C50 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8820c16c18e6832e](../../evidence/conditions-sets-053.md#c-8820c16c18e6832e) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001744

```text
(config-router-scope-af)# default bgp maxcommunity-limit <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 27 `；EOL ` RVA 0x34547260 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6460891d2538e055](../../evidence/conditions-sets-039.md#c-6460891d2538e055) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001752

```text
(config-router-scope-af)# default bgp maxextcommunity-limit <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 29 `；EOL ` RVA 0x34547900 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8a28a6f941863eb0](../../evidence/conditions-sets-053.md#c-8a28a6f941863eb0) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001748

```text
(config-router-scope-af)# default bgp maxlargecommunity-limit <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 28 `；EOL ` RVA 0x345475B0 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ea5eb6d959883f84](../../evidence/conditions-sets-091.md#c-ea5eb6d959883f84) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001716

```text
(config-router-scope-af)# default bgp mpls-local-label <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 81 `；EOL ` RVA 0x3454EA88 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8cfe7e0e372db70a](../../evidence/conditions-sets-055.md#c-8cfe7e0e372db70a) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001865

```text
(config-router-scope-af)# default bgp nexthop route-map <string> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 56 `；EOL ` RVA 0x3454D300 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` route-map name。

[条件 C-e7fae0a1d2b836dc](../../evidence/conditions-sets-090.md#c-e7fae0a1d2b836dc) · [参数 P-018cf62f945dd9fb](../../evidence/parameters-sets-001.md#p-018cf62f945dd9fb) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001809

```text
(config-router-scope-af)# default bgp nexthop trigger critical-delay <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 48 `；EOL ` RVA 0x3454D868 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ec1659655f2a7564](../../evidence/conditions-sets-091.md#c-ec1659655f2a7564) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001806

```text
(config-router-scope-af)# default bgp nexthop trigger delay <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 47 `；EOL ` RVA 0x3454D5E8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c0f2a5b04293820b](../../evidence/conditions-sets-074.md#c-c0f2a5b04293820b) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001861

```text
(config-router-scope-af)# default bgp nexthop trigger enable <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 49 `；EOL ` RVA 0x3454D5C0 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-71809c74616618a3](../../evidence/conditions-sets-044.md#c-71809c74616618a3) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001870

```text
(config-router-scope-af)# default bgp nopeerup-delay cold-boot <number:1..3600> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 74 `；EOL ` RVA 0x34542E68 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Delay in seconds。

[条件 C-a4057e89490d6056](../../evidence/conditions-sets-063.md#c-a4057e89490d6056) · [参数 P-06d763f31c291b7c](../../evidence/parameters-sets-001.md#p-06d763f31c291b7c) · [状态效果 S-645fcc95a3a12182](../../evidence/state_effects-sets-021.md#s-645fcc95a3a12182)

### observed_connections-001784

```text
(config-router-scope-af)# default bgp recursion host <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 72 `；EOL ` RVA 0x3454B960 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d87b32e4fbe61c8b](../../evidence/conditions-sets-083.md#c-d87b32e4fbe61c8b) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001667

```text
(config-router-scope-af)# default bgp redistribute-internal <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 2 `；EOL ` RVA 0x3454FC88 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-af02a502302afa3f](../../evidence/conditions-sets-068.md#c-af02a502302afa3f) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001826

```text
(config-router-scope-af)# default bgp refresh max-eor-time <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 16 `；EOL ` RVA 0x34545238 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1566d04ddc49c79e](../../evidence/conditions-sets-008.md#c-1566d04ddc49c79e) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001822

```text
(config-router-scope-af)# default bgp refresh stalepath-time <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 15 `；EOL ` RVA 0x34544EC8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2c6d3e539b020e20](../../evidence/conditions-sets-017.md#c-2c6d3e539b020e20) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001824

```text
(config-router-scope-af)# default bgp regexp deterministic <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 44 `；EOL ` RVA 0x34545C50 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f311201ce1b8ec9e](../../evidence/conditions-sets-094.md#c-f311201ce1b8ec9e) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001785

```text
(config-router-scope-af)# default bgp route-map priority <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 59 `；EOL ` RVA 0x34550E18 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-11589918a9054012](../../evidence/conditions-sets-007.md#c-11589918a9054012) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001650

```text
(config-router-scope-af)# default bgp route-map-cache <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 34 `；EOL ` RVA 0x3453EA90 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d038dabf7ea3a128](../../evidence/conditions-sets-080.md#c-d038dabf7ea3a128) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001658

```text
(config-router-scope-af)# default bgp router-id <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 4 `；EOL ` RVA 0x3453DE48 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b081150a52a6c73f](../../evidence/conditions-sets-068.md#c-b081150a52a6c73f) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001702

```text
(config-router-scope-af)# default bgp router-id <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 4 `；EOL ` RVA 0x3454C010 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2a9c37b900d583d0](../../evidence/conditions-sets-017.md#c-2a9c37b900d583d0) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001905

```text
(config-router-scope-af)# default bgp rpki server tcp <address> port <number:1..65535> refresh <number:1..65535> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 76 `；EOL ` RVA 0x34551C30 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IPv6 address of RPKI cache server；` unsigned_number ` Port number；` unsigned_number ` Refresh time in seconds。

[条件 C-dc3fc388f0c7095d](../../evidence/conditions-sets-085.md#c-dc3fc388f0c7095d) · [参数 P-6ddc8c613ed3413e](../../evidence/parameters-sets-009.md#p-6ddc8c613ed3413e) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001710

```text
(config-router-scope-af)# default bgp rr-group <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 23 `；EOL ` RVA 0x3454E2A8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-10a8b71aea07c5f3](../../evidence/conditions-sets-007.md#c-10a8b71aea07c5f3) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001757

```text
(config-router-scope-af)# default bgp safe-ebgp-policy <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 92 `；EOL ` RVA 0x345481E8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4123e929cf76e12f](../../evidence/conditions-sets-025.md#c-4123e929cf76e12f) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001808

```text
(config-router-scope-af)# default bgp scan-time <number:5..60> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 22 `；EOL ` RVA 0x3454DF38 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Scanner interval (seconds)。

[条件 C-5699db3668bbc500](../../evidence/conditions-sets-034.md#c-5699db3668bbc500) · [参数 P-8a5b54a14f207a55](../../evidence/parameters-sets-011.md#p-8a5b54a14f207a55) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001787

```text
(config-router-scope-af)# default bgp slow-peer detection <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 67 `；EOL ` RVA 0x3454EF58 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f714a5b93bf72cfc](../../evidence/conditions-sets-095.md#c-f714a5b93bf72cfc) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001853

```text
(config-router-scope-af)# default bgp slow-peer split-update-group dynamic <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 68 `；EOL ` RVA 0x3454F528 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-359238f8152a49e3](../../evidence/conditions-sets-021.md#c-359238f8152a49e3) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001867

```text
(config-router-scope-af)# default bgp snmp traps add-type <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 90 `；EOL ` RVA 0x34541B50 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d038dabf7ea3a128](../../evidence/conditions-sets-080.md#c-d038dabf7ea3a128) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001699

```text
(config-router-scope-af)# default bgp soft-reconfig-backup <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 52 `；EOL ` RVA 0x3454CEE8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-49d83a5d33e818c0](../../evidence/conditions-sets-029.md#c-49d83a5d33e818c0) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001897

```text
(config-router-scope-af)# default bgp sourced-paths per-net isis all <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 89 `；EOL ` RVA 0x34550A98 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6159d8ad545642ce](../../evidence/conditions-sets-038.md#c-6159d8ad545642ce) · [状态效果 S-62506105e079b9ba](../../evidence/state_effects-sets-021.md#s-62506105e079b9ba)

### observed_connections-001893

```text
(config-router-scope-af)# default bgp sourced-paths per-net ospf all <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 87 `；EOL ` RVA 0x34550438 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6159d8ad545642ce](../../evidence/conditions-sets-038.md#c-6159d8ad545642ce) · [状态效果 S-affcf22dd69fcc7f](../../evidence/state_effects-sets-037.md#s-affcf22dd69fcc7f)

### observed_connections-001895

```text
(config-router-scope-af)# default bgp sourced-paths per-net ospfv3 all <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 88 `；EOL ` RVA 0x34550780 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6159d8ad545642ce](../../evidence/conditions-sets-038.md#c-6159d8ad545642ce) · [状态效果 S-af8e9c9ddbca9e2c](../../evidence/state_effects-sets-037.md#s-af8e9c9ddbca9e2c)

### observed_connections-001891

```text
(config-router-scope-af)# default bgp sourced-paths per-net static all <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 86 `；EOL ` RVA 0x345500F0 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6159d8ad545642ce](../../evidence/conditions-sets-038.md#c-6159d8ad545642ce) · [状态效果 S-ab8ed7a5c6292113](../../evidence/state_effects-sets-036.md#s-ab8ed7a5c6292113)

### observed_connections-001816

```text
(config-router-scope-af)# default bgp sso route-refresh-enable <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 38 `；EOL ` RVA 0x34544B08 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f311201ce1b8ec9e](../../evidence/conditions-sets-094.md#c-f311201ce1b8ec9e) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001672

```text
(config-router-scope-af)# default bgp suppress-inactive <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 45 `；EOL ` RVA 0x3454BC60 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a18c8bfcf986468c](../../evidence/conditions-sets-062.md#c-a18c8bfcf986468c) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001558

```text
(config-router-scope-af)# default bgp tid <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 55 `；EOL ` RVA 0x3453D688 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e59c9a74c1de4a2e](../../evidence/conditions-sets-089.md#c-e59c9a74c1de4a2e) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001792

```text
(config-router-scope-af)# default bgp transport path-mtu-discovery <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 50 `；EOL ` RVA 0x34540500 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d038dabf7ea3a128](../../evidence/conditions-sets-080.md#c-d038dabf7ea3a128) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001612

```text
(config-router-scope-af)# default bgp update-delay <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 30 `；EOL ` RVA 0x34543480 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-27d4cb75bf524b65](../../evidence/conditions-sets-016.md#c-27d4cb75bf524b65) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001846

```text
(config-router-scope-af)# default bgp update-group split as-override <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 73 `；EOL ` RVA 0x3454F8F8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1f2cd0608d0fe1e4](../../evidence/conditions-sets-012.md#c-1f2cd0608d0fe1e4) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001645

```text
(config-router-scope-af)# default bgp upgrade-cli <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 33 `；EOL ` RVA 0x3453DAA0 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-99a615dc14da7261](../../evidence/conditions-sets-059.md#c-99a615dc14da7261) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001691

```text
(config-router-scope-af)# default bgp va <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 80 `；EOL ` RVA 0x345511C0 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f7cfd7ba4e0acbdd](../../evidence/conditions-sets-096.md#c-f7cfd7ba4e0acbdd) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001820

```text
(config-router-scope-af)# default bgp vrf-update-optimisation off <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 66 `；EOL ` RVA 0x345455C0 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f311201ce1b8ec9e](../../evidence/conditions-sets-094.md#c-f311201ce1b8ec9e) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001740

```text
(config-router-scope-af)# default bgp write-limit <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 40 `；EOL ` RVA 0x34545918 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-156cdac482787f36](../../evidence/conditions-sets-008.md#c-156cdac482787f36) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001552

```text
(config-router-scope-af)# default context <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 0 `；EOL ` RVA 0x33C44A60 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ada418e0516d363b](../../evidence/conditions-sets-067.md#c-ada418e0516d363b) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001638

```text
(config-router-scope-af)# default default-information originate <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 6 `；EOL ` RVA 0x3552C0E0 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-55ee11b1a1edf64f](../../evidence/conditions-sets-034.md#c-55ee11b1a1edf64f) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001715

```text
(config-router-scope-af)# default default-information originate <cr>
```

Handler ` RVA 0xE1F1F70 `；selector ` 0 `；EOL ` RVA 0x344F59A8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a9575d4774f8de5d](../../evidence/conditions-sets-065.md#c-a9575d4774f8de5d) · [状态效果 S-31abff40a35c44f1](../../evidence/state_effects-sets-011.md#s-31abff40a35c44f1)

### observed_connections-001577

```text
(config-router-scope-af)# default default-metric <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 12 `；EOL ` RVA 0x3552C878 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0d7ad9d9671c3c19](../../evidence/conditions-sets-005.md#c-0d7ad9d9671c3c19) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001604

```text
(config-router-scope-af)# default default-metric <cr>
```

Handler ` RVA 0xE1F35A0 `；selector ` 0 `；EOL ` RVA 0x344F6270 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7412fd70c0f11908](../../evidence/conditions-sets-045.md#c-7412fd70c0f11908) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001614

```text
(config-router-scope-af)# default distance <cr>
```

Handler ` RVA 0xE1E3290 `；selector ` 1 `；EOL ` RVA 0x344F73A0 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8507c54e95cd8959](../../evidence/conditions-sets-051.md#c-8507c54e95cd8959) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001723

```text
(config-router-scope-af)# default distance bgp <cr>
```

Handler ` RVA 0xF1B8400 `；selector ` 1 `；EOL ` RVA 0x344E1458 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b241df4e6f36d579](../../evidence/conditions-sets-069.md#c-b241df4e6f36d579) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001731

```text
(config-router-scope-af)# default distance mbgp <cr>
```

Handler ` RVA 0xF1B8400 `；selector ` 2 `；EOL ` RVA 0x344E1850 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad31524aadb46fbf](../../evidence/conditions-sets-067.md#c-ad31524aadb46fbf) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001729

```text
(config-router-scope-af)# default distribute-list in <cr>
```

Handler ` RVA 0xE1EE180 `；selector ` 0 `；EOL ` RVA 0x344F6960 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ea8c888fa5896889](../../evidence/conditions-sets-091.md#c-ea8c888fa5896889) · [状态效果 S-0fd23bf562887378](../../evidence/state_effects-sets-004.md#s-0fd23bf562887378)

### observed_connections-001543

```text
(config-router-scope-af)# default flash-update-threshold <cr>
```

Handler ` RVA 0xE1F7ED0 `；selector ` 0 `；EOL ` RVA 0x344F5498 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0e6ae0e65ef7f08e](../../evidence/conditions-sets-006.md#c-0e6ae0e65ef7f08e) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001564

```text
(config-router-scope-af)# default import <cr>
```

Handler ` RVA 0xF08D6A0 `；selector ` 0 `；EOL ` RVA 0x3453B9F8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-cf6c5368b0c90546](../../evidence/conditions-sets-080.md#c-cf6c5368b0c90546) · [状态效果 S-7eaea67e70599166](../../evidence/state_effects-sets-027.md#s-7eaea67e70599166)

### observed_connections-001762

```text
(config-router-scope-af)# default import l2vpn evpn <cr>
```

Handler ` RVA 0xF08DFA0 `；selector ` 0 `；EOL ` RVA 0x3453C778 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e4d616715d8d17cf](../../evidence/conditions-sets-088.md#c-e4d616715d8d17cf) · [状态效果 S-197f577fef47c709](../../evidence/state_effects-sets-006.md#s-197f577fef47c709)

### observed_connections-001631

```text
(config-router-scope-af)# default import nhrp <cr>
```

Handler ` RVA 0xF263450 `；selector ` 0 `；EOL ` RVA 0x3453CB58 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4fa832900473a20f](../../evidence/conditions-sets-031.md#c-4fa832900473a20f) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001759

```text
(config-router-scope-af)# default import vpnv4 unicast <cr>
```

Handler ` RVA 0xF08E500 `；selector ` 0 `；EOL ` RVA 0x3453C208 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f920191bbdeca293](../../evidence/conditions-sets-096.md#c-f920191bbdeca293) · [状态效果 S-87579fb5fea8813c](../../evidence/state_effects-sets-029.md#s-87579fb5fea8813c)

### observed_connections-001541

```text
(config-router-scope-af)# default input-queue <cr>
```

Handler ` RVA 0xE1F8060 `；selector ` 0 `；EOL ` RVA 0x344F51A8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c4824c7cac4b28be](../../evidence/conditions-sets-076.md#c-c4824c7cac4b28be) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001652

```text
(config-router-scope-af)# default label mode <cr>
```

Handler ` RVA 0xF1D1A30 `；selector ` 0 `；EOL ` RVA 0x344F20C8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5cf0aca29de8310d](../../evidence/conditions-sets-036.md#c-5cf0aca29de8310d) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001589

```text
(config-router-scope-af)# default maximum-paths <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 8 `；EOL ` RVA 0x3552D6D8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-83cfb67834f65d1d](../../evidence/conditions-sets-051.md#c-83cfb67834f65d1d) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001665

```text
(config-router-scope-af)# default metric holddown <cr>
```

Handler ` RVA 0xE1F32D0 `；selector ` 1 `；EOL ` RVA 0x344F3AF0 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4bbe96da81617452](../../evidence/conditions-sets-030.md#c-4bbe96da81617452) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001591

```text
(config-router-scope-af)# default metric maximum-hops <cr>
```

Handler ` RVA 0xE1F32D0 `；selector ` 2 `；EOL ` RVA 0x344F3B18 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8221b40cbcf421f4](../../evidence/conditions-sets-050.md#c-8221b40cbcf421f4) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001693

```text
(config-router-scope-af)# default metric weights <cr>
```

Handler ` RVA 0xE1F32D0 `；selector ` 0 `；EOL ` RVA 0x344F40D8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-74aaeceddc53dc5d](../../evidence/conditions-sets-045.md#c-74aaeceddc53dc5d) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001773

```text
(config-router-scope-af)# default offset-list <number:0..99> in <cr>
```

Handler ` RVA 0xE1F1330 `；selector ` 0 `；EOL ` RVA 0x344F1278 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Access list of networks to apply offset (0 selects all networks)。

[条件 C-b7414ba60af25c7b](../../evidence/conditions-sets-071.md#c-b7414ba60af25c7b) · [参数 P-583d525582bab90e](../../evidence/parameters-sets-007.md#p-583d525582bab90e) · [状态效果 S-b9747e9b69c9891f](../../evidence/state_effects-sets-039.md#s-b9747e9b69c9891f)

### observed_connections-001532

```text
(config-router-scope-af)# default output-delay <cr>
```

Handler ` RVA 0xE1F4590 `；selector ` 0 `；EOL ` RVA 0x344F0CD0 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-75b85446d28e76e2](../../evidence/conditions-sets-046.md#c-75b85446d28e76e2) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001636

```text
(config-router-scope-af)# default passive-interface default <cr>
```

Handler ` RVA 0xE1F3960 `；selector ` 0 `；EOL ` RVA 0x344F08C0 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-66b93bc17fdac1bf](../../evidence/conditions-sets-040.md#c-66b93bc17fdac1bf) · [状态效果 S-c059bff995679374](../../evidence/state_effects-sets-041.md#s-c059bff995679374)

### observed_connections-001566

```text
(config-router-scope-af)# default propagate-aspath <cr>
```

Handler ` RVA 0xF1D1560 `；selector ` 1 `；EOL ` RVA 0x344F1A40 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f1958560caef3b6e](../../evidence/conditions-sets-093.md#c-f1958560caef3b6e) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001571

```text
(config-router-scope-af)# default propagate-community <cr>
```

Handler ` RVA 0xF1D1560 `；selector ` 2 `；EOL ` RVA 0x344F1CE8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f1958560caef3b6e](../../evidence/conditions-sets-093.md#c-f1958560caef3b6e) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001633

```text
(config-router-scope-af)# default redistribute maximum-prefix <cr>
```

Handler ` RVA 0xE1E4550 `；selector ` 0 `；EOL ` RVA 0x344ED8B8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4aeb6ea7334e51cb](../../evidence/conditions-sets-029.md#c-4aeb6ea7334e51cb) · [状态效果 S-7f26a3e932f2af2d](../../evidence/state_effects-sets-027.md#s-7f26a3e932f2af2d)

### observed_connections-001634

```text
(config-router-scope-af)# default redistribute maximum-prefix <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 5 `；EOL ` RVA 0x3552A1B0 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4f3adb05292f668a](../../evidence/conditions-sets-031.md#c-4f3adb05292f668a) · [状态效果 S-eedb1b43479a376d](../../evidence/state_effects-sets-050.md#s-eedb1b43479a376d)

### observed_connections-001642

```text
(config-router-scope-af)# default snmp context <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 0 `；EOL ` RVA 0x33C455F0 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7598dc8aeb3669dc](../../evidence/conditions-sets-046.md#c-7598dc8aeb3669dc) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001889

```text
(config-router-scope-af)# default snmp context <string> community <string> <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 2 `；EOL ` RVA 0x33C45118 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Context Name；` string ` SNMP community string。

[条件 C-2573c969c66067b6](../../evidence/conditions-sets-015.md#c-2573c969c66067b6) · [参数 P-9b6eb89831feec60](../../evidence/parameters-sets-012.md#p-9b6eb89831feec60) · [状态效果 S-a7bba74eff5248f4](../../evidence/state_effects-sets-035.md#s-a7bba74eff5248f4)

### observed_connections-001888

```text
(config-router-scope-af)# default snmp context <string> user <string> <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 23 `；EOL ` RVA 0x33C456D0 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Context Name；` string ` Name of the user。

[条件 C-67e2e80e2c1c144d](../../evidence/conditions-sets-040.md#c-67e2e80e2c1c144d) · [参数 P-cfc42ec8ad667e32](../../evidence/parameters-sets-016.md#p-cfc42ec8ad667e32) · [状态效果 S-6247a785456481e4](../../evidence/state_effects-sets-021.md#s-6247a785456481e4)

### observed_connections-001763

```text
(config-router-scope-af)# default summary-prefix <address> <address> <cr>
```

Handler ` RVA 0xE1DF4C0 `；selector ` 0 `；EOL ` RVA 0x344ECB38 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IP summary address；` address ` Summary mask。

[条件 C-2cd36336053d115f](../../evidence/conditions-sets-018.md#c-2cd36336053d115f) · [参数 P-aebe586c61a4934d](../../evidence/parameters-sets-013.md#p-aebe586c61a4934d) · [状态效果 S-7ce87ba9df386165](../../evidence/state_effects-sets-026.md#s-7ce87ba9df386165)

### observed_connections-001628

```text
(config-router-scope-af)# default summary-prefix <address> <cr>
```

Handler ` RVA 0xE1DF4C0 `；selector ` 21 `；EOL ` RVA 0x344ED118 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IP summary address。

[条件 C-1a963b03b7350236](../../evidence/conditions-sets-010.md#c-1a963b03b7350236) · [参数 P-b5381e36e4d9d9b2](../../evidence/parameters-sets-014.md#p-b5381e36e4d9d9b2) · [状态效果 S-7ce87ba9df386165](../../evidence/state_effects-sets-026.md#s-7ce87ba9df386165)

### observed_connections-001554

```text
(config-router-scope-af)# default synchronization <cr>
```

Handler ` RVA 0xF1CF320 `；selector ` 0 `；EOL ` RVA 0x3453CF18 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-345576d2d611a8ef](../../evidence/conditions-sets-020.md#c-345576d2d611a8ef) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001557

```text
(config-router-scope-af)# default synchronization <cr>
```

Handler ` RVA 0xF1CF320 `；selector ` 0 `；EOL ` RVA 0x3552D0E8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-554622deff07851c](../../evidence/conditions-sets-033.md#c-554622deff07851c) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001563

```text
(config-router-scope-af)# default table-map <cr>
```

Handler ` RVA 0xE1F4690 `；selector ` 0 `；EOL ` RVA 0x3453D2F0 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-132e9960e3e10c3c](../../evidence/conditions-sets-008.md#c-132e9960e3e10c3c) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001576

```text
(config-router-scope-af)# default table-map <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 17 `；EOL ` RVA 0x3552CE08 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-93a0d247a917c17c](../../evidence/conditions-sets-057.md#c-93a0d247a917c17c) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001622

```text
(config-router-scope-af)# default topology base <cr>
```

Handler ` RVA 0xF14A450 `；selector ` 0 `；EOL ` RVA 0x345B9378 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-13c0bd21cae4d782](../../evidence/conditions-sets-008.md#c-13c0bd21cae4d782) · [状态效果 S-0b521a3ef7db4cb4](../../evidence/state_effects-sets-003.md#s-0b521a3ef7db4cb4)

### observed_connections-001551

```text
(config-router-scope-af)# default version <cr>
```

Handler ` RVA 0xFB4F020 `；selector ` 0 `；EOL ` RVA 0x344EC5E8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-af24935869a2b032](../../evidence/conditions-sets-068.md#c-af24935869a2b032) · [状态效果 S-58092378c9b9235c](../../evidence/state_effects-sets-019.md#s-58092378c9b9235c)

### observed_connections-001569

```text
(config-router-scope-af)# default-information originate <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 6 `；EOL ` RVA 0x3552C0E0 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-55ee11b1a1edf64f](../../evidence/conditions-sets-034.md#c-55ee11b1a1edf64f)

### observed_connections-001603

```text
(config-router-scope-af)# default-information originate <cr>
```

Handler ` RVA 0xE1F1F70 `；selector ` 0 `；EOL ` RVA 0x344F59A8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a9575d4774f8de5d](../../evidence/conditions-sets-065.md#c-a9575d4774f8de5d) · [状态效果 S-5d6c1fc095b9a969](../../evidence/state_effects-sets-020.md#s-5d6c1fc095b9a969)

### observed_connections-001580

```text
(config-router-scope-af)# default-metric <number:1..16777214> <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 12 `；EOL ` RVA 0x3552C878 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Default metric。

[条件 C-239a1db2f6a454ef](../../evidence/conditions-sets-014.md#c-239a1db2f6a454ef) · [参数 P-c2531ab199b4b1f6](../../evidence/parameters-sets-015.md#p-c2531ab199b4b1f6)

### observed_connections-001605

```text
(config-router-scope-af)# default-metric <number:1..16777214> <cr>
```

Handler ` RVA 0xE1F35A0 `；selector ` 0 `；EOL ` RVA 0x344F6270 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` OSPF default metric。

[条件 C-94b0514c823ae0a4](../../evidence/conditions-sets-057.md#c-94b0514c823ae0a4) · [参数 P-fc483cf9a933f3c9](../../evidence/parameters-sets-019.md#p-fc483cf9a933f3c9)

### observed_connections-001608

```text
(config-router-scope-af)# distance <number:1..255> <cr>
```

Handler ` RVA 0xE1E3290 `；selector ` 1 `；EOL ` RVA 0x344F73A0 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Administrative distance。

[条件 C-fa4013929c785873](../../evidence/conditions-sets-097.md#c-fa4013929c785873) · [参数 P-93d0335cadd4fa38](../../evidence/parameters-sets-011.md#p-93d0335cadd4fa38)

### observed_connections-001871

```text
(config-router-scope-af)# distance bgp <number:1..255> <number:1..255> <number:1..255> <cr>
```

Handler ` RVA 0xF1B8400 `；selector ` 1 `；EOL ` RVA 0x344E1458 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Distance for routes external to the AS；` unsigned_number ` Distance for routes internal to the AS；` unsigned_number ` Distance for local routes。

[条件 C-58f37f679a5a994b](../../evidence/conditions-sets-035.md#c-58f37f679a5a994b) · [参数 P-da75e935134966de](../../evidence/parameters-sets-016.md#p-da75e935134966de)

### observed_connections-001874

```text
(config-router-scope-af)# distance mbgp <number:0..255> <number:0..255> <number:0..255> <cr>
```

Handler ` RVA 0xF1B8400 `；selector ` 2 `；EOL ` RVA 0x344E1850 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Distance for routes external to the AS；` unsigned_number ` Distance for routes internal to the AS；` unsigned_number ` Distance for local routes。

[条件 C-d85a73f5e0afe600](../../evidence/conditions-sets-083.md#c-d85a73f5e0afe600) · [参数 P-fe1448f258db0f35](../../evidence/parameters-sets-019.md#p-fe1448f258db0f35)

### observed_connections-001616

```text
(config-router-scope-af)# distribute-list in <cr>
```

Handler ` RVA 0xE1EE180 `；selector ` 0 `；EOL ` RVA 0x344F6960 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ea8c888fa5896889](../../evidence/conditions-sets-091.md#c-ea8c888fa5896889) · [状态效果 S-ab5262da43f039dd](../../evidence/state_effects-sets-036.md#s-ab5262da43f039dd)

### observed_connections-001963

```text
(config-router-scope-af)# distribute-list out <?router_action_proc_vpn@555589a4a8e8> <cr>
```

Handler ` RVA 0xE1EE180 `；selector ` 0 `；EOL ` RVA 0x344F6960 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f2a9fe0c9ea0a6f4](../../evidence/conditions-sets-094.md#c-f2a9fe0c9ea0a6f4) · [缺口 G-2e21ce0a3cebe79d](../../evidence/gaps-sets-002.md#g-2e21ce0a3cebe79d) · [状态效果 S-1aa6b36ada32d509](../../evidence/state_effects-sets-006.md#s-1aa6b36ada32d509)

### observed_connections-001529

```text
(config-router-scope-af)# exit-address-family <cr>
```

Handler ` RVA 0xF11AA70 `；selector ` 0 `；EOL ` RVA 0x3453AE08 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9a03b9e699abbe25](../../evidence/conditions-sets-060.md#c-9a03b9e699abbe25)

### observed_connections-001528

```text
(config-router-scope-af)# flash-update-threshold <number:0..30> <cr>
```

Handler ` RVA 0xE1F7ED0 `；selector ` 0 `；EOL ` RVA 0x344F5498 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` threshold in seconds。

[条件 C-a987807880c47e2b](../../evidence/conditions-sets-065.md#c-a987807880c47e2b) · [参数 P-a2345e205347a59e](../../evidence/parameters-sets-012.md#p-a2345e205347a59e)

### observed_connections-001535

```text
(config-router-scope-af)# import <cr>
```

Handler ` RVA 0xF08D6A0 `；selector ` 0 `；EOL ` RVA 0x3453B9F8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cf6c5368b0c90546](../../evidence/conditions-sets-080.md#c-cf6c5368b0c90546) · [状态效果 S-b434b78d0c3abac9](../../evidence/state_effects-sets-038.md#s-b434b78d0c3abac9)

### observed_connections-001625

```text
(config-router-scope-af)# import l2vpn evpn <cr>
```

Handler ` RVA 0xF08DFA0 `；selector ` 0 `；EOL ` RVA 0x3453C778 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e4d616715d8d17cf](../../evidence/conditions-sets-088.md#c-e4d616715d8d17cf) · [状态效果 S-f4d5f5cfe4c09874](../../evidence/state_effects-sets-052.md#s-f4d5f5cfe4c09874)

### observed_connections-001559

```text
(config-router-scope-af)# import nhrp <cr>
```

Handler ` RVA 0xF263450 `；selector ` 0 `；EOL ` RVA 0x3453CB58 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4fa832900473a20f](../../evidence/conditions-sets-031.md#c-4fa832900473a20f)

### observed_connections-001985

```text
(config-router-scope-af)# import path selection <?option@555589a8fce0> <cr>
```

Handler ` RVA 0xF08D6A0 `；selector ` 0 `；EOL ` RVA 0x3453B9F8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-aa895deca4fda0ce](../../evidence/conditions-sets-066.md#c-aa895deca4fda0ce) · [缺口 G-559f8036ec168bbb](../../evidence/gaps-sets-003.md#g-559f8036ec168bbb) · [状态效果 S-f9ae137119760f39](../../evidence/state_effects-sets-053.md#s-f9ae137119760f39)

### observed_connections-001623

```text
(config-router-scope-af)# import vpnv4 unicast <cr>
```

Handler ` RVA 0xF08E500 `；selector ` 0 `；EOL ` RVA 0x3453C208 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f920191bbdeca293](../../evidence/conditions-sets-096.md#c-f920191bbdeca293) · [状态效果 S-4f93ab1ef6bdc97d](../../evidence/state_effects-sets-017.md#s-4f93ab1ef6bdc97d)

### observed_connections-001527

```text
(config-router-scope-af)# input-queue <number:0..1024> <cr>
```

Handler ` RVA 0xE1F8060 `；selector ` 0 `；EOL ` RVA 0x344F51A8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` queue depth。

[条件 C-9fd5ba85a10ee162](../../evidence/conditions-sets-062.md#c-9fd5ba85a10ee162) · [参数 P-5267c0140d4e52a7](../../evidence/parameters-sets-007.md#p-5267c0140d4e52a7)

### observed_connections-001959

```text
(config-router-scope-af)# label mode all-explicit-null <cr>
```

Handler ` RVA 0xF1D1A30 `；selector ` 2 `；EOL ` RVA 0x344F2410 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-196d3da51f3953c9](../../evidence/conditions-sets-010.md#c-196d3da51f3953c9) · [缺口 G-dc64f1c5cb22dabb](../../evidence/gaps-sets-008.md#g-dc64f1c5cb22dabb) · [状态效果 S-a45599ec6583c65b](../../evidence/state_effects-sets-035.md#s-a45599ec6583c65b)

### observed_connections-001958

```text
(config-router-scope-af)# label mode explicit-null <cr>
```

Handler ` RVA 0xF1D1A30 `；selector ` 1 `；EOL ` RVA 0x344F2158 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-196d3da51f3953c9](../../evidence/conditions-sets-010.md#c-196d3da51f3953c9) · [缺口 G-6ace9773ef4ef6df](../../evidence/gaps-sets-004.md#g-6ace9773ef4ef6df) · [状态效果 S-8bd26dbd0a18e1e8](../../evidence/state_effects-sets-030.md#s-8bd26dbd0a18e1e8)

### observed_connections-001538

```text
(config-router-scope-af)# maximum-paths <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 8 `；EOL ` RVA 0x3552D6D8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-83cfb67834f65d1d](../../evidence/conditions-sets-051.md#c-83cfb67834f65d1d)

### observed_connections-001919

```text
(config-router-scope-af)# maximum-paths <number:dynamic> <cr>
```

Handler ` RVA 0xE1E26B0 `；selector ` 0 `；EOL ` RVA 0x344F4CC0 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Number of paths。

[条件 C-c4d2c8b573521027](../../evidence/conditions-sets-076.md#c-c4d2c8b573521027) · [缺口 G-d1981088f6fbd147](../../evidence/gaps-sets-007.md#g-d1981088f6fbd147) · [参数 P-aa581bb178e213f9](../../evidence/parameters-sets-013.md#p-aa581bb178e213f9)

### observed_connections-001918

```text
(config-router-scope-af)# maximum-secondary-paths <number:dynamic> <cr>
```

Handler ` RVA 0xE1E2BD0 `；selector ` 0 `；EOL ` RVA 0x344F4758 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Number of secondary paths。

[条件 C-61ee179365919407](../../evidence/conditions-sets-038.md#c-61ee179365919407) · [缺口 G-19a9bd177250c456](../../evidence/gaps-sets-001.md#g-19a9bd177250c456) · [参数 P-20172f83589f021e](../../evidence/parameters-sets-003.md#p-20172f83589f021e)

### observed_connections-001584

```text
(config-router-scope-af)# metric holddown <cr>
```

Handler ` RVA 0xE1F32D0 `；selector ` 1 `；EOL ` RVA 0x344F3AF0 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4bbe96da81617452](../../evidence/conditions-sets-030.md#c-4bbe96da81617452)

### observed_connections-001539

```text
(config-router-scope-af)# metric maximum-hops <number:1..255> <cr>
```

Handler ` RVA 0xE1F32D0 `；selector ` 2 `；EOL ` RVA 0x344F3B18 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Hop count。

[条件 C-4f06080100d9aa31](../../evidence/conditions-sets-031.md#c-4f06080100d9aa31) · [参数 P-ade92f03be8d75a4](../../evidence/parameters-sets-013.md#p-ade92f03be8d75a4)

### observed_connections-001902

```text
(config-router-scope-af)# metric weights <number:0..8> <number:0..255> <number:0..255> <number:0..255> <number:0..255> <number:0..255> <cr>
```

Handler ` RVA 0xE1F32D0 `；selector ` 0 `；EOL ` RVA 0x344F40D8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Type Of Service (Only TOS 0 supported)；` unsigned_number ` K1；` unsigned_number ` K2；` unsigned_number ` K3；` unsigned_number ` K4；` unsigned_number ` K5。

[条件 C-d7dd7842e679d454](../../evidence/conditions-sets-083.md#c-d7dd7842e679d454) · [参数 P-814573c6aff87ec0](../../evidence/parameters-sets-010.md#p-814573c6aff87ec0)

### observed_connections-001907

```text
(config-router-scope-af)# neighbor <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 0 `；EOL ` RVA 0x344FAE30 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-13bab7a73be6995a](../../evidence/conditions-sets-008.md#c-13bab7a73be6995a) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001909

```text
(config-router-scope-af)# neighbor <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 0 `；EOL ` RVA 0x34514EB0 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1c96f9a1eaa0749d](../../evidence/conditions-sets-011.md#c-1c96f9a1eaa0749d) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001942

```text
(config-router-scope-af)# neighbor accept-route-legacy-rt <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 71 `；EOL ` RVA 0x3450FCA0 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-60e9cf81e8aa848e](../../evidence/conditions-sets-038.md#c-60e9cf81e8aa848e) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001948

```text
(config-router-scope-af)# neighbor activate <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 35 `；EOL ` RVA 0x34512F58 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ad8ccca0d04a9c9e](../../evidence/conditions-sets-067.md#c-ad8ccca0d04a9c9e) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001945

```text
(config-router-scope-af)# neighbor additional-paths <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 79 `；EOL ` RVA 0x34510680 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c21872e8d31dd697](../../evidence/conditions-sets-075.md#c-c21872e8d31dd697) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-310f72b0202c01f0](../../evidence/state_effects-sets-011.md#s-310f72b0202c01f0)

### observed_connections-001976

```text
(config-router-scope-af)# neighbor advertise additional-paths <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 78 `；EOL ` RVA 0x34510D88 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-192897edda681854](../../evidence/conditions-sets-010.md#c-192897edda681854) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-f5e7703a312d3e8e](../../evidence/state_effects-sets-052.md#s-f5e7703a312d3e8e)

### observed_connections-001974

```text
(config-router-scope-af)# neighbor advertise best-external <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 80 `；EOL ` RVA 0x34511438 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e02361fb7eb19d65](../../evidence/conditions-sets-086.md#c-e02361fb7eb19d65) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-002000

```text
(config-router-scope-af)# neighbor advertise diverse-path mpath <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 78 `；EOL ` RVA 0x34511158 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e02361fb7eb19d65](../../evidence/conditions-sets-086.md#c-e02361fb7eb19d65) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-bb007f0b56515910](../../evidence/state_effects-sets-039.md#s-bb007f0b56515910)

### observed_connections-001956

```text
(config-router-scope-af)# neighbor advertise-gw-ip-disable <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 88 `；EOL ` RVA 0x34517350 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-919986923aaf465d](../../evidence/conditions-sets-056.md#c-919986923aaf465d) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-002004

```text
(config-router-scope-af)# neighbor advertise-map <string> non-exist-map <string> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 39 `；EOL ` RVA 0x34513788 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` advertise route-map name；` string ` condition route-map name。

[条件 C-f0f800ded2b1c519](../../evidence/conditions-sets-093.md#c-f0f800ded2b1c519) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [参数 P-5700454f0b4c63c1](../../evidence/parameters-sets-007.md#p-5700454f0b4c63c1) · [状态效果 S-beeff3187c70c5dc](../../evidence/state_effects-sets-040.md#s-beeff3187c70c5dc)

### observed_connections-001933

```text
(config-router-scope-af)# neighbor advertisement-interval <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 40 `；EOL ` RVA 0x3450B210 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-197ad609ce2b0755](../../evidence/conditions-sets-010.md#c-197ad609ce2b0755) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001943

```text
(config-router-scope-af)# neighbor aigp <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 50 `；EOL ` RVA 0x3450F8A0 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d24ccc0a4da823d3](../../evidence/conditions-sets-081.md#c-d24ccc0a4da823d3) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-77488c72b6e8ed60](../../evidence/state_effects-sets-025.md#s-77488c72b6e8ed60)

### observed_connections-001944

```text
(config-router-scope-af)# neighbor allow-policy <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 51 `；EOL ` RVA 0x345102D0 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-171e78d3b71fbcbf](../../evidence/conditions-sets-009.md#c-171e78d3b71fbcbf) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001929

```text
(config-router-scope-af)# neighbor allowas-in <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 60 `；EOL ` RVA 0x34509FA8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8f00fb7563a28c95](../../evidence/conditions-sets-055.md#c-8f00fb7563a28c95) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001994

```text
(config-router-scope-af)# neighbor announce rpki state <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 77 `；EOL ` RVA 0x3450A798 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e691aedb1d2d97bd](../../evidence/conditions-sets-089.md#c-e691aedb1d2d97bd) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001980

```text
(config-router-scope-af)# neighbor ao <string> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 22 `；EOL ` RVA 0x345163A0 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Keychain name。

[条件 C-a2611dcb8d2ee112](../../evidence/conditions-sets-063.md#c-a2611dcb8d2ee112) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [参数 P-da5db2abf7b4d80d](../../evidence/parameters-sets-016.md#p-da5db2abf7b4d80d) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001951

```text
(config-router-scope-af)# neighbor as-override <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 61 `；EOL ` RVA 0x34514238 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c8ab98fc01ef13fe](../../evidence/conditions-sets-077.md#c-c8ab98fc01ef13fe) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-002005

```text
(config-router-scope-af)# neighbor capability orf prefix-list send <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 65 `；EOL ` RVA 0x34514680 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8b97c64536681f4e](../../evidence/conditions-sets-054.md#c-8b97c64536681f4e) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-bc48cf26c3524396](../../evidence/state_effects-sets-040.md#s-bc48cf26c3524396)

### observed_connections-001953

```text
(config-router-scope-af)# neighbor cluster-id <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 23 `；EOL ` RVA 0x34516768 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6ea8a4d8120fe344](../../evidence/conditions-sets-043.md#c-6ea8a4d8120fe344) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001938

```text
(config-router-scope-af)# neighbor default-originate <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 52 `；EOL ` RVA 0x3450DCD0 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-232002e2b94e88a8](../../evidence/conditions-sets-014.md#c-232002e2b94e88a8) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001947

```text
(config-router-scope-af)# neighbor description <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 8 `；EOL ` RVA 0x34512C20 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e88517045e0c013f](../../evidence/conditions-sets-090.md#c-e88517045e0c013f) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001927

```text
(config-router-scope-af)# neighbor disable-connected-check <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 13 `；EOL ` RVA 0x34509318 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-10dd06267d084e20](../../evidence/conditions-sets-007.md#c-10dd06267d084e20) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-9f0d6cbe68a958da](../../evidence/state_effects-sets-034.md#s-9f0d6cbe68a958da)

### observed_connections-001990

```text
(config-router-scope-af)# neighbor distribute-list <number:1..199> in <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 45 `；EOL ` RVA 0x345064A0 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` IP access list number。

[条件 C-d9c9086da3f4ebe4](../../evidence/conditions-sets-084.md#c-d9c9086da3f4ebe4) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [参数 P-0797f33209a82d83](../../evidence/parameters-sets-001.md#p-0797f33209a82d83) · [状态效果 S-abc7de4585cab362](../../evidence/state_effects-sets-036.md#s-abc7de4585cab362)

### observed_connections-001925

```text
(config-router-scope-af)# neighbor dmzlink-bw <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 63 `；EOL ` RVA 0x34507DA0 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8571c652afdb9a9f](../../evidence/conditions-sets-052.md#c-8571c652afdb9a9f) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-cccb14bcb9ec38cb](../../evidence/state_effects-sets-043.md#s-cccb14bcb9ec38cb)

### observed_connections-001922

```text
(config-router-scope-af)# neighbor dont-capability-negotiate <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 16 `；EOL ` RVA 0x34505060 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e58430b9c4f0f9ae](../../evidence/conditions-sets-089.md#c-e58430b9c4f0f9ae) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001962

```text
(config-router-scope-af)# neighbor dont-capability-negotiate enhanced-refresh <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 18 `；EOL ` RVA 0x34505038 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e58430b9c4f0f9ae](../../evidence/conditions-sets-089.md#c-e58430b9c4f0f9ae) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001960

```text
(config-router-scope-af)# neighbor dont-capability-negotiate four-octets-as <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 17 `；EOL ` RVA 0x34504D90 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e58430b9c4f0f9ae](../../evidence/conditions-sets-089.md#c-e58430b9c4f0f9ae) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001937

```text
(config-router-scope-af)# neighbor ebgp-multihop <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 6 `；EOL ` RVA 0x3450D8A8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-77b29bcbf6938ac1](../../evidence/conditions-sets-047.md#c-77b29bcbf6938ac1) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-147c8497d59aab13](../../evidence/state_effects-sets-005.md#s-147c8497d59aab13)

### observed_connections-001981

```text
(config-router-scope-af)# neighbor encap srv6 <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 86 `；EOL ` RVA 0x34517778 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4cd15865852f0942](../../evidence/conditions-sets-030.md#c-4cd15865852f0942) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-ce3e01bc3a1db752](../../evidence/state_effects-sets-044.md#s-ce3e01bc3a1db752)

### observed_connections-001930

```text
(config-router-scope-af)# neighbor fall-over <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 26 `；EOL ` RVA 0x34509670 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-03fa6bb6e2648f91](../../evidence/conditions-sets-002.md#c-03fa6bb6e2648f91) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-ea869f48fdbad9a6](../../evidence/state_effects-sets-050.md#s-ea869f48fdbad9a6)

### observed_connections-001993

```text
(config-router-scope-af)# neighbor filter-list <number:1..500> in <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 44 `；EOL ` RVA 0x34507280 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` AS path access list。

[条件 C-eeeedb84ea6e6a17](../../evidence/conditions-sets-092.md#c-eeeedb84ea6e6a17) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [参数 P-32386b885f3a56a1](../../evidence/parameters-sets-004.md#p-32386b885f3a56a1) · [状态效果 S-30faed4ccbccec2e](../../evidence/state_effects-sets-011.md#s-30faed4ccbccec2e)

### observed_connections-001921

```text
(config-router-scope-af)# neighbor force-open-collision <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 15 `；EOL ` RVA 0x345055F0 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-289a431576c5a2de](../../evidence/conditions-sets-016.md#c-289a431576c5a2de) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001983

```text
(config-router-scope-af)# neighbor ha-mode graceful-restart <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 28 `；EOL ` RVA 0x344FB150 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7e41f7d7f62c88c6](../../evidence/conditions-sets-049.md#c-7e41f7d7f62c88c6) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001984

```text
(config-router-scope-af)# neighbor ha-mode sso <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 29 `；EOL ` RVA 0x3372E478 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7e41f7d7f62c88c6](../../evidence/conditions-sets-049.md#c-7e41f7d7f62c88c6) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001999

```text
(config-router-scope-af)# neighbor inherit peer-policy <string> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 36 `；EOL ` RVA 0x345118B0 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Template name。

[条件 C-cbdd0eedb1248b5c](../../evidence/conditions-sets-078.md#c-cbdd0eedb1248b5c) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [参数 P-830038faf9dd3fd6](../../evidence/parameters-sets-010.md#p-830038faf9dd3fd6) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001998

```text
(config-router-scope-af)# neighbor inherit peer-session <string> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 19 `；EOL ` RVA 0x34511BC8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Template name。

[条件 C-c0ab4d89634c404f](../../evidence/conditions-sets-074.md#c-c0ab4d89634c404f) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [参数 P-0e28cc940f3097c3](../../evidence/parameters-sets-002.md#p-0e28cc940f3097c3) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001940

```text
(config-router-scope-af)# neighbor inter-as-hybrid <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 72 `；EOL ` RVA 0x3450F280 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-225a9309aed7568c](../../evidence/conditions-sets-013.md#c-225a9309aed7568c) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001950

```text
(config-router-scope-af)# neighbor internal-vpn-client <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 82 `；EOL ` RVA 0x34513E80 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-358884266787c0b1](../../evidence/conditions-sets-021.md#c-358884266787c0b1) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001928

```text
(config-router-scope-af)# neighbor local-as <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 11 `；EOL ` RVA 0x34508EA0 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a3c15a1e7ce2c66b](../../evidence/conditions-sets-063.md#c-a3c15a1e7ce2c66b) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001957

```text
(config-router-scope-af)# neighbor log-neighbor-changes <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 32 `；EOL ` RVA 0x34517FB0 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6404bb904798fc4d](../../evidence/conditions-sets-039.md#c-6404bb904798fc4d) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001955

```text
(config-router-scope-af)# neighbor long-lived-graceful-restart <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 85 `；EOL ` RVA 0x34516B88 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9d9516f08ea397fc](../../evidence/conditions-sets-061.md#c-9d9516f08ea397fc) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001975

```text
(config-router-scope-af)# neighbor maximum-prefix <number:1..2147483647> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 59 `；EOL ` RVA 0x34512728 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` maximum no. of prefix limit。

[条件 C-3d591c7f1e356b3f](../../evidence/conditions-sets-024.md#c-3d591c7f1e356b3f) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [参数 P-13ee3dfd3e93b318](../../evidence/parameters-sets-002.md#p-13ee3dfd3e93b318) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001935

```text
(config-router-scope-af)# neighbor next-hop-self <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 42 `；EOL ` RVA 0x3450C478 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f4351305e1c4a797](../../evidence/conditions-sets-094.md#c-f4351305e1c4a797) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001936

```text
(config-router-scope-af)# neighbor next-hop-unchanged <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 43 `；EOL ` RVA 0x3450D538 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1b0c1fcf5f3d086e](../../evidence/conditions-sets-011.md#c-1b0c1fcf5f3d086e) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001964

```text
(config-router-scope-af)# neighbor orf rt-import-list <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 70 `；EOL ` RVA 0x34506E60 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ab835ca27d439164](../../evidence/conditions-sets-066.md#c-ab835ca27d439164) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-6317e372b48e554b](../../evidence/state_effects-sets-021.md#s-6317e372b48e554b)

### observed_connections-001923

```text
(config-router-scope-af)# neighbor override-capability-neg <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 62 `；EOL ` RVA 0x345060B8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1e3df669ab0e3cf9](../../evidence/conditions-sets-012.md#c-1e3df669ab0e3cf9) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001946

```text
(config-router-scope-af)# neighbor password <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 7 `；EOL ` RVA 0x345122E0 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b85fedd316c09ae8](../../evidence/conditions-sets-071.md#c-b85fedd316c09ae8) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-002006

```text
(config-router-scope-af)# neighbor path-attribute treat-as-withdraw <number:1..255> in <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 27 `；EOL ` RVA 0x34515B80 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` path attribute type。

[条件 C-f6dcf8eb5c721af0](../../evidence/conditions-sets-095.md#c-f6dcf8eb5c721af0) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [参数 P-72a458c8c3022acf](../../evidence/parameters-sets-009.md#p-72a458c8c3022acf) · [状态效果 S-4ac3f2ec2d52db64](../../evidence/state_effects-sets-016.md#s-4ac3f2ec2d52db64)

### observed_connections-001920

```text
(config-router-scope-af)# neighbor peer-group <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 10 `；EOL ` RVA 0x344E0C38 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8e4c55852a704b71](../../evidence/conditions-sets-055.md#c-8e4c55852a704b71) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001973

```text
(config-router-scope-af)# neighbor peer-group <string> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 20 `；EOL ` RVA 0x34511F48 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` peer-group name。

[条件 C-6e258b24e0760038](../../evidence/conditions-sets-043.md#c-6e258b24e0760038) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [参数 P-52dda26f99b7df22](../../evidence/parameters-sets-007.md#p-52dda26f99b7df22) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001965

```text
(config-router-scope-af)# neighbor prefix-length-size <number:1..2> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 68 `；EOL ` RVA 0x34507A60 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Storage size in bytes。

[条件 C-cdd2e851f00d0e15](../../evidence/conditions-sets-079.md#c-cdd2e851f00d0e15) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [参数 P-a6116061aef9ac47](../../evidence/parameters-sets-013.md#p-a6116061aef9ac47) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001991

```text
(config-router-scope-af)# neighbor prefix-list <string> in <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 58 `；EOL ` RVA 0x34506988 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Name of a prefix list。

[条件 C-35994091da99805d](../../evidence/conditions-sets-021.md#c-35994091da99805d) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [参数 P-d19b4dab0d5c54fd](../../evidence/parameters-sets-016.md#p-d19b4dab0d5c54fd) · [状态效果 S-5405f3edeff72c73](../../evidence/state_effects-sets-018.md#s-5405f3edeff72c73)

### observed_connections-001926

```text
(config-router-scope-af)# neighbor remote-as <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 3 `；EOL ` RVA 0x34508488 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-160911c41469c892](../../evidence/conditions-sets-009.md#c-160911c41469c892) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001939

```text
(config-router-scope-af)# neighbor remove-private-as <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 55 `；EOL ` RVA 0x3450EA48 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3c15e60adcaa6f3e](../../evidence/conditions-sets-023.md#c-3c15e60adcaa6f3e) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001972

```text
(config-router-scope-af)# neighbor remove-private-as all <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 56 `；EOL ` RVA 0x3450EAB0 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8060cd7582c05ee1](../../evidence/conditions-sets-050.md#c-8060cd7582c05ee1) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001997

```text
(config-router-scope-af)# neighbor remove-private-as all replace-as <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 57 `；EOL ` RVA 0x3450EA88 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8060cd7582c05ee1](../../evidence/conditions-sets-050.md#c-8060cd7582c05ee1) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001992

```text
(config-router-scope-af)# neighbor route-map <string> in <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 47 `；EOL ` RVA 0x34507670 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Name of route map。

[条件 C-fc219d4e34260c06](../../evidence/conditions-sets-097.md#c-fc219d4e34260c06) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [参数 P-56a31330bb3dc696](../../evidence/parameters-sets-007.md#p-56a31330bb3dc696) · [状态效果 S-53f0ef09cb1c2df4](../../evidence/state_effects-sets-018.md#s-53f0ef09cb1c2df4)

### observed_connections-001941

```text
(config-router-scope-af)# neighbor route-reflector-client <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 49 `；EOL ` RVA 0x3450FF98 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-283381432d5aa003](../../evidence/conditions-sets-016.md#c-283381432d5aa003) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001932

```text
(config-router-scope-af)# neighbor send-community <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 46 `；EOL ` RVA 0x3450B9A8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c4aa87ec4762d0be](../../evidence/conditions-sets-076.md#c-c4aa87ec4762d0be) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001952

```text
(config-router-scope-af)# neighbor send-label <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 64 `；EOL ` RVA 0x34514B80 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b6f81c4e0bd5f8f5](../../evidence/conditions-sets-071.md#c-b6f81c4e0bd5f8f5) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001934

```text
(config-router-scope-af)# neighbor shutdown <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 5 `；EOL ` RVA 0x3450BE48 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ba483e96460a8055](../../evidence/conditions-sets-072.md#c-ba483e96460a8055) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001967

```text
(config-router-scope-af)# neighbor slow-peer detection <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 74 `；EOL ` RVA 0x3450CEF8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8f419973a82cf608](../../evidence/conditions-sets-055.md#c-8f419973a82cf608) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001968

```text
(config-router-scope-af)# neighbor slow-peer detection threshold <number:120..3600> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 74 `；EOL ` RVA 0x3450CF20 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Threshold value (seconds)。

[条件 C-839813b7d3861e3a](../../evidence/conditions-sets-051.md#c-839813b7d3861e3a) · [缺口 G-d75e16e85957f327](../../evidence/gaps-sets-007.md#g-d75e16e85957f327) · [参数 P-d3f734109cb70ab9](../../evidence/parameters-sets-016.md#p-d3f734109cb70ab9) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001996

```text
(config-router-scope-af)# neighbor slow-peer split-update-group dynamic <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 75 `；EOL ` RVA 0x3450CB80 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-df6254f59b5e0e20](../../evidence/conditions-sets-086.md#c-df6254f59b5e0e20) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001995

```text
(config-router-scope-af)# neighbor slow-peer split-update-group static <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 73 `；EOL ` RVA 0x3450C870 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4c959e4f28cdc8d7](../../evidence/conditions-sets-030.md#c-4c959e4f28cdc8d7) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001969

```text
(config-router-scope-af)# neighbor soft-reconfiguration inbound <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 54 `；EOL ` RVA 0x3450E068 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-86b9f1025a6fe26b](../../evidence/conditions-sets-052.md#c-86b9f1025a6fe26b) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-002011

```text
(config-router-scope-af)# neighbor soo <?bgp_extcomm_action@555589a5e320> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 69 `；EOL ` RVA 0x3450A368 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5b99992805d4b839](../../evidence/conditions-sets-036.md#c-5b99992805d4b839) · [缺口 G-0e8803a0f852e018](../../evidence/gaps-sets-001.md#g-0e8803a0f852e018) · [状态效果 S-363077405b04bf7a](../../evidence/state_effects-sets-012.md#s-363077405b04bf7a)

### observed_connections-001982

```text
(config-router-scope-af)# neighbor suppress-signaling-protocol ldp <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 81 `；EOL ` RVA 0x34517C70 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-325133a1bc3a6989](../../evidence/conditions-sets-020.md#c-325133a1bc3a6989) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001954

```text
(config-router-scope-af)# neighbor suppress-sr <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 87 `；EOL ` RVA 0x34517018 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-05db0ec610947357](../../evidence/conditions-sets-003.md#c-05db0ec610947357) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001949

```text
(config-router-scope-af)# neighbor timers <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 9 `；EOL ` RVA 0x345132B8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1db3879e1ea8e79e](../../evidence/conditions-sets-012.md#c-1db3879e1ea8e79e) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001961

```text
(config-router-scope-af)# neighbor translate-topology <number:1..4095> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 67 `；EOL ` RVA 0x34504A50 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Topology id。

[条件 C-36e4d1058431fe3e](../../evidence/conditions-sets-021.md#c-36e4d1058431fe3e) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [参数 P-29a580b5da5dc57a](../../evidence/parameters-sets-004.md#p-29a580b5da5dc57a) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001924

```text
(config-router-scope-af)# neighbor translate-update <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 66 `；EOL ` RVA 0x34505A50 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c41cc4f8d386df01](../../evidence/conditions-sets-076.md#c-c41cc4f8d386df01) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-0fe63544651cb37c](../../evidence/state_effects-sets-004.md#s-0fe63544651cb37c)

### observed_connections-001979

```text
(config-router-scope-af)# neighbor transport multi-session <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 25 `；EOL ` RVA 0x345155F8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5106ca4ee508f037](../../evidence/conditions-sets-032.md#c-5106ca4ee508f037) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-2a6f12fd310e73f0](../../evidence/state_effects-sets-010.md#s-2a6f12fd310e73f0)

### observed_connections-001978

```text
(config-router-scope-af)# neighbor transport path-mtu-discovery <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 24 `；EOL ` RVA 0x34515250 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5106ca4ee508f037](../../evidence/conditions-sets-032.md#c-5106ca4ee508f037) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-6a83e9fd912e972f](../../evidence/state_effects-sets-023.md#s-6a83e9fd912e972f)

### observed_connections-002001

```text
(config-router-scope-af)# neighbor ttl-security hops <number:1..254> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 21 `；EOL ` RVA 0x34515F88 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` maximum number of hops。

[条件 C-07c9f5416d843d09](../../evidence/conditions-sets-003.md#c-07c9f5416d843d09) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [参数 P-8cc2c830fd88076d](../../evidence/parameters-sets-011.md#p-8cc2c830fd88076d) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001966

```text
(config-router-scope-af)# neighbor unsuppress-map <string> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 53 `；EOL ` RVA 0x34508128 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Name of route map。

[条件 C-8e141e8fa6af9f28](../../evidence/conditions-sets-055.md#c-8e141e8fa6af9f28) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [参数 P-223c6e11c8568fdf](../../evidence/parameters-sets-003.md#p-223c6e11c8568fdf) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-002007

```text
(config-router-scope-af)# neighbor update in labeled-unicast unique <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 33 `；EOL ` RVA 0x345183D0 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4d8b718999425ead](../../evidence/conditions-sets-030.md#c-4d8b718999425ead) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-7cd551f1b064b514](../../evidence/state_effects-sets-026.md#s-7cd551f1b064b514)

### observed_connections-002012

```text
(config-router-scope-af)# neighbor update-source <interface> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 4 `；EOL ` RVA 0x3450B630 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9125e9a3c7bdde78](../../evidence/conditions-sets-056.md#c-9125e9a3c7bdde78) · [缺口 G-8daaf47d527eeec2](../../evidence/gaps-sets-005.md#g-8daaf47d527eeec2) · [参数 P-61fcc75034c55454](../../evidence/parameters-sets-008.md#p-61fcc75034c55454) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001977

```text
(config-router-scope-af)# neighbor use nexthop-attribute <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 37 `；EOL ` RVA 0x34513B40 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3be006df4c76bad6](../../evidence/conditions-sets-023.md#c-3be006df4c76bad6) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001970

```text
(config-router-scope-af)# neighbor validation off <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 83 `；EOL ` RVA 0x3450E3E8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-943c3e0115be4042](../../evidence/conditions-sets-057.md#c-943c3e0115be4042) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001971

```text
(config-router-scope-af)# neighbor validation redirect-off <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 84 `；EOL ` RVA 0x3450E690 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-943c3e0115be4042](../../evidence/conditions-sets-057.md#c-943c3e0115be4042) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001908

```text
(config-router-scope-af)# neighbor version <number:4..4> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 2 `；EOL ` RVA 0x3450AA40 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Neighbor's BGP version。

[条件 C-ddbd536532a30941](../../evidence/conditions-sets-085.md#c-ddbd536532a30941) · [缺口 G-42095c11b6c3a7a5](../../evidence/gaps-sets-003.md#g-42095c11b6c3a7a5) · [参数 P-db3efca0f5fa5dad](../../evidence/parameters-sets-017.md#p-db3efca0f5fa5dad) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001931

```text
(config-router-scope-af)# neighbor weight <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 41 `；EOL ` RVA 0x3450AE38 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-033cebca76205d75](../../evidence/conditions-sets-002.md#c-033cebca76205d75) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001917

```text
(config-router-scope-af)# network <address> <cr>
```

Handler ` RVA 0xF190B70 `；selector ` 0 `；EOL ` RVA 0x34552598 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` NSAP prefix。

[条件 C-3c02634e58ae02c7](../../evidence/conditions-sets-023.md#c-3c02634e58ae02c7) · [缺口 G-76736370463c18bc](../../evidence/gaps-sets-005.md#g-76736370463c18bc) · [参数 P-c0df855611dc1e77](../../evidence/parameters-sets-015.md#p-c0df855611dc1e77) · [状态效果 S-2b12435d203b332f](../../evidence/state_effects-sets-010.md#s-2b12435d203b332f)

### observed_connections-002010

```text
(config-router-scope-af)# network <address> <cr>
```

Handler ` RVA 0xE1E04C0 `；selector ` 0 `；EOL ` RVA 0x344F3258 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Network number。

[条件 C-1fa7aa820c5ad426](../../evidence/conditions-sets-012.md#c-1fa7aa820c5ad426) · [缺口 G-05cb3d1521972458](../../evidence/gaps-sets-001.md#g-05cb3d1521972458) · [参数 P-bc5dfd89d0bbefc6](../../evidence/parameters-sets-014.md#p-bc5dfd89d0bbefc6) · [状态效果 S-cf0dcd14c69eda70](../../evidence/state_effects-sets-044.md#s-cf0dcd14c69eda70)

### observed_connections-001799

```text
(config-router-scope-af)# no aggregate-address <address> <address> <cr>
```

Handler ` RVA 0xF1B7BE0 `；selector ` 0 `；EOL ` RVA 0x34552F40 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` Aggregate address；` address ` Aggregate mask。

[条件 C-f7ab9ff3c35afc8e](../../evidence/conditions-sets-096.md#c-f7ab9ff3c35afc8e) · [参数 P-9fe0ddf3e4cc9517](../../evidence/parameters-sets-012.md#p-9fe0ddf3e4cc9517) · [状态效果 S-474e4f29337dcd92](../../evidence/state_effects-sets-016.md#s-474e4f29337dcd92)

### observed_connections-001600

```text
(config-router-scope-af)# no auto-summary <cr>
```

Handler ` RVA 0xE1FA6B0 `；selector ` 0 `；EOL ` RVA 0x344F7B28 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-892cb3702bd56b94](../../evidence/conditions-sets-053.md#c-892cb3702bd56b94) · [状态效果 S-474e4f29337dcd92](../../evidence/state_effects-sets-016.md#s-474e4f29337dcd92)

### observed_connections-001786

```text
(config-router-scope-af)# no bgp additional-paths install <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 69 `；EOL ` RVA 0x3454A798 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8586360bd6d1b906](../../evidence/conditions-sets-052.md#c-8586360bd6d1b906) · [状态效果 S-df07f3bcc3daa53a](../../evidence/state_effects-sets-047.md#s-df07f3bcc3daa53a)

### observed_connections-001795

```text
(config-router-scope-af)# no bgp additional-paths select <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 71 `；EOL ` RVA 0x3454A440 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0982d1ddadb45b04](../../evidence/conditions-sets-004.md#c-0982d1ddadb45b04) · [状态效果 S-474e4f29337dcd92](../../evidence/state_effects-sets-016.md#s-474e4f29337dcd92)

### observed_connections-001663

```text
(config-router-scope-af)# no bgp advertise-best-external <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 70 `；EOL ` RVA 0x3454B5E8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-57bb992185c04f5b](../../evidence/conditions-sets-034.md#c-57bb992185c04f5b) · [状态效果 S-474e4f29337dcd92](../../evidence/state_effects-sets-016.md#s-474e4f29337dcd92)

### observed_connections-001717

```text
(config-router-scope-af)# no bgp advertisement startup-delay <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 95 `；EOL ` RVA 0x34543458 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a4b6ac0490741a56](../../evidence/conditions-sets-063.md#c-a4b6ac0490741a56) · [状态效果 S-474e4f29337dcd92](../../evidence/state_effects-sets-016.md#s-474e4f29337dcd92)

### observed_connections-001796

```text
(config-router-scope-af)# no bgp aggregate-timer <number:6..60> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 58 `；EOL ` RVA 0x34551638 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Timer interval。

[条件 C-e75e44fc50bad466](../../evidence/conditions-sets-089.md#c-e75e44fc50bad466) · [参数 P-2e3330fde6070f01](../../evidence/parameters-sets-004.md#p-2e3330fde6070f01) · [状态效果 S-474e4f29337dcd92](../../evidence/state_effects-sets-016.md#s-474e4f29337dcd92)

### observed_connections-001747

```text
(config-router-scope-af)# no bgp aigp-rib-metric <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 91 `；EOL ` RVA 0x34547ED8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f311201ce1b8ec9e](../../evidence/conditions-sets-094.md#c-f311201ce1b8ec9e) · [状态效果 S-474e4f29337dcd92](../../evidence/state_effects-sets-016.md#s-474e4f29337dcd92)

### observed_connections-001651

```text
(config-router-scope-af)# no bgp always-compare-med <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 5 `；EOL ` RVA 0x3453ED40 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d038dabf7ea3a128](../../evidence/conditions-sets-080.md#c-d038dabf7ea3a128) · [状态效果 S-474e4f29337dcd92](../../evidence/state_effects-sets-016.md#s-474e4f29337dcd92)

### observed_connections-001774

```text
(config-router-scope-af)# no bgp asnotation dot <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 64 `；EOL ` RVA 0x3453F050 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d038dabf7ea3a128](../../evidence/conditions-sets-080.md#c-d038dabf7ea3a128) · [状态效果 S-474e4f29337dcd92](../../evidence/state_effects-sets-016.md#s-474e4f29337dcd92)

### observed_connections-001883

```text
(config-router-scope-af)# no bgp bestpath aigp ignore <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 43 `；EOL ` RVA 0x34546C00 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d1964220dc649b09](../../evidence/conditions-sets-081.md#c-d1964220dc649b09) · [状态效果 S-474e4f29337dcd92](../../evidence/state_effects-sets-016.md#s-474e4f29337dcd92)

### observed_connections-001876

```text
(config-router-scope-af)# no bgp bestpath as-path ignore <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 17 `；EOL ` RVA 0x34546370 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f311201ce1b8ec9e](../../evidence/conditions-sets-094.md#c-f311201ce1b8ec9e) · [状态效果 S-474e4f29337dcd92](../../evidence/state_effects-sets-016.md#s-474e4f29337dcd92)

### observed_connections-001878

```text
(config-router-scope-af)# no bgp bestpath as-path multipath-relax <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 51 `；EOL ` RVA 0x34546618 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f311201ce1b8ec9e](../../evidence/conditions-sets-094.md#c-f311201ce1b8ec9e) · [状态效果 S-474e4f29337dcd92](../../evidence/state_effects-sets-016.md#s-474e4f29337dcd92)

### observed_connections-001829

```text
(config-router-scope-af)# no bgp bestpath compare-routerid <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 24 `；EOL ` RVA 0x345468B0 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f311201ce1b8ec9e](../../evidence/conditions-sets-094.md#c-f311201ce1b8ec9e) · [状态效果 S-474e4f29337dcd92](../../evidence/state_effects-sets-016.md#s-474e4f29337dcd92)

### observed_connections-001882

```text
(config-router-scope-af)# no bgp bestpath cost-community ignore <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 41 `；EOL ` RVA 0x34546ED8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f311201ce1b8ec9e](../../evidence/conditions-sets-094.md#c-f311201ce1b8ec9e) · [状态效果 S-474e4f29337dcd92](../../evidence/state_effects-sets-016.md#s-474e4f29337dcd92)

### observed_connections-001841

```text
(config-router-scope-af)# no bgp bestpath igp-metric ignore <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 42 `；EOL ` RVA 0x3454ACC8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-9eb32499553e628d](../../evidence/conditions-sets-061.md#c-9eb32499553e628d) · [状态效果 S-474e4f29337dcd92](../../evidence/state_effects-sets-016.md#s-474e4f29337dcd92)

### observed_connections-001879

```text
(config-router-scope-af)# no bgp bestpath med missing-as-worst <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 18 `；EOL ` RVA 0x34546060 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f311201ce1b8ec9e](../../evidence/conditions-sets-094.md#c-f311201ce1b8ec9e) · [状态效果 S-26490b37f4b6d682](../../evidence/state_effects-sets-009.md#s-26490b37f4b6d682)

### observed_connections-001847

```text
(config-router-scope-af)# no bgp bestpath prefix-validate allow-invalid <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 78 `；EOL ` RVA 0x3454AFD8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-6111a0a7e8a7ea86](../../evidence/conditions-sets-038.md#c-6111a0a7e8a7ea86) · [状态效果 S-474e4f29337dcd92](../../evidence/state_effects-sets-016.md#s-474e4f29337dcd92)

### observed_connections-001849

```text
(config-router-scope-af)# no bgp bestpath prefix-validate disable <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 77 `；EOL ` RVA 0x3454B280 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-6111a0a7e8a7ea86](../../evidence/conditions-sets-038.md#c-6111a0a7e8a7ea86) · [状态效果 S-474e4f29337dcd92](../../evidence/state_effects-sets-016.md#s-474e4f29337dcd92)

### observed_connections-001791

```text
(config-router-scope-af)# no bgp client-to-client reflection <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 9 `；EOL ` RVA 0x3453FEE0 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c76e7c8e33177186](../../evidence/conditions-sets-077.md#c-c76e7c8e33177186) · [状态效果 S-7fcbd9db87232469](../../evidence/state_effects-sets-027.md#s-7fcbd9db87232469)

### observed_connections-001676

```text
(config-router-scope-af)# no bgp cluster-id <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 7 `；EOL ` RVA 0x3453FAA8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-fa8255027dd1b9a7](../../evidence/conditions-sets-097.md#c-fa8255027dd1b9a7) · [状态效果 S-474e4f29337dcd92](../../evidence/state_effects-sets-016.md#s-474e4f29337dcd92)

### observed_connections-001686

```text
(config-router-scope-af)# no bgp consistency-checker <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 3 `；EOL ` RVA 0x3453F428 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-2f34adbbee3f06df](../../evidence/conditions-sets-018.md#c-2f34adbbee3f06df) · [状态效果 S-474e4f29337dcd92](../../evidence/state_effects-sets-016.md#s-474e4f29337dcd92)

### observed_connections-001653

```text
(config-router-scope-af)# no bgp dampening <cr>
```

Handler ` RVA 0xF1B85B0 `；selector ` 0 `；EOL ` RVA 0x34549860 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-958833730bc7b25e](../../evidence/conditions-sets-058.md#c-958833730bc7b25e) · [状态效果 S-474e4f29337dcd92](../../evidence/state_effects-sets-016.md#s-474e4f29337dcd92)

### observed_connections-001842

```text
(config-router-scope-af)# no bgp default inter-as-hybrid advertise-source-routes <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 57 `；EOL ` RVA 0x34548E98 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ec6dfe448cb8b3b0](../../evidence/conditions-sets-091.md#c-ec6dfe448cb8b3b0) · [状态效果 S-474e4f29337dcd92](../../evidence/state_effects-sets-016.md#s-474e4f29337dcd92)

### observed_connections-001764

```text
(config-router-scope-af)# no bgp default ipv4-unicast <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 19 `；EOL ` RVA 0x345485F0 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad3543d5e8c8e02b](../../evidence/conditions-sets-067.md#c-ad3543d5e8c8e02b) · [状态效果 S-474e4f29337dcd92](../../evidence/state_effects-sets-016.md#s-474e4f29337dcd92)

### observed_connections-001767

```text
(config-router-scope-af)# no bgp default ipv6-nexthop <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 75 `；EOL ` RVA 0x345488E8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4cf911d362de1ddd](../../evidence/conditions-sets-030.md#c-4cf911d362de1ddd) · [状态效果 S-474e4f29337dcd92](../../evidence/state_effects-sets-016.md#s-474e4f29337dcd92)

### observed_connections-001655

```text
(config-router-scope-af)# no bgp default local-preference <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 0 `；EOL ` RVA 0x34548B78 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1d4792eedfd8b981](../../evidence/conditions-sets-011.md#c-1d4792eedfd8b981) · [状态效果 S-474e4f29337dcd92](../../evidence/state_effects-sets-016.md#s-474e4f29337dcd92)

### observed_connections-001836

```text
(config-router-scope-af)# no bgp default route-target filter <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 25 `；EOL ` RVA 0x34549200 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-65e0de238ef95f31](../../evidence/conditions-sets-039.md#c-65e0de238ef95f31) · [状态效果 S-474e4f29337dcd92](../../evidence/state_effects-sets-016.md#s-474e4f29337dcd92)

### observed_connections-001837

```text
(config-router-scope-af)# no bgp default route-target filter <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 25 `；EOL ` RVA 0x345494A0 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0fb94622c94e5967](../../evidence/conditions-sets-006.md#c-0fb94622c94e5967) · [状态效果 S-474e4f29337dcd92](../../evidence/state_effects-sets-016.md#s-474e4f29337dcd92)

### observed_connections-001704

```text
(config-router-scope-af)# no bgp deterministic-med <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 10 `；EOL ` RVA 0x34541560 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d038dabf7ea3a128](../../evidence/conditions-sets-080.md#c-d038dabf7ea3a128) · [状态效果 S-474e4f29337dcd92](../../evidence/state_effects-sets-016.md#s-474e4f29337dcd92)

### observed_connections-001675

```text
(config-router-scope-af)# no bgp dmzlink-bw <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 31 `；EOL ` RVA 0x3454CB98 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e60672eeace3f616](../../evidence/conditions-sets-089.md#c-e60672eeace3f616) · [状态效果 S-474e4f29337dcd92](../../evidence/state_effects-sets-016.md#s-474e4f29337dcd92)

### observed_connections-001598

```text
(config-router-scope-af)# no bgp dynamic-med-interval <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 21 `；EOL ` RVA 0x34541588 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-9846d934a45ff2aa](../../evidence/conditions-sets-059.md#c-9846d934a45ff2aa) · [状态效果 S-474e4f29337dcd92](../../evidence/state_effects-sets-016.md#s-474e4f29337dcd92)

### observed_connections-001681

```text
(config-router-scope-af)# no bgp enforce-first-as <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 20 `；EOL ` RVA 0x34540790 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d038dabf7ea3a128](../../evidence/conditions-sets-080.md#c-d038dabf7ea3a128) · [状态效果 S-474e4f29337dcd92](../../evidence/state_effects-sets-016.md#s-474e4f29337dcd92)

### observed_connections-001719

```text
(config-router-scope-af)# no bgp enhanced-error <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 82 `；EOL ` RVA 0x345431D0 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-fe8044ca5f1d75ac](../../evidence/conditions-sets-098.md#c-fe8044ca5f1d75ac) · [状态效果 S-474e4f29337dcd92](../../evidence/state_effects-sets-016.md#s-474e4f29337dcd92)

### observed_connections-001637

```text
(config-router-scope-af)# no bgp fast-external-fallover <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 1 `；EOL ` RVA 0x3453E478 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d038dabf7ea3a128](../../evidence/conditions-sets-080.md#c-d038dabf7ea3a128) · [状态效果 S-474e4f29337dcd92](../../evidence/state_effects-sets-016.md#s-474e4f29337dcd92)

### observed_connections-001735

```text
(config-router-scope-af)# no bgp graceful-restart <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 35 `；EOL ` RVA 0x34544040 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d038dabf7ea3a128](../../evidence/conditions-sets-080.md#c-d038dabf7ea3a128) · [状态效果 S-474e4f29337dcd92](../../evidence/state_effects-sets-016.md#s-474e4f29337dcd92)

### observed_connections-001725

```text
(config-router-scope-af)# no bgp graceful-restart restart-time <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 36 `；EOL ` RVA 0x34543A10 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-258c387f51a1d7ce](../../evidence/conditions-sets-015.md#c-258c387f51a1d7ce) · [状态效果 S-474e4f29337dcd92](../../evidence/state_effects-sets-016.md#s-474e4f29337dcd92)

### observed_connections-001730

```text
(config-router-scope-af)# no bgp graceful-restart stalepath-time <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 37 `；EOL ` RVA 0x34543A78 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8d73d81d3f3ac40c](../../evidence/conditions-sets-055.md#c-8d73d81d3f3ac40c) · [状态效果 S-474e4f29337dcd92](../../evidence/state_effects-sets-016.md#s-474e4f29337dcd92)

### observed_connections-001900

```text
(config-router-scope-af)# no bgp graceful-shutdown all vrfs activate <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 79 `；EOL ` RVA 0x345444A8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-66f3816b6a249c29](../../evidence/conditions-sets-040.md#c-66f3816b6a249c29) · [状态效果 S-f806ba40dd17b671](../../evidence/state_effects-sets-052.md#s-f806ba40dd17b671)

### observed_connections-001898

```text
(config-router-scope-af)# no bgp inject-map <string> exist-map <string> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 32 `；EOL ` RVA 0x3454E710 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` route-map name；` string ` route-map name。

[条件 C-f8673071a7ce23a7](../../evidence/conditions-sets-096.md#c-f8673071a7ce23a7) · [参数 P-72ba39e577f273d6](../../evidence/parameters-sets-009.md#p-72ba39e577f273d6) · [状态效果 S-474e4f29337dcd92](../../evidence/state_effects-sets-016.md#s-474e4f29337dcd92)

### observed_connections-001835

```text
(config-router-scope-af)# no bgp label-allocation-batch <number:0..4294967295> <number:0..4294967295> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 53 `；EOL ` RVA 0x3453E808 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Timer value in milliseconds；` unsigned_number ` Batch Size。

[条件 C-d038dabf7ea3a128](../../evidence/conditions-sets-080.md#c-d038dabf7ea3a128) · [参数 P-675aa1ff414c4c13](../../evidence/parameters-sets-008.md#p-675aa1ff414c4c13) · [状态效果 S-474e4f29337dcd92](../../evidence/state_effects-sets-016.md#s-474e4f29337dcd92)

### observed_connections-001859

```text
(config-router-scope-af)# no bgp listen block <address> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 93 `；EOL ` RVA 0x3454C5A8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` IPv4 Dynamic Peering Address。

[条件 C-88fc52820904d643](../../evidence/conditions-sets-053.md#c-88fc52820904d643) · [参数 P-d42b5fda11d4d375](../../evidence/parameters-sets-016.md#p-d42b5fda11d4d375) · [状态效果 S-474e4f29337dcd92](../../evidence/state_effects-sets-016.md#s-474e4f29337dcd92)

### observed_connections-001872

```text
(config-router-scope-af)# no bgp listen block <address> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 93 `；EOL ` RVA 0x34542508 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` IPv4 Dynamic Peering Address。

[条件 C-9af955235c91b53a](../../evidence/conditions-sets-060.md#c-9af955235c91b53a) · [参数 P-3fcb738a2abc9e2d](../../evidence/parameters-sets-005.md#p-3fcb738a2abc9e2d) · [状态效果 S-474e4f29337dcd92](../../evidence/state_effects-sets-016.md#s-474e4f29337dcd92)

### observed_connections-001692

```text
(config-router-scope-af)# no bgp listen limit <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 61 `；EOL ` RVA 0x3454C4F0 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a1df8462dd54d10c](../../evidence/conditions-sets-063.md#c-a1df8462dd54d10c) · [状态效果 S-474e4f29337dcd92](../../evidence/state_effects-sets-016.md#s-474e4f29337dcd92)

### observed_connections-001721

```text
(config-router-scope-af)# no bgp listen limit <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 61 `；EOL ` RVA 0x34542428 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-23d23a5efd0b8f90](../../evidence/conditions-sets-014.md#c-23d23a5efd0b8f90) · [状态效果 S-474e4f29337dcd92](../../evidence/state_effects-sets-016.md#s-474e4f29337dcd92)

### observed_connections-001813

```text
(config-router-scope-af)# no bgp listen persistent <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 94 `；EOL ` RVA 0x34542840 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-9af955235c91b53a](../../evidence/conditions-sets-060.md#c-9af955235c91b53a) · [状态效果 S-474e4f29337dcd92](../../evidence/state_effects-sets-016.md#s-474e4f29337dcd92)

### observed_connections-001689

```text
(config-router-scope-af)# no bgp log-neighbor-changes <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 11 `；EOL ` RVA 0x34540A38 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d038dabf7ea3a128](../../evidence/conditions-sets-080.md#c-d038dabf7ea3a128) · [状态效果 S-474e4f29337dcd92](../../evidence/state_effects-sets-016.md#s-474e4f29337dcd92)

### observed_connections-001753

```text
(config-router-scope-af)# no bgp maxas-limit <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 26 `；EOL ` RVA 0x34547C50 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4182b170adf5e976](../../evidence/conditions-sets-026.md#c-4182b170adf5e976) · [状态效果 S-474e4f29337dcd92](../../evidence/state_effects-sets-016.md#s-474e4f29337dcd92)

### observed_connections-001742

```text
(config-router-scope-af)# no bgp maxcommunity-limit <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 27 `；EOL ` RVA 0x34547260 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8b379c227523c0d8](../../evidence/conditions-sets-054.md#c-8b379c227523c0d8) · [状态效果 S-474e4f29337dcd92](../../evidence/state_effects-sets-016.md#s-474e4f29337dcd92)

### observed_connections-001749

```text
(config-router-scope-af)# no bgp maxextcommunity-limit <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 29 `；EOL ` RVA 0x34547900 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b248dc64596958c0](../../evidence/conditions-sets-069.md#c-b248dc64596958c0) · [状态效果 S-474e4f29337dcd92](../../evidence/state_effects-sets-016.md#s-474e4f29337dcd92)

### observed_connections-001745

```text
(config-router-scope-af)# no bgp maxlargecommunity-limit <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 28 `；EOL ` RVA 0x345475B0 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e20e9f96456b5bfc](../../evidence/conditions-sets-087.md#c-e20e9f96456b5bfc) · [状态效果 S-474e4f29337dcd92](../../evidence/state_effects-sets-016.md#s-474e4f29337dcd92)

### observed_connections-001714

```text
(config-router-scope-af)# no bgp mpls-local-label <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 81 `；EOL ` RVA 0x3454EA88 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8cfe7e0e372db70a](../../evidence/conditions-sets-055.md#c-8cfe7e0e372db70a) · [状态效果 S-474e4f29337dcd92](../../evidence/state_effects-sets-016.md#s-474e4f29337dcd92)

### observed_connections-001863

```text
(config-router-scope-af)# no bgp nexthop route-map <string> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 56 `；EOL ` RVA 0x3454D300 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` route-map name。

[条件 C-e7fae0a1d2b836dc](../../evidence/conditions-sets-090.md#c-e7fae0a1d2b836dc) · [参数 P-018cf62f945dd9fb](../../evidence/parameters-sets-001.md#p-018cf62f945dd9fb) · [状态效果 S-474e4f29337dcd92](../../evidence/state_effects-sets-016.md#s-474e4f29337dcd92)

### observed_connections-001807

```text
(config-router-scope-af)# no bgp nexthop trigger critical-delay <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 48 `；EOL ` RVA 0x3454D868 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ec1659655f2a7564](../../evidence/conditions-sets-091.md#c-ec1659655f2a7564) · [状态效果 S-474e4f29337dcd92](../../evidence/state_effects-sets-016.md#s-474e4f29337dcd92)

### observed_connections-001802

```text
(config-router-scope-af)# no bgp nexthop trigger delay <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 47 `；EOL ` RVA 0x3454D5E8 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c0f2a5b04293820b](../../evidence/conditions-sets-074.md#c-c0f2a5b04293820b) · [状态效果 S-474e4f29337dcd92](../../evidence/state_effects-sets-016.md#s-474e4f29337dcd92)

### observed_connections-001858

```text
(config-router-scope-af)# no bgp nexthop trigger enable <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 49 `；EOL ` RVA 0x3454D5C0 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-71809c74616618a3](../../evidence/conditions-sets-044.md#c-71809c74616618a3) · [状态效果 S-474e4f29337dcd92](../../evidence/state_effects-sets-016.md#s-474e4f29337dcd92)

### observed_connections-001869

```text
(config-router-scope-af)# no bgp nopeerup-delay cold-boot <number:1..3600> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 74 `；EOL ` RVA 0x34542E68 `。

模式根 ` RVA 0x3453AD00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Delay in seconds。

[条件 C-a4057e89490d6056](../../evidence/conditions-sets-063.md#c-a4057e89490d6056) · [参数 P-06d763f31c291b7c](../../evidence/parameters-sets-001.md#p-06d763f31c291b7c) · [状态效果 S-de1630aa53bddf28](../../evidence/state_effects-sets-047.md#s-de1630aa53bddf28)
