# conf-dia-attr-list · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-009714

```text
(config-dia-attr-list)# attribute <number:1..65535> binary <hex-data> <cr>
```

Handler ` RVA 0xBD016B0 `；selector ` 0 `；EOL ` RVA 0x338B0448 `。

模式根 ` RVA 0x338A5AD0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` enter Attribute id；` hexdata ` value in hex format。

[条件 C-77f9c9fc90daa600](../../evidence/conditions-sets-047.md#c-77f9c9fc90daa600) · [缺口 G-48873eb14d7fa62c](../../evidence/gaps-sets-003.md#g-48873eb14d7fa62c) · [参数 P-b2dd7dd629a27385](../../evidence/parameters-sets-014.md#p-b2dd7dd629a27385) · [状态效果 S-8c64ead292c2a2d1](../../evidence/state_effects-sets-030.md#s-8c64ead292c2a2d1)

### observed_connections-009713

```text
(config-dia-attr-list)# attribute <number:1..65535> ipfilterrule <string> <cr>
```

Handler ` RVA 0xBD016B0 `；selector ` 0 `；EOL ` RVA 0x338B0448 `。

模式根 ` RVA 0x338A5AD0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` enter Attribute id；` string ` value in string format。

[条件 C-7fc4794f4f1c321a](../../evidence/conditions-sets-050.md#c-7fc4794f4f1c321a) · [参数 P-da48c54b0a821a66](../../evidence/parameters-sets-016.md#p-da48c54b0a821a66) · [状态效果 S-e7693394f1532418](../../evidence/state_effects-sets-049.md#s-e7693394f1532418)

### observed_connections-009711

```text
(config-dia-attr-list)# exit <cr>
```

Handler ` RVA 0xBD016B0 `；selector ` 1 `；EOL ` RVA 0x338A5FE0 `。

模式根 ` RVA 0x338A5AD0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ca0d32a5b88b3d9c](../../evidence/conditions-sets-078.md#c-ca0d32a5b88b3d9c)

### observed_connections-009712

```text
(config-dia-attr-list)# no attribute <number:1..65535> <cr>
```

Handler ` RVA 0xBD016B0 `；selector ` 0 `；EOL ` RVA 0x338B0448 `。

模式根 ` RVA 0x338A5AD0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` enter Attribute id。

[条件 C-6c6492f321723de5](../../evidence/conditions-sets-042.md#c-6c6492f321723de5) · [参数 P-838498d645f851b5](../../evidence/parameters-sets-010.md#p-838498d645f851b5) · [状态效果 S-de0b8efd46d4a347](../../evidence/state_effects-sets-047.md#s-de0b8efd46d4a347)

