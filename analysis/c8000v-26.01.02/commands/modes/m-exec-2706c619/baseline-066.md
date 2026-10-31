# exec · 六个基础模式的历史连接

[模式索引](README.md) · [总索引](../../README.md)

### path-001702

```text
(exec)# virtual-service throttle disable <cr>
```

Handler ` RVA 0x1590CDA0 `；selector ` 9 `；EOL ` RVA 0x35DBFFC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [状态效果 S-689092b3756cf2ca](../../evidence/state_effects-sets-022.md#s-689092b3756cf2ca)

### path-001685

```text
(exec)# virtual-service throttle enable <cr>
```

Handler ` RVA 0x1590CDA0 `；selector ` 8 `；EOL ` RVA 0x35DBFD18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [状态效果 S-689092b3756cf2ca](../../evidence/state_effects-sets-022.md#s-689092b3756cf2ca)

### path-005427

```text
(exec)# virtual-service uninstall name <string> <cr>
```

Handler ` RVA 0x1590CDA0 `；selector ` 2 `；EOL ` RVA 0x35DBE728 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of the appliance。

[条件 C-6dbab0e3d34d0db0](../../evidence/conditions-sets-042.md#c-6dbab0e3d34d0db0) · [参数 P-a384fddb04c12964](../../evidence/parameters-sets-012.md#p-a384fddb04c12964) · [状态效果 S-689092b3756cf2ca](../../evidence/state_effects-sets-022.md#s-689092b3756cf2ca)

### path-012450

```text
(exec)# vlan database <?sync_force_action@55558b3534c0> <cr>
```

Handler ` RVA 0x15C83360 `；selector ` 0 `；EOL ` RVA 0x35DFF500 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-34cc7d82591d7930](../../evidence/conditions-sets-021.md#c-34cc7d82591d7930) · [缺口 G-85a5b328a2377476](../../evidence/gaps-sets-005.md#g-85a5b328a2377476)

### path-001051

```text
(exec)# vtp password <string> <cr>
```

Handler ` RVA 0x15C83E80 `；selector ` 6 `；EOL ` RVA 0x35DFFF28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` The ascii password for the VTP administrative domain.。

[条件 C-794285eebb8028a5](../../evidence/conditions-sets-047.md#c-794285eebb8028a5) · [参数 P-a090e2e536b9c3e4](../../evidence/parameters-sets-012.md#p-a090e2e536b9c3e4)

### path-000195

```text
(exec)# vtp primary <cr>
```

Handler ` RVA 0x15C83E80 `；selector ` 8 `；EOL ` RVA 0x35DFF948 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1024703c88a6bcb6](../../evidence/conditions-sets-006.md#c-1024703c88a6bcb6)

### path-001054

```text
(exec)# vtp primary force <cr>
```

Handler ` RVA 0x15C83E80 `；selector ` 9 `；EOL ` RVA 0x35DFF920 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1024703c88a6bcb6](../../evidence/conditions-sets-006.md#c-1024703c88a6bcb6)

### path-000194

```text
(exec)# vtp pruning <cr>
```

Handler ` RVA 0x15C83E80 `；selector ` 2 `；EOL ` RVA 0x35E004C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9e3726012375a3e1](../../evidence/conditions-sets-061.md#c-9e3726012375a3e1)

### path-001067

```text
(exec)# vtp version <number:1..2> <cr>
```

Handler ` RVA 0x15C83E80 `；selector ` 7 `；EOL ` RVA 0x35E00238 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Set the administrative domain VTP version number。

[条件 C-f5a7046cc7c2e8ea](../../evidence/conditions-sets-095.md#c-f5a7046cc7c2e8ea) · [参数 P-98c30a1361c1f8c9](../../evidence/parameters-sets-012.md#p-98c30a1361c1f8c9)

### path-000014

```text
(exec)# where <cr>
```

Handler ` RVA 0xDE865C0 `；selector ` 0 `；EOL ` RVA 0x34187EE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d21a91743b03cfd0](../../evidence/conditions-sets-081.md#c-d21a91743b03cfd0)

### path-000202

```text
(exec)# which-route <address> <cr>
```

Handler ` RVA 0x1059FAC0 `；selector ` 0 `；EOL ` RVA 0x34B6A490 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Lookup route to OSI destination address or host name。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [参数 P-b0df04ab3f8b9251](../../evidence/parameters-sets-013.md#p-b0df04ab3f8b9251)

### path-000021

```text
(exec)# who <cr>
```

Handler ` RVA 0xDFE03B0 `；selector ` 0 `；EOL ` RVA 0x3415E1B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-dbe5b845c03dfc65](../../evidence/conditions-sets-085.md#c-dbe5b845c03dfc65)

### path-000027

```text
(exec)# write <cr>
```

Handler ` RVA 0xDFEA900 `；selector ` 3 `；EOL ` RVA 0x3415B0A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cc7273060e2c4907](../../evidence/conditions-sets-079.md#c-cc7273060e2c4907)

### path-012363

```text
(exec)# write core <?ipv4orv6_addr_action@5555896b24d0> <cr>
```

Handler ` RVA 0xDFF0CB0 `；selector ` 1 `；EOL ` RVA 0x3415E5A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2a575596203ae55e](../../evidence/conditions-sets-017.md#c-2a575596203ae55e) · [缺口 G-1351fc69330ed451](../../evidence/gaps-sets-001.md#g-1351fc69330ed451)

### path-000121

```text
(exec)# write erase <cr>
```

Handler ` RVA 0xDFF0D00 `；selector ` 2 `；EOL ` RVA 0x3415E828 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b6f12d98afcca4ee](../../evidence/conditions-sets-071.md#c-b6f12d98afcca4ee)

### path-000131

```text
(exec)# write memory <cr>
```

Handler ` RVA 0xDFEA900 `；selector ` 3 `；EOL ` RVA 0x3415EB38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b6f12d98afcca4ee](../../evidence/conditions-sets-071.md#c-b6f12d98afcca4ee)

### path-000128

```text
(exec)# write mib-data <cr>
```

Handler ` RVA 0xDFEA950 `；selector ` 0 `；EOL ` RVA 0x3415EDD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b6f12d98afcca4ee](../../evidence/conditions-sets-071.md#c-b6f12d98afcca4ee)

### path-000144

```text
(exec)# write network <cr>
```

Handler ` RVA 0xDFE8C50 `；selector ` 4 `；EOL ` RVA 0x3415F0E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b6f12d98afcca4ee](../../evidence/conditions-sets-071.md#c-b6f12d98afcca4ee)

### path-012374

```text
(exec)# write network <url:dynamic> <cr>
```

Handler ` RVA 0xDFE8C50 `；selector ` 4 `；EOL ` RVA 0x3415F0E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3bc0ca2bc953a02a](../../evidence/conditions-sets-023.md#c-3bc0ca2bc953a02a) · [缺口 G-f6451fdf902d02f8](../../evidence/gaps-sets-008.md#g-f6451fdf902d02f8) · [参数 P-ec740f6eed28fe3f](../../evidence/parameters-sets-018.md#p-ec740f6eed28fe3f)

### path-000142

```text
(exec)# write terminal <cr>
```

Handler ` RVA 0xDFE9DB0 `；selector ` 5 `；EOL ` RVA 0x3415F380 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b6f12d98afcca4ee](../../evidence/conditions-sets-071.md#c-b6f12d98afcca4ee)

### path-025298

```text
(exec)# x3 <number:0..22> : <number:0..255> <cr>
```

Handler ` RVA 0xFE6BE60 `；selector ` 0 `；EOL ` RVA 0x348FF8E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3b72f64d5b0948db](../../evidence/conditions-sets-023.md#c-3b72f64d5b0948db) · [缺口 G-cc48573e52deb032](../../evidence/gaps-sets-007.md#g-cc48573e52deb032) · [参数 P-e975d5364f0ba123](../../evidence/parameters-sets-017.md#p-e975d5364f0ba123) · [状态效果 S-312db8310fe16db6](../../evidence/state_effects-sets-011.md#s-312db8310fe16db6)

### path-000012

```text
(exec)# <number:1..99> <cr>
```

Handler ` RVA 0xDE857D0 `；selector ` 1 `；EOL ` RVA 0x34186F40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Session number to resume。

[条件 C-9ecb791aa2192b89](../../evidence/conditions-sets-061.md#c-9ecb791aa2192b89) · [参数 P-5a2136bf20667e61](../../evidence/parameters-sets-007.md#p-5a2136bf20667e61)
