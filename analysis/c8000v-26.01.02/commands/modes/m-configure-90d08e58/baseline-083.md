# configure · 六个基础模式的历史连接

[模式索引](README.md) · [总索引](../../README.md)

### path-055147

```text
(config)# no do-exec show ip igmp profile <number:1..4294967295> <cr>
```

Handler ` RVA 0xE7B30A0 `；selector ` 1 `；EOL ` RVA 0x3433A850 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Profile number。

[条件 C-0810e3d3bb81feb9](../../evidence/conditions-sets-003.md#c-0810e3d3bb81feb9) · [参数 P-6dcf44850ec5b755](../../evidence/parameters-sets-009.md#p-6dcf44850ec5b755) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-049255

```text
(config)# no do-exec show ip igmp snooping <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 10 `；EOL ` RVA 0x33A54C20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7c8d5e7b99f6d2b0](../../evidence/conditions-sets-048.md#c-7c8d5e7b99f6d2b0) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-058356

```text
(config)# no do-exec show ip igmp snooping bd <number:1006..4094> <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 11 `；EOL ` RVA 0x33A47310 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` BD number。

[条件 C-2c8a704b385be8b5](../../evidence/conditions-sets-017.md#c-2c8a704b385be8b5) · [参数 P-62a440c0a1746977](../../evidence/parameters-sets-008.md#p-62a440c0a1746977) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-059477

```text
(config)# no do-exec show ip igmp snooping bd <number:1006..4094> forced <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 29 `；EOL ` RVA 0x33A472E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` BD number。

[条件 C-9aa98306783ea6fa](../../evidence/conditions-sets-060.md#c-9aa98306783ea6fa) · [参数 P-62a440c0a1746977](../../evidence/parameters-sets-008.md#p-62a440c0a1746977) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055276

```text
(config)# no do-exec show ip igmp snooping counters <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 77 `；EOL ` RVA 0x33A490A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7c8d5e7b99f6d2b0](../../evidence/conditions-sets-048.md#c-7c8d5e7b99f6d2b0) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-059486

```text
(config)# no do-exec show ip igmp snooping counters bd <number:1006..4094> <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 78 `；EOL ` RVA 0x33A490E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` BD number。

[条件 C-391c5d656160a31f](../../evidence/conditions-sets-022.md#c-391c5d656160a31f) · [参数 P-14d525f738305481](../../evidence/parameters-sets-002.md#p-14d525f738305481) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-059482

```text
(config)# no do-exec show ip igmp snooping filter BD <number:1006..4094> <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 51 `；EOL ` RVA 0x33A47950 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` BD number。

[条件 C-c22c8f7988646117](../../evidence/conditions-sets-075.md#c-c22c8f7988646117) · [参数 P-dae9d46e28f0594c](../../evidence/parameters-sets-016.md#p-dae9d46e28f0594c) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-058394

```text
(config)# no do-exec show ip igmp snooping filter et <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 54 `；EOL ` RVA 0x33A47D68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8b49632dfa559c43](../../evidence/conditions-sets-054.md#c-8b49632dfa559c43) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055426

```text
(config)# no do-exec show ip igmp snooping groups <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 17 `；EOL ` RVA 0x33A4A138 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d88fbc692e48435d](../../evidence/conditions-sets-083.md#c-d88fbc692e48435d) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-058386

```text
(config)# no do-exec show ip igmp snooping groups count <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 18 `；EOL ` RVA 0x33A49CB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7c8d5e7b99f6d2b0](../../evidence/conditions-sets-048.md#c-7c8d5e7b99f6d2b0) · [状态效果 S-8a68e2a4e0b7d229](../../evidence/state_effects-sets-029.md#s-8a68e2a4e0b7d229)

### path-055533

```text
(config)# no do-exec show ip igmp snooping membership <cr>
```

Handler ` RVA 0xC31D110 `；selector ` 26 `；EOL ` RVA 0x33A5A510 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7c8d5e7b99f6d2b0](../../evidence/conditions-sets-048.md#c-7c8d5e7b99f6d2b0) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055310

```text
(config)# no do-exec show ip igmp snooping mrouter <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 12 `；EOL ` RVA 0x33A496D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7c8d5e7b99f6d2b0](../../evidence/conditions-sets-048.md#c-7c8d5e7b99f6d2b0) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-059490

```text
(config)# no do-exec show ip igmp snooping mrouter bd <number:1006..4094> <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 13 `；EOL ` RVA 0x33A49710 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` BD number。

[条件 C-f944dfdd52c0910f](../../evidence/conditions-sets-096.md#c-f944dfdd52c0910f) · [参数 P-2f4b396e2c97b79a](../../evidence/parameters-sets-004.md#p-2f4b396e2c97b79a) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055281

```text
(config)# no do-exec show ip igmp snooping querier <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 14 `；EOL ` RVA 0x33A48D68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-14f695302ab8cef3](../../evidence/conditions-sets-008.md#c-14f695302ab8cef3) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-048511

```text
(config)# no do-exec show ip igmp ssm-mapping <cr>
```

Handler ` RVA 0xF6C18D0 `；selector ` 0 `；EOL ` RVA 0x3472B6D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055017

```text
(config)# no do-exec show ip igmp static-group class-map <cr>
```

Handler ` RVA 0xF6AC4F0 `；selector ` 14 `；EOL ` RVA 0x3472C248 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-048630

```text
(config)# no do-exec show ip igmp udlr <cr>
```

Handler ` RVA 0xF6AC4F0 `；selector ` 6 `；EOL ` RVA 0x3472BA28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-048461

```text
(config)# no do-exec show ip igmp virtual-group-cache <cr>
```

Handler ` RVA 0xF6AC4F0 `；selector ` 41 `；EOL ` RVA 0x3472B3D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-047320

```text
(config)# no do-exec show ip interface address <cr>
```

Handler ` RVA 0xCF36F30 `；selector ` 0 `；EOL ` RVA 0x33D30310 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-fc7d353b58500d65](../../evidence/conditions-sets-097.md#c-fc7d353b58500d65) · [状态效果 S-784bd34a85c92ce5](../../evidence/state_effects-sets-026.md#s-784bd34a85c92ce5)

### path-038930

```text
(config)# no do-exec show ip irdp <cr>
```

Handler ` RVA 0xE242F00 `；selector ` 0 `；EOL ` RVA 0x34285418 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-3a2f6e9a1324f340](../../evidence/conditions-sets-022.md#c-3a2f6e9a1324f340) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-039385

```text
(config)# no do-exec show ip largecommunity-list <cr>
```

Handler ` RVA 0xF24B100 `；selector ` 0 `；EOL ` RVA 0x344BB208 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-2346960aeb93f3c7](../../evidence/conditions-sets-014.md#c-2346960aeb93f3c7) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-047598

```text
(config)# no do-exec show ip local policy <cr>
```

Handler ` RVA 0xFAD8CE0 `；selector ` 0 `；EOL ` RVA 0x34804760 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-047732

```text
(config)# no do-exec show ip local pool <cr>
```

Handler ` RVA 0xCEB0290 `；selector ` 0 `；EOL ` RVA 0x33D18188 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-079064ca986a3a49](../../evidence/conditions-sets-003.md#c-079064ca986a3a49) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-039037

```text
(config)# no do-exec show ip masks <cr>
```

Handler ` RVA 0xE1D6200 `；selector ` 0 `；EOL ` RVA 0x3422EDA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d310395f1ac60a7d](../../evidence/conditions-sets-081.md#c-d310395f1ac60a7d) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-039544

```text
(config)# no do-exec show ip mcache <cr>
```

Handler ` RVA 0xF6D6320 `；selector ` 0 `；EOL ` RVA 0x3474EDB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e85d0302d7ba3e1e](../../evidence/conditions-sets-090.md#c-e85d0302d7ba3e1e) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-040971

```text
(config)# no do-exec show ip mfib <cr>
```

Handler ` RVA 0x1197C6E0 `；selector ` 0 `；EOL ` RVA 0x355B5A98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-67a3bfa8448891e3](../../evidence/conditions-sets-040.md#c-67a3bfa8448891e3) · [状态效果 S-aa3b36b9f456f5b3](../../evidence/state_effects-sets-036.md#s-aa3b36b9f456f5b3)

### path-049649

```text
(config)# no do-exec show ip mfib cable <cr>
```

Handler ` RVA 0x1197DD40 `；selector ` 0 `；EOL ` RVA 0x355B4548 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-3f1bc9a945716139](../../evidence/state_effects-sets-014.md#s-3f1bc9a945716139)

### path-049735

```text
(config)# no do-exec show ip mfib interface <cr>
```

Handler ` RVA 0x1197DBC0 `；selector ` 0 `；EOL ` RVA 0x355B54B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-05d6f91ab27ef51f](../../evidence/conditions-sets-003.md#c-05d6f91ab27ef51f) · [状态效果 S-b8600c58558c15cc](../../evidence/state_effects-sets-039.md#s-b8600c58558c15cc)

### path-055490

```text
(config)# no do-exec show ip mfib internal fibidb <cr>
```

Handler ` RVA 0x1197DE80 `；selector ` 0 `；EOL ` RVA 0x355B49A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-706143aa0a5feb34](../../evidence/state_effects-sets-024.md#s-706143aa0a5feb34)

### path-055669

```text
(config)# no do-exec show ip mfib internal mem <cr>
```

Handler ` RVA 0x1197DF50 `；selector ` 0 `；EOL ` RVA 0x355B4CD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-60501d100c6c1006](../../evidence/state_effects-sets-021.md#s-60501d100c6c1006)

### path-049785

```text
(config)# no do-exec show ip mfib rate-list <cr>
```

Handler ` RVA 0x1197C6E0 `；selector ` 0 `；EOL ` RVA 0x355B5D90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b52a3045f630d0b8](../../evidence/conditions-sets-070.md#c-b52a3045f630d0b8) · [状态效果 S-b1b103d19321ecb8](../../evidence/state_effects-sets-038.md#s-b1b103d19321ecb8)

### path-049497

```text
(config)# no do-exec show ip mfib status <cr>
```

Handler ` RVA 0x1197C470 `；selector ` 0 `；EOL ` RVA 0x355B50E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-706143aa0a5feb34](../../evidence/state_effects-sets-024.md#s-706143aa0a5feb34)

### path-039772

```text
(config)# no do-exec show ip mpacket <cr>
```

Handler ` RVA 0xF70B090 `；selector ` 0 `；EOL ` RVA 0x347508C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-3362a984c2c73b4c](../../evidence/conditions-sets-020.md#c-3362a984c2c73b4c) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-049555

```text
(config)# no do-exec show ip mrib client <cr>
```

Handler ` RVA 0x119BB9A0 `；selector ` 1 `；EOL ` RVA 0x3537A9F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-455d1616a48a6d7b](../../evidence/state_effects-sets-015.md#s-455d1616a48a6d7b)

### path-058492

```text
(config)# no do-exec show ip mrib route <address> <address> <cr>
```

Handler ` RVA 0x119BD650 `；selector ` 0 `；EOL ` RVA 0x3537A398 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` source IP address；` address ` source IP address。

[条件 C-ab93dc5ba85837d8](../../evidence/conditions-sets-066.md#c-ab93dc5ba85837d8) · [参数 P-d7ab31900369f8e6](../../evidence/parameters-sets-016.md#p-d7ab31900369f8e6) · [状态效果 S-b94ea637d87c2968](../../evidence/state_effects-sets-039.md#s-b94ea637d87c2968)

### path-049739

```text
(config)# no do-exec show ip mrib route <cr>
```

Handler ` RVA 0x119BB9A0 `；selector ` 0 `；EOL ` RVA 0x35379F38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4730806389d24414](../../evidence/conditions-sets-028.md#c-4730806389d24414) · [状态效果 S-455d1616a48a6d7b](../../evidence/state_effects-sets-015.md#s-455d1616a48a6d7b)

### path-055460

```text
(config)# no do-exec show ip mrib route summary <cr>
```

Handler ` RVA 0x119BB9A0 `；selector ` 3 `；EOL ` RVA 0x35379BD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-455d1616a48a6d7b](../../evidence/state_effects-sets-015.md#s-455d1616a48a6d7b)

### path-049105

```text
(config)# no do-exec show ip mrm interface <cr>
```

Handler ` RVA 0xF671F00 `；selector ` 2 `；EOL ` RVA 0x3471FA18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-094e6a5e054b4f4a](../../evidence/conditions-sets-004.md#c-094e6a5e054b4f4a) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-049006

```text
(config)# no do-exec show ip mrm manager <cr>
```

Handler ` RVA 0xF671F00 `；selector ` 1 `；EOL ` RVA 0x3471F6A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-049102

```text
(config)# no do-exec show ip mrm status-report <cr>
```

Handler ` RVA 0xF671F00 `；selector ` 3 `；EOL ` RVA 0x3471FD18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-040320

```text
(config)# no do-exec show ip mroute <cr>
```

Handler ` RVA 0xF741DF0 `；selector ` 0 `；EOL ` RVA 0x3474F2C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1aea383d8f3532aa](../../evidence/conditions-sets-011.md#c-1aea383d8f3532aa) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-048570

```text
(config)# no do-exec show ip msdp count <cr>
```

Handler ` RVA 0xF78DB60 `；selector ` 23 `；EOL ` RVA 0x3473CBA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-058220

```text
(config)# no do-exec show ip msdp peer <address> accepted-SAs <cr>
```

Handler ` RVA 0xF78DB60 `；selector ` 27 `；EOL ` RVA 0x3473C668 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` Peer name or address。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-215ab85ec08c212f](../../evidence/parameters-sets-003.md#p-215ab85ec08c212f) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-058207

```text
(config)# no do-exec show ip msdp peer <address> advertised-SAs <cr>
```

Handler ` RVA 0xF78DB60 `；selector ` 26 `；EOL ` RVA 0x3473C3C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` Peer name or address。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-215ab85ec08c212f](../../evidence/parameters-sets-003.md#p-215ab85ec08c212f) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-048510

```text
(config)# no do-exec show ip msdp peer <cr>
```

Handler ` RVA 0xF78DB60 `；selector ` 25 `；EOL ` RVA 0x3473C380 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-054937

```text
(config)# no do-exec show ip msdp rpf-peer <address> <cr>
```

Handler ` RVA 0xF78DB60 `；selector ` 24 `；EOL ` RVA 0x3473CE70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` RP name or address。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-1e4a8b942f0e7cfd](../../evidence/parameters-sets-003.md#p-1e4a8b942f0e7cfd) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-048576

```text
(config)# no do-exec show ip msdp sa-cache <cr>
```

Handler ` RVA 0xF78DB60 `；selector ` 22 `；EOL ` RVA 0x3473BBE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-02126004a7888ab0](../../evidence/conditions-sets-001.md#c-02126004a7888ab0) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-048341

```text
(config)# no do-exec show ip msdp summary <cr>
```

Handler ` RVA 0xF78DB60 `；selector ` 21 `；EOL ` RVA 0x3473B8D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-039778

```text
(config)# no do-exec show ip multicast <cr>
```

Handler ` RVA 0xF710E60 `；selector ` 0 `；EOL ` RVA 0x34770E88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5fc63bc3602ff48f](../../evidence/conditions-sets-037.md#c-5fc63bc3602ff48f) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-054767

```text
(config)# no do-exec show ip multicast gir clients <cr>
```

Handler ` RVA 0xF710E60 `；selector ` 6 `；EOL ` RVA 0x3474C4D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-47562ebaa2bf7cd7](../../evidence/conditions-sets-028.md#c-47562ebaa2bf7cd7) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-048466

```text
(config)# no do-exec show ip multicast interface <cr>
```

Handler ` RVA 0xF710E60 `；selector ` 2 `；EOL ` RVA 0x3474D178 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c9e472e659b2c8fd](../../evidence/conditions-sets-078.md#c-c9e472e659b2c8fd) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-048516

```text
(config)# no do-exec show ip multicast limit <cr>
```

Handler ` RVA 0xF710E60 `；selector ` 1 `；EOL ` RVA 0x3474D520 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-2a3daf53dc296283](../../evidence/conditions-sets-017.md#c-2a3daf53dc296283) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-048498

```text
(config)# no do-exec show ip multicast lisp-rloc-state <cr>
```

Handler ` RVA 0xF710E60 `；selector ` 5 `；EOL ` RVA 0x3474DC58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-144740b0c080e615](../../evidence/conditions-sets-008.md#c-144740b0c080e615) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-058174

```text
(config)# no do-exec show ip multicast mpls mrib-client ipv4 <cr>
```

Handler ` RVA 0xF7114E0 `；selector ` 0 `；EOL ` RVA 0x3474C8B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f2992a11d1a58a09](../../evidence/conditions-sets-094.md#c-f2992a11d1a58a09) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-058189

```text
(config)# no do-exec show ip multicast mpls mrib-client ipv6 <cr>
```

Handler ` RVA 0xF711410 `；selector ` 0 `；EOL ` RVA 0x3474CB60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f2992a11d1a58a09](../../evidence/conditions-sets-094.md#c-f2992a11d1a58a09) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-054835

```text
(config)# no do-exec show ip multicast mpls vif <cr>
```

Handler ` RVA 0xF7113A0 `；selector ` 0 `；EOL ` RVA 0x3474CDF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f2992a11d1a58a09](../../evidence/conditions-sets-094.md#c-f2992a11d1a58a09) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-058285

```text
(config)# no do-exec show ip multicast overlay-mapping lisp <address> <cr>
```

Handler ` RVA 0xF710E60 `；selector ` 8 `；EOL ` RVA 0x3474E0E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` Overlay group address。

[条件 C-5d832276d20d451a](../../evidence/conditions-sets-036.md#c-5d832276d20d451a) · [参数 P-c33f2326c4cd42ed](../../evidence/parameters-sets-015.md#p-c33f2326c4cd42ed) · [状态效果 S-2d9e6eafec253bdf](../../evidence/state_effects-sets-010.md#s-2d9e6eafec253bdf)

### path-055385

```text
(config)# no do-exec show ip multicast redundancy ole <cr>
```

Handler ` RVA 0xD46FD80 `；selector ` 2 `；EOL ` RVA 0x33E52298 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-46fb15a3338d2e2d](../../evidence/conditions-sets-028.md#c-46fb15a3338d2e2d) · [状态效果 S-4a73a7902bb2e6fa](../../evidence/state_effects-sets-016.md#s-4a73a7902bb2e6fa)

### path-058368

```text
(config)# no do-exec show ip multicast redundancy reachability summary <cr>
```

Handler ` RVA 0xD46FD80 `；selector ` 3 `；EOL ` RVA 0x33E51F38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4a278267a3443ff0](../../evidence/conditions-sets-029.md#c-4a278267a3443ff0) · [状态效果 S-3b3d14ac35dc6535](../../evidence/state_effects-sets-013.md#s-3b3d14ac35dc6535)

### path-055207

```text
(config)# no do-exec show ip multicast redundancy state <cr>
```

Handler ` RVA 0xD46FD80 `；selector ` 0 `；EOL ` RVA 0x33E51948 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5fc63bc3602ff48f](../../evidence/conditions-sets-037.md#c-5fc63bc3602ff48f) · [状态效果 S-4a73a7902bb2e6fa](../../evidence/state_effects-sets-016.md#s-4a73a7902bb2e6fa)

### path-055195

```text
(config)# no do-exec show ip multicast redundancy statistics <cr>
```

Handler ` RVA 0xD46FD80 `；selector ` 1 `；EOL ` RVA 0x33E51BE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5fc63bc3602ff48f](../../evidence/conditions-sets-037.md#c-5fc63bc3602ff48f) · [状态效果 S-4a73a7902bb2e6fa](../../evidence/state_effects-sets-016.md#s-4a73a7902bb2e6fa)

### path-054763

```text
(config)# no do-exec show ip multicast rpf monitored <cr>
```

Handler ` RVA 0xF710E60 `；selector ` 3 `；EOL ` RVA 0x3474C188 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-059460

```text
(config)# no do-exec show ip multicast snooping limit vlan <number:1..4095> <cr>
```

Handler ` RVA 0xC361C10 `；selector ` 60 `；EOL ` RVA 0x33A5DEF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Vlan number。

[条件 C-5fc63bc3602ff48f](../../evidence/conditions-sets-037.md#c-5fc63bc3602ff48f) · [参数 P-236b3a3e749d1c7b](../../evidence/parameters-sets-003.md#p-236b3a3e749d1c7b) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055166

```text
(config)# no do-exec show ip multicast snooping summary <cr>
```

Handler ` RVA 0xC361C10 `；selector ` 70 `；EOL ` RVA 0x33A5E1F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5fc63bc3602ff48f](../../evidence/conditions-sets-037.md#c-5fc63bc3602ff48f) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-059466

```text
(config)# no do-exec show ip multicast snooping summary vlan <number:1..4095> <cr>
```

Handler ` RVA 0xC361C10 `；selector ` 68 `；EOL ` RVA 0x33A5E230 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Vlan number。

[条件 C-5fc63bc3602ff48f](../../evidence/conditions-sets-037.md#c-5fc63bc3602ff48f) · [参数 P-0e6e0511934953b5](../../evidence/parameters-sets-002.md#p-0e6e0511934953b5) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-048618

```text
(config)# no do-exec show ip multicast timer <cr>
```

Handler ` RVA 0xF710E60 `；selector ` 7 `；EOL ` RVA 0x3474E490 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-171912744b2da9bb](../../evidence/conditions-sets-009.md#c-171912744b2da9bb) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-048753

```text
(config)# no do-exec show ip multicast topology <cr>
```

Handler ` RVA 0xF710E60 `；selector ` 4 `；EOL ` RVA 0x3474D988 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d4ef608d9b63ee89](../../evidence/conditions-sets-082.md#c-d4ef608d9b63ee89) · [状态效果 S-8d3e620b65b64607](../../evidence/state_effects-sets-030.md#s-8d3e620b65b64607)

### path-038225

```text
(config)# no do-exec show ip name-servers <cr>
```

Handler ` RVA 0xCF2CF20 `；selector ` 2 `；EOL ` RVA 0x33D328D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055431

```text
(config)# no do-exec show ip nat aggregation top-100-allocator <cr>
```

Handler ` RVA 0xFA2EB90 `；selector ` 9 `；EOL ` RVA 0x347DB178 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0b4c84c7c32d7af9](../../evidence/conditions-sets-005.md#c-0b4c84c7c32d7af9) · [状态效果 S-71666d36853f200d](../../evidence/state_effects-sets-024.md#s-71666d36853f200d)

### path-049674

```text
(config)# no do-exec show ip nat alias-usecount <cr>
```

Handler ` RVA 0xFA2EB90 `；selector ` 10 `；EOL ` RVA 0x347DC148 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-38fb4afe68da981d](../../evidence/conditions-sets-022.md#c-38fb4afe68da981d) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-049290

```text
(config)# no do-exec show ip nat bpa <cr>
```

Handler ` RVA 0xFA2EB90 `；selector ` 5 `；EOL ` RVA 0x347DA9E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7028274df1d580ca](../../evidence/conditions-sets-043.md#c-7028274df1d580ca) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055561

```text
(config)# no do-exec show ip nat dia track <cr>
```

Handler ` RVA 0xFA2EB90 `；selector ` 12 `；EOL ` RVA 0x347DBB90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-54ffd23a7032a3ef](../../evidence/conditions-sets-033.md#c-54ffd23a7032a3ef) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-049633

```text
(config)# no do-exec show ip nat entry-static <cr>
```

Handler ` RVA 0xFA2EB90 `；selector ` 11 `；EOL ` RVA 0x347DBE60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f84eae1da57a0881](../../evidence/conditions-sets-096.md#c-f84eae1da57a0881) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-049767

```text
(config)# no do-exec show ip nat ha <cr>
```

Handler ` RVA 0x10C06B70 `；selector ` 0 `；EOL ` RVA 0x34CE8678 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-255475745bdb7c9b](../../evidence/conditions-sets-015.md#c-255475745bdb7c9b) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-058491

```text
(config)# no do-exec show ip nat ha inside destination <cr>
```

Handler ` RVA 0x10C06B70 `；selector ` 7 `；EOL ` RVA 0x34CE71F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0e43a703bb752aad](../../evidence/conditions-sets-006.md#c-0e43a703bb752aad) · [状态效果 S-1318921be92c785c](../../evidence/state_effects-sets-004.md#s-1318921be92c785c)

### path-059908

```text
(config)# no do-exec show ip nat ha inside destination list <number:1..2699> <cr>
```

Handler ` RVA 0x10C06B70 `；selector ` 6 `；EOL ` RVA 0x34CE7230 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Access list number for global addresses。

[条件 C-0e43a703bb752aad](../../evidence/conditions-sets-006.md#c-0e43a703bb752aad) · [参数 P-9c7276b446f8ff6f](../../evidence/parameters-sets-012.md#p-9c7276b446f8ff6f) · [状态效果 S-1318921be92c785c](../../evidence/state_effects-sets-004.md#s-1318921be92c785c)

### path-058485

```text
(config)# no do-exec show ip nat ha inside source <cr>
```

Handler ` RVA 0x10C06B70 `；selector ` 3 `；EOL ` RVA 0x34CE5E98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-760a5fe5ffc8a104](../../evidence/conditions-sets-046.md#c-760a5fe5ffc8a104) · [状态效果 S-e4ad200a728f7521](../../evidence/state_effects-sets-048.md#s-e4ad200a728f7521)

### path-058506

```text
(config)# no do-exec show ip nat ha inside source <cr>
```

Handler ` RVA 0x10C06B70 `；selector ` 5 `；EOL ` RVA 0x34CE6298 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5047286dcd88b236](../../evidence/conditions-sets-031.md#c-5047286dcd88b236) · [状态效果 S-e4ad200a728f7521](../../evidence/state_effects-sets-048.md#s-e4ad200a728f7521)

### path-060102

```text
(config)# no do-exec show ip nat ha inside source static <address> <address> <cr>
```

Handler ` RVA 0x10C06B70 `；selector ` 4 `；EOL ` RVA 0x34CE64A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` Inside local IP address；` address ` Inside global IP address。

[条件 C-5047286dcd88b236](../../evidence/conditions-sets-031.md#c-5047286dcd88b236) · [参数 P-93cfcae875ad4313](../../evidence/parameters-sets-011.md#p-93cfcae875ad4313) · [状态效果 S-e4ad200a728f7521](../../evidence/state_effects-sets-048.md#s-e4ad200a728f7521)

### path-055635

```text
(config)# no do-exec show ip nat ha mappings <cr>
```

Handler ` RVA 0x10C06B70 `；selector ` 11 `；EOL ` RVA 0x34CE8650 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-255475745bdb7c9b](../../evidence/conditions-sets-015.md#c-255475745bdb7c9b) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-058514

```text
(config)# no do-exec show ip nat ha outside source <cr>
```

Handler ` RVA 0x10C06B70 `；selector ` 10 `；EOL ` RVA 0x34CE7D80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-255475745bdb7c9b](../../evidence/conditions-sets-015.md#c-255475745bdb7c9b) · [状态效果 S-f5de9065bc31b2e7](../../evidence/state_effects-sets-052.md#s-f5de9065bc31b2e7)

### path-059910

```text
(config)# no do-exec show ip nat ha outside source list <number:1..2699> <cr>
```

Handler ` RVA 0x10C06B70 `；selector ` 8 `；EOL ` RVA 0x34CE79C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Access list number for global addresses。

[条件 C-255475745bdb7c9b](../../evidence/conditions-sets-015.md#c-255475745bdb7c9b) · [参数 P-b102d76a95775281](../../evidence/parameters-sets-013.md#p-b102d76a95775281) · [状态效果 S-f5de9065bc31b2e7](../../evidence/state_effects-sets-052.md#s-f5de9065bc31b2e7)

### path-060100

```text
(config)# no do-exec show ip nat ha outside source static <address> <address> <cr>
```

Handler ` RVA 0x10C06B70 `；selector ` 9 `；EOL ` RVA 0x34CE7F08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` Outside global IP address；` address ` Outside local IP address。

[条件 C-255475745bdb7c9b](../../evidence/conditions-sets-015.md#c-255475745bdb7c9b) · [参数 P-bac6837be306eb44](../../evidence/parameters-sets-014.md#p-bac6837be306eb44) · [状态效果 S-f5de9065bc31b2e7](../../evidence/state_effects-sets-052.md#s-f5de9065bc31b2e7)

### path-055572

```text
(config)# no do-exec show ip nat ha pool <cr>
```

Handler ` RVA 0x10C06B70 `；selector ` 2 `；EOL ` RVA 0x34CE57E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-2a8a9262f1a89162](../../evidence/conditions-sets-017.md#c-2a8a9262f1a89162) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-058458

```text
(config)# no do-exec show ip nat ha pool <string> <cr>
```

Handler ` RVA 0x10C06B70 `；selector ` 1 `；EOL ` RVA 0x34CE57C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Pool name。

[条件 C-2a8a9262f1a89162](../../evidence/conditions-sets-017.md#c-2a8a9262f1a89162) · [参数 P-9337e862cefa55d7](../../evidence/parameters-sets-011.md#p-9337e862cefa55d7) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055484

```text
(config)# no do-exec show ip nat limits all-host <cr>
```

Handler ` RVA 0xFA2EB90 `；selector ` 4 `；EOL ` RVA 0x347DA148 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-50b8bb48fe758e80](../../evidence/conditions-sets-032.md#c-50b8bb48fe758e80) · [状态效果 S-d03fe163f7b528fa](../../evidence/state_effects-sets-044.md#s-d03fe163f7b528fa)

### path-049513

```text
(config)# no do-exec show ip nat map <cr>
```

Handler ` RVA 0xFA2EB90 `；selector ` 7 `；EOL ` RVA 0x347DB578 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-dc8f64116004688f](../../evidence/conditions-sets-085.md#c-dc8f64116004688f) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-049151

```text
(config)# no do-exec show ip nat platform <cr>
```

Handler ` RVA 0xFA2EB90 `；selector ` 3 `；EOL ` RVA 0x347D94C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055468

```text
(config)# no do-exec show ip nat pool platform <cr>
```

Handler ` RVA 0xFA2EB90 `；selector ` 6 `；EOL ` RVA 0x347DADD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-6d794e298b82915c](../../evidence/conditions-sets-042.md#c-6d794e298b82915c) · [状态效果 S-960477020ba47de0](../../evidence/state_effects-sets-032.md#s-960477020ba47de0)

### path-055350

```text
(config)# no do-exec show ip nat portblock pat <cr>
```

Handler ` RVA 0xFA2EB90 `；selector ` 2 `；EOL ` RVA 0x347D9910 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-aadf07f045e24108](../../evidence/conditions-sets-066.md#c-aadf07f045e24108) · [状态效果 S-231998c85e262ff2](../../evidence/state_effects-sets-008.md#s-231998c85e262ff2)

### path-049544

```text
(config)# no do-exec show ip nat route-dia <cr>
```

Handler ` RVA 0xFA2EB90 `；selector ` 8 `；EOL ` RVA 0x347DB840 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ca48db494d58b37a](../../evidence/conditions-sets-078.md#c-ca48db494d58b37a) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-049244

```text
(config)# no do-exec show ip nat statistics <cr>
```

Handler ` RVA 0xFA2EB90 `；selector ` 1 `；EOL ` RVA 0x347DA700 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-88bfb62346132430](../../evidence/conditions-sets-053.md#c-88bfb62346132430) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-049877

```text
(config)# no do-exec show ip nat status <cr>
```

Handler ` RVA 0xFA2FB50 `；selector ` 0 `；EOL ` RVA 0x347DC440 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c5343b7627bf42ff](../../evidence/conditions-sets-076.md#c-c5343b7627bf42ff) · [状态效果 S-d9f0c9507d5d3245](../../evidence/state_effects-sets-046.md#s-d9f0c9507d5d3245)

### path-049654

```text
(config)# no do-exec show ip nat translations <cr>
```

Handler ` RVA 0xFA2EB90 `；selector ` 0 `；EOL ` RVA 0x347D7750 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-3bb115fc3f9a9f89](../../evidence/conditions-sets-023.md#c-3bb115fc3f9a9f89) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-048740

```text
(config)# no do-exec show ip nbar attribute <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 19 `；EOL ` RVA 0x35246A70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-048992

```text
(config)# no do-exec show ip nbar attribute-custom <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 36 `；EOL ` RVA 0x35248AD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-15bbd038c1ed607a](../../evidence/conditions-sets-009.md#c-15bbd038c1ed607a) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-049014

```text
(config)# no do-exec show ip nbar attribute-map <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 26 `；EOL ` RVA 0x35248618 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-15bbd038c1ed607a](../../evidence/conditions-sets-009.md#c-15bbd038c1ed607a) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055146

```text
(config)# no do-exec show ip nbar attribute-map <string> <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 25 `；EOL ` RVA 0x352485F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Attribute Map name。

[条件 C-15bbd038c1ed607a](../../evidence/conditions-sets-009.md#c-15bbd038c1ed607a) · [参数 P-00d2c85d1e33763e](../../evidence/parameters-sets-001.md#p-00d2c85d1e33763e) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-060092

```text
(config)# no do-exec show ip nbar classification cache sync export format table <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 54 `；EOL ` RVA 0x352440D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1b75c7a76044d989](../../evidence/conditions-sets-011.md#c-1b75c7a76044d989) · [状态效果 S-d680cbdef3756aa7](../../evidence/state_effects-sets-045.md#s-d680cbdef3756aa7)

### path-059886

```text
(config)# no do-exec show ip nbar classification cache sync import last <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 57 `；EOL ` RVA 0x35244498 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f3135ca154eb94d3](../../evidence/conditions-sets-094.md#c-f3135ca154eb94d3) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-058269

```text
(config)# no do-exec show ip nbar classification dns learning <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 44 `；EOL ` RVA 0x35243730 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-059889

```text
(config)# no do-exec show ip nbar classification dns learning cache <number:1..100000> <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 45 `；EOL ` RVA 0x352428C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Number of entries to show。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-7e5a6912abbf67f4](../../evidence/parameters-sets-010.md#p-7e5a6912abbf67f4) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-060084

```text
(config)# no do-exec show ip nbar classification dns learning cache <number:1..100000> unclassified <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 50 `；EOL ` RVA 0x352428A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Number of entries to show。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-7e5a6912abbf67f4](../../evidence/parameters-sets-010.md#p-7e5a6912abbf67f4) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-060087

```text
(config)# no do-exec show ip nbar classification dns learning cache clients-servers <number:1..100000> <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 46 `；EOL ` RVA 0x35242E78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Number of entries to show。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-c79de3b2a66f150c](../../evidence/parameters-sets-015.md#p-c79de3b2a66f150c) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-060085

```text
(config)# no do-exec show ip nbar classification dns learning cache ip-address <address> <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 47 `；EOL ` RVA 0x35243470 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` IPv4 address。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-d80f378e85a44dd1](../../evidence/parameters-sets-016.md#p-d80f378e85a44dd1) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-059449

```text
(config)# no do-exec show ip nbar classification dns learning stats <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 51 `；EOL ` RVA 0x35243708 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-054954

```text
(config)# no do-exec show ip nbar classification granularity <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 38 `；EOL ` RVA 0x35241B70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-058236

```text
(config)# no do-exec show ip nbar classification granularity protocol <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 40 `；EOL ` RVA 0x35241BD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-058259

```text
(config)# no do-exec show ip nbar classification socket-cache <number:1..100000> <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 52 `；EOL ` RVA 0x35244788 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Number of sockets to show。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-6099c4f0a96ec586](../../evidence/parameters-sets-008.md#p-6099c4f0a96ec586) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-058296

```text
(config)# no do-exec show ip nbar classification socket-cache pl-sockets <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 53 `；EOL ` RVA 0x35244A78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-048379

```text
(config)# no do-exec show ip nbar control-plane <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 42 `；EOL ` RVA 0x35241228 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-054984

```text
(config)# no do-exec show ip nbar function <string> <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 37 `；EOL ` RVA 0x35244E10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Function name。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-d038cc713a4324ff](../../evidence/parameters-sets-016.md#p-d038cc713a4324ff) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-048875

```text
(config)# no do-exec show ip nbar link-age <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 3 `；EOL ` RVA 0x35247FD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-054883

```text
(config)# no do-exec show ip nbar npc detail <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 64 `；EOL ` RVA 0x35241538 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-854194c0c939e8a4](../../evidence/conditions-sets-052.md#c-854194c0c939e8a4) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-054918

```text
(config)# no do-exec show ip nbar npc summary <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 65 `；EOL ` RVA 0x352417E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-72464d489fbf4778](../../evidence/conditions-sets-044.md#c-72464d489fbf4778) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055059

```text
(config)# no do-exec show ip nbar parameter extraction <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 34 `；EOL ` RVA 0x352459A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-058263

```text
(config)# no do-exec show ip nbar parameter extraction activated <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 35 `；EOL ` RVA 0x35245980 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055091

```text
(config)# no do-exec show ip nbar parameter subclassification <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 32 `；EOL ` RVA 0x352464E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-058277

```text
(config)# no do-exec show ip nbar parameter subclassification activated <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 33 `；EOL ` RVA 0x352464C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-048806

```text
(config)# no do-exec show ip nbar protocol-attribute <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 22 `；EOL ` RVA 0x352479E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-049738

```text
(config)# no do-exec show ip nbar protocol-discovery <cr>
```

Handler ` RVA 0x10F338B0 `；selector ` 0 `；EOL ` RVA 0x3524DED0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e6f7f47de2d1d824](../../evidence/conditions-sets-089.md#c-e6f7f47de2d1d824) · [状态效果 S-1ab685ba14f58e43](../../evidence/state_effects-sets-006.md#s-1ab685ba14f58e43)

### path-049146

```text
(config)# no do-exec show ip nbar protocol-id <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 0 `；EOL ` RVA 0x3524BA08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c732dccb57f95a83](../../evidence/conditions-sets-077.md#c-c732dccb57f95a83) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055388

```text
(config)# no do-exec show ip nbar protocol-pack <string> <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 12 `；EOL ` RVA 0x3524AEE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` NBAR protocol pack name。

[条件 C-cc4851d76a450c9a](../../evidence/conditions-sets-079.md#c-cc4851d76a450c9a) · [参数 P-ee2b771004345552](../../evidence/parameters-sets-018.md#p-ee2b771004345552) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-058385

```text
(config)# no do-exec show ip nbar protocol-pack <string> detail <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 11 `；EOL ` RVA 0x3524AC10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` NBAR protocol pack name。

[条件 C-cc4851d76a450c9a](../../evidence/conditions-sets-079.md#c-cc4851d76a450c9a) · [参数 P-ee2b771004345552](../../evidence/parameters-sets-018.md#p-ee2b771004345552) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-058404

```text
(config)# no do-exec show ip nbar protocol-pack <string> taxonomy <cr>
```

Handler ` RVA 0x10F21F60 `；selector ` 13 `；EOL ` RVA 0x3524AEB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` NBAR protocol pack name。

[条件 C-cc4851d76a450c9a](../../evidence/conditions-sets-079.md#c-cc4851d76a450c9a) · [参数 P-ee2b771004345552](../../evidence/parameters-sets-018.md#p-ee2b771004345552) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055241

```text
(config)# no do-exec show ip nbar protocol-pack active <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 5 `；EOL ` RVA 0x35249130 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b60cb66f0ecc6c89](../../evidence/conditions-sets-070.md#c-b60cb66f0ecc6c89) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-058322

```text
(config)# no do-exec show ip nbar protocol-pack active detail <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 4 `；EOL ` RVA 0x35248E60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b60cb66f0ecc6c89](../../evidence/conditions-sets-070.md#c-b60cb66f0ecc6c89) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-058340

```text
(config)# no do-exec show ip nbar protocol-pack active taxonomy <cr>
```

Handler ` RVA 0x10F21F60 `；selector ` 14 `；EOL ` RVA 0x35249108 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b60cb66f0ecc6c89](../../evidence/conditions-sets-070.md#c-b60cb66f0ecc6c89) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055280

```text
(config)# no do-exec show ip nbar protocol-pack inactive <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 7 `；EOL ` RVA 0x35249940 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b60cb66f0ecc6c89](../../evidence/conditions-sets-070.md#c-b60cb66f0ecc6c89) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-058338

```text
(config)# no do-exec show ip nbar protocol-pack inactive detail <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 6 `；EOL ` RVA 0x35249670 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b60cb66f0ecc6c89](../../evidence/conditions-sets-070.md#c-b60cb66f0ecc6c89) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-058376

```text
(config)# no do-exec show ip nbar protocol-pack inactive taxonomy <cr>
```

Handler ` RVA 0x10F21F60 `；selector ` 16 `；EOL ` RVA 0x352499A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b60cb66f0ecc6c89](../../evidence/conditions-sets-070.md#c-b60cb66f0ecc6c89) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-059475

```text
(config)# no do-exec show ip nbar protocol-pack inactive taxonomy <string> <cr>
```

Handler ` RVA 0x10F21F60 `；selector ` 15 `；EOL ` RVA 0x35249980 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` NBAR inactive protocol pack name。

[条件 C-b60cb66f0ecc6c89](../../evidence/conditions-sets-070.md#c-b60cb66f0ecc6c89) · [参数 P-677a9bb0ef608bac](../../evidence/parameters-sets-008.md#p-677a9bb0ef608bac) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055313

```text
(config)# no do-exec show ip nbar protocol-pack loaded <cr>
```

Handler ` RVA 0x10F21F60 `；selector ` 9 `；EOL ` RVA 0x3524A3F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b60cb66f0ecc6c89](../../evidence/conditions-sets-070.md#c-b60cb66f0ecc6c89) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-058349

```text
(config)# no do-exec show ip nbar protocol-pack loaded detail <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 8 `；EOL ` RVA 0x3524A128 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b60cb66f0ecc6c89](../../evidence/conditions-sets-070.md#c-b60cb66f0ecc6c89) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-058393

```text
(config)# no do-exec show ip nbar protocol-pack loaded taxonomy <cr>
```

Handler ` RVA 0x10F21F60 `；selector ` 18 `；EOL ` RVA 0x3524A460 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b60cb66f0ecc6c89](../../evidence/conditions-sets-070.md#c-b60cb66f0ecc6c89) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-059480

```text
(config)# no do-exec show ip nbar protocol-pack loaded taxonomy <string> <cr>
```

Handler ` RVA 0x10F21F60 `；selector ` 17 `；EOL ` RVA 0x3524A438 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` NBAR loaded protocol pack name。

[条件 C-b60cb66f0ecc6c89](../../evidence/conditions-sets-070.md#c-b60cb66f0ecc6c89) · [参数 P-658de79b2d501530](../../evidence/parameters-sets-008.md#p-658de79b2d501530) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-049305

```text
(config)# no do-exec show ip nbar resources <cr>
```

Handler ` RVA 0x10F3B120 `；selector ` 20 `；EOL ` RVA 0x3524C368 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7aaa3653baa5e431](../../evidence/conditions-sets-048.md#c-7aaa3653baa5e431) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055367

```text
(config)# no do-exec show ip nbar resources flow <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 24 `；EOL ` RVA 0x3524C058 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-85bd44377217f3f3](../../evidence/conditions-sets-052.md#c-85bd44377217f3f3) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055483

```text
(config)# no do-exec show ip nbar resources status <cr>
```

Handler ` RVA 0x10F3B120 `；selector ` 19 `；EOL ` RVA 0x3524CE80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7aaa3653baa5e431](../../evidence/conditions-sets-048.md#c-7aaa3653baa5e431) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-058444

```text
(config)# no do-exec show ip nbar resources status <number:10..86400> <cr>
```

Handler ` RVA 0x10F219A0 `；selector ` 22 `；EOL ` RVA 0x3524CEF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Specify age of links (to indicate which bucket)。

[条件 C-7aaa3653baa5e431](../../evidence/conditions-sets-048.md#c-7aaa3653baa5e431) · [参数 P-49c60d7b54c4f3ee](../../evidence/parameters-sets-006.md#p-49c60d7b54c4f3ee) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-059497

```text
(config)# no do-exec show ip nbar resources status <number:10..86400> <number:1..50> <cr>
```

Handler ` RVA 0x10F21F60 `；selector ` 23 `；EOL ` RVA 0x3524CEC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Specify age of links (to indicate which bucket)；` unsigned_number ` Number of links to view。

[条件 C-7aaa3653baa5e431](../../evidence/conditions-sets-048.md#c-7aaa3653baa5e431) · [参数 P-d71cbaf17a27d2ca](../../evidence/parameters-sets-016.md#p-d71cbaf17a27d2ca) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-058432

```text
(config)# no do-exec show ip nbar resources status fadebucket <cr>
```

Handler ` RVA 0x10F21F60 `；selector ` 24 `；EOL ` RVA 0x3524C990 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7aaa3653baa5e431](../../evidence/conditions-sets-048.md#c-7aaa3653baa5e431) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-059495

```text
(config)# no do-exec show ip nbar resources status fadebucket <number:1..50> <cr>
```

Handler ` RVA 0x10F21F60 `；selector ` 25 `；EOL ` RVA 0x3524C968 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Number of links to view。

[条件 C-7aaa3653baa5e431](../../evidence/conditions-sets-048.md#c-7aaa3653baa5e431) · [参数 P-663e50933124a4cf](../../evidence/parameters-sets-008.md#p-663e50933124a4cf) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-058424

```text
(config)# no do-exec show ip nbar resources status freebucket <cr>
```

Handler ` RVA 0x10F21F60 `；selector ` 26 `；EOL ` RVA 0x3524C438 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7aaa3653baa5e431](../../evidence/conditions-sets-048.md#c-7aaa3653baa5e431) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-059492

```text
(config)# no do-exec show ip nbar resources status freebucket <number:1..50> <cr>
```

Handler ` RVA 0x10F21F60 `；selector ` 27 `；EOL ` RVA 0x3524C410 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Number of links to view。

[条件 C-7aaa3653baa5e431](../../evidence/conditions-sets-048.md#c-7aaa3653baa5e431) · [参数 P-911a5d92236ca3a7](../../evidence/parameters-sets-011.md#p-911a5d92236ca3a7) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-049098

```text
(config)# no do-exec show ip nbar statistics <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 27 `；EOL ` RVA 0x3524B6C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-cbfce9c3d822aac3](../../evidence/conditions-sets-078.md#c-cbfce9c3d822aac3) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-048993

```text
(config)# no do-exec show ip nbar version <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 1 `；EOL ` RVA 0x3524B3E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b60cb66f0ecc6c89](../../evidence/conditions-sets-070.md#c-b60cb66f0ecc6c89) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-040847

```text
(config)# no do-exec show ip nhrp <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 0 `；EOL ` RVA 0x347F2000 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-12bcabe6c53f20cb](../../evidence/conditions-sets-007.md#c-12bcabe6c53f20cb) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-049347

```text
(config)# no do-exec show ip nhrp attribute <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 16 `；EOL ` RVA 0x347F5C28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-049464

```text
(config)# no do-exec show ip nhrp instances <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 20 `；EOL ` RVA 0x347F5F38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-770e74c752988f72](../../evidence/conditions-sets-046.md#c-770e74c752988f72) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-049416

```text
(config)# no do-exec show ip nhrp map <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 17 `；EOL ` RVA 0x347F5968 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a94bf2d8f05cab4e](../../evidence/conditions-sets-065.md#c-a94bf2d8f05cab4e) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-049521

```text
(config)# no do-exec show ip nhrp multicast <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 4 `；EOL ` RVA 0x347F5548 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7e510ef18eef196c](../../evidence/conditions-sets-049.md#c-7e510ef18eef196c) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-049424

```text
(config)# no do-exec show ip nhrp nhs <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 3 `；EOL ` RVA 0x347F4350 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-dfc4c5caa34e67fb](../../evidence/conditions-sets-086.md#c-dfc4c5caa34e67fb) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055553

```text
(config)# no do-exec show ip nhrp nhs redundancy <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 10 `；EOL ` RVA 0x347F4EB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-dfc4c5caa34e67fb](../../evidence/conditions-sets-086.md#c-dfc4c5caa34e67fb) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-059499

```text
(config)# no do-exec show ip nhrp nhs redundancy cluster <number:0..10> <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 14 `；EOL ` RVA 0x347F4958 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` NHS cluster number。

[条件 C-dfc4c5caa34e67fb](../../evidence/conditions-sets-086.md#c-dfc4c5caa34e67fb) · [参数 P-133a9e4b186bdac7](../../evidence/parameters-sets-002.md#p-133a9e4b186bdac7) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-058448

```text
(config)# no do-exec show ip nhrp nhs redundancy preempted <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 12 `；EOL ` RVA 0x347F4BE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-dfc4c5caa34e67fb](../../evidence/conditions-sets-086.md#c-dfc4c5caa34e67fb) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-058428

```text
(config)# no do-exec show ip nhrp nhs redundancy running <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 11 `；EOL ` RVA 0x347F4648 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-dfc4c5caa34e67fb](../../evidence/conditions-sets-086.md#c-dfc4c5caa34e67fb) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-058456

```text
(config)# no do-exec show ip nhrp nhs redundancy waiting <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 13 `；EOL ` RVA 0x347F4E88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-dfc4c5caa34e67fb](../../evidence/conditions-sets-086.md#c-dfc4c5caa34e67fb) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-049131

```text
(config)# no do-exec show ip nhrp purge <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 2 `；EOL ` RVA 0x347F3F80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-049642

```text
(config)# no do-exec show ip nhrp redirect <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 6 `；EOL ` RVA 0x347F1958 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055560

```text
(config)# no do-exec show ip nhrp redirect statistics <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 7 `；EOL ` RVA 0x347F1930 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-049632

```text
(config)# no do-exec show ip nhrp shortcut <cr>
```

Handler ` RVA 0x108FE580 `；selector ` 0 `；EOL ` RVA 0x34BF8EE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-677ec0f54d868499](../../evidence/state_effects-sets-022.md#s-677ec0f54d868499)

### path-049429

```text
(config)# no do-exec show ip nhrp stats <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 18 `；EOL ` RVA 0x347F3B90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-50ed8a211b890947](../../evidence/conditions-sets-032.md#c-50ed8a211b890947) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-049200

```text
(config)# no do-exec show ip nhrp traffic <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 1 `；EOL ` RVA 0x347F3670 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-040848

```text
(config)# no do-exec show ip ospf <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 7 `；EOL ` RVA 0x34892168 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1a5803a3a1c9b578](../../evidence/conditions-sets-010.md#c-1a5803a3a1c9b578) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-048773

```text
(config)# no do-exec show ip ospf bad-checksum <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 1 `；EOL ` RVA 0x3487AD60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-049422

```text
(config)# no do-exec show ip ospf border-routers <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 17 `；EOL ` RVA 0x348788A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d236fddacacd7923](../../evidence/conditions-sets-081.md#c-d236fddacacd7923) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-050091

```text
(config)# no do-exec show ip ospf database <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 58 `；EOL ` RVA 0x34895630 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-264cdf48d35a5449](../../evidence/conditions-sets-015.md#c-264cdf48d35a5449) · [状态效果 S-35ffdf87aa79c84e](../../evidence/state_effects-sets-012.md#s-35ffdf87aa79c84e)

### path-055807

```text
(config)# no do-exec show ip ospf database database-summary <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 60 `；EOL ` RVA 0x34896290 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5f09beff6301b7c5](../../evidence/conditions-sets-037.md#c-5f09beff6301b7c5) · [状态效果 S-35ffdf87aa79c84e](../../evidence/state_effects-sets-012.md#s-35ffdf87aa79c84e)

### path-058601

```text
(config)# no do-exec show ip ospf database database-summary detail <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 54 `；EOL ` RVA 0x348965B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0a8c31475b28564f](../../evidence/conditions-sets-004.md#c-0a8c31475b28564f) · [状态效果 S-3d8fa5991dbba07c](../../evidence/state_effects-sets-014.md#s-3d8fa5991dbba07c)

### path-049687

```text
(config)# no do-exec show ip ospf delete-list <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 57 `；EOL ` RVA 0x34876370 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d236fddacacd7923](../../evidence/conditions-sets-081.md#c-d236fddacacd7923) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-048937

```text
(config)# no do-exec show ip ospf events <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 16 `；EOL ` RVA 0x348769F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d601d8d07dd98107](../../evidence/conditions-sets-083.md#c-d601d8d07dd98107) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-049895

```text
(config)# no do-exec show ip ospf flood-list <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 66 `；EOL ` RVA 0x34890B28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-654fe22627967429](../../evidence/conditions-sets-039.md#c-654fe22627967429) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-049922

```text
(config)# no do-exec show ip ospf interface <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 65 `；EOL ` RVA 0x3488FEC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-64e9a11a490d9d30](../../evidence/conditions-sets-039.md#c-64e9a11a490d9d30) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055783

```text
(config)# no do-exec show ip ospf internal forwarding-addresses <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 23 `；EOL ` RVA 0x34891EA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d236fddacacd7923](../../evidence/conditions-sets-081.md#c-d236fddacacd7923) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-058559

```text
(config)# no do-exec show ip ospf internal memory cache <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 2 `；EOL ` RVA 0x34891C10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d236fddacacd7923](../../evidence/conditions-sets-081.md#c-d236fddacacd7923) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-049517

```text
(config)# no do-exec show ip ospf max-metric <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 10 `；EOL ` RVA 0x34879EC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d236fddacacd7923](../../evidence/conditions-sets-081.md#c-d236fddacacd7923) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-049455

```text
(config)# no do-exec show ip ospf maxage-list <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 9 `；EOL ` RVA 0x3487A410 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d236fddacacd7923](../../evidence/conditions-sets-081.md#c-d236fddacacd7923) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-058510

```text
(config)# no do-exec show ip ospf mpls traffic-eng link <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 61 `；EOL ` RVA 0x3488F830 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d236fddacacd7923](../../evidence/conditions-sets-081.md#c-d236fddacacd7923) · [状态效果 S-6a9fc866e3d9784d](../../evidence/state_effects-sets-023.md#s-6a9fc866e3d9784d)

### path-049095

```text
(config)# no do-exec show ip ospf multi-area <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 68 `；EOL ` RVA 0x348775F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b28cfdb94256e16e](../../evidence/conditions-sets-069.md#c-b28cfdb94256e16e) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-050056

```text
(config)# no do-exec show ip ospf neighbor <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 71 `；EOL ` RVA 0x34890EC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e3d10944cffa4e82](../../evidence/conditions-sets-088.md#c-e3d10944cffa4e82) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-049145

```text
(config)# no do-exec show ip ospf nsf <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 14 `；EOL ` RVA 0x34877900 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d236fddacacd7923](../../evidence/conditions-sets-081.md#c-d236fddacacd7923) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-049732

```text
(config)# no do-exec show ip ospf nsr <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 20 `；EOL ` RVA 0x33FC8EF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d236fddacacd7923](../../evidence/conditions-sets-081.md#c-d236fddacacd7923) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055581

```text
(config)# no do-exec show ip ospf nsr objects <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 21 `；EOL ` RVA 0x33FC8C20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d236fddacacd7923](../../evidence/conditions-sets-081.md#c-d236fddacacd7923) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055604

```text
(config)# no do-exec show ip ospf nsr statistics <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 22 `；EOL ` RVA 0x33FC8EC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d236fddacacd7923](../../evidence/conditions-sets-081.md#c-d236fddacacd7923) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-049987

```text
(config)# no do-exec show ip ospf request-list <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 73 `；EOL ` RVA 0x34891878 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-116bd051b88ca966](../../evidence/conditions-sets-007.md#c-116bd051b88ca966) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-049962

```text
(config)# no do-exec show ip ospf retransmission-list <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 72 `；EOL ` RVA 0x34891490 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7a1c7bd5caef7f01](../../evidence/conditions-sets-047.md#c-7a1c7bd5caef7f01) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-049615

```text
(config)# no do-exec show ip ospf rib <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 19 `；EOL ` RVA 0x34879088 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-9a2d99c305604a87](../../evidence/conditions-sets-060.md#c-9a2d99c305604a87) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-049616

```text
(config)# no do-exec show ip ospf rib <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 18 `；EOL ` RVA 0x34879308 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-2ea467d44a1139b0](../../evidence/conditions-sets-018.md#c-2ea467d44a1139b0) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-048985

```text
(config)# no do-exec show ip ospf sham-links <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 6 `；EOL ` RVA 0x34877308 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-049519

```text
(config)# no do-exec show ip ospf statistics <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 11 `；EOL ` RVA 0x34879890 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d236fddacacd7923](../../evidence/conditions-sets-081.md#c-d236fddacacd7923) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-049313

```text
(config)# no do-exec show ip ospf summary-address <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 8 `；EOL ` RVA 0x34878228 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d236fddacacd7923](../../evidence/conditions-sets-081.md#c-d236fddacacd7923) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055292

```text
(config)# no do-exec show ip ospf timers lsa-group <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 12 `；EOL ` RVA 0x34877C08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d236fddacacd7923](../../evidence/conditions-sets-081.md#c-d236fddacacd7923) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055336

```text
(config)# no do-exec show ip ospf timers rate-limit <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 13 `；EOL ` RVA 0x34877EB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d236fddacacd7923](../../evidence/conditions-sets-081.md#c-d236fddacacd7923) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-049604

```text
(config)# no do-exec show ip ospf topology-info <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 15 `；EOL ` RVA 0x3487A778 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d236fddacacd7923](../../evidence/conditions-sets-081.md#c-d236fddacacd7923) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-049897

```text
(config)# no do-exec show ip ospf traffic <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 67 `；EOL ` RVA 0x34890680 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-174a88fc5073a64c](../../evidence/conditions-sets-009.md#c-174a88fc5073a64c) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-049066

```text
(config)# no do-exec show ip ospf virtual-links <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 5 `；EOL ` RVA 0x34876DC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-048715

```text
(config)# no do-exec show ip pim autorp <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 46 `；EOL ` RVA 0x34753198 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f7f172e32cfc78a0](../../evidence/conditions-sets-096.md#c-f7f172e32cfc78a0) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-058460

```text
(config)# no do-exec show ip pim bfd neighbor inactive <cr>
```

Handler ` RVA 0xC4A31B0 `；selector ` 0 `；EOL ` RVA 0x33A9C0F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ddaf11059e672b92](../../evidence/conditions-sets-085.md#c-ddaf11059e672b92) · [状态效果 S-f8568ee04d018476](../../evidence/state_effects-sets-053.md#s-f8568ee04d018476)

### path-048785

```text
(config)# no do-exec show ip pim bsr-router <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 20 `；EOL ` RVA 0x34753440 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f7f172e32cfc78a0](../../evidence/conditions-sets-096.md#c-f7f172e32cfc78a0) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055278

```text
(config)# no do-exec show ip pim drlb gdr-candidates <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 79 `；EOL ` RVA 0x34754128 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-434c17223087681a](../../evidence/conditions-sets-026.md#c-434c17223087681a) · [状态效果 S-cd088fbf30b231c4](../../evidence/state_effects-sets-043.md#s-cd088fbf30b231c4)

### path-049294

```text
(config)# no do-exec show ip pim gir <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 87 `；EOL ` RVA 0x34756200 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c79cdeeb16a0a23a](../../evidence/conditions-sets-077.md#c-c79cdeeb16a0a23a) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-049573

```text
(config)# no do-exec show ip pim interface <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 12 `；EOL ` RVA 0x347558F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-07a68833af1a33e6](../../evidence/conditions-sets-003.md#c-07a68833af1a33e6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055617

```text
(config)# no do-exec show ip pim interface bfd <cr>
```

Handler ` RVA 0xC4A31B0 `；selector ` 1 `；EOL ` RVA 0x33A9C488 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d8f0ef3346d04137](../../evidence/conditions-sets-084.md#c-d8f0ef3346d04137) · [状态效果 S-ab8c719e6bdabb2f](../../evidence/state_effects-sets-036.md#s-ab8c719e6bdabb2f)

### path-055412

```text
(config)# no do-exec show ip pim interface detail <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 39 `；EOL ` RVA 0x34755648 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-07a68833af1a33e6](../../evidence/conditions-sets-003.md#c-07a68833af1a33e6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055376

```text
(config)# no do-exec show ip pim interface traffic <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 96 `；EOL ` RVA 0x347553A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-07a68833af1a33e6](../../evidence/conditions-sets-003.md#c-07a68833af1a33e6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-049797

```text
(config)# no do-exec show ip pim mdt <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 0 `；EOL ` RVA 0x3478DCC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ef425f477cec0d28](../../evidence/conditions-sets-092.md#c-ef425f477cec0d28) · [状态效果 S-867cb47577e5dd8e](../../evidence/state_effects-sets-029.md#s-867cb47577e5dd8e)

### path-055702

```text
(config)# no do-exec show ip pim mdt bgp <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 1 `；EOL ` RVA 0x3478BB78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ef425f477cec0d28](../../evidence/conditions-sets-092.md#c-ef425f477cec0d28) · [状态效果 S-867cb47577e5dd8e](../../evidence/state_effects-sets-029.md#s-867cb47577e5dd8e)

### path-058503

```text
(config)# no do-exec show ip pim mdt bgp c-mroutes <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 6 `；EOL ` RVA 0x3478B838 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-cf077db1e2ed5988](../../evidence/conditions-sets-080.md#c-cf077db1e2ed5988) · [状态效果 S-2a3fb4729d1d5b99](../../evidence/state_effects-sets-009.md#s-2a3fb4729d1d5b99)

### path-059506

```text
(config)# no do-exec show ip pim mdt history interval <number:1..71582> <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 2 `；EOL ` RVA 0x3478B440 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` in minutes, maximum is 71582 minutes (7 weeks)。

[条件 C-ef425f477cec0d28](../../evidence/conditions-sets-092.md#c-ef425f477cec0d28) · [参数 P-e84d14ee7ea2ba12](../../evidence/parameters-sets-017.md#p-e84d14ee7ea2ba12) · [状态效果 S-867cb47577e5dd8e](../../evidence/state_effects-sets-029.md#s-867cb47577e5dd8e)

### path-058512

```text
(config)# no do-exec show ip pim mdt internal bier <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 10 `；EOL ` RVA 0x3478C440 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-6db24216c4fdc7ec](../../evidence/conditions-sets-042.md#c-6db24216c4fdc7ec) · [状态效果 S-867cb47577e5dd8e](../../evidence/state_effects-sets-029.md#s-867cb47577e5dd8e)

### path-058537

```text
(config)# no do-exec show ip pim mdt internal crt <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 11 `；EOL ` RVA 0x3478CEE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7bbaed72ce0a43ad](../../evidence/conditions-sets-048.md#c-7bbaed72ce0a43ad) · [状态效果 S-867cb47577e5dd8e](../../evidence/state_effects-sets-029.md#s-867cb47577e5dd8e)

### path-058500

```text
(config)# no do-exec show ip pim mdt internal gre <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 7 `；EOL ` RVA 0x3478C198 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f2b4ac5100bf9f7f](../../evidence/conditions-sets-094.md#c-f2b4ac5100bf9f7f) · [状态效果 S-867cb47577e5dd8e](../../evidence/state_effects-sets-029.md#s-867cb47577e5dd8e)

### path-058519

```text
(config)# no do-exec show ip pim mdt internal ir <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 9 `；EOL ` RVA 0x3478C6E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c16359b8e05cadd8](../../evidence/conditions-sets-075.md#c-c16359b8e05cadd8) · [状态效果 S-867cb47577e5dd8e](../../evidence/state_effects-sets-029.md#s-867cb47577e5dd8e)

### path-058524

```text
(config)# no do-exec show ip pim mdt internal leaf-ad <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 15 `；EOL ` RVA 0x3478C990 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f5c211cb049c339b](../../evidence/conditions-sets-095.md#c-f5c211cb049c339b) · [状态效果 S-867cb47577e5dd8e](../../evidence/state_effects-sets-029.md#s-867cb47577e5dd8e)

### path-058530

```text
(config)# no do-exec show ip pim mdt internal mldp <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 8 `；EOL ` RVA 0x3478CC38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ddc67b17a015de2e](../../evidence/conditions-sets-085.md#c-ddc67b17a015de2e) · [状态效果 S-867cb47577e5dd8e](../../evidence/state_effects-sets-029.md#s-867cb47577e5dd8e)

### path-058568

```text
(config)# no do-exec show ip pim mdt internal pe <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 12 `；EOL ` RVA 0x3478D498 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-76cae2930b2d3c49](../../evidence/conditions-sets-046.md#c-76cae2930b2d3c49) · [状态效果 S-867cb47577e5dd8e](../../evidence/state_effects-sets-029.md#s-867cb47577e5dd8e)

### path-059523

```text
(config)# no do-exec show ip pim mdt internal pe all <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 14 `；EOL ` RVA 0x3478D740 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-96f6f37effc35394](../../evidence/conditions-sets-058.md#c-96f6f37effc35394) · [状态效果 S-867cb47577e5dd8e](../../evidence/state_effects-sets-029.md#s-867cb47577e5dd8e)

### path-058547

```text
(config)# no do-exec show ip pim mdt internal replication <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 16 `；EOL ` RVA 0x3478D188 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-742fb4ffa38ff317](../../evidence/conditions-sets-045.md#c-742fb4ffa38ff317) · [状态效果 S-867cb47577e5dd8e](../../evidence/state_effects-sets-029.md#s-867cb47577e5dd8e)

### path-058566

```text
(config)# no do-exec show ip pim mdt internal tdb <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 13 `；EOL ` RVA 0x3478D9D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-16dedd191bd5cbdd](../../evidence/conditions-sets-009.md#c-16dedd191bd5cbdd) · [状态效果 S-867cb47577e5dd8e](../../evidence/state_effects-sets-029.md#s-867cb47577e5dd8e)

### path-058489

```text
(config)# no do-exec show ip pim mdt internal vxlan <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 24 `；EOL ` RVA 0x3478BEF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-acd2dbb27d204214](../../evidence/conditions-sets-067.md#c-acd2dbb27d204214) · [状态效果 S-867cb47577e5dd8e](../../evidence/state_effects-sets-029.md#s-867cb47577e5dd8e)

### path-055593

```text
(config)# no do-exec show ip pim mdt receive <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 3 `；EOL ` RVA 0x3478AEC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ef425f477cec0d28](../../evidence/conditions-sets-092.md#c-ef425f477cec0d28) · [状态效果 S-867cb47577e5dd8e](../../evidence/state_effects-sets-029.md#s-867cb47577e5dd8e)

### path-058468

```text
(config)# no do-exec show ip pim mdt receive detail <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 4 `；EOL ` RVA 0x3478AEA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ef425f477cec0d28](../../evidence/conditions-sets-092.md#c-ef425f477cec0d28) · [状态效果 S-867cb47577e5dd8e](../../evidence/state_effects-sets-029.md#s-867cb47577e5dd8e)

### path-055545

```text
(config)# no do-exec show ip pim mdt send <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 5 `；EOL ` RVA 0x3478AB90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ef425f477cec0d28](../../evidence/conditions-sets-092.md#c-ef425f477cec0d28) · [状态效果 S-867cb47577e5dd8e](../../evidence/state_effects-sets-029.md#s-867cb47577e5dd8e)

### path-049256

```text
(config)# no do-exec show ip pim mvpn <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 52 `；EOL ` RVA 0x34752B10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f7f172e32cfc78a0](../../evidence/conditions-sets-096.md#c-f7f172e32cfc78a0) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055307

```text
(config)# no do-exec show ip pim mvpn bier <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 89 `；EOL ` RVA 0x34752840 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f7f172e32cfc78a0](../../evidence/conditions-sets-096.md#c-f7f172e32cfc78a0) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055080

```text
(config)# no do-exec show ip pim mvpn crt <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 70 `；EOL ` RVA 0x34751850 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f7f172e32cfc78a0](../../evidence/conditions-sets-096.md#c-f7f172e32cfc78a0) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055274

```text
(config)# no do-exec show ip pim mvpn gre <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 90 `；EOL ` RVA 0x34752598 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f7f172e32cfc78a0](../../evidence/conditions-sets-096.md#c-f7f172e32cfc78a0) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055237

```text
(config)# no do-exec show ip pim mvpn ir <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 91 `；EOL ` RVA 0x347522F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f7f172e32cfc78a0](../../evidence/conditions-sets-096.md#c-f7f172e32cfc78a0) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055159

```text
(config)# no do-exec show ip pim mvpn leaf-ad <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 92 `；EOL ` RVA 0x34751DA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f7f172e32cfc78a0](../../evidence/conditions-sets-096.md#c-f7f172e32cfc78a0) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055001

```text
(config)# no do-exec show ip pim mvpn mldp <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 68 `；EOL ` RVA 0x34751300 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f7f172e32cfc78a0](../../evidence/conditions-sets-096.md#c-f7f172e32cfc78a0) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055040

```text
(config)# no do-exec show ip pim mvpn pe <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 69 `；EOL ` RVA 0x347515A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f7f172e32cfc78a0](../../evidence/conditions-sets-096.md#c-f7f172e32cfc78a0) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055118

```text
(config)# no do-exec show ip pim mvpn replication <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 93 `；EOL ` RVA 0x34751AF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f7f172e32cfc78a0](../../evidence/conditions-sets-096.md#c-f7f172e32cfc78a0) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055203

```text
(config)# no do-exec show ip pim mvpn srv6 <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 97 `；EOL ` RVA 0x34752048 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f7f172e32cfc78a0](../../evidence/conditions-sets-096.md#c-f7f172e32cfc78a0) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055345

```text
(config)# no do-exec show ip pim mvpn tdb <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 94 `；EOL ` RVA 0x34752AE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f7f172e32cfc78a0](../../evidence/conditions-sets-096.md#c-f7f172e32cfc78a0) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-054959

```text
(config)# no do-exec show ip pim mvpn vxlan <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 95 `；EOL ` RVA 0x34751058 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f7f172e32cfc78a0](../../evidence/conditions-sets-096.md#c-f7f172e32cfc78a0) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-048886

```text
(config)# no do-exec show ip pim neighbor <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 10 `；EOL ` RVA 0x347710F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-51b0d38796dd21f0](../../evidence/conditions-sets-032.md#c-51b0d38796dd21f0) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055144

```text
(config)# no do-exec show ip pim pfp-sa announcements <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 83 `；EOL ` RVA 0x34753790 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a757d600e7b7aab8](../../evidence/conditions-sets-065.md#c-a757d600e7b7aab8) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055234

```text
(config)# no do-exec show ip pim pfp-sa cache <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 86 `；EOL ` RVA 0x34753CE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a757d600e7b7aab8](../../evidence/conditions-sets-065.md#c-a757d600e7b7aab8) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055194

```text
(config)# no do-exec show ip pim pfp-sa originator <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 84 `；EOL ` RVA 0x34753A38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a757d600e7b7aab8](../../evidence/conditions-sets-065.md#c-a757d600e7b7aab8) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-049253

```text
(config)# no do-exec show ip pim rp <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 11 `；EOL ` RVA 0x34754BB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-fa560e3937bdf339](../../evidence/conditions-sets-097.md#c-fa560e3937bdf339) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055260

```text
(config)# no do-exec show ip pim rp-hash <address> <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 22 `；EOL ` RVA 0x34754FF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` group address。

[条件 C-6dbd6590a9eb7383](../../evidence/conditions-sets-042.md#c-6dbd6590a9eb7383) · [参数 P-c66d3e1e0ed7b695](../../evidence/parameters-sets-015.md#p-c66d3e1e0ed7b695) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-049250

```text
(config)# no do-exec show ip pim tunnel <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 55 `；EOL ` RVA 0x347547A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-9bb185ecd494e32d](../../evidence/conditions-sets-060.md#c-9bb185ecd494e32d) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-040104

```text
(config)# no do-exec show ip policy <cr>
```

Handler ` RVA 0xFAD9620 `；selector ` 0 `；EOL ` RVA 0x34804A80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-049079

```text
(config)# no do-exec show ip policy adj-subblock <cr>
```

Handler ` RVA 0xFAD9440 `；selector ` 0 `；EOL ` RVA 0x34804A58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-039185

```text
(config)# no do-exec show ip policy-list <cr>
```

Handler ` RVA 0xE218540 `；selector ` 0 `；EOL ` RVA 0x344BABE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-059411

```text
(config)# no do-exec show ip portbundle ip <address> bundle <number:1..65535> <cr>
```

Handler ` RVA 0x11C31540 `；selector ` 0 `；EOL ` RVA 0x356A5148 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` Portbundle IP address；` unsigned_number ` Portbundle bundle number。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-81af61e5ba4224a6](../../evidence/parameters-sets-010.md#p-81af61e5ba4224a6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-047936

```text
(config)# no do-exec show ip portbundle status <cr>
```

Handler ` RVA 0x11C31540 `；selector ` 1 `；EOL ` RVA 0x356A4DE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-054592

```text
(config)# no do-exec show ip portbundle status free <cr>
```

Handler ` RVA 0x11C31540 `；selector ` 2 `；EOL ` RVA 0x356A4B28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-15007c2213680282](../../evidence/state_effects-sets-005.md#s-15007c2213680282)

### path-048049

```text
(config)# no do-exec show ip ports all <cr>
```

Handler ` RVA 0xCE51730 `；selector ` 0 `；EOL ` RVA 0x33CF6FA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-048000

```text
(config)# no do-exec show ip ports ephemeral-max <cr>
```

Handler ` RVA 0xCDEFA80 `；selector ` 0 `；EOL ` RVA 0x33CF6D00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-048095

```text
(config)# no do-exec show ip ports reservation <cr>
```

Handler ` RVA 0xCE518D0 `；selector ` 0 `；EOL ` RVA 0x33CF7250 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c6a825157ac462ea](../../evidence/conditions-sets-077.md#c-c6a825157ac462ea) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-040604

```text
(config)# no do-exec show ip prefix-list <cr>
```

Handler ` RVA 0xE2203B0 `；selector ` 0 `；EOL ` RVA 0x342832B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ddcaf979b496d8fc](../../evidence/conditions-sets-085.md#c-ddcaf979b496d8fc) · [状态效果 S-a96ff7b5ceb23990](../../evidence/state_effects-sets-036.md#s-a96ff7b5ceb23990)

### path-058498

```text
(config)# no do-exec show ip prefix-list <string> seq <number:1..4294967295> <cr>
```

Handler ` RVA 0xE2203B0 `；selector ` 3 `；EOL ` RVA 0x34283358 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Name of a prefix list；` unsigned_number ` Sequence number。

[条件 C-ddcaf979b496d8fc](../../evidence/conditions-sets-085.md#c-ddcaf979b496d8fc) · [参数 P-0d71bd8044f6fc2b](../../evidence/parameters-sets-001.md#p-0d71bd8044f6fc2b) · [状态效果 S-a96ff7b5ceb23990](../../evidence/state_effects-sets-036.md#s-a96ff7b5ceb23990)

### path-049723

```text
(config)# no do-exec show ip prefix-list detail <cr>
```

Handler ` RVA 0xE2203B0 `；selector ` 2 `；EOL ` RVA 0x34282FB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-a96ff7b5ceb23990](../../evidence/state_effects-sets-036.md#s-a96ff7b5ceb23990)

### path-049679

```text
(config)# no do-exec show ip prefix-list summary <cr>
```

Handler ` RVA 0xE2203B0 `；selector ` 1 `；EOL ` RVA 0x34282CA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-a96ff7b5ceb23990](../../evidence/state_effects-sets-036.md#s-a96ff7b5ceb23990)

### path-039243

```text
(config)# no do-exec show ip protocols <cr>
```

Handler ` RVA 0xE1F60E0 `；selector ` 0 `；EOL ` RVA 0x3422FAB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-662dab67c3ad9644](../../evidence/conditions-sets-039.md#c-662dab67c3ad9644) · [状态效果 S-4b26cd4c715b4a50](../../evidence/state_effects-sets-016.md#s-4b26cd4c715b4a50)

### path-048182

```text
(config)# no do-exec show ip protocols summary <cr>
```

Handler ` RVA 0xE1F5DF0 `；selector ` 0 `；EOL ` RVA 0x3422FA88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-662dab67c3ad9644](../../evidence/conditions-sets-039.md#c-662dab67c3ad9644) · [状态效果 S-4b26cd4c715b4a50](../../evidence/state_effects-sets-016.md#s-4b26cd4c715b4a50)

### path-038069

```text
(config)# no do-exec show ip redirects <cr>
```

Handler ` RVA 0xCF509C0 `；selector ` 0 `；EOL ` RVA 0x33D31570 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-048239

```text
(config)# no do-exec show ip rib database <cr>
```

Handler ` RVA 0xDC0B310 `；selector ` 1 `；EOL ` RVA 0x3422F578 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-aa3e36e3194bcd23](../../evidence/conditions-sets-066.md#c-aa3e36e3194bcd23) · [状态效果 S-51bb7f5900e7398f](../../evidence/state_effects-sets-018.md#s-51bb7f5900e7398f)

### path-049310

```text
(config)# no do-exec show ip rip database <cr>
```

Handler ` RVA 0xFB73AB0 `；selector ` 0 `；EOL ` RVA 0x34822820 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7c00b49cbd29f681](../../evidence/conditions-sets-048.md#c-7c00b49cbd29f681) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-049279

```text
(config)# no do-exec show ip rip neighbors <cr>
```

Handler ` RVA 0xFB52AC0 `；selector ` 0 `；EOL ` RVA 0x34822B40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-662365bd75b0a5eb](../../evidence/conditions-sets-039.md#c-662365bd75b0a5eb) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-049118

```text
(config)# no do-exec show ip rip timers <cr>
```

Handler ` RVA 0xFB56CB0 `；selector ` 0 `；EOL ` RVA 0x34822428 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-054798

```text
(config)# no do-exec show ip route list <number:1..199> <cr>
```

Handler ` RVA 0xE1CEA80 `；selector ` 12 `；EOL ` RVA 0x34230C38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` IP access list number。

[条件 C-ccae3c6fa6a19008](../../evidence/conditions-sets-079.md#c-ccae3c6fa6a19008) · [参数 P-6f46a0106e78d96b](../../evidence/parameters-sets-009.md#p-6f46a0106e78d96b) · [状态效果 S-792540d3b71cdeba](../../evidence/state_effects-sets-026.md#s-792540d3b71cdeba)

### path-054856

```text
(config)# no do-exec show ip route omp-tag <number:0..4294967295> <cr>
```

Handler ` RVA 0xE1CEA80 `；selector ` 15 `；EOL ` RVA 0x34231420 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Overlay Management Protocol (OMP) Tag value。

[条件 C-bfe07068749ae3df](../../evidence/conditions-sets-074.md#c-bfe07068749ae3df) · [参数 P-1586b2be9da07e52](../../evidence/parameters-sets-002.md#p-1586b2be9da07e52) · [状态效果 S-792540d3b71cdeba](../../evidence/state_effects-sets-026.md#s-792540d3b71cdeba)

### path-054855

```text
(config)# no do-exec show ip route tag <number:0..4294967295> <cr>
```

Handler ` RVA 0xE1CEA80 `；selector ` 14 `；EOL ` RVA 0x34231000 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Tag value。

[条件 C-247403f934361232](../../evidence/conditions-sets-014.md#c-247403f934361232) · [参数 P-e0210763947c7838](../../evidence/parameters-sets-017.md#p-e0210763947c7838) · [状态效果 S-792540d3b71cdeba](../../evidence/state_effects-sets-026.md#s-792540d3b71cdeba)

### path-058176

```text
(config)# no do-exec show ip route tree <address> <address> <cr>
```

Handler ` RVA 0xE1CEA80 `；selector ` 3 `；EOL ` RVA 0x34230700 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` Network to display information about；` address ` Network mask。

[条件 C-ccae3c6fa6a19008](../../evidence/conditions-sets-079.md#c-ccae3c6fa6a19008) · [参数 P-3c5f288fee4ae5f4](../../evidence/parameters-sets-005.md#p-3c5f288fee4ae5f4) · [状态效果 S-792540d3b71cdeba](../../evidence/state_effects-sets-026.md#s-792540d3b71cdeba)

### path-048366

```text
(config)# no do-exec show ip route tree <cr>
```

Handler ` RVA 0xE1CEA80 `；selector ` 1 `；EOL ` RVA 0x342306C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ccae3c6fa6a19008](../../evidence/conditions-sets-079.md#c-ccae3c6fa6a19008) · [状态效果 S-792540d3b71cdeba](../../evidence/state_effects-sets-026.md#s-792540d3b71cdeba)

### path-054769

```text
(config)# no do-exec show ip route tree summary <cr>
```

Handler ` RVA 0xE1CEA80 `；selector ` 2 `；EOL ` RVA 0x342303F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ccae3c6fa6a19008](../../evidence/conditions-sets-079.md#c-ccae3c6fa6a19008) · [状态效果 S-792540d3b71cdeba](../../evidence/state_effects-sets-026.md#s-792540d3b71cdeba)

### path-048507

```text
(config)# no do-exec show ip rpf queued <cr>
```

Handler ` RVA 0xF740240 `；selector ` 0 `；EOL ` RVA 0x34750190 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f7f172e32cfc78a0](../../evidence/conditions-sets-096.md#c-f7f172e32cfc78a0) · [状态效果 S-ad947acc808c6abd](../../evidence/state_effects-sets-037.md#s-ad947acc808c6abd)

### path-040938

```text
(config)# no do-exec show ip rsvp <cr>
```

Handler ` RVA 0x10073190 `；selector ` 0 `；EOL ` RVA 0x34A3A428 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5e6a7f2c6539d6b3](../../evidence/conditions-sets-037.md#c-5e6a7f2c6539d6b3) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055552

```text
(config)# no do-exec show ip rsvp aggregation ip <cr>
```

Handler ` RVA 0x101C49F0 `；selector ` 0 `；EOL ` RVA 0x34A69C90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-058495

```text
(config)# no do-exec show ip rsvp aggregation ip endpoints <cr>
```

Handler ` RVA 0x101C42E0 `；selector ` 0 `；EOL ` RVA 0x34A69F58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-058472

```text
(config)# no do-exec show ip rsvp aggregation ip interface <cr>
```

Handler ` RVA 0x101C4050 `；selector ` 0 `；EOL ` RVA 0x34A69970 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-77f9e62a2b300c22](../../evidence/conditions-sets-047.md#c-77f9e62a2b300c22) · [状态效果 S-4afe8f6076869bda](../../evidence/state_effects-sets-016.md#s-4afe8f6076869bda)

### path-058441

```text
(config)# no do-exec show ip rsvp aggregation ip map <cr>
```

Handler ` RVA 0x101C3C20 `；selector ` 0 `；EOL ` RVA 0x34A691B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-058451

```text
(config)# no do-exec show ip rsvp aggregation ip reservation <cr>
```

Handler ` RVA 0x101C3DE0 `；selector ` 0 `；EOL ` RVA 0x34A694F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-049961

```text
(config)# no do-exec show ip rsvp atm-peak-rate-limit <cr>
```

Handler ` RVA 0x100542A0 `；selector ` 0 `；EOL ` RVA 0x34A34388 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b6c5c4cc381f4a1f](../../evidence/conditions-sets-071.md#c-b6c5c4cc381f4a1f) · [状态效果 S-cdf23be1fbc19574](../../evidence/state_effects-sets-044.md#s-cdf23be1fbc19574)

### path-049518

```text
(config)# no do-exec show ip rsvp authentication <cr>
```

Handler ` RVA 0x10073FB0 `；selector ` 0 `；EOL ` RVA 0x34A2FFA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7fe18cb68439d029](../../evidence/conditions-sets-050.md#c-7fe18cb68439d029) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-050088

```text
(config)# no do-exec show ip rsvp counters <cr>
```

Handler ` RVA 0x100B61F0 `；selector ` 0 `；EOL ` RVA 0x34A35FE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4759a80b867df040](../../evidence/conditions-sets-028.md#c-4759a80b867df040) · [状态效果 S-d8ad36b3747728a7](../../evidence/state_effects-sets-046.md#s-d8ad36b3747728a7)

### path-049893

```text
(config)# no do-exec show ip rsvp handles <cr>
```

Handler ` RVA 0x10070450 `；selector ` 0 `；EOL ` RVA 0x34A34000 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f6ac0974c487853d](../../evidence/conditions-sets-095.md#c-f6ac0974c487853d) · [状态效果 S-871335ae6fbc4d0b](../../evidence/state_effects-sets-029.md#s-871335ae6fbc4d0b)

### path-050148

```text
(config)# no do-exec show ip rsvp hello <cr>
```

Handler ` RVA 0x10072260 `；selector ` 0 `；EOL ` RVA 0x34A38728 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-73e1ff93bbad3fdc](../../evidence/conditions-sets-045.md#c-73e1ff93bbad3fdc) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-058649

```text
(config)# no do-exec show ip rsvp hello bfd nbr <cr>
```

Handler ` RVA 0x10076740 `；selector ` 0 `；EOL ` RVA 0x34A37650 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ec7faa639c22b742](../../evidence/conditions-sets-091.md#c-ec7faa639c22b742) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-059550

```text
(config)# no do-exec show ip rsvp hello bfd nbr detail <cr>
```

Handler ` RVA 0x10076940 `；selector ` 0 `；EOL ` RVA 0x34A37348 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ec7faa639c22b742](../../evidence/conditions-sets-091.md#c-ec7faa639c22b742) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-059555

```text
(config)# no do-exec show ip rsvp hello client lsp detail <cr>
```

Handler ` RVA 0x10076EA0 `；selector ` 0 `；EOL ` RVA 0x34A38108 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-2cf0f65375dcb14e](../../evidence/conditions-sets-018.md#c-2cf0f65375dcb14e) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-059553

```text
(config)# no do-exec show ip rsvp hello client lsp summary <cr>
```

Handler ` RVA 0x10076D20 `；selector ` 0 `；EOL ` RVA 0x34A38410 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-2cf0f65375dcb14e](../../evidence/conditions-sets-018.md#c-2cf0f65375dcb14e) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-058656

```text
(config)# no do-exec show ip rsvp hello client nbr <cr>
```

Handler ` RVA 0x10076A40 `；selector ` 0 `；EOL ` RVA 0x34A37DA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-2cf0f65375dcb14e](../../evidence/conditions-sets-018.md#c-2cf0f65375dcb14e) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-059552

```text
(config)# no do-exec show ip rsvp hello client nbr detail <cr>
```

Handler ` RVA 0x10076C10 `；selector ` 0 `；EOL ` RVA 0x34A37A98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-2cf0f65375dcb14e](../../evidence/conditions-sets-018.md#c-2cf0f65375dcb14e) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055915

```text
(config)# no do-exec show ip rsvp hello graceful-restart <cr>
```

Handler ` RVA 0x10073050 `；selector ` 0 `；EOL ` RVA 0x34A38700 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-9e789b95db429da7](../../evidence/conditions-sets-061.md#c-9e789b95db429da7) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-058617

```text
(config)# no do-exec show ip rsvp hello instance internal <cr>
```

Handler ` RVA 0x10076620 `；selector ` 0 `；EOL ` RVA 0x34A368E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-2eb6da402bd619e6](../../evidence/conditions-sets-018.md#c-2eb6da402bd619e6) · [状态效果 S-9419a0fb031e4827](../../evidence/state_effects-sets-031.md#s-9419a0fb031e4827)

### path-058628

```text
(config)# no do-exec show ip rsvp hello instance summary <cr>
```

Handler ` RVA 0x10076290 `；selector ` 0 `；EOL ` RVA 0x34A36C40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-2eb6da402bd619e6](../../evidence/conditions-sets-018.md#c-2eb6da402bd619e6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055851

```text
(config)# no do-exec show ip rsvp hello statistics <cr>
```

Handler ` RVA 0x100761D0 `；selector ` 0 `；EOL ` RVA 0x34A36F28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7dad2cd3040acf55](../../evidence/conditions-sets-049.md#c-7dad2cd3040acf55) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055861

```text
(config)# no do-exec show ip rsvp host receivers <cr>
```

Handler ` RVA 0x1006D010 `；selector ` 0 `；EOL ` RVA 0x34A35B98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4759a80b867df040](../../evidence/conditions-sets-028.md#c-4759a80b867df040) · [状态效果 S-608912645d5201f7](../../evidence/state_effects-sets-021.md#s-608912645d5201f7)

### path-055840

```text
(config)# no do-exec show ip rsvp host senders <cr>
```

Handler ` RVA 0x1006D750 `；selector ` 0 `；EOL ` RVA 0x34A358A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4759a80b867df040](../../evidence/conditions-sets-028.md#c-4759a80b867df040) · [状态效果 S-2a0f05b8a2c8bb00](../../evidence/state_effects-sets-009.md#s-2a0f05b8a2c8bb00)

### path-049942

```text
(config)# no do-exec show ip rsvp installed <cr>
```

Handler ` RVA 0x1006B120 `；selector ` 0 `；EOL ` RVA 0x34A33858 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-be548ffe4fb04560](../../evidence/conditions-sets-073.md#c-be548ffe4fb04560) · [状态效果 S-263fed39f7bfdcb7](../../evidence/state_effects-sets-009.md#s-263fed39f7bfdcb7)

### path-049898

```text
(config)# no do-exec show ip rsvp interface <cr>
```

Handler ` RVA 0x1006B3E0 `；selector ` 0 `；EOL ` RVA 0x34A33020 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7276fe3cb0565025](../../evidence/conditions-sets-044.md#c-7276fe3cb0565025) · [状态效果 S-ac87d9c88d2f8af0](../../evidence/state_effects-sets-036.md#s-ac87d9c88d2f8af0)

### path-055862

```text
(config)# no do-exec show ip rsvp listeners <address> <cr>
```

Handler ` RVA 0x1006F480 `；selector ` 6 `；EOL ` RVA 0x34A35008 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` Destination address。

[条件 C-4759a80b867df040](../../evidence/conditions-sets-028.md#c-4759a80b867df040) · [参数 P-559a5e35800d3230](../../evidence/parameters-sets-007.md#p-559a5e35800d3230) · [状态效果 S-b52e1f03fc920a78](../../evidence/state_effects-sets-038.md#s-b52e1f03fc920a78)

### path-058604

```text
(config)# no do-exec show ip rsvp listeners <address> <number:0..255> <cr>
```

Handler ` RVA 0x1006F480 `；selector ` 4 `；EOL ` RVA 0x34A34CC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` Destination address；` unsigned_number ` IP Protocol。

[条件 C-4759a80b867df040](../../evidence/conditions-sets-028.md#c-4759a80b867df040) · [参数 P-c1d702e7762de23b](../../evidence/parameters-sets-015.md#p-c1d702e7762de23b) · [状态效果 S-b52e1f03fc920a78](../../evidence/state_effects-sets-038.md#s-b52e1f03fc920a78)

### path-059524

```text
(config)# no do-exec show ip rsvp listeners <address> <number:0..255> <number:0..65535> <cr>
```

Handler ` RVA 0x1006F480 `；selector ` 0 `；EOL ` RVA 0x34A34A18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` Destination address；` unsigned_number ` IP Protocol；` unsigned_number ` Destination port。

[条件 C-4759a80b867df040](../../evidence/conditions-sets-028.md#c-4759a80b867df040) · [参数 P-eeed49378aa0252c](../../evidence/parameters-sets-018.md#p-eeed49378aa0252c) · [状态效果 S-b52e1f03fc920a78](../../evidence/state_effects-sets-038.md#s-b52e1f03fc920a78)

### path-050014

```text
(config)# no do-exec show ip rsvp listeners <cr>
```

Handler ` RVA 0x1006F480 `；selector ` 7 `；EOL ` RVA 0x34A352C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4759a80b867df040](../../evidence/conditions-sets-028.md#c-4759a80b867df040) · [状态效果 S-b52e1f03fc920a78](../../evidence/state_effects-sets-038.md#s-b52e1f03fc920a78)

### path-049766

```text
(config)# no do-exec show ip rsvp metadata <cr>
```

Handler ` RVA 0x10069BC0 `；selector ` 0 `；EOL ` RVA 0x34A32250 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7fe18cb68439d029](../../evidence/conditions-sets-050.md#c-7fe18cb68439d029) · [状态效果 S-ad6043e9ecf20663](../../evidence/state_effects-sets-037.md#s-ad6043e9ecf20663)

### path-049694

```text
(config)# no do-exec show ip rsvp neighbor <cr>
```

Handler ` RVA 0x1006DCE0 `；selector ` 0 `；EOL ` RVA 0x34A309B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7fe18cb68439d029](../../evidence/conditions-sets-050.md#c-7fe18cb68439d029) · [状态效果 S-d6c99475a14b614c](../../evidence/state_effects-sets-046.md#s-d6c99475a14b614c)

### path-055589

```text
(config)# no do-exec show ip rsvp neighbor queues <cr>
```

Handler ` RVA 0x1006DB00 `；selector ` 0 `；EOL ` RVA 0x34A30C70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c1ac38b85e1fb7bb](../../evidence/conditions-sets-075.md#c-c1ac38b85e1fb7bb) · [状态效果 S-d6c99475a14b614c](../../evidence/state_effects-sets-046.md#s-d6c99475a14b614c)

### path-055430

```text
(config)# no do-exec show ip rsvp nsr counters <cr>
```

Handler ` RVA 0x100723C0 `；selector ` 0 `；EOL ` RVA 0x34A2FBB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-9514e4dc259ba20d](../../evidence/conditions-sets-058.md#c-9514e4dc259ba20d) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055843

```text
(config)# no do-exec show ip rsvp p2mp counters <cr>
```

Handler ` RVA 0x101A72E0 `；selector ` 0 `；EOL ` RVA 0x34A3A468 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-961c18143c16ea2a](../../evidence/conditions-sets-058.md#c-961c18143c16ea2a) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-049479

```text
(config)# no do-exec show ip rsvp policy <cr>
```

Handler ` RVA 0x10113110 `；selector ` 0 `；EOL ` RVA 0x34A40A60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-9c3376d0c22839b3](../../evidence/conditions-sets-060.md#c-9c3376d0c22839b3) · [状态效果 S-8f1fcd70d5c2868a](../../evidence/state_effects-sets-030.md#s-8f1fcd70d5c2868a)

### path-055531

```text
(config)# no do-exec show ip rsvp policy cops <cr>
```

Handler ` RVA 0x10113110 `；selector ` 8 `；EOL ` RVA 0x34A40AA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e3c951b0abf3e01c](../../evidence/conditions-sets-088.md#c-e3c951b0abf3e01c) · [状态效果 S-8f1fcd70d5c2868a](../../evidence/state_effects-sets-030.md#s-8f1fcd70d5c2868a)

### path-055450

```text
(config)# no do-exec show ip rsvp policy identity <cr>
```

Handler ` RVA 0x10112D90 `；selector ` 0 `；EOL ` RVA 0x34A40020 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-8f1fcd70d5c2868a](../../evidence/state_effects-sets-030.md#s-8f1fcd70d5c2868a)

### path-055690

```text
(config)# no do-exec show ip rsvp policy local <cr>
```

Handler ` RVA 0x10113110 `；selector ` 1 `；EOL ` RVA 0x34A40490 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-af443612a5524707](../../evidence/conditions-sets-068.md#c-af443612a5524707) · [状态效果 S-e74fb34f6c0ffd61](../../evidence/state_effects-sets-049.md#s-e74fb34f6c0ffd61)

### path-049896

```text
(config)# no do-exec show ip rsvp precedence <cr>
```

Handler ` RVA 0x10054510 `；selector ` 0 `；EOL ` RVA 0x34A33C50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-554816663dbba392](../../evidence/conditions-sets-033.md#c-554816663dbba392) · [状态效果 S-bf0cc787c2719599](../../evidence/state_effects-sets-040.md#s-bf0cc787c2719599)

### path-049610

```text
(config)# no do-exec show ip rsvp sbm <cr>
```

Handler ` RVA 0x1006E490 `；selector ` 0 `；EOL ` RVA 0x34A303A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e394e7d7feb6c7ab](../../evidence/conditions-sets-088.md#c-e394e7d7feb6c7ab) · [状态效果 S-ef2de74fd967fdea](../../evidence/state_effects-sets-051.md#s-ef2de74fd967fdea)

### path-049769

```text
(config)# no do-exec show ip rsvp sender <cr>
```

Handler ` RVA 0x10069BC0 `；selector ` 0 `；EOL ` RVA 0x34A315A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7fe18cb68439d029](../../evidence/conditions-sets-050.md#c-7fe18cb68439d029) · [状态效果 S-38006ed4aee60aac](../../evidence/state_effects-sets-012.md#s-38006ed4aee60aac)

### path-055959

```text
(config)# no do-exec show ip rsvp signalling blockade <cr>
```

Handler ` RVA 0x10067C20 `；selector ` 0 `；EOL ` RVA 0x34A3A0B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1de7acaebb82474a](../../evidence/conditions-sets-012.md#c-1de7acaebb82474a) · [状态效果 S-0cc83a1d0691c19c](../../evidence/state_effects-sets-003.md#s-0cc83a1d0691c19c)

### path-055836

```text
(config)# no do-exec show ip rsvp signalling fast-local-repair <cr>
```

Handler ` RVA 0x100713E0 `；selector ` 0 `；EOL ` RVA 0x34A38D20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-bbe8e5f206948a04](../../evidence/conditions-sets-073.md#c-bbe8e5f206948a04) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055830

```text
(config)# no do-exec show ip rsvp signalling rate-limit <cr>
```

Handler ` RVA 0x100712D0 `；selector ` 0 `；EOL ` RVA 0x34A38FF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-bbe8e5f206948a04](../../evidence/conditions-sets-073.md#c-bbe8e5f206948a04) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-058635

```text
(config)# no do-exec show ip rsvp signalling refresh interval <cr>
```

Handler ` RVA 0x10071130 `；selector ` 0 `；EOL ` RVA 0x34A39858 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-bbe8e5f206948a04](../../evidence/conditions-sets-073.md#c-bbe8e5f206948a04) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-058645

```text
(config)# no do-exec show ip rsvp signalling refresh misses <cr>
```

Handler ` RVA 0x100711A0 `；selector ` 0 `；EOL ` RVA 0x34A39B00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-bbe8e5f206948a04](../../evidence/conditions-sets-073.md#c-bbe8e5f206948a04) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-058625

```text
(config)# no do-exec show ip rsvp signalling refresh reduction <cr>
```

Handler ` RVA 0x10071210 `；selector ` 0 `；EOL ` RVA 0x34A395B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-bbe8e5f206948a04](../../evidence/conditions-sets-073.md#c-bbe8e5f206948a04) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055852

```text
(config)# no do-exec show ip rsvp signalling session-timers <cr>
```

Handler ` RVA 0x10072130 `；selector ` 0 `；EOL ` RVA 0x34A392A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-bbe8e5f206948a04](../../evidence/conditions-sets-073.md#c-bbe8e5f206948a04) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055565

```text
(config)# no do-exec show ip rsvp transport clients <cr>
```

Handler ` RVA 0x10069BC0 `；selector ` 0 `；EOL ` RVA 0x34A31E80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7fe18cb68439d029](../../evidence/conditions-sets-050.md#c-7fe18cb68439d029) · [状态效果 S-4cd21c588b7dab96](../../evidence/state_effects-sets-017.md#s-4cd21c588b7dab96)

### path-047731

```text
(config)# no do-exec show ip rtp header-compression <cr>
```

Handler ` RVA 0xD194110 `；selector ` 0 `；EOL ` RVA 0x33DAABA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-6a83c6ecb85845ec](../../evidence/conditions-sets-041.md#c-6a83c6ecb85845ec) · [状态效果 S-d61c362e48151790](../../evidence/state_effects-sets-045.md#s-d61c362e48151790)

### path-055043

```text
(config)# no do-exec show ip sctp association list <cr>
```

Handler ` RVA 0xCE6FC00 `；selector ` 2 `；EOL ` RVA 0x33D0DFE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-058256

```text
(config)# no do-exec show ip sctp association parameters <number:0..4294967295> <cr>
```

Handler ` RVA 0xCE6FC00 `；selector ` 3 `；EOL ` RVA 0x33D0DD58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Association ID。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-d2fce9ec1de3fa16](../../evidence/parameters-sets-016.md#p-d2fce9ec1de3fa16) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-058239

```text
(config)# no do-exec show ip sctp association statistics <number:0..4294967295> <cr>
```

Handler ` RVA 0xCE6FC00 `；selector ` 4 `；EOL ` RVA 0x33D0DA68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Association ID。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-39686869c9f42ad0](../../evidence/parameters-sets-005.md#p-39686869c9f42ad0) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-048542

```text
(config)# no do-exec show ip sctp errors <cr>
```

Handler ` RVA 0xCE6FC00 `；selector ` 6 `；EOL ` RVA 0x33D0D6F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-048659

```text
(config)# no do-exec show ip sctp instances <cr>
```

Handler ` RVA 0xCE6FC00 `；selector ` 1 `；EOL ` RVA 0x33D0E288 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-048480

```text
(config)# no do-exec show ip sctp statistics <cr>
```

Handler ` RVA 0xCE6FC00 `；selector ` 5 `；EOL ` RVA 0x33D0D448 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-039492

```text
(config)# no do-exec show ip sdr <cr>
```

Handler ` RVA 0xF87E5A0 `；selector ` 0 `；EOL ` RVA 0x3474E828 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0a322bbb3e692625](../../evidence/conditions-sets-004.md#c-0a322bbb3e692625) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-050109

```text
(config)# no do-exec show ip sla application <cr>
```

Handler ` RVA 0x102DD0E0 `；selector ` 0 `；EOL ` RVA 0x34A99F68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-049807

```text
(config)# no do-exec show ip sla authentication <cr>
```

Handler ` RVA 0x101DA830 `；selector ` 0 `；EOL ` RVA 0x34A6E750 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055818

```text
(config)# no do-exec show ip sla auto discovery <cr>
```

Handler ` RVA 0x10241B90 `；selector ` 0 `；EOL ` RVA 0x34A7ADC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055810

```text
(config)# no do-exec show ip sla auto group <cr>
```

Handler ` RVA 0x10240F70 `；selector ` 0 `；EOL ` RVA 0x34A7A360 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-156e238d6741f8e3](../../evidence/state_effects-sets-005.md#s-156e238d6741f8e3)

### path-055805

```text
(config)# no do-exec show ip sla auto schedule <cr>
```

Handler ` RVA 0x10241510 `；selector ` 0 `；EOL ` RVA 0x34A7A6B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-060104

```text
(config)# no do-exec show ip sla auto summary-statistics group type ip <string> <cr>
```

Handler ` RVA 0x10241ED0 `；selector ` 2 `；EOL ` RVA 0x34A7B1E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Group name。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-f84b4562b23f6845](../../evidence/parameters-sets-019.md#p-f84b4562b23f6845) · [状态效果 S-517239c6cf5c9328](../../evidence/state_effects-sets-018.md#s-517239c6cf5c9328)

### path-060238

```text
(config)# no do-exec show ip sla auto summary-statistics group type ip <string> ip-address <address> port <number:0..64000> <cr>
```

Handler ` RVA 0x10241ED0 `；selector ` 3 `；EOL ` RVA 0x34A7B2C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Group name；` address ` destination ip address；` unsigned_number ` destination port。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-8528621cf3b47973](../../evidence/parameters-sets-010.md#p-8528621cf3b47973) · [状态效果 S-517239c6cf5c9328](../../evidence/state_effects-sets-018.md#s-517239c6cf5c9328)

### path-060180

```text
(config)# no do-exec show ip sla auto summary-statistics group type ip <string> ip-address <cr>
```

Handler ` RVA 0x10241ED0 `；selector ` 1 `；EOL ` RVA 0x34A7B248 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Group name。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-f84b4562b23f6845](../../evidence/parameters-sets-019.md#p-f84b4562b23f6845) · [状态效果 S-517239c6cf5c9328](../../evidence/state_effects-sets-018.md#s-517239c6cf5c9328)

### path-055839

```text
(config)# no do-exec show ip sla auto template <cr>
```

Handler ` RVA 0x102415E0 `；selector ` 0 `；EOL ` RVA 0x34A7AAC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-2b99b3e934896be9](../../evidence/state_effects-sets-010.md#s-2b99b3e934896be9)

### path-050006

```text
(config)# no do-exec show ip sla collection-statistics <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 0 `；EOL ` RVA 0x34A97478 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-049851

```text
(config)# no do-exec show ip sla configuration <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 14 `；EOL ` RVA 0x34A95AC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-050121

```text
(config)# no do-exec show ip sla distribution-statistics <cr>
```

Handler ` RVA 0x102DD820 `；selector ` 0 `；EOL ` RVA 0x34A97D28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055850

```text
(config)# no do-exec show ip sla distribution-statistics full <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 1 `；EOL ` RVA 0x34A97A58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055829

```text
(config)# no do-exec show ip sla distribution-statistics raw <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 3 `；EOL ` RVA 0x34A977B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055876

```text
(config)# no do-exec show ip sla distribution-statistics tabular <cr>
```

Handler ` RVA 0x102DD820 `；selector ` 0 `；EOL ` RVA 0x34A97D00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-050239

```text
(config)# no do-exec show ip sla endpoint-list <cr>
```

Handler ` RVA 0x10241300 `；selector ` 0 `；EOL ` RVA 0x34A9A980 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-c4b18605a5a7d75a](../../evidence/state_effects-sets-042.md#s-c4b18605a5a7d75a)

### path-055856

```text
(config)# no do-exec show ip sla enhanced-history distribution-statistics <cr>
```

Handler ` RVA 0x102DD570 `；selector ` 0 `；EOL ` RVA 0x34A98318 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-5ad0e407d2986e95](../../evidence/state_effects-sets-020.md#s-5ad0e407d2986e95)

### path-055822

```text
(config)# no do-exec show ip sla ethernet-monitor configuration <cr>
```

Handler ` RVA 0x103C1120 `；selector ` 0 `；EOL ` RVA 0x34B09AE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055773

```text
(config)# no do-exec show ip sla ethernet-monitor responder <cr>
```

Handler ` RVA 0x103C1230 `；selector ` 0 `；EOL ` RVA 0x34B09800 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-049874

```text
(config)# no do-exec show ip sla event-publisher <cr>
```

Handler ` RVA 0x102759D0 `；selector ` 1 `；EOL ` RVA 0x34A890E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055716

```text
(config)# no do-exec show ip sla event-publisher detail <cr>
```

Handler ` RVA 0x102759D0 `；selector ` 2 `；EOL ` RVA 0x34A890C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055789

```text
(config)# no do-exec show ip sla group schedule <cr>
```

Handler ` RVA 0x102DD930 `；selector ` 0 `；EOL ` RVA 0x34A96958 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-058563

```text
(config)# no do-exec show ip sla group schedule details <cr>
```

Handler ` RVA 0x102DD930 `；selector ` 28 `；EOL ` RVA 0x34A96930 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-050200

```text
(config)# no do-exec show ip sla history <cr>
```

Handler ` RVA 0x102DD460 `；selector ` 0 `；EOL ` RVA 0x34A98F20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055894

```text
(config)# no do-exec show ip sla history full <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 5 `；EOL ` RVA 0x34A989A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055927

```text
(config)# no do-exec show ip sla history interval-statistics <cr>
```

Handler ` RVA 0x102DDA40 `；selector ` 45 `；EOL ` RVA 0x34A98EF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055871

```text
(config)# no do-exec show ip sla history raw <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 7 `；EOL ` RVA 0x34A98700 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055913

```text
(config)# no do-exec show ip sla history tabular <cr>
```

Handler ` RVA 0x102DD460 `；selector ` 0 `；EOL ` RVA 0x34A98C50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-049957

```text
(config)# no do-exec show ip sla operational-state <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 16 `；EOL ` RVA 0x34A96E98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-050195

```text
(config)# no do-exec show ip sla reaction-configuration <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 17 `；EOL ` RVA 0x34A9A568 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-050172

```text
(config)# no do-exec show ip sla reaction-trigger <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 12 `；EOL ` RVA 0x34A9A278 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-049867

```text
(config)# no do-exec show ip sla responder <cr>
```

Handler ` RVA 0x101FD080 `；selector ` 0 `；EOL ` RVA 0x34A719E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-050176

```text
(config)# no do-exec show ip sla statistics <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 18 `；EOL ` RVA 0x34A99A90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055917

```text
(config)# no do-exec show ip sla statistics aggregated <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 25 `；EOL ` RVA 0x34A99550 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-058634

```text
(config)# no do-exec show ip sla statistics aggregated details <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 26 `；EOL ` RVA 0x34A99528 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055912

```text
(config)# no do-exec show ip sla statistics details <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 22 `；EOL ` RVA 0x34A99A68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-049873

```text
(config)# no do-exec show ip sla summary <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 46 `；EOL ` RVA 0x34A95DE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-049979

```text
(config)# no do-exec show ip sla totals-statistics <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 4 `；EOL ` RVA 0x34A97188 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-058588

```text
(config)# no do-exec show ip sla twamp connection requests <cr>
```

Handler ` RVA 0x1021EB60 `；selector ` 0 `；EOL ` RVA 0x34A73EC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-3a8f6c782e235fe1](../../evidence/state_effects-sets-013.md#s-3a8f6c782e235fe1)

### path-055763

```text
(config)# no do-exec show ip sla twamp session <cr>
```

Handler ` RVA 0x10238810 `；selector ` 0 `；EOL ` RVA 0x34A76DF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-e260d9d4750ac654](../../evidence/state_effects-sets-048.md#s-e260d9d4750ac654)

### path-055747

```text
(config)# no do-exec show ip sla twamp standards <cr>
```

Handler ` RVA 0x10238750 `；selector ` 0 `；EOL ` RVA 0x34A770A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055790

```text
(config)# no do-exec show ip sla twamp-light session <cr>
```

Handler ` RVA 0x1023AE80 `；selector ` 0 `；EOL ` RVA 0x34A79728 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-5576fc8b79ab552f](../../evidence/state_effects-sets-019.md#s-5576fc8b79ab552f)

### path-038106

```text
(config)# no do-exec show ip sockets <cr>
```

Handler ` RVA 0xCE441C0 `；selector ` 0 `；EOL ` RVA 0x33D31858 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-049989

```text
(config)# no do-exec show ip source binding <cr>
```

Handler ` RVA 0x15FA8BF0 `；selector ` 0 `；EOL ` RVA 0x35E7DBE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b8dbd9ab5c91f915](../../evidence/conditions-sets-071.md#c-b8dbd9ab5c91f915) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-038094

```text
(config)# no do-exec show ip spd <cr>
```

Handler ` RVA 0xCF78E90 `；selector ` 0 `；EOL ` RVA 0x33D31AF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-040417

```text
(config)# no do-exec show ip ssh <cr>
```

Handler ` RVA 0x12360610 `；selector ` 0 `；EOL ` RVA 0x35828848 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055357

```text
(config)# no do-exec show ip static route bfd <cr>
```

Handler ` RVA 0xE2A6F50 `；selector ` 0 `；EOL ` RVA 0x3428F298 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-47dd4a8f8df142f4](../../evidence/conditions-sets-028.md#c-47dd4a8f8df142f4) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055200

```text
(config)# no do-exec show ip static route rwatch-rib <cr>
```

Handler ` RVA 0xE2A7940 `；selector ` 0 `；EOL ` RVA 0x3428F850 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d082036f9d027b1b](../../evidence/conditions-sets-080.md#c-d082036f9d027b1b) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055272

```text
(config)# no do-exec show ip static route sr-polices <cr>
```

Handler ` RVA 0xE2A79D0 `；selector ` 0 `；EOL ` RVA 0x3428FB38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-65d1b2164bbdba22](../../evidence/conditions-sets-039.md#c-65d1b2164bbdba22) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055110

```text
(config)# no do-exec show ip static route summary <cr>
```

Handler ` RVA 0xE2A7770 `；selector ` 0 `；EOL ` RVA 0x3428EE60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-040698

```text
(config)# no do-exec show ip subscriber <cr>
```

Handler ` RVA 0x11A37870 `；selector ` 0 `；EOL ` RVA 0x355CDAE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-4bf4f1cd0f0af17a](../../evidence/state_effects-sets-017.md#s-4bf4f1cd0f0af17a)

### path-047772

```text
(config)# no do-exec show ip tcp header-compression <cr>
```

Handler ` RVA 0xD194400 `；selector ` 0 `；EOL ` RVA 0x33DAB590 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f8c1239e9b64ddef](../../evidence/conditions-sets-096.md#c-f8c1239e9b64ddef) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-048085

```text
(config)# no do-exec show ip telnet status <cr>
```

Handler ` RVA 0xCDEFBC0 `；selector ` 0 `；EOL ` RVA 0x33D02090 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-038232

```text
(config)# no do-exec show ip traffic <cr>
```

Handler ` RVA 0xCECF560 `；selector ` 0 `；EOL ` RVA 0x33D32270 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-054431

```text
(config)# no do-exec show ip traffic topology base <cr>
```

Handler ` RVA 0xCF0ED10 `；selector ` 0 `；EOL ` RVA 0x33D31E70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0db355c33f95471f](../../evidence/state_effects-sets-003.md#s-0db355c33f95471f)

### path-040189

```text
(config)# no do-exec show ip trigger-authentication <cr>
```

Handler ` RVA 0x10571410 `；selector ` 2 `；EOL ` RVA 0x34B5A698 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-040628

```text
(config)# no do-exec show ip virtual-reassembly <cr>
```

Handler ` RVA 0xC78EA70 `；selector ` 0 `；EOL ` RVA 0x33AECED0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ed87af899d4f2fe6](../../evidence/conditions-sets-092.md#c-ed87af899d4f2fe6) · [状态效果 S-e1bed4c26d2550ab](../../evidence/state_effects-sets-048.md#s-e1bed4c26d2550ab)

### path-037897

```text
(config)# no do-exec show ipam counts <cr>
```

Handler ` RVA 0xCEA9220 `；selector ` 0 `；EOL ` RVA 0x33D1B0A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-037877

```text
(config)# no do-exec show ipam pool <cr>
```

Handler ` RVA 0xCEA02D0 `；selector ` 0 `；EOL ` RVA 0x33D1B340 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-037916

```text
(config)# no do-exec show ipam queues <cr>
```

Handler ` RVA 0xCEA9160 `；selector ` 0 `；EOL ` RVA 0x33D1B5E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-037952

```text
(config)# no do-exec show ipam status <cr>
```

Handler ` RVA 0xCE9D6D0 `；selector ` 0 `；EOL ` RVA 0x33D1B890 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-035555

```text
(config)# no do-exec show ipc all <cr>
```

Handler ` RVA 0xD3B9630 `；selector ` 0 `；EOL ` RVA 0x33E2A320 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-ba18dbb5d4a0c2e1](../../evidence/state_effects-sets-039.md#s-ba18dbb5d4a0c2e1)

### path-036114

```text
(config)# no do-exec show ipc app <cr>
```

Handler ` RVA 0xD3BE590 `；selector ` 0 `；EOL ` RVA 0x33E2D5B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-036187

```text
(config)# no do-exec show ipc buffer <cr>
```

Handler ` RVA 0xD39FCA0 `；selector ` 0 `；EOL ` RVA 0x33E2D858 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-052810

```text
(config)# no do-exec show ipc cli <number:0..4294967295> <string> <cr>
```

Handler ` RVA 0xD38B220 `；selector ` 0 `；EOL ` RVA 0x33E2AAB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` IPC Seatid (in hex)；` string ` Remote command string。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-d04ece3d584907a5](../../evidence/parameters-sets-016.md#p-d04ece3d584907a5) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-035957

```text
(config)# no do-exec show ipc delayed <cr>
```

Handler ` RVA 0xD3A24C0 `；selector ` 0 `；EOL ` RVA 0x33E2D018 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-035369

```text
(config)# no do-exec show ipc fc <cr>
```

Handler ` RVA 0xD3B96E0 `；selector ` 0 `；EOL ` RVA 0x33E29FA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-036136

```text
(config)# no do-exec show ipc fragment <cr>
```

Handler ` RVA 0xD3BE5F0 `；selector ` 0 `；EOL ` RVA 0x33E2CD28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-4620d16b7f149cdd](../../evidence/state_effects-sets-015.md#s-4620d16b7f149cdd)

### path-035826

```text
(config)# no do-exec show ipc hog-info <cr>
```

Handler ` RVA 0xD3B8FB0 `；selector ` 0 `；EOL ` RVA 0x33E2C938 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-045846

```text
(config)# no do-exec show ipc keepalive tx <cr>
```

Handler ` RVA 0xD3B8EC0 `；selector ` 0 `；EOL ` RVA 0x33E2E360 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-40f8757b150ea98b](../../evidence/state_effects-sets-014.md#s-40f8757b150ea98b)

### path-045163

```text
(config)# no do-exec show ipc mcast appclass <cr>
```

Handler ` RVA 0xD408040 `；selector ` 0 `；EOL ` RVA 0x33E42858 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-85ea4b013e324daf](../../evidence/state_effects-sets-028.md#s-85ea4b013e324daf)

### path-045270

```text
(config)# no do-exec show ipc mcast groups <cr>
```

Handler ` RVA 0xD407F80 `；selector ` 0 `；EOL ` RVA 0x33E42C30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-83f735be4d1cfda8](../../evidence/state_effects-sets-028.md#s-83f735be4d1cfda8)

### path-052849

```text
(config)# no do-exec show ipc mcast groups <number:1..4294967295> <cr>
```

Handler ` RVA 0xD407F10 `；selector ` 0 `；EOL ` RVA 0x33E42F18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` group id。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-6d276200dc0ed569](../../evidence/parameters-sets-009.md#p-6d276200dc0ed569) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)
