# ipv6-router-address-family · 已捕获槽位上的条件安装

[模式索引](README.md) · [总索引](../../README.md)

### conditional_registration_candidates-011138

```text
(config-ipv6-rtr-af)# default timers manet ackwait <cr>
```

Handler ` RVA 0x1B0895B0 `；selector ` 0 `；EOL ` RVA 0x36EF1430 `。

模式根 ` RVA 0x35582110 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-8424a9118cca664e](../../evidence/conditional_registrations-sets-002.md#r-8424a9118cca664e) · [条件 C-9c33904a13e39951](../../evidence/conditions-sets-060.md#c-9c33904a13e39951) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-65249a208e5b8dce](../../evidence/state_effects-sets-022.md#s-65249a208e5b8dce)

### conditional_registration_candidates-011136

```text
(config-ipv6-rtr-af)# no timers manet ackwait <cr>
```

Handler ` RVA 0x1B0895B0 `；selector ` 0 `；EOL ` RVA 0x36EF1430 `。

模式根 ` RVA 0x35582110 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-8424a9118cca664e](../../evidence/conditional_registrations-sets-002.md#r-8424a9118cca664e) · [条件 C-49a8ac7df0a075c1](../../evidence/conditions-sets-029.md#c-49a8ac7df0a075c1) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-847657a751413f84](../../evidence/state_effects-sets-028.md#s-847657a751413f84)

### conditional_registration_candidates-011137

```text
(config-ipv6-rtr-af)# timers manet ackwait <number:0..10000> <cr>
```

Handler ` RVA 0x1B0895B0 `；selector ` 0 `；EOL ` RVA 0x36EF1430 `。

模式根 ` RVA 0x35582110 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Acknowledgement delay timer value in milliseconds。

[候选注册 R-8424a9118cca664e](../../evidence/conditional_registrations-sets-002.md#r-8424a9118cca664e) · [条件 C-6b54a69bf0f7b6cb](../../evidence/conditions-sets-042.md#c-6b54a69bf0f7b6cb) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-7647b41b27b6ba45](../../evidence/parameters-sets-009.md#p-7647b41b27b6ba45) · [状态效果 S-a9c0e06fe058214b](../../evidence/state_effects-sets-036.md#s-a9c0e06fe058214b)

