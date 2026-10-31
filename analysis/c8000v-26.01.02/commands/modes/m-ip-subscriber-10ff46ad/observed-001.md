# ip-subscriber · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-009428

```text
(config-subscriber)# arp ignore local <cr>
```

Handler ` RVA 0x11A170D0 `；selector ` 0 `；EOL ` RVA 0x355CD348 `。

模式根 ` RVA 0x355CAC08 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4b12faa9b568660b](../../evidence/conditions-sets-029.md#c-4b12faa9b568660b)

### observed_connections-009426

```text
(config-subscriber)# exit <cr>
```

Handler ` RVA 0x11A3A850 `；selector ` 0 `；EOL ` RVA 0x355D08E8 `。

模式根 ` RVA 0x355CAC08 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e9955444facaca4d](../../evidence/conditions-sets-090.md#c-e9955444facaca4d)

### observed_connections-009427

```text
(config-subscriber)# initiator radius-proxy <cr>
```

Handler ` RVA 0x11A17AB0 `；selector ` 0 `；EOL ` RVA 0x355CC8C0 `。

模式根 ` RVA 0x355CAC08 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c8c83657438a39a0](../../evidence/conditions-sets-077.md#c-c8c83657438a39a0) · [状态效果 S-d865a4515c8ebb4f](../../evidence/state_effects-sets-046.md#s-d865a4515c8ebb4f)

### observed_connections-009431

```text
(config-subscriber)# no arp ignore local <cr>
```

Handler ` RVA 0x11A170D0 `；selector ` 0 `；EOL ` RVA 0x355CD348 `。

模式根 ` RVA 0x355CAC08 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4b12faa9b568660b](../../evidence/conditions-sets-029.md#c-4b12faa9b568660b) · [状态效果 S-4761e4c3f3fea9ec](../../evidence/state_effects-sets-016.md#s-4761e4c3f3fea9ec)

### observed_connections-009429

```text
(config-subscriber)# no initiator radius-proxy <cr>
```

Handler ` RVA 0x11A17AB0 `；selector ` 0 `；EOL ` RVA 0x355CC8C0 `。

模式根 ` RVA 0x355CAC08 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c8c83657438a39a0](../../evidence/conditions-sets-077.md#c-c8c83657438a39a0) · [状态效果 S-5435f34420049552](../../evidence/state_effects-sets-018.md#s-5435f34420049552)

### observed_connections-009432

```text
(config-subscriber)# no passthru downstream ipv6 <cr>
```

Handler ` RVA 0x11A19BE0 `；selector ` 0 `；EOL ` RVA 0x355CD748 `。

模式根 ` RVA 0x355CAC08 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-fbfac2d268d9e1d5](../../evidence/conditions-sets-097.md#c-fbfac2d268d9e1d5) · [状态效果 S-32bc1eb8294b76cb](../../evidence/state_effects-sets-011.md#s-32bc1eb8294b76cb)

### observed_connections-009430

```text
(config-subscriber)# passthru downstream ipv6 <cr>
```

Handler ` RVA 0x11A19BE0 `；selector ` 0 `；EOL ` RVA 0x355CD748 `。

模式根 ` RVA 0x355CAC08 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fbfac2d268d9e1d5](../../evidence/conditions-sets-097.md#c-fbfac2d268d9e1d5) · [状态效果 S-254de533ea82ab0a](../../evidence/state_effects-sets-008.md#s-254de533ea82ab0a)

