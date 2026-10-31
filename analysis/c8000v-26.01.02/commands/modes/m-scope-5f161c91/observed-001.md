# scope · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-003562

```text
(config-router-scope)# address-family <?option@555589a8f1c0> <cr>
```

Handler ` RVA 0xF12CFC0 `；selector ` 0 `；EOL ` RVA 0x3453B408 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-dedd52ceb858f9c8](../../evidence/conditions-sets-086.md#c-dedd52ceb858f9c8) · [缺口 G-31040d14abdc45a2](../../evidence/gaps-sets-002.md#g-31040d14abdc45a2) · [状态效果 S-b7c7cb110162f079](../../evidence/state_effects-sets-039.md#s-b7c7cb110162f079)

### observed_connections-003277

```text
(config-router-scope)# aggregate-address <address> <address> <cr>
```

Handler ` RVA 0xF1B7BE0 `；selector ` 0 `；EOL ` RVA 0x3457A030 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Aggregate address；` address ` Aggregate mask。

[条件 C-4eb836e3175cf5bd](../../evidence/conditions-sets-031.md#c-4eb836e3175cf5bd) · [参数 P-034bf7990709c321](../../evidence/parameters-sets-001.md#p-034bf7990709c321)

### observed_connections-003141

```text
(config-router-scope)# auto-summary <cr>
```

Handler ` RVA 0xE1FA6B0 `；selector ` 0 `；EOL ` RVA 0x34563B88 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fe8af09d9c1d13be](../../evidence/conditions-sets-098.md#c-fe8af09d9c1d13be)

### observed_connections-003246

```text
(config-router-scope)# bgp additional-paths install <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 69 `；EOL ` RVA 0x34571888 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c626df2c5a490a40](../../evidence/conditions-sets-076.md#c-c626df2c5a490a40) · [状态效果 S-8638e4d479ffeaef](../../evidence/state_effects-sets-028.md#s-8638e4d479ffeaef)

### observed_connections-003267

```text
(config-router-scope)# bgp additional-paths select <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 71 `；EOL ` RVA 0x34571530 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5f537ef68ce3cb25](../../evidence/conditions-sets-037.md#c-5f537ef68ce3cb25)

### observed_connections-003167

```text
(config-router-scope)# bgp advertise-best-external <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 70 `；EOL ` RVA 0x345726D8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5ee23059aaf8eb3a](../../evidence/conditions-sets-037.md#c-5ee23059aaf8eb3a)

### observed_connections-003190

```text
(config-router-scope)# bgp advertisement startup-delay <number:1..3600> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 95 `；EOL ` RVA 0x3456A548 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` value (seconds)。

[条件 C-4a4bee7d09aced86](../../evidence/conditions-sets-029.md#c-4a4bee7d09aced86) · [参数 P-2c80c6aa31391b93](../../evidence/parameters-sets-004.md#p-2c80c6aa31391b93)

### observed_connections-003268

```text
(config-router-scope)# bgp aggregate-timer <number:6..60> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 58 `；EOL ` RVA 0x34578728 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timer interval。

[条件 C-9828edb5d90b4a4a](../../evidence/conditions-sets-059.md#c-9828edb5d90b4a4a) · [参数 P-b1318a7e59a386fd](../../evidence/parameters-sets-013.md#p-b1318a7e59a386fd)

### observed_connections-003198

```text
(config-router-scope)# bgp aigp-rib-metric <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 91 `；EOL ` RVA 0x3456EFC8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e398f2ee0aabd351](../../evidence/conditions-sets-088.md#c-e398f2ee0aabd351)

### observed_connections-003165

```text
(config-router-scope)# bgp always-compare-med <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 5 `；EOL ` RVA 0x34565E30 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f2d18c8b4e477c8c](../../evidence/conditions-sets-094.md#c-f2d18c8b4e477c8c)

### observed_connections-003232

```text
(config-router-scope)# bgp asnotation dot <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 64 `；EOL ` RVA 0x34566140 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f2d18c8b4e477c8c](../../evidence/conditions-sets-094.md#c-f2d18c8b4e477c8c)

### observed_connections-003396

```text
(config-router-scope)# bgp bestpath aigp ignore <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 43 `；EOL ` RVA 0x3456DCF0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-af1a55da7d13e1c4](../../evidence/conditions-sets-068.md#c-af1a55da7d13e1c4)

### observed_connections-003390

```text
(config-router-scope)# bgp bestpath as-path ignore <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 17 `；EOL ` RVA 0x3456D460 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e398f2ee0aabd351](../../evidence/conditions-sets-088.md#c-e398f2ee0aabd351)

### observed_connections-003392

```text
(config-router-scope)# bgp bestpath as-path multipath-relax <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 51 `；EOL ` RVA 0x3456D708 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e398f2ee0aabd351](../../evidence/conditions-sets-088.md#c-e398f2ee0aabd351)

### observed_connections-003307

```text
(config-router-scope)# bgp bestpath compare-routerid <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 24 `；EOL ` RVA 0x3456D9A0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e398f2ee0aabd351](../../evidence/conditions-sets-088.md#c-e398f2ee0aabd351)

### observed_connections-003395

```text
(config-router-scope)# bgp bestpath cost-community ignore <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 41 `；EOL ` RVA 0x3456DFC8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e398f2ee0aabd351](../../evidence/conditions-sets-088.md#c-e398f2ee0aabd351)

### observed_connections-003337

```text
(config-router-scope)# bgp bestpath igp-metric ignore <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 42 `；EOL ` RVA 0x34571DB8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-96e540aecb31c83c](../../evidence/conditions-sets-058.md#c-96e540aecb31c83c)

### observed_connections-003393

```text
(config-router-scope)# bgp bestpath med missing-as-worst <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 18 `；EOL ` RVA 0x3456D150 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e398f2ee0aabd351](../../evidence/conditions-sets-088.md#c-e398f2ee0aabd351) · [状态效果 S-fb614c9c25821671](../../evidence/state_effects-sets-053.md#s-fb614c9c25821671)

### observed_connections-003345

```text
(config-router-scope)# bgp bestpath prefix-validate allow-invalid <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 78 `；EOL ` RVA 0x345720C8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3a39bc8175d21cd0](../../evidence/conditions-sets-023.md#c-3a39bc8175d21cd0)

### observed_connections-003351

```text
(config-router-scope)# bgp bestpath prefix-validate disable <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 77 `；EOL ` RVA 0x34572370 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3a39bc8175d21cd0](../../evidence/conditions-sets-023.md#c-3a39bc8175d21cd0)

### observed_connections-003254

```text
(config-router-scope)# bgp client-to-client reflection <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 9 `；EOL ` RVA 0x34566FD0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7b5c81f0eb8f2c77](../../evidence/conditions-sets-048.md#c-7b5c81f0eb8f2c77) · [状态效果 S-1a0ebd06a4a3557b](../../evidence/state_effects-sets-006.md#s-1a0ebd06a4a3557b)

### observed_connections-003555

```text
(config-router-scope)# bgp client-to-client reflection intra-cluster cluster-id <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 9 `；EOL ` RVA 0x34566FD0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8ca3332fbea5af22](../../evidence/conditions-sets-054.md#c-8ca3332fbea5af22) · [缺口 G-4467be8c1af61ca3](../../evidence/gaps-sets-003.md#g-4467be8c1af61ca3) · [状态效果 S-dc7c2dd13a5c9886](../../evidence/state_effects-sets-047.md#s-dc7c2dd13a5c9886)

### observed_connections-003251

```text
(config-router-scope)# bgp cluster-id <number:1..4294967294> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 7 `；EOL ` RVA 0x34566B98 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Route-Reflector Cluster-id as 32 bit quantity。

[条件 C-9e43d53cb610822a](../../evidence/conditions-sets-061.md#c-9e43d53cb610822a) · [参数 P-c5326c25a6cf9088](../../evidence/parameters-sets-015.md#p-c5326c25a6cf9088)

### observed_connections-003540

```text
(config-router-scope)# bgp confederation identifier <?bgp_as4_action@555589abbea0> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 6 `；EOL ` RVA 0x34567ED8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f2d18c8b4e477c8c](../../evidence/conditions-sets-094.md#c-f2d18c8b4e477c8c) · [缺口 G-81b86f7e819b47ec](../../evidence/gaps-sets-005.md#g-81b86f7e819b47ec)

### observed_connections-003541

```text
(config-router-scope)# bgp confederation peers <?bgp_as4_action@555589abc210> <cr>
```

Handler ` RVA 0xF1C67F0 `；selector ` 0 `；EOL ` RVA 0x34568350 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ab65cc7c4818f811](../../evidence/conditions-sets-066.md#c-ab65cc7c4818f811) · [缺口 G-0d51560384deb566](../../evidence/gaps-sets-001.md#g-0d51560384deb566) · [状态效果 S-9b2c6285fd12882b](../../evidence/state_effects-sets-033.md#s-9b2c6285fd12882b)

### observed_connections-003271

```text
(config-router-scope)# bgp consistency-checker error-message <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 3 `；EOL ` RVA 0x34566518 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f0b9c61b409174e6](../../evidence/conditions-sets-093.md#c-f0b9c61b409174e6) · [状态效果 S-49b56fa894550fd2](../../evidence/state_effects-sets-016.md#s-49b56fa894550fd2)

### observed_connections-003258

```text
(config-router-scope)# bgp consistency-checker error-message interval <number:5..1440> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 3 `；EOL ` RVA 0x34566540 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Interval (minutes)。

[条件 C-49d1e9f55a8179ac](../../evidence/conditions-sets-029.md#c-49d1e9f55a8179ac) · [参数 P-e603e1198adc1ad1](../../evidence/parameters-sets-017.md#p-e603e1198adc1ad1) · [状态效果 S-49b56fa894550fd2](../../evidence/state_effects-sets-016.md#s-49b56fa894550fd2)

### observed_connections-003169

```text
(config-router-scope)# bgp dampening <cr>
```

Handler ` RVA 0xF1B85B0 `；selector ` 0 `；EOL ` RVA 0x34570950 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-92e2256ac2825e65](../../evidence/conditions-sets-057.md#c-92e2256ac2825e65)

### observed_connections-003341

```text
(config-router-scope)# bgp dampening route-map <string> <cr>
```

Handler ` RVA 0xF1B85B0 `；selector ` 8 `；EOL ` RVA 0x34570B18 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` route-map name。

[条件 C-d9c1392188a5b8fa](../../evidence/conditions-sets-084.md#c-d9c1392188a5b8fa) · [参数 P-a9c109d48f13e5cd](../../evidence/parameters-sets-013.md#p-a9c109d48f13e5cd)

### observed_connections-003338

```text
(config-router-scope)# bgp default inter-as-hybrid advertise-source-routes <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 57 `；EOL ` RVA 0x3456FF88 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6db1be956b0c537b](../../evidence/conditions-sets-042.md#c-6db1be956b0c537b)

### observed_connections-003216

```text
(config-router-scope)# bgp default ipv4-unicast <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 19 `；EOL ` RVA 0x3456F6E0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b70918c03dee8921](../../evidence/conditions-sets-071.md#c-b70918c03dee8921)

### observed_connections-003220

```text
(config-router-scope)# bgp default ipv6-nexthop <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 75 `；EOL ` RVA 0x3456F9D8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8c098b49402f3cfe](../../evidence/conditions-sets-054.md#c-8c098b49402f3cfe)

### observed_connections-003166

```text
(config-router-scope)# bgp default local-preference <number:0..4294967295> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 0 `；EOL ` RVA 0x3456FC68 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Configure default local preference value。

[条件 C-7c8363b353487d1f](../../evidence/conditions-sets-048.md#c-7c8363b353487d1f) · [参数 P-1123f041c5abdfdf](../../evidence/parameters-sets-002.md#p-1123f041c5abdfdf)

### observed_connections-003332

```text
(config-router-scope)# bgp default route-target filter <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 25 `；EOL ` RVA 0x345702F0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6e88b262d39af1db](../../evidence/conditions-sets-043.md#c-6e88b262d39af1db)

### observed_connections-003333

```text
(config-router-scope)# bgp default route-target filter <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 25 `；EOL ` RVA 0x34570590 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-dcc3a1ccdaf9a9a8](../../evidence/conditions-sets-085.md#c-dcc3a1ccdaf9a9a8)

### observed_connections-003182

```text
(config-router-scope)# bgp deterministic-med <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 10 `；EOL ` RVA 0x34568650 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f2d18c8b4e477c8c](../../evidence/conditions-sets-094.md#c-f2d18c8b4e477c8c)

### observed_connections-003171

```text
(config-router-scope)# bgp dmzlink-bw <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 31 `；EOL ` RVA 0x34573C88 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c52df1d2f09c863e](../../evidence/conditions-sets-076.md#c-c52df1d2f09c863e)

### observed_connections-003142

```text
(config-router-scope)# bgp dynamic-med-interval <number:60..4294967295> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 21 `；EOL ` RVA 0x34568678 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Interval value (seconds)。

[条件 C-7725ddfe7038d17c](../../evidence/conditions-sets-046.md#c-7725ddfe7038d17c) · [参数 P-e76077828deb6049](../../evidence/parameters-sets-017.md#p-e76077828deb6049)

### observed_connections-003172

```text
(config-router-scope)# bgp enforce-first-as <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 20 `；EOL ` RVA 0x34567880 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f2d18c8b4e477c8c](../../evidence/conditions-sets-094.md#c-f2d18c8b4e477c8c)

### observed_connections-003194

```text
(config-router-scope)# bgp enhanced-error <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 82 `；EOL ` RVA 0x3456A2C0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-90e7040a17fa63a5](../../evidence/conditions-sets-056.md#c-90e7040a17fa63a5)

### observed_connections-003158

```text
(config-router-scope)# bgp fast-external-fallover <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 1 `；EOL ` RVA 0x34565568 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f2d18c8b4e477c8c](../../evidence/conditions-sets-094.md#c-f2d18c8b4e477c8c)

### observed_connections-003197

```text
(config-router-scope)# bgp graceful-restart <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 35 `；EOL ` RVA 0x3456B130 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f2d18c8b4e477c8c](../../evidence/conditions-sets-094.md#c-f2d18c8b4e477c8c)

### observed_connections-003195

```text
(config-router-scope)# bgp graceful-restart restart-time <number:1..3600> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 36 `；EOL ` RVA 0x3456AB00 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Delay value (seconds)。

[条件 C-e59f34d3abba1990](../../evidence/conditions-sets-089.md#c-e59f34d3abba1990) · [参数 P-a5fa11592beab6fe](../../evidence/parameters-sets-013.md#p-a5fa11592beab6fe)

### observed_connections-003196

```text
(config-router-scope)# bgp graceful-restart stalepath-time <number:1..3600> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 37 `；EOL ` RVA 0x3456AB68 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Delay value (seconds)。

[条件 C-e5ba9709633fa710](../../evidence/conditions-sets-089.md#c-e5ba9709633fa710) · [参数 P-0689af1cac5660f1](../../evidence/parameters-sets-001.md#p-0689af1cac5660f1)

### observed_connections-003561

```text
(config-router-scope)# bgp graceful-shutdown all vrfs <number:30..65535> community <?bgp_community_action@555589abfa48> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 79 `；EOL ` RVA 0x3456B598 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` time in seconds。

[条件 C-9a8f5db650a2bdd3](../../evidence/conditions-sets-060.md#c-9a8f5db650a2bdd3) · [缺口 G-4a04e4d98234b1ef](../../evidence/gaps-sets-003.md#g-4a04e4d98234b1ef) · [参数 P-26017df74aa6445e](../../evidence/parameters-sets-003.md#p-26017df74aa6445e) · [状态效果 S-261e7c23b2d1ac10](../../evidence/state_effects-sets-009.md#s-261e7c23b2d1ac10)

### observed_connections-003436

```text
(config-router-scope)# bgp graceful-shutdown all vrfs activate <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 79 `；EOL ` RVA 0x3456B598 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f71ec471c4706ed6](../../evidence/conditions-sets-095.md#c-f71ec471c4706ed6) · [状态效果 S-dbe24f0276422381](../../evidence/state_effects-sets-047.md#s-dbe24f0276422381)

### observed_connections-003431

```text
(config-router-scope)# bgp inject-map <string> exist-map <string> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 32 `；EOL ` RVA 0x34575800 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` route-map name；` string ` route-map name。

[条件 C-ef65e2591e463555](../../evidence/conditions-sets-092.md#c-ef65e2591e463555) · [参数 P-15b069a9948617b7](../../evidence/parameters-sets-002.md#p-15b069a9948617b7)

### observed_connections-003330

```text
(config-router-scope)# bgp label-allocation-batch <number:0..4294967295> <number:0..4294967295> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 53 `；EOL ` RVA 0x345658F8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timer value in milliseconds；` unsigned_number ` Batch Size。

[条件 C-f2d18c8b4e477c8c](../../evidence/conditions-sets-094.md#c-f2d18c8b4e477c8c) · [参数 P-67d56dc38a8352d0](../../evidence/parameters-sets-008.md#p-67d56dc38a8352d0)

### observed_connections-003363

```text
(config-router-scope)# bgp listen block <address> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 93 `；EOL ` RVA 0x34573698 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IPv4 Dynamic Peering Address。

[条件 C-9bc5921baff5d9a8](../../evidence/conditions-sets-060.md#c-9bc5921baff5d9a8) · [参数 P-dd46f1481a83f05c](../../evidence/parameters-sets-017.md#p-dd46f1481a83f05c)

### observed_connections-003374

```text
(config-router-scope)# bgp listen block <address> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 93 `；EOL ` RVA 0x345695F8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IPv4 Dynamic Peering Address。

[条件 C-141f60943613848c](../../evidence/conditions-sets-008.md#c-141f60943613848c) · [参数 P-6ed5db196fb7f6a7](../../evidence/parameters-sets-009.md#p-6ed5db196fb7f6a7)

### observed_connections-003178

```text
(config-router-scope)# bgp listen limit <number:1..10000> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 61 `；EOL ` RVA 0x345735E0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` max number。

[条件 C-127407e168c991f7](../../evidence/conditions-sets-007.md#c-127407e168c991f7) · [参数 P-8df57cd552abc815](../../evidence/parameters-sets-011.md#p-8df57cd552abc815)

### observed_connections-003192

```text
(config-router-scope)# bgp listen limit <number:1..10000> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 61 `；EOL ` RVA 0x34569518 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` max number。

[条件 C-260f35521bb3ac99](../../evidence/conditions-sets-015.md#c-260f35521bb3ac99) · [参数 P-0edef6afcc169612](../../evidence/parameters-sets-002.md#p-0edef6afcc169612)

### observed_connections-003299

```text
(config-router-scope)# bgp listen persistent <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 94 `；EOL ` RVA 0x34569930 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-141f60943613848c](../../evidence/conditions-sets-008.md#c-141f60943613848c)

### observed_connections-003560

```text
(config-router-scope)# bgp listen range <prefix:dynamic> peer-group <string> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 60 `；EOL ` RVA 0x34569170 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` IPv4 subnet range；` string ` peer-group name。

[条件 C-70b337016305f61b](../../evidence/conditions-sets-044.md#c-70b337016305f61b) · [缺口 G-cf6558f240dfdae4](../../evidence/gaps-sets-007.md#g-cf6558f240dfdae4) · [参数 P-9233a14c19005c49](../../evidence/parameters-sets-011.md#p-9233a14c19005c49)

### observed_connections-003175

```text
(config-router-scope)# bgp log-neighbor-changes <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 11 `；EOL ` RVA 0x34567B28 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f2d18c8b4e477c8c](../../evidence/conditions-sets-094.md#c-f2d18c8b4e477c8c)

### observed_connections-003320

```text
(config-router-scope)# bgp maxas-limit <number:1..254> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 26 `；EOL ` RVA 0x3456ED40 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of ASes in the AS-PATH attribute(max 254)。

[条件 C-a4b0cf74d55d44d7](../../evidence/conditions-sets-063.md#c-a4b0cf74d55d44d7) · [参数 P-44153a3218f0d626](../../evidence/parameters-sets-006.md#p-44153a3218f0d626)

### observed_connections-003309

```text
(config-router-scope)# bgp maxcommunity-limit <number:1..1018> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 27 `；EOL ` RVA 0x3456E350 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of communities in the COMMUNITY attribute。

[条件 C-95dc6d4ac813cef1](../../evidence/conditions-sets-058.md#c-95dc6d4ac813cef1) · [参数 P-ab7414d720ae1364](../../evidence/parameters-sets-013.md#p-ab7414d720ae1364)

### observed_connections-003316

```text
(config-router-scope)# bgp maxextcommunity-limit <number:1..509> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 29 `；EOL ` RVA 0x3456E9F0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of extended communities in the EXTENDED COMMUNITY attribute。

[条件 C-ffe58d7f6bc5a087](../../evidence/conditions-sets-099.md#c-ffe58d7f6bc5a087) · [参数 P-d2f9094a7fbf49ea](../../evidence/parameters-sets-016.md#p-d2f9094a7fbf49ea)

### observed_connections-003312

```text
(config-router-scope)# bgp maxlargecommunity-limit <number:1..339> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 28 `；EOL ` RVA 0x3456E6A0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of large communities in the LARGE COMMUNITY attribute。

[条件 C-ba5ef818ebbf51c9](../../evidence/conditions-sets-072.md#c-ba5ef818ebbf51c9) · [参数 P-43b317cfc6df44b0](../../evidence/parameters-sets-006.md#p-43b317cfc6df44b0)

### observed_connections-003189

```text
(config-router-scope)# bgp mpls-local-label <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 81 `；EOL ` RVA 0x34575B78 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b0bc0d7b5a3192d6](../../evidence/conditions-sets-068.md#c-b0bc0d7b5a3192d6)

### observed_connections-003366

```text
(config-router-scope)# bgp nexthop route-map <string> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 56 `；EOL ` RVA 0x345743F0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` route-map name。

[条件 C-0cf276f0d58f258f](../../evidence/conditions-sets-005.md#c-0cf276f0d58f258f) · [参数 P-00cff5a326a32144](../../evidence/parameters-sets-001.md#p-00cff5a326a32144)

### observed_connections-003283

```text
(config-router-scope)# bgp nexthop trigger critical-delay <number:0..100> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 48 `；EOL ` RVA 0x34574958 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Critical delay value (seconds)。

[条件 C-d4c438de4b42f1ef](../../evidence/conditions-sets-082.md#c-d4c438de4b42f1ef) · [参数 P-7591ec89f657e7a5](../../evidence/parameters-sets-009.md#p-7591ec89f657e7a5)

### observed_connections-003279

```text
(config-router-scope)# bgp nexthop trigger delay <number:0..100> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 47 `；EOL ` RVA 0x345746D8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Delay value (seconds)。

[条件 C-d400d8dd625fed8e](../../evidence/conditions-sets-082.md#c-d400d8dd625fed8e) · [参数 P-a4fed20caf95eebc](../../evidence/parameters-sets-013.md#p-a4fed20caf95eebc)

### observed_connections-003362

```text
(config-router-scope)# bgp nexthop trigger enable <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 49 `；EOL ` RVA 0x345746B0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cb9c5b4e371e2105](../../evidence/conditions-sets-078.md#c-cb9c5b4e371e2105)

### observed_connections-003373

```text
(config-router-scope)# bgp nopeerup-delay cold-boot <number:1..3600> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 74 `；EOL ` RVA 0x34569F58 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Delay in seconds。

[条件 C-c4108752facdd754](../../evidence/conditions-sets-076.md#c-c4108752facdd754) · [参数 P-1acf5679fb97f07b](../../evidence/parameters-sets-003.md#p-1acf5679fb97f07b) · [状态效果 S-200cca2c20b57734](../../evidence/state_effects-sets-007.md#s-200cca2c20b57734)

### observed_connections-003242

```text
(config-router-scope)# bgp recursion host <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 72 `；EOL ` RVA 0x34572A50 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-617372ad7b2daf22](../../evidence/conditions-sets-038.md#c-617372ad7b2daf22)

### observed_connections-003168

```text
(config-router-scope)# bgp redistribute-internal <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 2 `；EOL ` RVA 0x34576D78 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-98868e8ea2f0429e](../../evidence/conditions-sets-059.md#c-98868e8ea2f0429e)

### observed_connections-003387

```text
(config-router-scope)# bgp refresh max-eor-time <number:600..3600> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 16 `；EOL ` RVA 0x3456C328 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timer interval (seconds)。

[条件 C-d597c7dc0d3c9660](../../evidence/conditions-sets-082.md#c-d597c7dc0d3c9660) · [参数 P-47fee323a6f21a1b](../../evidence/parameters-sets-006.md#p-47fee323a6f21a1b)

### observed_connections-003383

```text
(config-router-scope)# bgp refresh stalepath-time <number:600..3600> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 15 `；EOL ` RVA 0x3456BFB8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timer interval (seconds)。

[条件 C-f5f6b51f66401ab5](../../evidence/conditions-sets-095.md#c-f5f6b51f66401ab5) · [参数 P-40144bc53ecaf885](../../evidence/parameters-sets-005.md#p-40144bc53ecaf885)

### observed_connections-003304

```text
(config-router-scope)# bgp regexp deterministic <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 44 `；EOL ` RVA 0x3456CD40 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e398f2ee0aabd351](../../evidence/conditions-sets-088.md#c-e398f2ee0aabd351)

### observed_connections-003243

```text
(config-router-scope)# bgp route-map priority <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 59 `；EOL ` RVA 0x34577F08 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a6eef08207e8589c](../../evidence/conditions-sets-064.md#c-a6eef08207e8589c)

### observed_connections-003162

```text
(config-router-scope)# bgp route-map-cache <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 34 `；EOL ` RVA 0x34565B80 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f2d18c8b4e477c8c](../../evidence/conditions-sets-094.md#c-f2d18c8b4e477c8c)

### observed_connections-003240

```text
(config-router-scope)# bgp router-id <address> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 4 `；EOL ` RVA 0x34564F38 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Manually configured router identifier。

[条件 C-fdf831d6cf32f327](../../evidence/conditions-sets-098.md#c-fdf831d6cf32f327) · [参数 P-5e7435a90173e4c1](../../evidence/parameters-sets-008.md#p-5e7435a90173e4c1)

### observed_connections-003275

```text
(config-router-scope)# bgp router-id auto-assign <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 4 `；EOL ` RVA 0x34573100 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2a0f39a9d33cdabe](../../evidence/conditions-sets-016.md#c-2a0f39a9d33cdabe) · [状态效果 S-7d866bee7a68f6e9](../../evidence/state_effects-sets-027.md#s-7d866bee7a68f6e9)

### observed_connections-003538

```text
(config-router-scope)# bgp router-id interface <interface> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 4 `；EOL ` RVA 0x34564F38 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-11c8c1eb0683184f](../../evidence/conditions-sets-007.md#c-11c8c1eb0683184f) · [缺口 G-76ed9108423128bd](../../evidence/gaps-sets-005.md#g-76ed9108423128bd) · [参数 P-ae6cd85a2b6c64f8](../../evidence/parameters-sets-013.md#p-ae6cd85a2b6c64f8)

### observed_connections-003539

```text
(config-router-scope)# bgp router-id interface <interface> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 4 `；EOL ` RVA 0x34573100 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1b0c9febde0dacaa](../../evidence/conditions-sets-011.md#c-1b0c9febde0dacaa) · [缺口 G-739146f72f2020ac](../../evidence/gaps-sets-004.md#g-739146f72f2020ac) · [参数 P-5516cc1a043c74f0](../../evidence/parameters-sets-007.md#p-5516cc1a043c74f0)

### observed_connections-003464

```text
(config-router-scope)# bgp rpki server tcp <address> port <number:1..65535> refresh <number:1..65535> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 76 `；EOL ` RVA 0x34578D20 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IPv6 address of RPKI cache server；` unsigned_number ` Port number；` unsigned_number ` Refresh time in seconds。

[条件 C-de4a98e22dc35703](../../evidence/conditions-sets-086.md#c-de4a98e22dc35703) · [参数 P-51d371163df6fb34](../../evidence/parameters-sets-007.md#p-51d371163df6fb34)

### observed_connections-003284

```text
(config-router-scope)# bgp rr-group <string> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 23 `；EOL ` RVA 0x34575398 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Extended community-list name。

[条件 C-d62fcdc71858e240](../../evidence/conditions-sets-083.md#c-d62fcdc71858e240) · [参数 P-840a92fe43458563](../../evidence/parameters-sets-010.md#p-840a92fe43458563)

### observed_connections-003199

```text
(config-router-scope)# bgp safe-ebgp-policy <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 92 `；EOL ` RVA 0x3456F2D8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b3c1a42a14d9bf4b](../../evidence/conditions-sets-070.md#c-b3c1a42a14d9bf4b)

### observed_connections-003281

```text
(config-router-scope)# bgp scan-time <number:5..60> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 22 `；EOL ` RVA 0x34575028 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Scanner interval (seconds)。

[条件 C-d54975684e7d66b8](../../evidence/conditions-sets-082.md#c-d54975684e7d66b8) · [参数 P-4ac08f37d767e2ab](../../evidence/parameters-sets-006.md#p-4ac08f37d767e2ab)

### observed_connections-003249

```text
(config-router-scope)# bgp slow-peer detection <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 67 `；EOL ` RVA 0x34576048 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a7c0ed15f5694d8c](../../evidence/conditions-sets-065.md#c-a7c0ed15f5694d8c)

### observed_connections-003245

```text
(config-router-scope)# bgp slow-peer detection threshold <number:120..3600> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 67 `；EOL ` RVA 0x34576020 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Threshold value (seconds)。

[条件 C-1418ffdc50a55348](../../evidence/conditions-sets-008.md#c-1418ffdc50a55348) · [参数 P-6eaff094a320e190](../../evidence/parameters-sets-009.md#p-6eaff094a320e190)

### observed_connections-003356

```text
(config-router-scope)# bgp slow-peer split-update-group dynamic <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 68 `；EOL ` RVA 0x34576618 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-21a8d3330fd70e82](../../evidence/conditions-sets-013.md#c-21a8d3330fd70e82)

### observed_connections-003372

```text
(config-router-scope)# bgp snmp traps add-type <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 90 `；EOL ` RVA 0x34568C40 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f2d18c8b4e477c8c](../../evidence/conditions-sets-094.md#c-f2d18c8b4e477c8c)

### observed_connections-003176

```text
(config-router-scope)# bgp soft-reconfig-backup <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 52 `；EOL ` RVA 0x34573FD8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-adf57b5967c3abb1](../../evidence/conditions-sets-067.md#c-adf57b5967c3abb1)

### observed_connections-003422

```text
(config-router-scope)# bgp sourced-paths per-net isis all <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 89 `；EOL ` RVA 0x34577B88 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d8d7c49542b93b9c](../../evidence/conditions-sets-083.md#c-d8d7c49542b93b9c) · [状态效果 S-29d95f8060e0366c](../../evidence/state_effects-sets-009.md#s-29d95f8060e0366c)

### observed_connections-003417

```text
(config-router-scope)# bgp sourced-paths per-net ospf all <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 87 `；EOL ` RVA 0x34577528 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d8d7c49542b93b9c](../../evidence/conditions-sets-083.md#c-d8d7c49542b93b9c) · [状态效果 S-6261812e15a865c1](../../evidence/state_effects-sets-021.md#s-6261812e15a865c1)

### observed_connections-003418

```text
(config-router-scope)# bgp sourced-paths per-net ospfv3 all <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 88 `；EOL ` RVA 0x34577870 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d8d7c49542b93b9c](../../evidence/conditions-sets-083.md#c-d8d7c49542b93b9c) · [状态效果 S-2646c94feaba7c57](../../evidence/state_effects-sets-009.md#s-2646c94feaba7c57)

### observed_connections-003414

```text
(config-router-scope)# bgp sourced-paths per-net static all <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 86 `；EOL ` RVA 0x345771E0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d8d7c49542b93b9c](../../evidence/conditions-sets-083.md#c-d8d7c49542b93b9c) · [状态效果 S-fc376559456c3563](../../evidence/state_effects-sets-053.md#s-fc376559456c3563)

### observed_connections-003300

```text
(config-router-scope)# bgp sso route-refresh-enable <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 38 `；EOL ` RVA 0x3456BBF8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e398f2ee0aabd351](../../evidence/conditions-sets-088.md#c-e398f2ee0aabd351)

### observed_connections-003170

```text
(config-router-scope)# bgp suppress-inactive <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 45 `；EOL ` RVA 0x34572D50 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4f05aeab7e8f8bdc](../../evidence/conditions-sets-031.md#c-4f05aeab7e8f8bdc)

### observed_connections-003134

```text
(config-router-scope)# bgp tid <number:1..255> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 55 `；EOL ` RVA 0x34564778 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Tolology identifier value。

[条件 C-81c53549a7e18fd4](../../evidence/conditions-sets-050.md#c-81c53549a7e18fd4) · [参数 P-a1d0f614296f703f](../../evidence/parameters-sets-012.md#p-a1d0f614296f703f)

### observed_connections-003250

```text
(config-router-scope)# bgp transport path-mtu-discovery <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 50 `；EOL ` RVA 0x345675F0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f2d18c8b4e477c8c](../../evidence/conditions-sets-094.md#c-f2d18c8b4e477c8c)

### observed_connections-003143

```text
(config-router-scope)# bgp update-delay <number:1..3600> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 30 `；EOL ` RVA 0x3456A570 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Delay value (seconds)。

[条件 C-cfe666a3a7f0f9eb](../../evidence/conditions-sets-080.md#c-cfe666a3a7f0f9eb) · [参数 P-d06f4e4ad9a60c25](../../evidence/parameters-sets-016.md#p-d06f4e4ad9a60c25)

### observed_connections-003340

```text
(config-router-scope)# bgp update-group split as-override <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 73 `；EOL ` RVA 0x345769E8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f4551f0fa238f3b5](../../evidence/conditions-sets-094.md#c-f4551f0fa238f3b5)

### observed_connections-003160

```text
(config-router-scope)# bgp upgrade-cli <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 33 `；EOL ` RVA 0x34564B90 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0bac9c68b382fb22](../../evidence/conditions-sets-005.md#c-0bac9c68b382fb22)

### observed_connections-003419

```text
(config-router-scope)# bgp va <address> mask <address> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 80 `；EOL ` RVA 0x345782B0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` BGP VA ip address；` address ` BGP VA mask address。

[条件 C-8c1f945d8e3de999](../../evidence/conditions-sets-054.md#c-8c1f945d8e3de999) · [参数 P-ab27800b69e6e243](../../evidence/parameters-sets-013.md#p-ab27800b69e6e243)

### observed_connections-003302

```text
(config-router-scope)# bgp vrf-update-optimisation off <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 66 `；EOL ` RVA 0x3456C6B0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e398f2ee0aabd351](../../evidence/conditions-sets-088.md#c-e398f2ee0aabd351)

### observed_connections-003389

```text
(config-router-scope)# bgp write-limit <number:500..2147483647> <number:500..2147483647> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 40 `；EOL ` RVA 0x3456CA08 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of messages to be formatted per neighbor/peergroup；` unsigned_number ` Number of messages that can be enqueued in total。

[条件 C-e8037753ae3c40d5](../../evidence/conditions-sets-090.md#c-e8037753ae3c40d5) · [参数 P-fd506d76a97e920c](../../evidence/parameters-sets-019.md#p-fd506d76a97e920c)

### observed_connections-003151

```text
(config-router-scope)# context <string> <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 0 `；EOL ` RVA 0x33C44A60 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` SNMP Context Name。

[条件 C-9affa1869574e86e](../../evidence/conditions-sets-060.md#c-9affa1869574e86e) · [参数 P-f3e465802edc027f](../../evidence/parameters-sets-018.md#p-f3e465802edc027f) · [状态效果 S-355a44aeb0ea4c7f](../../evidence/state_effects-sets-012.md#s-355a44aeb0ea4c7f)

### observed_connections-003365

```text
(config-router-scope)# default aggregate-address <address> <address> <cr>
```

Handler ` RVA 0xF1B7BE0 `；selector ` 0 `；EOL ` RVA 0x3457A030 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` Aggregate address；` address ` Aggregate mask。

[条件 C-4eb836e3175cf5bd](../../evidence/conditions-sets-031.md#c-4eb836e3175cf5bd) · [参数 P-034bf7990709c321](../../evidence/parameters-sets-001.md#p-034bf7990709c321) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003177

```text
(config-router-scope)# default auto-summary <cr>
```

Handler ` RVA 0xE1FA6B0 `；selector ` 0 `；EOL ` RVA 0x34563B88 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-fe8af09d9c1d13be](../../evidence/conditions-sets-098.md#c-fe8af09d9c1d13be) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003352

```text
(config-router-scope)# default bgp additional-paths install <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 69 `；EOL ` RVA 0x34571888 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c626df2c5a490a40](../../evidence/conditions-sets-076.md#c-c626df2c5a490a40) · [状态效果 S-e56d3e1a35f763fb](../../evidence/state_effects-sets-049.md#s-e56d3e1a35f763fb)

### observed_connections-003359

```text
(config-router-scope)# default bgp additional-paths select <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 71 `；EOL ` RVA 0x34571530 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5f537ef68ce3cb25](../../evidence/conditions-sets-037.md#c-5f537ef68ce3cb25) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003237

```text
(config-router-scope)# default bgp advertise-best-external <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 70 `；EOL ` RVA 0x345726D8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5ee23059aaf8eb3a](../../evidence/conditions-sets-037.md#c-5ee23059aaf8eb3a) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003290

```text
(config-router-scope)# default bgp advertisement startup-delay <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 95 `；EOL ` RVA 0x3456A548 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f7c142cf6532b5fb](../../evidence/conditions-sets-096.md#c-f7c142cf6532b5fb) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003360

```text
(config-router-scope)# default bgp aggregate-timer <number:6..60> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 58 `；EOL ` RVA 0x34578728 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Timer interval。

[条件 C-9828edb5d90b4a4a](../../evidence/conditions-sets-059.md#c-9828edb5d90b4a4a) · [参数 P-b1318a7e59a386fd](../../evidence/parameters-sets-013.md#p-b1318a7e59a386fd) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003317

```text
(config-router-scope)# default bgp aigp-rib-metric <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 91 `；EOL ` RVA 0x3456EFC8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e398f2ee0aabd351](../../evidence/conditions-sets-088.md#c-e398f2ee0aabd351) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003228

```text
(config-router-scope)# default bgp always-compare-med <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 5 `；EOL ` RVA 0x34565E30 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f2d18c8b4e477c8c](../../evidence/conditions-sets-094.md#c-f2d18c8b4e477c8c) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003339

```text
(config-router-scope)# default bgp asnotation dot <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 64 `；EOL ` RVA 0x34566140 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f2d18c8b4e477c8c](../../evidence/conditions-sets-094.md#c-f2d18c8b4e477c8c) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003446

```text
(config-router-scope)# default bgp bestpath aigp ignore <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 43 `；EOL ` RVA 0x3456DCF0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-af1a55da7d13e1c4](../../evidence/conditions-sets-068.md#c-af1a55da7d13e1c4) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003438

```text
(config-router-scope)# default bgp bestpath as-path ignore <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 17 `；EOL ` RVA 0x3456D460 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e398f2ee0aabd351](../../evidence/conditions-sets-088.md#c-e398f2ee0aabd351) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003441

```text
(config-router-scope)# default bgp bestpath as-path multipath-relax <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 51 `；EOL ` RVA 0x3456D708 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e398f2ee0aabd351](../../evidence/conditions-sets-088.md#c-e398f2ee0aabd351) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003394

```text
(config-router-scope)# default bgp bestpath compare-routerid <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 24 `；EOL ` RVA 0x3456D9A0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e398f2ee0aabd351](../../evidence/conditions-sets-088.md#c-e398f2ee0aabd351) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003445

```text
(config-router-scope)# default bgp bestpath cost-community ignore <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 41 `；EOL ` RVA 0x3456DFC8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e398f2ee0aabd351](../../evidence/conditions-sets-088.md#c-e398f2ee0aabd351) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003406

```text
(config-router-scope)# default bgp bestpath igp-metric ignore <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 42 `；EOL ` RVA 0x34571DB8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-96e540aecb31c83c](../../evidence/conditions-sets-058.md#c-96e540aecb31c83c) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003442

```text
(config-router-scope)# default bgp bestpath med missing-as-worst <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 18 `；EOL ` RVA 0x3456D150 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e398f2ee0aabd351](../../evidence/conditions-sets-088.md#c-e398f2ee0aabd351) · [状态效果 S-bf696abdb643d923](../../evidence/state_effects-sets-040.md#s-bf696abdb643d923)

### observed_connections-003411

```text
(config-router-scope)# default bgp bestpath prefix-validate allow-invalid <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 78 `；EOL ` RVA 0x345720C8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3a39bc8175d21cd0](../../evidence/conditions-sets-023.md#c-3a39bc8175d21cd0) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003415

```text
(config-router-scope)# default bgp bestpath prefix-validate disable <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 77 `；EOL ` RVA 0x34572370 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3a39bc8175d21cd0](../../evidence/conditions-sets-023.md#c-3a39bc8175d21cd0) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003355

```text
(config-router-scope)# default bgp client-to-client reflection <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 9 `；EOL ` RVA 0x34566FD0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7b5c81f0eb8f2c77](../../evidence/conditions-sets-048.md#c-7b5c81f0eb8f2c77) · [状态效果 S-0596650c62e12531](../../evidence/state_effects-sets-002.md#s-0596650c62e12531)

### observed_connections-003256

```text
(config-router-scope)# default bgp cluster-id <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 7 `；EOL ` RVA 0x34566B98 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a1319a74fcbc0342](../../evidence/conditions-sets-062.md#c-a1319a74fcbc0342) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003265

```text
(config-router-scope)# default bgp consistency-checker <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 3 `；EOL ` RVA 0x34566518 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-20ff5c2749a7396e](../../evidence/conditions-sets-013.md#c-20ff5c2749a7396e) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003229

```text
(config-router-scope)# default bgp dampening <cr>
```

Handler ` RVA 0xF1B85B0 `；selector ` 0 `；EOL ` RVA 0x34570950 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-cd87ed64aaa928f1](../../evidence/conditions-sets-079.md#c-cd87ed64aaa928f1) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003408

```text
(config-router-scope)# default bgp default inter-as-hybrid advertise-source-routes <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 57 `；EOL ` RVA 0x3456FF88 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6db1be956b0c537b](../../evidence/conditions-sets-042.md#c-6db1be956b0c537b) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003327

```text
(config-router-scope)# default bgp default ipv4-unicast <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 19 `；EOL ` RVA 0x3456F6E0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b70918c03dee8921](../../evidence/conditions-sets-071.md#c-b70918c03dee8921) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003331

```text
(config-router-scope)# default bgp default ipv6-nexthop <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 75 `；EOL ` RVA 0x3456F9D8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8c098b49402f3cfe](../../evidence/conditions-sets-054.md#c-8c098b49402f3cfe) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003231

```text
(config-router-scope)# default bgp default local-preference <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 0 `；EOL ` RVA 0x3456FC68 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f27a7ecd86b59dda](../../evidence/conditions-sets-094.md#c-f27a7ecd86b59dda) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003402

```text
(config-router-scope)# default bgp default route-target filter <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 25 `；EOL ` RVA 0x345702F0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6e88b262d39af1db](../../evidence/conditions-sets-043.md#c-6e88b262d39af1db) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003403

```text
(config-router-scope)# default bgp default route-target filter <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 25 `；EOL ` RVA 0x34570590 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-dcc3a1ccdaf9a9a8](../../evidence/conditions-sets-085.md#c-dcc3a1ccdaf9a9a8) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003278

```text
(config-router-scope)# default bgp deterministic-med <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 10 `；EOL ` RVA 0x34568650 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f2d18c8b4e477c8c](../../evidence/conditions-sets-094.md#c-f2d18c8b4e477c8c) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003252

```text
(config-router-scope)# default bgp dmzlink-bw <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 31 `；EOL ` RVA 0x34573C88 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c52df1d2f09c863e](../../evidence/conditions-sets-076.md#c-c52df1d2f09c863e) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003185

```text
(config-router-scope)# default bgp dynamic-med-interval <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 21 `；EOL ` RVA 0x34568678 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5cc28ec88c2bdc5f](../../evidence/conditions-sets-036.md#c-5cc28ec88c2bdc5f) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003259

```text
(config-router-scope)# default bgp enforce-first-as <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 20 `；EOL ` RVA 0x34567880 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f2d18c8b4e477c8c](../../evidence/conditions-sets-094.md#c-f2d18c8b4e477c8c) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003293

```text
(config-router-scope)# default bgp enhanced-error <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 82 `；EOL ` RVA 0x3456A2C0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0102661ded552d0e](../../evidence/conditions-sets-001.md#c-0102661ded552d0e) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003213

```text
(config-router-scope)# default bgp fast-external-fallover <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 1 `；EOL ` RVA 0x34565568 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f2d18c8b4e477c8c](../../evidence/conditions-sets-094.md#c-f2d18c8b4e477c8c) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003303

```text
(config-router-scope)# default bgp graceful-restart <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 35 `；EOL ` RVA 0x3456B130 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f2d18c8b4e477c8c](../../evidence/conditions-sets-094.md#c-f2d18c8b4e477c8c) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003296

```text
(config-router-scope)# default bgp graceful-restart restart-time <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 36 `；EOL ` RVA 0x3456AB00 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-43e2e64c73e0b6ec](../../evidence/conditions-sets-027.md#c-43e2e64c73e0b6ec) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003298

```text
(config-router-scope)# default bgp graceful-restart stalepath-time <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 37 `；EOL ` RVA 0x3456AB68 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-717bb31629fa6281](../../evidence/conditions-sets-044.md#c-717bb31629fa6281) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003462

```text
(config-router-scope)# default bgp graceful-shutdown all vrfs activate <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 79 `；EOL ` RVA 0x3456B598 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f71ec471c4706ed6](../../evidence/conditions-sets-095.md#c-f71ec471c4706ed6) · [状态效果 S-1c4bb20b83299cff](../../evidence/state_effects-sets-006.md#s-1c4bb20b83299cff)

### observed_connections-003460

```text
(config-router-scope)# default bgp inject-map <string> exist-map <string> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 32 `；EOL ` RVA 0x34575800 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` route-map name；` string ` route-map name。

[条件 C-ef65e2591e463555](../../evidence/conditions-sets-092.md#c-ef65e2591e463555) · [参数 P-15b069a9948617b7](../../evidence/parameters-sets-002.md#p-15b069a9948617b7) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003401

```text
(config-router-scope)# default bgp label-allocation-batch <number:0..4294967295> <number:0..4294967295> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 53 `；EOL ` RVA 0x345658F8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Timer value in milliseconds；` unsigned_number ` Batch Size。

[条件 C-f2d18c8b4e477c8c](../../evidence/conditions-sets-094.md#c-f2d18c8b4e477c8c) · [参数 P-67d56dc38a8352d0](../../evidence/parameters-sets-008.md#p-67d56dc38a8352d0) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003424

```text
(config-router-scope)# default bgp listen block <address> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 93 `；EOL ` RVA 0x34573698 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IPv4 Dynamic Peering Address。

[条件 C-9bc5921baff5d9a8](../../evidence/conditions-sets-060.md#c-9bc5921baff5d9a8) · [参数 P-dd46f1481a83f05c](../../evidence/parameters-sets-017.md#p-dd46f1481a83f05c) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003435

```text
(config-router-scope)# default bgp listen block <address> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 93 `；EOL ` RVA 0x345695F8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IPv4 Dynamic Peering Address。

[条件 C-141f60943613848c](../../evidence/conditions-sets-008.md#c-141f60943613848c) · [参数 P-6ed5db196fb7f6a7](../../evidence/parameters-sets-009.md#p-6ed5db196fb7f6a7) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003272

```text
(config-router-scope)# default bgp listen limit <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 61 `；EOL ` RVA 0x345735E0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-37c1185f48abc32a](../../evidence/conditions-sets-022.md#c-37c1185f48abc32a) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003294

```text
(config-router-scope)# default bgp listen limit <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 61 `；EOL ` RVA 0x34569518 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad0cd13cea4c0d57](../../evidence/conditions-sets-067.md#c-ad0cd13cea4c0d57) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003377

```text
(config-router-scope)# default bgp listen persistent <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 94 `；EOL ` RVA 0x34569930 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-141f60943613848c](../../evidence/conditions-sets-008.md#c-141f60943613848c) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003269

```text
(config-router-scope)# default bgp log-neighbor-changes <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 11 `；EOL ` RVA 0x34567B28 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f2d18c8b4e477c8c](../../evidence/conditions-sets-094.md#c-f2d18c8b4e477c8c) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003322

```text
(config-router-scope)# default bgp maxas-limit <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 26 `；EOL ` RVA 0x3456ED40 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3c3b228d8dcf87ad](../../evidence/conditions-sets-023.md#c-3c3b228d8dcf87ad) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003310

```text
(config-router-scope)# default bgp maxcommunity-limit <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 27 `；EOL ` RVA 0x3456E350 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-33c982bcb3ea3fd4](../../evidence/conditions-sets-020.md#c-33c982bcb3ea3fd4) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003318

```text
(config-router-scope)# default bgp maxextcommunity-limit <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 29 `；EOL ` RVA 0x3456E9F0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-56f5b792821c7159](../../evidence/conditions-sets-034.md#c-56f5b792821c7159) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003314

```text
(config-router-scope)# default bgp maxlargecommunity-limit <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 28 `；EOL ` RVA 0x3456E6A0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f3f4ad31e04f762e](../../evidence/conditions-sets-094.md#c-f3f4ad31e04f762e) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003288

```text
(config-router-scope)# default bgp mpls-local-label <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 81 `；EOL ` RVA 0x34575B78 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b0bc0d7b5a3192d6](../../evidence/conditions-sets-068.md#c-b0bc0d7b5a3192d6) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003427

```text
(config-router-scope)# default bgp nexthop route-map <string> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 56 `；EOL ` RVA 0x345743F0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` route-map name。

[条件 C-0cf276f0d58f258f](../../evidence/conditions-sets-005.md#c-0cf276f0d58f258f) · [参数 P-00cff5a326a32144](../../evidence/parameters-sets-001.md#p-00cff5a326a32144) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003371

```text
(config-router-scope)# default bgp nexthop trigger critical-delay <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 48 `；EOL ` RVA 0x34574958 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-26459da32ebaee08](../../evidence/conditions-sets-015.md#c-26459da32ebaee08) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003368

```text
(config-router-scope)# default bgp nexthop trigger delay <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 47 `；EOL ` RVA 0x345746D8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d3544264df4a03f0](../../evidence/conditions-sets-081.md#c-d3544264df4a03f0) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003423

```text
(config-router-scope)# default bgp nexthop trigger enable <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 49 `；EOL ` RVA 0x345746B0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-cb9c5b4e371e2105](../../evidence/conditions-sets-078.md#c-cb9c5b4e371e2105) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003433

```text
(config-router-scope)# default bgp nopeerup-delay cold-boot <number:1..3600> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 74 `；EOL ` RVA 0x34569F58 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Delay in seconds。

[条件 C-c4108752facdd754](../../evidence/conditions-sets-076.md#c-c4108752facdd754) · [参数 P-1acf5679fb97f07b](../../evidence/parameters-sets-003.md#p-1acf5679fb97f07b) · [状态效果 S-de233083bf32e254](../../evidence/state_effects-sets-047.md#s-de233083bf32e254)

### observed_connections-003346

```text
(config-router-scope)# default bgp recursion host <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 72 `；EOL ` RVA 0x34572A50 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-617372ad7b2daf22](../../evidence/conditions-sets-038.md#c-617372ad7b2daf22) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003238

```text
(config-router-scope)# default bgp redistribute-internal <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 2 `；EOL ` RVA 0x34576D78 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-98868e8ea2f0429e](../../evidence/conditions-sets-059.md#c-98868e8ea2f0429e) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003388

```text
(config-router-scope)# default bgp refresh max-eor-time <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 16 `；EOL ` RVA 0x3456C328 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4b162475ddc44cf5](../../evidence/conditions-sets-029.md#c-4b162475ddc44cf5) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003384

```text
(config-router-scope)# default bgp refresh stalepath-time <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 15 `；EOL ` RVA 0x3456BFB8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3172f4887be76883](../../evidence/conditions-sets-019.md#c-3172f4887be76883) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003386

```text
(config-router-scope)# default bgp regexp deterministic <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 44 `；EOL ` RVA 0x3456CD40 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e398f2ee0aabd351](../../evidence/conditions-sets-088.md#c-e398f2ee0aabd351) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003347

```text
(config-router-scope)# default bgp route-map priority <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 59 `；EOL ` RVA 0x34577F08 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a6eef08207e8589c](../../evidence/conditions-sets-064.md#c-a6eef08207e8589c) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003221

```text
(config-router-scope)# default bgp route-map-cache <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 34 `；EOL ` RVA 0x34565B80 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f2d18c8b4e477c8c](../../evidence/conditions-sets-094.md#c-f2d18c8b4e477c8c) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003230

```text
(config-router-scope)# default bgp router-id <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 4 `；EOL ` RVA 0x34564F38 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d90fc631d217417b](../../evidence/conditions-sets-084.md#c-d90fc631d217417b) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003274

```text
(config-router-scope)# default bgp router-id <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 4 `；EOL ` RVA 0x34573100 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5af9949f35161899](../../evidence/conditions-sets-036.md#c-5af9949f35161899) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003466

```text
(config-router-scope)# default bgp rpki server tcp <address> port <number:1..65535> refresh <number:1..65535> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 76 `；EOL ` RVA 0x34578D20 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IPv6 address of RPKI cache server；` unsigned_number ` Port number；` unsigned_number ` Refresh time in seconds。

[条件 C-de4a98e22dc35703](../../evidence/conditions-sets-086.md#c-de4a98e22dc35703) · [参数 P-51d371163df6fb34](../../evidence/parameters-sets-007.md#p-51d371163df6fb34) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003282

```text
(config-router-scope)# default bgp rr-group <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 23 `；EOL ` RVA 0x34575398 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f09f6f09191720f6](../../evidence/conditions-sets-093.md#c-f09f6f09191720f6) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003323

```text
(config-router-scope)# default bgp safe-ebgp-policy <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 92 `；EOL ` RVA 0x3456F2D8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b3c1a42a14d9bf4b](../../evidence/conditions-sets-070.md#c-b3c1a42a14d9bf4b) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003370

```text
(config-router-scope)# default bgp scan-time <number:5..60> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 22 `；EOL ` RVA 0x34575028 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Scanner interval (seconds)。

[条件 C-d54975684e7d66b8](../../evidence/conditions-sets-082.md#c-d54975684e7d66b8) · [参数 P-4ac08f37d767e2ab](../../evidence/parameters-sets-006.md#p-4ac08f37d767e2ab) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003349

```text
(config-router-scope)# default bgp slow-peer detection <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 67 `；EOL ` RVA 0x34576048 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f390138f1d9da875](../../evidence/conditions-sets-094.md#c-f390138f1d9da875) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003416

```text
(config-router-scope)# default bgp slow-peer split-update-group dynamic <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 68 `；EOL ` RVA 0x34576618 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-dde653062f764457](../../evidence/conditions-sets-085.md#c-dde653062f764457) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003430

```text
(config-router-scope)# default bgp snmp traps add-type <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 90 `；EOL ` RVA 0x34568C40 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f2d18c8b4e477c8c](../../evidence/conditions-sets-094.md#c-f2d18c8b4e477c8c) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003270

```text
(config-router-scope)# default bgp soft-reconfig-backup <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 52 `；EOL ` RVA 0x34573FD8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-adf57b5967c3abb1](../../evidence/conditions-sets-067.md#c-adf57b5967c3abb1) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003458

```text
(config-router-scope)# default bgp sourced-paths per-net isis all <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 89 `；EOL ` RVA 0x34577B88 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d8d7c49542b93b9c](../../evidence/conditions-sets-083.md#c-d8d7c49542b93b9c) · [状态效果 S-377f4f01c5f29c70](../../evidence/state_effects-sets-012.md#s-377f4f01c5f29c70)

### observed_connections-003454

```text
(config-router-scope)# default bgp sourced-paths per-net ospf all <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 87 `；EOL ` RVA 0x34577528 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d8d7c49542b93b9c](../../evidence/conditions-sets-083.md#c-d8d7c49542b93b9c) · [状态效果 S-9332dca5140f8154](../../evidence/state_effects-sets-031.md#s-9332dca5140f8154)

### observed_connections-003456

```text
(config-router-scope)# default bgp sourced-paths per-net ospfv3 all <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 88 `；EOL ` RVA 0x34577870 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d8d7c49542b93b9c](../../evidence/conditions-sets-083.md#c-d8d7c49542b93b9c) · [状态效果 S-ed4eaa330e3d2599](../../evidence/state_effects-sets-050.md#s-ed4eaa330e3d2599)

### observed_connections-003452

```text
(config-router-scope)# default bgp sourced-paths per-net static all <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 86 `；EOL ` RVA 0x345771E0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d8d7c49542b93b9c](../../evidence/conditions-sets-083.md#c-d8d7c49542b93b9c) · [状态效果 S-e936dba01a85a52f](../../evidence/state_effects-sets-049.md#s-e936dba01a85a52f)

### observed_connections-003378

```text
(config-router-scope)# default bgp sso route-refresh-enable <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 38 `；EOL ` RVA 0x3456BBF8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e398f2ee0aabd351](../../evidence/conditions-sets-088.md#c-e398f2ee0aabd351) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003244

```text
(config-router-scope)# default bgp suppress-inactive <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 45 `；EOL ` RVA 0x34572D50 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4f05aeab7e8f8bdc](../../evidence/conditions-sets-031.md#c-4f05aeab7e8f8bdc) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003152

```text
(config-router-scope)# default bgp tid <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 55 `；EOL ` RVA 0x34564778 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-cfff907ac6ec2dfc](../../evidence/conditions-sets-080.md#c-cfff907ac6ec2dfc) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003354

```text
(config-router-scope)# default bgp transport path-mtu-discovery <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 50 `；EOL ` RVA 0x345675F0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f2d18c8b4e477c8c](../../evidence/conditions-sets-094.md#c-f2d18c8b4e477c8c) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003193

```text
(config-router-scope)# default bgp update-delay <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 30 `；EOL ` RVA 0x3456A570 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-37b87d3cea420fa7](../../evidence/conditions-sets-022.md#c-37b87d3cea420fa7) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003409

```text
(config-router-scope)# default bgp update-group split as-override <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 73 `；EOL ` RVA 0x345769E8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f4551f0fa238f3b5](../../evidence/conditions-sets-094.md#c-f4551f0fa238f3b5) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003218

```text
(config-router-scope)# default bgp upgrade-cli <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 33 `；EOL ` RVA 0x34564B90 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0bac9c68b382fb22](../../evidence/conditions-sets-005.md#c-0bac9c68b382fb22) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003262

```text
(config-router-scope)# default bgp va <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 80 `；EOL ` RVA 0x345782B0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-47643ee2b82c3fc9](../../evidence/conditions-sets-028.md#c-47643ee2b82c3fc9) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003382

```text
(config-router-scope)# default bgp vrf-update-optimisation off <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 66 `；EOL ` RVA 0x3456C6B0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e398f2ee0aabd351](../../evidence/conditions-sets-088.md#c-e398f2ee0aabd351) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003306

```text
(config-router-scope)# default bgp write-limit <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 40 `；EOL ` RVA 0x3456CA08 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a4f645f11b999165](../../evidence/conditions-sets-064.md#c-a4f645f11b999165) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003149

```text
(config-router-scope)# default context <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 0 `；EOL ` RVA 0x33C44A60 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ada418e0516d363b](../../evidence/conditions-sets-067.md#c-ada418e0516d363b) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003273

```text
(config-router-scope)# default default-information originate <cr>
```

Handler ` RVA 0xE1F1F70 `；selector ` 0 `；EOL ` RVA 0x345619E0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-93c7ea10e301538b](../../evidence/conditions-sets-057.md#c-93c7ea10e301538b) · [状态效果 S-66b6c3991418c146](../../evidence/state_effects-sets-022.md#s-66b6c3991418c146)

### observed_connections-003180

```text
(config-router-scope)# default default-metric <cr>
```

Handler ` RVA 0xE1F35A0 `；selector ` 0 `；EOL ` RVA 0x345622A8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-686ef7b6670a0bde](../../evidence/conditions-sets-040.md#c-686ef7b6670a0bde) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003187

```text
(config-router-scope)# default distance <cr>
```

Handler ` RVA 0xE1E3290 `；selector ` 1 `；EOL ` RVA 0x34563400 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d3c5260364cdefc6](../../evidence/conditions-sets-082.md#c-d3c5260364cdefc6) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003287

```text
(config-router-scope)# default distribute-list in <cr>
```

Handler ` RVA 0xE1EE180 `；selector ` 0 `；EOL ` RVA 0x34562998 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-34a74756eb57dba7](../../evidence/conditions-sets-020.md#c-34a74756eb57dba7) · [状态效果 S-1b200e3f7d18f315](../../evidence/state_effects-sets-006.md#s-1b200e3f7d18f315)

### observed_connections-003140

```text
(config-router-scope)# default flash-update-threshold <cr>
```

Handler ` RVA 0xE1F7ED0 `；selector ` 0 `；EOL ` RVA 0x345614D0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-910a907e95c536c8](../../evidence/conditions-sets-056.md#c-910a907e95c536c8) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003138

```text
(config-router-scope)# default input-queue <cr>
```

Handler ` RVA 0xE1F8060 `；selector ` 0 `；EOL ` RVA 0x345611E0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-340cbb835bbba65e](../../evidence/conditions-sets-020.md#c-340cbb835bbba65e) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003215

```text
(config-router-scope)# default metric holddown <cr>
```

Handler ` RVA 0xE1F32D0 `；selector ` 1 `；EOL ` RVA 0x34560020 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2cf7c428a8ff3153](../../evidence/conditions-sets-018.md#c-2cf7c428a8ff3153) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003163

```text
(config-router-scope)# default metric maximum-hops <cr>
```

Handler ` RVA 0xE1F32D0 `；selector ` 2 `；EOL ` RVA 0x34560048 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-35da3690756c098b](../../evidence/conditions-sets-021.md#c-35da3690756c098b) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003241

```text
(config-router-scope)# default metric weights <cr>
```

Handler ` RVA 0xE1F32D0 `；selector ` 0 `；EOL ` RVA 0x34560608 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-92410408b9adf98e](../../evidence/conditions-sets-056.md#c-92410408b9adf98e) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003336

```text
(config-router-scope)# default offset-list <number:0..99> in <cr>
```

Handler ` RVA 0xE1F1330 `；selector ` 0 `；EOL ` RVA 0x3455F180 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Access list of networks to apply offset (0 selects all networks)。

[条件 C-066834b2881d9895](../../evidence/conditions-sets-003.md#c-066834b2881d9895) · [参数 P-0d8ea1ddb3233815](../../evidence/parameters-sets-001.md#p-0d8ea1ddb3233815) · [状态效果 S-215cc011a7049329](../../evidence/state_effects-sets-008.md#s-215cc011a7049329)

### observed_connections-003135

```text
(config-router-scope)# default output-delay <cr>
```

Handler ` RVA 0xE1F4590 `；selector ` 0 `；EOL ` RVA 0x3455EBD8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-cedbc527afa1727b](../../evidence/conditions-sets-080.md#c-cedbc527afa1727b) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003212

```text
(config-router-scope)# default passive-interface default <cr>
```

Handler ` RVA 0xE1F3960 `；selector ` 0 `；EOL ` RVA 0x3455E7C8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-871fa36dcb79c5f9](../../evidence/conditions-sets-052.md#c-871fa36dcb79c5f9) · [状态效果 S-73b8c5cabce36238](../../evidence/state_effects-sets-025.md#s-73b8c5cabce36238)

### observed_connections-003210

```text
(config-router-scope)# default redistribute maximum-prefix <cr>
```

Handler ` RVA 0xE1E4550 `；selector ` 0 `；EOL ` RVA 0x3455B7C0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-13b1399f49011521](../../evidence/conditions-sets-008.md#c-13b1399f49011521) · [状态效果 S-9a24f9d213ff610f](../../evidence/state_effects-sets-033.md#s-9a24f9d213ff610f)

### observed_connections-003224

```text
(config-router-scope)# default snmp context <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 0 `；EOL ` RVA 0x33C455F0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7598dc8aeb3669dc](../../evidence/conditions-sets-046.md#c-7598dc8aeb3669dc) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003451

```text
(config-router-scope)# default snmp context <string> community <string> <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 2 `；EOL ` RVA 0x33C45118 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Context Name；` string ` SNMP community string。

[条件 C-2573c969c66067b6](../../evidence/conditions-sets-015.md#c-2573c969c66067b6) · [参数 P-9b6eb89831feec60](../../evidence/parameters-sets-012.md#p-9b6eb89831feec60) · [状态效果 S-558cd4194b195b37](../../evidence/state_effects-sets-019.md#s-558cd4194b195b37)

### observed_connections-003450

```text
(config-router-scope)# default snmp context <string> user <string> <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 23 `；EOL ` RVA 0x33C456D0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Context Name；` string ` Name of the user。

[条件 C-67e2e80e2c1c144d](../../evidence/conditions-sets-040.md#c-67e2e80e2c1c144d) · [参数 P-cfc42ec8ad667e32](../../evidence/parameters-sets-016.md#p-cfc42ec8ad667e32) · [状态效果 S-0e9b9516134e077e](../../evidence/state_effects-sets-003.md#s-0e9b9516134e077e)

### observed_connections-003325

```text
(config-router-scope)# default summary-prefix <address> <address> <cr>
```

Handler ` RVA 0xE1DF4C0 `；selector ` 0 `；EOL ` RVA 0x3455AA40 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IP summary address；` address ` Summary mask。

[条件 C-1a5e60b8f6002ba8](../../evidence/conditions-sets-010.md#c-1a5e60b8f6002ba8) · [参数 P-88254a7499e8ab7c](../../evidence/parameters-sets-011.md#p-88254a7499e8ab7c) · [状态效果 S-05983050cf9aab77](../../evidence/state_effects-sets-002.md#s-05983050cf9aab77)

### observed_connections-003205

```text
(config-router-scope)# default summary-prefix <address> <cr>
```

Handler ` RVA 0xE1DF4C0 `；selector ` 21 `；EOL ` RVA 0x3455B020 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IP summary address。

[条件 C-9e5ef86b4609e742](../../evidence/conditions-sets-061.md#c-9e5ef86b4609e742) · [参数 P-c986c0ac48cc66f9](../../evidence/parameters-sets-015.md#p-c986c0ac48cc66f9) · [状态效果 S-05983050cf9aab77](../../evidence/state_effects-sets-002.md#s-05983050cf9aab77)

### observed_connections-003146

```text
(config-router-scope)# default synchronization <cr>
```

Handler ` RVA 0xF1CF320 `；selector ` 0 `；EOL ` RVA 0x34564008 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0fd33edbcb984768](../../evidence/conditions-sets-006.md#c-0fd33edbcb984768) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003155

```text
(config-router-scope)# default table-map <cr>
```

Handler ` RVA 0xE1F4690 `；selector ` 0 `；EOL ` RVA 0x345643E0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-31a2d5a24a70082d](../../evidence/conditions-sets-019.md#c-31a2d5a24a70082d) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003201

```text
(config-router-scope)# default timers basic <cr>
```

Handler ` RVA 0xE1F2D60 `；selector ` 0 `；EOL ` RVA 0x34559F60 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-984aaee1a59941f6](../../evidence/conditions-sets-059.md#c-984aaee1a59941f6) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003207

```text
(config-router-scope)# default timers bgp <cr>
```

Handler ` RVA 0xF1C7360 `；selector ` 0 `；EOL ` RVA 0x3458ED50 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-dda053afbcbc2f4f](../../evidence/conditions-sets-085.md#c-dda053afbcbc2f4f) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003147

```text
(config-router-scope)# default version <cr>
```

Handler ` RVA 0xFB4F020 `；selector ` 0 `；EOL ` RVA 0x3455A4F0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c7762695a588821b](../../evidence/conditions-sets-077.md#c-c7762695a588821b) · [状态效果 S-b09886271a7b163b](../../evidence/state_effects-sets-037.md#s-b09886271a7b163b)

### observed_connections-003179

```text
(config-router-scope)# default-information originate <cr>
```

Handler ` RVA 0xE1F1F70 `；selector ` 0 `；EOL ` RVA 0x345619E0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-93c7ea10e301538b](../../evidence/conditions-sets-057.md#c-93c7ea10e301538b) · [状态效果 S-7faaf81826f475bb](../../evidence/state_effects-sets-027.md#s-7faaf81826f475bb)

### observed_connections-003181

```text
(config-router-scope)# default-metric <number:1..16777214> <cr>
```

Handler ` RVA 0xE1F35A0 `；selector ` 0 `；EOL ` RVA 0x345622A8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` OSPF default metric。

[条件 C-c42f74a076797b3b](../../evidence/conditions-sets-076.md#c-c42f74a076797b3b) · [参数 P-6e79539e43d08751](../../evidence/parameters-sets-009.md#p-6e79539e43d08751)

### observed_connections-003184

```text
(config-router-scope)# distance <number:1..255> <cr>
```

Handler ` RVA 0xE1E3290 `；selector ` 1 `；EOL ` RVA 0x34563400 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Administrative distance。

[条件 C-df8baf7f4eb92146](../../evidence/conditions-sets-086.md#c-df8baf7f4eb92146) · [参数 P-c9c39e1d51cb0557](../../evidence/parameters-sets-015.md#p-c9c39e1d51cb0557)

### observed_connections-003188

```text
(config-router-scope)# distribute-list in <cr>
```

Handler ` RVA 0xE1EE180 `；selector ` 0 `；EOL ` RVA 0x34562998 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-34a74756eb57dba7](../../evidence/conditions-sets-020.md#c-34a74756eb57dba7) · [状态效果 S-4a9d6c32a86452a4](../../evidence/state_effects-sets-016.md#s-4a9d6c32a86452a4)

### observed_connections-003517

```text
(config-router-scope)# distribute-list out <?router_action_proc_vpn@555589ab6920> <cr>
```

Handler ` RVA 0xE1EE180 `；selector ` 0 `；EOL ` RVA 0x34562998 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-cd79ca25d3c303bf](../../evidence/conditions-sets-079.md#c-cd79ca25d3c303bf) · [缺口 G-a653897c73caf039](../../evidence/gaps-sets-006.md#g-a653897c73caf039) · [状态效果 S-0ae29d980da63d9c](../../evidence/state_effects-sets-003.md#s-0ae29d980da63d9c)

### observed_connections-003131

```text
(config-router-scope)# exit-scope <cr>
```

Handler ` RVA 0xF1EE330 `；selector ` 0 `；EOL ` RVA 0x345590A8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d552b2c0c4d4519b](../../evidence/conditions-sets-082.md#c-d552b2c0c4d4519b)

### observed_connections-003130

```text
(config-router-scope)# flash-update-threshold <number:0..30> <cr>
```

Handler ` RVA 0xE1F7ED0 `；selector ` 0 `；EOL ` RVA 0x345614D0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` threshold in seconds。

[条件 C-2de441310968f584](../../evidence/conditions-sets-018.md#c-2de441310968f584) · [参数 P-62fcdd5acc296472](../../evidence/parameters-sets-008.md#p-62fcdd5acc296472)

### observed_connections-003129

```text
(config-router-scope)# input-queue <number:0..1024> <cr>
```

Handler ` RVA 0xE1F8060 `；selector ` 0 `；EOL ` RVA 0x345611E0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` queue depth。

[条件 C-3ad1275923e5cb29](../../evidence/conditions-sets-023.md#c-3ad1275923e5cb29) · [参数 P-6a34b304708dfc30](../../evidence/parameters-sets-008.md#p-6a34b304708dfc30)

### observed_connections-003475

```text
(config-router-scope)# maximum-paths <number:dynamic> <cr>
```

Handler ` RVA 0xE1E26B0 `；selector ` 0 `；EOL ` RVA 0x34560CF8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Number of paths。

[条件 C-d530ad8cf35494a3](../../evidence/conditions-sets-082.md#c-d530ad8cf35494a3) · [缺口 G-b5e556fbe61586bf](../../evidence/gaps-sets-006.md#g-b5e556fbe61586bf) · [参数 P-b626aa75994e53ca](../../evidence/parameters-sets-014.md#p-b626aa75994e53ca)

### observed_connections-003159

```text
(config-router-scope)# metric holddown <cr>
```

Handler ` RVA 0xE1F32D0 `；selector ` 1 `；EOL ` RVA 0x34560020 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2cf7c428a8ff3153](../../evidence/conditions-sets-018.md#c-2cf7c428a8ff3153)

### observed_connections-003136

```text
(config-router-scope)# metric maximum-hops <number:1..255> <cr>
```

Handler ` RVA 0xE1F32D0 `；selector ` 2 `；EOL ` RVA 0x34560048 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Hop count。

[条件 C-1faa37570f357214](../../evidence/conditions-sets-012.md#c-1faa37570f357214) · [参数 P-21d2a75056500473](../../evidence/parameters-sets-003.md#p-21d2a75056500473)

### observed_connections-003463

```text
(config-router-scope)# metric weights <number:0..8> <number:0..255> <number:0..255> <number:0..255> <number:0..255> <number:0..255> <cr>
```

Handler ` RVA 0xE1F32D0 `；selector ` 0 `；EOL ` RVA 0x34560608 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Type Of Service (Only TOS 0 supported)；` unsigned_number ` K1；` unsigned_number ` K2；` unsigned_number ` K3；` unsigned_number ` K4；` unsigned_number ` K5。

[条件 C-833b1becd4a64802](../../evidence/conditions-sets-051.md#c-833b1becd4a64802) · [参数 P-81144059ac38a544](../../evidence/parameters-sets-010.md#p-81144059ac38a544)

### observed_connections-003467

```text
(config-router-scope)# neighbor <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 0 `；EOL ` RVA 0x345593B8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-866e98edd9ef1faf](../../evidence/conditions-sets-052.md#c-866e98edd9ef1faf) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [状态效果 S-e1e8d22418e3aae6](../../evidence/state_effects-sets-048.md#s-e1e8d22418e3aae6)

### observed_connections-003469

```text
(config-router-scope)# neighbor <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 0 `；EOL ` RVA 0x3458AAF0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c8a56f70600b8e2d](../../evidence/conditions-sets-077.md#c-c8a56f70600b8e2d) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [状态效果 S-e1e8d22418e3aae6](../../evidence/state_effects-sets-048.md#s-e1e8d22418e3aae6)

### observed_connections-003498

```text
(config-router-scope)# neighbor accept-route-legacy-rt <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 71 `；EOL ` RVA 0x345858E0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f1d6c9141e8225a1](../../evidence/conditions-sets-093.md#c-f1d6c9141e8225a1) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [状态效果 S-e1e8d22418e3aae6](../../evidence/state_effects-sets-048.md#s-e1e8d22418e3aae6)

### observed_connections-003504

```text
(config-router-scope)# neighbor activate <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 35 `；EOL ` RVA 0x34588B98 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-71a67fc649c39b23](../../evidence/conditions-sets-044.md#c-71a67fc649c39b23) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [状态效果 S-e1e8d22418e3aae6](../../evidence/state_effects-sets-048.md#s-e1e8d22418e3aae6)

### observed_connections-003501

```text
(config-router-scope)# neighbor additional-paths <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 79 `；EOL ` RVA 0x345862C0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6f3b5a2538a5bcb6](../../evidence/conditions-sets-043.md#c-6f3b5a2538a5bcb6) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [状态效果 S-505310b365fd337b](../../evidence/state_effects-sets-018.md#s-505310b365fd337b)

### observed_connections-003530

```text
(config-router-scope)# neighbor advertise additional-paths <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 78 `；EOL ` RVA 0x345869C8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a8c77668b103c2db](../../evidence/conditions-sets-065.md#c-a8c77668b103c2db) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [状态效果 S-815dfd5642a95793](../../evidence/state_effects-sets-027.md#s-815dfd5642a95793)

### observed_connections-003528

```text
(config-router-scope)# neighbor advertise best-external <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 80 `；EOL ` RVA 0x34587078 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b3d49821caf85c5d](../../evidence/conditions-sets-070.md#c-b3d49821caf85c5d) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [状态效果 S-e1e8d22418e3aae6](../../evidence/state_effects-sets-048.md#s-e1e8d22418e3aae6)

### observed_connections-003552

```text
(config-router-scope)# neighbor advertise diverse-path mpath <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 78 `；EOL ` RVA 0x34586D98 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b3d49821caf85c5d](../../evidence/conditions-sets-070.md#c-b3d49821caf85c5d) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [状态效果 S-cc31964cea5b2ea6](../../evidence/state_effects-sets-043.md#s-cc31964cea5b2ea6)

### observed_connections-003512

```text
(config-router-scope)# neighbor advertise-gw-ip-disable <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 88 `；EOL ` RVA 0x3458CF90 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-bd8f0d80ed9d39d0](../../evidence/conditions-sets-073.md#c-bd8f0d80ed9d39d0) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [状态效果 S-e1e8d22418e3aae6](../../evidence/state_effects-sets-048.md#s-e1e8d22418e3aae6)

### observed_connections-003556

```text
(config-router-scope)# neighbor advertise-map <string> non-exist-map <string> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 39 `；EOL ` RVA 0x345893C8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` advertise route-map name；` string ` condition route-map name。

[条件 C-e47b7d4aabc7d555](../../evidence/conditions-sets-088.md#c-e47b7d4aabc7d555) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [参数 P-5f2c7de3c41d51d9](../../evidence/parameters-sets-008.md#p-5f2c7de3c41d51d9) · [状态效果 S-a7045559b9b34bb6](../../evidence/state_effects-sets-035.md#s-a7045559b9b34bb6)

### observed_connections-003489

```text
(config-router-scope)# neighbor advertisement-interval <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 40 `；EOL ` RVA 0x34580E50 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6c4dcc972303683a](../../evidence/conditions-sets-042.md#c-6c4dcc972303683a) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [状态效果 S-e1e8d22418e3aae6](../../evidence/state_effects-sets-048.md#s-e1e8d22418e3aae6)

### observed_connections-003499

```text
(config-router-scope)# neighbor aigp <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 50 `；EOL ` RVA 0x345854E0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4f4764dc6f28474e](../../evidence/conditions-sets-031.md#c-4f4764dc6f28474e) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [状态效果 S-d30d1f53a20d2e37](../../evidence/state_effects-sets-045.md#s-d30d1f53a20d2e37)

### observed_connections-003500

```text
(config-router-scope)# neighbor allow-policy <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 51 `；EOL ` RVA 0x34585F10 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-cf2570e197b03e18](../../evidence/conditions-sets-080.md#c-cf2570e197b03e18) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [状态效果 S-e1e8d22418e3aae6](../../evidence/state_effects-sets-048.md#s-e1e8d22418e3aae6)

### observed_connections-003485

```text
(config-router-scope)# neighbor allowas-in <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 60 `；EOL ` RVA 0x3457FBF0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c54af920b0839981](../../evidence/conditions-sets-076.md#c-c54af920b0839981) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [状态效果 S-e1e8d22418e3aae6](../../evidence/state_effects-sets-048.md#s-e1e8d22418e3aae6)

### observed_connections-003546

```text
(config-router-scope)# neighbor announce rpki state <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 77 `；EOL ` RVA 0x345803D8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1dc66ea11e56c538](../../evidence/conditions-sets-012.md#c-1dc66ea11e56c538) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [状态效果 S-e1e8d22418e3aae6](../../evidence/state_effects-sets-048.md#s-e1e8d22418e3aae6)

### observed_connections-003534

```text
(config-router-scope)# neighbor ao <string> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 22 `；EOL ` RVA 0x3458BFE0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Keychain name。

[条件 C-de06d6b81a9f7b83](../../evidence/conditions-sets-086.md#c-de06d6b81a9f7b83) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [参数 P-cc7ca6702a4f0cdf](../../evidence/parameters-sets-015.md#p-cc7ca6702a4f0cdf) · [状态效果 S-e1e8d22418e3aae6](../../evidence/state_effects-sets-048.md#s-e1e8d22418e3aae6)

### observed_connections-003507

```text
(config-router-scope)# neighbor as-override <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 61 `；EOL ` RVA 0x34589E78 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-096b26117058255b](../../evidence/conditions-sets-004.md#c-096b26117058255b) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [状态效果 S-e1e8d22418e3aae6](../../evidence/state_effects-sets-048.md#s-e1e8d22418e3aae6)

### observed_connections-003557

```text
(config-router-scope)# neighbor capability orf prefix-list send <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 65 `；EOL ` RVA 0x3458A2C0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1367858ee8d414e8](../../evidence/conditions-sets-008.md#c-1367858ee8d414e8) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [状态效果 S-22a53d4fe39c0204](../../evidence/state_effects-sets-008.md#s-22a53d4fe39c0204)

### observed_connections-003509

```text
(config-router-scope)# neighbor cluster-id <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 23 `；EOL ` RVA 0x3458C3A8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9f0f0282d377a356](../../evidence/conditions-sets-062.md#c-9f0f0282d377a356) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [状态效果 S-e1e8d22418e3aae6](../../evidence/state_effects-sets-048.md#s-e1e8d22418e3aae6)

### observed_connections-003494

```text
(config-router-scope)# neighbor default-originate <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 52 `；EOL ` RVA 0x34583910 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-af7bd590c2606ab3](../../evidence/conditions-sets-068.md#c-af7bd590c2606ab3) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [状态效果 S-e1e8d22418e3aae6](../../evidence/state_effects-sets-048.md#s-e1e8d22418e3aae6)

### observed_connections-003503

```text
(config-router-scope)# neighbor description <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 8 `；EOL ` RVA 0x34588860 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b44b419c18aceb96](../../evidence/conditions-sets-070.md#c-b44b419c18aceb96) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [状态效果 S-e1e8d22418e3aae6](../../evidence/state_effects-sets-048.md#s-e1e8d22418e3aae6)

### observed_connections-003483

```text
(config-router-scope)# neighbor disable-connected-check <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 13 `；EOL ` RVA 0x3457EF60 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c517c536bb4b4139](../../evidence/conditions-sets-076.md#c-c517c536bb4b4139) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [状态效果 S-9514524013695198](../../evidence/state_effects-sets-032.md#s-9514524013695198)

### observed_connections-003542

```text
(config-router-scope)# neighbor distribute-list <number:1..199> in <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 45 `；EOL ` RVA 0x3457C0E8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` IP access list number。

[条件 C-4c44359e6d279498](../../evidence/conditions-sets-030.md#c-4c44359e6d279498) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [参数 P-4c0916ea7378a39b](../../evidence/parameters-sets-006.md#p-4c0916ea7378a39b) · [状态效果 S-5a395abade09be60](../../evidence/state_effects-sets-019.md#s-5a395abade09be60)

### observed_connections-003481

```text
(config-router-scope)# neighbor dmzlink-bw <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 63 `；EOL ` RVA 0x3457D9E8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2d9a7b00cd728e9d](../../evidence/conditions-sets-018.md#c-2d9a7b00cd728e9d) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [状态效果 S-d6e1a9c221b9837a](../../evidence/state_effects-sets-046.md#s-d6e1a9c221b9837a)

### observed_connections-003478

```text
(config-router-scope)# neighbor dont-capability-negotiate <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 16 `；EOL ` RVA 0x3457ACA8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0e8d100a511bd871](../../evidence/conditions-sets-006.md#c-0e8d100a511bd871) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [状态效果 S-e1e8d22418e3aae6](../../evidence/state_effects-sets-048.md#s-e1e8d22418e3aae6)

### observed_connections-003516

```text
(config-router-scope)# neighbor dont-capability-negotiate enhanced-refresh <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 18 `；EOL ` RVA 0x3457AC80 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0e8d100a511bd871](../../evidence/conditions-sets-006.md#c-0e8d100a511bd871) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [状态效果 S-e1e8d22418e3aae6](../../evidence/state_effects-sets-048.md#s-e1e8d22418e3aae6)

### observed_connections-003514

```text
(config-router-scope)# neighbor dont-capability-negotiate four-octets-as <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 17 `；EOL ` RVA 0x3457A9D8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0e8d100a511bd871](../../evidence/conditions-sets-006.md#c-0e8d100a511bd871) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [状态效果 S-e1e8d22418e3aae6](../../evidence/state_effects-sets-048.md#s-e1e8d22418e3aae6)

### observed_connections-003493

```text
(config-router-scope)# neighbor ebgp-multihop <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 6 `；EOL ` RVA 0x345834E8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d9a5efc1652eb0c4](../../evidence/conditions-sets-084.md#c-d9a5efc1652eb0c4) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [状态效果 S-dda84ca28f9c0947](../../evidence/state_effects-sets-047.md#s-dda84ca28f9c0947)

### observed_connections-003535

```text
(config-router-scope)# neighbor encap srv6 <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 86 `；EOL ` RVA 0x3458D3B8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2d564b667e88f2d2](../../evidence/conditions-sets-018.md#c-2d564b667e88f2d2) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [状态效果 S-80aaaecad441c00a](../../evidence/state_effects-sets-027.md#s-80aaaecad441c00a)

### observed_connections-003486

```text
(config-router-scope)# neighbor fall-over <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 26 `；EOL ` RVA 0x3457F2B8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-57dd543003616850](../../evidence/conditions-sets-034.md#c-57dd543003616850) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [状态效果 S-23636925118c3c3e](../../evidence/state_effects-sets-008.md#s-23636925118c3c3e)

### observed_connections-003545

```text
(config-router-scope)# neighbor filter-list <number:1..500> in <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 44 `；EOL ` RVA 0x3457CEC8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` AS path access list。

[条件 C-4b0b77b0421abbca](../../evidence/conditions-sets-029.md#c-4b0b77b0421abbca) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [参数 P-48fbd52df0db71e6](../../evidence/parameters-sets-006.md#p-48fbd52df0db71e6) · [状态效果 S-945dd44045a5e8b0](../../evidence/state_effects-sets-031.md#s-945dd44045a5e8b0)

### observed_connections-003477

```text
(config-router-scope)# neighbor force-open-collision <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 15 `；EOL ` RVA 0x3457B238 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ab35ecc1c45caeb5](../../evidence/conditions-sets-066.md#c-ab35ecc1c45caeb5) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [状态效果 S-e1e8d22418e3aae6](../../evidence/state_effects-sets-048.md#s-e1e8d22418e3aae6)

### observed_connections-003537

```text
(config-router-scope)# neighbor ha-mode graceful-restart <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 28 `；EOL ` RVA 0x3458D848 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2004f71c27d50b9b](../../evidence/conditions-sets-012.md#c-2004f71c27d50b9b) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [状态效果 S-e1e8d22418e3aae6](../../evidence/state_effects-sets-048.md#s-e1e8d22418e3aae6)

### observed_connections-003551

```text
(config-router-scope)# neighbor inherit peer-policy <string> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 36 `；EOL ` RVA 0x345874F0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Template name。

[条件 C-40a6db528296e847](../../evidence/conditions-sets-025.md#c-40a6db528296e847) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [参数 P-887f3502f6709295](../../evidence/parameters-sets-011.md#p-887f3502f6709295) · [状态效果 S-e1e8d22418e3aae6](../../evidence/state_effects-sets-048.md#s-e1e8d22418e3aae6)

### observed_connections-003550

```text
(config-router-scope)# neighbor inherit peer-session <string> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 19 `；EOL ` RVA 0x34587808 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Template name。

[条件 C-135c75d3c9efbfc9](../../evidence/conditions-sets-008.md#c-135c75d3c9efbfc9) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [参数 P-059f64d5a28805a5](../../evidence/parameters-sets-001.md#p-059f64d5a28805a5) · [状态效果 S-e1e8d22418e3aae6](../../evidence/state_effects-sets-048.md#s-e1e8d22418e3aae6)

### observed_connections-003496

```text
(config-router-scope)# neighbor inter-as-hybrid <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 72 `；EOL ` RVA 0x34584EC0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-80dd6833efd15ca4](../../evidence/conditions-sets-050.md#c-80dd6833efd15ca4) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [状态效果 S-e1e8d22418e3aae6](../../evidence/state_effects-sets-048.md#s-e1e8d22418e3aae6)

### observed_connections-003506

```text
(config-router-scope)# neighbor internal-vpn-client <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 82 `；EOL ` RVA 0x34589AC0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d330ee30da390f2c](../../evidence/conditions-sets-081.md#c-d330ee30da390f2c) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [状态效果 S-e1e8d22418e3aae6](../../evidence/state_effects-sets-048.md#s-e1e8d22418e3aae6)

### observed_connections-003484

```text
(config-router-scope)# neighbor local-as <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 11 `；EOL ` RVA 0x3457EAE8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-61e44e1c3f0668a0](../../evidence/conditions-sets-038.md#c-61e44e1c3f0668a0) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [状态效果 S-e1e8d22418e3aae6](../../evidence/state_effects-sets-048.md#s-e1e8d22418e3aae6)

### observed_connections-003513

```text
(config-router-scope)# neighbor log-neighbor-changes <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 32 `；EOL ` RVA 0x3458DF28 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-cb290f57335b852e](../../evidence/conditions-sets-078.md#c-cb290f57335b852e) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [状态效果 S-e1e8d22418e3aae6](../../evidence/state_effects-sets-048.md#s-e1e8d22418e3aae6)

### observed_connections-003511

```text
(config-router-scope)# neighbor long-lived-graceful-restart <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 85 `；EOL ` RVA 0x3458C7C8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b46c067af0b7d138](../../evidence/conditions-sets-070.md#c-b46c067af0b7d138) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [状态效果 S-e1e8d22418e3aae6](../../evidence/state_effects-sets-048.md#s-e1e8d22418e3aae6)

### observed_connections-003529

```text
(config-router-scope)# neighbor maximum-prefix <number:1..2147483647> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 59 `；EOL ` RVA 0x34588368 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` maximum no. of prefix limit。

[条件 C-5f87777980f69e27](../../evidence/conditions-sets-037.md#c-5f87777980f69e27) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [参数 P-d83e10c293ccf8b2](../../evidence/parameters-sets-016.md#p-d83e10c293ccf8b2) · [状态效果 S-e1e8d22418e3aae6](../../evidence/state_effects-sets-048.md#s-e1e8d22418e3aae6)

### observed_connections-003491

```text
(config-router-scope)# neighbor next-hop-self <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 42 `；EOL ` RVA 0x345820B8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-15d8cf7262dccfa1](../../evidence/conditions-sets-009.md#c-15d8cf7262dccfa1) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [状态效果 S-e1e8d22418e3aae6](../../evidence/state_effects-sets-048.md#s-e1e8d22418e3aae6)

### observed_connections-003492

```text
(config-router-scope)# neighbor next-hop-unchanged <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 43 `；EOL ` RVA 0x34583178 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b6166aee19308251](../../evidence/conditions-sets-070.md#c-b6166aee19308251) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [状态效果 S-e1e8d22418e3aae6](../../evidence/state_effects-sets-048.md#s-e1e8d22418e3aae6)

### observed_connections-003518

```text
(config-router-scope)# neighbor orf rt-import-list <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 70 `；EOL ` RVA 0x3457CAA8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-446bd6cec94ed0dc](../../evidence/conditions-sets-027.md#c-446bd6cec94ed0dc) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [状态效果 S-427713591a47998b](../../evidence/state_effects-sets-015.md#s-427713591a47998b)

### observed_connections-003479

```text
(config-router-scope)# neighbor override-capability-neg <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 62 `；EOL ` RVA 0x3457BD00 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-438a7c8ccbff46b5](../../evidence/conditions-sets-026.md#c-438a7c8ccbff46b5) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [状态效果 S-e1e8d22418e3aae6](../../evidence/state_effects-sets-048.md#s-e1e8d22418e3aae6)

### observed_connections-003502

```text
(config-router-scope)# neighbor password <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 7 `；EOL ` RVA 0x34587F20 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d0dcfd9b8b2721d5](../../evidence/conditions-sets-080.md#c-d0dcfd9b8b2721d5) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [状态效果 S-e1e8d22418e3aae6](../../evidence/state_effects-sets-048.md#s-e1e8d22418e3aae6)

### observed_connections-003558

```text
(config-router-scope)# neighbor path-attribute treat-as-withdraw <number:1..255> in <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 27 `；EOL ` RVA 0x3458B7C0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` path attribute type。

[条件 C-b01adb5202de0744](../../evidence/conditions-sets-068.md#c-b01adb5202de0744) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [参数 P-0d25b43be8ee618d](../../evidence/parameters-sets-001.md#p-0d25b43be8ee618d) · [状态效果 S-a650c5547ae4d5a9](../../evidence/state_effects-sets-035.md#s-a650c5547ae4d5a9)

### observed_connections-003476

```text
(config-router-scope)# neighbor peer-group <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 10 `；EOL ` RVA 0x3458E8F8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0c96bc8d37906f3e](../../evidence/conditions-sets-005.md#c-0c96bc8d37906f3e) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [状态效果 S-e1e8d22418e3aae6](../../evidence/state_effects-sets-048.md#s-e1e8d22418e3aae6)

### observed_connections-003527

```text
(config-router-scope)# neighbor peer-group <string> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 20 `；EOL ` RVA 0x34587B88 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` peer-group name。

[条件 C-7d774eeb63b1a9a4](../../evidence/conditions-sets-049.md#c-7d774eeb63b1a9a4) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [参数 P-e897810b11a8e17a](../../evidence/parameters-sets-017.md#p-e897810b11a8e17a) · [状态效果 S-e1e8d22418e3aae6](../../evidence/state_effects-sets-048.md#s-e1e8d22418e3aae6)

### observed_connections-003519

```text
(config-router-scope)# neighbor prefix-length-size <number:1..2> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 68 `；EOL ` RVA 0x3457D6A8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Storage size in bytes。

[条件 C-7d3f8a7e598bafbc](../../evidence/conditions-sets-049.md#c-7d3f8a7e598bafbc) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [参数 P-c240d8d2cee28659](../../evidence/parameters-sets-015.md#p-c240d8d2cee28659) · [状态效果 S-e1e8d22418e3aae6](../../evidence/state_effects-sets-048.md#s-e1e8d22418e3aae6)

### observed_connections-003543

```text
(config-router-scope)# neighbor prefix-list <string> in <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 58 `；EOL ` RVA 0x3457C5D0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Name of a prefix list。

[条件 C-09018de0dd43d0af](../../evidence/conditions-sets-004.md#c-09018de0dd43d0af) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [参数 P-acc845f852d79c11](../../evidence/parameters-sets-013.md#p-acc845f852d79c11) · [状态效果 S-23d826ddd294bcec](../../evidence/state_effects-sets-008.md#s-23d826ddd294bcec)

### observed_connections-003482

```text
(config-router-scope)# neighbor remote-as <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 3 `；EOL ` RVA 0x3457E0D0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-03ce645ffc214ad1](../../evidence/conditions-sets-002.md#c-03ce645ffc214ad1) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [状态效果 S-e1e8d22418e3aae6](../../evidence/state_effects-sets-048.md#s-e1e8d22418e3aae6)

### observed_connections-003495

```text
(config-router-scope)# neighbor remove-private-as <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 55 `；EOL ` RVA 0x34584688 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2cd9da7f634b949a](../../evidence/conditions-sets-018.md#c-2cd9da7f634b949a) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [状态效果 S-e1e8d22418e3aae6](../../evidence/state_effects-sets-048.md#s-e1e8d22418e3aae6)

### observed_connections-003526

```text
(config-router-scope)# neighbor remove-private-as all <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 56 `；EOL ` RVA 0x345846F0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2ee1f771cc9907ed](../../evidence/conditions-sets-018.md#c-2ee1f771cc9907ed) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [状态效果 S-e1e8d22418e3aae6](../../evidence/state_effects-sets-048.md#s-e1e8d22418e3aae6)

### observed_connections-003549

```text
(config-router-scope)# neighbor remove-private-as all replace-as <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 57 `；EOL ` RVA 0x345846C8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2ee1f771cc9907ed](../../evidence/conditions-sets-018.md#c-2ee1f771cc9907ed) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [状态效果 S-e1e8d22418e3aae6](../../evidence/state_effects-sets-048.md#s-e1e8d22418e3aae6)

### observed_connections-003544

```text
(config-router-scope)# neighbor route-map <string> in <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 47 `；EOL ` RVA 0x3457D2B8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Name of route map。

[条件 C-b722ff55f1572a4c](../../evidence/conditions-sets-071.md#c-b722ff55f1572a4c) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [参数 P-1e2d92be928155a3](../../evidence/parameters-sets-003.md#p-1e2d92be928155a3) · [状态效果 S-d1411feb798d2289](../../evidence/state_effects-sets-044.md#s-d1411feb798d2289)

### observed_connections-003497

```text
(config-router-scope)# neighbor route-reflector-client <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 49 `；EOL ` RVA 0x34585BD8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e55b3b620b12a1e9](../../evidence/conditions-sets-088.md#c-e55b3b620b12a1e9) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [状态效果 S-e1e8d22418e3aae6](../../evidence/state_effects-sets-048.md#s-e1e8d22418e3aae6)

### observed_connections-003488

```text
(config-router-scope)# neighbor send-community <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 46 `；EOL ` RVA 0x345815E8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-72ec10de26c315b1](../../evidence/conditions-sets-044.md#c-72ec10de26c315b1) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [状态效果 S-e1e8d22418e3aae6](../../evidence/state_effects-sets-048.md#s-e1e8d22418e3aae6)

### observed_connections-003508

```text
(config-router-scope)# neighbor send-label <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 64 `；EOL ` RVA 0x3458A7C0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-06c4d444be189a37](../../evidence/conditions-sets-003.md#c-06c4d444be189a37) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [状态效果 S-e1e8d22418e3aae6](../../evidence/state_effects-sets-048.md#s-e1e8d22418e3aae6)

### observed_connections-003490

```text
(config-router-scope)# neighbor shutdown <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 5 `；EOL ` RVA 0x34581A88 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0aa0b6b76a0471bd](../../evidence/conditions-sets-004.md#c-0aa0b6b76a0471bd) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [状态效果 S-e1e8d22418e3aae6](../../evidence/state_effects-sets-048.md#s-e1e8d22418e3aae6)

### observed_connections-003521

```text
(config-router-scope)# neighbor slow-peer detection <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 74 `；EOL ` RVA 0x34582B38 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-687d4cfb7a8bdfe1](../../evidence/conditions-sets-040.md#c-687d4cfb7a8bdfe1) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [状态效果 S-e1e8d22418e3aae6](../../evidence/state_effects-sets-048.md#s-e1e8d22418e3aae6)

### observed_connections-003522

```text
(config-router-scope)# neighbor slow-peer detection threshold <number:120..3600> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 74 `；EOL ` RVA 0x34582B60 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Threshold value (seconds)。

[条件 C-419ec353a633f2f7](../../evidence/conditions-sets-026.md#c-419ec353a633f2f7) · [缺口 G-27ab7bea4cc5631e](../../evidence/gaps-sets-002.md#g-27ab7bea4cc5631e) · [参数 P-518da0f0fe1b1f01](../../evidence/parameters-sets-007.md#p-518da0f0fe1b1f01) · [状态效果 S-e1e8d22418e3aae6](../../evidence/state_effects-sets-048.md#s-e1e8d22418e3aae6)

### observed_connections-003548

```text
(config-router-scope)# neighbor slow-peer split-update-group dynamic <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 75 `；EOL ` RVA 0x345827C0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e605b5913d26c66f](../../evidence/conditions-sets-089.md#c-e605b5913d26c66f) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [状态效果 S-e1e8d22418e3aae6](../../evidence/state_effects-sets-048.md#s-e1e8d22418e3aae6)

### observed_connections-003547

```text
(config-router-scope)# neighbor slow-peer split-update-group static <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 73 `；EOL ` RVA 0x345824B0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-db9f372407dd4030](../../evidence/conditions-sets-085.md#c-db9f372407dd4030) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [状态效果 S-e1e8d22418e3aae6](../../evidence/state_effects-sets-048.md#s-e1e8d22418e3aae6)

### observed_connections-003523

```text
(config-router-scope)# neighbor soft-reconfiguration inbound <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 54 `；EOL ` RVA 0x34583CA8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d2b790e297afdceb](../../evidence/conditions-sets-081.md#c-d2b790e297afdceb) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [状态效果 S-e1e8d22418e3aae6](../../evidence/state_effects-sets-048.md#s-e1e8d22418e3aae6)

### observed_connections-003564

```text
(config-router-scope)# neighbor soo <?bgp_extcomm_action@555589ad3f68> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 69 `；EOL ` RVA 0x3457FFB0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-75dfcc16352d14d9](../../evidence/conditions-sets-046.md#c-75dfcc16352d14d9) · [缺口 G-f4422813f5a4d98a](../../evidence/gaps-sets-008.md#g-f4422813f5a4d98a) · [状态效果 S-4c4b463be8b10713](../../evidence/state_effects-sets-017.md#s-4c4b463be8b10713)

### observed_connections-003536

```text
(config-router-scope)# neighbor suppress-signaling-protocol ldp <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 81 `；EOL ` RVA 0x3458DBE8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-51e927a605368567](../../evidence/conditions-sets-032.md#c-51e927a605368567) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [状态效果 S-e1e8d22418e3aae6](../../evidence/state_effects-sets-048.md#s-e1e8d22418e3aae6)

### observed_connections-003510

```text
(config-router-scope)# neighbor suppress-sr <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 87 `；EOL ` RVA 0x3458CC58 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0d5acb73016793f6](../../evidence/conditions-sets-005.md#c-0d5acb73016793f6) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [状态效果 S-e1e8d22418e3aae6](../../evidence/state_effects-sets-048.md#s-e1e8d22418e3aae6)

### observed_connections-003505

```text
(config-router-scope)# neighbor timers <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 9 `；EOL ` RVA 0x34588EF8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-171b33bf75efb204](../../evidence/conditions-sets-009.md#c-171b33bf75efb204) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [状态效果 S-e1e8d22418e3aae6](../../evidence/state_effects-sets-048.md#s-e1e8d22418e3aae6)

### observed_connections-003515

```text
(config-router-scope)# neighbor translate-topology <number:1..4095> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 67 `；EOL ` RVA 0x3457A698 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Topology id。

[条件 C-54d8a0591e01d8ed](../../evidence/conditions-sets-033.md#c-54d8a0591e01d8ed) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [参数 P-f462fbbe9a890828](../../evidence/parameters-sets-018.md#p-f462fbbe9a890828) · [状态效果 S-e1e8d22418e3aae6](../../evidence/state_effects-sets-048.md#s-e1e8d22418e3aae6)

### observed_connections-003480

```text
(config-router-scope)# neighbor translate-update <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 66 `；EOL ` RVA 0x3457B698 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-fa77bb18f7ecf37e](../../evidence/conditions-sets-097.md#c-fa77bb18f7ecf37e) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [状态效果 S-5e1f0726fd1a4748](../../evidence/state_effects-sets-020.md#s-5e1f0726fd1a4748)

### observed_connections-003533

```text
(config-router-scope)# neighbor transport multi-session <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 25 `；EOL ` RVA 0x3458B238 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-80c1748eeb55f0eb](../../evidence/conditions-sets-050.md#c-80c1748eeb55f0eb) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [状态效果 S-4d0dbdb89a049d25](../../evidence/state_effects-sets-017.md#s-4d0dbdb89a049d25)

### observed_connections-003532

```text
(config-router-scope)# neighbor transport path-mtu-discovery <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 24 `；EOL ` RVA 0x3458AE90 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-80c1748eeb55f0eb](../../evidence/conditions-sets-050.md#c-80c1748eeb55f0eb) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [状态效果 S-fb02b85e82bb7c09](../../evidence/state_effects-sets-053.md#s-fb02b85e82bb7c09)

### observed_connections-003553

```text
(config-router-scope)# neighbor ttl-security hops <number:1..254> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 21 `；EOL ` RVA 0x3458BBC8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` maximum number of hops。

[条件 C-9ea8e9c06db98259](../../evidence/conditions-sets-061.md#c-9ea8e9c06db98259) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [参数 P-9374840c562b47ef](../../evidence/parameters-sets-011.md#p-9374840c562b47ef) · [状态效果 S-e1e8d22418e3aae6](../../evidence/state_effects-sets-048.md#s-e1e8d22418e3aae6)

### observed_connections-003520

```text
(config-router-scope)# neighbor unsuppress-map <string> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 53 `；EOL ` RVA 0x3457DD70 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Name of route map。

[条件 C-927d4647589a91e2](../../evidence/conditions-sets-056.md#c-927d4647589a91e2) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [参数 P-42ea016af4dd7d0a](../../evidence/parameters-sets-006.md#p-42ea016af4dd7d0a) · [状态效果 S-e1e8d22418e3aae6](../../evidence/state_effects-sets-048.md#s-e1e8d22418e3aae6)

### observed_connections-003559

```text
(config-router-scope)# neighbor update in labeled-unicast unique <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 33 `；EOL ` RVA 0x3458E348 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3202cd190cc5adfc](../../evidence/conditions-sets-020.md#c-3202cd190cc5adfc) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [状态效果 S-1f392450a1915f73](../../evidence/state_effects-sets-007.md#s-1f392450a1915f73)

### observed_connections-003565

```text
(config-router-scope)# neighbor update-source <interface> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 4 `；EOL ` RVA 0x34581270 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-caa71659690b3284](../../evidence/conditions-sets-078.md#c-caa71659690b3284) · [缺口 G-34b42f8191f3bfea](../../evidence/gaps-sets-002.md#g-34b42f8191f3bfea) · [参数 P-ea7a5d8d55e4d0b1](../../evidence/parameters-sets-018.md#p-ea7a5d8d55e4d0b1) · [状态效果 S-e1e8d22418e3aae6](../../evidence/state_effects-sets-048.md#s-e1e8d22418e3aae6)

### observed_connections-003531

```text
(config-router-scope)# neighbor use nexthop-attribute <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 37 `；EOL ` RVA 0x34589780 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c5c8ca21ed1875df](../../evidence/conditions-sets-076.md#c-c5c8ca21ed1875df) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [状态效果 S-e1e8d22418e3aae6](../../evidence/state_effects-sets-048.md#s-e1e8d22418e3aae6)

### observed_connections-003524

```text
(config-router-scope)# neighbor validation off <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 83 `；EOL ` RVA 0x34584028 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-302695286c284e5f](../../evidence/conditions-sets-019.md#c-302695286c284e5f) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [状态效果 S-e1e8d22418e3aae6](../../evidence/state_effects-sets-048.md#s-e1e8d22418e3aae6)

### observed_connections-003525

```text
(config-router-scope)# neighbor validation redirect-off <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 84 `；EOL ` RVA 0x345842D0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-302695286c284e5f](../../evidence/conditions-sets-019.md#c-302695286c284e5f) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [状态效果 S-e1e8d22418e3aae6](../../evidence/state_effects-sets-048.md#s-e1e8d22418e3aae6)

### observed_connections-003468

```text
(config-router-scope)# neighbor version <number:4..4> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 2 `；EOL ` RVA 0x34580680 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Neighbor's BGP version。

[条件 C-0118468010e17465](../../evidence/conditions-sets-001.md#c-0118468010e17465) · [缺口 G-35f47de2b84a58df](../../evidence/gaps-sets-002.md#g-35f47de2b84a58df) · [参数 P-cc4a2c72b3e21596](../../evidence/parameters-sets-015.md#p-cc4a2c72b3e21596) · [状态效果 S-e1e8d22418e3aae6](../../evidence/state_effects-sets-048.md#s-e1e8d22418e3aae6)

### observed_connections-003487

```text
(config-router-scope)# neighbor weight <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 41 `；EOL ` RVA 0x34580A78 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-87f9963274d6cf57](../../evidence/conditions-sets-053.md#c-87f9963274d6cf57) · [缺口 G-51740766a8ebfd1e](../../evidence/gaps-sets-003.md#g-51740766a8ebfd1e) · [状态效果 S-e1e8d22418e3aae6](../../evidence/state_effects-sets-048.md#s-e1e8d22418e3aae6)

### observed_connections-003474

```text
(config-router-scope)# network <address> <cr>
```

Handler ` RVA 0xF190B70 `；selector ` 0 `；EOL ` RVA 0x34579688 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` NSAP prefix。

[条件 C-d1b12bc3f0cd12f3](../../evidence/conditions-sets-081.md#c-d1b12bc3f0cd12f3) · [缺口 G-526012ff1e06c59b](../../evidence/gaps-sets-003.md#g-526012ff1e06c59b) · [参数 P-88eab8f6d48129e0](../../evidence/parameters-sets-011.md#p-88eab8f6d48129e0) · [状态效果 S-51cb71ec4326ef7b](../../evidence/state_effects-sets-018.md#s-51cb71ec4326ef7b)

### observed_connections-003563

```text
(config-router-scope)# network <address> <cr>
```

Handler ` RVA 0xE1E04C0 `；selector ` 0 `；EOL ` RVA 0x3455F788 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Network number。

[条件 C-654691e5c608b26f](../../evidence/conditions-sets-039.md#c-654691e5c608b26f) · [缺口 G-28009e3f6dbb72c8](../../evidence/gaps-sets-002.md#g-28009e3f6dbb72c8) · [参数 P-b92920a6419366c8](../../evidence/parameters-sets-014.md#p-b92920a6419366c8) · [状态效果 S-959dc04ca201b855](../../evidence/state_effects-sets-032.md#s-959dc04ca201b855)

### observed_connections-003361

```text
(config-router-scope)# no aggregate-address <address> <address> <cr>
```

Handler ` RVA 0xF1B7BE0 `；selector ` 0 `；EOL ` RVA 0x3457A030 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` Aggregate address；` address ` Aggregate mask。

[条件 C-4eb836e3175cf5bd](../../evidence/conditions-sets-031.md#c-4eb836e3175cf5bd) · [参数 P-034bf7990709c321](../../evidence/parameters-sets-001.md#p-034bf7990709c321) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003173

```text
(config-router-scope)# no auto-summary <cr>
```

Handler ` RVA 0xE1FA6B0 `；selector ` 0 `；EOL ` RVA 0x34563B88 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-fe8af09d9c1d13be](../../evidence/conditions-sets-098.md#c-fe8af09d9c1d13be) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003348

```text
(config-router-scope)# no bgp additional-paths install <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 69 `；EOL ` RVA 0x34571888 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c626df2c5a490a40](../../evidence/conditions-sets-076.md#c-c626df2c5a490a40) · [状态效果 S-b64fb0353e9df962](../../evidence/state_effects-sets-039.md#s-b64fb0353e9df962)

### observed_connections-003357

```text
(config-router-scope)# no bgp additional-paths select <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 71 `；EOL ` RVA 0x34571530 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5f537ef68ce3cb25](../../evidence/conditions-sets-037.md#c-5f537ef68ce3cb25) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003233

```text
(config-router-scope)# no bgp advertise-best-external <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 70 `；EOL ` RVA 0x345726D8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5ee23059aaf8eb3a](../../evidence/conditions-sets-037.md#c-5ee23059aaf8eb3a) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003289

```text
(config-router-scope)# no bgp advertisement startup-delay <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 95 `；EOL ` RVA 0x3456A548 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f7c142cf6532b5fb](../../evidence/conditions-sets-096.md#c-f7c142cf6532b5fb) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003358

```text
(config-router-scope)# no bgp aggregate-timer <number:6..60> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 58 `；EOL ` RVA 0x34578728 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Timer interval。

[条件 C-9828edb5d90b4a4a](../../evidence/conditions-sets-059.md#c-9828edb5d90b4a4a) · [参数 P-b1318a7e59a386fd](../../evidence/parameters-sets-013.md#p-b1318a7e59a386fd) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003313

```text
(config-router-scope)# no bgp aigp-rib-metric <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 91 `；EOL ` RVA 0x3456EFC8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e398f2ee0aabd351](../../evidence/conditions-sets-088.md#c-e398f2ee0aabd351) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003222

```text
(config-router-scope)# no bgp always-compare-med <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 5 `；EOL ` RVA 0x34565E30 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f2d18c8b4e477c8c](../../evidence/conditions-sets-094.md#c-f2d18c8b4e477c8c) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003335

```text
(config-router-scope)# no bgp asnotation dot <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 64 `；EOL ` RVA 0x34566140 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f2d18c8b4e477c8c](../../evidence/conditions-sets-094.md#c-f2d18c8b4e477c8c) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003444

```text
(config-router-scope)# no bgp bestpath aigp ignore <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 43 `；EOL ` RVA 0x3456DCF0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-af1a55da7d13e1c4](../../evidence/conditions-sets-068.md#c-af1a55da7d13e1c4) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003437

```text
(config-router-scope)# no bgp bestpath as-path ignore <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 17 `；EOL ` RVA 0x3456D460 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e398f2ee0aabd351](../../evidence/conditions-sets-088.md#c-e398f2ee0aabd351) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003439

```text
(config-router-scope)# no bgp bestpath as-path multipath-relax <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 51 `；EOL ` RVA 0x3456D708 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e398f2ee0aabd351](../../evidence/conditions-sets-088.md#c-e398f2ee0aabd351) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003391

```text
(config-router-scope)# no bgp bestpath compare-routerid <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 24 `；EOL ` RVA 0x3456D9A0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e398f2ee0aabd351](../../evidence/conditions-sets-088.md#c-e398f2ee0aabd351) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003443

```text
(config-router-scope)# no bgp bestpath cost-community ignore <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 41 `；EOL ` RVA 0x3456DFC8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e398f2ee0aabd351](../../evidence/conditions-sets-088.md#c-e398f2ee0aabd351) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003404

```text
(config-router-scope)# no bgp bestpath igp-metric ignore <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 42 `；EOL ` RVA 0x34571DB8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-96e540aecb31c83c](../../evidence/conditions-sets-058.md#c-96e540aecb31c83c) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003440

```text
(config-router-scope)# no bgp bestpath med missing-as-worst <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 18 `；EOL ` RVA 0x3456D150 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e398f2ee0aabd351](../../evidence/conditions-sets-088.md#c-e398f2ee0aabd351) · [状态效果 S-fb45e1e7799a124b](../../evidence/state_effects-sets-053.md#s-fb45e1e7799a124b)

### observed_connections-003410

```text
(config-router-scope)# no bgp bestpath prefix-validate allow-invalid <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 78 `；EOL ` RVA 0x345720C8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-3a39bc8175d21cd0](../../evidence/conditions-sets-023.md#c-3a39bc8175d21cd0) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003412

```text
(config-router-scope)# no bgp bestpath prefix-validate disable <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 77 `；EOL ` RVA 0x34572370 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-3a39bc8175d21cd0](../../evidence/conditions-sets-023.md#c-3a39bc8175d21cd0) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003353

```text
(config-router-scope)# no bgp client-to-client reflection <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 9 `；EOL ` RVA 0x34566FD0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7b5c81f0eb8f2c77](../../evidence/conditions-sets-048.md#c-7b5c81f0eb8f2c77) · [状态效果 S-2c77d6f8bf44cd82](../../evidence/state_effects-sets-010.md#s-2c77d6f8bf44cd82)

### observed_connections-003248

```text
(config-router-scope)# no bgp cluster-id <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 7 `；EOL ` RVA 0x34566B98 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-18e0dd9b18272596](../../evidence/conditions-sets-010.md#c-18e0dd9b18272596) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003257

```text
(config-router-scope)# no bgp consistency-checker <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 3 `；EOL ` RVA 0x34566518 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7b6eb40e7b154da7](../../evidence/conditions-sets-048.md#c-7b6eb40e7b154da7) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003223

```text
(config-router-scope)# no bgp dampening <cr>
```

Handler ` RVA 0xF1B85B0 `；selector ` 0 `；EOL ` RVA 0x34570950 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-3cf90267394f7ae1](../../evidence/conditions-sets-024.md#c-3cf90267394f7ae1) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003405

```text
(config-router-scope)# no bgp default inter-as-hybrid advertise-source-routes <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 57 `；EOL ` RVA 0x3456FF88 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-6db1be956b0c537b](../../evidence/conditions-sets-042.md#c-6db1be956b0c537b) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003326

```text
(config-router-scope)# no bgp default ipv4-unicast <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 19 `；EOL ` RVA 0x3456F6E0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b70918c03dee8921](../../evidence/conditions-sets-071.md#c-b70918c03dee8921) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003328

```text
(config-router-scope)# no bgp default ipv6-nexthop <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 75 `；EOL ` RVA 0x3456F9D8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8c098b49402f3cfe](../../evidence/conditions-sets-054.md#c-8c098b49402f3cfe) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003227

```text
(config-router-scope)# no bgp default local-preference <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 0 `；EOL ` RVA 0x3456FC68 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f27a7ecd86b59dda](../../evidence/conditions-sets-094.md#c-f27a7ecd86b59dda) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003399

```text
(config-router-scope)# no bgp default route-target filter <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 25 `；EOL ` RVA 0x345702F0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-6e88b262d39af1db](../../evidence/conditions-sets-043.md#c-6e88b262d39af1db) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003400

```text
(config-router-scope)# no bgp default route-target filter <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 25 `；EOL ` RVA 0x34570590 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-dcc3a1ccdaf9a9a8](../../evidence/conditions-sets-085.md#c-dcc3a1ccdaf9a9a8) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003276

```text
(config-router-scope)# no bgp deterministic-med <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 10 `；EOL ` RVA 0x34568650 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f2d18c8b4e477c8c](../../evidence/conditions-sets-094.md#c-f2d18c8b4e477c8c) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003247

```text
(config-router-scope)# no bgp dmzlink-bw <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 31 `；EOL ` RVA 0x34573C88 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c52df1d2f09c863e](../../evidence/conditions-sets-076.md#c-c52df1d2f09c863e) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003183

```text
(config-router-scope)# no bgp dynamic-med-interval <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 21 `；EOL ` RVA 0x34568678 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5cc28ec88c2bdc5f](../../evidence/conditions-sets-036.md#c-5cc28ec88c2bdc5f) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003253

```text
(config-router-scope)# no bgp enforce-first-as <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 20 `；EOL ` RVA 0x34567880 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f2d18c8b4e477c8c](../../evidence/conditions-sets-094.md#c-f2d18c8b4e477c8c) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003291

```text
(config-router-scope)# no bgp enhanced-error <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 82 `；EOL ` RVA 0x3456A2C0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-030d73460ed10600](../../evidence/conditions-sets-002.md#c-030d73460ed10600) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003209

```text
(config-router-scope)# no bgp fast-external-fallover <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 1 `；EOL ` RVA 0x34565568 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f2d18c8b4e477c8c](../../evidence/conditions-sets-094.md#c-f2d18c8b4e477c8c) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003301

```text
(config-router-scope)# no bgp graceful-restart <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 35 `；EOL ` RVA 0x3456B130 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f2d18c8b4e477c8c](../../evidence/conditions-sets-094.md#c-f2d18c8b4e477c8c) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003295

```text
(config-router-scope)# no bgp graceful-restart restart-time <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 36 `；EOL ` RVA 0x3456AB00 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-43e2e64c73e0b6ec](../../evidence/conditions-sets-027.md#c-43e2e64c73e0b6ec) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003297

```text
(config-router-scope)# no bgp graceful-restart stalepath-time <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 37 `；EOL ` RVA 0x3456AB68 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-717bb31629fa6281](../../evidence/conditions-sets-044.md#c-717bb31629fa6281) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003461

```text
(config-router-scope)# no bgp graceful-shutdown all vrfs activate <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 79 `；EOL ` RVA 0x3456B598 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f71ec471c4706ed6](../../evidence/conditions-sets-095.md#c-f71ec471c4706ed6) · [状态效果 S-ff73e9fe667aa062](../../evidence/state_effects-sets-054.md#s-ff73e9fe667aa062)

### observed_connections-003459

```text
(config-router-scope)# no bgp inject-map <string> exist-map <string> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 32 `；EOL ` RVA 0x34575800 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` route-map name；` string ` route-map name。

[条件 C-ef65e2591e463555](../../evidence/conditions-sets-092.md#c-ef65e2591e463555) · [参数 P-15b069a9948617b7](../../evidence/parameters-sets-002.md#p-15b069a9948617b7) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003398

```text
(config-router-scope)# no bgp label-allocation-batch <number:0..4294967295> <number:0..4294967295> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 53 `；EOL ` RVA 0x345658F8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Timer value in milliseconds；` unsigned_number ` Batch Size。

[条件 C-f2d18c8b4e477c8c](../../evidence/conditions-sets-094.md#c-f2d18c8b4e477c8c) · [参数 P-67d56dc38a8352d0](../../evidence/parameters-sets-008.md#p-67d56dc38a8352d0) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003421

```text
(config-router-scope)# no bgp listen block <address> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 93 `；EOL ` RVA 0x34573698 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` IPv4 Dynamic Peering Address。

[条件 C-9bc5921baff5d9a8](../../evidence/conditions-sets-060.md#c-9bc5921baff5d9a8) · [参数 P-dd46f1481a83f05c](../../evidence/parameters-sets-017.md#p-dd46f1481a83f05c) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003434

```text
(config-router-scope)# no bgp listen block <address> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 93 `；EOL ` RVA 0x345695F8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` IPv4 Dynamic Peering Address。

[条件 C-141f60943613848c](../../evidence/conditions-sets-008.md#c-141f60943613848c) · [参数 P-6ed5db196fb7f6a7](../../evidence/parameters-sets-009.md#p-6ed5db196fb7f6a7) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003263

```text
(config-router-scope)# no bgp listen limit <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 61 `；EOL ` RVA 0x345735E0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-37c1185f48abc32a](../../evidence/conditions-sets-022.md#c-37c1185f48abc32a) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003292

```text
(config-router-scope)# no bgp listen limit <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 61 `；EOL ` RVA 0x34569518 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad0cd13cea4c0d57](../../evidence/conditions-sets-067.md#c-ad0cd13cea4c0d57) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003375

```text
(config-router-scope)# no bgp listen persistent <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 94 `；EOL ` RVA 0x34569930 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-141f60943613848c](../../evidence/conditions-sets-008.md#c-141f60943613848c) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003260

```text
(config-router-scope)# no bgp log-neighbor-changes <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 11 `；EOL ` RVA 0x34567B28 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f2d18c8b4e477c8c](../../evidence/conditions-sets-094.md#c-f2d18c8b4e477c8c) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003319

```text
(config-router-scope)# no bgp maxas-limit <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 26 `；EOL ` RVA 0x3456ED40 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-75ee04bc3ec2ee46](../../evidence/conditions-sets-046.md#c-75ee04bc3ec2ee46) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003308

```text
(config-router-scope)# no bgp maxcommunity-limit <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 27 `；EOL ` RVA 0x3456E350 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-57db4561f177392e](../../evidence/conditions-sets-034.md#c-57db4561f177392e) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003315

```text
(config-router-scope)# no bgp maxextcommunity-limit <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 29 `；EOL ` RVA 0x3456E9F0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-2313e771b881e950](../../evidence/conditions-sets-014.md#c-2313e771b881e950) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003311

```text
(config-router-scope)# no bgp maxlargecommunity-limit <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 28 `；EOL ` RVA 0x3456E6A0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-3af641b752e4c446](../../evidence/conditions-sets-023.md#c-3af641b752e4c446) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003286

```text
(config-router-scope)# no bgp mpls-local-label <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 81 `；EOL ` RVA 0x34575B78 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b0bc0d7b5a3192d6](../../evidence/conditions-sets-068.md#c-b0bc0d7b5a3192d6) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003425

```text
(config-router-scope)# no bgp nexthop route-map <string> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 56 `；EOL ` RVA 0x345743F0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` route-map name。

[条件 C-0cf276f0d58f258f](../../evidence/conditions-sets-005.md#c-0cf276f0d58f258f) · [参数 P-00cff5a326a32144](../../evidence/parameters-sets-001.md#p-00cff5a326a32144) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003369

```text
(config-router-scope)# no bgp nexthop trigger critical-delay <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 48 `；EOL ` RVA 0x34574958 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-26459da32ebaee08](../../evidence/conditions-sets-015.md#c-26459da32ebaee08) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003364

```text
(config-router-scope)# no bgp nexthop trigger delay <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 47 `；EOL ` RVA 0x345746D8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d3544264df4a03f0](../../evidence/conditions-sets-081.md#c-d3544264df4a03f0) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003420

```text
(config-router-scope)# no bgp nexthop trigger enable <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 49 `；EOL ` RVA 0x345746B0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-cb9c5b4e371e2105](../../evidence/conditions-sets-078.md#c-cb9c5b4e371e2105) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003432

```text
(config-router-scope)# no bgp nopeerup-delay cold-boot <number:1..3600> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 74 `；EOL ` RVA 0x34569F58 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Delay in seconds。

[条件 C-c4108752facdd754](../../evidence/conditions-sets-076.md#c-c4108752facdd754) · [参数 P-1acf5679fb97f07b](../../evidence/parameters-sets-003.md#p-1acf5679fb97f07b) · [状态效果 S-b939bf25c3f52eed](../../evidence/state_effects-sets-039.md#s-b939bf25c3f52eed)

### observed_connections-003342

```text
(config-router-scope)# no bgp recursion host <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 72 `；EOL ` RVA 0x34572A50 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-617372ad7b2daf22](../../evidence/conditions-sets-038.md#c-617372ad7b2daf22) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003234

```text
(config-router-scope)# no bgp redistribute-internal <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 2 `；EOL ` RVA 0x34576D78 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-98868e8ea2f0429e](../../evidence/conditions-sets-059.md#c-98868e8ea2f0429e) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003385

```text
(config-router-scope)# no bgp refresh max-eor-time <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 16 `；EOL ` RVA 0x3456C328 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-75c022aa592978c0](../../evidence/conditions-sets-046.md#c-75c022aa592978c0) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003380

```text
(config-router-scope)# no bgp refresh stalepath-time <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 15 `；EOL ` RVA 0x3456BFB8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5170b614581c791b](../../evidence/conditions-sets-032.md#c-5170b614581c791b) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003381

```text
(config-router-scope)# no bgp regexp deterministic <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 44 `；EOL ` RVA 0x3456CD40 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e398f2ee0aabd351](../../evidence/conditions-sets-088.md#c-e398f2ee0aabd351) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003343

```text
(config-router-scope)# no bgp route-map priority <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 59 `；EOL ` RVA 0x34577F08 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a6eef08207e8589c](../../evidence/conditions-sets-064.md#c-a6eef08207e8589c) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003217

```text
(config-router-scope)# no bgp route-map-cache <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 34 `；EOL ` RVA 0x34565B80 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f2d18c8b4e477c8c](../../evidence/conditions-sets-094.md#c-f2d18c8b4e477c8c) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003226

```text
(config-router-scope)# no bgp router-id <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 4 `；EOL ` RVA 0x34564F38 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-2ec83672913c6341](../../evidence/conditions-sets-018.md#c-2ec83672913c6341) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003266

```text
(config-router-scope)# no bgp router-id <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 4 `；EOL ` RVA 0x34573100 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-308cac2e7f2f69de](../../evidence/conditions-sets-019.md#c-308cac2e7f2f69de) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003465

```text
(config-router-scope)# no bgp rpki server tcp <address> port <number:1..65535> refresh <number:1..65535> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 76 `；EOL ` RVA 0x34578D20 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` IPv6 address of RPKI cache server；` unsigned_number ` Port number；` unsigned_number ` Refresh time in seconds。

[条件 C-de4a98e22dc35703](../../evidence/conditions-sets-086.md#c-de4a98e22dc35703) · [参数 P-51d371163df6fb34](../../evidence/parameters-sets-007.md#p-51d371163df6fb34) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003280

```text
(config-router-scope)# no bgp rr-group <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 23 `；EOL ` RVA 0x34575398 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c472063c502901ea](../../evidence/conditions-sets-076.md#c-c472063c502901ea) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003321

```text
(config-router-scope)# no bgp safe-ebgp-policy <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 92 `；EOL ` RVA 0x3456F2D8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b3c1a42a14d9bf4b](../../evidence/conditions-sets-070.md#c-b3c1a42a14d9bf4b) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003367

```text
(config-router-scope)# no bgp scan-time <number:5..60> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 22 `；EOL ` RVA 0x34575028 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Scanner interval (seconds)。

[条件 C-d54975684e7d66b8](../../evidence/conditions-sets-082.md#c-d54975684e7d66b8) · [参数 P-4ac08f37d767e2ab](../../evidence/parameters-sets-006.md#p-4ac08f37d767e2ab) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003344

```text
(config-router-scope)# no bgp slow-peer detection <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 67 `；EOL ` RVA 0x34576048 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0414ef46a05b0e07](../../evidence/conditions-sets-002.md#c-0414ef46a05b0e07) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003413

```text
(config-router-scope)# no bgp slow-peer split-update-group dynamic <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 68 `；EOL ` RVA 0x34576618 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a1db30d5c39cfaa8](../../evidence/conditions-sets-062.md#c-a1db30d5c39cfaa8) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003428

```text
(config-router-scope)# no bgp snmp traps add-type <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 90 `；EOL ` RVA 0x34568C40 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f2d18c8b4e477c8c](../../evidence/conditions-sets-094.md#c-f2d18c8b4e477c8c) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003261

```text
(config-router-scope)# no bgp soft-reconfig-backup <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 52 `；EOL ` RVA 0x34573FD8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-adf57b5967c3abb1](../../evidence/conditions-sets-067.md#c-adf57b5967c3abb1) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003457

```text
(config-router-scope)# no bgp sourced-paths per-net isis all <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 89 `；EOL ` RVA 0x34577B88 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d8d7c49542b93b9c](../../evidence/conditions-sets-083.md#c-d8d7c49542b93b9c) · [状态效果 S-46262a636a0e3ef5](../../evidence/state_effects-sets-015.md#s-46262a636a0e3ef5)

### observed_connections-003453

```text
(config-router-scope)# no bgp sourced-paths per-net ospf all <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 87 `；EOL ` RVA 0x34577528 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d8d7c49542b93b9c](../../evidence/conditions-sets-083.md#c-d8d7c49542b93b9c) · [状态效果 S-89733ff2935bda0a](../../evidence/state_effects-sets-029.md#s-89733ff2935bda0a)

### observed_connections-003455

```text
(config-router-scope)# no bgp sourced-paths per-net ospfv3 all <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 88 `；EOL ` RVA 0x34577870 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d8d7c49542b93b9c](../../evidence/conditions-sets-083.md#c-d8d7c49542b93b9c) · [状态效果 S-1cda9c9a00c6950b](../../evidence/state_effects-sets-007.md#s-1cda9c9a00c6950b)

### observed_connections-003449

```text
(config-router-scope)# no bgp sourced-paths per-net static all <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 86 `；EOL ` RVA 0x345771E0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d8d7c49542b93b9c](../../evidence/conditions-sets-083.md#c-d8d7c49542b93b9c) · [状态效果 S-99260ce7577b734c](../../evidence/state_effects-sets-033.md#s-99260ce7577b734c)

### observed_connections-003376

```text
(config-router-scope)# no bgp sso route-refresh-enable <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 38 `；EOL ` RVA 0x3456BBF8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e398f2ee0aabd351](../../evidence/conditions-sets-088.md#c-e398f2ee0aabd351) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003239

```text
(config-router-scope)# no bgp suppress-inactive <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 45 `；EOL ` RVA 0x34572D50 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4f05aeab7e8f8bdc](../../evidence/conditions-sets-031.md#c-4f05aeab7e8f8bdc) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003150

```text
(config-router-scope)# no bgp tid <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 55 `；EOL ` RVA 0x34564778 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-cfff907ac6ec2dfc](../../evidence/conditions-sets-080.md#c-cfff907ac6ec2dfc) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003350

```text
(config-router-scope)# no bgp transport path-mtu-discovery <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 50 `；EOL ` RVA 0x345675F0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f2d18c8b4e477c8c](../../evidence/conditions-sets-094.md#c-f2d18c8b4e477c8c) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003191

```text
(config-router-scope)# no bgp update-delay <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 30 `；EOL ` RVA 0x3456A570 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-37b87d3cea420fa7](../../evidence/conditions-sets-022.md#c-37b87d3cea420fa7) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003407

```text
(config-router-scope)# no bgp update-group split as-override <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 73 `；EOL ` RVA 0x345769E8 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f4551f0fa238f3b5](../../evidence/conditions-sets-094.md#c-f4551f0fa238f3b5) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003214

```text
(config-router-scope)# no bgp upgrade-cli <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 33 `；EOL ` RVA 0x34564B90 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0bac9c68b382fb22](../../evidence/conditions-sets-005.md#c-0bac9c68b382fb22) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003255

```text
(config-router-scope)# no bgp va <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 80 `；EOL ` RVA 0x345782B0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4265f8ccfe33cd1a](../../evidence/conditions-sets-026.md#c-4265f8ccfe33cd1a) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)

### observed_connections-003379

```text
(config-router-scope)# no bgp vrf-update-optimisation off <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 66 `；EOL ` RVA 0x3456C6B0 `。

模式根 ` RVA 0x34558FA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e398f2ee0aabd351](../../evidence/conditions-sets-088.md#c-e398f2ee0aabd351) · [状态效果 S-1b0c1d5138f9474d](../../evidence/state_effects-sets-006.md#s-1b0c1d5138f9474d)
