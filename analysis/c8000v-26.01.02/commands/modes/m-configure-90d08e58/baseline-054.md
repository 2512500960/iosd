# configure · 六个基础模式的历史连接

[模式索引](README.md) · [总索引](../../README.md)

### path-040106

```text
(config)# do-exec show ip mrm interface <cr>
```

Handler ` RVA 0xF671F00 `；selector ` 2 `；EOL ` RVA 0x3471FA18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-094e6a5e054b4f4a](../../evidence/conditions-sets-004.md#c-094e6a5e054b4f4a) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061558

```text
(config)# do-exec show ip mrm interface <interface> <cr>
```

Handler ` RVA 0xF671F00 `；selector ` 2 `；EOL ` RVA 0x3471FA18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c411f70c72c88bcf](../../evidence/conditions-sets-076.md#c-c411f70c72c88bcf) · [缺口 G-a26ab3a82305f7d9](../../evidence/gaps-sets-006.md#g-a26ab3a82305f7d9) · [参数 P-ea1e4a7b740e8306](../../evidence/parameters-sets-018.md#p-ea1e4a7b740e8306) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040022

```text
(config)# do-exec show ip mrm manager <cr>
```

Handler ` RVA 0xF671F00 `；selector ` 1 `；EOL ` RVA 0x3471F6A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040101

```text
(config)# do-exec show ip mrm status-report <cr>
```

Handler ` RVA 0xF671F00 `；selector ` 3 `；EOL ` RVA 0x3471FD18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032009

```text
(config)# do-exec show ip mroute <cr>
```

Handler ` RVA 0xF741DF0 `；selector ` 0 `；EOL ` RVA 0x3474F2C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1aea383d8f3532aa](../../evidence/conditions-sets-011.md#c-1aea383d8f3532aa) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061037

```text
(config)# do-exec show ip mroute <prefix:dynamic> <cr>
```

Handler ` RVA 0xF741DF0 `；selector ` 0 `；EOL ` RVA 0x3474F2C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` Group IP address/prefix length。

[条件 C-2e43fcc03dafb3fd](../../evidence/conditions-sets-018.md#c-2e43fcc03dafb3fd) · [缺口 G-7bee30ef788f7ab9](../../evidence/gaps-sets-005.md#g-7bee30ef788f7ab9) · [参数 P-4b47c5dd931b468b](../../evidence/parameters-sets-006.md#p-4b47c5dd931b468b) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-039648

```text
(config)# do-exec show ip msdp count <cr>
```

Handler ` RVA 0xF78DB60 `；selector ` 23 `；EOL ` RVA 0x3473CBA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-054939

```text
(config)# do-exec show ip msdp peer <address> accepted-SAs <cr>
```

Handler ` RVA 0xF78DB60 `；selector ` 27 `；EOL ` RVA 0x3473C668 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Peer name or address。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-215ab85ec08c212f](../../evidence/parameters-sets-003.md#p-215ab85ec08c212f) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-054904

```text
(config)# do-exec show ip msdp peer <address> advertised-SAs <cr>
```

Handler ` RVA 0xF78DB60 `；selector ` 26 `；EOL ` RVA 0x3473C3C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Peer name or address。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-215ab85ec08c212f](../../evidence/parameters-sets-003.md#p-215ab85ec08c212f) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-039587

```text
(config)# do-exec show ip msdp peer <cr>
```

Handler ` RVA 0xF78DB60 `；selector ` 25 `；EOL ` RVA 0x3473C380 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-048586

```text
(config)# do-exec show ip msdp rpf-peer <address> <cr>
```

Handler ` RVA 0xF78DB60 `；selector ` 24 `；EOL ` RVA 0x3473CE70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` RP name or address。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-1e4a8b942f0e7cfd](../../evidence/parameters-sets-003.md#p-1e4a8b942f0e7cfd) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-039658

```text
(config)# do-exec show ip msdp sa-cache <cr>
```

Handler ` RVA 0xF78DB60 `；selector ` 22 `；EOL ` RVA 0x3473BBE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-02126004a7888ab0](../../evidence/conditions-sets-001.md#c-02126004a7888ab0) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-039392

```text
(config)# do-exec show ip msdp summary <cr>
```

Handler ` RVA 0xF78DB60 `；selector ` 21 `；EOL ` RVA 0x3473B8D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062057

```text
(config)# do-exec show ip msdp vrf <?option@555589c8f7f0> count <cr>
```

Handler ` RVA 0xF78DB60 `；selector ` 23 `；EOL ` RVA 0x3473CBA8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-efb39352906f1917](../../evidence/conditions-sets-093.md#c-efb39352906f1917) · [缺口 G-353ae215ff667ff9](../../evidence/gaps-sets-002.md#g-353ae215ff667ff9) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062537

```text
(config)# do-exec show ip msdp vrf <?option@555589c8f7f0> peer <address> accepted-SAs <cr>
```

Handler ` RVA 0xF78DB60 `；selector ` 27 `；EOL ` RVA 0x3473C668 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Peer name or address。

[条件 C-efb39352906f1917](../../evidence/conditions-sets-093.md#c-efb39352906f1917) · [缺口 G-353ae215ff667ff9](../../evidence/gaps-sets-002.md#g-353ae215ff667ff9) · [参数 P-215ab85ec08c212f](../../evidence/parameters-sets-003.md#p-215ab85ec08c212f) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062536

```text
(config)# do-exec show ip msdp vrf <?option@555589c8f7f0> peer <address> advertised-SAs <cr>
```

Handler ` RVA 0xF78DB60 `；selector ` 26 `；EOL ` RVA 0x3473C3C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Peer name or address。

[条件 C-efb39352906f1917](../../evidence/conditions-sets-093.md#c-efb39352906f1917) · [缺口 G-353ae215ff667ff9](../../evidence/gaps-sets-002.md#g-353ae215ff667ff9) · [参数 P-215ab85ec08c212f](../../evidence/parameters-sets-003.md#p-215ab85ec08c212f) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062055

```text
(config)# do-exec show ip msdp vrf <?option@555589c8f7f0> peer <cr>
```

Handler ` RVA 0xF78DB60 `；selector ` 25 `；EOL ` RVA 0x3473C380 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-efb39352906f1917](../../evidence/conditions-sets-093.md#c-efb39352906f1917) · [缺口 G-353ae215ff667ff9](../../evidence/gaps-sets-002.md#g-353ae215ff667ff9) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062359

```text
(config)# do-exec show ip msdp vrf <?option@555589c8f7f0> rpf-peer <address> <cr>
```

Handler ` RVA 0xF78DB60 `；selector ` 24 `；EOL ` RVA 0x3473CE70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` RP name or address。

[条件 C-efb39352906f1917](../../evidence/conditions-sets-093.md#c-efb39352906f1917) · [缺口 G-353ae215ff667ff9](../../evidence/gaps-sets-002.md#g-353ae215ff667ff9) · [参数 P-1e4a8b942f0e7cfd](../../evidence/parameters-sets-003.md#p-1e4a8b942f0e7cfd) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062058

```text
(config)# do-exec show ip msdp vrf <?option@555589c8f7f0> sa-cache <cr>
```

Handler ` RVA 0xF78DB60 `；selector ` 22 `；EOL ` RVA 0x3473BBE8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-41f2ac7c8ff89f65](../../evidence/conditions-sets-026.md#c-41f2ac7c8ff89f65) · [缺口 G-353ae215ff667ff9](../../evidence/gaps-sets-002.md#g-353ae215ff667ff9) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062050

```text
(config)# do-exec show ip msdp vrf <?option@555589c8f7f0> summary <cr>
```

Handler ` RVA 0xF78DB60 `；selector ` 21 `；EOL ` RVA 0x3473B8D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-efb39352906f1917](../../evidence/conditions-sets-093.md#c-efb39352906f1917) · [缺口 G-353ae215ff667ff9](../../evidence/gaps-sets-002.md#g-353ae215ff667ff9) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031816

```text
(config)# do-exec show ip multicast <cr>
```

Handler ` RVA 0xF710E60 `；selector ` 0 `；EOL ` RVA 0x34770E88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5fc63bc3602ff48f](../../evidence/conditions-sets-037.md#c-5fc63bc3602ff48f) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-048284

```text
(config)# do-exec show ip multicast gir clients <cr>
```

Handler ` RVA 0xF710E60 `；selector ` 6 `；EOL ` RVA 0x3474C4D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-47562ebaa2bf7cd7](../../evidence/conditions-sets-028.md#c-47562ebaa2bf7cd7) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-039538

```text
(config)# do-exec show ip multicast interface <cr>
```

Handler ` RVA 0xF710E60 `；selector ` 2 `；EOL ` RVA 0x3474D178 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c9e472e659b2c8fd](../../evidence/conditions-sets-078.md#c-c9e472e659b2c8fd) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061514

```text
(config)# do-exec show ip multicast interface <interface> <cr>
```

Handler ` RVA 0xF710E60 `；selector ` 2 `；EOL ` RVA 0x3474D178 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e265dd35b1c702ba](../../evidence/conditions-sets-087.md#c-e265dd35b1c702ba) · [缺口 G-361d0c48fadd2b96](../../evidence/gaps-sets-002.md#g-361d0c48fadd2b96) · [参数 P-acd724441907d345](../../evidence/parameters-sets-013.md#p-acd724441907d345) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-039595

```text
(config)# do-exec show ip multicast limit <cr>
```

Handler ` RVA 0xF710E60 `；selector ` 1 `；EOL ` RVA 0x3474D520 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2a3daf53dc296283](../../evidence/conditions-sets-017.md#c-2a3daf53dc296283) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061519

```text
(config)# do-exec show ip multicast limit <interface> <cr>
```

Handler ` RVA 0xF710E60 `；selector ` 1 `；EOL ` RVA 0x3474D520 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-82561e3ab0840cd9](../../evidence/conditions-sets-050.md#c-82561e3ab0840cd9) · [缺口 G-71dd44afeefd19a3](../../evidence/gaps-sets-004.md#g-71dd44afeefd19a3) · [参数 P-864e86fd306f3647](../../evidence/parameters-sets-010.md#p-864e86fd306f3647) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-039575

```text
(config)# do-exec show ip multicast lisp-rloc-state <cr>
```

Handler ` RVA 0xF710E60 `；selector ` 5 `；EOL ` RVA 0x3474DC58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-144740b0c080e615](../../evidence/conditions-sets-008.md#c-144740b0c080e615) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-054815

```text
(config)# do-exec show ip multicast mpls mrib-client ipv4 <cr>
```

Handler ` RVA 0xF7114E0 `；selector ` 0 `；EOL ` RVA 0x3474C8B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f2992a11d1a58a09](../../evidence/conditions-sets-094.md#c-f2992a11d1a58a09) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-054862

```text
(config)# do-exec show ip multicast mpls mrib-client ipv6 <cr>
```

Handler ` RVA 0xF711410 `；selector ` 0 `；EOL ` RVA 0x3474CB60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f2992a11d1a58a09](../../evidence/conditions-sets-094.md#c-f2992a11d1a58a09) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-048382

```text
(config)# do-exec show ip multicast mpls vif <cr>
```

Handler ` RVA 0xF7113A0 `；selector ` 0 `；EOL ` RVA 0x3474CDF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f2992a11d1a58a09](../../evidence/conditions-sets-094.md#c-f2992a11d1a58a09) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-055093

```text
(config)# do-exec show ip multicast overlay-mapping lisp <address> <cr>
```

Handler ` RVA 0xF710E60 `；selector ` 8 `；EOL ` RVA 0x3474E0E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Overlay group address。

[条件 C-5d832276d20d451a](../../evidence/conditions-sets-036.md#c-5d832276d20d451a) · [参数 P-c33f2326c4cd42ed](../../evidence/parameters-sets-015.md#p-c33f2326c4cd42ed) · [状态效果 S-9007ce267f167403](../../evidence/state_effects-sets-031.md#s-9007ce267f167403)

### path-062538

```text
(config)# do-exec show ip multicast overlay-mapping lisp <address> interface <interface> <cr>
```

Handler ` RVA 0xF710E60 `；selector ` 8 `；EOL ` RVA 0x3474E0E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Overlay group address。

[条件 C-a9f19beb2282837d](../../evidence/conditions-sets-066.md#c-a9f19beb2282837d) · [缺口 G-65b4d686511158a9](../../evidence/gaps-sets-004.md#g-65b4d686511158a9) · [参数 P-a1fba0a5ea6a0177](../../evidence/parameters-sets-012.md#p-a1fba0a5ea6a0177) · [状态效果 S-9007ce267f167403](../../evidence/state_effects-sets-031.md#s-9007ce267f167403)

### path-049304

```text
(config)# do-exec show ip multicast redundancy ole <cr>
```

Handler ` RVA 0xD46FD80 `；selector ` 2 `；EOL ` RVA 0x33E52298 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-46fb15a3338d2e2d](../../evidence/conditions-sets-028.md#c-46fb15a3338d2e2d) · [状态效果 S-f98d99d410dd60c4](../../evidence/state_effects-sets-053.md#s-f98d99d410dd60c4)

### path-062081

```text
(config)# do-exec show ip multicast redundancy reachability <?ipv4orv6_addr_action@5555893a5f60> <cr>
```

Handler ` RVA 0xD46FD80 `；selector ` 3 `；EOL ` RVA 0x33E51F38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4a278267a3443ff0](../../evidence/conditions-sets-029.md#c-4a278267a3443ff0) · [缺口 G-c409a7e8a8282212](../../evidence/gaps-sets-007.md#g-c409a7e8a8282212) · [状态效果 S-f98d99d410dd60c4](../../evidence/state_effects-sets-053.md#s-f98d99d410dd60c4)

### path-055290

```text
(config)# do-exec show ip multicast redundancy reachability summary <cr>
```

Handler ` RVA 0xD46FD80 `；selector ` 3 `；EOL ` RVA 0x33E51F38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4a278267a3443ff0](../../evidence/conditions-sets-029.md#c-4a278267a3443ff0) · [状态效果 S-d2fa7f21e32fc4b2](../../evidence/state_effects-sets-045.md#s-d2fa7f21e32fc4b2)

### path-049060

```text
(config)# do-exec show ip multicast redundancy state <cr>
```

Handler ` RVA 0xD46FD80 `；selector ` 0 `；EOL ` RVA 0x33E51948 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5fc63bc3602ff48f](../../evidence/conditions-sets-037.md#c-5fc63bc3602ff48f) · [状态效果 S-f98d99d410dd60c4](../../evidence/state_effects-sets-053.md#s-f98d99d410dd60c4)

### path-049040

```text
(config)# do-exec show ip multicast redundancy statistics <cr>
```

Handler ` RVA 0xD46FD80 `；selector ` 1 `；EOL ` RVA 0x33E51BE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5fc63bc3602ff48f](../../evidence/conditions-sets-037.md#c-5fc63bc3602ff48f) · [状态效果 S-f98d99d410dd60c4](../../evidence/state_effects-sets-053.md#s-f98d99d410dd60c4)

### path-048274

```text
(config)# do-exec show ip multicast rpf monitored <cr>
```

Handler ` RVA 0xF710E60 `；selector ` 3 `；EOL ` RVA 0x3474C188 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-058301

```text
(config)# do-exec show ip multicast snooping limit vlan <number:1..4095> <cr>
```

Handler ` RVA 0xC361C10 `；selector ` 60 `；EOL ` RVA 0x33A5DEF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Vlan number。

[条件 C-5fc63bc3602ff48f](../../evidence/conditions-sets-037.md#c-5fc63bc3602ff48f) · [参数 P-236b3a3e749d1c7b](../../evidence/parameters-sets-003.md#p-236b3a3e749d1c7b) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-049007

```text
(config)# do-exec show ip multicast snooping summary <cr>
```

Handler ` RVA 0xC361C10 `；selector ` 70 `；EOL ` RVA 0x33A5E1F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5fc63bc3602ff48f](../../evidence/conditions-sets-037.md#c-5fc63bc3602ff48f) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-058320

```text
(config)# do-exec show ip multicast snooping summary vlan <number:1..4095> <cr>
```

Handler ` RVA 0xC361C10 `；selector ` 68 `；EOL ` RVA 0x33A5E230 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Vlan number。

[条件 C-5fc63bc3602ff48f](../../evidence/conditions-sets-037.md#c-5fc63bc3602ff48f) · [参数 P-0e6e0511934953b5](../../evidence/parameters-sets-002.md#p-0e6e0511934953b5) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-039691

```text
(config)# do-exec show ip multicast timer <cr>
```

Handler ` RVA 0xF710E60 `；selector ` 7 `；EOL ` RVA 0x3474E490 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-171912744b2da9bb](../../evidence/conditions-sets-009.md#c-171912744b2da9bb) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-039824

```text
(config)# do-exec show ip multicast topology <cr>
```

Handler ` RVA 0xF710E60 `；selector ` 4 `；EOL ` RVA 0x3474D988 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d4ef608d9b63ee89](../../evidence/conditions-sets-082.md#c-d4ef608d9b63ee89) · [状态效果 S-4374935630ee9c80](../../evidence/state_effects-sets-015.md#s-4374935630ee9c80)

### path-031159

```text
(config)# do-exec show ip name-servers <cr>
```

Handler ` RVA 0xCF2CF20 `；selector ` 2 `；EOL ` RVA 0x33D328D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-049383

```text
(config)# do-exec show ip nat aggregation top-100-allocator <cr>
```

Handler ` RVA 0xFA2EB90 `；selector ` 9 `；EOL ` RVA 0x347DB178 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0b4c84c7c32d7af9](../../evidence/conditions-sets-005.md#c-0b4c84c7c32d7af9) · [状态效果 S-266208735ebfa271](../../evidence/state_effects-sets-009.md#s-266208735ebfa271)

### path-040537

```text
(config)# do-exec show ip nat alias-usecount <cr>
```

Handler ` RVA 0xFA2EB90 `；selector ` 10 `；EOL ` RVA 0x347DC148 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-38fb4afe68da981d](../../evidence/conditions-sets-022.md#c-38fb4afe68da981d) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040264

```text
(config)# do-exec show ip nat bpa <cr>
```

Handler ` RVA 0xFA2EB90 `；selector ` 5 `；EOL ` RVA 0x347DA9E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7028274df1d580ca](../../evidence/conditions-sets-043.md#c-7028274df1d580ca) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-049620

```text
(config)# do-exec show ip nat dia track <cr>
```

Handler ` RVA 0xFA2EB90 `；selector ` 12 `；EOL ` RVA 0x347DBB90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-54ffd23a7032a3ef](../../evidence/conditions-sets-033.md#c-54ffd23a7032a3ef) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040505

```text
(config)# do-exec show ip nat entry-static <cr>
```

Handler ` RVA 0xFA2EB90 `；selector ` 11 `；EOL ` RVA 0x347DBE60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f84eae1da57a0881](../../evidence/conditions-sets-096.md#c-f84eae1da57a0881) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040601

```text
(config)# do-exec show ip nat ha <cr>
```

Handler ` RVA 0x10C06B70 `；selector ` 0 `；EOL ` RVA 0x34CE8678 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-255475745bdb7c9b](../../evidence/conditions-sets-015.md#c-255475745bdb7c9b) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-055663

```text
(config)# do-exec show ip nat ha inside destination <cr>
```

Handler ` RVA 0x10C06B70 `；selector ` 7 `；EOL ` RVA 0x34CE71F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e43a703bb752aad](../../evidence/conditions-sets-006.md#c-0e43a703bb752aad) · [状态效果 S-8d3634402ef396d9](../../evidence/state_effects-sets-030.md#s-8d3634402ef396d9)

### path-059508

```text
(config)# do-exec show ip nat ha inside destination list <number:1..2699> <cr>
```

Handler ` RVA 0x10C06B70 `；selector ` 6 `；EOL ` RVA 0x34CE7230 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Access list number for global addresses。

[条件 C-0e43a703bb752aad](../../evidence/conditions-sets-006.md#c-0e43a703bb752aad) · [参数 P-9c7276b446f8ff6f](../../evidence/parameters-sets-012.md#p-9c7276b446f8ff6f) · [状态效果 S-8d3634402ef396d9](../../evidence/state_effects-sets-030.md#s-8d3634402ef396d9)

### path-055641

```text
(config)# do-exec show ip nat ha inside source <cr>
```

Handler ` RVA 0x10C06B70 `；selector ` 3 `；EOL ` RVA 0x34CE5E98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-760a5fe5ffc8a104](../../evidence/conditions-sets-046.md#c-760a5fe5ffc8a104) · [状态效果 S-785b3fb5ca4969f5](../../evidence/state_effects-sets-026.md#s-785b3fb5ca4969f5)

### path-055688

```text
(config)# do-exec show ip nat ha inside source <cr>
```

Handler ` RVA 0x10C06B70 `；selector ` 5 `；EOL ` RVA 0x34CE6298 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5047286dcd88b236](../../evidence/conditions-sets-031.md#c-5047286dcd88b236) · [状态效果 S-785b3fb5ca4969f5](../../evidence/state_effects-sets-026.md#s-785b3fb5ca4969f5)

### path-059916

```text
(config)# do-exec show ip nat ha inside source static <address> <address> <cr>
```

Handler ` RVA 0x10C06B70 `；selector ` 4 `；EOL ` RVA 0x34CE64A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Inside local IP address；` address ` Inside global IP address。

[条件 C-5047286dcd88b236](../../evidence/conditions-sets-031.md#c-5047286dcd88b236) · [参数 P-93cfcae875ad4313](../../evidence/parameters-sets-011.md#p-93cfcae875ad4313) · [状态效果 S-785b3fb5ca4969f5](../../evidence/state_effects-sets-026.md#s-785b3fb5ca4969f5)

### path-062649

```text
(config)# do-exec show ip nat ha inside source static <address> interface <interface> <cr>
```

Handler ` RVA 0x10C06B70 `；selector ` 3 `；EOL ` RVA 0x34CE5E98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Inside local IP address。

[条件 C-cc255e483e3cee35](../../evidence/conditions-sets-079.md#c-cc255e483e3cee35) · [缺口 G-8814c98201b8d735](../../evidence/gaps-sets-005.md#g-8814c98201b8d735) · [参数 P-25272ae800a1d716](../../evidence/parameters-sets-003.md#p-25272ae800a1d716) · [状态效果 S-785b3fb5ca4969f5](../../evidence/state_effects-sets-026.md#s-785b3fb5ca4969f5)

### path-062672

```text
(config)# do-exec show ip nat ha inside source static network <address> <address> <?ipmask_action@55558a23a380> <cr>
```

Handler ` RVA 0x10C06B70 `；selector ` 4 `；EOL ` RVA 0x34CE64A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Inside local network；` address ` Inside global network。

[条件 C-5047286dcd88b236](../../evidence/conditions-sets-031.md#c-5047286dcd88b236) · [缺口 G-5401e86e29843787](../../evidence/gaps-sets-003.md#g-5401e86e29843787) · [参数 P-59450e8327b726a1](../../evidence/parameters-sets-007.md#p-59450e8327b726a1) · [状态效果 S-785b3fb5ca4969f5](../../evidence/state_effects-sets-026.md#s-785b3fb5ca4969f5)

### path-049748

```text
(config)# do-exec show ip nat ha mappings <cr>
```

Handler ` RVA 0x10C06B70 `；selector ` 11 `；EOL ` RVA 0x34CE8650 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-255475745bdb7c9b](../../evidence/conditions-sets-015.md#c-255475745bdb7c9b) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-055700

```text
(config)# do-exec show ip nat ha outside source <cr>
```

Handler ` RVA 0x10C06B70 `；selector ` 10 `；EOL ` RVA 0x34CE7D80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-255475745bdb7c9b](../../evidence/conditions-sets-015.md#c-255475745bdb7c9b) · [状态效果 S-f7f6a784e7529702](../../evidence/state_effects-sets-052.md#s-f7f6a784e7529702)

### path-059510

```text
(config)# do-exec show ip nat ha outside source list <number:1..2699> <cr>
```

Handler ` RVA 0x10C06B70 `；selector ` 8 `；EOL ` RVA 0x34CE79C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Access list number for global addresses。

[条件 C-255475745bdb7c9b](../../evidence/conditions-sets-015.md#c-255475745bdb7c9b) · [参数 P-b102d76a95775281](../../evidence/parameters-sets-013.md#p-b102d76a95775281) · [状态效果 S-f7f6a784e7529702](../../evidence/state_effects-sets-052.md#s-f7f6a784e7529702)

### path-059915

```text
(config)# do-exec show ip nat ha outside source static <address> <address> <cr>
```

Handler ` RVA 0x10C06B70 `；selector ` 9 `；EOL ` RVA 0x34CE7F08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Outside global IP address；` address ` Outside local IP address。

[条件 C-255475745bdb7c9b](../../evidence/conditions-sets-015.md#c-255475745bdb7c9b) · [参数 P-bac6837be306eb44](../../evidence/parameters-sets-014.md#p-bac6837be306eb44) · [状态效果 S-f7f6a784e7529702](../../evidence/state_effects-sets-052.md#s-f7f6a784e7529702)

### path-062671

```text
(config)# do-exec show ip nat ha outside source static network <address> <address> <?ipmask_action@55558a23be68> <cr>
```

Handler ` RVA 0x10C06B70 `；selector ` 9 `；EOL ` RVA 0x34CE7F08 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Outside global network；` address ` Outside local network。

[条件 C-255475745bdb7c9b](../../evidence/conditions-sets-015.md#c-255475745bdb7c9b) · [缺口 G-00502c9fc77adcfb](../../evidence/gaps-sets-001.md#g-00502c9fc77adcfb) · [参数 P-27ed0223200d868b](../../evidence/parameters-sets-003.md#p-27ed0223200d868b) · [状态效果 S-f7f6a784e7529702](../../evidence/state_effects-sets-052.md#s-f7f6a784e7529702)

### path-049637

```text
(config)# do-exec show ip nat ha pool <cr>
```

Handler ` RVA 0x10C06B70 `；selector ` 2 `；EOL ` RVA 0x34CE57E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2a8a9262f1a89162](../../evidence/conditions-sets-017.md#c-2a8a9262f1a89162) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-055555

```text
(config)# do-exec show ip nat ha pool <string> <cr>
```

Handler ` RVA 0x10C06B70 `；selector ` 1 `；EOL ` RVA 0x34CE57C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Pool name。

[条件 C-2a8a9262f1a89162](../../evidence/conditions-sets-017.md#c-2a8a9262f1a89162) · [参数 P-9337e862cefa55d7](../../evidence/parameters-sets-011.md#p-9337e862cefa55d7) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-049475

```text
(config)# do-exec show ip nat limits all-host <cr>
```

Handler ` RVA 0xFA2EB90 `；selector ` 4 `；EOL ` RVA 0x347DA148 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-50b8bb48fe758e80](../../evidence/conditions-sets-032.md#c-50b8bb48fe758e80) · [状态效果 S-10a83dc4782dc922](../../evidence/state_effects-sets-004.md#s-10a83dc4782dc922)

### path-040420

```text
(config)# do-exec show ip nat map <cr>
```

Handler ` RVA 0xFA2EB90 `；selector ` 7 `；EOL ` RVA 0x347DB578 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-dc8f64116004688f](../../evidence/conditions-sets-085.md#c-dc8f64116004688f) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040152

```text
(config)# do-exec show ip nat platform <cr>
```

Handler ` RVA 0xFA2EB90 `；selector ` 3 `；EOL ` RVA 0x347D94C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-049438

```text
(config)# do-exec show ip nat pool platform <cr>
```

Handler ` RVA 0xFA2EB90 `；selector ` 6 `；EOL ` RVA 0x347DADD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6d794e298b82915c](../../evidence/conditions-sets-042.md#c-6d794e298b82915c) · [状态效果 S-6d7ec02c3e250076](../../evidence/state_effects-sets-023.md#s-6d7ec02c3e250076)

### path-062392

```text
(config)# do-exec show ip nat portblock dynamic interface <interface> <cr>
```

Handler ` RVA 0xFA2EB90 `；selector ` 2 `；EOL ` RVA 0x347D9910 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1c38969057f0331e](../../evidence/conditions-sets-011.md#c-1c38969057f0331e) · [缺口 G-baaeb2300e40dd15](../../evidence/gaps-sets-007.md#g-baaeb2300e40dd15) · [参数 P-4774f24abba30d2b](../../evidence/parameters-sets-006.md#p-4774f24abba30d2b) · [状态效果 S-e42fc6ce90442877](../../evidence/state_effects-sets-048.md#s-e42fc6ce90442877)

### path-049246

```text
(config)# do-exec show ip nat portblock pat <cr>
```

Handler ` RVA 0xFA2EB90 `；selector ` 2 `；EOL ` RVA 0x347D9910 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-aadf07f045e24108](../../evidence/conditions-sets-066.md#c-aadf07f045e24108) · [状态效果 S-f86b4ec8d7aa1ad5](../../evidence/state_effects-sets-053.md#s-f86b4ec8d7aa1ad5)

### path-040448

```text
(config)# do-exec show ip nat route-dia <cr>
```

Handler ` RVA 0xFA2EB90 `；selector ` 8 `；EOL ` RVA 0x347DB840 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ca48db494d58b37a](../../evidence/conditions-sets-078.md#c-ca48db494d58b37a) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040233

```text
(config)# do-exec show ip nat statistics <cr>
```

Handler ` RVA 0xFA2EB90 `；selector ` 1 `；EOL ` RVA 0x347DA700 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-88bfb62346132430](../../evidence/conditions-sets-053.md#c-88bfb62346132430) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040728

```text
(config)# do-exec show ip nat status <cr>
```

Handler ` RVA 0xFA2FB50 `；selector ` 0 `；EOL ` RVA 0x347DC440 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c5343b7627bf42ff](../../evidence/conditions-sets-076.md#c-c5343b7627bf42ff) · [状态效果 S-099d6e90d017f486](../../evidence/state_effects-sets-002.md#s-099d6e90d017f486)

### path-040520

```text
(config)# do-exec show ip nat translations <cr>
```

Handler ` RVA 0xFA2EB90 `；selector ` 0 `；EOL ` RVA 0x347D7750 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3bb115fc3f9a9f89](../../evidence/conditions-sets-023.md#c-3bb115fc3f9a9f89) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062105

```text
(config)# do-exec show ip nat translations interface <interface> <cr>
```

Handler ` RVA 0xFA2EB90 `；selector ` 0 `；EOL ` RVA 0x347D7750 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-21b781dcfe7651fd](../../evidence/conditions-sets-013.md#c-21b781dcfe7651fd) · [缺口 G-ae13d94d28801bf8](../../evidence/gaps-sets-006.md#g-ae13d94d28801bf8) · [参数 P-2074a0dd7fde8512](../../evidence/parameters-sets-003.md#p-2074a0dd7fde8512) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-063019

```text
(config)# do-exec show ip nbar attribute <?option@55558a79a9e0> <?option@55558a79ab48> <?option@55558a79ac48> <?option@55558a79ad48> <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 60 `；EOL ` RVA 0x35246E20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ce676fdd08077d53](../../evidence/conditions-sets-079.md#c-ce676fdd08077d53) · [缺口 G-669af0bc54f8680c](../../evidence/gaps-sets-004.md#g-669af0bc54f8680c) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062888

```text
(config)# do-exec show ip nbar attribute <?option@55558a79a9e0> <?signed_number_func_action@55558a79b578> <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 21 `；EOL ` RVA 0x35246CB0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a6ac9935dc32de38](../../evidence/conditions-sets-064.md#c-a6ac9935dc32de38) · [缺口 G-d789f3d2e27ad4fe](../../evidence/gaps-sets-007.md#g-d789f3d2e27ad4fe) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061548

```text
(config)# do-exec show ip nbar attribute <?option@55558a79a9e0> <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 20 `；EOL ` RVA 0x35246BB0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4a80e850c9150e29](../../evidence/conditions-sets-029.md#c-4a80e850c9150e29) · [缺口 G-e7c8595bed475462](../../evidence/gaps-sets-008.md#g-e7c8595bed475462) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-039817

```text
(config)# do-exec show ip nbar attribute <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 19 `；EOL ` RVA 0x35246A70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040015

```text
(config)# do-exec show ip nbar attribute-custom <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 36 `；EOL ` RVA 0x35248AD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-15bbd038c1ed607a](../../evidence/conditions-sets-009.md#c-15bbd038c1ed607a) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040024

```text
(config)# do-exec show ip nbar attribute-map <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 26 `；EOL ` RVA 0x35248618 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-15bbd038c1ed607a](../../evidence/conditions-sets-009.md#c-15bbd038c1ed607a) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-048969

```text
(config)# do-exec show ip nbar attribute-map <string> <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 25 `；EOL ` RVA 0x352485F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Attribute Map name。

[条件 C-15bbd038c1ed607a](../../evidence/conditions-sets-009.md#c-15bbd038c1ed607a) · [参数 P-00d2c85d1e33763e](../../evidence/parameters-sets-001.md#p-00d2c85d1e33763e) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-059902

```text
(config)# do-exec show ip nbar classification cache sync export format table <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 54 `；EOL ` RVA 0x352440D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1b75c7a76044d989](../../evidence/conditions-sets-011.md#c-1b75c7a76044d989) · [状态效果 S-cee2d2f1237097f6](../../evidence/state_effects-sets-044.md#s-cee2d2f1237097f6)

### path-062938

```text
(config)# do-exec show ip nbar classification cache sync export format table attribute <?option@55558a797e00> <?option@55558a797f10> <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 54 `；EOL ` RVA 0x352440D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7685d20cfbbbe1ff](../../evidence/conditions-sets-046.md#c-7685d20cfbbbe1ff) · [缺口 G-b0d01dad71c103ba](../../evidence/gaps-sets-006.md#g-b0d01dad71c103ba) · [状态效果 S-e6aa81617fbfd158](../../evidence/state_effects-sets-049.md#s-e6aa81617fbfd158)

### path-059455

```text
(config)# do-exec show ip nbar classification cache sync import last <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 57 `；EOL ` RVA 0x35244498 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f3135ca154eb94d3](../../evidence/conditions-sets-094.md#c-f3135ca154eb94d3) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-055057

```text
(config)# do-exec show ip nbar classification dns learning <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 44 `；EOL ` RVA 0x35243730 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-059458

```text
(config)# do-exec show ip nbar classification dns learning cache <number:1..100000> <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 45 `；EOL ` RVA 0x352428C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of entries to show。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-7e5a6912abbf67f4](../../evidence/parameters-sets-010.md#p-7e5a6912abbf67f4) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062646

```text
(config)# do-exec show ip nbar classification dns learning cache <number:1..100000> protocol <?option@55558a796510> <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 48 `；EOL ` RVA 0x35242610 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Number of entries to show。

[条件 C-e031117ae290ba15](../../evidence/conditions-sets-086.md#c-e031117ae290ba15) · [缺口 G-53287de20e574113](../../evidence/gaps-sets-003.md#g-53287de20e574113) · [参数 P-7e5a6912abbf67f4](../../evidence/parameters-sets-010.md#p-7e5a6912abbf67f4) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-059887

```text
(config)# do-exec show ip nbar classification dns learning cache <number:1..100000> unclassified <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 50 `；EOL ` RVA 0x352428A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of entries to show。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-7e5a6912abbf67f4](../../evidence/parameters-sets-010.md#p-7e5a6912abbf67f4) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-059892

```text
(config)# do-exec show ip nbar classification dns learning cache clients-servers <number:1..100000> <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 46 `；EOL ` RVA 0x35242E78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of entries to show。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-c79de3b2a66f150c](../../evidence/parameters-sets-015.md#p-c79de3b2a66f150c) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062670

```text
(config)# do-exec show ip nbar classification dns learning cache clients-servers <number:1..100000> protocol <?option@55558a796e50> <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 49 `；EOL ` RVA 0x35242F50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Number of entries to show。

[条件 C-cbb6cdd634c805b3](../../evidence/conditions-sets-078.md#c-cbb6cdd634c805b3) · [缺口 G-64b7fc008b189aca](../../evidence/gaps-sets-004.md#g-64b7fc008b189aca) · [参数 P-c79de3b2a66f150c](../../evidence/parameters-sets-015.md#p-c79de3b2a66f150c) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-059891

```text
(config)# do-exec show ip nbar classification dns learning cache ip-address <address> <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 47 `；EOL ` RVA 0x35243470 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IPv4 address。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-d80f378e85a44dd1](../../evidence/parameters-sets-016.md#p-d80f378e85a44dd1) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-058262

```text
(config)# do-exec show ip nbar classification dns learning stats <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 51 `；EOL ` RVA 0x35243708 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-048624

```text
(config)# do-exec show ip nbar classification granularity <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 38 `；EOL ` RVA 0x35241B70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062362

```text
(config)# do-exec show ip nbar classification granularity protocol <?option@55558a795b48> <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 39 `；EOL ` RVA 0x35241C70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d4e3516d05be8897](../../evidence/conditions-sets-082.md#c-d4e3516d05be8897) · [缺口 G-1c48352e6920e863](../../evidence/gaps-sets-001.md#g-1c48352e6920e863) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-054982

```text
(config)# do-exec show ip nbar classification granularity protocol <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 40 `；EOL ` RVA 0x35241BD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-055029

```text
(config)# do-exec show ip nbar classification socket-cache <number:1..100000> <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 52 `；EOL ` RVA 0x35244788 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of sockets to show。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-6099c4f0a96ec586](../../evidence/parameters-sets-008.md#p-6099c4f0a96ec586) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-055124

```text
(config)# do-exec show ip nbar classification socket-cache pl-sockets <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 53 `；EOL ` RVA 0x35244A78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-039448

```text
(config)# do-exec show ip nbar control-plane <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 42 `；EOL ` RVA 0x35241228 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-048675

```text
(config)# do-exec show ip nbar function <string> <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 37 `；EOL ` RVA 0x35244E10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Function name。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-d038cc713a4324ff](../../evidence/parameters-sets-016.md#p-d038cc713a4324ff) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061546

```text
(config)# do-exec show ip nbar link-age <?option@55558a79bf48> <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 2 `；EOL ` RVA 0x35248070 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8e5aafd79c2627a6](../../evidence/conditions-sets-055.md#c-8e5aafd79c2627a6) · [缺口 G-136e7033e55c606d](../../evidence/gaps-sets-001.md#g-136e7033e55c606d) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-039924

```text
(config)# do-exec show ip nbar link-age <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 3 `；EOL ` RVA 0x35247FD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-048472

```text
(config)# do-exec show ip nbar npc detail <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 64 `；EOL ` RVA 0x35241538 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-854194c0c939e8a4](../../evidence/conditions-sets-052.md#c-854194c0c939e8a4) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-048539

```text
(config)# do-exec show ip nbar npc summary <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 65 `；EOL ` RVA 0x352417E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-72464d489fbf4778](../../evidence/conditions-sets-044.md#c-72464d489fbf4778) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062065

```text
(config)# do-exec show ip nbar parameter extraction <?option@55558a799320> <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 28 `；EOL ` RVA 0x352454B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-33c8a7f7837aa1ad](../../evidence/conditions-sets-020.md#c-33c8a7f7837aa1ad) · [缺口 G-41761292c625804c](../../evidence/gaps-sets-003.md#g-41761292c625804c) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062365

```text
(config)# do-exec show ip nbar parameter extraction <?option@55558a799320> activated <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 29 `；EOL ` RVA 0x35245488 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-33c8a7f7837aa1ad](../../evidence/conditions-sets-020.md#c-33c8a7f7837aa1ad) · [缺口 G-41761292c625804c](../../evidence/gaps-sets-003.md#g-41761292c625804c) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-048810

```text
(config)# do-exec show ip nbar parameter extraction <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 34 `；EOL ` RVA 0x352459A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-055034

```text
(config)# do-exec show ip nbar parameter extraction activated <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 35 `；EOL ` RVA 0x35245980 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062072

```text
(config)# do-exec show ip nbar parameter subclassification <?option@55558a799e80> <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 30 `；EOL ` RVA 0x35245FE8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8f41dc294d9a238e](../../evidence/conditions-sets-055.md#c-8f41dc294d9a238e) · [缺口 G-b928edce73d1eca0](../../evidence/gaps-sets-007.md#g-b928edce73d1eca0) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062368

```text
(config)# do-exec show ip nbar parameter subclassification <?option@55558a799e80> activated <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 31 `；EOL ` RVA 0x35245FC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8f41dc294d9a238e](../../evidence/conditions-sets-055.md#c-8f41dc294d9a238e) · [缺口 G-b928edce73d1eca0](../../evidence/gaps-sets-007.md#g-b928edce73d1eca0) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-048880

```text
(config)# do-exec show ip nbar parameter subclassification <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 32 `；EOL ` RVA 0x352464E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-055070

```text
(config)# do-exec show ip nbar parameter subclassification activated <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 33 `；EOL ` RVA 0x352464C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061539

```text
(config)# do-exec show ip nbar protocol-attribute <?option@55558a79b948> <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 23 `；EOL ` RVA 0x35247A78 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-75ea34a2303be017](../../evidence/conditions-sets-046.md#c-75ea34a2303be017) · [缺口 G-ba29e7926f65a2b5](../../evidence/gaps-sets-007.md#g-ba29e7926f65a2b5) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-039871

```text
(config)# do-exec show ip nbar protocol-attribute <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 22 `；EOL ` RVA 0x352479E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040578

```text
(config)# do-exec show ip nbar protocol-discovery <cr>
```

Handler ` RVA 0x10F338B0 `；selector ` 0 `；EOL ` RVA 0x3524DED0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e6f7f47de2d1d824](../../evidence/conditions-sets-089.md#c-e6f7f47de2d1d824) · [状态效果 S-946d5b859e51ecf0](../../evidence/state_effects-sets-031.md#s-946d5b859e51ecf0)

### path-062115

```text
(config)# do-exec show ip nbar protocol-discovery interface <interface> <cr>
```

Handler ` RVA 0x10F338B0 `；selector ` 0 `；EOL ` RVA 0x3524DED0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0cfcb38a2c7ec354](../../evidence/conditions-sets-005.md#c-0cfcb38a2c7ec354) · [缺口 G-61b93a149fe801ab](../../evidence/gaps-sets-004.md#g-61b93a149fe801ab) · [参数 P-a57d3ef15ab024b7](../../evidence/parameters-sets-013.md#p-a57d3ef15ab024b7) · [状态效果 S-febe02391e707930](../../evidence/state_effects-sets-054.md#s-febe02391e707930)

### path-061564

```text
(config)# do-exec show ip nbar protocol-id <?option@55558a79f970> <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 43 `；EOL ` RVA 0x3524BAA0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4d564b4415f1038a](../../evidence/conditions-sets-030.md#c-4d564b4415f1038a) · [缺口 G-cb6064e297dd7b3c](../../evidence/gaps-sets-007.md#g-cb6064e297dd7b3c) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040148

```text
(config)# do-exec show ip nbar protocol-id <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 0 `；EOL ` RVA 0x3524BA08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c732dccb57f95a83](../../evidence/conditions-sets-077.md#c-c732dccb57f95a83) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-049312

```text
(config)# do-exec show ip nbar protocol-pack <string> <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 12 `；EOL ` RVA 0x3524AEE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` NBAR protocol pack name。

[条件 C-cc4851d76a450c9a](../../evidence/conditions-sets-079.md#c-cc4851d76a450c9a) · [参数 P-ee2b771004345552](../../evidence/parameters-sets-018.md#p-ee2b771004345552) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-055326

```text
(config)# do-exec show ip nbar protocol-pack <string> detail <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 11 `；EOL ` RVA 0x3524AC10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` NBAR protocol pack name。

[条件 C-cc4851d76a450c9a](../../evidence/conditions-sets-079.md#c-cc4851d76a450c9a) · [参数 P-ee2b771004345552](../../evidence/parameters-sets-018.md#p-ee2b771004345552) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-055370

```text
(config)# do-exec show ip nbar protocol-pack <string> taxonomy <cr>
```

Handler ` RVA 0x10F21F60 `；selector ` 13 `；EOL ` RVA 0x3524AEB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` NBAR protocol pack name。

[条件 C-cc4851d76a450c9a](../../evidence/conditions-sets-079.md#c-cc4851d76a450c9a) · [参数 P-ee2b771004345552](../../evidence/parameters-sets-018.md#p-ee2b771004345552) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-049104

```text
(config)# do-exec show ip nbar protocol-pack active <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 5 `；EOL ` RVA 0x35249130 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b60cb66f0ecc6c89](../../evidence/conditions-sets-070.md#c-b60cb66f0ecc6c89) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-055179

```text
(config)# do-exec show ip nbar protocol-pack active detail <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 4 `；EOL ` RVA 0x35248E60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b60cb66f0ecc6c89](../../evidence/conditions-sets-070.md#c-b60cb66f0ecc6c89) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-055226

```text
(config)# do-exec show ip nbar protocol-pack active taxonomy <cr>
```

Handler ` RVA 0x10F21F60 `；selector ` 14 `；EOL ` RVA 0x35249108 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b60cb66f0ecc6c89](../../evidence/conditions-sets-070.md#c-b60cb66f0ecc6c89) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-049149

```text
(config)# do-exec show ip nbar protocol-pack inactive <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 7 `；EOL ` RVA 0x35249940 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b60cb66f0ecc6c89](../../evidence/conditions-sets-070.md#c-b60cb66f0ecc6c89) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-055221

```text
(config)# do-exec show ip nbar protocol-pack inactive detail <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 6 `；EOL ` RVA 0x35249670 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b60cb66f0ecc6c89](../../evidence/conditions-sets-070.md#c-b60cb66f0ecc6c89) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-055308

```text
(config)# do-exec show ip nbar protocol-pack inactive taxonomy <cr>
```

Handler ` RVA 0x10F21F60 `；selector ` 16 `；EOL ` RVA 0x352499A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b60cb66f0ecc6c89](../../evidence/conditions-sets-070.md#c-b60cb66f0ecc6c89) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-058366

```text
(config)# do-exec show ip nbar protocol-pack inactive taxonomy <string> <cr>
```

Handler ` RVA 0x10F21F60 `；selector ` 15 `；EOL ` RVA 0x35249980 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` NBAR inactive protocol pack name。

[条件 C-b60cb66f0ecc6c89](../../evidence/conditions-sets-070.md#c-b60cb66f0ecc6c89) · [参数 P-677a9bb0ef608bac](../../evidence/parameters-sets-008.md#p-677a9bb0ef608bac) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-049196

```text
(config)# do-exec show ip nbar protocol-pack loaded <cr>
```

Handler ` RVA 0x10F21F60 `；selector ` 9 `；EOL ` RVA 0x3524A3F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b60cb66f0ecc6c89](../../evidence/conditions-sets-070.md#c-b60cb66f0ecc6c89) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-055255

```text
(config)# do-exec show ip nbar protocol-pack loaded detail <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 8 `；EOL ` RVA 0x3524A128 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b60cb66f0ecc6c89](../../evidence/conditions-sets-070.md#c-b60cb66f0ecc6c89) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-055347

```text
(config)# do-exec show ip nbar protocol-pack loaded taxonomy <cr>
```

Handler ` RVA 0x10F21F60 `；selector ` 18 `；EOL ` RVA 0x3524A460 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b60cb66f0ecc6c89](../../evidence/conditions-sets-070.md#c-b60cb66f0ecc6c89) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-058382

```text
(config)# do-exec show ip nbar protocol-pack loaded taxonomy <string> <cr>
```

Handler ` RVA 0x10F21F60 `；selector ` 17 `；EOL ` RVA 0x3524A438 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` NBAR loaded protocol pack name。

[条件 C-b60cb66f0ecc6c89](../../evidence/conditions-sets-070.md#c-b60cb66f0ecc6c89) · [参数 P-658de79b2d501530](../../evidence/parameters-sets-008.md#p-658de79b2d501530) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040278

```text
(config)# do-exec show ip nbar resources <cr>
```

Handler ` RVA 0x10F3B120 `；selector ` 20 `；EOL ` RVA 0x3524C368 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7aaa3653baa5e431](../../evidence/conditions-sets-048.md#c-7aaa3653baa5e431) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-049266

```text
(config)# do-exec show ip nbar resources flow <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 24 `；EOL ` RVA 0x3524C058 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-85bd44377217f3f3](../../evidence/conditions-sets-052.md#c-85bd44377217f3f3) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-049472

```text
(config)# do-exec show ip nbar resources status <cr>
```

Handler ` RVA 0x10F3B120 `；selector ` 19 `；EOL ` RVA 0x3524CE80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7aaa3653baa5e431](../../evidence/conditions-sets-048.md#c-7aaa3653baa5e431) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-055507

```text
(config)# do-exec show ip nbar resources status <number:10..86400> <cr>
```

Handler ` RVA 0x10F219A0 `；selector ` 22 `；EOL ` RVA 0x3524CEF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Specify age of links (to indicate which bucket)。

[条件 C-7aaa3653baa5e431](../../evidence/conditions-sets-048.md#c-7aaa3653baa5e431) · [参数 P-49c60d7b54c4f3ee](../../evidence/parameters-sets-006.md#p-49c60d7b54c4f3ee) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-058438

```text
(config)# do-exec show ip nbar resources status <number:10..86400> <number:1..50> <cr>
```

Handler ` RVA 0x10F21F60 `；selector ` 23 `；EOL ` RVA 0x3524CEC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Specify age of links (to indicate which bucket)；` unsigned_number ` Number of links to view。

[条件 C-7aaa3653baa5e431](../../evidence/conditions-sets-048.md#c-7aaa3653baa5e431) · [参数 P-d71cbaf17a27d2ca](../../evidence/parameters-sets-016.md#p-d71cbaf17a27d2ca) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-055479

```text
(config)# do-exec show ip nbar resources status fadebucket <cr>
```

Handler ` RVA 0x10F21F60 `；selector ` 24 `；EOL ` RVA 0x3524C990 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7aaa3653baa5e431](../../evidence/conditions-sets-048.md#c-7aaa3653baa5e431) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-058427

```text
(config)# do-exec show ip nbar resources status fadebucket <number:1..50> <cr>
```

Handler ` RVA 0x10F21F60 `；selector ` 25 `；EOL ` RVA 0x3524C968 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of links to view。

[条件 C-7aaa3653baa5e431](../../evidence/conditions-sets-048.md#c-7aaa3653baa5e431) · [参数 P-663e50933124a4cf](../../evidence/parameters-sets-008.md#p-663e50933124a4cf) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-055448

```text
(config)# do-exec show ip nbar resources status freebucket <cr>
```

Handler ` RVA 0x10F21F60 `；selector ` 26 `；EOL ` RVA 0x3524C438 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7aaa3653baa5e431](../../evidence/conditions-sets-048.md#c-7aaa3653baa5e431) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-058418

```text
(config)# do-exec show ip nbar resources status freebucket <number:1..50> <cr>
```

Handler ` RVA 0x10F21F60 `；selector ` 27 `；EOL ` RVA 0x3524C410 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of links to view。

[条件 C-7aaa3653baa5e431](../../evidence/conditions-sets-048.md#c-7aaa3653baa5e431) · [参数 P-911a5d92236ca3a7](../../evidence/parameters-sets-011.md#p-911a5d92236ca3a7) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040095

```text
(config)# do-exec show ip nbar statistics <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 27 `；EOL ` RVA 0x3524B6C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cbfce9c3d822aac3](../../evidence/conditions-sets-078.md#c-cbfce9c3d822aac3) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040016

```text
(config)# do-exec show ip nbar version <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 1 `；EOL ` RVA 0x3524B3E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b60cb66f0ecc6c89](../../evidence/conditions-sets-070.md#c-b60cb66f0ecc6c89) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032258

```text
(config)# do-exec show ip nhrp <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 0 `；EOL ` RVA 0x347F2000 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-12bcabe6c53f20cb](../../evidence/conditions-sets-007.md#c-12bcabe6c53f20cb) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061036

```text
(config)# do-exec show ip nhrp <interface> <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 0 `；EOL ` RVA 0x347F2000 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-63b7f3881d62627d](../../evidence/conditions-sets-039.md#c-63b7f3881d62627d) · [缺口 G-11cf64e66bf8bcc9](../../evidence/gaps-sets-001.md#g-11cf64e66bf8bcc9) · [参数 P-25d6d38100e7fadc](../../evidence/parameters-sets-003.md#p-25d6d38100e7fadc) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040298

```text
(config)# do-exec show ip nhrp attribute <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 16 `；EOL ` RVA 0x347F5C28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040389

```text
(config)# do-exec show ip nhrp instances <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 20 `；EOL ` RVA 0x347F5F38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-770e74c752988f72](../../evidence/conditions-sets-046.md#c-770e74c752988f72) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040353

```text
(config)# do-exec show ip nhrp map <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 17 `；EOL ` RVA 0x347F5968 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a94bf2d8f05cab4e](../../evidence/conditions-sets-065.md#c-a94bf2d8f05cab4e) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061577

```text
(config)# do-exec show ip nhrp map <interface> <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 17 `；EOL ` RVA 0x347F5968 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-162813bb7f838587](../../evidence/conditions-sets-009.md#c-162813bb7f838587) · [缺口 G-3a69137f05319b89](../../evidence/gaps-sets-003.md#g-3a69137f05319b89) · [参数 P-6568a812c93047c0](../../evidence/parameters-sets-008.md#p-6568a812c93047c0) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040431

```text
(config)# do-exec show ip nhrp multicast <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 4 `；EOL ` RVA 0x347F5548 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7e510ef18eef196c](../../evidence/conditions-sets-049.md#c-7e510ef18eef196c) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061581

```text
(config)# do-exec show ip nhrp multicast <interface> <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 4 `；EOL ` RVA 0x347F5548 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-153187901bf614dc](../../evidence/conditions-sets-008.md#c-153187901bf614dc) · [缺口 G-b697487bd462b620](../../evidence/gaps-sets-006.md#g-b697487bd462b620) · [参数 P-1396d9b0340a62ea](../../evidence/parameters-sets-002.md#p-1396d9b0340a62ea) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040360

```text
(config)# do-exec show ip nhrp nhs <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 3 `；EOL ` RVA 0x347F4350 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-dfc4c5caa34e67fb](../../evidence/conditions-sets-086.md#c-dfc4c5caa34e67fb) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061582

```text
(config)# do-exec show ip nhrp nhs <interface> <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 3 `；EOL ` RVA 0x347F4350 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-85b7dab7d3a64cc6](../../evidence/conditions-sets-052.md#c-85b7dab7d3a64cc6) · [缺口 G-a24c209c1f029862](../../evidence/gaps-sets-006.md#g-a24c209c1f029862) · [参数 P-f4bbc780f0b0bf6a](../../evidence/parameters-sets-018.md#p-f4bbc780f0b0bf6a) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062097

```text
(config)# do-exec show ip nhrp nhs <interface> redundancy <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 10 `；EOL ` RVA 0x347F4EB0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-85b7dab7d3a64cc6](../../evidence/conditions-sets-052.md#c-85b7dab7d3a64cc6) · [缺口 G-a24c209c1f029862](../../evidence/gaps-sets-006.md#g-a24c209c1f029862) · [参数 P-f4bbc780f0b0bf6a](../../evidence/parameters-sets-018.md#p-f4bbc780f0b0bf6a) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062544

```text
(config)# do-exec show ip nhrp nhs <interface> redundancy cluster <number:0..10> <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 14 `；EOL ` RVA 0x347F4958 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` NHS cluster number。

[条件 C-85b7dab7d3a64cc6](../../evidence/conditions-sets-052.md#c-85b7dab7d3a64cc6) · [缺口 G-a24c209c1f029862](../../evidence/gaps-sets-006.md#g-a24c209c1f029862) · [参数 P-2f94580451c4bcf7](../../evidence/parameters-sets-004.md#p-2f94580451c4bcf7) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062399

```text
(config)# do-exec show ip nhrp nhs <interface> redundancy preempted <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 12 `；EOL ` RVA 0x347F4BE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-85b7dab7d3a64cc6](../../evidence/conditions-sets-052.md#c-85b7dab7d3a64cc6) · [缺口 G-a24c209c1f029862](../../evidence/gaps-sets-006.md#g-a24c209c1f029862) · [参数 P-f4bbc780f0b0bf6a](../../evidence/parameters-sets-018.md#p-f4bbc780f0b0bf6a) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062393

```text
(config)# do-exec show ip nhrp nhs <interface> redundancy running <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 11 `；EOL ` RVA 0x347F4648 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-85b7dab7d3a64cc6](../../evidence/conditions-sets-052.md#c-85b7dab7d3a64cc6) · [缺口 G-a24c209c1f029862](../../evidence/gaps-sets-006.md#g-a24c209c1f029862) · [参数 P-f4bbc780f0b0bf6a](../../evidence/parameters-sets-018.md#p-f4bbc780f0b0bf6a) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062401

```text
(config)# do-exec show ip nhrp nhs <interface> redundancy waiting <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 13 `；EOL ` RVA 0x347F4E88 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-85b7dab7d3a64cc6](../../evidence/conditions-sets-052.md#c-85b7dab7d3a64cc6) · [缺口 G-a24c209c1f029862](../../evidence/gaps-sets-006.md#g-a24c209c1f029862) · [参数 P-f4bbc780f0b0bf6a](../../evidence/parameters-sets-018.md#p-f4bbc780f0b0bf6a) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-049608

```text
(config)# do-exec show ip nhrp nhs redundancy <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 10 `；EOL ` RVA 0x347F4EB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-dfc4c5caa34e67fb](../../evidence/conditions-sets-086.md#c-dfc4c5caa34e67fb) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-058447

```text
(config)# do-exec show ip nhrp nhs redundancy cluster <number:0..10> <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 14 `；EOL ` RVA 0x347F4958 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` NHS cluster number。

[条件 C-dfc4c5caa34e67fb](../../evidence/conditions-sets-086.md#c-dfc4c5caa34e67fb) · [参数 P-133a9e4b186bdac7](../../evidence/parameters-sets-002.md#p-133a9e4b186bdac7) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-055524

```text
(config)# do-exec show ip nhrp nhs redundancy preempted <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 12 `；EOL ` RVA 0x347F4BE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-dfc4c5caa34e67fb](../../evidence/conditions-sets-086.md#c-dfc4c5caa34e67fb) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-055462

```text
(config)# do-exec show ip nhrp nhs redundancy running <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 11 `；EOL ` RVA 0x347F4648 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-dfc4c5caa34e67fb](../../evidence/conditions-sets-086.md#c-dfc4c5caa34e67fb) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-055546

```text
(config)# do-exec show ip nhrp nhs redundancy waiting <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 13 `；EOL ` RVA 0x347F4E88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-dfc4c5caa34e67fb](../../evidence/conditions-sets-086.md#c-dfc4c5caa34e67fb) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040132

```text
(config)# do-exec show ip nhrp purge <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 2 `；EOL ` RVA 0x347F3F80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062104

```text
(config)# do-exec show ip nhrp rd <?vrf_rd_action@555589d4a310> redirect <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 6 `；EOL ` RVA 0x347F1958 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [缺口 G-af3bcfcd53b79b6a](../../evidence/gaps-sets-006.md#g-af3bcfcd53b79b6a) · [状态效果 S-6fd6ff149904f2d4](../../evidence/state_effects-sets-024.md#s-6fd6ff149904f2d4)

### path-062408

```text
(config)# do-exec show ip nhrp rd <?vrf_rd_action@555589d4a310> redirect statistics <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 7 `；EOL ` RVA 0x347F1930 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [缺口 G-af3bcfcd53b79b6a](../../evidence/gaps-sets-006.md#g-af3bcfcd53b79b6a) · [状态效果 S-6fd6ff149904f2d4](../../evidence/state_effects-sets-024.md#s-6fd6ff149904f2d4)

### path-062102

```text
(config)# do-exec show ip nhrp rd <?vrf_rd_action@555589d4a310> shortcut <cr>
```

Handler ` RVA 0x108FE580 `；selector ` 0 `；EOL ` RVA 0x34BF8EE8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [缺口 G-af3bcfcd53b79b6a](../../evidence/gaps-sets-006.md#g-af3bcfcd53b79b6a) · [状态效果 S-4a51c230bd144fd0](../../evidence/state_effects-sets-016.md#s-4a51c230bd144fd0)

### path-040511

```text
(config)# do-exec show ip nhrp redirect <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 6 `；EOL ` RVA 0x347F1958 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-049619

```text
(config)# do-exec show ip nhrp redirect statistics <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 7 `；EOL ` RVA 0x347F1930 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040504

```text
(config)# do-exec show ip nhrp shortcut <cr>
```

Handler ` RVA 0x108FE580 `；selector ` 0 `；EOL ` RVA 0x34BF8EE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-86ae1ed7fc354af6](../../evidence/state_effects-sets-029.md#s-86ae1ed7fc354af6)

### path-040364

```text
(config)# do-exec show ip nhrp stats <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 18 `；EOL ` RVA 0x347F3B90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-50ed8a211b890947](../../evidence/conditions-sets-032.md#c-50ed8a211b890947) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061583

```text
(config)# do-exec show ip nhrp stats <interface> <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 18 `；EOL ` RVA 0x347F3B90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-32544b29a382a409](../../evidence/conditions-sets-020.md#c-32544b29a382a409) · [缺口 G-2438a1dc2685beb5](../../evidence/gaps-sets-002.md#g-2438a1dc2685beb5) · [参数 P-b3ec1b1c3984c82d](../../evidence/parameters-sets-014.md#p-b3ec1b1c3984c82d) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040196

```text
(config)# do-exec show ip nhrp traffic <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 1 `；EOL ` RVA 0x347F3670 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062084

```text
(config)# do-exec show ip nhrp traffic interface <interface> <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 1 `；EOL ` RVA 0x347F3670 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f04da6df0dc5754c](../../evidence/conditions-sets-093.md#c-f04da6df0dc5754c) · [缺口 G-2385d00d7b3e6c3a](../../evidence/gaps-sets-002.md#g-2385d00d7b3e6c3a) · [参数 P-f682848f403afdb1](../../evidence/parameters-sets-018.md#p-f682848f403afdb1) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032259

```text
(config)# do-exec show ip ospf <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 7 `；EOL ` RVA 0x34892168 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1a5803a3a1c9b578](../../evidence/conditions-sets-010.md#c-1a5803a3a1c9b578) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-039839

```text
(config)# do-exec show ip ospf bad-checksum <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 1 `；EOL ` RVA 0x3487AD60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040358

```text
(config)# do-exec show ip ospf border-routers <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 17 `；EOL ` RVA 0x348788A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d236fddacacd7923](../../evidence/conditions-sets-081.md#c-d236fddacacd7923) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-041012

```text
(config)# do-exec show ip ospf database <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 58 `；EOL ` RVA 0x34895630 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-264cdf48d35a5449](../../evidence/conditions-sets-015.md#c-264cdf48d35a5449) · [状态效果 S-65dccbd7b4856269](../../evidence/state_effects-sets-022.md#s-65dccbd7b4856269)

### path-050007

```text
(config)# do-exec show ip ospf database database-summary <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 60 `；EOL ` RVA 0x34896290 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5f09beff6301b7c5](../../evidence/conditions-sets-037.md#c-5f09beff6301b7c5) · [状态效果 S-65dccbd7b4856269](../../evidence/state_effects-sets-022.md#s-65dccbd7b4856269)

### path-055832

```text
(config)# do-exec show ip ospf database database-summary detail <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 54 `；EOL ` RVA 0x348965B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0a8c31475b28564f](../../evidence/conditions-sets-004.md#c-0a8c31475b28564f) · [状态效果 S-36a7e129628c2ecc](../../evidence/state_effects-sets-012.md#s-36a7e129628c2ecc)

### path-062433

```text
(config)# do-exec show ip ospf database opaque-link prefix <prefix:dynamic> <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 58 `；EOL ` RVA 0x34895630 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` IP prefix &lt;network&gt;/&lt;length&gt;, e.g., 10.0.0.0/8。

[条件 C-1945882df56fd195](../../evidence/conditions-sets-010.md#c-1945882df56fd195) · [缺口 G-0869d17fb61bfa98](../../evidence/gaps-sets-001.md#g-0869d17fb61bfa98) · [参数 P-c20e8d649d8779e6](../../evidence/parameters-sets-015.md#p-c20e8d649d8779e6) · [状态效果 S-4e0ffc817f7b84dd](../../evidence/state_effects-sets-017.md#s-4e0ffc817f7b84dd)

### path-040546

```text
(config)# do-exec show ip ospf delete-list <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 57 `；EOL ` RVA 0x34876370 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d236fddacacd7923](../../evidence/conditions-sets-081.md#c-d236fddacacd7923) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061551

```text
(config)# do-exec show ip ospf events <?option@555589dca990> <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 16 `；EOL ` RVA 0x348769F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d5d38538300ef056](../../evidence/conditions-sets-082.md#c-d5d38538300ef056) · [缺口 G-01e125fbb768b747](../../evidence/gaps-sets-001.md#g-01e125fbb768b747) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-039974

```text
(config)# do-exec show ip ospf events <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 16 `；EOL ` RVA 0x348769F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d601d8d07dd98107](../../evidence/conditions-sets-083.md#c-d601d8d07dd98107) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040755

```text
(config)# do-exec show ip ospf flood-list <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 66 `；EOL ` RVA 0x34890B28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-654fe22627967429](../../evidence/conditions-sets-039.md#c-654fe22627967429) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061639

```text
(config)# do-exec show ip ospf flood-list <interface> <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 66 `；EOL ` RVA 0x34890B28 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1f2e031f2e8466a7](../../evidence/conditions-sets-012.md#c-1f2e031f2e8466a7) · [缺口 G-c41d3ddccf01d0ea](../../evidence/gaps-sets-007.md#g-c41d3ddccf01d0ea) · [参数 P-559bdfbb17cb41ba](../../evidence/parameters-sets-007.md#p-559bdfbb17cb41ba) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040788

```text
(config)# do-exec show ip ospf interface <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 65 `；EOL ` RVA 0x3488FEC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-64e9a11a490d9d30](../../evidence/conditions-sets-039.md#c-64e9a11a490d9d30) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061638

```text
(config)# do-exec show ip ospf interface <interface> <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 65 `；EOL ` RVA 0x3488FEC8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1e9524994f16b88c](../../evidence/conditions-sets-012.md#c-1e9524994f16b88c) · [缺口 G-4ae8073d2450ae27](../../evidence/gaps-sets-003.md#g-4ae8073d2450ae27) · [参数 P-7d4580ce235b9ca9](../../evidence/parameters-sets-010.md#p-7d4580ce235b9ca9) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-049973

```text
(config)# do-exec show ip ospf internal forwarding-addresses <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 23 `；EOL ` RVA 0x34891EA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d236fddacacd7923](../../evidence/conditions-sets-081.md#c-d236fddacacd7923) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-055767

```text
(config)# do-exec show ip ospf internal memory cache <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 2 `；EOL ` RVA 0x34891C10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d236fddacacd7923](../../evidence/conditions-sets-081.md#c-d236fddacacd7923) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040424

```text
(config)# do-exec show ip ospf max-metric <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 10 `；EOL ` RVA 0x34879EC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d236fddacacd7923](../../evidence/conditions-sets-081.md#c-d236fddacacd7923) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040381

```text
(config)# do-exec show ip ospf maxage-list <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 9 `；EOL ` RVA 0x3487A410 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d236fddacacd7923](../../evidence/conditions-sets-081.md#c-d236fddacacd7923) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062421

```text
(config)# do-exec show ip ospf mpls ldp interface <interface> <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 61 `；EOL ` RVA 0x3488F830 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e47023c60f690c7c](../../evidence/conditions-sets-088.md#c-e47023c60f690c7c) · [缺口 G-9f0a272e36c2260b](../../evidence/gaps-sets-006.md#g-9f0a272e36c2260b) · [参数 P-1708b25356763448](../../evidence/parameters-sets-002.md#p-1708b25356763448) · [状态效果 S-7592e41004f58bb0](../../evidence/state_effects-sets-025.md#s-7592e41004f58bb0)

### path-055691

```text
(config)# do-exec show ip ospf mpls traffic-eng link <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 61 `；EOL ` RVA 0x3488F830 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d236fddacacd7923](../../evidence/conditions-sets-081.md#c-d236fddacacd7923) · [状态效果 S-04557cc50c715180](../../evidence/state_effects-sets-001.md#s-04557cc50c715180)

### path-040091

```text
(config)# do-exec show ip ospf multi-area <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 68 `；EOL ` RVA 0x348775F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b28cfdb94256e16e](../../evidence/conditions-sets-069.md#c-b28cfdb94256e16e) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040970

```text
(config)# do-exec show ip ospf neighbor <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 71 `；EOL ` RVA 0x34890EC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e3d10944cffa4e82](../../evidence/conditions-sets-088.md#c-e3d10944cffa4e82) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061657

```text
(config)# do-exec show ip ospf neighbor <interface> <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 71 `；EOL ` RVA 0x34890EC8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7cbe331693101269](../../evidence/conditions-sets-048.md#c-7cbe331693101269) · [缺口 G-f00c520c112f9683](../../evidence/gaps-sets-008.md#g-f00c520c112f9683) · [参数 P-0f45569dc916688e](../../evidence/parameters-sets-002.md#p-0f45569dc916688e) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040147

```text
(config)# do-exec show ip ospf nsf <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 14 `；EOL ` RVA 0x34877900 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d236fddacacd7923](../../evidence/conditions-sets-081.md#c-d236fddacacd7923) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040570

```text
(config)# do-exec show ip ospf nsr <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 20 `；EOL ` RVA 0x33FC8EF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d236fddacacd7923](../../evidence/conditions-sets-081.md#c-d236fddacacd7923) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-049658

```text
(config)# do-exec show ip ospf nsr objects <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 21 `；EOL ` RVA 0x33FC8C20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d236fddacacd7923](../../evidence/conditions-sets-081.md#c-d236fddacacd7923) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-049706

```text
(config)# do-exec show ip ospf nsr statistics <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 22 `；EOL ` RVA 0x33FC8EC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d236fddacacd7923](../../evidence/conditions-sets-081.md#c-d236fddacacd7923) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040873

```text
(config)# do-exec show ip ospf request-list <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 73 `；EOL ` RVA 0x34891878 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-116bd051b88ca966](../../evidence/conditions-sets-007.md#c-116bd051b88ca966) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061648

```text
(config)# do-exec show ip ospf request-list <interface> <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 73 `；EOL ` RVA 0x34891878 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2860eee27973c1b8](../../evidence/conditions-sets-016.md#c-2860eee27973c1b8) · [缺口 G-5ee5d435e7b117a7](../../evidence/gaps-sets-004.md#g-5ee5d435e7b117a7) · [参数 P-61af90c3cc0c36a7](../../evidence/parameters-sets-008.md#p-61af90c3cc0c36a7) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040842

```text
(config)# do-exec show ip ospf retransmission-list <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 72 `；EOL ` RVA 0x34891490 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7a1c7bd5caef7f01](../../evidence/conditions-sets-047.md#c-7a1c7bd5caef7f01) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061647

```text
(config)# do-exec show ip ospf retransmission-list <interface> <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 72 `；EOL ` RVA 0x34891490 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-05edc63bc007e31d](../../evidence/conditions-sets-003.md#c-05edc63bc007e31d) · [缺口 G-ddf5cad6f7926983](../../evidence/gaps-sets-008.md#g-ddf5cad6f7926983) · [参数 P-d0c7091b8167d658](../../evidence/parameters-sets-016.md#p-d0c7091b8167d658) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040488

```text
(config)# do-exec show ip ospf rib <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 19 `；EOL ` RVA 0x34879088 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9a2d99c305604a87](../../evidence/conditions-sets-060.md#c-9a2d99c305604a87) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040489

```text
(config)# do-exec show ip ospf rib <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 18 `；EOL ` RVA 0x34879308 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2ea467d44a1139b0](../../evidence/conditions-sets-018.md#c-2ea467d44a1139b0) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040007

```text
(config)# do-exec show ip ospf sham-links <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 6 `；EOL ` RVA 0x34877308 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040428

```text
(config)# do-exec show ip ospf statistics <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 11 `；EOL ` RVA 0x34879890 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d236fddacacd7923](../../evidence/conditions-sets-081.md#c-d236fddacacd7923) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040283

```text
(config)# do-exec show ip ospf summary-address <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 8 `；EOL ` RVA 0x34878228 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d236fddacacd7923](../../evidence/conditions-sets-081.md#c-d236fddacacd7923) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-049162

```text
(config)# do-exec show ip ospf timers lsa-group <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 12 `；EOL ` RVA 0x34877C08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d236fddacacd7923](../../evidence/conditions-sets-081.md#c-d236fddacacd7923) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-049222

```text
(config)# do-exec show ip ospf timers rate-limit <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 13 `；EOL ` RVA 0x34877EB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d236fddacacd7923](../../evidence/conditions-sets-081.md#c-d236fddacacd7923) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040484

```text
(config)# do-exec show ip ospf topology-info <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 15 `；EOL ` RVA 0x3487A778 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d236fddacacd7923](../../evidence/conditions-sets-081.md#c-d236fddacacd7923) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040758

```text
(config)# do-exec show ip ospf traffic <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 67 `；EOL ` RVA 0x34890680 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-174a88fc5073a64c](../../evidence/conditions-sets-009.md#c-174a88fc5073a64c) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061640

```text
(config)# do-exec show ip ospf traffic <interface> <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 67 `；EOL ` RVA 0x34890680 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2d2cd905f7466d11](../../evidence/conditions-sets-018.md#c-2d2cd905f7466d11) · [缺口 G-b924082425b71df1](../../evidence/gaps-sets-007.md#g-b924082425b71df1) · [参数 P-4087e195c55a7fdd](../../evidence/parameters-sets-005.md#p-4087e195c55a7fdd) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040068

```text
(config)# do-exec show ip ospf virtual-links <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 5 `；EOL ` RVA 0x34876DC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-039797

```text
(config)# do-exec show ip pim autorp <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 46 `；EOL ` RVA 0x34753198 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f7f172e32cfc78a0](../../evidence/conditions-sets-096.md#c-f7f172e32cfc78a0) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062403

```text
(config)# do-exec show ip pim bfd neighbor <interface> inactive <cr>
```

Handler ` RVA 0xC4A31B0 `；selector ` 0 `；EOL ` RVA 0x33A9C0F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-508168d5b7abb112](../../evidence/conditions-sets-031.md#c-508168d5b7abb112) · [缺口 G-3b711376ed9c33c3](../../evidence/gaps-sets-003.md#g-3b711376ed9c33c3) · [参数 P-f19137e773a21890](../../evidence/parameters-sets-018.md#p-f19137e773a21890) · [状态效果 S-c966061ca1ca36bc](../../evidence/state_effects-sets-043.md#s-c966061ca1ca36bc)

### path-055566

```text
(config)# do-exec show ip pim bfd neighbor inactive <cr>
```

Handler ` RVA 0xC4A31B0 `；selector ` 0 `；EOL ` RVA 0x33A9C0F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ddaf11059e672b92](../../evidence/conditions-sets-085.md#c-ddaf11059e672b92) · [状态效果 S-c966061ca1ca36bc](../../evidence/state_effects-sets-043.md#s-c966061ca1ca36bc)

### path-062540

```text
(config)# do-exec show ip pim boundary <interface> <address> <address> in <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 60 `；EOL ` RVA 0x34755E88 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` src address；` address ` grp address。

[条件 C-7662c978ab69abd6](../../evidence/conditions-sets-046.md#c-7662c978ab69abd6) · [缺口 G-e12737a4ff7112ee](../../evidence/gaps-sets-008.md#g-e12737a4ff7112ee) · [参数 P-1424b188ff35c0d2](../../evidence/parameters-sets-002.md#p-1424b188ff35c0d2) · [状态效果 S-fdf9640c35bec32c](../../evidence/state_effects-sets-054.md#s-fdf9640c35bec32c)

### path-039848

```text
(config)# do-exec show ip pim bsr-router <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 20 `；EOL ` RVA 0x34753440 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f7f172e32cfc78a0](../../evidence/conditions-sets-096.md#c-f7f172e32cfc78a0) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-049148

```text
(config)# do-exec show ip pim drlb gdr-candidates <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 79 `；EOL ` RVA 0x34754128 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-434c17223087681a](../../evidence/conditions-sets-026.md#c-434c17223087681a) · [状态效果 S-15a78b2fb4fb7ff2](../../evidence/state_effects-sets-005.md#s-15a78b2fb4fb7ff2)

### path-062078

```text
(config)# do-exec show ip pim drlb gdr-candidates <interface> <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 79 `；EOL ` RVA 0x34754128 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-84b100da3dea374e](../../evidence/conditions-sets-051.md#c-84b100da3dea374e) · [缺口 G-3e32c0ce1ee57818](../../evidence/gaps-sets-003.md#g-3e32c0ce1ee57818) · [参数 P-564edbb49c380db8](../../evidence/parameters-sets-007.md#p-564edbb49c380db8) · [状态效果 S-15a78b2fb4fb7ff2](../../evidence/state_effects-sets-005.md#s-15a78b2fb4fb7ff2)

### path-040267

```text
(config)# do-exec show ip pim gir <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 87 `；EOL ` RVA 0x34756200 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c79cdeeb16a0a23a](../../evidence/conditions-sets-077.md#c-c79cdeeb16a0a23a) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040467

```text
(config)# do-exec show ip pim interface <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 12 `；EOL ` RVA 0x347558F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-07a68833af1a33e6](../../evidence/conditions-sets-003.md#c-07a68833af1a33e6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061603

```text
(config)# do-exec show ip pim interface <interface> <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 12 `；EOL ` RVA 0x347558F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-36df24b5c95a880d](../../evidence/conditions-sets-021.md#c-36df24b5c95a880d) · [缺口 G-351f84834239c90a](../../evidence/gaps-sets-002.md#g-351f84834239c90a) · [参数 P-463e276a391bd8c0](../../evidence/parameters-sets-006.md#p-463e276a391bd8c0) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062110

```text
(config)# do-exec show ip pim interface <interface> bfd <cr>
```

Handler ` RVA 0xC4A31B0 `；selector ` 1 `；EOL ` RVA 0x33A9C488 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-88fcacf1f37932be](../../evidence/conditions-sets-053.md#c-88fcacf1f37932be) · [缺口 G-351f84834239c90a](../../evidence/gaps-sets-002.md#g-351f84834239c90a) · [参数 P-463e276a391bd8c0](../../evidence/parameters-sets-006.md#p-463e276a391bd8c0) · [状态效果 S-e1ad2dbddbb78230](../../evidence/state_effects-sets-048.md#s-e1ad2dbddbb78230)

### path-062087

```text
(config)# do-exec show ip pim interface <interface> detail <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 39 `；EOL ` RVA 0x34755648 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-36df24b5c95a880d](../../evidence/conditions-sets-021.md#c-36df24b5c95a880d) · [缺口 G-351f84834239c90a](../../evidence/gaps-sets-002.md#g-351f84834239c90a) · [参数 P-463e276a391bd8c0](../../evidence/parameters-sets-006.md#p-463e276a391bd8c0) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062083

```text
(config)# do-exec show ip pim interface <interface> traffic <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 96 `；EOL ` RVA 0x347553A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-36df24b5c95a880d](../../evidence/conditions-sets-021.md#c-36df24b5c95a880d) · [缺口 G-351f84834239c90a](../../evidence/gaps-sets-002.md#g-351f84834239c90a) · [参数 P-463e276a391bd8c0](../../evidence/parameters-sets-006.md#p-463e276a391bd8c0) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-049727

```text
(config)# do-exec show ip pim interface bfd <cr>
```

Handler ` RVA 0xC4A31B0 `；selector ` 1 `；EOL ` RVA 0x33A9C488 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d8f0ef3346d04137](../../evidence/conditions-sets-084.md#c-d8f0ef3346d04137) · [状态效果 S-e1ad2dbddbb78230](../../evidence/state_effects-sets-048.md#s-e1ad2dbddbb78230)

### path-049340

```text
(config)# do-exec show ip pim interface detail <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 39 `；EOL ` RVA 0x34755648 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-07a68833af1a33e6](../../evidence/conditions-sets-003.md#c-07a68833af1a33e6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-049277

```text
(config)# do-exec show ip pim interface traffic <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 96 `；EOL ` RVA 0x347553A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-07a68833af1a33e6](../../evidence/conditions-sets-003.md#c-07a68833af1a33e6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040631

```text
(config)# do-exec show ip pim mdt <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 0 `；EOL ` RVA 0x3478DCC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ef425f477cec0d28](../../evidence/conditions-sets-092.md#c-ef425f477cec0d28) · [状态效果 S-89d8f9ed3b36df43](../../evidence/state_effects-sets-029.md#s-89d8f9ed3b36df43)

### path-049837

```text
(config)# do-exec show ip pim mdt bgp <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 1 `；EOL ` RVA 0x3478BB78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ef425f477cec0d28](../../evidence/conditions-sets-092.md#c-ef425f477cec0d28) · [状态效果 S-89d8f9ed3b36df43](../../evidence/state_effects-sets-029.md#s-89d8f9ed3b36df43)

### path-055685

```text
(config)# do-exec show ip pim mdt bgp c-mroutes <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 6 `；EOL ` RVA 0x3478B838 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cf077db1e2ed5988](../../evidence/conditions-sets-080.md#c-cf077db1e2ed5988) · [状态效果 S-8c071e46af7f62fe](../../evidence/state_effects-sets-030.md#s-8c071e46af7f62fe)

### path-058482

```text
(config)# do-exec show ip pim mdt history interval <number:1..71582> <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 2 `；EOL ` RVA 0x3478B440 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` in minutes, maximum is 71582 minutes (7 weeks)。

[条件 C-ef425f477cec0d28](../../evidence/conditions-sets-092.md#c-ef425f477cec0d28) · [参数 P-e84d14ee7ea2ba12](../../evidence/parameters-sets-017.md#p-e84d14ee7ea2ba12) · [状态效果 S-89d8f9ed3b36df43](../../evidence/state_effects-sets-029.md#s-89d8f9ed3b36df43)

### path-055694

```text
(config)# do-exec show ip pim mdt internal bier <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 10 `；EOL ` RVA 0x3478C440 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6db24216c4fdc7ec](../../evidence/conditions-sets-042.md#c-6db24216c4fdc7ec) · [状态效果 S-89d8f9ed3b36df43](../../evidence/state_effects-sets-029.md#s-89d8f9ed3b36df43)

### path-055737

```text
(config)# do-exec show ip pim mdt internal crt <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 11 `；EOL ` RVA 0x3478CEE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7bbaed72ce0a43ad](../../evidence/conditions-sets-048.md#c-7bbaed72ce0a43ad) · [状态效果 S-89d8f9ed3b36df43](../../evidence/state_effects-sets-029.md#s-89d8f9ed3b36df43)

### path-055677

```text
(config)# do-exec show ip pim mdt internal gre <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 7 `；EOL ` RVA 0x3478C198 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f2b4ac5100bf9f7f](../../evidence/conditions-sets-094.md#c-f2b4ac5100bf9f7f) · [状态效果 S-89d8f9ed3b36df43](../../evidence/state_effects-sets-029.md#s-89d8f9ed3b36df43)

### path-055708

```text
(config)# do-exec show ip pim mdt internal ir <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 9 `；EOL ` RVA 0x3478C6E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c16359b8e05cadd8](../../evidence/conditions-sets-075.md#c-c16359b8e05cadd8) · [状态效果 S-89d8f9ed3b36df43](../../evidence/state_effects-sets-029.md#s-89d8f9ed3b36df43)

### path-055720

```text
(config)# do-exec show ip pim mdt internal leaf-ad <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 15 `；EOL ` RVA 0x3478C990 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f5c211cb049c339b](../../evidence/conditions-sets-095.md#c-f5c211cb049c339b) · [状态效果 S-89d8f9ed3b36df43](../../evidence/state_effects-sets-029.md#s-89d8f9ed3b36df43)

### path-055730

```text
(config)# do-exec show ip pim mdt internal mldp <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 8 `；EOL ` RVA 0x3478CC38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ddc67b17a015de2e](../../evidence/conditions-sets-085.md#c-ddc67b17a015de2e) · [状态效果 S-89d8f9ed3b36df43](../../evidence/state_effects-sets-029.md#s-89d8f9ed3b36df43)

### path-055787

```text
(config)# do-exec show ip pim mdt internal pe <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 12 `；EOL ` RVA 0x3478D498 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-76cae2930b2d3c49](../../evidence/conditions-sets-046.md#c-76cae2930b2d3c49) · [状态效果 S-89d8f9ed3b36df43](../../evidence/state_effects-sets-029.md#s-89d8f9ed3b36df43)

### path-058576

```text
(config)# do-exec show ip pim mdt internal pe all <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 14 `；EOL ` RVA 0x3478D740 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-96f6f37effc35394](../../evidence/conditions-sets-058.md#c-96f6f37effc35394) · [状态效果 S-89d8f9ed3b36df43](../../evidence/state_effects-sets-029.md#s-89d8f9ed3b36df43)

### path-055749

```text
(config)# do-exec show ip pim mdt internal replication <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 16 `；EOL ` RVA 0x3478D188 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-742fb4ffa38ff317](../../evidence/conditions-sets-045.md#c-742fb4ffa38ff317) · [状态效果 S-89d8f9ed3b36df43](../../evidence/state_effects-sets-029.md#s-89d8f9ed3b36df43)

### path-055784

```text
(config)# do-exec show ip pim mdt internal tdb <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 13 `；EOL ` RVA 0x3478D9D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-16dedd191bd5cbdd](../../evidence/conditions-sets-009.md#c-16dedd191bd5cbdd) · [状态效果 S-89d8f9ed3b36df43](../../evidence/state_effects-sets-029.md#s-89d8f9ed3b36df43)

### path-055649

```text
(config)# do-exec show ip pim mdt internal vxlan <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 24 `；EOL ` RVA 0x3478BEF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-acd2dbb27d204214](../../evidence/conditions-sets-067.md#c-acd2dbb27d204214) · [状态效果 S-89d8f9ed3b36df43](../../evidence/state_effects-sets-029.md#s-89d8f9ed3b36df43)

### path-049681

```text
(config)# do-exec show ip pim mdt receive <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 3 `；EOL ` RVA 0x3478AEC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ef425f477cec0d28](../../evidence/conditions-sets-092.md#c-ef425f477cec0d28) · [状态效果 S-89d8f9ed3b36df43](../../evidence/state_effects-sets-029.md#s-89d8f9ed3b36df43)

### path-055577

```text
(config)# do-exec show ip pim mdt receive detail <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 4 `；EOL ` RVA 0x3478AEA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ef425f477cec0d28](../../evidence/conditions-sets-092.md#c-ef425f477cec0d28) · [状态效果 S-89d8f9ed3b36df43](../../evidence/state_effects-sets-029.md#s-89d8f9ed3b36df43)

### path-049588

```text
(config)# do-exec show ip pim mdt send <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 5 `；EOL ` RVA 0x3478AB90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ef425f477cec0d28](../../evidence/conditions-sets-092.md#c-ef425f477cec0d28) · [状态效果 S-89d8f9ed3b36df43](../../evidence/state_effects-sets-029.md#s-89d8f9ed3b36df43)

### path-040248

```text
(config)# do-exec show ip pim mvpn <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 52 `；EOL ` RVA 0x34752B10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f7f172e32cfc78a0](../../evidence/conditions-sets-096.md#c-f7f172e32cfc78a0) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-049185

```text
(config)# do-exec show ip pim mvpn bier <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 89 `；EOL ` RVA 0x34752840 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f7f172e32cfc78a0](../../evidence/conditions-sets-096.md#c-f7f172e32cfc78a0) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-048847

```text
(config)# do-exec show ip pim mvpn crt <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 70 `；EOL ` RVA 0x34751850 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f7f172e32cfc78a0](../../evidence/conditions-sets-096.md#c-f7f172e32cfc78a0) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-049137

```text
(config)# do-exec show ip pim mvpn gre <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 90 `；EOL ` RVA 0x34752598 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f7f172e32cfc78a0](../../evidence/conditions-sets-096.md#c-f7f172e32cfc78a0) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-049096

```text
(config)# do-exec show ip pim mvpn ir <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 91 `；EOL ` RVA 0x347522F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f7f172e32cfc78a0](../../evidence/conditions-sets-096.md#c-f7f172e32cfc78a0) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-048987

```text
(config)# do-exec show ip pim mvpn leaf-ad <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 92 `；EOL ` RVA 0x34751DA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f7f172e32cfc78a0](../../evidence/conditions-sets-096.md#c-f7f172e32cfc78a0) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-048703

```text
(config)# do-exec show ip pim mvpn mldp <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 68 `；EOL ` RVA 0x34751300 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f7f172e32cfc78a0](../../evidence/conditions-sets-096.md#c-f7f172e32cfc78a0) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-048775

```text
(config)# do-exec show ip pim mvpn pe <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 69 `；EOL ` RVA 0x347515A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f7f172e32cfc78a0](../../evidence/conditions-sets-096.md#c-f7f172e32cfc78a0) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-048920

```text
(config)# do-exec show ip pim mvpn replication <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 93 `；EOL ` RVA 0x34751AF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f7f172e32cfc78a0](../../evidence/conditions-sets-096.md#c-f7f172e32cfc78a0) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-049053

```text
(config)# do-exec show ip pim mvpn srv6 <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 97 `；EOL ` RVA 0x34752048 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f7f172e32cfc78a0](../../evidence/conditions-sets-096.md#c-f7f172e32cfc78a0) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-049238

```text
(config)# do-exec show ip pim mvpn tdb <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 94 `；EOL ` RVA 0x34752AE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f7f172e32cfc78a0](../../evidence/conditions-sets-096.md#c-f7f172e32cfc78a0) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-048639

```text
(config)# do-exec show ip pim mvpn vxlan <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 95 `；EOL ` RVA 0x34751058 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f7f172e32cfc78a0](../../evidence/conditions-sets-096.md#c-f7f172e32cfc78a0) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-039931

```text
(config)# do-exec show ip pim neighbor <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 10 `；EOL ` RVA 0x347710F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-51b0d38796dd21f0](../../evidence/conditions-sets-032.md#c-51b0d38796dd21f0) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061540

```text
(config)# do-exec show ip pim neighbor <interface> <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 10 `；EOL ` RVA 0x347710F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-01c7f88c0d678a8b](../../evidence/conditions-sets-001.md#c-01c7f88c0d678a8b) · [缺口 G-5bde90dd26461a6c](../../evidence/gaps-sets-004.md#g-5bde90dd26461a6c) · [参数 P-78ff02a4e0cf0889](../../evidence/parameters-sets-009.md#p-78ff02a4e0cf0889) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-048967

```text
(config)# do-exec show ip pim pfp-sa announcements <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 83 `；EOL ` RVA 0x34753790 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a757d600e7b7aab8](../../evidence/conditions-sets-065.md#c-a757d600e7b7aab8) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-049089

```text
(config)# do-exec show ip pim pfp-sa cache <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 86 `；EOL ` RVA 0x34753CE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a757d600e7b7aab8](../../evidence/conditions-sets-065.md#c-a757d600e7b7aab8) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-049038

```text
(config)# do-exec show ip pim pfp-sa originator <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 84 `；EOL ` RVA 0x34753A38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a757d600e7b7aab8](../../evidence/conditions-sets-065.md#c-a757d600e7b7aab8) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040245

```text
(config)# do-exec show ip pim rp <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 11 `；EOL ` RVA 0x34754BB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fa560e3937bdf339](../../evidence/conditions-sets-097.md#c-fa560e3937bdf339) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-049116

```text
(config)# do-exec show ip pim rp-hash <address> <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 22 `；EOL ` RVA 0x34754FF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` group address。

[条件 C-6dbd6590a9eb7383](../../evidence/conditions-sets-042.md#c-6dbd6590a9eb7383) · [参数 P-c66d3e1e0ed7b695](../../evidence/parameters-sets-015.md#p-c66d3e1e0ed7b695) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040242

```text
(config)# do-exec show ip pim tunnel <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 55 `；EOL ` RVA 0x347547A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9bb185ecd494e32d](../../evidence/conditions-sets-060.md#c-9bb185ecd494e32d) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061569

```text
(config)# do-exec show ip pim tunnel <interface> <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 55 `；EOL ` RVA 0x347547A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ec4e95b224360699](../../evidence/conditions-sets-091.md#c-ec4e95b224360699) · [缺口 G-684fdf37951a3f07](../../evidence/gaps-sets-004.md#g-684fdf37951a3f07) · [参数 P-a42cd1aca99fb473](../../evidence/parameters-sets-013.md#p-a42cd1aca99fb473) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062061

```text
(config)# do-exec show ip pim vrf <?option@555589ca4f08> autorp <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 46 `；EOL ` RVA 0x34753198 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-801c8541fcaf55dd](../../evidence/conditions-sets-050.md#c-801c8541fcaf55dd) · [缺口 G-0e6ef693c52c193c](../../evidence/gaps-sets-001.md#g-0e6ef693c52c193c) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062063

```text
(config)# do-exec show ip pim vrf <?option@555589ca4f08> bsr-router <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 20 `；EOL ` RVA 0x34753440 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-801c8541fcaf55dd](../../evidence/conditions-sets-050.md#c-801c8541fcaf55dd) · [缺口 G-0e6ef693c52c193c](../../evidence/gaps-sets-001.md#g-0e6ef693c52c193c) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062088

```text
(config)# do-exec show ip pim vrf <?option@555589ca4f08> gir <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 87 `；EOL ` RVA 0x34756200 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f58366bb8773017e](../../evidence/conditions-sets-095.md#c-f58366bb8773017e) · [缺口 G-0e6ef693c52c193c](../../evidence/gaps-sets-001.md#g-0e6ef693c52c193c) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062125

```text
(config)# do-exec show ip pim vrf <?option@555589ca4f08> mdt <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 0 `；EOL ` RVA 0x3478DCC8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-11441836b618e1c4](../../evidence/conditions-sets-007.md#c-11441836b618e1c4) · [缺口 G-0e6ef693c52c193c](../../evidence/gaps-sets-001.md#g-0e6ef693c52c193c) · [状态效果 S-89d8f9ed3b36df43](../../evidence/state_effects-sets-029.md#s-89d8f9ed3b36df43)

### path-062419

```text
(config)# do-exec show ip pim vrf <?option@555589ca4f08> mdt bgp <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 1 `；EOL ` RVA 0x3478BB78 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-11441836b618e1c4](../../evidence/conditions-sets-007.md#c-11441836b618e1c4) · [缺口 G-0e6ef693c52c193c](../../evidence/gaps-sets-001.md#g-0e6ef693c52c193c) · [状态效果 S-89d8f9ed3b36df43](../../evidence/state_effects-sets-029.md#s-89d8f9ed3b36df43)

### path-062551

```text
(config)# do-exec show ip pim vrf <?option@555589ca4f08> mdt bgp c-mroutes <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 6 `；EOL ` RVA 0x3478B838 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-dd369cbadc9a8763](../../evidence/conditions-sets-085.md#c-dd369cbadc9a8763) · [缺口 G-0e6ef693c52c193c](../../evidence/gaps-sets-001.md#g-0e6ef693c52c193c) · [状态效果 S-8c071e46af7f62fe](../../evidence/state_effects-sets-030.md#s-8c071e46af7f62fe)

### path-062624

```text
(config)# do-exec show ip pim vrf <?option@555589ca4f08> mdt history interval <number:1..71582> <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 2 `；EOL ` RVA 0x3478B440 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` in minutes, maximum is 71582 minutes (7 weeks)。

[条件 C-11441836b618e1c4](../../evidence/conditions-sets-007.md#c-11441836b618e1c4) · [缺口 G-0e6ef693c52c193c](../../evidence/gaps-sets-001.md#g-0e6ef693c52c193c) · [参数 P-e84d14ee7ea2ba12](../../evidence/parameters-sets-017.md#p-e84d14ee7ea2ba12) · [状态效果 S-89d8f9ed3b36df43](../../evidence/state_effects-sets-029.md#s-89d8f9ed3b36df43)

### path-062552

```text
(config)# do-exec show ip pim vrf <?option@555589ca4f08> mdt internal bier <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 10 `；EOL ` RVA 0x3478C440 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-115257db514a4dab](../../evidence/conditions-sets-007.md#c-115257db514a4dab) · [缺口 G-0e6ef693c52c193c](../../evidence/gaps-sets-001.md#g-0e6ef693c52c193c) · [状态效果 S-89d8f9ed3b36df43](../../evidence/state_effects-sets-029.md#s-89d8f9ed3b36df43)

### path-062559

```text
(config)# do-exec show ip pim vrf <?option@555589ca4f08> mdt internal crt <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 11 `；EOL ` RVA 0x3478CEE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f5131e6820f3729f](../../evidence/conditions-sets-095.md#c-f5131e6820f3729f) · [缺口 G-0e6ef693c52c193c](../../evidence/gaps-sets-001.md#g-0e6ef693c52c193c) · [状态效果 S-89d8f9ed3b36df43](../../evidence/state_effects-sets-029.md#s-89d8f9ed3b36df43)

### path-062550

```text
(config)# do-exec show ip pim vrf <?option@555589ca4f08> mdt internal gre <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 7 `；EOL ` RVA 0x3478C198 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4f0e0f630a211931](../../evidence/conditions-sets-031.md#c-4f0e0f630a211931) · [缺口 G-0e6ef693c52c193c](../../evidence/gaps-sets-001.md#g-0e6ef693c52c193c) · [状态效果 S-89d8f9ed3b36df43](../../evidence/state_effects-sets-029.md#s-89d8f9ed3b36df43)

### path-062553

```text
(config)# do-exec show ip pim vrf <?option@555589ca4f08> mdt internal ir <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 9 `；EOL ` RVA 0x3478C6E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a32320b0787d55ab](../../evidence/conditions-sets-063.md#c-a32320b0787d55ab) · [缺口 G-0e6ef693c52c193c](../../evidence/gaps-sets-001.md#g-0e6ef693c52c193c) · [状态效果 S-89d8f9ed3b36df43](../../evidence/state_effects-sets-029.md#s-89d8f9ed3b36df43)

### path-062554

```text
(config)# do-exec show ip pim vrf <?option@555589ca4f08> mdt internal leaf-ad <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 15 `；EOL ` RVA 0x3478C990 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-86bc8987d1bb5191](../../evidence/conditions-sets-052.md#c-86bc8987d1bb5191) · [缺口 G-0e6ef693c52c193c](../../evidence/gaps-sets-001.md#g-0e6ef693c52c193c) · [状态效果 S-89d8f9ed3b36df43](../../evidence/state_effects-sets-029.md#s-89d8f9ed3b36df43)

### path-062558

```text
(config)# do-exec show ip pim vrf <?option@555589ca4f08> mdt internal mldp <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 8 `；EOL ` RVA 0x3478CC38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3cc07811e509b418](../../evidence/conditions-sets-024.md#c-3cc07811e509b418) · [缺口 G-0e6ef693c52c193c](../../evidence/gaps-sets-001.md#g-0e6ef693c52c193c) · [状态效果 S-89d8f9ed3b36df43](../../evidence/state_effects-sets-029.md#s-89d8f9ed3b36df43)

### path-062562

```text
(config)# do-exec show ip pim vrf <?option@555589ca4f08> mdt internal pe <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 12 `；EOL ` RVA 0x3478D498 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-62f64a86571169e2](../../evidence/conditions-sets-038.md#c-62f64a86571169e2) · [缺口 G-0e6ef693c52c193c](../../evidence/gaps-sets-001.md#g-0e6ef693c52c193c) · [状态效果 S-89d8f9ed3b36df43](../../evidence/state_effects-sets-029.md#s-89d8f9ed3b36df43)

### path-062627

```text
(config)# do-exec show ip pim vrf <?option@555589ca4f08> mdt internal pe all <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 14 `；EOL ` RVA 0x3478D740 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d5bc5487af463548](../../evidence/conditions-sets-082.md#c-d5bc5487af463548) · [缺口 G-0e6ef693c52c193c](../../evidence/gaps-sets-001.md#g-0e6ef693c52c193c) · [状态效果 S-89d8f9ed3b36df43](../../evidence/state_effects-sets-029.md#s-89d8f9ed3b36df43)

### path-062560

```text
(config)# do-exec show ip pim vrf <?option@555589ca4f08> mdt internal replication <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 16 `；EOL ` RVA 0x3478D188 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-cd7ff4074b637227](../../evidence/conditions-sets-079.md#c-cd7ff4074b637227) · [缺口 G-0e6ef693c52c193c](../../evidence/gaps-sets-001.md#g-0e6ef693c52c193c) · [状态效果 S-89d8f9ed3b36df43](../../evidence/state_effects-sets-029.md#s-89d8f9ed3b36df43)

### path-062561

```text
(config)# do-exec show ip pim vrf <?option@555589ca4f08> mdt internal tdb <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 13 `；EOL ` RVA 0x3478D9D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9156326c63ae2c41](../../evidence/conditions-sets-056.md#c-9156326c63ae2c41) · [缺口 G-0e6ef693c52c193c](../../evidence/gaps-sets-001.md#g-0e6ef693c52c193c) · [状态效果 S-89d8f9ed3b36df43](../../evidence/state_effects-sets-029.md#s-89d8f9ed3b36df43)

### path-062549

```text
(config)# do-exec show ip pim vrf <?option@555589ca4f08> mdt internal vxlan <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 24 `；EOL ` RVA 0x3478BEF0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-25e5ffb8dd4726cf](../../evidence/conditions-sets-015.md#c-25e5ffb8dd4726cf) · [缺口 G-0e6ef693c52c193c](../../evidence/gaps-sets-001.md#g-0e6ef693c52c193c) · [状态效果 S-89d8f9ed3b36df43](../../evidence/state_effects-sets-029.md#s-89d8f9ed3b36df43)

### path-062411

```text
(config)# do-exec show ip pim vrf <?option@555589ca4f08> mdt receive <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 3 `；EOL ` RVA 0x3478AEC8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-11441836b618e1c4](../../evidence/conditions-sets-007.md#c-11441836b618e1c4) · [缺口 G-0e6ef693c52c193c](../../evidence/gaps-sets-001.md#g-0e6ef693c52c193c) · [状态效果 S-89d8f9ed3b36df43](../../evidence/state_effects-sets-029.md#s-89d8f9ed3b36df43)

### path-062548

```text
(config)# do-exec show ip pim vrf <?option@555589ca4f08> mdt receive detail <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 4 `；EOL ` RVA 0x3478AEA0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-11441836b618e1c4](../../evidence/conditions-sets-007.md#c-11441836b618e1c4) · [缺口 G-0e6ef693c52c193c](../../evidence/gaps-sets-001.md#g-0e6ef693c52c193c) · [状态效果 S-89d8f9ed3b36df43](../../evidence/state_effects-sets-029.md#s-89d8f9ed3b36df43)

### path-062404

```text
(config)# do-exec show ip pim vrf <?option@555589ca4f08> mdt send <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 5 `；EOL ` RVA 0x3478AB90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-11441836b618e1c4](../../evidence/conditions-sets-007.md#c-11441836b618e1c4) · [缺口 G-0e6ef693c52c193c](../../evidence/gaps-sets-001.md#g-0e6ef693c52c193c) · [状态效果 S-89d8f9ed3b36df43](../../evidence/state_effects-sets-029.md#s-89d8f9ed3b36df43)

### path-062086

```text
(config)# do-exec show ip pim vrf <?option@555589ca4f08> mvpn <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 52 `；EOL ` RVA 0x34752B10 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-801c8541fcaf55dd](../../evidence/conditions-sets-050.md#c-801c8541fcaf55dd) · [缺口 G-0e6ef693c52c193c](../../evidence/gaps-sets-001.md#g-0e6ef693c52c193c) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062390

```text
(config)# do-exec show ip pim vrf <?option@555589ca4f08> mvpn bier <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 89 `；EOL ` RVA 0x34752840 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-801c8541fcaf55dd](../../evidence/conditions-sets-050.md#c-801c8541fcaf55dd) · [缺口 G-0e6ef693c52c193c](../../evidence/gaps-sets-001.md#g-0e6ef693c52c193c) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062369

```text
(config)# do-exec show ip pim vrf <?option@555589ca4f08> mvpn crt <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 70 `；EOL ` RVA 0x34751850 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-801c8541fcaf55dd](../../evidence/conditions-sets-050.md#c-801c8541fcaf55dd) · [缺口 G-0e6ef693c52c193c](../../evidence/gaps-sets-001.md#g-0e6ef693c52c193c) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062386

```text
(config)# do-exec show ip pim vrf <?option@555589ca4f08> mvpn gre <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 90 `；EOL ` RVA 0x34752598 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-801c8541fcaf55dd](../../evidence/conditions-sets-050.md#c-801c8541fcaf55dd) · [缺口 G-0e6ef693c52c193c](../../evidence/gaps-sets-001.md#g-0e6ef693c52c193c) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062382

```text
(config)# do-exec show ip pim vrf <?option@555589ca4f08> mvpn ir <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 91 `；EOL ` RVA 0x347522F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-801c8541fcaf55dd](../../evidence/conditions-sets-050.md#c-801c8541fcaf55dd) · [缺口 G-0e6ef693c52c193c](../../evidence/gaps-sets-001.md#g-0e6ef693c52c193c) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062375

```text
(config)# do-exec show ip pim vrf <?option@555589ca4f08> mvpn leaf-ad <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 92 `；EOL ` RVA 0x34751DA0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-801c8541fcaf55dd](../../evidence/conditions-sets-050.md#c-801c8541fcaf55dd) · [缺口 G-0e6ef693c52c193c](../../evidence/gaps-sets-001.md#g-0e6ef693c52c193c) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062363

```text
(config)# do-exec show ip pim vrf <?option@555589ca4f08> mvpn mldp <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 68 `；EOL ` RVA 0x34751300 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-801c8541fcaf55dd](../../evidence/conditions-sets-050.md#c-801c8541fcaf55dd) · [缺口 G-0e6ef693c52c193c](../../evidence/gaps-sets-001.md#g-0e6ef693c52c193c) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062366

```text
(config)# do-exec show ip pim vrf <?option@555589ca4f08> mvpn pe <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 69 `；EOL ` RVA 0x347515A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-801c8541fcaf55dd](../../evidence/conditions-sets-050.md#c-801c8541fcaf55dd) · [缺口 G-0e6ef693c52c193c](../../evidence/gaps-sets-001.md#g-0e6ef693c52c193c) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062371

```text
(config)# do-exec show ip pim vrf <?option@555589ca4f08> mvpn replication <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 93 `；EOL ` RVA 0x34751AF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-801c8541fcaf55dd](../../evidence/conditions-sets-050.md#c-801c8541fcaf55dd) · [缺口 G-0e6ef693c52c193c](../../evidence/gaps-sets-001.md#g-0e6ef693c52c193c) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062378

```text
(config)# do-exec show ip pim vrf <?option@555589ca4f08> mvpn srv6 <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 97 `；EOL ` RVA 0x34752048 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-801c8541fcaf55dd](../../evidence/conditions-sets-050.md#c-801c8541fcaf55dd) · [缺口 G-0e6ef693c52c193c](../../evidence/gaps-sets-001.md#g-0e6ef693c52c193c) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062391

```text
(config)# do-exec show ip pim vrf <?option@555589ca4f08> mvpn tdb <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 94 `；EOL ` RVA 0x34752AE8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-801c8541fcaf55dd](../../evidence/conditions-sets-050.md#c-801c8541fcaf55dd) · [缺口 G-0e6ef693c52c193c](../../evidence/gaps-sets-001.md#g-0e6ef693c52c193c) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062361

```text
(config)# do-exec show ip pim vrf <?option@555589ca4f08> mvpn vxlan <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 95 `；EOL ` RVA 0x34751058 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-801c8541fcaf55dd](../../evidence/conditions-sets-050.md#c-801c8541fcaf55dd) · [缺口 G-0e6ef693c52c193c](../../evidence/gaps-sets-001.md#g-0e6ef693c52c193c) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062374

```text
(config)# do-exec show ip pim vrf <?option@555589ca4f08> pfp-sa announcements <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 83 `；EOL ` RVA 0x34753790 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-04d51091b2cb6e5b](../../evidence/conditions-sets-002.md#c-04d51091b2cb6e5b) · [缺口 G-0e6ef693c52c193c](../../evidence/gaps-sets-001.md#g-0e6ef693c52c193c) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062381

```text
(config)# do-exec show ip pim vrf <?option@555589ca4f08> pfp-sa cache <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 86 `；EOL ` RVA 0x34753CE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-04d51091b2cb6e5b](../../evidence/conditions-sets-002.md#c-04d51091b2cb6e5b) · [缺口 G-0e6ef693c52c193c](../../evidence/gaps-sets-001.md#g-0e6ef693c52c193c) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062377

```text
(config)# do-exec show ip pim vrf <?option@555589ca4f08> pfp-sa originator <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 84 `；EOL ` RVA 0x34753A38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-04d51091b2cb6e5b](../../evidence/conditions-sets-002.md#c-04d51091b2cb6e5b) · [缺口 G-0e6ef693c52c193c](../../evidence/gaps-sets-001.md#g-0e6ef693c52c193c) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062085

```text
(config)# do-exec show ip pim vrf <?option@555589ca4f08> rp <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 11 `；EOL ` RVA 0x34754BB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-873cce75311ab172](../../evidence/conditions-sets-052.md#c-873cce75311ab172) · [缺口 G-0e6ef693c52c193c](../../evidence/gaps-sets-001.md#g-0e6ef693c52c193c) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062385

```text
(config)# do-exec show ip pim vrf <?option@555589ca4f08> rp-hash <address> <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 22 `；EOL ` RVA 0x34754FF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` group address。

[条件 C-d0f9770a25611fe5](../../evidence/conditions-sets-080.md#c-d0f9770a25611fe5) · [缺口 G-0e6ef693c52c193c](../../evidence/gaps-sets-001.md#g-0e6ef693c52c193c) · [参数 P-c66d3e1e0ed7b695](../../evidence/parameters-sets-015.md#p-c66d3e1e0ed7b695) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031925

```text
(config)# do-exec show ip policy <cr>
```

Handler ` RVA 0xFAD9620 `；selector ` 0 `；EOL ` RVA 0x34804A80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040076

```text
(config)# do-exec show ip policy adj-subblock <cr>
```

Handler ` RVA 0xFAD9440 `；selector ` 0 `；EOL ` RVA 0x34804A58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031593

```text
(config)# do-exec show ip policy-list <cr>
```

Handler ` RVA 0xE218540 `；selector ` 0 `；EOL ` RVA 0x344BABE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-058105

```text
(config)# do-exec show ip portbundle ip <address> bundle <number:1..65535> <cr>
```

Handler ` RVA 0x11C31540 `；selector ` 0 `；EOL ` RVA 0x356A5148 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Portbundle IP address；` unsigned_number ` Portbundle bundle number。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-81af61e5ba4224a6](../../evidence/parameters-sets-010.md#p-81af61e5ba4224a6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-038928

```text
(config)# do-exec show ip portbundle status <cr>
```

Handler ` RVA 0x11C31540 `；selector ` 1 `；EOL ` RVA 0x356A4DE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-047864

```text
(config)# do-exec show ip portbundle status free <cr>
```

Handler ` RVA 0x11C31540 `；selector ` 2 `；EOL ` RVA 0x356A4B28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-8705f9865c1fb147](../../evidence/state_effects-sets-029.md#s-8705f9865c1fb147)

### path-039052

```text
(config)# do-exec show ip ports all <cr>
```

Handler ` RVA 0xCE51730 `；selector ` 0 `；EOL ` RVA 0x33CF6FA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-038995

```text
(config)# do-exec show ip ports ephemeral-max <cr>
```

Handler ` RVA 0xCDEFA80 `；selector ` 0 `；EOL ` RVA 0x33CF6D00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-039108

```text
(config)# do-exec show ip ports reservation <cr>
```

Handler ` RVA 0xCE518D0 `；selector ` 0 `；EOL ` RVA 0x33CF7250 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6a825157ac462ea](../../evidence/conditions-sets-077.md#c-c6a825157ac462ea) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032126

```text
(config)# do-exec show ip prefix-list <cr>
```

Handler ` RVA 0xE2203B0 `；selector ` 0 `；EOL ` RVA 0x342832B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ddcaf979b496d8fc](../../evidence/conditions-sets-085.md#c-ddcaf979b496d8fc) · [状态效果 S-ca5bec2f952ca2c4](../../evidence/state_effects-sets-043.md#s-ca5bec2f952ca2c4)

### path-061636

```text
(config)# do-exec show ip prefix-list <string> <prefix:dynamic> <cr>
```

Handler ` RVA 0xE2203B0 `；selector ` 4 `；EOL ` RVA 0x34283688 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Name of a prefix list；` prefix_dynamic ` IP prefix &lt;network&gt;/&lt;length&gt;, e.g., 10.0.0.0/8。

[条件 C-cfe25cb3d2359b40](../../evidence/conditions-sets-080.md#c-cfe25cb3d2359b40) · [缺口 G-2196acf0a1478dd3](../../evidence/gaps-sets-002.md#g-2196acf0a1478dd3) · [参数 P-89e89425649c4718](../../evidence/parameters-sets-011.md#p-89e89425649c4718) · [状态效果 S-ca5bec2f952ca2c4](../../evidence/state_effects-sets-043.md#s-ca5bec2f952ca2c4)

### path-055672

```text
(config)# do-exec show ip prefix-list <string> seq <number:1..4294967295> <cr>
```

Handler ` RVA 0xE2203B0 `；selector ` 3 `；EOL ` RVA 0x34283358 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of a prefix list；` unsigned_number ` Sequence number。

[条件 C-ddcaf979b496d8fc](../../evidence/conditions-sets-085.md#c-ddcaf979b496d8fc) · [参数 P-0d71bd8044f6fc2b](../../evidence/parameters-sets-001.md#p-0d71bd8044f6fc2b) · [状态效果 S-ca5bec2f952ca2c4](../../evidence/state_effects-sets-043.md#s-ca5bec2f952ca2c4)

### path-040564

```text
(config)# do-exec show ip prefix-list detail <cr>
```

Handler ` RVA 0xE2203B0 `；selector ` 2 `；EOL ` RVA 0x34282FB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-ca5bec2f952ca2c4](../../evidence/state_effects-sets-043.md#s-ca5bec2f952ca2c4)

### path-040541

```text
(config)# do-exec show ip prefix-list summary <cr>
```

Handler ` RVA 0xE2203B0 `；selector ` 1 `；EOL ` RVA 0x34282CA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-ca5bec2f952ca2c4](../../evidence/state_effects-sets-043.md#s-ca5bec2f952ca2c4)

### path-031611

```text
(config)# do-exec show ip protocols <cr>
```

Handler ` RVA 0xE1F60E0 `；selector ` 0 `；EOL ` RVA 0x3422FAB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-662dab67c3ad9644](../../evidence/conditions-sets-039.md#c-662dab67c3ad9644) · [状态效果 S-2baee5e9fdac4e2d](../../evidence/state_effects-sets-010.md#s-2baee5e9fdac4e2d)

### path-039216

```text
(config)# do-exec show ip protocols summary <cr>
```

Handler ` RVA 0xE1F5DF0 `；selector ` 0 `；EOL ` RVA 0x3422FA88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-662dab67c3ad9644](../../evidence/conditions-sets-039.md#c-662dab67c3ad9644) · [状态效果 S-2baee5e9fdac4e2d](../../evidence/state_effects-sets-010.md#s-2baee5e9fdac4e2d)

### path-061014

```text
(config)# do-exec show ip reassembly <interface> <cr>
```

Handler ` RVA 0xC78EA70 `；selector ` 0 `；EOL ` RVA 0x33AECED0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4d42d402b87bd690](../../evidence/conditions-sets-030.md#c-4d42d402b87bd690) · [缺口 G-e7f0c28428edc901](../../evidence/gaps-sets-008.md#g-e7f0c28428edc901) · [参数 P-0e83b0412d60a526](../../evidence/parameters-sets-002.md#p-0e83b0412d60a526) · [状态效果 S-06552c761ce77d44](../../evidence/state_effects-sets-002.md#s-06552c761ce77d44)

### path-031072

```text
(config)# do-exec show ip redirects <cr>
```

Handler ` RVA 0xCF509C0 `；selector ` 0 `；EOL ` RVA 0x33D31570 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-039276

```text
(config)# do-exec show ip rib database <cr>
```

Handler ` RVA 0xDC0B310 `；selector ` 1 `；EOL ` RVA 0x3422F578 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-aa3e36e3194bcd23](../../evidence/conditions-sets-066.md#c-aa3e36e3194bcd23) · [状态效果 S-6ef5e0ddff3f980b](../../evidence/state_effects-sets-024.md#s-6ef5e0ddff3f980b)

### path-061507

```text
(config)# do-exec show ip rib route <?router_action_proc_vpn@555589783268> <cr>
```

Handler ` RVA 0xDC0B310 `；selector ` 2 `；EOL ` RVA 0x3422F2D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-aa3e36e3194bcd23](../../evidence/conditions-sets-066.md#c-aa3e36e3194bcd23) · [缺口 G-95f60b11cd716043](../../evidence/gaps-sets-005.md#g-95f60b11cd716043) · [状态效果 S-6ef5e0ddff3f980b](../../evidence/state_effects-sets-024.md#s-6ef5e0ddff3f980b)

### path-040281

```text
(config)# do-exec show ip rip database <cr>
```

Handler ` RVA 0xFB73AB0 `；selector ` 0 `；EOL ` RVA 0x34822820 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7c00b49cbd29f681](../../evidence/conditions-sets-048.md#c-7c00b49cbd29f681) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040260

```text
(config)# do-exec show ip rip neighbors <cr>
```

Handler ` RVA 0xFB52AC0 `；selector ` 0 `；EOL ` RVA 0x34822B40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-662365bd75b0a5eb](../../evidence/conditions-sets-039.md#c-662365bd75b0a5eb) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040125

```text
(config)# do-exec show ip rip timers <cr>
```

Handler ` RVA 0xFB56CB0 `；selector ` 0 `；EOL ` RVA 0x34822428 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062978

```text
(config)# do-exec show ip route <?router_action_no_proc_vpn@5555897853d8> <address> getnext <cr>
```

Handler ` RVA 0xE1CEA80 `；selector ` 8 `；EOL ` RVA 0x34233BA8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Network to display information about or hostname。

[条件 C-ca659dedd76e894e](../../evidence/conditions-sets-078.md#c-ca659dedd76e894e) · [缺口 G-a88c03ded52cad18](../../evidence/gaps-sets-006.md#g-a88c03ded52cad18) · [参数 P-2f6a56dcc94741bf](../../evidence/parameters-sets-004.md#p-2f6a56dcc94741bf) · [状态效果 S-fce107547bb32f82](../../evidence/state_effects-sets-054.md#s-fce107547bb32f82)

### path-062979

```text
(config)# do-exec show ip route <?router_action_no_proc_vpn@5555897853d8> <address> getprev <cr>
```

Handler ` RVA 0xE1CEA80 `；selector ` 9 `；EOL ` RVA 0x34233E50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Network to display information about or hostname。

[条件 C-ca659dedd76e894e](../../evidence/conditions-sets-078.md#c-ca659dedd76e894e) · [缺口 G-a88c03ded52cad18](../../evidence/gaps-sets-006.md#g-a88c03ded52cad18) · [参数 P-2f6a56dcc94741bf](../../evidence/parameters-sets-004.md#p-2f6a56dcc94741bf) · [状态效果 S-fce107547bb32f82](../../evidence/state_effects-sets-054.md#s-fce107547bb32f82)

### path-062980

```text
(config)# do-exec show ip route <?router_action_no_proc_vpn@5555897853d8> <address> longer-prefixes <cr>
```

Handler ` RVA 0xE1CEA80 `；selector ` 7 `；EOL ` RVA 0x342340F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Network to display information about or hostname。

[条件 C-ca659dedd76e894e](../../evidence/conditions-sets-078.md#c-ca659dedd76e894e) · [缺口 G-a88c03ded52cad18](../../evidence/gaps-sets-006.md#g-a88c03ded52cad18) · [参数 P-2f6a56dcc94741bf](../../evidence/parameters-sets-004.md#p-2f6a56dcc94741bf) · [状态效果 S-fce107547bb32f82](../../evidence/state_effects-sets-054.md#s-fce107547bb32f82)

### path-062977

```text
(config)# do-exec show ip route <?router_action_no_proc_vpn@5555897853d8> <address> resolve <cr>
```

Handler ` RVA 0xE1CEA80 `；selector ` 10 `；EOL ` RVA 0x34233900 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Network to display information about or hostname。

[条件 C-ca659dedd76e894e](../../evidence/conditions-sets-078.md#c-ca659dedd76e894e) · [缺口 G-a88c03ded52cad18](../../evidence/gaps-sets-006.md#g-a88c03ded52cad18) · [参数 P-2f6a56dcc94741bf](../../evidence/parameters-sets-004.md#p-2f6a56dcc94741bf) · [状态效果 S-fce107547bb32f82](../../evidence/state_effects-sets-054.md#s-fce107547bb32f82)

### path-062954

```text
(config)# do-exec show ip route <?router_action_no_proc_vpn@5555897853d8> <cr>
```

Handler ` RVA 0xE1CEA80 `；selector ` 0 `；EOL ` RVA 0x34231710 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ed73fbc4c20989f1](../../evidence/conditions-sets-092.md#c-ed73fbc4c20989f1) · [缺口 G-7a24ab141841f0e8](../../evidence/gaps-sets-005.md#g-7a24ab141841f0e8) · [状态效果 S-4db7c88b6f00ee96](../../evidence/state_effects-sets-017.md#s-4db7c88b6f00ee96)

### path-062964

```text
(config)# do-exec show ip route <?router_action_no_proc_vpn@5555897853d8> cidr <cr>
```

Handler ` RVA 0xE1CEA80 `；selector ` 6 `；EOL ` RVA 0x34233298 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-66e16a300f07410c](../../evidence/conditions-sets-040.md#c-66e16a300f07410c) · [缺口 G-a88c03ded52cad18](../../evidence/gaps-sets-006.md#g-a88c03ded52cad18) · [状态效果 S-fce107547bb32f82](../../evidence/state_effects-sets-054.md#s-fce107547bb32f82)

### path-062965

```text
(config)# do-exec show ip route <?router_action_no_proc_vpn@5555897853d8> dhcp <cr>
```

Handler ` RVA 0xE1CEA80 `；selector ` 13 `；EOL ` RVA 0x342335A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-66e16a300f07410c](../../evidence/conditions-sets-040.md#c-66e16a300f07410c) · [缺口 G-a88c03ded52cad18](../../evidence/gaps-sets-006.md#g-a88c03ded52cad18) · [状态效果 S-fce107547bb32f82](../../evidence/state_effects-sets-054.md#s-fce107547bb32f82)

### path-062961

```text
(config)# do-exec show ip route <?router_action_no_proc_vpn@5555897853d8> download <cr>
```

Handler ` RVA 0xCF9ADF0 `；selector ` 3 `；EOL ` RVA 0x342319E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f549e892b7b6eb6a](../../evidence/conditions-sets-095.md#c-f549e892b7b6eb6a) · [缺口 G-7a24ab141841f0e8](../../evidence/gaps-sets-005.md#g-7a24ab141841f0e8) · [状态效果 S-4db7c88b6f00ee96](../../evidence/state_effects-sets-017.md#s-4db7c88b6f00ee96)

### path-061522

```text
(config)# do-exec show ip route <?router_action_no_proc_vpn@5555897853d8> loops <cr>
```

Handler ` RVA 0xDBE99E0 `；selector ` 0 `；EOL ` RVA 0x34231F18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-bfe07068749ae3df](../../evidence/conditions-sets-074.md#c-bfe07068749ae3df) · [缺口 G-03c6795a1cd09c6e](../../evidence/gaps-sets-001.md#g-03c6795a1cd09c6e) · [状态效果 S-954e3a806575dac4](../../evidence/state_effects-sets-032.md#s-954e3a806575dac4)

### path-062962

```text
(config)# do-exec show ip route <?router_action_no_proc_vpn@5555897853d8> majornets-only <cr>
```

Handler ` RVA 0xE1CEA80 `；selector ` 5 `；EOL ` RVA 0x34232D48 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-66e16a300f07410c](../../evidence/conditions-sets-040.md#c-66e16a300f07410c) · [缺口 G-a88c03ded52cad18](../../evidence/gaps-sets-006.md#g-a88c03ded52cad18) · [状态效果 S-fce107547bb32f82](../../evidence/state_effects-sets-054.md#s-fce107547bb32f82)

### path-061520

```text
(config)# do-exec show ip route <?router_action_no_proc_vpn@5555897853d8> profile <cr>
```

Handler ` RVA 0xE1ADBE0 `；selector ` 0 `；EOL ` RVA 0x34231C70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-bfe07068749ae3df](../../evidence/conditions-sets-074.md#c-bfe07068749ae3df) · [缺口 G-03c6795a1cd09c6e](../../evidence/gaps-sets-001.md#g-03c6795a1cd09c6e) · [状态效果 S-954e3a806575dac4](../../evidence/state_effects-sets-032.md#s-954e3a806575dac4)

### path-061534

```text
(config)# do-exec show ip route <?router_action_no_proc_vpn@5555897853d8> replicate <cr>
```

Handler ` RVA 0xE1CEA80 `；selector ` 11 `；EOL ` RVA 0x342329C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-bfe07068749ae3df](../../evidence/conditions-sets-074.md#c-bfe07068749ae3df) · [缺口 G-03c6795a1cd09c6e](../../evidence/gaps-sets-001.md#g-03c6795a1cd09c6e) · [状态效果 S-954e3a806575dac4](../../evidence/state_effects-sets-032.md#s-954e3a806575dac4)

### path-061531

```text
(config)# do-exec show ip route <?router_action_no_proc_vpn@5555897853d8> static-table <cr>
```

Handler ` RVA 0xE2A4BF0 `；selector ` 0 `；EOL ` RVA 0x34232710 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-bfe07068749ae3df](../../evidence/conditions-sets-074.md#c-bfe07068749ae3df) · [缺口 G-03c6795a1cd09c6e](../../evidence/gaps-sets-001.md#g-03c6795a1cd09c6e) · [状态效果 S-954e3a806575dac4](../../evidence/state_effects-sets-032.md#s-954e3a806575dac4)

### path-061526

```text
(config)# do-exec show ip route <?router_action_no_proc_vpn@5555897853d8> summary <cr>
```

Handler ` RVA 0xE1D59C0 `；selector ` 0 `；EOL ` RVA 0x342321C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-bfe07068749ae3df](../../evidence/conditions-sets-074.md#c-bfe07068749ae3df) · [缺口 G-03c6795a1cd09c6e](../../evidence/gaps-sets-001.md#g-03c6795a1cd09c6e) · [状态效果 S-954e3a806575dac4](../../evidence/state_effects-sets-032.md#s-954e3a806575dac4)

### path-062963

```text
(config)# do-exec show ip route <?router_action_no_proc_vpn@5555897853d8> supernets-only <cr>
```

Handler ` RVA 0xE1CEA80 `；selector ` 4 `；EOL ` RVA 0x34232FF0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-66e16a300f07410c](../../evidence/conditions-sets-040.md#c-66e16a300f07410c) · [缺口 G-a88c03ded52cad18](../../evidence/gaps-sets-006.md#g-a88c03ded52cad18) · [状态效果 S-fce107547bb32f82](../../evidence/state_effects-sets-054.md#s-fce107547bb32f82)

### path-061530

```text
(config)# do-exec show ip route <?router_action_no_proc_vpn@5555897853d8> track-table <cr>
```

Handler ` RVA 0xD4A59D0 `；selector ` 0 `；EOL ` RVA 0x34232468 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-bfe07068749ae3df](../../evidence/conditions-sets-074.md#c-bfe07068749ae3df) · [缺口 G-03c6795a1cd09c6e](../../evidence/gaps-sets-001.md#g-03c6795a1cd09c6e) · [状态效果 S-954e3a806575dac4](../../evidence/state_effects-sets-032.md#s-954e3a806575dac4)

### path-048326

```text
(config)# do-exec show ip route list <number:1..199> <cr>
```

Handler ` RVA 0xE1CEA80 `；selector ` 12 `；EOL ` RVA 0x34230C38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` IP access list number。

[条件 C-ccae3c6fa6a19008](../../evidence/conditions-sets-079.md#c-ccae3c6fa6a19008) · [参数 P-6f46a0106e78d96b](../../evidence/parameters-sets-009.md#p-6f46a0106e78d96b) · [状态效果 S-954e3a806575dac4](../../evidence/state_effects-sets-032.md#s-954e3a806575dac4)

### path-048428

```text
(config)# do-exec show ip route omp-tag <number:0..4294967295> <cr>
```

Handler ` RVA 0xE1CEA80 `；selector ` 15 `；EOL ` RVA 0x34231420 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Overlay Management Protocol (OMP) Tag value。

[条件 C-bfe07068749ae3df](../../evidence/conditions-sets-074.md#c-bfe07068749ae3df) · [参数 P-1586b2be9da07e52](../../evidence/parameters-sets-002.md#p-1586b2be9da07e52) · [状态效果 S-954e3a806575dac4](../../evidence/state_effects-sets-032.md#s-954e3a806575dac4)

### path-062849

```text
(config)# do-exec show ip route tag <address> <cr>
```

Handler ` RVA 0xE1CEA80 `；selector ` 14 `；EOL ` RVA 0x34231000 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Tag in Dotted Decimal eg, 10.10.10.10。

[条件 C-247403f934361232](../../evidence/conditions-sets-014.md#c-247403f934361232) · [缺口 G-c3b5f9d4e2770976](../../evidence/gaps-sets-007.md#g-c3b5f9d4e2770976) · [参数 P-b21618ac46d8197c](../../evidence/parameters-sets-014.md#p-b21618ac46d8197c) · [状态效果 S-0c7f3a6525830e4a](../../evidence/state_effects-sets-003.md#s-0c7f3a6525830e4a)

### path-048427

```text
(config)# do-exec show ip route tag <number:0..4294967295> <cr>
```

Handler ` RVA 0xE1CEA80 `；selector ` 14 `；EOL ` RVA 0x34231000 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Tag value。

[条件 C-247403f934361232](../../evidence/conditions-sets-014.md#c-247403f934361232) · [参数 P-e0210763947c7838](../../evidence/parameters-sets-017.md#p-e0210763947c7838) · [状态效果 S-954e3a806575dac4](../../evidence/state_effects-sets-032.md#s-954e3a806575dac4)

### path-054818

```text
(config)# do-exec show ip route tree <address> <address> <cr>
```

Handler ` RVA 0xE1CEA80 `；selector ` 3 `；EOL ` RVA 0x34230700 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Network to display information about；` address ` Network mask。

[条件 C-ccae3c6fa6a19008](../../evidence/conditions-sets-079.md#c-ccae3c6fa6a19008) · [参数 P-3c5f288fee4ae5f4](../../evidence/parameters-sets-005.md#p-3c5f288fee4ae5f4) · [状态效果 S-954e3a806575dac4](../../evidence/state_effects-sets-032.md#s-954e3a806575dac4)

### path-039437

```text
(config)# do-exec show ip route tree <cr>
```

Handler ` RVA 0xE1CEA80 `；selector ` 1 `；EOL ` RVA 0x342306C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ccae3c6fa6a19008](../../evidence/conditions-sets-079.md#c-ccae3c6fa6a19008) · [状态效果 S-954e3a806575dac4](../../evidence/state_effects-sets-032.md#s-954e3a806575dac4)

### path-048285

```text
(config)# do-exec show ip route tree summary <cr>
```

Handler ` RVA 0xE1CEA80 `；selector ` 2 `；EOL ` RVA 0x342303F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ccae3c6fa6a19008](../../evidence/conditions-sets-079.md#c-ccae3c6fa6a19008) · [状态效果 S-954e3a806575dac4](../../evidence/state_effects-sets-032.md#s-954e3a806575dac4)

### path-062388

```text
(config)# do-exec show ip rpf <address> <address> rd <?vrf_rd_action@555589ca4700> <cr>
```

Handler ` RVA 0xF740240 `；selector ` 0 `；EOL ` RVA 0x34750190 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` IP name or address of multicast source；` address ` IP name or address of multicast group。

[条件 C-895bb1c7e416283c](../../evidence/conditions-sets-053.md#c-895bb1c7e416283c) · [缺口 G-237000f253fcb8fe](../../evidence/gaps-sets-002.md#g-237000f253fcb8fe) · [参数 P-d492befd77cb8d43](../../evidence/parameters-sets-016.md#p-d492befd77cb8d43) · [状态效果 S-f4ddc638ad858007](../../evidence/state_effects-sets-052.md#s-f4ddc638ad858007)

### path-039586

```text
(config)# do-exec show ip rpf queued <cr>
```

Handler ` RVA 0xF740240 `；selector ` 0 `；EOL ` RVA 0x34750190 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f7f172e32cfc78a0](../../evidence/conditions-sets-096.md#c-f7f172e32cfc78a0) · [状态效果 S-67255e6c047bc1b6](../../evidence/state_effects-sets-022.md#s-67255e6c047bc1b6)

### path-032316

```text
(config)# do-exec show ip rsvp <cr>
```

Handler ` RVA 0x10073190 `；selector ` 0 `；EOL ` RVA 0x34A3A428 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5e6a7f2c6539d6b3](../../evidence/conditions-sets-037.md#c-5e6a7f2c6539d6b3) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-049607

```text
(config)# do-exec show ip rsvp aggregation ip <cr>
```

Handler ` RVA 0x101C49F0 `；selector ` 0 `；EOL ` RVA 0x34A69C90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-055670

```text
(config)# do-exec show ip rsvp aggregation ip endpoints <cr>
```

Handler ` RVA 0x101C42E0 `；selector ` 0 `；EOL ` RVA 0x34A69F58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062556

```text
(config)# do-exec show ip rsvp aggregation ip endpoints dscp <?common_dscp_value_action@555589fbded0> <cr>
```

Handler ` RVA 0x101C42E0 `；selector ` 0 `；EOL ` RVA 0x34A69F58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8fe663681bbb9913](../../evidence/conditions-sets-056.md#c-8fe663681bbb9913) · [缺口 G-50a90a07b241e5dc](../../evidence/gaps-sets-003.md#g-50a90a07b241e5dc) · [状态效果 S-a16fe04b0ef6dd2f](../../evidence/state_effects-sets-034.md#s-a16fe04b0ef6dd2f)

### path-055595

```text
(config)# do-exec show ip rsvp aggregation ip interface <cr>
```

Handler ` RVA 0x101C4050 `；selector ` 0 `；EOL ` RVA 0x34A69970 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-77f9e62a2b300c22](../../evidence/conditions-sets-047.md#c-77f9e62a2b300c22) · [状态效果 S-b2bd20405688fd65](../../evidence/state_effects-sets-038.md#s-b2bd20405688fd65)

### path-062402

```text
(config)# do-exec show ip rsvp aggregation ip interface <interface> <cr>
```

Handler ` RVA 0x101C4050 `；selector ` 0 `；EOL ` RVA 0x34A69970 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5f39dab462ae0a68](../../evidence/conditions-sets-037.md#c-5f39dab462ae0a68) · [缺口 G-671688814f471f27](../../evidence/gaps-sets-004.md#g-671688814f471f27) · [参数 P-473b7f2b6b9040ec](../../evidence/parameters-sets-006.md#p-473b7f2b6b9040ec) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-055504

```text
(config)# do-exec show ip rsvp aggregation ip map <cr>
```

Handler ` RVA 0x101C3C20 `；selector ` 0 `；EOL ` RVA 0x34A691B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062543

```text
(config)# do-exec show ip rsvp aggregation ip map dscp <?common_dscp_value_action@555589fbd190> <cr>
```

Handler ` RVA 0x101C3C20 `；selector ` 0 `；EOL ` RVA 0x34A691B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [缺口 G-2fc61974c844cfd1](../../evidence/gaps-sets-002.md#g-2fc61974c844cfd1) · [状态效果 S-779dbe26e2aaf682](../../evidence/state_effects-sets-025.md#s-779dbe26e2aaf682)

### path-055530

```text
(config)# do-exec show ip rsvp aggregation ip reservation <cr>
```

Handler ` RVA 0x101C3DE0 `；selector ` 0 `；EOL ` RVA 0x34A694F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062545

```text
(config)# do-exec show ip rsvp aggregation ip reservation dscp <?common_dscp_value_action@555589fbd4d0> <cr>
```

Handler ` RVA 0x101C3DE0 `；selector ` 0 `；EOL ` RVA 0x34A694F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [缺口 G-1f62318eacfec0cf](../../evidence/gaps-sets-002.md#g-1f62318eacfec0cf) · [状态效果 S-66a726a13ea49699](../../evidence/state_effects-sets-022.md#s-66a726a13ea49699)

### path-040841

```text
(config)# do-exec show ip rsvp atm-peak-rate-limit <cr>
```

Handler ` RVA 0x100542A0 `；selector ` 0 `；EOL ` RVA 0x34A34388 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b6c5c4cc381f4a1f](../../evidence/conditions-sets-071.md#c-b6c5c4cc381f4a1f) · [状态效果 S-59189e46c8dc742e](../../evidence/state_effects-sets-019.md#s-59189e46c8dc742e)

### path-061646

```text
(config)# do-exec show ip rsvp atm-peak-rate-limit <interface> <cr>
```

Handler ` RVA 0x100542A0 `；selector ` 0 `；EOL ` RVA 0x34A34388 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3d9bdecc123063d5](../../evidence/conditions-sets-024.md#c-3d9bdecc123063d5) · [缺口 G-46cd77eaafbe8a37](../../evidence/gaps-sets-003.md#g-46cd77eaafbe8a37) · [参数 P-bd7fb8c43148e967](../../evidence/parameters-sets-014.md#p-bd7fb8c43148e967) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040427

```text
(config)# do-exec show ip rsvp authentication <cr>
```

Handler ` RVA 0x10073FB0 `；selector ` 0 `；EOL ` RVA 0x34A2FFA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7fe18cb68439d029](../../evidence/conditions-sets-050.md#c-7fe18cb68439d029) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-041010

```text
(config)# do-exec show ip rsvp counters <cr>
```

Handler ` RVA 0x100B61F0 `；selector ` 0 `；EOL ` RVA 0x34A35FE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4759a80b867df040](../../evidence/conditions-sets-028.md#c-4759a80b867df040) · [状态效果 S-3add76585c8c9776](../../evidence/state_effects-sets-013.md#s-3add76585c8c9776)

### path-062143

```text
(config)# do-exec show ip rsvp counters interface <interface> <cr>
```

Handler ` RVA 0x100B61F0 `；selector ` 0 `；EOL ` RVA 0x34A35FE8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b7ac897b7163b697](../../evidence/conditions-sets-071.md#c-b7ac897b7163b697) · [缺口 G-b60f66c9a7dab028](../../evidence/gaps-sets-006.md#g-b60f66c9a7dab028) · [参数 P-c09e81c90654a44a](../../evidence/parameters-sets-015.md#p-c09e81c90654a44a) · [状态效果 S-df81e38c20f450a3](../../evidence/state_effects-sets-047.md#s-df81e38c20f450a3)

### path-040751

```text
(config)# do-exec show ip rsvp handles <cr>
```

Handler ` RVA 0x10070450 `；selector ` 0 `；EOL ` RVA 0x34A34000 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f6ac0974c487853d](../../evidence/conditions-sets-095.md#c-f6ac0974c487853d) · [状态效果 S-079efa6fefc7e92e](../../evidence/state_effects-sets-002.md#s-079efa6fefc7e92e)

### path-041083

```text
(config)# do-exec show ip rsvp hello <cr>
```

Handler ` RVA 0x10072260 `；selector ` 0 `；EOL ` RVA 0x34A38728 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-73e1ff93bbad3fdc](../../evidence/conditions-sets-045.md#c-73e1ff93bbad3fdc) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-055931

```text
(config)# do-exec show ip rsvp hello bfd nbr <cr>
```

Handler ` RVA 0x10076740 `；selector ` 0 `；EOL ` RVA 0x34A37650 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ec7faa639c22b742](../../evidence/conditions-sets-091.md#c-ec7faa639c22b742) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-058648

```text
(config)# do-exec show ip rsvp hello bfd nbr detail <cr>
```

Handler ` RVA 0x10076940 `；selector ` 0 `；EOL ` RVA 0x34A37348 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ec7faa639c22b742](../../evidence/conditions-sets-091.md#c-ec7faa639c22b742) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-058661

```text
(config)# do-exec show ip rsvp hello client lsp detail <cr>
```

Handler ` RVA 0x10076EA0 `；selector ` 0 `；EOL ` RVA 0x34A38108 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2cf0f65375dcb14e](../../evidence/conditions-sets-018.md#c-2cf0f65375dcb14e) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-058658

```text
(config)# do-exec show ip rsvp hello client lsp summary <cr>
```

Handler ` RVA 0x10076D20 `；selector ` 0 `；EOL ` RVA 0x34A38410 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2cf0f65375dcb14e](../../evidence/conditions-sets-018.md#c-2cf0f65375dcb14e) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-055941

```text
(config)# do-exec show ip rsvp hello client nbr <cr>
```

Handler ` RVA 0x10076A40 `；selector ` 0 `；EOL ` RVA 0x34A37DA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2cf0f65375dcb14e](../../evidence/conditions-sets-018.md#c-2cf0f65375dcb14e) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-058654

```text
(config)# do-exec show ip rsvp hello client nbr detail <cr>
```

Handler ` RVA 0x10076C10 `；selector ` 0 `；EOL ` RVA 0x34A37A98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2cf0f65375dcb14e](../../evidence/conditions-sets-018.md#c-2cf0f65375dcb14e) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-050164

```text
(config)# do-exec show ip rsvp hello graceful-restart <cr>
```

Handler ` RVA 0x10073050 `；selector ` 0 `；EOL ` RVA 0x34A38700 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9e789b95db429da7](../../evidence/conditions-sets-061.md#c-9e789b95db429da7) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-055870

```text
(config)# do-exec show ip rsvp hello instance internal <cr>
```

Handler ` RVA 0x10076620 `；selector ` 0 `；EOL ` RVA 0x34A368E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2eb6da402bd619e6](../../evidence/conditions-sets-018.md#c-2eb6da402bd619e6) · [状态效果 S-7b64fdf414743285](../../evidence/state_effects-sets-026.md#s-7b64fdf414743285)

### path-055893

```text
(config)# do-exec show ip rsvp hello instance summary <cr>
```

Handler ` RVA 0x10076290 `；selector ` 0 `；EOL ` RVA 0x34A36C40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2eb6da402bd619e6](../../evidence/conditions-sets-018.md#c-2eb6da402bd619e6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-050069

```text
(config)# do-exec show ip rsvp hello statistics <cr>
```

Handler ` RVA 0x100761D0 `；selector ` 0 `；EOL ` RVA 0x34A36F28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7dad2cd3040acf55](../../evidence/conditions-sets-049.md#c-7dad2cd3040acf55) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-050083

```text
(config)# do-exec show ip rsvp host receivers <cr>
```

Handler ` RVA 0x1006D010 `；selector ` 0 `；EOL ` RVA 0x34A35B98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4759a80b867df040](../../evidence/conditions-sets-028.md#c-4759a80b867df040) · [状态效果 S-31845c6dab0ae5fb](../../evidence/state_effects-sets-011.md#s-31845c6dab0ae5fb)

### path-050053

```text
(config)# do-exec show ip rsvp host senders <cr>
```

Handler ` RVA 0x1006D750 `；selector ` 0 `；EOL ` RVA 0x34A358A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4759a80b867df040](../../evidence/conditions-sets-028.md#c-4759a80b867df040) · [状态效果 S-a6490b317e67f573](../../evidence/state_effects-sets-035.md#s-a6490b317e67f573)

### path-062436

```text
(config)# do-exec show ip rsvp host vrf * receivers <cr>
```

Handler ` RVA 0x1006D010 `；selector ` 0 `；EOL ` RVA 0x34A35B98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e34075b254670305](../../evidence/conditions-sets-088.md#c-e34075b254670305) · [缺口 G-ec1f73d500e5b959](../../evidence/gaps-sets-008.md#g-ec1f73d500e5b959) · [状态效果 S-f54d2bf6a3d873b9](../../evidence/state_effects-sets-052.md#s-f54d2bf6a3d873b9)

### path-062432

```text
(config)# do-exec show ip rsvp host vrf * senders <cr>
```

Handler ` RVA 0x1006D750 `；selector ` 0 `；EOL ` RVA 0x34A358A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e34075b254670305](../../evidence/conditions-sets-088.md#c-e34075b254670305) · [缺口 G-ec1f73d500e5b959](../../evidence/gaps-sets-008.md#g-ec1f73d500e5b959) · [状态效果 S-6fe869fb58a60ec0](../../evidence/state_effects-sets-024.md#s-6fe869fb58a60ec0)

### path-040816

```text
(config)# do-exec show ip rsvp installed <cr>
```

Handler ` RVA 0x1006B120 `；selector ` 0 `；EOL ` RVA 0x34A33858 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-be548ffe4fb04560](../../evidence/conditions-sets-073.md#c-be548ffe4fb04560) · [状态效果 S-d53a391e92dab148](../../evidence/state_effects-sets-045.md#s-d53a391e92dab148)

### path-061643

```text
(config)# do-exec show ip rsvp installed <interface> <cr>
```

Handler ` RVA 0x1006B120 `；selector ` 0 `；EOL ` RVA 0x34A33858 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-83d2cd63b62b8a28](../../evidence/conditions-sets-051.md#c-83d2cd63b62b8a28) · [缺口 G-b48897c36abff7d8](../../evidence/gaps-sets-006.md#g-b48897c36abff7d8) · [参数 P-09a4bace1c71e068](../../evidence/parameters-sets-001.md#p-09a4bace1c71e068) · [状态效果 S-1e3a406ab5794d0b](../../evidence/state_effects-sets-007.md#s-1e3a406ab5794d0b)

### path-040760

```text
(config)# do-exec show ip rsvp interface <cr>
```

Handler ` RVA 0x1006B3E0 `；selector ` 0 `；EOL ` RVA 0x34A33020 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7276fe3cb0565025](../../evidence/conditions-sets-044.md#c-7276fe3cb0565025) · [状态效果 S-db7b10c8a859f66c](../../evidence/state_effects-sets-046.md#s-db7b10c8a859f66c)

### path-061644

```text
(config)# do-exec show ip rsvp interface <interface> <cr>
```

Handler ` RVA 0x1006B3E0 `；selector ` 0 `；EOL ` RVA 0x34A33020 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a4bc3647199f1fb4](../../evidence/conditions-sets-063.md#c-a4bc3647199f1fb4) · [缺口 G-25245a7ad1610a00](../../evidence/gaps-sets-002.md#g-25245a7ad1610a00) · [参数 P-454cfd4a7bebbc08](../../evidence/parameters-sets-006.md#p-454cfd4a7bebbc08) · [状态效果 S-d931aedf4e2c054a](../../evidence/state_effects-sets-046.md#s-d931aedf4e2c054a)

### path-050085

```text
(config)# do-exec show ip rsvp listeners <address> <cr>
```

Handler ` RVA 0x1006F480 `；selector ` 6 `；EOL ` RVA 0x34A35008 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Destination address。

[条件 C-4759a80b867df040](../../evidence/conditions-sets-028.md#c-4759a80b867df040) · [参数 P-559a5e35800d3230](../../evidence/parameters-sets-007.md#p-559a5e35800d3230) · [状态效果 S-cd6aa22b179cf597](../../evidence/state_effects-sets-043.md#s-cd6aa22b179cf597)

### path-055838

```text
(config)# do-exec show ip rsvp listeners <address> <number:0..255> <cr>
```

Handler ` RVA 0x1006F480 `；selector ` 4 `；EOL ` RVA 0x34A34CC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Destination address；` unsigned_number ` IP Protocol。

[条件 C-4759a80b867df040](../../evidence/conditions-sets-028.md#c-4759a80b867df040) · [参数 P-c1d702e7762de23b](../../evidence/parameters-sets-015.md#p-c1d702e7762de23b) · [状态效果 S-cd6aa22b179cf597](../../evidence/state_effects-sets-043.md#s-cd6aa22b179cf597)

### path-058585

```text
(config)# do-exec show ip rsvp listeners <address> <number:0..255> <number:0..65535> <cr>
```

Handler ` RVA 0x1006F480 `；selector ` 0 `；EOL ` RVA 0x34A34A18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Destination address；` unsigned_number ` IP Protocol；` unsigned_number ` Destination port。

[条件 C-4759a80b867df040](../../evidence/conditions-sets-028.md#c-4759a80b867df040) · [参数 P-eeed49378aa0252c](../../evidence/parameters-sets-018.md#p-eeed49378aa0252c) · [状态效果 S-cd6aa22b179cf597](../../evidence/state_effects-sets-043.md#s-cd6aa22b179cf597)

### path-040906

```text
(config)# do-exec show ip rsvp listeners <cr>
```

Handler ` RVA 0x1006F480 `；selector ` 7 `；EOL ` RVA 0x34A352C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4759a80b867df040](../../evidence/conditions-sets-028.md#c-4759a80b867df040) · [状态效果 S-cd6aa22b179cf597](../../evidence/state_effects-sets-043.md#s-cd6aa22b179cf597)

### path-062437

```text
(config)# do-exec show ip rsvp listeners vrf * <address> <cr>
```

Handler ` RVA 0x1006F480 `；selector ` 6 `；EOL ` RVA 0x34A35008 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Destination address。

[条件 C-ed9bd15f80d49c57](../../evidence/conditions-sets-092.md#c-ed9bd15f80d49c57) · [缺口 G-a0da7dbe569e042b](../../evidence/gaps-sets-006.md#g-a0da7dbe569e042b) · [参数 P-559a5e35800d3230](../../evidence/parameters-sets-007.md#p-559a5e35800d3230) · [状态效果 S-12c3cd805c12b0d4](../../evidence/state_effects-sets-004.md#s-12c3cd805c12b0d4)

### path-062567

```text
(config)# do-exec show ip rsvp listeners vrf * <address> <number:0..255> <cr>
```

Handler ` RVA 0x1006F480 `；selector ` 4 `；EOL ` RVA 0x34A34CC8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Destination address；` unsigned_number ` IP Protocol。

[条件 C-ed9bd15f80d49c57](../../evidence/conditions-sets-092.md#c-ed9bd15f80d49c57) · [缺口 G-a0da7dbe569e042b](../../evidence/gaps-sets-006.md#g-a0da7dbe569e042b) · [参数 P-c1d702e7762de23b](../../evidence/parameters-sets-015.md#p-c1d702e7762de23b) · [状态效果 S-12c3cd805c12b0d4](../../evidence/state_effects-sets-004.md#s-12c3cd805c12b0d4)

### path-062629

```text
(config)# do-exec show ip rsvp listeners vrf * <address> <number:0..255> <number:0..65535> <cr>
```

Handler ` RVA 0x1006F480 `；selector ` 0 `；EOL ` RVA 0x34A34A18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Destination address；` unsigned_number ` IP Protocol；` unsigned_number ` Destination port。

[条件 C-ed9bd15f80d49c57](../../evidence/conditions-sets-092.md#c-ed9bd15f80d49c57) · [缺口 G-a0da7dbe569e042b](../../evidence/gaps-sets-006.md#g-a0da7dbe569e042b) · [参数 P-eeed49378aa0252c](../../evidence/parameters-sets-018.md#p-eeed49378aa0252c) · [状态效果 S-12c3cd805c12b0d4](../../evidence/state_effects-sets-004.md#s-12c3cd805c12b0d4)

### path-062146

```text
(config)# do-exec show ip rsvp listeners vrf * <cr>
```

Handler ` RVA 0x1006F480 `；selector ` 7 `；EOL ` RVA 0x34A352C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ed9bd15f80d49c57](../../evidence/conditions-sets-092.md#c-ed9bd15f80d49c57) · [缺口 G-a0da7dbe569e042b](../../evidence/gaps-sets-006.md#g-a0da7dbe569e042b) · [状态效果 S-12c3cd805c12b0d4](../../evidence/state_effects-sets-004.md#s-12c3cd805c12b0d4)
