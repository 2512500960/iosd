# conf-dia-peer · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-008747

```text
(config-dia-peer)# address ipv4 <address> <cr>
```

Handler ` RVA 0xBD06CF0 `；selector ` 13 `；EOL ` RVA 0x338AE258 `。

模式根 ` RVA 0x338A5B48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP address of diameter peer。

[参数 P-62861a6f6f116278](../../evidence/parameters-sets-008.md#p-62861a6f6f116278)

### observed_connections-008750

```text
(config-dia-peer)# destination host <string> <cr>
```

Handler ` RVA 0xBD06CF0 `；selector ` 8 `；EOL ` RVA 0x338AF5C0 `。

模式根 ` RVA 0x338A5B48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Host name。

[条件 C-3eb59fa089b5c3c2](../../evidence/conditions-sets-024.md#c-3eb59fa089b5c3c2) · [参数 P-2d0c6339d27231fb](../../evidence/parameters-sets-004.md#p-2d0c6339d27231fb)

### observed_connections-008752

```text
(config-dia-peer)# destination realm <string> <cr>
```

Handler ` RVA 0xBD06CF0 `；selector ` 7 `；EOL ` RVA 0x338AF8A8 `。

模式根 ` RVA 0x338A5B48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Realm string。

[条件 C-32c4e995cddcbeeb](../../evidence/conditions-sets-020.md#c-32c4e995cddcbeeb) · [参数 P-34a924f2514f2293](../../evidence/parameters-sets-004.md#p-34a924f2514f2293)

### observed_connections-008741

```text
(config-dia-peer)# exit <cr>
```

Handler ` RVA 0xBD06CF0 `；selector ` 23 `；EOL ` RVA 0x338A5CE0 `。

模式根 ` RVA 0x338A5B48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-66de5186b15d107c](../../evidence/conditions-sets-040.md#c-66de5186b15d107c)

### observed_connections-008756

```text
(config-dia-peer)# ip vrf forwarding <string> <cr>
```

Handler ` RVA 0xBD06CF0 `；selector ` 10 `；EOL ` RVA 0x338AF1F8 `。

模式根 ` RVA 0x338A5B48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Table name。

[条件 C-47462c87aa26a9d1](../../evidence/conditions-sets-028.md#c-47462c87aa26a9d1) · [参数 P-86960567bbc69d26](../../evidence/parameters-sets-010.md#p-86960567bbc69d26)

### observed_connections-008755

```text
(config-dia-peer)# no address ipv4 <address> <cr>
```

Handler ` RVA 0xBD06CF0 `；selector ` 13 `；EOL ` RVA 0x338AE258 `。

模式根 ` RVA 0x338A5B48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` IP address of diameter peer。

[参数 P-62861a6f6f116278](../../evidence/parameters-sets-008.md#p-62861a6f6f116278) · [状态效果 S-c05e58ae5f3d9ada](../../evidence/state_effects-sets-041.md#s-c05e58ae5f3d9ada)

### observed_connections-008751

```text
(config-dia-peer)# no destination host <cr>
```

Handler ` RVA 0xBD06CF0 `；selector ` 8 `；EOL ` RVA 0x338AF5C0 `。

模式根 ` RVA 0x338A5B48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b7504be7cad9bc85](../../evidence/conditions-sets-071.md#c-b7504be7cad9bc85) · [状态效果 S-c05e58ae5f3d9ada](../../evidence/state_effects-sets-041.md#s-c05e58ae5f3d9ada)

### observed_connections-008754

```text
(config-dia-peer)# no destination realm <cr>
```

Handler ` RVA 0xBD06CF0 `；selector ` 7 `；EOL ` RVA 0x338AF8A8 `。

模式根 ` RVA 0x338A5B48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7a3622d36ba89a81](../../evidence/conditions-sets-047.md#c-7a3622d36ba89a81) · [状态效果 S-c05e58ae5f3d9ada](../../evidence/state_effects-sets-041.md#s-c05e58ae5f3d9ada)

### observed_connections-008757

```text
(config-dia-peer)# no ip vrf forwarding <cr>
```

Handler ` RVA 0xBD06CF0 `；selector ` 10 `；EOL ` RVA 0x338AF1F8 `。

模式根 ` RVA 0x338A5B48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-6e0cc53d598fe9e5](../../evidence/conditions-sets-043.md#c-6e0cc53d598fe9e5) · [状态效果 S-c05e58ae5f3d9ada](../../evidence/state_effects-sets-041.md#s-c05e58ae5f3d9ada)

### observed_connections-008753

```text
(config-dia-peer)# no peer-type server <cr>
```

Handler ` RVA 0xBD06CF0 `；selector ` 14 `；EOL ` RVA 0x338AFFE8 `。

模式根 ` RVA 0x338A5B48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-e4137a3cbb9d6c1e](../../evidence/state_effects-sets-048.md#s-e4137a3cbb9d6c1e)

### observed_connections-008744

```text
(config-dia-peer)# no security <cr>
```

Handler ` RVA 0xBD06CF0 `；selector ` 11 `；EOL ` RVA 0x338AE9E0 `。

模式根 ` RVA 0x338A5B48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-9bf045908213be36](../../evidence/conditions-sets-060.md#c-9bf045908213be36) · [状态效果 S-c05e58ae5f3d9ada](../../evidence/state_effects-sets-041.md#s-c05e58ae5f3d9ada)

### observed_connections-008749

```text
(config-dia-peer)# no timer connection <cr>
```

Handler ` RVA 0xBD06CF0 `；selector ` 3 `；EOL ` RVA 0x338AED88 `。

模式根 ` RVA 0x338A5B48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-390482741f9ea0aa](../../evidence/conditions-sets-022.md#c-390482741f9ea0aa) · [状态效果 S-32b70c9ace9ad60c](../../evidence/state_effects-sets-011.md#s-32b70c9ace9ad60c)

### observed_connections-008742

```text
(config-dia-peer)# no transport <cr>
```

Handler ` RVA 0xBD06CF0 `；selector ` 12 `；EOL ` RVA 0x338AE5B0 `。

模式根 ` RVA 0x338A5B48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-794aaf89eca29627](../../evidence/conditions-sets-047.md#c-794aaf89eca29627) · [状态效果 S-c05e58ae5f3d9ada](../../evidence/state_effects-sets-041.md#s-c05e58ae5f3d9ada)

### observed_connections-008746

```text
(config-dia-peer)# peer-type server <cr>
```

Handler ` RVA 0xBD06CF0 `；selector ` 14 `；EOL ` RVA 0x338AFFE8 `。

模式根 ` RVA 0x338A5B48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[状态效果 S-3f3b71bbfba5e021](../../evidence/state_effects-sets-014.md#s-3f3b71bbfba5e021)

### observed_connections-008743

```text
(config-dia-peer)# security ipsec <cr>
```

Handler ` RVA 0xBD06CF0 `；selector ` 11 `；EOL ` RVA 0x338AE9E0 `。

模式根 ` RVA 0x338A5B48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e826ee59da3802ff](../../evidence/conditions-sets-090.md#c-e826ee59da3802ff) · [状态效果 S-9fbffbebc880ee01](../../evidence/state_effects-sets-034.md#s-9fbffbebc880ee01)

### observed_connections-008758

```text
(config-dia-peer)# source interface <interface> <cr>
```

Handler ` RVA 0xBD06CF0 `；selector ` 2 `；EOL ` RVA 0x338AFCA0 `。

模式根 ` RVA 0x338A5B48 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-915fdd2c1dc0feb8](../../evidence/conditions-sets-056.md#c-915fdd2c1dc0feb8) · [缺口 G-14c1d4c9491b602a](../../evidence/gaps-sets-001.md#g-14c1d4c9491b602a) · [参数 P-61005120187ce8dc](../../evidence/parameters-sets-008.md#p-61005120187ce8dc)

### observed_connections-008748

```text
(config-dia-peer)# timer connection <number:1..1000> <cr>
```

Handler ` RVA 0xBD06CF0 `；selector ` 3 `；EOL ` RVA 0x338AED88 `。

模式根 ` RVA 0x338A5B48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timer value in seconds。

[条件 C-2bde1bd3a4f38f1c](../../evidence/conditions-sets-017.md#c-2bde1bd3a4f38f1c) · [参数 P-9793aae3e9f2d632](../../evidence/parameters-sets-012.md#p-9793aae3e9f2d632) · [状态效果 S-0f39561160492d91](../../evidence/state_effects-sets-004.md#s-0f39561160492d91)

### observed_connections-008745

```text
(config-dia-peer)# transport tcp <cr>
```

Handler ` RVA 0xBD06CF0 `；selector ` 12 `；EOL ` RVA 0x338AE5B0 `。

模式根 ` RVA 0x338A5B48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-eb0208fe18f73d9b](../../evidence/conditions-sets-091.md#c-eb0208fe18f73d9b) · [状态效果 S-b53ae5a4a1c652ad](../../evidence/state_effects-sets-038.md#s-b53ae5a4a1c652ad)
