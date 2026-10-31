# bgp-address-family · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-001128

```text
(config-router-af)# advertise l2vpn evpn <cr>
```

Handler ` RVA 0xF2569C0 `；selector ` 0 `；EOL ` RVA 0x3448F770 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a3c28d6a0b2a77b5](../../evidence/conditions-sets-063.md#c-a3c28d6a0b2a77b5) · [状态效果 S-e3ccc434168b9e6f](../../evidence/state_effects-sets-048.md#s-e3ccc434168b9e6f)

### observed_connections-001204

```text
(config-router-af)# aggregate-address <address> <address> <cr>
```

Handler ` RVA 0xF1B7BE0 `；selector ` 0 `；EOL ` RVA 0x344A7EF0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Aggregate address；` address ` Aggregate mask。

[条件 C-7a4e6d3a417f3e95](../../evidence/conditions-sets-047.md#c-7a4e6d3a417f3e95) · [参数 P-914e458157ad6a8f](../../evidence/parameters-sets-011.md#p-914e458157ad6a8f)

### observed_connections-001429

```text
(config-router-af)# aggregate-address <prefix:dynamic> <cr>
```

Handler ` RVA 0xF1B7BE0 `；selector ` 0 `；EOL ` RVA 0x344A7EF0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` IPv6 Network number。

[条件 C-03188fe501fc1069](../../evidence/conditions-sets-002.md#c-03188fe501fc1069) · [缺口 G-205abf9717d2c5e6](../../evidence/gaps-sets-002.md#g-205abf9717d2c5e6) · [参数 P-3c5dcfc8a730fe96](../../evidence/parameters-sets-005.md#p-3c5dcfc8a730fe96)

### observed_connections-001027

```text
(config-router-af)# auto-summary <cr>
```

Handler ` RVA 0xE1FA6B0 `；selector ` 0 `；EOL ` RVA 0x344F7B28 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-892cb3702bd56b94](../../evidence/conditions-sets-053.md#c-892cb3702bd56b94)

### observed_connections-001174

```text
(config-router-af)# bgp additional-paths install <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 69 `；EOL ` RVA 0x3449F770 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-928f75bb67af333f](../../evidence/conditions-sets-057.md#c-928f75bb67af333f) · [状态效果 S-075777069778affc](../../evidence/state_effects-sets-002.md#s-075777069778affc)

### observed_connections-001194

```text
(config-router-af)# bgp additional-paths select <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 71 `；EOL ` RVA 0x3449F418 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4535ae221f00abe5](../../evidence/conditions-sets-027.md#c-4535ae221f00abe5)

### observed_connections-001080

```text
(config-router-af)# bgp advertise-best-external <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 70 `；EOL ` RVA 0x344A05C0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7657ebc5798c2d01](../../evidence/conditions-sets-046.md#c-7657ebc5798c2d01)

### observed_connections-001102

```text
(config-router-af)# bgp advertisement startup-delay <number:1..3600> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 95 `；EOL ` RVA 0x34498430 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` value (seconds)。

[条件 C-4415cd2c1a9d67c9](../../evidence/conditions-sets-027.md#c-4415cd2c1a9d67c9) · [参数 P-acec78031e6cbb82](../../evidence/parameters-sets-013.md#p-acec78031e6cbb82)

### observed_connections-001195

```text
(config-router-af)# bgp aggregate-timer <number:6..60> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 58 `；EOL ` RVA 0x344A6610 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timer interval。

[条件 C-5be2d964dc2681c9](../../evidence/conditions-sets-036.md#c-5be2d964dc2681c9) · [参数 P-51cebb32e63b4ca3](../../evidence/parameters-sets-007.md#p-51cebb32e63b4ca3)

### observed_connections-001111

```text
(config-router-af)# bgp aigp-rib-metric <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 91 `；EOL ` RVA 0x3449CEB0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-292918144cc23f5a](../../evidence/conditions-sets-016.md#c-292918144cc23f5a)

### observed_connections-001077

```text
(config-router-af)# bgp always-compare-med <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 5 `；EOL ` RVA 0x34493D18 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e27560d5ee3533f0](../../evidence/conditions-sets-087.md#c-e27560d5ee3533f0)

### observed_connections-001161

```text
(config-router-af)# bgp asnotation dot <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 64 `；EOL ` RVA 0x34494028 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e27560d5ee3533f0](../../evidence/conditions-sets-087.md#c-e27560d5ee3533f0)

### observed_connections-001339

```text
(config-router-af)# bgp bestpath aigp ignore <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 43 `；EOL ` RVA 0x3449BBD8 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1a37981dc0299bb4](../../evidence/conditions-sets-010.md#c-1a37981dc0299bb4)

### observed_connections-001333

```text
(config-router-af)# bgp bestpath as-path ignore <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 17 `；EOL ` RVA 0x3449B348 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-292918144cc23f5a](../../evidence/conditions-sets-016.md#c-292918144cc23f5a)

### observed_connections-001335

```text
(config-router-af)# bgp bestpath as-path multipath-relax <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 51 `；EOL ` RVA 0x3449B5F0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-292918144cc23f5a](../../evidence/conditions-sets-016.md#c-292918144cc23f5a)

### observed_connections-001239

```text
(config-router-af)# bgp bestpath compare-routerid <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 24 `；EOL ` RVA 0x3449B888 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-292918144cc23f5a](../../evidence/conditions-sets-016.md#c-292918144cc23f5a)

### observed_connections-001338

```text
(config-router-af)# bgp bestpath cost-community ignore <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 41 `；EOL ` RVA 0x3449BEB0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-292918144cc23f5a](../../evidence/conditions-sets-016.md#c-292918144cc23f5a)

### observed_connections-001280

```text
(config-router-af)# bgp bestpath igp-metric ignore <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 42 `；EOL ` RVA 0x3449FCA0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-12684a895e92662c](../../evidence/conditions-sets-007.md#c-12684a895e92662c)

### observed_connections-001336

```text
(config-router-af)# bgp bestpath med missing-as-worst <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 18 `；EOL ` RVA 0x3449B038 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-292918144cc23f5a](../../evidence/conditions-sets-016.md#c-292918144cc23f5a) · [状态效果 S-ef75727ad84f1f3b](../../evidence/state_effects-sets-051.md#s-ef75727ad84f1f3b)

### observed_connections-001288

```text
(config-router-af)# bgp bestpath prefix-validate allow-invalid <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 78 `；EOL ` RVA 0x3449FFB0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-87b72272feb7b1d0](../../evidence/conditions-sets-052.md#c-87b72272feb7b1d0)

### observed_connections-001294

```text
(config-router-af)# bgp bestpath prefix-validate disable <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 77 `；EOL ` RVA 0x344A0258 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-87b72272feb7b1d0](../../evidence/conditions-sets-052.md#c-87b72272feb7b1d0)

### observed_connections-001182

```text
(config-router-af)# bgp client-to-client reflection <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 9 `；EOL ` RVA 0x34494EB8 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d9b175ed3b628ebc](../../evidence/conditions-sets-084.md#c-d9b175ed3b628ebc) · [状态效果 S-e60eb071b525ce06](../../evidence/state_effects-sets-049.md#s-e60eb071b525ce06)

### observed_connections-001514

```text
(config-router-af)# bgp client-to-client reflection intra-cluster cluster-id <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 9 `；EOL ` RVA 0x34494EB8 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7b489ec867fa7e38](../../evidence/conditions-sets-048.md#c-7b489ec867fa7e38) · [缺口 G-19978005c849d77c](../../evidence/gaps-sets-001.md#g-19978005c849d77c) · [状态效果 S-cf2b75fff4fc8712](../../evidence/state_effects-sets-044.md#s-cf2b75fff4fc8712)

### observed_connections-001179

```text
(config-router-af)# bgp cluster-id <number:1..4294967294> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 7 `；EOL ` RVA 0x34494A80 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Route-Reflector Cluster-id as 32 bit quantity。

[条件 C-9655695f31c83d9d](../../evidence/conditions-sets-058.md#c-9655695f31c83d9d) · [参数 P-198fddb9243f1c93](../../evidence/parameters-sets-002.md#p-198fddb9243f1c93)

### observed_connections-001499

```text
(config-router-af)# bgp confederation identifier <?bgp_as4_action@5555899e9d88> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 6 `；EOL ` RVA 0x34495DC0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e27560d5ee3533f0](../../evidence/conditions-sets-087.md#c-e27560d5ee3533f0) · [缺口 G-9bb8a8946b2f23a6](../../evidence/gaps-sets-006.md#g-9bb8a8946b2f23a6)

### observed_connections-001500

```text
(config-router-af)# bgp confederation peers <?bgp_as4_action@5555899ea0f8> <cr>
```

Handler ` RVA 0xF1C67F0 `；selector ` 0 `；EOL ` RVA 0x34496238 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-369057c7cc12915c](../../evidence/conditions-sets-021.md#c-369057c7cc12915c) · [缺口 G-355e3d064c217023](../../evidence/gaps-sets-002.md#g-355e3d064c217023) · [状态效果 S-a83f3afe94eb5696](../../evidence/state_effects-sets-036.md#s-a83f3afe94eb5696)

### observed_connections-001198

```text
(config-router-af)# bgp consistency-checker error-message <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 3 `；EOL ` RVA 0x34494400 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9d42fc5a3b3d4fe5](../../evidence/conditions-sets-061.md#c-9d42fc5a3b3d4fe5) · [状态效果 S-5a6b46e727a06bf2](../../evidence/state_effects-sets-019.md#s-5a6b46e727a06bf2)

### observed_connections-001186

```text
(config-router-af)# bgp consistency-checker error-message interval <number:5..1440> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 3 `；EOL ` RVA 0x34494428 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Interval (minutes)。

[条件 C-d179c626d82ed522](../../evidence/conditions-sets-081.md#c-d179c626d82ed522) · [参数 P-f0be965367bc9fb4](../../evidence/parameters-sets-018.md#p-f0be965367bc9fb4) · [状态效果 S-5a6b46e727a06bf2](../../evidence/state_effects-sets-019.md#s-5a6b46e727a06bf2)

### observed_connections-001082

```text
(config-router-af)# bgp dampening <cr>
```

Handler ` RVA 0xF1B85B0 `；selector ` 0 `；EOL ` RVA 0x3449E838 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-410ec6475a83cf7b](../../evidence/conditions-sets-025.md#c-410ec6475a83cf7b)

### observed_connections-001284

```text
(config-router-af)# bgp dampening route-map <string> <cr>
```

Handler ` RVA 0xF1B85B0 `；selector ` 8 `；EOL ` RVA 0x3449EA00 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` route-map name。

[条件 C-cd7d782217f2080b](../../evidence/conditions-sets-079.md#c-cd7d782217f2080b) · [参数 P-4f1cca0f08925235](../../evidence/parameters-sets-007.md#p-4f1cca0f08925235)

### observed_connections-001281

```text
(config-router-af)# bgp default inter-as-hybrid advertise-source-routes <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 57 `；EOL ` RVA 0x3449DE70 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6e3b3262cdac263c](../../evidence/conditions-sets-043.md#c-6e3b3262cdac263c)

### observed_connections-001147

```text
(config-router-af)# bgp default ipv4-unicast <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 19 `；EOL ` RVA 0x3449D5C8 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7bd7eb7684f098f8](../../evidence/conditions-sets-048.md#c-7bd7eb7684f098f8)

### observed_connections-001151

```text
(config-router-af)# bgp default ipv6-nexthop <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 75 `；EOL ` RVA 0x3449D8C0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8fdadd724abf1080](../../evidence/conditions-sets-056.md#c-8fdadd724abf1080)

### observed_connections-001079

```text
(config-router-af)# bgp default local-preference <number:0..4294967295> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 0 `；EOL ` RVA 0x3449DB50 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Configure default local preference value。

[条件 C-06c9421d5ca815c3](../../evidence/conditions-sets-003.md#c-06c9421d5ca815c3) · [参数 P-cce9cd8c0d78100a](../../evidence/parameters-sets-016.md#p-cce9cd8c0d78100a)

### observed_connections-001277

```text
(config-router-af)# bgp default route-target filter <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 25 `；EOL ` RVA 0x3449E1D8 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-681462e02c6b52c0](../../evidence/conditions-sets-040.md#c-681462e02c6b52c0)

### observed_connections-001278

```text
(config-router-af)# bgp default route-target filter <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 25 `；EOL ` RVA 0x3449E478 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b99ec9f9a643af4d](../../evidence/conditions-sets-072.md#c-b99ec9f9a643af4d)

### observed_connections-001091

```text
(config-router-af)# bgp deterministic-med <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 10 `；EOL ` RVA 0x34496538 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e27560d5ee3533f0](../../evidence/conditions-sets-087.md#c-e27560d5ee3533f0)

### observed_connections-001084

```text
(config-router-af)# bgp dmzlink-bw <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 31 `；EOL ` RVA 0x344A1B70 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5c6277c6ec36b6d9](../../evidence/conditions-sets-036.md#c-5c6277c6ec36b6d9)

### observed_connections-001028

```text
(config-router-af)# bgp dynamic-med-interval <number:60..4294967295> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 21 `；EOL ` RVA 0x34496560 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Interval value (seconds)。

[条件 C-536533ee7da4e898](../../evidence/conditions-sets-033.md#c-536533ee7da4e898) · [参数 P-aa24431afd5b5c12](../../evidence/parameters-sets-013.md#p-aa24431afd5b5c12)

### observed_connections-001085

```text
(config-router-af)# bgp enforce-first-as <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 20 `；EOL ` RVA 0x34495768 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e27560d5ee3533f0](../../evidence/conditions-sets-087.md#c-e27560d5ee3533f0)

### observed_connections-001107

```text
(config-router-af)# bgp enhanced-error <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 82 `；EOL ` RVA 0x344981A8 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c257e879ed7f3f2d](../../evidence/conditions-sets-075.md#c-c257e879ed7f3f2d)

### observed_connections-001072

```text
(config-router-af)# bgp fast-external-fallover <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 1 `；EOL ` RVA 0x34493450 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e27560d5ee3533f0](../../evidence/conditions-sets-087.md#c-e27560d5ee3533f0)

### observed_connections-001110

```text
(config-router-af)# bgp graceful-restart <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 35 `；EOL ` RVA 0x34499018 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e27560d5ee3533f0](../../evidence/conditions-sets-087.md#c-e27560d5ee3533f0)

### observed_connections-001108

```text
(config-router-af)# bgp graceful-restart restart-time <number:1..3600> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 36 `；EOL ` RVA 0x344989E8 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Delay value (seconds)。

[条件 C-6fe552547d65a917](../../evidence/conditions-sets-043.md#c-6fe552547d65a917) · [参数 P-d3d0dcfa834bafce](../../evidence/parameters-sets-016.md#p-d3d0dcfa834bafce)

### observed_connections-001109

```text
(config-router-af)# bgp graceful-restart stalepath-time <number:1..3600> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 37 `；EOL ` RVA 0x34498A50 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Delay value (seconds)。

[条件 C-b392d5dc96869b03](../../evidence/conditions-sets-069.md#c-b392d5dc96869b03) · [参数 P-92f48922c7d718b0](../../evidence/parameters-sets-011.md#p-92f48922c7d718b0)

### observed_connections-001520

```text
(config-router-af)# bgp graceful-shutdown all vrfs <number:30..65535> community <?bgp_community_action@5555899ed930> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 79 `；EOL ` RVA 0x34499480 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` time in seconds。

[条件 C-d541d70e4d4c93e5](../../evidence/conditions-sets-082.md#c-d541d70e4d4c93e5) · [缺口 G-5838fada67fe834b](../../evidence/gaps-sets-004.md#g-5838fada67fe834b) · [参数 P-2d9258a938db02e1](../../evidence/parameters-sets-004.md#p-2d9258a938db02e1) · [状态效果 S-5ba4360cdd808e2d](../../evidence/state_effects-sets-020.md#s-5ba4360cdd808e2d)

### observed_connections-001383

```text
(config-router-af)# bgp graceful-shutdown all vrfs activate <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 79 `；EOL ` RVA 0x34499480 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-efaafb9b08f976da](../../evidence/conditions-sets-093.md#c-efaafb9b08f976da) · [状态效果 S-ecdd7e4c59d8d568](../../evidence/state_effects-sets-050.md#s-ecdd7e4c59d8d568)

### observed_connections-001376

```text
(config-router-af)# bgp inject-map <string> exist-map <string> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 32 `；EOL ` RVA 0x344A36E8 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` route-map name；` string ` route-map name。

[条件 C-9063251b6c849b1e](../../evidence/conditions-sets-056.md#c-9063251b6c849b1e) · [参数 P-b763d74c2b1995aa](../../evidence/parameters-sets-014.md#p-b763d74c2b1995aa)

### observed_connections-001275

```text
(config-router-af)# bgp label-allocation-batch <number:0..4294967295> <number:0..4294967295> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 53 `；EOL ` RVA 0x344937E0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timer value in milliseconds；` unsigned_number ` Batch Size。

[条件 C-e27560d5ee3533f0](../../evidence/conditions-sets-087.md#c-e27560d5ee3533f0) · [参数 P-af331c78273510e6](../../evidence/parameters-sets-013.md#p-af331c78273510e6)

### observed_connections-001306

```text
(config-router-af)# bgp listen block <address> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 93 `；EOL ` RVA 0x344A1580 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IPv4 Dynamic Peering Address。

[条件 C-36dded38ffe00d05](../../evidence/conditions-sets-021.md#c-36dded38ffe00d05) · [参数 P-290a2f21d7abad26](../../evidence/parameters-sets-004.md#p-290a2f21d7abad26)

### observed_connections-001317

```text
(config-router-af)# bgp listen block <address> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 93 `；EOL ` RVA 0x344974E0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IPv4 Dynamic Peering Address。

[条件 C-2bcc0ef917cd22d4](../../evidence/conditions-sets-017.md#c-2bcc0ef917cd22d4) · [参数 P-adb020645b3b8fc6](../../evidence/parameters-sets-013.md#p-adb020645b3b8fc6)

### observed_connections-001088

```text
(config-router-af)# bgp listen limit <number:1..10000> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 61 `；EOL ` RVA 0x344A14C8 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` max number。

[条件 C-a6e09aef08c2248b](../../evidence/conditions-sets-064.md#c-a6e09aef08c2248b) · [参数 P-40fa35b38ddf6ed4](../../evidence/parameters-sets-005.md#p-40fa35b38ddf6ed4)

### observed_connections-001105

```text
(config-router-af)# bgp listen limit <number:1..10000> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 61 `；EOL ` RVA 0x34497400 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` max number。

[条件 C-3f5730eff3bafdde](../../evidence/conditions-sets-025.md#c-3f5730eff3bafdde) · [参数 P-429279b84bc4d28e](../../evidence/parameters-sets-006.md#p-429279b84bc4d28e)

### observed_connections-001231

```text
(config-router-af)# bgp listen persistent <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 94 `；EOL ` RVA 0x34497818 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2bcc0ef917cd22d4](../../evidence/conditions-sets-017.md#c-2bcc0ef917cd22d4)

### observed_connections-001519

```text
(config-router-af)# bgp listen range <prefix:dynamic> peer-group <string> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 60 `；EOL ` RVA 0x34497058 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` IPv4 subnet range；` string ` peer-group name。

[条件 C-84ae3db1c118ad84](../../evidence/conditions-sets-051.md#c-84ae3db1c118ad84) · [缺口 G-d4bd9a7733d8ab8e](../../evidence/gaps-sets-007.md#g-d4bd9a7733d8ab8e) · [参数 P-fcb7dee67970dec6](../../evidence/parameters-sets-019.md#p-fcb7dee67970dec6)

### observed_connections-001086

```text
(config-router-af)# bgp log-neighbor-changes <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 11 `；EOL ` RVA 0x34495A10 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e27560d5ee3533f0](../../evidence/conditions-sets-087.md#c-e27560d5ee3533f0)

### observed_connections-001252

```text
(config-router-af)# bgp maxas-limit <number:1..254> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 26 `；EOL ` RVA 0x3449CC28 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of ASes in the AS-PATH attribute(max 254)。

[条件 C-101491430f674708](../../evidence/conditions-sets-006.md#c-101491430f674708) · [参数 P-29ce24d150144702](../../evidence/parameters-sets-004.md#p-29ce24d150144702)

### observed_connections-001241

```text
(config-router-af)# bgp maxcommunity-limit <number:1..1018> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 27 `；EOL ` RVA 0x3449C238 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of communities in the COMMUNITY attribute。

[条件 C-11d4024f20bdfb04](../../evidence/conditions-sets-007.md#c-11d4024f20bdfb04) · [参数 P-0db3b2701da27df0](../../evidence/parameters-sets-002.md#p-0db3b2701da27df0)

### observed_connections-001248

```text
(config-router-af)# bgp maxextcommunity-limit <number:1..509> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 29 `；EOL ` RVA 0x3449C8D8 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of extended communities in the EXTENDED COMMUNITY attribute。

[条件 C-55edc3a630c9ca92](../../evidence/conditions-sets-034.md#c-55edc3a630c9ca92) · [参数 P-1d62c7acf393e0a0](../../evidence/parameters-sets-003.md#p-1d62c7acf393e0a0)

### observed_connections-001244

```text
(config-router-af)# bgp maxlargecommunity-limit <number:1..339> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 28 `；EOL ` RVA 0x3449C588 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of large communities in the LARGE COMMUNITY attribute。

[条件 C-1356ca7ab61a607a](../../evidence/conditions-sets-008.md#c-1356ca7ab61a607a) · [参数 P-71ada95e426c8fbd](../../evidence/parameters-sets-009.md#p-71ada95e426c8fbd)

### observed_connections-001099

```text
(config-router-af)# bgp mpls-local-label <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 81 `；EOL ` RVA 0x344A3A60 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6d1cb1b0115c90b7](../../evidence/conditions-sets-042.md#c-6d1cb1b0115c90b7)

### observed_connections-001309

```text
(config-router-af)# bgp nexthop route-map <string> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 56 `；EOL ` RVA 0x344A22D8 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` route-map name。

[条件 C-8c1685701636e846](../../evidence/conditions-sets-054.md#c-8c1685701636e846) · [参数 P-59d729b1ba654aaa](../../evidence/parameters-sets-007.md#p-59d729b1ba654aaa)

### observed_connections-001211

```text
(config-router-af)# bgp nexthop trigger critical-delay <number:0..100> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 48 `；EOL ` RVA 0x344A2840 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Critical delay value (seconds)。

[条件 C-56588419b8c8a0fe](../../evidence/conditions-sets-034.md#c-56588419b8c8a0fe) · [参数 P-897f10a6a5172238](../../evidence/parameters-sets-011.md#p-897f10a6a5172238)

### observed_connections-001206

```text
(config-router-af)# bgp nexthop trigger delay <number:0..100> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 47 `；EOL ` RVA 0x344A25C0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Delay value (seconds)。

[条件 C-9c11afa10b77e744](../../evidence/conditions-sets-060.md#c-9c11afa10b77e744) · [参数 P-c5bf3a6bd50ad9a3](../../evidence/parameters-sets-015.md#p-c5bf3a6bd50ad9a3)

### observed_connections-001305

```text
(config-router-af)# bgp nexthop trigger enable <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 49 `；EOL ` RVA 0x344A2598 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-18909225b0ace186](../../evidence/conditions-sets-010.md#c-18909225b0ace186)

### observed_connections-001316

```text
(config-router-af)# bgp nopeerup-delay cold-boot <number:1..3600> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 74 `；EOL ` RVA 0x34497E40 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Delay in seconds。

[条件 C-69dbbd35fe6cdffb](../../evidence/conditions-sets-041.md#c-69dbbd35fe6cdffb) · [参数 P-e9d1a35db10881b9](../../evidence/parameters-sets-017.md#p-e9d1a35db10881b9) · [状态效果 S-b4e5959bf3a5f043](../../evidence/state_effects-sets-038.md#s-b4e5959bf3a5f043)

### observed_connections-001169

```text
(config-router-af)# bgp recursion host <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 72 `；EOL ` RVA 0x344A0938 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-17a55084b4c93e34](../../evidence/conditions-sets-009.md#c-17a55084b4c93e34)

### observed_connections-001081

```text
(config-router-af)# bgp redistribute-internal <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 2 `；EOL ` RVA 0x344A4C60 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-815ce693cf2919a4](../../evidence/conditions-sets-050.md#c-815ce693cf2919a4)

### observed_connections-001330

```text
(config-router-af)# bgp refresh max-eor-time <number:600..3600> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 16 `；EOL ` RVA 0x3449A210 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timer interval (seconds)。

[条件 C-7c77dcbe244666ee](../../evidence/conditions-sets-048.md#c-7c77dcbe244666ee) · [参数 P-7a0a26961118af4d](../../evidence/parameters-sets-010.md#p-7a0a26961118af4d)

### observed_connections-001326

```text
(config-router-af)# bgp refresh stalepath-time <number:600..3600> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 15 `；EOL ` RVA 0x34499EA0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timer interval (seconds)。

[条件 C-bf0d478167dcf25e](../../evidence/conditions-sets-074.md#c-bf0d478167dcf25e) · [参数 P-e78d74eb30e9cc09](../../evidence/parameters-sets-017.md#p-e78d74eb30e9cc09)

### observed_connections-001236

```text
(config-router-af)# bgp regexp deterministic <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 44 `；EOL ` RVA 0x3449AC28 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-292918144cc23f5a](../../evidence/conditions-sets-016.md#c-292918144cc23f5a)

### observed_connections-001170

```text
(config-router-af)# bgp route-map priority <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 59 `；EOL ` RVA 0x344A5DF0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e01fa6635eb32d5c](../../evidence/conditions-sets-086.md#c-e01fa6635eb32d5c)

### observed_connections-001075

```text
(config-router-af)# bgp route-map-cache <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 34 `；EOL ` RVA 0x34493A68 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e27560d5ee3533f0](../../evidence/conditions-sets-087.md#c-e27560d5ee3533f0)

### observed_connections-001167

```text
(config-router-af)# bgp router-id <address> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 4 `；EOL ` RVA 0x34492E20 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Manually configured router identifier。

[条件 C-261d4b59aa1bbf22](../../evidence/conditions-sets-015.md#c-261d4b59aa1bbf22) · [参数 P-0fe4d758f38c67d4](../../evidence/parameters-sets-002.md#p-0fe4d758f38c67d4)

### observed_connections-001201

```text
(config-router-af)# bgp router-id auto-assign <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 4 `；EOL ` RVA 0x344A0FE8 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ca0615040f6f589b](../../evidence/conditions-sets-078.md#c-ca0615040f6f589b) · [状态效果 S-9ef13f8c92e9b0c2](../../evidence/state_effects-sets-034.md#s-9ef13f8c92e9b0c2)

### observed_connections-001497

```text
(config-router-af)# bgp router-id interface <interface> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 4 `；EOL ` RVA 0x34492E20 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a064b48feded18a9](../../evidence/conditions-sets-062.md#c-a064b48feded18a9) · [缺口 G-3dc2b826fa115ef5](../../evidence/gaps-sets-003.md#g-3dc2b826fa115ef5) · [参数 P-10d5324edac4c19b](../../evidence/parameters-sets-002.md#p-10d5324edac4c19b)

### observed_connections-001498

```text
(config-router-af)# bgp router-id interface <interface> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 4 `；EOL ` RVA 0x344A0FE8 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0e1ca6a35b28e1ed](../../evidence/conditions-sets-006.md#c-0e1ca6a35b28e1ed) · [缺口 G-9d02a0c63545cc31](../../evidence/gaps-sets-006.md#g-9d02a0c63545cc31) · [参数 P-b6c89c62568b39b4](../../evidence/parameters-sets-014.md#p-b6c89c62568b39b4)

### observed_connections-001411

```text
(config-router-af)# bgp rpki server tcp <address> port <number:1..65535> refresh <number:1..65535> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 76 `；EOL ` RVA 0x344A6C08 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IPv6 address of RPKI cache server；` unsigned_number ` Port number；` unsigned_number ` Refresh time in seconds。

[条件 C-6bf86105846acfa4](../../evidence/conditions-sets-042.md#c-6bf86105846acfa4) · [参数 P-3e17e0a994a3855a](../../evidence/parameters-sets-005.md#p-3e17e0a994a3855a)

### observed_connections-001212

```text
(config-router-af)# bgp rr-group <string> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 23 `；EOL ` RVA 0x344A3280 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Extended community-list name。

[条件 C-a07f25a3a6ad63d9](../../evidence/conditions-sets-062.md#c-a07f25a3a6ad63d9) · [参数 P-f82df96dd32c6e2c](../../evidence/parameters-sets-019.md#p-f82df96dd32c6e2c)

### observed_connections-001112

```text
(config-router-af)# bgp safe-ebgp-policy <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 92 `；EOL ` RVA 0x3449D1C0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-56d9ed88612d65e8](../../evidence/conditions-sets-034.md#c-56d9ed88612d65e8)

### observed_connections-001209

```text
(config-router-af)# bgp scan-time <number:5..60> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 22 `；EOL ` RVA 0x344A2F10 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Scanner interval (seconds)。

[条件 C-bdb2604a5d82a44b](../../evidence/conditions-sets-073.md#c-bdb2604a5d82a44b) · [参数 P-82542ab10ec2dd00](../../evidence/parameters-sets-010.md#p-82542ab10ec2dd00)

### observed_connections-001177

```text
(config-router-af)# bgp slow-peer detection <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 67 `；EOL ` RVA 0x344A3F30 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9272d44e52c0df3b](../../evidence/conditions-sets-056.md#c-9272d44e52c0df3b)

### observed_connections-001172

```text
(config-router-af)# bgp slow-peer detection threshold <number:120..3600> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 67 `；EOL ` RVA 0x344A3F08 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Threshold value (seconds)。

[条件 C-23cf5b9eeddd0789](../../evidence/conditions-sets-014.md#c-23cf5b9eeddd0789) · [参数 P-7f2f952f54e6b565](../../evidence/parameters-sets-010.md#p-7f2f952f54e6b565)

### observed_connections-001299

```text
(config-router-af)# bgp slow-peer split-update-group dynamic <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 68 `；EOL ` RVA 0x344A4500 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3adfc3fbedef38e7](../../evidence/conditions-sets-023.md#c-3adfc3fbedef38e7)

### observed_connections-001315

```text
(config-router-af)# bgp snmp traps add-type <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 90 `；EOL ` RVA 0x34496B28 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e27560d5ee3533f0](../../evidence/conditions-sets-087.md#c-e27560d5ee3533f0)

### observed_connections-001087

```text
(config-router-af)# bgp soft-reconfig-backup <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 52 `；EOL ` RVA 0x344A1EC0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f3a2c49acfa96d26](../../evidence/conditions-sets-094.md#c-f3a2c49acfa96d26)

### observed_connections-001369

```text
(config-router-af)# bgp sourced-paths per-net isis all <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 89 `；EOL ` RVA 0x344A5A70 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3faeea567cbb523d](../../evidence/conditions-sets-025.md#c-3faeea567cbb523d) · [状态效果 S-7f08c238eafcb56a](../../evidence/state_effects-sets-027.md#s-7f08c238eafcb56a)

### observed_connections-001364

```text
(config-router-af)# bgp sourced-paths per-net ospf all <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 87 `；EOL ` RVA 0x344A5410 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3faeea567cbb523d](../../evidence/conditions-sets-025.md#c-3faeea567cbb523d) · [状态效果 S-0d1a4a97f1fb7292](../../evidence/state_effects-sets-003.md#s-0d1a4a97f1fb7292)

### observed_connections-001365

```text
(config-router-af)# bgp sourced-paths per-net ospfv3 all <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 88 `；EOL ` RVA 0x344A5758 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3faeea567cbb523d](../../evidence/conditions-sets-025.md#c-3faeea567cbb523d) · [状态效果 S-efe546f2c72cb643](../../evidence/state_effects-sets-051.md#s-efe546f2c72cb643)

### observed_connections-001361

```text
(config-router-af)# bgp sourced-paths per-net static all <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 86 `；EOL ` RVA 0x344A50C8 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3faeea567cbb523d](../../evidence/conditions-sets-025.md#c-3faeea567cbb523d) · [状态效果 S-86c5f5563c979f73](../../evidence/state_effects-sets-029.md#s-86c5f5563c979f73)

### observed_connections-001232

```text
(config-router-af)# bgp sso route-refresh-enable <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 38 `；EOL ` RVA 0x34499AE0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-292918144cc23f5a](../../evidence/conditions-sets-016.md#c-292918144cc23f5a)

### observed_connections-001083

```text
(config-router-af)# bgp suppress-inactive <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 45 `；EOL ` RVA 0x344A0C38 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9f33035ef271057a](../../evidence/conditions-sets-062.md#c-9f33035ef271057a)

### observed_connections-001020

```text
(config-router-af)# bgp tid <number:1..255> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 55 `；EOL ` RVA 0x34492660 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Tolology identifier value。

[条件 C-b3e289ae5f519121](../../evidence/conditions-sets-070.md#c-b3e289ae5f519121) · [参数 P-6a205001339032a4](../../evidence/parameters-sets-008.md#p-6a205001339032a4)

### observed_connections-001178

```text
(config-router-af)# bgp transport path-mtu-discovery <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 50 `；EOL ` RVA 0x344954D8 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e27560d5ee3533f0](../../evidence/conditions-sets-087.md#c-e27560d5ee3533f0)

### observed_connections-001029

```text
(config-router-af)# bgp update-delay <number:1..3600> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 30 `；EOL ` RVA 0x34498458 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Delay value (seconds)。

[条件 C-05941233b96378e3](../../evidence/conditions-sets-003.md#c-05941233b96378e3) · [参数 P-5d1ed69465607a33](../../evidence/parameters-sets-007.md#p-5d1ed69465607a33)

### observed_connections-001283

```text
(config-router-af)# bgp update-group split as-override <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 73 `；EOL ` RVA 0x344A48D0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3b7621dd62e73dfd](../../evidence/conditions-sets-023.md#c-3b7621dd62e73dfd)

### observed_connections-001073

```text
(config-router-af)# bgp upgrade-cli <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 33 `；EOL ` RVA 0x34492A78 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-462fb0c2285a55bb](../../evidence/conditions-sets-027.md#c-462fb0c2285a55bb)

### observed_connections-001366

```text
(config-router-af)# bgp va <address> mask <address> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 80 `；EOL ` RVA 0x344A6198 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` BGP VA ip address；` address ` BGP VA mask address。

[条件 C-10d4bdc7ce323597](../../evidence/conditions-sets-007.md#c-10d4bdc7ce323597) · [参数 P-4fd641e2999b913a](../../evidence/parameters-sets-007.md#p-4fd641e2999b913a)

### observed_connections-001234

```text
(config-router-af)# bgp vrf-update-optimisation off <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 66 `；EOL ` RVA 0x3449A598 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-292918144cc23f5a](../../evidence/conditions-sets-016.md#c-292918144cc23f5a)

### observed_connections-001332

```text
(config-router-af)# bgp write-limit <number:500..2147483647> <number:500..2147483647> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 40 `；EOL ` RVA 0x3449A8F0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of messages to be formatted per neighbor/peergroup；` unsigned_number ` Number of messages that can be enqueued in total。

[条件 C-2d8b70e503ed6af0](../../evidence/conditions-sets-018.md#c-2d8b70e503ed6af0) · [参数 P-25f3b20b73032e4e](../../evidence/parameters-sets-003.md#p-25f3b20b73032e4e)

### observed_connections-001033

```text
(config-router-af)# context <string> <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 0 `；EOL ` RVA 0x33C44A60 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` SNMP Context Name。

[条件 C-9affa1869574e86e](../../evidence/conditions-sets-060.md#c-9affa1869574e86e) · [参数 P-f3e465802edc027f](../../evidence/parameters-sets-018.md#p-f3e465802edc027f) · [状态效果 S-355a44aeb0ea4c7f](../../evidence/state_effects-sets-012.md#s-355a44aeb0ea4c7f)

### observed_connections-001263

```text
(config-router-af)# default advertise l2vpn evpn <cr>
```

Handler ` RVA 0xF2569C0 `；selector ` 0 `；EOL ` RVA 0x3448F770 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a3c28d6a0b2a77b5](../../evidence/conditions-sets-063.md#c-a3c28d6a0b2a77b5) · [状态效果 S-9138c42c4b1f75cd](../../evidence/state_effects-sets-031.md#s-9138c42c4b1f75cd)

### observed_connections-001308

```text
(config-router-af)# default aggregate-address <address> <address> <cr>
```

Handler ` RVA 0xF1B7BE0 `；selector ` 0 `；EOL ` RVA 0x344A7EF0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` Aggregate address；` address ` Aggregate mask。

[条件 C-7a4e6d3a417f3e95](../../evidence/conditions-sets-047.md#c-7a4e6d3a417f3e95) · [参数 P-914e458157ad6a8f](../../evidence/parameters-sets-011.md#p-914e458157ad6a8f) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001092

```text
(config-router-af)# default auto-summary <cr>
```

Handler ` RVA 0xE1FA6B0 `；selector ` 0 `；EOL ` RVA 0x344F7B28 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-892cb3702bd56b94](../../evidence/conditions-sets-053.md#c-892cb3702bd56b94) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001295

```text
(config-router-af)# default bgp additional-paths install <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 69 `；EOL ` RVA 0x3449F770 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-928f75bb67af333f](../../evidence/conditions-sets-057.md#c-928f75bb67af333f) · [状态效果 S-b19115fe8e73e991](../../evidence/state_effects-sets-038.md#s-b19115fe8e73e991)

### observed_connections-001302

```text
(config-router-af)# default bgp additional-paths select <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 71 `；EOL ` RVA 0x3449F418 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4535ae221f00abe5](../../evidence/conditions-sets-027.md#c-4535ae221f00abe5) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001164

```text
(config-router-af)# default bgp advertise-best-external <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 70 `；EOL ` RVA 0x344A05C0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7657ebc5798c2d01](../../evidence/conditions-sets-046.md#c-7657ebc5798c2d01) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001220

```text
(config-router-af)# default bgp advertisement startup-delay <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 95 `；EOL ` RVA 0x34498430 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-94587e380a65b0e2](../../evidence/conditions-sets-057.md#c-94587e380a65b0e2) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001303

```text
(config-router-af)# default bgp aggregate-timer <number:6..60> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 58 `；EOL ` RVA 0x344A6610 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Timer interval。

[条件 C-5be2d964dc2681c9](../../evidence/conditions-sets-036.md#c-5be2d964dc2681c9) · [参数 P-51cebb32e63b4ca3](../../evidence/parameters-sets-007.md#p-51cebb32e63b4ca3) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001249

```text
(config-router-af)# default bgp aigp-rib-metric <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 91 `；EOL ` RVA 0x3449CEB0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-292918144cc23f5a](../../evidence/conditions-sets-016.md#c-292918144cc23f5a) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001157

```text
(config-router-af)# default bgp always-compare-med <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 5 `；EOL ` RVA 0x34493D18 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e27560d5ee3533f0](../../evidence/conditions-sets-087.md#c-e27560d5ee3533f0) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001282

```text
(config-router-af)# default bgp asnotation dot <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 64 `；EOL ` RVA 0x34494028 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e27560d5ee3533f0](../../evidence/conditions-sets-087.md#c-e27560d5ee3533f0) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001393

```text
(config-router-af)# default bgp bestpath aigp ignore <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 43 `；EOL ` RVA 0x3449BBD8 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1a37981dc0299bb4](../../evidence/conditions-sets-010.md#c-1a37981dc0299bb4) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001385

```text
(config-router-af)# default bgp bestpath as-path ignore <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 17 `；EOL ` RVA 0x3449B348 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-292918144cc23f5a](../../evidence/conditions-sets-016.md#c-292918144cc23f5a) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001388

```text
(config-router-af)# default bgp bestpath as-path multipath-relax <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 51 `；EOL ` RVA 0x3449B5F0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-292918144cc23f5a](../../evidence/conditions-sets-016.md#c-292918144cc23f5a) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001337

```text
(config-router-af)# default bgp bestpath compare-routerid <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 24 `；EOL ` RVA 0x3449B888 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-292918144cc23f5a](../../evidence/conditions-sets-016.md#c-292918144cc23f5a) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001392

```text
(config-router-af)# default bgp bestpath cost-community ignore <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 41 `；EOL ` RVA 0x3449BEB0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-292918144cc23f5a](../../evidence/conditions-sets-016.md#c-292918144cc23f5a) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001353

```text
(config-router-af)# default bgp bestpath igp-metric ignore <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 42 `；EOL ` RVA 0x3449FCA0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-12684a895e92662c](../../evidence/conditions-sets-007.md#c-12684a895e92662c) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001389

```text
(config-router-af)# default bgp bestpath med missing-as-worst <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 18 `；EOL ` RVA 0x3449B038 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-292918144cc23f5a](../../evidence/conditions-sets-016.md#c-292918144cc23f5a) · [状态效果 S-299499d95cda66d2](../../evidence/state_effects-sets-009.md#s-299499d95cda66d2)

### observed_connections-001358

```text
(config-router-af)# default bgp bestpath prefix-validate allow-invalid <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 78 `；EOL ` RVA 0x3449FFB0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-87b72272feb7b1d0](../../evidence/conditions-sets-052.md#c-87b72272feb7b1d0) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001362

```text
(config-router-af)# default bgp bestpath prefix-validate disable <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 77 `；EOL ` RVA 0x344A0258 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-87b72272feb7b1d0](../../evidence/conditions-sets-052.md#c-87b72272feb7b1d0) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001298

```text
(config-router-af)# default bgp client-to-client reflection <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 9 `；EOL ` RVA 0x34494EB8 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d9b175ed3b628ebc](../../evidence/conditions-sets-084.md#c-d9b175ed3b628ebc) · [状态效果 S-da9cc08882ffd0ed](../../evidence/state_effects-sets-046.md#s-da9cc08882ffd0ed)

### observed_connections-001184

```text
(config-router-af)# default bgp cluster-id <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 7 `；EOL ` RVA 0x34494A80 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8be41dcc9fbe50bd](../../evidence/conditions-sets-054.md#c-8be41dcc9fbe50bd) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001192

```text
(config-router-af)# default bgp consistency-checker <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 3 `；EOL ` RVA 0x34494400 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-23b7e108cbf929df](../../evidence/conditions-sets-014.md#c-23b7e108cbf929df) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001158

```text
(config-router-af)# default bgp dampening <cr>
```

Handler ` RVA 0xF1B85B0 `；selector ` 0 `；EOL ` RVA 0x3449E838 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-85bb974bd3aebfb3](../../evidence/conditions-sets-052.md#c-85bb974bd3aebfb3) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001355

```text
(config-router-af)# default bgp default inter-as-hybrid advertise-source-routes <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 57 `；EOL ` RVA 0x3449DE70 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6e3b3262cdac263c](../../evidence/conditions-sets-043.md#c-6e3b3262cdac263c) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001273

```text
(config-router-af)# default bgp default ipv4-unicast <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 19 `；EOL ` RVA 0x3449D5C8 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7bd7eb7684f098f8](../../evidence/conditions-sets-048.md#c-7bd7eb7684f098f8) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001276

```text
(config-router-af)# default bgp default ipv6-nexthop <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 75 `；EOL ` RVA 0x3449D8C0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8fdadd724abf1080](../../evidence/conditions-sets-056.md#c-8fdadd724abf1080) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001160

```text
(config-router-af)# default bgp default local-preference <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 0 `；EOL ` RVA 0x3449DB50 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-203327081868b838](../../evidence/conditions-sets-013.md#c-203327081868b838) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001349

```text
(config-router-af)# default bgp default route-target filter <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 25 `；EOL ` RVA 0x3449E1D8 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-681462e02c6b52c0](../../evidence/conditions-sets-040.md#c-681462e02c6b52c0) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001350

```text
(config-router-af)# default bgp default route-target filter <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 25 `；EOL ` RVA 0x3449E478 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b99ec9f9a643af4d](../../evidence/conditions-sets-072.md#c-b99ec9f9a643af4d) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001205

```text
(config-router-af)# default bgp deterministic-med <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 10 `；EOL ` RVA 0x34496538 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e27560d5ee3533f0](../../evidence/conditions-sets-087.md#c-e27560d5ee3533f0) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001180

```text
(config-router-af)# default bgp dmzlink-bw <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 31 `；EOL ` RVA 0x344A1B70 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5c6277c6ec36b6d9](../../evidence/conditions-sets-036.md#c-5c6277c6ec36b6d9) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001097

```text
(config-router-af)# default bgp dynamic-med-interval <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 21 `；EOL ` RVA 0x34496560 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-42adbaa615c0110b](../../evidence/conditions-sets-026.md#c-42adbaa615c0110b) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001187

```text
(config-router-af)# default bgp enforce-first-as <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 20 `；EOL ` RVA 0x34495768 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e27560d5ee3533f0](../../evidence/conditions-sets-087.md#c-e27560d5ee3533f0) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001225

```text
(config-router-af)# default bgp enhanced-error <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 82 `；EOL ` RVA 0x344981A8 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b432d5e5039b9a65](../../evidence/conditions-sets-070.md#c-b432d5e5039b9a65) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001143

```text
(config-router-af)# default bgp fast-external-fallover <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 1 `；EOL ` RVA 0x34493450 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e27560d5ee3533f0](../../evidence/conditions-sets-087.md#c-e27560d5ee3533f0) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001235

```text
(config-router-af)# default bgp graceful-restart <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 35 `；EOL ` RVA 0x34499018 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e27560d5ee3533f0](../../evidence/conditions-sets-087.md#c-e27560d5ee3533f0) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001228

```text
(config-router-af)# default bgp graceful-restart restart-time <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 36 `；EOL ` RVA 0x344989E8 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b9790c5900320715](../../evidence/conditions-sets-072.md#c-b9790c5900320715) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001230

```text
(config-router-af)# default bgp graceful-restart stalepath-time <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 37 `；EOL ` RVA 0x34498A50 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6ed3aa722ead93e9](../../evidence/conditions-sets-043.md#c-6ed3aa722ead93e9) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001409

```text
(config-router-af)# default bgp graceful-shutdown all vrfs activate <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 79 `；EOL ` RVA 0x34499480 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-efaafb9b08f976da](../../evidence/conditions-sets-093.md#c-efaafb9b08f976da) · [状态效果 S-29ba9e8e92581c35](../../evidence/state_effects-sets-009.md#s-29ba9e8e92581c35)

### observed_connections-001407

```text
(config-router-af)# default bgp inject-map <string> exist-map <string> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 32 `；EOL ` RVA 0x344A36E8 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` route-map name；` string ` route-map name。

[条件 C-9063251b6c849b1e](../../evidence/conditions-sets-056.md#c-9063251b6c849b1e) · [参数 P-b763d74c2b1995aa](../../evidence/parameters-sets-014.md#p-b763d74c2b1995aa) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001348

```text
(config-router-af)# default bgp label-allocation-batch <number:0..4294967295> <number:0..4294967295> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 53 `；EOL ` RVA 0x344937E0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Timer value in milliseconds；` unsigned_number ` Batch Size。

[条件 C-e27560d5ee3533f0](../../evidence/conditions-sets-087.md#c-e27560d5ee3533f0) · [参数 P-af331c78273510e6](../../evidence/parameters-sets-013.md#p-af331c78273510e6) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001371

```text
(config-router-af)# default bgp listen block <address> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 93 `；EOL ` RVA 0x344A1580 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IPv4 Dynamic Peering Address。

[条件 C-36dded38ffe00d05](../../evidence/conditions-sets-021.md#c-36dded38ffe00d05) · [参数 P-290a2f21d7abad26](../../evidence/parameters-sets-004.md#p-290a2f21d7abad26) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001382

```text
(config-router-af)# default bgp listen block <address> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 93 `；EOL ` RVA 0x344974E0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IPv4 Dynamic Peering Address。

[条件 C-2bcc0ef917cd22d4](../../evidence/conditions-sets-017.md#c-2bcc0ef917cd22d4) · [参数 P-adb020645b3b8fc6](../../evidence/parameters-sets-013.md#p-adb020645b3b8fc6) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001199

```text
(config-router-af)# default bgp listen limit <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 61 `；EOL ` RVA 0x344A14C8 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ae5f30b14a82a7f2](../../evidence/conditions-sets-067.md#c-ae5f30b14a82a7f2) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001226

```text
(config-router-af)# default bgp listen limit <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 61 `；EOL ` RVA 0x34497400 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c9e04b78b2a95bd2](../../evidence/conditions-sets-078.md#c-c9e04b78b2a95bd2) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001320

```text
(config-router-af)# default bgp listen persistent <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 94 `；EOL ` RVA 0x34497818 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2bcc0ef917cd22d4](../../evidence/conditions-sets-017.md#c-2bcc0ef917cd22d4) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001196

```text
(config-router-af)# default bgp log-neighbor-changes <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 11 `；EOL ` RVA 0x34495A10 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e27560d5ee3533f0](../../evidence/conditions-sets-087.md#c-e27560d5ee3533f0) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001254

```text
(config-router-af)# default bgp maxas-limit <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 26 `；EOL ` RVA 0x3449CC28 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-82737b7de591e234](../../evidence/conditions-sets-051.md#c-82737b7de591e234) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001242

```text
(config-router-af)# default bgp maxcommunity-limit <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 27 `；EOL ` RVA 0x3449C238 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8ac72d42a0bd3c88](../../evidence/conditions-sets-054.md#c-8ac72d42a0bd3c88) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001250

```text
(config-router-af)# default bgp maxextcommunity-limit <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 29 `；EOL ` RVA 0x3449C8D8 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0d11230835c03f8d](../../evidence/conditions-sets-005.md#c-0d11230835c03f8d) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001246

```text
(config-router-af)# default bgp maxlargecommunity-limit <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 28 `；EOL ` RVA 0x3449C588 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e8444a28aec9f227](../../evidence/conditions-sets-090.md#c-e8444a28aec9f227) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001215

```text
(config-router-af)# default bgp mpls-local-label <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 81 `；EOL ` RVA 0x344A3A60 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6d1cb1b0115c90b7](../../evidence/conditions-sets-042.md#c-6d1cb1b0115c90b7) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001373

```text
(config-router-af)# default bgp nexthop route-map <string> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 56 `；EOL ` RVA 0x344A22D8 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` route-map name。

[条件 C-8c1685701636e846](../../evidence/conditions-sets-054.md#c-8c1685701636e846) · [参数 P-59d729b1ba654aaa](../../evidence/parameters-sets-007.md#p-59d729b1ba654aaa) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001314

```text
(config-router-af)# default bgp nexthop trigger critical-delay <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 48 `；EOL ` RVA 0x344A2840 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6f8db306b2850a35](../../evidence/conditions-sets-043.md#c-6f8db306b2850a35) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001311

```text
(config-router-af)# default bgp nexthop trigger delay <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 47 `；EOL ` RVA 0x344A25C0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a768399c8b14a916](../../evidence/conditions-sets-065.md#c-a768399c8b14a916) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001370

```text
(config-router-af)# default bgp nexthop trigger enable <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 49 `；EOL ` RVA 0x344A2598 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-18909225b0ace186](../../evidence/conditions-sets-010.md#c-18909225b0ace186) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001379

```text
(config-router-af)# default bgp nopeerup-delay cold-boot <number:1..3600> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 74 `；EOL ` RVA 0x34497E40 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Delay in seconds。

[条件 C-69dbbd35fe6cdffb](../../evidence/conditions-sets-041.md#c-69dbbd35fe6cdffb) · [参数 P-e9d1a35db10881b9](../../evidence/parameters-sets-017.md#p-e9d1a35db10881b9) · [状态效果 S-919296e3e945a522](../../evidence/state_effects-sets-031.md#s-919296e3e945a522)

### observed_connections-001289

```text
(config-router-af)# default bgp recursion host <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 72 `；EOL ` RVA 0x344A0938 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-17a55084b4c93e34](../../evidence/conditions-sets-009.md#c-17a55084b4c93e34) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001165

```text
(config-router-af)# default bgp redistribute-internal <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 2 `；EOL ` RVA 0x344A4C60 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-815ce693cf2919a4](../../evidence/conditions-sets-050.md#c-815ce693cf2919a4) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001331

```text
(config-router-af)# default bgp refresh max-eor-time <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 16 `；EOL ` RVA 0x3449A210 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e69bb68406b040c7](../../evidence/conditions-sets-089.md#c-e69bb68406b040c7) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001327

```text
(config-router-af)# default bgp refresh stalepath-time <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 15 `；EOL ` RVA 0x34499EA0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e06f7cab4b2f5505](../../evidence/conditions-sets-086.md#c-e06f7cab4b2f5505) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001329

```text
(config-router-af)# default bgp regexp deterministic <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 44 `；EOL ` RVA 0x3449AC28 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-292918144cc23f5a](../../evidence/conditions-sets-016.md#c-292918144cc23f5a) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001290

```text
(config-router-af)# default bgp route-map priority <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 59 `；EOL ` RVA 0x344A5DF0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e01fa6635eb32d5c](../../evidence/conditions-sets-086.md#c-e01fa6635eb32d5c) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001152

```text
(config-router-af)# default bgp route-map-cache <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 34 `；EOL ` RVA 0x34493A68 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e27560d5ee3533f0](../../evidence/conditions-sets-087.md#c-e27560d5ee3533f0) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001159

```text
(config-router-af)# default bgp router-id <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 4 `；EOL ` RVA 0x34492E20 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9fdc04670fb5b1ed](../../evidence/conditions-sets-062.md#c-9fdc04670fb5b1ed) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001200

```text
(config-router-af)# default bgp router-id <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 4 `；EOL ` RVA 0x344A0FE8 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4f7c358522986c3a](../../evidence/conditions-sets-031.md#c-4f7c358522986c3a) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001413

```text
(config-router-af)# default bgp rpki server tcp <address> port <number:1..65535> refresh <number:1..65535> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 76 `；EOL ` RVA 0x344A6C08 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IPv6 address of RPKI cache server；` unsigned_number ` Port number；` unsigned_number ` Refresh time in seconds。

[条件 C-6bf86105846acfa4](../../evidence/conditions-sets-042.md#c-6bf86105846acfa4) · [参数 P-3e17e0a994a3855a](../../evidence/parameters-sets-005.md#p-3e17e0a994a3855a) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001210

```text
(config-router-af)# default bgp rr-group <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 23 `；EOL ` RVA 0x344A3280 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ca7be684d21bafb7](../../evidence/conditions-sets-078.md#c-ca7be684d21bafb7) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001255

```text
(config-router-af)# default bgp safe-ebgp-policy <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 92 `；EOL ` RVA 0x3449D1C0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-56d9ed88612d65e8](../../evidence/conditions-sets-034.md#c-56d9ed88612d65e8) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001313

```text
(config-router-af)# default bgp scan-time <number:5..60> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 22 `；EOL ` RVA 0x344A2F10 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Scanner interval (seconds)。

[条件 C-bdb2604a5d82a44b](../../evidence/conditions-sets-073.md#c-bdb2604a5d82a44b) · [参数 P-82542ab10ec2dd00](../../evidence/parameters-sets-010.md#p-82542ab10ec2dd00) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001292

```text
(config-router-af)# default bgp slow-peer detection <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 67 `；EOL ` RVA 0x344A3F30 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-bc12adb769b845aa](../../evidence/conditions-sets-073.md#c-bc12adb769b845aa) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001363

```text
(config-router-af)# default bgp slow-peer split-update-group dynamic <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 68 `；EOL ` RVA 0x344A4500 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-32955e071c93a7cc](../../evidence/conditions-sets-020.md#c-32955e071c93a7cc) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001375

```text
(config-router-af)# default bgp snmp traps add-type <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 90 `；EOL ` RVA 0x34496B28 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e27560d5ee3533f0](../../evidence/conditions-sets-087.md#c-e27560d5ee3533f0) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001197

```text
(config-router-af)# default bgp soft-reconfig-backup <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 52 `；EOL ` RVA 0x344A1EC0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f3a2c49acfa96d26](../../evidence/conditions-sets-094.md#c-f3a2c49acfa96d26) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001405

```text
(config-router-af)# default bgp sourced-paths per-net isis all <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 89 `；EOL ` RVA 0x344A5A70 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3faeea567cbb523d](../../evidence/conditions-sets-025.md#c-3faeea567cbb523d) · [状态效果 S-aaf2d476b48b261e](../../evidence/state_effects-sets-036.md#s-aaf2d476b48b261e)

### observed_connections-001401

```text
(config-router-af)# default bgp sourced-paths per-net ospf all <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 87 `；EOL ` RVA 0x344A5410 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3faeea567cbb523d](../../evidence/conditions-sets-025.md#c-3faeea567cbb523d) · [状态效果 S-70b3220099d0acbe](../../evidence/state_effects-sets-024.md#s-70b3220099d0acbe)

### observed_connections-001403

```text
(config-router-af)# default bgp sourced-paths per-net ospfv3 all <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 88 `；EOL ` RVA 0x344A5758 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3faeea567cbb523d](../../evidence/conditions-sets-025.md#c-3faeea567cbb523d) · [状态效果 S-f146abfb75421581](../../evidence/state_effects-sets-051.md#s-f146abfb75421581)

### observed_connections-001399

```text
(config-router-af)# default bgp sourced-paths per-net static all <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 86 `；EOL ` RVA 0x344A50C8 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3faeea567cbb523d](../../evidence/conditions-sets-025.md#c-3faeea567cbb523d) · [状态效果 S-efbd23b125478a5d](../../evidence/state_effects-sets-051.md#s-efbd23b125478a5d)

### observed_connections-001321

```text
(config-router-af)# default bgp sso route-refresh-enable <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 38 `；EOL ` RVA 0x34499AE0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-292918144cc23f5a](../../evidence/conditions-sets-016.md#c-292918144cc23f5a) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001171

```text
(config-router-af)# default bgp suppress-inactive <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 45 `；EOL ` RVA 0x344A0C38 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9f33035ef271057a](../../evidence/conditions-sets-062.md#c-9f33035ef271057a) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001065

```text
(config-router-af)# default bgp tid <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 55 `；EOL ` RVA 0x34492660 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6515a478b68bd5fe](../../evidence/conditions-sets-039.md#c-6515a478b68bd5fe) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001297

```text
(config-router-af)# default bgp transport path-mtu-discovery <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 50 `；EOL ` RVA 0x344954D8 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e27560d5ee3533f0](../../evidence/conditions-sets-087.md#c-e27560d5ee3533f0) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001106

```text
(config-router-af)# default bgp update-delay <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 30 `；EOL ` RVA 0x34498458 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-396c7aba5ab065c3](../../evidence/conditions-sets-022.md#c-396c7aba5ab065c3) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001356

```text
(config-router-af)# default bgp update-group split as-override <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 73 `；EOL ` RVA 0x344A48D0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3b7621dd62e73dfd](../../evidence/conditions-sets-023.md#c-3b7621dd62e73dfd) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001149

```text
(config-router-af)# default bgp upgrade-cli <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 33 `；EOL ` RVA 0x34492A78 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-462fb0c2285a55bb](../../evidence/conditions-sets-027.md#c-462fb0c2285a55bb) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001190

```text
(config-router-af)# default bgp va <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 80 `；EOL ` RVA 0x344A6198 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2586208e947565bc](../../evidence/conditions-sets-015.md#c-2586208e947565bc) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001325

```text
(config-router-af)# default bgp vrf-update-optimisation off <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 66 `；EOL ` RVA 0x3449A598 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-292918144cc23f5a](../../evidence/conditions-sets-016.md#c-292918144cc23f5a) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001238

```text
(config-router-af)# default bgp write-limit <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 40 `；EOL ` RVA 0x3449A8F0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ff3fa97deb2013fa](../../evidence/conditions-sets-098.md#c-ff3fa97deb2013fa) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001031

```text
(config-router-af)# default context <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 0 `；EOL ` RVA 0x33C44A60 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ada418e0516d363b](../../evidence/conditions-sets-067.md#c-ada418e0516d363b) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001118

```text
(config-router-af)# default default-information originate <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 6 `；EOL ` RVA 0x3552C0E0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-55ee11b1a1edf64f](../../evidence/conditions-sets-034.md#c-55ee11b1a1edf64f) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001208

```text
(config-router-af)# default default-information originate <cr>
```

Handler ` RVA 0xE1F1F70 `；selector ` 0 `；EOL ` RVA 0x344F59A8 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a9575d4774f8de5d](../../evidence/conditions-sets-065.md#c-a9575d4774f8de5d) · [状态效果 S-0d77d7fd233e0044](../../evidence/state_effects-sets-003.md#s-0d77d7fd233e0044)

### observed_connections-001050

```text
(config-router-af)# default default-metric <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 12 `；EOL ` RVA 0x3552C878 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0d7ad9d9671c3c19](../../evidence/conditions-sets-005.md#c-0d7ad9d9671c3c19) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001094

```text
(config-router-af)# default default-metric <cr>
```

Handler ` RVA 0xE1F35A0 `；selector ` 0 `；EOL ` RVA 0x344F6270 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7412fd70c0f11908](../../evidence/conditions-sets-045.md#c-7412fd70c0f11908) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001039

```text
(config-router-af)# default distance <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 9 `；EOL ` RVA 0x35530D38 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-256dbeabc9b99bbc](../../evidence/conditions-sets-015.md#c-256dbeabc9b99bbc) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001101

```text
(config-router-af)# default distance <cr>
```

Handler ` RVA 0xE1E3290 `；selector ` 1 `；EOL ` RVA 0x344F73A0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8507c54e95cd8959](../../evidence/conditions-sets-051.md#c-8507c54e95cd8959) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001119

```text
(config-router-af)# default distance bgp <cr>
```

Handler ` RVA 0xF1B8400 `；selector ` 1 `；EOL ` RVA 0x355310F8 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b4939ca72f266b3e](../../evidence/conditions-sets-070.md#c-b4939ca72f266b3e) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001216

```text
(config-router-af)# default distance bgp <cr>
```

Handler ` RVA 0xF1B8400 `；selector ` 1 `；EOL ` RVA 0x344E1458 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b241df4e6f36d579](../../evidence/conditions-sets-069.md#c-b241df4e6f36d579) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001123

```text
(config-router-af)# default distance mbgp <cr>
```

Handler ` RVA 0xF1B8400 `；selector ` 2 `；EOL ` RVA 0x355314F0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3f9c2788ca7a36eb](../../evidence/conditions-sets-025.md#c-3f9c2788ca7a36eb) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001223

```text
(config-router-af)# default distance mbgp <cr>
```

Handler ` RVA 0xF1B8400 `；selector ` 2 `；EOL ` RVA 0x344E1850 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad31524aadb46fbf](../../evidence/conditions-sets-067.md#c-ad31524aadb46fbf) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001221

```text
(config-router-af)# default distribute-list in <cr>
```

Handler ` RVA 0xE1EE180 `；selector ` 0 `；EOL ` RVA 0x344F6960 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ea8c888fa5896889](../../evidence/conditions-sets-091.md#c-ea8c888fa5896889) · [状态效果 S-642daecfbe59b784](../../evidence/state_effects-sets-021.md#s-642daecfbe59b784)

### observed_connections-001043

```text
(config-router-af)# default domain-distinguisher <cr>
```

Handler ` RVA 0xF1D1870 `；selector ` 0 `；EOL ` RVA 0x3448F1E0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8a5499e94f9d3508](../../evidence/conditions-sets-053.md#c-8a5499e94f9d3508) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001026

```text
(config-router-af)# default flash-update-threshold <cr>
```

Handler ` RVA 0xE1F7ED0 `；selector ` 0 `；EOL ` RVA 0x344F5498 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0e6ae0e65ef7f08e](../../evidence/conditions-sets-006.md#c-0e6ae0e65ef7f08e) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001070

```text
(config-router-af)# default import <cr>
```

Handler ` RVA 0xF08D6A0 `；selector ` 0 `；EOL ` RVA 0x344909D0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f66640e5ce70c303](../../evidence/conditions-sets-095.md#c-f66640e5ce70c303) · [状态效果 S-94bda84f6830039b](../../evidence/state_effects-sets-032.md#s-94bda84f6830039b)

### observed_connections-001268

```text
(config-router-af)# default import l2vpn evpn <cr>
```

Handler ` RVA 0xF08DFA0 `；selector ` 0 `；EOL ` RVA 0x34491750 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-61c731c081b14a36](../../evidence/conditions-sets-038.md#c-61c731c081b14a36) · [状态效果 S-86daa0ba3ab15954](../../evidence/state_effects-sets-029.md#s-86daa0ba3ab15954)

### observed_connections-001138

```text
(config-router-af)# default import nhrp <cr>
```

Handler ` RVA 0xF263450 `；selector ` 0 `；EOL ` RVA 0x34491B30 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-022e7f206a625e26](../../evidence/conditions-sets-001.md#c-022e7f206a625e26) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001266

```text
(config-router-af)# default import vpnv4 unicast <cr>
```

Handler ` RVA 0xF08E500 `；selector ` 0 `；EOL ` RVA 0x344911E0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-cc52b7d9e19edc6f](../../evidence/conditions-sets-079.md#c-cc52b7d9e19edc6f) · [状态效果 S-73fe16af8f5253f8](../../evidence/state_effects-sets-025.md#s-73fe16af8f5253f8)

### observed_connections-001024

```text
(config-router-af)# default input-queue <cr>
```

Handler ` RVA 0xE1F8060 `；selector ` 0 `；EOL ` RVA 0x344F51A8 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c4824c7cac4b28be](../../evidence/conditions-sets-076.md#c-c4824c7cac4b28be) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001142

```text
(config-router-af)# default label mode <cr>
```

Handler ` RVA 0xF1D1A30 `；selector ` 0 `；EOL ` RVA 0x344F20C8 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5cf0aca29de8310d](../../evidence/conditions-sets-036.md#c-5cf0aca29de8310d) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001058

```text
(config-router-af)# default maximum-paths <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 8 `；EOL ` RVA 0x3552D6D8 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-83cfb67834f65d1d](../../evidence/conditions-sets-051.md#c-83cfb67834f65d1d) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001150

```text
(config-router-af)# default metric holddown <cr>
```

Handler ` RVA 0xE1F32D0 `；selector ` 1 `；EOL ` RVA 0x344F3AF0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4bbe96da81617452](../../evidence/conditions-sets-030.md#c-4bbe96da81617452) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001078

```text
(config-router-af)# default metric maximum-hops <cr>
```

Handler ` RVA 0xE1F32D0 `；selector ` 2 `；EOL ` RVA 0x344F3B18 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8221b40cbcf421f4](../../evidence/conditions-sets-050.md#c-8221b40cbcf421f4) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001173

```text
(config-router-af)# default metric weights <cr>
```

Handler ` RVA 0xE1F32D0 `；selector ` 0 `；EOL ` RVA 0x344F40D8 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-74aaeceddc53dc5d](../../evidence/conditions-sets-045.md#c-74aaeceddc53dc5d) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001259

```text
(config-router-af)# default mvpn export map <cr>
```

Handler ` RVA 0xF1B79F0 `；selector ` 0 `；EOL ` RVA 0x3448FF20 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-dd6e8b4efe3a069b](../../evidence/conditions-sets-085.md#c-dd6e8b4efe3a069b) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001257

```text
(config-router-af)# default mvpn single-forwarder-selection highest-ip-address <cr>
```

Handler ` RVA 0xF1B6280 `；selector ` 0 `；EOL ` RVA 0x3448FB98 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f2bd8d01d9b37a71](../../evidence/conditions-sets-094.md#c-f2bd8d01d9b37a71) · [状态效果 S-2c30503d50cbdb14](../../evidence/state_effects-sets-010.md#s-2c30503d50cbdb14)

### observed_connections-001271

```text
(config-router-af)# default offset-list <number:0..99> in <cr>
```

Handler ` RVA 0xE1F1330 `；selector ` 0 `；EOL ` RVA 0x344F1278 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Access list of networks to apply offset (0 selects all networks)。

[条件 C-b7414ba60af25c7b](../../evidence/conditions-sets-071.md#c-b7414ba60af25c7b) · [参数 P-583d525582bab90e](../../evidence/parameters-sets-007.md#p-583d525582bab90e) · [状态效果 S-0ce2a299c7164615](../../evidence/state_effects-sets-003.md#s-0ce2a299c7164615)

### observed_connections-001014

```text
(config-router-af)# default output-delay <cr>
```

Handler ` RVA 0xE1F4590 `；selector ` 0 `；EOL ` RVA 0x344F0CD0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-75b85446d28e76e2](../../evidence/conditions-sets-046.md#c-75b85446d28e76e2) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001135

```text
(config-router-af)# default passive-interface default <cr>
```

Handler ` RVA 0xE1F3960 `；selector ` 0 `；EOL ` RVA 0x344F08C0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-66b93bc17fdac1bf](../../evidence/conditions-sets-040.md#c-66b93bc17fdac1bf) · [状态效果 S-09f97efa98f61c23](../../evidence/state_effects-sets-003.md#s-09f97efa98f61c23)

### observed_connections-001060

```text
(config-router-af)# default propagate-aspath <cr>
```

Handler ` RVA 0xF1D1560 `；selector ` 1 `；EOL ` RVA 0x344F1A40 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f1958560caef3b6e](../../evidence/conditions-sets-093.md#c-f1958560caef3b6e) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001064

```text
(config-router-af)# default propagate-community <cr>
```

Handler ` RVA 0xF1D1560 `；selector ` 2 `；EOL ` RVA 0x344F1CE8 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f1958560caef3b6e](../../evidence/conditions-sets-093.md#c-f1958560caef3b6e) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001034

```text
(config-router-af)# default redistribute <cr>
```

Handler ` RVA 0xF013680 `；selector ` 0 `；EOL ` RVA 0x344A8848 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2950acac25a26c6c](../../evidence/conditions-sets-016.md#c-2950acac25a26c6c) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001114

```text
(config-router-af)# default redistribute maximum-prefix <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 5 `；EOL ` RVA 0x3552A1B0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4f3adb05292f668a](../../evidence/conditions-sets-031.md#c-4f3adb05292f668a) · [状态效果 S-6843f3af0903e14b](../../evidence/state_effects-sets-022.md#s-6843f3af0903e14b)

### observed_connections-001133

```text
(config-router-af)# default redistribute maximum-prefix <cr>
```

Handler ` RVA 0xE1E4550 `；selector ` 0 `；EOL ` RVA 0x344ED8B8 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4aeb6ea7334e51cb](../../evidence/conditions-sets-029.md#c-4aeb6ea7334e51cb) · [状态效果 S-752e4a174df5a403](../../evidence/state_effects-sets-025.md#s-752e4a174df5a403)

### observed_connections-001122

```text
(config-router-af)# default snmp context <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 0 `；EOL ` RVA 0x33C455F0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7598dc8aeb3669dc](../../evidence/conditions-sets-046.md#c-7598dc8aeb3669dc) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001397

```text
(config-router-af)# default snmp context <string> community <string> <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 2 `；EOL ` RVA 0x33C45118 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Context Name；` string ` SNMP community string。

[条件 C-2573c969c66067b6](../../evidence/conditions-sets-015.md#c-2573c969c66067b6) · [参数 P-9b6eb89831feec60](../../evidence/parameters-sets-012.md#p-9b6eb89831feec60) · [状态效果 S-280f0e5af45d14ab](../../evidence/state_effects-sets-009.md#s-280f0e5af45d14ab)

### observed_connections-001396

```text
(config-router-af)# default snmp context <string> user <string> <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 23 `；EOL ` RVA 0x33C456D0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Context Name；` string ` Name of the user。

[条件 C-67e2e80e2c1c144d](../../evidence/conditions-sets-040.md#c-67e2e80e2c1c144d) · [参数 P-cfc42ec8ad667e32](../../evidence/parameters-sets-016.md#p-cfc42ec8ad667e32) · [状态效果 S-d526c66a74e5c8c3](../../evidence/state_effects-sets-045.md#s-d526c66a74e5c8c3)

### observed_connections-001264

```text
(config-router-af)# default summary-prefix <address> <address> <cr>
```

Handler ` RVA 0xE1DF4C0 `；selector ` 0 `；EOL ` RVA 0x344ECB38 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IP summary address；` address ` Summary mask。

[条件 C-2cd36336053d115f](../../evidence/conditions-sets-018.md#c-2cd36336053d115f) · [参数 P-aebe586c61a4934d](../../evidence/parameters-sets-013.md#p-aebe586c61a4934d) · [状态效果 S-cc1f6eff8aa9f03e](../../evidence/state_effects-sets-043.md#s-cc1f6eff8aa9f03e)

### observed_connections-001130

```text
(config-router-af)# default summary-prefix <address> <cr>
```

Handler ` RVA 0xE1DF4C0 `；selector ` 21 `；EOL ` RVA 0x344ED118 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IP summary address。

[条件 C-1a963b03b7350236](../../evidence/conditions-sets-010.md#c-1a963b03b7350236) · [参数 P-b5381e36e4d9d9b2](../../evidence/parameters-sets-014.md#p-b5381e36e4d9d9b2) · [状态效果 S-cc1f6eff8aa9f03e](../../evidence/state_effects-sets-043.md#s-cc1f6eff8aa9f03e)

### observed_connections-001037

```text
(config-router-af)# default synchronization <cr>
```

Handler ` RVA 0xF1CF320 `；selector ` 0 `；EOL ` RVA 0x3552D0E8 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-554622deff07851c](../../evidence/conditions-sets-033.md#c-554622deff07851c) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001055

```text
(config-router-af)# default synchronization <cr>
```

Handler ` RVA 0xF1CF320 `；selector ` 0 `；EOL ` RVA 0x34491EF0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-88444b208ef3872b](../../evidence/conditions-sets-053.md#c-88444b208ef3872b) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001049

```text
(config-router-af)# default table-map <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 17 `；EOL ` RVA 0x3552CE08 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-93a0d247a917c17c](../../evidence/conditions-sets-057.md#c-93a0d247a917c17c) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001069

```text
(config-router-af)# default table-map <cr>
```

Handler ` RVA 0xE1F4690 `；selector ` 0 `；EOL ` RVA 0x344922C8 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-08c3ec5dab739ebd](../../evidence/conditions-sets-004.md#c-08c3ec5dab739ebd) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001127

```text
(config-router-af)# default timers basic <cr>
```

Handler ` RVA 0xE1F2D60 `；selector ` 0 `；EOL ` RVA 0x344F83B0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f97c22b79dd75538](../../evidence/conditions-sets-096.md#c-f97c22b79dd75538) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001063

```text
(config-router-af)# default unicast-reachability <cr>
```

Handler ` RVA 0xF1B6430 `；selector ` 0 `；EOL ` RVA 0x34490420 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3648e36964a8fe89](../../evidence/conditions-sets-021.md#c-3648e36964a8fe89) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001040

```text
(config-router-af)# default validate-update-source <cr>
```

Handler ` RVA 0xE1FA930 `；selector ` 0 `；EOL ` RVA 0x344F7F18 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7f1cdb931fd8ad7c](../../evidence/conditions-sets-049.md#c-7f1cdb931fd8ad7c) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001048

```text
(config-router-af)# default version <cr>
```

Handler ` RVA 0xFB4F020 `；selector ` 0 `；EOL ` RVA 0x344EC5E8 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-af24935869a2b032](../../evidence/conditions-sets-068.md#c-af24935869a2b032) · [状态效果 S-700fa9b5fe9726d4](../../evidence/state_effects-sets-024.md#s-700fa9b5fe9726d4)

### observed_connections-001042

```text
(config-router-af)# default-information originate <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 6 `；EOL ` RVA 0x3552C0E0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-55ee11b1a1edf64f](../../evidence/conditions-sets-034.md#c-55ee11b1a1edf64f)

### observed_connections-001093

```text
(config-router-af)# default-information originate <cr>
```

Handler ` RVA 0xE1F1F70 `；selector ` 0 `；EOL ` RVA 0x344F59A8 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a9575d4774f8de5d](../../evidence/conditions-sets-065.md#c-a9575d4774f8de5d) · [状态效果 S-5d6c1fc095b9a969](../../evidence/state_effects-sets-020.md#s-5d6c1fc095b9a969)

### observed_connections-001052

```text
(config-router-af)# default-metric <number:1..16777214> <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 12 `；EOL ` RVA 0x3552C878 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Default metric。

[条件 C-239a1db2f6a454ef](../../evidence/conditions-sets-014.md#c-239a1db2f6a454ef) · [参数 P-c2531ab199b4b1f6](../../evidence/parameters-sets-015.md#p-c2531ab199b4b1f6)

### observed_connections-001096

```text
(config-router-af)# default-metric <number:1..16777214> <cr>
```

Handler ` RVA 0xE1F35A0 `；selector ` 0 `；EOL ` RVA 0x344F6270 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` OSPF default metric。

[条件 C-94b0514c823ae0a4](../../evidence/conditions-sets-057.md#c-94b0514c823ae0a4) · [参数 P-fc483cf9a933f3c9](../../evidence/parameters-sets-019.md#p-fc483cf9a933f3c9)

### observed_connections-001011

```text
(config-router-af)# distance <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 9 `；EOL ` RVA 0x35530D38 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-256dbeabc9b99bbc](../../evidence/conditions-sets-015.md#c-256dbeabc9b99bbc)

### observed_connections-001468

```text
(config-router-af)# distance <number:1..254> <prefix:dynamic> <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 9 `；EOL ` RVA 0x35530D38 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Administrative distance；` prefix_dynamic ` Prefix to match source address。

[条件 C-18d6b1239092a50b](../../evidence/conditions-sets-010.md#c-18d6b1239092a50b) · [缺口 G-eecffcd56bc7cfdb](../../evidence/gaps-sets-008.md#g-eecffcd56bc7cfdb) · [参数 P-bd3a5e21944b3045](../../evidence/parameters-sets-014.md#p-bd3a5e21944b3045) · [状态效果 S-6a07357f55e9d8ad](../../evidence/state_effects-sets-023.md#s-6a07357f55e9d8ad)

### observed_connections-001098

```text
(config-router-af)# distance <number:1..255> <cr>
```

Handler ` RVA 0xE1E3290 `；selector ` 1 `；EOL ` RVA 0x344F73A0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Administrative distance。

[条件 C-fa4013929c785873](../../evidence/conditions-sets-097.md#c-fa4013929c785873) · [参数 P-93d0335cadd4fa38](../../evidence/parameters-sets-011.md#p-93d0335cadd4fa38)

### observed_connections-001340

```text
(config-router-af)# distance bgp <number:1..255> <number:1..255> <number:1..255> <cr>
```

Handler ` RVA 0xF1B8400 `；selector ` 1 `；EOL ` RVA 0x355310F8 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Distance for routes external to the AS；` unsigned_number ` Distance for routes internal to the AS；` unsigned_number ` Distance for local routes。

[条件 C-5a3a0f9e6964f60e](../../evidence/conditions-sets-035.md#c-5a3a0f9e6964f60e) · [参数 P-63e95ae76c81c7cb](../../evidence/parameters-sets-008.md#p-63e95ae76c81c7cb)

### observed_connections-001377

```text
(config-router-af)# distance bgp <number:1..255> <number:1..255> <number:1..255> <cr>
```

Handler ` RVA 0xF1B8400 `；selector ` 1 `；EOL ` RVA 0x344E1458 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Distance for routes external to the AS；` unsigned_number ` Distance for routes internal to the AS；` unsigned_number ` Distance for local routes。

[条件 C-58f37f679a5a994b](../../evidence/conditions-sets-035.md#c-58f37f679a5a994b) · [参数 P-da75e935134966de](../../evidence/parameters-sets-016.md#p-da75e935134966de)

### observed_connections-001341

```text
(config-router-af)# distance mbgp <number:0..255> <number:0..255> <number:0..255> <cr>
```

Handler ` RVA 0xF1B8400 `；selector ` 2 `；EOL ` RVA 0x355314F0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Distance for routes external to the AS；` unsigned_number ` Distance for routes internal to the AS；` unsigned_number ` Distance for local routes。

[条件 C-81329e1c160d98ea](../../evidence/conditions-sets-050.md#c-81329e1c160d98ea) · [参数 P-958f1b1c611914c9](../../evidence/parameters-sets-011.md#p-958f1b1c611914c9)

### observed_connections-001380

```text
(config-router-af)# distance mbgp <number:0..255> <number:0..255> <number:0..255> <cr>
```

Handler ` RVA 0xF1B8400 `；selector ` 2 `；EOL ` RVA 0x344E1850 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Distance for routes external to the AS；` unsigned_number ` Distance for routes internal to the AS；` unsigned_number ` Distance for local routes。

[条件 C-d85a73f5e0afe600](../../evidence/conditions-sets-083.md#c-d85a73f5e0afe600) · [参数 P-fe1448f258db0f35](../../evidence/parameters-sets-019.md#p-fe1448f258db0f35)

### observed_connections-001103

```text
(config-router-af)# distribute-list in <cr>
```

Handler ` RVA 0xE1EE180 `；selector ` 0 `；EOL ` RVA 0x344F6960 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ea8c888fa5896889](../../evidence/conditions-sets-091.md#c-ea8c888fa5896889) · [状态效果 S-ab5262da43f039dd](../../evidence/state_effects-sets-036.md#s-ab5262da43f039dd)

### observed_connections-001474

```text
(config-router-af)# distribute-list out <?router_action_proc_vpn@555589a4a8e8> <cr>
```

Handler ` RVA 0xE1EE180 `；selector ` 0 `；EOL ` RVA 0x344F6960 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f2a9fe0c9ea0a6f4](../../evidence/conditions-sets-094.md#c-f2a9fe0c9ea0a6f4) · [缺口 G-2e21ce0a3cebe79d](../../evidence/gaps-sets-002.md#g-2e21ce0a3cebe79d) · [状态效果 S-1aa6b36ada32d509](../../evidence/state_effects-sets-006.md#s-1aa6b36ada32d509)

### observed_connections-001467

```text
(config-router-af)# domain-distinguisher <?bgp_as4_action@5555899e31b8> <number:1..2147483647> <cr>
```

Handler ` RVA 0xF1D1870 `；selector ` 0 `；EOL ` RVA 0x3448F1E0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` LS-ID in 32 bit quantity。

[条件 C-31565b867c17cecb](../../evidence/conditions-sets-019.md#c-31565b867c17cecb) · [缺口 G-8012cc49821a9bab](../../evidence/gaps-sets-005.md#g-8012cc49821a9bab) · [参数 P-c2b9c420aece4f58](../../evidence/parameters-sets-015.md#p-c2b9c420aece4f58)

### observed_connections-001008

```text
(config-router-af)# exit-address-family <cr>
```

Handler ` RVA 0xE1A0ED0 `；selector ` 0 `；EOL ` RVA 0x344A8480 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-279072590886b5ba](../../evidence/conditions-sets-016.md#c-279072590886b5ba)

### observed_connections-001007

```text
(config-router-af)# flash-update-threshold <number:0..30> <cr>
```

Handler ` RVA 0xE1F7ED0 `；selector ` 0 `；EOL ` RVA 0x344F5498 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` threshold in seconds。

[条件 C-a987807880c47e2b](../../evidence/conditions-sets-065.md#c-a987807880c47e2b) · [参数 P-a2345e205347a59e](../../evidence/parameters-sets-012.md#p-a2345e205347a59e)

### observed_connections-001021

```text
(config-router-af)# import <cr>
```

Handler ` RVA 0xF08D6A0 `；selector ` 0 `；EOL ` RVA 0x344909D0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f66640e5ce70c303](../../evidence/conditions-sets-095.md#c-f66640e5ce70c303) · [状态效果 S-f16d4b4650746657](../../evidence/state_effects-sets-051.md#s-f16d4b4650746657)

### observed_connections-001136

```text
(config-router-af)# import l2vpn evpn <cr>
```

Handler ` RVA 0xF08DFA0 `；selector ` 0 `；EOL ` RVA 0x34491750 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-61c731c081b14a36](../../evidence/conditions-sets-038.md#c-61c731c081b14a36) · [状态效果 S-655dbbd91ac7fcbe](../../evidence/state_effects-sets-022.md#s-655dbbd91ac7fcbe)

### observed_connections-001066

```text
(config-router-af)# import nhrp <cr>
```

Handler ` RVA 0xF263450 `；selector ` 0 `；EOL ` RVA 0x34491B30 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-022e7f206a625e26](../../evidence/conditions-sets-001.md#c-022e7f206a625e26)

### observed_connections-001496

```text
(config-router-af)# import path selection <?option@5555899e4cb8> <cr>
```

Handler ` RVA 0xF08D6A0 `；selector ` 0 `；EOL ` RVA 0x344909D0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-939db6506b5fa843](../../evidence/conditions-sets-057.md#c-939db6506b5fa843) · [缺口 G-c0569e3bf687b247](../../evidence/gaps-sets-007.md#g-c0569e3bf687b247) · [状态效果 S-329cf918388086d4](../../evidence/state_effects-sets-011.md#s-329cf918388086d4)

### observed_connections-001134

```text
(config-router-af)# import vpnv4 unicast <cr>
```

Handler ` RVA 0xF08E500 `；selector ` 0 `；EOL ` RVA 0x344911E0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cc52b7d9e19edc6f](../../evidence/conditions-sets-079.md#c-cc52b7d9e19edc6f) · [状态效果 S-3472a7cb7d4684b1](../../evidence/state_effects-sets-012.md#s-3472a7cb7d4684b1)

### observed_connections-001006

```text
(config-router-af)# input-queue <number:0..1024> <cr>
```

Handler ` RVA 0xE1F8060 `；selector ` 0 `；EOL ` RVA 0x344F51A8 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` queue depth。

[条件 C-9fd5ba85a10ee162](../../evidence/conditions-sets-062.md#c-9fd5ba85a10ee162) · [参数 P-5267c0140d4e52a7](../../evidence/parameters-sets-007.md#p-5267c0140d4e52a7)

### observed_connections-001470

```text
(config-router-af)# label mode all-explicit-null <cr>
```

Handler ` RVA 0xF1D1A30 `；selector ` 2 `；EOL ` RVA 0x344F2410 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-196d3da51f3953c9](../../evidence/conditions-sets-010.md#c-196d3da51f3953c9) · [缺口 G-dc64f1c5cb22dabb](../../evidence/gaps-sets-008.md#g-dc64f1c5cb22dabb) · [状态效果 S-a45599ec6583c65b](../../evidence/state_effects-sets-035.md#s-a45599ec6583c65b)

### observed_connections-001469

```text
(config-router-af)# label mode explicit-null <cr>
```

Handler ` RVA 0xF1D1A30 `；selector ` 1 `；EOL ` RVA 0x344F2158 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-196d3da51f3953c9](../../evidence/conditions-sets-010.md#c-196d3da51f3953c9) · [缺口 G-6ace9773ef4ef6df](../../evidence/gaps-sets-004.md#g-6ace9773ef4ef6df) · [状态效果 S-8bd26dbd0a18e1e8](../../evidence/state_effects-sets-030.md#s-8bd26dbd0a18e1e8)

### observed_connections-001016

```text
(config-router-af)# maximum-paths <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 8 `；EOL ` RVA 0x3552D6D8 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-83cfb67834f65d1d](../../evidence/conditions-sets-051.md#c-83cfb67834f65d1d)

### observed_connections-001427

```text
(config-router-af)# maximum-paths <number:dynamic> <cr>
```

Handler ` RVA 0xE1E26B0 `；selector ` 0 `；EOL ` RVA 0x344F4CC0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Number of paths。

[条件 C-c4d2c8b573521027](../../evidence/conditions-sets-076.md#c-c4d2c8b573521027) · [缺口 G-d1981088f6fbd147](../../evidence/gaps-sets-007.md#g-d1981088f6fbd147) · [参数 P-aa581bb178e213f9](../../evidence/parameters-sets-013.md#p-aa581bb178e213f9)

### observed_connections-001426

```text
(config-router-af)# maximum-secondary-paths <number:dynamic> <cr>
```

Handler ` RVA 0xE1E2BD0 `；selector ` 0 `；EOL ` RVA 0x344F4758 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Number of secondary paths。

[条件 C-61ee179365919407](../../evidence/conditions-sets-038.md#c-61ee179365919407) · [缺口 G-19a9bd177250c456](../../evidence/gaps-sets-001.md#g-19a9bd177250c456) · [参数 P-20172f83589f021e](../../evidence/parameters-sets-003.md#p-20172f83589f021e)

### observed_connections-001074

```text
(config-router-af)# metric holddown <cr>
```

Handler ` RVA 0xE1F32D0 `；selector ` 1 `；EOL ` RVA 0x344F3AF0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4bbe96da81617452](../../evidence/conditions-sets-030.md#c-4bbe96da81617452)

### observed_connections-001022

```text
(config-router-af)# metric maximum-hops <number:1..255> <cr>
```

Handler ` RVA 0xE1F32D0 `；selector ` 2 `；EOL ` RVA 0x344F3B18 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Hop count。

[条件 C-4f06080100d9aa31](../../evidence/conditions-sets-031.md#c-4f06080100d9aa31) · [参数 P-ade92f03be8d75a4](../../evidence/parameters-sets-013.md#p-ade92f03be8d75a4)

### observed_connections-001410

```text
(config-router-af)# metric weights <number:0..8> <number:0..255> <number:0..255> <number:0..255> <number:0..255> <number:0..255> <cr>
```

Handler ` RVA 0xE1F32D0 `；selector ` 0 `；EOL ` RVA 0x344F40D8 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Type Of Service (Only TOS 0 supported)；` unsigned_number ` K1；` unsigned_number ` K2；` unsigned_number ` K3；` unsigned_number ` K4；` unsigned_number ` K5。

[条件 C-d7dd7842e679d454](../../evidence/conditions-sets-083.md#c-d7dd7842e679d454) · [参数 P-814573c6aff87ec0](../../evidence/parameters-sets-010.md#p-814573c6aff87ec0)

### observed_connections-001261

```text
(config-router-af)# mvpn export map <string> <cr>
```

Handler ` RVA 0xF1B79F0 `；selector ` 0 `；EOL ` RVA 0x3448FF20 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` MVPN export route-map name。

[条件 C-8e3ebacddfcec9ab](../../evidence/conditions-sets-055.md#c-8e3ebacddfcec9ab) · [参数 P-f32579c89e83d985](../../evidence/parameters-sets-018.md#p-f32579c89e83d985)

### observed_connections-001117

```text
(config-router-af)# mvpn single-forwarder-selection highest-ip-address <cr>
```

Handler ` RVA 0xF1B6280 `；selector ` 0 `；EOL ` RVA 0x3448FB98 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f2bd8d01d9b37a71](../../evidence/conditions-sets-094.md#c-f2bd8d01d9b37a71) · [状态效果 S-93a79979571a05df](../../evidence/state_effects-sets-031.md#s-93a79979571a05df)

### observed_connections-001415

```text
(config-router-af)# neighbor <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 0 `；EOL ` RVA 0x344FAE30 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-13bab7a73be6995a](../../evidence/conditions-sets-008.md#c-13bab7a73be6995a) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001417

```text
(config-router-af)# neighbor <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 0 `；EOL ` RVA 0x34514EB0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1c96f9a1eaa0749d](../../evidence/conditions-sets-011.md#c-1c96f9a1eaa0749d) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001451

```text
(config-router-af)# neighbor accept-route-legacy-rt <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 71 `；EOL ` RVA 0x3450FCA0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-60e9cf81e8aa848e](../../evidence/conditions-sets-038.md#c-60e9cf81e8aa848e) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001457

```text
(config-router-af)# neighbor activate <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 35 `；EOL ` RVA 0x34512F58 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ad8ccca0d04a9c9e](../../evidence/conditions-sets-067.md#c-ad8ccca0d04a9c9e) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001454

```text
(config-router-af)# neighbor additional-paths <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 79 `；EOL ` RVA 0x34510680 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c21872e8d31dd697](../../evidence/conditions-sets-075.md#c-c21872e8d31dd697) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-310f72b0202c01f0](../../evidence/state_effects-sets-011.md#s-310f72b0202c01f0)

### observed_connections-001487

```text
(config-router-af)# neighbor advertise additional-paths <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 78 `；EOL ` RVA 0x34510D88 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-192897edda681854](../../evidence/conditions-sets-010.md#c-192897edda681854) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-f5e7703a312d3e8e](../../evidence/state_effects-sets-052.md#s-f5e7703a312d3e8e)

### observed_connections-001485

```text
(config-router-af)# neighbor advertise best-external <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 80 `；EOL ` RVA 0x34511438 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e02361fb7eb19d65](../../evidence/conditions-sets-086.md#c-e02361fb7eb19d65) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001511

```text
(config-router-af)# neighbor advertise diverse-path mpath <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 78 `；EOL ` RVA 0x34511158 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e02361fb7eb19d65](../../evidence/conditions-sets-086.md#c-e02361fb7eb19d65) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-bb007f0b56515910](../../evidence/state_effects-sets-039.md#s-bb007f0b56515910)

### observed_connections-001465

```text
(config-router-af)# neighbor advertise-gw-ip-disable <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 88 `；EOL ` RVA 0x34517350 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-919986923aaf465d](../../evidence/conditions-sets-056.md#c-919986923aaf465d) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001515

```text
(config-router-af)# neighbor advertise-map <string> non-exist-map <string> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 39 `；EOL ` RVA 0x34513788 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` advertise route-map name；` string ` condition route-map name。

[条件 C-f0f800ded2b1c519](../../evidence/conditions-sets-093.md#c-f0f800ded2b1c519) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [参数 P-5700454f0b4c63c1](../../evidence/parameters-sets-007.md#p-5700454f0b4c63c1) · [状态效果 S-beeff3187c70c5dc](../../evidence/state_effects-sets-040.md#s-beeff3187c70c5dc)

### observed_connections-001442

```text
(config-router-af)# neighbor advertisement-interval <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 40 `；EOL ` RVA 0x3450B210 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-197ad609ce2b0755](../../evidence/conditions-sets-010.md#c-197ad609ce2b0755) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001452

```text
(config-router-af)# neighbor aigp <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 50 `；EOL ` RVA 0x3450F8A0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d24ccc0a4da823d3](../../evidence/conditions-sets-081.md#c-d24ccc0a4da823d3) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-77488c72b6e8ed60](../../evidence/state_effects-sets-025.md#s-77488c72b6e8ed60)

### observed_connections-001453

```text
(config-router-af)# neighbor allow-policy <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 51 `；EOL ` RVA 0x345102D0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-171e78d3b71fbcbf](../../evidence/conditions-sets-009.md#c-171e78d3b71fbcbf) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001438

```text
(config-router-af)# neighbor allowas-in <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 60 `；EOL ` RVA 0x34509FA8 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8f00fb7563a28c95](../../evidence/conditions-sets-055.md#c-8f00fb7563a28c95) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001505

```text
(config-router-af)# neighbor announce rpki state <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 77 `；EOL ` RVA 0x3450A798 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e691aedb1d2d97bd](../../evidence/conditions-sets-089.md#c-e691aedb1d2d97bd) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001491

```text
(config-router-af)# neighbor ao <string> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 22 `；EOL ` RVA 0x345163A0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Keychain name。

[条件 C-a2611dcb8d2ee112](../../evidence/conditions-sets-063.md#c-a2611dcb8d2ee112) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [参数 P-da5db2abf7b4d80d](../../evidence/parameters-sets-016.md#p-da5db2abf7b4d80d) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001460

```text
(config-router-af)# neighbor as-override <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 61 `；EOL ` RVA 0x34514238 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c8ab98fc01ef13fe](../../evidence/conditions-sets-077.md#c-c8ab98fc01ef13fe) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001516

```text
(config-router-af)# neighbor capability orf prefix-list send <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 65 `；EOL ` RVA 0x34514680 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8b97c64536681f4e](../../evidence/conditions-sets-054.md#c-8b97c64536681f4e) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-bc48cf26c3524396](../../evidence/state_effects-sets-040.md#s-bc48cf26c3524396)

### observed_connections-001462

```text
(config-router-af)# neighbor cluster-id <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 23 `；EOL ` RVA 0x34516768 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6ea8a4d8120fe344](../../evidence/conditions-sets-043.md#c-6ea8a4d8120fe344) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001447

```text
(config-router-af)# neighbor default-originate <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 52 `；EOL ` RVA 0x3450DCD0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-232002e2b94e88a8](../../evidence/conditions-sets-014.md#c-232002e2b94e88a8) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001456

```text
(config-router-af)# neighbor description <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 8 `；EOL ` RVA 0x34512C20 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e88517045e0c013f](../../evidence/conditions-sets-090.md#c-e88517045e0c013f) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001436

```text
(config-router-af)# neighbor disable-connected-check <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 13 `；EOL ` RVA 0x34509318 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-10dd06267d084e20](../../evidence/conditions-sets-007.md#c-10dd06267d084e20) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-9f0d6cbe68a958da](../../evidence/state_effects-sets-034.md#s-9f0d6cbe68a958da)

### observed_connections-001501

```text
(config-router-af)# neighbor distribute-list <number:1..199> in <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 45 `；EOL ` RVA 0x345064A0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` IP access list number。

[条件 C-d9c9086da3f4ebe4](../../evidence/conditions-sets-084.md#c-d9c9086da3f4ebe4) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [参数 P-0797f33209a82d83](../../evidence/parameters-sets-001.md#p-0797f33209a82d83) · [状态效果 S-abc7de4585cab362](../../evidence/state_effects-sets-036.md#s-abc7de4585cab362)

### observed_connections-001434

```text
(config-router-af)# neighbor dmzlink-bw <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 63 `；EOL ` RVA 0x34507DA0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8571c652afdb9a9f](../../evidence/conditions-sets-052.md#c-8571c652afdb9a9f) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-cccb14bcb9ec38cb](../../evidence/state_effects-sets-043.md#s-cccb14bcb9ec38cb)

### observed_connections-001431

```text
(config-router-af)# neighbor dont-capability-negotiate <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 16 `；EOL ` RVA 0x34505060 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e58430b9c4f0f9ae](../../evidence/conditions-sets-089.md#c-e58430b9c4f0f9ae) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001473

```text
(config-router-af)# neighbor dont-capability-negotiate enhanced-refresh <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 18 `；EOL ` RVA 0x34505038 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e58430b9c4f0f9ae](../../evidence/conditions-sets-089.md#c-e58430b9c4f0f9ae) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001471

```text
(config-router-af)# neighbor dont-capability-negotiate four-octets-as <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 17 `；EOL ` RVA 0x34504D90 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e58430b9c4f0f9ae](../../evidence/conditions-sets-089.md#c-e58430b9c4f0f9ae) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001446

```text
(config-router-af)# neighbor ebgp-multihop <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 6 `；EOL ` RVA 0x3450D8A8 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-77b29bcbf6938ac1](../../evidence/conditions-sets-047.md#c-77b29bcbf6938ac1) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-147c8497d59aab13](../../evidence/state_effects-sets-005.md#s-147c8497d59aab13)

### observed_connections-001492

```text
(config-router-af)# neighbor encap srv6 <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 86 `；EOL ` RVA 0x34517778 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4cd15865852f0942](../../evidence/conditions-sets-030.md#c-4cd15865852f0942) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-ce3e01bc3a1db752](../../evidence/state_effects-sets-044.md#s-ce3e01bc3a1db752)

### observed_connections-001439

```text
(config-router-af)# neighbor fall-over <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 26 `；EOL ` RVA 0x34509670 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-03fa6bb6e2648f91](../../evidence/conditions-sets-002.md#c-03fa6bb6e2648f91) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-ea869f48fdbad9a6](../../evidence/state_effects-sets-050.md#s-ea869f48fdbad9a6)

### observed_connections-001504

```text
(config-router-af)# neighbor filter-list <number:1..500> in <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 44 `；EOL ` RVA 0x34507280 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` AS path access list。

[条件 C-eeeedb84ea6e6a17](../../evidence/conditions-sets-092.md#c-eeeedb84ea6e6a17) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [参数 P-32386b885f3a56a1](../../evidence/parameters-sets-004.md#p-32386b885f3a56a1) · [状态效果 S-30faed4ccbccec2e](../../evidence/state_effects-sets-011.md#s-30faed4ccbccec2e)

### observed_connections-001430

```text
(config-router-af)# neighbor force-open-collision <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 15 `；EOL ` RVA 0x345055F0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-289a431576c5a2de](../../evidence/conditions-sets-016.md#c-289a431576c5a2de) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001494

```text
(config-router-af)# neighbor ha-mode graceful-restart <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 28 `；EOL ` RVA 0x344FB150 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7e41f7d7f62c88c6](../../evidence/conditions-sets-049.md#c-7e41f7d7f62c88c6) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001495

```text
(config-router-af)# neighbor ha-mode sso <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 29 `；EOL ` RVA 0x3372E478 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7e41f7d7f62c88c6](../../evidence/conditions-sets-049.md#c-7e41f7d7f62c88c6) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001510

```text
(config-router-af)# neighbor inherit peer-policy <string> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 36 `；EOL ` RVA 0x345118B0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Template name。

[条件 C-cbdd0eedb1248b5c](../../evidence/conditions-sets-078.md#c-cbdd0eedb1248b5c) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [参数 P-830038faf9dd3fd6](../../evidence/parameters-sets-010.md#p-830038faf9dd3fd6) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001509

```text
(config-router-af)# neighbor inherit peer-session <string> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 19 `；EOL ` RVA 0x34511BC8 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Template name。

[条件 C-c0ab4d89634c404f](../../evidence/conditions-sets-074.md#c-c0ab4d89634c404f) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [参数 P-0e28cc940f3097c3](../../evidence/parameters-sets-002.md#p-0e28cc940f3097c3) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001449

```text
(config-router-af)# neighbor inter-as-hybrid <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 72 `；EOL ` RVA 0x3450F280 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-225a9309aed7568c](../../evidence/conditions-sets-013.md#c-225a9309aed7568c) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001459

```text
(config-router-af)# neighbor internal-vpn-client <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 82 `；EOL ` RVA 0x34513E80 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-358884266787c0b1](../../evidence/conditions-sets-021.md#c-358884266787c0b1) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001437

```text
(config-router-af)# neighbor local-as <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 11 `；EOL ` RVA 0x34508EA0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a3c15a1e7ce2c66b](../../evidence/conditions-sets-063.md#c-a3c15a1e7ce2c66b) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001466

```text
(config-router-af)# neighbor log-neighbor-changes <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 32 `；EOL ` RVA 0x34517FB0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6404bb904798fc4d](../../evidence/conditions-sets-039.md#c-6404bb904798fc4d) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001464

```text
(config-router-af)# neighbor long-lived-graceful-restart <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 85 `；EOL ` RVA 0x34516B88 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9d9516f08ea397fc](../../evidence/conditions-sets-061.md#c-9d9516f08ea397fc) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001486

```text
(config-router-af)# neighbor maximum-prefix <number:1..2147483647> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 59 `；EOL ` RVA 0x34512728 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` maximum no. of prefix limit。

[条件 C-3d591c7f1e356b3f](../../evidence/conditions-sets-024.md#c-3d591c7f1e356b3f) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [参数 P-13ee3dfd3e93b318](../../evidence/parameters-sets-002.md#p-13ee3dfd3e93b318) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001444

```text
(config-router-af)# neighbor next-hop-self <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 42 `；EOL ` RVA 0x3450C478 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f4351305e1c4a797](../../evidence/conditions-sets-094.md#c-f4351305e1c4a797) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001445

```text
(config-router-af)# neighbor next-hop-unchanged <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 43 `；EOL ` RVA 0x3450D538 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1b0c1fcf5f3d086e](../../evidence/conditions-sets-011.md#c-1b0c1fcf5f3d086e) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001475

```text
(config-router-af)# neighbor orf rt-import-list <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 70 `；EOL ` RVA 0x34506E60 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ab835ca27d439164](../../evidence/conditions-sets-066.md#c-ab835ca27d439164) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-6317e372b48e554b](../../evidence/state_effects-sets-021.md#s-6317e372b48e554b)

### observed_connections-001432

```text
(config-router-af)# neighbor override-capability-neg <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 62 `；EOL ` RVA 0x345060B8 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1e3df669ab0e3cf9](../../evidence/conditions-sets-012.md#c-1e3df669ab0e3cf9) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001455

```text
(config-router-af)# neighbor password <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 7 `；EOL ` RVA 0x345122E0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b85fedd316c09ae8](../../evidence/conditions-sets-071.md#c-b85fedd316c09ae8) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001517

```text
(config-router-af)# neighbor path-attribute treat-as-withdraw <number:1..255> in <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 27 `；EOL ` RVA 0x34515B80 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` path attribute type。

[条件 C-f6dcf8eb5c721af0](../../evidence/conditions-sets-095.md#c-f6dcf8eb5c721af0) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [参数 P-72a458c8c3022acf](../../evidence/parameters-sets-009.md#p-72a458c8c3022acf) · [状态效果 S-4ac3f2ec2d52db64](../../evidence/state_effects-sets-016.md#s-4ac3f2ec2d52db64)

### observed_connections-001428

```text
(config-router-af)# neighbor peer-group <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 10 `；EOL ` RVA 0x344E0C38 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8e4c55852a704b71](../../evidence/conditions-sets-055.md#c-8e4c55852a704b71) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001484

```text
(config-router-af)# neighbor peer-group <string> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 20 `；EOL ` RVA 0x34511F48 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` peer-group name。

[条件 C-6e258b24e0760038](../../evidence/conditions-sets-043.md#c-6e258b24e0760038) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [参数 P-52dda26f99b7df22](../../evidence/parameters-sets-007.md#p-52dda26f99b7df22) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001476

```text
(config-router-af)# neighbor prefix-length-size <number:1..2> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 68 `；EOL ` RVA 0x34507A60 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Storage size in bytes。

[条件 C-cdd2e851f00d0e15](../../evidence/conditions-sets-079.md#c-cdd2e851f00d0e15) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [参数 P-a6116061aef9ac47](../../evidence/parameters-sets-013.md#p-a6116061aef9ac47) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001502

```text
(config-router-af)# neighbor prefix-list <string> in <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 58 `；EOL ` RVA 0x34506988 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Name of a prefix list。

[条件 C-35994091da99805d](../../evidence/conditions-sets-021.md#c-35994091da99805d) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [参数 P-d19b4dab0d5c54fd](../../evidence/parameters-sets-016.md#p-d19b4dab0d5c54fd) · [状态效果 S-5405f3edeff72c73](../../evidence/state_effects-sets-018.md#s-5405f3edeff72c73)

### observed_connections-001435

```text
(config-router-af)# neighbor remote-as <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 3 `；EOL ` RVA 0x34508488 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-160911c41469c892](../../evidence/conditions-sets-009.md#c-160911c41469c892) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001448

```text
(config-router-af)# neighbor remove-private-as <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 55 `；EOL ` RVA 0x3450EA48 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3c15e60adcaa6f3e](../../evidence/conditions-sets-023.md#c-3c15e60adcaa6f3e) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001483

```text
(config-router-af)# neighbor remove-private-as all <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 56 `；EOL ` RVA 0x3450EAB0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8060cd7582c05ee1](../../evidence/conditions-sets-050.md#c-8060cd7582c05ee1) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001508

```text
(config-router-af)# neighbor remove-private-as all replace-as <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 57 `；EOL ` RVA 0x3450EA88 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8060cd7582c05ee1](../../evidence/conditions-sets-050.md#c-8060cd7582c05ee1) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001503

```text
(config-router-af)# neighbor route-map <string> in <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 47 `；EOL ` RVA 0x34507670 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Name of route map。

[条件 C-fc219d4e34260c06](../../evidence/conditions-sets-097.md#c-fc219d4e34260c06) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [参数 P-56a31330bb3dc696](../../evidence/parameters-sets-007.md#p-56a31330bb3dc696) · [状态效果 S-53f0ef09cb1c2df4](../../evidence/state_effects-sets-018.md#s-53f0ef09cb1c2df4)

### observed_connections-001450

```text
(config-router-af)# neighbor route-reflector-client <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 49 `；EOL ` RVA 0x3450FF98 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-283381432d5aa003](../../evidence/conditions-sets-016.md#c-283381432d5aa003) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001441

```text
(config-router-af)# neighbor send-community <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 46 `；EOL ` RVA 0x3450B9A8 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c4aa87ec4762d0be](../../evidence/conditions-sets-076.md#c-c4aa87ec4762d0be) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001461

```text
(config-router-af)# neighbor send-label <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 64 `；EOL ` RVA 0x34514B80 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b6f81c4e0bd5f8f5](../../evidence/conditions-sets-071.md#c-b6f81c4e0bd5f8f5) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001443

```text
(config-router-af)# neighbor shutdown <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 5 `；EOL ` RVA 0x3450BE48 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ba483e96460a8055](../../evidence/conditions-sets-072.md#c-ba483e96460a8055) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001478

```text
(config-router-af)# neighbor slow-peer detection <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 74 `；EOL ` RVA 0x3450CEF8 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8f419973a82cf608](../../evidence/conditions-sets-055.md#c-8f419973a82cf608) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001479

```text
(config-router-af)# neighbor slow-peer detection threshold <number:120..3600> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 74 `；EOL ` RVA 0x3450CF20 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Threshold value (seconds)。

[条件 C-839813b7d3861e3a](../../evidence/conditions-sets-051.md#c-839813b7d3861e3a) · [缺口 G-d75e16e85957f327](../../evidence/gaps-sets-007.md#g-d75e16e85957f327) · [参数 P-d3f734109cb70ab9](../../evidence/parameters-sets-016.md#p-d3f734109cb70ab9) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001507

```text
(config-router-af)# neighbor slow-peer split-update-group dynamic <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 75 `；EOL ` RVA 0x3450CB80 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-df6254f59b5e0e20](../../evidence/conditions-sets-086.md#c-df6254f59b5e0e20) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001506

```text
(config-router-af)# neighbor slow-peer split-update-group static <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 73 `；EOL ` RVA 0x3450C870 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4c959e4f28cdc8d7](../../evidence/conditions-sets-030.md#c-4c959e4f28cdc8d7) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001480

```text
(config-router-af)# neighbor soft-reconfiguration inbound <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 54 `；EOL ` RVA 0x3450E068 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-86b9f1025a6fe26b](../../evidence/conditions-sets-052.md#c-86b9f1025a6fe26b) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001522

```text
(config-router-af)# neighbor soo <?bgp_extcomm_action@555589a5e320> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 69 `；EOL ` RVA 0x3450A368 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5b99992805d4b839](../../evidence/conditions-sets-036.md#c-5b99992805d4b839) · [缺口 G-0e8803a0f852e018](../../evidence/gaps-sets-001.md#g-0e8803a0f852e018) · [状态效果 S-363077405b04bf7a](../../evidence/state_effects-sets-012.md#s-363077405b04bf7a)

### observed_connections-001493

```text
(config-router-af)# neighbor suppress-signaling-protocol ldp <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 81 `；EOL ` RVA 0x34517C70 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-325133a1bc3a6989](../../evidence/conditions-sets-020.md#c-325133a1bc3a6989) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001463

```text
(config-router-af)# neighbor suppress-sr <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 87 `；EOL ` RVA 0x34517018 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-05db0ec610947357](../../evidence/conditions-sets-003.md#c-05db0ec610947357) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001458

```text
(config-router-af)# neighbor timers <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 9 `；EOL ` RVA 0x345132B8 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1db3879e1ea8e79e](../../evidence/conditions-sets-012.md#c-1db3879e1ea8e79e) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001472

```text
(config-router-af)# neighbor translate-topology <number:1..4095> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 67 `；EOL ` RVA 0x34504A50 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Topology id。

[条件 C-36e4d1058431fe3e](../../evidence/conditions-sets-021.md#c-36e4d1058431fe3e) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [参数 P-29a580b5da5dc57a](../../evidence/parameters-sets-004.md#p-29a580b5da5dc57a) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001433

```text
(config-router-af)# neighbor translate-update <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 66 `；EOL ` RVA 0x34505A50 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c41cc4f8d386df01](../../evidence/conditions-sets-076.md#c-c41cc4f8d386df01) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-0fe63544651cb37c](../../evidence/state_effects-sets-004.md#s-0fe63544651cb37c)

### observed_connections-001490

```text
(config-router-af)# neighbor transport multi-session <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 25 `；EOL ` RVA 0x345155F8 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5106ca4ee508f037](../../evidence/conditions-sets-032.md#c-5106ca4ee508f037) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-2a6f12fd310e73f0](../../evidence/state_effects-sets-010.md#s-2a6f12fd310e73f0)

### observed_connections-001489

```text
(config-router-af)# neighbor transport path-mtu-discovery <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 24 `；EOL ` RVA 0x34515250 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5106ca4ee508f037](../../evidence/conditions-sets-032.md#c-5106ca4ee508f037) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-6a83e9fd912e972f](../../evidence/state_effects-sets-023.md#s-6a83e9fd912e972f)

### observed_connections-001512

```text
(config-router-af)# neighbor ttl-security hops <number:1..254> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 21 `；EOL ` RVA 0x34515F88 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` maximum number of hops。

[条件 C-07c9f5416d843d09](../../evidence/conditions-sets-003.md#c-07c9f5416d843d09) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [参数 P-8cc2c830fd88076d](../../evidence/parameters-sets-011.md#p-8cc2c830fd88076d) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001477

```text
(config-router-af)# neighbor unsuppress-map <string> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 53 `；EOL ` RVA 0x34508128 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Name of route map。

[条件 C-8e141e8fa6af9f28](../../evidence/conditions-sets-055.md#c-8e141e8fa6af9f28) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [参数 P-223c6e11c8568fdf](../../evidence/parameters-sets-003.md#p-223c6e11c8568fdf) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001518

```text
(config-router-af)# neighbor update in labeled-unicast unique <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 33 `；EOL ` RVA 0x345183D0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4d8b718999425ead](../../evidence/conditions-sets-030.md#c-4d8b718999425ead) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-7cd551f1b064b514](../../evidence/state_effects-sets-026.md#s-7cd551f1b064b514)

### observed_connections-001523

```text
(config-router-af)# neighbor update-source <interface> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 4 `；EOL ` RVA 0x3450B630 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9125e9a3c7bdde78](../../evidence/conditions-sets-056.md#c-9125e9a3c7bdde78) · [缺口 G-8daaf47d527eeec2](../../evidence/gaps-sets-005.md#g-8daaf47d527eeec2) · [参数 P-61fcc75034c55454](../../evidence/parameters-sets-008.md#p-61fcc75034c55454) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001488

```text
(config-router-af)# neighbor use nexthop-attribute <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 37 `；EOL ` RVA 0x34513B40 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3be006df4c76bad6](../../evidence/conditions-sets-023.md#c-3be006df4c76bad6) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001481

```text
(config-router-af)# neighbor validation off <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 83 `；EOL ` RVA 0x3450E3E8 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-943c3e0115be4042](../../evidence/conditions-sets-057.md#c-943c3e0115be4042) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001482

```text
(config-router-af)# neighbor validation redirect-off <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 84 `；EOL ` RVA 0x3450E690 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-943c3e0115be4042](../../evidence/conditions-sets-057.md#c-943c3e0115be4042) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001416

```text
(config-router-af)# neighbor version <number:4..4> <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 2 `；EOL ` RVA 0x3450AA40 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Neighbor's BGP version。

[条件 C-ddbd536532a30941](../../evidence/conditions-sets-085.md#c-ddbd536532a30941) · [缺口 G-42095c11b6c3a7a5](../../evidence/gaps-sets-003.md#g-42095c11b6c3a7a5) · [参数 P-db3efca0f5fa5dad](../../evidence/parameters-sets-017.md#p-db3efca0f5fa5dad) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001440

```text
(config-router-af)# neighbor weight <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 41 `；EOL ` RVA 0x3450AE38 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-033cebca76205d75](../../evidence/conditions-sets-002.md#c-033cebca76205d75) · [缺口 G-6e4f1d4b2fd53316](../../evidence/gaps-sets-004.md#g-6e4f1d4b2fd53316) · [状态效果 S-08dfe7fc8485a15b](../../evidence/state_effects-sets-002.md#s-08dfe7fc8485a15b)

### observed_connections-001425

```text
(config-router-af)# network <address> <cr>
```

Handler ` RVA 0xF190B70 `；selector ` 0 `；EOL ` RVA 0x344A7570 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` NSAP prefix。

[条件 C-f99ee61380c7688c](../../evidence/conditions-sets-096.md#c-f99ee61380c7688c) · [缺口 G-ed21266aa4a4a33a](../../evidence/gaps-sets-008.md#g-ed21266aa4a4a33a) · [参数 P-01fe2e760d4d1204](../../evidence/parameters-sets-001.md#p-01fe2e760d4d1204) · [状态效果 S-7605dfc1d9285475](../../evidence/state_effects-sets-025.md#s-7605dfc1d9285475)

### observed_connections-001521

```text
(config-router-af)# network <address> <cr>
```

Handler ` RVA 0xE1E04C0 `；selector ` 0 `；EOL ` RVA 0x344F3258 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Network number。

[条件 C-1fa7aa820c5ad426](../../evidence/conditions-sets-012.md#c-1fa7aa820c5ad426) · [缺口 G-05cb3d1521972458](../../evidence/gaps-sets-001.md#g-05cb3d1521972458) · [参数 P-bc5dfd89d0bbefc6](../../evidence/parameters-sets-014.md#p-bc5dfd89d0bbefc6) · [状态效果 S-cf0dcd14c69eda70](../../evidence/state_effects-sets-044.md#s-cf0dcd14c69eda70)

### observed_connections-001260

```text
(config-router-af)# no advertise l2vpn evpn <cr>
```

Handler ` RVA 0xF2569C0 `；selector ` 0 `；EOL ` RVA 0x3448F770 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a3c28d6a0b2a77b5](../../evidence/conditions-sets-063.md#c-a3c28d6a0b2a77b5) · [状态效果 S-31fd3289002d6b3e](../../evidence/state_effects-sets-011.md#s-31fd3289002d6b3e)

### observed_connections-001304

```text
(config-router-af)# no aggregate-address <address> <address> <cr>
```

Handler ` RVA 0xF1B7BE0 `；selector ` 0 `；EOL ` RVA 0x344A7EF0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` Aggregate address；` address ` Aggregate mask。

[条件 C-7a4e6d3a417f3e95](../../evidence/conditions-sets-047.md#c-7a4e6d3a417f3e95) · [参数 P-914e458157ad6a8f](../../evidence/parameters-sets-011.md#p-914e458157ad6a8f) · [状态效果 S-5a471470eabbe594](../../evidence/state_effects-sets-019.md#s-5a471470eabbe594)

### observed_connections-001089

```text
(config-router-af)# no auto-summary <cr>
```

Handler ` RVA 0xE1FA6B0 `；selector ` 0 `；EOL ` RVA 0x344F7B28 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-892cb3702bd56b94](../../evidence/conditions-sets-053.md#c-892cb3702bd56b94) · [状态效果 S-5a471470eabbe594](../../evidence/state_effects-sets-019.md#s-5a471470eabbe594)

### observed_connections-001291

```text
(config-router-af)# no bgp additional-paths install <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 69 `；EOL ` RVA 0x3449F770 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-928f75bb67af333f](../../evidence/conditions-sets-057.md#c-928f75bb67af333f) · [状态效果 S-601839017f51336c](../../evidence/state_effects-sets-021.md#s-601839017f51336c)

### observed_connections-001300

```text
(config-router-af)# no bgp additional-paths select <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 71 `；EOL ` RVA 0x3449F418 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4535ae221f00abe5](../../evidence/conditions-sets-027.md#c-4535ae221f00abe5) · [状态效果 S-5a471470eabbe594](../../evidence/state_effects-sets-019.md#s-5a471470eabbe594)

### observed_connections-001162

```text
(config-router-af)# no bgp advertise-best-external <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 70 `；EOL ` RVA 0x344A05C0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7657ebc5798c2d01](../../evidence/conditions-sets-046.md#c-7657ebc5798c2d01) · [状态效果 S-5a471470eabbe594](../../evidence/state_effects-sets-019.md#s-5a471470eabbe594)

### observed_connections-001217

```text
(config-router-af)# no bgp advertisement startup-delay <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 95 `；EOL ` RVA 0x34498430 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-94587e380a65b0e2](../../evidence/conditions-sets-057.md#c-94587e380a65b0e2) · [状态效果 S-5a471470eabbe594](../../evidence/state_effects-sets-019.md#s-5a471470eabbe594)

### observed_connections-001301

```text
(config-router-af)# no bgp aggregate-timer <number:6..60> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 58 `；EOL ` RVA 0x344A6610 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Timer interval。

[条件 C-5be2d964dc2681c9](../../evidence/conditions-sets-036.md#c-5be2d964dc2681c9) · [参数 P-51cebb32e63b4ca3](../../evidence/parameters-sets-007.md#p-51cebb32e63b4ca3) · [状态效果 S-5a471470eabbe594](../../evidence/state_effects-sets-019.md#s-5a471470eabbe594)

### observed_connections-001245

```text
(config-router-af)# no bgp aigp-rib-metric <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 91 `；EOL ` RVA 0x3449CEB0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-292918144cc23f5a](../../evidence/conditions-sets-016.md#c-292918144cc23f5a) · [状态效果 S-5a471470eabbe594](../../evidence/state_effects-sets-019.md#s-5a471470eabbe594)

### observed_connections-001153

```text
(config-router-af)# no bgp always-compare-med <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 5 `；EOL ` RVA 0x34493D18 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e27560d5ee3533f0](../../evidence/conditions-sets-087.md#c-e27560d5ee3533f0) · [状态效果 S-5a471470eabbe594](../../evidence/state_effects-sets-019.md#s-5a471470eabbe594)

### observed_connections-001279

```text
(config-router-af)# no bgp asnotation dot <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 64 `；EOL ` RVA 0x34494028 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e27560d5ee3533f0](../../evidence/conditions-sets-087.md#c-e27560d5ee3533f0) · [状态效果 S-5a471470eabbe594](../../evidence/state_effects-sets-019.md#s-5a471470eabbe594)

### observed_connections-001391

```text
(config-router-af)# no bgp bestpath aigp ignore <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 43 `；EOL ` RVA 0x3449BBD8 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1a37981dc0299bb4](../../evidence/conditions-sets-010.md#c-1a37981dc0299bb4) · [状态效果 S-5a471470eabbe594](../../evidence/state_effects-sets-019.md#s-5a471470eabbe594)

### observed_connections-001384

```text
(config-router-af)# no bgp bestpath as-path ignore <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 17 `；EOL ` RVA 0x3449B348 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-292918144cc23f5a](../../evidence/conditions-sets-016.md#c-292918144cc23f5a) · [状态效果 S-5a471470eabbe594](../../evidence/state_effects-sets-019.md#s-5a471470eabbe594)

### observed_connections-001386

```text
(config-router-af)# no bgp bestpath as-path multipath-relax <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 51 `；EOL ` RVA 0x3449B5F0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-292918144cc23f5a](../../evidence/conditions-sets-016.md#c-292918144cc23f5a) · [状态效果 S-5a471470eabbe594](../../evidence/state_effects-sets-019.md#s-5a471470eabbe594)

### observed_connections-001334

```text
(config-router-af)# no bgp bestpath compare-routerid <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 24 `；EOL ` RVA 0x3449B888 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-292918144cc23f5a](../../evidence/conditions-sets-016.md#c-292918144cc23f5a) · [状态效果 S-5a471470eabbe594](../../evidence/state_effects-sets-019.md#s-5a471470eabbe594)

### observed_connections-001390

```text
(config-router-af)# no bgp bestpath cost-community ignore <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 41 `；EOL ` RVA 0x3449BEB0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-292918144cc23f5a](../../evidence/conditions-sets-016.md#c-292918144cc23f5a) · [状态效果 S-5a471470eabbe594](../../evidence/state_effects-sets-019.md#s-5a471470eabbe594)

### observed_connections-001351

```text
(config-router-af)# no bgp bestpath igp-metric ignore <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 42 `；EOL ` RVA 0x3449FCA0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-12684a895e92662c](../../evidence/conditions-sets-007.md#c-12684a895e92662c) · [状态效果 S-5a471470eabbe594](../../evidence/state_effects-sets-019.md#s-5a471470eabbe594)

### observed_connections-001387

```text
(config-router-af)# no bgp bestpath med missing-as-worst <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 18 `；EOL ` RVA 0x3449B038 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-292918144cc23f5a](../../evidence/conditions-sets-016.md#c-292918144cc23f5a) · [状态效果 S-06ca9540208a5bec](../../evidence/state_effects-sets-002.md#s-06ca9540208a5bec)

### observed_connections-001357

```text
(config-router-af)# no bgp bestpath prefix-validate allow-invalid <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 78 `；EOL ` RVA 0x3449FFB0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-87b72272feb7b1d0](../../evidence/conditions-sets-052.md#c-87b72272feb7b1d0) · [状态效果 S-5a471470eabbe594](../../evidence/state_effects-sets-019.md#s-5a471470eabbe594)

### observed_connections-001359

```text
(config-router-af)# no bgp bestpath prefix-validate disable <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 77 `；EOL ` RVA 0x344A0258 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-87b72272feb7b1d0](../../evidence/conditions-sets-052.md#c-87b72272feb7b1d0) · [状态效果 S-5a471470eabbe594](../../evidence/state_effects-sets-019.md#s-5a471470eabbe594)

### observed_connections-001296

```text
(config-router-af)# no bgp client-to-client reflection <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 9 `；EOL ` RVA 0x34494EB8 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d9b175ed3b628ebc](../../evidence/conditions-sets-084.md#c-d9b175ed3b628ebc) · [状态效果 S-ae77b5d1327c46b9](../../evidence/state_effects-sets-037.md#s-ae77b5d1327c46b9)

### observed_connections-001176

```text
(config-router-af)# no bgp cluster-id <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 7 `；EOL ` RVA 0x34494A80 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1faf1ecf67485161](../../evidence/conditions-sets-012.md#c-1faf1ecf67485161) · [状态效果 S-5a471470eabbe594](../../evidence/state_effects-sets-019.md#s-5a471470eabbe594)

### observed_connections-001185

```text
(config-router-af)# no bgp consistency-checker <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 3 `；EOL ` RVA 0x34494400 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b0038ba5089fa7be](../../evidence/conditions-sets-068.md#c-b0038ba5089fa7be) · [状态效果 S-5a471470eabbe594](../../evidence/state_effects-sets-019.md#s-5a471470eabbe594)

### observed_connections-001154

```text
(config-router-af)# no bgp dampening <cr>
```

Handler ` RVA 0xF1B85B0 `；selector ` 0 `；EOL ` RVA 0x3449E838 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1f6d77cc594a54fc](../../evidence/conditions-sets-012.md#c-1f6d77cc594a54fc) · [状态效果 S-5a471470eabbe594](../../evidence/state_effects-sets-019.md#s-5a471470eabbe594)

### observed_connections-001352

```text
(config-router-af)# no bgp default inter-as-hybrid advertise-source-routes <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 57 `；EOL ` RVA 0x3449DE70 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-6e3b3262cdac263c](../../evidence/conditions-sets-043.md#c-6e3b3262cdac263c) · [状态效果 S-5a471470eabbe594](../../evidence/state_effects-sets-019.md#s-5a471470eabbe594)

### observed_connections-001272

```text
(config-router-af)# no bgp default ipv4-unicast <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 19 `；EOL ` RVA 0x3449D5C8 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7bd7eb7684f098f8](../../evidence/conditions-sets-048.md#c-7bd7eb7684f098f8) · [状态效果 S-5a471470eabbe594](../../evidence/state_effects-sets-019.md#s-5a471470eabbe594)

### observed_connections-001274

```text
(config-router-af)# no bgp default ipv6-nexthop <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 75 `；EOL ` RVA 0x3449D8C0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8fdadd724abf1080](../../evidence/conditions-sets-056.md#c-8fdadd724abf1080) · [状态效果 S-5a471470eabbe594](../../evidence/state_effects-sets-019.md#s-5a471470eabbe594)

### observed_connections-001156

```text
(config-router-af)# no bgp default local-preference <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 0 `；EOL ` RVA 0x3449DB50 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-203327081868b838](../../evidence/conditions-sets-013.md#c-203327081868b838) · [状态效果 S-5a471470eabbe594](../../evidence/state_effects-sets-019.md#s-5a471470eabbe594)

### observed_connections-001345

```text
(config-router-af)# no bgp default route-target filter <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 25 `；EOL ` RVA 0x3449E1D8 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-681462e02c6b52c0](../../evidence/conditions-sets-040.md#c-681462e02c6b52c0) · [状态效果 S-5a471470eabbe594](../../evidence/state_effects-sets-019.md#s-5a471470eabbe594)

### observed_connections-001346

```text
(config-router-af)# no bgp default route-target filter <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 25 `；EOL ` RVA 0x3449E478 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b99ec9f9a643af4d](../../evidence/conditions-sets-072.md#c-b99ec9f9a643af4d) · [状态效果 S-5a471470eabbe594](../../evidence/state_effects-sets-019.md#s-5a471470eabbe594)

### observed_connections-001202

```text
(config-router-af)# no bgp deterministic-med <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 10 `；EOL ` RVA 0x34496538 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e27560d5ee3533f0](../../evidence/conditions-sets-087.md#c-e27560d5ee3533f0) · [状态效果 S-5a471470eabbe594](../../evidence/state_effects-sets-019.md#s-5a471470eabbe594)

### observed_connections-001175

```text
(config-router-af)# no bgp dmzlink-bw <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 31 `；EOL ` RVA 0x344A1B70 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5c6277c6ec36b6d9](../../evidence/conditions-sets-036.md#c-5c6277c6ec36b6d9) · [状态效果 S-5a471470eabbe594](../../evidence/state_effects-sets-019.md#s-5a471470eabbe594)

### observed_connections-001095

```text
(config-router-af)# no bgp dynamic-med-interval <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 21 `；EOL ` RVA 0x34496560 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-42adbaa615c0110b](../../evidence/conditions-sets-026.md#c-42adbaa615c0110b) · [状态效果 S-5a471470eabbe594](../../evidence/state_effects-sets-019.md#s-5a471470eabbe594)

### observed_connections-001181

```text
(config-router-af)# no bgp enforce-first-as <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 20 `；EOL ` RVA 0x34495768 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e27560d5ee3533f0](../../evidence/conditions-sets-087.md#c-e27560d5ee3533f0) · [状态效果 S-5a471470eabbe594](../../evidence/state_effects-sets-019.md#s-5a471470eabbe594)

### observed_connections-001222

```text
(config-router-af)# no bgp enhanced-error <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 82 `；EOL ` RVA 0x344981A8 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8d95adca8551d644](../../evidence/conditions-sets-055.md#c-8d95adca8551d644) · [状态效果 S-5a471470eabbe594](../../evidence/state_effects-sets-019.md#s-5a471470eabbe594)

### observed_connections-001141

```text
(config-router-af)# no bgp fast-external-fallover <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 1 `；EOL ` RVA 0x34493450 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e27560d5ee3533f0](../../evidence/conditions-sets-087.md#c-e27560d5ee3533f0) · [状态效果 S-5a471470eabbe594](../../evidence/state_effects-sets-019.md#s-5a471470eabbe594)

### observed_connections-001233

```text
(config-router-af)# no bgp graceful-restart <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 35 `；EOL ` RVA 0x34499018 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e27560d5ee3533f0](../../evidence/conditions-sets-087.md#c-e27560d5ee3533f0) · [状态效果 S-5a471470eabbe594](../../evidence/state_effects-sets-019.md#s-5a471470eabbe594)

### observed_connections-001227

```text
(config-router-af)# no bgp graceful-restart restart-time <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 36 `；EOL ` RVA 0x344989E8 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b9790c5900320715](../../evidence/conditions-sets-072.md#c-b9790c5900320715) · [状态效果 S-5a471470eabbe594](../../evidence/state_effects-sets-019.md#s-5a471470eabbe594)

### observed_connections-001229

```text
(config-router-af)# no bgp graceful-restart stalepath-time <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 37 `；EOL ` RVA 0x34498A50 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-6ed3aa722ead93e9](../../evidence/conditions-sets-043.md#c-6ed3aa722ead93e9) · [状态效果 S-5a471470eabbe594](../../evidence/state_effects-sets-019.md#s-5a471470eabbe594)

### observed_connections-001408

```text
(config-router-af)# no bgp graceful-shutdown all vrfs activate <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 79 `；EOL ` RVA 0x34499480 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-efaafb9b08f976da](../../evidence/conditions-sets-093.md#c-efaafb9b08f976da) · [状态效果 S-427ee669ad100d50](../../evidence/state_effects-sets-015.md#s-427ee669ad100d50)

### observed_connections-001406

```text
(config-router-af)# no bgp inject-map <string> exist-map <string> <cr>
```

Handler ` RVA 0xF1C00F0 `；selector ` 32 `；EOL ` RVA 0x344A36E8 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` route-map name；` string ` route-map name。

[条件 C-9063251b6c849b1e](../../evidence/conditions-sets-056.md#c-9063251b6c849b1e) · [参数 P-b763d74c2b1995aa](../../evidence/parameters-sets-014.md#p-b763d74c2b1995aa) · [状态效果 S-5a471470eabbe594](../../evidence/state_effects-sets-019.md#s-5a471470eabbe594)

### observed_connections-001344

```text
(config-router-af)# no bgp label-allocation-batch <number:0..4294967295> <number:0..4294967295> <cr>
```

Handler ` RVA 0xF1B9300 `；selector ` 53 `；EOL ` RVA 0x344937E0 `。

模式根 ` RVA 0x3448F060 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Timer value in milliseconds；` unsigned_number ` Batch Size。

[条件 C-e27560d5ee3533f0](../../evidence/conditions-sets-087.md#c-e27560d5ee3533f0) · [参数 P-af331c78273510e6](../../evidence/parameters-sets-013.md#p-af331c78273510e6) · [状态效果 S-5a471470eabbe594](../../evidence/state_effects-sets-019.md#s-5a471470eabbe594)

