# ecfm_ll_efp · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-009524

```text
(config-if-srv-ecfm-ll)# controller discover-interval <number:1..10> <cr>
```

Handler ` RVA 0xBDD0790 `；selector ` 1 `；EOL ` RVA 0x3390AD80 `。

模式根 ` RVA 0x33908B38 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` min (default: 2 min)。

[条件 C-7a8c427416b90f69](../../evidence/conditions-sets-048.md#c-7a8c427416b90f69) · [参数 P-b8c74bce5a8d5378](../../evidence/parameters-sets-014.md#p-b8c74bce5a8d5378)

### observed_connections-009525

```text
(config-if-srv-ecfm-ll)# default controller discover-interval <cr>
```

Handler ` RVA 0xBDD0790 `；selector ` 1 `；EOL ` RVA 0x3390AD80 `。

模式根 ` RVA 0x33908B38 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-eaf238403db318e3](../../evidence/conditions-sets-091.md#c-eaf238403db318e3) · [状态效果 S-acd1bf11f2d73b3e](../../evidence/state_effects-sets-037.md#s-acd1bf11f2d73b3e)

### observed_connections-009522

```text
(config-if-srv-ecfm-ll)# default responder <cr>
```

Handler ` RVA 0xBDD0790 `；selector ` 2 `；EOL ` RVA 0x3390AA30 `。

模式根 ` RVA 0x33908B38 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-acd1bf11f2d73b3e](../../evidence/state_effects-sets-037.md#s-acd1bf11f2d73b3e)

### observed_connections-009519

```text
(config-if-srv-ecfm-ll)# exit <cr>
```

Handler ` RVA 0xBDBE990 `；selector ` 0 `；EOL ` RVA 0x3390C8E8 `。

模式根 ` RVA 0x33908B38 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-78bce290521e5621](../../evidence/conditions-sets-047.md#c-78bce290521e5621)

### observed_connections-009523

```text
(config-if-srv-ecfm-ll)# no controller discover-interval <cr>
```

Handler ` RVA 0xBDD0790 `；selector ` 1 `；EOL ` RVA 0x3390AD80 `。

模式根 ` RVA 0x33908B38 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b2a7acd38c1e0a12](../../evidence/conditions-sets-069.md#c-b2a7acd38c1e0a12) · [状态效果 S-29722ade128d4b21](../../evidence/state_effects-sets-009.md#s-29722ade128d4b21)

### observed_connections-009521

```text
(config-if-srv-ecfm-ll)# no responder <cr>
```

Handler ` RVA 0xBDD0790 `；selector ` 2 `；EOL ` RVA 0x3390AA30 `。

模式根 ` RVA 0x33908B38 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-29722ade128d4b21](../../evidence/state_effects-sets-009.md#s-29722ade128d4b21)

### observed_connections-009520

```text
(config-if-srv-ecfm-ll)# responder <cr>
```

Handler ` RVA 0xBDD0790 `；selector ` 2 `；EOL ` RVA 0x3390AA30 `。

模式根 ` RVA 0x33908B38 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

