# configure · 六个基础模式的历史连接

[模式索引](README.md) · [总索引](../../README.md)

### path-062774

```text
(config)# vlan group <string> vlan-list <string> <cr>
```

Handler ` RVA 0x15EB6290 `；selector ` 0 `；EOL ` RVA 0x35E60A70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` vlan Group name ；` string ` &lt;1-4094&gt;  VLAN id。

[条件 C-e0933f9e8f393938](../../evidence/conditions-sets-086.md#c-e0933f9e8f393938) · [缺口 G-79c9ae0eed4ee8ea](../../evidence/gaps-sets-005.md#g-79c9ae0eed4ee8ea) · [参数 P-8882d230fad6b545](../../evidence/parameters-sets-011.md#p-8882d230fad6b545) · [状态效果 S-96bcefcfb83f17e4](../../evidence/state_effects-sets-032.md#s-96bcefcfb83f17e4)

### path-034112

```text
(config)# vlan internal allocation policy ascending <cr>
```

Handler ` RVA 0x15DB76E0 `；selector ` 0 `；EOL ` RVA 0x35E2F6E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3e1fd56c3e793e88](../../evidence/conditions-sets-024.md#c-3e1fd56c3e793e88) · [状态效果 S-7a754b9f5555790f](../../evidence/state_effects-sets-026.md#s-7a754b9f5555790f)

### path-044724

```text
(config)# vlan-autoconfig authorize list default password <string> <cr>
```

Handler ` RVA 0x112B65D0 `；selector ` 11 `；EOL ` RVA 0x35451028 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` password。

[条件 C-e231b4a05c6b5a25](../../evidence/conditions-sets-087.md#c-e231b4a05c6b5a25) · [参数 P-cf38db5444e8df1e](../../evidence/parameters-sets-016.md#p-cf38db5444e8df1e) · [状态效果 S-e56dc29487c9e89f](../../evidence/state_effects-sets-049.md#s-e56dc29487c9e89f)

### path-063013

```text
(config)# vlan-autoconfig identifier nas-port <cr>
```

Handler ` RVA 0x112B61A0 `；selector ` 12 `；EOL ` RVA 0x35451500 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ee0b12bf8d500f5f](../../evidence/conditions-sets-092.md#c-ee0b12bf8d500f5f) · [缺口 G-2fa0f2e1c26853be](../../evidence/gaps-sets-002.md#g-2fa0f2e1c26853be) · [状态效果 S-ec50e70705422599](../../evidence/state_effects-sets-050.md#s-ec50e70705422599)

### path-037183

```text
(config)# vpdn aaa attribute class tunnel-class <cr>
```

Handler ` RVA 0x11D48420 `；selector ` 7 `；EOL ` RVA 0x356E4610 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-037043

```text
(config)# vpdn aaa attribute nas-ip-address vpdn-nas <cr>
```

Handler ` RVA 0x11D48420 `；selector ` 4 `；EOL ` RVA 0x356E3978 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-037094

```text
(config)# vpdn aaa attribute nas-ip-address vpdn-tunnel-client <cr>
```

Handler ` RVA 0x11D48420 `；selector ` 5 `；EOL ` RVA 0x356E3C20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-037233

```text
(config)# vpdn aaa attribute nas-port physical-channel-id <cr>
```

Handler ` RVA 0x11D48420 `；selector ` 3 `；EOL ` RVA 0x356E3F80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2d1b98573a9f1859](../../evidence/conditions-sets-018.md#c-2d1b98573a9f1859) · [状态效果 S-6074e21c31ded66b](../../evidence/state_effects-sets-021.md#s-6074e21c31ded66b)

### path-037140

```text
(config)# vpdn aaa attribute username gateway <cr>
```

Handler ` RVA 0x11D48420 `；selector ` 6 `；EOL ` RVA 0x356E4340 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-030423

```text
(config)# vpdn aaa override-server <string> <cr>
```

Handler ` RVA 0x11DB9580 `；selector ` 2 `；EOL ` RVA 0x356E3628 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name or IP address of AAA server。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-f0995ff6dabadcd3](../../evidence/parameters-sets-018.md#p-f0995ff6dabadcd3) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-030472

```text
(config)# vpdn aaa untagged default <cr>
```

Handler ` RVA 0x11DB9580 `；selector ` 19 `；EOL ` RVA 0x356E4910 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025904

```text
(config)# vpdn authen-before-forward <cr>
```

Handler ` RVA 0x11D48420 `；selector ` 45 `；EOL ` RVA 0x356E0730 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027461

```text
(config)# vpdn authorize directed-request <cr>
```

Handler ` RVA 0x11D48420 `；selector ` 46 `；EOL ` RVA 0x356E90A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027466

```text
(config)# vpdn authorize domain <cr>
```

Handler ` RVA 0x11DB9580 `；selector ` 10 `；EOL ` RVA 0x356E9348 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060314

```text
(config)# vpdn domain-delimiter <cr>
```

Handler ` RVA 0x11DB9580 `；selector ` 1 `；EOL ` RVA 0x356E4C88 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [缺口 G-b1c582d32518e4f0](../../evidence/gaps-sets-006.md#g-b1c582d32518e4f0) · [状态效果 S-fd1c8cd6c275eaf7](../../evidence/state_effects-sets-054.md#s-fd1c8cd6c275eaf7)

### path-025893

```text
(config)# vpdn enable <cr>
```

Handler ` RVA 0x11D48420 `；selector ` 28 `；EOL ` RVA 0x356DFE50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027458

```text
(config)# vpdn history failure <cr>
```

Handler ` RVA 0x11D48420 `；selector ` 51 `；EOL ` RVA 0x356E86E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-061407

```text
(config)# vpdn incoming <string> <string> virtual-template <number:dynamic> <cr>
```

Handler ` RVA 0x11D48420 `；selector ` 2 `；EOL ` RVA 0x356E7E18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Name NAS will use to identify itself；` string ` Name to use when authenticating to NAS；` unsigned_number_dynamic ` Virtual Template interface to use。

[条件 C-d40ade9788e55de8](../../evidence/conditions-sets-082.md#c-d40ade9788e55de8) · [缺口 G-9af335e411783a71](../../evidence/gaps-sets-006.md#g-9af335e411783a71) · [参数 P-c7396a549e4eb916](../../evidence/parameters-sets-015.md#p-c7396a549e4eb916) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-037471

```text
(config)# vpdn ip udp ignore checksum <cr>
```

Handler ` RVA 0x11DB9580 `；selector ` 9 `；EOL ` RVA 0x356E8D90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-046741

```text
(config)# vpdn l2tp attribute clid mask-method remove <cr>
```

Handler ` RVA 0x11D48420 `；selector ` 16 `；EOL ` RVA 0x356E21F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-42735a98d331faea](../../evidence/conditions-sets-026.md#c-42735a98d331faea) · [状态效果 S-30e8df657f90587e](../../evidence/state_effects-sets-011.md#s-30e8df657f90587e)

### path-030502

```text
(config)# vpdn l2tp attribute initial-received-lcp-confreq <cr>
```

Handler ` RVA 0x11D48420 `；selector ` 18 `；EOL ` RVA 0x356E29C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-030476

```text
(config)# vpdn l2tp attribute physical-channel-id <cr>
```

Handler ` RVA 0x11D48420 `；selector ` 17 `；EOL ` RVA 0x356E2718 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-030473

```text
(config)# vpdn l2tp cac enable <cr>
```

Handler ` RVA 0x11DB9580 `；selector ` 143 `；EOL ` RVA 0x356E2CA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-046310

```text
(config)# vpdn l2tp nas-port-type map all virtual <cr>
```

Handler ` RVA 0x11D48420 `；selector ` 12 `；EOL ` RVA 0x356E1180 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-046369

```text
(config)# vpdn l2tp nas-port-type map digital-async v110 <cr>
```

Handler ` RVA 0x11D48420 `；selector ` 13 `；EOL ` RVA 0x356E1450 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-037111

```text
(config)# vpdn l2tp session refuse <number:0..12> <cr>
```

Handler ` RVA 0x11D48420 `；selector ` 15 `；EOL ` RVA 0x356E1E00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` L2TP result code to send in CDN。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-a67c40175a493765](../../evidence/parameters-sets-013.md#p-a67c40175a493765) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-037000

```text
(config)# vpdn l2tp session refuse icrp <cr>
```

Handler ` RVA 0x11D48420 `；selector ` 142 `；EOL ` RVA 0x356E1AE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-036947

```text
(config)# vpdn l2tp tunnel refuse <number:0..11> <cr>
```

Handler ` RVA 0x11D48420 `；selector ` 14 `；EOL ` RVA 0x356E17A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` L2TP error code to send in StopCCN。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-36e69e87ede83923](../../evidence/parameters-sets-005.md#p-36e69e87ede83923) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025931

```text
(config)# vpdn logging <cr>
```

Handler ` RVA 0x11D48420 `；selector ` 48 `；EOL ` RVA 0x356E0A40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-df24a13a99ddc2c8](../../evidence/conditions-sets-086.md#c-df24a13a99ddc2c8) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025922

```text
(config)# vpdn multihop <cr>
```

Handler ` RVA 0x11D48420 `；selector ` 53 `；EOL ` RVA 0x356E55A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-046904

```text
(config)# vpdn outgoing <string> <string> ip <address> <cr>
```

Handler ` RVA 0x11D48420 `；selector ` 1 `；EOL ` RVA 0x356E8250 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of GW domain；` string ` Name to use when authenticating to gateway；` address ` IP destination。

[条件 C-ac552c9b7623dfac](../../evidence/conditions-sets-067.md#c-ac552c9b7623dfac) · [参数 P-b58c4b78643f3d00](../../evidence/parameters-sets-014.md#p-b58c4b78643f3d00) · [状态效果 S-d2633cd65535b42c](../../evidence/state_effects-sets-045.md#s-d2633cd65535b42c)

### path-025957

```text
(config)# vpdn pmtu <cr>
```

Handler ` RVA 0x11D48420 `；selector ` 133 `；EOL ` RVA 0x356E9648 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7d090f98a1c9d2f1](../../evidence/conditions-sets-048.md#c-7d090f98a1c9d2f1) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060676

```text
(config)# vpdn pmtu minimum <number:dynamic> <cr>
```

Handler ` RVA 0x11D48420 `；selector ` 133 `；EOL ` RVA 0x356E9648 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` &lt;Minimum MTU size&gt;。

[条件 C-6bb7952ebf476756](../../evidence/conditions-sets-042.md#c-6bb7952ebf476756) · [缺口 G-14b895bcdd4742ab](../../evidence/gaps-sets-001.md#g-14b895bcdd4742ab) · [参数 P-8f07f5b1cddb529f](../../evidence/parameters-sets-011.md#p-8f07f5b1cddb529f) · [状态效果 S-cc694c946b0a5cfc](../../evidence/state_effects-sets-043.md#s-cc694c946b0a5cfc)

### path-027340

```text
(config)# vpdn pptp tcp listen-queue <number:32..128> <cr>
```

Handler ` RVA 0x11D48420 `；selector ` 94 `；EOL ` RVA 0x356E2FD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-587ab3ca841f29d0](../../evidence/conditions-sets-035.md#c-587ab3ca841f29d0) · [参数 P-1751cd22238b0d2d](../../evidence/parameters-sets-002.md#p-1751cd22238b0d2d) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027350

```text
(config)# vpdn pptp tcp window-size <number:256..4096> <cr>
```

Handler ` RVA 0x11D48420 `；selector ` 95 `；EOL ` RVA 0x356E3018 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c9a92318d80f4600](../../evidence/conditions-sets-078.md#c-c9a92318d80f4600) · [参数 P-1618e09030d753eb](../../evidence/parameters-sets-002.md#p-1618e09030d753eb) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027306

```text
(config)# vpdn queuesize-alert <number:10..16384> <cr>
```

Handler ` RVA 0x11D48420 `；selector ` 144 `；EOL ` RVA 0x356E0188 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Max queue size。

[条件 C-f75735c347f5a22e](../../evidence/conditions-sets-096.md#c-f75735c347f5a22e) · [参数 P-6f57fb4c13dd0208](../../evidence/parameters-sets-009.md#p-6f57fb4c13dd0208) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025945

```text
(config)# vpdn redirect <cr>
```

Handler ` RVA 0x11D48420 `；selector ` 124 `；EOL ` RVA 0x356E78A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-63e7b869a97a52fb](../../evidence/conditions-sets-039.md#c-63e7b869a97a52fb) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060319

```text
(config)# vpdn search-order <cr>
```

Handler ` RVA 0x11DB9580 `；selector ` 0 `；EOL ` RVA 0x356E5050 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9553a8a3a8e23ee3](../../evidence/conditions-sets-058.md#c-9553a8a3a8e23ee3) · [缺口 G-63242fb5f19bfb1e](../../evidence/gaps-sets-004.md#g-63242fb5f19bfb1e) · [状态效果 S-d1d976edf13b148e](../../evidence/state_effects-sets-044.md#s-d1d976edf13b148e)

### path-037344

```text
(config)# vpdn session accounting network default <cr>
```

Handler ` RVA 0x11D48420 `；selector ` 130 `；EOL ` RVA 0x356E7010 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a24464ba36462a58](../../evidence/conditions-sets-063.md#c-a24464ba36462a58) · [状态效果 S-37feae9797f87e70](../../evidence/state_effects-sets-012.md#s-37feae9797f87e70)

### path-046856

```text
(config)# vpdn session accounting suppress multihop inbound <cr>
```

Handler ` RVA 0x11D48420 `；selector ` 54 `；EOL ` RVA 0x356E7460 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fef340e38746f722](../../evidence/conditions-sets-098.md#c-fef340e38746f722) · [状态效果 S-b4af4fee7965e7bd](../../evidence/state_effects-sets-038.md#s-b4af4fee7965e7bd)

### path-030576

```text
(config)# vpdn session rate compute <cr>
```

Handler ` RVA 0x11D48420 `；selector ` 132 `；EOL ` RVA 0x356E6CB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060422

```text
(config)# vpdn session-limit <number:dynamic> <cr>
```

Handler ` RVA 0x11D48420 `；selector ` 118 `；EOL ` RVA 0x356E04A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Number of sessions。

[条件 C-8f2a3fad0c8f4e82](../../evidence/conditions-sets-055.md#c-8f2a3fad0c8f4e82) · [缺口 G-40ff9355c17220ac](../../evidence/gaps-sets-003.md#g-40ff9355c17220ac) · [参数 P-20e903153304d1a8](../../evidence/parameters-sets-003.md#p-20e903153304d1a8) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025941

```text
(config)# vpdn softshut <cr>
```

Handler ` RVA 0x11DB9580 `；selector ` 8 `；EOL ` RVA 0x356E8A00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027395

```text
(config)# vpdn source-ip <address> <cr>
```

Handler ` RVA 0x11D48420 `；selector ` 44 `；EOL ` RVA 0x356E58D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP source。

[条件 C-10a38f4074b823d9](../../evidence/conditions-sets-007.md#c-10a38f4074b823d9) · [参数 P-166451d72552a7bf](../../evidence/parameters-sets-002.md#p-166451d72552a7bf) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-037267

```text
(config)# vpdn tunnel accounting network default <cr>
```

Handler ` RVA 0x11D48420 `；selector ` 129 `；EOL ` RVA 0x356E5C90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b21c51df782910bd](../../evidence/conditions-sets-069.md#c-b21c51df782910bd) · [状态效果 S-a9d2265e210779de](../../evidence/state_effects-sets-036.md#s-a9d2265e210779de)

### path-037306

```text
(config)# vpdn tunnel authorization network default <cr>
```

Handler ` RVA 0x11D48420 `；selector ` 128 `；EOL ` RVA 0x356E60E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7a9cfa2a9be9ab03](../../evidence/conditions-sets-048.md#c-7a9cfa2a9be9ab03) · [状态效果 S-2834f4fb961580fc](../../evidence/state_effects-sets-009.md#s-2834f4fb961580fc)

### path-037486

```text
(config)# vpdn tunnel authorization password <string> <cr>
```

Handler ` RVA 0x11D48420 `；selector ` 126 `；EOL ` RVA 0x356E67D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` The UNENCRYPTED (cleartext) dummy password。

[条件 C-40e4ffbc51864bed](../../evidence/conditions-sets-025.md#c-40e4ffbc51864bed) · [参数 P-4bcc4c49114d51d3](../../evidence/parameters-sets-006.md#p-4bcc4c49114d51d3) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060912

```text
(config)# vpdn tunnel authorization virtual-template <number:dynamic> <cr>
```

Handler ` RVA 0x11D48420 `；selector ` 127 `；EOL ` RVA 0x356E64E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Virtual Template interface number。

[条件 C-2e93235979db5fb1](../../evidence/conditions-sets-018.md#c-2e93235979db5fb1) · [缺口 G-e9ba080c2b440837](../../evidence/gaps-sets-008.md#g-e9ba080c2b440837) · [参数 P-eb203f3c2db33777](../../evidence/parameters-sets-018.md#p-eb203f3c2db33777) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025900

```text
(config)# vpdn-group <string> <cr>
```

Handler ` RVA 0x11D50C10 `；selector ` 26 `；EOL ` RVA 0x356FA560 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` VPDN Group name。

[条件 C-f8dc4c912d821418](../../evidence/conditions-sets-096.md#c-f8dc4c912d821418) · [参数 P-cb2b0250c1e541f3](../../evidence/parameters-sets-015.md#p-cb2b0250c1e541f3) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025476

```text
(config)# vpdn-template <cr>
```

Handler ` RVA 0x11D50C10 `；selector ` 27 `；EOL ` RVA 0x356E9BC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-caa344cc46412794](../../evidence/conditions-sets-078.md#c-caa344cc46412794) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025534

```text
(config)# vrf definition <cr>
```

Handler ` RVA 0xDC3DE20 `；selector ` 1 `；EOL ` RVA 0x340127A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3d777f601b12001f](../../evidence/conditions-sets-024.md#c-3d777f601b12001f) · [状态效果 S-565aa3e01ecb30ac](../../evidence/state_effects-sets-019.md#s-565aa3e01ecb30ac)

### path-060371

```text
(config)# vrf definition <string> <cr>
```

Handler ` RVA 0xDC3DE20 `；selector ` 1 `；EOL ` RVA 0x340127A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` VRF name。

[条件 C-9b4960e411f8e371](../../evidence/conditions-sets-060.md#c-9b4960e411f8e371) · [缺口 G-0decde473c41dddf](../../evidence/gaps-sets-001.md#g-0decde473c41dddf) · [参数 P-1ef89c1b9ea85dfc](../../evidence/parameters-sets-003.md#p-1ef89c1b9ea85dfc) · [状态效果 S-eb71abf34587dc08](../../evidence/state_effects-sets-050.md#s-eb71abf34587dc08)

### path-025558

```text
(config)# vrf list <cr>
```

Handler ` RVA 0x12465510 `；selector ` 0 `；EOL ` RVA 0x35872490 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-034a823eca1cddcf](../../evidence/conditions-sets-002.md#c-034a823eca1cddcf) · [状态效果 S-51d41e01fd8c2412](../../evidence/state_effects-sets-018.md#s-51d41e01fd8c2412)

### path-060373

```text
(config)# vrf list <string> <cr>
```

Handler ` RVA 0x12465510 `；selector ` 0 `；EOL ` RVA 0x35872490 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` VRF list name。

[条件 C-e0e8f6f3e8525922](../../evidence/conditions-sets-087.md#c-e0e8f6f3e8525922) · [缺口 G-d10f75fb1a6df9e4](../../evidence/gaps-sets-007.md#g-d10f75fb1a6df9e4) · [参数 P-3399f02b7394eebd](../../evidence/parameters-sets-004.md#p-3399f02b7394eebd) · [状态效果 S-286fcada8d31593f](../../evidence/state_effects-sets-009.md#s-286fcada8d31593f)

### path-025522

```text
(config)# vrf rd-auto <cr>
```

Handler ` RVA 0xDC2C340 `；selector ` 0 `；EOL ` RVA 0x34011EB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a6f389688527cbc7](../../evidence/conditions-sets-064.md#c-a6f389688527cbc7) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-052066

```text
(config)# vrf selection source <address> <address> vrf <string> <cr>
```

Handler ` RVA 0xFADD5A0 `；selector ` 0 `；EOL ` RVA 0x34807EE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Source IP Address；` address ` Source IP Mask；` string ` vrf name。

[条件 C-dddac83a5ea96f8c](../../evidence/conditions-sets-085.md#c-dddac83a5ea96f8c) · [参数 P-0236b50aaa266eec](../../evidence/parameters-sets-001.md#p-0236b50aaa266eec) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027881

```text
(config)# vrf upgrade-cli multi-af-mode non-common-policies <cr>
```

Handler ` RVA 0xDC29960 `；selector ` 0 `；EOL ` RVA 0x34012430 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6c7d25c572665742](../../evidence/conditions-sets-042.md#c-6c7d25c572665742) · [状态效果 S-c90919adddbcec0d](../../evidence/state_effects-sets-043.md#s-c90919adddbcec0d)

### path-062810

```text
(config)# vrf upgrade-cli multi-af-mode non-common-policies vrf <?option@555589566280> <cr>
```

Handler ` RVA 0xDC29960 `；selector ` 0 `；EOL ` RVA 0x34012430 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-34d79274948fd9a1](../../evidence/conditions-sets-021.md#c-34d79274948fd9a1) · [缺口 G-06153324087fc797](../../evidence/gaps-sets-001.md#g-06153324087fc797) · [状态效果 S-1ce477067ca81a7d](../../evidence/state_effects-sets-007.md#s-1ce477067ca81a7d)

### path-025455

```text
(config)# vrrp match-address-limit <number:0..8> <cr>
```

Handler ` RVA 0x133C9190 `；selector ` 0 `；EOL ` RVA 0x35A80EE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Address limit。

[条件 C-e239ccb2efb60ee0](../../evidence/conditions-sets-087.md#c-e239ccb2efb60ee0) · [参数 P-a55773a1ac0a5726](../../evidence/parameters-sets-013.md#p-a55773a1ac0a5726) · [状态效果 S-052c6d383a09870f](../../evidence/state_effects-sets-002.md#s-052c6d383a09870f)

### path-062707

```text
(config)# vrrp sso <cr>
```

Handler ` RVA 0xE2E2C60 `；selector ` 1 `；EOL ` RVA 0x33FCF630 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c56f696683f4ced7](../../evidence/conditions-sets-076.md#c-c56f696683f4ced7) · [缺口 G-688711d43d11df7f](../../evidence/gaps-sets-004.md#g-688711d43d11df7f) · [状态效果 S-401e16a4dba6044b](../../evidence/state_effects-sets-014.md#s-401e16a4dba6044b)

### path-025712

```text
(config)# vrrs <string> <cr>
```

Handler ` RVA 0xE2FA9A0 `；selector ` 0 `；EOL ` RVA 0x342A2ED8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` vrrs name。

[条件 C-729a2f8fe24e4fd5](../../evidence/conditions-sets-044.md#c-729a2f8fe24e4fd5) · [参数 P-d332111ec86ea2db](../../evidence/parameters-sets-016.md#p-d332111ec86ea2db) · [状态效果 S-9b491d2ab62e21cc](../../evidence/state_effects-sets-033.md#s-9b491d2ab62e21cc)

### path-026962

```text
(config)# vtp domain <string> <cr>
```

Handler ` RVA 0x15C78530 `；selector ` 4 `；EOL ` RVA 0x35E01658 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` The ascii name for the VTP administrative domain.。

[条件 C-d2b11a982116e877](../../evidence/conditions-sets-081.md#c-d2b11a982116e877) · [参数 P-a226a4515f89bdb5](../../evidence/parameters-sets-012.md#p-a226a4515f89bdb5) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026884

```text
(config)# vtp file <string> <cr>
```

Handler ` RVA 0x15C78530 `；selector ` 0 `；EOL ` RVA 0x35E008D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` The ascii name of the IFS filesystem file where VTP configuration is stored.。

[条件 C-0be6928e300ad6d8](../../evidence/conditions-sets-005.md#c-0be6928e300ad6d8) · [参数 P-f8efa2c2814ebe5b](../../evidence/parameters-sets-019.md#p-f8efa2c2814ebe5b) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060401

```text
(config)# vtp if-id <interface> <cr>
```

Handler ` RVA 0x15C78530 `；selector ` 1 `；EOL ` RVA 0x35E00C20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d303802c0a81fc88](../../evidence/conditions-sets-081.md#c-d303802c0a81fc88) · [缺口 G-073022ec26032629](../../evidence/gaps-sets-001.md#g-073022ec26032629) · [参数 P-73cca9b1ca14f2db](../../evidence/parameters-sets-009.md#p-73cca9b1ca14f2db) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060588

```text
(config)# vtp if-id <interface> only <cr>
```

Handler ` RVA 0x15C78530 `；selector ` 2 `；EOL ` RVA 0x35E00D08 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d303802c0a81fc88](../../evidence/conditions-sets-081.md#c-d303802c0a81fc88) · [缺口 G-073022ec26032629](../../evidence/gaps-sets-001.md#g-073022ec26032629) · [参数 P-73cca9b1ca14f2db](../../evidence/parameters-sets-009.md#p-73cca9b1ca14f2db) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025827

```text
(config)# vtp mode <cr>
```

Handler ` RVA 0x15C78530 `；selector ` 5 `；EOL ` RVA 0x35E019F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6895da0ab73f1fd2](../../evidence/conditions-sets-040.md#c-6895da0ab73f1fd2) · [状态效果 S-57f83c0da86d0538](../../evidence/state_effects-sets-019.md#s-57f83c0da86d0538)

### path-027049

```text
(config)# vtp password <string> <cr>
```

Handler ` RVA 0x15C78530 `；selector ` 7 `；EOL ` RVA 0x35E01F80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` The ascii password for the VTP administrative domain.。

[条件 C-b53f2377ffaf6a8b](../../evidence/conditions-sets-070.md#c-b53f2377ffaf6a8b) · [参数 P-ffe7347f896c4a8a](../../evidence/parameters-sets-019.md#p-ffe7347f896c4a8a) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025806

```text
(config)# vtp pruning <cr>
```

Handler ` RVA 0x15C78530 `；selector ` 10 `；EOL ` RVA 0x35E02608 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5409bbc238ef3cc8](../../evidence/conditions-sets-033.md#c-5409bbc238ef3cc8) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027026

```text
(config)# vtp server primary <cr>
```

Handler ` RVA 0x15C78530 `；selector ` 11 `；EOL ` RVA 0x35E028F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5409bbc238ef3cc8](../../evidence/conditions-sets-033.md#c-5409bbc238ef3cc8) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026929

```text
(config)# vtp trunk <string> <cr>
```

Handler ` RVA 0x15C78530 `；selector ` 3 `；EOL ` RVA 0x35E012F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` The shortname of the port to be configured as VTP trunk.。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-c4440997c90a5f00](../../evidence/parameters-sets-015.md#p-c4440997c90a5f00) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060404

```text
(config)# vtp version <number:dynamic> <cr>
```

Handler ` RVA 0x15C78530 `；selector ` 6 `；EOL ` RVA 0x35E02380 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Set the administrative domain VTP version number。

[条件 C-80e5fbdbf8892d70](../../evidence/conditions-sets-050.md#c-80e5fbdbf8892d70) · [缺口 G-2671be0cedd154a8](../../evidence/gaps-sets-002.md#g-2671be0cedd154a8) · [参数 P-d62ae94d26c93a7e](../../evidence/parameters-sets-016.md#p-d62ae94d26c93a7e) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025667

```text
(config)# wrr-queue bandwidth <cr>
```

Handler ` RVA 0x15F292B0 `；selector ` 0 `；EOL ` RVA 0x35E6C288 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ca9db79788c2e0b7](../../evidence/conditions-sets-078.md#c-ca9db79788c2e0b7) · [状态效果 S-fdd6ee5a3e1d3dbb](../../evidence/state_effects-sets-054.md#s-fdd6ee5a3e1d3dbb)

### path-028536

```text
(config)# wrr-queue cos-map <number:1..8> <number:0..7> <cr>
```

Handler ` RVA 0x15F28BE0 `；selector ` 0 `；EOL ` RVA 0x35E6CB08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` enter cos-map queue id (1-8)；` unsigned_number ` cos values separated by spaces (up to 8 values total)。

[条件 C-847f6c2935733e69](../../evidence/conditions-sets-051.md#c-847f6c2935733e69) · [参数 P-8c0bffa1f1aedeac](../../evidence/parameters-sets-011.md#p-8c0bffa1f1aedeac) · [状态效果 S-96bbe27aaec2a2f1](../../evidence/state_effects-sets-032.md#s-96bbe27aaec2a2f1)

### path-060472

```text
(config)# wsma agent config <cr>
```

Handler ` RVA 0xF3EA320 `；selector ` 1 `；EOL ` RVA 0x346397A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a550d1f56befde07](../../evidence/conditions-sets-064.md#c-a550d1f56befde07) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [状态效果 S-9969179893d99381](../../evidence/state_effects-sets-033.md#s-9969179893d99381)

### path-060471

```text
(config)# wsma agent exec <cr>
```

Handler ` RVA 0xF3EA320 `；selector ` 2 `；EOL ` RVA 0x346393C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7043b40e6127e300](../../evidence/conditions-sets-043.md#c-7043b40e6127e300) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [状态效果 S-9969179893d99381](../../evidence/state_effects-sets-033.md#s-9969179893d99381)

### path-060475

```text
(config)# wsma agent filesys <cr>
```

Handler ` RVA 0xF3EA320 `；selector ` 3 `；EOL ` RVA 0x34639B78 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9dd1cbae965f9dd9](../../evidence/conditions-sets-061.md#c-9dd1cbae965f9dd9) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [状态效果 S-9969179893d99381](../../evidence/state_effects-sets-033.md#s-9969179893d99381)

### path-060469

```text
(config)# wsma agent mgmt <cr>
```

Handler ` RVA 0xF3EA320 `；selector ` 6 `；EOL ` RVA 0x34638FF0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7fb209fd0bd31d97](../../evidence/conditions-sets-050.md#c-7fb209fd0bd31d97) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [状态效果 S-9969179893d99381](../../evidence/state_effects-sets-033.md#s-9969179893d99381)

### path-060480

```text
(config)# wsma agent notify <cr>
```

Handler ` RVA 0xF3EA320 `；selector ` 4 `；EOL ` RVA 0x34639F28 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-63a414c180dd8b53](../../evidence/conditions-sets-039.md#c-63a414c180dd8b53) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [状态效果 S-9969179893d99381](../../evidence/state_effects-sets-033.md#s-9969179893d99381)

### path-060351

```text
(config)# wsma dhcp <cr>
```

Handler ` RVA 0xF3EE770 `；selector ` 1 `；EOL ` RVA 0x3463A2F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-fcfe47944fd7a0f6](../../evidence/conditions-sets-098.md#c-fcfe47944fd7a0f6) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [状态效果 S-9969179893d99381](../../evidence/state_effects-sets-033.md#s-9969179893d99381)

### path-060344

```text
(config)# wsma id <cr>
```

Handler ` RVA 0xF4026B0 `；selector ` 0 `；EOL ` RVA 0x34638948 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-79191a3903a17729](../../evidence/conditions-sets-047.md#c-79191a3903a17729) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [状态效果 S-9969179893d99381](../../evidence/state_effects-sets-033.md#s-9969179893d99381)

### path-060690

```text
(config)# wsma profile initiator <string> <cr>
```

Handler ` RVA 0xF3D6610 `；selector ` 0 `；EOL ` RVA 0x3462D8D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Initiator profile name。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [参数 P-9c6035bae88f5caa](../../evidence/parameters-sets-012.md#p-9c6035bae88f5caa) · [状态效果 S-9969179893d99381](../../evidence/state_effects-sets-033.md#s-9969179893d99381)

### path-060688

```text
(config)# wsma profile listener <string> <cr>
```

Handler ` RVA 0xF3DD390 `；selector ` 0 `；EOL ` RVA 0x3462D5D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Listener profile name。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [参数 P-ffa21eccc0081bb0](../../evidence/parameters-sets-019.md#p-ffa21eccc0081bb0) · [状态效果 S-9969179893d99381](../../evidence/state_effects-sets-033.md#s-9969179893d99381)

### path-025937

```text
(config)# x25 call-record <cr>
```

Handler ` RVA 0x105F3880 `；selector ` 6 `；EOL ` RVA 0x34BCC308 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029900

```text
(config)# x25 host <string> <address> <cr>
```

Handler ` RVA 0x105F3880 `；selector ` 0 `；EOL ` RVA 0x34BCACD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` X.25 hostname；` address ` X.121 address of host。

[条件 C-457c3c145205f948](../../evidence/conditions-sets-027.md#c-457c3c145205f948) · [参数 P-f941792ec58438d6](../../evidence/parameters-sets-019.md#p-f941792ec58438d6) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029723

```text
(config)# x25 hunt-group <string> rotary <cr>
```

Handler ` RVA 0x10616320 `；selector ` 0 `；EOL ` RVA 0x34BC90B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` X.25 hunt-group name。

[条件 C-6ec1bf4a756c078c](../../evidence/conditions-sets-043.md#c-6ec1bf4a756c078c) · [参数 P-81855ecb80295a4e](../../evidence/parameters-sets-010.md#p-81855ecb80295a4e) · [状态效果 S-81d25fb75260b916](../../evidence/state_effects-sets-028.md#s-81d25fb75260b916)

### path-027450

```text
(config)# x25 profile <string> <cr>
```

Handler ` RVA 0x10615500 `；selector ` 3 `；EOL ` RVA 0x34BCB608 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of X.25 profile。

[条件 C-48f5d6ef4231acf0](../../evidence/conditions-sets-029.md#c-48f5d6ef4231acf0) · [参数 P-6762b4c561fd64df](../../evidence/parameters-sets-008.md#p-6762b4c561fd64df) · [状态效果 S-ea630852c5a74acc](../../evidence/state_effects-sets-050.md#s-ea630852c5a74acc)

### path-027447

```text
(config)# x25 roa <string> <cr>
```

Handler ` RVA 0x105F3880 `；selector ` 1 `；EOL ` RVA 0x34BCBF30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name to reference ROA list by。

[条件 C-511b8819d863bb2c](../../evidence/conditions-sets-032.md#c-511b8819d863bb2c) · [参数 P-380216499366b849](../../evidence/parameters-sets-005.md#p-380216499366b849) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060669

```text
(config)# x25 roa <string> <number:0..9999> <cr>
```

Handler ` RVA 0x105F3880 `；selector ` 1 `；EOL ` RVA 0x34BCBF30 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Name to reference ROA list by；` unsigned_number ` ROA ID。

[条件 C-02bc05140ec53b08](../../evidence/conditions-sets-002.md#c-02bc05140ec53b08) · [缺口 G-36d933d00b80a801](../../evidence/gaps-sets-002.md#g-36d933d00b80a801) · [参数 P-b3c399fce9f82181](../../evidence/parameters-sets-014.md#p-b3c399fce9f82181) · [状态效果 S-a354110c80ddffa1](../../evidence/state_effects-sets-035.md#s-a354110c80ddffa1)

### path-029943

```text
(config)# x25 rotary <number:1..99> <address> <cr>
```

Handler ` RVA 0x105F3880 `；selector ` 5 `；EOL ` RVA 0x34BCB0D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Rotary group number；` address ` X.121 address of rotary group。

[条件 C-2e57a01922e1291a](../../evidence/conditions-sets-018.md#c-2e57a01922e1291a) · [参数 P-8fd6d13a07f0de81](../../evidence/parameters-sets-011.md#p-8fd6d13a07f0de81) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027346

```text
(config)# x25 route <string> <cr>
```

Handler ` RVA 0x1060E300 `；selector ` 4 `；EOL ` RVA 0x34BC9590 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Destination address pattern to match。

[条件 C-5ba5d19a058528fd](../../evidence/conditions-sets-036.md#c-5ba5d19a058528fd) · [参数 P-46b33f6e5c389ad6](../../evidence/parameters-sets-006.md#p-46b33f6e5c389ad6) · [状态效果 S-db3de20dc56ef95a](../../evidence/state_effects-sets-046.md#s-db3de20dc56ef95a)

### path-060642

```text
(config)# x25 route input-interface <interface> <cr>
```

Handler ` RVA 0x1060E300 `；selector ` 4 `；EOL ` RVA 0x34BC9590 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3d3ecf954477693e](../../evidence/conditions-sets-024.md#c-3d3ecf954477693e) · [缺口 G-a79167c7ef6f787c](../../evidence/gaps-sets-006.md#g-a79167c7ef6f787c) · [参数 P-2533104316499092](../../evidence/parameters-sets-003.md#p-2533104316499092) · [状态效果 S-c2611c5f5eeb5fe8](../../evidence/state_effects-sets-041.md#s-c2611c5f5eeb5fe8)

### path-025940

```text
(config)# x25 routing <cr>
```

Handler ` RVA 0x1060DEC0 `；selector ` 2 `；EOL ` RVA 0x34BCBA28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029334

```text
(config)# xdr multicast-group internal issu-slots-split <cr>
```

Handler ` RVA 0x10CA8670 `；selector ` 0 `；EOL ` RVA 0x34CFCB68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-045061

```text
(config)# xdr multicast-group internal split threshold <number:1000..60000> <cr>
```

Handler ` RVA 0x10CA85A0 `；selector ` 0 `；EOL ` RVA 0x34CFC8D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Split threshold value (ms)。

[条件 C-0fc38ae52d0d8756](../../evidence/conditions-sets-006.md#c-0fc38ae52d0d8756) · [参数 P-3088d4612439b121](../../evidence/parameters-sets-004.md#p-3088d4612439b121) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029245

```text
(config)# xdr multicast-group mode individual <cr>
```

Handler ` RVA 0x10CA84E0 `；selector ` 0 `；EOL ` RVA 0x34CFC520 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-6fb58e63f1d5b4b3](../../evidence/state_effects-sets-024.md#s-6fb58e63f1d5b4b3)

### path-026109

```text
(config)# xot access-group <number:1..99> <cr>
```

Handler ` RVA 0x10652660 `；selector ` 0 `；EOL ` RVA 0x34BD8238 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` IP access list (standard)。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-14e02fcbbb8cf1f7](../../evidence/parameters-sets-002.md#p-14e02fcbbb8cf1f7) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-063107

```text
(config)# yang-interfaces aaa accounting disable <cr>
```

Handler ` RVA 0xDF978A0 `；selector ` 0 `；EOL ` 历史 VA 0x7FFFBAE64990 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c48c6b10aa671e69](../../evidence/conditions-sets-076.md#c-c48c6b10aa671e69) · [缺口 G-d9e9c59821520e36](../../evidence/gaps-sets-008.md#g-d9e9c59821520e36) · [状态效果 S-bb8b6010b65e5ece](../../evidence/state_effects-sets-040.md#s-bb8b6010b65e5ece)

### path-063108

```text
(config)# yang-interfaces aaa accounting disable <cr>
```

Handler ` RVA 0xDF978A0 `；selector ` 0 `；EOL ` 历史 VA 0x7FFF37EA88C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e4b4c1e1e4160b80](../../evidence/conditions-sets-088.md#c-e4b4c1e1e4160b80) · [缺口 G-689303b941088a50](../../evidence/gaps-sets-004.md#g-689303b941088a50) · [状态效果 S-87f7986e8088a29e](../../evidence/state_effects-sets-029.md#s-87f7986e8088a29e)

### path-063123

```text
(config)# yang-interfaces aaa authentication method-list <cr>
```

Handler ` RVA 0xDF978A0 `；selector ` 0 `；EOL ` 历史 VA 0x7FFF37EA8958 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6913eddc4394b4ca](../../evidence/conditions-sets-041.md#c-6913eddc4394b4ca) · [缺口 G-db7d6f4a1eb63027](../../evidence/gaps-sets-008.md#g-db7d6f4a1eb63027) · [状态效果 S-d0f39a41590944dc](../../evidence/state_effects-sets-044.md#s-d0f39a41590944dc)

### path-063147

```text
(config)# yang-interfaces aaa authentication method-list <string> <cr>
```

Handler ` RVA 0xDF978A0 `；selector ` 0 `；EOL ` 历史 VA 0x7FFF37E2F9E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Named method list。

[条件 C-eb69ba25a094eec6](../../evidence/conditions-sets-091.md#c-eb69ba25a094eec6) · [缺口 G-7184d2d6e7a29875](../../evidence/gaps-sets-004.md#g-7184d2d6e7a29875) · [参数 P-c368a5eaef1ebc7e](../../evidence/parameters-sets-015.md#p-c368a5eaef1ebc7e) · [状态效果 S-d57206584c7ea80e](../../evidence/state_effects-sets-045.md#s-d57206584c7ea80e)

### path-063148

```text
(config)# yang-interfaces aaa authentication method-list <string> <cr>
```

Handler ` RVA 0xDF978A0 `；selector ` 0 `；EOL ` 历史 VA 0x7FFFBAEDD300 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Named method list。

[条件 C-22218f3890099543](../../evidence/conditions-sets-013.md#c-22218f3890099543) · [缺口 G-d047c5bc09700c1d](../../evidence/gaps-sets-007.md#g-d047c5bc09700c1d) · [参数 P-c368a5eaef1ebc7e](../../evidence/parameters-sets-015.md#p-c368a5eaef1ebc7e) · [状态效果 S-c8d281fc31c96713](../../evidence/state_effects-sets-043.md#s-c8d281fc31c96713)

### path-063125

```text
(config)# yang-interfaces aaa authorization method-list <cr>
```

Handler ` RVA 0xDF978A0 `；selector ` 0 `；EOL ` 历史 VA 0x7FFF37EA8B98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a99b6b232205ad4a](../../evidence/conditions-sets-065.md#c-a99b6b232205ad4a) · [缺口 G-b22939901134686f](../../evidence/gaps-sets-006.md#g-b22939901134686f) · [状态效果 S-4af6e66b3f891a9a](../../evidence/state_effects-sets-016.md#s-4af6e66b3f891a9a)

### path-063152

```text
(config)# yang-interfaces aaa authorization method-list <string> <cr>
```

Handler ` RVA 0xDF978A0 `；selector ` 0 `；EOL ` 历史 VA 0x7FFF37E2DA50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Named method list。

[条件 C-d681886b04dc7ad4](../../evidence/conditions-sets-083.md#c-d681886b04dc7ad4) · [缺口 G-a982825ff130d95c](../../evidence/gaps-sets-006.md#g-a982825ff130d95c) · [参数 P-0e08fd669eeab8f8](../../evidence/parameters-sets-002.md#p-0e08fd669eeab8f8) · [状态效果 S-daa21054aae0d3d5](../../evidence/state_effects-sets-046.md#s-daa21054aae0d3d5)

### path-063153

```text
(config)# yang-interfaces aaa authorization method-list <string> <cr>
```

Handler ` RVA 0xDF978A0 `；selector ` 0 `；EOL ` 历史 VA 0x7FFFBAEDD540 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Named method list。

[条件 C-c2dc4b9cf4d5695b](../../evidence/conditions-sets-075.md#c-c2dc4b9cf4d5695b) · [缺口 G-073ed55c16a65bed](../../evidence/gaps-sets-001.md#g-073ed55c16a65bed) · [参数 P-0e08fd669eeab8f8](../../evidence/parameters-sets-002.md#p-0e08fd669eeab8f8) · [状态效果 S-e3551ec511d4f821](../../evidence/state_effects-sets-048.md#s-e3551ec511d4f821)

### path-063042

```text
(config)# yang-interfaces feature atomic-config <cr>
```

Handler ` RVA 0xDF978A0 `；selector ` 0 `；EOL ` 历史 VA 0x7FFFBAE5D900 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c6c97823c4dfd7f9](../../evidence/conditions-sets-077.md#c-c6c97823c4dfd7f9) · [缺口 G-9a03a11dad5cfce7](../../evidence/gaps-sets-006.md#g-9a03a11dad5cfce7) · [状态效果 S-fb70d7d5151ec108](../../evidence/state_effects-sets-053.md#s-fb70d7d5151ec108)

### path-063043

```text
(config)# yang-interfaces feature atomic-config <cr>
```

Handler ` RVA 0xDF978A0 `；selector ` 0 `；EOL ` 历史 VA 0x7FFF37EA90A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-fb094a3767860537](../../evidence/conditions-sets-097.md#c-fb094a3767860537) · [缺口 G-0e751671760dcaec](../../evidence/gaps-sets-001.md#g-0e751671760dcaec) · [状态效果 S-f8ff11fffff8f9b5](../../evidence/state_effects-sets-053.md#s-f8ff11fffff8f9b5)

### path-063116

```text
(config)# yang-interfaces feature deprecated disable <cr>
```

Handler ` RVA 0xDF978A0 `；selector ` 0 `；EOL ` 历史 VA 0x7FFF37E29EB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4355b53db6f5aff9](../../evidence/conditions-sets-026.md#c-4355b53db6f5aff9) · [缺口 G-d3f3f7259ed4ae05](../../evidence/gaps-sets-007.md#g-d3f3f7259ed4ae05) · [状态效果 S-d0bc2bf3079b36c6](../../evidence/state_effects-sets-044.md#s-d0bc2bf3079b36c6)

### path-063117

```text
(config)# yang-interfaces feature deprecated disable <cr>
```

Handler ` RVA 0xDF978A0 `；selector ` 0 `；EOL ` 历史 VA 0x7FFFBAEDD8A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5723854e4d726bf6](../../evidence/conditions-sets-034.md#c-5723854e4d726bf6) · [缺口 G-152dd7f9cd577292](../../evidence/gaps-sets-001.md#g-152dd7f9cd577292) · [状态效果 S-c35e9c3aeaff069d](../../evidence/state_effects-sets-041.md#s-c35e9c3aeaff069d)

### path-063121

```text
(config)# yang-interfaces feature deprecated enable <cr>
```

Handler ` RVA 0xDF978A0 `；selector ` 0 `；EOL ` 历史 VA 0x7FFF37E28D00 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a1e33402c1ccf579](../../evidence/conditions-sets-063.md#c-a1e33402c1ccf579) · [缺口 G-b04f3b22778c8e18](../../evidence/gaps-sets-006.md#g-b04f3b22778c8e18) · [状态效果 S-561364bf8a245da8](../../evidence/state_effects-sets-019.md#s-561364bf8a245da8)

### path-063122

```text
(config)# yang-interfaces feature deprecated enable <cr>
```

Handler ` RVA 0xDF978A0 `；selector ` 0 `；EOL ` 历史 VA 0x7FFF37EA9018 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8915617cd0537b88](../../evidence/conditions-sets-053.md#c-8915617cd0537b88) · [缺口 G-3bab404eb1ecaf7b](../../evidence/gaps-sets-003.md#g-3bab404eb1ecaf7b) · [状态效果 S-0c13e00e566c0300](../../evidence/state_effects-sets-003.md#s-0c13e00e566c0300)

### path-063036

```text
(config)# yang-interfaces high-scale-paths <number:0..4294967295> <cr>
```

Handler ` RVA 0xDF978A0 `；selector ` 0 `；EOL ` 历史 VA 0x7FFFBAE5EB18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Query path index。

[条件 C-d7ebbb3035975d2f](../../evidence/conditions-sets-083.md#c-d7ebbb3035975d2f) · [缺口 G-7272192cb50fdfee](../../evidence/gaps-sets-004.md#g-7272192cb50fdfee) · [参数 P-10bc77a542fff3e9](../../evidence/parameters-sets-002.md#p-10bc77a542fff3e9) · [状态效果 S-a69b8c99a6301a37](../../evidence/state_effects-sets-035.md#s-a69b8c99a6301a37)

### path-063037

```text
(config)# yang-interfaces high-scale-paths <number:0..4294967295> <cr>
```

Handler ` RVA 0xDF978A0 `；selector ` 0 `；EOL ` 历史 VA 0x7FFFBAE5EE30 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Query path index。

[条件 C-1b8144a24d246969](../../evidence/conditions-sets-011.md#c-1b8144a24d246969) · [缺口 G-fd33c24357035f16](../../evidence/gaps-sets-009.md#g-fd33c24357035f16) · [参数 P-10bc77a542fff3e9](../../evidence/parameters-sets-002.md#p-10bc77a542fff3e9) · [状态效果 S-9765b2f1e954ab61](../../evidence/state_effects-sets-032.md#s-9765b2f1e954ab61)

### path-060629

```text
(config)# <?dumper_command_func@555589e561d0> x29 access-list <number:1..500> <cr>
```

Handler ` RVA 0xFE71180 `；selector ` 2 `；EOL ` RVA 0x349023B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Access list number。

[条件 C-2c2494611a0cb8ce](../../evidence/conditions-sets-017.md#c-2c2494611a0cb8ce) · [缺口 G-a4bfb0c692ded5a3](../../evidence/gaps-sets-006.md#g-a4bfb0c692ded5a3) · [参数 P-a4f8f2fa5c8ddab1](../../evidence/parameters-sets-013.md#p-a4f8f2fa5c8ddab1) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060627

```text
(config)# <?dumper_command_func@555589e561d0> x29 inviteclear-time <number:5..2147483> <cr>
```

Handler ` RVA 0xFE71180 `；selector ` 3 `；EOL ` RVA 0x34902788 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Time in seconds。

[条件 C-f6a5ddc2fe5df49d](../../evidence/conditions-sets-095.md#c-f6a5ddc2fe5df49d) · [缺口 G-a4bfb0c692ded5a3](../../evidence/gaps-sets-006.md#g-a4bfb0c692ded5a3) · [参数 P-134fc7f0d493ea1e](../../evidence/parameters-sets-002.md#p-134fc7f0d493ea1e) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060636

```text
(config)# <?dumper_command_func@555589e561d0> x29 profile default <cr>
```

Handler ` RVA 0xFE71180 `；selector ` 1 `；EOL ` RVA 0x34902B88 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-117b09569248c074](../../evidence/conditions-sets-007.md#c-117b09569248c074) · [缺口 G-a4bfb0c692ded5a3](../../evidence/gaps-sets-006.md#g-a4bfb0c692ded5a3) · [状态效果 S-bb475a84f5896b3a](../../evidence/state_effects-sets-040.md#s-bb475a84f5896b3a)

### path-060794

```text
(config)# <?test_subsys_action@555589bbb158> dialer clid group <string> <cr>
```

Handler ` RVA 0xF4DBD30 `；selector ` 0 `；EOL ` RVA 0x34675848 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Name of the CLID group。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [缺口 G-63eda40e9deb2468](../../evidence/gaps-sets-004.md#g-63eda40e9deb2468) · [参数 P-f129087404074886](../../evidence/parameters-sets-018.md#p-f129087404074886) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060790

```text
(config)# <?test_subsys_action@555589bbb158> dialer dnis group <string> <cr>
```

Handler ` RVA 0xF4DB800 `；selector ` 0 `；EOL ` RVA 0x34675500 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Name of the DNIS group。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [缺口 G-63eda40e9deb2468](../../evidence/gaps-sets-004.md#g-63eda40e9deb2468) · [参数 P-41d2968749edb1cd](../../evidence/parameters-sets-006.md#p-41d2968749edb1cd) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060554

```text
(config)# <?test_subsys_action@555589bbb158> dialer watch-list <number:1..255> <cr>
```

Handler ` RVA 0xF48A010 `；selector ` 0 `；EOL ` RVA 0x346606D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Dialer watch group number。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [缺口 G-63eda40e9deb2468](../../evidence/gaps-sets-004.md#g-63eda40e9deb2468) · [参数 P-b6b483796af986e9](../../evidence/parameters-sets-014.md#p-b6b483796af986e9) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060391

```text
(config)# <?test_subsys_action@555589bbb158> dialer-list <number:1..128> <cr>
```

Handler ` RVA 0xF4C85C0 `；selector ` 1 `；EOL ` RVA 0x34668BD8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Dialer group number。

[条件 C-d4f26c18bf4a9cda](../../evidence/conditions-sets-082.md#c-d4f26c18bf4a9cda) · [缺口 G-63eda40e9deb2468](../../evidence/gaps-sets-004.md#g-63eda40e9deb2468) · [参数 P-710e6120e4abc011](../../evidence/parameters-sets-009.md#p-710e6120e4abc011) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060798

```text
(config)# <?test_subsys_action@555589bbb158> dialer-list <number:1..128> protocol ip <cr>
```

Handler ` RVA 0xF4C85C0 `；selector ` 2 `；EOL ` RVA 0x34667D68 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Dialer group number。

[条件 C-189d84dc8b1ff9d5](../../evidence/conditions-sets-010.md#c-189d84dc8b1ff9d5) · [缺口 G-63eda40e9deb2468](../../evidence/gaps-sets-004.md#g-63eda40e9deb2468) · [参数 P-710e6120e4abc011](../../evidence/parameters-sets-009.md#p-710e6120e4abc011) · [状态效果 S-23f290acad0b3f66](../../evidence/state_effects-sets-008.md#s-23f290acad0b3f66)

### path-061253

```text
(config)# <?test_subsys_action@555589bbb158> dialer-list <number:1..128> protocol ip deny <cr>
```

Handler ` RVA 0xF4C85C0 `；selector ` 2 `；EOL ` RVA 0x34667640 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Dialer group number。

[条件 C-a6daa9534bad401c](../../evidence/conditions-sets-064.md#c-a6daa9534bad401c) · [缺口 G-63eda40e9deb2468](../../evidence/gaps-sets-004.md#g-63eda40e9deb2468) · [参数 P-710e6120e4abc011](../../evidence/parameters-sets-009.md#p-710e6120e4abc011) · [状态效果 S-0b6baeb3880a8941](../../evidence/state_effects-sets-003.md#s-0b6baeb3880a8941)
