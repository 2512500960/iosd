# configure · 六个基础模式的历史连接

[模式索引](README.md) · [总索引](../../README.md)

### path-026781

```text
(config)# ip ospf name-lookup <cr>
```

Handler ` RVA 0xFC67B00 `；selector ` 0 `；EOL ` RVA 0x34881C98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-035672

```text
(config)# ip pim accept-register list <number:100..199> <cr>
```

Handler ` RVA 0xF810790 `；selector ` 26 `；EOL ` RVA 0x3475EA80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Access list number。

[条件 C-3874a03547b8b6be](../../evidence/conditions-sets-022.md#c-3874a03547b8b6be) · [参数 P-1092695a2a0c422a](../../evidence/parameters-sets-002.md#p-1092695a2a0c422a) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029329

```text
(config)# ip pim accept-rp auto-rp <cr>
```

Handler ` RVA 0xF810790 `；selector ` 9 `；EOL ` RVA 0x3475BE50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8afa922b1bb90878](../../evidence/conditions-sets-054.md#c-8afa922b1bb90878) · [状态效果 S-d2e6ed03117a8104](../../evidence/state_effects-sets-045.md#s-d2e6ed03117a8104)

### path-027172

```text
(config)# ip pim allow-rp <cr>
```

Handler ` RVA 0xF810790 `；selector ` 66 `；EOL ` RVA 0x34760580 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5c39d3d602b70da0](../../evidence/conditions-sets-036.md#c-5c39d3d602b70da0) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026770

```text
(config)# ip pim autorp <cr>
```

Handler ` RVA 0xF810790 `；selector ` 62 `；EOL ` RVA 0x34759DB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-63db2e88a69e048f](../../evidence/conditions-sets-039.md#c-63db2e88a69e048f) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-028870

```text
(config)# ip pim autorp listener <cr>
```

Handler ` RVA 0xF810790 `；selector ` 47 `；EOL ` RVA 0x34759D90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-63db2e88a69e048f](../../evidence/conditions-sets-039.md#c-63db2e88a69e048f) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026609

```text
(config)# ip pim bidir-enable <cr>
```

Handler ` RVA 0xF810790 `；selector ` 45 `；EOL ` RVA 0x34757278 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f2e03679db599380](../../evidence/conditions-sets-094.md#c-f2e03679db599380) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-028819

```text
(config)# ip pim bidir-offer-interval <number:3..100> <cr>
```

Handler ` RVA 0xF810790 `；selector ` 30 `；EOL ` RVA 0x34758FA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Limit: no more than 100。

[条件 C-54ff140893cef4c7](../../evidence/conditions-sets-033.md#c-54ff140893cef4c7) · [参数 P-bebabfb13c3d8b94](../../evidence/parameters-sets-014.md#p-bebabfb13c3d8b94) · [状态效果 S-87460ad537b775bf](../../evidence/state_effects-sets-029.md#s-87460ad537b775bf)

### path-060586

```text
(config)# ip pim bsr-candidate <interface> <cr>
```

Handler ` RVA 0xF810790 `；selector ` 19 `；EOL ` RVA 0x3475C270 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-430dc71aabc135de](../../evidence/conditions-sets-026.md#c-430dc71aabc135de) · [缺口 G-be7579ceca805681](../../evidence/gaps-sets-007.md#g-be7579ceca805681) · [参数 P-3146a705c19b5f66](../../evidence/parameters-sets-004.md#p-3146a705c19b5f66) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-028759

```text
(config)# ip pim cache rpf-oif <cr>
```

Handler ` RVA 0xF810790 `；selector ` 88 `；EOL ` RVA 0x347597F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-63db2e88a69e048f](../../evidence/conditions-sets-039.md#c-63db2e88a69e048f) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026719

```text
(config)# ip pim dm-fallback <cr>
```

Handler ` RVA 0xF810790 `；selector ` 53 `；EOL ` RVA 0x34758C20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1c1d4d7eb6586ba0](../../evidence/conditions-sets-011.md#c-1c1d4d7eb6586ba0) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026949

```text
(config)# ip pim fast-register-stop <cr>
```

Handler ` RVA 0xF810790 `；selector ` 16 `；EOL ` RVA 0x3475E018 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6ec824d1abfaf50c](../../evidence/conditions-sets-043.md#c-6ec824d1abfaf50c) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027044

```text
(config)# ip pim log-neighbor-changes <cr>
```

Handler ` RVA 0xF810790 `；selector ` 54 `；EOL ` RVA 0x3475F6A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-21d0519a794d6b68](../../evidence/conditions-sets-013.md#c-21d0519a794d6b68) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-045287

```text
(config)# ip pim maximum group-mappings autorp <number:1..10000> <cr>
```

Handler ` RVA 0xF810790 `；selector ` 63 `；EOL ` RVA 0x3475EF80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Maximum PIM group mappings。

[条件 C-95ad654680b0dcf1](../../evidence/conditions-sets-058.md#c-95ad654680b0dcf1) · [参数 P-367862b01764f3ad](../../evidence/parameters-sets-005.md#p-367862b01764f3ad) · [状态效果 S-47730b5bcd320e21](../../evidence/state_effects-sets-016.md#s-47730b5bcd320e21)

### path-060138

```text
(config)# ip pim mofrr clone join <address> mask-length <number:0..32> to <address> and <address> <cr>
```

Handler ` RVA 0xF810790 `；selector ` 75 `；EOL ` RVA 0x34758128 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Source address to translate；` unsigned_number ` Mask length for translation；` address ` First source address to translate to；` address ` Second source address to translate to。

[条件 C-132f1b4d27511b2d](../../evidence/conditions-sets-008.md#c-132f1b4d27511b2d) · [参数 P-9655d9280aaf6c6c](../../evidence/parameters-sets-012.md#p-9655d9280aaf6c6c) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060137

```text
(config)# ip pim mofrr clone source <address> mask-length <number:0..32> to <address> and <address> <cr>
```

Handler ` RVA 0xF810790 `；selector ` 74 `；EOL ` RVA 0x34757C90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Source address to translate；` unsigned_number ` Mask length for translation；` address ` First source address to translate to；` address ` Second source address to translate to。

[条件 C-f68d1b4a6d0a9c3a](../../evidence/conditions-sets-095.md#c-f68d1b4a6d0a9c3a) · [参数 P-b1ff2b8651862785](../../evidence/parameters-sets-013.md#p-b1ff2b8651862785) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-061248

```text
(config)# ip pim mofrr flow <number:100..199> <interface> <cr>
```

Handler ` RVA 0xF810790 `；selector ` 73 `；EOL ` RVA 0x34757690 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Extended Access-list number。

[条件 C-36ed81a8a40bed5e](../../evidence/conditions-sets-021.md#c-36ed81a8a40bed5e) · [缺口 G-9cdeb171629d3468](../../evidence/gaps-sets-006.md#g-9cdeb171629d3468) · [参数 P-96fed1b84b7812d7](../../evidence/parameters-sets-012.md#p-96fed1b84b7812d7) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060792

```text
(config)# ip pim mpls source <interface> <cr>
```

Handler ` RVA 0xF810790 `；selector ` 67 `；EOL ` RVA 0x347586A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9cbbb9ef88401cc2](../../evidence/conditions-sets-061.md#c-9cbbb9ef88401cc2) · [缺口 G-423f966f12c85a01](../../evidence/gaps-sets-003.md#g-423f966f12c85a01) · [参数 P-fe295aa6d3c5904c](../../evidence/parameters-sets-019.md#p-fe295aa6d3c5904c) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026700

```text
(config)# ip pim old-register-checksum <cr>
```

Handler ` RVA 0xF810790 `；selector ` 61 `；EOL ` RVA 0x34758978 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1c1d4d7eb6586ba0](../../evidence/conditions-sets-011.md#c-1c1d4d7eb6586ba0) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-035395

```text
(config)# ip pim pfp-sa announce <address> <cr>
```

Handler ` RVA 0xF810790 `；selector ` 80 `；EOL ` RVA 0x3475AA58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Source IP address for PFP-SA announcements。

[条件 C-eaa22cefbb07b6f5](../../evidence/conditions-sets-091.md#c-eaa22cefbb07b6f5) · [参数 P-3d1695053103054c](../../evidence/parameters-sets-005.md#p-3d1695053103054c) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029363

```text
(config)# ip pim pfp-sa cache <cr>
```

Handler ` RVA 0xF810790 `；selector ` 85 `；EOL ` RVA 0x3475B4F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3568a5f8e0629606](../../evidence/conditions-sets-021.md#c-3568a5f8e0629606) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-044888

```text
(config)# ip pim pfp-sa timers holdtime <number:1..3600> <cr>
```

Handler ` RVA 0xF810790 `；selector ` 81 `；EOL ` RVA 0x3475AEF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Holdtime in seconds。

[条件 C-86b69c3e4073479f](../../evidence/conditions-sets-052.md#c-86b69c3e4073479f) · [参数 P-d2ed133a35a21468](../../evidence/parameters-sets-016.md#p-d2ed133a35a21468) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-044920

```text
(config)# ip pim pfp-sa timers interval <number:1..3600> <cr>
```

Handler ` RVA 0xF810790 `；selector ` 82 `；EOL ` RVA 0x3475B1E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Interval in seconds。

[条件 C-4b94b96041502d78](../../evidence/conditions-sets-030.md#c-4b94b96041502d78) · [参数 P-018c37c03402ddd7](../../evidence/parameters-sets-001.md#p-018c37c03402ddd7) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029479

```text
(config)# ip pim register-rate-limit <number:8000..2000000000> <cr>
```

Handler ` RVA 0xF810790 `；selector ` 24 `；EOL ` RVA 0x3475E310 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Bits per second。

[条件 C-0f322e69c466ed32](../../evidence/conditions-sets-006.md#c-0f322e69c466ed32) · [参数 P-047fc1366507a919](../../evidence/parameters-sets-001.md#p-047fc1366507a919) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060599

```text
(config)# ip pim register-source <interface> <cr>
```

Handler ` RVA 0xF810790 `；selector ` 28 `；EOL ` RVA 0x3475E6B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-618f50b0944e390a](../../evidence/conditions-sets-038.md#c-618f50b0944e390a) · [缺口 G-da37c330c1f82884](../../evidence/gaps-sets-008.md#g-da37c330c1f82884) · [参数 P-fc077d1cb33aa4f6](../../evidence/parameters-sets-019.md#p-fc077d1cb33aa4f6) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029186

```text
(config)# ip pim rp-address <address> <cr>
```

Handler ` RVA 0xF810790 `；selector ` 1 `；EOL ` RVA 0x3475A360 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP address of Rendezvous-point for group。

[条件 C-9b0cc7ff7408a6e1](../../evidence/conditions-sets-060.md#c-9b0cc7ff7408a6e1) · [参数 P-11c19964b1ed5fc8](../../evidence/parameters-sets-002.md#p-11c19964b1ed5fc8) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026937

```text
(config)# ip pim rp-announce-filter <cr>
```

Handler ` RVA 0xF810790 `；selector ` 15 `；EOL ` RVA 0x3475D068 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f11aeac7f1fc2a24](../../evidence/conditions-sets-093.md#c-f11aeac7f1fc2a24) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060585

```text
(config)# ip pim rp-candidate <interface> <cr>
```

Handler ` RVA 0xF810790 `；selector ` 21 `；EOL ` RVA 0x3475C908 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b4ec5c87345987de](../../evidence/conditions-sets-070.md#c-b4ec5c87345987de) · [缺口 G-0a067b7228a6e025](../../evidence/gaps-sets-001.md#g-0a067b7228a6e025) · [参数 P-370f9482d3f266b8](../../evidence/parameters-sets-005.md#p-370f9482d3f266b8) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026720

```text
(config)# ip pim rp-proxy-join <cr>
```

Handler ` RVA 0xF810790 `；selector ` 25 `；EOL ` RVA 0x34759A80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-63db2e88a69e048f](../../evidence/conditions-sets-039.md#c-63db2e88a69e048f) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-045269

```text
(config)# ip pim send-rp-announce <address> scope <number:1..255> <cr>
```

Handler ` RVA 0xF810790 `；selector ` 13 `；EOL ` RVA 0x3475D530 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP address of RP for group；` unsigned_number ` TTL of the RP announce packet。

[条件 C-61d1ef3e1452f1bf](../../evidence/conditions-sets-038.md#c-61d1ef3e1452f1bf) · [参数 P-9bda9d910c941258](../../evidence/parameters-sets-012.md#p-9bda9d910c941258) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060591

```text
(config)# ip pim send-rp-announce <interface> <cr>
```

Handler ` RVA 0xF810790 `；selector ` 13 `；EOL ` RVA 0x3475D530 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b0ccd9f28cf407fb](../../evidence/conditions-sets-068.md#c-b0ccd9f28cf407fb) · [缺口 G-4acad814951287bc](../../evidence/gaps-sets-003.md#g-4acad814951287bc) · [参数 P-4a0f1a5d0e0c6d55](../../evidence/parameters-sets-006.md#p-4a0f1a5d0e0c6d55) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-061285

```text
(config)# ip pim send-rp-discovery <interface> scope <number:1..255> <cr>
```

Handler ` RVA 0xF810790 `；selector ` 14 `；EOL ` RVA 0x3475DB48 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` TTL。

[条件 C-23b9f0b98d537cec](../../evidence/conditions-sets-014.md#c-23b9f0b98d537cec) · [缺口 G-297e357bcaab2009](../../evidence/gaps-sets-002.md#g-297e357bcaab2009) · [参数 P-cd991f57dda4a5bc](../../evidence/parameters-sets-016.md#p-cd991f57dda4a5bc) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-035653

```text
(config)# ip pim send-rp-discovery scope <number:1..255> <cr>
```

Handler ` RVA 0xF810790 `；selector ` 14 `；EOL ` RVA 0x3475DB48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` TTL。

[条件 C-11a48d94a8a6ba8f](../../evidence/conditions-sets-007.md#c-11a48d94a8a6ba8f) · [参数 P-82a8c2c263c516dd](../../evidence/parameters-sets-010.md#p-82a8c2c263c516dd) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029856

```text
(config)# ip pim sparse accept-source-reports <cr>
```

Handler ` RVA 0xF810790 `；selector ` 40 `；EOL ` RVA 0x3475FEA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a988b01983561a02](../../evidence/conditions-sets-065.md#c-a988b01983561a02) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-036042

```text
(config)# ip pim sparse sg-expiry-timer <number:181..57600> <cr>
```

Handler ` RVA 0xF810790 `；selector ` 58 `；EOL ` RVA 0x3475FA40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timer Value in seconds。

[条件 C-6d533e8196a4bbc3](../../evidence/conditions-sets-042.md#c-6d533e8196a4bbc3) · [参数 P-45abe2aea171106c](../../evidence/parameters-sets-006.md#p-45abe2aea171106c) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029076

```text
(config)# ip pim spt-threshold 0 <cr>
```

Handler ` RVA 0xF810790 `；selector ` 8 `；EOL ` RVA 0x3475B978 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-21d0519a794d6b68](../../evidence/conditions-sets-013.md#c-21d0519a794d6b68) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029632

```text
(config)# ip pim ssm default <cr>
```

Handler ` RVA 0xF810790 `；selector ` 35 `；EOL ` RVA 0x3475F2E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-572a99d840ce26c3](../../evidence/conditions-sets-034.md#c-572a99d840ce26c3) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-028716

```text
(config)# ip pim state-refresh disable <cr>
```

Handler ` RVA 0xF810790 `；selector ` 38 `；EOL ` RVA 0x347594F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-63db2e88a69e048f](../../evidence/conditions-sets-039.md#c-63db2e88a69e048f) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027080

```text
(config)# ip pim v1-rp-reachability <cr>
```

Handler ` RVA 0xF810790 `；selector ` 56 `；EOL ` RVA 0x34760230 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-21d0519a794d6b68](../../evidence/conditions-sets-013.md#c-21d0519a794d6b68) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-028543

```text
(config)# ip policy-list <string> permit <cr>
```

Handler ` RVA 0xE222AD0 `；selector ` 0 `；EOL ` RVA 0x344CC430 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` IP Policy list name。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [参数 P-e006b5636d1218eb](../../evidence/parameters-sets-017.md#p-e006b5636d1218eb) · [状态效果 S-29139978aadce204](../../evidence/state_effects-sets-009.md#s-29139978aadce204)

### path-025688

```text
(config)# ip portbundle <cr>
```

Handler ` RVA 0x11C30260 `；selector ` 0 `；EOL ` RVA 0x356A5468 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027129

```text
(config)# ip prefix-list <string> <cr>
```

Handler ` RVA 0xE21E820 `；selector ` 0 `；EOL ` RVA 0x342828B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of a prefix list。

[条件 C-ef81943334c4fd37](../../evidence/conditions-sets-092.md#c-ef81943334c4fd37) · [参数 P-ba56a54852b2cae0](../../evidence/parameters-sets-014.md#p-ba56a54852b2cae0) · [状态效果 S-07717392aa7dd4e0](../../evidence/state_effects-sets-002.md#s-07717392aa7dd4e0)

### path-060845

```text
(config)# ip prefix-list <string> deny <prefix:dynamic> <cr>
```

Handler ` RVA 0xE21E820 `；selector ` 0 `；EOL ` RVA 0x342821B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Name of a prefix list；` prefix_dynamic ` IP prefix &lt;network&gt;/&lt;length&gt;, e.g., 35.0.0.0/8。

[条件 C-ef872344507738c7](../../evidence/conditions-sets-093.md#c-ef872344507738c7) · [缺口 G-3f1bd91d9ef3edfd](../../evidence/gaps-sets-003.md#g-3f1bd91d9ef3edfd) · [参数 P-bd1296d7a1dec660](../../evidence/parameters-sets-014.md#p-bd1296d7a1dec660) · [状态效果 S-c67d5645c86d4cb9](../../evidence/state_effects-sets-042.md#s-c67d5645c86d4cb9)

### path-026982

```text
(config)# ip prefix-list sequence-number <cr>
```

Handler ` RVA 0xE21E820 `；selector ` 0 `；EOL ` RVA 0x342821B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [状态效果 S-99a55a33fdec717f](../../evidence/state_effects-sets-033.md#s-99a55a33fdec717f)

### path-060608

```text
(config)# ip radius source-interface <interface> <cr>
```

Handler ` RVA 0xFFD39D0 `；selector ` 16 `；EOL ` RVA 0x34966C68 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3aa5dbafc33e0864](../../evidence/conditions-sets-023.md#c-3aa5dbafc33e0864) · [缺口 G-c02e966ef73687ae](../../evidence/gaps-sets-007.md#g-c02e966ef73687ae) · [参数 P-e2ef000bed1d737c](../../evidence/parameters-sets-017.md#p-e2ef000bed1d737c) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026480

```text
(config)# ip rcmd domain-lookup <cr>
```

Handler ` RVA 0xCFFFEF0 `；selector ` 3 `；EOL ` RVA 0x33D7BC68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026525

```text
(config)# ip rcmd rcp-enable <cr>
```

Handler ` RVA 0xCFFFEF0 `；selector ` 5 `；EOL ` RVA 0x33D7BF78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-044495

```text
(config)# ip rcmd remote-host <string> <number:1..99> <string> <cr>
```

Handler ` RVA 0xCFFFEF0 `；selector ` 2 `；EOL ` RVA 0x33D7CA30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Local username；` unsigned_number ` Access list number；` string ` Remote username。

[条件 C-d295f102cfe702ea](../../evidence/conditions-sets-081.md#c-d295f102cfe702ea) · [参数 P-cf26ffcd1ce3a747](../../evidence/parameters-sets-016.md#p-cf26ffcd1ce3a747) · [状态效果 S-f049663d16c05aaf](../../evidence/state_effects-sets-051.md#s-f049663d16c05aaf)

### path-028576

```text
(config)# ip rcmd remote-username <string> <cr>
```

Handler ` RVA 0xCFFFEF0 `；selector ` 1 `；EOL ` RVA 0x33D7CE30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` This system's username for remote commands。

[条件 C-7f57ea015208f302](../../evidence/conditions-sets-049.md#c-7f57ea015208f302) · [参数 P-3cbd027b03a6a105](../../evidence/parameters-sets-005.md#p-3cbd027b03a6a105) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-028491

```text
(config)# ip rcmd rsh-disable-command <string> <cr>
```

Handler ` RVA 0xCFFFEF0 `；selector ` 6 `；EOL ` RVA 0x33D7C570 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [参数 P-1d40cf10fb3b7071](../../evidence/parameters-sets-003.md#p-1d40cf10fb3b7071) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026545

```text
(config)# ip rcmd rsh-enable <cr>
```

Handler ` RVA 0xCFFFEF0 `；selector ` 4 `；EOL ` RVA 0x33D7C258 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060547

```text
(config)# ip rcmd source-interface <interface> <cr>
```

Handler ` RVA 0xCFFFEF0 `；selector ` 0 `；EOL ` RVA 0x33D7D150 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3c09c704b06251d5](../../evidence/conditions-sets-023.md#c-3c09c704b06251d5) · [缺口 G-4c35a9db0167f769](../../evidence/gaps-sets-003.md#g-4c35a9db0167f769) · [参数 P-e7832fde1a7d098c](../../evidence/parameters-sets-017.md#p-e7832fde1a7d098c) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060630

```text
(config)# ip reflexive-list timeout <number:dynamic> <cr>
```

Handler ` RVA 0xF9C1E90 `；selector ` 0 `；EOL ` RVA 0x3479B210 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` timeout in seconds。

[条件 C-2e66359590d1aa8b](../../evidence/conditions-sets-018.md#c-2e66359590d1aa8b) · [缺口 G-9398a1a0a416518d](../../evidence/gaps-sets-005.md#g-9398a1a0a416518d) · [参数 P-c1bb070c49051e6e](../../evidence/parameters-sets-015.md#p-c1bb070c49051e6e) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-062720

```text
(config)# ip route * <cr>
```

Handler ` RVA 0xE2A7A50 `；selector ` 0 `；EOL ` RVA 0x3428BEC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3be99269fa3a7e1a](../../evidence/conditions-sets-023.md#c-3be99269fa3a7e1a) · [缺口 G-30fcac0158fc2e1a](../../evidence/gaps-sets-002.md#g-30fcac0158fc2e1a) · [状态效果 S-0a1b22d676480ac4](../../evidence/state_effects-sets-003.md#s-0a1b22d676480ac4)

### path-060624

```text
(config)# ip route <address> <address> <cr>
```

Handler ` RVA 0xE2A3100 `；selector ` 1 `；EOL ` RVA 0x3428AE40 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Destination prefix；` address ` Destination prefix mask。

[条件 C-bb5a36081f1dd394](../../evidence/conditions-sets-072.md#c-bb5a36081f1dd394) · [缺口 G-e475d597da05478a](../../evidence/gaps-sets-008.md#g-e475d597da05478a) · [参数 P-a81c2ba8127f8ad0](../../evidence/parameters-sets-013.md#p-a81c2ba8127f8ad0) · [状态效果 S-0a1b22d676480ac4](../../evidence/state_effects-sets-003.md#s-0a1b22d676480ac4)

### path-062487

```text
(config)# ip route <address> <address> segment-routing mpls path name <string> <cr>
```

Handler ` RVA 0xE2A4130 `；selector ` 0 `；EOL ` RVA 0x3428A888 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Destination prefix；` address ` Destination prefix mask；` string ` Explicit-Path name that will have labels defined。

[条件 C-eb2d9081004e7b74](../../evidence/conditions-sets-091.md#c-eb2d9081004e7b74) · [缺口 G-e475d597da05478a](../../evidence/gaps-sets-008.md#g-e475d597da05478a) · [参数 P-25b4b30453f0a590](../../evidence/parameters-sets-003.md#p-25b4b30453f0a590) · [状态效果 S-0a1b22d676480ac4](../../evidence/state_effects-sets-003.md#s-0a1b22d676480ac4)

### path-060400

```text
(config)# ip route profile <cr>
```

Handler ` RVA 0xE1AD560 `；selector ` 0 `；EOL ` RVA 0x34292218 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e7e203f63963497d](../../evidence/conditions-sets-090.md#c-e7e203f63963497d) · [缺口 G-e475d597da05478a](../../evidence/gaps-sets-008.md#g-e475d597da05478a) · [状态效果 S-0a1b22d676480ac4](../../evidence/state_effects-sets-003.md#s-0a1b22d676480ac4)

### path-060590

```text
(config)# ip route static adjust-time <cr>
```

Handler ` RVA 0xE2A7C50 `；selector ` 0 `；EOL ` RVA 0x342907C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-21af20f69d0b0233](../../evidence/conditions-sets-013.md#c-21af20f69d0b0233) · [缺口 G-e475d597da05478a](../../evidence/gaps-sets-008.md#g-e475d597da05478a) · [状态效果 S-0a1b22d676480ac4](../../evidence/state_effects-sets-003.md#s-0a1b22d676480ac4)

### path-061300

```text
(config)# ip route static bfd group <string> <cr>
```

Handler ` RVA 0xE2A6B20 `；selector ` 0 `；EOL ` RVA 0x34291020 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` bfd group name。

[条件 C-6f868cc6d2735449](../../evidence/conditions-sets-043.md#c-6f868cc6d2735449) · [缺口 G-e475d597da05478a](../../evidence/gaps-sets-008.md#g-e475d597da05478a) · [参数 P-b144741c3396d01d](../../evidence/parameters-sets-013.md#p-b144741c3396d01d) · [状态效果 S-0a1b22d676480ac4](../../evidence/state_effects-sets-003.md#s-0a1b22d676480ac4)

### path-060602

```text
(config)# ip route static install-routes-recurse-via-nexthop <cr>
```

Handler ` RVA 0xE2A63F0 `；selector ` 1 `；EOL ` RVA 0x34291CE8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-cf5a229bb0cbada3](../../evidence/conditions-sets-080.md#c-cf5a229bb0cbada3) · [缺口 G-e475d597da05478a](../../evidence/gaps-sets-008.md#g-e475d597da05478a) · [状态效果 S-0a1b22d676480ac4](../../evidence/state_effects-sets-003.md#s-0a1b22d676480ac4)

### path-060831

```text
(config)# ip route static install-routes-recurse-via-nexthop all <cr>
```

Handler ` RVA 0xE2A63F0 `；selector ` 0 `；EOL ` RVA 0x34291A18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-cf5a229bb0cbada3](../../evidence/conditions-sets-080.md#c-cf5a229bb0cbada3) · [缺口 G-e475d597da05478a](../../evidence/gaps-sets-008.md#g-e475d597da05478a) · [状态效果 S-0a1b22d676480ac4](../../evidence/state_effects-sets-003.md#s-0a1b22d676480ac4)

### path-060583

```text
(config)# ip route static inter-vrf <cr>
```

Handler ` RVA 0xE2A5EE0 `；selector ` 2 `；EOL ` RVA 0x34290A50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e7e203f63963497d](../../evidence/conditions-sets-090.md#c-e7e203f63963497d) · [缺口 G-e475d597da05478a](../../evidence/gaps-sets-008.md#g-e475d597da05478a) · [状态效果 S-0a1b22d676480ac4](../../evidence/state_effects-sets-003.md#s-0a1b22d676480ac4)

### path-029622

```text
(config)# ip rsvp aggregation ip <cr>
```

Handler ` RVA 0x101C30A0 `；selector ` 0 `；EOL ` RVA 0x34A685F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-045301

```text
(config)# ip rsvp aggregation ip level <number:1..8> <cr>
```

Handler ` RVA 0x101C3940 `；selector ` 0 `；EOL ` RVA 0x34A68340 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Aggregation level (default = 1)。

[条件 C-6d41f1aa0154f709](../../evidence/conditions-sets-042.md#c-6d41f1aa0154f709) · [参数 P-a0149a85a4668090](../../evidence/parameters-sets-012.md#p-a0149a85a4668090) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-062267

```text
(config)# ip rsvp aggregation ip map any dscp <?common_dscp_value_action@555589fbb708> <cr>
```

Handler ` RVA 0x101C35A0 `；selector ` 0 `；EOL ` RVA 0x34A676E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0f16b4116d3858de](../../evidence/conditions-sets-006.md#c-0f16b4116d3858de) · [缺口 G-63afcb4078404007](../../evidence/gaps-sets-004.md#g-63afcb4078404007) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-061891

```text
(config)# ip rsvp aggregation ip reservation dscp <?common_dscp_value_action@555589fbbb90> <cr>
```

Handler ` RVA 0x101C31D0 `；selector ` 0 `；EOL ` RVA 0x34A67D70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-80cb35718c2fb7fc](../../evidence/conditions-sets-050.md#c-80cb35718c2fb7fc) · [缺口 G-d7c63f65bc2423dc](../../evidence/gaps-sets-008.md#g-d7c63f65bc2423dc) · [状态效果 S-1de54c84e2129eb5](../../evidence/state_effects-sets-007.md#s-1de54c84e2129eb5)

### path-052977

```text
(config)# ip rsvp aggregation ip sender service guaranteed-rate <cr>
```

Handler ` RVA 0x101C3A90 `；selector ` 0 `；EOL ` RVA 0x34A686D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-05e33d4371515894](../../evidence/conditions-sets-003.md#c-05e33d4371515894) · [状态效果 S-84b37de1778455b5](../../evidence/state_effects-sets-028.md#s-84b37de1778455b5)

### path-027102

```text
(config)# ip rsvp authentication <cr>
```

Handler ` RVA 0x10073550 `；selector ` 10 `；EOL ` RVA 0x34A439B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ab4c1b3cef308834](../../evidence/conditions-sets-066.md#c-ab4c1b3cef308834) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029752

```text
(config)# ip rsvp authentication challenge <cr>
```

Handler ` RVA 0x10073550 `；selector ` 8 `；EOL ` RVA 0x34A43728 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4141a4ab24b771d7](../../evidence/conditions-sets-025.md#c-4141a4ab24b771d7) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-035688

```text
(config)# ip rsvp authentication key-chain <string> <cr>
```

Handler ` RVA 0x10073550 `；selector ` 12 `；EOL ` RVA 0x34A428F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of key chain (as created by global "key chain" command)。

[条件 C-6b12709ad36fdea2](../../evidence/conditions-sets-041.md#c-6b12709ad36fdea2) · [参数 P-18fa03624672cf67](../../evidence/parameters-sets-002.md#p-18fa03624672cf67) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060842

```text
(config)# ip rsvp authentication lifetime <hh:mm:ss> <cr>
```

Handler ` RVA 0x10073550 `；selector ` 9 `；EOL ` RVA 0x34A43408 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` time_hms ` Lifetime (default = 30 mins)。

[条件 C-19d4ba420088370c](../../evidence/conditions-sets-010.md#c-19d4ba420088370c) · [缺口 G-0e12140a935b62c5](../../evidence/gaps-sets-001.md#g-0e12140a935b62c5) · [参数 P-af5b3f6368d6a109](../../evidence/parameters-sets-013.md#p-af5b3f6368d6a109) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029755

```text
(config)# ip rsvp authentication type <cr>
```

Handler ` RVA 0x10073550 `；selector ` 7 `；EOL ` RVA 0x34A43020 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fd55ee9b264084e3](../../evidence/conditions-sets-098.md#c-fd55ee9b264084e3) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-035814

```text
(config)# ip rsvp authentication window-size <number:1..64> <cr>
```

Handler ` RVA 0x10073550 `；selector ` 5 `；EOL ` RVA 0x34A42C78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Maximum number of messages allowed in receive window (default = 1)。

[条件 C-09011093ea50c8b3](../../evidence/conditions-sets-004.md#c-09011093ea50c8b3) · [参数 P-8e192b49c198dcdd](../../evidence/parameters-sets-011.md#p-8e192b49c198dcdd) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-053228

```text
(config)# ip rsvp listener <address> <number:0..255> <number:0..65535> announce <cr>
```

Handler ` RVA 0x1005E650 `；selector ` 0 `；EOL ` RVA 0x34A46B78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Destination address；` unsigned_number ` IP Protocol；` unsigned_number ` Destination port。

[条件 C-0e1fdee263dd9cba](../../evidence/conditions-sets-006.md#c-0e1fdee263dd9cba) · [参数 P-8cbcf1b136e2c8b3](../../evidence/parameters-sets-011.md#p-8cbcf1b136e2c8b3) · [状态效果 S-0fc3cbe01442ac94](../../evidence/state_effects-sets-004.md#s-0fc3cbe01442ac94)

### path-027065

```text
(config)# ip rsvp metadata <cr>
```

Handler ` RVA 0x10077B70 `；selector ` 0 `；EOL ` RVA 0x34A4CBC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-059124

```text
(config)# ip rsvp metadata sender-host <address> <address> <number:0..255> <number:0..65535> <number:0..65535> <cr>
```

Handler ` RVA 0x10077C60 `；selector ` 0 `；EOL ` RVA 0x34A4CEE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Destination address；` address ` Source address；` unsigned_number ` IP Protocol；` unsigned_number ` Destination port；` unsigned_number ` Source port。

[条件 C-ddbbd97d6c600413](../../evidence/conditions-sets-085.md#c-ddbbd97d6c600413) · [参数 P-f430d883716a98a9](../../evidence/parameters-sets-018.md#p-f430d883716a98a9) · [状态效果 S-b0473533179f4957](../../evidence/state_effects-sets-037.md#s-b0473533179f4957)

### path-029577

```text
(config)# ip rsvp metadata statistics <cr>
```

Handler ` RVA 0x100783D0 `；selector ` 0 `；EOL ` RVA 0x34A4C8F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027226

```text
(config)# ip rsvp msg-pacing <cr>
```

Handler ` RVA 0x10070FD0 `；selector ` 0 `；EOL ` RVA 0x34A472B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e1fdee263dd9cba](../../evidence/conditions-sets-006.md#c-0e1fdee263dd9cba) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029605

```text
(config)# ip rsvp policy default-reject <cr>
```

Handler ` RVA 0x10113260 `；selector ` 0 `；EOL ` RVA 0x34A416A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e5d040cadd4659a2](../../evidence/conditions-sets-089.md#c-e5d040cadd4659a2) · [状态效果 S-b223d618a7b1c9be](../../evidence/state_effects-sets-038.md#s-b223d618a7b1c9be)

### path-052955

```text
(config)# ip rsvp policy identity <string> policy-locator <string> <cr>
```

Handler ` RVA 0x10113AC0 `；selector ` 0 `；EOL ` RVA 0x34A412F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Alias for use in other CLI commands (quotes allowed)；` string ` A regular expression to match X.500 DNs (use "ctrl-v ?" to enter "?")。

[条件 C-0f73287e3e21c1ac](../../evidence/conditions-sets-006.md#c-0f73287e3e21c1ac) · [参数 P-8ecead2ccfab3cf9](../../evidence/parameters-sets-011.md#p-8ecead2ccfab3cf9) · [状态效果 S-aab8c7855151b1d4](../../evidence/state_effects-sets-036.md#s-aab8c7855151b1d4)

### path-035871

```text
(config)# ip rsvp policy local default <cr>
```

Handler ` RVA 0x101134B0 `；selector ` 257 `；EOL ` RVA 0x34A41D18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4468f9f696c3dd63](../../evidence/conditions-sets-027.md#c-4468f9f696c3dd63) · [状态效果 S-9518eb4dfe9bc10b](../../evidence/state_effects-sets-032.md#s-9518eb4dfe9bc10b)

### path-061311

```text
(config)# ip rsvp policy local identity <string> <cr>
```

Handler ` RVA 0x101134B0 `；selector ` 257 `；EOL ` RVA 0x34A41D18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Local alias for identity 1 (quotes allowed)。

[条件 C-4468f9f696c3dd63](../../evidence/conditions-sets-027.md#c-4468f9f696c3dd63) · [缺口 G-902fb2bb9ce93ed4](../../evidence/gaps-sets-005.md#g-902fb2bb9ce93ed4) · [参数 P-667594126738b066](../../evidence/parameters-sets-008.md#p-667594126738b066) · [状态效果 S-5d205db6b58a0a39](../../evidence/state_effects-sets-020.md#s-5d205db6b58a0a39)

### path-029704

```text
(config)# ip rsvp policy preempt <cr>
```

Handler ` RVA 0x10113340 `；selector ` 0 `；EOL ` RVA 0x34A419C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-09b8a62e50b3e9c5](../../evidence/conditions-sets-004.md#c-09b8a62e50b3e9c5) · [状态效果 S-b223d618a7b1c9be](../../evidence/state_effects-sets-038.md#s-b223d618a7b1c9be)

### path-027055

```text
(config)# ip rsvp pq-profile <cr>
```

Handler ` RVA 0x10054960 `；selector ` 0 `；EOL ` RVA 0x34A43D40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1d456e37fe8f90ea](../../evidence/conditions-sets-011.md#c-1d456e37fe8f90ea) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027203

```text
(config)# ip rsvp qos <cr>
```

Handler ` RVA 0x10077270 `；selector ` 0 `；EOL ` RVA 0x34A4C590 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6c279dcac619e81b](../../evidence/conditions-sets-042.md#c-6c279dcac619e81b) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-062680

```text
(config)# ip rsvp reservation <address> <address> <number:0..255> <number:0..65535> <number:0..65535> <address> <interface> wf load <number:1..10000000> <number:1..65535> <cr>
```

Handler ` RVA 0x10059EB0 `；selector ` 0 `；EOL ` RVA 0x34A46428 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Destination address；` address ` Source address；` unsigned_number ` IP Protocol；` unsigned_number ` Destination port；` unsigned_number ` Source port；` address ` Next Hop address；` unsigned_number ` Average Bit Rate to reserve (kbps)；` unsigned_number ` Maximum Burst in Kilobytes。

[条件 C-f1390453aba85705](../../evidence/conditions-sets-093.md#c-f1390453aba85705) · [缺口 G-6bc8333877c52c6a](../../evidence/gaps-sets-004.md#g-6bc8333877c52c6a) · [参数 P-6be2d93a6fc9a449](../../evidence/parameters-sets-009.md#p-6be2d93a6fc9a449) · [状态效果 S-63d13cebd4746e12](../../evidence/state_effects-sets-021.md#s-63d13cebd4746e12)

### path-060159

```text
(config)# ip rsvp reservation <address> <address> <number:0..255> <number:0..65535> <number:0..65535> wf load <number:1..10000000> <number:1..65535> <cr>
```

Handler ` RVA 0x10059EB0 `；selector ` 0 `；EOL ` RVA 0x34A46428 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Destination address；` address ` Source address；` unsigned_number ` IP Protocol；` unsigned_number ` Destination port；` unsigned_number ` Source port；` unsigned_number ` Average Bit Rate to reserve (kbps)；` unsigned_number ` Maximum Burst in Kilobytes。

[条件 C-bb1a7866ded119ba](../../evidence/conditions-sets-072.md#c-bb1a7866ded119ba) · [参数 P-68894bfe840994a4](../../evidence/parameters-sets-008.md#p-68894bfe840994a4) · [状态效果 S-63d13cebd4746e12](../../evidence/state_effects-sets-021.md#s-63d13cebd4746e12)

### path-062663

```text
(config)# ip rsvp sender <address> <address> <number:0..255> <number:0..65535> <number:0..65535> <address> <interface> <number:1..10000000> <number:1..65535> <cr>
```

Handler ` RVA 0x1005AFF0 `；selector ` 0 `；EOL ` RVA 0x34A457D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Destination address；` address ` Source address；` unsigned_number ` IP Protocol；` unsigned_number ` Destination port；` unsigned_number ` Source port；` address ` Previous Hop address；` unsigned_number ` Average Bit Rate to reserve (kbps)；` unsigned_number ` Maximum Burst in Kilobytes。

[条件 C-0e1890ef536c272c](../../evidence/conditions-sets-006.md#c-0e1890ef536c272c) · [缺口 G-f9044411fbea3cd1](../../evidence/gaps-sets-009.md#g-f9044411fbea3cd1) · [参数 P-9071597bfb7c0c0e](../../evidence/parameters-sets-011.md#p-9071597bfb7c0c0e) · [状态效果 S-184374f4e109ebbd](../../evidence/state_effects-sets-006.md#s-184374f4e109ebbd)

### path-062665

```text
(config)# ip rsvp sender <address> <address> <number:0..255> <number:0..65535> <number:0..65535> <address> <interface> <number:1..10000000> <number:1..65535> <cr>
```

Handler ` RVA 0x1005C360 `；selector ` 0 `；EOL ` RVA 0x34A454C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Destination address；` address ` Source address；` unsigned_number ` IP Protocol；` unsigned_number ` Destination port；` unsigned_number ` Source port；` address ` Previous Hop address；` unsigned_number ` Average Bit Rate to reserve (kbps)；` unsigned_number ` Maximum Burst in Kilobytes。

[条件 C-0a92d3389e623413](../../evidence/conditions-sets-004.md#c-0a92d3389e623413) · [缺口 G-f9044411fbea3cd1](../../evidence/gaps-sets-009.md#g-f9044411fbea3cd1) · [参数 P-9071597bfb7c0c0e](../../evidence/parameters-sets-011.md#p-9071597bfb7c0c0e) · [状态效果 S-184374f4e109ebbd](../../evidence/state_effects-sets-006.md#s-184374f4e109ebbd)

### path-059755

```text
(config)# ip rsvp sender <address> <address> <number:0..255> <number:0..65535> <number:0..65535> <number:1..10000000> <number:1..65535> <cr>
```

Handler ` RVA 0x1005AFF0 `；selector ` 0 `；EOL ` RVA 0x34A457D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Destination address；` address ` Source address；` unsigned_number ` IP Protocol；` unsigned_number ` Destination port；` unsigned_number ` Source port；` unsigned_number ` Average Bit Rate to reserve (kbps)；` unsigned_number ` Maximum Burst in Kilobytes。

[条件 C-061b76ea09df04f1](../../evidence/conditions-sets-003.md#c-061b76ea09df04f1) · [参数 P-73daa0f5da215834](../../evidence/parameters-sets-009.md#p-73daa0f5da215834) · [状态效果 S-184374f4e109ebbd](../../evidence/state_effects-sets-006.md#s-184374f4e109ebbd)

### path-059759

```text
(config)# ip rsvp sender <address> <address> <number:0..255> <number:0..65535> <number:0..65535> <number:1..10000000> <number:1..65535> <cr>
```

Handler ` RVA 0x1005C360 `；selector ` 0 `；EOL ` RVA 0x34A454C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Destination address；` address ` Source address；` unsigned_number ` IP Protocol；` unsigned_number ` Destination port；` unsigned_number ` Source port；` unsigned_number ` Average Bit Rate to reserve (kbps)；` unsigned_number ` Maximum Burst in Kilobytes。

[条件 C-fffe20e206279b23](../../evidence/conditions-sets-099.md#c-fffe20e206279b23) · [参数 P-73daa0f5da215834](../../evidence/parameters-sets-009.md#p-73daa0f5da215834) · [状态效果 S-184374f4e109ebbd](../../evidence/state_effects-sets-006.md#s-184374f4e109ebbd)

### path-045904

```text
(config)# ip rsvp signalling fast-local-repair notifications <number:10..10000> <cr>
```

Handler ` RVA 0x10056150 `；selector ` 0 `；EOL ` RVA 0x34A47AA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of notifications to process before suspend。

[条件 C-c2aea443fef08e27](../../evidence/conditions-sets-075.md#c-c2aea443fef08e27) · [参数 P-bdbf20c4318850ba](../../evidence/parameters-sets-014.md#p-bdbf20c4318850ba) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-045957

```text
(config)# ip rsvp signalling fast-local-repair rate <number:1..2500> <cr>
```

Handler ` RVA 0x10056050 `；selector ` 0 `；EOL ` RVA 0x34A47DC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Fast Local Repair rate in messages/sec。

[条件 C-3abbad21a0e40767](../../evidence/conditions-sets-023.md#c-3abbad21a0e40767) · [参数 P-7961665fcf53fb72](../../evidence/parameters-sets-009.md#p-7961665fcf53fb72) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-030445

```text
(config)# ip rsvp signalling hello <cr>
```

Handler ` RVA 0x10074260 `；selector ` 0 `；EOL ` RVA 0x34A4AD28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ee70c5bde95b3ce5](../../evidence/conditions-sets-092.md#c-ee70c5bde95b3ce5) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-036973

```text
(config)# ip rsvp signalling hello bfd <cr>
```

Handler ` RVA 0x10074350 `；selector ` 0 `；EOL ` RVA 0x34A4AA18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5924a81640a4c9be](../../evidence/conditions-sets-035.md#c-5924a81640a4c9be) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-036943

```text
(config)# ip rsvp signalling hello cleanup-timer <cr>
```

Handler ` RVA 0x10077100 `；selector ` 0 `；EOL ` RVA 0x34A4A750 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3267b594985264c1](../../evidence/conditions-sets-020.md#c-3267b594985264c1) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-036774

```text
(config)# ip rsvp signalling hello down <cr>
```

Handler ` RVA 0x10074670 `；selector ` 0 `；EOL ` RVA 0x34A49E18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3267b594985264c1](../../evidence/conditions-sets-020.md#c-3267b594985264c1) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-053952

```text
(config)# ip rsvp signalling hello graceful-restart dscp <number:0..63> <cr>
```

Handler ` RVA 0x10075E80 `；selector ` 4 `；EOL ` RVA 0x34A4B4C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Hello Messages DSCP value。

[条件 C-849db98cba445cc8](../../evidence/conditions-sets-051.md#c-849db98cba445cc8) · [参数 P-7bae1d155e32a087](../../evidence/parameters-sets-010.md#p-7bae1d155e32a087) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-046651

```text
(config)# ip rsvp signalling hello graceful-restart help-neighbor <cr>
```

Handler ` RVA 0x10075310 `；selector ` 0 `；EOL ` RVA 0x34A4BEF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-281c7465882f84dd](../../evidence/conditions-sets-016.md#c-281c7465882f84dd) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-057692

```text
(config)# ip rsvp signalling hello graceful-restart refresh interval <number:1000..30000> <cr>
```

Handler ` RVA 0x10075E80 `；selector ` 1 `；EOL ` RVA 0x34A4AE60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Hello interval in msec。

[条件 C-16d85f08ee591eb2](../../evidence/conditions-sets-009.md#c-16d85f08ee591eb2) · [参数 P-79358e42b3201387](../../evidence/parameters-sets-009.md#p-79358e42b3201387) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-057726

```text
(config)# ip rsvp signalling hello graceful-restart refresh misses <number:4..10> <cr>
```

Handler ` RVA 0x10075E80 `；selector ` 2 `；EOL ` RVA 0x34A4B150 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of Hello misses for Graceful Restart。

[条件 C-e520adbaa9fdb992](../../evidence/conditions-sets-088.md#c-e520adbaa9fdb992) · [参数 P-264aa6f9f2dee236](../../evidence/parameters-sets-003.md#p-264aa6f9f2dee236) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-057774

```text
(config)# ip rsvp signalling hello graceful-restart send recovery-time <number:0..3600000> <cr>
```

Handler ` RVA 0x100760E0 `；selector ` 0 `；EOL ` RVA 0x34A4B880 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number `  recovery-time in msec。

[条件 C-3775b4425a1d6dee](../../evidence/conditions-sets-022.md#c-3775b4425a1d6dee) · [参数 P-c0df5cf872b87004](../../evidence/parameters-sets-015.md#p-c0df5cf872b87004) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-057804

```text
(config)# ip rsvp signalling hello graceful-restart send restart-time <number:0..600000> <cr>
```

Handler ` RVA 0x10076040 `；selector ` 0 `；EOL ` RVA 0x34A4BB70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number `  restart-time in msec。

[条件 C-6e34966fe2451dc3](../../evidence/conditions-sets-043.md#c-6e34966fe2451dc3) · [参数 P-e5a3fb2d1f0eb8b5](../../evidence/parameters-sets-017.md#p-e5a3fb2d1f0eb8b5) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-053632

```text
(config)# ip rsvp signalling hello queue <number:1..200> <number:1..200> <cr>
```

Handler ` RVA 0x10076FA0 `；selector ` 0 `；EOL ` RVA 0x34A4A170 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` # of Hello msgs to process when RSVP wakes up；` unsigned_number ` # of RSVP msgs to process when RSVP wakes up。

[条件 C-3267b594985264c1](../../evidence/conditions-sets-020.md#c-3267b594985264c1) · [参数 P-10738022e58d9740](../../evidence/parameters-sets-002.md#p-10738022e58d9740) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-036773

```text
(config)# ip rsvp signalling hello statistics <cr>
```

Handler ` RVA 0x10074570 `；selector ` 0 `；EOL ` RVA 0x34A49B70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-132998733aa5ee20](../../evidence/conditions-sets-008.md#c-132998733aa5ee20) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-046244

```text
(config)# ip rsvp signalling hello timer <number:1..100> <cr>
```

Handler ` RVA 0x10077070 `；selector ` 0 `；EOL ` RVA 0x34A4A460 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` # of RSVP timers to process when RSVP wakes up。

[条件 C-3267b594985264c1](../../evidence/conditions-sets-020.md#c-3267b594985264c1) · [参数 P-2375db552f265c6f](../../evidence/parameters-sets-003.md#p-2375db552f265c6f) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-036634

```text
(config)# ip rsvp signalling initial-retransmit-delay <number:500..30000> <cr>
```

Handler ` RVA 0x100704D0 `；selector ` 0 `；EOL ` RVA 0x34A48AE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Initial retransmit delay (msecs)。

[条件 C-2d803e6ee8030579](../../evidence/conditions-sets-018.md#c-2d803e6ee8030579) · [参数 P-c69016d150f9bfc5](../../evidence/parameters-sets-015.md#p-c69016d150f9bfc5) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-036664

```text
(config)# ip rsvp signalling patherr state-removal <cr>
```

Handler ` RVA 0x10070AA0 `；selector ` 0 `；EOL ` RVA 0x34A48730 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a703f2b98c1aaa4a](../../evidence/conditions-sets-064.md#c-a703f2b98c1aaa4a) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-030307

```text
(config)# ip rsvp signalling rate-limit <cr>
```

Handler ` RVA 0x10070C50 `；selector ` 0 `；EOL ` RVA 0x34A48130 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-27818868760c1b1e](../../evidence/conditions-sets-016.md#c-27818868760c1b1e) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-046135

```text
(config)# ip rsvp signalling refresh interval <number:5000..2147483647> <cr>
```

Handler ` RVA 0x100559D0 `；selector ` 0 `；EOL ` RVA 0x34A494A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Refresh interval in milliseconds。

[条件 C-eb6a9edbee1658fc](../../evidence/conditions-sets-091.md#c-eb6a9edbee1658fc) · [参数 P-048436d4ef23618c](../../evidence/parameters-sets-001.md#p-048436d4ef23618c) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-046182

```text
(config)# ip rsvp signalling refresh misses <number:2..10> <cr>
```

Handler ` RVA 0x100701A0 `；selector ` 0 `；EOL ` RVA 0x34A497C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of allowed misses。

[条件 C-9498e4df1fce04fe](../../evidence/conditions-sets-057.md#c-9498e4df1fce04fe) · [参数 P-a3196917777eb446](../../evidence/parameters-sets-012.md#p-a3196917777eb446) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-036652

```text
(config)# ip rsvp signalling refresh reduction <cr>
```

Handler ` RVA 0x100705C0 `；selector ` 0 `；EOL ` RVA 0x34A48E60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e1fdee263dd9cba](../../evidence/conditions-sets-006.md#c-0e1fdee263dd9cba) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-053539

```text
(config)# ip rsvp signalling refresh reduction ack-delay <number:100..10000> <cr>
```

Handler ` RVA 0x100558C0 `；selector ` 0 `；EOL ` RVA 0x34A48F00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` ACK delay (msecs)。

[条件 C-d35e98364c4aa6dc](../../evidence/conditions-sets-081.md#c-d35e98364c4aa6dc) · [参数 P-9a7b998ec68016fb](../../evidence/parameters-sets-012.md#p-9a7b998ec68016fb) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-036346

```text
(config)# ip rsvp sso nbr <address> <cr>
```

Handler ` RVA 0x10077190 `；selector ` 0 `；EOL ` RVA 0x34A47678 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` must be router-id of neighbor。

[条件 C-608a725cf05f7ccd](../../evidence/conditions-sets-038.md#c-608a725cf05f7ccd) · [参数 P-efc8816b121035d0](../../evidence/parameters-sets-018.md#p-efc8816b121035d0) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-035806

```text
(config)# ip rsvp transport client <number:1..65535> <cr>
```

Handler ` RVA 0x1005D010 `；selector ` 0 `；EOL ` RVA 0x34A44D68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Client Identifier。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [参数 P-3bdd4f6af1b7ae23](../../evidence/parameters-sets-005.md#p-3bdd4f6af1b7ae23) · [状态效果 S-9ee6445178f48b01](../../evidence/state_effects-sets-034.md#s-9ee6445178f48b01)

### path-029600

```text
(config)# ip rsvp transport statistics <cr>
```

Handler ` RVA 0x1005CD90 `；selector ` 0 `；EOL ` RVA 0x34A44A50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [状态效果 S-9ee6445178f48b01](../../evidence/state_effects-sets-034.md#s-9ee6445178f48b01)

### path-029613

```text
(config)# ip rsvp udp hosts <cr>
```

Handler ` RVA 0x10056A50 `；selector ` 13 `；EOL ` RVA 0x34A44250 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [状态效果 S-4e23d0455d80053b](../../evidence/state_effects-sets-017.md#s-4e23d0455d80053b)

### path-035905

```text
(config)# ip rsvp udp neighbor <address> <cr>
```

Handler ` RVA 0x10056A50 `；selector ` 14 `；EOL ` RVA 0x34A44648 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` RSVP neighbor's IP address。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [参数 P-af5ad741a5f0a2e3](../../evidence/parameters-sets-013.md#p-af5ad741a5f0a2e3) · [状态效果 S-0050acffcd0fdb0a](../../evidence/state_effects-sets-001.md#s-0050acffcd0fdb0a)

### path-035309

```text
(config)# ip rtcp report interval <number:1..65535> <cr>
```

Handler ` RVA 0xFD20A20 `；selector ` 0 `；EOL ` RVA 0x348C8130 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` time in milliseconds。

[条件 C-342aa94e1269cce2](../../evidence/conditions-sets-020.md#c-342aa94e1269cce2) · [参数 P-e6559ea4c47925b7](../../evidence/parameters-sets-017.md#p-e6559ea4c47925b7) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026839

```text
(config)# ip rtp coalesce <cr>
```

Handler ` RVA 0xD1900E0 `；selector ` 0 `；EOL ` RVA 0x33DACCA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-254566f36f9fd550](../../evidence/conditions-sets-015.md#c-254566f36f9fd550) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029421

```text
(config)# ip sap cache-timeout <number:1..4294967295> <cr>
```

Handler ` RVA 0xF87E120 `；selector ` 2 `；EOL ` RVA 0x34756E80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timeout in minutes。

[条件 C-437a9ac840e4c799](../../evidence/conditions-sets-026.md#c-437a9ac840e4c799) · [参数 P-1fdf3acc188cb6a7](../../evidence/parameters-sets-003.md#p-1fdf3acc188cb6a7) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029784

```text
(config)# ip scp password <string> <cr>
```

Handler ` RVA 0x12345610 `；selector ` 3 `；EOL ` RVA 0x35826108 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` The cleartext scp Password 。

[条件 C-b0a67cf4aeeed148](../../evidence/conditions-sets-068.md#c-b0a67cf4aeeed148) · [参数 P-bc271de36d6b08a2](../../evidence/parameters-sets-014.md#p-bc271de36d6b08a2) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029476

```text
(config)# ip scp remote-username <string> <cr>
```

Handler ` RVA 0x12345610 `；selector ` 1 `；EOL ` RVA 0x35825AA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` This system's username for remote commands。

[条件 C-313fdaf60eeae8b1](../../evidence/conditions-sets-019.md#c-313fdaf60eeae8b1) · [参数 P-8cd6ad52482d2e8a](../../evidence/parameters-sets-011.md#p-8cd6ad52482d2e8a) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029387

```text
(config)# ip scp server enable <cr>
```

Handler ` RVA 0x12345610 `；selector ` 0 `；EOL ` RVA 0x35825750 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029531

```text
(config)# ip scp username <string> <cr>
```

Handler ` RVA 0x12345610 `；selector ` 2 `；EOL ` RVA 0x35825DE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Username。

[条件 C-c3d51c0d5abb0957](../../evidence/conditions-sets-076.md#c-c3d51c0d5abb0957) · [参数 P-aa273b3f9c0ec76f](../../evidence/parameters-sets-013.md#p-aa273b3f9c0ec76f) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-061239

```text
(config)# ip sdwan route vrf <string> <prefix:dynamic> <cr>
```

Handler ` RVA 0xCF2A810 `；selector ` 20 `；EOL ` RVA 0x33D33D60 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` VPN Routing/Forwarding instance name；` prefix_dynamic ` IP &lt;address&gt;/&lt;len&gt;。

[条件 C-7f815dbb995edd67](../../evidence/conditions-sets-049.md#c-7f815dbb995edd67) · [缺口 G-b4ffecd52b1bfda0](../../evidence/gaps-sets-006.md#g-b4ffecd52b1bfda0) · [参数 P-0c0055c1716ec9ea](../../evidence/parameters-sets-001.md#p-0c0055c1716ec9ea) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-062910

```text
(config)# ip sdwan route vrf <string> <prefix:dynamic> tunnel active <interface> <cr>
```

Handler ` RVA 0xCF2A810 `；selector ` 20 `；EOL ` RVA 0x33D33958 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` VPN Routing/Forwarding instance name；` prefix_dynamic ` IP &lt;address&gt;/&lt;len&gt;。

[条件 C-b088a579fdd667c7](../../evidence/conditions-sets-068.md#c-b088a579fdd667c7) · [缺口 G-cf029decf4e93743](../../evidence/gaps-sets-007.md#g-cf029decf4e93743) · [参数 P-0057f3617dec4a51](../../evidence/parameters-sets-001.md#p-0057f3617dec4a51) · [状态效果 S-96746b25c388dbd2](../../evidence/state_effects-sets-032.md#s-96746b25c388dbd2)

### path-044467

```text
(config)# ip security eso-info <number:0..255> <number:1..16> <number:0..1> <cr>
```

Handler ` RVA 0xCF2A810 `；selector ` 4 `；EOL ` RVA 0x33D34A90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` NLESO source；` unsigned_number ` Max # of compartment bytes；` unsigned_number ` default bit value。

[条件 C-081308c963ed298e](../../evidence/conditions-sets-004.md#c-081308c963ed298e) · [参数 P-657dc9efd4bd71dc](../../evidence/parameters-sets-008.md#p-657dc9efd4bd71dc) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029732

```text
(config)# ip sftp password <string> <cr>
```

Handler ` RVA 0x1234BA50 `；selector ` 1 `；EOL ` RVA 0x358269C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` The cleartext sftp Password 。

[条件 C-dd2793114b2cb1a1](../../evidence/conditions-sets-085.md#c-dd2793114b2cb1a1) · [参数 P-aeb52a3fdda5be45](../../evidence/parameters-sets-013.md#p-aeb52a3fdda5be45) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029475

```text
(config)# ip sftp username <string> <cr>
```

Handler ` RVA 0x1234BA50 `；selector ` 0 `；EOL ` RVA 0x358266A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Username。

[条件 C-2d60650bff503b12](../../evidence/conditions-sets-018.md#c-2d60650bff503b12) · [参数 P-e774c24a8e2d5f3d](../../evidence/parameters-sets-017.md#p-e774c24a8e2d5f3d) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060412

```text
(config)# ip sla <number:1..2147483647> <cr>
```

Handler ` RVA 0x102D26B0 `；selector ` 0 `；EOL ` RVA 0x34A94858 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Entry Number。

[条件 C-9325c86ad84f9918](../../evidence/conditions-sets-057.md#c-9325c86ad84f9918) · [缺口 G-3e2495d137ec3302](../../evidence/gaps-sets-003.md#g-3e2495d137ec3302) · [参数 P-cdb2c49481e10e98](../../evidence/parameters-sets-016.md#p-cdb2c49481e10e98) · [状态效果 S-e9ed88953d41a6b9](../../evidence/state_effects-sets-049.md#s-e9ed88953d41a6b9)

### path-060626

```text
(config)# ip sla enable reaction-alerts <cr>
```

Handler ` RVA 0x10275660 `；selector ` 1 `；EOL ` RVA 0x34A88DC8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [缺口 G-3e2495d137ec3302](../../evidence/gaps-sets-003.md#g-3e2495d137ec3302) · [状态效果 S-e9ed88953d41a6b9](../../evidence/state_effects-sets-049.md#s-e9ed88953d41a6b9)

### path-061332

```text
(config)# ip sla endpoint-list type ipv6 <string> <cr>
```

Handler ` RVA 0x10257DC0 `；selector ` 0 `；EOL ` RVA 0x34A9C300 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Endpoint list name。

[条件 C-62c251b8f7ccc957](../../evidence/conditions-sets-038.md#c-62c251b8f7ccc957) · [缺口 G-3e2495d137ec3302](../../evidence/gaps-sets-003.md#g-3e2495d137ec3302) · [参数 P-dac9ea505b1212dd](../../evidence/parameters-sets-016.md#p-dac9ea505b1212dd) · [状态效果 S-048b4c3093fe2d99](../../evidence/state_effects-sets-001.md#s-048b4c3093fe2d99)

### path-060632

```text
(config)# ip sla ethernet-monitor <number:1..2147483647> <cr>
```

Handler ` RVA 0x103AF800 `；selector ` 0 `；EOL ` RVA 0x34B04A78 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Entry Number。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [缺口 G-3e2495d137ec3302](../../evidence/gaps-sets-003.md#g-3e2495d137ec3302) · [参数 P-5d8c9d5649e11e7f](../../evidence/parameters-sets-007.md#p-5d8c9d5649e11e7f) · [状态效果 S-e9ed88953d41a6b9](../../evidence/state_effects-sets-049.md#s-e9ed88953d41a6b9)

### path-061945

```text
(config)# ip sla ethernet-monitor reaction-configuration <number:1..2147483647> react rtt <cr>
```

Handler ` RVA 0x103AE860 `；selector ` 0 `；EOL ` RVA 0x34B04F40 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Entry number。

[条件 C-f23cd97b9f1336f8](../../evidence/conditions-sets-094.md#c-f23cd97b9f1336f8) · [缺口 G-3e2495d137ec3302](../../evidence/gaps-sets-003.md#g-3e2495d137ec3302) · [参数 P-08c44512949d15c0](../../evidence/parameters-sets-001.md#p-08c44512949d15c0) · [状态效果 S-f7fd85e21f485dc9](../../evidence/state_effects-sets-052.md#s-f7fd85e21f485dc9)

### path-060881

```text
(config)# ip sla ethernet-monitor schedule <number:1..2147483647> <cr>
```

Handler ` RVA 0x103AEC10 `；selector ` 0 `；EOL ` RVA 0x34B063F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Entry Number。

[条件 C-799bfa2dbd06819f](../../evidence/conditions-sets-047.md#c-799bfa2dbd06819f) · [缺口 G-3e2495d137ec3302](../../evidence/gaps-sets-003.md#g-3e2495d137ec3302) · [参数 P-704076ddd9c018f2](../../evidence/parameters-sets-009.md#p-704076ddd9c018f2) · [状态效果 S-e9ed88953d41a6b9](../../evidence/state_effects-sets-049.md#s-e9ed88953d41a6b9)

### path-060411

```text
(config)# ip sla key-chain <cr>
```

Handler ` RVA 0x101DA8C0 `；selector ` 0 `；EOL ` RVA 0x34A6E498 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8bb1a6ad0c93a7ac](../../evidence/conditions-sets-054.md#c-8bb1a6ad0c93a7ac) · [缺口 G-3e2495d137ec3302](../../evidence/gaps-sets-003.md#g-3e2495d137ec3302) · [状态效果 S-e9ed88953d41a6b9](../../evidence/state_effects-sets-049.md#s-e9ed88953d41a6b9)

### path-060625

```text
(config)# ip sla logging traps <cr>
```

Handler ` RVA 0x10286E30 `；selector ` 0 `；EOL ` RVA 0x34A8D618 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [缺口 G-3e2495d137ec3302](../../evidence/gaps-sets-003.md#g-3e2495d137ec3302) · [状态效果 S-e9ed88953d41a6b9](../../evidence/state_effects-sets-049.md#s-e9ed88953d41a6b9)

### path-060417

```text
(config)# ip sla low-memory <cr>
```

Handler ` RVA 0x102D14A0 `；selector ` 0 `；EOL ` RVA 0x34A95130 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1851845e7b6aac89](../../evidence/conditions-sets-009.md#c-1851845e7b6aac89) · [缺口 G-3e2495d137ec3302](../../evidence/gaps-sets-003.md#g-3e2495d137ec3302) · [状态效果 S-e9ed88953d41a6b9](../../evidence/state_effects-sets-049.md#s-e9ed88953d41a6b9)

### path-060861

```text
(config)# ip sla periodic hostname resolution <cr>
```

Handler ` RVA 0x102D1E10 `；selector ` 0 `；EOL ` RVA 0x34A9C6E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [缺口 G-3e2495d137ec3302](../../evidence/gaps-sets-003.md#g-3e2495d137ec3302) · [状态效果 S-e9ed88953d41a6b9](../../evidence/state_effects-sets-049.md#s-e9ed88953d41a6b9)

### path-062826

```text
(config)# ip sla reaction-configuration <number:1..2147483647> react <?option@555589fe0ac8> <cr>
```

Handler ` RVA 0x10286170 `；selector ` 0 `；EOL ` RVA 0x34A8CC30 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Entry number。

[条件 C-f679bb70e247326a](../../evidence/conditions-sets-095.md#c-f679bb70e247326a) · [缺口 G-a7aa306fe7283848](../../evidence/gaps-sets-006.md#g-a7aa306fe7283848) · [参数 P-9d3081ac457cd2a8](../../evidence/parameters-sets-012.md#p-9d3081ac457cd2a8) · [状态效果 S-e9ed88953d41a6b9](../../evidence/state_effects-sets-049.md#s-e9ed88953d41a6b9)

### path-060865

```text
(config)# ip sla reaction-trigger <number:1..2147483647> <number:1..2147483647> <cr>
```

Handler ` RVA 0x10286B40 `；selector ` 0 `；EOL ` RVA 0x34A8C720 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Entry number；` unsigned_number ` Target entry number。

[条件 C-23b7f1838bbc658d](../../evidence/conditions-sets-014.md#c-23b7f1838bbc658d) · [缺口 G-3e2495d137ec3302](../../evidence/gaps-sets-003.md#g-3e2495d137ec3302) · [参数 P-2e5c879e7443d9e7](../../evidence/parameters-sets-004.md#p-2e5c879e7443d9e7) · [状态效果 S-e9ed88953d41a6b9](../../evidence/state_effects-sets-049.md#s-e9ed88953d41a6b9)

### path-060413

```text
(config)# ip sla reset <cr>
```

Handler ` RVA 0x102D1600 `；selector ` 0 `；EOL ` RVA 0x34A94DC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [缺口 G-3e2495d137ec3302](../../evidence/gaps-sets-003.md#g-3e2495d137ec3302) · [状态效果 S-e9ed88953d41a6b9](../../evidence/state_effects-sets-049.md#s-e9ed88953d41a6b9)

### path-060421

```text
(config)# ip sla responder <cr>
```

Handler ` RVA 0x101FB110 `；selector ` 1 `；EOL ` RVA 0x34A70FB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [缺口 G-3e2495d137ec3302](../../evidence/gaps-sets-003.md#g-3e2495d137ec3302) · [状态效果 S-e9ed88953d41a6b9](../../evidence/state_effects-sets-049.md#s-e9ed88953d41a6b9)

### path-060888

```text
(config)# ip sla responder auto-register <string> <cr>
```

Handler ` RVA 0x101FB110 `；selector ` 4 `；EOL ` RVA 0x34A71110 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Hub IP Address or HostName。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [缺口 G-3e2495d137ec3302](../../evidence/gaps-sets-003.md#g-3e2495d137ec3302) · [参数 P-5dd20f1432da3b69](../../evidence/parameters-sets-007.md#p-5dd20f1432da3b69) · [状态效果 S-e9ed88953d41a6b9](../../evidence/state_effects-sets-049.md#s-e9ed88953d41a6b9)

### path-060637

```text
(config)# ip sla responder twamp <cr>
```

Handler ` RVA 0x10237A10 `；selector ` 21 `；EOL ` RVA 0x34A761B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [缺口 G-3e2495d137ec3302](../../evidence/gaps-sets-003.md#g-3e2495d137ec3302) · [状态效果 S-e9ed88953d41a6b9](../../evidence/state_effects-sets-049.md#s-e9ed88953d41a6b9)

### path-061360

```text
(config)# ip sla responder twamp-light test-session <number:1..100> <cr>
```

Handler ` RVA 0x10239920 `；selector ` 634 `；EOL ` RVA 0x34A78160 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Session Identifier。

[条件 C-8192d035e9f92ef3](../../evidence/conditions-sets-050.md#c-8192d035e9f92ef3) · [缺口 G-3e2495d137ec3302](../../evidence/gaps-sets-003.md#g-3e2495d137ec3302) · [参数 P-83bca08954604e4b](../../evidence/parameters-sets-010.md#p-83bca08954604e4b) · [状态效果 S-e9ed88953d41a6b9](../../evidence/state_effects-sets-049.md#s-e9ed88953d41a6b9)

### path-061358

```text
(config)# ip sla responder twamp-light test-session reset <cr>
```

Handler ` RVA 0x1023AF50 `；selector ` 0 `；EOL ` RVA 0x34A78A78 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [缺口 G-3e2495d137ec3302](../../evidence/gaps-sets-003.md#g-3e2495d137ec3302) · [状态效果 S-e9ed88953d41a6b9](../../evidence/state_effects-sets-049.md#s-e9ed88953d41a6b9)

### path-061943

```text
(config)# ip sla responder twamp-light test-session restart <number:1..100> <cr>
```

Handler ` RVA 0x1023B060 `；selector ` 0 `；EOL ` RVA 0x34A78D98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Session Identifier。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [缺口 G-3e2495d137ec3302](../../evidence/gaps-sets-003.md#g-3e2495d137ec3302) · [参数 P-80342afcefa23b40](../../evidence/parameters-sets-010.md#p-80342afcefa23b40) · [状态效果 S-e9ed88953d41a6b9](../../evidence/state_effects-sets-049.md#s-e9ed88953d41a6b9)

### path-062303

```text
(config)# ip sla responder udp-echo ipaddress <string> port <number:1..65535> <cr>
```

Handler ` RVA 0x101FB110 `；selector ` 3 `；EOL ` RVA 0x34A70450 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` IP Address or IP HostName；` unsigned_number ` Port Number(Recommended ports greater than 1023)。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [缺口 G-3e2495d137ec3302](../../evidence/gaps-sets-003.md#g-3e2495d137ec3302) · [参数 P-132672fee419d236](../../evidence/parameters-sets-002.md#p-132672fee419d236) · [状态效果 S-efe0c4ea7a6f0bb2](../../evidence/state_effects-sets-051.md#s-efe0c4ea7a6f0bb2)

### path-062606

```text
(config)# ip sla responder udp-echo ipaddress <string> port <number:1..65535> vrf <string> <cr>
```

Handler ` RVA 0x101FB110 `；selector ` 6 `；EOL ` RVA 0x34A70490 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` IP Address or IP HostName；` unsigned_number ` Port Number(Recommended ports greater than 1023)；` string ` VPN Routing/Forwarding instance name。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [缺口 G-3e2495d137ec3302](../../evidence/gaps-sets-003.md#g-3e2495d137ec3302) · [参数 P-f50232040faf185b](../../evidence/parameters-sets-018.md#p-f50232040faf185b) · [状态效果 S-efe0c4ea7a6f0bb2](../../evidence/state_effects-sets-051.md#s-efe0c4ea7a6f0bb2)

### path-061355

```text
(config)# ip sla responder udp-echo port <number:1..65535> <cr>
```

Handler ` RVA 0x101FB110 `；selector ` 2 `；EOL ` RVA 0x34A70A18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Port Number (Recommended ports greater than 1023)。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [缺口 G-3e2495d137ec3302](../../evidence/gaps-sets-003.md#g-3e2495d137ec3302) · [参数 P-1574aa9f3b470456](../../evidence/parameters-sets-002.md#p-1574aa9f3b470456) · [状态效果 S-efe0c4ea7a6f0bb2](../../evidence/state_effects-sets-051.md#s-efe0c4ea7a6f0bb2)

### path-062298

```text
(config)# ip sla responder udp-echo port <number:1..65535> vrf <string> <cr>
```

Handler ` RVA 0x101FB110 `；selector ` 5 `；EOL ` RVA 0x34A70A58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Port Number (Recommended ports greater than 1023)；` string ` VPN Routing/Forwarding instance name。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [缺口 G-3e2495d137ec3302](../../evidence/gaps-sets-003.md#g-3e2495d137ec3302) · [参数 P-2b85127d34312d21](../../evidence/parameters-sets-004.md#p-2b85127d34312d21) · [状态效果 S-efe0c4ea7a6f0bb2](../../evidence/state_effects-sets-051.md#s-efe0c4ea7a6f0bb2)

### path-060628

```text
(config)# ip sla restart <number:1..2147483647> <cr>
```

Handler ` RVA 0x102D12E0 `；selector ` 0 `；EOL ` RVA 0x34A95458 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Entry Number。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [缺口 G-3e2495d137ec3302](../../evidence/gaps-sets-003.md#g-3e2495d137ec3302) · [参数 P-aa0e8c5b1f49c6c3](../../evidence/parameters-sets-013.md#p-aa0e8c5b1f49c6c3) · [状态效果 S-e9ed88953d41a6b9](../../evidence/state_effects-sets-049.md#s-e9ed88953d41a6b9)

### path-060634

```text
(config)# ip sla schedule <number:1..2147483647> <cr>
```

Handler ` RVA 0x1028A940 `；selector ` 0 `；EOL ` RVA 0x34A8FED0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Entry number。

[条件 C-2df5e6d4ac1d6e8b](../../evidence/conditions-sets-018.md#c-2df5e6d4ac1d6e8b) · [缺口 G-3e2495d137ec3302](../../evidence/gaps-sets-003.md#g-3e2495d137ec3302) · [参数 P-1d4efa0501e6cbcb](../../evidence/parameters-sets-003.md#p-1d4efa0501e6cbcb) · [状态效果 S-e9ed88953d41a6b9](../../evidence/state_effects-sets-049.md#s-e9ed88953d41a6b9)

### path-060635

```text
(config)# ip sla schedule <number:1..2147483647> <cr>
```

Handler ` RVA 0x1028D530 `；selector ` 0 `；EOL ` RVA 0x34A90150 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Entry number。

[条件 C-edf52884cea21d8c](../../evidence/conditions-sets-092.md#c-edf52884cea21d8c) · [缺口 G-3e2495d137ec3302](../../evidence/gaps-sets-003.md#g-3e2495d137ec3302) · [参数 P-1d4efa0501e6cbcb](../../evidence/parameters-sets-003.md#p-1d4efa0501e6cbcb) · [状态效果 S-e9ed88953d41a6b9](../../evidence/state_effects-sets-049.md#s-e9ed88953d41a6b9)

### path-060638

```text
(config)# ip sla server twamp <cr>
```

Handler ` RVA 0x1021E1B0 `；selector ` 0 `；EOL ` RVA 0x34A73BA0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [缺口 G-3e2495d137ec3302](../../evidence/gaps-sets-003.md#g-3e2495d137ec3302) · [状态效果 S-e9ed88953d41a6b9](../../evidence/state_effects-sets-049.md#s-e9ed88953d41a6b9)

### path-060872

```text
(config)# ip sla snmp extend tag <cr>
```

Handler ` RVA 0x102D1230 `；selector ` 0 `；EOL ` RVA 0x34A95760 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [缺口 G-3e2495d137ec3302](../../evidence/gaps-sets-003.md#g-3e2495d137ec3302) · [状态效果 S-e9ed88953d41a6b9](../../evidence/state_effects-sets-049.md#s-e9ed88953d41a6b9)

### path-062721

```text
(config)# ip sla test http <cr>
```

Handler ` RVA 0x102E64D0 `；selector ` 0 `；EOL ` RVA 0x34A94B18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-cfa5a3ef67388163](../../evidence/conditions-sets-080.md#c-cfa5a3ef67388163) · [缺口 G-88c5290fd88918f0](../../evidence/gaps-sets-005.md#g-88c5290fd88918f0) · [状态效果 S-e9ed88953d41a6b9](../../evidence/state_effects-sets-049.md#s-e9ed88953d41a6b9)

### path-062895

```text
(config)# ip source binding <address> bridge-domain <number:dynamic> <address> <interface> <cr>
```

Handler ` RVA 0x15FA6A40 `；selector ` 0 `；EOL ` RVA 0x35E7CAA8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` binding MAC address；` unsigned_number_dynamic ` binding bridge-domain number；` address ` binding IP address。

[条件 C-53a22bb3f6b0b3f3](../../evidence/conditions-sets-033.md#c-53a22bb3f6b0b3f3) · [缺口 G-c04c8c1c7b4f189a](../../evidence/gaps-sets-007.md#g-c04c8c1c7b4f189a) · [参数 P-3ad9c278ee984cc9](../../evidence/parameters-sets-005.md#p-3ad9c278ee984cc9) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025692

```text
(config)# ip source-route <cr>
```

Handler ` RVA 0xCF2A810 `；selector ` 2 `；EOL ` RVA 0x33D343E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-028975

```text
(config)# ip spd mode aggressive <cr>
```

Handler ` RVA 0xCF2A810 `；selector ` 13 `；EOL ` RVA 0x33D39218 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e9a27461afae804b](../../evidence/conditions-sets-090.md#c-e9a27461afae804b) · [状态效果 S-c2499ef71abadfa4](../../evidence/state_effects-sets-041.md#s-c2499ef71abadfa4)

### path-035106

```text
(config)# ip spd queue max-threshold <number:0..65535> <cr>
```

Handler ` RVA 0xCF2A810 `；selector ` 11 `；EOL ` RVA 0x33D396B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Max queue threshold。

[条件 C-05797315f6f89dda](../../evidence/conditions-sets-002.md#c-05797315f6f89dda) · [参数 P-428f52874f5e976a](../../evidence/parameters-sets-006.md#p-428f52874f5e976a) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-035160

```text
(config)# ip spd queue min-threshold <number:0..65535> <cr>
```

Handler ` RVA 0xCF2A810 `；selector ` 12 `；EOL ` RVA 0x33D399D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Min queue threshold。

[条件 C-5316228e75cb0dcf](../../evidence/conditions-sets-032.md#c-5316228e75cb0dcf) · [参数 P-94c6fe89623da5d0](../../evidence/parameters-sets-011.md#p-94c6fe89623da5d0) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025795

```text
(config)# ip ssh authentication-retries <number:0..5> <cr>
```

Handler ` RVA 0x123549D0 `；selector ` 24 `；EOL ` RVA 0x3581B8C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of authentication retries。

[条件 C-87a6a4c556fb493d](../../evidence/conditions-sets-052.md#c-87a6a4c556fb493d) · [参数 P-d3afe4469dcca8aa](../../evidence/parameters-sets-016.md#p-d3afe4469dcca8aa) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029834

```text
(config)# ip ssh break-string <string> <cr>
```

Handler ` RVA 0x123549D0 `；selector ` 31 `；EOL ` RVA 0x3581D158 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Break string。

[条件 C-bea8a05ac039d4ce](../../evidence/conditions-sets-074.md#c-bea8a05ac039d4ce) · [参数 P-ac823d493604f280](../../evidence/parameters-sets-013.md#p-ac823d493604f280) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026994

```text
(config)# ip ssh bulk-mode <cr>
```

Handler ` RVA 0x123549D0 `；selector ` 41 `；EOL ` RVA 0x3581B640 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d8d3518180d1dea6](../../evidence/conditions-sets-083.md#c-d8d3518180d1dea6) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-062831

```text
(config)# ip ssh client algorithm authentication <?option@55558ad77908> <cr>
```

Handler ` RVA 0x123549D0 `；selector ` 44 `；EOL ` RVA 0x35823688 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-095c5fc8c278822d](../../evidence/conditions-sets-004.md#c-095c5fc8c278822d) · [缺口 G-31e0cd485c82238e](../../evidence/gaps-sets-002.md#g-31e0cd485c82238e) · [状态效果 S-d5256a552e7d380c](../../evidence/state_effects-sets-045.md#s-d5256a552e7d380c)

### path-037035

```text
(config)# ip ssh client algorithm authentication <cr>
```

Handler ` RVA 0x123549D0 `；selector ` 44 `；EOL ` RVA 0x35823688 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-39d682e24dfa1fe1](../../evidence/conditions-sets-022.md#c-39d682e24dfa1fe1) · [状态效果 S-d3f2aa17655f96da](../../evidence/state_effects-sets-045.md#s-d3f2aa17655f96da)

### path-062828

```text
(config)# ip ssh client algorithm encryption <?option@55558ad74c58> <cr>
```

Handler ` RVA 0x123549D0 `；selector ` 47 `；EOL ` RVA 0x358209D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-df25676b9c78e20d](../../evidence/conditions-sets-086.md#c-df25676b9c78e20d) · [缺口 G-a1d89462b64de2fe](../../evidence/gaps-sets-006.md#g-a1d89462b64de2fe) · [状态效果 S-5f80d086f8c99b5e](../../evidence/state_effects-sets-021.md#s-5f80d086f8c99b5e)

### path-036840

```text
(config)# ip ssh client algorithm encryption <cr>
```

Handler ` RVA 0x123549D0 `；selector ` 47 `；EOL ` RVA 0x358209D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-24dba19a283443df](../../evidence/conditions-sets-014.md#c-24dba19a283443df) · [状态效果 S-d3f2aa17655f96da](../../evidence/state_effects-sets-045.md#s-d3f2aa17655f96da)

### path-062830

```text
(config)# ip ssh client algorithm hostkey <?option@55558ad76ac8> <cr>
```

Handler ` RVA 0x123549D0 `；selector ` 45 `；EOL ` RVA 0x35822848 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-99a31496434773e5](../../evidence/conditions-sets-059.md#c-99a31496434773e5) · [缺口 G-52f41cfb08a07d7d](../../evidence/gaps-sets-003.md#g-52f41cfb08a07d7d) · [状态效果 S-db98dbbca27d5158](../../evidence/state_effects-sets-046.md#s-db98dbbca27d5158)

### path-036992

```text
(config)# ip ssh client algorithm hostkey <cr>
```

Handler ` RVA 0x123549D0 `；selector ` 45 `；EOL ` RVA 0x35822848 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b6efd8e35f459113](../../evidence/conditions-sets-071.md#c-b6efd8e35f459113) · [状态效果 S-d3f2aa17655f96da](../../evidence/state_effects-sets-045.md#s-d3f2aa17655f96da)

### path-062829

```text
(config)# ip ssh client algorithm kex <?option@55558ad75cf0> <cr>
```

Handler ` RVA 0x123549D0 `；selector ` 49 `；EOL ` RVA 0x35821A70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8d156f90df706e72](../../evidence/conditions-sets-055.md#c-8d156f90df706e72) · [缺口 G-ea317ced958ec813](../../evidence/gaps-sets-008.md#g-ea317ced958ec813) · [状态效果 S-b5a4927549bdd853](../../evidence/state_effects-sets-038.md#s-b5a4927549bdd853)

### path-036876

```text
(config)# ip ssh client algorithm kex <cr>
```

Handler ` RVA 0x123549D0 `；selector ` 49 `；EOL ` RVA 0x35821A70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c7e9bf28089cfe6d](../../evidence/conditions-sets-077.md#c-c7e9bf28089cfe6d) · [状态效果 S-d3f2aa17655f96da](../../evidence/state_effects-sets-045.md#s-d3f2aa17655f96da)

### path-062827

```text
(config)# ip ssh client algorithm mac <?option@55558ad74350> <cr>
```

Handler ` RVA 0x123549D0 `；selector ` 48 `；EOL ` RVA 0x358200D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7361631489e48ea3](../../evidence/conditions-sets-045.md#c-7361631489e48ea3) · [缺口 G-e11242724903f8fc](../../evidence/gaps-sets-008.md#g-e11242724903f8fc) · [状态效果 S-7bfa0fa0c8316ca4](../../evidence/state_effects-sets-026.md#s-7bfa0fa0c8316ca4)

### path-036796

```text
(config)# ip ssh client algorithm mac <cr>
```

Handler ` RVA 0x123549D0 `；selector ` 48 `；EOL ` RVA 0x358200D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c7b5ee540274ca4f](../../evidence/conditions-sets-077.md#c-c7b5ee540274ca4f) · [状态效果 S-d3f2aa17655f96da](../../evidence/state_effects-sets-045.md#s-d3f2aa17655f96da)

### path-062832

```text
(config)# ip ssh client algorithm publickey <?option@55558ad77fc0> <cr>
```

Handler ` RVA 0x123549D0 `；selector ` 46 `；EOL ` RVA 0x35823D40 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5975c4940ef969fd](../../evidence/conditions-sets-035.md#c-5975c4940ef969fd) · [缺口 G-87b53ef97aabc8b3](../../evidence/gaps-sets-005.md#g-87b53ef97aabc8b3) · [状态效果 S-6f7d4b9a56f8ad0d](../../evidence/state_effects-sets-024.md#s-6f7d4b9a56f8ad0d)

### path-037077

```text
(config)# ip ssh client algorithm publickey <cr>
```

Handler ` RVA 0x123549D0 `；selector ` 46 `；EOL ` RVA 0x35823D40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-338ec9e93e6ebb8f](../../evidence/conditions-sets-020.md#c-338ec9e93e6ebb8f) · [状态效果 S-d3f2aa17655f96da](../../evidence/state_effects-sets-045.md#s-d3f2aa17655f96da)

### path-045800

```text
(config)# ip ssh dh min size 2048 <cr>
```

Handler ` RVA 0x123549D0 `；selector ` 33 `；EOL ` RVA 0x3581DB98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c84512d9a4b229f0](../../evidence/conditions-sets-077.md#c-c84512d9a4b229f0) · [状态效果 S-f146dd3fad894635](../../evidence/state_effects-sets-051.md#s-f146dd3fad894635)

### path-030075

```text
(config)# ip ssh dscp <number:0..63> <cr>
```

Handler ` RVA 0x123549D0 `；selector ` 35 `；EOL ` RVA 0x3581E260 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` ip dscp value (default value 0 )。

[条件 C-2e10628b5e9f286c](../../evidence/conditions-sets-018.md#c-2e10628b5e9f286c) · [参数 P-be726b6ee05107e2](../../evidence/parameters-sets-014.md#p-be726b6ee05107e2) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-036017

```text
(config)# ip ssh ec keypair-name <string> <cr>
```

Handler ` RVA 0x123549D0 `；selector ` 29 `；EOL ` RVA 0x3581CE00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` keypair name。

[条件 C-e70303247286c23d](../../evidence/conditions-sets-089.md#c-e70303247286c23d) · [参数 P-ec1acfa967d2436d](../../evidence/parameters-sets-018.md#p-ec1acfa967d2436d) · [状态效果 S-7ee05d45a3267f7a](../../evidence/state_effects-sets-027.md#s-7ee05d45a3267f7a)

### path-029848

```text
(config)# ip ssh logging events <cr>
```

Handler ` RVA 0x123549D0 `；selector ` 32 `；EOL ` RVA 0x3581D480 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026950

```text
(config)# ip ssh maxstartups <cr>
```

Handler ` RVA 0x123549D0 `；selector ` 26 `；EOL ` RVA 0x3581B2F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-035805

```text
(config)# ip ssh port <number:2000..10000> <number:2000..10000> <cr>
```

Handler ` RVA 0x123549D0 `；selector ` 27 `；EOL ` RVA 0x3581C258 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Starting Port number；` unsigned_number ` Ending Port number。

[条件 C-851c49a088247003](../../evidence/conditions-sets-051.md#c-851c49a088247003) · [参数 P-cc18b975222adec1](../../evidence/parameters-sets-015.md#p-cc18b975222adec1) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-030045

```text
(config)# ip ssh precedence <number:0..7> <cr>
```

Handler ` RVA 0x123549D0 `；selector ` 34 `；EOL ` RVA 0x3581DF10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` ip precedence value (default value 0 )。

[条件 C-bf30319b613f690a](../../evidence/conditions-sets-074.md#c-bf30319b613f690a) · [参数 P-124685b0af4b94b5](../../evidence/parameters-sets-002.md#p-124685b0af4b94b5) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027245

```text
(config)# ip ssh pubkey-chain <cr>
```

Handler ` RVA 0x123549D0 `；selector ` 36 `；EOL ` RVA 0x3581E868 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2dc309bf2cc2ec1a](../../evidence/conditions-sets-018.md#c-2dc309bf2cc2ec1a) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027274

```text
(config)# ip ssh rekey <cr>
```

Handler ` RVA 0x123549D0 `；selector ` 40 `；EOL ` RVA 0x3581EEF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-348bd27f2c340d76](../../evidence/conditions-sets-020.md#c-348bd27f2c340d76) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-036683

```text
(config)# ip ssh rekey time <number:10..1440> <cr>
```

Handler ` RVA 0x123549D0 `；selector ` 38 `；EOL ` RVA 0x3581EC40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Minutes。

[条件 C-867597b4d7432a90](../../evidence/conditions-sets-052.md#c-867597b4d7432a90) · [参数 P-f934929e51533893](../../evidence/parameters-sets-019.md#p-f934929e51533893) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-036734

```text
(config)# ip ssh rekey volume <number:100..4194303> <cr>
```

Handler ` RVA 0x123549D0 `；selector ` 39 `；EOL ` RVA 0x3581EF90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` kilobytes。

[条件 C-928bf2c14d6b336d](../../evidence/conditions-sets-057.md#c-928bf2c14d6b336d) · [参数 P-da0280d641b7fdf2](../../evidence/parameters-sets-016.md#p-da0280d641b7fdf2) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-035946

```text
(config)# ip ssh rsa keypair-name <string> <cr>
```

Handler ` RVA 0x123549D0 `；selector ` 29 `；EOL ` RVA 0x3581CA58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` keypair name。

[条件 C-3978df7b44e58129](../../evidence/conditions-sets-022.md#c-3978df7b44e58129) · [参数 P-12708baa653d122c](../../evidence/parameters-sets-002.md#p-12708baa653d122c) · [状态效果 S-8ce0327a07e81eac](../../evidence/state_effects-sets-030.md#s-8ce0327a07e81eac)

### path-036705

```text
(config)# ip ssh server authenticate user <cr>
```

Handler ` RVA 0x123549D0 `；selector ` 43 `；EOL ` RVA 0x3581F5C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6cecc6839acb574f](../../evidence/conditions-sets-042.md#c-6cecc6839acb574f) · [状态效果 S-4cb6e3498b8474de](../../evidence/state_effects-sets-017.md#s-4cb6e3498b8474de)

### path-036722

```text
(config)# ip ssh server certificate profile <cr>
```

Handler ` RVA 0x123549D0 `；selector ` 50 `；EOL ` RVA 0x3581FD38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2658a4b05d4fadb7](../../evidence/conditions-sets-015.md#c-2658a4b05d4fadb7) · [状态效果 S-4cb6e3498b8474de](../../evidence/state_effects-sets-017.md#s-4cb6e3498b8474de)

### path-053579

```text
(config)# ip ssh server peruser session limit <number:1..16> <cr>
```

Handler ` RVA 0x123549D0 `；selector ` 58 `；EOL ` RVA 0x3581F9F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of connections alowed per user。

[条件 C-a8b7a4106efbc12d](../../evidence/conditions-sets-065.md#c-a8b7a4106efbc12d) · [参数 P-3894474d6f077a30](../../evidence/parameters-sets-005.md#p-3894474d6f077a30) · [状态效果 S-4cb6e3498b8474de](../../evidence/state_effects-sets-017.md#s-4cb6e3498b8474de)

### path-060610

```text
(config)# ip ssh source-interface <interface> <cr>
```

Handler ` RVA 0x123549D0 `；selector ` 28 `；EOL ` RVA 0x3581C600 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-afb80d1380575e55](../../evidence/conditions-sets-068.md#c-afb80d1380575e55) · [缺口 G-48dc5592179fed2c](../../evidence/gaps-sets-003.md#g-48dc5592179fed2c) · [参数 P-467cf9cace4ab513](../../evidence/parameters-sets-006.md#p-467cf9cace4ab513) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027209

```text
(config)# ip ssh stricthostkeycheck <cr>
```

Handler ` RVA 0x123549D0 `；selector ` 37 `；EOL ` RVA 0x3581E550 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-45aac9d47ff2aa63](../../evidence/conditions-sets-027.md#c-45aac9d47ff2aa63) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025788

```text
(config)# ip ssh time-out <number:1..120> <cr>
```

Handler ` RVA 0x123549D0 `；selector ` 25 `；EOL ` RVA 0x3581B5A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` SSH time-out interval (secs)。

[条件 C-6c3426152a77d396](../../evidence/conditions-sets-042.md#c-6c3426152a77d396) · [参数 P-8802d8b523180cb9](../../evidence/parameters-sets-010.md#p-8802d8b523180cb9) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029872

```text
(config)# ip ssh version 2 <cr>
```

Handler ` RVA 0x123549D0 `；selector ` 30 `；EOL ` RVA 0x3581D7B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-45aac9d47ff2aa63](../../evidence/conditions-sets-027.md#c-45aac9d47ff2aa63) · [状态效果 S-0b431041d2b42e24](../../evidence/state_effects-sets-003.md#s-0b431041d2b42e24)

### path-025803

```text
(config)# ip ssh window-size <number:8192..131072> <cr>
```

Handler ` RVA 0x123549D0 `；selector ` 60 `；EOL ` RVA 0x3581BB68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` SSH window-size in bits for SSH Client performance improvement。

[条件 C-df0ec57a12eb93c6](../../evidence/conditions-sets-086.md#c-df0ec57a12eb93c6) · [参数 P-26644d29acefdec5](../../evidence/parameters-sets-003.md#p-26644d29acefdec5) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025721

```text
(config)# ip sticky-arp <cr>
```

Handler ` RVA 0xCF2A810 `；selector ` 15 `；EOL ` RVA 0x33D37B80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0489298d4adc773f](../../evidence/conditions-sets-002.md#c-0489298d4adc773f) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025686

```text
(config)# ip subnet-zero <cr>
```

Handler ` RVA 0xCF2A810 `；selector ` 3 `；EOL ` RVA 0x33D34138 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027167

```text
(config)# ip subscriber l2-roaming <cr>
```

Handler ` RVA 0x11A15630 `；selector ` 0 `；EOL ` RVA 0x355CB190 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-254566f36f9fd550](../../evidence/conditions-sets-015.md#c-254566f36f9fd550) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029918

```text
(config)# ip subscriber list <string> <cr>
```

Handler ` RVA 0x11A14BD0 `；selector ` 0 `；EOL ` RVA 0x355CAF10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` list name。

[条件 C-254566f36f9fd550](../../evidence/conditions-sets-015.md#c-254566f36f9fd550) · [参数 P-4713559ac7e67948](../../evidence/parameters-sets-006.md#p-4713559ac7e67948) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-036426

```text
(config)# ip subscriber timer clear-dangling <number:60..10800> <cr>
```

Handler ` RVA 0x11A3A780 `；selector ` 1 `；EOL ` RVA 0x355D04B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of seconds。

[条件 C-9073c1b565a2022b](../../evidence/conditions-sets-056.md#c-9073c1b565a2022b) · [参数 P-5b9800d30246e38c](../../evidence/parameters-sets-007.md#p-5b9800d30246e38c) · [状态效果 S-036ae08a8c1eb544](../../evidence/state_effects-sets-001.md#s-036ae08a8c1eb544)

### path-060575

```text
(config)# ip tacacs source-interface <interface> <cr>
```

Handler ` RVA 0xDB8ADD0 `；selector ` 15 `；EOL ` RVA 0x33FEF648 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e5ae2adf881fb960](../../evidence/conditions-sets-089.md#c-e5ae2adf881fb960) · [缺口 G-4f84b53cc1da7904](../../evidence/gaps-sets-003.md#g-4f84b53cc1da7904) · [参数 P-34d37fb9e67d3d64](../../evidence/parameters-sets-004.md#p-34d37fb9e67d3d64) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-044981

```text
(config)# ip tcp RST-count <number:2..20> RST-window <number:2000..60000> <cr>
```

Handler ` RVA 0xCDEDB20 `；selector ` 13 `；EOL ` RVA 0x33CFE058 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` RST throttle count number；` unsigned_number ` RST throttle window in msec。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [参数 P-66a729b68f6456ab](../../evidence/parameters-sets-008.md#p-66a729b68f6456ab) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026734

```text
(config)# ip tcp ack-tuning <cr>
```

Handler ` RVA 0xCDEDB20 `；selector ` 3 `；EOL ` RVA 0x33CFBFF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-35e263062ea996d3](../../evidence/conditions-sets-021.md#c-35e263062ea996d3) · [状态效果 S-4d444aa7b4bc0bb0](../../evidence/state_effects-sets-017.md#s-4d444aa7b4bc0bb0)

### path-029093

```text
(config)# ip tcp async-mobility server <cr>
```

Handler ` RVA 0xCDEDB20 `；selector ` 12 `；EOL ` RVA 0x33CFDC90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025724

```text
(config)# ip tcp chunk-size <number:0..65535> <cr>
```

Handler ` RVA 0xCDEDB20 `；selector ` 0 `；EOL ` RVA 0x33CFBF40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Chunk size。

[条件 C-40f591aa46458630](../../evidence/conditions-sets-025.md#c-40f591aa46458630) · [参数 P-dd2d6a8119e72055](../../evidence/parameters-sets-017.md#p-dd2d6a8119e72055) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026632

```text
(config)# ip tcp delayed-ack <cr>
```

Handler ` RVA 0xCDEDB20 `；selector ` 18 `；EOL ` RVA 0x33CFB9C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026572

```text
(config)# ip tcp ecn <cr>
```

Handler ` RVA 0xCDEDB20 `；selector ` 15 `；EOL ` RVA 0x33CFB1D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025745

```text
(config)# ip tcp finwait-time <number:0..4294967295> <cr>
```

Handler ` RVA 0xCDEDB20 `；selector ` 5 `；EOL ` RVA 0x33CFCDA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Seconds。

[条件 C-18a92df229f2995c](../../evidence/conditions-sets-010.md#c-18a92df229f2995c) · [参数 P-163a4c93135d86da](../../evidence/parameters-sets-002.md#p-163a4c93135d86da) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026747

```text
(config)# ip tcp keepalive interval <number:1..7200> <cr>
```

Handler ` RVA 0xCDEDB20 `；selector ` 9 `；EOL ` RVA 0x33CFC870 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` seconds。

[条件 C-aaa11d3017a97c42](../../evidence/conditions-sets-066.md#c-aaa11d3017a97c42) · [参数 P-02f48606d125883f](../../evidence/parameters-sets-001.md#p-02f48606d125883f) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026721

```text
(config)# ip tcp keepalive retries <number:1..10> <cr>
```

Handler ` RVA 0xCDEDB20 `；selector ` 10 `；EOL ` RVA 0x33CFC808 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` number。

[条件 C-88a472913a3e8f4a](../../evidence/conditions-sets-053.md#c-88a472913a3e8f4a) · [参数 P-7397807deceb700e](../../evidence/parameters-sets-009.md#p-7397807deceb700e) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025731

```text
(config)# ip tcp mss <number:0..10000> <cr>
```

Handler ` RVA 0xCDEDB20 `；selector ` 1 `；EOL ` RVA 0x33CFC2C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` MSS 。

[条件 C-b566a0acb785ef84](../../evidence/conditions-sets-070.md#c-b566a0acb785ef84) · [参数 P-1c92470a2ac5e626](../../evidence/parameters-sets-003.md#p-1c92470a2ac5e626) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026877

```text
(config)# ip tcp path-mtu-discovery <cr>
```

Handler ` RVA 0xCDEDB20 `；selector ` 8 `；EOL ` RVA 0x33CFD8F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d4378e85d8320aef](../../evidence/conditions-sets-082.md#c-d4378e85d8320aef) · [状态效果 S-b3f9edead831e403](../../evidence/state_effects-sets-038.md#s-b3f9edead831e403)

### path-025750

```text
(config)# ip tcp queuemax <number:5..50> <cr>
```

Handler ` RVA 0xCDEDB20 `；selector ` 6 `；EOL ` RVA 0x33CFD040 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of packets。

[条件 C-82082f2eede8016b](../../evidence/conditions-sets-050.md#c-82082f2eede8016b) · [参数 P-e4fa5431b1d495c0](../../evidence/parameters-sets-017.md#p-e4fa5431b1d495c0) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026589

```text
(config)# ip tcp selective-ack <cr>
```

Handler ` RVA 0xCDEDB20 `；selector ` 14 `；EOL ` RVA 0x33CFB478 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025754

```text
(config)# ip tcp synwait-time <number:5..300> <cr>
```

Handler ` RVA 0xCDEDB20 `；selector ` 7 `；EOL ` RVA 0x33CFD2E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Wait time。

[条件 C-c4c39e63ddceabda](../../evidence/conditions-sets-076.md#c-c4c39e63ddceabda) · [参数 P-aa58b68c3d7c6cb9](../../evidence/parameters-sets-013.md#p-aa58b68c3d7c6cb9) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026612

```text
(config)# ip tcp timestamp <cr>
```

Handler ` RVA 0xCDEDB20 `；selector ` 16 `；EOL ` RVA 0x33CFB720 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025738

```text
(config)# ip tcp window-size <number:0..1073741823> <cr>
```

Handler ` RVA 0xCDEDB20 `；selector ` 4 `；EOL ` RVA 0x33CFC830 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Window size。

[条件 C-d2244f4450655c84](../../evidence/conditions-sets-081.md#c-d2244f4450655c84) · [参数 P-3976995158266163](../../evidence/parameters-sets-005.md#p-3976995158266163) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026650

```text
(config)# ip tcp winupdate-opt <cr>
```

Handler ` RVA 0xCDEDB20 `；selector ` 2 `；EOL ` RVA 0x33CFBC70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-044784

```text
(config)# ip telnet comport disconnect delay <number:0..360> <cr>
```

Handler ` RVA 0xCDEDB20 `；selector ` 20 `；EOL ` RVA 0x33D00258 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` seconds to delay tcp close。

[条件 C-cc2fbfe472dd4de4](../../evidence/conditions-sets-079.md#c-cc2fbfe472dd4de4) · [参数 P-83ddbba661de7c25](../../evidence/parameters-sets-010.md#p-83ddbba661de7c25) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-028852

```text
(config)# ip telnet comport enable <cr>
```

Handler ` RVA 0xCDEDB20 `；selector ` 23 `；EOL ` RVA 0x33CFF7D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d23bbd13eaa99674](../../evidence/conditions-sets-081.md#c-d23bbd13eaa99674) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-044699

```text
(config)# ip telnet comport flow level <number:1..1023> <cr>
```

Handler ` RVA 0xCDEDB20 `；selector ` 21 `；EOL ` RVA 0x33CFFB40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` number of characters to buffer at device before sending RFC 2217 SUSPEND message。

[条件 C-c4290aeafb8bb8e9](../../evidence/conditions-sets-076.md#c-c4290aeafb8bb8e9) · [参数 P-cc473b9d4e870c67](../../evidence/parameters-sets-015.md#p-cc473b9d4e870c67) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-044740

```text
(config)# ip telnet comport receive window <number:1..131072> <cr>
```

Handler ` RVA 0xCDEDB20 `；selector ` 22 `；EOL ` RVA 0x33CFFEE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` max TCP receive window。

[条件 C-5df20e69d4cce507](../../evidence/conditions-sets-037.md#c-5df20e69d4cce507) · [参数 P-a0981f2ae8e9aacb](../../evidence/parameters-sets-012.md#p-a0981f2ae8e9aacb) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026718

```text
(config)# ip telnet disable <cr>
```

Handler ` RVA 0xCDEDB20 `；selector ` 46 `；EOL ` RVA 0x33D00560 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-92863ebbc5851c03](../../evidence/conditions-sets-057.md#c-92863ebbc5851c03) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-028720

```text
(config)# ip telnet hidden addresses <cr>
```

Handler ` RVA 0xCDEDB20 `；selector ` 42 `；EOL ` RVA 0x33CFF430 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e8254d5207707bd1](../../evidence/conditions-sets-090.md#c-e8254d5207707bd1) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-028683

```text
(config)# ip telnet hidden hostnames <cr>
```

Handler ` RVA 0xCDEDB20 `；selector ` 43 `；EOL ` RVA 0x33CFF188 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e8254d5207707bd1](../../evidence/conditions-sets-090.md#c-e8254d5207707bd1) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026648

```text
(config)# ip telnet quiet <cr>
```

Handler ` RVA 0xCDEDB20 `；selector ` 19 `；EOL ` RVA 0x33CFEE78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e8254d5207707bd1](../../evidence/conditions-sets-090.md#c-e8254d5207707bd1) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060546

```text
(config)# ip telnet source-interface <interface> <cr>
```

Handler ` RVA 0xCDEDB20 `；selector ` 11 `；EOL ` RVA 0x33CFE4B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-eaca7375f1eeba0c](../../evidence/conditions-sets-091.md#c-eaca7375f1eeba0c) · [缺口 G-b779e4dfecb863af](../../evidence/gaps-sets-006.md#g-b779e4dfecb863af) · [参数 P-6be7607284751a86](../../evidence/parameters-sets-009.md#p-6be7607284751a86) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026647

```text
(config)# ip telnet timeout retransmit <number:0..2147483> <cr>
```

Handler ` RVA 0xCDEDB20 `；selector ` 44 `；EOL ` RVA 0x33CFEB88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` retransmit timeout in seconds。

[条件 C-ebdf08e136d156df](../../evidence/conditions-sets-091.md#c-ebdf08e136d156df) · [参数 P-ebbaf140f3aa1368](../../evidence/parameters-sets-018.md#p-ebbaf140f3aa1368) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-028653

```text
(config)# ip telnet tos <number:0..255> <cr>
```

Handler ` RVA 0xCDEDB20 `；selector ` 17 `；EOL ` RVA 0x33CFE8C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` TOS value。

[条件 C-d7dee8c1aa911425](../../evidence/conditions-sets-083.md#c-d7dee8c1aa911425) · [参数 P-818ae7d1e2ef69c1](../../evidence/parameters-sets-010.md#p-818ae7d1e2ef69c1) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026717

```text
(config)# ip tftp arp-glean <cr>
```

Handler ` RVA 0xCFF2FD0 `；selector ` 1 `；EOL ` RVA 0x33D79000 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029022

```text
(config)# ip tftp blocksize <number:512..8192> <cr>
```

Handler ` RVA 0xCFF2FD0 `；selector ` 4 `；EOL ` RVA 0x33D79750 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` blocksize value。

[条件 C-8cd838c6315a7d98](../../evidence/conditions-sets-055.md#c-8cd838c6315a7d98) · [参数 P-1729b7b81a4ae116](../../evidence/parameters-sets-002.md#p-1729b7b81a4ae116) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060564

```text
(config)# ip tftp boot-interface <interface> <cr>
```

Handler ` RVA 0xCFF2FD0 `；selector ` 3 `；EOL ` RVA 0x33D79370 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-fb845ffe042cd503](../../evidence/conditions-sets-097.md#c-fb845ffe042cd503) · [缺口 G-12542e47abcf6304](../../evidence/gaps-sets-001.md#g-12542e47abcf6304) · [参数 P-e69d67a1d0668bdd](../../evidence/parameters-sets-017.md#p-e69d67a1d0668bdd) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026699

```text
(config)# ip tftp claim-netascii <cr>
```

Handler ` RVA 0xCFF2FD0 `；selector ` 0 `；EOL ` RVA 0x33D78D58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060556

```text
(config)# ip tftp source-interface <interface> <cr>
```

Handler ` RVA 0xCFF2FD0 `；selector ` 2 `；EOL ` RVA 0x33D78A18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8bf2eb2bc820932b](../../evidence/conditions-sets-054.md#c-8bf2eb2bc820932b) · [缺口 G-bbbdd041c95b6b5b](../../evidence/gaps-sets-007.md#g-bbbdd041c95b6b5b) · [参数 P-e770ddd24b923496](../../evidence/parameters-sets-017.md#p-e770ddd24b923496) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025836

```text
(config)# ip trigger-authentication <cr>
```

Handler ` RVA 0x10571410 `；selector ` 0 `；EOL ` RVA 0x34B59F80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-848efb24bfe59aac](../../evidence/conditions-sets-051.md#c-848efb24bfe59aac) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026780

```text
(config)# ip ttl decrement <cr>
```

Handler ` RVA 0xCF2A810 `；selector ` 17 `；EOL ` RVA 0x33D39D38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-582072addfb4f1ab](../../evidence/conditions-sets-035.md#c-582072addfb4f1ab) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-044980

```text
(config)# ip verify drop-rate compute interval <number:30..300> <cr>
```

Handler ` RVA 0xB624D70 `；selector ` 0 `；EOL ` RVA 0x337C8E38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` time between computations in seconds。

[条件 C-88ac316ee06a4345](../../evidence/conditions-sets-053.md#c-88ac316ee06a4345) · [参数 P-eecc572337319d5b](../../evidence/parameters-sets-018.md#p-eecc572337319d5b) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-045022

```text
(config)# ip verify drop-rate compute window <number:30..300> <cr>
```

Handler ` RVA 0xB624D70 `；selector ` 1 `；EOL ` RVA 0x337C9128 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` max time to accumulate drops in seconds。

[条件 C-01058899de6298ee](../../evidence/conditions-sets-001.md#c-01058899de6298ee) · [参数 P-32551641eb7730a6](../../evidence/parameters-sets-004.md#p-32551641eb7730a6) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-045020

```text
(config)# ip verify drop-rate notify hold-down <number:30..300> <cr>
```

Handler ` RVA 0xB624D70 `；selector ` 2 `；EOL ` RVA 0x337C9470 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` min time between notifications in seconds。

[条件 C-b1cd6d35361ecd73](../../evidence/conditions-sets-069.md#c-b1cd6d35361ecd73) · [参数 P-9202a3801feade7f](../../evidence/parameters-sets-011.md#p-9202a3801feade7f) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-052521

```text
(config)# ip visibility global flow monitor sdwan_flow_monitor input <cr>
```

Handler ` RVA 0xC670530 `；selector ` 0 `；EOL ` RVA 0x33ACE698 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [状态效果 S-18ab4260b751c191](../../evidence/state_effects-sets-006.md#s-18ab4260b751c191)

### path-025781

```text
(config)# ip vrf <cr>
```

Handler ` RVA 0xDC3DE20 `；selector ` 0 `；EOL ` RVA 0x34012D68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-253289dd4aa581ac](../../evidence/conditions-sets-014.md#c-253289dd4aa581ac) · [状态效果 S-83b53dccb2d9f9a4](../../evidence/state_effects-sets-028.md#s-83b53dccb2d9f9a4)

### path-060402

```text
(config)# ip vrf <string> <cr>
```

Handler ` RVA 0xDC3DE20 `；selector ` 0 `；EOL ` RVA 0x34012D68 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` VRF name。

[条件 C-125a5e8f68e5533f](../../evidence/conditions-sets-007.md#c-125a5e8f68e5533f) · [缺口 G-a81989785ab79e06](../../evidence/gaps-sets-006.md#g-a81989785ab79e06) · [参数 P-f15aab74a4ed5de5](../../evidence/parameters-sets-018.md#p-f15aab74a4ed5de5) · [状态效果 S-f4699c475f00c3a1](../../evidence/state_effects-sets-052.md#s-f4699c475f00c3a1)

### path-035704

```text
(config)# ip wccp check acl outbound <cr>
```

Handler ` RVA 0x10AD0260 `；selector ` 5 `；EOL ` RVA 0x34C971C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d53387ff584a565c](../../evidence/conditions-sets-082.md#c-d53387ff584a565c) · [状态效果 S-c7332a5186845080](../../evidence/state_effects-sets-042.md#s-c7332a5186845080)

### path-035651

```text
(config)# ip wccp check services all <cr>
```

Handler ` RVA 0x10AD0260 `；selector ` 6 `；EOL ` RVA 0x34C96E78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9cad58f6a22339a1](../../evidence/conditions-sets-061.md#c-9cad58f6a22339a1) · [状态效果 S-c7332a5186845080](../../evidence/state_effects-sets-042.md#s-c7332a5186845080)

### path-027013

```text
(config)# ip wccp outbound-acl-check <cr>
```

Handler ` RVA 0x10AD0260 `；selector ` 4 `；EOL ` RVA 0x34C97548 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-da353358833c7da0](../../evidence/conditions-sets-084.md#c-da353358833c7da0) · [状态效果 S-c7332a5186845080](../../evidence/state_effects-sets-042.md#s-c7332a5186845080)

### path-060605

```text
(config)# ip wccp source-interface <interface> <cr>
```

Handler ` RVA 0x10AD0260 `；selector ` 7 `；EOL ` RVA 0x34C979C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6e432c37f5331910](../../evidence/conditions-sets-043.md#c-6e432c37f5331910) · [缺口 G-5cfab0d831934578](../../evidence/gaps-sets-004.md#g-5cfab0d831934578) · [参数 P-97ddbc9a1bb51d96](../../evidence/parameters-sets-012.md#p-97ddbc9a1bb51d96) · [状态效果 S-c7332a5186845080](../../evidence/state_effects-sets-042.md#s-c7332a5186845080)

### path-026948

```text
(config)# ip wccp variable-timers <cr>
```

Handler ` RVA 0x10AD0260 `；selector ` 3 `；EOL ` RVA 0x34C96A70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ca12b5280892f8a2](../../evidence/conditions-sets-078.md#c-ca12b5280892f8a2) · [状态效果 S-c7332a5186845080](../../evidence/state_effects-sets-042.md#s-c7332a5186845080)

### path-029335

```text
(config)# ip wccp version <number:2..2> <cr>
```

Handler ` RVA 0x10AD0260 `；selector ` 2 `；EOL ` RVA 0x34C96740 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` WCCP protocol version。

[条件 C-35dca5d82b2b7a5d](../../evidence/conditions-sets-021.md#c-35dca5d82b2b7a5d) · [参数 P-934707403858ea74](../../evidence/parameters-sets-011.md#p-934707403858ea74) · [状态效果 S-c7332a5186845080](../../evidence/state_effects-sets-042.md#s-c7332a5186845080)

### path-027214

```text
(config)# ip wccp web-cache <cr>
```

Handler ` RVA 0x10AD0260 `；selector ` 0 `；EOL ` RVA 0x34C98AB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-067290a17d8f2a2a](../../evidence/conditions-sets-003.md#c-067290a17d8f2a2a) · [状态效果 S-ec6f2844efe492e9](../../evidence/state_effects-sets-050.md#s-ec6f2844efe492e9)

### path-060508

```text
(config)# ipc buffers max-free <number:dynamic> <cr>
```

Handler ` RVA 0xD3BC170 `；selector ` 1 `；EOL ` RVA 0x33E29378 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Number of buffers。

[条件 C-dbdcda02dcb32c74](../../evidence/conditions-sets-085.md#c-dbdcda02dcb32c74) · [缺口 G-b19877689f75df6b](../../evidence/gaps-sets-006.md#g-b19877689f75df6b) · [参数 P-989d7eb4f87bf62c](../../evidence/parameters-sets-012.md#p-989d7eb4f87bf62c) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060509

```text
(config)# ipc buffers min-free <number:dynamic> <cr>
```

Handler ` RVA 0xD3BC170 `；selector ` 0 `；EOL ` RVA 0x33E296C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Number of buffers。

[条件 C-6fe474197555d2ba](../../evidence/conditions-sets-043.md#c-6fe474197555d2ba) · [缺口 G-926beb9d07a20e2d](../../evidence/gaps-sets-005.md#g-926beb9d07a20e2d) · [参数 P-5f7546bbe2851312](../../evidence/parameters-sets-008.md#p-5f7546bbe2851312) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060511

```text
(config)# ipc buffers permanent <number:dynamic> <cr>
```

Handler ` RVA 0xD3BC170 `；selector ` 2 `；EOL ` RVA 0x33E299F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Number of buffers。

[条件 C-b8b1bdb6df310312](../../evidence/conditions-sets-071.md#c-b8b1bdb6df310312) · [缺口 G-6adbc0a8733b88e9](../../evidence/gaps-sets-004.md#g-6adbc0a8733b88e9) · [参数 P-d29006c573d7ef64](../../evidence/parameters-sets-016.md#p-d29006c573d7ef64) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060372

```text
(config)# ipc cache <number:dynamic> <cr>
```

Handler ` RVA 0xD3B9730 `；selector ` 0 `；EOL ` RVA 0x33E27D90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Cache size。

[条件 C-f24b5ddbab11979f](../../evidence/conditions-sets-094.md#c-f24b5ddbab11979f) · [缺口 G-5c7e1e4fe1d572e0](../../evidence/gaps-sets-004.md#g-5c7e1e4fe1d572e0) · [参数 P-4984ed2a37f04b5e](../../evidence/parameters-sets-006.md#p-4984ed2a37f04b5e) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-034038

```text
(config)# ipc header-cache permanent <number:1000..10000> <number:100..2000> <cr>
```

Handler ` RVA 0xD3B97D0 `；selector ` 0 `；EOL ` RVA 0x33E28F90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Max permanent cache size ；` unsigned_number ` Cache Low water mark for Dynamic growth 。

[条件 C-6d624619435be432](../../evidence/conditions-sets-042.md#c-6d624619435be432) · [参数 P-c19d96112f18e23f](../../evidence/parameters-sets-015.md#p-c19d96112f18e23f) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-034034

```text
(config)# ipc holdq threshold lower <number:10..2000> <cr>
```

Handler ` RVA 0xD3BBF00 `；selector ` 1 `；EOL ` RVA 0x33E287E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Threshold to start sending of IPC messages。

[条件 C-1f96ac763ad454db](../../evidence/conditions-sets-012.md#c-1f96ac763ad454db) · [参数 P-c243df89c092b759](../../evidence/parameters-sets-015.md#p-c243df89c092b759) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-034025

```text
(config)# ipc holdq threshold upper <number:40..4000> <cr>
```

Handler ` RVA 0xD3BBF00 `；selector ` 2 `；EOL ` RVA 0x33E284C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Threshold to stop sending of IPC messages。

[条件 C-f6d91bff878a00dc](../../evidence/conditions-sets-095.md#c-f6d91bff878a00dc) · [参数 P-dd300b923cab1060](../../evidence/parameters-sets-017.md#p-dd300b923cab1060) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026117

```text
(config)# ipc ru-action on <cr>
```

Handler ` RVA 0xD3FE7B0 `；selector ` 0 `；EOL ` RVA 0x33E3F410 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c232d66a65f05dad](../../evidence/conditions-sets-075.md#c-c232d66a65f05dad) · [状态效果 S-7cb8a7957537b68b](../../evidence/state_effects-sets-026.md#s-7cb8a7957537b68b)

### path-026159

```text
(config)# ipc zone default <cr>
```

Handler ` RVA 0xD3BA1B0 `；selector ` 0 `；EOL ` RVA 0x33E28BB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bd9e25b6c0380d7d](../../evidence/conditions-sets-073.md#c-bd9e25b6c0380d7d) · [状态效果 S-f4116bd53f6e9265](../../evidence/state_effects-sets-052.md#s-f4116bd53f6e9265)

### path-027211

```text
(config)# ipv6 access-list <string> <cr>
```

Handler ` RVA 0x12173E60 `；selector ` 2 `；EOL ` RVA 0x357AD4B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` User selected string identifying this access list。

[条件 C-4ca255b584894e31](../../evidence/conditions-sets-030.md#c-4ca255b584894e31) · [参数 P-3882fcb01116a85b](../../evidence/parameters-sets-005.md#p-3882fcb01116a85b) · [状态效果 S-7fe12bf24ab662a1](../../evidence/state_effects-sets-027.md#s-7fe12bf24ab662a1)

### path-030059

```text
(config)# ipv6 access-list fqdn <string> <cr>
```

Handler ` RVA 0x12173E60 `；selector ` 5 `；EOL ` RVA 0x357AD0D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Access-list name。

[条件 C-dd04f3b98f074a70](../../evidence/conditions-sets-085.md#c-dd04f3b98f074a70) · [参数 P-14bdade43088c73a](../../evidence/parameters-sets-002.md#p-14bdade43088c73a) · [状态效果 S-f52d381d6fd642e1](../../evidence/state_effects-sets-052.md#s-f52d381d6fd642e1)

### path-036480

```text
(config)# ipv6 access-list log-update threshold <number:0..2147483647> <cr>
```

Handler ` RVA 0x12172B00 `；selector ` 0 `；EOL ` RVA 0x357AF3B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Access list log-update threshold (number of hits)。

[条件 C-d38166a440eeeff8](../../evidence/conditions-sets-082.md#c-d38166a440eeeff8) · [参数 P-53e5c7f8d6b8f52c](../../evidence/parameters-sets-007.md#p-53e5c7f8d6b8f52c) · [状态效果 S-f003ccfcef42a54a](../../evidence/state_effects-sets-051.md#s-f003ccfcef42a54a)

### path-027180

```text
(config)# ipv6 access-list match-local-traffic <cr>
```

Handler ` RVA 0x121616D0 `；selector ` 0 `；EOL ` RVA 0x357AF028 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c1b7b1c57909dd9b](../../evidence/conditions-sets-075.md#c-c1b7b1c57909dd9b) · [状态效果 S-f003ccfcef42a54a](../../evidence/state_effects-sets-051.md#s-f003ccfcef42a54a)

### path-029993

```text
(config)# ipv6 access-list role-based <string> <cr>
```

Handler ` RVA 0x12173E60 `；selector ` 4 `；EOL ` RVA 0x357ACC98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Access-list name。

[条件 C-90b7c0da3363aae6](../../evidence/conditions-sets-056.md#c-90b7c0da3363aae6) · [参数 P-2666d018d9735b27](../../evidence/parameters-sets-003.md#p-2666d018d9735b27) · [状态效果 S-ef5a8b776594abde](../../evidence/state_effects-sets-051.md#s-ef5a8b776594abde)

### path-025773

```text
(config)# ipv6 address-validate <cr>
```

Handler ` RVA 0x12302BA0 `；selector ` 0 `；EOL ` RVA 0x357DFB40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029724

```text
(config)# ipv6 alias <address> <number:1..65535> <cr>
```

Handler ` RVA 0x12303CE0 `；selector ` 0 `；EOL ` RVA 0x357E0EB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IPV6 address to alias to a port；` unsigned_number ` IP port number。

[条件 C-6467d26d8d69f26a](../../evidence/conditions-sets-039.md#c-6467d26d8d69f26a) · [参数 P-1c961702e880d28b](../../evidence/parameters-sets-003.md#p-1c961702e880d28b) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025862

```text
(config)# ipv6 cef <cr>
```

Handler ` RVA 0xB67C690 `；selector ` 0 `；EOL ` RVA 0x337D77E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c1c2b243ffe0338a](../../evidence/conditions-sets-075.md#c-c1c2b243ffe0338a) · [状态效果 S-4f78efdb08cba9fb](../../evidence/state_effects-sets-017.md#s-4f78efdb08cba9fb)

### path-027267

```text
(config)# ipv6 cef accounting <cr>
```

Handler ` RVA 0xB3625A0 `；selector ` 0 `；EOL ` RVA 0x337D6E18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cfc529009bdae64a](../../evidence/conditions-sets-080.md#c-cfc529009bdae64a) · [状态效果 S-843813a7aaf72ba4](../../evidence/state_effects-sets-028.md#s-843813a7aaf72ba4)

### path-036660

```text
(config)# ipv6 cef load-sharing algorithm dpi <cr>
```

Handler ` RVA 0xB67C8D0 `；selector ` 0 `；EOL ` RVA 0x337D4610 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fc0932bd62f46397](../../evidence/conditions-sets-097.md#c-fc0932bd62f46397) · [状态效果 S-ac55b9e84239ba25](../../evidence/state_effects-sets-036.md#s-ac55b9e84239ba25)

### path-036361

```text
(config)# ipv6 cef load-sharing algorithm original <cr>
```

Handler ` RVA 0xB67C8D0 `；selector ` 0 `；EOL ` RVA 0x337D3F80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e0f8dc1c6eaa9094](../../evidence/conditions-sets-087.md#c-e0f8dc1c6eaa9094) · [状态效果 S-bf974f5ab10185c5](../../evidence/state_effects-sets-041.md#s-bf974f5ab10185c5)

### path-057385

```text
(config)# ipv6 cef load-sharing key-control dpi default outer-src-ip ignore-outer-port <cr>
```

Handler ` RVA 0xB67C9A0 `；selector ` 6 `；EOL ` RVA 0x337D4C70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6a6edf91ae37864a](../../evidence/conditions-sets-041.md#c-6a6edf91ae37864a) · [状态效果 S-0264ee6e4c4bc565](../../evidence/state_effects-sets-001.md#s-0264ee6e4c4bc565)

### path-060218

```text
(config)# ipv6 cef load-sharing key-control dpi l2vpn-mac ignore-outer-mac ignore-outer-vlan ignore-outer-ip ignore-outer-port ignore-inner-mac ignore-inner-vlan ignore-inner-ip ignore-inner-port <cr>
```

Handler ` RVA 0xB67C9A0 `；selector ` 5 `；EOL ` RVA 0x337D50B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7eb52d07f26e399a](../../evidence/conditions-sets-049.md#c-7eb52d07f26e399a) · [状态效果 S-2e1d502bb97770f6](../../evidence/state_effects-sets-010.md#s-2e1d502bb97770f6)

### path-059177

```text
(config)# ipv6 cef load-sharing key-control dpi tunnel-gre outer-src-ip ignore-inner-ip ignore-inner-port <cr>
```

Handler ` RVA 0xB67C9A0 `；selector ` 0 `；EOL ` RVA 0x337D5BF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1166eff80fb1d17c](../../evidence/conditions-sets-007.md#c-1166eff80fb1d17c) · [状态效果 S-39b627794545b664](../../evidence/state_effects-sets-013.md#s-39b627794545b664)

### path-059168

```text
(config)# ipv6 cef load-sharing key-control dpi tunnel-ipinip outer-src-ip ignore-inner-ip ignore-inner-port <cr>
```

Handler ` RVA 0xB67C9A0 `；selector ` 3 `；EOL ` RVA 0x337D5760 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c08f466c8f35a618](../../evidence/conditions-sets-074.md#c-c08f466c8f35a618) · [状态效果 S-784e26cbbef4d8d1](../../evidence/state_effects-sets-026.md#s-784e26cbbef4d8d1)

### path-053495

```text
(config)# ipv6 cef load-sharing key-control dpi tunnel-ipsec ignore-outer-ip <cr>
```

Handler ` RVA 0xB67C9A0 `；selector ` 2 `；EOL ` RVA 0x337D6080 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-060bd87cb6ac3934](../../evidence/conditions-sets-003.md#c-060bd87cb6ac3934) · [状态效果 S-88ee08f620021a41](../../evidence/state_effects-sets-029.md#s-88ee08f620021a41)

### path-059787

```text
(config)# ipv6 cef load-sharing key-control dpi tunnel-l2tp ignore-outer-ip ignore-outer-port ignore-inner-ip ignore-inner-port <cr>
```

Handler ` RVA 0xB67C9A0 `；selector ` 1 `；EOL ` RVA 0x337D6840 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3b99d27aaf66a41b](../../evidence/conditions-sets-023.md#c-3b99d27aaf66a41b) · [状态效果 S-8c0db35c184cd53d](../../evidence/state_effects-sets-030.md#s-8c0db35c184cd53d)

### path-059789

```text
(config)# ipv6 cef load-sharing key-control dpi tunnel-vxlan ignore-outer-ip ignore-outer-port ignore-inner-mac ignore-inner-vlan <cr>
```

Handler ` RVA 0xB67C9A0 `；selector ` 4 `；EOL ` RVA 0x337D63A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-880d0b05a53cb266](../../evidence/conditions-sets-053.md#c-880d0b05a53cb266) · [状态效果 S-198bd64af512f59c](../../evidence/state_effects-sets-006.md#s-198bd64af512f59c)

### path-035921

```text
(config)# ipv6 cef optimize neighbor resolution <cr>
```

Handler ` RVA 0xB60D5B0 `；selector ` 2 `；EOL ` RVA 0x337D7C38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-4f78efdb08cba9fb](../../evidence/state_effects-sets-017.md#s-4f78efdb08cba9fb)

### path-027194

```text
(config)# ipv6 cef traffic-statistics <cr>
```

Handler ` RVA 0xB362360 `；selector ` 0 `；EOL ` RVA 0x337D74C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-89edfde5a6936d90](../../evidence/conditions-sets-053.md#c-89edfde5a6936d90) · [状态效果 S-9564c6914104e513](../../evidence/state_effects-sets-032.md#s-9564c6914104e513)

### path-025775

```text
(config)# ipv6 deny-echo-reply <cr>
```

Handler ` RVA 0x12306030 `；selector ` 0 `；EOL ` RVA 0x357E7720 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029467

```text
(config)# ipv6 destination-guard policy <string> <cr>
```

Handler ` RVA 0x136B0870 `；selector ` 0 `；EOL ` RVA 0x35C023B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of the destination guard policy。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-1689858caa4e8740](../../evidence/parameters-sets-002.md#p-1689858caa4e8740) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-035790

```text
(config)# ipv6 dhcp binding track ppp <cr>
```

Handler ` RVA 0x121D1F80 `；selector ` 0 `；EOL ` RVA 0x357CC468 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029717

```text
(config)# ipv6 dhcp database <string> <cr>
```

Handler ` RVA 0x121D1720 `；selector ` 0 `；EOL ` RVA 0x357CAFF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Uniform Resource Locator (URL)。

[条件 C-36b628c0349e2c86](../../evidence/conditions-sets-021.md#c-36b628c0349e2c86) · [参数 P-c8fc7defa064b7c9](../../evidence/parameters-sets-015.md#p-c8fc7defa064b7c9) · [状态效果 S-db6c76a6a8a7fa39](../../evidence/state_effects-sets-046.md#s-db6c76a6a8a7fa39)

### path-027031

```text
(config)# ipv6 dhcp iana-route-add <cr>
```

Handler ` RVA 0x121D1B80 `；selector ` 1 `；EOL ` RVA 0x357CC118 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027006

```text
(config)# ipv6 dhcp iapd-route-add <cr>
```

Handler ` RVA 0x121D1B80 `；selector ` 0 `；EOL ` RVA 0x357CBE70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-052907

```text
(config)# ipv6 dhcp monitor statistics start sample-size <number:0..4294967295> <cr>
```

Handler ` RVA 0x121C7630 `；selector ` 1 `；EOL ` RVA 0x357CB930 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of packets。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-e24016597d523192](../../evidence/parameters-sets-017.md#p-e24016597d523192) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-035739

```text
(config)# ipv6 dhcp monitor statistics stop <cr>
```

Handler ` RVA 0x121C7630 `；selector ` 0 `；EOL ` RVA 0x357CBBC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029665

```text
(config)# ipv6 dhcp ping packets <cr>
```

Handler ` RVA 0x121D1A90 `；selector ` 0 `；EOL ` RVA 0x357CB510 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4b08f896d2ead5d1](../../evidence/conditions-sets-029.md#c-4b08f896d2ead5d1) · [状态效果 S-aaa89e78622a97ab](../../evidence/state_effects-sets-036.md#s-aaa89e78622a97ab)

### path-029772

```text
(config)# ipv6 dhcp pool <string> <cr>
```

Handler ` RVA 0x121C8450 `；selector ` 0 `；EOL ` RVA 0x357CCD98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` DHCP pool name。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-ed3fe0901c614ca5](../../evidence/parameters-sets-018.md#p-ed3fe0901c614ca5) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-035924

```text
(config)# ipv6 dhcp ppp framed-prefix cache <cr>
```

Handler ` RVA 0x121D2110 `；selector ` 0 `；EOL ` RVA 0x357CCA50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029671

```text
(config)# ipv6 dhcp ppp terminate <cr>
```

Handler ` RVA 0x121D2040 `；selector ` 0 `；EOL ` RVA 0x357CC768 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-035998

```text
(config)# ipv6 dhcp server join all-dhcp-servers <cr>
```

Handler ` RVA 0x121D21E0 `；selector ` 0 `；EOL ` RVA 0x357CD0E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-036071

```text
(config)# ipv6 dhcp server vrf enable <cr>
```

Handler ` RVA 0x121D23D0 `；selector ` 0 `；EOL ` RVA 0x357CD3B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-053412

```text
(config)# ipv6 dhcp test relay drop peeraddr <address> <cr>
```

Handler ` RVA 0x121AF4D0 `；selector ` 6 `；EOL ` RVA 0x357CE580 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IPv6 peer address。

[条件 C-7c8c9918b758dc9c](../../evidence/conditions-sets-048.md#c-7c8c9918b758dc9c) · [参数 P-f8bcbd6fae56b020](../../evidence/parameters-sets-019.md#p-f8bcbd6fae56b020) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-062280

```text
(config)# ipv6 dhcp test relay forward add <number:1..2147483647> <hex-string> <cr>
```

Handler ` RVA 0x121AF4D0 `；selector ` 1 `；EOL ` RVA 0x357CD850 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Decimal option number；` hexstring ` Hex bytes to add in relay       packet。

[条件 C-af295171a9451762](../../evidence/conditions-sets-068.md#c-af295171a9451762) · [缺口 G-ad6fad0994639193](../../evidence/gaps-sets-006.md#g-ad6fad0994639193) · [参数 P-23e74fec67dd5366](../../evidence/parameters-sets-003.md#p-23e74fec67dd5366) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-036293

```text
(config)# ipv6 dhcp test relay notifications <cr>
```

Handler ` RVA 0x121AF4D0 `；selector ` 4 `；EOL ` RVA 0x357CDF50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b3e4fea329eb4bd3](../../evidence/conditions-sets-070.md#c-b3e4fea329eb4bd3) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-036363

```text
(config)# ipv6 dhcp test relay packet-control <cr>
```

Handler ` RVA 0x121AF4D0 `；selector ` 5 `；EOL ` RVA 0x357CE1F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b3e4fea329eb4bd3](../../evidence/conditions-sets-070.md#c-b3e4fea329eb4bd3) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-062493

```text
(config)# ipv6 dhcp test relay reply add vsio <number:1..2147483647> <hex-string> <cr>
```

Handler ` RVA 0x121AF4D0 `；selector ` 3 `；EOL ` RVA 0x357CDC70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Decimal option number；` hexstring ` Hex bytes to add in VSIO option。

[条件 C-5539ac6a086799cf](../../evidence/conditions-sets-033.md#c-5539ac6a086799cf) · [缺口 G-acfc2222dae095bf](../../evidence/gaps-sets-006.md#g-acfc2222dae095bf) · [参数 P-b48e5ce58e345877](../../evidence/parameters-sets-014.md#p-b48e5ce58e345877) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-061911

```text
(config)# ipv6 dhcp test server add vsio <hex-string> <cr>
```

Handler ` RVA 0x121AF4D0 `；selector ` 2 `；EOL ` RVA 0x357CE968 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` hexstring ` Hex bytes to add in relay packet。

[条件 C-28bd4295656919ef](../../evidence/conditions-sets-016.md#c-28bd4295656919ef) · [缺口 G-2cb1718851a37386](../../evidence/gaps-sets-002.md#g-2cb1718851a37386) · [参数 P-0ea3be04251e1da3](../../evidence/parameters-sets-002.md#p-0ea3be04251e1da3) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027041

```text
(config)# ipv6 dhcp-client leasequery <cr>
```

Handler ` RVA 0x1219DC60 `；selector ` 1 `；EOL ` RVA 0x357CAC18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d559cb94c0e9aabd](../../evidence/conditions-sets-082.md#c-d559cb94c0e9aabd) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-035787

```text
(config)# ipv6 dhcp-client leasequery server <address> <cr>
```

Handler ` RVA 0x1219D8F0 `；selector ` 1 `；EOL ` RVA 0x357CA5E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IPv6 address。

[条件 C-365e765e786a5dcf](../../evidence/conditions-sets-021.md#c-365e765e786a5dcf) · [参数 P-97ef8b240ca08945](../../evidence/parameters-sets-012.md#p-97ef8b240ca08945) · [状态效果 S-f0d7c2d8d5a3611f](../../evidence/state_effects-sets-051.md#s-f0d7c2d8d5a3611f)

### path-061288

```text
(config)# ipv6 dhcp-client leasequery server <address> <interface> <cr>
```

Handler ` RVA 0x1219D8F0 `；selector ` 1 `；EOL ` RVA 0x357CA5E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` IPv6 address。

[条件 C-23163d82611a63dd](../../evidence/conditions-sets-014.md#c-23163d82611a63dd) · [缺口 G-821dcbee7f7bb67b](../../evidence/gaps-sets-005.md#g-821dcbee7f7bb67b) · [参数 P-4a330b1a7447d0b5](../../evidence/parameters-sets-006.md#p-4a330b1a7447d0b5) · [状态效果 S-f0d7c2d8d5a3611f](../../evidence/state_effects-sets-051.md#s-f0d7c2d8d5a3611f)

### path-029413

```text
(config)# ipv6 dhcp-relay bulk-lease disable <cr>
```

Handler ` RVA 0x121AEFE0 `；selector ` 0 `；EOL ` RVA 0x357C9140 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-035854

```text
(config)# ipv6 dhcp-relay bulk-lease retry <number:0..15> <cr>
```

Handler ` RVA 0x121AF210 `；selector ` 0 `；EOL ` RVA 0x357C9820 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Retries。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-b9cd7fb963121a4b](../../evidence/parameters-sets-014.md#p-b9cd7fb963121a4b) · [状态效果 S-cd8ef5314f5099f8](../../evidence/state_effects-sets-044.md#s-cd8ef5314f5099f8)

### path-035617

```text
(config)# ipv6 dhcp-relay bulk-lease timeout <number:1..40> <cr>
```

Handler ` RVA 0x121AF0F0 `；selector ` 0 `；EOL ` RVA 0x357C9450 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Minutes。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-be54b78770e2902c](../../evidence/parameters-sets-014.md#p-be54b78770e2902c) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029527

```text
(config)# ipv6 dhcp-relay option client-link-addr <cr>
```

Handler ` RVA 0x121AE960 `；selector ` 0 `；EOL ` RVA 0x357CA0A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029460

```text
(config)# ipv6 dhcp-relay option vpn <cr>
```

Handler ` RVA 0x121AE850 `；selector ` 0 `；EOL ` RVA 0x357C9E00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029369

```text
(config)# ipv6 dhcp-relay short-lease <number:60..3600> <cr>
```

Handler ` RVA 0x121AEDC0 `；selector ` 0 `；EOL ` RVA 0x357C8E18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Short Lease in Seconds。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-916df8f5af48c7a3](../../evidence/parameters-sets-011.md#p-916df8f5af48c7a3) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060594

```text
(config)# ipv6 dhcp-relay source-interface <interface> <cr>
```

Handler ` RVA 0x121AEB80 `；selector ` 0 `；EOL ` RVA 0x357C8A38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b2e28acae47c4159](../../evidence/conditions-sets-069.md#c-b2e28acae47c4159) · [缺口 G-c93dbeecc5c25fcf](../../evidence/gaps-sets-007.md#g-c93dbeecc5c25fcf) · [参数 P-96563fa9abda84da](../../evidence/parameters-sets-012.md#p-96563fa9abda84da) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026964

```text
(config)# ipv6 dhcp-relay trust-all <cr>
```

Handler ` RVA 0x121AEA70 `；selector ` 0 `；EOL ` RVA 0x357C9B18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027016

```text
(config)# ipv6 first-hop full-proxy <cr>
```

Handler ` RVA 0x1367FFE0 `；selector ` 0 `；EOL ` RVA 0x35BDD090 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-93d2c1eb9d621109](../../evidence/conditions-sets-057.md#c-93d2c1eb9d621109) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027070

```text
(config)# ipv6 first-hop logging <cr>
```

Handler ` RVA 0x136800A0 `；selector ` 0 `；EOL ` RVA 0x35BDD438 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-3dfc97031e854355](../../evidence/state_effects-sets-014.md#s-3dfc97031e854355)

### path-035730

```text
(config)# ipv6 first-hop service-support punt-acl <number:0..7> <cr>
```

Handler ` RVA 0x13687B10 `；selector ` 0 `；EOL ` RVA 0x35BDD808 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Support (0: none, 1:port, 2:vlan, 4:box, 7: all, ...)。

[条件 C-919e4630fbba4a71](../../evidence/conditions-sets-056.md#c-919e4630fbba4a71) · [参数 P-f1ebff7dfc468e57](../../evidence/parameters-sets-018.md#p-f1ebff7dfc468e57) · [状态效果 S-6f546052b88ea86e](../../evidence/state_effects-sets-024.md#s-6f546052b88ea86e)

### path-062990

```text
(config)# ipv6 first-hop unit-test association interface <interface> <address> command new <cr>
```

Handler ` RVA 0x13685C30 `；selector ` 0 `；EOL ` RVA 0x35BD8F70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` 48-bit hardware address。

[条件 C-bebbb109f404849a](../../evidence/conditions-sets-074.md#c-bebbb109f404849a) · [缺口 G-e94b9a5adc8ceacf](../../evidence/gaps-sets-008.md#g-e94b9a5adc8ceacf) · [参数 P-89afef22378748d3](../../evidence/parameters-sets-011.md#p-89afef22378748d3) · [状态效果 S-4aff97daef01aba1](../../evidence/state_effects-sets-016.md#s-4aff97daef01aba1)

### path-063018

```text
(config)# ipv6 first-hop unit-test bt-add bd <number:dynamic> interface <interface> <address> <cr>
```

Handler ` RVA 0x13680440 `；selector ` 1001 `；EOL ` RVA 0x35BDB798 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Bridge-domain number；` address ` IPv6 address。

[条件 C-5711ae915703b2d4](../../evidence/conditions-sets-034.md#c-5711ae915703b2d4) · [缺口 G-d62ffe267eaf1420](../../evidence/gaps-sets-007.md#g-d62ffe267eaf1420) · [参数 P-d97d751941769d95](../../evidence/parameters-sets-016.md#p-d97d751941769d95) · [状态效果 S-404cc225fb5591e4](../../evidence/state_effects-sets-014.md#s-404cc225fb5591e4)

### path-029412

```text
(config)# ipv6 first-hop unit-test bulk-sync <cr>
```

Handler ` RVA 0x13685F80 `；selector ` 0 `；EOL ` RVA 0x35BD8468 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-728106110fe5b4fc](../../evidence/conditions-sets-044.md#c-728106110fe5b4fc) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-052994

```text
(config)# ipv6 first-hop unit-test check-reach vlan <number:0..4096> <address> <cr>
```

Handler ` RVA 0x136868D0 `；selector ` 0 `；EOL ` RVA 0x35BD97B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Vlan number；` address ` IPv6 address。

[条件 C-728106110fe5b4fc](../../evidence/conditions-sets-044.md#c-728106110fe5b4fc) · [参数 P-7facea3416f79200](../../evidence/parameters-sets-010.md#p-7facea3416f79200) · [状态效果 S-e88d8aa49b16312a](../../evidence/state_effects-sets-049.md#s-e88d8aa49b16312a)

### path-062496

```text
(config)# ipv6 first-hop unit-test clear neighbors binding <interface> vlanlist <string> <cr>
```

Handler ` RVA 0x13686C10 `；selector ` 0 `；EOL ` RVA 0x35BDCC60 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` A list of vlanids separated by space。

[条件 C-58814efd7dce12d1](../../evidence/conditions-sets-035.md#c-58814efd7dce12d1) · [缺口 G-67c200a8759844a7](../../evidence/gaps-sets-004.md#g-67c200a8759844a7) · [参数 P-ea13eb414cac0389](../../evidence/parameters-sets-018.md#p-ea13eb414cac0389) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-062932

```text
(config)# ipv6 first-hop unit-test dhcp_binding_chg vlan <number:1..4096> interface <interface> <?ipv4orv6_addr_action@55558b12e120> <address> mode add <cr>
```

Handler ` RVA 0x13684E20 `；selector ` 0 `；EOL ` RVA 0x35BDA2E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Vlan number；` address ` 48-bit hardware address。

[条件 C-51de0685bdd8cd31](../../evidence/conditions-sets-032.md#c-51de0685bdd8cd31) · [缺口 G-bfa8f1df76ece841](../../evidence/gaps-sets-007.md#g-bfa8f1df76ece841) · [参数 P-f2acc6defe2e1240](../../evidence/parameters-sets-018.md#p-f2acc6defe2e1240) · [状态效果 S-81cac7d458b75109](../../evidence/state_effects-sets-028.md#s-81cac7d458b75109)

### path-030020

```text
(config)# ipv6 first-hop unit-test disable-cli-sync <cr>
```

Handler ` RVA 0x13686B70 `；selector ` 0 `；EOL ` RVA 0x35BDC7F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-728106110fe5b4fc](../../evidence/conditions-sets-044.md#c-728106110fe5b4fc) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-057337

```text
(config)# ipv6 first-hop unit-test ha-sync-msg msg-type bt-entry action enable <cr>
```

Handler ` RVA 0x13686A80 `；selector ` 0 `；EOL ` RVA 0x35BDBFC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-728106110fe5b4fc](../../evidence/conditions-sets-044.md#c-728106110fe5b4fc) · [状态效果 S-8136d81d2d9ad14c](../../evidence/state_effects-sets-027.md#s-8136d81d2d9ad14c)

### path-061310

```text
(config)# ipv6 first-hop unit-test ipdt interface <interface> <cr>
```

Handler ` RVA 0x13685160 `；selector ` 0 `；EOL ` RVA 0x35BD9B80 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0b1240884ae92ace](../../evidence/conditions-sets-005.md#c-0b1240884ae92ace) · [缺口 G-44234f6bb2ec207c](../../evidence/gaps-sets-003.md#g-44234f6bb2ec207c) · [参数 P-38aaed28e873b32b](../../evidence/parameters-sets-005.md#p-38aaed28e873b32b) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-045470

```text
(config)# ipv6 first-hop unit-test ipdt vlan <number:1..4096> <cr>
```

Handler ` RVA 0x13685160 `；selector ` 0 `；EOL ` RVA 0x35BD9B80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Vlan number。

[条件 C-728106110fe5b4fc](../../evidence/conditions-sets-044.md#c-728106110fe5b4fc) · [参数 P-ba82800780ced9a3](../../evidence/parameters-sets-014.md#p-ba82800780ced9a3) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-061291

```text
(config)# ipv6 first-hop unit-test notify register <interface> <cr>
```

Handler ` RVA 0x13685CF0 `；selector ` 0 `；EOL ` RVA 0x35BD8870 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-64c2919995484c6b](../../evidence/conditions-sets-039.md#c-64c2919995484c6b) · [缺口 G-9447d86a54c9c7ca](../../evidence/gaps-sets-005.md#g-9447d86a54c9c7ca) · [参数 P-5650a5ff49e861fc](../../evidence/parameters-sets-007.md#p-5650a5ff49e861fc) · [状态效果 S-e60016be11e6164d](../../evidence/state_effects-sets-049.md#s-e60016be11e6164d)

### path-029954

```text
(config)# ipv6 first-hop unit-test pgm <cr>
```

Handler ` RVA 0x13680F90 `；selector ` 0 `；EOL ` RVA 0x35BDABC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-728106110fe5b4fc](../../evidence/conditions-sets-044.md#c-728106110fe5b4fc) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-061312

```text
(config)# ipv6 first-hop unit-test pgm peer <?ipv4orv6_addr_action@55558b12eb98> <cr>
```

Handler ` RVA 0x13680F90 `；selector ` 0 `；EOL ` RVA 0x35BDABC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-728106110fe5b4fc](../../evidence/conditions-sets-044.md#c-728106110fe5b4fc) · [缺口 G-6d80364c1d6f26c9](../../evidence/gaps-sets-004.md#g-6d80364c1d6f26c9) · [状态效果 S-08a2331b9eb2ac51](../../evidence/state_effects-sets-002.md#s-08a2331b9eb2ac51)

### path-061333

```text
(config)# ipv6 first-hop unit-test reapply-filters interface <interface> <cr>
```

Handler ` RVA 0x13685FF0 `；selector ` 0 `；EOL ` RVA 0x35BDC440 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ada70663c7f2f1d0](../../evidence/conditions-sets-067.md#c-ada70663c7f2f1d0) · [缺口 G-625a979760ba3ab5](../../evidence/gaps-sets-004.md#g-625a979760ba3ab5) · [参数 P-bd37ab274ace47c3](../../evidence/parameters-sets-014.md#p-bd37ab274ace47c3) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-045713

```text
(config)# ipv6 first-hop unit-test reapply-filters vlan <number:1..4096> <cr>
```

Handler ` RVA 0x13685FF0 `；selector ` 0 `；EOL ` RVA 0x35BDC440 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Vlan number。

[条件 C-728106110fe5b4fc](../../evidence/conditions-sets-044.md#c-728106110fe5b4fc) · [参数 P-e91f8d63075ae567](../../evidence/parameters-sets-017.md#p-e91f8d63075ae567) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060834

```text
(config)# ipv6 first-hop unit-test transport <hex-string> <cr>
```

Handler ` RVA 0x13680A60 `；selector ` 0 `；EOL ` RVA 0x35BD93F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` hexstring ` Authentication Key。

[条件 C-ed1fdebe60c41a4d](../../evidence/conditions-sets-092.md#c-ed1fdebe60c41a4d) · [缺口 G-5f936b742e527807](../../evidence/gaps-sets-004.md#g-5f936b742e527807) · [参数 P-42102da049527be0](../../evidence/parameters-sets-006.md#p-42102da049527be0) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029952

```text
(config)# ipv6 first-hop unit-test upgm <cr>
```

Handler ` RVA 0x13680B60 `；selector ` 0 `；EOL ` RVA 0x35BDB0D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-728106110fe5b4fc](../../evidence/conditions-sets-044.md#c-728106110fe5b4fc) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-061317

```text
(config)# ipv6 first-hop unit-test upgm interface <interface> <cr>
```

Handler ` RVA 0x13680B60 `；selector ` 0 `；EOL ` RVA 0x35BDB0D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4466ad7a925c2483](../../evidence/conditions-sets-027.md#c-4466ad7a925c2483) · [缺口 G-cafd61294242d7e8](../../evidence/gaps-sets-007.md#g-cafd61294242d7e8) · [参数 P-0c728d6efee1b554](../../evidence/parameters-sets-001.md#p-0c728d6efee1b554) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025771

```text
(config)# ipv6 flowset <cr>
```

Handler ` RVA 0x123062B0 `；selector ` 0 `；EOL ` RVA 0x357E7478 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060587

```text
(config)# ipv6 general-prefix <string> <prefix:dynamic> <cr>
```

Handler ` RVA 0x12302D50 `；selector ` 0 `；EOL ` RVA 0x357DFE70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` General prefix name；` prefix_dynamic ` IPv6 prefix。

[条件 C-07f6280acb06964e](../../evidence/conditions-sets-003.md#c-07f6280acb06964e) · [缺口 G-c01274587191dce5](../../evidence/gaps-sets-007.md#g-c01274587191dce5) · [参数 P-814a9def927a1048](../../evidence/parameters-sets-010.md#p-814a9def927a1048) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026841

```text
(config)# ipv6 hop-limit <number:1..255> <cr>
```

Handler ` RVA 0x12305EC0 `；selector ` 0 `；EOL ` RVA 0x357E5EB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Hop Limit value。

[条件 C-3e83752264b899b6](../../evidence/conditions-sets-024.md#c-3e83752264b899b6) · [参数 P-afa34fe62b3a631b](../../evidence/parameters-sets-013.md#p-afa34fe62b3a631b) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029390

```text
(config)# ipv6 host <string> <address> <cr>
```

Handler ` RVA 0x123215D0 `；selector ` 0 `；EOL ` RVA 0x3580E3B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of host；` address ` IPv6 address。

[条件 C-986f46655526a8f0](../../evidence/conditions-sets-059.md#c-986f46655526a8f0) · [参数 P-d282f3f0281751da](../../evidence/parameters-sets-016.md#p-d282f3f0281751da) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029321

```text
(config)# ipv6 icmp error-interval <number:0..2147483647> <cr>
```

Handler ` RVA 0x12306390 `；selector ` 0 `；EOL ` RVA 0x357E6968 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Interval between tokens in milliseconds。

[条件 C-73c5bdc51f6dfbe7](../../evidence/conditions-sets-045.md#c-73c5bdc51f6dfbe7) · [参数 P-8be1513c1923423e](../../evidence/parameters-sets-011.md#p-8be1513c1923423e) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029188

```text
(config)# ipv6 icmp od-length enable <cr>
```

Handler ` RVA 0x12307300 `；selector ` 0 `；EOL ` RVA 0x357E6C78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029255

```text
(config)# ipv6 icmp od-length test <cr>
```

Handler ` RVA 0x123073F0 `；selector ` 0 `；EOL ` RVA 0x357E6F20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-61524ae912be1b83](../../evidence/conditions-sets-038.md#c-61524ae912be1b83) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060611

```text
(config)# ipv6 ldap source-interface <interface> <cr>
```

Handler ` RVA 0x11ABB9B0 `；selector ` 29 `；EOL ` RVA 0x35611FE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f9fb3441b2aac94e](../../evidence/conditions-sets-097.md#c-f9fb3441b2aac94e) · [缺口 G-16c6f383de0ea62c](../../evidence/gaps-sets-001.md#g-16c6f383de0ea62c) · [参数 P-5c02e9836d79ab5e](../../evidence/parameters-sets-007.md#p-5c02e9836d79ab5e) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-035421

```text
(config)# ipv6 local policy route-map <string> <cr>
```

Handler ` RVA 0x118B9990 `；selector ` 0 `；EOL ` RVA 0x3559BDF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Route-map name。

[条件 C-8e22a74fe3e25006](../../evidence/conditions-sets-055.md#c-8e22a74fe3e25006) · [参数 P-9f51f3ef670daa43](../../evidence/parameters-sets-012.md#p-9f51f3ef670daa43) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-062821

```text
(config)# ipv6 local pool <string> <prefix:dynamic> <number:dynamic> <cr>
```

Handler ` RVA 0x1232C650 `；selector ` 0 `；EOL ` RVA 0x35810C20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Create named local prefix pool；` prefix_dynamic ` IPv6 pool prefix x:x::y/&lt;z&gt;；` unsigned_number_dynamic ` Prefix length to assign from pool。

[条件 C-d3bd80c442bb5e98](../../evidence/conditions-sets-082.md#c-d3bd80c442bb5e98) · [缺口 G-f127a4c37ed8f052](../../evidence/gaps-sets-008.md#g-f127a4c37ed8f052) · [参数 P-df3365ff8ffed2a8](../../evidence/parameters-sets-017.md#p-df3365ff8ffed2a8) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025790

```text
(config)# ipv6 mfib <cr>
```

Handler ` RVA 0x11903850 `；selector ` 0 `；EOL ` RVA 0x3553E1A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4b23c8c507fe5af2](../../evidence/conditions-sets-029.md#c-4b23c8c507fe5af2) · [状态效果 S-934de520b5a39faf](../../evidence/state_effects-sets-031.md#s-934de520b5a39faf)

### path-025809

```text
(config)# ipv6 mfib <cr>
```

Handler ` RVA 0x11903850 `；selector ` 0 `；EOL ` RVA 0x3553DEA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c9ded9d41ae45538](../../evidence/conditions-sets-078.md#c-c9ded9d41ae45538) · [状态效果 S-934de520b5a39faf](../../evidence/state_effects-sets-031.md#s-934de520b5a39faf)

### path-027073

```text
(config)# ipv6 mfib hardware-switching <cr>
```

Handler ` RVA 0x11827A60 `；selector ` 0 `；EOL ` RVA 0x3553D8C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-68150c0384476b4e](../../evidence/conditions-sets-040.md#c-68150c0384476b4e) · [状态效果 S-934de520b5a39faf](../../evidence/state_effects-sets-031.md#s-934de520b5a39faf)

### path-029588

```text
(config)# ipv6 mfib hardware-switching connected <cr>
```

Handler ` RVA 0x11827EF0 `；selector ` 0 `；EOL ` RVA 0x3553D278 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-11730e923d844f9f](../../evidence/conditions-sets-007.md#c-11730e923d844f9f) · [状态效果 S-934de520b5a39faf](../../evidence/state_effects-sets-031.md#s-934de520b5a39faf)

### path-035792

```text
(config)# ipv6 mfib hardware-switching replication-mode ingress <cr>
```

Handler ` RVA 0x118280C0 `；selector ` 0 `；EOL ` RVA 0x3553D588 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-11730e923d844f9f](../../evidence/conditions-sets-007.md#c-11730e923d844f9f) · [状态效果 S-934de520b5a39faf](../../evidence/state_effects-sets-031.md#s-934de520b5a39faf)

### path-029470

```text
(config)# ipv6 mfib hardware-switching shared-tree <cr>
```

Handler ` RVA 0x11827CE0 `；selector ` 0 `；EOL ` RVA 0x3553CF90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b5e13c2566523438](../../evidence/conditions-sets-070.md#c-b5e13c2566523438) · [状态效果 S-934de520b5a39faf](../../evidence/state_effects-sets-031.md#s-934de520b5a39faf)

### path-029733

```text
(config)# ipv6 mfib hardware-switching uplink <cr>
```

Handler ` RVA 0x11828350 `；selector ` 0 `；EOL ` RVA 0x3553D898 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-395975aa3036d315](../../evidence/conditions-sets-022.md#c-395975aa3036d315) · [状态效果 S-934de520b5a39faf](../../evidence/state_effects-sets-031.md#s-934de520b5a39faf)

### path-026910

```text
(config)# ipv6 mfib logging-ttl <cr>
```

Handler ` RVA 0x11905500 `；selector ` 0 `；EOL ` RVA 0x3553CBC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ac3ac80ac94b74d5](../../evidence/conditions-sets-067.md#c-ac3ac80ac94b74d5) · [状态效果 S-934de520b5a39faf](../../evidence/state_effects-sets-031.md#s-934de520b5a39faf)

### path-029459

```text
(config)# ipv6 mld ssm-map enable <cr>
```

Handler ` RVA 0x115D9B60 `；selector ` 17 `；EOL ` RVA 0x35543F90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c92a52d4f9a0426f](../../evidence/conditions-sets-077.md#c-c92a52d4f9a0426f) · [状态效果 S-9d4f540036512032](../../evidence/state_effects-sets-033.md#s-9d4f540036512032)

### path-035732

```text
(config)# ipv6 mld ssm-map query dns <cr>
```

Handler ` RVA 0x115D9B60 `；selector ` 19 `；EOL ` RVA 0x35544680 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c92a52d4f9a0426f](../../evidence/conditions-sets-077.md#c-c92a52d4f9a0426f) · [状态效果 S-9d4f540036512032](../../evidence/state_effects-sets-033.md#s-9d4f540036512032)

### path-045273

```text
(config)# ipv6 mld ssm-map static <number:1..199> <address> <cr>
```

Handler ` RVA 0x115D9B60 `；selector ` 18 `；EOL ` RVA 0x35544350 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Access list specifying SSM group range；` address ` SSM source address。

[条件 C-40bcd43c4a7cc7be](../../evidence/conditions-sets-025.md#c-40bcd43c4a7cc7be) · [参数 P-6b633ed1199d8fd7](../../evidence/parameters-sets-008.md#p-6b633ed1199d8fd7) · [状态效果 S-9d4f540036512032](../../evidence/state_effects-sets-033.md#s-9d4f540036512032)

### path-029583

```text
(config)# ipv6 mld state-limit <number:1..64000> <cr>
```

Handler ` RVA 0x115D9B60 `；selector ` 20 `；EOL ` RVA 0x35544998 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Max Allowed State。

[条件 C-775d95ea7b44725b](../../evidence/conditions-sets-046.md#c-775d95ea7b44725b) · [参数 P-5df4f95ce415938c](../../evidence/parameters-sets-008.md#p-5df4f95ce415938c) · [状态效果 S-9d4f540036512032](../../evidence/state_effects-sets-033.md#s-9d4f540036512032)

### path-030147

```text
(config)# ipv6 multicast group-range <number:1..199> <cr>
```

Handler ` RVA 0x118E3BE0 `；selector ` 3 `；EOL ` RVA 0x3553A510 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Access list specifying group ranges。

[条件 C-4fc94554bdbeff85](../../evidence/conditions-sets-031.md#c-4fc94554bdbeff85) · [参数 P-53f790ec162a0a1d](../../evidence/parameters-sets-007.md#p-53f790ec162a0a1d) · [状态效果 S-2d57e2fa2c26f266](../../evidence/state_effects-sets-010.md#s-2d57e2fa2c26f266)

### path-045950

```text
(config)# ipv6 multicast limit cost <number:1..199> <number:0..2147483647> <cr>
```

Handler ` RVA 0x11725BA0 `；selector ` 28 `；EOL ` RVA 0x35539E68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Access list specifying group ranges；` unsigned_number ` Cost associated with access list。

[条件 C-a2e79dbada5d403f](../../evidence/conditions-sets-063.md#c-a2e79dbada5d403f) · [参数 P-0992d7849024b9cc](../../evidence/parameters-sets-001.md#p-0992d7849024b9cc) · [状态效果 S-2d57e2fa2c26f266](../../evidence/state_effects-sets-010.md#s-2d57e2fa2c26f266)

### path-036583

```text
(config)# ipv6 multicast limit rate <number:0..100> <cr>
```

Handler ` RVA 0x11725BA0 `；selector ` 30 `；EOL ` RVA 0x3553A208 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` msg/sec, 0 not rate limited。

[条件 C-6ecc6dc7cf30793a](../../evidence/conditions-sets-043.md#c-6ecc6dc7cf30793a) · [参数 P-60271cc96df1a316](../../evidence/parameters-sets-008.md#p-60271cc96df1a316) · [状态效果 S-2d57e2fa2c26f266](../../evidence/state_effects-sets-010.md#s-2d57e2fa2c26f266)

### path-036228

```text
(config)# ipv6 multicast mib set-enable mgmd <cr>
```

Handler ` RVA 0x134A1C40 `；selector ` 0 `；EOL ` RVA 0x35A9F210 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-8466c8c91ecb350d](../../evidence/state_effects-sets-028.md#s-8466c8c91ecb350d)

### path-036296

```text
(config)# ipv6 multicast mib set-enable pimstdmib <cr>
```

Handler ` RVA 0x134ACBC0 `；selector ` 0 `；EOL ` RVA 0x35AA0C28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-8466c8c91ecb350d](../../evidence/state_effects-sets-028.md#s-8466c8c91ecb350d)

### path-030058

```text
(config)# ipv6 multicast mpls mldp <cr>
```

Handler ` RVA 0x118E3BE0 `；selector ` 5 `；EOL ` RVA 0x355366E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cb56a117c3c4a323](../../evidence/conditions-sets-078.md#c-cb56a117c3c4a323) · [状态效果 S-2d57e2fa2c26f266](../../evidence/state_effects-sets-010.md#s-2d57e2fa2c26f266)

### path-060871

```text
(config)# ipv6 multicast mpls source <interface> <cr>
```

Handler ` RVA 0x118E3BE0 `；selector ` 4 `；EOL ` RVA 0x35536F78 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-54fb9308e0d5ee33](../../evidence/conditions-sets-033.md#c-54fb9308e0d5ee33) · [缺口 G-b1fe266a0ac36afb](../../evidence/gaps-sets-006.md#g-b1fe266a0ac36afb) · [参数 P-b33de07f1b2b71db](../../evidence/parameters-sets-014.md#p-b33de07f1b2b71db) · [状态效果 S-2d57e2fa2c26f266](../../evidence/state_effects-sets-010.md#s-2d57e2fa2c26f266)

### path-030091

```text
(config)# ipv6 multicast mpls traffic-eng <cr>
```

Handler ` RVA 0x118E3BE0 `；selector ` 6 `；EOL ` RVA 0x35536B60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d22d60dfc11b43ad](../../evidence/conditions-sets-081.md#c-d22d60dfc11b43ad) · [状态效果 S-2d57e2fa2c26f266](../../evidence/state_effects-sets-010.md#s-2d57e2fa2c26f266)

### path-027182

```text
(config)# ipv6 multicast multipath <cr>
```

Handler ` RVA 0x118E3BE0 `；selector ` 2 `；EOL ` RVA 0x35539A18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff8eb02b54cf08c5](../../evidence/conditions-sets-099.md#c-ff8eb02b54cf08c5) · [状态效果 S-2d57e2fa2c26f266](../../evidence/state_effects-sets-010.md#s-2d57e2fa2c26f266)

### path-027111

```text
(config)# ipv6 multicast pim-passive-enable <cr>
```

Handler ` RVA 0x11725BA0 `；selector ` 19 `；EOL ` RVA 0x35538FF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ecdcd8ad5ebc4f00](../../evidence/conditions-sets-092.md#c-ecdcd8ad5ebc4f00) · [状态效果 S-2d57e2fa2c26f266](../../evidence/state_effects-sets-010.md#s-2d57e2fa2c26f266)

### path-030055

```text
(config)# ipv6 multicast route-limit <number:100..2147483647> <cr>
```

Handler ` RVA 0x11725BA0 `；selector ` 53 `；EOL ` RVA 0x355396F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` number of routes。

[条件 C-d1b0701708c7a076](../../evidence/conditions-sets-081.md#c-d1b0701708c7a076) · [参数 P-673f786f128639cf](../../evidence/parameters-sets-008.md#p-673f786f128639cf) · [状态效果 S-2d57e2fa2c26f266](../../evidence/state_effects-sets-010.md#s-2d57e2fa2c26f266)

### path-045986

```text
(config)# ipv6 multicast rpf backoff <number:200..65535> <number:200..65535> <cr>
```

Handler ` RVA 0x11725BA0 `；selector ` 17 `；EOL ` RVA 0x35563608 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Initial RPF backoff delay in milliseconds；` unsigned_number ` Maximum RPF backoff delay in milliseconds。

[条件 C-fe076ca821df7995](../../evidence/conditions-sets-098.md#c-fe076ca821df7995) · [参数 P-69607040a9c5f47c](../../evidence/parameters-sets-008.md#p-69607040a9c5f47c) · [状态效果 S-9b26bb40080535d3](../../evidence/state_effects-sets-033.md#s-9b26bb40080535d3)

### path-057510

```text
(config)# ipv6 multicast rpf select vrf <string> group-range <number:1..199> <cr>
```

Handler ` RVA 0x11725BA0 `；selector ` 18 `；EOL ` RVA 0x35563A58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` VPN Routing/Forwarding instance name；` unsigned_number ` Access list specifying group ranges。

[条件 C-74b7d68b7c98a74d](../../evidence/conditions-sets-045.md#c-74b7d68b7c98a74d) · [参数 P-651cae64a3448b1b](../../evidence/parameters-sets-008.md#p-651cae64a3448b1b) · [状态效果 S-9b26bb40080535d3](../../evidence/state_effects-sets-033.md#s-9b26bb40080535d3)

### path-029921

```text
(config)# ipv6 multicast rpf use-bgp <cr>
```

Handler ` RVA 0x118E3BE0 `；selector ` 1 `；EOL ` RVA 0x355393D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff8eb02b54cf08c5](../../evidence/conditions-sets-099.md#c-ff8eb02b54cf08c5) · [状态效果 S-2d57e2fa2c26f266](../../evidence/state_effects-sets-010.md#s-2d57e2fa2c26f266)

### path-025825

```text
(config)# ipv6 multicast-routing <cr>
```

Handler ` RVA 0x118E3BE0 `；selector ` 0 `；EOL ` RVA 0x355362A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-974b2b6301412b1a](../../evidence/conditions-sets-058.md#c-974b2b6301412b1a) · [状态效果 S-959f3c6fbdb5f519](../../evidence/state_effects-sets-032.md#s-959f3c6fbdb5f519)

### path-035525

```text
(config)# ipv6 nd cache expire refresh <cr>
```

Handler ` RVA 0x12318AD0 `；selector ` 0 `；EOL ` RVA 0x35804598 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-56a423aa783e9b0a](../../evidence/conditions-sets-034.md#c-56a423aa783e9b0a) · [状态效果 S-2519aef6bb6421b5](../../evidence/state_effects-sets-008.md#s-2519aef6bb6421b5)

### path-035490

```text
(config)# ipv6 nd cache interface-limit <number:1..4294967295> <cr>
```

Handler ` RVA 0x123187D0 `；selector ` 0 `；EOL ` RVA 0x358041D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of entries。

[条件 C-f6882993b2db3878](../../evidence/conditions-sets-095.md#c-f6882993b2db3878) · [参数 P-13961c879dc8fa89](../../evidence/parameters-sets-002.md#p-13961c879dc8fa89) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-035731

```text
(config)# ipv6 nd dad loopback detect <cr>
```

Handler ` RVA 0x12318E20 `；selector ` 0 `；EOL ` RVA 0x357F8940 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027008

```text
(config)# ipv6 nd dad time <number:1..6000> <cr>
```

Handler ` RVA 0x12319070 `；selector ` 0 `；EOL ` RVA 0x357F8620 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` time (milliseconds)。

[条件 C-c49ad7125361171c](../../evidence/conditions-sets-076.md#c-c49ad7125361171c) · [参数 P-130782338452365e](../../evidence/parameters-sets-002.md#p-130782338452365e) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027054

```text
(config)# ipv6 nd default-route <cr>
```

Handler ` RVA 0x12315B20 `；selector ` 0 `；EOL ` RVA 0x357F8368 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060838

```text
(config)# ipv6 nd default-route vrf <?match_ipv6_zoneinfo_action@55558ad4c2b8> <cr>
```

Handler ` RVA 0x12315B20 `；selector ` 0 `；EOL ` RVA 0x357F8368 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [缺口 G-7a3e9f6c33005086](../../evidence/gaps-sets-005.md#g-7a3e9f6c33005086) · [状态效果 S-077f01203aa2280e](../../evidence/state_effects-sets-002.md#s-077f01203aa2280e)

### path-035341

```text
(config)# ipv6 nd host mode strict <cr>
```

Handler ` RVA 0x123196C0 `；selector ` 0 `；EOL ` RVA 0x35805D30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025792

```text
(config)# ipv6 nd ns-interval <number:1000..30000> <cr>
```

Handler ` RVA 0x12315250 `；selector ` 0 `；EOL ` RVA 0x357F79A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Retransmission interval in milliseconds。

[条件 C-ea11492cab06562e](../../evidence/conditions-sets-090.md#c-ea11492cab06562e) · [参数 P-3eca35a80fbea252](../../evidence/parameters-sets-005.md#p-3eca35a80fbea252) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026857

```text
(config)# ipv6 nd nsf convergence <number:10..600> <cr>
```

Handler ` RVA 0x123158A0 `；selector ` 0 `；EOL ` RVA 0x357F6A38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Time (seconds)。

[条件 C-c669ba313d2e75c3](../../evidence/conditions-sets-076.md#c-c669ba313d2e75c3) · [参数 P-d3108a7c0d06de87](../../evidence/parameters-sets-016.md#p-d3108a7c0d06de87) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

