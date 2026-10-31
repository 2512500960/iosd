# configure · 依赖静态建槽的条件安装

[模式索引](README.md) · [总索引](../../README.md)

### static_slot_creation_candidates-000035

```text
(config)# atm max-sig-events <number:1..500> <cr>
```

Handler ` RVA 0xEE220F0 `；selector ` 44 `；EOL ` RVA 0x3443FB70 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of signalling events processed before suspend,         default-value is 10。

[候选注册 R-05beaa9c8337636c](../../evidence/conditional_registrations-sets-001.md#r-05beaa9c8337636c) · [条件 C-c8ce8784b93a73fb](../../evidence/conditions-sets-077.md#c-c8ce8784b93a73fb) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-0e2d72a4f7c9bd67](../../evidence/parameters-sets-002.md#p-0e2d72a4f7c9bd67) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### static_slot_creation_candidates-000113

```text
(config)# atm signalling mode conformance <cr>
```

Handler ` RVA 0xEE22650 `；selector ` 45 `；EOL ` RVA 0x34442560 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-0fa50957371de08d](../../evidence/conditional_registrations-sets-001.md#r-0fa50957371de08d) · [条件 C-58bec154157940ff](../../evidence/conditions-sets-035.md#c-58bec154157940ff) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### static_slot_creation_candidates-000001

```text
(config)# atm svc-drain-count <number:1..500> <cr>
```

Handler ` RVA 0xEE220F0 `；selector ` 43 `；EOL ` RVA 0x3443F560 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Maximum number of calls released per second 。

[候选注册 R-05beaa9c8337636c](../../evidence/conditional_registrations-sets-001.md#r-05beaa9c8337636c) · [条件 C-02716fa503b50264](../../evidence/conditions-sets-001.md#c-02716fa503b50264) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-a56026bdc8a2798d](../../evidence/parameters-sets-013.md#p-a56026bdc8a2798d) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### static_slot_creation_candidates-000002

```text
(config)# atm svc-max-conn-pending <number:1..800> <cr>
```

Handler ` RVA 0xEE220F0 `；selector ` 0 `；EOL ` RVA 0x3443F588 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Max number of connections pending。

[候选注册 R-05beaa9c8337636c](../../evidence/conditional_registrations-sets-001.md#r-05beaa9c8337636c) · [条件 C-b4004bd93a466a05](../../evidence/conditions-sets-070.md#c-b4004bd93a466a05) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-4c5f917dcdb26acf](../../evidence/parameters-sets-006.md#p-4c5f917dcdb26acf) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### static_slot_creation_candidates-000047

```text
(config)# crypto autovpn <string> <cr>
```

Handler ` RVA 0x165EB3F0 `；selector ` 1001 `；EOL ` RVA 0x35FA5610 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` AutoVPN configuration name。

[候选注册 R-021b51f4a25aecfb](../../evidence/conditional_registrations-sets-001.md#r-021b51f4a25aecfb) · [条件 C-ba931ba180d9406a](../../evidence/conditions-sets-072.md#c-ba931ba180d9406a) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-aae1ad4aaa211713](../../evidence/parameters-sets-013.md#p-aae1ad4aaa211713) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### static_slot_creation_candidates-000158

```text
(config)# crypto gkm group <string> <cr>
```

Handler ` RVA 0x190ABC00 `；selector ` 0 `；EOL ` RVA 0x3693F960 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Group Name。

[候选注册 R-1a9d19faad56856f](../../evidence/conditional_registrations-sets-001.md#r-1a9d19faad56856f) · [条件 C-238813cc939f2410](../../evidence/conditions-sets-014.md#c-238813cc939f2410) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-a044341d89aa4d0e](../../evidence/parameters-sets-012.md#p-a044341d89aa4d0e) · [状态效果 S-2e238f0004d097fc](../../evidence/state_effects-sets-010.md#s-2e238f0004d097fc)

### static_slot_creation_candidates-002716

```text
(config)# crypto ikev2 client flexvpn <string> <cr>
```

Handler ` RVA 0x18F32EB0 `；selector ` 0 `；EOL ` RVA 0x3691F948 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` IKEv2 FlexVPN name。

[候选注册 R-3d34f0a57fcb08d0](../../evidence/conditional_registrations-sets-001.md#r-3d34f0a57fcb08d0) · [条件 C-5761b20d2400936e](../../evidence/conditions-sets-034.md#c-5761b20d2400936e) · [缺口 G-5e46c6fdd249163b](../../evidence/gaps-sets-004.md#g-5e46c6fdd249163b) · [参数 P-bbfea873ebec719c](../../evidence/parameters-sets-014.md#p-bbfea873ebec719c) · [状态效果 S-ecdf33bd9148e922](../../evidence/state_effects-sets-050.md#s-ecdf33bd9148e922)

### static_slot_creation_candidates-000088

```text
(config)# crypto ikev2 cluster <cr>
```

Handler ` RVA 0x18F46500 `；selector ` 0 `；EOL ` RVA 0x36926318 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-da17ebc2c1235053](../../evidence/conditional_registrations-sets-002.md#r-da17ebc2c1235053) · [条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### static_slot_creation_candidates-000080

```text
(config)# crypto ipsec profile <cr>
```

Handler ` RVA 0x18D84B00 `；selector ` 0 `；EOL ` RVA 0x368B6120 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-fd610a05a528d9d4](../../evidence/conditional_registrations-sets-003.md#r-fd610a05a528d9d4) · [条件 C-8bdefaacc79f9a0f](../../evidence/conditions-sets-054.md#c-8bdefaacc79f9a0f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### static_slot_creation_candidates-000052

```text
(config)# crypto logging ikev2 <cr>
```

Handler ` RVA 0x18E92A80 `；selector ` 36 `；EOL ` RVA 0x368E8D10 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-b9e52741f78d3911](../../evidence/conditional_registrations-sets-002.md#r-b9e52741f78d3911) · [条件 C-7fd696fdd43ae129](../../evidence/conditions-sets-050.md#c-7fd696fdd43ae129) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### static_slot_creation_candidates-000205

```text
(config)# crypto map <string> <number:1..65535> <cr>
```

Handler ` RVA 0x18D25DC0 `；selector ` 0 `；EOL ` RVA 0x36895738 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Crypto map tag；` unsigned_number ` Sequence to insert into crypto map entry。

[候选注册 R-46e28176dd8b9ed9](../../evidence/conditional_registrations-sets-001.md#r-46e28176dd8b9ed9) · [条件 C-3de65596b4ee6dfb](../../evidence/conditions-sets-024.md#c-3de65596b4ee6dfb) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-db2fcd8c994d9dc8](../../evidence/parameters-sets-016.md#p-db2fcd8c994d9dc8) · [状态效果 S-71c7eb802b6fd6b1](../../evidence/state_effects-sets-024.md#s-71c7eb802b6fd6b1)

### static_slot_creation_candidates-001868

```text
(config)# crypto map <string> client configuration address initiate <cr>
```

Handler ` RVA 0x18D25DC0 `；selector ` 0 `；EOL ` RVA 0x36894430 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Crypto map tag。

[候选注册 R-b3a6b4c3c845910d](../../evidence/conditional_registrations-sets-002.md#r-b3a6b4c3c845910d) · [条件 C-397fc1361de89b12](../../evidence/conditions-sets-022.md#c-397fc1361de89b12) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-719031f943998497](../../evidence/parameters-sets-009.md#p-719031f943998497) · [状态效果 S-f1534d33712f8b5c](../../evidence/state_effects-sets-051.md#s-f1534d33712f8b5c)

### static_slot_creation_candidates-000495

```text
(config)# crypto map <string> gdoi fail-close <cr>
```

Handler ` RVA 0x18D25DC0 `；selector ` 0 `；EOL ` RVA 0x36894FA8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Crypto map tag。

[候选注册 R-b3a6b4c3c845910d](../../evidence/conditional_registrations-sets-002.md#r-b3a6b4c3c845910d) · [条件 C-91188381714de86a](../../evidence/conditions-sets-056.md#c-91188381714de86a) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-719031f943998497](../../evidence/parameters-sets-009.md#p-719031f943998497) · [状态效果 S-ea55d34d8bd04258](../../evidence/state_effects-sets-050.md#s-ea55d34d8bd04258)

### static_slot_creation_candidates-000558

```text
(config)# crypto map <string> isakmp-profile <string> <cr>
```

Handler ` RVA 0x18D25DC0 `；selector ` 0 `；EOL ` RVA 0x36894C88 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Crypto map tag；` string ` Name of the isakmp profile。

[候选注册 R-b3a6b4c3c845910d](../../evidence/conditional_registrations-sets-002.md#r-b3a6b4c3c845910d) · [条件 C-ec86f60ead2a4fea](../../evidence/conditions-sets-091.md#c-ec86f60ead2a4fea) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-92a0b4ea435317b7](../../evidence/parameters-sets-011.md#p-92a0b4ea435317b7) · [状态效果 S-700a548d7855a568](../../evidence/state_effects-sets-024.md#s-700a548d7855a568)

### static_slot_creation_candidates-002621

```text
(config)# crypto map <string> local-address <interface> <cr>
```

Handler ` RVA 0x18D25DC0 `；selector ` 0 `；EOL ` RVA 0x36893E10 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Crypto map tag。

[候选注册 R-b3a6b4c3c845910d](../../evidence/conditional_registrations-sets-002.md#r-b3a6b4c3c845910d) · [条件 C-f449552bc9b06d6a](../../evidence/conditions-sets-094.md#c-f449552bc9b06d6a) · [缺口 G-e9feb0c0e338e5aa](../../evidence/gaps-sets-008.md#g-e9feb0c0e338e5aa) · [参数 P-2c802e8d1cfd3bd9](../../evidence/parameters-sets-004.md#p-2c802e8d1cfd3bd9) · [状态效果 S-cf21a92fc37c8236](../../evidence/state_effects-sets-044.md#s-cf21a92fc37c8236)

### static_slot_creation_candidates-002483

```text
(config)# crypto map <string> redundancy replay-interval inbound <number:0..1000> outbound <number:1000..100000> <cr>
```

Handler ` RVA 0x18D25DC0 `；selector ` 0 `；EOL ` RVA 0x36895448 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Crypto map tag；` unsigned_number ` Inbound interval in packets；` unsigned_number ` Outbound interval in packets。

[候选注册 R-b3a6b4c3c845910d](../../evidence/conditional_registrations-sets-002.md#r-b3a6b4c3c845910d) · [条件 C-9b07b1d71dc1e209](../../evidence/conditions-sets-060.md#c-9b07b1d71dc1e209) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-28d1438a1458858a](../../evidence/parameters-sets-004.md#p-28d1438a1458858a) · [状态效果 S-20e77e52e3f5821f](../../evidence/state_effects-sets-007.md#s-20e77e52e3f5821f)

### static_slot_creation_candidates-000036

```text
(config)# default atm max-sig-events <cr>
```

Handler ` RVA 0xEE220F0 `；selector ` 44 `；EOL ` RVA 0x3443FB70 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-05beaa9c8337636c](../../evidence/conditional_registrations-sets-001.md#r-05beaa9c8337636c) · [条件 C-7a7dd19d6cdcb3a6](../../evidence/conditions-sets-048.md#c-7a7dd19d6cdcb3a6) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### static_slot_creation_candidates-000311

```text
(config)# default atm signalling mode conformance <cr>
```

Handler ` RVA 0xEE22650 `；selector ` 45 `；EOL ` RVA 0x34442560 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-0fa50957371de08d](../../evidence/conditional_registrations-sets-001.md#r-0fa50957371de08d) · [条件 C-58bec154157940ff](../../evidence/conditions-sets-035.md#c-58bec154157940ff) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### static_slot_creation_candidates-000008

```text
(config)# default atm svc-drain-count <number:1..500> <cr>
```

Handler ` RVA 0xEE220F0 `；selector ` 43 `；EOL ` RVA 0x3443F560 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Maximum number of calls released per second 。

[候选注册 R-05beaa9c8337636c](../../evidence/conditional_registrations-sets-001.md#r-05beaa9c8337636c) · [条件 C-0d6aa44ec3cd0b95](../../evidence/conditions-sets-005.md#c-0d6aa44ec3cd0b95) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-a56026bdc8a2798d](../../evidence/parameters-sets-013.md#p-a56026bdc8a2798d) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### static_slot_creation_candidates-000010

```text
(config)# default atm svc-max-conn-pending <number:1..800> <cr>
```

Handler ` RVA 0xEE220F0 `；selector ` 0 `；EOL ` RVA 0x3443F588 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Max number of connections pending。

[候选注册 R-05beaa9c8337636c](../../evidence/conditional_registrations-sets-001.md#r-05beaa9c8337636c) · [条件 C-1c3be85fe7337893](../../evidence/conditions-sets-011.md#c-1c3be85fe7337893) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-4c5f917dcdb26acf](../../evidence/parameters-sets-006.md#p-4c5f917dcdb26acf) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### static_slot_creation_candidates-000053

```text
(config)# default crypto autovpn <cr>
```

Handler ` RVA 0x165EB3F0 `；selector ` 1001 `；EOL ` RVA 0x35FA5610 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-021b51f4a25aecfb](../../evidence/conditional_registrations-sets-001.md#r-021b51f4a25aecfb) · [条件 C-587c2fe7203f2888](../../evidence/conditions-sets-035.md#c-587c2fe7203f2888) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### static_slot_creation_candidates-000353

```text
(config)# default crypto gkm group <string> <cr>
```

Handler ` RVA 0x190ABC00 `；selector ` 0 `；EOL ` RVA 0x3693F960 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Group Name。

[候选注册 R-1a9d19faad56856f](../../evidence/conditional_registrations-sets-001.md#r-1a9d19faad56856f) · [条件 C-238813cc939f2410](../../evidence/conditions-sets-014.md#c-238813cc939f2410) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-a044341d89aa4d0e](../../evidence/parameters-sets-012.md#p-a044341d89aa4d0e) · [状态效果 S-63579948de0a1d0b](../../evidence/state_effects-sets-021.md#s-63579948de0a1d0b)

### static_slot_creation_candidates-000223

```text
(config)# default crypto ikev2 cluster <cr>
```

Handler ` RVA 0x18F46500 `；selector ` 0 `；EOL ` RVA 0x36926318 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-da17ebc2c1235053](../../evidence/conditional_registrations-sets-002.md#r-da17ebc2c1235053) · [条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### static_slot_creation_candidates-000196

```text
(config)# default crypto ipsec profile <cr>
```

Handler ` RVA 0x18D84B00 `；selector ` 0 `；EOL ` RVA 0x368B6120 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-fd610a05a528d9d4](../../evidence/conditional_registrations-sets-003.md#r-fd610a05a528d9d4) · [条件 C-8bdefaacc79f9a0f](../../evidence/conditions-sets-054.md#c-8bdefaacc79f9a0f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### static_slot_creation_candidates-000140

```text
(config)# default crypto logging ikev2 <cr>
```

Handler ` RVA 0x18E92A80 `；selector ` 36 `；EOL ` RVA 0x368E8D10 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-b9e52741f78d3911](../../evidence/conditional_registrations-sets-002.md#r-b9e52741f78d3911) · [条件 C-4e15ca0f0fc34c56](../../evidence/conditions-sets-031.md#c-4e15ca0f0fc34c56) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### static_slot_creation_candidates-001888

```text
(config)# default crypto map <string> client authentication list <cr>
```

Handler ` RVA 0x18D25DC0 `；selector ` 0 `；EOL ` RVA 0x36894430 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Crypto map tag。

[候选注册 R-b3a6b4c3c845910d](../../evidence/conditional_registrations-sets-002.md#r-b3a6b4c3c845910d) · [条件 C-da59fc64db826a7f](../../evidence/conditions-sets-084.md#c-da59fc64db826a7f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-719031f943998497](../../evidence/parameters-sets-009.md#p-719031f943998497) · [状态效果 S-3a61ce6a1679cde0](../../evidence/state_effects-sets-013.md#s-3a61ce6a1679cde0)

### static_slot_creation_candidates-001115

```text
(config)# default crypto map <string> gdoi fail-close <cr>
```

Handler ` RVA 0x18D25DC0 `；selector ` 0 `；EOL ` RVA 0x36894FA8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Crypto map tag。

[候选注册 R-b3a6b4c3c845910d](../../evidence/conditional_registrations-sets-002.md#r-b3a6b4c3c845910d) · [条件 C-91188381714de86a](../../evidence/conditions-sets-056.md#c-91188381714de86a) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-719031f943998497](../../evidence/parameters-sets-009.md#p-719031f943998497) · [状态效果 S-602e72faec681218](../../evidence/state_effects-sets-021.md#s-602e72faec681218)

### static_slot_creation_candidates-000570

```text
(config)# default crypto map <string> isakmp-profile <cr>
```

Handler ` RVA 0x18D25DC0 `；selector ` 0 `；EOL ` RVA 0x36894C88 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Crypto map tag。

[候选注册 R-b3a6b4c3c845910d](../../evidence/conditional_registrations-sets-002.md#r-b3a6b4c3c845910d) · [条件 C-f46faf29155e3ca4](../../evidence/conditions-sets-094.md#c-f46faf29155e3ca4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-719031f943998497](../../evidence/parameters-sets-009.md#p-719031f943998497) · [状态效果 S-99539eb5a1f89b1b](../../evidence/state_effects-sets-033.md#s-99539eb5a1f89b1b)

### static_slot_creation_candidates-000483

```text
(config)# default crypto map <string> local-address <cr>
```

Handler ` RVA 0x18D25DC0 `；selector ` 0 `；EOL ` RVA 0x36893E10 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Crypto map tag。

[候选注册 R-b3a6b4c3c845910d](../../evidence/conditional_registrations-sets-002.md#r-b3a6b4c3c845910d) · [条件 C-fdd37e13ea5409fe](../../evidence/conditions-sets-098.md#c-fdd37e13ea5409fe) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-719031f943998497](../../evidence/parameters-sets-009.md#p-719031f943998497) · [状态效果 S-7a229a45efb0df65](../../evidence/state_effects-sets-026.md#s-7a229a45efb0df65)

### static_slot_creation_candidates-002539

```text
(config)# default crypto map <string> redundancy replay-interval inbound <number:0..1000> outbound <number:1000..100000> <cr>
```

Handler ` RVA 0x18D25DC0 `；selector ` 0 `；EOL ` RVA 0x36895448 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Crypto map tag；` unsigned_number ` Inbound interval in packets；` unsigned_number ` Outbound interval in packets。

[候选注册 R-b3a6b4c3c845910d](../../evidence/conditional_registrations-sets-002.md#r-b3a6b4c3c845910d) · [条件 C-9b07b1d71dc1e209](../../evidence/conditions-sets-060.md#c-9b07b1d71dc1e209) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-28d1438a1458858a](../../evidence/parameters-sets-004.md#p-28d1438a1458858a) · [状态效果 S-24e3a7ddcfc679a5](../../evidence/state_effects-sets-008.md#s-24e3a7ddcfc679a5)

### static_slot_creation_candidates-000301

```text
(config)# default dial-peer cor custom <cr>
```

Handler ` RVA 0x1BCE7770 `；selector ` 0 `；EOL ` RVA 0x37048978 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-0cae083882896d7c](../../evidence/conditional_registrations-sets-001.md#r-0cae083882896d7c) · [条件 C-c54686a4dfa8e49e](../../evidence/conditions-sets-076.md#c-c54686a4dfa8e49e) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### static_slot_creation_candidates-000303

```text
(config)# default dial-peer cor list <cr>
```

Handler ` RVA 0x1BCE7330 `；selector ` 0 `；EOL ` RVA 0x37048CE0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-0cae083882896d7c](../../evidence/conditional_registrations-sets-001.md#r-0cae083882896d7c) · [条件 C-a535317878b9529a](../../evidence/conditions-sets-064.md#c-a535317878b9529a) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### static_slot_creation_candidates-000109

```text
(config)# default dial-peer group <cr>
```

Handler ` RVA 0x1BD8F7F0 `；selector ` 0 `；EOL ` RVA 0x371DB8A8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-4b1131926812dbaa](../../evidence/conditional_registrations-sets-001.md#r-4b1131926812dbaa) · [条件 C-69bc9acfca20cf31](../../evidence/conditions-sets-041.md#c-69bc9acfca20cf31) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-5e0458f0d7835d05](../../evidence/state_effects-sets-020.md#s-5e0458f0d7835d05)

### static_slot_creation_candidates-001843

```text
(config)# default do-exec clear crypto ikev2 client flexvpn <cr>
```

Handler ` RVA 0x18F34C60 `；selector ` 0 `；EOL ` RVA 0x3691FCB0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-fbbb38046aef1e7e](../../evidence/conditional_registrations-sets-003.md#r-fbbb38046aef1e7e) · [条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### static_slot_creation_candidates-002305

```text
(config)# default do-exec clear crypto ikev2 client flexvpn <string> <cr>
```

Handler ` RVA 0x18F34C60 `；selector ` 1 `；EOL ` RVA 0x3691FC88 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Crypto IKEv2 FlexVPN name。

[候选注册 R-fbbb38046aef1e7e](../../evidence/conditional_registrations-sets-003.md#r-fbbb38046aef1e7e) · [条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-07853f5fe0552deb](../../evidence/parameters-sets-001.md#p-07853f5fe0552deb) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### static_slot_creation_candidates-000914

```text
(config)# default do-exec clear dapr border-router statistics <cr>
```

Handler ` RVA 0x1AE594B0 `；selector ` 0 `；EOL ` RVA 0x36E5B278 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-2ddb3d590f1cef8b](../../evidence/conditional_registrations-sets-001.md#r-2ddb3d590f1cef8b) · [条件 C-81a31e518d1bfabf](../../evidence/conditions-sets-050.md#c-81a31e518d1bfabf) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### static_slot_creation_candidates-001777

```text
(config)# default do-exec clear dapr route-manager border-router <address> <cr>
```

Handler ` RVA 0x1AE59510 `；selector ` 2 `；EOL ` RVA 0x36E5B840 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` BR address。

[候选注册 R-5926085f59fc1f1f](../../evidence/conditional_registrations-sets-001.md#r-5926085f59fc1f1f) · [条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-f6db5d971c2d6d63](../../evidence/parameters-sets-018.md#p-f6db5d971c2d6d63) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### static_slot_creation_candidates-000922

```text
(config)# default do-exec clear dapr route-manager statistics <cr>
```

Handler ` RVA 0x1AE59510 `；selector ` 1 `；EOL ` RVA 0x36E5B530 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-5926085f59fc1f1f](../../evidence/conditional_registrations-sets-001.md#r-5926085f59fc1f1f) · [条件 C-e4f74bd5f25e6af6](../../evidence/conditions-sets-088.md#c-e4f74bd5f25e6af6) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### static_slot_creation_candidates-002466

```text
(config)# default do-exec clear domain default border channel smart-probe statistics <cr>
```

Handler ` RVA 0x17FA1890 `；selector ` 2 `；EOL ` RVA 0x36679FE0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-eb9b5360be5212bd](../../evidence/conditional_registrations-sets-003.md#r-eb9b5360be5212bd) · [条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-a36e7511aeb33a85](../../evidence/state_effects-sets-035.md#s-a36e7511aeb33a85)

### static_slot_creation_candidates-001793

```text
(config)# default do-exec clear domain default border statistics <cr>
```

Handler ` RVA 0x17FA1890 `；selector ` 1 `；EOL ` RVA 0x3667A278 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-eb9b5360be5212bd](../../evidence/conditional_registrations-sets-003.md#r-eb9b5360be5212bd) · [条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c2d8c45d3d915612](../../evidence/state_effects-sets-041.md#s-c2d8c45d3d915612)

### static_slot_creation_candidates-002465

```text
(config)# default do-exec clear domain default master site-prefix <address> <number:1..32> <cr>
```

Handler ` RVA 0x17F2CB00 `；selector ` 3 `；EOL ` RVA 0x36679B88 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IP address of site-prefix；` unsigned_number ` Specify site-prefix mask length。

[候选注册 R-ef84bbf9e13afdef](../../evidence/conditional_registrations-sets-003.md#r-ef84bbf9e13afdef) · [条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-fab18ec361f585cf](../../evidence/parameters-sets-019.md#p-fab18ec361f585cf) · [状态效果 S-3eb8ac2496cfdaf4](../../evidence/state_effects-sets-014.md#s-3eb8ac2496cfdaf4)

### static_slot_creation_candidates-001782

```text
(config)# default do-exec clear domain default master statistics <cr>
```

Handler ` RVA 0x17F2CB00 `；selector ` 1 `；EOL ` RVA 0x366795B8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-ef84bbf9e13afdef](../../evidence/conditional_registrations-sets-003.md#r-ef84bbf9e13afdef) · [条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-3eb8ac2496cfdaf4](../../evidence/state_effects-sets-014.md#s-3eb8ac2496cfdaf4)

### static_slot_creation_candidates-001792

```text
(config)# default do-exec clear domain default master traffic-classes <cr>
```

Handler ` RVA 0x17F2CB00 `；selector ` 2 `；EOL ` RVA 0x36679860 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-ef84bbf9e13afdef](../../evidence/conditional_registrations-sets-003.md#r-ef84bbf9e13afdef) · [条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-3eb8ac2496cfdaf4](../../evidence/state_effects-sets-014.md#s-3eb8ac2496cfdaf4)

### static_slot_creation_candidates-000930

```text
(config)# default do-exec clear otv isis lspfull <cr>
```

Handler ` RVA 0xFD360F0 `；selector ` 0 `；EOL ` RVA 0x3610C4F0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-22f82a39c49fc3c3](../../evidence/conditional_registrations-sets-001.md#r-22f82a39c49fc3c3) · [条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-0584d1efa93a22a6](../../evidence/state_effects-sets-002.md#s-0584d1efa93a22a6)

### static_slot_creation_candidates-000975

```text
(config)# default do-exec clear otv isis neighbors <cr>
```

Handler ` RVA 0x16B82830 `；selector ` 48 `；EOL ` RVA 0x3610CCC0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-22f82a39c49fc3c3](../../evidence/conditional_registrations-sets-001.md#r-22f82a39c49fc3c3) · [条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-7dac41e4dfb5aac7](../../evidence/state_effects-sets-027.md#s-7dac41e4dfb5aac7)

### static_slot_creation_candidates-001827

```text
(config)# default do-exec clear otv isis rib redistribution <cr>
```

Handler ` RVA 0x16B82830 `；selector ` 47 `；EOL ` RVA 0x3610C8C8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-22f82a39c49fc3c3](../../evidence/conditional_registrations-sets-001.md#r-22f82a39c49fc3c3) · [条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-aa9d00d697d66982](../../evidence/state_effects-sets-036.md#s-aa9d00d697d66982)

### static_slot_creation_candidates-001845

```text
(config)# default do-exec clear sbc <string> sbe blacklist <cr>
```

Handler ` RVA 0x1D4A7DE0 `；selector ` 8 `；EOL ` RVA 0x37597F40 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` SBC name。

[候选注册 R-c61afd87d23d2874](../../evidence/conditional_registrations-sets-002.md#r-c61afd87d23d2874) · [条件 C-198b7a44c602dea3](../../evidence/conditions-sets-010.md#c-198b7a44c602dea3) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-a5ec91b0fe780235](../../evidence/parameters-sets-013.md#p-a5ec91b0fe780235) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### static_slot_creation_candidates-002472

```text
(config)# default do-exec clear sbc <string> sbe blacklist ipv4 <address> <cr>
```

Handler ` RVA 0x1D4A7DE0 `；selector ` 7 `；EOL ` RVA 0x37596D48 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` SBC name；` address ` Blacklisted IPv4 address。

[候选注册 R-c61afd87d23d2874](../../evidence/conditional_registrations-sets-002.md#r-c61afd87d23d2874) · [条件 C-035dc5d3e3744787](../../evidence/conditions-sets-002.md#c-035dc5d3e3744787) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-93e2ab09267e2fc8](../../evidence/parameters-sets-011.md#p-93e2ab09267e2fc8) · [状态效果 S-e69ddbb6eda620bb](../../evidence/state_effects-sets-049.md#s-e69ddbb6eda620bb)

### static_slot_creation_candidates-002559

```text
(config)# default do-exec clear sbc <string> sbe blacklist ipv4 <address> TCP <number:0..65535> <cr>
```

Handler ` RVA 0x1D4A7DE0 `；selector ` 5 `；EOL ` RVA 0x37596DD8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` SBC name；` address ` Blacklisted IPv4 address；` unsigned_number ` Blacklisted port number。

[候选注册 R-c61afd87d23d2874](../../evidence/conditional_registrations-sets-002.md#r-c61afd87d23d2874) · [条件 C-035dc5d3e3744787](../../evidence/conditions-sets-002.md#c-035dc5d3e3744787) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-143b06dfbaa40241](../../evidence/parameters-sets-002.md#p-143b06dfbaa40241) · [状态效果 S-e69ddbb6eda620bb](../../evidence/state_effects-sets-049.md#s-e69ddbb6eda620bb)

### static_slot_creation_candidates-002563

```text
(config)# default do-exec clear sbc <string> sbe blacklist ipv4 <address> UDP <number:0..65535> <cr>
```

Handler ` RVA 0x1D4A7DE0 `；selector ` 6 `；EOL ` RVA 0x375970A0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` SBC name；` address ` Blacklisted IPv4 address；` unsigned_number ` Blacklisted port number。

[候选注册 R-c61afd87d23d2874](../../evidence/conditional_registrations-sets-002.md#r-c61afd87d23d2874) · [条件 C-035dc5d3e3744787](../../evidence/conditions-sets-002.md#c-035dc5d3e3744787) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-2292cdeee2d5b2c2](../../evidence/parameters-sets-003.md#p-2292cdeee2d5b2c2) · [状态效果 S-e69ddbb6eda620bb](../../evidence/state_effects-sets-049.md#s-e69ddbb6eda620bb)

### static_slot_creation_candidates-002474

```text
(config)# default do-exec clear sbc <string> sbe blacklist ipv6 <address> <cr>
```

Handler ` RVA 0x1D4A7DE0 `；selector ` 4 `；EOL ` RVA 0x37597688 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` SBC name；` address ` Blacklisted IPv6 address。

[候选注册 R-c61afd87d23d2874](../../evidence/conditional_registrations-sets-002.md#r-c61afd87d23d2874) · [条件 C-035dc5d3e3744787](../../evidence/conditions-sets-002.md#c-035dc5d3e3744787) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-5ab92c4f819b1604](../../evidence/parameters-sets-007.md#p-5ab92c4f819b1604) · [状态效果 S-81d7656697db1cf4](../../evidence/state_effects-sets-028.md#s-81d7656697db1cf4)

### static_slot_creation_candidates-002562

```text
(config)# default do-exec clear sbc <string> sbe blacklist ipv6 <address> TCP <number:0..65535> <cr>
```

Handler ` RVA 0x1D4A7DE0 `；selector ` 2 `；EOL ` RVA 0x37597718 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` SBC name；` address ` Blacklisted IPv6 address；` unsigned_number ` Blacklisted port number。

[候选注册 R-c61afd87d23d2874](../../evidence/conditional_registrations-sets-002.md#r-c61afd87d23d2874) · [条件 C-035dc5d3e3744787](../../evidence/conditions-sets-002.md#c-035dc5d3e3744787) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-47feb26e690a6a86](../../evidence/parameters-sets-006.md#p-47feb26e690a6a86) · [状态效果 S-81d7656697db1cf4](../../evidence/state_effects-sets-028.md#s-81d7656697db1cf4)

### static_slot_creation_candidates-002565

```text
(config)# default do-exec clear sbc <string> sbe blacklist ipv6 <address> UDP <number:0..65535> <cr>
```

Handler ` RVA 0x1D4A7DE0 `；selector ` 3 `；EOL ` RVA 0x375979E0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` SBC name；` address ` Blacklisted IPv6 address；` unsigned_number ` Blacklisted port number。

[候选注册 R-c61afd87d23d2874](../../evidence/conditional_registrations-sets-002.md#r-c61afd87d23d2874) · [条件 C-035dc5d3e3744787](../../evidence/conditions-sets-002.md#c-035dc5d3e3744787) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-af04a6489bb540d3](../../evidence/parameters-sets-013.md#p-af04a6489bb540d3) · [状态效果 S-81d7656697db1cf4](../../evidence/state_effects-sets-028.md#s-81d7656697db1cf4)

### static_slot_creation_candidates-001847

```text
(config)# default do-exec clear sbc <string> sbe cac-policy-set-stats <cr>
```

Handler ` RVA 0x1D4A7000 `；selector ` 14 `；EOL ` RVA 0x37598BF0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` SBC name。

[候选注册 R-c61afd87d23d2874](../../evidence/conditional_registrations-sets-002.md#r-c61afd87d23d2874) · [条件 C-035dc5d3e3744787](../../evidence/conditions-sets-002.md#c-035dc5d3e3744787) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-a5ec91b0fe780235](../../evidence/parameters-sets-013.md#p-a5ec91b0fe780235) · [状态效果 S-3c53cee048151d1e](../../evidence/state_effects-sets-013.md#s-3c53cee048151d1e)

### static_slot_creation_candidates-002315

```text
(config)# default do-exec clear sbc <string> sbe call <number:0..2147483647> <cr>
```

Handler ` RVA 0x1D4A8FA0 `；selector ` 0 `；EOL ` RVA 0x3759A5D8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` SBC name；` unsigned_number ` Call number。

[候选注册 R-c61afd87d23d2874](../../evidence/conditional_registrations-sets-002.md#r-c61afd87d23d2874) · [条件 C-035dc5d3e3744787](../../evidence/conditions-sets-002.md#c-035dc5d3e3744787) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-747a6f39008b5c03](../../evidence/parameters-sets-009.md#p-747a6f39008b5c03) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### static_slot_creation_candidates-001861

```text
(config)# default do-exec clear sbc <string> sbe call-policy-set-stats <cr>
```

Handler ` RVA 0x1D4A7000 `；selector ` 13 `；EOL ` RVA 0x37598FD8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` SBC name。

[候选注册 R-c61afd87d23d2874](../../evidence/conditional_registrations-sets-002.md#r-c61afd87d23d2874) · [条件 C-035dc5d3e3744787](../../evidence/conditions-sets-002.md#c-035dc5d3e3744787) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-a5ec91b0fe780235](../../evidence/parameters-sets-013.md#p-a5ec91b0fe780235) · [状态效果 S-9976ed457ba57847](../../evidence/state_effects-sets-033.md#s-9976ed457ba57847)

### static_slot_creation_candidates-001801

```text
(config)# default do-exec clear sbc <string> sbe call-rate-stats <cr>
```

Handler ` RVA 0x1D4A7000 `；selector ` 12 `；EOL ` RVA 0x375982B8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` SBC name。

[候选注册 R-c61afd87d23d2874](../../evidence/conditional_registrations-sets-002.md#r-c61afd87d23d2874) · [条件 C-035dc5d3e3744787](../../evidence/conditions-sets-002.md#c-035dc5d3e3744787) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-a5ec91b0fe780235](../../evidence/parameters-sets-013.md#p-a5ec91b0fe780235) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### static_slot_creation_candidates-001867

```text
(config)# default do-exec clear sbc <string> sbe call-stats <cr>
```

Handler ` RVA 0x1D4A7000 `；selector ` 17 `；EOL ` RVA 0x375961E0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` SBC name。

[候选注册 R-c61afd87d23d2874](../../evidence/conditional_registrations-sets-002.md#r-c61afd87d23d2874) · [条件 C-035dc5d3e3744787](../../evidence/conditions-sets-002.md#c-035dc5d3e3744787) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-a5ec91b0fe780235](../../evidence/parameters-sets-013.md#p-a5ec91b0fe780235) · [状态效果 S-f6fa8e64adcf5c50](../../evidence/state_effects-sets-052.md#s-f6fa8e64adcf5c50)

### static_slot_creation_candidates-002467

```text
(config)# default do-exec clear sbc <string> sbe call-stats reject-threshold memory <cr>
```

Handler ` RVA 0x1D4A7000 `；selector ` 31 `；EOL ` RVA 0x37596578 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` SBC name。

[候选注册 R-c61afd87d23d2874](../../evidence/conditional_registrations-sets-002.md#r-c61afd87d23d2874) · [条件 C-035dc5d3e3744787](../../evidence/conditions-sets-002.md#c-035dc5d3e3744787) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-a5ec91b0fe780235](../../evidence/parameters-sets-013.md#p-a5ec91b0fe780235) · [状态效果 S-3d38bfbd0d0c8181](../../evidence/state_effects-sets-013.md#s-3d38bfbd0d0c8181)

### static_slot_creation_candidates-002319

```text
(config)# default do-exec clear sbc <string> sbe li cc <cr>
```

Handler ` RVA 0x1D4A9720 `；selector ` 0 `；EOL ` RVA 0x3759AD30 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` SBC name。

[候选注册 R-c61afd87d23d2874](../../evidence/conditional_registrations-sets-002.md#r-c61afd87d23d2874) · [条件 C-c02edb968d6b5392](../../evidence/conditions-sets-074.md#c-c02edb968d6b5392) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-a5ec91b0fe780235](../../evidence/parameters-sets-013.md#p-a5ec91b0fe780235) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### static_slot_creation_candidates-002487

```text
(config)# default do-exec clear sbc <string> sbe li intercept standby <cr>
```

Handler ` RVA 0x1D4A9790 `；selector ` 0 `；EOL ` RVA 0x3759B018 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` SBC name。

[候选注册 R-c61afd87d23d2874](../../evidence/conditional_registrations-sets-002.md#r-c61afd87d23d2874) · [条件 C-7d3b2d5f404f645e](../../evidence/conditions-sets-049.md#c-7d3b2d5f404f645e) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-a5ec91b0fe780235](../../evidence/parameters-sets-013.md#p-a5ec91b0fe780235) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### static_slot_creation_candidates-002540

```text
(config)# default do-exec clear sbc <string> sbe radius-client authentication radius-server-stats <string> <cr>
```

Handler ` RVA 0x1D4A9520 `；selector ` 21 `；EOL ` RVA 0x3759A270 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` SBC name；` string ` RADIUS server name。

[候选注册 R-c61afd87d23d2874](../../evidence/conditional_registrations-sets-002.md#r-c61afd87d23d2874) · [条件 C-035dc5d3e3744787](../../evidence/conditions-sets-002.md#c-035dc5d3e3744787) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-a34dd099eeb7f587](../../evidence/parameters-sets-012.md#p-a34dd099eeb7f587) · [状态效果 S-384b8ee32bb5cc5e](../../evidence/state_effects-sets-012.md#s-384b8ee32bb5cc5e)

### static_slot_creation_candidates-002477

```text
(config)# default do-exec clear sbc <string> sbe radius-client-stats accounting <string> <cr>
```

Handler ` RVA 0x1D4A9330 `；selector ` 18 `；EOL ` RVA 0x37599BC8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` SBC name；` string ` RADIUS client name。

[候选注册 R-c61afd87d23d2874](../../evidence/conditional_registrations-sets-002.md#r-c61afd87d23d2874) · [条件 C-035dc5d3e3744787](../../evidence/conditions-sets-002.md#c-035dc5d3e3744787) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-a9374d510d308ef1](../../evidence/parameters-sets-013.md#p-a9374d510d308ef1) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### static_slot_creation_candidates-002312

```text
(config)# default do-exec clear sbc <string> sbe radius-client-stats authentication <cr>
```

Handler ` RVA 0x1D4A9330 `；selector ` 19 `；EOL ` RVA 0x37599E48 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` SBC name。

[候选注册 R-c61afd87d23d2874](../../evidence/conditional_registrations-sets-002.md#r-c61afd87d23d2874) · [条件 C-035dc5d3e3744787](../../evidence/conditions-sets-002.md#c-035dc5d3e3744787) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-a5ec91b0fe780235](../../evidence/parameters-sets-013.md#p-a5ec91b0fe780235) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### static_slot_creation_candidates-002303

```text
(config)# default do-exec clear sbc <string> sbe script-set-stats <number:1..2147483647> <cr>
```

Handler ` RVA 0x1D4A7000 `；selector ` 15 `；EOL ` RVA 0x37598640 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` SBC name；` unsigned_number ` script-set number。

[候选注册 R-c61afd87d23d2874](../../evidence/conditional_registrations-sets-002.md#r-c61afd87d23d2874) · [条件 C-035dc5d3e3744787](../../evidence/conditions-sets-002.md#c-035dc5d3e3744787) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-3839ddf07560001f](../../evidence/parameters-sets-005.md#p-3839ddf07560001f) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### static_slot_creation_candidates-002528

```text
(config)# default do-exec clear sbc <string> sbe script-set-stats <number:1..2147483647> editor-stats <string> <cr>
```

Handler ` RVA 0x1D4A7000 `；selector ` 16 `；EOL ` RVA 0x37598680 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` SBC name；` unsigned_number ` script-set number；` string ` The name of the editor to reset stats for。

[候选注册 R-c61afd87d23d2874](../../evidence/conditional_registrations-sets-002.md#r-c61afd87d23d2874) · [条件 C-035dc5d3e3744787](../../evidence/conditions-sets-002.md#c-035dc5d3e3744787) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-810dd16c0bf30c01](../../evidence/parameters-sets-010.md#p-810dd16c0bf30c01) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### static_slot_creation_candidates-002316

```text
(config)# default do-exec clear sbc <string> sbe sip statistics <cr>
```

Handler ` RVA 0x1D4A7000 `；selector ` 25 `；EOL ` RVA 0x37599438 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` SBC name。

[候选注册 R-c61afd87d23d2874](../../evidence/conditional_registrations-sets-002.md#r-c61afd87d23d2874) · [条件 C-035dc5d3e3744787](../../evidence/conditions-sets-002.md#c-035dc5d3e3744787) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-a5ec91b0fe780235](../../evidence/parameters-sets-013.md#p-a5ec91b0fe780235) · [状态效果 S-67b35f7d44bce101](../../evidence/state_effects-sets-022.md#s-67b35f7d44bce101)

### static_slot_creation_candidates-002535

```text
(config)# default do-exec clear sbc <string> sbe sip subscriber aor <string> <cr>
```

Handler ` RVA 0x1D4A9800 `；selector ` 26 `；EOL ` RVA 0x37599848 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` SBC name；` string ` Address-Of-Record (AOR) for subscriber。

[候选注册 R-c61afd87d23d2874](../../evidence/conditional_registrations-sets-002.md#r-c61afd87d23d2874) · [条件 C-035dc5d3e3744787](../../evidence/conditions-sets-002.md#c-035dc5d3e3744787) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-fd05ba9d52cf37ca](../../evidence/parameters-sets-019.md#p-fd05ba9d52cf37ca) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### static_slot_creation_candidates-001909

```text
(config)# default do-exec clear sbc <string> sbe transcoding-stats <cr>
```

Handler ` RVA 0x1D4A99F0 `；selector ` 35 `；EOL ` RVA 0x3759A940 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` SBC name。

[候选注册 R-c61afd87d23d2874](../../evidence/conditional_registrations-sets-002.md#r-c61afd87d23d2874) · [条件 C-035dc5d3e3744787](../../evidence/conditions-sets-002.md#c-035dc5d3e3744787) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-a5ec91b0fe780235](../../evidence/parameters-sets-013.md#p-a5ec91b0fe780235) · [状态效果 S-fb61e76f39a48110](../../evidence/state_effects-sets-053.md#s-fb61e76f39a48110)

### static_slot_creation_candidates-001787

```text
(config)# default do-exec clear sbc h248 bac call-contexts <cr>
```

Handler ` RVA 0x1CEA72F0 `；selector ` 0 `；EOL ` RVA 0x37551F80 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-246783fba16bc8a1](../../evidence/conditional_registrations-sets-001.md#r-246783fba16bc8a1) · [条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### static_slot_creation_candidates-002461

```text
(config)# default do-exec clear sbc h248 bac call-contexts correlator <number:1..4294967295> <cr>
```

Handler ` RVA 0x1CEA7380 `；selector ` 0 `；EOL ` RVA 0x37551FE8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Call correlator。

[候选注册 R-246783fba16bc8a1](../../evidence/conditional_registrations-sets-001.md#r-246783fba16bc8a1) · [条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-5133c682344c3239](../../evidence/parameters-sets-007.md#p-5133c682344c3239) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### static_slot_creation_candidates-001774

```text
(config)# default do-exec clear sbc h248 bac iad-sessions <cr>
```

Handler ` RVA 0x1CEA71D0 `；selector ` 0 `；EOL ` RVA 0x37551730 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-246783fba16bc8a1](../../evidence/conditional_registrations-sets-001.md#r-246783fba16bc8a1) · [条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### static_slot_creation_candidates-002459

```text
(config)# default do-exec clear sbc h248 bac iad-sessions correlator <number:0..4294967295> <cr>
```

Handler ` RVA 0x1CEA7410 `；selector ` 0 `；EOL ` RVA 0x37551798 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` iad correlator。

[候选注册 R-246783fba16bc8a1](../../evidence/conditional_registrations-sets-001.md#r-246783fba16bc8a1) · [条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-16d8209b9b716d43](../../evidence/parameters-sets-002.md#p-16d8209b9b716d43) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### static_slot_creation_candidates-001773

```text
(config)# default do-exec clear sbc h248 bac transaction-sessions <cr>
```

Handler ` RVA 0x1CEA7260 `；selector ` 0 `；EOL ` RVA 0x37551C70 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-246783fba16bc8a1](../../evidence/conditional_registrations-sets-001.md#r-246783fba16bc8a1) · [条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### static_slot_creation_candidates-000925

```text
(config)# default do-exec clear voice accounting method <cr>
```

Handler ` RVA 0x1BF77C90 `；selector ` 0 `；EOL ` RVA 0x371F1168 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-06ad988ecd7f4441](../../evidence/conditional_registrations-sets-001.md#r-06ad988ecd7f4441) · [条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### static_slot_creation_candidates-000920

```text
(config)# default do-exec clear voice dsp error <cr>
```

Handler ` RVA 0x1BD76A70 `；selector ` 0 `；EOL ` RVA 0x37186690 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-4aa19f8118f9a992](../../evidence/conditional_registrations-sets-001.md#r-4aa19f8118f9a992) · [条件 C-ff5258c502c1a137](../../evidence/conditions-sets-098.md#c-ff5258c502c1a137) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### static_slot_creation_candidates-000919

```text
(config)# default do-exec clear voice fac statistics <cr>
```

Handler ` RVA 0x172443C0 `；selector ` 0 `；EOL ` RVA 0x3633A270 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-773380ac74671fb7](../../evidence/conditional_registrations-sets-002.md#r-773380ac74671fb7) · [条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### static_slot_creation_candidates-000909

```text
(config)# default do-exec clear voice lpcor statistics <cr>
```

Handler ` RVA 0x17244280 `；selector ` 0 `；EOL ` RVA 0x36339F98 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-773380ac74671fb7](../../evidence/conditional_registrations-sets-002.md#r-773380ac74671fb7) · [条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### static_slot_creation_candidates-000910

```text
(config)# default do-exec clear voice moh-group statistics <cr>
```

Handler ` RVA 0x1BDBEAA0 `；selector ` 0 `；EOL ` RVA 0x365BE128 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-29defe7467e6dc67](../../evidence/conditional_registrations-sets-001.md#r-29defe7467e6dc67) · [条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### static_slot_creation_candidates-000911

```text
(config)# default do-exec clear voice phone-proxy all-sessions <cr>
```

Handler ` RVA 0x1DA036A0 `；selector ` 0 `；EOL ` RVA 0x3779DC20 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-07c0bd23cb21a910](../../evidence/conditional_registrations-sets-001.md#r-07c0bd23cb21a910) · [条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### static_slot_creation_candidates-000933

```text
(config)# default do-exec clear voice register attempted-registrations <cr>
```

Handler ` RVA 0x17B78B40 `；selector ` 2 `；EOL ` RVA 0x365CC330 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-1136174a7fd2703b](../../evidence/conditional_registrations-sets-001.md#r-1136174a7fd2703b) · [条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### static_slot_creation_candidates-002289

```text
(config)# default do-exec clear voice register attempted-registrations ip <address> <cr>
```

Handler ` RVA 0x17B78B40 `；selector ` 1 `；EOL ` RVA 0x365CC370 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IP address in dotted-decimal notation。

[候选注册 R-1136174a7fd2703b](../../evidence/conditional_registrations-sets-001.md#r-1136174a7fd2703b) · [条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-cbc366392b4673a8](../../evidence/parameters-sets-015.md#p-cbc366392b4673a8) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### static_slot_creation_candidates-002285

```text
(config)# default do-exec clear voice register attempted-registrations mac <address> <cr>
```

Handler ` RVA 0x17B78B40 `；selector ` 0 `；EOL ` RVA 0x365CC088 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` MAC address H.H.H。

[候选注册 R-1136174a7fd2703b](../../evidence/conditional_registrations-sets-001.md#r-1136174a7fd2703b) · [条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-9bfa0ffa45dd0931](../../evidence/parameters-sets-012.md#p-9bfa0ffa45dd0931) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### static_slot_creation_candidates-001766

```text
(config)# default do-exec clear voice shared-line call all <cr>
```

Handler ` RVA 0x17C95210 `；selector ` 1 `；EOL ` RVA 0x36632008 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-a273ceebd196a8c5](../../evidence/conditional_registrations-sets-002.md#r-a273ceebd196a8c5) · [条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### static_slot_creation_candidates-002290

```text
(config)# default do-exec clear voice shared-line call line <string> <cr>
```

Handler ` RVA 0x17C95210 `；selector ` 2 `；EOL ` RVA 0x366322F0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` shared-line dn number。

[候选注册 R-a273ceebd196a8c5](../../evidence/conditional_registrations-sets-002.md#r-a273ceebd196a8c5) · [条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-8a1bb77ddaa0bf0c](../../evidence/parameters-sets-011.md#p-8a1bb77ddaa0bf0c) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### static_slot_creation_candidates-000359

```text
(config)# default do-exec clear voice statistics <cr>
```

Handler ` RVA 0x17C39FA0 `；selector ` 0 `；EOL ` RVA 0x366283B0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-2ef74fa0410ba88d](../../evidence/conditional_registrations-sets-001.md#r-2ef74fa0410ba88d) · [条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-f2ec889ccd539c4f](../../evidence/state_effects-sets-051.md#s-f2ec889ccd539c4f)

### static_slot_creation_candidates-001897

```text
(config)# default do-exec debug atm bundle adjacency events <cr>
```

Handler ` RVA 0xE002120 `；selector ` 28 `；EOL ` RVA 0x371F9868 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-26fff63483eac9ed](../../evidence/conditional_registrations-sets-001.md#r-26fff63483eac9ed) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-4ae7a83d7f25e060](../../evidence/state_effects-sets-016.md#s-4ae7a83d7f25e060)

### static_slot_creation_candidates-001128

```text
(config)# default do-exec debug atm bundle errors <cr>
```

Handler ` RVA 0xE002120 `；selector ` 26 `；EOL ` RVA 0x371F92D8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-26fff63483eac9ed](../../evidence/conditional_registrations-sets-001.md#r-26fff63483eac9ed) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-4ae7a83d7f25e060](../../evidence/state_effects-sets-016.md#s-4ae7a83d7f25e060)

### static_slot_creation_candidates-001116

```text
(config)# default do-exec debug atm bundle events <cr>
```

Handler ` RVA 0xE002120 `；selector ` 25 `；EOL ` RVA 0x371F9030 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-26fff63483eac9ed](../../evidence/conditional_registrations-sets-001.md#r-26fff63483eac9ed) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-4ae7a83d7f25e060](../../evidence/state_effects-sets-016.md#s-4ae7a83d7f25e060)

### static_slot_creation_candidates-001157

```text
(config)# default do-exec debug atm bundle inarp <cr>
```

Handler ` RVA 0xE002120 `；selector ` 27 `；EOL ` RVA 0x371F9580 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-26fff63483eac9ed](../../evidence/conditional_registrations-sets-001.md#r-26fff63483eac9ed) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-4ae7a83d7f25e060](../../evidence/state_effects-sets-016.md#s-4ae7a83d7f25e060)

### static_slot_creation_candidates-001929

```text
(config)# default do-exec debug crypto ikev2 client flexvpn <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x36920230 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-2e7c9af75fa36899](../../evidence/conditional_registrations-sets-001.md#r-2e7c9af75fa36899) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-0378cafb7123843a](../../evidence/state_effects-sets-001.md#s-0378cafb7123843a)

### static_slot_creation_candidates-001384

```text
(config)# default do-exec debug crypto ikev2 cluster <cr>
```

Handler ` RVA 0x18F460D0 `；selector ` 0 `；EOL ` RVA 0x36926608 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-6539eec47a0080d0](../../evidence/conditional_registrations-sets-001.md#r-6539eec47a0080d0) · [条件 C-9091b112c04a734f](../../evidence/conditions-sets-056.md#c-9091b112c04a734f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c8cbcedb8952bf2b](../../evidence/state_effects-sets-043.md#s-c8cbcedb8952bf2b)

### static_slot_creation_candidates-001070

```text
(config)# default do-exec debug dapr border-router all <cr>
```

Handler ` RVA 0x1AE42BB0 `；selector ` 0 `；EOL ` RVA 0x36E57B88 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-3c179fc854eb4fc5](../../evidence/conditional_registrations-sets-001.md#r-3c179fc854eb4fc5) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-18ec9f8d57386c0d](../../evidence/state_effects-sets-006.md#s-18ec9f8d57386c0d)

### static_slot_creation_candidates-001086

```text
(config)# default do-exec debug dapr border-router events <cr>
```

Handler ` RVA 0x1AE42BB0 `；selector ` 1 `；EOL ` RVA 0x36E576B0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-3c179fc854eb4fc5](../../evidence/conditional_registrations-sets-001.md#r-3c179fc854eb4fc5) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-18ec9f8d57386c0d](../../evidence/state_effects-sets-006.md#s-18ec9f8d57386c0d)

### static_slot_creation_candidates-001831

```text
(config)# default do-exec debug dapr border-router events detail <cr>
```

Handler ` RVA 0xE002120 `；selector ` 3 `；EOL ` RVA 0x36E573E0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-3c179fc854eb4fc5](../../evidence/conditional_registrations-sets-001.md#r-3c179fc854eb4fc5) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-18ec9f8d57386c0d](../../evidence/state_effects-sets-006.md#s-18ec9f8d57386c0d)

### static_slot_creation_candidates-001840

```text
(config)# default do-exec debug dapr border-router events error <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x36E57688 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-3c179fc854eb4fc5](../../evidence/conditional_registrations-sets-001.md#r-3c179fc854eb4fc5) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-18ec9f8d57386c0d](../../evidence/state_effects-sets-006.md#s-18ec9f8d57386c0d)

### static_slot_creation_candidates-000977

```text
(config)# default do-exec debug dapr border-router flow-export <cr>
```

Handler ` RVA 0x1AE42BB0 `；selector ` 10 `；EOL ` RVA 0x36E54E58 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-3c179fc854eb4fc5](../../evidence/conditional_registrations-sets-001.md#r-3c179fc854eb4fc5) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-18ec9f8d57386c0d](../../evidence/state_effects-sets-006.md#s-18ec9f8d57386c0d)

### static_slot_creation_candidates-001791

```text
(config)# default do-exec debug dapr border-router flow-export detail <cr>
```

Handler ` RVA 0xE002120 `；selector ` 12 `；EOL ` RVA 0x36E54E30 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-3c179fc854eb4fc5](../../evidence/conditional_registrations-sets-001.md#r-3c179fc854eb4fc5) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-18ec9f8d57386c0d](../../evidence/state_effects-sets-006.md#s-18ec9f8d57386c0d)

### static_slot_creation_candidates-001781

```text
(config)# default do-exec debug dapr border-router flow-export error <cr>
```

Handler ` RVA 0xE002120 `；selector ` 11 `；EOL ` RVA 0x36E54B88 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-3c179fc854eb4fc5](../../evidence/conditional_registrations-sets-001.md#r-3c179fc854eb4fc5) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-18ec9f8d57386c0d](../../evidence/state_effects-sets-006.md#s-18ec9f8d57386c0d)

### static_slot_creation_candidates-001055

```text
(config)# default do-exec debug dapr border-router flow-route <cr>
```

Handler ` RVA 0x1AE42BB0 `；selector ` 4 `；EOL ` RVA 0x36E56690 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-3c179fc854eb4fc5](../../evidence/conditional_registrations-sets-001.md#r-3c179fc854eb4fc5) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-18ec9f8d57386c0d](../../evidence/state_effects-sets-006.md#s-18ec9f8d57386c0d)

### static_slot_creation_candidates-001820

```text
(config)# default do-exec debug dapr border-router flow-route detail <cr>
```

Handler ` RVA 0xE002120 `；selector ` 6 `；EOL ` RVA 0x36E56668 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-3c179fc854eb4fc5](../../evidence/conditional_registrations-sets-001.md#r-3c179fc854eb4fc5) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-18ec9f8d57386c0d](../../evidence/state_effects-sets-006.md#s-18ec9f8d57386c0d)

### static_slot_creation_candidates-001807

```text
(config)# default do-exec debug dapr border-router flow-route error <cr>
```

Handler ` RVA 0xE002120 `；selector ` 5 `；EOL ` RVA 0x36E563C0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-3c179fc854eb4fc5](../../evidence/conditional_registrations-sets-001.md#r-3c179fc854eb4fc5) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-18ec9f8d57386c0d](../../evidence/state_effects-sets-006.md#s-18ec9f8d57386c0d)

### static_slot_creation_candidates-001004

```text
(config)# default do-exec debug dapr border-router inter-br <cr>
```

Handler ` RVA 0x1AE42BB0 `；selector ` 13 `；EOL ` RVA 0x36E55668 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-3c179fc854eb4fc5](../../evidence/conditional_registrations-sets-001.md#r-3c179fc854eb4fc5) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-18ec9f8d57386c0d](../../evidence/state_effects-sets-006.md#s-18ec9f8d57386c0d)

### static_slot_creation_candidates-001800

```text
(config)# default do-exec debug dapr border-router inter-br detail <cr>
```

Handler ` RVA 0xE002120 `；selector ` 15 `；EOL ` RVA 0x36E55640 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-3c179fc854eb4fc5](../../evidence/conditional_registrations-sets-001.md#r-3c179fc854eb4fc5) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-18ec9f8d57386c0d](../../evidence/state_effects-sets-006.md#s-18ec9f8d57386c0d)

### static_slot_creation_candidates-001789

```text
(config)# default do-exec debug dapr border-router inter-br error <cr>
```

Handler ` RVA 0xE002120 `；selector ` 14 `；EOL ` RVA 0x36E55398 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-3c179fc854eb4fc5](../../evidence/conditional_registrations-sets-001.md#r-3c179fc854eb4fc5) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-18ec9f8d57386c0d](../../evidence/state_effects-sets-006.md#s-18ec9f8d57386c0d)

### static_slot_creation_candidates-001072

```text
(config)# default do-exec debug dapr border-router rib <cr>
```

Handler ` RVA 0x1AE42BB0 `；selector ` 7 `；EOL ` RVA 0x36E56EA0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-3c179fc854eb4fc5](../../evidence/conditional_registrations-sets-001.md#r-3c179fc854eb4fc5) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-18ec9f8d57386c0d](../../evidence/state_effects-sets-006.md#s-18ec9f8d57386c0d)

### static_slot_creation_candidates-001833

```text
(config)# default do-exec debug dapr border-router rib detail <cr>
```

Handler ` RVA 0xE002120 `；selector ` 9 `；EOL ` RVA 0x36E56E78 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-3c179fc854eb4fc5](../../evidence/conditional_registrations-sets-001.md#r-3c179fc854eb4fc5) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-18ec9f8d57386c0d](../../evidence/state_effects-sets-006.md#s-18ec9f8d57386c0d)

### static_slot_creation_candidates-001818

```text
(config)# default do-exec debug dapr border-router rib error <cr>
```

Handler ` RVA 0xE002120 `；selector ` 8 `；EOL ` RVA 0x36E56BD0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-3c179fc854eb4fc5](../../evidence/conditional_registrations-sets-001.md#r-3c179fc854eb4fc5) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-18ec9f8d57386c0d](../../evidence/state_effects-sets-006.md#s-18ec9f8d57386c0d)

### static_slot_creation_candidates-001030

```text
(config)# default do-exec debug dapr border-router wan-metric <cr>
```

Handler ` RVA 0x1AE42BB0 `；selector ` 16 `；EOL ` RVA 0x36E55E78 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-3c179fc854eb4fc5](../../evidence/conditional_registrations-sets-001.md#r-3c179fc854eb4fc5) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-18ec9f8d57386c0d](../../evidence/state_effects-sets-006.md#s-18ec9f8d57386c0d)

### static_slot_creation_candidates-001810

```text
(config)# default do-exec debug dapr border-router wan-metric detail <cr>
```

Handler ` RVA 0xE002120 `；selector ` 18 `；EOL ` RVA 0x36E55E50 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-3c179fc854eb4fc5](../../evidence/conditional_registrations-sets-001.md#r-3c179fc854eb4fc5) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-18ec9f8d57386c0d](../../evidence/state_effects-sets-006.md#s-18ec9f8d57386c0d)

### static_slot_creation_candidates-001798

```text
(config)# default do-exec debug dapr border-router wan-metric error <cr>
```

Handler ` RVA 0xE002120 `；selector ` 17 `；EOL ` RVA 0x36E55BA8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-3c179fc854eb4fc5](../../evidence/conditional_registrations-sets-001.md#r-3c179fc854eb4fc5) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-18ec9f8d57386c0d](../../evidence/state_effects-sets-006.md#s-18ec9f8d57386c0d)

### static_slot_creation_candidates-001051

```text
(config)# default do-exec debug dapr route-manager all <cr>
```

Handler ` RVA 0x1AE9C0C0 `；selector ` 0 `；EOL ` RVA 0x36E5A6F0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-78413cbaf760c6c6](../../evidence/conditional_registrations-sets-002.md#r-78413cbaf760c6c6) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-460b11d6263b13d4](../../evidence/state_effects-sets-015.md#s-460b11d6263b13d4)

### static_slot_creation_candidates-001851

```text
(config)# default do-exec debug dapr route-manager condition unmatched <cr>
```

Handler ` RVA 0x1AE9ACB0 `；selector ` 0 `；EOL ` RVA 0x36E5AA50 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-78413cbaf760c6c6](../../evidence/conditional_registrations-sets-002.md#r-78413cbaf760c6c6) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-4a8acce0927d0a61](../../evidence/state_effects-sets-016.md#s-4a8acce0927d0a61)

### static_slot_creation_candidates-001088

```text
(config)# default do-exec debug dapr route-manager events <cr>
```

Handler ` RVA 0x1AE9C0C0 `；selector ` 12 `；EOL ` RVA 0x36E5A208 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-78413cbaf760c6c6](../../evidence/conditional_registrations-sets-002.md#r-78413cbaf760c6c6) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-460b11d6263b13d4](../../evidence/state_effects-sets-015.md#s-460b11d6263b13d4)

### static_slot_creation_candidates-001832

```text
(config)# default do-exec debug dapr route-manager events detail <cr>
```

Handler ` RVA 0xE002120 `；selector ` 14 `；EOL ` RVA 0x36E59F38 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-78413cbaf760c6c6](../../evidence/conditional_registrations-sets-002.md#r-78413cbaf760c6c6) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-460b11d6263b13d4](../../evidence/state_effects-sets-015.md#s-460b11d6263b13d4)

### static_slot_creation_candidates-001817

```text
(config)# default do-exec debug dapr route-manager events error <cr>
```

Handler ` RVA 0xE002120 `；selector ` 13 `；EOL ` RVA 0x36E59C90 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-78413cbaf760c6c6](../../evidence/conditional_registrations-sets-002.md#r-78413cbaf760c6c6) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-460b11d6263b13d4](../../evidence/state_effects-sets-015.md#s-460b11d6263b13d4)

### static_slot_creation_candidates-001841

```text
(config)# default do-exec debug dapr route-manager events verbose <cr>
```

Handler ` RVA 0xE002120 `；selector ` 15 `；EOL ` RVA 0x36E5A1E0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-78413cbaf760c6c6](../../evidence/conditional_registrations-sets-002.md#r-78413cbaf760c6c6) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-460b11d6263b13d4](../../evidence/state_effects-sets-015.md#s-460b11d6263b13d4)

### static_slot_creation_candidates-001029

```text
(config)# default do-exec debug dapr route-manager flow-collector <cr>
```

Handler ` RVA 0x1AE9C0C0 `；selector ` 5 `；EOL ` RVA 0x36E58C88 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-78413cbaf760c6c6](../../evidence/conditional_registrations-sets-002.md#r-78413cbaf760c6c6) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-460b11d6263b13d4](../../evidence/state_effects-sets-015.md#s-460b11d6263b13d4)

### static_slot_creation_candidates-001809

```text
(config)# default do-exec debug dapr route-manager flow-collector detail <cr>
```

Handler ` RVA 0xE002120 `；selector ` 7 `；EOL ` RVA 0x36E58C60 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-78413cbaf760c6c6](../../evidence/conditional_registrations-sets-002.md#r-78413cbaf760c6c6) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-460b11d6263b13d4](../../evidence/state_effects-sets-015.md#s-460b11d6263b13d4)

### static_slot_creation_candidates-001797

```text
(config)# default do-exec debug dapr route-manager flow-collector error <cr>
```

Handler ` RVA 0xE002120 `；selector ` 6 `；EOL ` RVA 0x36E589B8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-78413cbaf760c6c6](../../evidence/conditional_registrations-sets-002.md#r-78413cbaf760c6c6) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-460b11d6263b13d4](../../evidence/state_effects-sets-015.md#s-460b11d6263b13d4)

### static_slot_creation_candidates-001033

```text
(config)# default do-exec debug dapr route-manager rib <cr>
```

Handler ` RVA 0x1AE9C0C0 `；selector ` 8 `；EOL ` RVA 0x36E58468 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-78413cbaf760c6c6](../../evidence/conditional_registrations-sets-002.md#r-78413cbaf760c6c6) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-460b11d6263b13d4](../../evidence/state_effects-sets-015.md#s-460b11d6263b13d4)

### static_slot_creation_candidates-001799

```text
(config)# default do-exec debug dapr route-manager rib detail <cr>
```

Handler ` RVA 0xE002120 `；selector ` 10 `；EOL ` RVA 0x36E58198 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-78413cbaf760c6c6](../../evidence/conditional_registrations-sets-002.md#r-78413cbaf760c6c6) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-460b11d6263b13d4](../../evidence/state_effects-sets-015.md#s-460b11d6263b13d4)

### static_slot_creation_candidates-001788

```text
(config)# default do-exec debug dapr route-manager rib error <cr>
```

Handler ` RVA 0xE002120 `；selector ` 9 `；EOL ` RVA 0x36E57EF0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-78413cbaf760c6c6](../../evidence/conditional_registrations-sets-002.md#r-78413cbaf760c6c6) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-460b11d6263b13d4](../../evidence/state_effects-sets-015.md#s-460b11d6263b13d4)

### static_slot_creation_candidates-001811

```text
(config)# default do-exec debug dapr route-manager rib verbose <cr>
```

Handler ` RVA 0xE002120 `；selector ` 11 `；EOL ` RVA 0x36E58440 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-78413cbaf760c6c6](../../evidence/conditional_registrations-sets-002.md#r-78413cbaf760c6c6) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-460b11d6263b13d4](../../evidence/state_effects-sets-015.md#s-460b11d6263b13d4)

### static_slot_creation_candidates-001074

```text
(config)# default do-exec debug dapr route-manager route-compute <cr>
```

Handler ` RVA 0x1AE9C0C0 `；selector ` 1 `；EOL ` RVA 0x36E59740 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-78413cbaf760c6c6](../../evidence/conditional_registrations-sets-002.md#r-78413cbaf760c6c6) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-460b11d6263b13d4](../../evidence/state_effects-sets-015.md#s-460b11d6263b13d4)

### static_slot_creation_candidates-001819

```text
(config)# default do-exec debug dapr route-manager route-compute detail <cr>
```

Handler ` RVA 0xE002120 `；selector ` 3 `；EOL ` RVA 0x36E59470 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-78413cbaf760c6c6](../../evidence/conditional_registrations-sets-002.md#r-78413cbaf760c6c6) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-460b11d6263b13d4](../../evidence/state_effects-sets-015.md#s-460b11d6263b13d4)

### static_slot_creation_candidates-001806

```text
(config)# default do-exec debug dapr route-manager route-compute error <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x36E591C8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-78413cbaf760c6c6](../../evidence/conditional_registrations-sets-002.md#r-78413cbaf760c6c6) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-460b11d6263b13d4](../../evidence/state_effects-sets-015.md#s-460b11d6263b13d4)

### static_slot_creation_candidates-001834

```text
(config)# default do-exec debug dapr route-manager route-compute internal <cr>
```

Handler ` RVA 0xE002120 `；selector ` 4 `；EOL ` RVA 0x36E59718 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-78413cbaf760c6c6](../../evidence/conditional_registrations-sets-002.md#r-78413cbaf760c6c6) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-460b11d6263b13d4](../../evidence/state_effects-sets-015.md#s-460b11d6263b13d4)

### static_slot_creation_candidates-000937

```text
(config)# default do-exec debug domain master all <cr>
```

Handler ` RVA 0x17DF9390 `；selector ` 0 `；EOL ` RVA 0x36662DF0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-f5e76483c7539320](../../evidence/conditional_registrations-sets-003.md#r-f5e76483c7539320) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-132a29bfe5484ab1](../../evidence/state_effects-sets-004.md#s-132a29bfe5484ab1)

### static_slot_creation_candidates-001201

```text
(config)# default do-exec debug domain master auto-tunnel <cr>
```

Handler ` RVA 0x17DF9390 `；selector ` 15 `；EOL ` RVA 0x36665A58 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-f5e76483c7539320](../../evidence/conditional_registrations-sets-003.md#r-f5e76483c7539320) · [条件 C-b4e68d82f8fafa48](../../evidence/conditions-sets-070.md#c-b4e68d82f8fafa48) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-132a29bfe5484ab1](../../evidence/state_effects-sets-004.md#s-132a29bfe5484ab1)

### static_slot_creation_candidates-001496

```text
(config)# default do-exec debug domain master capability <cr>
```

Handler ` RVA 0x17DF9390 `；selector ` 20 `；EOL ` RVA 0x36669B30 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-f5e76483c7539320](../../evidence/conditional_registrations-sets-003.md#r-f5e76483c7539320) · [条件 C-722ab8ad6a0bd3bf](../../evidence/conditions-sets-044.md#c-722ab8ad6a0bd3bf) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-132a29bfe5484ab1](../../evidence/state_effects-sets-004.md#s-132a29bfe5484ab1)

### static_slot_creation_candidates-001963

```text
(config)# default do-exec debug domain master channel-health-db add <cr>
```

Handler ` RVA 0x17DF9390 `；selector ` 39 `；EOL ` RVA 0x36666338 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-f5e76483c7539320](../../evidence/conditional_registrations-sets-003.md#r-f5e76483c7539320) · [条件 C-62b82bdd01f1f819](../../evidence/conditions-sets-038.md#c-62b82bdd01f1f819) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-132a29bfe5484ab1](../../evidence/state_effects-sets-004.md#s-132a29bfe5484ab1)

### static_slot_creation_candidates-001993

```text
(config)# default do-exec debug domain master channel-health-db delete <cr>
```

Handler ` RVA 0x17DF9390 `；selector ` 41 `；EOL ` RVA 0x36666888 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-f5e76483c7539320](../../evidence/conditional_registrations-sets-003.md#r-f5e76483c7539320) · [条件 C-62b82bdd01f1f819](../../evidence/conditions-sets-038.md#c-62b82bdd01f1f819) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-132a29bfe5484ab1](../../evidence/state_effects-sets-004.md#s-132a29bfe5484ab1)

### static_slot_creation_candidates-001940

```text
(config)# default do-exec debug domain master channel-health-db general <cr>
```

Handler ` RVA 0x17DF9390 `；selector ` 38 `；EOL ` RVA 0x36666090 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-f5e76483c7539320](../../evidence/conditional_registrations-sets-003.md#r-f5e76483c7539320) · [条件 C-62b82bdd01f1f819](../../evidence/conditions-sets-038.md#c-62b82bdd01f1f819) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-132a29bfe5484ab1](../../evidence/state_effects-sets-004.md#s-132a29bfe5484ab1)

### static_slot_creation_candidates-002023

```text
(config)# default do-exec debug domain master channel-health-db ode <cr>
```

Handler ` RVA 0x17DF9390 `；selector ` 44 `；EOL ` RVA 0x36667080 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-f5e76483c7539320](../../evidence/conditional_registrations-sets-003.md#r-f5e76483c7539320) · [条件 C-62b82bdd01f1f819](../../evidence/conditions-sets-038.md#c-62b82bdd01f1f819) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-132a29bfe5484ab1](../../evidence/state_effects-sets-004.md#s-132a29bfe5484ab1)

### static_slot_creation_candidates-002005

```text
(config)# default do-exec debug domain master channel-health-db perf-tca <cr>
```

Handler ` RVA 0x17DF9390 `；selector ` 43 `；EOL ` RVA 0x36666B30 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-f5e76483c7539320](../../evidence/conditional_registrations-sets-003.md#r-f5e76483c7539320) · [条件 C-62b82bdd01f1f819](../../evidence/conditions-sets-038.md#c-62b82bdd01f1f819) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-132a29bfe5484ab1](../../evidence/state_effects-sets-004.md#s-132a29bfe5484ab1)

### static_slot_creation_candidates-002012

```text
(config)# default do-exec debug domain master channel-health-db unreach <cr>
```

Handler ` RVA 0x17DF9390 `；selector ` 42 `；EOL ` RVA 0x36666DD8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-f5e76483c7539320](../../evidence/conditional_registrations-sets-003.md#r-f5e76483c7539320) · [条件 C-62b82bdd01f1f819](../../evidence/conditions-sets-038.md#c-62b82bdd01f1f819) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-132a29bfe5484ab1](../../evidence/state_effects-sets-004.md#s-132a29bfe5484ab1)

### static_slot_creation_candidates-001979

```text
(config)# default do-exec debug domain master channel-health-db update <cr>
```

Handler ` RVA 0x17DF9390 `；selector ` 40 `；EOL ` RVA 0x366665E0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-f5e76483c7539320](../../evidence/conditional_registrations-sets-003.md#r-f5e76483c7539320) · [条件 C-62b82bdd01f1f819](../../evidence/conditions-sets-038.md#c-62b82bdd01f1f819) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-132a29bfe5484ab1](../../evidence/state_effects-sets-004.md#s-132a29bfe5484ab1)

### static_slot_creation_candidates-001068

```text
(config)# default do-exec debug domain master collector <cr>
```

Handler ` RVA 0x17DF9390 `；selector ` 8 `；EOL ` RVA 0x36663EF0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-f5e76483c7539320](../../evidence/conditional_registrations-sets-003.md#r-f5e76483c7539320) · [条件 C-e12eb970fc3567ad](../../evidence/conditions-sets-087.md#c-e12eb970fc3567ad) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-132a29bfe5484ab1](../../evidence/state_effects-sets-004.md#s-132a29bfe5484ab1)

### static_slot_creation_candidates-001052

```text
(config)# default do-exec debug domain master communication <cr>
```

Handler ` RVA 0x17DF9390 `；selector ` 7 `；EOL ` RVA 0x36663C08 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-f5e76483c7539320](../../evidence/conditional_registrations-sets-003.md#r-f5e76483c7539320) · [条件 C-7f093ff0a29160fb](../../evidence/conditions-sets-049.md#c-7f093ff0a29160fb) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-132a29bfe5484ab1](../../evidence/state_effects-sets-004.md#s-132a29bfe5484ab1)

### static_slot_creation_candidates-002100

```text
(config)# default do-exec debug domain master database prefix <cr>
```

Handler ` RVA 0x17DF9390 `；selector ` 10 `；EOL ` RVA 0x3666A838 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-f5e76483c7539320](../../evidence/conditional_registrations-sets-003.md#r-f5e76483c7539320) · [条件 C-dd3c8fb569b6fe19](../../evidence/conditions-sets-085.md#c-dd3c8fb569b6fe19) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-132a29bfe5484ab1](../../evidence/state_effects-sets-004.md#s-132a29bfe5484ab1)

### static_slot_creation_candidates-002129

```text
(config)# default do-exec debug domain master database route-control <cr>
```

Handler ` RVA 0x17DF9390 `；selector ` 11 `；EOL ` RVA 0x3666AC60 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-f5e76483c7539320](../../evidence/conditional_registrations-sets-003.md#r-f5e76483c7539320) · [条件 C-e8a450f639d0432e](../../evidence/conditions-sets-090.md#c-e8a450f639d0432e) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-132a29bfe5484ab1](../../evidence/state_effects-sets-004.md#s-132a29bfe5484ab1)

### static_slot_creation_candidates-002125

```text
(config)# default do-exec debug domain master database route-import <cr>
```

Handler ` RVA 0x17DF9390 `；selector ` 26 `；EOL ` RVA 0x3666B168 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-f5e76483c7539320](../../evidence/conditional_registrations-sets-003.md#r-f5e76483c7539320) · [条件 C-18c2e31a672992ae](../../evidence/conditions-sets-010.md#c-18c2e31a672992ae) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-132a29bfe5484ab1](../../evidence/state_effects-sets-004.md#s-132a29bfe5484ab1)

### static_slot_creation_candidates-002143

```text
(config)# default do-exec debug domain master database system <cr>
```

Handler ` RVA 0x17DF9390 `；selector ` 1 `；EOL ` RVA 0x3666B450 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-f5e76483c7539320](../../evidence/conditional_registrations-sets-003.md#r-f5e76483c7539320) · [条件 C-1ad781cba760a234](../../evidence/conditions-sets-010.md#c-1ad781cba760a234) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-132a29bfe5484ab1](../../evidence/state_effects-sets-004.md#s-132a29bfe5484ab1)

### static_slot_creation_candidates-001649

```text
(config)# default do-exec debug domain master dca <cr>
```

Handler ` RVA 0x17DF9390 `；selector ` 50 `；EOL ` RVA 0x3666CB08 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-f5e76483c7539320](../../evidence/conditional_registrations-sets-003.md#r-f5e76483c7539320) · [条件 C-b5f8c1dfa33b2840](../../evidence/conditions-sets-070.md#c-b5f8c1dfa33b2840) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-132a29bfe5484ab1](../../evidence/state_effects-sets-004.md#s-132a29bfe5484ab1)

### static_slot_creation_candidates-001108

```text
(config)# default do-exec debug domain master dp-probe <cr>
```

Handler ` RVA 0x17DF9390 `；selector ` 17 `；EOL ` RVA 0x36664BF8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-f5e76483c7539320](../../evidence/conditional_registrations-sets-003.md#r-f5e76483c7539320) · [条件 C-32666bd0c6568390](../../evidence/conditions-sets-020.md#c-32666bd0c6568390) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-132a29bfe5484ab1](../../evidence/state_effects-sets-004.md#s-132a29bfe5484ab1)

### static_slot_creation_candidates-001433

```text
(config)# default do-exec debug domain master error <cr>
```

Handler ` RVA 0x17DF9390 `；selector ` 18 `；EOL ` RVA 0x366694D0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-f5e76483c7539320](../../evidence/conditional_registrations-sets-003.md#r-f5e76483c7539320) · [条件 C-66647b886f6a604e](../../evidence/conditions-sets-040.md#c-66647b886f6a604e) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-132a29bfe5484ab1](../../evidence/state_effects-sets-004.md#s-132a29bfe5484ab1)

### static_slot_creation_candidates-001239

```text
(config)# default do-exec debug domain master exporter <cr>
```

Handler ` RVA 0x17DF9390 `；selector ` 14 `；EOL ` RVA 0x36665D40 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-f5e76483c7539320](../../evidence/conditional_registrations-sets-003.md#r-f5e76483c7539320) · [条件 C-d9f9ba3b60bb9357](../../evidence/conditions-sets-084.md#c-d9f9ba3b60bb9357) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-132a29bfe5484ab1](../../evidence/state_effects-sets-004.md#s-132a29bfe5484ab1)

### static_slot_creation_candidates-001493

```text
(config)# default do-exec debug domain master ipc <cr>
```

Handler ` RVA 0x17DF9390 `；selector ` 25 `；EOL ` RVA 0x36669EC8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-f5e76483c7539320](../../evidence/conditional_registrations-sets-003.md#r-f5e76483c7539320) · [条件 C-e645856f9546213f](../../evidence/conditions-sets-089.md#c-e645856f9546213f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-132a29bfe5484ab1](../../evidence/state_effects-sets-004.md#s-132a29bfe5484ab1)

### static_slot_creation_candidates-001098

```text
(config)# default do-exec debug domain master load-balance <cr>
```

Handler ` RVA 0x17DF9390 `；selector ` 16 `；EOL ` RVA 0x36664268 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-f5e76483c7539320](../../evidence/conditional_registrations-sets-003.md#r-f5e76483c7539320) · [条件 C-f244c00ae1d0bb6a](../../evidence/conditions-sets-094.md#c-f244c00ae1d0bb6a) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-132a29bfe5484ab1](../../evidence/state_effects-sets-004.md#s-132a29bfe5484ab1)

### static_slot_creation_candidates-001457

```text
(config)# default do-exec debug domain master mhop-exporter <cr>
```

Handler ` RVA 0x17DF9390 `；selector ` 36 `；EOL ` RVA 0x36667A70 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-f5e76483c7539320](../../evidence/conditional_registrations-sets-003.md#r-f5e76483c7539320) · [条件 C-e311665ad4b9aa50](../../evidence/conditions-sets-087.md#c-e311665ad4b9aa50) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c8cc9df11083ab9c](../../evidence/state_effects-sets-043.md#s-c8cc9df11083ab9c)

### static_slot_creation_candidates-001976

```text
(config)# default do-exec debug domain master multi-hop feature <cr>
```

Handler ` RVA 0x17DF9390 `；selector ` 47 `；EOL ` RVA 0x366676A8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-f5e76483c7539320](../../evidence/conditional_registrations-sets-003.md#r-f5e76483c7539320) · [条件 C-f69ac3658d834b04](../../evidence/conditions-sets-095.md#c-f69ac3658d834b04) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-132a29bfe5484ab1](../../evidence/state_effects-sets-004.md#s-132a29bfe5484ab1)

### static_slot_creation_candidates-001959

```text
(config)# default do-exec debug domain master multi-hop pdp <cr>
```

Handler ` RVA 0x17DF9390 `；selector ` 46 `；EOL ` RVA 0x36667400 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-f5e76483c7539320](../../evidence/conditional_registrations-sets-003.md#r-f5e76483c7539320) · [条件 C-f69ac3658d834b04](../../evidence/conditions-sets-095.md#c-f69ac3658d834b04) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-132a29bfe5484ab1](../../evidence/state_effects-sets-004.md#s-132a29bfe5484ab1)

### static_slot_creation_candidates-002007

```text
(config)# default do-exec debug domain master pdp path-preference <cr>
```

Handler ` RVA 0x17DF9390 `；selector ` 23 `；EOL ` RVA 0x366685D8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-f5e76483c7539320](../../evidence/conditional_registrations-sets-003.md#r-f5e76483c7539320) · [条件 C-71069b0db5aed034](../../evidence/conditions-sets-044.md#c-71069b0db5aed034) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-132a29bfe5484ab1](../../evidence/state_effects-sets-004.md#s-132a29bfe5484ab1)

### static_slot_creation_candidates-002025

```text
(config)# default do-exec debug domain master pdp path-probe-reduction <cr>
```

Handler ` RVA 0x17DF9390 `；selector ` 35 `；EOL ` RVA 0x36668FE0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-f5e76483c7539320](../../evidence/conditional_registrations-sets-003.md#r-f5e76483c7539320) · [条件 C-1a0465875010ae6f](../../evidence/conditions-sets-010.md#c-1a0465875010ae6f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-132a29bfe5484ab1](../../evidence/state_effects-sets-004.md#s-132a29bfe5484ab1)

### static_slot_creation_candidates-002014

```text
(config)# default do-exec debug domain master pdp path-selection <cr>
```

Handler ` RVA 0x17DF9390 `；selector ` 13 `；EOL ` RVA 0x36668AF0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-f5e76483c7539320](../../evidence/conditional_registrations-sets-003.md#r-f5e76483c7539320) · [条件 C-781c02511fe284ac](../../evidence/conditions-sets-047.md#c-781c02511fe284ac) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-132a29bfe5484ab1](../../evidence/state_effects-sets-004.md#s-132a29bfe5484ab1)

### static_slot_creation_candidates-001024

```text
(config)# default do-exec debug domain master peering <cr>
```

Handler ` RVA 0x17DF9390 `；selector ` 5 `；EOL ` RVA 0x36663920 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-f5e76483c7539320](../../evidence/conditional_registrations-sets-003.md#r-f5e76483c7539320) · [条件 C-aa158360d3ae4c79](../../evidence/conditions-sets-066.md#c-aa158360d3ae4c79) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-132a29bfe5484ab1](../../evidence/state_effects-sets-004.md#s-132a29bfe5484ab1)

### static_slot_creation_candidates-001001

```text
(config)# default do-exec debug domain master pmi <cr>
```

Handler ` RVA 0x17DF9390 `；selector ` 4 `；EOL ` RVA 0x36663638 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-f5e76483c7539320](../../evidence/conditional_registrations-sets-003.md#r-f5e76483c7539320) · [条件 C-468f82b9e8581a25](../../evidence/conditions-sets-028.md#c-468f82b9e8581a25) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-132a29bfe5484ab1](../../evidence/state_effects-sets-004.md#s-132a29bfe5484ab1)

### static_slot_creation_candidates-001379

```text
(config)# default do-exec debug domain master policy <cr>
```

Handler ` RVA 0x17DF9390 `；selector ` 2 `；EOL ` RVA 0x36668238 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-f5e76483c7539320](../../evidence/conditional_registrations-sets-003.md#r-f5e76483c7539320) · [条件 C-240de41b8d2cd610](../../evidence/conditions-sets-014.md#c-240de41b8d2cd610) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-132a29bfe5484ab1](../../evidence/state_effects-sets-004.md#s-132a29bfe5484ab1)

### static_slot_creation_candidates-001109

```text
(config)# default do-exec debug domain master probe <cr>
```

Handler ` RVA 0x17DF9390 `；selector ` 9 `；EOL ` RVA 0x366647C0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-f5e76483c7539320](../../evidence/conditional_registrations-sets-003.md#r-f5e76483c7539320) · [条件 C-ca21cdcedc3bb38a](../../evidence/conditions-sets-078.md#c-ca21cdcedc3bb38a) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-132a29bfe5484ab1](../../evidence/state_effects-sets-004.md#s-132a29bfe5484ab1)

### static_slot_creation_candidates-001163

```text
(config)# default do-exec debug domain master process <cr>
```

Handler ` RVA 0x17DF9390 `；selector ` 3 `；EOL ` RVA 0x36665770 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-f5e76483c7539320](../../evidence/conditional_registrations-sets-003.md#r-f5e76483c7539320) · [条件 C-675b0107e42d75d2](../../evidence/conditions-sets-040.md#c-675b0107e42d75d2) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-132a29bfe5484ab1](../../evidence/state_effects-sets-004.md#s-132a29bfe5484ab1)

### static_slot_creation_candidates-001134

```text
(config)# default do-exec debug domain master route-control <cr>
```

Handler ` RVA 0x17DF9390 `；selector ` 12 `；EOL ` RVA 0x36664F70 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-f5e76483c7539320](../../evidence/conditional_registrations-sets-003.md#r-f5e76483c7539320) · [条件 C-a26b8321a970b922](../../evidence/conditions-sets-063.md#c-a26b8321a970b922) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-132a29bfe5484ab1](../../evidence/state_effects-sets-004.md#s-132a29bfe5484ab1)

### static_slot_creation_candidates-001165

```text
(config)# default do-exec debug domain master route-import <cr>
```

Handler ` RVA 0x17DF9390 `；selector ` 26 `；EOL ` RVA 0x366653D8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-f5e76483c7539320](../../evidence/conditional_registrations-sets-003.md#r-f5e76483c7539320) · [条件 C-0f769308d2edf444](../../evidence/conditions-sets-006.md#c-0f769308d2edf444) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-132a29bfe5484ab1](../../evidence/state_effects-sets-004.md#s-132a29bfe5484ab1)

### static_slot_creation_candidates-001514

```text
(config)# default do-exec debug domain master service-overlay <cr>
```

Handler ` RVA 0x17DF9390 `；selector ` 24 `；EOL ` RVA 0x3666A1B0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-f5e76483c7539320](../../evidence/conditional_registrations-sets-003.md#r-f5e76483c7539320) · [条件 C-15daffbea0b39349](../../evidence/conditions-sets-009.md#c-15daffbea0b39349) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-132a29bfe5484ab1](../../evidence/state_effects-sets-004.md#s-132a29bfe5484ab1)

### static_slot_creation_candidates-002089

```text
(config)# default do-exec debug domain master smp-profile cp <cr>
```

Handler ` RVA 0x17DF9390 `；selector ` 28 `；EOL ` RVA 0x3666CE10 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-f5e76483c7539320](../../evidence/conditional_registrations-sets-003.md#r-f5e76483c7539320) · [条件 C-9da65385e5450c4c](../../evidence/conditions-sets-061.md#c-9da65385e5450c4c) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-132a29bfe5484ab1](../../evidence/state_effects-sets-004.md#s-132a29bfe5484ab1)

### static_slot_creation_candidates-002382

```text
(config)# default do-exec debug domain master smp-profile dp cp <cr>
```

Handler ` RVA 0x17DF9390 `；selector ` 30 `；EOL ` RVA 0x3666D138 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-f5e76483c7539320](../../evidence/conditional_registrations-sets-003.md#r-f5e76483c7539320) · [条件 C-30c2191bb75aa04a](../../evidence/conditions-sets-019.md#c-30c2191bb75aa04a) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-132a29bfe5484ab1](../../evidence/state_effects-sets-004.md#s-132a29bfe5484ab1)

### static_slot_creation_candidates-002517

```text
(config)# default do-exec debug domain master smp-profile dp timer active <cr>
```

Handler ` RVA 0x17DF9390 `；selector ` 34 `；EOL ` RVA 0x3666D860 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-f5e76483c7539320](../../evidence/conditional_registrations-sets-003.md#r-f5e76483c7539320) · [条件 C-30c2191bb75aa04a](../../evidence/conditions-sets-019.md#c-30c2191bb75aa04a) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-85cf507797088e37](../../evidence/state_effects-sets-028.md#s-85cf507797088e37)

### static_slot_creation_candidates-002513

```text
(config)# default do-exec debug domain master smp-profile dp timer burst <cr>
```

Handler ` RVA 0x17DF9390 `；selector ` 31 `；EOL ` RVA 0x3666D4E8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-f5e76483c7539320](../../evidence/conditional_registrations-sets-003.md#r-f5e76483c7539320) · [条件 C-30c2191bb75aa04a](../../evidence/conditions-sets-019.md#c-30c2191bb75aa04a) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-b21c3049ea981628](../../evidence/state_effects-sets-038.md#s-b21c3049ea981628)

### static_slot_creation_candidates-002520

```text
(config)# default do-exec debug domain master smp-profile dp timer rx-unreach <cr>
```

Handler ` RVA 0x17DF9390 `；selector ` 32 `；EOL ` RVA 0x3666DF28 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-f5e76483c7539320](../../evidence/conditional_registrations-sets-003.md#r-f5e76483c7539320) · [条件 C-30c2191bb75aa04a](../../evidence/conditions-sets-019.md#c-30c2191bb75aa04a) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-643360914ca48f47](../../evidence/state_effects-sets-021.md#s-643360914ca48f47)

### static_slot_creation_candidates-002519

```text
(config)# default do-exec debug domain master smp-profile dp timer tx-unreach <cr>
```

Handler ` RVA 0x17DF9390 `；selector ` 33 `；EOL ` RVA 0x3666DBD8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-f5e76483c7539320](../../evidence/conditional_registrations-sets-003.md#r-f5e76483c7539320) · [条件 C-30c2191bb75aa04a](../../evidence/conditions-sets-019.md#c-30c2191bb75aa04a) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-f61a08313d1c4712](../../evidence/state_effects-sets-052.md#s-f61a08313d1c4712)

### static_slot_creation_candidates-002199

```text
(config)# default do-exec debug domain master spa all <cr>
```

Handler ` RVA 0x17DF9130 `；selector ` 6 `；EOL ` RVA 0x3666C800 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-f5e76483c7539320](../../evidence/conditional_registrations-sets-003.md#r-f5e76483c7539320) · [条件 C-4fe31c4bbb6bae30](../../evidence/conditions-sets-031.md#c-4fe31c4bbb6bae30) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-132a29bfe5484ab1](../../evidence/state_effects-sets-004.md#s-132a29bfe5484ab1)

### static_slot_creation_candidates-002157

```text
(config)# default do-exec debug domain master spa client <cr>
```

Handler ` RVA 0x17DF9130 `；selector ` 1 `；EOL ` RVA 0x3666BD48 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-f5e76483c7539320](../../evidence/conditional_registrations-sets-003.md#r-f5e76483c7539320) · [条件 C-4fe31c4bbb6bae30](../../evidence/conditions-sets-031.md#c-4fe31c4bbb6bae30) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-132a29bfe5484ab1](../../evidence/state_effects-sets-004.md#s-132a29bfe5484ab1)

### static_slot_creation_candidates-002178

```text
(config)# default do-exec debug domain master spa dca-app <cr>
```

Handler ` RVA 0x17DF9130 `；selector ` 3 `；EOL ` RVA 0x3666C2A0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-f5e76483c7539320](../../evidence/conditional_registrations-sets-003.md#r-f5e76483c7539320) · [条件 C-4fe31c4bbb6bae30](../../evidence/conditions-sets-031.md#c-4fe31c4bbb6bae30) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-132a29bfe5484ab1](../../evidence/state_effects-sets-004.md#s-132a29bfe5484ab1)

### static_slot_creation_candidates-002169

```text
(config)# default do-exec debug domain master spa dca-interface <cr>
```

Handler ` RVA 0x17DF9130 `；selector ` 2 `；EOL ` RVA 0x3666BFF0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-f5e76483c7539320](../../evidence/conditional_registrations-sets-003.md#r-f5e76483c7539320) · [条件 C-4fe31c4bbb6bae30](../../evidence/conditions-sets-031.md#c-4fe31c4bbb6bae30) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-132a29bfe5484ab1](../../evidence/state_effects-sets-004.md#s-132a29bfe5484ab1)

### static_slot_creation_candidates-002184

```text
(config)# default do-exec debug domain master spa ipsla-probe <cr>
```

Handler ` RVA 0x17DF9130 `；selector ` 4 `；EOL ` RVA 0x3666C550 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-f5e76483c7539320](../../evidence/conditional_registrations-sets-003.md#r-f5e76483c7539320) · [条件 C-4fe31c4bbb6bae30](../../evidence/conditions-sets-031.md#c-4fe31c4bbb6bae30) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-132a29bfe5484ab1](../../evidence/state_effects-sets-004.md#s-132a29bfe5484ab1)

### static_slot_creation_candidates-002141

```text
(config)# default do-exec debug domain master spa proc <cr>
```

Handler ` RVA 0x17DF9130 `；selector ` 0 `；EOL ` RVA 0x3666BAA0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-f5e76483c7539320](../../evidence/conditional_registrations-sets-003.md#r-f5e76483c7539320) · [条件 C-4fe31c4bbb6bae30](../../evidence/conditions-sets-031.md#c-4fe31c4bbb6bae30) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-132a29bfe5484ab1](../../evidence/state_effects-sets-004.md#s-132a29bfe5484ab1)

### static_slot_creation_candidates-001629

```text
(config)# default do-exec debug domain master spa-interact <cr>
```

Handler ` RVA 0x17DF9390 `；selector ` 49 `；EOL ` RVA 0x3666B788 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-f5e76483c7539320](../../evidence/conditional_registrations-sets-003.md#r-f5e76483c7539320) · [条件 C-4fe31c4bbb6bae30](../../evidence/conditions-sets-031.md#c-4fe31c4bbb6bae30) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-132a29bfe5484ab1](../../evidence/state_effects-sets-004.md#s-132a29bfe5484ab1)

### static_slot_creation_candidates-001003

```text
(config)# default do-exec debug domain master tca <cr>
```

Handler ` RVA 0x17DF9390 `；selector ` 6 `；EOL ` RVA 0x36663170 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-f5e76483c7539320](../../evidence/conditional_registrations-sets-003.md#r-f5e76483c7539320) · [条件 C-0c34f866a84e54e0](../../evidence/conditions-sets-005.md#c-0c34f866a84e54e0) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-132a29bfe5484ab1](../../evidence/state_effects-sets-004.md#s-132a29bfe5484ab1)

### static_slot_creation_candidates-001550

```text
(config)# default do-exec debug domain master timer <cr>
```

Handler ` RVA 0x17DF9390 `；selector ` 19 `；EOL ` RVA 0x3666A498 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-f5e76483c7539320](../../evidence/conditional_registrations-sets-003.md#r-f5e76483c7539320) · [条件 C-8555725882509626](../../evidence/conditions-sets-052.md#c-8555725882509626) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-132a29bfe5484ab1](../../evidence/state_effects-sets-004.md#s-132a29bfe5484ab1)

### static_slot_creation_candidates-001451

```text
(config)# default do-exec debug domain master zero-sla <cr>
```

Handler ` RVA 0x17DF9390 `；selector ` 21 `；EOL ` RVA 0x366697B8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-f5e76483c7539320](../../evidence/conditional_registrations-sets-003.md#r-f5e76483c7539320) · [条件 C-73e7538f7000d975](../../evidence/conditions-sets-045.md#c-73e7538f7000d975) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-132a29bfe5484ab1](../../evidence/state_effects-sets-004.md#s-132a29bfe5484ab1)

### static_slot_creation_candidates-000973

```text
(config)# default do-exec debug ipv6 mobile packets <cr>
```

Handler ` RVA 0x1A6C92C0 `；selector ` 0 `；EOL ` RVA 0x36CB3F70 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-af512191017de624](../../evidence/conditional_registrations-sets-002.md#r-af512191017de624) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-4314948cc963a4dc](../../evidence/state_effects-sets-015.md#s-4314948cc963a4dc)

### static_slot_creation_candidates-001779

```text
(config)# default do-exec debug performance monitor context error <cr>
```

Handler ` RVA 0x17D61040 `；selector ` 2 `；EOL ` RVA 0x36651A98 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-82af769a4691a748](../../evidence/conditional_registrations-sets-002.md#r-82af769a4691a748) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-1c541afa9e2d8009](../../evidence/state_effects-sets-006.md#s-1c541afa9e2d8009)

### static_slot_creation_candidates-001771

```text
(config)# default do-exec debug performance monitor context info <cr>
```

Handler ` RVA 0x17D61040 `；selector ` 1 `；EOL ` RVA 0x366517F0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-82af769a4691a748](../../evidence/conditional_registrations-sets-002.md#r-82af769a4691a748) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-1c541afa9e2d8009](../../evidence/state_effects-sets-006.md#s-1c541afa9e2d8009)

### static_slot_creation_candidates-001931

```text
(config)# default do-exec debug performance monitor producer performance-monitor <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x36758E78 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-535c2b51b82abdc3](../../evidence/conditional_registrations-sets-001.md#r-535c2b51b82abdc3) · [条件 C-b783b4cfd0fce00c](../../evidence/conditions-sets-071.md#c-b783b4cfd0fce00c) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-4261003751a05680](../../evidence/state_effects-sets-015.md#s-4261003751a05680)

### static_slot_creation_candidates-002328

```text
(config)# default do-exec debug performance monitor producer performance-monitor all <cr>
```

Handler ` RVA 0x1841A540 `；selector ` 3 `；EOL ` RVA 0x36758E50 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-535c2b51b82abdc3](../../evidence/conditional_registrations-sets-001.md#r-535c2b51b82abdc3) · [条件 C-b783b4cfd0fce00c](../../evidence/conditions-sets-071.md#c-b783b4cfd0fce00c) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-4261003751a05680](../../evidence/state_effects-sets-015.md#s-4261003751a05680)

### static_slot_creation_candidates-002317

```text
(config)# default do-exec debug performance monitor producer performance-monitor error <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x36758658 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-535c2b51b82abdc3](../../evidence/conditional_registrations-sets-001.md#r-535c2b51b82abdc3) · [条件 C-b783b4cfd0fce00c](../../evidence/conditions-sets-071.md#c-b783b4cfd0fce00c) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-4261003751a05680](../../evidence/state_effects-sets-015.md#s-4261003751a05680)

### static_slot_creation_candidates-002323

```text
(config)# default do-exec debug performance monitor producer performance-monitor info <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x36758BA8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-535c2b51b82abdc3](../../evidence/conditional_registrations-sets-001.md#r-535c2b51b82abdc3) · [条件 C-b783b4cfd0fce00c](../../evidence/conditions-sets-071.md#c-b783b4cfd0fce00c) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-4261003751a05680](../../evidence/state_effects-sets-015.md#s-4261003751a05680)

### static_slot_creation_candidates-002320

```text
(config)# default do-exec debug performance monitor producer performance-monitor metering <cr>
```

Handler ` RVA 0x18419610 `；selector ` 2 `；EOL ` RVA 0x36758900 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-535c2b51b82abdc3](../../evidence/conditional_registrations-sets-001.md#r-535c2b51b82abdc3) · [条件 C-b783b4cfd0fce00c](../../evidence/conditions-sets-071.md#c-b783b4cfd0fce00c) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-4261003751a05680](../../evidence/state_effects-sets-015.md#s-4261003751a05680)

### static_slot_creation_candidates-001784

```text
(config)# default do-exec debug performance monitor profile error <cr>
```

Handler ` RVA 0x17D61040 `；selector ` 4 `；EOL ` RVA 0x36652018 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-82af769a4691a748](../../evidence/conditional_registrations-sets-002.md#r-82af769a4691a748) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-1c541afa9e2d8009](../../evidence/state_effects-sets-006.md#s-1c541afa9e2d8009)

### static_slot_creation_candidates-001776

```text
(config)# default do-exec debug performance monitor profile info <cr>
```

Handler ` RVA 0x17D61040 `；selector ` 3 `；EOL ` RVA 0x36651D70 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-82af769a4691a748](../../evidence/conditional_registrations-sets-002.md#r-82af769a4691a748) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-1c541afa9e2d8009](../../evidence/state_effects-sets-006.md#s-1c541afa9e2d8009)

### static_slot_creation_candidates-000938

```text
(config)# default do-exec debug site-manager master all <cr>
```

Handler ` RVA 0x17DF9390 `；selector ` 0 `；EOL ` RVA 0x3668A130 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-3d2c01ec96881dc9](../../evidence/conditional_registrations-sets-001.md#r-3d2c01ec96881dc9) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-39afc45a69bfef6a](../../evidence/state_effects-sets-013.md#s-39afc45a69bfef6a)

### static_slot_creation_candidates-001085

```text
(config)# default do-exec debug site-manager master auto-tunnel <cr>
```

Handler ` RVA 0x17DF9390 `；selector ` 15 `；EOL ` RVA 0x3668B2A8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-3d2c01ec96881dc9](../../evidence/conditional_registrations-sets-001.md#r-3d2c01ec96881dc9) · [条件 C-73672a308757a602](../../evidence/conditions-sets-045.md#c-73672a308757a602) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-39afc45a69bfef6a](../../evidence/state_effects-sets-013.md#s-39afc45a69bfef6a)

### static_slot_creation_candidates-001133

```text
(config)# default do-exec debug site-manager master capability <cr>
```

Handler ` RVA 0x17DF9390 `；selector ` 20 `；EOL ` RVA 0x3668C108 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-3d2c01ec96881dc9](../../evidence/conditional_registrations-sets-001.md#r-3d2c01ec96881dc9) · [条件 C-2b3fe8f3ea6e4c97](../../evidence/conditions-sets-017.md#c-2b3fe8f3ea6e4c97) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-39afc45a69bfef6a](../../evidence/state_effects-sets-013.md#s-39afc45a69bfef6a)

### static_slot_creation_candidates-001025

```text
(config)# default do-exec debug site-manager master communication <cr>
```

Handler ` RVA 0x17DF9390 `；selector ` 7 `；EOL ` RVA 0x3668A9F0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-3d2c01ec96881dc9](../../evidence/conditional_registrations-sets-001.md#r-3d2c01ec96881dc9) · [条件 C-25c75b84ba2f2607](../../evidence/conditions-sets-015.md#c-25c75b84ba2f2607) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-39afc45a69bfef6a](../../evidence/state_effects-sets-013.md#s-39afc45a69bfef6a)

### static_slot_creation_candidates-001240

```text
(config)# default do-exec debug site-manager master dca <cr>
```

Handler ` RVA 0x17DF9390 `；selector ` 50 `；EOL ` RVA 0x3668DD18 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-3d2c01ec96881dc9](../../evidence/conditional_registrations-sets-001.md#r-3d2c01ec96881dc9) · [条件 C-3fb8a6a862b97f42](../../evidence/conditions-sets-025.md#c-3fb8a6a862b97f42) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-39afc45a69bfef6a](../../evidence/state_effects-sets-013.md#s-39afc45a69bfef6a)

### static_slot_creation_candidates-001278

```text
(config)# default do-exec debug site-manager master dia <cr>
```

Handler ` RVA 0x17DF9390 `；selector ` 51 `；EOL ` RVA 0x3668E000 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-3d2c01ec96881dc9](../../evidence/conditional_registrations-sets-001.md#r-3d2c01ec96881dc9) · [条件 C-cabe52930aefa9db](../../evidence/conditions-sets-078.md#c-cabe52930aefa9db) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-39afc45a69bfef6a](../../evidence/state_effects-sets-013.md#s-39afc45a69bfef6a)

### static_slot_creation_candidates-001123

```text
(config)# default do-exec debug site-manager master error <cr>
```

Handler ` RVA 0x17DF9390 `；selector ` 18 `；EOL ` RVA 0x3668BE20 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-3d2c01ec96881dc9](../../evidence/conditional_registrations-sets-001.md#r-3d2c01ec96881dc9) · [条件 C-1f332a0323e71cec](../../evidence/conditions-sets-012.md#c-1f332a0323e71cec) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-39afc45a69bfef6a](../../evidence/state_effects-sets-013.md#s-39afc45a69bfef6a)

### static_slot_creation_candidates-001164

```text
(config)# default do-exec debug site-manager master ipc <cr>
```

Handler ` RVA 0x17DF9390 `；selector ` 25 `；EOL ` RVA 0x3668C3F0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-3d2c01ec96881dc9](../../evidence/conditional_registrations-sets-001.md#r-3d2c01ec96881dc9) · [条件 C-84972f649db8200b](../../evidence/conditions-sets-051.md#c-84972f649db8200b) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-39afc45a69bfef6a](../../evidence/state_effects-sets-013.md#s-39afc45a69bfef6a)

### static_slot_creation_candidates-001849

```text
(config)# default do-exec debug site-manager master pdp path-preference <cr>
```

Handler ` RVA 0x17DF9390 `；selector ` 23 `；EOL ` RVA 0x3668B8A0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-3d2c01ec96881dc9](../../evidence/conditional_registrations-sets-001.md#r-3d2c01ec96881dc9) · [条件 C-f1d6ef313fed96a9](../../evidence/conditions-sets-093.md#c-f1d6ef313fed96a9) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-39afc45a69bfef6a](../../evidence/state_effects-sets-013.md#s-39afc45a69bfef6a)

### static_slot_creation_candidates-001859

```text
(config)# default do-exec debug site-manager master pdp path-selection <cr>
```

Handler ` RVA 0x17DF9390 `；selector ` 13 `；EOL ` RVA 0x3668BB48 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-3d2c01ec96881dc9](../../evidence/conditional_registrations-sets-001.md#r-3d2c01ec96881dc9) · [条件 C-f1d6ef313fed96a9](../../evidence/conditions-sets-093.md#c-f1d6ef313fed96a9) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-39afc45a69bfef6a](../../evidence/state_effects-sets-013.md#s-39afc45a69bfef6a)

### static_slot_creation_candidates-001002

```text
(config)# default do-exec debug site-manager master peering <cr>
```

Handler ` RVA 0x17DF9390 `；selector ` 5 `；EOL ` RVA 0x3668A708 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-3d2c01ec96881dc9](../../evidence/conditional_registrations-sets-001.md#r-3d2c01ec96881dc9) · [条件 C-94dae68a51dbd582](../../evidence/conditions-sets-058.md#c-94dae68a51dbd582) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-39afc45a69bfef6a](../../evidence/state_effects-sets-013.md#s-39afc45a69bfef6a)

### static_slot_creation_candidates-001097

```text
(config)# default do-exec debug site-manager master policy <cr>
```

Handler ` RVA 0x17DF9390 `；selector ` 2 `；EOL ` RVA 0x3668B590 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-3d2c01ec96881dc9](../../evidence/conditional_registrations-sets-001.md#r-3d2c01ec96881dc9) · [条件 C-3f77b75062890c07](../../evidence/conditions-sets-025.md#c-3f77b75062890c07) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-39afc45a69bfef6a](../../evidence/state_effects-sets-013.md#s-39afc45a69bfef6a)

### static_slot_creation_candidates-001069

```text
(config)# default do-exec debug site-manager master process <cr>
```

Handler ` RVA 0x17DF9390 `；selector ` 3 `；EOL ` RVA 0x3668AFC0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-3d2c01ec96881dc9](../../evidence/conditional_registrations-sets-001.md#r-3d2c01ec96881dc9) · [条件 C-c140742ae67beac1](../../evidence/conditions-sets-075.md#c-c140742ae67beac1) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-39afc45a69bfef6a](../../evidence/state_effects-sets-013.md#s-39afc45a69bfef6a)

### static_slot_creation_candidates-001053

```text
(config)# default do-exec debug site-manager master route-control <cr>
```

Handler ` RVA 0x17DF9390 `；selector ` 12 `；EOL ` RVA 0x3668ACD8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-3d2c01ec96881dc9](../../evidence/conditional_registrations-sets-001.md#r-3d2c01ec96881dc9) · [条件 C-fef56f8a0f6397e9](../../evidence/conditions-sets-098.md#c-fef56f8a0f6397e9) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-39afc45a69bfef6a](../../evidence/state_effects-sets-013.md#s-39afc45a69bfef6a)

### static_slot_creation_candidates-002013

```text
(config)# default do-exec debug site-manager master spa all <cr>
```

Handler ` RVA 0x17DF9130 `；selector ` 6 `；EOL ` RVA 0x3668DA00 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-3d2c01ec96881dc9](../../evidence/conditional_registrations-sets-001.md#r-3d2c01ec96881dc9) · [条件 C-4ad374cc443ceb3e](../../evidence/conditions-sets-029.md#c-4ad374cc443ceb3e) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-39afc45a69bfef6a](../../evidence/state_effects-sets-013.md#s-39afc45a69bfef6a)

### static_slot_creation_candidates-001944

```text
(config)# default do-exec debug site-manager master spa client <cr>
```

Handler ` RVA 0x17DF9130 `；selector ` 1 `；EOL ` RVA 0x3668CC98 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-3d2c01ec96881dc9](../../evidence/conditional_registrations-sets-001.md#r-3d2c01ec96881dc9) · [条件 C-4ad374cc443ceb3e](../../evidence/conditions-sets-029.md#c-4ad374cc443ceb3e) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-39afc45a69bfef6a](../../evidence/state_effects-sets-013.md#s-39afc45a69bfef6a)

### static_slot_creation_candidates-001981

```text
(config)# default do-exec debug site-manager master spa dca-app <cr>
```

Handler ` RVA 0x17DF9130 `；selector ` 3 `；EOL ` RVA 0x3668D1F0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-3d2c01ec96881dc9](../../evidence/conditional_registrations-sets-001.md#r-3d2c01ec96881dc9) · [条件 C-4ad374cc443ceb3e](../../evidence/conditions-sets-029.md#c-4ad374cc443ceb3e) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-39afc45a69bfef6a](../../evidence/state_effects-sets-013.md#s-39afc45a69bfef6a)

### static_slot_creation_candidates-001966

```text
(config)# default do-exec debug site-manager master spa dca-interface <cr>
```

Handler ` RVA 0x17DF9130 `；selector ` 2 `；EOL ` RVA 0x3668CF40 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-3d2c01ec96881dc9](../../evidence/conditional_registrations-sets-001.md#r-3d2c01ec96881dc9) · [条件 C-4ad374cc443ceb3e](../../evidence/conditions-sets-029.md#c-4ad374cc443ceb3e) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-39afc45a69bfef6a](../../evidence/state_effects-sets-013.md#s-39afc45a69bfef6a)

### static_slot_creation_candidates-002006

```text
(config)# default do-exec debug site-manager master spa dia-class <cr>
```

Handler ` RVA 0x17DF9130 `；selector ` 5 `；EOL ` RVA 0x3668D750 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-3d2c01ec96881dc9](../../evidence/conditional_registrations-sets-001.md#r-3d2c01ec96881dc9) · [条件 C-4ad374cc443ceb3e](../../evidence/conditions-sets-029.md#c-4ad374cc443ceb3e) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-39afc45a69bfef6a](../../evidence/state_effects-sets-013.md#s-39afc45a69bfef6a)

### static_slot_creation_candidates-001996

```text
(config)# default do-exec debug site-manager master spa ipsla-probe <cr>
```

Handler ` RVA 0x17DF9130 `；selector ` 4 `；EOL ` RVA 0x3668D4A0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-3d2c01ec96881dc9](../../evidence/conditional_registrations-sets-001.md#r-3d2c01ec96881dc9) · [条件 C-4ad374cc443ceb3e](../../evidence/conditions-sets-029.md#c-4ad374cc443ceb3e) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-39afc45a69bfef6a](../../evidence/state_effects-sets-013.md#s-39afc45a69bfef6a)

### static_slot_creation_candidates-001917

```text
(config)# default do-exec debug site-manager master spa proc <cr>
```

Handler ` RVA 0x17DF9130 `；selector ` 0 `；EOL ` RVA 0x3668C9F0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-3d2c01ec96881dc9](../../evidence/conditional_registrations-sets-001.md#r-3d2c01ec96881dc9) · [条件 C-4ad374cc443ceb3e](../../evidence/conditions-sets-029.md#c-4ad374cc443ceb3e) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-39afc45a69bfef6a](../../evidence/state_effects-sets-013.md#s-39afc45a69bfef6a)

### static_slot_creation_candidates-001202

```text
(config)# default do-exec debug site-manager master spa-interact <cr>
```

Handler ` RVA 0x17DF9390 `；selector ` 49 `；EOL ` RVA 0x3668C6D8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-3d2c01ec96881dc9](../../evidence/conditional_registrations-sets-001.md#r-3d2c01ec96881dc9) · [条件 C-4ad374cc443ceb3e](../../evidence/conditions-sets-029.md#c-4ad374cc443ceb3e) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-39afc45a69bfef6a](../../evidence/state_effects-sets-013.md#s-39afc45a69bfef6a)

### static_slot_creation_candidates-000974

```text
(config)# default do-exec debug site-manager master tca <cr>
```

Handler ` RVA 0x17DF9390 `；selector ` 6 `；EOL ` RVA 0x3668A420 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-3d2c01ec96881dc9](../../evidence/conditional_registrations-sets-001.md#r-3d2c01ec96881dc9) · [条件 C-a86224b199f7db39](../../evidence/conditions-sets-065.md#c-a86224b199f7db39) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-39afc45a69bfef6a](../../evidence/state_effects-sets-013.md#s-39afc45a69bfef6a)

### static_slot_creation_candidates-000330

```text
(config)# default do-exec debug vfi checkpoint <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x36E6C2A8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-34024b6639daec1d](../../evidence/conditional_registrations-sets-001.md#r-34024b6639daec1d) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-3ba700ce64c7bbeb](../../evidence/state_effects-sets-013.md#s-3ba700ce64c7bbeb)

### static_slot_creation_candidates-000408

```text
(config)# default do-exec debug voip aaa <cr>
```

Handler ` RVA 0x1BF04DF0 `；selector ` 0 `；EOL ` RVA 0x371F05A0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-318cd6f8c3a726d7](../../evidence/conditional_registrations-sets-001.md#r-318cd6f8c3a726d7) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-ad1e85a81cb2239d](../../evidence/state_effects-sets-037.md#s-ad1e85a81cb2239d)

### static_slot_creation_candidates-000968

```text
(config)# default do-exec debug voip aaa asnl <cr>
```

Handler ` RVA 0x1BF04E90 `；selector ` 0 `；EOL ` RVA 0x371F0578 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-318cd6f8c3a726d7](../../evidence/conditional_registrations-sets-001.md#r-318cd6f8c3a726d7) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-ad1e85a81cb2239d](../../evidence/state_effects-sets-037.md#s-ad1e85a81cb2239d)

### static_slot_creation_candidates-000870

```text
(config)# default do-exec debug voip application <cr>
```

Handler ` RVA 0x1683E4C0 `；selector ` 1 `；EOL ` RVA 0x35FEB5B8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-4515014a01afa49b](../../evidence/conditional_registrations-sets-001.md#r-4515014a01afa49b) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-39008bb7b65e5fef](../../evidence/state_effects-sets-013.md#s-39008bb7b65e5fef)

### static_slot_creation_candidates-001606

```text
(config)# default do-exec debug voip application accounting <cr>
```

Handler ` RVA 0xE002120 `；selector ` 23 `；EOL ` RVA 0x35FEAF30 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-4515014a01afa49b](../../evidence/conditional_registrations-sets-001.md#r-4515014a01afa49b) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-39008bb7b65e5fef](../../evidence/state_effects-sets-013.md#s-39008bb7b65e5fef)

### static_slot_creation_candidates-001628

```text
(config)# default do-exec debug voip application all <cr>
```

Handler ` RVA 0x1683E1C0 `；selector ` 1 `；EOL ` RVA 0x35FEB1E0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-4515014a01afa49b](../../evidence/conditional_registrations-sets-001.md#r-4515014a01afa49b) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-39008bb7b65e5fef](../../evidence/state_effects-sets-013.md#s-39008bb7b65e5fef)

### static_slot_creation_candidates-001432

```text
(config)# default do-exec debug voip application auth <cr>
```

Handler ` RVA 0xE002120 `；selector ` 26 `；EOL ` RVA 0x35FE9C80 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-4515014a01afa49b](../../evidence/conditional_registrations-sets-001.md#r-4515014a01afa49b) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-39008bb7b65e5fef](../../evidence/state_effects-sets-013.md#s-39008bb7b65e5fef)

### static_slot_creation_candidates-001237

```text
(config)# default do-exec debug voip application callfeature <cr>
```

Handler ` RVA 0xE002120 `；selector ` 11 `；EOL ` RVA 0x35FE8C80 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-4515014a01afa49b](../../evidence/conditional_registrations-sets-001.md#r-4515014a01afa49b) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-39008bb7b65e5fef](../../evidence/state_effects-sets-013.md#s-39008bb7b65e5fef)

### static_slot_creation_candidates-001492

```text
(config)# default do-exec debug voip application callindependss <cr>
```

Handler ` RVA 0xE002120 `；selector ` 20 `；EOL ` RVA 0x35FEA490 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-4515014a01afa49b](../../evidence/conditional_registrations-sets-001.md#r-4515014a01afa49b) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-39008bb7b65e5fef](../../evidence/state_effects-sets-013.md#s-39008bb7b65e5fef)

### static_slot_creation_candidates-001277

```text
(config)# default do-exec debug voip application callsetup <cr>
```

Handler ` RVA 0xE002120 `；selector ` 12 `；EOL ` RVA 0x35FE8F28 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-4515014a01afa49b](../../evidence/conditional_registrations-sets-001.md#r-4515014a01afa49b) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-39008bb7b65e5fef](../../evidence/state_effects-sets-013.md#s-39008bb7b65e5fef)

### static_slot_creation_candidates-001161

```text
(config)# default do-exec debug voip application core <cr>
```

Handler ` RVA 0xE002120 `；selector ` 8 `；EOL ` RVA 0x35FE8730 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-4515014a01afa49b](../../evidence/conditional_registrations-sets-001.md#r-4515014a01afa49b) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-39008bb7b65e5fef](../../evidence/state_effects-sets-013.md#s-39008bb7b65e5fef)

### static_slot_creation_candidates-001581

```text
(config)# default do-exec debug voip application datastruct <cr>
```

Handler ` RVA 0xE002120 `；selector ` 22 `；EOL ` RVA 0x35FEAC88 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-4515014a01afa49b](../../evidence/conditional_registrations-sets-001.md#r-4515014a01afa49b) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-39008bb7b65e5fef](../../evidence/state_effects-sets-013.md#s-39008bb7b65e5fef)

### static_slot_creation_candidates-001199

```text
(config)# default do-exec debug voip application digitcollect <cr>
```

Handler ` RVA 0xE002120 `；selector ` 10 `；EOL ` RVA 0x35FE89D8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-4515014a01afa49b](../../evidence/conditional_registrations-sets-001.md#r-4515014a01afa49b) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-39008bb7b65e5fef](../../evidence/state_effects-sets-013.md#s-39008bb7b65e5fef)

### static_slot_creation_candidates-001061

```text
(config)# default do-exec debug voip application error <cr>
```

Handler ` RVA 0x1683E340 `；selector ` 0 `；EOL ` RVA 0x35FE6C70 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-4515014a01afa49b](../../evidence/conditional_registrations-sets-001.md#r-4515014a01afa49b) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-39008bb7b65e5fef](../../evidence/state_effects-sets-013.md#s-39008bb7b65e5fef)

### static_slot_creation_candidates-000983

```text
(config)# default do-exec debug voip application kadis_toggle <cr>
```

Handler ` RVA 0x17281860 `；selector ` 1 `；EOL ` RVA 0x35FE6470 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-4515014a01afa49b](../../evidence/conditional_registrations-sets-001.md#r-4515014a01afa49b) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-39008bb7b65e5fef](../../evidence/state_effects-sets-013.md#s-39008bb7b65e5fef)

### static_slot_creation_candidates-001549

```text
(config)# default do-exec debug voip application linking <cr>
```

Handler ` RVA 0xE002120 `；selector ` 21 `；EOL ` RVA 0x35FEA9E0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-4515014a01afa49b](../../evidence/conditional_registrations-sets-001.md#r-4515014a01afa49b) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-39008bb7b65e5fef](../../evidence/state_effects-sets-013.md#s-39008bb7b65e5fef)

### static_slot_creation_candidates-001404

```text
(config)# default do-exec debug voip application lpcor <cr>
```

Handler ` RVA 0xE002120 `；selector ` 25 `；EOL ` RVA 0x35FE99D0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-4515014a01afa49b](../../evidence/conditional_registrations-sets-001.md#r-4515014a01afa49b) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-39008bb7b65e5fef](../../evidence/state_effects-sets-013.md#s-39008bb7b65e5fef)

### static_slot_creation_candidates-001207

```text
(config)# default do-exec debug voip application media <cr>
```

Handler ` RVA 0x1683E690 `；selector ` 0 `；EOL ` RVA 0x35FE7CF0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-4515014a01afa49b](../../evidence/conditional_registrations-sets-001.md#r-4515014a01afa49b) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-39008bb7b65e5fef](../../evidence/state_effects-sets-013.md#s-39008bb7b65e5fef)

### static_slot_creation_candidates-001887

```text
(config)# default do-exec debug voip application media forking <cr>
```

Handler ` RVA 0xE002120 `；selector ` 3 `；EOL ` RVA 0x35FE7CC8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-4515014a01afa49b](../../evidence/conditional_registrations-sets-001.md#r-4515014a01afa49b) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-39008bb7b65e5fef](../../evidence/state_effects-sets-013.md#s-39008bb7b65e5fef)

### static_slot_creation_candidates-001874

```text
(config)# default do-exec debug voip application media negotiation <cr>
```

Handler ` RVA 0xE002120 `；selector ` 13 `；EOL ` RVA 0x35FE7A20 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-4515014a01afa49b](../../evidence/conditional_registrations-sets-001.md#r-4515014a01afa49b) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-39008bb7b65e5fef](../../evidence/state_effects-sets-013.md#s-39008bb7b65e5fef)

### static_slot_creation_candidates-001866

```text
(config)# default do-exec debug voip application media packet <cr>
```

Handler ` RVA 0xE002120 `；selector ` 4 `；EOL ` RVA 0x35FE7778 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-4515014a01afa49b](../../evidence/conditional_registrations-sets-001.md#r-4515014a01afa49b) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-39008bb7b65e5fef](../../evidence/state_effects-sets-013.md#s-39008bb7b65e5fef)

### static_slot_creation_candidates-001855

```text
(config)# default do-exec debug voip application media state <cr>
```

Handler ` RVA 0xE002120 `；selector ` 5 `；EOL ` RVA 0x35FE74D0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-4515014a01afa49b](../../evidence/conditional_registrations-sets-001.md#r-4515014a01afa49b) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-39008bb7b65e5fef](../../evidence/state_effects-sets-013.md#s-39008bb7b65e5fef)

### static_slot_creation_candidates-001473

```text
(config)# default do-exec debug voip application mlpp <cr>
```

Handler ` RVA 0xE002120 `；selector ` 24 `；EOL ` RVA 0x35FEA1E0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-4515014a01afa49b](../../evidence/conditional_registrations-sets-001.md#r-4515014a01afa49b) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-39008bb7b65e5fef](../../evidence/state_effects-sets-013.md#s-39008bb7b65e5fef)

### static_slot_creation_candidates-001450

```text
(config)# default do-exec debug voip application mwi <cr>
```

Handler ` RVA 0xE002120 `；selector ` 19 `；EOL ` RVA 0x35FE9F30 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-4515014a01afa49b](../../evidence/conditional_registrations-sets-001.md#r-4515014a01afa49b) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-39008bb7b65e5fef](../../evidence/state_effects-sets-013.md#s-39008bb7b65e5fef)

### static_slot_creation_candidates-001347

```text
(config)# default do-exec debug voip application oodrefer <cr>
```

Handler ` RVA 0xE002120 `；selector ` 16 `；EOL ` RVA 0x35FE9478 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-4515014a01afa49b](../../evidence/conditional_registrations-sets-001.md#r-4515014a01afa49b) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-39008bb7b65e5fef](../../evidence/state_effects-sets-013.md#s-39008bb7b65e5fef)

### static_slot_creation_candidates-001314

```text
(config)# default do-exec debug voip application park-pickup <cr>
```

Handler ` RVA 0xE002120 `；selector ` 17 `；EOL ` RVA 0x35FE91D0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-4515014a01afa49b](../../evidence/conditional_registrations-sets-001.md#r-4515014a01afa49b) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-39008bb7b65e5fef](../../evidence/state_effects-sets-013.md#s-39008bb7b65e5fef)

### static_slot_creation_candidates-001041

```text
(config)# default do-exec debug voip application redirect <cr>
```

Handler ` RVA 0xE002120 `；selector ` 14 `；EOL ` RVA 0x35FE69C8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-4515014a01afa49b](../../evidence/conditional_registrations-sets-001.md#r-4515014a01afa49b) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-39008bb7b65e5fef](../../evidence/state_effects-sets-013.md#s-39008bb7b65e5fef)

### static_slot_creation_candidates-001121

```text
(config)# default do-exec debug voip application script <cr>
```

Handler ` RVA 0xE002120 `；selector ` 7 `；EOL ` RVA 0x35FE81E0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-4515014a01afa49b](../../evidence/conditional_registrations-sets-001.md#r-4515014a01afa49b) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-39008bb7b65e5fef](../../evidence/state_effects-sets-013.md#s-39008bb7b65e5fef)

### static_slot_creation_candidates-001513

```text
(config)# default do-exec debug voip application session <cr>
```

Handler ` RVA 0xE002120 `；selector ` 18 `；EOL ` RVA 0x35FEA738 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-4515014a01afa49b](../../evidence/conditional_registrations-sets-001.md#r-4515014a01afa49b) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-39008bb7b65e5fef](../../evidence/state_effects-sets-013.md#s-39008bb7b65e5fef)

### static_slot_creation_candidates-001092

```text
(config)# default do-exec debug voip application settlement <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x35FE71C0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-4515014a01afa49b](../../evidence/conditional_registrations-sets-001.md#r-4515014a01afa49b) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-39008bb7b65e5fef](../../evidence/state_effects-sets-013.md#s-39008bb7b65e5fef)

### static_slot_creation_candidates-001079

```text
(config)# default do-exec debug voip application states <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x35FE6F18 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-4515014a01afa49b](../../evidence/conditional_registrations-sets-001.md#r-4515014a01afa49b) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-39008bb7b65e5fef](../../evidence/state_effects-sets-013.md#s-39008bb7b65e5fef)

### static_slot_creation_candidates-001012

```text
(config)# default do-exec debug voip application supplementary-service <cr>
```

Handler ` RVA 0xE002120 `；selector ` 15 `；EOL ` RVA 0x35FE6720 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-4515014a01afa49b](../../evidence/conditional_registrations-sets-001.md#r-4515014a01afa49b) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-39008bb7b65e5fef](../../evidence/state_effects-sets-013.md#s-39008bb7b65e5fef)

### static_slot_creation_candidates-001130

```text
(config)# default do-exec debug voip application tclcommands <cr>
```

Handler ` RVA 0xE002120 `；selector ` 9 `；EOL ` RVA 0x35FE8488 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-4515014a01afa49b](../../evidence/conditional_registrations-sets-001.md#r-4515014a01afa49b) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-39008bb7b65e5fef](../../evidence/state_effects-sets-013.md#s-39008bb7b65e5fef)

### static_slot_creation_candidates-001378

```text
(config)# default do-exec debug voip application translate <cr>
```

Handler ` RVA 0xE002120 `；selector ` 27 `；EOL ` RVA 0x35FE9720 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-4515014a01afa49b](../../evidence/conditional_registrations-sets-001.md#r-4515014a01afa49b) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-39008bb7b65e5fef](../../evidence/state_effects-sets-013.md#s-39008bb7b65e5fef)

### static_slot_creation_candidates-000475

```text
(config)# default do-exec debug voip avlist <cr>
```

Handler ` RVA 0x1BCE9B60 `；selector ` 1 `；EOL ` RVA 0x36FEE0F0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-f4dc766868209415](../../evidence/conditional_registrations-sets-003.md#r-f4dc766868209415) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-6b7d11495f34ae63](../../evidence/state_effects-sets-023.md#s-6b7d11495f34ae63)

### static_slot_creation_candidates-000966

```text
(config)# default do-exec debug voip avlist all <cr>
```

Handler ` RVA 0x1BCE9B60 `；selector ` 0 `；EOL ` RVA 0x36FED628 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-f4dc766868209415](../../evidence/conditional_registrations-sets-003.md#r-f4dc766868209415) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-6b7d11495f34ae63](../../evidence/state_effects-sets-023.md#s-6b7d11495f34ae63)

### static_slot_creation_candidates-000997

```text
(config)# default do-exec debug voip avlist default <cr>
```

Handler ` RVA 0x1BCE9B60 `；selector ` 1 `；EOL ` RVA 0x36FED8D0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-f4dc766868209415](../../evidence/conditional_registrations-sets-003.md#r-f4dc766868209415) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-6b7d11495f34ae63](../../evidence/state_effects-sets-023.md#s-6b7d11495f34ae63)

### static_slot_creation_candidates-001022

```text
(config)# default do-exec debug voip avlist detail <cr>
```

Handler ` RVA 0xE002120 `；selector ` 5 `；EOL ` RVA 0x36FEDB78 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-f4dc766868209415](../../evidence/conditional_registrations-sets-003.md#r-f4dc766868209415) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-6b7d11495f34ae63](../../evidence/state_effects-sets-023.md#s-6b7d11495f34ae63)

### static_slot_creation_candidates-001099

```text
(config)# default do-exec debug voip avlist error <cr>
```

Handler ` RVA 0x1BCE9B60 `；selector ` 2 `；EOL ` RVA 0x36FEE1B8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-f4dc766868209415](../../evidence/conditional_registrations-sets-003.md#r-f4dc766868209415) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-9856191405948d29](../../evidence/state_effects-sets-032.md#s-9856191405948d29)

### static_slot_creation_candidates-001049

```text
(config)# default do-exec debug voip avlist inout <cr>
```

Handler ` RVA 0xE002120 `；selector ` 4 `；EOL ` RVA 0x36FEDE20 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-f4dc766868209415](../../evidence/conditional_registrations-sets-003.md#r-f4dc766868209415) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-6b7d11495f34ae63](../../evidence/state_effects-sets-023.md#s-6b7d11495f34ae63)

### static_slot_creation_candidates-000502

```text
(config)# default do-exec debug voip dialpeer <cr>
```

Handler ` RVA 0x1BB3AAC0 `；selector ` 1 `；EOL ` RVA 0x36FADAD0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-b713c3df28d3ecf3](../../evidence/conditional_registrations-sets-002.md#r-b713c3df28d3ecf3) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-199cb6849d5de8c1](../../evidence/state_effects-sets-006.md#s-199cb6849d5de8c1)

### static_slot_creation_candidates-000965

```text
(config)# default do-exec debug voip dialpeer all <cr>
```

Handler ` RVA 0x1BB3AAC0 `；selector ` 0 `；EOL ` RVA 0x36FAC810 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-b713c3df28d3ecf3](../../evidence/conditional_registrations-sets-002.md#r-b713c3df28d3ecf3) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-199cb6849d5de8c1](../../evidence/state_effects-sets-006.md#s-199cb6849d5de8c1)

### static_slot_creation_candidates-001067

```text
(config)# default do-exec debug voip dialpeer config <cr>
```

Handler ` RVA 0xE002120 `；selector ` 7 `；EOL ` RVA 0x36FAD2B0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-b713c3df28d3ecf3](../../evidence/conditional_registrations-sets-002.md#r-b713c3df28d3ecf3) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-199cb6849d5de8c1](../../evidence/state_effects-sets-006.md#s-199cb6849d5de8c1)

### static_slot_creation_candidates-000996

```text
(config)# default do-exec debug voip dialpeer default <cr>
```

Handler ` RVA 0x1BB3AAC0 `；selector ` 1 `；EOL ` RVA 0x36FACAB8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-b713c3df28d3ecf3](../../evidence/conditional_registrations-sets-002.md#r-b713c3df28d3ecf3) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-199cb6849d5de8c1](../../evidence/state_effects-sets-006.md#s-199cb6849d5de8c1)

### static_slot_creation_candidates-001048

```text
(config)# default do-exec debug voip dialpeer detail <cr>
```

Handler ` RVA 0xE002120 `；selector ` 6 `；EOL ` RVA 0x36FAD008 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-b713c3df28d3ecf3](../../evidence/conditional_registrations-sets-002.md#r-b713c3df28d3ecf3) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-199cb6849d5de8c1](../../evidence/state_effects-sets-006.md#s-199cb6849d5de8c1)

### static_slot_creation_candidates-001135

```text
(config)# default do-exec debug voip dialpeer error <cr>
```

Handler ` RVA 0x1BB3AAC0 `；selector ` 2 `；EOL ` RVA 0x36FADB98 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-b713c3df28d3ecf3](../../evidence/conditional_registrations-sets-002.md#r-b713c3df28d3ecf3) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-dff6dced8bc7e49d](../../evidence/state_effects-sets-047.md#s-dff6dced8bc7e49d)

### static_slot_creation_candidates-001096

```text
(config)# default do-exec debug voip dialpeer function <cr>
```

Handler ` RVA 0xE002120 `；selector ` 4 `；EOL ` RVA 0x36FAD800 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-b713c3df28d3ecf3](../../evidence/conditional_registrations-sets-002.md#r-b713c3df28d3ecf3) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-199cb6849d5de8c1](../../evidence/state_effects-sets-006.md#s-199cb6849d5de8c1)

### static_slot_creation_candidates-001021

```text
(config)# default do-exec debug voip dialpeer inout <cr>
```

Handler ` RVA 0xE002120 `；selector ` 5 `；EOL ` RVA 0x36FACD60 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-b713c3df28d3ecf3](../../evidence/conditional_registrations-sets-002.md#r-b713c3df28d3ecf3) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-199cb6849d5de8c1](../../evidence/state_effects-sets-006.md#s-199cb6849d5de8c1)

### static_slot_creation_candidates-001083

```text
(config)# default do-exec debug voip dialpeer translation <cr>
```

Handler ` RVA 0xE002120 `；selector ` 8 `；EOL ` RVA 0x36FAD558 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-b713c3df28d3ecf3](../../evidence/conditional_registrations-sets-002.md#r-b713c3df28d3ecf3) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-199cb6849d5de8c1](../../evidence/state_effects-sets-006.md#s-199cb6849d5de8c1)

### static_slot_creation_candidates-000964

```text
(config)# default do-exec debug voip dsm dsp <cr>
```

Handler ` RVA 0x1812D180 `；selector ` 0 `；EOL ` RVA 0x366EDAA0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-bf06c6b524a5beb7](../../evidence/conditional_registrations-sets-002.md#r-bf06c6b524a5beb7) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-32502814af740bb9](../../evidence/state_effects-sets-011.md#s-32502814af740bb9)

### static_slot_creation_candidates-000666

```text
(config)# default do-exec debug voip dsmp <cr>
```

Handler ` RVA 0x181901F0 `；selector ` 13 `；EOL ` RVA 0x366F1B48 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-a3778c48128b9a7a](../../evidence/conditional_registrations-sets-002.md#r-a3778c48128b9a7a) · [条件 C-17f6c6cab0bdf00a](../../evidence/conditions-sets-009.md#c-17f6c6cab0bdf00a) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-b86a2a2b6fde7d05](../../evidence/state_effects-sets-039.md#s-b86a2a2b6fde7d05)

### static_slot_creation_candidates-000995

```text
(config)# default do-exec debug voip dsmp all <cr>
```

Handler ` RVA 0x181901F0 `；selector ` 0 `；EOL ` RVA 0x366F03E0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-a3778c48128b9a7a](../../evidence/conditional_registrations-sets-002.md#r-a3778c48128b9a7a) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-b4e828e3f2381a3f](../../evidence/state_effects-sets-038.md#s-b4e828e3f2381a3f)

### static_slot_creation_candidates-002498

```text
(config)# default do-exec debug voip dsmp rtp from-dsp payload all <cr>
```

Handler ` RVA 0x18190C60 `；selector ` 0 `；EOL ` RVA 0x366F13A8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-a3778c48128b9a7a](../../evidence/conditional_registrations-sets-002.md#r-a3778c48128b9a7a) · [条件 C-17f6c6cab0bdf00a](../../evidence/conditions-sets-009.md#c-17f6c6cab0bdf00a) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-54a61478e68ca261](../../evidence/state_effects-sets-018.md#s-54a61478e68ca261)

### static_slot_creation_candidates-001413

```text
(config)# default do-exec debug voip dsmp udp <cr>
```

Handler ` RVA 0x181922D0 `；selector ` 0 `；EOL ` RVA 0x366F1ED8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-a3778c48128b9a7a](../../evidence/conditional_registrations-sets-002.md#r-a3778c48128b9a7a) · [条件 C-17f6c6cab0bdf00a](../../evidence/conditions-sets-009.md#c-17f6c6cab0bdf00a) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-b86a2a2b6fde7d05](../../evidence/state_effects-sets-039.md#s-b86a2a2b6fde7d05)

### static_slot_creation_candidates-002341

```text
(config)# default do-exec debug voip dsmp udp from-dsp <number:0..10000000> <cr>
```

Handler ` RVA 0x18192140 `；selector ` 0 `；EOL ` RVA 0x366F1C00 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

参数提示：` unsigned_number ` number of udp packet to debug。

[候选注册 R-a3778c48128b9a7a](../../evidence/conditional_registrations-sets-002.md#r-a3778c48128b9a7a) · [条件 C-17f6c6cab0bdf00a](../../evidence/conditions-sets-009.md#c-17f6c6cab0bdf00a) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-fe123cb8e67d0103](../../evidence/parameters-sets-019.md#p-fe123cb8e67d0103) · [状态效果 S-7494ea8b8022d49f](../../evidence/state_effects-sets-025.md#s-7494ea8b8022d49f)

### static_slot_creation_candidates-002348

```text
(config)# default do-exec debug voip dsmp vofr subframe <number:0..5> <cr>
```

Handler ` RVA 0x18190E90 `；selector ` 0 `；EOL ` RVA 0x366F0CC0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

参数提示：` unsigned_number ` Payload type to debug。

[候选注册 R-a3778c48128b9a7a](../../evidence/conditional_registrations-sets-002.md#r-a3778c48128b9a7a) · [条件 C-17f6c6cab0bdf00a](../../evidence/conditions-sets-009.md#c-17f6c6cab0bdf00a) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-6e8328be77d075a0](../../evidence/parameters-sets-009.md#p-6e8328be77d075a0) · [状态效果 S-eb16ddb575571aff](../../evidence/state_effects-sets-050.md#s-eb16ddb575571aff)

### static_slot_creation_candidates-001075

```text
(config)# default do-exec debug voip dsp crash-dump <cr>
```

Handler ` RVA 0x18295630 `；selector ` 4 `；EOL ` RVA 0x3673B2F8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-2d25111ba1413abb](../../evidence/conditional_registrations-sets-001.md#r-2d25111ba1413abb) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-b86a2a2b6fde7d05](../../evidence/state_effects-sets-039.md#s-b86a2a2b6fde7d05)

### static_slot_creation_candidates-001795

```text
(config)# default do-exec debug voip dsp crash-dump detail <cr>
```

Handler ` RVA 0x18295630 `；selector ` 7 `；EOL ` RVA 0x3673AAD8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-2d25111ba1413abb](../../evidence/conditional_registrations-sets-001.md#r-2d25111ba1413abb) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-b86a2a2b6fde7d05](../../evidence/state_effects-sets-039.md#s-b86a2a2b6fde7d05)

### static_slot_creation_candidates-001835

```text
(config)# default do-exec debug voip dsp crash-dump error <cr>
```

Handler ` RVA 0x18295630 `；selector ` 9 `；EOL ` RVA 0x3673B2D0 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-2d25111ba1413abb](../../evidence/conditional_registrations-sets-001.md#r-2d25111ba1413abb) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-b86a2a2b6fde7d05](../../evidence/state_effects-sets-039.md#s-b86a2a2b6fde7d05)

### static_slot_creation_candidates-001821

```text
(config)# default do-exec debug voip dsp crash-dump jtag <cr>
```

Handler ` RVA 0x18295630 `；selector ` 8 `；EOL ` RVA 0x3673B028 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-2d25111ba1413abb](../../evidence/conditional_registrations-sets-001.md#r-2d25111ba1413abb) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-b86a2a2b6fde7d05](../../evidence/state_effects-sets-039.md#s-b86a2a2b6fde7d05)

### static_slot_creation_candidates-001808

```text
(config)# default do-exec debug voip dsp crash-dump keepalive <cr>
```

Handler ` RVA 0x18295630 `；selector ` 5 `；EOL ` RVA 0x3673AD80 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-2d25111ba1413abb](../../evidence/conditional_registrations-sets-001.md#r-2d25111ba1413abb) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-b86a2a2b6fde7d05](../../evidence/state_effects-sets-039.md#s-b86a2a2b6fde7d05)

### static_slot_creation_candidates-000382

```text
(config)# default do-exec debug voip em-profile <cr>
```

Handler ` RVA 0x17AE9FC0 `；selector ` 0 `；EOL ` RVA 0x36507D30 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-9d3ace11218657d1](../../evidence/conditional_registrations-sets-002.md#r-9d3ace11218657d1) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-b86a2a2b6fde7d05](../../evidence/state_effects-sets-039.md#s-b86a2a2b6fde7d05)

### static_slot_creation_candidates-000959

```text
(config)# default do-exec debug voip enum detail <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x36021A10 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-b8a89f1a9a878d84](../../evidence/conditional_registrations-sets-002.md#r-b8a89f1a9a878d84) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-214638f1b054f545](../../evidence/state_effects-sets-008.md#s-214638f1b054f545)

### static_slot_creation_candidates-000989

```text
(config)# default do-exec debug voip enum summary <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x36021CB8 `。

模式根 ` RVA 0x341168F8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,1,0] `。

[候选注册 R-b8a89f1a9a878d84](../../evidence/conditional_registrations-sets-002.md#r-b8a89f1a9a878d84) · [条件 C-72f663df324fea00](../../evidence/conditions-sets-044.md#c-72f663df324fea00) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-214638f1b054f545](../../evidence/state_effects-sets-008.md#s-214638f1b054f545)

