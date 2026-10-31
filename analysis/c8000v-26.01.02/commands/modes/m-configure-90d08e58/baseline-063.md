# configure · 六个基础模式的历史连接

[模式索引](README.md) · [总索引](../../README.md)

### path-062587

```text
(config)# do-exec test platform hardware poe get <number:dynamic> global <number:0..255> <number:0..4294967295> <cr>
```

Handler ` RVA 0x15FFD8E0 `；selector ` 5 `；EOL ` RVA 0x35EDCD30 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Slot number；` unsigned_number ` PSE register number；` unsigned_number ` Value to be written。

[条件 C-7f68157d2de705fa](../../evidence/conditions-sets-049.md#c-7f68157d2de705fa) · [缺口 G-afba395f0659b4cd](../../evidence/gaps-sets-006.md#g-afba395f0659b4cd) · [参数 P-6b75b43eaa2d5f51](../../evidence/parameters-sets-008.md#p-6b75b43eaa2d5f51) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062234

```text
(config)# do-exec test platform hardware poe get <number:dynamic> port <cr>
```

Handler ` RVA 0x15FFD8E0 `；selector ` 3 `；EOL ` RVA 0x35EDD288 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Slot number。

[条件 C-1fbf0ad5e10b8025](../../evidence/conditions-sets-012.md#c-1fbf0ad5e10b8025) · [缺口 G-afba395f0659b4cd](../../evidence/gaps-sets-006.md#g-afba395f0659b4cd) · [参数 P-0328915490ed50f1](../../evidence/parameters-sets-001.md#p-0328915490ed50f1) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062465

```text
(config)# do-exec test platform hardware poe get <number:dynamic> port <number:1..48> <cr>
```

Handler ` RVA 0x15FFD8E0 `；selector ` 1 `；EOL ` RVA 0x35EDD2F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Slot number；` unsigned_number ` Port Number。

[条件 C-1fbf0ad5e10b8025](../../evidence/conditions-sets-012.md#c-1fbf0ad5e10b8025) · [缺口 G-afba395f0659b4cd](../../evidence/gaps-sets-006.md#g-afba395f0659b4cd) · [参数 P-05cd8370c97217c3](../../evidence/parameters-sets-001.md#p-05cd8370c97217c3) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062590

```text
(config)# do-exec test platform hardware poe get <number:dynamic> port <number:1..48> mdi-tlv <cr>
```

Handler ` RVA 0x15FFD8E0 `；selector ` 9 `；EOL ` RVA 0x35EDD9B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Slot number；` unsigned_number ` Port Number。

[条件 C-f8bd36d2cb768aeb](../../evidence/conditions-sets-096.md#c-f8bd36d2cb768aeb) · [缺口 G-afba395f0659b4cd](../../evidence/gaps-sets-006.md#g-afba395f0659b4cd) · [参数 P-05cd8370c97217c3](../../evidence/parameters-sets-001.md#p-05cd8370c97217c3) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062633

```text
(config)# do-exec test platform hardware poe get <number:dynamic> port <number:1..48> mdi-tlv invoke <cr>
```

Handler ` RVA 0x15FFD8E0 `；selector ` 8 `；EOL ` RVA 0x35EDD428 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Slot number；` unsigned_number ` Port Number。

[条件 C-26d174127c50c72b](../../evidence/conditions-sets-015.md#c-26d174127c50c72b) · [缺口 G-afba395f0659b4cd](../../evidence/gaps-sets-006.md#g-afba395f0659b4cd) · [参数 P-05cd8370c97217c3](../../evidence/parameters-sets-001.md#p-05cd8370c97217c3) · [状态效果 S-ebc8d8eb8be2f6ee](../../evidence/state_effects-sets-050.md#s-ebc8d8eb8be2f6ee)

### path-062464

```text
(config)# do-exec test platform hardware pse get <number:dynamic> <number:0..24> <number:1..255> <cr>
```

Handler ` RVA 0x15FFD8E0 `；selector ` 6 `；EOL ` RVA 0x35EDEC70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Slot number；` unsigned_number ` Quad Chip number；` unsigned_number ` PSE register number。

[条件 C-152d123b6b42af31](../../evidence/conditions-sets-008.md#c-152d123b6b42af31) · [缺口 G-1fdcbce9dfb6fc5b](../../evidence/gaps-sets-002.md#g-1fdcbce9dfb6fc5b) · [参数 P-6b29e1d3e80ca9aa](../../evidence/parameters-sets-008.md#p-6b29e1d3e80ca9aa) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062588

```text
(config)# do-exec test platform hardware pse get <number:dynamic> <number:0..24> <number:1..255> <number:0..255> <cr>
```

Handler ` RVA 0x15FFD8E0 `；selector ` 7 `；EOL ` RVA 0x35EDE9E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Slot number；` unsigned_number ` Quad Chip number；` unsigned_number ` PSE register number；` unsigned_number ` Value to be written。

[条件 C-192925a2373fcaa9](../../evidence/conditions-sets-010.md#c-192925a2373fcaa9) · [缺口 G-1fdcbce9dfb6fc5b](../../evidence/gaps-sets-002.md#g-1fdcbce9dfb6fc5b) · [参数 P-8e2de16e80d65ac3](../../evidence/parameters-sets-011.md#p-8e2de16e80d65ac3) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-044457

```text
(config)# do-exec test platform software cef autovpn <cr>
```

Handler ` RVA 0xE5CE300 `；selector ` 5 `；EOL ` RVA 0x342FD060 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-044329

```text
(config)# do-exec test platform software cef bgp <cr>
```

Handler ` RVA 0xE5CE300 `；selector ` 2 `；EOL ` RVA 0x342FC2C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-044424

```text
(config)# do-exec test platform software cef off <cr>
```

Handler ` RVA 0xE5CE300 `；selector ` 1 `；EOL ` RVA 0x342FCDB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-044396

```text
(config)# do-exec test platform software cef on <cr>
```

Handler ` RVA 0xE5CE300 `；selector ` 0 `；EOL ` RVA 0x342FCB10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-052365

```text
(config)# do-exec test platform software cef replicate cbl_l2mc <cr>
```

Handler ` RVA 0xE5CE300 `；selector ` 4 `；EOL ` RVA 0x342FC878 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-052326

```text
(config)# do-exec test platform software cef replicate mpls <cr>
```

Handler ` RVA 0xE5CE300 `；selector ` 3 `；EOL ` RVA 0x342FC5D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062463

```text
(config)# do-exec test platform software chassis subslot <?slotcard_action@5555898019f0> insert <number:0..4294967295> <cr>
```

Handler ` RVA 0xE389330 `；selector ` 0 `；EOL ` RVA 0x342ADAE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Enter a supported spa type。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [缺口 G-e82f55e189092bfe](../../evidence/gaps-sets-008.md#g-e82f55e189092bfe) · [参数 P-2bb4f74a63fbc399](../../evidence/parameters-sets-004.md#p-2bb4f74a63fbc399) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062235

```text
(config)# do-exec test platform software chassis subslot <?slotcard_action@5555898019f0> remove <cr>
```

Handler ` RVA 0xE389330 `；selector ` 1 `；EOL ` RVA 0x342ADD68 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [缺口 G-e82f55e189092bfe](../../evidence/gaps-sets-008.md#g-e82f55e189092bfe) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-045042

```text
(config)# do-exec test platform software crimson db-write-lock <cr>
```

Handler ` RVA 0x1444AAD0 `；selector ` 28 `；EOL ` RVA 0x35D67DC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-4f9116dd8e1dd553](../../evidence/state_effects-sets-017.md#s-4f9116dd8e1dd553)

### path-045108

```text
(config)# do-exec test platform software crimson initdb <cr>
```

Handler ` RVA 0x1444AEF0 `；selector ` 17 `；EOL ` RVA 0x35D68110 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-052789

```text
(config)# do-exec test platform software crimson notification deregister <cr>
```

Handler ` RVA 0x1444A910 `；selector ` 23 `；EOL ` RVA 0x35D67A70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-052768

```text
(config)# do-exec test platform software crimson notification register <cr>
```

Handler ` RVA 0x1444A910 `；selector ` 22 `；EOL ` RVA 0x35D67770 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-059711

```text
(config)# do-exec test platform software crimson operational add <number:0..4294967295> idbname <string> <cr>
```

Handler ` RVA 0x1444A610 `；selector ` 3 `；EOL ` RVA 0x35D6CDA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Data to add；` string ` string to add。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [参数 P-82c7b75fd84e942b](../../evidence/parameters-sets-010.md#p-82c7b75fd84e942b) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062639

```text
(config)# do-exec test platform software crimson operational add <number:0..4294967295> subblock <?option@55558b2c1020> <number:0..4294967295> <cr>
```

Handler ` RVA 0x1444A680 `；selector ` 18 `；EOL ` RVA 0x35D6D168 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Data to add；` unsigned_number ` sb-type key to add。

[条件 C-b969d69f330aeb31](../../evidence/conditions-sets-072.md#c-b969d69f330aeb31) · [缺口 G-102c39908f63af86](../../evidence/gaps-sets-001.md#g-102c39908f63af86) · [参数 P-b5ea519a914743d7](../../evidence/parameters-sets-014.md#p-b5ea519a914743d7) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062658

```text
(config)# do-exec test platform software crimson operational add <number:0..4294967295> subblock <?option@55558b2c1020> <number:0..4294967295> delete <cr>
```

Handler ` RVA 0x1444A680 `；selector ` 20 `；EOL ` RVA 0x35D6D140 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Data to add；` unsigned_number ` sb-type key to add。

[条件 C-b969d69f330aeb31](../../evidence/conditions-sets-072.md#c-b969d69f330aeb31) · [缺口 G-102c39908f63af86](../../evidence/gaps-sets-001.md#g-102c39908f63af86) · [参数 P-b5ea519a914743d7](../../evidence/parameters-sets-014.md#p-b5ea519a914743d7) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-052958

```text
(config)# do-exec test platform software crimson operational disable <cr>
```

Handler ` RVA 0x1444A610 `；selector ` 24 `；EOL ` RVA 0x35D70078 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-057177

```text
(config)# do-exec test platform software crimson operational disable idb <cr>
```

Handler ` RVA 0x1444A610 `；selector ` 25 `；EOL ` RVA 0x35D700E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-059082

```text
(config)# do-exec test platform software crimson operational disable idb filter <cr>
```

Handler ` RVA 0x1444A610 `；selector ` 26 `；EOL ` RVA 0x35D700B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-052806

```text
(config)# do-exec test platform software crimson operational init <cr>
```

Handler ` RVA 0x1444A610 `；selector ` 0 `；EOL ` RVA 0x35D6C4E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-057088

```text
(config)# do-exec test platform software crimson operational init app <cr>
```

Handler ` RVA 0x1444A610 `；selector ` 1 `；EOL ` RVA 0x35D6C218 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-057077

```text
(config)# do-exec test platform software crimson operational init eventq <cr>
```

Handler ` RVA 0x1444A610 `；selector ` 32 `；EOL ` RVA 0x35D6BF70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-057107

```text
(config)# do-exec test platform software crimson operational init idb <cr>
```

Handler ` RVA 0x1444A610 `；selector ` 2 `；EOL ` RVA 0x35D6C550 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-059060

```text
(config)# do-exec test platform software crimson operational init idb filter <cr>
```

Handler ` RVA 0x1444A610 `；selector ` 27 `；EOL ` RVA 0x35D6C528 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-057161

```text
(config)# do-exec test platform software crimson operational lock acquire <cr>
```

Handler ` RVA 0x1444A610 `；selector ` 12 `；EOL ` RVA 0x35D6F338 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-059077

```text
(config)# do-exec test platform software crimson operational lock acquire offload <cr>
```

Handler ` RVA 0x1444A610 `；selector ` 13 `；EOL ` RVA 0x35D6F310 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-057178

```text
(config)# do-exec test platform software crimson operational lock release <cr>
```

Handler ` RVA 0x1444A610 `；selector ` 14 `；EOL ` RVA 0x35D6F898 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-059083

```text
(config)# do-exec test platform software crimson operational lock release offload <cr>
```

Handler ` RVA 0x1444A610 `；selector ` 15 `；EOL ` RVA 0x35D6F870 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-057174

```text
(config)# do-exec test platform software crimson operational lock status <cr>
```

Handler ` RVA 0x1444A610 `；selector ` 16 `；EOL ` RVA 0x35D6FD68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-052932

```text
(config)# do-exec test platform software crimson operational offload <cr>
```

Handler ` RVA 0x15711CA0 `；selector ` 5 `；EOL ` RVA 0x35D807B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-58bcaecff222bbe4](../../evidence/conditions-sets-035.md#c-58bcaecff222bbe4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-059720

```text
(config)# do-exec test platform software crimson operational offload add <number:0..4294967295> <number:0..4294967295> <cr>
```

Handler ` RVA 0x15711CA0 `；selector ` 1 `；EOL ` RVA 0x35D7FB40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` table type；` unsigned_number ` start key。

[条件 C-d43c00b88b93d6c1](../../evidence/conditions-sets-082.md#c-d43c00b88b93d6c1) · [参数 P-f2756e519af7f30b](../../evidence/parameters-sets-018.md#p-f2756e519af7f30b) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-059729

```text
(config)# do-exec test platform software crimson operational offload delete <number:0..4294967295> <number:0..4294967295> <cr>
```

Handler ` RVA 0x15711CA0 `；selector ` 3 `；EOL ` RVA 0x35D80240 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` table type；` unsigned_number ` start key。

[条件 C-4eac9a39cd4a190d](../../evidence/conditions-sets-031.md#c-4eac9a39cd4a190d) · [参数 P-da19aebda0fb7f04](../../evidence/parameters-sets-016.md#p-da19aebda0fb7f04) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-057098

```text
(config)# do-exec test platform software crimson operational offload register <cr>
```

Handler ` RVA 0x15711CA0 `；selector ` 0 `；EOL ` RVA 0x35D7F7C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5efadb4cdb17932c](../../evidence/conditions-sets-037.md#c-5efadb4cdb17932c) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-059075

```text
(config)# do-exec test platform software crimson operational offload unregister <number:0..4294967295> <cr>
```

Handler ` RVA 0x15711CA0 `；selector ` 4 `；EOL ` RVA 0x35D80530 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` table ID。

[条件 C-1918eecb4b2874b2](../../evidence/conditions-sets-010.md#c-1918eecb4b2874b2) · [参数 P-5b5df38e858431fe](../../evidence/parameters-sets-007.md#p-5b5df38e858431fe) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-059724

```text
(config)# do-exec test platform software crimson operational offload update <number:0..4294967295> <number:0..4294967295> <cr>
```

Handler ` RVA 0x15711CA0 `；selector ` 2 `；EOL ` RVA 0x35D7FEC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` table type；` unsigned_number ` start key。

[条件 C-79db36c854e7463b](../../evidence/conditions-sets-047.md#c-79db36c854e7463b) · [参数 P-95f8ffd09e1156d3](../../evidence/parameters-sets-012.md#p-95f8ffd09e1156d3) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-057118

```text
(config)# do-exec test platform software crimson operational print db <cr>
```

Handler ` RVA 0x1444A610 `；selector ` 7 `；EOL ` RVA 0x35D6E340 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-059074

```text
(config)# do-exec test platform software crimson operational print subblock <number:0..4294967295> <cr>
```

Handler ` RVA 0x1444A680 `；selector ` 21 `；EOL ` RVA 0x35D6E628 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` idb if number。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [参数 P-f15aeabce5aae957](../../evidence/parameters-sets-018.md#p-f15aeabce5aae957) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-057134

```text
(config)# do-exec test platform software crimson operational remove <number:0..4294967295> <cr>
```

Handler ` RVA 0x1444A610 `；selector ` 5 `；EOL ` RVA 0x35D6DD58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Item to remove。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [参数 P-20682b7bb48abe7d](../../evidence/parameters-sets-003.md#p-20682b7bb48abe7d) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062600

```text
(config)# do-exec test platform software crimson operational remove <number:0..4294967295> subblock <?option@55558b2c1d30> <cr>
```

Handler ` RVA 0x1444A680 `；selector ` 19 `；EOL ` RVA 0x35D6DD98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Item to remove。

[条件 C-7ca0c1a1ea7e9071](../../evidence/conditions-sets-048.md#c-7ca0c1a1ea7e9071) · [缺口 G-265fb0f30fb91426](../../evidence/gaps-sets-002.md#g-265fb0f30fb91426) · [参数 P-20682b7bb48abe7d](../../evidence/parameters-sets-003.md#p-20682b7bb48abe7d) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-059064

```text
(config)# do-exec test platform software crimson operational remove <number:0..4294967295> update <cr>
```

Handler ` RVA 0x1444A610 `；selector ` 6 `；EOL ` RVA 0x35D6DA88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Item to remove。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [参数 P-20682b7bb48abe7d](../../evidence/parameters-sets-003.md#p-20682b7bb48abe7d) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-059736

```text
(config)# do-exec test platform software crimson operational set <number:0..4294967295> idbstate <number:0..4294967295> <cr>
```

Handler ` RVA 0x1444A610 `；selector ` 11 `；EOL ` RVA 0x35D6EF90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Item number to set；` unsigned_number ` idbstate value。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [参数 P-f7eb74ab28d3f63d](../../evidence/parameters-sets-018.md#p-f7eb74ab28d3f63d) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-059725

```text
(config)# do-exec test platform software crimson operational set <number:0..4294967295> linestate <number:0..4294967295> <cr>
```

Handler ` RVA 0x1444A610 `；selector ` 8 `；EOL ` RVA 0x35D6E9E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Item number to set；` unsigned_number ` linestate value。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [参数 P-644c4fd59bb06720](../../evidence/parameters-sets-008.md#p-644c4fd59bb06720) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-059732

```text
(config)# do-exec test platform software crimson operational set <number:0..4294967295> namestring <string> <cr>
```

Handler ` RVA 0x1444A610 `；selector ` 9 `；EOL ` RVA 0x35D6ECD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Item number to set；` string ` namestring to set。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [参数 P-3262a3267a94e25d](../../evidence/parameters-sets-004.md#p-3262a3267a94e25d) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-059066

```text
(config)# do-exec test platform software crimson operational update <number:0..4294967295> description <cr>
```

Handler ` RVA 0x1444A610 `；selector ` 4 `；EOL ` RVA 0x35D6D748 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Data to update。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [参数 P-c4f742b09c31791e](../../evidence/parameters-sets-015.md#p-c4f742b09c31791e) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-057140

```text
(config)# do-exec test platform software crimson persist restore-once disable-del <cr>
```

Handler ` RVA 0x1444AEF0 `；selector ` 34 `；EOL ` RVA 0x35D68720 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-057157

```text
(config)# do-exec test platform software crimson persist restore-once enable-del <cr>
```

Handler ` RVA 0x1444AEF0 `；selector ` 35 `；EOL ` RVA 0x35D689C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-052843

```text
(config)# do-exec test platform software crimson unreferenced <string> <cr>
```

Handler ` RVA 0x1444AEF0 `；selector ` 33 `；EOL ` RVA 0x35D68420 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Database name to check for unreferenced memory。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [参数 P-6325791368bc4ff0](../../evidence/parameters-sets-008.md#p-6325791368bc4ff0) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061848

```text
(config)# do-exec test platform software database get <?ei_services_action@55558b2d81b8> <cr>
```

Handler ` RVA 0x1572F3D0 `；selector ` 0 `；EOL ` RVA 0x35D84238 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [缺口 G-c5024cb0cdfa3df9](../../evidence/gaps-sets-007.md#g-c5024cb0cdfa3df9) · [状态效果 S-0cb7cb98f99af0ab](../../evidence/state_effects-sets-003.md#s-0cb7cb98f99af0ab)

### path-058927

```text
(config)# do-exec test platform software dbal batch deadline <number:1..30000> <number:1..30000> <cr>
```

Handler ` RVA 0x15733360 `；selector ` 0 `；EOL ` RVA 0x35D81CA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Deadline of batch execution, between 1 ms and 30000 ms.；` unsigned_number ` After batch execution, sleep between 1 ms and 30000 ms.。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [参数 P-8d2974dd9c14f70c](../../evidence/parameters-sets-011.md#p-8d2974dd9c14f70c) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-059950

```text
(config)# do-exec test platform software dbal batch stress <number:1..4294967295> <number:1..2> <number:1..4294967295> <number:1..2> <cr>
```

Handler ` RVA 0x157307F0 `；selector ` 0 `；EOL ` RVA 0x35D81990 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` number of batches to test；` unsigned_number ` Defer or not in between. 1: defer, 2: do not defer；` unsigned_number ` Number of operation in a batch；` unsigned_number ` Mark batch as priority. 1: normal, 2: priority。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [参数 P-55b53e298fc46ee9](../../evidence/parameters-sets-007.md#p-55b53e298fc46ee9) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-052285

```text
(config)# do-exec test platform software dbal lipc create <cr>
```

Handler ` RVA 0x15730E00 `；selector ` 0 `；EOL ` RVA 0x35D82298 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-052315

```text
(config)# do-exec test platform software dbal lipc destroy <cr>
```

Handler ` RVA 0x15731120 `；selector ` 0 `；EOL ` RVA 0x35D82540 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-052307

```text
(config)# do-exec test platform software dbal ripc create <cr>
```

Handler ` RVA 0x15731320 `；selector ` 0 `；EOL ` RVA 0x35D82818 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-052265

```text
(config)# do-exec test platform software dbal scenario <number:1..6> <cr>
```

Handler ` RVA 0x157314C0 `；selector ` 0 `；EOL ` RVA 0x35D81FA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Type of scenario. 1: local, 2: app, 3: TDL sync, 4: TDL async with output, 5: TDL sync in async way, 6: dbal-test-server。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [参数 P-c71e187408ea9439](../../evidence/parameters-sets-015.md#p-c71e187408ea9439) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-052209

```text
(config)# do-exec test platform software dbal tunnel start <cr>
```

Handler ` RVA 0x15730260 `；selector ` 0 `；EOL ` RVA 0x35D812A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-052244

```text
(config)# do-exec test platform software dbal tunnel stop <cr>
```

Handler ` RVA 0x157306C0 `；selector ` 0 `；EOL ` RVA 0x35D81550 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-044503

```text
(config)# do-exec test platform software dta enable <cr>
```

Handler ` RVA 0xC63EF10 `；selector ` 0 `；EOL ` RVA 0x33AC6710 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-2fd2796c58b7a9ec](../../evidence/state_effects-sets-011.md#s-2fd2796c58b7a9ec)

### path-062247

```text
(config)# do-exec test platform software dvlan configuration <interface> off <cr>
```

Handler ` RVA 0x15761F40 `；selector ` 0 `；EOL ` RVA 0x35D87DB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-afc752d658d4f956](../../evidence/conditions-sets-068.md#c-afc752d658d4f956) · [缺口 G-bafe3d80572e839b](../../evidence/gaps-sets-007.md#g-bafe3d80572e839b) · [参数 P-3b9615c24f2c98fe](../../evidence/parameters-sets-005.md#p-3b9615c24f2c98fe) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062244

```text
(config)# do-exec test platform software dvlan configuration <interface> on <cr>
```

Handler ` RVA 0x15761F40 `；selector ` 1 `；EOL ` RVA 0x35D87B10 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-afc752d658d4f956](../../evidence/conditions-sets-068.md#c-afc752d658d4f956) · [缺口 G-bafe3d80572e839b](../../evidence/gaps-sets-007.md#g-bafe3d80572e839b) · [参数 P-3b9615c24f2c98fe](../../evidence/parameters-sets-005.md#p-3b9615c24f2c98fe) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-052420

```text
(config)# do-exec test platform software dvlan notification off <cr>
```

Handler ` RVA 0x15761F40 `；selector ` 2 `；EOL ` RVA 0x35D88378 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-052383

```text
(config)# do-exec test platform software dvlan notification on <cr>
```

Handler ` RVA 0x15761F40 `；selector ` 3 `；EOL ` RVA 0x35D880D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062251

```text
(config)# do-exec test platform software eoam <interface> lm frames <cr>
```

Handler ` RVA 0xBEBA870 `；selector ` 2 `；EOL ` RVA 0x3391D618 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f76885bf8c78a28e](../../evidence/conditions-sets-096.md#c-f76885bf8c78a28e) · [缺口 G-fccfd8124ec0fbdc](../../evidence/gaps-sets-009.md#g-fccfd8124ec0fbdc) · [参数 P-dcd1e2fe01216f0a](../../evidence/parameters-sets-017.md#p-dcd1e2fe01216f0a) · [状态效果 S-1f4d6b93d5d10ab5](../../evidence/state_effects-sets-007.md#s-1f4d6b93d5d10ab5)

### path-062250

```text
(config)# do-exec test platform software eoam <interface> rfi dg <cr>
```

Handler ` RVA 0xBEBA870 `；selector ` 1 `；EOL ` RVA 0x3391D2C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-bdea1f32d1174173](../../evidence/conditions-sets-073.md#c-bdea1f32d1174173) · [缺口 G-fccfd8124ec0fbdc](../../evidence/gaps-sets-009.md#g-fccfd8124ec0fbdc) · [参数 P-dcd1e2fe01216f0a](../../evidence/parameters-sets-017.md#p-dcd1e2fe01216f0a) · [状态效果 S-939dd88cc4953196](../../evidence/state_effects-sets-031.md#s-939dd88cc4953196)

### path-044695

```text
(config)# do-exec test platform software feature-telemetry disable <cr>
```

Handler ` RVA 0x14B5B8B0 `；selector ` 0 `；EOL ` RVA 0x35D758C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b299ea22be21f3ed](../../evidence/conditions-sets-069.md#c-b299ea22be21f3ed) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-044742

```text
(config)# do-exec test platform software feature-telemetry enable <cr>
```

Handler ` RVA 0x14B5B860 `；selector ` 0 `；EOL ` RVA 0x35D75B68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7cb45392be5b78b8](../../evidence/conditions-sets-048.md#c-7cb45392be5b78b8) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061867

```text
(config)# do-exec test platform software feature-telemetry file <url:dynamic> <cr>
```

Handler ` RVA 0x14B5B7F0 `；selector ` 0 `；EOL ` RVA 0x35D75628 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-40df23647ccc4491](../../evidence/conditions-sets-025.md#c-40df23647ccc4491) · [缺口 G-d02fbef2af5804bc](../../evidence/gaps-sets-007.md#g-d02fbef2af5804bc) · [参数 P-6b9c34b52604839b](../../evidence/parameters-sets-008.md#p-6b9c34b52604839b) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-058935

```text
(config)# do-exec test platform software flow-control identifiers allocate ebfc all <cr>
```

Handler ` RVA 0xEAFA960 `；selector ` 0 `；EOL ` RVA 0x343AA958 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3fe6a169decd9e35](../../evidence/conditions-sets-025.md#c-3fe6a169decd9e35) · [状态效果 S-6c0a2a4170f99ba7](../../evidence/state_effects-sets-023.md#s-6c0a2a4170f99ba7)

### path-059704

```text
(config)# do-exec test platform software infrastructure bipc clear fd <number:1..4294967295> <number:1..4294967295> <cr>
```

Handler ` RVA 0xE9C5930 `；selector ` 6 `；EOL ` RVA 0x34379A90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` IPC channel fd；` unsigned_number ` IPC sequence number。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [参数 P-338c1b6e73df1dd9](../../evidence/parameters-sets-004.md#p-338c1b6e73df1dd9) · [状态效果 S-eac412e6c04f7005](../../evidence/state_effects-sets-050.md#s-eac412e6c04f7005)

### path-052769

```text
(config)# do-exec test platform software infrastructure console on <cr>
```

Handler ` RVA 0xE9C5930 `；selector ` 7 `；EOL ` RVA 0x34379E28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-dfdd4f183575f9c8](../../evidence/conditions-sets-086.md#c-dfdd4f183575f9c8) · [状态效果 S-84375ed938fc8397](../../evidence/state_effects-sets-028.md#s-84375ed938fc8397)

### path-052645

```text
(config)# do-exec test platform software infrastructure drop-debug off <cr>
```

Handler ` RVA 0xE9C5930 `；selector ` 5 `；EOL ` RVA 0x34378A18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-052667

```text
(config)# do-exec test platform software infrastructure drop-debug on <cr>
```

Handler ` RVA 0xE9C5930 `；selector ` 4 `；EOL ` RVA 0x34378CC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-052682

```text
(config)# do-exec test platform software infrastructure pae-cssm send_packet <cr>
```

Handler ` RVA 0x1658B2C0 `；selector ` 0 `；EOL ` RVA 0x35FA4C68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-779c6201aeeb38b5](../../evidence/conditions-sets-047.md#c-779c6201aeeb38b5) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-057071

```text
(config)# do-exec test platform software infrastructure session open <number:1..4294967295> <cr>
```

Handler ` RVA 0xE9C5930 `；selector ` 1 `；EOL ` RVA 0x34379680 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Session handle。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [参数 P-4f1e17e220686aee](../../evidence/parameters-sets-007.md#p-4f1e17e220686aee) · [状态效果 S-9b92ef257d453230](../../evidence/state_effects-sets-033.md#s-9b92ef257d453230)

### path-052663

```text
(config)# do-exec test platform software infrastructure watchdog off <cr>
```

Handler ` RVA 0xE9C5930 `；selector ` 3 `；EOL ` RVA 0x34378FC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-052686

```text
(config)# do-exec test platform software infrastructure watchdog on <cr>
```

Handler ` RVA 0xE9C5930 `；selector ` 2 `；EOL ` RVA 0x34379268 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062473

```text
(config)# do-exec test platform software inject <interface> <address> <address> ipv4 <cr>
```

Handler ` RVA 0xEA9D540 `；selector ` 0 `；EOL ` RVA 0x3439AFB0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Dst MAC address；` address ` Src MAC address。

[条件 C-d5ca267597c96a9f](../../evidence/conditions-sets-082.md#c-d5ca267597c96a9f) · [缺口 G-24844c597d576968](../../evidence/gaps-sets-002.md#g-24844c597d576968) · [参数 P-a7b741a39392a374](../../evidence/parameters-sets-013.md#p-a7b741a39392a374) · [状态效果 S-88185b5ed39fc36a](../../evidence/state_effects-sets-029.md#s-88185b5ed39fc36a)

### path-062472

```text
(config)# do-exec test platform software inject <interface> dhcp discover <address> <cr>
```

Handler ` RVA 0xEA9BB10 `；selector ` 0 `；EOL ` RVA 0x3439A070 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Source mac address。

[条件 C-c1a4738e18ffbbc3](../../evidence/conditions-sets-075.md#c-c1a4738e18ffbbc3) · [缺口 G-03748ad32f2491a3](../../evidence/gaps-sets-001.md#g-03748ad32f2491a3) · [参数 P-9f1308996b5e170b](../../evidence/parameters-sets-012.md#p-9f1308996b5e170b) · [状态效果 S-c7ffdffae539a217](../../evidence/state_effects-sets-042.md#s-c7ffdffae539a217)

### path-062651

```text
(config)# do-exec test platform software inject bd <number:1..4096> <address> <address> <interface> <number:0..65535> ipv4 <cr>
```

Handler ` RVA 0xEA9C880 `；selector ` 1 `；EOL ` RVA 0x343994F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` BD number；` address ` Dst MAC address；` address ` Src MAC address；` unsigned_number ` Src EFP: EFP id。

[条件 C-7003c2f58080a6bc](../../evidence/conditions-sets-043.md#c-7003c2f58080a6bc) · [缺口 G-c4974f3332987537](../../evidence/gaps-sets-007.md#g-c4974f3332987537) · [参数 P-0910d2b161a20358](../../evidence/parameters-sets-001.md#p-0910d2b161a20358) · [状态效果 S-aa8fdbf0c3308924](../../evidence/state_effects-sets-036.md#s-aa8fdbf0c3308924)

### path-059653

```text
(config)# do-exec test platform software inject bd <number:1..4096> <address> <address> ipv4 <cr>
```

Handler ` RVA 0xEA9C880 `；selector ` 1 `；EOL ` RVA 0x343994F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` BD number；` address ` Dst MAC address；` address ` Src MAC address。

[条件 C-a9c8be145fb1b3cc](../../evidence/conditions-sets-065.md#c-a9c8be145fb1b3cc) · [参数 P-1b2ddfe043e3c48c](../../evidence/parameters-sets-003.md#p-1b2ddfe043e3c48c) · [状态效果 S-aa8fdbf0c3308924](../../evidence/state_effects-sets-036.md#s-aa8fdbf0c3308924)

### path-062652

```text
(config)# do-exec test platform software inject bd-local <number:1..4096> <address> <address> <interface> <number:0..65535> ipv4 <cr>
```

Handler ` RVA 0xEA9C880 `；selector ` 2 `；EOL ` RVA 0x34399B78 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` BD number；` address ` Dst MAC address；` address ` Src MAC address；` unsigned_number ` Src EFP: EFP id。

[条件 C-8f103cfc160084ad](../../evidence/conditions-sets-055.md#c-8f103cfc160084ad) · [缺口 G-c45f24ff84830909](../../evidence/gaps-sets-007.md#g-c45f24ff84830909) · [参数 P-a193b376e12df5cd](../../evidence/parameters-sets-012.md#p-a193b376e12df5cd) · [状态效果 S-949b7c4f1ad761f1](../../evidence/state_effects-sets-032.md#s-949b7c4f1ad761f1)

### path-059659

```text
(config)# do-exec test platform software inject bd-local <number:1..4096> <address> <address> ipv4 <cr>
```

Handler ` RVA 0xEA9C880 `；selector ` 2 `；EOL ` RVA 0x34399B78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` BD number；` address ` Dst MAC address；` address ` Src MAC address。

[条件 C-d7ef56c55d1404c7](../../evidence/conditions-sets-083.md#c-d7ef56c55d1404c7) · [参数 P-6e5d53caf4ab1776](../../evidence/parameters-sets-009.md#p-6e5d53caf4ab1776) · [状态效果 S-949b7c4f1ad761f1](../../evidence/state_effects-sets-032.md#s-949b7c4f1ad761f1)

### path-058966

```text
(config)# do-exec test platform software inject bridge_vlan <number:1..4096> <address> <address> <cr>
```

Handler ` RVA 0xEA9C880 `；selector ` 4 `；EOL ` RVA 0x3439A9F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Bridge VLAN number；` address ` Dst MAC address；` address ` Src MAC address。

[条件 C-ed4e88d6636d168b](../../evidence/conditions-sets-092.md#c-ed4e88d6636d168b) · [参数 P-f32d96ee52c39e1c](../../evidence/parameters-sets-018.md#p-f32d96ee52c39e1c) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062634

```text
(config)# do-exec test platform software inject bridge_vlan <number:1..4096> <address> <address> interface <interface> <cr>
```

Handler ` RVA 0xEA9C880 `；selector ` 4 `；EOL ` RVA 0x3439A9F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Bridge VLAN number；` address ` Dst MAC address；` address ` Src MAC address。

[条件 C-519de3ab59becff8](../../evidence/conditions-sets-032.md#c-519de3ab59becff8) · [缺口 G-c033e853ad26f6e2](../../evidence/gaps-sets-007.md#g-c033e853ad26f6e2) · [参数 P-8048fbdc4d17f5ed](../../evidence/parameters-sets-010.md#p-8048fbdc4d17f5ed) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-044184

```text
(config)# do-exec test platform software inject bypass <cr>
```

Handler ` RVA 0xEA60A60 `；selector ` 0 `；EOL ` RVA 0x34398A80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062636

```text
(config)# do-exec test platform software inject efp <interface> <number:0..65535> <address> <address> ipv4 <cr>
```

Handler ` RVA 0xEA9C880 `；selector ` 0 `；EOL ` RVA 0x3439B488 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` EFP id；` address ` Dst MAC address；` address ` Src MAC address。

[条件 C-ac1109a6661890f3](../../evidence/conditions-sets-066.md#c-ac1109a6661890f3) · [缺口 G-c289ed2baa5b197c](../../evidence/gaps-sets-007.md#g-c289ed2baa5b197c) · [参数 P-f0823c50a32323b1](../../evidence/parameters-sets-018.md#p-f0823c50a32323b1) · [状态效果 S-722636fa4ed48635](../../evidence/state_effects-sets-024.md#s-722636fa4ed48635)

### path-052353

```text
(config)# do-exec test platform software inject inject-rate <number:1..10000> <cr>
```

Handler ` RVA 0xEA9BB10 `；selector ` 0 `；EOL ` RVA 0x3439A070 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` packets/sec supported by platfform。

[条件 C-ed4e88d6636d168b](../../evidence/conditions-sets-092.md#c-ed4e88d6636d168b) · [参数 P-d70ce1762a244fde](../../evidence/parameters-sets-016.md#p-d70ce1762a244fde) · [状态效果 S-7c2cbf16e90fc38f](../../evidence/state_effects-sets-026.md#s-7c2cbf16e90fc38f)

### path-052525

```text
(config)# do-exec test platform software inject ipv4 arp-trigger <cr>
```

Handler ` RVA 0xEA60A60 `；selector ` 3 `；EOL ` RVA 0x3439BAB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b256c3b71822bbf8](../../evidence/conditions-sets-069.md#c-b256c3b71822bbf8) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-056972

```text
(config)# do-exec test platform software inject ipv4 nexthop <address> <cr>
```

Handler ` RVA 0xEA60A60 `；selector ` 2 `；EOL ` RVA 0x3439B830 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IPv4 Nexthop Address。

[条件 C-b256c3b71822bbf8](../../evidence/conditions-sets-069.md#c-b256c3b71822bbf8) · [参数 P-c9f339e88974e4e5](../../evidence/parameters-sets-015.md#p-c9f339e88974e4e5) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-052515

```text
(config)# do-exec test platform software inject ipv6 nd-trigger <cr>
```

Handler ` RVA 0xEA60A60 `；selector ` 4 `；EOL ` RVA 0x3439BD88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b256c3b71822bbf8](../../evidence/conditions-sets-069.md#c-b256c3b71822bbf8) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-044194

```text
(config)# do-exec test platform software inject keepalive <cr>
```

Handler ` RVA 0xEA60A60 `；selector ` 6 `；EOL ` RVA 0x343987D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-044218

```text
(config)# do-exec test platform software inject off <cr>
```

Handler ` RVA 0xEA60A60 `；selector ` 1 `；EOL ` RVA 0x34398D28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-044248

```text
(config)# do-exec test platform software inject pak-priority <cr>
```

Handler ` RVA 0xEA60A60 `；selector ` 5 `；EOL ` RVA 0x34398FD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-057075

```text
(config)# do-exec test platform software license expire eval <number:1..259200> <cr>
```

Handler ` RVA 0x12437380 `；selector ` 0 `；EOL ` RVA 0x35867168 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` minutes。

[条件 C-2c0106cbc1898a7c](../../evidence/conditions-sets-017.md#c-2c0106cbc1898a7c) · [参数 P-1e0ad3d9a0d06b72](../../evidence/parameters-sets-003.md#p-1e0ad3d9a0d06b72) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-052716

```text
(config)# do-exec test platform software license metering reachability <cr>
```

Handler ` RVA 0x124373D0 `；selector ` 0 `；EOL ` RVA 0x35866E58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f5c426468dd25130](../../evidence/conditions-sets-095.md#c-f5c426468dd25130) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-052282

```text
(config)# do-exec test platform software lsmpi tx-fail-retry enable <cr>
```

Handler ` RVA 0xED2D730 `；selector ` 0 `；EOL ` RVA 0x3440C730 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-201bd21b5ec2353d](../../evidence/state_effects-sets-007.md#s-201bd21b5ec2353d)

### path-062690

```text
(config)# do-exec test platform software macsec default-action ingress_non_control_non_macsec drop ingress_control_non_macsec drop ingress_non_control_macsec drop ingress_control_macsec drop egress_control drop egress_non_control drop <interface> <cr>
```

Handler ` RVA 0x160D7490 `；selector ` 69 `；EOL ` RVA 0x35EC8088 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-358e89fc93051d72](../../evidence/conditions-sets-021.md#c-358e89fc93051d72) · [缺口 G-c5b3c6e1a37e0e07](../../evidence/gaps-sets-007.md#g-c5b3c6e1a37e0e07) · [参数 P-f91498f2f12f9ee4](../../evidence/parameters-sets-019.md#p-f91498f2f12f9ee4) · [状态效果 S-98ec71f146d490b9](../../evidence/state_effects-sets-032.md#s-98ec71f146d490b9)

### path-062598

```text
(config)# do-exec test platform software macsec frame-capture enable direction ingress <interface> <cr>
```

Handler ` RVA 0x160D7490 `；selector ` 66 `；EOL ` RVA 0x35EC8880 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4a81be8ada6bd9b5](../../evidence/conditions-sets-029.md#c-4a81be8ada6bd9b5) · [缺口 G-771707a69e86f88d](../../evidence/gaps-sets-005.md#g-771707a69e86f88d) · [参数 P-1a573e51e4ef55fe](../../evidence/parameters-sets-002.md#p-1a573e51e4ef55fe) · [状态效果 S-08ee780aef6e4e11](../../evidence/state_effects-sets-002.md#s-08ee780aef6e4e11)

### path-057076

```text
(config)# do-exec test platform software macsec pattern-delete name <string> <cr>
```

Handler ` RVA 0x160D7490 `；selector ` 54 `；EOL ` RVA 0x35ECA218 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` pattern name。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [参数 P-2b96e7d041d5508f](../../evidence/parameters-sets-004.md#p-2b96e7d041d5508f) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062484

```text
(config)# do-exec test platform software macsec pattern-detach name <string> <interface> <cr>
```

Handler ` RVA 0x160D7490 `；selector ` 56 `；EOL ` RVA 0x35ECA610 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` pattern name。

[条件 C-05c58ebeeeccd169](../../evidence/conditions-sets-003.md#c-05c58ebeeeccd169) · [缺口 G-fe5b4b62c2cee16f](../../evidence/gaps-sets-009.md#g-fe5b4b62c2cee16f) · [参数 P-ca7f81b167576206](../../evidence/parameters-sets-015.md#p-ca7f81b167576206) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-060273

```text
(config)# do-exec test platform software macsec pattern-name name <string> is-control yes has-vlan-tag yes has-vlan-inner-tag yes vlan-id <number:0..65535> inner-vlan-id <number:0..65535> priority <number:0..15> header <string> header-length <number:0..65535> control-frame dmac dest-mac <address> <cr>
```

Handler ` RVA 0x160D7490 `；selector ` 55 `；EOL ` RVA 0x35EC94B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` pattern name；` unsigned_number ` outer vlan id；` unsigned_number ` inner vlan id；` unsigned_number ` priority level；` string ` header pattern；` unsigned_number ` header pattern length；` address ` MAC address。

[条件 C-46f9c82671e8712f](../../evidence/conditions-sets-028.md#c-46f9c82671e8712f) · [参数 P-8671486ebe6bccdf](../../evidence/parameters-sets-010.md#p-8671486ebe6bccdf) · [状态效果 S-55daa41a176e19e9](../../evidence/state_effects-sets-019.md#s-55daa41a176e19e9)

### path-062676

```text
(config)# do-exec test platform software macsec pattern-set name <string> action controlled-port direction ingress <interface> <cr>
```

Handler ` RVA 0x160D7490 `；selector ` 53 `；EOL ` RVA 0x35EC9D30 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` pattern name。

[条件 C-d6418e01ccac9566](../../evidence/conditions-sets-083.md#c-d6418e01ccac9566) · [缺口 G-c00353e2cbfa174c](../../evidence/gaps-sets-007.md#g-c00353e2cbfa174c) · [参数 P-0fc900d7b707bda3](../../evidence/parameters-sets-002.md#p-0fc900d7b707bda3) · [状态效果 S-b88dc966b7873a47](../../evidence/state_effects-sets-039.md#s-b88dc966b7873a47)

### path-061887

```text
(config)# do-exec test platform software macsec post <interface> <cr>
```

Handler ` RVA 0x160D7490 `；selector ` 20 `；EOL ` RVA 0x35ECF688 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-fd0879cf653e271d](../../evidence/conditions-sets-098.md#c-fd0879cf653e271d) · [缺口 G-25885e093e8090a4](../../evidence/gaps-sets-002.md#g-25885e093e8090a4) · [参数 P-f4c1fe614c8b6c78](../../evidence/parameters-sets-018.md#p-f4c1fe614c8b6c78) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062685

```text
(config)# do-exec test platform software macsec rx sa delete an <number:0..3> mac-addr <address> vport <number:0..65535> <interface> <cr>
```

Handler ` RVA 0x160D7490 `；selector ` 35 `；EOL ` RVA 0x35ECBFF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` 0-3 association；` address ` MAC address；` unsigned_number ` 16 bit port id。

[条件 C-5d920b298b9e5136](../../evidence/conditions-sets-036.md#c-5d920b298b9e5136) · [缺口 G-cd4a4aef3c784a18](../../evidence/gaps-sets-007.md#g-cd4a4aef3c784a18) · [参数 P-df88aa5f11f5e897](../../evidence/parameters-sets-017.md#p-df88aa5f11f5e897) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062686

```text
(config)# do-exec test platform software macsec rx sa lowest-pn <number:0..4294967295> an <number:0..3> mac-addr <address> vport <number:0..65535> <interface> <cr>
```

Handler ` RVA 0x160D7490 `；selector ` 37 `；EOL ` RVA 0x35ECC578 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` 32 bit lowest packet number；` unsigned_number ` 0-3 association；` address ` MAC address；` unsigned_number ` 16 bit port id。

[条件 C-8948be59b5ac2cdd](../../evidence/conditions-sets-053.md#c-8948be59b5ac2cdd) · [缺口 G-4ce08f20ba6e0a8c](../../evidence/gaps-sets-003.md#g-4ce08f20ba6e0a8c) · [参数 P-66fc7c05f2c52f4a](../../evidence/parameters-sets-008.md#p-66fc7c05f2c52f4a) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062694

```text
(config)# do-exec test platform software macsec rx sa set an <number:0..3> lowest-pn <number:0..4294967295> sak <string> length <number:0..4294967295> hash-key <string> mac-addr <address> vport <number:0..65535> <interface> <cr>
```

Handler ` RVA 0x160D7490 `；selector ` 36 `；EOL ` RVA 0x35ECBA68 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` 0-3 association；` unsigned_number ` 32 bit packet number；` string ` pre shared key；` unsigned_number ` SAK length；` string ` hash key (128 bit or 16 character)；` address ` MAC address；` unsigned_number ` 16 bit port id。

[条件 C-97c46e01089058d2](../../evidence/conditions-sets-059.md#c-97c46e01089058d2) · [缺口 G-7b52350f05401203](../../evidence/gaps-sets-005.md#g-7b52350f05401203) · [参数 P-2368a3845190d6fb](../../evidence/parameters-sets-003.md#p-2368a3845190d6fb) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062687

```text
(config)# do-exec test platform software macsec rx sc add mac-addr <address> vport <number:0..65535> mac-addr <address> vport <number:0..65535> <interface> <cr>
```

Handler ` RVA 0x160D7490 `；selector ` 24 `；EOL ` RVA 0x35ECB248 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` MAC address；` unsigned_number ` 16 bit port id；` address ` MAC address；` unsigned_number ` 16 bit port id。

[条件 C-d4af0417abc3df99](../../evidence/conditions-sets-082.md#c-d4af0417abc3df99) · [缺口 G-2c399004a64e4196](../../evidence/gaps-sets-002.md#g-2c399004a64e4196) · [参数 P-df797416e89fb5ac](../../evidence/parameters-sets-017.md#p-df797416e89fb5ac) · [状态效果 S-8ec3f9b192c621df](../../evidence/state_effects-sets-030.md#s-8ec3f9b192c621df)

### path-062696

```text
(config)# do-exec test platform software macsec secy create cipher 128 offset none mac-addr <address> replay-enable no protect yes sci yes es yes scb yes validate-frames check <interface> <cr>
```

Handler ` RVA 0x160D7490 `；selector ` 3 `；EOL ` RVA 0x35ECE5A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` MAC address。

[条件 C-b1df2a4af850ab5c](../../evidence/conditions-sets-069.md#c-b1df2a4af850ab5c) · [缺口 G-13cb7245c71a585f](../../evidence/gaps-sets-001.md#g-13cb7245c71a585f) · [参数 P-19758993ed4d3727](../../evidence/parameters-sets-002.md#p-19758993ed4d3727) · [状态效果 S-a12e294f8eab5a18](../../evidence/state_effects-sets-034.md#s-a12e294f8eab5a18)

### path-062268

```text
(config)# do-exec test platform software macsec secy delete <interface> <cr>
```

Handler ` RVA 0x160D7490 `；selector ` 2 `；EOL ` RVA 0x35ECEEA8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e15986e66a2ccc18](../../evidence/conditions-sets-087.md#c-e15986e66a2ccc18) · [缺口 G-fcdc387cad429372](../../evidence/gaps-sets-009.md#g-fcdc387cad429372) · [参数 P-860da46be79bd41a](../../evidence/parameters-sets-010.md#p-860da46be79bd41a) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062270

```text
(config)# do-exec test platform software macsec secy enable <interface> <cr>
```

Handler ` RVA 0x160D7490 `；selector ` 1 `；EOL ` RVA 0x35ECF288 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5d54fad239240c26](../../evidence/conditions-sets-036.md#c-5d54fad239240c26) · [缺口 G-e29ca66b2e98b5a0](../../evidence/gaps-sets-008.md#g-e29ca66b2e98b5a0) · [参数 P-ba022531a42377d2](../../evidence/parameters-sets-014.md#p-ba022531a42377d2) · [状态效果 S-9047fc5b2d611e14](../../evidence/state_effects-sets-031.md#s-9047fc5b2d611e14)

### path-062677

```text
(config)# do-exec test platform software macsec tag-clear-mode vlan-tag <number:0..65535> header-len <number:0..65535> header-etype <number:0..65535> <interface> <cr>
```

Handler ` RVA 0x160D7490 `；selector ` 63 `；EOL ` RVA 0x35ECAB60 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` number of vlans in the clear；` unsigned_number ` length of header；` unsigned_number ` length of header。

[条件 C-7660a632b2dc84d3](../../evidence/conditions-sets-046.md#c-7660a632b2dc84d3) · [缺口 G-d0ca0274cf2c33d2](../../evidence/gaps-sets-007.md#g-d0ca0274cf2c33d2) · [参数 P-0e6575adb123ccfc](../../evidence/parameters-sets-002.md#p-0e6575adb123ccfc) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062640

```text
(config)# do-exec test platform software macsec tx sa delete an <number:0..3> <interface> <cr>
```

Handler ` RVA 0x160D7490 `；selector ` 34 `；EOL ` RVA 0x35ECD950 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` 0-3 association。

[条件 C-8e599aeb6134c931](../../evidence/conditions-sets-055.md#c-8e599aeb6134c931) · [缺口 G-e2ebf7c1f1a4d54d](../../evidence/gaps-sets-008.md#g-e2ebf7c1f1a4d54d) · [参数 P-b74f7ede1251bb1d](../../evidence/parameters-sets-014.md#p-b74f7ede1251bb1d) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062695

```text
(config)# do-exec test platform software macsec tx sa set mac-addr <address> vport <number:0..65535> an <number:0..3> pn <number:0..4294967295> confidence yes sak <string> length <number:0..4294967295> hash-key <string> <interface> <cr>
```

Handler ` RVA 0x160D7490 `；selector ` 33 `；EOL ` RVA 0x35ECD478 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` MAC address；` unsigned_number ` &lt;0-65535&gt; 16 bit port id；` unsigned_number ` 0-3 association；` unsigned_number ` 32 bit packet number；` string ` pre shared key；` unsigned_number ` SAK length；` string ` hash key (128 bit or 16 character)。

[条件 C-5a6c2ae95bb08e50](../../evidence/conditions-sets-035.md#c-5a6c2ae95bb08e50) · [缺口 G-539fb1e95aa3965d](../../evidence/gaps-sets-003.md#g-539fb1e95aa3965d) · [参数 P-de9006aee71b5e11](../../evidence/parameters-sets-017.md#p-de9006aee71b5e11) · [状态效果 S-413629416b35c4f2](../../evidence/state_effects-sets-014.md#s-413629416b35c4f2)

### path-062678

```text
(config)# do-exec test platform software macsec tx sc add mac-addr <address> vport <number:0..65535> <interface> <cr>
```

Handler ` RVA 0x160D7490 `；selector ` 23 `；EOL ` RVA 0x35ECCB90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` MAC address；` unsigned_number ` 16 bit port id。

[条件 C-00101ce0abd82203](../../evidence/conditions-sets-001.md#c-00101ce0abd82203) · [缺口 G-05038b7c1783bb47](../../evidence/gaps-sets-001.md#g-05038b7c1783bb47) · [参数 P-358e19e1a5cc21e5](../../evidence/parameters-sets-005.md#p-358e19e1a5cc21e5) · [状态效果 S-2d5a198cc5d6e036](../../evidence/state_effects-sets-010.md#s-2d5a198cc5d6e036)

### path-044490

```text
(config)# do-exec test platform software multicast join <cr>
```

Handler ` RVA 0xE6FA7C0 `；selector ` 1 `；EOL ` RVA 0x3430E098 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-044518

```text
(config)# do-exec test platform software multicast leave <cr>
```

Handler ` RVA 0xE6FA7C0 `；selector ` 2 `；EOL ` RVA 0x3430E340 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062654

```text
(config)# do-exec test platform software multicast parameters in igmp <interface> <address> <address> <number:1..500000> <cr>
```

Handler ` RVA 0xE6FA7C0 `；selector ` 5 `；EOL ` RVA 0x3430D5D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` IPv4 address for peer；` address ` Group IPv4 address；` unsigned_number ` grp count。

[条件 C-ad2401dd0fb55ebd](../../evidence/conditions-sets-067.md#c-ad2401dd0fb55ebd) · [缺口 G-c82d1ee6d0ed0a5c](../../evidence/gaps-sets-007.md#g-c82d1ee6d0ed0a5c) · [参数 P-494ffb635ff795f4](../../evidence/parameters-sets-006.md#p-494ffb635ff795f4) · [状态效果 S-26404f95bcbe5472](../../evidence/state_effects-sets-009.md#s-26404f95bcbe5472)

### path-062656

```text
(config)# do-exec test platform software multicast parameters in mld <interface> <address> <address> <number:1..500000> <cr>
```

Handler ` RVA 0xE6FA7C0 `；selector ` 5 `；EOL ` RVA 0x3430DAB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` IPv6 address for peer (must be linklocal address)；` address ` Group IPv6 address；` unsigned_number ` grp count。

[条件 C-ca6eb31cd92bc1b7](../../evidence/conditions-sets-078.md#c-ca6eb31cd92bc1b7) · [缺口 G-59bb43c19dc28393](../../evidence/gaps-sets-004.md#g-59bb43c19dc28393) · [参数 P-adde99e1afd051dd](../../evidence/parameters-sets-013.md#p-adde99e1afd051dd) · [状态效果 S-3ddba7ecdd070e32](../../evidence/state_effects-sets-014.md#s-3ddba7ecdd070e32)

### path-052426

```text
(config)# do-exec test platform software multicast shim dynamic <cr>
```

Handler ` RVA 0xE6FA7C0 `；selector ` 9 `；EOL ` RVA 0x3430C810 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-052455

```text
(config)# do-exec test platform software multicast shim notdl <cr>
```

Handler ` RVA 0xE6FA7C0 `；selector ` 10 `；EOL ` RVA 0x3430CAB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-052364

```text
(config)# do-exec test platform software multicast shim off <cr>
```

Handler ` RVA 0xE6FA7C0 `；selector ` 6 `；EOL ` RVA 0x3430C2C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-052325

```text
(config)# do-exec test platform software multicast shim on <cr>
```

Handler ` RVA 0xE6FA7C0 `；selector ` 7 `；EOL ` RVA 0x3430C018 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-052393

```text
(config)# do-exec test platform software multicast shim sticky <cr>
```

Handler ` RVA 0xE6FA7C0 `；selector ` 8 `；EOL ` RVA 0x3430C568 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-052483

```text
(config)# do-exec test platform software multicast shim tdl <cr>
```

Handler ` RVA 0xE6FA7C0 `；selector ` 11 `；EOL ` RVA 0x3430CD60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-044456

```text
(config)# do-exec test platform software multicast start <cr>
```

Handler ` RVA 0xE6FA7C0 `；selector ` 0 `；EOL ` RVA 0x3430DDF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-044393

```text
(config)# do-exec test platform software multicast status <cr>
```

Handler ` RVA 0xE6FA7C0 `；selector ` 4 `；EOL ` RVA 0x3430D028 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-044548

```text
(config)# do-exec test platform software multicast stop <cr>
```

Handler ` RVA 0xE6FA7C0 `；selector ` 3 `；EOL ` RVA 0x3430E5E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-044196

```text
(config)# do-exec test platform software peer timeout <cr>
```

Handler ` RVA 0xE9492B0 `；selector ` 0 `；EOL ` RVA 0x34350DB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-513be3046f6b3107](../../evidence/conditions-sets-032.md#c-513be3046f6b3107) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-052832

```text
(config)# do-exec test platform software plim qos class-map <cr>
```

Handler ` RVA 0xE93D510 `；selector ` 0 `；EOL ` RVA 0x3434D0F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-d8a0c2387bcbf6d4](../../evidence/state_effects-sets-046.md#s-d8a0c2387bcbf6d4)

### path-062260

```text
(config)# do-exec test platform software plim qos interface <interface> <cr>
```

Handler ` RVA 0xE93D510 `；selector ` 0 `；EOL ` RVA 0x3434D0F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0fb63b36015778a5](../../evidence/conditions-sets-006.md#c-0fb63b36015778a5) · [缺口 G-9b5c1bcd71990603](../../evidence/gaps-sets-006.md#g-9b5c1bcd71990603) · [参数 P-add3fa87332fcad1](../../evidence/parameters-sets-013.md#p-add3fa87332fcad1) · [状态效果 S-9a51aebb900b0f64](../../evidence/state_effects-sets-033.md#s-9a51aebb900b0f64)

### path-062485

```text
(config)# do-exec test platform software plim qos vlan-bmap-tbl subslot <?slotcard_func_action@5555898a15f0> <cr>
```

Handler ` RVA 0xE93D460 `；selector ` 0 `；EOL ` RVA 0x3434D630 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [缺口 G-782fd99b1cee3216](../../evidence/gaps-sets-005.md#g-782fd99b1cee3216) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-044701

```text
(config)# do-exec test platform software product-analytics fast-grace-period <cr>
```

Handler ` RVA 0x1658B060 `；selector ` 0 `；EOL ` RVA 0x35FA4068 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-34ff8707fac2e0b3](../../evidence/conditions-sets-021.md#c-34ff8707fac2e0b3) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-044602

```text
(config)# do-exec test platform software product-analytics sa-notify-false <cr>
```

Handler ` RVA 0x1658ADB0 `；selector ` 0 `；EOL ` RVA 0x35FA3B18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c42e7c95b62b9b3e](../../evidence/conditions-sets-076.md#c-c42e7c95b62b9b3e) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-044649

```text
(config)# do-exec test platform software product-analytics sa-notify-true <cr>
```

Handler ` RVA 0x1658AFD0 `；selector ` 0 `；EOL ` RVA 0x35FA3DC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f9c9154b2f7bc0c0](../../evidence/conditions-sets-096.md#c-f9c9154b2f7bc0c0) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-044746

```text
(config)# do-exec test platform software product-analytics timer <cr>
```

Handler ` RVA 0x1658B100 `；selector ` 0 `；EOL ` RVA 0x35FA4310 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ecda1560dcb00e7d](../../evidence/conditions-sets-091.md#c-ecda1560dcb00e7d) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-044175

```text
(config)# do-exec test platform software punt-keepalive ignore-fault <cr>
```

Handler ` RVA 0xEA60F20 `；selector ` 1 `；EOL ` RVA 0x3439C158 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-044214

```text
(config)# do-exec test platform software punt-keepalive trigger-failure <cr>
```

Handler ` RVA 0xEA60F20 `；selector ` 0 `；EOL ` RVA 0x3439C400 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-058984

```text
(config)# do-exec test platform software qos statistics <number:1..50000> <number:1..100000> <number:1..100> <cr>
```

Handler ` RVA 0x10DA0020 `；selector ` 1 `；EOL ` RVA 0x34D1B8C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` dpidx from sh pl so dbidx swidb；` unsigned_number ` num queries；` unsigned_number ` num of query in parallel。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [参数 P-65b36f41d2d9da61](../../evidence/parameters-sets-008.md#p-65b36f41d2d9da61) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-044412

```text
(config)# do-exec test platform software redundancy use-vmac <cr>
```

Handler ` RVA 0x15A6EA80 `；selector ` 0 `；EOL ` RVA 0x35DE5530 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-056988

```text
(config)# do-exec test platform software rg ar_alwys_dvrt <number:0..4> <number:0..12> <cr>
```

Handler ` RVA 0xE75D020 `；selector ` 7 `；EOL ` RVA 0x3432BC80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` action；` unsigned_number ` rg id。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [参数 P-4ffd42aa3d1d5e77](../../evidence/parameters-sets-007.md#p-4ffd42aa3d1d5e77) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062684

```text
(config)# do-exec test platform software rg interface <number:0..10> <interface> ar_intf <number:0..10> <address> <address> <number:0..10> <number:0..2048> <number:0..2048> <cr>
```

Handler ` RVA 0xE75D020 `；selector ` 9 `；EOL ` RVA 0x3432D688 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` action；` unsigned_number ` rg id；` address ` IPv4 src address；` address ` IPv4 dst address；` unsigned_number ` l4 protocol；` unsigned_number ` src port；` unsigned_number ` dst port。

[条件 C-399efc676d4f5f46](../../evidence/conditions-sets-022.md#c-399efc676d4f5f46) · [缺口 G-fee64ad37a0f2010](../../evidence/gaps-sets-009.md#g-fee64ad37a0f2010) · [参数 P-34f8a15207b22a8f](../../evidence/parameters-sets-005.md#p-34f8a15207b22a8f) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062477

```text
(config)# do-exec test platform software rg interface <number:0..10> <interface> ar_vi_intf_assoc <cr>
```

Handler ` RVA 0xE75D020 `；selector ` 8 `；EOL ` RVA 0x3432D248 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` action。

[条件 C-399efc676d4f5f46](../../evidence/conditions-sets-022.md#c-399efc676d4f5f46) · [缺口 G-fee64ad37a0f2010](../../evidence/gaps-sets-009.md#g-fee64ad37a0f2010) · [参数 P-2a7191613b999463](../../evidence/parameters-sets-004.md#p-2a7191613b999463) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062596

```text
(config)# do-exec test platform software rg interface <number:0..10> <interface> rg <number:0..10> <cr>
```

Handler ` RVA 0xE75D020 `；selector ` 4 `；EOL ` RVA 0x3432CCD0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` action；` unsigned_number ` rg id。

[条件 C-399efc676d4f5f46](../../evidence/conditions-sets-022.md#c-399efc676d4f5f46) · [缺口 G-fee64ad37a0f2010](../../evidence/gaps-sets-009.md#g-fee64ad37a0f2010) · [参数 P-946f87fe654a121b](../../evidence/parameters-sets-011.md#p-946f87fe654a121b) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062597

```text
(config)# do-exec test platform software rg interface <number:0..10> <interface> rii <number:0..16000> <cr>
```

Handler ` RVA 0xE75D020 `；selector ` 6 `；EOL ` RVA 0x3432CFC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` action；` unsigned_number ` rii id。

[条件 C-399efc676d4f5f46](../../evidence/conditions-sets-022.md#c-399efc676d4f5f46) · [缺口 G-fee64ad37a0f2010](../../evidence/gaps-sets-009.md#g-fee64ad37a0f2010) · [参数 P-8caa816559fc637b](../../evidence/parameters-sets-011.md#p-8caa816559fc637b) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-059004

```text
(config)# do-exec test platform software rg notify bulksync <number:0..10> <number:0..10> <cr>
```

Handler ` RVA 0xE75D020 `；selector ` 2 `；EOL ` RVA 0x3432C378 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` rg id；` unsigned_number ` result。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [参数 P-5e3b6cf8076791cc](../../evidence/parameters-sets-008.md#p-5e3b6cf8076791cc) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-059677

```text
(config)# do-exec test platform software rg notify transport <number:0..10> <number:1..100000> <number:0..10> <cr>
```

Handler ` RVA 0xE75D020 `；selector ` 1 `；EOL ` RVA 0x3432C068 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` rg id；` unsigned_number ` handler；` unsigned_number ` state。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [参数 P-769bf5d82d2ae140](../../evidence/parameters-sets-009.md#p-769bf5d82d2ae140) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-060136

```text
(config)# do-exec test platform software rg services parameters <number:0..10> <number:0..10> <number:0..10> <number:0..1> <number:0..1> <cr>
```

Handler ` RVA 0xE75D020 `；selector ` 0 `；EOL ` RVA 0x3432B938 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` action；` unsigned_number ` rg id；` unsigned_number ` rg state；` unsigned_number ` transport request；` unsigned_number ` bulk sync request。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [参数 P-7c5e56bce406174a](../../evidence/parameters-sets-010.md#p-7c5e56bce406174a) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-044748

```text
(config)# do-exec test platform software rg tc-req <cr>
```

Handler ` RVA 0xE75D020 `；selector ` 5 `；EOL ` RVA 0x3432D980 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-060215

```text
(config)# do-exec test platform software rg transport parameters <number:1..100000> <number:0..10> <address> <address> <number:0..10> <number:0..2048> <number:0..2048> <cr>
```

Handler ` RVA 0xE75D020 `；selector ` 3 `；EOL ` RVA 0x3432C860 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` handler；` unsigned_number ` application；` address ` IPv4 src address；` address ` IPv4 dst address；` unsigned_number ` l4 protocol；` unsigned_number ` src port；` unsigned_number ` dst port。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [参数 P-82c662ee053c7586](../../evidence/parameters-sets-010.md#p-82c662ee053c7586) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062476

```text
(config)# do-exec test platform software shell command connection <number:dynamic> disconnect <cr>
```

Handler ` RVA 0xEB0CD80 `；selector ` 0 `；EOL ` RVA 0x343B1E40 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Connection number。

[条件 C-fe6bb876f3fc7692](../../evidence/conditions-sets-098.md#c-fe6bb876f3fc7692) · [缺口 G-1d711ad5d63397b8](../../evidence/gaps-sets-001.md#g-1d711ad5d63397b8) · [参数 P-71f354a74f64b80b](../../evidence/parameters-sets-009.md#p-71f354a74f64b80b) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-059031

```text
(config)# do-exec test platform software shell command handler automore disable <cr>
```

Handler ` RVA 0xEB0C800 `；selector ` 0 `；EOL ` RVA 0x343B1310 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-059022

```text
(config)# do-exec test platform software shell command handler automore manual <cr>
```

Handler ` RVA 0xEB0C900 `；selector ` 0 `；EOL ` RVA 0x343B1068 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-057041

```text
(config)# do-exec test platform software shell command handler basic <cr>
```

Handler ` RVA 0xEB0C720 `；selector ` 0 `；EOL ` RVA 0x343B15A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-057053

```text
(config)# do-exec test platform software shell command handler null <cr>
```

Handler ` RVA 0xEB0C640 `；selector ` 0 `；EOL ` RVA 0x343B1850 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-059015

```text
(config)# do-exec test platform software shell command handler output redirect <cr>
```

Handler ` RVA 0xEB0CA90 `；selector ` 0 `；EOL ` RVA 0x343B0D70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-057064

```text
(config)# do-exec test platform software shell command handler space <cr>
```

Handler ` RVA 0xEB0C560 `；selector ` 0 `；EOL ` RVA 0x343B1AF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-057020

```text
(config)# do-exec test platform software shell command set delete <cr>
```

Handler ` RVA 0xEB0CD30 `；selector ` 0 `；EOL ` RVA 0x343B0A08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-057016

```text
(config)# do-exec test platform software shell command set load <cr>
```

Handler ` RVA 0xEB0CCE0 `；selector ` 0 `；EOL ` RVA 0x343B0760 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-056790

```text
(config)# do-exec test platform software stdout log running-config enable <cr>
```

Handler ` RVA 0xE950340 `；selector ` 0 `；EOL ` RVA 0x34351DA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cd45860aeb890184](../../evidence/conditions-sets-079.md#c-cd45860aeb890184) · [状态效果 S-5f2efda7471a4d77](../../evidence/state_effects-sets-020.md#s-5f2efda7471a4d77)

### path-052350

```text
(config)# do-exec test platform software tdl ping rp <cr>
```

Handler ` RVA 0xE90CE60 `；selector ` 0 `；EOL ` RVA 0x343432E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-805256a98e774e10](../../evidence/conditions-sets-050.md#c-805256a98e774e10) · [状态效果 S-7904eeb04e48607d](../../evidence/state_effects-sets-026.md#s-7904eeb04e48607d)

### path-056861

```text
(config)# do-exec test platform software tdl ping rp stats <cr>
```

Handler ` RVA 0xE90F1B0 `；selector ` 0 `；EOL ` RVA 0x34343800 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-805256a98e774e10](../../evidence/conditions-sets-050.md#c-805256a98e774e10) · [状态效果 S-7904eeb04e48607d](../../evidence/state_effects-sets-026.md#s-7904eeb04e48607d)

### path-058923

```text
(config)# do-exec test platform software tdl ping rp stats clear <cr>
```

Handler ` RVA 0xE90F090 `；selector ` 0 `；EOL ` RVA 0x343437D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-805256a98e774e10](../../evidence/conditions-sets-050.md#c-805256a98e774e10) · [状态效果 S-7904eeb04e48607d](../../evidence/state_effects-sets-026.md#s-7904eeb04e48607d)

### path-062243

```text
(config)# do-exec test platform software tdl ping subslot <?slotcard_func_action@555589897d40> <cr>
```

Handler ` RVA 0xE90CE60 `；selector ` 0 `；EOL ` RVA 0x343432E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-661249edac55d539](../../evidence/conditions-sets-039.md#c-661249edac55d539) · [缺口 G-217d0a7de67c3a33](../../evidence/gaps-sets-002.md#g-217d0a7de67c3a33) · [状态效果 S-ea101cf9a3fff254](../../evidence/state_effects-sets-050.md#s-ea101cf9a3fff254)

### path-062469

```text
(config)# do-exec test platform software tdl ping subslot <?slotcard_func_action@555589897d40> stats <cr>
```

Handler ` RVA 0xE90F1B0 `；selector ` 0 `；EOL ` RVA 0x34343800 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-661249edac55d539](../../evidence/conditions-sets-039.md#c-661249edac55d539) · [缺口 G-217d0a7de67c3a33](../../evidence/gaps-sets-002.md#g-217d0a7de67c3a33) · [状态效果 S-ea101cf9a3fff254](../../evidence/state_effects-sets-050.md#s-ea101cf9a3fff254)

### path-062591

```text
(config)# do-exec test platform software tdl ping subslot <?slotcard_func_action@555589897d40> stats clear <cr>
```

Handler ` RVA 0xE90F090 `；selector ` 0 `；EOL ` RVA 0x343437D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-661249edac55d539](../../evidence/conditions-sets-039.md#c-661249edac55d539) · [缺口 G-217d0a7de67c3a33](../../evidence/gaps-sets-002.md#g-217d0a7de67c3a33) · [状态效果 S-ea101cf9a3fff254](../../evidence/state_effects-sets-050.md#s-ea101cf9a3fff254)

### path-062594

```text
(config)# do-exec test platform software timestamp-engine oam y1731 default disable <interface> <cr>
```

Handler ` RVA 0x15A9EA30 `；selector ` 3 `；EOL ` RVA 0x35DE75F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-878cb62907a00d86](../../evidence/conditions-sets-052.md#c-878cb62907a00d86) · [缺口 G-a391e1e42775fa9f](../../evidence/gaps-sets-006.md#g-a391e1e42775fa9f) · [参数 P-5cde95e6de438324](../../evidence/parameters-sets-007.md#p-5cde95e6de438324) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-059681

```text
(config)# do-exec test platform software timestamp-engine oam y1731 default disable all <cr>
```

Handler ` RVA 0x15A9EA30 `；selector ` 4 `；EOL ` RVA 0x35DE78A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff0158eefc867b95](../../evidence/conditions-sets-098.md#c-ff0158eefc867b95) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062593

```text
(config)# do-exec test platform software timestamp-engine oam y1731 default enable <interface> <cr>
```

Handler ` RVA 0x15A9EA30 `；selector ` 1 `；EOL ` RVA 0x35DE6FC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2b5ef25472ef4557](../../evidence/conditions-sets-017.md#c-2b5ef25472ef4557) · [缺口 G-00a913919e724e19](../../evidence/gaps-sets-001.md#g-00a913919e724e19) · [参数 P-1ccc1d5f4b9219b8](../../evidence/parameters-sets-003.md#p-1ccc1d5f4b9219b8) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-059675

```text
(config)# do-exec test platform software timestamp-engine oam y1731 default enable all <cr>
```

Handler ` RVA 0x15A9EA30 `；selector ` 2 `；EOL ` RVA 0x35DE7268 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3a063ed786e14f24](../../evidence/conditions-sets-022.md#c-3a063ed786e14f24) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062635

```text
(config)# do-exec test platform software timestamp-engine ptp clock-domain <number:0..255> ip <address> <interface> <cr>
```

Handler ` RVA 0x15A9EA30 `；selector ` 0 `；EOL ` RVA 0x35DE6B18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` clk domain；` address ` IPv4 address。

[条件 C-b349432570072042](../../evidence/conditions-sets-069.md#c-b349432570072042) · [缺口 G-1fc38f152d5663e4](../../evidence/gaps-sets-002.md#g-1fc38f152d5663e4) · [参数 P-0c109254b97f8ff6](../../evidence/parameters-sets-001.md#p-0c109254b97f8ff6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062657

```text
(config)# do-exec test platform software timestamp-engine tod load sec-hi <number:0..65535> sec-lo <number:0..4294967295> <interface> <cr>
```

Handler ` RVA 0x15A9EA30 `；selector ` 5 `；EOL ` RVA 0x35DE7DB0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Upper 16 bits of seconds from epoch；` unsigned_number ` Upper 32 bits of seconds from epoch。

[条件 C-992c2e25b17e29a1](../../evidence/conditions-sets-059.md#c-992c2e25b17e29a1) · [缺口 G-40ae7ad6b9fdd093](../../evidence/gaps-sets-003.md#g-40ae7ad6b9fdd093) · [参数 P-33b87f8f71142462](../../evidence/parameters-sets-004.md#p-33b87f8f71142462) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-052717

```text
(config)# do-exec test platform software uidp batch-count <number:0..1000> <cr>
```

Handler ` RVA 0x1599CE30 `；selector ` 0 `；EOL ` RVA 0x35DCF728 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of user sessions per batch。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [参数 P-7c336c4b98660031](../../evidence/parameters-sets-010.md#p-7c336c4b98660031) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-052706

```text
(config)# do-exec test platform software uidp binding clear <cr>
```

Handler ` RVA 0x1599C3F0 `；selector ` 0 `；EOL ` RVA 0x35DCEE38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-059982

```text
(config)# do-exec test platform software uidp binding ip-user add <address> <number:0..4294967295> <string> <cr>
```

Handler ` RVA 0x1599C4A0 `；selector ` 0 `；EOL ` RVA 0x35DCE1B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IPv4 Address；` unsigned_number ` VPN ID；` string ` User name。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [参数 P-168aba61599d0180](../../evidence/parameters-sets-002.md#p-168aba61599d0180) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-059984

```text
(config)# do-exec test platform software uidp binding ip-user delete <address> <number:0..4294967295> <string> <cr>
```

Handler ` RVA 0x1599C4A0 `；selector ` 1 `；EOL ` RVA 0x35DCE4F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IPv4 Address；` unsigned_number ` VPN ID；` string ` User name。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [参数 P-82cd5055a6ddb96f](../../evidence/parameters-sets-010.md#p-82cd5055a6ddb96f) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-059044

```text
(config)# do-exec test platform software uidp binding user-usergroup add <string> <cr>
```

Handler ` RVA 0x1599C7F0 `；selector ` 2 `；EOL ` RVA 0x35DCE8A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` User name。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [参数 P-12f4f3bbd76a04fe](../../evidence/parameters-sets-002.md#p-12f4f3bbd76a04fe) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-059049

```text
(config)# do-exec test platform software uidp binding user-usergroup delete <string> <cr>
```

Handler ` RVA 0x1599C7F0 `；selector ` 3 `；EOL ` RVA 0x35DCEBA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` User name。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [参数 P-1defe1bf1a446589](../../evidence/parameters-sets-003.md#p-1defe1bf1a446589) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-052731

```text
(config)# do-exec test platform software uidp dwnld-timer <number:100..2000> <cr>
```

Handler ` RVA 0x1599CEA0 `；selector ` 0 `；EOL ` RVA 0x35DCF9F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Pause time for downloading batch of sessions。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [参数 P-72b2461fd4b2a57e](../../evidence/parameters-sets-009.md#p-72b2461fd4b2a57e) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061872

```text
(config)# do-exec test platform software uidp load-file <url:dynamic> <cr>
```

Handler ` RVA 0x1599B640 `；selector ` 0 `；EOL ` RVA 0x35DCDD58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-76f0d1dd0c88f7a5](../../evidence/conditions-sets-046.md#c-76f0d1dd0c88f7a5) · [缺口 G-19dfe392d297c07f](../../evidence/gaps-sets-001.md#g-19dfe392d297c07f) · [参数 P-bdaadc3b21fb155e](../../evidence/parameters-sets-014.md#p-bdaadc3b21fb155e) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-052679

```text
(config)# do-exec test platform software uidp user <string> <cr>
```

Handler ` RVA 0x1599CCD0 `；selector ` 4 `；EOL ` RVA 0x35DCF150 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` User name。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [参数 P-0fa27b7ec79838bd](../../evidence/parameters-sets-002.md#p-0fa27b7ec79838bd) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-052697

```text
(config)# do-exec test platform software uidp user-group <string> <cr>
```

Handler ` RVA 0x1599CD80 `；selector ` 5 `；EOL ` RVA 0x35DCF440 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` User group name。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [参数 P-a9f2b7b5d4e2e4fa](../../evidence/parameters-sets-013.md#p-a9f2b7b5d4e2e4fa) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-059059

```text
(config)# do-exec test platform software usb slot <number:1..4294967295> usbflash0 fake-remove <cr>
```

Handler ` RVA 0xE9C72A0 `；selector ` 0 `；EOL ` RVA 0x3437C7F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` slot/switch Number。

[条件 C-a37c5dd4ddfec3d9](../../evidence/conditions-sets-063.md#c-a37c5dd4ddfec3d9) · [参数 P-8880f5ca265b7b86](../../evidence/parameters-sets-011.md#p-8880f5ca265b7b86) · [状态效果 S-33821120cb13f372](../../evidence/state_effects-sets-011.md#s-33821120cb13f372)

### path-031834

```text
(config)# do-exec test pm <string> <cr>
```

Handler ` RVA 0x15DD1600 `；selector ` 0 `；EOL ` RVA 0x35E22898 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` ...。

[条件 C-8cbb5653d1027960](../../evidence/conditions-sets-054.md#c-8cbb5653d1027960) · [参数 P-bc02e5e87b3d0fdc](../../evidence/parameters-sets-014.md#p-bc02e5e87b3d0fdc) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061537

```text
(config)# do-exec test pm error <interface> none <cr>
```

Handler ` RVA 0x15DD1740 `；selector ` 0 `；EOL ` RVA 0x35E22170 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5f579f6b72c86fb5](../../evidence/conditions-sets-037.md#c-5f579f6b72c86fb5) · [缺口 G-e7c06410305acf2f](../../evidence/gaps-sets-008.md#g-e7c06410305acf2f) · [参数 P-f52bb39e2fab6521](../../evidence/parameters-sets-018.md#p-f52bb39e2fab6521) · [状态效果 S-c2e08db6ac70d78a](../../evidence/state_effects-sets-041.md#s-c2e08db6ac70d78a)

### path-039093

```text
(config)# do-exec test policy-manager appl-event create <cr>
```

Handler ` RVA 0xE110C00 `；selector ` 0 `；EOL ` RVA 0x34205BA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2f1913a29079355a](../../evidence/conditions-sets-018.md#c-2f1913a29079355a) · [状态效果 S-f9b2284cd298eccc](../../evidence/state_effects-sets-053.md#s-f9b2284cd298eccc)

### path-039150

```text
(config)# do-exec test policy-manager wd-timer-event create <cr>
```

Handler ` RVA 0xE110C00 `；selector ` 0 `；EOL ` RVA 0x34205F40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-202d71370fb84be8](../../evidence/conditions-sets-013.md#c-202d71370fb84be8) · [状态效果 S-c204029f27f80f12](../../evidence/state_effects-sets-041.md#s-c204029f27f80f12)

### path-061226

```text
(config)# do-exec test ppp packet <interface> <string> <cr>
```

Handler ` RVA 0xFEDEDA0 `；selector ` 0 `；EOL ` RVA 0x34909C38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-bf8577b3f04ddd51](../../evidence/conditions-sets-074.md#c-bf8577b3f04ddd51) · [缺口 G-639070fd7e588553](../../evidence/gaps-sets-004.md#g-639070fd7e588553) · [参数 P-35b51fbb7a8e5629](../../evidence/parameters-sets-005.md#p-35b51fbb7a8e5629) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061222

```text
(config)# do-exec test ppp packet <interface> echo <cr>
```

Handler ` RVA 0xFEDEDA0 `；selector ` 1 `；EOL ` RVA 0x34909930 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-dbc906a6e78bcdde](../../evidence/conditions-sets-085.md#c-dbc906a6e78bcdde) · [缺口 G-639070fd7e588553](../../evidence/gaps-sets-004.md#g-639070fd7e588553) · [参数 P-d6f9f077cb6da492](../../evidence/parameters-sets-016.md#p-d6f9f077cb6da492) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-060067

```text
(config)# do-exec test pppatm subscriber delay <number:0..30000> <number:0..30000> <number:0..30000> <number:0..30000> <number:0..30000> <number:0..30000> <cr>
```

Handler ` RVA 0x1111E220 `；selector ` 0 `；EOL ` RVA 0x35401D68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` msecs. for subscriber msgs；` unsigned_number ` msecs. for ppp msgs；` unsigned_number ` msecs. for peer msgs；` unsigned_number ` msecs. for feature msgs；` unsigned_number ` msecs. for incoming calls；` unsigned_number ` msecs. for vaccess。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-9a76ee1c5bfa38c4](../../evidence/parameters-sets-012.md#p-9a76ee1c5bfa38c4) · [状态效果 S-e3131ffcb405142c](../../evidence/state_effects-sets-048.md#s-e3131ffcb405142c)

### path-062002

```text
(config)# do-exec test pppatm subscriber normal interface <interface> <cr>
```

Handler ` RVA 0x1111E220 `；selector ` 0 `；EOL ` RVA 0x35401D68 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-369911a95432233d](../../evidence/conditions-sets-021.md#c-369911a95432233d) · [缺口 G-51fba122ca367221](../../evidence/gaps-sets-003.md#g-51fba122ca367221) · [参数 P-b9f7c416d8d36dab](../../evidence/parameters-sets-014.md#p-b9f7c416d8d36dab) · [状态效果 S-e92df4b95772b90e](../../evidence/state_effects-sets-049.md#s-e92df4b95772b90e)

### path-027530

```text
(config)# do-exec test pppoe <cr>
```

Handler ` RVA 0x11CB06C0 `；selector ` 0 `；EOL ` RVA 0x356B32E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-97df2039620011a4](../../evidence/state_effects-sets-032.md#s-97df2039620011a4)

### path-060689

```text
(config)# do-exec test pppoe <number:dynamic> <cr>
```

Handler ` RVA 0x11CB06C0 `；selector ` 0 `；EOL ` RVA 0x356B32E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Number of PPPoE sessions to be opened。

[条件 C-b941ad68da58d599](../../evidence/conditions-sets-072.md#c-b941ad68da58d599) · [缺口 G-b33c5386ae50588d](../../evidence/gaps-sets-006.md#g-b33c5386ae50588d) · [参数 P-cb85bb7f12418403](../../evidence/parameters-sets-015.md#p-cb85bb7f12418403) · [状态效果 S-97df2039620011a4](../../evidence/state_effects-sets-032.md#s-97df2039620011a4)

### path-037734

```text
(config)# do-exec test pppoe init-session-num <number:1..65535> <cr>
```

Handler ` RVA 0x11CB06C0 `；selector ` 12 `；EOL ` RVA 0x356B3650 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Starting PPPoE Session Number。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-465592a267d1213c](../../evidence/parameters-sets-006.md#p-465592a267d1213c) · [状态效果 S-83afe854cecf184e](../../evidence/state_effects-sets-028.md#s-83afe854cecf184e)

### path-047250

```text
(config)# do-exec test pppoe session <number:1..20000> autogrant <cr>
```

Handler ` RVA 0x11CB0650 `；selector ` 2 `；EOL ` RVA 0x356B48A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` PPPoE Session Number to touch。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-7b01c122e4339bfe](../../evidence/parameters-sets-010.md#p-7b01c122e4339bfe) · [状态效果 S-83afe854cecf184e](../../evidence/state_effects-sets-028.md#s-83afe854cecf184e)

### path-054335

```text
(config)# do-exec test pppoe session <number:1..20000> autogrant on <cr>
```

Handler ` RVA 0x11CB0650 `；selector ` 1 `；EOL ` RVA 0x356B45F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` PPPoE Session Number to touch。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-7b01c122e4339bfe](../../evidence/parameters-sets-010.md#p-7b01c122e4339bfe) · [状态效果 S-83afe854cecf184e](../../evidence/state_effects-sets-028.md#s-83afe854cecf184e)

### path-054381

```text
(config)# do-exec test pppoe session <number:1..20000> grant-threshold <number:0..65534> <cr>
```

Handler ` RVA 0x11CB0650 `；selector ` 6 `；EOL ` RVA 0x356B56E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` PPPoE Session Number to touch；` unsigned_number ` Set grant credit unit threshold 。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-c52715e3f07536be](../../evidence/parameters-sets-015.md#p-c52715e3f07536be) · [状态效果 S-83afe854cecf184e](../../evidence/state_effects-sets-028.md#s-83afe854cecf184e)

### path-047209

```text
(config)# do-exec test pppoe session <number:1..20000> headDropping <cr>
```

Handler ` RVA 0x11CB0650 `；selector ` 16 `；EOL ` RVA 0x356B3D50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` PPPoE Session Number to touch。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-7b01c122e4339bfe](../../evidence/parameters-sets-010.md#p-7b01c122e4339bfe) · [状态效果 S-83afe854cecf184e](../../evidence/state_effects-sets-028.md#s-83afe854cecf184e)

### path-054311

```text
(config)# do-exec test pppoe session <number:1..20000> headDropping on <cr>
```

Handler ` RVA 0x11CB0650 `；selector ` 15 `；EOL ` RVA 0x356B3AA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` PPPoE Session Number to touch。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-7b01c122e4339bfe](../../evidence/parameters-sets-010.md#p-7b01c122e4339bfe) · [状态效果 S-83afe854cecf184e](../../evidence/state_effects-sets-028.md#s-83afe854cecf184e)

### path-047224

```text
(config)# do-exec test pppoe session <number:1..20000> inband-credits <cr>
```

Handler ` RVA 0x11CB0650 `；selector ` 14 `；EOL ` RVA 0x356B42F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` PPPoE Session Number to touch。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-7b01c122e4339bfe](../../evidence/parameters-sets-010.md#p-7b01c122e4339bfe) · [状态效果 S-83afe854cecf184e](../../evidence/state_effects-sets-028.md#s-83afe854cecf184e)

### path-054324

```text
(config)# do-exec test pppoe session <number:1..20000> inband-credits on <cr>
```

Handler ` RVA 0x11CB0650 `；selector ` 13 `；EOL ` RVA 0x356B4050 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` PPPoE Session Number to touch。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-7b01c122e4339bfe](../../evidence/parameters-sets-010.md#p-7b01c122e4339bfe) · [状态效果 S-83afe854cecf184e](../../evidence/state_effects-sets-028.md#s-83afe854cecf184e)

### path-054420

```text
(config)# do-exec test pppoe session <number:1..20000> local-credits <number:0..65535> <cr>
```

Handler ` RVA 0x11CB0650 `；selector ` 10 `；EOL ` RVA 0x356B5CC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` PPPoE Session Number to touch；` unsigned_number ` local credits。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-1eb21824c744cc30](../../evidence/parameters-sets-003.md#p-1eb21824c744cc30) · [状态效果 S-83afe854cecf184e](../../evidence/state_effects-sets-028.md#s-83afe854cecf184e)

### path-054360

```text
(config)# do-exec test pppoe session <number:1..20000> max-grant <number:0..65535> <cr>
```

Handler ` RVA 0x11CB0650 `；selector ` 5 `；EOL ` RVA 0x356B53F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` PPPoE Session Number to touch；` unsigned_number ` Set maximum number of credit units per grant。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-513dc72ce2a78132](../../evidence/parameters-sets-007.md#p-513dc72ce2a78132) · [状态效果 S-83afe854cecf184e](../../evidence/state_effects-sets-028.md#s-83afe854cecf184e)

### path-054384

```text
(config)# do-exec test pppoe session <number:1..20000> padg <number:1..65535> <cr>
```

Handler ` RVA 0x11CB0650 `；selector ` 7 `；EOL ` RVA 0x356B50F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` PPPoE Session Number to touch；` unsigned_number ` Number of PPPoE credit units to grant。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-18fe21eb467de39c](../../evidence/parameters-sets-002.md#p-18fe21eb467de39c) · [状态效果 S-83afe854cecf184e](../../evidence/state_effects-sets-028.md#s-83afe854cecf184e)

### path-054365

```text
(config)# do-exec test pppoe session <number:1..20000> padg off <cr>
```

Handler ` RVA 0x11CB0650 `；selector ` 3 `；EOL ` RVA 0x356B4E48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` PPPoE Session Number to touch。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-7b01c122e4339bfe](../../evidence/parameters-sets-010.md#p-7b01c122e4339bfe) · [状态效果 S-83afe854cecf184e](../../evidence/state_effects-sets-028.md#s-83afe854cecf184e)

### path-054343

```text
(config)# do-exec test pppoe session <number:1..20000> padg on <cr>
```

Handler ` RVA 0x11CB0650 `；selector ` 4 `；EOL ` RVA 0x356B4BA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` PPPoE Session Number to touch。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-7b01c122e4339bfe](../../evidence/parameters-sets-010.md#p-7b01c122e4339bfe) · [状态效果 S-83afe854cecf184e](../../evidence/state_effects-sets-028.md#s-83afe854cecf184e)

### path-054556

```text
(config)# do-exec test pppoe session <number:1..20000> padq receive-only <cr>
```

Handler ` RVA 0x11CB0650 `；selector ` 8 `；EOL ` RVA 0x356B6218 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` PPPoE Session Number to touch。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-7b01c122e4339bfe](../../evidence/parameters-sets-010.md#p-7b01c122e4339bfe) · [状态效果 S-baad625ebf44cb60](../../evidence/state_effects-sets-039.md#s-baad625ebf44cb60)

### path-054403

```text
(config)# do-exec test pppoe session <number:1..20000> peer-credits <number:0..65535> <cr>
```

Handler ` RVA 0x11CB0650 `；selector ` 9 `；EOL ` RVA 0x356B59D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` PPPoE Session Number to touch；` unsigned_number ` local credit units。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-cec15d709fc4fb0a](../../evidence/parameters-sets-016.md#p-cec15d709fc4fb0a) · [状态效果 S-83afe854cecf184e](../../evidence/state_effects-sets-028.md#s-83afe854cecf184e)

### path-052126

```text
(config)# do-exec test process create <number:1..5000> <number:1..10000> <number:1..5000> <cr>
```

Handler ` RVA 0xD6D2550 `；selector ` 0 `；EOL ` RVA 0x33ECDDE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Enter time to run for (ms)；` unsigned_number ` Enter time to sleep for (ms)；` unsigned_number ` Enter time to susp after (ms)。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-f57e4b11ecf3ba88](../../evidence/parameters-sets-018.md#p-f57e4b11ecf3ba88) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-034298

```text
(config)# do-exec test process kill <number:1..4294967295> <cr>
```

Handler ` RVA 0xD6D2A10 `；selector ` 0 `；EOL ` RVA 0x33ECE140 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Pid to kill。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-cca3915cfbc7547d](../../evidence/parameters-sets-016.md#p-cca3915cfbc7547d) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-027598

```text
(config)# do-exec test rfd <cr>
```

Handler ` RVA 0xD7C53C0 `；selector ` 0 `；EOL ` RVA 0x33EF4C90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-be2db87780940846](../../evidence/conditions-sets-073.md#c-be2db87780940846) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-046792

```text
(config)# do-exec test rib application create <string> <cr>
```

Handler ` RVA 0xDC0CAC0 `；selector ` 5 `；EOL ` RVA 0x3400B460 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Application instance name。

[条件 C-04b8fa829f79145d](../../evidence/conditions-sets-002.md#c-04b8fa829f79145d) · [参数 P-44a7689de98431a1](../../evidence/parameters-sets-006.md#p-44a7689de98431a1) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-046750

```text
(config)# do-exec test rib application delete <number:0..65535> <cr>
```

Handler ` RVA 0xDC0CAC0 `；selector ` 6 `；EOL ` RVA 0x3400B198 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` handle number。

[条件 C-04b8fa829f79145d](../../evidence/conditions-sets-002.md#c-04b8fa829f79145d) · [参数 P-84485f3ce4166b87](../../evidence/parameters-sets-010.md#p-84485f3ce4166b87) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-046656

```text
(config)# do-exec test rib client create <string> <cr>
```

Handler ` RVA 0xDC0CAC0 `；selector ` 0 `；EOL ` RVA 0x34009A60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Client name。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-6fbb31bff7eebb42](../../evidence/parameters-sets-009.md#p-6fbb31bff7eebb42) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-046522

```text
(config)# do-exec test rib client delete <number:1..2147483647> <cr>
```

Handler ` RVA 0xDC0CAC0 `；selector ` 1 `；EOL ` RVA 0x34009758 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` handle number。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-61bebf93f1ef1e6e](../../evidence/parameters-sets-008.md#p-61bebf93f1ef1e6e) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-046843

```text
(config)# do-exec test rib firsthop <address> <number:0..65535> <cr>
```

Handler ` RVA 0xDC0CAC0 `；selector ` 7 `；EOL ` RVA 0x3400AE20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` destination address；` unsigned_number ` Multipath path select index。

[条件 C-c2292911a7e8bfe1](../../evidence/conditions-sets-075.md#c-c2292911a7e8bfe1) · [参数 P-adbd895aad18df4d](../../evidence/parameters-sets-013.md#p-adbd895aad18df4d) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061990

```text
(config)# do-exec test rib firsthop <address> <number:0..65535> <interface> <cr>
```

Handler ` RVA 0xDC0CAC0 `；selector ` 7 `；EOL ` RVA 0x3400AE20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` destination address；` unsigned_number ` Multipath path select index。

[条件 C-159e46cdc9b79386](../../evidence/conditions-sets-009.md#c-159e46cdc9b79386) · [缺口 G-f83c84aa036ace52](../../evidence/gaps-sets-009.md#g-f83c84aa036ace52) · [参数 P-e378a7c7d30f8d22](../../evidence/parameters-sets-017.md#p-e378a7c7d30f8d22) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062903

```text
(config)# do-exec test rib route delete <number:1..2147483647> <?router_action_proc_vpn@55558955e160> <interface> <cr>
```

Handler ` RVA 0xDC0CAC0 `；selector ` 2 `；EOL ` RVA 0x3400A250 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` handle number。

[条件 C-5b25c9e07a1f2056](../../evidence/conditions-sets-036.md#c-5b25c9e07a1f2056) · [缺口 G-de012a9bc4214c67](../../evidence/gaps-sets-008.md#g-de012a9bc4214c67) · [参数 P-be2bb44230acb3b7](../../evidence/parameters-sets-014.md#p-be2bb44230acb3b7) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-046673

```text
(config)# do-exec test rib route show <number:1..2147483647> <cr>
```

Handler ` RVA 0xDC0CAC0 `；selector ` 3 `；EOL ` RVA 0x3400A550 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` handle number。

[条件 C-04b8fa829f79145d](../../evidence/conditions-sets-002.md#c-04b8fa829f79145d) · [参数 P-8d99215107ac3986](../../evidence/parameters-sets-011.md#p-8d99215107ac3986) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-046709

```text
(config)# do-exec test rib table set forwarding-base <cr>
```

Handler ` RVA 0xDC0CAC0 `；selector ` 4 `；EOL ` RVA 0x3400A950 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-04b8fa829f79145d](../../evidence/conditions-sets-002.md#c-04b8fa829f79145d) · [状态效果 S-0dba2167aab4219d](../../evidence/state_effects-sets-003.md#s-0dba2167aab4219d)

### path-030568

```text
(config)# do-exec test rib ut <cr>
```

Handler ` RVA 0xDC0CAC0 `；selector ` 8 `；EOL ` RVA 0x34009DE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ea981e0e12eb7a51](../../evidence/conditions-sets-091.md#c-ea981e0e12eb7a51) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-048150

```text
(config)# do-exec test rmi create user-type <string> <cr>
```

Handler ` RVA 0xE081680 `；selector ` 0 `；EOL ` RVA 0x341D60C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Resource User-Type Name。

[条件 C-0b0b6e41a17a8c06](../../evidence/conditions-sets-005.md#c-0b0b6e41a17a8c06) · [参数 P-71c7f62eb30da67d](../../evidence/parameters-sets-009.md#p-71c7f62eb30da67d) · [状态效果 S-10e302ef8800c5a2](../../evidence/state_effects-sets-004.md#s-10e302ef8800c5a2)

### path-031687

```text
(config)# do-exec test rmi entphyind <cr>
```

Handler ` RVA 0xD695F20 `；selector ` 0 `；EOL ` RVA 0x341D7518 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-059395

```text
(config)# do-exec test rmon hc-alarms <number:1..65535> Low32bitvalue <number:0..4294967295> High32bitvalue <number:0..4294967295> <cr>
```

Handler ` RVA 0xC4F9D90 `；selector ` 0 `；EOL ` RVA 0x33AADCE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Hc alarm index；` unsigned_number ` Low32bitvalue；` unsigned_number ` High32bitvalue。

[条件 C-716d9d144a297e82](../../evidence/conditions-sets-044.md#c-716d9d144a297e82) · [参数 P-88ec7857607f280e](../../evidence/parameters-sets-011.md#p-88ec7857607f280e) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062523

```text
(config)# do-exec test rsvp lockout psb <number:0..4294967295> set interface <interface> <cr>
```

Handler ` RVA 0x10078C60 `；selector ` 0 `；EOL ` RVA 0x34A3F910 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` PSB handle for lockout in hex。

[条件 C-040cf3d3021f70e7](../../evidence/conditions-sets-002.md#c-040cf3d3021f70e7) · [缺口 G-678b1c17d3c60157](../../evidence/gaps-sets-004.md#g-678b1c17d3c60157) · [参数 P-a7e66a588bfa8991](../../evidence/parameters-sets-013.md#p-a7e66a588bfa8991) · [状态效果 S-66770781ef9ba747](../../evidence/state_effects-sets-022.md#s-66770781ef9ba747)

### path-059847

```text
(config)# do-exec test rsvp metadata forward <address> <address> <number:0..255> <number:0..65535> <number:0..65535> <cr>
```

Handler ` RVA 0x100784A0 `；selector ` 0 `；EOL ` RVA 0x34A3F398 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Destination address；` address ` Source address；` unsigned_number ` IP Protocol；` unsigned_number ` Destination port；` unsigned_number ` Source port。

[条件 C-44e300ba87708e67](../../evidence/conditions-sets-027.md#c-44e300ba87708e67) · [参数 P-164d4baefc6af40a](../../evidence/parameters-sets-002.md#p-164d4baefc6af40a) · [状态效果 S-6e7e0338621cb45a](../../evidence/state_effects-sets-023.md#s-6e7e0338621cb45a)

### path-037481

```text
(config)# do-exec test rsvp nsr disable <cr>
```

Handler ` RVA 0x10078B00 `；selector ` 0 `；EOL ` RVA 0x34A3ED00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-037444

```text
(config)# do-exec test rsvp nsr enable <cr>
```

Handler ` RVA 0x100789F0 `；selector ` 0 `；EOL ` RVA 0x34A3EA58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-037412

```text
(config)# do-exec test rsvp nsr incr <cr>
```

Handler ` RVA 0x100788E0 `；selector ` 0 `；EOL ` RVA 0x34A3E7B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-037377

```text
(config)# do-exec test rsvp nsr start <cr>
```

Handler ` RVA 0x100787C0 `；selector ` 0 `；EOL ` RVA 0x34A3E508 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-060242

```text
(config)# do-exec test rsvp transport send path <address> <address> <number:0..255> <number:0..65535> <number:0..65535> <number:1..65535> <address> <number:1..65535> data <string> <cr>
```

Handler ` RVA 0x1005D100 `；selector ` 0 `；EOL ` RVA 0x34A3DFB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Destination address；` address ` Source address；` unsigned_number ` IP Protocol；` unsigned_number ` Destination port；` unsigned_number ` Source port；` unsigned_number ` Client Identifier；` address ` Initiator Id；` unsigned_number ` Instance Id；` string ` RSVP Transport message。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-c024f648c9188b95](../../evidence/parameters-sets-015.md#p-c024f648c9188b95) · [状态效果 S-ac9bd0efd867917e](../../evidence/state_effects-sets-036.md#s-ac9bd0efd867917e)

### path-039882

```text
(config)# do-exec test rtty <number:0..4294967295> <string> <cr>
```

Handler ` RVA 0xCC38580 `；selector ` 0 `；EOL ` RVA 0x33C237D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Remote Seat ID(in hexadecimal)；` string ` Command String。

[条件 C-9ee8389756ff7b14](../../evidence/conditions-sets-061.md#c-9ee8389756ff7b14) · [参数 P-87096cdef34360d5](../../evidence/parameters-sets-010.md#p-87096cdef34360d5) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-039995

```text
(config)# do-exec test rtty statistics disable <cr>
```

Handler ` RVA 0xCC382E0 `；selector ` 0 `；EOL ` RVA 0x33C23D38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7b263b83285ee6b6](../../evidence/conditions-sets-048.md#c-7b263b83285ee6b6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-039940

```text
(config)# do-exec test rtty statistics enable <cr>
```

Handler ` RVA 0xCC382E0 `；selector ` 1 `；EOL ` RVA 0x33C23A90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c937aa2f37c5639d](../../evidence/conditions-sets-078.md#c-c937aa2f37c5639d) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-040044

```text
(config)# do-exec test rtty statistics print <cr>
```

Handler ` RVA 0xCC38340 `；selector ` 0 `；EOL ` RVA 0x33C23FE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2f67e2e03fdf8f75](../../evidence/conditions-sets-019.md#c-2f67e2e03fdf8f75) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-058408

```text
(config)# do-exec test sasl client ip <address> port <number:0..65535> <cr>
```

Handler ` RVA 0x103D1180 `；selector ` 1 `；EOL ` RVA 0x34B14C98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP address for outgoing connection；` unsigned_number ` Port value for outgoing connection。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-0a6a0a313046b956](../../evidence/parameters-sets-001.md#p-0a6a0a313046b956) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-059906

```text
(config)# do-exec test sasl client ip <address> port <number:0..65535> profile <string> <cr>
```

Handler ` RVA 0x103D1180 `；selector ` 2 `；EOL ` RVA 0x34B14F88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP address for outgoing connection；` unsigned_number ` Port value for outgoing connection；` string ` SASL profile name。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-f6b83400a54cfc55](../../evidence/parameters-sets-018.md#p-f6b83400a54cfc55) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-049245

```text
(config)# do-exec test sasl server port <number:0..65535> <cr>
```

Handler ` RVA 0x103D1180 `；selector ` 3 `；EOL ` RVA 0x34B153F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Port value for SASL listening。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-f5808002237e59f6](../../evidence/parameters-sets-018.md#p-f5808002237e59f6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-058398

```text
(config)# do-exec test sasl server port <number:0..65535> profile <string> <cr>
```

Handler ` RVA 0x103D1180 `；selector ` 4 `；EOL ` RVA 0x34B156E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Port value for SASL listening；` string ` SASL profile name。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-7fbae1e202e71069](../../evidence/parameters-sets-010.md#p-7fbae1e202e71069) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-040129

```text
(config)# do-exec test sasl server stop <cr>
```

Handler ` RVA 0x103D1180 `；selector ` 5 `；EOL ` RVA 0x34B15978 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-028224

```text
(config)# do-exec test save snapshot <cr>
```

Handler ` RVA 0xD6D2B10 `；selector ` 0 `；EOL ` RVA 0x33ECE430 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-037086

```text
(config)# do-exec test scheduler trash edisms <cr>
```

Handler ` RVA 0xD7A41D0 `；selector ` 0 `；EOL ` RVA 0x33EEE678 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f463be9d971647c6](../../evidence/conditions-sets-094.md#c-f463be9d971647c6) · [状态效果 S-9e038f4f07a45bef](../../evidence/state_effects-sets-034.md#s-9e038f4f07a45bef)

### path-029424

```text
(config)# do-exec test scheduler watched-message <cr>
```

Handler ` RVA 0xD79FA20 `；selector ` 0 `；EOL ` RVA 0x33EED500 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c2445050f638f023](../../evidence/conditions-sets-075.md#c-c2445050f638f023) · [状态效果 S-f5cd7566af7860ed](../../evidence/state_effects-sets-052.md#s-f5cd7566af7860ed)

### path-037026

```text
(config)# do-exec test sctp association create <cr>
```

Handler ` RVA 0xCE848E0 `；selector ` 0 `；EOL ` RVA 0x33D12C40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-030464

```text
(config)# do-exec test sctp delete <cr>
```

Handler ` RVA 0xCE84E80 `；selector ` 0 `；EOL ` RVA 0x33D12690 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-036982

```text
(config)# do-exec test sctp instance create <cr>
```

Handler ` RVA 0xCE828C0 `；selector ` 0 `；EOL ` RVA 0x33D12308 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-046372

```text
(config)# do-exec test sctp instance delete <number:1..65535> <cr>
```

Handler ` RVA 0xCE847D0 `；selector ` 0 `；EOL ` RVA 0x33D12668 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Local port of instance to delete。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-b7f8a9d96e4fa6a8](../../evidence/parameters-sets-014.md#p-b7f8a9d96e4fa6a8) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-046679

```text
(config)# do-exec test sctp parameters burstsize <number:1..1024> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 8 `；EOL ` RVA 0x33D0FE28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of packets to burst。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-5f332658bcc3b1ba](../../evidence/parameters-sets-008.md#p-5f332658bcc3b1ba) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-054243

```text
(config)# do-exec test sctp parameters congabate <number:1..3> <number:0..65535> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 17 `；EOL ` RVA 0x33D11C18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Congestion level to define abate value；` unsigned_number ` Value for congestion abate。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-6e3b56e35279f34e](../../evidence/parameters-sets-009.md#p-6e3b56e35279f34e) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-046944

```text
(config)# do-exec test sctp parameters conglevels <number:0..3> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 15 `；EOL ` RVA 0x33D115A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of congestion levels to define。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-90dac4eb92412f64](../../evidence/parameters-sets-011.md#p-90dac4eb92412f64) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-054228

```text
(config)# do-exec test sctp parameters congonset <number:1..3> <number:0..65535> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 16 `；EOL ` RVA 0x33D118E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Congestion level to define onset value；` unsigned_number ` Value for congestion onset。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-07fdbf832d65708c](../../evidence/parameters-sets-001.md#p-07fdbf832d65708c) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-046715

```text
(config)# do-exec test sctp parameters delay <number:0..60000> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 9 `；EOL ` RVA 0x33D10118 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Delay (msecs) between bursts。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-a85ef6772e443ce4](../../evidence/parameters-sets-013.md#p-a85ef6772e443ce4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-037638

```text
(config)# do-exec test sctp parameters display <cr>
```

Handler ` RVA 0xCE6FC00 `；selector ` 0 `；EOL ` RVA 0x33D11EA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-046480

```text
(config)# do-exec test sctp parameters fixedparams <number:0..1> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 4 `；EOL ` RVA 0x33D0F268 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Use fixed params (FALSE=0/TRUE=1)?。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-148bb4a30eac7147](../../evidence/parameters-sets-002.md#p-148bb4a30eac7147) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-046759

```text
(config)# do-exec test sctp parameters hbenabled <number:0..1> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 10 `；EOL ` RVA 0x33D10408 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Heartbeat dest addrs (FALSE=0/TRUE=1)?。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-acd27b8447a1b688](../../evidence/parameters-sets-013.md#p-acd27b8447a1b688) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-046798

```text
(config)# do-exec test sctp parameters hbtimeout <number:0..600000> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 11 `；EOL ` RVA 0x33D106F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Heartbeat timer value。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-001bdbe6024b7fc0](../../evidence/parameters-sets-001.md#p-001bdbe6024b7fc0) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-046315

```text
(config)# do-exec test sctp parameters instreams <number:1..1024> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 1 `；EOL ` RVA 0x33D0E998 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of inbound streams。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-f60c7b1ad05500ca](../../evidence/parameters-sets-018.md#p-f60c7b1ad05500ca) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-046877

```text
(config)# do-exec test sctp parameters maxRTO <number:300..65535> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 13 `；EOL ` RVA 0x33D10FC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Max retrans timer value (ms)。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-656c5afea3fc72ab](../../evidence/parameters-sets-008.md#p-656c5afea3fc72ab) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-046631

```text
(config)# do-exec test sctp parameters maxoutstand <number:0..1024> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 7 `；EOL ` RVA 0x33D0FB38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Max number of packets outstanding。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-565a162e37a45ac2](../../evidence/parameters-sets-007.md#p-565a162e37a45ac2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-046582

```text
(config)# do-exec test sctp parameters maxpackets <number:0..65535> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 6 `；EOL ` RVA 0x33D0F848 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Max number of packets to send (9999=inf)。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-7b10493dc6084a57](../../evidence/parameters-sets-010.md#p-7b10493dc6084a57) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-046429

```text
(config)# do-exec test sctp parameters maxpdusize <number:4..10000> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 3 `；EOL ` RVA 0x33D0EF78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Pdu size of test dgrams。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-0cff93470ff98b66](../../evidence/parameters-sets-001.md#p-0cff93470ff98b66) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-046851

```text
(config)# do-exec test sctp parameters minRTO <number:300..65535> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 12 `；EOL ` RVA 0x33D10CD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Min retrans timer value (ms)。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-f7c8c4e77b4b985e](../../evidence/parameters-sets-018.md#p-f7c8c4e77b4b985e) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-046271

```text
(config)# do-exec test sctp parameters outstreams <number:1..1024> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 0 `；EOL ` RVA 0x33D0E6A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of outbound streams。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-71ac10a0fbb6fc04](../../evidence/parameters-sets-009.md#p-71ac10a0fbb6fc04) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-046373

```text
(config)# do-exec test sctp parameters pdusize <number:4..10000> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 2 `；EOL ` RVA 0x33D0EC88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Pdu size of test dgrams。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-6fa3fc9c170f9a06](../../evidence/parameters-sets-009.md#p-6fa3fc9c170f9a06) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-046911

```text
(config)# do-exec test sctp parameters rcvwin <number:1500..65535> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 14 `；EOL ` RVA 0x33D112B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Local receive window value (bytes)。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-ac176c644c368388](../../evidence/parameters-sets-013.md#p-ac176c644c368388) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-046826

```text
(config)# do-exec test sctp parameters testtype <number:0..1> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 18 `；EOL ` RVA 0x33D109E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Test type (SIMPLE=0/LOOPREQ=1)?。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-ed32cc90492c4587](../../evidence/parameters-sets-018.md#p-ed32cc90492c4587) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-046528

```text
(config)# do-exec test sctp parameters usealladdrs <number:0..1> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 5 `；EOL ` RVA 0x33D0F558 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Use all dest addrs (FALSE=0/TRUE=1)?。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-64b63411945a3011](../../evidence/parameters-sets-008.md#p-64b63411945a3011) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-038936

```text
(config)# do-exec test sdb add <string> <cr>
```

Handler ` RVA 0xDEC82E0 `；selector ` 0 `；EOL ` RVA 0x34093138 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` name。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-5c1d0be0e07d0031](../../evidence/parameters-sets-007.md#p-5c1d0be0e07d0031) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-038989

```text
(config)# do-exec test sdb remove <string> <cr>
```

Handler ` RVA 0xDEC8430 `；selector ` 0 `；EOL ` RVA 0x34093420 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` name。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-5c6127879750809b](../../evidence/parameters-sets-007.md#p-5c6127879750809b) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-039043

```text
(config)# do-exec test sdb search <string> <cr>
```

Handler ` RVA 0xDEC8550 `；selector ` 0 `；EOL ` RVA 0x340936E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` name。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-427368a9e0878d44](../../evidence/parameters-sets-006.md#p-427368a9e0878d44) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-037181

```text
(config)# do-exec test service-overlay application register <cr>
```

Handler ` RVA 0x108F5810 `；selector ` 1 `；EOL ` RVA 0x34BF7E70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-16bff770590b3413](../../evidence/conditions-sets-009.md#c-16bff770590b3413) · [状态效果 S-8356828ce0a6f4b2](../../evidence/state_effects-sets-028.md#s-8356828ce0a6f4b2)

### path-061982

```text
(config)# do-exec test service-overlay interface <interface> application register <cr>
```

Handler ` RVA 0x108F5810 `；selector ` 1 `；EOL ` RVA 0x34BF7E70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0afd30935b223ed3](../../evidence/conditions-sets-005.md#c-0afd30935b223ed3) · [缺口 G-de7cdcc20d2c9b9d](../../evidence/gaps-sets-008.md#g-de7cdcc20d2c9b9d) · [参数 P-c2b527b418c2f9c1](../../evidence/parameters-sets-015.md#p-c2b527b418c2f9c1) · [状态效果 S-8356828ce0a6f4b2](../../evidence/state_effects-sets-028.md#s-8356828ce0a6f4b2)

### path-054315

```text
(config)# do-exec test service-routing api debug <number:0..4294967295> <number:0..4294967295> <cr>
```

Handler ` RVA 0x10452690 `；selector ` 17 `；EOL ` RVA 0x34B2F8A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Service-Routing sf-client handle；` unsigned_number ` Debug flags。

[条件 C-e701e52bacd9039a](../../evidence/conditions-sets-089.md#c-e701e52bacd9039a) · [参数 P-fc2096c688c2da52](../../evidence/parameters-sets-019.md#p-fc2096c688c2da52) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062693

```text
(config)# do-exec test service-routing api publish-service <number:1..4294967295> <number:0..65535> : <number:0..65535> : <number:0..4294967295> - <number:0..65535> - <number:0..65535> - <number:0..65535> - <hex-string> <number:1..4294967295> <number:0..32768> <cr>
```

Handler ` RVA 0x10452690 `；selector ` 21 `；EOL ` RVA 0x34B2E0F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Service-Routing sf-client handle；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` hexstring ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` Service-sequence；` unsigned_number ` Service-size。

[条件 C-0707a8cc73c16eae](../../evidence/conditions-sets-003.md#c-0707a8cc73c16eae) · [缺口 G-8948cc2e129b4c68](../../evidence/gaps-sets-005.md#g-8948cc2e129b4c68) · [参数 P-42d37c8e54e08203](../../evidence/parameters-sets-006.md#p-42d37c8e54e08203) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-060266

```text
(config)# do-exec test service-routing api publish-service <number:1..4294967295> <number:0..65535> : <number:0..65535> : <number:0..4294967295> . <number:0..4294967295> . <number:0..4294967295> . <number:0..4294967295> <number:1..4294967295> <number:0..32768> <cr>
```

Handler ` RVA 0x10452690 `；selector ` 21 `；EOL ` RVA 0x34B2E0F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Service-Routing sf-client handle；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` Service-sequence；` unsigned_number ` Service-size。

[条件 C-3852d83c46d8182b](../../evidence/conditions-sets-022.md#c-3852d83c46d8182b) · [参数 P-bbe7af018acbc6ac](../../evidence/parameters-sets-014.md#p-bbe7af018acbc6ac) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-047031

```text
(config)# do-exec test service-routing api register-client <number:0..4294967295> <cr>
```

Handler ` RVA 0x10452690 `；selector ` 24 `；EOL ` RVA 0x34B2D520 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Client context。

[条件 C-e701e52bacd9039a](../../evidence/conditions-sets-089.md#c-e701e52bacd9039a) · [参数 P-c58be6cbdbca42b7](../../evidence/parameters-sets-015.md#p-c58be6cbdbca42b7) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-054240

```text
(config)# do-exec test service-routing api register-client <number:0..4294967295> <string> <cr>
```

Handler ` RVA 0x10452690 `；selector ` 23 `；EOL ` RVA 0x34B2D4F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Client context；` string ` Client name。

[条件 C-e701e52bacd9039a](../../evidence/conditions-sets-089.md#c-e701e52bacd9039a) · [参数 P-28a8a8d90e5fc0a1](../../evidence/parameters-sets-004.md#p-28a8a8d90e5fc0a1) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062692

```text
(config)# do-exec test service-routing api subscribe-service <number:1..4294967295> <number:0..65535> : <number:0..65535> : <number:0..4294967295> - <number:0..65535> - <number:0..65535> - <number:0..65535> - <hex-string> <number:0..255> <cr>
```

Handler ` RVA 0x10452690 `；selector ` 19 `；EOL ` RVA 0x34B2F088 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Service-Routing sf-client handle；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` hexstring ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` Maximum-paths。

[条件 C-2ecb1a1581631f64](../../evidence/conditions-sets-018.md#c-2ecb1a1581631f64) · [缺口 G-c7eaa34e6739b60b](../../evidence/gaps-sets-007.md#g-c7eaa34e6739b60b) · [参数 P-38d9ed723c8815b4](../../evidence/parameters-sets-005.md#p-38d9ed723c8815b4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-060260

```text
(config)# do-exec test service-routing api subscribe-service <number:1..4294967295> <number:0..65535> : <number:0..65535> : <number:0..4294967295> . <number:0..4294967295> . <number:0..4294967295> . <number:0..4294967295> <number:0..255> <cr>
```

Handler ` RVA 0x10452690 `；selector ` 19 `；EOL ` RVA 0x34B2F088 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Service-Routing sf-client handle；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` Maximum-paths。

[条件 C-f83ee40f41020790](../../evidence/conditions-sets-096.md#c-f83ee40f41020790) · [参数 P-7447444ab7796741](../../evidence/parameters-sets-009.md#p-7447444ab7796741) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062691

```text
(config)# do-exec test service-routing api unpublish-service <number:1..4294967295> <number:0..65535> : <number:0..65535> : <number:0..4294967295> - <number:0..65535> - <number:0..65535> - <number:0..65535> - <hex-string> <cr>
```

Handler ` RVA 0x10452690 `；selector ` 20 `；EOL ` RVA 0x34B2E898 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Service-Routing sf-client handle；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` hexstring ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance。

[条件 C-b337663bd38df979](../../evidence/conditions-sets-069.md#c-b337663bd38df979) · [缺口 G-aba1b8cb83943f01](../../evidence/gaps-sets-006.md#g-aba1b8cb83943f01) · [参数 P-9d63b9d343d0cbc0](../../evidence/parameters-sets-012.md#p-9d63b9d343d0cbc0) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-060251

```text
(config)# do-exec test service-routing api unpublish-service <number:1..4294967295> <number:0..65535> : <number:0..65535> : <number:0..4294967295> . <number:0..4294967295> . <number:0..4294967295> . <number:0..4294967295> <cr>
```

Handler ` RVA 0x10452690 `；selector ` 20 `；EOL ` RVA 0x34B2E898 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Service-Routing sf-client handle；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance。

[条件 C-ab217c6e4930bfe1](../../evidence/conditions-sets-066.md#c-ab217c6e4930bfe1) · [参数 P-6205f9bccb319166](../../evidence/parameters-sets-008.md#p-6205f9bccb319166) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-047010

```text
(config)# do-exec test service-routing api unregister-client <number:1..4294967295> <cr>
```

Handler ` RVA 0x10452690 `；selector ` 22 `；EOL ` RVA 0x34B2DA48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Service-Routing sf-client handle。

[条件 C-e701e52bacd9039a](../../evidence/conditions-sets-089.md#c-e701e52bacd9039a) · [参数 P-fd4fdd18c511da0a](../../evidence/parameters-sets-019.md#p-fd4fdd18c511da0a) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-054300

```text
(config)# do-exec test service-routing api unsubscribe-service <number:1..4294967295> <number:1..4294967295> <cr>
```

Handler ` RVA 0x10452690 `；selector ` 18 `；EOL ` RVA 0x34B2F598 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Service-Routing sf-client handle；` unsigned_number ` Subscription handle。

[条件 C-e701e52bacd9039a](../../evidence/conditions-sets-089.md#c-e701e52bacd9039a) · [参数 P-ea16afa033846cd9](../../evidence/parameters-sets-018.md#p-ea16afa033846cd9) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-037551

```text
(config)# do-exec test service-routing api version <cr>
```

Handler ` RVA 0x10452690 `；selector ` 25 `；EOL ` RVA 0x34B2D1A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e701e52bacd9039a](../../evidence/conditions-sets-089.md#c-e701e52bacd9039a) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-059321

```text
(config)# do-exec test service-routing capabilities-manager api register <string> <string> <string> <cr>
```

Handler ` RVA 0x1045B700 `；selector ` 80 `；EOL ` RVA 0x34B34700 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Component；` string ` Capability；` string ` Capability Data。

[条件 C-e701e52bacd9039a](../../evidence/conditions-sets-089.md#c-e701e52bacd9039a) · [参数 P-2cd42d186cef97f3](../../evidence/parameters-sets-004.md#p-2cd42d186cef97f3) · [状态效果 S-407121dbaacddd86](../../evidence/state_effects-sets-014.md#s-407121dbaacddd86)

### path-057905

```text
(config)# do-exec test service-routing capabilities-manager api unregister <string> <string> <cr>
```

Handler ` RVA 0x1045B700 `；selector ` 80 `；EOL ` RVA 0x34B34A28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Component；` string ` Capability。

[条件 C-e701e52bacd9039a](../../evidence/conditions-sets-089.md#c-e701e52bacd9039a) · [参数 P-ca371a52bc56aa69](../../evidence/parameters-sets-015.md#p-ca371a52bc56aa69) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-046973

```text
(config)# do-exec test service-routing capabilities-manager api version <cr>
```

Handler ` RVA 0x1045B660 `；selector ` 79 `；EOL ` RVA 0x34B34CA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e701e52bacd9039a](../../evidence/conditions-sets-089.md#c-e701e52bacd9039a) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-057904

```text
(config)# do-exec test service-routing xmcp client <number:0..4294967295> error-response <number:100..699> <cr>
```

Handler ` RVA 0x10472C70 `；selector ` 56 `；EOL ` RVA 0x34B37C48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Client handle；` unsigned_number ` Error code。

[条件 C-e701e52bacd9039a](../../evidence/conditions-sets-089.md#c-e701e52bacd9039a) · [参数 P-82ab05eb296bdede](../../evidence/parameters-sets-010.md#p-82ab05eb296bdede) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062643

```text
(config)# do-exec test session-mgr <interface> client-id <number:1..255> mac <address> mlist <string> dot1x <cr>
```

Handler ` RVA 0xCAF8B40 `；selector ` 0 `；EOL ` RVA 0x33B96F08 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Enter a value between 1 and 255；` address ` MAC address；` string ` Name of authentication method list。

[条件 C-a0a706b6f79515e5](../../evidence/conditions-sets-062.md#c-a0a706b6f79515e5) · [缺口 G-2cf92449e95aad04](../../evidence/gaps-sets-002.md#g-2cf92449e95aad04) · [参数 P-d0d17b1f4f9abc7d](../../evidence/parameters-sets-016.md#p-d0d17b1f4f9abc7d) · [状态效果 S-9562a56700ffce6c](../../evidence/state_effects-sets-032.md#s-9562a56700ffce6c)

### path-060901

```text
(config)# do-exec test session-mgr <interface> fips <cr>
```

Handler ` RVA 0xCAFC7F0 `；selector ` 0 `；EOL ` RVA 0x33BAFBA0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a0a706b6f79515e5](../../evidence/conditions-sets-062.md#c-a0a706b6f79515e5) · [缺口 G-2cf92449e95aad04](../../evidence/gaps-sets-002.md#g-2cf92449e95aad04) · [参数 P-11ec98d89dbdd7bc](../../evidence/parameters-sets-002.md#p-11ec98d89dbdd7bc) · [状态效果 S-cab710114dfdc733](../../evidence/state_effects-sets-043.md#s-cab710114dfdc733)

### path-037091

```text
(config)# do-exec test session-mgr acct-stats start <cr>
```

Handler ` RVA 0xCAF8B40 `；selector ` 0 `；EOL ` RVA 0x33B97CF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-34930c8cd32478c6](../../evidence/conditions-sets-020.md#c-34930c8cd32478c6) · [状态效果 S-b0e04ec575f05278](../../evidence/state_effects-sets-037.md#s-b0e04ec575f05278)

### path-046575

```text
(config)# do-exec test session-mgr cga-remote-auth authc <number:1..4294967295> <cr>
```

Handler ` RVA 0xCAF8B40 `；selector ` 0 `；EOL ` RVA 0x33B98398 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Handle value。

[条件 C-34930c8cd32478c6](../../evidence/conditions-sets-020.md#c-34930c8cd32478c6) · [参数 P-da2f08bdc200c03c](../../evidence/parameters-sets-016.md#p-da2f08bdc200c03c) · [状态效果 S-6eac216cdc3f78dc](../../evidence/state_effects-sets-024.md#s-6eac216cdc3f78dc)

### path-054058

```text
(config)# do-exec test session-mgr crimson table mab create <cr>
```

Handler ` RVA 0xCAF8B40 `；selector ` 0 `；EOL ` RVA 0x33B98F00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-34930c8cd32478c6](../../evidence/conditions-sets-020.md#c-34930c8cd32478c6) · [状态效果 S-9e77c49aeaf62135](../../evidence/state_effects-sets-034.md#s-9e77c49aeaf62135)

### path-059215

```text
(config)# do-exec test session-mgr event send async start handle <number:1..4294967295> <cr>
```

Handler ` RVA 0xCAF8B40 `；selector ` 0 `；EOL ` RVA 0x33B96910 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Handle value。

[条件 C-dbf47fc2f6ef65b4](../../evidence/conditions-sets-085.md#c-dbf47fc2f6ef65b4) · [参数 P-96568601ab7c7b37](../../evidence/parameters-sets-012.md#p-96568601ab7c7b37) · [状态效果 S-38d77d40d0c076c8](../../evidence/state_effects-sets-013.md#s-38d77d40d0c076c8)

### path-046670

```text
(config)# do-exec test session-mgr fqdn-epm-notify <number:1..4294967295> <address> <cr>
```

Handler ` RVA 0xCAF8B40 `；selector ` 0 `；EOL ` RVA 0x33B98B50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Handle value；` address ` IP address to notify。

[条件 C-34930c8cd32478c6](../../evidence/conditions-sets-020.md#c-34930c8cd32478c6) · [参数 P-d0e66e8ab24af0c2](../../evidence/parameters-sets-016.md#p-d0e66e8ab24af0c2) · [状态效果 S-864fa7e67dbb4137](../../evidence/state_effects-sets-028.md#s-864fa7e67dbb4137)

### path-037365

```text
(config)# do-exec test session-mgr green create <cr>
```

Handler ` RVA 0xCAD3E50 `；selector ` 0 `；EOL ` RVA 0x33B99460 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-34930c8cd32478c6](../../evidence/conditions-sets-020.md#c-34930c8cd32478c6) · [状态效果 S-4cde167ae28f223f](../../evidence/state_effects-sets-017.md#s-4cde167ae28f223f)

### path-059295

```text
(config)# do-exec test session-mgr identity mac <address> add ip <address> <cr>
```

Handler ` RVA 0xCAF8B40 `；selector ` 0 `；EOL ` RVA 0x33B9A048 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` MAC address；` address ` IP address。

[条件 C-34930c8cd32478c6](../../evidence/conditions-sets-020.md#c-34930c8cd32478c6) · [参数 P-bb158b26fcbfa514](../../evidence/parameters-sets-014.md#p-bb158b26fcbfa514) · [状态效果 S-6b2d8286d6cf960c](../../evidence/state_effects-sets-023.md#s-6b2d8286d6cf960c)

### path-062618

```text
(config)# do-exec test session-mgr session push mac <address> <interface> source switch-pi <cr>
```

Handler ` RVA 0xCAF8B40 `；selector ` 0 `；EOL ` RVA 0x33B9A950 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` MAC address。

[条件 C-d925413c9da96dc0](../../evidence/conditions-sets-084.md#c-d925413c9da96dc0) · [缺口 G-6ed41314c5e36b64](../../evidence/gaps-sets-004.md#g-6ed41314c5e36b64) · [参数 P-e04940707f210ada](../../evidence/parameters-sets-017.md#p-e04940707f210ada) · [状态效果 S-5cf9a367bbab8636](../../evidence/state_effects-sets-020.md#s-5cf9a367bbab8636)

### path-037046

```text
(config)# do-exec test session-mgr sm-client register <cr>
```

Handler ` RVA 0xCAF8B40 `；selector ` 0 `；EOL ` RVA 0x33B97830 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-34930c8cd32478c6](../../evidence/conditions-sets-020.md#c-34930c8cd32478c6) · [状态效果 S-8db57155111254f0](../../evidence/state_effects-sets-030.md#s-8db57155111254f0)

### path-061973

```text
(config)# do-exec test session-mgr spi server start <interface> <cr>
```

Handler ` RVA 0xCAF8B40 `；selector ` 0 `；EOL ` RVA 0x33B97480 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e387565b560899e5](../../evidence/conditions-sets-088.md#c-e387565b560899e5) · [缺口 G-6b745a88bd4ac37d](../../evidence/gaps-sets-004.md#g-6b745a88bd4ac37d) · [参数 P-8cbb6dd19a760537](../../evidence/parameters-sets-011.md#p-8cbb6dd19a760537) · [状态效果 S-9e0a23d08cf52301](../../evidence/state_effects-sets-034.md#s-9e0a23d08cf52301)

### path-057770

```text
(config)# do-exec test session-mgr test-vlan <string> <number:1..4095> <number:1..4> <number:1..1000> <cr>
```

Handler ` RVA 0xCAF8B40 `；selector ` 0 `；EOL ` RVA 0x33B98808 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of the vlan group；` unsigned_number ` Value of the vlan；` unsigned_number ` 1 to add any other value to remove；` unsigned_number ` Number of users。

[条件 C-34930c8cd32478c6](../../evidence/conditions-sets-020.md#c-34930c8cd32478c6) · [参数 P-8f6fc02bc311139a](../../evidence/parameters-sets-011.md#p-8f6fc02bc311139a) · [状态效果 S-29275dec472780fc](../../evidence/state_effects-sets-009.md#s-29275dec472780fc)

### path-036810

```text
(config)# do-exec test snmp cpu-stats start <cr>
```

Handler ` RVA 0xCC7C220 `；selector ` 0 `；EOL ` RVA 0x33C3C500 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-44e127c949423ac8](../../evidence/conditions-sets-027.md#c-44e127c949423ac8) · [状态效果 S-8d539b2e2ef89d59](../../evidence/state_effects-sets-030.md#s-8d539b2e2ef89d59)

### path-037127

```text
(config)# do-exec test snmp trap config-copy <cr>
```

Handler ` RVA 0x104C05D0 `；selector ` 41 `；EOL ` RVA 0x33C3C888 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-5000c2d9964e96e3](../../evidence/state_effects-sets-017.md#s-5000c2d9964e96e3)

### path-045668

```text
(config)# do-exec test ssm asynchronous throttling print <cr>
```

Handler ` RVA 0x10433590 `；selector ` 0 `；EOL ` RVA 0x34B25118 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-57328acc0e3f8ec5](../../evidence/state_effects-sets-019.md#s-57328acc0e3f8ec5)

### path-035850

```text
(config)# do-exec test ssm counters enable <cr>
```

Handler ` RVA 0x104332C0 `；selector ` 0 `；EOL ` RVA 0x34B23798 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-36265dca972197c4](../../evidence/state_effects-sets-012.md#s-36265dca972197c4)

### path-053027

```text
(config)# do-exec test ssm fcdb nosupport <number:1..25> <number:0..2> <cr>
```

Handler ` RVA 0x104365F0 `；selector ` 0 `；EOL ` RVA 0x34B23BB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` feature type；` unsigned_number ` nosupport action (0=ignore, 1=punt, 2=teardown seg)。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-23be321c29567b35](../../evidence/parameters-sets-003.md#p-23be321c29567b35) · [状态效果 S-605ba3148335c32d](../../evidence/state_effects-sets-021.md#s-605ba3148335c32d)

### path-036299

```text
(config)# do-exec test ssm feature status <cr>
```

Handler ` RVA 0x10435390 `；selector ` 0 `；EOL ` RVA 0x34B24850 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-084b435cff6d3c5c](../../evidence/state_effects-sets-002.md#s-084b435cff6d3c5c)

### path-045332

```text
(config)# do-exec test ssm repop <number:1..14> <number:0..2> <cr>
```

Handler ` RVA 0x104331B0 `；selector ` 0 `；EOL ` RVA 0x34B234A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` switch type : 1-AC/AC, 2-AC/ATOM, 3-AC/L2TP, 4-AC/VFI, 5-VFI/AToM, 6-VFI/L2TP, 7-All；` unsigned_number ` segment class type : 1-SSS, 2-HW, 3-ALL。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-53f05257c23695ba](../../evidence/parameters-sets-007.md#p-53f05257c23695ba) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-045543

```text
(config)# do-exec test ssm segment lock <number:1..4294967295> <cr>
```

Handler ` RVA 0x104332C0 `；selector ` 0 `；EOL ` RVA 0x34B24450 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` segment id。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-921027c1fa5afe65](../../evidence/parameters-sets-011.md#p-921027c1fa5afe65) · [状态效果 S-887d68842a1134e3](../../evidence/state_effects-sets-029.md#s-887d68842a1134e3)

### path-053065

```text
(config)# do-exec test ssm segment support enable <number:1..41> <cr>
```

Handler ` RVA 0x104332C0 `；selector ` 0 `；EOL ` RVA 0x34B24110 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` segment type value。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-35adb604690ed821](../../evidence/parameters-sets-005.md#p-35adb604690ed821) · [状态效果 S-33501d337083f7f7](../../evidence/state_effects-sets-011.md#s-33501d337083f7f7)

### path-057345

```text
(config)# do-exec test subscriber feature accounting accuracy throttling print <cr>
```

Handler ` RVA 0x1093B5A0 `；selector ` 0 `；EOL ` RVA 0x34C06558 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-283bf674c2bb85f0](../../evidence/conditions-sets-016.md#c-283bf674c2bb85f0) · [状态效果 S-4ce0334b84618775](../../evidence/state_effects-sets-017.md#s-4ce0334b84618775)

### path-053217

```text
(config)# do-exec test subscriber feature timer acceleration enable <cr>
```

Handler ` RVA 0x1093F020 `；selector ` 0 `；EOL ` RVA 0x34C06130 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4655ff8d3efa5834](../../evidence/conditions-sets-027.md#c-4655ff8d3efa5834) · [状态效果 S-27631a3d0a032423](../../evidence/state_effects-sets-009.md#s-27631a3d0a032423)

### path-053567

```text
(config)# do-exec test subscriber policy account-logon session <number:0..4294967295> <cr>
```

Handler ` RVA 0x109D50A0 `；selector ` 0 `；EOL ` RVA 0x34C56688 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Subscriber Service Switch session id value。

[条件 C-65fb485e87c94d63](../../evidence/conditions-sets-039.md#c-65fb485e87c94d63) · [参数 P-a89542a0c784be09](../../evidence/parameters-sets-013.md#p-a89542a0c784be09) · [状态效果 S-89edb791c3d8e432](../../evidence/state_effects-sets-029.md#s-89edb791c3d8e432)

### path-053313

```text
(config)# do-exec test subscriber policy condition-map <string> <string> <cr>
```

Handler ` RVA 0x10A59C40 `；selector ` 0 `；EOL ` RVA 0x34C749F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` The condition map to be tested for equality；` string ` The condition map to be used as the identifier source。

[条件 C-a5f24b6bf4def107](../../evidence/conditions-sets-064.md#c-a5f24b6bf4def107) · [参数 P-10987eb1655aac27](../../evidence/parameters-sets-002.md#p-10987eb1655aac27) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-036499

```text
(config)# do-exec test subscriber policy dummy <cr>
```

Handler ` RVA 0x109D50A0 `；selector ` 0 `；EOL ` RVA 0x34C55550 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-234568e1f8b26a9a](../../evidence/conditions-sets-014.md#c-234568e1f8b26a9a) · [状态效果 S-e369015f852c37fb](../../evidence/state_effects-sets-048.md#s-e369015f852c37fb)

### path-060200

```text
(config)# do-exec test subscriber policy epd accounting-req start session-guid <string> epd-flow-id <number:0..32> epd-ipaddress <address> <cr>
```

Handler ` RVA 0xFE8A740 `；selector ` 0 `；EOL ` RVA 0x34C53288 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Enter ISG Session GUID；` unsigned_number ` Enter EPD Flow Id；` address ` Enter EPD Device IP Address。

[条件 C-19aa69e77a2dedba](../../evidence/conditions-sets-010.md#c-19aa69e77a2dedba) · [参数 P-c12bb31bafc45042](../../evidence/parameters-sets-015.md#p-c12bb31bafc45042) · [状态效果 S-2b3365b49727fd3b](../../evidence/state_effects-sets-010.md#s-2b3365b49727fd3b)

### path-060219

```text
(config)# do-exec test subscriber policy epd conn_mgmt-query version <string> command <string> peer-ip <address> keepalive <number:0..3600> <cr>
```

Handler ` RVA 0xFE89ED0 `；selector ` 0 `；EOL ` RVA 0x34C54440 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Version string, only "1.0" is valid；` string ` Command string (establish, disestablish, keepalive)；` address ` IP address of the peer；` unsigned_number ` keepalive value(0 not to send)。

[条件 C-e6c55dbbd090fba6](../../evidence/conditions-sets-089.md#c-e6c55dbbd090fba6) · [参数 P-528cd97ddb37152d](../../evidence/parameters-sets-007.md#p-528cd97ddb37152d) · [状态效果 S-cf4e06778eff626e](../../evidence/state_effects-sets-044.md#s-cf4e06778eff626e)

### path-059192

```text
(config)# do-exec test subscriber policy epd conn_mgmt-ses-test <number:1..2> <number:0..30> <string> <cr>
```

Handler ` RVA 0xFE89E20 `；selector ` 0 `；EOL ` RVA 0x34C547F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` 1 - to add, 2 to remove；` unsigned_number ` conn id ；` string ` session guid string  。

[条件 C-5626498617550105](../../evidence/conditions-sets-034.md#c-5626498617550105) · [参数 P-2f90b406a6098bc7](../../evidence/parameters-sets-004.md#p-2f90b406a6098bc7) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-060035

```text
(config)# do-exec test subscriber policy epd handler coa-request epd-ipaddress <address> attr-list <string> <cr>
```

Handler ` RVA 0xFE7F1A0 `；selector ` 0 `；EOL ` RVA 0x34C537B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Enter Session IP Address；` string ` Attribute list name。

[条件 C-74b1d4d21e4c1926](../../evidence/conditions-sets-045.md#c-74b1d4d21e4c1926) · [参数 P-69204721b34e1501](../../evidence/parameters-sets-008.md#p-69204721b34e1501) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-060038

```text
(config)# do-exec test subscriber policy epd handler disconnect-request epd-ipaddress <address> attr-list <string> <cr>
```

Handler ` RVA 0xFE7F290 `；selector ` 0 `；EOL ` RVA 0x34C53B70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Enter Session IP Address；` string ` Attribute list name。

[条件 C-a51bb04b9f29e63a](../../evidence/conditions-sets-064.md#c-a51bb04b9f29e63a) · [参数 P-c47ed38e510f496d](../../evidence/parameters-sets-015.md#p-c47ed38e510f496d) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-053541

```text
(config)# do-exec test subscriber policy epd handler stop <cr>
```

Handler ` RVA 0xFE7ECD0 `；selector ` 0 `；EOL ` RVA 0x34C53E08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c420e74db5cd33f9](../../evidence/conditions-sets-076.md#c-c420e74db5cd33f9) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-059176

```text
(config)# do-exec test subscriber policy epd session-mgmt-req activate-policy-req session-handle <number:0..4294967295> <cr>
```

Handler ` RVA 0xFE8A1B0 `；selector ` 0 `；EOL ` RVA 0x34C52850 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Enter ISG Session Handle。

[条件 C-19b0749adcf714d2](../../evidence/conditions-sets-010.md#c-19b0749adcf714d2) · [参数 P-ef7400e9df8d5866](../../evidence/parameters-sets-018.md#p-ef7400e9df8d5866) · [状态效果 S-df3cf4192951bc0e](../../evidence/state_effects-sets-047.md#s-df3cf4192951bc0e)

### path-059756

```text
(config)# do-exec test subscriber policy epd session-query-req session-ipaddress <address> epd-ipaddress <address> <cr>
```

Handler ` RVA 0xFE89C40 `；selector ` 0 `；EOL ` RVA 0x34C52328 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Enter ISG Session IP Address；` address ` Enter EPD Device IP Address。

[条件 C-f1b1a69095e7b731](../../evidence/conditions-sets-093.md#c-f1b1a69095e7b731) · [参数 P-995339be86ea8070](../../evidence/parameters-sets-012.md#p-995339be86ea8070) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-057407

```text
(config)# do-exec test subscriber policy epd session-terminate-req session-handle <number:0..4294967295> <cr>
```

Handler ` RVA 0xFE8A610 `；selector ` 0 `；EOL ` RVA 0x34C52DA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Enter ISG Session Handle。

[条件 C-e42c8ad1a3bf92cd](../../evidence/conditions-sets-088.md#c-e42c8ad1a3bf92cd) · [参数 P-bfaf933945c5acf1](../../evidence/parameters-sets-015.md#p-bfaf933945c5acf1) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-053706

```text
(config)# do-exec test subscriber policy insert circuit-id <string> <cr>
```

Handler ` RVA 0x109D50A0 `；selector ` 0 `；EOL ` RVA 0x34C575A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Circuit Id to be inserted for testing, enter "none" to disable。

[条件 C-fb772603616821d0](../../evidence/conditions-sets-097.md#c-fb772603616821d0) · [参数 P-01f789955e639dbf](../../evidence/parameters-sets-001.md#p-01f789955e639dbf) · [状态效果 S-71b66fa5e9d44418](../../evidence/state_effects-sets-024.md#s-71b66fa5e9d44418)

### path-062501

```text
(config)# do-exec test subscriber policy mlpbundle-req bundle <?general_pointer_number_action@55558a1a9ec0> session <number:0..4294967295> <cr>
```

Handler ` RVA 0x109D50A0 `；selector ` 0 `；EOL ` RVA 0x34C55F90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` First MLP link Subscriber Service Switch session id value。

[条件 C-0ccc50305a49de75](../../evidence/conditions-sets-005.md#c-0ccc50305a49de75) · [缺口 G-683891788f0963a2](../../evidence/gaps-sets-004.md#g-683891788f0963a2) · [参数 P-0aba5c74a4fe1221](../../evidence/parameters-sets-001.md#p-0aba5c74a4fe1221) · [状态效果 S-0cbdae10fa45697f](../../evidence/state_effects-sets-003.md#s-0cbdae10fa45697f)

### path-053441

```text
(config)# do-exec test subscriber policy mlplink-added session <number:0..4294967295> <cr>
```

Handler ` RVA 0x109D50A0 `；selector ` 0 `；EOL ` RVA 0x34C55B88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` MLP link Subscriber Service Switch session id value。

[条件 C-9dea6c906dca9065](../../evidence/conditions-sets-061.md#c-9dea6c906dca9065) · [参数 P-eca3557bd67d1f82](../../evidence/parameters-sets-018.md#p-eca3557bd67d1f82) · [状态效果 S-efd21f3170bd253e](../../evidence/state_effects-sets-051.md#s-efd21f3170bd253e)

### path-060032

```text
(config)# do-exec test subscriber policy policy-client session <number:0..4294967295> client Radius-Proxy event start <cr>
```

Handler ` RVA 0x109D50A0 `；selector ` 0 `；EOL ` RVA 0x34C550E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Subscriber Service Switch session id value。

[条件 C-7b65c8e91fa58e16](../../evidence/conditions-sets-048.md#c-7b65c8e91fa58e16) · [参数 P-43db9ec51cad8b99](../../evidence/parameters-sets-006.md#p-43db9ec51cad8b99) · [状态效果 S-7f49164b069bf6d4](../../evidence/state_effects-sets-027.md#s-7f49164b069bf6d4)

### path-053664

```text
(config)# do-exec test subscriber policy send-session-log session <number:0..4294967295> <cr>
```

Handler ` RVA 0x109D50A0 `；selector ` 0 `；EOL ` RVA 0x34C57200 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Subscriber Service Switch session id value。

[条件 C-135a150050e616ea](../../evidence/conditions-sets-008.md#c-135a150050e616ea) · [参数 P-2db34b641405b555](../../evidence/parameters-sets-004.md#p-2db34b641405b555) · [状态效果 S-071325ea37e5a375](../../evidence/state_effects-sets-002.md#s-071325ea37e5a375)

### path-045795

```text
(config)# do-exec test subscriber policy service-profile-download <string> <cr>
```

Handler ` RVA 0x109D50A0 `；selector ` 0 `；EOL ` RVA 0x34C54BA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` service profile key name。

[条件 C-c2801c7c26902304](../../evidence/conditions-sets-075.md#c-c2801c7c26902304) · [参数 P-6e2772433acac708](../../evidence/parameters-sets-009.md#p-6e2772433acac708) · [状态效果 S-ac1759f50995e13d](../../evidence/state_effects-sets-036.md#s-ac1759f50995e13d)

### path-059207

```text
(config)# do-exec test subscriber policy service-start session <number:0..4294967295> name <string> <cr>
```

Handler ` RVA 0x109D50A0 `；selector ` 0 `；EOL ` RVA 0x34C56E88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Subscriber Service Switch session id value；` string ` Service name to download。

[条件 C-a0ad4d43cf0cf1b8](../../evidence/conditions-sets-062.md#c-a0ad4d43cf0cf1b8) · [参数 P-9a05bf3f9bba2324](../../evidence/parameters-sets-012.md#p-9a05bf3f9bba2324) · [状态效果 S-d8dbd561f73f8127](../../evidence/state_effects-sets-046.md#s-d8dbd561f73f8127)

### path-059204

```text
(config)# do-exec test subscriber policy service-stop session <number:0..4294967295> name <string> <cr>
```

Handler ` RVA 0x109D50A0 `；selector ` 0 `；EOL ` RVA 0x34C56A88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Subscriber Service Switch session id value；` string ` Service name to download。

[条件 C-fb4246fffc93af2d](../../evidence/conditions-sets-097.md#c-fb4246fffc93af2d) · [参数 P-51e8af1a53cec40c](../../evidence/parameters-sets-007.md#p-51e8af1a53cec40c) · [状态效果 S-bcc87d0fa149264a](../../evidence/state_effects-sets-040.md#s-bcc87d0fa149264a)

### path-053518

```text
(config)# do-exec test subscriber policy session-deactivated session <number:0..4294967295> <cr>
```

Handler ` RVA 0x109D50A0 `；selector ` 0 `；EOL ` RVA 0x34C56310 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Subscriber Service Switch session id value。

[条件 C-fd4c0db705194bf5](../../evidence/conditions-sets-098.md#c-fd4c0db705194bf5) · [参数 P-806442e5184ce743](../../evidence/parameters-sets-010.md#p-806442e5184ce743) · [状态效果 S-4e84dc87005c8bff](../../evidence/state_effects-sets-017.md#s-4e84dc87005c8bff)

### path-036561

```text
(config)# do-exec test subscriber policy tcsession-req <cr>
```

Handler ` RVA 0x109D50A0 `；selector ` 0 `；EOL ` RVA 0x34C55830 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9844943ad3ba4816](../../evidence/conditions-sets-059.md#c-9844943ad3ba4816) · [状态效果 S-0c813200c279dd2f](../../evidence/state_effects-sets-003.md#s-0c813200c279dd2f)

### path-059221

```text
(config)# do-exec test subscriber policy update session <number:0..4294967295> attr-list <string> <cr>
```

Handler ` RVA 0x109D50A0 `；selector ` 0 `；EOL ` RVA 0x34C57AD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Subscriber Service Switch session id value；` string ` AAA attribute list name。

[条件 C-9315976898b97646](../../evidence/conditions-sets-057.md#c-9315976898b97646) · [参数 P-2dc1c4b05030fe7a](../../evidence/parameters-sets-004.md#p-2dc1c4b05030fe7a) · [状态效果 S-21ad4446066ef4f5](../../evidence/state_effects-sets-008.md#s-21ad4446066ef4f5)

### path-061341

```text
(config)# do-exec test sw-vlan pruning <interface> status <cr>
```

Handler ` RVA 0x15C8FDA0 `；selector ` 0 `；EOL ` RVA 0x35DFEA50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c6487464dd22c1a4](../../evidence/conditions-sets-076.md#c-c6487464dd22c1a4) · [缺口 G-b6b9b1ce41a2f5ca](../../evidence/gaps-sets-006.md#g-b6b9b1ce41a2f5ca) · [参数 P-9cb2e20eebfd85fa](../../evidence/parameters-sets-012.md#p-9cb2e20eebfd85fa) · [状态效果 S-7ae58215a43b872b](../../evidence/state_effects-sets-026.md#s-7ae58215a43b872b)

