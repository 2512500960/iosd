# redundancy · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-008548

```text
(config-red)# application redundancy <cr>
```

Handler ` RVA 0xCBD6660 `；selector ` 0 `；EOL ` RVA 0x33C130D0 `。

模式根 ` RVA 0x33FD5FF0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-008558

```text
(config-red)# cloud provider aws <number:1..1023> <cr>
```

Handler ` RVA 0x1441A1F0 `；selector ` 0 `；EOL ` RVA 0x35D60D48 `。

模式根 ` RVA 0x33FD5FF0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Cloud instance ID。

[参数 P-8cbf58f2f99cc63a](../../evidence/parameters-sets-011.md#p-8cbf58f2f99cc63a) · [状态效果 S-d2fbc3312d7031ad](../../evidence/state_effects-sets-045.md#s-d2fbc3312d7031ad)

### observed_connections-008559

```text
(config-red)# cloud-ha bfd peer <address> <cr>
```

Handler ` RVA 0x1441B520 `；selector ` 0 `；EOL ` RVA 0x35D62250 `。

模式根 ` RVA 0x33FD5FF0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` The IPv4 address of the BFD neighbor。

[参数 P-f6895e6ad85a4952](../../evidence/parameters-sets-018.md#p-f6895e6ad85a4952) · [状态效果 S-3b701233fc0779b6](../../evidence/state_effects-sets-013.md#s-3b701233fc0779b6)

### observed_connections-008554

```text
(config-red)# default application redundancy <cr>
```

Handler ` RVA 0xCBD6660 `；selector ` 0 `；EOL ` RVA 0x33C130D0 `。

模式根 ` RVA 0x33FD5FF0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-7156f696d9ed929b](../../evidence/state_effects-sets-024.md#s-7156f696d9ed929b)

### observed_connections-008563

```text
(config-red)# default cloud provider aws <number:1..1023> <cr>
```

Handler ` RVA 0x1441A1F0 `；selector ` 0 `；EOL ` RVA 0x35D60D48 `。

模式根 ` RVA 0x33FD5FF0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Cloud instance ID。

[参数 P-8cbf58f2f99cc63a](../../evidence/parameters-sets-011.md#p-8cbf58f2f99cc63a) · [状态效果 S-980fdb16b7055a52](../../evidence/state_effects-sets-032.md#s-980fdb16b7055a52)

### observed_connections-008565

```text
(config-red)# default cloud-ha bfd peer <address> <cr>
```

Handler ` RVA 0x1441B520 `；selector ` 0 `；EOL ` RVA 0x35D62250 `。

模式根 ` RVA 0x33FD5FF0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` The IPv4 address of the BFD neighbor。

[参数 P-f6895e6ad85a4952](../../evidence/parameters-sets-018.md#p-f6895e6ad85a4952) · [状态效果 S-cb822f629613bfd1](../../evidence/state_effects-sets-043.md#s-cb822f629613bfd1)

### observed_connections-008561

```text
(config-red)# default interchassis group <number:1..4294967295> <cr>
```

Handler ` RVA 0xC930470 `；selector ` 0 `；EOL ` RVA 0x33B2F8E0 `。

模式根 ` RVA 0x33FD5FF0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` The redundancy group number。

[参数 P-8a9a44962c719b59](../../evidence/parameters-sets-011.md#p-8a9a44962c719b59) · [状态效果 S-7156f696d9ed929b](../../evidence/state_effects-sets-024.md#s-7156f696d9ed929b)

### observed_connections-008541

```text
(config-red)# default keepalive-enable <cr>
```

Handler ` RVA 0xDB54CF0 `；selector ` 2 `；EOL ` RVA 0x33FD7938 `。

模式根 ` RVA 0x33FD5FF0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a709d6d1042c19f9](../../evidence/conditions-sets-064.md#c-a709d6d1042c19f9) · [状态效果 S-7156f696d9ed929b](../../evidence/state_effects-sets-024.md#s-7156f696d9ed929b)

### observed_connections-008545

```text
(config-red)# default keepalive-threshold <cr>
```

Handler ` RVA 0xDB54CF0 `；selector ` 1 `；EOL ` RVA 0x33FD7670 `。

模式根 ` RVA 0x33FD5FF0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-228101f8c56cdc8f](../../evidence/conditions-sets-014.md#c-228101f8c56cdc8f) · [状态效果 S-7156f696d9ed929b](../../evidence/state_effects-sets-024.md#s-7156f696d9ed929b)

### observed_connections-008542

```text
(config-red)# default keepalive-timer <cr>
```

Handler ` RVA 0xDB54CF0 `；selector ` 0 `；EOL ` RVA 0x33FD72E0 `。

模式根 ` RVA 0x33FD5FF0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6fe0432f18342c02](../../evidence/conditions-sets-043.md#c-6fe0432f18342c02) · [状态效果 S-7156f696d9ed929b](../../evidence/state_effects-sets-024.md#s-7156f696d9ed929b)

### observed_connections-008547

```text
(config-red)# default maintenance-mode <cr>
```

Handler ` RVA 0xDB54CF0 `；selector ` 4 `；EOL ` RVA 0x33FD7F78 `。

模式根 ` RVA 0x33FD5FF0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-33666682f594d00d](../../evidence/conditions-sets-020.md#c-33666682f594d00d) · [状态效果 S-7156f696d9ed929b](../../evidence/state_effects-sets-024.md#s-7156f696d9ed929b)

### observed_connections-008549

```text
(config-red)# default notification-timer <cr>
```

Handler ` RVA 0xDB54CF0 `；selector ` 3 `；EOL ` RVA 0x33FD7CB0 `。

模式根 ` RVA 0x33FD5FF0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-deae91e07ab82628](../../evidence/conditions-sets-086.md#c-deae91e07ab82628) · [状态效果 S-7156f696d9ed929b](../../evidence/state_effects-sets-024.md#s-7156f696d9ed929b)

### observed_connections-008552

```text
(config-red)# default switchover-mode-classic <cr>
```

Handler ` RVA 0xD5287A0 `；selector ` 0 `；EOL ` RVA 0x33E7B0F0 `。

模式根 ` RVA 0x33FD5FF0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-58b72cc963177417](../../evidence/conditions-sets-035.md#c-58b72cc963177417) · [状态效果 S-7156f696d9ed929b](../../evidence/state_effects-sets-024.md#s-7156f696d9ed929b)

### observed_connections-008557

```text
(config-red)# default timer rpso <cr>
```

Handler ` RVA 0xD527C80 `；selector ` 0 `；EOL ` RVA 0x33E7ADE8 `。

模式根 ` RVA 0x33FD5FF0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e6ab94dc4635ba97](../../evidence/conditions-sets-089.md#c-e6ab94dc4635ba97) · [状态效果 S-7156f696d9ed929b](../../evidence/state_effects-sets-024.md#s-7156f696d9ed929b)

### observed_connections-008555

```text
(config-red)# interchassis group <number:1..4294967295> <cr>
```

Handler ` RVA 0xC930470 `；selector ` 0 `；EOL ` RVA 0x33B2F8E0 `。

模式根 ` RVA 0x33FD5FF0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` The redundancy group number。

[参数 P-8a9a44962c719b59](../../evidence/parameters-sets-011.md#p-8a9a44962c719b59)

### observed_connections-008535

```text
(config-red)# keepalive-enable <cr>
```

Handler ` RVA 0xDB54CF0 `；selector ` 2 `；EOL ` RVA 0x33FD7938 `。

模式根 ` RVA 0x33FD5FF0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a709d6d1042c19f9](../../evidence/conditions-sets-064.md#c-a709d6d1042c19f9)

### observed_connections-008567

```text
(config-red)# keepalive-threshold <number:dynamic> <cr>
```

Handler ` RVA 0xDB54CF0 `；selector ` 1 `；EOL ` RVA 0x33FD7670 `。

模式根 ` RVA 0x33FD5FF0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` count。

[条件 C-946a5278d4a42272](../../evidence/conditions-sets-057.md#c-946a5278d4a42272) · [缺口 G-3d02e56df790e201](../../evidence/gaps-sets-003.md#g-3d02e56df790e201) · [参数 P-3527e343ad823ca3](../../evidence/parameters-sets-005.md#p-3527e343ad823ca3)

### observed_connections-008566

```text
(config-red)# keepalive-timer <number:dynamic> <cr>
```

Handler ` RVA 0xDB54CF0 `；selector ` 0 `；EOL ` RVA 0x33FD72E0 `。

模式根 ` RVA 0x33FD5FF0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` milliseconds。

[条件 C-1c9e5d3c4dec0c86](../../evidence/conditions-sets-011.md#c-1c9e5d3c4dec0c86) · [缺口 G-126d2e53a517b476](../../evidence/gaps-sets-001.md#g-126d2e53a517b476) · [参数 P-eb2c57dce6e88d1e](../../evidence/parameters-sets-018.md#p-eb2c57dce6e88d1e)

### observed_connections-008537

```text
(config-red)# main-cpu <cr>
```

Handler ` RVA 0xD514A70 `；selector ` 0 `；EOL ` RVA 0x33E73348 `。

模式根 ` RVA 0x33FD5FF0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a9559c7adcbeebdf](../../evidence/conditions-sets-065.md#c-a9559c7adcbeebdf)

### observed_connections-008536

```text
(config-red)# maintenance-mode <cr>
```

Handler ` RVA 0xDB54CF0 `；selector ` 4 `；EOL ` RVA 0x33FD7F78 `。

模式根 ` RVA 0x33FD5FF0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-33666682f594d00d](../../evidence/conditions-sets-020.md#c-33666682f594d00d)

### observed_connections-008550

```text
(config-red)# mode hsa <cr>
```

Handler ` RVA 0xDA75910 `；selector ` 0 `；EOL ` RVA 0x33FC16C0 `。

模式根 ` RVA 0x33FD5FF0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-864c996408725da3](../../evidence/conditions-sets-052.md#c-864c996408725da3) · [状态效果 S-599e8bba9ca43279](../../evidence/state_effects-sets-019.md#s-599e8bba9ca43279)

### observed_connections-008553

```text
(config-red)# no application redundancy <cr>
```

Handler ` RVA 0xCBD6660 `；selector ` 0 `；EOL ` RVA 0x33C130D0 `。

模式根 ` RVA 0x33FD5FF0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-493920e0305d2097](../../evidence/state_effects-sets-016.md#s-493920e0305d2097)

### observed_connections-008562

```text
(config-red)# no cloud provider aws <number:1..1023> <cr>
```

Handler ` RVA 0x1441A1F0 `；selector ` 0 `；EOL ` RVA 0x35D60D48 `。

模式根 ` RVA 0x33FD5FF0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Cloud instance ID。

[参数 P-8cbf58f2f99cc63a](../../evidence/parameters-sets-011.md#p-8cbf58f2f99cc63a) · [状态效果 S-c6e65fde5cedd1c0](../../evidence/state_effects-sets-042.md#s-c6e65fde5cedd1c0)

### observed_connections-008564

```text
(config-red)# no cloud-ha bfd peer <address> <cr>
```

Handler ` RVA 0x1441B520 `；selector ` 0 `；EOL ` RVA 0x35D62250 `。

模式根 ` RVA 0x33FD5FF0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` The IPv4 address of the BFD neighbor。

[参数 P-f6895e6ad85a4952](../../evidence/parameters-sets-018.md#p-f6895e6ad85a4952) · [状态效果 S-434c58e8f940c5e4](../../evidence/state_effects-sets-015.md#s-434c58e8f940c5e4)

### observed_connections-008560

```text
(config-red)# no interchassis group <number:1..4294967295> <cr>
```

Handler ` RVA 0xC930470 `；selector ` 0 `；EOL ` RVA 0x33B2F8E0 `。

模式根 ` RVA 0x33FD5FF0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` The redundancy group number。

[参数 P-8a9a44962c719b59](../../evidence/parameters-sets-011.md#p-8a9a44962c719b59) · [状态效果 S-493920e0305d2097](../../evidence/state_effects-sets-016.md#s-493920e0305d2097)

### observed_connections-008539

```text
(config-red)# no keepalive-enable <cr>
```

Handler ` RVA 0xDB54CF0 `；selector ` 2 `；EOL ` RVA 0x33FD7938 `。

模式根 ` RVA 0x33FD5FF0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a709d6d1042c19f9](../../evidence/conditions-sets-064.md#c-a709d6d1042c19f9) · [状态效果 S-493920e0305d2097](../../evidence/state_effects-sets-016.md#s-493920e0305d2097)

### observed_connections-008543

```text
(config-red)# no keepalive-threshold <cr>
```

Handler ` RVA 0xDB54CF0 `；selector ` 1 `；EOL ` RVA 0x33FD7670 `。

模式根 ` RVA 0x33FD5FF0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7f09a0c97bcc2438](../../evidence/conditions-sets-049.md#c-7f09a0c97bcc2438) · [状态效果 S-493920e0305d2097](../../evidence/state_effects-sets-016.md#s-493920e0305d2097)

### observed_connections-008540

```text
(config-red)# no keepalive-timer <cr>
```

Handler ` RVA 0xDB54CF0 `；selector ` 0 `；EOL ` RVA 0x33FD72E0 `。

模式根 ` RVA 0x33FD5FF0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-dc794c41511999a0](../../evidence/conditions-sets-085.md#c-dc794c41511999a0) · [状态效果 S-493920e0305d2097](../../evidence/state_effects-sets-016.md#s-493920e0305d2097)

### observed_connections-008544

```text
(config-red)# no maintenance-mode <cr>
```

Handler ` RVA 0xDB54CF0 `；selector ` 4 `；EOL ` RVA 0x33FD7F78 `。

模式根 ` RVA 0x33FD5FF0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-33666682f594d00d](../../evidence/conditions-sets-020.md#c-33666682f594d00d) · [状态效果 S-493920e0305d2097](../../evidence/state_effects-sets-016.md#s-493920e0305d2097)

### observed_connections-008546

```text
(config-red)# no notification-timer <cr>
```

Handler ` RVA 0xDB54CF0 `；selector ` 3 `；EOL ` RVA 0x33FD7CB0 `。

模式根 ` RVA 0x33FD5FF0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-daa697ffcf8bc0f7](../../evidence/conditions-sets-084.md#c-daa697ffcf8bc0f7) · [状态效果 S-493920e0305d2097](../../evidence/state_effects-sets-016.md#s-493920e0305d2097)

### observed_connections-008551

```text
(config-red)# no switchover-mode-classic <cr>
```

Handler ` RVA 0xD5287A0 `；selector ` 0 `；EOL ` RVA 0x33E7B0F0 `。

模式根 ` RVA 0x33FD5FF0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-58b72cc963177417](../../evidence/conditions-sets-035.md#c-58b72cc963177417) · [状态效果 S-493920e0305d2097](../../evidence/state_effects-sets-016.md#s-493920e0305d2097)

### observed_connections-008556

```text
(config-red)# no timer rpso <cr>
```

Handler ` RVA 0xD527C80 `；selector ` 0 `；EOL ` RVA 0x33E7ADE8 `。

模式根 ` RVA 0x33FD5FF0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-70da3334213bf5c0](../../evidence/conditions-sets-044.md#c-70da3334213bf5c0) · [状态效果 S-493920e0305d2097](../../evidence/state_effects-sets-016.md#s-493920e0305d2097)

### observed_connections-008568

```text
(config-red)# notification-timer <number:dynamic> <cr>
```

Handler ` RVA 0xDB54CF0 `；selector ` 3 `；EOL ` RVA 0x33FD7CB0 `。

模式根 ` RVA 0x33FD5FF0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` milliseconds。

[条件 C-95286f11da4c7a2d](../../evidence/conditions-sets-058.md#c-95286f11da4c7a2d) · [缺口 G-fec3ca8aed5d7b4a](../../evidence/gaps-sets-009.md#g-fec3ca8aed5d7b4a) · [参数 P-61f2bbb9f89076f1](../../evidence/parameters-sets-008.md#p-61f2bbb9f89076f1)

### observed_connections-008538

```text
(config-red)# switchover-mode-classic <cr>
```

Handler ` RVA 0xD5287A0 `；selector ` 0 `；EOL ` RVA 0x33E7B0F0 `。

模式根 ` RVA 0x33FD5FF0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-58b72cc963177417](../../evidence/conditions-sets-035.md#c-58b72cc963177417)

### observed_connections-008569

```text
(config-red)# timer rpso <number:dynamic> <cr>
```

Handler ` RVA 0xD527C80 `；selector ` 0 `；EOL ` RVA 0x33E7ADE8 `。

模式根 ` RVA 0x33FD5FF0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Delay value in seconds。

[条件 C-17e0d4b379c2aa2c](../../evidence/conditions-sets-009.md#c-17e0d4b379c2aa2c) · [缺口 G-d3feebce5e67945f](../../evidence/gaps-sets-007.md#g-d3feebce5e67945f) · [参数 P-b6f4c104b9f24eba](../../evidence/parameters-sets-014.md#p-b6f4c104b9f24eba)
