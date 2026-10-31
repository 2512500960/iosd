# configure · 六个基础模式的历史连接

[模式索引](README.md) · [总索引](../../README.md)

### path-029152

```text
(config)# ip arp incomplete enable <cr>
```

Handler ` RVA 0xCF6D790 `；selector ` 2 `；EOL ` RVA 0x33D37888 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-39cdb69e08ed4750](../../evidence/conditions-sets-022.md#c-39cdb69e08ed4750) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-035249

```text
(config)# ip arp incomplete entries <number:1..2147483647> <cr>
```

Handler ` RVA 0xCF6D790 `；selector ` 1 `；EOL ` RVA 0x33D37600 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Specify the number of IP addresses to resolve。

[条件 C-5d33879c49f5c74d](../../evidence/conditions-sets-036.md#c-5d33879c49f5c74d) · [参数 P-b6b36df502bfabcb](../../evidence/parameters-sets-014.md#p-b6b36df502bfabcb) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-035199

```text
(config)# ip arp incomplete retry <number:1..2147483647> <cr>
```

Handler ` RVA 0xCF6D790 `；selector ` 0 `；EOL ` RVA 0x33D372E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Specify the number of times an ARP Request is sent。

[条件 C-0b18a655ba0ef8d5](../../evidence/conditions-sets-005.md#c-0b18a655ba0ef8d5) · [参数 P-c0cd72978c115d4e](../../evidence/parameters-sets-015.md#p-c0cd72978c115d4e) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-035018

```text
(config)# ip arp nat-garp-retry feature enable <cr>
```

Handler ` RVA 0xCF70EE0 `；selector ` 5 `；EOL ` RVA 0x33D36988 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-058aa87adb933d0f](../../evidence/conditions-sets-003.md#c-058aa87adb933d0f) · [状态效果 S-20cec46070ceb99e](../../evidence/state_effects-sets-007.md#s-20cec46070ceb99e)

### path-034887

```text
(config)# ip arp poll queue <number:10..10000> <cr>
```

Handler ` RVA 0xCFE2190 `；selector ` 2 `；EOL ` RVA 0x33D35750 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` IP ARP polling queue size。

[条件 C-30af889cae03af6e](../../evidence/conditions-sets-019.md#c-30af889cae03af6e) · [参数 P-7d4c19cd79a7c438](../../evidence/parameters-sets-010.md#p-7d4c19cd79a7c438) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-034945

```text
(config)# ip arp poll rate <number:10..10000> <cr>
```

Handler ` RVA 0xCFE2190 `；selector ` 1 `；EOL ` RVA 0x33D35A78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` IP ARP polling packet rate。

[条件 C-5db894a77ca0c688](../../evidence/conditions-sets-037.md#c-5db894a77ca0c688) · [参数 P-358dbac37bce50fb](../../evidence/parameters-sets-005.md#p-358dbac37bce50fb) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-028816

```text
(config)# ip arp proxy disable <cr>
```

Handler ` RVA 0xCF2A810 `；selector ` 5 `；EOL ` RVA 0x33D35DE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-565bb3469d8d2a26](../../evidence/conditions-sets-034.md#c-565bb3469d8d2a26) · [状态效果 S-1a5576c1e3336bb2](../../evidence/state_effects-sets-006.md#s-1a5576c1e3336bb2)

### path-029024

```text
(config)# ip arp queue <number:512..2147483647> <cr>
```

Handler ` RVA 0xCF2A810 `；selector ` 19 `；EOL ` RVA 0x33D36F18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Size of ARP Input Packet Queue。

[条件 C-94684634072e658d](../../evidence/conditions-sets-057.md#c-94684634072e658d) · [参数 P-7b7b3ea7d58cec76](../../evidence/parameters-sets-010.md#p-7b7b3ea7d58cec76) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-028955

```text
(config)# ip as-path access-list <number:1..500> <cr>
```

Handler ` RVA 0xF24D1D0 `；selector ` 0 `；EOL ` RVA 0x344CEB18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` AS path access list number。

[条件 C-2127af5c2bc0de42](../../evidence/conditions-sets-013.md#c-2127af5c2bc0de42) · [参数 P-d03940460717af2e](../../evidence/parameters-sets-016.md#p-d03940460717af2e) · [状态效果 S-e10f9bb2dedc9a7e](../../evidence/state_effects-sets-048.md#s-e10f9bb2dedc9a7e)

### path-025858

```text
(config)# ip auth-proxy <cr>
```

Handler ` RVA 0xCBA3DA0 `；selector ` 0 `；EOL ` RVA 0x33BFD190 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-52cfa7d1847a2730](../../evidence/conditions-sets-032.md#c-52cfa7d1847a2730) · [状态效果 S-d0442b07be0f27f7](../../evidence/state_effects-sets-044.md#s-d0442b07be0f27f7)

### path-027043

```text
(config)# ip auth-proxy auth-proxy-audit <cr>
```

Handler ` RVA 0xCBA3DA0 `；selector ` 9 `；EOL ` RVA 0x33BFBB88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-254566f36f9fd550](../../evidence/conditions-sets-015.md#c-254566f36f9fd550) · [状态效果 S-d0442b07be0f27f7](../../evidence/state_effects-sets-044.md#s-d0442b07be0f27f7)

### path-029571

```text
(config)# ip auth-proxy auth-proxy-banner file <cr>
```

Handler ` RVA 0xCBA3DA0 `；selector ` 6 `；EOL ` RVA 0x33BFA2E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-81dcfd517b281510](../../evidence/conditions-sets-050.md#c-81dcfd517b281510) · [状态效果 S-8cc202ad47a224ba](../../evidence/state_effects-sets-030.md#s-8cc202ad47a224ba)

### path-029833

```text
(config)# ip auth-proxy inactivity-timer <number:1..35791> <cr>
```

Handler ` RVA 0xCBA3DA0 `；selector ` 1 `；EOL ` RVA 0x33BFBF48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timeout in minutes。

[条件 C-b5b22cd4e51ff3ae](../../evidence/conditions-sets-070.md#c-b5b22cd4e51ff3ae) · [参数 P-1eb21df47968d0d5](../../evidence/parameters-sets-003.md#p-1eb21df47968d0d5) · [状态效果 S-a5f6891031a57c83](../../evidence/state_effects-sets-035.md#s-a5f6891031a57c83)

### path-029685

```text
(config)# ip auth-proxy init-state-time <number:1..35791> <cr>
```

Handler ` RVA 0xCBA3DA0 `；selector ` 10 `；EOL ` RVA 0x33BFB900 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timeout in minutes。

[条件 C-4d65336290c51e2f](../../evidence/conditions-sets-030.md#c-4d65336290c51e2f) · [参数 P-7099650865a13467](../../evidence/parameters-sets-009.md#p-7099650865a13467) · [状态效果 S-d0442b07be0f27f7](../../evidence/state_effects-sets-044.md#s-d0442b07be0f27f7)

### path-029587

```text
(config)# ip auth-proxy max-login-attempts <number:1..2147483647> <cr>
```

Handler ` RVA 0xCBA3DA0 `；selector ` 11 `；EOL ` RVA 0x33BFACA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of login attempts(retries)。

[条件 C-2eed8c4a15167ba2](../../evidence/conditions-sets-018.md#c-2eed8c4a15167ba2) · [参数 P-476206edcaec3bfa](../../evidence/parameters-sets-006.md#p-476206edcaec3bfa) · [状态效果 S-d0442b07be0f27f7](../../evidence/state_effects-sets-044.md#s-d0442b07be0f27f7)

### path-030064

```text
(config)# ip auth-proxy name <string> <cr>
```

Handler ` RVA 0xCBA3DA0 `；selector ` 13 `；EOL ` RVA 0x33BFC650 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of Authentication Rule。

[条件 C-4c09fcd30c7c5410](../../evidence/conditions-sets-030.md#c-4c09fcd30c7c5410) · [参数 P-6fb497f9e2417bc7](../../evidence/parameters-sets-009.md#p-6fb497f9e2417bc7) · [状态效果 S-d0442b07be0f27f7](../../evidence/state_effects-sets-044.md#s-d0442b07be0f27f7)

### path-035879

```text
(config)# ip auth-proxy proxy http refresh-all <cr>
```

Handler ` RVA 0xCBA3DA0 `；selector ` 21 `；EOL ` RVA 0x33BFB158 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-254566f36f9fd550](../../evidence/conditions-sets-015.md#c-254566f36f9fd550) · [状态效果 S-ed0b8cc89b2523ab](../../evidence/state_effects-sets-050.md#s-ed0b8cc89b2523ab)

### path-052971

```text
(config)# ip auth-proxy proxy http success redirect <string> <cr>
```

Handler ` RVA 0xCBA3DA0 `；selector ` 27 `；EOL ` RVA 0x33BFB4F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Specify URL string。

[条件 C-254566f36f9fd550](../../evidence/conditions-sets-015.md#c-254566f36f9fd550) · [参数 P-66aabd8c3ec73bc0](../../evidence/parameters-sets-008.md#p-66aabd8c3ec73bc0) · [状态效果 S-e8eec300ba3c707a](../../evidence/state_effects-sets-049.md#s-e8eec300ba3c707a)

### path-029549

```text
(config)# ip auth-proxy watch-list enable <cr>
```

Handler ` RVA 0xCBA3DA0 `；selector ` 12 `；EOL ` RVA 0x33BFA7E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-254566f36f9fd550](../../evidence/conditions-sets-015.md#c-254566f36f9fd550) · [状态效果 S-b0058b6f88c72aa3](../../evidence/state_effects-sets-037.md#s-b0058b6f88c72aa3)

### path-026645

```text
(config)# ip bgp-community new-format <cr>
```

Handler ` RVA 0xF247E30 `；selector ` 0 `；EOL ` RVA 0x344CDB30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027004

```text
(config)# ip bootp server <cr>
```

Handler ` RVA 0xD344B60 `；selector ` 0 `；EOL ` RVA 0x33E1B8A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-254566f36f9fd550](../../evidence/conditions-sets-015.md#c-254566f36f9fd550) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-035922

```text
(config)# ip cache-ager <number:0..2147483> <number:2..50> <number:3..100> <cr>
```

Handler ` RVA 0xD49EF70 `；selector ` 0 `；EOL ` RVA 0x33E54A40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` # seconds between ager runs；` unsigned_number ` Fraction of cache to age per run (low memory)；` unsigned_number ` Fraction of cache to age per run (normal)。

[条件 C-43ec6cafced2b4b6](../../evidence/conditions-sets-027.md#c-43ec6cafced2b4b6) · [参数 P-65d7cf093162669f](../../evidence/parameters-sets-008.md#p-65d7cf093162669f) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025824

```text
(config)# ip cache-invalidate-delay <cr>
```

Handler ` RVA 0xD49EF70 `；selector ` 1 `；EOL ` RVA 0x33E54640 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ece767679ad7b20c](../../evidence/conditions-sets-092.md#c-ece767679ad7b20c) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025843

```text
(config)# ip casa <cr>
```

Handler ` RVA 0x11266CB0 `；selector ` 0 `；EOL ` RVA 0x35440AA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-820feb9d81fd8552](../../evidence/conditions-sets-050.md#c-820feb9d81fd8552) · [状态效果 S-e0903bd067ef6082](../../evidence/state_effects-sets-048.md#s-e0903bd067ef6082)

### path-025916

```text
(config)# ip cef <cr>
```

Handler ` RVA 0xB611C10 `；selector ` 0 `；EOL ` RVA 0x337BE528 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9e5d3374a4f5d9f8](../../evidence/conditions-sets-061.md#c-9e5d3374a4f5d9f8) · [状态效果 S-31a5e7b956793656](../../evidence/state_effects-sets-011.md#s-31a5e7b956793656)

### path-027379

```text
(config)# ip cef accounting <cr>
```

Handler ` RVA 0xB3625A0 `；selector ` 0 `；EOL ` RVA 0x337C3568 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0588f36ea5308d65](../../evidence/conditions-sets-003.md#c-0588f36ea5308d65) · [状态效果 S-bf49477263e87a12](../../evidence/state_effects-sets-040.md#s-bf49477263e87a12)

### path-036920

```text
(config)# ip cef load-sharing algorithm original <cr>
```

Handler ` RVA 0xB612230 `；selector ` 0 `；EOL ` RVA 0x337BE908 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-48b2d78dc5caaa50](../../evidence/conditions-sets-029.md#c-48b2d78dc5caaa50) · [状态效果 S-94ac12b1a0fc2f92](../../evidence/state_effects-sets-032.md#s-94ac12b1a0fc2f92)

### path-057633

```text
(config)# ip cef load-sharing key-control dpi default outer-src-ip ignore-outer-port <cr>
```

Handler ` RVA 0xB6122F0 `；selector ` 6 `；EOL ` RVA 0x337BF3E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1efc2873de151d74](../../evidence/conditions-sets-012.md#c-1efc2873de151d74) · [状态效果 S-22cf9c491d499175](../../evidence/state_effects-sets-008.md#s-22cf9c491d499175)

### path-060220

```text
(config)# ip cef load-sharing key-control dpi l2vpn-mac ignore-outer-mac ignore-outer-vlan ignore-outer-ip ignore-outer-port ignore-inner-mac ignore-inner-vlan ignore-inner-ip ignore-inner-port <cr>
```

Handler ` RVA 0xB6122F0 `；selector ` 5 `；EOL ` RVA 0x337BF828 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-74a27dbf97f8c217](../../evidence/conditions-sets-045.md#c-74a27dbf97f8c217) · [状态效果 S-3090522f52e39317](../../evidence/state_effects-sets-011.md#s-3090522f52e39317)

### path-059249

```text
(config)# ip cef load-sharing key-control dpi tunnel-gre outer-src-ip ignore-inner-ip ignore-inner-port <cr>
```

Handler ` RVA 0xB6122F0 `；selector ` 0 `；EOL ` RVA 0x337C0368 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-dd2760e337cc531b](../../evidence/conditions-sets-085.md#c-dd2760e337cc531b) · [状态效果 S-9a41b7eb28125764](../../evidence/state_effects-sets-033.md#s-9a41b7eb28125764)

### path-059239

```text
(config)# ip cef load-sharing key-control dpi tunnel-ipinip outer-src-ip ignore-inner-ip ignore-inner-port <cr>
```

Handler ` RVA 0xB6122F0 `；selector ` 3 `；EOL ` RVA 0x337BFED8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-11686168c935a0a1](../../evidence/conditions-sets-007.md#c-11686168c935a0a1) · [状态效果 S-a31c155c1ad5a741](../../evidence/state_effects-sets-035.md#s-a31c155c1ad5a741)

### path-053955

```text
(config)# ip cef load-sharing key-control dpi tunnel-ipsec ignore-outer-ip <cr>
```

Handler ` RVA 0xB6122F0 `；selector ` 2 `；EOL ` RVA 0x337C07F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0ca343820cc1a171](../../evidence/conditions-sets-005.md#c-0ca343820cc1a171) · [状态效果 S-298dc783030cad0f](../../evidence/state_effects-sets-009.md#s-298dc783030cad0f)

### path-059830

```text
(config)# ip cef load-sharing key-control dpi tunnel-l2tp ignore-outer-ip ignore-outer-port ignore-inner-ip ignore-inner-port <cr>
```

Handler ` RVA 0xB6122F0 `；selector ` 1 `；EOL ` RVA 0x337C0FB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f736a718f30d33bc](../../evidence/conditions-sets-095.md#c-f736a718f30d33bc) · [状态效果 S-9492e8dac46321d6](../../evidence/state_effects-sets-031.md#s-9492e8dac46321d6)

### path-059831

```text
(config)# ip cef load-sharing key-control dpi tunnel-vxlan ignore-outer-ip ignore-outer-port ignore-inner-mac ignore-inner-vlan <cr>
```

Handler ` RVA 0xB6122F0 `；selector ` 4 `；EOL ` RVA 0x337C0B20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9deda6eb5e32593a](../../evidence/conditions-sets-061.md#c-9deda6eb5e32593a) · [状态效果 S-9eb9bafa4c02fa81](../../evidence/state_effects-sets-034.md#s-9eb9bafa4c02fa81)

### path-036622

```text
(config)# ip cef optimize neighbor resolution <cr>
```

Handler ` RVA 0xB60D5B0 `；selector ` 1 `；EOL ` RVA 0x337C3C88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-254566f36f9fd550](../../evidence/conditions-sets-015.md#c-254566f36f9fd550) · [状态效果 S-31a5e7b956793656](../../evidence/state_effects-sets-011.md#s-31a5e7b956793656)

### path-037003

```text
(config)# ip cef table adjacency-prefix override <cr>
```

Handler ` RVA 0xB5C9DE0 `；selector ` 5 `；EOL ` RVA 0x337C2DF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6d97bbe0067e111b](../../evidence/conditions-sets-042.md#c-6d97bbe0067e111b) · [状态效果 S-31a5e7b956793656](../../evidence/state_effects-sets-011.md#s-31a5e7b956793656)

### path-037215

```text
(config)# ip cef table consistency-check auto-repair <cr>
```

Handler ` RVA 0xB5C9DE0 `；selector ` 4 `；EOL ` RVA 0x337C2468 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-01852f2bf6cd160e](../../evidence/conditions-sets-001.md#c-01852f2bf6cd160e) · [状态效果 S-31a5e7b956793656](../../evidence/state_effects-sets-011.md#s-31a5e7b956793656)

### path-036957

```text
(config)# ip cef table consistency-check error-message <cr>
```

Handler ` RVA 0xB5C9DE0 `；selector ` 3 `；EOL ` RVA 0x337C2118 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6d97bbe0067e111b](../../evidence/conditions-sets-042.md#c-6d97bbe0067e111b) · [状态效果 S-31a5e7b956793656](../../evidence/state_effects-sets-011.md#s-31a5e7b956793656)

### path-046460

```text
(config)# ip cef table consistency-check type lc-detect <cr>
```

Handler ` RVA 0xB5C9DE0 `；selector ` 0 `；EOL ` RVA 0x337C1A50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-867e19a0c84fdab8](../../evidence/conditions-sets-052.md#c-867e19a0c84fdab8) · [状态效果 S-3c5f68d095521d87](../../evidence/state_effects-sets-013.md#s-3c5f68d095521d87)

### path-030491

```text
(config)# ip cef table event-log <cr>
```

Handler ` RVA 0xD2CFB40 `；selector ` 0 `；EOL ` RVA 0x337C28E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6d97bbe0067e111b](../../evidence/conditions-sets-042.md#c-6d97bbe0067e111b) · [状态效果 S-307ca05685efb1b9](../../evidence/state_effects-sets-011.md#s-307ca05685efb1b9)

### path-030518

```text
(config)# ip cef table short-mask-protection <cr>
```

Handler ` RVA 0xB5C9DE0 `；selector ` 6 `；EOL ` RVA 0x337C30F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8514ea770f77ddb6](../../evidence/conditions-sets-051.md#c-8514ea770f77ddb6) · [状态效果 S-31a5e7b956793656](../../evidence/state_effects-sets-011.md#s-31a5e7b956793656)

### path-027344

```text
(config)# ip cef traffic-statistics <cr>
```

Handler ` RVA 0xB362360 `；selector ` 0 `；EOL ` RVA 0x337C1578 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6d97bbe0067e111b](../../evidence/conditions-sets-042.md#c-6d97bbe0067e111b) · [状态效果 S-b28babaa58100e26](../../evidence/state_effects-sets-038.md#s-b28babaa58100e26)

### path-025687

```text
(config)# ip classless <cr>
```

Handler ` RVA 0xE1FAC50 `；selector ` 1 `；EOL ` RVA 0x3423D170 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026809

```text
(config)# ip community-list <number:1..99> <cr>
```

Handler ` RVA 0xF248150 `；selector ` 0 `；EOL ` RVA 0x344CE360 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Community list number (standard)。

[条件 C-7a1d9ceee6bef061](../../evidence/conditions-sets-047.md#c-7a1d9ceee6bef061) · [参数 P-34968a3e5c1eb2e2](../../evidence/parameters-sets-004.md#p-34968a3e5c1eb2e2) · [状态效果 S-5ac1ec54abca244c](../../evidence/state_effects-sets-020.md#s-5ac1ec54abca244c)

### path-062785

```text
(config)# ip community-list <number:1..99> deny <?bgp_community_action@555589a22030> <cr>
```

Handler ` RVA 0xF248150 `；selector ` 0 `；EOL ` RVA 0x344CE360 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Community list number (standard)。

[条件 C-5044dd2baf9838ea](../../evidence/conditions-sets-031.md#c-5044dd2baf9838ea) · [缺口 G-4a87df21fd7bd52a](../../evidence/gaps-sets-003.md#g-4a87df21fd7bd52a) · [参数 P-34968a3e5c1eb2e2](../../evidence/parameters-sets-004.md#p-34968a3e5c1eb2e2) · [状态效果 S-47b4600a6d1d9372](../../evidence/state_effects-sets-016.md#s-47b4600a6d1d9372)

### path-036354

```text
(config)# ip ddns update method <string> <cr>
```

Handler ` RVA 0xF47FCA0 `；selector ` 0 `；EOL ` RVA 0x3465BD68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Dynamic DNS update method name。

[条件 C-254566f36f9fd550](../../evidence/conditions-sets-015.md#c-254566f36f9fd550) · [参数 P-2f3b7d460cb4f3ab](../../evidence/parameters-sets-004.md#p-2f3b7d460cb4f3ab) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026467

```text
(config)# ip default-gateway <address> <cr>
```

Handler ` RVA 0xCF2A810 `；selector ` 0 `；EOL ` RVA 0x33D3A758 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP address of default gateway。

[条件 C-54fc6d7279d86f4c](../../evidence/conditions-sets-033.md#c-54fc6d7279d86f4c) · [参数 P-5ab4438869df4e6d](../../evidence/parameters-sets-007.md#p-5ab4438869df4e6d) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026826

```text
(config)# ip default-network <address> <cr>
```

Handler ` RVA 0xE2A52D0 `；selector ` 0 `；EOL ` RVA 0x34290360 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP address of default network。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [参数 P-53dea28df3d24965](../../evidence/parameters-sets-007.md#p-53dea28df3d24965) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-047056

```text
(config)# ip dhcp aaa default username <string> <cr>
```

Handler ` RVA 0xD29B830 `；selector ` 0 `；EOL ` RVA 0x33DDE1C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Default username for non-VRF pool subnet request or release。

[条件 C-e6bd57b9d8dd1b70](../../evidence/conditions-sets-089.md#c-e6bd57b9d8dd1b70) · [参数 P-65b1d2063c5ab157](../../evidence/parameters-sets-008.md#p-65b1d2063c5ab157) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027505

```text
(config)# ip dhcp auto-broadcast <cr>
```

Handler ` RVA 0xD2A9510 `；selector ` 0 `；EOL ` RVA 0x33DDFD90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-254566f36f9fd550](../../evidence/conditions-sets-015.md#c-254566f36f9fd550) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-046642

```text
(config)# ip dhcp binding cleanup interval <number:10..600> <cr>
```

Handler ` RVA 0xD24F380 `；selector ` 0 `；EOL ` RVA 0x33DCF260 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Seconds。

[条件 C-63e286bcb2a2532f](../../evidence/conditions-sets-039.md#c-63e286bcb2a2532f) · [参数 P-ea55e2668ec56b78](../../evidence/parameters-sets-018.md#p-ea55e2668ec56b78) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-030708

```text
(config)# ip dhcp bootp ignore <cr>
```

Handler ` RVA 0xD2A4750 `；selector ` 0 `；EOL ` RVA 0x33DDD3A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-254566f36f9fd550](../../evidence/conditions-sets-015.md#c-254566f36f9fd550) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-030910

```text
(config)# ip dhcp class <string> <cr>
```

Handler ` RVA 0xD2A9DD0 `；selector ` 0 `；EOL ` RVA 0x33DDF388 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Class name。

[条件 C-254566f36f9fd550](../../evidence/conditions-sets-015.md#c-254566f36f9fd550) · [参数 P-6dc1fac5f8052d2f](../../evidence/parameters-sets-009.md#p-6dc1fac5f8052d2f) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-046832

```text
(config)# ip dhcp compatibility lease-query client cisco <cr>
```

Handler ` RVA 0xF479870 `；selector ` 0 `；EOL ` RVA 0x34657EA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2d404410a3971403](../../evidence/conditions-sets-018.md#c-2d404410a3971403) · [状态效果 S-c1e219ea9a6958f1](../../evidence/state_effects-sets-041.md#s-c1e219ea9a6958f1)

### path-046723

```text
(config)# ip dhcp compatibility suboption link-selection cisco <cr>
```

Handler ` RVA 0xD24C6A0 `；selector ` 0 `；EOL ` RVA 0x33DCFE88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fe38414c7a3263e3](../../evidence/conditions-sets-098.md#c-fe38414c7a3263e3) · [状态效果 S-8b237581c48cc941](../../evidence/state_effects-sets-030.md#s-8b237581c48cc941)

### path-030735

```text
(config)# ip dhcp conflict logging <cr>
```

Handler ` RVA 0xD29A8F0 `；selector ` 0 `；EOL ` RVA 0x33DDD6A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-254566f36f9fd550](../../evidence/conditions-sets-015.md#c-254566f36f9fd550) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-030825

```text
(config)# ip dhcp conflict resolution <cr>
```

Handler ` RVA 0xD29A6C0 `；selector ` 0 `；EOL ` RVA 0x33DDD9E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-19367d18e98e0466](../../evidence/conditions-sets-010.md#c-19367d18e98e0466) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-030419

```text
(config)# ip dhcp database <string> <cr>
```

Handler ` RVA 0xD24F940 `；selector ` 0 `；EOL ` RVA 0x33DCA818 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Uniform Resource Locator (URL)。

[条件 C-6e47558a4e3f86be](../../evidence/conditions-sets-043.md#c-6e47558a4e3f86be) · [参数 P-33df33cea3fb669a](../../evidence/parameters-sets-004.md#p-33df33cea3fb669a) · [状态效果 S-fa356d8dd3ef08ee](../../evidence/state_effects-sets-053.md#s-fa356d8dd3ef08ee)

### path-027321

```text
(config)# ip dhcp drop-inform <cr>
```

Handler ` RVA 0xD24CBA0 `；selector ` 0 `；EOL ` RVA 0x33DCB590 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-254566f36f9fd550](../../evidence/conditions-sets-015.md#c-254566f36f9fd550) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-037622

```text
(config)# ip dhcp event-notification interval <number:1..300> <cr>
```

Handler ` RVA 0xD29A560 `；selector ` 0 `；EOL ` RVA 0x33DDDDE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Seconds。

[条件 C-230ee797c3b104a5](../../evidence/conditions-sets-014.md#c-230ee797c3b104a5) · [参数 P-e66d09d158c2f210](../../evidence/parameters-sets-017.md#p-e66d09d158c2f210) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-030870

```text
(config)# ip dhcp excluded-address <address> <cr>
```

Handler ` RVA 0xD29B520 `；selector ` 0 `；EOL ` RVA 0x33DDE5B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Low IP address。

[条件 C-254566f36f9fd550](../../evidence/conditions-sets-015.md#c-254566f36f9fd550) · [参数 P-2c73b37dfc1bbeaa](../../evidence/parameters-sets-004.md#p-2c73b37dfc1bbeaa) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027510

```text
(config)# ip dhcp global-options <cr>
```

Handler ` RVA 0xD2ACE90 `；selector ` 0 `；EOL ` RVA 0x33DDFB18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-254566f36f9fd550](../../evidence/conditions-sets-015.md#c-254566f36f9fd550) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-037286

```text
(config)# ip dhcp hardware-class <string> <string> <cr>
```

Handler ` RVA 0xD2502C0 `；selector ` 0 `；EOL ` RVA 0x33DCF608 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` MAC address；` string ` DHCP class name。

[条件 C-543994f636dfc7f1](../../evidence/conditions-sets-033.md#c-543994f636dfc7f1) · [参数 P-1be9eb20a5bf0ea7](../../evidence/parameters-sets-003.md#p-1be9eb20a5bf0ea7) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-062930

```text
(config)# ip dhcp hardware-class <string> <string> delay <number:1..5> <interface> <interface> class-ok offer-ok <cr>
```

Handler ` RVA 0xD2502C0 `；selector ` 0 `；EOL ` RVA 0x33DCF608 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` MAC address；` string ` DHCP class name；` unsigned_number ` Delay seconds。

[条件 C-dc25d6c6c676a0b0](../../evidence/conditions-sets-085.md#c-dc25d6c6c676a0b0) · [缺口 G-4e47ae16455e16ef](../../evidence/gaps-sets-003.md#g-4e47ae16455e16ef) · [参数 P-0ba1b6500c61d1fe](../../evidence/parameters-sets-001.md#p-0ba1b6500c61d1fe) · [状态效果 S-d9e80cab2713b334](../../evidence/state_effects-sets-046.md#s-d9e80cab2713b334)

### path-036817

```text
(config)# ip dhcp limit lease log <cr>
```

Handler ` RVA 0xD24EE80 `；selector ` 0 `；EOL ` RVA 0x33DCB038 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-254566f36f9fd550](../../evidence/conditions-sets-015.md#c-254566f36f9fd550) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-053674

```text
(config)# ip dhcp limit lease per interface <number:1..65535> <cr>
```

Handler ` RVA 0xD24ECC0 `；selector ` 0 `；EOL ` RVA 0x33DCADA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of dhcp lease per interface。

[条件 C-06d9dfdebc14ab81](../../evidence/conditions-sets-003.md#c-06d9dfdebc14ab81) · [参数 P-7dcea99412aa2a78](../../evidence/parameters-sets-010.md#p-7dcea99412aa2a78) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027310

```text
(config)# ip dhcp limited-broadcast-address <cr>
```

Handler ` RVA 0xD24CC80 `；selector ` 0 `；EOL ` RVA 0x33DCB2E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-254566f36f9fd550](../../evidence/conditions-sets-015.md#c-254566f36f9fd550) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-053796

```text
(config)# ip dhcp monitor statistics start sample-size <number:0..4294967295> <cr>
```

Handler ` RVA 0xD24C820 `；selector ` 0 `；EOL ` RVA 0x33DCBFF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of packets。

[条件 C-254566f36f9fd550](../../evidence/conditions-sets-015.md#c-254566f36f9fd550) · [参数 P-ec852188624d3249](../../evidence/parameters-sets-018.md#p-ec852188624d3249) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-037051

```text
(config)# ip dhcp monitor statistics stop <cr>
```

Handler ` RVA 0xD24C820 `；selector ` 1 `；EOL ` RVA 0x33DCC290 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-254566f36f9fd550](../../evidence/conditions-sets-015.md#c-254566f36f9fd550) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-030927

```text
(config)# ip dhcp ping packets <cr>
```

Handler ` RVA 0xD29B9D0 `；selector ` 0 `；EOL ` RVA 0x33DDE9B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-829225eda6be129b](../../evidence/conditions-sets-051.md#c-829225eda6be129b) · [状态效果 S-4d460f62f1d75ffc](../../evidence/state_effects-sets-017.md#s-4d460f62f1d75ffc)

### path-037796

```text
(config)# ip dhcp ping timeout <number:100..10000> <cr>
```

Handler ` RVA 0xD29BB10 `；selector ` 0 `；EOL ` RVA 0x33DDECD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Ping timeout in milliseconds。

[条件 C-0dfd4bb18eaea1c1](../../evidence/conditions-sets-006.md#c-0dfd4bb18eaea1c1) · [参数 P-b858c0360025bfd9](../../evidence/parameters-sets-014.md#p-b858c0360025bfd9) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-030882

```text
(config)# ip dhcp pool <string> <cr>
```

Handler ` RVA 0xD29E450 `；selector ` 0 `；EOL ` RVA 0x33DDF040 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Pool name。

[条件 C-254566f36f9fd550](../../evidence/conditions-sets-015.md#c-254566f36f9fd550) · [参数 P-a023d5b12b7ea4f7](../../evidence/parameters-sets-012.md#p-a023d5b12b7ea4f7) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-037066

```text
(config)# ip dhcp relay bootp ignore <cr>
```

Handler ` RVA 0xD24B760 `；selector ` 0 `；EOL ` RVA 0x33DCC648 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-254566f36f9fd550](../../evidence/conditions-sets-015.md#c-254566f36f9fd550) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-037194

```text
(config)# ip dhcp relay information check <cr>
```

Handler ` RVA 0xD24E360 `；selector ` 0 `；EOL ` RVA 0x33DCD648 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3ec7be0ab91bba1c](../../evidence/conditions-sets-024.md#c-3ec7be0ab91bba1c) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-037160

```text
(config)# ip dhcp relay information option <cr>
```

Handler ` RVA 0xD24CE50 `；selector ` 0 `；EOL ` RVA 0x33DCCA08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-01cd930a20694f28](../../evidence/conditions-sets-001.md#c-01cd930a20694f28) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-046525

```text
(config)# ip dhcp relay information option vpn <cr>
```

Handler ` RVA 0xD24CD60 `；selector ` 0 `；EOL ` RVA 0x33DCC9E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-01cd930a20694f28](../../evidence/conditions-sets-001.md#c-01cd930a20694f28) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-046643

```text
(config)# ip dhcp relay information policy drop <cr>
```

Handler ` RVA 0xD24C520 `；selector ` 0 `；EOL ` RVA 0x33DCCFA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2d3397447d2c4c60](../../evidence/conditions-sets-018.md#c-2d3397447d2c4c60) · [状态效果 S-bb8ddb4bbc724735](../../evidence/state_effects-sets-040.md#s-bb8ddb4bbc724735)

### path-046578

```text
(config)# ip dhcp relay information removal pad <cr>
```

Handler ` RVA 0xD24EBD0 `；selector ` 0 `；EOL ` RVA 0x33DCD3B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4eca542f51b9a3d8](../../evidence/conditions-sets-031.md#c-4eca542f51b9a3d8) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-037236

```text
(config)# ip dhcp relay information trust-all <cr>
```

Handler ` RVA 0xD24E270 `；selector ` 0 `；EOL ` RVA 0x33DCD8F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3ec7be0ab91bba1c](../../evidence/conditions-sets-024.md#c-3ec7be0ab91bba1c) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-046523

```text
(config)# ip dhcp relay override giaddr link-selection <cr>
```

Handler ` RVA 0xD251CA0 `；selector ` 0 `；EOL ` RVA 0x33DCDC30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-254566f36f9fd550](../../evidence/conditions-sets-015.md#c-254566f36f9fd550) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027407

```text
(config)# ip dhcp remember <cr>
```

Handler ` RVA 0xD2522B0 `；selector ` 0 `；EOL ` RVA 0x33DD04F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-254566f36f9fd550](../../evidence/conditions-sets-015.md#c-254566f36f9fd550) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-030401

```text
(config)# ip dhcp route static <cr>
```

Handler ` RVA 0xD24C9B0 `；selector ` 0 `；EOL ` RVA 0x33DCBB88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-254566f36f9fd550](../../evidence/conditions-sets-015.md#c-254566f36f9fd550) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027332

```text
(config)# ip dhcp smart-relay <cr>
```

Handler ` RVA 0xD24CAA0 `；selector ` 0 `；EOL ` RVA 0x33DCB840 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-254566f36f9fd550](../../evidence/conditions-sets-015.md#c-254566f36f9fd550) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027500

```text
(config)# ip dhcp snooping <cr>
```

Handler ` RVA 0x15FA3060 `；selector ` 0 `；EOL ` RVA 0x35E7AE78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cd6d319090f64c73](../../evidence/conditions-sets-079.md#c-cd6d319090f64c73) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-037522

```text
(config)# ip dhcp snooping acl <string> <cr>
```

Handler ` RVA 0x15FA3830 `；selector ` 0 `；EOL ` RVA 0x35E78AF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` MAC Access-list name。

[条件 C-254566f36f9fd550](../../evidence/conditions-sets-015.md#c-254566f36f9fd550) · [参数 P-1bcda9dacd870873](../../evidence/parameters-sets-003.md#p-1bcda9dacd870873) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-037781

```text
(config)# ip dhcp snooping bridge-domain <string> <cr>
```

Handler ` RVA 0x15FA3E30 `；selector ` 0 `；EOL ` RVA 0x35E78F50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` DHCP Snooping bd fist number or bd range, example: 1,3-5,7,9-11。

[条件 C-3c52ae4a7e350501](../../evidence/conditions-sets-023.md#c-3c52ae4a7e350501) · [参数 P-895053f2e138d4c7](../../evidence/parameters-sets-011.md#p-895053f2e138d4c7) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-061443

```text
(config)# ip dhcp snooping bridge-domain <string> <number:dynamic> <cr>
```

Handler ` RVA 0x15FA3E30 `；selector ` 0 `；EOL ` RVA 0x35E78F50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` DHCP Snooping bd fist number or bd range, example: 1,3-5,7,9-11；` unsigned_number_dynamic ` DHCP Snooping bd last number。

[条件 C-c1775e754d2d99b8](../../evidence/conditions-sets-075.md#c-c1775e754d2d99b8) · [缺口 G-a08418ff17036372](../../evidence/gaps-sets-006.md#g-a08418ff17036372) · [参数 P-7440ce0fd9639711](../../evidence/parameters-sets-009.md#p-7440ce0fd9639711) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060687

```text
(config)# ip dhcp snooping database <cr>
```

Handler ` RVA 0x15FA9C10 `；selector ` 0 `；EOL ` RVA 0x35E7A3C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-700aa7ccff3c5778](../../evidence/conditions-sets-043.md#c-700aa7ccff3c5778) · [缺口 G-f0ad272d361097e6](../../evidence/gaps-sets-008.md#g-f0ad272d361097e6) · [状态效果 S-8ac2839407c81ce2](../../evidence/state_effects-sets-029.md#s-8ac2839407c81ce2)

### path-047137

```text
(config)# ip dhcp snooping database timeout <number:0..86400> <cr>
```

Handler ` RVA 0x15FA9C10 `；selector ` 0 `；EOL ` RVA 0x35E7A3C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Abort timeout interval。

[条件 C-7f17ee0e61792df6](../../evidence/conditions-sets-049.md#c-7f17ee0e61792df6) · [参数 P-949cf8352a25ca1c](../../evidence/parameters-sets-011.md#p-949cf8352a25ca1c) · [状态效果 S-e693aa049b928752](../../evidence/state_effects-sets-049.md#s-e693aa049b928752)

### path-030682

```text
(config)# ip dhcp snooping glean <cr>
```

Handler ` RVA 0x15FA36D0 `；selector ` 0 `；EOL ` RVA 0x35E787A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-254566f36f9fd550](../../evidence/conditions-sets-015.md#c-254566f36f9fd550) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-037727

```text
(config)# ip dhcp snooping information option <cr>
```

Handler ` RVA 0x15FA4800 `；selector ` 0 `；EOL ` RVA 0x35E79A88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-620f3d920ca0d35a](../../evidence/conditions-sets-038.md#c-620f3d920ca0d35a) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-047005

```text
(config)# ip dhcp snooping information option allow-untrusted <cr>
```

Handler ` RVA 0x15FA4920 `；selector ` 0 `；EOL ` RVA 0x35E79778 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9ed551b0f9241a6e](../../evidence/conditions-sets-061.md#c-9ed551b0f9241a6e) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-054291

```text
(config)# ip dhcp snooping information option format snmp-ifindex <cr>
```

Handler ` RVA 0x15FA50E0 `；selector ` 0 `；EOL ` RVA 0x35E79B08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-684fafb20009bc24](../../evidence/conditions-sets-040.md#c-684fafb20009bc24) · [状态效果 S-674e73034607d354](../../evidence/state_effects-sets-022.md#s-674e73034607d354)

### path-037613

```text
(config)# ip dhcp snooping track host <cr>
```

Handler ` RVA 0x15FA4640 `；selector ` 0 `；EOL ` RVA 0x35E79440 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b20e7f8d115118da](../../evidence/conditions-sets-069.md#c-b20e7f8d115118da) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-037694

```text
(config)# ip dhcp snooping verify mac-address <cr>
```

Handler ` RVA 0x15FA4B90 `；selector ` 0 `；EOL ` RVA 0x35E7A910 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cd6d319090f64c73](../../evidence/conditions-sets-079.md#c-cd6d319090f64c73) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-037741

```text
(config)# ip dhcp snooping verify no-relay-agent-address <cr>
```

Handler ` RVA 0x15FA4D90 `；selector ` 0 `；EOL ` RVA 0x35E7ABB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cd6d319090f64c73](../../evidence/conditions-sets-079.md#c-cd6d319090f64c73) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-047097

```text
(config)# ip dhcp snooping wireless bootp-broadcast enable <cr>
```

Handler ` RVA 0x15FA4C80 `；selector ` 0 `；EOL ` RVA 0x35E7AEF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cd6d319090f64c73](../../evidence/conditions-sets-079.md#c-cd6d319090f64c73) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-030579

```text
(config)# ip dhcp subscriber-id interface-name <cr>
```

Handler ` RVA 0xD2521E0 `；selector ` 0 `；EOL ` RVA 0x33DD0260 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a4aa364e210101c9](../../evidence/conditions-sets-063.md#c-a4aa364e210101c9) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-030672

```text
(config)# ip dhcp support option125-override <cr>
```

Handler ` RVA 0xD250F70 `；selector ` 0 `；EOL ` RVA 0x33DD1048 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-254566f36f9fd550](../../evidence/conditions-sets-015.md#c-254566f36f9fd550) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-030650

```text
(config)# ip dhcp support option55-override <cr>
```

Handler ` RVA 0xD250D80 `；selector ` 0 `；EOL ` RVA 0x33DD0DA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-254566f36f9fd550](../../evidence/conditions-sets-015.md#c-254566f36f9fd550) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-030623

```text
(config)# ip dhcp support sort-pool-name <cr>
```

Handler ` RVA 0xD24EF60 `；selector ` 0 `；EOL ` RVA 0x33DD0AF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-254566f36f9fd550](../../evidence/conditions-sets-015.md#c-254566f36f9fd550) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-037300

```text
(config)# ip dhcp support tunnel unicast <cr>
```

Handler ` RVA 0xD250CA0 `；selector ` 0 `；EOL ` RVA 0x33DD0868 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-254566f36f9fd550](../../evidence/conditions-sets-015.md#c-254566f36f9fd550) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-061435

```text
(config)# ip dhcp test relay enabled <interface> <cr>
```

Handler ` RVA 0xD251070 `；selector ` 0 `；EOL ` RVA 0x33DD1378 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9932a5f8bf6b68e7](../../evidence/conditions-sets-059.md#c-9932a5f8bf6b68e7) · [缺口 G-084540966b32d7c2](../../evidence/gaps-sets-001.md#g-084540966b32d7c2) · [参数 P-0d8461b3289c28f6](../../evidence/parameters-sets-001.md#p-0d8461b3289c28f6) · [状态效果 S-3ca91349987476ef](../../evidence/state_effects-sets-013.md#s-3ca91349987476ef)

### path-037335

```text
(config)# ip dhcp test relay stateless <cr>
```

Handler ` RVA 0xD251070 `；selector ` 0 `；EOL ` RVA 0x33DD1378 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2ad068c6ba457d85](../../evidence/conditions-sets-017.md#c-2ad068c6ba457d85) · [状态效果 S-ee04d5f03e3bbb3a](../../evidence/state_effects-sets-050.md#s-ee04d5f03e3bbb3a)

### path-031025

```text
(config)# ip dhcp update dns <cr>
```

Handler ` RVA 0xD2A4530 `；selector ` 0 `；EOL ` RVA 0x33DDF720 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-92dc8e4d4eb30f7f](../../evidence/conditions-sets-057.md#c-92dc8e4d4eb30f7f) · [状态效果 S-4b0b7b02e2cca0a0](../../evidence/state_effects-sets-016.md#s-4b0b7b02e2cca0a0)

### path-030515

```text
(config)# ip dhcp use class <cr>
```

Handler ` RVA 0xD24F480 `；selector ` 32768 `；EOL ` RVA 0x33DCE020 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-254566f36f9fd550](../../evidence/conditions-sets-015.md#c-254566f36f9fd550) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-037095

```text
(config)# ip dhcp use class aaa <cr>
```

Handler ` RVA 0xD24F480 `；selector ` 32 `；EOL ` RVA 0x33DCDFF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-254566f36f9fd550](../../evidence/conditions-sets-015.md#c-254566f36f9fd550) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-037229

```text
(config)# ip dhcp use hardware-address client-id <cr>
```

Handler ` RVA 0xD252380 `；selector ` 0 `；EOL ` RVA 0x33DCEE58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a376f13e9bdf0efc](../../evidence/conditions-sets-063.md#c-a376f13e9bdf0efc) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-037187

```text
(config)# ip dhcp use subscriber-id client-id <cr>
```

Handler ` RVA 0xD252100 `；selector ` 0 `；EOL ` RVA 0x33DCEB60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5e90dc1f226bf2cc](../../evidence/conditions-sets-037.md#c-5e90dc1f226bf2cc) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-037191

```text
(config)# ip dhcp use vrf connected <cr>
```

Handler ` RVA 0xD24F640 `；selector ` 4194304 `；EOL ` RVA 0x33DCE838 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-254566f36f9fd550](../../evidence/conditions-sets-015.md#c-254566f36f9fd550) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-037147

```text
(config)# ip dhcp use vrf remote <cr>
```

Handler ` RVA 0xD24F640 `；selector ` 8388608 `；EOL ` RVA 0x33DCE590 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-254566f36f9fd550](../../evidence/conditions-sets-015.md#c-254566f36f9fd550) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027232

```text
(config)# ip dhcp-client broadcast-flag <cr>
```

Handler ` RVA 0xF476500 `；selector ` 0 `；EOL ` RVA 0x3464FBB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-254566f36f9fd550](../../evidence/conditions-sets-015.md#c-254566f36f9fd550) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-036733

```text
(config)# ip dhcp-client default-router distance <number:1..255> <cr>
```

Handler ` RVA 0xF476630 `；selector ` 0 `；EOL ` RVA 0x3464FF60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Metric value。

[条件 C-7c7808e0bffedff1](../../evidence/conditions-sets-048.md#c-7c7808e0bffedff1) · [参数 P-11b8c82b13dd89dd](../../evidence/parameters-sets-002.md#p-11b8c82b13dd89dd) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027282

```text
(config)# ip dhcp-client forcerenew <cr>
```

Handler ` RVA 0xF484600 `；selector ` 0 `；EOL ` RVA 0x34650660 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-254566f36f9fd550](../../evidence/conditions-sets-015.md#c-254566f36f9fd550) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-036698

```text
(config)# ip dhcp-client network-discovery informs <number:0..2> <cr>
```

Handler ` RVA 0xF471560 `；selector ` 2 `；EOL ` RVA 0x3464F2E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Maximum number of DHCP Inform transmissions。

[条件 C-b66f48a183d55816](../../evidence/conditions-sets-071.md#c-b66f48a183d55816) · [参数 P-2a868c5cf507206f](../../evidence/parameters-sets-004.md#p-2a868c5cf507206f) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-053551

```text
(config)# ip dhcp-client network-discovery informs <number:0..2> discovers <number:0..2> <cr>
```

Handler ` RVA 0xF471560 `；selector ` 3 `；EOL ` RVA 0x3464F440 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Maximum number of DHCP Inform transmissions；` unsigned_number ` Maximum number of DHCP Discover transmissions。

[条件 C-b66f48a183d55816](../../evidence/conditions-sets-071.md#c-b66f48a183d55816) · [参数 P-758c8f2df04b0149](../../evidence/parameters-sets-009.md#p-758c8f2df04b0149) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-059182

```text
(config)# ip dhcp-client network-discovery informs <number:0..2> discovers <number:0..2> period <number:3..15> <cr>
```

Handler ` RVA 0xF471560 `；selector ` 4 `；EOL ` RVA 0x3464F480 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Maximum number of DHCP Inform transmissions；` unsigned_number ` Maximum number of DHCP Discover transmissions；` unsigned_number ` Timeout (in seconds) between Inform/Discover retransmission。

[条件 C-b66f48a183d55816](../../evidence/conditions-sets-071.md#c-b66f48a183d55816) · [参数 P-f5ab360cca096c76](../../evidence/parameters-sets-018.md#p-f5ab360cca096c76) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-030330

```text
(config)# ip dhcp-client update dns <cr>
```

Handler ` RVA 0xF471840 `；selector ` 0 `；EOL ` RVA 0x34650338 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-254566f36f9fd550](../../evidence/conditions-sets-015.md#c-254566f36f9fd550) · [状态效果 S-5f50714ded5e265d](../../evidence/state_effects-sets-020.md#s-5f50714ded5e265d)

### path-036670

```text
(config)# ip dhcp-relay information option server-override <cr>
```

Handler ` RVA 0xD24E470 `；selector ` 0 `；EOL ` RVA 0x33DC9A58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-254566f36f9fd550](../../evidence/conditions-sets-015.md#c-254566f36f9fd550) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-030337

```text
(config)# ip dhcp-relay short-lease <number:60..3600> <cr>
```

Handler ` RVA 0xD24E5E0 `；selector ` 0 `；EOL ` RVA 0x33DCA418 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Short Lease (T1) in Seconds。

[条件 C-254566f36f9fd550](../../evidence/conditions-sets-015.md#c-254566f36f9fd550) · [参数 P-4204a9d053edc1f4](../../evidence/parameters-sets-006.md#p-4204a9d053edc1f4) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060643

```text
(config)# ip dhcp-relay source-interface <interface> <cr>
```

Handler ` RVA 0xD24E7F0 `；selector ` 0 `；EOL ` RVA 0x33DC9DB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b23cf029491de77d](../../evidence/conditions-sets-069.md#c-b23cf029491de77d) · [缺口 G-f40c48a953a0af55](../../evidence/gaps-sets-008.md#g-f40c48a953a0af55) · [参数 P-b7085a51e318a7e8](../../evidence/parameters-sets-014.md#p-b7085a51e318a7e8) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027295

```text
(config)# ip dhcp-relay validate-reply <cr>
```

Handler ` RVA 0xD250E70 `；selector ` 0 `；EOL ` RVA 0x33DCA0F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-254566f36f9fd550](../../evidence/conditions-sets-015.md#c-254566f36f9fd550) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027270

```text
(config)# ip dhcp-server <address> <cr>
```

Handler ` RVA 0xF470F00 `；selector ` 13 `；EOL ` RVA 0x3464EF38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP address or Name of DHCP server。

[条件 C-1e340c93fb00619c](../../evidence/conditions-sets-012.md#c-1e340c93fb00619c) · [参数 P-8963e571661046eb](../../evidence/parameters-sets-011.md#p-8963e571661046eb) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-036638

```text
(config)# ip dhcp-server query lease check-source <cr>
```

Handler ` RVA 0xF471350 `；selector ` 3 `；EOL ` RVA 0x3464EB78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-254566f36f9fd550](../../evidence/conditions-sets-015.md#c-254566f36f9fd550) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-045994

```text
(config)# ip dhcp-server query lease retries <number:0..5> <cr>
```

Handler ` RVA 0xF471350 `；selector ` 1 `；EOL ` RVA 0x3464E5D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Maximum number of retransmissions。

[条件 C-3a6d78dd1e6b8ace](../../evidence/conditions-sets-023.md#c-3a6d78dd1e6b8ace) · [参数 P-742155260b20288c](../../evidence/parameters-sets-009.md#p-742155260b20288c) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-046039

```text
(config)# ip dhcp-server query lease timeout <number:1..60> <cr>
```

Handler ` RVA 0xF471350 `；selector ` 2 `；EOL ` RVA 0x3464E8F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Time out for each query in seconds。

[条件 C-15de8484cf3ec213](../../evidence/conditions-sets-009.md#c-15de8484cf3ec213) · [参数 P-e111b2d3ba911c00](../../evidence/parameters-sets-017.md#p-e111b2d3ba911c00) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-030065

```text
(config)# ip dhcp-sip capture buffer-size <cr>
```

Handler ` RVA 0x112A93F0 `；selector ` 0 `；EOL ` RVA 0x35449440 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-296bbbde4d3dc97f](../../evidence/conditions-sets-016.md#c-296bbbde4d3dc97f) · [状态效果 S-ce48f0080e0d5cbb](../../evidence/state_effects-sets-044.md#s-ce48f0080e0d5cbb)

### path-029923

```text
(config)# ip dhcp-sip capture dead-session-info <cr>
```

Handler ` RVA 0x112A9260 `；selector ` 0 `；EOL ` RVA 0x354496C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bae3e6a59375e345](../../evidence/conditions-sets-072.md#c-bae3e6a59375e345) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029876

```text
(config)# ip dhcp-sip class <string> <cr>
```

Handler ` RVA 0x112A7C40 `；selector ` 0 `；EOL ` RVA 0x35449058 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Class name \[1-127 characters\]。

[条件 C-254566f36f9fd550](../../evidence/conditions-sets-015.md#c-254566f36f9fd550) · [参数 P-ff960c395e1d6289](../../evidence/parameters-sets-019.md#p-ff960c395e1d6289) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029919

```text
(config)# ip dhcp-sip test sanity <cr>
```

Handler ` RVA 0x112A7B10 `；selector ` 0 `；EOL ` RVA 0x354499A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e3399ea8459d4648](../../evidence/conditions-sets-088.md#c-e3399ea8459d4648) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-044805

```text
(config)# ip dns name-list <number:1..500> deny <string> <cr>
```

Handler ` RVA 0xD16C7F0 `；selector ` 0 `；EOL ` RVA 0x33D98B90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Regular expression name-list number；` string ` A regular-expression to match hostnames。

[条件 C-21e8e6e6f93cf2bb](../../evidence/conditions-sets-013.md#c-21e8e6e6f93cf2bb) · [参数 P-2ef19f0f44e7a94b](../../evidence/parameters-sets-004.md#p-2ef19f0f44e7a94b) · [状态效果 S-93d3351d1e1fde20](../../evidence/state_effects-sets-031.md#s-93d3351d1e1fde20)

### path-052899

```text
(config)# ip dns primary <string> soa <string> <string> <cr>
```

Handler ` RVA 0xD132D70 `；selector ` 1 `；EOL ` RVA 0x33D99990 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` DNS domain name；` string ` DNS primary name server；` string ` DNS mailbox of responsible person。

[条件 C-299dbdf9d26d25ea](../../evidence/conditions-sets-016.md#c-299dbdf9d26d25ea) · [参数 P-aad18a6306a844d1](../../evidence/parameters-sets-013.md#p-aad18a6306a844d1) · [状态效果 S-b80c4c2e285e3d1e](../../evidence/state_effects-sets-039.md#s-b80c4c2e285e3d1e)

### path-026853

```text
(config)# ip dns server <cr>
```

Handler ` RVA 0xD132D70 `；selector ` 2 `；EOL ` RVA 0x33D995F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a028d997d6b15b06](../../evidence/conditions-sets-062.md#c-a028d997d6b15b06) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-052705

```text
(config)# ip dns server queue limit forwarder <number:1..1000000> <cr>
```

Handler ` RVA 0xD1341A0 `；selector ` 0 `；EOL ` RVA 0x33D99010 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Queue size limit (value 0 indicates no limit)。

[条件 C-d53b66f5ac882c42](../../evidence/conditions-sets-082.md#c-d53b66f5ac882c42) · [参数 P-32f0aa131bc9645c](../../evidence/parameters-sets-004.md#p-32f0aa131bc9645c) · [状态效果 S-ca87cd5e72809413](../../evidence/state_effects-sets-043.md#s-ca87cd5e72809413)

### path-035254

```text
(config)# ip dns server view-group <string> <cr>
```

Handler ` RVA 0xD16F070 `；selector ` 0 `；EOL ` RVA 0x33D99378 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` View-list name。

[条件 C-dd6fca899143813b](../../evidence/conditions-sets-085.md#c-dd6fca899143813b) · [参数 P-5fce63025c7014d6](../../evidence/parameters-sets-008.md#p-5fce63025c7014d6) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026906

```text
(config)# ip dns spoofing <cr>
```

Handler ` RVA 0xD132D70 `；selector ` 3 `；EOL ` RVA 0x33D99F88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a028d997d6b15b06](../../evidence/conditions-sets-062.md#c-a028d997d6b15b06) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026837

```text
(config)# ip dns view <cr>
```

Handler ` RVA 0xD135C00 `；selector ` 0 `；EOL ` RVA 0x33D98328 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5a432089ce19ea54](../../evidence/conditions-sets-035.md#c-5a432089ce19ea54) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-028971

```text
(config)# ip dns view-list <string> <cr>
```

Handler ` RVA 0xD16D930 `；selector ` 0 `；EOL ` RVA 0x33D987B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` View-list name。

[条件 C-a028d997d6b15b06](../../evidence/conditions-sets-062.md#c-a028d997d6b15b06) · [参数 P-a6e532bb388edef9](../../evidence/parameters-sets-013.md#p-a6e532bb388edef9) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029744

```text
(config)# ip domain list <string> <cr>
```

Handler ` RVA 0xD136D90 `；selector ` 0 `；EOL ` RVA 0x33D92020 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` A domain name。

[条件 C-65fb6a026ba9dd1f](../../evidence/conditions-sets-039.md#c-65fb6a026ba9dd1f) · [参数 P-0519769a73936e2c](../../evidence/parameters-sets-001.md#p-0519769a73936e2c) · [状态效果 S-47178ce4d6284d14](../../evidence/state_effects-sets-016.md#s-47178ce4d6284d14)

### path-027174

```text
(config)# ip domain lookup <cr>
```

Handler ` RVA 0xD136680 `；selector ` 0 `；EOL ` RVA 0x33D93688 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-254566f36f9fd550](../../evidence/conditions-sets-015.md#c-254566f36f9fd550) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029832

```text
(config)# ip domain lookup nsap <cr>
```

Handler ` RVA 0xD136680 `；selector ` 1 `；EOL ` RVA 0x33D93010 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-254566f36f9fd550](../../evidence/conditions-sets-015.md#c-254566f36f9fd550) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029720

```text
(config)# ip domain lookup recursive <cr>
```

Handler ` RVA 0xD1396F0 `；selector ` 3 `；EOL ` RVA 0x33D92D30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-254566f36f9fd550](../../evidence/conditions-sets-015.md#c-254566f36f9fd550) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060858

```text
(config)# ip domain lookup source-interface <interface> <cr>
```

Handler ` RVA 0xD136680 `；selector ` 2 `；EOL ` RVA 0x33D933A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1df940774a179878](../../evidence/conditions-sets-012.md#c-1df940774a179878) · [缺口 G-1e16f3e029a80d8e](../../evidence/gaps-sets-002.md#g-1e16f3e029a80d8e) · [参数 P-7c85ba5cd332e122](../../evidence/parameters-sets-010.md#p-7c85ba5cd332e122) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-061909

```text
(config)# ip domain lookup vrf <string> source-interface <interface> <cr>
```

Handler ` RVA 0xD136680 `；selector ` 2 `；EOL ` RVA 0x33D937C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` VRF name。

[条件 C-2e4eae9f2e33f435](../../evidence/conditions-sets-018.md#c-2e4eae9f2e33f435) · [缺口 G-f0514d0d6de1e37c](../../evidence/gaps-sets-008.md#g-f0514d0d6de1e37c) · [参数 P-d7fd1b122d1bc5cb](../../evidence/parameters-sets-016.md#p-d7fd1b122d1bc5cb) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029928

```text
(config)# ip domain multicast <string> <cr>
```

Handler ` RVA 0xD136490 `；selector ` 0 `；EOL ` RVA 0x33D94200 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Multicast domain name。

[条件 C-31dad3959d1a708d](../../evidence/conditions-sets-020.md#c-31dad3959d1a708d) · [参数 P-99ac5a5c7f4262de](../../evidence/parameters-sets-012.md#p-99ac5a5c7f4262de) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029976

```text
(config)# ip domain name <string> <cr>
```

Handler ` RVA 0xD1371E0 `；selector ` 0 `；EOL ` RVA 0x33D93EA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Default domain name。

[条件 C-ab0fb12079d4f1c7](../../evidence/conditions-sets-066.md#c-ab0fb12079d4f1c7) · [参数 P-60f20425cadef641](../../evidence/parameters-sets-008.md#p-60f20425cadef641) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029779

```text
(config)# ip domain periodic-resolve <number:30..3000> <cr>
```

Handler ` RVA 0xD139A10 `；selector ` 0 `；EOL ` RVA 0x33D92A40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Periodicity value in minutes (default : 240 minutes)。

[条件 C-1459a20c8bd850ed](../../evidence/conditions-sets-008.md#c-1459a20c8bd850ed) · [参数 P-6a1cb76aef2f8938](../../evidence/parameters-sets-008.md#p-6a1cb76aef2f8938) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029973

```text
(config)# ip domain recursive allow-soa <cr>
```

Handler ` RVA 0xD139850 `；selector ` 4 `；EOL ` RVA 0x33D94810 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-254566f36f9fd550](../../evidence/conditions-sets-015.md#c-254566f36f9fd550) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-036291

```text
(config)# ip domain recursive retry <number:0..100> <cr>
```

Handler ` RVA 0xD139850 `；selector ` 5 `；EOL ` RVA 0x33D94588 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Maximum no. of referrals allowed - default 10。

[条件 C-53aa5b3ac80713b7](../../evidence/conditions-sets-033.md#c-53aa5b3ac80713b7) · [参数 P-004bc45de9aea63a](../../evidence/parameters-sets-001.md#p-004bc45de9aea63a) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029683

```text
(config)# ip domain retry <number:0..100> <cr>
```

Handler ` RVA 0xD139CD0 `；selector ` 0 `；EOL ` RVA 0x33D923A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of retries。

[条件 C-305f5aeaf4973ebc](../../evidence/conditions-sets-019.md#c-305f5aeaf4973ebc) · [参数 P-68dce16753eff95c](../../evidence/parameters-sets-008.md#p-68dce16753eff95c) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026979

```text
(config)# ip domain round-robin <cr>
```

Handler ` RVA 0xD136400 `；selector ` 0 `；EOL ` RVA 0x33D91B98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-254566f36f9fd550](../../evidence/conditions-sets-015.md#c-254566f36f9fd550) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029730

```text
(config)# ip domain timeout <number:1..3600> <cr>
```

Handler ` RVA 0xD139BB0 `；selector ` 0 `；EOL ` RVA 0x33D926F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timeout value in seconds。

[条件 C-b6d2ae2c98249116](../../evidence/conditions-sets-071.md#c-b6d2ae2c98249116) · [参数 P-63ff9f4f01697e73](../../evidence/parameters-sets-008.md#p-63ff9f4f01697e73) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-028494

```text
(config)# ip drp access-group <number:1..99> <cr>
```

Handler ` RVA 0xF4EDED0 `；selector ` 0 `；EOL ` RVA 0x34679670 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Access-list number。

[条件 C-fede4568ee1ef5bc](../../evidence/conditions-sets-098.md#c-fede4568ee1ef5bc) · [参数 P-527dbe1ed008372c](../../evidence/parameters-sets-007.md#p-527dbe1ed008372c) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-034615

```text
(config)# ip drp authentication key-chain <string> <cr>
```

Handler ` RVA 0xF4EDED0 `；selector ` 1 `；EOL ` RVA 0x34679A48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of key-chain。

[条件 C-1444fe167e899f76](../../evidence/conditions-sets-008.md#c-1444fe167e899f76) · [参数 P-23f4e5e46d533f77](../../evidence/parameters-sets-003.md#p-23f4e5e46d533f77) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026501

```text
(config)# ip drp delay <cr>
```

Handler ` RVA 0xF4EDDE0 `；selector ` 0 `；EOL ` RVA 0x34679300 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-028575

```text
(config)# ip drp drp-rtt <number:1..10000> <cr>
```

Handler ` RVA 0xF4EDED0 `；selector ` 3 `；EOL ` RVA 0x3467A080 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` rtt value in msecs。

[条件 C-0f1605591b1c3206](../../evidence/conditions-sets-006.md#c-0f1605591b1c3206) · [参数 P-a27ae1d483cf22f7](../../evidence/parameters-sets-012.md#p-a27ae1d483cf22f7) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-034761

```text
(config)# ip drp rttprobe destinationport <number:1..65535> <cr>
```

Handler ` RVA 0xF4EDED0 `；selector ` 6 `；EOL ` RVA 0x3467A7D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Specify port number。

[条件 C-395bb627ae4fc462](../../evidence/conditions-sets-022.md#c-395bb627ae4fc462) · [参数 P-6067b967de10704d](../../evidence/parameters-sets-008.md#p-6067b967de10704d) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-034720

```text
(config)# ip drp rttprobe sourceport dynamic <cr>
```

Handler ` RVA 0xF4EDED0 `；selector ` 5 `；EOL ` RVA 0x3467A410 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-949a2894dfdf7bb3](../../evidence/conditions-sets-057.md#c-949a2894dfdf7bb3) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026580

```text
(config)# ip drp server <cr>
```

Handler ` RVA 0xF4EDED0 `；selector ` 2 `；EOL ` RVA 0x34679D40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026735

```text
(config)# ip extcommunity-list <number:1..99> <cr>
```

Handler ` RVA 0xE2463F0 `；selector ` 0 `；EOL ` RVA 0x344CD4F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Extended Community list number (standard)。

[条件 C-b3182f5677158d26](../../evidence/conditions-sets-069.md#c-b3182f5677158d26) · [参数 P-b790d463e5850170](../../evidence/parameters-sets-014.md#p-b790d463e5850170) · [状态效果 S-fa8d98a5ca552e54](../../evidence/state_effects-sets-053.md#s-fa8d98a5ca552e54)

### path-060569

```text
(config)# ip extcommunity-list <number:1..99> deny <cr>
```

Handler ` RVA 0xE2463F0 `；selector ` 0 `；EOL ` RVA 0x344CD4F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Extended Community list number (standard)。

[条件 C-3a74cb8dc2847026](../../evidence/conditions-sets-023.md#c-3a74cb8dc2847026) · [缺口 G-cfe5c17526a7b707](../../evidence/gaps-sets-007.md#g-cfe5c17526a7b707) · [参数 P-b790d463e5850170](../../evidence/parameters-sets-014.md#p-b790d463e5850170) · [状态效果 S-e92d71db1dd6064b](../../evidence/state_effects-sets-049.md#s-e92d71db1dd6064b)

### path-025706

```text
(config)# ip finger <cr>
```

Handler ` RVA 0xCE0E150 `；selector ` 0 `；EOL ` RVA 0x33CFAC98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026573

```text
(config)# ip finger rfc-compliant <cr>
```

Handler ` RVA 0xCE0E150 `；selector ` 1 `；EOL ` RVA 0x33CFAC70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026596

```text
(config)# ip forward-protocol sdns <cr>
```

Handler ` RVA 0xCE49340 `；selector ` 0 `；EOL ` RVA 0x3423D828 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [状态效果 S-45bd4991298a1447](../../evidence/state_effects-sets-015.md#s-45bd4991298a1447)

### path-060551

```text
(config)# ip forward-protocol udp <?udpport_action@555589791d10> <cr>
```

Handler ` RVA 0xCE49340 `；selector ` 0 `；EOL ` RVA 0x3423D828 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [缺口 G-1218ddbce265405e](../../evidence/gaps-sets-001.md#g-1218ddbce265405e) · [状态效果 S-049327773cca0a39](../../evidence/state_effects-sets-001.md#s-049327773cca0a39)

### path-026696

```text
(config)# ip ftp passive <cr>
```

Handler ` RVA 0xD018330 `；selector ` 0 `；EOL ` RVA 0x33D859C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029208

```text
(config)# ip ftp password <string> <cr>
```

Handler ` RVA 0xD018330 `；selector ` 3 `；EOL ` RVA 0x33D86458 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` The cleartext FTP Password 。

[条件 C-8f61f480e5db25c5](../../evidence/conditions-sets-056.md#c-8f61f480e5db25c5) · [参数 P-f960c791fa4ca371](../../evidence/parameters-sets-019.md#p-f960c791fa4ca371) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060561

```text
(config)# ip ftp source-interface <interface> <cr>
```

Handler ` RVA 0xD018330 `；selector ` 1 `；EOL ` RVA 0x33D85D30 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-bb952dafc615cb75](../../evidence/conditions-sets-072.md#c-bb952dafc615cb75) · [缺口 G-f9755288dd42c3db](../../evidence/gaps-sets-009.md#g-f9755288dd42c3db) · [参数 P-7a9efea951986560](../../evidence/parameters-sets-010.md#p-7a9efea951986560) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-028979

```text
(config)# ip ftp username <string> <cr>
```

Handler ` RVA 0xD018330 `；selector ` 2 `；EOL ` RVA 0x33D86138 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Username。

[条件 C-aee15098e1dac86a](../../evidence/conditions-sets-068.md#c-aee15098e1dac86a) · [参数 P-dd924d6ff14c6607](../../evidence/parameters-sets-017.md#p-dd924d6ff14c6607) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026760

```text
(config)# ip gdp eigrp <cr>
```

Handler ` RVA 0xD46C6F0 `；selector ` 7 `；EOL ` RVA 0x33E4A4D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026817

```text
(config)# ip gdp irdp <cr>
```

Handler ` RVA 0xD46C6F0 `；selector ` 9 `；EOL ` RVA 0x33E4AA88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029015

```text
(config)# ip gdp irdp multicast <cr>
```

Handler ` RVA 0xD46C6F0 `；selector ` 11 `；EOL ` RVA 0x33E4AA60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026782

```text
(config)# ip gdp rip <cr>
```

Handler ` RVA 0xD46C6F0 `；selector ` 6 `；EOL ` RVA 0x33E4A778 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025815

```text
(config)# ip global-nameserver <cr>
```

Handler ` RVA 0xD12D4B0 `；selector ` 0 `；EOL ` RVA 0x33D91870 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-132d2c5a8c2c065b](../../evidence/conditions-sets-008.md#c-132d2c5a8c2c065b) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025744

```text
(config)# ip gratuitous-arps <cr>
```

Handler ` RVA 0xCF2A810 `；selector ` 8 `；EOL ` RVA 0x33D37EF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-607bfa23c7963fb1](../../evidence/conditions-sets-038.md#c-607bfa23c7963fb1) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060640

```text
(config)# ip host <string> <address> <cr>
```

Handler ` RVA 0xD12C800 `；selector ` 0 `；EOL ` RVA 0x33D907C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Name of host；` address ` Host IP address。

[条件 C-89d4a319068dbd14](../../evidence/conditions-sets-053.md#c-89d4a319068dbd14) · [缺口 G-ae3ba2607ed7290e](../../evidence/gaps-sets-006.md#g-ae3ba2607ed7290e) · [参数 P-32be2baf1c3460cd](../../evidence/parameters-sets-004.md#p-32be2baf1c3460cd) · [状态效果 S-0baaba4ddd45a3bc](../../evidence/state_effects-sets-003.md#s-0baaba4ddd45a3bc)

### path-027228

```text
(config)# ip host <string> <cr>
```

Handler ` RVA 0xD12C800 `；selector ` 0 `；EOL ` RVA 0x33D907C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of host。

[条件 C-89d4a319068dbd14](../../evidence/conditions-sets-053.md#c-89d4a319068dbd14) · [参数 P-7cef9e17df97c624](../../evidence/parameters-sets-010.md#p-7cef9e17df97c624) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-045331

```text
(config)# ip host <string> mx <number:0..65535> <string> <cr>
```

Handler ` RVA 0xD12BA10 `；selector ` 0 `；EOL ` RVA 0x33D8F8D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of host；` unsigned_number ` Preference value；` string ` Target MX server hostname。

[条件 C-1108995bc0ba83fd](../../evidence/conditions-sets-007.md#c-1108995bc0ba83fd) · [参数 P-c25749999fe2dd40](../../evidence/parameters-sets-015.md#p-c25749999fe2dd40) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-035925

```text
(config)# ip host <string> ns <string> <cr>
```

Handler ` RVA 0xD12C380 `；selector ` 0 `；EOL ` RVA 0x33D8FF80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of host；` string ` Target NS hostname。

[条件 C-1108995bc0ba83fd](../../evidence/conditions-sets-007.md#c-1108995bc0ba83fd) · [参数 P-139c1fa2ed0479d8](../../evidence/parameters-sets-002.md#p-139c1fa2ed0479d8) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-057199

```text
(config)# ip host <string> srv <number:0..65535> <number:0..65535> <number:0..65535> <string> <cr>
```

Handler ` RVA 0xD12BEB0 `；selector ` 0 `；EOL ` RVA 0x33D8FC98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of host；` unsigned_number ` Priority value；` unsigned_number ` Weight value；` unsigned_number ` Port number；` string ` Target SRV server hostname。

[条件 C-1108995bc0ba83fd](../../evidence/conditions-sets-007.md#c-1108995bc0ba83fd) · [参数 P-e6d6b478dd073243](../../evidence/parameters-sets-017.md#p-e6d6b478dd073243) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-036076

```text
(config)# ip host <string> standby <address> <cr>
```

Handler ` RVA 0xD129960 `；selector ` 0 `；EOL ` RVA 0x33D902B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of host。

[条件 C-fbdf7cf9bce707e1](../../evidence/conditions-sets-097.md#c-fbdf7cf9bce707e1) · [参数 P-46728ae4d792d3dc](../../evidence/parameters-sets-006.md#p-46728ae4d792d3dc) · [状态效果 S-9089e7811fcab4e7](../../evidence/state_effects-sets-031.md#s-9089e7811fcab4e7)

### path-027189

```text
(config)# ip host-list <string> <cr>
```

Handler ` RVA 0xF4871E0 `；selector ` 0 `；EOL ` RVA 0x3465C0B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of host list。

[条件 C-254566f36f9fd550](../../evidence/conditions-sets-015.md#c-254566f36f9fd550) · [参数 P-c12bd330171d9841](../../evidence/parameters-sets-015.md#p-c12bd330171d9841) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026630

```text
(config)# ip host-mode extended <cr>
```

Handler ` RVA 0xCF2A810 `；selector ` 18 `；EOL ` RVA 0x33D34E20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-80c272d8ee8ea122](../../evidence/conditions-sets-050.md#c-80c272d8ee8ea122) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025716

```text
(config)# ip host-routing <cr>
```

Handler ` RVA 0xCF2A810 `；selector ` 1 `；EOL ` RVA 0x33D35240 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0489298d4adc773f](../../evidence/conditions-sets-002.md#c-0489298d4adc773f) · [状态效果 S-a95aeabab872c846](../../evidence/state_effects-sets-036.md#s-a95aeabab872c846)

### path-027033

```text
(config)# ip hostname strict <cr>
```

Handler ` RVA 0xD128EC0 `；selector ` 0 `；EOL ` RVA 0x33D90B98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-132d2c5a8c2c065b](../../evidence/conditions-sets-008.md#c-132d2c5a8c2c065b) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029677

```text
(config)# ip hp-host <string> <address> <cr>
```

Handler ` RVA 0xD129170 `；selector ` 0 `；EOL ` RVA 0x33D90F28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` HP host's name；` address ` IP address of the named host。

[条件 C-a5e903d5aef74a52](../../evidence/conditions-sets-064.md#c-a5e903d5aef74a52) · [参数 P-2a2f0e7370842ae7](../../evidence/parameters-sets-004.md#p-2a2f0e7370842ae7) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025699

```text
(config)# ip hp-probe <cr>
```

Handler ` RVA 0xCF2A810 `；selector ` 23 `；EOL ` RVA 0x33D34690 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-028919

```text
(config)# ip http access-class <number:1..99> <cr>
```

Handler ` RVA 0xD1D5A70 `；selector ` 2 `；EOL ` RVA 0x33DBED10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Access list number。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [参数 P-4dceaeec06180bbf](../../evidence/parameters-sets-006.md#p-4dceaeec06180bbf) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-035155

```text
(config)# ip http access-class ipv4 <number:1..99> <cr>
```

Handler ` RVA 0xD1D5A70 `；selector ` 4 `；EOL ` RVA 0x33DBF0C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` IPV4 Access list number。

[条件 C-132ba1078a17510d](../../evidence/conditions-sets-008.md#c-132ba1078a17510d) · [参数 P-32f5be4f560c5771](../../evidence/parameters-sets-004.md#p-32f5be4f560c5771) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-035316

```text
(config)# ip http access-class ipv4 <string> <cr>
```

Handler ` RVA 0xD1D5A70 `；selector ` 3 `；EOL ` RVA 0x33DBF400 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` IPv4 Access list name。

[条件 C-bfdf351a0b483562](../../evidence/conditions-sets-074.md#c-bfdf351a0b483562) · [参数 P-466321ae34caae78](../../evidence/parameters-sets-006.md#p-466321ae34caae78) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-035201

```text
(config)# ip http access-class ipv6 <string> <cr>
```

Handler ` RVA 0xD1D5A70 `；selector ` 5 `；EOL ` RVA 0x33DBF700 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` IPv6 Access list name。

[条件 C-132ba1078a17510d](../../evidence/conditions-sets-008.md#c-132ba1078a17510d) · [参数 P-5003baf66e45a15b](../../evidence/parameters-sets-007.md#p-5003baf66e45a15b) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-045138

```text
(config)# ip http accounting commands <number:0..15> default <cr>
```

Handler ` RVA 0xD1D5A70 `；selector ` 15 `；EOL ` RVA 0x33DBE880 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Enable level。

[条件 C-99b154e4123d3cbb](../../evidence/conditions-sets-059.md#c-99b154e4123d3cbb) · [参数 P-978e30c7553d0146](../../evidence/parameters-sets-012.md#p-978e30c7553d0146) · [状态效果 S-0d8c427e01e96c28](../../evidence/state_effects-sets-003.md#s-0d8c427e01e96c28)

### path-027001

```text
(config)# ip http active-session-modules <cr>
```

Handler ` RVA 0xD1D5A70 `；selector ` 12 `；EOL ` RVA 0x33DBAEA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cbb5a7e3e7e64964](../../evidence/conditions-sets-078.md#c-cbb5a7e3e7e64964) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-044808

```text
(config)# ip http auth-retry <number:1..65535> time-window <number:1..65535> <cr>
```

Handler ` RVA 0xD1D5A70 `；selector ` 20 `；EOL ` RVA 0x33DBFA60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Retry number；` unsigned_number ` Time window in minutes。

[条件 C-0601a53b18f426b5](../../evidence/conditions-sets-003.md#c-0601a53b18f426b5) · [参数 P-85c8de8e4bbc7e4b](../../evidence/parameters-sets-010.md#p-85c8de8e4bbc7e4b) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029103

```text
(config)# ip http authentication enable <cr>
```

Handler ` RVA 0xD1D5A70 `；selector ` 6 `；EOL ` RVA 0x33DB94C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f0fad82cd5f06de0](../../evidence/conditions-sets-093.md#c-f0fad82cd5f06de0) · [状态效果 S-c016dc559c8fdb83](../../evidence/state_effects-sets-041.md#s-c016dc559c8fdb83)

### path-052923

```text
(config)# ip http client cache ager interval <number:0..60> <cr>
```

Handler ` RVA 0xD1D1EA0 `；selector ` 12 `；EOL ` RVA 0x33DBBF50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Interval in Minutes&lt;0-60&gt;, default is 5。

[条件 C-410ef60c3b128788](../../evidence/conditions-sets-025.md#c-410ef60c3b128788) · [参数 P-256f297d569cc54a](../../evidence/parameters-sets-003.md#p-256f297d569cc54a) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-061888

```text
(config)# ip http client cache memory file <number:dynamic> <cr>
```

Handler ` RVA 0xD1D1EA0 `；selector ` 4 `；EOL ` RVA 0x33DBBBD0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` size of cache memory file in kbytes&lt;1-10&gt;, default is 2。

[条件 C-8adf7d6b917ad8f6](../../evidence/conditions-sets-054.md#c-8adf7d6b917ad8f6) · [缺口 G-a7cfb326645f8781](../../evidence/gaps-sets-006.md#g-a7cfb326645f8781) · [参数 P-541b39a45d940c91](../../evidence/parameters-sets-007.md#p-541b39a45d940c91) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-061886

```text
(config)# ip http client cache memory pool <number:dynamic> <cr>
```

Handler ` RVA 0xD1D1EA0 `；selector ` 3 `；EOL ` RVA 0x33DBB8A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` size of cache memory pool in kbytes &lt;0-100&gt;, default is 100。

[条件 C-6ce5489769ad84e5](../../evidence/conditions-sets-042.md#c-6ce5489769ad84e5) · [缺口 G-2e057c4dac0a0268](../../evidence/gaps-sets-002.md#g-2e057c4dac0a0268) · [参数 P-f379fb28ef328c14](../../evidence/parameters-sets-018.md#p-f379fb28ef328c14) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-035976

```text
(config)# ip http client connection forceclose <cr>
```

Handler ` RVA 0xD1D24E0 `；selector ` 5 `；EOL ` RVA 0x33DBD070 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7e757753c6858679](../../evidence/conditions-sets-049.md#c-7e757753c6858679) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-061890

```text
(config)# ip http client connection idle timeout <number:dynamic> <cr>
```

Handler ` RVA 0xD1D24E0 `；selector ` 10 `；EOL ` RVA 0x33DBCCE8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` HTTP connection idle time-out value in seconds。

[条件 C-6f08f96f17f17f8a](../../evidence/conditions-sets-043.md#c-6f08f96f17f17f8a) · [缺口 G-e06539fa42f06ca2](../../evidence/gaps-sets-008.md#g-e06539fa42f06ca2) · [参数 P-d9f0b653de0553c6](../../evidence/parameters-sets-016.md#p-d9f0b653de0553c6) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-045361

```text
(config)# ip http client connection pipeline-length <number:2..100> <cr>
```

Handler ` RVA 0xD1D24E0 `；selector ` 16 `；EOL ` RVA 0x33DBC9D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` HTTP pipeline length。

[条件 C-76aedb570ef719e3](../../evidence/conditions-sets-046.md#c-76aedb570ef719e3) · [参数 P-c88261439b990258](../../evidence/parameters-sets-015.md#p-c88261439b990258) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-045300

```text
(config)# ip http client connection retry <number:1..5> <cr>
```

Handler ` RVA 0xD1D24E0 `；selector ` 13 `；EOL ` RVA 0x33DBC680 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` HTTP retry count。

[条件 C-6ca2537629616eaf](../../evidence/conditions-sets-042.md#c-6ca2537629616eaf) · [参数 P-71093e64e0dd22d4](../../evidence/parameters-sets-009.md#p-71093e64e0dd22d4) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-045238

```text
(config)# ip http client connection timeout <number:1..60> <cr>
```

Handler ` RVA 0xD1D24E0 `；selector ` 9 `；EOL ` RVA 0x33DBC330 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` HTTP connection time-out value (1-60) in seconds。

[条件 C-43a17938180c707d](../../evidence/conditions-sets-026.md#c-43a17938180c707d) · [参数 P-c3c25b53440d45e1](../../evidence/parameters-sets-015.md#p-c3c25b53440d45e1) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-036180

```text
(config)# ip http client password <string> <cr>
```

Handler ` RVA 0xD1D24E0 `；selector ` 6 `；EOL ` RVA 0x33DBDB30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` The UNENCRYPTED (cleartext) client password。

[条件 C-2a03d9d9c79f0df6](../../evidence/conditions-sets-016.md#c-2a03d9d9c79f0df6) · [参数 P-9c5236cc00dd83fc](../../evidence/parameters-sets-012.md#p-9c5236cc00dd83fc) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-053030

```text
(config)# ip http client proxy-server <string> proxy-port <number:1..65535> <cr>
```

Handler ` RVA 0xD1D24E0 `；selector ` 15 `；EOL ` RVA 0x33DBE028 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Proxy server name；` unsigned_number ` Proxy port number。

[条件 C-99af64e497413743](../../evidence/conditions-sets-059.md#c-99af64e497413743) · [参数 P-904049996e1d726c](../../evidence/parameters-sets-011.md#p-904049996e1d726c) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-045515

```text
(config)# ip http client response timeout <number:1..300> <cr>
```

Handler ` RVA 0xD1D24E0 `；selector ` 1 `；EOL ` RVA 0x33DBE420 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` HTTP Response time-out value (1-300) in seconds。

[条件 C-ec7823ddc127bdfe](../../evidence/conditions-sets-091.md#c-ec7823ddc127bdfe) · [参数 P-3cff61eb67be9c00](../../evidence/parameters-sets-005.md#p-3cff61eb67be9c00) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-030066

```text
(config)# ip http client secure-ciphersuite <cr>
```

Handler ` RVA 0xC49E960 `；selector ` 101 `；EOL ` RVA 0x33A9A430 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-770c21110fc2c549](../../evidence/conditions-sets-046.md#c-770c21110fc2c549) · [状态效果 S-aa09ec017bf21005](../../evidence/state_effects-sets-036.md#s-aa09ec017bf21005)

### path-060839

```text
(config)# ip http client source-interface <interface> <cr>
```

Handler ` RVA 0xD1D24E0 `；selector ` 14 `；EOL ` RVA 0x33DBD3E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-bf598562174f327d](../../evidence/conditions-sets-074.md#c-bf598562174f327d) · [缺口 G-d04a72bdcd3a63b5](../../evidence/gaps-sets-007.md#g-d04a72bdcd3a63b5) · [参数 P-68c88430e90a69bf](../../evidence/parameters-sets-008.md#p-68c88430e90a69bf) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-035815

```text
(config)# ip http client username <string> <cr>
```

Handler ` RVA 0xD1D24E0 `；selector ` 7 `；EOL ` RVA 0x33DBD7E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` username。

[条件 C-a84ac969a5adda01](../../evidence/conditions-sets-065.md#c-a84ac969a5adda01) · [参数 P-f5e325ffecafa2b4](../../evidence/parameters-sets-018.md#p-f5e325ffecafa2b4) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-035581

```text
(config)# ip http digest algorithm md5-sess <cr>
```

Handler ` RVA 0xD1D5A70 `；selector ` 16 `；EOL ` RVA 0x33DBB3C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fe62a0641d777b67](../../evidence/conditions-sets-098.md#c-fe62a0641d777b67) · [状态效果 S-4bc0a7a1d8cc0d90](../../evidence/state_effects-sets-017.md#s-4bc0a7a1d8cc0d90)

### path-029686

```text
(config)# ip http help-path <string> <cr>
```

Handler ` RVA 0xD222FD0 `；selector ` 1 `；EOL ` RVA 0x33DC5018 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` root URL for help pages。

[条件 C-aa01f97d89449a53](../../evidence/conditions-sets-066.md#c-aa01f97d89449a53) · [参数 P-ae9c777c8e39da5b](../../evidence/parameters-sets-013.md#p-ae9c777c8e39da5b) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060572

```text
(config)# ip http max-connections <number:dynamic> <cr>
```

Handler ` RVA 0xD1D5A70 `；selector ` 7 `；EOL ` RVA 0x33DB9C58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Maximum number of concurrent http server connections。

[条件 C-04402b374e96b80f](../../evidence/conditions-sets-002.md#c-04402b374e96b80f) · [缺口 G-87881d722e221073](../../evidence/gaps-sets-005.md#g-87881d722e221073) · [参数 P-4de871128d820b20](../../evidence/parameters-sets-006.md#p-4de871128d820b20) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029634

```text
(config)# ip http path <string> <cr>
```

Handler ` RVA 0xD222FD0 `；selector ` 0 `；EOL ` RVA 0x33DC4CF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` path name for HTML。

[条件 C-b159aec79c964dd4](../../evidence/conditions-sets-069.md#c-b159aec79c964dd4) · [参数 P-91fba8fb88275800](../../evidence/parameters-sets-011.md#p-91fba8fb88275800) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-028817

```text
(config)# ip http port 80 <cr>
```

Handler ` RVA 0xD1D5A70 `；selector ` 1 `；EOL ` RVA 0x33DAFCD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9287345ce04f44c8](../../evidence/conditions-sets-057.md#c-9287345ce04f44c8) · [状态效果 S-a4a31c981d155537](../../evidence/state_effects-sets-035.md#s-a4a31c981d155537)

### path-060597

```text
(config)# ip http secure-port <number:dynamic> <cr>
```

Handler ` RVA 0xC49D1F0 `；selector ` 100 `；EOL ` RVA 0x33A990E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Secure port number range。

[条件 C-0366fe4bc0c96406](../../evidence/conditions-sets-002.md#c-0366fe4bc0c96406) · [缺口 G-3c50557890373e78](../../evidence/gaps-sets-003.md#g-3c50557890373e78) · [参数 P-ec17ae7f5dfb555a](../../evidence/parameters-sets-018.md#p-ec17ae7f5dfb555a) · [状态效果 S-a44bda20032fcdd1](../../evidence/state_effects-sets-035.md#s-a44bda20032fcdd1)

### path-026848

```text
(config)# ip http secure-server <cr>
```

Handler ` RVA 0xC49D1F0 `；selector ` 100 `；EOL ` RVA 0x33A990E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [状态效果 S-85e2127c3aa4ad42](../../evidence/state_effects-sets-028.md#s-85e2127c3aa4ad42)

### path-026711

```text
(config)# ip http server <cr>
```

Handler ` RVA 0xD1D5A70 `；selector ` 0 `；EOL ` RVA 0x33DAF9A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6dd12ae9e7011650](../../evidence/conditions-sets-042.md#c-6dd12ae9e7011650) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060582

```text
(config)# ip http session-idle-timeout <number:dynamic> <cr>
```

Handler ` RVA 0xD1D5A70 `；selector ` 9 `；EOL ` RVA 0x33DBA7C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Maximum value of server session idle timeout。

[条件 C-2902f7d77b2e0d07](../../evidence/conditions-sets-016.md#c-2902f7d77b2e0d07) · [缺口 G-bdb64b1fd6443b28](../../evidence/gaps-sets-007.md#g-bdb64b1fd6443b28) · [参数 P-cce9e4f03658b703](../../evidence/parameters-sets-016.md#p-cce9e4f03658b703) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-035413

```text
(config)# ip http session-module-list <string> <string> <cr>
```

Handler ` RVA 0xD1D5A70 `；selector ` 11 `；EOL ` RVA 0x33DBAB58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Session module list name；` string ` List of comma separated http server session name prefixes。

[条件 C-4cfc299181871259](../../evidence/conditions-sets-030.md#c-4cfc299181871259) · [参数 P-2a3f491c002077c3](../../evidence/parameters-sets-004.md#p-2a3f491c002077c3) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-062912

```text
(config)# ip http timeout-policy idle <number:dynamic> life <number:dynamic> requests <number:1..86400> <cr>
```

Handler ` RVA 0xD1D5A70 `；selector ` 8 `；EOL ` RVA 0x33DBA010 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Connection idle time-out value in seconds；` unsigned_number_dynamic ` Connection life time value in seconds；` unsigned_number ` Maximum number of requests allowed on a http server connection。

[条件 C-4a9ce0589b9d465d](../../evidence/conditions-sets-029.md#c-4a9ce0589b9d465d) · [缺口 G-c2761776f580085e](../../evidence/gaps-sets-007.md#g-c2761776f580085e) · [参数 P-2cea24401293fd5e](../../evidence/parameters-sets-004.md#p-2cea24401293fd5e) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-035365

```text
(config)# ip http timeout-policy linger <number:1..300> <cr>
```

Handler ` RVA 0xD1D5A70 `；selector ` 17 `；EOL ` RVA 0x33DBA460 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` HTTP server connection linger time value (1-60) in seconds。

[条件 C-88ec775493323458](../../evidence/conditions-sets-053.md#c-88ec775493323458) · [参数 P-b209e0077bb4e6c2](../../evidence/parameters-sets-014.md#p-b209e0077bb4e6c2) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-044698

```text
(config)# ip http upload enable path <string> <cr>
```

Handler ` RVA 0xD1D5A70 `；selector ` 18 `；EOL ` RVA 0x33DB0100 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` List of comma separated upload paths。

[条件 C-4d851133106bba5c](../../evidence/conditions-sets-030.md#c-4d851133106bba5c) · [参数 P-3d76a35126ecc685](../../evidence/parameters-sets-005.md#p-3d76a35126ecc685) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-028812

```text
(config)# ip http upload overwrite <cr>
```

Handler ` RVA 0xD1D5A70 `；selector ` 19 `；EOL ` RVA 0x33DB0390 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-028911

```text
(config)# ip icmp od-length enable <cr>
```

Handler ` RVA 0xCF2A810 `；selector ` 21 `；EOL ` RVA 0x33D38B80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0489298d4adc773f](../../evidence/conditions-sets-002.md#c-0489298d4adc773f) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-028970

```text
(config)# ip icmp od-length test <cr>
```

Handler ` RVA 0xCF2A810 `；selector ` 22 `；EOL ` RVA 0x33D38E28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f86f4ccae2f3ab2a](../../evidence/conditions-sets-096.md#c-f86f4ccae2f3ab2a) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-035125

```text
(config)# ip icmp rate-limit unreachable <number:1..4294967295> <cr>
```

Handler ` RVA 0xCF2A810 `；selector ` 9 `；EOL ` RVA 0x33D383F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Once per milliseconds。

[条件 C-2adc0b394c8275ca](../../evidence/conditions-sets-017.md#c-2adc0b394c8275ca) · [参数 P-365938b518037110](../../evidence/parameters-sets-005.md#p-365938b518037110) · [状态效果 S-88db8a896768119f](../../evidence/state_effects-sets-029.md#s-88db8a896768119f)

### path-028977

```text
(config)# ip icmp redirect subnet <cr>
```

Handler ` RVA 0xCF2A810 `；selector ` 10 `；EOL ` RVA 0x33D38848 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a19d3a2f50744e02](../../evidence/conditions-sets-062.md#c-a19d3a2f50744e02) · [状态效果 S-60e15461b0902ba2](../../evidence/state_effects-sets-021.md#s-60e15461b0902ba2)

### path-026965

```text
(config)# ip igmp filter <cr>
```

Handler ` RVA 0xE7AFAF0 `；selector ` 0 `；EOL ` RVA 0x34338E98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-28b7699b9e2c2f44](../../evidence/conditions-sets-016.md#c-28b7699b9e2c2f44) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-035673

```text
(config)# ip igmp immediate-leave group-list <number:1..99> <cr>
```

Handler ` RVA 0xF69DC20 `；selector ` 10 `；EOL ` RVA 0x3472DC38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Access list number。

[条件 C-b3593ae27bc987b5](../../evidence/conditions-sets-069.md#c-b3593ae27bc987b5) · [参数 P-1edfcc0605d8d16b](../../evidence/parameters-sets-003.md#p-1edfcc0605d8d16b) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029478

```text
(config)# ip igmp limit <number:1..64000> <cr>
```

Handler ` RVA 0xF69DC20 `；selector ` 35 `；EOL ` RVA 0x3472D8E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Max Allowed State。

[条件 C-eff3c40ed9d0b0dd](../../evidence/conditions-sets-093.md#c-eff3c40ed9d0b0dd) · [参数 P-2a86194b514df886](../../evidence/parameters-sets-004.md#p-2a86194b514df886) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029415

```text
(config)# ip igmp profile <number:1..4294967295> <cr>
```

Handler ` RVA 0xE7B2B20 `；selector ` 0 `；EOL ` RVA 0x3433A550 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Profile number。

[条件 C-28b7699b9e2c2f44](../../evidence/conditions-sets-016.md#c-28b7699b9e2c2f44) · [参数 P-787f8a89ff310d01](../../evidence/parameters-sets-009.md#p-787f8a89ff310d01) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029461

```text
(config)# ip igmp query disperse <cr>
```

Handler ` RVA 0xF69DC20 `；selector ` 40 `；EOL ` RVA 0x3472E030 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-15fe2066c7d6f376](../../evidence/conditions-sets-009.md#c-15fe2066c7d6f376) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027150

```text
(config)# ip igmp snooping <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 0 `；EOL ` RVA 0x33A46E78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8b1cd8dcf3e6a966](../../evidence/conditions-sets-054.md#c-8b1cd8dcf3e6a966) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-035710

```text
(config)# ip igmp snooping check rtr-alert-option <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 67 `；EOL ` RVA 0x33A43568 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-28b7699b9e2c2f44](../../evidence/conditions-sets-016.md#c-28b7699b9e2c2f44) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-035652

```text
(config)# ip igmp snooping check ttl <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 66 `；EOL ` RVA 0x33A432B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-28b7699b9e2c2f44](../../evidence/conditions-sets-016.md#c-28b7699b9e2c2f44) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-045144

```text
(config)# ip igmp snooping explicit-tracking limit <number:0..128000> <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 73 `；EOL ` RVA 0x33A42C68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Explicit tracking DB limit value。

[条件 C-789d052e4badd4d5](../../evidence/conditions-sets-047.md#c-789d052e4badd4d5) · [参数 P-fd86e1fef08efb87](../../evidence/parameters-sets-019.md#p-fd86e1fef08efb87) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-035948

```text
(config)# ip igmp snooping last-member-query-count <number:1..7> <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 40 `；EOL ` RVA 0x33A44CF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Last member query count。

[条件 C-241a1edf243905f0](../../evidence/conditions-sets-014.md#c-241a1edf243905f0) · [参数 P-95b8b1c809fe4838](../../evidence/parameters-sets-012.md#p-95b8b1c809fe4838) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-036021

```text
(config)# ip igmp snooping last-member-query-interval <number:100..32767> <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 41 `；EOL ` RVA 0x33A45040 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Interval (milliseconds)。

[条件 C-505707797208c9a1](../../evidence/conditions-sets-031.md#c-505707797208c9a1) · [参数 P-7a9b5dc4e0a736d8](../../evidence/parameters-sets-010.md#p-7a9b5dc4e0a736d8) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-030100

```text
(config)# ip igmp snooping querier <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 30 `；EOL ` RVA 0x33A46B90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-adfd542f27122000](../../evidence/conditions-sets-067.md#c-adfd542f27122000) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-045672

```text
(config)# ip igmp snooping querier address <address> <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 32 `；EOL ` RVA 0x33A45788 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IGMP querier source IP address。

[条件 C-2d30d352f83241fe](../../evidence/conditions-sets-018.md#c-2d30d352f83241fe) · [参数 P-8b5ef1b0cc9da917](../../evidence/parameters-sets-011.md#p-8b5ef1b0cc9da917) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-045802

```text
(config)# ip igmp snooping querier max-response-time <number:1..25> <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 34 `；EOL ` RVA 0x33A45E20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` IGMP querier maximum response time (sec)。

[条件 C-c70cabd69bcfa50e](../../evidence/conditions-sets-077.md#c-c70cabd69bcfa50e) · [参数 P-0eec0ffe399a8da2](../../evidence/parameters-sets-002.md#p-0eec0ffe399a8da2) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-045740

```text
(config)# ip igmp snooping querier query-interval <number:1..18000> <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 33 `；EOL ` RVA 0x33A45AD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` IGMP querier query interval (sec)。

[条件 C-d4bacbeca448e4f4](../../evidence/conditions-sets-082.md#c-d4bacbeca448e4f4) · [参数 P-93d36d90ec7f17f1](../../evidence/parameters-sets-011.md#p-93d36d90ec7f17f1) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-057419

```text
(config)# ip igmp snooping querier tcn query count <number:1..10> <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 36 `；EOL ` RVA 0x33A465B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` IGMP querier TCN query count。

[条件 C-c93392e63cbae520](../../evidence/conditions-sets-078.md#c-c93392e63cbae520) · [参数 P-5908c6469238175e](../../evidence/parameters-sets-007.md#p-5908c6469238175e) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-057451

```text
(config)# ip igmp snooping querier tcn query interval <number:1..255> <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 37 `；EOL ` RVA 0x33A468E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` IGMP querier TCN query interval (sec)。

[条件 C-fbb436578fb3cf38](../../evidence/conditions-sets-097.md#c-fbb436578fb3cf38) · [参数 P-3cc93d290691cd04](../../evidence/parameters-sets-005.md#p-3cc93d290691cd04) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-053332

```text
(config)# ip igmp snooping querier timer expiry <number:60..300> <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 35 `；EOL ` RVA 0x33A461B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` IGMP querier other querier time out (sec)。

[条件 C-d4135ae15faa32e6](../../evidence/conditions-sets-082.md#c-d4135ae15faa32e6) · [参数 P-ec1cb1315859ff4a](../../evidence/parameters-sets-018.md#p-ec1cb1315859ff4a) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-045621

```text
(config)# ip igmp snooping querier version <number:1..3> <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 31 `；EOL ` RVA 0x33A45438 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` IGMP version。

[条件 C-09d78d8ba7e42fa6](../../evidence/conditions-sets-004.md#c-09d78d8ba7e42fa6) · [参数 P-2a728ace72d809ff](../../evidence/parameters-sets-004.md#p-2a728ace72d809ff) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029441

```text
(config)# ip igmp snooping report-suppression <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 3 `；EOL ` RVA 0x33A42F68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-28b7699b9e2c2f44](../../evidence/conditions-sets-016.md#c-28b7699b9e2c2f44) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-035876

```text
(config)# ip igmp snooping robustness-variable <number:1..3> <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 38 `；EOL ` RVA 0x33A449A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Robustness Variable number。

[条件 C-65c4a24f968621a1](../../evidence/conditions-sets-039.md#c-65c4a24f968621a1) · [参数 P-c24bd86d415e74ad](../../evidence/parameters-sets-015.md#p-c24bd86d415e74ad) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029756

```text
(config)# ip igmp snooping source-only-learning <cr>
```

Handler ` RVA 0xC30AC40 `；selector ` 0 `；EOL ` RVA 0x33A44650 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b05bb71f08606e8d](../../evidence/conditions-sets-068.md#c-b05bb71f08606e8d) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-045415

```text
(config)# ip igmp snooping source-only-learning age-timer <number:0..2880> <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 16 `；EOL ` RVA 0x33A44388 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Age timer value (minutes)。

[条件 C-5af136afd5c7e74f](../../evidence/conditions-sets-036.md#c-5af136afd5c7e74f) · [参数 P-adfeb9f2e20c4740](../../evidence/parameters-sets-013.md#p-adfeb9f2e20c4740) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-035833

```text
(config)# ip igmp snooping tcn flood <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 44 `；EOL ` RVA 0x33A43C38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-95244248f3af00f3](../../evidence/conditions-sets-058.md#c-95244248f3af00f3) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-057209

```text
(config)# ip igmp snooping tcn flood query count <number:1..10> <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 2 `；EOL ` RVA 0x33A43D18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Count。

[条件 C-df234c1b59b93e5f](../../evidence/conditions-sets-086.md#c-df234c1b59b93e5f) · [参数 P-d0091f43d1071234](../../evidence/parameters-sets-016.md#p-d0091f43d1071234) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-045251

```text
(config)# ip igmp snooping tcn query solicit <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 1 `；EOL ` RVA 0x33A43908 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-28b7699b9e2c2f44](../../evidence/conditions-sets-016.md#c-28b7699b9e2c2f44) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029370

```text
(config)# ip igmp ssm-map enable <cr>
```

Handler ` RVA 0xF6BFCD0 `；selector ` 0 `；EOL ` RVA 0x3472CAC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-15fe2066c7d6f376](../../evidence/conditions-sets-009.md#c-15fe2066c7d6f376) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-052935

```text
(config)# ip igmp ssm-map increment <address> <address> <number:2..16000> <cr>
```

Handler ` RVA 0xF6C0A90 `；selector ` 0 `；EOL ` RVA 0x3472D298 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` SSM group address range starting IP；` address ` SSM source address range starting IP；` unsigned_number ` Number of mappings。

[条件 C-972d39b1dec8f3fb](../../evidence/conditions-sets-058.md#c-972d39b1dec8f3fb) · [参数 P-32f6a73c10ecdd62](../../evidence/parameters-sets-004.md#p-32f6a73c10ecdd62) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-035675

```text
(config)# ip igmp ssm-map query dns <cr>
```

Handler ` RVA 0xF6C1620 `；selector ` 0 `；EOL ` RVA 0x3472D560 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1409c4aaa9cf2c81](../../evidence/conditions-sets-008.md#c-1409c4aaa9cf2c81) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-045121

```text
(config)# ip igmp ssm-map static <number:1..99> <address> <cr>
```

Handler ` RVA 0xF6BFF30 `；selector ` 0 `；EOL ` RVA 0x3472CE40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` SSM group access list number；` address ` SSM source address。

[条件 C-15fe2066c7d6f376](../../evidence/conditions-sets-009.md#c-15fe2066c7d6f376) · [参数 P-8e4358f444d86dc2](../../evidence/parameters-sets-011.md#p-8e4358f444d86dc2) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060620

```text
(config)# ip kerberos source-interface <interface> <cr>
```

Handler ` RVA 0xC3E3030 `；selector ` 15 `；EOL ` RVA 0x33A6ABE8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e7dac4bd27373518](../../evidence/conditions-sets-090.md#c-e7dac4bd27373518) · [缺口 G-964475ab475837e7](../../evidence/gaps-sets-005.md#g-964475ab475837e7) · [参数 P-0bd060a65467155e](../../evidence/parameters-sets-001.md#p-0bd060a65467155e) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026756

```text
(config)# ip large-community-list <number:1..99> <cr>
```

Handler ` RVA 0xF24A8B0 `；selector ` 0 `；EOL ` RVA 0x344CCAC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Community list number (standard)。

[条件 C-a9d4d61e28edaaea](../../evidence/conditions-sets-066.md#c-a9d4d61e28edaaea) · [参数 P-c74fa1af49829e0c](../../evidence/parameters-sets-015.md#p-c74fa1af49829e0c) · [状态效果 S-6fd1fab92139da5c](../../evidence/state_effects-sets-024.md#s-6fd1fab92139da5c)

### path-062780

```text
(config)# ip large-community-list <number:1..99> deny <?bgp_lrgcomm_action@555589a20960> <cr>
```

Handler ` RVA 0xF24A8B0 `；selector ` 0 `；EOL ` RVA 0x344CCAC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Community list number (standard)。

[条件 C-62d6cf058b21d547](../../evidence/conditions-sets-038.md#c-62d6cf058b21d547) · [缺口 G-57010ac0ae9eb476](../../evidence/gaps-sets-003.md#g-57010ac0ae9eb476) · [参数 P-c74fa1af49829e0c](../../evidence/parameters-sets-015.md#p-c74fa1af49829e0c) · [状态效果 S-ee7deb923531b3db](../../evidence/state_effects-sets-050.md#s-ee7deb923531b3db)

### path-060612

```text
(config)# ip ldap source-interface <interface> <cr>
```

Handler ` RVA 0x11ABB9B0 `；selector ` 4 `；EOL ` RVA 0x35611B18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f4b6363d3f4bca62](../../evidence/conditions-sets-094.md#c-f4b6363d3f4bca62) · [缺口 G-7e2a66c0fff129b3](../../evidence/gaps-sets-005.md#g-7e2a66c0fff129b3) · [参数 P-f750ce3d1db3b028](../../evidence/parameters-sets-018.md#p-f750ce3d1db3b028) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-034433

```text
(config)# ip local policy route-map <string> <cr>
```

Handler ` RVA 0xFAD8640 `；selector ` 0 `；EOL ` RVA 0x34804488 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Route map name。

[条件 C-7b414614123edb8e](../../evidence/conditions-sets-048.md#c-7b414614123edb8e) · [参数 P-7b69e73bdfa5c6a5](../../evidence/parameters-sets-010.md#p-7b69e73bdfa5c6a5) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-028464

```text
(config)# ip local pool default <cr>
```

Handler ` RVA 0xCEAD550 `；selector ` 0 `；EOL ` RVA 0x33D17D48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f9eeb0d44cb5fd33](../../evidence/conditions-sets-097.md#c-f9eeb0d44cb5fd33) · [状态效果 S-f9676441481b047c](../../evidence/state_effects-sets-053.md#s-f9676441481b047c)

### path-025833

```text
(config)# ip mfib <cr>
```

Handler ` RVA 0x11903850 `；selector ` 0 `；EOL ` RVA 0x35374460 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-65a14f90bc2e6f6d](../../evidence/conditions-sets-039.md#c-65a14f90bc2e6f6d) · [状态效果 S-0605e4c9a25314ab](../../evidence/state_effects-sets-002.md#s-0605e4c9a25314ab)

### path-027088

```text
(config)# ip mfib logging-ttl <cr>
```

Handler ` RVA 0x119053B0 `；selector ` 0 `；EOL ` RVA 0x35374438 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-65a14f90bc2e6f6d](../../evidence/conditions-sets-039.md#c-65a14f90bc2e6f6d) · [状态效果 S-0605e4c9a25314ab](../../evidence/state_effects-sets-002.md#s-0605e4c9a25314ab)

### path-029458

```text
(config)# ip mrm accept-manager <number:1..99> <cr>
```

Handler ` RVA 0xF665DA0 `；selector ` 0 `；EOL ` RVA 0x347208A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Access list number。

[条件 C-c45f1c2af488f4fe](../../evidence/conditions-sets-076.md#c-c45f1c2af488f4fe) · [参数 P-959f8fdb50fff107](../../evidence/parameters-sets-011.md#p-959f8fdb50fff107) · [状态效果 S-48bede6d012167bf](../../evidence/state_effects-sets-016.md#s-48bede6d012167bf)

### path-029193

```text
(config)# ip mrm manager <string> <cr>
```

Handler ` RVA 0xF66A360 `；selector ` 0 `；EOL ` RVA 0x34720518 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Manager name。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [参数 P-c9b48d0ac47b71b8](../../evidence/parameters-sets-015.md#p-c9b48d0ac47b71b8) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060803

```text
(config)# ip mroute <address> <address> <?router_action_proc_vpn@555589cb5068> <cr>
```

Handler ` RVA 0xF6EC770 `；selector ` 0 `；EOL ` RVA 0x34760C98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Source address；` address ` Network mask。

[条件 C-8f6ffdf07f9a1d1d](../../evidence/conditions-sets-056.md#c-8f6ffdf07f9a1d1d) · [缺口 G-fcf7286d4ba0147f](../../evidence/gaps-sets-009.md#g-fcf7286d4ba0147f) · [参数 P-700fd5c67872c7d2](../../evidence/parameters-sets-009.md#p-700fd5c67872c7d2) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026657

```text
(config)# ip mroute extend-timer <cr>
```

Handler ` RVA 0xF6EC770 `；selector ` 0 `；EOL ` RVA 0x34760C98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c0549575caab113c](../../evidence/conditions-sets-074.md#c-c0549575caab113c) · [状态效果 S-9f0ac1fe477c0da8](../../evidence/state_effects-sets-034.md#s-9f0ac1fe477c0da8)

### path-060817

```text
(config)# ip msdp border sa-address <interface> <cr>
```

Handler ` RVA 0xF7869E0 `；selector ` 8 `；EOL ` RVA 0x3473FB28 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e2662677dab8a9c6](../../evidence/conditions-sets-087.md#c-e2662677dab8a9c6) · [缺口 G-09539b3477d0c3b4](../../evidence/gaps-sets-001.md#g-09539b3477d0c3b4) · [参数 P-e861d7651aef6dca](../../evidence/parameters-sets-017.md#p-e861d7651aef6dca) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-028920

```text
(config)# ip msdp cache-rejected-sa <number:1..32766> <cr>
```

Handler ` RVA 0xF7869E0 `；selector ` 17 `；EOL ` RVA 0x3473E708 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of rejected SA entries to cache 。

[条件 C-c076e97872972ba8](../../evidence/conditions-sets-074.md#c-c076e97872972ba8) · [参数 P-ddfe98eb98a6a73d](../../evidence/parameters-sets-017.md#p-ddfe98eb98a6a73d) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026746

```text
(config)# ip msdp cache-sa-state <cr>
```

Handler ` RVA 0xF7869E0 `；selector ` 3 `；EOL ` RVA 0x3473E410 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9a0d20727c576955](../../evidence/conditions-sets-060.md#c-9a0d20727c576955) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029126

```text
(config)# ip msdp default-peer <address> <cr>
```

Handler ` RVA 0xF7869E0 `；selector ` 7 `；EOL ` RVA 0x3473F7C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Default peer name or address。

[条件 C-84dd7aa1c53512d5](../../evidence/conditions-sets-051.md#c-84dd7aa1c53512d5) · [参数 P-ec1e6f2145479016](../../evidence/parameters-sets-018.md#p-ec1e6f2145479016) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-035355

```text
(config)# ip msdp description <address> <string> <cr>
```

Handler ` RVA 0xF7869E0 `；selector ` 10 `；EOL ` RVA 0x347406B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Peer name or address；` string ` Up to 80 characters describing this peer。

[条件 C-b3426d5857caf7d3](../../evidence/conditions-sets-069.md#c-b3426d5857caf7d3) · [参数 P-2f4f988588011670](../../evidence/parameters-sets-004.md#p-2f4f988588011670) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-028842

```text
(config)# ip msdp filter-sa-request <address> <cr>
```

Handler ` RVA 0xF7869E0 `；selector ` 5 `；EOL ` RVA 0x3473E018 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Peer name or address。

[条件 C-9a0d20727c576955](../../evidence/conditions-sets-060.md#c-9a0d20727c576955) · [参数 P-2bbe1a7809d51b10](../../evidence/parameters-sets-004.md#p-2bbe1a7809d51b10) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-045124

```text
(config)# ip msdp keepalive <address> <number:1..60> <number:1..75> <cr>
```

Handler ` RVA 0xF7869E0 `；selector ` 16 `；EOL ` RVA 0x34741358 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Peer name or address；` unsigned_number ` Send keepalive period in seconds；` unsigned_number ` Maximum time in seconds to wait for a message。

[条件 C-013b7b0e27878149](../../evidence/conditions-sets-001.md#c-013b7b0e27878149) · [参数 P-88e22f9404a68612](../../evidence/parameters-sets-011.md#p-88e22f9404a68612) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-034826

```text
(config)# ip msdp mesh-group <string> <address> <cr>
```

Handler ` RVA 0xF7869E0 `；selector ` 12 `；EOL ` RVA 0x3473DCC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of mesh-group；` address ` Peer name or address。

[条件 C-9a0d20727c576955](../../evidence/conditions-sets-060.md#c-9a0d20727c576955) · [参数 P-5b9ba0b16184c7a2](../../evidence/parameters-sets-007.md#p-5b9ba0b16184c7a2) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026987

```text
(config)# ip msdp new-rpf-rules <cr>
```

Handler ` RVA 0xF7869E0 `；selector ` 18 `；EOL ` RVA 0x34741690 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9a0d20727c576955](../../evidence/conditions-sets-060.md#c-9a0d20727c576955) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060578

```text
(config)# ip msdp originator-id <interface> <cr>
```

Handler ` RVA 0xF7869E0 `；selector ` 13 `；EOL ` RVA 0x3473FF48 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e77fdf2a8da678e6](../../evidence/conditions-sets-089.md#c-e77fdf2a8da678e6) · [缺口 G-e546b3d82e974eed](../../evidence/gaps-sets-008.md#g-e546b3d82e974eed) · [参数 P-cd663caffcd16b2b](../../evidence/parameters-sets-016.md#p-cd663caffcd16b2b) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-044651

```text
(config)# ip msdp password peer <address> <string> <cr>
```

Handler ` RVA 0xF7869E0 `；selector ` 19 `；EOL ` RVA 0x3473D8F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Peer name or address；` string ` The password。

[条件 C-bf6fbcd6ae58aea5](../../evidence/conditions-sets-074.md#c-bf6fbcd6ae58aea5) · [参数 P-cd48f64d73255f74](../../evidence/parameters-sets-016.md#p-cd48f64d73255f74) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-028745

```text
(config)# ip msdp peer <address> <cr>
```

Handler ` RVA 0xF7869E0 `；selector ` 1 `；EOL ` RVA 0x3473D4B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Peer name or address。

[条件 C-9a0d20727c576955](../../evidence/conditions-sets-060.md#c-9a0d20727c576955) · [参数 P-525a2617dc96e95d](../../evidence/parameters-sets-007.md#p-525a2617dc96e95d) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-061250

```text
(config)# ip msdp peer <address> remote-as <?bgp_as4_action@555589c91490> <cr>
```

Handler ` RVA 0xF7869E0 `；selector ` 1 `；EOL ` RVA 0x3473D4B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Peer name or address。

[条件 C-9a0d20727c576955](../../evidence/conditions-sets-060.md#c-9a0d20727c576955) · [缺口 G-1bd8e5b505782a85](../../evidence/gaps-sets-001.md#g-1bd8e5b505782a85) · [参数 P-525a2617dc96e95d](../../evidence/parameters-sets-007.md#p-525a2617dc96e95d) · [状态效果 S-8e081f80a5ce4de8](../../evidence/state_effects-sets-030.md#s-8e081f80a5ce4de8)

### path-026835

```text
(config)# ip msdp redistribute <cr>
```

Handler ` RVA 0xF7869E0 `；selector ` 6 `；EOL ` RVA 0x3473EA20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5889935d1fbd3e09](../../evidence/conditions-sets-035.md#c-5889935d1fbd3e09) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-035339

```text
(config)# ip msdp sa-filter in <address> <cr>
```

Handler ` RVA 0xF7869E0 `；selector ` 2 `；EOL ` RVA 0x3473F0C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Peer name or address。

[条件 C-771b1727e2846bf9](../../evidence/conditions-sets-046.md#c-771b1727e2846bf9) · [参数 P-ad02ed574e25a4de](../../evidence/parameters-sets-013.md#p-ad02ed574e25a4de) · [状态效果 S-24241b0f7f69af5b](../../evidence/state_effects-sets-008.md#s-24241b0f7f69af5b)

### path-035461

```text
(config)# ip msdp sa-limit <address> <number:1..2147483646> <cr>
```

Handler ` RVA 0xF7869E0 `；selector ` 14 `；EOL ` RVA 0x34740CE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Peer name or address；` unsigned_number ` Limit of SAs。

[条件 C-7eed19016fba2d0a](../../evidence/conditions-sets-049.md#c-7eed19016fba2d0a) · [参数 P-d519805eefac3bf8](../../evidence/parameters-sets-016.md#p-d519805eefac3bf8) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029250

```text
(config)# ip msdp shutdown <address> <cr>
```

Handler ` RVA 0xF7869E0 `；selector ` 11 `；EOL ` RVA 0x34740998 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Peer name or address。

[条件 C-9a0d20727c576955](../../evidence/conditions-sets-060.md#c-9a0d20727c576955) · [参数 P-e6cbdb8616560bc6](../../evidence/parameters-sets-017.md#p-e6cbdb8616560bc6) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029372

```text
(config)# ip msdp timer <number:1..60> <cr>
```

Handler ` RVA 0xF7869E0 `；selector ` 15 `；EOL ` RVA 0x34741000 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Connection retry period。

[条件 C-0b7b7f263cdbce06](../../evidence/conditions-sets-005.md#c-0b7b7f263cdbce06) · [参数 P-38c9641a0d500e93](../../evidence/parameters-sets-005.md#p-38c9641a0d500e93) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-035300

```text
(config)# ip msdp ttl-threshold <address> <number:0..255> <cr>
```

Handler ` RVA 0xF7869E0 `；selector ` 9 `；EOL ` RVA 0x34740358 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Peer name or address；` unsigned_number ` TTL Threshold Value。

[条件 C-a42b37b16cf65570](../../evidence/conditions-sets-063.md#c-a42b37b16cf65570) · [参数 P-6e540a50ff3ba197](../../evidence/parameters-sets-009.md#p-6e540a50ff3ba197) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027077

```text
(config)# ip multicast auto-enable <cr>
```

Handler ` RVA 0xF70AE00 `；selector ` 0 `；EOL ` RVA 0x3476E7E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a7bb81c94d4663ad](../../evidence/conditions-sets-065.md#c-a7bb81c94d4663ad) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-046158

```text
(config)# ip multicast bier bidir <address> <string> <cr>
```

Handler ` RVA 0xF850570 `；selector ` 0 `；EOL ` RVA 0x347705C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Group address；` string ` BitString in &lt;BSL&gt;#hex:hex::hex format, examples 256#1::F 128#::F。

[条件 C-eb883723ecf5711a](../../evidence/conditions-sets-091.md#c-eb883723ecf5711a) · [参数 P-fd1e450b19c03172](../../evidence/parameters-sets-019.md#p-fd1e450b19c03172) · [状态效果 S-09e91bf8547f92d1](../../evidence/state_effects-sets-002.md#s-09e91bf8547f92d1)

### path-030301

```text
(config)# ip multicast bier disposition <cr>
```

Handler ` RVA 0xF850570 `；selector ` 1 `；EOL ` RVA 0x347709F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-95daacaf1dd4d3e5](../../evidence/conditions-sets-058.md#c-95daacaf1dd4d3e5) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-030160

```text
(config)# ip multicast bier igmp <cr>
```

Handler ` RVA 0xF850570 `；selector ` 2 `；EOL ` RVA 0x34770040 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-efb36af06c76f882](../../evidence/conditions-sets-093.md#c-efb36af06c76f882) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027094

```text
(config)# ip multicast cache-headers <cr>
```

Handler ` RVA 0xF703D40 `；selector ` 0 `；EOL ` RVA 0x3476E550 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a7bb81c94d4663ad](../../evidence/conditions-sets-065.md#c-a7bb81c94d4663ad) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029763

```text
(config)# ip multicast default-rpf-distance <number:0..255> <cr>
```

Handler ` RVA 0xF6EFBD0 `；selector ` 0 `；EOL ` RVA 0x3476EAF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Distance。

[条件 C-a7bb81c94d4663ad](../../evidence/conditions-sets-065.md#c-a7bb81c94d4663ad) · [参数 P-4c79805934ee5e76](../../evidence/parameters-sets-006.md#p-4c79805934ee5e76) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-030008

```text
(config)# ip multicast group-range <number:1..199> <cr>
```

Handler ` RVA 0xF70FEC0 `；selector ` 0 `；EOL ` RVA 0x3476F828 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Access-list number。

[条件 C-9c594c6c20619e55](../../evidence/conditions-sets-060.md#c-9c594c6c20619e55) · [参数 P-4ada36c286547d99](../../evidence/parameters-sets-006.md#p-4ada36c286547d99) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-053312

```text
(config)# ip multicast heartbeat <address> <number:1..100> <number:1..100> <number:10..3600> <cr>
```

Handler ` RVA 0xF762870 `；selector ` 0 `；EOL ` RVA 0x3476FC18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Group address of the heartbeat；` unsigned_number ` Minimal number of intervals where the heartbeats must be seen；` unsigned_number ` Number of intervals to monitor for heartbeat；` unsigned_number ` Length of intervals in seconds。

[条件 C-fc0c8287ffd66913](../../evidence/conditions-sets-097.md#c-fc0c8287ffd66913) · [参数 P-ad00d9f184a3bc3d](../../evidence/parameters-sets-013.md#p-ad00d9f184a3bc3d) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-045286

```text
(config)# ip multicast limit cost <number:1..199> <number:0..2147483647> <cr>
```

Handler ` RVA 0xF778200 `；selector ` 0 `；EOL ` RVA 0x3476A240 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Standard or Extended IP access list number；` unsigned_number ` Cost associated with Access list。

[条件 C-2d858cb7e9451db2](../../evidence/conditions-sets-018.md#c-2d858cb7e9451db2) · [参数 P-660f07df97837f1c](../../evidence/parameters-sets-008.md#p-660f07df97837f1c) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027112

```text
(config)# ip multicast longest-match <cr>
```

Handler ` RVA 0xF6EBFF0 `；selector ` 0 `；EOL ` RVA 0x3476ED80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a7bb81c94d4663ad](../../evidence/conditions-sets-065.md#c-a7bb81c94d4663ad) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029468

```text
(config)# ip multicast mofrr-dampening-period <number:500..25000> <cr>
```

Handler ` RVA 0xF7095E0 `；selector ` 0 `；EOL ` RVA 0x34769470 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` MoFRR Dampening period in milliseconds。

[条件 C-ced1a8f141d381d0](../../evidence/conditions-sets-080.md#c-ced1a8f141d381d0) · [参数 P-2a24018b97310ae4](../../evidence/parameters-sets-004.md#p-2a24018b97310ae4) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029528

```text
(config)# ip multicast mofrr-max-sw-flows <number:6..2048> <cr>
```

Handler ` RVA 0xF7097F0 `；selector ` 0 `；EOL ` RVA 0x34769788 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` MoFRR Max Data Stream flows。

[条件 C-6501c693b103e72b](../../evidence/conditions-sets-039.md#c-6501c693b103e72b) · [参数 P-5fd8008eef01227a](../../evidence/parameters-sets-008.md#p-5fd8008eef01227a) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029631

```text
(config)# ip multicast mofrr-threshold <number:1..10000> <cr>
```

Handler ` RVA 0xF709B90 `；selector ` 0 `；EOL ` RVA 0x34769DB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` MoFRR Traffic threshold to identify traffic loss。

[条件 C-273afb53b213de63](../../evidence/conditions-sets-015.md#c-273afb53b213de63) · [参数 P-f56ef83e5ac726a3](../../evidence/parameters-sets-018.md#p-f56ef83e5ac726a3) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029584

```text
(config)# ip multicast mofrr-traffic-monitoring-period <number:50..10000> <cr>
```

Handler ` RVA 0xF709980 `；selector ` 0 `；EOL ` RVA 0x34769AA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` MoFRR traffic monitoring period in milliseconds。

[条件 C-feae7249582078c0](../../evidence/conditions-sets-098.md#c-feae7249582078c0) · [参数 P-82309f83b318661a](../../evidence/parameters-sets-010.md#p-82309f83b318661a) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029745

```text
(config)# ip multicast mpls mldp <cr>
```

Handler ` RVA 0xF703FE0 `；selector ` 0 `；EOL ` RVA 0x3476AA30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d0cc5f568e1c0cc7](../../evidence/conditions-sets-080.md#c-d0cc5f568e1c0cc7) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029741

```text
(config)# ip multicast mpls traffic-eng <cr>
```

Handler ` RVA 0xF7048F0 `；selector ` 0 `；EOL ` RVA 0x3476AE70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3f43a8cea5b29513](../../evidence/conditions-sets-025.md#c-3f43a8cea5b29513) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029970

```text
(config)# ip multicast mrinfo-filter <number:1..99> <cr>
```

Handler ` RVA 0xF70A470 `；selector ` 0 `；EOL ` RVA 0x3476F478 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Access-list number。

[条件 C-57bad890ec41c20d](../../evidence/conditions-sets-034.md#c-57bad890ec41c20d) · [参数 P-84750bcc809d51fd](../../evidence/parameters-sets-010.md#p-84750bcc809d51fd) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027156

```text
(config)# ip multicast multipath <cr>
```

Handler ` RVA 0xF6EC360 `；selector ` 0 `；EOL ` RVA 0x3476F0C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a7bb81c94d4663ad](../../evidence/conditions-sets-065.md#c-a7bb81c94d4663ad) · [状态效果 S-3a54eedbae301cf8](../../evidence/state_effects-sets-013.md#s-3a54eedbae301cf8)

### path-045237

```text
(config)# ip multicast redundancy nsf holdtime <number:0..1800> <cr>
```

Handler ` RVA 0xD470740 `；selector ` 1 `；EOL ` RVA 0x33E50C68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Added delay time (seconds) before installing post-switchover mcast state。

[条件 C-9bd0ddc9c1cb19fc](../../evidence/conditions-sets-060.md#c-9bd0ddc9c1cb19fc) · [参数 P-5838c04fc690e30b](../../evidence/parameters-sets-007.md#p-5838c04fc690e30b) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-045195

```text
(config)# ip multicast redundancy routeflush maxtime <number:0..3600> <cr>
```

Handler ` RVA 0xD470740 `；selector ` 0 `；EOL ` RVA 0x33E508C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Expiration time (seconds) for stale pre-switchover mcast state。

[条件 C-de924622d8712672](../../evidence/conditions-sets-086.md#c-de924622d8712672) · [参数 P-555352fc1d1bb933](../../evidence/parameters-sets-007.md#p-555352fc1d1bb933) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029657

```text
(config)# ip multicast redundancy rpf-sync <cr>
```

Handler ` RVA 0xD470740 `；selector ` 2 `；EOL ` RVA 0x33E50FE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-158debb69519388e](../../evidence/conditions-sets-008.md#c-158debb69519388e) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029603

```text
(config)# ip multicast route-limit <number:1..2147483647> <cr>
```

Handler ` RVA 0xF709E10 `；selector ` 0 `；EOL ` RVA 0x3476B288 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` number of routes。

[条件 C-cdd3583c6228373e](../../evidence/conditions-sets-079.md#c-cdd3583c6228373e) · [参数 P-15b59974f1255e25](../../evidence/parameters-sets-002.md#p-15b59974f1255e25) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-035851

```text
(config)# ip multicast rpf backoff disable <cr>
```

Handler ` RVA 0xF709D90 `；selector ` 0 `；EOL ` RVA 0x3476C0A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8b052037f642575d](../../evidence/conditions-sets-054.md#c-8b052037f642575d) · [状态效果 S-e1481f5c73b056ac](../../evidence/state_effects-sets-048.md#s-e1481f5c73b056ac)

### path-035791

```text
(config)# ip multicast rpf default-distance <number:0..255> <cr>
```

Handler ` RVA 0xF6EFBD0 `；selector ` 0 `；EOL ` RVA 0x3476BDB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Distance。

[条件 C-8b052037f642575d](../../evidence/conditions-sets-054.md#c-8b052037f642575d) · [参数 P-56a0384b609507ed](../../evidence/parameters-sets-007.md#p-56a0384b609507ed) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-035900

```text
(config)# ip multicast rpf interval <number:1..30> <cr>
```

Handler ` RVA 0xF709D10 `；selector ` 0 `；EOL ` RVA 0x3476B9C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Seconds。

[条件 C-8b052037f642575d](../../evidence/conditions-sets-054.md#c-8b052037f642575d) · [参数 P-4e9b5c21bc0ad1eb](../../evidence/parameters-sets-006.md#p-4e9b5c21bc0ad1eb) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-036261

```text
(config)# ip multicast rpf mofrr <number:100..199> <cr>
```

Handler ` RVA 0xF7091C0 `；selector ` 0 `；EOL ` RVA 0x3476C4A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Extended Access-list number。

[条件 C-5644b5e783619cc2](../../evidence/conditions-sets-034.md#c-5644b5e783619cc2) · [参数 P-c39f096c59f0c9d0](../../evidence/parameters-sets-015.md#p-c39f096c59f0c9d0) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029585

```text
(config)# ip multicast rpf multitopology <cr>
```

Handler ` RVA 0xF6E4D00 `；selector ` 0 `；EOL ` RVA 0x3476B600 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ed07649872e98b3d](../../evidence/conditions-sets-092.md#c-ed07649872e98b3d) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-036077

```text
(config)# ip multicast rpf proxy disable <cr>
```

Handler ` RVA 0xF761B20 `；selector ` 0 `；EOL ` RVA 0x3476D298 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-14e7201cb44d2136](../../evidence/conditions-sets-008.md#c-14e7201cb44d2136) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-045721

```text
(config)# ip multicast rpf proxy rd vector <cr>
```

Handler ` RVA 0xF762130 `；selector ` 0 `；EOL ` RVA 0x3476D868 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a100d9508629c136](../../evidence/conditions-sets-062.md#c-a100d9508629c136) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-036159

```text
(config)# ip multicast rpf proxy vector <cr>
```

Handler ` RVA 0xF761D50 `；selector ` 0 `；EOL ` RVA 0x3476D540 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-14e7201cb44d2136](../../evidence/conditions-sets-008.md#c-14e7201cb44d2136) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-053136

```text
(config)# ip multicast rpf select global group-list <number:1..99> <cr>
```

Handler ` RVA 0xF705540 `；selector ` 0 `；EOL ` RVA 0x3476CAF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Access-list reference for multicast groups。

[条件 C-0f826442708ab00b](../../evidence/conditions-sets-006.md#c-0f826442708ab00b) · [参数 P-649fd4e545cc88bd](../../evidence/parameters-sets-008.md#p-649fd4e545cc88bd) · [状态效果 S-7e9ec9c8fbd26ffd](../../evidence/state_effects-sets-027.md#s-7e9ec9c8fbd26ffd)

### path-057270

```text
(config)# ip multicast rpf select topology unicast <string> <number:100..199> <cr>
```

Handler ` RVA 0xF6E65D0 `；selector ` 0 `；EOL ` RVA 0x3476CF80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Routing topology instance name；` unsigned_number ` Extended IP access-list reference for multicast address。

[条件 C-caa2ab4fcc4a4abd](../../evidence/conditions-sets-078.md#c-caa2ab4fcc4a4abd) · [参数 P-e5b691439a30a17d](../../evidence/parameters-sets-017.md#p-e5b691439a30a17d) · [状态效果 S-3b8552e6e16f3c0a](../../evidence/state_effects-sets-013.md#s-3b8552e6e16f3c0a)

### path-029746

```text
(config)# ip multicast rpf-check-interval <number:1..10> <cr>
```

Handler ` RVA 0xF709D10 `；selector ` 0 `；EOL ` RVA 0x3476E108 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Seconds。

[条件 C-a7bb81c94d4663ad](../../evidence/conditions-sets-065.md#c-a7bb81c94d4663ad) · [参数 P-fd880d73cee76eac](../../evidence/parameters-sets-019.md#p-fd880d73cee76eac) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029681

```text
(config)# ip multicast rsvp <number:1..199> <cr>
```

Handler ` RVA 0xF6F1390 `；selector ` 0 `；EOL ` RVA 0x3476A618 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Standard or Extended IP access list number。

[条件 C-f569a3809c0c3396](../../evidence/conditions-sets-095.md#c-f569a3809c0c3396) · [参数 P-e66ca94134a48e42](../../evidence/parameters-sets-017.md#p-e66ca94134a48e42) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-052961

```text
(config)# ip multicast topology unicast <string> tid <number:1..4095> <cr>
```

Handler ` RVA 0xF6E5A70 `；selector ` 0 `；EOL ` RVA 0x3476DD10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Routing topology instance name；` unsigned_number ` Multicast topology tid。

[条件 C-f28b29958d89287a](../../evidence/conditions-sets-094.md#c-f28b29958d89287a) · [参数 P-6d52f90c21ef643f](../../evidence/parameters-sets-009.md#p-6d52f90c21ef643f) · [状态效果 S-765c51fa304f6e3e](../../evidence/state_effects-sets-025.md#s-765c51fa304f6e3e)

### path-025791

```text
(config)# ip multicast-routing <cr>
```

Handler ` RVA 0xF700800 `；selector ` 0 `；EOL ` RVA 0x34756800 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-05718ba35a2d7fc6](../../evidence/conditions-sets-002.md#c-05718ba35a2d7fc6) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027119

```text
(config)# ip name-server <address> <cr>
```

Handler ` RVA 0xD12A630 `；selector ` 0 `；EOL ` RVA 0x33D914D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Domain server IP address (maximum of 6)。

[条件 C-132d2c5a8c2c065b](../../evidence/conditions-sets-008.md#c-132d2c5a8c2c065b) · [参数 P-bcd0103b22586721](../../evidence/parameters-sets-014.md#p-bcd0103b22586721) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029529

```text
(config)# ip nat create flow-entries <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 18 `；EOL ` RVA 0x347CA8C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c12576940a492abf](../../evidence/conditions-sets-075.md#c-c12576940a492abf) · [状态效果 S-2935a1f304a10e74](../../evidence/state_effects-sets-009.md#s-2935a1f304a10e74)

### path-035802

```text
(config)# ip nat dia track-enable <number:1..65534> <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 42 `；EOL ` RVA 0x347CAC88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Enter DIA track number。

[条件 C-e63fcdb6c6907073](../../evidence/conditions-sets-089.md#c-e63fcdb6c6907073) · [参数 P-c3d1fd70e890fa12](../../evidence/parameters-sets-015.md#p-c3d1fd70e890fa12) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-057432

```text
(config)# ip nat inside destination list <number:1..2699> pool <string> <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 4 `；EOL ` RVA 0x347D45C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Access list number for global addresses；` string ` Pool name for local addresses。

[条件 C-cea8d6620cfd8194](../../evidence/conditions-sets-080.md#c-cea8d6620cfd8194) · [参数 P-10505f0167cd5432](../../evidence/parameters-sets-002.md#p-10505f0167cd5432) · [状态效果 S-93ea1a1f9da75e5e](../../evidence/state_effects-sets-031.md#s-93ea1a1f9da75e5e)

### path-062289

```text
(config)# ip nat inside source list <number:1..2699> interface <interface> <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 2 `；EOL ` RVA 0x347D0F60 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Access list number for local addresses。

[条件 C-36e2e57eea759cae](../../evidence/conditions-sets-021.md#c-36e2e57eea759cae) · [缺口 G-06b405e7bc4144cd](../../evidence/gaps-sets-001.md#g-06b405e7bc4144cd) · [参数 P-ca5c95b34f214f35](../../evidence/parameters-sets-015.md#p-ca5c95b34f214f35) · [状态效果 S-a734a7241b77cca3](../../evidence/state_effects-sets-035.md#s-a734a7241b77cca3)

### path-053692

```text
(config)# ip nat inside source static <address> <address> <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 2 `；EOL ` RVA 0x347D0F60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Inside local IP address；` address ` Inside global IP address。

[条件 C-b8da344a9fce82e6](../../evidence/conditions-sets-071.md#c-b8da344a9fce82e6) · [参数 P-4b7c8ab8471c220d](../../evidence/parameters-sets-006.md#p-4b7c8ab8471c220d) · [状态效果 S-a734a7241b77cca3](../../evidence/state_effects-sets-035.md#s-a734a7241b77cca3)

### path-029620

```text
(config)# ip nat log translations <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 7 `；EOL ` RVA 0x347C9E70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fc144c8580798abf](../../evidence/conditions-sets-097.md#c-fc144c8580798abf) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-062659

```text
(config)# ip nat log translations flow-export v9 udp destination <address> <number:1..65535> source <interface> <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 7 `；EOL ` RVA 0x347C9E70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Host IP address；` unsigned_number ` Local UDP port。

[条件 C-f0d51ff4401f6cbd](../../evidence/conditions-sets-093.md#c-f0d51ff4401f6cbd) · [缺口 G-0fe0512ac139b646](../../evidence/gaps-sets-001.md#g-0fe0512ac139b646) · [参数 P-0cb4a89897cea5dd](../../evidence/parameters-sets-001.md#p-0cb4a89897cea5dd) · [状态效果 S-389149f929528317](../../evidence/state_effects-sets-013.md#s-389149f929528317)

### path-053659

```text
(config)# ip nat outside source static <address> <address> <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 3 `；EOL ` RVA 0x347D4F30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Outside global IP address；` address ` Outside local IP address。

[条件 C-90216e996d4d8035](../../evidence/conditions-sets-056.md#c-90216e996d4d8035) · [参数 P-442605d7e2d85755](../../evidence/parameters-sets-006.md#p-442605d7e2d85755) · [状态效果 S-4fb340cb757ce03e](../../evidence/state_effects-sets-017.md#s-4fb340cb757ce03e)

### path-062503

```text
(config)# ip nat outside source static network <address> <address> <?ipmask_action@555589d29ea8> <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 3 `；EOL ` RVA 0x347D4F30 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Outside global network；` address ` Outside local network。

[条件 C-027b071ef959865a](../../evidence/conditions-sets-001.md#c-027b071ef959865a) · [缺口 G-4953a625716f5aef](../../evidence/gaps-sets-003.md#g-4953a625716f5aef) · [参数 P-39708a7077ba02bb](../../evidence/parameters-sets-005.md#p-39708a7077ba02bb) · [状态效果 S-4fb340cb757ce03e](../../evidence/state_effects-sets-017.md#s-4fb340cb757ce03e)

### path-045880

```text
(config)# ip nat pool <string> netmask <address> <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 5 `；EOL ` RVA 0x347D0160 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Pool name；` address ` Network mask。

[条件 C-91b5a6b0252eff1d](../../evidence/conditions-sets-056.md#c-91b5a6b0252eff1d) · [参数 P-3e290db05818fe5a](../../evidence/parameters-sets-005.md#p-3e290db05818fe5a) · [状态效果 S-782962661ab9b87a](../../evidence/state_effects-sets-026.md#s-782962661ab9b87a)

### path-057215

```text
(config)# ip nat route vrf <string> <address> <address> global <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 30 `；EOL ` RVA 0x347CB100 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` VPN Routing/Forwarding instance name；` address ` IP address；` address ` Network mask。

[条件 C-4af9f78d194f48e4](../../evidence/conditions-sets-029.md#c-4af9f78d194f48e4) · [参数 P-cb15e1b162af71f6](../../evidence/parameters-sets-015.md#p-cb15e1b162af71f6) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029946

```text
(config)# ip nat service ftp <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 6 `；EOL ` RVA 0x347CEA88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fca532dd4f44adab](../../evidence/conditions-sets-097.md#c-fca532dd4f44adab) · [状态效果 S-af02a70294d8863f](../../evidence/state_effects-sets-037.md#s-af02a70294d8863f)

### path-029506

```text
(config)# ip nat settings central-policy <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 35 `；EOL ` RVA 0x347C51C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f197778bfbe2cbfc](../../evidence/conditions-sets-093.md#c-f197778bfbe2cbfc) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-035771

```text
(config)# ip nat settings cfg-check static-map-removal <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 24 `；EOL ` RVA 0x347C5840 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6e9a271b38c0791a](../../evidence/conditions-sets-043.md#c-6e9a271b38c0791a) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-030233

```text
(config)# ip nat settings fbd <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 39 `；EOL ` RVA 0x347C9298 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e19e271b321299a5](../../evidence/conditions-sets-087.md#c-e19e271b321299a5) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-036026

```text
(config)# ip nat settings gatekeeper-size <number:512..262144> <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 25 `；EOL ` RVA 0x347C5F80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of entries - truncated to power of 2。

[条件 C-98c6493086d65b32](../../evidence/conditions-sets-059.md#c-98c6493086d65b32) · [参数 P-7a981d70958d9e2c](../../evidence/parameters-sets-010.md#p-7a981d70958d9e2c) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-030129

```text
(config)# ip nat settings high-performance <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 34 `；EOL ` RVA 0x347C8980 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-88210d11ea398ba5](../../evidence/conditions-sets-053.md#c-88210d11ea398ba5) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-057341

```text
(config)# ip nat settings interface-overload block port tcp <number:1024..65535> <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 29 `；EOL ` RVA 0x347C7A78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Port number。

[条件 C-7e99b0669cfbb181](../../evidence/conditions-sets-049.md#c-7e99b0669cfbb181) · [参数 P-21361a27615d3ab2](../../evidence/parameters-sets-003.md#p-21361a27615d3ab2) · [状态效果 S-3dcb00cd3959cd94](../../evidence/state_effects-sets-014.md#s-3dcb00cd3959cd94)

### path-059752

```text
(config)# ip nat settings interface-overload port range start <number:1024..65535> end <number:1024..65535> <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 28 `；EOL ` RVA 0x347C7598 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Port number；` unsigned_number ` Port number。

[条件 C-9b7dca89bd484678](../../evidence/conditions-sets-060.md#c-9b7dca89bd484678) · [参数 P-cbfe13c6a0f2e7a0](../../evidence/parameters-sets-015.md#p-cbfe13c6a0f2e7a0) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-030164

```text
(config)# ip nat settings log-destination <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 36 `；EOL ` RVA 0x347C8C88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-38309d6ce514522b](../../evidence/conditions-sets-022.md#c-38309d6ce514522b) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-035813

```text
(config)# ip nat settings mode default <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 21 `；EOL ` RVA 0x347C5B80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-536734e0d587dc66](../../evidence/conditions-sets-033.md#c-536734e0d587dc66) · [状态效果 S-6aefc6d1d7226dbf](../../evidence/state_effects-sets-023.md#s-6aefc6d1d7226dbf)

### path-029910

```text
(config)# ip nat settings nonpatdrop <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 26 `；EOL ` RVA 0x347C6EF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-79c9c0ceb2092998](../../evidence/conditions-sets-047.md#c-79c9c0ceb2092998) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029953

```text
(config)# ip nat settings nonpatlog-disable <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 27 `；EOL ` RVA 0x347C71F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0625f619afad7da0](../../evidence/conditions-sets-003.md#c-0625f619afad7da0) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-030001

```text
(config)# ip nat settings pap <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 22 `；EOL ` RVA 0x347C6718 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7a9082d3796387a8](../../evidence/conditions-sets-048.md#c-7a9082d3796387a8) · [状态效果 S-a5ae2edb83d54a94](../../evidence/state_effects-sets-035.md#s-a5ae2edb83d54a94)

### path-061315

```text
(config)# ip nat settings pap limit <?keyword_option_mm_action@555589d1a778> <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 22 `；EOL ` RVA 0x347C6718 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7a9082d3796387a8](../../evidence/conditions-sets-048.md#c-7a9082d3796387a8) · [缺口 G-ed462a27db75cb5f](../../evidence/gaps-sets-008.md#g-ed462a27db75cb5f) · [状态效果 S-a5ae2edb83d54a94](../../evidence/state_effects-sets-035.md#s-a5ae2edb83d54a94)

### path-053343

```text
(config)# ip nat settings pool watermark high <number:1..100> <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 31 `；EOL ` RVA 0x347C7E70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Percentage。

[条件 C-7c693e21bf727ebd](../../evidence/conditions-sets-048.md#c-7c693e21bf727ebd) · [参数 P-ff5df22ff000247c](../../evidence/parameters-sets-019.md#p-ff5df22ff000247c) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-030269

```text
(config)# ip nat settings preserve-sdwan-ports <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 38 `；EOL ` RVA 0x347C9578 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d59a48a3203e36e2](../../evidence/conditions-sets-082.md#c-d59a48a3203e36e2) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-035631

```text
(config)# ip nat settings redundancy optimized-data-sync <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 41 `；EOL ` RVA 0x347C54D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b3bd65386fb35717](../../evidence/conditions-sets-070.md#c-b3bd65386fb35717) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-030199

```text
(config)# ip nat settings reserve-ports <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 37 `；EOL ` RVA 0x347C8F90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bfe8cf40401b1872](../../evidence/conditions-sets-074.md#c-bfe8cf40401b1872) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-036504

```text
(config)# ip nat settings scale bind <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 33 `；EOL ` RVA 0x347C8668 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2a13ad85a4e5fd0f](../../evidence/conditions-sets-016.md#c-2a13ad85a4e5fd0f) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-061298

```text
(config)# ip nat settings support mapping outside <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 20 `；EOL ` RVA 0x347C63B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-19d927a3d182847c](../../evidence/conditions-sets-010.md#c-19d927a3d182847c) · [缺口 G-6dce35d0c14bd218](../../evidence/gaps-sets-004.md#g-6dce35d0c14bd218) · [状态效果 S-e68a2f0c67254660](../../evidence/state_effects-sets-049.md#s-e68a2f0c67254660)

### path-045840

```text
(config)# ip nat settings trans-err-limit per-ip-pool <number:1..10080> <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 32 `；EOL ` RVA 0x347C82B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Minute(s)。

[条件 C-32ae2f74448b0844](../../evidence/conditions-sets-020.md#c-32ae2f74448b0844) · [参数 P-820a93faaf0b3190](../../evidence/parameters-sets-010.md#p-820a93faaf0b3190) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-035781

```text
(config)# ip nat switchover replication http <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 19 `；EOL ` RVA 0x347C9A50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-da97c5bcf1cedede](../../evidence/conditions-sets-084.md#c-da97c5bcf1cedede) · [状态效果 S-7859a807f9cc3283](../../evidence/state_effects-sets-026.md#s-7859a807f9cc3283)

### path-036298

```text
(config)# ip nat translation finrst-timeout <number:0..536870> <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 0 `；EOL ` RVA 0x347CC0E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timeout in seconds。

[条件 C-601a3dea95975197](../../evidence/conditions-sets-037.md#c-601a3dea95975197) · [参数 P-47c9960d2ea40767](../../evidence/parameters-sets-006.md#p-47c9960d2ea40767) · [状态效果 S-48283d912fc977c3](../../evidence/state_effects-sets-016.md#s-48283d912fc977c3)

### path-036368

```text
(config)# ip nat translation finrst-timeout never <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 0 `；EOL ` RVA 0x347CC190 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-601a3dea95975197](../../evidence/conditions-sets-037.md#c-601a3dea95975197) · [状态效果 S-397c0a9e0d9f2cd2](../../evidence/state_effects-sets-013.md#s-397c0a9e0d9f2cd2)

### path-036544

```text
(config)# ip nat translation icmp-timeout <number:0..536870> <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 0 `；EOL ` RVA 0x347CCFB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timeout in seconds。

[条件 C-f60c6fd9e24d34c6](../../evidence/conditions-sets-095.md#c-f60c6fd9e24d34c6) · [参数 P-026d28e8332cef02](../../evidence/parameters-sets-001.md#p-026d28e8332cef02) · [状态效果 S-94297f069efa1e4d](../../evidence/state_effects-sets-031.md#s-94297f069efa1e4d)

### path-036531

```text
(config)# ip nat translation max-entries <number:1..2147483647> <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 8 `；EOL ` RVA 0x347CD848 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of entries。

[条件 C-7f9db0835c3f1ae7](../../evidence/conditions-sets-049.md#c-7f9db0835c3f1ae7) · [参数 P-f61f3cefbdeeee1c](../../evidence/parameters-sets-018.md#p-f61f3cefbdeeee1c) · [状态效果 S-a575241d4bdb9fc0](../../evidence/state_effects-sets-035.md#s-a575241d4bdb9fc0)

### path-053457

```text
(config)# ip nat translation port-timeout tcp <number:1..65535> <number:0..536870> <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 1 `；EOL ` RVA 0x347CD460 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Port number；` unsigned_number ` Timeout in seconds。

[条件 C-9909652f69d58417](../../evidence/conditions-sets-059.md#c-9909652f69d58417) · [参数 P-0d4470cd2a36950d](../../evidence/parameters-sets-001.md#p-0d4470cd2a36950d) · [状态效果 S-45c235e941d38bc9](../../evidence/state_effects-sets-015.md#s-45c235e941d38bc9)

### path-036237

```text
(config)# ip nat translation pptp-timeout <number:0..536870> <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 0 `；EOL ` RVA 0x347CE3F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timeout in seconds。

[条件 C-5cef3876d27af29e](../../evidence/conditions-sets-036.md#c-5cef3876d27af29e) · [参数 P-5e18793378ea6b14](../../evidence/parameters-sets-008.md#p-5e18793378ea6b14) · [状态效果 S-4724bcec15d78286](../../evidence/state_effects-sets-016.md#s-4724bcec15d78286)

### path-036543

```text
(config)# ip nat translation routemap-entry-timeout <number:0..536870> <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 0 `；EOL ` RVA 0x347CCBC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timeout in seconds。

[条件 C-afda4573d1caeecf](../../evidence/conditions-sets-068.md#c-afda4573d1caeecf) · [参数 P-cb8e2f44a52e4625](../../evidence/parameters-sets-015.md#p-cb8e2f44a52e4625) · [状态效果 S-acf2412a7cdcd36f](../../evidence/state_effects-sets-037.md#s-acf2412a7cdcd36f)

### path-036364

```text
(config)# ip nat translation syn-timeout <number:0..536870> <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 0 `；EOL ` RVA 0x347CC748 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timeout in seconds。

[条件 C-3361130f37cebdac](../../evidence/conditions-sets-020.md#c-3361130f37cebdac) · [参数 P-e3ec3083d015a272](../../evidence/parameters-sets-017.md#p-e3ec3083d015a272) · [状态效果 S-e330778d0f6b626d](../../evidence/state_effects-sets-048.md#s-e330778d0f6b626d)

### path-036101

```text
(config)# ip nat translation tcp-timeout <number:0..536870> <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 0 `；EOL ` RVA 0x347CB8B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timeout in seconds。

[条件 C-69084f11a3e8427c](../../evidence/conditions-sets-041.md#c-69084f11a3e8427c) · [参数 P-e9933805ffdb0fc5](../../evidence/parameters-sets-017.md#p-e9933805ffdb0fc5) · [状态效果 S-99a1b4a9c6398736](../../evidence/state_effects-sets-033.md#s-99a1b4a9c6398736)

### path-036025

```text
(config)# ip nat translation timeout <number:0..536870> <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 0 `；EOL ` RVA 0x347CB4C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timeout in seconds。

[条件 C-fffd33ffb329e96c](../../evidence/conditions-sets-099.md#c-fffd33ffb329e96c) · [参数 P-c53dfc3e06fd77db](../../evidence/parameters-sets-015.md#p-c53dfc3e06fd77db) · [状态效果 S-baf1616d6cac0bff](../../evidence/state_effects-sets-039.md#s-baf1616d6cac0bff)

### path-036236

```text
(config)# ip nat translation udp-timeout <number:0..536870> <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 0 `；EOL ` RVA 0x347CBCF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timeout in seconds。

[条件 C-5a01eb00725bf6db](../../evidence/conditions-sets-035.md#c-5a01eb00725bf6db) · [参数 P-e5a1a8f732f12373](../../evidence/parameters-sets-017.md#p-e5a1a8f732f12373) · [状态效果 S-eafc6cf0e6267700](../../evidence/state_effects-sets-050.md#s-eafc6cf0e6267700)

### path-061297

```text
(config)# ip nbar attribute <?option@55558a78e518> custom <string> <cr>
```

Handler ` RVA 0x10F24CF0 `；selector ` 11 `；EOL ` RVA 0x3523A6E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Custom group value。

[条件 C-411e777223fe0ad0](../../evidence/conditions-sets-025.md#c-411e777223fe0ad0) · [缺口 G-42dbc8d7db71f482](../../evidence/gaps-sets-003.md#g-42dbc8d7db71f482) · [参数 P-3a6d800c77a3f84e](../../evidence/parameters-sets-005.md#p-3a6d800c77a3f84e) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029773

```text
(config)# ip nbar attribute-map <string> <cr>
```

Handler ` RVA 0x10F24CF0 `；selector ` 8 `；EOL ` RVA 0x35240410 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Attribute Profile Name - cannot exceed 20 characters。

[条件 C-36baca6458b62948](../../evidence/conditions-sets-021.md#c-36baca6458b62948) · [参数 P-bbd0d50663444514](../../evidence/parameters-sets-014.md#p-bbd0d50663444514) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-062790

```text
(config)# ip nbar attribute-set <?option@55558a794718> <?option@55558a7947e8> <cr>
```

Handler ` RVA 0x10F24CF0 `；selector ` 10 `；EOL ` RVA 0x352408C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8b8139d3896ec2d2](../../evidence/conditions-sets-054.md#c-8b8139d3896ec2d2) · [缺口 G-d6cf9ff70080f9f1](../../evidence/gaps-sets-007.md#g-d6cf9ff70080f9f1) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-036123

```text
(config)# ip nbar classification auto-learn top-hosts <cr>
```

Handler ` RVA 0x10F24CF0 `；selector ` 14 `；EOL ` RVA 0x3523C5B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bcc82ce1f4b03257](../../evidence/conditions-sets-073.md#c-bcc82ce1f4b03257) · [状态效果 S-f3f322772333904c](../../evidence/state_effects-sets-052.md#s-f3f322772333904c)

### path-053067

```text
(config)# ip nbar classification auto-learn top-hosts sample-rate <number:1..8192> <cr>
```

Handler ` RVA 0x10F24CF0 `；selector ` 15 `；EOL ` RVA 0x3523C5F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` sampler rate。

[条件 C-bcc82ce1f4b03257](../../evidence/conditions-sets-073.md#c-bcc82ce1f4b03257) · [参数 P-a88c83ad3ce43f20](../../evidence/parameters-sets-013.md#p-a88c83ad3ce43f20) · [状态效果 S-f3f322772333904c](../../evidence/state_effects-sets-052.md#s-f3f322772333904c)

### path-036166

```text
(config)# ip nbar classification dns classify-by-domain <cr>
```

Handler ` RVA 0x10F24CF0 `；selector ` 18 `；EOL ` RVA 0x3523D6C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d2361e69af884636](../../evidence/conditions-sets-081.md#c-d2361e69af884636) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-036336

```text
(config)# ip nbar classification dns learning <cr>
```

Handler ` RVA 0x10F24CF0 `；selector ` 16 `；EOL ` RVA 0x3523D1A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d2361e69af884636](../../evidence/conditions-sets-081.md#c-d2361e69af884636) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-045619

```text
(config)# ip nbar classification dns learning cache-ttl-zero <cr>
```

Handler ` RVA 0x10F24CF0 `；selector ` 17 `；EOL ` RVA 0x3523CED8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d2361e69af884636](../../evidence/conditions-sets-081.md#c-d2361e69af884636) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-045678

```text
(config)# ip nbar classification dns learning domains <cr>
```

Handler ` RVA 0x10F24CF0 `；selector ` 20 `；EOL ` RVA 0x3523D180 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d2361e69af884636](../../evidence/conditions-sets-081.md#c-d2361e69af884636) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-045561

```text
(config)# ip nbar classification dns learning guard <cr>
```

Handler ` RVA 0x10F24CF0 `；selector ` 19 `；EOL ` RVA 0x3523CC30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d2361e69af884636](../../evidence/conditions-sets-081.md#c-d2361e69af884636) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029799

```text
(config)# ip nbar classification granularity <cr>
```

Handler ` RVA 0x10F24CF0 `；selector ` 6 `；EOL ` RVA 0x3523BFB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-068eac01500ceba0](../../evidence/conditions-sets-003.md#c-068eac01500ceba0) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-061906

```text
(config)# ip nbar classification granularity fine-grain protocol <?option@55558a78fea8> <cr>
```

Handler ` RVA 0x10F24CF0 `；selector ` 6 `；EOL ` RVA 0x3523BFB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-794f09622123e9a9](../../evidence/conditions-sets-047.md#c-794f09622123e9a9) · [缺口 G-a4bbded1d6f7fad5](../../evidence/gaps-sets-006.md#g-a4bbded1d6f7fad5) · [状态效果 S-3939e38026f47304](../../evidence/state_effects-sets-013.md#s-3939e38026f47304)

### path-035801

```text
(config)# ip nbar classification ip-traffic all-caches <cr>
```

Handler ` RVA 0x10F24CF0 `；selector ` 40 `；EOL ` RVA 0x3523B670 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0b245294fadc8583](../../evidence/conditions-sets-005.md#c-0b245294fadc8583) · [状态效果 S-0be8c1be334a1105](../../evidence/state_effects-sets-003.md#s-0be8c1be334a1105)

### path-029888

```text
(config)# ip nbar classification multi-vrf <cr>
```

Handler ` RVA 0x10F24CF0 `；selector ` 24 `；EOL ` RVA 0x3523D998 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-42696176c897ebac](../../evidence/conditions-sets-026.md#c-42696176c897ebac) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-035864

```text
(config)# ip nbar classification tunneled-traffic ipv6inip <cr>
```

Handler ` RVA 0x10F24CF0 `；selector ` 5 `；EOL ` RVA 0x3523B9F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-98fa03775bf9951f](../../evidence/conditions-sets-059.md#c-98fa03775bf9951f) · [状态效果 S-6ddfb8ae7e16592e](../../evidence/state_effects-sets-023.md#s-6ddfb8ae7e16592e)

### path-061324

```text
(config)# ip nbar custom <string> transport udp <cr>
```

Handler ` RVA 0x10F25D20 `；selector ` 13 `；EOL ` RVA 0x3523DFE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Name of the User defined Protocol。

[条件 C-a1341634bd9653b6](../../evidence/conditions-sets-062.md#c-a1341634bd9653b6) · [缺口 G-da1ebfc40644eef3](../../evidence/gaps-sets-008.md#g-da1ebfc40644eef3) · [参数 P-3e35d998a4ef148c](../../evidence/parameters-sets-005.md#p-3e35d998a4ef148c) · [状态效果 S-21cd121f93e02257](../../evidence/state_effects-sets-008.md#s-21cd121f93e02257)

### path-029602

```text
(config)# ip nbar disable custom-async <cr>
```

Handler ` RVA 0x10F24CF0 `；selector ` 23 `；EOL ` RVA 0x3523AD30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8c619aeac51f093c](../../evidence/conditions-sets-054.md#c-8c619aeac51f093c) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029546

```text
(config)# ip nbar disable encrypted-app <cr>
```

Handler ` RVA 0x10F24CF0 `；selector ` 2 `；EOL ` RVA 0x3523AA50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-04702889663e37a2](../../evidence/conditions-sets-002.md#c-04702889663e37a2) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029649

```text
(config)# ip nbar disable sc-hit-vm-handler <cr>
```

Handler ` RVA 0x10F24CF0 `；selector ` 44 `；EOL ` RVA 0x3523AFE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad7cfeb564d82c84](../../evidence/conditions-sets-067.md#c-ad7cfeb564d82c84) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027034

```text
(config)# ip nbar http-services <cr>
```

Handler ` RVA 0x10F24CF0 `；selector ` 22 `；EOL ` RVA 0x3523B2F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d2361e69af884636](../../evidence/conditions-sets-081.md#c-d2361e69af884636) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-045169

```text
(config)# ip nbar protocol-map <string> id <number:1..65535> <cr>
```

Handler ` RVA 0x10F24CF0 `；selector ` 41 `；EOL ` RVA 0x3523A190 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` protocol name；` unsigned_number ` protocol id。

[条件 C-4c7ea1ddb2769b05](../../evidence/conditions-sets-030.md#c-4c7ea1ddb2769b05) · [参数 P-a2c8493e4d470e24](../../evidence/parameters-sets-012.md#p-a2c8493e4d470e24) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060598

```text
(config)# ip nbar protocol-pack <url:dynamic> <cr>
```

Handler ` RVA 0x10F24CF0 `；selector ` 3 `；EOL ` RVA 0x35239AF0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-45e34ee3c060f1f2](../../evidence/conditions-sets-027.md#c-45e34ee3c060f1f2) · [缺口 G-49c4061c2d988055](../../evidence/gaps-sets-003.md#g-49c4061c2d988055) · [参数 P-9479f4673300d543](../../evidence/parameters-sets-011.md#p-9479f4673300d543) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060829

```text
(config)# ip nbar protocol-pack <url:dynamic> force <cr>
```

Handler ` RVA 0x10F24CF0 `；selector ` 4 `；EOL ` RVA 0x35239AC8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-45e34ee3c060f1f2](../../evidence/conditions-sets-027.md#c-45e34ee3c060f1f2) · [缺口 G-49c4061c2d988055](../../evidence/gaps-sets-003.md#g-49c4061c2d988055) · [参数 P-9479f4673300d543](../../evidence/parameters-sets-011.md#p-9479f4673300d543) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026592

```text
(config)# ip nsf-converge <number:1..3600> <cr>
```

Handler ` RVA 0xE1FAC50 `；selector ` 2 `；EOL ` RVA 0x3423D4E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` The minimum NSF interval, in sec, before RIB reporting convergence。

[条件 C-6780db0323af9150](../../evidence/conditions-sets-040.md#c-6780db0323af9150) · [参数 P-330bda721d8260e5](../../evidence/parameters-sets-004.md#p-330bda721d8260e5) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026816

```text
(config)# ip options drop <cr>
```

Handler ` RVA 0xCF2A810 `；selector ` 14 `；EOL ` RVA 0x33D3A090 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e3240bbe074c8efd](../../evidence/conditions-sets-087.md#c-e3240bbe074c8efd) · [状态效果 S-a02625b7b3e0df7a](../../evidence/state_effects-sets-034.md#s-a02625b7b3e0df7a)

