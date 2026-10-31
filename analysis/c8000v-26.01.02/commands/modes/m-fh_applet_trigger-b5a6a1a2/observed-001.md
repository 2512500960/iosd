# fh_applet_trigger · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-009544

```text
(config-applet-trigger)# attribute tag <string> <cr>
```

Handler ` RVA 0xC0CC160 `；selector ` 9 `；EOL ` RVA 0x339BB550 `。

模式根 ` RVA 0x339A0508 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` tag name。

[条件 C-cce57235e7a25643](../../evidence/conditions-sets-079.md#c-cce57235e7a25643) · [参数 P-942c0c6844b0f077](../../evidence/parameters-sets-011.md#p-942c0c6844b0f077)

### observed_connections-009545

```text
(config-applet-trigger)# correlate event <string> <cr>
```

Handler ` RVA 0xC0CC160 `；selector ` 10 `；EOL ` RVA 0x339BB918 `。

模式根 ` RVA 0x339A0508 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` event tag value。

[条件 C-a680aa5c1fa1da22](../../evidence/conditions-sets-064.md#c-a680aa5c1fa1da22) · [参数 P-593d2a80b5b6136f](../../evidence/parameters-sets-007.md#p-593d2a80b5b6136f)

### observed_connections-009542

```text
(config-applet-trigger)# exit <cr>
```

Handler ` RVA 0xC0CC2F0 `；selector ` 8 `；EOL ` RVA 0x339A09A0 `。

模式根 ` RVA 0x339A0508 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2bf05ff3a9f217ad](../../evidence/conditions-sets-017.md#c-2bf05ff3a9f217ad)

### observed_connections-009546

```text
(config-applet-trigger)# no attribute tag <string> <cr>
```

Handler ` RVA 0xC0CC160 `；selector ` 9 `；EOL ` RVA 0x339BB550 `。

模式根 ` RVA 0x339A0508 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` tag name。

[条件 C-012a0b60dccfe24a](../../evidence/conditions-sets-001.md#c-012a0b60dccfe24a) · [参数 P-942c0c6844b0f077](../../evidence/parameters-sets-011.md#p-942c0c6844b0f077) · [状态效果 S-cfbec6a32a92db01](../../evidence/state_effects-sets-044.md#s-cfbec6a32a92db01)

### observed_connections-009543

```text
(config-applet-trigger)# no correlate <cr>
```

Handler ` RVA 0xC0CC160 `；selector ` 10 `；EOL ` RVA 0x339BB918 `。

模式根 ` RVA 0x339A0508 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f2739b957824c8c1](../../evidence/conditions-sets-094.md#c-f2739b957824c8c1) · [状态效果 S-cfbec6a32a92db01](../../evidence/state_effects-sets-044.md#s-cfbec6a32a92db01)
