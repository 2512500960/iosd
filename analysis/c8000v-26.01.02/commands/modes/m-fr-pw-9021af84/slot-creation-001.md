# fr-pw · 依赖静态建槽的条件安装

[模式索引](README.md) · [总索引](../../README.md)

### static_slot_creation_candidates-004494

```text
(config-fr-pw-switching)# default mpls l2transport route <cr>
```

Handler ` RVA 0x1934D2B0 `；selector ` 0 `；EOL ` RVA 0x369A4DA0 `。

模式根 ` RVA 0x369A39D8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-8139b87a8248f66a](../../evidence/conditional_registrations-sets-002.md#r-8139b87a8248f66a) · [条件 C-7b251a0bf2876e7f](../../evidence/conditions-sets-048.md#c-7b251a0bf2876e7f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-570518e9a785ff13](../../evidence/state_effects-sets-019.md#s-570518e9a785ff13)

### static_slot_creation_candidates-004491

```text
(config-fr-pw-switching)# default mtu <cr>
```

Handler ` RVA 0x1934D070 `；selector ` 0 `；EOL ` RVA 0x369A50E8 `。

模式根 ` RVA 0x369A39D8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-8139b87a8248f66a](../../evidence/conditional_registrations-sets-002.md#r-8139b87a8248f66a) · [条件 C-7a02c87397d85215](../../evidence/conditions-sets-047.md#c-7a02c87397d85215) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-570518e9a785ff13](../../evidence/state_effects-sets-019.md#s-570518e9a785ff13)

### static_slot_creation_candidates-004489

```text
(config-fr-pw-switching)# default xconnect <cr>
```

Handler ` RVA 0x1A9E4100 `；selector ` 0 `；EOL ` RVA 0x369A3C90 `。

模式根 ` RVA 0x369A39D8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-394fe22338668d25](../../evidence/conditional_registrations-sets-001.md#r-394fe22338668d25) · [条件 C-e0a600cf063cbc6e](../../evidence/conditions-sets-086.md#c-e0a600cf063cbc6e) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-570518e9a785ff13](../../evidence/state_effects-sets-019.md#s-570518e9a785ff13)

### static_slot_creation_candidates-004495

```text
(config-fr-pw-switching)# mpls l2transport route <address> <number:1..4294967295> <cr>
```

Handler ` RVA 0x1934D2B0 `；selector ` 0 `；EOL ` RVA 0x369A4DA0 `。

模式根 ` RVA 0x369A39D8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP address of Peer；` unsigned_number ` Enter VC ID value。

[候选注册 R-8139b87a8248f66a](../../evidence/conditional_registrations-sets-002.md#r-8139b87a8248f66a) · [条件 C-e5000be5cdd9d057](../../evidence/conditions-sets-088.md#c-e5000be5cdd9d057) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-a5dd11e3313534e9](../../evidence/parameters-sets-013.md#p-a5dd11e3313534e9)

### static_slot_creation_candidates-004497

```text
(config-fr-pw-switching)# mtu <number:dynamic> <cr>
```

Handler ` RVA 0x1934D070 `；selector ` 0 `；EOL ` RVA 0x369A50E8 `。

模式根 ` RVA 0x369A39D8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` MTU size in bytes。

[候选注册 R-8139b87a8248f66a](../../evidence/conditional_registrations-sets-002.md#r-8139b87a8248f66a) · [条件 C-e2bb9600c8c197ce](../../evidence/conditions-sets-087.md#c-e2bb9600c8c197ce) · [缺口 G-b2ebe1cb6d1277a5](../../evidence/gaps-sets-006.md#g-b2ebe1cb6d1277a5) · [参数 P-bb9fdbb2326da180](../../evidence/parameters-sets-014.md#p-bb9fdbb2326da180)

### static_slot_creation_candidates-004493

```text
(config-fr-pw-switching)# no mpls l2transport route <cr>
```

Handler ` RVA 0x1934D2B0 `；selector ` 0 `；EOL ` RVA 0x369A4DA0 `。

模式根 ` RVA 0x369A39D8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-8139b87a8248f66a](../../evidence/conditional_registrations-sets-002.md#r-8139b87a8248f66a) · [条件 C-25b182f983dcbb86](../../evidence/conditions-sets-015.md#c-25b182f983dcbb86) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9173e41b51dff3e3](../../evidence/state_effects-sets-031.md#s-9173e41b51dff3e3)

### static_slot_creation_candidates-004490

```text
(config-fr-pw-switching)# no mtu <cr>
```

Handler ` RVA 0x1934D070 `；selector ` 0 `；EOL ` RVA 0x369A50E8 `。

模式根 ` RVA 0x369A39D8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-8139b87a8248f66a](../../evidence/conditional_registrations-sets-002.md#r-8139b87a8248f66a) · [条件 C-2b0e6490a6929413](../../evidence/conditions-sets-017.md#c-2b0e6490a6929413) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9173e41b51dff3e3](../../evidence/state_effects-sets-031.md#s-9173e41b51dff3e3)

### static_slot_creation_candidates-004488

```text
(config-fr-pw-switching)# no xconnect <cr>
```

Handler ` RVA 0x1A9E4100 `；selector ` 0 `；EOL ` RVA 0x369A3C90 `。

模式根 ` RVA 0x369A39D8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-394fe22338668d25](../../evidence/conditional_registrations-sets-001.md#r-394fe22338668d25) · [条件 C-c7b418544d875392](../../evidence/conditions-sets-077.md#c-c7b418544d875392) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9173e41b51dff3e3](../../evidence/state_effects-sets-031.md#s-9173e41b51dff3e3)

### static_slot_creation_candidates-004498

```text
(config-fr-pw-switching)# pseudowire <address> <number:1..4294967295> encapsulation mpls <cr>
```

Handler ` RVA 0x1A9E4100 `；selector ` 0 `；EOL ` RVA 0x369A3C90 `。

模式根 ` RVA 0x369A39D8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` IP address of peer；` unsigned_number ` Enter VC ID value。

[候选注册 R-394fe22338668d25](../../evidence/conditional_registrations-sets-001.md#r-394fe22338668d25) · [条件 C-9552aacd8dc2fa8e](../../evidence/conditions-sets-058.md#c-9552aacd8dc2fa8e) · [缺口 G-93c906c745843e4b](../../evidence/gaps-sets-005.md#g-93c906c745843e4b) · [参数 P-e8c50285001db26c](../../evidence/parameters-sets-017.md#p-e8c50285001db26c) · [状态效果 S-ec26dad73527e9e4](../../evidence/state_effects-sets-050.md#s-ec26dad73527e9e4)

### static_slot_creation_candidates-004496

```text
(config-fr-pw-switching)# pseudowire <address> <number:1..4294967295> pw-class <string> <cr>
```

Handler ` RVA 0x1A9E4100 `；selector ` 0 `；EOL ` RVA 0x369A3C90 `。

模式根 ` RVA 0x369A39D8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP address of peer；` unsigned_number ` Enter VC ID value；` string ` Pseudowire-class name。

[候选注册 R-394fe22338668d25](../../evidence/conditional_registrations-sets-001.md#r-394fe22338668d25) · [条件 C-6d13d4e337625e98](../../evidence/conditions-sets-042.md#c-6d13d4e337625e98) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-fb015a00ba63aa5b](../../evidence/parameters-sets-019.md#p-fb015a00ba63aa5b) · [状态效果 S-d22ba44594094fe6](../../evidence/state_effects-sets-045.md#s-d22ba44594094fe6)

### static_slot_creation_candidates-004492

```text
(config-fr-pw-switching)# xconnect vfi <string> <cr>
```

Handler ` RVA 0x1A9E4100 `；selector ` 1 `；EOL ` RVA 0x369A3D98 `。

模式根 ` RVA 0x369A39D8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` VFI name。

[候选注册 R-394fe22338668d25](../../evidence/conditional_registrations-sets-001.md#r-394fe22338668d25) · [条件 C-24c8992f96229e79](../../evidence/conditions-sets-014.md#c-24c8992f96229e79) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-0d9f20d5c6cb1467](../../evidence/parameters-sets-001.md#p-0d9f20d5c6cb1467)
