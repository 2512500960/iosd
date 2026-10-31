# configure · 六个基础模式的历史连接

[模式索引](README.md) · [总索引](../../README.md)

### path-031969

```text
(config)# do-exec show ipv6 route <cr>
```

Handler ` RVA 0x1230A670 `；selector ` 0 `；EOL ` RVA 0x357E8B18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-66452b223b70afee](../../evidence/conditions-sets-039.md#c-66452b223b70afee) · [状态效果 S-f40691c6467a238a](../../evidence/state_effects-sets-052.md#s-f40691c6467a238a)

### path-061553

```text
(config)# do-exec show ipv6 route interface <interface> <cr>
```

Handler ` RVA 0x1230A670 `；selector ` 0 `；EOL ` RVA 0x357EAAF0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4b2b024d722dead7](../../evidence/conditions-sets-029.md#c-4b2b024d722dead7) · [缺口 G-7c537eefa5359b97](../../evidence/gaps-sets-005.md#g-7c537eefa5359b97) · [参数 P-72f91cdc047fd03b](../../evidence/parameters-sets-009.md#p-72f91cdc047fd03b) · [状态效果 S-d6ec84118db6b34f](../../evidence/state_effects-sets-046.md#s-d6ec84118db6b34f)

### path-061005

```text
(config)# do-exec show ipv6 route multicast <cr>
```

Handler ` RVA 0x1230A670 `；selector ` 0 `；EOL ` RVA 0x357E8B18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-66452b223b70afee](../../evidence/conditions-sets-039.md#c-66452b223b70afee) · [缺口 G-a2cbbd8135b6f598](../../evidence/gaps-sets-006.md#g-a2cbbd8135b6f598) · [状态效果 S-fc8ae9c92c41e012](../../evidence/state_effects-sets-053.md#s-fc8ae9c92c41e012)

### path-061538

```text
(config)# do-exec show ipv6 route multicast nsf <cr>
```

Handler ` RVA 0x1230A670 `；selector ` 0 `；EOL ` RVA 0x357EA488 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-66452b223b70afee](../../evidence/conditions-sets-039.md#c-66452b223b70afee) · [缺口 G-a2cbbd8135b6f598](../../evidence/gaps-sets-006.md#g-a2cbbd8135b6f598) · [状态效果 S-35358e756aa2135f](../../evidence/state_effects-sets-012.md#s-35358e756aa2135f)

### path-061541

```text
(config)# do-exec show ipv6 route multicast summary <cr>
```

Handler ` RVA 0x1230A670 `；selector ` 0 `；EOL ` RVA 0x357EA1E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-66452b223b70afee](../../evidence/conditions-sets-039.md#c-66452b223b70afee) · [缺口 G-a2cbbd8135b6f598](../../evidence/gaps-sets-006.md#g-a2cbbd8135b6f598) · [状态效果 S-056a209e516410b5](../../evidence/state_effects-sets-002.md#s-056a209e516410b5)

### path-061533

```text
(config)# do-exec show ipv6 route multicast table <cr>
```

Handler ` RVA 0x1230A240 `；selector ` 0 `；EOL ` RVA 0x357E9DE8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [缺口 G-a2cbbd8135b6f598](../../evidence/gaps-sets-006.md#g-a2cbbd8135b6f598) · [状态效果 S-fc8ae9c92c41e012](../../evidence/state_effects-sets-053.md#s-fc8ae9c92c41e012)

### path-062059

```text
(config)# do-exec show ipv6 route multicast table <number:0..4294967295> <cr>
```

Handler ` RVA 0x1230A670 `；selector ` 0 `；EOL ` RVA 0x357E9B38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Table id (hex)。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [缺口 G-a2cbbd8135b6f598](../../evidence/gaps-sets-006.md#g-a2cbbd8135b6f598) · [参数 P-c8a0d4a105edec77](../../evidence/parameters-sets-015.md#p-c8a0d4a105edec77) · [状态效果 S-fc8ae9c92c41e012](../../evidence/state_effects-sets-053.md#s-fc8ae9c92c41e012)

### path-062082

```text
(config)# do-exec show ipv6 route multicast tag <number:0..4294967295> <cr>
```

Handler ` RVA 0x1230A670 `；selector ` 0 `；EOL ` RVA 0x357F2C48 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Tag value。

[条件 C-66452b223b70afee](../../evidence/conditions-sets-039.md#c-66452b223b70afee) · [缺口 G-a2cbbd8135b6f598](../../evidence/gaps-sets-006.md#g-a2cbbd8135b6f598) · [参数 P-49e39b5d6941be33](../../evidence/parameters-sets-006.md#p-49e39b5d6941be33) · [状态效果 S-58cd44b644f205b7](../../evidence/state_effects-sets-019.md#s-58cd44b644f205b7)

### path-061545

```text
(config)# do-exec show ipv6 route multicast watch <cr>
```

Handler ` RVA 0x1230A670 `；selector ` 0 `；EOL ` RVA 0x357EA740 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-66452b223b70afee](../../evidence/conditions-sets-039.md#c-66452b223b70afee) · [缺口 G-a2cbbd8135b6f598](../../evidence/gaps-sets-006.md#g-a2cbbd8135b6f598) · [状态效果 S-7ba1c66d26e18149](../../evidence/state_effects-sets-026.md#s-7ba1c66d26e18149)

### path-039851

```text
(config)# do-exec show ipv6 route nsf <cr>
```

Handler ` RVA 0x1230A670 `；selector ` 0 `；EOL ` RVA 0x357EA488 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-66452b223b70afee](../../evidence/conditions-sets-039.md#c-66452b223b70afee) · [状态效果 S-78aa8e00d31af142](../../evidence/state_effects-sets-026.md#s-78aa8e00d31af142)

### path-039868

```text
(config)# do-exec show ipv6 route summary <cr>
```

Handler ` RVA 0x1230A670 `；selector ` 0 `；EOL ` RVA 0x357EA1E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-66452b223b70afee](../../evidence/conditions-sets-039.md#c-66452b223b70afee) · [状态效果 S-5e53a3387d7f4bf9](../../evidence/state_effects-sets-020.md#s-5e53a3387d7f4bf9)

### path-039767

```text
(config)# do-exec show ipv6 route table <cr>
```

Handler ` RVA 0x1230A240 `；selector ` 0 `；EOL ` RVA 0x357E9DE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-f40691c6467a238a](../../evidence/state_effects-sets-052.md#s-f40691c6467a238a)

### path-048583

```text
(config)# do-exec show ipv6 route table <number:0..4294967295> <cr>
```

Handler ` RVA 0x1230A670 `；selector ` 0 `；EOL ` RVA 0x357E9B38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Table id (hex)。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-c8a0d4a105edec77](../../evidence/parameters-sets-015.md#p-c8a0d4a105edec77) · [状态效果 S-f40691c6467a238a](../../evidence/state_effects-sets-052.md#s-f40691c6467a238a)

### path-049165

```text
(config)# do-exec show ipv6 route tag <number:0..4294967295> <cr>
```

Handler ` RVA 0x1230A670 `；selector ` 0 `；EOL ` RVA 0x357F2C48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Tag value。

[条件 C-66452b223b70afee](../../evidence/conditions-sets-039.md#c-66452b223b70afee) · [参数 P-49e39b5d6941be33](../../evidence/parameters-sets-006.md#p-49e39b5d6941be33) · [状态效果 S-ac756640ccacda9a](../../evidence/state_effects-sets-036.md#s-ac756640ccacda9a)

### path-039905

```text
(config)# do-exec show ipv6 route watch <cr>
```

Handler ` RVA 0x1230A670 `；selector ` 0 `；EOL ` RVA 0x357EA740 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-66452b223b70afee](../../evidence/conditions-sets-039.md#c-66452b223b70afee) · [状态效果 S-87579f743536be4f](../../evidence/state_effects-sets-029.md#s-87579f743536be4f)

### path-031880

```text
(config)# do-exec show ipv6 routers <cr>
```

Handler ` RVA 0x12312D70 `；selector ` 0 `；EOL ` RVA 0x357FA910 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-18ad31c32cf5c72f](../../evidence/conditions-sets-010.md#c-18ad31c32cf5c72f) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-060997

```text
(config)# do-exec show ipv6 routers <interface> <cr>
```

Handler ` RVA 0x12312D70 `；selector ` 0 `；EOL ` RVA 0x357FA910 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c21b87cc0af08b6d](../../evidence/conditions-sets-075.md#c-c21b87cc0af08b6d) · [缺口 G-57972797f16c9176](../../evidence/gaps-sets-004.md#g-57972797f16c9176) · [参数 P-626059d4e05be74e](../../evidence/parameters-sets-008.md#p-626059d4e05be74e) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040694

```text
(config)# do-exec show ipv6 rpf <address> <cr>
```

Handler ` RVA 0x118E47F0 `；selector ` 0 `；EOL ` RVA 0x35538420 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` RP/Source address。

[条件 C-b78447efd0cd37f2](../../evidence/conditions-sets-071.md#c-b78447efd0cd37f2) · [参数 P-45778e765de8f2c0](../../evidence/parameters-sets-006.md#p-45778e765de8f2c0) · [状态效果 S-7a03cbb7a91b6e60](../../evidence/state_effects-sets-026.md#s-7a03cbb7a91b6e60)

### path-040616

```text
(config)# do-exec show ipv6 rpf select <cr>
```

Handler ` RVA 0x118E47F0 `；selector ` 1 `；EOL ` RVA 0x355380F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e3c5271c8e891e8a](../../evidence/conditions-sets-088.md#c-e3c5271c8e891e8a) · [状态效果 S-7a03cbb7a91b6e60](../../evidence/state_effects-sets-026.md#s-7a03cbb7a91b6e60)

### path-062982

```text
(config)# do-exec show ipv6 snooping capture-policy bd <number:dynamic> <cr>
```

Handler ` RVA 0x13688090 `；selector ` 1043 `；EOL ` RVA 0x35BEE0B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Bridge-domain number。

[条件 C-bf17ca33de8df17a](../../evidence/conditions-sets-074.md#c-bf17ca33de8df17a) · [缺口 G-645338896b1f7df3](../../evidence/gaps-sets-004.md#g-645338896b1f7df3) · [参数 P-8a4c8fa6fd4c88b5](../../evidence/parameters-sets-011.md#p-8a4c8fa6fd4c88b5) · [状态效果 S-d2e53f23300671b0](../../evidence/state_effects-sets-045.md#s-d2e53f23300671b0)

### path-062981

```text
(config)# do-exec show ipv6 snooping counters bd <number:dynamic> <cr>
```

Handler ` RVA 0x13688090 `；selector ` 1044 `；EOL ` RVA 0x35BEDB18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Bridge-domain number。

[条件 C-73ddbb17ee617feb](../../evidence/conditions-sets-045.md#c-73ddbb17ee617feb) · [缺口 G-7d4eb9ffb7d69854](../../evidence/gaps-sets-005.md#g-7d4eb9ffb7d69854) · [参数 P-3b9082e9e85b7c94](../../evidence/parameters-sets-005.md#p-3b9082e9e85b7c94) · [状态效果 S-0758536ed7477c16](../../evidence/state_effects-sets-002.md#s-0758536ed7477c16)

### path-040502

```text
(config)# do-exec show ipv6 snooping events <cr>
```

Handler ` RVA 0x13688090 `；selector ` 1046 `；EOL ` RVA 0x35BED058 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7ab22d2ab288c2e2](../../evidence/conditions-sets-048.md#c-7ab22d2ab288c2e2) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040559

```text
(config)# do-exec show ipv6 snooping features <cr>
```

Handler ` RVA 0x13688090 `；selector ` 1045 `；EOL ` RVA 0x35BED640 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7ab22d2ab288c2e2](../../evidence/conditions-sets-048.md#c-7ab22d2ab288c2e2) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062422

```text
(config)# do-exec show ipv6 snooping internal access-list interface <interface> <cr>
```

Handler ` RVA 0x13688090 `；selector ` 1041 `；EOL ` RVA 0x35BEEF80 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b7f2fd5e564067b7](../../evidence/conditions-sets-071.md#c-b7f2fd5e564067b7) · [缺口 G-1a33376769b2afc5](../../evidence/gaps-sets-001.md#g-1a33376769b2afc5) · [参数 P-f36250a0072309b8](../../evidence/parameters-sets-018.md#p-f36250a0072309b8) · [状态效果 S-5588ee7ab75654b0](../../evidence/state_effects-sets-019.md#s-5588ee7ab75654b0)

### path-049841

```text
(config)# do-exec show ipv6 snooping internal counters <cr>
```

Handler ` RVA 0x13688090 `；selector ` 1040 `；EOL ` RVA 0x35BEEBA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ef2a3a067495f7eb](../../evidence/conditions-sets-092.md#c-ef2a3a067495f7eb) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040565

```text
(config)# do-exec show ipv6 snooping messages <cr>
```

Handler ` RVA 0x13688090 `；selector ` 1047 `；EOL ` RVA 0x35BED390 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7ab22d2ab288c2e2](../../evidence/conditions-sets-048.md#c-7ab22d2ab288c2e2) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062983

```text
(config)# do-exec show ipv6 snooping policies bd <number:dynamic> <cr>
```

Handler ` RVA 0x13688090 `；selector ` 1042 `；EOL ` RVA 0x35BEE7B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Bridge-domain number。

[条件 C-9c6cc754555cd7a2](../../evidence/conditions-sets-060.md#c-9c6cc754555cd7a2) · [缺口 G-574799d07bf7ca1f](../../evidence/gaps-sets-004.md#g-574799d07bf7ca1f) · [参数 P-de55dd4fc12c6a87](../../evidence/parameters-sets-017.md#p-de55dd4fc12c6a87) · [状态效果 S-5b3c4c45ca5d6fa9](../../evidence/state_effects-sets-020.md#s-5b3c4c45ca5d6fa9)

### path-040566

```text
(config)# do-exec show ipv6 snooping policy <cr>
```

Handler ` RVA 0x1368B750 `；selector ` 0 `；EOL ` RVA 0x35BCC410 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d267542fdef8a630](../../evidence/conditions-sets-081.md#c-d267542fdef8a630) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040453

```text
(config)# do-exec show ipv6 source-guard policy <cr>
```

Handler ` RVA 0x136C03A0 `；selector ` 0 `；EOL ` RVA 0x35C08A38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032090

```text
(config)# do-exec show ipv6 spd <cr>
```

Handler ` RVA 0x12328600 `；selector ` 0 `；EOL ` RVA 0x358101A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061003

```text
(config)# do-exec show ipv6 static <?match_ipv6_pfxinfo_action@55558ad3fdb8> <cr>
```

Handler ` RVA 0x1230F810 `；selector ` 0 `；EOL ` RVA 0x357EBA98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-02b6dd4d1e9387d6](../../evidence/conditions-sets-002.md#c-02b6dd4d1e9387d6) · [缺口 G-c4ce9b0a3578f244](../../evidence/gaps-sets-007.md#g-c4ce9b0a3578f244) · [状态效果 S-d967d45ab495b72f](../../evidence/state_effects-sets-046.md#s-d967d45ab495b72f)

### path-031931

```text
(config)# do-exec show ipv6 static <cr>
```

Handler ` RVA 0x1230F810 `；selector ` 0 `；EOL ` RVA 0x357EBA98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9eacbd15ca85776f](../../evidence/conditions-sets-061.md#c-9eacbd15ca85776f) · [状态效果 S-d967d45ab495b72f](../../evidence/state_effects-sets-046.md#s-d967d45ab495b72f)

### path-039921

```text
(config)# do-exec show ipv6 static bfd <cr>
```

Handler ` RVA 0x12310780 `；selector ` 0 `；EOL ` RVA 0x357EB4A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-d967d45ab495b72f](../../evidence/state_effects-sets-046.md#s-d967d45ab495b72f)

### path-061547

```text
(config)# do-exec show ipv6 static multicast bfd <cr>
```

Handler ` RVA 0x12310780 `；selector ` 0 `；EOL ` RVA 0x357EB4A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [缺口 G-66db1908cb612aa8](../../evidence/gaps-sets-004.md#g-66db1908cb612aa8) · [状态效果 S-5709aef4d43f0a0e](../../evidence/state_effects-sets-019.md#s-5709aef4d43f0a0e)

### path-031768

```text
(config)# do-exec show ipv6 traffic <cr>
```

Handler ` RVA 0x1231EF70 `；selector ` 0 `；EOL ` RVA 0x3580B3D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-039766

```text
(config)# do-exec show ipv6 traffic interface <cr>
```

Handler ` RVA 0x1231EF70 `；selector ` 1 `；EOL ` RVA 0x3580B490 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a6b479c710d40bac](../../evidence/conditions-sets-064.md#c-a6b479c710d40bac) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061529

```text
(config)# do-exec show ipv6 traffic interface <interface> <cr>
```

Handler ` RVA 0x1231EF70 `；selector ` 1 `；EOL ` RVA 0x3580B490 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9eb170e7b6f205ea](../../evidence/conditions-sets-061.md#c-9eb170e7b6f205ea) · [缺口 G-fb672dd6354a3daa](../../evidence/gaps-sets-009.md#g-fb672dd6354a3daa) · [参数 P-c3153726aeadeceb](../../evidence/parameters-sets-015.md#p-c3153726aeadeceb) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031810

```text
(config)# do-exec show ipv6 tunnel <cr>
```

Handler ` RVA 0x12321E20 `；selector ` 0 `；EOL ` RVA 0x3580EC48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-8be99ac9c87c4830](../../evidence/state_effects-sets-030.md#s-8be99ac9c87c4830)

### path-032107

```text
(config)# do-exec show ipv6 virtual-reassembly <cr>
```

Handler ` RVA 0xC78A5E0 `；selector ` 0 `；EOL ` RVA 0x33AE9230 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e8906e5b95f3a5ac](../../evidence/conditions-sets-090.md#c-e8906e5b95f3a5ac) · [状态效果 S-afd506d493e31c93](../../evidence/state_effects-sets-037.md#s-afd506d493e31c93)

### path-062852

```text
(config)# do-exec show isdn <?test_int_action@55558ce1c950> <?test_int_action@55558ce1dd80> call-rate <cr>
```

Handler ` RVA 0x1E0319F0 `；selector ` 8 `；EOL ` RVA 0x378CA770 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0ad74d0466c90e80](../../evidence/conditions-sets-005.md#c-0ad74d0466c90e80) · [缺口 G-1c0ea94d2418f038](../../evidence/gaps-sets-001.md#g-1c0ea94d2418f038) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062891

```text
(config)# do-exec show isdn <?test_int_action@55558ce1c950> <?test_int_action@55558ce1dd80> variables statistics <cr>
```

Handler ` RVA 0x1E0319F0 `；selector ` 7 `；EOL ` RVA 0x378CA210 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0ad74d0466c90e80](../../evidence/conditions-sets-005.md#c-0ad74d0466c90e80) · [缺口 G-1c0ea94d2418f038](../../evidence/gaps-sets-001.md#g-1c0ea94d2418f038) · [状态效果 S-120b0cfaf17c9351](../../evidence/state_effects-sets-004.md#s-120b0cfaf17c9351)

### path-061168

```text
(config)# do-exec show isdn <?test_int_action@55558ce1c950> active <cr>
```

Handler ` RVA 0x1E0319F0 `；selector ` 5 `；EOL ` RVA 0x378C9DD0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8f156108be02a6cc](../../evidence/conditions-sets-055.md#c-8f156108be02a6cc) · [缺口 G-4fe0ddbfc26b9408](../../evidence/gaps-sets-003.md#g-4fe0ddbfc26b9408) · [状态效果 S-bc7df97381d3478f](../../evidence/state_effects-sets-040.md#s-bc7df97381d3478f)

### path-061166

```text
(config)# do-exec show isdn <?test_int_action@55558ce1c950> history <cr>
```

Handler ` RVA 0x1E0319F0 `；selector ` 4 `；EOL ` RVA 0x378C99D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a84cec78f6a311b7](../../evidence/conditions-sets-065.md#c-a84cec78f6a311b7) · [缺口 G-4fe0ddbfc26b9408](../../evidence/gaps-sets-003.md#g-4fe0ddbfc26b9408) · [状态效果 S-288c2a37ef28b8a5](../../evidence/state_effects-sets-009.md#s-288c2a37ef28b8a5)

### path-061161

```text
(config)# do-exec show isdn <?test_int_action@55558ce1c950> memory <cr>
```

Handler ` RVA 0x1E0319F0 `；selector ` 1 `；EOL ` RVA 0x378C8E00 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0ad74d0466c90e80](../../evidence/conditions-sets-005.md#c-0ad74d0466c90e80) · [缺口 G-4fe0ddbfc26b9408](../../evidence/gaps-sets-003.md#g-4fe0ddbfc26b9408) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061167

```text
(config)# do-exec show isdn <?test_int_action@55558ce1c950> status <cr>
```

Handler ` RVA 0x1E0319F0 `；selector ` 3 `；EOL ` RVA 0x378C95E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e5d3ef8331c5f811](../../evidence/conditions-sets-089.md#c-e5d3ef8331c5f811) · [缺口 G-4fe0ddbfc26b9408](../../evidence/gaps-sets-003.md#g-4fe0ddbfc26b9408) · [状态效果 S-fb8eb4c6c4a3c9df](../../evidence/state_effects-sets-053.md#s-fb8eb4c6c4a3c9df)

### path-061163

```text
(config)# do-exec show isdn <?test_int_action@55558ce1c950> timers <cr>
```

Handler ` RVA 0x1E0319F0 `；selector ` 2 `；EOL ` RVA 0x378C9170 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-944c7d5008d47990](../../evidence/conditions-sets-057.md#c-944c7d5008d47990) · [缺口 G-4fe0ddbfc26b9408](../../evidence/gaps-sets-003.md#g-4fe0ddbfc26b9408) · [状态效果 S-d12186ccd8fb9c70](../../evidence/state_effects-sets-044.md#s-d12186ccd8fb9c70)

### path-061778

```text
(config)# do-exec show isdn answer <interface> <string> <cr>
```

Handler ` RVA 0x1E0319F0 `；selector ` 9 `；EOL ` RVA 0x378C8A00 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` callingnumber:subaddr。

[条件 C-307c55f52e86a51e](../../evidence/conditions-sets-019.md#c-307c55f52e86a51e) · [缺口 G-3679ac6450d690bd](../../evidence/gaps-sets-002.md#g-3679ac6450d690bd) · [参数 P-aeb4cf28cd4ab242](../../evidence/parameters-sets-013.md#p-aeb4cf28cd4ab242) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-051049

```text
(config)# do-exec show isdn answer <number:0..95> <string> <cr>
```

Handler ` RVA 0x1E0319F0 `；selector ` 9 `；EOL ` RVA 0x378C8A00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` List of DSL's；` string ` callingnumber:subaddr。

[条件 C-0ad74d0466c90e80](../../evidence/conditions-sets-005.md#c-0ad74d0466c90e80) · [参数 P-a1270995903425ab](../../evidence/parameters-sets-012.md#p-a1270995903425ab) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061769

```text
(config)# do-exec show isis * <string> hostname <cr>
```

Handler ` RVA 0x10768F10 `；selector ` 10 `；EOL ` RVA 0x34B62158 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` IS-IS Process tag (use "null" for no tag)。

[条件 C-db16f2039570f514](../../evidence/conditions-sets-084.md#c-db16f2039570f514) · [缺口 G-d37556bc956284ee](../../evidence/gaps-sets-007.md#g-d37556bc956284ee) · [参数 P-248701c061a5d527](../../evidence/parameters-sets-003.md#p-248701c061a5d527) · [状态效果 S-98f434aa3e7ca2b0](../../evidence/state_effects-sets-032.md#s-98f434aa3e7ca2b0)

### path-061772

```text
(config)# do-exec show isis * <string> lsp-log <cr>
```

Handler ` RVA 0x107666B0 `；selector ` 9 `；EOL ` RVA 0x34B62400 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` IS-IS Process tag (use "null" for no tag)。

[条件 C-db16f2039570f514](../../evidence/conditions-sets-084.md#c-db16f2039570f514) · [缺口 G-d37556bc956284ee](../../evidence/gaps-sets-007.md#g-d37556bc956284ee) · [参数 P-248701c061a5d527](../../evidence/parameters-sets-003.md#p-248701c061a5d527) · [状态效果 S-98f434aa3e7ca2b0](../../evidence/state_effects-sets-032.md#s-98f434aa3e7ca2b0)

### path-061777

```text
(config)# do-exec show isis * <string> mpls <cr>
```

Handler ` RVA 0x1E6FEF60 `；selector ` 21 `；EOL ` RVA 0x34B66288 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` IS-IS Process tag (use "null" for no tag)。

[条件 C-9680562460f614bf](../../evidence/conditions-sets-058.md#c-9680562460f614bf) · [缺口 G-d37556bc956284ee](../../evidence/gaps-sets-007.md#g-d37556bc956284ee) · [参数 P-248701c061a5d527](../../evidence/parameters-sets-003.md#p-248701c061a5d527) · [状态效果 S-98f434aa3e7ca2b0](../../evidence/state_effects-sets-032.md#s-98f434aa3e7ca2b0)

### path-062455

```text
(config)# do-exec show isis * <string> mpls traffic-eng adjacency-log <cr>
```

Handler ` RVA 0x1E6FECE0 `；selector ` 6 `；EOL ` RVA 0x34B65968 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` IS-IS Process tag (use "null" for no tag)。

[条件 C-9680562460f614bf](../../evidence/conditions-sets-058.md#c-9680562460f614bf) · [缺口 G-d37556bc956284ee](../../evidence/gaps-sets-007.md#g-d37556bc956284ee) · [参数 P-248701c061a5d527](../../evidence/parameters-sets-003.md#p-248701c061a5d527) · [状态效果 S-98f434aa3e7ca2b0](../../evidence/state_effects-sets-032.md#s-98f434aa3e7ca2b0)

### path-062454

```text
(config)# do-exec show isis * <string> mpls traffic-eng advertisements <cr>
```

Handler ` RVA 0x1E6FECE0 `；selector ` 5 `；EOL ` RVA 0x34B656C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` IS-IS Process tag (use "null" for no tag)。

[条件 C-9680562460f614bf](../../evidence/conditions-sets-058.md#c-9680562460f614bf) · [缺口 G-d37556bc956284ee](../../evidence/gaps-sets-007.md#g-d37556bc956284ee) · [参数 P-248701c061a5d527](../../evidence/parameters-sets-003.md#p-248701c061a5d527) · [状态效果 S-98f434aa3e7ca2b0](../../evidence/state_effects-sets-032.md#s-98f434aa3e7ca2b0)

### path-062582

```text
(config)# do-exec show isis * <string> mpls traffic-eng downstream-tree <string> <cr>
```

Handler ` RVA 0x1E6FECE0 `；selector ` 7 `；EOL ` RVA 0x34B65CB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` IS-IS Process tag (use "null" for no tag)；` string ` System ID in hostname or in the form of xxxx.xxxx.xxxx。

[条件 C-9680562460f614bf](../../evidence/conditions-sets-058.md#c-9680562460f614bf) · [缺口 G-d37556bc956284ee](../../evidence/gaps-sets-007.md#g-d37556bc956284ee) · [参数 P-80c33a66a17e4af9](../../evidence/parameters-sets-010.md#p-80c33a66a17e4af9) · [状态效果 S-98f434aa3e7ca2b0](../../evidence/state_effects-sets-032.md#s-98f434aa3e7ca2b0)

### path-062456

```text
(config)# do-exec show isis * <string> mpls traffic-eng tunnel <cr>
```

Handler ` RVA 0x1E6FECE0 `；selector ` 8 `；EOL ` RVA 0x34B65FB0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` IS-IS Process tag (use "null" for no tag)。

[条件 C-9680562460f614bf](../../evidence/conditions-sets-058.md#c-9680562460f614bf) · [缺口 G-d37556bc956284ee](../../evidence/gaps-sets-007.md#g-d37556bc956284ee) · [参数 P-248701c061a5d527](../../evidence/parameters-sets-003.md#p-248701c061a5d527) · [状态效果 S-98f434aa3e7ca2b0](../../evidence/state_effects-sets-032.md#s-98f434aa3e7ca2b0)

### path-061771

```text
(config)# do-exec show isis * <string> neighbors <cr>
```

Handler ` RVA 0x1076CB60 `；selector ` 4 `；EOL ` RVA 0x34B62738 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` IS-IS Process tag (use "null" for no tag)。

[条件 C-9680562460f614bf](../../evidence/conditions-sets-058.md#c-9680562460f614bf) · [缺口 G-d37556bc956284ee](../../evidence/gaps-sets-007.md#g-d37556bc956284ee) · [参数 P-248701c061a5d527](../../evidence/parameters-sets-003.md#p-248701c061a5d527) · [状态效果 S-98f434aa3e7ca2b0](../../evidence/state_effects-sets-032.md#s-98f434aa3e7ca2b0)

### path-061779

```text
(config)# do-exec show isis * <string> node <cr>
```

Handler ` RVA 0x106D25B0 `；selector ` 42 `；EOL ` RVA 0x34B64460 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` IS-IS Process tag (use "null" for no tag)。

[条件 C-9680562460f614bf](../../evidence/conditions-sets-058.md#c-9680562460f614bf) · [缺口 G-d37556bc956284ee](../../evidence/gaps-sets-007.md#g-d37556bc956284ee) · [参数 P-248701c061a5d527](../../evidence/parameters-sets-003.md#p-248701c061a5d527) · [状态效果 S-cb2bf185b5dae534](../../evidence/state_effects-sets-043.md#s-cb2bf185b5dae534)

### path-061774

```text
(config)# do-exec show isis * <string> private <cr>
```

Handler ` RVA 0x1076B790 `；selector ` 16 `；EOL ` RVA 0x34B62D20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` IS-IS Process tag (use "null" for no tag)。

[条件 C-9680562460f614bf](../../evidence/conditions-sets-058.md#c-9680562460f614bf) · [缺口 G-d37556bc956284ee](../../evidence/gaps-sets-007.md#g-d37556bc956284ee) · [参数 P-248701c061a5d527](../../evidence/parameters-sets-003.md#p-248701c061a5d527) · [状态效果 S-98f434aa3e7ca2b0](../../evidence/state_effects-sets-032.md#s-98f434aa3e7ca2b0)

### path-061770

```text
(config)# do-exec show isis * <string> timers <cr>
```

Handler ` RVA 0x10769C20 `；selector ` 11 `；EOL ` RVA 0x34B62A10 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` IS-IS Process tag (use "null" for no tag)。

[条件 C-9680562460f614bf](../../evidence/conditions-sets-058.md#c-9680562460f614bf) · [缺口 G-d37556bc956284ee](../../evidence/gaps-sets-007.md#g-d37556bc956284ee) · [参数 P-248701c061a5d527](../../evidence/parameters-sets-003.md#p-248701c061a5d527) · [状态效果 S-98f434aa3e7ca2b0](../../evidence/state_effects-sets-032.md#s-98f434aa3e7ca2b0)

### path-061775

```text
(config)# do-exec show isis * <string> tree <cr>
```

Handler ` RVA 0x106B8630 `；selector ` 0 `；EOL ` RVA 0x34B61DA8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` IS-IS Process tag (use "null" for no tag)。

[条件 C-db16f2039570f514](../../evidence/conditions-sets-084.md#c-db16f2039570f514) · [缺口 G-d37556bc956284ee](../../evidence/gaps-sets-007.md#g-d37556bc956284ee) · [参数 P-248701c061a5d527](../../evidence/parameters-sets-003.md#p-248701c061a5d527) · [状态效果 S-2e63395f70676c66](../../evidence/state_effects-sets-010.md#s-2e63395f70676c66)

### path-061743

```text
(config)# do-exec show isis * adjacency stagger <cr>
```

Handler ` RVA 0x106F9DE0 `；selector ` 13 `；EOL ` RVA 0x34B69630 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-728e761dc62fad3c](../../evidence/conditions-sets-044.md#c-728e761dc62fad3c) · [缺口 G-d37556bc956284ee](../../evidence/gaps-sets-007.md#g-d37556bc956284ee) · [状态效果 S-98f434aa3e7ca2b0](../../evidence/state_effects-sets-032.md#s-98f434aa3e7ca2b0)

### path-061122

```text
(config)# do-exec show isis * mesh-groups <cr>
```

Handler ` RVA 0x10769310 `；selector ` 14 `；EOL ` RVA 0x34B69290 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-728e761dc62fad3c](../../evidence/conditions-sets-044.md#c-728e761dc62fad3c) · [缺口 G-d37556bc956284ee](../../evidence/gaps-sets-007.md#g-d37556bc956284ee) · [状态效果 S-98f434aa3e7ca2b0](../../evidence/state_effects-sets-032.md#s-98f434aa3e7ca2b0)

### path-061124

```text
(config)# do-exec show isis * mt <cr>
```

Handler ` RVA 0x1076C920 `；selector ` 20 `；EOL ` RVA 0x34B68F90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-32d764269bb00efa](../../evidence/conditions-sets-020.md#c-32d764269bb00efa) · [缺口 G-d37556bc956284ee](../../evidence/gaps-sets-007.md#g-d37556bc956284ee) · [状态效果 S-98f434aa3e7ca2b0](../../evidence/state_effects-sets-032.md#s-98f434aa3e7ca2b0)

### path-061133

```text
(config)# do-exec show isis * nsf <cr>
```

Handler ` RVA 0x1076C1B0 `；selector ` 19 `；EOL ` RVA 0x33FCAB48 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-728e761dc62fad3c](../../evidence/conditions-sets-044.md#c-728e761dc62fad3c) · [缺口 G-d37556bc956284ee](../../evidence/gaps-sets-007.md#g-d37556bc956284ee) · [状态效果 S-98f434aa3e7ca2b0](../../evidence/state_effects-sets-032.md#s-98f434aa3e7ca2b0)

### path-061127

```text
(config)# do-exec show isis * protocol <cr>
```

Handler ` RVA 0x10769A20 `；selector ` 12 `；EOL ` RVA 0x34B698E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-728e761dc62fad3c](../../evidence/conditions-sets-044.md#c-728e761dc62fad3c) · [缺口 G-d37556bc956284ee](../../evidence/gaps-sets-007.md#g-d37556bc956284ee) · [状态效果 S-98f434aa3e7ca2b0](../../evidence/state_effects-sets-032.md#s-98f434aa3e7ca2b0)

### path-061126

```text
(config)# do-exec show isis * rib <cr>
```

Handler ` RVA 0x1076C3C0 `；selector ` 17 `；EOL ` RVA 0x34B67E38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e4656162ee5a22a6](../../evidence/conditions-sets-088.md#c-e4656162ee5a22a6) · [缺口 G-d37556bc956284ee](../../evidence/gaps-sets-007.md#g-d37556bc956284ee) · [状态效果 S-98f434aa3e7ca2b0](../../evidence/state_effects-sets-032.md#s-98f434aa3e7ca2b0)

### path-061735

```text
(config)# do-exec show isis * rib prefix-sid <cr>
```

Handler ` RVA 0x1076C3C0 `；selector ` 34 `；EOL ` RVA 0x34B68540 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3becdc228d146a14](../../evidence/conditions-sets-023.md#c-3becdc228d146a14) · [缺口 G-d37556bc956284ee](../../evidence/gaps-sets-007.md#g-d37556bc956284ee) · [状态效果 S-240a5a38873c85a7](../../evidence/state_effects-sets-008.md#s-240a5a38873c85a7)

### path-061736

```text
(config)# do-exec show isis * rib redistribution <cr>
```

Handler ` RVA 0x1076C3C0 `；selector ` 18 `；EOL ` RVA 0x34B67AB0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-80ca76575567dd43](../../evidence/conditions-sets-050.md#c-80ca76575567dd43) · [缺口 G-d37556bc956284ee](../../evidence/gaps-sets-007.md#g-d37556bc956284ee) · [状态效果 S-98f434aa3e7ca2b0](../../evidence/state_effects-sets-032.md#s-98f434aa3e7ca2b0)

### path-061741

```text
(config)# do-exec show isis * rib strict-spf-sid <cr>
```

Handler ` RVA 0x1076C3C0 `；selector ` 35 `；EOL ` RVA 0x34B68880 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3becdc228d146a14](../../evidence/conditions-sets-023.md#c-3becdc228d146a14) · [缺口 G-d37556bc956284ee](../../evidence/gaps-sets-007.md#g-d37556bc956284ee) · [状态效果 S-e73878b1416067b6](../../evidence/state_effects-sets-049.md#s-e73878b1416067b6)

### path-061130

```text
(config)# do-exec show isis * route <cr>
```

Handler ` RVA 0xFD35BD0 `；selector ` 2 `；EOL ` RVA 0x34B69BD0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-728e761dc62fad3c](../../evidence/conditions-sets-044.md#c-728e761dc62fad3c) · [缺口 G-d37556bc956284ee](../../evidence/gaps-sets-007.md#g-d37556bc956284ee) · [状态效果 S-98f434aa3e7ca2b0](../../evidence/state_effects-sets-032.md#s-98f434aa3e7ca2b0)

### path-061117

```text
(config)# do-exec show isis * spf-log <cr>
```

Handler ` RVA 0x10768B40 `；selector ` 3 `；EOL ` RVA 0x34B674B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e733523371213026](../../evidence/conditions-sets-089.md#c-e733523371213026) · [缺口 G-d37556bc956284ee](../../evidence/gaps-sets-007.md#g-d37556bc956284ee) · [状态效果 S-98f434aa3e7ca2b0](../../evidence/state_effects-sets-032.md#s-98f434aa3e7ca2b0)

### path-061112

```text
(config)# do-exec show isis * topology <cr>
```

Handler ` RVA 0x106B8970 `；selector ` 1 `；EOL ` RVA 0x34B66B98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e733523371213026](../../evidence/conditions-sets-089.md#c-e733523371213026) · [缺口 G-d37556bc956284ee](../../evidence/gaps-sets-007.md#g-d37556bc956284ee) · [状态效果 S-73ac0009508231d2](../../evidence/state_effects-sets-025.md#s-73ac0009508231d2)

### path-042019

```text
(config)# do-exec show isis adjacency stagger <cr>
```

Handler ` RVA 0x106F9DE0 `；selector ` 13 `；EOL ` RVA 0x34B69630 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b22e0830437ab529](../../evidence/conditions-sets-069.md#c-b22e0830437ab529) · [状态效果 S-7eb57a9552ae3d54](../../evidence/state_effects-sets-027.md#s-7eb57a9552ae3d54)

### path-032694

```text
(config)# do-exec show isis database <cr>
```

Handler ` RVA 0x106B7B10 `；selector ` 0 `；EOL ` RVA 0x34B630A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0831611ef3050e7b](../../evidence/conditions-sets-004.md#c-0831611ef3050e7b) · [状态效果 S-133fa59d9f711825](../../evidence/state_effects-sets-005.md#s-133fa59d9f711825)

### path-061746

```text
(config)# do-exec show isis database prefix <prefix:dynamic> <cr>
```

Handler ` RVA 0x106B7B10 `；selector ` 0 `；EOL ` RVA 0x34B630A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` IP prefix &lt;network&gt;/&lt;length&gt;, e.g., 10.0.0.0/8。

[条件 C-a45423d9c1c8b39d](../../evidence/conditions-sets-063.md#c-a45423d9c1c8b39d) · [缺口 G-824137ec13bc260f](../../evidence/gaps-sets-005.md#g-824137ec13bc260f) · [参数 P-08f3b9c67bbe8067](../../evidence/parameters-sets-001.md#p-08f3b9c67bbe8067) · [状态效果 S-0b6f4271f3e09010](../../evidence/state_effects-sets-003.md#s-0b6f4271f3e09010)

### path-032606

```text
(config)# do-exec show isis hostname <cr>
```

Handler ` RVA 0x10768F10 `；selector ` 10 `；EOL ` RVA 0x34B62158 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0b90454a71b6a7f7](../../evidence/conditions-sets-005.md#c-0b90454a71b6a7f7) · [状态效果 S-195b452dd6deb4e7](../../evidence/state_effects-sets-006.md#s-195b452dd6deb4e7)

### path-032633

```text
(config)# do-exec show isis lsp-log <cr>
```

Handler ` RVA 0x107666B0 `；selector ` 9 `；EOL ` RVA 0x34B62400 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0b90454a71b6a7f7](../../evidence/conditions-sets-005.md#c-0b90454a71b6a7f7) · [状态效果 S-195b452dd6deb4e7](../../evidence/state_effects-sets-006.md#s-195b452dd6deb4e7)

### path-050530

```text
(config)# do-exec show isis lspgen tlv neighbor <cr>
```

Handler ` RVA 0x10780F80 `；selector ` 43 `；EOL ` RVA 0x34B652D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0831611ef3050e7b](../../evidence/conditions-sets-004.md#c-0831611ef3050e7b) · [状态效果 S-efd364c312d15000](../../evidence/state_effects-sets-051.md#s-efd364c312d15000)

### path-062447

```text
(config)# do-exec show isis lspgen tlv neighbor interface <interface> <cr>
```

Handler ` RVA 0x10780F80 `；selector ` 43 `；EOL ` RVA 0x34B652D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b61b592c302f8405](../../evidence/conditions-sets-070.md#c-b61b592c302f8405) · [缺口 G-e2f582be339a92f8](../../evidence/gaps-sets-008.md#g-e2f582be339a92f8) · [参数 P-7d8d3462f85e745d](../../evidence/parameters-sets-010.md#p-7d8d3462f85e745d) · [状态效果 S-efd364c312d15000](../../evidence/state_effects-sets-051.md#s-efd364c312d15000)

### path-032856

```text
(config)# do-exec show isis mesh-groups <cr>
```

Handler ` RVA 0x10769310 `；selector ` 14 `；EOL ` RVA 0x34B69290 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b22e0830437ab529](../../evidence/conditions-sets-069.md#c-b22e0830437ab529) · [状态效果 S-7eb57a9552ae3d54](../../evidence/state_effects-sets-027.md#s-7eb57a9552ae3d54)

### path-032730

```text
(config)# do-exec show isis mpls <cr>
```

Handler ` RVA 0x1E6FEF60 `；selector ` 21 `；EOL ` RVA 0x34B66288 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0831611ef3050e7b](../../evidence/conditions-sets-004.md#c-0831611ef3050e7b) · [状态效果 S-195b452dd6deb4e7](../../evidence/state_effects-sets-006.md#s-195b452dd6deb4e7)

### path-050527

```text
(config)# do-exec show isis mpls ldp igp-shortcuts <cr>
```

Handler ` RVA 0x1E6FEF60 `；selector ` 27 `；EOL ` RVA 0x34B66358 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0831611ef3050e7b](../../evidence/conditions-sets-004.md#c-0831611ef3050e7b) · [状态效果 S-195b452dd6deb4e7](../../evidence/state_effects-sets-006.md#s-195b452dd6deb4e7)

### path-062445

```text
(config)# do-exec show isis mpls ldp igp-shortcuts interface <interface> <cr>
```

Handler ` RVA 0x1E6FEF60 `；selector ` 27 `；EOL ` RVA 0x34B66358 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-cb09763984ea3fad](../../evidence/conditions-sets-078.md#c-cb09763984ea3fad) · [缺口 G-f6a4f7f1a96f1117](../../evidence/gaps-sets-008.md#g-f6a4f7f1a96f1117) · [参数 P-2dfafcb34cb5cd21](../../evidence/parameters-sets-004.md#p-2dfafcb34cb5cd21) · [状态效果 S-195b452dd6deb4e7](../../evidence/state_effects-sets-006.md#s-195b452dd6deb4e7)

### path-050499

```text
(config)# do-exec show isis mpls traffic-eng adjacency-log <cr>
```

Handler ` RVA 0x1E6FECE0 `；selector ` 6 `；EOL ` RVA 0x34B65968 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0831611ef3050e7b](../../evidence/conditions-sets-004.md#c-0831611ef3050e7b) · [状态效果 S-195b452dd6deb4e7](../../evidence/state_effects-sets-006.md#s-195b452dd6deb4e7)

### path-050479

```text
(config)# do-exec show isis mpls traffic-eng advertisements <cr>
```

Handler ` RVA 0x1E6FECE0 `；selector ` 5 `；EOL ` RVA 0x34B656C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0831611ef3050e7b](../../evidence/conditions-sets-004.md#c-0831611ef3050e7b) · [状态效果 S-195b452dd6deb4e7](../../evidence/state_effects-sets-006.md#s-195b452dd6deb4e7)

### path-056112

```text
(config)# do-exec show isis mpls traffic-eng downstream-tree <string> <cr>
```

Handler ` RVA 0x1E6FECE0 `；selector ` 7 `；EOL ` RVA 0x34B65CB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` System ID in hostname or in the form of xxxx.xxxx.xxxx。

[条件 C-0831611ef3050e7b](../../evidence/conditions-sets-004.md#c-0831611ef3050e7b) · [参数 P-eb90314b48b3b746](../../evidence/parameters-sets-018.md#p-eb90314b48b3b746) · [状态效果 S-195b452dd6deb4e7](../../evidence/state_effects-sets-006.md#s-195b452dd6deb4e7)

### path-050550

```text
(config)# do-exec show isis mpls traffic-eng tunnel <cr>
```

Handler ` RVA 0x1E6FECE0 `；selector ` 8 `；EOL ` RVA 0x34B65FB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0831611ef3050e7b](../../evidence/conditions-sets-004.md#c-0831611ef3050e7b) · [状态效果 S-195b452dd6deb4e7](../../evidence/state_effects-sets-006.md#s-195b452dd6deb4e7)

### path-032862

```text
(config)# do-exec show isis mt <cr>
```

Handler ` RVA 0x1076C920 `；selector ` 20 `；EOL ` RVA 0x34B68F90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-858191689cf0b69a](../../evidence/conditions-sets-052.md#c-858191689cf0b69a) · [状态效果 S-7eb57a9552ae3d54](../../evidence/state_effects-sets-027.md#s-7eb57a9552ae3d54)

### path-032614

```text
(config)# do-exec show isis neighbors <cr>
```

Handler ` RVA 0x1076CB60 `；selector ` 4 `；EOL ` RVA 0x34B62738 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0831611ef3050e7b](../../evidence/conditions-sets-004.md#c-0831611ef3050e7b) · [状态效果 S-195b452dd6deb4e7](../../evidence/state_effects-sets-006.md#s-195b452dd6deb4e7)

### path-032771

```text
(config)# do-exec show isis node <cr>
```

Handler ` RVA 0x106D25B0 `；selector ` 42 `；EOL ` RVA 0x34B64460 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0831611ef3050e7b](../../evidence/conditions-sets-004.md#c-0831611ef3050e7b) · [状态效果 S-112333266b2e5a86](../../evidence/state_effects-sets-004.md#s-112333266b2e5a86)

### path-032937

```text
(config)# do-exec show isis nsf <cr>
```

Handler ` RVA 0x1076C1B0 `；selector ` 19 `；EOL ` RVA 0x33FCAB48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b22e0830437ab529](../../evidence/conditions-sets-069.md#c-b22e0830437ab529) · [状态效果 S-7eb57a9552ae3d54](../../evidence/state_effects-sets-027.md#s-7eb57a9552ae3d54)

### path-032656

```text
(config)# do-exec show isis private <cr>
```

Handler ` RVA 0x1076B790 `；selector ` 16 `；EOL ` RVA 0x34B62D20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0831611ef3050e7b](../../evidence/conditions-sets-004.md#c-0831611ef3050e7b) · [状态效果 S-195b452dd6deb4e7](../../evidence/state_effects-sets-006.md#s-195b452dd6deb4e7)

### path-032880

```text
(config)# do-exec show isis protocol <cr>
```

Handler ` RVA 0x10769A20 `；selector ` 12 `；EOL ` RVA 0x34B698E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b22e0830437ab529](../../evidence/conditions-sets-069.md#c-b22e0830437ab529) · [状态效果 S-7eb57a9552ae3d54](../../evidence/state_effects-sets-027.md#s-7eb57a9552ae3d54)

### path-032874

```text
(config)# do-exec show isis rib <cr>
```

Handler ` RVA 0x1076C3C0 `；selector ` 17 `；EOL ` RVA 0x34B67E38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-494f9acbdcf342cc](../../evidence/conditions-sets-029.md#c-494f9acbdcf342cc) · [状态效果 S-7eb57a9552ae3d54](../../evidence/state_effects-sets-027.md#s-7eb57a9552ae3d54)

### path-041980

```text
(config)# do-exec show isis rib prefix-sid <cr>
```

Handler ` RVA 0x1076C3C0 `；selector ` 34 `；EOL ` RVA 0x34B68540 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-06897c89d6ebbaea](../../evidence/conditions-sets-003.md#c-06897c89d6ebbaea) · [状态效果 S-5f46ca92e2969dc6](../../evidence/state_effects-sets-020.md#s-5f46ca92e2969dc6)

### path-041981

```text
(config)# do-exec show isis rib redistribution <cr>
```

Handler ` RVA 0x1076C3C0 `；selector ` 18 `；EOL ` RVA 0x34B67AB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-505fde52bab62387](../../evidence/conditions-sets-031.md#c-505fde52bab62387) · [状态效果 S-7eb57a9552ae3d54](../../evidence/state_effects-sets-027.md#s-7eb57a9552ae3d54)

### path-042000

```text
(config)# do-exec show isis rib strict-spf-sid <cr>
```

Handler ` RVA 0x1076C3C0 `；selector ` 35 `；EOL ` RVA 0x34B68880 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-06897c89d6ebbaea](../../evidence/conditions-sets-003.md#c-06897c89d6ebbaea) · [状态效果 S-375fb6f8ae916a4f](../../evidence/state_effects-sets-012.md#s-375fb6f8ae916a4f)

### path-032905

```text
(config)# do-exec show isis route <cr>
```

Handler ` RVA 0xFD35BD0 `；selector ` 2 `；EOL ` RVA 0x34B69BD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b22e0830437ab529](../../evidence/conditions-sets-069.md#c-b22e0830437ab529) · [状态效果 S-7eb57a9552ae3d54](../../evidence/state_effects-sets-027.md#s-7eb57a9552ae3d54)

### path-032820

```text
(config)# do-exec show isis spf-log <cr>
```

Handler ` RVA 0x10768B40 `；selector ` 3 `；EOL ` RVA 0x34B674B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0831611ef3050e7b](../../evidence/conditions-sets-004.md#c-0831611ef3050e7b) · [状态效果 S-7eb57a9552ae3d54](../../evidence/state_effects-sets-027.md#s-7eb57a9552ae3d54)

### path-032607

```text
(config)# do-exec show isis timers <cr>
```

Handler ` RVA 0x10769C20 `；selector ` 11 `；EOL ` RVA 0x34B62A10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0831611ef3050e7b](../../evidence/conditions-sets-004.md#c-0831611ef3050e7b) · [状态效果 S-195b452dd6deb4e7](../../evidence/state_effects-sets-006.md#s-195b452dd6deb4e7)

### path-032786

```text
(config)# do-exec show isis topology <cr>
```

Handler ` RVA 0x106B8970 `；selector ` 1 `；EOL ` RVA 0x34B66B98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0831611ef3050e7b](../../evidence/conditions-sets-004.md#c-0831611ef3050e7b) · [状态效果 S-e6dcefccc099f998](../../evidence/state_effects-sets-049.md#s-e6dcefccc099f998)

### path-032681

```text
(config)# do-exec show isis tree <cr>
```

Handler ` RVA 0x106B8630 `；selector ` 0 `；EOL ` RVA 0x34B61DA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0b90454a71b6a7f7](../../evidence/conditions-sets-005.md#c-0b90454a71b6a7f7) · [状态效果 S-b3c241ce18ed7b05](../../evidence/state_effects-sets-038.md#s-b3c241ce18ed7b05)

### path-033381

```text
(config)# do-exec show issu FSM <cr>
```

Handler ` RVA 0xD4B3A40 `；selector ` 16 `；EOL ` RVA 0x33E5DFD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cdeb835cf48d7e7d](../../evidence/conditions-sets-079.md#c-cdeb835cf48d7e7d) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042825

```text
(config)# do-exec show issu FSM <number:1..4294967295> <cr>
```

Handler ` RVA 0xD4B3A40 `；selector ` 17 `；EOL ` RVA 0x33E5DFA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Session ID。

[条件 C-cdeb835cf48d7e7d](../../evidence/conditions-sets-079.md#c-cdeb835cf48d7e7d) · [参数 P-3786898db2265749](../../evidence/parameters-sets-005.md#p-3786898db2265749) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042800

```text
(config)# do-exec show issu capability types <cr>
```

Handler ` RVA 0xD4B3A40 `；selector ` 8 `；EOL ` RVA 0x33E5C858 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cdeb835cf48d7e7d](../../evidence/conditions-sets-079.md#c-cdeb835cf48d7e7d) · [状态效果 S-88a70f24d482cacf](../../evidence/state_effects-sets-029.md#s-88a70f24d482cacf)

### path-051310

```text
(config)# do-exec show issu capability types <number:1..8035> <cr>
```

Handler ` RVA 0xD4B3A40 `；selector ` 9 `；EOL ` RVA 0x33E5C8C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Client ID。

[条件 C-cdeb835cf48d7e7d](../../evidence/conditions-sets-079.md#c-cdeb835cf48d7e7d) · [参数 P-7a8151b894eb0d6b](../../evidence/parameters-sets-010.md#p-7a8151b894eb0d6b) · [状态效果 S-88a70f24d482cacf](../../evidence/state_effects-sets-029.md#s-88a70f24d482cacf)

### path-056505

```text
(config)# do-exec show issu capability types <number:1..8035> <number:1..4294967295> <cr>
```

Handler ` RVA 0xD4B3A40 `；selector ` 10 `；EOL ` RVA 0x33E5C8A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Client ID；` unsigned_number ` Entity ID。

[条件 C-cdeb835cf48d7e7d](../../evidence/conditions-sets-079.md#c-cdeb835cf48d7e7d) · [参数 P-2e4be3649c0d169e](../../evidence/parameters-sets-004.md#p-2e4be3649c0d169e) · [状态效果 S-88a70f24d482cacf](../../evidence/state_effects-sets-029.md#s-88a70f24d482cacf)

### path-033313

```text
(config)# do-exec show issu clients <cr>
```

Handler ` RVA 0xD4B3A40 `；selector ` 1 `；EOL ` RVA 0x33E5B758 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cdeb835cf48d7e7d](../../evidence/conditions-sets-079.md#c-cdeb835cf48d7e7d) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061170

```text
(config)# do-exec show issu clients <number:dynamic> <cr>
```

Handler ` RVA 0xD4B3A40 `；selector ` 1 `；EOL ` RVA 0x33E5B758 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` peer uid。

[条件 C-b93cbf61b30f6ee5](../../evidence/conditions-sets-072.md#c-b93cbf61b30f6ee5) · [缺口 G-614b46b29da7c1f5](../../evidence/gaps-sets-004.md#g-614b46b29da7c1f5) · [参数 P-0742ad430ad11dfe](../../evidence/parameters-sets-001.md#p-0742ad430ad11dfe) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042682

```text
(config)# do-exec show issu clients distributed <cr>
```

Handler ` RVA 0xD4B3A40 `；selector ` 2 `；EOL ` RVA 0x33E5B4B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cdeb835cf48d7e7d](../../evidence/conditions-sets-079.md#c-cdeb835cf48d7e7d) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042851

```text
(config)# do-exec show issu comp-matrix stored <cr>
```

Handler ` RVA 0xD4B3A40 `；selector ` 18 `；EOL ` RVA 0x33E5E500 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cdeb835cf48d7e7d](../../evidence/conditions-sets-079.md#c-cdeb835cf48d7e7d) · [状态效果 S-ced2f1ab594ed545](../../evidence/state_effects-sets-044.md#s-ced2f1ab594ed545)

### path-033271

```text
(config)# do-exec show issu endpoints <cr>
```

Handler ` RVA 0xD4B3A40 `；selector ` 0 `；EOL ` RVA 0x33E5B1A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cdeb835cf48d7e7d](../../evidence/conditions-sets-079.md#c-cdeb835cf48d7e7d) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033311

```text
(config)# do-exec show issu entities <cr>
```

Handler ` RVA 0xD4B3A40 `；selector ` 3 `；EOL ` RVA 0x33E5BA80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cdeb835cf48d7e7d](../../evidence/conditions-sets-079.md#c-cdeb835cf48d7e7d) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042703

```text
(config)# do-exec show issu entities <number:1..8035> <cr>
```

Handler ` RVA 0xD4B3A40 `；selector ` 4 `；EOL ` RVA 0x33E5BA58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Client ID。

[条件 C-cdeb835cf48d7e7d](../../evidence/conditions-sets-079.md#c-cdeb835cf48d7e7d) · [参数 P-95068abb77fab82f](../../evidence/parameters-sets-011.md#p-95068abb77fab82f) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042683

```text
(config)# do-exec show issu image-version compatibility <cr>
```

Handler ` RVA 0xC795B00 `；selector ` 0 `；EOL ` RVA 0x33AEEA48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cdeb835cf48d7e7d](../../evidence/conditions-sets-079.md#c-cdeb835cf48d7e7d) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042822

```text
(config)# do-exec show issu message types <cr>
```

Handler ` RVA 0xD4B3A40 `；selector ` 11 `；EOL ` RVA 0x33E5D178 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cdeb835cf48d7e7d](../../evidence/conditions-sets-079.md#c-cdeb835cf48d7e7d) · [状态效果 S-5af435fd2cf4b5cf](../../evidence/state_effects-sets-020.md#s-5af435fd2cf4b5cf)

### path-051332

```text
(config)# do-exec show issu message types <number:1..8035> <cr>
```

Handler ` RVA 0xD4B3A40 `；selector ` 12 `；EOL ` RVA 0x33E5D1E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Client ID。

[条件 C-cdeb835cf48d7e7d](../../evidence/conditions-sets-079.md#c-cdeb835cf48d7e7d) · [参数 P-35ab82c68173873e](../../evidence/parameters-sets-005.md#p-35ab82c68173873e) · [状态效果 S-5af435fd2cf4b5cf](../../evidence/state_effects-sets-020.md#s-5af435fd2cf4b5cf)

### path-056514

```text
(config)# do-exec show issu message types <number:1..8035> <number:1..4294967295> <cr>
```

Handler ` RVA 0xD4B3A40 `；selector ` 13 `；EOL ` RVA 0x33E5D1C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Client ID；` unsigned_number ` Entity ID。

[条件 C-cdeb835cf48d7e7d](../../evidence/conditions-sets-079.md#c-cdeb835cf48d7e7d) · [参数 P-9d748ae178a27ee3](../../evidence/parameters-sets-012.md#p-9d748ae178a27ee3) · [状态效果 S-5af435fd2cf4b5cf](../../evidence/state_effects-sets-020.md#s-5af435fd2cf4b5cf)

### path-042845

```text
(config)# do-exec show issu negotiated capability <cr>
```

Handler ` RVA 0xD4B3A40 `；selector ` 14 `；EOL ` RVA 0x33E5DA38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cdeb835cf48d7e7d](../../evidence/conditions-sets-079.md#c-cdeb835cf48d7e7d) · [状态效果 S-a96dbc1b88d58272](../../evidence/state_effects-sets-036.md#s-a96dbc1b88d58272)

### path-051314

```text
(config)# do-exec show issu negotiated capability <number:1..4294967295> <cr>
```

Handler ` RVA 0xD4B3A40 `；selector ` 15 `；EOL ` RVA 0x33E5DA10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Session ID。

[条件 C-cdeb835cf48d7e7d](../../evidence/conditions-sets-079.md#c-cdeb835cf48d7e7d) · [参数 P-a550057b702b975a](../../evidence/parameters-sets-013.md#p-a550057b702b975a) · [状态效果 S-a96dbc1b88d58272](../../evidence/state_effects-sets-036.md#s-a96dbc1b88d58272)

### path-033328

```text
(config)# do-exec show issu sessions <cr>
```

Handler ` RVA 0xD4B3A40 `；selector ` 5 `；EOL ` RVA 0x33E5BFD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cdeb835cf48d7e7d](../../evidence/conditions-sets-079.md#c-cdeb835cf48d7e7d) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042772

```text
(config)# do-exec show issu sessions <number:1..8035> <cr>
```

Handler ` RVA 0xD4B3A40 `；selector ` 6 `；EOL ` RVA 0x33E5C048 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Client ID。

[条件 C-cdeb835cf48d7e7d](../../evidence/conditions-sets-079.md#c-cdeb835cf48d7e7d) · [参数 P-cc85f03b59e13e56](../../evidence/parameters-sets-015.md#p-cc85f03b59e13e56) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-051259

```text
(config)# do-exec show issu sessions <number:1..8035> <number:1..4294967295> <cr>
```

Handler ` RVA 0xD4B3A40 `；selector ` 7 `；EOL ` RVA 0x33E5C020 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Client ID；` unsigned_number ` Entity ID。

[条件 C-cdeb835cf48d7e7d](../../evidence/conditions-sets-079.md#c-cdeb835cf48d7e7d) · [参数 P-bd364dc6ecbe4858](../../evidence/parameters-sets-014.md#p-bd364dc6ecbe4858) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-030757

```text
(config)# do-exec show kerberos creds <cr>
```

Handler ` RVA 0xC3E3030 `；selector ` 5 `；EOL ` RVA 0x33A6AFA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032983

```text
(config)# do-exec show key chain <cr>
```

Handler ` RVA 0xFDBAB60 `；selector ` 0 `；EOL ` RVA 0x348CE238 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027615

```text
(config)# do-exec show keystore <cr>
```

Handler ` RVA 0x136EAC70 `；selector ` 0 `；EOL ` RVA 0x35C0BDD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033581

```text
(config)# do-exec show kron schedule <cr>
```

Handler ` RVA 0xF3BA710 `；selector ` 0 `；EOL ` RVA 0x34624D50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-060949

```text
(config)# do-exec show l2fib bridge-domain <number:dynamic> <cr>
```

Handler ` RVA 0xC7A6090 `；selector ` 0 `；EOL ` RVA 0x33AFC170 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Bridge domain number。

[条件 C-ec6eae2b410f044c](../../evidence/conditions-sets-091.md#c-ec6eae2b410f044c) · [缺口 G-755f15eff51ac4b4](../../evidence/gaps-sets-005.md#g-755f15eff51ac4b4) · [参数 P-ef791d15f6aedcba](../../evidence/parameters-sets-018.md#p-ef791d15f6aedcba) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062528

```text
(config)# do-exec show l2fib bridge-domain <number:dynamic> address multicast <address> <address> <cr>
```

Handler ` RVA 0xC7A6090 `；selector ` 3 `；EOL ` RVA 0x33AF9DB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Bridge domain number；` address ` Source or Group IPv4 address；` address ` Group IPv4 address。

[条件 C-ec6eae2b410f044c](../../evidence/conditions-sets-091.md#c-ec6eae2b410f044c) · [缺口 G-755f15eff51ac4b4](../../evidence/gaps-sets-005.md#g-755f15eff51ac4b4) · [参数 P-3f5c4381a447f58d](../../evidence/parameters-sets-005.md#p-3f5c4381a447f58d) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062340

```text
(config)# do-exec show l2fib bridge-domain <number:dynamic> address unicast <address> <cr>
```

Handler ` RVA 0xC7A6090 `；selector ` 4 `；EOL ` RVA 0x33AF9A70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Bridge domain number；` address ` MAC Address。

[条件 C-ec6eae2b410f044c](../../evidence/conditions-sets-091.md#c-ec6eae2b410f044c) · [缺口 G-755f15eff51ac4b4](../../evidence/gaps-sets-005.md#g-755f15eff51ac4b4) · [参数 P-2886aca62db9b90e](../../evidence/parameters-sets-003.md#p-2886aca62db9b90e) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062020

```text
(config)# do-exec show l2fib bridge-domain <number:dynamic> lisp decap <cr>
```

Handler ` RVA 0xC7A6090 `；selector ` 22 `；EOL ` RVA 0x33AFB0C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Bridge domain number。

[条件 C-ec6eae2b410f044c](../../evidence/conditions-sets-091.md#c-ec6eae2b410f044c) · [缺口 G-755f15eff51ac4b4](../../evidence/gaps-sets-005.md#g-755f15eff51ac4b4) · [参数 P-ef791d15f6aedcba](../../evidence/parameters-sets-018.md#p-ef791d15f6aedcba) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062016

```text
(config)# do-exec show l2fib bridge-domain <number:dynamic> lisp encap <cr>
```

Handler ` RVA 0xC7A6090 `；selector ` 23 `；EOL ` RVA 0x33AFAE20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Bridge domain number。

[条件 C-ec6eae2b410f044c](../../evidence/conditions-sets-091.md#c-ec6eae2b410f044c) · [缺口 G-755f15eff51ac4b4](../../evidence/gaps-sets-005.md#g-755f15eff51ac4b4) · [参数 P-ef791d15f6aedcba](../../evidence/parameters-sets-018.md#p-ef791d15f6aedcba) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062025

```text
(config)# do-exec show l2fib bridge-domain <number:dynamic> lisp mac_oce <cr>
```

Handler ` RVA 0xC7A6090 `；selector ` 21 `；EOL ` RVA 0x33AFB370 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Bridge domain number。

[条件 C-ec6eae2b410f044c](../../evidence/conditions-sets-091.md#c-ec6eae2b410f044c) · [缺口 G-755f15eff51ac4b4](../../evidence/gaps-sets-005.md#g-755f15eff51ac4b4) · [参数 P-ef791d15f6aedcba](../../evidence/parameters-sets-018.md#p-ef791d15f6aedcba) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062023

```text
(config)# do-exec show l2fib bridge-domain <number:dynamic> mpls mac_oce <cr>
```

Handler ` RVA 0xC7A6090 `；selector ` 15 `；EOL ` RVA 0x33AFBEE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Bridge domain number。

[条件 C-ec6eae2b410f044c](../../evidence/conditions-sets-091.md#c-ec6eae2b410f044c) · [缺口 G-755f15eff51ac4b4](../../evidence/gaps-sets-005.md#g-755f15eff51ac4b4) · [参数 P-ef791d15f6aedcba](../../evidence/parameters-sets-018.md#p-ef791d15f6aedcba) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062017

```text
(config)# do-exec show l2fib bridge-domain <number:dynamic> otv decap <cr>
```

Handler ` RVA 0xC7A6090 `；selector ` 11 `；EOL ` RVA 0x33AFAB20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Bridge domain number。

[条件 C-ec6eae2b410f044c](../../evidence/conditions-sets-091.md#c-ec6eae2b410f044c) · [缺口 G-755f15eff51ac4b4](../../evidence/gaps-sets-005.md#g-755f15eff51ac4b4) · [参数 P-ef791d15f6aedcba](../../evidence/parameters-sets-018.md#p-ef791d15f6aedcba) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062344

```text
(config)# do-exec show l2fib bridge-domain <number:dynamic> otv encap <address> <cr>
```

Handler ` RVA 0xC7A6090 `；selector ` 10 `；EOL ` RVA 0x33AFA860 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Bridge domain number；` address ` Encap IPv4 address。

[条件 C-ec6eae2b410f044c](../../evidence/conditions-sets-091.md#c-ec6eae2b410f044c) · [缺口 G-755f15eff51ac4b4](../../evidence/gaps-sets-005.md#g-755f15eff51ac4b4) · [参数 P-02cee063ecfb9acb](../../evidence/parameters-sets-001.md#p-02cee063ecfb9acb) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061447

```text
(config)# do-exec show l2fib bridge-domain <number:dynamic> port <cr>
```

Handler ` RVA 0xC7A6090 `；selector ` 5 `；EOL ` RVA 0x33AF9658 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Bridge domain number。

[条件 C-ec6eae2b410f044c](../../evidence/conditions-sets-091.md#c-ec6eae2b410f044c) · [缺口 G-755f15eff51ac4b4](../../evidence/gaps-sets-005.md#g-755f15eff51ac4b4) · [参数 P-ef791d15f6aedcba](../../evidence/parameters-sets-018.md#p-ef791d15f6aedcba) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062014

```text
(config)# do-exec show l2fib bridge-domain <number:dynamic> table multicast <cr>
```

Handler ` RVA 0xC7A6090 `；selector ` 2 `；EOL ` RVA 0x33AFA4F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Bridge domain number。

[条件 C-ec6eae2b410f044c](../../evidence/conditions-sets-091.md#c-ec6eae2b410f044c) · [缺口 G-755f15eff51ac4b4](../../evidence/gaps-sets-005.md#g-755f15eff51ac4b4) · [参数 P-ef791d15f6aedcba](../../evidence/parameters-sets-018.md#p-ef791d15f6aedcba) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062013

```text
(config)# do-exec show l2fib bridge-domain <number:dynamic> table unicast <cr>
```

Handler ` RVA 0xC7A6090 `；selector ` 1 `；EOL ` RVA 0x33AFA250 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Bridge domain number。

[条件 C-ec6eae2b410f044c](../../evidence/conditions-sets-091.md#c-ec6eae2b410f044c) · [缺口 G-755f15eff51ac4b4](../../evidence/gaps-sets-005.md#g-755f15eff51ac4b4) · [参数 P-ef791d15f6aedcba](../../evidence/parameters-sets-018.md#p-ef791d15f6aedcba) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062024

```text
(config)# do-exec show l2fib bridge-domain <number:dynamic> vxlan decap <cr>
```

Handler ` RVA 0xC7A6090 `；selector ` 13 `；EOL ` RVA 0x33AFB928 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Bridge domain number。

[条件 C-ec6eae2b410f044c](../../evidence/conditions-sets-091.md#c-ec6eae2b410f044c) · [缺口 G-755f15eff51ac4b4](../../evidence/gaps-sets-005.md#g-755f15eff51ac4b4) · [参数 P-ef791d15f6aedcba](../../evidence/parameters-sets-018.md#p-ef791d15f6aedcba) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062019

```text
(config)# do-exec show l2fib bridge-domain <number:dynamic> vxlan encap <cr>
```

Handler ` RVA 0xC7A6090 `；selector ` 12 `；EOL ` RVA 0x33AFB680 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Bridge domain number。

[条件 C-ec6eae2b410f044c](../../evidence/conditions-sets-091.md#c-ec6eae2b410f044c) · [缺口 G-755f15eff51ac4b4](../../evidence/gaps-sets-005.md#g-755f15eff51ac4b4) · [参数 P-ef791d15f6aedcba](../../evidence/parameters-sets-018.md#p-ef791d15f6aedcba) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062028

```text
(config)# do-exec show l2fib bridge-domain <number:dynamic> vxlan mac_oce <cr>
```

Handler ` RVA 0xC7A6090 `；selector ` 14 `；EOL ` RVA 0x33AFBBD0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Bridge domain number。

[条件 C-ec6eae2b410f044c](../../evidence/conditions-sets-091.md#c-ec6eae2b410f044c) · [缺口 G-755f15eff51ac4b4](../../evidence/gaps-sets-005.md#g-755f15eff51ac4b4) · [参数 P-ef791d15f6aedcba](../../evidence/parameters-sets-018.md#p-ef791d15f6aedcba) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-037661

```text
(config)# do-exec show l2fib bridge-domain detail <cr>
```

Handler ` RVA 0xC7A6090 `；selector ` 8 `；EOL ` RVA 0x33AF92D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-037610

```text
(config)# do-exec show l2fib bridge-domain summary <cr>
```

Handler ` RVA 0xC7A6090 `；selector ` 7 `；EOL ` RVA 0x33AF9030 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-047157

```text
(config)# do-exec show l2fib evpn ead local <cr>
```

Handler ` RVA 0xC7A6090 `；selector ` 24 `；EOL ` RVA 0x33AFDEC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-047206

```text
(config)# do-exec show l2fib evpn ead remote <cr>
```

Handler ` RVA 0xC7A6090 `；selector ` 25 `；EOL ` RVA 0x33AFE1D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062907

```text
(config)# do-exec show l2fib evpn ead remote esi <number:0..4294967295> <cr>
```

Handler ` RVA 0xC7A6090 `；selector ` 25 `；EOL ` RVA 0x33AFE1D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-708dfcd61d1674ef](../../evidence/conditions-sets-044.md#c-708dfcd61d1674ef) · [缺口 G-1a252f19d8665987](../../evidence/gaps-sets-001.md#g-1a252f19d8665987) · [参数 P-dd7eca0b16b832f3](../../evidence/parameters-sets-017.md#p-dd7eca0b16b832f3) · [状态效果 S-8952f0f86cc2b6e6](../../evidence/state_effects-sets-029.md#s-8952f0f86cc2b6e6)

### path-037655

```text
(config)# do-exec show l2fib log event <cr>
```

Handler ` RVA 0xC7A3F10 `；selector ` 0 `；EOL ` RVA 0x33AF8650 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-b1010f289d80c14f](../../evidence/state_effects-sets-037.md#s-b1010f289d80c14f)

### path-030897

```text
(config)# do-exec show l2fib next-hop-list <cr>
```

Handler ` RVA 0xC7A6090 `；selector ` 27 `；EOL ` RVA 0x33AFCBA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062842

```text
(config)# do-exec show l2fib next-hop-list esi <number:0..4294967295> <cr>
```

Handler ` RVA 0xC7A6090 `；selector ` 27 `；EOL ` RVA 0x33AFCBA8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2f94600d52eeeb9e](../../evidence/conditions-sets-019.md#c-2f94600d52eeeb9e) · [缺口 G-dd98345d1e0f9eea](../../evidence/gaps-sets-008.md#g-dd98345d1e0f9eea) · [参数 P-ee861de959893932](../../evidence/parameters-sets-018.md#p-ee861de959893932) · [状态效果 S-869ea9e64d8594c2](../../evidence/state_effects-sets-029.md#s-869ea9e64d8594c2)

### path-030873

```text
(config)# do-exec show l2fib output-list <cr>
```

Handler ` RVA 0xC7A6090 `；selector ` 9 `；EOL ` RVA 0x33AFC4E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-030898

```text
(config)# do-exec show l2fib path-list <cr>
```

Handler ` RVA 0xC7A6090 `；selector ` 26 `；EOL ` RVA 0x33AFC878 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061457

```text
(config)# do-exec show l2fib statistics bridge-domain <number:dynamic> <cr>
```

Handler ` RVA 0xC7A6090 `；selector ` 18 `；EOL ` RVA 0x33AFDB90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Bridge domain number。

[条件 C-7ffa8d550146e243](../../evidence/conditions-sets-050.md#c-7ffa8d550146e243) · [缺口 G-cafa7f697b4ecabd](../../evidence/gaps-sets-007.md#g-cafa7f697b4ecabd) · [参数 P-7a4937dc4a997b07](../../evidence/parameters-sets-010.md#p-7a4937dc4a997b07) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-037839

```text
(config)# do-exec show l2fib statistics detail <cr>
```

Handler ` RVA 0xC7A6090 `；selector ` 17 `；EOL ` RVA 0x33AFD348 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-037930

```text
(config)# do-exec show l2fib statistics events <cr>
```

Handler ` RVA 0xC7A6090 `；selector ` 19 `；EOL ` RVA 0x33AFD680 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-047181

```text
(config)# do-exec show l2fib statistics events history <cr>
```

Handler ` RVA 0xC7A6090 `；selector ` 20 `；EOL ` RVA 0x33AFD658 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-037784

```text
(config)# do-exec show l2fib statistics summary <cr>
```

Handler ` RVA 0xC7A6090 `；selector ` 16 `；EOL ` RVA 0x33AFD0A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027808

```text
(config)# do-exec show l2protocol-forward <cr>
```

Handler ` RVA 0x15FDB140 `；selector ` 29 `；EOL ` RVA 0x35E8EAA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061194

```text
(config)# do-exec show l2protocol-forward interface <interface> <cr>
```

Handler ` RVA 0x15FDB140 `；selector ` 29 `；EOL ` RVA 0x35E8EAA8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-752b179086d03238](../../evidence/conditions-sets-045.md#c-752b179086d03238) · [缺口 G-f62fe126ee7a5afb](../../evidence/gaps-sets-008.md#g-f62fe126ee7a5afb) · [参数 P-525084458e231c3e](../../evidence/parameters-sets-007.md#p-525084458e231c3e) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027807

```text
(config)# do-exec show l2protocol-tunnel <cr>
```

Handler ` RVA 0x15FDB140 `；selector ` 12 `；EOL ` RVA 0x35E8E678 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061192

```text
(config)# do-exec show l2protocol-tunnel interface <interface> <cr>
```

Handler ` RVA 0x15FDB140 `；selector ` 12 `；EOL ` RVA 0x35E8E678 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-38ca763d17f372d1](../../evidence/conditions-sets-022.md#c-38ca763d17f372d1) · [缺口 G-dce807a23250d7e8](../../evidence/gaps-sets-008.md#g-dce807a23250d7e8) · [参数 P-fdb717a61f4bbe95](../../evidence/parameters-sets-019.md#p-fdb717a61f4bbe95) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031794

```text
(config)# do-exec show l2rib clients <cr>
```

Handler ` RVA 0x12566CD0 `；selector ` 0 `；EOL ` RVA 0x358B3B40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-b097960f6e2cb803](../../evidence/state_effects-sets-037.md#s-b097960f6e2cb803)

### path-031786

```text
(config)# do-exec show l2rib counters <cr>
```

Handler ` RVA 0x12567A60 `；selector ` 0 `；EOL ` RVA 0x358B4888 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ae58b9eaf3392dfb](../../evidence/conditions-sets-067.md#c-ae58b9eaf3392dfb) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031789

```text
(config)# do-exec show l2rib deletions <cr>
```

Handler ` RVA 0x125677B0 `；selector ` 0 `；EOL ` RVA 0x358B45F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fb3b3b847a9f18d1](../../evidence/conditions-sets-097.md#c-fb3b3b847a9f18d1) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040700

```text
(config)# do-exec show l2rib multicast route <cr>
```

Handler ` RVA 0xC88D6E0 `；selector ` 1 `；EOL ` RVA 0x33B08858 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-930e4aac04e6dba4](../../evidence/conditions-sets-057.md#c-930e4aac04e6dba4) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031767

```text
(config)# do-exec show l2rib notifications <cr>
```

Handler ` RVA 0x12567680 `；selector ` 0 `；EOL ` RVA 0x358B42C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e7e42e5a3c27bdea](../../evidence/conditions-sets-090.md#c-e7e42e5a3c27bdea) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031793

```text
(config)# do-exec show l2rib producers <cr>
```

Handler ` RVA 0x125672F0 `；selector ` 0 `；EOL ` RVA 0x358B3F58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-34aa1e6a932fb760](../../evidence/state_effects-sets-012.md#s-34aa1e6a932fb760)

### path-031795

```text
(config)# do-exec show l2rib registrations <cr>
```

Handler ` RVA 0x125666A0 `；selector ` 0 `；EOL ` RVA 0x358B3760 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-ab058f38635b4ad2](../../evidence/state_effects-sets-036.md#s-ab058f38635b4ad2)

### path-061555

```text
(config)# do-exec show l2rib registrations topology <number:1..4294967293> <cr>
```

Handler ` RVA 0x125666A0 `；selector ` 0 `；EOL ` RVA 0x358B3760 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-af19a88834012c6a](../../evidence/conditions-sets-068.md#c-af19a88834012c6a) · [缺口 G-3df6751cabf3d672](../../evidence/gaps-sets-003.md#g-3df6751cabf3d672) · [参数 P-afe60d4e145377f1](../../evidence/parameters-sets-013.md#p-afe60d4e145377f1) · [状态效果 S-b92b5f754f7e95c4](../../evidence/state_effects-sets-039.md#s-b92b5f754f7e95c4)

### path-049003

```text
(config)# do-exec show l2rib test <string> msg-buffer <cr>
```

Handler ` RVA 0x125CDA60 `；selector ` 0 `；EOL ` RVA 0x358BF148 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Client name。

[条件 C-9cff1893b0707f6e](../../evidence/conditions-sets-061.md#c-9cff1893b0707f6e) · [参数 P-56c359cd28967776](../../evidence/parameters-sets-007.md#p-56c359cd28967776) · [状态效果 S-aec3b7d72b4a5c84](../../evidence/state_effects-sets-037.md#s-aec3b7d72b4a5c84)

### path-031753

```text
(config)# do-exec show l2rib topologies <cr>
```

Handler ` RVA 0x12566200 `；selector ` 0 `；EOL ` RVA 0x358B2FC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-b6b6f51e05222b36](../../evidence/state_effects-sets-039.md#s-b6b6f51e05222b36)

### path-061549

```text
(config)# do-exec show l2rib topologies topology <number:1..4294967293> <cr>
```

Handler ` RVA 0x12566200 `；selector ` 0 `；EOL ` RVA 0x358B2FC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d8efc39b2b6061d1](../../evidence/conditions-sets-083.md#c-d8efc39b2b6061d1) · [缺口 G-46a550b4746455c1](../../evidence/gaps-sets-003.md#g-46a550b4746455c1) · [参数 P-661bd94e5baf3316](../../evidence/parameters-sets-008.md#p-661bd94e5baf3316) · [状态效果 S-7e95aae8cc3a14bf](../../evidence/state_effects-sets-027.md#s-7e95aae8cc3a14bf)

### path-040673

```text
(config)# do-exec show l2rib unicast route <cr>
```

Handler ` RVA 0xC88D6E0 `；selector ` 0 `；EOL ` RVA 0x33B08588 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-930e4aac04e6dba4](../../evidence/conditions-sets-057.md#c-930e4aac04e6dba4) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062079

```text
(config)# do-exec show l2route evpn mac next-hop <interface> <cr>
```

Handler ` RVA 0x125C8E60 `；selector ` 0 `；EOL ` RVA 0x358B6C98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7e49983c61ce2efb](../../evidence/conditions-sets-049.md#c-7e49983c61ce2efb) · [缺口 G-6816492a54c1d6a8](../../evidence/gaps-sets-004.md#g-6816492a54c1d6a8) · [参数 P-1af67dc822b92c28](../../evidence/parameters-sets-003.md#p-1af67dc822b92c28) · [状态效果 S-ac12505f9b7742a6](../../evidence/state_effects-sets-036.md#s-ac12505f9b7742a6)

### path-039907

```text
(config)# do-exec show l2route evpn summary <cr>
```

Handler ` RVA 0x125C8E60 `；selector ` 0 `；EOL ` RVA 0x358B6C98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-9194c02a7698bd75](../../evidence/state_effects-sets-031.md#s-9194c02a7698bd75)

### path-061199

```text
(config)# do-exec show lacp <number:dynamic> counters <cr>
```

Handler ` RVA 0xC8D30C0 `；selector ` 0 `；EOL ` RVA 0x33B143B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Channel group number。

[条件 C-6c43741ccd4877e8](../../evidence/conditions-sets-042.md#c-6c43741ccd4877e8) · [缺口 G-75d44ae2cde48e14](../../evidence/gaps-sets-005.md#g-75d44ae2cde48e14) · [参数 P-0f3d8edd9bac5de5](../../evidence/parameters-sets-002.md#p-0f3d8edd9bac5de5) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061202

```text
(config)# do-exec show lacp <number:dynamic> internal <cr>
```

Handler ` RVA 0xC8D3050 `；selector ` 0 `；EOL ` RVA 0x33B146C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Channel group number。

[条件 C-6c43741ccd4877e8](../../evidence/conditions-sets-042.md#c-6c43741ccd4877e8) · [缺口 G-75d44ae2cde48e14](../../evidence/gaps-sets-005.md#g-75d44ae2cde48e14) · [参数 P-0f3d8edd9bac5de5](../../evidence/parameters-sets-002.md#p-0f3d8edd9bac5de5) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061200

```text
(config)# do-exec show lacp <number:dynamic> neighbor <cr>
```

Handler ` RVA 0xC8D2FE0 `；selector ` 0 `；EOL ` RVA 0x33B14118 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Channel group number。

[条件 C-6c43741ccd4877e8](../../evidence/conditions-sets-042.md#c-6c43741ccd4877e8) · [缺口 G-75d44ae2cde48e14](../../evidence/gaps-sets-005.md#g-75d44ae2cde48e14) · [参数 P-0f3d8edd9bac5de5](../../evidence/parameters-sets-002.md#p-0f3d8edd9bac5de5) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061201

```text
(config)# do-exec show lacp <number:dynamic> sm-state <cr>
```

Handler ` RVA 0xC8D3260 `；selector ` 0 `；EOL ` RVA 0x33B14968 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Channel group number。

[条件 C-6c43741ccd4877e8](../../evidence/conditions-sets-042.md#c-6c43741ccd4877e8) · [缺口 G-75d44ae2cde48e14](../../evidence/gaps-sets-005.md#g-75d44ae2cde48e14) · [参数 P-0f3d8edd9bac5de5](../../evidence/parameters-sets-002.md#p-0f3d8edd9bac5de5) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033897

```text
(config)# do-exec show lacp counters <cr>
```

Handler ` RVA 0xC8D30C0 `；selector ` 0 `；EOL ` RVA 0x33B143B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033910

```text
(config)# do-exec show lacp internal <cr>
```

Handler ` RVA 0xC8D3050 `；selector ` 0 `；EOL ` RVA 0x33B146C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-043748

```text
(config)# do-exec show lacp multi-chassis group <cr>
```

Handler ` RVA 0xC961EC0 `；selector ` 0 `；EOL ` RVA 0x33B33CE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-052014

```text
(config)# do-exec show lacp multi-chassis load-balance group <cr>
```

Handler ` RVA 0xC963BC0 `；selector ` 0 `；EOL ` RVA 0x33B34660 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-01026ecaf0983cf5](../../evidence/conditions-sets-001.md#c-01026ecaf0983cf5) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-052018

```text
(config)# do-exec show lacp multi-chassis load-balance port-channel <cr>
```

Handler ` RVA 0xC963BC0 `；selector ` 2 `；EOL ` RVA 0x33B349D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e86f49fd2aee1f70](../../evidence/conditions-sets-090.md#c-e86f49fd2aee1f70) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062227

```text
(config)# do-exec show lacp multi-chassis load-balance port-channel <interface> <cr>
```

Handler ` RVA 0xC963BC0 `；selector ` 1 `；EOL ` RVA 0x33B349A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-31590cf19a2d4e89](../../evidence/conditions-sets-019.md#c-31590cf19a2d4e89) · [缺口 G-a78e54fbf9c0bec8](../../evidence/gaps-sets-006.md#g-a78e54fbf9c0bec8) · [参数 P-627606ef8ad93af2](../../evidence/parameters-sets-008.md#p-627606ef8ad93af2) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-043763

```text
(config)# do-exec show lacp multi-chassis port-channel <cr>
```

Handler ` RVA 0xC961EC0 `；selector ` 2 `；EOL ` RVA 0x33B34078 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-aef62f669677dcbb](../../evidence/conditions-sets-068.md#c-aef62f669677dcbb) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061804

```text
(config)# do-exec show lacp multi-chassis port-channel <interface> <cr>
```

Handler ` RVA 0xC961EC0 `；selector ` 1 `；EOL ` RVA 0x33B34050 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6434078a078f26bf](../../evidence/conditions-sets-039.md#c-6434078a078f26bf) · [缺口 G-6b74398a5042923d](../../evidence/gaps-sets-004.md#g-6b74398a5042923d) · [参数 P-fdc0d7a33fc2633d](../../evidence/parameters-sets-019.md#p-fdc0d7a33fc2633d) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033899

```text
(config)# do-exec show lacp neighbor <cr>
```

Handler ` RVA 0xC8D2FE0 `；selector ` 0 `；EOL ` RVA 0x33B14118 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033907

```text
(config)# do-exec show lacp sm-state <cr>
```

Handler ` RVA 0xC8D3260 `；selector ` 0 `；EOL ` RVA 0x33B14968 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033884

```text
(config)# do-exec show lacp sys-id <cr>
```

Handler ` RVA 0xC8D31D0 `；selector ` 0 `；EOL ` RVA 0x33B11658 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033084

```text
(config)# do-exec show ldap attributes <cr>
```

Handler ` RVA 0x11ABB210 `；selector ` 22 `；EOL ` RVA 0x3560D6E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a6e3c1e156501b0d](../../evidence/conditions-sets-064.md#c-a6e3c1e156501b0d) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042336

```text
(config)# do-exec show ldap server all <cr>
```

Handler ` RVA 0x11ABAFB0 `；selector ` 23 `；EOL ` RVA 0x3560D298 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a6e3c1e156501b0d](../../evidence/conditions-sets-064.md#c-a6e3c1e156501b0d) · [状态效果 S-b05f648f4b6535b6](../../evidence/state_effects-sets-037.md#s-b05f648f4b6535b6)

### path-061374

```text
(config)# do-exec show license rum id <?fixed_number_action@555588da9408> <cr>
```

Handler ` RVA 0xBB467A0 `；selector ` 0 `；EOL ` RVA 0x33854DD8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ced47ececb95c2a8](../../evidence/conditions-sets-080.md#c-ced47ececb95c2a8) · [缺口 G-ed298030560d9fd6](../../evidence/gaps-sets-008.md#g-ed298030560d9fd6) · [状态效果 S-a06bc1016344a137](../../evidence/state_effects-sets-034.md#s-a06bc1016344a137)

### path-030175

```text
(config)# do-exec show license udi <cr>
```

Handler ` RVA 0xBB467A0 `；selector ` 0 `；EOL ` RVA 0x33854DD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2604a5c4a545571e](../../evidence/conditions-sets-015.md#c-2604a5c4a545571e) · [状态效果 S-bb326b2ab486fa5c](../../evidence/state_effects-sets-040.md#s-bb326b2ab486fa5c)

### path-060753

```text
(config)# do-exec show line <?ttyline_action@5555896d0f80> <cr>
```

Handler ` RVA 0xE2CC610 `；selector ` 0 `；EOL ` RVA 0x3417D010 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [缺口 G-255b2083e4794b1d](../../evidence/gaps-sets-002.md#g-255b2083e4794b1d) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061205

```text
(config)# do-exec show line <?ttyline_action@5555896d0f80> history <cr>
```

Handler ` RVA 0xE2CC3F0 `；selector ` 0 `；EOL ` RVA 0x3417D2C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [缺口 G-255b2083e4794b1d](../../evidence/gaps-sets-002.md#g-255b2083e4794b1d) · [状态效果 S-329670db1bc6783e](../../evidence/state_effects-sets-011.md#s-329670db1bc6783e)

### path-033939

```text
(config)# do-exec show line async-queue <cr>
```

Handler ` RVA 0xCCFA910 `；selector ` 0 `；EOL ` RVA 0x33C67D68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-c26f1bec1ab0c570](../../evidence/state_effects-sets-041.md#s-c26f1bec1ab0c570)

### path-033924

```text
(config)# do-exec show line x121-address <cr>
```

Handler ` RVA 0xFE59A10 `；selector ` 0 `；EOL ` RVA 0x34903960 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027747

```text
(config)# do-exec show list <cr>
```

Handler ` RVA 0xDEC7820 `；selector ` 0 `；EOL ` RVA 0x34092988 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027813

```text
(config)# do-exec show llc2 <cr>
```

Handler ` RVA 0xFDDE720 `；selector ` 0 `；EOL ` RVA 0x348DF260 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027623

```text
(config)# do-exec show lldp <cr>
```

Handler ` RVA 0x158A0DC0 `；selector ` 0 `；EOL ` RVA 0x35DA0DC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ef16c655930a9d84](../../evidence/conditions-sets-092.md#c-ef16c655930a9d84) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031960

```text
(config)# do-exec show lldp custom-information <cr>
```

Handler ` RVA 0x158A0DC0 `；selector ` 7 `；EOL ` RVA 0x35DA0D98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a4dfa349f522f2f6](../../evidence/conditions-sets-064.md#c-a4dfa349f522f2f6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040169

```text
(config)# do-exec show lldp entry <string> <cr>
```

Handler ` RVA 0x158A0DC0 `；selector ` 3 `；EOL ` RVA 0x35DA0AD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of LLDP neighbor entry。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-3b6d72de4a6a3586](../../evidence/parameters-sets-005.md#p-3b6d72de4a6a3586) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031885

```text
(config)# do-exec show lldp errors <cr>
```

Handler ` RVA 0x158A0DC0 `；selector ` 1 `；EOL ` RVA 0x35DA0328 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031896

```text
(config)# do-exec show lldp interface <cr>
```

Handler ` RVA 0x158A0DC0 `；selector ` 4 `；EOL ` RVA 0x35D9FAE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-43e68fe3e942a0b5](../../evidence/conditions-sets-027.md#c-43e68fe3e942a0b5) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061000

```text
(config)# do-exec show lldp interface <interface> <cr>
```

Handler ` RVA 0x158A0DC0 `；selector ` 4 `；EOL ` RVA 0x35D9FAE8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-efbe70c2f6ce5880](../../evidence/conditions-sets-093.md#c-efbe70c2f6ce5880) · [缺口 G-dbf9e654ab69a040](../../evidence/gaps-sets-008.md#g-dbf9e654ab69a040) · [参数 P-907042f9602b04c9](../../evidence/parameters-sets-011.md#p-907042f9602b04c9) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062077

```text
(config)# do-exec show lldp interface <interface> service-instance <number:1..8000> <cr>
```

Handler ` RVA 0x158A0DC0 `；selector ` 6 `；EOL ` RVA 0x35D9FB68 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Service instance ID。

[条件 C-efbe70c2f6ce5880](../../evidence/conditions-sets-093.md#c-efbe70c2f6ce5880) · [缺口 G-dbf9e654ab69a040](../../evidence/gaps-sets-008.md#g-dbf9e654ab69a040) · [参数 P-385adecdcbe4e02a](../../evidence/parameters-sets-005.md#p-385adecdcbe4e02a) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031967

```text
(config)# do-exec show lldp neighbors <cr>
```

Handler ` RVA 0x158A0DC0 `；selector ` 5 `；EOL ` RVA 0x35DA0720 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a57593a5c094f721](../../evidence/conditions-sets-064.md#c-a57593a5c094f721) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061004

```text
(config)# do-exec show lldp neighbors <interface> <cr>
```

Handler ` RVA 0x158A0DC0 `；selector ` 5 `；EOL ` RVA 0x35DA0720 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-997130bea118e170](../../evidence/conditions-sets-059.md#c-997130bea118e170) · [缺口 G-0fcf6a92b14704e7](../../evidence/gaps-sets-001.md#g-0fcf6a92b14704e7) · [参数 P-60a71d44b1209092](../../evidence/parameters-sets-008.md#p-60a71d44b1209092) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031869

```text
(config)# do-exec show lldp traffic <cr>
```

Handler ` RVA 0x158A0DC0 `；selector ` 2 `；EOL ` RVA 0x35DA0080 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-041268

```text
(config)# do-exec show llp nhrp multicast <cr>
```

Handler ` RVA 0x108D5B20 `；selector ` 4 `；EOL ` RVA 0x34BF3A28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-be7fe83e2ae2323b](../../evidence/conditions-sets-074.md#c-be7fe83e2ae2323b) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061659

```text
(config)# do-exec show llp nhrp multicast <interface> <cr>
```

Handler ` RVA 0x108D5B20 `；selector ` 4 `；EOL ` RVA 0x34BF3A28 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d90c66c32f48f9cb](../../evidence/conditions-sets-084.md#c-d90c66c32f48f9cb) · [缺口 G-156a48b5df198e8b](../../evidence/gaps-sets-001.md#g-156a48b5df198e8b) · [参数 P-09f6060c19ea1e59](../../evidence/parameters-sets-001.md#p-09f6060c19ea1e59) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033923

```text
(config)# do-exec show lnm bridge <cr>
```

Handler ` RVA 0x1233AF00 `；selector ` 0 `；EOL ` RVA 0x358130F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7a4f3d14390b8ea0](../../evidence/conditions-sets-047.md#c-7a4f3d14390b8ea0) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061203

```text
(config)# do-exec show lnm bridge <interface> <cr>
```

Handler ` RVA 0x1233AF00 `；selector ` 0 `；EOL ` RVA 0x358130F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0508eec353ad95ea](../../evidence/conditions-sets-002.md#c-0508eec353ad95ea) · [缺口 G-8de02418a8b4cb45](../../evidence/gaps-sets-005.md#g-8de02418a8b4cb45) · [参数 P-9cede3b9f0a6cff9](../../evidence/parameters-sets-012.md#p-9cede3b9f0a6cff9) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033917

```text
(config)# do-exec show lnm config <cr>
```

Handler ` RVA 0x1233AF00 `；selector ` 1 `；EOL ` RVA 0x358133B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-01c21347211b1f9b](../../evidence/conditions-sets-001.md#c-01c21347211b1f9b) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033932

```text
(config)# do-exec show lnm interface <cr>
```

Handler ` RVA 0x1233AF00 `；selector ` 2 `；EOL ` RVA 0x35813748 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-17ac5789c902dd0a](../../evidence/conditions-sets-009.md#c-17ac5789c902dd0a) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061204

```text
(config)# do-exec show lnm interface <interface> <cr>
```

Handler ` RVA 0x1233AF00 `；selector ` 2 `；EOL ` RVA 0x35813748 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-992bd7a25ddf9098](../../evidence/conditions-sets-059.md#c-992bd7a25ddf9098) · [缺口 G-6942553203c46ef5](../../evidence/gaps-sets-004.md#g-6942553203c46ef5) · [参数 P-f4fafee86455cf57](../../evidence/parameters-sets-018.md#p-f4fafee86455cf57) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033930

```text
(config)# do-exec show lnm ring <cr>
```

Handler ` RVA 0x1233AF00 `；selector ` 3 `；EOL ` RVA 0x35813A70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-01c21347211b1f9b](../../evidence/conditions-sets-001.md#c-01c21347211b1f9b) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061206

```text
(config)# do-exec show lnm station * <cr>
```

Handler ` RVA 0x1233AF00 `；selector ` 4 `；EOL ` RVA 0x35813DC8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f7c18b8f34943b62](../../evidence/conditions-sets-096.md#c-f7c18b8f34943b62) · [缺口 G-99894fa3a7b75931](../../evidence/gaps-sets-006.md#g-99894fa3a7b75931) · [状态效果 S-f4b337228139cfd0](../../evidence/state_effects-sets-052.md#s-f4b337228139cfd0)

### path-033940

```text
(config)# do-exec show lnm station <cr>
```

Handler ` RVA 0x1233AF00 `；selector ` 4 `；EOL ` RVA 0x35813DC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-01c21347211b1f9b](../../evidence/conditions-sets-001.md#c-01c21347211b1f9b) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027796

```text
(config)# do-exec show local-ack <cr>
```

Handler ` RVA 0x114A98F0 `；selector ` 0 `；EOL ` RVA 0x354FA698 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fb650d0e6817b4ff](../../evidence/conditions-sets-097.md#c-fb650d0e6817b4ff) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-026394

```text
(config)# do-exec show location <cr>
```

Handler ` RVA 0xD7987F0 `；selector ` 0 `；EOL ` RVA 0x34126998 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-028296

```text
(config)# do-exec show location admin-tag <cr>
```

Handler ` RVA 0xC916150 `；selector ` 1 `；EOL ` RVA 0x33B1E920 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-028537

```text
(config)# do-exec show location ap-proximity <cr>
```

Handler ` RVA 0xC916150 `；selector ` 8 `；EOL ` RVA 0x33B20990 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-202cc5ae4e47884c](../../evidence/conditions-sets-013.md#c-202cc5ae4e47884c) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061227

```text
(config)# do-exec show location civic-location interface <interface> <cr>
```

Handler ` RVA 0xC916150 `；selector ` 2 `；EOL ` RVA 0x33B1ED58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-bccc551afe7ed223](../../evidence/conditions-sets-073.md#c-bccc551afe7ed223) · [缺口 G-b8853412f547e817](../../evidence/gaps-sets-007.md#g-b8853412f547e817) · [参数 P-461967e7622522f2](../../evidence/parameters-sets-006.md#p-461967e7622522f2) · [状态效果 S-1476e78d8b3a30a8](../../evidence/state_effects-sets-005.md#s-1476e78d8b3a30a8)

### path-034401

```text
(config)# do-exec show location civic-location static <cr>
```

Handler ` RVA 0xC916150 `；selector ` 2 `；EOL ` RVA 0x33B1ED58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-e421910993507e0b](../../evidence/state_effects-sets-048.md#s-e421910993507e0b)

### path-061234

```text
(config)# do-exec show location custom-location interface <interface> <cr>
```

Handler ` RVA 0xC916150 `；selector ` 4 `；EOL ` RVA 0x33B1F8D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b8a0412f2763c7dc](../../evidence/conditions-sets-071.md#c-b8a0412f2763c7dc) · [缺口 G-e8db3dba76d7a08e](../../evidence/gaps-sets-008.md#g-e8db3dba76d7a08e) · [参数 P-9a305645e42da1e3](../../evidence/parameters-sets-012.md#p-9a305645e42da1e3) · [状态效果 S-c9dd4c537d360de0](../../evidence/state_effects-sets-043.md#s-c9dd4c537d360de0)

### path-034477

```text
(config)# do-exec show location custom-location static <cr>
```

Handler ` RVA 0xC916150 `；selector ` 4 `；EOL ` RVA 0x33B1F8D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-af230646b5f9b0ab](../../evidence/state_effects-sets-037.md#s-af230646b5f9b0ab)

### path-061230

```text
(config)# do-exec show location elin-location interface <interface> <cr>
```

Handler ` RVA 0xC916150 `；selector ` 3 `；EOL ` RVA 0x33B1F318 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-33195c7accecd8dc](../../evidence/conditions-sets-020.md#c-33195c7accecd8dc) · [缺口 G-8d3a3d906d99d4c0](../../evidence/gaps-sets-005.md#g-8d3a3d906d99d4c0) · [参数 P-7453b2716b413b2a](../../evidence/parameters-sets-009.md#p-7453b2716b413b2a) · [状态效果 S-354be3870dca46ab](../../evidence/state_effects-sets-012.md#s-354be3870dca46ab)

### path-034434

```text
(config)# do-exec show location elin-location static <cr>
```

Handler ` RVA 0xC916150 `；selector ` 3 `；EOL ` RVA 0x33B1F318 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-32bde5e4fab05b0f](../../evidence/state_effects-sets-011.md#s-32bde5e4fab05b0f)

### path-034613

```text
(config)# do-exec show location fex all <cr>
```

Handler ` RVA 0xC916150 `；selector ` 7 `；EOL ` RVA 0x33B20650 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-071bd517c16b604c](../../evidence/conditions-sets-003.md#c-071bd517c16b604c) · [状态效果 S-d1e18200cca72a76](../../evidence/state_effects-sets-044.md#s-d1e18200cca72a76)

### path-061237

```text
(config)# do-exec show location geo-location interface <interface> <cr>
```

Handler ` RVA 0xC916150 `；selector ` 6 `；EOL ` RVA 0x33B1FE98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-aa6c2836f2ad3cbd](../../evidence/conditions-sets-066.md#c-aa6c2836f2ad3cbd) · [缺口 G-eeec7b6307b7e167](../../evidence/gaps-sets-008.md#g-eeec7b6307b7e167) · [参数 P-f3c00a7763a8efb1](../../evidence/parameters-sets-018.md#p-f3c00a7763a8efb1) · [状态效果 S-1859009468133561](../../evidence/state_effects-sets-006.md#s-1859009468133561)

### path-034522

```text
(config)# do-exec show location geo-location static <cr>
```

Handler ` RVA 0xC916150 `；selector ` 6 `；EOL ` RVA 0x33B1FE98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-b08d012f1a2f604c](../../evidence/state_effects-sets-037.md#s-b08d012f1a2f604c)

### path-028451

```text
(config)# do-exec show location host <cr>
```

Handler ` RVA 0xC916150 `；selector ` 5 `；EOL ` RVA 0x33B202C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-026792

```text
(config)# do-exec show logging <cr>
```

Handler ` RVA 0xE0737A0 `；selector ` 0 `；EOL ` RVA 0x341908E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-028824

```text
(config)# do-exec show logging count <cr>
```

Handler ` RVA 0xE073560 `；selector ` 0 `；EOL ` RVA 0x34190370 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-028825

```text
(config)# do-exec show logging history <cr>
```

Handler ` RVA 0x123A1530 `；selector ` 0 `；EOL ` RVA 0x358327C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-034875

```text
(config)# do-exec show logging last <number:1..214748364> <cr>
```

Handler ` RVA 0xE0732A0 `；selector ` 0 `；EOL ` RVA 0x341900E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of lines。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-751e6c29ba38d6bd](../../evidence/parameters-sets-009.md#p-751e6c29ba38d6bd) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-029044

```text
(config)# do-exec show logging persistent <cr>
```

Handler ` RVA 0xE06B420 `；selector ` 0 `；EOL ` RVA 0x341909E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061257

```text
(config)# do-exec show logging persistent selector-url <url:dynamic> <cr>
```

Handler ` RVA 0xE06B420 `；selector ` 0 `；EOL ` RVA 0x341909E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0c00165580cce294](../../evidence/conditions-sets-005.md#c-0c00165580cce294) · [缺口 G-8667063bcf776b7e](../../evidence/gaps-sets-005.md#g-8667063bcf776b7e) · [参数 P-b9eebb8be0325b89](../../evidence/parameters-sets-014.md#p-b9eebb8be0325b89) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-028879

```text
(config)# do-exec show logging xml <cr>
```

Handler ` RVA 0xE0735C0 `；selector ` 0 `；EOL ` RVA 0x34190618 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027519

```text
(config)# do-exec show login <cr>
```

Handler ` RVA 0xCFD4180 `；selector ` 0 `；EOL ` RVA 0x33D76290 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-030971

```text
(config)# do-exec show login failures <cr>
```

Handler ` RVA 0xCFD4550 `；selector ` 0 `；EOL ` RVA 0x33D76268 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033894

```text
(config)# do-exec show mac address-table <cr>
```

Handler ` RVA 0x15E77B60 `；selector ` 4 `；EOL ` RVA 0x35E53230 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a5be5d1d376cb29e](../../evidence/conditions-sets-064.md#c-a5be5d1d376cb29e) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-043681

```text
(config)# do-exec show mac address-table aging-time <cr>
```

Handler ` RVA 0x15E77B60 `；selector ` 3 `；EOL ` RVA 0x35E552A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062224

```text
(config)# do-exec show mac address-table aging-time vlan <number:dynamic> <cr>
```

Handler ` RVA 0x15E77B60 `；selector ` 3 `；EOL ` RVA 0x35E552A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Enter VLAN Number。

[条件 C-9244b98384a9c6ce](../../evidence/conditions-sets-056.md#c-9244b98384a9c6ce) · [缺口 G-787c05fc803fb1eb](../../evidence/gaps-sets-005.md#g-787c05fc803fb1eb) · [参数 P-e07b2c11dc6d9323](../../evidence/parameters-sets-017.md#p-e07b2c11dc6d9323) · [状态效果 S-1b31bca9444092ed](../../evidence/state_effects-sets-006.md#s-1b31bca9444092ed)

### path-043677

```text
(config)# do-exec show mac address-table control-packet-learn <cr>
```

Handler ` RVA 0x15C438F0 `；selector ` 0 `；EOL ` RVA 0x35E555B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8d465482cc8555aa](../../evidence/conditions-sets-055.md#c-8d465482cc8555aa) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-043674

```text
(config)# do-exec show mac address-table count <cr>
```

Handler ` RVA 0x15E77B60 `；selector ` 1 `；EOL ` RVA 0x35E54988 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062225

```text
(config)# do-exec show mac address-table count vlan <number:dynamic> <cr>
```

Handler ` RVA 0x15E77B60 `；selector ` 1 `；EOL ` RVA 0x35E54988 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Enter VLAN Number。

[条件 C-3f7a79378b353453](../../evidence/conditions-sets-025.md#c-3f7a79378b353453) · [缺口 G-a9a55ea17283a96c](../../evidence/gaps-sets-006.md#g-a9a55ea17283a96c) · [参数 P-dd21a48cce17cc60](../../evidence/parameters-sets-017.md#p-dd21a48cce17cc60) · [状态效果 S-82d69445a92f91c2](../../evidence/state_effects-sets-028.md#s-82d69445a92f91c2)

### path-043693

```text
(config)# do-exec show mac address-table multicast <cr>
```

Handler ` RVA 0x15E77B60 `；selector ` 2 `；EOL ` RVA 0x35E54E40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6ec492d64dae399b](../../evidence/conditions-sets-043.md#c-6ec492d64dae399b) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062226

```text
(config)# do-exec show mac address-table multicast vlan <number:dynamic> <cr>
```

Handler ` RVA 0x15E77B60 `；selector ` 2 `；EOL ` RVA 0x35E54E40 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Enter VLAN number。

[条件 C-5de215bb4189d4fa](../../evidence/conditions-sets-037.md#c-5de215bb4189d4fa) · [缺口 G-26554fdadb9772f1](../../evidence/gaps-sets-002.md#g-26554fdadb9772f1) · [参数 P-f5628e2c3f8f39a3](../../evidence/parameters-sets-018.md#p-f5628e2c3f8f39a3) · [状态效果 S-422bbac5edb15682](../../evidence/state_effects-sets-014.md#s-422bbac5edb15682)

### path-061802

```text
(config)# do-exec show mac address-table vlan <number:dynamic> <cr>
```

Handler ` RVA 0x15E77B60 `；selector ` 4 `；EOL ` RVA 0x35E53230 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` VLAN number。

[条件 C-e9c6d0919f775cc7](../../evidence/conditions-sets-090.md#c-e9c6d0919f775cc7) · [缺口 G-8ae3023fdac65f1f](../../evidence/gaps-sets-005.md#g-8ae3023fdac65f1f) · [参数 P-1eb78cd3f04db503](../../evidence/parameters-sets-003.md#p-1eb78cd3f04db503) · [状态效果 S-e6eb0751fe1d5e0d](../../evidence/state_effects-sets-049.md#s-e6eb0751fe1d5e0d)

### path-027622

```text
(config)# do-exec show macdb <cr>
```

Handler ` RVA 0x1339C500 `；selector ` 0 `；EOL ` RVA 0x35A7C198 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6303aeb88c4cc0ab](../../evidence/conditions-sets-038.md#c-6303aeb88c4cc0ab) · [状态效果 S-8165b7738b271233](../../evidence/state_effects-sets-027.md#s-8165b7738b271233)

### path-060716

```text
(config)# do-exec show macdb <interface> <cr>
```

Handler ` RVA 0x1339C500 `；selector ` 0 `；EOL ` RVA 0x35A7C198 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-06848fcd69abc60d](../../evidence/conditions-sets-003.md#c-06848fcd69abc60d) · [缺口 G-419ff5c2a9c13f44](../../evidence/gaps-sets-003.md#g-419ff5c2a9c13f44) · [参数 P-159ea646247fdf76](../../evidence/parameters-sets-002.md#p-159ea646247fdf76) · [状态效果 S-8165b7738b271233](../../evidence/state_effects-sets-027.md#s-8165b7738b271233)

### path-030613

```text
(config)# do-exec show macsec hw <cr>
```

Handler ` RVA 0x16104EA0 `；selector ` 8 `；EOL ` RVA 0x35ED5AA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-afdfa7e3e5b668f0](../../evidence/conditions-sets-068.md#c-afdfa7e3e5b668f0) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-037259

```text
(config)# do-exec show macsec hw detail <cr>
```

Handler ` RVA 0x16104EA0 `；selector ` 9 `；EOL ` RVA 0x35ED5A78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-afdfa7e3e5b668f0](../../evidence/conditions-sets-068.md#c-afdfa7e3e5b668f0) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-030658

```text
(config)# do-exec show macsec mka-request-notify <cr>
```

Handler ` RVA 0x16104EA0 `；selector ` 6 `；EOL ` RVA 0x35ED62A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-afdfa7e3e5b668f0](../../evidence/conditions-sets-068.md#c-afdfa7e3e5b668f0) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-037338

```text
(config)# do-exec show macsec mka-request-notify clear <cr>
```

Handler ` RVA 0x16104EA0 `；selector ` 7 `；EOL ` RVA 0x35ED6280 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-afdfa7e3e5b668f0](../../evidence/conditions-sets-068.md#c-afdfa7e3e5b668f0) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-030602

```text
(config)# do-exec show macsec post <cr>
```

Handler ` RVA 0x16104EA0 `；selector ` 10 `；EOL ` RVA 0x35ED5F70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-afdfa7e3e5b668f0](../../evidence/conditions-sets-068.md#c-afdfa7e3e5b668f0) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061423

```text
(config)# do-exec show macsec statistics interface <interface> <cr>
```

Handler ` RVA 0x1610BE60 `；selector ` 2 `；EOL ` RVA 0x35ED7030 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1930ff738b2101d3](../../evidence/conditions-sets-010.md#c-1930ff738b2101d3) · [缺口 G-2f015fa58f5a94fa](../../evidence/gaps-sets-002.md#g-2f015fa58f5a94fa) · [参数 P-4310063a2b8ba071](../../evidence/parameters-sets-006.md#p-4310063a2b8ba071) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061427

```text
(config)# do-exec show macsec statistics interface <interface> <cr>
```

Handler ` RVA 0x16104EA0 `；selector ` 2 `；EOL ` RVA 0x35ED72D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5b755268efe03d96](../../evidence/conditions-sets-036.md#c-5b755268efe03d96) · [缺口 G-2f015fa58f5a94fa](../../evidence/gaps-sets-002.md#g-2f015fa58f5a94fa) · [参数 P-4310063a2b8ba071](../../evidence/parameters-sets-006.md#p-4310063a2b8ba071) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062905

```text
(config)# do-exec show macsec statistics interface <interface> rx-sci <hex-string> <cr>
```

Handler ` RVA 0x16104EA0 `；selector ` 5 `；EOL ` RVA 0x35ED78F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` hexstring ` 64-bit Hexadecimal Local Rx-SCI。

[条件 C-cf1ffee31eb94ca9](../../evidence/conditions-sets-080.md#c-cf1ffee31eb94ca9) · [缺口 G-2f47edcd6919fc57](../../evidence/gaps-sets-002.md#g-2f47edcd6919fc57) · [参数 P-51a640767f0406f1](../../evidence/parameters-sets-007.md#p-51a640767f0406f1) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062000

```text
(config)# do-exec show macsec statistics interface <interface> secy <cr>
```

Handler ` RVA 0x16104EA0 `；selector ` 4 `；EOL ` RVA 0x35ED7608 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-28ca4e05f7d8d964](../../evidence/conditions-sets-016.md#c-28ca4e05f7d8d964) · [缺口 G-2f015fa58f5a94fa](../../evidence/gaps-sets-002.md#g-2f015fa58f5a94fa) · [参数 P-4310063a2b8ba071](../../evidence/parameters-sets-006.md#p-4310063a2b8ba071) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061418

```text
(config)# do-exec show macsec status interface <interface> <cr>
```

Handler ` RVA 0x1610BE60 `；selector ` 1 `；EOL ` RVA 0x35ED68E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-742cb60ac53101ae](../../evidence/conditions-sets-045.md#c-742cb60ac53101ae) · [缺口 G-696d0ffad6951acc](../../evidence/gaps-sets-004.md#g-696d0ffad6951acc) · [参数 P-586f1128f4d7527e](../../evidence/parameters-sets-007.md#p-586f1128f4d7527e) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061424

```text
(config)# do-exec show macsec status interface <interface> <cr>
```

Handler ` RVA 0x16104EA0 `；selector ` 1 `；EOL ` RVA 0x35ED6B88 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0b3ec1acf2e17232](../../evidence/conditions-sets-005.md#c-0b3ec1acf2e17232) · [缺口 G-696d0ffad6951acc](../../evidence/gaps-sets-004.md#g-696d0ffad6951acc) · [参数 P-586f1128f4d7527e](../../evidence/parameters-sets-007.md#p-586f1128f4d7527e) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-030552

```text
(config)# do-exec show macsec summary <cr>
```

Handler ` RVA 0x16104EA0 `；selector ` 3 `；EOL ` RVA 0x35ED5768 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-afdfa7e3e5b668f0](../../evidence/conditions-sets-068.md#c-afdfa7e3e5b668f0) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033710

```text
(config)# do-exec show management event <cr>
```

Handler ` RVA 0x11304A30 `；selector ` 0 `；EOL ` RVA 0x35492578 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033698

```text
(config)# do-exec show management expression <cr>
```

Handler ` RVA 0x11324900 `；selector ` 0 `；EOL ` RVA 0x354922D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061605

```text
(config)# do-exec show mdns-sd cache interface <interface> <cr>
```

Handler ` RVA 0x142A9940 `；selector ` 0 `；EOL ` RVA 0x35D0C0A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f47f75ceb20f88f5](../../evidence/conditions-sets-094.md#c-f47f75ceb20f88f5) · [缺口 G-14082bd369a4f1df](../../evidence/gaps-sets-001.md#g-14082bd369a4f1df) · [参数 P-fde44b9b28cdd046](../../evidence/parameters-sets-019.md#p-fde44b9b28cdd046) · [状态效果 S-c918a21d7bc28175](../../evidence/state_effects-sets-043.md#s-c918a21d7bc28175)

### path-031964

```text
(config)# do-exec show mdns-sd location-filter <cr>
```

Handler ` RVA 0x1434AC40 `；selector ` 0 `；EOL ` RVA 0x35D324B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-635c80bcee8a2558](../../evidence/conditions-sets-038.md#c-635c80bcee8a2558) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032028

```text
(config)# do-exec show mdns-sd remote-cache <cr>
```

Handler ` RVA 0x142A9940 `；selector ` 0 `；EOL ` RVA 0x35D0C0A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-52e6aaa9c0a1bf5e](../../evidence/conditions-sets-032.md#c-52e6aaa9c0a1bf5e) · [状态效果 S-bccfa418a813bdd6](../../evidence/state_effects-sets-040.md#s-bccfa418a813bdd6)

### path-049073

```text
(config)# do-exec show mdns-sd sdg service-peer summary <cr>
```

Handler ` RVA 0x1434BF30 `；selector ` 0 `；EOL ` RVA 0x35D318A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-930c32ae4595de94](../../evidence/conditions-sets-057.md#c-930c32ae4595de94) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031912

```text
(config)# do-exec show mdns-sd service-definition <cr>
```

Handler ` RVA 0x1434A990 `；selector ` 0 `；EOL ` RVA 0x35D31488 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-930c32ae4595de94](../../evidence/conditions-sets-057.md#c-930c32ae4595de94) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031914

```text
(config)# do-exec show mdns-sd service-list <cr>
```

Handler ` RVA 0x1434A6E0 `；selector ` 0 `；EOL ` RVA 0x35D30FC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-930c32ae4595de94](../../evidence/conditions-sets-057.md#c-930c32ae4595de94) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031984

```text
(config)# do-exec show mdns-sd service-policy <cr>
```

Handler ` RVA 0x1434B0D0 `；selector ` 0 `；EOL ` RVA 0x35D31C28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-930c32ae4595de94](../../evidence/conditions-sets-057.md#c-930c32ae4595de94) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-049260

```text
(config)# do-exec show mdns-sd service-policy association vlan <cr>
```

Handler ` RVA 0x14345BD0 `；selector ` 0 `；EOL ` RVA 0x35D32088 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-930c32ae4595de94](../../evidence/conditions-sets-057.md#c-930c32ae4595de94) · [状态效果 S-9d7e26948d7f35fc](../../evidence/state_effects-sets-033.md#s-9d7e26948d7f35fc)

### path-061567

```text
(config)# do-exec show mdns-sd service-policy interface <interface> <cr>
```

Handler ` RVA 0x1434B0D0 `；selector ` 0 `；EOL ` RVA 0x35D31C28 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9319882f0b01ea80](../../evidence/conditions-sets-057.md#c-9319882f0b01ea80) · [缺口 G-fafa3094d604ffa6](../../evidence/gaps-sets-009.md#g-fafa3094d604ffa6) · [参数 P-31b4eb30fcdfc5f9](../../evidence/parameters-sets-004.md#p-31b4eb30fcdfc5f9) · [状态效果 S-a59499f765390c92](../../evidence/state_effects-sets-035.md#s-a59499f765390c92)

### path-031982

```text
(config)# do-exec show mdns-sd summary <cr>
```

Handler ` RVA 0x1434C470 `；selector ` 0 `；EOL ` RVA 0x35D32870 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-09b14fe806e05200](../../evidence/conditions-sets-004.md#c-09b14fe806e05200) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061570

```text
(config)# do-exec show mdns-sd summary interface <interface> <cr>
```

Handler ` RVA 0x1434C470 `；selector ` 0 `；EOL ` RVA 0x35D32870 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-064bf8394987f77b](../../evidence/conditions-sets-003.md#c-064bf8394987f77b) · [缺口 G-d017defdade76330](../../evidence/gaps-sets-007.md#g-d017defdade76330) · [参数 P-166fc60bbfbd6206](../../evidence/parameters-sets-002.md#p-166fc60bbfbd6206) · [状态效果 S-9a4b623266c15e13](../../evidence/state_effects-sets-033.md#s-9a4b623266c15e13)

### path-033607

```text
(config)# do-exec show media access-lists <cr>
```

Handler ` RVA 0xF290D50 `；selector ` 0 `；EOL ` RVA 0x345E7860 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061175

```text
(config)# do-exec show media access-lists <number:1..100> <cr>
```

Handler ` RVA 0xF290D50 `；selector ` 0 `；EOL ` RVA 0x345E7860 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [缺口 G-27d9c632b3d9c124](../../evidence/gaps-sets-002.md#g-27d9c632b3d9c124) · [参数 P-aa0d6b1fb8603c26](../../evidence/parameters-sets-013.md#p-aa0d6b1fb8603c26) · [状态效果 S-13b92d050b79421e](../../evidence/state_effects-sets-005.md#s-13b92d050b79421e)

### path-060751

```text
(config)# do-exec show memory <?general_pointer_number_action@55558973ddd8> <cr>
```

Handler ` RVA 0xE08F580 `；selector ` 0 `；EOL ` RVA 0x341E8370 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-55b15adaf3ecb554](../../evidence/conditions-sets-034.md#c-55b15adaf3ecb554) · [缺口 G-e6b66e6242ae1b30](../../evidence/gaps-sets-008.md#g-e6b66e6242ae1b30) · [状态效果 S-475bdfdf1fd46725](../../evidence/state_effects-sets-016.md#s-475bdfdf1fd46725)

### path-027795

```text
(config)# do-exec show memory <cr>
```

Handler ` RVA 0xE08F580 `；selector ` 0 `；EOL ` RVA 0x341E8370 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-947e644b7d960c4c](../../evidence/conditions-sets-057.md#c-947e644b7d960c4c) · [状态效果 S-475bdfdf1fd46725](../../evidence/state_effects-sets-016.md#s-475bdfdf1fd46725)

### path-043123

```text
(config)# do-exec show memory console reserved <cr>
```

Handler ` RVA 0xE043790 `；selector ` 0 `；EOL ` RVA 0x341E7F80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-baff48ed7d5c160c](../../evidence/conditions-sets-072.md#c-baff48ed7d5c160c) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-051607

```text
(config)# do-exec show memory debug incremental allocations <cr>
```

Handler ` RVA 0xE08DDF0 `；selector ` 0 `；EOL ` RVA 0x341E6E78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-051612

```text
(config)# do-exec show memory debug incremental leaks <cr>
```

Handler ` RVA 0xE08DED0 `；selector ` 0 `；EOL ` RVA 0x341E6BD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-051581

```text
(config)# do-exec show memory debug incremental status <cr>
```

Handler ` RVA 0xE08DAE0 `；selector ` 0 `；EOL ` RVA 0x341E68C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-043202

```text
(config)# do-exec show memory debug leaks <cr>
```

Handler ` RVA 0xE08D530 `；selector ` 0 `；EOL ` RVA 0x341E64B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-063016

```text
(config)# do-exec show memory debug references <?general_pointer_number_action@55558973b430> <?general_pointer_number_action@55558973b700> <cr>
```

Handler ` RVA 0xE08EE90 `；selector ` 0 `；EOL ` RVA 0x341E7788 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [缺口 G-8814d502d53d5620](../../evidence/gaps-sets-005.md#g-8814d502d53d5620) · [状态效果 S-5095b35a64681e5c](../../evidence/state_effects-sets-018.md#s-5095b35a64681e5c)

### path-051602

```text
(config)# do-exec show memory debug references dangling <cr>
```

Handler ` RVA 0xE08E430 `；selector ` 0 `；EOL ` RVA 0x341E7408 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-043161

```text
(config)# do-exec show memory debug unused <cr>
```

Handler ` RVA 0xE08E7A0 `；selector ` 0 `；EOL ` RVA 0x341E7120 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033629

```text
(config)# do-exec show memory events <cr>
```

Handler ` RVA 0xE092F40 `；selector ` 0 `；EOL ` RVA 0x341E9620 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a0b0f8a4d6934011](../../evidence/conditions-sets-062.md#c-a0b0f8a4d6934011) · [状态效果 S-219a92fe0f0dd809](../../evidence/state_effects-sets-008.md#s-219a92fe0f0dd809)

### path-043069

```text
(config)# do-exec show memory failures alloc <cr>
```

Handler ` RVA 0xE041EB0 `；selector ` 0 `；EOL ` RVA 0x341E60E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-043048

```text
(config)# do-exec show memory lite-chunks statistics <cr>
```

Handler ` RVA 0xE045320 `；selector ` 0 `；EOL ` RVA 0x341E5CA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-44956a0e2774ce4a](../../evidence/state_effects-sets-015.md#s-44956a0e2774ce4a)

### path-033585

```text
(config)# do-exec show memory overflow <cr>
```

Handler ` RVA 0xE03E380 `；selector ` 0 `；EOL ` RVA 0x341E8F48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a4b4354bcda928d4](../../evidence/conditions-sets-063.md#c-a4b4354bcda928d4) · [状态效果 S-475bdfdf1fd46725](../../evidence/state_effects-sets-016.md#s-475bdfdf1fd46725)

### path-043211

```text
(config)# do-exec show memory overflow poisoning <cr>
```

Handler ` RVA 0xE041FD0 `；selector ` 0 `；EOL ` RVA 0x341E8F20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8d6ce13b78f71f74](../../evidence/conditions-sets-055.md#c-8d6ce13b78f71f74) · [状态效果 S-475bdfdf1fd46725](../../evidence/state_effects-sets-016.md#s-475bdfdf1fd46725)

### path-043245

```text
(config)# do-exec show memory traceback <number:1..4294967294> <cr>
```

Handler ` RVA 0xE08FE60 `；selector ` 0 `；EOL ` RVA 0x341E8C18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Traceback ID。

[条件 C-ac9acce73626ad3e](../../evidence/conditions-sets-067.md#c-ac9acce73626ad3e) · [参数 P-7097096138595854](../../evidence/parameters-sets-009.md#p-7097096138595854) · [状态效果 S-ddcd4ef62d4e3be1](../../evidence/state_effects-sets-047.md#s-ddcd4ef62d4e3be1)

### path-043210

```text
(config)# do-exec show memory traceback exclusive <cr>
```

Handler ` RVA 0xE090130 `；selector ` 0 `；EOL ` RVA 0x341E86C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ac9acce73626ad3e](../../evidence/conditions-sets-067.md#c-ac9acce73626ad3e) · [状态效果 S-ddcd4ef62d4e3be1](../../evidence/state_effects-sets-047.md#s-ddcd4ef62d4e3be1)

### path-043230

```text
(config)# do-exec show memory traceback totals <cr>
```

Handler ` RVA 0xE08FC30 `；selector ` 0 `；EOL ` RVA 0x341E8970 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ac9acce73626ad3e](../../evidence/conditions-sets-067.md#c-ac9acce73626ad3e) · [状态效果 S-ddcd4ef62d4e3be1](../../evidence/state_effects-sets-047.md#s-ddcd4ef62d4e3be1)

### path-032554

```text
(config)# do-exec show mfib background <cr>
```

Handler ` RVA 0x119469C0 `；selector ` 0 `；EOL ` RVA 0x355ABB78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061104

```text
(config)# do-exec show mfib broker <?option@55558aa78120> <cr>
```

Handler ` RVA 0x11666350 `；selector ` 0 `；EOL ` RVA 0x35524220 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f1e345985645b454](../../evidence/conditions-sets-093.md#c-f1e345985645b454) · [缺口 G-3b32fb7d36f38c04](../../evidence/gaps-sets-003.md#g-3b32fb7d36f38c04) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032586

```text
(config)# do-exec show mfib error <cr>
```

Handler ` RVA 0x11957AF0 `；selector ` 0 `；EOL ` RVA 0x355AC3C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032756

```text
(config)# do-exec show mfib linecard <cr>
```

Handler ` RVA 0x116665C0 `；selector ` 0 `；EOL ` RVA 0x35523A78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-90486fb01072256f](../../evidence/conditions-sets-056.md#c-90486fb01072256f) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061120

```text
(config)# do-exec show mfib linecard <number:dynamic> <cr>
```

Handler ` RVA 0x116665C0 `；selector ` 0 `；EOL ` RVA 0x35523A78 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` linecard slot number。

[条件 C-91a92207fe0a7437](../../evidence/conditions-sets-056.md#c-91a92207fe0a7437) · [缺口 G-b506bfe1b35de677](../../evidence/gaps-sets-006.md#g-b506bfe1b35de677) · [参数 P-213fb2809ecc69be](../../evidence/parameters-sets-003.md#p-213fb2809ecc69be) · [状态效果 S-afe00e7dacf72751](../../evidence/state_effects-sets-037.md#s-afe00e7dacf72751)

### path-032652

```text
(config)# do-exec show mfib nsf <cr>
```

Handler ` RVA 0x1166AE70 `；selector ` 0 `；EOL ` RVA 0x35525D20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032589

```text
(config)# do-exec show mfib state <cr>
```

Handler ` RVA 0x11946400 `；selector ` 0 `；EOL ` RVA 0x355AC128 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061091

```text
(config)# do-exec show mfib table <?option@55558aaff498> <cr>
```

Handler ` RVA 0x1193FE70 `；selector ` 0 `；EOL ` RVA 0x355AB538 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-585f6cb191a5dc2a](../../evidence/conditions-sets-035.md#c-585f6cb191a5dc2a) · [缺口 G-92e12de43d092cac](../../evidence/gaps-sets-005.md#g-92e12de43d092cac) · [状态效果 S-fdaf8e72da0b98dc](../../evidence/state_effects-sets-054.md#s-fdaf8e72da0b98dc)

### path-032594

```text
(config)# do-exec show mfib table <cr>
```

Handler ` RVA 0x1193FE70 `；selector ` 0 `；EOL ` RVA 0x355AB538 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032549

```text
(config)# do-exec show mfib timers <cr>
```

Handler ` RVA 0x11957A10 `；selector ` 0 `；EOL ` RVA 0x355ABE18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-043360

```text
(config)# do-exec show mgmt-traffic control ipv4 <cr>
```

Handler ` RVA 0xFA036E0 `；selector ` 0 `；EOL ` RVA 0x347BB768 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b110161de9aa4496](../../evidence/conditions-sets-068.md#c-b110161de9aa4496) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027204

```text
(config)# do-exec show microcode <cr>
```

Handler ` RVA 0x162D0B10 `；selector ` 0 `；EOL ` RVA 0x35F6E858 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033931

```text
(config)# do-exec show mka default-policy <cr>
```

Handler ` RVA 0x160847F0 `；selector ` 1 `；EOL ` RVA 0x35EAED20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033943

```text
(config)# do-exec show mka keychains <cr>
```

Handler ` RVA 0x160847F0 `；selector ` 19 `；EOL ` RVA 0x35EB99D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033929

```text
(config)# do-exec show mka policy <cr>
```

Handler ` RVA 0x160847F0 `；selector ` 3 `；EOL ` RVA 0x35EB74E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-043808

```text
(config)# do-exec show mka policy <string> <cr>
```

Handler ` RVA 0x160847F0 `；selector ` 2 `；EOL ` RVA 0x35EAEF88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` MKA Policy NAME。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-78187144e42d11a1](../../evidence/parameters-sets-009.md#p-78187144e42d11a1) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033948

```text
(config)# do-exec show mka sessions <cr>
```

Handler ` RVA 0x160847F0 `；selector ` 4 `；EOL ` RVA 0x35EAF1F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-043793

```text
(config)# do-exec show mka sessions detail <cr>
```

Handler ` RVA 0x160847F0 `；selector ` 5 `；EOL ` RVA 0x35EB78C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061822

```text
(config)# do-exec show mka sessions interface <interface> <cr>
```

Handler ` RVA 0x160847F0 `；selector ` 11 `；EOL ` RVA 0x35EAF6C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c3c166b3786082c1](../../evidence/conditions-sets-076.md#c-c3c166b3786082c1) · [缺口 G-6d98c2f62a65ef9b](../../evidence/gaps-sets-004.md#g-6d98c2f62a65ef9b) · [参数 P-e35c2ea1188b6426](../../evidence/parameters-sets-017.md#p-e35c2ea1188b6426) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062231

```text
(config)# do-exec show mka sessions interface <interface> detail <cr>
```

Handler ` RVA 0x160847F0 `；selector ` 10 `；EOL ` RVA 0x35EB7FD0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a9bf77b2485322f2](../../evidence/conditions-sets-065.md#c-a9bf77b2485322f2) · [缺口 G-6d98c2f62a65ef9b](../../evidence/gaps-sets-004.md#g-6d98c2f62a65ef9b) · [参数 P-e35c2ea1188b6426](../../evidence/parameters-sets-017.md#p-e35c2ea1188b6426) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062462

```text
(config)# do-exec show mka sessions interface <interface> efp <number:1..16384> <cr>
```

Handler ` RVA 0x160847F0 `；selector ` 9 `；EOL ` RVA 0x35EB8628 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Service instance Id (default = 0。

[条件 C-f15f8fc6cbcafbdc](../../evidence/conditions-sets-093.md#c-f15f8fc6cbcafbdc) · [缺口 G-6d98c2f62a65ef9b](../../evidence/gaps-sets-004.md#g-6d98c2f62a65ef9b) · [参数 P-2affc90002b9c92b](../../evidence/parameters-sets-004.md#p-2affc90002b9c92b) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062584

```text
(config)# do-exec show mka sessions interface <interface> efp <number:1..16384> detail <cr>
```

Handler ` RVA 0x160847F0 `；selector ` 7 `；EOL ` RVA 0x35EB8380 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Service instance Id (default = 0。

[条件 C-f15f8fc6cbcafbdc](../../evidence/conditions-sets-093.md#c-f15f8fc6cbcafbdc) · [缺口 G-6d98c2f62a65ef9b](../../evidence/gaps-sets-004.md#g-6d98c2f62a65ef9b) · [参数 P-2affc90002b9c92b](../../evidence/parameters-sets-004.md#p-2affc90002b9c92b) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062460

```text
(config)# do-exec show mka sessions interface <interface> port-id <number:1..65535> <cr>
```

Handler ` RVA 0x160847F0 `；selector ` 8 `；EOL ` RVA 0x35EAF928 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` MKA Port ID。

[条件 C-a9bf77b2485322f2](../../evidence/conditions-sets-065.md#c-a9bf77b2485322f2) · [缺口 G-6d98c2f62a65ef9b](../../evidence/gaps-sets-004.md#g-6d98c2f62a65ef9b) · [参数 P-1c569572fad6a2ec](../../evidence/parameters-sets-003.md#p-1c569572fad6a2ec) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062583

```text
(config)# do-exec show mka sessions interface <interface> port-id <number:1..65535> detail <cr>
```

Handler ` RVA 0x160847F0 `；selector ` 6 `；EOL ` RVA 0x35EB7D40 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` MKA Port ID。

[条件 C-a9bf77b2485322f2](../../evidence/conditions-sets-065.md#c-a9bf77b2485322f2) · [缺口 G-6d98c2f62a65ef9b](../../evidence/gaps-sets-004.md#g-6d98c2f62a65ef9b) · [参数 P-1c569572fad6a2ec](../../evidence/parameters-sets-003.md#p-1c569572fad6a2ec) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061817

```text
(config)# do-exec show mka sessions local-sci <hex-string> <cr>
```

Handler ` RVA 0x160847F0 `；selector ` 13 `；EOL ` RVA 0x35EAF458 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` hexstring ` 64-bit Hexadecimal Local Tx-SCI。

[条件 C-07820310fe6a0f0d](../../evidence/conditions-sets-003.md#c-07820310fe6a0f0d) · [缺口 G-ccbbe146c8f7e3f7](../../evidence/gaps-sets-007.md#g-ccbbe146c8f7e3f7) · [参数 P-c6d8fc5a4b227b40](../../evidence/parameters-sets-015.md#p-c6d8fc5a4b227b40) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062230

```text
(config)# do-exec show mka sessions local-sci <hex-string> detail <cr>
```

Handler ` RVA 0x160847F0 `；selector ` 12 `；EOL ` RVA 0x35EB8980 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` hexstring ` 64-bit Hexadecimal Local Tx-SCI。

[条件 C-07820310fe6a0f0d](../../evidence/conditions-sets-003.md#c-07820310fe6a0f0d) · [缺口 G-ccbbe146c8f7e3f7](../../evidence/gaps-sets-007.md#g-ccbbe146c8f7e3f7) · [参数 P-c6d8fc5a4b227b40](../../evidence/parameters-sets-015.md#p-c6d8fc5a4b227b40) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033947

```text
(config)# do-exec show mka statistics <cr>
```

Handler ` RVA 0x160847F0 `；selector ` 14 `；EOL ` RVA 0x35EAFB90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061819

```text
(config)# do-exec show mka statistics interface <interface> <cr>
```

Handler ` RVA 0x160847F0 `；selector ` 15 `；EOL ` RVA 0x35EB8E28 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8bdfdc3a8ff894a8](../../evidence/conditions-sets-054.md#c-8bdfdc3a8ff894a8) · [缺口 G-32530677b08c936b](../../evidence/gaps-sets-002.md#g-32530677b08c936b) · [参数 P-1d60024297b2a892](../../evidence/parameters-sets-003.md#p-1d60024297b2a892) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062461

```text
(config)# do-exec show mka statistics interface <interface> efp <number:1..16384> <cr>
```

Handler ` RVA 0x160847F0 `；selector ` 16 `；EOL ` RVA 0x35EB9170 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Service instance Id (default = 0。

[条件 C-0b2d76ce9ac0e790](../../evidence/conditions-sets-005.md#c-0b2d76ce9ac0e790) · [缺口 G-32530677b08c936b](../../evidence/gaps-sets-002.md#g-32530677b08c936b) · [参数 P-865f0aa5f35f12bd](../../evidence/parameters-sets-010.md#p-865f0aa5f35f12bd) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061813

```text
(config)# do-exec show mka statistics local-sci <hex-string> <cr>
```

Handler ` RVA 0x160847F0 `；selector ` 17 `；EOL ` RVA 0x35EB9490 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` hexstring ` 64-bit Hexadecimal Local Tx-SCI。

[条件 C-0329aaf42e88c25a](../../evidence/conditions-sets-002.md#c-0329aaf42e88c25a) · [缺口 G-8be58cb7051a79d8](../../evidence/gaps-sets-005.md#g-8be58cb7051a79d8) · [参数 P-1a225bdeba90e881](../../evidence/parameters-sets-002.md#p-1a225bdeba90e881) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033937

```text
(config)# do-exec show mka summary <cr>
```

Handler ` RVA 0x160847F0 `；selector ` 18 `；EOL ` RVA 0x35EB9728 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-055724

```text
(config)# do-exec show mlrib common log event all <cr>
```

Handler ` RVA 0xC882F30 `；selector ` 0 `；EOL ` RVA 0x33B08CA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-cab4b9cce8e049dc](../../evidence/state_effects-sets-043.md#s-cab4b9cce8e049dc)

### path-040781

```text
(config)# do-exec show mlrib evpn mac <cr>
```

Handler ` RVA 0xC88D6E0 `；selector ` 0 `；EOL ` RVA 0x33B096A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-9cde2fe12d75578d](../../evidence/state_effects-sets-033.md#s-9cde2fe12d75578d)

### path-055740

```text
(config)# do-exec show mlrib evpn mac evi <number:1..65535> <cr>
```

Handler ` RVA 0xC88D6E0 `；selector ` 0 `；EOL ` RVA 0x33B096F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` EVI (BD) number。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-72f7666171291b63](../../evidence/parameters-sets-009.md#p-72f7666171291b63) · [状态效果 S-46f11db46c9ecb4c](../../evidence/state_effects-sets-016.md#s-46f11db46c9ecb4c)

### path-040747

```text
(config)# do-exec show mlrib evpn vtep <cr>
```

Handler ` RVA 0xC8B7E30 `；selector ` 0 `；EOL ` RVA 0x33B09118 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-055733

```text
(config)# do-exec show mlrib evpn vtep evi <number:1..65535> <cr>
```

Handler ` RVA 0xC8B7C70 `；selector ` 1 `；EOL ` RVA 0x33B09158 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` EVI (BD) number。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-7b24122338c65872](../../evidence/parameters-sets-010.md#p-7b24122338c65872) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-049925

```text
(config)# do-exec show mlrib layer2 clientdb producer <cr>
```

Handler ` RVA 0xC88CE90 `；selector ` 1 `；EOL ` RVA 0x33B08128 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3a9cd14679153664](../../evidence/conditions-sets-023.md#c-3a9cd14679153664) · [状态效果 S-45c89f10c9afb2ea](../../evidence/state_effects-sets-015.md#s-45c89f10c9afb2ea)

### path-055741

```text
(config)# do-exec show mlrib layer2 log event all <cr>
```

Handler ` RVA 0xC88C810 `；selector ` 0 `；EOL ` RVA 0x33B07CF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-d9fe17fe0b28a3d9](../../evidence/state_effects-sets-046.md#s-d9fe17fe0b28a3d9)

### path-062137

```text
(config)# do-exec show mlrib layer2 statistics producer <number:dynamic> <cr>
```

Handler ` RVA 0xC88CE90 `；selector ` 0 `；EOL ` RVA 0x33B07888 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` database index。

[条件 C-ed53a5c1fb3bd75a](../../evidence/conditions-sets-092.md#c-ed53a5c1fb3bd75a) · [缺口 G-649cc79cb638e9a0](../../evidence/gaps-sets-004.md#g-649cc79cb638e9a0) · [参数 P-8fa8097cef4b6f76](../../evidence/parameters-sets-011.md#p-8fa8097cef4b6f76) · [状态效果 S-add091c0fdc06b0b](../../evidence/state_effects-sets-037.md#s-add091c0fdc06b0b)

### path-055746

```text
(config)# do-exec show mlrib layer2 statistics producer all <cr>
```

Handler ` RVA 0xC88CE90 `；selector ` 0 `；EOL ` RVA 0x33B07888 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7011dc351d1aa92b](../../evidence/conditions-sets-043.md#c-7011dc351d1aa92b) · [状态效果 S-fe90912f934c53ed](../../evidence/state_effects-sets-054.md#s-fe90912f934c53ed)

### path-027713

```text
(config)# do-exec show modemcap <cr>
```

Handler ` RVA 0xFDCB170 `；selector ` 0 `；EOL ` RVA 0x348DBE78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-029656

```text
(config)# do-exec show monitor capture <cr>
```

Handler ` RVA 0x1334C6F0 `；selector ` 0 `；EOL ` RVA 0x35A6B8E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d1ced36e9a563bd2](../../evidence/conditions-sets-081.md#c-d1ced36e9a563bd2) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-045654

```text
(config)# do-exec show monitor capture <string> buffer <cr>
```

Handler ` RVA 0x1334BEC0 `；selector ` 0 `；EOL ` RVA 0x35A6B350 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of the Capture Point。

[条件 C-c282e217426596fa](../../evidence/conditions-sets-075.md#c-c282e217426596fa) · [参数 P-d4dc8e5eb9c77892](../../evidence/parameters-sets-016.md#p-d4dc8e5eb9c77892) · [状态效果 S-93ff10d4fa1b22e5](../../evidence/state_effects-sets-031.md#s-93ff10d4fa1b22e5)

### path-061323

```text
(config)# do-exec show monitor capture file <url:dynamic> <cr>
```

Handler ` RVA 0x1334BEC0 `；selector ` 0 `；EOL ` RVA 0x35A6B350 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e8917835b1b00cbc](../../evidence/conditions-sets-090.md#c-e8917835b1b00cbc) · [缺口 G-1bceb0f867046ca9](../../evidence/gaps-sets-001.md#g-1bceb0f867046ca9) · [参数 P-af9f827244486768](../../evidence/parameters-sets-013.md#p-af9f827244486768) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061927

```text
(config)# do-exec show monitor event-trace all-traces from-boot <number:dynamic> <cr>
```

Handler ` RVA 0xD2D0C90 `；selector ` 0 `；EOL ` RVA 0x33DF8BF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Time after boot (seconds)。

[条件 C-0a77ee926d408c04](../../evidence/conditions-sets-004.md#c-0a77ee926d408c04) · [缺口 G-223c802726cb85a2](../../evidence/gaps-sets-002.md#g-223c802726cb85a2) · [参数 P-f5f11bb517664118](../../evidence/parameters-sets-018.md#p-f5f11bb517664118) · [状态效果 S-29385670605505a2](../../evidence/state_effects-sets-009.md#s-29385670605505a2)

### path-035928

```text
(config)# do-exec show monitor event-trace continuous <cr>
```

Handler ` RVA 0xD2D0C90 `；selector ` 0 `；EOL ` RVA 0x33DF8BF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0c1d2f2f9e776058](../../evidence/conditions-sets-005.md#c-0c1d2f2f9e776058) · [状态效果 S-a22dfedc187f6080](../../evidence/state_effects-sets-034.md#s-a22dfedc187f6080)

### path-053733

```text
(config)# do-exec show monitor event-trace cpu-report handle <number:1..255> <cr>
```

Handler ` RVA 0xD6CB230 `；selector ` 0 `；EOL ` RVA 0x33ECCE38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` cpu report handle。

[条件 C-0c1d2f2f9e776058](../../evidence/conditions-sets-005.md#c-0c1d2f2f9e776058) · [参数 P-781105a9d1d9c313](../../evidence/parameters-sets-009.md#p-781105a9d1d9c313) · [状态效果 S-1d8a705887317339](../../evidence/state_effects-sets-007.md#s-1d8a705887317339)

### path-029689

```text
(config)# do-exec show monitor permit-list <cr>
```

Handler ` RVA 0xE4DD2A0 `；selector ` 0 `；EOL ` RVA 0x342DDE70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8e3ba91d81992bfa](../../evidence/conditions-sets-055.md#c-8e3ba91d81992bfa) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-036052

```text
(config)# do-exec show monitor session <number:1..1> <cr>
```

Handler ` RVA 0xE4C8B30 `；selector ` 0 `；EOL ` RVA 0x342D6D20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` SPAN session number。

[条件 C-fcdddb8f50b54d1c](../../evidence/conditions-sets-098.md#c-fcdddb8f50b54d1c) · [参数 P-0e6871d58042f146](../../evidence/parameters-sets-002.md#p-0e6871d58042f146) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-060846

```text
(config)# do-exec show monitor session <number:dynamic> <cr>
```

Handler ` RVA 0xE4C8B30 `；selector ` 0 `；EOL ` RVA 0x342D6D20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` SPAN session number。

[条件 C-481730b7a1884440](../../evidence/conditions-sets-028.md#c-481730b7a1884440) · [缺口 G-324a79e61605ec96](../../evidence/gaps-sets-002.md#g-324a79e61605ec96) · [参数 P-10c9bbb37d79f4a9](../../evidence/parameters-sets-002.md#p-10c9bbb37d79f4a9) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033269

```text
(config)# do-exec show mtm table <cr>
```

Handler ` RVA 0xD563CA0 `；selector ` 0 `；EOL ` RVA 0x33E83BE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-041636

```text
(config)# do-exec show mvpn ipv4 auto-discovery <cr>
```

Handler ` RVA 0xF95C950 `；selector ` 18 `；EOL ` RVA 0x3478EDB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b1fed8cd2bc122c3](../../evidence/conditions-sets-069.md#c-b1fed8cd2bc122c3) · [状态效果 S-61f6ae5b2611b83c](../../evidence/state_effects-sets-021.md#s-61f6ae5b2611b83c)

### path-041637

```text
(config)# do-exec show mvpn ipv4 auto-discovery <cr>
```

Handler ` RVA 0xF95C950 `；selector ` 19 `；EOL ` RVA 0x3478F030 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0f0ff2dfcbe610d7](../../evidence/conditions-sets-006.md#c-0f0ff2dfcbe610d7) · [状态效果 S-61f6ae5b2611b83c](../../evidence/state_effects-sets-021.md#s-61f6ae5b2611b83c)

### path-050409

```text
(config)# do-exec show mvpn ipv4 ingress-replication egress-info <cr>
```

Handler ` RVA 0xF95C950 `；selector ` 20 `；EOL ` RVA 0x3478F620 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3bf37d2ab7a25759](../../evidence/conditions-sets-023.md#c-3bf37d2ab7a25759) · [状态效果 S-23a2efc8e7225c5b](../../evidence/state_effects-sets-008.md#s-23a2efc8e7225c5b)

### path-061719

```text
(config)# do-exec show mvpn ipv4 leaf-information * <cr>
```

Handler ` RVA 0xF95C950 `；selector ` 18 `；EOL ` RVA 0x3478EDB0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-aae8335f2519659d](../../evidence/conditions-sets-066.md#c-aae8335f2519659d) · [缺口 G-c16ff738cb0771fd](../../evidence/gaps-sets-007.md#g-c16ff738cb0771fd) · [状态效果 S-80fa8dd7ac39f783](../../evidence/state_effects-sets-027.md#s-80fa8dd7ac39f783)

### path-061720

```text
(config)# do-exec show mvpn ipv4 leaf-information * <cr>
```

Handler ` RVA 0xF95C950 `；selector ` 19 `；EOL ` RVA 0x3478F030 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-82efae9aa553eb79](../../evidence/conditions-sets-051.md#c-82efae9aa553eb79) · [缺口 G-c16ff738cb0771fd](../../evidence/gaps-sets-007.md#g-c16ff738cb0771fd) · [状态效果 S-80fa8dd7ac39f783](../../evidence/state_effects-sets-027.md#s-80fa8dd7ac39f783)

### path-041656

```text
(config)# do-exec show mvpn ipv6 auto-discovery <cr>
```

Handler ` RVA 0xF95C950 `；selector ` 18 `；EOL ` RVA 0x3478FC40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a6845e0778b15944](../../evidence/conditions-sets-064.md#c-a6845e0778b15944) · [状态效果 S-4a60b9ac9d7cf426](../../evidence/state_effects-sets-016.md#s-4a60b9ac9d7cf426)

### path-041657

```text
(config)# do-exec show mvpn ipv6 auto-discovery <cr>
```

Handler ` RVA 0xF95C950 `；selector ` 19 `；EOL ` RVA 0x3478FEC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fac186c4a5999953](../../evidence/conditions-sets-097.md#c-fac186c4a5999953) · [状态效果 S-4a60b9ac9d7cf426](../../evidence/state_effects-sets-016.md#s-4a60b9ac9d7cf426)

### path-050423

```text
(config)# do-exec show mvpn ipv6 ingress-replication egress-info <cr>
```

Handler ` RVA 0xF95C950 `；selector ` 20 `；EOL ` RVA 0x347904B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5f5c9b278ef89362](../../evidence/conditions-sets-037.md#c-5f5c9b278ef89362) · [状态效果 S-64ed40257763c8e3](../../evidence/state_effects-sets-022.md#s-64ed40257763c8e3)

### path-061722

```text
(config)# do-exec show mvpn ipv6 leaf-information * <cr>
```

Handler ` RVA 0xF95C950 `；selector ` 18 `；EOL ` RVA 0x3478FC40 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c9fb5f829887309b](../../evidence/conditions-sets-078.md#c-c9fb5f829887309b) · [缺口 G-bbe9572c95551c55](../../evidence/gaps-sets-007.md#g-bbe9572c95551c55) · [状态效果 S-410d704240ab381c](../../evidence/state_effects-sets-014.md#s-410d704240ab381c)

### path-061723

```text
(config)# do-exec show mvpn ipv6 leaf-information * <cr>
```

Handler ` RVA 0xF95C950 `；selector ` 19 `；EOL ` RVA 0x3478FEC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-fc4aa7f0cef2f382](../../evidence/conditions-sets-097.md#c-fc4aa7f0cef2f382) · [缺口 G-bbe9572c95551c55](../../evidence/gaps-sets-007.md#g-bbe9572c95551c55) · [状态效果 S-410d704240ab381c](../../evidence/state_effects-sets-014.md#s-410d704240ab381c)

### path-061065

```text
(config)# do-exec show mvpn pe <?ipv4orv6_addr_action@555589ce2410> <cr>
```

Handler ` RVA 0xF95C950 `；selector ` 21 `；EOL ` RVA 0x3478E4A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [缺口 G-a9d34fa2fd853225](../../evidence/gaps-sets-006.md#g-a9d34fa2fd853225) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032483

```text
(config)# do-exec show mvpn replication <cr>
```

Handler ` RVA 0xF95C950 `；selector ` 17 `；EOL ` RVA 0x3478E0B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032453

```text
(config)# do-exec show mvpn vrfri <cr>
```

Handler ` RVA 0xF95C950 `；selector ` 22 `；EOL ` RVA 0x3478E7A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027643

```text
(config)# do-exec show mvr <cr>
```

Handler ` RVA 0xC3B3820 `；selector ` 0 `；EOL ` RVA 0x33A63B88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032105

```text
(config)# do-exec show mvr interface <cr>
```

Handler ` RVA 0xC3B3A90 `；selector ` 0 `；EOL ` RVA 0x33A62730 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a7129017d0ef1fe2](../../evidence/conditions-sets-064.md#c-a7129017d0ef1fe2) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061012

```text
(config)# do-exec show mvr interface <interface> <cr>
```

Handler ` RVA 0xC3B3D40 `；selector ` 0 `；EOL ` RVA 0x33A62798 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a2c2dff3a7a232b2](../../evidence/conditions-sets-063.md#c-a2c2dff3a7a232b2) · [缺口 G-04e7dd68ce243861](../../evidence/gaps-sets-001.md#g-04e7dd68ce243861) · [参数 P-e481c507b75881fd](../../evidence/parameters-sets-017.md#p-e481c507b75881fd) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061617

```text
(config)# do-exec show mvr interface <interface> members <cr>
```

Handler ` RVA 0xC3B3FD0 `；selector ` 0 `；EOL ` RVA 0x33A62770 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a2c2dff3a7a232b2](../../evidence/conditions-sets-063.md#c-a2c2dff3a7a232b2) · [缺口 G-04e7dd68ce243861](../../evidence/gaps-sets-001.md#g-04e7dd68ce243861) · [参数 P-e481c507b75881fd](../../evidence/parameters-sets-017.md#p-e481c507b75881fd) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032195

```text
(config)# do-exec show mvr members <cr>
```

Handler ` RVA 0xC3B4960 `；selector ` 0 `；EOL ` RVA 0x33A62F50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-dee25ebd444c6c22](../../evidence/conditions-sets-086.md#c-dee25ebd444c6c22) · [状态效果 S-4b0cf3712144d94f](../../evidence/state_effects-sets-016.md#s-4b0cf3712144d94f)

### path-061025

```text
(config)# do-exec show mvr members <interface> <cr>
```

Handler ` RVA 0xC3B4960 `；selector ` 0 `；EOL ` RVA 0x33A62F50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4841acf928802fc8](../../evidence/conditions-sets-028.md#c-4841acf928802fc8) · [缺口 G-51ec74fa297a213f](../../evidence/gaps-sets-003.md#g-51ec74fa297a213f) · [参数 P-3a966beffb09cab6](../../evidence/parameters-sets-005.md#p-3a966beffb09cab6) · [状态效果 S-4b0cf3712144d94f](../../evidence/state_effects-sets-016.md#s-4b0cf3712144d94f)

### path-032139

```text
(config)# do-exec show mvr receiver-ports <cr>
```

Handler ` RVA 0xC3B5230 `；selector ` 0 `；EOL ` RVA 0x33A63520 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0efe219025e463eb](../../evidence/conditions-sets-006.md#c-0efe219025e463eb) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061013

```text
(config)# do-exec show mvr receiver-ports <interface> <cr>
```

Handler ` RVA 0xC3B5230 `；selector ` 0 `；EOL ` RVA 0x33A63520 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-32f0fef0f089d914](../../evidence/conditions-sets-020.md#c-32f0fef0f089d914) · [缺口 G-e094003f25ed1289](../../evidence/gaps-sets-008.md#g-e094003f25ed1289) · [参数 P-3ef4ee31f8e8169d](../../evidence/parameters-sets-005.md#p-3ef4ee31f8e8169d) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032152

```text
(config)# do-exec show mvr source-ports <cr>
```

Handler ` RVA 0xC3B5700 `；selector ` 0 `；EOL ` RVA 0x33A638C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-562fd62f37d036f5](../../evidence/conditions-sets-034.md#c-562fd62f37d036f5) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061015

```text
(config)# do-exec show mvr source-ports <interface> <cr>
```

Handler ` RVA 0xC3B5700 `；selector ` 0 `；EOL ` RVA 0x33A638C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a6b355297683fab9](../../evidence/conditions-sets-064.md#c-a6b355297683fab9) · [缺口 G-d55c5670433bf325](../../evidence/gaps-sets-007.md#g-d55c5670433bf325) · [参数 P-8cf83f08caeaa25a](../../evidence/parameters-sets-011.md#p-8cf83f08caeaa25a) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-038237

```text
(config)# do-exec show nat46 mappings static <cr>
```

Handler ` RVA 0xD5D3450 `；selector ` 20 `；EOL ` RVA 0x33EA9158 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d7ebfdfe9125d011](../../evidence/conditions-sets-083.md#c-d7ebfdfe9125d011) · [状态效果 S-567b1a185d4a169e](../../evidence/state_effects-sets-019.md#s-567b1a185d4a169e)

### path-031180

```text
(config)# do-exec show nat46 pools <cr>
```

Handler ` RVA 0xD5D3450 `；selector ` 21 `；EOL ` RVA 0x33EA8E40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a263631b71c4cd09](../../evidence/conditions-sets-063.md#c-a263631b71c4cd09) · [状态效果 S-65afeb24b8cc86a5](../../evidence/state_effects-sets-022.md#s-65afeb24b8cc86a5)

### path-031081

```text
(config)# do-exec show nat46 prefix <cr>
```

Handler ` RVA 0xD5D3450 `；selector ` 19 `；EOL ` RVA 0x33EA8A38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-375ca03d5065d92d](../../evidence/conditions-sets-022.md#c-375ca03d5065d92d) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-038157

```text
(config)# do-exec show nat64 adjacency count <cr>
```

Handler ` RVA 0xD584480 `；selector ` 3 `；EOL ` RVA 0x33E86C20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8493ef5dc089b8bb](../../evidence/conditions-sets-051.md#c-8493ef5dc089b8bb) · [状态效果 S-031a8cf192d082f6](../../evidence/state_effects-sets-001.md#s-031a8cf192d082f6)

### path-031394

```text
(config)# do-exec show nat64 aliases <cr>
```

Handler ` RVA 0xD584480 `；selector ` 14 `；EOL ` RVA 0x33E88B98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-96d30ef8febedc89](../../evidence/conditions-sets-058.md#c-96d30ef8febedc89) · [状态效果 S-9c5d7e7e5135bea3](../../evidence/state_effects-sets-033.md#s-9c5d7e7e5135bea3)

### path-038342

```text
(config)# do-exec show nat64 ha status <cr>
```

Handler ` RVA 0xD584480 `；selector ` 4 `；EOL ` RVA 0x33E8B5B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-967712f29302a78c](../../evidence/conditions-sets-058.md#c-967712f29302a78c) · [状态效果 S-05e7ee9e44b66d31](../../evidence/state_effects-sets-002.md#s-05e7ee9e44b66d31)

### path-031299

```text
(config)# do-exec show nat64 limits <cr>
```

Handler ` RVA 0xD584480 `；selector ` 6 `；EOL ` RVA 0x33E88188 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9c667a97af1b1097](../../evidence/conditions-sets-060.md#c-9c667a97af1b1097) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031195

```text
(config)# do-exec show nat64 logging <cr>
```

Handler ` RVA 0xD584480 `；selector ` 11 `；EOL ` RVA 0x33E87890 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4d0094cb56a61482](../../evidence/conditions-sets-030.md#c-4d0094cb56a61482) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031181

```text
(config)# do-exec show nat64 map-e <cr>
```

Handler ` RVA 0xD584480 `；selector ` 17 `；EOL ` RVA 0x33E8C020 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3fe44f67080fd072](../../evidence/conditions-sets-025.md#c-3fe44f67080fd072) · [状态效果 S-df57bd43f3c7d5f4](../../evidence/state_effects-sets-047.md#s-df57bd43f3c7d5f4)

### path-031161

```text
(config)# do-exec show nat64 map-t <cr>
```

Handler ` RVA 0xD584480 `；selector ` 16 `；EOL ` RVA 0x33E8BC88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3fe44f67080fd072](../../evidence/conditions-sets-025.md#c-3fe44f67080fd072) · [状态效果 S-d0612c460d1fc48f](../../evidence/state_effects-sets-044.md#s-d0612c460d1fc48f)

### path-038932

```text
(config)# do-exec show nat64 mappings dynamic <cr>
```

Handler ` RVA 0xD584480 `；selector ` 12 `；EOL ` RVA 0x33E89038 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0d9bfea996bed24f](../../evidence/conditions-sets-006.md#c-0d9bfea996bed24f) · [状态效果 S-f3929a38c7b6a8b4](../../evidence/state_effects-sets-051.md#s-f3929a38c7b6a8b4)

### path-062360

```text
(config)# do-exec show nat64 mappings static key-port <number:1..65535> <number:dynamic> <cr>
```

Handler ` RVA 0xD584480 `；selector ` 12 `；EOL ` RVA 0x33E89038 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Port number (exact match if one port is given or lower port in range if two ports are given)；` unsigned_number_dynamic ` Upper port number in range。

[条件 C-74314bfb2a5f0329](../../evidence/conditions-sets-045.md#c-74314bfb2a5f0329) · [缺口 G-9879b98e2d1667f4](../../evidence/gaps-sets-006.md#g-9879b98e2d1667f4) · [参数 P-96772970adaa37cb](../../evidence/parameters-sets-012.md#p-96772970adaa37cb) · [状态效果 S-51244576bc81b289](../../evidence/state_effects-sets-018.md#s-51244576bc81b289)

### path-031449

```text
(config)# do-exec show nat64 pools <cr>
```

Handler ` RVA 0xD584480 `；selector ` 13 `；EOL ` RVA 0x33E885F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9ab8ac13fcc8e243](../../evidence/conditions-sets-060.md#c-9ab8ac13fcc8e243) · [状态效果 S-1f54dab7dcd2b372](../../evidence/state_effects-sets-007.md#s-1f54dab7dcd2b372)

### path-047448

```text
(config)# do-exec show nat64 prefix stateful global <cr>
```

Handler ` RVA 0xD584480 `；selector ` 2 `；EOL ` RVA 0x33E870C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ae98bce8a8886d98](../../evidence/conditions-sets-067.md#c-ae98bce8a8886d98) · [状态效果 S-d299d8f0dd5a94c3](../../evidence/state_effects-sets-045.md#s-d299d8f0dd5a94c3)

### path-062357

```text
(config)# do-exec show nat64 prefix stateful interfaces prefix <prefix:dynamic> <cr>
```

Handler ` RVA 0xD584480 `；selector ` 2 `；EOL ` RVA 0x33E870C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` Prefix/length to lookup。

[条件 C-ce2a525e973d68c8](../../evidence/conditions-sets-079.md#c-ce2a525e973d68c8) · [缺口 G-69883718dbdb4ee7](../../evidence/gaps-sets-004.md#g-69883718dbdb4ee7) · [参数 P-e6116d7a8f82c3bd](../../evidence/parameters-sets-017.md#p-e6116d7a8f82c3bd) · [状态效果 S-2b23850f444bf4b4](../../evidence/state_effects-sets-010.md#s-2b23850f444bf4b4)

### path-031150

```text
(config)# do-exec show nat64 provisioning <cr>
```

Handler ` RVA 0xD584480 `；selector ` 18 `；EOL ` RVA 0x33E8C2C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-264d818e3055b8d7](../../evidence/conditions-sets-015.md#c-264d818e3055b8d7) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031225

```text
(config)# do-exec show nat64 reconciliation <cr>
```

Handler ` RVA 0xD584480 `；selector ` 15 `；EOL ` RVA 0x33E8B890 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4a8bd35816266fe2](../../evidence/conditions-sets-029.md#c-4a8bd35816266fe2) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031274

```text
(config)# do-exec show nat64 replications <cr>
```

Handler ` RVA 0xD584480 `；selector ` 8 `；EOL ` RVA 0x33E87EA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9a2f15f9956ef689](../../evidence/conditions-sets-060.md#c-9a2f15f9956ef689) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031309

```text
(config)# do-exec show nat64 routes <cr>
```

Handler ` RVA 0xD584480 `；selector ` 1 `；EOL ` RVA 0x33E8C628 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3fe44f67080fd072](../../evidence/conditions-sets-025.md#c-3fe44f67080fd072) · [状态效果 S-277dde0f9939460f](../../evidence/state_effects-sets-009.md#s-277dde0f9939460f)

### path-061484

```text
(config)# do-exec show nat64 routes prefix <prefix:dynamic> <cr>
```

Handler ` RVA 0xD584480 `；selector ` 1 `；EOL ` RVA 0x33E8C628 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` Prefix/length to lookup。

[条件 C-fda4c31f25c02f2b](../../evidence/conditions-sets-098.md#c-fda4c31f25c02f2b) · [缺口 G-e81e158b0a1673b8](../../evidence/gaps-sets-008.md#g-e81e158b0a1673b8) · [参数 P-515eec98c654b214](../../evidence/parameters-sets-007.md#p-515eec98c654b214) · [状态效果 S-8dc218184120476a](../../evidence/state_effects-sets-030.md#s-8dc218184120476a)

### path-031275

```text
(config)# do-exec show nat64 services <cr>
```

Handler ` RVA 0xD584480 `；selector ` 9 `；EOL ` RVA 0x33E8B238 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e2d4d91491c4e5b7](../../evidence/conditions-sets-087.md#c-e2d4d91491c4e5b7) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031249

```text
(config)# do-exec show nat64 settings <cr>
```

Handler ` RVA 0xD584480 `；selector ` 10 `；EOL ` RVA 0x33E8AF50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-224b1ba4460d0170](../../evidence/conditions-sets-013.md#c-224b1ba4460d0170) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031212

```text
(config)# do-exec show nat64 statistics <cr>
```

Handler ` RVA 0xD584480 `；selector ` 0 `；EOL ` RVA 0x33E860C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4928fb406e746a97](../../evidence/conditions-sets-029.md#c-4928fb406e746a97) · [状态效果 S-25515dbcf4ce3e6d](../../evidence/state_effects-sets-008.md#s-25515dbcf4ce3e6d)

### path-061485

```text
(config)# do-exec show nat64 statistics interface <interface> <cr>
```

Handler ` RVA 0xD584480 `；selector ` 0 `；EOL ` RVA 0x33E860C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-fa76914531487f3b](../../evidence/conditions-sets-097.md#c-fa76914531487f3b) · [缺口 G-738ffcb9aa31c504](../../evidence/gaps-sets-004.md#g-738ffcb9aa31c504) · [参数 P-5bebd610f48dadea](../../evidence/parameters-sets-007.md#p-5bebd610f48dadea) · [状态效果 S-72f014404ab3f57a](../../evidence/state_effects-sets-024.md#s-72f014404ab3f57a)

### path-031248

```text
(config)# do-exec show nat64 timeouts <cr>
```

Handler ` RVA 0xD584480 `；selector ` 7 `；EOL ` RVA 0x33E87BB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-966fa665d55aecce](../../evidence/conditions-sets-058.md#c-966fa665d55aecce) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031463

```text
(config)# do-exec show nat64 translations <cr>
```

Handler ` RVA 0xD584480 `；selector ` 5 `；EOL ` RVA 0x33E8AB70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0dea75356faf42d1](../../evidence/conditions-sets-006.md#c-0dea75356faf42d1) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062931

```text
(config)# do-exec show nat64 translations time created newer-than <number:1..31> <?month_action@5555893de5c0> <number:1993..2035> <hh:mm:ss> <cr>
```

Handler ` RVA 0xD584480 `；selector ` 5 `；EOL ` RVA 0x33E8AB70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Day of the month；` unsigned_number ` Year；` time_hms ` Local Time (hh:mm:ss)。

[条件 C-2821397a8e0db15c](../../evidence/conditions-sets-016.md#c-2821397a8e0db15c) · [缺口 G-f1ee4ce37c3c3dd5](../../evidence/gaps-sets-008.md#g-f1ee4ce37c3c3dd5) · [参数 P-dceba5cc76543538](../../evidence/parameters-sets-017.md#p-dceba5cc76543538) · [状态效果 S-4e4178d8a4be311e](../../evidence/state_effects-sets-017.md#s-4e4178d8a4be311e)

