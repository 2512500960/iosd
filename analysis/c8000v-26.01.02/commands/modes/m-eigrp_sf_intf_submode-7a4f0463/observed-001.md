# eigrp_sf_intf_submode · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-008639

```text
(config-router-sf-interface)# authentication key-chain <string> <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 50 `；EOL ` RVA 0x346A6188 `。

模式根 ` RVA 0x346A5448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` name of key-chain。

[条件 C-0fe35392429e2088](../../evidence/conditions-sets-006.md#c-0fe35392429e2088) · [参数 P-ae5158f8658c8552](../../evidence/parameters-sets-013.md#p-ae5158f8658c8552)

### observed_connections-008641

```text
(config-router-sf-interface)# authentication mode hmac-sha-256 <string> <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 51 `；EOL ` RVA 0x346A5BE0 `。

模式根 ` RVA 0x346A5448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Authentication key-string used to compute HMAC-SHA-256 hash (maximum 32 characters for clear text, 69 characters for AES encrypted and 66 characters for proprietary)。

[条件 C-703db5b51bbd9746](../../evidence/conditions-sets-043.md#c-703db5b51bbd9746) · [参数 P-65ba89f51d90dfcc](../../evidence/parameters-sets-008.md#p-65ba89f51d90dfcc) · [状态效果 S-4c895bf01887ce4e](../../evidence/state_effects-sets-017.md#s-4c895bf01887ce4e)

### observed_connections-008636

```text
(config-router-sf-interface)# authentication mode md5 <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 51 `；EOL ` RVA 0x346A5A68 `。

模式根 ` RVA 0x346A5448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-615c4cbce5a7fa21](../../evidence/conditions-sets-038.md#c-615c4cbce5a7fa21) · [状态效果 S-50dad478fece765e](../../evidence/state_effects-sets-018.md#s-50dad478fece765e)

### observed_connections-008617

```text
(config-router-sf-interface)# bandwidth-percent <number:1..999999> <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 54 `；EOL ` RVA 0x346A6838 `。

模式根 ` RVA 0x346A5448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Maximum bandwidth percentage that EIGRP may use。

[条件 C-b38c788d9b2219f4](../../evidence/conditions-sets-069.md#c-b38c788d9b2219f4) · [参数 P-0ec2155fef7c38ed](../../evidence/parameters-sets-002.md#p-0ec2155fef7c38ed)

### observed_connections-008609

```text
(config-router-sf-interface)# dampening-change <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 55 `；EOL ` RVA 0x346A6BC0 `。

模式根 ` RVA 0x346A5448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3828521644209f02](../../evidence/conditions-sets-022.md#c-3828521644209f02) · [状态效果 S-c5dd64668c7b3c33](../../evidence/state_effects-sets-042.md#s-c5dd64668c7b3c33)

### observed_connections-008610

```text
(config-router-sf-interface)# dampening-interval <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 56 `；EOL ` RVA 0x346A6F48 `。

模式根 ` RVA 0x346A5448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-16d22b5bb961c0e4](../../evidence/conditions-sets-009.md#c-16d22b5bb961c0e4) · [状态效果 S-352bdcd7aefd3d7f](../../evidence/state_effects-sets-012.md#s-352bdcd7aefd3d7f)

### observed_connections-008640

```text
(config-router-sf-interface)# default authentication key-chain <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 50 `；EOL ` RVA 0x346A6188 `。

模式根 ` RVA 0x346A5448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-af5818f37b4d6377](../../evidence/conditions-sets-068.md#c-af5818f37b4d6377) · [状态效果 S-667302f8a16c6a7e](../../evidence/state_effects-sets-022.md#s-667302f8a16c6a7e)

### observed_connections-008637

```text
(config-router-sf-interface)# default authentication mode <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 51 `；EOL ` RVA 0x346A5A68 `。

模式根 ` RVA 0x346A5448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f5ac9ee1fc6a1b1e](../../evidence/conditions-sets-095.md#c-f5ac9ee1fc6a1b1e) · [状态效果 S-667302f8a16c6a7e](../../evidence/state_effects-sets-022.md#s-667302f8a16c6a7e)

### observed_connections-008618

```text
(config-router-sf-interface)# default bandwidth-percent <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 54 `；EOL ` RVA 0x346A6838 `。

模式根 ` RVA 0x346A5448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1b8cfd641f6d04bb](../../evidence/conditions-sets-011.md#c-1b8cfd641f6d04bb) · [状态效果 S-667302f8a16c6a7e](../../evidence/state_effects-sets-022.md#s-667302f8a16c6a7e)

### observed_connections-008621

```text
(config-router-sf-interface)# default dampening-change <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 55 `；EOL ` RVA 0x346A6BC0 `。

模式根 ` RVA 0x346A5448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-15a630e1bb3f8623](../../evidence/conditions-sets-009.md#c-15a630e1bb3f8623) · [状态效果 S-34296d3e84b9890a](../../evidence/state_effects-sets-012.md#s-34296d3e84b9890a)

### observed_connections-008625

```text
(config-router-sf-interface)# default dampening-interval <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 56 `；EOL ` RVA 0x346A6F48 `。

模式根 ` RVA 0x346A5448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d71b1663f96a4734](../../evidence/conditions-sets-083.md#c-d71b1663f96a4734) · [状态效果 S-9e06d1f9b273ce30](../../evidence/state_effects-sets-034.md#s-9e06d1f9b273ce30)

### observed_connections-008628

```text
(config-router-sf-interface)# default hello-interval <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 58 `；EOL ` RVA 0x346A75F8 `。

模式根 ` RVA 0x346A5448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-76d03c61d9d81641](../../evidence/conditions-sets-046.md#c-76d03c61d9d81641) · [状态效果 S-667302f8a16c6a7e](../../evidence/state_effects-sets-022.md#s-667302f8a16c6a7e)

### observed_connections-008633

```text
(config-router-sf-interface)# default hold-time <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 59 `；EOL ` RVA 0x346A7948 `。

模式根 ` RVA 0x346A5448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-77a99e86de43897f](../../evidence/conditions-sets-047.md#c-77a99e86de43897f) · [状态效果 S-667302f8a16c6a7e](../../evidence/state_effects-sets-022.md#s-667302f8a16c6a7e)

### observed_connections-008631

```text
(config-router-sf-interface)# default shutdown <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 63 `；EOL ` RVA 0x346A7C38 `。

模式根 ` RVA 0x346A5448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-667302f8a16c6a7e](../../evidence/state_effects-sets-022.md#s-667302f8a16c6a7e)

### observed_connections-008634

```text
(config-router-sf-interface)# default split-horizon <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 64 `；EOL ` RVA 0x346A7EF0 `。

模式根 ` RVA 0x346A5448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-667302f8a16c6a7e](../../evidence/state_effects-sets-022.md#s-667302f8a16c6a7e)

### observed_connections-008615

```text
(config-router-sf-interface)# default test-bandwidth <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 53 `；EOL ` RVA 0x346A64E8 `。

模式根 ` RVA 0x346A5448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-efb7e2eb6af484a9](../../evidence/conditions-sets-093.md#c-efb7e2eb6af484a9) · [状态效果 S-667302f8a16c6a7e](../../evidence/state_effects-sets-022.md#s-667302f8a16c6a7e)

### observed_connections-008623

```text
(config-router-sf-interface)# default test-delay <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 57 `；EOL ` RVA 0x346A7298 `。

模式根 ` RVA 0x346A5448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7dd2a168b0859f5e](../../evidence/conditions-sets-049.md#c-7dd2a168b0859f5e) · [状态效果 S-667302f8a16c6a7e](../../evidence/state_effects-sets-022.md#s-667302f8a16c6a7e)

### observed_connections-008608

```text
(config-router-sf-interface)# exit-sf-interface <cr>
```

Handler ` RVA 0xF593790 `；selector ` 0 `；EOL ` RVA 0x346A82C0 `。

模式根 ` RVA 0x346A5448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-58e256e1fc36f67a](../../evidence/conditions-sets-035.md#c-58e256e1fc36f67a)

### observed_connections-008626

```text
(config-router-sf-interface)# hello-interval <number:1..65535> <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 58 `；EOL ` RVA 0x346A75F8 `。

模式根 ` RVA 0x346A5448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Seconds between hello transmissions。

[条件 C-73ef19509147fa6b](../../evidence/conditions-sets-045.md#c-73ef19509147fa6b) · [参数 P-03b8661a7e814340](../../evidence/parameters-sets-001.md#p-03b8661a7e814340)

### observed_connections-008630

```text
(config-router-sf-interface)# hold-time <number:1..65535> <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 59 `；EOL ` RVA 0x346A7948 `。

模式根 ` RVA 0x346A5448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Seconds before neighbor is considered down。

[条件 C-4f8a299390b31cb9](../../evidence/conditions-sets-031.md#c-4f8a299390b31cb9) · [参数 P-7418d8b33642cc4a](../../evidence/parameters-sets-009.md#p-7418d8b33642cc4a)

### observed_connections-008638

```text
(config-router-sf-interface)# no authentication key-chain <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 50 `；EOL ` RVA 0x346A6188 `。

模式根 ` RVA 0x346A5448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8d08f808c6e67aaa](../../evidence/conditions-sets-055.md#c-8d08f808c6e67aaa) · [状态效果 S-76aad98677ca5138](../../evidence/state_effects-sets-025.md#s-76aad98677ca5138)

### observed_connections-008635

```text
(config-router-sf-interface)# no authentication mode <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 51 `；EOL ` RVA 0x346A5A68 `。

模式根 ` RVA 0x346A5448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f9f492f9225dfcd3](../../evidence/conditions-sets-097.md#c-f9f492f9225dfcd3) · [状态效果 S-76aad98677ca5138](../../evidence/state_effects-sets-025.md#s-76aad98677ca5138)

### observed_connections-008616

```text
(config-router-sf-interface)# no bandwidth-percent <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 54 `；EOL ` RVA 0x346A6838 `。

模式根 ` RVA 0x346A5448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a4e1e6276ac70fab](../../evidence/conditions-sets-064.md#c-a4e1e6276ac70fab) · [状态效果 S-76aad98677ca5138](../../evidence/state_effects-sets-025.md#s-76aad98677ca5138)

### observed_connections-008619

```text
(config-router-sf-interface)# no dampening-change <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 55 `；EOL ` RVA 0x346A6BC0 `。

模式根 ` RVA 0x346A5448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-08ea525654e3f156](../../evidence/conditions-sets-004.md#c-08ea525654e3f156) · [状态效果 S-297ef0baba5fe08f](../../evidence/state_effects-sets-009.md#s-297ef0baba5fe08f)

### observed_connections-008622

```text
(config-router-sf-interface)# no dampening-interval <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 56 `；EOL ` RVA 0x346A6F48 `。

模式根 ` RVA 0x346A5448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-423db6d5509feb5a](../../evidence/conditions-sets-026.md#c-423db6d5509feb5a) · [状态效果 S-3145b2c88c6a0b0d](../../evidence/state_effects-sets-011.md#s-3145b2c88c6a0b0d)

### observed_connections-008624

```text
(config-router-sf-interface)# no hello-interval <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 58 `；EOL ` RVA 0x346A75F8 `。

模式根 ` RVA 0x346A5448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ce08e96d472f2c2a](../../evidence/conditions-sets-079.md#c-ce08e96d472f2c2a) · [状态效果 S-76aad98677ca5138](../../evidence/state_effects-sets-025.md#s-76aad98677ca5138)

### observed_connections-008629

```text
(config-router-sf-interface)# no hold-time <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 59 `；EOL ` RVA 0x346A7948 `。

模式根 ` RVA 0x346A5448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-2a1eacc1d2913c3b](../../evidence/conditions-sets-016.md#c-2a1eacc1d2913c3b) · [状态效果 S-76aad98677ca5138](../../evidence/state_effects-sets-025.md#s-76aad98677ca5138)

### observed_connections-008627

```text
(config-router-sf-interface)# no shutdown <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 63 `；EOL ` RVA 0x346A7C38 `。

模式根 ` RVA 0x346A5448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-76aad98677ca5138](../../evidence/state_effects-sets-025.md#s-76aad98677ca5138)

### observed_connections-008632

```text
(config-router-sf-interface)# no split-horizon <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 64 `；EOL ` RVA 0x346A7EF0 `。

模式根 ` RVA 0x346A5448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-76aad98677ca5138](../../evidence/state_effects-sets-025.md#s-76aad98677ca5138)

### observed_connections-008613

```text
(config-router-sf-interface)# no test-bandwidth <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 53 `；EOL ` RVA 0x346A64E8 `。

模式根 ` RVA 0x346A5448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-9ac79e3d397dc05f](../../evidence/conditions-sets-060.md#c-9ac79e3d397dc05f) · [状态效果 S-76aad98677ca5138](../../evidence/state_effects-sets-025.md#s-76aad98677ca5138)

### observed_connections-008620

```text
(config-router-sf-interface)# no test-delay <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 57 `；EOL ` RVA 0x346A7298 `。

模式根 ` RVA 0x346A5448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-214f6024f4f14cbd](../../evidence/conditions-sets-013.md#c-214f6024f4f14cbd) · [状态效果 S-76aad98677ca5138](../../evidence/state_effects-sets-025.md#s-76aad98677ca5138)

### observed_connections-008611

```text
(config-router-sf-interface)# shutdown <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 63 `；EOL ` RVA 0x346A7C38 `。

模式根 ` RVA 0x346A5448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-008612

```text
(config-router-sf-interface)# split-horizon <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 64 `；EOL ` RVA 0x346A7EF0 `。

模式根 ` RVA 0x346A5448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-008614

```text
(config-router-sf-interface)# test-bandwidth <number:1..4294967295> <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 53 `；EOL ` RVA 0x346A64E8 `。

模式根 ` RVA 0x346A5448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` &lt;1-4294967295&gt; bandwidth in kilobits per second。

[条件 C-1334ae2315b399d3](../../evidence/conditions-sets-008.md#c-1334ae2315b399d3) · [参数 P-59799a376916847c](../../evidence/parameters-sets-007.md#p-59799a376916847c)

### observed_connections-008642

```text
(config-router-sf-interface)# test-delay <?general_to_number_action@555589bfb270> <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 57 `；EOL ` RVA 0x346A7298 `。

模式根 ` RVA 0x346A5448 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7885a4607e2d3484](../../evidence/conditions-sets-047.md#c-7885a4607e2d3484) · [缺口 G-42d6451a3002e59a](../../evidence/gaps-sets-003.md#g-42d6451a3002e59a)
