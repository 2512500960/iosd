# scope-address-family-topology · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-002820

```text
(config-router-scope-af-topo)# aggregate-address <address> <address> <cr>
```

Handler ` RVA 0xF1B7BE0 `；selector ` 0 `；EOL ` RVA 0x345D0F60 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Aggregate address；` address ` Aggregate mask。

[条件 C-23d5f57ce591a637](../../evidence/conditions-sets-014.md#c-23d5f57ce591a637) · [参数 P-76b5f9e92a505038](../../evidence/parameters-sets-009.md#p-76b5f9e92a505038)

### observed_connections-002679

```text
(config-router-scope-af-topo)# auto-summary <cr>
```

Handler ` RVA 0xE1FA6B0 `；selector ` 0 `；EOL ` RVA 0x344F7B28 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-892cb3702bd56b94](../../evidence/conditions-sets-053.md#c-892cb3702bd56b94)

### observed_connections-002789

```text
(config-router-scope-af-topo)# bgp additional-paths install <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 69 `；EOL ` RVA 0x345C87B8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-60d75d37bc053107](../../evidence/conditions-sets-038.md#c-60d75d37bc053107) · [状态效果 S-75ab1c0104ad88f4](../../evidence/state_effects-sets-025.md#s-75ab1c0104ad88f4)

### observed_connections-002811

```text
(config-router-scope-af-topo)# bgp additional-paths select <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 71 `；EOL ` RVA 0x345C8460 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b007819fa3ccbb28](../../evidence/conditions-sets-068.md#c-b007819fa3ccbb28)

### observed_connections-002709

```text
(config-router-scope-af-topo)# bgp advertise-best-external <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 70 `；EOL ` RVA 0x345C9608 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bb586878f7114cd8](../../evidence/conditions-sets-072.md#c-bb586878f7114cd8)

### observed_connections-002730

```text
(config-router-scope-af-topo)# bgp advertisement startup-delay <number:1..3600> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 95 `；EOL ` RVA 0x345C1478 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` value (seconds)。

[条件 C-0a8f3bc62a41720c](../../evidence/conditions-sets-004.md#c-0a8f3bc62a41720c) · [参数 P-2b8204535c585b6f](../../evidence/parameters-sets-004.md#p-2b8204535c585b6f)

### observed_connections-002812

```text
(config-router-scope-af-topo)# bgp aggregate-timer <number:6..60> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 58 `；EOL ` RVA 0x345CF658 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timer interval。

[条件 C-fc28056caeba15bb](../../evidence/conditions-sets-097.md#c-fc28056caeba15bb) · [参数 P-1d77f5e43add4cdb](../../evidence/parameters-sets-003.md#p-1d77f5e43add4cdb)

### observed_connections-002741

```text
(config-router-scope-af-topo)# bgp aigp-rib-metric <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 91 `；EOL ` RVA 0x345C5EF8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a6d86b91e3f7b225](../../evidence/conditions-sets-064.md#c-a6d86b91e3f7b225)

### observed_connections-002705

```text
(config-router-scope-af-topo)# bgp always-compare-med <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 5 `；EOL ` RVA 0x345BCD60 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ab4874c439cf7460](../../evidence/conditions-sets-066.md#c-ab4874c439cf7460)

### observed_connections-002777

```text
(config-router-scope-af-topo)# bgp asnotation dot <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 64 `；EOL ` RVA 0x345BD070 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ab4874c439cf7460](../../evidence/conditions-sets-066.md#c-ab4874c439cf7460)

### observed_connections-002949

```text
(config-router-scope-af-topo)# bgp bestpath aigp ignore <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 43 `；EOL ` RVA 0x345C4C20 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-044dcc0f1cbb62eb](../../evidence/conditions-sets-002.md#c-044dcc0f1cbb62eb)

### observed_connections-002943

```text
(config-router-scope-af-topo)# bgp bestpath as-path ignore <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 17 `；EOL ` RVA 0x345C4390 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a6d86b91e3f7b225](../../evidence/conditions-sets-064.md#c-a6d86b91e3f7b225)

### observed_connections-002945

```text
(config-router-scope-af-topo)# bgp bestpath as-path multipath-relax <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 51 `；EOL ` RVA 0x345C4638 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a6d86b91e3f7b225](../../evidence/conditions-sets-064.md#c-a6d86b91e3f7b225)

### observed_connections-002856

```text
(config-router-scope-af-topo)# bgp bestpath compare-routerid <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 24 `；EOL ` RVA 0x345C48D0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a6d86b91e3f7b225](../../evidence/conditions-sets-064.md#c-a6d86b91e3f7b225)

### observed_connections-002948

```text
(config-router-scope-af-topo)# bgp bestpath cost-community ignore <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 41 `；EOL ` RVA 0x345C4EF8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a6d86b91e3f7b225](../../evidence/conditions-sets-064.md#c-a6d86b91e3f7b225)

### observed_connections-002890

```text
(config-router-scope-af-topo)# bgp bestpath igp-metric ignore <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 42 `；EOL ` RVA 0x345C8CE8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad20aa2ce79c5c50](../../evidence/conditions-sets-067.md#c-ad20aa2ce79c5c50)

### observed_connections-002946

```text
(config-router-scope-af-topo)# bgp bestpath med missing-as-worst <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 18 `；EOL ` RVA 0x345C4080 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a6d86b91e3f7b225](../../evidence/conditions-sets-064.md#c-a6d86b91e3f7b225) · [状态效果 S-3f3039ded9a571d5](../../evidence/state_effects-sets-014.md#s-3f3039ded9a571d5)

### observed_connections-002898

```text
(config-router-scope-af-topo)# bgp bestpath prefix-validate allow-invalid <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 78 `；EOL ` RVA 0x345C8FF8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-31956af50c4a9141](../../evidence/conditions-sets-019.md#c-31956af50c4a9141)

### observed_connections-002904

```text
(config-router-scope-af-topo)# bgp bestpath prefix-validate disable <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 77 `；EOL ` RVA 0x345C92A0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-31956af50c4a9141](../../evidence/conditions-sets-019.md#c-31956af50c4a9141)

### observed_connections-002798

```text
(config-router-scope-af-topo)# bgp client-to-client reflection <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 9 `；EOL ` RVA 0x345BDF00 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d84da79c9374e309](../../evidence/conditions-sets-083.md#c-d84da79c9374e309) · [状态效果 S-b5d7cfbb85267560](../../evidence/state_effects-sets-038.md#s-b5d7cfbb85267560)

### observed_connections-003117

```text
(config-router-scope-af-topo)# bgp client-to-client reflection intra-cluster cluster-id <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 9 `；EOL ` RVA 0x345BDF00 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-457211ddb2ffa861](../../evidence/conditions-sets-027.md#c-457211ddb2ffa861) · [缺口 G-b977f21fe18676e6](../../evidence/gaps-sets-007.md#g-b977f21fe18676e6) · [状态效果 S-ec58efe369bc8e9f](../../evidence/state_effects-sets-050.md#s-ec58efe369bc8e9f)

### observed_connections-002795

```text
(config-router-scope-af-topo)# bgp cluster-id <number:1..4294967294> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 7 `；EOL ` RVA 0x345BDAC8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Route-Reflector Cluster-id as 32 bit quantity。

[条件 C-5dbdb307eea4e255](../../evidence/conditions-sets-037.md#c-5dbdb307eea4e255) · [参数 P-ff6fcc4bc5b7c4db](../../evidence/parameters-sets-019.md#p-ff6fcc4bc5b7c4db)

### observed_connections-003102

```text
(config-router-scope-af-topo)# bgp confederation identifier <?bgp_as4_action@555589b12dd0> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 6 `；EOL ` RVA 0x345BEE08 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ab4874c439cf7460](../../evidence/conditions-sets-066.md#c-ab4874c439cf7460) · [缺口 G-1eb340c0a335a63e](../../evidence/gaps-sets-002.md#g-1eb340c0a335a63e)

### observed_connections-003103

```text
(config-router-scope-af-topo)# bgp confederation peers <?bgp_as4_action@555589b13140> <cr>
```

Handler ` RVA 0xF1C67F0 `；selector ` 0 `；EOL ` RVA 0x345BF280 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a05e092d4d72c190](../../evidence/conditions-sets-062.md#c-a05e092d4d72c190) · [缺口 G-921174c6db394d23](../../evidence/gaps-sets-005.md#g-921174c6db394d23) · [状态效果 S-ca94889120ff877c](../../evidence/state_effects-sets-043.md#s-ca94889120ff877c)

### observed_connections-002815

```text
(config-router-scope-af-topo)# bgp consistency-checker error-message <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 3 `；EOL ` RVA 0x345BD448 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d15b9beb7e94f562](../../evidence/conditions-sets-081.md#c-d15b9beb7e94f562) · [状态效果 S-42682549072e27c5](../../evidence/state_effects-sets-015.md#s-42682549072e27c5)

### observed_connections-002803

```text
(config-router-scope-af-topo)# bgp consistency-checker error-message interval <number:5..1440> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 3 `；EOL ` RVA 0x345BD470 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Interval (minutes)。

[条件 C-2f3ea5985fa0075f](../../evidence/conditions-sets-018.md#c-2f3ea5985fa0075f) · [参数 P-1c658bf14478a8f0](../../evidence/parameters-sets-003.md#p-1c658bf14478a8f0) · [状态效果 S-42682549072e27c5](../../evidence/state_effects-sets-015.md#s-42682549072e27c5)

### observed_connections-002712

```text
(config-router-scope-af-topo)# bgp dampening <cr>
```

Handler ` RVA 0xF1B85B0 `；selector ` 0 `；EOL ` RVA 0x345C7880 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b46de2d828cc54c4](../../evidence/conditions-sets-070.md#c-b46de2d828cc54c4)

### observed_connections-002894

```text
(config-router-scope-af-topo)# bgp dampening route-map <string> <cr>
```

Handler ` RVA 0xF1B85B0 `；selector ` 8 `；EOL ` RVA 0x345C7A48 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` route-map name。

[条件 C-2206f847acdc54ee](../../evidence/conditions-sets-013.md#c-2206f847acdc54ee) · [参数 P-93ad3a3c91291452](../../evidence/parameters-sets-011.md#p-93ad3a3c91291452)

### observed_connections-002891

```text
(config-router-scope-af-topo)# bgp default inter-as-hybrid advertise-source-routes <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 57 `；EOL ` RVA 0x345C6EB8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c0f22f5509b0574d](../../evidence/conditions-sets-074.md#c-c0f22f5509b0574d)

### observed_connections-002761

```text
(config-router-scope-af-topo)# bgp default ipv4-unicast <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 19 `；EOL ` RVA 0x345C6610 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-21977b251acb837f](../../evidence/conditions-sets-013.md#c-21977b251acb837f)

### observed_connections-002765

```text
(config-router-scope-af-topo)# bgp default ipv6-nexthop <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 75 `；EOL ` RVA 0x345C6908 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-745de96593c1eadf](../../evidence/conditions-sets-045.md#c-745de96593c1eadf)

### observed_connections-002706

```text
(config-router-scope-af-topo)# bgp default local-preference <number:0..4294967295> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 0 `；EOL ` RVA 0x345C6B98 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Configure default local preference value。

[条件 C-d00ff58901452fc4](../../evidence/conditions-sets-080.md#c-d00ff58901452fc4) · [参数 P-8dfda33418fe633b](../../evidence/parameters-sets-011.md#p-8dfda33418fe633b)

### observed_connections-002887

```text
(config-router-scope-af-topo)# bgp default route-target filter <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 25 `；EOL ` RVA 0x345C7220 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a1d6f7b25430895a](../../evidence/conditions-sets-062.md#c-a1d6f7b25430895a)

### observed_connections-002888

```text
(config-router-scope-af-topo)# bgp default route-target filter <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 25 `；EOL ` RVA 0x345C74C0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8b8d63d3237cfa03](../../evidence/conditions-sets-054.md#c-8b8d63d3237cfa03)

### observed_connections-002719

```text
(config-router-scope-af-topo)# bgp deterministic-med <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 10 `；EOL ` RVA 0x345BF580 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ab4874c439cf7460](../../evidence/conditions-sets-066.md#c-ab4874c439cf7460)

### observed_connections-002714

```text
(config-router-scope-af-topo)# bgp dmzlink-bw <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 31 `；EOL ` RVA 0x345CABB8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3adab7f53eab96ed](../../evidence/conditions-sets-023.md#c-3adab7f53eab96ed)

### observed_connections-002678

```text
(config-router-scope-af-topo)# bgp dynamic-med-interval <number:60..4294967295> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 21 `；EOL ` RVA 0x345BF5A8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Interval value (seconds)。

[条件 C-2ad50c481071d67f](../../evidence/conditions-sets-017.md#c-2ad50c481071d67f) · [参数 P-d28434b14ab57676](../../evidence/parameters-sets-016.md#p-d28434b14ab57676)

### observed_connections-002715

```text
(config-router-scope-af-topo)# bgp enforce-first-as <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 20 `；EOL ` RVA 0x345BE7B0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ab4874c439cf7460](../../evidence/conditions-sets-066.md#c-ab4874c439cf7460)

### observed_connections-002737

```text
(config-router-scope-af-topo)# bgp enhanced-error <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 82 `；EOL ` RVA 0x345C11F0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-454872c68d0ab02f](../../evidence/conditions-sets-027.md#c-454872c68d0ab02f)

### observed_connections-002702

```text
(config-router-scope-af-topo)# bgp fast-external-fallover <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 1 `；EOL ` RVA 0x345BC498 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ab4874c439cf7460](../../evidence/conditions-sets-066.md#c-ab4874c439cf7460)

### observed_connections-002740

```text
(config-router-scope-af-topo)# bgp graceful-restart <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 35 `；EOL ` RVA 0x345C2060 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ab4874c439cf7460](../../evidence/conditions-sets-066.md#c-ab4874c439cf7460)

### observed_connections-002738

```text
(config-router-scope-af-topo)# bgp graceful-restart restart-time <number:1..3600> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 36 `；EOL ` RVA 0x345C1A30 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Delay value (seconds)。

[条件 C-ba76fb79328aa9b9](../../evidence/conditions-sets-072.md#c-ba76fb79328aa9b9) · [参数 P-6a65339715d8512a](../../evidence/parameters-sets-008.md#p-6a65339715d8512a)

### observed_connections-002739

```text
(config-router-scope-af-topo)# bgp graceful-restart stalepath-time <number:1..3600> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 37 `；EOL ` RVA 0x345C1A98 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Delay value (seconds)。

[条件 C-47cbe023f1fe885c](../../evidence/conditions-sets-028.md#c-47cbe023f1fe885c) · [参数 P-b848269146233afc](../../evidence/parameters-sets-014.md#p-b848269146233afc)

### observed_connections-003123

```text
(config-router-scope-af-topo)# bgp graceful-shutdown all vrfs <number:30..65535> community <?bgp_community_action@555589b16978> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 79 `；EOL ` RVA 0x345C24C8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` time in seconds。

[条件 C-904c238bdad7a313](../../evidence/conditions-sets-056.md#c-904c238bdad7a313) · [缺口 G-3d52c6e7c260847c](../../evidence/gaps-sets-003.md#g-3d52c6e7c260847c) · [参数 P-957fa662b4a1ed0c](../../evidence/parameters-sets-011.md#p-957fa662b4a1ed0c) · [状态效果 S-fdede1b15ffee709](../../evidence/state_effects-sets-054.md#s-fdede1b15ffee709)

### observed_connections-002990

```text
(config-router-scope-af-topo)# bgp graceful-shutdown all vrfs activate <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 79 `；EOL ` RVA 0x345C24C8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9b1924e01b9a6adb](../../evidence/conditions-sets-060.md#c-9b1924e01b9a6adb) · [状态效果 S-c8bde9d014cf9ec1](../../evidence/state_effects-sets-043.md#s-c8bde9d014cf9ec1)

### observed_connections-002983

```text
(config-router-scope-af-topo)# bgp inject-map <string> exist-map <string> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 32 `；EOL ` RVA 0x345CC730 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` route-map name；` string ` route-map name。

[条件 C-fedb6cae967c9a50](../../evidence/conditions-sets-098.md#c-fedb6cae967c9a50) · [参数 P-c031eb060e8bf349](../../evidence/parameters-sets-015.md#p-c031eb060e8bf349)

### observed_connections-002885

```text
(config-router-scope-af-topo)# bgp label-allocation-batch <number:0..4294967295> <number:0..4294967295> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 53 `；EOL ` RVA 0x345BC828 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timer value in milliseconds；` unsigned_number ` Batch Size。

[条件 C-ab4874c439cf7460](../../evidence/conditions-sets-066.md#c-ab4874c439cf7460) · [参数 P-25b90a94faeaa469](../../evidence/parameters-sets-003.md#p-25b90a94faeaa469)

### observed_connections-002916

```text
(config-router-scope-af-topo)# bgp listen block <address> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 93 `；EOL ` RVA 0x345CA5C8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IPv4 Dynamic Peering Address。

[条件 C-68b3d1afb9f1515e](../../evidence/conditions-sets-041.md#c-68b3d1afb9f1515e) · [参数 P-4423f7a79b076b21](../../evidence/parameters-sets-006.md#p-4423f7a79b076b21)

### observed_connections-002927

```text
(config-router-scope-af-topo)# bgp listen block <address> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 93 `；EOL ` RVA 0x345C0528 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IPv4 Dynamic Peering Address。

[条件 C-4383b9d78c985b8e](../../evidence/conditions-sets-026.md#c-4383b9d78c985b8e) · [参数 P-11231d0c3b66f126](../../evidence/parameters-sets-002.md#p-11231d0c3b66f126)

### observed_connections-002718

```text
(config-router-scope-af-topo)# bgp listen limit <number:1..10000> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 61 `；EOL ` RVA 0x345CA510 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` max number。

[条件 C-f90d311575d7bd83](../../evidence/conditions-sets-096.md#c-f90d311575d7bd83) · [参数 P-a8aa49afbff52987](../../evidence/parameters-sets-013.md#p-a8aa49afbff52987)

### observed_connections-002733

```text
(config-router-scope-af-topo)# bgp listen limit <number:1..10000> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 61 `；EOL ` RVA 0x345C0448 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` max number。

[条件 C-540a7ec31b766fdf](../../evidence/conditions-sets-033.md#c-540a7ec31b766fdf) · [参数 P-ae95ee9a2d962be7](../../evidence/parameters-sets-013.md#p-ae95ee9a2d962be7)

### observed_connections-002848

```text
(config-router-scope-af-topo)# bgp listen persistent <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 94 `；EOL ` RVA 0x345C0860 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4383b9d78c985b8e](../../evidence/conditions-sets-026.md#c-4383b9d78c985b8e)

### observed_connections-003122

```text
(config-router-scope-af-topo)# bgp listen range <prefix:dynamic> peer-group <string> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 60 `；EOL ` RVA 0x345C00A0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` IPv4 subnet range；` string ` peer-group name。

[条件 C-6a7766e0099cd0ae](../../evidence/conditions-sets-041.md#c-6a7766e0099cd0ae) · [缺口 G-d9203c79a55ef925](../../evidence/gaps-sets-008.md#g-d9203c79a55ef925) · [参数 P-1be5e4d660474fba](../../evidence/parameters-sets-003.md#p-1be5e4d660474fba)

### observed_connections-002716

```text
(config-router-scope-af-topo)# bgp log-neighbor-changes <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 11 `；EOL ` RVA 0x345BEA58 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ab4874c439cf7460](../../evidence/conditions-sets-066.md#c-ab4874c439cf7460)

### observed_connections-002869

```text
(config-router-scope-af-topo)# bgp maxas-limit <number:1..254> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 26 `；EOL ` RVA 0x345C5C70 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of ASes in the AS-PATH attribute(max 254)。

[条件 C-7a453e7bcf21807b](../../evidence/conditions-sets-047.md#c-7a453e7bcf21807b) · [参数 P-70b88a50fe839ae6](../../evidence/parameters-sets-009.md#p-70b88a50fe839ae6)

### observed_connections-002858

```text
(config-router-scope-af-topo)# bgp maxcommunity-limit <number:1..1018> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 27 `；EOL ` RVA 0x345C5280 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of communities in the COMMUNITY attribute。

[条件 C-8295578b6e7ac8f8](../../evidence/conditions-sets-051.md#c-8295578b6e7ac8f8) · [参数 P-0c47ef5f1865a187](../../evidence/parameters-sets-001.md#p-0c47ef5f1865a187)

### observed_connections-002865

```text
(config-router-scope-af-topo)# bgp maxextcommunity-limit <number:1..509> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 29 `；EOL ` RVA 0x345C5920 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of extended communities in the EXTENDED COMMUNITY attribute。

[条件 C-db36155f7d6c13a4](../../evidence/conditions-sets-084.md#c-db36155f7d6c13a4) · [参数 P-5cf92542599d1ebb](../../evidence/parameters-sets-007.md#p-5cf92542599d1ebb)

### observed_connections-002861

```text
(config-router-scope-af-topo)# bgp maxlargecommunity-limit <number:1..339> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 28 `；EOL ` RVA 0x345C55D0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of large communities in the LARGE COMMUNITY attribute。

[条件 C-0b8a4a397fa8c945](../../evidence/conditions-sets-005.md#c-0b8a4a397fa8c945) · [参数 P-04c65558b59d42c8](../../evidence/parameters-sets-001.md#p-04c65558b59d42c8)

### observed_connections-002728

```text
(config-router-scope-af-topo)# bgp mpls-local-label <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 81 `；EOL ` RVA 0x345CCAA8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-31488a0baa289d4d](../../evidence/conditions-sets-019.md#c-31488a0baa289d4d)

### observed_connections-002919

```text
(config-router-scope-af-topo)# bgp nexthop route-map <string> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 56 `；EOL ` RVA 0x345CB320 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` route-map name。

[条件 C-7820ec64c4324b06](../../evidence/conditions-sets-047.md#c-7820ec64c4324b06) · [参数 P-6f819417a906606a](../../evidence/parameters-sets-009.md#p-6f819417a906606a)

### observed_connections-002827

```text
(config-router-scope-af-topo)# bgp nexthop trigger critical-delay <number:0..100> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 48 `；EOL ` RVA 0x345CB888 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Critical delay value (seconds)。

[条件 C-f11556380b3f71d8](../../evidence/conditions-sets-093.md#c-f11556380b3f71d8) · [参数 P-ca23d70c6a164738](../../evidence/parameters-sets-015.md#p-ca23d70c6a164738)

### observed_connections-002822

```text
(config-router-scope-af-topo)# bgp nexthop trigger delay <number:0..100> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 47 `；EOL ` RVA 0x345CB608 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Delay value (seconds)。

[条件 C-378d07d1e33cf779](../../evidence/conditions-sets-022.md#c-378d07d1e33cf779) · [参数 P-49cc9f06328db500](../../evidence/parameters-sets-006.md#p-49cc9f06328db500)

### observed_connections-002915

```text
(config-router-scope-af-topo)# bgp nexthop trigger enable <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 49 `；EOL ` RVA 0x345CB5E0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8afb2da867e5f253](../../evidence/conditions-sets-054.md#c-8afb2da867e5f253)

### observed_connections-002926

```text
(config-router-scope-af-topo)# bgp nopeerup-delay cold-boot <number:1..3600> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 74 `；EOL ` RVA 0x345C0E88 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Delay in seconds。

[条件 C-d307f5eb044f3a7c](../../evidence/conditions-sets-081.md#c-d307f5eb044f3a7c) · [参数 P-ca7b15937712ec27](../../evidence/parameters-sets-015.md#p-ca7b15937712ec27) · [状态效果 S-73cd85bad906aae5](../../evidence/state_effects-sets-025.md#s-73cd85bad906aae5)

### observed_connections-002785

```text
(config-router-scope-af-topo)# bgp recursion host <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 72 `；EOL ` RVA 0x345C9980 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-019c433b5d1f87b0](../../evidence/conditions-sets-001.md#c-019c433b5d1f87b0)

### observed_connections-002710

```text
(config-router-scope-af-topo)# bgp redistribute-internal <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 2 `；EOL ` RVA 0x345CDCA8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2ffde756bdc3d691](../../evidence/conditions-sets-019.md#c-2ffde756bdc3d691)

### observed_connections-002940

```text
(config-router-scope-af-topo)# bgp refresh max-eor-time <number:600..3600> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 16 `；EOL ` RVA 0x345C3258 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timer interval (seconds)。

[条件 C-99c658f2ec7b619c](../../evidence/conditions-sets-059.md#c-99c658f2ec7b619c) · [参数 P-66e3c1fb195a534d](../../evidence/parameters-sets-008.md#p-66e3c1fb195a534d)

### observed_connections-002936

```text
(config-router-scope-af-topo)# bgp refresh stalepath-time <number:600..3600> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 15 `；EOL ` RVA 0x345C2EE8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timer interval (seconds)。

[条件 C-020a8d3efc4f23ca](../../evidence/conditions-sets-001.md#c-020a8d3efc4f23ca) · [参数 P-3d8a3cb10175309a](../../evidence/parameters-sets-005.md#p-3d8a3cb10175309a)

### observed_connections-002853

```text
(config-router-scope-af-topo)# bgp regexp deterministic <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 44 `；EOL ` RVA 0x345C3C70 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a6d86b91e3f7b225](../../evidence/conditions-sets-064.md#c-a6d86b91e3f7b225)

### observed_connections-002786

```text
(config-router-scope-af-topo)# bgp route-map priority <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 59 `；EOL ` RVA 0x345CEE38 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a57efef1bb356cf9](../../evidence/conditions-sets-064.md#c-a57efef1bb356cf9)

### observed_connections-002704

```text
(config-router-scope-af-topo)# bgp route-map-cache <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 34 `；EOL ` RVA 0x345BCAB0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ab4874c439cf7460](../../evidence/conditions-sets-066.md#c-ab4874c439cf7460)

### observed_connections-002784

```text
(config-router-scope-af-topo)# bgp router-id <address> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 4 `；EOL ` RVA 0x345BBE68 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Manually configured router identifier。

[条件 C-5ef47205a578b8ac](../../evidence/conditions-sets-037.md#c-5ef47205a578b8ac) · [参数 P-3a50f1f36ad31eec](../../evidence/parameters-sets-005.md#p-3a50f1f36ad31eec)

### observed_connections-002818

```text
(config-router-scope-af-topo)# bgp router-id auto-assign <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 4 `；EOL ` RVA 0x345CA030 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-28da95b37d6a19b6](../../evidence/conditions-sets-016.md#c-28da95b37d6a19b6) · [状态效果 S-c7735055414f37c6](../../evidence/state_effects-sets-042.md#s-c7735055414f37c6)

### observed_connections-003100

```text
(config-router-scope-af-topo)# bgp router-id interface <interface> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 4 `；EOL ` RVA 0x345BBE68 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d6e399d539d227e8](../../evidence/conditions-sets-083.md#c-d6e399d539d227e8) · [缺口 G-c1deee0ae117d6f8](../../evidence/gaps-sets-007.md#g-c1deee0ae117d6f8) · [参数 P-11b5cce27998b383](../../evidence/parameters-sets-002.md#p-11b5cce27998b383)

### observed_connections-003101

```text
(config-router-scope-af-topo)# bgp router-id interface <interface> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 4 `；EOL ` RVA 0x345CA030 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-735c035c227ac0cf](../../evidence/conditions-sets-045.md#c-735c035c227ac0cf) · [缺口 G-0e5ffd6e2f66700a](../../evidence/gaps-sets-001.md#g-0e5ffd6e2f66700a) · [参数 P-71a2f88855f87293](../../evidence/parameters-sets-009.md#p-71a2f88855f87293)

### observed_connections-003018

```text
(config-router-scope-af-topo)# bgp rpki server tcp <address> port <number:1..65535> refresh <number:1..65535> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 76 `；EOL ` RVA 0x345CFC50 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IPv6 address of RPKI cache server；` unsigned_number ` Port number；` unsigned_number ` Refresh time in seconds。

[条件 C-fd6cda537b929d75](../../evidence/conditions-sets-098.md#c-fd6cda537b929d75) · [参数 P-c7888514a7534998](../../evidence/parameters-sets-015.md#p-c7888514a7534998)

### observed_connections-002828

```text
(config-router-scope-af-topo)# bgp rr-group <string> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 23 `；EOL ` RVA 0x345CC2C8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Extended community-list name。

[条件 C-4a9636bb392c9cdd](../../evidence/conditions-sets-029.md#c-4a9636bb392c9cdd) · [参数 P-c489e046ae0ce186](../../evidence/parameters-sets-015.md#p-c489e046ae0ce186)

### observed_connections-002742

```text
(config-router-scope-af-topo)# bgp safe-ebgp-policy <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 92 `；EOL ` RVA 0x345C6208 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c3ec135058645164](../../evidence/conditions-sets-076.md#c-c3ec135058645164)

### observed_connections-002824

```text
(config-router-scope-af-topo)# bgp scan-time <number:5..60> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 22 `；EOL ` RVA 0x345CBF58 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Scanner interval (seconds)。

[条件 C-f6c5e214b2225f3e](../../evidence/conditions-sets-095.md#c-f6c5e214b2225f3e) · [参数 P-75e51e2c3101672c](../../evidence/parameters-sets-009.md#p-75e51e2c3101672c)

### observed_connections-002793

```text
(config-router-scope-af-topo)# bgp slow-peer detection <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 67 `；EOL ` RVA 0x345CCF78 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ac4189e2080c8425](../../evidence/conditions-sets-067.md#c-ac4189e2080c8425)

### observed_connections-002788

```text
(config-router-scope-af-topo)# bgp slow-peer detection threshold <number:120..3600> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 67 `；EOL ` RVA 0x345CCF50 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Threshold value (seconds)。

[条件 C-15b8c09e7adfdb21](../../evidence/conditions-sets-009.md#c-15b8c09e7adfdb21) · [参数 P-8133dbaf0a134b24](../../evidence/parameters-sets-010.md#p-8133dbaf0a134b24)

### observed_connections-002909

```text
(config-router-scope-af-topo)# bgp slow-peer split-update-group dynamic <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 68 `；EOL ` RVA 0x345CD548 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d59f27326993e29b](../../evidence/conditions-sets-082.md#c-d59f27326993e29b)

### observed_connections-002925

```text
(config-router-scope-af-topo)# bgp snmp traps add-type <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 90 `；EOL ` RVA 0x345BFB70 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ab4874c439cf7460](../../evidence/conditions-sets-066.md#c-ab4874c439cf7460)

### observed_connections-002717

```text
(config-router-scope-af-topo)# bgp soft-reconfig-backup <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 52 `；EOL ` RVA 0x345CAF08 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-756792ade7cc9960](../../evidence/conditions-sets-046.md#c-756792ade7cc9960)

### observed_connections-002975

```text
(config-router-scope-af-topo)# bgp sourced-paths per-net isis all <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 89 `；EOL ` RVA 0x345CEAB8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c83d4e3bedad6190](../../evidence/conditions-sets-077.md#c-c83d4e3bedad6190) · [状态效果 S-28041116c34f1919](../../evidence/state_effects-sets-009.md#s-28041116c34f1919)

### observed_connections-002969

```text
(config-router-scope-af-topo)# bgp sourced-paths per-net ospf all <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 87 `；EOL ` RVA 0x345CE458 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c83d4e3bedad6190](../../evidence/conditions-sets-077.md#c-c83d4e3bedad6190) · [状态效果 S-958faef03f70ced3](../../evidence/state_effects-sets-032.md#s-958faef03f70ced3)

### observed_connections-002971

```text
(config-router-scope-af-topo)# bgp sourced-paths per-net ospfv3 all <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 88 `；EOL ` RVA 0x345CE7A0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c83d4e3bedad6190](../../evidence/conditions-sets-077.md#c-c83d4e3bedad6190) · [状态效果 S-6d1b4ce024379c31](../../evidence/state_effects-sets-023.md#s-6d1b4ce024379c31)

### observed_connections-002966

```text
(config-router-scope-af-topo)# bgp sourced-paths per-net static all <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 86 `；EOL ` RVA 0x345CE110 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c83d4e3bedad6190](../../evidence/conditions-sets-077.md#c-c83d4e3bedad6190) · [状态效果 S-881b7f9e54b486a7](../../evidence/state_effects-sets-029.md#s-881b7f9e54b486a7)

### observed_connections-002849

```text
(config-router-scope-af-topo)# bgp sso route-refresh-enable <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 38 `；EOL ` RVA 0x345C2B28 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a6d86b91e3f7b225](../../evidence/conditions-sets-064.md#c-a6d86b91e3f7b225)

### observed_connections-002713

```text
(config-router-scope-af-topo)# bgp suppress-inactive <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 45 `；EOL ` RVA 0x345C9C80 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-133a19ecba7cce81](../../evidence/conditions-sets-008.md#c-133a19ecba7cce81)

### observed_connections-002669

```text
(config-router-scope-af-topo)# bgp tid <number:1..255> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 55 `；EOL ` RVA 0x345BB6A8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Tolology identifier value。

[条件 C-7028513ee784d562](../../evidence/conditions-sets-043.md#c-7028513ee784d562) · [参数 P-50edd0cb08372a0b](../../evidence/parameters-sets-007.md#p-50edd0cb08372a0b)

### observed_connections-002794

```text
(config-router-scope-af-topo)# bgp transport path-mtu-discovery <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 50 `；EOL ` RVA 0x345BE520 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ab4874c439cf7460](../../evidence/conditions-sets-066.md#c-ab4874c439cf7460)

### observed_connections-002680

```text
(config-router-scope-af-topo)# bgp update-delay <number:1..3600> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 30 `；EOL ` RVA 0x345C14A0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Delay value (seconds)。

[条件 C-621e5b2294bd083e](../../evidence/conditions-sets-038.md#c-621e5b2294bd083e) · [参数 P-3b4701b23986302d](../../evidence/parameters-sets-005.md#p-3b4701b23986302d)

### observed_connections-002893

```text
(config-router-scope-af-topo)# bgp update-group split as-override <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 73 `；EOL ` RVA 0x345CD918 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4969fbb5328f8a37](../../evidence/conditions-sets-029.md#c-4969fbb5328f8a37)

### observed_connections-002703

```text
(config-router-scope-af-topo)# bgp upgrade-cli <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 33 `；EOL ` RVA 0x345BBAC0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9780fe2be46b60d7](../../evidence/conditions-sets-058.md#c-9780fe2be46b60d7)

### observed_connections-002972

```text
(config-router-scope-af-topo)# bgp va <address> mask <address> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 80 `；EOL ` RVA 0x345CF1E0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` BGP VA ip address；` address ` BGP VA mask address。

[条件 C-6f04dc41431d4021](../../evidence/conditions-sets-043.md#c-6f04dc41431d4021) · [参数 P-21947d967a27ecfe](../../evidence/parameters-sets-003.md#p-21947d967a27ecfe)

### observed_connections-002851

```text
(config-router-scope-af-topo)# bgp vrf-update-optimisation off <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 66 `；EOL ` RVA 0x345C35E0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a6d86b91e3f7b225](../../evidence/conditions-sets-064.md#c-a6d86b91e3f7b225)

### observed_connections-002942

```text
(config-router-scope-af-topo)# bgp write-limit <number:500..2147483647> <number:500..2147483647> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 40 `；EOL ` RVA 0x345C3938 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of messages to be formatted per neighbor/peergroup；` unsigned_number ` Number of messages that can be enqueued in total。

[条件 C-df5a108b3ef7097e](../../evidence/conditions-sets-086.md#c-df5a108b3ef7097e) · [参数 P-bb9bb4882e45ec66](../../evidence/parameters-sets-014.md#p-bb9bb4882e45ec66)

### observed_connections-002685

```text
(config-router-scope-af-topo)# context <string> <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 0 `；EOL ` RVA 0x33C44A60 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` SNMP Context Name。

[条件 C-9affa1869574e86e](../../evidence/conditions-sets-060.md#c-9affa1869574e86e) · [参数 P-f3e465802edc027f](../../evidence/parameters-sets-018.md#p-f3e465802edc027f) · [状态效果 S-355a44aeb0ea4c7f](../../evidence/state_effects-sets-012.md#s-355a44aeb0ea4c7f)

### observed_connections-002918

```text
(config-router-scope-af-topo)# default aggregate-address <address> <address> <cr>
```

Handler ` RVA 0xF1B7BE0 `；selector ` 0 `；EOL ` RVA 0x345D0F60 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` Aggregate address；` address ` Aggregate mask。

[条件 C-23d5f57ce591a637](../../evidence/conditions-sets-014.md#c-23d5f57ce591a637) · [参数 P-76b5f9e92a505038](../../evidence/parameters-sets-009.md#p-76b5f9e92a505038) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002724

```text
(config-router-scope-af-topo)# default auto-summary <cr>
```

Handler ` RVA 0xE1FA6B0 `；selector ` 0 `；EOL ` RVA 0x344F7B28 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-892cb3702bd56b94](../../evidence/conditions-sets-053.md#c-892cb3702bd56b94) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002905

```text
(config-router-scope-af-topo)# default bgp additional-paths install <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 69 `；EOL ` RVA 0x345C87B8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-60d75d37bc053107](../../evidence/conditions-sets-038.md#c-60d75d37bc053107) · [状态效果 S-9c7680bb8df2faa0](../../evidence/state_effects-sets-033.md#s-9c7680bb8df2faa0)

### observed_connections-002912

```text
(config-router-scope-af-topo)# default bgp additional-paths select <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 71 `；EOL ` RVA 0x345C8460 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b007819fa3ccbb28](../../evidence/conditions-sets-068.md#c-b007819fa3ccbb28) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002781

```text
(config-router-scope-af-topo)# default bgp advertise-best-external <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 70 `；EOL ` RVA 0x345C9608 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-bb586878f7114cd8](../../evidence/conditions-sets-072.md#c-bb586878f7114cd8) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002834

```text
(config-router-scope-af-topo)# default bgp advertisement startup-delay <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 95 `；EOL ` RVA 0x345C1478 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-080ae7a4274fcc15](../../evidence/conditions-sets-003.md#c-080ae7a4274fcc15) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002913

```text
(config-router-scope-af-topo)# default bgp aggregate-timer <number:6..60> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 58 `；EOL ` RVA 0x345CF658 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Timer interval。

[条件 C-fc28056caeba15bb](../../evidence/conditions-sets-097.md#c-fc28056caeba15bb) · [参数 P-1d77f5e43add4cdb](../../evidence/parameters-sets-003.md#p-1d77f5e43add4cdb) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002866

```text
(config-router-scope-af-topo)# default bgp aigp-rib-metric <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 91 `；EOL ` RVA 0x345C5EF8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a6d86b91e3f7b225](../../evidence/conditions-sets-064.md#c-a6d86b91e3f7b225) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002773

```text
(config-router-scope-af-topo)# default bgp always-compare-med <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 5 `；EOL ` RVA 0x345BCD60 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ab4874c439cf7460](../../evidence/conditions-sets-066.md#c-ab4874c439cf7460) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002892

```text
(config-router-scope-af-topo)# default bgp asnotation dot <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 64 `；EOL ` RVA 0x345BD070 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ab4874c439cf7460](../../evidence/conditions-sets-066.md#c-ab4874c439cf7460) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-003000

```text
(config-router-scope-af-topo)# default bgp bestpath aigp ignore <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 43 `；EOL ` RVA 0x345C4C20 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-044dcc0f1cbb62eb](../../evidence/conditions-sets-002.md#c-044dcc0f1cbb62eb) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002992

```text
(config-router-scope-af-topo)# default bgp bestpath as-path ignore <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 17 `；EOL ` RVA 0x345C4390 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a6d86b91e3f7b225](../../evidence/conditions-sets-064.md#c-a6d86b91e3f7b225) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002995

```text
(config-router-scope-af-topo)# default bgp bestpath as-path multipath-relax <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 51 `；EOL ` RVA 0x345C4638 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a6d86b91e3f7b225](../../evidence/conditions-sets-064.md#c-a6d86b91e3f7b225) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002947

```text
(config-router-scope-af-topo)# default bgp bestpath compare-routerid <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 24 `；EOL ` RVA 0x345C48D0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a6d86b91e3f7b225](../../evidence/conditions-sets-064.md#c-a6d86b91e3f7b225) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002999

```text
(config-router-scope-af-topo)# default bgp bestpath cost-community ignore <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 41 `；EOL ` RVA 0x345C4EF8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a6d86b91e3f7b225](../../evidence/conditions-sets-064.md#c-a6d86b91e3f7b225) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002958

```text
(config-router-scope-af-topo)# default bgp bestpath igp-metric ignore <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 42 `；EOL ` RVA 0x345C8CE8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad20aa2ce79c5c50](../../evidence/conditions-sets-067.md#c-ad20aa2ce79c5c50) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002996

```text
(config-router-scope-af-topo)# default bgp bestpath med missing-as-worst <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 18 `；EOL ` RVA 0x345C4080 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a6d86b91e3f7b225](../../evidence/conditions-sets-064.md#c-a6d86b91e3f7b225) · [状态效果 S-091a42cda71f9a27](../../evidence/state_effects-sets-002.md#s-091a42cda71f9a27)

### observed_connections-002963

```text
(config-router-scope-af-topo)# default bgp bestpath prefix-validate allow-invalid <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 78 `；EOL ` RVA 0x345C8FF8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-31956af50c4a9141](../../evidence/conditions-sets-019.md#c-31956af50c4a9141) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002967

```text
(config-router-scope-af-topo)# default bgp bestpath prefix-validate disable <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 77 `；EOL ` RVA 0x345C92A0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-31956af50c4a9141](../../evidence/conditions-sets-019.md#c-31956af50c4a9141) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002908

```text
(config-router-scope-af-topo)# default bgp client-to-client reflection <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 9 `；EOL ` RVA 0x345BDF00 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d84da79c9374e309](../../evidence/conditions-sets-083.md#c-d84da79c9374e309) · [状态效果 S-e59b90ee9f0c6eba](../../evidence/state_effects-sets-049.md#s-e59b90ee9f0c6eba)

### observed_connections-002801

```text
(config-router-scope-af-topo)# default bgp cluster-id <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 7 `；EOL ` RVA 0x345BDAC8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-bd666b48a2afb3e1](../../evidence/conditions-sets-073.md#c-bd666b48a2afb3e1) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002809

```text
(config-router-scope-af-topo)# default bgp consistency-checker <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 3 `；EOL ` RVA 0x345BD448 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8251c5dc4177e6be](../../evidence/conditions-sets-050.md#c-8251c5dc4177e6be) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002774

```text
(config-router-scope-af-topo)# default bgp dampening <cr>
```

Handler ` RVA 0xF1B85B0 `；selector ` 0 `；EOL ` RVA 0x345C7880 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-985390fdd0174757](../../evidence/conditions-sets-059.md#c-985390fdd0174757) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002960

```text
(config-router-scope-af-topo)# default bgp default inter-as-hybrid advertise-source-routes <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 57 `；EOL ` RVA 0x345C6EB8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c0f22f5509b0574d](../../evidence/conditions-sets-074.md#c-c0f22f5509b0574d) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002882

```text
(config-router-scope-af-topo)# default bgp default ipv4-unicast <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 19 `；EOL ` RVA 0x345C6610 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-21977b251acb837f](../../evidence/conditions-sets-013.md#c-21977b251acb837f) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002886

```text
(config-router-scope-af-topo)# default bgp default ipv6-nexthop <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 75 `；EOL ` RVA 0x345C6908 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-745de96593c1eadf](../../evidence/conditions-sets-045.md#c-745de96593c1eadf) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002776

```text
(config-router-scope-af-topo)# default bgp default local-preference <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 0 `；EOL ` RVA 0x345C6B98 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-bce9a25435a542ed](../../evidence/conditions-sets-073.md#c-bce9a25435a542ed) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002954

```text
(config-router-scope-af-topo)# default bgp default route-target filter <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 25 `；EOL ` RVA 0x345C7220 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a1d6f7b25430895a](../../evidence/conditions-sets-062.md#c-a1d6f7b25430895a) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002955

```text
(config-router-scope-af-topo)# default bgp default route-target filter <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 25 `；EOL ` RVA 0x345C74C0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8b8d63d3237cfa03](../../evidence/conditions-sets-054.md#c-8b8d63d3237cfa03) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002821

```text
(config-router-scope-af-topo)# default bgp deterministic-med <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 10 `；EOL ` RVA 0x345BF580 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ab4874c439cf7460](../../evidence/conditions-sets-066.md#c-ab4874c439cf7460) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002796

```text
(config-router-scope-af-topo)# default bgp dmzlink-bw <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 31 `；EOL ` RVA 0x345CABB8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3adab7f53eab96ed](../../evidence/conditions-sets-023.md#c-3adab7f53eab96ed) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002723

```text
(config-router-scope-af-topo)# default bgp dynamic-med-interval <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 21 `；EOL ` RVA 0x345BF5A8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c50e2821402bb9e3](../../evidence/conditions-sets-076.md#c-c50e2821402bb9e3) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002804

```text
(config-router-scope-af-topo)# default bgp enforce-first-as <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 20 `；EOL ` RVA 0x345BE7B0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ab4874c439cf7460](../../evidence/conditions-sets-066.md#c-ab4874c439cf7460) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002839

```text
(config-router-scope-af-topo)# default bgp enhanced-error <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 82 `；EOL ` RVA 0x345C11F0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6682cdc66ee2fee4](../../evidence/conditions-sets-040.md#c-6682cdc66ee2fee4) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002757

```text
(config-router-scope-af-topo)# default bgp fast-external-fallover <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 1 `；EOL ` RVA 0x345BC498 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ab4874c439cf7460](../../evidence/conditions-sets-066.md#c-ab4874c439cf7460) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002852

```text
(config-router-scope-af-topo)# default bgp graceful-restart <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 35 `；EOL ` RVA 0x345C2060 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ab4874c439cf7460](../../evidence/conditions-sets-066.md#c-ab4874c439cf7460) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002845

```text
(config-router-scope-af-topo)# default bgp graceful-restart restart-time <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 36 `；EOL ` RVA 0x345C1A30 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c82877477f708348](../../evidence/conditions-sets-077.md#c-c82877477f708348) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002847

```text
(config-router-scope-af-topo)# default bgp graceful-restart stalepath-time <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 37 `；EOL ` RVA 0x345C1A98 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7031783c88894352](../../evidence/conditions-sets-043.md#c-7031783c88894352) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-003016

```text
(config-router-scope-af-topo)# default bgp graceful-shutdown all vrfs activate <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 79 `；EOL ` RVA 0x345C24C8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9b1924e01b9a6adb](../../evidence/conditions-sets-060.md#c-9b1924e01b9a6adb) · [状态效果 S-bc1e6173cb28b036](../../evidence/state_effects-sets-040.md#s-bc1e6173cb28b036)

### observed_connections-003014

```text
(config-router-scope-af-topo)# default bgp inject-map <string> exist-map <string> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 32 `；EOL ` RVA 0x345CC730 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` route-map name；` string ` route-map name。

[条件 C-fedb6cae967c9a50](../../evidence/conditions-sets-098.md#c-fedb6cae967c9a50) · [参数 P-c031eb060e8bf349](../../evidence/parameters-sets-015.md#p-c031eb060e8bf349) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002953

```text
(config-router-scope-af-topo)# default bgp label-allocation-batch <number:0..4294967295> <number:0..4294967295> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 53 `；EOL ` RVA 0x345BC828 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Timer value in milliseconds；` unsigned_number ` Batch Size。

[条件 C-ab4874c439cf7460](../../evidence/conditions-sets-066.md#c-ab4874c439cf7460) · [参数 P-25b90a94faeaa469](../../evidence/parameters-sets-003.md#p-25b90a94faeaa469) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002978

```text
(config-router-scope-af-topo)# default bgp listen block <address> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 93 `；EOL ` RVA 0x345CA5C8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IPv4 Dynamic Peering Address。

[条件 C-68b3d1afb9f1515e](../../evidence/conditions-sets-041.md#c-68b3d1afb9f1515e) · [参数 P-4423f7a79b076b21](../../evidence/parameters-sets-006.md#p-4423f7a79b076b21) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002989

```text
(config-router-scope-af-topo)# default bgp listen block <address> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 93 `；EOL ` RVA 0x345C0528 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IPv4 Dynamic Peering Address。

[条件 C-4383b9d78c985b8e](../../evidence/conditions-sets-026.md#c-4383b9d78c985b8e) · [参数 P-11231d0c3b66f126](../../evidence/parameters-sets-002.md#p-11231d0c3b66f126) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002816

```text
(config-router-scope-af-topo)# default bgp listen limit <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 61 `；EOL ` RVA 0x345CA510 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0965838a33a65b88](../../evidence/conditions-sets-004.md#c-0965838a33a65b88) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002841

```text
(config-router-scope-af-topo)# default bgp listen limit <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 61 `；EOL ` RVA 0x345C0448 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1a8aa0eeb10fb66b](../../evidence/conditions-sets-010.md#c-1a8aa0eeb10fb66b) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002930

```text
(config-router-scope-af-topo)# default bgp listen persistent <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 94 `；EOL ` RVA 0x345C0860 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4383b9d78c985b8e](../../evidence/conditions-sets-026.md#c-4383b9d78c985b8e) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002813

```text
(config-router-scope-af-topo)# default bgp log-neighbor-changes <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 11 `；EOL ` RVA 0x345BEA58 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ab4874c439cf7460](../../evidence/conditions-sets-066.md#c-ab4874c439cf7460) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002871

```text
(config-router-scope-af-topo)# default bgp maxas-limit <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 26 `；EOL ` RVA 0x345C5C70 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-102b730ee812e4f1](../../evidence/conditions-sets-006.md#c-102b730ee812e4f1) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002859

```text
(config-router-scope-af-topo)# default bgp maxcommunity-limit <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 27 `；EOL ` RVA 0x345C5280 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-bed8e2864e8d2387](../../evidence/conditions-sets-074.md#c-bed8e2864e8d2387) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002867

```text
(config-router-scope-af-topo)# default bgp maxextcommunity-limit <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 29 `；EOL ` RVA 0x345C5920 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-233a44b08dfeee28](../../evidence/conditions-sets-014.md#c-233a44b08dfeee28) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002863

```text
(config-router-scope-af-topo)# default bgp maxlargecommunity-limit <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 28 `；EOL ` RVA 0x345C55D0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c389abe0bafee3f1](../../evidence/conditions-sets-075.md#c-c389abe0bafee3f1) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002831

```text
(config-router-scope-af-topo)# default bgp mpls-local-label <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 81 `；EOL ` RVA 0x345CCAA8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-31488a0baa289d4d](../../evidence/conditions-sets-019.md#c-31488a0baa289d4d) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002980

```text
(config-router-scope-af-topo)# default bgp nexthop route-map <string> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 56 `；EOL ` RVA 0x345CB320 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` route-map name。

[条件 C-7820ec64c4324b06](../../evidence/conditions-sets-047.md#c-7820ec64c4324b06) · [参数 P-6f819417a906606a](../../evidence/parameters-sets-009.md#p-6f819417a906606a) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002924

```text
(config-router-scope-af-topo)# default bgp nexthop trigger critical-delay <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 48 `；EOL ` RVA 0x345CB888 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-50ad60349bfbef12](../../evidence/conditions-sets-031.md#c-50ad60349bfbef12) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002921

```text
(config-router-scope-af-topo)# default bgp nexthop trigger delay <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 47 `；EOL ` RVA 0x345CB608 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-20b49d9bc5181fec](../../evidence/conditions-sets-013.md#c-20b49d9bc5181fec) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002977

```text
(config-router-scope-af-topo)# default bgp nexthop trigger enable <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 49 `；EOL ` RVA 0x345CB5E0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8afb2da867e5f253](../../evidence/conditions-sets-054.md#c-8afb2da867e5f253) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002985

```text
(config-router-scope-af-topo)# default bgp nopeerup-delay cold-boot <number:1..3600> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 74 `；EOL ` RVA 0x345C0E88 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Delay in seconds。

[条件 C-d307f5eb044f3a7c](../../evidence/conditions-sets-081.md#c-d307f5eb044f3a7c) · [参数 P-ca7b15937712ec27](../../evidence/parameters-sets-015.md#p-ca7b15937712ec27) · [状态效果 S-b9465f63fa635792](../../evidence/state_effects-sets-039.md#s-b9465f63fa635792)

### observed_connections-002899

```text
(config-router-scope-af-topo)# default bgp recursion host <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 72 `；EOL ` RVA 0x345C9980 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-019c433b5d1f87b0](../../evidence/conditions-sets-001.md#c-019c433b5d1f87b0) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002782

```text
(config-router-scope-af-topo)# default bgp redistribute-internal <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 2 `；EOL ` RVA 0x345CDCA8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2ffde756bdc3d691](../../evidence/conditions-sets-019.md#c-2ffde756bdc3d691) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002941

```text
(config-router-scope-af-topo)# default bgp refresh max-eor-time <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 16 `；EOL ` RVA 0x345C3258 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-05988c04cb6433c3](../../evidence/conditions-sets-003.md#c-05988c04cb6433c3) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002937

```text
(config-router-scope-af-topo)# default bgp refresh stalepath-time <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 15 `；EOL ` RVA 0x345C2EE8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5204863675f7f751](../../evidence/conditions-sets-032.md#c-5204863675f7f751) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002939

```text
(config-router-scope-af-topo)# default bgp regexp deterministic <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 44 `；EOL ` RVA 0x345C3C70 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a6d86b91e3f7b225](../../evidence/conditions-sets-064.md#c-a6d86b91e3f7b225) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002900

```text
(config-router-scope-af-topo)# default bgp route-map priority <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 59 `；EOL ` RVA 0x345CEE38 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a57efef1bb356cf9](../../evidence/conditions-sets-064.md#c-a57efef1bb356cf9) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002766

```text
(config-router-scope-af-topo)# default bgp route-map-cache <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 34 `；EOL ` RVA 0x345BCAB0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ab4874c439cf7460](../../evidence/conditions-sets-066.md#c-ab4874c439cf7460) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002775

```text
(config-router-scope-af-topo)# default bgp router-id <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 4 `；EOL ` RVA 0x345BBE68 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8b9a86b090230220](../../evidence/conditions-sets-054.md#c-8b9a86b090230220) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002817

```text
(config-router-scope-af-topo)# default bgp router-id <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 4 `；EOL ` RVA 0x345CA030 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6b7b28d1f67a54bf](../../evidence/conditions-sets-042.md#c-6b7b28d1f67a54bf) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-003020

```text
(config-router-scope-af-topo)# default bgp rpki server tcp <address> port <number:1..65535> refresh <number:1..65535> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 76 `；EOL ` RVA 0x345CFC50 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IPv6 address of RPKI cache server；` unsigned_number ` Port number；` unsigned_number ` Refresh time in seconds。

[条件 C-fd6cda537b929d75](../../evidence/conditions-sets-098.md#c-fd6cda537b929d75) · [参数 P-c7888514a7534998](../../evidence/parameters-sets-015.md#p-c7888514a7534998) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002825

```text
(config-router-scope-af-topo)# default bgp rr-group <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 23 `；EOL ` RVA 0x345CC2C8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-279384ebf0bdeaf9](../../evidence/conditions-sets-016.md#c-279384ebf0bdeaf9) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002872

```text
(config-router-scope-af-topo)# default bgp safe-ebgp-policy <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 92 `；EOL ` RVA 0x345C6208 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c3ec135058645164](../../evidence/conditions-sets-076.md#c-c3ec135058645164) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002923

```text
(config-router-scope-af-topo)# default bgp scan-time <number:5..60> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 22 `；EOL ` RVA 0x345CBF58 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Scanner interval (seconds)。

[条件 C-f6c5e214b2225f3e](../../evidence/conditions-sets-095.md#c-f6c5e214b2225f3e) · [参数 P-75e51e2c3101672c](../../evidence/parameters-sets-009.md#p-75e51e2c3101672c) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002902

```text
(config-router-scope-af-topo)# default bgp slow-peer detection <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 67 `；EOL ` RVA 0x345CCF78 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-68e20aa0ec564438](../../evidence/conditions-sets-041.md#c-68e20aa0ec564438) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002968

```text
(config-router-scope-af-topo)# default bgp slow-peer split-update-group dynamic <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 68 `；EOL ` RVA 0x345CD548 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5e434496224649a6](../../evidence/conditions-sets-037.md#c-5e434496224649a6) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002982

```text
(config-router-scope-af-topo)# default bgp snmp traps add-type <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 90 `；EOL ` RVA 0x345BFB70 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ab4874c439cf7460](../../evidence/conditions-sets-066.md#c-ab4874c439cf7460) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002814

```text
(config-router-scope-af-topo)# default bgp soft-reconfig-backup <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 52 `；EOL ` RVA 0x345CAF08 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-756792ade7cc9960](../../evidence/conditions-sets-046.md#c-756792ade7cc9960) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-003012

```text
(config-router-scope-af-topo)# default bgp sourced-paths per-net isis all <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 89 `；EOL ` RVA 0x345CEAB8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c83d4e3bedad6190](../../evidence/conditions-sets-077.md#c-c83d4e3bedad6190) · [状态效果 S-f2a6bc3a94069193](../../evidence/state_effects-sets-051.md#s-f2a6bc3a94069193)

### observed_connections-003008

```text
(config-router-scope-af-topo)# default bgp sourced-paths per-net ospf all <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 87 `；EOL ` RVA 0x345CE458 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c83d4e3bedad6190](../../evidence/conditions-sets-077.md#c-c83d4e3bedad6190) · [状态效果 S-5398a3f751eb3e34](../../evidence/state_effects-sets-018.md#s-5398a3f751eb3e34)

### observed_connections-003010

```text
(config-router-scope-af-topo)# default bgp sourced-paths per-net ospfv3 all <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 88 `；EOL ` RVA 0x345CE7A0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c83d4e3bedad6190](../../evidence/conditions-sets-077.md#c-c83d4e3bedad6190) · [状态效果 S-b885931208863df8](../../evidence/state_effects-sets-039.md#s-b885931208863df8)

### observed_connections-003006

```text
(config-router-scope-af-topo)# default bgp sourced-paths per-net static all <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 86 `；EOL ` RVA 0x345CE110 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c83d4e3bedad6190](../../evidence/conditions-sets-077.md#c-c83d4e3bedad6190) · [状态效果 S-a8c1f01bb9b0a734](../../evidence/state_effects-sets-036.md#s-a8c1f01bb9b0a734)

### observed_connections-002931

```text
(config-router-scope-af-topo)# default bgp sso route-refresh-enable <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 38 `；EOL ` RVA 0x345C2B28 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a6d86b91e3f7b225](../../evidence/conditions-sets-064.md#c-a6d86b91e3f7b225) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002787

```text
(config-router-scope-af-topo)# default bgp suppress-inactive <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 45 `；EOL ` RVA 0x345C9C80 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-133a19ecba7cce81](../../evidence/conditions-sets-008.md#c-133a19ecba7cce81) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002690

```text
(config-router-scope-af-topo)# default bgp tid <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 55 `；EOL ` RVA 0x345BB6A8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-daadd1d725ee3f94](../../evidence/conditions-sets-084.md#c-daadd1d725ee3f94) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002907

```text
(config-router-scope-af-topo)# default bgp transport path-mtu-discovery <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 50 `；EOL ` RVA 0x345BE520 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ab4874c439cf7460](../../evidence/conditions-sets-066.md#c-ab4874c439cf7460) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002735

```text
(config-router-scope-af-topo)# default bgp update-delay <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 30 `；EOL ` RVA 0x345C14A0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-879c9419fc8ed990](../../evidence/conditions-sets-052.md#c-879c9419fc8ed990) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002961

```text
(config-router-scope-af-topo)# default bgp update-group split as-override <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 73 `；EOL ` RVA 0x345CD918 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4969fbb5328f8a37](../../evidence/conditions-sets-029.md#c-4969fbb5328f8a37) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002763

```text
(config-router-scope-af-topo)# default bgp upgrade-cli <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 33 `；EOL ` RVA 0x345BBAC0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9780fe2be46b60d7](../../evidence/conditions-sets-058.md#c-9780fe2be46b60d7) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002807

```text
(config-router-scope-af-topo)# default bgp va <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 80 `；EOL ` RVA 0x345CF1E0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-26892144eff9abfa](../../evidence/conditions-sets-015.md#c-26892144eff9abfa) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002935

```text
(config-router-scope-af-topo)# default bgp vrf-update-optimisation off <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 66 `；EOL ` RVA 0x345C35E0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a6d86b91e3f7b225](../../evidence/conditions-sets-064.md#c-a6d86b91e3f7b225) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002855

```text
(config-router-scope-af-topo)# default bgp write-limit <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 40 `；EOL ` RVA 0x345C3938 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-762135fdb5ef5b01](../../evidence/conditions-sets-046.md#c-762135fdb5ef5b01) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002684

```text
(config-router-scope-af-topo)# default context <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 0 `；EOL ` RVA 0x33C44A60 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ada418e0516d363b](../../evidence/conditions-sets-067.md#c-ada418e0516d363b) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002829

```text
(config-router-scope-af-topo)# default default-information originate <cr>
```

Handler ` RVA 0xE1F1F70 `；selector ` 0 `；EOL ` RVA 0x344F59A8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a9575d4774f8de5d](../../evidence/conditions-sets-065.md#c-a9575d4774f8de5d) · [状态效果 S-61ab4e34de34cd32](../../evidence/state_effects-sets-021.md#s-61ab4e34de34cd32)

### observed_connections-002726

```text
(config-router-scope-af-topo)# default default-metric <cr>
```

Handler ` RVA 0xE1F35A0 `；selector ` 0 `；EOL ` RVA 0x344F6270 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7412fd70c0f11908](../../evidence/conditions-sets-045.md#c-7412fd70c0f11908) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002734

```text
(config-router-scope-af-topo)# default distance <cr>
```

Handler ` RVA 0xE1E3290 `；selector ` 1 `；EOL ` RVA 0x344F73A0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8507c54e95cd8959](../../evidence/conditions-sets-051.md#c-8507c54e95cd8959) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002836

```text
(config-router-scope-af-topo)# default distance bgp <cr>
```

Handler ` RVA 0xF1B8400 `；selector ` 1 `；EOL ` RVA 0x344E1458 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b241df4e6f36d579](../../evidence/conditions-sets-069.md#c-b241df4e6f36d579) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002844

```text
(config-router-scope-af-topo)# default distance mbgp <cr>
```

Handler ` RVA 0xF1B8400 `；selector ` 2 `；EOL ` RVA 0x344E1850 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad31524aadb46fbf](../../evidence/conditions-sets-067.md#c-ad31524aadb46fbf) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002843

```text
(config-router-scope-af-topo)# default distribute-list in <cr>
```

Handler ` RVA 0xE1EE180 `；selector ` 0 `；EOL ` RVA 0x344F6960 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ea8c888fa5896889](../../evidence/conditions-sets-091.md#c-ea8c888fa5896889) · [状态效果 S-fdd1b8cf54f3c4ac](../../evidence/state_effects-sets-054.md#s-fdd1b8cf54f3c4ac)

### observed_connections-002677

```text
(config-router-scope-af-topo)# default flash-update-threshold <cr>
```

Handler ` RVA 0xE1F7ED0 `；selector ` 0 `；EOL ` RVA 0x344F5498 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0e6ae0e65ef7f08e](../../evidence/conditions-sets-006.md#c-0e6ae0e65ef7f08e) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002698

```text
(config-router-scope-af-topo)# default import <cr>
```

Handler ` RVA 0xF08D6A0 `；selector ` 0 `；EOL ` RVA 0x345B9A18 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a0c800ed54083c83](../../evidence/conditions-sets-062.md#c-a0c800ed54083c83) · [状态效果 S-bf5d74f32c01607e](../../evidence/state_effects-sets-040.md#s-bf5d74f32c01607e)

### observed_connections-002878

```text
(config-router-scope-af-topo)# default import l2vpn evpn <cr>
```

Handler ` RVA 0xF08DFA0 `；selector ` 0 `；EOL ` RVA 0x345BA798 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d5076489d906cbe5](../../evidence/conditions-sets-082.md#c-d5076489d906cbe5) · [状态效果 S-000bd2a7659160d9](../../evidence/state_effects-sets-001.md#s-000bd2a7659160d9)

### observed_connections-002752

```text
(config-router-scope-af-topo)# default import nhrp <cr>
```

Handler ` RVA 0xF263450 `；selector ` 0 `；EOL ` RVA 0x345BAB78 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4ecfb69fa69530ad](../../evidence/conditions-sets-031.md#c-4ecfb69fa69530ad) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002875

```text
(config-router-scope-af-topo)# default import vpnv4 unicast <cr>
```

Handler ` RVA 0xF08E500 `；selector ` 0 `；EOL ` RVA 0x345BA228 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4b081c7193042454](../../evidence/conditions-sets-029.md#c-4b081c7193042454) · [状态效果 S-5754273e6180ac5a](../../evidence/state_effects-sets-019.md#s-5754273e6180ac5a)

### observed_connections-002675

```text
(config-router-scope-af-topo)# default input-queue <cr>
```

Handler ` RVA 0xE1F8060 `；selector ` 0 `；EOL ` RVA 0x344F51A8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c4824c7cac4b28be](../../evidence/conditions-sets-076.md#c-c4824c7cac4b28be) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002764

```text
(config-router-scope-af-topo)# default label mode <cr>
```

Handler ` RVA 0xF1D1A30 `；selector ` 0 `；EOL ` RVA 0x344F20C8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5cf0aca29de8310d](../../evidence/conditions-sets-036.md#c-5cf0aca29de8310d) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002778

```text
(config-router-scope-af-topo)# default metric holddown <cr>
```

Handler ` RVA 0xE1F32D0 `；selector ` 1 `；EOL ` RVA 0x344F3AF0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4bbe96da81617452](../../evidence/conditions-sets-030.md#c-4bbe96da81617452) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002711

```text
(config-router-scope-af-topo)# default metric maximum-hops <cr>
```

Handler ` RVA 0xE1F32D0 `；selector ` 2 `；EOL ` RVA 0x344F3B18 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8221b40cbcf421f4](../../evidence/conditions-sets-050.md#c-8221b40cbcf421f4) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002800

```text
(config-router-scope-af-topo)# default metric weights <cr>
```

Handler ` RVA 0xE1F32D0 `；selector ` 0 `；EOL ` RVA 0x344F40D8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-74aaeceddc53dc5d](../../evidence/conditions-sets-045.md#c-74aaeceddc53dc5d) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002884

```text
(config-router-scope-af-topo)# default offset-list <number:0..99> in <cr>
```

Handler ` RVA 0xE1F1330 `；selector ` 0 `；EOL ` RVA 0x344F1278 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Access list of networks to apply offset (0 selects all networks)。

[条件 C-b7414ba60af25c7b](../../evidence/conditions-sets-071.md#c-b7414ba60af25c7b) · [参数 P-583d525582bab90e](../../evidence/parameters-sets-007.md#p-583d525582bab90e) · [状态效果 S-f1144167864b2983](../../evidence/state_effects-sets-051.md#s-f1144167864b2983)

### observed_connections-002668

```text
(config-router-scope-af-topo)# default output-delay <cr>
```

Handler ` RVA 0xE1F4590 `；selector ` 0 `；EOL ` RVA 0x344F0CD0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-75b85446d28e76e2](../../evidence/conditions-sets-046.md#c-75b85446d28e76e2) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002753

```text
(config-router-scope-af-topo)# default passive-interface default <cr>
```

Handler ` RVA 0xE1F3960 `；selector ` 0 `；EOL ` RVA 0x344F08C0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-66b93bc17fdac1bf](../../evidence/conditions-sets-040.md#c-66b93bc17fdac1bf) · [状态效果 S-f3fa2be5b25842ef](../../evidence/state_effects-sets-052.md#s-f3fa2be5b25842ef)

### observed_connections-002695

```text
(config-router-scope-af-topo)# default propagate-aspath <cr>
```

Handler ` RVA 0xF1D1560 `；selector ` 1 `；EOL ` RVA 0x344F1A40 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f1958560caef3b6e](../../evidence/conditions-sets-093.md#c-f1958560caef3b6e) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002699

```text
(config-router-scope-af-topo)# default propagate-community <cr>
```

Handler ` RVA 0xF1D1560 `；selector ` 2 `；EOL ` RVA 0x344F1CE8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f1958560caef3b6e](../../evidence/conditions-sets-093.md#c-f1958560caef3b6e) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002751

```text
(config-router-scope-af-topo)# default redistribute maximum-prefix <cr>
```

Handler ` RVA 0xE1E4550 `；selector ` 0 `；EOL ` RVA 0x344ED8B8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4aeb6ea7334e51cb](../../evidence/conditions-sets-029.md#c-4aeb6ea7334e51cb) · [状态效果 S-10001ea58903f9ec](../../evidence/state_effects-sets-004.md#s-10001ea58903f9ec)

### observed_connections-002756

```text
(config-router-scope-af-topo)# default snmp context <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 0 `；EOL ` RVA 0x33C455F0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7598dc8aeb3669dc](../../evidence/conditions-sets-046.md#c-7598dc8aeb3669dc) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-003004

```text
(config-router-scope-af-topo)# default snmp context <string> community <string> <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 2 `；EOL ` RVA 0x33C45118 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Context Name；` string ` SNMP community string。

[条件 C-2573c969c66067b6](../../evidence/conditions-sets-015.md#c-2573c969c66067b6) · [参数 P-9b6eb89831feec60](../../evidence/parameters-sets-012.md#p-9b6eb89831feec60) · [状态效果 S-b8da3eee45949cd2](../../evidence/state_effects-sets-039.md#s-b8da3eee45949cd2)

### observed_connections-003003

```text
(config-router-scope-af-topo)# default snmp context <string> user <string> <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 23 `；EOL ` RVA 0x33C456D0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Context Name；` string ` Name of the user。

[条件 C-67e2e80e2c1c144d](../../evidence/conditions-sets-040.md#c-67e2e80e2c1c144d) · [参数 P-cfc42ec8ad667e32](../../evidence/parameters-sets-016.md#p-cfc42ec8ad667e32) · [状态效果 S-0609d1497ad3ce21](../../evidence/state_effects-sets-002.md#s-0609d1497ad3ce21)

### observed_connections-002877

```text
(config-router-scope-af-topo)# default summary-prefix <address> <address> <cr>
```

Handler ` RVA 0xE1DF4C0 `；selector ` 0 `；EOL ` RVA 0x344ECB38 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IP summary address；` address ` Summary mask。

[条件 C-2cd36336053d115f](../../evidence/conditions-sets-018.md#c-2cd36336053d115f) · [参数 P-aebe586c61a4934d](../../evidence/parameters-sets-013.md#p-aebe586c61a4934d) · [状态效果 S-7749eb0b732820a7](../../evidence/state_effects-sets-025.md#s-7749eb0b732820a7)

### observed_connections-002746

```text
(config-router-scope-af-topo)# default summary-prefix <address> <cr>
```

Handler ` RVA 0xE1DF4C0 `；selector ` 21 `；EOL ` RVA 0x344ED118 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IP summary address。

[条件 C-1a963b03b7350236](../../evidence/conditions-sets-010.md#c-1a963b03b7350236) · [参数 P-b5381e36e4d9d9b2](../../evidence/parameters-sets-014.md#p-b5381e36e4d9d9b2) · [状态效果 S-7749eb0b732820a7](../../evidence/state_effects-sets-025.md#s-7749eb0b732820a7)

### observed_connections-002687

```text
(config-router-scope-af-topo)# default synchronization <cr>
```

Handler ` RVA 0xF1CF320 `；selector ` 0 `；EOL ` RVA 0x345BAF38 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6acc88802a133995](../../evidence/conditions-sets-041.md#c-6acc88802a133995) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002697

```text
(config-router-scope-af-topo)# default table-map <cr>
```

Handler ` RVA 0xE1F4690 `；selector ` 0 `；EOL ` RVA 0x345BB310 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a213098a7f2bb948](../../evidence/conditions-sets-063.md#c-a213098a7f2bb948) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002683

```text
(config-router-scope-af-topo)# default version <cr>
```

Handler ` RVA 0xFB4F020 `；selector ` 0 `；EOL ` RVA 0x344EC5E8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-af24935869a2b032](../../evidence/conditions-sets-068.md#c-af24935869a2b032) · [状态效果 S-d714698b921a3643](../../evidence/state_effects-sets-046.md#s-d714698b921a3643)

### observed_connections-002725

```text
(config-router-scope-af-topo)# default-information originate <cr>
```

Handler ` RVA 0xE1F1F70 `；selector ` 0 `；EOL ` RVA 0x344F59A8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a9575d4774f8de5d](../../evidence/conditions-sets-065.md#c-a9575d4774f8de5d) · [状态效果 S-5d6c1fc095b9a969](../../evidence/state_effects-sets-020.md#s-5d6c1fc095b9a969)

### observed_connections-002727

```text
(config-router-scope-af-topo)# default-metric <number:1..16777214> <cr>
```

Handler ` RVA 0xE1F35A0 `；selector ` 0 `；EOL ` RVA 0x344F6270 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` OSPF default metric。

[条件 C-94b0514c823ae0a4](../../evidence/conditions-sets-057.md#c-94b0514c823ae0a4) · [参数 P-fc483cf9a933f3c9](../../evidence/parameters-sets-019.md#p-fc483cf9a933f3c9)

### observed_connections-002729

```text
(config-router-scope-af-topo)# distance <number:1..255> <cr>
```

Handler ` RVA 0xE1E3290 `；selector ` 1 `；EOL ` RVA 0x344F73A0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Administrative distance。

[条件 C-fa4013929c785873](../../evidence/conditions-sets-097.md#c-fa4013929c785873) · [参数 P-93d0335cadd4fa38](../../evidence/parameters-sets-011.md#p-93d0335cadd4fa38)

### observed_connections-002986

```text
(config-router-scope-af-topo)# distance bgp <number:1..255> <number:1..255> <number:1..255> <cr>
```

Handler ` RVA 0xF1B8400 `；selector ` 1 `；EOL ` RVA 0x344E1458 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Distance for routes external to the AS；` unsigned_number ` Distance for routes internal to the AS；` unsigned_number ` Distance for local routes。

[条件 C-58f37f679a5a994b](../../evidence/conditions-sets-035.md#c-58f37f679a5a994b) · [参数 P-da75e935134966de](../../evidence/parameters-sets-016.md#p-da75e935134966de)

### observed_connections-002988

```text
(config-router-scope-af-topo)# distance mbgp <number:0..255> <number:0..255> <number:0..255> <cr>
```

Handler ` RVA 0xF1B8400 `；selector ` 2 `；EOL ` RVA 0x344E1850 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Distance for routes external to the AS；` unsigned_number ` Distance for routes internal to the AS；` unsigned_number ` Distance for local routes。

[条件 C-d85a73f5e0afe600](../../evidence/conditions-sets-083.md#c-d85a73f5e0afe600) · [参数 P-fe1448f258db0f35](../../evidence/parameters-sets-019.md#p-fe1448f258db0f35)

### observed_connections-002736

```text
(config-router-scope-af-topo)# distribute-list in <cr>
```

Handler ` RVA 0xE1EE180 `；selector ` 0 `；EOL ` RVA 0x344F6960 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ea8c888fa5896889](../../evidence/conditions-sets-091.md#c-ea8c888fa5896889) · [状态效果 S-ab5262da43f039dd](../../evidence/state_effects-sets-036.md#s-ab5262da43f039dd)

### observed_connections-003077

```text
(config-router-scope-af-topo)# distribute-list out <?router_action_proc_vpn@555589a4a8e8> <cr>
```

Handler ` RVA 0xE1EE180 `；selector ` 0 `；EOL ` RVA 0x344F6960 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f2a9fe0c9ea0a6f4](../../evidence/conditions-sets-094.md#c-f2a9fe0c9ea0a6f4) · [缺口 G-2e21ce0a3cebe79d](../../evidence/gaps-sets-002.md#g-2e21ce0a3cebe79d) · [状态效果 S-1aa6b36ada32d509](../../evidence/state_effects-sets-006.md#s-1aa6b36ada32d509)

### observed_connections-002665

```text
(config-router-scope-af-topo)# exit <cr>
```

Handler ` RVA 0xF1EE5C0 `；selector ` 0 `；EOL ` RVA 0x345B8F48 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-91b46c0c173490ab](../../evidence/conditions-sets-056.md#c-91b46c0c173490ab)

### observed_connections-002664

```text
(config-router-scope-af-topo)# flash-update-threshold <number:0..30> <cr>
```

Handler ` RVA 0xE1F7ED0 `；selector ` 0 `；EOL ` RVA 0x344F5498 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` threshold in seconds。

[条件 C-a987807880c47e2b](../../evidence/conditions-sets-065.md#c-a987807880c47e2b) · [参数 P-a2345e205347a59e](../../evidence/parameters-sets-012.md#p-a2345e205347a59e)

### observed_connections-002671

```text
(config-router-scope-af-topo)# import <cr>
```

Handler ` RVA 0xF08D6A0 `；selector ` 0 `；EOL ` RVA 0x345B9A18 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a0c800ed54083c83](../../evidence/conditions-sets-062.md#c-a0c800ed54083c83) · [状态效果 S-e912bade4661545c](../../evidence/state_effects-sets-049.md#s-e912bade4661545c)

### observed_connections-002748

```text
(config-router-scope-af-topo)# import l2vpn evpn <cr>
```

Handler ` RVA 0xF08DFA0 `；selector ` 0 `；EOL ` RVA 0x345BA798 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d5076489d906cbe5](../../evidence/conditions-sets-082.md#c-d5076489d906cbe5) · [状态效果 S-cffd7c08a1ac245a](../../evidence/state_effects-sets-044.md#s-cffd7c08a1ac245a)

### observed_connections-002691

```text
(config-router-scope-af-topo)# import nhrp <cr>
```

Handler ` RVA 0xF263450 `；selector ` 0 `；EOL ` RVA 0x345BAB78 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4ecfb69fa69530ad](../../evidence/conditions-sets-031.md#c-4ecfb69fa69530ad)

### observed_connections-003099

```text
(config-router-scope-af-topo)# import path selection <?option@555589b0dd00> <cr>
```

Handler ` RVA 0xF08D6A0 `；selector ` 0 `；EOL ` RVA 0x345B9A18 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c85a7668204187a0](../../evidence/conditions-sets-077.md#c-c85a7668204187a0) · [缺口 G-8d91b41b9fba1b2b](../../evidence/gaps-sets-005.md#g-8d91b41b9fba1b2b) · [状态效果 S-99f4d31b1357456f](../../evidence/state_effects-sets-033.md#s-99f4d31b1357456f)

### observed_connections-002744

```text
(config-router-scope-af-topo)# import vpnv4 unicast <cr>
```

Handler ` RVA 0xF08E500 `；selector ` 0 `；EOL ` RVA 0x345BA228 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4b081c7193042454](../../evidence/conditions-sets-029.md#c-4b081c7193042454) · [状态效果 S-b2ac2b81f5ae6a4f](../../evidence/state_effects-sets-038.md#s-b2ac2b81f5ae6a4f)

### observed_connections-002663

```text
(config-router-scope-af-topo)# input-queue <number:0..1024> <cr>
```

Handler ` RVA 0xE1F8060 `；selector ` 0 `；EOL ` RVA 0x344F51A8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` queue depth。

[条件 C-9fd5ba85a10ee162](../../evidence/conditions-sets-062.md#c-9fd5ba85a10ee162) · [参数 P-5267c0140d4e52a7](../../evidence/parameters-sets-007.md#p-5267c0140d4e52a7)

### observed_connections-003073

```text
(config-router-scope-af-topo)# label mode all-explicit-null <cr>
```

Handler ` RVA 0xF1D1A30 `；selector ` 2 `；EOL ` RVA 0x344F2410 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-196d3da51f3953c9](../../evidence/conditions-sets-010.md#c-196d3da51f3953c9) · [缺口 G-dc64f1c5cb22dabb](../../evidence/gaps-sets-008.md#g-dc64f1c5cb22dabb) · [状态效果 S-a45599ec6583c65b](../../evidence/state_effects-sets-035.md#s-a45599ec6583c65b)

### observed_connections-003072

```text
(config-router-scope-af-topo)# label mode explicit-null <cr>
```

Handler ` RVA 0xF1D1A30 `；selector ` 1 `；EOL ` RVA 0x344F2158 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-196d3da51f3953c9](../../evidence/conditions-sets-010.md#c-196d3da51f3953c9) · [缺口 G-6ace9773ef4ef6df](../../evidence/gaps-sets-004.md#g-6ace9773ef4ef6df) · [状态效果 S-8bd26dbd0a18e1e8](../../evidence/state_effects-sets-030.md#s-8bd26dbd0a18e1e8)

### observed_connections-003033

```text
(config-router-scope-af-topo)# maximum-paths <number:dynamic> <cr>
```

Handler ` RVA 0xE1E26B0 `；selector ` 0 `；EOL ` RVA 0x344F4CC0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Number of paths。

[条件 C-c4d2c8b573521027](../../evidence/conditions-sets-076.md#c-c4d2c8b573521027) · [缺口 G-d1981088f6fbd147](../../evidence/gaps-sets-007.md#g-d1981088f6fbd147) · [参数 P-aa581bb178e213f9](../../evidence/parameters-sets-013.md#p-aa581bb178e213f9)

### observed_connections-003032

```text
(config-router-scope-af-topo)# maximum-secondary-paths <number:dynamic> <cr>
```

Handler ` RVA 0xE1E2BD0 `；selector ` 0 `；EOL ` RVA 0x344F4758 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Number of secondary paths。

[条件 C-61ee179365919407](../../evidence/conditions-sets-038.md#c-61ee179365919407) · [缺口 G-19a9bd177250c456](../../evidence/gaps-sets-001.md#g-19a9bd177250c456) · [参数 P-20172f83589f021e](../../evidence/parameters-sets-003.md#p-20172f83589f021e)

### observed_connections-002707

```text
(config-router-scope-af-topo)# metric holddown <cr>
```

Handler ` RVA 0xE1F32D0 `；selector ` 1 `；EOL ` RVA 0x344F3AF0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4bbe96da81617452](../../evidence/conditions-sets-030.md#c-4bbe96da81617452)

### observed_connections-002673

```text
(config-router-scope-af-topo)# metric maximum-hops <number:1..255> <cr>
```

Handler ` RVA 0xE1F32D0 `；selector ` 2 `；EOL ` RVA 0x344F3B18 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Hop count。

[条件 C-4f06080100d9aa31](../../evidence/conditions-sets-031.md#c-4f06080100d9aa31) · [参数 P-ade92f03be8d75a4](../../evidence/parameters-sets-013.md#p-ade92f03be8d75a4)

### observed_connections-003017

```text
(config-router-scope-af-topo)# metric weights <number:0..8> <number:0..255> <number:0..255> <number:0..255> <number:0..255> <number:0..255> <cr>
```

Handler ` RVA 0xE1F32D0 `；selector ` 0 `；EOL ` RVA 0x344F40D8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Type Of Service (Only TOS 0 supported)；` unsigned_number ` K1；` unsigned_number ` K2；` unsigned_number ` K3；` unsigned_number ` K4；` unsigned_number ` K5。

[条件 C-d7dd7842e679d454](../../evidence/conditions-sets-083.md#c-d7dd7842e679d454) · [参数 P-814573c6aff87ec0](../../evidence/parameters-sets-010.md#p-814573c6aff87ec0)

### observed_connections-003022

```text
(config-router-scope-af-topo)# neighbor <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 0 `；EOL ` RVA 0x344FAE30 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-13bab7a73be6995a](../../evidence/conditions-sets-008.md#c-13bab7a73be6995a) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-003024

```text
(config-router-scope-af-topo)# neighbor <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 0 `；EOL ` RVA 0x34514EB0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1c96f9a1eaa0749d](../../evidence/conditions-sets-011.md#c-1c96f9a1eaa0749d) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-003056

```text
(config-router-scope-af-topo)# neighbor accept-route-legacy-rt <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 71 `；EOL ` RVA 0x3450FCA0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-60e9cf81e8aa848e](../../evidence/conditions-sets-038.md#c-60e9cf81e8aa848e) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-003062

```text
(config-router-scope-af-topo)# neighbor activate <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 35 `；EOL ` RVA 0x34512F58 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ad8ccca0d04a9c9e](../../evidence/conditions-sets-067.md#c-ad8ccca0d04a9c9e) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-003059

```text
(config-router-scope-af-topo)# neighbor additional-paths <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 79 `；EOL ` RVA 0x34510680 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c21872e8d31dd697](../../evidence/conditions-sets-075.md#c-c21872e8d31dd697) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-310f72b0202c01f0](../../evidence/state_effects-sets-011.md#s-310f72b0202c01f0)

### observed_connections-003090

```text
(config-router-scope-af-topo)# neighbor advertise additional-paths <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 78 `；EOL ` RVA 0x34510D88 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-192897edda681854](../../evidence/conditions-sets-010.md#c-192897edda681854) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-f5e7703a312d3e8e](../../evidence/state_effects-sets-052.md#s-f5e7703a312d3e8e)

### observed_connections-003088

```text
(config-router-scope-af-topo)# neighbor advertise best-external <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 80 `；EOL ` RVA 0x34511438 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e02361fb7eb19d65](../../evidence/conditions-sets-086.md#c-e02361fb7eb19d65) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-003114

```text
(config-router-scope-af-topo)# neighbor advertise diverse-path mpath <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 78 `；EOL ` RVA 0x34511158 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e02361fb7eb19d65](../../evidence/conditions-sets-086.md#c-e02361fb7eb19d65) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-bb007f0b56515910](../../evidence/state_effects-sets-039.md#s-bb007f0b56515910)

### observed_connections-003070

```text
(config-router-scope-af-topo)# neighbor advertise-gw-ip-disable <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 88 `；EOL ` RVA 0x34517350 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-919986923aaf465d](../../evidence/conditions-sets-056.md#c-919986923aaf465d) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-003118

```text
(config-router-scope-af-topo)# neighbor advertise-map <string> non-exist-map <string> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 39 `；EOL ` RVA 0x34513788 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` advertise route-map name；` string ` condition route-map name。

[条件 C-f0f800ded2b1c519](../../evidence/conditions-sets-093.md#c-f0f800ded2b1c519) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [参数 P-5700454f0b4c63c1](../../evidence/parameters-sets-007.md#p-5700454f0b4c63c1) · [状态效果 S-beeff3187c70c5dc](../../evidence/state_effects-sets-040.md#s-beeff3187c70c5dc)

### observed_connections-003047

```text
(config-router-scope-af-topo)# neighbor advertisement-interval <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 40 `；EOL ` RVA 0x3450B210 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-197ad609ce2b0755](../../evidence/conditions-sets-010.md#c-197ad609ce2b0755) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-003057

```text
(config-router-scope-af-topo)# neighbor aigp <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 50 `；EOL ` RVA 0x3450F8A0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d24ccc0a4da823d3](../../evidence/conditions-sets-081.md#c-d24ccc0a4da823d3) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-77488c72b6e8ed60](../../evidence/state_effects-sets-025.md#s-77488c72b6e8ed60)

### observed_connections-003058

```text
(config-router-scope-af-topo)# neighbor allow-policy <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 51 `；EOL ` RVA 0x345102D0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-171e78d3b71fbcbf](../../evidence/conditions-sets-009.md#c-171e78d3b71fbcbf) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-003043

```text
(config-router-scope-af-topo)# neighbor allowas-in <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 60 `；EOL ` RVA 0x34509FA8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8f00fb7563a28c95](../../evidence/conditions-sets-055.md#c-8f00fb7563a28c95) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-003108

```text
(config-router-scope-af-topo)# neighbor announce rpki state <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 77 `；EOL ` RVA 0x3450A798 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e691aedb1d2d97bd](../../evidence/conditions-sets-089.md#c-e691aedb1d2d97bd) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-003094

```text
(config-router-scope-af-topo)# neighbor ao <string> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 22 `；EOL ` RVA 0x345163A0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Keychain name。

[条件 C-a2611dcb8d2ee112](../../evidence/conditions-sets-063.md#c-a2611dcb8d2ee112) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [参数 P-da5db2abf7b4d80d](../../evidence/parameters-sets-016.md#p-da5db2abf7b4d80d) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-003065

```text
(config-router-scope-af-topo)# neighbor as-override <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 61 `；EOL ` RVA 0x34514238 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c8ab98fc01ef13fe](../../evidence/conditions-sets-077.md#c-c8ab98fc01ef13fe) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-003119

```text
(config-router-scope-af-topo)# neighbor capability orf prefix-list send <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 65 `；EOL ` RVA 0x34514680 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8b97c64536681f4e](../../evidence/conditions-sets-054.md#c-8b97c64536681f4e) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-bc48cf26c3524396](../../evidence/state_effects-sets-040.md#s-bc48cf26c3524396)

### observed_connections-003067

```text
(config-router-scope-af-topo)# neighbor cluster-id <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 23 `；EOL ` RVA 0x34516768 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6ea8a4d8120fe344](../../evidence/conditions-sets-043.md#c-6ea8a4d8120fe344) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-003052

```text
(config-router-scope-af-topo)# neighbor default-originate <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 52 `；EOL ` RVA 0x3450DCD0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-232002e2b94e88a8](../../evidence/conditions-sets-014.md#c-232002e2b94e88a8) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-003061

```text
(config-router-scope-af-topo)# neighbor description <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 8 `；EOL ` RVA 0x34512C20 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e88517045e0c013f](../../evidence/conditions-sets-090.md#c-e88517045e0c013f) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-003041

```text
(config-router-scope-af-topo)# neighbor disable-connected-check <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 13 `；EOL ` RVA 0x34509318 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-10dd06267d084e20](../../evidence/conditions-sets-007.md#c-10dd06267d084e20) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-9f0d6cbe68a958da](../../evidence/state_effects-sets-034.md#s-9f0d6cbe68a958da)

### observed_connections-003104

```text
(config-router-scope-af-topo)# neighbor distribute-list <number:1..199> in <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 45 `；EOL ` RVA 0x345064A0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` IP access list number。

[条件 C-d9c9086da3f4ebe4](../../evidence/conditions-sets-084.md#c-d9c9086da3f4ebe4) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [参数 P-0797f33209a82d83](../../evidence/parameters-sets-001.md#p-0797f33209a82d83) · [状态效果 S-abc7de4585cab362](../../evidence/state_effects-sets-036.md#s-abc7de4585cab362)

### observed_connections-003039

```text
(config-router-scope-af-topo)# neighbor dmzlink-bw <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 63 `；EOL ` RVA 0x34507DA0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8571c652afdb9a9f](../../evidence/conditions-sets-052.md#c-8571c652afdb9a9f) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-cccb14bcb9ec38cb](../../evidence/state_effects-sets-043.md#s-cccb14bcb9ec38cb)

### observed_connections-003036

```text
(config-router-scope-af-topo)# neighbor dont-capability-negotiate <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 16 `；EOL ` RVA 0x34505060 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e58430b9c4f0f9ae](../../evidence/conditions-sets-089.md#c-e58430b9c4f0f9ae) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-003076

```text
(config-router-scope-af-topo)# neighbor dont-capability-negotiate enhanced-refresh <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 18 `；EOL ` RVA 0x34505038 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e58430b9c4f0f9ae](../../evidence/conditions-sets-089.md#c-e58430b9c4f0f9ae) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-003074

```text
(config-router-scope-af-topo)# neighbor dont-capability-negotiate four-octets-as <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 17 `；EOL ` RVA 0x34504D90 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e58430b9c4f0f9ae](../../evidence/conditions-sets-089.md#c-e58430b9c4f0f9ae) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-003051

```text
(config-router-scope-af-topo)# neighbor ebgp-multihop <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 6 `；EOL ` RVA 0x3450D8A8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-77b29bcbf6938ac1](../../evidence/conditions-sets-047.md#c-77b29bcbf6938ac1) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-147c8497d59aab13](../../evidence/state_effects-sets-005.md#s-147c8497d59aab13)

### observed_connections-003095

```text
(config-router-scope-af-topo)# neighbor encap srv6 <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 86 `；EOL ` RVA 0x34517778 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4cd15865852f0942](../../evidence/conditions-sets-030.md#c-4cd15865852f0942) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-ce3e01bc3a1db752](../../evidence/state_effects-sets-044.md#s-ce3e01bc3a1db752)

### observed_connections-003044

```text
(config-router-scope-af-topo)# neighbor fall-over <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 26 `；EOL ` RVA 0x34509670 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-03fa6bb6e2648f91](../../evidence/conditions-sets-002.md#c-03fa6bb6e2648f91) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-ea869f48fdbad9a6](../../evidence/state_effects-sets-050.md#s-ea869f48fdbad9a6)

### observed_connections-003107

```text
(config-router-scope-af-topo)# neighbor filter-list <number:1..500> in <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 44 `；EOL ` RVA 0x34507280 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` AS path access list。

[条件 C-eeeedb84ea6e6a17](../../evidence/conditions-sets-092.md#c-eeeedb84ea6e6a17) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [参数 P-32386b885f3a56a1](../../evidence/parameters-sets-004.md#p-32386b885f3a56a1) · [状态效果 S-30faed4ccbccec2e](../../evidence/state_effects-sets-011.md#s-30faed4ccbccec2e)

### observed_connections-003035

```text
(config-router-scope-af-topo)# neighbor force-open-collision <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 15 `；EOL ` RVA 0x345055F0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-289a431576c5a2de](../../evidence/conditions-sets-016.md#c-289a431576c5a2de) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-003097

```text
(config-router-scope-af-topo)# neighbor ha-mode graceful-restart <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 28 `；EOL ` RVA 0x344FB150 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7e41f7d7f62c88c6](../../evidence/conditions-sets-049.md#c-7e41f7d7f62c88c6) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-003098

```text
(config-router-scope-af-topo)# neighbor ha-mode sso <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 29 `；EOL ` RVA 0x3372E478 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7e41f7d7f62c88c6](../../evidence/conditions-sets-049.md#c-7e41f7d7f62c88c6) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-003113

```text
(config-router-scope-af-topo)# neighbor inherit peer-policy <string> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 36 `；EOL ` RVA 0x345118B0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Template name。

[条件 C-cbdd0eedb1248b5c](../../evidence/conditions-sets-078.md#c-cbdd0eedb1248b5c) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [参数 P-830038faf9dd3fd6](../../evidence/parameters-sets-010.md#p-830038faf9dd3fd6) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-003112

```text
(config-router-scope-af-topo)# neighbor inherit peer-session <string> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 19 `；EOL ` RVA 0x34511BC8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Template name。

[条件 C-c0ab4d89634c404f](../../evidence/conditions-sets-074.md#c-c0ab4d89634c404f) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [参数 P-0e28cc940f3097c3](../../evidence/parameters-sets-002.md#p-0e28cc940f3097c3) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-003054

```text
(config-router-scope-af-topo)# neighbor inter-as-hybrid <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 72 `；EOL ` RVA 0x3450F280 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-225a9309aed7568c](../../evidence/conditions-sets-013.md#c-225a9309aed7568c) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-003064

```text
(config-router-scope-af-topo)# neighbor internal-vpn-client <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 82 `；EOL ` RVA 0x34513E80 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-358884266787c0b1](../../evidence/conditions-sets-021.md#c-358884266787c0b1) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-003042

```text
(config-router-scope-af-topo)# neighbor local-as <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 11 `；EOL ` RVA 0x34508EA0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a3c15a1e7ce2c66b](../../evidence/conditions-sets-063.md#c-a3c15a1e7ce2c66b) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-003071

```text
(config-router-scope-af-topo)# neighbor log-neighbor-changes <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 32 `；EOL ` RVA 0x34517FB0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6404bb904798fc4d](../../evidence/conditions-sets-039.md#c-6404bb904798fc4d) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-003069

```text
(config-router-scope-af-topo)# neighbor long-lived-graceful-restart <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 85 `；EOL ` RVA 0x34516B88 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9d9516f08ea397fc](../../evidence/conditions-sets-061.md#c-9d9516f08ea397fc) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-003089

```text
(config-router-scope-af-topo)# neighbor maximum-prefix <number:1..2147483647> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 59 `；EOL ` RVA 0x34512728 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` maximum no. of prefix limit。

[条件 C-3d591c7f1e356b3f](../../evidence/conditions-sets-024.md#c-3d591c7f1e356b3f) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [参数 P-13ee3dfd3e93b318](../../evidence/parameters-sets-002.md#p-13ee3dfd3e93b318) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-003049

```text
(config-router-scope-af-topo)# neighbor next-hop-self <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 42 `；EOL ` RVA 0x3450C478 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f4351305e1c4a797](../../evidence/conditions-sets-094.md#c-f4351305e1c4a797) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-003050

```text
(config-router-scope-af-topo)# neighbor next-hop-unchanged <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 43 `；EOL ` RVA 0x3450D538 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1b0c1fcf5f3d086e](../../evidence/conditions-sets-011.md#c-1b0c1fcf5f3d086e) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-003078

```text
(config-router-scope-af-topo)# neighbor orf rt-import-list <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 70 `；EOL ` RVA 0x34506E60 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ab835ca27d439164](../../evidence/conditions-sets-066.md#c-ab835ca27d439164) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-6317e372b48e554b](../../evidence/state_effects-sets-021.md#s-6317e372b48e554b)

### observed_connections-003037

```text
(config-router-scope-af-topo)# neighbor override-capability-neg <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 62 `；EOL ` RVA 0x345060B8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1e3df669ab0e3cf9](../../evidence/conditions-sets-012.md#c-1e3df669ab0e3cf9) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-003060

```text
(config-router-scope-af-topo)# neighbor password <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 7 `；EOL ` RVA 0x345122E0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b85fedd316c09ae8](../../evidence/conditions-sets-071.md#c-b85fedd316c09ae8) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-003120

```text
(config-router-scope-af-topo)# neighbor path-attribute treat-as-withdraw <number:1..255> in <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 27 `；EOL ` RVA 0x34515B80 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` path attribute type。

[条件 C-f6dcf8eb5c721af0](../../evidence/conditions-sets-095.md#c-f6dcf8eb5c721af0) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [参数 P-72a458c8c3022acf](../../evidence/parameters-sets-009.md#p-72a458c8c3022acf) · [状态效果 S-4ac3f2ec2d52db64](../../evidence/state_effects-sets-016.md#s-4ac3f2ec2d52db64)

### observed_connections-003034

```text
(config-router-scope-af-topo)# neighbor peer-group <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 10 `；EOL ` RVA 0x344E0C38 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8e4c55852a704b71](../../evidence/conditions-sets-055.md#c-8e4c55852a704b71) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-003087

```text
(config-router-scope-af-topo)# neighbor peer-group <string> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 20 `；EOL ` RVA 0x34511F48 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` peer-group name。

[条件 C-6e258b24e0760038](../../evidence/conditions-sets-043.md#c-6e258b24e0760038) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [参数 P-52dda26f99b7df22](../../evidence/parameters-sets-007.md#p-52dda26f99b7df22) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-003079

```text
(config-router-scope-af-topo)# neighbor prefix-length-size <number:1..2> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 68 `；EOL ` RVA 0x34507A60 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Storage size in bytes。

[条件 C-cdd2e851f00d0e15](../../evidence/conditions-sets-079.md#c-cdd2e851f00d0e15) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [参数 P-a6116061aef9ac47](../../evidence/parameters-sets-013.md#p-a6116061aef9ac47) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-003105

```text
(config-router-scope-af-topo)# neighbor prefix-list <string> in <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 58 `；EOL ` RVA 0x34506988 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Name of a prefix list。

[条件 C-35994091da99805d](../../evidence/conditions-sets-021.md#c-35994091da99805d) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [参数 P-d19b4dab0d5c54fd](../../evidence/parameters-sets-016.md#p-d19b4dab0d5c54fd) · [状态效果 S-5405f3edeff72c73](../../evidence/state_effects-sets-018.md#s-5405f3edeff72c73)

### observed_connections-003040

```text
(config-router-scope-af-topo)# neighbor remote-as <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 3 `；EOL ` RVA 0x34508488 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-160911c41469c892](../../evidence/conditions-sets-009.md#c-160911c41469c892) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-003053

```text
(config-router-scope-af-topo)# neighbor remove-private-as <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 55 `；EOL ` RVA 0x3450EA48 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3c15e60adcaa6f3e](../../evidence/conditions-sets-023.md#c-3c15e60adcaa6f3e) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-003086

```text
(config-router-scope-af-topo)# neighbor remove-private-as all <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 56 `；EOL ` RVA 0x3450EAB0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8060cd7582c05ee1](../../evidence/conditions-sets-050.md#c-8060cd7582c05ee1) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-003111

```text
(config-router-scope-af-topo)# neighbor remove-private-as all replace-as <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 57 `；EOL ` RVA 0x3450EA88 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8060cd7582c05ee1](../../evidence/conditions-sets-050.md#c-8060cd7582c05ee1) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-003106

```text
(config-router-scope-af-topo)# neighbor route-map <string> in <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 47 `；EOL ` RVA 0x34507670 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Name of route map。

[条件 C-fc219d4e34260c06](../../evidence/conditions-sets-097.md#c-fc219d4e34260c06) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [参数 P-56a31330bb3dc696](../../evidence/parameters-sets-007.md#p-56a31330bb3dc696) · [状态效果 S-53f0ef09cb1c2df4](../../evidence/state_effects-sets-018.md#s-53f0ef09cb1c2df4)

### observed_connections-003055

```text
(config-router-scope-af-topo)# neighbor route-reflector-client <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 49 `；EOL ` RVA 0x3450FF98 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-283381432d5aa003](../../evidence/conditions-sets-016.md#c-283381432d5aa003) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-003046

```text
(config-router-scope-af-topo)# neighbor send-community <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 46 `；EOL ` RVA 0x3450B9A8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c4aa87ec4762d0be](../../evidence/conditions-sets-076.md#c-c4aa87ec4762d0be) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-003066

```text
(config-router-scope-af-topo)# neighbor send-label <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 64 `；EOL ` RVA 0x34514B80 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b6f81c4e0bd5f8f5](../../evidence/conditions-sets-071.md#c-b6f81c4e0bd5f8f5) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-003048

```text
(config-router-scope-af-topo)# neighbor shutdown <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 5 `；EOL ` RVA 0x3450BE48 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ba483e96460a8055](../../evidence/conditions-sets-072.md#c-ba483e96460a8055) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-003081

```text
(config-router-scope-af-topo)# neighbor slow-peer detection <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 74 `；EOL ` RVA 0x3450CEF8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8f419973a82cf608](../../evidence/conditions-sets-055.md#c-8f419973a82cf608) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-003082

```text
(config-router-scope-af-topo)# neighbor slow-peer detection threshold <number:120..3600> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 74 `；EOL ` RVA 0x3450CF20 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Threshold value (seconds)。

[条件 C-839813b7d3861e3a](../../evidence/conditions-sets-051.md#c-839813b7d3861e3a) · [缺口 G-d75e16e85957f327](../../evidence/gaps-sets-007.md#g-d75e16e85957f327) · [参数 P-d3f734109cb70ab9](../../evidence/parameters-sets-016.md#p-d3f734109cb70ab9) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-003110

```text
(config-router-scope-af-topo)# neighbor slow-peer split-update-group dynamic <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 75 `；EOL ` RVA 0x3450CB80 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-df6254f59b5e0e20](../../evidence/conditions-sets-086.md#c-df6254f59b5e0e20) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-003109

```text
(config-router-scope-af-topo)# neighbor slow-peer split-update-group static <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 73 `；EOL ` RVA 0x3450C870 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4c959e4f28cdc8d7](../../evidence/conditions-sets-030.md#c-4c959e4f28cdc8d7) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-003083

```text
(config-router-scope-af-topo)# neighbor soft-reconfiguration inbound <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 54 `；EOL ` RVA 0x3450E068 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-86b9f1025a6fe26b](../../evidence/conditions-sets-052.md#c-86b9f1025a6fe26b) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-003125

```text
(config-router-scope-af-topo)# neighbor soo <?bgp_extcomm_action@555589a5e320> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 69 `；EOL ` RVA 0x3450A368 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5b99992805d4b839](../../evidence/conditions-sets-036.md#c-5b99992805d4b839) · [缺口 G-0e8803a0f852e018](../../evidence/gaps-sets-001.md#g-0e8803a0f852e018) · [状态效果 S-363077405b04bf7a](../../evidence/state_effects-sets-012.md#s-363077405b04bf7a)

### observed_connections-003096

```text
(config-router-scope-af-topo)# neighbor suppress-signaling-protocol ldp <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 81 `；EOL ` RVA 0x34517C70 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-325133a1bc3a6989](../../evidence/conditions-sets-020.md#c-325133a1bc3a6989) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-003068

```text
(config-router-scope-af-topo)# neighbor suppress-sr <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 87 `；EOL ` RVA 0x34517018 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-05db0ec610947357](../../evidence/conditions-sets-003.md#c-05db0ec610947357) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-003063

```text
(config-router-scope-af-topo)# neighbor timers <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 9 `；EOL ` RVA 0x345132B8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1db3879e1ea8e79e](../../evidence/conditions-sets-012.md#c-1db3879e1ea8e79e) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-003075

```text
(config-router-scope-af-topo)# neighbor translate-topology <number:1..4095> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 67 `；EOL ` RVA 0x34504A50 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Topology id。

[条件 C-36e4d1058431fe3e](../../evidence/conditions-sets-021.md#c-36e4d1058431fe3e) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [参数 P-29a580b5da5dc57a](../../evidence/parameters-sets-004.md#p-29a580b5da5dc57a) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-003038

```text
(config-router-scope-af-topo)# neighbor translate-update <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 66 `；EOL ` RVA 0x34505A50 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c41cc4f8d386df01](../../evidence/conditions-sets-076.md#c-c41cc4f8d386df01) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-0fe63544651cb37c](../../evidence/state_effects-sets-004.md#s-0fe63544651cb37c)

### observed_connections-003093

```text
(config-router-scope-af-topo)# neighbor transport multi-session <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 25 `；EOL ` RVA 0x345155F8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5106ca4ee508f037](../../evidence/conditions-sets-032.md#c-5106ca4ee508f037) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-2a6f12fd310e73f0](../../evidence/state_effects-sets-010.md#s-2a6f12fd310e73f0)

### observed_connections-003092

```text
(config-router-scope-af-topo)# neighbor transport path-mtu-discovery <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 24 `；EOL ` RVA 0x34515250 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5106ca4ee508f037](../../evidence/conditions-sets-032.md#c-5106ca4ee508f037) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-6a83e9fd912e972f](../../evidence/state_effects-sets-023.md#s-6a83e9fd912e972f)

### observed_connections-003115

```text
(config-router-scope-af-topo)# neighbor ttl-security hops <number:1..254> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 21 `；EOL ` RVA 0x34515F88 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` maximum number of hops。

[条件 C-07c9f5416d843d09](../../evidence/conditions-sets-003.md#c-07c9f5416d843d09) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [参数 P-8cc2c830fd88076d](../../evidence/parameters-sets-011.md#p-8cc2c830fd88076d) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-003080

```text
(config-router-scope-af-topo)# neighbor unsuppress-map <string> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 53 `；EOL ` RVA 0x34508128 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Name of route map。

[条件 C-8e141e8fa6af9f28](../../evidence/conditions-sets-055.md#c-8e141e8fa6af9f28) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [参数 P-223c6e11c8568fdf](../../evidence/parameters-sets-003.md#p-223c6e11c8568fdf) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-003121

```text
(config-router-scope-af-topo)# neighbor update in labeled-unicast unique <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 33 `；EOL ` RVA 0x345183D0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4d8b718999425ead](../../evidence/conditions-sets-030.md#c-4d8b718999425ead) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-7cd551f1b064b514](../../evidence/state_effects-sets-026.md#s-7cd551f1b064b514)

### observed_connections-003126

```text
(config-router-scope-af-topo)# neighbor update-source <interface> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 4 `；EOL ` RVA 0x3450B630 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9125e9a3c7bdde78](../../evidence/conditions-sets-056.md#c-9125e9a3c7bdde78) · [缺口 G-8daaf47d527eeec2](../../evidence/gaps-sets-005.md#g-8daaf47d527eeec2) · [参数 P-61fcc75034c55454](../../evidence/parameters-sets-008.md#p-61fcc75034c55454) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-003091

```text
(config-router-scope-af-topo)# neighbor use nexthop-attribute <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 37 `；EOL ` RVA 0x34513B40 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3be006df4c76bad6](../../evidence/conditions-sets-023.md#c-3be006df4c76bad6) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-003084

```text
(config-router-scope-af-topo)# neighbor validation off <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 83 `；EOL ` RVA 0x3450E3E8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-943c3e0115be4042](../../evidence/conditions-sets-057.md#c-943c3e0115be4042) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-003085

```text
(config-router-scope-af-topo)# neighbor validation redirect-off <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 84 `；EOL ` RVA 0x3450E690 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-943c3e0115be4042](../../evidence/conditions-sets-057.md#c-943c3e0115be4042) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-003023

```text
(config-router-scope-af-topo)# neighbor version <number:4..4> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 2 `；EOL ` RVA 0x3450AA40 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Neighbor's BGP version。

[条件 C-ddbd536532a30941](../../evidence/conditions-sets-085.md#c-ddbd536532a30941) · [缺口 G-42095c11b6c3a7a5](../../evidence/gaps-sets-003.md#g-42095c11b6c3a7a5) · [参数 P-db3efca0f5fa5dad](../../evidence/parameters-sets-017.md#p-db3efca0f5fa5dad) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-003045

```text
(config-router-scope-af-topo)# neighbor weight <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 41 `；EOL ` RVA 0x3450AE38 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-033cebca76205d75](../../evidence/conditions-sets-002.md#c-033cebca76205d75) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-003031

```text
(config-router-scope-af-topo)# network <address> <cr>
```

Handler ` RVA 0xF190B70 `；selector ` 0 `；EOL ` RVA 0x345D05B8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` NSAP prefix。

[条件 C-212bd37edb8d1bec](../../evidence/conditions-sets-013.md#c-212bd37edb8d1bec) · [缺口 G-ce3c01abfd61960f](../../evidence/gaps-sets-007.md#g-ce3c01abfd61960f) · [参数 P-0d76d20ee8872bc0](../../evidence/parameters-sets-001.md#p-0d76d20ee8872bc0) · [状态效果 S-ddcbbe923096d3c4](../../evidence/state_effects-sets-047.md#s-ddcbbe923096d3c4)

### observed_connections-003124

```text
(config-router-scope-af-topo)# network <address> <cr>
```

Handler ` RVA 0xE1E04C0 `；selector ` 0 `；EOL ` RVA 0x344F3258 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Network number。

[条件 C-1fa7aa820c5ad426](../../evidence/conditions-sets-012.md#c-1fa7aa820c5ad426) · [缺口 G-05cb3d1521972458](../../evidence/gaps-sets-001.md#g-05cb3d1521972458) · [参数 P-bc5dfd89d0bbefc6](../../evidence/parameters-sets-014.md#p-bc5dfd89d0bbefc6) · [状态效果 S-cf0dcd14c69eda70](../../evidence/state_effects-sets-044.md#s-cf0dcd14c69eda70)

### observed_connections-002914

```text
(config-router-scope-af-topo)# no aggregate-address <address> <address> <cr>
```

Handler ` RVA 0xF1B7BE0 `；selector ` 0 `；EOL ` RVA 0x345D0F60 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` Aggregate address；` address ` Aggregate mask。

[条件 C-23d5f57ce591a637](../../evidence/conditions-sets-014.md#c-23d5f57ce591a637) · [参数 P-76b5f9e92a505038](../../evidence/parameters-sets-009.md#p-76b5f9e92a505038) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002721

```text
(config-router-scope-af-topo)# no auto-summary <cr>
```

Handler ` RVA 0xE1FA6B0 `；selector ` 0 `；EOL ` RVA 0x344F7B28 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-892cb3702bd56b94](../../evidence/conditions-sets-053.md#c-892cb3702bd56b94) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002901

```text
(config-router-scope-af-topo)# no bgp additional-paths install <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 69 `；EOL ` RVA 0x345C87B8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-60d75d37bc053107](../../evidence/conditions-sets-038.md#c-60d75d37bc053107) · [状态效果 S-d16145b438038708](../../evidence/state_effects-sets-044.md#s-d16145b438038708)

### observed_connections-002910

```text
(config-router-scope-af-topo)# no bgp additional-paths select <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 71 `；EOL ` RVA 0x345C8460 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b007819fa3ccbb28](../../evidence/conditions-sets-068.md#c-b007819fa3ccbb28) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002779

```text
(config-router-scope-af-topo)# no bgp advertise-best-external <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 70 `；EOL ` RVA 0x345C9608 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-bb586878f7114cd8](../../evidence/conditions-sets-072.md#c-bb586878f7114cd8) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002832

```text
(config-router-scope-af-topo)# no bgp advertisement startup-delay <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 95 `；EOL ` RVA 0x345C1478 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-080ae7a4274fcc15](../../evidence/conditions-sets-003.md#c-080ae7a4274fcc15) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002911

```text
(config-router-scope-af-topo)# no bgp aggregate-timer <number:6..60> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 58 `；EOL ` RVA 0x345CF658 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Timer interval。

[条件 C-fc28056caeba15bb](../../evidence/conditions-sets-097.md#c-fc28056caeba15bb) · [参数 P-1d77f5e43add4cdb](../../evidence/parameters-sets-003.md#p-1d77f5e43add4cdb) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002862

```text
(config-router-scope-af-topo)# no bgp aigp-rib-metric <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 91 `；EOL ` RVA 0x345C5EF8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a6d86b91e3f7b225](../../evidence/conditions-sets-064.md#c-a6d86b91e3f7b225) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002767

```text
(config-router-scope-af-topo)# no bgp always-compare-med <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 5 `；EOL ` RVA 0x345BCD60 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ab4874c439cf7460](../../evidence/conditions-sets-066.md#c-ab4874c439cf7460) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002889

```text
(config-router-scope-af-topo)# no bgp asnotation dot <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 64 `；EOL ` RVA 0x345BD070 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ab4874c439cf7460](../../evidence/conditions-sets-066.md#c-ab4874c439cf7460) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002998

```text
(config-router-scope-af-topo)# no bgp bestpath aigp ignore <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 43 `；EOL ` RVA 0x345C4C20 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-044dcc0f1cbb62eb](../../evidence/conditions-sets-002.md#c-044dcc0f1cbb62eb) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002991

```text
(config-router-scope-af-topo)# no bgp bestpath as-path ignore <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 17 `；EOL ` RVA 0x345C4390 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a6d86b91e3f7b225](../../evidence/conditions-sets-064.md#c-a6d86b91e3f7b225) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002993

```text
(config-router-scope-af-topo)# no bgp bestpath as-path multipath-relax <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 51 `；EOL ` RVA 0x345C4638 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a6d86b91e3f7b225](../../evidence/conditions-sets-064.md#c-a6d86b91e3f7b225) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002944

```text
(config-router-scope-af-topo)# no bgp bestpath compare-routerid <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 24 `；EOL ` RVA 0x345C48D0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a6d86b91e3f7b225](../../evidence/conditions-sets-064.md#c-a6d86b91e3f7b225) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002997

```text
(config-router-scope-af-topo)# no bgp bestpath cost-community ignore <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 41 `；EOL ` RVA 0x345C4EF8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a6d86b91e3f7b225](../../evidence/conditions-sets-064.md#c-a6d86b91e3f7b225) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002956

```text
(config-router-scope-af-topo)# no bgp bestpath igp-metric ignore <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 42 `；EOL ` RVA 0x345C8CE8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad20aa2ce79c5c50](../../evidence/conditions-sets-067.md#c-ad20aa2ce79c5c50) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002994

```text
(config-router-scope-af-topo)# no bgp bestpath med missing-as-worst <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 18 `；EOL ` RVA 0x345C4080 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a6d86b91e3f7b225](../../evidence/conditions-sets-064.md#c-a6d86b91e3f7b225) · [状态效果 S-f6a7b763679c3c7c](../../evidence/state_effects-sets-052.md#s-f6a7b763679c3c7c)

### observed_connections-002962

```text
(config-router-scope-af-topo)# no bgp bestpath prefix-validate allow-invalid <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 78 `；EOL ` RVA 0x345C8FF8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-31956af50c4a9141](../../evidence/conditions-sets-019.md#c-31956af50c4a9141) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002964

```text
(config-router-scope-af-topo)# no bgp bestpath prefix-validate disable <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 77 `；EOL ` RVA 0x345C92A0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-31956af50c4a9141](../../evidence/conditions-sets-019.md#c-31956af50c4a9141) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002906

```text
(config-router-scope-af-topo)# no bgp client-to-client reflection <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 9 `；EOL ` RVA 0x345BDF00 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d84da79c9374e309](../../evidence/conditions-sets-083.md#c-d84da79c9374e309) · [状态效果 S-c633f3708e803868](../../evidence/state_effects-sets-042.md#s-c633f3708e803868)

### observed_connections-002792

```text
(config-router-scope-af-topo)# no bgp cluster-id <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 7 `；EOL ` RVA 0x345BDAC8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d536ef29746823d9](../../evidence/conditions-sets-082.md#c-d536ef29746823d9) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002802

```text
(config-router-scope-af-topo)# no bgp consistency-checker <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 3 `；EOL ` RVA 0x345BD448 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0a3136f5c57f0840](../../evidence/conditions-sets-004.md#c-0a3136f5c57f0840) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002768

```text
(config-router-scope-af-topo)# no bgp dampening <cr>
```

Handler ` RVA 0xF1B85B0 `；selector ` 0 `；EOL ` RVA 0x345C7880 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8ddd4b70082ec42f](../../evidence/conditions-sets-055.md#c-8ddd4b70082ec42f) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002957

```text
(config-router-scope-af-topo)# no bgp default inter-as-hybrid advertise-source-routes <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 57 `；EOL ` RVA 0x345C6EB8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c0f22f5509b0574d](../../evidence/conditions-sets-074.md#c-c0f22f5509b0574d) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002880

```text
(config-router-scope-af-topo)# no bgp default ipv4-unicast <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 19 `；EOL ` RVA 0x345C6610 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-21977b251acb837f](../../evidence/conditions-sets-013.md#c-21977b251acb837f) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002883

```text
(config-router-scope-af-topo)# no bgp default ipv6-nexthop <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 75 `；EOL ` RVA 0x345C6908 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-745de96593c1eadf](../../evidence/conditions-sets-045.md#c-745de96593c1eadf) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002770

```text
(config-router-scope-af-topo)# no bgp default local-preference <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 0 `；EOL ` RVA 0x345C6B98 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-bce9a25435a542ed](../../evidence/conditions-sets-073.md#c-bce9a25435a542ed) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002951

```text
(config-router-scope-af-topo)# no bgp default route-target filter <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 25 `；EOL ` RVA 0x345C7220 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a1d6f7b25430895a](../../evidence/conditions-sets-062.md#c-a1d6f7b25430895a) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002952

```text
(config-router-scope-af-topo)# no bgp default route-target filter <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 25 `；EOL ` RVA 0x345C74C0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8b8d63d3237cfa03](../../evidence/conditions-sets-054.md#c-8b8d63d3237cfa03) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002819

```text
(config-router-scope-af-topo)# no bgp deterministic-med <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 10 `；EOL ` RVA 0x345BF580 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ab4874c439cf7460](../../evidence/conditions-sets-066.md#c-ab4874c439cf7460) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002790

```text
(config-router-scope-af-topo)# no bgp dmzlink-bw <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 31 `；EOL ` RVA 0x345CABB8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-3adab7f53eab96ed](../../evidence/conditions-sets-023.md#c-3adab7f53eab96ed) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002720

```text
(config-router-scope-af-topo)# no bgp dynamic-med-interval <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 21 `；EOL ` RVA 0x345BF5A8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c50e2821402bb9e3](../../evidence/conditions-sets-076.md#c-c50e2821402bb9e3) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002797

```text
(config-router-scope-af-topo)# no bgp enforce-first-as <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 20 `；EOL ` RVA 0x345BE7B0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ab4874c439cf7460](../../evidence/conditions-sets-066.md#c-ab4874c439cf7460) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002835

```text
(config-router-scope-af-topo)# no bgp enhanced-error <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 82 `；EOL ` RVA 0x345C11F0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d404c15dadfba5f1](../../evidence/conditions-sets-082.md#c-d404c15dadfba5f1) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002755

```text
(config-router-scope-af-topo)# no bgp fast-external-fallover <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 1 `；EOL ` RVA 0x345BC498 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ab4874c439cf7460](../../evidence/conditions-sets-066.md#c-ab4874c439cf7460) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002850

```text
(config-router-scope-af-topo)# no bgp graceful-restart <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 35 `；EOL ` RVA 0x345C2060 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ab4874c439cf7460](../../evidence/conditions-sets-066.md#c-ab4874c439cf7460) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002842

```text
(config-router-scope-af-topo)# no bgp graceful-restart restart-time <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 36 `；EOL ` RVA 0x345C1A30 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c82877477f708348](../../evidence/conditions-sets-077.md#c-c82877477f708348) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002846

```text
(config-router-scope-af-topo)# no bgp graceful-restart stalepath-time <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 37 `；EOL ` RVA 0x345C1A98 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7031783c88894352](../../evidence/conditions-sets-043.md#c-7031783c88894352) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-003015

```text
(config-router-scope-af-topo)# no bgp graceful-shutdown all vrfs activate <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 79 `；EOL ` RVA 0x345C24C8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-9b1924e01b9a6adb](../../evidence/conditions-sets-060.md#c-9b1924e01b9a6adb) · [状态效果 S-4009f3c09fc9fb43](../../evidence/state_effects-sets-014.md#s-4009f3c09fc9fb43)

### observed_connections-003013

```text
(config-router-scope-af-topo)# no bgp inject-map <string> exist-map <string> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 32 `；EOL ` RVA 0x345CC730 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` route-map name；` string ` route-map name。

[条件 C-fedb6cae967c9a50](../../evidence/conditions-sets-098.md#c-fedb6cae967c9a50) · [参数 P-c031eb060e8bf349](../../evidence/parameters-sets-015.md#p-c031eb060e8bf349) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002950

```text
(config-router-scope-af-topo)# no bgp label-allocation-batch <number:0..4294967295> <number:0..4294967295> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 53 `；EOL ` RVA 0x345BC828 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Timer value in milliseconds；` unsigned_number ` Batch Size。

[条件 C-ab4874c439cf7460](../../evidence/conditions-sets-066.md#c-ab4874c439cf7460) · [参数 P-25b90a94faeaa469](../../evidence/parameters-sets-003.md#p-25b90a94faeaa469) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002974

```text
(config-router-scope-af-topo)# no bgp listen block <address> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 93 `；EOL ` RVA 0x345CA5C8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` IPv4 Dynamic Peering Address。

[条件 C-68b3d1afb9f1515e](../../evidence/conditions-sets-041.md#c-68b3d1afb9f1515e) · [参数 P-4423f7a79b076b21](../../evidence/parameters-sets-006.md#p-4423f7a79b076b21) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002987

```text
(config-router-scope-af-topo)# no bgp listen block <address> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 93 `；EOL ` RVA 0x345C0528 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` IPv4 Dynamic Peering Address。

[条件 C-4383b9d78c985b8e](../../evidence/conditions-sets-026.md#c-4383b9d78c985b8e) · [参数 P-11231d0c3b66f126](../../evidence/parameters-sets-002.md#p-11231d0c3b66f126) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002808

```text
(config-router-scope-af-topo)# no bgp listen limit <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 61 `；EOL ` RVA 0x345CA510 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0965838a33a65b88](../../evidence/conditions-sets-004.md#c-0965838a33a65b88) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002837

```text
(config-router-scope-af-topo)# no bgp listen limit <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 61 `；EOL ` RVA 0x345C0448 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1a8aa0eeb10fb66b](../../evidence/conditions-sets-010.md#c-1a8aa0eeb10fb66b) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002928

```text
(config-router-scope-af-topo)# no bgp listen persistent <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 94 `；EOL ` RVA 0x345C0860 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4383b9d78c985b8e](../../evidence/conditions-sets-026.md#c-4383b9d78c985b8e) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002805

```text
(config-router-scope-af-topo)# no bgp log-neighbor-changes <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 11 `；EOL ` RVA 0x345BEA58 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ab4874c439cf7460](../../evidence/conditions-sets-066.md#c-ab4874c439cf7460) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002868

```text
(config-router-scope-af-topo)# no bgp maxas-limit <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 26 `；EOL ` RVA 0x345C5C70 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-115abedd43b102bc](../../evidence/conditions-sets-007.md#c-115abedd43b102bc) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002857

```text
(config-router-scope-af-topo)# no bgp maxcommunity-limit <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 27 `；EOL ` RVA 0x345C5280 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8a31efed133b247f](../../evidence/conditions-sets-053.md#c-8a31efed133b247f) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002864

```text
(config-router-scope-af-topo)# no bgp maxextcommunity-limit <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 29 `；EOL ` RVA 0x345C5920 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1e69d6c751a17001](../../evidence/conditions-sets-012.md#c-1e69d6c751a17001) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002860

```text
(config-router-scope-af-topo)# no bgp maxlargecommunity-limit <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 28 `；EOL ` RVA 0x345C55D0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-216d87b077dc8bef](../../evidence/conditions-sets-013.md#c-216d87b077dc8bef) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002830

```text
(config-router-scope-af-topo)# no bgp mpls-local-label <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 81 `；EOL ` RVA 0x345CCAA8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-31488a0baa289d4d](../../evidence/conditions-sets-019.md#c-31488a0baa289d4d) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002979

```text
(config-router-scope-af-topo)# no bgp nexthop route-map <string> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 56 `；EOL ` RVA 0x345CB320 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` route-map name。

[条件 C-7820ec64c4324b06](../../evidence/conditions-sets-047.md#c-7820ec64c4324b06) · [参数 P-6f819417a906606a](../../evidence/parameters-sets-009.md#p-6f819417a906606a) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002922

```text
(config-router-scope-af-topo)# no bgp nexthop trigger critical-delay <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 48 `；EOL ` RVA 0x345CB888 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-50ad60349bfbef12](../../evidence/conditions-sets-031.md#c-50ad60349bfbef12) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002917

```text
(config-router-scope-af-topo)# no bgp nexthop trigger delay <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 47 `；EOL ` RVA 0x345CB608 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-20b49d9bc5181fec](../../evidence/conditions-sets-013.md#c-20b49d9bc5181fec) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002973

```text
(config-router-scope-af-topo)# no bgp nexthop trigger enable <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 49 `；EOL ` RVA 0x345CB5E0 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8afb2da867e5f253](../../evidence/conditions-sets-054.md#c-8afb2da867e5f253) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002984

```text
(config-router-scope-af-topo)# no bgp nopeerup-delay cold-boot <number:1..3600> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 74 `；EOL ` RVA 0x345C0E88 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Delay in seconds。

[条件 C-d307f5eb044f3a7c](../../evidence/conditions-sets-081.md#c-d307f5eb044f3a7c) · [参数 P-ca7b15937712ec27](../../evidence/parameters-sets-015.md#p-ca7b15937712ec27) · [状态效果 S-1bf1854e189da328](../../evidence/state_effects-sets-006.md#s-1bf1854e189da328)

### observed_connections-002895

```text
(config-router-scope-af-topo)# no bgp recursion host <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 72 `；EOL ` RVA 0x345C9980 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-019c433b5d1f87b0](../../evidence/conditions-sets-001.md#c-019c433b5d1f87b0) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002780

```text
(config-router-scope-af-topo)# no bgp redistribute-internal <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 2 `；EOL ` RVA 0x345CDCA8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-2ffde756bdc3d691](../../evidence/conditions-sets-019.md#c-2ffde756bdc3d691) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002938

```text
(config-router-scope-af-topo)# no bgp refresh max-eor-time <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 16 `；EOL ` RVA 0x345C3258 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-67748b0e0d53580a](../../evidence/conditions-sets-040.md#c-67748b0e0d53580a) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002933

```text
(config-router-scope-af-topo)# no bgp refresh stalepath-time <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 15 `；EOL ` RVA 0x345C2EE8 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-6eb6839298b1e4b3](../../evidence/conditions-sets-043.md#c-6eb6839298b1e4b3) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

### observed_connections-002934

```text
(config-router-scope-af-topo)# no bgp regexp deterministic <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 44 `；EOL ` RVA 0x345C3C70 `。

模式根 ` RVA 0x345B8E50 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a6d86b91e3f7b225](../../evidence/conditions-sets-064.md#c-a6d86b91e3f7b225) · [状态效果 S-50a5db3b6b42ce92](../../evidence/state_effects-sets-018.md#s-50a5db3b6b42ce92)

