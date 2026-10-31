# interface · 六个基础模式的历史连接

[模式索引](README.md) · [总索引](../../README.md)

### path-067297

```text
(config-if)# ip access-group common <number:1..199> <number:1..199> in <cr>
```

Handler ` RVA 0xCF2D130 `；selector ` 1 `；EOL ` RVA 0x33D3CD10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` IP access list common (standard or extended)；` unsigned_number ` IP access list regular (standard or extended)。

[条件 C-93eab30263c56c7b](../../evidence/conditions-sets-057.md#c-93eab30263c56c7b) · [参数 P-7c162cbf9baa26f5](../../evidence/parameters-sets-010.md#p-7c162cbf9baa26f5) · [状态效果 S-96ba62ccd7e500d7](../../evidence/state_effects-sets-032.md#s-96ba62ccd7e500d7)

### path-067299

```text
(config-if)# ip access-group common <number:1..199> <number:1..199> out <cr>
```

Handler ` RVA 0xCF2D130 `；selector ` 2 `；EOL ` RVA 0x33D3CFC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` IP access list common (standard or extended)；` unsigned_number ` IP access list regular (standard or extended)。

[条件 C-93eab30263c56c7b](../../evidence/conditions-sets-057.md#c-93eab30263c56c7b) · [参数 P-7c162cbf9baa26f5](../../evidence/parameters-sets-010.md#p-7c162cbf9baa26f5) · [状态效果 S-b9d7c862edf5beb1](../../evidence/state_effects-sets-039.md#s-b9d7c862edf5beb1)

### path-066678

```text
(config-if)# ip access-group common <number:1..199> in <cr>
```

Handler ` RVA 0xCF2D130 `；selector ` 1 `；EOL ` RVA 0x33D3C750 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` IP access list common (standard or extended)。

[条件 C-93eab30263c56c7b](../../evidence/conditions-sets-057.md#c-93eab30263c56c7b) · [参数 P-c356925545084349](../../evidence/parameters-sets-015.md#p-c356925545084349)

### path-066679

```text
(config-if)# ip access-group common <number:1..199> out <cr>
```

Handler ` RVA 0xCF2D130 `；selector ` 2 `；EOL ` RVA 0x33D3C9F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` IP access list common (standard or extended)。

[条件 C-93eab30263c56c7b](../../evidence/conditions-sets-057.md#c-93eab30263c56c7b) · [参数 P-c356925545084349](../../evidence/parameters-sets-015.md#p-c356925545084349)

### path-063507

```text
(config-if)# ip accounting <cr>
```

Handler ` RVA 0xCF2FEC0 `；selector ` 0 `；EOL ` RVA 0x33D22570 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b823da852a9b89ca](../../evidence/conditions-sets-071.md#c-b823da852a9b89ca) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-065527

```text
(config-if)# ip address <address> <address> <cr>
```

Handler ` RVA 0xCEC0830 `；selector ` 2 `；EOL ` RVA 0x33D286F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP address；` address ` IP subnet mask。

[条件 C-ace765cf1039ebf3](../../evidence/conditions-sets-067.md#c-ace765cf1039ebf3) · [参数 P-b9679102400b79db](../../evidence/parameters-sets-014.md#p-b9679102400b79db) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-067836

```text
(config-if)# ip address dhcp client-id <interface> <cr>
```

Handler ` RVA 0xCEC0830 `；selector ` 0 `；EOL ` RVA 0x33D27AF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c8d1ae8b52919d8a](../../evidence/conditions-sets-077.md#c-c8d1ae8b52919d8a) · [缺口 G-d3cf08fc741fb03c](../../evidence/gaps-sets-007.md#g-d3cf08fc741fb03c) · [参数 P-1ff432b43fdc0a4e](../../evidence/parameters-sets-003.md#p-1ff432b43fdc0a4e) · [状态效果 S-8b48b5daeddbaabe](../../evidence/state_effects-sets-030.md#s-8b48b5daeddbaabe)

### path-064108

```text
(config-if)# ip address docsis <cr>
```

Handler ` RVA 0xCEC0830 `；selector ` 0 `；EOL ` RVA 0x33D27AF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3a4e3c9d00c5cad4](../../evidence/conditions-sets-023.md#c-3a4e3c9d00c5cad4) · [状态效果 S-775c53a0f86b0c93](../../evidence/state_effects-sets-025.md#s-775c53a0f86b0c93)

### path-066902

```text
(config-if)# ip address slarp retry <number:1..60> <cr>
```

Handler ` RVA 0xEF34510 `；selector ` 0 `；EOL ` RVA 0x34481748 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Retry timer interval, from 1 to 60 seconds。

[条件 C-0d37103132e42789](../../evidence/conditions-sets-005.md#c-0d37103132e42789) · [参数 P-73c8ba5e4ec17a72](../../evidence/parameters-sets-009.md#p-73c8ba5e4ec17a72) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-064522

```text
(config-if)# ip auth-proxy <string> <cr>
```

Handler ` RVA 0xCBA5850 `；selector ` 16 `；EOL ` RVA 0x33BFE480 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of authenticaion/admission rule。

[条件 C-61151227a4e48383](../../evidence/conditions-sets-038.md#c-61151227a4e48383) · [参数 P-544fc19563c4f227](../../evidence/parameters-sets-007.md#p-544fc19563c4f227) · [状态效果 S-31520b55e3e4f166](../../evidence/state_effects-sets-011.md#s-31520b55e3e4f166)

### path-067362

```text
(config-if)# ip authentication key-chain eigrp <number:1..65535> <string> <cr>
```

Handler ` RVA 0xF58CAE0 `；selector ` 122 `；EOL ` RVA 0x346DDCD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` AS number；` string ` name of key-chain。

[条件 C-8c61ce7eb8b72f46](../../evidence/conditions-sets-054.md#c-8c61ce7eb8b72f46) · [参数 P-2d8a679b92f7baac](../../evidence/parameters-sets-004.md#p-2d8a679b92f7baac) · [状态效果 S-4af214c14f210766](../../evidence/state_effects-sets-016.md#s-4af214c14f210766)

### path-067354

```text
(config-if)# ip authentication mode eigrp <number:1..65535> md5 <cr>
```

Handler ` RVA 0xF58CAE0 `；selector ` 123 `；EOL ` RVA 0x346DD900 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` AS number。

[条件 C-17ddbd9f5229c56e](../../evidence/conditions-sets-009.md#c-17ddbd9f5229c56e) · [参数 P-1f4e1873a3000a40](../../evidence/parameters-sets-003.md#p-1f4e1873a3000a40) · [状态效果 S-8bd9fa7ad954d561](../../evidence/state_effects-sets-030.md#s-8bd9fa7ad954d561)

### path-066789

```text
(config-if)# ip bandwidth-percent eigrp <number:1..65535> <number:1..999999> <cr>
```

Handler ` RVA 0xF58CAE0 `；selector ` 124 `；EOL ` RVA 0x346DE0C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` AS number；` unsigned_number ` Maximum bandwidth percentage that EIGRP may use。

[条件 C-1d0d5447ad3de368](../../evidence/conditions-sets-011.md#c-1d0d5447ad3de368) · [参数 P-e42490c4ba55cc0f](../../evidence/parameters-sets-017.md#p-e42490c4ba55cc0f) · [状态效果 S-4af214c14f210766](../../evidence/state_effects-sets-016.md#s-4af214c14f210766)

### path-065519

```text
(config-if)# ip bgp fast-external-fallover permit <cr>
```

Handler ` RVA 0xF1C64C0 `；selector ` 1 `；EOL ` RVA 0x344CBA20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b6b12175d43d6ab9](../../evidence/conditions-sets-071.md#c-b6b12175d43d6ab9) · [状态效果 S-437b8f8fe5c2257b](../../evidence/state_effects-sets-015.md#s-437b8f8fe5c2257b)

### path-064132

```text
(config-if)# ip broadcast-address <address> <cr>
```

Handler ` RVA 0xCF31430 `；selector ` 0 `；EOL ` RVA 0x33D26F40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP broadcast address。

[条件 C-f9c89669a05e5f89](../../evidence/conditions-sets-096.md#c-f9c89669a05e5f89) · [参数 P-670e641e142ca3b6](../../evidence/parameters-sets-008.md#p-670e641e142ca3b6) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-066926

```text
(config-if)# ip cef accounting non-recursive internal <cr>
```

Handler ` RVA 0xB611D80 `；selector ` 0 `；EOL ` RVA 0x337C4EC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4e1d582b0107e102](../../evidence/conditions-sets-031.md#c-4e1d582b0107e102) · [状态效果 S-4a7013110d2939bb](../../evidence/state_effects-sets-016.md#s-4a7013110d2939bb)

### path-063479

```text
(config-if)# ip cgmp <cr>
```

Handler ` RVA 0xF676950 `；selector ` 0 `；EOL ` RVA 0x34734230 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8905dbb66d92b58e](../../evidence/conditions-sets-053.md#c-8905dbb66d92b58e)

### path-064188

```text
(config-if)# ip cgmp batch-joins <cr>
```

Handler ` RVA 0xF676370 `；selector ` 0 `；EOL ` RVA 0x34733F50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8905dbb66d92b58e](../../evidence/conditions-sets-053.md#c-8905dbb66d92b58e)

### path-064182

```text
(config-if)# ip cgmp process-leaves <cr>
```

Handler ` RVA 0xF676190 `；selector ` 0 `；EOL ` RVA 0x34733CA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8905dbb66d92b58e](../../evidence/conditions-sets-053.md#c-8905dbb66d92b58e)

### path-063440

```text
(config-if)# ip clear-dont-fragment <cr>
```

Handler ` RVA 0xCF33A50 `；selector ` 6 `；EOL ` RVA 0x33D20A50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a1d840fa0bc3aa08](../../evidence/conditions-sets-062.md#c-a1d840fa0bc3aa08) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-065816

```text
(config-if)# ip dampening-change eigrp <number:1..65535> <cr>
```

Handler ` RVA 0xF58CAE0 `；selector ` 125 `；EOL ` RVA 0x346DE4B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` AS number。

[条件 C-46bbca136099cb7f](../../evidence/conditions-sets-028.md#c-46bbca136099cb7f) · [参数 P-3cd701dfa13d30d9](../../evidence/parameters-sets-005.md#p-3cd701dfa13d30d9) · [状态效果 S-6e88d51a0ffaaadf](../../evidence/state_effects-sets-023.md#s-6e88d51a0ffaaadf)

### path-065841

```text
(config-if)# ip dampening-interval eigrp <number:1..65535> <cr>
```

Handler ` RVA 0xF58CAE0 `；selector ` 126 `；EOL ` RVA 0x346DE8D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` AS number。

[条件 C-5006f5833e280481](../../evidence/conditions-sets-031.md#c-5006f5833e280481) · [参数 P-40e18ec8b8a3cd70](../../evidence/parameters-sets-005.md#p-40e18ec8b8a3cd70) · [状态效果 S-4fd0383296bf4b97](../../evidence/state_effects-sets-017.md#s-4fd0383296bf4b97)

### path-065524

```text
(config-if)# ip ddns update <string> <cr>
```

Handler ` RVA 0xF480120 `；selector ` 0 `；EOL ` RVA 0x3465C870 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Method name。

[条件 C-4d242b7f557fc0f7](../../evidence/conditions-sets-030.md#c-4d242b7f557fc0f7) · [参数 P-ef6d4073a142a32f](../../evidence/parameters-sets-018.md#p-ef6d4073a142a32f) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-066684

```text
(config-if)# ip ddns update hostname <string> <cr>
```

Handler ` RVA 0xF47FF10 `；selector ` 0 `；EOL ` RVA 0x3465C4F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Host name。

[条件 C-51e0d82da1f4ca8c](../../evidence/conditions-sets-032.md#c-51e0d82da1f4ca8c) · [参数 P-75cefcf0e1a74e50](../../evidence/parameters-sets-009.md#p-75cefcf0e1a74e50) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-067344

```text
(config-if)# ip dhcp client authentication key-chain <string> <cr>
```

Handler ` RVA 0xF482E50 `；selector ` 0 `；EOL ` RVA 0x34657698 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Key-chain string。

[条件 C-da2f20f30b274b2c](../../evidence/conditions-sets-084.md#c-da2f20f30b274b2c) · [参数 P-2f2eb275e133eeb2](../../evidence/parameters-sets-004.md#p-2f2eb275e133eeb2) · [状态效果 S-8508772c452c25d6](../../evidence/state_effects-sets-028.md#s-8508772c452c25d6)

### path-066715

```text
(config-if)# ip dhcp client broadcast-flag set <cr>
```

Handler ` RVA 0xF476370 `；selector ` 0 `；EOL ` RVA 0x346544A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-aa396b3ac8bf9ab6](../../evidence/conditions-sets-066.md#c-aa396b3ac8bf9ab6) · [状态效果 S-f3ec1b423406af2d](../../evidence/state_effects-sets-052.md#s-f3ec1b423406af2d)

### path-066732

```text
(config-if)# ip dhcp client class-id <string> <cr>
```

Handler ` RVA 0xF478440 `；selector ` 0 `；EOL ` RVA 0x34655480 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Class-ID string, truncated to 200 characters。

[条件 C-ce3e33be74d19a0d](../../evidence/conditions-sets-079.md#c-ce3e33be74d19a0d) · [参数 P-fd6f882536d191c1](../../evidence/parameters-sets-019.md#p-fd6f882536d191c1) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-067880

```text
(config-if)# ip dhcp client class-id hex <hex-string> <cr>
```

Handler ` RVA 0xF478440 `；selector ` 0 `；EOL ` RVA 0x34655480 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` hexstring ` Class-ID in hex。

[条件 C-730bc617b8657922](../../evidence/conditions-sets-044.md#c-730bc617b8657922) · [缺口 G-0769909bcdf406ae](../../evidence/gaps-sets-001.md#g-0769909bcdf406ae) · [参数 P-416546e0abfabdab](../../evidence/parameters-sets-006.md#p-416546e0abfabdab) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-067840

```text
(config-if)# ip dhcp client client-id <interface> <cr>
```

Handler ` RVA 0xF477630 `；selector ` 0 `；EOL ` RVA 0x34653FB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c9740acc1ff82c2a](../../evidence/conditions-sets-078.md#c-c9740acc1ff82c2a) · [缺口 G-569c03e423bd9ae7](../../evidence/gaps-sets-003.md#g-569c03e423bd9ae7) · [参数 P-d2a8c97b5435877e](../../evidence/parameters-sets-016.md#p-d2a8c97b5435877e) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-067325

```text
(config-if)# ip dhcp client client-id ascii <string> <cr>
```

Handler ` RVA 0xF477630 `；selector ` 0 `；EOL ` RVA 0x34653FB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Client-ID string。

[条件 C-83ae78aa52c871eb](../../evidence/conditions-sets-051.md#c-83ae78aa52c871eb) · [参数 P-3b3c71913b91a0a7](../../evidence/parameters-sets-005.md#p-3b3c71913b91a0a7) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-067331

```text
(config-if)# ip dhcp client default-router distance <number:1..255> <cr>
```

Handler ` RVA 0xF477CD0 `；selector ` 0 `；EOL ` RVA 0x34655C38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Configure default router administrative distance。

[条件 C-9a316e1e87400b70](../../evidence/conditions-sets-060.md#c-9a316e1e87400b70) · [参数 P-071d81f09aa88a17](../../evidence/parameters-sets-001.md#p-071d81f09aa88a17) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-066730

```text
(config-if)# ip dhcp client hostname <string> <cr>
```

Handler ` RVA 0xF478870 `；selector ` 0 `；EOL ` RVA 0x346558B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Hostname string。

[条件 C-707eb589f13bb70b](../../evidence/conditions-sets-043.md#c-707eb589f13bb70b) · [参数 P-b223c5609b14b80e](../../evidence/parameters-sets-014.md#p-b223c5609b14b80e) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-066740

```text
(config-if)# ip dhcp client lease <number:0..365> <cr>
```

Handler ` RVA 0xF478A50 `；selector ` 0 `；EOL ` RVA 0x34656DB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Days。

[条件 C-53f42b757668bcf6](../../evidence/conditions-sets-033.md#c-53f42b757668bcf6) · [参数 P-b4fae3db07b4cee5](../../evidence/parameters-sets-014.md#p-b4fae3db07b4cee5) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-067896

```text
(config-if)# ip dhcp client option <number:1..254> hex <hex-string> <cr>
```

Handler ` RVA 0xF474B20 `；selector ` 0 `；EOL ` RVA 0x346566D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` DHCP option code (1-254)；` hexstring ` Data is a hexadecimal string。

[条件 C-30b1375f9b0bbbee](../../evidence/conditions-sets-019.md#c-30b1375f9b0bbbee) · [缺口 G-af77bc30cb47b2fc](../../evidence/gaps-sets-006.md#g-af77bc30cb47b2fc) · [参数 P-c93f87d993bf983b](../../evidence/parameters-sets-015.md#p-c93f87d993bf983b) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-067585

```text
(config-if)# ip dhcp client option <number:1..254> ip <address> <cr>
```

Handler ` RVA 0xF474B20 `；selector ` 0 `；EOL ` RVA 0x346566D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` DHCP option code (1-254)；` address ` IP Address。

[条件 C-2e034d381d124f07](../../evidence/conditions-sets-018.md#c-2e034d381d124f07) · [参数 P-3dca2d5b51d62231](../../evidence/parameters-sets-005.md#p-3dca2d5b51d62231) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-065623

```text
(config-if)# ip dhcp client process-requested-options-only <cr>
```

Handler ` RVA 0xF478C90 `；selector ` 0 `；EOL ` RVA 0x34657A70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-21d4b1e6497c9292](../../evidence/conditions-sets-013.md#c-21d4b1e6497c9292) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-065642

```text
(config-if)# ip dhcp client request <cr>
```

Handler ` RVA 0xF477100 `；selector ` 0 `；EOL ` RVA 0x34653940 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-21d4b1e6497c9292](../../evidence/conditions-sets-013.md#c-21d4b1e6497c9292) · [状态效果 S-5234875b836ea826](../../evidence/state_effects-sets-018.md#s-5234875b836ea826)

### path-067882

```text
(config-if)# ip dhcp client request option <number:1..254> <cr>
```

Handler ` RVA 0xF477100 `；selector ` 0 `；EOL ` RVA 0x34653940 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` DHCP option code (1-254)。

[条件 C-21688d950a42731e](../../evidence/conditions-sets-013.md#c-21688d950a42731e) · [缺口 G-243702a92d706e61](../../evidence/gaps-sets-002.md#g-243702a92d706e61) · [参数 P-2e39c10a8e0dee2b](../../evidence/parameters-sets-004.md#p-2e39c10a8e0dee2b) · [状态效果 S-f432be62f7b89121](../../evidence/state_effects-sets-052.md#s-f432be62f7b89121)

### path-067339

```text
(config-if)# ip dhcp client route distance <number:0..254> <cr>
```

Handler ` RVA 0xF477B60 `；selector ` 0 `；EOL ` RVA 0x34656328 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` enter distance range (0-254)。

[条件 C-8c6a9bc58130396f](../../evidence/conditions-sets-054.md#c-8c6a9bc58130396f) · [参数 P-e958347a2c8b4aee](../../evidence/parameters-sets-017.md#p-e958347a2c8b4aee) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-067335

```text
(config-if)# ip dhcp client route track <number:1..32767> <cr>
```

Handler ` RVA 0xF477E40 `；selector ` 0 `；EOL ` RVA 0x34656000 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Tracked object number。

[条件 C-8b698a792c269283](../../evidence/conditions-sets-054.md#c-8b698a792c269283) · [参数 P-a29b55c70b1820a6](../../evidence/parameters-sets-012.md#p-a29b55c70b1820a6) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-066742

```text
(config-if)# ip dhcp client update dns <cr>
```

Handler ` RVA 0xF476B70 `；selector ` 0 `；EOL ` RVA 0x34657208 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-21d4b1e6497c9292](../../evidence/conditions-sets-013.md#c-21d4b1e6497c9292) · [状态效果 S-2de5296b1d739429](../../evidence/state_effects-sets-010.md#s-2de5296b1d739429)

### path-067330

```text
(config-if)# ip dhcp client vendor-class ascii <string> <cr>
```

Handler ` RVA 0xF477FC0 `；selector ` 1 `；EOL ` RVA 0x34655108 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Vendor class data as string。

[条件 C-4f93d92b04b896d9](../../evidence/conditions-sets-031.md#c-4f93d92b04b896d9) · [参数 P-45a889aba25f6ee9](../../evidence/parameters-sets-006.md#p-45a889aba25f6ee9) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-066720

```text
(config-if)# ip dhcp client vendor-class disable <cr>
```

Handler ` RVA 0xF477FC0 `；selector ` 4 `；EOL ` RVA 0x34654840 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-21d4b1e6497c9292](../../evidence/conditions-sets-013.md#c-21d4b1e6497c9292) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-067881

```text
(config-if)# ip dhcp client vendor-class hex <hex-string> <cr>
```

Handler ` RVA 0xF477FC0 `；selector ` 2 `；EOL ` RVA 0x34654E20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` hexstring ` Vendor class data as hex。

[条件 C-671b945a05fce77d](../../evidence/conditions-sets-040.md#c-671b945a05fce77d) · [缺口 G-beb0f1524ac77e5b](../../evidence/gaps-sets-007.md#g-beb0f1524ac77e5b) · [参数 P-bde1a659147b56ce](../../evidence/parameters-sets-014.md#p-bde1a659147b56ce) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-066723

```text
(config-if)# ip dhcp client vendor-class mac-address <cr>
```

Handler ` RVA 0xF477FC0 `；selector ` 3 `；EOL ` RVA 0x34654AE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-21d4b1e6497c9292](../../evidence/conditions-sets-013.md#c-21d4b1e6497c9292) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-066693

```text
(config-if)# ip dhcp limit lease <number:1..65535> <cr>
```

Handler ` RVA 0xD24EA50 `；selector ` 0 `；EOL ` RVA 0x33DD25D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of dhcp lease per interface。

[条件 C-e372636c2d677bdc](../../evidence/conditions-sets-088.md#c-e372636c2d677bdc) · [参数 P-e5cd204b2169991e](../../evidence/parameters-sets-017.md#p-e5cd204b2169991e) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-066710

```text
(config-if)# ip dhcp relay information check-reply <cr>
```

Handler ` RVA 0xD24D6C0 `；selector ` 0 `；EOL ` RVA 0x33DD3A58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7a8b17fb4501a46e](../../evidence/conditions-sets-048.md#c-7a8b17fb4501a46e) · [状态效果 S-971898abaffb970a](../../evidence/state_effects-sets-032.md#s-971898abaffb970a)

### path-067300

```text
(config-if)# ip dhcp relay information option server-id-override <cr>
```

Handler ` RVA 0xD24E470 `；selector ` 0 `；EOL ` RVA 0x33DD2C48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-21d4b1e6497c9292](../../evidence/conditions-sets-013.md#c-21d4b1e6497c9292) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-067580

```text
(config-if)# ip dhcp relay information option subscriber-id <string> <cr>
```

Handler ` RVA 0xD24DDF0 `；selector ` 0 `；EOL ` RVA 0x33DD2FB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Subscriber identifier string。

[条件 C-5fe66ec12fc84fce](../../evidence/conditions-sets-037.md#c-5fe66ec12fc84fce) · [参数 P-1943fdc6e9aca77f](../../evidence/parameters-sets-002.md#p-1943fdc6e9aca77f) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-067316

```text
(config-if)# ip dhcp relay information option vpn-id <cr>
```

Handler ` RVA 0xD24D900 `；selector ` 0 `；EOL ` RVA 0x33DD32E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0256e0a82576e88f](../../evidence/conditions-sets-001.md#c-0256e0a82576e88f) · [状态效果 S-bcf7c82d173d8946](../../evidence/state_effects-sets-040.md#s-bcf7c82d173d8946)

### path-066708

```text
(config-if)# ip dhcp relay information option-insert <cr>
```

Handler ` RVA 0xD24DB80 `；selector ` 0 `；EOL ` RVA 0x33DD36B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9ba8f327baa2b437](../../evidence/conditions-sets-060.md#c-9ba8f327baa2b437) · [状态效果 S-9778fbdd2a458619](../../evidence/state_effects-sets-032.md#s-9778fbdd2a458619)

### path-067314

```text
(config-if)# ip dhcp relay information policy-action drop <cr>
```

Handler ` RVA 0xD24D430 `；selector ` 0 `；EOL ` RVA 0x33DD3DD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7f79237cd65a171e](../../evidence/conditions-sets-049.md#c-7f79237cd65a171e) · [状态效果 S-5e3b44871d72cd7d](../../evidence/state_effects-sets-020.md#s-5e3b44871d72cd7d)

### path-066687

```text
(config-if)# ip dhcp relay information trusted <cr>
```

Handler ` RVA 0xD24CF30 `；selector ` 0 `；EOL ` RVA 0x33DD2938 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-21d4b1e6497c9292](../../evidence/conditions-sets-013.md#c-21d4b1e6497c9292) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-066701

```text
(config-if)# ip dhcp relay short-lease <number:60..3600> <cr>
```

Handler ` RVA 0xD24E5E0 `；selector ` 0 `；EOL ` RVA 0x33DD4648 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Short Lease (T1) in Seconds。

[条件 C-21d4b1e6497c9292](../../evidence/conditions-sets-013.md#c-21d4b1e6497c9292) · [参数 P-e5fbd474842f0de5](../../evidence/parameters-sets-017.md#p-e5fbd474842f0de5) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-067837

```text
(config-if)# ip dhcp relay source-interface <interface> <cr>
```

Handler ` RVA 0xD24E7F0 `；selector ` 0 `；EOL ` RVA 0x33DD4290 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-716f369452e213dd](../../evidence/conditions-sets-044.md#c-716f369452e213dd) · [缺口 G-8638de1a2a658856](../../evidence/gaps-sets-005.md#g-8638de1a2a658856) · [参数 P-78c8050bfa83f836](../../evidence/parameters-sets-009.md#p-78c8050bfa83f836) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-065520

```text
(config-if)# ip dhcp restrict-next-hop cdp <cr>
```

Handler ` RVA 0xD252580 `；selector ` 0 `；EOL ` RVA 0x33DD5080 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bb5acfbd3a54be61](../../evidence/conditions-sets-072.md#c-bb5acfbd3a54be61) · [状态效果 S-35cb7a65b9c916e3](../../evidence/state_effects-sets-012.md#s-35cb7a65b9c916e3)

### path-067306

```text
(config-if)# ip dhcp server use hardware-address client-id <cr>
```

Handler ` RVA 0xD252470 `；selector ` 0 `；EOL ` RVA 0x33DD4D28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-94916f2358a397f2](../../evidence/conditions-sets-057.md#c-94916f2358a397f2) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-067302

```text
(config-if)# ip dhcp server use subscriber-id client-id <cr>
```

Handler ` RVA 0xD251FF0 `；selector ` 0 `；EOL ` RVA 0x33DD4A30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-47fdb233fcc1c8c4](../../evidence/conditions-sets-028.md#c-47fdb233fcc1c8c4) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-068036

```text
(config-if)# ip dhcp snooping bridge-domain <number:dynamic> information option format-type circuit-id string <cr>
```

Handler ` RVA 0x15FA5820 `；selector ` 0 `；EOL ` RVA 0x35E7C2E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` DHCP Snooping  bridge-domain number。

[条件 C-04f4d6e0e3cdcda6](../../evidence/conditions-sets-002.md#c-04f4d6e0e3cdcda6) · [缺口 G-dad1203e479f83a4](../../evidence/gaps-sets-008.md#g-dad1203e479f83a4) · [参数 P-dcde8d639f08c624](../../evidence/parameters-sets-017.md#p-dcde8d639f08c624) · [状态效果 S-4939962f0b701c6c](../../evidence/state_effects-sets-016.md#s-4939962f0b701c6c)

### path-067887

```text
(config-if)# ip dhcp snooping information option allow-untrusted <cr>
```

Handler ` RVA 0x15FA4A10 `；selector ` 0 `；EOL ` RVA 0x35E7BD40 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7ea2609e3b5d082d](../../evidence/conditions-sets-049.md#c-7ea2609e3b5d082d) · [缺口 G-8939a31ae03dab15](../../evidence/gaps-sets-005.md#g-8939a31ae03dab15) · [状态效果 S-4f64fe7223fa44d0](../../evidence/state_effects-sets-017.md#s-4f64fe7223fa44d0)

### path-067855

```text
(config-if)# ip dhcp snooping limit rate <cr>
```

Handler ` RVA 0x15FA6450 `；selector ` 0 `；EOL ` RVA 0x35E7B718 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f8cf5b6f906db965](../../evidence/conditions-sets-096.md#c-f8cf5b6f906db965) · [缺口 G-8939a31ae03dab15](../../evidence/gaps-sets-005.md#g-8939a31ae03dab15) · [状态效果 S-4f64fe7223fa44d0](../../evidence/state_effects-sets-017.md#s-4f64fe7223fa44d0)

### path-067319

```text
(config-if)# ip dhcp snooping limit rate <number:1..4294967294> <cr>
```

Handler ` RVA 0x15FA6280 `；selector ` 0 `；EOL ` RVA 0x35E7D4E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` DHCP snooping rate limit。

[条件 C-ff9996e1f699a60c](../../evidence/conditions-sets-099.md#c-ff9996e1f699a60c) · [参数 P-3155985b8a83654b](../../evidence/parameters-sets-004.md#p-3155985b8a83654b) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-065528

```text
(config-if)# ip dhcp snooping packets <cr>
```

Handler ` RVA 0x15FA3540 `；selector ` 0 `；EOL ` RVA 0x35E7D160 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f08c2ae0cbc5c257](../../evidence/conditions-sets-093.md#c-f08c2ae0cbc5c257) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-067813

```text
(config-if)# ip dhcp snooping trust <cr>
```

Handler ` RVA 0x15FA5CF0 `；selector ` 0 `；EOL ` RVA 0x35E7B9B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1b075d15230eba55](../../evidence/conditions-sets-011.md#c-1b075d15230eba55) · [缺口 G-8939a31ae03dab15](../../evidence/gaps-sets-005.md#g-8939a31ae03dab15) · [状态效果 S-4f64fe7223fa44d0](../../evidence/state_effects-sets-017.md#s-4f64fe7223fa44d0)

### path-063465

```text
(config-if)# ip directed-broadcast <cr>
```

Handler ` RVA 0xCF31820 `；selector ` 0 `；EOL ` RVA 0x33D21310 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bcedd6975e417419](../../evidence/conditions-sets-073.md#c-bcedd6975e417419) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-066896

```text
(config-if)# ip dlep set heartbeat-threshold <number:2..8> <cr>
```

Handler ` RVA 0x132CD6E0 `；selector ` 5 `；EOL ` RVA 0x35A5B1F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Threshold of missed heartbeat messages。

[条件 C-393e2d4c2a5c6516](../../evidence/conditions-sets-022.md#c-393e2d4c2a5c6516) · [参数 P-abe08d9477b626b9](../../evidence/parameters-sets-013.md#p-abe08d9477b626b9) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-066923

```text
(config-if)# ip dlep set nbr-down-ack-timeout <number:1..50> <cr>
```

Handler ` RVA 0x132CD6E0 `；selector ` 7 `；EOL ` RVA 0x35A5B7D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Neighbor Down ACK timer duration in seconds。

[条件 C-910b50def0082bcc](../../evidence/conditions-sets-056.md#c-910b50def0082bcc) · [参数 P-fefe038d03c8a9fb](../../evidence/parameters-sets-019.md#p-fefe038d03c8a9fb) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-066946

```text
(config-if)# ip dlep set peer-description <string> <cr>
```

Handler ` RVA 0x132CD6E0 `；selector ` 13 `；EOL ` RVA 0x35A5C668 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Peer Description Name。

[条件 C-393e2d4c2a5c6516](../../evidence/conditions-sets-022.md#c-393e2d4c2a5c6516) · [参数 P-6a1cc9bdd4642746](../../evidence/parameters-sets-008.md#p-6a1cc9bdd4642746) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-066939

```text
(config-if)# ip dlep set peer-discovery-interval <number:1..60> <cr>
```

Handler ` RVA 0x132CD6E0 `；selector ` 12 `；EOL ` RVA 0x35A5C0A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Peer Discovery Interval timer duration in seconds。

[条件 C-393e2d4c2a5c6516](../../evidence/conditions-sets-022.md#c-393e2d4c2a5c6516) · [参数 P-e2d07a63f0a3f6c1](../../evidence/parameters-sets-017.md#p-e2d07a63f0a3f6c1) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-066943

```text
(config-if)# ip dlep set peer-discovery-mode ipv6 <cr>
```

Handler ` RVA 0x132CD6E0 `；selector ` 14 `；EOL ` RVA 0x35A5C398 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-393e2d4c2a5c6516](../../evidence/conditions-sets-022.md#c-393e2d4c2a5c6516) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-066935

```text
(config-if)# ip dlep set peer-heartbeat-interval <number:1..60> <cr>
```

Handler ` RVA 0x132CD6E0 `；selector ` 11 `；EOL ` RVA 0x35A5BDB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Peer Heartbeat Interval timer duration in seconds。

[条件 C-393e2d4c2a5c6516](../../evidence/conditions-sets-022.md#c-393e2d4c2a5c6516) · [参数 P-dc16e7b869eee81f](../../evidence/parameters-sets-017.md#p-dc16e7b869eee81f) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-066932

```text
(config-if)# ip dlep set peer-init-ack-timeout <number:1..60> <cr>
```

Handler ` RVA 0x132CD6E0 `；selector ` 10 `；EOL ` RVA 0x35A5BAC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Peer Init ACK timer duration in seconds。

[条件 C-10062258d0d6b4b6](../../evidence/conditions-sets-006.md#c-10062258d0d6b4b6) · [参数 P-3dbfa78001173ebd](../../evidence/parameters-sets-005.md#p-3dbfa78001173ebd) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-066912

```text
(config-if)# ip dlep set peer-terminate-ack-timeout <number:1..50> <cr>
```

Handler ` RVA 0x132CD6E0 `；selector ` 3 `；EOL ` RVA 0x35A5B4E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Peer Terminate ACK timer duration in seconds。

[条件 C-4a3e49bec0223dcd](../../evidence/conditions-sets-029.md#c-4a3e49bec0223dcd) · [参数 P-bd3d2034712af91f](../../evidence/parameters-sets-014.md#p-bd3d2034712af91f) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-065980

```text
(config-if)# ip dlep vtemplate <number:1..4096> <cr>
```

Handler ` RVA 0x132CD6E0 `；selector ` 1 `；EOL ` RVA 0x35A5AC38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Virtual Template number。

[条件 C-393e2d4c2a5c6516](../../evidence/conditions-sets-022.md#c-393e2d4c2a5c6516) · [参数 P-9d9c4edcfa3cd658](../../evidence/parameters-sets-012.md#p-9d9c4edcfa3cd658) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-065688

```text
(config-if)# ip dns view-group <string> <cr>
```

Handler ` RVA 0xD16F070 `；selector ` 0 `；EOL ` RVA 0x33D9BBE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` View-list name。

[条件 C-17ddbd9f5229c56e](../../evidence/conditions-sets-009.md#c-17ddbd9f5229c56e) · [参数 P-3ac6b36cb6cf95fa](../../evidence/parameters-sets-005.md#p-3ac6b36cb6cf95fa) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-068010

```text
(config-if)# ip flow monitor <?option@555588f5d9c8> sampler <cr>
```

Handler ` RVA 0xC1F7CA0 `；selector ` 0 `；EOL ` RVA 0x33A09BF0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c3b6d297b8502a5d](../../evidence/conditions-sets-076.md#c-c3b6d297b8502a5d) · [缺口 G-694ddce53cf83200](../../evidence/gaps-sets-004.md#g-694ddce53cf83200) · [状态效果 S-c2ce7cc0ebcaa1fe](../../evidence/state_effects-sets-041.md#s-c2ce7cc0ebcaa1fe)

### path-067741

```text
(config-if)# ip flow monitor <cr>
```

Handler ` RVA 0xC1F7D50 `；selector ` 0 `；EOL ` RVA 0x33A09EA8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-41ca83d0fea50e98](../../evidence/conditions-sets-026.md#c-41ca83d0fea50e98) · [缺口 G-1e71d71c7a56f389](../../evidence/gaps-sets-002.md#g-1e71d71c7a56f389) · [状态效果 S-c2ce7cc0ebcaa1fe](../../evidence/state_effects-sets-041.md#s-c2ce7cc0ebcaa1fe)

### path-064574

```text
(config-if)# ip flowspec disable <cr>
```

Handler ` RVA 0x1344F290 `；selector ` 0 `；EOL ` RVA 0x35A99478 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-17ddbd9f5229c56e](../../evidence/conditions-sets-009.md#c-17ddbd9f5229c56e) · [状态效果 S-46deb9b111468542](../../evidence/state_effects-sets-015.md#s-46deb9b111468542)

### path-064582

```text
(config-if)# ip header-compression disable-feedback <cr>
```

Handler ` RVA 0xD196200 `；selector ` 0 `；EOL ` RVA 0x33DAC7A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-af52c7cf8a2a5b96](../../evidence/conditions-sets-068.md#c-af52c7cf8a2a5b96) · [状态效果 S-77e9bd8e4cf16e19](../../evidence/state_effects-sets-025.md#s-77e9bd8e4cf16e19)

### path-066823

```text
(config-if)# ip hello-interval eigrp <number:1..65535> <number:1..65535> <cr>
```

Handler ` RVA 0xF58CAE0 `；selector ` 129 `；EOL ` RVA 0x346DECF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` AS number；` unsigned_number ` Seconds between hello transmissions。

[条件 C-380206e5e4622190](../../evidence/conditions-sets-022.md#c-380206e5e4622190) · [参数 P-ff15d9f07537350e](../../evidence/parameters-sets-019.md#p-ff15d9f07537350e) · [状态效果 S-4af214c14f210766](../../evidence/state_effects-sets-016.md#s-4af214c14f210766)

### path-064153

```text
(config-if)# ip helper-address <address> <cr>
```

Handler ` RVA 0xCF2C740 `；selector ` 5 `；EOL ` RVA 0x33D26650 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP destination address。

[条件 C-810b956dff7fe1e4](../../evidence/conditions-sets-050.md#c-810b956dff7fe1e4) · [参数 P-a26b2ec082138cb1](../../evidence/parameters-sets-012.md#p-a26b2ec082138cb1) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-065496

```text
(config-if)# ip helper-address global <address> <cr>
```

Handler ` RVA 0xCF2C740 `；selector ` 6 `；EOL ` RVA 0x33D263D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP destination address。

[条件 C-810b956dff7fe1e4](../../evidence/conditions-sets-050.md#c-810b956dff7fe1e4) · [参数 P-7706631a499848f4](../../evidence/parameters-sets-009.md#p-7706631a499848f4) · [状态效果 S-874374de6faf8e70](../../evidence/state_effects-sets-029.md#s-874374de6faf8e70)

### path-066681

```text
(config-if)# ip helper-address vrf <string> <address> <cr>
```

Handler ` RVA 0xCF2C740 `；selector ` 5 `；EOL ` RVA 0x33D260D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` VPN Routing/Forwarding instance name；` address ` IP destination address。

[条件 C-810b956dff7fe1e4](../../evidence/conditions-sets-050.md#c-810b956dff7fe1e4) · [参数 P-b1d6b4fa8e40b6bb](../../evidence/parameters-sets-013.md#p-b1d6b4fa8e40b6bb) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-066841

```text
(config-if)# ip hold-time eigrp <number:1..65535> <number:1..65535> <cr>
```

Handler ` RVA 0xF58CAE0 `；selector ` 130 `；EOL ` RVA 0x346DF0D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` AS number；` unsigned_number ` Seconds before neighbor is considered down。

[条件 C-40ad037d3744392a](../../evidence/conditions-sets-025.md#c-40ad037d3744392a) · [参数 P-03d929ec743c9f84](../../evidence/parameters-sets-001.md#p-03d929ec743c9f84) · [状态效果 S-4af214c14f210766](../../evidence/state_effects-sets-016.md#s-4af214c14f210766)

### path-065492

```text
(config-if)# ip idle-group <number:1..199> in <cr>
```

Handler ` RVA 0xCF2F980 `；selector ` 1 `；EOL ` RVA 0x33D272A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` IP access list (standard or extended)。

[条件 C-c4d236361d4d3a75](../../evidence/conditions-sets-076.md#c-c4d236361d4d3a75) · [参数 P-fe6bc6ffea762a5c](../../evidence/parameters-sets-019.md#p-fe6bc6ffea762a5c) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-065497

```text
(config-if)# ip idle-group <number:1..199> out <cr>
```

Handler ` RVA 0xCF2F980 `；selector ` 2 `；EOL ` RVA 0x33D27550 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` IP access list (standard or extended)。

[条件 C-c4d236361d4d3a75](../../evidence/conditions-sets-076.md#c-c4d236361d4d3a75) · [参数 P-fe6bc6ffea762a5c](../../evidence/parameters-sets-019.md#p-fe6bc6ffea762a5c) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-065595

```text
(config-if)# ip igmp access-group <number:1..199> <cr>
```

Handler ` RVA 0xF697F40 `；selector ` 0 `；EOL ` RVA 0x34730BC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Access list number。

[条件 C-74c640016e6cb340](../../evidence/conditions-sets-045.md#c-74c640016e6cb340) · [参数 P-d0266cc8a7a098aa](../../evidence/parameters-sets-016.md#p-d0266cc8a7a098aa)

### path-064259

```text
(config-if)# ip igmp explicit-tracking <cr>
```

Handler ` RVA 0xF6982A0 `；selector ` 1 `；EOL ` RVA 0x347316B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-44d9b7f1350ce585](../../evidence/conditions-sets-027.md#c-44d9b7f1350ce585)

### path-065939

```text
(config-if)# ip igmp filter <number:1..4294967295> <cr>
```

Handler ` RVA 0xE7AFD90 `；selector ` 0 `；EOL ` RVA 0x34339208 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` IGMP profile number。

[条件 C-5c1493fef4bdaef0](../../evidence/conditions-sets-036.md#c-5c1493fef4bdaef0) · [参数 P-7c4d6fdc95130520](../../evidence/parameters-sets-010.md#p-7c4d6fdc95130520)

### path-065560

```text
(config-if)# ip igmp helper-address <address> <cr>
```

Handler ` RVA 0xF6986B0 `；selector ` 2 `；EOL ` RVA 0x3472F2E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IGMP helper address。

[条件 C-14783ad46449e847](../../evidence/conditions-sets-008.md#c-14783ad46449e847) · [参数 P-43fec04ec244ab62](../../evidence/parameters-sets-006.md#p-43fec04ec244ab62)

### path-067839

```text
(config-if)# ip igmp helper-address udl <interface> <cr>
```

Handler ` RVA 0xF6987E0 `；selector ` 3 `；EOL ` RVA 0x3472EF28 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3e44e9c3bbb797c8](../../evidence/conditions-sets-024.md#c-3e44e9c3bbb797c8) · [缺口 G-19ebf47a40eb5790](../../evidence/gaps-sets-001.md#g-19ebf47a40eb5790) · [参数 P-9afcafc8097a7bd7](../../evidence/parameters-sets-012.md#p-9afcafc8097a7bd7)

### path-064223

```text
(config-if)# ip igmp iif-starg <cr>
```

Handler ` RVA 0xF699BA0 `；selector ` 11 `；EOL ` RVA 0x347301E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-44d9b7f1350ce585](../../evidence/conditions-sets-027.md#c-44d9b7f1350ce585)

### path-066736

```text
(config-if)# ip igmp immediate-leave group-list <number:1..99> <cr>
```

Handler ` RVA 0xF698DB0 `；selector ` 4 `；EOL ` RVA 0x34730FA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Access list number。

[条件 C-0a3fb80ea01d959f](../../evidence/conditions-sets-004.md#c-0a3fb80ea01d959f) · [参数 P-2c9b151bd74ab09e](../../evidence/parameters-sets-004.md#p-2c9b151bd74ab09e)

### path-065557

```text
(config-if)# ip igmp join-group <address> <cr>
```

Handler ` RVA 0xF69DC20 `；selector ` 1 `；EOL ` RVA 0x3472F680 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP group address。

[条件 C-44d9b7f1350ce585](../../evidence/conditions-sets-027.md#c-44d9b7f1350ce585) · [参数 P-32dcc30583b8097d](../../evidence/parameters-sets-004.md#p-32dcc30583b8097d)

### path-065546

```text
(config-if)# ip igmp last-member-query-count <number:1..7> <cr>
```

Handler ` RVA 0xF699100 `；selector ` 5 `；EOL ` RVA 0x3472EB70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Last member query count。

[条件 C-0816b9a2aa6c3945](../../evidence/conditions-sets-004.md#c-0816b9a2aa6c3945) · [参数 P-0b878dd52b3de017](../../evidence/parameters-sets-001.md#p-0b878dd52b3de017)

### path-065538

```text
(config-if)# ip igmp last-member-query-interval <number:100..25500> <cr>
```

Handler ` RVA 0xF699650 `；selector ` 6 `；EOL ` RVA 0x3472E820 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Last member query interval in milliseconds。

[条件 C-ca176435314e4c73](../../evidence/conditions-sets-078.md#c-ca176435314e4c73) · [参数 P-5f8f2cd128a8976c](../../evidence/parameters-sets-008.md#p-5f8f2cd128a8976c)

### path-065709

```text
(config-if)# ip igmp limit <number:1..64000> <cr>
```

Handler ` RVA 0xF6998A0 `；selector ` 8 `；EOL ` RVA 0x34732410 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Max Allowed State on this interface。

[条件 C-ce5cd2fe4865b33d](../../evidence/conditions-sets-079.md#c-ce5cd2fe4865b33d) · [参数 P-4d1e3637b04bd7a0](../../evidence/parameters-sets-006.md#p-4d1e3637b04bd7a0)

### path-067804

```text
(config-if)# ip igmp mroute-proxy <interface> <cr>
```

Handler ` RVA 0xF699FE0 `；selector ` 9 `；EOL ` RVA 0x34732B38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-eca4213a4b1951a5](../../evidence/conditions-sets-091.md#c-eca4213a4b1951a5) · [缺口 G-152abcd66837641a](../../evidence/gaps-sets-001.md#g-152abcd66837641a) · [参数 P-915a041ce2d4de7b](../../evidence/parameters-sets-011.md#p-915a041ce2d4de7b)

### path-065658

```text
(config-if)# ip igmp proxy-report-interval <number:1..18000> <cr>
```

Handler ` RVA 0xF69A550 `；selector ` 12 `；EOL ` RVA 0x34731D70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Report interval in seconds。

[条件 C-1b0de5af3a512566](../../evidence/conditions-sets-011.md#c-1b0de5af3a512566) · [参数 P-7fee05b10e19ec1f](../../evidence/parameters-sets-010.md#p-7fee05b10e19ec1f)

### path-064332

```text
(config-if)# ip igmp proxy-service <cr>
```

Handler ` RVA 0xF69A1F0 `；selector ` 13 `；EOL ` RVA 0x34732E78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-44d9b7f1350ce585](../../evidence/conditions-sets-027.md#c-44d9b7f1350ce585)

### path-065675

```text
(config-if)# ip igmp querier-timeout <number:60..300> <cr>
```

Handler ` RVA 0xF69A3A0 `；selector ` 14 `；EOL ` RVA 0x347320C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` timeout value in seconds 。

[条件 C-8f5af7d2d6931754](../../evidence/conditions-sets-055.md#c-8f5af7d2d6931754) · [参数 P-2abd0317b84094b3](../../evidence/parameters-sets-004.md#p-2abd0317b84094b3)

### path-065645

```text
(config-if)# ip igmp query-interval <number:1..18000> <cr>
```

Handler ` RVA 0xF69A7B0 `；selector ` 15 `；EOL ` RVA 0x34731A20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Query interval in seconds。

[条件 C-2cbe576a780ec5d3](../../evidence/conditions-sets-018.md#c-2cbe576a780ec5d3) · [参数 P-1cf32a3adbfc69b8](../../evidence/parameters-sets-003.md#p-1cf32a3adbfc69b8)

### path-065578

```text
(config-if)# ip igmp query-max-response-time <number:1..25> <cr>
```

Handler ` RVA 0xF69AA00 `；selector ` 16 `；EOL ` RVA 0x34730520 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` query response value in seconds。

[条件 C-62c0cff3758abb8c](../../evidence/conditions-sets-038.md#c-62c0cff3758abb8c) · [参数 P-d0d274775e07287d](../../evidence/parameters-sets-016.md#p-d0d274775e07287d)

### path-065537

```text
(config-if)# ip igmp robustness-variable <number:1..7> <cr>
```

Handler ` RVA 0xF699390 `；selector ` 7 `；EOL ` RVA 0x3472E4D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` robustness-variable。

[条件 C-1becf3d5306dc1c1](../../evidence/conditions-sets-011.md#c-1becf3d5306dc1c1) · [参数 P-b5b0cc3feaccfa54](../../evidence/parameters-sets-014.md#p-b5b0cc3feaccfa54)

### path-066883

```text
(config-if)# ip igmp snooping access-group <number:1..199> <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 49 `；EOL ` RVA 0x33A4C3B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Access list number。

[条件 C-dd12f00835b2a098](../../evidence/conditions-sets-085.md#c-dd12f00835b2a098) · [参数 P-8bf5721794ebe194](../../evidence/parameters-sets-011.md#p-8bf5721794ebe194)

### path-065993

```text
(config-if)# ip igmp snooping limit <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 50 `；EOL ` RVA 0x33A4C908 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2b93ded32a0d4d2c](../../evidence/conditions-sets-017.md#c-2b93ded32a0d4d2c) · [状态效果 S-9f4ead995c3dfcbe](../../evidence/state_effects-sets-034.md#s-9f4ead995c3dfcbe)

### path-066854

```text
(config-if)# ip igmp snooping tcn flood <cr>
```

Handler ` RVA 0xC30A700 `；selector ` 0 `；EOL ` RVA 0x33A4D0E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fa418c7656331879](../../evidence/conditions-sets-097.md#c-fa418c7656331879)

### path-067800

```text
(config-if)# ip igmp static-group * <cr>
```

Handler ` RVA 0xF69DC20 `；selector ` 11 `；EOL ` RVA 0x3472FA58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3830dc2ab87b64a7](../../evidence/conditions-sets-022.md#c-3830dc2ab87b64a7) · [缺口 G-3bd83ac0eb5cadb3](../../evidence/gaps-sets-003.md#g-3bd83ac0eb5cadb3) · [状态效果 S-23b3f44076170bed](../../evidence/state_effects-sets-008.md#s-23b3f44076170bed)

### path-065561

```text
(config-if)# ip igmp static-group <address> <cr>
```

Handler ` RVA 0xF69DC20 `；selector ` 11 `；EOL ` RVA 0x3472FA58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP group address。

[条件 C-44d9b7f1350ce585](../../evidence/conditions-sets-027.md#c-44d9b7f1350ce585) · [参数 P-ffee6b66fddcbfef](../../evidence/parameters-sets-019.md#p-ffee6b66fddcbfef)

### path-067364

```text
(config-if)# ip igmp tcn query count <number:1..10> <cr>
```

Handler ` RVA 0xF698910 `；selector ` 18 `；EOL ` RVA 0x34733290 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Count。

[条件 C-7ae3a8fa3d5e78e0](../../evidence/conditions-sets-048.md#c-7ae3a8fa3d5e78e0) · [参数 P-5f4d22594a2953bb](../../evidence/parameters-sets-008.md#p-5f4d22594a2953bb)

### path-067371

```text
(config-if)# ip igmp tcn query interval <number:1..255> <cr>
```

Handler ` RVA 0xF698B60 `；selector ` 19 `；EOL ` RVA 0x347335B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Query interval in seconds。

[条件 C-4af391df36bf19c5](../../evidence/conditions-sets-029.md#c-4af391df36bf19c5) · [参数 P-f279537c64d4adba](../../evidence/parameters-sets-018.md#p-f279537c64d4adba)

### path-064298

```text
(config-if)# ip igmp unidirectional-link <cr>
```

Handler ` RVA 0xF69AEA0 `；selector ` 20 `；EOL ` RVA 0x347327C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-44d9b7f1350ce585](../../evidence/conditions-sets-027.md#c-44d9b7f1350ce585)

### path-065567

```text
(config-if)# ip igmp upstream-proxy <string> <cr>
```

Handler ` RVA 0xF699D60 `；selector ` 10 `；EOL ` RVA 0x3472FEF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of class-map of type multicast-flows。

[条件 C-e670afd5180453cf](../../evidence/conditions-sets-089.md#c-e670afd5180453cf) · [参数 P-aa96275cff71ec2b](../../evidence/parameters-sets-013.md#p-aa96275cff71ec2b)

### path-065587

```text
(config-if)# ip igmp v3-query-max-response-time <number:1..3175> <cr>
```

Handler ` RVA 0xF69AC50 `；selector ` 17 `；EOL ` RVA 0x34730870 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` v3 query response value in seconds 。

[条件 C-7d7fdf4a74269066](../../evidence/conditions-sets-049.md#c-7d7fdf4a74269066) · [参数 P-69ec7c7ec7e7db32](../../evidence/parameters-sets-008.md#p-69ec7c7ec7e7db32)

### path-064383

```text
(config-if)# ip igmp v3lite <cr>
```

Handler ` RVA 0xF69B050 `；selector ` 21 `；EOL ` RVA 0x34733868 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-44d9b7f1350ce585](../../evidence/conditions-sets-027.md#c-44d9b7f1350ce585)

### path-065620

```text
(config-if)# ip igmp version <number:1..3> <cr>
```

Handler ` RVA 0xF69B200 `；selector ` 22 `；EOL ` RVA 0x34731428 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` version number。

[条件 C-dc5de1fa7b9884a3](../../evidence/conditions-sets-085.md#c-dc5de1fa7b9884a3) · [参数 P-3642e5d28f545229](../../evidence/parameters-sets-005.md#p-3642e5d28f545229)

### path-063434

```text
(config-if)# ip information-reply <cr>
```

Handler ` RVA 0xCF31A50 `；selector ` 0 `；EOL ` RVA 0x33D207A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a1d840fa0bc3aa08](../../evidence/conditions-sets-062.md#c-a1d840fa0bc3aa08) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-063505

```text
(config-if)# ip irdp <cr>
```

Handler ` RVA 0xE241F10 `；selector ` 7 `；EOL ` RVA 0x34285750 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-17ddbd9f5229c56e](../../evidence/conditions-sets-009.md#c-17ddbd9f5229c56e) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-066762

```text
(config-if)# ip irdp address <address> <signed:-2147483648..2147483647> <cr>
```

Handler ` RVA 0xE241F10 `；selector ` 1 `；EOL ` RVA 0x342869A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` address to advertise；` signed_number ` preference for this address。

[条件 C-2c41bbb6fea5d609](../../evidence/conditions-sets-017.md#c-2c41bbb6fea5d609) · [参数 P-3b5fbef2d9125ad2](../../evidence/parameters-sets-005.md#p-3b5fbef2d9125ad2) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-063517

```text
(config-if)# ip irdp holdtime <number:4..9000> <cr>
```

Handler ` RVA 0xE241F10 `；selector ` 3 `；EOL ` RVA 0x34286038 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` holdtime (default 1800 seconds)。

[条件 C-616b8bd53f5bc1cf](../../evidence/conditions-sets-038.md#c-616b8bd53f5bc1cf) · [参数 P-b49c4f1a23063f36](../../evidence/parameters-sets-014.md#p-b49c4f1a23063f36) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-065674

```text
(config-if)# ip irdp maxadvertinterval <number:4..1800> <cr>
```

Handler ` RVA 0xE241F10 `；selector ` 5 `；EOL ` RVA 0x34285D50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` maximum time between advertisements (default 600 seconds)。

[条件 C-96a87de50ce924fe](../../evidence/conditions-sets-058.md#c-96a87de50ce924fe) · [参数 P-6ff0f4283d2afb74](../../evidence/parameters-sets-009.md#p-6ff0f4283d2afb74) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-063510

```text
(config-if)# ip irdp minadvertinterval <number:3..1800> <cr>
```

Handler ` RVA 0xE241F10 `；selector ` 4 `；EOL ` RVA 0x34285CB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` minimum time between advertisements 		       (default 450 seconds)。

[条件 C-bc6e861a51c47e31](../../evidence/conditions-sets-073.md#c-bc6e861a51c47e31) · [参数 P-f6e17d1b7676ecc3](../../evidence/parameters-sets-018.md#p-f6e17d1b7676ecc3) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-064274

```text
(config-if)# ip irdp multicast <cr>
```

Handler ` RVA 0xE241F10 `；selector ` 6 `；EOL ` RVA 0x342859E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-17ddbd9f5229c56e](../../evidence/conditions-sets-009.md#c-17ddbd9f5229c56e) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-065703

```text
(config-if)# ip irdp preference <signed:-2147483648..2147483647> <cr>
```

Handler ` RVA 0xE241F10 `；selector ` 2 `；EOL ` RVA 0x34286618 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` signed_number ` preference for this address (higher values preferred)。

[条件 C-7ffadaa96ec2367c](../../evidence/conditions-sets-050.md#c-7ffadaa96ec2367c) · [参数 P-40321c64f06d9468](../../evidence/parameters-sets-005.md#p-40321c64f06d9468) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-067761

```text
(config-if)# ip load-sharing <?option@555588d17fb0> <cr>
```

Handler ` RVA 0xB611F90 `；selector ` 0 `；EOL ` RVA 0x337C3FE8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-32702d14b14f39cb](../../evidence/conditions-sets-020.md#c-32702d14b14f39cb) · [缺口 G-645ba67a3baa86ea](../../evidence/gaps-sets-004.md#g-645ba67a3baa86ea) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-063681

```text
(config-if)# ip load-sharing <cr>
```

Handler ` RVA 0xB611F90 `；selector ` 0 `；EOL ` RVA 0x337C3FE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bf03c4e632d7d999](../../evidence/conditions-sets-074.md#c-bf03c4e632d7d999) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-063462

```text
(config-if)# ip local-proxy-arp <cr>
```

Handler ` RVA 0xCF33350 `；selector ` 0 `；EOL ` RVA 0x33D21EA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a1d840fa0bc3aa08](../../evidence/conditions-sets-062.md#c-a1d840fa0bc3aa08) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-063430

```text
(config-if)# ip mask-reply <cr>
```

Handler ` RVA 0xCF31C20 `；selector ` 0 `；EOL ` RVA 0x33D20500 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a1d840fa0bc3aa08](../../evidence/conditions-sets-062.md#c-a1d840fa0bc3aa08) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-065847

```text
(config-if)# ip mfib cef input <cr>
```

Handler ` RVA 0x11904EB0 `；selector ` 4 `；EOL ` RVA 0x353752A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-17ddbd9f5229c56e](../../evidence/conditions-sets-009.md#c-17ddbd9f5229c56e) · [状态效果 S-ad70d940fd65828f](../../evidence/state_effects-sets-037.md#s-ad70d940fd65828f)

### path-065880

```text
(config-if)# ip mfib cef output <cr>
```

Handler ` RVA 0x11904EB0 `；selector ` 8 `；EOL ` RVA 0x35375548 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-17ddbd9f5229c56e](../../evidence/conditions-sets-009.md#c-17ddbd9f5229c56e) · [状态效果 S-ad70d940fd65828f](../../evidence/state_effects-sets-037.md#s-ad70d940fd65828f)

### path-064570

```text
(config-if)# ip mfib forwarding <cr>
```

Handler ` RVA 0x11904EB0 `；selector ` 2147483649 `；EOL ` RVA 0x35374FB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-61bf1f5eeff2d4da](../../evidence/conditions-sets-038.md#c-61bf1f5eeff2d4da) · [状态效果 S-ad70d940fd65828f](../../evidence/state_effects-sets-037.md#s-ad70d940fd65828f)

### path-065818

```text
(config-if)# ip mfib forwarding input <cr>
```

Handler ` RVA 0x11904EB0 `；selector ` 1 `；EOL ` RVA 0x35374A50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-17ddbd9f5229c56e](../../evidence/conditions-sets-009.md#c-17ddbd9f5229c56e) · [状态效果 S-ad70d940fd65828f](../../evidence/state_effects-sets-037.md#s-ad70d940fd65828f)

### path-065851

```text
(config-if)# ip mfib forwarding output <cr>
```

Handler ` RVA 0x11904EB0 `；selector ` 2 `；EOL ` RVA 0x35374CF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-17ddbd9f5229c56e](../../evidence/conditions-sets-009.md#c-17ddbd9f5229c56e) · [状态效果 S-ad70d940fd65828f](../../evidence/state_effects-sets-037.md#s-ad70d940fd65828f)

### path-065926

```text
(config-if)# ip mfib test adjacency <cr>
```

Handler ` RVA 0x11904EB0 `；selector ` 512 `；EOL ` RVA 0x35375D70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-17ddbd9f5229c56e](../../evidence/conditions-sets-009.md#c-17ddbd9f5229c56e) · [状态效果 S-ad70d940fd65828f](../../evidence/state_effects-sets-037.md#s-ad70d940fd65828f)

### path-065942

```text
(config-if)# ip mfib test headless <cr>
```

Handler ` RVA 0x11904EB0 `；selector ` 1024 `；EOL ` RVA 0x35376018 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-17ddbd9f5229c56e](../../evidence/conditions-sets-009.md#c-17ddbd9f5229c56e) · [状态效果 S-ad70d940fd65828f](../../evidence/state_effects-sets-037.md#s-ad70d940fd65828f)

### path-065899

```text
(config-if)# ip mfib test macfilter <cr>
```

Handler ` RVA 0x11904EB0 `；selector ` 32768 `；EOL ` RVA 0x35375AC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-17ddbd9f5229c56e](../../evidence/conditions-sets-009.md#c-17ddbd9f5229c56e) · [状态效果 S-ad70d940fd65828f](../../evidence/state_effects-sets-037.md#s-ad70d940fd65828f)

### path-065875

```text
(config-if)# ip mfib test mask <cr>
```

Handler ` RVA 0x11904EB0 `；selector ` 256 `；EOL ` RVA 0x35375820 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-17ddbd9f5229c56e](../../evidence/conditions-sets-009.md#c-17ddbd9f5229c56e) · [状态效果 S-ad70d940fd65828f](../../evidence/state_effects-sets-037.md#s-ad70d940fd65828f)

### path-064378

```text
(config-if)# ip mrm test-sender <cr>
```

Handler ` RVA 0xF666280 `；selector ` 0 `；EOL ` RVA 0x34720098 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7715cff1b97775ca](../../evidence/conditions-sets-046.md#c-7715cff1b97775ca) · [状态效果 S-ca56e26c93cea5d8](../../evidence/state_effects-sets-043.md#s-ca56e26c93cea5d8)

### path-063478

```text
(config-if)# ip mroute-cache <cr>
```

Handler ` RVA 0xF6D51D0 `；selector ` 0 `；EOL ` RVA 0x347348B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ccad116df910224a](../../evidence/conditions-sets-079.md#c-ccad116df910224a)

### path-067749

```text
(config-if)# ip mtu <number:dynamic> <cr>
```

Handler ` RVA 0xCF321C0 `；selector ` 3 `；EOL ` RVA 0x33D22E38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` MTU (bytes)。

[条件 C-606a9712b5ed5e8e](../../evidence/conditions-sets-037.md#c-606a9712b5ed5e8e) · [缺口 G-12a23ef8c3ecc1f7](../../evidence/gaps-sets-001.md#g-12a23ef8c3ecc1f7) · [参数 P-11cc75916cabcd60](../../evidence/parameters-sets-002.md#p-11cc75916cabcd60) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-064571

```text
(config-if)# ip multicast boundary <cr>
```

Handler ` RVA 0xF75DA30 `；selector ` 0 `；EOL ` RVA 0x34766010 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-75cf1c0dba9bb508](../../evidence/conditions-sets-046.md#c-75cf1c0dba9bb508) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-066792

```text
(config-if)# ip multicast boundary block source <cr>
```

Handler ` RVA 0xF75DA30 `；selector ` 2 `；EOL ` RVA 0x34766A00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-29e2e9eb7813728f](../../evidence/conditions-sets-016.md#c-29e2e9eb7813728f) · [状态效果 S-797d0fb2b06983f9](../../evidence/state_effects-sets-026.md#s-797d0fb2b06983f9)

### path-066795

```text
(config-if)# ip multicast boundary filter-autorp <number:1..99> <cr>
```

Handler ` RVA 0xF75DA30 `；selector ` 1 `；EOL ` RVA 0x347660E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Standard IP access-list number。

[条件 C-fa61fb7c3a5cb641](../../evidence/conditions-sets-097.md#c-fa61fb7c3a5cb641) · [参数 P-39fb08a646354c83](../../evidence/parameters-sets-005.md#p-39fb08a646354c83) · [状态效果 S-b0a869736f29e43e](../../evidence/state_effects-sets-037.md#s-b0a869736f29e43e)

### path-066807

```text
(config-if)# ip multicast boundary filter-autorp <number:1..99> <cr>
```

Handler ` RVA 0xF75DA30 `；selector ` 3 `；EOL ` RVA 0x34766390 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Standard IP access-list number。

[条件 C-3a45b2d1c0b3aee7](../../evidence/conditions-sets-023.md#c-3a45b2d1c0b3aee7) · [参数 P-39fb08a646354c83](../../evidence/parameters-sets-005.md#p-39fb08a646354c83) · [状态效果 S-b0a869736f29e43e](../../evidence/state_effects-sets-037.md#s-b0a869736f29e43e)

### path-065798

```text
(config-if)# ip multicast cca test <cr>
```

Handler ` RVA 0xF75DD30 `；selector ` 4 `；EOL ` RVA 0x34767E10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-89883dc8823b2801](../../evidence/conditions-sets-053.md#c-89883dc8823b2801) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-067376

```text
(config-if)# ip multicast helper-map broadcast <address> <number:2000..2699> <cr>
```

Handler ` RVA 0xF75F050 `；selector ` 0 `；EOL ` RVA 0x34768218 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP address；` unsigned_number ` access-list (expanded range)。

[条件 C-f94ef4712bf98b6d](../../evidence/conditions-sets-096.md#c-f94ef4712bf98b6d) · [参数 P-f50a7dc2ce14b410](../../evidence/parameters-sets-018.md#p-f50a7dc2ce14b410) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-066824

```text
(config-if)# ip multicast limit <number:1..199> <number:0..2147483647> <cr>
```

Handler ` RVA 0xF778B40 `；selector ` 0 `；EOL ` RVA 0x34768830 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Standard or Extended IP access list number；` unsigned_number ` Max Allowed State on this interface。

[条件 C-535f853e7232c756](../../evidence/conditions-sets-033.md#c-535f853e7232c756) · [参数 P-0cdaee7f78682cca](../../evidence/parameters-sets-001.md#p-0cdaee7f78682cca) · [状态效果 S-865da0bd5c5e4fea](../../evidence/state_effects-sets-028.md#s-865da0bd5c5e4fea)

### path-065817

```text
(config-if)# ip multicast rate-limit in <cr>
```

Handler ` RVA 0xF75B4F0 `；selector ` 0 `；EOL ` RVA 0x34767600 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-23061cb42d9f149c](../../evidence/conditions-sets-014.md#c-23061cb42d9f149c) · [状态效果 S-79101a075d8a63b2](../../evidence/state_effects-sets-026.md#s-79101a075d8a63b2)

### path-063527

```text
(config-if)# ip multicast ttl-threshold <number:0..255> <cr>
```

Handler ` RVA 0xF70B630 `；selector ` 0 `；EOL ` RVA 0x34765BB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` TTL threshold。

[条件 C-81db36242f207478](../../evidence/conditions-sets-050.md#c-81db36242f207478) · [参数 P-4870c9fd334e1845](../../evidence/parameters-sets-006.md#p-4870c9fd334e1845) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-063528

```text
(config-if)# ip multicast ttl-threshold <number:0..255> <cr>
```

Handler ` RVA 0xF70B630 `；selector ` 0 `；EOL ` RVA 0x34768C48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` TTL threshold。

[条件 C-8556c2000953f816](../../evidence/conditions-sets-052.md#c-8556c2000953f816) · [参数 P-fdcf532ecf307d82](../../evidence/parameters-sets-019.md#p-fdcf532ecf307d82) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-064417

```text
(config-if)# ip multicast use-functional <cr>
```

Handler ` RVA 0xF761920 `；selector ` 0 `；EOL ` RVA 0x34767AA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-851d1ad22affddce](../../evidence/conditions-sets-051.md#c-851d1ad22affddce) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-064497

```text
(config-if)# ip nat allow-static-host <cr>
```

Handler ` RVA 0xFA2D8D0 `；selector ` 2 `；EOL ` RVA 0x347D71D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ac0f0bcd2323e617](../../evidence/conditions-sets-066.md#c-ac0f0bcd2323e617) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-064454

```text
(config-if)# ip nat enable <cr>
```

Handler ` RVA 0xFA2D8D0 `；selector ` 3 `；EOL ` RVA 0x347D6EF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-73eea20370f72536](../../evidence/conditions-sets-045.md#c-73eea20370f72536) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-064409

```text
(config-if)# ip nat inside <cr>
```

Handler ` RVA 0xFA2D8D0 `；selector ` 0 `；EOL ` RVA 0x347D69A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-73eea20370f72536](../../evidence/conditions-sets-045.md#c-73eea20370f72536) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-064369

```text
(config-if)# ip nat outside <cr>
```

Handler ` RVA 0xFA2D8D0 `；selector ` 1 `；EOL ` RVA 0x347D66F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-73eea20370f72536](../../evidence/conditions-sets-045.md#c-73eea20370f72536) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-064437

```text
(config-if)# ip nat stick <cr>
```

Handler ` RVA 0xFA2D8D0 `；selector ` 4 `；EOL ` RVA 0x347D6C48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-73eea20370f72536](../../evidence/conditions-sets-045.md#c-73eea20370f72536) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-064299

```text
(config-if)# ip nbar collect-dhcpv6-data <cr>
```

Handler ` RVA 0x10F72060 `；selector ` 0 `；EOL ` RVA 0x353717B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a95b07ad20d4f741](../../evidence/conditions-sets-065.md#c-a95b07ad20d4f741) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-064398

```text
(config-if)# ip nbar protocol-discovery <cr>
```

Handler ` RVA 0x10F30AE0 `；selector ` 0 `；EOL ` RVA 0x35371AE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-17ddbd9f5229c56e](../../evidence/conditions-sets-009.md#c-17ddbd9f5229c56e) · [状态效果 S-d5dcfd0eba187b34](../../evidence/state_effects-sets-045.md#s-d5dcfd0eba187b34)

### path-063458

```text
(config-if)# ip network-broadcast <cr>
```

Handler ` RVA 0xCF31710 `；selector ` 0 `；EOL ` RVA 0x33D21648 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a1d840fa0bc3aa08](../../evidence/conditions-sets-062.md#c-a1d840fa0bc3aa08) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-065856

```text
(config-if)# ip next-hop-self eigrp <number:1..65535> <cr>
```

Handler ` RVA 0xF58CAE0 `；selector ` 131 `；EOL ` RVA 0x346DF470 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` AS number。

[条件 C-17ddbd9f5229c56e](../../evidence/conditions-sets-009.md#c-17ddbd9f5229c56e) · [参数 P-2f6632ef28bd20b6](../../evidence/parameters-sets-004.md#p-2f6632ef28bd20b6) · [状态效果 S-4af214c14f210766](../../evidence/state_effects-sets-016.md#s-4af214c14f210766)

### path-067986

```text
(config-if)# ip nhrp attribute group <cr>
```

Handler ` RVA 0xFAB45E0 `；selector ` 35 `；EOL ` RVA 0x347F93B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-befda4b6a257e637](../../evidence/conditions-sets-074.md#c-befda4b6a257e637) · [缺口 G-a0f7dd096d76fbba](../../evidence/gaps-sets-006.md#g-a0f7dd096d76fbba) · [状态效果 S-ff5e3097c414394f](../../evidence/state_effects-sets-054.md#s-ff5e3097c414394f)

### path-068023

```text
(config-if)# ip nhrp attribute set <string> <string> <cr>
```

Handler ` RVA 0xFAB45E0 `；selector ` 24 `；EOL ` RVA 0x347F96F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` &lt;0-32&gt; attribute type；` string ` &lt;0-128&gt; attribute value。

[条件 C-44b58748c3e83df9](../../evidence/conditions-sets-027.md#c-44b58748c3e83df9) · [缺口 G-a0f7dd096d76fbba](../../evidence/gaps-sets-006.md#g-a0f7dd096d76fbba) · [参数 P-18480cfce706db71](../../evidence/parameters-sets-002.md#p-18480cfce706db71) · [状态效果 S-f6661034b31d6f0a](../../evidence/state_effects-sets-052.md#s-f6661034b31d6f0a)

### path-067945

```text
(config-if)# ip nhrp authentication <cr>
```

Handler ` RVA 0xFAB45E0 `；selector ` 6 `；EOL ` RVA 0x347F65A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e6f46d40bf810f0b](../../evidence/conditions-sets-089.md#c-e6f46d40bf810f0b) · [缺口 G-a0f7dd096d76fbba](../../evidence/gaps-sets-006.md#g-a0f7dd096d76fbba) · [状态效果 S-f6661034b31d6f0a](../../evidence/state_effects-sets-052.md#s-f6661034b31d6f0a)

### path-067988

```text
(config-if)# ip nhrp bfd strict-mode <cr>
```

Handler ` RVA 0xFAB45E0 `；selector ` 39 `；EOL ` RVA 0x347FB528 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-44b58748c3e83df9](../../evidence/conditions-sets-027.md#c-44b58748c3e83df9) · [缺口 G-a0f7dd096d76fbba](../../evidence/gaps-sets-006.md#g-a0f7dd096d76fbba) · [状态效果 S-de5e84bd03cf2a9a](../../evidence/state_effects-sets-047.md#s-de5e84bd03cf2a9a)

### path-067957

```text
(config-if)# ip nhrp block-next-hop-override <cr>
```

Handler ` RVA 0xFAB45E0 `；selector ` 48 `；EOL ` RVA 0x347FEB18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-44b58748c3e83df9](../../evidence/conditions-sets-027.md#c-44b58748c3e83df9) · [缺口 G-a0f7dd096d76fbba](../../evidence/gaps-sets-006.md#g-a0f7dd096d76fbba) · [状态效果 S-f6661034b31d6f0a](../../evidence/state_effects-sets-052.md#s-f6661034b31d6f0a)

### path-067990

```text
(config-if)# ip nhrp cache bgp-sync <cr>
```

Handler ` RVA 0xFAB45E0 `；selector ` 15 `；EOL ` RVA 0x347FD608 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f5e6ff9b370baff4](../../evidence/conditions-sets-095.md#c-f5e6ff9b370baff4) · [缺口 G-a0f7dd096d76fbba](../../evidence/gaps-sets-006.md#g-a0f7dd096d76fbba) · [状态效果 S-f6661034b31d6f0a](../../evidence/state_effects-sets-052.md#s-f6661034b31d6f0a)

### path-068016

```text
(config-if)# ip nhrp cache next-hop route-validate <cr>
```

Handler ` RVA 0xFAB45E0 `；selector ` 46 `；EOL ` RVA 0x347FDB98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-44b58748c3e83df9](../../evidence/conditions-sets-027.md#c-44b58748c3e83df9) · [缺口 G-a0f7dd096d76fbba](../../evidence/gaps-sets-006.md#g-a0f7dd096d76fbba) · [状态效果 S-f6661034b31d6f0a](../../evidence/state_effects-sets-052.md#s-f6661034b31d6f0a)

### path-067992

```text
(config-if)# ip nhrp cache non-authoritative <cr>
```

Handler ` RVA 0xFAB45E0 `；selector ` 17 `；EOL ` RVA 0x347FD8B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-44b58748c3e83df9](../../evidence/conditions-sets-027.md#c-44b58748c3e83df9) · [缺口 G-a0f7dd096d76fbba](../../evidence/gaps-sets-006.md#g-a0f7dd096d76fbba) · [状态效果 S-f6661034b31d6f0a](../../evidence/state_effects-sets-052.md#s-f6661034b31d6f0a)

### path-067984

```text
(config-if)# ip nhrp connect <number:1..65535> <cr>
```

Handler ` RVA 0xFAB45E0 `；selector ` 30 `；EOL ` RVA 0x347F8FF0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` NHRP event request id。

[条件 C-44b58748c3e83df9](../../evidence/conditions-sets-027.md#c-44b58748c3e83df9) · [缺口 G-a0f7dd096d76fbba](../../evidence/gaps-sets-006.md#g-a0f7dd096d76fbba) · [参数 P-5efd2d8b40f02058](../../evidence/parameters-sets-008.md#p-5efd2d8b40f02058) · [状态效果 S-f6661034b31d6f0a](../../evidence/state_effects-sets-052.md#s-f6661034b31d6f0a)

### path-067920

```text
(config-if)# ip nhrp holdtime <number:1..65535> <cr>
```

Handler ` RVA 0xFAB45E0 `；selector ` 4 `；EOL ` RVA 0x347F7F18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Number of seconds。

[条件 C-2be3d8da0ee3a1b3](../../evidence/conditions-sets-017.md#c-2be3d8da0ee3a1b3) · [缺口 G-a66b3c650be6281b](../../evidence/gaps-sets-006.md#g-a66b3c650be6281b) · [参数 P-c36980365eb4ab04](../../evidence/parameters-sets-015.md#p-c36980365eb4ab04) · [状态效果 S-f6661034b31d6f0a](../../evidence/state_effects-sets-052.md#s-f6661034b31d6f0a)

### path-067946

```text
(config-if)# ip nhrp interest <cr>
```

Handler ` RVA 0xFAB45E0 `；selector ` 3 `；EOL ` RVA 0x347F8560 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ad210394b8635e53](../../evidence/conditions-sets-067.md#c-ad210394b8635e53) · [缺口 G-a0f7dd096d76fbba](../../evidence/gaps-sets-006.md#g-a0f7dd096d76fbba) · [状态效果 S-f6661034b31d6f0a](../../evidence/state_effects-sets-052.md#s-f6661034b31d6f0a)

### path-068011

```text
(config-if)# ip nhrp map multicast dynamic <cr>
```

Handler ` RVA 0xFAB45E0 `；selector ` 1 `；EOL ` RVA 0x347F6DA8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-44b58748c3e83df9](../../evidence/conditions-sets-027.md#c-44b58748c3e83df9) · [缺口 G-a0f7dd096d76fbba](../../evidence/gaps-sets-006.md#g-a0f7dd096d76fbba) · [状态效果 S-0477fd127130c3e2](../../evidence/state_effects-sets-001.md#s-0477fd127130c3e2)

### path-067952

```text
(config-if)# ip nhrp max-send <cr>
```

Handler ` RVA 0xFAB45E0 `；selector ` 9 `；EOL ` RVA 0x347FB050 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2dab7b1a80046051](../../evidence/conditions-sets-018.md#c-2dab7b1a80046051) · [缺口 G-a0f7dd096d76fbba](../../evidence/gaps-sets-006.md#g-a0f7dd096d76fbba) · [状态效果 S-f6661034b31d6f0a](../../evidence/state_effects-sets-052.md#s-f6661034b31d6f0a)

### path-067989

```text
(config-if)# ip nhrp multicast batch-size <cr>
```

Handler ` RVA 0xFAB45E0 `；selector ` 23 `；EOL ` RVA 0x347FBA98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-44b58748c3e83df9](../../evidence/conditions-sets-027.md#c-44b58748c3e83df9) · [缺口 G-a0f7dd096d76fbba](../../evidence/gaps-sets-006.md#g-a0f7dd096d76fbba) · [状态效果 S-f6661034b31d6f0a](../../evidence/state_effects-sets-052.md#s-f6661034b31d6f0a)

### path-067919

```text
(config-if)# ip nhrp network-id <number:1..4294967295> <cr>
```

Handler ` RVA 0xFAB45E0 `；selector ` 0 `；EOL ` RVA 0x347F7468 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Network identifier。

[条件 C-32b8c2149fb57cc1](../../evidence/conditions-sets-020.md#c-32b8c2149fb57cc1) · [缺口 G-eebc16c09cf58bf4](../../evidence/gaps-sets-008.md#g-eebc16c09cf58bf4) · [参数 P-c27a390c8fd5ccf5](../../evidence/parameters-sets-015.md#p-c27a390c8fd5ccf5) · [状态效果 S-f6661034b31d6f0a](../../evidence/state_effects-sets-052.md#s-f6661034b31d6f0a)

### path-067987

```text
(config-if)# ip nhrp nhs <address> <cr>
```

Handler ` RVA 0xFAB45E0 `；selector ` 2 `；EOL ` RVA 0x347F9D08 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Protocol IP address of NHS。

[条件 C-44b58748c3e83df9](../../evidence/conditions-sets-027.md#c-44b58748c3e83df9) · [缺口 G-a0f7dd096d76fbba](../../evidence/gaps-sets-006.md#g-a0f7dd096d76fbba) · [参数 P-0740f86cfd06dbcf](../../evidence/parameters-sets-001.md#p-0740f86cfd06dbcf) · [状态效果 S-f6661034b31d6f0a](../../evidence/state_effects-sets-052.md#s-f6661034b31d6f0a)

### path-068033

```text
(config-if)# ip nhrp nhs cluster <number:0..10> max-connections <number:0..255> <cr>
```

Handler ` RVA 0xFAB45E0 `；selector ` 21 `；EOL ` RVA 0x347FA170 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` NHS cluster number；` unsigned_number ` Max-connections value。

[条件 C-44b58748c3e83df9](../../evidence/conditions-sets-027.md#c-44b58748c3e83df9) · [缺口 G-a0f7dd096d76fbba](../../evidence/gaps-sets-006.md#g-a0f7dd096d76fbba) · [参数 P-03e1abb5eff04700](../../evidence/parameters-sets-001.md#p-03e1abb5eff04700) · [状态效果 S-f6661034b31d6f0a](../../evidence/state_effects-sets-052.md#s-f6661034b31d6f0a)

### path-068014

```text
(config-if)# ip nhrp nhs fallback <number:0..60> <cr>
```

Handler ` RVA 0xFAB45E0 `；selector ` 22 `；EOL ` RVA 0x347FA448 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` NHS Redundancy Fallback time, 0 -60 seconds。

[条件 C-44b58748c3e83df9](../../evidence/conditions-sets-027.md#c-44b58748c3e83df9) · [缺口 G-a0f7dd096d76fbba](../../evidence/gaps-sets-006.md#g-a0f7dd096d76fbba) · [参数 P-b47da544c1404a05](../../evidence/parameters-sets-014.md#p-b47da544c1404a05) · [状态效果 S-f6661034b31d6f0a](../../evidence/state_effects-sets-052.md#s-f6661034b31d6f0a)

### path-067996

```text
(config-if)# ip nhrp path preference <cr>
```

Handler ` RVA 0xFAB45E0 `；selector ` 36 `；EOL ` RVA 0x347FE830 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9da5d64c866dc5e9](../../evidence/conditions-sets-061.md#c-9da5d64c866dc5e9) · [缺口 G-a0f7dd096d76fbba](../../evidence/gaps-sets-006.md#g-a0f7dd096d76fbba) · [状态效果 S-f6661034b31d6f0a](../../evidence/state_effects-sets-052.md#s-f6661034b31d6f0a)

### path-067950

```text
(config-if)# ip nhrp process-delay <cr>
```

Handler ` RVA 0xFAB45E0 `；selector ` 40 `；EOL ` RVA 0x347FA9A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-44b58748c3e83df9](../../evidence/conditions-sets-027.md#c-44b58748c3e83df9) · [缺口 G-a0f7dd096d76fbba](../../evidence/gaps-sets-006.md#g-a0f7dd096d76fbba) · [状态效果 S-f6661034b31d6f0a](../../evidence/state_effects-sets-052.md#s-f6661034b31d6f0a)

### path-067948

```text
(config-if)# ip nhrp record <cr>
```

Handler ` RVA 0xFAB45E0 `；selector ` 5 `；EOL ` RVA 0x347FA6F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-44b58748c3e83df9](../../evidence/conditions-sets-027.md#c-44b58748c3e83df9) · [缺口 G-a0f7dd096d76fbba](../../evidence/gaps-sets-006.md#g-a0f7dd096d76fbba) · [状态效果 S-f6661034b31d6f0a](../../evidence/state_effects-sets-052.md#s-f6661034b31d6f0a)

### path-067958

```text
(config-if)# ip nhrp redirect <cr>
```

Handler ` RVA 0xFAB45E0 `；selector ` 19 `；EOL ` RVA 0x347FE288 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7dd338e96ef40175](../../evidence/conditions-sets-049.md#c-7dd338e96ef40175) · [缺口 G-a0f7dd096d76fbba](../../evidence/gaps-sets-006.md#g-a0f7dd096d76fbba) · [状态效果 S-f6661034b31d6f0a](../../evidence/state_effects-sets-052.md#s-f6661034b31d6f0a)

### path-067953

```text
(config-if)# ip nhrp registration delay <number:0..10> <cr>
```

Handler ` RVA 0xFAB45E0 `；selector ` 13 `；EOL ` RVA 0x347FC320 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Seconds to delay。

[条件 C-7b1b596bac8888a9](../../evidence/conditions-sets-048.md#c-7b1b596bac8888a9) · [缺口 G-d2c5d9bac968c256](../../evidence/gaps-sets-007.md#g-d2c5d9bac968c256) · [参数 P-d25121c9d9c4f4df](../../evidence/parameters-sets-016.md#p-d25121c9d9c4f4df) · [状态效果 S-f6661034b31d6f0a](../../evidence/state_effects-sets-052.md#s-f6661034b31d6f0a)

### path-067993

```text
(config-if)# ip nhrp registration differential <cr>
```

Handler ` RVA 0xFAB45E0 `；selector ` 42 `；EOL ` RVA 0x347FCCB0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-44b58748c3e83df9](../../evidence/conditions-sets-027.md#c-44b58748c3e83df9) · [缺口 G-a0f7dd096d76fbba](../../evidence/gaps-sets-006.md#g-a0f7dd096d76fbba) · [状态效果 S-f6661034b31d6f0a](../../evidence/state_effects-sets-052.md#s-f6661034b31d6f0a)

### path-067991

```text
(config-if)# ip nhrp registration no-unique <cr>
```

Handler ` RVA 0xFAB45E0 `；selector ` 12 `；EOL ` RVA 0x347FC690 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-44b58748c3e83df9](../../evidence/conditions-sets-027.md#c-44b58748c3e83df9) · [缺口 G-a0f7dd096d76fbba](../../evidence/gaps-sets-006.md#g-a0f7dd096d76fbba) · [状态效果 S-f6661034b31d6f0a](../../evidence/state_effects-sets-052.md#s-f6661034b31d6f0a)

### path-067994

```text
(config-if)# ip nhrp registration req-def-map <cr>
```

Handler ` RVA 0xFAB45E0 `；selector ` 38 `；EOL ` RVA 0x347FC9A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-44b58748c3e83df9](../../evidence/conditions-sets-027.md#c-44b58748c3e83df9) · [缺口 G-a0f7dd096d76fbba](../../evidence/gaps-sets-006.md#g-a0f7dd096d76fbba) · [状态效果 S-f6661034b31d6f0a](../../evidence/state_effects-sets-052.md#s-f6661034b31d6f0a)

### path-067955

```text
(config-if)# ip nhrp registration timeout <number:1..65535> <cr>
```

Handler ` RVA 0xFAB45E0 `；selector ` 14 `；EOL ` RVA 0x347FCC70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Number of seconds。

[条件 C-f09c4bf9dc3e1c7b](../../evidence/conditions-sets-093.md#c-f09c4bf9dc3e1c7b) · [缺口 G-3d94926afade3a03](../../evidence/gaps-sets-003.md#g-3d94926afade3a03) · [参数 P-58e9af937360215e](../../evidence/parameters-sets-007.md#p-58e9af937360215e) · [状态效果 S-f6661034b31d6f0a](../../evidence/state_effects-sets-052.md#s-f6661034b31d6f0a)

### path-067985

```text
(config-if)# ip nhrp reject <number:1..65535> <cr>
```

Handler ` RVA 0xFAB45E0 `；selector ` 31 `；EOL ` RVA 0x347F8CC8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` reqid value。

[条件 C-44b58748c3e83df9](../../evidence/conditions-sets-027.md#c-44b58748c3e83df9) · [缺口 G-a0f7dd096d76fbba](../../evidence/gaps-sets-006.md#g-a0f7dd096d76fbba) · [参数 P-0a5f80e4a64c0ed9](../../evidence/parameters-sets-001.md#p-0a5f80e4a64c0ed9) · [状态效果 S-f6661034b31d6f0a](../../evidence/state_effects-sets-052.md#s-f6661034b31d6f0a)

### path-068026

```text
(config-if)# ip nhrp resolution refresh base <number:1..65535> <cr>
```

Handler ` RVA 0xFAB45E0 `；selector ` 41 `；EOL ` RVA 0x347FD300 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Route every 'n'th request through this topology。

[条件 C-44b58748c3e83df9](../../evidence/conditions-sets-027.md#c-44b58748c3e83df9) · [缺口 G-a0f7dd096d76fbba](../../evidence/gaps-sets-006.md#g-a0f7dd096d76fbba) · [参数 P-583649b05a83bcd4](../../evidence/parameters-sets-007.md#p-583649b05a83bcd4) · [状态效果 S-f6661034b31d6f0a](../../evidence/state_effects-sets-052.md#s-f6661034b31d6f0a)

### path-067983

```text
(config-if)# ip nhrp responder default-originate <cr>
```

Handler ` RVA 0xFAB45E0 `；selector ` 7 `；EOL ` RVA 0x347F69B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9f05393b1f29968e](../../evidence/conditions-sets-061.md#c-9f05393b1f29968e) · [缺口 G-a0f7dd096d76fbba](../../evidence/gaps-sets-006.md#g-a0f7dd096d76fbba) · [状态效果 S-0669b3184f357f29](../../evidence/state_effects-sets-002.md#s-0669b3184f357f29)

### path-067982

```text
(config-if)# ip nhrp role hub <cr>
```

Handler ` RVA 0xFAB45E0 `；selector ` 49 `；EOL ` RVA 0x347F7F58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-44b58748c3e83df9](../../evidence/conditions-sets-027.md#c-44b58748c3e83df9) · [缺口 G-a0f7dd096d76fbba](../../evidence/gaps-sets-006.md#g-a0f7dd096d76fbba) · [状态效果 S-abf09f4815c07168](../../evidence/state_effects-sets-036.md#s-abf09f4815c07168)

### path-067954

```text
(config-if)# ip nhrp send-routed <cr>
```

Handler ` RVA 0xFAB45E0 `；selector ` 16 `；EOL ` RVA 0x347FC0A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-44b58748c3e83df9](../../evidence/conditions-sets-027.md#c-44b58748c3e83df9) · [缺口 G-a0f7dd096d76fbba](../../evidence/gaps-sets-006.md#g-a0f7dd096d76fbba) · [状态效果 S-f6661034b31d6f0a](../../evidence/state_effects-sets-052.md#s-f6661034b31d6f0a)

### path-067951

```text
(config-if)# ip nhrp server-only <cr>
```

Handler ` RVA 0xFAB45E0 `；selector ` 10 `；EOL ` RVA 0x347FACE8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-44b58748c3e83df9](../../evidence/conditions-sets-027.md#c-44b58748c3e83df9) · [缺口 G-a0f7dd096d76fbba](../../evidence/gaps-sets-006.md#g-a0f7dd096d76fbba) · [状态效果 S-f6661034b31d6f0a](../../evidence/state_effects-sets-052.md#s-f6661034b31d6f0a)

### path-067956

```text
(config-if)# ip nhrp shortcut <cr>
```

Handler ` RVA 0xFAB45E0 `；selector ` 18 `；EOL ` RVA 0x347FDF10 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-44b58748c3e83df9](../../evidence/conditions-sets-027.md#c-44b58748c3e83df9) · [缺口 G-a0f7dd096d76fbba](../../evidence/gaps-sets-006.md#g-a0f7dd096d76fbba) · [状态效果 S-f6661034b31d6f0a](../../evidence/state_effects-sets-052.md#s-f6661034b31d6f0a)

### path-068012

```text
(config-if)# ip nhrp summary-map <address> <address> <cr>
```

Handler ` RVA 0xFAB45E0 `；selector ` 37 `；EOL ` RVA 0x347F7740 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` IP address；` address ` mask destination。

[条件 C-44b58748c3e83df9](../../evidence/conditions-sets-027.md#c-44b58748c3e83df9) · [缺口 G-a0f7dd096d76fbba](../../evidence/gaps-sets-006.md#g-a0f7dd096d76fbba) · [参数 P-7bc95e112f6b94f8](../../evidence/parameters-sets-010.md#p-7bc95e112f6b94f8) · [状态效果 S-f6661034b31d6f0a](../../evidence/state_effects-sets-052.md#s-f6661034b31d6f0a)

### path-067947

```text
(config-if)# ip nhrp trigger-svc <cr>
```

Handler ` RVA 0xFAB45E0 `；selector ` 11 `；EOL ` RVA 0x347F8910 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-eaea44a080dfe7ba](../../evidence/conditions-sets-091.md#c-eaea44a080dfe7ba) · [缺口 G-a0f7dd096d76fbba](../../evidence/gaps-sets-006.md#g-a0f7dd096d76fbba) · [状态效果 S-f6661034b31d6f0a](../../evidence/state_effects-sets-052.md#s-f6661034b31d6f0a)

### path-067921

```text
(config-if)# ip nhrp use <number:1..65535> <cr>
```

Handler ` RVA 0xFAB45E0 `；selector ` 8 `；EOL ` RVA 0x347FB9B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Number of packets to cause NHRP request。

[条件 C-2c220315ccbce781](../../evidence/conditions-sets-017.md#c-2c220315ccbce781) · [缺口 G-a3ee78313b864596](../../evidence/gaps-sets-006.md#g-a3ee78313b864596) · [参数 P-95f0653c4c173b27](../../evidence/parameters-sets-012.md#p-95f0653c4c173b27) · [状态效果 S-f6661034b31d6f0a](../../evidence/state_effects-sets-052.md#s-f6661034b31d6f0a)

### path-066862

```text
(config-if)# ip ospf <number:1..65535> area <address> <cr>
```

Handler ` RVA 0xFCEEEF0 `；selector ` 18 `；EOL ` RVA 0x348810B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Process ID；` address ` OSPF area ID in IP address format。

[条件 C-6c0f1c2b4fa5aaa4](../../evidence/conditions-sets-042.md#c-6c0f1c2b4fa5aaa4) · [参数 P-aeaa49bf7dc714a9](../../evidence/parameters-sets-013.md#p-aeaa49bf7dc714a9) · [状态效果 S-6f19554943167e02](../../evidence/state_effects-sets-024.md#s-6f19554943167e02)

### path-066778

```text
(config-if)# ip ospf adjacency stagger disable <cr>
```

Handler ` RVA 0xFCEEEF0 `；selector ` 23 `；EOL ` RVA 0x3487F500 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-58028ca8fbcd983c](../../evidence/conditions-sets-034.md#c-58028ca8fbcd983c) · [状态效果 S-55911a24e4e75b6e](../../evidence/state_effects-sets-019.md#s-55911a24e4e75b6e)

### path-064212

```text
(config-if)# ip ospf authentication <cr>
```

Handler ` RVA 0xFCEEEF0 `；selector ` 11 `；EOL ` RVA 0x3487B190 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7590e1748c605a5d](../../evidence/conditions-sets-046.md#c-7590e1748c605a5d) · [状态效果 S-4e792723953d7be7](../../evidence/state_effects-sets-017.md#s-4e792723953d7be7)

### path-065553

```text
(config-if)# ip ospf authentication-key <string> <cr>
```

Handler ` RVA 0xFCEEEF0 `；selector ` 7 `；EOL ` RVA 0x3487B638 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Authentication key-string to authenticate OSPF peer (maximum 8 characters for clear text, 33 characters for AES encrypted and 18 characters for proprietary)。

[条件 C-aecaaf7879b3b2db](../../evidence/conditions-sets-068.md#c-aecaaf7879b3b2db) · [参数 P-8b9aa983397360d9](../../evidence/parameters-sets-011.md#p-8b9aa983397360d9)

### path-064430

```text
(config-if)# ip ospf bfd <cr>
```

Handler ` RVA 0xFCEEEF0 `；selector ` 17 `；EOL ` RVA 0x3487F080 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0bcf875eb6274299](../../evidence/conditions-sets-005.md#c-0bcf875eb6274299)

### path-063625

```text
(config-if)# ip ospf cost <number:1..65535> <cr>
```

Handler ` RVA 0xFCEEEF0 `；selector ` 0 `；EOL ` RVA 0x34881830 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Cost。

[条件 C-411aec4c4a1050ca](../../evidence/conditions-sets-025.md#c-411aec4c4a1050ca) · [参数 P-d7b2e765e90a1b82](../../evidence/parameters-sets-016.md#p-d7b2e765e90a1b82)

### path-066753

```text
(config-if)# ip ospf database-filter all out <cr>
```

Handler ` RVA 0xFCEEEF0 `；selector ` 10 `；EOL ` RVA 0x3487E820 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-185ff1eee992775e](../../evidence/conditions-sets-009.md#c-185ff1eee992775e)

### path-065572

```text
(config-if)# ip ospf dead-interval <number:1..65535> <cr>
```

Handler ` RVA 0xFCEEEF0 `；selector ` 5 `；EOL ` RVA 0x3487CB58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Seconds。

[条件 C-14689e05ad13a638](../../evidence/conditions-sets-008.md#c-14689e05ad13a638) · [参数 P-329d29b62b1d79eb](../../evidence/parameters-sets-004.md#p-329d29b62b1d79eb)

### path-067393

```text
(config-if)# ip ospf delay normalize interval <number:1..16777215> <cr>
```

Handler ` RVA 0xFCEEEF0 `；selector ` 35 `；EOL ` RVA 0x348814B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Micro seconds。

[条件 C-59bf725098608e5a](../../evidence/conditions-sets-035.md#c-59bf725098608e5a) · [参数 P-a9a3fd620d6622d7](../../evidence/parameters-sets-013.md#p-a9a3fd620d6622d7)

### path-064292

```text
(config-if)# ip ospf demand-circuit <cr>
```

Handler ` RVA 0xFCEEEF0 `；selector ` 9 `；EOL ` RVA 0x3487E0D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7985f4cd08af0529](../../evidence/conditions-sets-047.md#c-7985f4cd08af0529)

### path-064279

```text
(config-if)# ip ospf flood-reduction <cr>
```

Handler ` RVA 0xFCEEEF0 `；selector ` 13 `；EOL ` RVA 0x3487DD98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7f76f6c434e4b9ab](../../evidence/conditions-sets-049.md#c-7f76f6c434e4b9ab)

### path-063486

```text
(config-if)# ip ospf hello-interval <number:1..65535> <cr>
```

Handler ` RVA 0xFCEEEF0 `；selector ` 4 `；EOL ` RVA 0x3487CAB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Seconds。

[条件 C-caa7195b8a969ca4](../../evidence/conditions-sets-078.md#c-caa7195b8a969ca4) · [参数 P-12260b0e11cd61ed](../../evidence/parameters-sets-002.md#p-12260b0e11cd61ed)

### path-063475

```text
(config-if)# ip ospf interface-retry <number:1..65535> <cr>
```

Handler ` RVA 0xFCEEEF0 `；selector ` 12 `；EOL ` RVA 0x3487C550 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Retry。

[条件 C-5d356dfda20beeda](../../evidence/conditions-sets-036.md#c-5d356dfda20beeda) · [参数 P-e0620dc599c04501](../../evidence/parameters-sets-017.md#p-e0620dc599c04501)

### path-064280

```text
(config-if)# ip ospf lls <cr>
```

Handler ` RVA 0xFCEEEF0 `；selector ` 16 `；EOL ` RVA 0x3487DA18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ebff5c4de9b41fe6](../../evidence/conditions-sets-091.md#c-ebff5c4de9b41fe6)

### path-067322

```text
(config-if)# ip ospf message-digest-key <number:1..255> md5 <string> <cr>
```

Handler ` RVA 0xFCEEEF0 `；selector ` 8 `；EOL ` RVA 0x3487BA68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Key ID；` string ` Authentication key-string used to compute MD5 hash (maximum 16 characters for clear text, 45 characters for AES encrypted and 34 characters for proprietary)。

[条件 C-f654154b13291a5b](../../evidence/conditions-sets-095.md#c-f654154b13291a5b) · [参数 P-609144fc4215c65e](../../evidence/parameters-sets-008.md#p-609144fc4215c65e)

### path-064291

```text
(config-if)# ip ospf mtu-ignore <cr>
```

Handler ` RVA 0xFCEEEF0 `；selector ` 14 `；EOL ` RVA 0x3487E4F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f7419777108156a7](../../evidence/conditions-sets-095.md#c-f7419777108156a7)

### path-065868

```text
(config-if)# ip ospf multi-area <address> <cr>
```

Handler ` RVA 0xFCEEEF0 `；selector ` 28 `；EOL ` RVA 0x34880BF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` OSPF multi-area ID in IP address format。

[条件 C-6b82b5d323976361](../../evidence/conditions-sets-042.md#c-6b82b5d323976361) · [参数 P-e515fe0da2db2c6f](../../evidence/parameters-sets-017.md#p-e515fe0da2db2c6f)

### path-065791

```text
(config-if)# ip ospf multi-area <address> cost <number:1..65535> <cr>
```

Handler ` RVA 0xFCEEEF0 `；selector ` 29 `；EOL ` RVA 0x34880428 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` OSPF multi-area ID in IP address format；` unsigned_number ` Cost。

[条件 C-b06e9b721f8f24ce](../../evidence/conditions-sets-068.md#c-b06e9b721f8f24ce) · [参数 P-d241e1b654dee0e8](../../evidence/parameters-sets-016.md#p-d241e1b654dee0e8)

### path-067692

```text
(config-if)# ip ospf multi-area <address> delay normalize interval <number:1..16777215> <cr>
```

Handler ` RVA 0xFCEEEF0 `；selector ` 36 `；EOL ` RVA 0x34880838 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` OSPF multi-area ID in IP address format；` unsigned_number ` Micro seconds。

[条件 C-b710d5d8dca126ff](../../evidence/conditions-sets-071.md#c-b710d5d8dca126ff) · [参数 P-ee19860e03f79703](../../evidence/parameters-sets-018.md#p-ee19860e03f79703)

### path-065552

```text
(config-if)# ip ospf network broadcast <cr>
```

Handler ` RVA 0xFCEEEF0 `；selector ` 6 `；EOL ` RVA 0x3487BEA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fcaf478c6d5782d7](../../evidence/conditions-sets-097.md#c-fcaf478c6d5782d7) · [状态效果 S-f841f50cd69a29bf](../../evidence/state_effects-sets-053.md#s-f841f50cd69a29bf)

### path-063464

```text
(config-if)# ip ospf packet-size <number:576..10000> <cr>
```

Handler ` RVA 0xFCEEEF0 `；selector ` 37 `；EOL ` RVA 0x3487BE00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` OSPF Packet Size。

[条件 C-723e625a7fa96f17](../../evidence/conditions-sets-044.md#c-723e625a7fa96f17) · [参数 P-0f724e7092ef44f0](../../evidence/parameters-sets-002.md#p-0f724e7092ef44f0)

### path-064364

```text
(config-if)# ip ospf prefix-suppression <cr>
```

Handler ` RVA 0xFCEEEF0 `；selector ` 22 `；EOL ` RVA 0x3487ECD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fd7064caf126ac73](../../evidence/conditions-sets-098.md#c-fd7064caf126ac73)

### path-063491

```text
(config-if)# ip ospf priority <number:0..255> <cr>
```

Handler ` RVA 0xFCEEEF0 `；selector ` 3 `；EOL ` RVA 0x3487CED0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Priority。

[条件 C-6a86b842b6af35f9](../../evidence/conditions-sets-041.md#c-6a86b842b6af35f9) · [参数 P-09a097f0cf1dba4b](../../evidence/parameters-sets-001.md#p-09a097f0cf1dba4b)

### path-063470

```text
(config-if)# ip ospf resync-timeout <number:1..65535> <cr>
```

Handler ` RVA 0xFCEEEF0 `；selector ` 15 `；EOL ` RVA 0x3487C2B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Seconds。

[条件 C-ff4c005cfa0ffb84](../../evidence/conditions-sets-098.md#c-ff4c005cfa0ffb84) · [参数 P-c0305a6d357292d7](../../evidence/parameters-sets-015.md#p-c0305a6d357292d7)

### path-063495

```text
(config-if)# ip ospf retransmit-interval <number:1..65535> <cr>
```

Handler ` RVA 0xFCEEEF0 `；selector ` 1 `；EOL ` RVA 0x3487D170 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Seconds。

[条件 C-08ae9b2b2d4505da](../../evidence/conditions-sets-004.md#c-08ae9b2b2d4505da) · [参数 P-54f462665822f5e4](../../evidence/parameters-sets-007.md#p-54f462665822f5e4)

### path-064429

```text
(config-if)# ip ospf shutdown <cr>
```

Handler ` RVA 0xFCEEEF0 `；selector ` 21 `；EOL ` RVA 0x3487FC88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5537ad8c392fef1e](../../evidence/conditions-sets-033.md#c-5537ad8c392fef1e)

### path-063499

```text
(config-if)# ip ospf transmit-delay <number:1..65535> <cr>
```

Handler ` RVA 0xFCEEEF0 `；selector ` 2 `；EOL ` RVA 0x3487D410 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Seconds。

[条件 C-b37b7a43c088ade7](../../evidence/conditions-sets-069.md#c-b37b7a43c088ade7) · [参数 P-d6fbba744cf4660c](../../evidence/parameters-sets-016.md#p-d6fbba744cf4660c)

### path-064447

```text
(config-if)# ip ospf ttl-security <cr>
```

Handler ` RVA 0xFCEEEF0 `；selector ` 20 `；EOL ` RVA 0x3487F878 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3be5b8b2a50e5310](../../evidence/conditions-sets-023.md#c-3be5b8b2a50e5310)

### path-066810

```text
(config-if)# ip ospf vnet area <address> <cr>
```

Handler ` RVA 0xFCEEEF0 `；selector ` 27 `；EOL ` RVA 0x34880070 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` OSPF area ID in IP address format。

[条件 C-f60cca224d6618aa](../../evidence/conditions-sets-095.md#c-f60cca224d6618aa) · [参数 P-415634c690f6ef90](../../evidence/parameters-sets-006.md#p-415634c690f6ef90)

### path-064420

```text
(config-if)# ip pim bfd <cr>
```

Handler ` RVA 0xC4A3100 `；selector ` 0 `；EOL ` RVA 0x33A9BCC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b18c7bb24523239a](../../evidence/conditions-sets-069.md#c-b18c7bb24523239a) · [状态效果 S-05d50f7559711d8e](../../evidence/state_effects-sets-002.md#s-05d50f7559711d8e)

### path-065778

```text
(config-if)# ip pim bidir-neighbor-filter <number:1..99> <cr>
```

Handler ` RVA 0xF807C30 `；selector ` 0 `；EOL ` RVA 0x34763530 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Access list number。

[条件 C-a068c194215aa650](../../evidence/conditions-sets-062.md#c-a068c194215aa650) · [参数 P-c5dfd83ab338560e](../../evidence/parameters-sets-015.md#p-c5dfd83ab338560e) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-064529

```text
(config-if)# ip pim bsr-border <cr>
```

Handler ` RVA 0xF807F50 `；selector ` 1 `；EOL ` RVA 0x34765050 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-55c3629240168205](../../evidence/conditions-sets-034.md#c-55c3629240168205) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-065779

```text
(config-if)# ip pim dr-priority <number:0..4294967294> <cr>
```

Handler ` RVA 0xF809580 `；selector ` 3 `；EOL ` RVA 0x34763918 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` DR priority, preference given to larger value。

[条件 C-4b4a5f2ecb82ab1d](../../evidence/conditions-sets-030.md#c-4b4a5f2ecb82ab1d) · [参数 P-4d69f7547dab402c](../../evidence/parameters-sets-006.md#p-4d69f7547dab402c) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-064556

```text
(config-if)# ip pim drlb <cr>
```

Handler ` RVA 0xF8091F0 `；selector ` 13 `；EOL ` RVA 0x34763CA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f9da3c4fd813cf8a](../../evidence/conditions-sets-097.md#c-f9da3c4fd813cf8a) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-065691

```text
(config-if)# ip pim join-prune-interval <number:10..600> <cr>
```

Handler ` RVA 0xF8097D0 `；selector ` 11 `；EOL ` RVA 0x347620B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Join-Prune interval in seconds。

[条件 C-ed8e7a7c6c7c2543](../../evidence/conditions-sets-092.md#c-ed8e7a7c6c7c2543) · [参数 P-e2c3a4bb98f98676](../../evidence/parameters-sets-017.md#p-e2c3a4bb98f98676) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-067363

```text
(config-if)# ip pim lisp core-group-range <address> <number:1..1000> <cr>
```

Handler ` RVA 0xF80CB40 `；selector ` 15 `；EOL ` RVA 0x347628F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Start group address of the range；` unsigned_number ` Size of the group range。

[条件 C-a232e05b322ddaaa](../../evidence/conditions-sets-063.md#c-a232e05b322ddaaa) · [参数 P-8e07165a90944a19](../../evidence/parameters-sets-011.md#p-8e07165a90944a19) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-067370

```text
(config-if)# ip pim lisp transit-core-group-range <address> <number:1..1000> <cr>
```

Handler ` RVA 0xF80CD90 `；selector ` 17 `；EOL ` RVA 0x34762CA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Start group address of the range；` unsigned_number ` Size of the group range。

[条件 C-71f035fb6dc14a4b](../../evidence/conditions-sets-044.md#c-71f035fb6dc14a4b) · [参数 P-f9448319cf1084b2](../../evidence/parameters-sets-019.md#p-f9448319cf1084b2) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-066797

```text
(config-if)# ip pim lisp transport unicast <cr>
```

Handler ` RVA 0xF80C840 `；selector ` 14 `；EOL ` RVA 0x34762480 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1ece4b6c2c2cd5c7](../../evidence/conditions-sets-012.md#c-1ece4b6c2c2cd5c7) · [状态效果 S-15c30ca4d91bf888](../../evidence/state_effects-sets-005.md#s-15c30ca4d91bf888)

### path-064498

```text
(config-if)# ip pim nbma-mode <cr>
```

Handler ` RVA 0xF809A30 `；selector ` 4 `；EOL ` RVA 0x34764DA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-55c3629240168205](../../evidence/conditions-sets-034.md#c-55c3629240168205) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-065740

```text
(config-if)# ip pim neighbor-filter <number:1..99> <cr>
```

Handler ` RVA 0xF807C30 `；selector ` 5 `；EOL ` RVA 0x34763108 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Access list number。

[条件 C-fe990a4526e9f994](../../evidence/conditions-sets-098.md#c-fe990a4526e9f994) · [参数 P-688fd12e14f4e835](../../evidence/parameters-sets-008.md#p-688fd12e14f4e835) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-064458

```text
(config-if)# ip pim non-dr-join <cr>
```

Handler ` RVA 0xF809C00 `；selector ` 12 `；EOL ` RVA 0x347646C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-55c3629240168205](../../evidence/conditions-sets-034.md#c-55c3629240168205) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-064351

```text
(config-if)# ip pim passive <cr>
```

Handler ` RVA 0xF808120 `；selector ` 2 `；EOL ` RVA 0x34761758 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2642452a0714ed91](../../evidence/conditions-sets-015.md#c-2642452a0714ed91) · [状态效果 S-12ffb31aabc42a51](../../evidence/state_effects-sets-004.md#s-12ffb31aabc42a51)

### path-065922

```text
(config-if)# ip pim pfp-sa border <cr>
```

Handler ` RVA 0xF80CFE0 `；selector ` 16 `；EOL ` RVA 0x347653E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e952bc342fa3ed8](../../evidence/conditions-sets-006.md#c-0e952bc342fa3ed8) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-065907

```text
(config-if)# ip pim query-interval <number:1..65535> <cr>
```

Handler ` RVA 0xF809DD0 `；selector ` 6 `；EOL ` RVA 0x34764A30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Query interval in seconds or milliseconds。

[条件 C-ceea71cda01e940e](../../evidence/conditions-sets-080.md#c-ceea71cda01e940e) · [参数 P-4089cccea2a77410](../../evidence/parameters-sets-005.md#p-4089cccea2a77410) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-067400

```text
(config-if)# ip pim redundancy <string> dr-priority <number:0..4294967294> <cr>
```

Handler ` RVA 0xF80A320 `；selector ` 9 `；EOL ` RVA 0x347642F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Standby group name；` unsigned_number ` Redundancy DR priority. Preference given to larger value。

[条件 C-5c15959a70ce26c9](../../evidence/conditions-sets-036.md#c-5c15959a70ce26c9) · [参数 P-e7e7db4f1d0d191f](../../evidence/parameters-sets-017.md#p-e7e7db4f1d0d191f) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-067847

```text
(config-if)# ip pim sparse-mode encap-helper <interface> <cr>
```

Handler ` RVA 0xF808120 `；selector ` 2 `；EOL ` RVA 0x34761758 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4e6014ac97935650](../../evidence/conditions-sets-031.md#c-4e6014ac97935650) · [缺口 G-33709ecf57e9f974](../../evidence/gaps-sets-002.md#g-33709ecf57e9f974) · [参数 P-4600cece0fef6995](../../evidence/parameters-sets-006.md#p-4600cece0fef6995) · [状态效果 S-1bb100ac99ff1ae8](../../evidence/state_effects-sets-006.md#s-1bb100ac99ff1ae8)

### path-065978

```text
(config-if)# ip pim state-refresh origination-interval <cr>
```

Handler ` RVA 0xF80A120 `；selector ` 7 `；EOL ` RVA 0x34765750 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bf484e38a845956a](../../evidence/conditions-sets-074.md#c-bf484e38a845956a) · [状态效果 S-7842a029143306db](../../evidence/state_effects-sets-026.md#s-7842a029143306db)

### path-065545

```text
(config-if)# ip policy route-map <string> <cr>
```

Handler ` RVA 0xFAD7E60 `；selector ` 0 `；EOL ` RVA 0x34802570 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Route map name。

[条件 C-a1d99df71f5eda10](../../evidence/conditions-sets-062.md#c-a1d99df71f5eda10) · [参数 P-d51361524c0d9a4b](../../evidence/parameters-sets-016.md#p-d51361524c0d9a4b)

### path-064267

```text
(config-if)# ip portbundle outside <cr>
```

Handler ` RVA 0x11C30260 `；selector ` 5 `；EOL ` RVA 0x356A5798 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-17ddbd9f5229c56e](../../evidence/conditions-sets-009.md#c-17ddbd9f5229c56e) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-064206

```text
(config-if)# ip probe proxy <cr>
```

Handler ` RVA 0xCF2C520 `；selector ` 8 `；EOL ` RVA 0x33D221B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a1d840fa0bc3aa08](../../evidence/conditions-sets-062.md#c-a1d840fa0bc3aa08) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-063461

```text
(config-if)# ip proxy-arp <cr>
```

Handler ` RVA 0xCF32E60 `；selector ` 1 `；EOL ` RVA 0x33D21C00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a1d840fa0bc3aa08](../../evidence/conditions-sets-062.md#c-a1d840fa0bc3aa08) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-064142

```text
(config-if)# ip rarp-server <address> <cr>
```

Handler ` RVA 0xCF2C650 `；selector ` 0 `；EOL ` RVA 0x33D20280 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP server address。

[条件 C-1cd40f9b6d1b7ea1](../../evidence/conditions-sets-011.md#c-1cd40f9b6d1b7ea1) · [参数 P-e4b173ae23c7eb4a](../../evidence/parameters-sets-017.md#p-e4b173ae23c7eb4a) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-063680

```text
(config-if)# ip reassembly <cr>
```

Handler ` RVA 0xC78BC80 `；selector ` 0 `；EOL ` RVA 0x33AEB138 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-191bb1c78d6dddb3](../../evidence/conditions-sets-010.md#c-191bb1c78d6dddb3) · [状态效果 S-95914aa70b985b7a](../../evidence/state_effects-sets-032.md#s-95914aa70b985b7a)

### path-068024

```text
(config-if)# ip reassembly percentage <number:1..100> dscp <?common_dscp_value_action@55558903efd0> <cr>
```

Handler ` RVA 0xC78BC80 `；selector ` 0 `；EOL ` RVA 0x33AEB138 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Reserved Reassembly capacity percentage。

[条件 C-e85e09c524c4546b](../../evidence/conditions-sets-090.md#c-e85e09c524c4546b) · [缺口 G-cb1ec7f68c12d18f](../../evidence/gaps-sets-007.md#g-cb1ec7f68c12d18f) · [参数 P-627ed9c00a9f09b7](../../evidence/parameters-sets-008.md#p-627ed9c00a9f09b7) · [状态效果 S-676bfe67cc17cd4d](../../evidence/state_effects-sets-022.md#s-676bfe67cc17cd4d)

### path-068025

```text
(config-if)# ip reassembly percentage <number:1..100> dscp <?common_dscp_value_action@55558903efd0> <cr>
```

Handler ` RVA 0xC78BC80 `；selector ` 0 `；EOL ` RVA 0x33AEAC40 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Reserved Reassembly capacity percentage。

[条件 C-716c4bf7ee9c78a0](../../evidence/conditions-sets-044.md#c-716c4bf7ee9c78a0) · [缺口 G-cb1ec7f68c12d18f](../../evidence/gaps-sets-007.md#g-cb1ec7f68c12d18f) · [参数 P-627ed9c00a9f09b7](../../evidence/parameters-sets-008.md#p-627ed9c00a9f09b7) · [状态效果 S-676bfe67cc17cd4d](../../evidence/state_effects-sets-022.md#s-676bfe67cc17cd4d)

### path-063444

```text
(config-if)# ip redirects <cr>
```

Handler ` RVA 0xCF33730 `；selector ` 0 `；EOL ` RVA 0x33D20CF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a1d840fa0bc3aa08](../../evidence/conditions-sets-062.md#c-a1d840fa0bc3aa08) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-063460

```text
(config-if)# ip rgmp <cr>
```

Handler ` RVA 0xF87C8D0 `；selector ` 0 `；EOL ` RVA 0x34734540 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8905dbb66d92b58e](../../evidence/conditions-sets-053.md#c-8905dbb66d92b58e)

### path-063618

```text
(config-if)# ip rip advertise <number:0..4294966> <cr>
```

Handler ` RVA 0xFB54010 `；selector ` 7 `；EOL ` RVA 0x348237D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` interval in seconds。

[条件 C-4c66f7744e37a785](../../evidence/conditions-sets-030.md#c-4c66f7744e37a785) · [参数 P-f800be5d3900a98f](../../evidence/parameters-sets-018.md#p-f800be5d3900a98f) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-066839

```text
(config-if)# ip rip advertise-default <number:1..15> <number:0..65535> <cr>
```

Handler ` RVA 0xFB54010 `；selector ` 9 `；EOL ` RVA 0x34823248 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Metric for default-route (1-15)；` unsigned_number ` Tag for default-route (0-65535)。

[条件 C-15a4ce18907d371a](../../evidence/conditions-sets-009.md#c-15a4ce18907d371a) · [参数 P-d205d807f0f6ea44](../../evidence/parameters-sets-016.md#p-d205d807f0f6ea44) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-066927

```text
(config-if)# ip rip authentication key-chain <string> <cr>
```

Handler ` RVA 0xFB54010 `；selector ` 3 `；EOL ` RVA 0x34824A20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` name of key-chain。

[条件 C-8b81da1fd3ec4205](../../evidence/conditions-sets-054.md#c-8b81da1fd3ec4205) · [参数 P-436caf253ffda67c](../../evidence/parameters-sets-006.md#p-436caf253ffda67c) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-066915

```text
(config-if)# ip rip authentication mode text <cr>
```

Handler ` RVA 0xFB54010 `；selector ` 2 `；EOL ` RVA 0x34824688 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-aa2d19834770b183](../../evidence/conditions-sets-066.md#c-aa2d19834770b183) · [状态效果 S-ea7de71958d19f4d](../../evidence/state_effects-sets-050.md#s-ea7de71958d19f4d)

### path-063602

```text
(config-if)# ip rip initial-delay <number:0..1800> <cr>
```

Handler ` RVA 0xFB54010 `；selector ` 8 `；EOL ` RVA 0x34823550 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` interval in seconds。

[条件 C-f0af1d72c59273e1](../../evidence/conditions-sets-093.md#c-f0af1d72c59273e1) · [参数 P-592e72e5871bdcdd](../../evidence/parameters-sets-007.md#p-592e72e5871bdcdd) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-065948

```text
(config-if)# ip rip receive version <cr>
```

Handler ` RVA 0xFB54010 `；selector ` 1 `；EOL ` RVA 0x34824250 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-37b1e973e3dcb9ac](../../evidence/conditions-sets-022.md#c-37b1e973e3dcb9ac) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-065933

```text
(config-if)# ip rip send version <cr>
```

Handler ` RVA 0xFB54010 `；selector ` 0 `；EOL ` RVA 0x34823E18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9f0d1ed5132af555](../../evidence/conditions-sets-061.md#c-9f0d1ed5132af555) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-064434

```text
(config-if)# ip rip triggered <cr>
```

Handler ` RVA 0xFB54010 `；selector ` 4 `；EOL ` RVA 0x34822E90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-333736ec97b5ee66](../../evidence/conditions-sets-020.md#c-333736ec97b5ee66) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-064453

```text
(config-if)# ip rip v2-broadcast <cr>
```

Handler ` RVA 0xFB54010 `；selector ` 6 `；EOL ` RVA 0x34823528 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6b90d5bf90f603e3](../../evidence/conditions-sets-042.md#c-6b90d5bf90f603e3) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-063431

```text
(config-if)# ip route-cache <cr>
```

Handler ` RVA 0xCF33E40 `；selector ` 9 `；EOL ` RVA 0x33D28AD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-07a3dc2096366792](../../evidence/conditions-sets-003.md#c-07a3dc2096366792)

### path-064114

```text
(config-if)# ip route-cache same-interface <cr>
```

Handler ` RVA 0xCF343F0 `；selector ` 12 `；EOL ` RVA 0x33D3E0C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-07a3dc2096366792](../../evidence/conditions-sets-003.md#c-07a3dc2096366792)

### path-064500

```text
(config-if)# ip router isis <cr>
```

Handler ` RVA 0xFD60450 `；selector ` 22 `；EOL ` RVA 0x34B98450 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-17ddbd9f5229c56e](../../evidence/conditions-sets-009.md#c-17ddbd9f5229c56e) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-067434

```text
(config-if)# ip rsvp aggregation ip role interior <cr>
```

Handler ` RVA 0x101C2F40 `；selector ` 1 `；EOL ` RVA 0x34A68DA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8791a865dd7e91fd](../../evidence/conditions-sets-052.md#c-8791a865dd7e91fd)

### path-063736

```text
(config-if)# ip rsvp atm-peak-rate-limit <number:1..2139095> <cr>
```

Handler ` RVA 0x10054E80 `；selector ` 0 `；EOL ` RVA 0x34A527E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Maximum peak rate to be used in SVC setup (in kilobytes) 。

[条件 C-fe6980fd0b67241f](../../evidence/conditions-sets-098.md#c-fe6980fd0b67241f) · [参数 P-40c3ced6ba99ea73](../../evidence/parameters-sets-005.md#p-40c3ced6ba99ea73)

### path-065085

```text
(config-if)# ip rsvp authentication <cr>
```

Handler ` RVA 0x10073550 `；selector ` 10 `；EOL ` RVA 0x34A57B18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f700c2056aae74d0](../../evidence/conditions-sets-095.md#c-f700c2056aae74d0)

### path-066341

```text
(config-if)# ip rsvp authentication challenge <cr>
```

Handler ` RVA 0x10073550 `；selector ` 8 `；EOL ` RVA 0x34A57520 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bd10c0af0d27d949](../../evidence/conditions-sets-073.md#c-bd10c0af0d27d949)

### path-067115

```text
(config-if)# ip rsvp authentication exception fast-reroute <cr>
```

Handler ` RVA 0x10073550 `；selector ` 11 `；EOL ` RVA 0x34A57878 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-54995ddf823db0dc](../../evidence/conditions-sets-033.md#c-54995ddf823db0dc) · [状态效果 S-b465debcc64991c5](../../evidence/state_effects-sets-038.md#s-b465debcc64991c5)

### path-067042

```text
(config-if)# ip rsvp authentication key <string> <cr>
```

Handler ` RVA 0x10073550 `；selector ` 6 `；EOL ` RVA 0x34A56398 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Password (8 to 40 characters, spaces allowed)。

[条件 C-56f72a25e39dd77b](../../evidence/conditions-sets-034.md#c-56f72a25e39dd77b) · [参数 P-3c1ea58cb7369e5f](../../evidence/parameters-sets-005.md#p-3c1ea58cb7369e5f)

### path-067055

```text
(config-if)# ip rsvp authentication key-chain <string> <cr>
```

Handler ` RVA 0x10073550 `；selector ` 12 `；EOL ` RVA 0x34A566E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of key chain (as created by global "key chain" command)。

[条件 C-8a94f93966407ca1](../../evidence/conditions-sets-054.md#c-8a94f93966407ca1) · [参数 P-e7a61500913361a2](../../evidence/parameters-sets-017.md#p-e7a61500913361a2)

### path-067864

```text
(config-if)# ip rsvp authentication lifetime <hh:mm:ss> <cr>
```

Handler ` RVA 0x10073550 `；selector ` 9 `；EOL ` RVA 0x34A57200 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` time_hms ` Lifetime (default = 30 mins)。

[条件 C-3cfab1b5237ee8f9](../../evidence/conditions-sets-024.md#c-3cfab1b5237ee8f9) · [缺口 G-8808f984bd00f56a](../../evidence/gaps-sets-005.md#g-8808f984bd00f56a) · [参数 P-376a1fd736090b76](../../evidence/parameters-sets-005.md#p-376a1fd736090b76)

### path-066347

```text
(config-if)# ip rsvp authentication type <cr>
```

Handler ` RVA 0x10073550 `；selector ` 7 `；EOL ` RVA 0x34A56E18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-439a727580d90435](../../evidence/conditions-sets-026.md#c-439a727580d90435)

### path-067085

```text
(config-if)# ip rsvp authentication window-size <number:1..64> <cr>
```

Handler ` RVA 0x10073550 `；selector ` 5 `；EOL ` RVA 0x34A56A70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Maximum number of messages allowed in receive window (default = 1)。

[条件 C-b8504445d97aa964](../../evidence/conditions-sets-071.md#c-b8504445d97aa964) · [参数 P-ca42beaec8753a62](../../evidence/parameters-sets-015.md#p-ca42beaec8753a62)

### path-064638

```text
(config-if)# ip rsvp bandwidth <cr>
```

Handler ` RVA 0x10058B60 `；selector ` 0 `；EOL ` RVA 0x34A4E0A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e2266d0773b005dc](../../evidence/conditions-sets-087.md#c-e2266d0773b005dc) · [状态效果 S-ecc7c006a17ad1bc](../../evidence/state_effects-sets-050.md#s-ecc7c006a17ad1bc)

### path-066146

```text
(config-if)# ip rsvp burst policing <cr>
```

Handler ` RVA 0x10070280 `；selector ` 0 `；EOL ` RVA 0x34A536E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5deccf9d803bd267](../../evidence/conditions-sets-037.md#c-5deccf9d803bd267)

### path-066983

```text
(config-if)# ip rsvp data-packet classification none <cr>
```

Handler ` RVA 0x100706B0 `；selector ` 1 `；EOL ` RVA 0x34A530F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1b511c223b82091a](../../evidence/conditions-sets-011.md#c-1b511c223b82091a)

### path-066261

```text
(config-if)# ip rsvp dsbm candidate <cr>
```

Handler ` RVA 0x1006F810 `；selector ` 0 `；EOL ` RVA 0x34A54EA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fa07f201e74a1c07](../../evidence/conditions-sets-097.md#c-fa07f201e74a1c07) · [状态效果 S-112615f74853100e](../../evidence/state_effects-sets-004.md#s-112615f74853100e)

### path-067505

```text
(config-if)# ip rsvp dsbm non-resv-send-limit burst <number:1..2147483> <cr>
```

Handler ` RVA 0x1006FD80 `；selector ` 1 `；EOL ` RVA 0x34A555B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Maximum burst (Kbytes)。

[条件 C-7d5c9b8d7b00511c](../../evidence/conditions-sets-049.md#c-7d5c9b8d7b00511c) · [参数 P-cbd1dfddbb9ca48a](../../evidence/parameters-sets-015.md#p-cbd1dfddbb9ca48a)

### path-067518

```text
(config-if)# ip rsvp dsbm non-resv-send-limit max-unit <number:1..2147483647> <cr>
```

Handler ` RVA 0x1006FD80 `；selector ` 4 `；EOL ` RVA 0x34A55F80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Maximum packet size (bytes)。

[条件 C-47e930f7e8628f8a](../../evidence/conditions-sets-028.md#c-47e930f7e8628f8a) · [参数 P-08cf69ec5d2a9ed6](../../evidence/parameters-sets-001.md#p-08cf69ec5d2a9ed6)

### path-067514

```text
(config-if)# ip rsvp dsbm non-resv-send-limit min-unit <number:1..2147483647> <cr>
```

Handler ` RVA 0x1006FD80 `；selector ` 3 `；EOL ` RVA 0x34A55C58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Minimum policed unit (bytes)。

[条件 C-d5718131c1b9dce6](../../evidence/conditions-sets-082.md#c-d5718131c1b9dce6) · [参数 P-ddf5c6151848d69d](../../evidence/parameters-sets-017.md#p-ddf5c6151848d69d)

### path-067510

```text
(config-if)# ip rsvp dsbm non-resv-send-limit peak <number:1..2147483> <cr>
```

Handler ` RVA 0x1006FD80 `；selector ` 2 `；EOL ` RVA 0x34A55908 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Peak rate (Kbytes/sec)。

[条件 C-6fdd09a3f74ee58e](../../evidence/conditions-sets-043.md#c-6fdd09a3f74ee58e) · [参数 P-6ab447796f916079](../../evidence/parameters-sets-008.md#p-6ab447796f916079)

### path-067501

```text
(config-if)# ip rsvp dsbm non-resv-send-limit rate <number:1..2147483> <cr>
```

Handler ` RVA 0x1006FD80 `；selector ` 0 `；EOL ` RVA 0x34A55268 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Average rate (Kbytes/sec)。

[条件 C-8e84302b89cfad9d](../../evidence/conditions-sets-055.md#c-8e84302b89cfad9d) · [参数 P-e75be1287f412f7d](../../evidence/parameters-sets-017.md#p-e75be1287f412f7d)

### path-064861

```text
(config-if)# ip rsvp dsbm-candidate <cr>
```

Handler ` RVA 0x1006FD20 `；selector ` 0 `；EOL ` RVA 0x34A54A98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f4a3a05125f8747b](../../evidence/conditions-sets-094.md#c-f4a3a05125f8747b) · [状态效果 S-fbd7dc591bdb09f0](../../evidence/state_effects-sets-053.md#s-fbd7dc591bdb09f0)

### path-064655

```text
(config-if)# ip rsvp flow-assist <cr>
```

Handler ` RVA 0x10055630 `；selector ` 0 `；EOL ` RVA 0x34A52248 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5478f38c6e442d93](../../evidence/conditions-sets-033.md#c-5478f38c6e442d93)

### path-066961

```text
(config-if)# ip rsvp listener outbound reply <cr>
```

Handler ` RVA 0x1005E650 `；selector ` 0 `；EOL ` RVA 0x34A58448 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-25e37d0c86b7d36a](../../evidence/conditions-sets-015.md#c-25e37d0c86b7d36a) · [状态效果 S-85a690e1a44d43a6](../../evidence/state_effects-sets-028.md#s-85a690e1a44d43a6)

### path-064645

```text
(config-if)# ip rsvp neighbor <cr>
```

Handler ` RVA 0x10056250 `；selector ` 0 `；EOL ` RVA 0x34A4F570 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5478f38c6e442d93](../../evidence/conditions-sets-033.md#c-5478f38c6e442d93)

### path-067885

```text
(config-if)# ip rsvp policy <?test_subsys_action@555589fa15e0> local default <cr>
```

Handler ` RVA 0x101134B0 `；selector ` 257 `；EOL ` RVA 0x34A4D6F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8791a865dd7e91fd](../../evidence/conditions-sets-052.md#c-8791a865dd7e91fd) · [缺口 G-1f5a5bbbdb9d7f0b](../../evidence/gaps-sets-002.md#g-1f5a5bbbdb9d7f0b) · [状态效果 S-58489e3d660c6354](../../evidence/state_effects-sets-019.md#s-58489e3d660c6354)

### path-064958

```text
(config-if)# ip rsvp precedence <cr>
```

Handler ` RVA 0x10055330 `；selector ` 0 `；EOL ` RVA 0x34A54618 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7013f791dac64be9](../../evidence/conditions-sets-043.md#c-7013f791dac64be9)

### path-066141

```text
(config-if)# ip rsvp resource-provider none <cr>
```

Handler ` RVA 0x100708B0 `；selector ` 1 `；EOL ` RVA 0x34A53A68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f0b3c9061b75d314](../../evidence/conditions-sets-093.md#c-f0b3c9061b75d314)

### path-067019

```text
(config-if)# ip rsvp resource-provider wfq interface <cr>
```

Handler ` RVA 0x100708B0 `；selector ` 3 `；EOL ` RVA 0x34A53D90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-43cb2ad8f93b20b0](../../evidence/conditions-sets-027.md#c-43cb2ad8f93b20b0)

### path-067030

```text
(config-if)# ip rsvp resource-provider wfq pvc <cr>
```

Handler ` RVA 0x100708B0 `；selector ` 4 `；EOL ` RVA 0x34A54038 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-43cb2ad8f93b20b0](../../evidence/conditions-sets-027.md#c-43cb2ad8f93b20b0)

### path-066955

```text
(config-if)# ip rsvp signalling blockade <number:1..65536> <cr>
```

Handler ` RVA 0x10055B10 `；selector ` 0 `；EOL ` RVA 0x34A50018 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of refresh intervals over which to enforce blockades。

[条件 C-11772048a7d7a004](../../evidence/conditions-sets-007.md#c-11772048a7d7a004) · [参数 P-f7e8746c7317a8ac](../../evidence/parameters-sets-018.md#p-f7e8746c7317a8ac)

### path-066949

```text
(config-if)# ip rsvp signalling dscp <number:0..63> <cr>
```

Handler ` RVA 0x10055CD0 `；selector ` 0 `；EOL ` RVA 0x34A4FCC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` DSCP value。

[条件 C-6f93db38e3cbd74f](../../evidence/conditions-sets-043.md#c-6f93db38e3cbd74f) · [参数 P-ce8212d4207cc479](../../evidence/parameters-sets-016.md#p-ce8212d4207cc479)

### path-067452

```text
(config-if)# ip rsvp signalling fast-local-repair wait-time <number:0..5000> <cr>
```

Handler ` RVA 0x10055E90 `；selector ` 0 `；EOL ` RVA 0x34A4F968 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Wait Time for start of Fast Local Repair in msec。

[条件 C-b671aef005c4fe6c](../../evidence/conditions-sets-071.md#c-b671aef005c4fe6c) · [参数 P-bfde160585354e21](../../evidence/parameters-sets-015.md#p-bfde160585354e21)

### path-066165

```text
(config-if)# ip rsvp signalling hello <cr>
```

Handler ` RVA 0x10074E00 `；selector ` 0 `；EOL ` RVA 0x34A51C18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ab2d19c615609ac9](../../evidence/conditions-sets-066.md#c-ab2d19c615609ac9)

### path-066965

```text
(config-if)# ip rsvp signalling hello bfd <cr>
```

Handler ` RVA 0x10075080 `；selector ` 0 `；EOL ` RVA 0x34A50398 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-eb1ef206bc7cc1a0](../../evidence/conditions-sets-091.md#c-eb1ef206bc7cc1a0)

### path-067484

```text
(config-if)# ip rsvp signalling hello dscp <number:0..63> <cr>
```

Handler ` RVA 0x10075880 `；selector ` 4 `；EOL ` RVA 0x34A51810 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Hello Messages DSCP value。

[条件 C-4146425cb0952bc7](../../evidence/conditions-sets-026.md#c-4146425cb0952bc7) · [参数 P-34d596d235a369cd](../../evidence/parameters-sets-004.md#p-34d596d235a369cd)

### path-067025

```text
(config-if)# ip rsvp signalling hello graceful-restart <cr>
```

Handler ` RVA 0x100754F0 `；selector ` 0 `；EOL ` RVA 0x34A51C80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-faa6c0070ec85aed](../../evidence/conditions-sets-097.md#c-faa6c0070ec85aed)

### path-067649

```text
(config-if)# ip rsvp signalling hello refresh interval <number:10..30000> <cr>
```

Handler ` RVA 0x10075880 `；selector ` 1 `；EOL ` RVA 0x34A51218 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Hello interval in msec。

[条件 C-d9216742b09e7132](../../evidence/conditions-sets-084.md#c-d9216742b09e7132) · [参数 P-4ddc79255bff1b9e](../../evidence/parameters-sets-006.md#p-4ddc79255bff1b9e)

### path-067653

```text
(config-if)# ip rsvp signalling hello refresh misses <number:4..10> <cr>
```

Handler ` RVA 0x10075880 `；selector ` 2 `；EOL ` RVA 0x34A51508 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of Hello misses。

[条件 C-e2d0e0c144f7878a](../../evidence/conditions-sets-087.md#c-e2d0e0c144f7878a) · [参数 P-37227e2c38f34f44](../../evidence/parameters-sets-005.md#p-37227e2c38f34f44)

### path-067645

```text
(config-if)# ip rsvp signalling hello reroute dscp <number:0..63> <cr>
```

Handler ` RVA 0x10075BA0 `；selector ` 4 `；EOL ` RVA 0x34A50DD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Hello Messages DSCP value。

[条件 C-ef6cb0ef331c70f7](../../evidence/conditions-sets-092.md#c-ef6cb0ef331c70f7) · [参数 P-cf4389495cb0287e](../../evidence/parameters-sets-016.md#p-cf4389495cb0287e)

### path-067695

```text
(config-if)# ip rsvp signalling hello reroute refresh interval <number:1000..30000> <cr>
```

Handler ` RVA 0x10075BA0 `；selector ` 1 `；EOL ` RVA 0x34A507E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Hello Reroute interval in msec。

[条件 C-e5cd60522c745595](../../evidence/conditions-sets-089.md#c-e5cd60522c745595) · [参数 P-8ab35949898e7684](../../evidence/parameters-sets-011.md#p-8ab35949898e7684)

### path-067698

```text
(config-if)# ip rsvp signalling hello reroute refresh misses <number:4..10> <cr>
```

Handler ` RVA 0x10075BA0 `；selector ` 2 `；EOL ` RVA 0x34A50AD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of Hello misses。

[条件 C-b917f4f14a4c1e76](../../evidence/conditions-sets-071.md#c-b917f4f14a4c1e76) · [参数 P-c1d8f38d723358c4](../../evidence/parameters-sets-015.md#p-c1d8f38d723358c4)

### path-067054

```text
(config-if)# ip rsvp source address <address> <cr>
```

Handler ` RVA 0x100773C0 `；selector ` 0 `；EOL ` RVA 0x34A57E50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Source IP address。

[条件 C-dcb73a69543a76b1](../../evidence/conditions-sets-085.md#c-dcb73a69543a76b1) · [参数 P-28066812089e0dc2](../../evidence/parameters-sets-003.md#p-28066812089e0dc2) · [状态效果 S-2b1afbdc9b93a07b](../../evidence/state_effects-sets-010.md#s-2b1afbdc9b93a07b)

### path-067862

```text
(config-if)# ip rsvp source interface <interface> <cr>
```

Handler ` RVA 0x100773C0 `；selector ` 0 `；EOL ` RVA 0x34A57E50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5ac3c95c8027e0d9](../../evidence/conditions-sets-036.md#c-5ac3c95c8027e0d9) · [缺口 G-c0935d066d3c91af](../../evidence/gaps-sets-007.md#g-c0935d066d3c91af) · [参数 P-5b91a2fd7a767811](../../evidence/parameters-sets-007.md#p-5b91a2fd7a767811) · [状态效果 S-52f9dc13e8cf9c33](../../evidence/state_effects-sets-018.md#s-52f9dc13e8cf9c33)

### path-064686

```text
(config-if)# ip rsvp svc-required <cr>
```

Handler ` RVA 0x100556B0 `；selector ` 0 `；EOL ` RVA 0x34A52568 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bd2e9aa085713615](../../evidence/conditions-sets-073.md#c-bd2e9aa085713615)

### path-064845

```text
(config-if)# ip rsvp tos <cr>
```

Handler ` RVA 0x10055050 `；selector ` 0 `；EOL ` RVA 0x34A52BB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c7a8038cdbf3563d](../../evidence/conditions-sets-077.md#c-c7a8038cdbf3563d)

### path-065997

```text
(config-if)# ip rsvp tunnel overhead-percent <cr>
```

Handler ` RVA 0x100564E0 `；selector ` 0 `；EOL ` RVA 0x34A4F1F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-dc02453546bda8e4](../../evidence/conditions-sets-085.md#c-dc02453546bda8e4)

### path-064628

```text
(config-if)# ip rsvp udp-multicasts <cr>
```

Handler ` RVA 0x10056E60 `；selector ` 0 `；EOL ` RVA 0x34A4EE58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8791a865dd7e91fd](../../evidence/conditions-sets-052.md#c-8791a865dd7e91fd)

### path-067807

```text
(config-if)# ip rtp compression-connections <number:dynamic> <cr>
```

Handler ` RVA 0xD195AE0 `；selector ` 0 `；EOL ` RVA 0x33DAA790 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Number of connections。

[条件 C-2dae4bea36d15c07](../../evidence/conditions-sets-018.md#c-2dae4bea36d15c07) · [缺口 G-b9e8616c891f8afd](../../evidence/gaps-sets-007.md#g-b9e8616c891f8afd) · [参数 P-2cbacf98ba621c5f](../../evidence/parameters-sets-004.md#p-2cbacf98ba621c5f)

### path-064585

```text
(config-if)# ip rtp header-compression <cr>
```

Handler ` RVA 0xD1967C0 `；selector ` 0 `；EOL ` RVA 0x33DAA338 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c32b95c43a3dc72c](../../evidence/conditions-sets-075.md#c-c32b95c43a3dc72c)

### path-064215

```text
(config-if)# ip sap listen <cr>
```

Handler ` RVA 0xF87E120 `；selector ` 1 `；EOL ` RVA 0x34734C98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8905dbb66d92b58e](../../evidence/conditions-sets-053.md#c-8905dbb66d92b58e)

### path-064228

```text
(config-if)# ip security add <cr>
```

Handler ` RVA 0xCF34DD0 `；selector ` 2 `；EOL ` RVA 0x33D23158 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-17ddbd9f5229c56e](../../evidence/conditions-sets-009.md#c-17ddbd9f5229c56e) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-064344

```text
(config-if)# ip security dedicated <cr>
```

Handler ` RVA 0xCF34DD0 `；selector ` 4 `；EOL ` RVA 0x33D24A58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-dd77dc28508a7c04](../../evidence/conditions-sets-085.md#c-dd77dc28508a7c04) · [状态效果 S-d27dbdade5acadf6](../../evidence/state_effects-sets-045.md#s-d27dbdade5acadf6)

### path-065671

```text
(config-if)# ip security dedicated Reserved1 <cr>
```

Handler ` RVA 0xCF34DD0 `；selector ` 8 `；EOL ` RVA 0x33D24798 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-85c56f9c88c9f5c2](../../evidence/conditions-sets-052.md#c-85c56f9c88c9f5c2) · [状态效果 S-95ab3799096bc149](../../evidence/state_effects-sets-032.md#s-95ab3799096bc149)

### path-065685

```text
(config-if)# ip security dedicated Reserved1 <cr>
```

Handler ` RVA 0xCF34DD0 `；selector ` 9 `；EOL ` RVA 0x33D24A80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1d4a8bb73c8da0ef](../../evidence/conditions-sets-011.md#c-1d4a8bb73c8da0ef) · [状态效果 S-95ab3799096bc149](../../evidence/state_effects-sets-032.md#s-95ab3799096bc149)

### path-067851

```text
(config-if)# ip security dedicated Reserved1 to <cr>
```

Handler ` RVA 0xCF34DD0 `；selector ` 4 `；EOL ` RVA 0x33D24A58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-bb0b242902029d80](../../evidence/conditions-sets-072.md#c-bb0b242902029d80) · [缺口 G-a6ad51aa0bcc756c](../../evidence/gaps-sets-006.md#g-a6ad51aa0bcc756c) · [状态效果 S-4c0606ea22823be5](../../evidence/state_effects-sets-017.md#s-4c0606ea22823be5)

### path-067883

```text
(config-if)# ip security dedicated Reserved1 to Reserved1 <cr>
```

Handler ` RVA 0xCF34DD0 `；selector ` 8 `；EOL ` RVA 0x33D24798 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a127b0427f2dfffb](../../evidence/conditions-sets-062.md#c-a127b0427f2dfffb) · [缺口 G-a6ad51aa0bcc756c](../../evidence/gaps-sets-006.md#g-a6ad51aa0bcc756c) · [状态效果 S-ecbec82450dcb078](../../evidence/state_effects-sets-050.md#s-ecbec82450dcb078)

### path-067884

```text
(config-if)# ip security dedicated Reserved1 to Reserved1 <cr>
```

Handler ` RVA 0xCF34DD0 `；selector ` 9 `；EOL ` RVA 0x33D24A80 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-24042ad4d93c5e02](../../evidence/conditions-sets-014.md#c-24042ad4d93c5e02) · [缺口 G-a6ad51aa0bcc756c](../../evidence/gaps-sets-006.md#g-a6ad51aa0bcc756c) · [状态效果 S-ecbec82450dcb078](../../evidence/state_effects-sets-050.md#s-ecbec82450dcb078)

### path-067845

```text
(config-if)# ip security eso-min <number:0..255> <hex-data> <cr>
```

Handler ` RVA 0xCF34970 `；selector ` 0 `；EOL ` RVA 0x33D256E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` ESO source；` hexdata ` Compartment bits in hex。

[条件 C-ab22568af40e968f](../../evidence/conditions-sets-066.md#c-ab22568af40e968f) · [缺口 G-39add461be15f427](../../evidence/gaps-sets-002.md#g-39add461be15f427) · [参数 P-d23aee3bc108aee7](../../evidence/parameters-sets-016.md#p-d23aee3bc108aee7) · [状态效果 S-287564453f8bd7ac](../../evidence/state_effects-sets-009.md#s-287564453f8bd7ac)

### path-064236

```text
(config-if)# ip security extended-allowed <cr>
```

Handler ` RVA 0xCF34DD0 `；selector ` 3 `；EOL ` RVA 0x33D23400 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-17ddbd9f5229c56e](../../evidence/conditions-sets-009.md#c-17ddbd9f5229c56e) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-064246

```text
(config-if)# ip security extended-ignored <cr>
```

Handler ` RVA 0xCF34DD0 `；selector ` 6 `；EOL ` RVA 0x33D236A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-17ddbd9f5229c56e](../../evidence/conditions-sets-009.md#c-17ddbd9f5229c56e) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-064258

```text
(config-if)# ip security first <cr>
```

Handler ` RVA 0xCF34DD0 `；selector ` 0 `；EOL ` RVA 0x33D23BF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-17ddbd9f5229c56e](../../evidence/conditions-sets-009.md#c-17ddbd9f5229c56e) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-064265

```text
(config-if)# ip security ignore-authorities <cr>
```

Handler ` RVA 0xCF34DD0 `；selector ` 5 `；EOL ` RVA 0x33D23EA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-17ddbd9f5229c56e](../../evidence/conditions-sets-009.md#c-17ddbd9f5229c56e) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-064276

```text
(config-if)# ip security ignore-cipso <cr>
```

Handler ` RVA 0xCF34DD0 `；selector ` 7 `；EOL ` RVA 0x33D24148 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-17ddbd9f5229c56e](../../evidence/conditions-sets-009.md#c-17ddbd9f5229c56e) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-064253

```text
(config-if)# ip security reserved-allowed <cr>
```

Handler ` RVA 0xCF34DD0 `；selector ` 10 `；EOL ` RVA 0x33D23950 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-17ddbd9f5229c56e](../../evidence/conditions-sets-009.md#c-17ddbd9f5229c56e) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-064288

```text
(config-if)# ip security strip <cr>
```

Handler ` RVA 0xCF34DD0 `；selector ` 1 `；EOL ` RVA 0x33D25320 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-17ddbd9f5229c56e](../../evidence/conditions-sets-009.md#c-17ddbd9f5229c56e) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-063441

```text
(config-if)# ip split-horizon <cr>
```

Handler ` RVA 0xE1FAB20 `；selector ` 0 `；EOL ` RVA 0x34257A98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fa418361cc754694](../../evidence/conditions-sets-097.md#c-fa418361cc754694)

### path-065512

```text
(config-if)# ip split-horizon eigrp <number:1..65535> <cr>
```

Handler ` RVA 0xF58CAE0 `；selector ` 133 `；EOL ` RVA 0x346DCE58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` AS number。

[条件 C-fa418361cc754694](../../evidence/conditions-sets-097.md#c-fa418361cc754694) · [参数 P-1a44f54621a3caa9](../../evidence/parameters-sets-002.md#p-1a44f54621a3caa9) · [状态效果 S-1ae8ed3b6882ac5f](../../evidence/state_effects-sets-006.md#s-1ae8ed3b6882ac5f)

### path-063463

```text
(config-if)# ip sticky-arp <cr>
```

Handler ` RVA 0xCF33480 `；selector ` 0 `；EOL ` RVA 0x33D21960 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a1d840fa0bc3aa08](../../evidence/conditions-sets-062.md#c-a1d840fa0bc3aa08) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-064590

```text
(config-if)# ip subscriber routed <cr>
```

Handler ` RVA 0x11A371C0 `；selector ` 0 `；EOL ` RVA 0x355CC2C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-66a88553a2d9242b](../../evidence/conditions-sets-040.md#c-66a88553a2d9242b) · [状态效果 S-eadfa3427b1d2844](../../evidence/state_effects-sets-050.md#s-eadfa3427b1d2844)

### path-067838

```text
(config-if)# ip summary-address <?router_action_proc_vpn@555589d79118> <address> <address> <cr>
```

Handler ` RVA 0xFB54010 `；selector ` 5 `；EOL ` RVA 0x348251B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` IP address；` address ` IP network mask。

[条件 C-fa418361cc754694](../../evidence/conditions-sets-097.md#c-fa418361cc754694) · [缺口 G-f6da75dfd6308b26](../../evidence/gaps-sets-009.md#g-f6da75dfd6308b26) · [参数 P-c754db5e7eebe858](../../evidence/parameters-sets-015.md#p-c754db5e7eebe858)

### path-067879

```text
(config-if)# ip summary-address eigrp <number:1..65535> <address> <address> <cr>
```

Handler ` RVA 0xF5E07B0 `；selector ` 134 `；EOL ` RVA 0x346DD318 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` AS number；` address ` Summary IP address；` address ` IP network mask。

[条件 C-45be22e43466bbb7](../../evidence/conditions-sets-027.md#c-45be22e43466bbb7) · [缺口 G-10bf28a20cba743e](../../evidence/gaps-sets-001.md#g-10bf28a20cba743e) · [参数 P-6fd520bd57cb6d6d](../../evidence/parameters-sets-009.md#p-6fd520bd57cb6d6d) · [状态效果 S-47b09e6faa91150b](../../evidence/state_effects-sets-016.md#s-47b09e6faa91150b)

### path-063438

```text
(config-if)# ip tcp adjust-mss <number:500..1460> <cr>
```

Handler ` RVA 0xCDEDB20 `；selector ` 47 `；EOL ` RVA 0x33D019B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Maximum segment size in bytes。

[条件 C-d30531586039ca14](../../evidence/conditions-sets-081.md#c-d30531586039ca14) · [参数 P-bafeeb6ead950358](../../evidence/parameters-sets-014.md#p-bafeeb6ead950358)

### path-063442

```text
(config-if)# ip tcp compression-connections <number:1..256> <cr>
```

Handler ` RVA 0xD195EB0 `；selector ` 0 `；EOL ` RVA 0x33DABEA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of connections。

[条件 C-beddbfca187705e8](../../evidence/conditions-sets-074.md#c-beddbfca187705e8) · [参数 P-3a83edbde2918bfb](../../evidence/parameters-sets-005.md#p-3a83edbde2918bfb)

### path-064205

```text
(config-if)# ip tcp header-compression <cr>
```

Handler ` RVA 0xD196D00 `；selector ` 0 `；EOL ` RVA 0x33DABF40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2ea048f2a57df95b](../../evidence/conditions-sets-018.md#c-2ea048f2a57df95b) · [状态效果 S-74db2956e7a07041](../../evidence/state_effects-sets-025.md#s-74db2956e7a07041)

### path-063501

```text
(config-if)# ip topology-accounting <cr>
```

Handler ` RVA 0xDB6A700 `；selector ` 0 `；EOL ` RVA 0x33FE62B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-918abd0d1f8dffe8](../../evidence/conditions-sets-056.md#c-918abd0d1f8dffe8) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-063613

```text
(config-if)# ip trigger-authentication <cr>
```

Handler ` RVA 0x10571410 `；selector ` 1 `；EOL ` RVA 0x34B5A3F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a7d361126c094a17](../../evidence/conditions-sets-065.md#c-a7d361126c094a17) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-067737

```text
(config-if)# ip unnumbered <interface> <cr>
```

Handler ` RVA 0xCEC41C0 `；selector ` 0 `；EOL ` RVA 0x33D26A40 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-73f2af8a1cda5e1d](../../evidence/conditions-sets-045.md#c-73f2af8a1cda5e1d) · [缺口 G-0374ccfd28c8e92c](../../evidence/gaps-sets-001.md#g-0374ccfd28c8e92c) · [参数 P-cb4ecac6a58d9a9d](../../evidence/parameters-sets-015.md#p-cb4ecac6a58d9a9d) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-063447

```text
(config-if)# ip unreachables <cr>
```

Handler ` RVA 0xCF34540 `；selector ` 4 `；EOL ` RVA 0x33D20FA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a1d840fa0bc3aa08](../../evidence/conditions-sets-062.md#c-a1d840fa0bc3aa08) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-063494

```text
(config-if)# ip urd <cr>
```

Handler ` RVA 0xF883270 `；selector ` 0 `；EOL ` RVA 0x34735020 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d99dec4da0148931](../../evidence/conditions-sets-084.md#c-d99dec4da0148931)

### path-067442

```text
(config-if)# ip verify unicast notification threshold <number:0..4294967295> <cr>
```

Handler ` RVA 0xB6250D0 `；selector ` 2 `；EOL ` RVA 0x337C99C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Drop rate in pps triggering notify - 0 is any drops。

[条件 C-d10dff47316a93a4](../../evidence/conditions-sets-081.md#c-d10dff47316a93a4) · [参数 P-526abff72f471205](../../evidence/parameters-sets-007.md#p-526abff72f471205) · [状态效果 S-dba8b74d89069337](../../evidence/state_effects-sets-046.md#s-dba8b74d89069337)

### path-067858

```text
(config-if)# ip verify unicast reverse-path <?option@555588d1dd40> <cr>
```

Handler ` RVA 0xB6255B0 `；selector ` 0 `；EOL ` RVA 0x337C98B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9ef4910ba09fc1cc](../../evidence/conditions-sets-061.md#c-9ef4910ba09fc1cc) · [缺口 G-1a188bc310363624](../../evidence/gaps-sets-001.md#g-1a188bc310363624) · [状态效果 S-2718e668b92404b5](../../evidence/state_effects-sets-009.md#s-2718e668b92404b5)

### path-066052

```text
(config-if)# ip verify unicast reverse-path <cr>
```

Handler ` RVA 0xB6255B0 `；selector ` 0 `；EOL ` RVA 0x337C98B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9e0c07037a139d71](../../evidence/conditions-sets-061.md#c-9e0c07037a139d71) · [状态效果 S-2718e668b92404b5](../../evidence/state_effects-sets-009.md#s-2718e668b92404b5)

### path-063665

```text
(config-if)# ip virtual-reassembly <cr>
```

Handler ` RVA 0xC78BC80 `；selector ` 0 `；EOL ` RVA 0x33AEAC40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-61151227a4e48383](../../evidence/conditions-sets-038.md#c-61151227a4e48383) · [状态效果 S-237c052d85f9ea77](../../evidence/state_effects-sets-008.md#s-237c052d85f9ea77)

### path-067796

```text
(config-if)# ip vrf autoclassify source <cr>
```

Handler ` RVA 0xCFD7910 `；selector ` 0 `；EOL ` RVA 0x33D77620 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5e4d6647fe48c011](../../evidence/conditions-sets-037.md#c-5e4d6647fe48c011) · [缺口 G-58905f704c5427cd](../../evidence/gaps-sets-004.md#g-58905f704c5427cd) · [状态效果 S-319f06f01f3bb672](../../evidence/state_effects-sets-011.md#s-319f06f01f3bb672)

### path-067799

```text
(config-if)# ip vrf receive <string> <cr>
```

Handler ` RVA 0xFADE850 `；selector ` 1 `；EOL ` RVA 0x34807A30 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Table name。

[条件 C-5e4d6647fe48c011](../../evidence/conditions-sets-037.md#c-5e4d6647fe48c011) · [缺口 G-58905f704c5427cd](../../evidence/gaps-sets-004.md#g-58905f704c5427cd) · [参数 P-461a4dfaf2c49eb5](../../evidence/parameters-sets-006.md#p-461a4dfaf2c49eb5) · [状态效果 S-e013a482d9488325](../../evidence/state_effects-sets-047.md#s-e013a482d9488325)

### path-067797

```text
(config-if)# ip vrf select source <cr>
```

Handler ` RVA 0xFADE850 `；selector ` 0 `；EOL ` RVA 0x34807730 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5e4d6647fe48c011](../../evidence/conditions-sets-037.md#c-5e4d6647fe48c011) · [缺口 G-58905f704c5427cd](../../evidence/gaps-sets-004.md#g-58905f704c5427cd) · [状态效果 S-e013a482d9488325](../../evidence/state_effects-sets-047.md#s-e013a482d9488325)

### path-067739

```text
(config-if)# ip vrf sitemap <cr>
```

Handler ` RVA 0xDC2A990 `；selector ` 1 `；EOL ` RVA 0x34013BE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-422305b068780ec1](../../evidence/conditions-sets-026.md#c-422305b068780ec1) · [缺口 G-58905f704c5427cd](../../evidence/gaps-sets-004.md#g-58905f704c5427cd) · [状态效果 S-e013a482d9488325](../../evidence/state_effects-sets-047.md#s-e013a482d9488325)

### path-066745

```text
(config-if)# ip wccp redirect exclude in <cr>
```

Handler ` RVA 0x10AD1F30 `；selector ` 2 `；EOL ` RVA 0x34C99140 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1ac9a68940d5d8dc](../../evidence/conditions-sets-010.md#c-1ac9a68940d5d8dc) · [状态效果 S-e6aa0119000e87f6](../../evidence/state_effects-sets-049.md#s-e6aa0119000e87f6)

### path-064399

```text
(config-if)# ip wccp web-cache <cr>
```

Handler ` RVA 0x10AD1F30 `；selector ` 6 `；EOL ` RVA 0x34C99EB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-39bbcb7a51dca719](../../evidence/conditions-sets-022.md#c-39bbcb7a51dca719) · [状态效果 S-57328c29f2611c4a](../../evidence/state_effects-sets-019.md#s-57328c29f2611c4a)

### path-065705

```text
(config-if)# ip wccp web-cache group-listen <cr>
```

Handler ` RVA 0x10AD1F30 `；selector ` 5 `；EOL ` RVA 0x34C99BF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-02a38accd442c4fd](../../evidence/conditions-sets-001.md#c-02a38accd442c4fd) · [状态效果 S-57328c29f2611c4a](../../evidence/state_effects-sets-019.md#s-57328c29f2611c4a)

### path-066765

```text
(config-if)# ip wccp web-cache redirect in <cr>
```

Handler ` RVA 0x10AD1F30 `；selector ` 1 `；EOL ` RVA 0x34C99958 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-66b0277514b0e0a9](../../evidence/conditions-sets-040.md#c-66b0277514b0e0a9) · [状态效果 S-57328c29f2611c4a](../../evidence/state_effects-sets-019.md#s-57328c29f2611c4a)

### path-066754

```text
(config-if)# ip wccp web-cache redirect out <cr>
```

Handler ` RVA 0x10AD1F30 `；selector ` 0 `；EOL ` RVA 0x34C99670 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7308a81bc8d53b16](../../evidence/conditions-sets-044.md#c-7308a81bc8d53b16) · [状态效果 S-57328c29f2611c4a](../../evidence/state_effects-sets-019.md#s-57328c29f2611c4a)

### path-066127

```text
(config-if)# ipv6 address <address> link-local <cr>
```

Handler ` RVA 0x123011F0 `；selector ` 2 `；EOL ` RVA 0x357DD1E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IPv6 link-local address。

[条件 C-5b521a0242790101](../../evidence/conditions-sets-036.md#c-5b521a0242790101) · [参数 P-387326c7d0442fc9](../../evidence/parameters-sets-005.md#p-387326c7d0442fc9) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-063880

```text
(config-if)# ipv6 address <cr>
```

Handler ` RVA 0x123011F0 `；selector ` 1 `；EOL ` RVA 0x357DD520 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e3f7d4509c993121](../../evidence/conditions-sets-088.md#c-e3f7d4509c993121) · [状态效果 S-a94c1b59bc94866c](../../evidence/state_effects-sets-036.md#s-a94c1b59bc94866c)

### path-067781

```text
(config-if)# ipv6 address <prefix:dynamic> <cr>
```

Handler ` RVA 0x123011F0 `；selector ` 1 `；EOL ` RVA 0x357DD520 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` IPv6 prefix。

[条件 C-ba58de64d86ec833](../../evidence/conditions-sets-072.md#c-ba58de64d86ec833) · [缺口 G-45fc05ef3a3fb392](../../evidence/gaps-sets-003.md#g-45fc05ef3a3fb392) · [参数 P-e299cc61c21bf417](../../evidence/parameters-sets-017.md#p-e299cc61c21bf417) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-064746

```text
(config-if)# ipv6 address autoconfig <cr>
```

Handler ` RVA 0x123011F0 `；selector ` 3 `；EOL ` RVA 0x357DCE08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-96d9b597753adceb](../../evidence/conditions-sets-058.md#c-96d9b597753adceb) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-064802

```text
(config-if)# ipv6 address dhcp <cr>
```

Handler ` RVA 0x1218DDC0 `；selector ` 0 `；EOL ` RVA 0x357BC848 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a63f40b13b9e969d](../../evidence/conditions-sets-064.md#c-a63f40b13b9e969d) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-067494

```text
(config-if)# ipv6 authentication key-chain eigrp <number:1..65535> <string> <cr>
```

Handler ` RVA 0xF58CAE0 `；selector ` 122 `；EOL ` RVA 0x35468CB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` AS number；` string ` name of key-chain。

[条件 C-2031f3fd60878758](../../evidence/conditions-sets-013.md#c-2031f3fd60878758) · [参数 P-f20fbfee16d0ee65](../../evidence/parameters-sets-018.md#p-f20fbfee16d0ee65) · [状态效果 S-f2e6681386526499](../../evidence/state_effects-sets-051.md#s-f2e6681386526499)

### path-067483

```text
(config-if)# ipv6 authentication mode eigrp <number:1..65535> md5 <cr>
```

Handler ` RVA 0xF58CAE0 `；selector ` 123 `；EOL ` RVA 0x354688E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` AS number。

[条件 C-96d9b597753adceb](../../evidence/conditions-sets-058.md#c-96d9b597753adceb) · [参数 P-806e93774a122416](../../evidence/parameters-sets-010.md#p-806e93774a122416) · [状态效果 S-6e207d6a31953ea4](../../evidence/state_effects-sets-023.md#s-6e207d6a31953ea4)

### path-067029

```text
(config-if)# ipv6 bandwidth-percent eigrp <number:1..65535> <number:1..999999> <cr>
```

Handler ` RVA 0xF58CAE0 `；selector ` 124 `；EOL ` RVA 0x354690B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` AS number；` unsigned_number ` Maximum bandwidth percentage that EIGRP may use。

[条件 C-9dc7d4e5aa8600a8](../../evidence/conditions-sets-061.md#c-9dc7d4e5aa8600a8) · [参数 P-1d802fd6416c9ac6](../../evidence/parameters-sets-003.md#p-1d802fd6416c9ac6) · [状态效果 S-f2e6681386526499](../../evidence/state_effects-sets-051.md#s-f2e6681386526499)

### path-063877

```text
(config-if)# ipv6 cef <cr>
```

Handler ` RVA 0xB67CF80 `；selector ` 0 `；EOL ` RVA 0x337D7FE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c480350eb46705c3](../../evidence/conditions-sets-076.md#c-c480350eb46705c3) · [状态效果 S-441d999be940cc74](../../evidence/state_effects-sets-015.md#s-441d999be940cc74)

### path-066281

```text
(config-if)# ipv6 dampening-change eigrp <number:1..65535> <cr>
```

Handler ` RVA 0xF58CAE0 `；selector ` 125 `；EOL ` RVA 0x35469498 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` AS number。

[条件 C-a07528be3a94a0a8](../../evidence/conditions-sets-062.md#c-a07528be3a94a0a8) · [参数 P-1188406346602e7b](../../evidence/parameters-sets-002.md#p-1188406346602e7b) · [状态效果 S-10a9dc3a9b50a2a2](../../evidence/state_effects-sets-004.md#s-10a9dc3a9b50a2a2)

### path-066302

```text
(config-if)# ipv6 dampening-interval eigrp <number:1..65535> <cr>
```

Handler ` RVA 0xF58CAE0 `；selector ` 126 `；EOL ` RVA 0x354698B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` AS number。

[条件 C-499dd4d1947174e2](../../evidence/conditions-sets-029.md#c-499dd4d1947174e2) · [参数 P-441b8c010eddef14](../../evidence/parameters-sets-006.md#p-441b8c010eddef14) · [状态效果 S-43217374ff8d4665](../../evidence/state_effects-sets-015.md#s-43217374ff8d4665)

### path-063783

```text
(config-if)# ipv6 destination-guard <cr>
```

Handler ` RVA 0x136B0F50 `；selector ` 1601 `；EOL ` RVA 0x35C02750 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5875cb038016265f](../../evidence/conditions-sets-035.md#c-5875cb038016265f) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-067642

```text
(config-if)# ipv6 dhcp client information refresh minimum <number:60..3600> <cr>
```

Handler ` RVA 0x1218C490 `；selector ` 0 `；EOL ` RVA 0x357BAD90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Seconds。

[条件 C-5b7a5e72c310c0b2](../../evidence/conditions-sets-036.md#c-5b7a5e72c310c0b2) · [参数 P-6ee5e1dd9d4e09db](../../evidence/parameters-sets-009.md#p-6ee5e1dd9d4e09db) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-067024

```text
(config-if)# ipv6 dhcp client pd <string> <cr>
```

Handler ` RVA 0x1218D210 `；selector ` 0 `；EOL ` RVA 0x357BC448 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Prefix name, truncated to 200 characters。

[条件 C-6cb9802972dcd995](../../evidence/conditions-sets-042.md#c-6cb9802972dcd995) · [参数 P-8c349df752524aae](../../evidence/parameters-sets-011.md#p-8c349df752524aae) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-067890

```text
(config-if)# ipv6 dhcp client pd hint <prefix:dynamic> <cr>
```

Handler ` RVA 0x1218CE70 `；selector ` 0 `；EOL ` RVA 0x357BC110 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` IPv6 x:x::y/&lt;z&gt;。

[条件 C-3e3132d9fa17df96](../../evidence/conditions-sets-024.md#c-3e3132d9fa17df96) · [缺口 G-eedded8b546a56ef](../../evidence/gaps-sets-008.md#g-eedded8b546a56ef) · [参数 P-0128d929e4505a53](../../evidence/parameters-sets-001.md#p-0128d929e4505a53) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-066970

```text
(config-if)# ipv6 dhcp client request vendor <cr>
```

Handler ` RVA 0x1218C670 `；selector ` 0 `；EOL ` RVA 0x357BB100 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-90d0a3ad7dae2d64](../../evidence/conditions-sets-056.md#c-90d0a3ad7dae2d64) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-067473

```text
(config-if)# ipv6 dhcp client vendor-class ascii <string> <cr>
```

Handler ` RVA 0x1218C840 `；selector ` 2 `；EOL ` RVA 0x357BB788 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Vendor class data string。

[条件 C-2ee13f223bdac3d9](../../evidence/conditions-sets-018.md#c-2ee13f223bdac3d9) · [参数 P-3c1f053e8241d861](../../evidence/parameters-sets-005.md#p-3c1f053e8241d861) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-067008

```text
(config-if)# ipv6 dhcp client vendor-class disable <cr>
```

Handler ` RVA 0x1218C840 `；selector ` 4 `；EOL ` RVA 0x357BBD58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-93da2144acc7671e](../../evidence/conditions-sets-057.md#c-93da2144acc7671e) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-067892

```text
(config-if)# ipv6 dhcp client vendor-class hex <hex-string> <cr>
```

Handler ` RVA 0x1218C840 `；selector ` 3 `；EOL ` RVA 0x357BBA98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` hexstring ` Vendor class hex data。

[条件 C-4e6007e9ec77e60f](../../evidence/conditions-sets-031.md#c-4e6007e9ec77e60f) · [缺口 G-d5f585e3fb6e324f](../../evidence/gaps-sets-007.md#g-d5f585e3fb6e324f) · [参数 P-4fec1a0ec0ed64b9](../../evidence/parameters-sets-007.md#p-4fec1a0ec0ed64b9) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-066974

```text
(config-if)# ipv6 dhcp client vendor-class mac-address <cr>
```

Handler ` RVA 0x1218C840 `；selector ` 1 `；EOL ` RVA 0x357BB490 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-264458af7b49f574](../../evidence/conditions-sets-015.md#c-264458af7b49f574) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-067154

```text
(config-if)# ipv6 dhcp framed password <string> <cr>
```

Handler ` RVA 0x121CD380 `；selector ` 0 `；EOL ` RVA 0x357C5608 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Password for Framed-IPv6-Prefix allocation。

[条件 C-aedc1952a2f2f88a](../../evidence/conditions-sets-068.md#c-aedc1952a2f2f88a) · [参数 P-565bd3ce81d196b0](../../evidence/parameters-sets-007.md#p-565bd3ce81d196b0) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-067170

```text
(config-if)# ipv6 dhcp relay destination <address> <cr>
```

Handler ` RVA 0x121B2150 `；selector ` 0 `；EOL ` RVA 0x357C1B20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IPv6 address。

[条件 C-5638cb7d8e8a61cc](../../evidence/conditions-sets-034.md#c-5638cb7d8e8a61cc) · [参数 P-eaaafb6cfbde2adb](../../evidence/parameters-sets-018.md#p-eaaafb6cfbde2adb) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-067893

```text
(config-if)# ipv6 dhcp relay destination <address> <interface> <cr>
```

Handler ` RVA 0x121B2150 `；selector ` 0 `；EOL ` RVA 0x357C1B20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` IPv6 address。

[条件 C-53d3966d98d66fa5](../../evidence/conditions-sets-033.md#c-53d3966d98d66fa5) · [缺口 G-2c6a7daca160e082](../../evidence/gaps-sets-002.md#g-2c6a7daca160e082) · [参数 P-d325f8ff9b4e3435](../../evidence/parameters-sets-016.md#p-d325f8ff9b4e3435) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-067143

```text
(config-if)# ipv6 dhcp relay option vpn <cr>
```

Handler ` RVA 0x121B32C0 `；selector ` 0 `；EOL ` RVA 0x357C2AA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0a278732559ea77f](../../evidence/conditions-sets-004.md#c-0a278732559ea77f) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-067136

```text
(config-if)# ipv6 dhcp relay short-lease <number:60..3600> <cr>
```

Handler ` RVA 0x121AEDC0 `；selector ` 0 `；EOL ` RVA 0x357C2538 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` T1 (Short Lease Renew) in Seconds。

[条件 C-0a278732559ea77f](../../evidence/conditions-sets-004.md#c-0a278732559ea77f) · [参数 P-6225c605c54bed8b](../../evidence/parameters-sets-008.md#p-6225c605c54bed8b) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-067869

```text
(config-if)# ipv6 dhcp relay source-interface <interface> <cr>
```

Handler ` RVA 0x121AEB80 `；selector ` 0 `；EOL ` RVA 0x357C2158 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3c28c50485967e74](../../evidence/conditions-sets-023.md#c-3c28c50485967e74) · [缺口 G-9090fa29b80ef109](../../evidence/gaps-sets-005.md#g-9090fa29b80ef109) · [参数 P-e97d20714c8106ca](../../evidence/parameters-sets-017.md#p-e97d20714c8106ca) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-066392

```text
(config-if)# ipv6 dhcp relay trust <cr>
```

Handler ` RVA 0x121B3110 `；selector ` 0 `；EOL ` RVA 0x357C27C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0a278732559ea77f](../../evidence/conditions-sets-004.md#c-0a278732559ea77f) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-065140

```text
(config-if)# ipv6 dhcp server <cr>
```

Handler ` RVA 0x121CCE50 `；selector ` 0 `；EOL ` RVA 0x357C4F78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cc845aff188ba446](../../evidence/conditions-sets-079.md#c-cc845aff188ba446) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-064808

```text
(config-if)# ipv6 eigrp <number:1..65535> <cr>
```

Handler ` RVA 0xF58CAE0 `；selector ` 128 `；EOL ` RVA 0x354684D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` AS number。

[条件 C-96d9b597753adceb](../../evidence/conditions-sets-058.md#c-96d9b597753adceb) · [参数 P-a1d2ed2b9ae17e03](../../evidence/parameters-sets-012.md#p-a1d2ed2b9ae17e03) · [状态效果 S-f2e6681386526499](../../evidence/state_effects-sets-051.md#s-f2e6681386526499)

### path-063784

```text
(config-if)# ipv6 enable <cr>
```

Handler ` RVA 0x122FF770 `；selector ` 0 `；EOL ` RVA 0x357E07D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9156b6e8fa685e22](../../evidence/conditions-sets-056.md#c-9156b6e8fa685e22) · [状态效果 S-33566865e6b6edd6](../../evidence/state_effects-sets-011.md#s-33566865e6b6edd6)

### path-068015

```text
(config-if)# ipv6 flow monitor <?option@555588f619a8> sampler <cr>
```

Handler ` RVA 0xC1F7CA0 `；selector ` 0 `；EOL ` RVA 0x33A0DBD0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ba237ae0679e41cd](../../evidence/conditions-sets-072.md#c-ba237ae0679e41cd) · [缺口 G-2d48111062402419](../../evidence/gaps-sets-002.md#g-2d48111062402419) · [状态效果 S-68ec5ee7a2e47e21](../../evidence/state_effects-sets-022.md#s-68ec5ee7a2e47e21)

### path-067774

```text
(config-if)# ipv6 flow monitor <cr>
```

Handler ` RVA 0xC1F7D50 `；selector ` 0 `；EOL ` RVA 0x33A0DE88 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4a64af0399bbff5f](../../evidence/conditions-sets-029.md#c-4a64af0399bbff5f) · [缺口 G-0c2533fc1b8e934f](../../evidence/gaps-sets-001.md#g-0c2533fc1b8e934f) · [状态效果 S-68ec5ee7a2e47e21](../../evidence/state_effects-sets-022.md#s-68ec5ee7a2e47e21)

### path-067070

```text
(config-if)# ipv6 hello-interval eigrp <number:1..65535> <number:1..65535> <cr>
```

Handler ` RVA 0xF58CAE0 `；selector ` 129 `；EOL ` RVA 0x35469CD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` AS number；` unsigned_number ` Seconds between hello transmissions。

[条件 C-6cb46414cf552fbe](../../evidence/conditions-sets-042.md#c-6cb46414cf552fbe) · [参数 P-1440a474063e1f90](../../evidence/parameters-sets-002.md#p-1440a474063e1f90) · [状态效果 S-f2e6681386526499](../../evidence/state_effects-sets-051.md#s-f2e6681386526499)

### path-067084

```text
(config-if)# ipv6 hold-time eigrp <number:1..65535> <number:1..65535> <cr>
```

Handler ` RVA 0xF58CAE0 `；selector ` 130 `；EOL ` RVA 0x3546A0C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` AS number；` unsigned_number ` Seconds before neighbor is considered down。

[条件 C-2f4b0d87d36111ef](../../evidence/conditions-sets-019.md#c-2f4b0d87d36111ef) · [参数 P-4cdcb6a496ff45ef](../../evidence/parameters-sets-006.md#p-4cdcb6a496ff45ef) · [状态效果 S-f2e6681386526499](../../evidence/state_effects-sets-051.md#s-f2e6681386526499)

### path-066117

```text
(config-if)# ipv6 mfib cef input <cr>
```

Handler ` RVA 0x11904EB0 `；selector ` 4 `；EOL ` RVA 0x3553EDB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-96d9b597753adceb](../../evidence/conditions-sets-058.md#c-96d9b597753adceb) · [状态效果 S-4e4f3092f8b794bd](../../evidence/state_effects-sets-017.md#s-4e4f3092f8b794bd)

### path-066138

```text
(config-if)# ipv6 mfib cef output <cr>
```

Handler ` RVA 0x11904EB0 `；selector ` 8 `；EOL ` RVA 0x3553F060 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-96d9b597753adceb](../../evidence/conditions-sets-058.md#c-96d9b597753adceb) · [状态效果 S-4e4f3092f8b794bd](../../evidence/state_effects-sets-017.md#s-4e4f3092f8b794bd)

### path-064843

```text
(config-if)# ipv6 mfib forwarding <cr>
```

Handler ` RVA 0x11904EB0 `；selector ` 2147483649 `；EOL ` RVA 0x3553EAD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8edbaaad496e998e](../../evidence/conditions-sets-055.md#c-8edbaaad496e998e) · [状态效果 S-4e4f3092f8b794bd](../../evidence/state_effects-sets-017.md#s-4e4f3092f8b794bd)

### path-066098

```text
(config-if)# ipv6 mfib forwarding input <cr>
```

Handler ` RVA 0x11904EB0 `；selector ` 1 `；EOL ` RVA 0x3553E568 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-96d9b597753adceb](../../evidence/conditions-sets-058.md#c-96d9b597753adceb) · [状态效果 S-4e4f3092f8b794bd](../../evidence/state_effects-sets-017.md#s-4e4f3092f8b794bd)

### path-066120

```text
(config-if)# ipv6 mfib forwarding output <cr>
```

Handler ` RVA 0x11904EB0 `；selector ` 2 `；EOL ` RVA 0x3553E810 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-96d9b597753adceb](../../evidence/conditions-sets-058.md#c-96d9b597753adceb) · [状态效果 S-4e4f3092f8b794bd](../../evidence/state_effects-sets-017.md#s-4e4f3092f8b794bd)

### path-066172

```text
(config-if)# ipv6 mfib test adjacency <cr>
```

Handler ` RVA 0x11904EB0 `；selector ` 512 `；EOL ` RVA 0x3553F888 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-96d9b597753adceb](../../evidence/conditions-sets-058.md#c-96d9b597753adceb) · [状态效果 S-4e4f3092f8b794bd](../../evidence/state_effects-sets-017.md#s-4e4f3092f8b794bd)

### path-066195

```text
(config-if)# ipv6 mfib test headless <cr>
```

Handler ` RVA 0x11904EB0 `；selector ` 1024 `；EOL ` RVA 0x3553FB30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-96d9b597753adceb](../../evidence/conditions-sets-058.md#c-96d9b597753adceb) · [状态效果 S-4e4f3092f8b794bd](../../evidence/state_effects-sets-017.md#s-4e4f3092f8b794bd)

### path-066149

```text
(config-if)# ipv6 mfib test macfilter <cr>
```

Handler ` RVA 0x11904EB0 `；selector ` 32768 `；EOL ` RVA 0x3553F5E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-96d9b597753adceb](../../evidence/conditions-sets-058.md#c-96d9b597753adceb) · [状态效果 S-4e4f3092f8b794bd](../../evidence/state_effects-sets-017.md#s-4e4f3092f8b794bd)

### path-066133

```text
(config-if)# ipv6 mfib test mask <cr>
```

Handler ` RVA 0x11904EB0 `；selector ` 256 `；EOL ` RVA 0x3553F338 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-96d9b597753adceb](../../evidence/conditions-sets-058.md#c-96d9b597753adceb) · [状态效果 S-4e4f3092f8b794bd](../../evidence/state_effects-sets-017.md#s-4e4f3092f8b794bd)

