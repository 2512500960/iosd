# config-x25-huntgroup · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-009738

```text
(config-x25-huntgroup)# exit <cr>
```

Handler ` RVA 0x10617500 `；selector ` 0 `；EOL ` RVA 0x34BCC6A0 `。

模式根 ` RVA 0x34BC4440 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-009742

```text
(config-x25-huntgroup)# interface <interface> <cr>
```

Handler ` RVA 0x10616A70 `；selector ` 0 `；EOL ` RVA 0x34BCCB10 `。

模式根 ` RVA 0x34BC4440 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-354f0bde08b0ef2d](../../evidence/conditions-sets-021.md#c-354f0bde08b0ef2d) · [缺口 G-b47c3fbce853e1da](../../evidence/gaps-sets-006.md#g-b47c3fbce853e1da) · [参数 P-69d13698933bf016](../../evidence/parameters-sets-008.md#p-69d13698933bf016) · [状态效果 S-a46467ad6b27b2a4](../../evidence/state_effects-sets-035.md#s-a46467ad6b27b2a4)

### observed_connections-009739

```text
(config-x25-huntgroup)# no exit <cr>
```

Handler ` RVA 0x10617500 `；selector ` 0 `；EOL ` RVA 0x34BCC6A0 `。

模式根 ` RVA 0x34BC4440 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-4f51c2f685052def](../../evidence/state_effects-sets-017.md#s-4f51c2f685052def)

### observed_connections-009741

```text
(config-x25-huntgroup)# no xot <address> <cr>
```

Handler ` RVA 0x10616A70 `；selector ` 0 `；EOL ` RVA 0x34BCCB10 `。

模式根 ` RVA 0x34BC4440 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` Address of remote XOT host。

[条件 C-63d73479f94307d5](../../evidence/conditions-sets-039.md#c-63d73479f94307d5) · [参数 P-c5b6786074d20b54](../../evidence/parameters-sets-015.md#p-c5b6786074d20b54) · [状态效果 S-6daa8d0a039175ba](../../evidence/state_effects-sets-023.md#s-6daa8d0a039175ba)

### observed_connections-009740

```text
(config-x25-huntgroup)# xot <address> <cr>
```

Handler ` RVA 0x10616A70 `；selector ` 0 `；EOL ` RVA 0x34BCCB10 `。

模式根 ` RVA 0x34BC4440 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Address of remote XOT host。

[条件 C-63d73479f94307d5](../../evidence/conditions-sets-039.md#c-63d73479f94307d5) · [参数 P-c5b6786074d20b54](../../evidence/parameters-sets-015.md#p-c5b6786074d20b54) · [状态效果 S-1326fb97d24eea5b](../../evidence/state_effects-sets-004.md#s-1326fb97d24eea5b)

