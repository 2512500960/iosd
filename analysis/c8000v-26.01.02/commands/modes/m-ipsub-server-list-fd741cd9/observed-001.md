# ipsub-server-list · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-009607

```text
(config-server-list)# exit <cr>
```

Handler ` RVA 0x11A159E0 `；selector ` 0 `；EOL ` RVA 0x355CBD70 `。

模式根 ` RVA 0x355CAB78 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8f3e9b0d5a37c848](../../evidence/conditions-sets-055.md#c-8f3e9b0d5a37c848)

### observed_connections-009608

```text
(config-server-list)# ip source <address> <cr>
```

Handler ` RVA 0x11A156C0 `；selector ` 0 `；EOL ` RVA 0x355CB5D0 `。

模式根 ` RVA 0x355CAB78 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Static session server ip address。

[参数 P-0d41edaead34f9ee](../../evidence/parameters-sets-001.md#p-0d41edaead34f9ee) · [状态效果 S-a30aa7a0b55ab520](../../evidence/state_effects-sets-035.md#s-a30aa7a0b55ab520)

### observed_connections-009609

```text
(config-server-list)# ipv6 prefix default <number:1..128> <cr>
```

Handler ` RVA 0x11A173A0 `；selector ` 0 `；EOL ` RVA 0x355CBA18 `。

模式根 ` RVA 0x355CAB78 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Prefix length。

[条件 C-d5a121b15d4b322a](../../evidence/conditions-sets-082.md#c-d5a121b15d4b322a) · [参数 P-8a1c8bc83916af46](../../evidence/parameters-sets-011.md#p-8a1c8bc83916af46)

### observed_connections-009610

```text
(config-server-list)# no ip source <address> <cr>
```

Handler ` RVA 0x11A156C0 `；selector ` 0 `；EOL ` RVA 0x355CB5D0 `。

模式根 ` RVA 0x355CAB78 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` Static session server ip address。

[参数 P-0d41edaead34f9ee](../../evidence/parameters-sets-001.md#p-0d41edaead34f9ee) · [状态效果 S-dd22da5e08ac2eee](../../evidence/state_effects-sets-047.md#s-dd22da5e08ac2eee)

### observed_connections-009611

```text
(config-server-list)# no ipv6 prefix default <number:1..128> <cr>
```

Handler ` RVA 0x11A173A0 `；selector ` 0 `；EOL ` RVA 0x355CBA18 `。

模式根 ` RVA 0x355CAB78 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Prefix length。

[条件 C-d5a121b15d4b322a](../../evidence/conditions-sets-082.md#c-d5a121b15d4b322a) · [参数 P-8a1c8bc83916af46](../../evidence/parameters-sets-011.md#p-8a1c8bc83916af46) · [状态效果 S-bf979c49e45f64bd](../../evidence/state_effects-sets-041.md#s-bf979c49e45f64bd)

