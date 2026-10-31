# control-plane · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-009569

```text
(config-cp)# exit <cr>
```

Handler ` RVA 0xE47F390 `；selector ` 0 `；EOL ` RVA 0x342C4BC8 `。

模式根 ` RVA 0x342C4740 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-dd477fd6b4a1163a](../../evidence/conditions-sets-085.md#c-dd477fd6b4a1163a)

### observed_connections-009571

```text
(config-cp)# ip flow ingress <cr>
```

Handler ` RVA 0xE47E260 `；selector ` 0 `；EOL ` RVA 0x342C4F70 `。

模式根 ` RVA 0x342C4740 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7c91214fa3600198](../../evidence/conditions-sets-048.md#c-7c91214fa3600198)

### observed_connections-009570

```text
(config-cp)# no exit <cr>
```

Handler ` RVA 0xE47F390 `；selector ` 0 `；EOL ` RVA 0x342C4BC8 `。

模式根 ` RVA 0x342C4740 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-dd477fd6b4a1163a](../../evidence/conditions-sets-085.md#c-dd477fd6b4a1163a) · [状态效果 S-5943882a766229c7](../../evidence/state_effects-sets-019.md#s-5943882a766229c7)

### observed_connections-009573

```text
(config-cp)# no ip flow ingress <cr>
```

Handler ` RVA 0xE47E260 `；selector ` 0 `；EOL ` RVA 0x342C4F70 `。

模式根 ` RVA 0x342C4740 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7c91214fa3600198](../../evidence/conditions-sets-048.md#c-7c91214fa3600198) · [状态效果 S-5943882a766229c7](../../evidence/state_effects-sets-019.md#s-5943882a766229c7)

### observed_connections-009574

```text
(config-cp)# no service-policy input <string> <cr>
```

Handler ` RVA 0xDA58A60 `；selector ` 0 `；EOL ` RVA 0x33FBAE00 `。

模式根 ` RVA 0x342C4740 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Policy map name。

[条件 C-653fc368e456738a](../../evidence/conditions-sets-039.md#c-653fc368e456738a) · [参数 P-ea04bb707b898941](../../evidence/parameters-sets-017.md#p-ea04bb707b898941) · [状态效果 S-1289abe97c59c005](../../evidence/state_effects-sets-004.md#s-1289abe97c59c005)

### observed_connections-009572

```text
(config-cp)# service-policy input <string> <cr>
```

Handler ` RVA 0xDA58A60 `；selector ` 0 `；EOL ` RVA 0x33FBAE00 `。

模式根 ` RVA 0x342C4740 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Policy map name。

[条件 C-653fc368e456738a](../../evidence/conditions-sets-039.md#c-653fc368e456738a) · [参数 P-ea04bb707b898941](../../evidence/parameters-sets-017.md#p-ea04bb707b898941) · [状态效果 S-38a9980c4ca0101a](../../evidence/state_effects-sets-013.md#s-38a9980c4ca0101a)

