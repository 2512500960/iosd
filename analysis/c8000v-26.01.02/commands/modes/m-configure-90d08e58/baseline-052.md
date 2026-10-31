# configure · 六个基础模式的历史连接

[模式索引](README.md) · [总索引](../../README.md)

### path-058838

```text
(config)# do-exec show crypto key pubkey-chain rsa address <address> <cr>
```

Handler ` RVA 0x123A4C00 `；selector ` 0 `；EOL ` RVA 0x35794548 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Peer IP address。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-4f58b1bb520f6f99](../../evidence/parameters-sets-007.md#p-4f58b1bb520f6f99) · [状态效果 S-123d6229254cb294](../../evidence/state_effects-sets-004.md#s-123d6229254cb294)

### path-058830

```text
(config)# do-exec show crypto key pubkey-chain rsa name <string> <cr>
```

Handler ` RVA 0x123A4C00 `；selector ` 0 `；EOL ` RVA 0x35794250 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Peer name。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-4ab5581401eb1bf1](../../evidence/parameters-sets-006.md#p-4ab5581401eb1bf1) · [状态效果 S-1cac83af79c939b0](../../evidence/state_effects-sets-007.md#s-1cac83af79c939b0)

### path-058847

```text
(config)# do-exec show crypto key pubkey-chain rsa vrf <string> <cr>
```

Handler ` RVA 0x123A4C00 `；selector ` 0 `；EOL ` RVA 0x357948A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` the VRF name。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-3106e7451af1ac7a](../../evidence/parameters-sets-004.md#p-3106e7451af1ac7a) · [状态效果 S-4bfeb7908b572597](../../evidence/state_effects-sets-017.md#s-4bfeb7908b572597)

### path-042463

```text
(config)# do-exec show crypto key storage <cr>
```

Handler ` RVA 0x121539B0 `；selector ` 0 `；EOL ` RVA 0x35795218 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042539

```text
(config)# do-exec show crypto pki server <cr>
```

Handler ` RVA 0xBBBC250 `；selector ` 0 `；EOL ` RVA 0x33870D68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-2bd2e891ca6b4f1c](../../evidence/state_effects-sets-010.md#s-2bd2e891ca6b4f1c)

### path-027745

```text
(config)# do-exec show cts <cr>
```

Handler ` RVA 0x13033940 `；selector ` 0 `；EOL ` RVA 0x35A288F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ea013992bb6273f0](../../evidence/conditions-sets-090.md#c-ea013992bb6273f0) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-051291

```text
(config)# do-exec show cts ap sgt-info <string> <cr>
```

Handler ` RVA 0x13033940 `；selector ` 33 `；EOL ` RVA 0x35A1CB80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Show SGT info by AP name。

[条件 C-e31f11854fd08352](../../evidence/conditions-sets-087.md#c-e31f11854fd08352) · [参数 P-2249494c4998cbf4](../../evidence/parameters-sets-003.md#p-2249494c4998cbf4) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042707

```text
(config)# do-exec show cts authorization entries <cr>
```

Handler ` RVA 0x13033940 `；selector ` 15 `；EOL ` RVA 0x35A1B718 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d17ebfab06d88ff3](../../evidence/conditions-sets-081.md#c-d17ebfab06d88ff3) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033210

```text
(config)# do-exec show cts credentials <cr>
```

Handler ` RVA 0x13033940 `；selector ` 6 `；EOL ` RVA 0x35A18060 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1b1c43bdf7cc4d14](../../evidence/conditions-sets-011.md#c-1b1c43bdf7cc4d14) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033251

```text
(config)# do-exec show cts environment-data <cr>
```

Handler ` RVA 0x13033940 `；selector ` 8 `；EOL ` RVA 0x35A19268 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6709b12fd5bbcefd](../../evidence/conditions-sets-040.md#c-6709b12fd5bbcefd) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042780

```text
(config)# do-exec show cts ha sync-status <cr>
```

Handler ` RVA 0x13033940 `；selector ` 39 `；EOL ` RVA 0x35A1CE50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ea013992bb6273f0](../../evidence/conditions-sets-090.md#c-ea013992bb6273f0) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033278

```text
(config)# do-exec show cts interface <cr>
```

Handler ` RVA 0x13033940 `；selector ` 1 `；EOL ` RVA 0x35A18718 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c1b0de8f31f5434e](../../evidence/conditions-sets-075.md#c-c1b0de8f31f5434e) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061169

```text
(config)# do-exec show cts interface <interface> <cr>
```

Handler ` RVA 0x13033940 `；selector ` 1 `；EOL ` RVA 0x35A18718 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-55a63be272eaf9c1](../../evidence/conditions-sets-034.md#c-55a63be272eaf9c1) · [缺口 G-c05a47c21b89d969](../../evidence/gaps-sets-007.md#g-c05a47c21b89d969) · [参数 P-043d9e61c9495761](../../evidence/parameters-sets-001.md#p-043d9e61c9495761) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042633

```text
(config)# do-exec show cts interface brief <cr>
```

Handler ` RVA 0x13033940 `；selector ` 2 `；EOL ` RVA 0x35A189C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c1b0de8f31f5434e](../../evidence/conditions-sets-075.md#c-c1b0de8f31f5434e) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042656

```text
(config)# do-exec show cts interface summary <cr>
```

Handler ` RVA 0x13033940 `；selector ` 3 `；EOL ` RVA 0x35A18C68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c1b0de8f31f5434e](../../evidence/conditions-sets-075.md#c-c1b0de8f31f5434e) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033225

```text
(config)# do-exec show cts keystore <cr>
```

Handler ` RVA 0x13033940 `；selector ` 4 `；EOL ` RVA 0x35A18348 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-22128c275a43e6d4](../../evidence/conditions-sets-013.md#c-22128c275a43e6d4) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062218

```text
(config)# do-exec show cts macsec counters interface <interface> <cr>
```

Handler ` RVA 0x16071FB0 `；selector ` 0 `；EOL ` RVA 0x35EADA38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4aa78f68bf4f8e6a](../../evidence/conditions-sets-029.md#c-4aa78f68bf4f8e6a) · [缺口 G-75c4e3c27564342b](../../evidence/gaps-sets-005.md#g-75c4e3c27564342b) · [参数 P-bce36eccb78ff860](../../evidence/parameters-sets-014.md#p-bce36eccb78ff860) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033195

```text
(config)# do-exec show cts pacs <cr>
```

Handler ` RVA 0x13033940 `；selector ` 5 `；EOL ` RVA 0x35A17D78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d776fc6f1702af87](../../evidence/conditions-sets-083.md#c-d776fc6f1702af87) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033332

```text
(config)# do-exec show cts policy <cr>
```

Handler ` RVA 0x13033940 `；selector ` 12 `；EOL ` RVA 0x35A1A170 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-93763c2b4ea4bf99](../../evidence/conditions-sets-057.md#c-93763c2b4ea4bf99) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042721

```text
(config)# do-exec show cts policy peer <cr>
```

Handler ` RVA 0x13033940 `；selector ` 10 `；EOL ` RVA 0x35A199D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d549887b64a6224d](../../evidence/conditions-sets-082.md#c-d549887b64a6224d) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042824

```text
(config)# do-exec show cts policy sgt <cr>
```

Handler ` RVA 0x13033940 `；selector ` 11 `；EOL ` RVA 0x35A19DC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e1d387a978eb407b](../../evidence/conditions-sets-087.md#c-e1d387a978eb407b) · [状态效果 S-8b301ffbbcb9b988](../../evidence/state_effects-sets-030.md#s-8b301ffbbcb9b988)

### path-051247

```text
(config)# do-exec show cts policy-server details active <cr>
```

Handler ` RVA 0x13033940 `；selector ` 43 `；EOL ` RVA 0x35A1AE20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-58435242123bc2bd](../../evidence/conditions-sets-035.md#c-58435242123bc2bd) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-051268

```text
(config)# do-exec show cts policy-server details all <cr>
```

Handler ` RVA 0x13033940 `；selector ` 41 `；EOL ` RVA 0x35A1B0C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-58435242123bc2bd](../../evidence/conditions-sets-035.md#c-58435242123bc2bd) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-056508

```text
(config)# do-exec show cts policy-server details name <string> <cr>
```

Handler ` RVA 0x13033940 `；selector ` 42 `；EOL ` RVA 0x35A1B3B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of the server。

[条件 C-58435242123bc2bd](../../evidence/conditions-sets-035.md#c-58435242123bc2bd) · [参数 P-58c816d50814c6ce](../../evidence/parameters-sets-007.md#p-58c816d50814c6ce) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-051231

```text
(config)# do-exec show cts policy-server statistics active <cr>
```

Handler ` RVA 0x13033940 `；selector ` 46 `；EOL ` RVA 0x35A1A5A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-58435242123bc2bd](../../evidence/conditions-sets-035.md#c-58435242123bc2bd) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-051255

```text
(config)# do-exec show cts policy-server statistics all <cr>
```

Handler ` RVA 0x13033940 `；selector ` 44 `；EOL ` RVA 0x35A1A850 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-58435242123bc2bd](../../evidence/conditions-sets-035.md#c-58435242123bc2bd) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-056502

```text
(config)# do-exec show cts policy-server statistics name <string> <cr>
```

Handler ` RVA 0x13033940 `；selector ` 45 `；EOL ` RVA 0x35A1AB38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of the server。

[条件 C-58435242123bc2bd](../../evidence/conditions-sets-035.md#c-58435242123bc2bd) · [参数 P-a116b3c14ccfdc61](../../evidence/parameters-sets-012.md#p-a116b3c14ccfdc61) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033329

```text
(config)# do-exec show cts provisioning <cr>
```

Handler ` RVA 0x13033940 `；selector ` 13 `；EOL ` RVA 0x35A1BA78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-29b1fedbdefb2a60](../../evidence/conditions-sets-016.md#c-29b1fedbdefb2a60) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042727

```text
(config)# do-exec show cts provisioning queue <cr>
```

Handler ` RVA 0x13033940 `；selector ` 14 `；EOL ` RVA 0x35A1BA50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-29b1fedbdefb2a60](../../evidence/conditions-sets-016.md#c-29b1fedbdefb2a60) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033291

```text
(config)# do-exec show cts rbacl <cr>
```

Handler ` RVA 0x13033940 `；selector ` 9 `；EOL ` RVA 0x35A195F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-eac5244d56a04427](../../evidence/conditions-sets-091.md#c-eac5244d56a04427) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-043122

```text
(config)# do-exec show cts role-based counters <cr>
```

Handler ` RVA 0x141F88B0 `；selector ` 2 `；EOL ` RVA 0x35CFC620 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c88a245bd6e9817e](../../evidence/conditions-sets-077.md#c-c88a245bd6e9817e) · [状态效果 S-4ab72e5ee667e7f9](../../evidence/state_effects-sets-016.md#s-4ab72e5ee667e7f9)

### path-043155

```text
(config)# do-exec show cts role-based permissions <cr>
```

Handler ` RVA 0x141F88B0 `；selector ` 0 `；EOL ` RVA 0x35CFCBD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-55d9e3e147393bf8](../../evidence/conditions-sets-034.md#c-55d9e3e147393bf8) · [状态效果 S-93ab19c0b8813267](../../evidence/state_effects-sets-031.md#s-93ab19c0b8813267)

### path-061785

```text
(config)# do-exec show cts role-based sgt-map <prefix:dynamic> <cr>
```

Handler ` RVA 0x1403CDF0 `；selector ` 1 `；EOL ` RVA 0x35CEA118 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` Mappings for IPv4 prefix &lt;network&gt;/&lt;length&gt;, e.g., 35.0.0.0/8。

[条件 C-8986b126ff6ed539](../../evidence/conditions-sets-053.md#c-8986b126ff6ed539) · [缺口 G-577a73092863a6f2](../../evidence/gaps-sets-004.md#g-577a73092863a6f2) · [参数 P-27acb80bb4f9d379](../../evidence/parameters-sets-003.md#p-27acb80bb4f9d379) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-051410

```text
(config)# do-exec show cts role-based sgt-map platform <cr>
```

Handler ` RVA 0x1403CDF0 `；selector ` 1 `；EOL ` RVA 0x35CEA118 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-dbe21acb36bc3d56](../../evidence/conditions-sets-085.md#c-dbe21acb36bc3d56) · [状态效果 S-efba2330e2c73587](../../evidence/state_effects-sets-051.md#s-efba2330e2c73587)

### path-033241

```text
(config)# do-exec show cts server-list <cr>
```

Handler ` RVA 0x13033940 `；selector ` 7 `；EOL ` RVA 0x35A18F80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-dac4263279cd32d1](../../evidence/conditions-sets-084.md#c-dac4263279cd32d1) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042849

```text
(config)# do-exec show cts sg-epg translations <cr>
```

Handler ` RVA 0x13033940 `；selector ` 20 `；EOL ` RVA 0x35A1C5A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-022731bf3a684763](../../evidence/conditions-sets-001.md#c-022731bf3a684763) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-051324

```text
(config)# do-exec show cts sg-epg translations all <cr>
```

Handler ` RVA 0x13033940 `；selector ` 23 `；EOL ` RVA 0x35A1C580 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-022731bf3a684763](../../evidence/conditions-sets-001.md#c-022731bf3a684763) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-051298

```text
(config)# do-exec show cts sg-epg translations default-epg <cr>
```

Handler ` RVA 0x13033940 `；selector ` 22 `；EOL ` RVA 0x35A1C2D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-022731bf3a684763](../../evidence/conditions-sets-001.md#c-022731bf3a684763) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-051275

```text
(config)# do-exec show cts sg-epg translations default-sg <cr>
```

Handler ` RVA 0x13033940 `；selector ` 21 `；EOL ` RVA 0x35A1C030 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-022731bf3a684763](../../evidence/conditions-sets-001.md#c-022731bf3a684763) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-056579

```text
(config)# do-exec show cts sxp ap connections <string> <cr>
```

Handler ` RVA 0x13227830 `；selector ` 34 `；EOL ` RVA 0x35A51B20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Show SXP connection details by AP name。

[条件 C-1bbcd1564ad27ff4](../../evidence/conditions-sets-011.md#c-1bbcd1564ad27ff4) · [参数 P-69c8548296abda45](../../evidence/parameters-sets-008.md#p-69c8548296abda45) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-056583

```text
(config)# do-exec show cts sxp ap summary <string> <cr>
```

Handler ` RVA 0x13227830 `；selector ` 35 `；EOL ` RVA 0x35A51DE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Show SXP summary for the given sxp profile-name。

[条件 C-1bbcd1564ad27ff4](../../evidence/conditions-sets-011.md#c-1bbcd1564ad27ff4) · [参数 P-e2b6b7253722fb32](../../evidence/parameters-sets-017.md#p-e2b6b7253722fb32) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042946

```text
(config)# do-exec show cts sxp connections <cr>
```

Handler ` RVA 0x13227830 `；selector ` 16 `；EOL ` RVA 0x35A50708 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bf119e243b7a8faa](../../evidence/conditions-sets-074.md#c-bf119e243b7a8faa) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-051404

```text
(config)# do-exec show cts sxp connections brief <cr>
```

Handler ` RVA 0x13227830 `；selector ` 17 `；EOL ` RVA 0x35A506E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bf119e243b7a8faa](../../evidence/conditions-sets-074.md#c-bf119e243b7a8faa) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-043139

```text
(config)# do-exec show cts sxp export-import-group <cr>
```

Handler ` RVA 0x13227830 `；selector ` 49 `；EOL ` RVA 0x35A52718 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-05bbdb05a5f17fb5](../../evidence/conditions-sets-003.md#c-05bbdb05a5f17fb5) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-043044

```text
(config)# do-exec show cts sxp export-list <cr>
```

Handler ` RVA 0x13227830 `；selector ` 47 `；EOL ` RVA 0x35A520E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-05bbdb05a5f17fb5](../../evidence/conditions-sets-003.md#c-05bbdb05a5f17fb5) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-043067

```text
(config)# do-exec show cts sxp filter-group <cr>
```

Handler ` RVA 0x13227830 `；selector ` 26 `；EOL ` RVA 0x35A515E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ea013992bb6273f0](../../evidence/conditions-sets-090.md#c-ea013992bb6273f0) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042970

```text
(config)# do-exec show cts sxp filter-list <cr>
```

Handler ` RVA 0x13227830 `；selector ` 25 `；EOL ` RVA 0x35A51278 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ea013992bb6273f0](../../evidence/conditions-sets-090.md#c-ea013992bb6273f0) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-043064

```text
(config)# do-exec show cts sxp import-list <cr>
```

Handler ` RVA 0x13227830 `；selector ` 48 `；EOL ` RVA 0x35A523D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-05bbdb05a5f17fb5](../../evidence/conditions-sets-003.md#c-05bbdb05a5f17fb5) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042971

```text
(config)# do-exec show cts sxp sgt-map <cr>
```

Handler ` RVA 0x13227830 `；selector ` 18 `；EOL ` RVA 0x35A50D30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6645353b2923a766](../../evidence/conditions-sets-040.md#c-6645353b2923a766) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-051424

```text
(config)# do-exec show cts sxp sgt-map brief <cr>
```

Handler ` RVA 0x13227830 `；selector ` 19 `；EOL ` RVA 0x35A50D08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6645353b2923a766](../../evidence/conditions-sets-040.md#c-6645353b2923a766) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033177

```text
(config)# do-exec show cts transaction-id <cr>
```

Handler ` RVA 0x13033940 `；selector ` 54 `；EOL ` RVA 0x35A17A90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042120

```text
(config)# do-exec show cwmp map hosttable <cr>
```

Handler ` RVA 0x16472800 `；selector ` 13 `；EOL ` RVA 0x35F8CE78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-041963

```text
(config)# do-exec show cwmp map landevice <cr>
```

Handler ` RVA 0x16472800 `；selector ` 6 `；EOL ` RVA 0x35F8BBE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042029

```text
(config)# do-exec show cwmp map lanethernetinterface <cr>
```

Handler ` RVA 0x16472800 `；selector ` 9 `；EOL ` RVA 0x35F8C3D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042073

```text
(config)# do-exec show cwmp map manageddevice <cr>
```

Handler ` RVA 0x16472800 `；selector ` 11 `；EOL ` RVA 0x35F8C928 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042051

```text
(config)# do-exec show cwmp map portmapping <cr>
```

Handler ` RVA 0x16472800 `；selector ` 10 `；EOL ` RVA 0x35F8C680 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042095

```text
(config)# do-exec show cwmp map routetable <cr>
```

Handler ` RVA 0x16472800 `；selector ` 12 `；EOL ` RVA 0x35F8CBD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042011

```text
(config)# do-exec show cwmp map wanconnectiondevice <cr>
```

Handler ` RVA 0x16472800 `；selector ` 8 `；EOL ` RVA 0x35F8C130 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-041990

```text
(config)# do-exec show cwmp map wandevice <cr>
```

Handler ` RVA 0x16472800 `；selector ` 7 `；EOL ` RVA 0x35F8BE88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032807

```text
(config)# do-exec show cwmp methods <cr>
```

Handler ` RVA 0x16472800 `；selector ` 1 `；EOL ` RVA 0x35F8AB60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-041912

```text
(config)# do-exec show cwmp parameter all <cr>
```

Handler ` RVA 0x16472800 `；selector ` 3 `；EOL ` RVA 0x35F8B288 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-c7a35fb36a082c95](../../evidence/state_effects-sets-042.md#s-c7a35fb36a082c95)

### path-050647

```text
(config)# do-exec show cwmp parameter notify all <cr>
```

Handler ` RVA 0x16472800 `；selector ` 2 `；EOL ` RVA 0x35F8AED8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-38ef0599bd2df22e](../../evidence/state_effects-sets-013.md#s-38ef0599bd2df22e)

### path-041938

```text
(config)# do-exec show cwmp persistent data <cr>
```

Handler ` RVA 0x16472800 `；selector ` 5 `；EOL ` RVA 0x35F8B910 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032837

```text
(config)# do-exec show cwmp session <cr>
```

Handler ` RVA 0x16472800 `；selector ` 4 `；EOL ` RVA 0x35F8B600 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-029548

```text
(config)# do-exec show dampening interface <cr>
```

Handler ` RVA 0xE47A600 `；selector ` 1 `；EOL ` RVA 0x342C3AF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-75a696445ff71727](../../evidence/state_effects-sets-025.md#s-75a696445ff71727)

### path-026967

```text
(config)# do-exec show data-corruption <cr>
```

Handler ` RVA 0xE1131A0 `；selector ` 0 `；EOL ` RVA 0x34208498 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033260

```text
(config)# do-exec show data-descriptor controller <cr>
```

Handler ` RVA 0xD550080 `；selector ` 0 `；EOL ` RVA 0x33E7EDD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-576f1cf2b58c2d28](../../evidence/conditions-sets-034.md#c-576f1cf2b58c2d28) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033272

```text
(config)# do-exec show data-descriptor hwidb <cr>
```

Handler ` RVA 0xD5500D0 `；selector ` 0 `；EOL ` RVA 0x33E7F080 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-50e7fe4ac5b7f91e](../../evidence/conditions-sets-032.md#c-50e7fe4ac5b7f91e) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033312

```text
(config)# do-exec show data-descriptor queue <cr>
```

Handler ` RVA 0xD550400 `；selector ` 0 `；EOL ` RVA 0x33E7F638 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9d12baaac17fe3d4](../../evidence/conditions-sets-061.md#c-9d12baaac17fe3d4) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042704

```text
(config)# do-exec show data-descriptor queue old <cr>
```

Handler ` RVA 0xD550220 `；selector ` 0 `；EOL ` RVA 0x33E7F610 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fc9ae8fcfc50cefb](../../evidence/conditions-sets-097.md#c-fc9ae8fcfc50cefb) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033285

```text
(config)# do-exec show data-descriptor swidb <cr>
```

Handler ` RVA 0xD550120 `；selector ` 0 `；EOL ` RVA 0x33E7F328 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a929367a4dd5297f](../../evidence/conditions-sets-065.md#c-a929367a4dd5297f) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032943

```text
(config)# do-exec show database clients <cr>
```

Handler ` RVA 0xE1079C0 `；selector ` 2 `；EOL ` RVA 0x342025F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-050823

```text
(config)# do-exec show database data <string> <number:0..2> <cr>
```

Handler ` RVA 0xE1079C0 `；selector ` 1 `；EOL ` RVA 0x34202370 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of database；` unsigned_number ` Client type。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-8901519ec5008c62](../../evidence/parameters-sets-011.md#p-8901519ec5008c62) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032918

```text
(config)# do-exec show database names <cr>
```

Handler ` RVA 0xE1079C0 `；selector ` 0 `；EOL ` RVA 0x34202020 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033221

```text
(config)# do-exec show dcm assa <cr>
```

Handler ` RVA 0xBCC09A0 `；selector ` 4 `；EOL ` RVA 0x3389C9E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033234

```text
(config)# do-exec show dcm client <cr>
```

Handler ` RVA 0xBCC09A0 `；selector ` 0 `；EOL ` RVA 0x3389C160 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d3fbf234c0746499](../../evidence/conditions-sets-082.md#c-d3fbf234c0746499) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-051181

```text
(config)# do-exec show dcm client <number:1..4294967295> subscription <cr>
```

Handler ` RVA 0xBCC09A0 `；selector ` 2 `；EOL ` RVA 0x3389C1C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Client ID。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-9549ab7b759714b6](../../evidence/parameters-sets-011.md#p-9549ab7b759714b6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033207

```text
(config)# do-exec show dcm data-providers <cr>
```

Handler ` RVA 0xBCC09A0 `；selector ` 1 `；EOL ` RVA 0x3389C738 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042611

```text
(config)# do-exec show dcm errcode <number:0..60> <cr>
```

Handler ` RVA 0xBCC09A0 `；selector ` 5 `；EOL ` RVA 0x3389CF70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` DCM error number。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-749b33c25c111926](../../evidence/parameters-sets-009.md#p-749b33c25c111926) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033231

```text
(config)# do-exec show dcm session <cr>
```

Handler ` RVA 0xBCC09A0 `；selector ` 3 `；EOL ` RVA 0x3389CC88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-026788

```text
(config)# do-exec show debugging <cr>
```

Handler ` RVA 0xE001F30 `；selector ` 0 `；EOL ` RVA 0x34163880 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-029128

```text
(config)# do-exec show debugging condition <cr>
```

Handler ` RVA 0xE012E90 `；selector ` 0 `；EOL ` RVA 0x34168658 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-026852

```text
(config)# do-exec show derived-config <cr>
```

Handler ` RVA 0xD6EEDF0 `；selector ` 0 `；EOL ` RVA 0x33EDE870 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7c323505ada09dc2](../../evidence/conditions-sets-048.md#c-7c323505ada09dc2) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-060571

```text
(config)# do-exec show derived-config <interface> <cr>
```

Handler ` RVA 0xD6EEDF0 `；selector ` 0 `；EOL ` RVA 0x33EDE870 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9ab6b77d058757b7](../../evidence/conditions-sets-060.md#c-9ab6b77d058757b7) · [缺口 G-7fdba88877f8cb01](../../evidence/gaps-sets-005.md#g-7fdba88877f8cb01) · [参数 P-126905f311986849](../../evidence/parameters-sets-002.md#p-126905f311986849) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062967

```text
(config)# do-exec show device-tracking capture-policy bd <number:dynamic> <cr>
```

Handler ` RVA 0x13688090 `；selector ` 1043 `；EOL ` RVA 0x35BF05E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Bridge-domain number。

[条件 C-251acb470f0f935a](../../evidence/conditions-sets-014.md#c-251acb470f0f935a) · [缺口 G-a744bad2ea74af88](../../evidence/gaps-sets-006.md#g-a744bad2ea74af88) · [参数 P-4fa181d8b3f0f52d](../../evidence/parameters-sets-007.md#p-4fa181d8b3f0f52d) · [状态效果 S-2adce03ccef9ba44](../../evidence/state_effects-sets-010.md#s-2adce03ccef9ba44)

### path-062966

```text
(config)# do-exec show device-tracking counters bd <number:dynamic> <cr>
```

Handler ` RVA 0x13688090 `；selector ` 1044 `；EOL ` RVA 0x35BEFFE8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Bridge-domain number。

[条件 C-f524acb5280e66a2](../../evidence/conditions-sets-095.md#c-f524acb5280e66a2) · [缺口 G-954500c3dee916bc](../../evidence/gaps-sets-005.md#g-954500c3dee916bc) · [参数 P-893246b950948853](../../evidence/parameters-sets-011.md#p-893246b950948853) · [状态效果 S-332a66be120e0020](../../evidence/state_effects-sets-011.md#s-332a66be120e0020)

### path-062969

```text
(config)# do-exec show device-tracking database bdid <number:dynamic> <cr>
```

Handler ` RVA 0x136862F0 `；selector ` 1048 `；EOL ` RVA 0x35BF18E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Bridge-domain number。

[条件 C-420b49dbecb829fe](../../evidence/conditions-sets-026.md#c-420b49dbecb829fe) · [缺口 G-e0bce44584ac230f](../../evidence/gaps-sets-008.md#g-e0bce44584ac230f) · [参数 P-5bb64854af237801](../../evidence/parameters-sets-007.md#p-5bb64854af237801) · [状态效果 S-b48181ec13e05cab](../../evidence/state_effects-sets-038.md#s-b48181ec13e05cab)

### path-032812

```text
(config)# do-exec show device-tracking events <cr>
```

Handler ` RVA 0x13688090 `；selector ` 1046 `；EOL ` RVA 0x35BEF528 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b47adab449e17bb5](../../evidence/conditions-sets-070.md#c-b47adab449e17bb5) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032839

```text
(config)# do-exec show device-tracking features <cr>
```

Handler ` RVA 0x13688090 `；selector ` 1045 `；EOL ` RVA 0x35BEFB10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b47adab449e17bb5](../../evidence/conditions-sets-070.md#c-b47adab449e17bb5) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062213

```text
(config)# do-exec show device-tracking internal access-list interface <interface> <cr>
```

Handler ` RVA 0x13688090 `；selector ` 1041 `；EOL ` RVA 0x35BF3EE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-16797c5ddedc5865](../../evidence/conditions-sets-009.md#c-16797c5ddedc5865) · [缺口 G-41445b3ad313435a](../../evidence/gaps-sets-003.md#g-41445b3ad313435a) · [参数 P-20ecc1b56b18594e](../../evidence/parameters-sets-003.md#p-20ecc1b56b18594e) · [状态效果 S-0be2063e10051d91](../../evidence/state_effects-sets-003.md#s-0be2063e10051d91)

### path-042042

```text
(config)# do-exec show device-tracking internal counters <cr>
```

Handler ` RVA 0x13688090 `；selector ` 1040 `；EOL ` RVA 0x35BF1ED0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7d29535f38d3cf03](../../evidence/conditions-sets-049.md#c-7d29535f38d3cf03) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042174

```text
(config)# do-exec show device-tracking internal crimson-dhcp-svr <cr>
```

Handler ` RVA 0x13688090 `；selector ` 1057 `；EOL ` RVA 0x35BF2ED0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7d29535f38d3cf03](../../evidence/conditions-sets-049.md#c-7d29535f38d3cf03) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042155

```text
(config)# do-exec show device-tracking internal crimson-fault-evq <cr>
```

Handler ` RVA 0x13688090 `；selector ` 1056 `；EOL ` RVA 0x35BF2C28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7d29535f38d3cf03](../../evidence/conditions-sets-049.md#c-7d29535f38d3cf03) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042089

```text
(config)# do-exec show device-tracking internal crimson-ip <cr>
```

Handler ` RVA 0x13688090 `；selector ` 1053 `；EOL ` RVA 0x35BF2420 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7d29535f38d3cf03](../../evidence/conditions-sets-049.md#c-7d29535f38d3cf03) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042135

```text
(config)# do-exec show device-tracking internal crimson-ip-evq <cr>
```

Handler ` RVA 0x13688090 `；selector ` 1055 `；EOL ` RVA 0x35BF2978 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7d29535f38d3cf03](../../evidence/conditions-sets-049.md#c-7d29535f38d3cf03) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042065

```text
(config)# do-exec show device-tracking internal crimson-mac <cr>
```

Handler ` RVA 0x13688090 `；selector ` 1052 `；EOL ` RVA 0x35BF2178 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7d29535f38d3cf03](../../evidence/conditions-sets-049.md#c-7d29535f38d3cf03) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042114

```text
(config)# do-exec show device-tracking internal crimson-mac-evq <cr>
```

Handler ` RVA 0x13688090 `；selector ` 1054 `；EOL ` RVA 0x35BF26C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7d29535f38d3cf03](../../evidence/conditions-sets-049.md#c-7d29535f38d3cf03) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061765

```text
(config)# do-exec show device-tracking internal dhcp-server-stats <?ipv4orv6_addr_action@55558b147178> <cr>
```

Handler ` RVA 0x13688090 `；selector ` 1058 `；EOL ` RVA 0x35BF3208 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7d29535f38d3cf03](../../evidence/conditions-sets-049.md#c-7d29535f38d3cf03) · [缺口 G-806f3934d411d270](../../evidence/gaps-sets-005.md#g-806f3934d411d270) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042211

```text
(config)# do-exec show device-tracking internal groups <cr>
```

Handler ` RVA 0x13687F50 `；selector ` 0 `；EOL ` RVA 0x35BF34C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7d29535f38d3cf03](../../evidence/conditions-sets-049.md#c-7d29535f38d3cf03) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062211

```text
(config)# do-exec show device-tracking internal notify interface <interface> <cr>
```

Handler ` RVA 0x13687FA0 `；selector ` 0 `；EOL ` RVA 0x35BF38D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-40aa7da070e34bae](../../evidence/conditions-sets-025.md#c-40aa7da070e34bae) · [缺口 G-c24c4127b78ccaec](../../evidence/gaps-sets-007.md#g-c24c4127b78ccaec) · [参数 P-54a67621c69da000](../../evidence/parameters-sets-007.md#p-54a67621c69da000) · [状态效果 S-b4bb768a49ae313c](../../evidence/state_effects-sets-038.md#s-b4bb768a49ae313c)

### path-032848

```text
(config)# do-exec show device-tracking messages <cr>
```

Handler ` RVA 0x13688090 `；selector ` 1047 `；EOL ` RVA 0x35BEF860 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b47adab449e17bb5](../../evidence/conditions-sets-070.md#c-b47adab449e17bb5) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062968

```text
(config)# do-exec show device-tracking policies bd <number:dynamic> <cr>
```

Handler ` RVA 0x13688090 `；selector ` 1042 `；EOL ` RVA 0x35BF0CE8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Bridge-domain number。

[条件 C-53202d0b4ecb4856](../../evidence/conditions-sets-032.md#c-53202d0b4ecb4856) · [缺口 G-509e7f65dba42b35](../../evidence/gaps-sets-003.md#g-509e7f65dba42b35) · [参数 P-6cb23e24c768db24](../../evidence/parameters-sets-009.md#p-6cb23e24c768db24) · [状态效果 S-c7e28d01d250044e](../../evidence/state_effects-sets-042.md#s-c7e28d01d250044e)

### path-042004

```text
(config)# do-exec show device-tracking policy <string> <cr>
```

Handler ` RVA 0x1368B750 `；selector ` 0 `；EOL ` RVA 0x35BF1158 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Policy name for feature device-tracking。

[条件 C-b47adab449e17bb5](../../evidence/conditions-sets-070.md#c-b47adab449e17bb5) · [参数 P-776425f1a5b0bf27](../../evidence/parameters-sets-009.md#p-776425f1a5b0bf27) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033171

```text
(config)# do-exec show dhcp lease <cr>
```

Handler ` RVA 0xF472550 `；selector ` 1 `；EOL ` RVA 0x34652E40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-304450a2d9488836](../../evidence/conditions-sets-019.md#c-304450a2d9488836) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061165

```text
(config)# do-exec show dhcp lease <interface> <cr>
```

Handler ` RVA 0xF472550 `；selector ` 1 `；EOL ` RVA 0x34652E40 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-aebe2c32c5260377](../../evidence/conditions-sets-068.md#c-aebe2c32c5260377) · [缺口 G-41304126230c0345](../../evidence/gaps-sets-003.md#g-41304126230c0345) · [参数 P-a3a9923402d65310](../../evidence/parameters-sets-012.md#p-a3a9923402d65310) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033135

```text
(config)# do-exec show dhcp server <cr>
```

Handler ` RVA 0xF471F30 `；selector ` 0 `；EOL ` RVA 0x34652AD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032819

```text
(config)# do-exec show dhcp-server-tracking database <cr>
```

Handler ` RVA 0x136A1ED0 `；selector ` 0 `；EOL ` RVA 0x35C01420 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032757

```text
(config)# do-exec show dhcp-server-tracking policy <cr>
```

Handler ` RVA 0x136A1E80 `；selector ` 0 `；EOL ` RVA 0x35C010A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-043704

```text
(config)# do-exec show diag chassis eeprom <cr>
```

Handler ` RVA 0xED99270 `；selector ` 0 `；EOL ` RVA 0x34354F60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8009f9fb3b11d504](../../evidence/conditions-sets-050.md#c-8009f9fb3b11d504) · [状态效果 S-f98c3982ad4ad91d](../../evidence/state_effects-sets-053.md#s-f98c3982ad4ad91d)

### path-061800

```text
(config)# do-exec show diag subslot <?slotcard_func_action@5555898a8e68> eeprom <cr>
```

Handler ` RVA 0xED99270 `；selector ` 0 `；EOL ` RVA 0x34354F60 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8009f9fb3b11d504](../../evidence/conditions-sets-050.md#c-8009f9fb3b11d504) · [缺口 G-64713a147b3df393](../../evidence/gaps-sets-004.md#g-64713a147b3df393) · [状态效果 S-be11d00c277c1120](../../evidence/state_effects-sets-040.md#s-be11d00c277c1120)

### path-043268

```text
(config)# do-exec show diagnostic bootup level <cr>
```

Handler ` RVA 0xEB79810 `；selector ` 0 `；EOL ` RVA 0x343BA6C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9a1f9659812ebb80](../../evidence/conditions-sets-060.md#c-9a1f9659812ebb80) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-043384

```text
(config)# do-exec show diagnostic cns publish <cr>
```

Handler ` RVA 0x159C34B0 `；selector ` 1 `；EOL ` RVA 0x35DD3AC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c57f7bc397c85b26](../../evidence/conditions-sets-076.md#c-c57f7bc397c85b26) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061791

```text
(config)# do-exec show diagnostic content slot <?option@5555898db448> <cr>
```

Handler ` RVA 0xEB7A790 `；selector ` 7 `；EOL ` RVA 0x343BFBA8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-806da34b96ca1c2b](../../evidence/conditions-sets-050.md#c-806da34b96ca1c2b) · [缺口 G-4965f0866e885e51](../../evidence/gaps-sets-003.md#g-4965f0866e885e51) · [状态效果 S-031fc87d474daecb](../../evidence/state_effects-sets-001.md#s-031fc87d474daecb)

### path-043419

```text
(config)# do-exec show diagnostic content slot <cr>
```

Handler ` RVA 0xEB7A790 `；selector ` 9 `；EOL ` RVA 0x343C00A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8ba3fe679a20ea6f](../../evidence/conditions-sets-054.md#c-8ba3fe679a20ea6f) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062919

```text
(config)# do-exec show diagnostic description slot <?option@5555898db620> test <?number_help_func_action@555589914ac0> <string> <cr>
```

Handler ` RVA 0xEB7F780 `；selector ` 17 `；EOL ` RVA 0x343C0B60 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Test ID or Test Name。

[条件 C-ada51f6251513fed](../../evidence/conditions-sets-067.md#c-ada51f6251513fed) · [缺口 G-be4aaffea5e8b887](../../evidence/gaps-sets-007.md#g-be4aaffea5e8b887) · [参数 P-5778765eeb9cff45](../../evidence/parameters-sets-007.md#p-5778765eeb9cff45) · [状态效果 S-aa2345a1fb9b9878](../../evidence/state_effects-sets-036.md#s-aa2345a1fb9b9878)

### path-061790

```text
(config)# do-exec show diagnostic events slot <?option@5555898db090> <cr>
```

Handler ` RVA 0xEB7E470 `；selector ` 10 `；EOL ` RVA 0x343BEDE8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ece6cd8372810009](../../evidence/conditions-sets-092.md#c-ece6cd8372810009) · [缺口 G-ea1363b762140cfa](../../evidence/gaps-sets-008.md#g-ea1363b762140cfa) · [状态效果 S-58f5e1e380479895](../../evidence/state_effects-sets-019.md#s-58f5e1e380479895)

### path-051753

```text
(config)# do-exec show diagnostic events slot all <cr>
```

Handler ` RVA 0xEB7E470 `；selector ` 10 `；EOL ` RVA 0x343BEDE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c34ea5f194ee42bb](../../evidence/conditions-sets-075.md#c-c34ea5f194ee42bb) · [状态效果 S-58f5e1e380479895](../../evidence/state_effects-sets-019.md#s-58f5e1e380479895)

### path-033598

```text
(config)# do-exec show diagnostic level <cr>
```

Handler ` RVA 0xEB79810 `；selector ` 0 `；EOL ` RVA 0x343BA370 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0ab6bd1040d43071](../../evidence/conditions-sets-004.md#c-0ab6bd1040d43071) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-043239

```text
(config)# do-exec show diagnostic ondemand settings <cr>
```

Handler ` RVA 0xEB798C0 `；selector ` 0 `；EOL ` RVA 0x343BA020 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-eb7e8b9917cfdf11](../../evidence/conditions-sets-091.md#c-eb7e8b9917cfdf11) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062996

```text
(config)# do-exec show diagnostic ondemand test-parameter slot <?option@5555898dbd48> test <?number_help_func_action@555589914f68> <cr>
```

Handler ` RVA 0xEB7FBA0 `；selector ` 0 `；EOL ` RVA 0x343C0FE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3d1f2ff8bf527dd3](../../evidence/conditions-sets-024.md#c-3d1f2ff8bf527dd3) · [缺口 G-ff2eafc5e65e69a8](../../evidence/gaps-sets-009.md#g-ff2eafc5e65e69a8) · [状态效果 S-661b439b2451767c](../../evidence/state_effects-sets-022.md#s-661b439b2451767c)

### path-061795

```text
(config)# do-exec show diagnostic result slot <?option@5555898dae48> <cr>
```

Handler ` RVA 0xEB7D320 `；selector ` 0 `；EOL ` RVA 0x343BDDB0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4396076b72909525](../../evidence/conditions-sets-026.md#c-4396076b72909525) · [缺口 G-3abe9e3c5c292ae2](../../evidence/gaps-sets-003.md#g-3abe9e3c5c292ae2) · [状态效果 S-fed2d71952b95516](../../evidence/state_effects-sets-054.md#s-fed2d71952b95516)

### path-062222

```text
(config)# do-exec show diagnostic result slot <?option@5555898dae48> xml <cr>
```

Handler ` RVA 0xEB7D320 `；selector ` 2 `；EOL ` RVA 0x343BE068 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4396076b72909525](../../evidence/conditions-sets-026.md#c-4396076b72909525) · [缺口 G-3abe9e3c5c292ae2](../../evidence/gaps-sets-003.md#g-3abe9e3c5c292ae2) · [状态效果 S-fed2d71952b95516](../../evidence/state_effects-sets-054.md#s-fed2d71952b95516)

### path-043483

```text
(config)# do-exec show diagnostic result slot <cr>
```

Handler ` RVA 0xEB7D320 `；selector ` 3 `；EOL ` RVA 0x343BEA48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c5fdf8eea529a323](../../evidence/conditions-sets-076.md#c-c5fdf8eea529a323) · [状态效果 S-47328418940cebfc](../../evidence/state_effects-sets-016.md#s-47328418940cebfc)

### path-061792

```text
(config)# do-exec show diagnostic schedule slot <?option@5555898db270> <cr>
```

Handler ` RVA 0xEB7B150 `；selector ` 4 `；EOL ` RVA 0x343BF430 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c25dc6c7c3af1b1d](../../evidence/conditions-sets-075.md#c-c25dc6c7c3af1b1d) · [缺口 G-ac10029648ae8588](../../evidence/gaps-sets-006.md#g-ac10029648ae8588) · [状态效果 S-230f7f32b8d2ecf1](../../evidence/state_effects-sets-008.md#s-230f7f32b8d2ecf1)

### path-043438

```text
(config)# do-exec show diagnostic schedule slot <cr>
```

Handler ` RVA 0xEB7B150 `；selector ` 6 `；EOL ` RVA 0x343BF928 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-000aa952cb593d0c](../../evidence/conditions-sets-001.md#c-000aa952cb593d0c) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062221

```text
(config)# do-exec show diagnostic simulation failure slot <?option@5555898db7f8> <cr>
```

Handler ` RVA 0xEB7F070 `；selector ` 13 `；EOL ` RVA 0x343C0320 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6a44e00b6cae45d6](../../evidence/conditions-sets-041.md#c-6a44e00b6cae45d6) · [缺口 G-601b470c3b318fe5](../../evidence/gaps-sets-004.md#g-601b470c3b318fe5) · [状态效果 S-c1148a98b40f82da](../../evidence/state_effects-sets-041.md#s-c1148a98b40f82da)

### path-051793

```text
(config)# do-exec show diagnostic simulation failure slot <cr>
```

Handler ` RVA 0xEB7F070 `；selector ` 15 `；EOL ` RVA 0x343C0818 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6dede3f1cf2438f2](../../evidence/conditions-sets-043.md#c-6dede3f1cf2438f2) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061190

```text
(config)# do-exec show diagnostic slot <?option@5555898dac70> <cr>
```

Handler ` RVA 0xEB7D320 `；selector ` 0 `；EOL ` RVA 0x343BD3A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3a1e915c091a7fc8](../../evidence/conditions-sets-022.md#c-3a1e915c091a7fc8) · [缺口 G-20e934f634d2a172](../../evidence/gaps-sets-002.md#g-20e934f634d2a172) · [状态效果 S-b1166d5fb61e4002](../../evidence/state_effects-sets-038.md#s-b1166d5fb61e4002)

### path-033762

```text
(config)# do-exec show diagnostic slot <cr>
```

Handler ` RVA 0xEB7D320 `；selector ` 3 `；EOL ` RVA 0x343BDA38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a90c05e8205272ac](../../evidence/conditions-sets-065.md#c-a90c05e8205272ac) · [状态效果 S-80518d67d652a9fd](../../evidence/state_effects-sets-027.md#s-80518d67d652a9fd)

### path-033558

```text
(config)# do-exec show diagnostic status <cr>
```

Handler ` RVA 0xEB7EB30 `；selector ` 12 `；EOL ` RVA 0x343B9BA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-943353c2de22eb97](../../evidence/conditions-sets-057.md#c-943353c2de22eb97) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027159

```text
(config)# do-exec show dialer <cr>
```

Handler ` RVA 0xF4CC4F0 `；selector ` 0 `；EOL ` RVA 0x34666C98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1fb0788947c6b5aa](../../evidence/conditions-sets-012.md#c-1fb0788947c6b5aa) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-060621

```text
(config)# do-exec show dialer <interface> <cr>
```

Handler ` RVA 0xF4CC4F0 `；selector ` 0 `；EOL ` RVA 0x34666C98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e39e39c212ac7fda](../../evidence/conditions-sets-088.md#c-e39e39c212ac7fda) · [缺口 G-c1c50e7a93143aef](../../evidence/gaps-sets-007.md#g-c1c50e7a93143aef) · [参数 P-5dcfaee3fb3fba95](../../evidence/parameters-sets-007.md#p-5dcfaee3fb3fba95) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-036326

```text
(config)# do-exec show dialer dnis group <cr>
```

Handler ` RVA 0xF4E8D90 `；selector ` 0 `；EOL ` RVA 0x34674EB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-036192

```text
(config)# do-exec show dialer dnis number <cr>
```

Handler ` RVA 0xF4E8910 `；selector ` 1 `；EOL ` RVA 0x346748D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-036258

```text
(config)# do-exec show dialer dnis range <cr>
```

Handler ` RVA 0xF4E8910 `；selector ` 2 `；EOL ` RVA 0x34674BE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-029777

```text
(config)# do-exec show dialer maps <cr>
```

Handler ` RVA 0xF4CC4F0 `；selector ` 1 `；EOL ` RVA 0x34666970 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-029885

```text
(config)# do-exec show dialer sessions <cr>
```

Handler ` RVA 0xF4DC9E0 `；selector ` 2 `；EOL ` RVA 0x34675160 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033941

```text
(config)# do-exec show diameter attributes <cr>
```

Handler ` RVA 0xBD08210 `；selector ` 20 `；EOL ` RVA 0x338A9148 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cd68eb1f208a1195](../../evidence/conditions-sets-079.md#c-cd68eb1f208a1195) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-052031

```text
(config)# do-exec show diameter gx session all <cr>
```

Handler ` RVA 0xBD053B0 `；selector ` 28 `；EOL ` RVA 0x338A94C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cd68eb1f208a1195](../../evidence/conditions-sets-079.md#c-cd68eb1f208a1195) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-056765

```text
(config)# do-exec show diameter gx session id <string> <cr>
```

Handler ` RVA 0xBD053B0 `；selector ` 29 `；EOL ` RVA 0x338A97E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Gx session ID。

[条件 C-cd68eb1f208a1195](../../evidence/conditions-sets-079.md#c-cd68eb1f208a1195) · [参数 P-ba3bdd1a6bf1ea74](../../evidence/parameters-sets-014.md#p-ba3bdd1a6bf1ea74) · [状态效果 S-c93660c348d1ee7f](../../evidence/state_effects-sets-043.md#s-c93660c348d1ee7f)

### path-043835

```text
(config)# do-exec show diameter gx statistics <cr>
```

Handler ` RVA 0xBD053B0 `；selector ` 30 `；EOL ` RVA 0x338A9A78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cd68eb1f208a1195](../../evidence/conditions-sets-079.md#c-cd68eb1f208a1195) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-043834

```text
(config)# do-exec show diameter id-manager statistics <cr>
```

Handler ` RVA 0xBD053B0 `；selector ` 38 `；EOL ` RVA 0x338A9D50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cd68eb1f208a1195](../../evidence/conditions-sets-079.md#c-cd68eb1f208a1195) · [状态效果 S-21e27d4ca2d5b6b6](../../evidence/state_effects-sets-008.md#s-21e27d4ca2d5b6b6)

### path-033945

```text
(config)# do-exec show diameter peer <cr>
```

Handler ` RVA 0xBD053B0 `；selector ` 17 `；EOL ` RVA 0x338A8EB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cd68eb1f208a1195](../../evidence/conditions-sets-079.md#c-cd68eb1f208a1195) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033934

```text
(config)# do-exec show diameter redundancy <cr>
```

Handler ` RVA 0xBD053B0 `；selector ` 19 `；EOL ` RVA 0x338A8B80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cd68eb1f208a1195](../../evidence/conditions-sets-079.md#c-cd68eb1f208a1195) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033108

```text
(config)# do-exec show dlep clients <cr>
```

Handler ` RVA 0x132D1A60 `；selector ` 3 `；EOL ` RVA 0x35A60450 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bc330326b1b6a590](../../evidence/conditions-sets-073.md#c-bc330326b1b6a590) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061155

```text
(config)# do-exec show dlep clients <interface> <cr>
```

Handler ` RVA 0x132D1A60 `；selector ` 2 `；EOL ` RVA 0x35A60428 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b943fc55141b8fe1](../../evidence/conditions-sets-072.md#c-b943fc55141b8fe1) · [缺口 G-dd603a394c1382e2](../../evidence/gaps-sets-008.md#g-dd603a394c1382e2) · [参数 P-22b5af9bcfe68e69](../../evidence/parameters-sets-003.md#p-22b5af9bcfe68e69) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033098

```text
(config)# do-exec show dlep config <cr>
```

Handler ` RVA 0x132D1A60 `；selector ` 5 `；EOL ` RVA 0x35A5FE40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8d0a7205c81ae876](../../evidence/conditions-sets-055.md#c-8d0a7205c81ae876) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061154

```text
(config)# do-exec show dlep config <interface> <cr>
```

Handler ` RVA 0x132D1A60 `；selector ` 4 `；EOL ` RVA 0x35A5FE18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-076004507565d710](../../evidence/conditions-sets-003.md#c-076004507565d710) · [缺口 G-fc51eed873351711](../../evidence/gaps-sets-009.md#g-fc51eed873351711) · [参数 P-32f1bbf4df6e33f8](../../evidence/parameters-sets-004.md#p-32f1bbf4df6e33f8) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033125

```text
(config)# do-exec show dlep counters <cr>
```

Handler ` RVA 0x132D1A60 `；selector ` 7 `；EOL ` RVA 0x35A61048 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7394119a09f14ea0](../../evidence/conditions-sets-045.md#c-7394119a09f14ea0) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061158

```text
(config)# do-exec show dlep counters <interface> <cr>
```

Handler ` RVA 0x132D1A60 `；selector ` 6 `；EOL ` RVA 0x35A61020 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c0191e35ea584529](../../evidence/conditions-sets-074.md#c-c0191e35ea584529) · [缺口 G-1ad72129d7534d93](../../evidence/gaps-sets-001.md#g-1ad72129d7534d93) · [参数 P-a30d001b46b40ecf](../../evidence/parameters-sets-012.md#p-a30d001b46b40ecf) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033118

```text
(config)# do-exec show dlep neighbors <cr>
```

Handler ` RVA 0x132D1A60 `；selector ` 0 `；EOL ` RVA 0x35A60A60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a5beab96a284cbce](../../evidence/conditions-sets-064.md#c-a5beab96a284cbce) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061156

```text
(config)# do-exec show dlep neighbors <interface> <cr>
```

Handler ` RVA 0x132D1A60 `；selector ` 1 `；EOL ` RVA 0x35A60A38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-72740f02c8c4c302](../../evidence/conditions-sets-044.md#c-72740f02c8c4c302) · [缺口 G-fe667c4cda44eaee](../../evidence/gaps-sets-009.md#g-fe667c4cda44eaee) · [参数 P-d5ddbe15bedc7f6e](../../evidence/parameters-sets-016.md#p-d5ddbe15bedc7f6e) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061797

```text
(config)# do-exec show dlsw capabilities interface <interface> <cr>
```

Handler ` RVA 0x11421620 `；selector ` 0 `；EOL ` RVA 0x354CAB48 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2623a596fe253407](../../evidence/conditions-sets-015.md#c-2623a596fe253407) · [缺口 G-0aa29607b6b187bd](../../evidence/gaps-sets-001.md#g-0aa29607b6b187bd) · [参数 P-c0da1b1cf8d56408](../../evidence/parameters-sets-015.md#p-c0da1b1cf8d56408) · [状态效果 S-a1da6cf0f7e95517](../../evidence/state_effects-sets-034.md#s-a1da6cf0f7e95517)

### path-033809

```text
(config)# do-exec show dlsw fastcache <cr>
```

Handler ` RVA 0x11421620 `；selector ` 0 `；EOL ` RVA 0x354CAB48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a6537476bf634616](../../evidence/conditions-sets-064.md#c-a6537476bf634616) · [状态效果 S-0ef50eb71c22d7f4](../../evidence/state_effects-sets-004.md#s-0ef50eb71c22d7f4)

### path-027788

```text
(config)# do-exec show dmvpn <cr>
```

Handler ` RVA 0xF4F42C0 `；selector ` 0 `；EOL ` RVA 0x3467C2A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c7e31d1b35ee01d6](../../evidence/conditions-sets-077.md#c-c7e31d1b35ee01d6) · [状态效果 S-6317d2b6959da9ea](../../evidence/state_effects-sets-021.md#s-6317d2b6959da9ea)

### path-033672

```text
(config)# do-exec show dmvpn debug-condition <cr>
```

Handler ` RVA 0xF4F4E10 `；selector ` 0 `；EOL ` RVA 0x3467BB98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c7e31d1b35ee01d6](../../evidence/conditions-sets-077.md#c-c7e31d1b35ee01d6) · [状态效果 S-6317d2b6959da9ea](../../evidence/state_effects-sets-021.md#s-6317d2b6959da9ea)

### path-043440

```text
(config)# do-exec show dmvpn detail rwatch <cr>
```

Handler ` RVA 0xF4F4F20 `；selector ` 0 `；EOL ` RVA 0x3467C000 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1a03f454c71ccb92](../../evidence/conditions-sets-010.md#c-1a03f454c71ccb92) · [状态效果 S-1e5e9b2f9d191c3b](../../evidence/state_effects-sets-007.md#s-1e5e9b2f9d191c3b)

### path-061188

```text
(config)# do-exec show dmvpn rd <?vrf_rd_action@555589bd0ac0> <cr>
```

Handler ` RVA 0xF4F42C0 `；selector ` 0 `；EOL ` RVA 0x3467C2A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c7e31d1b35ee01d6](../../evidence/conditions-sets-077.md#c-c7e31d1b35ee01d6) · [缺口 G-8eb297e2609af30a](../../evidence/gaps-sets-005.md#g-8eb297e2609af30a) · [状态效果 S-a26a18ae88a80267](../../evidence/state_effects-sets-034.md#s-a26a18ae88a80267)

### path-061789

```text
(config)# do-exec show dmvpn rd <?vrf_rd_action@555589bd0ac0> debug-condition <cr>
```

Handler ` RVA 0xF4F4E10 `；selector ` 0 `；EOL ` RVA 0x3467BB98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c7e31d1b35ee01d6](../../evidence/conditions-sets-077.md#c-c7e31d1b35ee01d6) · [缺口 G-8eb297e2609af30a](../../evidence/gaps-sets-005.md#g-8eb297e2609af30a) · [状态效果 S-a26a18ae88a80267](../../evidence/state_effects-sets-034.md#s-a26a18ae88a80267)

### path-062220

```text
(config)# do-exec show dmvpn rd <?vrf_rd_action@555589bd0ac0> detail rwatch <cr>
```

Handler ` RVA 0xF4F4F20 `；selector ` 0 `；EOL ` RVA 0x3467C000 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1a03f454c71ccb92](../../evidence/conditions-sets-010.md#c-1a03f454c71ccb92) · [缺口 G-8eb297e2609af30a](../../evidence/gaps-sets-005.md#g-8eb297e2609af30a) · [状态效果 S-c4c15ae4cab8e638](../../evidence/state_effects-sets-042.md#s-c4c15ae4cab8e638)

### path-032224

```text
(config)# do-exec show dns-lookup cache <cr>
```

Handler ` RVA 0xD12D760 `；selector ` 1 `；EOL ` RVA 0x33D95160 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040850

```text
(config)# do-exec show dns-lookup hostname <string> <cr>
```

Handler ` RVA 0xD12D760 `；selector ` 2 `；EOL ` RVA 0x33D95448 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Specify host name。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-6ef002087d9de39d](../../evidence/parameters-sets-009.md#p-6ef002087d9de39d) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027652

```text
(config)# do-exec show dnsix <cr>
```

Handler ` RVA 0xD4A3700 `；selector ` 0 `；EOL ` RVA 0x33E56418 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027806

```text
(config)# do-exec show dot1q-tunnel <cr>
```

Handler ` RVA 0x15FEB9E0 `；selector ` 2 `；EOL ` RVA 0x35E93FC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061191

```text
(config)# do-exec show dot1q-tunnel interface <interface> <cr>
```

Handler ` RVA 0x15FEB9E0 `；selector ` 2 `；EOL ` RVA 0x35E93FC8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0b920da7e1e2468f](../../evidence/conditions-sets-005.md#c-0b920da7e1e2468f) · [缺口 G-06f6364f05ac9e29](../../evidence/gaps-sets-001.md#g-06f6364f05ac9e29) · [参数 P-6253425a392e888c](../../evidence/parameters-sets-008.md#p-6253425a392e888c) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027780

```text
(config)# do-exec show drip <cr>
```

Handler ` RVA 0x112B4330 `；selector ` 1 `；EOL ` RVA 0x3544C9C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027412

```text
(config)# do-exec show drops <cr>
```

Handler ` RVA 0x15863EF0 `；selector ` 0 `；EOL ` RVA 0x35D99578 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-030506

```text
(config)# do-exec show drops bqs <cr>
```

Handler ` RVA 0x15863970 `；selector ` 0 `；EOL ` RVA 0x35D98D00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-030458

```text
(config)# do-exec show drops crypto <cr>
```

Handler ` RVA 0x158636B0 `；selector ` 0 `；EOL ` RVA 0x35D987B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-030482

```text
(config)# do-exec show drops firewall <cr>
```

Handler ` RVA 0x15863810 `；selector ` 0 `；EOL ` RVA 0x35D98A58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-037244

```text
(config)# do-exec show drops history qfp <cr>
```

Handler ` RVA 0x15863C30 `；selector ` 0 `；EOL ` RVA 0x35D99078 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-046621

```text
(config)# do-exec show drops history qfp clear <cr>
```

Handler ` RVA 0x15863AD0 `；selector ` 0 `；EOL ` RVA 0x35D99050 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-030338

```text
(config)# do-exec show drops interface <cr>
```

Handler ` RVA 0x15862FD0 `；selector ` 0 `；EOL ` RVA 0x35D97A68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-030407

```text
(config)# do-exec show drops ip-all <cr>
```

Handler ` RVA 0x158633F0 `；selector ` 0 `；EOL ` RVA 0x35D98260 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-030384

```text
(config)# do-exec show drops nat <cr>
```

Handler ` RVA 0x15863290 `；selector ` 0 `；EOL ` RVA 0x35D97FB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-030432

```text
(config)# do-exec show drops punt <cr>
```

Handler ` RVA 0x15863550 `；selector ` 0 `；EOL ` RVA 0x35D98508 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-030309

```text
(config)# do-exec show drops qfp <cr>
```

Handler ` RVA 0x15862E70 `；selector ` 0 `；EOL ` RVA 0x35D977C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-030363

```text
(config)# do-exec show drops qos <cr>
```

Handler ` RVA 0x15863130 `；selector ` 0 `；EOL ` RVA 0x35D97D10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-030561

```text
(config)# do-exec show drops thresholds <cr>
```

Handler ` RVA 0x15863D90 `；selector ` 0 `；EOL ` RVA 0x35D99550 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-026715

```text
(config)# do-exec show dspfarm <cr>
```

Handler ` RVA 0x188BA840 `；selector ` 1 `；EOL ` RVA 0x367F29A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b3e12630f8428735](../../evidence/conditions-sets-070.md#c-b3e12630f8428735) · [状态效果 S-35ec2cf33d7b1f8d](../../evidence/state_effects-sets-012.md#s-35ec2cf33d7b1f8d)

### path-044585

```text
(config)# do-exec show dspfarm dsp stats <number:1..2147483647> <cr>
```

Handler ` RVA 0x188BA840 `；selector ` 1 `；EOL ` RVA 0x367F2FA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Show DSP stats for a call bridge with this BRIDGE_ID。

[条件 C-a72b56ff3afb8850](../../evidence/conditions-sets-064.md#c-a72b56ff3afb8850) · [参数 P-d9a9d5f872da573a](../../evidence/parameters-sets-016.md#p-d9a9d5f872da573a) · [状态效果 S-3dc6016a5fe7e8e1](../../evidence/state_effects-sets-014.md#s-3dc6016a5fe7e8e1)

### path-044430

```text
(config)# do-exec show dspfarm utilization profile all <cr>
```

Handler ` RVA 0x188AC750 `；selector ` 1 `；EOL ` RVA 0x367F25C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-495b0f7b9423e516](../../evidence/conditions-sets-029.md#c-495b0f7b9423e516) · [状态效果 S-d643810727afe915](../../evidence/state_effects-sets-045.md#s-d643810727afe915)

### path-027620

```text
(config)# do-exec show dtp <cr>
```

Handler ` RVA 0x15F14320 `；selector ` 0 `；EOL ` RVA 0x35E66940 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031927

```text
(config)# do-exec show dtp interface <cr>
```

Handler ` RVA 0x15F14320 `；selector ` 1 `；EOL ` RVA 0x35E66A00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1e8e761baf98357e](../../evidence/conditions-sets-012.md#c-1e8e761baf98357e) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061001

```text
(config)# do-exec show dtp interface <interface> <cr>
```

Handler ` RVA 0x15F14320 `；selector ` 1 `；EOL ` RVA 0x35E66A00 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-bd1ff5c5970744e0](../../evidence/conditions-sets-073.md#c-bd1ff5c5970744e0) · [缺口 G-4f4460a780d6d5ee](../../evidence/gaps-sets-003.md#g-4f4460a780d6d5ee) · [参数 P-d4b93c40f82a66f2](../../evidence/parameters-sets-016.md#p-d4b93c40f82a66f2) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-060978

```text
(config)# do-exec show dwnld_mgr AAA Unique ID <number:0..4294967295> <cr>
```

Handler ` RVA 0x106556F0 `；selector ` 0 `；EOL ` RVA 0x34BD98A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` specify the aaa_unique_id value in Hex。

[条件 C-df9337a9bc63d855](../../evidence/conditions-sets-086.md#c-df9337a9bc63d855) · [缺口 G-e684a3e6f70995a7](../../evidence/gaps-sets-008.md#g-e684a3e6f70995a7) · [参数 P-4baaedb8ac2ba868](../../evidence/parameters-sets-006.md#p-4baaedb8ac2ba868) · [状态效果 S-8d5b3ed9004911b4](../../evidence/state_effects-sets-030.md#s-8d5b3ed9004911b4)

### path-038922

```text
(config)# do-exec show dwnld_mgr profiles all <cr>
```

Handler ` RVA 0x106556F0 `；selector ` 0 `；EOL ` RVA 0x34BD98A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-c744049b462996ac](../../evidence/state_effects-sets-042.md#s-c744049b462996ac)

### path-031286

```text
(config)# do-exec show dxi map <cr>
```

Handler ` RVA 0xEF31BB0 `；selector ` 0 `；EOL ` RVA 0x3447F0B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031343

```text
(config)# do-exec show dxi pvc <cr>
```

Handler ` RVA 0xEF31BB0 `；selector ` 1 `；EOL ` RVA 0x3447F3C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061497

```text
(config)# do-exec show dxi pvc interface <interface> <cr>
```

Handler ` RVA 0xEF31BB0 `；selector ` 1 `；EOL ` RVA 0x3447F3C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0c64b1631595ffb0](../../evidence/conditions-sets-005.md#c-0c64b1631595ffb0) · [缺口 G-2634797d4cac812d](../../evidence/gaps-sets-002.md#g-2634797d4cac812d) · [参数 P-4514487d804bc180](../../evidence/parameters-sets-006.md#p-4514487d804bc180) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-060742

```text
(config)# do-exec show eapol <interface> <cr>
```

Handler ` RVA 0xCB44640 `；selector ` 0 `；EOL ` RVA 0x33BCFBB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-82965e759f8e7349](../../evidence/conditions-sets-051.md#c-82965e759f8e7349) · [缺口 G-8ac7f1a9bf9a1a41](../../evidence/gaps-sets-005.md#g-8ac7f1a9bf9a1a41) · [参数 P-69e1079ff89cd0aa](../../evidence/parameters-sets-008.md#p-69e1079ff89cd0aa) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-050551

```text
(config)# do-exec show eigrp address-family ipv4 accounting <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 98 `；EOL ` RVA 0x346B8728 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4be2875bada221b1](../../evidence/conditions-sets-030.md#c-4be2875bada221b1) · [状态效果 S-c4bc70e1358b0a5b](../../evidence/state_effects-sets-042.md#s-c4bc70e1358b0a5b)

### path-050533

```text
(config)# do-exec show eigrp address-family ipv4 interfaces <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 89 `；EOL ` RVA 0x346B7220 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-73b634352ab7537b](../../evidence/conditions-sets-045.md#c-73b634352ab7537b) · [状态效果 S-c4bc70e1358b0a5b](../../evidence/state_effects-sets-042.md#s-c4bc70e1358b0a5b)

### path-062174

```text
(config)# do-exec show eigrp address-family ipv4 interfaces <interface> <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 89 `；EOL ` RVA 0x346B7220 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7509be558a414034](../../evidence/conditions-sets-045.md#c-7509be558a414034) · [缺口 G-413c91d9c70cdbba](../../evidence/gaps-sets-003.md#g-413c91d9c70cdbba) · [参数 P-7e847aaff301e01b](../../evidence/parameters-sets-010.md#p-7e847aaff301e01b) · [状态效果 S-c4bc70e1358b0a5b](../../evidence/state_effects-sets-042.md#s-c4bc70e1358b0a5b)

### path-050559

```text
(config)# do-exec show eigrp address-family ipv4 neighbors <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 90 `；EOL ` RVA 0x346B6D28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-33cc5362802879e8](../../evidence/conditions-sets-020.md#c-33cc5362802879e8) · [状态效果 S-c4bc70e1358b0a5b](../../evidence/state_effects-sets-042.md#s-c4bc70e1358b0a5b)

### path-062177

```text
(config)# do-exec show eigrp address-family ipv4 neighbors <interface> <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 90 `；EOL ` RVA 0x346B6D28 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0080b8faa5526f68](../../evidence/conditions-sets-001.md#c-0080b8faa5526f68) · [缺口 G-d6f04a1526b38784](../../evidence/gaps-sets-007.md#g-d6f04a1526b38784) · [参数 P-cbef972ce6e1cd5a](../../evidence/parameters-sets-015.md#p-cbef972ce6e1cd5a) · [状态效果 S-c4bc70e1358b0a5b](../../evidence/state_effects-sets-042.md#s-c4bc70e1358b0a5b)

### path-050615

```text
(config)# do-exec show eigrp address-family ipv4 perf-stats <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 100 `；EOL ` RVA 0x346B92F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4be2875bada221b1](../../evidence/conditions-sets-030.md#c-4be2875bada221b1) · [状态效果 S-c4bc70e1358b0a5b](../../evidence/state_effects-sets-042.md#s-c4bc70e1358b0a5b)

### path-050588

```text
(config)# do-exec show eigrp address-family ipv4 sia-event <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 99 `；EOL ` RVA 0x346B8A70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4be2875bada221b1](../../evidence/conditions-sets-030.md#c-4be2875bada221b1) · [状态效果 S-36c0cff9d8323661](../../evidence/state_effects-sets-012.md#s-36c0cff9d8323661)

### path-050621

```text
(config)# do-exec show eigrp address-family ipv4 sia-statistics <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 99 `；EOL ` RVA 0x346B8DF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4be2875bada221b1](../../evidence/conditions-sets-030.md#c-4be2875bada221b1) · [状态效果 S-853f728d9cb6df6a](../../evidence/state_effects-sets-028.md#s-853f728d9cb6df6a)

### path-050489

```text
(config)# do-exec show eigrp address-family ipv4 timers <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 95 `；EOL ` RVA 0x346B74F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4be2875bada221b1](../../evidence/conditions-sets-030.md#c-4be2875bada221b1) · [状态效果 S-c4bc70e1358b0a5b](../../evidence/state_effects-sets-042.md#s-c4bc70e1358b0a5b)

### path-050781

```text
(config)# do-exec show eigrp address-family ipv4 topology <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 97 `；EOL ` RVA 0x346B7B50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0485ff243d74c18b](../../evidence/conditions-sets-002.md#c-0485ff243d74c18b) · [状态效果 S-fa6d4161a6dece60](../../evidence/state_effects-sets-053.md#s-fa6d4161a6dece60)

### path-062185

```text
(config)# do-exec show eigrp address-family ipv4 topology <prefix:dynamic> <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 97 `；EOL ` RVA 0x346B7B50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` Prefix &lt;network&gt;/&lt;length&gt;, e.g., 192.168.0.0/16。

[条件 C-0b2bfefc76f028f9](../../evidence/conditions-sets-005.md#c-0b2bfefc76f028f9) · [缺口 G-7d1a42e12c3fd448](../../evidence/gaps-sets-005.md#g-7d1a42e12c3fd448) · [参数 P-b491a89c592aa197](../../evidence/parameters-sets-014.md#p-b491a89c592aa197) · [状态效果 S-e4ebf01f95124156](../../evidence/state_effects-sets-048.md#s-e4ebf01f95124156)

### path-050505

```text
(config)# do-exec show eigrp address-family ipv4 traffic <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 96 `；EOL ` RVA 0x346B7798 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4be2875bada221b1](../../evidence/conditions-sets-030.md#c-4be2875bada221b1) · [状态效果 S-c4bc70e1358b0a5b](../../evidence/state_effects-sets-042.md#s-c4bc70e1358b0a5b)

### path-050506

```text
(config)# do-exec show eigrp address-family ipv6 accounting <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 98 `；EOL ` RVA 0x35456B90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d626b228299db8a5](../../evidence/conditions-sets-083.md#c-d626b228299db8a5) · [状态效果 S-6f80b63845d411e5](../../evidence/state_effects-sets-024.md#s-6f80b63845d411e5)

### path-050491

```text
(config)# do-exec show eigrp address-family ipv6 interfaces <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 89 `；EOL ` RVA 0x35455858 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-47c4cd37e4bb8363](../../evidence/conditions-sets-028.md#c-47c4cd37e4bb8363) · [状态效果 S-6f80b63845d411e5](../../evidence/state_effects-sets-024.md#s-6f80b63845d411e5)

### path-062171

```text
(config)# do-exec show eigrp address-family ipv6 interfaces <interface> <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 89 `；EOL ` RVA 0x35455858 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e14d9451113c9f01](../../evidence/conditions-sets-087.md#c-e14d9451113c9f01) · [缺口 G-5b13e35bae2d95f8](../../evidence/gaps-sets-004.md#g-5b13e35bae2d95f8) · [参数 P-70dd10e1c7ee0519](../../evidence/parameters-sets-009.md#p-70dd10e1c7ee0519) · [状态效果 S-6f80b63845d411e5](../../evidence/state_effects-sets-024.md#s-6f80b63845d411e5)

### path-050510

```text
(config)# do-exec show eigrp address-family ipv6 neighbors <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 90 `；EOL ` RVA 0x35455360 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-47222bc6964b7539](../../evidence/conditions-sets-028.md#c-47222bc6964b7539) · [状态效果 S-6f80b63845d411e5](../../evidence/state_effects-sets-024.md#s-6f80b63845d411e5)

### path-062173

```text
(config)# do-exec show eigrp address-family ipv6 neighbors <interface> <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 90 `；EOL ` RVA 0x35455360 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-80ba8195abe0f976](../../evidence/conditions-sets-050.md#c-80ba8195abe0f976) · [缺口 G-4a58f08a47ca293b](../../evidence/gaps-sets-003.md#g-4a58f08a47ca293b) · [参数 P-b26175db588ddd63](../../evidence/parameters-sets-014.md#p-b26175db588ddd63) · [状态效果 S-6f80b63845d411e5](../../evidence/state_effects-sets-024.md#s-6f80b63845d411e5)

### path-050586

```text
(config)# do-exec show eigrp address-family ipv6 perf-stats <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 100 `；EOL ` RVA 0x35457758 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d626b228299db8a5](../../evidence/conditions-sets-083.md#c-d626b228299db8a5) · [状态效果 S-6f80b63845d411e5](../../evidence/state_effects-sets-024.md#s-6f80b63845d411e5)

### path-050553

```text
(config)# do-exec show eigrp address-family ipv6 sia-event <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 99 `；EOL ` RVA 0x35456ED8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d626b228299db8a5](../../evidence/conditions-sets-083.md#c-d626b228299db8a5) · [状态效果 S-05b99028609ecf85](../../evidence/state_effects-sets-002.md#s-05b99028609ecf85)

### path-050589

```text
(config)# do-exec show eigrp address-family ipv6 sia-statistics <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 99 `；EOL ` RVA 0x35457260 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d626b228299db8a5](../../evidence/conditions-sets-083.md#c-d626b228299db8a5) · [状态效果 S-5dd9b952c583b3a8](../../evidence/state_effects-sets-020.md#s-5dd9b952c583b3a8)

### path-050460

```text
(config)# do-exec show eigrp address-family ipv6 timers <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 95 `；EOL ` RVA 0x35455B28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d626b228299db8a5](../../evidence/conditions-sets-083.md#c-d626b228299db8a5) · [状态效果 S-6f80b63845d411e5](../../evidence/state_effects-sets-024.md#s-6f80b63845d411e5)

### path-050690

```text
(config)# do-exec show eigrp address-family ipv6 topology <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 97 `；EOL ` RVA 0x35456180 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-852a3abab717bf44](../../evidence/conditions-sets-052.md#c-852a3abab717bf44) · [状态效果 S-ccb6f4191dc87312](../../evidence/state_effects-sets-043.md#s-ccb6f4191dc87312)

### path-062178

```text
(config)# do-exec show eigrp address-family ipv6 topology <prefix:dynamic> <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 97 `；EOL ` RVA 0x35456180 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` Network to display information about。

[条件 C-bcaaaab9650eda5e](../../evidence/conditions-sets-073.md#c-bcaaaab9650eda5e) · [缺口 G-9d70df28494e4a84](../../evidence/gaps-sets-006.md#g-9d70df28494e4a84) · [参数 P-c6fc7dd7bb559948](../../evidence/parameters-sets-015.md#p-c6fc7dd7bb559948) · [状态效果 S-6996b35c7181476c](../../evidence/state_effects-sets-023.md#s-6996b35c7181476c)

### path-050473

```text
(config)# do-exec show eigrp address-family ipv6 traffic <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 96 `；EOL ` RVA 0x35455DD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d626b228299db8a5](../../evidence/conditions-sets-083.md#c-d626b228299db8a5) · [状态效果 S-6f80b63845d411e5](../../evidence/state_effects-sets-024.md#s-6f80b63845d411e5)

### path-032506

```text
(config)# do-exec show eigrp parser <cr>
```

Handler ` RVA 0xF590E10 `；selector ` 91 `；EOL ` RVA 0x3469C668 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-3cd3ea7f5d1961e1](../../evidence/state_effects-sets-013.md#s-3cd3ea7f5d1961e1)

### path-032520

```text
(config)# do-exec show eigrp plugins <cr>
```

Handler ` RVA 0xF590E10 `；selector ` 92 `；EOL ` RVA 0x3469C970 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-eda4dc7fdf016252](../../evidence/conditions-sets-092.md#c-eda4dc7fdf016252) · [状态效果 S-1b4e8e153df9d5de](../../evidence/state_effects-sets-006.md#s-1b4e8e153df9d5de)

### path-032501

```text
(config)# do-exec show eigrp protocols <cr>
```

Handler ` RVA 0xF590E10 `；selector ` 93 `；EOL ` RVA 0x3469CD90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1b4e8e153df9d5de](../../evidence/state_effects-sets-006.md#s-1b4e8e153df9d5de)

### path-041537

```text
(config)# do-exec show eigrp service-family external-client <cr>
```

Handler ` RVA 0x10472870 `；selector ` 39 `；EOL ` RVA 0x34B3AE80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-847bd171a8f0c9df](../../evidence/state_effects-sets-028.md#s-847bd171a8f0c9df)

### path-050526

```text
(config)# do-exec show eigrp service-family ipv4 accounting <cr>
```

Handler ` RVA 0xF5933F0 `；selector ` 98 `；EOL ` RVA 0x346F3D80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-335bd6f895d8c282](../../evidence/conditions-sets-020.md#c-335bd6f895d8c282) · [状态效果 S-d478d83ef1758b7b](../../evidence/state_effects-sets-045.md#s-d478d83ef1758b7b)

### path-050620

```text
(config)# do-exec show eigrp service-family ipv4 clients <cr>
```

Handler ` RVA 0xF5933F0 `；selector ` 115 `；EOL ` RVA 0x346F49D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-335bd6f895d8c282](../../evidence/conditions-sets-020.md#c-335bd6f895d8c282) · [状态效果 S-d478d83ef1758b7b](../../evidence/state_effects-sets-045.md#s-d478d83ef1758b7b)

### path-056129

```text
(config)# do-exec show eigrp service-family ipv4 clients detail <cr>
```

Handler ` RVA 0xF5933F0 `；selector ` 116 `；EOL ` RVA 0x346F49B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-335bd6f895d8c282](../../evidence/conditions-sets-020.md#c-335bd6f895d8c282) · [状态效果 S-effb6d7154425b8a](../../evidence/state_effects-sets-051.md#s-effb6d7154425b8a)

### path-050509

```text
(config)# do-exec show eigrp service-family ipv4 interfaces <cr>
```

Handler ` RVA 0xF5933F0 `；selector ` 89 `；EOL ` RVA 0x346F27C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d824ffe7c071d49e](../../evidence/conditions-sets-083.md#c-d824ffe7c071d49e) · [状态效果 S-d478d83ef1758b7b](../../evidence/state_effects-sets-045.md#s-d478d83ef1758b7b)

### path-062172

```text
(config)# do-exec show eigrp service-family ipv4 interfaces <interface> <cr>
```

Handler ` RVA 0xF5933F0 `；selector ` 89 `；EOL ` RVA 0x346F27C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-048da1dfedca855d](../../evidence/conditions-sets-002.md#c-048da1dfedca855d) · [缺口 G-e9bf7cd3e35103cd](../../evidence/gaps-sets-008.md#g-e9bf7cd3e35103cd) · [参数 P-829c8ead46bb4054](../../evidence/parameters-sets-010.md#p-829c8ead46bb4054) · [状态效果 S-d478d83ef1758b7b](../../evidence/state_effects-sets-045.md#s-d478d83ef1758b7b)

### path-050534

```text
(config)# do-exec show eigrp service-family ipv4 neighbors <cr>
```

Handler ` RVA 0xF5933F0 `；selector ` 90 `；EOL ` RVA 0x346F22C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-53ac1b41a81ff19a](../../evidence/conditions-sets-033.md#c-53ac1b41a81ff19a) · [状态效果 S-d478d83ef1758b7b](../../evidence/state_effects-sets-045.md#s-d478d83ef1758b7b)

### path-062175

```text
(config)# do-exec show eigrp service-family ipv4 neighbors <interface> <cr>
```

Handler ` RVA 0xF5933F0 `；selector ` 90 `；EOL ` RVA 0x346F22C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5770aee7544ec635](../../evidence/conditions-sets-034.md#c-5770aee7544ec635) · [缺口 G-0f217afabfbbaddc](../../evidence/gaps-sets-001.md#g-0f217afabfbbaddc) · [参数 P-75c2f539614f2707](../../evidence/parameters-sets-009.md#p-75c2f539614f2707) · [状态效果 S-d478d83ef1758b7b](../../evidence/state_effects-sets-045.md#s-d478d83ef1758b7b)

### path-050575

```text
(config)# do-exec show eigrp service-family ipv4 sia-event <cr>
```

Handler ` RVA 0xF5933F0 `；selector ` 99 `；EOL ` RVA 0x346F40C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-335bd6f895d8c282](../../evidence/conditions-sets-020.md#c-335bd6f895d8c282) · [状态效果 S-f0b0025851024be8](../../evidence/state_effects-sets-051.md#s-f0b0025851024be8)

### path-050601

```text
(config)# do-exec show eigrp service-family ipv4 sia-statistics <cr>
```

Handler ` RVA 0xF5933F0 `；selector ` 99 `；EOL ` RVA 0x346F4450 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-335bd6f895d8c282](../../evidence/conditions-sets-020.md#c-335bd6f895d8c282) · [状态效果 S-b4eb52c3353fd9be](../../evidence/state_effects-sets-038.md#s-b4eb52c3353fd9be)

### path-050643

```text
(config)# do-exec show eigrp service-family ipv4 subscriptions <cr>
```

Handler ` RVA 0xF5933F0 `；selector ` 117 `；EOL ` RVA 0x346F4F20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-335bd6f895d8c282](../../evidence/conditions-sets-020.md#c-335bd6f895d8c282) · [状态效果 S-d478d83ef1758b7b](../../evidence/state_effects-sets-045.md#s-d478d83ef1758b7b)

### path-056142

```text
(config)# do-exec show eigrp service-family ipv4 subscriptions detail <cr>
```

Handler ` RVA 0xF5933F0 `；selector ` 118 `；EOL ` RVA 0x346F4EF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-335bd6f895d8c282](../../evidence/conditions-sets-020.md#c-335bd6f895d8c282) · [状态效果 S-3f18059b8fcd947f](../../evidence/state_effects-sets-014.md#s-3f18059b8fcd947f)

### path-050472

```text
(config)# do-exec show eigrp service-family ipv4 timers <cr>
```

Handler ` RVA 0xF5933F0 `；selector ` 95 `；EOL ` RVA 0x346F2A90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-335bd6f895d8c282](../../evidence/conditions-sets-020.md#c-335bd6f895d8c282) · [状态效果 S-d478d83ef1758b7b](../../evidence/state_effects-sets-045.md#s-d478d83ef1758b7b)

### path-050708

```text
(config)# do-exec show eigrp service-family ipv4 topology <cr>
```

Handler ` RVA 0xF5933F0 `；selector ` 97 `；EOL ` RVA 0x346F3328 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-402f8fdde5370b83](../../evidence/conditions-sets-025.md#c-402f8fdde5370b83) · [状态效果 S-c5d2265103c9495d](../../evidence/state_effects-sets-042.md#s-c5d2265103c9495d)

### path-050488

```text
(config)# do-exec show eigrp service-family ipv4 traffic <cr>
```

Handler ` RVA 0xF5933F0 `；selector ` 96 `；EOL ` RVA 0x346F2D38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-335bd6f895d8c282](../../evidence/conditions-sets-020.md#c-335bd6f895d8c282) · [状态效果 S-d478d83ef1758b7b](../../evidence/state_effects-sets-045.md#s-d478d83ef1758b7b)

### path-050572

```text
(config)# do-exec show eigrp service-family ipv6 accounting <cr>
```

Handler ` RVA 0xF5933F0 `；selector ` 98 `；EOL ` RVA 0x3547A488 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ead7f0a21e659ac3](../../evidence/conditions-sets-091.md#c-ead7f0a21e659ac3) · [状态效果 S-28cb502006350bc6](../../evidence/state_effects-sets-009.md#s-28cb502006350bc6)

### path-050666

```text
(config)# do-exec show eigrp service-family ipv6 clients <cr>
```

Handler ` RVA 0xF5933F0 `；selector ` 115 `；EOL ` RVA 0x3547B0E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ead7f0a21e659ac3](../../evidence/conditions-sets-091.md#c-ead7f0a21e659ac3) · [状态效果 S-28cb502006350bc6](../../evidence/state_effects-sets-009.md#s-28cb502006350bc6)

### path-056158

```text
(config)# do-exec show eigrp service-family ipv6 clients detail <cr>
```

Handler ` RVA 0xF5933F0 `；selector ` 116 `；EOL ` RVA 0x3547B0B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ead7f0a21e659ac3](../../evidence/conditions-sets-091.md#c-ead7f0a21e659ac3) · [状态效果 S-6aff2103ebc03381](../../evidence/state_effects-sets-023.md#s-6aff2103ebc03381)

### path-050558

```text
(config)# do-exec show eigrp service-family ipv6 interfaces <cr>
```

Handler ` RVA 0xF5933F0 `；selector ` 89 `；EOL ` RVA 0x35478EC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-29a303869d35b1f8](../../evidence/conditions-sets-016.md#c-29a303869d35b1f8) · [状态效果 S-28cb502006350bc6](../../evidence/state_effects-sets-009.md#s-28cb502006350bc6)

### path-062176

```text
(config)# do-exec show eigrp service-family ipv6 interfaces <interface> <cr>
```

Handler ` RVA 0xF5933F0 `；selector ` 89 `；EOL ` RVA 0x35478EC8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9e7c205576674437](../../evidence/conditions-sets-061.md#c-9e7c205576674437) · [缺口 G-e0aaa5f4b4157921](../../evidence/gaps-sets-008.md#g-e0aaa5f4b4157921) · [参数 P-7ced382f60145b6c](../../evidence/parameters-sets-010.md#p-7ced382f60145b6c) · [状态效果 S-28cb502006350bc6](../../evidence/state_effects-sets-009.md#s-28cb502006350bc6)

### path-050578

```text
(config)# do-exec show eigrp service-family ipv6 neighbors <cr>
```

Handler ` RVA 0xF5933F0 `；selector ` 90 `；EOL ` RVA 0x354789D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c9f09264998f3873](../../evidence/conditions-sets-078.md#c-c9f09264998f3873) · [状态效果 S-28cb502006350bc6](../../evidence/state_effects-sets-009.md#s-28cb502006350bc6)

### path-062179

```text
(config)# do-exec show eigrp service-family ipv6 neighbors <interface> <cr>
```

Handler ` RVA 0xF5933F0 `；selector ` 90 `；EOL ` RVA 0x354789D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3f522a3fff4e5d54](../../evidence/conditions-sets-025.md#c-3f522a3fff4e5d54) · [缺口 G-9a82b33ee1902649](../../evidence/gaps-sets-006.md#g-9a82b33ee1902649) · [参数 P-6cd124a9453c9e4d](../../evidence/parameters-sets-009.md#p-6cd124a9453c9e4d) · [状态效果 S-28cb502006350bc6](../../evidence/state_effects-sets-009.md#s-28cb502006350bc6)

### path-050599

```text
(config)# do-exec show eigrp service-family ipv6 sia-event <cr>
```

Handler ` RVA 0xF5933F0 `；selector ` 99 `；EOL ` RVA 0x3547A7D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ead7f0a21e659ac3](../../evidence/conditions-sets-091.md#c-ead7f0a21e659ac3) · [状态效果 S-97b9b3850eef38fe](../../evidence/state_effects-sets-032.md#s-97b9b3850eef38fe)

### path-050644

```text
(config)# do-exec show eigrp service-family ipv6 sia-statistics <cr>
```

Handler ` RVA 0xF5933F0 `；selector ` 99 `；EOL ` RVA 0x3547AB58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ead7f0a21e659ac3](../../evidence/conditions-sets-091.md#c-ead7f0a21e659ac3) · [状态效果 S-e5ac3c6c5034dd32](../../evidence/state_effects-sets-049.md#s-e5ac3c6c5034dd32)

### path-050685

```text
(config)# do-exec show eigrp service-family ipv6 subscriptions <cr>
```

Handler ` RVA 0xF5933F0 `；selector ` 117 `；EOL ` RVA 0x3547B628 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ead7f0a21e659ac3](../../evidence/conditions-sets-091.md#c-ead7f0a21e659ac3) · [状态效果 S-28cb502006350bc6](../../evidence/state_effects-sets-009.md#s-28cb502006350bc6)

### path-056172

```text
(config)# do-exec show eigrp service-family ipv6 subscriptions detail <cr>
```

Handler ` RVA 0xF5933F0 `；selector ` 118 `；EOL ` RVA 0x3547B600 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ead7f0a21e659ac3](../../evidence/conditions-sets-091.md#c-ead7f0a21e659ac3) · [状态效果 S-e01f9c896e3d586e](../../evidence/state_effects-sets-047.md#s-e01f9c896e3d586e)

### path-050504

```text
(config)# do-exec show eigrp service-family ipv6 timers <cr>
```

Handler ` RVA 0xF5933F0 `；selector ` 95 `；EOL ` RVA 0x35479198 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ead7f0a21e659ac3](../../evidence/conditions-sets-091.md#c-ead7f0a21e659ac3) · [状态效果 S-28cb502006350bc6](../../evidence/state_effects-sets-009.md#s-28cb502006350bc6)

### path-050745

```text
(config)# do-exec show eigrp service-family ipv6 topology <cr>
```

Handler ` RVA 0xF5933F0 `；selector ` 97 `；EOL ` RVA 0x35479A30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4431a42f8b169653](../../evidence/conditions-sets-027.md#c-4431a42f8b169653) · [状态效果 S-135f0d137f364250](../../evidence/state_effects-sets-005.md#s-135f0d137f364250)

### path-050525

```text
(config)# do-exec show eigrp service-family ipv6 traffic <cr>
```

Handler ` RVA 0xF5933F0 `；selector ` 96 `；EOL ` RVA 0x35479440 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ead7f0a21e659ac3](../../evidence/conditions-sets-091.md#c-ead7f0a21e659ac3) · [状态效果 S-28cb502006350bc6](../../evidence/state_effects-sets-009.md#s-28cb502006350bc6)

### path-032517

```text
(config)# do-exec show eigrp tech-support <cr>
```

Handler ` RVA 0xF590E10 `；selector ` 94 `；EOL ` RVA 0x3469D078 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1b4e8e153df9d5de](../../evidence/state_effects-sets-006.md#s-1b4e8e153df9d5de)

### path-026868

```text
(config)# do-exec show end-user-license-agreement <cr>
```

Handler ` RVA 0xE006D20 `；selector ` 0 `；EOL ` RVA 0x341635F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f0aca990aed40166](../../evidence/conditions-sets-093.md#c-f0aca990aed40166) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027656

```text
(config)# do-exec show endpoint-tracker <cr>
```

Handler ` RVA 0xC5A6530 `；selector ` 27 `；EOL ` RVA 0x33ABF350 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-09062bff53df9df4](../../evidence/conditions-sets-004.md#c-09062bff53df9df4) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-060724

```text
(config)# do-exec show endpoint-tracker <interface> <cr>
```

Handler ` RVA 0xC5A6530 `；selector ` 27 `；EOL ` RVA 0x33ABF350 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-30d8ab4aa1f1c11f](../../evidence/conditions-sets-019.md#c-30d8ab4aa1f1c11f) · [缺口 G-2a751e8e9bf65425](../../evidence/gaps-sets-002.md#g-2a751e8e9bf65425) · [参数 P-350130fe66e1b706](../../evidence/parameters-sets-005.md#p-350130fe66e1b706) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032111

```text
(config)# do-exec show endpoint-tracker dns-probe <cr>
```

Handler ` RVA 0xC5A9EA0 `；selector ` 36 `；EOL ` RVA 0x33ABDAE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032131

```text
(config)# do-exec show endpoint-tracker history <cr>
```

Handler ` RVA 0xC5AA7D0 `；selector ` 37 `；EOL ` RVA 0x33ABDD90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032218

```text
(config)# do-exec show endpoint-tracker records <cr>
```

Handler ` RVA 0xC5A7330 `；selector ` 28 `；EOL ` RVA 0x33ABED80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032185

```text
(config)# do-exec show endpoint-tracker sla-mode <cr>
```

Handler ` RVA 0xC5A9CC0 `；selector ` 31 `；EOL ` RVA 0x33ABE830 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032169

```text
(config)# do-exec show endpoint-tracker sla-profile <cr>
```

Handler ` RVA 0xC5A9B90 `；selector ` 32 `；EOL ` RVA 0x33ABE588 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032146

```text
(config)# do-exec show endpoint-tracker sla-statistics <cr>
```

Handler ` RVA 0xC5A9D70 `；selector ` 34 `；EOL ` RVA 0x33ABE038 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032157

```text
(config)# do-exec show endpoint-tracker sla-status <cr>
```

Handler ` RVA 0xC5A9A50 `；selector ` 33 `；EOL ` RVA 0x33ABE2E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032234

```text
(config)# do-exec show endpoint-tracker static-route <cr>
```

Handler ` RVA 0xC5A78F0 `；selector ` 29 `；EOL ` RVA 0x33ABF028 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032202

```text
(config)# do-exec show endpoint-tracker tracker-group <cr>
```

Handler ` RVA 0xC5A6D40 `；selector ` 30 `；EOL ` RVA 0x33ABEAD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027484

```text
(config)# do-exec show entry <cr>
```

Handler ` RVA 0xCCF7E20 `；selector ` 0 `；EOL ` RVA 0x33C66FE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027770

```text
(config)# do-exec show environment <cr>
```

Handler ` RVA 0xE123FA0 `；selector ` 6 `；EOL ` RVA 0x3420DDA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033533

```text
(config)# do-exec show environment all <cr>
```

Handler ` RVA 0xE123FA0 `；selector ` 1 `；EOL ` RVA 0x3420C320 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-051654

```text
(config)# do-exec show environment chassis <number:1..2> R0 <cr>
```

Handler ` RVA 0xE123FA0 `；selector ` 7 `；EOL ` RVA 0x3420D528 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Chassis num。

[条件 C-79c3049a72d744f7](../../evidence/conditions-sets-047.md#c-79c3049a72d744f7) · [参数 P-73bcd9c9b128d4ce](../../evidence/parameters-sets-009.md#p-73bcd9c9b128d4ce) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-051668

```text
(config)# do-exec show environment chassis active R0 <cr>
```

Handler ` RVA 0xE123FA0 `；selector ` 8 `；EOL ` RVA 0x3420D820 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-79c3049a72d744f7](../../evidence/conditions-sets-047.md#c-79c3049a72d744f7) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-051683

```text
(config)# do-exec show environment chassis standby R0 <cr>
```

Handler ` RVA 0xE123FA0 `；selector ` 9 `；EOL ` RVA 0x3420DAF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-79c3049a72d744f7](../../evidence/conditions-sets-047.md#c-79c3049a72d744f7) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033583

```text
(config)# do-exec show environment counters <cr>
```

Handler ` RVA 0xE123FA0 `；selector ` 0 `；EOL ` RVA 0x3420D168 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-043156

```text
(config)# do-exec show environment history <string> <cr>
```

Handler ` RVA 0xE123FA0 `；selector ` 5 `；EOL ` RVA 0x3420C630 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Sensor name。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-ce18fd8d61f2210a](../../evidence/parameters-sets-016.md#p-ce18fd8d61f2210a) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-043174

```text
(config)# do-exec show environment location <string> <cr>
```

Handler ` RVA 0xE123FA0 `；selector ` 2 `；EOL ` RVA 0x3420C918 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Sensor location。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-34f99b46609b4395](../../evidence/parameters-sets-005.md#p-34f99b46609b4395) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-043209

```text
(config)# do-exec show environment sensor <string> <cr>
```

Handler ` RVA 0xE123FA0 `；selector ` 3 `；EOL ` RVA 0x3420CEE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Sensor name。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-e500fd2af324ccc6](../../evidence/parameters-sets-017.md#p-e500fd2af324ccc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-043190

```text
(config)# do-exec show environment table <string> <cr>
```

Handler ` RVA 0xE123FA0 `；selector ` 4 `；EOL ` RVA 0x3420CC00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Sensor name。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-0d5137d84d11342e](../../evidence/parameters-sets-001.md#p-0d5137d84d11342e) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027345

```text
(config)# do-exec show eobc <cr>
```

Handler ` RVA 0xED89450 `；selector ` 0 `；EOL ` RVA 0x3442D800 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-030360

```text
(config)# do-exec show eobc controller <cr>
```

Handler ` RVA 0xED89360 `；selector ` 0 `；EOL ` RVA 0x3442D530 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-030378

```text
(config)# do-exec show eobc interface <cr>
```

Handler ` RVA 0xED893E0 `；selector ` 0 `；EOL ` RVA 0x3442D7D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033885

```text
(config)# do-exec show errdisable detect <cr>
```

Handler ` RVA 0x15DB4A10 `；selector ` 0 `；EOL ` RVA 0x35E2A248 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033888

```text
(config)# do-exec show errdisable flap-values <cr>
```

Handler ` RVA 0x15DB5090 `；selector ` 0 `；EOL ` RVA 0x35E2A4F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033882

```text
(config)# do-exec show errdisable recovery <cr>
```

Handler ` RVA 0x15DB3490 `；selector ` 0 `；EOL ` RVA 0x35E29FA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-030500

```text
(config)# do-exec show etherchannel load-balancing <cr>
```

Handler ` RVA 0xE9A0CE0 `；selector ` 0 `；EOL ` RVA 0x3436F970 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-030557

```text
(config)# do-exec show etherchannel summary <cr>
```

Handler ` RVA 0xE9A1660 `；selector ` 0 `；EOL ` RVA 0x3436FC58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b2367d4010600738](../../evidence/conditions-sets-069.md#c-b2367d4010600738) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-036753

```text
(config)# do-exec show ethernet cfm capabilities <cr>
```

Handler ` RVA 0xBDC0F40 `；selector ` 0 `；EOL ` RVA 0x338D7398 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6d96396d46ddc865](../../evidence/conditions-sets-042.md#c-6d96396d46ddc865) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061944

```text
(config)# do-exec show ethernet cfm capabilities interface <interface> <cr>
```

Handler ` RVA 0xBDC0F40 `；selector ` 0 `；EOL ` RVA 0x338D7398 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-22324969ecbe8db7](../../evidence/conditions-sets-013.md#c-22324969ecbe8db7) · [缺口 G-038539759b186c51](../../evidence/gaps-sets-001.md#g-038539759b186c51) · [参数 P-f6c32727ee4c4859](../../evidence/parameters-sets-018.md#p-f6c32727ee4c4859) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-037039

```text
(config)# do-exec show ethernet cfm ccm-learning-database <cr>
```

Handler ` RVA 0xBDC0EE0 `；selector ` 0 `；EOL ` RVA 0x338D87B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cbdf2ebd075c67b6](../../evidence/conditions-sets-078.md#c-cbdf2ebd075c67b6) · [状态效果 S-9ed8967132875423](../../evidence/state_effects-sets-034.md#s-9ed8967132875423)

### path-036757

```text
(config)# do-exec show ethernet cfm domain <cr>
```

Handler ` RVA 0xBDC1260 `；selector ` 0 `；EOL ` RVA 0x338D6B20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5cbd505584606c89](../../evidence/conditions-sets-036.md#c-5cbd505584606c89) · [状态效果 S-2e2997641e3ae12c](../../evidence/state_effects-sets-010.md#s-2e2997641e3ae12c)

### path-046077

```text
(config)# do-exec show ethernet cfm efd meps <cr>
```

Handler ` RVA 0xBDC2620 `；selector ` 0 `；EOL ` RVA 0x338D7968 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8613b4c0471e9c39](../../evidence/conditions-sets-052.md#c-8613b4c0471e9c39) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-036572

```text
(config)# do-exec show ethernet cfm errors <cr>
```

Handler ` RVA 0xBDC2670 `；selector ` 0 `；EOL ` RVA 0x338D4028 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-70b01ddd58a3b7eb](../../evidence/conditions-sets-044.md#c-70b01ddd58a3b7eb) · [状态效果 S-b5b706d96d5165e3](../../evidence/state_effects-sets-038.md#s-b5b706d96d5165e3)

### path-045908

```text
(config)# do-exec show ethernet cfm errors configuration <cr>
```

Handler ` RVA 0xBDC2880 `；selector ` 0 `；EOL ` RVA 0x338D48E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-70b01ddd58a3b7eb](../../evidence/conditions-sets-044.md#c-70b01ddd58a3b7eb) · [状态效果 S-b5b706d96d5165e3](../../evidence/state_effects-sets-038.md#s-b5b706d96d5165e3)

### path-053639

```text
(config)# do-exec show ethernet cfm fast-timeout database interfaces <cr>
```

Handler ` RVA 0xBDC11C0 `；selector ` 0 `；EOL ` RVA 0x338D8070 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-946843844715746e](../../evidence/conditions-sets-057.md#c-946843844715746e) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-053689

```text
(config)# do-exec show ethernet cfm fast-timeout database remote-meps <cr>
```

Handler ` RVA 0xBDC1150 `；selector ` 0 `；EOL ` RVA 0x338D7DD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-416d16b16cefe156](../../evidence/conditions-sets-026.md#c-416d16b16cefe156) · [状态效果 S-170813d0bd5aeabf](../../evidence/state_effects-sets-005.md#s-170813d0bd5aeabf)

### path-046219

```text
(config)# do-exec show ethernet cfm fast-timeout statistics <cr>
```

Handler ` RVA 0xBDC1210 `；selector ` 0 `；EOL ` RVA 0x338D8308 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ecf0419a46ecb11d](../../evidence/conditions-sets-092.md#c-ecf0419a46ecb11d) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-053665

```text
(config)# do-exec show ethernet cfm internal counters packet <cr>
```

Handler ` RVA 0xBDC0E80 `；selector ` 0 `；EOL ` RVA 0x338DDA58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-53df3aaa02d65428](../../evidence/conditions-sets-033.md#c-53df3aaa02d65428) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-053978

```text
(config)# do-exec show ethernet cfm internal database crosscheck-meps <cr>
```

Handler ` RVA 0xBDC0210 `；selector ` 0 `；EOL ` RVA 0x338DB488 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-733fa51cb7067c49](../../evidence/conditions-sets-045.md#c-733fa51cb7067c49) · [状态效果 S-ddf1876e4e54d18c](../../evidence/state_effects-sets-047.md#s-ddf1876e4e54d18c)

### path-053832

```text
(config)# do-exec show ethernet cfm internal database domains <cr>
```

Handler ` RVA 0xBDBF840 `；selector ` 0 `；EOL ` RVA 0x338D8E00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-aee2331596f48bbd](../../evidence/conditions-sets-068.md#c-aee2331596f48bbd) · [状态效果 S-052a74b78c3962e9](../../evidence/state_effects-sets-002.md#s-052a74b78c3962e9)

### path-054122

```text
(config)# do-exec show ethernet cfm internal database interfaces <cr>
```

Handler ` RVA 0xBDC0510 `；selector ` 0 `；EOL ` RVA 0x338DC0F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-888fcbc2b9a4236e](../../evidence/conditions-sets-053.md#c-888fcbc2b9a4236e) · [状态效果 S-171a713224436342](../../evidence/state_effects-sets-005.md#s-171a713224436342)

### path-062330

```text
(config)# do-exec show ethernet cfm internal database interfaces <interface> <cr>
```

Handler ` RVA 0xBDC0510 `；selector ` 0 `；EOL ` RVA 0x338DC0F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ec53146e8dc9b08a](../../evidence/conditions-sets-091.md#c-ec53146e8dc9b08a) · [缺口 G-2b7b942b9befc75f](../../evidence/gaps-sets-002.md#g-2b7b942b9befc75f) · [参数 P-49a2015198be64aa](../../evidence/parameters-sets-006.md#p-49a2015198be64aa) · [状态效果 S-171a713224436342](../../evidence/state_effects-sets-005.md#s-171a713224436342)

### path-054174

```text
(config)# do-exec show ethernet cfm internal database mac-learning <cr>
```

Handler ` RVA 0xBDC07D0 `；selector ` 0 `；EOL ` RVA 0x338DCD80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bba2fae2c6c1ae2d](../../evidence/conditions-sets-072.md#c-bba2fae2c6c1ae2d) · [状态效果 S-5ea78549c9f43e56](../../evidence/state_effects-sets-020.md#s-5ea78549c9f43e56)

### path-054057

```text
(config)# do-exec show ethernet cfm internal database meps <cr>
```

Handler ` RVA 0xBDBFA10 `；selector ` 0 `；EOL ` RVA 0x338D98D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-204bcf6d3d015c52](../../evidence/conditions-sets-013.md#c-204bcf6d3d015c52) · [状态效果 S-faebcbefa1cc19ee](../../evidence/state_effects-sets-053.md#s-faebcbefa1cc19ee)

### path-062520

```text
(config)# do-exec show ethernet cfm internal database meps interface <interface> <cr>
```

Handler ` RVA 0xBDBFA10 `；selector ` 0 `；EOL ` RVA 0x338D98D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3c4f6f1105fc9c9a](../../evidence/conditions-sets-023.md#c-3c4f6f1105fc9c9a) · [缺口 G-61c19237189fc8c1](../../evidence/gaps-sets-004.md#g-61c19237189fc8c1) · [参数 P-353ce7ff200f64d2](../../evidence/parameters-sets-005.md#p-353ce7ff200f64d2) · [状态效果 S-faebcbefa1cc19ee](../../evidence/state_effects-sets-053.md#s-faebcbefa1cc19ee)

### path-053874

```text
(config)# do-exec show ethernet cfm internal database mips <cr>
```

Handler ` RVA 0xBDBFCF0 `；selector ` 0 `；EOL ` RVA 0x338DA230 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e3d73dd0039e4df1](../../evidence/conditions-sets-088.md#c-e3d73dd0039e4df1) · [状态效果 S-b5a3960bee5e6c5d](../../evidence/state_effects-sets-038.md#s-b5a3960bee5e6c5d)

### path-062519

```text
(config)# do-exec show ethernet cfm internal database mips interface <interface> <cr>
```

Handler ` RVA 0xBDBFCF0 `；selector ` 0 `；EOL ` RVA 0x338DA230 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a9c1967363d79d7d](../../evidence/conditions-sets-065.md#c-a9c1967363d79d7d) · [缺口 G-1d214c612ef784f1](../../evidence/gaps-sets-001.md#g-1d214c612ef784f1) · [参数 P-adb1a3992605d29d](../../evidence/parameters-sets-013.md#p-adb1a3992605d29d) · [状态效果 S-b5a3960bee5e6c5d](../../evidence/state_effects-sets-038.md#s-b5a3960bee5e6c5d)

### path-057835

```text
(config)# do-exec show ethernet cfm internal database oir-config crosscheck-meps <cr>
```

Handler ` RVA 0xBDC0E20 `；selector ` 0 `；EOL ` RVA 0x338DD6F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0d00a590e5da3d27](../../evidence/conditions-sets-005.md#c-0d00a590e5da3d27) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-057803

```text
(config)# do-exec show ethernet cfm internal database oir-config interfaces <cr>
```

Handler ` RVA 0xBDC0D60 `；selector ` 0 `；EOL ` RVA 0x338DD1A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3743eb651560762e](../../evidence/conditions-sets-021.md#c-3743eb651560762e) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-057823

```text
(config)# do-exec show ethernet cfm internal database oir-config meps <cr>
```

Handler ` RVA 0xBDC0DC0 `；selector ` 0 `；EOL ` RVA 0x338DD448 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-397d7473249a3ae9](../../evidence/conditions-sets-022.md#c-397d7473249a3ae9) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-054149

```text
(config)# do-exec show ethernet cfm internal database ports <cr>
```

Handler ` RVA 0xBDC0730 `；selector ` 0 `；EOL ` RVA 0x338DC7A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d530e3671eb895bb](../../evidence/conditions-sets-082.md#c-d530e3671eb895bb) · [状态效果 S-ef1c7abf744647dc](../../evidence/state_effects-sets-051.md#s-ef1c7abf744647dc)

### path-062327

```text
(config)# do-exec show ethernet cfm internal database ports <interface> <cr>
```

Handler ` RVA 0xBDC0730 `；selector ` 0 `；EOL ` RVA 0x338DC7A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1c7433e5e992a011](../../evidence/conditions-sets-011.md#c-1c7433e5e992a011) · [缺口 G-682b101b9b5db695](../../evidence/gaps-sets-004.md#g-682b101b9b5db695) · [参数 P-2d61ed78ac0ddd22](../../evidence/parameters-sets-004.md#p-2d61ed78ac0ddd22) · [状态效果 S-ef1c7abf744647dc](../../evidence/state_effects-sets-051.md#s-ef1c7abf744647dc)

### path-054105

```text
(config)# do-exec show ethernet cfm internal database remote-meps <cr>
```

Handler ` RVA 0xBDBFF00 `；selector ` 0 `；EOL ` RVA 0x338DAA50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2756b041ec1b66f7](../../evidence/conditions-sets-015.md#c-2756b041ec1b66f7) · [状态效果 S-160434b289019d69](../../evidence/state_effects-sets-005.md#s-160434b289019d69)

### path-062522

```text
(config)# do-exec show ethernet cfm internal database remote-meps interface <interface> <cr>
```

Handler ` RVA 0xBDBFF00 `；selector ` 0 `；EOL ` RVA 0x338DAA50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8bf67e7b0ba928f6](../../evidence/conditions-sets-054.md#c-8bf67e7b0ba928f6) · [缺口 G-8191c4c1c07c9338](../../evidence/gaps-sets-005.md#g-8191c4c1c07c9338) · [参数 P-5888ed602cfe3afd](../../evidence/parameters-sets-007.md#p-5888ed602cfe3afd) · [状态效果 S-160434b289019d69](../../evidence/state_effects-sets-005.md#s-160434b289019d69)

### path-053875

```text
(config)# do-exec show ethernet cfm internal database services <cr>
```

Handler ` RVA 0xBDBF900 `；selector ` 0 `；EOL ` RVA 0x338D9250 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f236371c034c3c9f](../../evidence/conditions-sets-094.md#c-f236371c034c3c9f) · [状态效果 S-eb5b99c11b919c31](../../evidence/state_effects-sets-050.md#s-eb5b99c11b919c31)

### path-054104

```text
(config)# do-exec show ethernet cfm internal database transports <cr>
```

Handler ` RVA 0xBDC0330 `；selector ` 0 `；EOL ` RVA 0x338DBB40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-44d017a2bf7efcbb](../../evidence/conditions-sets-027.md#c-44d017a2bf7efcbb) · [状态效果 S-4dcc5dc14fc4f02a](../../evidence/state_effects-sets-017.md#s-4dcc5dc14fc4f02a)

### path-061356

```text
(config)# do-exec show ethernet cfm latching-loopback active <cr>
```

Handler ` RVA 0xBDC25A0 `；selector ` 2 `；EOL ` RVA 0x338D5A48 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-70b01ddd58a3b7eb](../../evidence/conditions-sets-044.md#c-70b01ddd58a3b7eb) · [缺口 G-5e306bbbda5d3580](../../evidence/gaps-sets-004.md#g-5e306bbbda5d3580) · [状态效果 S-8618b4f87598a476](../../evidence/state_effects-sets-028.md#s-8618b4f87598a476)

### path-061937

```text
(config)# do-exec show ethernet cfm latching-loopback active brief <cr>
```

Handler ` RVA 0xBDC25A0 `；selector ` 3 `；EOL ` RVA 0x338D5EF0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-70b01ddd58a3b7eb](../../evidence/conditions-sets-044.md#c-70b01ddd58a3b7eb) · [缺口 G-5e306bbbda5d3580](../../evidence/gaps-sets-004.md#g-5e306bbbda5d3580) · [状态效果 S-8618b4f87598a476](../../evidence/state_effects-sets-028.md#s-8618b4f87598a476)

### path-062310

```text
(config)# do-exec show ethernet cfm latching-loopback discover-phase mip detail <cr>
```

Handler ` RVA 0xBDC1300 `；selector ` 0 `；EOL ` RVA 0x338D66C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5a181c4829245aec](../../evidence/conditions-sets-035.md#c-5a181c4829245aec) · [缺口 G-5e306bbbda5d3580](../../evidence/gaps-sets-004.md#g-5e306bbbda5d3580) · [状态效果 S-8454809027a63a7d](../../evidence/state_effects-sets-028.md#s-8454809027a63a7d)

### path-045737

```text
(config)# do-exec show ethernet cfm maintenance-points database <cr>
```

Handler ` RVA 0xBDC2F30 `；selector ` 0 `；EOL ` RVA 0x338D27D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-70b01ddd58a3b7eb](../../evidence/conditions-sets-044.md#c-70b01ddd58a3b7eb) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-046028

```text
(config)# do-exec show ethernet cfm maintenance-points local <cr>
```

Handler ` RVA 0xBDC28D0 `；selector ` 0 `；EOL ` RVA 0x338CFFB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-93722996e3645ec3](../../evidence/conditions-sets-057.md#c-93722996e3645ec3) · [状态效果 S-701fbe17cc1b9960](../../evidence/state_effects-sets-024.md#s-701fbe17cc1b9960)

### path-062287

```text
(config)# do-exec show ethernet cfm maintenance-points local interface <interface> <cr>
```

Handler ` RVA 0xBDC28D0 `；selector ` 0 `；EOL ` RVA 0x338CFFB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-87898f035429929c](../../evidence/conditions-sets-052.md#c-87898f035429929c) · [缺口 G-20c8ebf1f6e6df32](../../evidence/gaps-sets-002.md#g-20c8ebf1f6e6df32) · [参数 P-bc5aace83a4b1617](../../evidence/parameters-sets-014.md#p-bc5aace83a4b1617) · [状态效果 S-26ae1f9d4dd1df07](../../evidence/state_effects-sets-009.md#s-26ae1f9d4dd1df07)

### path-045937

```text
(config)# do-exec show ethernet cfm maintenance-points remote <cr>
```

Handler ` RVA 0xBDC2AC0 `；selector ` 0 `；EOL ` RVA 0x338D2020 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-70b01ddd58a3b7eb](../../evidence/conditions-sets-044.md#c-70b01ddd58a3b7eb) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-053437

```text
(config)# do-exec show ethernet cfm maintenance-points remote crosscheck <cr>
```

Handler ` RVA 0xBDC2FB0 `；selector ` 0 `；EOL ` RVA 0x338D0C50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0666404166ded403](../../evidence/conditions-sets-003.md#c-0666404166ded403) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-053391

```text
(config)# do-exec show ethernet cfm maintenance-points remote detail <cr>
```

Handler ` RVA 0xBDC2C30 `；selector ` 0 `；EOL ` RVA 0x338D17A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-70b01ddd58a3b7eb](../../evidence/conditions-sets-044.md#c-70b01ddd58a3b7eb) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-036391

```text
(config)# do-exec show ethernet cfm mpdb <cr>
```

Handler ` RVA 0xBDC3200 `；selector ` 0 `；EOL ` RVA 0x338D2B48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-70b01ddd58a3b7eb](../../evidence/conditions-sets-044.md#c-70b01ddd58a3b7eb) · [状态效果 S-838fa5c57564fcc0](../../evidence/state_effects-sets-028.md#s-838fa5c57564fcc0)

### path-036389

```text
(config)# do-exec show ethernet cfm pm <cr>
```

Handler ` RVA 0xBE8C040 `；selector ` 0 `；EOL ` RVA 0x339147F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-70b01ddd58a3b7eb](../../evidence/conditions-sets-044.md#c-70b01ddd58a3b7eb) · [状态效果 S-f6cdf22730a0d8fc](../../evidence/state_effects-sets-052.md#s-f6cdf22730a0d8fc)

### path-053346

```text
(config)# do-exec show ethernet cfm pm slm responder <cr>
```

Handler ` RVA 0xBE89820 `；selector ` 0 `；EOL ` RVA 0x33918A10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b5898665a3cc58f8](../../evidence/conditions-sets-070.md#c-b5898665a3cc58f8) · [状态效果 S-aa1a0f8972e5dbaa](../../evidence/state_effects-sets-036.md#s-aa1a0f8972e5dbaa)

### path-036702

```text
(config)# do-exec show ethernet cfm smep <cr>
```

Handler ` RVA 0xBDC3410 `；selector ` 0 `；EOL ` RVA 0x338D6F20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-896b9c01781e73e9](../../evidence/conditions-sets-053.md#c-896b9c01781e73e9) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061935

```text
(config)# do-exec show ethernet cfm smep interface <interface> <cr>
```

Handler ` RVA 0xBDC3410 `；selector ` 0 `；EOL ` RVA 0x338D6F20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6f0e31932fa2889b](../../evidence/conditions-sets-043.md#c-6f0e31932fa2889b) · [缺口 G-001311749bd97615](../../evidence/gaps-sets-001.md#g-001311749bd97615) · [参数 P-f8159be330e7d46a](../../evidence/parameters-sets-018.md#p-f8159be330e7d46a) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-036449

```text
(config)# do-exec show ethernet cfm statistics <cr>
```

Handler ` RVA 0xBDC3470 `；selector ` 0 `；EOL ` RVA 0x338D35F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-70b01ddd58a3b7eb](../../evidence/conditions-sets-044.md#c-70b01ddd58a3b7eb) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-036717

```text
(config)# do-exec show ethernet cfm traceroute-cache <cr>
```

Handler ` RVA 0xBDC35A0 `；selector ` 0 `；EOL ` RVA 0x338D4E30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-70b01ddd58a3b7eb](../../evidence/conditions-sets-044.md#c-70b01ddd58a3b7eb) · [状态效果 S-741de3cc301cc57f](../../evidence/state_effects-sets-025.md#s-741de3cc301cc57f)

### path-030724

```text
(config)# do-exec show ethernet dot1ad <cr>
```

Handler ` RVA 0xBF8E150 `；selector ` 1 `；EOL ` RVA 0x33961590 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-b0a0931305be1889](../../evidence/state_effects-sets-037.md#s-b0a0931305be1889)

### path-061419

```text
(config)# do-exec show ethernet dot1ad interface <interface> <cr>
```

Handler ` RVA 0xBF8E150 `；selector ` 1 `；EOL ` RVA 0x33961590 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e654361ce1e1efb5](../../evidence/conditions-sets-089.md#c-e654361ce1e1efb5) · [缺口 G-2c55892879ea608a](../../evidence/gaps-sets-002.md#g-2c55892879ea608a) · [参数 P-1bfa747fcc17f82e](../../evidence/parameters-sets-003.md#p-1bfa747fcc17f82e) · [状态效果 S-b0a0931305be1889](../../evidence/state_effects-sets-037.md#s-b0a0931305be1889)

### path-061316

```text
(config)# do-exec show ethernet l2ctrl interface <interface> <cr>
```

Handler ` RVA 0xC04E930 `；selector ` 2 `；EOL ` RVA 0x3398AA58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0ef6a654af2b0dd8](../../evidence/conditions-sets-006.md#c-0ef6a654af2b0dd8) · [缺口 G-11255cb358b3c528](../../evidence/gaps-sets-001.md#g-11255cb358b3c528) · [参数 P-049a860be02bf81c](../../evidence/parameters-sets-001.md#p-049a860be02bf81c) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-036193

```text
(config)# do-exec show ethernet l2ctrl vlan <cr>
```

Handler ` RVA 0xC04E930 `；selector ` 1 `；EOL ` RVA 0x3398A710 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-24c0dad1952bb99d](../../evidence/conditions-sets-014.md#c-24c0dad1952bb99d) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-036268

```text
(config)# do-exec show ethernet lmi evc <cr>
```

Handler ` RVA 0xBEC2E40 `；selector ` 0 `；EOL ` RVA 0x339213A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-70b01ddd58a3b7eb](../../evidence/conditions-sets-044.md#c-70b01ddd58a3b7eb) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-045696

```text
(config)# do-exec show ethernet lmi evc detail <cr>
```

Handler ` RVA 0xBEC2E40 `；selector ` 1 `；EOL ` RVA 0x33921418 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-70b01ddd58a3b7eb](../../evidence/conditions-sets-044.md#c-70b01ddd58a3b7eb) · [状态效果 S-6c58d9570bd3bc6b](../../evidence/state_effects-sets-023.md#s-6c58d9570bd3bc6b)

### path-062492

```text
(config)# do-exec show ethernet lmi evc detail <string> interface <interface> <cr>
```

Handler ` RVA 0xBEC2E40 `；selector ` 1 `；EOL ` RVA 0x33921418 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` EVC Identifier。

[条件 C-e332595b1f364e99](../../evidence/conditions-sets-087.md#c-e332595b1f364e99) · [缺口 G-2203a0f83630db55](../../evidence/gaps-sets-002.md#g-2203a0f83630db55) · [参数 P-347d783099093b3a](../../evidence/parameters-sets-004.md#p-347d783099093b3a) · [状态效果 S-0e46efc131836259](../../evidence/state_effects-sets-003.md#s-0e46efc131836259)

### path-062277

```text
(config)# do-exec show ethernet lmi evc map interface <interface> <cr>
```

Handler ` RVA 0xBEC2E40 `；selector ` 2 `；EOL ` RVA 0x339210A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1eaba8e95b02b816](../../evidence/conditions-sets-012.md#c-1eaba8e95b02b816) · [缺口 G-0e56181244ceea4d](../../evidence/gaps-sets-001.md#g-0e56181244ceea4d) · [参数 P-6898eadf318d1234](../../evidence/parameters-sets-008.md#p-6898eadf318d1234) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-036122

```text
(config)# do-exec show ethernet lmi parameters <cr>
```

Handler ` RVA 0xBEC2E40 `；selector ` 4 `；EOL ` RVA 0x33920BB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-70b01ddd58a3b7eb](../../evidence/conditions-sets-044.md#c-70b01ddd58a3b7eb) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061898

```text
(config)# do-exec show ethernet lmi parameters interface <interface> <cr>
```

Handler ` RVA 0xBEC2E40 `；selector ` 4 `；EOL ` RVA 0x33920BB0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-00f7a760a046703a](../../evidence/conditions-sets-001.md#c-00f7a760a046703a) · [缺口 G-d480e3fa63099f00](../../evidence/gaps-sets-007.md#g-d480e3fa63099f00) · [参数 P-206523d2a4b640af](../../evidence/parameters-sets-003.md#p-206523d2a4b640af) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-036039

```text
(config)# do-exec show ethernet lmi statistics <cr>
```

Handler ` RVA 0xBEC2E40 `；selector ` 3 `；EOL ` RVA 0x339207B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-70b01ddd58a3b7eb](../../evidence/conditions-sets-044.md#c-70b01ddd58a3b7eb) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061894

```text
(config)# do-exec show ethernet lmi statistics interface <interface> <cr>
```

Handler ` RVA 0xBEC2E40 `；selector ` 3 `；EOL ` RVA 0x339207B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-34810b6c9cc4514c](../../evidence/conditions-sets-020.md#c-34810b6c9cc4514c) · [缺口 G-b499a66417770a3a](../../evidence/gaps-sets-006.md#g-b499a66417770a3a) · [参数 P-40073317d50b5707](../../evidence/parameters-sets-005.md#p-40073317d50b5707) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-045693

```text
(config)# do-exec show ethernet lmi uni map <cr>
```

Handler ` RVA 0xBEC2E40 `；selector ` 5 `；EOL ` RVA 0x33921AF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-70b01ddd58a3b7eb](../../evidence/conditions-sets-044.md#c-70b01ddd58a3b7eb) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062279

```text
(config)# do-exec show ethernet lmi uni map interface <interface> <cr>
```

Handler ` RVA 0xBEC2E40 `；selector ` 5 `；EOL ` RVA 0x33921AF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7dadf2baea21a645](../../evidence/conditions-sets-049.md#c-7dadf2baea21a645) · [缺口 G-81e10baad8b34115](../../evidence/gaps-sets-005.md#g-81e10baad8b34115) · [参数 P-1d00e9783cdb20cb](../../evidence/parameters-sets-003.md#p-1d00e9783cdb20cb) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-060877

```text
(config)# do-exec show ethernet loopback active <cr>
```

Handler ` RVA 0xBF14BF0 `；selector ` 2 `；EOL ` RVA 0x3393CF70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-70b01ddd58a3b7eb](../../evidence/conditions-sets-044.md#c-70b01ddd58a3b7eb) · [缺口 G-43249c2c6a7d72ef](../../evidence/gaps-sets-003.md#g-43249c2c6a7d72ef) · [状态效果 S-ddf209326ec84e24](../../evidence/state_effects-sets-047.md#s-ddf209326ec84e24)

### path-061352

```text
(config)# do-exec show ethernet loopback active brief <cr>
```

Handler ` RVA 0xBF14BF0 `；selector ` 3 `；EOL ` RVA 0x3393D418 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-70b01ddd58a3b7eb](../../evidence/conditions-sets-044.md#c-70b01ddd58a3b7eb) · [缺口 G-43249c2c6a7d72ef](../../evidence/gaps-sets-003.md#g-43249c2c6a7d72ef) · [状态效果 S-ddf209326ec84e24](../../evidence/state_effects-sets-047.md#s-ddf209326ec84e24)

### path-060873

```text
(config)# do-exec show ethernet loopback permitted <cr>
```

Handler ` RVA 0xBF14BF0 `；selector ` 1 `；EOL ` RVA 0x3393C818 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-70b01ddd58a3b7eb](../../evidence/conditions-sets-044.md#c-70b01ddd58a3b7eb) · [缺口 G-43249c2c6a7d72ef](../../evidence/gaps-sets-003.md#g-43249c2c6a7d72ef) · [状态效果 S-ddf209326ec84e24](../../evidence/state_effects-sets-047.md#s-ddf209326ec84e24)

### path-062096

```text
(config)# do-exec show ethernet mac-tunnel engine slot <number:dynamic> <cr>
```

Handler ` RVA 0xC030740 `；selector ` 0 `；EOL ` RVA 0x33981FD8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Slot Number。

[条件 C-97187b7adb9b7cb2](../../evidence/conditions-sets-058.md#c-97187b7adb9b7cb2) · [缺口 G-5a07ac50f0881fd2](../../evidence/gaps-sets-004.md#g-5a07ac50f0881fd2) · [参数 P-3f1904db53c599a1](../../evidence/parameters-sets-005.md#p-3f1904db53c599a1) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-045972

```text
(config)# do-exec show ethernet oam debug link-monitor <cr>
```

Handler ` RVA 0xBF08810 `；selector ` 0 `；EOL ` RVA 0x33939A60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-df830d30e85f7b07](../../evidence/conditions-sets-086.md#c-df830d30e85f7b07) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062290

```text
(config)# do-exec show ethernet oam debug link-monitor interface <interface> <cr>
```

Handler ` RVA 0xBF08810 `；selector ` 1 `；EOL ` RVA 0x33939B20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-93ccbdf8cab86fc1](../../evidence/conditions-sets-057.md#c-93ccbdf8cab86fc1) · [缺口 G-7a6eff62c1479f73](../../evidence/gaps-sets-005.md#g-7a6eff62c1479f73) · [参数 P-77964409e1d7369e](../../evidence/parameters-sets-009.md#p-77964409e1d7369e) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-045952

```text
(config)# do-exec show ethernet oam debug loopback <cr>
```

Handler ` RVA 0xBF08810 `；selector ` 2 `；EOL ` RVA 0x3393A030 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f54b22ece38b6a4b](../../evidence/conditions-sets-095.md#c-f54b22ece38b6a4b) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-036120

```text
(config)# do-exec show ethernet oam discovery <cr>
```

Handler ` RVA 0xBEEB290 `；selector ` 36 `；EOL ` RVA 0x3392DD70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-70b01ddd58a3b7eb](../../evidence/conditions-sets-044.md#c-70b01ddd58a3b7eb) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061896

```text
(config)# do-exec show ethernet oam discovery interface <interface> <cr>
```

Handler ` RVA 0xBEEB290 `；selector ` 40 `；EOL ` RVA 0x3392DE30 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-289cbae0e666fa44](../../evidence/conditions-sets-016.md#c-289cbae0e666fa44) · [缺口 G-9be5097bbd8bf132](../../evidence/gaps-sets-006.md#g-9be5097bbd8bf132) · [参数 P-50efcd8942ed7a62](../../evidence/parameters-sets-007.md#p-50efcd8942ed7a62) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-036194

```text
(config)# do-exec show ethernet oam runtime <cr>
```

Handler ` RVA 0xBEEB290 `；selector ` 41 `；EOL ` RVA 0x3392E3D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-70b01ddd58a3b7eb](../../evidence/conditions-sets-044.md#c-70b01ddd58a3b7eb) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061901

```text
(config)# do-exec show ethernet oam runtime interface <interface> <cr>
```

Handler ` RVA 0xBEEB290 `；selector ` 41 `；EOL ` RVA 0x3392E3D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9076afb1caa7bf46](../../evidence/conditions-sets-056.md#c-9076afb1caa7bf46) · [缺口 G-0388fb4ff5ea5073](../../evidence/gaps-sets-001.md#g-0388fb4ff5ea5073) · [参数 P-ffaf53db0ab2d75d](../../evidence/parameters-sets-019.md#p-ffaf53db0ab2d75d) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-036328

```text
(config)# do-exec show ethernet oam statistics <cr>
```

Handler ` RVA 0xBEEB290 `；selector ` 38 `；EOL ` RVA 0x3392EE28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-70b01ddd58a3b7eb](../../evidence/conditions-sets-044.md#c-70b01ddd58a3b7eb) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061910

```text
(config)# do-exec show ethernet oam statistics interface <interface> <cr>
```

Handler ` RVA 0xBEEB290 `；selector ` 43 `；EOL ` RVA 0x3392EEE8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-309d8ebc5ec2f55e](../../evidence/conditions-sets-019.md#c-309d8ebc5ec2f55e) · [缺口 G-0178c3799d0e28bb](../../evidence/gaps-sets-001.md#g-0178c3799d0e28bb) · [参数 P-01361675886b7880](../../evidence/parameters-sets-001.md#p-01361675886b7880) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-036260

```text
(config)# do-exec show ethernet oam status <cr>
```

Handler ` RVA 0xBEEB290 `；selector ` 37 `；EOL ` RVA 0x3392E7C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-70b01ddd58a3b7eb](../../evidence/conditions-sets-044.md#c-70b01ddd58a3b7eb) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061903

```text
(config)# do-exec show ethernet oam status interface <interface> <cr>
```

Handler ` RVA 0xBEEB290 `；selector ` 42 `；EOL ` RVA 0x3392E888 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-687061bf653f6d53](../../evidence/conditions-sets-040.md#c-687061bf653f6d53) · [缺口 G-f09602c775954e7c](../../evidence/gaps-sets-008.md#g-f09602c775954e7c) · [参数 P-5aa4b77c87f784e1](../../evidence/parameters-sets-007.md#p-5aa4b77c87f784e1) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-036305

```text
(config)# do-exec show ethernet oam summary <cr>
```

Handler ` RVA 0xBEEB290 `；selector ` 39 `；EOL ` RVA 0x3392F3F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-70b01ddd58a3b7eb](../../evidence/conditions-sets-044.md#c-70b01ddd58a3b7eb) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040599

```text
(config)# do-exec show ethernet service evc <cr>
```

Handler ` RVA 0xC0168D0 `；selector ` 3 `；EOL ` RVA 0x33977F60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2a85c37c554a9490](../../evidence/conditions-sets-017.md#c-2a85c37c554a9490) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062122

```text
(config)# do-exec show ethernet service evc interface <interface> <cr>
```

Handler ` RVA 0xC0168D0 `；selector ` 3 `；EOL ` RVA 0x33977F60 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3d758caf9ece674b](../../evidence/conditions-sets-024.md#c-3d758caf9ece674b) · [缺口 G-cb8d102aebff2d3a](../../evidence/gaps-sets-007.md#g-cb8d102aebff2d3a) · [参数 P-80009a0507e41827](../../evidence/parameters-sets-010.md#p-80009a0507e41827) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040762

```text
(config)# do-exec show ethernet service instance <cr>
```

Handler ` RVA 0xC0168D0 `；selector ` 2 `；EOL ` RVA 0x33977BB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062139

```text
(config)# do-exec show ethernet service instance interface <interface> <cr>
```

Handler ` RVA 0xC0168D0 `；selector ` 2 `；EOL ` RVA 0x33977BB0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c071d692b783c826](../../evidence/conditions-sets-074.md#c-c071d692b783c826) · [缺口 G-0ae60460cb2b3cf8](../../evidence/gaps-sets-001.md#g-0ae60460cb2b3cf8) · [参数 P-6f8291695ce3680c](../../evidence/parameters-sets-009.md#p-6f8291695ce3680c) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-049655

```text
(config)# do-exec show ethernet service instance policy-map <cr>
```

Handler ` RVA 0xC0168D0 `；selector ` 4 `；EOL ` RVA 0x33978430 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040656

```text
(config)# do-exec show ethernet service interface <cr>
```

Handler ` RVA 0xC0168D0 `；selector ` 1 `；EOL ` RVA 0x33978E60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-feda29a644eb6a81](../../evidence/conditions-sets-098.md#c-feda29a644eb6a81) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061627

```text
(config)# do-exec show ethernet service interface <interface> <cr>
```

Handler ` RVA 0xC0168D0 `；selector ` 1 `；EOL ` RVA 0x33978E60 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-54376f7288bdee08](../../evidence/conditions-sets-033.md#c-54376f7288bdee08) · [缺口 G-fd2f23028f9f936d](../../evidence/gaps-sets-009.md#g-fd2f23028f9f936d) · [参数 P-bdd091389843ce1e](../../evidence/parameters-sets-014.md#p-bdd091389843ce1e) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-049814

```text
(config)# do-exec show ethernet service internal back-trace <cr>
```

Handler ` RVA 0xC013940 `；selector ` 0 `；EOL ` RVA 0x3397C868 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-c3685fae562099bd](../../evidence/state_effects-sets-041.md#s-c3685fae562099bd)

### path-055711

```text
(config)# do-exec show ethernet service internal db global <cr>
```

Handler ` RVA 0xC01CEE0 `；selector ` 0 `；EOL ` RVA 0x3397D6B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fb50b6ea9e8d1e7a](../../evidence/conditions-sets-097.md#c-fb50b6ea9e8d1e7a) · [状态效果 S-ccc40f60cbbd47a7](../../evidence/state_effects-sets-043.md#s-ccc40f60cbbd47a7)

### path-062555

```text
(config)# do-exec show ethernet service internal db pcb interface <interface> <cr>
```

Handler ` RVA 0xC01CEE0 `；selector ` 0 `；EOL ` RVA 0x3397D6B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-39b28960c22dc330](../../evidence/conditions-sets-022.md#c-39b28960c22dc330) · [缺口 G-c1d517615716af6c](../../evidence/gaps-sets-007.md#g-c1d517615716af6c) · [参数 P-99639bde4bc009ef](../../evidence/parameters-sets-012.md#p-99639bde4bc009ef) · [状态效果 S-451a6743a369efba](../../evidence/state_effects-sets-015.md#s-451a6743a369efba)

### path-058521

```text
(config)# do-exec show ethernet service internal db vport all <cr>
```

Handler ` RVA 0xC04E8E0 `；selector ` 0 `；EOL ` RVA 0x3398A2F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7543f123c7e68a61](../../evidence/conditions-sets-046.md#c-7543f123c7e68a61) · [状态效果 S-ce8ab8df47306669](../../evidence/state_effects-sets-044.md#s-ce8ab8df47306669)

### path-049774

```text
(config)# do-exec show ethernet service ipc statistics <cr>
```

Handler ` RVA 0xBF93B20 `；selector ` 0 `；EOL ` RVA 0x33962998 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061622

```text
(config)# do-exec show ethernet service mac-tunnel <number:dynamic> <cr>
```

Handler ` RVA 0xC0168D0 `；selector ` 5 `；EOL ` RVA 0x33979248 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Mac-in-Mac tunnel identifier。

[条件 C-8fc24dcedca3e130](../../evidence/conditions-sets-056.md#c-8fc24dcedca3e130) · [缺口 G-d330e9b69db34716](../../evidence/gaps-sets-007.md#g-d330e9b69db34716) · [参数 P-05bae0806d9085ee](../../evidence/parameters-sets-001.md#p-05bae0806d9085ee) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-049777

```text
(config)# do-exec show ethernet service mac-tunnel summary <cr>
```

Handler ` RVA 0xC0168D0 `；selector ` 5 `；EOL ` RVA 0x33979248 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-93c9b7aa13aa92fa](../../evidence/state_effects-sets-031.md#s-93c9b7aa13aa92fa)

### path-061805

```text
(config)# do-exec show event manager detector all <cr>
```

Handler ` RVA 0xC0CC4F0 `；selector ` 0 `；EOL ` RVA 0x339A5050 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [缺口 G-38f8217294a82e87](../../evidence/gaps-sets-002.md#g-38f8217294a82e87) · [状态效果 S-17b1e71ae69d3147](../../evidence/state_effects-sets-005.md#s-17b1e71ae69d3147)

### path-061812

```text
(config)# do-exec show event manager detector application <cr>
```

Handler ` RVA 0x110D87D0 `；selector ` 0 `；EOL ` RVA 0x353AAC48 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [缺口 G-c18d7bad9161ee7e](../../evidence/gaps-sets-007.md#g-c18d7bad9161ee7e) · [状态效果 S-7cbf4ff11468a9ff](../../evidence/state_effects-sets-026.md#s-7cbf4ff11468a9ff)

### path-061830

```text
(config)# do-exec show event manager detector cli <cr>
```

Handler ` RVA 0x110822C0 `；selector ` 0 `；EOL ` RVA 0x35388888 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [缺口 G-d42a0b344f6f294e](../../evidence/gaps-sets-007.md#g-d42a0b344f6f294e) · [状态效果 S-1ee7cee6c56c3777](../../evidence/state_effects-sets-007.md#s-1ee7cee6c56c3777)

### path-061833

```text
(config)# do-exec show event manager detector config <cr>
```

Handler ` RVA 0xC094EA0 `；selector ` 0 `；EOL ` RVA 0x339957E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [缺口 G-913bb5cf67e76ea2](../../evidence/gaps-sets-005.md#g-913bb5cf67e76ea2) · [状态效果 S-1607e4bbe4de0654](../../evidence/state_effects-sets-005.md#s-1607e4bbe4de0654)

### path-061829

```text
(config)# do-exec show event manager detector counter <cr>
```

Handler ` RVA 0x1108E5B0 `；selector ` 0 `；EOL ` RVA 0x3538C818 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [缺口 G-713abd94bb21a055](../../evidence/gaps-sets-004.md#g-713abd94bb21a055) · [状态效果 S-5e6680a3b2d6167d](../../evidence/state_effects-sets-020.md#s-5e6680a3b2d6167d)

### path-061832

```text
(config)# do-exec show event manager detector env <cr>
```

Handler ` RVA 0xC096B50 `；selector ` 0 `；EOL ` RVA 0x33996CC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [缺口 G-27eff722969de97c](../../evidence/gaps-sets-002.md#g-27eff722969de97c) · [状态效果 S-f7e81c13b29c5eaa](../../evidence/state_effects-sets-052.md#s-f7e81c13b29c5eaa)

### path-061816

```text
(config)# do-exec show event manager detector generic <cr>
```

Handler ` RVA 0x110CDF60 `；selector ` 0 `；EOL ` RVA 0x353A5FB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [缺口 G-292d8d7870cf1742](../../evidence/gaps-sets-002.md#g-292d8d7870cf1742) · [状态效果 S-454321adb2dc8412](../../evidence/state_effects-sets-015.md#s-454321adb2dc8412)

### path-061831

```text
(config)# do-exec show event manager detector gold <cr>
```

Handler ` RVA 0xC09F8F0 `；selector ` 0 `；EOL ` RVA 0x33999AA8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-eae195d3129a832d](../../evidence/conditions-sets-091.md#c-eae195d3129a832d) · [缺口 G-23f409e29bbea8a8](../../evidence/gaps-sets-002.md#g-23f409e29bbea8a8) · [状态效果 S-e8d130c6426f8487](../../evidence/state_effects-sets-049.md#s-e8d130c6426f8487)

### path-061828

```text
(config)# do-exec show event manager detector interface <cr>
```

Handler ` RVA 0x11095F70 `；selector ` 0 `；EOL ` RVA 0x35390270 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [缺口 G-14cd99241be7ad00](../../evidence/gaps-sets-001.md#g-14cd99241be7ad00) · [状态效果 S-5287f542b818ab2c](../../evidence/state_effects-sets-018.md#s-5287f542b818ab2c)

### path-061827

```text
(config)# do-exec show event manager detector ioswdsysmon <cr>
```

Handler ` RVA 0x110A1AA0 `；selector ` 0 `；EOL ` RVA 0x35393ED8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [缺口 G-011e3e8a396ce4b9](../../evidence/gaps-sets-001.md#g-011e3e8a396ce4b9) · [状态效果 S-324aeb1737eeb841](../../evidence/state_effects-sets-011.md#s-324aeb1737eeb841)

### path-061810

```text
(config)# do-exec show event manager detector mat <cr>
```

Handler ` RVA 0x110E4660 `；selector ` 0 `；EOL ` RVA 0x353B01A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [缺口 G-8437e9050e1b6d39](../../evidence/gaps-sets-005.md#g-8437e9050e1b6d39) · [状态效果 S-fbf6cff7a0a1e9a3](../../evidence/state_effects-sets-053.md#s-fbf6cff7a0a1e9a3)

### path-061809

```text
(config)# do-exec show event manager detector neighbor-discovery <cr>
```

Handler ` RVA 0x110EDCB0 `；selector ` 0 `；EOL ` RVA 0x353B2818 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [缺口 G-93a2f766fde371dc](../../evidence/gaps-sets-005.md#g-93a2f766fde371dc) · [状态效果 S-f25d60626c9896c4](../../evidence/state_effects-sets-051.md#s-f25d60626c9896c4)

### path-061815

```text
(config)# do-exec show event manager detector nhrp <cr>
```

Handler ` RVA 0x110D1860 `；selector ` 0 `；EOL ` RVA 0x353A7D80 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [缺口 G-5b3f80cfed3ea0fc](../../evidence/gaps-sets-004.md#g-5b3f80cfed3ea0fc) · [状态效果 S-853ae5cd47da8b31](../../evidence/state_effects-sets-028.md#s-853ae5cd47da8b31)

### path-061826

```text
(config)# do-exec show event manager detector none <cr>
```

Handler ` RVA 0x110A54A0 `；selector ` 0 `；EOL ` RVA 0x35396A18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [缺口 G-32e9d773c0e5bf84](../../evidence/gaps-sets-002.md#g-32e9d773c0e5bf84) · [状态效果 S-59bb9051bffd00fc](../../evidence/state_effects-sets-019.md#s-59bb9051bffd00fc)

### path-061825

```text
(config)# do-exec show event manager detector oir <cr>
```

Handler ` RVA 0x110A75A0 `；selector ` 0 `；EOL ` RVA 0x353988B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [缺口 G-0fc0cf68062f9f7c](../../evidence/gaps-sets-001.md#g-0fc0cf68062f9f7c) · [状态效果 S-4894ad03af9eb456](../../evidence/state_effects-sets-016.md#s-4894ad03af9eb456)

### path-061808

```text
(config)# do-exec show event manager detector resource <cr>
```

Handler ` RVA 0x11202F20 `；selector ` 0 `；EOL ` RVA 0x35416F18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [缺口 G-5fa56bb5aa65898d](../../evidence/gaps-sets-004.md#g-5fa56bb5aa65898d) · [状态效果 S-19513c349f227f5a](../../evidence/state_effects-sets-006.md#s-19513c349f227f5a)

### path-061824

```text
(config)# do-exec show event manager detector rf <cr>
```

Handler ` RVA 0x110AA040 `；selector ` 0 `；EOL ` RVA 0x3539A258 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ba389bfbc5c6d001](../../evidence/conditions-sets-072.md#c-ba389bfbc5c6d001) · [缺口 G-b20dda2e6cf7d348](../../evidence/gaps-sets-006.md#g-b20dda2e6cf7d348) · [状态效果 S-47a2323bc3b6fc5f](../../evidence/state_effects-sets-016.md#s-47a2323bc3b6fc5f)

### path-061811

```text
(config)# do-exec show event manager detector routing <cr>
```

Handler ` RVA 0x110DF400 `；selector ` 0 `；EOL ` RVA 0x353AD7E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [缺口 G-55f68c49f83dcc94](../../evidence/gaps-sets-003.md#g-55f68c49f83dcc94) · [状态效果 S-4ec7ef755953dbf2](../../evidence/state_effects-sets-017.md#s-4ec7ef755953dbf2)

### path-061806

```text
(config)# do-exec show event manager detector rpc <cr>
```

Handler ` RVA 0xC0A2C50 `；selector ` 0 `；EOL ` RVA 0x3399BB28 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ea3b24ac9cf68f1d](../../evidence/conditions-sets-090.md#c-ea3b24ac9cf68f1d) · [缺口 G-e05ac841a766aca1](../../evidence/gaps-sets-008.md#g-e05ac841a766aca1) · [状态效果 S-b53b1181f13379a6](../../evidence/state_effects-sets-038.md#s-b53b1181f13379a6)

### path-062229

```text
(config)# do-exec show event manager detector rpc counters <cr>
```

Handler ` RVA 0xC0A2A20 `；selector ` 0 `；EOL ` RVA 0x3399C0D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ea3b24ac9cf68f1d](../../evidence/conditions-sets-090.md#c-ea3b24ac9cf68f1d) · [缺口 G-e05ac841a766aca1](../../evidence/gaps-sets-008.md#g-e05ac841a766aca1) · [状态效果 S-b53b1181f13379a6](../../evidence/state_effects-sets-038.md#s-b53b1181f13379a6)

### path-062228

```text
(config)# do-exec show event manager detector rpc session <cr>
```

Handler ` RVA 0xC0A2BF0 `；selector ` 0 `；EOL ` RVA 0x3399BE30 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ea3b24ac9cf68f1d](../../evidence/conditions-sets-090.md#c-ea3b24ac9cf68f1d) · [缺口 G-e05ac841a766aca1](../../evidence/gaps-sets-008.md#g-e05ac841a766aca1) · [状态效果 S-b53b1181f13379a6](../../evidence/state_effects-sets-038.md#s-b53b1181f13379a6)

### path-061823

```text
(config)# do-exec show event manager detector snmp <cr>
```

Handler ` RVA 0x110B4990 `；selector ` 0 `；EOL ` RVA 0x3539CDF0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [缺口 G-6972c740b1dd518c](../../evidence/gaps-sets-004.md#g-6972c740b1dd518c) · [状态效果 S-e2c5ba68614bcfea](../../evidence/state_effects-sets-048.md#s-e2c5ba68614bcfea)

### path-061820

```text
(config)# do-exec show event manager detector snmp-notification <cr>
```

Handler ` RVA 0x110C4790 `；selector ` 0 `；EOL ` RVA 0x353A1F78 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [缺口 G-511c8aea009e2f9f](../../evidence/gaps-sets-003.md#g-511c8aea009e2f9f) · [状态效果 S-24fec018b719d53b](../../evidence/state_effects-sets-008.md#s-24fec018b719d53b)

### path-061821

```text
(config)# do-exec show event manager detector snmp-object <cr>
```

Handler ` RVA 0x110BBDA0 `；selector ` 0 `；EOL ` RVA 0x3539F8F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [缺口 G-e21966ec58a9d4db](../../evidence/gaps-sets-008.md#g-e21966ec58a9d4db) · [状态效果 S-28bed1baa9ef39e3](../../evidence/state_effects-sets-009.md#s-28bed1baa9ef39e3)

### path-061818

```text
(config)# do-exec show event manager detector syslog <cr>
```

Handler ` RVA 0x110CABC0 `；selector ` 0 `；EOL ` RVA 0x353A4798 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [缺口 G-9c5bb42ed92aab36](../../evidence/gaps-sets-006.md#g-9c5bb42ed92aab36) · [状态效果 S-9b402009697f3a72](../../evidence/state_effects-sets-033.md#s-9b402009697f3a72)

### path-061834

```text
(config)# do-exec show event manager detector test <cr>
```

Handler ` RVA 0xC092E70 `；selector ` 0 `；EOL ` RVA 0x33994618 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [缺口 G-4b3ecff271f76f3d](../../evidence/gaps-sets-003.md#g-4b3ecff271f76f3d) · [状态效果 S-946e1c507a5c097d](../../evidence/state_effects-sets-031.md#s-946e1c507a5c097d)

### path-061814

```text
(config)# do-exec show event manager detector timer <cr>
```

Handler ` RVA 0x110D8120 `；selector ` 0 `；EOL ` RVA 0x353A9A10 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [缺口 G-07416cce222cc98a](../../evidence/gaps-sets-001.md#g-07416cce222cc98a) · [状态效果 S-93d5153ef96095ec](../../evidence/state_effects-sets-031.md#s-93d5153ef96095ec)

### path-061807

```text
(config)# do-exec show event manager detector track <cr>
```

Handler ` RVA 0x112061E0 `；selector ` 0 `；EOL ` RVA 0x35418E50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [缺口 G-3c276b918fbf145d](../../evidence/gaps-sets-003.md#g-3c276b918fbf145d) · [状态效果 S-c1b99721a9df2a0f](../../evidence/state_effects-sets-041.md#s-c1b99721a9df2a0f)

### path-056729

```text
(config)# do-exec show event manager directory user policy <cr>
```

Handler ` RVA 0xC0CC5D0 `；selector ` 0 `；EOL ` RVA 0x339A3EC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-a67a47341c38dcce](../../evidence/state_effects-sets-035.md#s-a67a47341c38dcce)

### path-043712

```text
(config)# do-exec show event manager environment <cr>
```

Handler ` RVA 0xC0CC640 `；selector ` 0 `；EOL ` RVA 0x339A3BA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-051995

```text
(config)# do-exec show event manager history events <cr>
```

Handler ` RVA 0xC0CC800 `；selector ` 0 `；EOL ` RVA 0x339A4670 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-f8b8993dabca9b4f](../../evidence/state_effects-sets-053.md#s-f8b8993dabca9b4f)

### path-062459

```text
(config)# do-exec show event manager history events maximum <number:dynamic> <cr>
```

Handler ` RVA 0xC0CC800 `；selector ` 0 `；EOL ` RVA 0x339A4670 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Maximum entries。

[条件 C-441f2671a7fc9158](../../evidence/conditions-sets-027.md#c-441f2671a7fc9158) · [缺口 G-8212eb4e829d00b1](../../evidence/gaps-sets-005.md#g-8212eb4e829d00b1) · [参数 P-7ca9e9d7e7f11953](../../evidence/parameters-sets-010.md#p-7ca9e9d7e7f11953) · [状态效果 S-c9ee10bf04360387](../../evidence/state_effects-sets-043.md#s-c9ee10bf04360387)

