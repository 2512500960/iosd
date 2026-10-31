# pw-tlv-template · 依赖静态建槽的条件安装

[模式索引](README.md) · [总索引](../../README.md)

### static_slot_creation_candidates-004615

```text
(config-pw-tlv-template)# default tlv <number:1..64> <number:1..255> <number:1..4294967295> <cr>
```

Handler ` RVA 0x1AA1F600 `；selector ` 1 `；EOL ` RVA 0x36D492D8 `。

模式根 ` RVA 0x36D490F0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` TLV type in hex format；` unsigned_number ` TLV length；` unsigned_number ` TLV value in decimal format。

[候选注册 R-d9b50ed2abf3f302](../../evidence/conditional_registrations-sets-002.md#r-d9b50ed2abf3f302) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-b65e83c0f565317e](../../evidence/parameters-sets-014.md#p-b65e83c0f565317e) · [状态效果 S-64738f67350e3e6e](../../evidence/state_effects-sets-021.md#s-64738f67350e3e6e)

### static_slot_creation_candidates-004614

```text
(config-pw-tlv-template)# no tlv <number:1..64> <number:1..255> <number:1..4294967295> <cr>
```

Handler ` RVA 0x1AA1F600 `；selector ` 1 `；EOL ` RVA 0x36D492D8 `。

模式根 ` RVA 0x36D490F0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` TLV type in hex format；` unsigned_number ` TLV length；` unsigned_number ` TLV value in decimal format。

[候选注册 R-d9b50ed2abf3f302](../../evidence/conditional_registrations-sets-002.md#r-d9b50ed2abf3f302) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-b65e83c0f565317e](../../evidence/parameters-sets-014.md#p-b65e83c0f565317e) · [状态效果 S-ad8846a56894f175](../../evidence/state_effects-sets-037.md#s-ad8846a56894f175)

### static_slot_creation_candidates-004613

```text
(config-pw-tlv-template)# tlv <number:1..64> <number:1..255> <number:1..4294967295> <cr>
```

Handler ` RVA 0x1AA1F600 `；selector ` 1 `；EOL ` RVA 0x36D492D8 `。

模式根 ` RVA 0x36D490F0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` TLV type in hex format；` unsigned_number ` TLV length；` unsigned_number ` TLV value in decimal format。

[候选注册 R-d9b50ed2abf3f302](../../evidence/conditional_registrations-sets-002.md#r-d9b50ed2abf3f302) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-b65e83c0f565317e](../../evidence/parameters-sets-014.md#p-b65e83c0f565317e)

### static_slot_creation_candidates-004616

```text
(config-pw-tlv-template)# tlv <number:1..64> <number:1..255> hexstr <hex-string> <cr>
```

Handler ` RVA 0x1AA1F600 `；selector ` 1 `；EOL ` RVA 0x36D492D8 `。

模式根 ` RVA 0x36D490F0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` TLV type in hex format；` unsigned_number ` TLV length；` hexstring ` TLV value in hex string format。

[候选注册 R-d9b50ed2abf3f302](../../evidence/conditional_registrations-sets-002.md#r-d9b50ed2abf3f302) · [条件 C-c6b3275ca3f4406e](../../evidence/conditions-sets-077.md#c-c6b3275ca3f4406e) · [缺口 G-e990f4293950e9c2](../../evidence/gaps-sets-008.md#g-e990f4293950e9c2) · [参数 P-2fee98b3ae912a33](../../evidence/parameters-sets-004.md#p-2fee98b3ae912a33) · [状态效果 S-f7ca0388b5ebfc7b](../../evidence/state_effects-sets-052.md#s-f7ca0388b5ebfc7b)
