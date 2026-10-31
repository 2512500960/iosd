# eap-mprofile-mode · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-008643

```text
(config-eap-method-profile)# accept-on-auth-prov <cr>
```

Handler ` RVA 0xCB42020 `；selector ` 9 `；EOL ` RVA 0x33BCC040 `。

模式根 ` RVA 0x33BC64B0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-581adcff1e427df7](../../evidence/conditions-sets-035.md#c-581adcff1e427df7)

### observed_connections-008644

```text
(config-eap-method-profile)# allow-anon-prov <cr>
```

Handler ` RVA 0xCB42020 `；selector ` 8 `；EOL ` RVA 0x33BCC320 `。

模式根 ` RVA 0x33BC64B0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-581adcff1e427df7](../../evidence/conditions-sets-035.md#c-581adcff1e427df7)

### observed_connections-008645

```text
(config-eap-method-profile)# allow-auth-prov <cr>
```

Handler ` RVA 0xCB42020 `；selector ` 11 `；EOL ` RVA 0x33BCC600 `。

模式根 ` RVA 0x33BC64B0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-581adcff1e427df7](../../evidence/conditions-sets-035.md#c-581adcff1e427df7)

### observed_connections-008663

```text
(config-eap-method-profile)# authority-id identity <string> <cr>
```

Handler ` RVA 0xCB42020 `；selector ` 2 `；EOL ` RVA 0x33BCC9A8 `。

模式根 ` RVA 0x33BC64B0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` (any text)。

[条件 C-e64308be8115e253](../../evidence/conditions-sets-089.md#c-e64308be8115e253) · [参数 P-4fb794548300e980](../../evidence/parameters-sets-007.md#p-4fb794548300e980)

### observed_connections-008665

```text
(config-eap-method-profile)# authority-id information <string> <cr>
```

Handler ` RVA 0xCB42020 `；selector ` 3 `；EOL ` RVA 0x33BCCCC8 `。

模式根 ` RVA 0x33BC64B0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` (any text)。

[条件 C-6298a034e366f80a](../../evidence/conditions-sets-038.md#c-6298a034e366f80a) · [参数 P-9f4113ee85a1ef24](../../evidence/parameters-sets-012.md#p-9f4113ee85a1ef24)

### observed_connections-008646

```text
(config-eap-method-profile)# client-cert-required <cr>
```

Handler ` RVA 0xCB42020 `；selector ` 7 `；EOL ` RVA 0x33BCCFC8 `。

模式根 ` RVA 0x33BC64B0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-581adcff1e427df7](../../evidence/conditions-sets-035.md#c-581adcff1e427df7)

### observed_connections-008649

```text
(config-eap-method-profile)# description <string> <cr>
```

Handler ` RVA 0xCB42020 `；selector ` 1 `；EOL ` RVA 0x33BCBD58 `。

模式根 ` RVA 0x33BC64B0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` (any textual description)。

[条件 C-fb1b147a00c0cf87](../../evidence/conditions-sets-097.md#c-fb1b147a00c0cf87) · [参数 P-a1a38667604b76ab](../../evidence/parameters-sets-012.md#p-a1a38667604b76ab)

### observed_connections-008648

```text
(config-eap-method-profile)# exit <cr>
```

Handler ` RVA 0xCB42020 `；selector ` 12 `；EOL ` RVA 0x33BCE350 `。

模式根 ` RVA 0x33BC64B0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-581adcff1e427df7](../../evidence/conditions-sets-035.md#c-581adcff1e427df7)

### observed_connections-008647

```text
(config-eap-method-profile)# local-cert-required <cr>
```

Handler ` RVA 0xCB42020 `；selector ` 6 `；EOL ` RVA 0x33BCD2A8 `。

模式根 ` RVA 0x33BC64B0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-581adcff1e427df7](../../evidence/conditions-sets-035.md#c-581adcff1e427df7)

### observed_connections-008661

```text
(config-eap-method-profile)# local-key <string> <cr>
```

Handler ` RVA 0xCB42020 `；selector ` 4 `；EOL ` RVA 0x33BCD5E8 `。

模式根 ` RVA 0x33BC64B0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` The UNENCRYPTED (cleartext) local key。

[条件 C-da3e06704d4ff31b](../../evidence/conditions-sets-084.md#c-da3e06704d4ff31b) · [参数 P-c283978fbc3eba63](../../evidence/parameters-sets-015.md#p-c283978fbc3eba63) · [状态效果 S-b2f5642b5f4329f0](../../evidence/state_effects-sets-038.md#s-b2f5642b5f4329f0)

### observed_connections-008650

```text
(config-eap-method-profile)# no accept-on-auth-prov <cr>
```

Handler ` RVA 0xCB42020 `；selector ` 9 `；EOL ` RVA 0x33BCC040 `。

模式根 ` RVA 0x33BC64B0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-581adcff1e427df7](../../evidence/conditions-sets-035.md#c-581adcff1e427df7) · [状态效果 S-654e334a7b86949d](../../evidence/state_effects-sets-022.md#s-654e334a7b86949d)

### observed_connections-008652

```text
(config-eap-method-profile)# no allow-anon-prov <cr>
```

Handler ` RVA 0xCB42020 `；selector ` 8 `；EOL ` RVA 0x33BCC320 `。

模式根 ` RVA 0x33BC64B0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-581adcff1e427df7](../../evidence/conditions-sets-035.md#c-581adcff1e427df7) · [状态效果 S-654e334a7b86949d](../../evidence/state_effects-sets-022.md#s-654e334a7b86949d)

### observed_connections-008653

```text
(config-eap-method-profile)# no allow-auth-prov <cr>
```

Handler ` RVA 0xCB42020 `；selector ` 11 `；EOL ` RVA 0x33BCC600 `。

模式根 ` RVA 0x33BC64B0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-581adcff1e427df7](../../evidence/conditions-sets-035.md#c-581adcff1e427df7) · [状态效果 S-654e334a7b86949d](../../evidence/state_effects-sets-022.md#s-654e334a7b86949d)

### observed_connections-008664

```text
(config-eap-method-profile)# no authority-id identity <cr>
```

Handler ` RVA 0xCB42020 `；selector ` 2 `；EOL ` RVA 0x33BCC9A8 `。

模式根 ` RVA 0x33BC64B0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-18ed7fdff0047dec](../../evidence/conditions-sets-010.md#c-18ed7fdff0047dec) · [状态效果 S-654e334a7b86949d](../../evidence/state_effects-sets-022.md#s-654e334a7b86949d)

### observed_connections-008666

```text
(config-eap-method-profile)# no authority-id information <cr>
```

Handler ` RVA 0xCB42020 `；selector ` 3 `；EOL ` RVA 0x33BCCCC8 `。

模式根 ` RVA 0x33BC64B0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f23afc35e1aa2ee6](../../evidence/conditions-sets-094.md#c-f23afc35e1aa2ee6) · [状态效果 S-654e334a7b86949d](../../evidence/state_effects-sets-022.md#s-654e334a7b86949d)

### observed_connections-008654

```text
(config-eap-method-profile)# no client-cert-required <cr>
```

Handler ` RVA 0xCB42020 `；selector ` 7 `；EOL ` RVA 0x33BCCFC8 `。

模式根 ` RVA 0x33BC64B0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-581adcff1e427df7](../../evidence/conditions-sets-035.md#c-581adcff1e427df7) · [状态效果 S-654e334a7b86949d](../../evidence/state_effects-sets-022.md#s-654e334a7b86949d)

### observed_connections-008651

```text
(config-eap-method-profile)# no description <cr>
```

Handler ` RVA 0xCB42020 `；selector ` 1 `；EOL ` RVA 0x33BCBD58 `。

模式根 ` RVA 0x33BC64B0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-2acfe2d2d38e2c85](../../evidence/conditions-sets-017.md#c-2acfe2d2d38e2c85) · [状态效果 S-654e334a7b86949d](../../evidence/state_effects-sets-022.md#s-654e334a7b86949d)

### observed_connections-008657

```text
(config-eap-method-profile)# no exit <cr>
```

Handler ` RVA 0xCB42020 `；selector ` 12 `；EOL ` RVA 0x33BCE350 `。

模式根 ` RVA 0x33BC64B0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-581adcff1e427df7](../../evidence/conditions-sets-035.md#c-581adcff1e427df7) · [状态效果 S-654e334a7b86949d](../../evidence/state_effects-sets-022.md#s-654e334a7b86949d)

### observed_connections-008655

```text
(config-eap-method-profile)# no local-cert-required <cr>
```

Handler ` RVA 0xCB42020 `；selector ` 6 `；EOL ` RVA 0x33BCD2A8 `。

模式根 ` RVA 0x33BC64B0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-581adcff1e427df7](../../evidence/conditions-sets-035.md#c-581adcff1e427df7) · [状态效果 S-654e334a7b86949d](../../evidence/state_effects-sets-022.md#s-654e334a7b86949d)

### observed_connections-008656

```text
(config-eap-method-profile)# no local-key <cr>
```

Handler ` RVA 0xCB42020 `；selector ` 4 `；EOL ` RVA 0x33BCD5E8 `。

模式根 ` RVA 0x33BC64B0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c08186461d76b5e2](../../evidence/conditions-sets-074.md#c-c08186461d76b5e2) · [状态效果 S-654e334a7b86949d](../../evidence/state_effects-sets-022.md#s-654e334a7b86949d)

### observed_connections-008658

```text
(config-eap-method-profile)# no pac-password <cr>
```

Handler ` RVA 0xCB42020 `；selector ` 10 `；EOL ` RVA 0x33BCDB58 `。

模式根 ` RVA 0x33BC64B0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0165fac89c90d176](../../evidence/conditions-sets-001.md#c-0165fac89c90d176) · [状态效果 S-654e334a7b86949d](../../evidence/state_effects-sets-022.md#s-654e334a7b86949d)

### observed_connections-008660

```text
(config-eap-method-profile)# no pac-ttl <cr>
```

Handler ` RVA 0xCB42020 `；selector ` 5 `；EOL ` RVA 0x33BCE0C8 `。

模式根 ` RVA 0x33BC64B0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-3ac3d11f7ce21848](../../evidence/conditions-sets-023.md#c-3ac3d11f7ce21848) · [状态效果 S-654e334a7b86949d](../../evidence/state_effects-sets-022.md#s-654e334a7b86949d)

### observed_connections-008662

```text
(config-eap-method-profile)# pac-password <string> <cr>
```

Handler ` RVA 0xCB42020 `；selector ` 10 `；EOL ` RVA 0x33BCDB58 `。

模式根 ` RVA 0x33BC64B0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` The UNENCRYPTED (cleartext) password。

[条件 C-8a8bad1feae2342e](../../evidence/conditions-sets-054.md#c-8a8bad1feae2342e) · [参数 P-2f5bf07db304c968](../../evidence/parameters-sets-004.md#p-2f5bf07db304c968) · [状态效果 S-a6b66a9c0f7cdd51](../../evidence/state_effects-sets-035.md#s-a6b66a9c0f7cdd51)

### observed_connections-008659

```text
(config-eap-method-profile)# pac-ttl <number:1..700000000> <cr>
```

Handler ` RVA 0xCB42020 `；selector ` 5 `；EOL ` RVA 0x33BCE0C8 `。

模式根 ` RVA 0x33BC64B0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Enter a value (in seconds) between 1 and 700000000。

[条件 C-86969286a21eb67f](../../evidence/conditions-sets-052.md#c-86969286a21eb67f) · [参数 P-125ce528bb9ee966](../../evidence/parameters-sets-002.md#p-125ce528bb9ee966)
