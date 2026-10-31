# eigrp_af_intf_vnet_submode · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-007774

```text
(config-router-af-int-vnet)# add-paths <number:1..4> <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 61 `；EOL ` RVA 0x3468F1A8 `。

模式根 ` RVA 0x3468BD38 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of add paths to be advertised。

[条件 C-b3a5a55be151a95c](../../evidence/conditions-sets-069.md#c-b3a5a55be151a95c) · [参数 P-d9e30876d9d95a79](../../evidence/parameters-sets-016.md#p-d9e30876d9d95a79)

### observed_connections-007786

```text
(config-router-af-int-vnet)# authentication key-chain <string> <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 50 `；EOL ` RVA 0x3468CFD0 `。

模式根 ` RVA 0x3468BD38 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` name of key-chain。

[条件 C-c50d0bf3e56c6162](../../evidence/conditions-sets-076.md#c-c50d0bf3e56c6162) · [参数 P-8c4400fbf1fd3209](../../evidence/parameters-sets-011.md#p-8c4400fbf1fd3209)

### observed_connections-007791

```text
(config-router-af-int-vnet)# authentication mode hmac-sha-256 <string> <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 51 `；EOL ` RVA 0x3468C4A8 `。

模式根 ` RVA 0x3468BD38 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Authentication key-string used to compute HMAC-SHA-256 hash (maximum 32 characters for clear text, 69 characters for AES encrypted and 66 characters for proprietary)。

[条件 C-90a82ad8ce892f27](../../evidence/conditions-sets-056.md#c-90a82ad8ce892f27) · [参数 P-0ab93308cb18788f](../../evidence/parameters-sets-001.md#p-0ab93308cb18788f) · [状态效果 S-94c4ccb6c4cfafd6](../../evidence/state_effects-sets-032.md#s-94c4ccb6c4cfafd6)

### observed_connections-007783

```text
(config-router-af-int-vnet)# authentication mode md5 <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 51 `；EOL ` RVA 0x3468C330 `。

模式根 ` RVA 0x3468BD38 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cc588668aaefe481](../../evidence/conditions-sets-079.md#c-cc588668aaefe481) · [状态效果 S-8db00efbdb586787](../../evidence/state_effects-sets-030.md#s-8db00efbdb586787)

### observed_connections-007754

```text
(config-router-af-int-vnet)# bandwidth-percent <number:1..999999> <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 54 `；EOL ` RVA 0x3468D680 `。

模式根 ` RVA 0x3468BD38 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Maximum bandwidth percentage that EIGRP may use。

[条件 C-60dacfd11c65b1d5](../../evidence/conditions-sets-038.md#c-60dacfd11c65b1d5) · [参数 P-8f3364dfcdbe1e0d](../../evidence/parameters-sets-011.md#p-8f3364dfcdbe1e0d)

### observed_connections-007743

```text
(config-router-af-int-vnet)# bfd <cr>
```

Handler ` RVA 0xF57A660 `；selector ` 52 `；EOL ` RVA 0x3468D9B0 `。

模式根 ` RVA 0x3468BD38 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6d2c51d8ae41e202](../../evidence/conditions-sets-042.md#c-6d2c51d8ae41e202)

### observed_connections-007744

```text
(config-router-af-int-vnet)# dampening-change <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 55 `；EOL ` RVA 0x3468DD38 `。

模式根 ` RVA 0x3468BD38 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4a029d0e28768c08](../../evidence/conditions-sets-029.md#c-4a029d0e28768c08) · [状态效果 S-a7ed54bc3ed1af74](../../evidence/state_effects-sets-035.md#s-a7ed54bc3ed1af74)

### observed_connections-007745

```text
(config-router-af-int-vnet)# dampening-interval <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 56 `；EOL ` RVA 0x3468E0C0 `。

模式根 ` RVA 0x3468BD38 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4ba59c5a4be6764a](../../evidence/conditions-sets-030.md#c-4ba59c5a4be6764a) · [状态效果 S-1c31281c4181c6a3](../../evidence/state_effects-sets-006.md#s-1c31281c4181c6a3)

### observed_connections-007777

```text
(config-router-af-int-vnet)# default add-paths <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 61 `；EOL ` RVA 0x3468F1A8 `。

模式根 ` RVA 0x3468BD38 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-deffc74b4156e9cd](../../evidence/conditions-sets-086.md#c-deffc74b4156e9cd) · [状态效果 S-307180e39e444982](../../evidence/state_effects-sets-011.md#s-307180e39e444982)

### observed_connections-007787

```text
(config-router-af-int-vnet)# default authentication key-chain <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 50 `；EOL ` RVA 0x3468CFD0 `。

模式根 ` RVA 0x3468BD38 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-53087731499de46d](../../evidence/conditions-sets-032.md#c-53087731499de46d) · [状态效果 S-307180e39e444982](../../evidence/state_effects-sets-011.md#s-307180e39e444982)

### observed_connections-007784

```text
(config-router-af-int-vnet)# default authentication mode <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 51 `；EOL ` RVA 0x3468C330 `。

模式根 ` RVA 0x3468BD38 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e8ad7487d41e0aff](../../evidence/conditions-sets-090.md#c-e8ad7487d41e0aff) · [状态效果 S-307180e39e444982](../../evidence/state_effects-sets-011.md#s-307180e39e444982)

### observed_connections-007756

```text
(config-router-af-int-vnet)# default bandwidth-percent <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 54 `；EOL ` RVA 0x3468D680 `。

模式根 ` RVA 0x3468BD38 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-bfab8f85683d21ae](../../evidence/conditions-sets-074.md#c-bfab8f85683d21ae) · [状态效果 S-307180e39e444982](../../evidence/state_effects-sets-011.md#s-307180e39e444982)

### observed_connections-007757

```text
(config-router-af-int-vnet)# default bfd <cr>
```

Handler ` RVA 0xF57A660 `；selector ` 52 `；EOL ` RVA 0x3468D9B0 `。

模式根 ` RVA 0x3468BD38 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6d2c51d8ae41e202](../../evidence/conditions-sets-042.md#c-6d2c51d8ae41e202) · [状态效果 S-307180e39e444982](../../evidence/state_effects-sets-011.md#s-307180e39e444982)

### observed_connections-007760

```text
(config-router-af-int-vnet)# default dampening-change <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 55 `；EOL ` RVA 0x3468DD38 `。

模式根 ` RVA 0x3468BD38 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-21a9dee6144950c0](../../evidence/conditions-sets-013.md#c-21a9dee6144950c0) · [状态效果 S-592137b50d7a2448](../../evidence/state_effects-sets-019.md#s-592137b50d7a2448)

### observed_connections-007764

```text
(config-router-af-int-vnet)# default dampening-interval <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 56 `；EOL ` RVA 0x3468E0C0 `。

模式根 ` RVA 0x3468BD38 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-fdd0f7d599c0e874](../../evidence/conditions-sets-098.md#c-fdd0f7d599c0e874) · [状态效果 S-7a8a832195ad912a](../../evidence/state_effects-sets-026.md#s-7a8a832195ad912a)

### observed_connections-007766

```text
(config-router-af-int-vnet)# default hello-interval <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 58 `；EOL ` RVA 0x3468E770 `。

模式根 ` RVA 0x3468BD38 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f1990839cb242d93](../../evidence/conditions-sets-093.md#c-f1990839cb242d93) · [状态效果 S-307180e39e444982](../../evidence/state_effects-sets-011.md#s-307180e39e444982)

### observed_connections-007769

```text
(config-router-af-int-vnet)# default hold-time <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 59 `；EOL ` RVA 0x3468EAC0 `。

模式根 ` RVA 0x3468BD38 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-412792bbaa156f27](../../evidence/conditions-sets-025.md#c-412792bbaa156f27) · [状态效果 S-307180e39e444982](../../evidence/state_effects-sets-011.md#s-307180e39e444982)

### observed_connections-007772

```text
(config-router-af-int-vnet)# default next-hop-self <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 60 `；EOL ` RVA 0x3468EDE8 `。

模式根 ` RVA 0x3468BD38 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-307180e39e444982](../../evidence/state_effects-sets-011.md#s-307180e39e444982)

### observed_connections-007775

```text
(config-router-af-int-vnet)# default passive-interface <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 62 `；EOL ` RVA 0x3468F498 `。

模式根 ` RVA 0x3468BD38 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-307180e39e444982](../../evidence/state_effects-sets-011.md#s-307180e39e444982)

### observed_connections-007778

```text
(config-router-af-int-vnet)# default shutdown <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 63 `；EOL ` RVA 0x3468F778 `。

模式根 ` RVA 0x3468BD38 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-307180e39e444982](../../evidence/state_effects-sets-011.md#s-307180e39e444982)

### observed_connections-007780

```text
(config-router-af-int-vnet)# default split-horizon <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 64 `；EOL ` RVA 0x3468FA58 `。

模式根 ` RVA 0x3468BD38 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-307180e39e444982](../../evidence/state_effects-sets-011.md#s-307180e39e444982)

### observed_connections-007789

```text
(config-router-af-int-vnet)# default stub-site wan-interface <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 66 `；EOL ` RVA 0x3468FD90 `。

模式根 ` RVA 0x3468BD38 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-036e8a92152de800](../../evidence/conditions-sets-002.md#c-036e8a92152de800) · [状态效果 S-307180e39e444982](../../evidence/state_effects-sets-011.md#s-307180e39e444982)

### observed_connections-007793

```text
(config-router-af-int-vnet)# default summary-address <address> <address> <cr>
```

Handler ` RVA 0xF5E07B0 `；selector ` 65 `；EOL ` RVA 0x3468C9D8 `。

模式根 ` RVA 0x3468BD38 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` Summary network address；` address ` Summary network mask。

[条件 C-57ec47eebaa6e786](../../evidence/conditions-sets-034.md#c-57ec47eebaa6e786) · [参数 P-f1e81614a51fe766](../../evidence/parameters-sets-018.md#p-f1e81614a51fe766) · [状态效果 S-307180e39e444982](../../evidence/state_effects-sets-011.md#s-307180e39e444982)

### observed_connections-007752

```text
(config-router-af-int-vnet)# default test-bandwidth <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 53 `；EOL ` RVA 0x3468D330 `。

模式根 ` RVA 0x3468BD38 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f28a190609a404e3](../../evidence/conditions-sets-094.md#c-f28a190609a404e3) · [状态效果 S-307180e39e444982](../../evidence/state_effects-sets-011.md#s-307180e39e444982)

### observed_connections-007762

```text
(config-router-af-int-vnet)# default test-delay <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 57 `；EOL ` RVA 0x3468E410 `。

模式根 ` RVA 0x3468BD38 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-cdcf9a7e53e90768](../../evidence/conditions-sets-079.md#c-cdcf9a7e53e90768) · [状态效果 S-307180e39e444982](../../evidence/state_effects-sets-011.md#s-307180e39e444982)

### observed_connections-007742

```text
(config-router-af-int-vnet)# exit-af-int-vnet <cr>
```

Handler ` RVA 0xF5747D0 `；selector ` 0 `；EOL ` RVA 0x346901A0 `。

模式根 ` RVA 0x3468BD38 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-92f9047c413ad32a](../../evidence/conditions-sets-057.md#c-92f9047c413ad32a)

### observed_connections-007765

```text
(config-router-af-int-vnet)# hello-interval <number:1..65535> <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 58 `；EOL ` RVA 0x3468E770 `。

模式根 ` RVA 0x3468BD38 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Seconds between hello transmissions。

[条件 C-e1b82d86405733b5](../../evidence/conditions-sets-087.md#c-e1b82d86405733b5) · [参数 P-d65bd75821ea42b4](../../evidence/parameters-sets-016.md#p-d65bd75821ea42b4)

### observed_connections-007768

```text
(config-router-af-int-vnet)# hold-time <number:1..65535> <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 59 `；EOL ` RVA 0x3468EAC0 `。

模式根 ` RVA 0x3468BD38 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Seconds before neighbor is considered down。

[条件 C-05f6470b8f808c41](../../evidence/conditions-sets-003.md#c-05f6470b8f808c41) · [参数 P-c11be18a4c28f3f3](../../evidence/parameters-sets-015.md#p-c11be18a4c28f3f3)

### observed_connections-007746

```text
(config-router-af-int-vnet)# next-hop-self <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 60 `；EOL ` RVA 0x3468EDE8 `。

模式根 ` RVA 0x3468BD38 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-007773

```text
(config-router-af-int-vnet)# no add-paths <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 61 `；EOL ` RVA 0x3468F1A8 `。

模式根 ` RVA 0x3468BD38 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-70a27f487a4d4b58](../../evidence/conditions-sets-044.md#c-70a27f487a4d4b58) · [状态效果 S-6145d189437dc25b](../../evidence/state_effects-sets-021.md#s-6145d189437dc25b)

### observed_connections-007785

```text
(config-router-af-int-vnet)# no authentication key-chain <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 50 `；EOL ` RVA 0x3468CFD0 `。

模式根 ` RVA 0x3468BD38 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a1bbdae43d438eda](../../evidence/conditions-sets-062.md#c-a1bbdae43d438eda) · [状态效果 S-6145d189437dc25b](../../evidence/state_effects-sets-021.md#s-6145d189437dc25b)

### observed_connections-007782

```text
(config-router-af-int-vnet)# no authentication mode <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 51 `；EOL ` RVA 0x3468C330 `。

模式根 ` RVA 0x3468BD38 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c8a4109d79394444](../../evidence/conditions-sets-077.md#c-c8a4109d79394444) · [状态效果 S-6145d189437dc25b](../../evidence/state_effects-sets-021.md#s-6145d189437dc25b)

### observed_connections-007753

```text
(config-router-af-int-vnet)# no bandwidth-percent <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 54 `；EOL ` RVA 0x3468D680 `。

模式根 ` RVA 0x3468BD38 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-3730d79398f687e7](../../evidence/conditions-sets-021.md#c-3730d79398f687e7) · [状态效果 S-6145d189437dc25b](../../evidence/state_effects-sets-021.md#s-6145d189437dc25b)

### observed_connections-007755

```text
(config-router-af-int-vnet)# no bfd <cr>
```

Handler ` RVA 0xF57A660 `；selector ` 52 `；EOL ` RVA 0x3468D9B0 `。

模式根 ` RVA 0x3468BD38 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-6d2c51d8ae41e202](../../evidence/conditions-sets-042.md#c-6d2c51d8ae41e202) · [状态效果 S-6145d189437dc25b](../../evidence/state_effects-sets-021.md#s-6145d189437dc25b)

### observed_connections-007758

```text
(config-router-af-int-vnet)# no dampening-change <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 55 `；EOL ` RVA 0x3468DD38 `。

模式根 ` RVA 0x3468BD38 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8eafc1dcfe51b423](../../evidence/conditions-sets-055.md#c-8eafc1dcfe51b423) · [状态效果 S-467c55a2f728fb52](../../evidence/state_effects-sets-015.md#s-467c55a2f728fb52)

### observed_connections-007761

```text
(config-router-af-int-vnet)# no dampening-interval <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 56 `；EOL ` RVA 0x3468E0C0 `。

模式根 ` RVA 0x3468BD38 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-2c5734518a72f0ac](../../evidence/conditions-sets-017.md#c-2c5734518a72f0ac) · [状态效果 S-871e389c881a31fa](../../evidence/state_effects-sets-029.md#s-871e389c881a31fa)

### observed_connections-007763

```text
(config-router-af-int-vnet)# no hello-interval <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 58 `；EOL ` RVA 0x3468E770 `。

模式根 ` RVA 0x3468BD38 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-43f84c08f701697c](../../evidence/conditions-sets-027.md#c-43f84c08f701697c) · [状态效果 S-6145d189437dc25b](../../evidence/state_effects-sets-021.md#s-6145d189437dc25b)

### observed_connections-007767

```text
(config-router-af-int-vnet)# no hold-time <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 59 `；EOL ` RVA 0x3468EAC0 `。

模式根 ` RVA 0x3468BD38 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-deaea85df986b3b0](../../evidence/conditions-sets-086.md#c-deaea85df986b3b0) · [状态效果 S-6145d189437dc25b](../../evidence/state_effects-sets-021.md#s-6145d189437dc25b)

### observed_connections-007770

```text
(config-router-af-int-vnet)# no next-hop-self <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 60 `；EOL ` RVA 0x3468EDE8 `。

模式根 ` RVA 0x3468BD38 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-6145d189437dc25b](../../evidence/state_effects-sets-021.md#s-6145d189437dc25b)

### observed_connections-007771

```text
(config-router-af-int-vnet)# no passive-interface <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 62 `；EOL ` RVA 0x3468F498 `。

模式根 ` RVA 0x3468BD38 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-6145d189437dc25b](../../evidence/state_effects-sets-021.md#s-6145d189437dc25b)

### observed_connections-007776

```text
(config-router-af-int-vnet)# no shutdown <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 63 `；EOL ` RVA 0x3468F778 `。

模式根 ` RVA 0x3468BD38 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-6145d189437dc25b](../../evidence/state_effects-sets-021.md#s-6145d189437dc25b)

### observed_connections-007779

```text
(config-router-af-int-vnet)# no split-horizon <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 64 `；EOL ` RVA 0x3468FA58 `。

模式根 ` RVA 0x3468BD38 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-6145d189437dc25b](../../evidence/state_effects-sets-021.md#s-6145d189437dc25b)

### observed_connections-007788

```text
(config-router-af-int-vnet)# no stub-site wan-interface <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 66 `；EOL ` RVA 0x3468FD90 `。

模式根 ` RVA 0x3468BD38 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-036e8a92152de800](../../evidence/conditions-sets-002.md#c-036e8a92152de800) · [状态效果 S-6145d189437dc25b](../../evidence/state_effects-sets-021.md#s-6145d189437dc25b)

### observed_connections-007792

```text
(config-router-af-int-vnet)# no summary-address <address> <address> <cr>
```

Handler ` RVA 0xF5E07B0 `；selector ` 65 `；EOL ` RVA 0x3468C9D8 `。

模式根 ` RVA 0x3468BD38 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` Summary network address；` address ` Summary network mask。

[条件 C-57ec47eebaa6e786](../../evidence/conditions-sets-034.md#c-57ec47eebaa6e786) · [参数 P-f1e81614a51fe766](../../evidence/parameters-sets-018.md#p-f1e81614a51fe766) · [状态效果 S-6145d189437dc25b](../../evidence/state_effects-sets-021.md#s-6145d189437dc25b)

### observed_connections-007750

```text
(config-router-af-int-vnet)# no test-bandwidth <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 53 `；EOL ` RVA 0x3468D330 `。

模式根 ` RVA 0x3468BD38 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7d62bfff57e7f1b0](../../evidence/conditions-sets-049.md#c-7d62bfff57e7f1b0) · [状态效果 S-6145d189437dc25b](../../evidence/state_effects-sets-021.md#s-6145d189437dc25b)

### observed_connections-007759

```text
(config-router-af-int-vnet)# no test-delay <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 57 `；EOL ` RVA 0x3468E410 `。

模式根 ` RVA 0x3468BD38 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-44202dd1405bbd59](../../evidence/conditions-sets-027.md#c-44202dd1405bbd59) · [状态效果 S-6145d189437dc25b](../../evidence/state_effects-sets-021.md#s-6145d189437dc25b)

### observed_connections-007747

```text
(config-router-af-int-vnet)# passive-interface <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 62 `；EOL ` RVA 0x3468F498 `。

模式根 ` RVA 0x3468BD38 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-007748

```text
(config-router-af-int-vnet)# shutdown <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 63 `；EOL ` RVA 0x3468F778 `。

模式根 ` RVA 0x3468BD38 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-007749

```text
(config-router-af-int-vnet)# split-horizon <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 64 `；EOL ` RVA 0x3468FA58 `。

模式根 ` RVA 0x3468BD38 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-007781

```text
(config-router-af-int-vnet)# stub-site wan-interface <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 66 `；EOL ` RVA 0x3468FD90 `。

模式根 ` RVA 0x3468BD38 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-036e8a92152de800](../../evidence/conditions-sets-002.md#c-036e8a92152de800)

### observed_connections-007790

```text
(config-router-af-int-vnet)# summary-address <address> <address> <cr>
```

Handler ` RVA 0xF5E07B0 `；selector ` 65 `；EOL ` RVA 0x3468C9D8 `。

模式根 ` RVA 0x3468BD38 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Summary network address；` address ` Summary network mask。

[条件 C-57ec47eebaa6e786](../../evidence/conditions-sets-034.md#c-57ec47eebaa6e786) · [参数 P-f1e81614a51fe766](../../evidence/parameters-sets-018.md#p-f1e81614a51fe766)

### observed_connections-007795

```text
(config-router-af-int-vnet)# summary-address <prefix:dynamic> <cr>
```

Handler ` RVA 0xF5E07B0 `；selector ` 65 `；EOL ` RVA 0x3468C9D8 `。

模式根 ` RVA 0x3468BD38 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` Summary &lt;network&gt;/&lt;length&gt;, e.g. 192.168.0.0/16。

[条件 C-7f2b62a03e793065](../../evidence/conditions-sets-049.md#c-7f2b62a03e793065) · [缺口 G-15eea26994c03ea3](../../evidence/gaps-sets-001.md#g-15eea26994c03ea3) · [参数 P-e9356cf5da98bdf2](../../evidence/parameters-sets-017.md#p-e9356cf5da98bdf2) · [状态效果 S-9dd39c77d64e8428](../../evidence/state_effects-sets-034.md#s-9dd39c77d64e8428)

### observed_connections-007751

```text
(config-router-af-int-vnet)# test-bandwidth <number:1..4294967295> <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 53 `；EOL ` RVA 0x3468D330 `。

模式根 ` RVA 0x3468BD38 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` &lt;1-4294967295&gt; bandwidth in kilobits per second。

[条件 C-9c8bc2a98a2afaa6](../../evidence/conditions-sets-060.md#c-9c8bc2a98a2afaa6) · [参数 P-50b3828babcea402](../../evidence/parameters-sets-007.md#p-50b3828babcea402)

### observed_connections-007794

```text
(config-router-af-int-vnet)# test-delay <?general_to_number_action@555589be23e8> <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 57 `；EOL ` RVA 0x3468E410 `。

模式根 ` RVA 0x3468BD38 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-04fbd0ecf364b637](../../evidence/conditions-sets-002.md#c-04fbd0ecf364b637) · [缺口 G-9cbddcc110e6b61f](../../evidence/gaps-sets-006.md#g-9cbddcc110e6b61f)
