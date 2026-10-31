# conf-rad-server · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-008341

```text
(config-radius-server)# address ipv4 <address> alias <cr>
```

Handler ` RVA 0x100440B0 `；selector ` 81 `；EOL ` RVA 0x34967A38 `。

模式根 ` RVA 0x34944F00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IPv4 Address of radius server。

[参数 P-3231279fa0559dfa](../../evidence/parameters-sets-004.md#p-3231279fa0559dfa) · [状态效果 S-1e5cb77f8bbab8ca](../../evidence/state_effects-sets-007.md#s-1e5cb77f8bbab8ca)

### observed_connections-008342

```text
(config-radius-server)# attribute policy-name <string> include-in-access-req <cr>
```

Handler ` RVA 0x100440B0 `；selector ` 140 `；EOL ` RVA 0x349686D8 `。

模式根 ` RVA 0x34944F00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Policy name (max of 64 characters)。

[参数 P-1fe75b86093cf651](../../evidence/parameters-sets-003.md#p-1fe75b86093cf651) · [状态效果 S-21e533bcaa382240](../../evidence/state_effects-sets-008.md#s-21e533bcaa382240)

### observed_connections-008339

```text
(config-radius-server)# automate-tester username <string> <cr>
```

Handler ` RVA 0x100440B0 `；selector ` 90 `；EOL ` RVA 0x3496A3A0 `。

模式根 ` RVA 0x34944F00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` User Name。

[参数 P-9f036fc0d6743e47](../../evidence/parameters-sets-012.md#p-9f036fc0d6743e47) · [状态效果 S-99d861aca2dc9a4d](../../evidence/state_effects-sets-033.md#s-99d861aca2dc9a4d)

### observed_connections-008334

```text
(config-radius-server)# backoff exponential <cr>
```

Handler ` RVA 0x100440B0 `；selector ` 89 `；EOL ` RVA 0x34969D48 `。

模式根 ` RVA 0x34944F00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d34a6362af741f18](../../evidence/conditions-sets-081.md#c-d34a6362af741f18) · [状态效果 S-37a20d4586935419](../../evidence/state_effects-sets-012.md#s-37a20d4586935419)

### observed_connections-008340

```text
(config-radius-server)# dscp acct <number:1..63> <cr>
```

Handler ` RVA 0x100440B0 `；selector ` 133 `；EOL ` RVA 0x3496C6A0 `。

模式根 ` RVA 0x34944F00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Dscp Acct Value。

[条件 C-31a8675ca87873e1](../../evidence/conditions-sets-019.md#c-31a8675ca87873e1) · [参数 P-92102d62c02a08ec](../../evidence/parameters-sets-011.md#p-92102d62c02a08ec) · [状态效果 S-37a20d4586935419](../../evidence/state_effects-sets-012.md#s-37a20d4586935419)

### observed_connections-008324

```text
(config-radius-server)# dtls <cr>
```

Handler ` RVA 0x100440B0 `；selector ` 111 `；EOL ` RVA 0x3496B830 `。

模式根 ` RVA 0x34944F00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-31a8675ca87873e1](../../evidence/conditions-sets-019.md#c-31a8675ca87873e1) · [状态效果 S-fe5cc3ae538a0e30](../../evidence/state_effects-sets-054.md#s-fe5cc3ae538a0e30)

### observed_connections-008348

```text
(config-radius-server)# dtls ip radius source-interface <interface> <cr>
```

Handler ` RVA 0x100440B0 `；selector ` 111 `；EOL ` RVA 0x3496B830 `。

模式根 ` RVA 0x34944F00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2f7ea6f7aa60a343](../../evidence/conditions-sets-019.md#c-2f7ea6f7aa60a343) · [缺口 G-769a6c6516fabf7e](../../evidence/gaps-sets-005.md#g-769a6c6516fabf7e) · [参数 P-e772ee3118768718](../../evidence/parameters-sets-017.md#p-e772ee3118768718) · [状态效果 S-6391a0bd011df96f](../../evidence/state_effects-sets-021.md#s-6391a0bd011df96f)

### observed_connections-008319

```text
(config-radius-server)# exit <cr>
```

Handler ` RVA 0x10042B80 `；selector ` 0 `；EOL ` RVA 0x34965AC8 `。

模式根 ` RVA 0x34944F00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f9b3d4b06890794d](../../evidence/conditions-sets-096.md#c-f9b3d4b06890794d)

### observed_connections-008321

```text
(config-radius-server)# ignore-acct-authenticator <cr>
```

Handler ` RVA 0x100440B0 `；selector ` 88 `；EOL ` RVA 0x34969408 `。

模式根 ` RVA 0x34944F00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[状态效果 S-37a20d4586935419](../../evidence/state_effects-sets-012.md#s-37a20d4586935419)

### observed_connections-008336

```text
(config-radius-server)# key <string> <cr>
```

Handler ` RVA 0x100440B0 `；selector ` 84 `；EOL ` RVA 0x3496B1D0 `。

模式根 ` RVA 0x34944F00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` The UNCRYPTED (cleartext) shared key。

[条件 C-77cd975612197578](../../evidence/conditions-sets-047.md#c-77cd975612197578) · [参数 P-da5090deeffc0150](../../evidence/parameters-sets-016.md#p-da5090deeffc0150) · [状态效果 S-0d2bbfc6436fd4ed](../../evidence/state_effects-sets-003.md#s-0d2bbfc6436fd4ed)

### observed_connections-008347

```text
(config-radius-server)# key-wrap encryption-key <string> message-auth-code-key <string> <cr>
```

Handler ` RVA 0x100440B0 `；selector ` 110 `；EOL ` RVA 0x3496A7B8 `。

模式根 ` RVA 0x34944F00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` The UNENCRYPTED (cleartext) server key；` string ` The UNENCRYPTED (cleartext) server key。

[条件 C-39d4663cb5ab6ec5](../../evidence/conditions-sets-022.md#c-39d4663cb5ab6ec5) · [参数 P-d4a234672206ea6d](../../evidence/parameters-sets-016.md#p-d4a234672206ea6d) · [状态效果 S-d966ff230de0a678](../../evidence/state_effects-sets-046.md#s-d966ff230de0a678)

### observed_connections-008345

```text
(config-radius-server)# no address ipv4 <address> alias <cr>
```

Handler ` RVA 0x100440B0 `；selector ` 81 `；EOL ` RVA 0x34967A38 `。

模式根 ` RVA 0x34944F00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` IPv4 Address of radius server。

[参数 P-3231279fa0559dfa](../../evidence/parameters-sets-004.md#p-3231279fa0559dfa) · [状态效果 S-3338055586d5c129](../../evidence/state_effects-sets-011.md#s-3338055586d5c129)

### observed_connections-008346

```text
(config-radius-server)# no attribute policy-name <string> include-in-access-req <cr>
```

Handler ` RVA 0x100440B0 `；selector ` 140 `；EOL ` RVA 0x349686D8 `。

模式根 ` RVA 0x34944F00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Policy name (max of 64 characters)。

[参数 P-1fe75b86093cf651](../../evidence/parameters-sets-003.md#p-1fe75b86093cf651) · [状态效果 S-e908d3f4de26a50b](../../evidence/state_effects-sets-049.md#s-e908d3f4de26a50b)

### observed_connections-008343

```text
(config-radius-server)# no automate-tester username <string> <cr>
```

Handler ` RVA 0x100440B0 `；selector ` 90 `；EOL ` RVA 0x3496A3A0 `。

模式根 ` RVA 0x34944F00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` User Name。

[参数 P-9f036fc0d6743e47](../../evidence/parameters-sets-012.md#p-9f036fc0d6743e47) · [状态效果 S-915a74639c0afe9c](../../evidence/state_effects-sets-031.md#s-915a74639c0afe9c)

### observed_connections-008338

```text
(config-radius-server)# no backoff exponential <cr>
```

Handler ` RVA 0x100440B0 `；selector ` 89 `；EOL ` RVA 0x34969D48 `。

模式根 ` RVA 0x34944F00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-3d018b439a3af347](../../evidence/conditions-sets-024.md#c-3d018b439a3af347) · [状态效果 S-e428d3ee22bc8bb6](../../evidence/state_effects-sets-048.md#s-e428d3ee22bc8bb6)

### observed_connections-008344

```text
(config-radius-server)# no dscp acct <number:1..63> <cr>
```

Handler ` RVA 0x100440B0 `；selector ` 133 `；EOL ` RVA 0x3496C6A0 `。

模式根 ` RVA 0x34944F00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Dscp Acct Value。

[条件 C-31a8675ca87873e1](../../evidence/conditions-sets-019.md#c-31a8675ca87873e1) · [参数 P-92102d62c02a08ec](../../evidence/parameters-sets-011.md#p-92102d62c02a08ec) · [状态效果 S-e428d3ee22bc8bb6](../../evidence/state_effects-sets-048.md#s-e428d3ee22bc8bb6)

### observed_connections-008337

```text
(config-radius-server)# no dtls <cr>
```

Handler ` RVA 0x100440B0 `；selector ` 111 `；EOL ` RVA 0x3496B830 `。

模式根 ` RVA 0x34944F00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-31a8675ca87873e1](../../evidence/conditions-sets-019.md#c-31a8675ca87873e1) · [状态效果 S-b52d91e471b879cb](../../evidence/state_effects-sets-038.md#s-b52d91e471b879cb)

### observed_connections-008330

```text
(config-radius-server)# no ignore-acct-authenticator <cr>
```

Handler ` RVA 0x100440B0 `；selector ` 88 `；EOL ` RVA 0x34969408 `。

模式根 ` RVA 0x34944F00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-e428d3ee22bc8bb6](../../evidence/state_effects-sets-048.md#s-e428d3ee22bc8bb6)

### observed_connections-008335

```text
(config-radius-server)# no key <cr>
```

Handler ` RVA 0x100440B0 `；selector ` 84 `；EOL ` RVA 0x3496B1D0 `。

模式根 ` RVA 0x34944F00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ec715bc0be5d5d8a](../../evidence/conditions-sets-091.md#c-ec715bc0be5d5d8a) · [状态效果 S-eaad93cdf1f9c143](../../evidence/state_effects-sets-050.md#s-eaad93cdf1f9c143)

### observed_connections-008333

```text
(config-radius-server)# no key-wrap <cr>
```

Handler ` RVA 0x100440B0 `；selector ` 110 `；EOL ` RVA 0x3496A7B8 `。

模式根 ` RVA 0x34944F00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-79b272b9abd89465](../../evidence/conditions-sets-047.md#c-79b272b9abd89465) · [状态效果 S-e428d3ee22bc8bb6](../../evidence/state_effects-sets-048.md#s-e428d3ee22bc8bb6)

### observed_connections-008328

```text
(config-radius-server)# no non-standard <cr>
```

Handler ` RVA 0x100440B0 `；selector ` 87 `；EOL ` RVA 0x34969128 `。

模式根 ` RVA 0x34944F00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-e428d3ee22bc8bb6](../../evidence/state_effects-sets-048.md#s-e428d3ee22bc8bb6)

### observed_connections-008329

```text
(config-radius-server)# no retransmit <cr>
```

Handler ` RVA 0x100440B0 `；selector ` 86 `；EOL ` RVA 0x34968E30 `。

模式根 ` RVA 0x34944F00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1eb7f68f53db1659](../../evidence/conditions-sets-012.md#c-1eb7f68f53db1659) · [状态效果 S-e428d3ee22bc8bb6](../../evidence/state_effects-sets-048.md#s-e428d3ee22bc8bb6)

### observed_connections-008331

```text
(config-radius-server)# no send-ma <cr>
```

Handler ` RVA 0x100440B0 `；selector ` 141 `；EOL ` RVA 0x349696E8 `。

模式根 ` RVA 0x34944F00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-e428d3ee22bc8bb6](../../evidence/state_effects-sets-048.md#s-e428d3ee22bc8bb6)

### observed_connections-008326

```text
(config-radius-server)# no timeout <cr>
```

Handler ` RVA 0x100440B0 `；selector ` 85 `；EOL ` RVA 0x34968AA8 `。

模式根 ` RVA 0x34944F00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-42f6246640319199](../../evidence/conditions-sets-026.md#c-42f6246640319199) · [状态效果 S-e8dcae07ff8bdd67](../../evidence/state_effects-sets-049.md#s-e8dcae07ff8bdd67)

### observed_connections-008332

```text
(config-radius-server)# no validate-ma <cr>
```

Handler ` RVA 0x100440B0 `；selector ` 142 `；EOL ` RVA 0x349699C8 `。

模式根 ` RVA 0x34944F00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-e428d3ee22bc8bb6](../../evidence/state_effects-sets-048.md#s-e428d3ee22bc8bb6)

### observed_connections-008320

```text
(config-radius-server)# non-standard <cr>
```

Handler ` RVA 0x100440B0 `；selector ` 87 `；EOL ` RVA 0x34969128 `。

模式根 ` RVA 0x34944F00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[状态效果 S-37a20d4586935419](../../evidence/state_effects-sets-012.md#s-37a20d4586935419)

### observed_connections-008327

```text
(config-radius-server)# retransmit <number:0..100> <cr>
```

Handler ` RVA 0x100440B0 `；selector ` 86 `；EOL ` RVA 0x34968E30 `。

模式根 ` RVA 0x34944F00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of retries to this server。

[条件 C-add860204bb745c6](../../evidence/conditions-sets-067.md#c-add860204bb745c6) · [参数 P-c08efcfac06bce37](../../evidence/parameters-sets-015.md#p-c08efcfac06bce37) · [状态效果 S-37a20d4586935419](../../evidence/state_effects-sets-012.md#s-37a20d4586935419)

### observed_connections-008322

```text
(config-radius-server)# send-ma <cr>
```

Handler ` RVA 0x100440B0 `；selector ` 141 `；EOL ` RVA 0x349696E8 `。

模式根 ` RVA 0x34944F00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[状态效果 S-37a20d4586935419](../../evidence/state_effects-sets-012.md#s-37a20d4586935419)

### observed_connections-008325

```text
(config-radius-server)# timeout <number:1..1000> <cr>
```

Handler ` RVA 0x100440B0 `；selector ` 85 `；EOL ` RVA 0x34968AA8 `。

模式根 ` RVA 0x34944F00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timeout value in seconds。

[条件 C-6b9b469e60a7417d](../../evidence/conditions-sets-042.md#c-6b9b469e60a7417d) · [参数 P-3f8543c113a65a85](../../evidence/parameters-sets-005.md#p-3f8543c113a65a85)

### observed_connections-008323

```text
(config-radius-server)# validate-ma <cr>
```

Handler ` RVA 0x100440B0 `；selector ` 142 `；EOL ` RVA 0x349699C8 `。

模式根 ` RVA 0x34944F00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[状态效果 S-37a20d4586935419](../../evidence/state_effects-sets-012.md#s-37a20d4586935419)
