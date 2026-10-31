# null-interface · 六个基础模式的历史连接

[模式索引](README.md) · [总索引](../../README.md)

### path-072858

```text
(config-if)# default ip unreachables <cr>
```

Handler ` RVA 0xCF34540 `；selector ` 11 `；EOL ` RVA 0x33D40358 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5ae7611be1ed91bd](../../evidence/conditions-sets-036.md#c-5ae7611be1ed91bd) · [状态效果 S-98f16013efaab37a](../../evidence/state_effects-sets-032.md#s-98f16013efaab37a)

### path-072861

```text
(config-if)# default ipv6 unreachables <cr>
```

Handler ` RVA 0x123064E0 `；selector ` 0 `；EOL ` RVA 0x357E7A10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6eb819d361b5e988](../../evidence/conditions-sets-043.md#c-6eb819d361b5e988) · [状态效果 S-98f16013efaab37a](../../evidence/state_effects-sets-032.md#s-98f16013efaab37a)

### path-072859

```text
(config-if)# default ntp enable <cr>
```

Handler ` RVA 0xFE1E3B0 `；selector ` 0 `；EOL ` RVA 0x348EF9B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-98f16013efaab37a](../../evidence/state_effects-sets-032.md#s-98f16013efaab37a)

### path-072851

```text
(config-if)# exit <cr>
```

Handler ` RVA 0xDEE92A0 `；selector ` 0 `；EOL ` RVA 0x34143DE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-560048482ba254c9](../../evidence/conditions-sets-034.md#c-560048482ba254c9)

### path-072852

```text
(config-if)# help <cr>
```

Handler ` RVA 0xE006150 `；selector ` 0 `；EOL ` RVA 0x341667E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b0eb474247bd0b39](../../evidence/conditions-sets-068.md#c-b0eb474247bd0b39)

### path-072853

```text
(config-if)# ip unreachables <cr>
```

Handler ` RVA 0xCF34540 `；selector ` 11 `；EOL ` RVA 0x33D40358 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5ae7611be1ed91bd](../../evidence/conditions-sets-036.md#c-5ae7611be1ed91bd)

### path-072855

```text
(config-if)# ipv6 unreachables <cr>
```

Handler ` RVA 0x123064E0 `；selector ` 0 `；EOL ` RVA 0x357E7A10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6eb819d361b5e988](../../evidence/conditions-sets-043.md#c-6eb819d361b5e988)

### path-072856

```text
(config-if)# no ip unreachables <cr>
```

Handler ` RVA 0xCF34540 `；selector ` 11 `；EOL ` RVA 0x33D40358 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5ae7611be1ed91bd](../../evidence/conditions-sets-036.md#c-5ae7611be1ed91bd) · [状态效果 S-0a23a7f95f9977e3](../../evidence/state_effects-sets-003.md#s-0a23a7f95f9977e3)

### path-072860

```text
(config-if)# no ipv6 unreachables <cr>
```

Handler ` RVA 0x123064E0 `；selector ` 0 `；EOL ` RVA 0x357E7A10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-6eb819d361b5e988](../../evidence/conditions-sets-043.md#c-6eb819d361b5e988) · [状态效果 S-0a23a7f95f9977e3](../../evidence/state_effects-sets-003.md#s-0a23a7f95f9977e3)

### path-072857

```text
(config-if)# no ntp enable <cr>
```

Handler ` RVA 0xFE1E3B0 `；selector ` 0 `；EOL ` RVA 0x348EF9B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-0a23a7f95f9977e3](../../evidence/state_effects-sets-003.md#s-0a23a7f95f9977e3)

### path-072854

```text
(config-if)# ntp enable <cr>
```

Handler ` RVA 0xFE1E3B0 `；selector ` 0 `；EOL ` RVA 0x348EF9B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。
