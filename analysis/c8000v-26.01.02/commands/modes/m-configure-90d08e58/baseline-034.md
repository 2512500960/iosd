# configure · 六个基础模式的历史连接

[模式索引](README.md) · [总索引](../../README.md)

### path-026957

```text
(config)# default ip multicast-routing <cr>
```

Handler ` RVA 0xF700800 `；selector ` 0 `；EOL ` RVA 0x34756800 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-05718ba35a2d7fc6](../../evidence/conditions-sets-002.md#c-05718ba35a2d7fc6) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-027148

```text
(config)# default ip name-server <cr>
```

Handler ` RVA 0xD12A630 `；selector ` 0 `；EOL ` RVA 0x33D914D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-59cc9aadc2ec33bd](../../evidence/conditions-sets-035.md#c-59cc9aadc2ec33bd) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-035685

```text
(config)# default ip nat create flow-entries <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 18 `；EOL ` RVA 0x347CA8C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c12576940a492abf](../../evidence/conditions-sets-075.md#c-c12576940a492abf) · [状态效果 S-cf1c58f837d79f43](../../evidence/state_effects-sets-044.md#s-cf1c58f837d79f43)

### path-045347

```text
(config)# default ip nat dia track-enable <number:1..65534> <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 42 `；EOL ` RVA 0x347CAC88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Enter DIA track number。

[条件 C-e63fcdb6c6907073](../../evidence/conditions-sets-089.md#c-e63fcdb6c6907073) · [参数 P-c3d1fd70e890fa12](../../evidence/parameters-sets-015.md#p-c3d1fd70e890fa12) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-059154

```text
(config)# default ip nat inside destination list <number:1..2699> pool <string> <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 4 `；EOL ` RVA 0x347D45C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Access list number for global addresses；` string ` Pool name for local addresses。

[条件 C-f84c417fb8e5466f](../../evidence/conditions-sets-096.md#c-f84c417fb8e5466f) · [参数 P-10505f0167cd5432](../../evidence/parameters-sets-002.md#p-10505f0167cd5432) · [状态效果 S-2a2db5c8d6fb036e](../../evidence/state_effects-sets-009.md#s-2a2db5c8d6fb036e)

### path-057603

```text
(config)# default ip nat inside source static <address> <address> <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 2 `；EOL ` RVA 0x347D0F60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` Inside local IP address；` address ` Inside global IP address。

[条件 C-b8da344a9fce82e6](../../evidence/conditions-sets-071.md#c-b8da344a9fce82e6) · [参数 P-4b7c8ab8471c220d](../../evidence/parameters-sets-006.md#p-4b7c8ab8471c220d) · [状态效果 S-ea0358683676a731](../../evidence/state_effects-sets-050.md#s-ea0358683676a731)

### path-035783

```text
(config)# default ip nat log translations <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 7 `；EOL ` RVA 0x347C9E70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-fc144c8580798abf](../../evidence/conditions-sets-097.md#c-fc144c8580798abf) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-036327

```text
(config)# default ip nat name <string> <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 23 `；EOL ` RVA 0x347D0750 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Unique NAT rule name。

[条件 C-b28bdb1d29167c85](../../evidence/conditions-sets-069.md#c-b28bdb1d29167c85) · [参数 P-bb3cc03b9f4d0487](../../evidence/parameters-sets-014.md#p-bb3cc03b9f4d0487) · [状态效果 S-ddf6f9950917d457](../../evidence/state_effects-sets-047.md#s-ddf6f9950917d457)

### path-057583

```text
(config)# default ip nat outside source static <address> <address> <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 3 `；EOL ` RVA 0x347D4F30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` Outside global IP address；` address ` Outside local IP address。

[条件 C-90216e996d4d8035](../../evidence/conditions-sets-056.md#c-90216e996d4d8035) · [参数 P-442605d7e2d85755](../../evidence/parameters-sets-006.md#p-442605d7e2d85755) · [状态效果 S-125fe40cc6b629f9](../../evidence/state_effects-sets-004.md#s-125fe40cc6b629f9)

### path-036267

```text
(config)# default ip nat pool <string> <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 5 `；EOL ` RVA 0x347D0160 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Pool name。

[条件 C-abeba49b28309aee](../../evidence/conditions-sets-066.md#c-abeba49b28309aee) · [参数 P-564288fce6ccb33c](../../evidence/parameters-sets-007.md#p-564288fce6ccb33c) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-059104

```text
(config)# default ip nat route vrf <string> <address> <address> global <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 30 `；EOL ` RVA 0x347CB100 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` VPN Routing/Forwarding instance name；` address ` IP address；` address ` Network mask。

[条件 C-0980870c935f3feb](../../evidence/conditions-sets-004.md#c-0980870c935f3feb) · [参数 P-cb15e1b162af71f6](../../evidence/parameters-sets-015.md#p-cb15e1b162af71f6) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-036263

```text
(config)# default ip nat service ftp <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 6 `；EOL ` RVA 0x347CEA88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-fca532dd4f44adab](../../evidence/conditions-sets-097.md#c-fca532dd4f44adab) · [状态效果 S-96f6dfd5588a9823](../../evidence/state_effects-sets-032.md#s-96f6dfd5588a9823)

### path-035663

```text
(config)# default ip nat settings central-policy <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 35 `；EOL ` RVA 0x347C51C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2b3771e422c2356b](../../evidence/conditions-sets-017.md#c-2b3771e422c2356b) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-045322

```text
(config)# default ip nat settings cfg-check static-map-removal <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 24 `；EOL ` RVA 0x347C5840 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-64aad065c2dd3ef8](../../evidence/conditions-sets-039.md#c-64aad065c2dd3ef8) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-036710

```text
(config)# default ip nat settings fbd <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 39 `；EOL ` RVA 0x347C9298 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-648e5a44549c39fb](../../evidence/conditions-sets-039.md#c-648e5a44549c39fb) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-035977

```text
(config)# default ip nat settings gatekeeper-size <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 25 `；EOL ` RVA 0x347C5F80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c2cf428958c18f8c](../../evidence/conditions-sets-075.md#c-c2cf428958c18f8c) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-036569

```text
(config)# default ip nat settings high-performance <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 34 `；EOL ` RVA 0x347C8980 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c36664293dca202d](../../evidence/conditions-sets-075.md#c-c36664293dca202d) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-059136

```text
(config)# default ip nat settings interface-overload block port tcp <number:1024..65535> <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 29 `；EOL ` RVA 0x347C7A78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Port number。

[条件 C-7e99b0669cfbb181](../../evidence/conditions-sets-049.md#c-7e99b0669cfbb181) · [参数 P-21361a27615d3ab2](../../evidence/parameters-sets-003.md#p-21361a27615d3ab2) · [状态效果 S-0138942157288147](../../evidence/state_effects-sets-001.md#s-0138942157288147)

### path-053218

```text
(config)# default ip nat settings interface-overload port range <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 28 `；EOL ` RVA 0x347C7598 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-96037cbf838f8a76](../../evidence/conditions-sets-058.md#c-96037cbf838f8a76) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-036617

```text
(config)# default ip nat settings log-destination <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 36 `；EOL ` RVA 0x347C8C88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-59ccab8aac1559ec](../../evidence/conditions-sets-035.md#c-59ccab8aac1559ec) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-035840

```text
(config)# default ip nat settings mode <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 21 `；EOL ` RVA 0x347C5B80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3121ffd7873ff07b](../../evidence/conditions-sets-019.md#c-3121ffd7873ff07b) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-036205

```text
(config)# default ip nat settings nonpatdrop <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 26 `；EOL ` RVA 0x347C6EF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-edb056f983fabd08](../../evidence/conditions-sets-092.md#c-edb056f983fabd08) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-036272

```text
(config)# default ip nat settings nonpatlog-disable <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 27 `；EOL ` RVA 0x347C71F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-798213ada1ffaa6d](../../evidence/conditions-sets-047.md#c-798213ada1ffaa6d) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-036054

```text
(config)# default ip nat settings pap <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 22 `；EOL ` RVA 0x347C6718 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ed94d21f75d40cc2](../../evidence/conditions-sets-092.md#c-ed94d21f75d40cc2) · [状态效果 S-c8e213dca765213a](../../evidence/state_effects-sets-043.md#s-c8e213dca765213a)

### path-045825

```text
(config)# default ip nat settings pool watermark <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 31 `；EOL ` RVA 0x347C7E70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e6a709c68427f6c7](../../evidence/conditions-sets-089.md#c-e6a709c68427f6c7) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-036754

```text
(config)# default ip nat settings preserve-sdwan-ports <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 38 `；EOL ` RVA 0x347C9578 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e7e98e8f00dcbcd0](../../evidence/conditions-sets-090.md#c-e7e98e8f00dcbcd0) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-045180

```text
(config)# default ip nat settings redundancy optimized-data-sync <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 41 `；EOL ` RVA 0x347C54D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b3bd65386fb35717](../../evidence/conditions-sets-070.md#c-b3bd65386fb35717) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-036661

```text
(config)# default ip nat settings reserve-ports <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 37 `；EOL ` RVA 0x347C8F90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8f18383cb6b8690b](../../evidence/conditions-sets-055.md#c-8f18383cb6b8690b) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-045931

```text
(config)# default ip nat settings scale bind <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 33 `；EOL ` RVA 0x347C8668 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6d1548220ab3a5b0](../../evidence/conditions-sets-042.md#c-6d1548220ab3a5b0) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-036455

```text
(config)# default ip nat settings trans-err-limit <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 32 `；EOL ` RVA 0x347C82B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-40af4ca7ce280927](../../evidence/conditions-sets-025.md#c-40af4ca7ce280927) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-045259

```text
(config)# default ip nat switchover replication http <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 19 `；EOL ` RVA 0x347C9A50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4b41c130e7d790d2](../../evidence/conditions-sets-030.md#c-4b41c130e7d790d2) · [状态效果 S-89b46cb673411e39](../../evidence/state_effects-sets-029.md#s-89b46cb673411e39)

### path-036452

```text
(config)# default ip nat translation dns-timeout <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 0 `；EOL ` RVA 0x347CC190 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-49cd3b9fb223e2e0](../../evidence/conditions-sets-029.md#c-49cd3b9fb223e2e0) · [状态效果 S-089116080cc32987](../../evidence/state_effects-sets-002.md#s-089116080cc32987)

### path-036269

```text
(config)# default ip nat translation finrst-timeout <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 0 `；EOL ` RVA 0x347CC0E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0f620700022683c8](../../evidence/conditions-sets-006.md#c-0f620700022683c8) · [状态效果 S-633bf0bf54ede991](../../evidence/state_effects-sets-021.md#s-633bf0bf54ede991)

### path-036509

```text
(config)# default ip nat translation icmp-timeout <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 0 `；EOL ` RVA 0x347CCFB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-799c85530dbb9462](../../evidence/conditions-sets-047.md#c-799c85530dbb9462) · [状态效果 S-4f8579d3d33087dd](../../evidence/state_effects-sets-017.md#s-4f8579d3d33087dd)

### path-045953

```text
(config)# default ip nat translation max-entries <number:1..2147483647> <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 8 `；EOL ` RVA 0x347CD848 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Number of entries。

[条件 C-7f9db0835c3f1ae7](../../evidence/conditions-sets-049.md#c-7f9db0835c3f1ae7) · [参数 P-f61f3cefbdeeee1c](../../evidence/parameters-sets-018.md#p-f61f3cefbdeeee1c) · [状态效果 S-cec340fb03e6bb60](../../evidence/state_effects-sets-044.md#s-cec340fb03e6bb60)

### path-053426

```text
(config)# default ip nat translation port-timeout tcp <number:1..65535> <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 1 `；EOL ` RVA 0x347CD460 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Port number。

[条件 C-ce7b9a61cbc87b62](../../evidence/conditions-sets-080.md#c-ce7b9a61cbc87b62) · [参数 P-cb7ab74e536edf65](../../evidence/parameters-sets-015.md#p-cb7ab74e536edf65) · [状态效果 S-8ecf738d84074261](../../evidence/state_effects-sets-030.md#s-8ecf738d84074261)

### path-036203

```text
(config)# default ip nat translation pptp-timeout <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 0 `；EOL ` RVA 0x347CE3F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-55d72f1b8b7498ff](../../evidence/conditions-sets-034.md#c-55d72f1b8b7498ff) · [状态效果 S-211240947e659c39](../../evidence/state_effects-sets-007.md#s-211240947e659c39)

### path-036508

```text
(config)# default ip nat translation routemap-entry-timeout <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 0 `；EOL ` RVA 0x347CCBC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-27f0d50b12690dd3](../../evidence/conditions-sets-016.md#c-27f0d50b12690dd3) · [状态效果 S-71b1936cc3e9ae48](../../evidence/state_effects-sets-024.md#s-71b1936cc3e9ae48)

### path-036333

```text
(config)# default ip nat translation syn-timeout <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 0 `；EOL ` RVA 0x347CC748 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-bafd06c8befa32a3](../../evidence/conditions-sets-072.md#c-bafd06c8befa32a3) · [状态效果 S-e02d95475a153b16](../../evidence/state_effects-sets-047.md#s-e02d95475a153b16)

### path-036050

```text
(config)# default ip nat translation tcp-timeout <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 0 `；EOL ` RVA 0x347CB8B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0de1a29bb6606655](../../evidence/conditions-sets-006.md#c-0de1a29bb6606655) · [状态效果 S-c1b3cb57fba20ed2](../../evidence/state_effects-sets-041.md#s-c1b3cb57fba20ed2)

### path-035972

```text
(config)# default ip nat translation timeout <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 0 `；EOL ` RVA 0x347CB4C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-61890a3e61645547](../../evidence/conditions-sets-038.md#c-61890a3e61645547) · [状态效果 S-5c71602c13209e09](../../evidence/state_effects-sets-020.md#s-5c71602c13209e09)

### path-036202

```text
(config)# default ip nat translation udp-timeout <cr>
```

Handler ` RVA 0xFA23030 `；selector ` 0 `；EOL ` RVA 0x347CBCF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db80c33013290b0d](../../evidence/conditions-sets-084.md#c-db80c33013290b0d) · [状态效果 S-fb78a7df4c771899](../../evidence/state_effects-sets-053.md#s-fb78a7df4c771899)

### path-036013

```text
(config)# default ip nbar attribute-map <string> <cr>
```

Handler ` RVA 0x10F24CF0 `；selector ` 8 `；EOL ` RVA 0x35240410 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Attribute Profile Name - cannot exceed 20 characters。

[条件 C-36baca6458b62948](../../evidence/conditions-sets-021.md#c-36baca6458b62948) · [参数 P-bbd0d50663444514](../../evidence/parameters-sets-014.md#p-bbd0d50663444514) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-045590

```text
(config)# default ip nbar classification auto-learn top-hosts <cr>
```

Handler ` RVA 0x10F24CF0 `；selector ` 14 `；EOL ` RVA 0x3523C5B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-bcc82ce1f4b03257](../../evidence/conditions-sets-073.md#c-bcc82ce1f4b03257) · [状态效果 S-b06d816430676256](../../evidence/state_effects-sets-037.md#s-b06d816430676256)

### path-057246

```text
(config)# default ip nbar classification auto-learn top-hosts sample-rate <number:1..8192> <cr>
```

Handler ` RVA 0x10F24CF0 `；selector ` 15 `；EOL ` RVA 0x3523C5F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` sampler rate。

[条件 C-bcc82ce1f4b03257](../../evidence/conditions-sets-073.md#c-bcc82ce1f4b03257) · [参数 P-a88c83ad3ce43f20](../../evidence/parameters-sets-013.md#p-a88c83ad3ce43f20) · [状态效果 S-b06d816430676256](../../evidence/state_effects-sets-037.md#s-b06d816430676256)

### path-045623

```text
(config)# default ip nbar classification dns classify-by-domain <cr>
```

Handler ` RVA 0x10F24CF0 `；selector ` 18 `；EOL ` RVA 0x3523D6C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d2361e69af884636](../../evidence/conditions-sets-081.md#c-d2361e69af884636) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-045774

```text
(config)# default ip nbar classification dns learning <cr>
```

Handler ` RVA 0x10F24CF0 `；selector ` 16 `；EOL ` RVA 0x3523D1A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d2361e69af884636](../../evidence/conditions-sets-081.md#c-d2361e69af884636) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-053158

```text
(config)# default ip nbar classification dns learning cache-ttl-zero <cr>
```

Handler ` RVA 0x10F24CF0 `；selector ` 17 `；EOL ` RVA 0x3523CED8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d2361e69af884636](../../evidence/conditions-sets-081.md#c-d2361e69af884636) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-053209

```text
(config)# default ip nbar classification dns learning domains <cr>
```

Handler ` RVA 0x10F24CF0 `；selector ` 20 `；EOL ` RVA 0x3523D180 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d2361e69af884636](../../evidence/conditions-sets-081.md#c-d2361e69af884636) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-053111

```text
(config)# default ip nbar classification dns learning guard <cr>
```

Handler ` RVA 0x10F24CF0 `；selector ` 19 `；EOL ` RVA 0x3523CC30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d2361e69af884636](../../evidence/conditions-sets-081.md#c-d2361e69af884636) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-036053

```text
(config)# default ip nbar classification granularity <cr>
```

Handler ` RVA 0x10F24CF0 `；selector ` 6 `；EOL ` RVA 0x3523BFB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-068eac01500ceba0](../../evidence/conditions-sets-003.md#c-068eac01500ceba0) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-045346

```text
(config)# default ip nbar classification ip-traffic all-caches <cr>
```

Handler ` RVA 0x10F24CF0 `；selector ` 40 `；EOL ` RVA 0x3523B670 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0b245294fadc8583](../../evidence/conditions-sets-005.md#c-0b245294fadc8583) · [状态效果 S-008aeb2a725a9e5a](../../evidence/state_effects-sets-001.md#s-008aeb2a725a9e5a)

### path-036181

```text
(config)# default ip nbar classification multi-vrf <cr>
```

Handler ` RVA 0x10F24CF0 `；selector ` 24 `；EOL ` RVA 0x3523D998 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-42696176c897ebac](../../evidence/conditions-sets-026.md#c-42696176c897ebac) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-045404

```text
(config)# default ip nbar classification tunneled-traffic ipv6inip <cr>
```

Handler ` RVA 0x10F24CF0 `；selector ` 5 `；EOL ` RVA 0x3523B9F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-98fa03775bf9951f](../../evidence/conditions-sets-059.md#c-98fa03775bf9951f) · [状态效果 S-69a9302f6a5d5bfc](../../evidence/state_effects-sets-023.md#s-69a9302f6a5d5bfc)

### path-035766

```text
(config)# default ip nbar disable custom-async <cr>
```

Handler ` RVA 0x10F24CF0 `；selector ` 23 `；EOL ` RVA 0x3523AD30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8c619aeac51f093c](../../evidence/conditions-sets-054.md#c-8c619aeac51f093c) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-035705

```text
(config)# default ip nbar disable encrypted-app <cr>
```

Handler ` RVA 0x10F24CF0 `；selector ` 2 `；EOL ` RVA 0x3523AA50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-04702889663e37a2](../../evidence/conditions-sets-002.md#c-04702889663e37a2) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-035834

```text
(config)# default ip nbar disable sc-hit-vm-handler <cr>
```

Handler ` RVA 0x10F24CF0 `；selector ` 44 `；EOL ` RVA 0x3523AFE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad7cfeb564d82c84](../../evidence/conditions-sets-067.md#c-ad7cfeb564d82c84) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-029608

```text
(config)# default ip nbar http-services <cr>
```

Handler ` RVA 0x10F24CF0 `；selector ` 22 `；EOL ` RVA 0x3523B2F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d2361e69af884636](../../evidence/conditions-sets-081.md#c-d2361e69af884636) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-035658

```text
(config)# default ip nbar protocol-map <string> <cr>
```

Handler ` RVA 0x10F24CF0 `；selector ` 41 `；EOL ` RVA 0x3523A190 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` protocol name。

[条件 C-b9cb5e5a6b372678](../../evidence/conditions-sets-072.md#c-b9cb5e5a6b372678) · [参数 P-0c6cc3c0017ed9ee](../../evidence/parameters-sets-001.md#p-0c6cc3c0017ed9ee) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-029573

```text
(config)# default ip nbar protocol-pack <cr>
```

Handler ` RVA 0x10F24CF0 `；selector ` 3 `；EOL ` RVA 0x35239AF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-59d88e62629ad524](../../evidence/conditions-sets-035.md#c-59d88e62629ad524) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-026601

```text
(config)# default ip nsf-converge <cr>
```

Handler ` RVA 0xE1FAC50 `；selector ` 2 `；EOL ` RVA 0x3423D4E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-212a7ad73e73f1bb](../../evidence/conditions-sets-013.md#c-212a7ad73e73f1bb) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-026819

```text
(config)# default ip options <cr>
```

Handler ` RVA 0xCF2A810 `；selector ` 14 `；EOL ` RVA 0x33D3A090 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-24d3dcddfbad1f2f](../../evidence/conditions-sets-014.md#c-24d3dcddfbad1f2f) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-028966

```text
(config)# default ip ospf name-lookup <cr>
```

Handler ` RVA 0xFC67B00 `；selector ` 0 `；EOL ` RVA 0x34881C98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-029558

```text
(config)# default ip pim accept-register <cr>
```

Handler ` RVA 0xF810790 `；selector ` 26 `；EOL ` RVA 0x3475EA80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ea79108aa5d707a5](../../evidence/conditions-sets-091.md#c-ea79108aa5d707a5) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-035220

```text
(config)# default ip pim accept-rp auto-rp <cr>
```

Handler ` RVA 0xF810790 `；selector ` 9 `；EOL ` RVA 0x3475BE50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c7b9f8bbb48d4273](../../evidence/conditions-sets-077.md#c-c7b9f8bbb48d4273) · [状态效果 S-6c719c097685d25c](../../evidence/state_effects-sets-023.md#s-6c719c097685d25c)

### path-029905

```text
(config)# default ip pim allow-rp <cr>
```

Handler ` RVA 0xF810790 `；selector ` 66 `；EOL ` RVA 0x34760580 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-866aa7c12a394f57](../../evidence/conditions-sets-052.md#c-866aa7c12a394f57) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-028939

```text
(config)# default ip pim autorp <cr>
```

Handler ` RVA 0xF810790 `；selector ` 62 `；EOL ` RVA 0x34759DB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-63db2e88a69e048f](../../evidence/conditions-sets-039.md#c-63db2e88a69e048f) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-034985

```text
(config)# default ip pim autorp listener <cr>
```

Handler ` RVA 0xF810790 `；selector ` 47 `；EOL ` RVA 0x34759D90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-63db2e88a69e048f](../../evidence/conditions-sets-039.md#c-63db2e88a69e048f) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-028572

```text
(config)# default ip pim bidir-enable <cr>
```

Handler ` RVA 0xF810790 `；selector ` 45 `；EOL ` RVA 0x34757278 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f2e03679db599380](../../evidence/conditions-sets-094.md#c-f2e03679db599380) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-028795

```text
(config)# default ip pim bidir-offer-interval <cr>
```

Handler ` RVA 0xF810790 `；selector ` 30 `；EOL ` RVA 0x34758FA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c22a6d3eb243199c](../../evidence/conditions-sets-075.md#c-c22a6d3eb243199c) · [状态效果 S-d6b7f930b4f3f246](../../evidence/state_effects-sets-046.md#s-d6b7f930b4f3f246)

### path-029170

```text
(config)# default ip pim bsr-candidate <cr>
```

Handler ` RVA 0xF810790 `；selector ` 19 `；EOL ` RVA 0x3475C270 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e8f6bde05799b261](../../evidence/conditions-sets-090.md#c-e8f6bde05799b261) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-034878

```text
(config)# default ip pim cache rpf-oif <cr>
```

Handler ` RVA 0xF810790 `；selector ` 88 `；EOL ` RVA 0x347597F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-63db2e88a69e048f](../../evidence/conditions-sets-039.md#c-63db2e88a69e048f) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-028832

```text
(config)# default ip pim dm-fallback <cr>
```

Handler ` RVA 0xF810790 `；selector ` 53 `；EOL ` RVA 0x34758C20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1c1d4d7eb6586ba0](../../evidence/conditions-sets-011.md#c-1c1d4d7eb6586ba0) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-029396

```text
(config)# default ip pim fast-register-stop <cr>
```

Handler ` RVA 0xF810790 `；selector ` 16 `；EOL ` RVA 0x3475E018 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-45f3be2e8de815ec](../../evidence/conditions-sets-027.md#c-45f3be2e8de815ec) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-029644

```text
(config)# default ip pim log-neighbor-changes <cr>
```

Handler ` RVA 0xF810790 `；selector ` 54 `；EOL ` RVA 0x3475F6A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-21d0519a794d6b68](../../evidence/conditions-sets-013.md#c-21d0519a794d6b68) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-045316

```text
(config)# default ip pim maximum group-mappings autorp <cr>
```

Handler ` RVA 0xF810790 `；selector ` 63 `；EOL ` RVA 0x3475EF80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e55ea1d82cfc1b66](../../evidence/conditions-sets-088.md#c-e55ea1d82cfc1b66) · [状态效果 S-0e7b3ca1a2899648](../../evidence/state_effects-sets-003.md#s-0e7b3ca1a2899648)

### path-058998

```text
(config)# default ip pim mofrr clone join <address> mask-length <number:0..32> <cr>
```

Handler ` RVA 0xF810790 `；selector ` 75 `；EOL ` RVA 0x34758128 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` Source address to translate；` unsigned_number ` Mask length for translation。

[条件 C-7c8b21ef8f46f8c3](../../evidence/conditions-sets-048.md#c-7c8b21ef8f46f8c3) · [参数 P-909a4c1215786d08](../../evidence/parameters-sets-011.md#p-909a4c1215786d08) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-058991

```text
(config)# default ip pim mofrr clone source <address> mask-length <number:0..32> <cr>
```

Handler ` RVA 0xF810790 `；selector ` 74 `；EOL ` RVA 0x34757C90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` Source address to translate；` unsigned_number ` Mask length for translation。

[条件 C-badafcb995c37cab](../../evidence/conditions-sets-072.md#c-badafcb995c37cab) · [参数 P-71fe80b6d6767cb0](../../evidence/parameters-sets-009.md#p-71fe80b6d6767cb0) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-034818

```text
(config)# default ip pim mofrr flow <cr>
```

Handler ` RVA 0xF810790 `；selector ` 73 `；EOL ` RVA 0x34757690 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-df1a83b8076f35c6](../../evidence/conditions-sets-086.md#c-df1a83b8076f35c6) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-028772

```text
(config)# default ip pim old-register-checksum <cr>
```

Handler ` RVA 0xF810790 `；selector ` 61 `；EOL ` RVA 0x34758978 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1c1d4d7eb6586ba0](../../evidence/conditions-sets-011.md#c-1c1d4d7eb6586ba0) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-035176

```text
(config)# default ip pim pfp-sa announce <cr>
```

Handler ` RVA 0xF810790 `；selector ` 80 `；EOL ` RVA 0x3475AA58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9e7f2db4cb2dd129](../../evidence/conditions-sets-061.md#c-9e7f2db4cb2dd129) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-035276

```text
(config)# default ip pim pfp-sa cache <cr>
```

Handler ` RVA 0xF810790 `；selector ` 85 `；EOL ` RVA 0x3475B4F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d31aef09d0bf98f0](../../evidence/conditions-sets-081.md#c-d31aef09d0bf98f0) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-044903

```text
(config)# default ip pim pfp-sa timers holdtime <cr>
```

Handler ` RVA 0xF810790 `；selector ` 81 `；EOL ` RVA 0x3475AEF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b95009e7ebe07eb1](../../evidence/conditions-sets-072.md#c-b95009e7ebe07eb1) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-044934

```text
(config)# default ip pim pfp-sa timers interval <cr>
```

Handler ` RVA 0xF810790 `；selector ` 82 `；EOL ` RVA 0x3475B1E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-08ff62680e107cae](../../evidence/conditions-sets-004.md#c-08ff62680e107cae) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-029446

```text
(config)# default ip pim register-rate-limit <cr>
```

Handler ` RVA 0xF810790 `；selector ` 24 `；EOL ` RVA 0x3475E310 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db21375bc1395eb0](../../evidence/conditions-sets-084.md#c-db21375bc1395eb0) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-029503

```text
(config)# default ip pim register-source <cr>
```

Handler ` RVA 0xF810790 `；selector ` 28 `；EOL ` RVA 0x3475E6B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-aca25644362536ea](../../evidence/conditions-sets-067.md#c-aca25644362536ea) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-035078

```text
(config)# default ip pim rp-address <address> <cr>
```

Handler ` RVA 0xF810790 `；selector ` 1 `；EOL ` RVA 0x3475A360 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IP address of Rendezvous-point for group。

[条件 C-095b98b43e7aaff4](../../evidence/conditions-sets-004.md#c-095b98b43e7aaff4) · [参数 P-11c19964b1ed5fc8](../../evidence/parameters-sets-002.md#p-11c19964b1ed5fc8) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-029361

```text
(config)# default ip pim rp-announce-filter <cr>
```

Handler ` RVA 0xF810790 `；selector ` 15 `；EOL ` RVA 0x3475D068 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f11aeac7f1fc2a24](../../evidence/conditions-sets-093.md#c-f11aeac7f1fc2a24) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-028833

```text
(config)# default ip pim rp-proxy-join <cr>
```

Handler ` RVA 0xF810790 `；selector ` 25 `；EOL ` RVA 0x34759A80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-63db2e88a69e048f](../../evidence/conditions-sets-039.md#c-63db2e88a69e048f) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-035548

```text
(config)# default ip pim send-rp-announce <address> <cr>
```

Handler ` RVA 0xF810790 `；selector ` 13 `；EOL ` RVA 0x3475D530 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IP address of RP for group。

[条件 C-eb78b36b50f62696](../../evidence/conditions-sets-091.md#c-eb78b36b50f62696) · [参数 P-a363a8d37781f4ea](../../evidence/parameters-sets-012.md#p-a363a8d37781f4ea) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-029352

```text
(config)# default ip pim send-rp-discovery <cr>
```

Handler ` RVA 0xF810790 `；selector ` 14 `；EOL ` RVA 0x3475DB48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5a9e6dbf098aca63](../../evidence/conditions-sets-035.md#c-5a9e6dbf098aca63) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-036045

```text
(config)# default ip pim sparse accept-source-reports <cr>
```

Handler ` RVA 0xF810790 `；selector ` 40 `；EOL ` RVA 0x3475FEA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-23006feb1fa68ba3](../../evidence/conditions-sets-014.md#c-23006feb1fa68ba3) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-035963

```text
(config)# default ip pim sparse sg-expiry-timer <cr>
```

Handler ` RVA 0xF810790 `；selector ` 58 `；EOL ` RVA 0x3475FA40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3d8bb253fba7a600](../../evidence/conditions-sets-024.md#c-3d8bb253fba7a600) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-035177

```text
(config)# default ip pim spt-threshold 0 <cr>
```

Handler ` RVA 0xF810790 `；selector ` 8 `；EOL ` RVA 0x3475B978 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-21d0519a794d6b68](../../evidence/conditions-sets-013.md#c-21d0519a794d6b68) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-029653

```text
(config)# default ip pim ssm <cr>
```

Handler ` RVA 0xF810790 `；selector ` 35 `；EOL ` RVA 0x3475F2E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b208dfe9aab4bdab](../../evidence/conditions-sets-069.md#c-b208dfe9aab4bdab) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-034833

```text
(config)# default ip pim state-refresh disable <cr>
```

Handler ` RVA 0xF810790 `；selector ` 38 `；EOL ` RVA 0x347594F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-63db2e88a69e048f](../../evidence/conditions-sets-039.md#c-63db2e88a69e048f) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-029738

```text
(config)# default ip pim v1-rp-reachability <cr>
```

Handler ` RVA 0xF810790 `；selector ` 56 `；EOL ` RVA 0x34760230 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-21d0519a794d6b68](../../evidence/conditions-sets-013.md#c-21d0519a794d6b68) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-034635

```text
(config)# default ip policy-list <string> permit <cr>
```

Handler ` RVA 0xE222AD0 `；selector ` 0 `；EOL ` RVA 0x344CC430 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` IP Policy list name。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [参数 P-e006b5636d1218eb](../../evidence/parameters-sets-017.md#p-e006b5636d1218eb) · [状态效果 S-0a5c9250e73fe176](../../evidence/state_effects-sets-003.md#s-0a5c9250e73fe176)

### path-026547

```text
(config)# default ip portbundle <cr>
```

Handler ` RVA 0x11C30260 `；selector ` 0 `；EOL ` RVA 0x356A5468 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-029865

```text
(config)# default ip prefix-list <string> <cr>
```

Handler ` RVA 0xE21E820 `；selector ` 0 `；EOL ` RVA 0x342828B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Name of a prefix list。

[条件 C-ef81943334c4fd37](../../evidence/conditions-sets-092.md#c-ef81943334c4fd37) · [参数 P-ba56a54852b2cae0](../../evidence/parameters-sets-014.md#p-ba56a54852b2cae0) · [状态效果 S-09b376f7d7e3d525](../../evidence/state_effects-sets-002.md#s-09b376f7d7e3d525)

### path-029472

```text
(config)# default ip prefix-list sequence-number <cr>
```

Handler ` RVA 0xE21E820 `；selector ` 0 `；EOL ` RVA 0x342821B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [状态效果 S-161d1a67b950f9ff](../../evidence/state_effects-sets-005.md#s-161d1a67b950f9ff)

### path-028375

```text
(config)# default ip rcmd domain-lookup <cr>
```

Handler ` RVA 0xCFFFEF0 `；selector ` 3 `；EOL ` RVA 0x33D7BC68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-028457

```text
(config)# default ip rcmd rcp-enable <cr>
```

Handler ` RVA 0xCFFFEF0 `；selector ` 5 `；EOL ` RVA 0x33D7BF78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-052462

```text
(config)# default ip rcmd remote-host <string> <number:1..99> <string> <cr>
```

Handler ` RVA 0xCFFFEF0 `；selector ` 2 `；EOL ` RVA 0x33D7CA30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Local username；` unsigned_number ` Access list number；` string ` Remote username。

[条件 C-d295f102cfe702ea](../../evidence/conditions-sets-081.md#c-d295f102cfe702ea) · [参数 P-cf26ffcd1ce3a747](../../evidence/parameters-sets-016.md#p-cf26ffcd1ce3a747) · [状态效果 S-92f0f407f65f3372](../../evidence/state_effects-sets-031.md#s-92f0f407f65f3372)

### path-028602

```text
(config)# default ip rcmd remote-username <cr>
```

Handler ` RVA 0xCFFFEF0 `；selector ` 1 `；EOL ` RVA 0x33D7CE30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-581a30bb1a93ec4c](../../evidence/conditions-sets-035.md#c-581a30bb1a93ec4c) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-034581

```text
(config)# default ip rcmd rsh-disable-command <string> <cr>
```

Handler ` RVA 0xCFFFEF0 `；selector ` 6 `；EOL ` RVA 0x33D7C570 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [参数 P-1d40cf10fb3b7071](../../evidence/parameters-sets-003.md#p-1d40cf10fb3b7071) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-028478

```text
(config)# default ip rcmd rsh-enable <cr>
```

Handler ` RVA 0xCFFFEF0 `；selector ` 4 `；EOL ` RVA 0x33D7C258 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-028639

```text
(config)# default ip rcmd source-interface <cr>
```

Handler ` RVA 0xCFFFEF0 `；selector ` 0 `；EOL ` RVA 0x33D7D150 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-118717b21c9d51c9](../../evidence/conditions-sets-007.md#c-118717b21c9d51c9) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-030161

```text
(config)# default ip reflexive-list timeout <cr>
```

Handler ` RVA 0xF9C1E90 `；selector ` 0 `；EOL ` RVA 0x3479B210 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-25a63b7f561b2485](../../evidence/conditions-sets-015.md#c-25a63b7f561b2485) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-035786

```text
(config)# default ip rsvp aggregation ip <cr>
```

Handler ` RVA 0x101C30A0 `；selector ` 0 `；EOL ` RVA 0x34A685F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-045325

```text
(config)# default ip rsvp aggregation ip level <cr>
```

Handler ` RVA 0x101C3940 `；selector ` 0 `；EOL ` RVA 0x34A68340 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-468d49ae651c6316](../../evidence/conditions-sets-028.md#c-468d49ae651c6316) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-052900

```text
(config)# default ip rsvp aggregation ip map any <cr>
```

Handler ` RVA 0x101C35A0 `；selector ` 0 `；EOL ` RVA 0x34A676E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-eeb9c76be5fd6ce5](../../evidence/conditions-sets-092.md#c-eeb9c76be5fd6ce5) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-052993

```text
(config)# default ip rsvp aggregation ip sender service <cr>
```

Handler ` RVA 0x101C3A90 `；selector ` 0 `；EOL ` RVA 0x34A686D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-fa06060abd98ce73](../../evidence/conditions-sets-097.md#c-fa06060abd98ce73) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-029813

```text
(config)# default ip rsvp authentication <cr>
```

Handler ` RVA 0x10073550 `；selector ` 10 `；EOL ` RVA 0x34A439B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ab4c1b3cef308834](../../evidence/conditions-sets-066.md#c-ab4c1b3cef308834) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-035978

```text
(config)# default ip rsvp authentication challenge <cr>
```

Handler ` RVA 0x10073550 `；selector ` 8 `；EOL ` RVA 0x34A43728 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-dcac3ba3fb4253b6](../../evidence/conditions-sets-085.md#c-dcac3ba3fb4253b6) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-035716

```text
(config)# default ip rsvp authentication key-chain <cr>
```

Handler ` RVA 0x10073550 `；selector ` 12 `；EOL ` RVA 0x34A428F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d8d63ac3bc5708cd](../../evidence/conditions-sets-083.md#c-d8d63ac3bc5708cd) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-035906

```text
(config)# default ip rsvp authentication lifetime <cr>
```

Handler ` RVA 0x10073550 `；selector ` 9 `；EOL ` RVA 0x34A43408 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b69f86fcf5783c1c](../../evidence/conditions-sets-071.md#c-b69f86fcf5783c1c) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-035986

```text
(config)# default ip rsvp authentication type <cr>
```

Handler ` RVA 0x10073550 `；selector ` 7 `；EOL ` RVA 0x34A43020 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5b770cb8a08a09b2](../../evidence/conditions-sets-036.md#c-5b770cb8a08a09b2) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-035841

```text
(config)# default ip rsvp authentication window-size <cr>
```

Handler ` RVA 0x10073550 `；selector ` 5 `；EOL ` RVA 0x34A42C78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b756d2b3a7bb3cf9](../../evidence/conditions-sets-071.md#c-b756d2b3a7bb3cf9) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-057338

```text
(config)# default ip rsvp listener <address> <number:0..255> <number:0..65535> announce <cr>
```

Handler ` RVA 0x1005E650 `；selector ` 0 `；EOL ` RVA 0x34A46B78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` Destination address；` unsigned_number ` IP Protocol；` unsigned_number ` Destination port。

[条件 C-0e1fdee263dd9cba](../../evidence/conditions-sets-006.md#c-0e1fdee263dd9cba) · [参数 P-8cbcf1b136e2c8b3](../../evidence/parameters-sets-011.md#p-8cbcf1b136e2c8b3) · [状态效果 S-789261a9917cc124](../../evidence/state_effects-sets-026.md#s-789261a9917cc124)

### path-029711

```text
(config)# default ip rsvp metadata <cr>
```

Handler ` RVA 0x10077B70 `；selector ` 0 `；EOL ` RVA 0x34A4CBC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-059749

```text
(config)# default ip rsvp metadata sender-host <address> <address> <number:0..255> <number:0..65535> <number:0..65535> <cr>
```

Handler ` RVA 0x10077C60 `；selector ` 0 `；EOL ` RVA 0x34A4CEE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` Destination address；` address ` Source address；` unsigned_number ` IP Protocol；` unsigned_number ` Destination port；` unsigned_number ` Source port。

[条件 C-ddbbd97d6c600413](../../evidence/conditions-sets-085.md#c-ddbbd97d6c600413) · [参数 P-f430d883716a98a9](../../evidence/parameters-sets-018.md#p-f430d883716a98a9) · [状态效果 S-ed8fe77e56534217](../../evidence/state_effects-sets-050.md#s-ed8fe77e56534217)

### path-035736

```text
(config)# default ip rsvp metadata statistics <cr>
```

Handler ` RVA 0x100783D0 `；selector ` 0 `；EOL ` RVA 0x34A4C8F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-030133

```text
(config)# default ip rsvp msg-pacing <cr>
```

Handler ` RVA 0x10070FD0 `；selector ` 0 `；EOL ` RVA 0x34A472B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0e1fdee263dd9cba](../../evidence/conditions-sets-006.md#c-0e1fdee263dd9cba) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-035769

```text
(config)# default ip rsvp policy default-reject <cr>
```

Handler ` RVA 0x10113260 `；selector ` 0 `；EOL ` RVA 0x34A416A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e5d040cadd4659a2](../../evidence/conditions-sets-089.md#c-e5d040cadd4659a2) · [状态效果 S-49e661ffa8a1b7f0](../../evidence/state_effects-sets-016.md#s-49e661ffa8a1b7f0)

### path-045256

```text
(config)# default ip rsvp policy identity <string> <cr>
```

Handler ` RVA 0x10113AC0 `；selector ` 0 `；EOL ` RVA 0x34A412F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Alias for use in other CLI commands (quotes allowed)。

[条件 C-9af7ca21ba0f19ec](../../evidence/conditions-sets-060.md#c-9af7ca21ba0f19ec) · [参数 P-296bf290e31a3f4f](../../evidence/parameters-sets-004.md#p-296bf290e31a3f4f) · [状态效果 S-49e661ffa8a1b7f0](../../evidence/state_effects-sets-016.md#s-49e661ffa8a1b7f0)

### path-045408

```text
(config)# default ip rsvp policy local default <cr>
```

Handler ` RVA 0x101134B0 `；selector ` 257 `；EOL ` RVA 0x34A41D18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4468f9f696c3dd63](../../evidence/conditions-sets-027.md#c-4468f9f696c3dd63) · [状态效果 S-2fd15d2c1e1b35f5](../../evidence/state_effects-sets-011.md#s-2fd15d2c1e1b35f5)

### path-035898

```text
(config)# default ip rsvp policy preempt <cr>
```

Handler ` RVA 0x10113340 `；selector ` 0 `；EOL ` RVA 0x34A419C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-09b8a62e50b3e9c5](../../evidence/conditions-sets-004.md#c-09b8a62e50b3e9c5) · [状态效果 S-49e661ffa8a1b7f0](../../evidence/state_effects-sets-016.md#s-49e661ffa8a1b7f0)

### path-029567

```text
(config)# default ip rsvp pq-profile <cr>
```

Handler ` RVA 0x10054960 `；selector ` 0 `；EOL ` RVA 0x34A43D40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-fb881d24c82cb8a7](../../evidence/conditions-sets-097.md#c-fb881d24c82cb8a7) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-030081

```text
(config)# default ip rsvp qos <cr>
```

Handler ` RVA 0x10077270 `；selector ` 0 `；EOL ` RVA 0x34A4C590 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6c279dcac619e81b](../../evidence/conditions-sets-042.md#c-6c279dcac619e81b) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-060199

```text
(config)# default ip rsvp reservation <address> <address> <number:0..255> <number:0..65535> <number:0..65535> wf load <number:1..10000000> <number:1..65535> <cr>
```

Handler ` RVA 0x10059EB0 `；selector ` 0 `；EOL ` RVA 0x34A46428 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` Destination address；` address ` Source address；` unsigned_number ` IP Protocol；` unsigned_number ` Destination port；` unsigned_number ` Source port；` unsigned_number ` Average Bit Rate to reserve (kbps)；` unsigned_number ` Maximum Burst in Kilobytes。

[条件 C-bb1a7866ded119ba](../../evidence/conditions-sets-072.md#c-bb1a7866ded119ba) · [参数 P-68894bfe840994a4](../../evidence/parameters-sets-008.md#p-68894bfe840994a4) · [状态效果 S-a952ffc065b80bd8](../../evidence/state_effects-sets-036.md#s-a952ffc065b80bd8)

### path-060024

```text
(config)# default ip rsvp sender <address> <address> <number:0..255> <number:0..65535> <number:0..65535> <number:1..10000000> <number:1..65535> <cr>
```

Handler ` RVA 0x1005AFF0 `；selector ` 0 `；EOL ` RVA 0x34A457D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` Destination address；` address ` Source address；` unsigned_number ` IP Protocol；` unsigned_number ` Destination port；` unsigned_number ` Source port；` unsigned_number ` Average Bit Rate to reserve (kbps)；` unsigned_number ` Maximum Burst in Kilobytes。

[条件 C-061b76ea09df04f1](../../evidence/conditions-sets-003.md#c-061b76ea09df04f1) · [参数 P-73daa0f5da215834](../../evidence/parameters-sets-009.md#p-73daa0f5da215834) · [状态效果 S-a4ae4a68d5447fe8](../../evidence/state_effects-sets-035.md#s-a4ae4a68d5447fe8)

### path-060029

```text
(config)# default ip rsvp sender <address> <address> <number:0..255> <number:0..65535> <number:0..65535> <number:1..10000000> <number:1..65535> <cr>
```

Handler ` RVA 0x1005C360 `；selector ` 0 `；EOL ` RVA 0x34A454C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` Destination address；` address ` Source address；` unsigned_number ` IP Protocol；` unsigned_number ` Destination port；` unsigned_number ` Source port；` unsigned_number ` Average Bit Rate to reserve (kbps)；` unsigned_number ` Maximum Burst in Kilobytes。

[条件 C-fffe20e206279b23](../../evidence/conditions-sets-099.md#c-fffe20e206279b23) · [参数 P-73daa0f5da215834](../../evidence/parameters-sets-009.md#p-73daa0f5da215834) · [状态效果 S-a4ae4a68d5447fe8](../../evidence/state_effects-sets-035.md#s-a4ae4a68d5447fe8)

### path-045930

```text
(config)# default ip rsvp signalling fast-local-repair notifications <cr>
```

Handler ` RVA 0x10056150 `；selector ` 0 `；EOL ` RVA 0x34A47AA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c3ff9f0ab0483707](../../evidence/conditions-sets-076.md#c-c3ff9f0ab0483707) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-045979

```text
(config)# default ip rsvp signalling fast-local-repair rate <cr>
```

Handler ` RVA 0x10056050 `；selector ` 0 `；EOL ` RVA 0x34A47DC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1b41c076843ece42](../../evidence/conditions-sets-011.md#c-1b41c076843ece42) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-037040

```text
(config)# default ip rsvp signalling hello <cr>
```

Handler ` RVA 0x10074260 `；selector ` 0 `；EOL ` RVA 0x34A4AD28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ee70c5bde95b3ce5](../../evidence/conditions-sets-092.md#c-ee70c5bde95b3ce5) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-046401

```text
(config)# default ip rsvp signalling hello bfd <cr>
```

Handler ` RVA 0x10074350 `；selector ` 0 `；EOL ` RVA 0x34A4AA18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5924a81640a4c9be](../../evidence/conditions-sets-035.md#c-5924a81640a4c9be) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-046358

```text
(config)# default ip rsvp signalling hello cleanup-timer <cr>
```

Handler ` RVA 0x10077100 `；selector ` 0 `；EOL ` RVA 0x34A4A750 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3267b594985264c1](../../evidence/conditions-sets-020.md#c-3267b594985264c1) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-046185

```text
(config)# default ip rsvp signalling hello down <cr>
```

Handler ` RVA 0x10074670 `；selector ` 0 `；EOL ` RVA 0x34A49E18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3267b594985264c1](../../evidence/conditions-sets-020.md#c-3267b594985264c1) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-053972

```text
(config)# default ip rsvp signalling hello graceful-restart dscp <cr>
```

Handler ` RVA 0x10075E80 `；selector ` 4 `；EOL ` RVA 0x34A4B4C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6c7ef2b0f6b93575](../../evidence/conditions-sets-042.md#c-6c7ef2b0f6b93575) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-054007

```text
(config)# default ip rsvp signalling hello graceful-restart help-neighbor <cr>
```

Handler ` RVA 0x10075310 `；selector ` 0 `；EOL ` RVA 0x34A4BEF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-281c7465882f84dd](../../evidence/conditions-sets-016.md#c-281c7465882f84dd) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-057705

```text
(config)# default ip rsvp signalling hello graceful-restart refresh interval <cr>
```

Handler ` RVA 0x10075E80 `；selector ` 1 `；EOL ` RVA 0x34A4AE60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2f34122aa48ebef7](../../evidence/conditions-sets-018.md#c-2f34122aa48ebef7) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-057738

```text
(config)# default ip rsvp signalling hello graceful-restart refresh misses <cr>
```

Handler ` RVA 0x10075E80 `；selector ` 2 `；EOL ` RVA 0x34A4B150 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ea23f0ed771e250d](../../evidence/conditions-sets-090.md#c-ea23f0ed771e250d) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-057788

```text
(config)# default ip rsvp signalling hello graceful-restart send recovery-time <cr>
```

Handler ` RVA 0x100760E0 `；selector ` 0 `；EOL ` RVA 0x34A4B880 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0491be8a70490c30](../../evidence/conditions-sets-002.md#c-0491be8a70490c30) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-057813

```text
(config)# default ip rsvp signalling hello graceful-restart send restart-time <cr>
```

Handler ` RVA 0x10076040 `；selector ` 0 `；EOL ` RVA 0x34A4BB70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-56cac318ff53b04a](../../evidence/conditions-sets-034.md#c-56cac318ff53b04a) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-057561

```text
(config)# default ip rsvp signalling hello queue <number:1..200> <number:1..200> <cr>
```

Handler ` RVA 0x10076FA0 `；selector ` 0 `；EOL ` RVA 0x34A4A170 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` # of Hello msgs to process when RSVP wakes up；` unsigned_number ` # of RSVP msgs to process when RSVP wakes up。

[条件 C-3267b594985264c1](../../evidence/conditions-sets-020.md#c-3267b594985264c1) · [参数 P-10738022e58d9740](../../evidence/parameters-sets-002.md#p-10738022e58d9740) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-046184

```text
(config)# default ip rsvp signalling hello statistics <cr>
```

Handler ` RVA 0x10074570 `；selector ` 0 `；EOL ` RVA 0x34A49B70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-132998733aa5ee20](../../evidence/conditions-sets-008.md#c-132998733aa5ee20) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-053670

```text
(config)# default ip rsvp signalling hello timer <number:1..100> <cr>
```

Handler ` RVA 0x10077070 `；selector ` 0 `；EOL ` RVA 0x34A4A460 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` # of RSVP timers to process when RSVP wakes up。

[条件 C-3267b594985264c1](../../evidence/conditions-sets-020.md#c-3267b594985264c1) · [参数 P-2375db552f265c6f](../../evidence/parameters-sets-003.md#p-2375db552f265c6f) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-036659

```text
(config)# default ip rsvp signalling initial-retransmit-delay <cr>
```

Handler ` RVA 0x100704D0 `；selector ` 0 `；EOL ` RVA 0x34A48AE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2141c9c9d6d87833](../../evidence/conditions-sets-013.md#c-2141c9c9d6d87833) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-046024

```text
(config)# default ip rsvp signalling patherr state-removal <cr>
```

Handler ` RVA 0x10070AA0 `；selector ` 0 `；EOL ` RVA 0x34A48730 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-766ee226b9881824](../../evidence/conditions-sets-046.md#c-766ee226b9881824) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-036566

```text
(config)# default ip rsvp signalling rate-limit <cr>
```

Handler ` RVA 0x10070C50 `；selector ` 0 `；EOL ` RVA 0x34A48130 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9868c8b8a0aaa942](../../evidence/conditions-sets-059.md#c-9868c8b8a0aaa942) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-046160

```text
(config)# default ip rsvp signalling refresh interval <cr>
```

Handler ` RVA 0x100559D0 `；selector ` 0 `；EOL ` RVA 0x34A494A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a1fa90190109ac06](../../evidence/conditions-sets-063.md#c-a1fa90190109ac06) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-046204

```text
(config)# default ip rsvp signalling refresh misses <cr>
```

Handler ` RVA 0x100701A0 `；selector ` 0 `；EOL ` RVA 0x34A497C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2da12286403f85bb](../../evidence/conditions-sets-018.md#c-2da12286403f85bb) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-046056

```text
(config)# default ip rsvp signalling refresh reduction <cr>
```

Handler ` RVA 0x100705C0 `；selector ` 0 `；EOL ` RVA 0x34A48E60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0e1fdee263dd9cba](../../evidence/conditions-sets-006.md#c-0e1fdee263dd9cba) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-053558

```text
(config)# default ip rsvp signalling refresh reduction ack-delay <cr>
```

Handler ` RVA 0x100558C0 `；selector ` 0 `；EOL ` RVA 0x34A48F00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ca8f288367a2ba88](../../evidence/conditions-sets-078.md#c-ca8f288367a2ba88) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-045783

```text
(config)# default ip rsvp sso nbr <address> <cr>
```

Handler ` RVA 0x10077190 `；selector ` 0 `；EOL ` RVA 0x34A47678 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` must be router-id of neighbor。

[条件 C-608a725cf05f7ccd](../../evidence/conditions-sets-038.md#c-608a725cf05f7ccd) · [参数 P-efc8816b121035d0](../../evidence/parameters-sets-018.md#p-efc8816b121035d0) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-045352

```text
(config)# default ip rsvp transport client <number:1..65535> <cr>
```

Handler ` RVA 0x1005D010 `；selector ` 0 `；EOL ` RVA 0x34A44D68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Client Identifier。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [参数 P-3bdd4f6af1b7ae23](../../evidence/parameters-sets-005.md#p-3bdd4f6af1b7ae23) · [状态效果 S-a476a5b3e5fd4f3e](../../evidence/state_effects-sets-035.md#s-a476a5b3e5fd4f3e)

### path-035763

```text
(config)# default ip rsvp transport statistics <cr>
```

Handler ` RVA 0x1005CD90 `；selector ` 0 `；EOL ` RVA 0x34A44A50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [状态效果 S-a476a5b3e5fd4f3e](../../evidence/state_effects-sets-035.md#s-a476a5b3e5fd4f3e)

### path-035772

```text
(config)# default ip rsvp udp hosts <cr>
```

Handler ` RVA 0x10056A50 `；selector ` 13 `；EOL ` RVA 0x34A44250 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [状态效果 S-4972bd2f23eb332b](../../evidence/state_effects-sets-016.md#s-4972bd2f23eb332b)

### path-045432

```text
(config)# default ip rsvp udp neighbor <address> <cr>
```

Handler ` RVA 0x10056A50 `；selector ` 14 `；EOL ` RVA 0x34A44648 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` RSVP neighbor's IP address。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [参数 P-af5ad741a5f0a2e3](../../evidence/parameters-sets-013.md#p-af5ad741a5f0a2e3) · [状态效果 S-83537a696a9fdef8](../../evidence/state_effects-sets-028.md#s-83537a696a9fdef8)

### path-035331

```text
(config)# default ip rtcp report interval <cr>
```

Handler ` RVA 0xFD20A20 `；selector ` 0 `；EOL ` RVA 0x348C8130 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f0d7ad47d84e4640](../../evidence/conditions-sets-093.md#c-f0d7ad47d84e4640) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-029141

```text
(config)# default ip rtp coalesce <cr>
```

Handler ` RVA 0xD1900E0 `；selector ` 0 `；EOL ` RVA 0x33DACCA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-254566f36f9fd550](../../evidence/conditions-sets-015.md#c-254566f36f9fd550) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-029449

```text
(config)# default ip sap cache-timeout <cr>
```

Handler ` RVA 0xF87E120 `；selector ` 2 `；EOL ` RVA 0x34756E80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b0cbf452606ab66d](../../evidence/conditions-sets-068.md#c-b0cbf452606ab66d) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-029618

```text
(config)# default ip scp password <cr>
```

Handler ` RVA 0x12345610 `；selector ` 3 `；EOL ` RVA 0x35826108 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8b344f359e1e13a9](../../evidence/conditions-sets-054.md#c-8b344f359e1e13a9) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-029510

```text
(config)# default ip scp remote-username <cr>
```

Handler ` RVA 0x12345610 `；selector ` 1 `；EOL ` RVA 0x35825AA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-82431db2f6659e55](../../evidence/conditions-sets-050.md#c-82431db2f6659e55) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-035542

```text
(config)# default ip scp server enable <cr>
```

Handler ` RVA 0x12345610 `；selector ` 0 `；EOL ` RVA 0x35825750 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-029565

```text
(config)# default ip scp username <cr>
```

Handler ` RVA 0x12345610 `；selector ` 2 `；EOL ` RVA 0x35825DE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ff4415e2349a2159](../../evidence/conditions-sets-098.md#c-ff4415e2349a2159) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-034731

```text
(config)# default ip security eso-info <number:0..255> <cr>
```

Handler ` RVA 0xCF2A810 `；selector ` 4 `；EOL ` RVA 0x33D34A90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` NLESO source。

[条件 C-9840ce3c5c58be11](../../evidence/conditions-sets-059.md#c-9840ce3c5c58be11) · [参数 P-195d1c5ce1e1fe02](../../evidence/parameters-sets-002.md#p-195d1c5ce1e1fe02) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-029563

```text
(config)# default ip sftp password <cr>
```

Handler ` RVA 0x1234BA50 `；selector ` 1 `；EOL ` RVA 0x358269C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-42511010d88cabf2](../../evidence/conditions-sets-026.md#c-42511010d88cabf2) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-029507

```text
(config)# default ip sftp username <cr>
```

Handler ` RVA 0x1234BA50 `；selector ` 0 `；EOL ` RVA 0x358266A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7f7b39b7471ac85c](../../evidence/conditions-sets-049.md#c-7f7b39b7471ac85c) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-026558

```text
(config)# default ip source-route <cr>
```

Handler ` RVA 0xCF2A810 `；selector ` 2 `；EOL ` RVA 0x33D343E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-028997

```text
(config)# default ip spd mode <cr>
```

Handler ` RVA 0xCF2A810 `；selector ` 13 `；EOL ` RVA 0x33D39218 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0536e3537d67b6d3](../../evidence/conditions-sets-002.md#c-0536e3537d67b6d3) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-035127

```text
(config)# default ip spd queue max-threshold <cr>
```

Handler ` RVA 0xCF2A810 `；selector ` 11 `；EOL ` RVA 0x33D396B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-30045888ded96f04](../../evidence/conditions-sets-019.md#c-30045888ded96f04) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-035183

```text
(config)# default ip spd queue min-threshold <cr>
```

Handler ` RVA 0xCF2A810 `；selector ` 12 `；EOL ` RVA 0x33D399D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1318400ae518d622](../../evidence/conditions-sets-008.md#c-1318400ae518d622) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-026973

```text
(config)# default ip ssh authentication-retries <cr>
```

Handler ` RVA 0x123549D0 `；selector ` 24 `；EOL ` RVA 0x3581B8C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-977499e4070928ab](../../evidence/conditions-sets-058.md#c-977499e4070928ab) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-029859

```text
(config)# default ip ssh break-string <cr>
```

Handler ` RVA 0x123549D0 `；selector ` 31 `；EOL ` RVA 0x3581D158 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7858f89b4e5fcc6d](../../evidence/conditions-sets-047.md#c-7858f89b4e5fcc6d) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-029452

```text
(config)# default ip ssh bulk-mode <cr>
```

Handler ` RVA 0x123549D0 `；selector ` 41 `；EOL ` RVA 0x3581B640 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2255ccf3160ca51d](../../evidence/conditions-sets-013.md#c-2255ccf3160ca51d) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-046468

```text
(config)# default ip ssh client algorithm authentication <cr>
```

Handler ` RVA 0x123549D0 `；selector ` 44 `；EOL ` RVA 0x35823688 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-39d682e24dfa1fe1](../../evidence/conditions-sets-022.md#c-39d682e24dfa1fe1) · [状态效果 S-6122cbbf6cd79626](../../evidence/state_effects-sets-021.md#s-6122cbbf6cd79626)

### path-046237

```text
(config)# default ip ssh client algorithm encryption <cr>
```

Handler ` RVA 0x123549D0 `；selector ` 47 `；EOL ` RVA 0x358209D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-24dba19a283443df](../../evidence/conditions-sets-014.md#c-24dba19a283443df) · [状态效果 S-6122cbbf6cd79626](../../evidence/state_effects-sets-021.md#s-6122cbbf6cd79626)

### path-046418

```text
(config)# default ip ssh client algorithm hostkey <cr>
```

Handler ` RVA 0x123549D0 `；selector ` 45 `；EOL ` RVA 0x35822848 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b6efd8e35f459113](../../evidence/conditions-sets-071.md#c-b6efd8e35f459113) · [状态效果 S-6122cbbf6cd79626](../../evidence/state_effects-sets-021.md#s-6122cbbf6cd79626)

### path-046267

```text
(config)# default ip ssh client algorithm kex <cr>
```

Handler ` RVA 0x123549D0 `；selector ` 49 `；EOL ` RVA 0x35821A70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c7e9bf28089cfe6d](../../evidence/conditions-sets-077.md#c-c7e9bf28089cfe6d) · [状态效果 S-6122cbbf6cd79626](../../evidence/state_effects-sets-021.md#s-6122cbbf6cd79626)

### path-046202

```text
(config)# default ip ssh client algorithm mac <cr>
```

Handler ` RVA 0x123549D0 `；selector ` 48 `；EOL ` RVA 0x358200D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c7b5ee540274ca4f](../../evidence/conditions-sets-077.md#c-c7b5ee540274ca4f) · [状态效果 S-6122cbbf6cd79626](../../evidence/state_effects-sets-021.md#s-6122cbbf6cd79626)

### path-046515

```text
(config)# default ip ssh client algorithm publickey <cr>
```

Handler ` RVA 0x123549D0 `；selector ` 46 `；EOL ` RVA 0x35823D40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-338ec9e93e6ebb8f](../../evidence/conditions-sets-020.md#c-338ec9e93e6ebb8f) · [状态效果 S-6122cbbf6cd79626](../../evidence/state_effects-sets-021.md#s-6122cbbf6cd79626)

### path-045823

```text
(config)# default ip ssh dh min size <cr>
```

Handler ` RVA 0x123549D0 `；selector ` 33 `；EOL ` RVA 0x3581DB98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-03f777a8b60f0753](../../evidence/conditions-sets-002.md#c-03f777a8b60f0753) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-030094

```text
(config)# default ip ssh dscp <cr>
```

Handler ` RVA 0x123549D0 `；selector ` 35 `；EOL ` RVA 0x3581E260 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d4f24f1e792ef584](../../evidence/conditions-sets-082.md#c-d4f24f1e792ef584) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-036049

```text
(config)# default ip ssh ec keypair-name <cr>
```

Handler ` RVA 0x123549D0 `；selector ` 29 `；EOL ` RVA 0x3581CE00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b3857b464881641f](../../evidence/conditions-sets-069.md#c-b3857b464881641f) · [状态效果 S-dc41360e00b7f004](../../evidence/state_effects-sets-047.md#s-dc41360e00b7f004)

### path-036121

```text
(config)# default ip ssh logging events <cr>
```

Handler ` RVA 0x123549D0 `；selector ` 32 `；EOL ` RVA 0x3581D480 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-029401

```text
(config)# default ip ssh maxstartups <cr>
```

Handler ` RVA 0x123549D0 `；selector ` 26 `；EOL ` RVA 0x3581B2F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-045351

```text
(config)# default ip ssh port <number:2000..10000> <number:2000..10000> <cr>
```

Handler ` RVA 0x123549D0 `；selector ` 27 `；EOL ` RVA 0x3581C258 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Starting Port number；` unsigned_number ` Ending Port number。

[条件 C-851c49a088247003](../../evidence/conditions-sets-051.md#c-851c49a088247003) · [参数 P-cc18b975222adec1](../../evidence/parameters-sets-015.md#p-cc18b975222adec1) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-030062

```text
(config)# default ip ssh precedence <cr>
```

Handler ` RVA 0x123549D0 `；selector ` 34 `；EOL ` RVA 0x3581DF10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e0464b57b2e0dcaf](../../evidence/conditions-sets-086.md#c-e0464b57b2e0dcaf) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-030165

```text
(config)# default ip ssh pubkey-chain <cr>
```

Handler ` RVA 0x123549D0 `；selector ` 36 `；EOL ` RVA 0x3581E868 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-70542e365cef60fb](../../evidence/conditions-sets-043.md#c-70542e365cef60fb) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-030234

```text
(config)# default ip ssh rekey <cr>
```

Handler ` RVA 0x123549D0 `；selector ` 40 `；EOL ` RVA 0x3581EEF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-348bd27f2c340d76](../../evidence/conditions-sets-020.md#c-348bd27f2c340d76) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-036707

```text
(config)# default ip ssh rekey time <cr>
```

Handler ` RVA 0x123549D0 `；selector ` 38 `；EOL ` RVA 0x3581EC40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad328434183504cf](../../evidence/conditions-sets-067.md#c-ad328434183504cf) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-036751

```text
(config)# default ip ssh rekey volume <cr>
```

Handler ` RVA 0x123549D0 `；selector ` 39 `；EOL ` RVA 0x3581EF90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d196a9f098eaaf90](../../evidence/conditions-sets-081.md#c-d196a9f098eaaf90) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-035971

```text
(config)# default ip ssh rsa keypair-name <cr>
```

Handler ` RVA 0x123549D0 `；selector ` 29 `；EOL ` RVA 0x3581CA58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad454440fc5dd853](../../evidence/conditions-sets-067.md#c-ad454440fc5dd853) · [状态效果 S-249d944555c401e5](../../evidence/state_effects-sets-008.md#s-249d944555c401e5)

### path-046107

```text
(config)# default ip ssh server authenticate user <cr>
```

Handler ` RVA 0x123549D0 `；selector ` 43 `；EOL ` RVA 0x3581F5C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6cecc6839acb574f](../../evidence/conditions-sets-042.md#c-6cecc6839acb574f) · [状态效果 S-f812fb641d2e5a2e](../../evidence/state_effects-sets-053.md#s-f812fb641d2e5a2e)

### path-046124

```text
(config)# default ip ssh server certificate profile <cr>
```

Handler ` RVA 0x123549D0 `；selector ` 50 `；EOL ` RVA 0x3581FD38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2658a4b05d4fadb7](../../evidence/conditions-sets-015.md#c-2658a4b05d4fadb7) · [状态效果 S-f812fb641d2e5a2e](../../evidence/state_effects-sets-053.md#s-f812fb641d2e5a2e)

### path-053598

```text
(config)# default ip ssh server peruser session limit <cr>
```

Handler ` RVA 0x123549D0 `；selector ` 58 `；EOL ` RVA 0x3581F9F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-18fdeb597eda0654](../../evidence/conditions-sets-010.md#c-18fdeb597eda0654) · [状态效果 S-f812fb641d2e5a2e](../../evidence/state_effects-sets-053.md#s-f812fb641d2e5a2e)

### path-029710

```text
(config)# default ip ssh source-interface <cr>
```

Handler ` RVA 0x123549D0 `；selector ` 28 `；EOL ` RVA 0x3581C600 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c3e685e975461719](../../evidence/conditions-sets-076.md#c-c3e685e975461719) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-030088

```text
(config)# default ip ssh stricthostkeycheck <cr>
```

Handler ` RVA 0x123549D0 `；selector ` 37 `；EOL ` RVA 0x3581E550 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-45aac9d47ff2aa63](../../evidence/conditions-sets-027.md#c-45aac9d47ff2aa63) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-026951

```text
(config)# default ip ssh time-out <cr>
```

Handler ` RVA 0x123549D0 `；selector ` 25 `；EOL ` RVA 0x3581B5A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6d4c2c6cb3ebcd63](../../evidence/conditions-sets-042.md#c-6d4c2c6cb3ebcd63) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-036151

```text
(config)# default ip ssh version 2 <cr>
```

Handler ` RVA 0x123549D0 `；selector ` 30 `；EOL ` RVA 0x3581D7B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-45aac9d47ff2aa63](../../evidence/conditions-sets-027.md#c-45aac9d47ff2aa63) · [状态效果 S-6d4bd573d182207d](../../evidence/state_effects-sets-023.md#s-6d4bd573d182207d)

### path-027000

```text
(config)# default ip ssh window-size <cr>
```

Handler ` RVA 0x123549D0 `；selector ` 60 `；EOL ` RVA 0x3581BB68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-dd5a9cacf8a2f42e](../../evidence/conditions-sets-085.md#c-dd5a9cacf8a2f42e) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-026682

```text
(config)# default ip sticky-arp <cr>
```

Handler ` RVA 0xCF2A810 `；selector ` 15 `；EOL ` RVA 0x33D37B80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0489298d4adc773f](../../evidence/conditions-sets-002.md#c-0489298d4adc773f) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-026538

```text
(config)# default ip subnet-zero <cr>
```

Handler ` RVA 0xCF2A810 `；selector ` 3 `；EOL ` RVA 0x33D34138 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-029974

```text
(config)# default ip subscriber l2-roaming <cr>
```

Handler ` RVA 0x11A15630 `；selector ` 0 `；EOL ` RVA 0x355CB190 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-254566f36f9fd550](../../evidence/conditions-sets-015.md#c-254566f36f9fd550) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-036217

```text
(config)# default ip subscriber list <string> <cr>
```

Handler ` RVA 0x11A14BD0 `；selector ` 0 `；EOL ` RVA 0x355CAF10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` list name。

[条件 C-254566f36f9fd550](../../evidence/conditions-sets-015.md#c-254566f36f9fd550) · [参数 P-4713559ac7e67948](../../evidence/parameters-sets-006.md#p-4713559ac7e67948) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-036388

```text
(config)# default ip subscriber timer clear-dangling <cr>
```

Handler ` RVA 0x11A3A780 `；selector ` 1 `；EOL ` RVA 0x355D04B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2003dcccadfd613e](../../evidence/conditions-sets-012.md#c-2003dcccadfd613e) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-052761

```text
(config)# default ip tcp RST-count <number:2..20> RST-window <number:2000..60000> <cr>
```

Handler ` RVA 0xCDEDB20 `；selector ` 13 `；EOL ` RVA 0x33CFE058 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` RST throttle count number；` unsigned_number ` RST throttle window in msec。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [参数 P-66a729b68f6456ab](../../evidence/parameters-sets-008.md#p-66a729b68f6456ab) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-028801

```text
(config)# default ip tcp ack-tuning <cr>
```

Handler ` RVA 0xCDEDB20 `；selector ` 3 `；EOL ` RVA 0x33CFBFF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3ec99a4264edd027](../../evidence/conditions-sets-024.md#c-3ec99a4264edd027) · [状态效果 S-b513a40606a5fa2e](../../evidence/state_effects-sets-038.md#s-b513a40606a5fa2e)

### path-035193

```text
(config)# default ip tcp async-mobility server <cr>
```

Handler ` RVA 0xCDEDB20 `；selector ` 12 `；EOL ` RVA 0x33CFDC90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-026690

```text
(config)# default ip tcp chunk-size <cr>
```

Handler ` RVA 0xCDEDB20 `；selector ` 0 `；EOL ` RVA 0x33CFBF40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8bfca5cc7cc10029](../../evidence/conditions-sets-054.md#c-8bfca5cc7cc10029) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-028617

```text
(config)# default ip tcp delayed-ack <cr>
```

Handler ` RVA 0xCDEDB20 `；selector ` 18 `；EOL ` RVA 0x33CFB9C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-028515

```text
(config)# default ip tcp ecn <cr>
```

Handler ` RVA 0xCDEDB20 `；selector ` 15 `；EOL ` RVA 0x33CFB1D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-026777

```text
(config)# default ip tcp finwait-time <cr>
```

Handler ` RVA 0xCDEDB20 `；selector ` 5 `；EOL ` RVA 0x33CFCDA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2f391e505da4b967](../../evidence/conditions-sets-018.md#c-2f391e505da4b967) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-028893

```text
(config)# default ip tcp keepalive interval <cr>
```

Handler ` RVA 0xCDEDB20 `；selector ` 9 `；EOL ` RVA 0x33CFC870 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0031e26dd3c28e3f](../../evidence/conditions-sets-001.md#c-0031e26dd3c28e3f) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-028836

```text
(config)# default ip tcp keepalive retries <cr>
```

Handler ` RVA 0xCDEDB20 `；selector ` 10 `；EOL ` RVA 0x33CFC808 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-cec63fac3d9fd0c0](../../evidence/conditions-sets-080.md#c-cec63fac3d9fd0c0) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-026714

```text
(config)# default ip tcp mss <cr>
```

Handler ` RVA 0xCDEDB20 `；selector ` 1 `；EOL ` RVA 0x33CFC2C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7203c2dfb37f2c17](../../evidence/conditions-sets-044.md#c-7203c2dfb37f2c17) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-029181

```text
(config)# default ip tcp path-mtu-discovery <cr>
```

Handler ` RVA 0xCDEDB20 `；selector ` 8 `；EOL ` RVA 0x33CFD8F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1079ab16c024bdee](../../evidence/conditions-sets-007.md#c-1079ab16c024bdee) · [状态效果 S-39af139a329f000a](../../evidence/state_effects-sets-013.md#s-39af139a329f000a)

### path-026794

```text
(config)# default ip tcp queuemax <cr>
```

Handler ` RVA 0xCDEDB20 `；selector ` 6 `；EOL ` RVA 0x33CFD040 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d802ac25e8974936](../../evidence/conditions-sets-083.md#c-d802ac25e8974936) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-028545

```text
(config)# default ip tcp selective-ack <cr>
```

Handler ` RVA 0xCDEDB20 `；selector ` 14 `；EOL ` RVA 0x33CFB478 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-026810

```text
(config)# default ip tcp synwait-time <cr>
```

Handler ` RVA 0xCDEDB20 `；selector ` 7 `；EOL ` RVA 0x33CFD2E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f63cc6205be417f6](../../evidence/conditions-sets-095.md#c-f63cc6205be417f6) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-028578

```text
(config)# default ip tcp timestamp <cr>
```

Handler ` RVA 0xCDEDB20 `；selector ` 16 `；EOL ` RVA 0x33CFB720 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-026757

```text
(config)# default ip tcp window-size <cr>
```

Handler ` RVA 0xCDEDB20 `；selector ` 4 `；EOL ` RVA 0x33CFC830 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-667b0f536566789f](../../evidence/conditions-sets-040.md#c-667b0f536566789f) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-028659

```text
(config)# default ip tcp winupdate-opt <cr>
```

Handler ` RVA 0xCDEDB20 `；selector ` 2 `；EOL ` RVA 0x33CFBC70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-044800

```text
(config)# default ip telnet comport disconnect delay <cr>
```

Handler ` RVA 0xCDEDB20 `；selector ` 20 `；EOL ` RVA 0x33D00258 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1770a94687f39efc](../../evidence/conditions-sets-009.md#c-1770a94687f39efc) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-034970

```text
(config)# default ip telnet comport enable <cr>
```

Handler ` RVA 0xCDEDB20 `；selector ` 23 `；EOL ` RVA 0x33CFF7D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9970c652e68b6054](../../evidence/conditions-sets-059.md#c-9970c652e68b6054) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-044713

```text
(config)# default ip telnet comport flow level <cr>
```

Handler ` RVA 0xCDEDB20 `；selector ` 21 `；EOL ` RVA 0x33CFFB40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2f6d2c7d6831a8a3](../../evidence/conditions-sets-019.md#c-2f6d2c7d6831a8a3) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-044758

```text
(config)# default ip telnet comport receive window <cr>
```

Handler ` RVA 0xCDEDB20 `；selector ` 22 `；EOL ` RVA 0x33CFFEE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-30ca81b7ea7a09ef](../../evidence/conditions-sets-019.md#c-30ca81b7ea7a09ef) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-028831

```text
(config)# default ip telnet disable <cr>
```

Handler ` RVA 0xCDEDB20 `；selector ` 46 `；EOL ` RVA 0x33D00560 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-92863ebbc5851c03](../../evidence/conditions-sets-057.md#c-92863ebbc5851c03) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-034840

```text
(config)# default ip telnet hidden addresses <cr>
```

Handler ` RVA 0xCDEDB20 `；selector ` 42 `；EOL ` RVA 0x33CFF430 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e8254d5207707bd1](../../evidence/conditions-sets-090.md#c-e8254d5207707bd1) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-034790

```text
(config)# default ip telnet hidden hostnames <cr>
```

Handler ` RVA 0xCDEDB20 `；selector ` 43 `；EOL ` RVA 0x33CFF188 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e8254d5207707bd1](../../evidence/conditions-sets-090.md#c-e8254d5207707bd1) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-028657

```text
(config)# default ip telnet quiet <cr>
```

Handler ` RVA 0xCDEDB20 `；selector ` 19 `；EOL ` RVA 0x33CFEE78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e8254d5207707bd1](../../evidence/conditions-sets-090.md#c-e8254d5207707bd1) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-028636

```text
(config)# default ip telnet source-interface <cr>
```

Handler ` RVA 0xCDEDB20 `；selector ` 11 `；EOL ` RVA 0x33CFE4B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-da105f80b1d6e1bd](../../evidence/conditions-sets-084.md#c-da105f80b1d6e1bd) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-028656

```text
(config)# default ip telnet timeout retransmit <cr>
```

Handler ` RVA 0xCDEDB20 `；selector ` 44 `；EOL ` RVA 0x33CFEB88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e36a1b59b772ec48](../../evidence/conditions-sets-088.md#c-e36a1b59b772ec48) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-028672

```text
(config)# default ip telnet tos <cr>
```

Handler ` RVA 0xCDEDB20 `；selector ` 17 `；EOL ` RVA 0x33CFE8C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ca4a25d884cae2ce](../../evidence/conditions-sets-078.md#c-ca4a25d884cae2ce) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-028820

```text
(config)# default ip tftp arp-glean <cr>
```

Handler ` RVA 0xCFF2FD0 `；selector ` 1 `；EOL ` RVA 0x33D79000 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-029043

```text
(config)# default ip tftp blocksize <cr>
```

Handler ` RVA 0xCFF2FD0 `；selector ` 4 `；EOL ` RVA 0x33D79750 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-89895d63ff4c0cf9](../../evidence/conditions-sets-053.md#c-89895d63ff4c0cf9) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-029000

```text
(config)# default ip tftp boot-interface <cr>
```

Handler ` RVA 0xCFF2FD0 `；selector ` 3 `；EOL ` RVA 0x33D79370 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d76bbf253d36488c](../../evidence/conditions-sets-083.md#c-d76bbf253d36488c) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-028762

```text
(config)# default ip tftp claim-netascii <cr>
```

Handler ` RVA 0xCFF2FD0 `；selector ` 0 `；EOL ` RVA 0x33D78D58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-028853

```text
(config)# default ip tftp source-interface <cr>
```

Handler ` RVA 0xCFF2FD0 `；selector ` 2 `；EOL ` RVA 0x33D78A18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-023efbab7264e76f](../../evidence/conditions-sets-001.md#c-023efbab7264e76f) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-027082

```text
(config)# default ip trigger-authentication <cr>
```

Handler ` RVA 0x10571410 `；selector ` 0 `；EOL ` RVA 0x34B59F80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-19c1f27792a6000d](../../evidence/conditions-sets-010.md#c-19c1f27792a6000d) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-028965

```text
(config)# default ip ttl decrement <cr>
```

Handler ` RVA 0xCF2A810 `；selector ` 17 `；EOL ` RVA 0x33D39D38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-582072addfb4f1ab](../../evidence/conditions-sets-035.md#c-582072addfb4f1ab) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-044995

```text
(config)# default ip verify drop-rate compute interval <cr>
```

Handler ` RVA 0xB624D70 `；selector ` 0 `；EOL ` RVA 0x337C8E38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-efcfa03f866bdad4](../../evidence/conditions-sets-093.md#c-efcfa03f866bdad4) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-045040

```text
(config)# default ip verify drop-rate compute window <cr>
```

Handler ` RVA 0xB624D70 `；selector ` 1 `；EOL ` RVA 0x337C9128 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ca07ef2f7990b886](../../evidence/conditions-sets-078.md#c-ca07ef2f7990b886) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-045039

```text
(config)# default ip verify drop-rate notify hold-down <cr>
```

Handler ` RVA 0xB624D70 `；selector ` 2 `；EOL ` RVA 0x337C9470 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-666d13b73e355d35](../../evidence/conditions-sets-040.md#c-666d13b73e355d35) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-056993

```text
(config)# default ip visibility global flow monitor sdwan_flow_monitor input <cr>
```

Handler ` RVA 0xC670530 `；selector ` 0 `；EOL ` RVA 0x33ACE698 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-126ca7792afc1ef2](../../evidence/conditions-sets-007.md#c-126ca7792afc1ef2) · [状态效果 S-579df5ab1e24bfa0](../../evidence/state_effects-sets-019.md#s-579df5ab1e24bfa0)

### path-026934

```text
(config)# default ip vrf <cr>
```

Handler ` RVA 0xDC3DE20 `；selector ` 0 `；EOL ` RVA 0x34012D68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-253289dd4aa581ac](../../evidence/conditions-sets-014.md#c-253289dd4aa581ac) · [状态效果 S-aa3128186d818354](../../evidence/state_effects-sets-036.md#s-aa3128186d818354)

### path-045254

```text
(config)# default ip wccp check acl outbound <cr>
```

Handler ` RVA 0x10AD0260 `；selector ` 5 `；EOL ` RVA 0x34C971C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d53387ff584a565c](../../evidence/conditions-sets-082.md#c-d53387ff584a565c) · [状态效果 S-8939d7aea3189756](../../evidence/state_effects-sets-029.md#s-8939d7aea3189756)

### path-045204

```text
(config)# default ip wccp check services all <cr>
```

Handler ` RVA 0x10AD0260 `；selector ` 6 `；EOL ` RVA 0x34C96E78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9cad58f6a22339a1](../../evidence/conditions-sets-061.md#c-9cad58f6a22339a1) · [状态效果 S-8939d7aea3189756](../../evidence/state_effects-sets-029.md#s-8939d7aea3189756)

### path-029556

```text
(config)# default ip wccp outbound-acl-check <cr>
```

Handler ` RVA 0x10AD0260 `；selector ` 4 `；EOL ` RVA 0x34C97548 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-da353358833c7da0](../../evidence/conditions-sets-084.md#c-da353358833c7da0) · [状态效果 S-8939d7aea3189756](../../evidence/state_effects-sets-029.md#s-8939d7aea3189756)

### path-029611

```text
(config)# default ip wccp source-interface <cr>
```

Handler ` RVA 0x10AD0260 `；selector ` 7 `；EOL ` RVA 0x34C979C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-90e516a8a157602a](../../evidence/conditions-sets-056.md#c-90e516a8a157602a) · [状态效果 S-8939d7aea3189756](../../evidence/state_effects-sets-029.md#s-8939d7aea3189756)

### path-029393

```text
(config)# default ip wccp variable-timers <cr>
```

Handler ` RVA 0x10AD0260 `；selector ` 3 `；EOL ` RVA 0x34C96A70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ca12b5280892f8a2](../../evidence/conditions-sets-078.md#c-ca12b5280892f8a2) · [状态效果 S-8939d7aea3189756](../../evidence/state_effects-sets-029.md#s-8939d7aea3189756)

### path-035467

```text
(config)# default ip wccp version <number:2..2> <cr>
```

Handler ` RVA 0x10AD0260 `；selector ` 2 `；EOL ` RVA 0x34C96740 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` WCCP protocol version。

[条件 C-35dca5d82b2b7a5d](../../evidence/conditions-sets-021.md#c-35dca5d82b2b7a5d) · [参数 P-934707403858ea74](../../evidence/parameters-sets-011.md#p-934707403858ea74) · [状态效果 S-8939d7aea3189756](../../evidence/state_effects-sets-029.md#s-8939d7aea3189756)

### path-030102

```text
(config)# default ip wccp web-cache <cr>
```

Handler ` RVA 0x10AD0260 `；selector ` 0 `；EOL ` RVA 0x34C98AB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-067290a17d8f2a2a](../../evidence/conditions-sets-003.md#c-067290a17d8f2a2a) · [状态效果 S-5373e120e4df690e](../../evidence/state_effects-sets-018.md#s-5373e120e4df690e)

### path-027970

```text
(config)# default ipc buffers max-free <cr>
```

Handler ` RVA 0xD3BC170 `；selector ` 1 `；EOL ` RVA 0x33E29378 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b0c548a4bd1de066](../../evidence/conditions-sets-068.md#c-b0c548a4bd1de066) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-027988

```text
(config)# default ipc buffers min-free <cr>
```

Handler ` RVA 0xD3BC170 `；selector ` 0 `；EOL ` RVA 0x33E296C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-af39330b0ba5ce47](../../evidence/conditions-sets-068.md#c-af39330b0ba5ce47) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-028005

```text
(config)# default ipc buffers permanent <cr>
```

Handler ` RVA 0xD3BC170 `；selector ` 2 `；EOL ` RVA 0x33E299F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5cb5e1cb1a3c8b72](../../evidence/conditions-sets-036.md#c-5cb5e1cb1a3c8b72) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-026148

```text
(config)# default ipc cache <cr>
```

Handler ` RVA 0xD3B9730 `；selector ` 0 `；EOL ` RVA 0x33E27D90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7755f7694a22a376](../../evidence/conditions-sets-046.md#c-7755f7694a22a376) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-034040

```text
(config)# default ipc cache slot all <cr>
```

Handler ` RVA 0xD3B9730 `；selector ` 1 `；EOL ` RVA 0x33E28060 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c4ee24a6dee3e16f](../../evidence/conditions-sets-076.md#c-c4ee24a6dee3e16f) · [状态效果 S-f9b17cf687e82d5d](../../evidence/state_effects-sets-053.md#s-f9b17cf687e82d5d)

### path-027959

```text
(config)# default ipc header-cache permanent <cr>
```

Handler ` RVA 0xD3B97D0 `；selector ` 0 `；EOL ` RVA 0x33E28F90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-526a16cc7ce4120d](../../evidence/conditions-sets-032.md#c-526a16cc7ce4120d) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-034037

```text
(config)# default ipc holdq threshold lower <cr>
```

Handler ` RVA 0xD3BBF00 `；selector ` 1 `；EOL ` RVA 0x33E287E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ec702b1d599b7358](../../evidence/conditions-sets-091.md#c-ec702b1d599b7358) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-034029

```text
(config)# default ipc holdq threshold upper <cr>
```

Handler ` RVA 0xD3BBF00 `；selector ` 2 `；EOL ` RVA 0x33E284C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6bbe6364751ae9a5](../../evidence/conditions-sets-042.md#c-6bbe6364751ae9a5) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-027918

```text
(config)# default ipc ru-action on <cr>
```

Handler ` RVA 0xD3FE7B0 `；selector ` 0 `；EOL ` RVA 0x33E3F410 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c232d66a65f05dad](../../evidence/conditions-sets-075.md#c-c232d66a65f05dad) · [状态效果 S-d4754d2f59fe1d9e](../../evidence/state_effects-sets-045.md#s-d4754d2f59fe1d9e)

### path-027949

```text
(config)# default ipc zone default <cr>
```

Handler ` RVA 0xD3BA1B0 `；selector ` 0 `；EOL ` RVA 0x33E28BB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-03cdadb03b9d6679](../../evidence/conditions-sets-002.md#c-03cdadb03b9d6679) · [状态效果 S-bc4faa7222debc8f](../../evidence/state_effects-sets-040.md#s-bc4faa7222debc8f)

### path-030093

```text
(config)# default ipv6 access-list <string> <cr>
```

Handler ` RVA 0x12173E60 `；selector ` 2 `；EOL ` RVA 0x357AD4B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` User selected string identifying this access list。

[条件 C-4ca255b584894e31](../../evidence/conditions-sets-030.md#c-4ca255b584894e31) · [参数 P-3882fcb01116a85b](../../evidence/parameters-sets-005.md#p-3882fcb01116a85b) · [状态效果 S-079de17a9faffdc7](../../evidence/state_effects-sets-002.md#s-079de17a9faffdc7)

### path-036448

```text
(config)# default ipv6 access-list fqdn <string> <cr>
```

Handler ` RVA 0x12173E60 `；selector ` 5 `；EOL ` RVA 0x357AD0D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Access-list name。

[条件 C-dd04f3b98f074a70](../../evidence/conditions-sets-085.md#c-dd04f3b98f074a70) · [参数 P-14bdade43088c73a](../../evidence/parameters-sets-002.md#p-14bdade43088c73a) · [状态效果 S-a0e0d51290ed16ba](../../evidence/state_effects-sets-034.md#s-a0e0d51290ed16ba)

### path-036502

```text
(config)# default ipv6 access-list log-update threshold <cr>
```

Handler ` RVA 0x12172B00 `；selector ` 0 `；EOL ` RVA 0x357AF3B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c3d17114397e26c7](../../evidence/conditions-sets-076.md#c-c3d17114397e26c7) · [状态效果 S-9429ed8a4fe4d9da](../../evidence/state_effects-sets-031.md#s-9429ed8a4fe4d9da)

### path-030016

```text
(config)# default ipv6 access-list match-local-traffic <cr>
```

Handler ` RVA 0x121616D0 `；selector ` 0 `；EOL ` RVA 0x357AF028 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c1b7b1c57909dd9b](../../evidence/conditions-sets-075.md#c-c1b7b1c57909dd9b) · [状态效果 S-9429ed8a4fe4d9da](../../evidence/state_effects-sets-031.md#s-9429ed8a4fe4d9da)

### path-036331

```text
(config)# default ipv6 access-list role-based <string> <cr>
```

Handler ` RVA 0x12173E60 `；selector ` 4 `；EOL ` RVA 0x357ACC98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Access-list name。

[条件 C-90b7c0da3363aae6](../../evidence/conditions-sets-056.md#c-90b7c0da3363aae6) · [参数 P-2666d018d9735b27](../../evidence/parameters-sets-003.md#p-2666d018d9735b27) · [状态效果 S-257ebe685d7c080b](../../evidence/state_effects-sets-008.md#s-257ebe685d7c080b)

### path-026897

```text
(config)# default ipv6 address-validate <cr>
```

Handler ` RVA 0x12302BA0 `；selector ` 0 `；EOL ` RVA 0x357DFB40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-029743

```text
(config)# default ipv6 alias <address> <cr>
```

Handler ` RVA 0x12303CE0 `；selector ` 0 `；EOL ` RVA 0x357E0EB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IPV6 address to alias to a port。

[条件 C-c7188d4393f5a3fb](../../evidence/conditions-sets-077.md#c-c7188d4393f5a3fb) · [参数 P-db734bc6fd45ff91](../../evidence/parameters-sets-017.md#p-db734bc6fd45ff91) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-027198

```text
(config)# default ipv6 cef <cr>
```

Handler ` RVA 0xB67C690 `；selector ` 0 `；EOL ` RVA 0x337D77E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c1c2b243ffe0338a](../../evidence/conditions-sets-075.md#c-c1c2b243ffe0338a) · [状态效果 S-1c826574087b14a1](../../evidence/state_effects-sets-006.md#s-1c826574087b14a1)

### path-030204

```text
(config)# default ipv6 cef accounting <cr>
```

Handler ` RVA 0xB3625A0 `；selector ` 0 `；EOL ` RVA 0x337D6E18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-cfc529009bdae64a](../../evidence/conditions-sets-080.md#c-cfc529009bdae64a) · [状态效果 S-e900677912255122](../../evidence/state_effects-sets-049.md#s-e900677912255122)

### path-036323

```text
(config)# default ipv6 cef load-sharing algorithm <cr>
```

Handler ` RVA 0xB67C8D0 `；selector ` 0 `；EOL ` RVA 0x337D3F80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2569a644b9e44c48](../../evidence/conditions-sets-015.md#c-2569a644b9e44c48) · [状态效果 S-1c826574087b14a1](../../evidence/state_effects-sets-006.md#s-1c826574087b14a1)

### path-053342

```text
(config)# default ipv6 cef load-sharing key-control dpi default <cr>
```

Handler ` RVA 0xB67C9A0 `；selector ` 6 `；EOL ` RVA 0x337D4C70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-fa6ce98a99f5c38c](../../evidence/conditions-sets-097.md#c-fa6ce98a99f5c38c) · [状态效果 S-1c826574087b14a1](../../evidence/state_effects-sets-006.md#s-1c826574087b14a1)

### path-053387

```text
(config)# default ipv6 cef load-sharing key-control dpi l2vpn-mac <cr>
```

Handler ` RVA 0xB67C9A0 `；selector ` 5 `；EOL ` RVA 0x337D50B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-90dc354654fbc5f5](../../evidence/conditions-sets-056.md#c-90dc354654fbc5f5) · [状态效果 S-1c826574087b14a1](../../evidence/state_effects-sets-006.md#s-1c826574087b14a1)

### path-053471

```text
(config)# default ipv6 cef load-sharing key-control dpi tunnel-gre <cr>
```

Handler ` RVA 0xB67C9A0 `；selector ` 0 `；EOL ` RVA 0x337D5BF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-41c799fb7613607a](../../evidence/conditions-sets-026.md#c-41c799fb7613607a) · [状态效果 S-1c826574087b14a1](../../evidence/state_effects-sets-006.md#s-1c826574087b14a1)

### path-053431

```text
(config)# default ipv6 cef load-sharing key-control dpi tunnel-ipinip <cr>
```

Handler ` RVA 0xB67C9A0 `；selector ` 3 `；EOL ` RVA 0x337D5760 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-93f23281d47b9a5a](../../evidence/conditions-sets-057.md#c-93f23281d47b9a5a) · [状态效果 S-1c826574087b14a1](../../evidence/state_effects-sets-006.md#s-1c826574087b14a1)

### path-053508

```text
(config)# default ipv6 cef load-sharing key-control dpi tunnel-ipsec <cr>
```

Handler ` RVA 0xB67C9A0 `；selector ` 2 `；EOL ` RVA 0x337D6080 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0860e5fabfe13c88](../../evidence/conditions-sets-004.md#c-0860e5fabfe13c88) · [状态效果 S-1c826574087b14a1](../../evidence/state_effects-sets-006.md#s-1c826574087b14a1)

### path-053596

```text
(config)# default ipv6 cef load-sharing key-control dpi tunnel-l2tp <cr>
```

Handler ` RVA 0xB67C9A0 `；selector ` 1 `；EOL ` RVA 0x337D6840 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9793b5688de5ea75](../../evidence/conditions-sets-059.md#c-9793b5688de5ea75) · [状态效果 S-1c826574087b14a1](../../evidence/state_effects-sets-006.md#s-1c826574087b14a1)

### path-053554

```text
(config)# default ipv6 cef load-sharing key-control dpi tunnel-vxlan <cr>
```

Handler ` RVA 0xB67C9A0 `；selector ` 4 `；EOL ` RVA 0x337D63A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c8e8fecf39302cd2](../../evidence/conditions-sets-077.md#c-c8e8fecf39302cd2) · [状态效果 S-1c826574087b14a1](../../evidence/state_effects-sets-006.md#s-1c826574087b14a1)

### path-045442

```text
(config)# default ipv6 cef optimize neighbor resolution <cr>
```

Handler ` RVA 0xB60D5B0 `；selector ` 2 `；EOL ` RVA 0x337D7C38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-1c826574087b14a1](../../evidence/state_effects-sets-006.md#s-1c826574087b14a1)

### path-030060

```text
(config)# default ipv6 cef traffic-statistics <cr>
```

Handler ` RVA 0xB362360 `；selector ` 0 `；EOL ` RVA 0x337D74C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-89edfde5a6936d90](../../evidence/conditions-sets-053.md#c-89edfde5a6936d90) · [状态效果 S-00bd04a7ab0eb7fc](../../evidence/state_effects-sets-001.md#s-00bd04a7ab0eb7fc)

### path-026915

```text
(config)# default ipv6 deny-echo-reply <cr>
```

Handler ` RVA 0x12306030 `；selector ` 0 `；EOL ` RVA 0x357E7720 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-035629

```text
(config)# default ipv6 destination-guard policy <string> <cr>
```

Handler ` RVA 0x136B0870 `；selector ` 0 `；EOL ` RVA 0x35C023B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Name of the destination guard policy。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-1689858caa4e8740](../../evidence/parameters-sets-002.md#p-1689858caa4e8740) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-045333

```text
(config)# default ipv6 dhcp binding track ppp <cr>
```

Handler ` RVA 0x121D1F80 `；selector ` 0 `；EOL ` RVA 0x357CC468 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-035657

```text
(config)# default ipv6 dhcp database <string> <cr>
```

Handler ` RVA 0x121D1720 `；selector ` 0 `；EOL ` RVA 0x357CAFF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Uniform Resource Locator (URL)。

[条件 C-e0e58cfcca59d433](../../evidence/conditions-sets-087.md#c-e0e58cfcca59d433) · [参数 P-c8fc7defa064b7c9](../../evidence/parameters-sets-015.md#p-c8fc7defa064b7c9) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-029590

```text
(config)# default ipv6 dhcp iana-route-add <cr>
```

Handler ` RVA 0x121D1B80 `；selector ` 1 `；EOL ` RVA 0x357CC118 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-029533

```text
(config)# default ipv6 dhcp iapd-route-add <cr>
```

Handler ` RVA 0x121D1B80 `；selector ` 0 `；EOL ` RVA 0x357CBE70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-057150

```text
(config)# default ipv6 dhcp monitor statistics start sample-size <number:0..4294967295> <cr>
```

Handler ` RVA 0x121C7630 `；selector ` 1 `；EOL ` RVA 0x357CB930 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Number of packets。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-e24016597d523192](../../evidence/parameters-sets-017.md#p-e24016597d523192) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-045292

```text
(config)# default ipv6 dhcp monitor statistics stop <cr>
```

Handler ` RVA 0x121C7630 `；selector ` 0 `；EOL ` RVA 0x357CBBC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-035782

```text
(config)# default ipv6 dhcp ping packets <cr>
```

Handler ` RVA 0x121D1A90 `；selector ` 0 `；EOL ` RVA 0x357CB510 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6ff1ebaebcc99407](../../evidence/conditions-sets-043.md#c-6ff1ebaebcc99407) · [状态效果 S-f59d103215c6143f](../../evidence/state_effects-sets-052.md#s-f59d103215c6143f)

### path-036012

```text
(config)# default ipv6 dhcp pool <string> <cr>
```

Handler ` RVA 0x121C8450 `；selector ` 0 `；EOL ` RVA 0x357CCD98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` DHCP pool name。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-ed3fe0901c614ca5](../../evidence/parameters-sets-018.md#p-ed3fe0901c614ca5) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-045445

```text
(config)# default ipv6 dhcp ppp framed-prefix cache <cr>
```

Handler ` RVA 0x121D2110 `；selector ` 0 `；EOL ` RVA 0x357CCA50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-035855

```text
(config)# default ipv6 dhcp ppp terminate <cr>
```

Handler ` RVA 0x121D2040 `；selector ` 0 `；EOL ` RVA 0x357CC768 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-045491

```text
(config)# default ipv6 dhcp server join all-dhcp-servers <cr>
```

Handler ` RVA 0x121D21E0 `；selector ` 0 `；EOL ` RVA 0x357CD0E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-045544

```text
(config)# default ipv6 dhcp server vrf enable <cr>
```

Handler ` RVA 0x121D23D0 `；selector ` 0 `；EOL ` RVA 0x357CD3B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-053435

```text
(config)# default ipv6 dhcp test relay drop peeraddr <cr>
```

Handler ` RVA 0x121AF4D0 `；selector ` 6 `；EOL ` RVA 0x357CE580 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0fc9b204a3a3d72a](../../evidence/conditions-sets-006.md#c-0fc9b204a3a3d72a) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-053266

```text
(config)# default ipv6 dhcp test relay forward add <cr>
```

Handler ` RVA 0x121AF4D0 `；selector ` 1 `；EOL ` RVA 0x357CD850 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-cc95d79e6a67dfb0](../../evidence/conditions-sets-079.md#c-cc95d79e6a67dfb0) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-045738

```text
(config)# default ipv6 dhcp test relay notifications <cr>
```

Handler ` RVA 0x121AF4D0 `；selector ` 4 `；EOL ` RVA 0x357CDF50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b3e4fea329eb4bd3](../../evidence/conditions-sets-070.md#c-b3e4fea329eb4bd3) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-045805

```text
(config)# default ipv6 dhcp test relay packet-control <cr>
```

Handler ` RVA 0x121AF4D0 `；selector ` 5 `；EOL ` RVA 0x357CE1F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b3e4fea329eb4bd3](../../evidence/conditions-sets-070.md#c-b3e4fea329eb4bd3) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-057379

```text
(config)# default ipv6 dhcp test relay reply add vsio <cr>
```

Handler ` RVA 0x121AF4D0 `；selector ` 3 `；EOL ` RVA 0x357CDC70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f84d7d69a421f04c](../../evidence/conditions-sets-096.md#c-f84d7d69a421f04c) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-053306

```text
(config)# default ipv6 dhcp test server add vsio <cr>
```

Handler ` RVA 0x121AF4D0 `；selector ` 2 `；EOL ` RVA 0x357CE968 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-352da69a06052a1a](../../evidence/conditions-sets-021.md#c-352da69a06052a1a) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-029624

```text
(config)# default ipv6 dhcp-client leasequery <cr>
```

Handler ` RVA 0x1219DC60 `；selector ` 1 `；EOL ` RVA 0x357CAC18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d559cb94c0e9aabd](../../evidence/conditions-sets-082.md#c-d559cb94c0e9aabd) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-045330

```text
(config)# default ipv6 dhcp-client leasequery server <address> <cr>
```

Handler ` RVA 0x1219D8F0 `；selector ` 1 `；EOL ` RVA 0x357CA5E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IPv6 address。

[条件 C-365e765e786a5dcf](../../evidence/conditions-sets-021.md#c-365e765e786a5dcf) · [参数 P-97ef8b240ca08945](../../evidence/parameters-sets-012.md#p-97ef8b240ca08945) · [状态效果 S-de917ed95e79c243](../../evidence/state_effects-sets-047.md#s-de917ed95e79c243)

### path-035574

```text
(config)# default ipv6 dhcp-relay bulk-lease disable <cr>
```

Handler ` RVA 0x121AEFE0 `；selector ` 0 `；EOL ` RVA 0x357C9140 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-045396

```text
(config)# default ipv6 dhcp-relay bulk-lease retry <number:0..15> <cr>
```

Handler ` RVA 0x121AF210 `；selector ` 0 `；EOL ` RVA 0x357C9820 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Retries。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-b9cd7fb963121a4b](../../evidence/parameters-sets-014.md#p-b9cd7fb963121a4b) · [状态效果 S-51fc16684159afa0](../../evidence/state_effects-sets-018.md#s-51fc16684159afa0)

### path-045171

```text
(config)# default ipv6 dhcp-relay bulk-lease timeout <number:1..40> <cr>
```

Handler ` RVA 0x121AF0F0 `；selector ` 0 `；EOL ` RVA 0x357C9450 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Minutes。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-be54b78770e2902c](../../evidence/parameters-sets-014.md#p-be54b78770e2902c) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-035683

```text
(config)# default ipv6 dhcp-relay option client-link-addr <cr>
```

Handler ` RVA 0x121AE960 `；selector ` 0 `；EOL ` RVA 0x357CA0A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-035621

```text
(config)# default ipv6 dhcp-relay option vpn <cr>
```

Handler ` RVA 0x121AE850 `；selector ` 0 `；EOL ` RVA 0x357C9E00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-035512

```text
(config)# default ipv6 dhcp-relay short-lease <number:60..3600> <cr>
```

Handler ` RVA 0x121AEDC0 `；selector ` 0 `；EOL ` RVA 0x357C8E18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Short Lease in Seconds。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-916df8f5af48c7a3](../../evidence/parameters-sets-011.md#p-916df8f5af48c7a3) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-029399

```text
(config)# default ipv6 dhcp-relay source-interface <cr>
```

Handler ` RVA 0x121AEB80 `；selector ` 0 `；EOL ` RVA 0x357C8A38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b9094b41b2a724fd](../../evidence/conditions-sets-071.md#c-b9094b41b2a724fd) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-029425

```text
(config)# default ipv6 dhcp-relay trust-all <cr>
```

Handler ` RVA 0x121AEA70 `；selector ` 0 `；EOL ` RVA 0x357C9B18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-029561

```text
(config)# default ipv6 first-hop full-proxy <cr>
```

Handler ` RVA 0x1367FFE0 `；selector ` 0 `；EOL ` RVA 0x35BDD090 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7ac701ec23986ce1](../../evidence/conditions-sets-048.md#c-7ac701ec23986ce1) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-029714

```text
(config)# default ipv6 first-hop logging <cr>
```

Handler ` RVA 0x136800A0 `；selector ` 0 `；EOL ` RVA 0x35BDD438 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-c2638efedb5f7785](../../evidence/state_effects-sets-041.md#s-c2638efedb5f7785)

### path-045274

```text
(config)# default ipv6 first-hop service-support punt-acl <number:0..7> <cr>
```

Handler ` RVA 0x13687B10 `；selector ` 0 `；EOL ` RVA 0x35BDD808 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Support (0: none, 1:port, 2:vlan, 4:box, 7: all, ...)。

[条件 C-919e4630fbba4a71](../../evidence/conditions-sets-056.md#c-919e4630fbba4a71) · [参数 P-f1ebff7dfc468e57](../../evidence/parameters-sets-018.md#p-f1ebff7dfc468e57) · [状态效果 S-32535b70f2e8d554](../../evidence/state_effects-sets-011.md#s-32535b70f2e8d554)

### path-035572

```text
(config)# default ipv6 first-hop unit-test bulk-sync <cr>
```

Handler ` RVA 0x13685F80 `；selector ` 0 `；EOL ` RVA 0x35BD8468 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-728106110fe5b4fc](../../evidence/conditions-sets-044.md#c-728106110fe5b4fc) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-057202

```text
(config)# default ipv6 first-hop unit-test check-reach vlan <number:0..4096> <address> <cr>
```

Handler ` RVA 0x136868D0 `；selector ` 0 `；EOL ` RVA 0x35BD97B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Vlan number；` address ` IPv6 address。

[条件 C-728106110fe5b4fc](../../evidence/conditions-sets-044.md#c-728106110fe5b4fc) · [参数 P-7facea3416f79200](../../evidence/parameters-sets-010.md#p-7facea3416f79200) · [状态效果 S-783bbbda9a906763](../../evidence/state_effects-sets-026.md#s-783bbbda9a906763)

### path-036376

```text
(config)# default ipv6 first-hop unit-test disable-cli-sync <cr>
```

Handler ` RVA 0x13686B70 `；selector ` 0 `；EOL ` RVA 0x35BDC7F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-728106110fe5b4fc](../../evidence/conditions-sets-044.md#c-728106110fe5b4fc) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-059134

```text
(config)# default ipv6 first-hop unit-test ha-sync-msg msg-type bt-entry action enable <cr>
```

Handler ` RVA 0x13686A80 `；selector ` 0 `；EOL ` RVA 0x35BDBFC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-728106110fe5b4fc](../../evidence/conditions-sets-044.md#c-728106110fe5b4fc) · [状态效果 S-12a29c0331ec3379](../../evidence/state_effects-sets-004.md#s-12a29c0331ec3379)

### path-053056

```text
(config)# default ipv6 first-hop unit-test ipdt vlan <number:1..4096> <cr>
```

Handler ` RVA 0x13685160 `；selector ` 0 `；EOL ` RVA 0x35BD9B80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Vlan number。

[条件 C-728106110fe5b4fc](../../evidence/conditions-sets-044.md#c-728106110fe5b4fc) · [参数 P-ba82800780ced9a3](../../evidence/parameters-sets-014.md#p-ba82800780ced9a3) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-036274

```text
(config)# default ipv6 first-hop unit-test pgm <cr>
```

Handler ` RVA 0x13680F90 `；selector ` 0 `；EOL ` RVA 0x35BDABC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-728106110fe5b4fc](../../evidence/conditions-sets-044.md#c-728106110fe5b4fc) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-053231

```text
(config)# default ipv6 first-hop unit-test reapply-filters vlan <number:1..4096> <cr>
```

Handler ` RVA 0x13685FF0 `；selector ` 0 `；EOL ` RVA 0x35BDC440 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Vlan number。

[条件 C-728106110fe5b4fc](../../evidence/conditions-sets-044.md#c-728106110fe5b4fc) · [参数 P-e91f8d63075ae567](../../evidence/parameters-sets-017.md#p-e91f8d63075ae567) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-036271

```text
(config)# default ipv6 first-hop unit-test upgm <cr>
```

Handler ` RVA 0x13680B60 `；selector ` 0 `；EOL ` RVA 0x35BDB0D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-728106110fe5b4fc](../../evidence/conditions-sets-044.md#c-728106110fe5b4fc) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-026888

```text
(config)# default ipv6 flowset <cr>
```

Handler ` RVA 0x123062B0 `；selector ` 0 `；EOL ` RVA 0x357E7478 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-026851

```text
(config)# default ipv6 hop-limit <cr>
```

Handler ` RVA 0x12305EC0 `；selector ` 0 `；EOL ` RVA 0x357E5EB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ab8f129fea0c88da](../../evidence/conditions-sets-066.md#c-ab8f129fea0c88da) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-029319

```text
(config)# default ipv6 host <string> <cr>
```

Handler ` RVA 0x123215D0 `；selector ` 0 `；EOL ` RVA 0x3580E3B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Name of host。

[条件 C-87a90b8bda7150ce](../../evidence/conditions-sets-052.md#c-87a90b8bda7150ce) · [参数 P-226e7096f4577940](../../evidence/parameters-sets-003.md#p-226e7096f4577940) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-029290

```text
(config)# default ipv6 icmp error-interval <cr>
```

Handler ` RVA 0x12306390 `；selector ` 0 `；EOL ` RVA 0x357E6968 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-cc817053e039f1ca](../../evidence/conditions-sets-079.md#c-cc817053e039f1ca) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-035288

```text
(config)# default ipv6 icmp od-length enable <cr>
```

Handler ` RVA 0x12307300 `；selector ` 0 `；EOL ` RVA 0x357E6C78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-035356

```text
(config)# default ipv6 icmp od-length test <cr>
```

Handler ` RVA 0x123073F0 `；selector ` 0 `；EOL ` RVA 0x357E6F20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-61524ae912be1b83](../../evidence/conditions-sets-038.md#c-61524ae912be1b83) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-035497

```text
(config)# default ipv6 local policy route-map <cr>
```

Handler ` RVA 0x118B9990 `；selector ` 0 `；EOL ` RVA 0x3559BDF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9e16cf101d628dfd](../../evidence/conditions-sets-061.md#c-9e16cf101d628dfd) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-035387

```text
(config)# default ipv6 local pool <string> <cr>
```

Handler ` RVA 0x1232C650 `；selector ` 0 `；EOL ` RVA 0x35810C20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Create named local prefix pool。

[条件 C-55631f98956327bc](../../evidence/conditions-sets-034.md#c-55631f98956327bc) · [参数 P-697e72abcb3603d7](../../evidence/parameters-sets-008.md#p-697e72abcb3603d7) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-026956

```text
(config)# default ipv6 mfib <cr>
```

Handler ` RVA 0x11903850 `；selector ` 0 `；EOL ` RVA 0x3553E1A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4b23c8c507fe5af2](../../evidence/conditions-sets-029.md#c-4b23c8c507fe5af2) · [状态效果 S-9d798c5872b21431](../../evidence/state_effects-sets-033.md#s-9d798c5872b21431)

### path-027024

```text
(config)# default ipv6 mfib <cr>
```

Handler ` RVA 0x11903850 `；selector ` 0 `；EOL ` RVA 0x3553DEA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c9ded9d41ae45538](../../evidence/conditions-sets-078.md#c-c9ded9d41ae45538) · [状态效果 S-9d798c5872b21431](../../evidence/state_effects-sets-033.md#s-9d798c5872b21431)

### path-029718

```text
(config)# default ipv6 mfib hardware-switching <cr>
```

Handler ` RVA 0x11827A60 `；selector ` 0 `；EOL ` RVA 0x3553D8C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-68150c0384476b4e](../../evidence/conditions-sets-040.md#c-68150c0384476b4e) · [状态效果 S-9d798c5872b21431](../../evidence/state_effects-sets-033.md#s-9d798c5872b21431)

### path-035747

```text
(config)# default ipv6 mfib hardware-switching connected <cr>
```

Handler ` RVA 0x11827EF0 `；selector ` 0 `；EOL ` RVA 0x3553D278 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-11730e923d844f9f](../../evidence/conditions-sets-007.md#c-11730e923d844f9f) · [状态效果 S-9d798c5872b21431](../../evidence/state_effects-sets-033.md#s-9d798c5872b21431)

### path-045338

```text
(config)# default ipv6 mfib hardware-switching replication-mode ingress <cr>
```

Handler ` RVA 0x118280C0 `；selector ` 0 `；EOL ` RVA 0x3553D588 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-11730e923d844f9f](../../evidence/conditions-sets-007.md#c-11730e923d844f9f) · [状态效果 S-9d798c5872b21431](../../evidence/state_effects-sets-033.md#s-9d798c5872b21431)

### path-035633

```text
(config)# default ipv6 mfib hardware-switching shared-tree <cr>
```

Handler ` RVA 0x11827CE0 `；selector ` 0 `；EOL ` RVA 0x3553CF90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b5e13c2566523438](../../evidence/conditions-sets-070.md#c-b5e13c2566523438) · [状态效果 S-9d798c5872b21431](../../evidence/state_effects-sets-033.md#s-9d798c5872b21431)

### path-035953

```text
(config)# default ipv6 mfib hardware-switching uplink <cr>
```

Handler ` RVA 0x11828350 `；selector ` 0 `；EOL ` RVA 0x3553D898 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-395975aa3036d315](../../evidence/conditions-sets-022.md#c-395975aa3036d315) · [状态效果 S-9d798c5872b21431](../../evidence/state_effects-sets-033.md#s-9d798c5872b21431)

### path-029301

```text
(config)# default ipv6 mfib logging-ttl <cr>
```

Handler ` RVA 0x11905500 `；selector ` 0 `；EOL ` RVA 0x3553CBC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ac3ac80ac94b74d5](../../evidence/conditions-sets-067.md#c-ac3ac80ac94b74d5) · [状态效果 S-9d798c5872b21431](../../evidence/state_effects-sets-033.md#s-9d798c5872b21431)

### path-035619

```text
(config)# default ipv6 mld ssm-map enable <cr>
```

Handler ` RVA 0x115D9B60 `；selector ` 17 `；EOL ` RVA 0x35543F90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c92a52d4f9a0426f](../../evidence/conditions-sets-077.md#c-c92a52d4f9a0426f) · [状态效果 S-815f1f77dc7041f0](../../evidence/state_effects-sets-027.md#s-815f1f77dc7041f0)

### path-045277

```text
(config)# default ipv6 mld ssm-map query dns <cr>
```

Handler ` RVA 0x115D9B60 `；selector ` 19 `；EOL ` RVA 0x35544680 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c92a52d4f9a0426f](../../evidence/conditions-sets-077.md#c-c92a52d4f9a0426f) · [状态效果 S-815f1f77dc7041f0](../../evidence/state_effects-sets-027.md#s-815f1f77dc7041f0)

### path-052936

```text
(config)# default ipv6 mld ssm-map static <number:1..199> <address> <cr>
```

Handler ` RVA 0x115D9B60 `；selector ` 18 `；EOL ` RVA 0x35544350 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Access list specifying SSM group range；` address ` SSM source address。

[条件 C-40bcd43c4a7cc7be](../../evidence/conditions-sets-025.md#c-40bcd43c4a7cc7be) · [参数 P-6b633ed1199d8fd7](../../evidence/parameters-sets-008.md#p-6b633ed1199d8fd7) · [状态效果 S-815f1f77dc7041f0](../../evidence/state_effects-sets-027.md#s-815f1f77dc7041f0)

### path-029606

```text
(config)# default ipv6 mld state-limit <cr>
```

Handler ` RVA 0x115D9B60 `；selector ` 20 `；EOL ` RVA 0x35544998 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4d28a3ebec1c4157](../../evidence/conditions-sets-030.md#c-4d28a3ebec1c4157) · [状态效果 S-815f1f77dc7041f0](../../evidence/state_effects-sets-027.md#s-815f1f77dc7041f0)

### path-030124

```text
(config)# default ipv6 multicast group-range <cr>
```

Handler ` RVA 0x118E3BE0 `；selector ` 3 `；EOL ` RVA 0x3553A510 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3f236a2ff2722b07](../../evidence/conditions-sets-024.md#c-3f236a2ff2722b07) · [状态效果 S-94dc8d0c5837175b](../../evidence/state_effects-sets-032.md#s-94dc8d0c5837175b)

### path-045974

```text
(config)# default ipv6 multicast limit cost <number:1..199> <cr>
```

Handler ` RVA 0x11725BA0 `；selector ` 28 `；EOL ` RVA 0x35539E68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Access list specifying group ranges。

[条件 C-69d4715457a01fed](../../evidence/conditions-sets-041.md#c-69d4715457a01fed) · [参数 P-b00e5b1b6c8f00f9](../../evidence/parameters-sets-013.md#p-b00e5b1b6c8f00f9) · [状态效果 S-94dc8d0c5837175b](../../evidence/state_effects-sets-032.md#s-94dc8d0c5837175b)

### path-036609

```text
(config)# default ipv6 multicast limit rate <cr>
```

Handler ` RVA 0x11725BA0 `；selector ` 30 `；EOL ` RVA 0x3553A208 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-99622b4d7e06130c](../../evidence/conditions-sets-059.md#c-99622b4d7e06130c) · [状态效果 S-94dc8d0c5837175b](../../evidence/state_effects-sets-032.md#s-94dc8d0c5837175b)

### path-045670

```text
(config)# default ipv6 multicast mib set-enable mgmd <cr>
```

Handler ` RVA 0x134A1C40 `；selector ` 0 `；EOL ` RVA 0x35A9F210 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-5c57c8da709a614e](../../evidence/state_effects-sets-020.md#s-5c57c8da709a614e)

### path-045742

```text
(config)# default ipv6 multicast mib set-enable pimstdmib <cr>
```

Handler ` RVA 0x134ACBC0 `；selector ` 0 `；EOL ` RVA 0x35AA0C28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-5c57c8da709a614e](../../evidence/state_effects-sets-020.md#s-5c57c8da709a614e)

### path-036385

```text
(config)# default ipv6 multicast mpls mldp <cr>
```

Handler ` RVA 0x118E3BE0 `；selector ` 5 `；EOL ` RVA 0x355366E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0bf1a77df43eb22e](../../evidence/conditions-sets-005.md#c-0bf1a77df43eb22e) · [状态效果 S-94dc8d0c5837175b](../../evidence/state_effects-sets-032.md#s-94dc8d0c5837175b)

### path-036498

```text
(config)# default ipv6 multicast mpls source <cr>
```

Handler ` RVA 0x118E3BE0 `；selector ` 4 `；EOL ` RVA 0x35536F78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0eabbe6dd8dd42a7](../../evidence/conditions-sets-006.md#c-0eabbe6dd8dd42a7) · [状态效果 S-94dc8d0c5837175b](../../evidence/state_effects-sets-032.md#s-94dc8d0c5837175b)

### path-036442

```text
(config)# default ipv6 multicast mpls traffic-eng <cr>
```

Handler ` RVA 0x118E3BE0 `；selector ` 6 `；EOL ` RVA 0x35536B60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4fb08e74fb57fa70](../../evidence/conditions-sets-031.md#c-4fb08e74fb57fa70) · [状态效果 S-94dc8d0c5837175b](../../evidence/state_effects-sets-032.md#s-94dc8d0c5837175b)

### path-030018

```text
(config)# default ipv6 multicast multipath <cr>
```

Handler ` RVA 0x118E3BE0 `；selector ` 2 `；EOL ` RVA 0x35539A18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ff8eb02b54cf08c5](../../evidence/conditions-sets-099.md#c-ff8eb02b54cf08c5) · [状态效果 S-94dc8d0c5837175b](../../evidence/state_effects-sets-032.md#s-94dc8d0c5837175b)

### path-029838

```text
(config)# default ipv6 multicast pim-passive-enable <cr>
```

Handler ` RVA 0x11725BA0 `；selector ` 19 `；EOL ` RVA 0x35538FF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ecdcd8ad5ebc4f00](../../evidence/conditions-sets-092.md#c-ecdcd8ad5ebc4f00) · [状态效果 S-94dc8d0c5837175b](../../evidence/state_effects-sets-032.md#s-94dc8d0c5837175b)

### path-030024

```text
(config)# default ipv6 multicast route-limit <cr>
```

Handler ` RVA 0x11725BA0 `；selector ` 53 `；EOL ` RVA 0x355396F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-08770393eee3b672](../../evidence/conditions-sets-004.md#c-08770393eee3b672) · [状态效果 S-94dc8d0c5837175b](../../evidence/state_effects-sets-032.md#s-94dc8d0c5837175b)

### path-036612

```text
(config)# default ipv6 multicast rpf backoff <cr>
```

Handler ` RVA 0x11725BA0 `；selector ` 17 `；EOL ` RVA 0x35563608 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-dea1ded93b3a58bd](../../evidence/conditions-sets-086.md#c-dea1ded93b3a58bd) · [状态效果 S-aa5caa8e38f49ff2](../../evidence/state_effects-sets-036.md#s-aa5caa8e38f49ff2)

### path-059196

```text
(config)# default ipv6 multicast rpf select vrf <string> group-range <number:1..199> <cr>
```

Handler ` RVA 0x11725BA0 `；selector ` 18 `；EOL ` RVA 0x35563A58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` VPN Routing/Forwarding instance name；` unsigned_number ` Access list specifying group ranges。

[条件 C-74b7d68b7c98a74d](../../evidence/conditions-sets-045.md#c-74b7d68b7c98a74d) · [参数 P-651cae64a3448b1b](../../evidence/parameters-sets-008.md#p-651cae64a3448b1b) · [状态效果 S-aa5caa8e38f49ff2](../../evidence/state_effects-sets-036.md#s-aa5caa8e38f49ff2)

### path-036222

```text
(config)# default ipv6 multicast rpf use-bgp <cr>
```

Handler ` RVA 0x118E3BE0 `；selector ` 1 `；EOL ` RVA 0x355393D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ff8eb02b54cf08c5](../../evidence/conditions-sets-099.md#c-ff8eb02b54cf08c5) · [状态效果 S-94dc8d0c5837175b](../../evidence/state_effects-sets-032.md#s-94dc8d0c5837175b)

### path-027084

```text
(config)# default ipv6 multicast-routing <cr>
```

Handler ` RVA 0x118E3BE0 `；selector ` 0 `；EOL ` RVA 0x355362A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-974b2b6301412b1a](../../evidence/conditions-sets-058.md#c-974b2b6301412b1a) · [状态效果 S-ac2ea5ead5145014](../../evidence/state_effects-sets-036.md#s-ac2ea5ead5145014)

### path-035495

```text
(config)# default ipv6 nd cache expire <cr>
```

Handler ` RVA 0x12318AD0 `；selector ` 0 `；EOL ` RVA 0x35804598 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1597a15263badb60](../../evidence/conditions-sets-009.md#c-1597a15263badb60) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-035443

```text
(config)# default ipv6 nd cache interface-limit <cr>
```

Handler ` RVA 0x123187D0 `；selector ` 0 `；EOL ` RVA 0x358041D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-68b4631ce2b90a5b](../../evidence/conditions-sets-041.md#c-68b4631ce2b90a5b) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-045275

```text
(config)# default ipv6 nd dad loopback detect <cr>
```

Handler ` RVA 0x12318E20 `；selector ` 0 `；EOL ` RVA 0x357F8940 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-029538

```text
(config)# default ipv6 nd dad time <cr>
```

Handler ` RVA 0x12319070 `；selector ` 0 `；EOL ` RVA 0x357F8620 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c586175dd04b5f61](../../evidence/conditions-sets-076.md#c-c586175dd04b5f61) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-029664

```text
(config)# default ipv6 nd default-route <cr>
```

Handler ` RVA 0x12315B20 `；selector ` 0 `；EOL ` RVA 0x357F8368 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-044966

```text
(config)# default ipv6 nd host mode strict <cr>
```

Handler ` RVA 0x123196C0 `；selector ` 0 `；EOL ` RVA 0x35805D30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-026959

```text
(config)# default ipv6 nd ns-interval <cr>
```

Handler ` RVA 0x12315250 `；selector ` 0 `；EOL ` RVA 0x357F79A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-90832f9c3d23ca0b](../../evidence/conditions-sets-056.md#c-90832f9c3d23ca0b) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-029200

```text
(config)# default ipv6 nd nsf convergence <cr>
```

Handler ` RVA 0x123158A0 `；selector ` 0 `；EOL ` RVA 0x357F6A38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-fa267f5262d5b043](../../evidence/conditions-sets-097.md#c-fa267f5262d5b043) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-035422

```text
(config)# default ipv6 nd nsf dad suppress <cr>
```

Handler ` RVA 0x12315FA0 `；selector ` 0 `；EOL ` RVA 0x357F6FE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-fbfae4e40bcde7ee](../../evidence/conditions-sets-097.md#c-fbfae4e40bcde7ee) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-029285

```text
(config)# default ipv6 nd nsf throttle <cr>
```

Handler ` RVA 0x12315E90 `；selector ` 0 `；EOL ` RVA 0x357F6AA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4b628121ae596ecd](../../evidence/conditions-sets-030.md#c-4b628121ae596ecd) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-029357

```text
(config)# default ipv6 nd nud <cr>
```

Handler ` RVA 0x123159C0 `；selector ` 0 `；EOL ` RVA 0x357F7390 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9a5f868f7b647e77](../../evidence/conditions-sets-060.md#c-9a5f868f7b647e77) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-044910

```text
(config)# default ipv6 nd ra solicited unicast <cr>
```

Handler ` RVA 0x123179F0 `；selector ` 0 `；EOL ` RVA 0x357F67A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-026940

```text
(config)# default ipv6 nd reachable-time <cr>
```

Handler ` RVA 0x12315350 `；selector ` 0 `；EOL ` RVA 0x357F7720 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-408561b6662d2f67](../../evidence/conditions-sets-025.md#c-408561b6662d2f67) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-035567

```text
(config)# default ipv6 nd resolution data limit <cr>
```

Handler ` RVA 0x1231B330 `；selector ` 0 `；EOL ` RVA 0x357F7F48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-263532f946184d93](../../evidence/conditions-sets-015.md#c-263532f946184d93) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-029307

```text
(config)# default ipv6 nd route-owner <cr>
```

Handler ` RVA 0x123160A0 `；selector ` 0 `；EOL ` RVA 0x357F76F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-029670

```text
(config)# default ipv6 neighbor binding <cr>
```

Handler ` RVA 0x13680440 `；selector ` 1004 `；EOL ` RVA 0x35BEBAB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1f734c4f3657852b](../../evidence/conditions-sets-012.md#c-1f734c4f3657852b) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-035587

```text
(config)# default ipv6 neighbor binding logging <cr>
```

Handler ` RVA 0x13680440 `；selector ` 1003 `；EOL ` RVA 0x35BEB728 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-bbe643bd5974e3cf](../../evidence/conditions-sets-073.md#c-bbe643bd5974e3cf) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-035605

```text
(config)# default ipv6 neighbor binding max-entries <cr>
```

Handler ` RVA 0x13680440 `；selector ` 1002 `；EOL ` RVA 0x35BEB1F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a1fd4191296933f3](../../evidence/conditions-sets-063.md#c-a1fd4191296933f3) · [状态效果 S-ae229e4122697341](../../evidence/state_effects-sets-037.md#s-ae229e4122697341)

### path-029358

```text
(config)# default ipv6 neighbor tracking <cr>
```

Handler ` RVA 0x13680440 `；selector ` 1005 `；EOL ` RVA 0x35BECCF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-24a971dab09adc20](../../evidence/conditions-sets-014.md#c-24a971dab09adc20) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-026923

```text
(config)# default ipv6 nsf-converge <cr>
```

Handler ` RVA 0x118AC940 `；selector ` 0 `；EOL ` RVA 0x35590608 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6f8281c7e11dc5a6](../../evidence/conditions-sets-043.md#c-6f8281c7e11dc5a6) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-029409

```text
(config)# default ipv6 ospf name-lookup <cr>
```

Handler ` RVA 0x11BC2820 `；selector ` 0 `；EOL ` RVA 0x35681728 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-029650

```text
(config)# default ipv6 pim accept-register <cr>
```

Handler ` RVA 0x11725BA0 `；selector ` 14 `；EOL ` RVA 0x355538F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9b82550c7576f88c](../../evidence/conditions-sets-060.md#c-9b82550c7576f88c) · [状态效果 S-6ec2a46f6b5023e8](../../evidence/state_effects-sets-024.md#s-6ec2a46f6b5023e8)

### path-030087

```text
(config)# default ipv6 pim allow-rp <cr>
```

Handler ` RVA 0x11725BA0 `；selector ` 35 `；EOL ` RVA 0x35555CA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b54d94de10842367](../../evidence/conditions-sets-070.md#c-b54d94de10842367) · [状态效果 S-6ec2a46f6b5023e8](../../evidence/state_effects-sets-024.md#s-6ec2a46f6b5023e8)

### path-045780

```text
(config)# default ipv6 pim anycast-rp <address> <address> <cr>
```

Handler ` RVA 0x11725BA0 `；selector ` 33 `；EOL ` RVA 0x35555958 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IP address of the Anycast Rendezvous Point；` address ` IP address of the Anycast RP peer。

[条件 C-96f5b87be8db8e6b](../../evidence/conditions-sets-058.md#c-96f5b87be8db8e6b) · [参数 P-3e4cef02346a59f8](../../evidence/parameters-sets-005.md#p-3e4cef02346a59f8) · [状态效果 S-6ec2a46f6b5023e8](../../evidence/state_effects-sets-024.md#s-6ec2a46f6b5023e8)

### path-053722

```text
(config)# default ipv6 pim bsr announced rp <address> <cr>
```

Handler ` RVA 0x11725BA0 `；selector ` 26 `；EOL ` RVA 0x355510F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IP name or address of Announced RP。

[条件 C-c9304a4db53b344a](../../evidence/conditions-sets-078.md#c-c9304a4db53b344a) · [参数 P-4723e2b28b5ce721](../../evidence/parameters-sets-006.md#p-4723e2b28b5ce721) · [状态效果 S-0284dad31dcb70e2](../../evidence/state_effects-sets-001.md#s-0284dad31dcb70e2)

### path-053724

```text
(config)# default ipv6 pim bsr candidate bsr <address> <cr>
```

Handler ` RVA 0x11725BA0 `；selector ` 24 `；EOL ` RVA 0x355503E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IP name or address of BSR。

[条件 C-0c67f102d91ba159](../../evidence/conditions-sets-005.md#c-0c67f102d91ba159) · [参数 P-f9eb199b3c4952c8](../../evidence/parameters-sets-019.md#p-f9eb199b3c4952c8) · [状态效果 S-75d5e5c2c82e3006](../../evidence/state_effects-sets-025.md#s-75d5e5c2c82e3006)

### path-053762

```text
(config)# default ipv6 pim bsr candidate rp <address> <cr>
```

Handler ` RVA 0x11725BA0 `；selector ` 27 `；EOL ` RVA 0x35550B38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IP name or address of Candidate RP。

[条件 C-c9304a4db53b344a](../../evidence/conditions-sets-078.md#c-c9304a4db53b344a) · [参数 P-56b08dfe4265191e](../../evidence/parameters-sets-007.md#p-56b08dfe4265191e) · [状态效果 S-adfaef2690b46bd2](../../evidence/state_effects-sets-037.md#s-adfaef2690b46bd2)

### path-045761

```text
(config)# default ipv6 pim maximum group-mappings bsr <cr>
```

Handler ` RVA 0x11725BA0 `；selector ` 34 `；EOL ` RVA 0x355555D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3398c3e3e859b883](../../evidence/conditions-sets-020.md#c-3398c3e3e859b883) · [状态效果 S-6ec2a46f6b5023e8](../../evidence/state_effects-sets-024.md#s-6ec2a46f6b5023e8)

### path-036414

```text
(config)# default ipv6 pim mvpn source-link-local <cr>
```

Handler ` RVA 0x11725BA0 `；selector ` 16 `；EOL ` RVA 0x35556180 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c9304a4db53b344a](../../evidence/conditions-sets-078.md#c-c9304a4db53b344a) · [状态效果 S-6ec2a46f6b5023e8](../../evidence/state_effects-sets-024.md#s-6ec2a46f6b5023e8)

### path-029604

```text
(config)# default ipv6 pim neighbor-filter <cr>
```

Handler ` RVA 0x11725BA0 `；selector ` 15 `；EOL ` RVA 0x355534B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f6bc5dbc7e5f5115](../../evidence/conditions-sets-095.md#c-f6bc5dbc7e5f5115) · [状态效果 S-6ec2a46f6b5023e8](../../evidence/state_effects-sets-024.md#s-6ec2a46f6b5023e8)

### path-029891

```text
(config)# default ipv6 pim old-register-checksum <cr>
```

Handler ` RVA 0x11725BA0 `；selector ` 12 `；EOL ` RVA 0x35555218 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-924fb0804ea39d1c](../../evidence/conditions-sets-056.md#c-924fb0804ea39d1c) · [状态效果 S-6ec2a46f6b5023e8](../../evidence/state_effects-sets-024.md#s-6ec2a46f6b5023e8)

### path-036837

```text
(config)# default ipv6 pim pfp-sa announce <cr>
```

Handler ` RVA 0x11725BA0 `；selector ` 48 `；EOL ` RVA 0x355A3D48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-52880d2f121362e3](../../evidence/conditions-sets-032.md#c-52880d2f121362e3) · [状态效果 S-89899994bdaa69ea](../../evidence/state_effects-sets-029.md#s-89899994bdaa69ea)

### path-036906

```text
(config)# default ipv6 pim pfp-sa cache <cr>
```

Handler ` RVA 0x11725BA0 `；selector ` 51 `；EOL ` RVA 0x355A47E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5cccd6537db7ca1e](../../evidence/conditions-sets-036.md#c-5cccd6537db7ca1e) · [状态效果 S-89899994bdaa69ea](../../evidence/state_effects-sets-029.md#s-89899994bdaa69ea)

### path-046262

```text
(config)# default ipv6 pim pfp-sa timers holdtime <cr>
```

Handler ` RVA 0x11725BA0 `；selector ` 49 `；EOL ` RVA 0x355A41E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e807657f9db92579](../../evidence/conditions-sets-090.md#c-e807657f9db92579) · [状态效果 S-89899994bdaa69ea](../../evidence/state_effects-sets-029.md#s-89899994bdaa69ea)

### path-046301

```text
(config)# default ipv6 pim pfp-sa timers interval <cr>
```

Handler ` RVA 0x11725BA0 `；selector ` 50 `；EOL ` RVA 0x355A44D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-89b0d753bfc5f474](../../evidence/conditions-sets-053.md#c-89b0d753bfc5f474) · [状态效果 S-89899994bdaa69ea](../../evidence/state_effects-sets-029.md#s-89899994bdaa69ea)

### path-035793

```text
(config)# default ipv6 pim rp embedded <cr>
```

Handler ` RVA 0x11725BA0 `；selector ` 13 `；EOL ` RVA 0x35553D10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4e02b58d4c64c037](../../evidence/conditions-sets-031.md#c-4e02b58d4c64c037) · [状态效果 S-6ec2a46f6b5023e8](../../evidence/state_effects-sets-024.md#s-6ec2a46f6b5023e8)

### path-036048

```text
(config)# default ipv6 pim rp-address <address> <cr>
```

Handler ` RVA 0x11725BA0 `；selector ` 7 `；EOL ` RVA 0x355540C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IP name or address of Rendezvous Point。

[条件 C-0c23a90f26c136b7](../../evidence/conditions-sets-005.md#c-0c23a90f26c136b7) · [参数 P-95c3b39af062bf39](../../evidence/parameters-sets-012.md#p-95c3b39af062bf39) · [状态效果 S-6ec2a46f6b5023e8](../../evidence/state_effects-sets-024.md#s-6ec2a46f6b5023e8)

### path-029852

```text
(config)# default ipv6 pim spt-threshold <cr>
```

Handler ` RVA 0x11725BA0 `；selector ` 9 `；EOL ` RVA 0x35554970 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4f6a0b649c30df7c](../../evidence/conditions-sets-031.md#c-4f6a0b649c30df7c) · [状态效果 S-6ec2a46f6b5023e8](../../evidence/state_effects-sets-024.md#s-6ec2a46f6b5023e8)

### path-029959

```text
(config)# default ipv6 prefix-list <string> <cr>
```

Handler ` RVA 0xE21E820 `；selector ` 0 `；EOL ` RVA 0x3557E768 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Name of a prefix list。

[条件 C-5ea6be5510163735](../../evidence/conditions-sets-037.md#c-5ea6be5510163735) · [参数 P-df0de99fc459d497](../../evidence/parameters-sets-017.md#p-df0de99fc459d497) · [状态效果 S-0093d87e065cb81c](../../evidence/state_effects-sets-001.md#s-0093d87e065cb81c)

### path-029586

```text
(config)# default ipv6 prefix-list sequence-number <cr>
```

Handler ` RVA 0xE21E820 `；selector ` 0 `；EOL ` RVA 0x3557E068 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-70700df814f93683](../../evidence/state_effects-sets-024.md#s-70700df814f93683)

