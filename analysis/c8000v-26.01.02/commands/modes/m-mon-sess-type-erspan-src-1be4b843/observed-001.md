# mon-sess-type-erspan-src · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-009723

```text
(config-mon-erspan-src)# destination <cr>
```

Handler ` RVA 0xE4F7A60 `；selector ` 0 `；EOL ` RVA 0x342EC8D0 `。

模式根 ` RVA 0x342DE6D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bcbc9babab7a10fb](../../evidence/conditions-sets-073.md#c-bcbc9babab7a10fb) · [状态效果 S-9315ad9b349e4037](../../evidence/state_effects-sets-031.md#s-9315ad9b349e4037)

### observed_connections-009724

```text
(config-mon-erspan-src)# no destination <cr>
```

Handler ` RVA 0xE4F7A60 `；selector ` 0 `；EOL ` RVA 0x342EC8D0 `。

模式根 ` RVA 0x342DE6D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-bcbc9babab7a10fb](../../evidence/conditions-sets-073.md#c-bcbc9babab7a10fb) · [状态效果 S-5e8c3900ed05f647](../../evidence/state_effects-sets-020.md#s-5e8c3900ed05f647)

### observed_connections-009725

```text
(config-mon-erspan-src)# source cpu <cr>
```

Handler ` RVA 0xE4E0120 `；selector ` 1 `；EOL ` RVA 0x342DE828 `。

模式根 ` RVA 0x342DE6D0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f51c8376e162a1a7](../../evidence/conditions-sets-095.md#c-f51c8376e162a1a7) · [缺口 G-22a34e2b298aaaad](../../evidence/gaps-sets-002.md#g-22a34e2b298aaaad) · [状态效果 S-8f31249d145024c4](../../evidence/state_effects-sets-030.md#s-8f31249d145024c4)
