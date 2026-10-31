# l2-vfi-neighbor-interface · 依赖静态建槽的条件安装

[模式索引](README.md) · [总索引](../../README.md)

### static_slot_creation_candidates-004584

```text
(config-vfi-neighbor-interface)# default tlv <number:1..64> <number:1..255> <number:1..4294967295> <cr>
```

Handler ` RVA 0x1AA1F600 `；selector ` 1 `；EOL ` RVA 0x36D5B560 `。

模式根 ` RVA 0x36D5B3A0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` TLV type in hex format；` unsigned_number ` TLV length；` unsigned_number ` TLV value in decimal format。

[候选注册 R-8f4d418b3de3ee7d](../../evidence/conditional_registrations-sets-002.md#r-8f4d418b3de3ee7d) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-6d49a47d5223187c](../../evidence/parameters-sets-009.md#p-6d49a47d5223187c) · [状态效果 S-dda59449576894e0](../../evidence/state_effects-sets-047.md#s-dda59449576894e0)

### static_slot_creation_candidates-004581

```text
(config-vfi-neighbor-interface)# default tlv template <string> <cr>
```

Handler ` RVA 0x1AA4B260 `；selector ` 1 `；EOL ` RVA 0x36D5B9E8 `。

模式根 ` RVA 0x36D5B3A0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` TLV template name string。

[候选注册 R-b4ed8203a456f6e0](../../evidence/conditional_registrations-sets-002.md#r-b4ed8203a456f6e0) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-cc4cb7b220780111](../../evidence/parameters-sets-015.md#p-cc4cb7b220780111) · [状态效果 S-dda59449576894e0](../../evidence/state_effects-sets-047.md#s-dda59449576894e0)

### static_slot_creation_candidates-004583

```text
(config-vfi-neighbor-interface)# no tlv <number:1..64> <number:1..255> <number:1..4294967295> <cr>
```

Handler ` RVA 0x1AA1F600 `；selector ` 1 `；EOL ` RVA 0x36D5B560 `。

模式根 ` RVA 0x36D5B3A0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` TLV type in hex format；` unsigned_number ` TLV length；` unsigned_number ` TLV value in decimal format。

[候选注册 R-8f4d418b3de3ee7d](../../evidence/conditional_registrations-sets-002.md#r-8f4d418b3de3ee7d) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-6d49a47d5223187c](../../evidence/parameters-sets-009.md#p-6d49a47d5223187c) · [状态效果 S-a339fd88250b92be](../../evidence/state_effects-sets-035.md#s-a339fd88250b92be)

### static_slot_creation_candidates-004580

```text
(config-vfi-neighbor-interface)# no tlv template <string> <cr>
```

Handler ` RVA 0x1AA4B260 `；selector ` 1 `；EOL ` RVA 0x36D5B9E8 `。

模式根 ` RVA 0x36D5B3A0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` TLV template name string。

[候选注册 R-b4ed8203a456f6e0](../../evidence/conditional_registrations-sets-002.md#r-b4ed8203a456f6e0) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-cc4cb7b220780111](../../evidence/parameters-sets-015.md#p-cc4cb7b220780111) · [状态效果 S-a339fd88250b92be](../../evidence/state_effects-sets-035.md#s-a339fd88250b92be)

### static_slot_creation_candidates-004582

```text
(config-vfi-neighbor-interface)# tlv <number:1..64> <number:1..255> <number:1..4294967295> <cr>
```

Handler ` RVA 0x1AA1F600 `；selector ` 1 `；EOL ` RVA 0x36D5B560 `。

模式根 ` RVA 0x36D5B3A0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` TLV type in hex format；` unsigned_number ` TLV length；` unsigned_number ` TLV value in decimal format。

[候选注册 R-8f4d418b3de3ee7d](../../evidence/conditional_registrations-sets-002.md#r-8f4d418b3de3ee7d) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-6d49a47d5223187c](../../evidence/parameters-sets-009.md#p-6d49a47d5223187c)

### static_slot_creation_candidates-004585

```text
(config-vfi-neighbor-interface)# tlv <number:1..64> <number:1..255> hexstr <hex-string> <cr>
```

Handler ` RVA 0x1AA1F600 `；selector ` 1 `；EOL ` RVA 0x36D5B560 `。

模式根 ` RVA 0x36D5B3A0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` TLV type in hex format；` unsigned_number ` TLV length；` hexstring ` TLV value in hex string format。

[候选注册 R-8f4d418b3de3ee7d](../../evidence/conditional_registrations-sets-002.md#r-8f4d418b3de3ee7d) · [条件 C-d6525f3ab2783dff](../../evidence/conditions-sets-083.md#c-d6525f3ab2783dff) · [缺口 G-2488b15c62f9dfad](../../evidence/gaps-sets-002.md#g-2488b15c62f9dfad) · [参数 P-777d2fcc9cd5ce24](../../evidence/parameters-sets-009.md#p-777d2fcc9cd5ce24) · [状态效果 S-41029848c0d2934f](../../evidence/state_effects-sets-014.md#s-41029848c0d2934f)

### static_slot_creation_candidates-004579

```text
(config-vfi-neighbor-interface)# tlv template <string> <cr>
```

Handler ` RVA 0x1AA4B260 `；selector ` 1 `；EOL ` RVA 0x36D5B9E8 `。

模式根 ` RVA 0x36D5B3A0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` TLV template name string。

[候选注册 R-b4ed8203a456f6e0](../../evidence/conditional_registrations-sets-002.md#r-b4ed8203a456f6e0) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-cc4cb7b220780111](../../evidence/parameters-sets-015.md#p-cc4cb7b220780111)

