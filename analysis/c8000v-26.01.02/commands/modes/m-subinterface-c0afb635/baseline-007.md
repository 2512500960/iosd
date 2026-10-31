# subinterface · 六个基础模式的历史连接

[模式索引](README.md) · [总索引](../../README.md)

### path-068598

```text
(config-subif)# ipv6 mfib-cef <cr>
```

Handler ` RVA 0x11904EB0 `；selector ` 2147483656 `；EOL ` RVA 0x3553FE50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-96d9b597753adceb](../../evidence/conditions-sets-058.md#c-96d9b597753adceb) · [状态效果 S-bf1dda9d69499b19](../../evidence/state_effects-sets-040.md#s-bf1dda9d69499b19)

### path-071224

```text
(config-subif)# ipv6 mld access-group <number:1..199> <cr>
```

Handler ` RVA 0x115D9A40 `；selector ` 15 `；EOL ` RVA 0x35547678 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Access list specifying tracking group range。

[条件 C-76b97fef04f24cf7](../../evidence/conditions-sets-046.md#c-76b97fef04f24cf7) · [参数 P-f3eed89abfc4c58f](../../evidence/parameters-sets-018.md#p-f3eed89abfc4c58f) · [状态效果 S-88848ca4aa030eeb](../../evidence/state_effects-sets-029.md#s-88848ca4aa030eeb)

### path-069921

```text
(config-subif)# ipv6 mld explicit-tracking <cr>
```

Handler ` RVA 0x115D9A40 `；selector ` 12 `；EOL ` RVA 0x35546320 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8f1617a4019cef62](../../evidence/conditions-sets-055.md#c-8f1617a4019cef62) · [状态效果 S-88848ca4aa030eeb](../../evidence/state_effects-sets-029.md#s-88848ca4aa030eeb)

### path-071240

```text
(config-subif)# ipv6 mld join-group <address> <cr>
```

Handler ` RVA 0x115D9A40 `；selector ` 13 `；EOL ` RVA 0x35546788 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP group address。

[条件 C-deb56e49a842e6d5](../../evidence/conditions-sets-086.md#c-deb56e49a842e6d5) · [参数 P-c739a29c9927ee1e](../../evidence/parameters-sets-015.md#p-c739a29c9927ee1e) · [状态效果 S-88848ca4aa030eeb](../../evidence/state_effects-sets-029.md#s-88848ca4aa030eeb)

### path-071236

```text
(config-subif)# ipv6 mld limit <number:1..64000> <cr>
```

Handler ` RVA 0x115D9A40 `；selector ` 21 `；EOL ` RVA 0x35547AA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Max Allowed State on this interface。

[条件 C-110d50cd9f91f3ff](../../evidence/conditions-sets-007.md#c-110d50cd9f91f3ff) · [参数 P-437a0871723d4bb2](../../evidence/parameters-sets-006.md#p-437a0871723d4bb2) · [状态效果 S-88848ca4aa030eeb](../../evidence/state_effects-sets-029.md#s-88848ca4aa030eeb)

### path-071137

```text
(config-subif)# ipv6 mld query-interval <number:1..3600> <cr>
```

Handler ` RVA 0x115D9A40 `；selector ` 10 `；EOL ` RVA 0x35545CC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Query interval in seconds。

[条件 C-0efd79419160778a](../../evidence/conditions-sets-006.md#c-0efd79419160778a) · [参数 P-556cfd6545b29eb8](../../evidence/parameters-sets-007.md#p-556cfd6545b29eb8) · [状态效果 S-88848ca4aa030eeb](../../evidence/state_effects-sets-029.md#s-88848ca4aa030eeb)

### path-071097

```text
(config-subif)# ipv6 mld query-max-response-time <number:1..12> <cr>
```

Handler ` RVA 0x115D9A40 `；selector ` 8 `；EOL ` RVA 0x35545188 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` query response value in seconds。

[条件 C-af935d53f03b303a](../../evidence/conditions-sets-068.md#c-af935d53f03b303a) · [参数 P-372a6c42b0b4328c](../../evidence/parameters-sets-005.md#p-372a6c42b0b4328c) · [状态效果 S-88848ca4aa030eeb](../../evidence/state_effects-sets-029.md#s-88848ca4aa030eeb)

### path-071118

```text
(config-subif)# ipv6 mld query-timeout <number:1..18006> <cr>
```

Handler ` RVA 0x115D9A40 `；selector ` 9 `；EOL ` RVA 0x35545560 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` timeout value in seconds 。

[条件 C-f45578b5183b131a](../../evidence/conditions-sets-094.md#c-f45578b5183b131a) · [参数 P-8a6c5d96ecec8347](../../evidence/parameters-sets-011.md#p-8a6c5d96ecec8347) · [状态效果 S-88848ca4aa030eeb](../../evidence/state_effects-sets-029.md#s-88848ca4aa030eeb)

### path-071136

```text
(config-subif)# ipv6 mld robustness-variable <number:1..7> <cr>
```

Handler ` RVA 0x115D9A40 `；selector ` 22 `；EOL ` RVA 0x35545978 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` robustness value。

[条件 C-bfdf05db8ac3c726](../../evidence/conditions-sets-074.md#c-bfdf05db8ac3c726) · [参数 P-81627382e0291ff6](../../evidence/parameters-sets-010.md#p-81627382e0291ff6) · [状态效果 S-88848ca4aa030eeb](../../evidence/state_effects-sets-029.md#s-88848ca4aa030eeb)

### path-069873

```text
(config-subif)# ipv6 mld router <cr>
```

Handler ` RVA 0x115D9A40 `；selector ` 11 `；EOL ` RVA 0x35545FF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-13e54603bddd202e](../../evidence/conditions-sets-008.md#c-13e54603bddd202e) · [状态效果 S-88848ca4aa030eeb](../../evidence/state_effects-sets-029.md#s-88848ca4aa030eeb)

### path-071250

```text
(config-subif)# ipv6 mld static-group <address> <cr>
```

Handler ` RVA 0x115D9A40 `；selector ` 14 `；EOL ` RVA 0x35546F20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP group address。

[条件 C-92b0caf7ae555224](../../evidence/conditions-sets-057.md#c-92b0caf7ae555224) · [参数 P-278b15b69a495932](../../evidence/parameters-sets-003.md#p-278b15b69a495932) · [状态效果 S-88848ca4aa030eeb](../../evidence/state_effects-sets-029.md#s-88848ca4aa030eeb)

### path-071241

```text
(config-subif)# ipv6 mld v2-report-type <number:133..255> <cr>
```

Handler ` RVA 0x115D9A40 `；selector ` 16 `；EOL ` RVA 0x35547F78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` MLDv2 Report Type。

[条件 C-16b2044a857e2753](../../evidence/conditions-sets-009.md#c-16b2044a857e2753) · [参数 P-05c1ee0928919f3e](../../evidence/parameters-sets-001.md#p-05c1ee0928919f3e) · [状态效果 S-88848ca4aa030eeb](../../evidence/state_effects-sets-029.md#s-88848ca4aa030eeb)

### path-071050

```text
(config-subif)# ipv6 mld version <number:1..2> <cr>
```

Handler ` RVA 0x115D9A40 `；selector ` 7 `；EOL ` RVA 0x35544E38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` version number。

[条件 C-03775a2dee6f09a5](../../evidence/conditions-sets-002.md#c-03775a2dee6f09a5) · [参数 P-ac74361bdcf18c4e](../../evidence/parameters-sets-013.md#p-ac74361bdcf18c4e) · [状态效果 S-88848ca4aa030eeb](../../evidence/state_effects-sets-029.md#s-88848ca4aa030eeb)

### path-070922

```text
(config-subif)# ipv6 mode host unicast <cr>
```

Handler ` RVA 0x12307660 `；selector ` 0 `；EOL ` RVA 0x35590950 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-96d9b597753adceb](../../evidence/conditions-sets-058.md#c-96d9b597753adceb) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-072576

```text
(config-subif)# ipv6 mtu <number:dynamic> <cr>
```

Handler ` RVA 0x12300EC0 `；selector ` 0 `；EOL ` RVA 0x357E0AF0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` MTU (bytes)。

[条件 C-12047be687d35a39](../../evidence/conditions-sets-007.md#c-12047be687d35a39) · [缺口 G-b655f75ee3fabd8d](../../evidence/gaps-sets-006.md#g-b655f75ee3fabd8d) · [参数 P-a516f4d3e5eeca22](../../evidence/parameters-sets-013.md#p-a516f4d3e5eeca22) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-072335

```text
(config-subif)# ipv6 multicast aaa accounting receive <number:1..199> <cr>
```

Handler ` RVA 0xC49F730 `；selector ` 1000 `；EOL ` RVA 0x355346A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Standard or Extended IP access list number。

[条件 C-cee11bb62e4498df](../../evidence/conditions-sets-080.md#c-cee11bb62e4498df) · [参数 P-fe7a81e759633a6e](../../evidence/parameters-sets-019.md#p-fe7a81e759633a6e) · [状态效果 S-0d9f180e823fc08d](../../evidence/state_effects-sets-003.md#s-0d9f180e823fc08d)

### path-071824

```text
(config-subif)# ipv6 multicast boundary block source <cr>
```

Handler ` RVA 0x118E5110 `；selector ` 0 `；EOL ` RVA 0x355374C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2903dc8da001675f](../../evidence/conditions-sets-016.md#c-2903dc8da001675f) · [状态效果 S-9347f4b7d655695d](../../evidence/state_effects-sets-031.md#s-9347f4b7d655695d)

### path-071919

```text
(config-subif)# ipv6 multicast limit <string> <number:0..2147483647> <cr>
```

Handler ` RVA 0x11725A80 `；selector ` 29 `；EOL ` RVA 0x35537A88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Named Access list；` unsigned_number ` Max allowed state on this interface。

[条件 C-7472c9cc2200a1fc](../../evidence/conditions-sets-045.md#c-7472c9cc2200a1fc) · [参数 P-cc91952d0ef80a51](../../evidence/parameters-sets-015.md#p-cc91952d0ef80a51) · [状态效果 S-799a4f8652cb2844](../../evidence/state_effects-sets-026.md#s-799a4f8652cb2844)

### path-069913

```text
(config-subif)# ipv6 nd advertisement-interval <cr>
```

Handler ` RVA 0x123186C0 `；selector ` 0 `；EOL ` RVA 0x35596208 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-71accf15d7fe95eb](../../evidence/conditions-sets-044.md#c-71accf15d7fe95eb) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-070956

```text
(config-subif)# ipv6 nd autoconfig default-route <cr>
```

Handler ` RVA 0x12316680 `；selector ` 0 `；EOL ` RVA 0x35801E60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-71accf15d7fe95eb](../../evidence/conditions-sets-044.md#c-71accf15d7fe95eb) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-070940

```text
(config-subif)# ipv6 nd autoconfig prefix <cr>
```

Handler ` RVA 0x12316550 `；selector ` 0 `；EOL ` RVA 0x35801BB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-71accf15d7fe95eb](../../evidence/conditions-sets-044.md#c-71accf15d7fe95eb) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-071895

```text
(config-subif)# ipv6 nd cache expire <number:1..65536> <cr>
```

Handler ` RVA 0x12318C80 `；selector ` 0 `；EOL ` RVA 0x35803D98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Expiry time (seconds)。

[条件 C-5c0ef038d834e0ba](../../evidence/conditions-sets-036.md#c-5c0ef038d834e0ba) · [参数 P-8b5ed5b24df248ef](../../evidence/parameters-sets-011.md#p-8b5ed5b24df248ef) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-071882

```text
(config-subif)# ipv6 nd cache interface-limit <number:1..4294967295> <cr>
```

Handler ` RVA 0x12318930 `；selector ` 0 `；EOL ` RVA 0x358039D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of entries。

[条件 C-b34b774109a1e017](../../evidence/conditions-sets-069.md#c-b34b774109a1e017) · [参数 P-996c65d5e7bb1251](../../evidence/parameters-sets-012.md#p-996c65d5e7bb1251) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-069532

```text
(config-subif)# ipv6 nd dad attempts <number:0..600> <cr>
```

Handler ` RVA 0x123169E0 `；selector ` 0 `；EOL ` RVA 0x35800A98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of attempts。

[条件 C-7aa321ecc3a4b1bd](../../evidence/conditions-sets-048.md#c-7aa321ecc3a4b1bd) · [参数 P-404f371847e8f59f](../../evidence/parameters-sets-005.md#p-404f371847e8f59f) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-071785

```text
(config-subif)# ipv6 nd dad loopback detect <cr>
```

Handler ` RVA 0x12318F30 `；selector ` 0 `；EOL ` RVA 0x35801080 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-71accf15d7fe95eb](../../evidence/conditions-sets-044.md#c-71accf15d7fe95eb) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-069553

```text
(config-subif)# ipv6 nd dad time <number:1..6000> <cr>
```

Handler ` RVA 0x12319180 `；selector ` 0 `；EOL ` RVA 0x35800B00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` time (milliseconds)。

[条件 C-672752d84a3cf0c2](../../evidence/conditions-sets-040.md#c-672752d84a3cf0c2) · [参数 P-b1ced6041ac8147a](../../evidence/parameters-sets-013.md#p-b1ced6041ac8147a) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-069549

```text
(config-subif)# ipv6 nd dad-proxy <cr>
```

Handler ` RVA 0x136B2510 `；selector ` 1701 `；EOL ` RVA 0x35C04EC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-267f2ac22523aa92](../../evidence/conditions-sets-015.md#c-267f2ac22523aa92) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-069550

```text
(config-subif)# ipv6 nd destination-guard <cr>
```

Handler ` RVA 0x123162D0 `；selector ` 0 `；EOL ` RVA 0x35801330 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-71accf15d7fe95eb](../../evidence/conditions-sets-044.md#c-71accf15d7fe95eb) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-069864

```text
(config-subif)# ipv6 nd managed-config-flag <cr>
```

Handler ` RVA 0x123182A0 `；selector ` 0 `；EOL ` RVA 0x35595898 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-71accf15d7fe95eb](../../evidence/conditions-sets-044.md#c-71accf15d7fe95eb) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-070924

```text
(config-subif)# ipv6 nd na glean <cr>
```

Handler ` RVA 0x12316190 `；selector ` 0 `；EOL ` RVA 0x358018E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-71accf15d7fe95eb](../../evidence/conditions-sets-044.md#c-71accf15d7fe95eb) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-068551

```text
(config-subif)# ipv6 nd ns-interval <number:1000..172800000> <cr>
```

Handler ` RVA 0x123167B0 `；selector ` 0 `；EOL ` RVA 0x35800558 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Retransmission interval in milliseconds。

[条件 C-84a75cfd7f900609](../../evidence/conditions-sets-051.md#c-84a75cfd7f900609) · [参数 P-7689f19b6ecf43a7](../../evidence/parameters-sets-009.md#p-7689f19b6ecf43a7) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-071210

```text
(config-subif)# ipv6 nd nud igp <cr>
```

Handler ` RVA 0x12315760 `；selector ` 0 `；EOL ` RVA 0x35596518 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-71accf15d7fe95eb](../../evidence/conditions-sets-044.md#c-71accf15d7fe95eb) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-072709

```text
(config-subif)# ipv6 nd nud retry <number:1..3> <number:1000..32000> <?number_help_func_action@55558aaea8d0> <cr>
```

Handler ` RVA 0x12315510 `；selector ` 0 `；EOL ` RVA 0x35596860 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Base；` unsigned_number ` Interval (milliseconds)。

[条件 C-9af21b187d914c57](../../evidence/conditions-sets-060.md#c-9af21b187d914c57) · [缺口 G-2fc002397084fe12](../../evidence/gaps-sets-002.md#g-2fc002397084fe12) · [参数 P-14f9b28d76c800f6](../../evidence/parameters-sets-002.md#p-14f9b28d76c800f6) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-069880

```text
(config-subif)# ipv6 nd other-config-flag <cr>
```

Handler ` RVA 0x12318470 `；selector ` 0 `；EOL ` RVA 0x35595B40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-71accf15d7fe95eb](../../evidence/conditions-sets-044.md#c-71accf15d7fe95eb) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-069574

```text
(config-subif)# ipv6 nd packet-priority <cr>
```

Handler ` RVA 0x12316410 `；selector ` 0 `；EOL ` RVA 0x358015D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-71accf15d7fe95eb](../../evidence/conditions-sets-044.md#c-71accf15d7fe95eb) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-072629

```text
(config-subif)# ipv6 nd prefix <prefix:dynamic> <cr>
```

Handler ` RVA 0x12316BC0 `；selector ` 0 `；EOL ` RVA 0x35594620 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` IPv6 prefix x:x::y/&lt;z&gt;。

[条件 C-c41ca4e9f663aac2](../../evidence/conditions-sets-076.md#c-c41ca4e9f663aac2) · [缺口 G-749f6dd8d11fce6a](../../evidence/gaps-sets-004.md#g-749f6dd8d11fce6a) · [参数 P-c4b5c5ea00be763b](../../evidence/parameters-sets-015.md#p-c4b5c5ea00be763b) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-071313

```text
(config-subif)# ipv6 nd prefix default <cr>
```

Handler ` RVA 0x12316BC0 `；selector ` 0 `；EOL ` RVA 0x35594620 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6f56079c50a65065](../../evidence/conditions-sets-043.md#c-6f56079c50a65065) · [状态效果 S-bec97c0d535423ca](../../evidence/state_effects-sets-040.md#s-bec97c0d535423ca)

### path-071094

```text
(config-subif)# ipv6 nd prefix framed-ipv6-prefix <cr>
```

Handler ` RVA 0x12317870 `；selector ` 0 `；EOL ` RVA 0x35594278 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-71accf15d7fe95eb](../../evidence/conditions-sets-044.md#c-71accf15d7fe95eb) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-072672

```text
(config-subif)# ipv6 nd prefix-advertisement <prefix:dynamic> <number:0..4294967295> <cr>
```

Handler ` RVA 0x12316BC0 `；selector ` 0 `；EOL ` RVA 0x35595348 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` IPv6 prefix x:x::y/&lt;z&gt;；` unsigned_number ` Valid Lifetime (secs)。

[条件 C-71c62214259df0cd](../../evidence/conditions-sets-044.md#c-71c62214259df0cd) · [缺口 G-dc3152d9dc2ca1dc](../../evidence/gaps-sets-008.md#g-dc3152d9dc2ca1dc) · [参数 P-76630020318500b1](../../evidence/parameters-sets-009.md#p-76630020318500b1) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-072355

```text
(config-subif)# ipv6 nd ra dns server <address> <cr>
```

Handler ` RVA 0x12313A50 `；selector ` 0 `；EOL ` RVA 0x35598FF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IPv6 address。

[条件 C-ecb7fdb34a3751ad](../../evidence/conditions-sets-091.md#c-ecb7fdb34a3751ad) · [参数 P-46aa98178c382743](../../evidence/parameters-sets-006.md#p-46aa98178c382743) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-072710

```text
(config-subif)# ipv6 nd ra dns server <address> <number:dynamic> <cr>
```

Handler ` RVA 0x12313A50 `；selector ` 0 `；EOL ` RVA 0x35598FF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` IPv6 address；` unsigned_number_dynamic ` Lifetime (seconds)。

[条件 C-ef51e93ca9a921c2](../../evidence/conditions-sets-092.md#c-ef51e93ca9a921c2) · [缺口 G-5b93e93aa34af446](../../evidence/gaps-sets-004.md#g-5b93e93aa34af446) · [参数 P-3a6d44130855fa43](../../evidence/parameters-sets-005.md#p-3a6d44130855fa43) · [状态效果 S-779fbaa53e9cce44](../../evidence/state_effects-sets-025.md#s-779fbaa53e9cce44)

### path-072354

```text
(config-subif)# ipv6 nd ra dns-search-list domain <string> <cr>
```

Handler ` RVA 0x123141C0 `；selector ` 0 `；EOL ` RVA 0x35598AF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` domain-name。

[条件 C-8d7d7108ac8ad50d](../../evidence/conditions-sets-055.md#c-8d7d7108ac8ad50d) · [参数 P-aa6f57fb2b935d74](../../evidence/parameters-sets-013.md#p-aa6f57fb2b935d74) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-072712

```text
(config-subif)# ipv6 nd ra dns-search-list domain <string> lifetime <number:dynamic> <cr>
```

Handler ` RVA 0x123141C0 `；selector ` 0 `；EOL ` RVA 0x35598AF0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` domain-name；` unsigned_number_dynamic ` Lifetime (seconds)。

[条件 C-08b13c2be0b95dc4](../../evidence/conditions-sets-004.md#c-08b13c2be0b95dc4) · [缺口 G-26cbd374f977e8d6](../../evidence/gaps-sets-002.md#g-26cbd374f977e8d6) · [参数 P-2cd53ee9311ed661](../../evidence/parameters-sets-004.md#p-2cd53ee9311ed661) · [状态效果 S-7ed93028d0f0e321](../../evidence/state_effects-sets-027.md#s-7ed93028d0f0e321)

### path-071958

```text
(config-subif)# ipv6 nd ra hop-limit unspecified <cr>
```

Handler ` RVA 0x12317F30 `；selector ` 0 `；EOL ` RVA 0x35596F68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-71accf15d7fe95eb](../../evidence/conditions-sets-044.md#c-71accf15d7fe95eb) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-072052

```text
(config-subif)# ipv6 nd ra initial <number:1..64> <cr>
```

Handler ` RVA 0x12314BB0 `；selector ` 0 `；EOL ` RVA 0x355993F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Initial count。

[条件 C-0f6f91d1fa4eaef2](../../evidence/conditions-sets-006.md#c-0f6f91d1fa4eaef2) · [参数 P-124596d158362e5a](../../evidence/parameters-sets-002.md#p-124596d158362e5a) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-072836

```text
(config-subif)# ipv6 nd ra interval <?number_help_func_action@55558aaebc98> <?number_help_func_action@55558aaebce8> <cr>
```

Handler ` RVA 0x12314E10 `；selector ` 0 `；EOL ` RVA 0x35597C70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c8c7302f74e8bd50](../../evidence/conditions-sets-077.md#c-c8c7302f74e8bd50) · [缺口 G-5e1102fbc2d4f429](../../evidence/gaps-sets-004.md#g-5e1102fbc2d4f429) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-072676

```text
(config-subif)# ipv6 nd ra lifetime <number:dynamic> <cr>
```

Handler ` RVA 0x12313580 `；selector ` 0 `；EOL ` RVA 0x35597920 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` RA Lifetime (seconds)。

[条件 C-01cffd8b0d0171a0](../../evidence/conditions-sets-001.md#c-01cffd8b0d0171a0) · [缺口 G-0ca52879930f0599](../../evidence/gaps-sets-001.md#g-0ca52879930f0599) · [参数 P-8352928b2d8e938f](../../evidence/parameters-sets-010.md#p-8352928b2d8e938f) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-071955

```text
(config-subif)# ipv6 nd ra mtu suppress <cr>
```

Handler ` RVA 0x123180C0 `；selector ` 0 `；EOL ` RVA 0x35596C70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-71accf15d7fe95eb](../../evidence/conditions-sets-044.md#c-71accf15d7fe95eb) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-072680

```text
(config-subif)# ipv6 nd ra nat64-prefix <prefix:dynamic> <cr>
```

Handler ` RVA 0x12313D50 `；selector ` 0 `；EOL ` RVA 0x35598088 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` IPv6 prefix x:x::y/&lt;z&gt;。

[条件 C-dacfe4cb97e3fe83](../../evidence/conditions-sets-084.md#c-dacfe4cb97e3fe83) · [缺口 G-0d74fb64ebdea81a](../../evidence/gaps-sets-001.md#g-0d74fb64ebdea81a) · [参数 P-2e8fad8c9e8419fc](../../evidence/parameters-sets-004.md#p-2e8fad8c9e8419fc) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-071963

```text
(config-subif)# ipv6 nd ra solicited unicast <cr>
```

Handler ` RVA 0x12317AF0 `；selector ` 0 `；EOL ` RVA 0x35597260 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-71accf15d7fe95eb](../../evidence/conditions-sets-044.md#c-71accf15d7fe95eb) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-072681

```text
(config-subif)# ipv6 nd ra specific-route <prefix:dynamic> <cr>
```

Handler ` RVA 0x12314530 `；selector ` 0 `；EOL ` RVA 0x355984A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` IPv6 prefix x:x::y/&lt;z&gt;。

[条件 C-c72bb91d272de048](../../evidence/conditions-sets-077.md#c-c72bb91d272de048) · [缺口 G-32ed5c5ff9760037](../../evidence/gaps-sets-002.md#g-32ed5c5ff9760037) · [参数 P-a3862d4104529928](../../evidence/parameters-sets-012.md#p-a3862d4104529928) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-071301

```text
(config-subif)# ipv6 nd ra suppress <cr>
```

Handler ` RVA 0x12317C20 `；selector ` 0 `；EOL ` RVA 0x355975B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-71accf15d7fe95eb](../../evidence/conditions-sets-044.md#c-71accf15d7fe95eb) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-072669

```text
(config-subif)# ipv6 nd ra-interval <number:4..1800> <?number_help_func_action@55558aae7bf0> <cr>
```

Handler ` RVA 0x12314E10 `；selector ` 0 `；EOL ` RVA 0x35593B50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` RA Interval (sec)。

[条件 C-11873bfd2941c9e6](../../evidence/conditions-sets-007.md#c-11873bfd2941c9e6) · [缺口 G-611be995e28aa601](../../evidence/gaps-sets-004.md#g-611be995e28aa601) · [参数 P-8b5ae59d3a246e73](../../evidence/parameters-sets-011.md#p-8b5ae59d3a246e73) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-071117

```text
(config-subif)# ipv6 nd ra-lifetime <number:0..9000> <cr>
```

Handler ` RVA 0x12313580 `；selector ` 0 `；EOL ` RVA 0x35593F88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` RA Lifetime (seconds)。

[条件 C-eb827d02c9eaa936](../../evidence/conditions-sets-091.md#c-eb827d02c9eaa936) · [参数 P-3e9d2472e4840211](../../evidence/parameters-sets-005.md#p-3e9d2472e4840211) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-068534

```text
(config-subif)# ipv6 nd reachable-time <number:0..3600000> <cr>
```

Handler ` RVA 0x12313740 `；selector ` 0 `；EOL ` RVA 0x35800530 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Reachability time in milliseconds。

[条件 C-012c045b98a884d3](../../evidence/conditions-sets-001.md#c-012c045b98a884d3) · [参数 P-d4f90233fdb84639](../../evidence/parameters-sets-016.md#p-d4f90233fdb84639) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-071211

```text
(config-subif)# ipv6 nd router-preference High <cr>
```

Handler ` RVA 0x12318580 `；selector ` 0 `；EOL ` RVA 0x35595EB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d0add8e9351ac5b0](../../evidence/conditions-sets-080.md#c-d0add8e9351ac5b0) · [状态效果 S-eeaa9eda5eae7c97](../../evidence/state_effects-sets-050.md#s-eeaa9eda5eae7c97)

### path-069609

```text
(config-subif)# ipv6 nd suppress <cr>
```

Handler ` RVA 0x136B2400 `；selector ` 1701 `；EOL ` RVA 0x35C048C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-267f2ac22523aa92](../../evidence/conditions-sets-015.md#c-267f2ac22523aa92) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-069844

```text
(config-subif)# ipv6 nd suppress-ra <cr>
```

Handler ` RVA 0x12317C20 `；selector ` 0 `；EOL ` RVA 0x355955E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-71accf15d7fe95eb](../../evidence/conditions-sets-044.md#c-71accf15d7fe95eb) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-071120

```text
(config-subif)# ipv6 next-hop-self eigrp <number:1..65535> <cr>
```

Handler ` RVA 0xF58CAE0 `；selector ` 131 `；EOL ` RVA 0x3546A480 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` AS number。

[条件 C-96d9b597753adceb](../../evidence/conditions-sets-058.md#c-96d9b597753adceb) · [参数 P-8c733e6188f78f0c](../../evidence/parameters-sets-011.md#p-8c733e6188f78f0c) · [状态效果 S-f2e6681386526499](../../evidence/state_effects-sets-051.md#s-f2e6681386526499)

### path-072835

```text
(config-subif)# ipv6 nhrp attribute set <string> <string> <cr>
```

Handler ` RVA 0x1186E520 `；selector ` 24 `；EOL ` RVA 0x3556F2E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` attribute type；` string ` attribute value。

[条件 C-877b2f8d955222b8](../../evidence/conditions-sets-052.md#c-877b2f8d955222b8) · [缺口 G-414852f247b8cf5e](../../evidence/gaps-sets-003.md#g-414852f247b8cf5e) · [参数 P-dfe495d6b57547b4](../../evidence/parameters-sets-017.md#p-dfe495d6b57547b4) · [状态效果 S-9740c5ae98034b85](../../evidence/state_effects-sets-032.md#s-9740c5ae98034b85)

### path-072765

```text
(config-subif)# ipv6 nhrp authentication <cr>
```

Handler ` RVA 0x1186E520 `；selector ` 6 `；EOL ` RVA 0x3556C600 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-dec1d66ddef5040f](../../evidence/conditions-sets-086.md#c-dec1d66ddef5040f) · [缺口 G-414852f247b8cf5e](../../evidence/gaps-sets-003.md#g-414852f247b8cf5e) · [状态效果 S-9740c5ae98034b85](../../evidence/state_effects-sets-032.md#s-9740c5ae98034b85)

### path-072807

```text
(config-subif)# ipv6 nhrp bfd strict-mode <cr>
```

Handler ` RVA 0x1186E520 `；selector ` 39 `；EOL ` RVA 0x35571200 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-877b2f8d955222b8](../../evidence/conditions-sets-052.md#c-877b2f8d955222b8) · [缺口 G-414852f247b8cf5e](../../evidence/gaps-sets-003.md#g-414852f247b8cf5e) · [状态效果 S-8bf05d5dd0116e37](../../evidence/state_effects-sets-030.md#s-8bf05d5dd0116e37)

### path-072778

```text
(config-subif)# ipv6 nhrp block-next-hop-override <cr>
```

Handler ` RVA 0x1186E520 `；selector ` 48 `；EOL ` RVA 0x35574760 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-877b2f8d955222b8](../../evidence/conditions-sets-052.md#c-877b2f8d955222b8) · [缺口 G-414852f247b8cf5e](../../evidence/gaps-sets-003.md#g-414852f247b8cf5e) · [状态效果 S-9740c5ae98034b85](../../evidence/state_effects-sets-032.md#s-9740c5ae98034b85)

### path-072809

```text
(config-subif)# ipv6 nhrp cache bgp-sync <cr>
```

Handler ` RVA 0x1186E520 `；selector ` 15 `；EOL ` RVA 0x355732E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d55e4aeb1e1bdfe2](../../evidence/conditions-sets-082.md#c-d55e4aeb1e1bdfe2) · [缺口 G-414852f247b8cf5e](../../evidence/gaps-sets-003.md#g-414852f247b8cf5e) · [状态效果 S-9740c5ae98034b85](../../evidence/state_effects-sets-032.md#s-9740c5ae98034b85)

### path-072826

```text
(config-subif)# ipv6 nhrp cache next-hop route-validate <cr>
```

Handler ` RVA 0x1186E520 `；selector ` 46 `；EOL ` RVA 0x35573870 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-877b2f8d955222b8](../../evidence/conditions-sets-052.md#c-877b2f8d955222b8) · [缺口 G-414852f247b8cf5e](../../evidence/gaps-sets-003.md#g-414852f247b8cf5e) · [状态效果 S-9740c5ae98034b85](../../evidence/state_effects-sets-032.md#s-9740c5ae98034b85)

### path-072811

```text
(config-subif)# ipv6 nhrp cache non-authoritative <cr>
```

Handler ` RVA 0x1186E520 `；selector ` 17 `；EOL ` RVA 0x35573588 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-877b2f8d955222b8](../../evidence/conditions-sets-052.md#c-877b2f8d955222b8) · [缺口 G-414852f247b8cf5e](../../evidence/gaps-sets-003.md#g-414852f247b8cf5e) · [状态效果 S-9740c5ae98034b85](../../evidence/state_effects-sets-032.md#s-9740c5ae98034b85)

### path-072804

```text
(config-subif)# ipv6 nhrp connect <number:1..65535> <cr>
```

Handler ` RVA 0xFAB45E0 `；selector ` 30 `；EOL ` RVA 0x3556EF40 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` NHRP event request id。

[条件 C-877b2f8d955222b8](../../evidence/conditions-sets-052.md#c-877b2f8d955222b8) · [缺口 G-414852f247b8cf5e](../../evidence/gaps-sets-003.md#g-414852f247b8cf5e) · [参数 P-32b32a276daddf9b](../../evidence/parameters-sets-004.md#p-32b32a276daddf9b) · [状态效果 S-9740c5ae98034b85](../../evidence/state_effects-sets-032.md#s-9740c5ae98034b85)

### path-072733

```text
(config-subif)# ipv6 nhrp holdtime <number:1..65535> <cr>
```

Handler ` RVA 0x1186E520 `；selector ` 4 `；EOL ` RVA 0x3556DE18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Number of seconds。

[条件 C-4ee556f657ef9c82](../../evidence/conditions-sets-031.md#c-4ee556f657ef9c82) · [缺口 G-041a5714682c70a4](../../evidence/gaps-sets-001.md#g-041a5714682c70a4) · [参数 P-519decfa8692b744](../../evidence/parameters-sets-007.md#p-519decfa8692b744) · [状态效果 S-9740c5ae98034b85](../../evidence/state_effects-sets-032.md#s-9740c5ae98034b85)

### path-072768

```text
(config-subif)# ipv6 nhrp interest <cr>
```

Handler ` RVA 0x1186E520 `；selector ` 3 `；EOL ` RVA 0x3556E460 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d0e04f1c54a6efc0](../../evidence/conditions-sets-080.md#c-d0e04f1c54a6efc0) · [缺口 G-414852f247b8cf5e](../../evidence/gaps-sets-003.md#g-414852f247b8cf5e) · [状态效果 S-9740c5ae98034b85](../../evidence/state_effects-sets-032.md#s-9740c5ae98034b85)

### path-072824

```text
(config-subif)# ipv6 nhrp map multicast dynamic <cr>
```

Handler ` RVA 0x1186E520 `；selector ` 1 `；EOL ` RVA 0x3556CDA0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-877b2f8d955222b8](../../evidence/conditions-sets-052.md#c-877b2f8d955222b8) · [缺口 G-414852f247b8cf5e](../../evidence/gaps-sets-003.md#g-414852f247b8cf5e) · [状态效果 S-c868fc7d5426b9a9](../../evidence/state_effects-sets-042.md#s-c868fc7d5426b9a9)

### path-072773

```text
(config-subif)# ipv6 nhrp max-send <cr>
```

Handler ` RVA 0x1186E520 `；selector ` 9 `；EOL ` RVA 0x35570D28 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ed1cd9ae15241b9c](../../evidence/conditions-sets-092.md#c-ed1cd9ae15241b9c) · [缺口 G-414852f247b8cf5e](../../evidence/gaps-sets-003.md#g-414852f247b8cf5e) · [状态效果 S-9740c5ae98034b85](../../evidence/state_effects-sets-032.md#s-9740c5ae98034b85)

### path-072808

```text
(config-subif)# ipv6 nhrp multicast batch-size <cr>
```

Handler ` RVA 0x1186E520 `；selector ` 23 `；EOL ` RVA 0x35571770 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-877b2f8d955222b8](../../evidence/conditions-sets-052.md#c-877b2f8d955222b8) · [缺口 G-414852f247b8cf5e](../../evidence/gaps-sets-003.md#g-414852f247b8cf5e) · [状态效果 S-9740c5ae98034b85](../../evidence/state_effects-sets-032.md#s-9740c5ae98034b85)

### path-072732

```text
(config-subif)# ipv6 nhrp network-id <number:1..4294967295> <cr>
```

Handler ` RVA 0x1186E520 `；selector ` 0 `；EOL ` RVA 0x3556D3E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Network identifier。

[条件 C-0e01f37176374b0a](../../evidence/conditions-sets-006.md#c-0e01f37176374b0a) · [缺口 G-ccd6cbd35674cd54](../../evidence/gaps-sets-007.md#g-ccd6cbd35674cd54) · [参数 P-9a579a1365799225](../../evidence/parameters-sets-012.md#p-9a579a1365799225) · [状态效果 S-9740c5ae98034b85](../../evidence/state_effects-sets-032.md#s-9740c5ae98034b85)

### path-072806

```text
(config-subif)# ipv6 nhrp nhs <address> <cr>
```

Handler ` RVA 0x1186E520 `；selector ` 2 `；EOL ` RVA 0x3556F9D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Protocol IPv6 address of NHS。

[条件 C-6ff1ba12ee679479](../../evidence/conditions-sets-043.md#c-6ff1ba12ee679479) · [缺口 G-414852f247b8cf5e](../../evidence/gaps-sets-003.md#g-414852f247b8cf5e) · [参数 P-8bfeeb3de0d30fcb](../../evidence/parameters-sets-011.md#p-8bfeeb3de0d30fcb) · [状态效果 S-9740c5ae98034b85](../../evidence/state_effects-sets-032.md#s-9740c5ae98034b85)

### path-072840

```text
(config-subif)# ipv6 nhrp nhs cluster <number:0..10> max-connections <number:0..255> <cr>
```

Handler ` RVA 0x1186E520 `；selector ` 21 `；EOL ` RVA 0x3556FE48 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` NHS cluster number；` unsigned_number ` Max-connections value。

[条件 C-877b2f8d955222b8](../../evidence/conditions-sets-052.md#c-877b2f8d955222b8) · [缺口 G-414852f247b8cf5e](../../evidence/gaps-sets-003.md#g-414852f247b8cf5e) · [参数 P-d16e15f6f9da2f1f](../../evidence/parameters-sets-016.md#p-d16e15f6f9da2f1f) · [状态效果 S-9740c5ae98034b85](../../evidence/state_effects-sets-032.md#s-9740c5ae98034b85)

### path-072825

```text
(config-subif)# ipv6 nhrp nhs fallback <number:0..60> <cr>
```

Handler ` RVA 0x1186E520 `；selector ` 22 `；EOL ` RVA 0x35570120 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` NHS Redundancy Fallback time, 0 -60 seconds。

[条件 C-877b2f8d955222b8](../../evidence/conditions-sets-052.md#c-877b2f8d955222b8) · [缺口 G-414852f247b8cf5e](../../evidence/gaps-sets-003.md#g-414852f247b8cf5e) · [参数 P-14a1e07448e12745](../../evidence/parameters-sets-002.md#p-14a1e07448e12745) · [状态效果 S-9740c5ae98034b85](../../evidence/state_effects-sets-032.md#s-9740c5ae98034b85)

### path-072814

```text
(config-subif)# ipv6 nhrp path preference <cr>
```

Handler ` RVA 0x1186E520 `；selector ` 36 `；EOL ` RVA 0x35574478 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e6c751ea86377a19](../../evidence/conditions-sets-089.md#c-e6c751ea86377a19) · [缺口 G-414852f247b8cf5e](../../evidence/gaps-sets-003.md#g-414852f247b8cf5e) · [状态效果 S-9740c5ae98034b85](../../evidence/state_effects-sets-032.md#s-9740c5ae98034b85)

### path-072771

```text
(config-subif)# ipv6 nhrp process-delay <cr>
```

Handler ` RVA 0x1186E520 `；selector ` 40 `；EOL ` RVA 0x35570678 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-877b2f8d955222b8](../../evidence/conditions-sets-052.md#c-877b2f8d955222b8) · [缺口 G-414852f247b8cf5e](../../evidence/gaps-sets-003.md#g-414852f247b8cf5e) · [状态效果 S-9740c5ae98034b85](../../evidence/state_effects-sets-032.md#s-9740c5ae98034b85)

### path-072770

```text
(config-subif)# ipv6 nhrp record <cr>
```

Handler ` RVA 0x1186E520 `；selector ` 5 `；EOL ` RVA 0x355703D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-877b2f8d955222b8](../../evidence/conditions-sets-052.md#c-877b2f8d955222b8) · [缺口 G-414852f247b8cf5e](../../evidence/gaps-sets-003.md#g-414852f247b8cf5e) · [状态效果 S-9740c5ae98034b85](../../evidence/state_effects-sets-032.md#s-9740c5ae98034b85)

### path-072779

```text
(config-subif)# ipv6 nhrp redirect <cr>
```

Handler ` RVA 0x1186E520 `；selector ` 19 `；EOL ` RVA 0x35573F60 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a4230efc0eb00e04](../../evidence/conditions-sets-063.md#c-a4230efc0eb00e04) · [缺口 G-414852f247b8cf5e](../../evidence/gaps-sets-003.md#g-414852f247b8cf5e) · [状态效果 S-9740c5ae98034b85](../../evidence/state_effects-sets-032.md#s-9740c5ae98034b85)

### path-072774

```text
(config-subif)# ipv6 nhrp registration delay <number:0..10> <cr>
```

Handler ` RVA 0x1186E520 `；selector ` 13 `；EOL ` RVA 0x35571FF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Seconds to delay。

[条件 C-3ab4a8248be986e0](../../evidence/conditions-sets-023.md#c-3ab4a8248be986e0) · [缺口 G-7b330f93eb9d71b5](../../evidence/gaps-sets-005.md#g-7b330f93eb9d71b5) · [参数 P-125d21f029e8f054](../../evidence/parameters-sets-002.md#p-125d21f029e8f054) · [状态效果 S-9740c5ae98034b85](../../evidence/state_effects-sets-032.md#s-9740c5ae98034b85)

### path-072812

```text
(config-subif)# ipv6 nhrp registration differential <cr>
```

Handler ` RVA 0x1186E520 `；selector ` 42 `；EOL ` RVA 0x35572988 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-877b2f8d955222b8](../../evidence/conditions-sets-052.md#c-877b2f8d955222b8) · [缺口 G-414852f247b8cf5e](../../evidence/gaps-sets-003.md#g-414852f247b8cf5e) · [状态效果 S-9740c5ae98034b85](../../evidence/state_effects-sets-032.md#s-9740c5ae98034b85)

### path-072810

```text
(config-subif)# ipv6 nhrp registration no-unique <cr>
```

Handler ` RVA 0x1186E520 `；selector ` 12 `；EOL ` RVA 0x35572368 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-877b2f8d955222b8](../../evidence/conditions-sets-052.md#c-877b2f8d955222b8) · [缺口 G-414852f247b8cf5e](../../evidence/gaps-sets-003.md#g-414852f247b8cf5e) · [状态效果 S-9740c5ae98034b85](../../evidence/state_effects-sets-032.md#s-9740c5ae98034b85)

### path-072813

```text
(config-subif)# ipv6 nhrp registration req-def-map <cr>
```

Handler ` RVA 0x1186E520 `；selector ` 38 `；EOL ` RVA 0x35572680 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-877b2f8d955222b8](../../evidence/conditions-sets-052.md#c-877b2f8d955222b8) · [缺口 G-414852f247b8cf5e](../../evidence/gaps-sets-003.md#g-414852f247b8cf5e) · [状态效果 S-9740c5ae98034b85](../../evidence/state_effects-sets-032.md#s-9740c5ae98034b85)

### path-072776

```text
(config-subif)# ipv6 nhrp registration timeout <number:1..65535> <cr>
```

Handler ` RVA 0x1186E520 `；selector ` 14 `；EOL ` RVA 0x35572948 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Number of seconds。

[条件 C-31fdf6e91e25fd0f](../../evidence/conditions-sets-020.md#c-31fdf6e91e25fd0f) · [缺口 G-f3dc81e8de3d06f2](../../evidence/gaps-sets-008.md#g-f3dc81e8de3d06f2) · [参数 P-0919aa651f93e068](../../evidence/parameters-sets-001.md#p-0919aa651f93e068) · [状态效果 S-9740c5ae98034b85](../../evidence/state_effects-sets-032.md#s-9740c5ae98034b85)

### path-072805

```text
(config-subif)# ipv6 nhrp reject <number:1..65535> <cr>
```

Handler ` RVA 0xFAB45E0 `；selector ` 31 `；EOL ` RVA 0x3556EC18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` reqid value。

[条件 C-877b2f8d955222b8](../../evidence/conditions-sets-052.md#c-877b2f8d955222b8) · [缺口 G-414852f247b8cf5e](../../evidence/gaps-sets-003.md#g-414852f247b8cf5e) · [参数 P-b142d6205eea268a](../../evidence/parameters-sets-013.md#p-b142d6205eea268a) · [状态效果 S-9740c5ae98034b85](../../evidence/state_effects-sets-032.md#s-9740c5ae98034b85)

### path-072837

```text
(config-subif)# ipv6 nhrp resolution refresh base <number:1..65535> <cr>
```

Handler ` RVA 0x1186E520 `；selector ` 41 `；EOL ` RVA 0x35572FD8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Route every 'n'th request through this topology。

[条件 C-877b2f8d955222b8](../../evidence/conditions-sets-052.md#c-877b2f8d955222b8) · [缺口 G-414852f247b8cf5e](../../evidence/gaps-sets-003.md#g-414852f247b8cf5e) · [参数 P-55b953e549b95ef9](../../evidence/parameters-sets-007.md#p-55b953e549b95ef9) · [状态效果 S-9740c5ae98034b85](../../evidence/state_effects-sets-032.md#s-9740c5ae98034b85)

### path-072767

```text
(config-subif)# ipv6 nhrp responder <cr>
```

Handler ` RVA 0x1186E520 `；selector ` 7 `；EOL ` RVA 0x3556C948 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2412f324cedb28bd](../../evidence/conditions-sets-014.md#c-2412f324cedb28bd) · [缺口 G-414852f247b8cf5e](../../evidence/gaps-sets-003.md#g-414852f247b8cf5e) · [状态效果 S-9740c5ae98034b85](../../evidence/state_effects-sets-032.md#s-9740c5ae98034b85)

### path-072803

```text
(config-subif)# ipv6 nhrp role hub <cr>
```

Handler ` RVA 0x1186E520 `；selector ` 49 `；EOL ` RVA 0x3556DE58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-877b2f8d955222b8](../../evidence/conditions-sets-052.md#c-877b2f8d955222b8) · [缺口 G-414852f247b8cf5e](../../evidence/gaps-sets-003.md#g-414852f247b8cf5e) · [状态效果 S-d4365ca3ba3b1e38](../../evidence/state_effects-sets-045.md#s-d4365ca3ba3b1e38)

### path-072775

```text
(config-subif)# ipv6 nhrp send-routed <cr>
```

Handler ` RVA 0x1186E520 `；selector ` 16 `；EOL ` RVA 0x35571D80 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-877b2f8d955222b8](../../evidence/conditions-sets-052.md#c-877b2f8d955222b8) · [缺口 G-414852f247b8cf5e](../../evidence/gaps-sets-003.md#g-414852f247b8cf5e) · [状态效果 S-9740c5ae98034b85](../../evidence/state_effects-sets-032.md#s-9740c5ae98034b85)

### path-072772

```text
(config-subif)# ipv6 nhrp server-only <cr>
```

Handler ` RVA 0x1186E520 `；selector ` 10 `；EOL ` RVA 0x355709C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-877b2f8d955222b8](../../evidence/conditions-sets-052.md#c-877b2f8d955222b8) · [缺口 G-414852f247b8cf5e](../../evidence/gaps-sets-003.md#g-414852f247b8cf5e) · [状态效果 S-9740c5ae98034b85](../../evidence/state_effects-sets-032.md#s-9740c5ae98034b85)

### path-072777

```text
(config-subif)# ipv6 nhrp shortcut <cr>
```

Handler ` RVA 0x1186E520 `；selector ` 18 `；EOL ` RVA 0x35573BE8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-877b2f8d955222b8](../../evidence/conditions-sets-052.md#c-877b2f8d955222b8) · [缺口 G-414852f247b8cf5e](../../evidence/gaps-sets-003.md#g-414852f247b8cf5e) · [状态效果 S-9740c5ae98034b85](../../evidence/state_effects-sets-032.md#s-9740c5ae98034b85)

### path-072843

```text
(config-subif)# ipv6 nhrp summary-map <prefix:dynamic> <cr>
```

Handler ` RVA 0x1186E520 `；selector ` 37 `；EOL ` RVA 0x3556D530 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` IPv6 address/&lt;length&gt; of destination, eg:x.x.x.x.x/&lt;0-128&gt;。

[条件 C-4eeb01a44f4d7a0c](../../evidence/conditions-sets-031.md#c-4eeb01a44f4d7a0c) · [缺口 G-384bdb602259a82d](../../evidence/gaps-sets-002.md#g-384bdb602259a82d) · [参数 P-3d97d2934bbc0c4b](../../evidence/parameters-sets-005.md#p-3d97d2934bbc0c4b) · [状态效果 S-9740c5ae98034b85](../../evidence/state_effects-sets-032.md#s-9740c5ae98034b85)

### path-072769

```text
(config-subif)# ipv6 nhrp trigger-svc <cr>
```

Handler ` RVA 0x1186E520 `；selector ` 11 `；EOL ` RVA 0x3556E860 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-47c9367105a26619](../../evidence/conditions-sets-028.md#c-47c9367105a26619) · [缺口 G-414852f247b8cf5e](../../evidence/gaps-sets-003.md#g-414852f247b8cf5e) · [状态效果 S-9740c5ae98034b85](../../evidence/state_effects-sets-032.md#s-9740c5ae98034b85)

### path-072736

```text
(config-subif)# ipv6 nhrp use <number:1..65535> <cr>
```

Handler ` RVA 0x1186E520 `；selector ` 8 `；EOL ` RVA 0x35571690 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Number of packets to cause NHRP request。

[条件 C-5db17f8fa6641528](../../evidence/conditions-sets-037.md#c-5db17f8fa6641528) · [缺口 G-25728d780ec3bd68](../../evidence/gaps-sets-002.md#g-25728d780ec3bd68) · [参数 P-343a95bc1b67943f](../../evidence/parameters-sets-004.md#p-343a95bc1b67943f) · [状态效果 S-9740c5ae98034b85](../../evidence/state_effects-sets-032.md#s-9740c5ae98034b85)

### path-068692

```text
(config-subif)# ipv6 pim <cr>
```

Handler ` RVA 0x11725A80 `；selector ` 20 `；EOL ` RVA 0x35563DA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fa88c522a604cdc7](../../evidence/conditions-sets-097.md#c-fa88c522a604cdc7) · [状态效果 S-bbe341916f6725ad](../../evidence/state_effects-sets-040.md#s-bbe341916f6725ad)

### path-069912

```text
(config-subif)# ipv6 pim bfd <cr>
```

Handler ` RVA 0xC4A3100 `；selector ` 0 `；EOL ` RVA 0x33A9D218 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-270067499c5f9056](../../evidence/conditions-sets-015.md#c-270067499c5f9056) · [状态效果 S-dba603a80dc1c68f](../../evidence/state_effects-sets-046.md#s-dba603a80dc1c68f)

### path-071154

```text
(config-subif)# ipv6 pim bsr border <cr>
```

Handler ` RVA 0x11725BA0 `；selector ` 25 `；EOL ` RVA 0x355514B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fa88c522a604cdc7](../../evidence/conditions-sets-097.md#c-fa88c522a604cdc7) · [状态效果 S-e7629623b587fb46](../../evidence/state_effects-sets-049.md#s-e7629623b587fb46)

### path-068700

```text
(config-subif)# ipv6 pim dr-priority <number:0..4294967295> <cr>
```

Handler ` RVA 0x11725A80 `；selector ` 22 `；EOL ` RVA 0x355577F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Hello DR priority, preference given to larger value。

[条件 C-226e1d5627b29eb3](../../evidence/conditions-sets-013.md#c-226e1d5627b29eb3) · [参数 P-582484642e68f9c5](../../evidence/parameters-sets-007.md#p-582484642e68f9c5) · [状态效果 S-bbe341916f6725ad](../../evidence/state_effects-sets-040.md#s-bbe341916f6725ad)

### path-069908

```text
(config-subif)# ipv6 pim drlb <cr>
```

Handler ` RVA 0x11725A80 `；selector ` 39 `；EOL ` RVA 0x35557898 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-faf965a4b435c19f](../../evidence/conditions-sets-097.md#c-faf965a4b435c19f) · [状态效果 S-bbe341916f6725ad](../../evidence/state_effects-sets-040.md#s-bbe341916f6725ad)

### path-068685

```text
(config-subif)# ipv6 pim hello-interval <number:1..3600> <cr>
```

Handler ` RVA 0x11725A80 `；selector ` 21 `；EOL ` RVA 0x355572B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Hello interval in seconds。

[条件 C-391d30c077dea768](../../evidence/conditions-sets-022.md#c-391d30c077dea768) · [参数 P-0cb5b2754d6e53b2](../../evidence/parameters-sets-001.md#p-0cb5b2754d6e53b2) · [状态效果 S-bbe341916f6725ad](../../evidence/state_effects-sets-040.md#s-bbe341916f6725ad)

### path-068663

```text
(config-subif)# ipv6 pim join-prune-interval <number:10..600> <cr>
```

Handler ` RVA 0x11725A80 `；selector ` 23 `；EOL ` RVA 0x35556590 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Join-Prune interval in seconds。

[条件 C-5c99f43b7a0d80c2](../../evidence/conditions-sets-036.md#c-5c99f43b7a0d80c2) · [参数 P-9ca1a852cdf056cc](../../evidence/parameters-sets-012.md#p-9ca1a852cdf056cc) · [状态效果 S-bbe341916f6725ad](../../evidence/state_effects-sets-040.md#s-bbe341916f6725ad)

### path-072328

```text
(config-subif)# ipv6 pim lisp core-group-range <address> <number:1..1000> <cr>
```

Handler ` RVA 0x11725A80 `；selector ` 47 `；EOL ` RVA 0x35556F28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Start group address of the range；` unsigned_number ` Size of the group range。

[条件 C-d283de064bc48d65](../../evidence/conditions-sets-081.md#c-d283de064bc48d65) · [参数 P-12493ecba3cedd8d](../../evidence/parameters-sets-002.md#p-12493ecba3cedd8d) · [状态效果 S-bbe341916f6725ad](../../evidence/state_effects-sets-040.md#s-bbe341916f6725ad)

### path-071922

```text
(config-subif)# ipv6 pim lisp transport unicast <cr>
```

Handler ` RVA 0x11725A80 `；selector ` 46 `；EOL ` RVA 0x355569B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3816cc4bacfa4d1b](../../evidence/conditions-sets-022.md#c-3816cc4bacfa4d1b) · [状态效果 S-38f4e21e050db3f1](../../evidence/state_effects-sets-013.md#s-38f4e21e050db3f1)

### path-069739

```text
(config-subif)# ipv6 pim non-dr-join <cr>
```

Handler ` RVA 0x11725A80 `；selector ` 37 `；EOL ` RVA 0x35558068 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9b3b729b9621eec9](../../evidence/conditions-sets-060.md#c-9b3b729b9621eec9) · [状态效果 S-bbe341916f6725ad](../../evidence/state_effects-sets-040.md#s-bbe341916f6725ad)

### path-069738

```text
(config-subif)# ipv6 pim passive <cr>
```

Handler ` RVA 0x11725A80 `；selector ` 32 `；EOL ` RVA 0x35557288 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-53138341ff5bfbdf](../../evidence/conditions-sets-032.md#c-53138341ff5bfbdf) · [状态效果 S-bbe341916f6725ad](../../evidence/state_effects-sets-040.md#s-bbe341916f6725ad)

### path-071209

```text
(config-subif)# ipv6 pim pfp-sa border <cr>
```

Handler ` RVA 0x11725BA0 `；selector ` 52 `；EOL ` RVA 0x355A4C90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e74c4ed4e9ce272e](../../evidence/conditions-sets-089.md#c-e74c4ed4e9ce272e) · [状态效果 S-8857595b0c4d4ddb](../../evidence/state_effects-sets-029.md#s-8857595b0c4d4ddb)

### path-072465

```text
(config-subif)# ipv6 pim redundancy <string> vrrp dr-priority <number:1..4294967295> <cr>
```

Handler ` RVA 0xC4AE630 `；selector ` 38 `；EOL ` RVA 0x33A9E858 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Redundancy group name；` unsigned_number ` Redundancy DR priority. Preference given to larger value。

[条件 C-205f0471ceec8a3d](../../evidence/conditions-sets-013.md#c-205f0471ceec8a3d) · [参数 P-b4b8d08b97132011](../../evidence/parameters-sets-014.md#p-b4b8d08b97132011) · [状态效果 S-b5142cee5b3c573b](../../evidence/state_effects-sets-038.md#s-b5142cee5b3c573b)

### path-071051

```text
(config-subif)# ipv6 policy route-map <string> <cr>
```

Handler ` RVA 0x118B9E70 `；selector ` 0 `；EOL ` RVA 0x3559C210 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Route-map name。

[条件 C-121ab7a1cb8f2835](../../evidence/conditions-sets-007.md#c-121ab7a1cb8f2835) · [参数 P-0a1af3f4464defc5](../../evidence/parameters-sets-001.md#p-0a1af3f4464defc5) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-068640

```text
(config-subif)# ipv6 reassembly <cr>
```

Handler ` RVA 0xC788BE0 `；selector ` 0 `；EOL ` RVA 0x33AE7640 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-60a1029ba3cd20c4](../../evidence/conditions-sets-038.md#c-60a1029ba3cd20c4) · [状态效果 S-d34ace017dd7d3eb](../../evidence/state_effects-sets-045.md#s-d34ace017dd7d3eb)

### path-072833

```text
(config-subif)# ipv6 reassembly percentage <number:1..100> dscp <?common_dscp_value_action@55558903b4d8> <cr>
```

Handler ` RVA 0xC788BE0 `；selector ` 0 `；EOL ` RVA 0x33AE7640 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Reserved Reassembly capacity percentage。

[条件 C-080e600897ed6dce](../../evidence/conditions-sets-003.md#c-080e600897ed6dce) · [缺口 G-9b76d1c0d7819c61](../../evidence/gaps-sets-006.md#g-9b76d1c0d7819c61) · [参数 P-3d6ecf3951fa99bd](../../evidence/parameters-sets-005.md#p-3d6ecf3951fa99bd) · [状态效果 S-c7bbd6b6e4d77cc5](../../evidence/state_effects-sets-042.md#s-c7bbd6b6e4d77cc5)

### path-072834

```text
(config-subif)# ipv6 reassembly percentage <number:1..100> dscp <?common_dscp_value_action@55558903b4d8> <cr>
```

Handler ` RVA 0xC788BE0 `；selector ` 0 `；EOL ` RVA 0x33AE7148 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Reserved Reassembly capacity percentage。

[条件 C-674cb056f68d3473](../../evidence/conditions-sets-040.md#c-674cb056f68d3473) · [缺口 G-9b76d1c0d7819c61](../../evidence/gaps-sets-006.md#g-9b76d1c0d7819c61) · [参数 P-3d6ecf3951fa99bd](../../evidence/parameters-sets-005.md#p-3d6ecf3951fa99bd) · [状态效果 S-c7bbd6b6e4d77cc5](../../evidence/state_effects-sets-042.md#s-c7bbd6b6e4d77cc5)

### path-068653

```text
(config-subif)# ipv6 reassembly-timer <cr>
```

Handler ` RVA 0xC788BE0 `；selector ` 0 `；EOL ` RVA 0x33AE7148 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b5dc39c00eca5b8f](../../evidence/conditions-sets-070.md#c-b5dc39c00eca5b8f) · [状态效果 S-5039a0005d075009](../../evidence/state_effects-sets-018.md#s-5039a0005d075009)

### path-068635

```text
(config-subif)# ipv6 redirects <cr>
```

Handler ` RVA 0x12306610 `；selector ` 0 `；EOL ` RVA 0x35593410 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2903dc8da001675f](../../evidence/conditions-sets-016.md#c-2903dc8da001675f) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-071909

```text
(config-subif)# ipv6 rip <string> default-information originate <cr>
```

Handler ` RVA 0x118A2990 `；selector ` 3 `；EOL ` RVA 0x3557B318 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` User selected string identifying this RIP process。

[条件 C-f8a12d959c7d7d42](../../evidence/conditions-sets-096.md#c-f8a12d959c7d7d42) · [参数 P-2609ff256a05d402](../../evidence/parameters-sets-003.md#p-2609ff256a05d402) · [状态效果 S-bcd7c6ac44bc5258](../../evidence/state_effects-sets-040.md#s-bcd7c6ac44bc5258)

### path-071018

```text
(config-subif)# ipv6 rip <string> enable <cr>
```

Handler ` RVA 0x118A2990 `；selector ` 4 `；EOL ` RVA 0x3557AF68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` User selected string identifying this RIP process。

[条件 C-96d9b597753adceb](../../evidence/conditions-sets-058.md#c-96d9b597753adceb) · [参数 P-2609ff256a05d402](../../evidence/parameters-sets-003.md#p-2609ff256a05d402) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-071902

```text
(config-subif)# ipv6 rip <string> metric-offset <number:1..16> <cr>
```

Handler ` RVA 0x118A2990 `；selector ` 1 `；EOL ` RVA 0x3557B9E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` User selected string identifying this RIP process。

[条件 C-fe04df766eb8cdbe](../../evidence/conditions-sets-098.md#c-fe04df766eb8cdbe) · [参数 P-4c463612286885e0](../../evidence/parameters-sets-006.md#p-4c463612286885e0) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-072666

```text
(config-subif)# ipv6 rip <string> summary-address <prefix:dynamic> <cr>
```

Handler ` RVA 0x118A2990 `；selector ` 2 `；EOL ` RVA 0x3557B6D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` User selected string identifying this RIP process；` prefix_dynamic ` summary prefix。

[条件 C-0cdd66319211c15b](../../evidence/conditions-sets-005.md#c-0cdd66319211c15b) · [缺口 G-52fd84f4f56f2928](../../evidence/gaps-sets-003.md#g-52fd84f4f56f2928) · [参数 P-255ffa359291e723](../../evidence/parameters-sets-003.md#p-255ffa359291e723) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-069801

```text
(config-subif)# ipv6 router isis <cr>
```

Handler ` RVA 0x11A995F0 `；selector ` 0 `；EOL ` RVA 0x355D6188 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-96d9b597753adceb](../../evidence/conditions-sets-058.md#c-96d9b597753adceb) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-072728

```text
(config-subif)# ipv6 snooping <cr>
```

Handler ` RVA 0x1368B060 `；selector ` 1121 `；EOL ` RVA 0x35BCAB70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-bfad228f02990baf](../../evidence/conditions-sets-074.md#c-bfad228f02990baf) · [缺口 G-60e1648c1cb308cd](../../evidence/gaps-sets-004.md#g-60e1648c1cb308cd) · [状态效果 S-1cea9e00865666f7](../../evidence/state_effects-sets-007.md#s-1cea9e00865666f7)

### path-068608

```text
(config-subif)# ipv6 source-guard <cr>
```

Handler ` RVA 0x136BFEE0 `；selector ` 1520 `；EOL ` RVA 0x35C07F40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9ffae0ea0a1c49b3](../../evidence/conditions-sets-062.md#c-9ffae0ea0a1c49b3) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-071110

```text
(config-subif)# ipv6 split-horizon eigrp <number:1..65535> <cr>
```

Handler ` RVA 0xF58CAE0 `；selector ` 133 `；EOL ` RVA 0x3546A860 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` AS number。

[条件 C-96d9b597753adceb](../../evidence/conditions-sets-058.md#c-96d9b597753adceb) · [参数 P-44fee36d026c7be2](../../evidence/parameters-sets-006.md#p-44fee36d026c7be2) · [状态效果 S-f2e6681386526499](../../evidence/state_effects-sets-051.md#s-f2e6681386526499)

### path-072671

```text
(config-subif)# ipv6 summary-address eigrp <number:1..65535> <prefix:dynamic> <cr>
```

Handler ` RVA 0x112E5010 `；selector ` 134 `；EOL ` RVA 0x3546AC60 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` AS number；` prefix_dynamic ` IPv6 prefix。

[条件 C-859f2a81e97bb712](../../evidence/conditions-sets-052.md#c-859f2a81e97bb712) · [缺口 G-006d5bd023c33dd1](../../evidence/gaps-sets-001.md#g-006d5bd023c33dd1) · [参数 P-47a8ec30f896c0a8](../../evidence/parameters-sets-006.md#p-47a8ec30f896c0a8) · [状态效果 S-f2e6681386526499](../../evidence/state_effects-sets-051.md#s-f2e6681386526499)

### path-072622

```text
(config-subif)# ipv6 tcp adjust-mss <number:dynamic> <cr>
```

Handler ` RVA 0xCDEDB20 `；selector ` 48 `；EOL ` RVA 0x33D01D88 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Maximum segment size in bytes。

[条件 C-7913efcb2262b732](../../evidence/conditions-sets-047.md#c-7913efcb2262b732) · [缺口 G-783179d6b7e1b4c2](../../evidence/gaps-sets-005.md#g-783179d6b7e1b4c2) · [参数 P-ec2ca37626b29a43](../../evidence/parameters-sets-018.md#p-ec2ca37626b29a43) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-070973

```text
(config-subif)# ipv6 traffic-filter <string> in <cr>
```

Handler ` RVA 0x12164030 `；selector ` 0 `；EOL ` RVA 0x357AF7C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Access-list name。

[条件 C-760f93d925c6155b](../../evidence/conditions-sets-046.md#c-760f93d925c6155b) · [参数 P-8130050db2014603](../../evidence/parameters-sets-010.md#p-8130050db2014603) · [状态效果 S-d061e5bd8213911a](../../evidence/state_effects-sets-044.md#s-d061e5bd8213911a)

### path-072575

```text
(config-subif)# ipv6 unnumbered <interface> <cr>
```

Handler ` RVA 0x123028B0 `；selector ` 0 `；EOL ` RVA 0x357E0408 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3aaf78efb22780b2](../../evidence/conditions-sets-023.md#c-3aaf78efb22780b2) · [缺口 G-c4f71a8ff67fd661](../../evidence/gaps-sets-007.md#g-c4f71a8ff67fd661) · [参数 P-31b50a1ec328e874](../../evidence/parameters-sets-004.md#p-31b50a1ec328e874) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-068649

```text
(config-subif)# ipv6 unreachables <cr>
```

Handler ` RVA 0x123064E0 `；selector ` 0 `；EOL ` RVA 0x355936B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2903dc8da001675f](../../evidence/conditions-sets-016.md#c-2903dc8da001675f) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-071172

```text
(config-subif)# ipv6 verify unicast reverse-path <cr>
```

Handler ` RVA 0x118B8120 `；selector ` 0 `；EOL ` RVA 0x3559B290 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b1ffe5f9df0efdbd](../../evidence/conditions-sets-069.md#c-b1ffe5f9df0efdbd) · [状态效果 S-27e6782416da79fa](../../evidence/state_effects-sets-009.md#s-27e6782416da79fa)

### path-070184

```text
(config-subif)# isdn N200 <number:1..100> <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 28 `；EOL ` RVA 0x378B32C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of Retransmissions。

[条件 C-11fc82ba86bbb451](../../evidence/conditions-sets-007.md#c-11fc82ba86bbb451) · [参数 P-9f51477ec5f49ee1](../../evidence/parameters-sets-012.md#p-9f51477ec5f49ee1)

### path-070167

```text
(config-subif)# isdn T-Activate <number:1000..15000> <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 127 `；EOL ` RVA 0x378B1F68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timer T-Activate value in milliseconds。

[条件 C-2916dddbc8e60234](../../evidence/conditions-sets-016.md#c-2916dddbc8e60234) · [参数 P-4ce5be0578a7ecd5](../../evidence/parameters-sets-006.md#p-4ce5be0578a7ecd5)

### path-070187

```text
(config-subif)# isdn T200 <number:400..400000> <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 27 `；EOL ` RVA 0x378B3618 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timer T200 value in milliseconds。

[条件 C-f0d174549e401477](../../evidence/conditions-sets-093.md#c-f0d174549e401477) · [参数 P-2349517b5aff3f0d](../../evidence/parameters-sets-003.md#p-2349517b5aff3f0d)

### path-070191

```text
(config-subif)# isdn T203 <number:400..400000> <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 62 `；EOL ` RVA 0x378B3CB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timer T203 value in milliseconds。

[条件 C-501169d35469d556](../../evidence/conditions-sets-031.md#c-501169d35469d556) · [参数 P-8b67f4f81fa116c1](../../evidence/parameters-sets-011.md#p-8b67f4f81fa116c1)

### path-070180

```text
(config-subif)# isdn T303 <number:400..86400000> <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 108 `；EOL ` RVA 0x378B2CA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timer T303 in miliseconds.。

[条件 C-d423d211e18fc470](../../evidence/conditions-sets-082.md#c-d423d211e18fc470) · [参数 P-333ebe0097700ffd](../../evidence/parameters-sets-004.md#p-333ebe0097700ffd)

### path-070194

```text
(config-subif)# isdn T306 <number:1..400000> <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 105 `；EOL ` RVA 0x378B4008 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timer T306 value in milliseconds。

[条件 C-42767dbddff209bf](../../evidence/conditions-sets-026.md#c-42767dbddff209bf) · [参数 P-3e11768890983b15](../../evidence/parameters-sets-005.md#p-3e11768890983b15)

### path-070205

```text
(config-subif)# isdn T307 <number:30000..300000> <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 110 `；EOL ` RVA 0x378B46F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timer T307 value in milliseconds。

[条件 C-2ef064cb9cc01f5f](../../evidence/conditions-sets-018.md#c-2ef064cb9cc01f5f) · [参数 P-eceef77c6c41bfc2](../../evidence/parameters-sets-018.md#p-eceef77c6c41bfc2)

### path-070176

```text
(config-subif)# isdn T309 <number:0..86400000> <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 103 `；EOL ` RVA 0x378B2958 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timer T309 in miliseconds or 0 to Disable.。

[条件 C-543796bb5e03b1a0](../../evidence/conditions-sets-033.md#c-543796bb5e03b1a0) · [参数 P-15dbbc2ac24984a2](../../evidence/parameters-sets-002.md#p-15dbbc2ac24984a2)

### path-068849

```text
(config-subif)# isdn T309-enable <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 100 `；EOL ` RVA 0x378AE048 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d3bce07fbceabc72](../../evidence/conditions-sets-082.md#c-d3bce07fbceabc72)

### path-070199

```text
(config-subif)# isdn T310 <number:1..400000> <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 112 `；EOL ` RVA 0x378B4360 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timer T310 value in milliseconds。

[条件 C-db3b51472b6ee6ed](../../evidence/conditions-sets-084.md#c-db3b51472b6ee6ed) · [参数 P-9c2fbcaf4f9cf1ba](../../evidence/parameters-sets-012.md#p-9c2fbcaf4f9cf1ba)

### path-070173

```text
(config-subif)# isdn T321 <number:0..86400000> <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 104 `；EOL ` RVA 0x378B2608 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timer T321 in miliseconds or 0 to Disable.。

[条件 C-2768267991af4b10](../../evidence/conditions-sets-015.md#c-2768267991af4b10) · [参数 P-acb6102b2ef12da4](../../evidence/parameters-sets-013.md#p-acb6102b2ef12da4)

### path-070170

```text
(config-subif)# isdn T3OOS <number:500..86400000> <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 113 `；EOL ` RVA 0x378B22B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timer T3OS in miliseconds.。

[条件 C-c579a6a0a96cd0f0](../../evidence/conditions-sets-076.md#c-c579a6a0a96cd0f0) · [参数 P-a4a155a88fb87b3b](../../evidence/parameters-sets-013.md#p-a4a155a88fb87b3b)

### path-068834

```text
(config-subif)# isdn answer1 <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 24 `；EOL ` RVA 0x378ABD70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-52c394276c9314d8](../../evidence/conditions-sets-032.md#c-52c394276c9314d8)

### path-068842

```text
(config-subif)# isdn answer2 <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 25 `；EOL ` RVA 0x378AC0B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-52c394276c9314d8](../../evidence/conditions-sets-032.md#c-52c394276c9314d8)

### path-068833

```text
(config-subif)# isdn autodetect <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 75 `；EOL ` RVA 0x378AA068 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d7b79859f4dd295b](../../evidence/conditions-sets-083.md#c-d7b79859f4dd295b)

### path-071461

```text
(config-subif)# isdn bcac service audit <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 43 `；EOL ` RVA 0x378AF9E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-580ceb7c84249b48](../../evidence/conditions-sets-034.md#c-580ceb7c84249b48)

### path-072091

```text
(config-subif)# isdn bcac service audit interface <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 41 `；EOL ` RVA 0x378AF768 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-580ceb7c84249b48](../../evidence/conditions-sets-034.md#c-580ceb7c84249b48)

### path-072372

```text
(config-subif)# isdn bcac service audit trigger <number:1..6> <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 44 `；EOL ` RVA 0x378AF478 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number `  1) On receiving an incoming call on a channel which is in OOS/Maint state  2) On receiving an unsolicited SERV ACK message  3) On receiving an unallowed response to SERV message  4) On receiving a REL COMP message with a cause #44  5) Once every 24 hours on all channels  6) Once every hour on all channels that are in the OOS/Far end state  。

[条件 C-580ceb7c84249b48](../../evidence/conditions-sets-034.md#c-580ceb7c84249b48) · [参数 P-579071b939c7e043](../../evidence/parameters-sets-007.md#p-579071b939c7e043)

### path-072082

```text
(config-subif)# isdn bcac service retry in-serv-on-fail <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 42 `；EOL ` RVA 0x378AE7A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-580ceb7c84249b48](../../evidence/conditions-sets-034.md#c-580ceb7c84249b48)

### path-072366

```text
(config-subif)# isdn bcac service retry max <number:0..127> <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 37 `；EOL ` RVA 0x378AE4D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Valid range for max retry attempts。

[条件 C-b9276ab03dde0b8e](../../evidence/conditions-sets-071.md#c-b9276ab03dde0b8e) · [参数 P-c9e34c2a484d6309](../../evidence/parameters-sets-015.md#p-c9e34c2a484d6309)

### path-072088

```text
(config-subif)# isdn bcac service timer <number:5000..120000> <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 40 `；EOL ` RVA 0x378AF110 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Service Timer value in milliseconds。

[条件 C-8305032b8ab709d0](../../evidence/conditions-sets-051.md#c-8305032b8ab709d0) · [参数 P-522a49d65535aa68](../../evidence/parameters-sets-007.md#p-522a49d65535aa68)

### path-072081

```text
(config-subif)# isdn bcac service update linkup <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 38 `；EOL ` RVA 0x378AEB00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-580ceb7c84249b48](../../evidence/conditions-sets-034.md#c-580ceb7c84249b48)

### path-072085

```text
(config-subif)# isdn bcac service update provision <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 39 `；EOL ` RVA 0x378AEDB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-580ceb7c84249b48](../../evidence/conditions-sets-034.md#c-580ceb7c84249b48)

### path-070231

```text
(config-subif)# isdn bchan-number-order ascending <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 57 `；EOL ` RVA 0x378B6BF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-936c6ef4a75557f4](../../evidence/conditions-sets-057.md#c-936c6ef4a75557f4) · [状态效果 S-7f7efba6f43feddb](../../evidence/state_effects-sets-027.md#s-7f7efba6f43feddb)

### path-070209

```text
(config-subif)# isdn bind-l3 q931 <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 91 `；EOL ` RVA 0x378B4EE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-26bc39b80cf13dfb](../../evidence/conditions-sets-015.md#c-26bc39b80cf13dfb) · [状态效果 S-b8ada09e22665c57](../../evidence/state_effects-sets-039.md#s-b8ada09e22665c57)

### path-072375

```text
(config-subif)# isdn busy b_channel <number:0..24> - <number:0..24> <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 46 `；EOL ` RVA 0x378B0098 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` B channel range or 0 for complete interface；` unsigned_number ` B channel range or 0 for complete interface。

[条件 C-0cdfbf213b6b3bba](../../evidence/conditions-sets-005.md#c-0cdfbf213b6b3bba) · [参数 P-b5da4c61d5b8cc75](../../evidence/parameters-sets-014.md#p-b5da4c61d5b8cc75) · [状态效果 S-c61046ebfe607600](../../evidence/state_effects-sets-042.md#s-c61046ebfe607600)

### path-072641

```text
(config-subif)# isdn busy b_channel <number:0..24> <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 46 `；EOL ` RVA 0x378B0098 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` B channel range or 0 for complete interface。

[条件 C-feb69f0b35a7a6af](../../evidence/conditions-sets-098.md#c-feb69f0b35a7a6af) · [缺口 G-f385f6b897311b94](../../evidence/gaps-sets-008.md#g-f385f6b897311b94) · [参数 P-183c00890ef89c06](../../evidence/parameters-sets-002.md#p-183c00890ef89c06) · [状态效果 S-adca7d77cf43f67e](../../evidence/state_effects-sets-037.md#s-adca7d77cf43f67e)

### path-070042

```text
(config-subif)# isdn caller <string> <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 22 `；EOL ` RVA 0x378AA440 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Caller String。

[条件 C-52c394276c9314d8](../../evidence/conditions-sets-032.md#c-52c394276c9314d8) · [参数 P-1b52a7966b4a59bc](../../evidence/parameters-sets-003.md#p-1b52a7966b4a59bc)

### path-070115

```text
(config-subif)# isdn calling-number <string> <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 26 `；EOL ` RVA 0x378AD180 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Calling Number。

[条件 C-cd90bf97dee53927](../../evidence/conditions-sets-079.md#c-cd90bf97dee53927) · [参数 P-b0ed0e92d13c1126](../../evidence/parameters-sets-013.md#p-b0ed0e92d13c1126)

### path-070135

```text
(config-subif)# isdn calling-party-num network-provided <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 119 `；EOL ` RVA 0x378ADC98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bcca4b2f55625fb6](../../evidence/conditions-sets-073.md#c-bcca4b2f55625fb6) · [状态效果 S-f35653e62d354ae1](../../evidence/state_effects-sets-051.md#s-f35653e62d354ae1)

### path-068860

```text
(config-subif)# isdn cause-location <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 165 `；EOL ` RVA 0x378B6458 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9fbce0af18f71764](../../evidence/conditions-sets-062.md#c-9fbce0af18f71764)

### path-070237

```text
(config-subif)# isdn cc-pattern <string> <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 169 `；EOL ` RVA 0x378B7FA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Collect Call Pattern。

[条件 C-aa2f869da1319178](../../evidence/conditions-sets-066.md#c-aa2f869da1319178) · [参数 P-e434c07fd62aee62](../../evidence/parameters-sets-017.md#p-e434c07fd62aee62)

### path-071480

```text
(config-subif)# isdn channel-id invert extend-bit <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 145 `；EOL ` RVA 0x378BC3D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a6db3f12f9eed212](../../evidence/conditions-sets-064.md#c-a6db3f12f9eed212)

### path-072376

```text
(config-subif)# isdn datetime message connect priority remote <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 158 `；EOL ` RVA 0x378B9B50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bfcd55285a3de999](../../evidence/conditions-sets-074.md#c-bfcd55285a3de999) · [状态效果 S-257ff01bbcea61b6](../../evidence/state_effects-sets-008.md#s-257ff01bbcea61b6)

### path-070219

```text
(config-subif)# isdn disconnect-cause busy <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 47 `；EOL ` RVA 0x378B67A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-76aa3e734b3a8331](../../evidence/conditions-sets-046.md#c-76aa3e734b3a8331) · [状态效果 S-711b1d636a476cee](../../evidence/state_effects-sets-024.md#s-711b1d636a476cee)

### path-068185

```text
(config-subif)# isdn fast-rollover-delay <number:1..45> <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 33 `；EOL ` RVA 0x378AA338 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Fast rollover delay in seconds。

[条件 C-895e89f8237a0b1b](../../evidence/conditions-sets-053.md#c-895e89f8237a0b1b) · [参数 P-89bd4a13b1b45c56](../../evidence/parameters-sets-011.md#p-89bd4a13b1b45c56)

### path-068855

```text
(config-subif)# isdn flip-chan-flag <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 92 `；EOL ` RVA 0x378B2F98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b473169e77a10609](../../evidence/conditions-sets-070.md#c-b473169e77a10609)

### path-070066

```text
(config-subif)# isdn guard-timer <number:1000..20000> <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 89 `；EOL ` RVA 0x378AB5C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Guard Timer value in milliseconds。

[条件 C-6ee31a256ed37de6](../../evidence/conditions-sets-043.md#c-6ee31a256ed37de6) · [参数 P-1b6e13bfa3ba42d9](../../evidence/parameters-sets-003.md#p-1b6e13bfa3ba42d9)

### path-071478

```text
(config-subif)# isdn incoming alerting add-PI <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 130 `；EOL ` RVA 0x378BA4A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b7daab3507ce7e41](../../evidence/conditions-sets-071.md#c-b7daab3507ce7e41) · [状态效果 S-20a83c9508cbf288](../../evidence/state_effects-sets-007.md#s-20a83c9508cbf288)

### path-072097

```text
(config-subif)# isdn incoming ie channel-id accept-qsig-variant <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 131 `；EOL ` RVA 0x378BA880 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-52c394276c9314d8](../../evidence/conditions-sets-032.md#c-52c394276c9314d8) · [状态效果 S-329f8f908a719291](../../evidence/state_effects-sets-011.md#s-329f8f908a719291)

### path-071475

```text
(config-subif)# isdn incoming progress accept <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 114 `；EOL ` RVA 0x378BA0B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-517c4de6bf3509fc](../../evidence/conditions-sets-032.md#c-517c4de6bf3509fc) · [状态效果 S-88aa2866cd5e5c96](../../evidence/state_effects-sets-029.md#s-88aa2866cd5e5c96)

### path-070076

```text
(config-subif)# isdn incoming-voice data <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 31 `；EOL ` RVA 0x378AAAC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4cc1617b043c2a1d](../../evidence/conditions-sets-030.md#c-4cc1617b043c2a1d)

### path-070103

```text
(config-subif)# isdn incoming-voice modem <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 32 `；EOL ` RVA 0x378AAEC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2a886799c3338483](../../evidence/conditions-sets-017.md#c-2a886799c3338483)

### path-070084

```text
(config-subif)# isdn incoming-voice voice <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 73 `；EOL ` RVA 0x378AB270 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-eb55192e61bde876](../../evidence/conditions-sets-091.md#c-eb55192e61bde876)

### path-070189

```text
(config-subif)# isdn k <number:1..7> <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 87 `；EOL ` RVA 0x378B3988 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Q.921 Window size。

[条件 C-25c0abc2a3e14a6b](../../evidence/conditions-sets-015.md#c-25c0abc2a3e14a6b) · [参数 P-401cad77ce80baae](../../evidence/parameters-sets-005.md#p-401cad77ce80baae)

### path-070078

```text
(config-subif)# isdn layer1-emulate network <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 74 `；EOL ` RVA 0x378A9510 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8ba57e46e820a0be](../../evidence/conditions-sets-054.md#c-8ba57e46e820a0be) · [状态效果 S-de44ca0906111b58](../../evidence/state_effects-sets-047.md#s-de44ca0906111b58)

### path-070257

```text
(config-subif)# isdn layer2-flap STATUS-ENQ <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 164 `；EOL ` RVA 0x378BC9E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-aa746013d7a3ae98](../../evidence/conditions-sets-066.md#c-aa746013d7a3ae98) · [状态效果 S-98e4223cee871be7](../../evidence/state_effects-sets-032.md#s-98e4223cee871be7)

### path-070144

```text
(config-subif)# isdn map address <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 23 `；EOL ` RVA 0x378AC418 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-23dab50b3216bdef](../../evidence/conditions-sets-014.md#c-23dab50b3216bdef) · [状态效果 S-81e508bcf67a11d4](../../evidence/state_effects-sets-028.md#s-81e508bcf67a11d4)

### path-070215

```text
(config-subif)# isdn max-restart-tries <number:1..20> <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 101 `；EOL ` RVA 0x378B60F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Specify maximum number of RESTART attempts。

[条件 C-1ee272d895669ce4](../../evidence/conditions-sets-012.md#c-1ee272d895669ce4) · [参数 P-9926d6932b0f7ae5](../../evidence/parameters-sets-012.md#p-9926d6932b0f7ae5)

### path-068859

```text
(config-subif)# isdn negotiate-bchan <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 70 `；EOL ` RVA 0x378B5828 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-54e42d778590f11a](../../evidence/conditions-sets-033.md#c-54e42d778590f11a) · [状态效果 S-64fd3f38097c7ef4](../../evidence/state_effects-sets-022.md#s-64fd3f38097c7ef4)

### path-068854

```text
(config-subif)# isdn network <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 9 `；EOL ` RVA 0x378B0EB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cf302818b786d558](../../evidence/conditions-sets-080.md#c-cf302818b786d558)

### path-070229

```text
(config-subif)# isdn nfas-channel_id implicit <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 59 `；EOL ` RVA 0x378B73E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1e90689e08fad95a](../../evidence/conditions-sets-012.md#c-1e90689e08fad95a) · [状态效果 S-db466c885eabacd6](../../evidence/state_effects-sets-046.md#s-db466c885eabacd6)

### path-070224

```text
(config-subif)# isdn nfas-order dsl <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 58 `；EOL ` RVA 0x378B7020 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-198bcdd0073131c8](../../evidence/conditions-sets-010.md#c-198bcdd0073131c8) · [状态效果 S-c4c7f4184a64a61d](../../evidence/state_effects-sets-042.md#s-c4c7f4184a64a61d)

### path-068798

```text
(config-subif)# isdn not-end-to-end <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 30 `；EOL ` RVA 0x378A8210 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6974d771722685d8](../../evidence/conditions-sets-041.md#c-6974d771722685d8)

### path-070247

```text
(config-subif)# isdn nsf-service sdn <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 64 `；EOL ` RVA 0x378BAE40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ecb1114f9dca3cc4](../../evidence/conditions-sets-091.md#c-ecb1114f9dca3cc4) · [状态效果 S-02c49725983f4029](../../evidence/state_effects-sets-001.md#s-02c49725983f4029)

### path-072070

```text
(config-subif)# isdn number called enbloc <number:1..32> <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 144 `；EOL ` RVA 0x378AD5B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Maximum Number of digits。

[条件 C-908a502ee75222f5](../../evidence/conditions-sets-056.md#c-908a502ee75222f5) · [参数 P-298a6075541e31e6](../../evidence/parameters-sets-004.md#p-298a6075541e31e6)

### path-072073

```text
(config-subif)# isdn number called setup <number:0..32> <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 146 `；EOL ` RVA 0x378AD8D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Called Number digits。

[条件 C-01dd88804c77a98b](../../evidence/conditions-sets-001.md#c-01dd88804c77a98b) · [参数 P-01265952eeddecf3](../../evidence/parameters-sets-001.md#p-01265952eeddecf3)

### path-070239

```text
(config-subif)# isdn outgoing display-ie <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 129 `；EOL ` RVA 0x378B8338 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-34cc6a9c36832d45](../../evidence/conditions-sets-021.md#c-34cc6a9c36832d45) · [状态效果 S-2ed61b7dc83eff9a](../../evidence/state_effects-sets-010.md#s-2ed61b7dc83eff9a)

### path-068783

```text
(config-subif)# isdn overlap-receiving <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 56 `；EOL ` RVA 0x378A7BD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6499669d7ed9eb29](../../evidence/conditions-sets-039.md#c-6499669d7ed9eb29)

### path-071251

```text
(config-subif)# isdn overlap-receiving T302 <number:500..20000> <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 56 `；EOL ` RVA 0x378A78E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timer T302 value in milliseconds。

[条件 C-9f00fe88ba1a36f5](../../evidence/conditions-sets-061.md#c-9f00fe88ba1a36f5) · [参数 P-62e5d695fdd83a70](../../evidence/parameters-sets-008.md#p-62e5d695fdd83a70)

### path-068819

```text
(config-subif)# isdn point-to-point-setup <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 102 `；EOL ` RVA 0x378A9150 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-32e0d4cfaba93d9d](../../evidence/conditions-sets-020.md#c-32e0d4cfaba93d9d)

### path-070013

```text
(config-subif)# isdn protocol-emulate network <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 72 `；EOL ` RVA 0x378A8610 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d849563328c6e94f](../../evidence/conditions-sets-083.md#c-d849563328c6e94f) · [状态效果 S-7336572f6afd93d3](../../evidence/state_effects-sets-024.md#s-7336572f6afd93d3)

### path-070242

```text
(config-subif)# isdn reject v110 <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 111 `；EOL ` RVA 0x378B9408 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-adef36207e20b422](../../evidence/conditions-sets-067.md#c-adef36207e20b422) · [状态效果 S-2ece81d5622839db](../../evidence/state_effects-sets-010.md#s-2ece81d5622839db)

### path-068862

```text
(config-subif)# isdn reverse-charging-indicator <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 168 `；EOL ` RVA 0x378B7C30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-52c394276c9314d8](../../evidence/conditions-sets-032.md#c-52c394276c9314d8)

### path-068858

```text
(config-subif)# isdn send-alerting <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 54 `；EOL ` RVA 0x378B54A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b4bb749f343d8cbd](../../evidence/conditions-sets-070.md#c-b4bb749f343d8cbd)

### path-068857

```text
(config-subif)# isdn send-status-enquiry <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 107 `；EOL ` RVA 0x378B4A28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-368c1a87ef9eb756](../../evidence/conditions-sets-021.md#c-368c1a87ef9eb756)

### path-068863

```text
(config-subif)# isdn sending-complete <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 48 `；EOL ` RVA 0x378B79C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-23fb6d25625bd14c](../../evidence/conditions-sets-014.md#c-23fb6d25625bd14c)

### path-072512

```text
(config-subif)# isdn service b_channel <number:0..24> - <number:0..24> state <number:0..2> <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 45 `；EOL ` RVA 0x378B09E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` B channel range or 0 for complete interface；` unsigned_number ` B channel range or 0 for complete interface；` unsigned_number ` Valid states are 0=Inservice 1=Maint 2=Outofservice。

[条件 C-2e54fb3533d943fe](../../evidence/conditions-sets-018.md#c-2e54fb3533d943fe) · [参数 P-0b8627696aae903c](../../evidence/parameters-sets-001.md#p-0b8627696aae903c) · [状态效果 S-d99ddb45299c8ba9](../../evidence/state_effects-sets-046.md#s-d99ddb45299c8ba9)

### path-072701

```text
(config-subif)# isdn service b_channel <number:0..24> state <number:0..2> <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 45 `；EOL ` RVA 0x378B09E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` B channel range or 0 for complete interface；` unsigned_number ` Valid states are 0=Inservice 1=Maint 2=Outofservice。

[条件 C-8c13ec30838c6fe1](../../evidence/conditions-sets-054.md#c-8c13ec30838c6fe1) · [缺口 G-b283fded9933f531](../../evidence/gaps-sets-006.md#g-b283fded9933f531) · [参数 P-3ea7cb2217de26b8](../../evidence/parameters-sets-005.md#p-3ea7cb2217de26b8) · [状态效果 S-8aea935c6cfbf3c7](../../evidence/state_effects-sets-030.md#s-8aea935c6cfbf3c7)

### path-070062

```text
(config-subif)# isdn setup-delay-timer <number:0..300> <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 167 `；EOL ` RVA 0x378ABA20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Setup delay timer value in milliseconds。

[条件 C-11f224781dc493d7](../../evidence/conditions-sets-007.md#c-11f224781dc493d7) · [参数 P-af9967c3ea88fb6c](../../evidence/parameters-sets-013.md#p-af9967c3ea88fb6c)

### path-068861

```text
(config-subif)# isdn skip-async-callerid-check <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 55 `；EOL ` RVA 0x378B7680 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-52c394276c9314d8](../../evidence/conditions-sets-032.md#c-52c394276c9314d8)

### path-068871

```text
(config-subif)# isdn skipsend-idverify <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 68 `；EOL ` RVA 0x378BB7D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f8be1b51cfec74d2](../../evidence/conditions-sets-096.md#c-f8be1b51cfec74d2)

### path-071221

```text
(config-subif)# isdn snmp busyout b-channel <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 95 `；EOL ` RVA 0x378A4FD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9f00fe88ba1a36f5](../../evidence/conditions-sets-061.md#c-9f00fe88ba1a36f5)

### path-068869

```text
(config-subif)# isdn spc <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 50 `；EOL ` RVA 0x378BBDA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-326b91e480a17915](../../evidence/conditions-sets-020.md#c-326b91e480a17915)

### path-068866

```text
(config-subif)# isdn spc deactivate <number:1..30> <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 51 `；EOL ` RVA 0x378BBAC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` B Channel Number。

[条件 C-3f5011aebed07349](../../evidence/conditions-sets-025.md#c-3f5011aebed07349) · [参数 P-4e09f7979df00976](../../evidence/parameters-sets-006.md#p-4e09f7979df00976)

### path-068867

```text
(config-subif)# isdn spc reactivate <number:0..30> <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 52 `；EOL ` RVA 0x378BBB08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` B Channel Number(0=any channel)。

[条件 C-49252ee545e5ed92](../../evidence/conditions-sets-029.md#c-49252ee545e5ed92) · [参数 P-6f2759984f87b1f1](../../evidence/parameters-sets-009.md#p-6f2759984f87b1f1)

### path-070082

```text
(config-subif)# isdn spid1 <string> <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 21 `；EOL ` RVA 0x378A98E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` spid1 string。

[条件 C-77a64291085e6bad](../../evidence/conditions-sets-047.md#c-77a64291085e6bad) · [参数 P-0811e3173d33fb8f](../../evidence/parameters-sets-001.md#p-0811e3173d33fb8f)

### path-070095

```text
(config-subif)# isdn spid2 <string> <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 20 `；EOL ` RVA 0x378A9CE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` spid2 string。

[条件 C-5c93bab76799b73c](../../evidence/conditions-sets-036.md#c-5c93bab76799b73c) · [参数 P-99216c2f663fd8f7](../../evidence/parameters-sets-012.md#p-99216c2f663fd8f7)

### path-068868

```text
(config-subif)# isdn spoofing <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 155 `；EOL ` RVA 0x378BC6D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-39afc1fb18d9c3b3](../../evidence/conditions-sets-022.md#c-39afc1fb18d9c3b3)

### path-068198

```text
(config-subif)# isdn static-tei <number:0..63> <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 53 `；EOL ` RVA 0x378BB148 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Static TEI Number。

[条件 C-1b9a05097c564b54](../../evidence/conditions-sets-011.md#c-1b9a05097c564b54) · [参数 P-6f99f3a79e3ac896](../../evidence/parameters-sets-009.md#p-6f99f3a79e3ac896)

### path-070165

```text
(config-subif)# isdn supp-service callRerouteing <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 126 `；EOL ` RVA 0x378B1240 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f4d6c5fa733b5066](../../evidence/conditions-sets-094.md#c-f4d6c5fa733b5066) · [状态效果 S-943015dbe424ca57](../../evidence/state_effects-sets-031.md#s-943015dbe424ca57)

### path-069954

```text
(config-subif)# isdn switch-type basic-net3 <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 5 `；EOL ` RVA 0x378A4378 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-41fc4d8e650b1091](../../evidence/conditions-sets-026.md#c-41fc4d8e650b1091) · [状态效果 S-a90543e3d0b176c0](../../evidence/state_effects-sets-036.md#s-a90543e3d0b176c0)

### path-068837

```text
(config-subif)# isdn tei-negotiation <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 8 `；EOL ` RVA 0x378A8CB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-878a2de2c6df62aa](../../evidence/conditions-sets-052.md#c-878a2de2c6df62aa)

### path-068870

```text
(config-subif)# isdn timeout-signaling <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 69 `；EOL ` RVA 0x378BB4F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-67291da352c5e0c8](../../evidence/conditions-sets-040.md#c-67291da352c5e0c8)

### path-071374

```text
(config-subif)# isdn timer T-Activate <number:1000..15000> <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 133 `；EOL ` RVA 0x378A71B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timer T-Activate value in milliseconds。

[条件 C-044dc7f221c176d0](../../evidence/conditions-sets-002.md#c-044dc7f221c176d0) · [参数 P-3a264fe7f892e776](../../evidence/parameters-sets-005.md#p-3a264fe7f892e776)

### path-071253

```text
(config-subif)# isdn timer T200 <number:400..400000> <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 143 `；EOL ` RVA 0x378A5398 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timer T200 value in milliseconds。

[条件 C-fd2f854bda9631df](../../evidence/conditions-sets-098.md#c-fd2f854bda9631df) · [参数 P-9c27b4db8cf9eba4](../../evidence/parameters-sets-012.md#p-9c27b4db8cf9eba4)

### path-071272

```text
(config-subif)# isdn timer T203 <number:400..400000> <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 142 `；EOL ` RVA 0x378A56E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timer T203 value in milliseconds。

[条件 C-7b012a249079e8be](../../evidence/conditions-sets-048.md#c-7b012a249079e8be) · [参数 P-05734ec61ee459fd](../../evidence/parameters-sets-001.md#p-05734ec61ee459fd)

### path-071292

```text
(config-subif)# isdn timer T301 <number:180000..86400000> <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 141 `；EOL ` RVA 0x378A5A38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timer T301 in milliseconds.。

[条件 C-84bb22bab0e22830](../../evidence/conditions-sets-051.md#c-84bb22bab0e22830) · [参数 P-159478846247ceae](../../evidence/parameters-sets-002.md#p-159478846247ceae)

### path-071305

```text
(config-subif)# isdn timer T303 <number:400..86400000> <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 140 `；EOL ` RVA 0x378A5D88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timer T303 in milliseconds.。

[条件 C-35e750f404683b50](../../evidence/conditions-sets-021.md#c-35e750f404683b50) · [参数 P-3f6d5cfdfad55025](../../evidence/parameters-sets-005.md#p-3f6d5cfdfad55025)

### path-071315

```text
(config-subif)# isdn timer T306 <number:400..86400000> <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 139 `；EOL ` RVA 0x378A60D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timer T306 value in milliseconds。

[条件 C-b5fcfbb93f3d4418](../../evidence/conditions-sets-070.md#c-b5fcfbb93f3d4418) · [参数 P-61efbd286dd65b2b](../../evidence/parameters-sets-008.md#p-61efbd286dd65b2b)

### path-071344

```text
(config-subif)# isdn timer T307 <number:30000..300000> <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 138 `；EOL ` RVA 0x378A6468 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timer T307 value in milliseconds。

[条件 C-5f84f9723d57f032](../../evidence/conditions-sets-037.md#c-5f84f9723d57f032) · [参数 P-d940251c663b7cca](../../evidence/parameters-sets-016.md#p-d940251c663b7cca)

### path-071343

```text
(config-subif)# isdn timer T309 <number:0..86400000> <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 137 `；EOL ` RVA 0x378A67C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timer value in milliseconds or 0 to Disable.。

[条件 C-c35e4e7d967f741c](../../evidence/conditions-sets-075.md#c-c35e4e7d967f741c) · [参数 P-b19e5d247e5d9c2f](../../evidence/parameters-sets-013.md#p-b19e5d247e5d9c2f)

### path-071352

```text
(config-subif)# isdn timer T310 <number:400..400000> <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 136 `；EOL ` RVA 0x378A6B18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timer T310 value in milliseconds。

[条件 C-dd9a08d73111f643](../../evidence/conditions-sets-085.md#c-dd9a08d73111f643) · [参数 P-72c5104f78d4222f](../../evidence/parameters-sets-009.md#p-72c5104f78d4222f)

### path-071363

```text
(config-subif)# isdn timer T321 <number:0..86400000> <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 134 `；EOL ` RVA 0x378A6E68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timer T321 in milliseconds or 0 to Disable.。

[条件 C-fdd7c048ef39ca91](../../evidence/conditions-sets-098.md#c-fdd7c048ef39ca91) · [参数 P-68b03c4fd3458dd3](../../evidence/parameters-sets-008.md#p-68b03c4fd3458dd3)

### path-071384

```text
(config-subif)# isdn timer T3OOS <number:500..86400000> <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 132 `；EOL ` RVA 0x378A74E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timer T3OS in milliseconds.。

[条件 C-a548af478a7d43c2](../../evidence/conditions-sets-064.md#c-a548af478a7d43c2) · [参数 P-d29f9bf70e498f63](../../evidence/parameters-sets-016.md#p-d29f9bf70e498f63)

### path-068178

```text
(config-subif)# isdn transition-delay <number:1..3600> <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 123 `；EOL ` RVA 0x378A7808 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Line transition delay in seconds。

[条件 C-af718b5798ffea5a](../../evidence/conditions-sets-068.md#c-af718b5798ffea5a) · [参数 P-5393f796939a4449](../../evidence/parameters-sets-007.md#p-5393f796939a4449)

### path-068792

```text
(config-subif)# isdn twait-disable <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 49 `；EOL ` RVA 0x378A8970 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7cca8f61eb32f163](../../evidence/conditions-sets-048.md#c-7cca8f61eb32f163)

### path-069940

```text
(config-subif)# isis adjacency-filter <string> <cr>
```

Handler ` RVA 0xFD2D980 `；selector ` 23 `；EOL ` RVA 0x34B83000 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of filter expression or set。

[条件 C-2eb914228e52a053](../../evidence/conditions-sets-018.md#c-2eb914228e52a053) · [参数 P-d209d6b128eb20ae](../../evidence/parameters-sets-016.md#p-d209d6b128eb20ae)

### path-069711

```text
(config-subif)# isis advertise prefix <cr>
```

Handler ` RVA 0xFD2D980 `；selector ` 82 `；EOL ` RVA 0x34B80DF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3fb58df82ff6286a](../../evidence/conditions-sets-025.md#c-3fb58df82ff6286a)

### path-071040

```text
(config-subif)# isis authentication key-chain <string> <cr>
```

Handler ` RVA 0xFD2D980 `；selector ` 5 `；EOL ` RVA 0x34B7F8C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of key-chain。

[条件 C-3fb58df82ff6286a](../../evidence/conditions-sets-025.md#c-3fb58df82ff6286a) · [参数 P-ef5db84a4ff45910](../../evidence/parameters-sets-018.md#p-ef5db84a4ff45910) · [状态效果 S-f2044f695970575f](../../evidence/state_effects-sets-051.md#s-f2044f695970575f)

### path-071014

```text
(config-subif)# isis authentication mode md5 <cr>
```

Handler ` RVA 0xFD2D980 `；selector ` 4 `；EOL ` RVA 0x34B7F478 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3fb58df82ff6286a](../../evidence/conditions-sets-025.md#c-3fb58df82ff6286a) · [状态效果 S-ff4273b02f0d1e2f](../../evidence/state_effects-sets-054.md#s-ff4273b02f0d1e2f)

### path-069761

```text
(config-subif)# isis authentication send-only <cr>
```

Handler ` RVA 0xFD2D980 `；selector ` 6 `；EOL ` RVA 0x34B7FC70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3fb58df82ff6286a](../../evidence/conditions-sets-025.md#c-3fb58df82ff6286a) · [状态效果 S-aa3c634d82b16be5](../../evidence/state_effects-sets-036.md#s-aa3c634d82b16be5)

### path-068777

```text
(config-subif)# isis bfd <cr>
```

Handler ` RVA 0xFD2D980 `；selector ` 88 `；EOL ` RVA 0x34B83A18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a0ebd72797fe42a8](../../evidence/conditions-sets-062.md#c-a0ebd72797fe42a8)

### path-069589

```text
(config-subif)# isis campus-lisp <string> <cr>
```

Handler ` RVA 0xFD2D7E0 `；selector ` 3 `；EOL ` RVA 0x34B7F040 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Tag Name。

[条件 C-3fb58df82ff6286a](../../evidence/conditions-sets-025.md#c-3fb58df82ff6286a) · [参数 P-3a3fe7bf5f7e9759](../../evidence/parameters-sets-005.md#p-3a3fe7bf5f7e9759)

### path-068593

```text
(config-subif)# isis circuit-type <cr>
```

Handler ` RVA 0xFD2D980 `；selector ` 9 `；EOL ` RVA 0x34B7D830 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-228db79bddbd1b23](../../evidence/conditions-sets-014.md#c-228db79bddbd1b23) · [状态效果 S-f21ebb818399ea0e](../../evidence/state_effects-sets-051.md#s-f21ebb818399ea0e)

### path-069906

```text
(config-subif)# isis csnp-interval <number:0..65535> <cr>
```

Handler ` RVA 0xFD2D980 `；selector ` 12 `；EOL ` RVA 0x34B82090 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` CSNP interval value。

[条件 C-3fb58df82ff6286a](../../evidence/conditions-sets-025.md#c-3fb58df82ff6286a) · [参数 P-1735bbd03a43c4f7](../../evidence/parameters-sets-002.md#p-1735bbd03a43c4f7) · [状态效果 S-9352edd6699d16d2](../../evidence/state_effects-sets-031.md#s-9352edd6699d16d2)

### path-069830

```text
(config-subif)# isis hello padding <cr>
```

Handler ` RVA 0xFD2D980 `；selector ` 32 `；EOL ` RVA 0x34B81978 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3fb58df82ff6286a](../../evidence/conditions-sets-025.md#c-3fb58df82ff6286a)

### path-069788

```text
(config-subif)# isis hello-interval <number:1..65535> <cr>
```

Handler ` RVA 0xFD2D980 `；selector ` 10 `；EOL ` RVA 0x34B809C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Hello interval value。

[条件 C-3fb58df82ff6286a](../../evidence/conditions-sets-025.md#c-3fb58df82ff6286a) · [参数 P-a0072125b79ce2a3](../../evidence/parameters-sets-012.md#p-a0072125b79ce2a3) · [状态效果 S-49b2c996a8bfaa4c](../../evidence/state_effects-sets-016.md#s-49b2c996a8bfaa4c)

### path-069759

```text
(config-subif)# isis hello-multiplier <number:3..1000> <cr>
```

Handler ` RVA 0xFD2D980 `；selector ` 11 `；EOL ` RVA 0x34B80550 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Hello multiplier value。

[条件 C-3fb58df82ff6286a](../../evidence/conditions-sets-025.md#c-3fb58df82ff6286a) · [参数 P-97287084e3b4937f](../../evidence/parameters-sets-012.md#p-97287084e3b4937f) · [状态效果 S-93c84a58922afc37](../../evidence/state_effects-sets-031.md#s-93c84a58922afc37)

### path-070020

```text
(config-subif)# isis ipv6 bfd <cr>
```

Handler ` RVA 0x11A9E1E0 `；selector ` 78 `；EOL ` RVA 0x355D6A38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c693c6287d426beb](../../evidence/conditions-sets-076.md#c-c693c6287d426beb)

### path-071339

```text
(config-subif)# isis ipv6 metric <number:1..16777214> <cr>
```

Handler ` RVA 0x11A9E1E0 `；selector ` 76 `；EOL ` RVA 0x355D65D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Default metric。

[条件 C-1e49a2dde3782fe4](../../evidence/conditions-sets-012.md#c-1e49a2dde3782fe4) · [参数 P-7592a2c68b91a12b](../../evidence/parameters-sets-009.md#p-7592a2c68b91a12b) · [状态效果 S-89435c5fda67db25](../../evidence/state_effects-sets-029.md#s-89435c5fda67db25)

### path-071342

```text
(config-subif)# isis ipv6 tag <number:1..4294967295> <cr>
```

Handler ` RVA 0x11A9E1E0 `；selector ` 77 `；EOL ` RVA 0x355D6DB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Admin tag number。

[条件 C-65f8bcc5422a4f47](../../evidence/conditions-sets-039.md#c-65f8bcc5422a4f47) · [参数 P-fd8285d716258857](../../evidence/parameters-sets-019.md#p-fd8285d716258857)

### path-068162

```text
(config-subif)# isis lsp-interval <number:1..4294967295> <cr>
```

Handler ` RVA 0xFD2D980 `；selector ` 15 `；EOL ` RVA 0x34B82658 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` LSP transmission interval (milliseconds)。

[条件 C-c348aa4011f8e989](../../evidence/conditions-sets-075.md#c-c348aa4011f8e989) · [参数 P-d6a1e01d8718921c](../../evidence/parameters-sets-016.md#p-d6a1e01d8718921c)

### path-069924

```text
(config-subif)# isis mesh-group <number:1..4294967295> <cr>
```

Handler ` RVA 0xFD2D980 `；selector ` 44 `；EOL ` RVA 0x34B82C60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Mesh group number。

[条件 C-f9474515075cbd28](../../evidence/conditions-sets-096.md#c-f9474515075cbd28) · [参数 P-000438cb9327a460](../../evidence/parameters-sets-001.md#p-000438cb9327a460)

### path-069650

```text
(config-subif)# isis metric <number:1..16777214> <cr>
```

Handler ` RVA 0xFD2D980 `；selector ` 7 `；EOL ` RVA 0x34B7E1B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Default metric。

[条件 C-bcf13fb2e5615cdd](../../evidence/conditions-sets-073.md#c-bcf13fb2e5615cdd) · [参数 P-d388070177c96667](../../evidence/parameters-sets-016.md#p-d388070177c96667) · [状态效果 S-d309e281476fb121](../../evidence/state_effects-sets-045.md#s-d309e281476fb121)

### path-069536

```text
(config-subif)# isis network point-to-point <cr>
```

Handler ` RVA 0xFD2D980 `；selector ` 50 `；EOL ` RVA 0x34B7DC88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bba56491eb170e9c](../../evidence/conditions-sets-072.md#c-bba56491eb170e9c) · [状态效果 S-77725916734774af](../../evidence/state_effects-sets-025.md#s-77725916734774af)

### path-069726

```text
(config-subif)# isis password <string> <cr>
```

Handler ` RVA 0xFD2D980 `；selector ` 2 `；EOL ` RVA 0x34B7EC78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Password。

[条件 C-549e368784755a49](../../evidence/conditions-sets-033.md#c-549e368784755a49) · [参数 P-f2738e45c8491b03](../../evidence/parameters-sets-018.md#p-f2738e45c8491b03) · [状态效果 S-c3069bf4cefb10c2](../../evidence/state_effects-sets-041.md#s-c3069bf4cefb10c2)

### path-069837

```text
(config-subif)# isis prefix-attributes n-flag-clear <cr>
```

Handler ` RVA 0xFD2D980 `；selector ` 83 `；EOL ` RVA 0x34B81198 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3fb58df82ff6286a](../../evidence/conditions-sets-025.md#c-3fb58df82ff6286a) · [状态效果 S-f005248cd1f54679](../../evidence/state_effects-sets-051.md#s-f005248cd1f54679)

### path-069724

```text
(config-subif)# isis priority <number:0..127> <cr>
```

Handler ` RVA 0xFD2D980 `；selector ` 1 `；EOL ` RVA 0x34B800D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Priority value。

[条件 C-3fb58df82ff6286a](../../evidence/conditions-sets-025.md#c-3fb58df82ff6286a) · [参数 P-9782a48c49c94a24](../../evidence/parameters-sets-012.md#p-9782a48c49c94a24) · [状态效果 S-bc8c833e6b38113c](../../evidence/state_effects-sets-040.md#s-bc8c833e6b38113c)

### path-069934

```text
(config-subif)# isis protocol shutdown <cr>
```

Handler ` RVA 0xFD2D980 `；selector ` 90 `；EOL ` RVA 0x34B83388 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3fb58df82ff6286a](../../evidence/conditions-sets-025.md#c-3fb58df82ff6286a)

### path-069947

```text
(config-subif)# isis remote-psnp-delay <number:1..10000> <cr>
```

Handler ` RVA 0xFD2D980 `；selector ` 140 `；EOL ` RVA 0x34B836D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Remote PSNP delay in msec。

[条件 C-b8207e29f25fc698](../../evidence/conditions-sets-071.md#c-b8207e29f25fc698) · [参数 P-645e7d1df9128018](../../evidence/parameters-sets-008.md#p-645e7d1df9128018)

### path-068158

```text
(config-subif)# isis retransmit-interval <number:0..65535> <cr>
```

Handler ` RVA 0xFD2D980 `；selector ` 13 `；EOL ` RVA 0x34B823B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Interval between retransmissions of the same LSP (seconds)。

[条件 C-4450f132948299ec](../../evidence/conditions-sets-027.md#c-4450f132948299ec) · [参数 P-90bd1d20c13bdf79](../../evidence/parameters-sets-011.md#p-90bd1d20c13bdf79)

### path-068155

```text
(config-subif)# isis retransmit-throttle-interval <number:0..65535> <cr>
```

Handler ` RVA 0xFD2D980 `；selector ` 14 `；EOL ` RVA 0x34B81F70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Delay between retransmitted LSPs (milliseconds)。

[条件 C-f1e726b90611baec](../../evidence/conditions-sets-093.md#c-f1e726b90611baec) · [参数 P-c0932dccb0d58de5](../../evidence/parameters-sets-015.md#p-c0932dccb0d58de5)

### path-069821

```text
(config-subif)# isis tag <number:1..4294967295> <cr>
```

Handler ` RVA 0xFD2D980 `；selector ` 33 `；EOL ` RVA 0x34B81CC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Admin tag number。

[条件 C-3fb58df82ff6286a](../../evidence/conditions-sets-025.md#c-3fb58df82ff6286a) · [参数 P-2bcc68113a35d186](../../evidence/parameters-sets-004.md#p-2bcc68113a35d186)

### path-070967

```text
(config-subif)# isis te-metric flex-algo <number:1..16777214> <cr>
```

Handler ` RVA 0xFD2D980 `；selector ` 8 `；EOL ` RVA 0x34B7E7A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` te-metric value。

[条件 C-f74c178e736ee7da](../../evidence/conditions-sets-095.md#c-f74c178e736ee7da) · [参数 P-aedb4257829ae206](../../evidence/parameters-sets-013.md#p-aedb4257829ae206) · [状态效果 S-f4271e461d2139e4](../../evidence/state_effects-sets-052.md#s-f4271e461d2139e4)

### path-068717

```text
(config-subif)# isis three-way-handshake <cr>
```

Handler ` RVA 0xFD2D980 `；selector ` 49 `；EOL ` RVA 0x34B81568 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-44ca805f4a060cd9](../../evidence/conditions-sets-027.md#c-44ca805f4a060cd9) · [状态效果 S-e80de0abc1519f60](../../evidence/state_effects-sets-049.md#s-e80de0abc1519f60)

### path-069531

```text
(config-subif)# iso-igrp adjacency-filter <string> <cr>
```

Handler ` RVA 0x10588700 `；selector ` 0 `；EOL ` RVA 0x34B83EE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of filter set or expression。

[条件 C-2903d4e6c70b3112](../../evidence/conditions-sets-016.md#c-2903d4e6c70b3112) · [参数 P-4e4c701f4d469f12](../../evidence/parameters-sets-006.md#p-4e4c701f4d469f12)

### path-072546

```text
(config-subif)# itu channel <?number_help_func_action@555589695e58> <cr>
```

Handler ` RVA 0xDFFD9F0 `；selector ` 0 `；EOL ` RVA 0x34141E80 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7bc0e35b7ffe3d99](../../evidence/conditions-sets-048.md#c-7bc0e35b7ffe3d99) · [缺口 G-da2769156cd8b902](../../evidence/gaps-sets-008.md#g-da2769156cd8b902)

### path-068068

```text
(config-subif)# keepalive <cr>
```

Handler ` RVA 0xDEC5F30 `；selector ` 0 `；EOL ` RVA 0x340914D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2d0d035333588381](../../evidence/conditions-sets-018.md#c-2d0d035333588381) · [状态效果 S-ff95ac2698deef93](../../evidence/state_effects-sets-054.md#s-ff95ac2698deef93)

### path-072530

```text
(config-subif)# keepalive <number:dynamic> <cr>
```

Handler ` RVA 0xDEC5F30 `；selector ` 0 `；EOL ` RVA 0x340914D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Keepalive period (default 10 seconds)。

[条件 C-ce0d777faf9b115f](../../evidence/conditions-sets-079.md#c-ce0d777faf9b115f) · [缺口 G-57310d87f91bbbec](../../evidence/gaps-sets-004.md#g-57310d87f91bbbec) · [参数 P-0d85b54549497a3a](../../evidence/parameters-sets-001.md#p-0d85b54549497a3a) · [状态效果 S-ff95ac2698deef93](../../evidence/state_effects-sets-054.md#s-ff95ac2698deef93)

### path-072536

```text
(config-subif)# l2protocol drop <cr>
```

Handler ` RVA 0xBF8F6F0 `；selector ` 4 `；EOL ` RVA 0x33960EA0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-37ecdb4abbd3c11a](../../evidence/conditions-sets-022.md#c-37ecdb4abbd3c11a) · [缺口 G-154e34f447567b9b](../../evidence/gaps-sets-001.md#g-154e34f447567b9b) · [状态效果 S-64f711a2efaeb388](../../evidence/state_effects-sets-022.md#s-64f711a2efaeb388)

### path-068856

```text
(config-subif)# l2protocol forward <cr>
```

Handler ` RVA 0x15FDB140 `；selector ` 26 `；EOL ` RVA 0x35E8E0B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-055572e2bff89fa1](../../evidence/conditions-sets-002.md#c-055572e2bff89fa1) · [状态效果 S-2311d6703aeb6b0a](../../evidence/state_effects-sets-008.md#s-2311d6703aeb6b0a)

### path-070201

```text
(config-subif)# l2protocol forward drop-threshold <cr>
```

Handler ` RVA 0x15FDB140 `；selector ` 28 `；EOL ` RVA 0x35E8D518 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-510491b855007b1b](../../evidence/conditions-sets-032.md#c-510491b855007b1b) · [状态效果 S-f7708fa9f1742669](../../evidence/state_effects-sets-052.md#s-f7708fa9f1742669)

### path-070197

```text
(config-subif)# l2protocol forward shutdown-threshold <cr>
```

Handler ` RVA 0x15FDB140 `；selector ` 27 `；EOL ` RVA 0x35E8C870 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-50b8430438ab0b42](../../evidence/conditions-sets-031.md#c-50b8430438ab0b42) · [状态效果 S-2f9442ea3efb7609](../../evidence/state_effects-sets-011.md#s-2f9442ea3efb7609)

### path-068197

```text
(config-subif)# l2protocol-tunnel <cr>
```

Handler ` RVA 0x15FDB140 `；selector ` 11 `；EOL ` RVA 0x35E8B398 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-401138b8c763a6a0](../../evidence/conditions-sets-025.md#c-401138b8c763a6a0)

### path-068852

```text
(config-subif)# l2protocol-tunnel drop-threshold <cr>
```

Handler ` RVA 0x15FDB140 `；selector ` 10 `；EOL ` RVA 0x35E8A800 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d30cee6a4a23afb6](../../evidence/conditions-sets-081.md#c-d30cee6a4a23afb6)

### path-068850

```text
(config-subif)# l2protocol-tunnel shutdown-threshold <cr>
```

Handler ` RVA 0x15FDB140 `；selector ` 9 `；EOL ` RVA 0x35E89B30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-24b655d14db5af15](../../evidence/conditions-sets-014.md#c-24b655d14db5af15)

### path-069862

```text
(config-subif)# lacp device-id <address> <cr>
```

Handler ` RVA 0xC8D1EA0 `；selector ` 11 `；EOL ` RVA 0x33B139E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` MAC address。

[条件 C-f0e96dd640fa1161](../../evidence/conditions-sets-093.md#c-f0e96dd640fa1161) · [参数 P-c2e04e6a439bdce5](../../evidence/parameters-sets-015.md#p-c2e04e6a439bdce5)

### path-068695

```text
(config-subif)# lacp direct-loadswap <cr>
```

Handler ` RVA 0xC8D1EA0 `；selector ` 7 `；EOL ` RVA 0x33B13308 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f381c4d6997b8374](../../evidence/conditions-sets-094.md#c-f381c4d6997b8374)

### path-069698

```text
(config-subif)# lacp failover non-revertive <cr>
```

Handler ` RVA 0xC8D11D0 `；selector ` 10 `；EOL ` RVA 0x33B12618 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-eea0d6379185273f](../../evidence/conditions-sets-092.md#c-eea0d6379185273f) · [状态效果 S-90a3caa64f09cb9a](../../evidence/state_effects-sets-031.md#s-90a3caa64f09cb9a)

### path-068672

```text
(config-subif)# lacp fast-switchover <cr>
```

Handler ` RVA 0xC8D1EA0 `；selector ` 3 `；EOL ` RVA 0x33B129A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-288149ec680e4cd3](../../evidence/conditions-sets-016.md#c-288149ec680e4cd3)

### path-068658

```text
(config-subif)# lacp fast-switchover dampening <number:30..180> <cr>
```

Handler ` RVA 0xC8D1EA0 `；selector ` 12 `；EOL ` RVA 0x33B12940 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` LACP Fast Switchover Hot-Standby Dampening Time in Seconds。

[条件 C-7318afe1c26cd50b](../../evidence/conditions-sets-045.md#c-7318afe1c26cd50b) · [参数 P-29e93e5247e241c7](../../evidence/parameters-sets-004.md#p-29e93e5247e241c7)

### path-072589

```text
(config-subif)# lacp max-bundle <number:dynamic> <cr>
```

Handler ` RVA 0xC8D1EA0 `；selector ` 5 `；EOL ` RVA 0x33B12FA0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Max number of ports to bundle in this Port Channel。

[条件 C-3e79edb7bbfd7001](../../evidence/conditions-sets-024.md#c-3e79edb7bbfd7001) · [缺口 G-e4e6ed51b0d3fc56](../../evidence/gaps-sets-008.md#g-e4e6ed51b0d3fc56) · [参数 P-63c68d080a9c9a31](../../evidence/parameters-sets-008.md#p-63c68d080a9c9a31)

### path-072591

```text
(config-subif)# lacp min-bundle <number:dynamic> <cr>
```

Handler ` RVA 0xC8D1EA0 `；selector ` 4 `；EOL ` RVA 0x33B13678 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Minimum number of ports to bundle in this Port Channel。

[条件 C-8c54c5c9919c66fc](../../evidence/conditions-sets-054.md#c-8c54c5c9919c66fc) · [缺口 G-fad6954b6fbdced6](../../evidence/gaps-sets-009.md#g-fad6954b6fbdced6) · [参数 P-e77b3d0100aaf93a](../../evidence/parameters-sets-017.md#p-e77b3d0100aaf93a)

### path-069674

```text
(config-subif)# lacp port-priority <number:0..65535> <cr>
```

Handler ` RVA 0xC8D1EA0 `；selector ` 1 `；EOL ` RVA 0x33B11E08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Priority value。

[条件 C-a78cef374ce4091b](../../evidence/conditions-sets-065.md#c-a78cef374ce4091b) · [参数 P-aaaa7b9149319c4b](../../evidence/parameters-sets-013.md#p-aaaa7b9149319c4b)

### path-069735

```text
(config-subif)# lacp rate normal <cr>
```

Handler ` RVA 0xC8D1EA0 `；selector ` 9 `；EOL ` RVA 0x33B12170 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e0ed4e56e20642ab](../../evidence/conditions-sets-087.md#c-e0ed4e56e20642ab) · [状态效果 S-ff2be8e6d23b0974](../../evidence/state_effects-sets-054.md#s-ff2be8e6d23b0974)

### path-068385

```text
(config-subif)# lan-name <string> <cr>
```

Handler ` RVA 0x114FAAD0 `；selector ` 21 `；EOL ` RVA 0x355150A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Up to 8 characters lan name。

[条件 C-892a7f7dda9305cb](../../evidence/conditions-sets-053.md#c-892a7f7dda9305cb) · [参数 P-10d3add38516413e](../../evidence/parameters-sets-002.md#p-10d3add38516413e)

### path-072568

```text
(config-subif)# lapb N1 <number:dynamic> <cr>
```

Handler ` RVA 0xFDBBC40 `；selector ` 5 `；EOL ` RVA 0x348D8950 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` LAPB N1 parameter (bits; multiple of 8)。

[条件 C-3dedae771762817e](../../evidence/conditions-sets-024.md#c-3dedae771762817e) · [缺口 G-9d1078143b5ae9f9](../../evidence/gaps-sets-006.md#g-9d1078143b5ae9f9) · [参数 P-afa6b0d0d5bce919](../../evidence/parameters-sets-013.md#p-afa6b0d0d5bce919)

### path-068090

```text
(config-subif)# lapb N2 <number:1..255> <cr>
```

Handler ` RVA 0xFDBBC40 `；selector ` 6 `；EOL ` RVA 0x348D88B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` LAPB N2 parameter (transmit count)。

[条件 C-dd05a8e320d1ed42](../../evidence/conditions-sets-085.md#c-dd05a8e320d1ed42) · [参数 P-9407e6838a05fff2](../../evidence/parameters-sets-011.md#p-9407e6838a05fff2)

### path-068077

```text
(config-subif)# lapb T1 <number:1..64000> <cr>
```

Handler ` RVA 0xFDBBC40 `；selector ` 1 `；EOL ` RVA 0x348D7A30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` LAPB T1 parameter (milliseconds)。

[条件 C-ae9f7a6498b2830b](../../evidence/conditions-sets-068.md#c-ae9f7a6498b2830b) · [参数 P-10874122c24cd7ad](../../evidence/parameters-sets-002.md#p-10874122c24cd7ad)

### path-068079

```text
(config-subif)# lapb T2 <number:1..32000> <cr>
```

Handler ` RVA 0xFDBBC40 `；selector ` 2 `；EOL ` RVA 0x348D7DC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` LAPB T2 parameter (milliseconds)。

[条件 C-a3ff19f820ce5971](../../evidence/conditions-sets-063.md#c-a3ff19f820ce5971) · [参数 P-d3e87a6ff0ec88f2](../../evidence/parameters-sets-016.md#p-d3e87a6ff0ec88f2)

### path-068083

```text
(config-subif)# lapb T4 <number:0..255> <cr>
```

Handler ` RVA 0xFDBBC40 `；selector ` 4 `；EOL ` RVA 0x348D8308 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` LAPB T4 parameter (seconds)。

[条件 C-fc8feb1f18a22f52](../../evidence/conditions-sets-097.md#c-fc8feb1f18a22f52) · [参数 P-4964e4f7ee9fdab9](../../evidence/parameters-sets-006.md#p-4964e4f7ee9fdab9)

### path-068081

```text
(config-subif)# lapb interface-outage <number:0..64000> <cr>
```

Handler ` RVA 0xFDBBC40 `；selector ` 3 `；EOL ` RVA 0x348D8068 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Allowable interface outage (milliseconds)。

[条件 C-93665ac55c79c9c9](../../evidence/conditions-sets-057.md#c-93665ac55c79c9c9) · [参数 P-1f73db22ee12a51a](../../evidence/parameters-sets-003.md#p-1f73db22ee12a51a)

### path-068092

```text
(config-subif)# lapb k <number:1..127> <cr>
```

Handler ` RVA 0xFDBBC40 `；selector ` 7 `；EOL ` RVA 0x348D8C18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` LAPB k parameter (frames)。

[条件 C-9bdafd840d2bf816](../../evidence/conditions-sets-060.md#c-9bdafd840d2bf816) · [参数 P-e5e128729fbe8023](../../evidence/parameters-sets-017.md#p-e5e128729fbe8023)

### path-069278

```text
(config-subif)# lapb modulo 8 <cr>
```

Handler ` RVA 0xFDBBC40 `；selector ` 0 `；EOL ` RVA 0x348D7AD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-634ea76d57e7d46a](../../evidence/conditions-sets-038.md#c-634ea76d57e7d46a) · [状态效果 S-29ee15b3063e9c1f](../../evidence/state_effects-sets-009.md#s-29ee15b3063e9c1f)

### path-068188

```text
(config-subif)# link <cr>
```

Handler ` RVA 0x15DD4900 `；selector ` 0 `；EOL ` RVA 0x35E2EF30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-05fdc74b4ea7e682](../../evidence/conditions-sets-003.md#c-05fdc74b4ea7e682)

### path-068835

```text
(config-subif)# link debounce <cr>
```

Handler ` RVA 0x15DB7330 `；selector ` 0 `；EOL ` RVA 0x35E2F010 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1150599215a51f3f](../../evidence/conditions-sets-007.md#c-1150599215a51f3f)

### path-072635

```text
(config-subif)# link debounce time <number:dynamic> <cr>
```

Handler ` RVA 0x15DB7330 `；selector ` 0 `；EOL ` RVA 0x35E2F010 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Extended debounce time value in ms。

[条件 C-1b430aeb168f9830](../../evidence/conditions-sets-011.md#c-1b430aeb168f9830) · [缺口 G-18a21d210450a5c3](../../evidence/gaps-sets-001.md#g-18a21d210450a5c3) · [参数 P-29d70afedb488c55](../../evidence/parameters-sets-004.md#p-29d70afedb488c55)

### path-068100

```text
(config-subif)# linksec-shim <cr>
```

Handler ` RVA 0x16072E80 `；selector ` 1 `；EOL ` RVA 0x35EAE5E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-05fdc74b4ea7e682](../../evidence/conditions-sets-003.md#c-05fdc74b4ea7e682)

### path-068161

```text
(config-subif)# llc2 N2 <number:1..255> <cr>
```

Handler ` RVA 0xFDDE8D0 `；selector ` 4 `；EOL ` RVA 0x348E02D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of times router should retry various operations。

[条件 C-9738eb2503327e45](../../evidence/conditions-sets-058.md#c-9738eb2503327e45) · [参数 P-08c85de6456967bf](../../evidence/parameters-sets-001.md#p-08c85de6456967bf)

### path-068152

```text
(config-subif)# llc2 ack-delay-time <number:1..60000> <cr>
```

Handler ` RVA 0xFDDE8D0 `；selector ` 1 `；EOL ` RVA 0x348DFAF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Ack delay time in milliseconds。

[条件 C-cf4af35b5319ed5b](../../evidence/conditions-sets-080.md#c-cf4af35b5319ed5b) · [参数 P-fb8ad230a4bfd966](../../evidence/parameters-sets-019.md#p-fb8ad230a4bfd966)

### path-068150

```text
(config-subif)# llc2 ack-max <number:1..255> <cr>
```

Handler ` RVA 0xFDDE8D0 `；selector ` 0 `；EOL ` RVA 0x348DF5B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Ack max。

[条件 C-614484d721571c1a](../../evidence/conditions-sets-038.md#c-614484d721571c1a) · [参数 P-94ed8054e7266dfa](../../evidence/parameters-sets-011.md#p-94ed8054e7266dfa)

### path-068179

```text
(config-subif)# llc2 adm-timer-value <number:0..60000> <cr>
```

Handler ` RVA 0xFDDE8D0 `；selector ` 19 `；EOL ` RVA 0x348E1530 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Wait time for session activation in milliseconds。

[条件 C-fe7e4bd875615c4d](../../evidence/conditions-sets-098.md#c-fe7e4bd875615c4d) · [参数 P-29874ac16e204578](../../evidence/parameters-sets-004.md#p-29874ac16e204578)

### path-068151

```text
(config-subif)# llc2 akdelay-time <number:1..60000> <cr>
```

Handler ` RVA 0xFDDE8D0 `；selector ` 1 `；EOL ` RVA 0x348DF850 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9a748990657481dd](../../evidence/conditions-sets-060.md#c-9a748990657481dd) · [参数 P-bf81a35d53f20923](../../evidence/parameters-sets-015.md#p-bf81a35d53f20923)

### path-068148

```text
(config-subif)# llc2 akmax <number:1..255> <cr>
```

Handler ` RVA 0xFDDE8D0 `；selector ` 0 `；EOL ` RVA 0x348DF570 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c67936202b6a42af](../../evidence/conditions-sets-076.md#c-c67936202b6a42af) · [参数 P-03f92491335f9b35](../../evidence/parameters-sets-001.md#p-03f92491335f9b35)

### path-068803

```text
(config-subif)# llc2 dynwind <cr>
```

Handler ` RVA 0xFDDE8D0 `；selector ` 18 `；EOL ` RVA 0x348E1E60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6f34ec6c7bc357ea](../../evidence/conditions-sets-043.md#c-6f34ec6c7bc357ea)

### path-068154

```text
(config-subif)# llc2 idle-time <number:1..60000> <cr>
```

Handler ` RVA 0xFDDE8D0 `；selector ` 2 `；EOL ` RVA 0x348DFD90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Frequency of polls in milliseconds。

[条件 C-440f51c65f5ef570](../../evidence/conditions-sets-027.md#c-440f51c65f5ef570) · [参数 P-9d8a7c0a9115274a](../../evidence/parameters-sets-012.md#p-9d8a7c0a9115274a)

### path-068157

```text
(config-subif)# llc2 local-window <number:1..127> <cr>
```

Handler ` RVA 0xFDDE8D0 `；selector ` 3 `；EOL ` RVA 0x348E0030 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Max number of I-frames to send before waiting for an acknowledgment。

[条件 C-f6515329c685bd36](../../evidence/conditions-sets-095.md#c-f6515329c685bd36) · [参数 P-3922f998323e1d4b](../../evidence/parameters-sets-005.md#p-3922f998323e1d4b)

### path-068164

```text
(config-subif)# llc2 t1-time <number:1..60000> <cr>
```

Handler ` RVA 0xFDDE8D0 `；selector ` 5 `；EOL ` RVA 0x348E0570 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` T1 time in milliseconds。

[条件 C-be3692365cee82b0](../../evidence/conditions-sets-073.md#c-be3692365cee82b0) · [参数 P-618379c7b01cc6d2](../../evidence/parameters-sets-008.md#p-618379c7b01cc6d2)

### path-068167

```text
(config-subif)# llc2 tbusy-time <number:1..60000> <cr>
```

Handler ` RVA 0xFDDE8D0 `；selector ` 7 `；EOL ` RVA 0x348E0810 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Tbusy time in milliseconds。

[条件 C-36c2ef85e2d89f74](../../evidence/conditions-sets-021.md#c-36c2ef85e2d89f74) · [参数 P-88d678710eee567c](../../evidence/parameters-sets-011.md#p-88d678710eee567c)

### path-068171

```text
(config-subif)# llc2 tpf-time <number:1..60000> <cr>
```

Handler ` RVA 0xFDDE8D0 `；selector ` 9 `；EOL ` RVA 0x348E0D50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Tpf time in milliseconds。

[条件 C-5628f1864268bc92](../../evidence/conditions-sets-034.md#c-5628f1864268bc92) · [参数 P-7a1153b60efd54a8](../../evidence/parameters-sets-010.md#p-7a1153b60efd54a8)

### path-068169

```text
(config-subif)# llc2 trej-time <number:1..60000> <cr>
```

Handler ` RVA 0xFDDE8D0 `；selector ` 8 `；EOL ` RVA 0x348E0AB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Trej time in milliseconds。

[条件 C-17978ddff50487d1](../../evidence/conditions-sets-009.md#c-17978ddff50487d1) · [参数 P-6a546df6b842b238](../../evidence/parameters-sets-008.md#p-6a546df6b842b238)

### path-068182

```text
(config-subif)# llc2 txq-max <number:20..200> <cr>
```

Handler ` RVA 0xFDDE8D0 `；selector ` 12 `；EOL ` RVA 0x348E17D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Depth of queue in I-frames。

[条件 C-007f61c3eb9962d9](../../evidence/conditions-sets-001.md#c-007f61c3eb9962d9) · [参数 P-728dc4682cfacc1a](../../evidence/parameters-sets-009.md#p-728dc4682cfacc1a)

### path-068173

```text
(config-subif)# llc2 xid-neg-val-time <number:1..60000> <cr>
```

Handler ` RVA 0xFDDE8D0 `；selector ` 10 `；EOL ` RVA 0x348E0FF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Frequency of XID in milliseconds。

[条件 C-f3174f2c9abbc196](../../evidence/conditions-sets-094.md#c-f3174f2c9abbc196) · [参数 P-2afd698b26931713](../../evidence/parameters-sets-004.md#p-2afd698b26931713)

### path-068177

```text
(config-subif)# llc2 xid-retry-time <number:0..60000> <cr>
```

Handler ` RVA 0xFDDE8D0 `；selector ` 11 `；EOL ` RVA 0x348E1290 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Wait time for reply to XID in milliseconds。

[条件 C-ee4ddc1d7af3c8c2](../../evidence/conditions-sets-092.md#c-ee4ddc1d7af3c8c2) · [参数 P-5e89245cbe18d3c3](../../evidence/parameters-sets-008.md#p-5e89245cbe18d3c3)

### path-069438

```text
(config-subif)# lldp med-tlv-select network-policy <cr>
```

Handler ` RVA 0xC777860 `；selector ` 0 `；EOL ` RVA 0x33AE5810 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-31caba7e0853440a](../../evidence/conditions-sets-020.md#c-31caba7e0853440a) · [状态效果 S-6f8ce5d389b0ce28](../../evidence/state_effects-sets-024.md#s-6f8ce5d389b0ce28)

### path-068452

```text
(config-subif)# lldp receive <cr>
```

Handler ` RVA 0x158A1F50 `；selector ` 6 `；EOL ` RVA 0x35DA3F68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4f832e89cba0c01f](../../evidence/conditions-sets-031.md#c-4f832e89cba0c01f)

### path-069378

```text
(config-subif)# lldp tlv-select power-management <cr>
```

Handler ` RVA 0x158A1F50 `；selector ` 17 `；EOL ` RVA 0x35DA4278 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4f832e89cba0c01f](../../evidence/conditions-sets-031.md#c-4f832e89cba0c01f) · [状态效果 S-0eda02c9e4d2df05](../../evidence/state_effects-sets-004.md#s-0eda02c9e4d2df05)

### path-068439

```text
(config-subif)# lldp transmit <cr>
```

Handler ` RVA 0x158A1F50 `；selector ` 5 `；EOL ` RVA 0x35DA3CC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4f832e89cba0c01f](../../evidence/conditions-sets-031.md#c-4f832e89cba0c01f)

### path-070758

```text
(config-subif)# lldp ucs-chassis-tlv rack-id <number:1..255> <cr>
```

Handler ` RVA 0x158A5440 `；selector ` 21 `；EOL ` RVA 0x35DA4628 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Rack ID。

[条件 C-4f832e89cba0c01f](../../evidence/conditions-sets-031.md#c-4f832e89cba0c01f) · [参数 P-5609756e685a9970](../../evidence/parameters-sets-007.md#p-5609756e685a9970)

### path-071859

```text
(config-subif)# llp nhrp map multicast dynamic <cr>
```

Handler ` RVA 0x108D5D50 `；selector ` 1 `；EOL ` RVA 0x34BF34C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-642b1486f94b3da5](../../evidence/conditions-sets-039.md#c-642b1486f94b3da5) · [状态效果 S-0243b41502491c91](../../evidence/state_effects-sets-001.md#s-0243b41502491c91)

### path-069892

```text
(config-subif)# lnm alternate <number:0..3> <cr>
```

Handler ` RVA 0x12339790 `；selector ` 0 `；EOL ` RVA 0x35814C38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of lan managers。

[条件 C-7e397adffee62ded](../../evidence/conditions-sets-049.md#c-7e397adffee62ded) · [参数 P-7c7a4803f44bd5af](../../evidence/parameters-sets-010.md#p-7c7a4803f44bd5af)

### path-068731

```text
(config-subif)# lnm crs <cr>
```

Handler ` RVA 0x12339790 `；selector ` 1 `；EOL ` RVA 0x35814F28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e06f5e6114ae1905](../../evidence/conditions-sets-086.md#c-e06f5e6114ae1905)

### path-068761

```text
(config-subif)# lnm express-buffer <cr>
```

Handler ` RVA 0x12339790 `；selector ` 12 `；EOL ` RVA 0x35815BF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e06f5e6114ae1905](../../evidence/conditions-sets-086.md#c-e06f5e6114ae1905)

### path-069923

```text
(config-subif)# lnm loss-threshold <number:0..999> <cr>
```

Handler ` RVA 0x12339790 `；selector ` 2 `；EOL ` RVA 0x35815268 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Threshold。

[条件 C-0da86379ef36b702](../../evidence/conditions-sets-006.md#c-0da86379ef36b702) · [参数 P-623861246bd0b0ee](../../evidence/parameters-sets-008.md#p-623861246bd0b0ee)

### path-071231

```text
(config-subif)# lnm password <number:0..3> <string> <cr>
```

Handler ` RVA 0x12339790 `；selector ` 4 `；EOL ` RVA 0x358155E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Link to which this password applies；` string ` Password (maximum 8 characters)。

[条件 C-5062c8f5f9475e9d](../../evidence/conditions-sets-031.md#c-5062c8f5f9475e9d) · [参数 P-0bdeeb9a8d0de0e9](../../evidence/parameters-sets-001.md#p-0bdeeb9a8d0de0e9)

### path-068754

```text
(config-subif)# lnm rem <cr>
```

Handler ` RVA 0x12339790 `；selector ` 5 `；EOL ` RVA 0x35815910 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e06f5e6114ae1905](../../evidence/conditions-sets-086.md#c-e06f5e6114ae1905)

### path-068794

```text
(config-subif)# lnm ring-number-mismatch-allowed <cr>
```

Handler ` RVA 0x12339790 `；selector ` 14 `；EOL ` RVA 0x35816588 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e06f5e6114ae1905](../../evidence/conditions-sets-086.md#c-e06f5e6114ae1905)

### path-068782

```text
(config-subif)# lnm rps <cr>
```

Handler ` RVA 0x12339790 `；selector ` 7 `；EOL ` RVA 0x35815F30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e06f5e6114ae1905](../../evidence/conditions-sets-086.md#c-e06f5e6114ae1905)

### path-070001

```text
(config-subif)# lnm softerr <number:0..4294967295> <cr>
```

Handler ` RVA 0x12339790 `；selector ` 9 `；EOL ` RVA 0x358162C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Frequency of error reports in tens of milliseconds。

[条件 C-19b810d77a31cb42](../../evidence/conditions-sets-010.md#c-19b810d77a31cb42) · [参数 P-180a6e4cf55e2b7e](../../evidence/parameters-sets-002.md#p-180a6e4cf55e2b7e)

### path-072529

```text
(config-subif)# load-balance-hash-algo <?keyword_option_mm_action@5555898c4350> <cr>
```

Handler ` RVA 0xE9A2170 `；selector ` 0 `；EOL ` RVA 0x34370378 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f5bac9215ec35a89](../../evidence/conditions-sets-095.md#c-f5bac9215ec35a89) · [缺口 G-13e17ddb7ff8e728](../../evidence/gaps-sets-001.md#g-13e17ddb7ff8e728)

### path-068325

```text
(config-subif)# load-balancing vlan <cr>
```

Handler ` RVA 0xE9A2C20 `；selector ` 0 `；EOL ` RVA 0x343707A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-416f068fb8cb0fd8](../../evidence/conditions-sets-026.md#c-416f068fb8cb0fd8) · [状态效果 S-33279cc2d6596a86](../../evidence/state_effects-sets-011.md#s-33279cc2d6596a86)

### path-068045

```text
(config-subif)# load-interval <number:30..600> <cr>
```

Handler ` RVA 0xE40DC60 `；selector ` 4 `；EOL ` RVA 0x3413B480 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Load interval delay in seconds。

[条件 C-bb5adb8e146213fb](../../evidence/conditions-sets-072.md#c-bb5adb8e146213fb) · [参数 P-5ad00e97835e4613](../../evidence/parameters-sets-007.md#p-5ad00e97835e4613)

### path-068048

```text
(config-subif)# locaddr-priority <number:1..10> <cr>
```

Handler ` RVA 0x1E53C520 `；selector ` 0 `；EOL ` RVA 0x35517630 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Priority list number。

[条件 C-03355a686139e9a7](../../evidence/conditions-sets-002.md#c-03355a686139e9a7) · [参数 P-9ff65f560284c6c6](../../evidence/parameters-sets-012.md#p-9ff65f560284c6c6)

### path-068877

```text
(config-subif)# location additional-location-information <string> <cr>
```

Handler ` RVA 0xC912650 `；selector ` 22 `；EOL ` RVA 0x33B1CFC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Additional location information。

[条件 C-77e1a6617579b2f7](../../evidence/conditions-sets-047.md#c-77e1a6617579b2f7) · [参数 P-8d9790a50d8a6480](../../evidence/parameters-sets-011.md#p-8d9790a50d8a6480)

### path-068875

```text
(config-subif)# location civic-location-id none <cr>
```

Handler ` RVA 0xC912B30 `；selector ` 0 `；EOL ` RVA 0x33B1C710 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f0789f62609cfd9b](../../evidence/conditions-sets-093.md#c-f0789f62609cfd9b) · [状态效果 S-4ac189e6e1f31de1](../../evidence/state_effects-sets-016.md#s-4ac189e6e1f31de1)

### path-068880

```text
(config-subif)# location custom-location-id none <cr>
```

Handler ` RVA 0xC912B30 `；selector ` 10 `；EOL ` RVA 0x33B1D3A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5c72c7a1ae4c595d](../../evidence/conditions-sets-036.md#c-5c72c7a1ae4c595d) · [状态效果 S-bf943180f0e93830](../../evidence/state_effects-sets-041.md#s-bf943180f0e93830)

### path-068873

```text
(config-subif)# location elin-location-id <string> <cr>
```

Handler ` RVA 0xC912B30 `；selector ` 101 `；EOL ` RVA 0x33B1CC78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` ELIN identifier string。

[条件 C-940db11846d7a0c2](../../evidence/conditions-sets-057.md#c-940db11846d7a0c2) · [参数 P-cd1ca29bb18c7d05](../../evidence/parameters-sets-016.md#p-cd1ca29bb18c7d05)

### path-068881

```text
(config-subif)# location geo-location-id none <cr>
```

Handler ` RVA 0xC912B30 `；selector ` 102 `；EOL ` RVA 0x33B1D960 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8a17cc6121f693b4](../../evidence/conditions-sets-053.md#c-8a17cc6121f693b4) · [状态效果 S-910682e00e02079a](../../evidence/state_effects-sets-031.md#s-910682e00e02079a)

### path-068970

```text
(config-subif)# logging event dlci-status-change <cr>
```

Handler ` RVA 0xF5FA570 `；selector ` 0 `；EOL ` RVA 0x346FF940 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-75cadc4ae2122393](../../evidence/conditions-sets-046.md#c-75cadc4ae2122393) · [状态效果 S-4917347c9df5f031](../../evidence/state_effects-sets-016.md#s-4917347c9df5f031)

### path-070322

```text
(config-subif)# logging event frame-relay dlci <cr>
```

Handler ` RVA 0xF5FA740 `；selector ` 135 `；EOL ` RVA 0x34700530 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0a431245bd2c000a](../../evidence/conditions-sets-004.md#c-0a431245bd2c000a) · [状态效果 S-234e70926502b609](../../evidence/state_effects-sets-008.md#s-234e70926502b609)

### path-068905

```text
(config-subif)# logging event link-status <cr>
```

Handler ` RVA 0xE446800 `；selector ` 0 `；EOL ` RVA 0x34146DC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6ad77a14a7899610](../../evidence/conditions-sets-041.md#c-6ad77a14a7899610) · [状态效果 S-f095b54b5d909953](../../evidence/state_effects-sets-051.md#s-f095b54b5d909953)

### path-068912

```text
(config-subif)# logging event link-status <cr>
```

Handler ` RVA 0xE4474D0 `；selector ` 0 `；EOL ` RVA 0x34146AE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-22c502a179dc6a76](../../evidence/conditions-sets-014.md#c-22c502a179dc6a76) · [状态效果 S-52db435293ab80b4](../../evidence/state_effects-sets-018.md#s-52db435293ab80b4)

### path-068062

```text
(config-subif)# loopback <cr>
```

Handler ` RVA 0xE408FE0 `；selector ` 0 `；EOL ` RVA 0x3413DE30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-770592df5d9cc9e8](../../evidence/conditions-sets-046.md#c-770592df5d9cc9e8) · [状态效果 S-6e377147c000b0e4](../../evidence/state_effects-sets-023.md#s-6e377147c000b0e4)

### path-068254

```text
(config-subif)# loopback dte <cr>
```

Handler ` RVA 0xDFFAE70 `；selector ` 2 `；EOL ` RVA 0x3413CCA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-677186f0e9943852](../../evidence/conditions-sets-040.md#c-677186f0e9943852) · [状态效果 S-59b117bc2074a0fe](../../evidence/state_effects-sets-019.md#s-59b117bc2074a0fe)

### path-068351

```text
(config-subif)# loopback dte <cr>
```

Handler ` RVA 0xED6F530 `；selector ` 10 `；EOL ` RVA 0x3440FAD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7eac62e7936df663](../../evidence/conditions-sets-049.md#c-7eac62e7936df663) · [状态效果 S-d67d0db559c4bbcc](../../evidence/state_effects-sets-045.md#s-d67d0db559c4bbcc)

### path-068259

```text
(config-subif)# loopback line <cr>
```

Handler ` RVA 0xDFFAE70 `；selector ` 3 `；EOL ` RVA 0x3413D028 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ccbb3218235e5d64](../../evidence/conditions-sets-079.md#c-ccbb3218235e5d64) · [状态效果 S-f10198909744cd10](../../evidence/state_effects-sets-051.md#s-f10198909744cd10)

### path-068239

```text
(config-subif)# loopback remote <cr>
```

Handler ` RVA 0xDFFAD90 `；selector ` 5 `；EOL ` RVA 0x3413C7B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0b8b8de38015607b](../../evidence/conditions-sets-005.md#c-0b8b8de38015607b) · [状态效果 S-72636cc0f5f9fe3e](../../evidence/state_effects-sets-024.md#s-72636cc0f5f9fe3e)

### path-068272

```text
(config-subif)# loopback remote <cr>
```

Handler ` RVA 0xDFFAE70 `；selector ` 4 `；EOL ` RVA 0x3413D3F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-dad18d4fc7cd36c8](../../evidence/conditions-sets-084.md#c-dad18d4fc7cd36c8) · [状态效果 S-9f57bdfbe772e07a](../../evidence/state_effects-sets-034.md#s-9f57bdfbe772e07a)

### path-072649

```text
(config-subif)# loopback remote full user-pattern <string> <cr>
```

Handler ` RVA 0xDFFAE70 `；selector ` 4 `；EOL ` RVA 0x3413D3F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` User define binary pattern (up to 24 bits)。

[条件 C-426377ecd1a2fa3e](../../evidence/conditions-sets-026.md#c-426377ecd1a2fa3e) · [缺口 G-6ba388b22b3e6bb5](../../evidence/gaps-sets-004.md#g-6ba388b22b3e6bb5) · [参数 P-e5ff065eca50f753](../../evidence/parameters-sets-017.md#p-e5ff065eca50f753) · [状态效果 S-fb8614ece32d26cf](../../evidence/state_effects-sets-053.md#s-fb8614ece32d26cf)

### path-068138

```text
(config-subif)# mab <cr>
```

Handler ` RVA 0xCB56940 `；selector ` 0 `；EOL ` RVA 0x33BEA530 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d004e91cb2bc84e9](../../evidence/conditions-sets-080.md#c-d004e91cb2bc84e9)

### path-068602

```text
(config-subif)# mab eap <cr>
```

Handler ` RVA 0xCB56940 `；selector ` 1 `；EOL ` RVA 0x33BEA508 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d004e91cb2bc84e9](../../evidence/conditions-sets-080.md#c-d004e91cb2bc84e9)

### path-068218

```text
(config-subif)# mac-address <address> <cr>
```

Handler ` RVA 0xE40DD50 `；selector ` 0 `；EOL ` RVA 0x3412EB10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` MAC address。

[条件 C-f3e01b618c79ee66](../../evidence/conditions-sets-094.md#c-f3e01b618c79ee66) · [参数 P-a49457ba3e9a8473](../../evidence/parameters-sets-013.md#p-a49457ba3e9a8473)

### path-068073

```text
(config-subif)# macsec <cr>
```

Handler ` RVA 0x16100410 `；selector ` 1 `；EOL ` RVA 0x35ED50E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-17a03be7ab9eb569](../../evidence/conditions-sets-009.md#c-17a03be7ab9eb569)

### path-069279

```text
(config-subif)# macsec access-control should-secure <cr>
```

Handler ` RVA 0x16100410 `；selector ` 3 `；EOL ` RVA 0x35ED4DA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ebaee1406b2066f7](../../evidence/conditions-sets-091.md#c-ebaee1406b2066f7) · [状态效果 S-10d0bd97b2275543](../../evidence/state_effects-sets-004.md#s-10d0bd97b2275543)

### path-068373

```text
(config-subif)# macsec disable-sci <cr>
```

Handler ` RVA 0x16100410 `；selector ` 5 `；EOL ` RVA 0x35ED4A58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-deb9d8c7770ebf88](../../evidence/conditions-sets-086.md#c-deb9d8c7770ebf88)

### path-068410

```text
(config-subif)# macsec dot1q-in-clear <cr>
```

Handler ` RVA 0x16100410 `；selector ` 2 `；EOL ` RVA 0x35ED46B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08a64efb7ac2de0c](../../evidence/conditions-sets-004.md#c-08a64efb7ac2de0c)

### path-070582

```text
(config-subif)# macsec replay-protection window-size <number:0..4294967295> <cr>
```

Handler ` RVA 0x16100410 `；selector ` 4 `；EOL ` RVA 0x35ED51C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Window size 0 - 4294967295。

[条件 C-3682927063fce3aa](../../evidence/conditions-sets-021.md#c-3682927063fce3aa) · [参数 P-ca57e7526ddc4c56](../../evidence/parameters-sets-015.md#p-ca57e7526ddc4c56)

### path-068306

```text
(config-subif)# map-group <string> <cr>
```

Handler ` RVA 0xDD008F0 `；selector ` 0 `；EOL ` RVA 0x3403E018 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Static map group name。

[条件 C-bffb24482370b3ae](../../evidence/conditions-sets-074.md#c-bffb24482370b3ae) · [参数 P-00ac0ea018edf978](../../evidence/parameters-sets-001.md#p-00ac0ea018edf978)

### path-068491

```text
(config-subif)# mdns-sd gateway <cr>
```

Handler ` RVA 0x143514D0 `；selector ` 0 `；EOL ` RVA 0x35D30B88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-62b445caa8c401b1](../../evidence/conditions-sets-038.md#c-62b445caa8c401b1)

### path-068066

```text
(config-subif)# media-type <cr>
```

Handler ` RVA 0xE40CBB0 `；selector ` 0 `；EOL ` RVA 0x34142790 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a8b2c605362c888c](../../evidence/conditions-sets-065.md#c-a8b2c605362c888c)

### path-068310

```text
(config-subif)# medium p2p <cr>
```

Handler ` RVA 0xED13DD0 `；selector ` 0 `；EOL ` RVA 0x34404B38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-94a579f792a7392d](../../evidence/conditions-sets-057.md#c-94a579f792a7392d)

### path-072695

```text
(config-subif)# member <?ttyline_action@555589e87378> async default ip address <cr>
```

Handler ` RVA 0xFF48960 `；selector ` 9 `；EOL ` RVA 0x34933888 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8bdbfa51c2d65e95](../../evidence/conditions-sets-054.md#c-8bdbfa51c2d65e95) · [缺口 G-ad5b874beb7500a8](../../evidence/gaps-sets-006.md#g-ad5b874beb7500a8)

### path-072573

```text
(config-subif)# member <?ttyline_action@555589e87378> description <cr>
```

Handler ` RVA 0xFF48960 `；selector ` 8 `；EOL ` RVA 0x349334B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-528788028ab546a6](../../evidence/conditions-sets-032.md#c-528788028ab546a6) · [缺口 G-ad5b874beb7500a8](../../evidence/gaps-sets-006.md#g-ad5b874beb7500a8)

### path-068846

```text
(config-subif)# mka default-policy <cr>
```

Handler ` RVA 0x16074660 `；selector ` 2 `；EOL ` RVA 0x35EBCC98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-728f2bf9a2dcca7d](../../evidence/conditions-sets-044.md#c-728f2bf9a2dcca7d)

### path-070105

```text
(config-subif)# mka policy <string> <cr>
```

Handler ` RVA 0x160765E0 `；selector ` 1 `；EOL ` RVA 0x35EBC350 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` MKA Policy NAME。

[条件 C-4e94889e43acf3ce](../../evidence/conditions-sets-031.md#c-4e94889e43acf3ce) · [参数 P-dba71629563c593a](../../evidence/parameters-sets-017.md#p-dba71629563c593a)

### path-071433

```text
(config-subif)# mka pre-shared-key key-chain <string> <cr>
```

Handler ` RVA 0x16074660 `；selector ` 3 `；EOL ` RVA 0x35EBC758 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of key-chain to be used to get keys。

[条件 C-21a8d7e91df3ac4c](../../evidence/conditions-sets-013.md#c-21a8d7e91df3ac4c) · [参数 P-8d76c671ac7043b7](../../evidence/parameters-sets-011.md#p-8d76c671ac7043b7)

### path-072357

```text
(config-subif)# mka pre-shared-key key-chain <string> fallback-key-chain <string> <cr>
```

Handler ` RVA 0x16074660 `；selector ` 4 `；EOL ` RVA 0x35EBC798 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of key-chain to be used to get keys；` string ` Name of fallback key-chain to be used to get keys。

[条件 C-21a8d7e91df3ac4c](../../evidence/conditions-sets-013.md#c-21a8d7e91df3ac4c) · [参数 P-2584aede8f7ab154](../../evidence/parameters-sets-003.md#p-2584aede8f7ab154)

### path-068657

```text
(config-subif)# mlacp interchassis group <number:1..4294967295> <cr>
```

Handler ` RVA 0xC960F90 `；selector ` 0 `；EOL ` RVA 0x33B32308 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Group ID。

[条件 C-75d0179d996ddd34](../../evidence/conditions-sets-046.md#c-75d0179d996ddd34) · [参数 P-b29facd19c31a1c9](../../evidence/parameters-sets-014.md#p-b29facd19c31a1c9)

### path-068146

```text
(config-subif)# mlacp lag-priority <number:0..65535> <cr>
```

Handler ` RVA 0xC960F90 `；selector ` 1 `；EOL ` RVA 0x33B32028 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Priority value。

[条件 C-c612690396596d23](../../evidence/conditions-sets-076.md#c-c612690396596d23) · [参数 P-35a28237e4cd2c19](../../evidence/parameters-sets-005.md#p-35a28237e4cd2c19)

### path-072630

```text
(config-subif)# mlacp load-balance primary vlan <cr>
```

Handler ` RVA 0xC960F90 `；selector ` 3 `；EOL ` RVA 0x33B33028 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0c8fc21d34d71081](../../evidence/conditions-sets-005.md#c-0c8fc21d34d71081) · [缺口 G-77dacb8a060bcfbb](../../evidence/gaps-sets-005.md#g-77dacb8a060bcfbb) · [状态效果 S-06efce23a56d75a5](../../evidence/state_effects-sets-002.md#s-06efce23a56d75a5)

### path-069819

```text
(config-subif)# mlacp mac mstp-tcn <cr>
```

Handler ` RVA 0xC960F90 `；selector ` 4 `；EOL ` RVA 0x33B329E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-df3fc9d6e1846d97](../../evidence/conditions-sets-086.md#c-df3fc9d6e1846d97) · [状态效果 S-3da8b35bc79a082b](../../evidence/state_effects-sets-014.md#s-3da8b35bc79a082b)

### path-069767

```text
(config-subif)# mlacp mode active-active <cr>
```

Handler ` RVA 0xC960F90 `；selector ` 2 `；EOL ` RVA 0x33B326A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-157d029f6a7ef801](../../evidence/conditions-sets-008.md#c-157d029f6a7ef801) · [状态效果 S-e7700e4655d38801](../../evidence/state_effects-sets-049.md#s-e7700e4655d38801)

### path-068217

```text
(config-subif)# mtu 1500 <cr>
```

Handler ` RVA 0xE425A60 `；selector ` 0 `；EOL ` RVA 0x3412F000 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0a63ccdcae359609](../../evidence/conditions-sets-004.md#c-0a63ccdcae359609) · [状态效果 S-6d7d39b29168effd](../../evidence/state_effects-sets-023.md#s-6d7d39b29168effd)

### path-072524

```text
(config-subif)# mtu <number:dynamic> <cr>
```

Handler ` RVA 0xE425A60 `；selector ` 0 `；EOL ` RVA 0x3412F000 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` MTU size in bytes。

[条件 C-3043c44bca4d0cb5](../../evidence/conditions-sets-019.md#c-3043c44bca4d0cb5) · [缺口 G-8c0a532e697b28cd](../../evidence/gaps-sets-005.md#g-8c0a532e697b28cd) · [参数 P-bf03454a5cd836cb](../../evidence/parameters-sets-014.md#p-bf03454a5cd836cb)

### path-069631

```text
(config-subif)# multilink load-threshold <number:1..255> <cr>
```

Handler ` RVA 0xFF5C450 `；selector ` 88 `；EOL ` RVA 0x349371C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9bf7f0b717d3983b](../../evidence/conditions-sets-060.md#c-9bf7f0b717d3983b) · [参数 P-9db84a1bd7597ee4](../../evidence/parameters-sets-012.md#p-9db84a1bd7597ee4)

### path-069570

```text
(config-subif)# multilink max-fragments 1 <cr>
```

Handler ` RVA 0xFF5C450 `；selector ` 94 `；EOL ` RVA 0x349375C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e6f50629d29e984a](../../evidence/conditions-sets-089.md#c-e6f50629d29e984a) · [状态效果 S-858e5d389f70a082](../../evidence/state_effects-sets-028.md#s-858e5d389f70a082)

### path-069466

```text
(config-subif)# multilink max-links <number:256..2147483646> <cr>
```

Handler ` RVA 0xFF5C450 `；selector ` 90 `；EOL ` RVA 0x34936A70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-adf453a8502e9825](../../evidence/conditions-sets-067.md#c-adf453a8502e9825) · [参数 P-29f660ce2ce45d78](../../evidence/parameters-sets-004.md#p-29f660ce2ce45d78)

### path-069506

```text
(config-subif)# multilink min-links <number:256..2147483647> <cr>
```

Handler ` RVA 0xFF5C450 `；selector ` 89 `；EOL ` RVA 0x34936E18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-adf453a8502e9825](../../evidence/conditions-sets-067.md#c-adf453a8502e9825) · [参数 P-100f8bf04c519a1d](../../evidence/parameters-sets-002.md#p-100f8bf04c519a1d)

### path-068530

```text
(config-subif)# multilink-group <number:1..2147483647> <cr>
```

Handler ` RVA 0xFF5C450 `；selector ` 99 `；EOL ` RVA 0x349379B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fbd69b0412a3fdcf](../../evidence/conditions-sets-097.md#c-fbd69b0412a3fdcf) · [参数 P-1d8277dd4269e8e5](../../evidence/parameters-sets-003.md#p-1d8277dd4269e8e5)

### path-068392

```text
(config-subif)# multiring all <cr>
```

Handler ` RVA 0x12404E50 `；selector ` 0 `；EOL ` RVA 0x35853198 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-186a07ad430e8f55](../../evidence/conditions-sets-009.md#c-186a07ad430e8f55) · [状态效果 S-801712c6f8e89ec8](../../evidence/state_effects-sets-027.md#s-801712c6f8e89ec8)

### path-072654

```text
(config-subif)# multiring trcrf-vlan <number:dynamic> ring <number:1..4095> <cr>
```

Handler ` RVA 0x12404E50 `；selector ` 0 `；EOL ` RVA 0x35853198 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` CRF Vlan id；` unsigned_number ` CRF Ring number。

[条件 C-be2d2ecc641a962a](../../evidence/conditions-sets-073.md#c-be2d2ecc641a962a) · [缺口 G-898f0d6cbb1b9377](../../evidence/gaps-sets-005.md#g-898f0d6cbb1b9377) · [参数 P-5faf7be0e75e8ee3](../../evidence/parameters-sets-008.md#p-5faf7be0e75e8ee3) · [状态效果 S-c688017208479645](../../evidence/state_effects-sets-042.md#s-c688017208479645)

### path-068549

```text
(config-subif)# mvr immediate <cr>
```

Handler ` RVA 0xC3B2CF0 `；selector ` 0 `；EOL ` RVA 0x33A622E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-05fdc74b4ea7e682](../../evidence/conditions-sets-003.md#c-05fdc74b4ea7e682)

### path-069514

```text
(config-subif)# mvr type receiver <cr>
```

Handler ` RVA 0xC3B3310 `；selector ` 0 `；EOL ` RVA 0x33A61B60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-11557d1f33aea319](../../evidence/conditions-sets-007.md#c-11557d1f33aea319) · [状态效果 S-71e2e8c895ef8cdd](../../evidence/state_effects-sets-024.md#s-71e2e8c895ef8cdd)

### path-072620

```text
(config-subif)# mvr vlan <number:dynamic> group <cr>
```

Handler ` RVA 0xC3B35B0 `；selector ` 0 `；EOL ` RVA 0x33A61FE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` The VLAN id。

[条件 C-b6211d595b554df9](../../evidence/conditions-sets-070.md#c-b6211d595b554df9) · [缺口 G-5bbff123b79aceb3](../../evidence/gaps-sets-004.md#g-5bbff123b79aceb3) · [参数 P-c0707d21fd9087f1](../../evidence/parameters-sets-015.md#p-c0707d21fd9087f1) · [状态效果 S-f87525fb1974b42f](../../evidence/state_effects-sets-053.md#s-f87525fb1974b42f)

### path-068360

```text
(config-subif)# nat64 enable <cr>
```

Handler ` RVA 0xD59D3E0 `；selector ` 0 `；EOL ` RVA 0x33E93758 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-81ec7286c401d215](../../evidence/conditions-sets-050.md#c-81ec7286c401d215)

### path-072612

```text
(config-subif)# nat64 prefix stateful <prefix:dynamic> <cr>
```

Handler ` RVA 0xD59D3E0 `；selector ` 1 `；EOL ` RVA 0x33E93BF0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` IPv6 prefix。

[条件 C-e8db75ad30ec369d](../../evidence/conditions-sets-090.md#c-e8db75ad30ec369d) · [缺口 G-b06147beeee7e3ce](../../evidence/gaps-sets-006.md#g-b06147beeee7e3ce) · [参数 P-7fb29f0298f07825](../../evidence/parameters-sets-010.md#p-7fb29f0298f07825) · [状态效果 S-c7f2a44c86dc7db4](../../evidence/state_effects-sets-042.md#s-c7f2a44c86dc7db4)

### path-072658

```text
(config-subif)# nat64 settings mtu minimum <number:dynamic> <cr>
```

Handler ` RVA 0xD59D3E0 `；selector ` 2 `；EOL ` RVA 0x33E940E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Minimum MTU (bytes)。

[条件 C-6894253292ff6e48](../../evidence/conditions-sets-040.md#c-6894253292ff6e48) · [缺口 G-cc039a901e1bf0e7](../../evidence/gaps-sets-007.md#g-cc039a901e1bf0e7) · [参数 P-92c9f3f7a70f342b](../../evidence/parameters-sets-011.md#p-92c9f3f7a70f342b)

### path-068371

```text
(config-subif)# nat66 inside <cr>
```

Handler ` RVA 0xD60E8B0 `；selector ` 0 `；EOL ` RVA 0x33EAD9D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5791ab7ea4e60a1c](../../evidence/conditions-sets-034.md#c-5791ab7ea4e60a1c)

### path-068384

```text
(config-subif)# nat66 outside <cr>
```

Handler ` RVA 0xD60E8B0 `；selector ` 1 `；EOL ` RVA 0x33EADC78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5791ab7ea4e60a1c](../../evidence/conditions-sets-034.md#c-5791ab7ea4e60a1c)

### path-069242

```text
(config-subif)# national bit <number:0..1> <cr>
```

Handler ` RVA 0xED6F530 `；selector ` 4 `；EOL ` RVA 0x34410E60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Value of national bit.。

[条件 C-89e0e1d65a3a243e](../../evidence/conditions-sets-053.md#c-89e0e1d65a3a243e) · [参数 P-67c988d3ef5d686b](../../evidence/parameters-sets-008.md#p-67c988d3ef5d686b)

### path-068304

```text
(config-subif)# negotiation auto <cr>
```

Handler ` RVA 0xE40CC50 `；selector ` 4 `；EOL ` RVA 0x34135E08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5180c32052896e3d](../../evidence/conditions-sets-032.md#c-5180c32052896e3d) · [状态效果 S-634679006d9d91be](../../evidence/state_effects-sets-021.md#s-634679006d9d91be)

### path-068361

```text
(config-subif)# netbios enable-name-cache <cr>
```

Handler ` RVA 0x114B4BD0 `；selector ` 5 `；EOL ` RVA 0x354F6B68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-80379a6379ec81fe](../../evidence/conditions-sets-050.md#c-80379a6379ec81fe)

### path-070542

```text
(config-subif)# netbios input-access-filter host <string> <cr>
```

Handler ` RVA 0xFDF4680 `；selector ` 0 `；EOL ` RVA 0x348E39D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of previously defined access list filter。

[条件 C-80379a6379ec81fe](../../evidence/conditions-sets-050.md#c-80379a6379ec81fe) · [参数 P-034361a38257713e](../../evidence/parameters-sets-001.md#p-034361a38257713e) · [状态效果 S-d60ceaa1c3cc99d9](../../evidence/state_effects-sets-045.md#s-d60ceaa1c3cc99d9)

### path-072766

```text
(config-subif)# nhrp attribute group <cr>
```

Handler ` RVA 0xFAB45E0 `；selector ` 35 `；EOL ` RVA 0x34BEEBA0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0fef421443b4b2bd](../../evidence/conditions-sets-006.md#c-0fef421443b4b2bd) · [缺口 G-da63c01e9e903355](../../evidence/gaps-sets-008.md#g-da63c01e9e903355) · [状态效果 S-911d8e7a22d1bf2f](../../evidence/state_effects-sets-031.md#s-911d8e7a22d1bf2f)

### path-072729

```text
(config-subif)# nhrp event-publisher max-event-timeout <number:1..22> <cr>
```

Handler ` RVA 0x108BE5A0 `；selector ` 1 `；EOL ` RVA 0x34BEE450 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Number of seconds。

[条件 C-e773e8cfc5ff6215](../../evidence/conditions-sets-089.md#c-e773e8cfc5ff6215) · [缺口 G-8be50bbdfb36f5ed](../../evidence/gaps-sets-005.md#g-8be50bbdfb36f5ed) · [参数 P-281d1c66228e7320](../../evidence/parameters-sets-003.md#p-281d1c66228e7320) · [状态效果 S-f4c7bb2446caf6e5](../../evidence/state_effects-sets-052.md#s-f4c7bb2446caf6e5)

### path-072731

```text
(config-subif)# nhrp group <cr>
```

Handler ` RVA 0x108850F0 `；selector ` 20 `；EOL ` RVA 0x34BEE808 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c8b2b97d085493e6](../../evidence/conditions-sets-077.md#c-c8b2b97d085493e6) · [缺口 G-da63c01e9e903355](../../evidence/gaps-sets-008.md#g-da63c01e9e903355) · [状态效果 S-f4c7bb2446caf6e5](../../evidence/state_effects-sets-052.md#s-f4c7bb2446caf6e5)

### path-072801

```text
(config-subif)# nhrp map group <string> <cr>
```

Handler ` RVA 0x108850F0 `；selector ` 32 `；EOL ` RVA 0x34BEEF50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` NHRP group name。

[条件 C-629fc87fd3e88595](../../evidence/conditions-sets-038.md#c-629fc87fd3e88595) · [缺口 G-da63c01e9e903355](../../evidence/gaps-sets-008.md#g-da63c01e9e903355) · [参数 P-271d45dca301b6d6](../../evidence/parameters-sets-003.md#p-271d45dca301b6d6) · [状态效果 S-f4c7bb2446caf6e5](../../evidence/state_effects-sets-052.md#s-f4c7bb2446caf6e5)

### path-072730

```text
(config-subif)# nhrp route-watch <cr>
```

Handler ` RVA 0x108FB1C0 `；selector ` 33 `；EOL ` RVA 0x34BF9B20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9b8ac1be7ce1ee99](../../evidence/conditions-sets-060.md#c-9b8ac1be7ce1ee99) · [缺口 G-da63c01e9e903355](../../evidence/gaps-sets-008.md#g-da63c01e9e903355) · [状态效果 S-f4c7bb2446caf6e5](../../evidence/state_effects-sets-052.md#s-f4c7bb2446caf6e5)

### path-070391

```text
(config-subif)# no aaa connect-info <string> <cr>
```

Handler ` RVA 0xE075DC0 `；selector ` 72 `；EOL ` RVA 0x3419C2B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` connect-info。

[条件 C-05fdc74b4ea7e682](../../evidence/conditions-sets-003.md#c-05fdc74b4ea7e682) · [参数 P-23ea33b390829d45](../../evidence/parameters-sets-003.md#p-23ea33b390829d45) · [状态效果 S-a763f0b283e40fef](../../evidence/state_effects-sets-035.md#s-a763f0b283e40fef)

### path-069579

```text
(config-subif)# no access-expression input <cr>
```

Handler ` RVA 0x1E3FC780 `；selector ` 0 `；EOL ` RVA 0x345EC7A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-2328464fd2f49f8a](../../evidence/conditions-sets-014.md#c-2328464fd2f49f8a) · [状态效果 S-ed0a591e6a6d6b08](../../evidence/state_effects-sets-050.md#s-ed0a591e6a6d6b08)

### path-069707

```text
(config-subif)# no access-session closed <cr>
```

Handler ` RVA 0xCAECB20 `；selector ` 2 `；EOL ` RVA 0x33BA55D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d7b70ab64f158610](../../evidence/conditions-sets-083.md#c-d7b70ab64f158610) · [状态效果 S-a763f0b283e40fef](../../evidence/state_effects-sets-035.md#s-a763f0b283e40fef)

### path-069805

```text
(config-subif)# no access-session control-direction <cr>
```

Handler ` RVA 0xCAECB20 `；selector ` 4 `；EOL ` RVA 0x33BA5CF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-01961dd46c761915](../../evidence/conditions-sets-001.md#c-01961dd46c761915) · [状态效果 S-a763f0b283e40fef](../../evidence/state_effects-sets-035.md#s-a763f0b283e40fef)

### path-069684

```text
(config-subif)# no access-session host-mode <cr>
```

Handler ` RVA 0xCAECB20 `；selector ` 1 `；EOL ` RVA 0x33BA4CB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f7aaa63346e784c0](../../evidence/conditions-sets-096.md#c-f7aaa63346e784c0) · [状态效果 S-a763f0b283e40fef](../../evidence/state_effects-sets-035.md#s-a763f0b283e40fef)

### path-071801

```text
(config-subif)# no access-session inherit disable service-policy <cr>
```

Handler ` RVA 0xCAECB20 `；selector ` 7 `；EOL ` RVA 0x33BA6680 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-366c2145c1d195d1](../../evidence/conditions-sets-021.md#c-366c2145c1d195d1) · [状态效果 S-127629e53554c646](../../evidence/state_effects-sets-004.md#s-127629e53554c646)

### path-071140

```text
(config-subif)# no access-session interface-template sticky <cr>
```

Handler ` RVA 0xCAECB20 `；selector ` 6 `；EOL ` RVA 0x33BA60D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d7b70ab64f158610](../../evidence/conditions-sets-083.md#c-d7b70ab64f158610) · [状态效果 S-491829dcf243d0dc](../../evidence/state_effects-sets-016.md#s-491829dcf243d0dc)

### path-069715

```text
(config-subif)# no access-session limit <cr>
```

Handler ` RVA 0xCAECB20 `；selector ` 9 `；EOL ` RVA 0x33BA5258 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad62fd45bc14756e](../../evidence/conditions-sets-067.md#c-ad62fd45bc14756e) · [状态效果 S-a763f0b283e40fef](../../evidence/state_effects-sets-035.md#s-a763f0b283e40fef)

### path-069620

```text
(config-subif)# no access-session monitor <cr>
```

Handler ` RVA 0xCAECB20 `；selector ` 10 `；EOL ` RVA 0x33BA4940 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1f8877db32c126ab](../../evidence/conditions-sets-012.md#c-1f8877db32c126ab) · [状态效果 S-a763f0b283e40fef](../../evidence/state_effects-sets-035.md#s-a763f0b283e40fef)

### path-069776

```text
(config-subif)# no access-session port-control <cr>
```

Handler ` RVA 0xCAECB20 `；selector ` 3 `；EOL ` RVA 0x33BA5910 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d32d8b213d47b30d](../../evidence/conditions-sets-081.md#c-d32d8b213d47b30d) · [状态效果 S-a763f0b283e40fef](../../evidence/state_effects-sets-035.md#s-a763f0b283e40fef)

### path-071330

```text
(config-subif)# no alps ascu <number:33..79> <cr>
```

Handler ` RVA 0x11213B30 `；selector ` 8 `；EOL ` RVA 0x354201A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number `  RID value。

[条件 C-0a4668f7a9da7767](../../evidence/conditions-sets-004.md#c-0a4668f7a9da7767) · [参数 P-99e755fa8bd22d3d](../../evidence/parameters-sets-012.md#p-99e755fa8bd22d3d) · [状态效果 S-a763f0b283e40fef](../../evidence/state_effects-sets-035.md#s-a763f0b283e40fef)

### path-071314

```text
(config-subif)# no alps ascu <number:65..126> <cr>
```

Handler ` RVA 0x11213B30 `；selector ` 8 `；EOL ` RVA 0x3541DE58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number `  Interchange address。

[条件 C-e45d57df3a3beb07](../../evidence/conditions-sets-088.md#c-e45d57df3a3beb07) · [参数 P-3f81ae14511241f6](../../evidence/parameters-sets-005.md#p-3f81ae14511241f6) · [状态效果 S-a763f0b283e40fef](../../evidence/state_effects-sets-035.md#s-a763f0b283e40fef)

### path-072479

```text
(config-subif)# no alps host-hld <number:1..65535> host-link <number:1..255> ax25 <cr>
```

Handler ` RVA 0x11213450 `；selector ` 0 `；EOL ` RVA 0x3541D688 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Host HLD Number；` unsigned_number ` Host-link identifier number。

[条件 C-d1fccaa4aac6a927](../../evidence/conditions-sets-081.md#c-d1fccaa4aac6a927) · [参数 P-05eb6bb78df80933](../../evidence/parameters-sets-001.md#p-05eb6bb78df80933) · [状态效果 S-61ec1fedf1c13634](../../evidence/state_effects-sets-021.md#s-61ec1fedf1c13634)
