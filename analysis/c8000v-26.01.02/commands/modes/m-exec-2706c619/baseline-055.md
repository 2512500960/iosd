# exec · 六个基础模式的历史连接

[模式索引](README.md) · [总索引](../../README.md)

### path-005807

```text
(exec)# test ipc window-size <number:32..1024> <cr>
```

Handler ` RVA 0xD3C5130 `；selector ` 0 `；EOL ` RVA 0x33E32DB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` window-size。

[条件 C-0221e2aa7e8f9b9b](../../evidence/conditions-sets-001.md#c-0221e2aa7e8f9b9b) · [参数 P-a42b339d50af46ca](../../evidence/parameters-sets-013.md#p-a42b339d50af46ca)

### path-009388

```text
(exec)# test ipc zone seat2slave <number:2..15> <cr>
```

Handler ` RVA 0xD3C79C0 `；selector ` 0 `；EOL ` RVA 0x33E36A90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` zone number。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [参数 P-11ee00fec1791900](../../evidence/parameters-sets-002.md#p-11ee00fec1791900) · [状态效果 S-f0118d4ca3c3bf1b](../../evidence/state_effects-sets-051.md#s-f0118d4ca3c3bf1b)

### path-017192

```text
(exec)# test iphc context lifetime <number:dynamic> <cr>
```

Handler ` RVA 0xD19AC60 `；selector ` 0 `；EOL ` RVA 0x33DA9230 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Context lifetime &lt;milli secs&gt;。

[条件 C-6db337f1f0f10d8e](../../evidence/conditions-sets-042.md#c-6db337f1f0f10d8e) · [缺口 G-d61c8518e7dbd032](../../evidence/gaps-sets-007.md#g-d61c8518e7dbd032) · [参数 P-159c11e81284fd63](../../evidence/parameters-sets-002.md#p-159c11e81284fd63) · [状态效果 S-7a6daab03a245700](../../evidence/state_effects-sets-026.md#s-7a6daab03a245700)

### path-008476

```text
(exec)# test iphc context lifetime default <cr>
```

Handler ` RVA 0xD19AC60 `；selector ` 0 `；EOL ` RVA 0x33DA9230 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [状态效果 S-7a6daab03a245700](../../evidence/state_effects-sets-026.md#s-7a6daab03a245700)

### path-008728

```text
(exec)# test ipv6 access-list common enable <cr>
```

Handler ` RVA 0x12166310 `；selector ` 0 `；EOL ` RVA 0x357B0D38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-344788770d245d72](../../evidence/conditions-sets-020.md#c-344788770d245d72) · [状态效果 S-3d826f48da78cf69](../../evidence/state_effects-sets-013.md#s-3d826f48da78cf69)

### path-023685

```text
(exec)# test ipv6 dhcp-client autoinstall <interface> test-case <number:1..65535> <cr>
```

Handler ` RVA 0x1218A870 `；selector ` 0 `；EOL ` RVA 0x357BD568 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` test case number。

[条件 C-3c62fe4ea9fb430c](../../evidence/conditions-sets-023.md#c-3c62fe4ea9fb430c) · [缺口 G-5f54ac697a1afdad](../../evidence/gaps-sets-004.md#g-5f54ac697a1afdad) · [参数 P-2a82be7442163efa](../../evidence/parameters-sets-004.md#p-2a82be7442163efa)

### path-010808

```text
(exec)# test ipv6 dhcp-client lease-query address <address> <cr>
```

Handler ` RVA 0x12189610 `；selector ` 0 `；EOL ` RVA 0x357BD0A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IPv6 address。

[条件 C-344788770d245d72](../../evidence/conditions-sets-020.md#c-344788770d245d72) · [参数 P-486f1516edce2b17](../../evidence/parameters-sets-006.md#p-486f1516edce2b17)

### path-005041

```text
(exec)# test ipv6 dhcp-relay bulk-lease-query <cr>
```

Handler ` RVA 0x121AF430 `；selector ` 0 `；EOL ` RVA 0x357C3B48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-344788770d245d72](../../evidence/conditions-sets-020.md#c-344788770d245d72)

### path-005078

```text
(exec)# test ipv6 dhcp-relay ldra <cr>
```

Handler ` RVA 0x121AE630 `；selector ` 0 `；EOL ` RVA 0x357C3E30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-344788770d245d72](../../evidence/conditions-sets-020.md#c-344788770d245d72)

### path-008716

```text
(exec)# test ipv6 dhcp-server hostnum <number:0..4294967295> <cr>
```

Handler ` RVA 0x121D2540 `；selector ` 0 `；EOL ` RVA 0x357CED60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` 32 bit host number in hex。

[条件 C-344788770d245d72](../../evidence/conditions-sets-020.md#c-344788770d245d72) · [参数 P-e77823c1af7cfc82](../../evidence/parameters-sets-017.md#p-e77823c1af7cfc82)

### path-025002

```text
(exec)# test ipv6 nd cache populate <interface> <address> <number:1..1000000> <address> <cr>
```

Handler ` RVA 0x1231AE00 `；selector ` 0 `；EOL ` RVA 0x357FCFC8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f4117212128cbb77](../../evidence/conditions-sets-094.md#c-f4117212128cbb77) · [缺口 G-57f47da0774c2188](../../evidence/gaps-sets-004.md#g-57f47da0774c2188) · [参数 P-9983055205a54d33](../../evidence/parameters-sets-012.md#p-9983055205a54d33)

### path-024689

```text
(exec)# test ipv6 nd cache stale-traffic <interface> <address> <number:1..1000000> <cr>
```

Handler ` RVA 0x1231B260 `；selector ` 0 `；EOL ` RVA 0x357FD3C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3b261c7bef3d0214](../../evidence/conditions-sets-023.md#c-3b261c7bef3d0214) · [缺口 G-e4f0c54725e9cd21](../../evidence/gaps-sets-008.md#g-e4f0c54725e9cd21) · [参数 P-21b74598aea17359](../../evidence/parameters-sets-003.md#p-21b74598aea17359)

### path-010852

```text
(exec)# test ipv6 nd client del <number:0..15> <cr>
```

Handler ` RVA 0x1231B440 `；selector ` 0 `；EOL ` RVA 0x357FCA70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` client id。

[条件 C-344788770d245d72](../../evidence/conditions-sets-020.md#c-344788770d245d72) · [参数 P-bd545017980207cf](../../evidence/parameters-sets-014.md#p-bd545017980207cf) · [状态效果 S-e07e219407b1de49](../../evidence/state_effects-sets-048.md#s-e07e219407b1de49)

### path-024682

```text
(exec)# test ipv6 nd client pfx-adv-ctrl <number:0..15> <interface> enable <cr>
```

Handler ` RVA 0x1231B570 `；selector ` 0 `；EOL ` RVA 0x357FC1F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` client id。

[条件 C-396c606b57a4d3e9](../../evidence/conditions-sets-022.md#c-396c606b57a4d3e9) · [缺口 G-cf35f113483d5765](../../evidence/gaps-sets-007.md#g-cf35f113483d5765) · [参数 P-715db31255dbb2ae](../../evidence/parameters-sets-009.md#p-715db31255dbb2ae) · [状态效果 S-0b61d82ecb625c49](../../evidence/state_effects-sets-003.md#s-0b61d82ecb625c49)

### path-024692

```text
(exec)# test ipv6 nd client sendra <number:0..15> <interface> <address> <cr>
```

Handler ` RVA 0x1231B650 `；selector ` 0 `；EOL ` RVA 0x357FC6D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` client id；` address ` Destination address。

[条件 C-3fcd68d16a9f2d69](../../evidence/conditions-sets-025.md#c-3fcd68d16a9f2d69) · [缺口 G-21c50847db42e3fe](../../evidence/gaps-sets-002.md#g-21c50847db42e3fe) · [参数 P-b75c11ff1b63e956](../../evidence/parameters-sets-014.md#p-b75c11ff1b63e956)

### path-025139

```text
(exec)# test ipv6 nd db populate <interface> <address> <number:1..262144> <address> add <cr>
```

Handler ` RVA 0x1231B0A0 `；selector ` 0 `；EOL ` RVA 0x35800088 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-aba02b735c45c3aa](../../evidence/conditions-sets-066.md#c-aba02b735c45c3aa) · [缺口 G-accf9b67d7c43119](../../evidence/gaps-sets-006.md#g-accf9b67d7c43119) · [参数 P-431814581a662b90](../../evidence/parameters-sets-006.md#p-431814581a662b90) · [状态效果 S-efa8d8ea71547789](../../evidence/state_effects-sets-051.md#s-efa8d8ea71547789)

### path-021545

```text
(exec)# test ipv6 nd ha <interface> <number:0..1> <cr>
```

Handler ` RVA 0x1231D080 `；selector ` 0 `；EOL ` RVA 0x357FDC08 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` sense。

[条件 C-7b28470cb2fbbf19](../../evidence/conditions-sets-048.md#c-7b28470cb2fbbf19) · [缺口 G-721a3bde9d9af595](../../evidence/gaps-sets-004.md#g-721a3bde9d9af595) · [参数 P-fb987dba5cf3ff63](../../evidence/parameters-sets-019.md#p-fb987dba5cf3ff63)

### path-021509

```text
(exec)# test ipv6 nd mip_rmg <interface> <number:0..1> <cr>
```

Handler ` RVA 0x1231D120 `；selector ` 0 `；EOL ` RVA 0x357FD7D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` sense。

[条件 C-5d8dbe8e97f2550e](../../evidence/conditions-sets-036.md#c-5d8dbe8e97f2550e) · [缺口 G-c99a8b86f93d83ff](../../evidence/gaps-sets-007.md#g-c99a8b86f93d83ff) · [参数 P-bb230184350e3250](../../evidence/parameters-sets-014.md#p-bb230184350e3250)

### path-008698

```text
(exec)# test ipv6 nd pd-limit <number:0..2147483647> <cr>
```

Handler ` RVA 0x123198C0 `；selector ` 0 `；EOL ` RVA 0x357FBA50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of entries。

[条件 C-344788770d245d72](../../evidence/conditions-sets-020.md#c-344788770d245d72) · [参数 P-defb6b1a96e6831a](../../evidence/parameters-sets-017.md#p-defb6b1a96e6831a)

### path-010795

```text
(exec)# test ipv6 nd repopulate queue-size <number:1..512> <cr>
```

Handler ` RVA 0x123197B0 `；selector ` 0 `；EOL ` RVA 0x357FBD80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Queue size。

[条件 C-344788770d245d72](../../evidence/conditions-sets-020.md#c-344788770d245d72) · [参数 P-6970d6f8d867e4bf](../../evidence/parameters-sets-008.md#p-6970d6f8d867e4bf)

### path-023634

```text
(exec)# test ipv6 nd router number <number:0..70000> <interface> <cr>
```

Handler ` RVA 0x123197F0 `；selector ` 0 `；EOL ` RVA 0x357FAF90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Number of routers。

[条件 C-85db5cc684a2069d](../../evidence/conditions-sets-052.md#c-85db5cc684a2069d) · [缺口 G-7cff1df5a0d79896](../../evidence/gaps-sets-005.md#g-7cff1df5a0d79896) · [参数 P-c7eb82c1d7f6f990](../../evidence/parameters-sets-015.md#p-c7eb82c1d7f6f990)

### path-023794

```text
(exec)# test ipv6 nd session create <interface> <number:1..65535> <cr>
```

Handler ` RVA 0x1231BBF0 `；selector ` 0 `；EOL ` RVA 0x357FE450 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Count。

[条件 C-30673156413f78eb](../../evidence/conditions-sets-019.md#c-30673156413f78eb) · [缺口 G-c7351edaf533bc44](../../evidence/gaps-sets-007.md#g-c7351edaf533bc44) · [参数 P-70b9f1362143ec9a](../../evidence/parameters-sets-009.md#p-70b9f1362143ec9a)

### path-024727

```text
(exec)# test ipv6 nd session delete <interface> <number:1..65535> <number:1..65535> <cr>
```

Handler ` RVA 0x1231C500 `；selector ` 0 `；EOL ` RVA 0x357FFB60 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Initial；` unsigned_number ` Count。

[条件 C-85f21c70abbec4de](../../evidence/conditions-sets-052.md#c-85f21c70abbec4de) · [缺口 G-4b0779d99fd91235](../../evidence/gaps-sets-003.md#g-4b0779d99fd91235) · [参数 P-4a8cc4f4585b8595](../../evidence/parameters-sets-006.md#p-4a8cc4f4585b8595)

### path-025014

```text
(exec)# test ipv6 nd session mac <interface> <number:1..65535> <number:1..65535> <address> <cr>
```

Handler ` RVA 0x1231BFD0 `；selector ` 0 `；EOL ` RVA 0x357FEED8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Initial；` unsigned_number ` Count；` address ` 48-bit hardware address。

[条件 C-2bdc571ae1bccd3a](../../evidence/conditions-sets-017.md#c-2bdc571ae1bccd3a) · [缺口 G-e74216921dd04b84](../../evidence/gaps-sets-008.md#g-e74216921dd04b84) · [参数 P-b17f2a63c4a6ce9d](../../evidence/parameters-sets-013.md#p-b17f2a63c4a6ce9d)

### path-025372

```text
(exec)# test ipv6 nd session prefix <interface> <number:1..65535> <number:1..65535> <prefix:dynamic> <cr>
```

Handler ` RVA 0x1231BD40 `；selector ` 0 `；EOL ` RVA 0x357FE910 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Initial；` unsigned_number ` Count；` prefix_dynamic ` IPv6 prefix x:x::y/&lt;z&gt;。

[条件 C-1e4ba48e66abc9f3](../../evidence/conditions-sets-012.md#c-1e4ba48e66abc9f3) · [缺口 G-abc07253a2c5cfbf](../../evidence/gaps-sets-006.md#g-abc07253a2c5cfbf) · [参数 P-08b690d7942b68e0](../../evidence/parameters-sets-001.md#p-08b690d7942b68e0)

### path-023783

```text
(exec)# test ipv6 nd session set <interface> <number:0..1> <cr>
```

Handler ` RVA 0x1231B730 `；selector ` 0 `；EOL ` RVA 0x357FE060 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` sense。

[条件 C-03237bc5e4bf2fc3](../../evidence/conditions-sets-002.md#c-03237bc5e4bf2fc3) · [缺口 G-11f232c2d8c6cee5](../../evidence/gaps-sets-001.md#g-11f232c2d8c6cee5) · [参数 P-d122028835d514e9](../../evidence/parameters-sets-016.md#p-d122028835d514e9)

### path-024713

```text
(exec)# test ipv6 nd session start <interface> <number:1..65535> <number:1..65535> <cr>
```

Handler ` RVA 0x1231C3B0 `；selector ` 0 `；EOL ` RVA 0x357FF308 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Initial；` unsigned_number ` Count。

[条件 C-127cba33c7b41f4e](../../evidence/conditions-sets-007.md#c-127cba33c7b41f4e) · [缺口 G-93bc545592df5d9e](../../evidence/gaps-sets-005.md#g-93bc545592df5d9e) · [参数 P-2b22a719a8c59122](../../evidence/parameters-sets-004.md#p-2b22a719a8c59122)

### path-024719

```text
(exec)# test ipv6 nd session stop <interface> <number:1..65535> <number:1..65535> <cr>
```

Handler ` RVA 0x1231C500 `；selector ` 0 `；EOL ` RVA 0x357FF750 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Initial；` unsigned_number ` Count。

[条件 C-d57c43aae7df2300](../../evidence/conditions-sets-082.md#c-d57c43aae7df2300) · [缺口 G-7834f58d7b6b66b5](../../evidence/gaps-sets-005.md#g-7834f58d7b6b66b5) · [参数 P-1a8efde88a20cf81](../../evidence/parameters-sets-002.md#p-1a8efde88a20cf81) · [状态效果 S-5ff56c26c269d59f](../../evidence/state_effects-sets-021.md#s-5ff56c26c269d59f)

### path-024668

```text
(exec)# test ipv6 nd test-evpn-entry add <address> <interface> <address> <cr>
```

Handler ` RVA 0x12319970 `；selector ` 0 `；EOL ` RVA 0x357FB6E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` IPv6 address；` address ` 48-bit hardware address。

[条件 C-c344440b69a93598](../../evidence/conditions-sets-075.md#c-c344440b69a93598) · [缺口 G-90976623ec772783](../../evidence/gaps-sets-005.md#g-90976623ec772783) · [参数 P-2bebad0a41458ee1](../../evidence/parameters-sets-004.md#p-2bebad0a41458ee1) · [状态效果 S-4b64b02aef2e60da](../../evidence/state_effects-sets-017.md#s-4b64b02aef2e60da)

### path-005010

```text
(exec)# test ipv6 nd test-nsf <cr>
```

Handler ` RVA 0x12319920 `；selector ` 0 `；EOL ` RVA 0x357FB260 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-344788770d245d72](../../evidence/conditions-sets-020.md#c-344788770d245d72)

### path-008763

```text
(exec)# test ipv6 rib multicast add <cr>
```

Handler ` RVA 0x1230B6E0 `；selector ` 0 `；EOL ` RVA 0x357ECD58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a9221de4cc56d913](../../evidence/conditions-sets-065.md#c-a9221de4cc56d913) · [状态效果 S-4b75396cf4148275](../../evidence/state_effects-sets-017.md#s-4b75396cf4148275)

### path-025419

```text
(exec)# test ipv6 rib path add clone <prefix:dynamic> <address> <interface> <interface> <cr>
```

Handler ` RVA 0x1230C860 `；selector ` 0 `；EOL ` RVA 0x357EF460 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-51f8399fdfa483e6](../../evidence/conditions-sets-032.md#c-51f8399fdfa483e6) · [缺口 G-30fcf680cee6b2b0](../../evidence/gaps-sets-002.md#g-30fcf680cee6b2b0) · [参数 P-0f0200380bef9f0b](../../evidence/parameters-sets-002.md#p-0f0200380bef9f0b)

### path-025373

```text
(exec)# test ipv6 rib path add foreign <number:1..16> <prefix:dynamic> <address> <interface> <cr>
```

Handler ` RVA 0x1230B900 `；selector ` 0 `；EOL ` RVA 0x357EDA00 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9f944e4b24908cba](../../evidence/conditions-sets-062.md#c-9f944e4b24908cba) · [缺口 G-25b92b0a47ab8ce1](../../evidence/gaps-sets-002.md#g-25b92b0a47ab8ce1) · [参数 P-56f0ec8311f47521](../../evidence/parameters-sets-007.md#p-56f0ec8311f47521)

### path-025420

```text
(exec)# test ipv6 rib path add primary <number:1..16> <prefix:dynamic> <address> <interface> <address> <interface> <number:1..255> <number:1..255> <cr>
```

Handler ` RVA 0x1230C050 `；selector ` 0 `；EOL ` RVA 0x357EEA10 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-629d2f54487c3680](../../evidence/conditions-sets-038.md#c-629d2f54487c3680) · [缺口 G-80dd46fdf6d1f397](../../evidence/gaps-sets-005.md#g-80dd46fdf6d1f397) · [参数 P-ef0442f2797d35e1](../../evidence/parameters-sets-018.md#p-ef0442f2797d35e1)

### path-025379

```text
(exec)# test ipv6 rib path add repair <number:1..16> <prefix:dynamic> <address> <interface> <number:1..255> <number:1..255> <cr>
```

Handler ` RVA 0x1230C5A0 `；selector ` 0 `；EOL ` RVA 0x357EDF68 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1eb8ee219844b8ad](../../evidence/conditions-sets-012.md#c-1eb8ee219844b8ad) · [缺口 G-330cd16605a65ef4](../../evidence/gaps-sets-002.md#g-330cd16605a65ef4) · [参数 P-b15a2736acb0c202](../../evidence/parameters-sets-013.md#p-b15a2736acb0c202)

### path-025382

```text
(exec)# test ipv6 rib path add tilfa-primary <number:1..16> <prefix:dynamic> <address> <interface> <number:16777217..33554430> <number:1..255> <number:1..255> <cr>
```

Handler ` RVA 0x1230BAA0 `；selector ` 0 `；EOL ` RVA 0x357EEF98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-82d7018b8b5ddf55](../../evidence/conditions-sets-051.md#c-82d7018b8b5ddf55) · [缺口 G-7594a8d475db56be](../../evidence/gaps-sets-005.md#g-7594a8d475db56be) · [参数 P-6f87358eaf7e38de](../../evidence/parameters-sets-009.md#p-6f87358eaf7e38de)

### path-025209

```text
(exec)# test ipv6 rib path add tilfa-repair <number:1..16> <prefix:dynamic> <number:16777217..33554430> <number:1..255> <number:1..255> <cr>
```

Handler ` RVA 0x1230C340 `；selector ` 0 `；EOL ` RVA 0x357EE438 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-452f9a26d9eef037](../../evidence/conditions-sets-027.md#c-452f9a26d9eef037) · [缺口 G-5a8a83a4d2c3b5e0](../../evidence/gaps-sets-004.md#g-5a8a83a4d2c3b5e0) · [参数 P-d385be79b243bc1c](../../evidence/parameters-sets-016.md#p-d385be79b243bc1c)

### path-025374

```text
(exec)# test ipv6 rib path del foreign <number:1..16> <prefix:dynamic> <address> <interface> <cr>
```

Handler ` RVA 0x1230CAA0 `；selector ` 0 `；EOL ` RVA 0x357EF998 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4b5d69792e4692c5](../../evidence/conditions-sets-030.md#c-4b5d69792e4692c5) · [缺口 G-e8ceecf22fc1d3d3](../../evidence/gaps-sets-008.md#g-e8ceecf22fc1d3d3) · [参数 P-feab6951d2a3654a](../../evidence/parameters-sets-019.md#p-feab6951d2a3654a)

### path-025378

```text
(exec)# test ipv6 rib path del primary <number:1..16> <prefix:dynamic> <address> <interface> <number:1..255> <number:1..255> <cr>
```

Handler ` RVA 0x1230BD80 `；selector ` 0 `；EOL ` RVA 0x357EFE68 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b9dc38a4c48674d9](../../evidence/conditions-sets-072.md#c-b9dc38a4c48674d9) · [缺口 G-fd97ce8ba817775f](../../evidence/gaps-sets-009.md#g-fd97ce8ba817775f) · [参数 P-11bbc1be4c4d98b5](../../evidence/parameters-sets-002.md#p-11bbc1be4c4d98b5)

### path-011993

```text
(exec)# test ipv6 rib pdb add <number:1..16> <number:1..255> <number:0..1> <cr>
```

Handler ` RVA 0x1230B4F0 `；selector ` 0 `；EOL ` RVA 0x357ED4E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-344788770d245d72](../../evidence/conditions-sets-020.md#c-344788770d245d72) · [参数 P-ebee9a394e927907](../../evidence/parameters-sets-018.md#p-ebee9a394e927907)

### path-010766

```text
(exec)# test ipv6 rib pdb del <number:1..16> <cr>
```

Handler ` RVA 0x1230B640 `；selector ` 0 `；EOL ` RVA 0x357ED140 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-344788770d245d72](../../evidence/conditions-sets-020.md#c-344788770d245d72) · [参数 P-4d58cc23e6e79a5d](../../evidence/parameters-sets-006.md#p-4d58cc23e6e79a5d)

### path-025380

```text
(exec)# test ipv6 rib prefix add <number:1..16> <prefix:dynamic> <address> <interface> <number:1..255> <number:1..255> <number:1..32000> <cr>
```

Handler ` RVA 0x1230CC40 `；selector ` 0 `；EOL ` RVA 0x357F0558 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` id；` prefix_dynamic ` prefix；` address ` neighbour；` unsigned_number ` admin；` unsigned_number ` metric；` unsigned_number ` repeat。

[条件 C-c5591b9ebe4b7f64](../../evidence/conditions-sets-076.md#c-c5591b9ebe4b7f64) · [缺口 G-dddb4ff58b516f68](../../evidence/gaps-sets-008.md#g-dddb4ff58b516f68) · [参数 P-094ffc8e7bffbfe6](../../evidence/parameters-sets-001.md#p-094ffc8e7bffbfe6) · [状态效果 S-00c6eae995313e2f](../../evidence/state_effects-sets-001.md#s-00c6eae995313e2f)

### path-024688

```text
(exec)# test ipv6 rib prefix del <number:1..16> <prefix:dynamic> <address> <cr>
```

Handler ` RVA 0x1230CF80 `；selector ` 0 `；EOL ` RVA 0x357F0970 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-279284fa5f01cd0b](../../evidence/conditions-sets-016.md#c-279284fa5f01cd0b) · [缺口 G-7e61500914191c1c](../../evidence/gaps-sets-005.md#g-7e61500914191c1c) · [参数 P-acc2a8881e66193c](../../evidence/parameters-sets-013.md#p-acc2a8881e66193c) · [状态效果 S-00c6eae995313e2f](../../evidence/state_effects-sets-001.md#s-00c6eae995313e2f)

### path-008636

```text
(exec)# test ipv6 rib queue start <cr>
```

Handler ` RVA 0x1230B430 `；selector ` 0 `；EOL ` RVA 0x357EC420 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-344788770d245d72](../../evidence/conditions-sets-020.md#c-344788770d245d72) · [状态效果 S-7e85e00b13bdd3c7](../../evidence/state_effects-sets-027.md#s-7e85e00b13bdd3c7)

### path-008651

```text
(exec)# test ipv6 rib suspend start <cr>
```

Handler ` RVA 0x1230B490 `；selector ` 0 `；EOL ` RVA 0x357EC780 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-344788770d245d72](../../evidence/conditions-sets-020.md#c-344788770d245d72) · [状态效果 S-59ab3739daa03429](../../evidence/state_effects-sets-019.md#s-59ab3739daa03429)

### path-021588

```text
(exec)# test ipv6 rmap associate <string> <interface> <cr>
```

Handler ` RVA 0x118C0490 `；selector ` 0 `；EOL ` RVA 0x3559F648 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` rmap name to (dis)associate。

[条件 C-d9564a589f48341b](../../evidence/conditions-sets-084.md#c-d9564a589f48341b) · [缺口 G-65650b17e6d858a4](../../evidence/gaps-sets-004.md#g-65650b17e6d858a4) · [参数 P-52665bfba48ca87a](../../evidence/parameters-sets-007.md#p-52665bfba48ca87a) · [状态效果 S-3ad67cef8f5a3f25](../../evidence/state_effects-sets-013.md#s-3ad67cef8f5a3f25)

### path-010927

```text
(exec)# test ipv6 rmap associate <string> local <cr>
```

Handler ` RVA 0x118C0490 `；selector ` 0 `；EOL ` RVA 0x3559F648 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` rmap name to (dis)associate。

[条件 C-d589125cdae713be](../../evidence/conditions-sets-082.md#c-d589125cdae713be) · [参数 P-ea229d8e07f52d10](../../evidence/parameters-sets-018.md#p-ea229d8e07f52d10) · [状态效果 S-001838fe517d6b2b](../../evidence/state_effects-sets-001.md#s-001838fe517d6b2b)

### path-010851

```text
(exec)# test ipv6 rmap create <number:1..7> <string> <cr>
```

Handler ` RVA 0xE202AC0 `；selector ` 0 `；EOL ` RVA 0x3559CF80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Application: 1 - AAA；` string ` application specific string。

[条件 C-344788770d245d72](../../evidence/conditions-sets-020.md#c-344788770d245d72) · [参数 P-700266de357f47fd](../../evidence/parameters-sets-009.md#p-700266de357f47fd)

### path-010936

```text
(exec)# test ipv6 rmap delete <string> <number:0..4294967295> <cr>
```

Handler ` RVA 0xE202FB0 `；selector ` 0 `；EOL ` RVA 0x3559EEE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle。

[条件 C-2e45070c430f0ff6](../../evidence/conditions-sets-018.md#c-2e45070c430f0ff6) · [参数 P-e1f9c2e256f45292](../../evidence/parameters-sets-017.md#p-e1f9c2e256f45292) · [状态效果 S-31083421ac86798c](../../evidence/state_effects-sets-011.md#s-31083421ac86798c)

### path-012110

```text
(exec)# test ipv6 rmap delete <string> <number:0..4294967295> match acl <string> <cr>
```

Handler ` RVA 0x118BCAF0 `；selector ` 0 `；EOL ` RVA 0x3559D768 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` string ` acl name。

[条件 C-750a812b02b00163](../../evidence/conditions-sets-045.md#c-750a812b02b00163) · [参数 P-131b5c4417a1f1af](../../evidence/parameters-sets-002.md#p-131b5c4417a1f1af) · [状态效果 S-31083421ac86798c](../../evidence/state_effects-sets-011.md#s-31083421ac86798c)

### path-012167

```text
(exec)# test ipv6 rmap delete <string> <number:0..4294967295> match length <number:0..2147483647> <number:0..2147483647> <cr>
```

Handler ` RVA 0xE2036F0 `；selector ` 0 `；EOL ` RVA 0x3559DA70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` unsigned_number ` Minimum packet length；` unsigned_number ` Maximum packet length。

[条件 C-750a812b02b00163](../../evidence/conditions-sets-045.md#c-750a812b02b00163) · [参数 P-43c97c6f77edf50d](../../evidence/parameters-sets-006.md#p-43c97c6f77edf50d) · [状态效果 S-31083421ac86798c](../../evidence/state_effects-sets-011.md#s-31083421ac86798c)

### path-012014

```text
(exec)# test ipv6 rmap delete <string> <number:0..4294967295> set global <cr>
```

Handler ` RVA 0xE204CB0 `；selector ` 0 `；EOL ` RVA 0x3559E720 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle。

[条件 C-40504cdef4f39589](../../evidence/conditions-sets-025.md#c-40504cdef4f39589) · [参数 P-e1f9c2e256f45292](../../evidence/parameters-sets-017.md#p-e1f9c2e256f45292) · [状态效果 S-31083421ac86798c](../../evidence/state_effects-sets-011.md#s-31083421ac86798c)

### path-025030

```text
(exec)# test ipv6 rmap delete <string> <number:0..4294967295> set interface <interface> <cr>
```

Handler ` RVA 0x118BD3B0 `；selector ` 0 `；EOL ` RVA 0x3559EA90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle。

[条件 C-b9d3114aa47db50d](../../evidence/conditions-sets-072.md#c-b9d3114aa47db50d) · [缺口 G-b6faf044e3dba0a4](../../evidence/gaps-sets-006.md#g-b6faf044e3dba0a4) · [参数 P-e127611f1cbf4d17](../../evidence/parameters-sets-017.md#p-e127611f1cbf4d17) · [状态效果 S-c7dd52d103669862](../../evidence/state_effects-sets-042.md#s-c7dd52d103669862)

### path-012112

```text
(exec)# test ipv6 rmap delete <string> <number:0..4294967295> set next-hop <address> <cr>
```

Handler ` RVA 0x118BCDA0 `；selector ` 0 `；EOL ` RVA 0x3559DE00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` address ` IPv6 address of next-hop。

[条件 C-f111621d7996149d](../../evidence/conditions-sets-093.md#c-f111621d7996149d) · [参数 P-9c64443c07b0a179](../../evidence/parameters-sets-012.md#p-9c64443c07b0a179) · [状态效果 S-6141bbbe28dbc6f6](../../evidence/state_effects-sets-021.md#s-6141bbbe28dbc6f6)

### path-012114

```text
(exec)# test ipv6 rmap delete <string> <number:0..4294967295> set precedence <number:0..7> <cr>
```

Handler ` RVA 0x118BD130 `；selector ` 0 `；EOL ` RVA 0x3559E1B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` unsigned_number ` Value of precedence。

[条件 C-40504cdef4f39589](../../evidence/conditions-sets-025.md#c-40504cdef4f39589) · [参数 P-ce115e51ed785080](../../evidence/parameters-sets-016.md#p-ce115e51ed785080) · [状态效果 S-31083421ac86798c](../../evidence/state_effects-sets-011.md#s-31083421ac86798c)

### path-012116

```text
(exec)# test ipv6 rmap delete <string> <number:0..4294967295> set vrf <string> <cr>
```

Handler ` RVA 0xE204A00 `；selector ` 0 `；EOL ` RVA 0x3559E4A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` string ` VRF name。

[条件 C-40504cdef4f39589](../../evidence/conditions-sets-025.md#c-40504cdef4f39589) · [参数 P-0f25ae5261c5ab19](../../evidence/parameters-sets-002.md#p-0f25ae5261c5ab19) · [状态效果 S-31083421ac86798c](../../evidence/state_effects-sets-011.md#s-31083421ac86798c)

### path-010901

```text
(exec)# test ipv6 rmap delete <string> permit <cr>
```

Handler ` RVA 0xE202DC0 `；selector ` 0 `；EOL ` RVA 0x3559F180 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` routemap tag。

[条件 C-750a812b02b00163](../../evidence/conditions-sets-045.md#c-750a812b02b00163) · [参数 P-afea805b9cc43465](../../evidence/parameters-sets-013.md#p-afea805b9cc43465) · [状态效果 S-9f0307e50a474c70](../../evidence/state_effects-sets-034.md#s-9f0307e50a474c70)

### path-008745

```text
(exec)# test ipv6 rmap register <number:1..7> <cr>
```

Handler ` RVA 0xE2028D0 `；selector ` 0 `；EOL ` RVA 0x3559CBF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Application。

[条件 C-344788770d245d72](../../evidence/conditions-sets-020.md#c-344788770d245d72) · [参数 P-ffc4586fce516f90](../../evidence/parameters-sets-019.md#p-ffc4586fce516f90) · [状态效果 S-4867fd7fd30d96ed](../../evidence/state_effects-sets-016.md#s-4867fd7fd30d96ed)

### path-010867

```text
(exec)# test ipv6 rmap remove <string> <number:1..7> <cr>
```

Handler ` RVA 0xE202C80 `；selector ` 0 `；EOL ` RVA 0x3559D2A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` application specific string；` unsigned_number ` Application: 1 - AAA。

[条件 C-344788770d245d72](../../evidence/conditions-sets-020.md#c-344788770d245d72) · [参数 P-6ee64968fd4901d6](../../evidence/parameters-sets-009.md#p-6ee64968fd4901d6)

### path-008666

```text
(exec)# test ipv6 static limit <number:0..32> <cr>
```

Handler ` RVA 0x12310D00 `；selector ` 0 `；EOL ` RVA 0x357F0F90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-344788770d245d72](../../evidence/conditions-sets-020.md#c-344788770d245d72) · [参数 P-f007846cc54b8f35](../../evidence/parameters-sets-018.md#p-f007846cc54b8f35)

### path-004987

```text
(exec)# test ipv6 static policy <cr>
```

Handler ` RVA 0x12310CC0 `；selector ` 0 `；EOL ` RVA 0x357F0CA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-344788770d245d72](../../evidence/conditions-sets-020.md#c-344788770d245d72)

### path-005450

```text
(exec)# test isis case <number:0..4294967295> <cr>
```

Handler ` RVA 0x10743F90 `；selector ` 4 `；EOL ` RVA 0x34B9ACE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` test number。

[条件 C-5aee62e855a149a4](../../evidence/conditions-sets-036.md#c-5aee62e855a149a4) · [参数 P-648cc8ff7d755148](../../evidence/parameters-sets-008.md#p-648cc8ff7d755148)

### path-017912

```text
(exec)# test isis case <number:0..4294967295> <interface> <cr>
```

Handler ` RVA 0x10743F90 `；selector ` 4 `；EOL ` RVA 0x34B9ACE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` test number。

[条件 C-e9156e81b246e53d](../../evidence/conditions-sets-090.md#c-e9156e81b246e53d) · [缺口 G-f88f15910f0bda41](../../evidence/gaps-sets-009.md#g-f88f15910f0bda41) · [参数 P-fca7330218061f69](../../evidence/parameters-sets-019.md#p-fca7330218061f69)

### path-005355

```text
(exec)# test isis clear counters <cr>
```

Handler ` RVA 0x10743F90 `；selector ` 5 `；EOL ` RVA 0x34B792E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-001535

```text
(exec)# test isis debug <cr>
```

Handler ` RVA 0x10743F90 `；selector ` 0 `；EOL ` RVA 0x34B78708 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-005361

```text
(exec)# test isis ip address <cr>
```

Handler ` RVA 0x10743F90 `；selector ` 3 `；EOL ` RVA 0x34B78F58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-011049

```text
(exec)# test isis lsp advertise lan-adj-sid <number:1..255> <cr>
```

Handler ` RVA 0x10743F90 `；selector ` 15 `；EOL ` RVA 0x34B9B8A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` number of items。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-555260a8b81f290e](../../evidence/parameters-sets-007.md#p-555260a8b81f290e) · [状态效果 S-e66224beb3c76a2f](../../evidence/state_effects-sets-049.md#s-e66224beb3c76a2f)

### path-005526

```text
(exec)# test isis lsp build <cr>
```

Handler ` RVA 0x10743F90 `；selector ` 8 `；EOL ` RVA 0x34B9C870 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-005446

```text
(exec)# test isis lsp id <cr>
```

Handler ` RVA 0x10743F90 `；selector ` 1 `；EOL ` RVA 0x34B9B520 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-009069

```text
(exec)# test isis lsp non_pn_delay on <cr>
```

Handler ` RVA 0x10743F90 `；selector ` 13 `；EOL ` RVA 0x34B9C4E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [状态效果 S-0eae8cafb577c047](../../evidence/state_effects-sets-003.md#s-0eae8cafb577c047)

### path-009064

```text
(exec)# test isis lsp pn_delay on <cr>
```

Handler ` RVA 0x10743F90 `；selector ` 12 `；EOL ` RVA 0x34B9C188 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [状态效果 S-7724b0455e700c4a](../../evidence/state_effects-sets-025.md#s-7724b0455e700c4a)

### path-005562

```text
(exec)# test isis lsp purge <cr>
```

Handler ` RVA 0x10743F90 `；selector ` 9 `；EOL ` RVA 0x34B9D118 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-009096

```text
(exec)# test isis lsp purge dr <cr>
```

Handler ` RVA 0x10743F90 `；selector ` 10 `；EOL ` RVA 0x34B9CC98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-005484

```text
(exec)# test isis lsp refresh <cr>
```

Handler ` RVA 0x10743F90 `；selector ` 11 `；EOL ` RVA 0x34B9BCF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-001556

```text
(exec)# test isis nsap <cr>
```

Handler ` RVA 0x10743F90 `；selector ` 2 `；EOL ` RVA 0x34B78BF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-005366

```text
(exec)# test isis show counters <cr>
```

Handler ` RVA 0x10743F90 `；selector ` 6 `；EOL ` RVA 0x34B795E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-001659

```text
(exec)# test isis spf <cr>
```

Handler ` RVA 0x10743F90 `；selector ` 7 `；EOL ` RVA 0x34B9B0D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-005375

```text
(exec)# test isis telemetry enable <cr>
```

Handler ` RVA 0x10743F90 `；selector ` 21 `；EOL ` RVA 0x34B798B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [状态效果 S-8816e9edea9d98e6](../../evidence/state_effects-sets-029.md#s-8816e9edea9d98e6)

### path-011942

```text
(exec)# test issu capability entry register <number:1..4294967295> <number:0..100> <string> <cr>
```

Handler ` RVA 0xD4C7970 `；selector ` 0 `；EOL ` RVA 0x33E62D08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` entity id；` unsigned_number ` cap entry id；` string ` Cap Type list ex: 1,3,4 - Comma needed。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-b7aee89a0684739a](../../evidence/parameters-sets-014.md#p-b7aee89a0684739a) · [状态效果 S-cd90d6ef7b6f6da8](../../evidence/state_effects-sets-044.md#s-cd90d6ef7b6f6da8)

### path-012077

```text
(exec)# test issu capability group register <number:1..4294967295> <number:1..100> <number:0..1> <string> <cr>
```

Handler ` RVA 0xD4C7970 `；selector ` 0 `；EOL ` RVA 0x33E63100 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` entity id；` unsigned_number ` cap group id；` unsigned_number ` no_mandatory_entry 1=TRUE, 0=FALSE；` string ` Cap entry list ex: 1,3,4 - Comma needed。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-edb3c0f496cab6b9](../../evidence/parameters-sets-018.md#p-edb3c0f496cab6b9) · [状态效果 S-f0f8a5a012270a01](../../evidence/state_effects-sets-051.md#s-f0f8a5a012270a01)

### path-011606

```text
(exec)# test issu capability type-list register <number:1..4294967295> <string> <cr>
```

Handler ` RVA 0xD4C7970 `；selector ` 0 `；EOL ` RVA 0x33E62930 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` entity id；` string ` Cap Type list ex: 1,3,4 - Comma needed。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-369daa5871e461d5](../../evidence/parameters-sets-005.md#p-369daa5871e461d5) · [状态效果 S-1329607d5c62a0ee](../../evidence/state_effects-sets-004.md#s-1329607d5c62a0ee)

### path-010495

```text
(exec)# test issu client <number:1..9999> bits enable <cr>
```

Handler ` RVA 0xD4C7970 `；selector ` 0 `；EOL ` RVA 0x33E61080 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` client id。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-3ef334e0ec790657](../../evidence/parameters-sets-005.md#p-3ef334e0ec790657) · [状态效果 S-3c85f9b12af37552](../../evidence/state_effects-sets-013.md#s-3c85f9b12af37552)

### path-004423

```text
(exec)# test issu client register <cr>
```

Handler ` RVA 0xD4C7970 `；selector ` 0 `；EOL ` RVA 0x33E61478 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [状态效果 S-9a6fb32bd353261c](../../evidence/state_effects-sets-033.md#s-9a6fb32bd353261c)

### path-004378

```text
(exec)# test issu distributed show <cr>
```

Handler ` RVA 0xD4C7970 `；selector ` 0 `；EOL ` RVA 0x33E60B18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [状态效果 S-e5266006f3a06f86](../../evidence/state_effects-sets-048.md#s-e5266006f3a06f86)

### path-004627

```text
(exec)# test issu divc no-test <cr>
```

Handler ` RVA 0xD4BFE40 `；selector ` 0 `；EOL ` RVA 0x33E66EA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [状态效果 S-5b701c726f01449c](../../evidence/state_effects-sets-020.md#s-5b701c726f01449c)

### path-008190

```text
(exec)# test issu entity register <number:0..4294967295> <cr>
```

Handler ` RVA 0xD4C7970 `；selector ` 0 `；EOL ` RVA 0x33E618C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` entity id。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-a8d135807cc9287b](../../evidence/parameters-sets-013.md#p-a8d135807cc9287b) · [状态效果 S-01d5456e818f4778](../../evidence/state_effects-sets-001.md#s-01d5456e818f4778)

### path-011625

```text
(exec)# test issu injected calc_mtu <number:0..4294967295> <number:1..100> <number:1..100> <cr>
```

Handler ` RVA 0xD4BFC10 `；selector ` 0 `；EOL ` RVA 0x33E65928 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` session id；` unsigned_number ` message type；` unsigned_number ` negotiated version。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-853668705988955a](../../evidence/parameters-sets-010.md#p-853668705988955a)

### path-010541

```text
(exec)# test issu injected capability <number:0..4294967295> <number:1..100> <cr>
```

Handler ` RVA 0xD4BFCF0 `；selector ` 0 `；EOL ` RVA 0x33E65298 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` session id；` unsigned_number ` capability entry id。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-393798d128e2709a](../../evidence/parameters-sets-005.md#p-393798d128e2709a)

### path-010547

```text
(exec)# test issu injected comp_result <number:0..4294967295> <number:1..2> <cr>
```

Handler ` RVA 0xD4BFC80 `；selector ` 0 `；EOL ` RVA 0x33E655D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` session id；` unsigned_number ` compatible result。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-6361eb3e9623ecfb](../../evidence/parameters-sets-008.md#p-6361eb3e9623ecfb)

### path-011952

```text
(exec)# test issu injected message <number:0..4294967295> <number:1..100> <number:1..100> <number:1..100> <cr>
```

Handler ` RVA 0xD4BFD60 `；selector ` 0 `；EOL ` RVA 0x33E64F60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` session id；` unsigned_number ` message type；` unsigned_number ` negotiated version；` unsigned_number ` message mtu。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-7510cad559f30d36](../../evidence/parameters-sets-009.md#p-7510cad559f30d36)

### path-008239

```text
(exec)# test issu injected register <number:0..4294967295> <cr>
```

Handler ` RVA 0xD4BFDE0 `；selector ` 0 `；EOL ` RVA 0x33E64B98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` session id。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-0084d67a308f4e0e](../../evidence/parameters-sets-001.md#p-0084d67a308f4e0e)

### path-008220

```text
(exec)# test issu lossless session setup <cr>
```

Handler ` RVA 0xD4BF540 `；selector ` 0 `；EOL ` RVA 0x33E634F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [状态效果 S-d36a0f386ca5163f](../../evidence/state_effects-sets-045.md#s-d36a0f386ca5163f)

### path-011941

```text
(exec)# test issu message group register <number:1..4294967295> <number:1..100> <string> <cr>
```

Handler ` RVA 0xD4C7970 `；selector ` 0 `；EOL ` RVA 0x33E62520 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` entity id；` unsigned_number ` msg group id；` string ` msg type list ex: 1,2,3 - Comma needed。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-5853af0f9184149a](../../evidence/parameters-sets-007.md#p-5853af0f9184149a) · [状态效果 S-d72f5bbd5d97070b](../../evidence/state_effects-sets-046.md#s-d72f5bbd5d97070b)

### path-012074

```text
(exec)# test issu message type register <number:1..4294967295> <number:1..100> <number:1..5> <number:1..5> <cr>
```

Handler ` RVA 0xD4BF240 `；selector ` 0 `；EOL ` RVA 0x33E61F30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` entity id；` unsigned_number ` msg type；` unsigned_number ` low ver；` unsigned_number ` hi ver。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-c8d4fce5568ed841](../../evidence/parameters-sets-015.md#p-c8d4fce5568ed841) · [状态效果 S-ae10f3f754a313f2](../../evidence/state_effects-sets-037.md#s-ae10f3f754a313f2)

### path-012149

```text
(exec)# test issu message type register <number:1..4294967295> <number:1..100> <number:1..5> <number:1..5> <string> <cr>
```

Handler ` RVA 0xD4BF1A0 `；selector ` 0 `；EOL ` RVA 0x33E61F08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` entity id；` unsigned_number ` msg type；` unsigned_number ` low ver；` unsigned_number ` hi ver；` string ` dummy version list, ex: 2,3,5 - Comma needed。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-5787eb47f94b9f1d](../../evidence/parameters-sets-007.md#p-5787eb47f94b9f1d) · [状态效果 S-ae10f3f754a313f2](../../evidence/state_effects-sets-037.md#s-ae10f3f754a313f2)

### path-004563

```text
(exec)# test issu negative on <cr>
```

Handler ` RVA 0xD4C7970 `；selector ` 0 `；EOL ` RVA 0x33E66700 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [状态效果 S-f69dbde30662c4b7](../../evidence/state_effects-sets-052.md#s-f69dbde30662c4b7)

### path-011621

```text
(exec)# test issu nego-version config <number:1..4294967295> <number:1..100> <number:1..100> <cr>
```

Handler ` RVA 0xD4BF6C0 `；selector ` 0 `；EOL ` RVA 0x33E66400 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` session id；` unsigned_number ` Msg Type；` unsigned_number ` new negotiated version。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-84abe38d8cd95294](../../evidence/parameters-sets-010.md#p-84abe38d8cd95294)

### path-008255

```text
(exec)# test issu negotiate <number:1..4294967295> <number:0..1> <cr>
```

Handler ` RVA 0xD4C7970 `；selector ` 0 `；EOL ` RVA 0x33E65CB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` session id；` unsigned_number ` domain id。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-e3a16036306ccf7a](../../evidence/parameters-sets-017.md#p-e3a16036306ccf7a) · [状态效果 S-bb2af76b7870beb3](../../evidence/state_effects-sets-040.md#s-bb2af76b7870beb3)

### path-004613

```text
(exec)# test issu policy off <cr>
```

Handler ` RVA 0xD4C7970 `；selector ` 0 `；EOL ` RVA 0x33E66AD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [状态效果 S-680e85c5beb3637d](../../evidence/state_effects-sets-022.md#s-680e85c5beb3637d)

### path-004521

```text
(exec)# test issu session ipc <cr>
```

Handler ` RVA 0xD4C7970 `；selector ` 0 `；EOL ` RVA 0x33E63998 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [状态效果 S-c4b395bd3763f958](../../evidence/state_effects-sets-042.md#s-c4b395bd3763f958)

### path-011611

```text
(exec)# test issu shared message_session unregister <number:1..4294967295> <number:0..1> <cr>
```

Handler ` RVA 0xD4BFA00 `；selector ` 0 `；EOL ` RVA 0x33E64010 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` session id；` unsigned_number ` domain id。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-15f9d1914836288c](../../evidence/parameters-sets-002.md#p-15f9d1914836288c) · [状态效果 S-0120a83d7160b816](../../evidence/state_effects-sets-001.md#s-0120a83d7160b816)

### path-008267

```text
(exec)# test issu shared nego_session register <cr>
```

Handler ` RVA 0xD4BFB40 `；selector ` 0 `；EOL ` RVA 0x33E64428 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [状态效果 S-efc888695efbc66b](../../evidence/state_effects-sets-051.md#s-efc888695efbc66b)

### path-011614

```text
(exec)# test issu shared negotiate <number:1..4294967295> <number:1..4294967295> <number:0..1> <cr>
```

Handler ` RVA 0xD4BF7A0 `；selector ` 0 `；EOL ` RVA 0x33E64818 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number `  message session id；` unsigned_number `  negotiation session id；` unsigned_number ` domain id。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-002060df6e92087d](../../evidence/parameters-sets-001.md#p-002060df6e92087d)

### path-010540

```text
(exec)# test issu transform <number:1..4294967295> <number:1..100> <number:0..1> <cr>
```

Handler ` RVA 0xD4C7970 `；selector ` 0 `；EOL ` RVA 0x33E66040 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` session id；` unsigned_number ` Msg Type；` unsigned_number ` domain id。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-5bac2e1d7c4c7095](../../evidence/parameters-sets-007.md#p-5bac2e1d7c4c7095) · [状态效果 S-3bc40453bc0290f6](../../evidence/state_effects-sets-013.md#s-3bc40453bc0290f6)

### path-000316

```text
(exec)# test l2protocol-forward <cr>
```

Handler ` RVA 0x15FD9700 `；selector ` 32 `；EOL ` RVA 0x35E87788 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b8bf6a5a94b9fbb4](../../evidence/conditions-sets-071.md#c-b8bf6a5a94b9fbb4)

### path-012600

```text
(exec)# test l2protocol-forward <interface> <cr>
```

Handler ` RVA 0x15FD93E0 `；selector ` 32 `；EOL ` RVA 0x35E87760 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b1a4ddbafbdb68a8](../../evidence/conditions-sets-069.md#c-b1a4ddbafbdb68a8) · [缺口 G-7bb168c8bbfcb9de](../../evidence/gaps-sets-005.md#g-7bb168c8bbfcb9de) · [参数 P-ea0e6cb5a4df3956](../../evidence/parameters-sets-018.md#p-ea0e6cb5a4df3956)

### path-000314

```text
(exec)# test l2protocol-tunnel <cr>
```

Handler ` RVA 0x15FD9700 `；selector ` 31 `；EOL ` RVA 0x35E871A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-deebdbb24a64c9b4](../../evidence/conditions-sets-086.md#c-deebdbb24a64c9b4)

### path-012598

```text
(exec)# test l2protocol-tunnel <interface> <cr>
```

Handler ` RVA 0x15FD93E0 `；selector ` 31 `；EOL ` RVA 0x35E87178 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-94d5098b7af92149](../../evidence/conditions-sets-058.md#c-94d5098b7af92149) · [缺口 G-5fa858f690b7f4c6](../../evidence/gaps-sets-004.md#g-5fa858f690b7f4c6) · [参数 P-a539e5e2eae972e5](../../evidence/parameters-sets-013.md#p-a539e5e2eae972e5)

### path-006507

```text
(exec)# test lacp disable insert-seq-num <cr>
```

Handler ` RVA 0xC8D36F0 `；selector ` 0 `；EOL ` RVA 0x33B15208 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [状态效果 S-38f5ee16a3428e38](../../evidence/state_effects-sets-013.md#s-38f5ee16a3428e38)

### path-006473

```text
(exec)# test lacp disable recv <cr>
```

Handler ` RVA 0xC8D3680 `；selector ` 0 `；EOL ` RVA 0x33B14F60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [状态效果 S-38f5ee16a3428e38](../../evidence/state_effects-sets-013.md#s-38f5ee16a3428e38)

### path-006432

```text
(exec)# test lacp disable send <cr>
```

Handler ` RVA 0xC8D3610 `；selector ` 0 `；EOL ` RVA 0x33B14CB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [状态效果 S-38f5ee16a3428e38](../../evidence/state_effects-sets-013.md#s-38f5ee16a3428e38)

### path-006530

```text
(exec)# test lacp enable insert-seq-num <cr>
```

Handler ` RVA 0xC8D36F0 `；selector ` 0 `；EOL ` RVA 0x33B15A78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [状态效果 S-60aba3477c0fe1ae](../../evidence/state_effects-sets-021.md#s-60aba3477c0fe1ae)

### path-006504

```text
(exec)# test lacp enable recv <cr>
```

Handler ` RVA 0xC8D3680 `；selector ` 0 `；EOL ` RVA 0x33B157D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [状态效果 S-60aba3477c0fe1ae](../../evidence/state_effects-sets-021.md#s-60aba3477c0fe1ae)

### path-006468

```text
(exec)# test lacp enable send <cr>
```

Handler ` RVA 0xC8D3610 `；selector ` 0 `；EOL ` RVA 0x33B15528 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [状态效果 S-60aba3477c0fe1ae](../../evidence/state_effects-sets-021.md#s-60aba3477c0fe1ae)

### path-009524

```text
(exec)# test lacp multi-chassis iccp-version <number:0..65535> <cr>
```

Handler ` RVA 0xC960530 `；selector ` 0 `；EOL ` RVA 0x33B38290 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Version in ICCP connection TLV。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-1fc392fcc1ad0e26](../../evidence/parameters-sets-003.md#p-1fc392fcc1ad0e26) · [状态效果 S-8f45fa6a609cf74d](../../evidence/state_effects-sets-030.md#s-8f45fa6a609cf74d)

### path-019091

```text
(exec)# test lacp sync-bit set <interface> <cr>
```

Handler ` RVA 0xC8D33C0 `；selector ` 0 `；EOL ` RVA 0x33B16328 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e9ab0016fdfb8338](../../evidence/conditions-sets-090.md#c-e9ab0016fdfb8338) · [缺口 G-1fc8a6c7c11b148c](../../evidence/gaps-sets-002.md#g-1fc8a6c7c11b148c) · [参数 P-a7ffa45be4f41a3b](../../evidence/parameters-sets-013.md#p-a7ffa45be4f41a3b) · [状态效果 S-4f011870870be79e](../../evidence/state_effects-sets-017.md#s-4f011870870be79e)

### path-025348

```text
(exec)# test lacp sync-bit switch <interface> <interface> <cr>
```

Handler ` RVA 0xC8D34C0 `；selector ` 0 `；EOL ` RVA 0x33B15F30 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f1547b721d7f61b6](../../evidence/conditions-sets-093.md#c-f1547b721d7f61b6) · [缺口 G-272b31ada0f209f8](../../evidence/gaps-sets-002.md#g-272b31ada0f209f8) · [参数 P-c5ac7ba310175862](../../evidence/parameters-sets-015.md#p-c5ac7ba310175862)

### path-011287

```text
(exec)# test lacp timer wait fast default <cr>
```

Handler ` RVA 0xC8D32D0 `；selector ` 0 `；EOL ` RVA 0x33B166F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [状态效果 S-19c31f3082eac26a](../../evidence/state_effects-sets-006.md#s-19c31f3082eac26a)

### path-016944

```text
(exec)# test license smart factory-reset clear all <cr>
```

Handler ` RVA 0xBB47540 `；selector ` 0 `；EOL ` RVA 0x33856CA0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-48b2236ba0e29e76](../../evidence/conditions-sets-029.md#c-48b2236ba0e29e76) · [缺口 G-35063cd6f80afd0d](../../evidence/gaps-sets-002.md#g-35063cd6f80afd0d) · [状态效果 S-ffe3f177539b276d](../../evidence/state_effects-sets-054.md#s-ffe3f177539b276d)

### path-004702

```text
(exec)# test license smart tech-support <cr>
```

Handler ` RVA 0xBB47540 `；selector ` 0 `；EOL ` RVA 0x33856CA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-53b3d4657d4e6713](../../evidence/conditions-sets-033.md#c-53b3d4657d4e6713) · [状态效果 S-0d9df339e31ca7dc](../../evidence/state_effects-sets-003.md#s-0d9df339e31ca7dc)

### path-004619

```text
(exec)# test lim proximity-db enable <cr>
```

Handler ` RVA 0xC9242D0 `；selector ` 1 `；EOL ` RVA 0x33B1E4A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a2a91441a037a770](../../evidence/conditions-sets-063.md#c-a2a91441a037a770) · [状态效果 S-f2dcaa2624ee65f5](../../evidence/state_effects-sets-051.md#s-f2dcaa2624ee65f5)

### path-021834

```text
(exec)# test mac-table-mibs get-addr-info vlan <number:dynamic> <address> <cr>
```

Handler ` RVA 0x15E77C10 `；selector ` 17 `；EOL ` RVA 0x35E4FC90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` VLAN Id value；` address ` 48 bit mac address。

[条件 C-5fc9fe33c59ebf00](../../evidence/conditions-sets-037.md#c-5fc9fe33c59ebf00) · [缺口 G-884350b12689720b](../../evidence/gaps-sets-005.md#g-884350b12689720b) · [参数 P-f819bcc27cd2479e](../../evidence/parameters-sets-018.md#p-f819bcc27cd2479e)

### path-017927

```text
(exec)# test mac-table-mibs get-aging vlan <number:dynamic> <cr>
```

Handler ` RVA 0x15E77C10 `；selector ` 14 `；EOL ` RVA 0x35E4F1F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` VLAN Id vlaue。

[条件 C-73d0818295230843](../../evidence/conditions-sets-045.md#c-73d0818295230843) · [缺口 G-56d51312f2024c84](../../evidence/gaps-sets-003.md#g-56d51312f2024c84) · [参数 P-cd8a702da351f59c](../../evidence/parameters-sets-016.md#p-cd8a702da351f59c)

### path-018049

```text
(exec)# test mac-table-mibs get-igmp-status vlan <number:dynamic> <cr>
```

Handler ` RVA 0x15E77C10 `；selector ` 23 `；EOL ` RVA 0x35E51308 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` VLAN Id value。

[条件 C-3724a84ea012f3a7](../../evidence/conditions-sets-021.md#c-3724a84ea012f3a7) · [缺口 G-6794891567c77f78](../../evidence/gaps-sets-004.md#g-6794891567c77f78) · [参数 P-37177cb18223b496](../../evidence/parameters-sets-005.md#p-37177cb18223b496)

### path-018028

```text
(exec)# test mac-table-mibs get-learned-discards vlan <number:dynamic> <cr>
```

Handler ` RVA 0x15E77C10 `；selector ` 22 `；EOL ` RVA 0x35E50FC8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` VLAN Id value。

[条件 C-14492ee2b607dc71](../../evidence/conditions-sets-008.md#c-14492ee2b607dc71) · [缺口 G-e5f0dec673e6be26](../../evidence/gaps-sets-008.md#g-e5f0dec673e6be26) · [参数 P-de85b204d9d90a05](../../evidence/parameters-sets-017.md#p-de85b204d9d90a05)

### path-017953

```text
(exec)# test mac-table-mibs get-next-addr vlan <number:dynamic> <cr>
```

Handler ` RVA 0x15E77C10 `；selector ` 16 `；EOL ` RVA 0x35E4F908 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` VLAN Id value。

[条件 C-111ac03e496d47b4](../../evidence/conditions-sets-007.md#c-111ac03e496d47b4) · [缺口 G-f1d74e17fe7b29bb](../../evidence/gaps-sets-008.md#g-f1d74e17fe7b29bb) · [参数 P-dea280cc3bb04afc](../../evidence/parameters-sets-017.md#p-dea280cc3bb04afc)

### path-023983

```text
(exec)# test mac-table-mibs get-next-staticaddr vlan <number:dynamic> port <number:0..128> <cr>
```

Handler ` RVA 0x15E77C10 `；selector ` 18 `；EOL ` RVA 0x35E50050 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` VLAN Id value；` unsigned_number ` Port Index。

[条件 C-a49a72c86d53fe31](../../evidence/conditions-sets-063.md#c-a49a72c86d53fe31) · [缺口 G-d017013f3c09b903](../../evidence/gaps-sets-007.md#g-d017013f3c09b903) · [参数 P-9bfa3904934995f3](../../evidence/parameters-sets-012.md#p-9bfa3904934995f3)

### path-023973

```text
(exec)# test mac-table-mibs set-aging vlan <number:dynamic> aging-time <number:0..1000000> <cr>
```

Handler ` RVA 0x15E77C10 `；selector ` 15 `；EOL ` RVA 0x35E4F5C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` VLAN Id value；` unsigned_number ` Aging Time Value。

[条件 C-b1a1aa14853f801c](../../evidence/conditions-sets-069.md#c-b1a1aa14853f801c) · [缺口 G-21cac691862d1024](../../evidence/gaps-sets-002.md#g-21cac691862d1024) · [参数 P-df2cbee7cad77c52](../../evidence/parameters-sets-017.md#p-df2cbee7cad77c52)

### path-024008

```text
(exec)# test mac-table-mibs set-cpu-addr <address> vlan <number:dynamic> <number:1..2> <cr>
```

Handler ` RVA 0x15E77C10 `；selector ` 24 `；EOL ` RVA 0x35E516A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` 48 bit mac address；` unsigned_number_dynamic ` VLAN Id value；` unsigned_number ` Add/Del Addr。

[条件 C-94d43e8c2b8c9f47](../../evidence/conditions-sets-058.md#c-94d43e8c2b8c9f47) · [缺口 G-7b004d3552174b95](../../evidence/gaps-sets-005.md#g-7b004d3552174b95) · [参数 P-e22713caaaf5ba98](../../evidence/parameters-sets-017.md#p-e22713caaaf5ba98)

### path-024770

```text
(exec)# test mac-table-mibs set-delete-status vlan <number:dynamic> port <number:0..128> <address> <cr>
```

Handler ` RVA 0x15E77C10 `；selector ` 20 `；EOL ` RVA 0x35E50878 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` VLAN Id value；` unsigned_number ` Port Index；` address ` 48 bit mac address。

[条件 C-3c4d80269498b41c](../../evidence/conditions-sets-023.md#c-3c4d80269498b41c) · [缺口 G-212f9ad1fa331ae1](../../evidence/gaps-sets-002.md#g-212f9ad1fa331ae1) · [参数 P-ca3a06e86fe14a13](../../evidence/parameters-sets-015.md#p-ca3a06e86fe14a13)

### path-024771

```text
(exec)# test mac-table-mibs set-invalid-status vlan <number:dynamic> port <number:0..128> <address> <cr>
```

Handler ` RVA 0x15E77C10 `；selector ` 21 `；EOL ` RVA 0x35E50C88 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` VLAN Id value；` unsigned_number ` Port Index；` address ` 48 bit mac address。

[条件 C-689dc18c4a3482a6](../../evidence/conditions-sets-040.md#c-689dc18c4a3482a6) · [缺口 G-cabb78a09e6ce200](../../evidence/gaps-sets-007.md#g-cabb78a09e6ce200) · [参数 P-c4d90c82d0dc9ce4](../../evidence/parameters-sets-015.md#p-c4d90c82d0dc9ce4)

### path-024769

```text
(exec)# test mac-table-mibs set-permanent-status vlan <number:dynamic> port <number:0..128> <address> <cr>
```

Handler ` RVA 0x15E77C10 `；selector ` 19 `；EOL ` RVA 0x35E50468 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` VLAN Id value；` unsigned_number ` Port Index；` address ` 48 bit mac address。

[条件 C-ccf7252862d803a0](../../evidence/conditions-sets-079.md#c-ccf7252862d803a0) · [缺口 G-d1b0c674efc6b2be](../../evidence/gaps-sets-007.md#g-d1b0c674efc6b2be) · [参数 P-640d72e8c68ba40c](../../evidence/parameters-sets-008.md#p-640d72e8c68ba40c)

### path-012185

```text
(exec)# test mdns browse regtype <string> domain <string> periodicity <number:0..4294967295> interface <number:0..4294967295> <cr>
```

Handler ` RVA 0x142AA8B0 `；selector ` 0 `；EOL ` RVA 0x35D12E90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Specify in this form _servicename._protocol；` string ` Specify Domain or 0 for NULL；` unsigned_number ` Specify Periodicity in seconds；` unsigned_number ` Specify interface Index。

[条件 C-13390d35dddb1359](../../evidence/conditions-sets-008.md#c-13390d35dddb1359) · [参数 P-a5635059931d6d21](../../evidence/parameters-sets-013.md#p-a5635059931d6d21)

### path-008746

```text
(exec)# test mdns browse stop <number:1..4294967295> <cr>
```

Handler ` RVA 0x142AA9D0 `；selector ` 0 `；EOL ` RVA 0x35D13180 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Enter Request ID value。

[条件 C-4323fecd907d6eed](../../evidence/conditions-sets-026.md#c-4323fecd907d6eed) · [参数 P-f5e43b71021fa86d](../../evidence/parameters-sets-018.md#p-f5e43b71021fa86d)

### path-001396

```text
(exec)# test mdns cache <cr>
```

Handler ` RVA 0x142ABBE0 `；selector ` 1 `；EOL ` RVA 0x35D14068 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cdeb48af9d6b443c](../../evidence/conditions-sets-079.md#c-cdeb48af9d6b443c)

### path-013569

```text
(exec)# test mdns intf-wdraw <interface> <cr>
```

Handler ` RVA 0x142AC590 `；selector ` 10 `；EOL ` RVA 0x35D12428 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1ff890e5b8067c7f](../../evidence/conditions-sets-012.md#c-1ff890e5b8067c7f) · [缺口 G-428884fbd90f64a2](../../evidence/gaps-sets-003.md#g-428884fbd90f64a2) · [参数 P-46d1f66fe55d85f9](../../evidence/parameters-sets-006.md#p-46d1f66fe55d85f9)

### path-011717

```text
(exec)# test mdns resolve host <string> interface <number:0..4294967295> <cr>
```

Handler ` RVA 0x142AAC10 `；selector ` 0 `；EOL ` RVA 0x35D13A58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Specify HostName to Resolve；` unsigned_number ` Specify Interface Index。

[条件 C-b987c6223dae83b5](../../evidence/conditions-sets-072.md#c-b987c6223dae83b5) · [参数 P-0467657afa55ba03](../../evidence/parameters-sets-001.md#p-0467657afa55ba03)

### path-012186

```text
(exec)# test mdns resolve service <string> regtype <string> domain <string> interface <number:0..4294967295> <cr>
```

Handler ` RVA 0x142AAAF0 `；selector ` 0 `；EOL ` RVA 0x35D13670 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Service Instance Name；` string ` Specify in this form _servicename._protocol；` string ` Specify Domain name or 0 for NULL；` unsigned_number ` Specify Interface Index。

[条件 C-87b72df779a70c36](../../evidence/conditions-sets-052.md#c-87b72df779a70c36) · [参数 P-7a2f34b5b2da854f](../../evidence/parameters-sets-010.md#p-7a2f34b5b2da854f)

### path-001245

```text
(exec)# test mdns resync <cr>
```

Handler ` RVA 0x142AC590 `；selector ` 9 `；EOL ` RVA 0x35D12098 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4ef83fd400480529](../../evidence/conditions-sets-031.md#c-4ef83fd400480529)

### path-004984

```text
(exec)# test mdns srv-enum <number:0..1> <cr>
```

Handler ` RVA 0x142AC590 `；selector ` 11 `；EOL ` RVA 0x35D11E10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Enter 0 for clear and 1 for request。

[条件 C-0b3ff354e90ab8d3](../../evidence/conditions-sets-005.md#c-0b3ff354e90ab8d3) · [参数 P-79203c4ca1832bbb](../../evidence/parameters-sets-009.md#p-79203c4ca1832bbb)

### path-001278

```text
(exec)# test mdns start <cr>
```

Handler ` RVA 0x142AC590 `；selector ` 0 `；EOL ` RVA 0x35D126E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9375bf6b879237e9](../../evidence/conditions-sets-057.md#c-9375bf6b879237e9)

### path-001293

```text
(exec)# test mdns stop <cr>
```

Handler ` RVA 0x142AC590 `；selector ` 1 `；EOL ` RVA 0x35D12990 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c3bb8ed1fefa860f](../../evidence/conditions-sets-076.md#c-c3bb8ed1fefa860f)

### path-011714

```text
(exec)# test mdns update bssid <address> client-mac <address> <cr>
```

Handler ` RVA 0x142ABAD0 `；selector ` 1 `；EOL ` RVA 0x35D14590 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` 48 bit mac address；` address ` 48 bit mac address。

[条件 C-1303dcd8eb5786b3](../../evidence/conditions-sets-008.md#c-1303dcd8eb5786b3) · [参数 P-54086fa71b463a2f](../../evidence/parameters-sets-007.md#p-54086fa71b463a2f)

### path-010866

```text
(exec)# test mdns update query-pak bssid-mac <address> <cr>
```

Handler ` RVA 0x142ABA60 `；selector ` 1 `；EOL ` RVA 0x35D148A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` 48 bit mac address。

[条件 C-1901f0514a971661](../../evidence/conditions-sets-010.md#c-1901f0514a971661) · [参数 P-cb5e5912b30e3de5](../../evidence/parameters-sets-015.md#p-cb5e5912b30e3de5)

### path-000136

```text
(exec)# test memory <cr>
```

Handler ` RVA 0xE8F44F0 `；selector ` 0 `；EOL ` RVA 0x3433F0E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-391637fe0bc02762](../../evidence/conditions-sets-022.md#c-391637fe0bc02762)

### path-011632

```text
(exec)# test memory allocate processor <number:0..4294967294> <number:0..4294967294> <number:0..4294967294> <cr>
```

Handler ` RVA 0xD79CC10 `；selector ` 0 `；EOL ` RVA 0x33EE8290 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` alignment；` unsigned_number ` number of allocations；` unsigned_number ` size of each allocated block。

[条件 C-391637fe0bc02762](../../evidence/conditions-sets-022.md#c-391637fe0bc02762) · [参数 P-493f9cb9de8c2f52](../../evidence/parameters-sets-006.md#p-493f9cb9de8c2f52) · [状态效果 S-7b999f71d6dbdc99](../../evidence/state_effects-sets-026.md#s-7b999f71d6dbdc99)

### path-017093

```text
(exec)# test memory chunk lock <?general_pointer_number_action@55558943eb28> <cr>
```

Handler ` RVA 0xD79B8E0 `；selector ` 0 `；EOL ` RVA 0x33EEAB90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08349088d0705dd4](../../evidence/conditions-sets-004.md#c-08349088d0705dd4) · [缺口 G-3e3424abb7c82a29](../../evidence/gaps-sets-003.md#g-3e3424abb7c82a29)

### path-017105

```text
(exec)# test memory chunk refcount <?general_pointer_number_action@55558943ee20> <cr>
```

Handler ` RVA 0xD79B950 `；selector ` 0 `；EOL ` RVA 0x33EEAE60 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08349088d0705dd4](../../evidence/conditions-sets-004.md#c-08349088d0705dd4) · [缺口 G-894740e478c6950d](../../evidence/gaps-sets-005.md#g-894740e478c6950d)

### path-004589

```text
(exec)# test memory create dangling-reference <cr>
```

Handler ` RVA 0xD79C2F0 `；selector ` 0 `；EOL ` RVA 0x33EE8D28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-391637fe0bc02762](../../evidence/conditions-sets-022.md#c-391637fe0bc02762) · [状态效果 S-ee8155c2c8f1ad31](../../evidence/state_effects-sets-050.md#s-ee8155c2c8f1ad31)

### path-011637

```text
(exec)# test memory create leak type1 <number:28..4294967295> <number:1..4294967295> <cr>
```

Handler ` RVA 0xD79C5D0 `；selector ` 0 `；EOL ` RVA 0x33EE9470 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` size of blocks to leak；` unsigned_number ` number of blocks to leak。

[条件 C-391637fe0bc02762](../../evidence/conditions-sets-022.md#c-391637fe0bc02762) · [参数 P-e7de55dec44fbd77](../../evidence/parameters-sets-017.md#p-e7de55dec44fbd77) · [状态效果 S-18afca3413cf668d](../../evidence/state_effects-sets-006.md#s-18afca3413cf668d)

### path-024589

```text
(exec)# test memory create leak type1 chunk <?general_pointer_number_action@55558943d098> <number:1..4294967295> <cr>
```

Handler ` RVA 0xD79C7E0 `；selector ` 0 `；EOL ` RVA 0x33EE9150 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` number of chunk elements to leak。

[条件 C-391637fe0bc02762](../../evidence/conditions-sets-022.md#c-391637fe0bc02762) · [缺口 G-c792ef09578ce8ea](../../evidence/gaps-sets-007.md#g-c792ef09578ce8ea) · [参数 P-d9d3b29a49c1919e](../../evidence/parameters-sets-016.md#p-d9d3b29a49c1919e) · [状态效果 S-18afca3413cf668d](../../evidence/state_effects-sets-006.md#s-18afca3413cf668d)

### path-021000

```text
(exec)# test memory delay-sibling-free <?general_pointer_number_action@55558943d778> <number:0..1> <number:0..1> <cr>
```

Handler ` RVA 0xD79BFE0 `；selector ` 0 `；EOL ` RVA 0x33EE9878 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` 0 for disabling and 1 for enabling；` unsigned_number ` 0 not to suspend and 1 to suspend while freeing the siblings。

[条件 C-391637fe0bc02762](../../evidence/conditions-sets-022.md#c-391637fe0bc02762) · [缺口 G-3ea430db00582304](../../evidence/gaps-sets-003.md#g-3ea430db00582304) · [参数 P-ddd211b15a703d3f](../../evidence/parameters-sets-017.md#p-ddd211b15a703d3f)

### path-017023

```text
(exec)# test memory destroy chunk <?general_pointer_number_action@55558943dc08> <cr>
```

Handler ` RVA 0xD79C970 `；selector ` 0 `；EOL ` RVA 0x33EE9C70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-391637fe0bc02762](../../evidence/conditions-sets-022.md#c-391637fe0bc02762) · [缺口 G-518a8b54e36141fe](../../evidence/gaps-sets-003.md#g-518a8b54e36141fe)

### path-004659

```text
(exec)# test memory history <number:1..60> <cr>
```

Handler ` RVA 0xD79B850 `；selector ` 0 `；EOL ` RVA 0x33EEA5B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Period of history collection in minutes。

[条件 C-08349088d0705dd4](../../evidence/conditions-sets-004.md#c-08349088d0705dd4) · [参数 P-bff5968e13295850](../../evidence/parameters-sets-015.md#p-bff5968e13295850)

### path-000725

```text
(exec)# test memory nvram-multibus <cr>
```

Handler ` RVA 0xE8F44F0 `；selector ` 0 `；EOL ` RVA 0x3433EE50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-391637fe0bc02762](../../evidence/conditions-sets-022.md#c-391637fe0bc02762)

### path-021059

```text
(exec)# test memory overflow <?general_pointer_number_action@55558943dfe8> <number:0..4294967294> <number:0..4294967294> <cr>
```

Handler ` RVA 0xD79CA50 `；selector ` 0 `；EOL ` RVA 0x33EEA0E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` size of the corruption in words；` unsigned_number ` corruption pattern。

[条件 C-91c5c28cb393636c](../../evidence/conditions-sets-056.md#c-91c5c28cb393636c) · [缺口 G-428e2243ef5fda03](../../evidence/gaps-sets-003.md#g-428e2243ef5fda03) · [参数 P-dae1cb7bff83826c](../../evidence/parameters-sets-016.md#p-dae1cb7bff83826c)

### path-013137

```text
(exec)# test memory transfer <?general_pointer_number_action@55558943c6e0> <cr>
```

Handler ` RVA 0xD79CC10 `；selector ` 0 `；EOL ` RVA 0x33EE8290 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-391637fe0bc02762](../../evidence/conditions-sets-022.md#c-391637fe0bc02762) · [缺口 G-c83e41a6aa9aa77e](../../evidence/gaps-sets-007.md#g-c83e41a6aa9aa77e) · [状态效果 S-4d177d4224121046](../../evidence/state_effects-sets-017.md#s-4d177d4224121046)

### path-012197

```text
(exec)# test mfib cb-support IPv4 add group <address> source <address> vrf <number:0..100> intf <number:0..255> <cr>
```

Handler ` RVA 0x11957C90 `；selector ` 1 `；EOL ` RVA 0x355AFA00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` group address；` address ` source address；` unsigned_number ` vrf id；` unsigned_number ` if_number。

[条件 C-cae13a57f800f2d3](../../evidence/conditions-sets-078.md#c-cae13a57f800f2d3) · [参数 P-f3f238ba8bd70d5c](../../evidence/parameters-sets-018.md#p-f3f238ba8bd70d5c) · [状态效果 S-5781b29d3ccbc997](../../evidence/state_effects-sets-019.md#s-5781b29d3ccbc997)

### path-012198

```text
(exec)# test mfib cb-support IPv6 add group <address> source <address> vrf <number:0..100> intf <number:0..255> <cr>
```

Handler ` RVA 0x11957C90 `；selector ` 2 `；EOL ` RVA 0x355AFFE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` group address；` address ` source address；` unsigned_number ` vrf id；` unsigned_number ` if_number。

[条件 C-cae13a57f800f2d3](../../evidence/conditions-sets-078.md#c-cae13a57f800f2d3) · [参数 P-b9f20fac51ecc555](../../evidence/parameters-sets-014.md#p-b9f20fac51ecc555) · [状态效果 S-add45da315d7f4d4](../../evidence/state_effects-sets-037.md#s-add45da315d7f4d4)

### path-001699

```text
(exec)# test mfib channel <cr>
```

Handler ` RVA 0x11667890 `；selector ` 0 `；EOL ` RVA 0x35524680 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-100b38edda4757c6](../../evidence/conditions-sets-006.md#c-100b38edda4757c6)

### path-001564

```text
(exec)# test mfib enable <cr>
```

Handler ` RVA 0x11949710 `；selector ` 0 `；EOL ` RVA 0x355AC7B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c063568e2cb65da0](../../evidence/conditions-sets-074.md#c-c063568e2cb65da0) · [状态效果 S-3e56a4fcf95480d3](../../evidence/state_effects-sets-014.md#s-3e56a4fcf95480d3)

### path-017950

```text
(exec)# test mfib epoch new <?option@55558aafa690> <cr>
```

Handler ` RVA 0x118FAFB0 `；selector ` 0 `；EOL ` RVA 0x355A6730 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7f8502c29f1fbe7c](../../evidence/conditions-sets-049.md#c-7f8502c29f1fbe7c) · [缺口 G-f56498c9e9ed6be6](../../evidence/gaps-sets-008.md#g-f56498c9e9ed6be6) · [状态效果 S-9f11123e62d1c2b3](../../evidence/state_effects-sets-034.md#s-9f11123e62d1c2b3)

### path-005460

```text
(exec)# test mfib epoch new <cr>
```

Handler ` RVA 0x118FAFB0 `；selector ` 0 `；EOL ` RVA 0x355A6730 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c8f2d51e4fb8c4ae](../../evidence/conditions-sets-077.md#c-c8f2d51e4fb8c4ae) · [状态效果 S-6b93bf467952442b](../../evidence/state_effects-sets-023.md#s-6b93bf467952442b)

### path-001663

```text
(exec)# test mfib mrib <cr>
```

Handler ` RVA 0x1196AC30 `；selector ` 0 `；EOL ` RVA 0x355AF460 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cae13a57f800f2d3](../../evidence/conditions-sets-078.md#c-cae13a57f800f2d3)

### path-013975

```text
(exec)# test mfib mrib <number:dynamic> <cr>
```

Handler ` RVA 0x1196AC30 `；selector ` 0 `；EOL ` RVA 0x355AF460 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` error duration (milliseconds)。

[条件 C-237b7ac20a0fe894](../../evidence/conditions-sets-014.md#c-237b7ac20a0fe894) · [缺口 G-6aeaa43c969bb7b7](../../evidence/gaps-sets-004.md#g-6aeaa43c969bb7b7) · [参数 P-b3d6337a30e0851e](../../evidence/parameters-sets-014.md#p-b3d6337a30e0851e) · [状态效果 S-3b5cf6e6bd04bff8](../../evidence/state_effects-sets-013.md#s-3b5cf6e6bd04bff8)

### path-001717

```text
(exec)# test mfib reload <cr>
```

Handler ` RVA 0x11667B00 `；selector ` 0 `；EOL ` RVA 0x35524B30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-553f65663477b480](../../evidence/conditions-sets-033.md#c-553f65663477b480)

### path-001109

```text
(exec)# test mgd-timer watch <cr>
```

Handler ` RVA 0xD7AD830 `；selector ` 0 `；EOL ` RVA 0x33EF0C08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [状态效果 S-d058efbf7205e07c](../../evidence/state_effects-sets-044.md#s-d058efbf7205e07c)

### path-024267

```text
(exec)# test mka linksec start interface <interface> preshared <cr>
```

Handler ` RVA 0x16085270 `；selector ` 8 `；EOL ` RVA 0x35EBB090 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-98e2d4b5344b29a5](../../evidence/conditions-sets-059.md#c-98e2d4b5344b29a5) · [缺口 G-c3a4d69e2c4b6087](../../evidence/gaps-sets-007.md#g-c3a4d69e2c4b6087) · [参数 P-b23d7e6994cdff39](../../evidence/parameters-sets-014.md#p-b23d7e6994cdff39) · [状态效果 S-98399bccdd3f8774](../../evidence/state_effects-sets-032.md#s-98399bccdd3f8774)

### path-006497

```text
(exec)# test mka macsec-sim off <cr>
```

Handler ` RVA 0x16085270 `；selector ` 1 `；EOL ` RVA 0x35EB9D78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d1482e4e73ff99d8](../../evidence/conditions-sets-081.md#c-d1482e4e73ff99d8) · [状态效果 S-ae5efbbf44f9cba2](../../evidence/state_effects-sets-037.md#s-ae5efbbf44f9cba2)

### path-009562

```text
(exec)# test mka message-number initial-value <number:1..4294967295> <cr>
```

Handler ` RVA 0x16085270 `；selector ` 2 `；EOL ` RVA 0x35EBA128 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` 32-bit Message Number (default = 1)。

[条件 C-2c10eb37fd6af5cb](../../evidence/conditions-sets-017.md#c-2c10eb37fd6af5cb) · [参数 P-2cc60459240682de](../../evidence/parameters-sets-004.md#p-2cc60459240682de)

### path-009579

```text
(exec)# test mka message-number window-size <number:0..4294967295> <cr>
```

Handler ` RVA 0x16085270 `；selector ` 5 `；EOL ` RVA 0x35EBA3F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` MN Window Size - # of MKPDUs (default = 0, off)。

[条件 C-2c10eb37fd6af5cb](../../evidence/conditions-sets-017.md#c-2c10eb37fd6af5cb) · [参数 P-76ba54810b928371](../../evidence/parameters-sets-009.md#p-76ba54810b928371)

### path-009595

```text
(exec)# test mka packet-number initial-value <number:0..4294967295> <cr>
```

Handler ` RVA 0x16085270 `；selector ` 6 `；EOL ` RVA 0x35EBABB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` 32-bit Packet Number (default = 1, PendingPNExhaustion at 3221225472)。

[条件 C-2c10eb37fd6af5cb](../../evidence/conditions-sets-017.md#c-2c10eb37fd6af5cb) · [参数 P-5f2a7ac5cf4b91bf](../../evidence/parameters-sets-008.md#p-5f2a7ac5cf4b91bf)

### path-025361

```text
(exec)# test mka sak-rekey ckn <hex-string> interface <interface> <cr>
```

Handler ` RVA 0x16085270 `；selector ` 7 `；EOL ` RVA 0x35EBA838 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` hexstring ` 128-bit Hexadecimal CKN。

[条件 C-f1499427385353b1](../../evidence/conditions-sets-093.md#c-f1499427385353b1) · [缺口 G-1a10bfb2d00b04c4](../../evidence/gaps-sets-001.md#g-1a10bfb2d00b04c4) · [参数 P-08bbea5392940b87](../../evidence/parameters-sets-001.md#p-08bbea5392940b87)

### path-002003

```text
(exec)# test mock btrace <cr>
```

Handler ` RVA 0x1653EB30 `；selector ` 4 `；EOL ` RVA 0x35FA0940 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-71e9699c7860bed3](../../evidence/conditions-sets-044.md#c-71e9699c7860bed3)

### path-002042

```text
(exec)# test mock chasfs <cr>
```

Handler ` RVA 0x1653EB30 `；selector ` 6 `；EOL ` RVA 0x35FA0E90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a676280344836c0b](../../evidence/conditions-sets-064.md#c-a676280344836c0b)

### path-002019

```text
(exec)# test mock chassis <cr>
```

Handler ` RVA 0x1653EB30 `；selector ` 5 `；EOL ` RVA 0x35FA0BE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c04c722c138e83e2](../../evidence/conditions-sets-074.md#c-c04c722c138e83e2)

### path-002099

```text
(exec)# test mock crypto <cr>
```

Handler ` RVA 0x1653EB30 `；selector ` 18 `；EOL ` RVA 0x35FA1930 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-eeb5ba0b1c800bd7](../../evidence/conditions-sets-092.md#c-eeb5ba0b1c800bd7)

### path-002052

```text
(exec)# test mock cyan <cr>
```

Handler ` RVA 0x1653EB30 `；selector ` 7 `；EOL ` RVA 0x35FA1138 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-730afb9a1dde6901](../../evidence/conditions-sets-044.md#c-730afb9a1dde6901)

### path-001984

```text
(exec)# test mock ei <cr>
```

Handler ` RVA 0x1653EB30 `；selector ` 8 `；EOL ` RVA 0x35FA0698 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ae63daa4b329aab2](../../evidence/conditions-sets-067.md#c-ae63daa4b329aab2)

### path-005674

```text
(exec)# test mock infra enqueue <cr>
```

Handler ` RVA 0x1653EB30 `；selector ` 1 `；EOL ` RVA 0x35F9F7E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a638a345f05fa8c2](../../evidence/conditions-sets-064.md#c-a638a345f05fa8c2) · [状态效果 S-fefd0af894d9851a](../../evidence/state_effects-sets-054.md#s-fefd0af894d9851a)

### path-001952

```text
(exec)# test mock ipc <cr>
```

Handler ` RVA 0x1653EB30 `；selector ` 11 `；EOL ` RVA 0x35FA0148 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c2c6586647f7be09](../../evidence/conditions-sets-075.md#c-c2c6586647f7be09)

### path-001932

```text
(exec)# test mock mcp <cr>
```

Handler ` RVA 0x1653EB30 `；selector ` 2 `；EOL ` RVA 0x35F9FEA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9be50e71f4ba7c1c](../../evidence/conditions-sets-060.md#c-9be50e71f4ba7c1c)

### path-001970

```text
(exec)# test mock misc <cr>
```

Handler ` RVA 0x1653EB30 `；selector ` 3 `；EOL ` RVA 0x35FA03F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0d5511568893b821](../../evidence/conditions-sets-005.md#c-0d5511568893b821)

### path-005984

```text
(exec)# test mock overlayfs system-call <cr>
```

Handler ` RVA 0x1653EB30 `；selector ` 20 `；EOL ` RVA 0x35FA1EC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9b1b87d9958d4697](../../evidence/conditions-sets-060.md#c-9b1b87d9958d4697) · [状态效果 S-42997407570928c2](../../evidence/state_effects-sets-015.md#s-42997407570928c2)

### path-002081

```text
(exec)# test mock real <cr>
```

Handler ` RVA 0x1653EB30 `；selector ` 9 `；EOL ` RVA 0x35FA1688 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-160059a6fea2740e](../../evidence/conditions-sets-009.md#c-160059a6fea2740e)

### path-001914

```text
(exec)# test mock system <cr>
```

Handler ` RVA 0x1653EB30 `；selector ` 17 `；EOL ` RVA 0x35F9FBF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cc8e32e775a81c75](../../evidence/conditions-sets-079.md#c-cc8e32e775a81c75)

### path-002069

```text
(exec)# test mock tdl <cr>
```

Handler ` RVA 0x1653EB30 `；selector ` 10 `；EOL ` RVA 0x35FA13E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9d65b17cf8c3b50e](../../evidence/conditions-sets-061.md#c-9d65b17cf8c3b50e)

### path-002119

```text
(exec)# test mock vaarg <cr>
```

Handler ` RVA 0x1653EB30 `；selector ` 19 `；EOL ` RVA 0x35FA1BD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3c0ae84cd8eb1ffa](../../evidence/conditions-sets-023.md#c-3c0ae84cd8eb1ffa)

### path-009276

```text
(exec)# test monitor clear config lock <cr>
```

Handler ` RVA 0xE4CE1F0 `；selector ` 0 `；EOL ` RVA 0x342CFCF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-001614

```text
(exec)# test mrib disable <cr>
```

Handler ` RVA 0x1190F470 `；selector ` 0 `；EOL ` RVA 0x355A7AF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-19d38f0bae87dd65](../../evidence/conditions-sets-010.md#c-19d38f0bae87dd65) · [状态效果 S-9efa990cfb5fdddc](../../evidence/state_effects-sets-034.md#s-9efa990cfb5fdddc)

### path-005473

```text
(exec)# test mrib ip stop <cr>
```

Handler ` RVA 0x1190F470 `；selector ` 0 `；EOL ` RVA 0x35376868 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c509e16008966f7f](../../evidence/conditions-sets-076.md#c-c509e16008966f7f) · [状态效果 S-eaa76b3e5baf3fc5](../../evidence/state_effects-sets-050.md#s-eaa76b3e5baf3fc5)

### path-005467

```text
(exec)# test mrib ipv6 stop <cr>
```

Handler ` RVA 0x1190F470 `；selector ` 0 `；EOL ` RVA 0x35540A50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-745ad1cbbc0fb872](../../evidence/conditions-sets-045.md#c-745ad1cbbc0fb872) · [状态效果 S-7d219cc6ef946ff0](../../evidence/state_effects-sets-027.md#s-7d219cc6ef946ff0)

### path-012021

```text
(exec)# test mvpn ipv4 leaf-ad-recv add <address> <address> <address> <cr>
```

Handler ` RVA 0xF963F30 `；selector ` 0 `；EOL ` RVA 0x34790B08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Leaf A-D Route Key Source address；` address ` Leaf A-D Route Key Group address；` address ` Leaf A-D Originating IP address。

[条件 C-fe97fd1163db9d0a](../../evidence/conditions-sets-098.md#c-fe97fd1163db9d0a) · [参数 P-e7edaa477d6f924d](../../evidence/parameters-sets-017.md#p-e7edaa477d6f924d) · [状态效果 S-e11d91fd064abf71](../../evidence/state_effects-sets-048.md#s-e11d91fd064abf71)

### path-009007

```text
(exec)# test mvpn ipv4 spt-only disable <cr>
```

Handler ` RVA 0xF963F30 `；selector ` 2 `；EOL ` RVA 0x347910B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-be506ef255ae8532](../../evidence/conditions-sets-073.md#c-be506ef255ae8532) · [状态效果 S-3bff1ff7d502af13](../../evidence/state_effects-sets-013.md#s-3bff1ff7d502af13)

### path-008995

```text
(exec)# test mvpn ipv4 spt-only enable <cr>
```

Handler ` RVA 0xF963F30 `；selector ` 1 `；EOL ` RVA 0x34790E10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bb8b7d85c6e5b67a](../../evidence/conditions-sets-072.md#c-bb8b7d85c6e5b67a) · [状态效果 S-3bff1ff7d502af13](../../evidence/state_effects-sets-013.md#s-3bff1ff7d502af13)

### path-012023

```text
(exec)# test mvpn ipv6 leaf-ad-recv add <address> <address> <address> <cr>
```

Handler ` RVA 0xF963F30 `；selector ` 0 `；EOL ` RVA 0x347916C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Leaf A-D Route Key Source address；` address ` Leaf A-D Route Key Group address；` address ` Leaf A-D Originating IP address。

[条件 C-5777c56982c57e1f](../../evidence/conditions-sets-034.md#c-5777c56982c57e1f) · [参数 P-2d64e798f1d53ea9](../../evidence/parameters-sets-004.md#p-2d64e798f1d53ea9) · [状态效果 S-68ac1bd187cc43fd](../../evidence/state_effects-sets-022.md#s-68ac1bd187cc43fd)

### path-009013

```text
(exec)# test mvpn ipv6 spt-only disable <cr>
```

Handler ` RVA 0xF963F30 `；selector ` 2 `；EOL ` RVA 0x34791C70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8785db4633997928](../../evidence/conditions-sets-052.md#c-8785db4633997928) · [状态效果 S-f6364f3549e3c3bc](../../evidence/state_effects-sets-052.md#s-f6364f3549e3c3bc)

### path-009003

```text
(exec)# test mvpn ipv6 spt-only enable <cr>
```

Handler ` RVA 0xF963F30 `；selector ` 1 `；EOL ` RVA 0x347919C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-687f5824f1d67310](../../evidence/conditions-sets-040.md#c-687f5824f1d67310) · [状态效果 S-f6364f3549e3c3bc](../../evidence/state_effects-sets-052.md#s-f6364f3549e3c3bc)

### path-004655

```text
(exec)# test mvrp enable <number:0..1> <cr>
```

Handler ` RVA 0xC96A0D0 `；selector ` 2 `；EOL ` RVA 0x33B3ACD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Enable - 1, Disable - 0。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-2b2af8342a3221a3](../../evidence/parameters-sets-004.md#p-2b2af8342a3221a3)

### path-008369

```text
(exec)# test mvrp joinin <number:1..4094> <number:1..4094> <cr>
```

Handler ` RVA 0xC96A0D0 `；selector ` 1 `；EOL ` RVA 0x33B3AA08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Starting VLAN；` unsigned_number ` VLAN count。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-347f484921822044](../../evidence/parameters-sets-004.md#p-347f484921822044)

### path-008358

```text
(exec)# test mvrp new <number:1..4094> <number:1..4094> <cr>
```

Handler ` RVA 0xC96A0D0 `；selector ` 0 `；EOL ` RVA 0x33B3A6D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Starting VLAN；` unsigned_number ` VLAN count。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-47e3eaebeb4262d6](../../evidence/parameters-sets-006.md#p-47e3eaebeb4262d6)

### path-001014

```text
(exec)# test natmode suppress <cr>
```

Handler ` RVA 0xCF73670 `；selector ` 0 `；EOL ` RVA 0x33D44630 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [状态效果 S-6d7fa3ba101abd8a](../../evidence/state_effects-sets-023.md#s-6d7fa3ba101abd8a)

### path-002254

```text
(exec)# test netconf-agent history <cr>
```

Handler ` RVA 0xF3BDEF0 `；selector ` 1 `；EOL ` RVA 0x3462AA78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-002278

```text
(exec)# test netconf-agent summary <cr>
```

Handler ` RVA 0xF3BDEF0 `；selector ` 3 `；EOL ` RVA 0x3462AD20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-001496

```text
(exec)# test ngdns config <cr>
```

Handler ` RVA 0xD177360 `；selector ` 0 `；EOL ` RVA 0x33DA53C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-dbd01ecd58231423](../../evidence/conditions-sets-085.md#c-dbd01ecd58231423)

### path-005246

```text
(exec)# test ngdns lookup <string> <cr>
```

Handler ` RVA 0xD177DF0 `；selector ` 0 `；EOL ` RVA 0x33DA5878 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` lookup name。

[条件 C-dbd01ecd58231423](../../evidence/conditions-sets-085.md#c-dbd01ecd58231423) · [参数 P-decc2673888888d4](../../evidence/parameters-sets-017.md#p-decc2673888888d4)

### path-005195

```text
(exec)# test ngdns periodic dump <cr>
```

Handler ` RVA 0xD177180 `；selector ` 0 `；EOL ` RVA 0x33DA4720 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-dbd01ecd58231423](../../evidence/conditions-sets-085.md#c-dbd01ecd58231423)

### path-012168

```text
(exec)# test ngdns periodic register fqdn-name <string> type both module-id <number:1..3> <cr>
```

Handler ` RVA 0xD176ED0 `；selector ` 0 `；EOL ` RVA 0x33DA4368 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Specify FQDN；` unsigned_number ` module-id。

[条件 C-dbd01ecd58231423](../../evidence/conditions-sets-085.md#c-dbd01ecd58231423) · [参数 P-ed5b72c7cd03d32e](../../evidence/parameters-sets-018.md#p-ed5b72c7cd03d32e) · [状态效果 S-038de886717d0e7b](../../evidence/state_effects-sets-001.md#s-038de886717d0e7b)

### path-006363

```text
(exec)# test ngiosd process-isolation start <cr>
```

Handler ` RVA 0x1653B780 `；selector ` 0 `；EOL ` RVA 0x35F9EE48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [状态效果 S-ed4ae2b89047ddfe](../../evidence/state_effects-sets-050.md#s-ed4ae2b89047ddfe)

### path-009480

```text
(exec)# test ngiosd simulation prepare-failure enable <cr>
```

Handler ` RVA 0x1653B5E0 `；selector ` 0 `；EOL ` RVA 0x35F9E6E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [状态效果 S-21622715cbda5d3a](../../evidence/state_effects-sets-008.md#s-21622715cbda5d3a)

### path-009500

```text
(exec)# test ngiosd simulation prepare-pass enable <cr>
```

Handler ` RVA 0x1653B520 `；selector ` 0 `；EOL ` RVA 0x35F9EA80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [状态效果 S-65dd83c4bf16676a](../../evidence/state_effects-sets-022.md#s-65dd83c4bf16676a)

### path-006329

```text
(exec)# test ngiosd simulation start <cr>
```

Handler ` RVA 0x1653B6A0 `；selector ` 0 `；EOL ` RVA 0x35F9E378 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [状态效果 S-4dbd6c5886f19a65](../../evidence/state_effects-sets-017.md#s-4dbd6c5886f19a65)

### path-000243

```text
(exec)# test nhrp event <number:0..1500> <cr>
```

Handler ` RVA 0x108D66C0 `；selector ` 8 `；EOL ` RVA 0x34BEAEE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` event code。

[条件 C-5c19a6d365776e81](../../evidence/conditions-sets-036.md#c-5c19a6d365776e81) · [参数 P-6c57de9d403a368b](../../evidence/parameters-sets-009.md#p-6c57de9d403a368b)

### path-025410

```text
(exec)# test nhrp redirect interface <interface> <?ipv4orv6_addr_action@55558a13efe0> <prefix:dynamic> <cr>
```

Handler ` RVA 0x108D66C0 `；selector ` 7 `；EOL ` RVA 0x34BEB060 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` IP address/&lt;length&gt; of destination, eg:192.168.0.0/16。

[条件 C-26cd19cbbd244aa9](../../evidence/conditions-sets-015.md#c-26cd19cbbd244aa9) · [缺口 G-f34972516f0c31ac](../../evidence/gaps-sets-008.md#g-f34972516f0c31ac) · [参数 P-4d6fd10b9bc76322](../../evidence/parameters-sets-006.md#p-4d6fd10b9bc76322)

### path-002480

```text
(exec)# test notify <string> <cr>
```

Handler ` RVA 0x15A6CE70 `；selector ` 0 `；EOL ` RVA 0x35DE3AB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Virtual-service name。

[条件 C-e2bc1f5c8b2db1af](../../evidence/conditions-sets-087.md#c-e2bc1f5c8b2db1af) · [参数 P-bb63f77282b0e6a2](../../evidence/parameters-sets-014.md#p-bb63f77282b0e6a2)

### path-009207

```text
(exec)# test nvram <string> clear remote-lock <cr>
```

Handler ` RVA 0xD620830 `；selector ` 1 `；EOL ` RVA 0x33EB0A58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` URL for Nvram filesystem。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-465a9fec902c71c5](../../evidence/parameters-sets-006.md#p-465a9fec902c71c5)

### path-005882

```text
(exec)# test nvram <string> explicit-lock <cr>
```

Handler ` RVA 0xD620830 `；selector ` 0 `；EOL ` RVA 0x33EB0CE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` URL for Nvram filesystem。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-465a9fec902c71c5](../../evidence/parameters-sets-006.md#p-465a9fec902c71c5)

### path-005908

```text
(exec)# test nvram <string> initialize <cr>
```

Handler ` RVA 0xD620830 `；selector ` 2 `；EOL ` RVA 0x33EB0F90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` URL for Nvram filesystem。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-465a9fec902c71c5](../../evidence/parameters-sets-006.md#p-465a9fec902c71c5)

### path-011805

```text
(exec)# test odb client <number:1..256> add-static-tlv type <number:0..65535> <cr>
```

Handler ` RVA 0x12414A30 `；selector ` 2 `；EOL ` RVA 0x35856F38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Client handle；` unsigned_number ` TLV type。

[条件 C-80216fb1f9949281](../../evidence/conditions-sets-050.md#c-80216fb1f9949281) · [参数 P-4937c32f8d4b15b3](../../evidence/parameters-sets-006.md#p-4937c32f8d4b15b3)

### path-009127

```text
(exec)# test odb client <number:1..256> deregister <cr>
```

Handler ` RVA 0x12414A30 `；selector ` 1 `；EOL ` RVA 0x35856BE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Client handle。

[条件 C-d53d47f92e3d412c](../../evidence/conditions-sets-082.md#c-d53d47f92e3d412c) · [参数 P-9dd44be07c481a6e](../../evidence/parameters-sets-012.md#p-9dd44be07c481a6e)

### path-012193

```text
(exec)# test odb client <number:1..256> row <number:0..4294967295> <number:0..4294967295> add-tlv type <number:0..65535> value <string> <cr>
```

Handler ` RVA 0x12414A30 `；selector ` 8 `；EOL ` RVA 0x358585E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Client handle；` unsigned_number ` Higher 32 bits of record handle；` unsigned_number ` Lower 32 bits of record handle；` unsigned_number ` TLV type；` string ` TLV value。

[条件 C-603c5f71a51d9aa5](../../evidence/conditions-sets-037.md#c-603c5f71a51d9aa5) · [参数 P-3761b49542bab2b5](../../evidence/parameters-sets-005.md#p-3761b49542bab2b5)

### path-012029

```text
(exec)# test odb client <number:1..256> row <number:0..4294967295> <number:0..4294967295> delete <cr>
```

Handler ` RVA 0x12414A30 `；selector ` 7 `；EOL ` RVA 0x35858208 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Client handle；` unsigned_number ` Higher 32 bits of record handle；` unsigned_number ` Lower 32 bits of record handle。

[条件 C-41ec9c5c88dd2ce6](../../evidence/conditions-sets-026.md#c-41ec9c5c88dd2ce6) · [参数 P-cbbc12b169c74bfe](../../evidence/parameters-sets-015.md#p-cbbc12b169c74bfe)

### path-012172

```text
(exec)# test odb client <number:1..256> row <number:0..4294967295> <number:0..4294967295> notify subscribe change <cr>
```

Handler ` RVA 0x12414A30 `；selector ` 9 `；EOL ` RVA 0x35858930 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Client handle；` unsigned_number ` Higher 32 bits of record handle；` unsigned_number ` Lower 32 bits of record handle。

[条件 C-c1893af9033fb1f9](../../evidence/conditions-sets-075.md#c-c1893af9033fb1f9) · [参数 P-cbbc12b169c74bfe](../../evidence/parameters-sets-015.md#p-cbbc12b169c74bfe) · [状态效果 S-a8992292d120e0a2](../../evidence/state_effects-sets-036.md#s-a8992292d120e0a2)

### path-012187

```text
(exec)# test odb client <number:1..256> table <number:1..65534> add-row type <number:0..65535> value <string> <cr>
```

Handler ` RVA 0x12414A30 `；selector ` 6 `；EOL ` RVA 0x35857A20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Client handle；` unsigned_number ` Table id；` unsigned_number ` TLV type；` string ` TLV value。

[条件 C-3c5d3f8e4539e524](../../evidence/conditions-sets-023.md#c-3c5d3f8e4539e524) · [参数 P-339759b930726c8c](../../evidence/parameters-sets-004.md#p-339759b930726c8c)

### path-011806

```text
(exec)# test odb client <number:1..256> table <number:1..65534> delete <cr>
```

Handler ` RVA 0x12414A30 `；selector ` 4 `；EOL ` RVA 0x35857648 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Client handle；` unsigned_number ` Table id。

[条件 C-7c978f9c07c92832](../../evidence/conditions-sets-048.md#c-7c978f9c07c92832) · [参数 P-f95d9efa001e6a73](../../evidence/parameters-sets-019.md#p-f95d9efa001e6a73)

### path-012123

```text
(exec)# test odb client <number:1..256> table <number:1..65534> notify subscribe add <cr>
```

Handler ` RVA 0x12414A30 `；selector ` 5 `；EOL ` RVA 0x35857D70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Client handle；` unsigned_number ` Table id。

[条件 C-02058b781e1101b0](../../evidence/conditions-sets-001.md#c-02058b781e1101b0) · [参数 P-f95d9efa001e6a73](../../evidence/parameters-sets-019.md#p-f95d9efa001e6a73) · [状态效果 S-406db991125f61c8](../../evidence/state_effects-sets-014.md#s-406db991125f61c8)

### path-011095

```text
(exec)# test odb client <number:1..256> table create <cr>
```

Handler ` RVA 0x12414A30 `；selector ` 3 `；EOL ` RVA 0x358572C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Client handle。

[条件 C-b430db76483bbdf3](../../evidence/conditions-sets-070.md#c-b430db76483bbdf3) · [参数 P-9dd44be07c481a6e](../../evidence/parameters-sets-012.md#p-9dd44be07c481a6e)

### path-009122

```text
(exec)# test odb client register <string> <cr>
```

Handler ` RVA 0x12414A30 `；selector ` 0 `；EOL ` RVA 0x35856920 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Client name。

[条件 C-9d4808203c71352b](../../evidence/conditions-sets-061.md#c-9d4808203c71352b) · [参数 P-13828cb53228f29f](../../evidence/parameters-sets-002.md#p-13828cb53228f29f)

### path-009133

```text
(exec)# test onep cli uninstall <string> <cr>
```

Handler ` RVA 0x13A82E40 `；selector ` 0 `；EOL ` RVA 0x35CAA6E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Configuration Domain。

[条件 C-30650f11735b2424](../../evidence/conditions-sets-019.md#c-30650f11735b2424) · [参数 P-6b00482f66f10d6d](../../evidence/parameters-sets-008.md#p-6b00482f66f10d6d) · [状态效果 S-c89564dd73f529e1](../../evidence/state_effects-sets-042.md#s-c89564dd73f529e1)

### path-002021

```text
(exec)# test onep ctx_reg <cr>
```

Handler ` RVA 0x13A858B0 `；selector ` 0 `；EOL ` RVA 0x35CABFC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2e013613ed02bb0c](../../evidence/conditions-sets-018.md#c-2e013613ed02bb0c) · [状态效果 S-9e0a703b5be47198](../../evidence/state_effects-sets-034.md#s-9e0a703b5be47198)

### path-005859

```text
(exec)# test onep if_ctx_event enable <cr>
```

Handler ` RVA 0x13A85820 `；selector ` 0 `；EOL ` RVA 0x35CAC308 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6d26840ca034f356](../../evidence/conditions-sets-042.md#c-6d26840ca034f356) · [状态效果 S-55a6c57aa7bb2933](../../evidence/state_effects-sets-019.md#s-55a6c57aa7bb2933)

### path-005706

```text
(exec)# test onep internal enable <cr>
```

Handler ` RVA 0x13A82DA0 `；selector ` 0 `；EOL ` RVA 0x35CAA9D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [状态效果 S-83bd66a5db107e7b](../../evidence/state_effects-sets-028.md#s-83bd66a5db107e7b)

### path-005759

```text
(exec)# test onep thrift list <cr>
```

Handler ` RVA 0x13A863B0 `；selector ` 0 `；EOL ` RVA 0x35CAADE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fbe63d357ef87e68](../../evidence/conditions-sets-097.md#c-fbe63d357ef87e68) · [状态效果 S-edca8d89e1a5f6ab](../../evidence/state_effects-sets-050.md#s-edca8d89e1a5f6ab)

### path-018253

```text
(exec)# test onep timing api <?option@55558b1ff1d0> <cr>
```

Handler ` RVA 0x13A86300 `；selector ` 0 `；EOL ` RVA 0x35CAB210 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e7204f69b0cdfa13](../../evidence/conditions-sets-089.md#c-e7204f69b0cdfa13) · [缺口 G-e77c4547d82b75c0](../../evidence/gaps-sets-008.md#g-e77c4547d82b75c0) · [状态效果 S-c89564dd73f529e1](../../evidence/state_effects-sets-042.md#s-c89564dd73f529e1)

### path-005793

```text
(exec)# test onep version disable <cr>
```

Handler ` RVA 0x13A86260 `；selector ` 0 `；EOL ` RVA 0x35CAB5B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7459f6318f62df31](../../evidence/conditions-sets-045.md#c-7459f6318f62df31) · [状态效果 S-c89564dd73f529e1](../../evidence/state_effects-sets-042.md#s-c89564dd73f529e1)

### path-009162

```text
(exec)# test onep version disable exact <cr>
```

Handler ` RVA 0x13A86210 `；selector ` 0 `；EOL ` RVA 0x35CAB588 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7459f6318f62df31](../../evidence/conditions-sets-045.md#c-7459f6318f62df31) · [状态效果 S-c89564dd73f529e1](../../evidence/state_effects-sets-042.md#s-c89564dd73f529e1)

### path-005783

```text
(exec)# test onep version enable <cr>
```

Handler ` RVA 0x13A862B0 `；selector ` 0 `；EOL ` RVA 0x35CABA80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7459f6318f62df31](../../evidence/conditions-sets-045.md#c-7459f6318f62df31) · [状态效果 S-c89564dd73f529e1](../../evidence/state_effects-sets-042.md#s-c89564dd73f529e1)

### path-002004

```text
(exec)# test onep xdt_buginf <cr>
```

Handler ` RVA 0x13A84B00 `；selector ` 0 `；EOL ` RVA 0x35CABD18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f740640b0f81d7ab](../../evidence/conditions-sets-095.md#c-f740640b0f81d7ab) · [状态效果 S-c89564dd73f529e1](../../evidence/state_effects-sets-042.md#s-c89564dd73f529e1)

### path-005514

```text
(exec)# test opflex agent ha <cr>
```

Handler ` RVA 0xC482E30 `；selector ` 1 `；EOL ` RVA 0x33A939F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-011803

```text
(exec)# test opflex agent service vxlan-evpn create <string> <cr>
```

Handler ` RVA 0xC494C00 `；selector ` 0 `；EOL ` RVA 0x33A97360 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Tenant name。

[条件 C-9725188d4df45d9f](../../evidence/conditions-sets-058.md#c-9725188d4df45d9f) · [参数 P-b42fb32a7d39d38b](../../evidence/parameters-sets-014.md#p-b42fb32a7d39d38b) · [状态效果 S-f28e6bface61a5ee](../../evidence/state_effects-sets-051.md#s-f28e6bface61a5ee)

### path-011080

```text
(exec)# test opflex agent service vxlan-evpn state <cr>
```

Handler ` RVA 0xC494F30 `；selector ` 0 `；EOL ` RVA 0x33A96FC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-011113

```text
(exec)# test opssl nonblockingsession server dtls stop <cr>
```

Handler ` RVA 0x12A14A30 `；selector ` 0 `；EOL ` RVA 0x35936140 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-222758c3ad39c65b](../../evidence/conditions-sets-013.md#c-222758c3ad39c65b) · [状态效果 S-e4666ba52d6ddd4e](../../evidence/state_effects-sets-048.md#s-e4666ba52d6ddd4e)

### path-001418

```text
(exec)# test ospf debug <cr>
```

Handler ` RVA 0xFCD52B0 `；selector ` 0 `；EOL ` RVA 0x34894F28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-010982

```text
(exec)# test ospf nsr cf error <number:0..65535> <cr>
```

Handler ` RVA 0xDACCD90 `；selector ` 10 `；EOL ` RVA 0x33FC6990 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Repeat count。

[条件 C-7f29f1fc84862c68](../../evidence/conditions-sets-049.md#c-7f29f1fc84862c68) · [参数 P-1e19628e5a2b3740](../../evidence/parameters-sets-003.md#p-1e19628e5a2b3740)

### path-008907

```text
(exec)# test ospf nsr cf flow-off <cr>
```

Handler ` RVA 0xDACCD90 `；selector ` 9 `；EOL ` RVA 0x33FC66A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7f29f1fc84862c68](../../evidence/conditions-sets-049.md#c-7f29f1fc84862c68)

### path-008881

```text
(exec)# test ospf nsr cf flow-on <cr>
```

Handler ` RVA 0xDACCD90 `；selector ` 8 `；EOL ` RVA 0x33FC6400 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7f29f1fc84862c68](../../evidence/conditions-sets-049.md#c-7f29f1fc84862c68)

### path-010981

```text
(exec)# test ospf nsr cp clear <number:0..65535> <cr>
```

Handler ` RVA 0xDACCD90 `；selector ` 2 `；EOL ` RVA 0x33FC6FB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Opcode。

[条件 C-7f29f1fc84862c68](../../evidence/conditions-sets-049.md#c-7f29f1fc84862c68) · [参数 P-588a2cc36056eed0](../../evidence/parameters-sets-007.md#p-588a2cc36056eed0)

### path-008982

```text
(exec)# test ospf nsr cp interface <cr>
```

Handler ` RVA 0xDACCD90 `；selector ` 5 `；EOL ` RVA 0x33FC78C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-26928c89a7ffa274](../../evidence/conditions-sets-015.md#c-26928c89a7ffa274)

### path-021720

```text
(exec)# test ospf nsr cp interface <interface> <cr>
```

Handler ` RVA 0xDACCD90 `；selector ` 5 `；EOL ` RVA 0x33FC78C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0c7ea05a1c9bfd4f](../../evidence/conditions-sets-005.md#c-0c7ea05a1c9bfd4f) · [缺口 G-9521a88e41a22004](../../evidence/gaps-sets-005.md#g-9521a88e41a22004) · [参数 P-78822c7581dad0fd](../../evidence/parameters-sets-009.md#p-78822c7581dad0fd)

### path-008979

```text
(exec)# test ospf nsr cp lsa <cr>
```

Handler ` RVA 0xDACCD90 `；selector ` 7 `；EOL ` RVA 0x33FC7F68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7f29f1fc84862c68](../../evidence/conditions-sets-049.md#c-7f29f1fc84862c68)

### path-008993

```text
(exec)# test ospf nsr cp neighbor <cr>
```

Handler ` RVA 0xDACCD90 `；selector ` 6 `；EOL ` RVA 0x33FC7C90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-89a84a7895e761cc](../../evidence/conditions-sets-053.md#c-89a84a7895e761cc)

### path-021750

```text
(exec)# test ospf nsr cp neighbor <interface> <cr>
```

Handler ` RVA 0xDACCD90 `；selector ` 6 `；EOL ` RVA 0x33FC7C90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-609a70414cee4b31](../../evidence/conditions-sets-038.md#c-609a70414cee4b31) · [缺口 G-c92728bf805e6458](../../evidence/gaps-sets-007.md#g-c92728bf805e6458) · [参数 P-5c29a76996e4e816](../../evidence/parameters-sets-007.md#p-5c29a76996e4e816)

### path-008903

```text
(exec)# test ospf nsr cp nop <cr>
```

Handler ` RVA 0xDACCD90 `；selector ` 1 `；EOL ` RVA 0x33FC6CA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7f29f1fc84862c68](../../evidence/conditions-sets-049.md#c-7f29f1fc84862c68)

### path-008947

```text
(exec)# test ospf nsr cp router-id <cr>
```

Handler ` RVA 0xDACCD90 `；selector ` 4 `；EOL ` RVA 0x33FC7530 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7f29f1fc84862c68](../../evidence/conditions-sets-049.md#c-7f29f1fc84862c68)

### path-010996

```text
(exec)# test ospf nsr cp sync <number:0..65535> <cr>
```

Handler ` RVA 0xDACCD90 `；selector ` 3 `；EOL ` RVA 0x33FC72A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Event。

[条件 C-7f29f1fc84862c68](../../evidence/conditions-sets-049.md#c-7f29f1fc84862c68) · [参数 P-1dd2c57cd27b0f0d](../../evidence/parameters-sets-003.md#p-1dd2c57cd27b0f0d)

### path-010980

```text
(exec)# test ospf nsr recovery delay <number:0..255> <cr>
```

Handler ` RVA 0xDACCD90 `；selector ` 11 `；EOL ` RVA 0x33FC82E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Seconds to delay recovery。

[条件 C-7f29f1fc84862c68](../../evidence/conditions-sets-049.md#c-7f29f1fc84862c68) · [参数 P-56211fbc98f531aa](../../evidence/parameters-sets-007.md#p-56211fbc98f531aa)

### path-005282

```text
(exec)# test ospf nsr unsynchronize <cr>
```

Handler ` RVA 0xDACCD90 `；selector ` 12 `；EOL ` RVA 0x33FC8580 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7f29f1fc84862c68](../../evidence/conditions-sets-049.md#c-7f29f1fc84862c68)

### path-001744

```text
(exec)# test ospfv3 crimson <cr>
```

Handler ` RVA 0x11C027D0 `；selector ` 17 `；EOL ` RVA 0x35691980 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [状态效果 S-5e2e802ef4640187](../../evidence/state_effects-sets-020.md#s-5e2e802ef4640187)

### path-021859

```text
(exec)# test ospfv3 interface <interface> filter hello <cr>
```

Handler ` RVA 0x11C027D0 `；selector ` 3 `；EOL ` RVA 0x35691D90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2163470b417fb4fd](../../evidence/conditions-sets-013.md#c-2163470b417fb4fd) · [缺口 G-895fc534bcc28abc](../../evidence/gaps-sets-005.md#g-895fc534bcc28abc) · [参数 P-bca83470b4d22658](../../evidence/parameters-sets-014.md#p-bca83470b4d22658) · [状态效果 S-5e2e802ef4640187](../../evidence/state_effects-sets-020.md#s-5e2e802ef4640187)

### path-021869

```text
(exec)# test ospfv3 interface <interface> filter none <cr>
```

Handler ` RVA 0x11C027D0 `；selector ` 4 `；EOL ` RVA 0x35692038 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2163470b417fb4fd](../../evidence/conditions-sets-013.md#c-2163470b417fb4fd) · [缺口 G-895fc534bcc28abc](../../evidence/gaps-sets-005.md#g-895fc534bcc28abc) · [参数 P-bca83470b4d22658](../../evidence/parameters-sets-014.md#p-bca83470b4d22658) · [状态效果 S-5e2e802ef4640187](../../evidence/state_effects-sets-020.md#s-5e2e802ef4640187)

### path-024003

```text
(exec)# test ospfv3 interface <interface> neighbor <address> down <cr>
```

Handler ` RVA 0x11C027D0 `；selector ` 1 `；EOL ` RVA 0x35692608 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Router ID。

[条件 C-2163470b417fb4fd](../../evidence/conditions-sets-013.md#c-2163470b417fb4fd) · [缺口 G-895fc534bcc28abc](../../evidence/gaps-sets-005.md#g-895fc534bcc28abc) · [参数 P-7fdffd224e813f9b](../../evidence/parameters-sets-010.md#p-7fdffd224e813f9b) · [状态效果 S-c3dbbb85290484d4](../../evidence/state_effects-sets-041.md#s-c3dbbb85290484d4)

### path-023995

```text
(exec)# test ospfv3 interface <interface> neighbor <address> up <cr>
```

Handler ` RVA 0x11C027D0 `；selector ` 0 `；EOL ` RVA 0x35692360 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Router ID。

[条件 C-2163470b417fb4fd](../../evidence/conditions-sets-013.md#c-2163470b417fb4fd) · [缺口 G-895fc534bcc28abc](../../evidence/gaps-sets-005.md#g-895fc534bcc28abc) · [参数 P-7fdffd224e813f9b](../../evidence/parameters-sets-010.md#p-7fdffd224e813f9b) · [状态效果 S-c3dbbb85290484d4](../../evidence/state_effects-sets-041.md#s-c3dbbb85290484d4)

### path-000594

```text
(exec)# test parser afs <cr>
```

Handler ` RVA 0xDF6BFD0 `；selector ` 0 `；EOL ` RVA 0x340E0AD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3fb93dcbb5609e4e](../../evidence/conditions-sets-025.md#c-3fb93dcbb5609e4e)

### path-016793

```text
(exec)# test parser chainfunc recursion <?call_action@555589600a20> <cr>
```

Handler ` RVA 0xDF33300 `；selector ` 0 `；EOL ` RVA 0x340A91E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-916a320481e96250](../../evidence/conditions-sets-056.md#c-916a320481e96250) · [缺口 G-d8f093436b8ebb53](../../evidence/gaps-sets-008.md#g-d8f093436b8ebb53) · [状态效果 S-8d8ccce20eb8b69c](../../evidence/state_effects-sets-030.md#s-8d8ccce20eb8b69c)

### path-004408

```text
(exec)# test parser configure buffer <cr>
```

Handler ` RVA 0xDEF9430 `；selector ` 0 `；EOL ` RVA 0x340B00E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e1fb39995fb37c72](../../evidence/conditions-sets-087.md#c-e1fb39995fb37c72) · [状态效果 S-d67da89d1619b695](../../evidence/state_effects-sets-045.md#s-d67da89d1619b695)

### path-004342

```text
(exec)# test parser consume-memory <number:0..2147483647> <cr>
```

Handler ` RVA 0xDEF9560 `；selector ` 0 `；EOL ` RVA 0x340ACF20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Memory size。

[条件 C-916a320481e96250](../../evidence/conditions-sets-056.md#c-916a320481e96250) · [参数 P-9fc98b3d0183c115](../../evidence/parameters-sets-012.md#p-9fc98b3d0183c115)

### path-000567

```text
(exec)# test parser gmd <cr>
```

Handler ` RVA 0xDF333D0 `；selector ` 0 `；EOL ` RVA 0x340AC020 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-916a320481e96250](../../evidence/conditions-sets-056.md#c-916a320481e96250)

### path-000803

```text
(exec)# test parser green-fe <cr>
```

Handler ` RVA 0xDF8E5F0 `；selector ` 0 `；EOL ` RVA 0x340AEDA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e2e5c58d10549f98](../../evidence/conditions-sets-087.md#c-e2e5c58d10549f98)

### path-008146

```text
(exec)# test parser ngios native-green enable <cr>
```

Handler ` RVA 0xDF8EDC0 `；selector ` 0 `；EOL ` RVA 0x340AE210 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e2e5c58d10549f98](../../evidence/conditions-sets-087.md#c-e2e5c58d10549f98) · [状态效果 S-549d6ca6173f03dc](../../evidence/state_effects-sets-018.md#s-549d6ca6173f03dc)

### path-008156

```text
(exec)# test parser ngios side-effect per-batch <cr>
```

Handler ` RVA 0xDF8ED00 `；selector ` 0 `；EOL ` RVA 0x340AE5D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e2e5c58d10549f98](../../evidence/conditions-sets-087.md#c-e2e5c58d10549f98) · [状态效果 S-8bc16d2fae219c01](../../evidence/state_effects-sets-030.md#s-8bc16d2fae219c01)

### path-008163

```text
(exec)# test parser ngios validation enable <cr>
```

Handler ` RVA 0xDF8EC40 `；selector ` 0 `；EOL ` RVA 0x340AE9C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e2e5c58d10549f98](../../evidence/conditions-sets-087.md#c-e2e5c58d10549f98) · [状态效果 S-edb754ef0c4492a6](../../evidence/state_effects-sets-050.md#s-edb754ef0c4492a6)

### path-008177

```text
(exec)# test parser ngios-meta path disable <cr>
```

Handler ` RVA 0xDF8EA80 `；selector ` 0 `；EOL ` RVA 0x340AF4E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e2e5c58d10549f98](../../evidence/conditions-sets-087.md#c-e2e5c58d10549f98) · [状态效果 S-f629356353551956](../../evidence/state_effects-sets-052.md#s-f629356353551956)

### path-020852

```text
(exec)# test parser ngios-meta path enable <url:dynamic> <cr>
```

Handler ` RVA 0xDF8EA80 `；selector ` 0 `；EOL ` RVA 0x340AF4E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8453ff22d2204123](../../evidence/conditions-sets-051.md#c-8453ff22d2204123) · [缺口 G-eb8224ee74a37d70](../../evidence/gaps-sets-008.md#g-eb8224ee74a37d70) · [参数 P-7f98c5c283d1631c](../../evidence/parameters-sets-010.md#p-7f98c5c283d1631c) · [状态效果 S-c06523ddf703bf2c](../../evidence/state_effects-sets-041.md#s-c06523ddf703bf2c)

### path-020758

```text
(exec)# test parser opt list dyn <?option@555589609530> <cr>
```

Handler ` RVA 0xDF341F0 `；selector ` 0 `；EOL ` RVA 0x340B5598 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8a28630e5de5794f](../../evidence/conditions-sets-053.md#c-8a28630e5de5794f) · [缺口 G-7b0ca2d6822ed961](../../evidence/gaps-sets-005.md#g-7b0ca2d6822ed961)

### path-020762

```text
(exec)# test parser opt list norm <?keyword_option_list_mm_action@555589609880> <cr>
```

Handler ` RVA 0xDF34180 `；selector ` 0 `；EOL ` RVA 0x340B58C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-916a320481e96250](../../evidence/conditions-sets-056.md#c-916a320481e96250) · [缺口 G-c759fbaa946d2d2a](../../evidence/gaps-sets-007.md#g-c759fbaa946d2d2a)

### path-012901

```text
(exec)# test parser pipeline <string> <cr>
```

Handler ` RVA 0xDF64E90 `；selector ` 0 `；EOL ` RVA 0x340AC498 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Enter the pipeline to run。

[条件 C-6c782651ed8d232d](../../evidence/conditions-sets-042.md#c-6c782651ed8d232d) · [缺口 G-df61d2e85006d5a8](../../evidence/gaps-sets-008.md#g-df61d2e85006d5a8) · [参数 P-4aac0968ffb2d725](../../evidence/parameters-sets-006.md#p-4aac0968ffb2d725) · [状态效果 S-02c5a26de4294a46](../../evidence/state_effects-sets-001.md#s-02c5a26de4294a46)

### path-008158

```text
(exec)# test parser rc errno <number:0..2147483647> <cr>
```

Handler ` RVA 0xDEE2F90 `；selector ` 5 `；EOL ` RVA 0x340ADBA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` errno value to be mapped。

[条件 C-916a320481e96250](../../evidence/conditions-sets-056.md#c-916a320481e96250) · [参数 P-712d36c9f93ef0d8](../../evidence/parameters-sets-009.md#p-712d36c9f93ef0d8)

### path-010467

```text
(exec)# test parser rc failure <number:11..211> <number:1..2> <cr>
```

Handler ` RVA 0xDEE2F90 `；selector ` 4 `；EOL ` RVA 0x340AD2F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` PRC error code；` unsigned_number ` PRC failure type。

[条件 C-916a320481e96250](../../evidence/conditions-sets-056.md#c-916a320481e96250) · [参数 P-0d3868e4e55310a0](../../evidence/parameters-sets-001.md#p-0d3868e4e55310a0)

### path-004385

```text
(exec)# test parser rc invalid <cr>
```

Handler ` RVA 0xDEE2F90 `；selector ` 2 `；EOL ` RVA 0x340AD8B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-916a320481e96250](../../evidence/conditions-sets-056.md#c-916a320481e96250)

### path-010471

```text
(exec)# test parser rc success <number:1..3> <number:1..4> <cr>
```

Handler ` RVA 0xDEE2F90 `；selector ` 3 `；EOL ` RVA 0x340AD630 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` PRC change type；` unsigned_number ` PRC change mode。

[条件 C-916a320481e96250](../../evidence/conditions-sets-056.md#c-916a320481e96250) · [参数 P-961119851006963a](../../evidence/parameters-sets-012.md#p-961119851006963a)

### path-004365

```text
(exec)# test parser redirect small <cr>
```

Handler ` RVA 0xDF6BFD0 `；selector ` 4 `；EOL ` RVA 0x340E0E18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-401bad26f0222cf5](../../evidence/conditions-sets-025.md#c-401bad26f0222cf5) · [状态效果 S-d15c432991d0e046](../../evidence/state_effects-sets-044.md#s-d15c432991d0e046)

### path-004323

```text
(exec)# test parser session-lock <number:0..1200> <cr>
```

Handler ` RVA 0xDF6BE30 `；selector ` 1 `；EOL ` RVA 0x340E0238 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Config session lock holdtime in seconds。

[条件 C-19519dc36d8d974a](../../evidence/conditions-sets-010.md#c-19519dc36d8d974a) · [参数 P-146602e89f177353](../../evidence/parameters-sets-002.md#p-146602e89f177353)

### path-004335

```text
(exec)# test parser session-lock exit <cr>
```

Handler ` RVA 0xDF6BE30 `；selector ` 2 `；EOL ` RVA 0x340E04E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3174b2ac1d6f72c1](../../evidence/conditions-sets-019.md#c-3174b2ac1d6f72c1)

### path-004355

```text
(exec)# test parser session-lock lock-break <cr>
```

Handler ` RVA 0xDF6BE30 `；selector ` 3 `；EOL ` RVA 0x340E07D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9aab55ec3da8252f](../../evidence/conditions-sets-060.md#c-9aab55ec3da8252f)

### path-000612

```text
(exec)# test parser shell <cr>
```

Handler ` RVA 0xDF8E540 `；selector ` 0 `；EOL ` RVA 0x340ADE58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-916a320481e96250](../../evidence/conditions-sets-056.md#c-916a320481e96250)

### path-008167

```text
(exec)# test parser syntax exclude display <cr>
```

Handler ` RVA 0xDF8F080 `；selector ` 0 `；EOL ` RVA 0x340AFC18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e1fb39995fb37c72](../../evidence/conditions-sets-087.md#c-e1fb39995fb37c72)

### path-010476

```text
(exec)# test parser syntax exclude mode <string> <cr>
```

Handler ` RVA 0xDF8EF50 `；selector ` 0 `；EOL ` RVA 0x340AF948 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of mode or eol name。

[条件 C-e1fb39995fb37c72](../../evidence/conditions-sets-087.md#c-e1fb39995fb37c72) · [参数 P-7e1cba4935d8d80b](../../evidence/parameters-sets-010.md#p-7e1cba4935d8d80b) · [状态效果 S-3a493eb69459bd3d](../../evidence/state_effects-sets-013.md#s-3a493eb69459bd3d)

### path-023926

```text
(exec)# test pbr unset <number:1..7> color adjacency <?general_pointer_number_action@555589d59438> <cr>
```

Handler ` RVA 0xFAE08D0 `；selector ` 0 `；EOL ` RVA 0x34805478 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Application: 1 - AAA。

[条件 C-a2e3e721c2400fba](../../evidence/conditions-sets-063.md#c-a2e3e721c2400fba) · [缺口 G-2470e7dc9a20e7a8](../../evidence/gaps-sets-002.md#g-2470e7dc9a20e7a8) · [参数 P-e311ee4f38aa4338](../../evidence/parameters-sets-017.md#p-e311ee4f38aa4338)

### path-011592

```text
(exec)# test persistent variable api delete default <string> <cr>
```

Handler ` RVA 0xD7C8140 `；selector ` 3 `；EOL ` RVA 0x33EF6C10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Variable name string to delete。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-ff0df765d3c8d9be](../../evidence/parameters-sets-019.md#p-ff0df765d3c8d9be) · [状态效果 S-2b9c6d3056136fbd](../../evidence/state_effects-sets-010.md#s-2b9c6d3056136fbd)

### path-010468

```text
(exec)# test persistent variable api flush default <cr>
```

Handler ` RVA 0xD7C8140 `；selector ` 4 `；EOL ` RVA 0x33EF6F58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [状态效果 S-499b279fc826271a](../../evidence/state_effects-sets-016.md#s-499b279fc826271a)

### path-011590

```text
(exec)# test persistent variable api get default <string> <cr>
```

Handler ` RVA 0xD7C8140 `；selector ` 2 `；EOL ` RVA 0x33EF67C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Variable name string to get。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-643ff067af6eb8fe](../../evidence/parameters-sets-008.md#p-643ff067af6eb8fe) · [状态效果 S-06c900effbb14f97](../../evidence/state_effects-sets-002.md#s-06c900effbb14f97)

### path-011588

```text
(exec)# test persistent variable api isset default <string> <cr>
```

Handler ` RVA 0xD7C8140 `；selector ` 1 `；EOL ` RVA 0x33EF63E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Variable name string to determine if set。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-1e43095dccf81b7e](../../evidence/parameters-sets-003.md#p-1e43095dccf81b7e) · [状态效果 S-f54d13647b7e51b5](../../evidence/state_effects-sets-052.md#s-f54d13647b7e51b5)

### path-011587

```text
(exec)# test persistent variable api set default <string> <cr>
```

Handler ` RVA 0xD7C8140 `；selector ` 0 `；EOL ` RVA 0x33EF5FF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Namevar string to set of the form &lt;name&gt;=&lt;value&gt;。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-bfff11a8e69a755d](../../evidence/parameters-sets-015.md#p-bfff11a8e69a755d) · [状态效果 S-beaf2362f5a7b118](../../evidence/state_effects-sets-040.md#s-beaf2362f5a7b118)

### path-008113

```text
(exec)# test persistent variable error <string> <cr>
```

Handler ` RVA 0xD7C8140 `；selector ` 7 `；EOL ` RVA 0x33EF7960 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Error text to display。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-e6db5d0ce3e2c1f1](../../evidence/parameters-sets-017.md#p-e6db5d0ce3e2c1f1)

### path-008104

```text
(exec)# test persistent variable media-delete <string> <cr>
```

Handler ` RVA 0xD7C8140 `；selector ` 6 `；EOL ` RVA 0x33EF76A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Full media entry string (filepath) to delete。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-ab01ede20decf82c](../../evidence/parameters-sets-013.md#p-ab01ede20decf82c)

### path-008093

```text
(exec)# test persistent variable show cache <cr>
```

Handler ` RVA 0xD7C8140 `；selector ` 5 `；EOL ` RVA 0x33EF7340 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [状态效果 S-635497d8b804fe8c](../../evidence/state_effects-sets-021.md#s-635497d8b804fe8c)

### path-021787

```text
(exec)# test pimv6 join group <address> <interface> <cr>
```

Handler ` RVA 0x117AD0E0 `；selector ` 0 `；EOL ` RVA 0x35558540 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d0806fad8d9bdfdd](../../evidence/conditions-sets-080.md#c-d0806fad8d9bdfdd) · [缺口 G-6777e6402e8b1051](../../evidence/gaps-sets-004.md#g-6777e6402e8b1051) · [参数 P-9f9e8846585630cc](../../evidence/parameters-sets-012.md#p-9f9e8846585630cc) · [状态效果 S-274ae8c9bee0161e](../../evidence/state_effects-sets-009.md#s-274ae8c9bee0161e)

### path-025093

```text
(exec)# test platform hardware interface <interface> plim egress max-fill hp <number:0..245760> <cr>
```

Handler ` RVA 0xE93D130 `；selector ` 0 `；EOL ` RVA 0x3434E0D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Bytes。

[条件 C-a0620df076911527](../../evidence/conditions-sets-062.md#c-a0620df076911527) · [缺口 G-234685bca6553a71](../../evidence/gaps-sets-002.md#g-234685bca6553a71) · [参数 P-117b59bc060fcdbd](../../evidence/parameters-sets-002.md#p-117b59bc060fcdbd) · [状态效果 S-fbc4b52529b569cb](../../evidence/state_effects-sets-053.md#s-fbc4b52529b569cb)

### path-011591

```text
(exec)# test platform hardware poe cfg crit-limit <number:5000..15000> <cr>
```

Handler ` RVA 0x15FFE680 `；selector ` 11 `；EOL ` RVA 0x35EDE1D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Load shedding critical limit。

[条件 C-b8332689a5840f5c](../../evidence/conditions-sets-071.md#c-b8332689a5840f5c) · [参数 P-7d7edd3858492b7b](../../evidence/parameters-sets-010.md#p-7d7edd3858492b7b)

### path-011595

```text
(exec)# test platform hardware poe cfg warn-limit <number:3000..8000> <cr>
```

Handler ` RVA 0x15FFE680 `；selector ` 12 `；EOL ` RVA 0x35EDE498 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Load shedding warning limit。

[条件 C-b8332689a5840f5c](../../evidence/conditions-sets-071.md#c-b8332689a5840f5c) · [参数 P-c98be1bcde1a0f08](../../evidence/parameters-sets-015.md#p-c98be1bcde1a0f08)

### path-023318

```text
(exec)# test platform hardware poe get <number:dynamic> global <cr>
```

Handler ` RVA 0x15FFD8E0 `；selector ` 4 `；EOL ` RVA 0x35EDCFB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Slot number。

[条件 C-029d2398aca9033b](../../evidence/conditions-sets-001.md#c-029d2398aca9033b) · [缺口 G-afba395f0659b4cd](../../evidence/gaps-sets-006.md#g-afba395f0659b4cd) · [参数 P-0328915490ed50f1](../../evidence/parameters-sets-001.md#p-0328915490ed50f1)

### path-024922

```text
(exec)# test platform hardware poe get <number:dynamic> global <number:0..255> <number:0..4294967295> <cr>
```

Handler ` RVA 0x15FFD8E0 `；selector ` 5 `；EOL ` RVA 0x35EDCD30 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Slot number；` unsigned_number ` PSE register number；` unsigned_number ` Value to be written。

[条件 C-95def09ce907ebab](../../evidence/conditions-sets-058.md#c-95def09ce907ebab) · [缺口 G-afba395f0659b4cd](../../evidence/gaps-sets-006.md#g-afba395f0659b4cd) · [参数 P-6b75b43eaa2d5f51](../../evidence/parameters-sets-008.md#p-6b75b43eaa2d5f51)

### path-023323

```text
(exec)# test platform hardware poe get <number:dynamic> port <cr>
```

Handler ` RVA 0x15FFD8E0 `；selector ` 3 `；EOL ` RVA 0x35EDD288 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Slot number。

[条件 C-b80f9c4141d69470](../../evidence/conditions-sets-071.md#c-b80f9c4141d69470) · [缺口 G-afba395f0659b4cd](../../evidence/gaps-sets-006.md#g-afba395f0659b4cd) · [参数 P-0328915490ed50f1](../../evidence/parameters-sets-001.md#p-0328915490ed50f1)

### path-024547

```text
(exec)# test platform hardware poe get <number:dynamic> port <number:1..48> <cr>
```

Handler ` RVA 0x15FFD8E0 `；selector ` 1 `；EOL ` RVA 0x35EDD2F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Slot number；` unsigned_number ` Port Number。

[条件 C-b80f9c4141d69470](../../evidence/conditions-sets-071.md#c-b80f9c4141d69470) · [缺口 G-afba395f0659b4cd](../../evidence/gaps-sets-006.md#g-afba395f0659b4cd) · [参数 P-05cd8370c97217c3](../../evidence/parameters-sets-001.md#p-05cd8370c97217c3)

### path-024926

```text
(exec)# test platform hardware poe get <number:dynamic> port <number:1..48> mdi-tlv <cr>
```

Handler ` RVA 0x15FFD8E0 `；selector ` 9 `；EOL ` RVA 0x35EDD9B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Slot number；` unsigned_number ` Port Number。

[条件 C-05a0e27b27221c0f](../../evidence/conditions-sets-003.md#c-05a0e27b27221c0f) · [缺口 G-afba395f0659b4cd](../../evidence/gaps-sets-006.md#g-afba395f0659b4cd) · [参数 P-05cd8370c97217c3](../../evidence/parameters-sets-001.md#p-05cd8370c97217c3)

### path-025095

```text
(exec)# test platform hardware poe get <number:dynamic> port <number:1..48> mdi-tlv invoke <cr>
```

Handler ` RVA 0x15FFD8E0 `；selector ` 8 `；EOL ` RVA 0x35EDD428 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Slot number；` unsigned_number ` Port Number。

[条件 C-bcc717ad7c440f6e](../../evidence/conditions-sets-073.md#c-bcc717ad7c440f6e) · [缺口 G-afba395f0659b4cd](../../evidence/gaps-sets-006.md#g-afba395f0659b4cd) · [参数 P-05cd8370c97217c3](../../evidence/parameters-sets-001.md#p-05cd8370c97217c3) · [状态效果 S-f774f84cb1613ce3](../../evidence/state_effects-sets-052.md#s-f774f84cb1613ce3)

### path-024546

```text
(exec)# test platform hardware pse get <number:dynamic> <number:0..24> <number:1..255> <cr>
```

Handler ` RVA 0x15FFD8E0 `；selector ` 6 `；EOL ` RVA 0x35EDEC70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Slot number；` unsigned_number ` Quad Chip number；` unsigned_number ` PSE register number。

[条件 C-6502322eab6869ab](../../evidence/conditions-sets-039.md#c-6502322eab6869ab) · [缺口 G-1fdcbce9dfb6fc5b](../../evidence/gaps-sets-002.md#g-1fdcbce9dfb6fc5b) · [参数 P-6b29e1d3e80ca9aa](../../evidence/parameters-sets-008.md#p-6b29e1d3e80ca9aa)

### path-024924

```text
(exec)# test platform hardware pse get <number:dynamic> <number:0..24> <number:1..255> <number:0..255> <cr>
```

Handler ` RVA 0x15FFD8E0 `；selector ` 7 `；EOL ` RVA 0x35EDE9E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Slot number；` unsigned_number ` Quad Chip number；` unsigned_number ` PSE register number；` unsigned_number ` Value to be written。

[条件 C-1aa0782a4f6931cd](../../evidence/conditions-sets-010.md#c-1aa0782a4f6931cd) · [缺口 G-1fdcbce9dfb6fc5b](../../evidence/gaps-sets-002.md#g-1fdcbce9dfb6fc5b) · [参数 P-8e2de16e80d65ac3](../../evidence/parameters-sets-011.md#p-8e2de16e80d65ac3)

### path-008232

```text
(exec)# test platform software cef autovpn <cr>
```

Handler ` RVA 0xE5CE300 `；selector ` 5 `；EOL ` RVA 0x342FD060 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980)

### path-008172

```text
(exec)# test platform software cef bgp <cr>
```

Handler ` RVA 0xE5CE300 `；selector ` 2 `；EOL ` RVA 0x342FC2C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980)

### path-008216

```text
(exec)# test platform software cef off <cr>
```

Handler ` RVA 0xE5CE300 `；selector ` 1 `；EOL ` RVA 0x342FCDB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980)

### path-008202

```text
(exec)# test platform software cef on <cr>
```

Handler ` RVA 0xE5CE300 `；selector ` 0 `；EOL ` RVA 0x342FCB10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980)

### path-010509

```text
(exec)# test platform software cef replicate cbl_l2mc <cr>
```

Handler ` RVA 0xE5CE300 `；selector ` 4 `；EOL ` RVA 0x342FC878 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980)

### path-010500

```text
(exec)# test platform software cef replicate mpls <cr>
```

Handler ` RVA 0xE5CE300 `；selector ` 3 `；EOL ` RVA 0x342FC5D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980)

### path-024543

```text
(exec)# test platform software chassis subslot <?slotcard_action@5555898019f0> insert <number:0..4294967295> <cr>
```

Handler ` RVA 0xE389330 `；selector ` 0 `；EOL ` RVA 0x342ADAE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Enter a supported spa type。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-e82f55e189092bfe](../../evidence/gaps-sets-008.md#g-e82f55e189092bfe) · [参数 P-2bb4f74a63fbc399](../../evidence/parameters-sets-004.md#p-2bb4f74a63fbc399)

### path-023327

```text
(exec)# test platform software chassis subslot <?slotcard_action@5555898019f0> remove <cr>
```

Handler ` RVA 0xE389330 `；selector ` 1 `；EOL ` RVA 0x342ADD68 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-e82f55e189092bfe](../../evidence/gaps-sets-008.md#g-e82f55e189092bfe)

### path-008443

```text
(exec)# test platform software crimson db-write-lock <cr>
```

Handler ` RVA 0x1444AAD0 `；selector ` 28 `；EOL ` RVA 0x35D67DC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [状态效果 S-b7b1d095faf1d366](../../evidence/state_effects-sets-039.md#s-b7b1d095faf1d366)

### path-008460

```text
(exec)# test platform software crimson initdb <cr>
```

Handler ` RVA 0x1444AEF0 `；selector ` 17 `；EOL ` RVA 0x35D68110 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980)

### path-010595

```text
(exec)# test platform software crimson notification deregister <cr>
```

Handler ` RVA 0x1444A910 `；selector ` 23 `；EOL ` RVA 0x35D67A70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980)

### path-010591

```text
(exec)# test platform software crimson notification register <cr>
```

Handler ` RVA 0x1444A910 `；selector ` 22 `；EOL ` RVA 0x35D67770 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980)

### path-012088

```text
(exec)# test platform software crimson operational add <number:0..4294967295> idbname <string> <cr>
```

Handler ` RVA 0x1444A610 `；selector ` 3 `；EOL ` RVA 0x35D6CDA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Data to add；` string ` string to add。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [参数 P-82c7b75fd84e942b](../../evidence/parameters-sets-010.md#p-82c7b75fd84e942b)

### path-025117

```text
(exec)# test platform software crimson operational add <number:0..4294967295> subblock <?option@55558b2c1020> <number:0..4294967295> <cr>
```

Handler ` RVA 0x1444A680 `；selector ` 18 `；EOL ` RVA 0x35D6D168 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Data to add；` unsigned_number ` sb-type key to add。

[条件 C-e2e8a4d699d1d971](../../evidence/conditions-sets-087.md#c-e2e8a4d699d1d971) · [缺口 G-102c39908f63af86](../../evidence/gaps-sets-001.md#g-102c39908f63af86) · [参数 P-b5ea519a914743d7](../../evidence/parameters-sets-014.md#p-b5ea519a914743d7)

### path-025194

```text
(exec)# test platform software crimson operational add <number:0..4294967295> subblock <?option@55558b2c1020> <number:0..4294967295> delete <cr>
```

Handler ` RVA 0x1444A680 `；selector ` 20 `；EOL ` RVA 0x35D6D140 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Data to add；` unsigned_number ` sb-type key to add。

[条件 C-e2e8a4d699d1d971](../../evidence/conditions-sets-087.md#c-e2e8a4d699d1d971) · [缺口 G-102c39908f63af86](../../evidence/gaps-sets-001.md#g-102c39908f63af86) · [参数 P-b5ea519a914743d7](../../evidence/parameters-sets-014.md#p-b5ea519a914743d7)

### path-010632

```text
(exec)# test platform software crimson operational disable <cr>
```

Handler ` RVA 0x1444A610 `；selector ` 24 `；EOL ` RVA 0x35D70078 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980)

### path-011666

```text
(exec)# test platform software crimson operational disable idb <cr>
```

Handler ` RVA 0x1444A610 `；selector ` 25 `；EOL ` RVA 0x35D700E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980)

### path-011978

```text
(exec)# test platform software crimson operational disable idb filter <cr>
```

Handler ` RVA 0x1444A610 `；selector ` 26 `；EOL ` RVA 0x35D700B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980)

### path-010598

```text
(exec)# test platform software crimson operational init <cr>
```

Handler ` RVA 0x1444A610 `；selector ` 0 `；EOL ` RVA 0x35D6C4E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980)

### path-011652

```text
(exec)# test platform software crimson operational init app <cr>
```

Handler ` RVA 0x1444A610 `；selector ` 1 `；EOL ` RVA 0x35D6C218 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980)

### path-011651

```text
(exec)# test platform software crimson operational init eventq <cr>
```

Handler ` RVA 0x1444A610 `；selector ` 32 `；EOL ` RVA 0x35D6BF70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980)

### path-011655

```text
(exec)# test platform software crimson operational init idb <cr>
```

Handler ` RVA 0x1444A610 `；selector ` 2 `；EOL ` RVA 0x35D6C550 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980)

### path-011972

```text
(exec)# test platform software crimson operational init idb filter <cr>
```

Handler ` RVA 0x1444A610 `；selector ` 27 `；EOL ` RVA 0x35D6C528 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980)

### path-011663

```text
(exec)# test platform software crimson operational lock acquire <cr>
```

Handler ` RVA 0x1444A610 `；selector ` 12 `；EOL ` RVA 0x35D6F338 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980)

### path-011977

```text
(exec)# test platform software crimson operational lock acquire offload <cr>
```

Handler ` RVA 0x1444A610 `；selector ` 13 `；EOL ` RVA 0x35D6F310 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980)

### path-011667

```text
(exec)# test platform software crimson operational lock release <cr>
```

Handler ` RVA 0x1444A610 `；selector ` 14 `；EOL ` RVA 0x35D6F898 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980)

### path-011979

```text
(exec)# test platform software crimson operational lock release offload <cr>
```

Handler ` RVA 0x1444A610 `；selector ` 15 `；EOL ` RVA 0x35D6F870 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980)

### path-011665

```text
(exec)# test platform software crimson operational lock status <cr>
```

Handler ` RVA 0x1444A610 `；selector ` 16 `；EOL ` RVA 0x35D6FD68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980)

### path-010625

```text
(exec)# test platform software crimson operational offload <cr>
```

Handler ` RVA 0x15711CA0 `；selector ` 5 `；EOL ` RVA 0x35D807B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2c01494c2478aadb](../../evidence/conditions-sets-017.md#c-2c01494c2478aadb)

### path-012090

```text
(exec)# test platform software crimson operational offload add <number:0..4294967295> <number:0..4294967295> <cr>
```

Handler ` RVA 0x15711CA0 `；selector ` 1 `；EOL ` RVA 0x35D7FB40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` table type；` unsigned_number ` start key。

[条件 C-cf4e4e31f2c7d1b7](../../evidence/conditions-sets-080.md#c-cf4e4e31f2c7d1b7) · [参数 P-f2756e519af7f30b](../../evidence/parameters-sets-018.md#p-f2756e519af7f30b)

### path-012093

```text
(exec)# test platform software crimson operational offload delete <number:0..4294967295> <number:0..4294967295> <cr>
```

Handler ` RVA 0x15711CA0 `；selector ` 3 `；EOL ` RVA 0x35D80240 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` table type；` unsigned_number ` start key。

[条件 C-902bd60139f2589b](../../evidence/conditions-sets-056.md#c-902bd60139f2589b) · [参数 P-da19aebda0fb7f04](../../evidence/parameters-sets-016.md#p-da19aebda0fb7f04)

### path-011654

```text
(exec)# test platform software crimson operational offload register <cr>
```

Handler ` RVA 0x15711CA0 `；selector ` 0 `；EOL ` RVA 0x35D7F7C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-76923d32c91e51a8](../../evidence/conditions-sets-046.md#c-76923d32c91e51a8)

### path-011976

```text
(exec)# test platform software crimson operational offload unregister <number:0..4294967295> <cr>
```

Handler ` RVA 0x15711CA0 `；selector ` 4 `；EOL ` RVA 0x35D80530 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` table ID。

[条件 C-2548b433c7819dc4](../../evidence/conditions-sets-015.md#c-2548b433c7819dc4) · [参数 P-5b5df38e858431fe](../../evidence/parameters-sets-007.md#p-5b5df38e858431fe)

### path-012091

```text
(exec)# test platform software crimson operational offload update <number:0..4294967295> <number:0..4294967295> <cr>
```

Handler ` RVA 0x15711CA0 `；selector ` 2 `；EOL ` RVA 0x35D7FEC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` table type；` unsigned_number ` start key。

[条件 C-1f8745f238b3e271](../../evidence/conditions-sets-012.md#c-1f8745f238b3e271) · [参数 P-95f8ffd09e1156d3](../../evidence/parameters-sets-012.md#p-95f8ffd09e1156d3)

### path-011657

```text
(exec)# test platform software crimson operational print db <cr>
```

Handler ` RVA 0x1444A610 `；selector ` 7 `；EOL ` RVA 0x35D6E340 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980)

### path-011975

```text
(exec)# test platform software crimson operational print subblock <number:0..4294967295> <cr>
```

Handler ` RVA 0x1444A680 `；selector ` 21 `；EOL ` RVA 0x35D6E628 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` idb if number。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [参数 P-f15aeabce5aae957](../../evidence/parameters-sets-018.md#p-f15aeabce5aae957)

### path-011659

```text
(exec)# test platform software crimson operational remove <number:0..4294967295> <cr>
```

Handler ` RVA 0x1444A610 `；selector ` 5 `；EOL ` RVA 0x35D6DD58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Item to remove。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [参数 P-20682b7bb48abe7d](../../evidence/parameters-sets-003.md#p-20682b7bb48abe7d)

### path-024974

```text
(exec)# test platform software crimson operational remove <number:0..4294967295> subblock <?option@55558b2c1d30> <cr>
```

Handler ` RVA 0x1444A680 `；selector ` 19 `；EOL ` RVA 0x35D6DD98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Item to remove。

[条件 C-1780357b278cfe6b](../../evidence/conditions-sets-009.md#c-1780357b278cfe6b) · [缺口 G-265fb0f30fb91426](../../evidence/gaps-sets-002.md#g-265fb0f30fb91426) · [参数 P-20682b7bb48abe7d](../../evidence/parameters-sets-003.md#p-20682b7bb48abe7d)

### path-011973

```text
(exec)# test platform software crimson operational remove <number:0..4294967295> update <cr>
```

Handler ` RVA 0x1444A610 `；selector ` 6 `；EOL ` RVA 0x35D6DA88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Item to remove。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [参数 P-20682b7bb48abe7d](../../evidence/parameters-sets-003.md#p-20682b7bb48abe7d)

### path-012095

```text
(exec)# test platform software crimson operational set <number:0..4294967295> idbstate <number:0..4294967295> <cr>
```

Handler ` RVA 0x1444A610 `；selector ` 11 `；EOL ` RVA 0x35D6EF90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Item number to set；` unsigned_number ` idbstate value。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [参数 P-f7eb74ab28d3f63d](../../evidence/parameters-sets-018.md#p-f7eb74ab28d3f63d)

### path-012092

```text
(exec)# test platform software crimson operational set <number:0..4294967295> linestate <number:0..4294967295> <cr>
```

Handler ` RVA 0x1444A610 `；selector ` 8 `；EOL ` RVA 0x35D6E9E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Item number to set；` unsigned_number ` linestate value。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [参数 P-644c4fd59bb06720](../../evidence/parameters-sets-008.md#p-644c4fd59bb06720)

### path-012094

```text
(exec)# test platform software crimson operational set <number:0..4294967295> namestring <string> <cr>
```

Handler ` RVA 0x1444A610 `；selector ` 9 `；EOL ` RVA 0x35D6ECD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Item number to set；` string ` namestring to set。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [参数 P-3262a3267a94e25d](../../evidence/parameters-sets-004.md#p-3262a3267a94e25d)

### path-011974

```text
(exec)# test platform software crimson operational update <number:0..4294967295> description <cr>
```

Handler ` RVA 0x1444A610 `；selector ` 4 `；EOL ` RVA 0x35D6D748 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Data to update。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [参数 P-c4f742b09c31791e](../../evidence/parameters-sets-015.md#p-c4f742b09c31791e)

### path-011660

```text
(exec)# test platform software crimson persist restore-once disable-del <cr>
```

Handler ` RVA 0x1444AEF0 `；selector ` 34 `；EOL ` RVA 0x35D68720 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980)

### path-011661

```text
(exec)# test platform software crimson persist restore-once enable-del <cr>
```

Handler ` RVA 0x1444AEF0 `；selector ` 35 `；EOL ` RVA 0x35D689C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980)

### path-010609

```text
(exec)# test platform software crimson unreferenced <string> <cr>
```

Handler ` RVA 0x1444AEF0 `；selector ` 33 `；EOL ` RVA 0x35D68420 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Database name to check for unreferenced memory。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [参数 P-6325791368bc4ff0](../../evidence/parameters-sets-008.md#p-6325791368bc4ff0)

### path-020832

```text
(exec)# test platform software database get <?ei_services_action@55558b2d81b8> <cr>
```

Handler ` RVA 0x1572F3D0 `；selector ` 0 `；EOL ` RVA 0x35D84238 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-c5024cb0cdfa3df9](../../evidence/gaps-sets-007.md#g-c5024cb0cdfa3df9) · [状态效果 S-813d09e3e894ad37](../../evidence/state_effects-sets-027.md#s-813d09e3e894ad37)

### path-011935

```text
(exec)# test platform software dbal batch deadline <number:1..30000> <number:1..30000> <cr>
```

Handler ` RVA 0x15733360 `；selector ` 0 `；EOL ` RVA 0x35D81CA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Deadline of batch execution, between 1 ms and 30000 ms.；` unsigned_number ` After batch execution, sleep between 1 ms and 30000 ms.。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [参数 P-8d2974dd9c14f70c](../../evidence/parameters-sets-011.md#p-8d2974dd9c14f70c)

### path-012145

```text
(exec)# test platform software dbal batch stress <number:1..4294967295> <number:1..2> <number:1..4294967295> <number:1..2> <cr>
```

Handler ` RVA 0x157307F0 `；selector ` 0 `；EOL ` RVA 0x35D81990 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` number of batches to test；` unsigned_number ` Defer or not in between. 1: defer, 2: do not defer；` unsigned_number ` Number of operation in a batch；` unsigned_number ` Mark batch as priority. 1: normal, 2: priority。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [参数 P-55b53e298fc46ee9](../../evidence/parameters-sets-007.md#p-55b53e298fc46ee9)

### path-010491

```text
(exec)# test platform software dbal lipc create <cr>
```

Handler ` RVA 0x15730E00 `；selector ` 0 `；EOL ` RVA 0x35D82298 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980)

### path-010497

```text
(exec)# test platform software dbal lipc destroy <cr>
```

Handler ` RVA 0x15731120 `；selector ` 0 `；EOL ` RVA 0x35D82540 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980)

### path-010496

```text
(exec)# test platform software dbal ripc create <cr>
```

Handler ` RVA 0x15731320 `；selector ` 0 `；EOL ` RVA 0x35D82818 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980)

### path-010485

```text
(exec)# test platform software dbal scenario <number:1..6> <cr>
```

Handler ` RVA 0x157314C0 `；selector ` 0 `；EOL ` RVA 0x35D81FA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Type of scenario. 1: local, 2: app, 3: TDL sync, 4: TDL async with output, 5: TDL sync in async way, 6: dbal-test-server。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [参数 P-c71e187408ea9439](../../evidence/parameters-sets-015.md#p-c71e187408ea9439)

### path-010472

```text
(exec)# test platform software dbal tunnel start <cr>
```

Handler ` RVA 0x15730260 `；selector ` 0 `；EOL ` RVA 0x35D812A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980)

### path-010479

```text
(exec)# test platform software dbal tunnel stop <cr>
```

Handler ` RVA 0x157306C0 `；selector ` 0 `；EOL ` RVA 0x35D81550 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980)

### path-008256

```text
(exec)# test platform software dta enable <cr>
```

Handler ` RVA 0xC63EF10 `；selector ` 0 `；EOL ` RVA 0x33AC6710 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [状态效果 S-36669c9731dce13e](../../evidence/state_effects-sets-012.md#s-36669c9731dce13e)

### path-023382

```text
(exec)# test platform software dvlan configuration <interface> off <cr>
```

Handler ` RVA 0x15761F40 `；selector ` 0 `；EOL ` RVA 0x35D87DB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-14007d087b118d6a](../../evidence/conditions-sets-008.md#c-14007d087b118d6a) · [缺口 G-bafe3d80572e839b](../../evidence/gaps-sets-007.md#g-bafe3d80572e839b) · [参数 P-3b9615c24f2c98fe](../../evidence/parameters-sets-005.md#p-3b9615c24f2c98fe)

### path-023372

```text
(exec)# test platform software dvlan configuration <interface> on <cr>
```

Handler ` RVA 0x15761F40 `；selector ` 1 `；EOL ` RVA 0x35D87B10 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-14007d087b118d6a](../../evidence/conditions-sets-008.md#c-14007d087b118d6a) · [缺口 G-bafe3d80572e839b](../../evidence/gaps-sets-007.md#g-bafe3d80572e839b) · [参数 P-3b9615c24f2c98fe](../../evidence/parameters-sets-005.md#p-3b9615c24f2c98fe)

### path-010523

```text
(exec)# test platform software dvlan notification off <cr>
```

Handler ` RVA 0x15761F40 `；selector ` 2 `；EOL ` RVA 0x35D88378 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980)

### path-010515

```text
(exec)# test platform software dvlan notification on <cr>
```

Handler ` RVA 0x15761F40 `；selector ` 3 `；EOL ` RVA 0x35D880D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980)

### path-023397

```text
(exec)# test platform software eoam <interface> lm frames <cr>
```

Handler ` RVA 0xBEBA870 `；selector ` 2 `；EOL ` RVA 0x3391D618 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-892ed93611474ffa](../../evidence/conditions-sets-053.md#c-892ed93611474ffa) · [缺口 G-fccfd8124ec0fbdc](../../evidence/gaps-sets-009.md#g-fccfd8124ec0fbdc) · [参数 P-dcd1e2fe01216f0a](../../evidence/parameters-sets-017.md#p-dcd1e2fe01216f0a) · [状态效果 S-ebe79c6173c69f2c](../../evidence/state_effects-sets-050.md#s-ebe79c6173c69f2c)

### path-023388

```text
(exec)# test platform software eoam <interface> rfi dg <cr>
```

Handler ` RVA 0xBEBA870 `；selector ` 1 `；EOL ` RVA 0x3391D2C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5b5d08434c96703a](../../evidence/conditions-sets-036.md#c-5b5d08434c96703a) · [缺口 G-fccfd8124ec0fbdc](../../evidence/gaps-sets-009.md#g-fccfd8124ec0fbdc) · [参数 P-dcd1e2fe01216f0a](../../evidence/parameters-sets-017.md#p-dcd1e2fe01216f0a) · [状态效果 S-4e9932f64b16d3ad](../../evidence/state_effects-sets-017.md#s-4e9932f64b16d3ad)

### path-008327

```text
(exec)# test platform software feature-telemetry disable <cr>
```

Handler ` RVA 0x14B5B8B0 `；selector ` 0 `；EOL ` RVA 0x35D758C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6505e995d929e959](../../evidence/conditions-sets-039.md#c-6505e995d929e959)

### path-008346

```text
(exec)# test platform software feature-telemetry enable <cr>
```

Handler ` RVA 0x14B5B860 `；selector ` 0 `；EOL ` RVA 0x35D75B68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a9d5171a6cf07ad8](../../evidence/conditions-sets-066.md#c-a9d5171a6cf07ad8)

### path-020999

```text
(exec)# test platform software feature-telemetry file <url:dynamic> <cr>
```

Handler ` RVA 0x14B5B7F0 `；selector ` 0 `；EOL ` RVA 0x35D75628 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6551e8a112713dec](../../evidence/conditions-sets-039.md#c-6551e8a112713dec) · [缺口 G-d02fbef2af5804bc](../../evidence/gaps-sets-007.md#g-d02fbef2af5804bc) · [参数 P-6b9c34b52604839b](../../evidence/parameters-sets-008.md#p-6b9c34b52604839b)

### path-011938

```text
(exec)# test platform software flow-control identifiers allocate ebfc all <cr>
```

Handler ` RVA 0xEAFA960 `；selector ` 0 `；EOL ` RVA 0x343AA958 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c316bb26dc0a8a0e](../../evidence/conditions-sets-075.md#c-c316bb26dc0a8a0e) · [状态效果 S-90b9b90c6872f7eb](../../evidence/state_effects-sets-031.md#s-90b9b90c6872f7eb)

### path-012086

```text
(exec)# test platform software infrastructure bipc clear fd <number:1..4294967295> <number:1..4294967295> <cr>
```

Handler ` RVA 0xE9C5930 `；selector ` 6 `；EOL ` RVA 0x34379A90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` IPC channel fd；` unsigned_number ` IPC sequence number。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [参数 P-338c1b6e73df1dd9](../../evidence/parameters-sets-004.md#p-338c1b6e73df1dd9) · [状态效果 S-cbd509cd5a697955](../../evidence/state_effects-sets-043.md#s-cbd509cd5a697955)

### path-010592

```text
(exec)# test platform software infrastructure console on <cr>
```

Handler ` RVA 0xE9C5930 `；selector ` 7 `；EOL ` RVA 0x34379E28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c90d9df4fa9bed6c](../../evidence/conditions-sets-077.md#c-c90d9df4fa9bed6c) · [状态效果 S-2404a4d7f705f00a](../../evidence/state_effects-sets-008.md#s-2404a4d7f705f00a)

### path-010560

```text
(exec)# test platform software infrastructure drop-debug off <cr>
```

Handler ` RVA 0xE9C5930 `；selector ` 5 `；EOL ` RVA 0x34378A18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980)

### path-010565

```text
(exec)# test platform software infrastructure drop-debug on <cr>
```

Handler ` RVA 0xE9C5930 `；selector ` 4 `；EOL ` RVA 0x34378CC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980)

### path-010569

```text
(exec)# test platform software infrastructure pae-cssm send_packet <cr>
```

Handler ` RVA 0x1658B2C0 `；selector ` 0 `；EOL ` RVA 0x35FA4C68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-628d63a9597ebce1](../../evidence/conditions-sets-038.md#c-628d63a9597ebce1)

### path-011648

```text
(exec)# test platform software infrastructure session open <number:1..4294967295> <cr>
```

Handler ` RVA 0xE9C5930 `；selector ` 1 `；EOL ` RVA 0x34379680 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Session handle。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [参数 P-4f1e17e220686aee](../../evidence/parameters-sets-007.md#p-4f1e17e220686aee) · [状态效果 S-902fef83bf46b4d5](../../evidence/state_effects-sets-031.md#s-902fef83bf46b4d5)

### path-010564

```text
(exec)# test platform software infrastructure watchdog off <cr>
```

Handler ` RVA 0xE9C5930 `；selector ` 3 `；EOL ` RVA 0x34378FC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980)

### path-010571

```text
(exec)# test platform software infrastructure watchdog on <cr>
```

Handler ` RVA 0xE9C5930 `；selector ` 2 `；EOL ` RVA 0x34379268 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980)

### path-024583

```text
(exec)# test platform software inject <interface> <address> <address> ipv4 <cr>
```

Handler ` RVA 0xEA9D540 `；selector ` 0 `；EOL ` RVA 0x3439AFB0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Dst MAC address；` address ` Src MAC address。

[条件 C-aa22eca198177ea7](../../evidence/conditions-sets-066.md#c-aa22eca198177ea7) · [缺口 G-24844c597d576968](../../evidence/gaps-sets-002.md#g-24844c597d576968) · [参数 P-a7b741a39392a374](../../evidence/parameters-sets-013.md#p-a7b741a39392a374) · [状态效果 S-cc70e8d64b3b52cf](../../evidence/state_effects-sets-043.md#s-cc70e8d64b3b52cf)

### path-012075

```text
(exec)# test platform software inject bd <number:1..4096> <address> <address> ipv4 <cr>
```

Handler ` RVA 0xEA9C880 `；selector ` 1 `；EOL ` RVA 0x343994F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` BD number；` address ` Dst MAC address；` address ` Src MAC address。

[条件 C-80feb7c74f758a33](../../evidence/conditions-sets-050.md#c-80feb7c74f758a33) · [参数 P-1b2ddfe043e3c48c](../../evidence/parameters-sets-003.md#p-1b2ddfe043e3c48c) · [状态效果 S-fbffc88d8164e54a](../../evidence/state_effects-sets-053.md#s-fbffc88d8164e54a)

### path-012076

```text
(exec)# test platform software inject bd-local <number:1..4096> <address> <address> ipv4 <cr>
```

Handler ` RVA 0xEA9C880 `；selector ` 2 `；EOL ` RVA 0x34399B78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` BD number；` address ` Dst MAC address；` address ` Src MAC address。

[条件 C-7bdc232d232ad06b](../../evidence/conditions-sets-048.md#c-7bdc232d232ad06b) · [参数 P-6e5d53caf4ab1776](../../evidence/parameters-sets-009.md#p-6e5d53caf4ab1776) · [状态效果 S-6c5d875530991375](../../evidence/state_effects-sets-023.md#s-6c5d875530991375)

### path-011951

```text
(exec)# test platform software inject bridge_vlan <number:1..4096> <address> <address> <cr>
```

Handler ` RVA 0xEA9C880 `；selector ` 4 `；EOL ` RVA 0x3439A9F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Bridge VLAN number；` address ` Dst MAC address；` address ` Src MAC address。

[条件 C-6a62b2b36b23b4b5](../../evidence/conditions-sets-041.md#c-6a62b2b36b23b4b5) · [参数 P-f32d96ee52c39e1c](../../evidence/parameters-sets-018.md#p-f32d96ee52c39e1c)

### path-008128

```text
(exec)# test platform software inject bypass <cr>
```

Handler ` RVA 0xEA60A60 `；selector ` 0 `；EOL ` RVA 0x34398A80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980)

### path-025106

```text
(exec)# test platform software inject efp <interface> <number:0..65535> <address> <address> ipv4 <cr>
```

Handler ` RVA 0xEA9C880 `；selector ` 0 `；EOL ` RVA 0x3439B488 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` EFP id；` address ` Dst MAC address；` address ` Src MAC address。

[条件 C-d7af8e77df82e7c5](../../evidence/conditions-sets-083.md#c-d7af8e77df82e7c5) · [缺口 G-c289ed2baa5b197c](../../evidence/gaps-sets-007.md#g-c289ed2baa5b197c) · [参数 P-f0823c50a32323b1](../../evidence/parameters-sets-018.md#p-f0823c50a32323b1) · [状态效果 S-f7175aec9186a92d](../../evidence/state_effects-sets-052.md#s-f7175aec9186a92d)

### path-010505

```text
(exec)# test platform software inject inject-rate <number:1..10000> <cr>
```

Handler ` RVA 0xEA9BB10 `；selector ` 0 `；EOL ` RVA 0x3439A070 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` packets/sec supported by platfform。

[条件 C-6a62b2b36b23b4b5](../../evidence/conditions-sets-041.md#c-6a62b2b36b23b4b5) · [参数 P-d70ce1762a244fde](../../evidence/parameters-sets-016.md#p-d70ce1762a244fde) · [状态效果 S-726ef9019e4f3922](../../evidence/state_effects-sets-024.md#s-726ef9019e4f3922)

### path-010551

```text
(exec)# test platform software inject ipv4 arp-trigger <cr>
```

Handler ` RVA 0xEA60A60 `；selector ` 3 `；EOL ` RVA 0x3439BAB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a6bd1ecbb1c5c724](../../evidence/conditions-sets-064.md#c-a6bd1ecbb1c5c724)

### path-011618

```text
(exec)# test platform software inject ipv4 nexthop <address> <cr>
```

Handler ` RVA 0xEA60A60 `；selector ` 2 `；EOL ` RVA 0x3439B830 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IPv4 Nexthop Address。

[条件 C-a6bd1ecbb1c5c724](../../evidence/conditions-sets-064.md#c-a6bd1ecbb1c5c724) · [参数 P-c9f339e88974e4e5](../../evidence/parameters-sets-015.md#p-c9f339e88974e4e5)

### path-010548

```text
(exec)# test platform software inject ipv6 nd-trigger <cr>
```

Handler ` RVA 0xEA60A60 `；selector ` 4 `；EOL ` RVA 0x3439BD88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a6bd1ecbb1c5c724](../../evidence/conditions-sets-064.md#c-a6bd1ecbb1c5c724)

### path-008133

```text
(exec)# test platform software inject keepalive <cr>
```

Handler ` RVA 0xEA60A60 `；selector ` 6 `；EOL ` RVA 0x343987D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980)

### path-008141

```text
(exec)# test platform software inject off <cr>
```

Handler ` RVA 0xEA60A60 `；selector ` 1 `；EOL ` RVA 0x34398D28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980)

### path-008153

```text
(exec)# test platform software inject pak-priority <cr>
```

Handler ` RVA 0xEA60A60 `；selector ` 5 `；EOL ` RVA 0x34398FD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980)

### path-011649

```text
(exec)# test platform software license expire eval <number:1..259200> <cr>
```

Handler ` RVA 0x12437380 `；selector ` 0 `；EOL ` RVA 0x35867168 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` minutes。

[条件 C-e3c66b1102dd1283](../../evidence/conditions-sets-088.md#c-e3c66b1102dd1283) · [参数 P-1e0ad3d9a0d06b72](../../evidence/parameters-sets-003.md#p-1e0ad3d9a0d06b72)

### path-010581

```text
(exec)# test platform software license metering reachability <cr>
```

Handler ` RVA 0x124373D0 `；selector ` 0 `；EOL ` RVA 0x35866E58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97a2de8a9ab82402](../../evidence/conditions-sets-059.md#c-97a2de8a9ab82402)

### path-010490

```text
(exec)# test platform software lsmpi tx-fail-retry enable <cr>
```

Handler ` RVA 0xED2D730 `；selector ` 0 `；EOL ` RVA 0x3440C730 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [状态效果 S-0cfb0c9f0742d54e](../../evidence/state_effects-sets-003.md#s-0cfb0c9f0742d54e)

### path-025266

```text
(exec)# test platform software macsec default-action ingress_non_control_non_macsec drop ingress_control_non_macsec drop ingress_non_control_macsec drop ingress_control_macsec drop egress_control drop egress_non_control drop <interface> <cr>
```

Handler ` RVA 0x160D7490 `；selector ` 69 `；EOL ` RVA 0x35EC8088 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-058ec18af6a9b940](../../evidence/conditions-sets-003.md#c-058ec18af6a9b940) · [缺口 G-c5b3c6e1a37e0e07](../../evidence/gaps-sets-007.md#g-c5b3c6e1a37e0e07) · [参数 P-f91498f2f12f9ee4](../../evidence/parameters-sets-019.md#p-f91498f2f12f9ee4) · [状态效果 S-483f6f315ddd5f6c](../../evidence/state_effects-sets-016.md#s-483f6f315ddd5f6c)

### path-024968

```text
(exec)# test platform software macsec frame-capture enable direction ingress <interface> <cr>
```

Handler ` RVA 0x160D7490 `；selector ` 66 `；EOL ` RVA 0x35EC8880 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ac9bb1a2d3c65090](../../evidence/conditions-sets-067.md#c-ac9bb1a2d3c65090) · [缺口 G-771707a69e86f88d](../../evidence/gaps-sets-005.md#g-771707a69e86f88d) · [参数 P-1a573e51e4ef55fe](../../evidence/parameters-sets-002.md#p-1a573e51e4ef55fe) · [状态效果 S-fe3b9c6514aa348f](../../evidence/state_effects-sets-054.md#s-fe3b9c6514aa348f)
