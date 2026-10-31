# conn · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-009581

```text
(config-connection)# default description <cr>
```

Handler ` RVA 0xF43A6E0 `；selector ` 3 `；EOL ` RVA 0x34649D38 `。

模式根 ` RVA 0x34647F70 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8cb26a87548c567d](../../evidence/conditions-sets-054.md#c-8cb26a87548c567d) · [状态效果 S-f3040c51b064112b](../../evidence/state_effects-sets-051.md#s-f3040c51b064112b)

### observed_connections-009578

```text
(config-connection)# default shutdown <cr>
```

Handler ` RVA 0xF43A6E0 `；selector ` 1 `；EOL ` RVA 0x34649A00 `。

模式根 ` RVA 0x34647F70 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-f3040c51b064112b](../../evidence/state_effects-sets-051.md#s-f3040c51b064112b)

### observed_connections-009580

```text
(config-connection)# description <string> <cr>
```

Handler ` RVA 0xF43A6E0 `；selector ` 3 `；EOL ` RVA 0x34649D38 `。

模式根 ` RVA 0x34647F70 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Set connect description string。

[条件 C-d2ff1f1ad1815b0f](../../evidence/conditions-sets-081.md#c-d2ff1f1ad1815b0f) · [参数 P-dc9ebee47f88c719](../../evidence/parameters-sets-017.md#p-dc9ebee47f88c719)

### observed_connections-009579

```text
(config-connection)# no description <cr>
```

Handler ` RVA 0xF43A6E0 `；selector ` 3 `；EOL ` RVA 0x34649D38 `。

模式根 ` RVA 0x34647F70 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5d7f34eee9d9b621](../../evidence/conditions-sets-036.md#c-5d7f34eee9d9b621) · [状态效果 S-43d03b5456941146](../../evidence/state_effects-sets-015.md#s-43d03b5456941146)

### observed_connections-009577

```text
(config-connection)# no shutdown <cr>
```

Handler ` RVA 0xF43A6E0 `；selector ` 1 `；EOL ` RVA 0x34649A00 `。

模式根 ` RVA 0x34647F70 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-43d03b5456941146](../../evidence/state_effects-sets-015.md#s-43d03b5456941146)

### observed_connections-009576

```text
(config-connection)# shutdown <cr>
```

Handler ` RVA 0xF43A6E0 `；selector ` 1 `；EOL ` RVA 0x34649A00 `。

模式根 ` RVA 0x34647F70 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-009575

```text
(config-connection)# <cr>
```

Handler ` RVA 0xF43A6E0 `；selector ` 0 `；EOL ` RVA 0x3464A010 `。

模式根 ` RVA 0x34647F70 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f26a0b21da52ff23](../../evidence/conditions-sets-094.md#c-f26a0b21da52ff23)
