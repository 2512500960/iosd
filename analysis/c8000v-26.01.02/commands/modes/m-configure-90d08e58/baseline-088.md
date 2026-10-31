# configure · 六个基础模式的历史连接

[模式索引](README.md) · [总索引](../../README.md)

### path-054728

```text
(config)# no do-exec test ifs disk modes <string> <cr>
```

Handler ` RVA 0xD65FD60 `；selector ` 9 `；EOL ` RVA 0x33EC3CB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` URL for disk file。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-9c06b36a6a837b34](../../evidence/parameters-sets-012.md#p-9c06b36a6a837b34) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-054681

```text
(config)# no do-exec test ifs disk rdwr <string> <cr>
```

Handler ` RVA 0xD65FD60 `；selector ` 7 `；EOL ` RVA 0x33EC3710 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` URL for disk file。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-c0576a6ad695a918](../../evidence/parameters-sets-015.md#p-c0576a6ad695a918) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-048034

```text
(config)# no do-exec test ifs show hidden <cr>
```

Handler ` RVA 0xD65FD60 `；selector ` 5 `；EOL ` RVA 0x33EC33D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-039028

```text
(config)# no do-exec test ifs slot <cr>
```

Handler ` RVA 0xD65FD60 `；selector ` 6 `；EOL ` RVA 0x33EC3018 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-957e7ebfbe332d5f](../../evidence/conditions-sets-058.md#c-957e7ebfbe332d5f) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-028566

```text
(config)# no do-exec test interfaces <cr>
```

Handler ` RVA 0xE8F4F60 `；selector ` 0 `；EOL ` RVA 0x3433F348 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-18472d7888f7c1a4](../../evidence/conditions-sets-009.md#c-18472d7888f7c1a4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-059063

```text
(config)# no do-exec test ip access-list dynamic delete <number:100..199> <number:1..262144> <cr>
```

Handler ` RVA 0xCF06CB0 `；selector ` 0 `；EOL ` RVA 0x33D565B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Extended ACL；` unsigned_number ` handle。

[条件 C-aad388a616fbeb7d](../../evidence/conditions-sets-066.md#c-aad388a616fbeb7d) · [参数 P-891680d3d0bbb4cb](../../evidence/parameters-sets-011.md#p-891680d3d0bbb4cb) · [状态效果 S-af08e84a4348ee5f](../../evidence/state_effects-sets-037.md#s-af08e84a4348ee5f)

### path-057074

```text
(config)# no do-exec test ip access-list dynamic empty <number:100..199> <cr>
```

Handler ` RVA 0xCF073F0 `；selector ` 0 `；EOL ` RVA 0x33D560A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Extended ACL。

[条件 C-aad388a616fbeb7d](../../evidence/conditions-sets-066.md#c-aad388a616fbeb7d) · [参数 P-3210d07544b61f37](../../evidence/parameters-sets-004.md#p-3210d07544b61f37) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-044948

```text
(config)# no do-exec test ip access-list register <cr>
```

Handler ` RVA 0xCF065A0 `；selector ` 0 `；EOL ` RVA 0x33D56DC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f75acb2a779d8db1](../../evidence/conditions-sets-096.md#c-f75acb2a779d8db1) · [状态效果 S-36ba92a50550799e](../../evidence/state_effects-sets-012.md#s-36ba92a50550799e)

### path-059747

```text
(config)# no do-exec test ip dhcp api pool <string> <string> create <cr>
```

Handler ` RVA 0xD2C3400 `；selector ` 0 `；EOL ` RVA 0x33DD7270 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Pool name；` string ` Pool owner name。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-07dc240d29126b32](../../evidence/parameters-sets-001.md#p-07dc240d29126b32) · [状态效果 S-668e981c8e45cf05](../../evidence/state_effects-sets-022.md#s-668e981c8e45cf05)

### path-053203

```text
(config)# no do-exec test ip dhcp query <address> <cr>
```

Handler ` RVA 0xD250100 `；selector ` 0 `；EOL ` RVA 0x33DD6E40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` Client IP address。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-e83f674c88cc9462](../../evidence/parameters-sets-017.md#p-e83f674c88cc9462) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-053112

```text
(config)# no do-exec test ip dhcp terminate <address> <cr>
```

Handler ` RVA 0xD250060 `；selector ` 0 `；EOL ` RVA 0x33DD6AE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` Client IP address。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-3b4645e85fd16383](../../evidence/parameters-sets-005.md#p-3b4645e85fd16383) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-057230

```text
(config)# no do-exec test ip domain apis <address> <string> <cr>
```

Handler ` RVA 0xD139D60 `；selector ` 0 `；EOL ` RVA 0x33D96B38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` Host IP address；` string ` VRF name。

[条件 C-f4c93b68702085dd](../../evidence/conditions-sets-094.md#c-f4c93b68702085dd) · [参数 P-787fba5cde6b4234](../../evidence/parameters-sets-009.md#p-787fba5cde6b4234) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-045242

```text
(config)# no do-exec test ip domain default-domain <cr>
```

Handler ` RVA 0xD139380 `；selector ` 0 `；EOL ` RVA 0x33D95E68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d8a6173b822f2a2c](../../evidence/conditions-sets-083.md#c-d8a6173b822f2a2c) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-053002

```text
(config)# no do-exec test ip domain get-ipv4-server <number:0..25> <cr>
```

Handler ` RVA 0xD139580 `；selector ` 0 `；EOL ` RVA 0x33D967E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Server index。

[条件 C-0e897ddcacc96c4e](../../evidence/conditions-sets-006.md#c-0e897ddcacc96c4e) · [参数 P-64d2f2e2a2204061](../../evidence/parameters-sets-008.md#p-64d2f2e2a2204061) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-052968

```text
(config)# no do-exec test ip domain get-server <number:0..25> <cr>
```

Handler ` RVA 0xD139440 `；selector ` 0 `；EOL ` RVA 0x33D964F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Server index。

[条件 C-915c9c26d21d1955](../../evidence/conditions-sets-056.md#c-915c9c26d21d1955) · [参数 P-a508c7655a359164](../../evidence/parameters-sets-013.md#p-a508c7655a359164) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-053270

```text
(config)# no do-exec test ip domain lookup <address> <cr>
```

Handler ` RVA 0xD137930 `；selector ` 0 `；EOL ` RVA 0x33D972D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` IP address。

[条件 C-0b99e5c2da2dd36e](../../evidence/conditions-sets-005.md#c-0b99e5c2da2dd36e) · [参数 P-b70e952a38201f2e](../../evidence/parameters-sets-014.md#p-b70e952a38201f2e) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-053170

```text
(config)# no do-exec test ip domain mcast-lookup <address> <cr>
```

Handler ` RVA 0xD140A70 `；selector ` 0 `；EOL ` RVA 0x33D976F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` IP address。

[条件 C-be304ce819f20fed](../../evidence/conditions-sets-073.md#c-be304ce819f20fed) · [参数 P-c09f62870a65c5cd](../../evidence/parameters-sets-015.md#p-c09f62870a65c5cd) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-059090

```text
(config)# no do-exec test ip domain name-delete <string> <number:1..255> <number:1..4194304> <cr>
```

Handler ` RVA 0xD139670 `；selector ` 0 `；EOL ` RVA 0x33D96200 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Hostname；` unsigned_number ` Namekind；` unsigned_number ` Type。

[条件 C-4b21fbaa6292d072](../../evidence/conditions-sets-029.md#c-4b21fbaa6292d072) · [参数 P-e34808f4aca9e093](../../evidence/parameters-sets-017.md#p-e34808f4aca9e093) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-052850

```text
(config)# no do-exec test ip multicast sync resume <cr>
```

Handler ` RVA 0xD470550 `；selector ` 1 `；EOL ` RVA 0x33E51598 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-052814

```text
(config)# no do-exec test ip multicast sync suspend <cr>
```

Handler ` RVA 0xD470550 `；selector ` 0 `；EOL ` RVA 0x33E512F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-053032

```text
(config)# no do-exec test ip nat clear translations <cr>
```

Handler ` RVA 0xFA39690 `；selector ` 0 `；EOL ` RVA 0x347DE818 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-045688

```text
(config)# no do-exec test ip nat dump <cr>
```

Handler ` RVA 0xFA39B10 `；selector ` 0 `；EOL ` RVA 0x347DF4B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-d837862e5a1cf5c4](../../evidence/state_effects-sets-046.md#s-d837862e5a1cf5c4)

### path-053160

```text
(config)# no do-exec test ip nat portmap trans_report <cr>
```

Handler ` RVA 0xFA39700 `；selector ` 0 `；EOL ` RVA 0x347DEDB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-2604d2badabef78a](../../evidence/state_effects-sets-009.md#s-2604d2badabef78a)

### path-057263

```text
(config)# no do-exec test ip nat show pool <string> <cr>
```

Handler ` RVA 0xFA38D50 `；selector ` 0 `；EOL ` RVA 0x347DDF38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Pool name。

[条件 C-b1309a7e1ed805ca](../../evidence/conditions-sets-069.md#c-b1309a7e1ed805ca) · [参数 P-2fc9437051580fb2](../../evidence/parameters-sets-004.md#p-2fc9437051580fb2) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-057201

```text
(config)# no do-exec test ip nat show pool all <cr>
```

Handler ` RVA 0xFA38D50 `；selector ` 1 `；EOL ` RVA 0x347DDC38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-057289

```text
(config)# no do-exec test ip nat show rule <string> <cr>
```

Handler ` RVA 0xFA38D50 `；selector ` 2 `；EOL ` RVA 0x347DE508 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Rule name。

[条件 C-a188749f3840f2b8](../../evidence/conditions-sets-062.md#c-a188749f3840f2b8) · [参数 P-83418bd3b9811e31](../../evidence/parameters-sets-010.md#p-83418bd3b9811e31) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-057231

```text
(config)# no do-exec test ip nat show rule all <cr>
```

Handler ` RVA 0xFA38D50 `；selector ` 3 `；EOL ` RVA 0x347DE208 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-045409

```text
(config)# no do-exec test ip nat-route database <cr>
```

Handler ` RVA 0x13725FC0 `；selector ` 0 `；EOL ` RVA 0x35C0F330 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-bfdc7db0b231813d](../../evidence/state_effects-sets-041.md#s-bfdc7db0b231813d)

### path-053045

```text
(config)# no do-exec test ip nbar batch-config end <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 5 `；EOL ` RVA 0x35259330 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-053004

```text
(config)# no do-exec test ip nbar batch-config start <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 4 `；EOL ` RVA 0x35259088 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-053089

```text
(config)# no do-exec test ip nbar byte-count-window disable <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 9 `；EOL ` RVA 0x352596A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-5569324e9de1ff6e](../../evidence/state_effects-sets-019.md#s-5569324e9de1ff6e)

### path-052855

```text
(config)# no do-exec test ip nbar caches clear <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 29 `；EOL ` RVA 0x35255258 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-057115

```text
(config)# no do-exec test ip nbar caches export <string> <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 28 `；EOL ` RVA 0x35254FD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` File name to load (json format)。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-3b46f8fae4be42bd](../../evidence/parameters-sets-005.md#p-3b46f8fae4be42bd) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-057101

```text
(config)# no do-exec test ip nbar caches import <string> <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 27 `；EOL ` RVA 0x35254CF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` File name to load (json format)。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-693dea4536eeb117](../../evidence/parameters-sets-008.md#p-693dea4536eeb117) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-052892

```text
(config)# no do-exec test ip nbar caches show <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 30 `；EOL ` RVA 0x35255500 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-053117

```text
(config)# no do-exec test ip nbar cedge-simulation disable <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 11 `；EOL ` RVA 0x35259C80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-053080

```text
(config)# no do-exec test ip nbar cedge-simulation enable <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 10 `；EOL ` RVA 0x352599D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-052873

```text
(config)# no do-exec test ip nbar config-mode async <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 8 `；EOL ` RVA 0x35257498 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-052920

```text
(config)# no do-exec test ip nbar config-mode sync <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 7 `；EOL ` RVA 0x35257740 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-059132

```text
(config)# no do-exec test ip nbar dataplane-info-monitor memory-thresholds low <number:1..100> <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 14 `；EOL ` RVA 0x3525A618 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Low threshold in percents。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-2360135968ca2bc4](../../evidence/parameters-sets-003.md#p-2360135968ca2bc4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-057308

```text
(config)# no do-exec test ip nbar dataplane-info-monitor traffic-over-subscription-state false <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 12 `；EOL ` RVA 0x3525A290 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-057273

```text
(config)# no do-exec test ip nbar dataplane-info-monitor traffic-over-subscription-state true <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 13 `；EOL ` RVA 0x35259FE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-052956

```text
(config)# no do-exec test ip nbar function <string> <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 6 `；EOL ` RVA 0x35257AA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Function name。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-4af9a509018bb542](../../evidence/parameters-sets-006.md#p-4af9a509018bb542) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-052847

```text
(config)# no do-exec test ip nbar npc disable <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 19 `；EOL ` RVA 0x35255B90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-057131

```text
(config)# no do-exec test ip nbar npc enable <string> <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 18 `；EOL ` RVA 0x352558E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` File name to load (json format)。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-b8c3dd324e3e92e2](../../evidence/parameters-sets-014.md#p-b8c3dd324e3e92e2) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-057155

```text
(config)# no do-exec test ip nbar npc pack-mode allow <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 21 `；EOL ` RVA 0x35256120 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-057172

```text
(config)# no do-exec test ip nbar npc pack-mode disallow <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 22 `；EOL ` RVA 0x352563C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-052888

```text
(config)# no do-exec test ip nbar npc save <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 20 `；EOL ` RVA 0x35255E38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-053145

```text
(config)# no do-exec test ip nbar set-max-protocol-id-no-cloud_ext <number:0..32767> <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 15 `；EOL ` RVA 0x3525A950 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` max protocol id without cloud extension。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-507a9096f4509329](../../evidence/parameters-sets-007.md#p-507a9096f4509329) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-057324

```text
(config)# no do-exec test ip nbar set-protocol-feature-support <number:0..255> <number:0..255> <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 16 `；EOL ` RVA 0x3525AC88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Feature id；` unsigned_number ` Feature value。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-bdb8d401bdc33739](../../evidence/parameters-sets-014.md#p-bdb8d401bdc33739) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-045814

```text
(config)# no do-exec test ip nbar show-features-activation <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 17 `；EOL ` RVA 0x3525AF38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-045758

```text
(config)# no do-exec test ip nbar show-fib-ad-info <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 31 `；EOL ` RVA 0x3525BA58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-052880

```text
(config)# no do-exec test ip nbar track-ip disable <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 24 `；EOL ` RVA 0x35256C30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-060240

```text
(config)# no do-exec test ip nbar track-ip enable <string> port <number:0..4294967295> vrf-id <number:0..4294967295> l4-proto <number:0..255> memory-size <number:0..20000> <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 23 `；EOL ` RVA 0x35256978 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` IPv4/v6 to track；` unsigned_number ` port number；` unsigned_number ` VRF id；` unsigned_number ` L4 Protocol；` unsigned_number ` memory size in KB。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-74d155980cc4da67](../../evidence/parameters-sets-009.md#p-74d155980cc4da67) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-052925

```text
(config)# no do-exec test ip nbar track-ip flush <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 25 `；EOL ` RVA 0x35256ED8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-052951

```text
(config)# no do-exec test ip nbar track-ip status <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 26 `；EOL ` RVA 0x35257180 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-045437

```text
(config)# no do-exec test ip omp flush <cr>
```

Handler ` RVA 0x137422E0 `；selector ` 0 `；EOL ` RVA 0x35C105C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d5d31c3f438ffd21](../../evidence/conditions-sets-082.md#c-d5d31c3f438ffd21) · [状态效果 S-b75f83942905526f](../../evidence/state_effects-sets-039.md#s-b75f83942905526f)

### path-052753

```text
(config)# no do-exec test ip pbr ipv6 attach <cr>
```

Handler ` RVA 0x10C6E4E0 `；selector ` 0 `；EOL ` RVA 0x34CF0520 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4292a4821897d1f5](../../evidence/conditions-sets-026.md#c-4292a4821897d1f5) · [状态效果 S-03aeb9988c6551cf](../../evidence/state_effects-sets-001.md#s-03aeb9988c6551cf)

### path-052729

```text
(config)# no do-exec test ip pbr map <string> <cr>
```

Handler ` RVA 0x10C6E570 `；selector ` 0 `；EOL ` RVA 0x34CF0228 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` PBR route-map name。

[条件 C-4292a4821897d1f5](../../evidence/conditions-sets-026.md#c-4292a4821897d1f5) · [参数 P-e93b53fee09f3a16](../../evidence/parameters-sets-017.md#p-e93b53fee09f3a16) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-052950

```text
(config)# no do-exec test ip rib api iprib_geteachroute <cr>
```

Handler ` RVA 0xE2634E0 `；selector ` 2 `；EOL ` RVA 0x3423BD18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-e0a46229b6186f91](../../evidence/state_effects-sets-048.md#s-e0a46229b6186f91)

### path-035996

```text
(config)# no do-exec test ip rmap <cr>
```

Handler ` RVA 0xE207640 `；selector ` 0 `；EOL ` RVA 0x3423B1B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-9e13b9363d2692b4](../../evidence/conditions-sets-061.md#c-9e13b9363d2692b4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-057268

```text
(config)# no do-exec test ip rmap associate <string> local <cr>
```

Handler ` RVA 0xE2025D0 `；selector ` 0 `；EOL ` RVA 0x3423ADC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` rmap name to (dis)associate。

[条件 C-0d322722fb87f580](../../evidence/conditions-sets-005.md#c-0d322722fb87f580) · [参数 P-bd73181f983ba232](../../evidence/parameters-sets-014.md#p-bd73181f983ba232) · [状态效果 S-60eaef96813d30fe](../../evidence/state_effects-sets-021.md#s-60eaef96813d30fe)

### path-057102

```text
(config)# no do-exec test ip rmap batch-commit <string> <number:0..2147483647> <cr>
```

Handler ` RVA 0xE208090 `；selector ` 0 `；EOL ` RVA 0x34234C08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Specify rmapHandle；` unsigned_number ` Application: 1 - AAA。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-ab77153375655df9](../../evidence/parameters-sets-013.md#p-ab77153375655df9) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-057132

```text
(config)# no do-exec test ip rmap create <number:0..2147483647> <string> <cr>
```

Handler ` RVA 0xE202AC0 `；selector ` 0 `；EOL ` RVA 0x34234FA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Application: 1 - AAA；` string ` application specific string。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-0a14d68c1ec1aa26](../../evidence/parameters-sets-001.md#p-0a14d68c1ec1aa26) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-057220

```text
(config)# no do-exec test ip rmap delete <string> <number:0..4294967295> <cr>
```

Handler ` RVA 0xE202FB0 `；selector ` 0 `；EOL ` RVA 0x3423A5F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle。

[条件 C-23491533d0d4bfd8](../../evidence/conditions-sets-014.md#c-23491533d0d4bfd8) · [参数 P-cd3e0fed6134dbc5](../../evidence/parameters-sets-016.md#p-cd3e0fed6134dbc5) · [状态效果 S-a0dcab4fe90d3365](../../evidence/state_effects-sets-034.md#s-a0dcab4fe90d3365)

### path-060002

```text
(config)# no do-exec test ip rmap delete <string> <number:0..4294967295> match acl <string> <cr>
```

Handler ` RVA 0xE203110 `；selector ` 0 `；EOL ` RVA 0x342357B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` string ` acl name。

[条件 C-8c36b7a250ffc64c](../../evidence/conditions-sets-054.md#c-8c36b7a250ffc64c) · [参数 P-272ac774548295cd](../../evidence/parameters-sets-003.md#p-272ac774548295cd) · [状态效果 S-a0dcab4fe90d3365](../../evidence/state_effects-sets-034.md#s-a0dcab4fe90d3365)

### path-060152

```text
(config)# no do-exec test ip rmap delete <string> <number:0..4294967295> match destination tag <number:0..1000> <cr>
```

Handler ` RVA 0xE2039C0 `；selector ` 2 `；EOL ` RVA 0x34236208 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` unsigned_number ` dgt id value。

[条件 C-8c36b7a250ffc64c](../../evidence/conditions-sets-054.md#c-8c36b7a250ffc64c) · [参数 P-6d91a93fa721550c](../../evidence/parameters-sets-009.md#p-6d91a93fa721550c) · [状态效果 S-a0dcab4fe90d3365](../../evidence/state_effects-sets-034.md#s-a0dcab4fe90d3365)

### path-060146

```text
(config)# no do-exec test ip rmap delete <string> <number:0..4294967295> match length <number:0..2147483647> <number:0..2147483647> <cr>
```

Handler ` RVA 0xE2036F0 `；selector ` 0 `；EOL ` RVA 0x34235B98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` unsigned_number ` Minimum packet length；` unsigned_number ` Maximum packet length。

[条件 C-8c36b7a250ffc64c](../../evidence/conditions-sets-054.md#c-8c36b7a250ffc64c) · [参数 P-937ae3c156e0cb63](../../evidence/parameters-sets-011.md#p-937ae3c156e0cb63) · [状态效果 S-a0dcab4fe90d3365](../../evidence/state_effects-sets-034.md#s-a0dcab4fe90d3365)

### path-060149

```text
(config)# no do-exec test ip rmap delete <string> <number:0..4294967295> match source tag <number:0..1000> <cr>
```

Handler ` RVA 0xE2039C0 `；selector ` 1 `；EOL ` RVA 0x34235EC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` unsigned_number ` Security id value。

[条件 C-8c36b7a250ffc64c](../../evidence/conditions-sets-054.md#c-8c36b7a250ffc64c) · [参数 P-4ef7f2833cf942dd](../../evidence/parameters-sets-007.md#p-4ef7f2833cf942dd) · [状态效果 S-a0dcab4fe90d3365](../../evidence/state_effects-sets-034.md#s-a0dcab4fe90d3365)

### path-060015

```text
(config)# no do-exec test ip rmap delete <string> <number:0..4294967295> match vrf <string> <cr>
```

Handler ` RVA 0xE2033E0 `；selector ` 0 `；EOL ` RVA 0x342364E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` string ` VRF name。

[条件 C-8c36b7a250ffc64c](../../evidence/conditions-sets-054.md#c-8c36b7a250ffc64c) · [参数 P-7568d67122bab58a](../../evidence/parameters-sets-009.md#p-7568d67122bab58a) · [状态效果 S-a0dcab4fe90d3365](../../evidence/state_effects-sets-034.md#s-a0dcab4fe90d3365)

### path-060042

```text
(config)# no do-exec test ip rmap delete <string> <number:0..4294967295> set color red <cr>
```

Handler ` RVA 0xE203F30 `；selector ` 0 `；EOL ` RVA 0x3423A160 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle。

[条件 C-da4144df48a5bbb3](../../evidence/conditions-sets-084.md#c-da4144df48a5bbb3) · [参数 P-cd3e0fed6134dbc5](../../evidence/parameters-sets-016.md#p-cd3e0fed6134dbc5) · [状态效果 S-3b8a4542220aaaec](../../evidence/state_effects-sets-013.md#s-3b8a4542220aaaec)

### path-060020

```text
(config)# no do-exec test ip rmap delete <string> <number:0..4294967295> set def-global-nh <address> <cr>
```

Handler ` RVA 0xE205C50 `；selector ` 0 `；EOL ` RVA 0x34237A40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` address ` IP address of next-hop。

[条件 C-a9998f50032d241f](../../evidence/conditions-sets-065.md#c-a9998f50032d241f) · [参数 P-ea7c91e852d793a4](../../evidence/parameters-sets-018.md#p-ea7c91e852d793a4) · [状态效果 S-a0dcab4fe90d3365](../../evidence/state_effects-sets-034.md#s-a0dcab4fe90d3365)

### path-060028

```text
(config)# no do-exec test ip rmap delete <string> <number:0..4294967295> set def-next-hop <address> <cr>
```

Handler ` RVA 0xE2059B0 `；selector ` 0 `；EOL ` RVA 0x34238050 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` address ` IP address of default next-hop。

[条件 C-a9998f50032d241f](../../evidence/conditions-sets-065.md#c-a9998f50032d241f) · [参数 P-b3295dd415de6554](../../evidence/parameters-sets-014.md#p-b3295dd415de6554) · [状态效果 S-a0dcab4fe90d3365](../../evidence/state_effects-sets-034.md#s-a0dcab4fe90d3365)

### path-059763

```text
(config)# no do-exec test ip rmap delete <string> <number:0..4294967295> set def-nh-verify <cr>
```

Handler ` RVA 0xE205720 `；selector ` 0 `；EOL ` RVA 0x342382D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle。

[条件 C-a9998f50032d241f](../../evidence/conditions-sets-065.md#c-a9998f50032d241f) · [参数 P-cd3e0fed6134dbc5](../../evidence/parameters-sets-016.md#p-cd3e0fed6134dbc5) · [状态效果 S-a0dcab4fe90d3365](../../evidence/state_effects-sets-034.md#s-a0dcab4fe90d3365)

### path-060156

```text
(config)# no do-exec test ip rmap delete <string> <number:0..4294967295> set def-vrf-nh <string> <address> <cr>
```

Handler ` RVA 0xE205EF0 `；selector ` 0 `；EOL ` RVA 0x34237D68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` string ` VRF name；` address ` IP address of next-hop。

[条件 C-a9998f50032d241f](../../evidence/conditions-sets-065.md#c-a9998f50032d241f) · [参数 P-6835e23ae0bf3d34](../../evidence/parameters-sets-008.md#p-6835e23ae0bf3d34) · [状态效果 S-a0dcab4fe90d3365](../../evidence/state_effects-sets-034.md#s-a0dcab4fe90d3365)

### path-060037

```text
(config)# no do-exec test ip rmap delete <string> <number:0..4294967295> set df <number:0..65535> <cr>
```

Handler ` RVA 0xE204F40 `；selector ` 0 `；EOL ` RVA 0x34238BC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` unsigned_number ` Value of df。

[条件 C-a9998f50032d241f](../../evidence/conditions-sets-065.md#c-a9998f50032d241f) · [参数 P-06c275ebd6daa0a6](../../evidence/parameters-sets-001.md#p-06c275ebd6daa0a6) · [状态效果 S-a0dcab4fe90d3365](../../evidence/state_effects-sets-034.md#s-a0dcab4fe90d3365)

### path-060007

```text
(config)# no do-exec test ip rmap delete <string> <number:0..4294967295> set gateway <address> <cr>
```

Handler ` RVA 0xE206C40 `；selector ` 0 `；EOL ` RVA 0x34236890 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` address ` IP address of gateway。

[条件 C-a9998f50032d241f](../../evidence/conditions-sets-065.md#c-a9998f50032d241f) · [参数 P-e729039b021e96f0](../../evidence/parameters-sets-017.md#p-e729039b021e96f0) · [状态效果 S-a0dcab4fe90d3365](../../evidence/state_effects-sets-034.md#s-a0dcab4fe90d3365)

### path-059786

```text
(config)# no do-exec test ip rmap delete <string> <number:0..4294967295> set global <cr>
```

Handler ` RVA 0xE204CB0 `；selector ` 0 `；EOL ` RVA 0x34239130 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle。

[条件 C-a9998f50032d241f](../../evidence/conditions-sets-065.md#c-a9998f50032d241f) · [参数 P-cd3e0fed6134dbc5](../../evidence/parameters-sets-016.md#p-cd3e0fed6134dbc5) · [状态效果 S-a0dcab4fe90d3365](../../evidence/state_effects-sets-034.md#s-a0dcab4fe90d3365)

### path-060147

```text
(config)# no do-exec test ip rmap delete <string> <number:0..4294967295> set gw-vrf <string> <address> <cr>
```

Handler ` RVA 0xE206EE0 `；selector ` 0 `；EOL ` RVA 0x34236BB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` string ` VRF name；` address ` IP address of gateway。

[条件 C-a9998f50032d241f](../../evidence/conditions-sets-065.md#c-a9998f50032d241f) · [参数 P-2acbe67311ea0ecd](../../evidence/parameters-sets-004.md#p-2acbe67311ea0ecd) · [状态效果 S-a0dcab4fe90d3365](../../evidence/state_effects-sets-034.md#s-a0dcab4fe90d3365)

### path-060016

```text
(config)# no do-exec test ip rmap delete <string> <number:0..4294967295> set ip-global-nh <address> <cr>
```

Handler ` RVA 0xE2066E0 `；selector ` 0 `；EOL ` RVA 0x34237430 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` address ` IP address of next-hop。

[条件 C-a9998f50032d241f](../../evidence/conditions-sets-065.md#c-a9998f50032d241f) · [参数 P-b63ee37da7e7cdd4](../../evidence/parameters-sets-014.md#p-b63ee37da7e7cdd4) · [状态效果 S-a0dcab4fe90d3365](../../evidence/state_effects-sets-034.md#s-a0dcab4fe90d3365)

### path-060154

```text
(config)# no do-exec test ip rmap delete <string> <number:0..4294967295> set ip-vrf-nh <string> <address> <cr>
```

Handler ` RVA 0xE206980 `；selector ` 0 `；EOL ` RVA 0x34237758 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` string ` VRF name；` address ` IP address of next-hop。

[条件 C-a9998f50032d241f](../../evidence/conditions-sets-065.md#c-a9998f50032d241f) · [参数 P-ceeec3d0d198abf4](../../evidence/parameters-sets-016.md#p-ceeec3d0d198abf4) · [状态效果 S-a0dcab4fe90d3365](../../evidence/state_effects-sets-034.md#s-a0dcab4fe90d3365)

### path-060012

```text
(config)# no do-exec test ip rmap delete <string> <number:0..4294967295> set next-hop <address> <cr>
```

Handler ` RVA 0xE206440 `；selector ` 0 `；EOL ` RVA 0x34236EA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` address ` IP address of next-hop。

[条件 C-a9998f50032d241f](../../evidence/conditions-sets-065.md#c-a9998f50032d241f) · [参数 P-ac5b408e00df8dee](../../evidence/parameters-sets-013.md#p-ac5b408e00df8dee) · [状态效果 S-a0dcab4fe90d3365](../../evidence/state_effects-sets-034.md#s-a0dcab4fe90d3365)

### path-059743

```text
(config)# no do-exec test ip rmap delete <string> <number:0..4294967295> set nh-verify <cr>
```

Handler ` RVA 0xE2061B0 `；selector ` 0 `；EOL ` RVA 0x34237120 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle。

[条件 C-a9998f50032d241f](../../evidence/conditions-sets-065.md#c-a9998f50032d241f) · [参数 P-cd3e0fed6134dbc5](../../evidence/parameters-sets-016.md#p-cd3e0fed6134dbc5) · [状态效果 S-a0dcab4fe90d3365](../../evidence/state_effects-sets-034.md#s-a0dcab4fe90d3365)

### path-060034

```text
(config)# no do-exec test ip rmap delete <string> <number:0..4294967295> set precedence <number:0..65535> <cr>
```

Handler ` RVA 0xE2051E0 `；selector ` 0 `；EOL ` RVA 0x342388D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` unsigned_number ` Value of precedence。

[条件 C-a9998f50032d241f](../../evidence/conditions-sets-065.md#c-a9998f50032d241f) · [参数 P-c55c967820bd003f](../../evidence/parameters-sets-015.md#p-c55c967820bd003f) · [状态效果 S-a0dcab4fe90d3365](../../evidence/state_effects-sets-034.md#s-a0dcab4fe90d3365)

### path-060031

```text
(config)# no do-exec test ip rmap delete <string> <number:0..4294967295> set tos <number:0..65535> <cr>
```

Handler ` RVA 0xE205480 `；selector ` 0 `；EOL ` RVA 0x342385E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` unsigned_number ` Value of tos。

[条件 C-a9998f50032d241f](../../evidence/conditions-sets-065.md#c-a9998f50032d241f) · [参数 P-4dce7f6ad2f960e0](../../evidence/parameters-sets-006.md#p-4dce7f6ad2f960e0) · [状态效果 S-a0dcab4fe90d3365](../../evidence/state_effects-sets-034.md#s-a0dcab4fe90d3365)

### path-060040

```text
(config)# no do-exec test ip rmap delete <string> <number:0..4294967295> set vrf <string> <cr>
```

Handler ` RVA 0xE204A00 `；selector ` 0 `；EOL ` RVA 0x34238EB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` string ` VRF name。

[条件 C-a9998f50032d241f](../../evidence/conditions-sets-065.md#c-a9998f50032d241f) · [参数 P-e80fe2c3ff0d0f92](../../evidence/parameters-sets-017.md#p-e80fe2c3ff0d0f92) · [状态效果 S-a0dcab4fe90d3365](../../evidence/state_effects-sets-034.md#s-a0dcab4fe90d3365)

### path-057197

```text
(config)# no do-exec test ip rmap delete <string> permit <cr>
```

Handler ` RVA 0xE202DC0 `；selector ` 0 `；EOL ` RVA 0x3423A900 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` routemap tag。

[条件 C-8c36b7a250ffc64c](../../evidence/conditions-sets-054.md#c-8c36b7a250ffc64c) · [参数 P-55050655b3d5bb05](../../evidence/parameters-sets-007.md#p-55050655b3d5bb05) · [状态效果 S-52201a45635dc61b](../../evidence/state_effects-sets-018.md#s-52201a45635dc61b)

### path-052752

```text
(config)# no do-exec test ip rmap register <number:0..2147483647> <cr>
```

Handler ` RVA 0xE2028D0 `；selector ` 0 `；EOL ` RVA 0x34234888 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Application。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-7f8a93636669cf1c](../../evidence/parameters-sets-010.md#p-7f8a93636669cf1c) · [状态效果 S-669b17741bf47897](../../evidence/state_effects-sets-022.md#s-669b17741bf47897)

### path-057125

```text
(config)# no do-exec test ip rmap remove <string> <number:0..2147483647> <cr>
```

Handler ` RVA 0xE202C80 `；selector ` 0 `；EOL ` RVA 0x342352F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` application specific string；` unsigned_number ` Application: 1 - AAA。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-c35ad9aae5dc6839](../../evidence/parameters-sets-015.md#p-c35ad9aae5dc6839) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-045572

```text
(config)# no do-exec test ip subscriber enable <cr>
```

Handler ` RVA 0x11A36370 `；selector ` 0 `；EOL ` RVA 0x355CF310 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f34cff36dcdd4978](../../evidence/conditions-sets-094.md#c-f34cff36dcdd4978) · [状态效果 S-62870604ed0daa70](../../evidence/state_effects-sets-021.md#s-62870604ed0daa70)

### path-057348

```text
(config)# no do-exec test ip subscriber interface association disable <cr>
```

Handler ` RVA 0x11A362F0 `；selector ` 0 `；EOL ` RVA 0x355CF9F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-dc3a6a867e229f9b](../../evidence/conditions-sets-085.md#c-dc3a6a867e229f9b) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-057347

```text
(config)# no do-exec test ip subscriber interface association enable <cr>
```

Handler ` RVA 0x11A362F0 `；selector ` 1 `；EOL ` RVA 0x355CF740 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b60c70310e5ef397](../../evidence/conditions-sets-070.md#c-b60c70310e5ef397) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-052833

```text
(config)# no do-exec test ipam pool local alloc <cr>
```

Handler ` RVA 0xCEB79B0 `；selector ` 0 `；EOL ` RVA 0x33D1C4F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-9bcda9bfd9837237](../../evidence/conditions-sets-060.md#c-9bcda9bfd9837237) · [状态效果 S-6ab375197671890f](../../evidence/state_effects-sets-023.md#s-6ab375197671890f)

### path-054622

```text
(config)# no do-exec test ipc FC <number:1..5> <number:0..50000> <cr>
```

Handler ` RVA 0xD3C63E0 `；selector ` 0 `；EOL ` RVA 0x33E33C18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` threshold type；` unsigned_number ` Value。

[条件 C-7944f21a3b55c661](../../evidence/conditions-sets-047.md#c-7944f21a3b55c661) · [参数 P-569822aca9aeb7ed](../../evidence/parameters-sets-007.md#p-569822aca9aeb7ed) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-047790

```text
(config)# no do-exec test ipc ack-drop <number:1..10000> <cr>
```

Handler ` RVA 0xD3C6310 `；selector ` 0 `；EOL ` RVA 0x33E33138 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` state。

[条件 C-4c17065756994bdc](../../evidence/conditions-sets-030.md#c-4c17065756994bdc) · [参数 P-58b2f2cef5d5926b](../../evidence/parameters-sets-007.md#p-58b2f2cef5d5926b) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-047830

```text
(config)# no do-exec test ipc ack-pending <number:1..10000> <cr>
```

Handler ` RVA 0xD3C6260 `；selector ` 0 `；EOL ` RVA 0x33E334C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` state。

[条件 C-fb98a3674073ddea](../../evidence/conditions-sets-097.md#c-fb98a3674073ddea) · [参数 P-8a3569dabade40fa](../../evidence/parameters-sets-011.md#p-8a3569dabade40fa) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-048902

```text
(config)# no do-exec test ipc ack-timer <number:0..50000> <cr>
```

Handler ` RVA 0xD3C65C0 `；selector ` 0 `；EOL ` RVA 0x33E3B6D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Value。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [参数 P-90be1626a3d9d9fe](../../evidence/parameters-sets-011.md#p-90be1626a3d9d9fe) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-038873

```text
(config)# no do-exec test ipc api <cr>
```

Handler ` RVA 0xD3C1A60 `；selector ` 0 `；EOL ` RVA 0x33E33EB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-039540

```text
(config)# no do-exec test ipc app-send <cr>
```

Handler ` RVA 0xD3C5F70 `；selector ` 0 `；EOL ` RVA 0x33E36440 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-058326

```text
(config)# no do-exec test ipc bundle mode seat on <cr>
```

Handler ` RVA 0xD3C4B50 `；selector ` 0 `；EOL ` RVA 0x33E3B080 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [状态效果 S-67a0efdc4a5ffe65](../../evidence/state_effects-sets-022.md#s-67a0efdc4a5ffe65)

### path-058303

```text
(config)# no do-exec test ipc bundle mode session on <cr>
```

Handler ` RVA 0xD3C4A80 `；selector ` 0 `；EOL ` RVA 0x33E3AD48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [状态效果 S-31089e384cf6a090](../../evidence/state_effects-sets-011.md#s-31089e384cf6a090)

### path-059894

```text
(config)# no do-exec test ipc bundle status seat <number:0..4294967295> seat-level on <cr>
```

Handler ` RVA 0xD3C4E20 `；selector ` 0 `；EOL ` RVA 0x33E3A950 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` seat id。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [参数 P-a3276e418678fa92](../../evidence/parameters-sets-012.md#p-a3276e418678fa92) · [状态效果 S-dd061f5885c3dc7c](../../evidence/state_effects-sets-047.md#s-dd061f5885c3dc7c)

### path-059897

```text
(config)# no do-exec test ipc bundle status session <number:0..4294967295> <number:0..65535> on <cr>
```

Handler ` RVA 0xD3C4C20 `；selector ` 0 `；EOL ` RVA 0x33E3A570 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` port id；` unsigned_number ` session id 。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [参数 P-67bb089c8c087a64](../../evidence/parameters-sets-008.md#p-67bb089c8c087a64) · [状态效果 S-f8505596855650fb](../../evidence/state_effects-sets-053.md#s-f8505596855650fb)

### path-039129

```text
(config)# no do-exec test ipc callback <cr>
```

Handler ` RVA 0xD3C28E0 `；selector ` 0 `；EOL ` RVA 0x33E35280 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-039483

```text
(config)# no do-exec test ipc diag <cr>
```

Handler ` RVA 0xD3C50D0 `；selector ` 0 `；EOL ` RVA 0x33E36708 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-047876

```text
(config)# no do-exec test ipc driver stop <cr>
```

Handler ` RVA 0xD3FF9D0 `；selector ` 0 `；EOL ` RVA 0x33E41AE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-da4caf7be07414e1](../../evidence/conditions-sets-084.md#c-da4caf7be07414e1) · [状态效果 S-bb6d37d8e2b8ba74](../../evidence/state_effects-sets-040.md#s-bb6d37d8e2b8ba74)

### path-047996

```text
(config)# no do-exec test ipc drop <number:0..9999> <cr>
```

Handler ` RVA 0xD3C1990 `；selector ` 0 `；EOL ` RVA 0x33E34468 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` n: drop every nth packet sent; n=0 for no dropping。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [参数 P-95af16f3e49d885d](../../evidence/parameters-sets-011.md#p-95af16f3e49d885d) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-059427

```text
(config)# no do-exec test ipc drop ack <number:65540..4294967295> <number:0..65535> <number:0..65535> <cr>
```

Handler ` RVA 0xD3C1860 `；selector ` 0 `；EOL ` RVA 0x33E34A90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Port id；` unsigned_number ` Session id；` unsigned_number ` Number of ACKs to drop。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [参数 P-71a0b4089b1449b0](../../evidence/parameters-sets-009.md#p-71a0b4089b1449b0) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-048046

```text
(config)# no do-exec test ipc drop next <cr>
```

Handler ` RVA 0xD3C1930 `；selector ` 0 `；EOL ` RVA 0x33E34718 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-059394

```text
(config)# no do-exec test ipc mcast appclass subscribe <string> <number:0..15> <cr>
```

Handler ` RVA 0xD452370 `；selector ` 0 `；EOL ` RVA 0x33E44940 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` appclass name；` unsigned_number ` zone number。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [参数 P-43a6c12fa7a112c4](../../evidence/parameters-sets-006.md#p-43a6c12fa7a112c4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-059432

```text
(config)# no do-exec test ipc mcast group close <number:0..4294967295> <number:0..65535> <cr>
```

Handler ` RVA 0xD452A50 `；selector ` 0 `；EOL ` RVA 0x33E473E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` group id；` unsigned_number ` session id。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [参数 P-5c89ea6d871c9a6c](../../evidence/parameters-sets-007.md#p-5c89ea6d871c9a6c) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-059871

```text
(config)# no do-exec test ipc mcast group create <string> <string> <number:0..15> <cr>
```

Handler ` RVA 0xD453670 `；selector ` 0 `；EOL ` RVA 0x33E45A88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` group name；` string ` appclass name；` unsigned_number ` zone number。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [参数 P-1dc629c309feb0c9](../../evidence/parameters-sets-003.md#p-1dc629c309feb0c9) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-059419

```text
(config)# no do-exec test ipc mcast group locate <string> <number:0..15> <cr>
```

Handler ` RVA 0xD453280 `；selector ` 0 `；EOL ` RVA 0x33E46438 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` group name；` unsigned_number ` zone number。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [参数 P-acb97f54bcda4b49](../../evidence/parameters-sets-013.md#p-acb97f54bcda4b49) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-059877

```text
(config)# no do-exec test ipc mcast group member add <number:0..4294967295> <number:0..4294967295> <cr>
```

Handler ` RVA 0xD452C20 `；selector ` 0 `；EOL ` RVA 0x33E46F50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` group id；` unsigned_number ` member id。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [参数 P-7e52d3e5b9cd8270](../../evidence/parameters-sets-010.md#p-7e52d3e5b9cd8270) · [状态效果 S-7a3279e29a83481e](../../evidence/state_effects-sets-026.md#s-7a3279e29a83481e)

### path-059435

```text
(config)# no do-exec test ipc mcast group open <number:0..4294967295> <number:1..2> <cr>
```

Handler ` RVA 0xD452570 `；selector ` 0 `；EOL ` RVA 0x33E477F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` group id；` unsigned_number ` mode of group open(1. reliable 2. unreliable)。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [参数 P-64e154c7c2bb31ab](../../evidence/parameters-sets-008.md#p-64e154c7c2bb31ab) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-058131

```text
(config)# no do-exec test ipc mcast group remove <number:0..4294967295> <cr>
```

Handler ` RVA 0xD452EE0 `；selector ` 0 `；EOL ` RVA 0x33E46B40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` group id。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [参数 P-87c59ea63b268029](../../evidence/parameters-sets-010.md#p-87c59ea63b268029) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-059407

```text
(config)# no do-exec test ipc mcast group reserve <string> <number:0..15> <cr>
```

Handler ` RVA 0xD4533E0 `；selector ` 0 `；EOL ` RVA 0x33E45DD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` group name；` unsigned_number ` zone number。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [参数 P-d67325ad12ec381b](../../evidence/parameters-sets-016.md#p-d67325ad12ec381b) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-059875

```text
(config)# no do-exec test ipc mcast group subscribe <string> <string> <number:0..15> <cr>
```

Handler ` RVA 0xD453040 `；selector ` 0 `；EOL ` RVA 0x33E467F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` group name；` string ` appclass name；` unsigned_number ` zone number。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [参数 P-d154cfe91c8424b2](../../evidence/parameters-sets-016.md#p-d154cfe91c8424b2) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-059414

```text
(config)# no do-exec test ipc mcast group unreserve <string> <number:0..15> <cr>
```

Handler ` RVA 0xD453540 `；selector ` 0 `；EOL ` RVA 0x33E46108 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` group name；` unsigned_number ` zone number。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [参数 P-4cbd93331c44b6dc](../../evidence/parameters-sets-006.md#p-4cbd93331c44b6dc) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-059415

```text
(config)# no do-exec test ipc mcast platform emulation <number:0..4294967295> disable <cr>
```

Handler ` RVA 0xD453C00 `；selector ` 0 `；EOL ` RVA 0x33E45560 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` seat id。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [参数 P-59a3f025174c90ad](../../evidence/parameters-sets-007.md#p-59a3f025174c90ad) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-059408

```text
(config)# no do-exec test ipc mcast platform emulation <number:0..4294967295> enable <cr>
```

Handler ` RVA 0xD453C00 `；selector ` 1 `；EOL ` RVA 0x33E452B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` seat id。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [参数 P-59a3f025174c90ad](../../evidence/parameters-sets-007.md#p-59a3f025174c90ad) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-059399

```text
(config)# no do-exec test ipc mcast platform max-groups <number:0..15> <number:0..65535> <cr>
```

Handler ` RVA 0xD453D60 `；selector ` 0 `；EOL ` RVA 0x33E44FA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` zone number；` unsigned_number ` max group count。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [参数 P-784d9380b4381ff2](../../evidence/parameters-sets-009.md#p-784d9380b4381ff2) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-054561

```text
(config)# no do-exec test ipc mcast platform registries <cr>
```

Handler ` RVA 0xD453E30 `；selector ` 0 `；EOL ` RVA 0x33E44C50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-039316

```text
(config)# no do-exec test ipc misc <cr>
```

Handler ` RVA 0xD3C40D0 `；selector ` 0 `；EOL ` RVA 0x33E35E10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-048699

```text
(config)# no do-exec test ipc ping <number:0..4294967295> <cr>
```

Handler ` RVA 0xD3C4640 `；selector ` 0 `；EOL ` RVA 0x33E3A0A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` seat id。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [参数 P-e106634c2595c7c8](../../evidence/parameters-sets-017.md#p-e106634c2595c7c8) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-058327

```text
(config)# no do-exec test ipc port close <number:0..4294967295> <number:0..65535> <cr>
```

Handler ` RVA 0xD3C8D40 `；selector ` 0 `；EOL ` RVA 0x33E38F68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` port id；` unsigned_number ` session id 。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [参数 P-53b2dab481ba7761](../../evidence/parameters-sets-007.md#p-53b2dab481ba7761) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-058345

```text
(config)# no do-exec test ipc port create <string> <number:1..3> <cr>
```

Handler ` RVA 0xD3C7F80 `；selector ` 0 `；EOL ` RVA 0x33E37500 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` port name；` unsigned_number ` method of message reception(1. callback 2. fast callback 3. queue)。

[条件 C-9f71008f77cd3eae](../../evidence/conditions-sets-062.md#c-9f71008f77cd3eae) · [参数 P-127dda5a32adb5cf](../../evidence/parameters-sets-002.md#p-127dda5a32adb5cf) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-058388

```text
(config)# no do-exec test ipc port free <number:0..4294967295> <number:1..1000000> <cr>
```

Handler ` RVA 0xD3C8FA0 `；selector ` 0 `；EOL ` RVA 0x33E39A10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` port id；` unsigned_number ` Number of messages。

[条件 C-419d025b99e7e671](../../evidence/conditions-sets-026.md#c-419d025b99e7e671) · [参数 P-cbcec36820e3d032](../../evidence/parameters-sets-015.md#p-cbcec36820e3d032) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-060090

```text
(config)# no do-exec test ipc port msend <number:0..4294967295> <number:0..65535> <number:0..65535> <number:1..1000000> <number:1..4064> <cr>
```

Handler ` RVA 0xD3C8300 `；selector ` 0 `；EOL ` RVA 0x33E38040 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` port id；` unsigned_number ` start session id；` unsigned_number ` end session id；` unsigned_number ` number of messages to be sent；` unsigned_number ` size of message。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [参数 P-78d8a152dee698ee](../../evidence/parameters-sets-009.md#p-78d8a152dee698ee) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-055187

```text
(config)# no do-exec test ipc port notify enable <cr>
```

Handler ` RVA 0xD3C8F00 `；selector ` 0 `；EOL ` RVA 0x33E395B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [状态效果 S-6e7260cc5bb66ddd](../../evidence/state_effects-sets-023.md#s-6e7260cc5bb66ddd)

### path-058362

```text
(config)# no do-exec test ipc port open <number:0..4294967295> <number:1..3> <cr>
```

Handler ` RVA 0xD3C80F0 `；selector ` 0 `；EOL ` RVA 0x33E37A98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` port id；` unsigned_number ` mode of port open(1. reliable 2. unreliable 3. unrel-with-not)。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [参数 P-d00235038e651bbb](../../evidence/parameters-sets-016.md#p-d00235038e651bbb) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-055193

```text
(config)# no do-exec test ipc port remove <number:0..4294967295> <cr>
```

Handler ` RVA 0xD3C8DC0 `；selector ` 0 `；EOL ` RVA 0x33E392B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` port id。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [参数 P-a00f33de364d076f](../../evidence/parameters-sets-012.md#p-a00f33de364d076f) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-055246

```text
(config)# no do-exec test ipc port send header <cr>
```

Handler ` RVA 0xD3C8890 `；selector ` 0 `；EOL ` RVA 0x33E38678 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-97228be178e3388b](../../evidence/conditions-sets-058.md#c-97228be178e3388b) · [状态效果 S-de10722940f1aa36](../../evidence/state_effects-sets-047.md#s-de10722940f1aa36)

### path-039073

```text
(config)# no do-exec test ipc queue <cr>
```

Handler ` RVA 0xD3C2330 `；selector ` 0 `；EOL ` RVA 0x33E34FD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-048834

```text
(config)# no do-exec test ipc retry-period <number:0..50000> <cr>
```

Handler ` RVA 0xD3C6520 `；selector ` 0 `；EOL ` RVA 0x33E3B410 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Value。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [参数 P-8966cb03db7d6b54](../../evidence/parameters-sets-011.md#p-8966cb03db7d6b54) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-039329

```text
(config)# no do-exec test ipc rpc <cr>
```

Handler ` RVA 0xD3C1DE0 `；selector ` 0 `；EOL ` RVA 0x33E358B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-059397

```text
(config)# no do-exec test ipc ru create <string> <number:1..15> conf <cr>
```

Handler ` RVA 0xD3FEFE0 `；selector ` 0 `；EOL ` RVA 0x33E40F90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` IPC RU name；` unsigned_number ` Priority of IPC RU。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [参数 P-799b680ccf4bb802](../../evidence/parameters-sets-009.md#p-799b680ccf4bb802) · [状态效果 S-8910d1c2310de74d](../../evidence/state_effects-sets-029.md#s-8910d1c2310de74d)

### path-054593

```text
(config)# no do-exec test ipc ru remove <string> <cr>
```

Handler ` RVA 0xD3FF380 `；selector ` 0 `；EOL ` RVA 0x33E412F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` IPC RU id to be removed(in hex)。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [参数 P-d52691dd1900e41d](../../evidence/parameters-sets-016.md#p-d52691dd1900e41d) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-060081

```text
(config)# no do-exec test ipc ru tune-thresh <string> <number:1..6> rising major <number:0..10000> <cr>
```

Handler ` RVA 0xD3FF5E0 `；selector ` 0 `；EOL ` RVA 0x33E41728 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` IPC RU id(in hex) whose threshold need to be tuned；` unsigned_number ` Entity to be thresholded: 1. Tx Session Usage 2. Rx Session Usage 3. Rx Port Usage 4. RU Usage 5. Reliable Session ACK pending 6. Seat level ACK pending ；` unsigned_number ` New threshold value。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [参数 P-8d1eaef814f1e8b7](../../evidence/parameters-sets-011.md#p-8d1eaef814f1e8b7) · [状态效果 S-a1ec650b9fcad327](../../evidence/state_effects-sets-034.md#s-a1ec650b9fcad327)

### path-047875

```text
(config)# no do-exec test ipc seat-fc <number:0..1024> <cr>
```

Handler ` RVA 0xD3C61B0 `；selector ` 0 `；EOL ` RVA 0x33E33848 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` state。

[条件 C-03eba49778e23d8f](../../evidence/conditions-sets-002.md#c-03eba49778e23d8f) · [参数 P-c3cdd8e9175bec8d](../../evidence/parameters-sets-015.md#p-c3cdd8e9175bec8d) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-054990

```text
(config)# no do-exec test ipc size <number:0..100000> <number:0..1000> <cr>
```

Handler ` RVA 0xD3C3720 `；selector ` 0 `；EOL ` RVA 0x33E39DB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` IPC packet size；` unsigned_number ` Number of IPC packet。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [参数 P-646aa7c03b43ab31](../../evidence/parameters-sets-008.md#p-646aa7c03b43ab31) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-038914

```text
(config)# no do-exec test ipc slavecore <cr>
```

Handler ` RVA 0xD3C3CC0 `；selector ` 0 `；EOL ` RVA 0x33E34158 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-039023

```text
(config)# no do-exec test ipc slavelog <cr>
```

Handler ` RVA 0xD3C3D00 `；selector ` 0 `；EOL ` RVA 0x33E34D30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-039271

```text
(config)# no do-exec test ipc speed <cr>
```

Handler ` RVA 0xD3C3840 `；selector ` 0 `；EOL ` RVA 0x33E35B68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-039369

```text
(config)# no do-exec test ipc split-init <cr>
```

Handler ` RVA 0xD3C1330 `；selector ` 0 `；EOL ` RVA 0x33E360B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-039179

```text
(config)# no do-exec test ipc task-pool <cr>
```

Handler ` RVA 0xD3C2D00 `；selector ` 0 `；EOL ` RVA 0x33E35528 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-038668

```text
(config)# no do-exec test ipc toggle-mask-error <cr>
```

Handler ` RVA 0xD3FFA80 `；selector ` 0 `；EOL ` RVA 0x33E40B90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-059424

```text
(config)# no do-exec test ipc traffic <number:0..4294967295> <number:1..2147483647> <number:1..5> <number:1..50000> <cr>
```

Handler ` RVA 0xD3C5290 `；selector ` 0 `；EOL ` RVA 0x33E32570 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Destination Seat ID or Port ID；` unsigned_number ` Number of messages to be sent；` unsigned_number `  1 - Unreliable 2 - Reliable Non-blocking 3 - RPC blocking 4 - Reliable Non-Blocking and Final Blocked 5 - Reliable Blocking；` unsigned_number ` Size of each IPC message。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [参数 P-8ec07d117ce331bc](../../evidence/parameters-sets-011.md#p-8ec07d117ce331bc) · [状态效果 S-5c880a52f35cc37c](../../evidence/state_effects-sets-020.md#s-5c880a52f35cc37c)

### path-054545

```text
(config)# no do-exec test ipc traffic abort <number:0..2147483647> <cr>
```

Handler ` RVA 0xD3C5D40 `；selector ` 0 `；EOL ` RVA 0x33E32A28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` The process id which is sending the traffic。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [参数 P-116ec98253371dfa](../../evidence/parameters-sets-002.md#p-116ec98253371dfa) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-048534

```text
(config)# no do-exec test ipc watermark callback <cr>
```

Handler ` RVA 0xD3C6050 `；selector ` 0 `；EOL ` RVA 0x33E36F30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-047745

```text
(config)# no do-exec test ipc window-size <number:32..1024> <cr>
```

Handler ` RVA 0xD3C5130 `；selector ` 0 `；EOL ` RVA 0x33E32DB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` window-size。

[条件 C-0ad39be4f18f5ed7](../../evidence/conditions-sets-005.md#c-0ad39be4f18f5ed7) · [参数 P-a42b339d50af46ca](../../evidence/parameters-sets-013.md#p-a42b339d50af46ca) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-054906

```text
(config)# no do-exec test ipc zone seat2slave <number:2..15> <cr>
```

Handler ` RVA 0xD3C79C0 `；selector ` 0 `；EOL ` RVA 0x33E36A90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` zone number。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [参数 P-11ee00fec1791900](../../evidence/parameters-sets-002.md#p-11ee00fec1791900) · [状态效果 S-61833e1e00eda753](../../evidence/state_effects-sets-021.md#s-61833e1e00eda753)

### path-052826

```text
(config)# no do-exec test iphc context lifetime default <cr>
```

Handler ` RVA 0xD19AC60 `；selector ` 0 `；EOL ` RVA 0x33DA9230 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-3f776354627ad977](../../evidence/state_effects-sets-014.md#s-3f776354627ad977)

### path-053482

```text
(config)# no do-exec test ipv6 access-list common enable <cr>
```

Handler ` RVA 0x12166310 `；selector ` 0 `；EOL ` RVA 0x357B0D38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-155649a3af50aea7](../../evidence/conditions-sets-008.md#c-155649a3af50aea7) · [状态效果 S-4843637acb4a8547](../../evidence/state_effects-sets-016.md#s-4843637acb4a8547)

### path-057480

```text
(config)# no do-exec test ipv6 dhcp-client lease-query address <address> <cr>
```

Handler ` RVA 0x12189610 `；selector ` 0 `；EOL ` RVA 0x357BD0A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` IPv6 address。

[条件 C-155649a3af50aea7](../../evidence/conditions-sets-008.md#c-155649a3af50aea7) · [参数 P-486f1516edce2b17](../../evidence/parameters-sets-006.md#p-486f1516edce2b17) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-045942

```text
(config)# no do-exec test ipv6 dhcp-relay bulk-lease-query <cr>
```

Handler ` RVA 0x121AF430 `；selector ` 0 `；EOL ` RVA 0x357C3B48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-155649a3af50aea7](../../evidence/conditions-sets-008.md#c-155649a3af50aea7) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-046057

```text
(config)# no do-exec test ipv6 dhcp-relay ldra <cr>
```

Handler ` RVA 0x121AE630 `；selector ` 0 `；EOL ` RVA 0x357C3E30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-155649a3af50aea7](../../evidence/conditions-sets-008.md#c-155649a3af50aea7) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-053440

```text
(config)# no do-exec test ipv6 dhcp-server hostnum <number:0..4294967295> <cr>
```

Handler ` RVA 0x121D2540 `；selector ` 0 `；EOL ` RVA 0x357CED60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` 32 bit host number in hex。

[条件 C-155649a3af50aea7](../../evidence/conditions-sets-008.md#c-155649a3af50aea7) · [参数 P-e77823c1af7cfc82](../../evidence/parameters-sets-017.md#p-e77823c1af7cfc82) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-057543

```text
(config)# no do-exec test ipv6 nd client del <number:0..15> <cr>
```

Handler ` RVA 0x1231B440 `；selector ` 0 `；EOL ` RVA 0x357FCA70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` client id。

[条件 C-155649a3af50aea7](../../evidence/conditions-sets-008.md#c-155649a3af50aea7) · [参数 P-bd545017980207cf](../../evidence/parameters-sets-014.md#p-bd545017980207cf) · [状态效果 S-781a197b28d5dd3c](../../evidence/state_effects-sets-025.md#s-781a197b28d5dd3c)

### path-053395

```text
(config)# no do-exec test ipv6 nd pd-limit <number:0..2147483647> <cr>
```

Handler ` RVA 0x123198C0 `；selector ` 0 `；EOL ` RVA 0x357FBA50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Number of entries。

[条件 C-155649a3af50aea7](../../evidence/conditions-sets-008.md#c-155649a3af50aea7) · [参数 P-defb6b1a96e6831a](../../evidence/parameters-sets-017.md#p-defb6b1a96e6831a) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-057464

```text
(config)# no do-exec test ipv6 nd repopulate queue-size <number:1..512> <cr>
```

Handler ` RVA 0x123197B0 `；selector ` 0 `；EOL ` RVA 0x357FBD80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Queue size。

[条件 C-155649a3af50aea7](../../evidence/conditions-sets-008.md#c-155649a3af50aea7) · [参数 P-6970d6f8d867e4bf](../../evidence/parameters-sets-008.md#p-6970d6f8d867e4bf) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-045856

```text
(config)# no do-exec test ipv6 nd test-nsf <cr>
```

Handler ` RVA 0x12319920 `；selector ` 0 `；EOL ` RVA 0x357FB260 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-155649a3af50aea7](../../evidence/conditions-sets-008.md#c-155649a3af50aea7) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-053560

```text
(config)# no do-exec test ipv6 rib multicast add <cr>
```

Handler ` RVA 0x1230B6E0 `；selector ` 0 `；EOL ` RVA 0x357ECD58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-fa9eae260bcb2076](../../evidence/conditions-sets-097.md#c-fa9eae260bcb2076) · [状态效果 S-f95c9cad9414bafe](../../evidence/state_effects-sets-053.md#s-f95c9cad9414bafe)

### path-059776

```text
(config)# no do-exec test ipv6 rib pdb add <number:1..16> <number:1..255> <number:0..1> <cr>
```

Handler ` RVA 0x1230B4F0 `；selector ` 0 `；EOL ` RVA 0x357ED4E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-155649a3af50aea7](../../evidence/conditions-sets-008.md#c-155649a3af50aea7) · [参数 P-ebee9a394e927907](../../evidence/parameters-sets-018.md#p-ebee9a394e927907) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-057409

```text
(config)# no do-exec test ipv6 rib pdb del <number:1..16> <cr>
```

Handler ` RVA 0x1230B640 `；selector ` 0 `；EOL ` RVA 0x357ED140 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-155649a3af50aea7](../../evidence/conditions-sets-008.md#c-155649a3af50aea7) · [参数 P-4d58cc23e6e79a5d](../../evidence/parameters-sets-006.md#p-4d58cc23e6e79a5d) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-053230

```text
(config)# no do-exec test ipv6 rib queue start <cr>
```

Handler ` RVA 0x1230B430 `；selector ` 0 `；EOL ` RVA 0x357EC420 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-155649a3af50aea7](../../evidence/conditions-sets-008.md#c-155649a3af50aea7) · [状态效果 S-328ac5af4986e274](../../evidence/state_effects-sets-011.md#s-328ac5af4986e274)

### path-053276

```text
(config)# no do-exec test ipv6 rib suspend start <cr>
```

Handler ` RVA 0x1230B490 `；selector ` 0 `；EOL ` RVA 0x357EC780 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-155649a3af50aea7](../../evidence/conditions-sets-008.md#c-155649a3af50aea7) · [状态效果 S-cba523c20616bf59](../../evidence/state_effects-sets-043.md#s-cba523c20616bf59)

### path-057666

```text
(config)# no do-exec test ipv6 rmap associate <string> local <cr>
```

Handler ` RVA 0x118C0490 `；selector ` 0 `；EOL ` RVA 0x3559F648 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` rmap name to (dis)associate。

[条件 C-dce18dac73d2d613](../../evidence/conditions-sets-085.md#c-dce18dac73d2d613) · [参数 P-ea229d8e07f52d10](../../evidence/parameters-sets-018.md#p-ea229d8e07f52d10) · [状态效果 S-3acd9eaae2b8fd31](../../evidence/state_effects-sets-013.md#s-3acd9eaae2b8fd31)

### path-057541

```text
(config)# no do-exec test ipv6 rmap create <number:1..7> <string> <cr>
```

Handler ` RVA 0xE202AC0 `；selector ` 0 `；EOL ` RVA 0x3559CF80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Application: 1 - AAA；` string ` application specific string。

[条件 C-155649a3af50aea7](../../evidence/conditions-sets-008.md#c-155649a3af50aea7) · [参数 P-700266de357f47fd](../../evidence/parameters-sets-009.md#p-700266de357f47fd) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-057678

```text
(config)# no do-exec test ipv6 rmap delete <string> <number:0..4294967295> <cr>
```

Handler ` RVA 0xE202FB0 `；selector ` 0 `；EOL ` RVA 0x3559EEE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle。

[条件 C-3da3f7c7f476935d](../../evidence/conditions-sets-024.md#c-3da3f7c7f476935d) · [参数 P-e1f9c2e256f45292](../../evidence/parameters-sets-017.md#p-e1f9c2e256f45292) · [状态效果 S-63ed81fa443b530b](../../evidence/state_effects-sets-021.md#s-63ed81fa443b530b)

### path-060044

```text
(config)# no do-exec test ipv6 rmap delete <string> <number:0..4294967295> match acl <string> <cr>
```

Handler ` RVA 0x118BCAF0 `；selector ` 0 `；EOL ` RVA 0x3559D768 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` string ` acl name。

[条件 C-54893d9a658412db](../../evidence/conditions-sets-033.md#c-54893d9a658412db) · [参数 P-131b5c4417a1f1af](../../evidence/parameters-sets-002.md#p-131b5c4417a1f1af) · [状态效果 S-63ed81fa443b530b](../../evidence/state_effects-sets-021.md#s-63ed81fa443b530b)

### path-060167

```text
(config)# no do-exec test ipv6 rmap delete <string> <number:0..4294967295> match length <number:0..2147483647> <number:0..2147483647> <cr>
```

Handler ` RVA 0xE2036F0 `；selector ` 0 `；EOL ` RVA 0x3559DA70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` unsigned_number ` Minimum packet length；` unsigned_number ` Maximum packet length。

[条件 C-54893d9a658412db](../../evidence/conditions-sets-033.md#c-54893d9a658412db) · [参数 P-43c97c6f77edf50d](../../evidence/parameters-sets-006.md#p-43c97c6f77edf50d) · [状态效果 S-63ed81fa443b530b](../../evidence/state_effects-sets-021.md#s-63ed81fa443b530b)

### path-059825

```text
(config)# no do-exec test ipv6 rmap delete <string> <number:0..4294967295> set global <cr>
```

Handler ` RVA 0xE204CB0 `；selector ` 0 `；EOL ` RVA 0x3559E720 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle。

[条件 C-cab10ed150ee7567](../../evidence/conditions-sets-078.md#c-cab10ed150ee7567) · [参数 P-e1f9c2e256f45292](../../evidence/parameters-sets-017.md#p-e1f9c2e256f45292) · [状态效果 S-63ed81fa443b530b](../../evidence/state_effects-sets-021.md#s-63ed81fa443b530b)

### path-060051

```text
(config)# no do-exec test ipv6 rmap delete <string> <number:0..4294967295> set next-hop <address> <cr>
```

Handler ` RVA 0x118BCDA0 `；selector ` 0 `；EOL ` RVA 0x3559DE00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` address ` IPv6 address of next-hop。

[条件 C-d2283e6ae4fff89a](../../evidence/conditions-sets-081.md#c-d2283e6ae4fff89a) · [参数 P-9c64443c07b0a179](../../evidence/parameters-sets-012.md#p-9c64443c07b0a179) · [状态效果 S-e17fbf16e7ba2513](../../evidence/state_effects-sets-048.md#s-e17fbf16e7ba2513)

### path-060055

```text
(config)# no do-exec test ipv6 rmap delete <string> <number:0..4294967295> set precedence <number:0..7> <cr>
```

Handler ` RVA 0x118BD130 `；selector ` 0 `；EOL ` RVA 0x3559E1B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` unsigned_number ` Value of precedence。

[条件 C-cab10ed150ee7567](../../evidence/conditions-sets-078.md#c-cab10ed150ee7567) · [参数 P-ce115e51ed785080](../../evidence/parameters-sets-016.md#p-ce115e51ed785080) · [状态效果 S-63ed81fa443b530b](../../evidence/state_effects-sets-021.md#s-63ed81fa443b530b)

### path-060060

```text
(config)# no do-exec test ipv6 rmap delete <string> <number:0..4294967295> set vrf <string> <cr>
```

Handler ` RVA 0xE204A00 `；selector ` 0 `；EOL ` RVA 0x3559E4A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` string ` VRF name。

[条件 C-cab10ed150ee7567](../../evidence/conditions-sets-078.md#c-cab10ed150ee7567) · [参数 P-0f25ae5261c5ab19](../../evidence/parameters-sets-002.md#p-0f25ae5261c5ab19) · [状态效果 S-63ed81fa443b530b](../../evidence/state_effects-sets-021.md#s-63ed81fa443b530b)

### path-057624

```text
(config)# no do-exec test ipv6 rmap delete <string> permit <cr>
```

Handler ` RVA 0xE202DC0 `；selector ` 0 `；EOL ` RVA 0x3559F180 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` routemap tag。

[条件 C-54893d9a658412db](../../evidence/conditions-sets-033.md#c-54893d9a658412db) · [参数 P-afea805b9cc43465](../../evidence/parameters-sets-013.md#p-afea805b9cc43465) · [状态效果 S-f99cea2292292ffa](../../evidence/state_effects-sets-053.md#s-f99cea2292292ffa)

### path-053516

```text
(config)# no do-exec test ipv6 rmap register <number:1..7> <cr>
```

Handler ` RVA 0xE2028D0 `；selector ` 0 `；EOL ` RVA 0x3559CBF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Application。

[条件 C-155649a3af50aea7](../../evidence/conditions-sets-008.md#c-155649a3af50aea7) · [参数 P-ffc4586fce516f90](../../evidence/parameters-sets-019.md#p-ffc4586fce516f90) · [状态效果 S-130bed2effe81735](../../evidence/state_effects-sets-004.md#s-130bed2effe81735)

### path-057562

```text
(config)# no do-exec test ipv6 rmap remove <string> <number:1..7> <cr>
```

Handler ` RVA 0xE202C80 `；selector ` 0 `；EOL ` RVA 0x3559D2A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` application specific string；` unsigned_number ` Application: 1 - AAA。

[条件 C-155649a3af50aea7](../../evidence/conditions-sets-008.md#c-155649a3af50aea7) · [参数 P-6ee64968fd4901d6](../../evidence/parameters-sets-009.md#p-6ee64968fd4901d6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-053316

```text
(config)# no do-exec test ipv6 static limit <number:0..32> <cr>
```

Handler ` RVA 0x12310D00 `；selector ` 0 `；EOL ` RVA 0x357F0F90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-155649a3af50aea7](../../evidence/conditions-sets-008.md#c-155649a3af50aea7) · [参数 P-f007846cc54b8f35](../../evidence/parameters-sets-018.md#p-f007846cc54b8f35) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-045785

```text
(config)# no do-exec test ipv6 static policy <cr>
```

Handler ` RVA 0x12310CC0 `；selector ` 0 `；EOL ` RVA 0x357F0CA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-155649a3af50aea7](../../evidence/conditions-sets-008.md#c-155649a3af50aea7) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-047125

```text
(config)# no do-exec test isis case <number:0..4294967295> <cr>
```

Handler ` RVA 0x10743F90 `；selector ` 4 `；EOL ` RVA 0x34B9ACE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` test number。

[条件 C-ff6e6c05c47f5f01](../../evidence/conditions-sets-098.md#c-ff6e6c05c47f5f01) · [参数 P-648cc8ff7d755148](../../evidence/parameters-sets-008.md#p-648cc8ff7d755148) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-046909

```text
(config)# no do-exec test isis clear counters <cr>
```

Handler ` RVA 0x10743F90 `；selector ` 5 `；EOL ` RVA 0x34B792E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-037427

```text
(config)# no do-exec test isis debug <cr>
```

Handler ` RVA 0x10743F90 `；selector ` 0 `；EOL ` RVA 0x34B78708 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-046927

```text
(config)# no do-exec test isis ip address <cr>
```

Handler ` RVA 0x10743F90 `；selector ` 3 `；EOL ` RVA 0x34B78F58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-057937

```text
(config)# no do-exec test isis lsp advertise lan-adj-sid <number:1..255> <cr>
```

Handler ` RVA 0x10743F90 `；selector ` 15 `；EOL ` RVA 0x34B9B8A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` number of items。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-555260a8b81f290e](../../evidence/parameters-sets-007.md#p-555260a8b81f290e) · [状态效果 S-c80540277f65c8dc](../../evidence/state_effects-sets-042.md#s-c80540277f65c8dc)

### path-047283

```text
(config)# no do-exec test isis lsp build <cr>
```

Handler ` RVA 0x10743F90 `；selector ` 8 `；EOL ` RVA 0x34B9C870 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-047118

```text
(config)# no do-exec test isis lsp id <cr>
```

Handler ` RVA 0x10743F90 `；selector ` 1 `；EOL ` RVA 0x34B9B520 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-054345

```text
(config)# no do-exec test isis lsp non_pn_delay on <cr>
```

Handler ` RVA 0x10743F90 `；selector ` 13 `；EOL ` RVA 0x34B9C4E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-02d8031c6a6be4de](../../evidence/state_effects-sets-001.md#s-02d8031c6a6be4de)

### path-054336

```text
(config)# no do-exec test isis lsp pn_delay on <cr>
```

Handler ` RVA 0x10743F90 `；selector ` 12 `；EOL ` RVA 0x34B9C188 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-26c8d35edf240c75](../../evidence/state_effects-sets-009.md#s-26c8d35edf240c75)

### path-047352

```text
(config)# no do-exec test isis lsp purge <cr>
```

Handler ` RVA 0x10743F90 `；selector ` 9 `；EOL ` RVA 0x34B9D118 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-054414

```text
(config)# no do-exec test isis lsp purge dr <cr>
```

Handler ` RVA 0x10743F90 `；selector ` 10 `；EOL ` RVA 0x34B9CC98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-047208

```text
(config)# no do-exec test isis lsp refresh <cr>
```

Handler ` RVA 0x10743F90 `；selector ` 11 `；EOL ` RVA 0x34B9BCF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-037462

```text
(config)# no do-exec test isis nsap <cr>
```

Handler ` RVA 0x10743F90 `；selector ` 2 `；EOL ` RVA 0x34B78BF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-046940

```text
(config)# no do-exec test isis show counters <cr>
```

Handler ` RVA 0x10743F90 `；selector ` 6 `；EOL ` RVA 0x34B795E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-037724

```text
(config)# no do-exec test isis spf <cr>
```

Handler ` RVA 0x10743F90 `；selector ` 7 `；EOL ` RVA 0x34B9B0D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-046966

```text
(config)# no do-exec test isis telemetry enable <cr>
```

Handler ` RVA 0x10743F90 `；selector ` 21 `；EOL ` RVA 0x34B798B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-4cbf284c2fd20409](../../evidence/state_effects-sets-017.md#s-4cbf284c2fd20409)

### path-059649

```text
(config)# no do-exec test issu capability entry register <number:1..4294967295> <number:0..100> <string> <cr>
```

Handler ` RVA 0xD4C7970 `；selector ` 0 `；EOL ` RVA 0x33E62D08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` entity id；` unsigned_number ` cap entry id；` string ` Cap Type list ex: 1,3,4 - Comma needed。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-b7aee89a0684739a](../../evidence/parameters-sets-014.md#p-b7aee89a0684739a) · [状态效果 S-1fc57913f2be74c8](../../evidence/state_effects-sets-007.md#s-1fc57913f2be74c8)

### path-059963

```text
(config)# no do-exec test issu capability group register <number:1..4294967295> <number:1..100> <number:0..1> <string> <cr>
```

Handler ` RVA 0xD4C7970 `；selector ` 0 `；EOL ` RVA 0x33E63100 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` entity id；` unsigned_number ` cap group id；` unsigned_number ` no_mandatory_entry 1=TRUE, 0=FALSE；` string ` Cap entry list ex: 1,3,4 - Comma needed。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-edb3c0f496cab6b9](../../evidence/parameters-sets-018.md#p-edb3c0f496cab6b9) · [状态效果 S-8f10ba3e88bc1f09](../../evidence/state_effects-sets-030.md#s-8f10ba3e88bc1f09)

### path-058937

```text
(config)# no do-exec test issu capability type-list register <number:1..4294967295> <string> <cr>
```

Handler ` RVA 0xD4C7970 `；selector ` 0 `；EOL ` RVA 0x33E62930 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` entity id；` string ` Cap Type list ex: 1,3,4 - Comma needed。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-369daa5871e461d5](../../evidence/parameters-sets-005.md#p-369daa5871e461d5) · [状态效果 S-946d7a9de5e4a17f](../../evidence/state_effects-sets-031.md#s-946d7a9de5e4a17f)

### path-056866

```text
(config)# no do-exec test issu client <number:1..9999> bits enable <cr>
```

Handler ` RVA 0xD4C7970 `；selector ` 0 `；EOL ` RVA 0x33E61080 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` client id。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-3ef334e0ec790657](../../evidence/parameters-sets-005.md#p-3ef334e0ec790657) · [状态效果 S-e07683435e71e92f](../../evidence/state_effects-sets-048.md#s-e07683435e71e92f)

### path-044310

```text
(config)# no do-exec test issu client register <cr>
```

Handler ` RVA 0xD4C7970 `；selector ` 0 `；EOL ` RVA 0x33E61478 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-9372de8a0a87dccf](../../evidence/state_effects-sets-031.md#s-9372de8a0a87dccf)

### path-044200

```text
(config)# no do-exec test issu distributed show <cr>
```

Handler ` RVA 0xD4C7970 `；selector ` 0 `；EOL ` RVA 0x33E60B18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-8974f6118dd09dc6](../../evidence/state_effects-sets-029.md#s-8974f6118dd09dc6)

### path-044710

```text
(config)# no do-exec test issu divc no-test <cr>
```

Handler ` RVA 0xD4BFE40 `；selector ` 0 `；EOL ` RVA 0x33E66EA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-d6fc001f6c32ea63](../../evidence/state_effects-sets-046.md#s-d6fc001f6c32ea63)

### path-052318

```text
(config)# no do-exec test issu entity register <number:0..4294967295> <cr>
```

Handler ` RVA 0xD4C7970 `；selector ` 0 `；EOL ` RVA 0x33E618C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` entity id。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-a8d135807cc9287b](../../evidence/parameters-sets-013.md#p-a8d135807cc9287b) · [状态效果 S-f9113df92a124efb](../../evidence/state_effects-sets-053.md#s-f9113df92a124efb)

### path-058985

```text
(config)# no do-exec test issu injected calc_mtu <number:0..4294967295> <number:1..100> <number:1..100> <cr>
```

Handler ` RVA 0xD4BFC10 `；selector ` 0 `；EOL ` RVA 0x33E65928 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` session id；` unsigned_number ` message type；` unsigned_number ` negotiated version。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-853668705988955a](../../evidence/parameters-sets-010.md#p-853668705988955a) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-056957

```text
(config)# no do-exec test issu injected capability <number:0..4294967295> <number:1..100> <cr>
```

Handler ` RVA 0xD4BFCF0 `；selector ` 0 `；EOL ` RVA 0x33E65298 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` session id；` unsigned_number ` capability entry id。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-393798d128e2709a](../../evidence/parameters-sets-005.md#p-393798d128e2709a) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-056971

```text
(config)# no do-exec test issu injected comp_result <number:0..4294967295> <number:1..2> <cr>
```

Handler ` RVA 0xD4BFC80 `；selector ` 0 `；EOL ` RVA 0x33E655D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` session id；` unsigned_number ` compatible result。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-6361eb3e9623ecfb](../../evidence/parameters-sets-008.md#p-6361eb3e9623ecfb) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-059666

```text
(config)# no do-exec test issu injected message <number:0..4294967295> <number:1..100> <number:1..100> <number:1..100> <cr>
```

Handler ` RVA 0xD4BFD60 `；selector ` 0 `；EOL ` RVA 0x33E64F60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` session id；` unsigned_number ` message type；` unsigned_number ` negotiated version；` unsigned_number ` message mtu。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-7510cad559f30d36](../../evidence/parameters-sets-009.md#p-7510cad559f30d36) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-052409

```text
(config)# no do-exec test issu injected register <number:0..4294967295> <cr>
```

Handler ` RVA 0xD4BFDE0 `；selector ` 0 `；EOL ` RVA 0x33E64B98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` session id。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-0084d67a308f4e0e](../../evidence/parameters-sets-001.md#p-0084d67a308f4e0e) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-052376

```text
(config)# no do-exec test issu lossless session setup <cr>
```

Handler ` RVA 0xD4BF540 `；selector ` 0 `；EOL ` RVA 0x33E634F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-61cdbfb0512135b5](../../evidence/state_effects-sets-021.md#s-61cdbfb0512135b5)

### path-059645

```text
(config)# no do-exec test issu message group register <number:1..4294967295> <number:1..100> <string> <cr>
```

Handler ` RVA 0xD4C7970 `；selector ` 0 `；EOL ` RVA 0x33E62520 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` entity id；` unsigned_number ` msg group id；` string ` msg type list ex: 1,2,3 - Comma needed。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-5853af0f9184149a](../../evidence/parameters-sets-007.md#p-5853af0f9184149a) · [状态效果 S-30d569dfdb4a66db](../../evidence/state_effects-sets-011.md#s-30d569dfdb4a66db)

### path-059956

```text
(config)# no do-exec test issu message type register <number:1..4294967295> <number:1..100> <number:1..5> <number:1..5> <cr>
```

Handler ` RVA 0xD4BF240 `；selector ` 0 `；EOL ` RVA 0x33E61F30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` entity id；` unsigned_number ` msg type；` unsigned_number ` low ver；` unsigned_number ` hi ver。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-c8d4fce5568ed841](../../evidence/parameters-sets-015.md#p-c8d4fce5568ed841) · [状态效果 S-89a984663b1ccd98](../../evidence/state_effects-sets-029.md#s-89a984663b1ccd98)

### path-060125

```text
(config)# no do-exec test issu message type register <number:1..4294967295> <number:1..100> <number:1..5> <number:1..5> <string> <cr>
```

Handler ` RVA 0xD4BF1A0 `；selector ` 0 `；EOL ` RVA 0x33E61F08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` entity id；` unsigned_number ` msg type；` unsigned_number ` low ver；` unsigned_number ` hi ver；` string ` dummy version list, ex: 2,3,5 - Comma needed。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-5787eb47f94b9f1d](../../evidence/parameters-sets-007.md#p-5787eb47f94b9f1d) · [状态效果 S-89a984663b1ccd98](../../evidence/state_effects-sets-029.md#s-89a984663b1ccd98)

### path-044565

```text
(config)# no do-exec test issu negative on <cr>
```

Handler ` RVA 0xD4C7970 `；selector ` 0 `；EOL ` RVA 0x33E66700 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-d0d1bc24c49d84cb](../../evidence/state_effects-sets-044.md#s-d0d1bc24c49d84cb)

### path-058974

```text
(config)# no do-exec test issu nego-version config <number:1..4294967295> <number:1..100> <number:1..100> <cr>
```

Handler ` RVA 0xD4BF6C0 `；selector ` 0 `；EOL ` RVA 0x33E66400 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` session id；` unsigned_number ` Msg Type；` unsigned_number ` new negotiated version。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-84abe38d8cd95294](../../evidence/parameters-sets-010.md#p-84abe38d8cd95294) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-052438

```text
(config)# no do-exec test issu negotiate <number:1..4294967295> <number:0..1> <cr>
```

Handler ` RVA 0xD4C7970 `；selector ` 0 `；EOL ` RVA 0x33E65CB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` session id；` unsigned_number ` domain id。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-e3a16036306ccf7a](../../evidence/parameters-sets-017.md#p-e3a16036306ccf7a) · [状态效果 S-a3203e1db3dc328f](../../evidence/state_effects-sets-035.md#s-a3203e1db3dc328f)

### path-044648

```text
(config)# no do-exec test issu policy off <cr>
```

Handler ` RVA 0xD4C7970 `；selector ` 0 `；EOL ` RVA 0x33E66AD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-55fa661136e58934](../../evidence/state_effects-sets-019.md#s-55fa661136e58934)

### path-044494

```text
(config)# no do-exec test issu session ipc <cr>
```

Handler ` RVA 0xD4C7970 `；selector ` 0 `；EOL ` RVA 0x33E63998 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-859c9905873b9c0d](../../evidence/state_effects-sets-028.md#s-859c9905873b9c0d)

### path-058956

```text
(config)# no do-exec test issu shared message_session unregister <number:1..4294967295> <number:0..1> <cr>
```

Handler ` RVA 0xD4BFA00 `；selector ` 0 `；EOL ` RVA 0x33E64010 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` session id；` unsigned_number ` domain id。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-15f9d1914836288c](../../evidence/parameters-sets-002.md#p-15f9d1914836288c) · [状态效果 S-5535a02ce8df0d6f](../../evidence/state_effects-sets-018.md#s-5535a02ce8df0d6f)

### path-052460

```text
(config)# no do-exec test issu shared nego_session register <cr>
```

Handler ` RVA 0xD4BFB40 `；selector ` 0 `；EOL ` RVA 0x33E64428 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-b651674f342a0a15](../../evidence/state_effects-sets-039.md#s-b651674f342a0a15)

### path-058961

```text
(config)# no do-exec test issu shared negotiate <number:1..4294967295> <number:1..4294967295> <number:0..1> <cr>
```

Handler ` RVA 0xD4BF7A0 `；selector ` 0 `；EOL ` RVA 0x33E64818 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number `  message session id；` unsigned_number `  negotiation session id；` unsigned_number ` domain id。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-002060df6e92087d](../../evidence/parameters-sets-001.md#p-002060df6e92087d) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-056954

```text
(config)# no do-exec test issu transform <number:1..4294967295> <number:1..100> <number:0..1> <cr>
```

Handler ` RVA 0xD4C7970 `；selector ` 0 `；EOL ` RVA 0x33E66040 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` session id；` unsigned_number ` Msg Type；` unsigned_number ` domain id。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-5bac2e1d7c4c7095](../../evidence/parameters-sets-007.md#p-5bac2e1d7c4c7095) · [状态效果 S-c48ecf2eace89134](../../evidence/state_effects-sets-042.md#s-c48ecf2eace89134)

### path-031812

```text
(config)# no do-exec test l2protocol-forward <cr>
```

Handler ` RVA 0x15FD9700 `；selector ` 32 `；EOL ` RVA 0x35E87788 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-aeee0c70d98a45eb](../../evidence/conditions-sets-068.md#c-aeee0c70d98a45eb) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-031792

```text
(config)# no do-exec test l2protocol-tunnel <cr>
```

Handler ` RVA 0x15FD9700 `；selector ` 31 `；EOL ` RVA 0x35E871A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ddbd1287a634e214](../../evidence/conditions-sets-085.md#c-ddbd1287a634e214) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-048979

```text
(config)# no do-exec test lacp disable insert-seq-num <cr>
```

Handler ` RVA 0xC8D36F0 `；selector ` 0 `；EOL ` RVA 0x33B15208 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-fdf2f17d455a7673](../../evidence/state_effects-sets-054.md#s-fdf2f17d455a7673)

### path-048906

```text
(config)# no do-exec test lacp disable recv <cr>
```

Handler ` RVA 0xC8D3680 `；selector ` 0 `；EOL ` RVA 0x33B14F60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-fdf2f17d455a7673](../../evidence/state_effects-sets-054.md#s-fdf2f17d455a7673)

### path-048824

```text
(config)# no do-exec test lacp disable send <cr>
```

Handler ` RVA 0xC8D3610 `；selector ` 0 `；EOL ` RVA 0x33B14CB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-fdf2f17d455a7673](../../evidence/state_effects-sets-054.md#s-fdf2f17d455a7673)

### path-049044

```text
(config)# no do-exec test lacp enable insert-seq-num <cr>
```

Handler ` RVA 0xC8D36F0 `；selector ` 0 `；EOL ` RVA 0x33B15A78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-080e78e97db1ba02](../../evidence/state_effects-sets-002.md#s-080e78e97db1ba02)

### path-048977

```text
(config)# no do-exec test lacp enable recv <cr>
```

Handler ` RVA 0xC8D3680 `；selector ` 0 `；EOL ` RVA 0x33B157D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-080e78e97db1ba02](../../evidence/state_effects-sets-002.md#s-080e78e97db1ba02)

### path-048895

```text
(config)# no do-exec test lacp enable send <cr>
```

Handler ` RVA 0xC8D3610 `；selector ` 0 `；EOL ` RVA 0x33B15528 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-080e78e97db1ba02](../../evidence/state_effects-sets-002.md#s-080e78e97db1ba02)

### path-055136

```text
(config)# no do-exec test lacp multi-chassis iccp-version <number:0..65535> <cr>
```

Handler ` RVA 0xC960530 `；selector ` 0 `；EOL ` RVA 0x33B38290 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Version in ICCP connection TLV。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-1fc392fcc1ad0e26](../../evidence/parameters-sets-003.md#p-1fc392fcc1ad0e26) · [状态效果 S-c0945d31a9d45fb4](../../evidence/state_effects-sets-041.md#s-c0945d31a9d45fb4)

### path-058347

```text
(config)# no do-exec test lacp timer wait fast default <cr>
```

Handler ` RVA 0xC8D32D0 `；selector ` 0 `；EOL ` RVA 0x33B166F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-00c3762a918bacec](../../evidence/state_effects-sets-001.md#s-00c3762a918bacec)

### path-044964

```text
(config)# no do-exec test license smart tech-support <cr>
```

Handler ` RVA 0xBB47540 `；selector ` 0 `；EOL ` RVA 0x33856CA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-df6437d35f0df1cc](../../evidence/conditions-sets-086.md#c-df6437d35f0df1cc) · [状态效果 S-0f58d8a4095838b4](../../evidence/state_effects-sets-004.md#s-0f58d8a4095838b4)

### path-044673

```text
(config)# no do-exec test lim proximity-db enable <cr>
```

Handler ` RVA 0xC9242D0 `；selector ` 1 `；EOL ` RVA 0x33B1E4A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0875a4850114d37f](../../evidence/conditions-sets-004.md#c-0875a4850114d37f) · [状态效果 S-1e2d852f4b50bef0](../../evidence/state_effects-sets-007.md#s-1e2d852f4b50bef0)

### path-060201

```text
(config)# no do-exec test mdns browse regtype <string> domain <string> periodicity <number:0..4294967295> interface <number:0..4294967295> <cr>
```

Handler ` RVA 0x142AA8B0 `；selector ` 0 `；EOL ` RVA 0x35D12E90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Specify in this form _servicename._protocol；` string ` Specify Domain or 0 for NULL；` unsigned_number ` Specify Periodicity in seconds；` unsigned_number ` Specify interface Index。

[条件 C-e6b11f3ca6b60f83](../../evidence/conditions-sets-089.md#c-e6b11f3ca6b60f83) · [参数 P-a5635059931d6d21](../../evidence/parameters-sets-013.md#p-a5635059931d6d21) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-053517

```text
(config)# no do-exec test mdns browse stop <number:1..4294967295> <cr>
```

Handler ` RVA 0x142AA9D0 `；selector ` 0 `；EOL ` RVA 0x35D13180 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Enter Request ID value。

[条件 C-7e3902f9c0bef28a](../../evidence/conditions-sets-049.md#c-7e3902f9c0bef28a) · [参数 P-f5e43b71021fa86d](../../evidence/parameters-sets-018.md#p-f5e43b71021fa86d) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-036998

```text
(config)# no do-exec test mdns cache <cr>
```

Handler ` RVA 0x142ABBE0 `；selector ` 1 `；EOL ` RVA 0x35D14068 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-bb76b8eb5b0cf5dd](../../evidence/conditions-sets-072.md#c-bb76b8eb5b0cf5dd) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-059209

```text
(config)# no do-exec test mdns resolve host <string> interface <number:0..4294967295> <cr>
```

Handler ` RVA 0x142AAC10 `；selector ` 0 `；EOL ` RVA 0x35D13A58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Specify HostName to Resolve；` unsigned_number ` Specify Interface Index。

[条件 C-c62e197fc7d0055f](../../evidence/conditions-sets-076.md#c-c62e197fc7d0055f) · [参数 P-0467657afa55ba03](../../evidence/parameters-sets-001.md#p-0467657afa55ba03) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-060203

```text
(config)# no do-exec test mdns resolve service <string> regtype <string> domain <string> interface <number:0..4294967295> <cr>
```

Handler ` RVA 0x142AAAF0 `；selector ` 0 `；EOL ` RVA 0x35D13670 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Service Instance Name；` string ` Specify in this form _servicename._protocol；` string ` Specify Domain name or 0 for NULL；` unsigned_number ` Specify Interface Index。

[条件 C-0c6cade41cd725aa](../../evidence/conditions-sets-005.md#c-0c6cade41cd725aa) · [参数 P-7a2f34b5b2da854f](../../evidence/parameters-sets-010.md#p-7a2f34b5b2da854f) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-036422

```text
(config)# no do-exec test mdns resync <cr>
```

Handler ` RVA 0x142AC590 `；selector ` 9 `；EOL ` RVA 0x35D12098 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-3f52af221f1d2920](../../evidence/conditions-sets-025.md#c-3f52af221f1d2920) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-045781

```text
(config)# no do-exec test mdns srv-enum <number:0..1> <cr>
```

Handler ` RVA 0x142AC590 `；selector ` 11 `；EOL ` RVA 0x35D11E10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Enter 0 for clear and 1 for request。

[条件 C-6c2e6f89a5ff3c4e](../../evidence/conditions-sets-042.md#c-6c2e6f89a5ff3c4e) · [参数 P-79203c4ca1832bbb](../../evidence/parameters-sets-009.md#p-79203c4ca1832bbb) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-036546

```text
(config)# no do-exec test mdns start <cr>
```

Handler ` RVA 0x142AC590 `；selector ` 0 `；EOL ` RVA 0x35D126E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1e602975eaca0eb1](../../evidence/conditions-sets-012.md#c-1e602975eaca0eb1) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-036600

```text
(config)# no do-exec test mdns stop <cr>
```

Handler ` RVA 0x142AC590 `；selector ` 1 `；EOL ` RVA 0x35D12990 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f39ee03118cf0b29](../../evidence/conditions-sets-094.md#c-f39ee03118cf0b29) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-059203

```text
(config)# no do-exec test mdns update bssid <address> client-mac <address> <cr>
```

Handler ` RVA 0x142ABAD0 `；selector ` 1 `；EOL ` RVA 0x35D14590 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` 48 bit mac address；` address ` 48 bit mac address。

[条件 C-fbff4f7f4bec12be](../../evidence/conditions-sets-097.md#c-fbff4f7f4bec12be) · [参数 P-54086fa71b463a2f](../../evidence/parameters-sets-007.md#p-54086fa71b463a2f) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-057559

```text
(config)# no do-exec test mdns update query-pak bssid-mac <address> <cr>
```

Handler ` RVA 0x142ABA60 `；selector ` 1 `；EOL ` RVA 0x35D148A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` 48 bit mac address。

[条件 C-5715c0ac941bb7e4](../../evidence/conditions-sets-034.md#c-5715c0ac941bb7e4) · [参数 P-cb5e5912b30e3de5](../../evidence/parameters-sets-015.md#p-cb5e5912b30e3de5) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-028562

```text
(config)# no do-exec test memory <cr>
```

Handler ` RVA 0xE8F44F0 `；selector ` 0 `；EOL ` RVA 0x3433F0E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-687391d529d2b295](../../evidence/conditions-sets-040.md#c-687391d529d2b295) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-059001

```text
(config)# no do-exec test memory allocate processor <number:0..4294967294> <number:0..4294967294> <number:0..4294967294> <cr>
```

Handler ` RVA 0xD79CC10 `；selector ` 0 `；EOL ` RVA 0x33EE8290 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` alignment；` unsigned_number ` number of allocations；` unsigned_number ` size of each allocated block。

[条件 C-687391d529d2b295](../../evidence/conditions-sets-040.md#c-687391d529d2b295) · [参数 P-493f9cb9de8c2f52](../../evidence/parameters-sets-006.md#p-493f9cb9de8c2f52) · [状态效果 S-0b1cffd7f7272d1e](../../evidence/state_effects-sets-003.md#s-0b1cffd7f7272d1e)

### path-044607

```text
(config)# no do-exec test memory create dangling-reference <cr>
```

Handler ` RVA 0xD79C2F0 `；selector ` 0 `；EOL ` RVA 0x33EE8D28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-687391d529d2b295](../../evidence/conditions-sets-040.md#c-687391d529d2b295) · [状态效果 S-007cfd9d04bdb2ef](../../evidence/state_effects-sets-001.md#s-007cfd9d04bdb2ef)

### path-059017

```text
(config)# no do-exec test memory create leak type1 <number:28..4294967295> <number:1..4294967295> <cr>
```

Handler ` RVA 0xD79C5D0 `；selector ` 0 `；EOL ` RVA 0x33EE9470 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` size of blocks to leak；` unsigned_number ` number of blocks to leak。

[条件 C-687391d529d2b295](../../evidence/conditions-sets-040.md#c-687391d529d2b295) · [参数 P-e7de55dec44fbd77](../../evidence/parameters-sets-017.md#p-e7de55dec44fbd77) · [状态效果 S-31ecaa896ac1092c](../../evidence/state_effects-sets-011.md#s-31ecaa896ac1092c)

### path-044822

```text
(config)# no do-exec test memory history <number:1..60> <cr>
```

Handler ` RVA 0xD79B850 `；selector ` 0 `；EOL ` RVA 0x33EEA5B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Period of history collection in minutes。

[条件 C-5fbbe7294519f4af](../../evidence/conditions-sets-037.md#c-5fbbe7294519f4af) · [参数 P-bff5968e13295850](../../evidence/parameters-sets-015.md#p-bff5968e13295850) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-034683

```text
(config)# no do-exec test memory nvram-multibus <cr>
```

Handler ` RVA 0xE8F44F0 `；selector ` 0 `；EOL ` RVA 0x3433EE50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-687391d529d2b295](../../evidence/conditions-sets-040.md#c-687391d529d2b295) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-060234

```text
(config)# no do-exec test mfib cb-support IPv4 add group <address> source <address> vrf <number:0..100> intf <number:0..255> <cr>
```

Handler ` RVA 0x11957C90 `；selector ` 1 `；EOL ` RVA 0x355AFA00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` group address；` address ` source address；` unsigned_number ` vrf id；` unsigned_number ` if_number。

[条件 C-44764a37c29fe8c0](../../evidence/conditions-sets-027.md#c-44764a37c29fe8c0) · [参数 P-f3f238ba8bd70d5c](../../evidence/parameters-sets-018.md#p-f3f238ba8bd70d5c) · [状态效果 S-a0d646f8ed52463d](../../evidence/state_effects-sets-034.md#s-a0d646f8ed52463d)

### path-060236

```text
(config)# no do-exec test mfib cb-support IPv6 add group <address> source <address> vrf <number:0..100> intf <number:0..255> <cr>
```

Handler ` RVA 0x11957C90 `；selector ` 2 `；EOL ` RVA 0x355AFFE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` group address；` address ` source address；` unsigned_number ` vrf id；` unsigned_number ` if_number。

[条件 C-44764a37c29fe8c0](../../evidence/conditions-sets-027.md#c-44764a37c29fe8c0) · [参数 P-b9f20fac51ecc555](../../evidence/parameters-sets-014.md#p-b9f20fac51ecc555) · [状态效果 S-6b689aba24d1ff6c](../../evidence/state_effects-sets-023.md#s-6b689aba24d1ff6c)

### path-037826

```text
(config)# no do-exec test mfib channel <cr>
```

Handler ` RVA 0x11667890 `；selector ` 0 `；EOL ` RVA 0x35524680 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-962eb28d68dcd55c](../../evidence/conditions-sets-058.md#c-962eb28d68dcd55c) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-037479

```text
(config)# no do-exec test mfib enable <cr>
```

Handler ` RVA 0x11949710 `；selector ` 0 `；EOL ` RVA 0x355AC7B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8391b26b34510a34](../../evidence/conditions-sets-051.md#c-8391b26b34510a34) · [状态效果 S-8daeb7bc0b3528f5](../../evidence/state_effects-sets-030.md#s-8daeb7bc0b3528f5)

### path-047147

```text
(config)# no do-exec test mfib epoch new <cr>
```

Handler ` RVA 0x118FAFB0 `；selector ` 0 `；EOL ` RVA 0x355A6730 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-eabfc2c1c969fe0d](../../evidence/conditions-sets-091.md#c-eabfc2c1c969fe0d) · [状态效果 S-1015096ddbb2cd7a](../../evidence/state_effects-sets-004.md#s-1015096ddbb2cd7a)

### path-037732

```text
(config)# no do-exec test mfib mrib <cr>
```

Handler ` RVA 0x1196AC30 `；selector ` 0 `；EOL ` RVA 0x355AF460 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-44764a37c29fe8c0](../../evidence/conditions-sets-027.md#c-44764a37c29fe8c0) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-037867

```text
(config)# no do-exec test mfib reload <cr>
```

Handler ` RVA 0x11667B00 `；selector ` 0 `；EOL ` RVA 0x35524B30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e5aade789d45dbb5](../../evidence/conditions-sets-089.md#c-e5aade789d45dbb5) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-035754

```text
(config)# no do-exec test mgd-timer watch <cr>
```

Handler ` RVA 0xD7AD830 `；selector ` 0 `；EOL ` RVA 0x33EF0C08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-cfecc57513f0cd36](../../evidence/state_effects-sets-044.md#s-cfecc57513f0cd36)

### path-048959

```text
(config)# no do-exec test mka macsec-sim off <cr>
```

Handler ` RVA 0x16085270 `；selector ` 1 `；EOL ` RVA 0x35EB9D78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-dd5d51dff14980c2](../../evidence/conditions-sets-085.md#c-dd5d51dff14980c2) · [状态效果 S-7d887e238dc77e0b](../../evidence/state_effects-sets-027.md#s-7d887e238dc77e0b)

### path-055217

```text
(config)# no do-exec test mka message-number initial-value <number:1..4294967295> <cr>
```

Handler ` RVA 0x16085270 `；selector ` 2 `；EOL ` RVA 0x35EBA128 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` 32-bit Message Number (default = 1)。

[条件 C-0e36ad791f5199a4](../../evidence/conditions-sets-006.md#c-0e36ad791f5199a4) · [参数 P-2cc60459240682de](../../evidence/parameters-sets-004.md#p-2cc60459240682de) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-055254

```text
(config)# no do-exec test mka message-number window-size <number:0..4294967295> <cr>
```

Handler ` RVA 0x16085270 `；selector ` 5 `；EOL ` RVA 0x35EBA3F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` MN Window Size - # of MKPDUs (default = 0, off)。

[条件 C-0e36ad791f5199a4](../../evidence/conditions-sets-006.md#c-0e36ad791f5199a4) · [参数 P-76ba54810b928371](../../evidence/parameters-sets-009.md#p-76ba54810b928371) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-055287

```text
(config)# no do-exec test mka packet-number initial-value <number:0..4294967295> <cr>
```

Handler ` RVA 0x16085270 `；selector ` 6 `；EOL ` RVA 0x35EBABB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` 32-bit Packet Number (default = 1, PendingPNExhaustion at 3221225472)。

[条件 C-0e36ad791f5199a4](../../evidence/conditions-sets-006.md#c-0e36ad791f5199a4) · [参数 P-5f2a7ac5cf4b91bf](../../evidence/parameters-sets-008.md#p-5f2a7ac5cf4b91bf) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-038624

```text
(config)# no do-exec test mock btrace <cr>
```

Handler ` RVA 0x1653EB30 `；selector ` 4 `；EOL ` RVA 0x35FA0940 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a758693af815a517](../../evidence/conditions-sets-065.md#c-a758693af815a517) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-038737

```text
(config)# no do-exec test mock chasfs <cr>
```

Handler ` RVA 0x1653EB30 `；selector ` 6 `；EOL ` RVA 0x35FA0E90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5c5a31e2e409d5d6](../../evidence/conditions-sets-036.md#c-5c5a31e2e409d5d6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-038677

```text
(config)# no do-exec test mock chassis <cr>
```

Handler ` RVA 0x1653EB30 `；selector ` 5 `；EOL ` RVA 0x35FA0BE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-478553e14dbd2539](../../evidence/conditions-sets-028.md#c-478553e14dbd2539) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-038917

```text
(config)# no do-exec test mock crypto <cr>
```

Handler ` RVA 0x1653EB30 `；selector ` 18 `；EOL ` RVA 0x35FA1930 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-6f29d59c80112ff4](../../evidence/conditions-sets-043.md#c-6f29d59c80112ff4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-038791

```text
(config)# no do-exec test mock cyan <cr>
```

Handler ` RVA 0x1653EB30 `；selector ` 7 `；EOL ` RVA 0x35FA1138 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-eef0a01449389c31](../../evidence/conditions-sets-092.md#c-eef0a01449389c31) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-038582

```text
(config)# no do-exec test mock ei <cr>
```

Handler ` RVA 0x1653EB30 `；selector ` 8 `；EOL ` RVA 0x35FA0698 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a99faa64739f377a](../../evidence/conditions-sets-065.md#c-a99faa64739f377a) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-047531

```text
(config)# no do-exec test mock infra enqueue <cr>
```

Handler ` RVA 0x1653EB30 `；selector ` 1 `；EOL ` RVA 0x35F9F7E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f07c66f4f31683c4](../../evidence/conditions-sets-093.md#c-f07c66f4f31683c4) · [状态效果 S-db8edc484b28f73a](../../evidence/state_effects-sets-046.md#s-db8edc484b28f73a)

### path-038491

```text
(config)# no do-exec test mock ipc <cr>
```

Handler ` RVA 0x1653EB30 `；selector ` 11 `；EOL ` RVA 0x35FA0148 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c3ad160a58a0442b](../../evidence/conditions-sets-076.md#c-c3ad160a58a0442b) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-038441

```text
(config)# no do-exec test mock mcp <cr>
```

Handler ` RVA 0x1653EB30 `；selector ` 2 `；EOL ` RVA 0x35F9FEA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f5de2f34f1177ce3](../../evidence/conditions-sets-095.md#c-f5de2f34f1177ce3) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-038537

```text
(config)# no do-exec test mock misc <cr>
```

Handler ` RVA 0x1653EB30 `；selector ` 3 `；EOL ` RVA 0x35FA03F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1684677513a6c990](../../evidence/conditions-sets-009.md#c-1684677513a6c990) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-048038

```text
(config)# no do-exec test mock overlayfs system-call <cr>
```

Handler ` RVA 0x1653EB30 `；selector ` 20 `；EOL ` RVA 0x35FA1EC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-fbb70f28ff9e9aa1](../../evidence/conditions-sets-097.md#c-fbb70f28ff9e9aa1) · [状态效果 S-7c397a7315d14b9a](../../evidence/state_effects-sets-026.md#s-7c397a7315d14b9a)

### path-038875

```text
(config)# no do-exec test mock real <cr>
```

Handler ` RVA 0x1653EB30 `；selector ` 9 `；EOL ` RVA 0x35FA1688 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-af921d3f03ebd3dc](../../evidence/conditions-sets-068.md#c-af921d3f03ebd3dc) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-038401

```text
(config)# no do-exec test mock system <cr>
```

Handler ` RVA 0x1653EB30 `；selector ` 17 `；EOL ` RVA 0x35F9FBF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1361ca0ee2f133b6](../../evidence/conditions-sets-008.md#c-1361ca0ee2f133b6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-038831

```text
(config)# no do-exec test mock tdl <cr>
```

Handler ` RVA 0x1653EB30 `；selector ` 10 `；EOL ` RVA 0x35FA13E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ca441ac90ac4a059](../../evidence/conditions-sets-078.md#c-ca441ac90ac4a059) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-038971

```text
(config)# no do-exec test mock vaarg <cr>
```

Handler ` RVA 0x1653EB30 `；selector ` 19 `；EOL ` RVA 0x35FA1BD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-692039b231158d53](../../evidence/conditions-sets-041.md#c-692039b231158d53) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-054702

```text
(config)# no do-exec test monitor clear config lock <cr>
```

Handler ` RVA 0xE4CE1F0 `；selector ` 0 `；EOL ` RVA 0x342CFCF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-037621

```text
(config)# no do-exec test mrib disable <cr>
```

Handler ` RVA 0x1190F470 `；selector ` 0 `；EOL ` RVA 0x355A7AF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c2e6d5847a9b8347](../../evidence/conditions-sets-075.md#c-c2e6d5847a9b8347) · [状态效果 S-7d9948c4645b9eac](../../evidence/state_effects-sets-027.md#s-7d9948c4645b9eac)

### path-047188

```text
(config)# no do-exec test mrib ip stop <cr>
```

Handler ` RVA 0x1190F470 `；selector ` 0 `；EOL ` RVA 0x35376868 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4e4d94fe48ab7d0a](../../evidence/conditions-sets-031.md#c-4e4d94fe48ab7d0a) · [状态效果 S-3c6c9fea8a0227ca](../../evidence/state_effects-sets-013.md#s-3c6c9fea8a0227ca)

### path-047166

```text
(config)# no do-exec test mrib ipv6 stop <cr>
```

Handler ` RVA 0x1190F470 `；selector ` 0 `；EOL ` RVA 0x35540A50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7040c83f84fac2a4](../../evidence/conditions-sets-043.md#c-7040c83f84fac2a4) · [状态效果 S-4c8f293615411e54](../../evidence/state_effects-sets-017.md#s-4c8f293615411e54)

### path-059840

```text
(config)# no do-exec test mvpn ipv4 leaf-ad-recv add <address> <address> <address> <cr>
```

Handler ` RVA 0xF963F30 `；selector ` 0 `；EOL ` RVA 0x34790B08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` Leaf A-D Route Key Source address；` address ` Leaf A-D Route Key Group address；` address ` Leaf A-D Originating IP address。

[条件 C-8c5641a18797689a](../../evidence/conditions-sets-054.md#c-8c5641a18797689a) · [参数 P-e7edaa477d6f924d](../../evidence/parameters-sets-017.md#p-e7edaa477d6f924d) · [状态效果 S-2a57923e56f901dc](../../evidence/state_effects-sets-009.md#s-2a57923e56f901dc)

### path-054203

```text
(config)# no do-exec test mvpn ipv4 spt-only disable <cr>
```

Handler ` RVA 0xF963F30 `；selector ` 2 `；EOL ` RVA 0x347910B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-95ee4499abae09e7](../../evidence/conditions-sets-058.md#c-95ee4499abae09e7) · [状态效果 S-63376d42415b540a](../../evidence/state_effects-sets-021.md#s-63376d42415b540a)

### path-054178

```text
(config)# no do-exec test mvpn ipv4 spt-only enable <cr>
```

Handler ` RVA 0xF963F30 `；selector ` 1 `；EOL ` RVA 0x34790E10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-cf7c1e2ec741c8a8](../../evidence/conditions-sets-080.md#c-cf7c1e2ec741c8a8) · [状态效果 S-63376d42415b540a](../../evidence/state_effects-sets-021.md#s-63376d42415b540a)

### path-059844

```text
(config)# no do-exec test mvpn ipv6 leaf-ad-recv add <address> <address> <address> <cr>
```

Handler ` RVA 0xF963F30 `；selector ` 0 `；EOL ` RVA 0x347916C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` Leaf A-D Route Key Source address；` address ` Leaf A-D Route Key Group address；` address ` Leaf A-D Originating IP address。

[条件 C-d06722cfa05bc8f6](../../evidence/conditions-sets-080.md#c-d06722cfa05bc8f6) · [参数 P-2d64e798f1d53ea9](../../evidence/parameters-sets-004.md#p-2d64e798f1d53ea9) · [状态效果 S-3307eb2e46afbb18](../../evidence/state_effects-sets-011.md#s-3307eb2e46afbb18)

### path-054219

```text
(config)# no do-exec test mvpn ipv6 spt-only disable <cr>
```

Handler ` RVA 0xF963F30 `；selector ` 2 `；EOL ` RVA 0x34791C70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e58e8f3d0772129a](../../evidence/conditions-sets-089.md#c-e58e8f3d0772129a) · [状态效果 S-29d496e5a7ff3025](../../evidence/state_effects-sets-009.md#s-29d496e5a7ff3025)

### path-054197

```text
(config)# no do-exec test mvpn ipv6 spt-only enable <cr>
```

Handler ` RVA 0xF963F30 `；selector ` 1 `；EOL ` RVA 0x347919C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-efbb0a5413fa7fe3](../../evidence/conditions-sets-093.md#c-efbb0a5413fa7fe3) · [状态效果 S-29d496e5a7ff3025](../../evidence/state_effects-sets-009.md#s-29d496e5a7ff3025)

### path-044817

```text
(config)# no do-exec test mvrp enable <number:0..1> <cr>
```

Handler ` RVA 0xC96A0D0 `；selector ` 2 `；EOL ` RVA 0x33B3ACD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Enable - 1, Disable - 0。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-2b2af8342a3221a3](../../evidence/parameters-sets-004.md#p-2b2af8342a3221a3) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-052644

```text
(config)# no do-exec test mvrp joinin <number:1..4094> <number:1..4094> <cr>
```

Handler ` RVA 0xC96A0D0 `；selector ` 1 `；EOL ` RVA 0x33B3AA08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Starting VLAN；` unsigned_number ` VLAN count。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-347f484921822044](../../evidence/parameters-sets-004.md#p-347f484921822044) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-052618

```text
(config)# no do-exec test mvrp new <number:1..4094> <number:1..4094> <cr>
```

Handler ` RVA 0xC96A0D0 `；selector ` 0 `；EOL ` RVA 0x33B3A6D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Starting VLAN；` unsigned_number ` VLAN count。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-47e3eaebeb4262d6](../../evidence/parameters-sets-006.md#p-47e3eaebeb4262d6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-035383

```text
(config)# no do-exec test natmode suppress <cr>
```

Handler ` RVA 0xCF73670 `；selector ` 0 `；EOL ` RVA 0x33D44630 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-6e90c17aae8cf605](../../evidence/state_effects-sets-023.md#s-6e90c17aae8cf605)

### path-039340

```text
(config)# no do-exec test netconf-agent history <cr>
```

Handler ` RVA 0xF3BDEF0 `；selector ` 1 `；EOL ` RVA 0x3462AA78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-039395

```text
(config)# no do-exec test netconf-agent summary <cr>
```

Handler ` RVA 0xF3BDEF0 `；selector ` 3 `；EOL ` RVA 0x3462AD20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-037334

```text
(config)# no do-exec test ngdns config <cr>
```

Handler ` RVA 0xD177360 `；selector ` 0 `；EOL ` RVA 0x33DA53C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e46bb5e8be877e78](../../evidence/conditions-sets-088.md#c-e46bb5e8be877e78) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-046566

```text
(config)# no do-exec test ngdns lookup <string> <cr>
```

Handler ` RVA 0xD177DF0 `；selector ` 0 `；EOL ` RVA 0x33DA5878 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` lookup name。

[条件 C-e46bb5e8be877e78](../../evidence/conditions-sets-088.md#c-e46bb5e8be877e78) · [参数 P-decc2673888888d4](../../evidence/parameters-sets-017.md#p-decc2673888888d4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-046389

```text
(config)# no do-exec test ngdns periodic dump <cr>
```

Handler ` RVA 0xD177180 `；selector ` 0 `；EOL ` RVA 0x33DA4720 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e46bb5e8be877e78](../../evidence/conditions-sets-088.md#c-e46bb5e8be877e78) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-060168

```text
(config)# no do-exec test ngdns periodic register fqdn-name <string> type both module-id <number:1..3> <cr>
```

Handler ` RVA 0xD176ED0 `；selector ` 0 `；EOL ` RVA 0x33DA4368 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Specify FQDN；` unsigned_number ` module-id。

[条件 C-e46bb5e8be877e78](../../evidence/conditions-sets-088.md#c-e46bb5e8be877e78) · [参数 P-ed5b72c7cd03d32e](../../evidence/parameters-sets-018.md#p-ed5b72c7cd03d32e) · [状态效果 S-f43e41d10e09447f](../../evidence/state_effects-sets-052.md#s-f43e41d10e09447f)

### path-048693

```text
(config)# no do-exec test ngiosd process-isolation start <cr>
```

Handler ` RVA 0x1653B780 `；selector ` 0 `；EOL ` RVA 0x35F9EE48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-033417a27e85055a](../../evidence/state_effects-sets-001.md#s-033417a27e85055a)

### path-055064

```text
(config)# no do-exec test ngiosd simulation prepare-failure enable <cr>
```

Handler ` RVA 0x1653B5E0 `；selector ` 0 `；EOL ` RVA 0x35F9E6E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-ac3a5a64915c2810](../../evidence/state_effects-sets-036.md#s-ac3a5a64915c2810)

### path-055104

```text
(config)# no do-exec test ngiosd simulation prepare-pass enable <cr>
```

Handler ` RVA 0x1653B520 `；selector ` 0 `；EOL ` RVA 0x35F9EA80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-8bf8ebd895b5485c](../../evidence/state_effects-sets-030.md#s-8bf8ebd895b5485c)

### path-048638

```text
(config)# no do-exec test ngiosd simulation start <cr>
```

Handler ` RVA 0x1653B6A0 `；selector ` 0 `；EOL ` RVA 0x35F9E378 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-f4218f47d12824f6](../../evidence/state_effects-sets-052.md#s-f4218f47d12824f6)

### path-030488

```text
(config)# no do-exec test nhrp event <cr>
```

Handler ` RVA 0x108D66C0 `；selector ` 8 `；EOL ` RVA 0x34BEAEE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-955b27050b2c0b86](../../evidence/conditions-sets-058.md#c-955b27050b2c0b86) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-040038

```text
(config)# no do-exec test notify <string> <cr>
```

Handler ` RVA 0x15A6CE70 `；selector ` 0 `；EOL ` RVA 0x35DE3AB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Virtual-service name。

[条件 C-bdb6be6e80307689](../../evidence/conditions-sets-073.md#c-bdb6be6e80307689) · [参数 P-bb63f77282b0e6a2](../../evidence/parameters-sets-014.md#p-bb63f77282b0e6a2) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-054591

```text
(config)# no do-exec test nvram <string> clear remote-lock <cr>
```

Handler ` RVA 0xD620830 `；selector ` 1 `；EOL ` RVA 0x33EB0A58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` URL for Nvram filesystem。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-465a9fec902c71c5](../../evidence/parameters-sets-006.md#p-465a9fec902c71c5) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-047873

```text
(config)# no do-exec test nvram <string> explicit-lock <cr>
```

Handler ` RVA 0xD620830 `；selector ` 0 `；EOL ` RVA 0x33EB0CE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` URL for Nvram filesystem。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-465a9fec902c71c5](../../evidence/parameters-sets-006.md#p-465a9fec902c71c5) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-047916

```text
(config)# no do-exec test nvram <string> initialize <cr>
```

Handler ` RVA 0xD620830 `；selector ` 2 `；EOL ` RVA 0x33EB0F90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` URL for Nvram filesystem。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-465a9fec902c71c5](../../evidence/parameters-sets-006.md#p-465a9fec902c71c5) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-059375

```text
(config)# no do-exec test odb client <number:1..256> add-static-tlv type <number:0..65535> <cr>
```

Handler ` RVA 0x12414A30 `；selector ` 2 `；EOL ` RVA 0x35856F38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Client handle；` unsigned_number ` TLV type。

[条件 C-65c960ae397cdeca](../../evidence/conditions-sets-039.md#c-65c960ae397cdeca) · [参数 P-4937c32f8d4b15b3](../../evidence/parameters-sets-006.md#p-4937c32f8d4b15b3) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-054470

```text
(config)# no do-exec test odb client <number:1..256> deregister <cr>
```

Handler ` RVA 0x12414A30 `；selector ` 1 `；EOL ` RVA 0x35856BE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Client handle。

[条件 C-bd0d4f42fd52a202](../../evidence/conditions-sets-073.md#c-bd0d4f42fd52a202) · [参数 P-9dd44be07c481a6e](../../evidence/parameters-sets-012.md#p-9dd44be07c481a6e) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-060223

```text
(config)# no do-exec test odb client <number:1..256> row <number:0..4294967295> <number:0..4294967295> add-tlv type <number:0..65535> value <string> <cr>
```

Handler ` RVA 0x12414A30 `；selector ` 8 `；EOL ` RVA 0x358585E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Client handle；` unsigned_number ` Higher 32 bits of record handle；` unsigned_number ` Lower 32 bits of record handle；` unsigned_number ` TLV type；` string ` TLV value。

[条件 C-3719a4adf19f9b4e](../../evidence/conditions-sets-021.md#c-3719a4adf19f9b4e) · [参数 P-3761b49542bab2b5](../../evidence/parameters-sets-005.md#p-3761b49542bab2b5) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-059860

```text
(config)# no do-exec test odb client <number:1..256> row <number:0..4294967295> <number:0..4294967295> delete <cr>
```

Handler ` RVA 0x12414A30 `；selector ` 7 `；EOL ` RVA 0x35858208 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Client handle；` unsigned_number ` Higher 32 bits of record handle；` unsigned_number ` Lower 32 bits of record handle。

[条件 C-5e3eda88e891c3c4](../../evidence/conditions-sets-037.md#c-5e3eda88e891c3c4) · [参数 P-cbbc12b169c74bfe](../../evidence/parameters-sets-015.md#p-cbbc12b169c74bfe) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-060178

```text
(config)# no do-exec test odb client <number:1..256> row <number:0..4294967295> <number:0..4294967295> notify subscribe change <cr>
```

Handler ` RVA 0x12414A30 `；selector ` 9 `；EOL ` RVA 0x35858930 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Client handle；` unsigned_number ` Higher 32 bits of record handle；` unsigned_number ` Lower 32 bits of record handle。

[条件 C-3fc22bb34f143f45](../../evidence/conditions-sets-025.md#c-3fc22bb34f143f45) · [参数 P-cbbc12b169c74bfe](../../evidence/parameters-sets-015.md#p-cbbc12b169c74bfe) · [状态效果 S-ac9ae3f2363542b0](../../evidence/state_effects-sets-036.md#s-ac9ae3f2363542b0)

### path-060205

```text
(config)# no do-exec test odb client <number:1..256> table <number:1..65534> add-row type <number:0..65535> value <string> <cr>
```

Handler ` RVA 0x12414A30 `；selector ` 6 `；EOL ` RVA 0x35857A20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Client handle；` unsigned_number ` Table id；` unsigned_number ` TLV type；` string ` TLV value。

[条件 C-8280f73aebce65a8](../../evidence/conditions-sets-051.md#c-8280f73aebce65a8) · [参数 P-339759b930726c8c](../../evidence/parameters-sets-004.md#p-339759b930726c8c) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-059378

```text
(config)# no do-exec test odb client <number:1..256> table <number:1..65534> delete <cr>
```

Handler ` RVA 0x12414A30 `；selector ` 4 `；EOL ` RVA 0x35857648 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Client handle；` unsigned_number ` Table id。

[条件 C-0594cc0f76363c8c](../../evidence/conditions-sets-003.md#c-0594cc0f76363c8c) · [参数 P-f95d9efa001e6a73](../../evidence/parameters-sets-019.md#p-f95d9efa001e6a73) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-060075

```text
(config)# no do-exec test odb client <number:1..256> table <number:1..65534> notify subscribe add <cr>
```

Handler ` RVA 0x12414A30 `；selector ` 5 `；EOL ` RVA 0x35857D70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Client handle；` unsigned_number ` Table id。

[条件 C-7de68de12eb84937](../../evidence/conditions-sets-049.md#c-7de68de12eb84937) · [参数 P-f95d9efa001e6a73](../../evidence/parameters-sets-019.md#p-f95d9efa001e6a73) · [状态效果 S-541540b84152902a](../../evidence/state_effects-sets-018.md#s-541540b84152902a)

### path-058047

```text
(config)# no do-exec test odb client <number:1..256> table create <cr>
```

Handler ` RVA 0x12414A30 `；selector ` 3 `；EOL ` RVA 0x358572C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Client handle。

[条件 C-1035e1208b6509d2](../../evidence/conditions-sets-006.md#c-1035e1208b6509d2) · [参数 P-9dd44be07c481a6e](../../evidence/parameters-sets-012.md#p-9dd44be07c481a6e) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-054456

```text
(config)# no do-exec test odb client register <string> <cr>
```

Handler ` RVA 0x12414A30 `；selector ` 0 `；EOL ` RVA 0x35856920 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Client name。

[条件 C-eada2de200bdc128](../../evidence/conditions-sets-091.md#c-eada2de200bdc128) · [参数 P-13828cb53228f29f](../../evidence/parameters-sets-002.md#p-13828cb53228f29f) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-054482

```text
(config)# no do-exec test onep cli uninstall <string> <cr>
```

Handler ` RVA 0x13A82E40 `；selector ` 0 `；EOL ` RVA 0x35CAA6E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Configuration Domain。

[条件 C-aca8c656e44e8d48](../../evidence/conditions-sets-067.md#c-aca8c656e44e8d48) · [参数 P-6b00482f66f10d6d](../../evidence/parameters-sets-008.md#p-6b00482f66f10d6d) · [状态效果 S-2d6043057b5c2da7](../../evidence/state_effects-sets-010.md#s-2d6043057b5c2da7)

### path-038679

```text
(config)# no do-exec test onep ctx_reg <cr>
```

Handler ` RVA 0x13A858B0 `；selector ` 0 `；EOL ` RVA 0x35CABFC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-cbd2d4ca9bdda82a](../../evidence/conditions-sets-078.md#c-cbd2d4ca9bdda82a) · [状态效果 S-32569375059a89f7](../../evidence/state_effects-sets-011.md#s-32569375059a89f7)

### path-047823

```text
(config)# no do-exec test onep if_ctx_event enable <cr>
```

Handler ` RVA 0x13A85820 `；selector ` 0 `；EOL ` RVA 0x35CAC308 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c1e0595157b699b1](../../evidence/conditions-sets-075.md#c-c1e0595157b699b1) · [状态效果 S-1807b7e7e356ff3d](../../evidence/state_effects-sets-005.md#s-1807b7e7e356ff3d)

### path-047587

```text
(config)# no do-exec test onep internal enable <cr>
```

Handler ` RVA 0x13A82DA0 `；selector ` 0 `；EOL ` RVA 0x35CAA9D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-b708e0b7f9f33858](../../evidence/state_effects-sets-039.md#s-b708e0b7f9f33858)

### path-047683

```text
(config)# no do-exec test onep thrift list <cr>
```

Handler ` RVA 0x13A863B0 `；selector ` 0 `；EOL ` RVA 0x35CAADE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c667348fe5b32643](../../evidence/conditions-sets-076.md#c-c667348fe5b32643) · [状态效果 S-73f8e416fde8e6b8](../../evidence/state_effects-sets-025.md#s-73f8e416fde8e6b8)

### path-047724

```text
(config)# no do-exec test onep version disable <cr>
```

Handler ` RVA 0x13A86260 `；selector ` 0 `；EOL ` RVA 0x35CAB5B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f0b2d46f709f2a07](../../evidence/conditions-sets-093.md#c-f0b2d46f709f2a07) · [状态效果 S-2d6043057b5c2da7](../../evidence/state_effects-sets-010.md#s-2d6043057b5c2da7)

### path-054524

```text
(config)# no do-exec test onep version disable exact <cr>
```

Handler ` RVA 0x13A86210 `；selector ` 0 `；EOL ` RVA 0x35CAB588 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f0b2d46f709f2a07](../../evidence/conditions-sets-093.md#c-f0b2d46f709f2a07) · [状态效果 S-2d6043057b5c2da7](../../evidence/state_effects-sets-010.md#s-2d6043057b5c2da7)

### path-047711

```text
(config)# no do-exec test onep version enable <cr>
```

Handler ` RVA 0x13A862B0 `；selector ` 0 `；EOL ` RVA 0x35CABA80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f0b2d46f709f2a07](../../evidence/conditions-sets-093.md#c-f0b2d46f709f2a07) · [状态效果 S-2d6043057b5c2da7](../../evidence/state_effects-sets-010.md#s-2d6043057b5c2da7)

### path-038628

```text
(config)# no do-exec test onep xdt_buginf <cr>
```

Handler ` RVA 0x13A84B00 `；selector ` 0 `；EOL ` RVA 0x35CABD18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a860982fc8a9eb83](../../evidence/conditions-sets-065.md#c-a860982fc8a9eb83) · [状态效果 S-2d6043057b5c2da7](../../evidence/state_effects-sets-010.md#s-2d6043057b5c2da7)

### path-047255

```text
(config)# no do-exec test opflex agent ha <cr>
```

Handler ` RVA 0xC482E30 `；selector ` 1 `；EOL ` RVA 0x33A939F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-059370

```text
(config)# no do-exec test opflex agent service vxlan-evpn create <string> <cr>
```

Handler ` RVA 0xC494C00 `；selector ` 0 `；EOL ` RVA 0x33A97360 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Tenant name。

[条件 C-063ab9a36dd5b975](../../evidence/conditions-sets-003.md#c-063ab9a36dd5b975) · [参数 P-b42fb32a7d39d38b](../../evidence/parameters-sets-014.md#p-b42fb32a7d39d38b) · [状态效果 S-bc502bd8b3867b8e](../../evidence/state_effects-sets-040.md#s-bc502bd8b3867b8e)

### path-058007

```text
(config)# no do-exec test opflex agent service vxlan-evpn state <cr>
```

Handler ` RVA 0xC494F30 `；selector ` 0 `；EOL ` RVA 0x33A96FC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-058084

```text
(config)# no do-exec test opssl nonblockingsession server dtls stop <cr>
```

Handler ` RVA 0x12A14A30 `；selector ` 0 `；EOL ` RVA 0x35936140 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-6d1cef05085a0d2a](../../evidence/conditions-sets-042.md#c-6d1cef05085a0d2a) · [状态效果 S-47a7a9d0636eea0d](../../evidence/state_effects-sets-016.md#s-47a7a9d0636eea0d)

### path-037068

```text
(config)# no do-exec test ospf debug <cr>
```

Handler ` RVA 0xFCD52B0 `；selector ` 0 `；EOL ` RVA 0x34894F28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-057773

```text
(config)# no do-exec test ospf nsr cf error <number:0..65535> <cr>
```

Handler ` RVA 0xDACCD90 `；selector ` 10 `；EOL ` RVA 0x33FC6990 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Repeat count。

[条件 C-fc558060f3694bca](../../evidence/conditions-sets-097.md#c-fc558060f3694bca) · [参数 P-1e19628e5a2b3740](../../evidence/parameters-sets-003.md#p-1e19628e5a2b3740) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-053945

```text
(config)# no do-exec test ospf nsr cf flow-off <cr>
```

Handler ` RVA 0xDACCD90 `；selector ` 9 `；EOL ` RVA 0x33FC66A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-fc558060f3694bca](../../evidence/conditions-sets-097.md#c-fc558060f3694bca) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-053879

```text
(config)# no do-exec test ospf nsr cf flow-on <cr>
```

Handler ` RVA 0xDACCD90 `；selector ` 8 `；EOL ` RVA 0x33FC6400 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-fc558060f3694bca](../../evidence/conditions-sets-097.md#c-fc558060f3694bca) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-057772

```text
(config)# no do-exec test ospf nsr cp clear <number:0..65535> <cr>
```

Handler ` RVA 0xDACCD90 `；selector ` 2 `；EOL ` RVA 0x33FC6FB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Opcode。

[条件 C-fc558060f3694bca](../../evidence/conditions-sets-097.md#c-fc558060f3694bca) · [参数 P-588a2cc36056eed0](../../evidence/parameters-sets-007.md#p-588a2cc36056eed0) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-054148

```text
(config)# no do-exec test ospf nsr cp interface <cr>
```

Handler ` RVA 0xDACCD90 `；selector ` 5 `；EOL ` RVA 0x33FC78C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-54ca1d317d7f8cf8](../../evidence/conditions-sets-033.md#c-54ca1d317d7f8cf8) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-054142

```text
(config)# no do-exec test ospf nsr cp lsa <cr>
```

Handler ` RVA 0xDACCD90 `；selector ` 7 `；EOL ` RVA 0x33FC7F68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-fc558060f3694bca](../../evidence/conditions-sets-097.md#c-fc558060f3694bca) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-054173

```text
(config)# no do-exec test ospf nsr cp neighbor <cr>
```

Handler ` RVA 0xDACCD90 `；selector ` 6 `；EOL ` RVA 0x33FC7C90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1c82d1b2cde87f5f](../../evidence/conditions-sets-011.md#c-1c82d1b2cde87f5f) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-053932

```text
(config)# no do-exec test ospf nsr cp nop <cr>
```

Handler ` RVA 0xDACCD90 `；selector ` 1 `；EOL ` RVA 0x33FC6CA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-fc558060f3694bca](../../evidence/conditions-sets-097.md#c-fc558060f3694bca) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-054072

```text
(config)# no do-exec test ospf nsr cp router-id <cr>
```

Handler ` RVA 0xDACCD90 `；selector ` 4 `；EOL ` RVA 0x33FC7530 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-fc558060f3694bca](../../evidence/conditions-sets-097.md#c-fc558060f3694bca) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-057799

```text
(config)# no do-exec test ospf nsr cp sync <number:0..65535> <cr>
```

Handler ` RVA 0xDACCD90 `；selector ` 3 `；EOL ` RVA 0x33FC72A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Event。

[条件 C-fc558060f3694bca](../../evidence/conditions-sets-097.md#c-fc558060f3694bca) · [参数 P-1dd2c57cd27b0f0d](../../evidence/parameters-sets-003.md#p-1dd2c57cd27b0f0d) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-057771

```text
(config)# no do-exec test ospf nsr recovery delay <number:0..255> <cr>
```

Handler ` RVA 0xDACCD90 `；selector ` 11 `；EOL ` RVA 0x33FC82E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Seconds to delay recovery。

[条件 C-fc558060f3694bca](../../evidence/conditions-sets-097.md#c-fc558060f3694bca) · [参数 P-56211fbc98f531aa](../../evidence/parameters-sets-007.md#p-56211fbc98f531aa) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-046689

```text
(config)# no do-exec test ospf nsr unsynchronize <cr>
```

Handler ` RVA 0xDACCD90 `；selector ` 12 `；EOL ` RVA 0x33FC8580 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-fc558060f3694bca](../../evidence/conditions-sets-097.md#c-fc558060f3694bca) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-037923

```text
(config)# no do-exec test ospfv3 crimson <cr>
```

Handler ` RVA 0x11C027D0 `；selector ` 17 `；EOL ` RVA 0x35691980 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-b9628605d8da49c9](../../evidence/state_effects-sets-039.md#s-b9628605d8da49c9)

### path-034288

```text
(config)# no do-exec test parser afs <cr>
```

Handler ` RVA 0xDF6BFD0 `；selector ` 0 `；EOL ` RVA 0x340E0AD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-49514f258a87cea4](../../evidence/conditions-sets-029.md#c-49514f258a87cea4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-044272

```text
(config)# no do-exec test parser configure buffer <cr>
```

Handler ` RVA 0xDEF9430 `；selector ` 0 `；EOL ` RVA 0x340B00E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5f6508a36b1d191a](../../evidence/conditions-sets-037.md#c-5f6508a36b1d191a) · [状态效果 S-f37e1a02ec2e7606](../../evidence/state_effects-sets-051.md#s-f37e1a02ec2e7606)

### path-044089

```text
(config)# no do-exec test parser consume-memory <number:0..2147483647> <cr>
```

Handler ` RVA 0xDEF9560 `；selector ` 0 `；EOL ` RVA 0x340ACF20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Memory size。

[条件 C-73c5f3fb2edd5194](../../evidence/conditions-sets-045.md#c-73c5f3fb2edd5194) · [参数 P-9fc98b3d0183c115](../../evidence/parameters-sets-012.md#p-9fc98b3d0183c115) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-034201

```text
(config)# no do-exec test parser gmd <cr>
```

Handler ` RVA 0xDF333D0 `；selector ` 0 `；EOL ` RVA 0x340AC020 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-73c5f3fb2edd5194](../../evidence/conditions-sets-045.md#c-73c5f3fb2edd5194) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-034825

```text
(config)# no do-exec test parser green-fe <cr>
```

Handler ` RVA 0xDF8E5F0 `；selector ` 0 `；EOL ` RVA 0x340AEDA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8342959d5623cf34](../../evidence/conditions-sets-051.md#c-8342959d5623cf34) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-052210

```text
(config)# no do-exec test parser ngios native-green enable <cr>
```

Handler ` RVA 0xDF8EDC0 `；selector ` 0 `；EOL ` RVA 0x340AE210 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8342959d5623cf34](../../evidence/conditions-sets-051.md#c-8342959d5623cf34) · [状态效果 S-aa955e555e9c609a](../../evidence/state_effects-sets-036.md#s-aa955e555e9c609a)

### path-052237

```text
(config)# no do-exec test parser ngios side-effect per-batch <cr>
```

Handler ` RVA 0xDF8ED00 `；selector ` 0 `；EOL ` RVA 0x340AE5D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8342959d5623cf34](../../evidence/conditions-sets-051.md#c-8342959d5623cf34) · [状态效果 S-bee51989d3cbc0cb](../../evidence/state_effects-sets-040.md#s-bee51989d3cbc0cb)

### path-052266

```text
(config)# no do-exec test parser ngios validation enable <cr>
```

Handler ` RVA 0xDF8EC40 `；selector ` 0 `；EOL ` RVA 0x340AE9C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8342959d5623cf34](../../evidence/conditions-sets-051.md#c-8342959d5623cf34) · [状态效果 S-4299d53b6a7ae569](../../evidence/state_effects-sets-015.md#s-4299d53b6a7ae569)

### path-052290

```text
(config)# no do-exec test parser ngios-meta path disable <cr>
```

Handler ` RVA 0xDF8EA80 `；selector ` 0 `；EOL ` RVA 0x340AF4E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8342959d5623cf34](../../evidence/conditions-sets-051.md#c-8342959d5623cf34) · [状态效果 S-e9298e903855db73](../../evidence/state_effects-sets-049.md#s-e9298e903855db73)

### path-052241

```text
(config)# no do-exec test parser rc errno <number:0..2147483647> <cr>
```

Handler ` RVA 0xDEE2F90 `；selector ` 5 `；EOL ` RVA 0x340ADBA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` errno value to be mapped。

[条件 C-73c5f3fb2edd5194](../../evidence/conditions-sets-045.md#c-73c5f3fb2edd5194) · [参数 P-712d36c9f93ef0d8](../../evidence/parameters-sets-009.md#p-712d36c9f93ef0d8) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-056799

```text
(config)# no do-exec test parser rc failure <number:11..211> <number:1..2> <cr>
```

Handler ` RVA 0xDEE2F90 `；selector ` 4 `；EOL ` RVA 0x340AD2F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` PRC error code；` unsigned_number ` PRC failure type。

[条件 C-73c5f3fb2edd5194](../../evidence/conditions-sets-045.md#c-73c5f3fb2edd5194) · [参数 P-0d3868e4e55310a0](../../evidence/parameters-sets-001.md#p-0d3868e4e55310a0) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-044220

```text
(config)# no do-exec test parser rc invalid <cr>
```

Handler ` RVA 0xDEE2F90 `；selector ` 2 `；EOL ` RVA 0x340AD8B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-73c5f3fb2edd5194](../../evidence/conditions-sets-045.md#c-73c5f3fb2edd5194) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-056811

```text
(config)# no do-exec test parser rc success <number:1..3> <number:1..4> <cr>
```

Handler ` RVA 0xDEE2F90 `；selector ` 3 `；EOL ` RVA 0x340AD630 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` PRC change type；` unsigned_number ` PRC change mode。

[条件 C-73c5f3fb2edd5194](../../evidence/conditions-sets-045.md#c-73c5f3fb2edd5194) · [参数 P-961119851006963a](../../evidence/parameters-sets-012.md#p-961119851006963a) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-044162

```text
(config)# no do-exec test parser redirect small <cr>
```

Handler ` RVA 0xDF6BFD0 `；selector ` 4 `；EOL ` RVA 0x340E0E18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-66cef6ef5cfa3d6f](../../evidence/conditions-sets-040.md#c-66cef6ef5cfa3d6f) · [状态效果 S-1584b64cb32ae232](../../evidence/state_effects-sets-005.md#s-1584b64cb32ae232)

### path-044038

```text
(config)# no do-exec test parser session-lock <number:0..1200> <cr>
```

Handler ` RVA 0xDF6BE30 `；selector ` 1 `；EOL ` RVA 0x340E0238 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Config session lock holdtime in seconds。

[条件 C-e58d1f8bc58f9c10](../../evidence/conditions-sets-089.md#c-e58d1f8bc58f9c10) · [参数 P-146602e89f177353](../../evidence/parameters-sets-002.md#p-146602e89f177353) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-044073

```text
(config)# no do-exec test parser session-lock exit <cr>
```

Handler ` RVA 0xDF6BE30 `；selector ` 2 `；EOL ` RVA 0x340E04E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ac60a8bb88de2f75](../../evidence/conditions-sets-067.md#c-ac60a8bb88de2f75) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-044131

```text
(config)# no do-exec test parser session-lock lock-break <cr>
```

Handler ` RVA 0xDF6BE30 `；selector ` 3 `；EOL ` RVA 0x340E07D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-02a7dfea128fd8c2](../../evidence/conditions-sets-001.md#c-02a7dfea128fd8c2) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-034347

```text
(config)# no do-exec test parser shell <cr>
```

Handler ` RVA 0xDF8E540 `；selector ` 0 `；EOL ` RVA 0x340ADE58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-73c5f3fb2edd5194](../../evidence/conditions-sets-045.md#c-73c5f3fb2edd5194) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-052274

```text
(config)# no do-exec test parser syntax exclude display <cr>
```

Handler ` RVA 0xDF8F080 `；selector ` 0 `；EOL ` RVA 0x340AFC18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5f6508a36b1d191a](../../evidence/conditions-sets-037.md#c-5f6508a36b1d191a) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-056822

```text
(config)# no do-exec test parser syntax exclude mode <string> <cr>
```

Handler ` RVA 0xDF8EF50 `；selector ` 0 `；EOL ` RVA 0x340AF948 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Name of mode or eol name。

[条件 C-5f6508a36b1d191a](../../evidence/conditions-sets-037.md#c-5f6508a36b1d191a) · [参数 P-7e1cba4935d8d80b](../../evidence/parameters-sets-010.md#p-7e1cba4935d8d80b) · [状态效果 S-79b21e81b7f24cda](../../evidence/state_effects-sets-026.md#s-79b21e81b7f24cda)

### path-058904

```text
(config)# no do-exec test persistent variable api delete default <string> <cr>
```

Handler ` RVA 0xD7C8140 `；selector ` 3 `；EOL ` RVA 0x33EF6C10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Variable name string to delete。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-ff0df765d3c8d9be](../../evidence/parameters-sets-019.md#p-ff0df765d3c8d9be) · [状态效果 S-8e19c43235a3885f](../../evidence/state_effects-sets-030.md#s-8e19c43235a3885f)

### path-056807

```text
(config)# no do-exec test persistent variable api flush default <cr>
```

Handler ` RVA 0xD7C8140 `；selector ` 4 `；EOL ` RVA 0x33EF6F58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-2d021ccd07ac37d4](../../evidence/state_effects-sets-010.md#s-2d021ccd07ac37d4)

### path-058900

```text
(config)# no do-exec test persistent variable api get default <string> <cr>
```

Handler ` RVA 0xD7C8140 `；selector ` 2 `；EOL ` RVA 0x33EF67C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Variable name string to get。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-643ff067af6eb8fe](../../evidence/parameters-sets-008.md#p-643ff067af6eb8fe) · [状态效果 S-7ed3ed5c9c4bdebc](../../evidence/state_effects-sets-027.md#s-7ed3ed5c9c4bdebc)

### path-058894

```text
(config)# no do-exec test persistent variable api isset default <string> <cr>
```

Handler ` RVA 0xD7C8140 `；selector ` 1 `；EOL ` RVA 0x33EF63E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Variable name string to determine if set。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-1e43095dccf81b7e](../../evidence/parameters-sets-003.md#p-1e43095dccf81b7e) · [状态效果 S-d7a1f79c704814e7](../../evidence/state_effects-sets-046.md#s-d7a1f79c704814e7)

### path-058890

```text
(config)# no do-exec test persistent variable api set default <string> <cr>
```

Handler ` RVA 0xD7C8140 `；selector ` 0 `；EOL ` RVA 0x33EF5FF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Namevar string to set of the form &lt;name&gt;=&lt;value&gt;。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-bfff11a8e69a755d](../../evidence/parameters-sets-015.md#p-bfff11a8e69a755d) · [状态效果 S-ebd9155553453289](../../evidence/state_effects-sets-050.md#s-ebd9155553453289)

### path-052147

```text
(config)# no do-exec test persistent variable error <string> <cr>
```

Handler ` RVA 0xD7C8140 `；selector ` 7 `；EOL ` RVA 0x33EF7960 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Error text to display。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-e6db5d0ce3e2c1f1](../../evidence/parameters-sets-017.md#p-e6db5d0ce3e2c1f1) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-052130

```text
(config)# no do-exec test persistent variable media-delete <string> <cr>
```

Handler ` RVA 0xD7C8140 `；selector ` 6 `；EOL ` RVA 0x33EF76A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Full media entry string (filepath) to delete。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-ab01ede20decf82c](../../evidence/parameters-sets-013.md#p-ab01ede20decf82c) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-052115

```text
(config)# no do-exec test persistent variable show cache <cr>
```

Handler ` RVA 0xD7C8140 `；selector ` 5 `；EOL ` RVA 0x33EF7340 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-457a162541760e03](../../evidence/state_effects-sets-015.md#s-457a162541760e03)

### path-058903

```text
(config)# no do-exec test platform hardware poe cfg crit-limit <number:5000..15000> <cr>
```

Handler ` RVA 0x15FFE680 `；selector ` 11 `；EOL ` RVA 0x35EDE1D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Load shedding critical limit。

[条件 C-6c4a5951fac42fcb](../../evidence/conditions-sets-042.md#c-6c4a5951fac42fcb) · [参数 P-7d7edd3858492b7b](../../evidence/parameters-sets-010.md#p-7d7edd3858492b7b) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-058910

```text
(config)# no do-exec test platform hardware poe cfg warn-limit <number:3000..8000> <cr>
```

Handler ` RVA 0x15FFE680 `；selector ` 12 `；EOL ` RVA 0x35EDE498 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Load shedding warning limit。

[条件 C-6c4a5951fac42fcb](../../evidence/conditions-sets-042.md#c-6c4a5951fac42fcb) · [参数 P-c98be1bcde1a0f08](../../evidence/parameters-sets-015.md#p-c98be1bcde1a0f08) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-052400

```text
(config)# no do-exec test platform software cef autovpn <cr>
```

Handler ` RVA 0xE5CE300 `；selector ` 5 `；EOL ` RVA 0x342FD060 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-052286

```text
(config)# no do-exec test platform software cef bgp <cr>
```

Handler ` RVA 0xE5CE300 `；selector ` 2 `；EOL ` RVA 0x342FC2C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-052373

```text
(config)# no do-exec test platform software cef off <cr>
```

Handler ` RVA 0xE5CE300 `；selector ` 1 `；EOL ` RVA 0x342FCDB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-052342

```text
(config)# no do-exec test platform software cef on <cr>
```

Handler ` RVA 0xE5CE300 `；selector ` 0 `；EOL ` RVA 0x342FCB10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-056896

```text
(config)# no do-exec test platform software cef replicate cbl_l2mc <cr>
```

Handler ` RVA 0xE5CE300 `；selector ` 4 `；EOL ` RVA 0x342FC878 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-056879

```text
(config)# no do-exec test platform software cef replicate mpls <cr>
```

Handler ` RVA 0xE5CE300 `；selector ` 3 `；EOL ` RVA 0x342FC5D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-052770

```text
(config)# no do-exec test platform software crimson db-write-lock <cr>
```

Handler ` RVA 0x1444AAD0 `；selector ` 28 `；EOL ` RVA 0x35D67DC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-041dae412143639f](../../evidence/state_effects-sets-001.md#s-041dae412143639f)

### path-052800

```text
(config)# no do-exec test platform software crimson initdb <cr>
```

Handler ` RVA 0x1444AEF0 `；selector ` 17 `；EOL ` RVA 0x35D68110 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-057093

```text
(config)# no do-exec test platform software crimson notification deregister <cr>
```

Handler ` RVA 0x1444A910 `；selector ` 23 `；EOL ` RVA 0x35D67A70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-057081

```text
(config)# no do-exec test platform software crimson notification register <cr>
```

Handler ` RVA 0x1444A910 `；selector ` 22 `；EOL ` RVA 0x35D67770 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-059986

```text
(config)# no do-exec test platform software crimson operational add <number:0..4294967295> idbname <string> <cr>
```

Handler ` RVA 0x1444A610 `；selector ` 3 `；EOL ` RVA 0x35D6CDA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Data to add；` string ` string to add。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [参数 P-82c7b75fd84e942b](../../evidence/parameters-sets-010.md#p-82c7b75fd84e942b) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-057162

```text
(config)# no do-exec test platform software crimson operational disable <cr>
```

Handler ` RVA 0x1444A610 `；selector ` 24 `；EOL ` RVA 0x35D70078 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)
