# configure · 六个基础模式的历史连接

[模式索引](README.md) · [总索引](../../README.md)

### path-029303

```text
(config)# ipv6 nd nsf dad suppress <number:0..600> <cr>
```

Handler ` RVA 0x12315FA0 `；selector ` 0 `；EOL ` RVA 0x357F6FE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` seconds。

[条件 C-241494c456c7769b](../../evidence/conditions-sets-014.md#c-241494c456c7769b) · [参数 P-9aafe976e07a21a1](../../evidence/parameters-sets-012.md#p-9aafe976e07a21a1) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026896

```text
(config)# ipv6 nd nsf throttle <number:128..4096> <cr>
```

Handler ` RVA 0x12315E90 `；selector ` 0 `；EOL ` RVA 0x357F6AA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Resolutions。

[条件 C-1feec4d624049351](../../evidence/conditions-sets-012.md#c-1feec4d624049351) · [参数 P-24d12e32f35fd41c](../../evidence/parameters-sets-003.md#p-24d12e32f35fd41c) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-035543

```text
(config)# ipv6 nd nud limit <number:32..4096> <cr>
```

Handler ` RVA 0x123159C0 `；selector ` 0 `；EOL ` RVA 0x357F7390 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Limit (NS)。

[条件 C-1b3687bd4c0b0079](../../evidence/conditions-sets-011.md#c-1b3687bd4c0b0079) · [参数 P-ff9627b33094a23d](../../evidence/parameters-sets-019.md#p-ff9627b33094a23d) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-035237

```text
(config)# ipv6 nd ra solicited unicast <cr>
```

Handler ` RVA 0x123179F0 `；selector ` 0 `；EOL ` RVA 0x357F67A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025783

```text
(config)# ipv6 nd reachable-time <number:0..3600000> <cr>
```

Handler ` RVA 0x12315350 `；selector ` 0 `；EOL ` RVA 0x357F7720 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Reachability time in milliseconds。

[条件 C-1f4924bc36f02295](../../evidence/conditions-sets-012.md#c-1f4924bc36f02295) · [参数 P-61bc8cc30fc5d9bd](../../evidence/parameters-sets-008.md#p-61bc8cc30fc5d9bd) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029408

```text
(config)# ipv6 nd resolution data limit <number:16..2048> <cr>
```

Handler ` RVA 0x1231B330 `；selector ` 0 `；EOL ` RVA 0x357F7F48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Limit in packets。

[条件 C-ff32b1f67d8a1fb1](../../evidence/conditions-sets-098.md#c-ff32b1f67d8a1fb1) · [参数 P-770a8f78a3dc3d0a](../../evidence/parameters-sets-009.md#p-770a8f78a3dc3d0a) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026913

```text
(config)# ipv6 nd route-owner <cr>
```

Handler ` RVA 0x123160A0 `；selector ` 0 `；EOL ` RVA 0x357F76F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-062719

```text
(config)# ipv6 nd suppress <cr>
```

Handler ` RVA 0x136B2390 `；selector ` 0 `；EOL ` RVA 0x35C04470 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-19aaf9fdb91739bf](../../evidence/conditions-sets-010.md#c-19aaf9fdb91739bf) · [缺口 G-80dc7170d402388f](../../evidence/gaps-sets-005.md#g-80dc7170d402388f) · [状态效果 S-928aed849d8aad91](../../evidence/state_effects-sets-031.md#s-928aed849d8aad91)

### path-062787

```text
(config)# ipv6 nd suppress policy <string> <cr>
```

Handler ` RVA 0x136B1D70 `；selector ` 0 `；EOL ` RVA 0x35C04150 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Name of the ndsuppress policy。

[条件 C-f64fa844d9031366](../../evidence/conditions-sets-095.md#c-f64fa844d9031366) · [缺口 G-80dc7170d402388f](../../evidence/gaps-sets-005.md#g-80dc7170d402388f) · [参数 P-6e0779347c5d1c3e](../../evidence/parameters-sets-009.md#p-6e0779347c5d1c3e) · [状态效果 S-928aed849d8aad91](../../evidence/state_effects-sets-031.md#s-928aed849d8aad91)

### path-060584

```text
(config)# ipv6 neighbor <address> <interface> <cr>
```

Handler ` RVA 0x12319320 `；selector ` 0 `；EOL ` RVA 0x35803520 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` IPv6 address。

[条件 C-357d97a537cc7af7](../../evidence/conditions-sets-021.md#c-357d97a537cc7af7) · [缺口 G-2a9cf2b466f27acb](../../evidence/gaps-sets-002.md#g-2a9cf2b466f27acb) · [参数 P-f8c6ff3b281127ad](../../evidence/parameters-sets-019.md#p-f8c6ff3b281127ad) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027057

```text
(config)# ipv6 neighbor binding <cr>
```

Handler ` RVA 0x13680440 `；selector ` 1004 `；EOL ` RVA 0x35BEBAB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1f734c4f3657852b](../../evidence/conditions-sets-012.md#c-1f734c4f3657852b) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-062947

```text
(config)# ipv6 neighbor binding <prefix:dynamic> <cr>
```

Handler ` RVA 0x13680440 `；selector ` 1001 `；EOL ` RVA 0x35BEC2C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` IPv6 prefix。

[条件 C-6556c463fb6139f2](../../evidence/conditions-sets-039.md#c-6556c463fb6139f2) · [缺口 G-3609582a45447bcd](../../evidence/gaps-sets-002.md#g-3609582a45447bcd) · [参数 P-b1f2f30c52858227](../../evidence/parameters-sets-013.md#p-b1f2f30c52858227) · [状态效果 S-002232f830da0155](../../evidence/state_effects-sets-001.md#s-002232f830da0155)

### path-029427

```text
(config)# ipv6 neighbor binding logging <cr>
```

Handler ` RVA 0x13680440 `；selector ` 1003 `；EOL ` RVA 0x35BEB728 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bbe643bd5974e3cf](../../evidence/conditions-sets-073.md#c-bbe643bd5974e3cf) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-035784

```text
(config)# ipv6 neighbor binding max-entries <number:1..1000000> <cr>
```

Handler ` RVA 0x13680440 `；selector ` 1002 `；EOL ` RVA 0x35BEB1F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of entries。

[条件 C-5ee2afcc84f614ed](../../evidence/conditions-sets-037.md#c-5ee2afcc84f614ed) · [参数 P-0bdbcf4bc127174f](../../evidence/parameters-sets-001.md#p-0bdbcf4bc127174f) · [状态效果 S-20870d9917d982bd](../../evidence/state_effects-sets-007.md#s-20870d9917d982bd)

### path-060844

```text
(config)# ipv6 neighbor binding reachable-lifetime <number:1..86400> <cr>
```

Handler ` RVA 0x13680440 `；selector ` 1004 `；EOL ` RVA 0x35BEBAB0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Seconds。

[条件 C-59c7f162f47199b4](../../evidence/conditions-sets-035.md#c-59c7f162f47199b4) · [缺口 G-568c5208a3dddac6](../../evidence/gaps-sets-003.md#g-568c5208a3dddac6) · [参数 P-9f5efd9b78b87f59](../../evidence/parameters-sets-012.md#p-9f5efd9b78b87f59) · [状态效果 S-1b489c3bf611a825](../../evidence/state_effects-sets-006.md#s-1b489c3bf611a825)

### path-026955

```text
(config)# ipv6 neighbor tracking <cr>
```

Handler ` RVA 0x13680440 `；selector ` 1005 `；EOL ` RVA 0x35BECCF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-02091299c92cccf1](../../evidence/conditions-sets-001.md#c-02091299c92cccf1) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026912

```text
(config)# ipv6 nsf-converge <number:1..3600> <cr>
```

Handler ` RVA 0x118AC940 `；selector ` 0 `；EOL ` RVA 0x35590608 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` The minimum NSF interval, in sec, before RIB reporting convergence。

[条件 C-c1ecf6cc71fad6bb](../../evidence/conditions-sets-075.md#c-c1ecf6cc71fad6bb) · [参数 P-8ab1ce2b10cce507](../../evidence/parameters-sets-011.md#p-8ab1ce2b10cce507) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026961

```text
(config)# ipv6 ospf name-lookup <cr>
```

Handler ` RVA 0x11BC2820 `；selector ` 0 `；EOL ` RVA 0x35681728 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-035863

```text
(config)# ipv6 pim accept-register list <number:100..199> <cr>
```

Handler ` RVA 0x11725BA0 `；selector ` 14 `；EOL ` RVA 0x355538F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Access-list for Accept-register。

[条件 C-fba0d932f316d72a](../../evidence/conditions-sets-097.md#c-fba0d932f316d72a) · [参数 P-565de5f118e3aaa8](../../evidence/parameters-sets-007.md#p-565de5f118e3aaa8) · [状态效果 S-8a42c0a7b1112646](../../evidence/state_effects-sets-029.md#s-8a42c0a7b1112646)

### path-027249

```text
(config)# ipv6 pim allow-rp <cr>
```

Handler ` RVA 0x11725BA0 `；selector ` 35 `；EOL ` RVA 0x35555CA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c0602bbba78e12b3](../../evidence/conditions-sets-074.md#c-c0602bbba78e12b3) · [状态效果 S-8a42c0a7b1112646](../../evidence/state_effects-sets-029.md#s-8a42c0a7b1112646)

### path-036342

```text
(config)# ipv6 pim anycast-rp <address> <address> <cr>
```

Handler ` RVA 0x11725BA0 `；selector ` 33 `；EOL ` RVA 0x35555958 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP address of the Anycast Rendezvous Point；` address ` IP address of the Anycast RP peer。

[条件 C-96f5b87be8db8e6b](../../evidence/conditions-sets-058.md#c-96f5b87be8db8e6b) · [参数 P-3e4cef02346a59f8](../../evidence/parameters-sets-005.md#p-3e4cef02346a59f8) · [状态效果 S-8a42c0a7b1112646](../../evidence/state_effects-sets-029.md#s-8a42c0a7b1112646)

### path-046308

```text
(config)# ipv6 pim bsr announced rp <address> <cr>
```

Handler ` RVA 0x11725BA0 `；selector ` 26 `；EOL ` RVA 0x355510F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP name or address of Announced RP。

[条件 C-c9304a4db53b344a](../../evidence/conditions-sets-078.md#c-c9304a4db53b344a) · [参数 P-4723e2b28b5ce721](../../evidence/parameters-sets-006.md#p-4723e2b28b5ce721) · [状态效果 S-0fcfa17f6170cb74](../../evidence/state_effects-sets-004.md#s-0fcfa17f6170cb74)

### path-046309

```text
(config)# ipv6 pim bsr candidate bsr <address> <cr>
```

Handler ` RVA 0x11725BA0 `；selector ` 24 `；EOL ` RVA 0x355503E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP name or address of BSR。

[条件 C-0c67f102d91ba159](../../evidence/conditions-sets-005.md#c-0c67f102d91ba159) · [参数 P-f9eb199b3c4952c8](../../evidence/parameters-sets-019.md#p-f9eb199b3c4952c8) · [状态效果 S-b79bf8926725c39f](../../evidence/state_effects-sets-039.md#s-b79bf8926725c39f)

### path-046364

```text
(config)# ipv6 pim bsr candidate rp <address> <cr>
```

Handler ` RVA 0x11725BA0 `；selector ` 27 `；EOL ` RVA 0x35550B38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP name or address of Candidate RP。

[条件 C-c9304a4db53b344a](../../evidence/conditions-sets-078.md#c-c9304a4db53b344a) · [参数 P-56b08dfe4265191e](../../evidence/parameters-sets-007.md#p-56b08dfe4265191e) · [状态效果 S-5da9b0ac10faf567](../../evidence/state_effects-sets-020.md#s-5da9b0ac10faf567)

### path-045728

```text
(config)# ipv6 pim maximum group-mappings bsr <number:1..10000> <cr>
```

Handler ` RVA 0x11725BA0 `；selector ` 34 `；EOL ` RVA 0x355555D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Maximum PIM group mappings。

[条件 C-014794a6ff2c5991](../../evidence/conditions-sets-001.md#c-014794a6ff2c5991) · [参数 P-faf3f2b85e0f33db](../../evidence/parameters-sets-019.md#p-faf3f2b85e0f33db) · [状态效果 S-8a42c0a7b1112646](../../evidence/state_effects-sets-029.md#s-8a42c0a7b1112646)

### path-030039

```text
(config)# ipv6 pim mvpn source-link-local <cr>
```

Handler ` RVA 0x11725BA0 `；selector ` 16 `；EOL ` RVA 0x35556180 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c9304a4db53b344a](../../evidence/conditions-sets-078.md#c-c9304a4db53b344a) · [状态效果 S-8a42c0a7b1112646](../../evidence/state_effects-sets-029.md#s-8a42c0a7b1112646)

### path-035804

```text
(config)# ipv6 pim neighbor-filter list <number:100..199> <cr>
```

Handler ` RVA 0x11725BA0 `；selector ` 15 `；EOL ` RVA 0x355534B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Access-list for Accept-register。

[条件 C-6e3898e178063dcf](../../evidence/conditions-sets-043.md#c-6e3898e178063dcf) · [参数 P-725eaf1ead64a7bb](../../evidence/parameters-sets-009.md#p-725eaf1ead64a7bb) · [状态效果 S-8a42c0a7b1112646](../../evidence/state_effects-sets-029.md#s-8a42c0a7b1112646)

### path-027139

```text
(config)# ipv6 pim old-register-checksum <cr>
```

Handler ` RVA 0x11725BA0 `；selector ` 12 `；EOL ` RVA 0x35555218 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-924fb0804ea39d1c](../../evidence/conditions-sets-056.md#c-924fb0804ea39d1c) · [状态效果 S-8a42c0a7b1112646](../../evidence/state_effects-sets-029.md#s-8a42c0a7b1112646)

### path-036995

```text
(config)# ipv6 pim pfp-sa announce <address> <cr>
```

Handler ` RVA 0x11725BA0 `；selector ` 48 `；EOL ` RVA 0x355A3D48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Source IP address for PFP-SA announcements。

[条件 C-9463a0f22b673cba](../../evidence/conditions-sets-057.md#c-9463a0f22b673cba) · [参数 P-7de652e45070f536](../../evidence/parameters-sets-010.md#p-7de652e45070f536) · [状态效果 S-2c67412e57b14e76](../../evidence/state_effects-sets-010.md#s-2c67412e57b14e76)

### path-030468

```text
(config)# ipv6 pim pfp-sa cache <cr>
```

Handler ` RVA 0x11725BA0 `；selector ` 51 `；EOL ` RVA 0x355A47E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6425d090942c12f6](../../evidence/conditions-sets-039.md#c-6425d090942c12f6) · [状态效果 S-2c67412e57b14e76](../../evidence/state_effects-sets-010.md#s-2c67412e57b14e76)

### path-046249

```text
(config)# ipv6 pim pfp-sa timers holdtime <number:1..3600> <cr>
```

Handler ` RVA 0x11725BA0 `；selector ` 49 `；EOL ` RVA 0x355A41E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Holdtime in seconds。

[条件 C-1e7e04e44197c46c](../../evidence/conditions-sets-012.md#c-1e7e04e44197c46c) · [参数 P-dbc4328732f85675](../../evidence/parameters-sets-017.md#p-dbc4328732f85675) · [状态效果 S-2c67412e57b14e76](../../evidence/state_effects-sets-010.md#s-2c67412e57b14e76)

### path-046284

```text
(config)# ipv6 pim pfp-sa timers interval <number:1..3600> <cr>
```

Handler ` RVA 0x11725BA0 `；selector ` 50 `；EOL ` RVA 0x355A44D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Interval in seconds。

[条件 C-e958e6f2f0bc2e33](../../evidence/conditions-sets-090.md#c-e958e6f2f0bc2e33) · [参数 P-8300aed183fc4946](../../evidence/parameters-sets-010.md#p-8300aed183fc4946) · [状态效果 S-2c67412e57b14e76](../../evidence/state_effects-sets-010.md#s-2c67412e57b14e76)

### path-060617

```text
(config)# ipv6 pim register-source <interface> <cr>
```

Handler ` RVA 0x11725BA0 `；selector ` 10 `；EOL ` RVA 0x35554620 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ba1c31e6cae47c23](../../evidence/conditions-sets-072.md#c-ba1c31e6cae47c23) · [缺口 G-59f2062ba78d1e43](../../evidence/gaps-sets-004.md#g-59f2062ba78d1e43) · [参数 P-f2d04ba87456783a](../../evidence/parameters-sets-018.md#p-f2d04ba87456783a) · [状态效果 S-8a42c0a7b1112646](../../evidence/state_effects-sets-029.md#s-8a42c0a7b1112646)

### path-029627

```text
(config)# ipv6 pim rp embedded <cr>
```

Handler ` RVA 0x11725BA0 `；selector ` 13 `；EOL ` RVA 0x35553D10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4e02b58d4c64c037](../../evidence/conditions-sets-031.md#c-4e02b58d4c64c037) · [状态效果 S-8a42c0a7b1112646](../../evidence/state_effects-sets-029.md#s-8a42c0a7b1112646)

### path-029796

```text
(config)# ipv6 pim rp-address <address> <cr>
```

Handler ` RVA 0x11725BA0 `；selector ` 7 `；EOL ` RVA 0x355540C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP name or address of Rendezvous Point。

[条件 C-0c23a90f26c136b7](../../evidence/conditions-sets-005.md#c-0c23a90f26c136b7) · [参数 P-95c3b39af062bf39](../../evidence/parameters-sets-012.md#p-95c3b39af062bf39) · [状态效果 S-8a42c0a7b1112646](../../evidence/state_effects-sets-029.md#s-8a42c0a7b1112646)

### path-029903

```text
(config)# ipv6 pim spt-threshold infinity <cr>
```

Handler ` RVA 0x11725BA0 `；selector ` 9 `；EOL ` RVA 0x35554970 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-49badb88cf53da1b](../../evidence/conditions-sets-029.md#c-49badb88cf53da1b) · [状态效果 S-8a42c0a7b1112646](../../evidence/state_effects-sets-029.md#s-8a42c0a7b1112646)

### path-061905

```text
(config)# ipv6 pim static-rpf <address> <number:0..32> <interface> <address> <cr>
```

Handler ` RVA 0x11725BA0 `；selector ` 11 `；EOL ` RVA 0x35554F58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Prefix for address range；` unsigned_number ` Prefix mask for address range；` address ` RPF neighbor。

[条件 C-1a0005a50bec3b63](../../evidence/conditions-sets-010.md#c-1a0005a50bec3b63) · [缺口 G-4a4a464bbfa885de](../../evidence/gaps-sets-003.md#g-4a4a464bbfa885de) · [参数 P-b5e4a45af92935a4](../../evidence/parameters-sets-014.md#p-b5e4a45af92935a4) · [状态效果 S-8a42c0a7b1112646](../../evidence/state_effects-sets-029.md#s-8a42c0a7b1112646)

### path-027160

```text
(config)# ipv6 prefix-list <string> <cr>
```

Handler ` RVA 0xE21E820 `；selector ` 0 `；EOL ` RVA 0x3557E768 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of a prefix list。

[条件 C-5ea6be5510163735](../../evidence/conditions-sets-037.md#c-5ea6be5510163735) · [参数 P-df0de99fc459d497](../../evidence/parameters-sets-017.md#p-df0de99fc459d497) · [状态效果 S-91a1ed95fe391c72](../../evidence/state_effects-sets-031.md#s-91a1ed95fe391c72)

### path-060852

```text
(config)# ipv6 prefix-list <string> deny <prefix:dynamic> <cr>
```

Handler ` RVA 0xE21E820 `；selector ` 0 `；EOL ` RVA 0x3557E068 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Name of a prefix list；` prefix_dynamic ` IPv6 prefix &lt;network&gt;/&lt;length&gt;。

[条件 C-69acbb8f4b6f8b45](../../evidence/conditions-sets-041.md#c-69acbb8f4b6f8b45) · [缺口 G-1d3c25fc94c9cfda](../../evidence/gaps-sets-001.md#g-1d3c25fc94c9cfda) · [参数 P-08c7f8661aca5b14](../../evidence/parameters-sets-001.md#p-08c7f8661aca5b14) · [状态效果 S-1e63a14f70299ebd](../../evidence/state_effects-sets-007.md#s-1e63a14f70299ebd)

### path-027028

```text
(config)# ipv6 prefix-list sequence-number <cr>
```

Handler ` RVA 0xE21E820 `；selector ` 0 `；EOL ` RVA 0x3557E068 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-f469dc52407942b6](../../evidence/state_effects-sets-052.md#s-f469dc52407942b6)

### path-060607

```text
(config)# ipv6 radius source-interface <interface> <cr>
```

Handler ` RVA 0xFFD39D0 `；selector ` 94 `；EOL ` RVA 0x34967130 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8389aef7ca0da80e](../../evidence/conditions-sets-051.md#c-8389aef7ca0da80e) · [缺口 G-94fae528356bb34a](../../evidence/gaps-sets-005.md#g-94fae528356bb34a) · [参数 P-5fd4283d2f787b0a](../../evidence/parameters-sets-008.md#p-5fd4283d2f787b0a) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060577

```text
(config)# ipv6 reassembly-queue length <number:dynamic> <cr>
```

Handler ` RVA 0x12305B90 `；selector ` 0 `；EOL ` RVA 0x357E6270 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` maximum simultaneous reassemblies。

[条件 C-f6f40769fdb4eb2f](../../evidence/conditions-sets-095.md#c-f6f40769fdb4eb2f) · [缺口 G-68156b27bb00780c](../../evidence/gaps-sets-004.md#g-68156b27bb00780c) · [参数 P-dbec6a8a614bc4ec](../../evidence/parameters-sets-017.md#p-dbec6a8a614bc4ec) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029261

```text
(config)# ipv6 reassembly-queue time-out <number:0..60> <cr>
```

Handler ` RVA 0x12305D80 `；selector ` 0 `；EOL ` RVA 0x357E6598 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` time-out in seconds。

[条件 C-28afef7ea46c86b5](../../evidence/conditions-sets-016.md#c-28afef7ea46c86b5) · [参数 P-b619fedb079d5e25](../../evidence/parameters-sets-014.md#p-b619fedb079d5e25) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029246

```text
(config)# ipv6 rip vrf-mode enable <cr>
```

Handler ` RVA 0x118A8710 `；selector ` 0 `；EOL ` RVA 0x35579B40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-062276

```text
(config)# ipv6 route <?match_ipv6_pfxinfo_action@55558ad45b90> segment-routing srv6 via policy <string> <cr>
```

Handler ` RVA 0x1230F1F0 `；selector ` 0 `；EOL ` RVA 0x357F2328 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` SR Policy Name。

[条件 C-da2910ef0374dcc5](../../evidence/conditions-sets-084.md#c-da2910ef0374dcc5) · [缺口 G-fe3d27de151c507f](../../evidence/gaps-sets-009.md#g-fe3d27de151c507f) · [参数 P-7f1f50991f14374d](../../evidence/parameters-sets-010.md#p-7f1f50991f14374d) · [状态效果 S-e9ff745362a74694](../../evidence/state_effects-sets-050.md#s-e9ff745362a74694)

### path-061269

```text
(config)# ipv6 route static bfd <interface> <address> <cr>
```

Handler ` RVA 0x123102A0 `；selector ` 0 `；EOL ` RVA 0x357F1558 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` IPv6 address of BFD neighbor。

[条件 C-2ff24eaac01318de](../../evidence/conditions-sets-019.md#c-2ff24eaac01318de) · [缺口 G-1a86bc547d931617](../../evidence/gaps-sets-001.md#g-1a86bc547d931617) · [参数 P-86f809832506d808](../../evidence/parameters-sets-010.md#p-86f809832506d808) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-035135

```text
(config)# ipv6 route static resolve default <cr>
```

Handler ` RVA 0x12310680 `；selector ` 0 `；EOL ` RVA 0x357F1888 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-062718

```text
(config)# ipv6 router <?ipv6_router_action@55558aae3f98> <cr>
```

Handler ` RVA 0x118AF310 `；selector ` 0 `；EOL ` RVA 0x3558FFD0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [缺口 G-39dcad81ab27fc55](../../evidence/gaps-sets-003.md#g-39dcad81ab27fc55) · [状态效果 S-a11cef5e151ada66](../../evidence/state_effects-sets-034.md#s-a11cef5e151ada66)

### path-025838

```text
(config)# ipv6 snooping <cr>
```

Handler ` RVA 0x1368AFF0 `；selector ` 1123 `；EOL ` RVA 0x35BCA6C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-207964839355e237](../../evidence/conditions-sets-013.md#c-207964839355e237) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029680

```text
(config)# ipv6 snooping policy <string> <cr>
```

Handler ` RVA 0x1368A1D0 `；selector ` 1100 `；EOL ` RVA 0x35BCA3A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of the snooping policy。

[条件 C-e5b31a9ab17a79e7](../../evidence/conditions-sets-089.md#c-e5b31a9ab17a79e7) · [参数 P-a35746d31cfb61ab](../../evidence/parameters-sets-012.md#p-a35746d31cfb61ab) · [状态效果 S-c3d97c5023648e81](../../evidence/state_effects-sets-041.md#s-c3d97c5023648e81)

### path-025819

```text
(config)# ipv6 source-guard <cr>
```

Handler ` RVA 0x136BFE70 `；selector ` 1522 `；EOL ` RVA 0x35C07AD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7a3db213e250349f](../../evidence/conditions-sets-047.md#c-7a3db213e250349f) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029525

```text
(config)# ipv6 source-guard policy <string> <cr>
```

Handler ` RVA 0x136BFD10 `；selector ` 1500 `；EOL ` RVA 0x35C077B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of the source-guard policy。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-427f82511c202d2f](../../evidence/parameters-sets-006.md#p-427f82511c202d2f) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025768

```text
(config)# ipv6 source-route <cr>
```

Handler ` RVA 0x12306120 `；selector ` 0 `；EOL ` RVA 0x357E71D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029676

```text
(config)# ipv6 spd mode aggressive <cr>
```

Handler ` RVA 0x12328100 `；selector ` 0 `；EOL ` RVA 0x3580F768 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b929712929f7a507](../../evidence/conditions-sets-071.md#c-b929712929f7a507) · [状态效果 S-2669ebe5075fb689](../../evidence/state_effects-sets-009.md#s-2669ebe5075fb689)

### path-035934

```text
(config)# ipv6 spd queue max-threshold <number:2..65535> <cr>
```

Handler ` RVA 0x123281B0 `；selector ` 0 `；EOL ` RVA 0x3580FBC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` spd value。

[条件 C-75ec8a20c16ed306](../../evidence/conditions-sets-046.md#c-75ec8a20c16ed306) · [参数 P-caef85f3535c3b08](../../evidence/parameters-sets-015.md#p-caef85f3535c3b08) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-036008

```text
(config)# ipv6 spd queue min-threshold <number:1..65535> <cr>
```

Handler ` RVA 0x12328360 `；selector ` 0 `；EOL ` RVA 0x3580FEB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` spd value。

[条件 C-c276ea9f77f7bd2e](../../evidence/conditions-sets-075.md#c-c276ea9f77f7bd2e) · [参数 P-2ca002f8b7f5a819](../../evidence/parameters-sets-004.md#p-2ca002f8b7f5a819) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060592

```text
(config)# ipv6 tacacs source-interface <interface> <cr>
```

Handler ` RVA 0xDB8ADD0 `；selector ` 26 `；EOL ` RVA 0x33FEFB10 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-cf0d8cf8da9a17ee](../../evidence/conditions-sets-080.md#c-cf0d8cf8da9a17ee) · [缺口 G-c3ba5b8fcbdfec43](../../evidence/gaps-sets-007.md#g-c3ba5b8fcbdfec43) · [参数 P-17ca6aee944ea6c4](../../evidence/parameters-sets-002.md#p-17ca6aee944ea6c4) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026925

```text
(config)# ipv6 traffic interface-statistics <cr>
```

Handler ` RVA 0x1231FDD0 `；selector ` 0 `；EOL ` RVA 0x3580B088 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-de81f180b5e64b2f](../../evidence/conditions-sets-086.md#c-de81f180b5e64b2f) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025764

```text
(config)# ipv6 unicast-routing <cr>
```

Handler ` RVA 0x118AC790 `；selector ` 0 `；EOL ` RVA 0x355902C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ffa7766731bf7398](../../evidence/conditions-sets-099.md#c-ffa7766731bf7398) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-052781

```text
(config)# ipv6 visibility global flow monitor sdwan_flow_monitor_ipv6 input <cr>
```

Handler ` RVA 0xC670530 `；selector ` 0 `；EOL ` RVA 0x33ACEC30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-501b3dfc091432ba](../../evidence/state_effects-sets-017.md#s-501b3dfc091432ba)

### path-025955

```text
(config)# isdn alert-end-to-end <cr>
```

Handler ` RVA 0x1E020F90 `；selector ` 99 `；EOL ` RVA 0x378A2A60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ee521a1986ad9f7b](../../evidence/conditions-sets-092.md#c-ee521a1986ad9f7b) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025958

```text
(config)# isdn debug <cr>
```

Handler ` RVA 0x1E04BE50 `；selector ` 40 `；EOL ` RVA 0x378A26E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-868f3bb8a575b573](../../evidence/conditions-sets-052.md#c-868f3bb8a575b573) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027454

```text
(config)# isdn display layer2-status <cr>
```

Handler ` RVA 0x1E020F90 `；selector ` 63 `；EOL ` RVA 0x378A2398 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-87c0f52614ba148f](../../evidence/conditions-sets-052.md#c-87c0f52614ba148f) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027476

```text
(config)# isdn housekeeping warn <cr>
```

Handler ` RVA 0x1E020F90 `；selector ` 125 `；EOL ` RVA 0x378A2D68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-41eb0d2f91d8fda0](../../evidence/conditions-sets-026.md#c-41eb0d2f91d8fda0) · [状态效果 S-2043561714e4d3d7](../../evidence/state_effects-sets-007.md#s-2043561714e4d3d7)

### path-025956

```text
(config)# isdn logging <cr>
```

Handler ` RVA 0x1E020F90 `；selector ` 117 `；EOL ` RVA 0x378A3100 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-87c0f52614ba148f](../../evidence/conditions-sets-052.md#c-87c0f52614ba148f) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025952

```text
(config)# isdn silent-boot <cr>
```

Handler ` RVA 0x1E020F90 `；selector ` 60 `；EOL ` RVA 0x378A2078 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-50b1edcecda64e55](../../evidence/conditions-sets-031.md#c-50b1edcecda64e55) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027437

```text
(config)# isdn switch-type none <cr>
```

Handler ` RVA 0x1E020F90 `；selector ` 3 `；EOL ` RVA 0x378A13D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff0673075f26a874](../../evidence/conditions-sets-098.md#c-ff0673075f26a874) · [状态效果 S-5f7c37ff6f2aac4e](../../evidence/state_effects-sets-021.md#s-5f7c37ff6f2aac4e)

### path-027452

```text
(config)# isdn-mib retain-timer <number:0..336> <cr>
```

Handler ` RVA 0x1E020F90 `；selector ` 96 `；EOL ` RVA 0x378A3F18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` retain time in hours, 0 to 336.。

[条件 C-efcba60f53bd167b](../../evidence/conditions-sets-093.md#c-efcba60f53bd167b) · [参数 P-24e8c7001677bf72](../../evidence/parameters-sets-003.md#p-24e8c7001677bf72) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027320

```text
(config)# isis display delimiter <cr>
```

Handler ` RVA 0x106B9450 `；selector ` 0 `；EOL ` RVA 0x34B95448 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-040c5a50503193b1](../../evidence/conditions-sets-002.md#c-040c5a50503193b1) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027215

```text
(config)# isis optimize inline <cr>
```

Handler ` RVA 0x106BDCB0 `；selector ` 0 `；EOL ` RVA 0x34B94E28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027231

```text
(config)# isis optimize lspdb-walk <cr>
```

Handler ` RVA 0x106BDBD0 `；selector ` 0 `；EOL ` RVA 0x34B950D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027591

```text
(config)# issu set rollback-timer <cr>
```

Handler ` RVA 0xEAE3FB0 `；selector ` 0 `；EOL ` RVA 0x343A74D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c1297f1931cdfe70](../../evidence/conditions-sets-075.md#c-c1297f1931cdfe70) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060710

```text
(config)# issu set rollback-timer <hh:mm:ss> <cr>
```

Handler ` RVA 0xEAE3FB0 `；selector ` 0 `；EOL ` RVA 0x343A74D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` time_hms ` Rollback timer in hh:mm:ss format。

[条件 C-0c15f89ce1827478](../../evidence/conditions-sets-005.md#c-0c15f89ce1827478) · [缺口 G-af34bd5b0858470f](../../evidence/gaps-sets-006.md#g-af34bd5b0858470f) · [参数 P-5dfc10996b4bf79a](../../evidence/parameters-sets-008.md#p-5dfc10996b4bf79a) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026434

```text
(config)# kerberos clients mandatory <cr>
```

Handler ` RVA 0xC3E3030 `；selector ` 9 `；EOL ` RVA 0x33A68D90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f1f208c7c02d8867](../../evidence/conditions-sets-093.md#c-f1f208c7c02d8867) · [状态效果 S-9b580670be232682](../../evidence/state_effects-sets-033.md#s-9b580670be232682)

### path-026531

```text
(config)# kerberos credentials forward <cr>
```

Handler ` RVA 0xC3E3030 `；selector ` 10 `；EOL ` RVA 0x33A69CF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3ffca5fade5ff5fe](../../evidence/conditions-sets-025.md#c-3ffca5fade5ff5fe) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-034475

```text
(config)# kerberos instance map <string> <number:0..15> <cr>
```

Handler ` RVA 0xC3E3030 `；selector ` 7 `；EOL ` RVA 0x33A69978 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Enable instance name；` unsigned_number ` Privilege level。

[条件 C-86e158c253dce555](../../evidence/conditions-sets-052.md#c-86e158c253dce555) · [参数 P-9fd54806e7729edb](../../evidence/parameters-sets-012.md#p-9fd54806e7729edb) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026368

```text
(config)# kerberos local-realm <string> <cr>
```

Handler ` RVA 0xC3E3030 `；selector ` 1 `；EOL ` RVA 0x33A67F58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Local kerberos realm name。

[条件 C-1f2fe6ad356075c9](../../evidence/conditions-sets-012.md#c-1f2fe6ad356075c9) · [参数 P-1229cb95e8686928](../../evidence/parameters-sets-002.md#p-1229cb95e8686928) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025703

```text
(config)# kerberos password <cr>
```

Handler ` RVA 0xC3E3030 `；selector ` 13 `；EOL ` RVA 0x33A6A548 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026485

```text
(config)# kerberos preauth encrypted-kerberos-timestamp <cr>
```

Handler ` RVA 0xC3E3030 `；selector ` 8 `；EOL ` RVA 0x33A694D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0d17d8d4fd86348e](../../evidence/conditions-sets-005.md#c-0d17d8d4fd86348e) · [状态效果 S-aba574bb73e02663](../../evidence/state_effects-sets-036.md#s-aba574bb73e02663)

### path-025446

```text
(config)# kerberos processes <number:1..10> <cr>
```

Handler ` RVA 0xC3E3030 `；selector ` 14 `；EOL ` RVA 0x33A6A4D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of processes。

[条件 C-80be21fef7a37f16](../../evidence/conditions-sets-050.md#c-80be21fef7a37f16) · [参数 P-e61d9e493d2b6c1f](../../evidence/parameters-sets-017.md#p-e61d9e493d2b6c1f) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-028246

```text
(config)# kerberos realm <string> <string> <cr>
```

Handler ` RVA 0xC3E3030 `；selector ` 3 `；EOL ` RVA 0x33A68A48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` DNS suffix；` string ` Kerberos Realm for given DNS suffix。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-16418d50b858183a](../../evidence/parameters-sets-002.md#p-16418d50b858183a) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025444

```text
(config)# kerberos retry <number:1..5> <cr>
```

Handler ` RVA 0xC3E3030 `；selector ` 12 `；EOL ` RVA 0x33A69F68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Value 1 to 5 (default 4)。

[条件 C-292ffa03a0687300](../../evidence/conditions-sets-016.md#c-292ffa03a0687300) · [参数 P-841de1e6ecf1585e](../../evidence/parameters-sets-010.md#p-841de1e6ecf1585e) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-028400

```text
(config)# kerberos server <string> <address> <cr>
```

Handler ` RVA 0xC3E3030 `；selector ` 4 `；EOL ` RVA 0x33A69188 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Kerberos Realm name；` address ` Server for realm。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-d5ee6fc9533e4678](../../evidence/parameters-sets-016.md#p-d5ee6fc9533e4678) · [状态效果 S-375503c5c7465f19](../../evidence/state_effects-sets-012.md#s-375503c5c7465f19)

### path-034365

```text
(config)# kerberos srvtab remote <address> <string> <cr>
```

Handler ` RVA 0xC3E3030 `；selector ` 2 `；EOL ` RVA 0x33A68340 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Remote srvtab server；` string ` Name of srvtab file on remote host。

[条件 C-c311a316a2b35101](../../evidence/conditions-sets-075.md#c-c311a316a2b35101) · [参数 P-41225a2e820210ee](../../evidence/parameters-sets-005.md#p-41225a2e820210ee) · [状态效果 S-f0c5ddc12dd5da0b](../../evidence/state_effects-sets-051.md#s-f0c5ddc12dd5da0b)

### path-060531

```text
(config)# kerberos srvtab remote <url:dynamic> <cr>
```

Handler ` RVA 0xC3E3030 `；selector ` 2 `；EOL ` RVA 0x33A68340 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-78c077fa65e1a01d](../../evidence/conditions-sets-047.md#c-78c077fa65e1a01d) · [缺口 G-6c18266f6e87f4bb](../../evidence/gaps-sets-004.md#g-6c18266f6e87f4bb) · [参数 P-9e8247c9df2d4acc](../../evidence/parameters-sets-012.md#p-9e8247c9df2d4acc) · [状态效果 S-f0c5ddc12dd5da0b](../../evidence/state_effects-sets-051.md#s-f0c5ddc12dd5da0b)

### path-025443

```text
(config)# kerberos timeout <number:1..10> <cr>
```

Handler ` RVA 0xC3E3030 `；selector ` 11 `；EOL ` RVA 0x33A69C38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Value 1 to 10 (default 5)。

[条件 C-9aa95ef73487754b](../../evidence/conditions-sets-060.md#c-9aa95ef73487754b) · [参数 P-7dd9d077812e6a25](../../evidence/parameters-sets-010.md#p-7dd9d077812e6a25) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027401

```text
(config)# key chain <string> <cr>
```

Handler ` RVA 0xFDB3AF0 `；selector ` 0 `；EOL ` RVA 0x348CD128 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Key-chain name。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-edc63902d937accb](../../evidence/parameters-sets-018.md#p-edc63902d937accb) · [状态效果 S-c7e462454fc91a70](../../evidence/state_effects-sets-042.md#s-c7e462454fc91a70)

### path-030531

```text
(config)# key config-key 1 <string> <cr>
```

Handler ` RVA 0xFDB3AF0 `；selector ` 1 `；EOL ` RVA 0x348CD528 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` The config-key。

[条件 C-f0d5532236745bb2](../../evidence/conditions-sets-093.md#c-f0d5532236745bb2) · [参数 P-2544abc7115d2106](../../evidence/parameters-sets-003.md#p-2544abc7115d2106) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-030565

```text
(config)# key config-key newpass <string> <cr>
```

Handler ` RVA 0xFDB3AF0 `；selector ` 3 `；EOL ` RVA 0x348CDEE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` The config-key, minimum 8 characters not beginning with IOS special         character(! # ;)。

[条件 C-eaa40cd531c6164e](../../evidence/conditions-sets-091.md#c-eaa40cd531c6164e) · [参数 P-edba5fb46b61eb6f](../../evidence/parameters-sets-018.md#p-edba5fb46b61eb6f) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-046769

```text
(config)# key config-key newpass <string> oldpass <string> <cr>
```

Handler ` RVA 0xFDB3AF0 `；selector ` 3 `；EOL ` RVA 0x348CDC50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` The config-key, minimum 8 characters not beginning with IOS special         character(! # ;)；` string ` The config-key, minimum 8 characters not beginning with IOS special         character(! # ;)。

[条件 C-7821ce5d61f3179e](../../evidence/conditions-sets-047.md#c-7821ce5d61f3179e) · [参数 P-3a3d062979a983df](../../evidence/parameters-sets-005.md#p-3a3d062979a983df) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027408

```text
(config)# key config-key password-encrypt <cr>
```

Handler ` RVA 0xFDB3AF0 `；selector ` 2 `；EOL ` RVA 0x348CD870 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8bab8d1ce57dabb4](../../evidence/conditions-sets-054.md#c-8bab8d1ce57dabb4) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-061233

```text
(config)# kron occurrence <string> in <number:0..4294967294> oneshot <cr>
```

Handler ` RVA 0xF3B88E0 `；selector ` 0 `；EOL ` RVA 0x34624468 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` The name of this occurrence。

[条件 C-cbd212948739ee82](../../evidence/conditions-sets-078.md#c-cbd212948739ee82) · [缺口 G-5f4b2d940f502dc0](../../evidence/gaps-sets-004.md#g-5f4b2d940f502dc0) · [参数 P-105ef509be8575c8](../../evidence/parameters-sets-002.md#p-105ef509be8575c8) · [状态效果 S-1d6b0f4c3fd6d2c0](../../evidence/state_effects-sets-007.md#s-1d6b0f4c3fd6d2c0)

### path-026513

```text
(config)# kron policy-list <string> <cr>
```

Handler ` RVA 0xF3BA0C0 `；selector ` 0 `；EOL ` RVA 0x34624A28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of the policy-list being defined。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-bccd29f583560c05](../../evidence/parameters-sets-014.md#p-bccd29f583560c05) · [状态效果 S-a987a332a77b2ff5](../../evidence/state_effects-sets-036.md#s-a987a332a77b2ff5)

### path-027558

```text
(config)# l2protocol-tunnel cos <number:0..7> <cr>
```

Handler ` RVA 0x15FDB140 `；selector ` 16 `；EOL ` RVA 0x35E89288 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` priority value。

[条件 C-7b05b8a405bfb311](../../evidence/conditions-sets-048.md#c-7b05b8a405bfb311) · [参数 P-2883e81853f58865](../../evidence/parameters-sets-003.md#p-2883e81853f58865) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-031241

```text
(config)# l2protocol-tunnel global drop-threshold <number:100..20000> <cr>
```

Handler ` RVA 0x15FDB140 `；selector ` 17 `；EOL ` RVA 0x35E895F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Packets per second。

[条件 C-d6b7a0c84ef3a643](../../evidence/conditions-sets-083.md#c-d6b7a0c84ef3a643) · [参数 P-1ebd439f9376f5bb](../../evidence/parameters-sets-003.md#p-1ebd439f9376f5bb) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025741

```text
(config)# l2tp congestion-control <cr>
```

Handler ` RVA 0x11EC9810 `；selector ` 0 `；EOL ` RVA 0x35744D18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026799

```text
(config)# l2tp connect-speed-update ancp <cr>
```

Handler ` RVA 0x11EC9540 `；selector ` 2 `；EOL ` RVA 0x357452D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026779

```text
(config)# l2tp connect-speed-update enable <cr>
```

Handler ` RVA 0x11EC9540 `；selector ` 1 `；EOL ` RVA 0x35745028 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-062893

```text
(config)# l2tp session l2tpv3 id min <number:dynamic> max <number:dynamic> <cr>
```

Handler ` RVA 0x11EC9810 `；selector ` 1 `；EOL ` RVA 0x35745678 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Configure the minimum L2TPv3 session ID allocatable；` unsigned_number_dynamic ` Configure the maximum L2TPv3 session ID allocatable。

[条件 C-5716134f35da9444](../../evidence/conditions-sets-034.md#c-5716134f35da9444) · [缺口 G-5efeec045ce5498a](../../evidence/gaps-sets-004.md#g-5efeec045ce5498a) · [参数 P-350a98563ed3aa30](../../evidence/parameters-sets-005.md#p-350a98563ed3aa30) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029249

```text
(config)# l2tp sso cf-flow disable <cr>
```

Handler ` RVA 0x11EC9720 `；selector ` 0 `；EOL ` RVA 0x35746AA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b417529191c8ee9c](../../evidence/conditions-sets-070.md#c-b417529191c8ee9c) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026838

```text
(config)# l2tp sso enable <cr>
```

Handler ` RVA 0x11EC9660 `；selector ` 0 `；EOL ` RVA 0x35746450 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b417529191c8ee9c](../../evidence/conditions-sets-070.md#c-b417529191c8ee9c) · [状态效果 S-6a04679c9737c68b](../../evidence/state_effects-sets-023.md#s-6a04679c9737c68b)

### path-029189

```text
(config)# l2tp sso test transform <cr>
```

Handler ` RVA 0x11EC96C0 `；selector ` 0 `；EOL ` RVA 0x35746770 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-95b686b181401df7](../../evidence/conditions-sets-058.md#c-95b686b181401df7) · [状态效果 S-5c5540a1233b3f85](../../evidence/state_effects-sets-020.md#s-5c5540a1233b3f85)

### path-026842

```text
(config)# l2tp tunnel failover-cap <cr>
```

Handler ` RVA 0x11EC9810 `；selector ` 4 `；EOL ` RVA 0x35746128 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-035133

```text
(config)# l2tp tunnel l2tpv3 accounting headers <cr>
```

Handler ` RVA 0x11EC9810 `；selector ` 2 `；EOL ` RVA 0x35745B40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029199

```text
(config)# l2tp tunnel max-sessions <number:1..65535> <cr>
```

Handler ` RVA 0x11EC9810 `；selector ` 3 `；EOL ` RVA 0x35745EA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Maximum L2TP sessions in a tunnel。

[条件 C-d33ecef63634267f](../../evidence/conditions-sets-081.md#c-d33ecef63634267f) · [参数 P-b2a0c023edd72398](../../evidence/parameters-sets-014.md#p-b2a0c023edd72398) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025742

```text
(config)# l2tp-class <string> <cr>
```

Handler ` RVA 0x11E259C0 `；selector ` 0 `；EOL ` RVA 0x357271B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` l2tp-class name。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-4e0a7ca522c03830](../../evidence/parameters-sets-006.md#p-4e0a7ca522c03830) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027012

```text
(config)# l2vpn evpn all-active-mh <cr>
```

Handler ` RVA 0x1252A5E0 `；selector ` 0 `；EOL ` RVA 0x35897678 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3fac47f5c6e46d80](../../evidence/conditions-sets-025.md#c-3fac47f5c6e46d80) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060600

```text
(config)# l2vpn evpn ethernet-segment <number:dynamic> <cr>
```

Handler ` RVA 0x1251C1A0 `；selector ` 0 `；EOL ` RVA 0x3587DD08 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Ethernet segment local discriminator value。

[条件 C-1891eb1edebe2034](../../evidence/conditions-sets-010.md#c-1891eb1edebe2034) · [缺口 G-a6fdd797a7b08c19](../../evidence/gaps-sets-006.md#g-a6fdd797a7b08c19) · [参数 P-b10f295d0552f359](../../evidence/parameters-sets-013.md#p-b10f295d0552f359) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060619

```text
(config)# l2vpn evpn instance <number:1..65535> <cr>
```

Handler ` RVA 0x1251B630 `；selector ` 0 `；EOL ` RVA 0x3587D5E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` EVPN instance identifier value。

[条件 C-819fa7440c37e8c5](../../evidence/conditions-sets-050.md#c-819fa7440c37e8c5) · [缺口 G-5535ef22330f202d](../../evidence/gaps-sets-003.md#g-5535ef22330f202d) · [参数 P-d843214e1bd7f5e1](../../evidence/parameters-sets-016.md#p-d843214e1bd7f5e1) · [状态效果 S-2388891d422e8c7d](../../evidence/state_effects-sets-008.md#s-2388891d422e8c7d)

### path-029474

```text
(config)# l2vpn evpn profile default <cr>
```

Handler ` RVA 0x12527270 `；selector ` 0 `；EOL ` RVA 0x35891A20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-f35421f409fd0b69](../../evidence/state_effects-sets-051.md#s-f35421f409fd0b69)

### path-027581

```text
(config)# lacp system-priority <number:0..65535> <cr>
```

Handler ` RVA 0xC8D1BC0 `；selector ` 6 `；EOL ` RVA 0x33B119F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Priority value。

[条件 C-3ba059eb76590d5c](../../evidence/conditions-sets-023.md#c-3ba059eb76590d5c) · [参数 P-ffcdd76d0fe146a8](../../evidence/parameters-sets-019.md#p-ffcdd76d0fe146a8) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027106

```text
(config)# ldap attribute-map <string> <cr>
```

Handler ` RVA 0x11AC0FC0 `；selector ` 0 `；EOL ` RVA 0x355E9F28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of LDAP attribute map。

[条件 C-60a963fb95c6e0be](../../evidence/conditions-sets-038.md#c-60a963fb95c6e0be) · [参数 P-c857ea6453032d8f](../../evidence/parameters-sets-015.md#p-c857ea6453032d8f) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027135

```text
(config)# ldap server <string> <cr>
```

Handler ` RVA 0x11AC0FC0 `；selector ` 3 `；EOL ` RVA 0x355EA220 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name for the ldap server configuration。

[条件 C-60a963fb95c6e0be](../../evidence/conditions-sets-038.md#c-60a963fb95c6e0be) · [参数 P-4dee8c0d04c3e542](../../evidence/parameters-sets-006.md#p-4dee8c0d04c3e542) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-043895

```text
(config)# li-view <string> user <string> password <string> <cr>
```

Handler ` RVA 0xDF752F0 `；selector ` 0 `；EOL ` RVA 0x340B65A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` LI-Password；` string ` LI Admin or User；` string ` LI Admin or User Password。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-eb8dbfcf65cd425d](../../evidence/parameters-sets-018.md#p-eb8dbfcf65cd425d) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-037933

```text
(config)# license accept end user agreement <cr>
```

Handler ` RVA 0xB791ED0 `；selector ` 0 `；EOL ` RVA 0x33806910 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b2edda0e7e70ecca](../../evidence/conditions-sets-069.md#c-b2edda0e7e70ecca) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-031094

```text
(config)# license boot level ipbase <cr>
```

Handler ` RVA 0x12420040 `；selector ` 0 `；EOL ` RVA 0x358685C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9d04f8bbf38a0f25](../../evidence/conditions-sets-061.md#c-9d04f8bbf38a0f25) · [状态效果 S-7f0d1c3b2db93789](../../evidence/state_effects-sets-027.md#s-7f0d1c3b2db93789)

### path-060696

```text
(config)# license boot level network-essentials <cr>
```

Handler ` RVA 0xB7C7D10 `；selector ` 0 `；EOL ` RVA 0x3380C800 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6e9f35456116ff45](../../evidence/conditions-sets-043.md#c-6e9f35456116ff45) · [缺口 G-ac57e4319844de76](../../evidence/gaps-sets-006.md#g-ac57e4319844de76) · [状态效果 S-63a2332b8d330e10](../../evidence/state_effects-sets-021.md#s-63a2332b8d330e10)

### path-027512

```text
(config)# license mode dna <cr>
```

Handler ` RVA 0xB7C70C0 `；selector ` 0 `；EOL ` RVA 0x3380C468 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cefe2c2013c732e2](../../evidence/conditions-sets-080.md#c-cefe2c2013c732e2) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-031107

```text
(config)# license smart conversion automatic <cr>
```

Handler ` RVA 0xBB365A0 `；selector ` 0 `；EOL ` RVA 0x33845E18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-719fff5a48b6c0c0](../../evidence/conditions-sets-044.md#c-719fff5a48b6c0c0) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027543

```text
(config)# license smart custom_id <cr>
```

Handler ` RVA 0xBB4C220 `；selector ` 0 `；EOL ` RVA 0x33846188 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-66abe39d2b6110ee](../../evidence/conditions-sets-040.md#c-66abe39d2b6110ee) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027529

```text
(config)# license smart enable <cr>
```

Handler ` RVA 0xBB33B10 `；selector ` 0 `；EOL ` RVA 0x338455B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1e06d70db459e476](../../evidence/conditions-sets-012.md#c-1e06d70db459e476) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-031047

```text
(config)# license smart enable noprompt <cr>
```

Handler ` RVA 0xBB33B10 `；selector ` 37 `；EOL ` RVA 0x33845590 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-28d47169e533de35](../../evidence/conditions-sets-016.md#c-28d47169e533de35) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-031316

```text
(config)# license smart ip-type os-default <cr>
```

Handler ` RVA 0xBB35290 `；selector ` 0 `；EOL ` RVA 0x33849CC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9ab570273d55ff0b](../../evidence/conditions-sets-060.md#c-9ab570273d55ff0b) · [状态效果 S-8e5677d52cc6f945](../../evidence/state_effects-sets-030.md#s-8e5677d52cc6f945)

### path-031342

```text
(config)# license smart log verbose <cr>
```

Handler ` RVA 0xBB35650 `；selector ` 0 `；EOL ` RVA 0x3384A518 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-198a1f7525b68a89](../../evidence/conditions-sets-010.md#c-198a1f7525b68a89) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-031331

```text
(config)# license smart onprem trust <cr>
```

Handler ` RVA 0xBB46620 `；selector ` 0 `；EOL ` RVA 0x3384A7E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-198a1f7525b68a89](../../evidence/conditions-sets-010.md#c-198a1f7525b68a89) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-031218

```text
(config)# license smart privacy all <cr>
```

Handler ` RVA 0xBB400F0 `；selector ` 0 `；EOL ` RVA 0x33848F60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a970b74df13a293e](../../evidence/conditions-sets-065.md#c-a970b74df13a293e) · [状态效果 S-445fb51f65a9495d](../../evidence/state_effects-sets-015.md#s-445fb51f65a9495d)

### path-038339

```text
(config)# license smart proxy address <string> <cr>
```

Handler ` RVA 0xBB34E90 `；selector ` 0 `；EOL ` RVA 0x33848BB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` address/hostname。

[条件 C-a970b74df13a293e](../../evidence/conditions-sets-065.md#c-a970b74df13a293e) · [参数 P-86bc3542c7aa731c](../../evidence/parameters-sets-010.md#p-86bc3542c7aa731c) · [状态效果 S-eb9f3a6a845a0027](../../evidence/state_effects-sets-050.md#s-eb9f3a6a845a0027)

### path-027527

```text
(config)# license smart reservation <cr>
```

Handler ` RVA 0xBB44320 `；selector ` 0 `；EOL ` RVA 0x33845A88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4c72e07b9c7e8141](../../evidence/conditions-sets-030.md#c-4c72e07b9c7e8141) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027565

```text
(config)# license smart server-identity-check <cr>
```

Handler ` RVA 0xBB350F0 `；selector ` 0 `；EOL ` RVA 0x33849990 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-198a1f7525b68a89](../../evidence/conditions-sets-010.md#c-198a1f7525b68a89) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-031191

```text
(config)# license smart transport smart <cr>
```

Handler ` RVA 0xBB34C60 `；selector ` 0 `；EOL ` RVA 0x338485B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-48e84f85324bb6bb](../../evidence/conditions-sets-029.md#c-48e84f85324bb6bb) · [状态效果 S-8cedcefc115a2a9a](../../evidence/state_effects-sets-030.md#s-8cedcefc115a2a9a)

### path-027584

```text
(config)# license smart url <cr>
```

Handler ` RVA 0xBB348A0 `；selector ` 0 `；EOL ` RVA 0x33847F98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6ce9dd6b91061454](../../evidence/conditions-sets-042.md#c-6ce9dd6b91061454) · [状态效果 S-6085ef4e68359722](../../evidence/state_effects-sets-021.md#s-6085ef4e68359722)

### path-031303

```text
(config)# license smart usage interval <cr>
```

Handler ` RVA 0xBB4C3E0 `；selector ` 0 `；EOL ` RVA 0x33849470 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f5c0362562362cad](../../evidence/conditions-sets-095.md#c-f5c0362562362cad) · [状态效果 S-9fa4a15e973a9d18](../../evidence/state_effects-sets-034.md#s-9fa4a15e973a9d18)

### path-027542

```text
(config)# license smart utility <cr>
```

Handler ` RVA 0xBB4B460 `；selector ` 0 `；EOL ` RVA 0x33846498 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a970b74df13a293e](../../evidence/conditions-sets-065.md#c-a970b74df13a293e) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-038424

```text
(config)# license smart utility customer_info city <cr>
```

Handler ` RVA 0xBB4BAE0 `；selector ` 0 `；EOL ` RVA 0x33846FD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-562fa831d43b30f9](../../evidence/conditions-sets-034.md#c-562fa831d43b30f9) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-038516

```text
(config)# license smart utility customer_info country <cr>
```

Handler ` RVA 0xBB4B740 `；selector ` 0 `；EOL ` RVA 0x33847698 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5dc289b4ef273975](../../evidence/conditions-sets-037.md#c-5dc289b4ef273975) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-038275

```text
(config)# license smart utility customer_info id <cr>
```

Handler ` RVA 0xBB4C050 `；selector ` 0 `；EOL ` RVA 0x338465B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7c95b6c407ad29c9](../../evidence/conditions-sets-048.md#c-7c95b6c407ad29c9) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-038327

```text
(config)# license smart utility customer_info name <cr>
```

Handler ` RVA 0xBB4BE80 `；selector ` 0 `；EOL ` RVA 0x33846918 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3b18126475a2bec7](../../evidence/conditions-sets-023.md#c-3b18126475a2bec7) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-038561

```text
(config)# license smart utility customer_info postalcode <cr>
```

Handler ` RVA 0xBB4B570 `；selector ` 0 `；EOL ` RVA 0x338479D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-298f24626b487d76](../../evidence/conditions-sets-016.md#c-298f24626b487d76) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-038466

```text
(config)# license smart utility customer_info state <cr>
```

Handler ` RVA 0xBB4B910 `；selector ` 0 `；EOL ` RVA 0x33847338 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-be843d049c0aa664](../../evidence/conditions-sets-074.md#c-be843d049c0aa664) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-038383

```text
(config)# license smart utility customer_info street <cr>
```

Handler ` RVA 0xBB4BCB0 `；selector ` 0 `；EOL ` RVA 0x33846C78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-73b3c753c8f05873](../../evidence/conditions-sets-045.md#c-73b3c753c8f05873) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027583

```text
(config)# license smart vrf <cr>
```

Handler ` RVA 0xBB354F0 `；selector ` 0 `；EOL ` RVA 0x3384A1F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-30fccb34d5b2e38c](../../evidence/conditions-sets-019.md#c-30fccb34d5b2e38c) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025964

```text
(config)# license udi <cr>
```

Handler ` RVA 0xB7939A0 `；selector ` 0 `；EOL ` RVA 0x338063E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0ff9af1eb9bec578](../../evidence/conditions-sets-006.md#c-0ff9af1eb9bec578) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060301

```text
(config)# line <?ttyline_action@5555896718b8> <cr>
```

Handler ` RVA 0xE059390 `；selector ` 17 `；EOL ` RVA 0x3411DB38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [缺口 G-438d6ed855970c8a](../../evidence/gaps-sets-003.md#g-438d6ed855970c8a) · [状态效果 S-f47010f40e1294de](../../evidence/state_effects-sets-052.md#s-f47010f40e1294de)

### path-025892

```text
(config)# line auto-consolidation <cr>
```

Handler ` RVA 0xE059390 `；selector ` 41 `；EOL ` RVA 0x3411D890 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-f47010f40e1294de](../../evidence/state_effects-sets-052.md#s-f47010f40e1294de)

### path-026350

```text
(config)# lldp custom-network-hash <string> <cr>
```

Handler ` RVA 0x1589CEF0 `；selector ` 24 `；EOL ` RVA 0x35DA2ED0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` custom Network Hash Value。

[条件 C-342f69943d52d657](../../evidence/conditions-sets-020.md#c-342f69943d52d657) · [参数 P-0876c0756d2fb517](../../evidence/parameters-sets-001.md#p-0876c0756d2fb517) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025434

```text
(config)# lldp holdtime <number:0..65535> <cr>
```

Handler ` RVA 0x1589CEF0 `；selector ` 2 `；EOL ` RVA 0x35DA1340 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Length	of time	(in sec) that receiver must keep this packet 。

[条件 C-11fdaea01406250b](../../evidence/conditions-sets-007.md#c-11fdaea01406250b) · [参数 P-a5c0b504e7fa91cd](../../evidence/parameters-sets-013.md#p-a5c0b504e7fa91cd) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060527

```text
(config)# lldp management-address ipv4 <address> <cr>
```

Handler ` RVA 0x158A56D0 `；selector ` 1 `；EOL ` RVA 0x35DA32D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` IPV4 management address。

[条件 C-183a665b9c33b8bc](../../evidence/conditions-sets-009.md#c-183a665b9c33b8bc) · [缺口 G-23868ea5f54c2650](../../evidence/gaps-sets-002.md#g-23868ea5f54c2650) · [参数 P-eef66f921355c4c4](../../evidence/parameters-sets-018.md#p-eef66f921355c4c4) · [状态效果 S-93062388c3ffbbfe](../../evidence/state_effects-sets-031.md#s-93062388c3ffbbfe)

### path-060528

```text
(config)# lldp management-address ipv6 <address> <cr>
```

Handler ` RVA 0x158A5BF0 `；selector ` 1 `；EOL ` RVA 0x35DA3640 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` IPV6 management address。

[条件 C-183a665b9c33b8bc](../../evidence/conditions-sets-009.md#c-183a665b9c33b8bc) · [缺口 G-beb38b0c79953482](../../evidence/gaps-sets-007.md#g-beb38b0c79953482) · [参数 P-10fc4d6fc8dc8176](../../evidence/parameters-sets-002.md#p-10fc4d6fc8dc8176) · [状态效果 S-777fbae7b5564a2b](../../evidence/state_effects-sets-025.md#s-777fbae7b5564a2b)

### path-026324

```text
(config)# lldp management-vlan <number:1..4095> <cr>
```

Handler ` RVA 0x1589CEF0 `；selector ` 22 `；EOL ` RVA 0x35DA27C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Management Vlan ID。

[条件 C-627d490d5f370410](../../evidence/conditions-sets-038.md#c-627d490d5f370410) · [参数 P-972ea0c2050c312b](../../evidence/parameters-sets-012.md#p-972ea0c2050c312b) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025436

```text
(config)# lldp reinit <number:2..5> <cr>
```

Handler ` RVA 0x1589CEF0 `；selector ` 3 `；EOL ` RVA 0x35DA15E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Specify the delay (in secs) for LLDP to initialize。

[条件 C-5a9b3a0e668fc973](../../evidence/conditions-sets-035.md#c-5a9b3a0e668fc973) · [参数 P-15f34a8e6cf76517](../../evidence/parameters-sets-002.md#p-15f34a8e6cf76517) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025620

```text
(config)# lldp run <cr>
```

Handler ` RVA 0x1589CEF0 `；selector ` 0 `；EOL ` RVA 0x35DA3918 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-428840d72836e01d](../../evidence/conditions-sets-026.md#c-428840d72836e01d) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-034185

```text
(config)# lldp system-name <string> switch-id <number:0..16> <cr>
```

Handler ` RVA 0x1589CEF0 `；selector ` 23 `；EOL ` RVA 0x35DA2B70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` System name per switch ID(220 characters max)；` unsigned_number ` Switch ID。

[条件 C-183a665b9c33b8bc](../../evidence/conditions-sets-009.md#c-183a665b9c33b8bc) · [参数 P-c4e5e481d4cef83a](../../evidence/parameters-sets-015.md#p-c4e5e481d4cef83a) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025432

```text
(config)# lldp timer <number:5..65534> <cr>
```

Handler ` RVA 0x1589CEF0 `；selector ` 1 `；EOL ` RVA 0x35DA1300 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Rate at which LLDP packets are sent (in sec)。

[条件 C-d4d2d4f9b7790fe8](../../evidence/conditions-sets-082.md#c-d4d2d4f9b7790fe8) · [参数 P-b845870a9a101634](../../evidence/parameters-sets-014.md#p-b845870a9a101634) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026233

```text
(config)# lldp tlv-select management-address <cr>
```

Handler ` RVA 0x1589CEF0 `；selector ` 7 `；EOL ` RVA 0x35DA1B88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-da52acb38cb4b910](../../evidence/state_effects-sets-046.md#s-da52acb38cb4b910)

### path-059619

```text
(config)# lldp ucs-tlv ipv6 <address> mgmt-port <number:1..65534> infra-vlan <number:1..4095> cluster-id <string> <cr>
```

Handler ` RVA 0x158A4F00 `；selector ` 20 `；EOL ` RVA 0x35DA23E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Management IPv6 prefix/len；` unsigned_number ` Specify management port number；` unsigned_number ` Vlan ID；` string ` Cluster ID。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-c81424293397cf9e](../../evidence/parameters-sets-015.md#p-c81424293397cf9e) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025670

```text
(config)# lnm disabled <cr>
```

Handler ` RVA 0x12338E90 `；selector ` 11 `；EOL ` RVA 0x35814410 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-371f7f59e9ff01f5](../../evidence/conditions-sets-021.md#c-371f7f59e9ff01f5) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025704

```text
(config)# lnm pathtrace-disabled <cr>
```

Handler ` RVA 0x12338E90 `；selector ` 13 `；EOL ` RVA 0x35814730 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-371f7f59e9ff01f5](../../evidence/conditions-sets-021.md#c-371f7f59e9ff01f5) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025664

```text
(config)# lnm snmp-only <cr>
```

Handler ` RVA 0x12338E90 `；selector ` 8 `；EOL ` RVA 0x35814168 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-371f7f59e9ff01f5](../../evidence/conditions-sets-021.md#c-371f7f59e9ff01f5) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060370

```text
(config)# load protocol <?fpm_protocol_action@55558935a170> <cr>
```

Handler ` RVA 0xD2DF680 `；selector ` 0 `；EOL ` RVA 0x33E061B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9187ddf4e280b0ba](../../evidence/conditions-sets-056.md#c-9187ddf4e280b0ba) · [缺口 G-5a7db55cafc772f9](../../evidence/gaps-sets-004.md#g-5a7db55cafc772f9) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-028568

```text
(config)# locaddr-priority-list <number:1..10> <number:0..255> high <cr>
```

Handler ` RVA 0x1E53BD20 `；selector ` 0 `；EOL ` RVA 0x35516828 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` LU address priority list；` unsigned_number ` One-byte LU addr (in hex)。

[条件 C-64b86689f19001fa](../../evidence/conditions-sets-039.md#c-64b86689f19001fa) · [参数 P-103dbe9ff988245e](../../evidence/parameters-sets-002.md#p-103dbe9ff988245e) · [状态效果 S-0c8483e24b3d66da](../../evidence/state_effects-sets-003.md#s-0c8483e24b3d66da)

### path-026537

```text
(config)# location admin-tag <string> <cr>
```

Handler ` RVA 0xC914B40 `；selector ` 0 `；EOL ` RVA 0x33B1C128 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` admin-tag string。

[条件 C-3f2972e5b3acbbf7](../../evidence/conditions-sets-024.md#c-3f2972e5b3acbbf7) · [参数 P-8852a01a5a1e7595](../../evidence/parameters-sets-011.md#p-8852a01a5a1e7595) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-028365

```text
(config)# location civic-location identifier host <cr>
```

Handler ` RVA 0xC914380 `；selector ` 0 `；EOL ` RVA 0x33B1B188 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-7d6be013a33e9c8a](../../evidence/state_effects-sets-027.md#s-7d6be013a33e9c8a)

### path-028379

```text
(config)# location custom-location identifier host <cr>
```

Handler ` RVA 0xC8F5140 `；selector ` 0 `；EOL ` RVA 0x33B1B918 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-391e965e504b5347](../../evidence/state_effects-sets-013.md#s-391e965e504b5347)

### path-034388

```text
(config)# location elin-location <string> identifier <string> <cr>
```

Handler ` RVA 0xC914980 `；selector ` 0 `；EOL ` RVA 0x33B1B5A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` elin string；` string ` elin identifier string。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-144120eda0224c98](../../evidence/parameters-sets-002.md#p-144120eda0224c98) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-028413

```text
(config)# location geo-location identifier host <cr>
```

Handler ` RVA 0xC90B6B0 `；selector ` 0 `；EOL ` RVA 0x33B1BD40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-eb2e05d4b600b13d](../../evidence/state_effects-sets-050.md#s-eb2e05d4b600b13d)

### path-026462

```text
(config)# location prefer cdp weight <number:0..255> <cr>
```

Handler ` RVA 0xC914E70 `；selector ` 3 `；EOL ` RVA 0x33B1AD40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` priority value。

[条件 C-2eed18906b153405](../../evidence/conditions-sets-018.md#c-2eed18906b153405) · [参数 P-1eace1aad0cd6617](../../evidence/parameters-sets-003.md#p-1eace1aad0cd6617) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026406

```text
(config)# location prefer lldp-med weight <number:0..255> <cr>
```

Handler ` RVA 0xC914E70 `；selector ` 2 `；EOL ` RVA 0x33B1AA10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` priority value。

[条件 C-2af717325e821f3d](../../evidence/conditions-sets-017.md#c-2af717325e821f3d) · [参数 P-3c5bdc6ed4a4847c](../../evidence/parameters-sets-005.md#p-3c5bdc6ed4a4847c) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026383

```text
(config)# location prefer static weight <number:0..255> <cr>
```

Handler ` RVA 0xC914E70 `；selector ` 0 `；EOL ` RVA 0x33B1A720 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` priority value。

[条件 C-1f3d4b65a74e10a3](../../evidence/conditions-sets-012.md#c-1f3d4b65a74e10a3) · [参数 P-7459b423d7699357](../../evidence/parameters-sets-009.md#p-7459b423d7699357) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-063024

```text
(config)# log-export local <cr>
```

Handler ` RVA 0xDF978A0 `；selector ` 0 `；EOL ` 历史 VA 0x7FFF37DA6E58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1f7995542cf87bc0](../../evidence/conditions-sets-012.md#c-1f7995542cf87bc0) · [缺口 G-91dddd84498a8b5a](../../evidence/gaps-sets-005.md#g-91dddd84498a8b5a) · [状态效果 S-73ba9df0dbaf3477](../../evidence/state_effects-sets-025.md#s-73ba9df0dbaf3477)

### path-063026

```text
(config)# log-export local <cr>
```

Handler ` RVA 0xDF978A0 `；selector ` 0 `；EOL ` 历史 VA 0x7FFF37DA6978 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b160290e5a3c1425](../../evidence/conditions-sets-069.md#c-b160290e5a3c1425) · [缺口 G-33588dbc34084b24](../../evidence/gaps-sets-002.md#g-33588dbc34084b24) · [状态效果 S-4f7af5546a4ec912](../../evidence/state_effects-sets-017.md#s-4f7af5546a4ec912)

### path-060298

```text
(config)# logging <address> <cr>
```

Handler ` RVA 0xD00DB30 `；selector ` 0 `；EOL ` RVA 0x33D81630 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` IP address of the logging host。

[条件 C-51d408757a6285f6](../../evidence/conditions-sets-032.md#c-51d408757a6285f6) · [缺口 G-cd940467ddf9caf6](../../evidence/gaps-sets-007.md#g-cd940467ddf9caf6) · [参数 P-2099768b58f5e61f](../../evidence/parameters-sets-003.md#p-2099768b58f5e61f) · [状态效果 S-e6bf4723e4e2df2a](../../evidence/state_effects-sets-049.md#s-e6bf4723e4e2df2a)

### path-060292

```text
(config)# logging alarm <cr>
```

Handler ` RVA 0xC2A0FB0 `；selector ` 1 `；EOL ` RVA 0x33A2AF70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f43a6b84d5c49658](../../evidence/conditions-sets-094.md#c-f43a6b84d5c49658) · [缺口 G-cd940467ddf9caf6](../../evidence/gaps-sets-007.md#g-cd940467ddf9caf6) · [状态效果 S-e6bf4723e4e2df2a](../../evidence/state_effects-sets-049.md#s-e6bf4723e4e2df2a)

### path-025564

```text
(config)# logging buginf <cr>
```

Handler ` RVA 0xE0621F0 `；selector ` 33 `；EOL ` RVA 0x3418CBC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0f9a18191ddbbac7](../../evidence/conditions-sets-006.md#c-0f9a18191ddbbac7) · [状态效果 S-1bf399712ec8d45f](../../evidence/state_effects-sets-006.md#s-1bf399712ec8d45f)

### path-025546

```text
(config)# logging count <cr>
```

Handler ` RVA 0xE0621F0 `；selector ` 5 `；EOL ` RVA 0x3418BE58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c242923f2a4a8e0d](../../evidence/conditions-sets-075.md#c-c242923f2a4a8e0d) · [状态效果 S-78d3d44e1d81d6db](../../evidence/state_effects-sets-026.md#s-78d3d44e1d81d6db)

### path-060394

```text
(config)# logging delimiter tcp <cr>
```

Handler ` RVA 0xD00DB30 `；selector ` 9 `；EOL ` RVA 0x33D820D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [缺口 G-cd940467ddf9caf6](../../evidence/gaps-sets-007.md#g-cd940467ddf9caf6) · [状态效果 S-e6bf4723e4e2df2a](../../evidence/state_effects-sets-049.md#s-e6bf4723e4e2df2a)

### path-026174

```text
(config)# logging discriminator <string> <cr>
```

Handler ` RVA 0xE0621F0 `；selector ` 6 `；EOL ` RVA 0x3418A300 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` discriminator name; string; max. 8 characters。

[条件 C-7615c0a76e9e477b](../../evidence/conditions-sets-046.md#c-7615c0a76e9e477b) · [参数 P-22481203d7ac661c](../../evidence/parameters-sets-003.md#p-22481203d7ac661c) · [状态效果 S-cd2b07084d34bdfa](../../evidence/state_effects-sets-043.md#s-cd2b07084d34bdfa)

### path-061208

```text
(config)# logging discriminator <string> msg-body includes <string> <cr>
```

Handler ` RVA 0xE0621F0 `；selector ` 6 `；EOL ` RVA 0x3418A300 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` discriminator name; string; max. 8 characters；` string ` Specify a regular expression string for message filtering。

[条件 C-bb8e2b0a12d9af0d](../../evidence/conditions-sets-072.md#c-bb8e2b0a12d9af0d) · [缺口 G-4130761d3f3b460c](../../evidence/gaps-sets-003.md#g-4130761d3f3b460c) · [参数 P-be5225bfd1de8bfa](../../evidence/parameters-sets-014.md#p-be5225bfd1de8bfa) · [状态效果 S-6fa8ecd8ad8914a3](../../evidence/state_effects-sets-024.md#s-6fa8ecd8ad8914a3)

### path-060291

```text
(config)# logging dmvpn <cr>
```

Handler ` RVA 0xF4F2D00 `；selector ` 2 `；EOL ` RVA 0x3467E7C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-15c91ccb8c0ed410](../../evidence/conditions-sets-009.md#c-15c91ccb8c0ed410) · [缺口 G-cd940467ddf9caf6](../../evidence/gaps-sets-007.md#g-cd940467ddf9caf6) · [状态效果 S-e6bf4723e4e2df2a](../../evidence/state_effects-sets-049.md#s-e6bf4723e4e2df2a)

### path-060389

```text
(config)# logging esm config <cr>
```

Handler ` RVA 0xCC446D0 `；selector ` 32 `；EOL ` RVA 0x33C24EC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [缺口 G-cd940467ddf9caf6](../../evidence/gaps-sets-007.md#g-cd940467ddf9caf6) · [状态效果 S-e6bf4723e4e2df2a](../../evidence/state_effects-sets-049.md#s-e6bf4723e4e2df2a)

### path-028198

```text
(config)# logging event link-status global <cr>
```

Handler ` RVA 0xE060840 `；selector ` 1 `；EOL ` RVA 0x3418F2C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-96789cc8e92a00a9](../../evidence/conditions-sets-058.md#c-96789cc8e92a00a9) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-028220

```text
(config)# logging event trunk-status global <cr>
```

Handler ` RVA 0xE060840 `；selector ` 2 `；EOL ` RVA 0x3418F598 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-96789cc8e92a00a9](../../evidence/conditions-sets-058.md#c-96789cc8e92a00a9) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026092

```text
(config)# logging exception <number:4096..2147483647> <cr>
```

Handler ` RVA 0xE0621F0 `；selector ` 25 `；EOL ` RVA 0x3418BB20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Set size of logging exception flush。

[条件 C-a1831026f16a91ef](../../evidence/conditions-sets-062.md#c-a1831026f16a91ef) · [参数 P-3569cf288e14097d](../../evidence/parameters-sets-005.md#p-3569cf288e14097d) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060296

```text
(config)# logging facility <cr>
```

Handler ` RVA 0xD00DB30 `；selector ` 2 `；EOL ` RVA 0x33D830E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3da24a11db993ed6](../../evidence/conditions-sets-024.md#c-3da24a11db993ed6) · [缺口 G-cd940467ddf9caf6](../../evidence/gaps-sets-007.md#g-cd940467ddf9caf6) · [状态效果 S-e6bf4723e4e2df2a](../../evidence/state_effects-sets-049.md#s-e6bf4723e4e2df2a)

### path-060380

```text
(config)# logging file <url:dynamic> <cr>
```

Handler ` RVA 0xE0621F0 `；selector ` 24 `；EOL ` RVA 0x3418B4F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-05bb2904aabb36c8](../../evidence/conditions-sets-003.md#c-05bb2904aabb36c8) · [缺口 G-611f7c589597064d](../../evidence/gaps-sets-004.md#g-611f7c589597064d) · [参数 P-aded43e4dfc18ad5](../../evidence/parameters-sets-013.md#p-aded43e4dfc18ad5) · [状态效果 S-e60714e8877aa460](../../evidence/state_effects-sets-049.md#s-e60714e8877aa460)

### path-062717

```text
(config)# logging filter <url:dynamic> <cr>
```

Handler ` RVA 0xCC448D0 `；selector ` 31 `；EOL ` RVA 0x33C24B30 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e57686e452d6062e](../../evidence/conditions-sets-088.md#c-e57686e452d6062e) · [缺口 G-e03ab4245874b866](../../evidence/gaps-sets-008.md#g-e03ab4245874b866) · [参数 P-a75c0be874c801b8](../../evidence/parameters-sets-013.md#p-a75c0be874c801b8) · [状态效果 S-e6bf4723e4e2df2a](../../evidence/state_effects-sets-049.md#s-e6bf4723e4e2df2a)

### path-060392

```text
(config)# logging history emergencies <cr>
```

Handler ` RVA 0x123A10C0 `；selector ` 0 `；EOL ` RVA 0x35832DA8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [缺口 G-cd940467ddf9caf6](../../evidence/gaps-sets-007.md#g-cd940467ddf9caf6) · [状态效果 S-4796525102c37a57](../../evidence/state_effects-sets-016.md#s-4796525102c37a57)

### path-060290

```text
(config)# logging history size <number:0..500> <cr>
```

Handler ` RVA 0x123A10C0 `；selector ` 1 `；EOL ` RVA 0x35832A80 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` History size。

[条件 C-833fa3df8176d1f0](../../evidence/conditions-sets-051.md#c-833fa3df8176d1f0) · [缺口 G-6d6592122ccf27d3](../../evidence/gaps-sets-004.md#g-6d6592122ccf27d3) · [参数 P-7794c9bbf78c4b32](../../evidence/parameters-sets-009.md#p-7794c9bbf78c4b32) · [状态效果 S-56bd8b40b0a45634](../../evidence/state_effects-sets-019.md#s-56bd8b40b0a45634)

### path-060408

```text
(config)# logging host <address> <cr>
```

Handler ` RVA 0xD00DB30 `；selector ` 5 `；EOL ` RVA 0x33D802C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` IP address of the syslog server。

[条件 C-095be4d541b7d374](../../evidence/conditions-sets-004.md#c-095be4d541b7d374) · [缺口 G-cd940467ddf9caf6](../../evidence/gaps-sets-007.md#g-cd940467ddf9caf6) · [参数 P-dc93d05aa2e33d16](../../evidence/parameters-sets-017.md#p-dc93d05aa2e33d16) · [状态效果 S-e6bf4723e4e2df2a](../../evidence/state_effects-sets-049.md#s-e6bf4723e4e2df2a)

### path-026127

```text
(config)# logging message-counter log <cr>
```

Handler ` RVA 0xE0621F0 `；selector ` 17 `；EOL ` RVA 0x3418C1D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3fe8220bf3d25486](../../evidence/conditions-sets-025.md#c-3fe8220bf3d25486) · [状态效果 S-93fac43205c56b52](../../evidence/state_effects-sets-031.md#s-93fac43205c56b52)

### path-025623

```text
(config)# logging on <cr>
```

Handler ` RVA 0xE0621F0 `；selector ` 23 `；EOL ` RVA 0x3418EF00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0a85a91897d46078](../../evidence/conditions-sets-004.md#c-0a85a91897d46078) · [状态效果 S-20e98299498bbcc5](../../evidence/state_effects-sets-007.md#s-20e98299498bbcc5)

### path-060294

```text
(config)# logging origin-id <cr>
```

Handler ` RVA 0xD00DB30 `；selector ` 6 `；EOL ` RVA 0x33D82420 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-674d76f574623729](../../evidence/conditions-sets-040.md#c-674d76f574623729) · [缺口 G-cd940467ddf9caf6](../../evidence/gaps-sets-007.md#g-cd940467ddf9caf6) · [状态效果 S-e6bf4723e4e2df2a](../../evidence/state_effects-sets-049.md#s-e6bf4723e4e2df2a)

### path-025658

```text
(config)# logging persistent <cr>
```

Handler ` RVA 0xE0621F0 `；selector ` 4 `；EOL ` RVA 0x3418DFB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fe9ef51bf0f67cef](../../evidence/conditions-sets-098.md#c-fe9ef51bf0f67cef) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060532

```text
(config)# logging persistent threshold <number:dynamic> <cr>
```

Handler ` RVA 0xE0621F0 `；selector ` 4 `；EOL ` RVA 0x3418DFB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Setting threshold capacity. When setting circular logging is disabled。

[条件 C-004a80eaa65eec10](../../evidence/conditions-sets-001.md#c-004a80eaa65eec10) · [缺口 G-945bbb4ee3066832](../../evidence/gaps-sets-005.md#g-945bbb4ee3066832) · [参数 P-eabda5e10a7bc07f](../../evidence/parameters-sets-018.md#p-eabda5e10a7bc07f) · [状态效果 S-a1ea3311ab668274](../../evidence/state_effects-sets-034.md#s-a1ea3311ab668274)

### path-028292

```text
(config)# logging prefix version <number:1..2> <cr>
```

Handler ` RVA 0xE0621F0 `；selector ` 29 `；EOL ` RVA 0x3418F978 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Logging prefix version number。

[条件 C-3cbe0b8e56a77c6b](../../evidence/conditions-sets-024.md#c-3cbe0b8e56a77c6b) · [参数 P-b5d143e084bf3bc0](../../evidence/parameters-sets-014.md#p-b5d143e084bf3bc0) · [状态效果 S-bc148c6cec214eb8](../../evidence/state_effects-sets-040.md#s-bc148c6cec214eb8)

### path-034114

```text
(config)# logging purge-log buffer days <number:1..120> <cr>
```

Handler ` RVA 0xE0621F0 `；selector ` 39 `；EOL ` RVA 0x3418D9B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of days。

[条件 C-67508aff0dd312b5](../../evidence/conditions-sets-040.md#c-67508aff0dd312b5) · [参数 P-762c69697d603d82](../../evidence/parameters-sets-009.md#p-762c69697d603d82) · [状态效果 S-e24cfd8f5f17bd8f](../../evidence/state_effects-sets-048.md#s-e24cfd8f5f17bd8f)

### path-061836

```text
(config)# logging purge-log buffer days <number:1..120> time <hh:mm> <cr>
```

Handler ` RVA 0xE0621F0 `；selector ` 39 `；EOL ` RVA 0x3418D9B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Number of days；` time_hm ` Deletion start time。

[条件 C-3a0f0891f4187e97](../../evidence/conditions-sets-022.md#c-3a0f0891f4187e97) · [缺口 G-acd94106553635f2](../../evidence/gaps-sets-006.md#g-acd94106553635f2) · [参数 P-46dd74fd969eee02](../../evidence/parameters-sets-006.md#p-46dd74fd969eee02) · [状态效果 S-efe47b9a88dafbc4](../../evidence/state_effects-sets-051.md#s-efe47b9a88dafbc4)

### path-025599

```text
(config)# logging queue-limit <cr>
```

Handler ` RVA 0xE0621F0 `；selector ` 19 `；EOL ` RVA 0x3418D218 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6a0de5a3dff7c4d4](../../evidence/conditions-sets-041.md#c-6a0de5a3dff7c4d4) · [状态效果 S-081e4592c0e76db0](../../evidence/state_effects-sets-002.md#s-081e4592c0e76db0)

### path-025569

```text
(config)# logging radioactive-trace <cr>
```

Handler ` RVA 0xE0621F0 `；selector ` 38 `；EOL ` RVA 0x3418CED8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4fa31606dbab194a](../../evidence/conditions-sets-031.md#c-4fa31606dbab194a) · [状态效果 S-b1979d9e7ef0b6ea](../../evidence/state_effects-sets-038.md#s-b1979d9e7ef0b6ea)

### path-060295

```text
(config)# logging server-arp <cr>
```

Handler ` RVA 0xD00DB30 `；selector ` 8 `；EOL ` RVA 0x33D82D80 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [缺口 G-cd940467ddf9caf6](../../evidence/gaps-sets-007.md#g-cd940467ddf9caf6) · [状态效果 S-e6bf4723e4e2df2a](../../evidence/state_effects-sets-049.md#s-e6bf4723e4e2df2a)

### path-025557

```text
(config)# logging snmp-authfail <cr>
```

Handler ` RVA 0xE0621F0 `；selector ` 26 `；EOL ` RVA 0x3418C590 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db2d2f96810dfa7](../../evidence/conditions-sets-030.md#c-4db2d2f96810dfa7) · [状态效果 S-c6a2bfe116378fed](../../evidence/state_effects-sets-042.md#s-c6a2bfe116378fed)

### path-060398

```text
(config)# logging snmp-trap emergencies <cr>
```

Handler ` RVA 0xD00DB30 `；selector ` 7 `；EOL ` RVA 0x33D80FB0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [缺口 G-cd940467ddf9caf6](../../evidence/gaps-sets-007.md#g-cd940467ddf9caf6) · [状态效果 S-4c8526c7e907afdb](../../evidence/state_effects-sets-017.md#s-4c8526c7e907afdb)

### path-060297

```text
(config)# logging source-interface <cr>
```

Handler ` RVA 0xD00DB30 `；selector ` 4 `；EOL ` RVA 0x33D82A40 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7b65eb5b8a8a3995](../../evidence/conditions-sets-048.md#c-7b65eb5b8a8a3995) · [缺口 G-cd940467ddf9caf6](../../evidence/gaps-sets-007.md#g-cd940467ddf9caf6) · [状态效果 S-e6bf4723e4e2df2a](../../evidence/state_effects-sets-049.md#s-e6bf4723e4e2df2a)

### path-025649

```text
(config)# logging syslog-events <cr>
```

Handler ` RVA 0xE0621F0 `；selector ` 24 `；EOL ` RVA 0x3418B4F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-206f49d6b8e67ec0](../../evidence/conditions-sets-013.md#c-206f49d6b8e67ec0) · [状态效果 S-0ee986e177fa1360](../../evidence/state_effects-sets-004.md#s-0ee986e177fa1360)

### path-060399

```text
(config)# logging tls-profile <string> <cr>
```

Handler ` RVA 0x123AE180 `；selector ` 0 `；EOL ` RVA 0x35841FC8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` TLS profile name. Max 30 chars。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [缺口 G-cd940467ddf9caf6](../../evidence/gaps-sets-007.md#g-cd940467ddf9caf6) · [参数 P-c72140cbffc37939](../../evidence/parameters-sets-015.md#p-c72140cbffc37939) · [状态效果 S-e6bf4723e4e2df2a](../../evidence/state_effects-sets-049.md#s-e6bf4723e4e2df2a)

### path-060293

```text
(config)# logging trap <cr>
```

Handler ` RVA 0xD00DB30 `；selector ` 1 `；EOL ` RVA 0x33D819E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1dce419f586e8427](../../evidence/conditions-sets-012.md#c-1dce419f586e8427) · [缺口 G-cd940467ddf9caf6](../../evidence/gaps-sets-007.md#g-cd940467ddf9caf6) · [状态效果 S-e6bf4723e4e2df2a](../../evidence/state_effects-sets-049.md#s-e6bf4723e4e2df2a)

### path-025561

```text
(config)# logging userinfo <cr>
```

Handler ` RVA 0xE0621F0 `；selector ` 27 `；EOL ` RVA 0x3418C8A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8cdb433819178fa4](../../evidence/conditions-sets-055.md#c-8cdb433819178fa4) · [状态效果 S-fb9aa262d89b33a3](../../evidence/state_effects-sets-053.md#s-fb9aa262d89b33a3)

### path-052322

```text
(config)# login block-for <number:1..65535> attempts <number:1..65535> within <number:1..65535> <cr>
```

Handler ` RVA 0xCFD1FB0 `；selector ` 1 `；EOL ` RVA 0x33D73248 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Time period in seconds；` unsigned_number ` Fail attempts max value；` unsigned_number ` Time period in seconds。

[条件 C-46b4aeb6f94b14b8](../../evidence/conditions-sets-028.md#c-46b4aeb6f94b14b8) · [参数 P-6ceaff6eebc9ba35](../../evidence/parameters-sets-009.md#p-6ceaff6eebc9ba35) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026574

```text
(config)# login delay <number:1..10> <cr>
```

Handler ` RVA 0xCFD1FB0 `；selector ` 2 `；EOL ` RVA 0x33D736C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Time period in seconds。

[条件 C-c4881bbc54c20dd4](../../evidence/conditions-sets-076.md#c-c4881bbc54c20dd4) · [参数 P-116045b4ec17d014](../../evidence/parameters-sets-002.md#p-116045b4ec17d014) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025710

```text
(config)# login on-failure <cr>
```

Handler ` RVA 0xCFD1FB0 `；selector ` 6 `；EOL ` RVA 0x33D74320 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025714

```text
(config)# login on-success <cr>
```

Handler ` RVA 0xCFD1FB0 `；selector ` 5 `；EOL ` RVA 0x33D746F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026665

```text
(config)# login password-reuse-interval <number:1..365> <cr>
```

Handler ` RVA 0xCFD1FB0 `；selector ` 13 `；EOL ` RVA 0x33D75ED8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Time period in days。

[条件 C-b2819a3105e1a1eb](../../evidence/conditions-sets-069.md#c-b2819a3105e1a1eb) · [参数 P-2040c79e1d25a845](../../evidence/parameters-sets-003.md#p-2040c79e1d25a845) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-028876

```text
(config)# login password-warning-interval days <number:0..30> <cr>
```

Handler ` RVA 0xCFD1FB0 `；selector ` 12 `；EOL ` RVA 0x33D75B68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of days。

[条件 C-d08b5d6c02533b97](../../evidence/conditions-sets-080.md#c-d08b5d6c02533b97) · [参数 P-5ab72a924064c4f4](../../evidence/parameters-sets-007.md#p-5ab72a924064c4f4) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-028723

```text
(config)# login password-warning-interval hours <number:0..23> <cr>
```

Handler ` RVA 0xCFD1FB0 `；selector ` 9 `；EOL ` RVA 0x33D751A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of hours。

[条件 C-332af8458e803968](../../evidence/conditions-sets-020.md#c-332af8458e803968) · [参数 P-ccba6c63d5f34972](../../evidence/parameters-sets-016.md#p-ccba6c63d5f34972) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-028818

```text
(config)# login password-warning-interval minutes <number:0..59> <cr>
```

Handler ` RVA 0xCFD1FB0 `；selector ` 11 `；EOL ` RVA 0x33D75840 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of minutes。

[条件 C-737a73b931913c32](../../evidence/conditions-sets-045.md#c-737a73b931913c32) · [参数 P-62e83cae494532cd](../../evidence/parameters-sets-008.md#p-62e83cae494532cd) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-028764

```text
(config)# login password-warning-interval months <number:0..11> <cr>
```

Handler ` RVA 0xCFD1FB0 `；selector ` 10 `；EOL ` RVA 0x33D754F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of months。

[条件 C-cb59291513dbb3a0](../../evidence/conditions-sets-078.md#c-cb59291513dbb3a0) · [参数 P-40f70b6b79d54a93](../../evidence/parameters-sets-005.md#p-40f70b6b79d54a93) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-028689

```text
(config)# login password-warning-interval seconds <number:0..59> <cr>
```

Handler ` RVA 0xCFD1FB0 `；selector ` 8 `；EOL ` RVA 0x33D74E50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of seconds。

[条件 C-e0fd5667d0b4525c](../../evidence/conditions-sets-087.md#c-e0fd5667d0b4525c) · [参数 P-30f7279344b9d2e1](../../evidence/parameters-sets-004.md#p-30f7279344b9d2e1) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-028652

```text
(config)# login password-warning-interval years <number:0..99> <cr>
```

Handler ` RVA 0xCFD1FB0 `；selector ` 7 `；EOL ` RVA 0x33D74B00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of years。

[条件 C-3614a628de6ad2cd](../../evidence/conditions-sets-021.md#c-3614a628de6ad2cd) · [参数 P-e79eea789d48e0b8](../../evidence/parameters-sets-017.md#p-e79eea789d48e0b8) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-028593

```text
(config)# login quiet-mode access-class <number:1..199> <cr>
```

Handler ` RVA 0xCFD1FB0 `；selector ` 4 `；EOL ` RVA 0x33D73A78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` IP access list。

[条件 C-04c97c2d55738fa6](../../evidence/conditions-sets-002.md#c-04c97c2d55738fa6) · [参数 P-2a330a74ffafad4e](../../evidence/parameters-sets-004.md#p-2a330a74ffafad4e) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-034678

```text
(config)# login quiet-mode ipv6 access-class <string> <cr>
```

Handler ` RVA 0xCFD1FB0 `；selector ` 3 `；EOL ` RVA 0x33D73F78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Access-list name (IPv6)。

[条件 C-9b9e070fbb17f645](../../evidence/conditions-sets-060.md#c-9b9e070fbb17f645) · [参数 P-4641c0ccbbd2f6ed](../../evidence/parameters-sets-006.md#p-4641c0ccbbd2f6ed) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026716

```text
(config)# login-string <string> <string> <cr>
```

Handler ` RVA 0xCCF3F00 `；selector ` 0 `；EOL ` RVA 0x33C60728 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of the host for this login string；` string ` c login-string c, where 'c' is a delimiting character。

[条件 C-87c4f9d96291a847](../../evidence/conditions-sets-053.md#c-87c4f9d96291a847) · [参数 P-e3e718c0b0f165a0](../../evidence/parameters-sets-017.md#p-e3e718c0b0f165a0) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027143

```text
(config)# mab logging verbose <cr>
```

Handler ` RVA 0xCB56460 `；selector ` 2 `；EOL ` RVA 0x33BEA150 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e7179fdc88e9b129](../../evidence/conditions-sets-089.md#c-e7179fdc88e9b129) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-045968

```text
(config)# mab request format attribute 2 <string> <cr>
```

Handler ` RVA 0xCB56460 `；selector ` 1 `；EOL ` RVA 0x33BE96D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` The UNENCRYPTED (cleartext) password。

[条件 C-53c1f27eb0f63842](../../evidence/conditions-sets-033.md#c-53c1f27eb0f63842) · [参数 P-58195d43ad158c23](../../evidence/parameters-sets-007.md#p-58195d43ad158c23) · [状态效果 S-326cd34d28645fe9](../../evidence/state_effects-sets-011.md#s-326cd34d28645fe9)

### path-031216

```text
(config)# mac access-list extended <string> <cr>
```

Handler ` RVA 0xE98EFA0 `；selector ` 14 `；EOL ` RVA 0x34368300 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` access-list name。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-74dc5cf449687691](../../evidence/parameters-sets-009.md#p-74dc5cf449687691) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060343

```text
(config)# mac-address-table aging-time <cr>
```

Handler ` RVA 0x15E779F0 `；selector ` 6 `；EOL ` RVA 0x35E52D10 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-cc547a02e464073e](../../evidence/conditions-sets-079.md#c-cc547a02e464073e) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [状态效果 S-9969179893d99381](../../evidence/state_effects-sets-033.md#s-9969179893d99381)

### path-060334

```text
(config)# mac-address-table control-packet-learn <cr>
```

Handler ` RVA 0x15C43960 `；selector ` 0 `；EOL ` RVA 0x35E538D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-cff52fbd14af5980](../../evidence/conditions-sets-080.md#c-cff52fbd14af5980) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [状态效果 S-9969179893d99381](../../evidence/state_effects-sets-033.md#s-9969179893d99381)

### path-060349

```text
(config)# mac-address-table static <cr>
```

Handler ` RVA 0x15E779F0 `；selector ` 5 `；EOL ` RVA 0x35E52A80 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ecf0f2d20596b68d](../../evidence/conditions-sets-092.md#c-ecf0f2d20596b68d) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [状态效果 S-9969179893d99381](../../evidence/state_effects-sets-033.md#s-9969179893d99381)

### path-026553

```text
(config)# map-class frame-relay <string> <cr>
```

Handler ` RVA 0xDCFE010 `；selector ` 0 `；EOL ` RVA 0x3403ED60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Static map class name。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-3bb3acddd68f2de4](../../evidence/parameters-sets-005.md#p-3bb3acddd68f2de4) · [状态效果 S-46a73725a167eb33](../../evidence/state_effects-sets-015.md#s-46a73725a167eb33)

### path-025678

```text
(config)# map-list <string> <cr>
```

Handler ` RVA 0xDCFFA90 `；selector ` 0 `；EOL ` RVA 0x3403E3C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Static map list name。

[条件 C-c8fea8c98419b778](../../evidence/conditions-sets-077.md#c-c8fea8c98419b778) · [参数 P-ec7a1353d975e702](../../evidence/parameters-sets-018.md#p-ec7a1353d975e702) · [状态效果 S-b5fb722ed6deb24c](../../evidence/state_effects-sets-039.md#s-b5fb722ed6deb24c)

### path-027995

```text
(config)# mdns-sd controller service-list <string> <cr>
```

Handler ` RVA 0x14344A30 `；selector ` 0 `；EOL ` RVA 0x35D30518 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` mDNS controller service list name。

[条件 C-c63e00126c4233f1](../../evidence/conditions-sets-076.md#c-c63e00126c4233f1) · [参数 P-166902dbb27ebca8](../../evidence/parameters-sets-002.md#p-166902dbb27ebca8) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027978

```text
(config)# mdns-sd controller service-policy <string> <cr>
```

Handler ` RVA 0x143442D0 `；selector ` 0 `；EOL ` RVA 0x35D30218 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` mDNS controller Service Policy Name。

[条件 C-c63e00126c4233f1](../../evidence/conditions-sets-076.md#c-c63e00126c4233f1) · [参数 P-e9b518049f3b9dde](../../evidence/parameters-sets-017.md#p-e9b518049f3b9dde) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026276

```text
(config)# mdns-sd flex-profile <string> <cr>
```

Handler ` RVA 0x14355390 `；selector ` 0 `；EOL ` RVA 0x35D2EDF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` mDNS flex-profile name。

[条件 C-562f6acb75ac96b0](../../evidence/conditions-sets-034.md#c-562f6acb75ac96b0) · [参数 P-48c3fe539df6b76a](../../evidence/parameters-sets-006.md#p-48c3fe539df6b76a) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025560

```text
(config)# mdns-sd gateway <cr>
```

Handler ` RVA 0x1433EE60 `；selector ` 0 `；EOL ` RVA 0x35D307E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026290

```text
(config)# mdns-sd location-filter <string> <cr>
```

Handler ` RVA 0x14354370 `；selector ` 0 `；EOL ` RVA 0x35D2EA88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` mDNS Location Filter Name。

[条件 C-1025e153931b1477](../../evidence/conditions-sets-006.md#c-1025e153931b1477) · [参数 P-f888b9b15ecf789c](../../evidence/parameters-sets-019.md#p-f888b9b15ecf789c) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026201

```text
(config)# mdns-sd service-definition <string> <cr>
```

Handler ` RVA 0x14349070 `；selector ` 0 `；EOL ` RVA 0x35D2FB00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` mDNS Service Definition Name。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-a6bde90ad9f00065](../../evidence/parameters-sets-013.md#p-a6bde90ad9f00065) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-028007

```text
(config)# mdns-sd service-list <string> IN <cr>
```

Handler ` RVA 0x14348690 `；selector ` 0 `；EOL ` RVA 0x35D2F4E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` mDNS Service List Name。

[条件 C-0a24da6cae5a3d85](../../evidence/conditions-sets-004.md#c-0a24da6cae5a3d85) · [参数 P-31b584f08584202f](../../evidence/parameters-sets-004.md#p-31b584f08584202f) · [状态效果 S-3f2be1a55f07a79e](../../evidence/state_effects-sets-014.md#s-3f2be1a55f07a79e)

### path-028034

```text
(config)# mdns-sd service-list <string> OUT <cr>
```

Handler ` RVA 0x14348CB0 `；selector ` 0 `；EOL ` RVA 0x35D2F7A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` mDNS Service List Name。

[条件 C-e6c11f5b6fe10d6b](../../evidence/conditions-sets-089.md#c-e6c11f5b6fe10d6b) · [参数 P-31b584f08584202f](../../evidence/parameters-sets-004.md#p-31b584f08584202f) · [状态效果 S-b605fa8bed838e63](../../evidence/state_effects-sets-039.md#s-b605fa8bed838e63)

### path-026266

```text
(config)# mdns-sd service-peer group <cr>
```

Handler ` RVA 0x1434D6A0 `；selector ` 0 `；EOL ` RVA 0x35D2F170 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e84e6cabd89f3fe5](../../evidence/conditions-sets-090.md#c-e84e6cabd89f3fe5) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026190

```text
(config)# mdns-sd service-policy <string> <cr>
```

Handler ` RVA 0x14343EF0 `；selector ` 0 `；EOL ` RVA 0x35D2FE38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` mDNS Service Policy Name。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-b571279b6a24b11f](../../evidence/parameters-sets-014.md#p-b571279b6a24b11f) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026307

```text
(config)# mdns-sd wired-filter <string> <cr>
```

Handler ` RVA 0x14356090 `；selector ` 0 `；EOL ` RVA 0x35D2E710 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` mDNS Wired Filter Name。

[条件 C-51c7949fb1df1713](../../evidence/conditions-sets-032.md#c-51c7949fb1df1713) · [参数 P-d304e93fddeb9ce8](../../evidence/parameters-sets-016.md#p-d304e93fddeb9ce8) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025486

```text
(config)# memory check-interval <number:1..2147483> <cr>
```

Handler ` RVA 0xE041A50 `；selector ` 0 `；EOL ` RVA 0x341EBDC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6b4cc27cd9852c57](../../evidence/conditions-sets-041.md#c-6b4cc27cd9852c57) · [参数 P-dbe3278e5ed0f937](../../evidence/parameters-sets-017.md#p-dbe3278e5ed0f937) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-038481

```text
(config)# memory chunk siblings threshold <number:2..4294967295> <cr>
```

Handler ` RVA 0xE0424E0 `；selector ` 0 `；EOL ` RVA 0x341ED728 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Default is platform dependent。

[条件 C-0c006ec7aae0194b](../../evidence/conditions-sets-005.md#c-0c006ec7aae0194b) · [参数 P-10c5230f2e431a73](../../evidence/parameters-sets-002.md#p-10c5230f2e431a73) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-038523

```text
(config)# memory free low-watermark processor <number:1..3994575> <cr>
```

Handler ` RVA 0xE042600 `；selector ` 0 `；EOL ` RVA 0x341EDB20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` low water mark of memory in KB。

[条件 C-70939e9ae4efd308](../../evidence/conditions-sets-044.md#c-70939e9ae4efd308) · [参数 P-ed692162f01fc6f1](../../evidence/parameters-sets-018.md#p-ed692162f01fc6f1) · [状态效果 S-f0b59fbd4c233d08](../../evidence/state_effects-sets-051.md#s-f0b59fbd4c233d08)

### path-027531

```text
(config)# memory free-list <number:1..4294967280> <cr>
```

Handler ` RVA 0xE03AC90 `；selector ` 0 `；EOL ` RVA 0x341EBE48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-90de72389bb3e3e4](../../evidence/parameters-sets-011.md#p-90de72389bb3e3e4) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025979

```text
(config)# memory lite <cr>
```

Handler ` RVA 0xE042100 `；selector ` 0 `；EOL ` RVA 0x341EDE70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-39c105959c6a3f82](../../evidence/conditions-sets-022.md#c-39c105959c6a3f82) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027548

```text
(config)# memory record events <cr>
```

Handler ` RVA 0xE091570 `；selector ` 0 `；EOL ` RVA 0x341EBAC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-975944c4b4477f65](../../evidence/conditions-sets-058.md#c-975944c4b4477f65) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060955

```text
(config)# memory record filter PC <?general_pointer_number_action@55558973f1b0> <cr>
```

Handler ` RVA 0xE0907E0 `；selector ` 5 `；EOL ` RVA 0x341EB1F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-975944c4b4477f65](../../evidence/conditions-sets-058.md#c-975944c4b4477f65) · [缺口 G-ba1a663f0a2ef741](../../evidence/gaps-sets-007.md#g-ba1a663f0a2ef741) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-038050

```text
(config)# memory record filter include <string> <cr>
```

Handler ` RVA 0xE0907E0 `；selector ` 4 `；EOL ` RVA 0x341EAE90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` the string to match。

[条件 C-975944c4b4477f65](../../evidence/conditions-sets-058.md#c-975944c4b4477f65) · [参数 P-6942ad18b4e8030e](../../evidence/parameters-sets-008.md#p-6942ad18b4e8030e) · [状态效果 S-4853563a436f3d95](../../evidence/state_effects-sets-016.md#s-4853563a436f3d95)

### path-027544

```text
(config)# memory record traceback <cr>
```

Handler ` RVA 0xE090220 `；selector ` 0 `；EOL ` RVA 0x341EB578 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e86e6181a0af5d5c](../../evidence/conditions-sets-090.md#c-e86e6181a0af5d5c) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027568

```text
(config)# memory reserve critical <cr>
```

Handler ` RVA 0xE042E20 `；selector ` 0 `；EOL ` RVA 0x341ECF50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ef421147a854d09d](../../evidence/conditions-sets-092.md#c-ef421147a854d09d) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-031265

```text
(config)# memory reserved console <number:0..4096> <cr>
```

Handler ` RVA 0xE0434F0 `；selector ` 0 `；EOL ` RVA 0x341ED2B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Size in Kilo Bytes。

[条件 C-a70b1cc6ea92278e](../../evidence/conditions-sets-064.md#c-a70b1cc6ea92278e) · [参数 P-d84bb396bcb7c3eb](../../evidence/parameters-sets-016.md#p-d84bb396bcb7c3eb) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025984

```text
(config)# memory sanity <cr>
```

Handler ` RVA 0xE043350 `；selector ` 0 `；EOL ` RVA 0x341ECAC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d458568b6c8d2f1f](../../evidence/conditions-sets-082.md#c-d458568b6c8d2f1f) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-038201

```text
(config)# memory statistics history table <number:12..72> <cr>
```

Handler ` RVA 0xE092FD0 `；selector ` 0 `；EOL ` RVA 0x341EC400 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of hours of history。

[条件 C-2421e5e28d1c5d92](../../evidence/conditions-sets-014.md#c-2421e5e28d1c5d92) · [参数 P-31d3d951cc5d2255](../../evidence/parameters-sets-004.md#p-31d3d951cc5d2255) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025487

```text
(config)# memory validate-checksum <number:1..2147483> <cr>
```

Handler ` RVA 0xE041D20 `；selector ` 0 `；EOL ` RVA 0x341EC398 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7479145b2eacd8d0](../../evidence/conditions-sets-045.md#c-7479145b2eacd8d0) · [参数 P-f5658744ebca814e](../../evidence/parameters-sets-018.md#p-f5658744ebca814e) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060467

```text
(config)# mgmt-traffic control ipv4 <cr>
```

Handler ` RVA 0xFA031E0 `；selector ` 0 `；EOL ` RVA 0x347BB3D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c6575ca60da74792](../../evidence/conditions-sets-076.md#c-c6575ca60da74792) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [状态效果 S-9969179893d99381](../../evidence/state_effects-sets-033.md#s-9969179893d99381)

### path-025580

```text
(config)# microcode reload <cr>
```

Handler ` RVA 0x162D0C70 `；selector ` 0 `；EOL ` RVA 0x35F6ECB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-031448

```text
(config)# mka defaults policy send-secure-announcements <cr>
```

Handler ` RVA 0x16073550 `；selector ` 2 `；EOL ` RVA 0x35EBB888 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e873fc0f94792499](../../evidence/conditions-sets-090.md#c-e873fc0f94792499) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027593

```text
(config)# mka policy <string> <cr>
```

Handler ` RVA 0x16073550 `；selector ` 1 `；EOL ` RVA 0x35EBBBB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` MKA Policy NAME。

[条件 C-06ac504ca4ce4f5f](../../evidence/conditions-sets-003.md#c-06ac504ca4ce4f5f) · [参数 P-ff16decb88ad8255](../../evidence/parameters-sets-019.md#p-ff16decb88ad8255) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-031462

```text
(config)# mka suppress syslogs sak-rekey <cr>
```

Handler ` RVA 0x16073550 `；selector ` 3 `；EOL ` RVA 0x35EBBF30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4c0694c80e89bc38](../../evidence/conditions-sets-030.md#c-4c0694c80e89bc38) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-037268

```text
(config)# modemcap edit <string> miscellaneous <string> <cr>
```

Handler ` RVA 0xFDCD180 `；selector ` 2 `；EOL ` RVA 0x348DC5F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Modem type；` string ` Modem string for this attribute。

[条件 C-7715642abf2c035a](../../evidence/conditions-sets-046.md#c-7715642abf2c035a) · [参数 P-803f5780b5b0bcf8](../../evidence/parameters-sets-010.md#p-803f5780b5b0bcf8) · [状态效果 S-f0116ce85abf6a8b](../../evidence/state_effects-sets-051.md#s-f0116ce85abf6a8b)

### path-027381

```text
(config)# modemcap entry <string> <cr>
```

Handler ` RVA 0xFDCD180 `；selector ` 1 `；EOL ` RVA 0x348DC218 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Modemcap entry for this modem。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-6713ef24070d622c](../../evidence/parameters-sets-008.md#p-6713ef24070d622c) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060663

```text
(config)# monitor drop log urpf <cr>
```

Handler ` RVA 0xE988280 `；selector ` 0 `；EOL ` RVA 0x34362000 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e0f7aed16e3cf91d](../../evidence/conditions-sets-087.md#c-e0f7aed16e3cf91d) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [状态效果 S-1c3e8cc48916f265](../../evidence/state_effects-sets-006.md#s-1c3e8cc48916f265)

### path-060916

```text
(config)# monitor drop match ip <string> <cr>
```

Handler ` RVA 0xE9877D0 `；selector ` 0 `；EOL ` RVA 0x34361C30 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` ACL name。

[条件 C-e0f7aed16e3cf91d](../../evidence/conditions-sets-087.md#c-e0f7aed16e3cf91d) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [参数 P-aa66c5c1f951c917](../../evidence/parameters-sets-013.md#p-aa66c5c1f951c917) · [状态效果 S-6f7e6d9adf306738](../../evidence/state_effects-sets-024.md#s-6f7e6d9adf306738)

### path-061007

```text
(config)# monitor event-trace eigrp perf-events rate-limiting <cr>
```

Handler ` RVA 0xF50F630 `；selector ` 1 `；EOL ` RVA 0x34683E58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f3ddd6990d3d735a](../../evidence/conditions-sets-094.md#c-f3ddd6990d3d735a) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [状态效果 S-309f07e539aaa44c](../../evidence/state_effects-sets-011.md#s-309f07e539aaa44c)

### path-060439

```text
(config)# monitor event-trace stacktrace <cr>
```

Handler ` RVA 0xD2D1180 `；selector ` 0 `；EOL ` RVA 0x33DF9678 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9fef9d3e79cb30b0](../../evidence/conditions-sets-062.md#c-9fef9d3e79cb30b0) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [状态效果 S-2d08e8de1e10310f](../../evidence/state_effects-sets-010.md#s-2d08e8de1e10310f)

### path-062942

```text
(config)# monitor pcm-tracer <cr>
```

Handler ` RVA 0x1629F110 `；selector ` 1 `；EOL ` RVA 0x35F68DD0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3ca0f8b50d02e911](../../evidence/conditions-sets-024.md#c-3ca0f8b50d02e911) · [缺口 G-fab198ec39413a46](../../evidence/gaps-sets-009.md#g-fab198ec39413a46) · [状态效果 S-ab26201b033b83e7](../../evidence/state_effects-sets-036.md#s-ab26201b033b83e7)

### path-063028

```text
(config)# monitor pcm-tracer capture-destination <cr>
```

Handler ` RVA 0x1629F110 `；selector ` 5 `；EOL ` RVA 0x35F697E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-237118618464d54e](../../evidence/conditions-sets-014.md#c-237118618464d54e) · [缺口 G-eef635d1c4fa745d](../../evidence/gaps-sets-008.md#g-eef635d1c4fa745d) · [状态效果 S-1f3c54e8d0fbf010](../../evidence/state_effects-sets-007.md#s-1f3c54e8d0fbf010)

### path-063027

```text
(config)# monitor pcm-tracer capture-duration <cr>
```

Handler ` RVA 0x1629F110 `；selector ` 6 `；EOL ` RVA 0x35F69490 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7b7dc363cd0582da](../../evidence/conditions-sets-048.md#c-7b7dc363cd0582da) · [缺口 G-eef635d1c4fa745d](../../evidence/gaps-sets-008.md#g-eef635d1c4fa745d) · [状态效果 S-1f3c54e8d0fbf010](../../evidence/state_effects-sets-007.md#s-1f3c54e8d0fbf010)

### path-063029

```text
(config)# monitor pcm-tracer delayed-start <cr>
```

Handler ` RVA 0x1629F110 `；selector ` 4 `；EOL ` RVA 0x35F69B00 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-04b417206f93ee4b](../../evidence/conditions-sets-002.md#c-04b417206f93ee4b) · [缺口 G-eef635d1c4fa745d](../../evidence/gaps-sets-008.md#g-eef635d1c4fa745d) · [状态效果 S-1f3c54e8d0fbf010](../../evidence/state_effects-sets-007.md#s-1f3c54e8d0fbf010)

### path-063038

```text
(config)# monitor pcm-tracer profile <number:1..10> <cr>
```

Handler ` RVA 0x1629F110 `；selector ` 7 `；EOL ` RVA 0x35F69198 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Profile number。

[条件 C-0483fbffcd7abc19](../../evidence/conditions-sets-002.md#c-0483fbffcd7abc19) · [缺口 G-eef635d1c4fa745d](../../evidence/gaps-sets-008.md#g-eef635d1c4fa745d) · [参数 P-3980607331e9c01e](../../evidence/parameters-sets-005.md#p-3980607331e9c01e) · [状态效果 S-1f3c54e8d0fbf010](../../evidence/state_effects-sets-007.md#s-1f3c54e8d0fbf010)

### path-060328

```text
(config)# monitor permit-list <cr>
```

Handler ` RVA 0xE4DDDD0 `；selector ` 13 `；EOL ` RVA 0x342DD300 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1e225eb5d16eca7a](../../evidence/conditions-sets-012.md#c-1e225eb5d16eca7a) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [状态效果 S-9969179893d99381](../../evidence/state_effects-sets-033.md#s-9969179893d99381)

### path-063106

```text
(config)# monitor permit-list destination interface <interface> <cr>
```

Handler ` RVA 0xE4DDDD0 `；selector ` 14 `；EOL ` RVA 0x342DD7E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-499e33168b05a022](../../evidence/conditions-sets-029.md#c-499e33168b05a022) · [缺口 G-23cd4907a157d792](../../evidence/gaps-sets-002.md#g-23cd4907a157d792) · [参数 P-9b2594f665c140ff](../../evidence/parameters-sets-012.md#p-9b2594f665c140ff) · [状态效果 S-0cc52e6bf3817bbd](../../evidence/state_effects-sets-003.md#s-0cc52e6bf3817bbd)

### path-062726

```text
(config)# monitor session <number:dynamic> <cr>
```

Handler ` RVA 0xE4C4370 `；selector ` 2 `；EOL ` RVA 0x342D3390 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` SPAN session number。

[条件 C-6c078b5e0f0aaafd](../../evidence/conditions-sets-042.md#c-6c078b5e0f0aaafd) · [缺口 G-b479dd78897ef8c3](../../evidence/gaps-sets-006.md#g-b479dd78897ef8c3) · [参数 P-6d4a70f1949e8426](../../evidence/parameters-sets-009.md#p-6d4a70f1949e8426) · [状态效果 S-9969179893d99381](../../evidence/state_effects-sets-033.md#s-9969179893d99381)

### path-062727

```text
(config)# monitor session <number:dynamic> <cr>
```

Handler ` RVA 0xE4C4370 `；selector ` 2 `；EOL ` RVA 0x342E0218 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` SPAN session number。

[条件 C-b14948f21fcaac2f](../../evidence/conditions-sets-069.md#c-b14948f21fcaac2f) · [缺口 G-b479dd78897ef8c3](../../evidence/gaps-sets-006.md#g-b479dd78897ef8c3) · [参数 P-6d4a70f1949e8426](../../evidence/parameters-sets-009.md#p-6d4a70f1949e8426) · [状态效果 S-9969179893d99381](../../evidence/state_effects-sets-033.md#s-9969179893d99381)

### path-062757

```text
(config)# monitor session <number:dynamic> filter <cr>
```

Handler ` RVA 0xE4C4370 `；selector ` 9 `；EOL ` RVA 0x342D54B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` SPAN session number。

[条件 C-5be912505ae5d084](../../evidence/conditions-sets-036.md#c-5be912505ae5d084) · [缺口 G-b479dd78897ef8c3](../../evidence/gaps-sets-006.md#g-b479dd78897ef8c3) · [参数 P-6d4a70f1949e8426](../../evidence/parameters-sets-009.md#p-6d4a70f1949e8426) · [状态效果 S-2cab447ea972cab1](../../evidence/state_effects-sets-010.md#s-2cab447ea972cab1)

### path-062805

```text
(config)# monitor session <number:dynamic> filter address-type <cr>
```

Handler ` RVA 0xE4C4370 `；selector ` 12 `；EOL ` RVA 0x342D4518 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` SPAN session number。

[条件 C-15f6365bf637a594](../../evidence/conditions-sets-009.md#c-15f6365bf637a594) · [缺口 G-b479dd78897ef8c3](../../evidence/gaps-sets-006.md#g-b479dd78897ef8c3) · [参数 P-6d4a70f1949e8426](../../evidence/parameters-sets-009.md#p-6d4a70f1949e8426) · [状态效果 S-5e6c41b4f7ea6e98](../../evidence/state_effects-sets-020.md#s-5e6c41b4f7ea6e98)

### path-062843

```text
(config)# monitor session <number:dynamic> filter ip access-group <cr>
```

Handler ` RVA 0xE4C4370 `；selector ` 16 `；EOL ` RVA 0x342D4A30 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` SPAN session number。

[条件 C-5d897850eeb2328c](../../evidence/conditions-sets-036.md#c-5d897850eeb2328c) · [缺口 G-b479dd78897ef8c3](../../evidence/gaps-sets-006.md#g-b479dd78897ef8c3) · [参数 P-6d4a70f1949e8426](../../evidence/parameters-sets-009.md#p-6d4a70f1949e8426) · [状态效果 S-3fcab1919fd26b40](../../evidence/state_effects-sets-014.md#s-3fcab1919fd26b40)

### path-062841

```text
(config)# monitor session <number:dynamic> filter ipv6 access-group <cr>
```

Handler ` RVA 0xE4C4370 `；selector ` 18 `；EOL ` RVA 0x342D51F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` SPAN session number。

[条件 C-87c8b1ba45374b83](../../evidence/conditions-sets-053.md#c-87c8b1ba45374b83) · [缺口 G-b479dd78897ef8c3](../../evidence/gaps-sets-006.md#g-b479dd78897ef8c3) · [参数 P-6d4a70f1949e8426](../../evidence/parameters-sets-009.md#p-6d4a70f1949e8426) · [状态效果 S-155a3c913f6fa479](../../evidence/state_effects-sets-005.md#s-155a3c913f6fa479)

### path-062839

```text
(config)# monitor session <number:dynamic> filter mac access-group <cr>
```

Handler ` RVA 0xE4C4370 `；selector ` 17 `；EOL ` RVA 0x342D4E00 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` SPAN session number。

[条件 C-ad0ae4ff22447e0e](../../evidence/conditions-sets-067.md#c-ad0ae4ff22447e0e) · [缺口 G-b479dd78897ef8c3](../../evidence/gaps-sets-006.md#g-b479dd78897ef8c3) · [参数 P-6d4a70f1949e8426](../../evidence/parameters-sets-009.md#p-6d4a70f1949e8426) · [状态效果 S-8d0313f022540acb](../../evidence/state_effects-sets-030.md#s-8d0313f022540acb)

### path-062802

```text
(config)# monitor session <number:dynamic> filter packet-type <cr>
```

Handler ` RVA 0xE4C4370 `；selector ` 11 `；EOL ` RVA 0x342D4000 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` SPAN session number。

[条件 C-9fead746cb92e545](../../evidence/conditions-sets-062.md#c-9fead746cb92e545) · [缺口 G-b479dd78897ef8c3](../../evidence/gaps-sets-006.md#g-b479dd78897ef8c3) · [参数 P-6d4a70f1949e8426](../../evidence/parameters-sets-009.md#p-6d4a70f1949e8426) · [状态效果 S-a691dbb06139d9da](../../evidence/state_effects-sets-035.md#s-a691dbb06139d9da)

### path-062840

```text
(config)# monitor session <number:dynamic> filter packet-type good <cr>
```

Handler ` RVA 0xE4C4370 `；selector ` 0 `；EOL ` RVA 0x342D01F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` SPAN session number。

[条件 C-491d858c8386fab4](../../evidence/conditions-sets-029.md#c-491d858c8386fab4) · [缺口 G-b479dd78897ef8c3](../../evidence/gaps-sets-006.md#g-b479dd78897ef8c3) · [参数 P-6d4a70f1949e8426](../../evidence/parameters-sets-009.md#p-6d4a70f1949e8426) · [状态效果 S-416c25e072e178d8](../../evidence/state_effects-sets-014.md#s-416c25e072e178d8)

### path-062952

```text
(config)# monitor session <number:dynamic> filter vlan <cr>
```

Handler ` RVA 0xE4C4370 `；selector ` 10 `；EOL ` RVA 0x342D3B90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` SPAN session number。

[条件 C-87022a3b87eaabc8](../../evidence/conditions-sets-052.md#c-87022a3b87eaabc8) · [缺口 G-3675c379519c29d0](../../evidence/gaps-sets-002.md#g-3675c379519c29d0) · [参数 P-6d4a70f1949e8426](../../evidence/parameters-sets-009.md#p-6d4a70f1949e8426) · [状态效果 S-ffb58b49c465f12a](../../evidence/state_effects-sets-054.md#s-ffb58b49c465f12a)

### path-062806

```text
(config)# monitor session <number:dynamic> type capture <cr>
```

Handler ` RVA 0xE4F1800 `；selector ` 0 `；EOL ` RVA 0x342DFF30 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` SPAN session number。

[条件 C-b22a13b037a3c386](../../evidence/conditions-sets-069.md#c-b22a13b037a3c386) · [缺口 G-b479dd78897ef8c3](../../evidence/gaps-sets-006.md#g-b479dd78897ef8c3) · [参数 P-6d4a70f1949e8426](../../evidence/parameters-sets-009.md#p-6d4a70f1949e8426) · [状态效果 S-b9242c59e7ebbdc4](../../evidence/state_effects-sets-039.md#s-b9242c59e7ebbdc4)

### path-062798

```text
(config)# monitor session <number:dynamic> type erspan-destination <cr>
```

Handler ` RVA 0xE4F1B30 `；selector ` 0 `；EOL ` RVA 0x342DF010 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` SPAN session number。

[条件 C-980188aa126664b7](../../evidence/conditions-sets-059.md#c-980188aa126664b7) · [缺口 G-b479dd78897ef8c3](../../evidence/gaps-sets-006.md#g-b479dd78897ef8c3) · [参数 P-6d4a70f1949e8426](../../evidence/parameters-sets-009.md#p-6d4a70f1949e8426) · [状态效果 S-7719a83f4056adff](../../evidence/state_effects-sets-025.md#s-7719a83f4056adff)

### path-062796

```text
(config)# monitor session <number:dynamic> type erspan-source <cr>
```

Handler ` RVA 0xE4F1860 `；selector ` 0 `；EOL ` RVA 0x342DED18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` SPAN session number。

[条件 C-7e9c1be77bbc4a16](../../evidence/conditions-sets-049.md#c-7e9c1be77bbc4a16) · [缺口 G-b479dd78897ef8c3](../../evidence/gaps-sets-006.md#g-b479dd78897ef8c3) · [参数 P-6d4a70f1949e8426](../../evidence/parameters-sets-009.md#p-6d4a70f1949e8426) · [状态效果 S-760503e2f5e427bd](../../evidence/state_effects-sets-025.md#s-760503e2f5e427bd)

### path-062803

```text
(config)# monitor session <number:dynamic> type local <cr>
```

Handler ` RVA 0xE4F2310 `；selector ` 0 `；EOL ` RVA 0x342DF938 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` SPAN session number。

[条件 C-0f432874ed80c5a1](../../evidence/conditions-sets-006.md#c-0f432874ed80c5a1) · [缺口 G-b479dd78897ef8c3](../../evidence/gaps-sets-006.md#g-b479dd78897ef8c3) · [参数 P-6d4a70f1949e8426](../../evidence/parameters-sets-009.md#p-6d4a70f1949e8426) · [状态效果 S-d7d3dba826e787c4](../../evidence/state_effects-sets-046.md#s-d7d3dba826e787c4)

### path-062804

```text
(config)# monitor session <number:dynamic> type local-tx <cr>
```

Handler ` RVA 0xE4F25A0 `；selector ` 0 `；EOL ` RVA 0x342DFC30 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` SPAN session number。

[条件 C-a951d16706e2dbf7](../../evidence/conditions-sets-065.md#c-a951d16706e2dbf7) · [缺口 G-b479dd78897ef8c3](../../evidence/gaps-sets-006.md#g-b479dd78897ef8c3) · [参数 P-6d4a70f1949e8426](../../evidence/parameters-sets-009.md#p-6d4a70f1949e8426) · [状态效果 S-35004b7cd569b8fb](../../evidence/state_effects-sets-012.md#s-35004b7cd569b8fb)

### path-062800

```text
(config)# monitor session <number:dynamic> type rspan-destination <cr>
```

Handler ` RVA 0xE4F2080 `；selector ` 0 `；EOL ` RVA 0x342DF640 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` SPAN session number。

[条件 C-fb47ee96965c84eb](../../evidence/conditions-sets-097.md#c-fb47ee96965c84eb) · [缺口 G-b479dd78897ef8c3](../../evidence/gaps-sets-006.md#g-b479dd78897ef8c3) · [参数 P-6d4a70f1949e8426](../../evidence/parameters-sets-009.md#p-6d4a70f1949e8426) · [状态效果 S-f2c0d76d7dbcb285](../../evidence/state_effects-sets-051.md#s-f2c0d76d7dbcb285)

### path-062799

```text
(config)# monitor session <number:dynamic> type rspan-source <cr>
```

Handler ` RVA 0xE4F1E00 `；selector ` 0 `；EOL ` RVA 0x342DF348 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` SPAN session number。

[条件 C-699ca5033b4b436a](../../evidence/conditions-sets-041.md#c-699ca5033b4b436a) · [缺口 G-b479dd78897ef8c3](../../evidence/gaps-sets-006.md#g-b479dd78897ef8c3) · [参数 P-6d4a70f1949e8426](../../evidence/parameters-sets-009.md#p-6d4a70f1949e8426) · [状态效果 S-e0ac6e433e21cf63](../../evidence/state_effects-sets-048.md#s-e0ac6e433e21cf63)

### path-060451

```text
(config)# monitor session all <cr>
```

Handler ` RVA 0xE4C4370 `；selector ` 1 `；EOL ` RVA 0x342D58A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2148656ad811337a](../../evidence/conditions-sets-013.md#c-2148656ad811337a) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [状态效果 S-9969179893d99381](../../evidence/state_effects-sets-033.md#s-9969179893d99381)

### path-060458

```text
(config)# monitor session capture <cr>
```

Handler ` RVA 0xE4C4370 `；selector ` 7 `；EOL ` RVA 0x342D66B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3b55fd3bbd112a3d](../../evidence/conditions-sets-023.md#c-3b55fd3bbd112a3d) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [状态效果 S-9969179893d99381](../../evidence/state_effects-sets-033.md#s-9969179893d99381)

### path-060462

```text
(config)# monitor session erspan-destination <cr>
```

Handler ` RVA 0xE4C4370 `；selector ` 6 `；EOL ` RVA 0x342D63C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-015f24aaea48c6d6](../../evidence/conditions-sets-001.md#c-015f24aaea48c6d6) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [状态效果 S-9969179893d99381](../../evidence/state_effects-sets-033.md#s-9969179893d99381)

### path-060459

```text
(config)# monitor session erspan-source <cr>
```

Handler ` RVA 0xE4C4370 `；selector ` 5 `；EOL ` RVA 0x342D6120 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-015f24aaea48c6d6](../../evidence/conditions-sets-001.md#c-015f24aaea48c6d6) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [状态效果 S-9969179893d99381](../../evidence/state_effects-sets-033.md#s-9969179893d99381)

### path-060452

```text
(config)# monitor session local <cr>
```

Handler ` RVA 0xE4C4370 `；selector ` 3 `；EOL ` RVA 0x342D5B50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2148656ad811337a](../../evidence/conditions-sets-013.md#c-2148656ad811337a) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [状态效果 S-9969179893d99381](../../evidence/state_effects-sets-033.md#s-9969179893d99381)

### path-062756

```text
(config)# monitor session range <?string_help_func_action@55558982a958> <cr>
```

Handler ` RVA 0xE4C4370 `；selector ` 8 `；EOL ` RVA 0x342D6998 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6dd8ca6b19cb7259](../../evidence/conditions-sets-042.md#c-6dd8ca6b19cb7259) · [缺口 G-69be066196e720e7](../../evidence/gaps-sets-004.md#g-69be066196e720e7) · [状态效果 S-9969179893d99381](../../evidence/state_effects-sets-033.md#s-9969179893d99381)

### path-060456

```text
(config)# monitor session remote <cr>
```

Handler ` RVA 0xE4C4370 `；selector ` 4 `；EOL ` RVA 0x342D5E38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6b83867e9c3feffa](../../evidence/conditions-sets-042.md#c-6b83867e9c3feffa) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [状态效果 S-9969179893d99381](../../evidence/state_effects-sets-033.md#s-9969179893d99381)

### path-060426

```text
(config)# monitor ssm id <cr>
```

Handler ` RVA 0x104323E0 `；selector ` 0 `；EOL ` RVA 0x34B28130 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-00f411b0164df3a1](../../evidence/conditions-sets-001.md#c-00f411b0164df3a1) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [状态效果 S-9969179893d99381](../../evidence/state_effects-sets-033.md#s-9969179893d99381)

### path-027253

```text
(config)# multilink bundle-name authenticated <cr>
```

Handler ` RVA 0xFF5A340 `；selector ` 3 `；EOL ` RVA 0x34938348 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6026176d30fc9d2a](../../evidence/conditions-sets-037.md#c-6026176d30fc9d2a) · [状态效果 S-cbf824c60d0bcdad](../../evidence/state_effects-sets-043.md#s-cbf824c60d0bcdad)

### path-025467

```text
(config)# multilink test-mode <number:0..1> <cr>
```

Handler ` RVA 0xFF5A340 `；selector ` 2 `；EOL ` RVA 0x34937CE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8ca4c75058287523](../../evidence/conditions-sets-054.md#c-8ca4c75058287523) · [参数 P-cbb9e2dc901badfe](../../evidence/parameters-sets-015.md#p-cbb9e2dc901badfe) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060415

```text
(config)# multilink virtual-template <number:dynamic> <cr>
```

Handler ` RVA 0xFF5A340 `；selector ` 1 `；EOL ` RVA 0x34937D80 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` virtual template number。

[条件 C-21197ae8d0516b2d](../../evidence/conditions-sets-013.md#c-21197ae8d0516b2d) · [缺口 G-bad0e962afbec3e6](../../evidence/gaps-sets-007.md#g-bad0e962afbec3e6) · [参数 P-bb1f02d01483ce27](../../evidence/parameters-sets-014.md#p-bb1f02d01483ce27) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025462

```text
(config)# mvr <cr>
```

Handler ` RVA 0xC3B62A0 `；selector ` 1 `；EOL ` RVA 0x33A61628 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060616

```text
(config)# mvr group <address> <number:dynamic> <cr>
```

Handler ` RVA 0xC3B62A0 `；selector ` 2 `；EOL ` RVA 0x33A612F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` IP multicast address；` unsigned_number_dynamic ` Count of contiguous groups。

[条件 C-0ba1541ae7c067fe](../../evidence/conditions-sets-005.md#c-0ba1541ae7c067fe) · [缺口 G-51af0538493bd365](../../evidence/gaps-sets-003.md#g-51af0538493bd365) · [参数 P-e2416ac122d0cb0a](../../evidence/parameters-sets-017.md#p-e2416ac122d0cb0a) · [状态效果 S-4edfe8adc0c2c401](../../evidence/state_effects-sets-017.md#s-4edfe8adc0c2c401)

### path-060405

```text
(config)# mvr max-groups <number:dynamic> <cr>
```

Handler ` RVA 0xC3B62A0 `；selector ` 7 `；EOL ` RVA 0x33A60828 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Maximum number of MVR groups。

[条件 C-e6c475f351e5acc1](../../evidence/conditions-sets-089.md#c-e6c475f351e5acc1) · [缺口 G-a33ba41860df1caf](../../evidence/gaps-sets-006.md#g-a33ba41860df1caf) · [参数 P-4a23635018037746](../../evidence/parameters-sets-006.md#p-4a23635018037746) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025835

```text
(config)# mvr mode <cr>
```

Handler ` RVA 0xC3B62A0 `；selector ` 4 `；EOL ` RVA 0x33A60EB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-8fcf8ce009774c8e](../../evidence/state_effects-sets-031.md#s-8fcf8ce009774c8e)

### path-027060

```text
(config)# mvr querytime <number:1..100> <cr>
```

Handler ` RVA 0xC3B62A0 `；selector ` 6 `；EOL ` RVA 0x33A60B78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` time value in units of 1/10 seconds。

[条件 C-2a3da7750ed4bf3c](../../evidence/conditions-sets-017.md#c-2a3da7750ed4bf3c) · [参数 P-8402827dc7343529](../../evidence/parameters-sets-010.md#p-8402827dc7343529) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060403

```text
(config)# mvr vlan <number:dynamic> <cr>
```

Handler ` RVA 0xC3B62A0 `；selector ` 5 `；EOL ` RVA 0x33A604D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` MVR Multicast VLAN id。

[条件 C-31aede877ec86f4d](../../evidence/conditions-sets-019.md#c-31aede877ec86f4d) · [缺口 G-f2a821bce4d1dc6d](../../evidence/gaps-sets-008.md#g-f2a821bce4d1dc6d) · [参数 P-f53e5cab01011c53](../../evidence/parameters-sets-018.md#p-f53e5cab01011c53) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025756

```text
(config)# named-ordering-route-map enable <cr>
```

Handler ` RVA 0xE2387D0 `；selector ` 0 `；EOL ` RVA 0x3423E420 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1bafa46bc6d9f23a](../../evidence/conditions-sets-011.md#c-1bafa46bc6d9f23a) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-062725

```text
(config)# nat46 prefix <prefix:dynamic> <cr>
```

Handler ` RVA 0xD5D31F0 `；selector ` 13 `；EOL ` RVA 0x33EA9AC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` IPv6 prefix/length。

[条件 C-5d5cae8f105584a8](../../evidence/conditions-sets-036.md#c-5d5cae8f105584a8) · [缺口 G-cd463a2852d928ca](../../evidence/gaps-sets-007.md#g-cd463a2852d928ca) · [参数 P-45d2ecc1393e7bdb](../../evidence/parameters-sets-006.md#p-45d2ecc1393e7bdb) · [状态效果 S-640abb9350ccb1da](../../evidence/state_effects-sets-021.md#s-640abb9350ccb1da)

### path-060667

```text
(config)# nat46 v4 pool <string> <cr>
```

Handler ` RVA 0xD5D31F0 `；selector ` 11 `；EOL ` RVA 0x33EA9740 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` NAT46 pool name。

[条件 C-10cac2cb5058b124](../../evidence/conditions-sets-007.md#c-10cac2cb5058b124) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [参数 P-6deaa20b2dbe1b17](../../evidence/parameters-sets-009.md#p-6deaa20b2dbe1b17) · [状态效果 S-5671b61aa06cbb7f](../../evidence/state_effects-sets-019.md#s-5671b61aa06cbb7f)

### path-060670

```text
(config)# nat46 v6v4 pool <string> <cr>
```

Handler ` RVA 0xD5D31F0 `；selector ` 12 `；EOL ` RVA 0x33EA9FC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` NAT46 pool name。

[条件 C-97d4955a91020557](../../evidence/conditions-sets-059.md#c-97d4955a91020557) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [参数 P-1a9e367e3bfcaa69](../../evidence/parameters-sets-003.md#p-1a9e367e3bfcaa69) · [状态效果 S-2566a9275a0def31](../../evidence/state_effects-sets-008.md#s-2566a9275a0def31)

### path-062524

```text
(config)# nat64 logging translations flow-export v9 udp destination <address> <number:1..65535> <cr>
```

Handler ` RVA 0xD595760 `；selector ` 2 `；EOL ` RVA 0x33E94F80 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` IPv4 address；` unsigned_number ` Port number。

[条件 C-711bf3c422429418](../../evidence/conditions-sets-044.md#c-711bf3c422429418) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [参数 P-0f77e047396c5aff](../../evidence/parameters-sets-002.md#p-0f77e047396c5aff) · [状态效果 S-cf0291419d9bd401](../../evidence/state_effects-sets-044.md#s-cf0291419d9bd401)

### path-060678

```text
(config)# nat64 map-t domain <number:1..10000> <cr>
```

Handler ` RVA 0xD595760 `；selector ` 10 `；EOL ` RVA 0x33E99500 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` NAT64 MAP-T domain number。

[条件 C-c72415a95050d922](../../evidence/conditions-sets-077.md#c-c72415a95050d922) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [参数 P-3017bb39e6ddc006](../../evidence/parameters-sets-004.md#p-3017bb39e6ddc006) · [状态效果 S-9ae7b0dbe15793c5](../../evidence/state_effects-sets-033.md#s-9ae7b0dbe15793c5)

### path-060447

```text
(config)# nat64 prefix stateful <cr>
```

Handler ` RVA 0xD595760 `；selector ` 0 `；EOL ` RVA 0x33E946A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-54f40209db7a573f](../../evidence/conditions-sets-033.md#c-54f40209db7a573f) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [状态效果 S-067aeae9e6ebedd7](../../evidence/state_effects-sets-002.md#s-067aeae9e6ebedd7)

### path-060680

```text
(config)# nat64 provisioning mode jp01 <cr>
```

Handler ` RVA 0xD595760 `；selector ` 14 `；EOL ` RVA 0x33E99988 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c72415a95050d922](../../evidence/conditions-sets-077.md#c-c72415a95050d922) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [状态效果 S-9969179893d99381](../../evidence/state_effects-sets-033.md#s-9969179893d99381)

### path-062728

```text
(config)# nat64 route <prefix:dynamic> <cr>
```

Handler ` RVA 0xD595760 `；selector ` 1 `；EOL ` RVA 0x33E99050 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` IPv4 prefix/length。

[条件 C-d994c2d27cc0538c](../../evidence/conditions-sets-084.md#c-d994c2d27cc0538c) · [缺口 G-844efc7083f01521](../../evidence/gaps-sets-005.md#g-844efc7083f01521) · [参数 P-fe248ae8d5ffec8d](../../evidence/parameters-sets-019.md#p-fe248ae8d5ffec8d) · [状态效果 S-9969179893d99381](../../evidence/state_effects-sets-033.md#s-9969179893d99381)

### path-062837

```text
(config)# nat64 route vrf <string> <prefix:dynamic> global <cr>
```

Handler ` RVA 0xD595760 `；selector ` 15 `；EOL ` RVA 0x33E98D58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` vrf name；` prefix_dynamic ` IPv6 prefix x:x::y/&lt;z&gt;。

[条件 C-fc065dcfcdbc6de9](../../evidence/conditions-sets-097.md#c-fc065dcfcdbc6de9) · [缺口 G-1652cc3c79e149ca](../../evidence/gaps-sets-001.md#g-1652cc3c79e149ca) · [参数 P-15a5727402964b74](../../evidence/parameters-sets-002.md#p-15a5727402964b74) · [状态效果 S-9969179893d99381](../../evidence/state_effects-sets-033.md#s-9969179893d99381)

### path-060455

```text
(config)# nat64 service ftp <cr>
```

Handler ` RVA 0xD595760 `；selector ` 5 `；EOL ` RVA 0x33E955B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b3af75ab9add37a6](../../evidence/conditions-sets-069.md#c-b3af75ab9add37a6) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [状态效果 S-812fdb4981cd91c0](../../evidence/state_effects-sets-027.md#s-812fdb4981cd91c0)

### path-060353

```text
(config)# nat64 settings <cr>
```

Handler ` RVA 0xD595760 `；selector ` 6 `；EOL ` RVA 0x33E981D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c72415a95050d922](../../evidence/conditions-sets-077.md#c-c72415a95050d922) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [状态效果 S-9969179893d99381](../../evidence/state_effects-sets-033.md#s-9969179893d99381)

### path-060673

```text
(config)# nat64 switchover replicate http <cr>
```

Handler ` RVA 0xD595760 `；selector ` 4 `；EOL ` RVA 0x33E97C48 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-57b420cfc63292a8](../../evidence/conditions-sets-034.md#c-57b420cfc63292a8) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [状态效果 S-5ec7cbb77ec961e0](../../evidence/state_effects-sets-020.md#s-5ec7cbb77ec961e0)

### path-060461

```text
(config)# nat64 translation max-entries <cr>
```

Handler ` RVA 0xD595760 `；selector ` 3 `；EOL ` RVA 0x33E97510 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6872fa61a6493830](../../evidence/conditions-sets-040.md#c-6872fa61a6493830) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [状态效果 S-b0ed3dd409c2b517](../../evidence/state_effects-sets-037.md#s-b0ed3dd409c2b517)

### path-060674

```text
(config)# nat64 v4 pool <string> <cr>
```

Handler ` RVA 0xD595760 `；selector ` 8 `；EOL ` RVA 0x33E95BC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` NAT64 pool name。

[条件 C-29ff47619a78a112](../../evidence/conditions-sets-016.md#c-29ff47619a78a112) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [参数 P-6362495cad706deb](../../evidence/parameters-sets-008.md#p-6362495cad706deb) · [状态效果 S-bbd83879225c113e](../../evidence/state_effects-sets-040.md#s-bbd83879225c113e)

### path-060685

```text
(config)# nat64 v6v4 list <string> <cr>
```

Handler ` RVA 0xD595760 `；selector ` 7 `；EOL ` RVA 0x33E964E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` IPv6 ACL name。

[条件 C-bb6215bdb56358fc](../../evidence/conditions-sets-072.md#c-bb6215bdb56358fc) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [参数 P-3e43d24e4bd05c44](../../evidence/parameters-sets-005.md#p-3e43d24e4bd05c44) · [状态效果 S-c132b7839e346a94](../../evidence/state_effects-sets-041.md#s-c132b7839e346a94)

### path-060444

```text
(config)# nat66 max-vpn <number:1..250> <cr>
```

Handler ` RVA 0xD60D510 `；selector ` 3 `；EOL ` RVA 0x33EAE3B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` max vpn number。

[条件 C-dc9dbf4b005ae0ca](../../evidence/conditions-sets-085.md#c-dc9dbf4b005ae0ca) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [参数 P-909b9f0e4fffa7ce](../../evidence/parameters-sets-011.md#p-909b9f0e4fffa7ce) · [状态效果 S-9969179893d99381](../../evidence/state_effects-sets-033.md#s-9969179893d99381)

### path-060438

```text
(config)# nat66 nd enable <cr>
```

Handler ` RVA 0xD60D510 `；selector ` 2 `；EOL ` RVA 0x33EAE070 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-dc9dbf4b005ae0ca](../../evidence/conditions-sets-085.md#c-dc9dbf4b005ae0ca) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [状态效果 S-ced85b22a5cdc650](../../evidence/state_effects-sets-044.md#s-ced85b22a5cdc650)

### path-062960

```text
(config)# nat66 prefix inside <prefix:dynamic> outside <prefix:dynamic> <cr>
```

Handler ` RVA 0xD60D510 `；selector ` 0 `；EOL ` RVA 0x33EAE938 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` IPv6 prefix；` prefix_dynamic ` IPv6 prefix。

[条件 C-849c61116bad0dfa](../../evidence/conditions-sets-051.md#c-849c61116bad0dfa) · [缺口 G-5c70f460731e85c7](../../evidence/gaps-sets-004.md#g-5c70f460731e85c7) · [参数 P-409d2f19a2ac1153](../../evidence/parameters-sets-005.md#p-409d2f19a2ac1153) · [状态效果 S-9969179893d99381](../../evidence/state_effects-sets-033.md#s-9969179893d99381)

### path-062834

```text
(config)# nat66 route vrf <string> <prefix:dynamic> global <cr>
```

Handler ` RVA 0xD60D510 `；selector ` 1 `；EOL ` RVA 0x33EAEFC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` vrf name；` prefix_dynamic ` IPv6 prefix x:x::y/&lt;z&gt;。

[条件 C-fb68f0ccef7acff9](../../evidence/conditions-sets-097.md#c-fb68f0ccef7acff9) · [缺口 G-662c9a26f7df70ca](../../evidence/gaps-sets-004.md#g-662c9a26f7df70ca) · [参数 P-9bcb7a461d3d8af3](../../evidence/parameters-sets-012.md#p-9bcb7a461d3d8af3) · [状态效果 S-9969179893d99381](../../evidence/state_effects-sets-033.md#s-9969179893d99381)

### path-034600

```text
(config)# ncia client <number:1..1> <address> <address> <cr>
```

Handler ` RVA 0x11B0D5C0 `；selector ` 3 `；EOL ` RVA 0x3562CAE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` NCIA Server Number；` address ` NCIA Client IP Address；` address ` NCIA Client Virtual Macaddr。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-959fd6c195f630a6](../../evidence/parameters-sets-011.md#p-959fd6c195f630a6) · [状态效果 S-bc9c73ae6f6202f2](../../evidence/state_effects-sets-040.md#s-bc9c73ae6f6202f2)

### path-056820

```text
(config)# ncia rsrb <number:1..4095> <number:1..15> <number:1..4095> <number:1..15> <number:1..4095> <address> <cr>
```

Handler ` RVA 0x11B0D5C0 `；selector ` 1 `；EOL ` RVA 0x3562C0E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` RSRB Virtual Ring Number；` unsigned_number ` RSRB Bridge Number；` unsigned_number ` Local Ring Number；` unsigned_number ` NCIA Bridge Number；` unsigned_number ` NCIA Ring Number；` address ` NCIA RSRB Virtual Macaddr。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-77e3c7b5163e96b3](../../evidence/parameters-sets-009.md#p-77e3c7b5163e96b3) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-052405

```text
(config)# ncia server <number:1..1> <address> <address> <address> <number:1..4095> <cr>
```

Handler ` RVA 0x11B0D5C0 `；selector ` 2 `；EOL ` RVA 0x3562C6C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` NCIA Server Number；` address ` NCIA Server IP Address；` address ` NCIA Server Virtual Macaddr；` address ` NCIA Virtual Macaddr for Client；` unsigned_number ` NCIA Virtual Macaddr Range。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-d887f3eab34b41cd](../../evidence/parameters-sets-016.md#p-d887f3eab34b41cd) · [状态效果 S-ac4e681c36b2d492](../../evidence/state_effects-sets-036.md#s-ac4e681c36b2d492)

### path-060756

```text
(config)# netbios <?dumper_command_func@555589e36bc8> access-list bytes <string> <cr>
```

Handler ` RVA 0xFDF2F20 `；selector ` 1 `；EOL ` RVA 0x348E32B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` NETBIOS station name。

[条件 C-2d23fd9f615f1028](../../evidence/conditions-sets-018.md#c-2d23fd9f615f1028) · [缺口 G-4cfecc84f004c6ad](../../evidence/gaps-sets-003.md#g-4cfecc84f004c6ad) · [参数 P-2b3136a571c60584](../../evidence/parameters-sets-004.md#p-2b3136a571c60584) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060501

```text
(config)# netbios <?dumper_command_func@555589e36bc8> access-list filter-name-recognized <cr>
```

Handler ` RVA 0xFDF2F20 `；selector ` 17 `；EOL ` RVA 0x348E35E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-05c9a13caea217f2](../../evidence/conditions-sets-003.md#c-05c9a13caea217f2) · [缺口 G-4cfecc84f004c6ad](../../evidence/gaps-sets-003.md#g-4cfecc84f004c6ad) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060755

```text
(config)# netbios <?dumper_command_func@555589e36bc8> access-list host <string> <cr>
```

Handler ` RVA 0xFDF2F20 `；selector ` 2 `；EOL ` RVA 0x348E2DF0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Access-list name。

[条件 C-73afb9aa6090c1ad](../../evidence/conditions-sets-045.md#c-73afb9aa6090c1ad) · [缺口 G-4cfecc84f004c6ad](../../evidence/gaps-sets-003.md#g-4cfecc84f004c6ad) · [参数 P-9931c63dcec376aa](../../evidence/parameters-sets-012.md#p-9931c63dcec376aa) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027913

```text
(config)# netbios name-cache <address> <string> <cr>
```

Handler ` RVA 0x114B2B70 `；selector ` 9 `；EOL ` RVA 0x354F6708 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` MAC addr of static name-cache entry；` string ` NetBIOS-name。

[条件 C-e6dcfaddcf65d419](../../evidence/conditions-sets-089.md#c-e6dcfaddcf65d419) · [参数 P-786916e5402d2c79](../../evidence/parameters-sets-009.md#p-786916e5402d2c79) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060757

```text
(config)# netbios name-cache <address> <string> <interface> <cr>
```

Handler ` RVA 0x114B2B70 `；selector ` 9 `；EOL ` RVA 0x354F6708 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` MAC addr of static name-cache entry；` string ` NetBIOS-name。

[条件 C-ab99676558a356ae](../../evidence/conditions-sets-066.md#c-ab99676558a356ae) · [缺口 G-973ff9524cba203c](../../evidence/gaps-sets-006.md#g-973ff9524cba203c) · [参数 P-e4aaabc155b564ff](../../evidence/parameters-sets-017.md#p-e4aaabc155b564ff) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026051

```text
(config)# netbios name-cache broadcast-name-recognized <cr>
```

Handler ` RVA 0x114B2B70 `；selector ` 15 `；EOL ` RVA 0x354F5E40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-05c9a13caea217f2](../../evidence/conditions-sets-003.md#c-05c9a13caea217f2) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026025

```text
(config)# netbios name-cache cache-add-name <cr>
```

Handler ` RVA 0x114B2B70 `；selector ` 10 `；EOL ` RVA 0x354F5658 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-05c9a13caea217f2](../../evidence/conditions-sets-003.md#c-05c9a13caea217f2) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025517

```text
(config)# netbios name-cache name-len <number:8..16> <cr>
```

Handler ` RVA 0x114B2B70 `；selector ` 14 `；EOL ` RVA 0x354F5680 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Numbers。

[条件 C-b89937912f9db0a6](../../evidence/conditions-sets-071.md#c-b89937912f9db0a6) · [参数 P-fa2bc988407fd60e](../../evidence/parameters-sets-019.md#p-fa2bc988407fd60e) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025520

```text
(config)# netbios name-cache proxy-datagram <number:0..4294967295> <cr>
```

Handler ` RVA 0x114B2B70 `；selector ` 13 `；EOL ` RVA 0x354F5900 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Seconds。

[条件 C-c546fc535269bc0b](../../evidence/conditions-sets-076.md#c-c546fc535269bc0b) · [参数 P-a4ef1e70955f04ce](../../evidence/parameters-sets-013.md#p-a4ef1e70955f04ce) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025524

```text
(config)# netbios name-cache query-timeout <number:1..4294967295> <cr>
```

Handler ` RVA 0x114B2B70 `；selector ` 7 `；EOL ` RVA 0x354F5E68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Seconds。

[条件 C-6ef592e917046a19](../../evidence/conditions-sets-043.md#c-6ef592e917046a19) · [参数 P-1f9ffad6c85b6a1f](../../evidence/parameters-sets-003.md#p-1f9ffad6c85b6a1f) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025525

```text
(config)# netbios name-cache recognized-timeout <number:1..4294967295> <cr>
```

Handler ` RVA 0x114B2B70 `；selector ` 8 `；EOL ` RVA 0x354F60E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Seconds。

[条件 C-4f9451b116c3b779](../../evidence/conditions-sets-031.md#c-4f9451b116c3b779) · [参数 P-7064d21139b7dd36](../../evidence/parameters-sets-009.md#p-7064d21139b7dd36) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025512

```text
(config)# netbios name-cache timeout <number:1..35000> <cr>
```

Handler ` RVA 0x114B2B70 `；selector ` 6 `；EOL ` RVA 0x354F5378 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Minutes。

[条件 C-a18d155ff705350d](../../evidence/conditions-sets-062.md#c-a18d155ff705350d) · [参数 P-c9c6fd78708934c7](../../evidence/parameters-sets-015.md#p-c9c6fd78708934c7) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060956

```text
(config)# netconf beep initiator <string> <number:1..65535> <cr>
```

Handler ` RVA 0xF3BF350 `；selector ` 0 `；EOL ` RVA 0x34629080 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Hostname or ip address of remote；` unsigned_number ` BEEP port to send on。

[条件 C-22f7474d2585217e](../../evidence/conditions-sets-014.md#c-22f7474d2585217e) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [参数 P-c4907844995bcf12](../../evidence/parameters-sets-015.md#p-c4907844995bcf12) · [状态效果 S-9969179893d99381](../../evidence/state_effects-sets-033.md#s-9969179893d99381)

### path-060483

```text
(config)# netconf beep listener <cr>
```

Handler ` RVA 0xF3BE3C0 `；selector ` 0 `；EOL ` RVA 0x34628AE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5de4a3a452c0aa5f](../../evidence/conditions-sets-037.md#c-5de4a3a452c0aa5f) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [状态效果 S-9969179893d99381](../../evidence/state_effects-sets-033.md#s-9969179893d99381)

### path-060340

```text
(config)# netconf detailed-error <cr>
```

Handler ` RVA 0xF3BBC30 `；selector ` 6 `；EOL ` RVA 0x34627350 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [状态效果 S-9969179893d99381](../../evidence/state_effects-sets-033.md#s-9969179893d99381)

### path-060354

```text
(config)# netconf format <cr>
```

Handler ` RVA 0xF3BBC30 `；selector ` 3 `；EOL ` RVA 0x34628010 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c04a45ac460c8459](../../evidence/conditions-sets-074.md#c-c04a45ac460c8459) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [状态效果 S-9969179893d99381](../../evidence/state_effects-sets-033.md#s-9969179893d99381)

### path-060342

```text
(config)# netconf legacy <cr>
```

Handler ` RVA 0xF3BBC30 `；selector ` 5 `；EOL ` RVA 0x34627630 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [状态效果 S-9969179893d99381](../../evidence/state_effects-sets-033.md#s-9969179893d99381)

### path-060352

```text
(config)# netconf lock-time <cr>
```

Handler ` RVA 0xF3BBC30 `；selector ` 2 `；EOL ` RVA 0x34627CC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-60612ea25e6dc393](../../evidence/conditions-sets-037.md#c-60612ea25e6dc393) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [状态效果 S-9969179893d99381](../../evidence/state_effects-sets-033.md#s-9969179893d99381)

### path-060358

```text
(config)# netconf max-message <cr>
```

Handler ` RVA 0xF3BBC30 `；selector ` 4 `；EOL ` RVA 0x34628370 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d0a6baf1b7eb68a9](../../evidence/conditions-sets-080.md#c-d0a6baf1b7eb68a9) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [状态效果 S-9969179893d99381](../../evidence/state_effects-sets-033.md#s-9969179893d99381)

### path-060346

```text
(config)# netconf max-sessions <cr>
```

Handler ` RVA 0xF3BBC30 `；selector ` 1 `；EOL ` RVA 0x34627970 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f760487ddc67b5b3](../../evidence/conditions-sets-096.md#c-f760487ddc67b5b3) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [状态效果 S-9969179893d99381](../../evidence/state_effects-sets-033.md#s-9969179893d99381)

### path-060360

```text
(config)# netconf ssh <cr>
```

Handler ` RVA 0xF3CA630 `；selector ` 0 `；EOL ` RVA 0x34628700 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f281ff34a2b5430a](../../evidence/conditions-sets-094.md#c-f281ff34a2b5430a) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [状态效果 S-9969179893d99381](../../evidence/state_effects-sets-033.md#s-9969179893d99381)

### path-063003

```text
(config)# netconf-yang <cr>
```

Handler ` RVA 0xDF978A0 `；selector ` 0 `；EOL ` 历史 VA 0x7FFFBAE6FAC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8cfd8d765dbf7ae4](../../evidence/conditions-sets-055.md#c-8cfd8d765dbf7ae4) · [缺口 G-51a74544a691adb9](../../evidence/gaps-sets-003.md#g-51a74544a691adb9) · [状态效果 S-adf2d2b211adbbd9](../../evidence/state_effects-sets-037.md#s-adf2d2b211adbbd9)

### path-063004

```text
(config)# netconf-yang <cr>
```

Handler ` RVA 0xDF978A0 `；selector ` 0 `；EOL ` 历史 VA 0x7FFF37E9D0E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-491028f99952635a](../../evidence/conditions-sets-029.md#c-491028f99952635a) · [缺口 G-741d5bb1b8461349](../../evidence/gaps-sets-004.md#g-741d5bb1b8461349) · [状态效果 S-9b782c97ba53600f](../../evidence/state_effects-sets-033.md#s-9b782c97ba53600f)

### path-063080

```text
(config)# netconf-yang callhome client <string> <cr>
```

Handler ` RVA 0xDF978A0 `；selector ` 0 `；EOL ` 历史 VA 0x7FFF37E68C30 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Client name。

[条件 C-e80f8c5baaeba577](../../evidence/conditions-sets-090.md#c-e80f8c5baaeba577) · [缺口 G-1caf4ac109cbedb0](../../evidence/gaps-sets-001.md#g-1caf4ac109cbedb0) · [参数 P-1363394f24c51448](../../evidence/parameters-sets-002.md#p-1363394f24c51448) · [状态效果 S-ce52511e539d9e60](../../evidence/state_effects-sets-044.md#s-ce52511e539d9e60)

### path-063085

```text
(config)# netconf-yang callhome client <string> <cr>
```

Handler ` RVA 0xDF978A0 `；selector ` 0 `；EOL ` 历史 VA 0x7FFF37E68F38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Client name。

[条件 C-7cf59eaa54cedbc6](../../evidence/conditions-sets-048.md#c-7cf59eaa54cedbc6) · [缺口 G-e4b2d0889fa2f0de](../../evidence/gaps-sets-008.md#g-e4b2d0889fa2f0de) · [参数 P-1363394f24c51448](../../evidence/parameters-sets-002.md#p-1363394f24c51448) · [状态效果 S-53e7bdfae4bd9d88](../../evidence/state_effects-sets-018.md#s-53e7bdfae4bd9d88)

### path-063054

```text
(config)# netconf-yang cisco-ia auto-sync <cr>
```

Handler ` RVA 0xDF978A0 `；selector ` 0 `；EOL ` 历史 VA 0x7FFFBAED7D20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-43c7198295608857](../../evidence/conditions-sets-027.md#c-43c7198295608857) · [缺口 G-068bf75c9cd616d3](../../evidence/gaps-sets-001.md#g-068bf75c9cd616d3) · [状态效果 S-e61c345d53de95cb](../../evidence/state_effects-sets-049.md#s-e61c345d53de95cb)

### path-063113

```text
(config)# netconf-yang cisco-ia auto-sync disabled <cr>
```

Handler ` RVA 0xDF978A0 `；selector ` 0 `；EOL ` 历史 VA 0x7FFFBAECA4B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4ff6ecace5c42d61](../../evidence/conditions-sets-031.md#c-4ff6ecace5c42d61) · [缺口 G-4470323a09b650ef](../../evidence/gaps-sets-003.md#g-4470323a09b650ef) · [状态效果 S-366e3d6cafa17904](../../evidence/state_effects-sets-012.md#s-366e3d6cafa17904)

### path-063114

```text
(config)# netconf-yang cisco-ia auto-sync disabled <cr>
```

Handler ` RVA 0xDF978A0 `；selector ` 0 `；EOL ` 历史 VA 0x7FFF37EA3198 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a8409178c912c9e5](../../evidence/conditions-sets-065.md#c-a8409178c912c9e5) · [缺口 G-29c93705c7dc6c03](../../evidence/gaps-sets-002.md#g-29c93705c7dc6c03) · [状态效果 S-e90f011c6d61533d](../../evidence/state_effects-sets-049.md#s-e90f011c6d61533d)

### path-063109

```text
(config)# netconf-yang cisco-ia blocking cli-blocking-enabled <cr>
```

Handler ` RVA 0xDF978A0 `；selector ` 0 `；EOL ` 历史 VA 0x7FFFBAEC8B50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-223faefd2899d8a3](../../evidence/conditions-sets-013.md#c-223faefd2899d8a3) · [缺口 G-f6d45f9ce0491795](../../evidence/gaps-sets-009.md#g-f6d45f9ce0491795) · [状态效果 S-6168d7a4a4df53f5](../../evidence/state_effects-sets-021.md#s-6168d7a4a4df53f5)

### path-063110

```text
(config)# netconf-yang cisco-ia blocking cli-blocking-enabled <cr>
```

Handler ` RVA 0xDF978A0 `；selector ` 0 `；EOL ` 历史 VA 0x7FFFBAED7B70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4d3f2881fb12d3fc](../../evidence/conditions-sets-030.md#c-4d3f2881fb12d3fc) · [缺口 G-cffd30a20060d001](../../evidence/gaps-sets-007.md#g-cffd30a20060d001) · [状态效果 S-91acec2dced2db4f](../../evidence/state_effects-sets-031.md#s-91acec2dced2db4f)

### path-063118

```text
(config)# netconf-yang cisco-ia blocking confd-cfg-blocking-enabled <cr>
```

Handler ` RVA 0xDF978A0 `；selector ` 0 `；EOL ` 历史 VA 0x7FFFBAEC7A38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4ea2d3a42378fa57](../../evidence/conditions-sets-031.md#c-4ea2d3a42378fa57) · [缺口 G-7268d0fe013a0ad8](../../evidence/gaps-sets-004.md#g-7268d0fe013a0ad8) · [状态效果 S-ba84ada907f86d33](../../evidence/state_effects-sets-039.md#s-ba84ada907f86d33)

### path-063119

```text
(config)# netconf-yang cisco-ia blocking confd-cfg-blocking-enabled <cr>
```

Handler ` RVA 0xDF978A0 `；selector ` 0 `；EOL ` 历史 VA 0x7FFFBAED7AE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ffde9d1f3a43dcd3](../../evidence/conditions-sets-099.md#c-ffde9d1f3a43dcd3) · [缺口 G-046a02c1df2d3d65](../../evidence/gaps-sets-001.md#g-046a02c1df2d3d65) · [状态效果 S-95643610d0be692f](../../evidence/state_effects-sets-032.md#s-95643610d0be692f)

### path-063145

```text
(config)# netconf-yang cisco-ia blocking confd-cfg-command <string> <cr>
```

Handler ` RVA 0xDF978A0 `；selector ` 0 `；EOL ` 历史 VA 0x7FFFBAEC6BE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Specifies pattern to omit。

[条件 C-8e9cf0b760bc1c13](../../evidence/conditions-sets-055.md#c-8e9cf0b760bc1c13) · [缺口 G-5a5a4bc30b584e3e](../../evidence/gaps-sets-004.md#g-5a5a4bc30b584e3e) · [参数 P-6f0b907407e5bfdb](../../evidence/parameters-sets-009.md#p-6f0b907407e5bfdb) · [状态效果 S-48b423f29979903c](../../evidence/state_effects-sets-016.md#s-48b423f29979903c)

### path-063146

```text
(config)# netconf-yang cisco-ia blocking confd-cfg-command <string> <cr>
```

Handler ` RVA 0xDF978A0 `；selector ` 0 `；EOL ` 历史 VA 0x7FFFBAED7A50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Specifies pattern to omit。

[条件 C-2ed854e1e5eb6f6a](../../evidence/conditions-sets-018.md#c-2ed854e1e5eb6f6a) · [缺口 G-2d176add99305be4](../../evidence/gaps-sets-002.md#g-2d176add99305be4) · [参数 P-6f0b907407e5bfdb](../../evidence/parameters-sets-009.md#p-6f0b907407e5bfdb) · [状态效果 S-3013dd2c7226fd95](../../evidence/state_effects-sets-011.md#s-3013dd2c7226fd95)

### path-063150

```text
(config)# netconf-yang cisco-ia blocking network-element-command <string> <cr>
```

Handler ` RVA 0xDF978A0 `；selector ` 0 `；EOL ` 历史 VA 0x7FFFBAEC5BF0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Specifies pattern to disallow。

[条件 C-ce2f712fe5530fd6](../../evidence/conditions-sets-079.md#c-ce2f712fe5530fd6) · [缺口 G-aaedd77a8c40189d](../../evidence/gaps-sets-006.md#g-aaedd77a8c40189d) · [参数 P-e856ae823e7e144f](../../evidence/parameters-sets-017.md#p-e856ae823e7e144f) · [状态效果 S-2ce2da83eb4ac4d1](../../evidence/state_effects-sets-010.md#s-2ce2da83eb4ac4d1)

### path-063151

```text
(config)# netconf-yang cisco-ia blocking network-element-command <string> <cr>
```

Handler ` RVA 0xDF978A0 `；selector ` 0 `；EOL ` 历史 VA 0x7FFF37EA2D18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Specifies pattern to disallow。

[条件 C-49f4f05bf1279443](../../evidence/conditions-sets-029.md#c-49f4f05bf1279443) · [缺口 G-04922c7964b10adb](../../evidence/gaps-sets-001.md#g-04922c7964b10adb) · [参数 P-e856ae823e7e144f](../../evidence/parameters-sets-017.md#p-e856ae823e7e144f) · [状态效果 S-c7745d41be2c8571](../../evidence/state_effects-sets-042.md#s-c7745d41be2c8571)

### path-063083

```text
(config)# netconf-yang cisco-ia conf-full-sync-cli <string> <cr>
```

Handler ` RVA 0xDF978A0 `；selector ` 0 `；EOL ` 历史 VA 0x7FFF37E91180 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Specifies command line。

[条件 C-7e91567a12b927f5](../../evidence/conditions-sets-049.md#c-7e91567a12b927f5) · [缺口 G-55fbaf1252ab5749](../../evidence/gaps-sets-003.md#g-55fbaf1252ab5749) · [参数 P-3581662399ab46ab](../../evidence/parameters-sets-005.md#p-3581662399ab46ab) · [状态效果 S-0044c9bb92064171](../../evidence/state_effects-sets-001.md#s-0044c9bb92064171)

### path-063084

```text
(config)# netconf-yang cisco-ia conf-full-sync-cli <string> <cr>
```

Handler ` RVA 0xDF978A0 `；selector ` 0 `；EOL ` 历史 VA 0x7FFFBAED7660 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Specifies command line。

[条件 C-bc6a6620fcabd7d8](../../evidence/conditions-sets-073.md#c-bc6a6620fcabd7d8) · [缺口 G-1b07bc56b5f7e3cb](../../evidence/gaps-sets-001.md#g-1b07bc56b5f7e3cb) · [参数 P-3581662399ab46ab](../../evidence/parameters-sets-005.md#p-3581662399ab46ab) · [状态效果 S-0c5942e68993e1af](../../evidence/state_effects-sets-003.md#s-0c5942e68993e1af)

### path-063086

```text
(config)# netconf-yang cisco-ia conf-parser-msg-error <string> <cr>
```

Handler ` RVA 0xDF978A0 `；selector ` 0 `；EOL ` 历史 VA 0x7FFF37E90318 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Specifies parser message that is a true error。

[条件 C-356bde53fcd7613c](../../evidence/conditions-sets-021.md#c-356bde53fcd7613c) · [缺口 G-1300e1f8480b721c](../../evidence/gaps-sets-001.md#g-1300e1f8480b721c) · [参数 P-522d7414e19021cd](../../evidence/parameters-sets-007.md#p-522d7414e19021cd) · [状态效果 S-2d05aa67dbdd91fd](../../evidence/state_effects-sets-010.md#s-2d05aa67dbdd91fd)

### path-063087

```text
(config)# netconf-yang cisco-ia conf-parser-msg-error <string> <cr>
```

Handler ` RVA 0xDF978A0 `；selector ` 0 `；EOL ` 历史 VA 0x7FFF37EA2928 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Specifies parser message that is a true error。

[条件 C-6ed9be934c8e223d](../../evidence/conditions-sets-043.md#c-6ed9be934c8e223d) · [缺口 G-70b8cb39a6d55164](../../evidence/gaps-sets-004.md#g-70b8cb39a6d55164) · [参数 P-522d7414e19021cd](../../evidence/parameters-sets-007.md#p-522d7414e19021cd) · [状态效果 S-0762c9f4574383d8](../../evidence/state_effects-sets-002.md#s-0762c9f4574383d8)

### path-063089

```text
(config)# netconf-yang cisco-ia conf-parser-msg-ignore <string> <cr>
```

Handler ` RVA 0xDF978A0 `；selector ` 0 `；EOL ` 历史 VA 0x7FFF37E8F288 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Specifies parser message。

[条件 C-50dd9d451957e544](../../evidence/conditions-sets-032.md#c-50dd9d451957e544) · [缺口 G-dbd898e33953083d](../../evidence/gaps-sets-008.md#g-dbd898e33953083d) · [参数 P-bc459a07562f2c01](../../evidence/parameters-sets-014.md#p-bc459a07562f2c01) · [状态效果 S-ed7d5d54ca62a130](../../evidence/state_effects-sets-050.md#s-ed7d5d54ca62a130)

### path-063090

```text
(config)# netconf-yang cisco-ia conf-parser-msg-ignore <string> <cr>
```

Handler ` RVA 0xDF978A0 `；selector ` 0 `；EOL ` 历史 VA 0x7FFFBAED74B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Specifies parser message。

[条件 C-9655fc7208bf9890](../../evidence/conditions-sets-058.md#c-9655fc7208bf9890) · [缺口 G-d66f0bf102bf42ec](../../evidence/gaps-sets-007.md#g-d66f0bf102bf42ec) · [参数 P-bc459a07562f2c01](../../evidence/parameters-sets-014.md#p-bc459a07562f2c01) · [状态效果 S-b3b815f0d492fe7c](../../evidence/state_effects-sets-038.md#s-b3b815f0d492fe7c)

### path-063057

```text
(config)# netconf-yang cisco-ia config-change-delay <cr>
```

Handler ` RVA 0xDF978A0 `；selector ` 0 `；EOL ` 历史 VA 0x7FFF37EA26E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f23ccb25f7684fca](../../evidence/conditions-sets-094.md#c-f23ccb25f7684fca) · [缺口 G-9c9d1254313e085f](../../evidence/gaps-sets-006.md#g-9c9d1254313e085f) · [状态效果 S-c7180a85497bc255](../../evidence/state_effects-sets-042.md#s-c7180a85497bc255)

### path-063092

```text
(config)# netconf-yang cisco-ia config-change-delay <number:0..65535> <cr>
```

Handler ` RVA 0xDF978A0 `；selector ` 0 `；EOL ` 历史 VA 0x7FFF37E8E2A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Delay in ms before applying CDB change to NE。

[条件 C-0f13697c9cee55dc](../../evidence/conditions-sets-006.md#c-0f13697c9cee55dc) · [缺口 G-3736d9aaaf4b43ee](../../evidence/gaps-sets-002.md#g-3736d9aaaf4b43ee) · [参数 P-6494ceb581f794f3](../../evidence/parameters-sets-008.md#p-6494ceb581f794f3) · [状态效果 S-0a38c464e7a36bb1](../../evidence/state_effects-sets-003.md#s-0a38c464e7a36bb1)

### path-063093

```text
(config)# netconf-yang cisco-ia config-change-delay <number:0..65535> <cr>
```

Handler ` RVA 0xDF978A0 `；selector ` 0 `；EOL ` 历史 VA 0x7FFF37EA2778 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Delay in ms before applying CDB change to NE。

[条件 C-61e473ffb76401c2](../../evidence/conditions-sets-038.md#c-61e473ffb76401c2) · [缺口 G-d59bd9e568f4f94d](../../evidence/gaps-sets-007.md#g-d59bd9e568f4f94d) · [参数 P-6494ceb581f794f3](../../evidence/parameters-sets-008.md#p-6494ceb581f794f3) · [状态效果 S-c97d564d17841b73](../../evidence/state_effects-sets-043.md#s-c97d564d17841b73)

### path-063062

```text
(config)# netconf-yang cisco-ia init-sync <cr>
```

Handler ` RVA 0xDF978A0 `；selector ` 0 `；EOL ` 历史 VA 0x7FFF37EA2538 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4afb0f1bb65299a3](../../evidence/conditions-sets-029.md#c-4afb0f1bb65299a3) · [缺口 G-15e5c7ba5f200a92](../../evidence/gaps-sets-001.md#g-15e5c7ba5f200a92) · [状态效果 S-8e0a3c4f2c96d011](../../evidence/state_effects-sets-030.md#s-8e0a3c4f2c96d011)

### path-063129

```text
(config)# netconf-yang cisco-ia init-sync disabled <cr>
```

Handler ` RVA 0xDF978A0 `；selector ` 0 `；EOL ` 历史 VA 0x7FFFBAEBFE38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c31d087063601ab9](../../evidence/conditions-sets-075.md#c-c31d087063601ab9) · [缺口 G-dd2c3288ccbcc219](../../evidence/gaps-sets-008.md#g-dd2c3288ccbcc219) · [状态效果 S-7f1ed72fbabfc335](../../evidence/state_effects-sets-027.md#s-7f1ed72fbabfc335)

