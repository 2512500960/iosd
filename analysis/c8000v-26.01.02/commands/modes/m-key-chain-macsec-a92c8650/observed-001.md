# key-chain-macsec · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-009590

```text
(config-keychain-macsec)# description <string> <cr>
```

Handler ` RVA 0xFDB4360 `；selector ` 2 `；EOL ` RVA 0x348D08D8 `。

模式根 ` RVA 0x348CCE90 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` A Short description。

[条件 C-ab807cebc4f0fcca](../../evidence/conditions-sets-066.md#c-ab807cebc4f0fcca) · [参数 P-d560762b1c1bcfa3](../../evidence/parameters-sets-016.md#p-d560762b1c1bcfa3)

### observed_connections-009589

```text
(config-keychain-macsec)# exit <cr>
```

Handler ` RVA 0xDEE92A0 `；selector ` 0 `；EOL ` RVA 0x348D0ED0 `。

模式根 ` RVA 0x348CCE90 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-821fd41be131fb6a](../../evidence/conditions-sets-050.md#c-821fd41be131fb6a)

### observed_connections-009592

```text
(config-keychain-macsec)# key <hex-string> <cr>
```

Handler ` RVA 0xFDB4360 `；selector ` 1 `；EOL ` RVA 0x348D0BF8 `。

模式根 ` RVA 0x348CCE90 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` hexstring ` Key identifier as a hex string with even number of digits。

[条件 C-43acecb0ff820661](../../evidence/conditions-sets-026.md#c-43acecb0ff820661) · [缺口 G-f7cced9618c27dc5](../../evidence/gaps-sets-009.md#g-f7cced9618c27dc5) · [参数 P-0c782d685b8f28bd](../../evidence/parameters-sets-001.md#p-0c782d685b8f28bd)

### observed_connections-009591

```text
(config-keychain-macsec)# no description <cr>
```

Handler ` RVA 0xFDB4360 `；selector ` 2 `；EOL ` RVA 0x348D08D8 `。

模式根 ` RVA 0x348CCE90 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-41c9afb6cc120d26](../../evidence/conditions-sets-026.md#c-41c9afb6cc120d26) · [状态效果 S-92b17f3bc015a304](../../evidence/state_effects-sets-031.md#s-92b17f3bc015a304)

