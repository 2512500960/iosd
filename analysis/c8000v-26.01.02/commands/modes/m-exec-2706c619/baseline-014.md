# exec · 六个基础模式的历史连接

[模式索引](README.md) · [总索引](../../README.md)

### path-012344

```text
(exec)# do-exec clear rif-cache <cr>
```

Handler ` RVA 0x124072B0 `；selector ` 0 `；EOL ` RVA 0x3584F7A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-017563

```text
(exec)# do-exec clear route-map counters <string> <cr>
```

Handler ` RVA 0xE22E110 `；selector ` 0 `；EOL ` RVA 0x34246048 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Route Map Name。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-52aca164f0880451](../../evidence/parameters-sets-007.md#p-52aca164f0880451) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-013964

```text
(exec)# do-exec clear rudpv1 statistics <cr>
```

Handler ` RVA 0x1617CBC0 `；selector ` 1 `；EOL ` RVA 0x35F04230 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-012425

```text
(exec)# do-exec clear sampler <cr>
```

Handler ` RVA 0xC17E1A0 `；selector ` 0 `；EOL ` RVA 0x339E79E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-afca1c8acf7841af](../../evidence/conditions-sets-068.md#c-afca1c8acf7841af) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-013896

```text
(exec)# do-exec clear service-routing capabilities-manager <cr>
```

Handler ` RVA 0x1045B420 `；selector ` 76 `；EOL ` RVA 0x34B33B30 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-017827

```text
(exec)# do-exec clear service-routing client <number:0..65535> <cr>
```

Handler ` RVA 0x104521D0 `；selector ` 2 `；EOL ` RVA 0x34B2A458 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Client handle。

[条件 C-8646e7cce1c82449](../../evidence/conditions-sets-052.md#c-8646e7cce1c82449) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-5dbf6eb77b33065c](../../evidence/parameters-sets-007.md#p-5dbf6eb77b33065c) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-025256

```text
(exec)# do-exec clear service-routing database <number:0..65535> : <number:0..65535> : <number:0..4294967295> . <number:0..4294967295> . <number:0..4294967295> . <number:0..4294967295> <cr>
```

Handler ` RVA 0x104521D0 `；selector ` 3 `；EOL ` RVA 0x34B29FB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance。

[条件 C-6d92551faca8d1c9](../../evidence/conditions-sets-042.md#c-6d92551faca8d1c9) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-b207d0bb6f65dc60](../../evidence/parameters-sets-013.md#p-b207d0bb6f65dc60) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-013816

```text
(exec)# do-exec clear smef stats <cr>
```

Handler ` RVA 0x108F4A00 `；selector ` 1 `；EOL ` RVA 0x34BF79E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b665e2b48af959ff](../../evidence/conditions-sets-071.md#c-b665e2b48af959ff) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-017723

```text
(exec)# do-exec clear snmp stats hosts <cr>
```

Handler ` RVA 0x104BFC00 `；selector ` 0 `；EOL ` RVA 0x33C2B8A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-df141d52a3cb971f](../../evidence/conditions-sets-086.md#c-df141d52a3cb971f) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-017711

```text
(exec)# do-exec clear snmp sync lock <cr>
```

Handler ` RVA 0x104F0150 `；selector ` 0 `；EOL ` RVA 0x33C2B5D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a7417b278c29a14e](../../evidence/conditions-sets-065.md#c-a7417b278c29a14e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-013783

```text
(exec)# do-exec clear sockets <number:1..4294967295> <cr>
```

Handler ` RVA 0xD067830 `；selector ` 0 `；EOL ` RVA 0x33D89498 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` \[pid\]。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-df57faf1f861f4b2](../../evidence/parameters-sets-017.md#p-df57faf1f861f4b2) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-012579

```text
(exec)# do-exec clear source-bridge <cr>
```

Handler ` RVA 0x113A4950 `；selector ` 0 `；EOL ` RVA 0x354A63E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c2f0d8d765308f6e](../../evidence/conditions-sets-075.md#c-c2f0d8d765308f6e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-012288

```text
(exec)# do-exec clear startup-config <cr>
```

Handler ` RVA 0xDFF0D00 `；selector ` 2 `；EOL ` RVA 0x341201F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-017194

```text
(exec)# do-exec clear subscriber coa statistics <cr>
```

Handler ` RVA 0x109E13C0 `；selector ` 0 `；EOL ` RVA 0x34C5F598 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-017221

```text
(exec)# do-exec clear subscriber disconnect history <cr>
```

Handler ` RVA 0x10A1B520 `；selector ` 0 `；EOL ` RVA 0x34C5FE80 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-017243

```text
(exec)# do-exec clear subscriber disconnect stats <cr>
```

Handler ` RVA 0x10A1B5B0 `；selector ` 0 `；EOL ` RVA 0x34C60128 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021279

```text
(exec)# do-exec clear subscriber lite-session ip <address> <cr>
```

Handler ` RVA 0x10A1BAD0 `；selector ` 0 `；EOL ` RVA 0x34C611A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` IPv4 address。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-465dcddc8ecfbf67](../../evidence/parameters-sets-006.md#p-465dcddc8ecfbf67) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021237

```text
(exec)# do-exec clear subscriber log mac-address <string> <cr>
```

Handler ` RVA 0x10A1C360 `；selector ` 0 `；EOL ` RVA 0x34C60738 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` subscriber log。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-8a55b604c7cceac0](../../evidence/parameters-sets-011.md#p-8a55b604c7cceac0) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024637

```text
(exec)# do-exec clear subscriber log vrf <string> ip <address> <cr>
```

Handler ` RVA 0x10A1C4E0 `；selector ` 0 `；EOL ` RVA 0x34C60AA0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string `  vrf name ；` address ` IPV4 address。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-fc85a33c794d4c15](../../evidence/parameters-sets-019.md#p-fc85a33c794d4c15) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-017404

```text
(exec)# do-exec clear subscriber policy conditions <cr>
```

Handler ` RVA 0x10A5CC50 `；selector ` 0 `；EOL ` RVA 0x34C74620 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3ee3007732399fea](../../evidence/conditions-sets-024.md#c-3ee3007732399fea) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021487

```text
(exec)# do-exec clear subscriber policy peer all <cr>
```

Handler ` RVA 0xFE8BEF0 `；selector ` 3 `；EOL ` RVA 0x34906F98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3ee3007732399fea](../../evidence/conditions-sets-024.md#c-3ee3007732399fea) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d81ea206e17a7231](../../evidence/state_effects-sets-046.md#s-d81ea206e17a7231)

### path-023582

```text
(exec)# do-exec clear subscriber policy preauth handle <number:0..4294967295> <cr>
```

Handler ` RVA 0x109A64A0 `；selector ` 2 `；EOL ` RVA 0x34C50008 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Enter Policy Handle。

[条件 C-894112a3b8d88dee](../../evidence/conditions-sets-053.md#c-894112a3b8d88dee) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-79238e2f008eaf91](../../evidence/parameters-sets-009.md#p-79238e2f008eaf91) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-017385

```text
(exec)# do-exec clear subscriber policy rules <cr>
```

Handler ` RVA 0x10A70090 `；selector ` 0 `；EOL ` RVA 0x34C74368 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3ee3007732399fea](../../evidence/conditions-sets-024.md#c-3ee3007732399fea) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-017313

```text
(exec)# do-exec clear subscriber session all <cr>
```

Handler ` RVA 0x10A1BBD0 `；selector ` 0 `；EOL ` RVA 0x34C61528 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a49559e929201636](../../evidence/conditions-sets-063.md#c-a49559e929201636) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-604a49aa8e5d6a8a](../../evidence/state_effects-sets-021.md#s-604a49aa8e5d6a8a)

### path-013390

```text
(exec)# do-exec clear subscriber statistics <cr>
```

Handler ` RVA 0x10A1EB60 `；selector ` 0 `；EOL ` RVA 0x34C603C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-017224

```text
(exec)# do-exec clear subscriber template idle <cr>
```

Handler ` RVA 0x10A243A0 `；selector ` 0 `；EOL ` RVA 0x34C5FB80 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-cbe5d62fb709548d](../../evidence/conditions-sets-078.md#c-cbe5d62fb709548d) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021203

```text
(exec)# do-exec clear subscriber template tid <number:1..1000> <cr>
```

Handler ` RVA 0x10A24310 `；selector ` 0 `；EOL ` RVA 0x34C5F8F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Template Id。

[条件 C-cbe5d62fb709548d](../../evidence/conditions-sets-078.md#c-cbe5d62fb709548d) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-b2ac16fcff39191c](../../evidence/parameters-sets-014.md#p-b2ac16fcff39191c) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-017673

```text
(exec)# do-exec clear tcp ha statistics <cr>
```

Handler ` RVA 0x123C5CC0 `；selector ` 0 `；EOL ` RVA 0x35844EF0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-99e59c167808dff6](../../evidence/state_effects-sets-033.md#s-99e59c167808dff6)

### path-025015

```text
(exec)# do-exec clear tcp local <address> <number:1..65535> remote <address> <number:1..65535> <cr>
```

Handler ` RVA 0xCDEF5E0 `；selector ` 0 `；EOL ` RVA 0x33D027A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Local host name or IP address；` unsigned_number ` Local TCP port；` address ` Remote host name or IP address；` unsigned_number ` Remote TCP port。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-be899779410f7be3](../../evidence/parameters-sets-014.md#p-be899779410f7be3) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-013667

```text
(exec)# do-exec clear tcp statistics <cr>
```

Handler ` RVA 0xCDEF5E0 `；selector ` 3 `；EOL ` RVA 0x33D00950 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-017578

```text
(exec)# do-exec clear tcp statistics ingress <cr>
```

Handler ` RVA 0xCDEF5E0 `；selector ` 4 `；EOL ` RVA 0x33D00928 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0b7b7bd108ff5a2a](../../evidence/conditions-sets-005.md#c-0b7b7bd108ff5a2a) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-f2faae1c515ccef8](../../evidence/state_effects-sets-051.md#s-f2faae1c515ccef8)

### path-013614

```text
(exec)# do-exec clear vlan counters <cr>
```

Handler ` RVA 0x15C83570 `；selector ` 1 `；EOL ` RVA 0x35DFF158 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-182219d37cf0dc26](../../evidence/conditions-sets-009.md#c-182219d37cf0dc26) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-013406

```text
(exec)# do-exec clear vlan-autoconfig Statistics <cr>
```

Handler ` RVA 0x112BC610 `；selector ` 9 `；EOL ` RVA 0x354507E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-013969

```text
(exec)# do-exec clear vpdn accounting <cr>
```

Handler ` RVA 0x11D467B0 `；selector ` 37 `；EOL ` RVA 0x35707FB0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-017967

```text
(exec)# do-exec clear vpdn dead-cache all <cr>
```

Handler ` RVA 0x11DB86F0 `；selector ` 1 `；EOL ` RVA 0x35708B38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021823

```text
(exec)# do-exec clear vpdn dead-cache group <string> <cr>
```

Handler ` RVA 0x11DB86F0 `；selector ` 2 `；EOL ` RVA 0x357085D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Name of VPDN group。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-971a473fbe1885df](../../evidence/parameters-sets-012.md#p-971a473fbe1885df) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021828

```text
(exec)# do-exec clear vpdn dead-cache ip-address <address> <cr>
```

Handler ` RVA 0x11DB86F0 `；selector ` 3 `；EOL ` RVA 0x357088B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` IP address。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-e415f3e899e97e2f](../../evidence/parameters-sets-017.md#p-e415f3e899e97e2f) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-017899

```text
(exec)# do-exec clear vpdn history failure <cr>
```

Handler ` RVA 0x11D467B0 `；selector ` 52 `；EOL ` RVA 0x35707D20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-014023

```text
(exec)# do-exec clear vpdn queue <cr>
```

Handler ` RVA 0x11D467B0 `；selector ` 38 `；EOL ` RVA 0x35708DE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-013986

```text
(exec)# do-exec clear vpdn redirect <cr>
```

Handler ` RVA 0x11DB8790 `；selector ` 0 `；EOL ` RVA 0x35708258 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021789

```text
(exec)# do-exec clear vpdn statistics call fsm <cr>
```

Handler ` RVA 0x11D9C4F0 `；selector ` 0 `；EOL ` RVA 0x35707448 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021796

```text
(exec)# do-exec clear vpdn statistics mgr fsm <cr>
```

Handler ` RVA 0x11DA0ED0 `；selector ` 0 `；EOL ` RVA 0x35707718 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-017881

```text
(exec)# do-exec clear vpdn subscriber fsm <cr>
```

Handler ` RVA 0x11E16690 `；selector ` 0 `；EOL ` RVA 0x35707A28 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-013638

```text
(exec)# do-exec clear vrrp statistics <cr>
```

Handler ` RVA 0x133C90B0 `；selector ` 0 `；EOL ` RVA 0x35A809F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ec728df5d696ccb5](../../evidence/conditions-sets-091.md#c-ec728df5d696ccb5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-ad6c8482ca55c086](../../evidence/state_effects-sets-037.md#s-ad6c8482ca55c086)

### path-017991

```text
(exec)# do-exec clear vtemplate redundancy counters <cr>
```

Handler ` RVA 0x105C8720 `；selector ` 0 `；EOL ` RVA 0x34BAF818 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d9b21c69110ab307](../../evidence/conditions-sets-084.md#c-d9b21c69110ab307) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-013587

```text
(exec)# do-exec clear vtp counters <cr>
```

Handler ` RVA 0x15C834F0 `；selector ` 0 `；EOL ` RVA 0x35DFEE18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-012472

```text
(exec)# do-exec clear wccp <cr>
```

Handler ` RVA 0x10AD8640 `；selector ` 0 `；EOL ` RVA 0x34C9A4C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-19d5ef4571d0de23](../../evidence/conditions-sets-010.md#c-19d5ef4571d0de23) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-b0ff6d57b06f3ae8](../../evidence/state_effects-sets-037.md#s-b0ff6d57b06f3ae8)

### path-018456

```text
(exec)# do-exec clear wsma agent counters <cr>
```

Handler ` RVA 0xF3EA130 `；selector ` 0 `；EOL ` RVA 0x3463CCB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-018450

```text
(exec)# do-exec clear wsma profile counters <cr>
```

Handler ` RVA 0xF3D60D0 `；selector ` 0 `；EOL ` RVA 0x3462E8F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-baa315d5e785ec24](../../evidence/state_effects-sets-039.md#s-baa315d5e785ec24)

### path-018626

```text
(exec)# do-exec clear xmpp profile counters <cr>
```

Handler ` RVA 0x12618AD0 `；selector ` 0 `；EOL ` RVA 0x358C6EF0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-1c8dabf76dc5ed92](../../evidence/state_effects-sets-007.md#s-1c8dabf76dc5ed92)

### path-025043

```text
(exec)# do-exec clear xot remote <address> <number:1..65535> local <address> <number:1..65535> <cr>
```

Handler ` RVA 0x105F21C0 `；selector ` 1 `；EOL ` RVA 0x34BC4C88 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` host IP address；` unsigned_number ` port number；` address ` host IP address；` unsigned_number ` port number。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-9f1afb08a24b6a09](../../evidence/parameters-sets-012.md#p-9f1afb08a24b6a09) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-012384

```text
(exec)# do-exec clock read-calendar <cr>
```

Handler ` RVA 0xD70DA20 `；selector ` 0 `；EOL ` RVA 0x34173EF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-10ad613b42265698](../../evidence/conditions-sets-007.md#c-10ad613b42265698) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-012388

```text
(exec)# do-exec clock update-calendar <cr>
```

Handler ` RVA 0xD70DC00 `；selector ` 0 `；EOL ` RVA 0x341741A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-10ad613b42265698](../../evidence/conditions-sets-007.md#c-10ad613b42265698) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-017735

```text
(exec)# do-exec cns config cancel <number:1..4294967295> <cr>
```

Handler ` RVA 0xF319830 `；selector ` 3 `；EOL ` RVA 0x34608BF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` the queue identifier of the configuration。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-6cbc1dc0016dfbe6](../../evidence/parameters-sets-009.md#p-6cbc1dc0016dfbe6) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-017979

```text
(exec)# do-exec cns config retrieve <string> <cr>
```

Handler ` RVA 0xF31C1E0 `；selector ` 4 `；EOL ` RVA 0x34609570 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Host name or address of configuration server。

[条件 C-b2360e38ea4e4f25](../../evidence/conditions-sets-069.md#c-b2360e38ea4e4f25) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-6c0ba6c7b99b146e](../../evidence/parameters-sets-009.md#p-6c0ba6c7b99b146e) · [状态效果 S-7805814d96cb2f34](../../evidence/state_effects-sets-025.md#s-7805814d96cb2f34)

### path-013804

```text
(exec)# do-exec cns image retrieve <cr>
```

Handler ` RVA 0xF36DB10 `；selector ` 1 `；EOL ` RVA 0x3461B140 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-012239

```text
(exec)# do-exec configure <cr>
```

Handler ` RVA 0xDFE7770 `；selector ` 0 `；EOL ` RVA 0x340D23F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5239e03e0e4988f4](../../evidence/conditions-sets-032.md#c-5239e03e0e4988f4) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-012957

```text
(exec)# do-exec configure check syntax <cr>
```

Handler ` RVA 0xDFE7770 `；selector ` 8 `；EOL ` RVA 0x340D4558 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-671f089f7288c437](../../evidence/conditions-sets-040.md#c-671f089f7288c437) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-012360

```text
(exec)# do-exec configure confirm <cr>
```

Handler ` RVA 0xDFE7770 `；selector ` 9 `；EOL ` RVA 0x340D3598 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-98f7f0ab1a0d2624](../../evidence/conditions-sets-059.md#c-98f7f0ab1a0d2624) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-85263cc7211def63](../../evidence/state_effects-sets-028.md#s-85263cc7211def63)

### path-012342

```text
(exec)# do-exec configure http <cr>
```

Handler ` RVA 0xDFE7770 `；selector ` 6 `；EOL ` RVA 0x340D26D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-98f7f0ab1a0d2624](../../evidence/conditions-sets-059.md#c-98f7f0ab1a0d2624) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-012351

```text
(exec)# do-exec configure memory <cr>
```

Handler ` RVA 0xDFE7770 `；selector ` 2 `；EOL ` RVA 0x340D29E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5bfa28f498df8ed5](../../evidence/conditions-sets-036.md#c-5bfa28f498df8ed5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-012973

```text
(exec)# do-exec configure revert now <cr>
```

Handler ` RVA 0xDFE7770 `；selector ` 11 `；EOL ` RVA 0x340D39B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-98f7f0ab1a0d2624](../../evidence/conditions-sets-059.md#c-98f7f0ab1a0d2624) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-016904

```text
(exec)# do-exec configure revert timer <number:1..120> <cr>
```

Handler ` RVA 0xDFE7770 `；selector ` 10 `；EOL ` RVA 0x340D3D18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` New timer value in minutes。

[条件 C-98f7f0ab1a0d2624](../../evidence/conditions-sets-059.md#c-98f7f0ab1a0d2624) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-c1d1eee87db7ea91](../../evidence/parameters-sets-015.md#p-c1d1eee87db7ea91) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-012505

```text
(exec)# do-exec controller-mode disable <cr>
```

Handler ` RVA 0xC6B1B90 `；selector ` 0 `；EOL ` RVA 0x33AD1FF0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-17f0feb6e41ab18e](../../evidence/conditions-sets-009.md#c-17f0feb6e41ab18e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-012503

```text
(exec)# do-exec controller-mode enable <cr>
```

Handler ` RVA 0xC6B1A10 `；selector ` 0 `；EOL ` RVA 0x33AD1D48 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-17f0feb6e41ab18e](../../evidence/conditions-sets-009.md#c-17f0feb6e41ab18e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-012509

```text
(exec)# do-exec controller-mode reset <cr>
```

Handler ` RVA 0xC6B19C0 `；selector ` 0 `；EOL ` RVA 0x33AD2298 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-17f0feb6e41ab18e](../../evidence/conditions-sets-009.md#c-17f0feb6e41ab18e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-017667

```text
(exec)# do-exec crypto key benchmark rsa <cr>
```

Handler ` RVA 0x12134420 `；selector ` 0 `；EOL ` RVA 0x35839208 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-025145

```text
(exec)# do-exec crypto key export ec <string> pem terminal 3des <string> <cr>
```

Handler ` RVA 0x123A44C0 `；selector ` 0 `；EOL ` RVA 0x3583B070 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` ec key label；` string ` Passphrase used to protect the private key。

[条件 C-ed204923cea56fea](../../evidence/conditions-sets-092.md#c-ed204923cea56fea) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-2fd90096cf5a9b80](../../evidence/parameters-sets-004.md#p-2fd90096cf5a9b80) · [状态效果 S-f36d37e4f3f6e8f7](../../evidence/state_effects-sets-051.md#s-f36d37e4f3f6e8f7)

### path-025143

```text
(exec)# do-exec crypto key export rsa <string> pem terminal 3des <string> <cr>
```

Handler ` RVA 0x123A44C0 `；selector ` 0 `；EOL ` RVA 0x3583AA90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` RSA key label；` string ` Passphrase used to protect the private key。

[条件 C-bc3acacf7e2290f3](../../evidence/conditions-sets-073.md#c-bc3acacf7e2290f3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-620a7ff7aea3bd36](../../evidence/parameters-sets-008.md#p-620a7ff7aea3bd36) · [状态效果 S-f4f55e04a0ff9191](../../evidence/state_effects-sets-052.md#s-f4f55e04a0ff9191)

### path-023845

```text
(exec)# do-exec crypto key generate ec keysize <number:256..256> <cr>
```

Handler ` RVA 0x123A9250 `；selector ` 18 `；EOL ` RVA 0x35839FE8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` 256 bit keys。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-418f0a6cc28e2ea1](../../evidence/parameters-sets-006.md#p-418f0a6cc28e2ea1) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-017709

```text
(exec)# do-exec crypto key generate rsa <cr>
```

Handler ` RVA 0x123A96D0 `；selector ` 2 `；EOL ` RVA 0x35839BB0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b3857b40abcfea88](../../evidence/conditions-sets-069.md#c-b3857b40abcfea88) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023904

```text
(exec)# do-exec crypto key import ec <string> terminal <cr>
```

Handler ` RVA 0x123A44C0 `；selector ` 0 `；EOL ` RVA 0x3583BFB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` EC key label。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-8a36ed0e2a693e42](../../evidence/parameters-sets-011.md#p-8a36ed0e2a693e42) · [状态效果 S-343ea5e68a0cb9e8](../../evidence/state_effects-sets-012.md#s-343ea5e68a0cb9e8)

### path-023924

```text
(exec)# do-exec crypto key import rsa <string> terminal <cr>
```

Handler ` RVA 0x123A44C0 `；selector ` 0 `；EOL ` RVA 0x3583BB28 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` RSA key label。

[条件 C-9353ad59caf555cb](../../evidence/conditions-sets-057.md#c-9353ad59caf555cb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-e38d172fc8953679](../../evidence/parameters-sets-017.md#p-e38d172fc8953679) · [状态效果 S-f7ea4a66f2973a61](../../evidence/state_effects-sets-052.md#s-f7ea4a66f2973a61)

### path-017731

```text
(exec)# do-exec crypto key lock rsa <cr>
```

Handler ` RVA 0x123A4840 `；selector ` 0 `；EOL ` RVA 0x3583C490 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-cdc73475856c4950](../../evidence/state_effects-sets-044.md#s-cdc73475856c4950)

### path-017752

```text
(exec)# do-exec crypto key unlock rsa <cr>
```

Handler ` RVA 0x123A4840 `；selector ` 1 `；EOL ` RVA 0x3583C940 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-0e6a230dd112da16](../../evidence/state_effects-sets-003.md#s-0e6a230dd112da16)

### path-013736

```text
(exec)# do-exec crypto key zeroize <cr>
```

Handler ` RVA 0x123A4370 `；selector ` 0 `；EOL ` RVA 0x3583A470 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-365031a1f27cf9ed](../../evidence/state_effects-sets-012.md#s-365031a1f27cf9ed)

### path-017662

```text
(exec)# do-exec crypto pki authenticate <string> <cr>
```

Handler ` RVA 0x11F203B0 `；selector ` 1 `；EOL ` RVA 0x35753B58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` CA Server Name。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-54ea9cac6bfc4291](../../evidence/parameters-sets-007.md#p-54ea9cac6bfc4291) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021707

```text
(exec)# do-exec crypto pki benchmark start <number:0..9990> <cr>
```

Handler ` RVA 0x11F3DA00 `；selector ` 0 `；EOL ` RVA 0x357555E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Collection limit。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-38923874e1a26c51](../../evidence/parameters-sets-005.md#p-38923874e1a26c51) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-017759

```text
(exec)# do-exec crypto pki benchmark stop <cr>
```

Handler ` RVA 0x11F3D9B0 `；selector ` 0 `；EOL ` RVA 0x35755888 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021638

```text
(exec)# do-exec crypto pki certificate clear <string> <cr>
```

Handler ` RVA 0x11F203B0 `；selector ` 37 `；EOL ` RVA 0x35754720 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` trust point。

[条件 C-4e95a7d56674db38](../../evidence/conditions-sets-031.md#c-4e95a7d56674db38) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-7af60f959eac61af](../../evidence/parameters-sets-010.md#p-7af60f959eac61af) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021604

```text
(exec)# do-exec crypto pki certificate validate <string> <cr>
```

Handler ` RVA 0x11F19FB0 `；selector ` 36 `；EOL ` RVA 0x35754420 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` trust point。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-f4181397cdea960d](../../evidence/parameters-sets-018.md#p-f4181397cdea960d) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-017611

```text
(exec)# do-exec crypto pki crl refresh-cache <cr>
```

Handler ` RVA 0x11F32FE0 `；selector ` 0 `；EOL ` RVA 0x35753508 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021570

```text
(exec)# do-exec crypto pki crl request <string> <cr>
```

Handler ` RVA 0x11F19FB0 `；selector ` 17 `；EOL ` RVA 0x357537F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` CA Server Name。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-dc6c271ba16503af](../../evidence/parameters-sets-017.md#p-dc6c271ba16503af) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-017653

```text
(exec)# do-exec crypto pki enroll <string> <cr>
```

Handler ` RVA 0x11F203B0 `；selector ` 15 `；EOL ` RVA 0x357540D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` CA Server Name。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-3d39673253a3dd73](../../evidence/parameters-sets-005.md#p-3d39673253a3dd73) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021643

```text
(exec)# do-exec crypto pki import <string> certificate <cr>
```

Handler ` RVA 0x11F19FB0 `；selector ` 16 `；EOL ` RVA 0x35754DF0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Trustpoint label to associate certificate or pkcs-12 file with。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-23db83b805e2cb83](../../evidence/parameters-sets-003.md#p-23db83b805e2cb83) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023938

```text
(exec)# do-exec crypto pki server <string> grant <number:1..999> <cr>
```

Handler ` RVA 0xBBBCD30 `；selector ` 83 `；EOL ` RVA 0x3386E610 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Certificate Server Name；` unsigned_number ` Request ID。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-fb290df102034538](../../evidence/parameters-sets-019.md#p-fb290df102034538) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023928

```text
(exec)# do-exec crypto pki server <string> grant all <cr>
```

Handler ` RVA 0xBBBCD30 `；selector ` 82 `；EOL ` RVA 0x3386E368 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Certificate Server Name。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-c62cb402b082848f](../../evidence/parameters-sets-015.md#p-c62cb402b082848f) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023953

```text
(exec)# do-exec crypto pki server <string> password generate <cr>
```

Handler ` RVA 0xBBBCD30 `；selector ` 88 `；EOL ` RVA 0x3386F4C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Certificate Server Name。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-c62cb402b082848f](../../evidence/parameters-sets-015.md#p-c62cb402b082848f) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024754

```text
(exec)# do-exec crypto pki server <string> password generate <number:1..1440> <cr>
```

Handler ` RVA 0xBBBCD30 `；selector ` 89 `；EOL ` RVA 0x3386F4A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Certificate Server Name；` unsigned_number ` Validity time in minutes。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-f1e63bb67ec3fb64](../../evidence/parameters-sets-018.md#p-f1e63bb67ec3fb64) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023945

```text
(exec)# do-exec crypto pki server <string> reject <number:1..999> <cr>
```

Handler ` RVA 0xBBBCD30 `；selector ` 85 `；EOL ` RVA 0x3386EBB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Certificate Server Name；` unsigned_number ` Request ID。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-a4361076d0fd1464](../../evidence/parameters-sets-013.md#p-a4361076d0fd1464) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023936

```text
(exec)# do-exec crypto pki server <string> reject all <cr>
```

Handler ` RVA 0xBBBCD30 `；selector ` 84 `；EOL ` RVA 0x3386E910 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Certificate Server Name。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-c62cb402b082848f](../../evidence/parameters-sets-015.md#p-c62cb402b082848f) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023949

```text
(exec)# do-exec crypto pki server <string> remove <number:1..999> <cr>
```

Handler ` RVA 0xBBBCD30 `；selector ` 87 `；EOL ` RVA 0x3386F160 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Certificate Server Name；` unsigned_number ` Request ID。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-fc436da5623bd268](../../evidence/parameters-sets-019.md#p-fc436da5623bd268) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023944

```text
(exec)# do-exec crypto pki server <string> remove all <cr>
```

Handler ` RVA 0xBBBCD30 `；selector ` 86 `；EOL ` RVA 0x3386EEB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Certificate Server Name。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-c62cb402b082848f](../../evidence/parameters-sets-015.md#p-c62cb402b082848f) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023951

```text
(exec)# do-exec crypto pki server <string> revoke <number:1..2147483647> <cr>
```

Handler ` RVA 0xBBBCD30 `；selector ` 90 `；EOL ` RVA 0x3386FA08 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Certificate Server Name；` unsigned_number ` Serial Number in Hexadecimal.。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-b88c73cbf649e417](../../evidence/parameters-sets-014.md#p-b88c73cbf649e417) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021699

```text
(exec)# do-exec crypto pki server <string> start <cr>
```

Handler ` RVA 0xBBBCD30 `；selector ` 53 `；EOL ` RVA 0x3386DFF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Certificate Server Name。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-c62cb402b082848f](../../evidence/parameters-sets-015.md#p-c62cb402b082848f) · [状态效果 S-1bcea38886e08132](../../evidence/state_effects-sets-006.md#s-1bcea38886e08132)

### path-023955

```text
(exec)# do-exec crypto pki server <string> unrevoke <number:1..2147483647> <cr>
```

Handler ` RVA 0xBBBCD30 `；selector ` 91 `；EOL ` RVA 0x3386FCF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Certificate Server Name；` unsigned_number ` Certificate serial number in Hex。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-a136ae8bfab62529](../../evidence/parameters-sets-012.md#p-a136ae8bfab62529) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-013651

```text
(exec)# do-exec ct-isdn delay <number:100..1000000> <cr>
```

Handler ` RVA 0x1E095BE0 `；selector ` 5 `；EOL ` RVA 0x378C14F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Time Delay in Milliseconds。

[条件 C-e45565c6d226b1d3](../../evidence/conditions-sets-088.md#c-e45565c6d226b1d3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-1208637761736633](../../evidence/parameters-sets-002.md#p-1208637761736633) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-013710

```text
(exec)# do-exec ct-isdn start overlap <cr>
```

Handler ` RVA 0x1E095BE0 `；selector ` 1 `；EOL ` RVA 0x378C2D90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e45565c6d226b1d3](../../evidence/conditions-sets-088.md#c-e45565c6d226b1d3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-e8394e3046e47f18](../../evidence/state_effects-sets-049.md#s-e8394e3046e47f18)

### path-012513

```text
(exec)# do-exec ct-isdn test-end <cr>
```

Handler ` RVA 0x1E095BE0 `；selector ` 2 `；EOL ` RVA 0x378C3088 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e45565c6d226b1d3](../../evidence/conditions-sets-088.md#c-e45565c6d226b1d3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023852

```text
(exec)# do-exec cts credentials id <string> password <string> <cr>
```

Handler ` RVA 0x1304C510 `；selector ` 5 `；EOL ` RVA 0x35A14858 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` the CTS device ID for this switch or router(upto 32 char)；` string ` this device's CTS password(upto 24 char)。

[条件 C-d431a1b34614e672](../../evidence/conditions-sets-082.md#c-d431a1b34614e672) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-279f0f16904264c0](../../evidence/parameters-sets-003.md#p-279f0f16904264c0) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-013696

```text
(exec)# do-exec cts refresh environment-data <cr>
```

Handler ` RVA 0x1304C510 `；selector ` 3 `；EOL ` RVA 0x35A13778 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-91ddf5eadc294583](../../evidence/conditions-sets-056.md#c-91ddf5eadc294583) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-013712

```text
(exec)# do-exec cts refresh pac <cr>
```

Handler ` RVA 0x1304C510 `；selector ` 4 `；EOL ` RVA 0x35A13A20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-91ddf5eadc294583](../../evidence/conditions-sets-056.md#c-91ddf5eadc294583) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-013734

```text
(exec)# do-exec cts refresh policy <cr>
```

Handler ` RVA 0x1304C510 `；selector ` 0 `；EOL ` RVA 0x35A13168 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4831d39faaf3ef50](../../evidence/conditions-sets-028.md#c-4831d39faaf3ef50) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-017681

```text
(exec)# do-exec cts refresh policy peer <cr>
```

Handler ` RVA 0x1304C510 `；selector ` 1 `；EOL ` RVA 0x35A12EC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4831d39faaf3ef50](../../evidence/conditions-sets-028.md#c-4831d39faaf3ef50) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-017732

```text
(exec)# do-exec cts refresh policy sgt <cr>
```

Handler ` RVA 0x1304C510 `；selector ` 2 `；EOL ` RVA 0x35A131E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4831d39faaf3ef50](../../evidence/conditions-sets-028.md#c-4831d39faaf3ef50) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-0c2dc01adcfe62f9](../../evidence/state_effects-sets-003.md#s-0c2dc01adcfe62f9)

### path-025213

```text
(exec)# do-exec cts role-based policy trace ipv4 ip host <address> host <address> <cr>
```

Handler ` RVA 0x141F6D00 `；selector ` 0 `；EOL ` RVA 0x35CFDAF0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Source address；` address ` Destination Address。

[条件 C-2c253a002911cd60](../../evidence/conditions-sets-017.md#c-2c253a002911cd60) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-d23317032fa3ed74](../../evidence/parameters-sets-016.md#p-d23317032fa3ed74) · [状态效果 S-467678ed2e367f81](../../evidence/state_effects-sets-015.md#s-467678ed2e367f81)

### path-012214

```text
(exec)# do-exec debug <cr>
```

Handler ` RVA 0xE006320 `；selector ` 0 `；EOL ` RVA 0x341207D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-cc6dc89545a92ace](../../evidence/conditions-sets-079.md#c-cc6dc89545a92ace) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d4a8f2431a7dc91e](../../evidence/state_effects-sets-045.md#s-d4a8f2431a7dc91e)

### path-012869

```text
(exec)# do-exec debug ACM all <cr>
```

Handler ` RVA 0xDEDBDB0 `；selector ` 0 `；EOL ` RVA 0x34096D30 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-9092343efd5b8385](../../evidence/state_effects-sets-031.md#s-9092343efd5b8385)

### path-012851

```text
(exec)# do-exec debug ACM error <cr>
```

Handler ` RVA 0xDEDBD60 `；selector ` 1 `；EOL ` RVA 0x340967E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-9092343efd5b8385](../../evidence/state_effects-sets-031.md#s-9092343efd5b8385)

### path-012865

```text
(exec)# do-exec debug ACM event <cr>
```

Handler ` RVA 0xDEDBD60 `；selector ` 0 `；EOL ` RVA 0x34096A88 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-9092343efd5b8385](../../evidence/state_effects-sets-031.md#s-9092343efd5b8385)

### path-015730

```text
(exec)# do-exec debug LDAP all <cr>
```

Handler ` RVA 0x11AC30E0 `；selector ` 0 `；EOL ` RVA 0x3560CAB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-cf89f578260cf64e](../../evidence/conditions-sets-080.md#c-cf89f578260cf64e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-25b19d64ad2642ef](../../evidence/state_effects-sets-008.md#s-25b19d64ad2642ef)

### path-015692

```text
(exec)# do-exec debug LDAP error <cr>
```

Handler ` RVA 0xDD48D90 `；selector ` 1 `；EOL ` RVA 0x3560C2C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-cf89f578260cf64e](../../evidence/conditions-sets-080.md#c-cf89f578260cf64e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-25b19d64ad2642ef](../../evidence/state_effects-sets-008.md#s-25b19d64ad2642ef)

### path-015708

```text
(exec)# do-exec debug LDAP event <cr>
```

Handler ` RVA 0xDD48D90 `；selector ` 0 `；EOL ` RVA 0x3560C568 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-cf89f578260cf64e](../../evidence/conditions-sets-080.md#c-cf89f578260cf64e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-25b19d64ad2642ef](../../evidence/state_effects-sets-008.md#s-25b19d64ad2642ef)

### path-015722

```text
(exec)# do-exec debug LDAP legacy <cr>
```

Handler ` RVA 0xE002120 `；selector ` 3 `；EOL ` RVA 0x3560C810 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-cf89f578260cf64e](../../evidence/conditions-sets-080.md#c-cf89f578260cf64e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-25b19d64ad2642ef](../../evidence/state_effects-sets-008.md#s-25b19d64ad2642ef)

### path-015674

```text
(exec)# do-exec debug LDAP packet <cr>
```

Handler ` RVA 0xDD48D90 `；selector ` 2 `；EOL ` RVA 0x3560C018 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-cf89f578260cf64e](../../evidence/conditions-sets-080.md#c-cf89f578260cf64e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-25b19d64ad2642ef](../../evidence/state_effects-sets-008.md#s-25b19d64ad2642ef)

### path-013037

```text
(exec)# do-exec debug aaa accounting <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 16 `；EOL ` RVA 0x341B80C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-ae033786ffdac101](../../evidence/state_effects-sets-037.md#s-ae033786ffdac101)

### path-013058

```text
(exec)# do-exec debug aaa administrative <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 17 `；EOL ` RVA 0x341B8368 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-ae033786ffdac101](../../evidence/state_effects-sets-037.md#s-ae033786ffdac101)

### path-013399

```text
(exec)# do-exec debug aaa api <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 35 `；EOL ` RVA 0x341BC6A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-ae033786ffdac101](../../evidence/state_effects-sets-037.md#s-ae033786ffdac101)

### path-017223

```text
(exec)# do-exec debug aaa api attr <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 36 `；EOL ` RVA 0x341BC680 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-ae033786ffdac101](../../evidence/state_effects-sets-037.md#s-ae033786ffdac101)

### path-013373

```text
(exec)# do-exec debug aaa attr <cr>
```

Handler ` RVA 0xDD3A410 `；selector ` 26 `；EOL ` RVA 0x341BB120 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-ae033786ffdac101](../../evidence/state_effects-sets-037.md#s-ae033786ffdac101)

### path-017171

```text
(exec)# do-exec debug aaa attr add <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 30 `；EOL ` RVA 0x341BABA8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-ae033786ffdac101](../../evidence/state_effects-sets-037.md#s-ae033786ffdac101)

### path-017153

```text
(exec)# do-exec debug aaa attr alloc-free <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 31 `；EOL ` RVA 0x341BA900 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-ae033786ffdac101](../../evidence/state_effects-sets-037.md#s-ae033786ffdac101)

### path-017132

```text
(exec)# do-exec debug aaa attr error <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 32 `；EOL ` RVA 0x341BA658 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-ae033786ffdac101](../../evidence/state_effects-sets-037.md#s-ae033786ffdac101)

### path-017112

```text
(exec)# do-exec debug aaa attr handle <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 27 `；EOL ` RVA 0x341BA3B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-ae033786ffdac101](../../evidence/state_effects-sets-037.md#s-ae033786ffdac101)

### path-017205

```text
(exec)# do-exec debug aaa attr info <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 28 `；EOL ` RVA 0x341BB0F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-ae033786ffdac101](../../evidence/state_effects-sets-037.md#s-ae033786ffdac101)

### path-017187

```text
(exec)# do-exec debug aaa attr update <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 29 `；EOL ` RVA 0x341BAE50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-ae033786ffdac101](../../evidence/state_effects-sets-037.md#s-ae033786ffdac101)

### path-012998

```text
(exec)# do-exec debug aaa authentication <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 12 `；EOL ` RVA 0x341B7B70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-ae033786ffdac101](../../evidence/state_effects-sets-037.md#s-ae033786ffdac101)

### path-013018

```text
(exec)# do-exec debug aaa authorization <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 15 `；EOL ` RVA 0x341B7E18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-ae033786ffdac101](../../evidence/state_effects-sets-037.md#s-ae033786ffdac101)

### path-013079

```text
(exec)# do-exec debug aaa boundary <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 56 `；EOL ` RVA 0x341B8610 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-ae033786ffdac101](../../evidence/state_effects-sets-037.md#s-ae033786ffdac101)

### path-016865

```text
(exec)# do-exec debug aaa cache filterserver <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 50 `；EOL ` RVA 0x341B7040 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-ae033786ffdac101](../../evidence/state_effects-sets-037.md#s-ae033786ffdac101)

### path-016881

```text
(exec)# do-exec debug aaa cache group <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 51 `；EOL ` RVA 0x341B72E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-ae033786ffdac101](../../evidence/state_effects-sets-037.md#s-ae033786ffdac101)

### path-013101

```text
(exec)# do-exec debug aaa cca <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 57 `；EOL ` RVA 0x341B88B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-ae033786ffdac101](../../evidence/state_effects-sets-037.md#s-ae033786ffdac101)

### path-013208

```text
(exec)# do-exec debug aaa coa <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 25 `；EOL ` RVA 0x341B98A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-ae033786ffdac101](../../evidence/state_effects-sets-037.md#s-ae033786ffdac101)

### path-013475

```text
(exec)# do-exec debug aaa common-criteria <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 55 `；EOL ` RVA 0x341BD9A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-736155d58fe4eb36](../../evidence/conditions-sets-045.md#c-736155d58fe4eb36) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-ae033786ffdac101](../../evidence/state_effects-sets-037.md#s-ae033786ffdac101)

### path-013319

```text
(exec)# do-exec debug aaa db <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 38 `；EOL ` RVA 0x341BBB78 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-ae033786ffdac101](../../evidence/state_effects-sets-037.md#s-ae033786ffdac101)

### path-017258

```text
(exec)# do-exec debug aaa dead-criteria transaction <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 42 `；EOL ` RVA 0x341BD188 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-ae033786ffdac101](../../evidence/state_effects-sets-037.md#s-ae033786ffdac101)

### path-013493

```text
(exec)# do-exec debug aaa green <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 69 `；EOL ` RVA 0x341BDC90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-7b9cc801d12679b1](../../evidence/conditions-sets-048.md#c-7b9cc801d12679b1) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-ae033786ffdac101](../../evidence/state_effects-sets-037.md#s-ae033786ffdac101)

### path-013352

```text
(exec)# do-exec debug aaa id <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 37 `；EOL ` RVA 0x341BC0C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-ae033786ffdac101](../../evidence/state_effects-sets-037.md#s-ae033786ffdac101)

### path-013289

```text
(exec)# do-exec debug aaa ipc <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 33 `；EOL ` RVA 0x341BB628 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-ae033786ffdac101](../../evidence/state_effects-sets-037.md#s-ae033786ffdac101)

### path-013256

```text
(exec)# do-exec debug aaa memory <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 13 `；EOL ` RVA 0x341BA0A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-ae033786ffdac101](../../evidence/state_effects-sets-037.md#s-ae033786ffdac101)

### path-013149

```text
(exec)# do-exec debug aaa mlist-ref-count <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 44 `；EOL ` RVA 0x341B8E08 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-ae033786ffdac101](../../evidence/state_effects-sets-037.md#s-ae033786ffdac101)

### path-013439

```text
(exec)# do-exec debug aaa mlist-state <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 45 `；EOL ` RVA 0x341BD6C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-ae033786ffdac101](../../evidence/state_effects-sets-037.md#s-ae033786ffdac101)

### path-013190

```text
(exec)# do-exec debug aaa per-user <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 18 `；EOL ` RVA 0x341B9600 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-ae033786ffdac101](../../evidence/state_effects-sets-037.md#s-ae033786ffdac101)

### path-013223

```text
(exec)# do-exec debug aaa pod <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 24 `；EOL ` RVA 0x341B9B50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-ae033786ffdac101](../../evidence/state_effects-sets-037.md#s-ae033786ffdac101)

### path-016888

```text
(exec)# do-exec debug aaa profile db <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 52 `；EOL ` RVA 0x341B78E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-ae033786ffdac101](../../evidence/state_effects-sets-037.md#s-ae033786ffdac101)

### path-017242

```text
(exec)# do-exec debug aaa protocol local <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 40 `；EOL ` RVA 0x341BCBE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-ae033786ffdac101](../../evidence/state_effects-sets-037.md#s-ae033786ffdac101)

### path-017261

```text
(exec)# do-exec debug aaa protocol radius <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 41 `；EOL ` RVA 0x341BCE88 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-ae033786ffdac101](../../evidence/state_effects-sets-037.md#s-ae033786ffdac101)

### path-013240

```text
(exec)# do-exec debug aaa proxy <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 23 `；EOL ` RVA 0x341B9DF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-ae033786ffdac101](../../evidence/state_effects-sets-037.md#s-ae033786ffdac101)

### path-013494

```text
(exec)# do-exec debug aaa redundancy <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 54 `；EOL ` RVA 0x341BDF38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-1dd35935f0eb2c5e](../../evidence/conditions-sets-012.md#c-1dd35935f0eb2c5e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-ae033786ffdac101](../../evidence/state_effects-sets-037.md#s-ae033786ffdac101)

### path-013178

```text
(exec)# do-exec debug aaa server-ref-count <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 46 `；EOL ` RVA 0x341B9358 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-ae033786ffdac101](../../evidence/state_effects-sets-037.md#s-ae033786ffdac101)

### path-013163

```text
(exec)# do-exec debug aaa sg-ref-count <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 47 `；EOL ` RVA 0x341B90B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-ae033786ffdac101](../../evidence/state_effects-sets-037.md#s-ae033786ffdac101)

### path-013128

```text
(exec)# do-exec debug aaa sg-server-selection <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 48 `；EOL ` RVA 0x341B8B60 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-ae033786ffdac101](../../evidence/state_effects-sets-037.md#s-ae033786ffdac101)

### path-016876

```text
(exec)# do-exec debug aaa subscriber profile <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 53 `；EOL ` RVA 0x341B75E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-ae033786ffdac101](../../evidence/state_effects-sets-037.md#s-ae033786ffdac101)

### path-013303

```text
(exec)# do-exec debug aaa subsys <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 34 `；EOL ` RVA 0x341BB8D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-ae033786ffdac101](../../evidence/state_effects-sets-037.md#s-ae033786ffdac101)

### path-013426

```text
(exec)# do-exec debug aaa testing <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 43 `；EOL ` RVA 0x341BD418 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-ae033786ffdac101](../../evidence/state_effects-sets-037.md#s-ae033786ffdac101)

### path-016877

```text
(exec)# do-exec debug aaa tools memleak <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x35C0DA90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-c2fbafa2fe2f3980](../../evidence/state_effects-sets-041.md#s-c2fbafa2fe2f3980)

### path-013367

```text
(exec)# do-exec debug aaa traceback <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 14 `；EOL ` RVA 0x341BC370 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-ae033786ffdac101](../../evidence/state_effects-sets-037.md#s-ae033786ffdac101)

### path-013340

```text
(exec)# do-exec debug aaa userdb <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 39 `；EOL ` RVA 0x341BBE20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-ae033786ffdac101](../../evidence/state_effects-sets-037.md#s-ae033786ffdac101)

### path-012739

```text
(exec)# do-exec debug access-expression <cr>
```

Handler ` RVA 0xF2A3970 `；selector ` 0 `；EOL ` RVA 0x345E4A20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-54007509098b0b56](../../evidence/state_effects-sets-018.md#s-54007509098b0b56)

### path-015932

```text
(exec)# do-exec debug access-session all <cr>
```

Handler ` RVA 0xCAFB1B0 `；selector ` 4 `；EOL ` RVA 0x33BAEA50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-70f5c28bd3422961](../../evidence/conditions-sets-044.md#c-70f5c28bd3422961) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-efb0e5d04aa8666e](../../evidence/state_effects-sets-051.md#s-efb0e5d04aa8666e)

### path-015923

```text
(exec)# do-exec debug access-session detail <cr>
```

Handler ` RVA 0xCAFB1B0 `；selector ` 2 `；EOL ` RVA 0x33BAE7A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-70f5c28bd3422961](../../evidence/conditions-sets-044.md#c-70f5c28bd3422961) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-efb0e5d04aa8666e](../../evidence/state_effects-sets-051.md#s-efb0e5d04aa8666e)

### path-015903

```text
(exec)# do-exec debug access-session errors <cr>
```

Handler ` RVA 0xCAFB1B0 `；selector ` 0 `；EOL ` RVA 0x33BAE258 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-70f5c28bd3422961](../../evidence/conditions-sets-044.md#c-70f5c28bd3422961) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-efb0e5d04aa8666e](../../evidence/state_effects-sets-051.md#s-efb0e5d04aa8666e)

### path-015913

```text
(exec)# do-exec debug access-session events <cr>
```

Handler ` RVA 0xCAFB1B0 `；selector ` 1 `；EOL ` RVA 0x33BAE500 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-70f5c28bd3422961](../../evidence/conditions-sets-044.md#c-70f5c28bd3422961) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-efb0e5d04aa8666e](../../evidence/state_effects-sets-051.md#s-efb0e5d04aa8666e)

### path-020080

```text
(exec)# do-exec debug access-session feature all <cr>
```

Handler ` RVA 0xCAFB1B0 `；selector ` 5 `；EOL ` RVA 0x33BAF118 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-70f5c28bd3422961](../../evidence/conditions-sets-044.md#c-70f5c28bd3422961) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-efb0e5d04aa8666e](../../evidence/state_effects-sets-051.md#s-efb0e5d04aa8666e)

### path-020164

```text
(exec)# do-exec debug access-session rcl_server all <cr>
```

Handler ` RVA 0xCAF9B10 `；selector ` 3 `；EOL ` RVA 0x33BAD888 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-4ada8cd97f152e6b](../../evidence/conditions-sets-029.md#c-4ada8cd97f152e6b) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-12b638cb137bd27f](../../evidence/state_effects-sets-004.md#s-12b638cb137bd27f)

### path-020157

```text
(exec)# do-exec debug access-session rcl_server detail <cr>
```

Handler ` RVA 0xCAF9B10 `；selector ` 2 `；EOL ` RVA 0x33BAD5E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-4ada8cd97f152e6b](../../evidence/conditions-sets-029.md#c-4ada8cd97f152e6b) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-12b638cb137bd27f](../../evidence/state_effects-sets-004.md#s-12b638cb137bd27f)

### path-020148

```text
(exec)# do-exec debug access-session rcl_server error <cr>
```

Handler ` RVA 0xCAF9B10 `；selector ` 0 `；EOL ` RVA 0x33BAD338 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-4ada8cd97f152e6b](../../evidence/conditions-sets-029.md#c-4ada8cd97f152e6b) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-12b638cb137bd27f](../../evidence/state_effects-sets-004.md#s-12b638cb137bd27f)

### path-020141

```text
(exec)# do-exec debug access-session rcl_server event <cr>
```

Handler ` RVA 0xCAF9B10 `；selector ` 1 `；EOL ` RVA 0x33BAD090 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-4ada8cd97f152e6b](../../evidence/conditions-sets-029.md#c-4ada8cd97f152e6b) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-12b638cb137bd27f](../../evidence/state_effects-sets-004.md#s-12b638cb137bd27f)

### path-015950

```text
(exec)# do-exec debug access-session sync <cr>
```

Handler ` RVA 0xCAFB1B0 `；selector ` 3 `；EOL ` RVA 0x33BAED38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-4ada8cd97f152e6b](../../evidence/conditions-sets-029.md#c-4ada8cd97f152e6b) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-efb0e5d04aa8666e](../../evidence/state_effects-sets-051.md#s-efb0e5d04aa8666e)

### path-017880

```text
(exec)# do-exec debug acl cca error <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x3447D290 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-cc7dfcabbb85dcd1](../../evidence/state_effects-sets-043.md#s-cc7dfcabbb85dcd1)

### path-017905

```text
(exec)# do-exec debug acl cca event <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x3447D538 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-cc7dfcabbb85dcd1](../../evidence/state_effects-sets-043.md#s-cc7dfcabbb85dcd1)

### path-012501

```text
(exec)# do-exec debug adjacency <cr>
```

Handler ` RVA 0xB559CD0 `；selector ` 0 `；EOL ` RVA 0x3379B6B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-8a9b2d8773e3affa](../../evidence/conditions-sets-054.md#c-8a9b2d8773e3affa) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-8570c9a37783741c](../../evidence/state_effects-sets-028.md#s-8570c9a37783741c)

### path-013711

```text
(exec)# do-exec debug alg all <cr>
```

Handler ` RVA 0xCD3BF50 `；selector ` 1 `；EOL ` RVA 0x33CD4910 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-dd668de48e0a56ca](../../evidence/state_effects-sets-047.md#s-dd668de48e0a56ca)

### path-013757

```text
(exec)# do-exec debug alg info <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x33CD5108 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-dd668de48e0a56ca](../../evidence/state_effects-sets-047.md#s-dd668de48e0a56ca)

### path-013742

```text
(exec)# do-exec debug alg trace <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x33CD4E60 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-dd668de48e0a56ca](../../evidence/state_effects-sets-047.md#s-dd668de48e0a56ca)

### path-013726

```text
(exec)# do-exec debug alg warn <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x33CD4BB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-dd668de48e0a56ca](../../evidence/state_effects-sets-047.md#s-dd668de48e0a56ca)

### path-012287

```text
(exec)# do-exec debug all <cr>
```

Handler ` RVA 0xE002630 `；selector ` 0 `；EOL ` RVA 0x34121818 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d4a8f2431a7dc91e](../../evidence/state_effects-sets-045.md#s-d4a8f2431a7dc91e)

### path-020360

```text
(exec)# do-exec debug alps ascu event <cr>
```

Handler ` RVA 0x1121A510 `；selector ` 3 `；EOL ` RVA 0x3541C160 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-2211ad45186be3b2](../../evidence/conditions-sets-013.md#c-2211ad45186be3b2) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-e1c87f734d741ab0](../../evidence/state_effects-sets-048.md#s-e1c87f734d741ab0)

### path-020317

```text
(exec)# do-exec debug alps circuit event <cr>
```

Handler ` RVA 0x1121A510 `；selector ` 2 `；EOL ` RVA 0x3541BCD8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-46a4b5f8eb35afce](../../evidence/state_effects-sets-015.md#s-46a4b5f8eb35afce)

### path-020318

```text
(exec)# do-exec debug alps peer event <cr>
```

Handler ` RVA 0x1121A510 `；selector ` 1 `；EOL ` RVA 0x3541B960 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-8f9c0bc4a27466f0](../../evidence/state_effects-sets-030.md#s-8f9c0bc4a27466f0)

### path-016216

```text
(exec)# do-exec debug alps snmp <cr>
```

Handler ` RVA 0x1121A510 `；selector ` 4 `；EOL ` RVA 0x3541C6A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d4a8f2431a7dc91e](../../evidence/state_effects-sets-045.md#s-d4a8f2431a7dc91e)

### path-015437

```text
(exec)# do-exec debug analyze memory-leak <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x341F0BE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c16d737a1c9c2aca](../../evidence/conditions-sets-075.md#c-c16d737a1c9c2aca) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-9d1dc59ad47646b2](../../evidence/state_effects-sets-033.md#s-9d1dc59ad47646b2)

### path-013482

```text
(exec)# do-exec debug ancp adjacency <cr>
```

Handler ` RVA 0xB258990 `；selector ` 0 `；EOL ` RVA 0x336D7DA8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-f6ef456cedb8dd9b](../../evidence/state_effects-sets-052.md#s-f6ef456cedb8dd9b)

### path-015284

```text
(exec)# do-exec debug application db <cr>
```

Handler ` RVA 0x12810B70 `；selector ` 7 `；EOL ` RVA 0x358DCD80 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d4a8f2431a7dc91e](../../evidence/state_effects-sets-045.md#s-d4a8f2431a7dc91e)

### path-015301

```text
(exec)# do-exec debug application detail <cr>
```

Handler ` RVA 0x12810B70 `；selector ` 2 `；EOL ` RVA 0x358DD028 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d4a8f2431a7dc91e](../../evidence/state_effects-sets-045.md#s-d4a8f2431a7dc91e)

### path-015256

```text
(exec)# do-exec debug application event <cr>
```

Handler ` RVA 0x12810B70 `；selector ` 5 `；EOL ` RVA 0x358DC578 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d4a8f2431a7dc91e](../../evidence/state_effects-sets-045.md#s-d4a8f2431a7dc91e)

### path-015361

```text
(exec)# do-exec debug application ha <cr>
```

Handler ` RVA 0x12810B70 `；selector ` 8 `；EOL ` RVA 0x358DD660 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d4a8f2431a7dc91e](../../evidence/state_effects-sets-045.md#s-d4a8f2431a7dc91e)

### path-019652

```text
(exec)# do-exec debug application ha detail <cr>
```

Handler ` RVA 0x12810B70 `；selector ` 9 `；EOL ` RVA 0x358DD638 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d4a8f2431a7dc91e](../../evidence/state_effects-sets-045.md#s-d4a8f2431a7dc91e)

### path-022784

```text
(exec)# do-exec debug application route <address> <address> <cr>
```

Handler ` RVA 0x12810B70 `；selector ` 1 `；EOL ` RVA 0x358DD378 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

参数提示：` address ` Destination prefix；` address ` Destination prefix mask。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-3fadc80999e697ce](../../evidence/parameters-sets-005.md#p-3fadc80999e697ce) · [状态效果 S-d4a8f2431a7dc91e](../../evidence/state_effects-sets-045.md#s-d4a8f2431a7dc91e)

### path-015288

```text
(exec)# do-exec debug application rwatch <cr>
```

Handler ` RVA 0x12810B70 `；selector ` 3 `；EOL ` RVA 0x358DC8B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d4a8f2431a7dc91e](../../evidence/state_effects-sets-045.md#s-d4a8f2431a7dc91e)

### path-019603

```text
(exec)# do-exec debug application rwatch rib <cr>
```

Handler ` RVA 0x12810B70 `；selector ` 4 `；EOL ` RVA 0x358DC888 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d4a8f2431a7dc91e](../../evidence/state_effects-sets-045.md#s-d4a8f2431a7dc91e)

### path-015236

```text
(exec)# do-exec debug application summary <cr>
```

Handler ` RVA 0x12810B70 `；selector ` 6 `；EOL ` RVA 0x358DC2D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d4a8f2431a7dc91e](../../evidence/state_effects-sets-045.md#s-d4a8f2431a7dc91e)

### path-020156

```text
(exec)# do-exec debug archive config differences <cr>
```

Handler ` RVA 0xDEDE750 `；selector ` 1 `；EOL ` RVA 0x3409D060 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-51262b776d9fbf2c](../../evidence/state_effects-sets-018.md#s-51262b776d9fbf2c)

### path-020169

```text
(exec)# do-exec debug archive config ha <cr>
```

Handler ` RVA 0xDEDE750 `；selector ` 1 `；EOL ` RVA 0x3409D5D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-cad730323abec8fe](../../evidence/state_effects-sets-043.md#s-cad730323abec8fe)

### path-020163

```text
(exec)# do-exec debug archive config timestamp <cr>
```

Handler ` RVA 0xDEDE750 `；selector ` 1 `；EOL ` RVA 0x3409D318 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-356a8bbfe6d19828](../../evidence/state_effects-sets-012.md#s-356a8bbfe6d19828)

### path-023046

```text
(exec)# do-exec debug archive log config persistent <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x3409A520 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-7e0e16c27c285885](../../evidence/state_effects-sets-027.md#s-7e0e16c27c285885)

### path-015998

```text
(exec)# do-exec debug archive versioning <cr>
```

Handler ` RVA 0xDEDE750 `；selector ` 0 `；EOL ` RVA 0x3409CB40 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-9cb1a38c87ec2f30](../../evidence/state_effects-sets-033.md#s-9cb1a38c87ec2f30)

### path-020147

```text
(exec)# do-exec debug archive versioning ha <cr>
```

Handler ` RVA 0xDEDE750 `；selector ` 0 `；EOL ` RVA 0x3409CB18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-838f1419f79a235d](../../evidence/state_effects-sets-028.md#s-838f1419f79a235d)

### path-012402

```text
(exec)# do-exec debug arp <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x33CDA618 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-fafc6f23e7cd70a1](../../evidence/conditions-sets-097.md#c-fafc6f23e7cd70a1) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-9e958954d30e10b2](../../evidence/state_effects-sets-034.md#s-9e958954d30e10b2)

### path-012903

```text
(exec)# do-exec debug arp adjacency <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x33CD8580 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-9e958954d30e10b2](../../evidence/state_effects-sets-034.md#s-9e958954d30e10b2)

### path-012911

```text
(exec)# do-exec debug arp application <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x33CD8828 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-9e958954d30e10b2](../../evidence/state_effects-sets-034.md#s-9e958954d30e10b2)

### path-013000

```text
(exec)# do-exec debug arp database <cr>
```

Handler ` RVA 0xE002120 `；selector ` 9 `；EOL ` RVA 0x33CD9D68 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-9e958954d30e10b2](../../evidence/state_effects-sets-034.md#s-9e958954d30e10b2)

### path-012918

```text
(exec)# do-exec debug arp dynamic <cr>
```

Handler ` RVA 0xE002120 `；selector ` 3 `；EOL ` RVA 0x33CD8AD0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-9e958954d30e10b2](../../evidence/state_effects-sets-034.md#s-9e958954d30e10b2)

### path-012977

```text
(exec)# do-exec debug arp error <cr>
```

Handler ` RVA 0xE002120 `；selector ` 13 `；EOL ` RVA 0x33CD9818 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-9e958954d30e10b2](../../evidence/state_effects-sets-034.md#s-9e958954d30e10b2)

### path-012931

```text
(exec)# do-exec debug arp ha <cr>
```

Handler ` RVA 0xE002120 `；selector ` 4 `；EOL ` RVA 0x33CD8D78 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-9e958954d30e10b2](../../evidence/state_effects-sets-034.md#s-9e958954d30e10b2)

### path-012940

```text
(exec)# do-exec debug arp interface <cr>
```

Handler ` RVA 0xE002120 `；selector ` 5 `；EOL ` RVA 0x33CD9020 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-9e958954d30e10b2](../../evidence/state_effects-sets-034.md#s-9e958954d30e10b2)

### path-013062

```text
(exec)# do-exec debug arp retry <cr>
```

Handler ` RVA 0xE002120 `；selector ` 12 `；EOL ` RVA 0x33CDA2F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-4b3a3d1751f02625](../../evidence/conditions-sets-030.md#c-4b3a3d1751f02625) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-9e958954d30e10b2](../../evidence/state_effects-sets-034.md#s-9e958954d30e10b2)

### path-012954

```text
(exec)# do-exec debug arp static <cr>
```

Handler ` RVA 0xE002120 `；selector ` 6 `；EOL ` RVA 0x33CD92C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-9e958954d30e10b2](../../evidence/state_effects-sets-034.md#s-9e958954d30e10b2)

### path-012965

```text
(exec)# do-exec debug arp subblocking <cr>
```

Handler ` RVA 0xE002120 `；selector ` 7 `；EOL ` RVA 0x33CD9570 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-9e958954d30e10b2](../../evidence/state_effects-sets-034.md#s-9e958954d30e10b2)

### path-012990

```text
(exec)# do-exec debug arp table <cr>
```

Handler ` RVA 0xE002120 `；selector ` 8 `；EOL ` RVA 0x33CD9AC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-9e958954d30e10b2](../../evidence/state_effects-sets-034.md#s-9e958954d30e10b2)

### path-013021

```text
(exec)# do-exec debug arp timer <cr>
```

Handler ` RVA 0xE002120 `；selector ` 10 `；EOL ` RVA 0x33CDA010 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-9e958954d30e10b2](../../evidence/state_effects-sets-034.md#s-9e958954d30e10b2)

### path-016463

```text
(exec)# do-exec debug aspp event <cr>
```

Handler ` RVA 0x113A0AC0 `；selector ` 0 `；EOL ` RVA 0x354A3338 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86be3c97d8d2f7fa](../../evidence/state_effects-sets-029.md#s-86be3c97d8d2f7fa)

### path-016483

```text
(exec)# do-exec debug aspp packet <cr>
```

Handler ` RVA 0x113A0AC0 `；selector ` 1 `；EOL ` RVA 0x354A3668 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86be3c97d8d2f7fa](../../evidence/state_effects-sets-029.md#s-86be3c97d8d2f7fa)

### path-015063

```text
(exec)# do-exec debug async async-queue <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x34935440 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-2e055ec396167eb8](../../evidence/state_effects-sets-010.md#s-2e055ec396167eb8)

### path-015026

```text
(exec)# do-exec debug async framing <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x34934C48 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-2e055ec396167eb8](../../evidence/state_effects-sets-010.md#s-2e055ec396167eb8)

### path-015038

```text
(exec)# do-exec debug async packet <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x34934EF0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-2e055ec396167eb8](../../evidence/state_effects-sets-010.md#s-2e055ec396167eb8)

### path-015048

```text
(exec)# do-exec debug async state <cr>
```

Handler ` RVA 0xE002120 `；selector ` 3 `；EOL ` RVA 0x34935198 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-2e055ec396167eb8](../../evidence/state_effects-sets-010.md#s-2e055ec396167eb8)

### path-014917

```text
(exec)# do-exec debug atm ilmi <cr>
```

Handler ` RVA 0xCCCAC00 `；selector ` 24 `；EOL ` RVA 0x33C52E30 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-380e1fd46139157d](../../evidence/conditions-sets-022.md#c-380e1fd46139157d) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d4a8f2431a7dc91e](../../evidence/state_effects-sets-045.md#s-d4a8f2431a7dc91e)

### path-019223

```text
(exec)# do-exec debug atm ilmi red <cr>
```

Handler ` RVA 0xCCCAC00 `；selector ` 29 `；EOL ` RVA 0x33C530D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-380e1fd46139157d](../../evidence/conditions-sets-022.md#c-380e1fd46139157d) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d4a8f2431a7dc91e](../../evidence/state_effects-sets-045.md#s-d4a8f2431a7dc91e)

### path-012768

```text
(exec)# do-exec debug atomic-config <cr>
```

Handler ` RVA 0x165754F0 `；selector ` 0 `；EOL ` RVA 0x35FA2C18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-7a804aab23089263](../../evidence/conditions-sets-048.md#c-7a804aab23089263) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d4a8f2431a7dc91e](../../evidence/state_effects-sets-045.md#s-d4a8f2431a7dc91e)

### path-015294

```text
(exec)# do-exec debug autoip event <cr>
```

Handler ` RVA 0xB286740 `；selector ` 0 `；EOL ` RVA 0x3372B5B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-01ead0ea95ae8c37](../../evidence/state_effects-sets-001.md#s-01ead0ea95ae8c37)

### path-012377

```text
(exec)# do-exec debug backup <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x34481E60 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-0b53a1aa365eb77c](../../evidence/state_effects-sets-003.md#s-0b53a1aa365eb77c)

### path-015537

```text
(exec)# do-exec debug beep concurrency <cr>
```

Handler ` RVA 0xEF60830 `；selector ` 3 `；EOL ` RVA 0x3448B2A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-81bc462d109cbab7](../../evidence/conditions-sets-050.md#c-81bc462d109cbab7) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-e57a3c627af09f6a](../../evidence/state_effects-sets-049.md#s-e57a3c627af09f6a)

### path-015573

```text
(exec)# do-exec debug beep profile <cr>
```

Handler ` RVA 0xEF60830 `；selector ` 1 `；EOL ` RVA 0x3448B950 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-81bc462d109cbab7](../../evidence/conditions-sets-050.md#c-81bc462d109cbab7) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-e57a3c627af09f6a](../../evidence/state_effects-sets-049.md#s-e57a3c627af09f6a)

### path-015579

```text
(exec)# do-exec debug beep session <cr>
```

Handler ` RVA 0xEF60830 `；selector ` 2 `；EOL ` RVA 0x3448B5D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-9f96a961b1d8c355](../../evidence/conditions-sets-062.md#c-9f96a961b1d8c355) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-e57a3c627af09f6a](../../evidence/state_effects-sets-049.md#s-e57a3c627af09f6a)

### path-014158

```text
(exec)# do-exec debug bfd dampening <cr>
```

Handler ` RVA 0x10B3D630 `；selector ` 3 `；EOL ` RVA 0x34CAD060 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d4a8f2431a7dc91e](../../evidence/state_effects-sets-045.md#s-d4a8f2431a7dc91e)

### path-014219

```text
(exec)# do-exec debug bfd event <cr>
```

Handler ` RVA 0x10B3D630 `；selector ` 1 `；EOL ` RVA 0x34CAC8B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-fb78c4ad31bd5b91](../../evidence/state_effects-sets-053.md#s-fb78c4ad31bd5b91)

### path-014130

```text
(exec)# do-exec debug bfd ha <cr>
```

Handler ` RVA 0x10B663D0 `；selector ` 0 `；EOL ` RVA 0x34CBEF70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-9445aae8fcc0f843](../../evidence/state_effects-sets-031.md#s-9445aae8fcc0f843)

### path-014198

```text
(exec)# do-exec debug bfd packet <cr>
```

Handler ` RVA 0x10B3D630 `；selector ` 0 `；EOL ` RVA 0x34CAC2A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-0df9338204ff9854](../../evidence/state_effects-sets-003.md#s-0df9338204ff9854)

### path-014143

```text
(exec)# do-exec debug bfd stub <cr>
```

Handler ` RVA 0x10B3D630 `；selector ` 2 `；EOL ` RVA 0x34CACDB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d4a8f2431a7dc91e](../../evidence/state_effects-sets-045.md#s-d4a8f2431a7dc91e)

### path-018704

```text
(exec)# do-exec debug bgp telemetry enable <cr>
```

Handler ` RVA 0xF047BD0 `；selector ` 1 `；EOL ` RVA 0x344F9690 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-e112a75c9f182ed6](../../evidence/state_effects-sets-048.md#s-e112a75c9f182ed6)

### path-014869

```text
(exec)# do-exec debug bidb errors <cr>
```

Handler ` RVA 0xE002120 `；selector ` 67 `；EOL ` RVA 0x33BF93F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-a8345e5eaa532084](../../evidence/state_effects-sets-036.md#s-a8345e5eaa532084)

### path-014852

```text
(exec)# do-exec debug bidb events <cr>
```

Handler ` RVA 0xE002120 `；selector ` 66 `；EOL ` RVA 0x33BF9150 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-a8345e5eaa532084](../../evidence/state_effects-sets-036.md#s-a8345e5eaa532084)

### path-014889

```text
(exec)# do-exec debug bidb verbose <cr>
```

Handler ` RVA 0xE002120 `；selector ` 68 `；EOL ` RVA 0x33BF96A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-a8345e5eaa532084](../../evidence/state_effects-sets-036.md#s-a8345e5eaa532084)

### path-012669

```text
(exec)# do-exec debug bing <cr>
```

Handler ` RVA 0xF277B80 `；selector ` 0 `；EOL ` RVA 0x345DE0F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-aca218c66635ddd1](../../evidence/state_effects-sets-037.md#s-aca218c66635ddd1)

### path-015538

```text
(exec)# do-exec debug bing detail <cr>
```

Handler ` RVA 0xF277B80 `；selector ` 1 `；EOL ` RVA 0x345DE0C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-aca218c66635ddd1](../../evidence/state_effects-sets-037.md#s-aca218c66635ddd1)

### path-017481

```text
(exec)# do-exec debug bridge-domain client api <cr>
```

Handler ` RVA 0xE002120 `；selector ` 9 `；EOL ` RVA 0x33950710 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-fa38053072f33138](../../evidence/state_effects-sets-053.md#s-fa38053072f33138)

### path-017460

```text
(exec)# do-exec debug bridge-domain client errors <cr>
```

Handler ` RVA 0xE002120 `；selector ` 8 `；EOL ` RVA 0x33950468 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-fa38053072f33138](../../evidence/state_effects-sets-053.md#s-fa38053072f33138)

### path-013575

```text
(exec)# do-exec debug bridge-domain configuration <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x339509A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-fa38053072f33138](../../evidence/state_effects-sets-053.md#s-fa38053072f33138)

### path-013591

```text
(exec)# do-exec debug bridge-domain errors <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x33950C50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-fa38053072f33138](../../evidence/state_effects-sets-053.md#s-fa38053072f33138)

### path-013604

```text
(exec)# do-exec debug bridge-domain ipc <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x33950EF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-fa38053072f33138](../../evidence/state_effects-sets-053.md#s-fa38053072f33138)

### path-017598

```text
(exec)# do-exec debug bridge-domain l2fib errors <cr>
```

Handler ` RVA 0xE002120 `；selector ` 11 `；EOL ` RVA 0x339522E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-2fd4070c5aa3e2fc](../../evidence/conditions-sets-019.md#c-2fd4070c5aa3e2fc) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-fa38053072f33138](../../evidence/state_effects-sets-053.md#s-fa38053072f33138)

### path-017580

```text
(exec)# do-exec debug bridge-domain l2fib events <cr>
```

Handler ` RVA 0xE002120 `；selector ` 10 `；EOL ` RVA 0x33952040 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-2fd4070c5aa3e2fc](../../evidence/conditions-sets-019.md#c-2fd4070c5aa3e2fc) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-fa38053072f33138](../../evidence/state_effects-sets-053.md#s-fa38053072f33138)

### path-013618

```text
(exec)# do-exec debug bridge-domain linkfault <cr>
```

Handler ` RVA 0xE002120 `；selector ` 3 `；EOL ` RVA 0x339511A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-fa38053072f33138](../../evidence/state_effects-sets-053.md#s-fa38053072f33138)

### path-017582

```text
(exec)# do-exec debug bridge-domain route errors <cr>
```

Handler ` RVA 0xE002120 `；selector ` 5 `；EOL ` RVA 0x33951798 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-a2c8f4785d34409f](../../evidence/conditions-sets-063.md#c-a2c8f4785d34409f) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-fa38053072f33138](../../evidence/state_effects-sets-053.md#s-fa38053072f33138)

### path-017564

```text
(exec)# do-exec debug bridge-domain route events <cr>
```

Handler ` RVA 0xE002120 `；selector ` 4 `；EOL ` RVA 0x339514F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-a2c8f4785d34409f](../../evidence/conditions-sets-063.md#c-a2c8f4785d34409f) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-fa38053072f33138](../../evidence/state_effects-sets-053.md#s-fa38053072f33138)

### path-017618

```text
(exec)# do-exec debug bridge-domain route flow-control <cr>
```

Handler ` RVA 0xE002120 `；selector ` 7 `；EOL ` RVA 0x33951CE8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-a2c8f4785d34409f](../../evidence/conditions-sets-063.md#c-a2c8f4785d34409f) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-fa38053072f33138](../../evidence/state_effects-sets-053.md#s-fa38053072f33138)

### path-017601

```text
(exec)# do-exec debug bridge-domain route messages <cr>
```

Handler ` RVA 0xE002120 `；selector ` 6 `；EOL ` RVA 0x33951A40 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-a2c8f4785d34409f](../../evidence/conditions-sets-063.md#c-a2c8f4785d34409f) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-fa38053072f33138](../../evidence/state_effects-sets-053.md#s-fa38053072f33138)

### path-016240

```text
(exec)# do-exec debug bsc diagnostic <cr>
```

Handler ` RVA 0x113C3860 `；selector ` 2 `；EOL ` RVA 0x354B4EF0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-7ad05864500022cf](../../evidence/state_effects-sets-026.md#s-7ad05864500022cf)

### path-016251

```text
(exec)# do-exec debug bsc event <cr>
```

Handler ` RVA 0x113C3860 `；selector ` 0 `；EOL ` RVA 0x354B51E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-7ad05864500022cf](../../evidence/state_effects-sets-026.md#s-7ad05864500022cf)

### path-016267

```text
(exec)# do-exec debug bsc packet <cr>
```

Handler ` RVA 0x113C3860 `；selector ` 1 `；EOL ` RVA 0x354B5510 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-7ad05864500022cf](../../evidence/state_effects-sets-026.md#s-7ad05864500022cf)

### path-016250

```text
(exec)# do-exec debug bstun event <cr>
```

Handler ` RVA 0x113E6740 `；selector ` 1 `；EOL ` RVA 0x354BBF48 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-e8dd7d9532728825](../../evidence/state_effects-sets-049.md#s-e8dd7d9532728825)

### path-016266

```text
(exec)# do-exec debug bstun packet <cr>
```

Handler ` RVA 0x113E6740 `；selector ` 2 `；EOL ` RVA 0x354BC278 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-e8dd7d9532728825](../../evidence/state_effects-sets-049.md#s-e8dd7d9532728825)

### path-012737

```text
(exec)# do-exec debug buffer <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x342BC530 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-c8081f83a81c57e5](../../evidence/state_effects-sets-042.md#s-c8081f83a81c57e5)

### path-016027

```text
(exec)# do-exec debug buffer failures <cr>
```

Handler ` RVA 0xE002120 `；selector ` 22 `；EOL ` RVA 0x342BC508 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-c8081f83a81c57e5](../../evidence/state_effects-sets-042.md#s-c8081f83a81c57e5)

### path-020492

```text
(exec)# do-exec debug bulkstat client all <cr>
```

Handler ` RVA 0xBC6CE30 `；selector ` 2 `；EOL ` RVA 0x33888E78 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d4a8f2431a7dc91e](../../evidence/state_effects-sets-045.md#s-d4a8f2431a7dc91e)

### path-020478

```text
(exec)# do-exec debug bulkstat client error <cr>
```

Handler ` RVA 0xBC6CCA0 `；selector ` 0 `；EOL ` RVA 0x33888908 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-141b5024754c9d72](../../evidence/state_effects-sets-005.md#s-141b5024754c9d72)

### path-020485

```text
(exec)# do-exec debug bulkstat client info <cr>
```

Handler ` RVA 0xBC6CCA0 `；selector ` 1 `；EOL ` RVA 0x33888BC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-f307e8be814c51db](../../evidence/state_effects-sets-051.md#s-f307e8be814c51db)

### path-020486

```text
(exec)# do-exec debug bulkstat file all <cr>
```

Handler ` RVA 0xBC6CE30 `；selector ` 1 `；EOL ` RVA 0x33888620 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d4a8f2431a7dc91e](../../evidence/state_effects-sets-045.md#s-d4a8f2431a7dc91e)

### path-020469

```text
(exec)# do-exec debug bulkstat file error <cr>
```

Handler ` RVA 0xBC6CB70 `；selector ` 0 `；EOL ` RVA 0x338880B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-6f42b6b33ae1838e](../../evidence/state_effects-sets-024.md#s-6f42b6b33ae1838e)

### path-020479

```text
(exec)# do-exec debug bulkstat file info <cr>
```

Handler ` RVA 0xBC6CB70 `；selector ` 1 `；EOL ` RVA 0x33888368 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-01d3c12c49f31465](../../evidence/state_effects-sets-001.md#s-01d3c12c49f31465)

### path-020510

```text
(exec)# do-exec debug bulkstat processing all <cr>
```

Handler ` RVA 0xBC88F60 `；selector ` 0 `；EOL ` RVA 0x338984B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d4a8f2431a7dc91e](../../evidence/state_effects-sets-045.md#s-d4a8f2431a7dc91e)

### path-020504

```text
(exec)# do-exec debug bulkstat processing error <cr>
```

Handler ` RVA 0xBC88E60 `；selector ` 0 `；EOL ` RVA 0x338981F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-a87537ccb7d314ac](../../evidence/state_effects-sets-036.md#s-a87537ccb7d314ac)

### path-020495

```text
(exec)# do-exec debug bulkstat processing info <cr>
```

Handler ` RVA 0xBC88E60 `；selector ` 1 `；EOL ` RVA 0x33897F40 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-b34b10b53601425b](../../evidence/state_effects-sets-038.md#s-b34b10b53601425b)

### path-014874

```text
(exec)# do-exec debug caaa accounting <cr>
```

Handler ` RVA 0xCB23BA0 `；selector ` 4 `；EOL ` RVA 0x33BB3A88 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-694d96eafc24b4dc](../../evidence/state_effects-sets-023.md#s-694d96eafc24b4dc)

### path-014945

```text
(exec)# do-exec debug caaa all <cr>
```

Handler ` RVA 0xCB23BA0 `；selector ` 0 `；EOL ` RVA 0x33BB4A78 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-694d96eafc24b4dc](../../evidence/state_effects-sets-023.md#s-694d96eafc24b4dc)

### path-014891

```text
(exec)# do-exec debug caaa authentication <cr>
```

Handler ` RVA 0xCB23BA0 `；selector ` 2 `；EOL ` RVA 0x33BB3D30 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-694d96eafc24b4dc](../../evidence/state_effects-sets-023.md#s-694d96eafc24b4dc)

### path-014901

```text
(exec)# do-exec debug caaa authorization <cr>
```

Handler ` RVA 0xCB23BA0 `；selector ` 3 `；EOL ` RVA 0x33BB3FD8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-694d96eafc24b4dc](../../evidence/state_effects-sets-023.md#s-694d96eafc24b4dc)

### path-014846

```text
(exec)# do-exec debug caaa command-handler <cr>
```

Handler ` RVA 0xCB23BA0 `；selector ` 6 `；EOL ` RVA 0x33BB3538 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-694d96eafc24b4dc](../../evidence/state_effects-sets-023.md#s-694d96eafc24b4dc)

### path-014910

```text
(exec)# do-exec debug caaa error <cr>
```

Handler ` RVA 0xCB23BA0 `；selector ` 1 `；EOL ` RVA 0x33BB4280 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-694d96eafc24b4dc](../../evidence/state_effects-sets-023.md#s-694d96eafc24b4dc)

### path-014827

```text
(exec)# do-exec debug caaa ha <cr>
```

Handler ` RVA 0xCB23BA0 `；selector ` 7 `；EOL ` RVA 0x33BB3290 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-694d96eafc24b4dc](../../evidence/state_effects-sets-023.md#s-694d96eafc24b4dc)

### path-014854

```text
(exec)# do-exec debug caaa service <cr>
```

Handler ` RVA 0xCB23BA0 `；selector ` 5 `；EOL ` RVA 0x33BB37E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-694d96eafc24b4dc](../../evidence/state_effects-sets-023.md#s-694d96eafc24b4dc)

### path-019796

```text
(exec)# do-exec debug call filter detail <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x3605B290 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-258041ec2881700c](../../evidence/conditions-sets-015.md#c-258041ec2881700c) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-96753c2cf79a74e6](../../evidence/state_effects-sets-032.md#s-96753c2cf79a74e6)

### path-019782

```text
(exec)# do-exec debug call filter inout <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x3605AFD8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-258041ec2881700c](../../evidence/conditions-sets-015.md#c-258041ec2881700c) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-94f863806e525fff](../../evidence/state_effects-sets-032.md#s-94f863806e525fff)

### path-015832

```text
(exec)# do-exec debug call-admission elog <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x3408F7A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-98b80068de0f2d44](../../evidence/state_effects-sets-032.md#s-98b80068de0f2d44)

### path-015841

```text
(exec)# do-exec debug call-admission trace <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x3408FA50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-98b80068de0f2d44](../../evidence/state_effects-sets-032.md#s-98b80068de0f2d44)

### path-013605

```text
(exec)# do-exec debug call-home all <cr>
```

Handler ` RVA 0xB6C6E20 `；selector ` 14 `；EOL ` RVA 0x337F5370 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-62d7ac9fa6265b99](../../evidence/state_effects-sets-021.md#s-62d7ac9fa6265b99)

### path-013538

```text
(exec)# do-exec debug call-home detail <cr>
```

Handler ` RVA 0xB6C6E20 `；selector ` 2 `；EOL ` RVA 0x337F48D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-62d7ac9fa6265b99](../../evidence/state_effects-sets-021.md#s-62d7ac9fa6265b99)

### path-017602

```text
(exec)# do-exec debug call-home diagnostic-signature action <cr>
```

Handler ` RVA 0xB6C6E20 `；selector ` 6 `；EOL ` RVA 0x337F61B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-b58ba307c710c9e3](../../evidence/conditions-sets-070.md#c-b58ba307c710c9e3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-62d7ac9fa6265b99](../../evidence/state_effects-sets-021.md#s-62d7ac9fa6265b99)

### path-017690

```text
(exec)# do-exec debug call-home diagnostic-signature all <cr>
```

Handler ` RVA 0xB6C6E20 `；selector ` 15 `；EOL ` RVA 0x337F6EF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-b58ba307c710c9e3](../../evidence/conditions-sets-070.md#c-b58ba307c710c9e3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-62d7ac9fa6265b99](../../evidence/state_effects-sets-021.md#s-62d7ac9fa6265b99)

### path-017637

```text
(exec)# do-exec debug call-home diagnostic-signature api <cr>
```

Handler ` RVA 0xB6C6E20 `；selector ` 8 `；EOL ` RVA 0x337F6700 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-b58ba307c710c9e3](../../evidence/conditions-sets-070.md#c-b58ba307c710c9e3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-62d7ac9fa6265b99](../../evidence/state_effects-sets-021.md#s-62d7ac9fa6265b99)

### path-017660

```text
(exec)# do-exec debug call-home diagnostic-signature cli <cr>
```

Handler ` RVA 0xB6C6E20 `；selector ` 10 `；EOL ` RVA 0x337F69A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-b58ba307c710c9e3](../../evidence/conditions-sets-070.md#c-b58ba307c710c9e3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-62d7ac9fa6265b99](../../evidence/state_effects-sets-021.md#s-62d7ac9fa6265b99)

### path-017619

```text
(exec)# do-exec debug call-home diagnostic-signature download <cr>
```

Handler ` RVA 0xB6C6E20 `；selector ` 7 `；EOL ` RVA 0x337F6458 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-b58ba307c710c9e3](../../evidence/conditions-sets-070.md#c-b58ba307c710c9e3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-62d7ac9fa6265b99](../../evidence/state_effects-sets-021.md#s-62d7ac9fa6265b99)

### path-017677

```text
(exec)# do-exec debug call-home diagnostic-signature error <cr>
```

Handler ` RVA 0xB6C6E20 `；selector ` 9 `；EOL ` RVA 0x337F6C50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-b58ba307c710c9e3](../../evidence/conditions-sets-070.md#c-b58ba307c710c9e3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-62d7ac9fa6265b99](../../evidence/state_effects-sets-021.md#s-62d7ac9fa6265b99)

### path-017583

```text
(exec)# do-exec debug call-home diagnostic-signature event-registration <cr>
```

Handler ` RVA 0xB6C6E20 `；selector ` 5 `；EOL ` RVA 0x337F5F08 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-b58ba307c710c9e3](../../evidence/conditions-sets-070.md#c-b58ba307c710c9e3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-62d7ac9fa6265b99](../../evidence/state_effects-sets-021.md#s-62d7ac9fa6265b99)

### path-017565

```text
(exec)# do-exec debug call-home diagnostic-signature parsing <cr>
```

Handler ` RVA 0xB6C6E20 `；selector ` 4 `；EOL ` RVA 0x337F5C60 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-b58ba307c710c9e3](../../evidence/conditions-sets-070.md#c-b58ba307c710c9e3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-62d7ac9fa6265b99](../../evidence/state_effects-sets-021.md#s-62d7ac9fa6265b99)

### path-013576

```text
(exec)# do-exec debug call-home error <cr>
```

Handler ` RVA 0xB6C6E20 `；selector ` 1 `；EOL ` RVA 0x337F4E20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-62d7ac9fa6265b99](../../evidence/state_effects-sets-021.md#s-62d7ac9fa6265b99)

### path-013557

```text
(exec)# do-exec debug call-home mail <cr>
```

Handler ` RVA 0xB6C6E20 `；selector ` 3 `；EOL ` RVA 0x337F4B78 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-62d7ac9fa6265b99](../../evidence/state_effects-sets-021.md#s-62d7ac9fa6265b99)

### path-013635

```text
(exec)# do-exec debug call-home message-content <cr>
```

Handler ` RVA 0xB6C6E20 `；selector ` 13 `；EOL ` RVA 0x337F56A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-62d7ac9fa6265b99](../../evidence/state_effects-sets-021.md#s-62d7ac9fa6265b99)

### path-021472

```text
(exec)# do-exec debug call-home message-content profile <string> <cr>
```

Handler ` RVA 0xB6C71B0 `；selector ` 0 `；EOL ` RVA 0x337F56E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

参数提示：` string ` Profile name。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-e516ecaeeb5cb103](../../evidence/parameters-sets-017.md#p-e516ecaeeb5cb103) · [状态效果 S-62d7ac9fa6265b99](../../evidence/state_effects-sets-021.md#s-62d7ac9fa6265b99)

### path-017617

```text
(exec)# do-exec debug call-home smart-licensing all <cr>
```

Handler ` RVA 0xB6C6E20 `；selector ` 16 `；EOL ` RVA 0x337F77A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c282937774386a6d](../../evidence/conditions-sets-075.md#c-c282937774386a6d) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-62d7ac9fa6265b99](../../evidence/state_effects-sets-021.md#s-62d7ac9fa6265b99)

### path-017599

```text
(exec)# do-exec debug call-home smart-licensing error <cr>
```

Handler ` RVA 0xB6C6E20 `；selector ` 12 `；EOL ` RVA 0x337F7500 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c282937774386a6d](../../evidence/conditions-sets-075.md#c-c282937774386a6d) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-62d7ac9fa6265b99](../../evidence/state_effects-sets-021.md#s-62d7ac9fa6265b99)

### path-017581

```text
(exec)# do-exec debug call-home smart-licensing trace <cr>
```

Handler ` RVA 0xB6C6E20 `；selector ` 11 `；EOL ` RVA 0x337F7258 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c282937774386a6d](../../evidence/conditions-sets-075.md#c-c282937774386a6d) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-62d7ac9fa6265b99](../../evidence/state_effects-sets-021.md#s-62d7ac9fa6265b99)

### path-013592

```text
(exec)# do-exec debug call-home trace <cr>
```

Handler ` RVA 0xB6C6E20 `；selector ` 0 `；EOL ` RVA 0x337F50C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-62d7ac9fa6265b99](../../evidence/state_effects-sets-021.md#s-62d7ac9fa6265b99)

### path-012672

```text
(exec)# do-exec debug callback <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x346049D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d82a5c0180fbd033](../../evidence/state_effects-sets-046.md#s-d82a5c0180fbd033)

### path-012322

```text
(exec)# do-exec debug cca <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x33EDDF58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-edb95c3e271de9fc](../../evidence/state_effects-sets-050.md#s-edb95c3e271de9fc)

### path-013872

```text
(exec)# do-exec debug cce cp <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x340387A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-a92b32d9940db7cf](../../evidence/state_effects-sets-036.md#s-a92b32d9940db7cf)

### path-021742

```text
(exec)# do-exec debug cce cp filter balance <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x34038DE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-a92b32d9940db7cf](../../evidence/state_effects-sets-036.md#s-a92b32d9940db7cf)

### path-013940

```text
(exec)# do-exec debug cce cpdp <cr>
```

Handler ` RVA 0xE002120 `；selector ` 3 `；EOL ` RVA 0x3403BB90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-db5e512fc34d0186](../../evidence/state_effects-sets-046.md#s-db5e512fc34d0186)

### path-017869

```text
(exec)# do-exec debug cce cpdp elog <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x3403BB68 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-db5e512fc34d0186](../../evidence/state_effects-sets-046.md#s-db5e512fc34d0186)

### path-017878

```text
(exec)# do-exec debug cce cpdp events <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x3403B698 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-db5e512fc34d0186](../../evidence/state_effects-sets-046.md#s-db5e512fc34d0186)

### path-021779

```text
(exec)# do-exec debug cce cpdp events detailed <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x3403B670 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-db5e512fc34d0186](../../evidence/state_effects-sets-046.md#s-db5e512fc34d0186)

### path-013941

```text
(exec)# do-exec debug cce ha <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x33CDECF0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-c5ae7e900a751ba9](../../evidence/state_effects-sets-042.md#s-c5ae7e900a751ba9)

### path-017850

```text
(exec)# do-exec debug cce ha event <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x33CDEA20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-c5ae7e900a751ba9](../../evidence/state_effects-sets-042.md#s-c5ae7e900a751ba9)

### path-017870

```text
(exec)# do-exec debug cce ha issu <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x33CDECC8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-c5ae7e900a751ba9](../../evidence/state_effects-sets-042.md#s-c5ae7e900a751ba9)

### path-015758

```text
(exec)# do-exec debug cdapi detail <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x35F0C540 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-6eeba880c9b6cc52](../../evidence/state_effects-sets-024.md#s-6eeba880c9b6cc52)

### path-015749

```text
(exec)# do-exec debug cdapi events <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x35F0C298 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-6eeba880c9b6cc52](../../evidence/state_effects-sets-024.md#s-6eeba880c9b6cc52)

### path-013756

```text
(exec)# do-exec debug cdp adjacency <cr>
```

Handler ` RVA 0xCDB4000 `；selector ` 2 `；EOL ` RVA 0x33CE0CC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-2e1ac7e5fc7ce8d5](../../evidence/state_effects-sets-010.md#s-2e1ac7e5fc7ce8d5)

### path-013741

```text
(exec)# do-exec debug cdp events <cr>
```

Handler ` RVA 0xCDB4000 `；selector ` 1 `；EOL ` RVA 0x33CE0A18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-2e1ac7e5fc7ce8d5](../../evidence/state_effects-sets-010.md#s-2e1ac7e5fc7ce8d5)

### path-013803

```text
(exec)# do-exec debug cdp ilp <cr>
```

Handler ` RVA 0xE002120 `；selector ` 6 `；EOL ` RVA 0x33CE1760 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-2e1ac7e5fc7ce8d5](../../evidence/state_effects-sets-010.md#s-2e1ac7e5fc7ce8d5)

### path-013770

```text
(exec)# do-exec debug cdp ip <cr>
```

Handler ` RVA 0xCDB4000 `；selector ` 3 `；EOL ` RVA 0x33CE0F68 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-2e1ac7e5fc7ce8d5](../../evidence/state_effects-sets-010.md#s-2e1ac7e5fc7ce8d5)

### path-013780

```text
(exec)# do-exec debug cdp location-server <cr>
```

Handler ` RVA 0xCDB4000 `；selector ` 4 `；EOL ` RVA 0x33CE1210 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-2e1ac7e5fc7ce8d5](../../evidence/state_effects-sets-010.md#s-2e1ac7e5fc7ce8d5)

### path-013725

```text
(exec)# do-exec debug cdp packets <cr>
```

Handler ` RVA 0xCDB4000 `；selector ` 0 `；EOL ` RVA 0x33CE0770 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-2e1ac7e5fc7ce8d5](../../evidence/state_effects-sets-010.md#s-2e1ac7e5fc7ce8d5)

### path-013791

```text
(exec)# do-exec debug cdp test <cr>
```

Handler ` RVA 0xCDB4000 `；selector ` 5 `；EOL ` RVA 0x33CE14B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-2e1ac7e5fc7ce8d5](../../evidence/state_effects-sets-010.md#s-2e1ac7e5fc7ce8d5)

### path-017494

```text
(exec)# do-exec debug cef filter fib <cr>
```

Handler ` RVA 0xB384EB0 `；selector ` 0 `；EOL ` RVA 0x337431A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-23ff211ff072c38e](../../evidence/conditions-sets-014.md#c-23ff211ff072c38e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d4a8f2431a7dc91e](../../evidence/state_effects-sets-045.md#s-d4a8f2431a7dc91e)

### path-024677

```text
(exec)# do-exec debug cef filter hardware notifications type global <cr>
```

Handler ` RVA 0xB4F8820 `；selector ` 0 `；EOL ` RVA 0x33743D70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-b49d61a50aefd7fc](../../evidence/conditions-sets-070.md#c-b49d61a50aefd7fc) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-b69ef00ac7a563f4](../../evidence/state_effects-sets-039.md#s-b69ef00ac7a563f4)

### path-017530

```text
(exec)# do-exec debug cef filter path <cr>
```

Handler ` RVA 0xB422A80 `；selector ` 0 `；EOL ` RVA 0x33742A20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-1d9eff5c458d488a](../../evidence/conditions-sets-011.md#c-1d9eff5c458d488a) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-9334153e3dac3627](../../evidence/state_effects-sets-031.md#s-9334153e3dac3627)

### path-023632

```text
(exec)# do-exec debug cef filter subtree context client <cr>
```

Handler ` RVA 0xB4537D0 `；selector ` 0 `；EOL ` RVA 0x33742120 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-2202aea78e5fe8f9](../../evidence/conditions-sets-013.md#c-2202aea78e5fe8f9) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d4a8f2431a7dc91e](../../evidence/state_effects-sets-045.md#s-d4a8f2431a7dc91e)

### path-017507

```text
(exec)# do-exec debug cef filter table <cr>
```

Handler ` RVA 0xB45B0A0 `；selector ` 0 `；EOL ` RVA 0x33743680 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-8d9574f67f9c000b](../../evidence/conditions-sets-055.md#c-8d9574f67f9c000b) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d4a8f2431a7dc91e](../../evidence/state_effects-sets-045.md#s-d4a8f2431a7dc91e)

### path-021396

```text
(exec)# do-exec debug cef filter uid key <cr>
```

Handler ` RVA 0xB4B72F0 `；selector ` 0 `；EOL ` RVA 0x337424F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-8853bc4a8d2ea75b](../../evidence/conditions-sets-053.md#c-8853bc4a8d2ea75b) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-9b75f6c1f3462899](../../evidence/state_effects-sets-033.md#s-9b75f6c1f3462899)

### path-017524

```text
(exec)# do-exec debug cef filter vrf <cr>
```

Handler ` RVA 0xB4863B0 `；selector ` 0 `；EOL ` RVA 0x337439F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-2c53eccc697cbeaa](../../evidence/conditions-sets-017.md#c-2c53eccc697cbeaa) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d4a8f2431a7dc91e](../../evidence/state_effects-sets-045.md#s-d4a8f2431a7dc91e)

### path-013567

```text
(exec)# do-exec debug cef table <cr>
```

Handler ` RVA 0xB37CB40 `；selector ` 0 `；EOL ` RVA 0x33744360 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-f1137aa5bfa5a5ee](../../evidence/conditions-sets-093.md#c-f1137aa5bfa5a5ee) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3c1b9e5ed88f2e4a](../../evidence/state_effects-sets-013.md#s-3c1b9e5ed88f2e4a)

### path-012323

```text
(exec)# do-exec debug cfgdiff <cr>
```

Handler ` RVA 0xDFDE3D0 `；selector ` 1 `；EOL ` RVA 0x34113FC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-b5539a04714e019a](../../evidence/state_effects-sets-038.md#s-b5539a04714e019a)

### path-012874

```text
(exec)# do-exec debug cfgdiff timestamp <cr>
```

Handler ` RVA 0xDFDE3D0 `；selector ` 2 `；EOL ` RVA 0x34113F98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-b5539a04714e019a](../../evidence/state_effects-sets-038.md#s-b5539a04714e019a)

### path-012578

```text
(exec)# do-exec debug cft <cr>
```

Handler ` RVA 0x1294A410 `；selector ` 6 `；EOL ` RVA 0x358FF988 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-05ee9ecdcf9df941](../../evidence/conditions-sets-003.md#c-05ee9ecdcf9df941) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-eba2a42fa2f9efe8](../../evidence/state_effects-sets-050.md#s-eba2a42fa2f9efe8)

### path-014293

```text
(exec)# do-exec debug cft ager <cr>
```

Handler ` RVA 0x1294A410 `；selector ` 4 `；EOL ` RVA 0x358FEEC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c63405c103f266fa](../../evidence/conditions-sets-076.md#c-c63405c103f266fa) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-eba2a42fa2f9efe8](../../evidence/state_effects-sets-050.md#s-eba2a42fa2f9efe8)

### path-014331

```text
(exec)# do-exec debug cft engine <cr>
```

Handler ` RVA 0x1294A410 `；selector ` 0 `；EOL ` RVA 0x358FF410 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-65a4da85f565c802](../../evidence/conditions-sets-039.md#c-65a4da85f565c802) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-eba2a42fa2f9efe8](../../evidence/state_effects-sets-050.md#s-eba2a42fa2f9efe8)

### path-014348

```text
(exec)# do-exec debug cft fe <cr>
```

Handler ` RVA 0x1294A410 `；selector ` 3 `；EOL ` RVA 0x358FF6B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-827860dbf2bd2652](../../evidence/conditions-sets-051.md#c-827860dbf2bd2652) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-eba2a42fa2f9efe8](../../evidence/state_effects-sets-050.md#s-eba2a42fa2f9efe8)

### path-014272

```text
(exec)# do-exec debug cft flow <cr>
```

Handler ` RVA 0x1294A410 `；selector ` 5 `；EOL ` RVA 0x358FEC18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-85cda2da03d2f0ef](../../evidence/conditions-sets-052.md#c-85cda2da03d2f0ef) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-eba2a42fa2f9efe8](../../evidence/state_effects-sets-050.md#s-eba2a42fa2f9efe8)

### path-014370

```text
(exec)# do-exec debug cft l4 <cr>
```

Handler ` RVA 0x1294A410 `；selector ` 2 `；EOL ` RVA 0x358FF960 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-e86e00332a835f9a](../../evidence/conditions-sets-090.md#c-e86e00332a835f9a) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-eba2a42fa2f9efe8](../../evidence/state_effects-sets-050.md#s-eba2a42fa2f9efe8)

### path-014310

```text
(exec)# do-exec debug cft memory <cr>
```

Handler ` RVA 0x1294A410 `；selector ` 1 `；EOL ` RVA 0x358FF168 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-1545adc3150c5285](../../evidence/conditions-sets-008.md#c-1545adc3150c5285) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-eba2a42fa2f9efe8](../../evidence/state_effects-sets-050.md#s-eba2a42fa2f9efe8)

### path-012674

```text
(exec)# do-exec debug chat <cr>
```

Handler ` RVA 0xF2F58D0 `；selector ` 0 `；EOL ` RVA 0x346038B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-046d8988795821bf](../../evidence/state_effects-sets-001.md#s-046d8988795821bf)

### path-013258

```text
(exec)# do-exec debug checkpoint timers <cr>
```

Handler ` RVA 0xCDBA680 `；selector ` 0 `；EOL ` RVA 0x33CECC38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-263debe3019bb027](../../evidence/state_effects-sets-009.md#s-263debe3019bb027)

### path-015161

```text
(exec)# do-exec debug clns cache <cr>
```

Handler ` RVA 0xE002120 `；selector ` 6 `；EOL ` RVA 0x34B6DC98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-5a332d8ef81f92df](../../evidence/state_effects-sets-019.md#s-5a332d8ef81f92df)

### path-019434

```text
(exec)# do-exec debug clns esis events <cr>
```

Handler ` RVA 0xE002120 `；selector ` 8 `；EOL ` RVA 0x34B6C768 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-5a332d8ef81f92df](../../evidence/state_effects-sets-019.md#s-5a332d8ef81f92df)

### path-019448

```text
(exec)# do-exec debug clns esis packets <cr>
```

Handler ` RVA 0xE002120 `；selector ` 9 `；EOL ` RVA 0x34B6CA10 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-5a332d8ef81f92df](../../evidence/state_effects-sets-019.md#s-5a332d8ef81f92df)

### path-015061

```text
(exec)# do-exec debug clns events <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x34B6CCA8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-5a332d8ef81f92df](../../evidence/state_effects-sets-019.md#s-5a332d8ef81f92df)

### path-015149

```text
(exec)# do-exec debug clns filters <cr>
```

Handler ` RVA 0xE002120 `；selector ` 7 `；EOL ` RVA 0x34B6D9F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-5a332d8ef81f92df](../../evidence/state_effects-sets-019.md#s-5a332d8ef81f92df)

### path-015112

```text
(exec)# do-exec debug clns igrp-adjacency <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x34B6D4A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-5a332d8ef81f92df](../../evidence/state_effects-sets-019.md#s-5a332d8ef81f92df)

### path-015081

```text
(exec)# do-exec debug clns igrp-events <cr>
```

Handler ` RVA 0xE002120 `；selector ` 3 `；EOL ` RVA 0x34B6CF50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-5a332d8ef81f92df](../../evidence/state_effects-sets-019.md#s-5a332d8ef81f92df)

### path-015097

```text
(exec)# do-exec debug clns igrp-packets <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x34B6D1F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-5a332d8ef81f92df](../../evidence/state_effects-sets-019.md#s-5a332d8ef81f92df)

### path-015132

```text
(exec)# do-exec debug clns packets <cr>
```

Handler ` RVA 0xE002120 `；selector ` 4 `；EOL ` RVA 0x34B6D748 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-5a332d8ef81f92df](../../evidence/state_effects-sets-019.md#s-5a332d8ef81f92df)

### path-015182

```text
(exec)# do-exec debug clns routing <cr>
```

Handler ` RVA 0xE002120 `；selector ` 5 `；EOL ` RVA 0x34B6DF40 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-5a332d8ef81f92df](../../evidence/state_effects-sets-019.md#s-5a332d8ef81f92df)

### path-015143

```text
(exec)# do-exec debug cls errors <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x354C1F30 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-a08fa7c140c12567](../../evidence/state_effects-sets-034.md#s-a08fa7c140c12567)

### path-015212

```text
(exec)# do-exec debug cls flow-control <cr>
```

Handler ` RVA 0xE002120 `；selector ` 7 `；EOL ` RVA 0x354C29D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-a08fa7c140c12567](../../evidence/state_effects-sets-034.md#s-a08fa7c140c12567)

### path-015227

```text
(exec)# do-exec debug cls hpr <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x354C2C78 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-a08fa7c140c12567](../../evidence/state_effects-sets-034.md#s-a08fa7c140c12567)

### path-015157

```text
(exec)# do-exec debug cls messages <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x354C21D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-a08fa7c140c12567](../../evidence/state_effects-sets-034.md#s-a08fa7c140c12567)

### path-015176

```text
(exec)# do-exec debug cls sdlc <cr>
```

Handler ` RVA 0xE002120 `；selector ` 4 `；EOL ` RVA 0x354C2480 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-a08fa7c140c12567](../../evidence/state_effects-sets-034.md#s-a08fa7c140c12567)

### path-015124

```text
(exec)# do-exec debug cls state <cr>
```

Handler ` RVA 0xE002120 `；selector ` 5 `；EOL ` RVA 0x354C1C88 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-a08fa7c140c12567](../../evidence/state_effects-sets-034.md#s-a08fa7c140c12567)

### path-015195

```text
(exec)# do-exec debug cls vdlc <cr>
```

Handler ` RVA 0xE002120 `；selector ` 3 `；EOL ` RVA 0x354C2728 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-a08fa7c140c12567](../../evidence/state_effects-sets-034.md#s-a08fa7c140c12567)

### path-016192

```text
(exec)# do-exec debug cns aaa <cr>
```

Handler ` RVA 0xE002120 `；selector ` 6 `；EOL ` RVA 0x340E7338 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-d2f0a3c77c500959](../../evidence/conditions-sets-081.md#c-d2f0a3c77c500959) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-638eab795b48d518](../../evidence/state_effects-sets-021.md#s-638eab795b48d518)

### path-016239

```text
(exec)# do-exec debug cns all <cr>
```

Handler ` RVA 0xDFA8FB0 `；selector ` 0 `；EOL ` RVA 0x340E8680 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-d2f0a3c77c500959](../../evidence/conditions-sets-081.md#c-d2f0a3c77c500959) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d4a8f2431a7dc91e](../../evidence/state_effects-sets-045.md#s-d4a8f2431a7dc91e)

### path-016147

```text
(exec)# do-exec debug cns config <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x3460F7F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-1599e7a0e40a9dc7](../../evidence/state_effects-sets-005.md#s-1599e7a0e40a9dc7)

### path-020324

```text
(exec)# do-exec debug cns config all <cr>
```

Handler ` RVA 0xF314C20 `；selector ` 0 `；EOL ` RVA 0x3460F518 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-e73b5be61871a329](../../evidence/state_effects-sets-049.md#s-e73b5be61871a329)

### path-020298

```text
(exec)# do-exec debug cns config apply <cr>
```

Handler ` RVA 0xE002120 `；selector ` 3 `；EOL ` RVA 0x3460ED20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-e73b5be61871a329](../../evidence/state_effects-sets-049.md#s-e73b5be61871a329)

### path-020310

```text
(exec)# do-exec debug cns config decode <cr>
```

Handler ` RVA 0xE002120 `；selector ` 4 `；EOL ` RVA 0x3460EFC8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-e73b5be61871a329](../../evidence/state_effects-sets-049.md#s-e73b5be61871a329)

### path-020284

```text
(exec)# do-exec debug cns config initial <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x3460EA78 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-e73b5be61871a329](../../evidence/state_effects-sets-049.md#s-e73b5be61871a329)

### path-020255

```text
(exec)# do-exec debug cns config interface <cr>
```

Handler ` RVA 0xE002120 `；selector ` 6 `；EOL ` RVA 0x3460E528 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-e73b5be61871a329](../../evidence/state_effects-sets-049.md#s-e73b5be61871a329)

### path-020316

```text
(exec)# do-exec debug cns config messages <cr>
```

Handler ` RVA 0xE002120 `；selector ` 5 `；EOL ` RVA 0x3460F270 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-e73b5be61871a329](../../evidence/state_effects-sets-049.md#s-e73b5be61871a329)

### path-023169

```text
(exec)# do-exec debug cns config notify all <cr>
```

Handler ` RVA 0xF32E760 `；selector ` 0 `；EOL ` RVA 0x34611C20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-8130df01f36cc7ad](../../evidence/state_effects-sets-027.md#s-8130df01f36cc7ad)

### path-023144

```text
(exec)# do-exec debug cns config notify eventing <cr>
```

Handler ` RVA 0xE002120 `；selector ` 5 `；EOL ` RVA 0x34610C30 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-8130df01f36cc7ad](../../evidence/state_effects-sets-027.md#s-8130df01f36cc7ad)

### path-023165

```text
(exec)# do-exec debug cns config notify expand <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x34611978 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-8130df01f36cc7ad](../../evidence/state_effects-sets-027.md#s-8130df01f36cc7ad)

### path-023152

```text
(exec)# do-exec debug cns config notify generation <cr>
```

Handler ` RVA 0xE002120 `；selector ` 3 `；EOL ` RVA 0x34611180 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-8130df01f36cc7ad](../../evidence/state_effects-sets-027.md#s-8130df01f36cc7ad)

### path-023160

```text
(exec)# do-exec debug cns config notify modes <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x346116D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-8130df01f36cc7ad](../../evidence/state_effects-sets-027.md#s-8130df01f36cc7ad)

### path-023148

```text
(exec)# do-exec debug cns config notify nvgen <cr>
```

Handler ` RVA 0xE002120 `；selector ` 4 `；EOL ` RVA 0x34610ED8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-8130df01f36cc7ad](../../evidence/state_effects-sets-027.md#s-8130df01f36cc7ad)

### path-023155

```text
(exec)# do-exec debug cns config notify xml <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x34611428 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-8130df01f36cc7ad](../../evidence/state_effects-sets-027.md#s-8130df01f36cc7ad)

### path-020269

```text
(exec)# do-exec debug cns config partial <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x3460E7D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-e73b5be61871a329](../../evidence/state_effects-sets-049.md#s-e73b5be61871a329)

### path-020244

```text
(exec)# do-exec debug cns config retrieve <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x3460E280 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-e73b5be61871a329](../../evidence/state_effects-sets-049.md#s-e73b5be61871a329)

### path-020249

```text
(exec)# do-exec debug cns event agent <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x34617F78 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-933a9ddd4b23e812](../../evidence/state_effects-sets-031.md#s-933a9ddd4b23e812)

### path-020272

```text
(exec)# do-exec debug cns event all <cr>
```

Handler ` RVA 0xF35D580 `；selector ` 0 `；EOL ` RVA 0x346184C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-933a9ddd4b23e812](../../evidence/state_effects-sets-031.md#s-933a9ddd4b23e812)

### path-020236

```text
(exec)# do-exec debug cns event connection <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x34617CD0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-933a9ddd4b23e812](../../evidence/state_effects-sets-031.md#s-933a9ddd4b23e812)

### path-020258

```text
(exec)# do-exec debug cns event subscriber <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x34618220 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-933a9ddd4b23e812](../../evidence/state_effects-sets-031.md#s-933a9ddd4b23e812)

### path-020253

```text
(exec)# do-exec debug cns exec agent <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x346198D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d679a762957f8868](../../evidence/state_effects-sets-045.md#s-d679a762957f8868)

### path-020296

```text
(exec)# do-exec debug cns exec all <cr>
```

Handler ` RVA 0xF369750 `；selector ` 0 `；EOL ` RVA 0x3461A0C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d679a762957f8868](../../evidence/state_effects-sets-045.md#s-d679a762957f8868)

### path-020282

```text
(exec)# do-exec debug cns exec decode <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x34619E20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d679a762957f8868](../../evidence/state_effects-sets-045.md#s-d679a762957f8868)

### path-020267

```text
(exec)# do-exec debug cns exec messages <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x34619B78 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d679a762957f8868](../../evidence/state_effects-sets-045.md#s-d679a762957f8868)

### path-016208

```text
(exec)# do-exec debug cns format <cr>
```

Handler ` RVA 0xE002120 `；selector ` 5 `；EOL ` RVA 0x340E75F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-d2f0a3c77c500959](../../evidence/conditions-sets-081.md#c-d2f0a3c77c500959) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-fb635b0d0bc669ee](../../evidence/state_effects-sets-053.md#s-fb635b0d0bc669ee)

### path-016181

```text
(exec)# do-exec debug cns framework <cr>
```

Handler ` RVA 0xE002120 `；selector ` 4 `；EOL ` RVA 0x340E7080 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-d2f0a3c77c500959](../../evidence/conditions-sets-081.md#c-d2f0a3c77c500959) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-4cbe08f01c3c3c8d](../../evidence/state_effects-sets-017.md#s-4cbe08f01c3c3c8d)

### path-016219

```text
(exec)# do-exec debug cns http <cr>
```

Handler ` RVA 0xE002120 `；selector ` 7 `；EOL ` RVA 0x340E78A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-d2f0a3c77c500959](../../evidence/conditions-sets-081.md#c-d2f0a3c77c500959) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-ac496d5fb8352004](../../evidence/state_effects-sets-036.md#s-ac496d5fb8352004)

### path-020280

```text
(exec)# do-exec debug cns image agent <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x3461CC78 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-01d4ef58f638ce7a](../../evidence/state_effects-sets-001.md#s-01d4ef58f638ce7a)

### path-020308

```text
(exec)# do-exec debug cns image all <cr>
```

Handler ` RVA 0xF36F680 `；selector ` 0 `；EOL ` RVA 0x3461D1C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-01d4ef58f638ce7a](../../evidence/state_effects-sets-001.md#s-01d4ef58f638ce7a)

### path-020264

```text
(exec)# do-exec debug cns image connection <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x3461C9D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

[条件 C-c6ae9c1b3845cab6](../../evidence/conditions-sets-077.md#c-c6ae9c1b3845cab6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-01d4ef58f638ce7a](../../evidence/state_effects-sets-001.md#s-01d4ef58f638ce7a)

