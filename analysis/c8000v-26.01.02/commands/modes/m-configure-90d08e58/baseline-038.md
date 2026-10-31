# configure · 六个基础模式的历史连接

[模式索引](README.md) · [总索引](../../README.md)

### path-047382

```text
(config)# do-exec clear eigrp service-family ipv6 neighbors <cr>
```

Handler ` RVA 0xF5933F0 `；selector ` 67 `；EOL ` RVA 0x35475988 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5079892e533d3ab0](../../evidence/conditions-sets-031.md#c-5079892e533d3ab0) · [状态效果 S-24f6910b88a9a4bf](../../evidence/state_effects-sets-008.md#s-24f6910b88a9a4bf)

### path-062038

```text
(config)# do-exec clear eigrp service-family ipv6 neighbors <interface> <cr>
```

Handler ` RVA 0xF5933F0 `；selector ` 67 `；EOL ` RVA 0x35475988 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d4acbfa3ed8d4ea3](../../evidence/conditions-sets-082.md#c-d4acbfa3ed8d4ea3) · [缺口 G-57fa5f4bc32a0961](../../evidence/gaps-sets-004.md#g-57fa5f4bc32a0961) · [参数 P-85069a83d9913ff2](../../evidence/parameters-sets-010.md#p-85069a83d9913ff2) · [状态效果 S-24f6910b88a9a4bf](../../evidence/state_effects-sets-008.md#s-24f6910b88a9a4bf)

### path-060253

```text
(config)# do-exec clear eigrp service-family ipv6 topology <number:1..65535> : <number:1..65535> : <number:0..4294967295> . <number:0..4294967295> . <number:0..4294967295> . <number:0..4294967295> <cr>
```

Handler ` RVA 0xF5933F0 `；selector ` 68 `；EOL ` RVA 0x35476000 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Service:Sub-Service:Instance.Instance.Instance.Instance；` unsigned_number ` Service:Sub-Service:Instance.Instance.Instance.Instance；` unsigned_number ` Service:Sub-Service:Instance.Instance.Instance.Instance；` unsigned_number ` Service:Sub-Service:Instance.Instance.Instance.Instance；` unsigned_number ` Service:Sub-Service:Instance.Instance.Instance.Instance；` unsigned_number ` Service:Sub-Service:Instance.Instance.Instance.Instance。

[条件 C-1993d4bf841bf125](../../evidence/conditions-sets-010.md#c-1993d4bf841bf125) · [参数 P-b117aaae787be4fd](../../evidence/parameters-sets-013.md#p-b117aaae787be4fd) · [状态效果 S-24f6910b88a9a4bf](../../evidence/state_effects-sets-008.md#s-24f6910b88a9a4bf)

### path-054405

```text
(config)# do-exec clear eigrp service-family ipv6 topology active <cr>
```

Handler ` RVA 0xF593530 `；selector ` 69 `；EOL ` RVA 0x354762D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-619ec423152a32a8](../../evidence/conditions-sets-038.md#c-619ec423152a32a8) · [状态效果 S-24f6910b88a9a4bf](../../evidence/state_effects-sets-008.md#s-24f6910b88a9a4bf)

### path-047376

```text
(config)# do-exec clear eigrp service-family ipv6 traffic <cr>
```

Handler ` RVA 0xF5933F0 `；selector ` 70 `；EOL ` RVA 0x35476C28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-619ec423152a32a8](../../evidence/conditions-sets-038.md#c-619ec423152a32a8) · [状态效果 S-24f6910b88a9a4bf](../../evidence/state_effects-sets-008.md#s-24f6910b88a9a4bf)

### path-029057

```text
(config)# do-exec clear entry <number:0..256> <cr>
```

Handler ` RVA 0xCCF7FE0 `；selector ` 0 `；EOL ` RVA 0x33C66A58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Queue entry number。

[条件 C-ae130bfe4f93ffb9](../../evidence/conditions-sets-067.md#c-ae130bfe4f93ffb9) · [参数 P-baff37d66d7bf69e](../../evidence/parameters-sets-014.md#p-baff37d66d7bf69e) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-031263

```text
(config)# do-exec clear environment counters <cr>
```

Handler ` RVA 0xE123D20 `；selector ` 16 `；EOL ` RVA 0x3420AE78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-028442

```text
(config)# do-exec clear eobc counters <cr>
```

Handler ` RVA 0xED896F0 `；selector ` 0 `；EOL ` RVA 0x3442E440 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-028468

```text
(config)# do-exec clear eobc interface <cr>
```

Handler ` RVA 0xED897B0 `；selector ` 0 `；EOL ` RVA 0x3442E6E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-060994

```text
(config)# do-exec clear errdisable <interface> recover-link <cr>
```

Handler ` RVA 0x15E5A980 `；selector ` 5 `；EOL ` RVA 0x35E2AE58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c99dd3fe723e6e0f](../../evidence/conditions-sets-078.md#c-c99dd3fe723e6e0f) · [缺口 G-3556a2d5e51e383c](../../evidence/gaps-sets-002.md#g-3556a2d5e51e383c) · [参数 P-3241337386bbc684](../../evidence/parameters-sets-004.md#p-3241337386bbc684) · [状态效果 S-36f64923dd5b4c37](../../evidence/state_effects-sets-012.md#s-36f64923dd5b4c37)

### path-060993

```text
(config)# do-exec clear errdisable <interface> vlan <cr>
```

Handler ` RVA 0x15E5A980 `；selector ` 4 `；EOL ` RVA 0x35E2A958 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-53e49f8e9b1a2314](../../evidence/conditions-sets-033.md#c-53e49f8e9b1a2314) · [缺口 G-3556a2d5e51e383c](../../evidence/gaps-sets-002.md#g-3556a2d5e51e383c) · [参数 P-3241337386bbc684](../../evidence/parameters-sets-004.md#p-3241337386bbc684) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061525

```text
(config)# do-exec clear errdisable <interface> vlan <string> <cr>
```

Handler ` RVA 0x15E5A980 `；selector ` 3 `；EOL ` RVA 0x35E2A930 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` list of vlans to clear, or &lt;cr&gt; for all vlans。

[条件 C-53e49f8e9b1a2314](../../evidence/conditions-sets-033.md#c-53e49f8e9b1a2314) · [缺口 G-3556a2d5e51e383c](../../evidence/gaps-sets-002.md#g-3556a2d5e51e383c) · [参数 P-b9787b4f9341097c](../../evidence/parameters-sets-014.md#p-b9787b4f9341097c) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-059668

```text
(config)# do-exec clear ethernet cfm ais domain <string> mpid <number:1..8191> port <cr>
```

Handler ` RVA 0xBDD3860 `；selector ` 0 `；EOL ` RVA 0x338CDFB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` maintenance domain name；` unsigned_number ` Maintenance End Point Identifier。

[条件 C-334f7c49a7ede4e3](../../evidence/conditions-sets-020.md#c-334f7c49a7ede4e3) · [参数 P-d12e398db42d71ec](../../evidence/parameters-sets-016.md#p-d12e398db42d71ec) · [状态效果 S-9b316d092fb2d773](../../evidence/state_effects-sets-033.md#s-9b316d092fb2d773)

### path-062245

```text
(config)# do-exec clear ethernet cfm ais link-status Interface <interface> <cr>
```

Handler ` RVA 0xBDD3780 `；selector ` 0 `；EOL ` RVA 0x338CDB70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-fbf3d24dbf74a8e4](../../evidence/conditions-sets-097.md#c-fbf3d24dbf74a8e4) · [缺口 G-f560e27589ff51cb](../../evidence/gaps-sets-008.md#g-f560e27589ff51cb) · [参数 P-878c009ee9041459](../../evidence/parameters-sets-010.md#p-878c009ee9041459) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-035012

```text
(config)# do-exec clear ethernet cfm ccm-learning-database <cr>
```

Handler ` RVA 0xBDD3D70 `；selector ` 0 `；EOL ` RVA 0x338CF840 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6babdf68d76558b8](../../evidence/conditions-sets-042.md#c-6babdf68d76558b8) · [状态效果 S-211b7bcdfd9501b9](../../evidence/state_effects-sets-008.md#s-211b7bcdfd9501b9)

### path-034783

```text
(config)# do-exec clear ethernet cfm errors <cr>
```

Handler ` RVA 0xBDD2B30 `；selector ` 0 `；EOL ` RVA 0x338CE920 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6645a68419d2583e](../../evidence/conditions-sets-040.md#c-6645a68419d2583e) · [状态效果 S-a7466cf0961ecfbb](../../evidence/state_effects-sets-035.md#s-a7466cf0961ecfbb)

### path-044473

```text
(config)# do-exec clear ethernet cfm fast-timeout statistics <cr>
```

Handler ` RVA 0xBDD3CD0 `；selector ` 0 `；EOL ` RVA 0x338CF3C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-49fdd367145abd42](../../evidence/conditions-sets-029.md#c-49fdd367145abd42) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-052375

```text
(config)# do-exec clear ethernet cfm latching-loopback discover-phase mep <cr>
```

Handler ` RVA 0xBDD3360 `；selector ` 1 `；EOL ` RVA 0x338CD438 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ace8b6fac2666806](../../evidence/conditions-sets-067.md#c-ace8b6fac2666806) · [状态效果 S-e873a55990200801](../../evidence/state_effects-sets-049.md#s-e873a55990200801)

### path-052363

```text
(config)# do-exec clear ethernet cfm latching-loopback discover-phase mip <cr>
```

Handler ` RVA 0xBDD3360 `；selector ` 2 `；EOL ` RVA 0x338CD6E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ace8b6fac2666806](../../evidence/conditions-sets-067.md#c-ace8b6fac2666806) · [状态效果 S-bc748fb3b99ef1bc](../../evidence/state_effects-sets-040.md#s-bc748fb3b99ef1bc)

### path-044316

```text
(config)# do-exec clear ethernet cfm maintenance-points remote <cr>
```

Handler ` RVA 0xBDD28E0 `；selector ` 0 `；EOL ` RVA 0x338CC7F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ace8b6fac2666806](../../evidence/conditions-sets-067.md#c-ace8b6fac2666806) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-056846

```text
(config)# do-exec clear ethernet cfm maintenance-points remote domain <string> <cr>
```

Handler ` RVA 0xBDD2A20 `；selector ` 0 `；EOL ` RVA 0x338CC830 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` maintenance domain name。

[条件 C-ace8b6fac2666806](../../evidence/conditions-sets-067.md#c-ace8b6fac2666806) · [参数 P-b4f885fc792161b1](../../evidence/parameters-sets-014.md#p-b4f885fc792161b1) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-056875

```text
(config)# do-exec clear ethernet cfm pm session db <number:0..8000> <cr>
```

Handler ` RVA 0xBE8C2A0 `；selector ` 0 `；EOL ` RVA 0x339155B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Session Id。

[条件 C-ace8b6fac2666806](../../evidence/conditions-sets-067.md#c-ace8b6fac2666806) · [参数 P-c0ee7e00d5a1eec9](../../evidence/parameters-sets-015.md#p-c0ee7e00d5a1eec9) · [状态效果 S-ee8f5437506e6b71](../../evidence/state_effects-sets-050.md#s-ee8f5437506e6b71)

### path-034593

```text
(config)# do-exec clear ethernet cfm statistics <cr>
```

Handler ` RVA 0xBDD3070 `；selector ` 0 `；EOL ` RVA 0x338CD040 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ace8b6fac2666806](../../evidence/conditions-sets-067.md#c-ace8b6fac2666806) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-034520

```text
(config)# do-exec clear ethernet cfm traceroute-cache <cr>
```

Handler ` RVA 0xBDD3D20 `；selector ` 0 `；EOL ` RVA 0x338CCD08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ace8b6fac2666806](../../evidence/conditions-sets-067.md#c-ace8b6fac2666806) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-034503

```text
(config)# do-exec clear ethernet lmi statistics <cr>
```

Handler ` RVA 0xBEC38F0 `；selector ` 0 `；EOL ` RVA 0x339203E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e252cf8c35d4f1d1](../../evidence/conditions-sets-087.md#c-e252cf8c35d4f1d1) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061224

```text
(config)# do-exec clear ethernet lmi statistics <interface> <cr>
```

Handler ` RVA 0xBEC38F0 `；selector ` 0 `；EOL ` RVA 0x339203E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-451bec9c479be8c2](../../evidence/conditions-sets-027.md#c-451bec9c479be8c2) · [缺口 G-8c4906c49f660d40](../../evidence/gaps-sets-005.md#g-8c4906c49f660d40) · [参数 P-711b12ab2ac057ea](../../evidence/parameters-sets-009.md#p-711b12ab2ac057ea) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-034495

```text
(config)# do-exec clear ethernet oam statistics <cr>
```

Handler ` RVA 0xBEECC20 `；selector ` 44 `；EOL ` RVA 0x3392F790 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ace8b6fac2666806](../../evidence/conditions-sets-067.md#c-ace8b6fac2666806) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061852

```text
(config)# do-exec clear ethernet oam statistics interface <interface> <cr>
```

Handler ` RVA 0xBEECC20 `；selector ` 45 `；EOL ` RVA 0x3392F850 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-707ad9cd7f9d0813](../../evidence/conditions-sets-043.md#c-707ad9cd7f9d0813) · [缺口 G-4b6f91a8b7b837de](../../evidence/gaps-sets-003.md#g-4b6f91a8b7b837de) · [参数 P-973a347b471c3aa4](../../evidence/parameters-sets-012.md#p-973a347b471c3aa4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-056948

```text
(config)# do-exec clear ethernet service instance id <number:1..16384> mac-tunnel <cr>
```

Handler ` RVA 0xC0188D0 `；selector ` 1 `；EOL ` RVA 0x33979C58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Identifier。

[条件 C-ea732fa9e043fe11](../../evidence/conditions-sets-091.md#c-ea732fa9e043fe11) · [参数 P-1dc6a57d8cba6c9f](../../evidence/parameters-sets-003.md#p-1dc6a57d8cba6c9f) · [状态效果 S-235293448995e561](../../evidence/state_effects-sets-008.md#s-235293448995e561)

### path-058981

```text
(config)# do-exec clear ethernet service instance id <number:1..16384> mac-tunnel errdisable <cr>
```

Handler ` RVA 0xC0357A0 `；selector ` 3 `；EOL ` RVA 0x33985898 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Identifier。

[条件 C-6966d62b8dc7328d](../../evidence/conditions-sets-041.md#c-6966d62b8dc7328d) · [参数 P-1dc6a57d8cba6c9f](../../evidence/parameters-sets-003.md#p-1dc6a57d8cba6c9f) · [状态效果 S-235293448995e561](../../evidence/state_effects-sets-008.md#s-235293448995e561)

### path-061861

```text
(config)# do-exec clear ethernet service instance interface <interface> <cr>
```

Handler ` RVA 0xC0188D0 `；selector ` 1 `；EOL ` RVA 0x33979C58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b6b4c4e6cab630aa](../../evidence/conditions-sets-071.md#c-b6b4c4e6cab630aa) · [缺口 G-889d5e09ea647677](../../evidence/gaps-sets-005.md#g-889d5e09ea647677) · [参数 P-93b1a4af74db590d](../../evidence/parameters-sets-011.md#p-93b1a4af74db590d) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062253

```text
(config)# do-exec clear ethernet service instance interface <interface> errdisable <cr>
```

Handler ` RVA 0xC0357A0 `；selector ` 3 `；EOL ` RVA 0x33985898 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-71bd0dedb7aa3c48](../../evidence/conditions-sets-044.md#c-71bd0dedb7aa3c48) · [缺口 G-889d5e09ea647677](../../evidence/gaps-sets-005.md#g-889d5e09ea647677) · [参数 P-93b1a4af74db590d](../../evidence/parameters-sets-011.md#p-93b1a4af74db590d) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-044353

```text
(config)# do-exec clear ethernet service internal back-trace <cr>
```

Handler ` RVA 0xC013D80 `；selector ` 0 `；EOL ` RVA 0x3397BF40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-59b07fa78c1ec760](../../evidence/conditions-sets-035.md#c-59b07fa78c1ec760) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-044382

```text
(config)# do-exec clear ethernet service ipc statistics <cr>
```

Handler ` RVA 0xBF920F0 `；selector ` 0 `；EOL ` RVA 0x33962C98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ace8b6fac2666806](../../evidence/conditions-sets-067.md#c-ace8b6fac2666806) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061240

```text
(config)# do-exec clear ethernet service mac-tunnel <number:dynamic> <cr>
```

Handler ` RVA 0xC0188D0 `；selector ` 2 `；EOL ` RVA 0x339796A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Mac-in-Mac tunnel identifier。

[条件 C-456ecd9cf3b974fe](../../evidence/conditions-sets-027.md#c-456ecd9cf3b974fe) · [缺口 G-aab5934e79e0b703](../../evidence/gaps-sets-006.md#g-aab5934e79e0b703) · [参数 P-ccf825a36f0ff1d1](../../evidence/parameters-sets-016.md#p-ccf825a36f0ff1d1) · [状态效果 S-cd26ba20b915ceb4](../../evidence/state_effects-sets-043.md#s-cd26ba20b915ceb4)

### path-048525

```text
(config)# do-exec clear event manager detector counters <cr>
```

Handler ` RVA 0xC0CB550 `；selector ` 0 `；EOL ` RVA 0x339BCBB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-055028

```text
(config)# do-exec clear event manager detector rpc counters <cr>
```

Handler ` RVA 0xC0A29A0 `；selector ` 0 `；EOL ` RVA 0x3399C3F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-055071

```text
(config)# do-exec clear event manager detector rpc sessions <cr>
```

Handler ` RVA 0xC0A2BA0 `；selector ` 0 `；EOL ` RVA 0x3399C698 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-048469

```text
(config)# do-exec clear event manager server counters <cr>
```

Handler ` RVA 0xC0CB5C0 `；selector ` 0 `；EOL ` RVA 0x339BC8E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-026432

```text
(config)# do-exec clear facility-alarm <cr>
```

Handler ` RVA 0xC299EF0 `；selector ` 0 `；EOL ` RVA 0x33A28388 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-028119

```text
(config)# do-exec clear facility-alarm critical <cr>
```

Handler ` RVA 0xC299990 `；selector ` 0 `；EOL ` RVA 0x33A27F68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-ad683d9883ac3685](../../evidence/state_effects-sets-037.md#s-ad683d9883ac3685)

### path-061847

```text
(config)# do-exec clear facility-alarm hw-module slot <number:dynamic> oir <cr>
```

Handler ` RVA 0xC299D10 `；selector ` 0 `；EOL ` RVA 0x33A28508 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` slot number。

[条件 C-8ae4050b707a0805](../../evidence/conditions-sets-054.md#c-8ae4050b707a0805) · [缺口 G-917e8cdd9748594d](../../evidence/gaps-sets-005.md#g-917e8cdd9748594d) · [参数 P-127131a92a3cda1a](../../evidence/parameters-sets-002.md#p-127131a92a3cda1a) · [状态效果 S-f320b999652cdf81](../../evidence/state_effects-sets-051.md#s-f320b999652cdf81)

### path-061266

```text
(config)# do-exec clear flow exporter <?option@555588f376b0> statistics <cr>
```

Handler ` RVA 0xC154D30 `；selector ` 0 `；EOL ` RVA 0x339E3370 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-494988544add441b](../../evidence/conditions-sets-029.md#c-494988544add441b) · [缺口 G-61c2b27c5cfd852e](../../evidence/gaps-sets-004.md#g-61c2b27c5cfd852e) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-034982

```text
(config)# do-exec clear flow exporter statistics <cr>
```

Handler ` RVA 0xC154D30 `；selector ` 0 `；EOL ` RVA 0x339E3370 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062788

```text
(config)# do-exec clear flow monitor <?option@555588f41c90> <cr>
```

Handler ` RVA 0xC18F9D0 `；selector ` 0 `；EOL ` RVA 0x339EDE90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1af8d2b7a0b4820d](../../evidence/conditions-sets-011.md#c-1af8d2b7a0b4820d) · [缺口 G-780ba3d830198b03](../../evidence/gaps-sets-005.md#g-780ba3d830198b03) · [状态效果 S-6f700220b7eb5d44](../../evidence/state_effects-sets-024.md#s-6f700220b7eb5d44)

### path-031728

```text
(config)# do-exec clear flowspec afi-all <cr>
```

Handler ` RVA 0x1344A810 `；selector ` 5 `；EOL ` RVA 0x35A98610 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a0a86034b1ad4591](../../evidence/conditions-sets-062.md#c-a0a86034b1ad4591) · [状态效果 S-d63062a30a241013](../../evidence/state_effects-sets-045.md#s-d63062a30a241013)

### path-061517

```text
(config)# do-exec clear flowspec afi-all nlri <hex-data> <cr>
```

Handler ` RVA 0x1344A810 `；selector ` 6 `；EOL ` RVA 0x35A98358 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` hexdata ` Enter NLRI in hex。

[条件 C-3de89bf6fb48a2bc](../../evidence/conditions-sets-024.md#c-3de89bf6fb48a2bc) · [缺口 G-f7bf8992244e3522](../../evidence/gaps-sets-009.md#g-f7bf8992244e3522) · [参数 P-29e848b788832a0a](../../evidence/parameters-sets-004.md#p-29e848b788832a0a) · [状态效果 S-d63062a30a241013](../../evidence/state_effects-sets-045.md#s-d63062a30a241013)

### path-039458

```text
(config)# do-exec clear flowspec counters afi-all <cr>
```

Handler ` RVA 0x1344A810 `；selector ` 2 `；EOL ` RVA 0x35A97D60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-e1c9287f50fc57c0](../../evidence/state_effects-sets-048.md#s-e1c9287f50fc57c0)

### path-039335

```text
(config)# do-exec clear flowspec counters internal <cr>
```

Handler ` RVA 0x1344A810 `；selector ` 4 `；EOL ` RVA 0x35A97918 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-974ee9b08838ee4a](../../evidence/state_effects-sets-032.md#s-974ee9b08838ee4a)

### path-037783

```text
(config)# do-exec clear fqdn packet statistics <cr>
```

Handler ` RVA 0xC2E0BF0 `；selector ` 0 `；EOL ` RVA 0x33A3CB48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-477171926bc8d55e](../../evidence/state_effects-sets-016.md#s-477171926bc8d55e)

### path-030538

```text
(config)# do-exec clear frame-relay counter <cr>
```

Handler ` RVA 0xF606570 `；selector ` 18 `；EOL ` RVA 0x34700850 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061402

```text
(config)# do-exec clear frame-relay counter interface <interface> <cr>
```

Handler ` RVA 0xF606570 `；selector ` 18 `；EOL ` RVA 0x34700850 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-babea90797a9c280](../../evidence/conditions-sets-072.md#c-babea90797a9c280) · [缺口 G-3fbf5ffe33c8c495](../../evidence/gaps-sets-003.md#g-3fbf5ffe33c8c495) · [参数 P-560b0669f2f3e579](../../evidence/parameters-sets-007.md#p-560b0669f2f3e579) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-030567

```text
(config)# do-exec clear frame-relay inarp <cr>
```

Handler ` RVA 0xF62D080 `；selector ` 17 `；EOL ` RVA 0x3470EE40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061406

```text
(config)# do-exec clear frame-relay inarp interface <interface> <cr>
```

Handler ` RVA 0xF62D080 `；selector ` 17 `；EOL ` RVA 0x3470EE40 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4f91056fb4def1bd](../../evidence/conditions-sets-031.md#c-4f91056fb4def1bd) · [缺口 G-748efb6ea7786896](../../evidence/gaps-sets-004.md#g-748efb6ea7786896) · [参数 P-ce79cb5a21e80ae0](../../evidence/parameters-sets-016.md#p-ce79cb5a21e80ae0) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-030699

```text
(config)# do-exec clear host <string> <cr>
```

Handler ` RVA 0xD128DD0 `；selector ` 0 `；EOL ` RVA 0x33D95930 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Hostname to delete (* for all entries)。

[条件 C-7cd4fea57bafbb25](../../evidence/conditions-sets-048.md#c-7cd4fea57bafbb25) · [参数 P-5fa77e3c3044d1c6](../../evidence/parameters-sets-008.md#p-5fa77e3c3044d1c6) · [状态效果 S-c200b95993ab0afa](../../evidence/state_effects-sets-041.md#s-c200b95993ab0afa)

### path-030424

```text
(config)# do-exec clear icm statistics <cr>
```

Handler ` RVA 0xC2FAF60 `；selector ` 0 `；EOL ` RVA 0x33A40790 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-63090568c0c45705](../../evidence/state_effects-sets-021.md#s-63090568c0c45705)

### path-060515

```text
(config)# do-exec clear interface <interface> <cr>
```

Handler ` RVA 0xE002C40 `；selector ` 0 `；EOL ` RVA 0x341661E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7024495c76d61492](../../evidence/conditions-sets-043.md#c-7024495c76d61492) · [缺口 G-2840999d7791e4d2](../../evidence/gaps-sets-002.md#g-2840999d7791e4d2) · [参数 P-2f2c0b6b3666db1a](../../evidence/parameters-sets-004.md#p-2f2c0b6b3666db1a) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062812

```text
(config)# do-exec clear interface range <interface> <interface> <cr>
```

Handler ` RVA 0xE002F70 `；selector ` 0 `；EOL ` RVA 0x341664F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e0bce9c46a7671f2](../../evidence/conditions-sets-087.md#c-e0bce9c46a7671f2) · [缺口 G-41b79ce593cc13f4](../../evidence/gaps-sets-003.md#g-41b79ce593cc13f4) · [参数 P-dce3ddcd12794452](../../evidence/parameters-sets-017.md#p-dce3ddcd12794452) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-027612

```text
(config)# do-exec clear iox <cr>
```

Handler ` RVA 0xEADA610 `；selector ` 0 `；EOL ` RVA 0x343A3698 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-035838

```text
(config)# do-exec clear ip access-list counters <cr>
```

Handler ` RVA 0xCEEDDF0 `；selector ` 0 `；EOL ` RVA 0x33D2D580 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-29b5b928497ba869](../../evidence/conditions-sets-016.md#c-29b5b928497ba869) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-030512

```text
(config)# do-exec clear ip accounting <cr>
```

Handler ` RVA 0xD17A5F0 `；selector ` 0 `；EOL ` RVA 0x33DA6DB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-d286aa82338d599b](../../evidence/state_effects-sets-045.md#s-d286aa82338d599b)

### path-035303

```text
(config)# do-exec clear ip arp <address> <cr>
```

Handler ` RVA 0xCF5FF90 `；selector ` 0 `；EOL ` RVA 0x33D1E250 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP address of dynamic ARP entry。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [参数 P-b690c2ce67487b89](../../evidence/parameters-sets-014.md#p-b690c2ce67487b89) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-044972

```text
(config)# do-exec clear ip arp poll statistics <cr>
```

Handler ` RVA 0xCFE25A0 `；selector ` 0 `；EOL ` RVA 0x33D1E538 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-060884

```text
(config)# do-exec clear ip bgp <?match_ipv6_addrinfo_action@555589a037f0> <cr>
```

Handler ` RVA 0xF1C77B0 `；selector ` 0 `；EOL ` RVA 0x344AFD80 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6913f702d805e73d](../../evidence/conditions-sets-041.md#c-6913f702d805e73d) · [缺口 G-14199b39249e3a2d](../../evidence/gaps-sets-001.md#g-14199b39249e3a2d) · [状态效果 S-f2a4c9062eaf473a](../../evidence/state_effects-sets-051.md#s-f2a4c9062eaf473a)

### path-061351

```text
(config)# do-exec clear ip bgp <?match_ipv6_addrinfo_action@555589a037f0> cease <cr>
```

Handler ` RVA 0xF1CC180 `；selector ` 7 `；EOL ` RVA 0x344B0470 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4d372dcc1645fdde](../../evidence/conditions-sets-030.md#c-4d372dcc1645fdde) · [缺口 G-14199b39249e3a2d](../../evidence/gaps-sets-001.md#g-14199b39249e3a2d) · [状态效果 S-f2a4c9062eaf473a](../../evidence/state_effects-sets-051.md#s-f2a4c9062eaf473a)

### path-061347

```text
(config)# do-exec clear ip bgp <?match_ipv6_addrinfo_action@555589a037f0> flap-statistics <cr>
```

Handler ` RVA 0xF1CC180 `；selector ` 6 `；EOL ` RVA 0x344B01C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4d372dcc1645fdde](../../evidence/conditions-sets-030.md#c-4d372dcc1645fdde) · [缺口 G-14199b39249e3a2d](../../evidence/gaps-sets-001.md#g-14199b39249e3a2d) · [状态效果 S-f2a4c9062eaf473a](../../evidence/state_effects-sets-051.md#s-f2a4c9062eaf473a)

### path-061348

```text
(config)# do-exec clear ip bgp <?match_ipv6_addrinfo_action@555589a037f0> internal <cr>
```

Handler ` RVA 0xF1CD7B0 `；selector ` 0 `；EOL ` RVA 0x344B0730 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e59971b147dbc394](../../evidence/conditions-sets-089.md#c-e59971b147dbc394) · [缺口 G-14199b39249e3a2d](../../evidence/gaps-sets-001.md#g-14199b39249e3a2d) · [状态效果 S-f2a4c9062eaf473a](../../evidence/state_effects-sets-051.md#s-f2a4c9062eaf473a)

### path-030159

```text
(config)# do-exec clear ip cache <cr>
```

Handler ` RVA 0xD49E510 `；selector ` 0 `；EOL ` RVA 0x33E54E00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-036914

```text
(config)# do-exec clear ip casa counters <cr>
```

Handler ` RVA 0x1132C870 `；selector ` 0 `；EOL ` RVA 0x35499608 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061415

```text
(config)# do-exec clear ip cef * prefix-statistics <cr>
```

Handler ` RVA 0xB61F7B0 `；selector ` 0 `；EOL ` RVA 0x337C4660 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6d98fee83714ae9f](../../evidence/conditions-sets-042.md#c-6d98fee83714ae9f) · [缺口 G-3491539c14800b04](../../evidence/gaps-sets-002.md#g-3491539c14800b04) · [状态效果 S-30332ce42490d73c](../../evidence/state_effects-sets-011.md#s-30332ce42490d73c)

### path-037189

```text
(config)# do-exec clear ip cef event-log <cr>
```

Handler ` RVA 0xB5ECF20 `；selector ` 0 `；EOL ` RVA 0x337B4F90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-037143

```text
(config)# do-exec clear ip cef inconsistency <cr>
```

Handler ` RVA 0xB5ECEE0 `；selector ` 0 `；EOL ` RVA 0x337B4CE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-037539

```text
(config)# do-exec clear ip cef prefix-statistics <cr>
```

Handler ` RVA 0xB61F7B0 `；selector ` 0 `；EOL ` RVA 0x337C4660 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d5f42d62acdf9713](../../evidence/conditions-sets-083.md#c-d5f42d62acdf9713) · [状态效果 S-30332ce42490d73c](../../evidence/state_effects-sets-011.md#s-30332ce42490d73c)

### path-030166

```text
(config)# do-exec clear ip cgmp <cr>
```

Handler ` RVA 0xF6779A0 `；selector ` 0 `；EOL ` RVA 0x34746408 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-15c8fb31734caa71](../../evidence/conditions-sets-009.md#c-15c8fb31734caa71) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-060869

```text
(config)# do-exec clear ip cgmp <interface> <cr>
```

Handler ` RVA 0xF6779A0 `；selector ` 0 `；EOL ` RVA 0x34746408 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ec08263733a632e6](../../evidence/conditions-sets-091.md#c-ec08263733a632e6) · [缺口 G-3fdf2da03149b692](../../evidence/gaps-sets-003.md#g-3fdf2da03149b692) · [参数 P-606ce1ff40b811af](../../evidence/parameters-sets-008.md#p-606ce1ff40b811af) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061421

```text
(config)# do-exec clear ip dhcp binding * <cr>
```

Handler ` RVA 0xD29A1F0 `；selector ` 0 `；EOL ` RVA 0x33DE4238 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a4558eaf54a7b708](../../evidence/conditions-sets-063.md#c-a4558eaf54a7b708) · [缺口 G-34a6802e331f1db9](../../evidence/gaps-sets-002.md#g-34a6802e331f1db9) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-046950

```text
(config)# do-exec clear ip dhcp binding <address> <cr>
```

Handler ` RVA 0xD29A1F0 `；selector ` 1 `；EOL ` RVA 0x33DE44E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Clear a specific binding。

[条件 C-915a8514a34f7b53](../../evidence/conditions-sets-056.md#c-915a8514a34f7b53) · [参数 P-701f423f9be8657b](../../evidence/parameters-sets-009.md#p-701f423f9be8657b) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061432

```text
(config)# do-exec clear ip dhcp conflict * <cr>
```

Handler ` RVA 0xD29A1F0 `；selector ` 2 `；EOL ` RVA 0x33DE4900 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9bb8e41d662d8273](../../evidence/conditions-sets-060.md#c-9bb8e41d662d8273) · [缺口 G-de6621ce3918ea84](../../evidence/gaps-sets-008.md#g-de6621ce3918ea84) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-046996

```text
(config)# do-exec clear ip dhcp conflict <address> <cr>
```

Handler ` RVA 0xD29A1F0 `；selector ` 3 `；EOL ` RVA 0x33DE4BA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Clear a specific conflict。

[条件 C-1ef20701edbe572d](../../evidence/conditions-sets-012.md#c-1ef20701edbe572d) · [参数 P-98938e3b3a412be2](../../evidence/parameters-sets-012.md#p-98938e3b3a412be2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-047068

```text
(config)# do-exec clear ip dhcp limit lease <cr>
```

Handler ` RVA 0xD29A1F0 `；selector ` 8 `；EOL ` RVA 0x33DE5590 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2498161afb0903f2](../../evidence/conditions-sets-014.md#c-2498161afb0903f2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062003

```text
(config)# do-exec clear ip dhcp limit lease <interface> <cr>
```

Handler ` RVA 0xD29A1F0 `；selector ` 7 `；EOL ` RVA 0x33DE5568 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-569a38e54e2c9a80](../../evidence/conditions-sets-034.md#c-569a38e54e2c9a80) · [缺口 G-02b924108f71f223](../../evidence/gaps-sets-001.md#g-02b924108f71f223) · [参数 P-bc74f852c8c1296f](../../evidence/parameters-sets-014.md#p-bc74f852c8c1296f) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-046830

```text
(config)# do-exec clear ip dhcp server odap-statistics <cr>
```

Handler ` RVA 0xD29A1F0 `；selector ` 10 `；EOL ` RVA 0x33DE3E18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-88701873d8528f78](../../evidence/conditions-sets-053.md#c-88701873d8528f78) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-046870

```text
(config)# do-exec clear ip dhcp server statistics <cr>
```

Handler ` RVA 0xD29A1F0 `；selector ` 4 `；EOL ` RVA 0x33DE3918 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b7107639c9a89805](../../evidence/conditions-sets-071.md#c-b7107639c9a89805) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061991

```text
(config)# do-exec clear ip dhcp server statistics <interface> <cr>
```

Handler ` RVA 0xD29A1F0 `；selector ` 9 `；EOL ` RVA 0x33DE38F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-bdf76c153e9321d1](../../evidence/conditions-sets-073.md#c-bdf76c153e9321d1) · [缺口 G-97d7874488d4e0e1](../../evidence/gaps-sets-006.md#g-97d7874488d4e0e1) · [参数 P-9be37e5051587589](../../evidence/parameters-sets-012.md#p-9be37e5051587589) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061989

```text
(config)# do-exec clear ip dhcp snooping binding * <cr>
```

Handler ` RVA 0x15FA9260 `；selector ` 0 `；EOL ` RVA 0x35E818A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-29283e337c801d43](../../evidence/conditions-sets-016.md#c-29283e337c801d43) · [缺口 G-51a56d3715830f1e](../../evidence/gaps-sets-003.md#g-51a56d3715830f1e) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-054135

```text
(config)# do-exec clear ip dhcp snooping binding <address> <cr>
```

Handler ` RVA 0x15FA9260 `；selector ` 1 `；EOL ` RVA 0x35E81B48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Clear address specific bindings。

[条件 C-88701873d8528f78](../../evidence/conditions-sets-053.md#c-88701873d8528f78) · [参数 P-24a6453abfb0d28a](../../evidence/parameters-sets-003.md#p-24a6453abfb0d28a) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061994

```text
(config)# do-exec clear ip dhcp snooping binding <interface> <cr>
```

Handler ` RVA 0x15FA9260 `；selector ` 2 `；EOL ` RVA 0x35E81E70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e61df0f16bb1adb2](../../evidence/conditions-sets-089.md#c-e61df0f16bb1adb2) · [缺口 G-4669f266a5c3f438](../../evidence/gaps-sets-003.md#g-4669f266a5c3f438) · [参数 P-06a696bd55f1f878](../../evidence/parameters-sets-001.md#p-06a696bd55f1f878) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-057921

```text
(config)# do-exec clear ip dhcp snooping binding bridge-domain <string> <cr>
```

Handler ` RVA 0x15FA9260 `；selector ` 3 `；EOL ` RVA 0x35E821D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` DHCP Snooping bd range, example : 1,3-5,7,9-11。

[条件 C-75fcf496af8704d2](../../evidence/conditions-sets-046.md#c-75fcf496af8704d2) · [参数 P-cce908d8140214c8](../../evidence/parameters-sets-016.md#p-cce908d8140214c8) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-054129

```text
(config)# do-exec clear ip dhcp snooping database statistics <cr>
```

Handler ` RVA 0x15FAA320 `；selector ` 0 `；EOL ` RVA 0x35E825B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-88701873d8528f78](../../evidence/conditions-sets-053.md#c-88701873d8528f78) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-046859

```text
(config)# do-exec clear ip dhcp snooping statistics <cr>
```

Handler ` RVA 0x15FA9590 `；selector ` 0 `；EOL ` RVA 0x35E82840 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-88701873d8528f78](../../evidence/conditions-sets-053.md#c-88701873d8528f78) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061429

```text
(config)# do-exec clear ip dhcp subnet * <cr>
```

Handler ` RVA 0xD29A1F0 `；selector ` 6 `；EOL ` RVA 0x33DE4F30 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8c345d6d7210342a](../../evidence/conditions-sets-054.md#c-8c345d6d7210342a) · [缺口 G-a04ce115b4b6ed1d](../../evidence/gaps-sets-006.md#g-a04ce115b4b6ed1d) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-046993

```text
(config)# do-exec clear ip dhcp subnet <address> <cr>
```

Handler ` RVA 0xD29A1F0 `；selector ` 5 `；EOL ` RVA 0x33DE51D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Specify an address in the subnet to clear。

[条件 C-8127a4d438972794](../../evidence/conditions-sets-050.md#c-8127a4d438972794) · [参数 P-604821058269eb93](../../evidence/parameters-sets-008.md#p-604821058269eb93) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061354

```text
(config)# do-exec clear ip dns servers * <cr>
```

Handler ` RVA 0xD133B70 `；selector ` 0 `；EOL ` RVA 0x33D9B6E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1fbaa6f203a36e32](../../evidence/conditions-sets-012.md#c-1fbaa6f203a36e32) · [缺口 G-71508ff11bc3fd83](../../evidence/gaps-sets-004.md#g-71508ff11bc3fd83) · [状态效果 S-72a59dd6f5b39880](../../evidence/state_effects-sets-024.md#s-72a59dd6f5b39880)

### path-045949

```text
(config)# do-exec clear ip dns servers <address> <cr>
```

Handler ` RVA 0xD133B70 `；selector ` 0 `；EOL ` RVA 0x33D9B6E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IPV4 Server Address。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [参数 P-f3837ab8cf79a70e](../../evidence/parameters-sets-018.md#p-f3837ab8cf79a70e) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-029640

```text
(config)# do-exec clear ip drp <cr>
```

Handler ` RVA 0xF4F0BA0 `；selector ` 0 `；EOL ` RVA 0x3467ADA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-036976

```text
(config)# do-exec clear ip eigrp events <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 71 `；EOL ` RVA 0x346D9C60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3d6bbdb71e02be33](../../evidence/conditions-sets-024.md#c-3d6bbdb71e02be33) · [状态效果 S-e504741cce9766f2](../../evidence/state_effects-sets-048.md#s-e504741cce9766f2)

### path-036931

```text
(config)# do-exec clear ip eigrp logging <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 72 `；EOL ` RVA 0x346D99B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3d6bbdb71e02be33](../../evidence/conditions-sets-024.md#c-3d6bbdb71e02be33) · [状态效果 S-e504741cce9766f2](../../evidence/state_effects-sets-048.md#s-e504741cce9766f2)

### path-037037

```text
(config)# do-exec clear ip eigrp neighbors <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 67 `；EOL ` RVA 0x346D92A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-753308e3327070a9](../../evidence/conditions-sets-045.md#c-753308e3327070a9) · [状态效果 S-e504741cce9766f2](../../evidence/state_effects-sets-048.md#s-e504741cce9766f2)

### path-061384

```text
(config)# do-exec clear ip eigrp neighbors <interface> <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 67 `；EOL ` RVA 0x346D92A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-da0a09f0c3020167](../../evidence/conditions-sets-084.md#c-da0a09f0c3020167) · [缺口 G-d088bfb99087ae2b](../../evidence/gaps-sets-007.md#g-d088bfb99087ae2b) · [参数 P-db885fec6df06f89](../../evidence/parameters-sets-017.md#p-db885fec6df06f89) · [状态效果 S-e504741cce9766f2](../../evidence/state_effects-sets-048.md#s-e504741cce9766f2)

### path-046353

```text
(config)# do-exec clear ip eigrp topology <address> <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 68 `；EOL ` RVA 0x346D96E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Network to clear from topology。

[条件 C-3d6bbdb71e02be33](../../evidence/conditions-sets-024.md#c-3d6bbdb71e02be33) · [参数 P-c5c28ea144019d4d](../../evidence/parameters-sets-015.md#p-c5c28ea144019d4d) · [状态效果 S-e504741cce9766f2](../../evidence/state_effects-sets-048.md#s-e504741cce9766f2)

### path-061383

```text
(config)# do-exec clear ip eigrp topology <prefix:dynamic> <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 68 `；EOL ` RVA 0x346D96E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` Prefix &lt;network&gt;/&lt;length&gt;, e.g., 192.168.0.0/16。

[条件 C-e4983cba84f92f42](../../evidence/conditions-sets-088.md#c-e4983cba84f92f42) · [缺口 G-fbb8fea18633edf3](../../evidence/gaps-sets-009.md#g-fbb8fea18633edf3) · [参数 P-f39852c340c83db0](../../evidence/parameters-sets-018.md#p-f39852c340c83db0) · [状态效果 S-7d62cbf5e39fabe2](../../evidence/state_effects-sets-027.md#s-7d62cbf5e39fabe2)

### path-053367

```text
(config)# do-exec clear ip http client cache all <cr>
```

Handler ` RVA 0xD1D2220 `；selector ` 1 `；EOL ` RVA 0x33DB0D38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-057386

```text
(config)# do-exec clear ip http client cache session <string> <cr>
```

Handler ` RVA 0xD1D2220 `；selector ` 2 `；EOL ` RVA 0x33DB0AB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` session name。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [参数 P-ba614fcf6b2daaef](../../evidence/parameters-sets-014.md#p-ba614fcf6b2daaef) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-057360

```text
(config)# do-exec clear ip http client cache url <string> <cr>
```

Handler ` RVA 0xD1D2220 `；selector ` 3 `；EOL ` RVA 0x33DB07D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` url to clear。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [参数 P-04caf09ff1ffb9ea](../../evidence/parameters-sets-001.md#p-04caf09ff1ffb9ea) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-046027

```text
(config)# do-exec clear ip http client cookie <cr>
```

Handler ` RVA 0xD1D23A0 `；selector ` 4 `；EOL ` RVA 0x33DB1618 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-057410

```text
(config)# do-exec clear ip http client cookie domain <string> <cr>
```

Handler ` RVA 0xD1D23A0 `；selector ` 6 `；EOL ` RVA 0x33DB1370 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Client domain/host name。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [参数 P-7ddae15590050dbb](../../evidence/parameters-sets-010.md#p-7ddae15590050dbb) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-057442

```text
(config)# do-exec clear ip http client cookie name <string> <cr>
```

Handler ` RVA 0xD1D23A0 `；selector ` 7 `；EOL ` RVA 0x33DB1658 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Client cookie name。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [参数 P-70e3f6d6b140bc15](../../evidence/parameters-sets-009.md#p-70e3f6d6b140bc15) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-057382

```text
(config)# do-exec clear ip http client cookie session <string> <cr>
```

Handler ` RVA 0xD1D23A0 `；selector ` 5 `；EOL ` RVA 0x33DB1088 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Client session name。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [参数 P-7dc08f985880508a](../../evidence/parameters-sets-010.md#p-7dc08f985880508a) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-035442

```text
(config)# do-exec clear ip icmp rate-limit <cr>
```

Handler ` RVA 0xCFE5700 `；selector ` 0 `；EOL ` RVA 0x33D2B198 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d149a0ed9e1c68ff](../../evidence/conditions-sets-081.md#c-d149a0ed9e1c68ff) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061271

```text
(config)# do-exec clear ip icmp rate-limit <interface> <cr>
```

Handler ` RVA 0xCFE5700 `；selector ` 0 `；EOL ` RVA 0x33D2B198 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3111794780c8a45c](../../evidence/conditions-sets-019.md#c-3111794780c8a45c) · [缺口 G-2bbf7fbb07f399cb](../../evidence/gaps-sets-002.md#g-2bbf7fbb07f399cb) · [参数 P-b03239b6c3606417](../../evidence/parameters-sets-013.md#p-b03239b6c3606417) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-036843

```text
(config)# do-exec clear ip igmp group <cr>
```

Handler ` RVA 0xF6B26D0 `；selector ` 0 `；EOL ` RVA 0x34746DF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5b415668ee6ea98d](../../evidence/conditions-sets-036.md#c-5b415668ee6ea98d) · [状态效果 S-f4ea226de82d3f01](../../evidence/state_effects-sets-052.md#s-f4ea226de82d3f01)

### path-061364

```text
(config)# do-exec clear ip igmp group <interface> <cr>
```

Handler ` RVA 0xF6B26D0 `；selector ` 0 `；EOL ` RVA 0x34746DF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-27c56cb360c52e25](../../evidence/conditions-sets-016.md#c-27c56cb360c52e25) · [缺口 G-b30ec43a1c3b2e3e](../../evidence/gaps-sets-006.md#g-b30ec43a1c3b2e3e) · [参数 P-cece2de85eb2be27](../../evidence/parameters-sets-016.md#p-cece2de85eb2be27) · [状态效果 S-f4ea226de82d3f01](../../evidence/state_effects-sets-052.md#s-f4ea226de82d3f01)

### path-060832

```text
(config)# do-exec clear ip interface <interface> <cr>
```

Handler ` RVA 0xCF0E720 `；selector ` 0 `；EOL ` RVA 0x33D2C780 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-cd2fde57f28e4c2a](../../evidence/conditions-sets-079.md#c-cd2fde57f28e4c2a) · [缺口 G-da3907552e4d8118](../../evidence/gaps-sets-008.md#g-da3907552e4d8118) · [参数 P-19b41cc50ccf0878](../../evidence/parameters-sets-002.md#p-19b41cc50ccf0878) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061284

```text
(config)# do-exec clear ip interface <interface> stats <cr>
```

Handler ` RVA 0xCF38F80 `；selector ` 0 `；EOL ` RVA 0x33D2C758 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-cd2fde57f28e4c2a](../../evidence/conditions-sets-079.md#c-cd2fde57f28e4c2a) · [缺口 G-da3907552e4d8118](../../evidence/gaps-sets-008.md#g-da3907552e4d8118) · [参数 P-19b41cc50ccf0878](../../evidence/parameters-sets-002.md#p-19b41cc50ccf0878) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062262

```text
(config)# do-exec clear ip interface <interface> topology base stats <cr>
```

Handler ` RVA 0xCF38F10 `；selector ` 0 `；EOL ` RVA 0x33D2C3B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-cd2fde57f28e4c2a](../../evidence/conditions-sets-079.md#c-cd2fde57f28e4c2a) · [缺口 G-da3907552e4d8118](../../evidence/gaps-sets-008.md#g-da3907552e4d8118) · [参数 P-19b41cc50ccf0878](../../evidence/parameters-sets-002.md#p-19b41cc50ccf0878) · [状态效果 S-f673fc0bb27c8564](../../evidence/state_effects-sets-052.md#s-f673fc0bb27c8564)

### path-037126

```text
(config)# do-exec clear ip mfib counters <cr>
```

Handler ` RVA 0x1197D5A0 `；selector ` 0 `；EOL ` RVA 0x355B7700 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f808427ebefa84e5](../../evidence/conditions-sets-096.md#c-f808427ebefa84e5) · [状态效果 S-fc8035c43fd48805](../../evidence/state_effects-sets-053.md#s-fc8035c43fd48805)

### path-061391

```text
(config)# do-exec clear ip mfib counters <prefix:dynamic> <cr>
```

Handler ` RVA 0x1197D5A0 `；selector ` 0 `；EOL ` RVA 0x355B7700 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` Group IP address/prefix length。

[条件 C-dc5eff231fa38628](../../evidence/conditions-sets-085.md#c-dc5eff231fa38628) · [缺口 G-e0825a477ae95de3](../../evidence/gaps-sets-008.md#g-e0825a477ae95de3) · [参数 P-11932c0b949637f4](../../evidence/parameters-sets-002.md#p-11932c0b949637f4) · [状态效果 S-fc8035c43fd48805](../../evidence/state_effects-sets-053.md#s-fc8035c43fd48805)

### path-036748

```text
(config)# do-exec clear ip mrm status-report <cr>
```

Handler ` RVA 0xF672250 `；selector ` 0 `；EOL ` RVA 0x3471F308 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-060878

```text
(config)# do-exec clear ip mroute * <cr>
```

Handler ` RVA 0xF74EC90 `；selector ` 0 `；EOL ` RVA 0x347468B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a5a649a7fd4e196d](../../evidence/conditions-sets-064.md#c-a5a649a7fd4e196d) · [缺口 G-495214df7e16558b](../../evidence/gaps-sets-003.md#g-495214df7e16558b) · [状态效果 S-ff54670480e6287e](../../evidence/state_effects-sets-054.md#s-ff54670480e6287e)

### path-036752

```text
(config)# do-exec clear ip mroute <address> <cr>
```

Handler ` RVA 0xF74EC90 `；selector ` 0 `；EOL ` RVA 0x347468B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP name or group address。

[条件 C-be25b0dc514ae992](../../evidence/conditions-sets-073.md#c-be25b0dc514ae992) · [参数 P-5526640d1cbfc478](../../evidence/parameters-sets-007.md#p-5526640d1cbfc478) · [状态效果 S-69c61ab58bea54ca](../../evidence/state_effects-sets-023.md#s-69c61ab58bea54ca)

### path-045718

```text
(config)# do-exec clear ip msdp peer <address> <cr>
```

Handler ` RVA 0xF78ED70 `；selector ` 0 `；EOL ` RVA 0x34741B88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Peer name or address。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [参数 P-9f44f2d1408a3f5d](../../evidence/parameters-sets-012.md#p-9f44f2d1408a3f5d) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-036445

```text
(config)# do-exec clear ip msdp sa-cache <cr>
```

Handler ` RVA 0xF78EA70 `；selector ` 0 `；EOL ` RVA 0x34741E70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-036500

```text
(config)# do-exec clear ip msdp statistics <cr>
```

Handler ` RVA 0xF78EB10 `；selector ` 0 `；EOL ` RVA 0x34742130 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-036615

```text
(config)# do-exec clear ip multicast limit <cr>
```

Handler ` RVA 0xF777FE0 `；selector ` 0 `；EOL ` RVA 0x34746048 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d5aff361b478776d](../../evidence/conditions-sets-082.md#c-d5aff361b478776d) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061339

```text
(config)# do-exec clear ip multicast limit <interface> <cr>
```

Handler ` RVA 0xF777FE0 `；selector ` 0 `；EOL ` RVA 0x34746048 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a31a7ea3415a20c8](../../evidence/conditions-sets-063.md#c-a31a7ea3415a20c8) · [缺口 G-6c2dd868b4a31c65](../../evidence/gaps-sets-004.md#g-6c2dd868b4a31c65) · [参数 P-b0899c18c843ca25](../../evidence/parameters-sets-013.md#p-b0899c18c843ca25) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-046075

```text
(config)# do-exec clear ip multicast redundancy statistics <cr>
```

Handler ` RVA 0xD4712F0 `；selector ` 0 `；EOL ` RVA 0x33E525D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e51874697090e566](../../evidence/conditions-sets-088.md#c-e51874697090e566) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-036565

```text
(config)# do-exec clear ip multicast rsvp <cr>
```

Handler ` RVA 0xF6F1770 `；selector ` 0 `；EOL ` RVA 0x34745CC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e532f6e964361ea1](../../evidence/conditions-sets-088.md#c-e532f6e964361ea1) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061337

```text
(config)# do-exec clear ip multicast rsvp <interface> <cr>
```

Handler ` RVA 0xF6F1770 `；selector ` 0 `；EOL ` RVA 0x34745CC8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-34c3b07aa6c2cfcf](../../evidence/conditions-sets-021.md#c-34c3b07aa6c2cfcf) · [缺口 G-d22044241edd3608](../../evidence/gaps-sets-007.md#g-d22044241edd3608) · [参数 P-bb819926b72a1e7d](../../evidence/parameters-sets-014.md#p-bb819926b72a1e7d) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-059184

```text
(config)# do-exec clear ip multicast snooping limit vlan <number:1..4095> statistics <cr>
```

Handler ` RVA 0xC3568D0 `；selector ` 64 `；EOL ` RVA 0x33A5F240 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Vlan number。

[条件 C-e51874697090e566](../../evidence/conditions-sets-088.md#c-e51874697090e566) · [参数 P-85cbffd05ab530a5](../../evidence/parameters-sets-010.md#p-85cbffd05ab530a5) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-036771

```text
(config)# do-exec clear ip nat statistics <cr>
```

Handler ` RVA 0xFA0A1A0 `；selector ` 1 `；EOL ` RVA 0x347DD7F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061361

```text
(config)# do-exec clear ip nat translation * <cr>
```

Handler ` RVA 0xFA0A1A0 `；selector ` 0 `；EOL ` RVA 0x347DCB40 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c5d078692cf3caff](../../evidence/conditions-sets-076.md#c-c5d078692cf3caff) · [缺口 G-18ce86318758d554](../../evidence/gaps-sets-001.md#g-18ce86318758d554) · [状态效果 S-36bfb2c8bf153eaa](../../evidence/state_effects-sets-012.md#s-36bfb2c8bf153eaa)

### path-037084

```text
(config)# do-exec clear ip nat translation <cr>
```

Handler ` RVA 0xFA0A1A0 `；selector ` 0 `；EOL ` RVA 0x347DCB40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a1cc54701c6ed739](../../evidence/conditions-sets-062.md#c-a1cc54701c6ed739) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-030132

```text
(config)# do-exec clear ip nbar <cr>
```

Handler ` RVA 0x10F3B120 `；selector ` 2 `；EOL ` RVA 0x3527C770 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ce4cc5e5f2365570](../../evidence/conditions-sets-079.md#c-ce4cc5e5f2365570) · [状态效果 S-5f9b544c7c6aa3ec](../../evidence/state_effects-sets-021.md#s-5f9b544c7c6aa3ec)

### path-057414

```text
(config)# do-exec clear ip nbar classification auto-learn top-hosts restart <cr>
```

Handler ` RVA 0x10F3B120 `；selector ` 14 `；EOL ` RVA 0x3527B870 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a8d94fa5b85f8d8a](../../evidence/conditions-sets-065.md#c-a8d94fa5b85f8d8a) · [状态效果 S-475b3e1fb86ac19e](../../evidence/state_effects-sets-016.md#s-475b3e1fb86ac19e)

### path-057381

```text
(config)# do-exec clear ip nbar classification auto-learn top-hosts statistics <cr>
```

Handler ` RVA 0x10F3B120 `；selector ` 13 `；EOL ` RVA 0x3527B5C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a8d94fa5b85f8d8a](../../evidence/conditions-sets-065.md#c-a8d94fa5b85f8d8a) · [状态效果 S-475b3e1fb86ac19e](../../evidence/state_effects-sets-016.md#s-475b3e1fb86ac19e)

### path-053352

```text
(config)# do-exec clear ip nbar classification cache sync <cr>
```

Handler ` RVA 0x10F3B120 `；selector ` 12 `；EOL ` RVA 0x3527BBD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-5f9b544c7c6aa3ec](../../evidence/state_effects-sets-021.md#s-5f9b544c7c6aa3ec)

### path-057437

```text
(config)# do-exec clear ip nbar classification dns learning cache <cr>
```

Handler ` RVA 0x10F3B120 `；selector ` 47 `；EOL ` RVA 0x3527BF08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-5f9b544c7c6aa3ec](../../evidence/state_effects-sets-021.md#s-5f9b544c7c6aa3ec)

### path-057470

```text
(config)# do-exec clear ip nbar classification dns learning statistics <cr>
```

Handler ` RVA 0x10F3B120 `；selector ` 49 `；EOL ` RVA 0x3527C1B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-5f9b544c7c6aa3ec](../../evidence/state_effects-sets-021.md#s-5f9b544c7c6aa3ec)

### path-046006

```text
(config)# do-exec clear ip nbar classification socket-cache <cr>
```

Handler ` RVA 0x10F3B120 `；selector ` 48 `；EOL ` RVA 0x3527C458 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-5f9b544c7c6aa3ec](../../evidence/state_effects-sets-021.md#s-5f9b544c7c6aa3ec)

### path-036505

```text
(config)# do-exec clear ip nbar protocol-discovery <cr>
```

Handler ` RVA 0x10F3B120 `；selector ` 34 `；EOL ` RVA 0x3527B048 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cd1aff9592498208](../../evidence/conditions-sets-079.md#c-cd1aff9592498208) · [状态效果 S-5f9b544c7c6aa3ec](../../evidence/state_effects-sets-021.md#s-5f9b544c7c6aa3ec)

### path-061918

```text
(config)# do-exec clear ip nbar protocol-discovery interface <interface> <cr>
```

Handler ` RVA 0x10F3B120 `；selector ` 34 `；EOL ` RVA 0x3527B048 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e5a54bc1c7acd30d](../../evidence/conditions-sets-089.md#c-e5a54bc1c7acd30d) · [缺口 G-e67ae6b4785de5f9](../../evidence/gaps-sets-008.md#g-e67ae6b4785de5f9) · [参数 P-658f99059c5e7bb6](../../evidence/parameters-sets-008.md#p-658f99059c5e7bb6) · [状态效果 S-8c896bb071eb5c71](../../evidence/state_effects-sets-030.md#s-8c896bb071eb5c71)

### path-036545

```text
(config)# do-exec clear ip nbar statistics <cr>
```

Handler ` RVA 0x10F3B120 `；selector ` 7 `；EOL ` RVA 0x3527C748 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-71e0524c2117ffd7](../../evidence/conditions-sets-044.md#c-71e0524c2117ffd7) · [状态效果 S-5f9b544c7c6aa3ec](../../evidence/state_effects-sets-021.md#s-5f9b544c7c6aa3ec)

### path-030495

```text
(config)# do-exec clear ip nhrp <cr>
```

Handler ` RVA 0xFAB4540 `；selector ` 0 `；EOL ` RVA 0x347F2628 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-27b8c2ad606f4640](../../evidence/conditions-sets-016.md#c-27b8c2ad606f4640) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-060895

```text
(config)# do-exec clear ip nhrp <interface> <cr>
```

Handler ` RVA 0xFAB4540 `；selector ` 0 `；EOL ` RVA 0x347F2628 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4578caff42a4225e](../../evidence/conditions-sets-027.md#c-4578caff42a4225e) · [缺口 G-33f69aa2e0415a4e](../../evidence/gaps-sets-002.md#g-33f69aa2e0415a4e) · [参数 P-57d8892cc9e461c1](../../evidence/parameters-sets-007.md#p-57d8892cc9e461c1) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-037073

```text
(config)# do-exec clear ip nhrp counters <cr>
```

Handler ` RVA 0xFAB4540 `；selector ` 1 `；EOL ` RVA 0x347F29F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-27b8c2ad606f4640](../../evidence/conditions-sets-016.md#c-27b8c2ad606f4640) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061969

```text
(config)# do-exec clear ip nhrp rd <?vrf_rd_action@555589d53098> counters <cr>
```

Handler ` RVA 0xFAB4540 `；selector ` 1 `；EOL ` RVA 0x347F29F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-27b8c2ad606f4640](../../evidence/conditions-sets-016.md#c-27b8c2ad606f4640) · [缺口 G-51e631aacf68fac1](../../evidence/gaps-sets-003.md#g-51e631aacf68fac1) · [状态效果 S-bda247a3aaeaa120](../../evidence/state_effects-sets-040.md#s-bda247a3aaeaa120)

### path-061958

```text
(config)# do-exec clear ip nhrp rd <?vrf_rd_action@555589d53098> shortcut <cr>
```

Handler ` RVA 0x108FE760 `；selector ` 0 `；EOL ` RVA 0x34BF9228 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [缺口 G-51e631aacf68fac1](../../evidence/gaps-sets-003.md#g-51e631aacf68fac1) · [状态效果 S-24ca7ae3fa502379](../../evidence/state_effects-sets-008.md#s-24ca7ae3fa502379)

### path-036987

```text
(config)# do-exec clear ip nhrp shortcut <cr>
```

Handler ` RVA 0x108FE760 `；selector ` 0 `；EOL ` RVA 0x34BF9228 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-510c8b3fd9f29aed](../../evidence/state_effects-sets-018.md#s-510c8b3fd9f29aed)

### path-061962

```text
(config)# do-exec clear ip nhrp shortcut interface <interface> <cr>
```

Handler ` RVA 0x108FE760 `；selector ` 1 `；EOL ` RVA 0x34BF92E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-89de24f594f24842](../../evidence/conditions-sets-053.md#c-89de24f594f24842) · [缺口 G-32b151dc5831b823](../../evidence/gaps-sets-002.md#g-32b151dc5831b823) · [参数 P-b7cfd3b87c5b765b](../../evidence/parameters-sets-014.md#p-b7cfd3b87c5b765b) · [状态效果 S-510c8b3fd9f29aed](../../evidence/state_effects-sets-018.md#s-510c8b3fd9f29aed)

### path-037298

```text
(config)# do-exec clear ip nhrp stats <cr>
```

Handler ` RVA 0xFAB4540 `；selector ` 2 `；EOL ` RVA 0x347F2F38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-72d46b46a297f481](../../evidence/conditions-sets-044.md#c-72d46b46a297f481) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061403

```text
(config)# do-exec clear ip nhrp stats <interface> <cr>
```

Handler ` RVA 0xFAB4540 `；selector ` 2 `；EOL ` RVA 0x347F2F38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4fcdd9dc8429eb66](../../evidence/conditions-sets-031.md#c-4fcdd9dc8429eb66) · [缺口 G-e4b9cff4886156ea](../../evidence/gaps-sets-008.md#g-e4b9cff4886156ea) · [参数 P-e74517d0446cc71b](../../evidence/parameters-sets-017.md#p-e74517d0446cc71b) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-036944

```text
(config)# do-exec clear ip ospf counters <cr>
```

Handler ` RVA 0xFCD4210 `；selector ` 4 `；EOL ` RVA 0x348934D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061965

```text
(config)# do-exec clear ip ospf counters neighbor <interface> <cr>
```

Handler ` RVA 0xFCD4210 `；selector ` 4 `；EOL ` RVA 0x348934D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-da2519218a50006c](../../evidence/conditions-sets-084.md#c-da2519218a50006c) · [缺口 G-837337431b34fd9f](../../evidence/gaps-sets-005.md#g-837337431b34fd9f) · [参数 P-0b7950fbc7507d11](../../evidence/parameters-sets-001.md#p-0b7950fbc7507d11) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-036977

```text
(config)# do-exec clear ip ospf events <cr>
```

Handler ` RVA 0xFCD4210 `；selector ` 6 `；EOL ` RVA 0x34893FD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-036826

```text
(config)# do-exec clear ip ospf force-spf <cr>
```

Handler ` RVA 0xFCD4210 `；selector ` 0 `；EOL ` RVA 0x34892C50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-057646

```text
(config)# do-exec clear ip ospf lsa router <address> self <cr>
```

Handler ` RVA 0xFCD4210 `；selector ` 7 `；EOL ` RVA 0x34893A68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` OSPF LSID in IP address format。

[条件 C-a52f305b1c8c11f0](../../evidence/conditions-sets-064.md#c-a52f305b1c8c11f0) · [参数 P-4bb4f15a3e4f951b](../../evidence/parameters-sets-006.md#p-4bb4f15a3e4f951b) · [状态效果 S-b254d49f0fd97ee5](../../evidence/state_effects-sets-038.md#s-b254d49f0fd97ee5)

### path-046125

```text
(config)# do-exec clear ip ospf nsr statistics <cr>
```

Handler ` RVA 0xDACCB50 `；selector ` 20 `；EOL ` RVA 0x33FC88B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-46600f157bf4d49a](../../evidence/state_effects-sets-015.md#s-46600f157bf4d49a)

### path-036737

```text
(config)# do-exec clear ip ospf process <cr>
```

Handler ` RVA 0xFCD4210 `；selector ` 3 `；EOL ` RVA 0x34892700 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-036684

```text
(config)# do-exec clear ip ospf redistribution <cr>
```

Handler ` RVA 0xFCD4210 `；selector ` 2 `；EOL ` RVA 0x34892458 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-036780

```text
(config)# do-exec clear ip ospf rib <cr>
```

Handler ` RVA 0xFCD4210 `；selector ` 1 `；EOL ` RVA 0x348929A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-036994

```text
(config)# do-exec clear ip ospf traffic <cr>
```

Handler ` RVA 0xFCD4210 `；selector ` 5 `；EOL ` RVA 0x34893080 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9481ef008e1de97f](../../evidence/conditions-sets-057.md#c-9481ef008e1de97f) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061376

```text
(config)# do-exec clear ip ospf traffic <interface> <cr>
```

Handler ` RVA 0xFCD4210 `；selector ` 5 `；EOL ` RVA 0x34893080 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-735f8f7e1b78503b](../../evidence/conditions-sets-045.md#c-735f8f7e1b78503b) · [缺口 G-431fff5b8a95e318](../../evidence/gaps-sets-003.md#g-431fff5b8a95e318) · [参数 P-319be4011d545c98](../../evidence/parameters-sets-004.md#p-319be4011d545c98) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-036568

```text
(config)# do-exec clear ip pim df <cr>
```

Handler ` RVA 0xF7CB460 `；selector ` 0 `；EOL ` RVA 0x34771D68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e51874697090e566](../../evidence/conditions-sets-088.md#c-e51874697090e566) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061925

```text
(config)# do-exec clear ip pim df int <interface> <cr>
```

Handler ` RVA 0xF7CB460 `；selector ` 0 `；EOL ` RVA 0x34771D68 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d8f0012cbc17f852](../../evidence/conditions-sets-083.md#c-d8f0012cbc17f852) · [缺口 G-2bdaa88ba83e168d](../../evidence/gaps-sets-002.md#g-2bdaa88ba83e168d) · [参数 P-0b4926ba6b47454a](../../evidence/parameters-sets-001.md#p-0b4926ba6b47454a) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061922

```text
(config)# do-exec clear ip pim interface <interface> count <cr>
```

Handler ` RVA 0xF827030 `；selector ` 0 `；EOL ` RVA 0x34772140 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-50c72ad34e96f503](../../evidence/conditions-sets-032.md#c-50c72ad34e96f503) · [缺口 G-18a7425124d07066](../../evidence/gaps-sets-001.md#g-18a7425124d07066) · [参数 P-8e30251f47fbf72e](../../evidence/parameters-sets-011.md#p-8e30251f47fbf72e) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-046000

```text
(config)# do-exec clear ip pim interface count <cr>
```

Handler ` RVA 0xF827030 `；selector ` 0 `；EOL ` RVA 0x34772140 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d0cc604d16d7fbbd](../../evidence/conditions-sets-080.md#c-d0cc604d16d7fbbd) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-045996

```text
(config)# do-exec clear ip pim pfp-sa cache <cr>
```

Handler ` RVA 0xF8A2050 `；selector ` 0 `；EOL ` RVA 0x347726F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e51874697090e566](../../evidence/conditions-sets-088.md#c-e51874697090e566) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-045941

```text
(config)# do-exec clear ip pim pfp-sa originator <cr>
```

Handler ` RVA 0xF8A1FA0 `；selector ` 0 `；EOL ` RVA 0x34772450 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e51874697090e566](../../evidence/conditions-sets-088.md#c-e51874697090e566) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-036444

```text
(config)# do-exec clear ip pim rp-mapping <cr>
```

Handler ` RVA 0xF7BE560 `；selector ` 0 `；EOL ` RVA 0x34771918 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e51874697090e566](../../evidence/conditions-sets-088.md#c-e51874697090e566) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-030490

```text
(config)# do-exec clear ip prefix-list <cr>
```

Handler ` RVA 0xE21FCB0 `；selector ` 0 `；EOL ` RVA 0x34283CA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-8e04a3bf7f2727bb](../../evidence/state_effects-sets-030.md#s-8e04a3bf7f2727bb)

### path-061397

```text
(config)# do-exec clear ip prefix-list <string> <prefix:dynamic> <cr>
```

Handler ` RVA 0xE21FCB0 `；selector ` 0 `；EOL ` RVA 0x34283CA8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Name of a prefix list；` prefix_dynamic ` IP prefix &lt;network&gt;/&lt;length&gt;, e.g., 35.0.0.0/8。

[条件 C-8f1563c46ae8536e](../../evidence/conditions-sets-055.md#c-8f1563c46ae8536e) · [缺口 G-38020f4eebb48e5c](../../evidence/gaps-sets-002.md#g-38020f4eebb48e5c) · [参数 P-bdd7072064224684](../../evidence/parameters-sets-014.md#p-bdd7072064224684) · [状态效果 S-7b4e218dfac3478c](../../evidence/state_effects-sets-026.md#s-7b4e218dfac3478c)

### path-029265

```text
(config)# do-exec clear ip redirect <cr>
```

Handler ` RVA 0xCF50BF0 `；selector ` 0 `；EOL ` RVA 0x33D2B468 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-c85ff84d905c4f10](../../evidence/state_effects-sets-042.md#s-c85ff84d905c4f10)

### path-060899

```text
(config)# do-exec clear ip reflexive-list * <cr>
```

Handler ` RVA 0xCEFCA00 `；selector ` 0 `；EOL ` RVA 0x3479AD88 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-568954e5deec973e](../../evidence/conditions-sets-034.md#c-568954e5deec973e) · [缺口 G-1ed2d3717e2e43f4](../../evidence/gaps-sets-002.md#g-1ed2d3717e2e43f4) · [状态效果 S-942c1ca0b21f62f4](../../evidence/state_effects-sets-031.md#s-942c1ca0b21f62f4)

### path-037192

```text
(config)# do-exec clear ip reflexive-list <string> <cr>
```

Handler ` RVA 0xCEFCA00 `；selector ` 0 `；EOL ` RVA 0x3479AD88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Delete a specific reflexive ACL。

[条件 C-94a4629f79b58d64](../../evidence/conditions-sets-057.md#c-94a4629f79b58d64) · [参数 P-afb5c6d87d9e8de3](../../evidence/parameters-sets-013.md#p-afb5c6d87d9e8de3) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-060864

```text
(config)# do-exec clear ip route * <cr>
```

Handler ` RVA 0xE1F84C0 `；selector ` 1 `；EOL ` RVA 0x3422DF58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6bb539a09ceb869c](../../evidence/conditions-sets-042.md#c-6bb539a09ceb869c) · [缺口 G-e12c79afb36e567d](../../evidence/gaps-sets-008.md#g-e12c79afb36e567d) · [状态效果 S-b7c8ebb57fee9b3c](../../evidence/state_effects-sets-039.md#s-b7c8ebb57fee9b3c)

### path-036392

```text
(config)# do-exec clear ip route <address> <cr>
```

Handler ` RVA 0xE1F84C0 `；selector ` 1 `；EOL ` RVA 0x3422DF58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Destination network route to delete。

[条件 C-3ef1add5b3f1b32e](../../evidence/conditions-sets-024.md#c-3ef1add5b3f1b32e) · [参数 P-a606ea51f9247878](../../evidence/parameters-sets-013.md#p-a606ea51f9247878) · [状态效果 S-5ef6ed12350aeecf](../../evidence/state_effects-sets-020.md#s-5ef6ed12350aeecf)

### path-045722

```text
(config)# do-exec clear ip route dhcp <address> <cr>
```

Handler ` RVA 0xE1F84C0 `；selector ` 2 `；EOL ` RVA 0x3422E240 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Destination host route to delete。

[条件 C-3ef1add5b3f1b32e](../../evidence/conditions-sets-024.md#c-3ef1add5b3f1b32e) · [参数 P-f4e189f9e5e93c08](../../evidence/parameters-sets-018.md#p-f4e189f9e5e93c08) · [状态效果 S-b7c8ebb57fee9b3c](../../evidence/state_effects-sets-039.md#s-b7c8ebb57fee9b3c)

### path-061340

```text
(config)# do-exec clear ip route download * <cr>
```

Handler ` RVA 0xCF9ADF0 `；selector ` 1 `；EOL ` RVA 0x3422E620 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-acee0e6304f23184](../../evidence/conditions-sets-067.md#c-acee0e6304f23184) · [缺口 G-eaeda2c32a5e0a29](../../evidence/gaps-sets-008.md#g-eaeda2c32a5e0a29) · [状态效果 S-b7c8ebb57fee9b3c](../../evidence/state_effects-sets-039.md#s-b7c8ebb57fee9b3c)

### path-053405

```text
(config)# do-exec clear ip route download <address> <address> <cr>
```

Handler ` RVA 0xCF9ADF0 `；selector ` 1 `；EOL ` RVA 0x3422E620 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Destination network route to delete；` address ` Destination network mask。

[条件 C-3c5166292a75cfac](../../evidence/conditions-sets-023.md#c-3c5166292a75cfac) · [参数 P-405fcd062cfd9eeb](../../evidence/parameters-sets-005.md#p-405fcd062cfd9eeb) · [状态效果 S-572c0cd356db8a04](../../evidence/state_effects-sets-019.md#s-572c0cd356db8a04)

### path-046002

```text
(config)# do-exec clear ip route download reload <cr>
```

Handler ` RVA 0xCF9ADF0 `；selector ` 2 `；EOL ` RVA 0x3422E8E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3c5166292a75cfac](../../evidence/conditions-sets-023.md#c-3c5166292a75cfac) · [状态效果 S-b7c8ebb57fee9b3c](../../evidence/state_effects-sets-039.md#s-b7c8ebb57fee9b3c)

### path-037212

```text
(config)# do-exec clear ip rsvp authentication <cr>
```

Handler ` RVA 0x100741B0 `；selector ` 0 `；EOL ` RVA 0x34A3D340 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fb980b4a4b3feec7](../../evidence/conditions-sets-097.md#c-fb980b4a4b3feec7) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-036969

```text
(config)# do-exec clear ip rsvp counters <cr>
```

Handler ` RVA 0x100B7230 `；selector ` 0 `；EOL ` RVA 0x34A3B830 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fb980b4a4b3feec7](../../evidence/conditions-sets-097.md#c-fb980b4a4b3feec7) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-053886

```text
(config)# do-exec clear ip rsvp hello bfd lost-cnt <cr>
```

Handler ` RVA 0x10074420 `；selector ` 0 `；EOL ` RVA 0x34A3C3D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fb980b4a4b3feec7](../../evidence/conditions-sets-097.md#c-fb980b4a4b3feec7) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-053951

```text
(config)# do-exec clear ip rsvp hello bfd nbr-lost <cr>
```

Handler ` RVA 0x100744C0 `；selector ` 0 `；EOL ` RVA 0x34A3C678 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fb980b4a4b3feec7](../../evidence/conditions-sets-097.md#c-fb980b4a4b3feec7) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-053901

```text
(config)# do-exec clear ip rsvp hello instance counters <cr>
```

Handler ` RVA 0x1006F1F0 `；selector ` 0 `；EOL ` RVA 0x34A3C0F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fb980b4a4b3feec7](../../evidence/conditions-sets-097.md#c-fb980b4a4b3feec7) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-053839

```text
(config)# do-exec clear ip rsvp hello instance statistics <cr>
```

Handler ` RVA 0x1006F240 `；selector ` 0 `；EOL ` RVA 0x34A3BE50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fb980b4a4b3feec7](../../evidence/conditions-sets-097.md#c-fb980b4a4b3feec7) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-046431

```text
(config)# do-exec clear ip rsvp hello statistics <cr>
```

Handler ` RVA 0x1006F290 `；selector ` 0 `；EOL ` RVA 0x34A3BB40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fb980b4a4b3feec7](../../evidence/conditions-sets-097.md#c-fb980b4a4b3feec7) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-046583

```text
(config)# do-exec clear ip rsvp metadata interface <cr>
```

Handler ` RVA 0x10078C10 `；selector ` 0 `；EOL ` RVA 0x34A3D630 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-577970e4f2d7b997](../../evidence/conditions-sets-034.md#c-577970e4f2d7b997) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-046275

```text
(config)# do-exec clear ip rsvp nsr counters <cr>
```

Handler ` RVA 0x100B71E0 `；selector ` 0 `；EOL ` RVA 0x34A3AB20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-628bdccceb1356de](../../evidence/conditions-sets-038.md#c-628bdccceb1356de) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061380

```text
(config)# do-exec clear ip rsvp reservation * <cr>
```

Handler ` RVA 0x1006F000 `；selector ` 0 `；EOL ` RVA 0x34A3B4F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9dd1f0a8dcfc4a0e](../../evidence/conditions-sets-061.md#c-9dd1f0a8dcfc4a0e) · [缺口 G-6a53b8077a48b93b](../../evidence/gaps-sets-004.md#g-6a53b8077a48b93b) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-059807

```text
(config)# do-exec clear ip rsvp reservation <address> <address> <number:0..255> <number:0..65535> <number:0..65535> <cr>
```

Handler ` RVA 0x1006F000 `；selector ` 0 `；EOL ` RVA 0x34A3B4F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Destination address；` address ` Source address；` unsigned_number ` IP Protocol；` unsigned_number ` Destination port；` unsigned_number ` Source port。

[条件 C-fb980b4a4b3feec7](../../evidence/conditions-sets-097.md#c-fb980b4a4b3feec7) · [参数 P-bca9d63baab5c636](../../evidence/parameters-sets-014.md#p-bca9d63baab5c636) · [状态效果 S-154158a1620ee27c](../../evidence/state_effects-sets-005.md#s-154158a1620ee27c)

### path-061375

```text
(config)# do-exec clear ip rsvp sender * <cr>
```

Handler ` RVA 0x1006ED80 `；selector ` 0 `；EOL ` RVA 0x34A3AFB0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f9d423e76dc0f78b](../../evidence/conditions-sets-096.md#c-f9d423e76dc0f78b) · [缺口 G-ea5c953c425fce52](../../evidence/gaps-sets-008.md#g-ea5c953c425fce52) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-059801

```text
(config)# do-exec clear ip rsvp sender <address> <address> <number:0..255> <number:0..65535> <number:0..65535> <cr>
```

Handler ` RVA 0x1006ED80 `；selector ` 0 `；EOL ` RVA 0x34A3AFB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Destination address；` address ` Source address；` unsigned_number ` IP Protocol；` unsigned_number ` Destination port；` unsigned_number ` Source port。

[条件 C-fb980b4a4b3feec7](../../evidence/conditions-sets-097.md#c-fb980b4a4b3feec7) · [参数 P-6ed41e2ffa47e5cc](../../evidence/parameters-sets-009.md#p-6ed41e2ffa47e5cc) · [状态效果 S-cd8c6b00ff554b01](../../evidence/state_effects-sets-044.md#s-cd8c6b00ff554b01)

### path-053837

```text
(config)# do-exec clear ip rsvp signalling fast-local-repair statistics <cr>
```

Handler ` RVA 0x100710E0 `；selector ` 0 `；EOL ` RVA 0x34A3CA08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fb980b4a4b3feec7](../../evidence/conditions-sets-097.md#c-fb980b4a4b3feec7) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-046541

```text
(config)# do-exec clear ip rsvp signalling rate-limit <cr>
```

Handler ` RVA 0x10070F70 `；selector ` 0 `；EOL ` RVA 0x34A3CC98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fb980b4a4b3feec7](../../evidence/conditions-sets-097.md#c-fb980b4a4b3feec7) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-053935

```text
(config)# do-exec clear ip rsvp signalling refresh reduction <cr>
```

Handler ` RVA 0x10071080 `；selector ` 0 `；EOL ` RVA 0x34A3CF80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fb980b4a4b3feec7](../../evidence/conditions-sets-097.md#c-fb980b4a4b3feec7) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-035913

```text
(config)# do-exec clear ip rtp header-compression <cr>
```

Handler ` RVA 0xD194840 `；selector ` 0 `；EOL ` RVA 0x33DAB158 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8acdee18c18ec765](../../evidence/conditions-sets-054.md#c-8acdee18c18ec765) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061294

```text
(config)# do-exec clear ip rtp header-compression <interface> <cr>
```

Handler ` RVA 0xD194840 `；selector ` 0 `；EOL ` RVA 0x33DAB158 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-02499ab4101a2767](../../evidence/conditions-sets-001.md#c-02499ab4101a2767) · [缺口 G-520989431460918e](../../evidence/gaps-sets-003.md#g-520989431460918e) · [参数 P-07185bcb23c38cd9](../../evidence/parameters-sets-001.md#p-07185bcb23c38cd9) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-036415

```text
(config)# do-exec clear ip sctp statistics <cr>
```

Handler ` RVA 0xCE6FD20 `；selector ` 0 `；EOL ` RVA 0x33D0AAF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-030095

```text
(config)# do-exec clear ip sdr <cr>
```

Handler ` RVA 0xF87F070 `；selector ` 0 `；EOL ` RVA 0x34745820 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4899a50427063fad](../../evidence/conditions-sets-028.md#c-4899a50427063fad) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-030618

```text
(config)# do-exec clear ip subscriber <cr>
```

Handler ` RVA 0x11A39570 `；selector ` 0 `；EOL ` RVA 0x355CE968 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-2795c63618f4c7fd](../../evidence/state_effects-sets-009.md#s-2795c63618f4c7fd)

### path-061400

```text
(config)# do-exec clear ip subscriber interface <interface> <cr>
```

Handler ` RVA 0x11A39570 `；selector ` 0 `；EOL ` RVA 0x355CE968 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-69aa98de0bee7e1f](../../evidence/conditions-sets-041.md#c-69aa98de0bee7e1f) · [缺口 G-7d59143d777c930e](../../evidence/gaps-sets-005.md#g-7d59143d777c930e) · [参数 P-33b34a65ae26950a](../../evidence/parameters-sets-004.md#p-33b34a65ae26950a) · [状态效果 S-5bbfafe534712111](../../evidence/state_effects-sets-020.md#s-5bbfafe534712111)

### path-061897

```text
(config)# do-exec clear ip tcp adjust stats <interface> <cr>
```

Handler ` RVA 0xCDEF970 `；selector ` 0 `；EOL ` RVA 0x33D015E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9389972ffd5e880f](../../evidence/conditions-sets-057.md#c-9389972ffd5e880f) · [缺口 G-4a9a6c36ea8070c6](../../evidence/gaps-sets-003.md#g-4a9a6c36ea8070c6) · [参数 P-46d97962b774ce4d](../../evidence/parameters-sets-006.md#p-46d97962b774ce4d) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-035984

```text
(config)# do-exec clear ip tcp header-compression <cr>
```

Handler ` RVA 0xD194AE0 `；selector ` 0 `；EOL ` RVA 0x33DABAE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e1f32afed43d6d4c](../../evidence/conditions-sets-087.md#c-e1f32afed43d6d4c) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061295

```text
(config)# do-exec clear ip tcp header-compression <interface> <cr>
```

Handler ` RVA 0xD194AE0 `；selector ` 0 `；EOL ` RVA 0x33DABAE8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1394012bedcc6731](../../evidence/conditions-sets-008.md#c-1394012bedcc6731) · [缺口 G-81461f499b3b41e5](../../evidence/gaps-sets-005.md#g-81461f499b3b41e5) · [参数 P-4d516fa8bc220d2a](../../evidence/parameters-sets-006.md#p-4d516fa8bc220d2a) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-029403

```text
(config)# do-exec clear ip traffic <cr>
```

Handler ` RVA 0xCECF5C0 `；selector ` 0 `；EOL ` RVA 0x33D2BBF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061281

```text
(config)# do-exec clear ip traffic interface <interface> <cr>
```

Handler ` RVA 0xCECF640 `；selector ` 0 `；EOL ` RVA 0x33D2BCB0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-68d526ee6d41196a](../../evidence/conditions-sets-041.md#c-68d526ee6d41196a) · [缺口 G-de4845ddf7589d6d](../../evidence/gaps-sets-008.md#g-de4845ddf7589d6d) · [参数 P-8ffb16f07f792337](../../evidence/parameters-sets-011.md#p-8ffb16f07f792337) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-045004

```text
(config)# do-exec clear ip traffic topology base <cr>
```

Handler ` RVA 0xCF0EE20 `；selector ` 0 `；EOL ` RVA 0x33D2B7F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-e790825817676cda](../../evidence/state_effects-sets-049.md#s-e790825817676cda)

### path-030348

```text
(config)# do-exec clear ip trigger-authentication <cr>
```

Handler ` RVA 0x10571410 `；selector ` 3 `；EOL ` RVA 0x34B5AEB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-029097

```text
(config)# do-exec clear ipam counts <cr>
```

Handler ` RVA 0xCEA9040 `；selector ` 0 `；EOL ` RVA 0x33D1BBC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-029147

```text
(config)# do-exec clear ipam queues <cr>
```

Handler ` RVA 0xCEA90F0 `；selector ` 0 `；EOL ` RVA 0x33D1BE68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-034344

```text
(config)# do-exec clear ipc statistics peak <cr>
```

Handler ` RVA 0xD3B9920 `；selector ` 0 `；EOL ` RVA 0x33E272C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-f54a001b5f6d2fdb](../../evidence/state_effects-sets-052.md#s-f54a001b5f6d2fdb)

### path-034238

```text
(config)# do-exec clear ipc statistics queue <cr>
```

Handler ` RVA 0xD3B9F70 `；selector ` 0 `；EOL ` RVA 0x33E26F40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-034353

```text
(config)# do-exec clear ipc statistics zone <cr>
```

Handler ` RVA 0xD3B9FC0 `；selector ` 0 `；EOL ` RVA 0x33E27570 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-030511

```text
(config)# do-exec clear ipv6 access-list <cr>
```

Handler ` RVA 0x1217F700 `；selector ` 0 `；EOL ` RVA 0x357B0A00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061413

```text
(config)# do-exec clear ipv6 cef * prefix-statistics <cr>
```

Handler ` RVA 0xB684240 `；selector ` 0 `；EOL ` RVA 0x337D8618 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-13f828a712964dd2](../../evidence/conditions-sets-008.md#c-13f828a712964dd2) · [缺口 G-44c4f63f24035649](../../evidence/gaps-sets-003.md#g-44c4f63f24035649) · [状态效果 S-84de54d4147ec735](../../evidence/state_effects-sets-028.md#s-84de54d4147ec735)

### path-037490

```text
(config)# do-exec clear ipv6 cef prefix-statistics <cr>
```

Handler ` RVA 0xB684240 `；selector ` 0 `；EOL ` RVA 0x337D8618 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a9b9f48e3754b1f2](../../evidence/conditions-sets-065.md#c-a9b9f48e3754b1f2) · [状态效果 S-84de54d4147ec735](../../evidence/state_effects-sets-028.md#s-84de54d4147ec735)

### path-061405

```text
(config)# do-exec clear ipv6 dhcp binding * <cr>
```

Handler ` RVA 0x121D09B0 `；selector ` 1 `；EOL ` RVA 0x357C7E60 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d935785382a01a4f](../../evidence/conditions-sets-084.md#c-d935785382a01a4f) · [缺口 G-94b8dce15365eade](../../evidence/gaps-sets-005.md#g-94b8dce15365eade) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-046684

```text
(config)# do-exec clear ipv6 dhcp binding <address> <cr>
```

Handler ` RVA 0x121D09B0 `；selector ` 0 `；EOL ` RVA 0x357C7BB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Client IPv6 address。

[条件 C-b71caea3e07a6894](../../evidence/conditions-sets-071.md#c-b71caea3e07a6894) · [参数 P-5cdfea9b76c9ff77](../../evidence/parameters-sets-007.md#p-5cdfea9b76c9ff77) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061398

```text
(config)# do-exec clear ipv6 dhcp client <interface> <cr>
```

Handler ` RVA 0x1218E110 `；selector ` 0 `；EOL ` RVA 0x357BCBE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-aa16c25d8ba40f52](../../evidence/conditions-sets-066.md#c-aa16c25d8ba40f52) · [缺口 G-84e1a9b82384ab83](../../evidence/gaps-sets-005.md#g-84e1a9b82384ab83) · [参数 P-74b5cb6e7c4f1ffc](../../evidence/parameters-sets-009.md#p-74b5cb6e7c4f1ffc) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061408

```text
(config)# do-exec clear ipv6 dhcp conflict * <cr>
```

Handler ` RVA 0x121D09B0 `；selector ` 2 `；EOL ` RVA 0x357C85C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-15489695f46bff7b](../../evidence/conditions-sets-008.md#c-15489695f46bff7b) · [缺口 G-39f010dcf0f72ffd](../../evidence/gaps-sets-003.md#g-39f010dcf0f72ffd) · [状态效果 S-216c0d40167cf0b5](../../evidence/state_effects-sets-008.md#s-216c0d40167cf0b5)

### path-046764

```text
(config)# do-exec clear ipv6 dhcp conflict <address> <cr>
```

Handler ` RVA 0x121D09B0 `；selector ` 2 `；EOL ` RVA 0x357C85C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IPv6 address。

[条件 C-b71caea3e07a6894](../../evidence/conditions-sets-071.md#c-b71caea3e07a6894) · [参数 P-88dca45322fc40b3](../../evidence/parameters-sets-011.md#p-88dca45322fc40b3) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-054041

```text
(config)# do-exec clear ipv6 dhcp relay binding <address> <cr>
```

Handler ` RVA 0x121B39B0 `；selector ` 1 `；EOL ` RVA 0x357C37A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IPv6 Address。

[条件 C-b71caea3e07a6894](../../evidence/conditions-sets-071.md#c-b71caea3e07a6894) · [参数 P-2ed5ae9a7eacd364](../../evidence/parameters-sets-004.md#p-2ed5ae9a7eacd364) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061980

```text
(config)# do-exec clear ipv6 dhcp relay binding <prefix:dynamic> <cr>
```

Handler ` RVA 0x121B39B0 `；selector ` 1 `；EOL ` RVA 0x357C37A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` IPv6 prefix。

[条件 C-a8f0b3b5acbbce4c](../../evidence/conditions-sets-065.md#c-a8f0b3b5acbbce4c) · [缺口 G-96ea5342fb960fc8](../../evidence/gaps-sets-006.md#g-96ea5342fb960fc8) · [参数 P-a4b153b90a9010cc](../../evidence/parameters-sets-013.md#p-a4b153b90a9010cc) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-046770

```text
(config)# do-exec clear ipv6 dhcp route <address> <cr>
```

Handler ` RVA 0x121D09B0 `；selector ` 3 `；EOL ` RVA 0x357C81E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IPv6 Address。

[条件 C-b71caea3e07a6894](../../evidence/conditions-sets-071.md#c-b71caea3e07a6894) · [参数 P-ed6dcf58eee13906](../../evidence/parameters-sets-018.md#p-ed6dcf58eee13906) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061404

```text
(config)# do-exec clear ipv6 dhcp route <prefix:dynamic> <cr>
```

Handler ` RVA 0x121D09B0 `；selector ` 3 `；EOL ` RVA 0x357C81E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` IPv6 prefix。

[条件 C-e8f84beaf23fc9d9](../../evidence/conditions-sets-090.md#c-e8f84beaf23fc9d9) · [缺口 G-04bafa440cde4d98](../../evidence/gaps-sets-001.md#g-04bafa440cde4d98) · [参数 P-8b10ab131c9c5799](../../evidence/parameters-sets-011.md#p-8b10ab131c9c5799) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-037023

```text
(config)# do-exec clear ipv6 eigrp events <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 71 `；EOL ` RVA 0x354657B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-2e7c1dcc1caf04a9](../../evidence/state_effects-sets-010.md#s-2e7c1dcc1caf04a9)

### path-036972

```text
(config)# do-exec clear ipv6 eigrp logging <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 72 `；EOL ` RVA 0x35465510 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-2e7c1dcc1caf04a9](../../evidence/state_effects-sets-010.md#s-2e7c1dcc1caf04a9)

### path-037135

```text
(config)# do-exec clear ipv6 eigrp neighbors <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 67 `；EOL ` RVA 0x35465198 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-47d7b69e2f177ee8](../../evidence/conditions-sets-028.md#c-47d7b69e2f177ee8) · [状态效果 S-2e7c1dcc1caf04a9](../../evidence/state_effects-sets-010.md#s-2e7c1dcc1caf04a9)

### path-061395

```text
(config)# do-exec clear ipv6 eigrp neighbors <interface> <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 67 `；EOL ` RVA 0x35465198 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b05743b01347dae0](../../evidence/conditions-sets-068.md#c-b05743b01347dae0) · [缺口 G-eba222ee5e5e691b](../../evidence/gaps-sets-008.md#g-eba222ee5e5e691b) · [参数 P-6df9891e35afd1f3](../../evidence/parameters-sets-009.md#p-6df9891e35afd1f3) · [状态效果 S-2e7c1dcc1caf04a9](../../evidence/state_effects-sets-010.md#s-2e7c1dcc1caf04a9)

### path-061372

```text
(config)# do-exec clear ipv6 eigrp topology <prefix:dynamic> <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 68 `；EOL ` RVA 0x35464E48 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` Network to clear from topology。

[条件 C-b6bf43ad18af4779](../../evidence/conditions-sets-071.md#c-b6bf43ad18af4779) · [缺口 G-c18db4825ec0cb8a](../../evidence/gaps-sets-007.md#g-c18db4825ec0cb8a) · [参数 P-9eb1694add2ac22d](../../evidence/parameters-sets-012.md#p-9eb1694add2ac22d) · [状态效果 S-2e7c1dcc1caf04a9](../../evidence/state_effects-sets-010.md#s-2e7c1dcc1caf04a9)

### path-029875

```text
(config)# do-exec clear ipv6 errors-internal <cr>
```

Handler ` RVA 0x12304FE0 `；selector ` 0 `；EOL ` RVA 0x357E36C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4454cce5585dae44](../../evidence/conditions-sets-027.md#c-4454cce5585dae44) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-036909

```text
(config)# do-exec clear ipv6 mfib counters <cr>
```

Handler ` RVA 0x1197D5A0 `；selector ` 0 `；EOL ` RVA 0x355BC008 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1a9cce6ac4cd81e3](../../evidence/conditions-sets-010.md#c-1a9cce6ac4cd81e3) · [状态效果 S-f137dd2cccadd4ee](../../evidence/state_effects-sets-051.md#s-f137dd2cccadd4ee)

### path-061369

```text
(config)# do-exec clear ipv6 mfib counters <prefix:dynamic> <cr>
```

Handler ` RVA 0x1197D5A0 `；selector ` 0 `；EOL ` RVA 0x355BC008 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` Group IP address/prefix length。

[条件 C-e33a909abf8b3b08](../../evidence/conditions-sets-088.md#c-e33a909abf8b3b08) · [缺口 G-270acc6c8840f4ad](../../evidence/gaps-sets-002.md#g-270acc6c8840f4ad) · [参数 P-cbb064ebf7a5a915](../../evidence/parameters-sets-015.md#p-cbb064ebf7a5a915) · [状态效果 S-f137dd2cccadd4ee](../../evidence/state_effects-sets-051.md#s-f137dd2cccadd4ee)

### path-046318

```text
(config)# do-exec clear ipv6 mld all-vrfs traffic <cr>
```

Handler ` RVA 0x115D9690 `；selector ` 2 `；EOL ` RVA 0x3554C180 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-34b717c56dbdfb70](../../evidence/conditions-sets-020.md#c-34b717c56dbdfb70) · [状态效果 S-603b04351bd004b7](../../evidence/state_effects-sets-021.md#s-603b04351bd004b7)

### path-037034

```text
(config)# do-exec clear ipv6 mld counters <cr>
```

Handler ` RVA 0x115D9690 `；selector ` 3 `；EOL ` RVA 0x3554B900 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2b6b77bb1f2c1093](../../evidence/conditions-sets-017.md#c-2b6b77bb1f2c1093) · [状态效果 S-603b04351bd004b7](../../evidence/state_effects-sets-021.md#s-603b04351bd004b7)

### path-061381

```text
(config)# do-exec clear ipv6 mld counters <interface> <cr>
```

Handler ` RVA 0x115D9690 `；selector ` 3 `；EOL ` RVA 0x3554B900 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-930bdce311dc7dff](../../evidence/conditions-sets-057.md#c-930bdce311dc7dff) · [缺口 G-7e5f9cf995c2bc85](../../evidence/gaps-sets-005.md#g-7e5f9cf995c2bc85) · [参数 P-08793236fd68f92b](../../evidence/parameters-sets-001.md#p-08793236fd68f92b) · [状态效果 S-603b04351bd004b7](../../evidence/state_effects-sets-021.md#s-603b04351bd004b7)

### path-037176

```text
(config)# do-exec clear ipv6 mld group <cr>
```

Handler ` RVA 0x115D9690 `；selector ` 4 `；EOL ` RVA 0x3554BD10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-76b249d987d749b4](../../evidence/conditions-sets-046.md#c-76b249d987d749b4) · [状态效果 S-603b04351bd004b7](../../evidence/state_effects-sets-021.md#s-603b04351bd004b7)

### path-061394

```text
(config)# do-exec clear ipv6 mld group <interface> <cr>
```

Handler ` RVA 0x115D9690 `；selector ` 4 `；EOL ` RVA 0x3554BD10 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6aaa734f48fc3bb7](../../evidence/conditions-sets-041.md#c-6aaa734f48fc3bb7) · [缺口 G-e4bca0b95e91bcdf](../../evidence/gaps-sets-008.md#g-e4bca0b95e91bcdf) · [参数 P-09b75738c6c26df6](../../evidence/parameters-sets-001.md#p-09b75738c6c26df6) · [状态效果 S-603b04351bd004b7](../../evidence/state_effects-sets-021.md#s-603b04351bd004b7)

### path-036895

```text
(config)# do-exec clear ipv6 mld traffic <cr>
```

Handler ` RVA 0x115D9690 `；selector ` 1 `；EOL ` RVA 0x3554B570 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a522572a98f7b12a](../../evidence/conditions-sets-064.md#c-a522572a98f7b12a) · [状态效果 S-603b04351bd004b7](../../evidence/state_effects-sets-021.md#s-603b04351bd004b7)

### path-030013

```text
(config)# do-exec clear ipv6 mtu <cr>
```

Handler ` RVA 0x123069A0 `；selector ` 0 `；EOL ` RVA 0x357E5B38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-046738

```text
(config)# do-exec clear ipv6 multicast aaa authorization <cr>
```

Handler ` RVA 0xC49F810 `；selector ` 1001 `；EOL ` RVA 0x35534C78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a73dfb09fd12da18](../../evidence/conditions-sets-065.md#c-a73dfb09fd12da18) · [状态效果 S-a4dab6bff452654b](../../evidence/state_effects-sets-035.md#s-a4dab6bff452654b)

### path-061983

```text
(config)# do-exec clear ipv6 multicast aaa authorization <interface> <cr>
```

Handler ` RVA 0xC49F810 `；selector ` 1001 `；EOL ` RVA 0x35534C78 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b30ca59499d47eb2](../../evidence/conditions-sets-069.md#c-b30ca59499d47eb2) · [缺口 G-c21c47c2d779d1ac](../../evidence/gaps-sets-007.md#g-c21c47c2d779d1ac) · [参数 P-4746d67646d2d098](../../evidence/parameters-sets-006.md#p-4746d67646d2d098) · [状态效果 S-a4dab6bff452654b](../../evidence/state_effects-sets-035.md#s-a4dab6bff452654b)

### path-059183

```text
(config)# do-exec clear ipv6 multicast snooping limit vlan <number:1..4095> statistics <cr>
```

Handler ` RVA 0xC3568D0 `；selector ` 65 `；EOL ` RVA 0x33A5F660 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Vlan number。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [参数 P-5b0920e26311c92a](../../evidence/parameters-sets-007.md#p-5b0920e26311c92a) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-036700

```text
(config)# do-exec clear ipv6 nd destination <cr>
```

Handler ` RVA 0x1231A7C0 `；selector ` 0 `；EOL ` RVA 0x358056A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061930

```text
(config)# do-exec clear ipv6 nd destination vrf <?match_ipv6_zoneinfo_action@55558ad59678> <cr>
```

Handler ` RVA 0x1231A7C0 `；selector ` 0 `；EOL ` RVA 0x358056A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [缺口 G-b4fcb38e7beb77b1](../../evidence/gaps-sets-006.md#g-b4fcb38e7beb77b1) · [状态效果 S-f73369f2669441bb](../../evidence/state_effects-sets-052.md#s-f73369f2669441bb)

### path-046055

```text
(config)# do-exec clear ipv6 nd on-link prefix <cr>
```

Handler ` RVA 0x1231A3B0 `；selector ` 0 `；EOL ` RVA 0x35805358 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062292

```text
(config)# do-exec clear ipv6 nd on-link prefix vrf <?match_ipv6_zoneinfo_action@55558ad59330> <cr>
```

Handler ` RVA 0x1231A3B0 `；selector ` 0 `；EOL ` RVA 0x35805358 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [缺口 G-63400b3535a3f92f](../../evidence/gaps-sets-004.md#g-63400b3535a3f92f) · [状态效果 S-653cfd725b43440a](../../evidence/state_effects-sets-022.md#s-653cfd725b43440a)

### path-036749

```text
(config)# do-exec clear ipv6 nd router <cr>
```

Handler ` RVA 0x1231A8D0 `；selector ` 0 `；EOL ` RVA 0x358059B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061934

```text
(config)# do-exec clear ipv6 nd router vrf <?match_ipv6_zoneinfo_action@55558ad59990> <cr>
```

Handler ` RVA 0x1231A8D0 `；selector ` 0 `；EOL ` RVA 0x358059B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [缺口 G-8d7bd407d827983d](../../evidence/gaps-sets-005.md#g-8d7bd407d827983d) · [状态效果 S-ca32d6a86317a13f](../../evidence/state_effects-sets-043.md#s-ca32d6a86317a13f)

### path-030333

```text
(config)# do-exec clear ipv6 neighbors <cr>
```

Handler ` RVA 0x12312B50 `；selector ` 0 `；EOL ` RVA 0x35802BD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4d41c4b0ffea9641](../../evidence/conditions-sets-030.md#c-4d41c4b0ffea9641) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-060891

```text
(config)# do-exec clear ipv6 neighbors <interface> <cr>
```

Handler ` RVA 0x12312B50 `；selector ` 0 `；EOL ` RVA 0x35802BD0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e1bbc3bd3547eaa1](../../evidence/conditions-sets-087.md#c-e1bbc3bd3547eaa1) · [缺口 G-9a728b0b548ae026](../../evidence/gaps-sets-006.md#g-9a728b0b548ae026) · [参数 P-7d2af92ebc55b15f](../../evidence/parameters-sets-010.md#p-7d2af92ebc55b15f) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062505

```text
(config)# do-exec clear ipv6 neighbors binding address <?ipv4orv6_addr_action@55558b14a808> policy <string> <cr>
```

Handler ` RVA 0x136806D0 `；selector ` 1020 `；EOL ` RVA 0x35BF63A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Snooping Policy name to be cleared。

[条件 C-1909215f3ec7ca4b](../../evidence/conditions-sets-010.md#c-1909215f3ec7ca4b) · [缺口 G-00879ee61bdd2c17](../../evidence/gaps-sets-001.md#g-00879ee61bdd2c17) · [参数 P-44ff88cb184b8e62](../../evidence/parameters-sets-006.md#p-44ff88cb184b8e62) · [状态效果 S-ff1b20033f0fb3f3](../../evidence/state_effects-sets-054.md#s-ff1b20033f0fb3f3)

### path-053669

```text
(config)# do-exec clear ipv6 neighbors binding policy <string> <cr>
```

Handler ` RVA 0x136806D0 `；selector ` 1020 `；EOL ` RVA 0x35BF63A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Snooping Policy name to be cleared。

[条件 C-1909215f3ec7ca4b](../../evidence/conditions-sets-010.md#c-1909215f3ec7ca4b) · [参数 P-44ff88cb184b8e62](../../evidence/parameters-sets-006.md#p-44ff88cb184b8e62) · [状态效果 S-e9d7d21078e17cb7](../../evidence/state_effects-sets-049.md#s-e9d7d21078e17cb7)

### path-046033

```text
(config)# do-exec clear ipv6 neighbors ha statistics <cr>
```

Handler ` RVA 0x12312A70 `；selector ` 0 `；EOL ` RVA 0x35803088 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-43cc9284dd448f7b](../../evidence/state_effects-sets-015.md#s-43cc9284dd448f7b)

### path-030549

```text
(config)# do-exec clear ipv6 nhrp <cr>
```

Handler ` RVA 0x1186E480 `；selector ` 0 `；EOL ` RVA 0x35575280 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b222251f03aeb996](../../evidence/conditions-sets-069.md#c-b222251f03aeb996) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-060894

```text
(config)# do-exec clear ipv6 nhrp <prefix:dynamic> <cr>
```

Handler ` RVA 0x1186E480 `；selector ` 0 `；EOL ` RVA 0x35575280 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` Destination IPv6 network/&lt;mask&gt; to delete。

[条件 C-4d7b53de13272ea4](../../evidence/conditions-sets-030.md#c-4d7b53de13272ea4) · [缺口 G-fac5b60ecfbdd49f](../../evidence/gaps-sets-009.md#g-fac5b60ecfbdd49f) · [参数 P-d9316301be003ea8](../../evidence/parameters-sets-016.md#p-d9316301be003ea8) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-037164

```text
(config)# do-exec clear ipv6 nhrp counters <cr>
```

Handler ` RVA 0x1186E480 `；selector ` 1 `；EOL ` RVA 0x35575678 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b222251f03aeb996](../../evidence/conditions-sets-069.md#c-b222251f03aeb996) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061976

```text
(config)# do-exec clear ipv6 nhrp rd <?vrf_rd_action@55558aaca110> counters <cr>
```

Handler ` RVA 0x1186E480 `；selector ` 1 `；EOL ` RVA 0x35575678 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b222251f03aeb996](../../evidence/conditions-sets-069.md#c-b222251f03aeb996) · [缺口 G-381336ef728d84ea](../../evidence/gaps-sets-002.md#g-381336ef728d84ea) · [状态效果 S-f05af4460bb41d77](../../evidence/state_effects-sets-051.md#s-f05af4460bb41d77)

### path-061978

```text
(config)# do-exec clear ipv6 nhrp rd <?vrf_rd_action@55558aaca110> shortcut <cr>
```

Handler ` RVA 0x1186E410 `；selector ` 0 `；EOL ` RVA 0x35575A68 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b222251f03aeb996](../../evidence/conditions-sets-069.md#c-b222251f03aeb996) · [缺口 G-381336ef728d84ea](../../evidence/gaps-sets-002.md#g-381336ef728d84ea) · [状态效果 S-9de9a953274ae888](../../evidence/state_effects-sets-034.md#s-9de9a953274ae888)

### path-037209

```text
(config)# do-exec clear ipv6 nhrp shortcut <cr>
```

Handler ` RVA 0x1186E410 `；selector ` 0 `；EOL ` RVA 0x35575A68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b222251f03aeb996](../../evidence/conditions-sets-069.md#c-b222251f03aeb996) · [状态效果 S-a1ebbff8b67a6ac9](../../evidence/state_effects-sets-034.md#s-a1ebbff8b67a6ac9)

### path-061981

```text
(config)# do-exec clear ipv6 nhrp shortcut interface <interface> <cr>
```

Handler ` RVA 0x1186E410 `；selector ` 1 `；EOL ` RVA 0x35575B28 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-92bfbcb343a8b7de](../../evidence/conditions-sets-057.md#c-92bfbcb343a8b7de) · [缺口 G-c5fc7ac98a963edd](../../evidence/gaps-sets-007.md#g-c5fc7ac98a963edd) · [参数 P-d4a6eade3c633d02](../../evidence/parameters-sets-016.md#p-d4a6eade3c633d02) · [状态效果 S-a1ebbff8b67a6ac9](../../evidence/state_effects-sets-034.md#s-a1ebbff8b67a6ac9)

### path-037081

```text
(config)# do-exec clear ipv6 nhrp stats <cr>
```

Handler ` RVA 0x1186E480 `；selector ` 2 `；EOL ` RVA 0x35574D98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-82b4309de47f4ee2](../../evidence/conditions-sets-051.md#c-82b4309de47f4ee2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061389

```text
(config)# do-exec clear ipv6 nhrp stats <interface> <cr>
```

Handler ` RVA 0x1186E480 `；selector ` 2 `；EOL ` RVA 0x35574D98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e471db3205e067e1](../../evidence/conditions-sets-088.md#c-e471db3205e067e1) · [缺口 G-ac81eddc6488eb96](../../evidence/gaps-sets-006.md#g-ac81eddc6488eb96) · [参数 P-03f7e4dfd6c1a52a](../../evidence/parameters-sets-001.md#p-03f7e4dfd6c1a52a) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-046377

```text
(config)# do-exec clear ipv6 pim all-vrfs traffic <cr>
```

Handler ` RVA 0x11725630 `；selector ` 3 `；EOL ` RVA 0x35563230 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-61aa384bdfdaf4b0](../../evidence/conditions-sets-038.md#c-61aa384bdfdaf4b0) · [状态效果 S-9345b542f0c81bc4](../../evidence/state_effects-sets-031.md#s-9345b542f0c81bc4)

### path-037128

```text
(config)# do-exec clear ipv6 pim limit <cr>
```

Handler ` RVA 0x11725630 `；selector ` 4 `；EOL ` RVA 0x355626C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c792dc2853bbd0dc](../../evidence/conditions-sets-077.md#c-c792dc2853bbd0dc) · [状态效果 S-9345b542f0c81bc4](../../evidence/state_effects-sets-031.md#s-9345b542f0c81bc4)

### path-061392

```text
(config)# do-exec clear ipv6 pim limit <interface> <cr>
```

Handler ` RVA 0x11725630 `；selector ` 4 `；EOL ` RVA 0x355626C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e86173650124f782](../../evidence/conditions-sets-090.md#c-e86173650124f782) · [缺口 G-020d550ca5fbeb59](../../evidence/gaps-sets-001.md#g-020d550ca5fbeb59) · [参数 P-3dc6e6d409058c49](../../evidence/parameters-sets-005.md#p-3dc6e6d409058c49) · [状态效果 S-9345b542f0c81bc4](../../evidence/state_effects-sets-031.md#s-9345b542f0c81bc4)

### path-046595

```text
(config)# do-exec clear ipv6 pim pfp-sa cache <cr>
```

Handler ` RVA 0x11725630 `；selector ` 6 `；EOL ` RVA 0x35562F18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3c123bc221e8796d](../../evidence/conditions-sets-023.md#c-3c123bc221e8796d) · [状态效果 S-9345b542f0c81bc4](../../evidence/state_effects-sets-031.md#s-9345b542f0c81bc4)

### path-046531

```text
(config)# do-exec clear ipv6 pim pfp-sa originator <cr>
```

Handler ` RVA 0x11725630 `；selector ` 5 `；EOL ` RVA 0x35562C70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3c123bc221e8796d](../../evidence/conditions-sets-023.md#c-3c123bc221e8796d) · [状态效果 S-9345b542f0c81bc4](../../evidence/state_effects-sets-031.md#s-9345b542f0c81bc4)

### path-036968

```text
(config)# do-exec clear ipv6 pim reset <cr>
```

Handler ` RVA 0x11725630 `；selector ` 1 `；EOL ` RVA 0x355622F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3c123bc221e8796d](../../evidence/conditions-sets-023.md#c-3c123bc221e8796d) · [状态效果 S-4b0561ef5fbe51a7](../../evidence/state_effects-sets-016.md#s-4b0561ef5fbe51a7)

### path-037061

```text
(config)# do-exec clear ipv6 pim traffic <cr>
```

Handler ` RVA 0x11725630 `；selector ` 2 `；EOL ` RVA 0x35562988 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3c123bc221e8796d](../../evidence/conditions-sets-023.md#c-3c123bc221e8796d) · [状态效果 S-9345b542f0c81bc4](../../evidence/state_effects-sets-031.md#s-9345b542f0c81bc4)

### path-030519

```text
(config)# do-exec clear ipv6 prefix-list <cr>
```

Handler ` RVA 0xE21FCB0 `；selector ` 0 `；EOL ` RVA 0x3557FB60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-7a94627137188ee4](../../evidence/state_effects-sets-026.md#s-7a94627137188ee4)

### path-061399

```text
(config)# do-exec clear ipv6 prefix-list <string> <prefix:dynamic> <cr>
```

Handler ` RVA 0xE21FCB0 `；selector ` 0 `；EOL ` RVA 0x3557FB60 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Name of a prefix list；` prefix_dynamic ` IPv6 prefix &lt;network&gt;/&lt;length&gt;。

[条件 C-49691a3adaf059d3](../../evidence/conditions-sets-029.md#c-49691a3adaf059d3) · [缺口 G-4ba0436f718ae24b](../../evidence/gaps-sets-003.md#g-4ba0436f718ae24b) · [参数 P-1578a0c17fd934b1](../../evidence/parameters-sets-002.md#p-1578a0c17fd934b1) · [状态效果 S-b7219c6eb92de736](../../evidence/state_effects-sets-039.md#s-b7219c6eb92de736)

### path-030417

```text
(config)# do-exec clear ipv6 rip <cr>
```

Handler ` RVA 0x118A6380 `；selector ` 0 `；EOL ` RVA 0x3557C770 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7a8b1a79f7ff80b2](../../evidence/conditions-sets-048.md#c-7a8b1a79f7ff80b2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-036597

```text
(config)# do-exec clear ipv6 route <address> <cr>
```

Handler ` RVA 0x123075A0 `；selector ` 0 `；EOL ` RVA 0x357EBFF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IPv6 address。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [参数 P-80c04b2fec363bf8](../../evidence/parameters-sets-010.md#p-80c04b2fec363bf8) · [状态效果 S-1ecbb88be8f88a02](../../evidence/state_effects-sets-007.md#s-1ecbb88be8f88a02)

### path-060876

```text
(config)# do-exec clear ipv6 route <prefix:dynamic> <cr>
```

Handler ` RVA 0x123075A0 `；selector ` 0 `；EOL ` RVA 0x357EBFF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` IPv6 prefix。

[条件 C-e43a22125ebed01c](../../evidence/conditions-sets-088.md#c-e43a22125ebed01c) · [缺口 G-4196481e1749dbda](../../evidence/gaps-sets-003.md#g-4196481e1749dbda) · [参数 P-3c82e1e161a38a01](../../evidence/parameters-sets-005.md#p-3c82e1e161a38a01) · [状态效果 S-1ecbb88be8f88a02](../../evidence/state_effects-sets-007.md#s-1ecbb88be8f88a02)

### path-037288

```text
(config)# do-exec clear ipv6 snooping counters <cr>
```

Handler ` RVA 0x13686600 `；selector ` 1023 `；EOL ` RVA 0x35BF5768 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a95c6c5f538488c4](../../evidence/conditions-sets-065.md#c-a95c6c5f538488c4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061985

```text
(config)# do-exec clear ipv6 snooping counters interface <interface> <cr>
```

Handler ` RVA 0x13686600 `；selector ` 1023 `；EOL ` RVA 0x35BF5768 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-743d92e86309b7da](../../evidence/conditions-sets-045.md#c-743d92e86309b7da) · [缺口 G-675bc2d06c05e4f4](../../evidence/gaps-sets-004.md#g-675bc2d06c05e4f4) · [参数 P-a39ed858776171dd](../../evidence/parameters-sets-012.md#p-a39ed858776171dd) · [状态效果 S-3142338fd44f2bd7](../../evidence/state_effects-sets-011.md#s-3142338fd44f2bd7)

### path-037276

```text
(config)# do-exec clear ipv6 snooping events <cr>
```

Handler ` RVA 0x13686600 `；selector ` 1021 `；EOL ` RVA 0x35BF5AE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a95c6c5f538488c4](../../evidence/conditions-sets-065.md#c-a95c6c5f538488c4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-037319

```text
(config)# do-exec clear ipv6 snooping messages <cr>
```

Handler ` RVA 0x13686600 `；selector ` 1022 `；EOL ` RVA 0x35BF5D88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a95c6c5f538488c4](../../evidence/conditions-sets-065.md#c-a95c6c5f538488c4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-030537

```text
(config)# do-exec clear ipv6 spd <cr>
```

Handler ` RVA 0x12328050 `；selector ` 0 `；EOL ` RVA 0x35810460 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-030158

```text
(config)# do-exec clear ipv6 traffic <cr>
```

Handler ` RVA 0x1231FC30 `；selector ` 0 `；EOL ` RVA 0x3580BA38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-036657

```text
(config)# do-exec clear ipv6 traffic interface <cr>
```

Handler ` RVA 0x1231FC30 `；selector ` 1 `；EOL ` RVA 0x3580BAF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-dde915198ac38d0d](../../evidence/conditions-sets-085.md#c-dde915198ac38d0d) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061345

```text
(config)# do-exec clear ipv6 traffic interface <interface> <cr>
```

Handler ` RVA 0x1231FC30 `；selector ` 1 `；EOL ` RVA 0x3580BAF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f96cf6ee3d5e8f61](../../evidence/conditions-sets-096.md#c-f96cf6ee3d5e8f61) · [缺口 G-5d08902e8cb32c7c](../../evidence/gaps-sets-004.md#g-5d08902e8cb32c7c) · [参数 P-16c5cb1c2a44ef9f](../../evidence/parameters-sets-002.md#p-16c5cb1c2a44ef9f) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-060672

```text
(config)# do-exec clear isis * <cr>
```

Handler ` RVA 0xFD360F0 `；selector ` 0 `；EOL ` RVA 0x34B6A818 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-342cc2d4b7e43ea2](../../evidence/conditions-sets-020.md#c-342cc2d4b7e43ea2) · [缺口 G-37bdd9a307ad1e35](../../evidence/gaps-sets-002.md#g-37bdd9a307ad1e35) · [状态效果 S-f8cf060d2d9ddf72](../../evidence/state_effects-sets-053.md#s-f8cf060d2d9ddf72)

### path-030812

```text
(config)# do-exec clear isis lsp-fast-flooding <cr>
```

Handler ` RVA 0xFD360F0 `；selector ` 0 `；EOL ` RVA 0x34B6ADC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-eb5ae5e4b711ad83](../../evidence/state_effects-sets-050.md#s-eb5ae5e4b711ad83)

### path-030762

```text
(config)# do-exec clear isis lspfull <cr>
```

Handler ` RVA 0xFD360F0 `；selector ` 0 `；EOL ` RVA 0x34B6A818 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-91a2edef4c148a7f](../../evidence/state_effects-sets-031.md#s-91a2edef4c148a7f)

### path-061452

```text
(config)# do-exec clear isis rib redistribution <prefix:dynamic> <cr>
```

Handler ` RVA 0xFD360F0 `；selector ` 0 `；EOL ` RVA 0x34B6ADC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` IPv6 network prefix/length。

[条件 C-c4a253e4c8591dd0](../../evidence/conditions-sets-076.md#c-c4a253e4c8591dd0) · [缺口 G-b01c98a96d8411b5](../../evidence/gaps-sets-006.md#g-b01c98a96d8411b5) · [参数 P-79fd22ce757395b4](../../evidence/parameters-sets-010.md#p-79fd22ce757395b4) · [状态效果 S-334bafce193975ad](../../evidence/state_effects-sets-011.md#s-334bafce193975ad)

### path-028873

```text
(config)# do-exec clear kerberos creds <cr>
```

Handler ` RVA 0xC3E3030 `；selector ` 6 `；EOL ` RVA 0x33A6B2A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-035017

```text
(config)# do-exec clear l2fib statistics all <cr>
```

Handler ` RVA 0xC7C4460 `；selector ` 0 `；EOL ` RVA 0x33AF8A00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061256

```text
(config)# do-exec clear l2fib statistics bridge-domain <number:dynamic> <cr>
```

Handler ` RVA 0xC7C4460 `；selector ` 1 `；EOL ` RVA 0x33AF8CE8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Bridge domain number。

[条件 C-3082e37aa83fe5bf](../../evidence/conditions-sets-019.md#c-3082e37aa83fe5bf) · [缺口 G-cf36885a0f7e8c56](../../evidence/gaps-sets-007.md#g-cf36885a0f7e8c56) · [参数 P-9ca55ea367a776a1](../../evidence/parameters-sets-012.md#p-9ca55ea367a776a1) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-031749

```text
(config)# do-exec clear l2protocol-forward counters <cr>
```

Handler ` RVA 0x15FDB140 `；selector ` 30 `；EOL ` RVA 0x35E8F288 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-dbb01e28bf8488ae](../../evidence/conditions-sets-085.md#c-dbb01e28bf8488ae) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-060990

```text
(config)# do-exec clear l2protocol-forward counters <interface> <cr>
```

Handler ` RVA 0x15FDB140 `；selector ` 30 `；EOL ` RVA 0x35E8F288 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-46c66e3259800158](../../evidence/conditions-sets-028.md#c-46c66e3259800158) · [缺口 G-dc44f70a919be517](../../evidence/gaps-sets-008.md#g-dc44f70a919be517) · [参数 P-b0ae730cfa206d20](../../evidence/parameters-sets-013.md#p-b0ae730cfa206d20) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-031727

```text
(config)# do-exec clear l2protocol-tunnel counters <cr>
```

Handler ` RVA 0x15FDB140 `；selector ` 15 `；EOL ` RVA 0x35E8EEB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-028407bd9bcef226](../../evidence/conditions-sets-001.md#c-028407bd9bcef226) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-060989

```text
(config)# do-exec clear l2protocol-tunnel counters <interface> <cr>
```

Handler ` RVA 0x15FDB140 `；selector ` 15 `；EOL ` RVA 0x35E8EEB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-230c93333ba95295](../../evidence/conditions-sets-014.md#c-230c93333ba95295) · [缺口 G-8b84156050bcda12](../../evidence/gaps-sets-005.md#g-8b84156050bcda12) · [参数 P-9fa8ac9e4b02d3ee](../../evidence/parameters-sets-012.md#p-9fa8ac9e4b02d3ee) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-045730

```text
(config)# do-exec clear l2rib counters client producers <cr>
```

Handler ` RVA 0x125685C0 `；selector ` 0 `；EOL ` RVA 0x358B4CD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7fd9dbe61bf3884a](../../evidence/conditions-sets-050.md#c-7fd9dbe61bf3884a) · [状态效果 S-8d41d9ec59e0794e](../../evidence/state_effects-sets-030.md#s-8d41d9ec59e0794e)

### path-045816

```text
(config)# do-exec clear l2rib test <string> msg-buffer <cr>
```

Handler ` RVA 0x125CDA60 `；selector ` 0 `；EOL ` RVA 0x358BF500 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Client name。

[条件 C-5e015be4c4cf5293](../../evidence/conditions-sets-037.md#c-5e015be4c4cf5293) · [参数 P-6491247b4d38c173](../../evidence/parameters-sets-008.md#p-6491247b4d38c173) · [状态效果 S-132e73f9f45408b6](../../evidence/state_effects-sets-004.md#s-132e73f9f45408b6)

### path-060992

```text
(config)# do-exec clear lacp <number:dynamic> counters <cr>
```

Handler ` RVA 0xC8D3130 `；selector ` 0 `；EOL ` RVA 0x33B13D58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Channel group number。

[条件 C-be2b61aa1b58d6c8](../../evidence/conditions-sets-073.md#c-be2b61aa1b58d6c8) · [缺口 G-d3d6c58bb09f4016](../../evidence/gaps-sets-007.md#g-d3d6c58bb09f4016) · [参数 P-d3527a97af0e81cc](../../evidence/parameters-sets-016.md#p-d3527a97af0e81cc) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-031758

```text
(config)# do-exec clear lacp counters <cr>
```

Handler ` RVA 0xC8D3130 `；selector ` 0 `；EOL ` RVA 0x33B13D58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-038146

```text
(config)# do-exec clear ldap server <string> <cr>
```

Handler ` RVA 0x11ABB2B0 `；selector ` 21 `；EOL ` RVA 0x3560CEA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Server name。

[条件 C-b439acb4a73e550d](../../evidence/conditions-sets-070.md#c-b439acb4a73e550d) · [参数 P-4ad9af8e953ad328](../../evidence/parameters-sets-006.md#p-4ad9af8e953ad328) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-060519

```text
(config)# do-exec clear line <?ttyline_action@5555896af940> <cr>
```

Handler ` RVA 0xE0008A0 `；selector ` 0 `；EOL ` RVA 0x3415B9A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b67127a28b6ea35c](../../evidence/conditions-sets-071.md#c-b67127a28b6ea35c) · [缺口 G-79f13ebc4039af03](../../evidence/gaps-sets-005.md#g-79f13ebc4039af03) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-060520

```text
(config)# do-exec clear line <?ttyline_action@5555896af940> <cr>
```

Handler ` RVA 0xDFE6D10 `；selector ` 0 `；EOL ` RVA 0x3415BC28 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e82f4a46d8de482e](../../evidence/conditions-sets-090.md#c-e82f4a46d8de482e) · [缺口 G-79f13ebc4039af03](../../evidence/gaps-sets-005.md#g-79f13ebc4039af03) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-028214

```text
(config)# do-exec clear line async-queue <cr>
```

Handler ` RVA 0xCCFAD80 `；selector ` 0 `；EOL ` RVA 0x33C680A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1d1ab4034f0fca5d](../../evidence/state_effects-sets-007.md#s-1d1ab4034f0fca5d)

### path-030136

```text
(config)# do-exec clear lldp counters <cr>
```

Handler ` RVA 0x158A1C40 `；selector ` 0 `；EOL ` RVA 0x35D9E640 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-030176

```text
(config)# do-exec clear lldp table <cr>
```

Handler ` RVA 0x158A1DB0 `；selector ` 0 `；EOL ` RVA 0x35D9E8E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-026302

```text
(config)# do-exec clear logging <cr>
```

Handler ` RVA 0xE073AF0 `；selector ` 0 `；EOL ` RVA 0x34191218 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-028104

```text
(config)# do-exec clear logging persistent <cr>
```

Handler ` RVA 0xE06AAF0 `；selector ` 0 `；EOL ` RVA 0x34191280 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061211

```text
(config)# do-exec clear logging persistent url <url:dynamic> <cr>
```

Handler ` RVA 0xE06AAF0 `；selector ` 0 `；EOL ` RVA 0x34191280 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a800aebb929aa16a](../../evidence/conditions-sets-065.md#c-a800aebb929aa16a) · [缺口 G-cb87c2ba76385b34](../../evidence/gaps-sets-007.md#g-cb87c2ba76385b34) · [参数 P-f5c46526879ab3f9](../../evidence/parameters-sets-018.md#p-f5c46526879ab3f9) · [状态效果 S-26b72acc7e8e0b75](../../evidence/state_effects-sets-009.md#s-26b72acc7e8e0b75)

### path-028049

```text
(config)# do-exec clear logging xml <cr>
```

Handler ` RVA 0xE073A20 `；selector ` 0 `；EOL ` RVA 0x34190F48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-039827

```text
(config)# do-exec clear mac address-table dynamic <cr>
```

Handler ` RVA 0x15E779F0 `；selector ` 7 `；EOL ` RVA 0x35E52FA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062062

```text
(config)# do-exec clear mac address-table dynamic vlan <number:dynamic> <cr>
```

Handler ` RVA 0x15E779F0 `；selector ` 7 `；EOL ` RVA 0x35E52FA0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` VLAN number。

[条件 C-e5c587f59f49db01](../../evidence/conditions-sets-089.md#c-e5c587f59f49db01) · [缺口 G-571c3a5f40809568](../../evidence/gaps-sets-004.md#g-571c3a5f40809568) · [参数 P-c0bfb07cf990b843](../../evidence/parameters-sets-015.md#p-c0bfb07cf990b843) · [状态效果 S-5d5c7b7d212a5c11](../../evidence/state_effects-sets-020.md#s-5d5c7b7d212a5c11)

### path-060789

```text
(config)# do-exec clear macsec interface <interface> <cr>
```

Handler ` RVA 0x1610BF20 `；selector ` 1 `；EOL ` RVA 0x35ED7E38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e1cbfc72f4d099ec](../../evidence/conditions-sets-087.md#c-e1cbfc72f4d099ec) · [缺口 G-14f7efacf0b1fbd8](../../evidence/gaps-sets-001.md#g-14f7efacf0b1fbd8) · [参数 P-73c9d0c120c4f9a4](../../evidence/parameters-sets-009.md#p-73c9d0c120c4f9a4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-060791

```text
(config)# do-exec clear macsec interface <interface> <cr>
```

Handler ` RVA 0x16107EE0 `；selector ` 1 `；EOL ` RVA 0x35ED80E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-683892cfceea4b97](../../evidence/conditions-sets-040.md#c-683892cfceea4b97) · [缺口 G-14f7efacf0b1fbd8](../../evidence/gaps-sets-001.md#g-14f7efacf0b1fbd8) · [参数 P-73c9d0c120c4f9a4](../../evidence/parameters-sets-009.md#p-73c9d0c120c4f9a4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061357

```text
(config)# do-exec clear mdns-sd cache interface <interface> <cr>
```

Handler ` RVA 0x142A3750 `；selector ` 0 `；EOL ` RVA 0x35D0FFE8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9aa9cacd4187da53](../../evidence/conditions-sets-060.md#c-9aa9cacd4187da53) · [缺口 G-023b399e03ac9891](../../evidence/gaps-sets-001.md#g-023b399e03ac9891) · [参数 P-d1ac6734bfdbb3ee](../../evidence/parameters-sets-016.md#p-d1ac6734bfdbb3ee) · [状态效果 S-bc0dc1d9e8a3fc6d](../../evidence/state_effects-sets-040.md#s-bc0dc1d9e8a3fc6d)

### path-030286

```text
(config)# do-exec clear mdns-sd query-db <cr>
```

Handler ` RVA 0x142A3750 `；selector ` 0 `；EOL ` RVA 0x35D0FFE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-07a7cff2fe96286d](../../evidence/conditions-sets-003.md#c-07a7cff2fe96286d) · [状态效果 S-2dd35df2004b4efa](../../evidence/state_effects-sets-010.md#s-2dd35df2004b4efa)

### path-031291

```text
(config)# do-exec clear memory events <cr>
```

Handler ` RVA 0xE0914B0 `；selector ` 0 `；EOL ` RVA 0x341E5930 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-84dc18100e4fe16f](../../evidence/conditions-sets-051.md#c-84dc18100e4fe16f) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-031238

```text
(config)# do-exec clear memory low-water-mark <cr>
```

Handler ` RVA 0xE0403F0 `；selector ` 0 `；EOL ` RVA 0x341E5648 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-030899

```text
(config)# do-exec clear mfib linecard <cr>
```

Handler ` RVA 0x11667DB0 `；selector ` 0 `；EOL ` RVA 0x35524F90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-dbcfe4717b43cd3b](../../evidence/conditions-sets-085.md#c-dbcfe4717b43cd3b) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-060939

```text
(config)# do-exec clear mfib linecard <number:dynamic> <cr>
```

Handler ` RVA 0x11667DB0 `；selector ` 0 `；EOL ` RVA 0x35524F90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` linecard slot number。

[条件 C-de4b01c1134f19e2](../../evidence/conditions-sets-086.md#c-de4b01c1134f19e2) · [缺口 G-0c32c9941973a8da](../../evidence/gaps-sets-001.md#g-0c32c9941973a8da) · [参数 P-2bb1176f17fe6f51](../../evidence/parameters-sets-004.md#p-2bb1176f17fe6f51) · [状态效果 S-2043f2098f64aa90](../../evidence/state_effects-sets-007.md#s-2043f2098f64aa90)

### path-060926

```text
(config)# do-exec clear mfib table <?option@55558aafab20> <cr>
```

Handler ` RVA 0x118FAD20 `；selector ` 0 `；EOL ` RVA 0x355A6B88 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ac5cfdd9b88b227e](../../evidence/conditions-sets-067.md#c-ac5cfdd9b88b227e) · [缺口 G-eb31622f19d906db](../../evidence/gaps-sets-008.md#g-eb31622f19d906db) · [状态效果 S-f5064bf5ed9b9d81](../../evidence/state_effects-sets-052.md#s-f5064bf5ed9b9d81)

### path-030782

```text
(config)# do-exec clear mfib table <cr>
```

Handler ` RVA 0x118FAD20 `；selector ` 0 `；EOL ` RVA 0x355A6B88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-88896570ce88308c](../../evidence/conditions-sets-053.md#c-88896570ce88308c) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-031777

```text
(config)# do-exec clear mka all <cr>
```

Handler ` RVA 0x160776D0 `；selector ` 1 `；EOL ` RVA 0x35EB59A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-031866

```text
(config)# do-exec clear mka sessions <cr>
```

Handler ` RVA 0x160776D0 `；selector ` 2 `；EOL ` RVA 0x35EAFDF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061559

```text
(config)# do-exec clear mka sessions interface <interface> <cr>
```

Handler ` RVA 0x160776D0 `；selector ` 5 `；EOL ` RVA 0x35EB0060 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d549e5c1686352f0](../../evidence/conditions-sets-082.md#c-d549e5c1686352f0) · [缺口 G-733cfbe6692228eb](../../evidence/gaps-sets-004.md#g-733cfbe6692228eb) · [参数 P-c2680b780628892f](../../evidence/parameters-sets-015.md#p-c2680b780628892f) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062380

```text
(config)# do-exec clear mka sessions interface <interface> efp <number:1..16384> <cr>
```

Handler ` RVA 0x160776D0 `；selector ` 3 `；EOL ` RVA 0x35EB6188 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Service instance Id (default = 0。

[条件 C-be06eeb994a7e89b](../../evidence/conditions-sets-073.md#c-be06eeb994a7e89b) · [缺口 G-733cfbe6692228eb](../../evidence/gaps-sets-004.md#g-733cfbe6692228eb) · [参数 P-f974a674d387be37](../../evidence/parameters-sets-019.md#p-f974a674d387be37) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062370

```text
(config)# do-exec clear mka sessions interface <interface> port-id <number:1..65535> <cr>
```

Handler ` RVA 0x160776D0 `；selector ` 4 `；EOL ` RVA 0x35EB5E40 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` MKA Port ID。

[条件 C-730a9d6951321d9d](../../evidence/conditions-sets-044.md#c-730a9d6951321d9d) · [缺口 G-733cfbe6692228eb](../../evidence/gaps-sets-004.md#g-733cfbe6692228eb) · [参数 P-1b42e7fe217985e5](../../evidence/parameters-sets-003.md#p-1b42e7fe217985e5) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061535

```text
(config)# do-exec clear mka sessions local-sci <hex-string> <cr>
```

Handler ` RVA 0x160776D0 `；selector ` 6 `；EOL ` RVA 0x35EB64A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` hexstring ` 64-bit Hexadecimal Local Tx-SCI。

[条件 C-7659267a94eaf318](../../evidence/conditions-sets-046.md#c-7659267a94eaf318) · [缺口 G-50033e68ebeffa9f](../../evidence/gaps-sets-003.md#g-50033e68ebeffa9f) · [参数 P-58cb731acac4366c](../../evidence/parameters-sets-007.md#p-58cb731acac4366c) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-031879

```text
(config)# do-exec clear mka statistics <cr>
```

Handler ` RVA 0x160776D0 `；selector ` 7 `；EOL ` RVA 0x35EB02C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061563

```text
(config)# do-exec clear mka statistics interface <interface> <cr>
```

Handler ` RVA 0x160776D0 `；selector ` 8 `；EOL ` RVA 0x35EB0530 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-562fb657358b4cb2](../../evidence/conditions-sets-034.md#c-562fb657358b4cb2) · [缺口 G-752addc57444e789](../../evidence/gaps-sets-005.md#g-752addc57444e789) · [参数 P-85169aaa6d8420c1](../../evidence/parameters-sets-010.md#p-85169aaa6d8420c1) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062384

```text
(config)# do-exec clear mka statistics interface <interface> efp <number:1..16384> <cr>
```

Handler ` RVA 0x160776D0 `；selector ` 9 `；EOL ` RVA 0x35EB6C58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Service instance Id (default = 0。

[条件 C-6a52012317c4b9c5](../../evidence/conditions-sets-041.md#c-6a52012317c4b9c5) · [缺口 G-752addc57444e789](../../evidence/gaps-sets-005.md#g-752addc57444e789) · [参数 P-357d253696002111](../../evidence/parameters-sets-005.md#p-357d253696002111) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062373

```text
(config)# do-exec clear mka statistics interface <interface> port-id <number:1..65535> <cr>
```

Handler ` RVA 0x160776D0 `；selector ` 8 `；EOL ` RVA 0x35EB6910 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` MKA Port ID。

[条件 C-188e1dcf4e337150](../../evidence/conditions-sets-010.md#c-188e1dcf4e337150) · [缺口 G-752addc57444e789](../../evidence/gaps-sets-005.md#g-752addc57444e789) · [参数 P-37392f467f1c1fe4](../../evidence/parameters-sets-005.md#p-37392f467f1c1fe4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061543

```text
(config)# do-exec clear mka statistics local-sci <hex-string> <cr>
```

Handler ` RVA 0x160776D0 `；selector ` 10 `；EOL ` RVA 0x35EB6F78 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` hexstring ` 64-bit Hexadecimal Local Tx-SCI。

[条件 C-8bd4e1be17f8057d](../../evidence/conditions-sets-054.md#c-8bd4e1be17f8057d) · [缺口 G-d7652b875923a242](../../evidence/gaps-sets-007.md#g-d7652b875923a242) · [参数 P-56d4632e094d4386](../../evidence/parameters-sets-007.md#p-56d4632e094d4386) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-037291

```text
(config)# do-exec clear mlrib layer2 statistics <cr>
```

Handler ` RVA 0xC88D760 `；selector ` 0 `；EOL ` RVA 0x33B09E28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fb46cf23a65ec1af](../../evidence/conditions-sets-097.md#c-fb46cf23a65ec1af) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-030516

```text
(config)# do-exec clear mvr counters <cr>
```

Handler ` RVA 0xC3B5C20 `；selector ` 0 `；EOL ` RVA 0x33A64008 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061396

```text
(config)# do-exec clear mvr counters receiver-ports <interface> <cr>
```

Handler ` RVA 0xC3B5C20 `；selector ` 0 `；EOL ` RVA 0x33A64008 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8e08ff6052c4b62e](../../evidence/conditions-sets-055.md#c-8e08ff6052c4b62e) · [缺口 G-ccb3e5c3322e0d1a](../../evidence/gaps-sets-007.md#g-ccb3e5c3322e0d1a) · [参数 P-46dad9761e059d77](../../evidence/parameters-sets-006.md#p-46dad9761e059d77) · [状态效果 S-56f38c9c6c928070](../../evidence/state_effects-sets-019.md#s-56f38c9c6c928070)

### path-035503

```text
(config)# do-exec clear nat64 ha statistics <cr>
```

Handler ` RVA 0xD58DBC0 `；selector ` 1 `；EOL ` RVA 0x33E928B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5b9a28e1fef1b188](../../evidence/conditions-sets-036.md#c-5b9a28e1fef1b188) · [状态效果 S-a5ac67dc3a433089](../../evidence/state_effects-sets-035.md#s-a5ac67dc3a433089)

### path-045167

```text
(config)# do-exec clear nat64 map-e rule running <cr>
```

Handler ` RVA 0xD58DBC0 `；selector ` 3 `；EOL ` RVA 0x33E93370 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-49d82582f10f1ef6](../../evidence/conditions-sets-029.md#c-49d82582f10f1ef6) · [状态效果 S-3644d8b8eee34ece](../../evidence/state_effects-sets-012.md#s-3644d8b8eee34ece)

### path-029669

```text
(config)# do-exec clear nat64 statistics <cr>
```

Handler ` RVA 0xD58DBC0 `；selector ` 0 `；EOL ` RVA 0x33E92028 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-63556c9dc475bf87](../../evidence/conditions-sets-038.md#c-63556c9dc475bf87) · [状态效果 S-ccc36459adb9c515](../../evidence/state_effects-sets-043.md#s-ccc36459adb9c515)

### path-061279

```text
(config)# do-exec clear nat64 statistics interface <interface> <cr>
```

Handler ` RVA 0xD58DBC0 `；selector ` 0 `；EOL ` RVA 0x33E92028 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-fd0b695b816c7fb3](../../evidence/conditions-sets-098.md#c-fd0b695b816c7fb3) · [缺口 G-62e3f3054ea96dc0](../../evidence/gaps-sets-004.md#g-62e3f3054ea96dc0) · [参数 P-30c486a00d7c8fd5](../../evidence/parameters-sets-004.md#p-30c486a00d7c8fd5) · [状态效果 S-6943b99b420ff11e](../../evidence/state_effects-sets-023.md#s-6943b99b420ff11e)

### path-035632

```text
(config)# do-exec clear nat64 translations all <cr>
```

Handler ` RVA 0xD58DBC0 `；selector ` 2 `；EOL ` RVA 0x33E92C30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1440cf250c18609a](../../evidence/conditions-sets-008.md#c-1440cf250c18609a) · [状态效果 S-acc3dfa51b8673c3](../../evidence/state_effects-sets-037.md#s-acc3dfa51b8673c3)

### path-061293

```text
(config)# do-exec clear nat64 translations interface <interface> <cr>
```

Handler ` RVA 0xD58DBC0 `；selector ` 2 `；EOL ` RVA 0x33E92C30 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-efda634e71a2e54a](../../evidence/conditions-sets-093.md#c-efda634e71a2e54a) · [缺口 G-2c1aa6ec1c703740](../../evidence/gaps-sets-002.md#g-2c1aa6ec1c703740) · [参数 P-447d850c58f06c4c](../../evidence/parameters-sets-006.md#p-447d850c58f06c4c) · [状态效果 S-79de76a835865f8d](../../evidence/state_effects-sets-026.md#s-79de76a835865f8d)

### path-029625

```text
(config)# do-exec clear nat66 statistics <cr>
```

Handler ` RVA 0xD612DA0 `；selector ` 0 `；EOL ` RVA 0x33EAD460 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c04533ad125be8a7](../../evidence/conditions-sets-074.md#c-c04533ad125be8a7) · [状态效果 S-25bb632626b09ea7](../../evidence/state_effects-sets-008.md#s-25bb632626b09ea7)

### path-061277

```text
(config)# do-exec clear nat66 statistics prefix <prefix:dynamic> <cr>
```

Handler ` RVA 0xD612DA0 `；selector ` 0 `；EOL ` RVA 0x33EAD460 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` Prefix/length to lookup。

[条件 C-5407616d2520c681](../../evidence/conditions-sets-033.md#c-5407616d2520c681) · [缺口 G-b0b91fc31834a82a](../../evidence/gaps-sets-006.md#g-b0b91fc31834a82a) · [参数 P-986460338cf6ff9f](../../evidence/parameters-sets-012.md#p-986460338cf6ff9f) · [状态效果 S-f8ba9b35c5b6a6c1](../../evidence/state_effects-sets-053.md#s-f8ba9b35c5b6a6c1)

### path-031625

```text
(config)# do-exec clear ncia circuits <cr>
```

Handler ` RVA 0x11B1D2B0 `；selector ` 0 `；EOL ` RVA 0x3562BAC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-a49242cc04d358dd](../../evidence/state_effects-sets-035.md#s-a49242cc04d358dd)

### path-027600

```text
(config)# do-exec clear netbios-cache <cr>
```

Handler ` RVA 0x114B22B0 `；selector ` 0 `；EOL ` RVA 0x354F4B00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-031374

```text
(config)# do-exec clear netconf counters <cr>
```

Handler ` RVA 0xF3C94B0 `；selector ` 0 `；EOL ` RVA 0x3462A498 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-031406

```text
(config)# do-exec clear netconf sessions <cr>
```

Handler ` RVA 0xF3C9770 `；selector ` 0 `；EOL ` RVA 0x3462A740 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-030734

```text
(config)# do-exec clear nhrp stats <cr>
```

Handler ` RVA 0x10886440 `；selector ` 2 `；EOL ` RVA 0x34BEA778 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-634a40b52d15d14f](../../evidence/conditions-sets-038.md#c-634a40b52d15d14f) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-060917

```text
(config)# do-exec clear nhrp stats <interface> <cr>
```

Handler ` RVA 0x10886440 `；selector ` 2 `；EOL ` RVA 0x34BEA778 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2d43fcace0c5d7f7](../../evidence/conditions-sets-018.md#c-2d43fcace0c5d7f7) · [缺口 G-844aa1cbf2d59099](../../evidence/gaps-sets-005.md#g-844aa1cbf2d59099) · [参数 P-a48e646a15620729](../../evidence/parameters-sets-013.md#p-a48e646a15620729) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-037451

```text
(config)# do-exec clear nhrp stats performance <cr>
```

Handler ` RVA 0x10886440 `；selector ` 4 `；EOL ` RVA 0x34BEAAF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-634a40b52d15d14f](../../evidence/conditions-sets-038.md#c-634a40b52d15d14f) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061486

```text
(config)# do-exec clear onep statistics session <?option@55558b204b98> <cr>
```

Handler ` RVA 0x13A7E7E0 `；selector ` 0 `；EOL ` RVA 0x35CB0C78 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3e66e5ecb1dab6a4](../../evidence/conditions-sets-024.md#c-3e66e5ecb1dab6a4) · [缺口 G-4bba474144a01b96](../../evidence/gaps-sets-003.md#g-4bba474144a01b96) · [状态效果 S-54ea0361442bcfa2](../../evidence/state_effects-sets-018.md#s-54ea0361442bcfa2)

### path-031194

```text
(config)# do-exec clear onep trace <cr>
```

Handler ` RVA 0x13A7E7E0 `；selector ` 0 `；EOL ` RVA 0x35CB0C78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6ffc52315397e374](../../evidence/conditions-sets-043.md#c-6ffc52315397e374) · [状态效果 S-c33a05fe8478a5a3](../../evidence/state_effects-sets-041.md#s-c33a05fe8478a5a3)

### path-054334

```text
(config)# do-exec clear opflex agent service vxlan-evpn all <cr>
```

Handler ` RVA 0xC496410 `；selector ` 0 `；EOL ` RVA 0x33A96CC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-031020

```text
(config)# do-exec clear ospfv3 counters <cr>
```

Handler ` RVA 0x11BF58A0 `；selector ` 4 `；EOL ` RVA 0x35691290 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9932317dec97839b](../../evidence/conditions-sets-059.md#c-9932317dec97839b) · [状态效果 S-c8a9982c7091eb0e](../../evidence/state_effects-sets-042.md#s-c8a9982c7091eb0e)

### path-061461

```text
(config)# do-exec clear ospfv3 counters neighbor <interface> <cr>
```

Handler ` RVA 0x11BF58A0 `；selector ` 4 `；EOL ` RVA 0x35691290 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4668cb114f325f92](../../evidence/conditions-sets-027.md#c-4668cb114f325f92) · [缺口 G-451aad08ba5859b7](../../evidence/gaps-sets-003.md#g-451aad08ba5859b7) · [参数 P-08f32a4bf85bf02a](../../evidence/parameters-sets-001.md#p-08f32a4bf85bf02a) · [状态效果 S-c8a9982c7091eb0e](../../evidence/state_effects-sets-042.md#s-c8a9982c7091eb0e)

### path-031011

```text
(config)# do-exec clear ospfv3 events <cr>
```

Handler ` RVA 0x11BF58A0 `；selector ` 5 `；EOL ` RVA 0x35691690 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9932317dec97839b](../../evidence/conditions-sets-059.md#c-9932317dec97839b) · [状态效果 S-c8a9982c7091eb0e](../../evidence/state_effects-sets-042.md#s-c8a9982c7091eb0e)

### path-030936

```text
(config)# do-exec clear ospfv3 force-spf <cr>
```

Handler ` RVA 0x11BF58A0 `；selector ` 2 `；EOL ` RVA 0x35690A10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9932317dec97839b](../../evidence/conditions-sets-059.md#c-9932317dec97839b) · [状态效果 S-c8a9982c7091eb0e](../../evidence/state_effects-sets-042.md#s-c8a9982c7091eb0e)

### path-030916

```text
(config)# do-exec clear ospfv3 process <cr>
```

Handler ` RVA 0x11BF58A0 `；selector ` 1 `；EOL ` RVA 0x35690768 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9932317dec97839b](../../evidence/conditions-sets-059.md#c-9932317dec97839b) · [状态效果 S-c8a9982c7091eb0e](../../evidence/state_effects-sets-042.md#s-c8a9982c7091eb0e)

### path-030887

```text
(config)# do-exec clear ospfv3 redistribution <cr>
```

Handler ` RVA 0x11BF58A0 `；selector ` 0 `；EOL ` RVA 0x356904C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9932317dec97839b](../../evidence/conditions-sets-059.md#c-9932317dec97839b) · [状态效果 S-c8a9982c7091eb0e](../../evidence/state_effects-sets-042.md#s-c8a9982c7091eb0e)

### path-031043

```text
(config)# do-exec clear ospfv3 traffic <cr>
```

Handler ` RVA 0x11BF58A0 `；selector ` 3 `；EOL ` RVA 0x35690E40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a1353d583ddd5931](../../evidence/conditions-sets-062.md#c-a1353d583ddd5931) · [状态效果 S-c8a9982c7091eb0e](../../evidence/state_effects-sets-042.md#s-c8a9982c7091eb0e)

### path-060947

```text
(config)# do-exec clear ospfv3 traffic <interface> <cr>
```

Handler ` RVA 0x11BF58A0 `；selector ` 3 `；EOL ` RVA 0x35690E40 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-071eb6ae01b1478b](../../evidence/conditions-sets-003.md#c-071eb6ae01b1478b) · [缺口 G-2e5f6368a351fbcd](../../evidence/gaps-sets-002.md#g-2e5f6368a351fbcd) · [参数 P-2c0754fd830d2242](../../evidence/parameters-sets-004.md#p-2c0754fd830d2242) · [状态效果 S-c8a9982c7091eb0e](../../evidence/state_effects-sets-042.md#s-c8a9982c7091eb0e)

### path-061481

```text
(config)# do-exec clear ospfv3 vrf * events <cr>
```

Handler ` RVA 0x11BF58A0 `；selector ` 5 `；EOL ` RVA 0x35691690 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c3863efe63871374](../../evidence/conditions-sets-075.md#c-c3863efe63871374) · [缺口 G-ef6c3604c6bd8232](../../evidence/gaps-sets-008.md#g-ef6c3604c6bd8232) · [状态效果 S-be3d37483428763d](../../evidence/state_effects-sets-040.md#s-be3d37483428763d)

### path-061473

```text
(config)# do-exec clear ospfv3 vrf * force-spf <cr>
```

Handler ` RVA 0x11BF58A0 `；selector ` 2 `；EOL ` RVA 0x35690A10 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c3863efe63871374](../../evidence/conditions-sets-075.md#c-c3863efe63871374) · [缺口 G-ef6c3604c6bd8232](../../evidence/gaps-sets-008.md#g-ef6c3604c6bd8232) · [状态效果 S-be3d37483428763d](../../evidence/state_effects-sets-040.md#s-be3d37483428763d)

### path-061469

```text
(config)# do-exec clear ospfv3 vrf * process <cr>
```

Handler ` RVA 0x11BF58A0 `；selector ` 1 `；EOL ` RVA 0x35690768 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c3863efe63871374](../../evidence/conditions-sets-075.md#c-c3863efe63871374) · [缺口 G-ef6c3604c6bd8232](../../evidence/gaps-sets-008.md#g-ef6c3604c6bd8232) · [状态效果 S-be3d37483428763d](../../evidence/state_effects-sets-040.md#s-be3d37483428763d)

### path-061467

```text
(config)# do-exec clear ospfv3 vrf * redistribution <cr>
```

Handler ` RVA 0x11BF58A0 `；selector ` 0 `；EOL ` RVA 0x356904C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c3863efe63871374](../../evidence/conditions-sets-075.md#c-c3863efe63871374) · [缺口 G-ef6c3604c6bd8232](../../evidence/gaps-sets-008.md#g-ef6c3604c6bd8232) · [状态效果 S-be3d37483428763d](../../evidence/state_effects-sets-040.md#s-be3d37483428763d)

### path-029368

```text
(config)# do-exec clear packet-debug pak_debug_tracebuf <cr>
```

Handler ` RVA 0xEB837C0 `；selector ` 0 `；EOL ` RVA 0x343CEE00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-027993

```text
(config)# do-exec clear parser atomic-config <cr>
```

Handler ` RVA 0xDF052E0 `；selector ` 0 `；EOL ` RVA 0x340BD738 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-028035

```text
(config)# do-exec clear parser cache <cr>
```

Handler ` RVA 0xE101400 `；selector ` 0 `；EOL ` RVA 0x340BDC88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-028015

```text
(config)# do-exec clear parser statistics <cr>
```

Handler ` RVA 0xDF05050 `；selector ` 0 `；EOL ` RVA 0x340BD9E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-027944

```text
(config)# do-exec clear platform arpsnooping-trace <cr>
```

Handler ` RVA 0xEACB020 `；selector ` 1 `；EOL ` RVA 0x343A1328 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b3dc36f781238252](../../evidence/conditions-sets-070.md#c-b3dc36f781238252) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061835

```text
(config)# do-exec clear platform authentication secure-mac <interface> all <cr>
```

Handler ` RVA 0x15E9D290 `；selector ` 0 `；EOL ` RVA 0x35E5AD50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-570b6683ea45c251](../../evidence/conditions-sets-034.md#c-570b6683ea45c251) · [缺口 G-92f12b4aec2b56db](../../evidence/gaps-sets-005.md#g-92f12b4aec2b56db) · [参数 P-b76a291150af090d](../../evidence/parameters-sets-014.md#p-b76a291150af090d) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062232

```text
(config)# do-exec clear platform authentication secure-mac <interface> mac <address> <cr>
```

Handler ` RVA 0x15E9D290 `；selector ` 1 `；EOL ` RVA 0x35E5B038 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` MAC address。

[条件 C-570b6683ea45c251](../../evidence/conditions-sets-034.md#c-570b6683ea45c251) · [缺口 G-92f12b4aec2b56db](../../evidence/gaps-sets-005.md#g-92f12b4aec2b56db) · [参数 P-f2b7a5e4d238934c](../../evidence/parameters-sets-018.md#p-f2b7a5e4d238934c) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-034045

```text
(config)# do-exec clear platform condition all <cr>
```

Handler ` RVA 0x158E4EA0 `；selector ` 0 `；EOL ` RVA 0x35DB0F20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c99aac6451c4bf30](../../evidence/conditions-sets-078.md#c-c99aac6451c4bf30) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-043906

```text
(config)# do-exec clear platform dhcpsnooping pkt-trace ipv4 <cr>
```

Handler ` RVA 0xEACB090 `；selector ` 0 `；EOL ` RVA 0x343A0C10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b3dc36f781238252](../../evidence/conditions-sets-070.md#c-b3dc36f781238252) · [状态效果 S-d69479c5e79d09b1](../../evidence/state_effects-sets-045.md#s-d69479c5e79d09b1)

### path-034044

```text
(config)# do-exec clear platform packet-trace configuration <cr>
```

Handler ` RVA 0x158D4090 `；selector ` 0 `；EOL ` RVA 0x35DB09A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c61c620eec968228](../../evidence/conditions-sets-076.md#c-c61c620eec968228) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-034059

```text
(config)# do-exec clear platform packet-trace statistics <cr>
```

Handler ` RVA 0x158D3F00 `；selector ` 0 `；EOL ` RVA 0x35DB0C48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c61c620eec968228](../../evidence/conditions-sets-076.md#c-c61c620eec968228) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-043970

```text
(config)# do-exec clear platform software adjacency counters <cr>
```

Handler ` RVA 0xE567190 `；selector ` 1 `；EOL ` RVA 0x342F4BD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2a0639050eff5d0d](../../evidence/conditions-sets-016.md#c-2a0639050eff5d0d) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-043958

```text
(config)# do-exec clear platform software adjacency nexthop-ipfrr <cr>
```

Handler ` RVA 0xE567190 `；selector ` 2 `；EOL ` RVA 0x342F4930 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2a0639050eff5d0d](../../evidence/conditions-sets-016.md#c-2a0639050eff5d0d) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-044478

```text
(config)# do-exec clear platform software cce statistics <cr>
```

Handler ` RVA 0xE597F40 `；selector ` 2 `；EOL ` RVA 0x342F8050 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2a0639050eff5d0d](../../evidence/conditions-sets-016.md#c-2a0639050eff5d0d) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-043966

```text
(config)# do-exec clear platform software cef counters <cr>
```

Handler ` RVA 0xE5CE250 `；selector ` 1 `；EOL ` RVA 0x342FBFC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2a0639050eff5d0d](../../evidence/conditions-sets-016.md#c-2a0639050eff5d0d) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-043928

```text
(config)# do-exec clear platform software cli-agent counters <cr>
```

Handler ` RVA 0x143F2CF0 `；selector ` 0 `；EOL ` RVA 0x35D5D6C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2a0639050eff5d0d](../../evidence/conditions-sets-016.md#c-2a0639050eff5d0d) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-043913

```text
(config)# do-exec clear platform software cman statistics <cr>
```

Handler ` RVA 0xE3583D0 `；selector ` 1 `；EOL ` RVA 0x342AD6F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2a0639050eff5d0d](../../evidence/conditions-sets-016.md#c-2a0639050eff5d0d) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-052493

```text
(config)# do-exec clear platform software crimson operational statistics <cr>
```

Handler ` RVA 0x1444A8A0 `；selector ` 0 `；EOL ` RVA 0x35D68D80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2a0639050eff5d0d](../../evidence/conditions-sets-016.md#c-2a0639050eff5d0d) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-043921

```text
(config)# do-exec clear platform software dpidb counters <cr>
```

Handler ` RVA 0xEA1B4A0 `；selector ` 1 `；EOL ` RVA 0x3438F280 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2a0639050eff5d0d](../../evidence/conditions-sets-016.md#c-2a0639050eff5d0d) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-044065

```text
(config)# do-exec clear platform software epbr statistics <cr>
```

Handler ` RVA 0x15775CC0 `；selector ` 1 `；EOL ` RVA 0x35D8A6C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2a0639050eff5d0d](../../evidence/conditions-sets-016.md#c-2a0639050eff5d0d) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-052061

```text
(config)# do-exec clear platform software ethernet efp statistics <cr>
```

Handler ` RVA 0xC0843F0 `；selector ` 2 `；EOL ` RVA 0x3398F018 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2a0639050eff5d0d](../../evidence/conditions-sets-016.md#c-2a0639050eff5d0d) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-043999

```text
(config)# do-exec clear platform software fhs statistics <cr>
```

Handler ` RVA 0x1579CD20 `；selector ` 2 `；EOL ` RVA 0x35D8E080 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2a0639050eff5d0d](../../evidence/conditions-sets-016.md#c-2a0639050eff5d0d) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-044179

```text
(config)# do-exec clear platform software flow statistics <cr>
```

Handler ` RVA 0xE6AE2F0 `；selector ` 1 `；EOL ` RVA 0x34304060 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2a0639050eff5d0d](../../evidence/conditions-sets-016.md#c-2a0639050eff5d0d) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-044207

```text
(config)# do-exec clear platform software icmp statistics <cr>
```

Handler ` RVA 0xE6CEF90 `；selector ` 2 `；EOL ` RVA 0x34306D68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2a0639050eff5d0d](../../evidence/conditions-sets-016.md#c-2a0639050eff5d0d) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-044665

```text
(config)# do-exec clear platform software infrastructure bipc <cr>
```

Handler ` RVA 0xE9C5750 `；selector ` 1 `；EOL ` RVA 0x34377AB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2a0639050eff5d0d](../../evidence/conditions-sets-016.md#c-2a0639050eff5d0d) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-044704

```text
(config)# do-exec clear platform software infrastructure chasfs <cr>
```

Handler ` RVA 0xE9C5750 `；selector ` 4 `；EOL ` RVA 0x34378418 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2a0639050eff5d0d](../../evidence/conditions-sets-016.md#c-2a0639050eff5d0d) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-044749

```text
(config)# do-exec clear platform software infrastructure debug <cr>
```

Handler ` RVA 0xE9C5750 `；selector ` 5 `；EOL ` RVA 0x343786C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2a0639050eff5d0d](../../evidence/conditions-sets-016.md#c-2a0639050eff5d0d) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-044653

```text
(config)# do-exec clear platform software infrastructure inject <cr>
```

Handler ` RVA 0xEA60970 `；selector ` 1 `；EOL ` RVA 0x34395F80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2a0639050eff5d0d](../../evidence/conditions-sets-016.md#c-2a0639050eff5d0d) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-057004

```text
(config)# do-exec clear platform software infrastructure lfts sar all <cr>
```

Handler ` RVA 0xE3081B0 `；selector ` 2 `；EOL ` RVA 0x342AB328 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2a0639050eff5d0d](../../evidence/conditions-sets-016.md#c-2a0639050eff5d0d) · [状态效果 S-dcc5687d4ec0085c](../../evidence/state_effects-sets-047.md#s-dcc5687d4ec0085c)

### path-059006

```text
(config)# do-exec clear platform software infrastructure lfts sar ipv4-addr <address> <cr>
```

Handler ` RVA 0xE3081B0 `；selector ` 1 `；EOL ` RVA 0x342AADD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IPv4 destination address。

[条件 C-2a0639050eff5d0d](../../evidence/conditions-sets-016.md#c-2a0639050eff5d0d) · [参数 P-f3c024ccdf099f41](../../evidence/parameters-sets-018.md#p-f3c024ccdf099f41) · [状态效果 S-dcc5687d4ec0085c](../../evidence/state_effects-sets-047.md#s-dcc5687d4ec0085c)

### path-059011

```text
(config)# do-exec clear platform software infrastructure lfts sar ipv6-addr <address> <cr>
```

Handler ` RVA 0xE3081B0 `；selector ` 0 `；EOL ` RVA 0x342AB090 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IPv6 destination address。

[条件 C-2a0639050eff5d0d](../../evidence/conditions-sets-016.md#c-2a0639050eff5d0d) · [参数 P-4e61aab428a25168](../../evidence/parameters-sets-006.md#p-4e61aab428a25168) · [状态效果 S-dcc5687d4ec0085c](../../evidence/state_effects-sets-047.md#s-dcc5687d4ec0085c)

### path-044614

```text
(config)# do-exec clear platform software infrastructure lsmpi <cr>
```

Handler ` RVA 0xED2F9D0 `；selector ` 1 `；EOL ` RVA 0x3440B2E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2a0639050eff5d0d](../../evidence/conditions-sets-016.md#c-2a0639050eff5d0d) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-044613

```text
(config)# do-exec clear platform software infrastructure packet <cr>
```

Handler ` RVA 0xE9C5750 `；selector ` 2 `；EOL ` RVA 0x34377DC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2a0639050eff5d0d](../../evidence/conditions-sets-016.md#c-2a0639050eff5d0d) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062818

```text
(config)# do-exec clear platform software infrastructure punt <cr>
```

Handler ` RVA 0xEA601D0 `；selector ` 1 `；EOL ` RVA 0x343962A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-fd72c0ac09ce2373](../../evidence/conditions-sets-098.md#c-fd72c0ac09ce2373) · [缺口 G-a7d8af021b8792a5](../../evidence/gaps-sets-006.md#g-a7d8af021b8792a5) · [状态效果 S-8d5ade8b15aa33c4](../../evidence/state_effects-sets-030.md#s-8d5ade8b15aa33c4)

### path-062857

```text
(config)# do-exec clear platform software infrastructure punt statistics <cr>
```

Handler ` RVA 0xEA942F0 `；selector ` 2 `；EOL ` RVA 0x34396538 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b9cd5252240f49ab](../../evidence/conditions-sets-072.md#c-b9cd5252240f49ab) · [缺口 G-a7d8af021b8792a5](../../evidence/gaps-sets-006.md#g-a7d8af021b8792a5) · [状态效果 S-8d5ade8b15aa33c4](../../evidence/state_effects-sets-030.md#s-8d5ade8b15aa33c4)
