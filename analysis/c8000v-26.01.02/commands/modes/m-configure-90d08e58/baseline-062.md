# configure · 六个基础模式的历史连接

[模式索引](README.md) · [总索引](../../README.md)

### path-059470

```text
(config)# do-exec test ipc bundle status seat <number:0..4294967295> seat-level on <cr>
```

Handler ` RVA 0xD3C4E20 `；selector ` 0 `；EOL ` RVA 0x33E3A950 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` seat id。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [参数 P-a3276e418678fa92](../../evidence/parameters-sets-012.md#p-a3276e418678fa92) · [状态效果 S-0bba274607f548eb](../../evidence/state_effects-sets-003.md#s-0bba274607f548eb)

### path-059473

```text
(config)# do-exec test ipc bundle status session <number:0..4294967295> <number:0..65535> on <cr>
```

Handler ` RVA 0xD3C4C20 `；selector ` 0 `；EOL ` RVA 0x33E3A570 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` port id；` unsigned_number ` session id 。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [参数 P-67bb089c8c087a64](../../evidence/parameters-sets-008.md#p-67bb089c8c087a64) · [状态效果 S-a4536dc84def9457](../../evidence/state_effects-sets-035.md#s-a4536dc84def9457)

### path-031568

```text
(config)# do-exec test ipc callback <cr>
```

Handler ` RVA 0xD3C28E0 `；selector ` 0 `；EOL ` RVA 0x33E35280 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-031708

```text
(config)# do-exec test ipc diag <cr>
```

Handler ` RVA 0xD3C50D0 `；selector ` 0 `；EOL ` RVA 0x33E36708 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-038858

```text
(config)# do-exec test ipc driver stop <cr>
```

Handler ` RVA 0xD3FF9D0 `；selector ` 0 `；EOL ` RVA 0x33E41AE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-da4caf7be07414e1](../../evidence/conditions-sets-084.md#c-da4caf7be07414e1) · [状态效果 S-196da1bd04df76fb](../../evidence/state_effects-sets-006.md#s-196da1bd04df76fb)

### path-038992

```text
(config)# do-exec test ipc drop <number:0..9999> <cr>
```

Handler ` RVA 0xD3C1990 `；selector ` 0 `；EOL ` RVA 0x33E34468 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` n: drop every nth packet sent; n=0 for no dropping。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [参数 P-95af16f3e49d885d](../../evidence/parameters-sets-011.md#p-95af16f3e49d885d) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-058143

```text
(config)# do-exec test ipc drop ack <number:65540..4294967295> <number:0..65535> <number:0..65535> <cr>
```

Handler ` RVA 0xD3C1860 `；selector ` 0 `；EOL ` RVA 0x33E34A90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Port id；` unsigned_number ` Session id；` unsigned_number ` Number of ACKs to drop。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [参数 P-71a0b4089b1449b0](../../evidence/parameters-sets-009.md#p-71a0b4089b1449b0) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-039051

```text
(config)# do-exec test ipc drop next <cr>
```

Handler ` RVA 0xD3C1930 `；selector ` 0 `；EOL ` RVA 0x33E34718 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-058088

```text
(config)# do-exec test ipc mcast appclass subscribe <string> <number:0..15> <cr>
```

Handler ` RVA 0xD452370 `；selector ` 0 `；EOL ` RVA 0x33E44940 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` appclass name；` unsigned_number ` zone number。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [参数 P-43a6c12fa7a112c4](../../evidence/parameters-sets-006.md#p-43a6c12fa7a112c4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-058158

```text
(config)# do-exec test ipc mcast group close <number:0..4294967295> <number:0..65535> <cr>
```

Handler ` RVA 0xD452A50 `；selector ` 0 `；EOL ` RVA 0x33E473E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` group id；` unsigned_number ` session id。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [参数 P-5c89ea6d871c9a6c](../../evidence/parameters-sets-007.md#p-5c89ea6d871c9a6c) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-059421

```text
(config)# do-exec test ipc mcast group create <string> <string> <number:0..15> <cr>
```

Handler ` RVA 0xD453670 `；selector ` 0 `；EOL ` RVA 0x33E45A88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` group name；` string ` appclass name；` unsigned_number ` zone number。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [参数 P-1dc629c309feb0c9](../../evidence/parameters-sets-003.md#p-1dc629c309feb0c9) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-058114

```text
(config)# do-exec test ipc mcast group locate <string> <number:0..15> <cr>
```

Handler ` RVA 0xD453280 `；selector ` 0 `；EOL ` RVA 0x33E46438 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` group name；` unsigned_number ` zone number。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [参数 P-acb97f54bcda4b49](../../evidence/parameters-sets-013.md#p-acb97f54bcda4b49) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-059431

```text
(config)# do-exec test ipc mcast group member add <number:0..4294967295> <number:0..4294967295> <cr>
```

Handler ` RVA 0xD452C20 `；selector ` 0 `；EOL ` RVA 0x33E46F50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` group id；` unsigned_number ` member id。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [参数 P-7e52d3e5b9cd8270](../../evidence/parameters-sets-010.md#p-7e52d3e5b9cd8270) · [状态效果 S-84dd6bce531aeb48](../../evidence/state_effects-sets-028.md#s-84dd6bce531aeb48)

### path-058182

```text
(config)# do-exec test ipc mcast group open <number:0..4294967295> <number:1..2> <cr>
```

Handler ` RVA 0xD452570 `；selector ` 0 `；EOL ` RVA 0x33E477F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` group id；` unsigned_number ` mode of group open(1. reliable 2. unreliable)。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [参数 P-64e154c7c2bb31ab](../../evidence/parameters-sets-008.md#p-64e154c7c2bb31ab) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-054697

```text
(config)# do-exec test ipc mcast group remove <number:0..4294967295> <cr>
```

Handler ` RVA 0xD452EE0 `；selector ` 0 `；EOL ` RVA 0x33E46B40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` group id。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [参数 P-87c59ea63b268029](../../evidence/parameters-sets-010.md#p-87c59ea63b268029) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-058099

```text
(config)# do-exec test ipc mcast group reserve <string> <number:0..15> <cr>
```

Handler ` RVA 0xD4533E0 `；selector ` 0 `；EOL ` RVA 0x33E45DD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` group name；` unsigned_number ` zone number。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [参数 P-d67325ad12ec381b](../../evidence/parameters-sets-016.md#p-d67325ad12ec381b) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-059426

```text
(config)# do-exec test ipc mcast group subscribe <string> <string> <number:0..15> <cr>
```

Handler ` RVA 0xD453040 `；selector ` 0 `；EOL ` RVA 0x33E467F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` group name；` string ` appclass name；` unsigned_number ` zone number。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [参数 P-d154cfe91c8424b2](../../evidence/parameters-sets-016.md#p-d154cfe91c8424b2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-058107

```text
(config)# do-exec test ipc mcast group unreserve <string> <number:0..15> <cr>
```

Handler ` RVA 0xD453540 `；selector ` 0 `；EOL ` RVA 0x33E46108 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` group name；` unsigned_number ` zone number。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [参数 P-4cbd93331c44b6dc](../../evidence/parameters-sets-006.md#p-4cbd93331c44b6dc) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-058109

```text
(config)# do-exec test ipc mcast platform emulation <number:0..4294967295> disable <cr>
```

Handler ` RVA 0xD453C00 `；selector ` 0 `；EOL ` RVA 0x33E45560 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` seat id。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [参数 P-59a3f025174c90ad](../../evidence/parameters-sets-007.md#p-59a3f025174c90ad) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-058100

```text
(config)# do-exec test ipc mcast platform emulation <number:0..4294967295> enable <cr>
```

Handler ` RVA 0xD453C00 `；selector ` 1 `；EOL ` RVA 0x33E452B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` seat id。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [参数 P-59a3f025174c90ad](../../evidence/parameters-sets-007.md#p-59a3f025174c90ad) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-058091

```text
(config)# do-exec test ipc mcast platform max-groups <number:0..15> <number:0..65535> <cr>
```

Handler ` RVA 0xD453D60 `；selector ` 0 `；EOL ` RVA 0x33E44FA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` zone number；` unsigned_number ` max group count。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [参数 P-784d9380b4381ff2](../../evidence/parameters-sets-009.md#p-784d9380b4381ff2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-047778

```text
(config)# do-exec test ipc mcast platform registries <cr>
```

Handler ` RVA 0xD453E30 `；selector ` 0 `；EOL ` RVA 0x33E44C50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-031641

```text
(config)# do-exec test ipc misc <cr>
```

Handler ` RVA 0xD3C40D0 `；selector ` 0 `；EOL ` RVA 0x33E35E10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-039784

```text
(config)# do-exec test ipc ping <number:0..4294967295> <cr>
```

Handler ` RVA 0xD3C4640 `；selector ` 0 `；EOL ` RVA 0x33E3A0A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` seat id。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [参数 P-e106634c2595c7c8](../../evidence/parameters-sets-017.md#p-e106634c2595c7c8) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-055182

```text
(config)# do-exec test ipc port close <number:0..4294967295> <number:0..65535> <cr>
```

Handler ` RVA 0xD3C8D40 `；selector ` 0 `；EOL ` RVA 0x33E38F68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` port id；` unsigned_number ` session id 。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [参数 P-53b2dab481ba7761](../../evidence/parameters-sets-007.md#p-53b2dab481ba7761) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-055247

```text
(config)# do-exec test ipc port create <string> <number:1..3> <cr>
```

Handler ` RVA 0xD3C7F80 `；selector ` 0 `；EOL ` RVA 0x33E37500 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` port name；` unsigned_number ` method of message reception(1. callback 2. fast callback 3. queue)。

[条件 C-9f71008f77cd3eae](../../evidence/conditions-sets-062.md#c-9f71008f77cd3eae) · [参数 P-127dda5a32adb5cf](../../evidence/parameters-sets-002.md#p-127dda5a32adb5cf) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-055333

```text
(config)# do-exec test ipc port free <number:0..4294967295> <number:1..1000000> <cr>
```

Handler ` RVA 0xD3C8FA0 `；selector ` 0 `；EOL ` RVA 0x33E39A10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` port id；` unsigned_number ` Number of messages。

[条件 C-419d025b99e7e671](../../evidence/conditions-sets-026.md#c-419d025b99e7e671) · [参数 P-cbcec36820e3d032](../../evidence/parameters-sets-015.md#p-cbcec36820e3d032) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-059896

```text
(config)# do-exec test ipc port msend <number:0..4294967295> <number:0..65535> <number:0..65535> <number:1..1000000> <number:1..4064> <cr>
```

Handler ` RVA 0xD3C8300 `；selector ` 0 `；EOL ` RVA 0x33E38040 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` port id；` unsigned_number ` start session id；` unsigned_number ` end session id；` unsigned_number ` number of messages to be sent；` unsigned_number ` size of message。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [参数 P-78d8a152dee698ee](../../evidence/parameters-sets-009.md#p-78d8a152dee698ee) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-049028

```text
(config)# do-exec test ipc port notify enable <cr>
```

Handler ` RVA 0xD3C8F00 `；selector ` 0 `；EOL ` RVA 0x33E395B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [状态效果 S-3f97d3c940090142](../../evidence/state_effects-sets-014.md#s-3f97d3c940090142)

### path-055285

```text
(config)# do-exec test ipc port open <number:0..4294967295> <number:1..3> <cr>
```

Handler ` RVA 0xD3C80F0 `；selector ` 0 `；EOL ` RVA 0x33E37A98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` port id；` unsigned_number ` mode of port open(1. reliable 2. unreliable 3. unrel-with-not)。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [参数 P-d00235038e651bbb](../../evidence/parameters-sets-016.md#p-d00235038e651bbb) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-049036

```text
(config)# do-exec test ipc port remove <number:0..4294967295> <cr>
```

Handler ` RVA 0xD3C8DC0 `；selector ` 0 `；EOL ` RVA 0x33E392B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` port id。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [参数 P-a00f33de364d076f](../../evidence/parameters-sets-012.md#p-a00f33de364d076f) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-049110

```text
(config)# do-exec test ipc port send header <cr>
```

Handler ` RVA 0xD3C8890 `；selector ` 0 `；EOL ` RVA 0x33E38678 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97228be178e3388b](../../evidence/conditions-sets-058.md#c-97228be178e3388b) · [状态效果 S-e1821b0bd8cbfbef](../../evidence/state_effects-sets-048.md#s-e1821b0bd8cbfbef)

### path-062890

```text
(config)# do-exec test ipc port send header <number:0..4294967295> <cr>
```

Handler ` RVA 0xD3C8890 `；selector ` 0 `；EOL ` RVA 0x33E38678 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` next four bytes。

[条件 C-ef808b96fe57d8e9](../../evidence/conditions-sets-092.md#c-ef808b96fe57d8e9) · [缺口 G-e5830d8fae2a5b5b](../../evidence/gaps-sets-008.md#g-e5830d8fae2a5b5b) · [参数 P-1f43a1dac40ab39f](../../evidence/parameters-sets-003.md#p-1f43a1dac40ab39f) · [状态效果 S-1ea08a886067df28](../../evidence/state_effects-sets-007.md#s-1ea08a886067df28)

### path-031541

```text
(config)# do-exec test ipc queue <cr>
```

Handler ` RVA 0xD3C2330 `；selector ` 0 `；EOL ` RVA 0x33E34FD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-039886

```text
(config)# do-exec test ipc retry-period <number:0..50000> <cr>
```

Handler ` RVA 0xD3C6520 `；selector ` 0 `；EOL ` RVA 0x33E3B410 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Value。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [参数 P-8966cb03db7d6b54](../../evidence/parameters-sets-011.md#p-8966cb03db7d6b54) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-031649

```text
(config)# do-exec test ipc rpc <cr>
```

Handler ` RVA 0xD3C1DE0 `；selector ` 0 `；EOL ` RVA 0x33E358B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-058089

```text
(config)# do-exec test ipc ru create <string> <number:1..15> conf <cr>
```

Handler ` RVA 0xD3FEFE0 `；selector ` 0 `；EOL ` RVA 0x33E40F90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` IPC RU name；` unsigned_number ` Priority of IPC RU。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [参数 P-799b680ccf4bb802](../../evidence/parameters-sets-009.md#p-799b680ccf4bb802) · [状态效果 S-4ee613342aedeac2](../../evidence/state_effects-sets-017.md#s-4ee613342aedeac2)

### path-047865

```text
(config)# do-exec test ipc ru remove <string> <cr>
```

Handler ` RVA 0xD3FF380 `；selector ` 0 `；EOL ` RVA 0x33E412F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` IPC RU id to be removed(in hex)。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [参数 P-d52691dd1900e41d](../../evidence/parameters-sets-016.md#p-d52691dd1900e41d) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-059873

```text
(config)# do-exec test ipc ru tune-thresh <string> <number:1..6> rising major <number:0..10000> <cr>
```

Handler ` RVA 0xD3FF5E0 `；selector ` 0 `；EOL ` RVA 0x33E41728 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` IPC RU id(in hex) whose threshold need to be tuned；` unsigned_number ` Entity to be thresholded: 1. Tx Session Usage 2. Rx Session Usage 3. Rx Port Usage 4. RU Usage 5. Reliable Session ACK pending 6. Seat level ACK pending ；` unsigned_number ` New threshold value。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [参数 P-8d1eaef814f1e8b7](../../evidence/parameters-sets-011.md#p-8d1eaef814f1e8b7) · [状态效果 S-fedd3b8c4429a968](../../evidence/state_effects-sets-054.md#s-fedd3b8c4429a968)

### path-038857

```text
(config)# do-exec test ipc seat-fc <number:0..1024> <cr>
```

Handler ` RVA 0xD3C61B0 `；selector ` 0 `；EOL ` RVA 0x33E33848 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` state。

[条件 C-03eba49778e23d8f](../../evidence/conditions-sets-002.md#c-03eba49778e23d8f) · [参数 P-c3cdd8e9175bec8d](../../evidence/parameters-sets-015.md#p-c3cdd8e9175bec8d) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-048690

```text
(config)# do-exec test ipc size <number:0..100000> <number:0..1000> <cr>
```

Handler ` RVA 0xD3C3720 `；selector ` 0 `；EOL ` RVA 0x33E39DB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` IPC packet size；` unsigned_number ` Number of IPC packet。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [参数 P-646aa7c03b43ab31](../../evidence/parameters-sets-008.md#p-646aa7c03b43ab31) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-031476

```text
(config)# do-exec test ipc slavecore <cr>
```

Handler ` RVA 0xD3C3CC0 `；selector ` 0 `；EOL ` RVA 0x33E34158 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-031518

```text
(config)# do-exec test ipc slavelog <cr>
```

Handler ` RVA 0xD3C3D00 `；selector ` 0 `；EOL ` RVA 0x33E34D30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-031621

```text
(config)# do-exec test ipc speed <cr>
```

Handler ` RVA 0xD3C3840 `；selector ` 0 `；EOL ` RVA 0x33E35B68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-031666

```text
(config)# do-exec test ipc split-init <cr>
```

Handler ` RVA 0xD3C1330 `；selector ` 0 `；EOL ` RVA 0x33E360B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-031590

```text
(config)# do-exec test ipc task-pool <cr>
```

Handler ` RVA 0xD3C2D00 `；selector ` 0 `；EOL ` RVA 0x33E35528 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-031378

```text
(config)# do-exec test ipc toggle-mask-error <cr>
```

Handler ` RVA 0xD3FFA80 `；selector ` 0 `；EOL ` RVA 0x33E40B90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-058123

```text
(config)# do-exec test ipc traffic <number:0..4294967295> <number:1..2147483647> <number:1..5> <number:1..50000> <cr>
```

Handler ` RVA 0xD3C5290 `；selector ` 0 `；EOL ` RVA 0x33E32570 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Destination Seat ID or Port ID；` unsigned_number ` Number of messages to be sent；` unsigned_number `  1 - Unreliable 2 - Reliable Non-blocking 3 - RPC blocking 4 - Reliable Non-Blocking and Final Blocked 5 - Reliable Blocking；` unsigned_number ` Size of each IPC message。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [参数 P-8ec07d117ce331bc](../../evidence/parameters-sets-011.md#p-8ec07d117ce331bc) · [状态效果 S-cc74ccd95fd1e2ae](../../evidence/state_effects-sets-043.md#s-cc74ccd95fd1e2ae)

### path-047736

```text
(config)# do-exec test ipc traffic abort <number:0..2147483647> <cr>
```

Handler ` RVA 0xD3C5D40 `；selector ` 0 `；EOL ` RVA 0x33E32A28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` The process id which is sending the traffic。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [参数 P-116ec98253371dfa](../../evidence/parameters-sets-002.md#p-116ec98253371dfa) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-039614

```text
(config)# do-exec test ipc watermark callback <cr>
```

Handler ` RVA 0xD3C6050 `；selector ` 0 `；EOL ` RVA 0x33E36F30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-038709

```text
(config)# do-exec test ipc window-size <number:32..1024> <cr>
```

Handler ` RVA 0xD3C5130 `；selector ` 0 `；EOL ` RVA 0x33E32DB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` window-size。

[条件 C-0ad39be4f18f5ed7](../../evidence/conditions-sets-005.md#c-0ad39be4f18f5ed7) · [参数 P-a42b339d50af46ca](../../evidence/parameters-sets-013.md#p-a42b339d50af46ca) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-048522

```text
(config)# do-exec test ipc zone seat2slave <number:2..15> <cr>
```

Handler ` RVA 0xD3C79C0 `；selector ` 0 `；EOL ` RVA 0x33E36A90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` zone number。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [参数 P-11ee00fec1791900](../../evidence/parameters-sets-002.md#p-11ee00fec1791900) · [状态效果 S-8970cfd47940348c](../../evidence/state_effects-sets-029.md#s-8970cfd47940348c)

### path-061289

```text
(config)# do-exec test iphc context lifetime <number:dynamic> <cr>
```

Handler ` RVA 0xD19AC60 `；selector ` 0 `；EOL ` RVA 0x33DA9230 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Context lifetime &lt;milli secs&gt;。

[条件 C-5ca9e9251c79ac28](../../evidence/conditions-sets-036.md#c-5ca9e9251c79ac28) · [缺口 G-d61c8518e7dbd032](../../evidence/gaps-sets-007.md#g-d61c8518e7dbd032) · [参数 P-159c11e81284fd63](../../evidence/parameters-sets-002.md#p-159c11e81284fd63) · [状态效果 S-43c2cde57372c7a5](../../evidence/state_effects-sets-015.md#s-43c2cde57372c7a5)

### path-045150

```text
(config)# do-exec test iphc context lifetime default <cr>
```

Handler ` RVA 0xD19AC60 `；selector ` 0 `；EOL ` RVA 0x33DA9230 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-43c2cde57372c7a5](../../evidence/state_effects-sets-015.md#s-43c2cde57372c7a5)

### path-046072

```text
(config)# do-exec test ipv6 access-list common enable <cr>
```

Handler ` RVA 0x12166310 `；selector ` 0 `；EOL ` RVA 0x357B0D38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-155649a3af50aea7](../../evidence/conditions-sets-008.md#c-155649a3af50aea7) · [状态效果 S-1b443e437f0a1cb6](../../evidence/state_effects-sets-006.md#s-1b443e437f0a1cb6)

### path-062297

```text
(config)# do-exec test ipv6 dhcp-client autoinstall <interface> test-case <number:1..65535> <cr>
```

Handler ` RVA 0x1218A870 `；selector ` 0 `；EOL ` RVA 0x357BD568 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` test case number。

[条件 C-cfd4e254937d4c11](../../evidence/conditions-sets-080.md#c-cfd4e254937d4c11) · [缺口 G-5f54ac697a1afdad](../../evidence/gaps-sets-004.md#g-5f54ac697a1afdad) · [参数 P-2a82be7442163efa](../../evidence/parameters-sets-004.md#p-2a82be7442163efa) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-053510

```text
(config)# do-exec test ipv6 dhcp-client lease-query address <address> <cr>
```

Handler ` RVA 0x12189610 `；selector ` 0 `；EOL ` RVA 0x357BD0A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IPv6 address。

[条件 C-155649a3af50aea7](../../evidence/conditions-sets-008.md#c-155649a3af50aea7) · [参数 P-486f1516edce2b17](../../evidence/parameters-sets-006.md#p-486f1516edce2b17) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062500

```text
(config)# do-exec test ipv6 dhcp-client lease-query address <address> out-intf <interface> <cr>
```

Handler ` RVA 0x12189610 `；selector ` 0 `；EOL ` RVA 0x357BD0A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` IPv6 address。

[条件 C-f7609b4d82369e92](../../evidence/conditions-sets-096.md#c-f7609b4d82369e92) · [缺口 G-3005d022f58cfb77](../../evidence/gaps-sets-002.md#g-3005d022f58cfb77) · [参数 P-ebbf146ca8715d78](../../evidence/parameters-sets-018.md#p-ebbf146ca8715d78) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-036578

```text
(config)# do-exec test ipv6 dhcp-relay bulk-lease-query <cr>
```

Handler ` RVA 0x121AF430 `；selector ` 0 `；EOL ` RVA 0x357C3B48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-155649a3af50aea7](../../evidence/conditions-sets-008.md#c-155649a3af50aea7) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-036699

```text
(config)# do-exec test ipv6 dhcp-relay ldra <cr>
```

Handler ` RVA 0x121AE630 `；selector ` 0 `；EOL ` RVA 0x357C3E30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-155649a3af50aea7](../../evidence/conditions-sets-008.md#c-155649a3af50aea7) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-046031

```text
(config)# do-exec test ipv6 dhcp-server hostnum <number:0..4294967295> <cr>
```

Handler ` RVA 0x121D2540 `；selector ` 0 `；EOL ` RVA 0x357CED60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` 32 bit host number in hex。

[条件 C-155649a3af50aea7](../../evidence/conditions-sets-008.md#c-155649a3af50aea7) · [参数 P-e77823c1af7cfc82](../../evidence/parameters-sets-017.md#p-e77823c1af7cfc82) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062607

```text
(config)# do-exec test ipv6 nd cache populate <interface> <address> <number:1..1000000> <address> <cr>
```

Handler ` RVA 0x1231AE00 `；selector ` 0 `；EOL ` RVA 0x357FCFC8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5ed4bc48ce60ef22](../../evidence/conditions-sets-037.md#c-5ed4bc48ce60ef22) · [缺口 G-57f47da0774c2188](../../evidence/gaps-sets-004.md#g-57f47da0774c2188) · [参数 P-9983055205a54d33](../../evidence/parameters-sets-012.md#p-9983055205a54d33) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062508

```text
(config)# do-exec test ipv6 nd cache stale-traffic <interface> <address> <number:1..1000000> <cr>
```

Handler ` RVA 0x1231B260 `；selector ` 0 `；EOL ` RVA 0x357FD3C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2302aac8be7321e0](../../evidence/conditions-sets-014.md#c-2302aac8be7321e0) · [缺口 G-e4f0c54725e9cd21](../../evidence/gaps-sets-008.md#g-e4f0c54725e9cd21) · [参数 P-21b74598aea17359](../../evidence/parameters-sets-003.md#p-21b74598aea17359) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-053633

```text
(config)# do-exec test ipv6 nd client del <number:0..15> <cr>
```

Handler ` RVA 0x1231B440 `；selector ` 0 `；EOL ` RVA 0x357FCA70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` client id。

[条件 C-155649a3af50aea7](../../evidence/conditions-sets-008.md#c-155649a3af50aea7) · [参数 P-bd545017980207cf](../../evidence/parameters-sets-014.md#p-bd545017980207cf) · [状态效果 S-cc96068161b2f7f8](../../evidence/state_effects-sets-043.md#s-cc96068161b2f7f8)

### path-062504

```text
(config)# do-exec test ipv6 nd client pfx-adv-ctrl <number:0..15> <interface> enable <cr>
```

Handler ` RVA 0x1231B570 `；selector ` 0 `；EOL ` RVA 0x357FC1F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` client id。

[条件 C-26e5a3ba623b3604](../../evidence/conditions-sets-015.md#c-26e5a3ba623b3604) · [缺口 G-cf35f113483d5765](../../evidence/gaps-sets-007.md#g-cf35f113483d5765) · [参数 P-715db31255dbb2ae](../../evidence/parameters-sets-009.md#p-715db31255dbb2ae) · [状态效果 S-4ef512f102dfca30](../../evidence/state_effects-sets-017.md#s-4ef512f102dfca30)

### path-062509

```text
(config)# do-exec test ipv6 nd client sendra <number:0..15> <interface> <address> <cr>
```

Handler ` RVA 0x1231B650 `；selector ` 0 `；EOL ` RVA 0x357FC6D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` client id；` address ` Destination address。

[条件 C-ef3095dc66cdc7c7](../../evidence/conditions-sets-092.md#c-ef3095dc66cdc7c7) · [缺口 G-21c50847db42e3fe](../../evidence/gaps-sets-002.md#g-21c50847db42e3fe) · [参数 P-b75c11ff1b63e956](../../evidence/parameters-sets-014.md#p-b75c11ff1b63e956) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062642

```text
(config)# do-exec test ipv6 nd db populate <interface> <address> <number:1..262144> <address> add <cr>
```

Handler ` RVA 0x1231B0A0 `；selector ` 0 `；EOL ` RVA 0x35800088 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5a766ee0de7c218b](../../evidence/conditions-sets-035.md#c-5a766ee0de7c218b) · [缺口 G-accf9b67d7c43119](../../evidence/gaps-sets-006.md#g-accf9b67d7c43119) · [参数 P-431814581a662b90](../../evidence/parameters-sets-006.md#p-431814581a662b90) · [状态效果 S-0bca48dc54e06469](../../evidence/state_effects-sets-003.md#s-0bca48dc54e06469)

### path-061954

```text
(config)# do-exec test ipv6 nd ha <interface> <number:0..1> <cr>
```

Handler ` RVA 0x1231D080 `；selector ` 0 `；EOL ` RVA 0x357FDC08 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` sense。

[条件 C-ceb903d8e6c5d34c](../../evidence/conditions-sets-080.md#c-ceb903d8e6c5d34c) · [缺口 G-721a3bde9d9af595](../../evidence/gaps-sets-004.md#g-721a3bde9d9af595) · [参数 P-fb987dba5cf3ff63](../../evidence/parameters-sets-019.md#p-fb987dba5cf3ff63) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061942

```text
(config)# do-exec test ipv6 nd mip_rmg <interface> <number:0..1> <cr>
```

Handler ` RVA 0x1231D120 `；selector ` 0 `；EOL ` RVA 0x357FD7D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` sense。

[条件 C-5429efcf50129de7](../../evidence/conditions-sets-033.md#c-5429efcf50129de7) · [缺口 G-c99a8b86f93d83ff](../../evidence/gaps-sets-007.md#g-c99a8b86f93d83ff) · [参数 P-bb230184350e3250](../../evidence/parameters-sets-014.md#p-bb230184350e3250) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-045989

```text
(config)# do-exec test ipv6 nd pd-limit <number:0..2147483647> <cr>
```

Handler ` RVA 0x123198C0 `；selector ` 0 `；EOL ` RVA 0x357FBA50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of entries。

[条件 C-155649a3af50aea7](../../evidence/conditions-sets-008.md#c-155649a3af50aea7) · [参数 P-defb6b1a96e6831a](../../evidence/parameters-sets-017.md#p-defb6b1a96e6831a) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-053480

```text
(config)# do-exec test ipv6 nd repopulate queue-size <number:1..512> <cr>
```

Handler ` RVA 0x123197B0 `；selector ` 0 `；EOL ` RVA 0x357FBD80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Queue size。

[条件 C-155649a3af50aea7](../../evidence/conditions-sets-008.md#c-155649a3af50aea7) · [参数 P-6970d6f8d867e4bf](../../evidence/parameters-sets-008.md#p-6970d6f8d867e4bf) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062285

```text
(config)# do-exec test ipv6 nd router number <number:0..70000> <interface> <cr>
```

Handler ` RVA 0x123197F0 `；selector ` 0 `；EOL ` RVA 0x357FAF90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Number of routers。

[条件 C-d725a4fbfb3e7d02](../../evidence/conditions-sets-083.md#c-d725a4fbfb3e7d02) · [缺口 G-7cff1df5a0d79896](../../evidence/gaps-sets-005.md#g-7cff1df5a0d79896) · [参数 P-c7eb82c1d7f6f990](../../evidence/parameters-sets-015.md#p-c7eb82c1d7f6f990) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062312

```text
(config)# do-exec test ipv6 nd session create <interface> <number:1..65535> <cr>
```

Handler ` RVA 0x1231BBF0 `；selector ` 0 `；EOL ` RVA 0x357FE450 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Count。

[条件 C-466189db50f19325](../../evidence/conditions-sets-027.md#c-466189db50f19325) · [缺口 G-c7351edaf533bc44](../../evidence/gaps-sets-007.md#g-c7351edaf533bc44) · [参数 P-70b9f1362143ec9a](../../evidence/parameters-sets-009.md#p-70b9f1362143ec9a) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062518

```text
(config)# do-exec test ipv6 nd session delete <interface> <number:1..65535> <number:1..65535> <cr>
```

Handler ` RVA 0x1231C500 `；selector ` 0 `；EOL ` RVA 0x357FFB60 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Initial；` unsigned_number ` Count。

[条件 C-1e2e2839d808db90](../../evidence/conditions-sets-012.md#c-1e2e2839d808db90) · [缺口 G-4b0779d99fd91235](../../evidence/gaps-sets-003.md#g-4b0779d99fd91235) · [参数 P-4a8cc4f4585b8595](../../evidence/parameters-sets-006.md#p-4a8cc4f4585b8595) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062611

```text
(config)# do-exec test ipv6 nd session mac <interface> <number:1..65535> <number:1..65535> <address> <cr>
```

Handler ` RVA 0x1231BFD0 `；selector ` 0 `；EOL ` RVA 0x357FEED8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Initial；` unsigned_number ` Count；` address ` 48-bit hardware address。

[条件 C-f50e5558b33d1b90](../../evidence/conditions-sets-095.md#c-f50e5558b33d1b90) · [缺口 G-e74216921dd04b84](../../evidence/gaps-sets-008.md#g-e74216921dd04b84) · [参数 P-b17f2a63c4a6ce9d](../../evidence/parameters-sets-013.md#p-b17f2a63c4a6ce9d) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062924

```text
(config)# do-exec test ipv6 nd session prefix <interface> <number:1..65535> <number:1..65535> <prefix:dynamic> <cr>
```

Handler ` RVA 0x1231BD40 `；selector ` 0 `；EOL ` RVA 0x357FE910 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Initial；` unsigned_number ` Count；` prefix_dynamic ` IPv6 prefix x:x::y/&lt;z&gt;。

[条件 C-d28781bae2a8bec3](../../evidence/conditions-sets-081.md#c-d28781bae2a8bec3) · [缺口 G-abc07253a2c5cfbf](../../evidence/gaps-sets-006.md#g-abc07253a2c5cfbf) · [参数 P-08b690d7942b68e0](../../evidence/parameters-sets-001.md#p-08b690d7942b68e0) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062311

```text
(config)# do-exec test ipv6 nd session set <interface> <number:0..1> <cr>
```

Handler ` RVA 0x1231B730 `；selector ` 0 `；EOL ` RVA 0x357FE060 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` sense。

[条件 C-35e48e485a81e54a](../../evidence/conditions-sets-021.md#c-35e48e485a81e54a) · [缺口 G-11f232c2d8c6cee5](../../evidence/gaps-sets-001.md#g-11f232c2d8c6cee5) · [参数 P-d122028835d514e9](../../evidence/parameters-sets-016.md#p-d122028835d514e9) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062514

```text
(config)# do-exec test ipv6 nd session start <interface> <number:1..65535> <number:1..65535> <cr>
```

Handler ` RVA 0x1231C3B0 `；selector ` 0 `；EOL ` RVA 0x357FF308 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Initial；` unsigned_number ` Count。

[条件 C-079bb7400ba2b5b0](../../evidence/conditions-sets-003.md#c-079bb7400ba2b5b0) · [缺口 G-93bc545592df5d9e](../../evidence/gaps-sets-005.md#g-93bc545592df5d9e) · [参数 P-2b22a719a8c59122](../../evidence/parameters-sets-004.md#p-2b22a719a8c59122) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062516

```text
(config)# do-exec test ipv6 nd session stop <interface> <number:1..65535> <number:1..65535> <cr>
```

Handler ` RVA 0x1231C500 `；selector ` 0 `；EOL ` RVA 0x357FF750 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Initial；` unsigned_number ` Count。

[条件 C-e9d531054b1f701b](../../evidence/conditions-sets-090.md#c-e9d531054b1f701b) · [缺口 G-7834f58d7b6b66b5](../../evidence/gaps-sets-005.md#g-7834f58d7b6b66b5) · [参数 P-1a8efde88a20cf81](../../evidence/parameters-sets-002.md#p-1a8efde88a20cf81) · [状态效果 S-990b539b72223e6e](../../evidence/state_effects-sets-033.md#s-990b539b72223e6e)

### path-062499

```text
(config)# do-exec test ipv6 nd test-evpn-entry add <address> <interface> <address> <cr>
```

Handler ` RVA 0x12319970 `；selector ` 0 `；EOL ` RVA 0x357FB6E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` IPv6 address；` address ` 48-bit hardware address。

[条件 C-53ce4a9192e52f27](../../evidence/conditions-sets-033.md#c-53ce4a9192e52f27) · [缺口 G-90976623ec772783](../../evidence/gaps-sets-005.md#g-90976623ec772783) · [参数 P-2bebad0a41458ee1](../../evidence/parameters-sets-004.md#p-2bebad0a41458ee1) · [状态效果 S-81da60301daef59c](../../evidence/state_effects-sets-028.md#s-81da60301daef59c)

### path-036475

```text
(config)# do-exec test ipv6 nd test-nsf <cr>
```

Handler ` RVA 0x12319920 `；selector ` 0 `；EOL ` RVA 0x357FB260 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-155649a3af50aea7](../../evidence/conditions-sets-008.md#c-155649a3af50aea7) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-046165

```text
(config)# do-exec test ipv6 rib multicast add <cr>
```

Handler ` RVA 0x1230B6E0 `；selector ` 0 `；EOL ` RVA 0x357ECD58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fa9eae260bcb2076](../../evidence/conditions-sets-097.md#c-fa9eae260bcb2076) · [状态效果 S-776f3b614995d336](../../evidence/state_effects-sets-025.md#s-776f3b614995d336)

### path-061940

```text
(config)# do-exec test ipv6 rib multicast add <interface> <cr>
```

Handler ` RVA 0x1230B6E0 `；selector ` 0 `；EOL ` RVA 0x357ECD58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5b62227e89e2a9cf](../../evidence/conditions-sets-036.md#c-5b62227e89e2a9cf) · [缺口 G-d52f7d19630ab820](../../evidence/gaps-sets-007.md#g-d52f7d19630ab820) · [参数 P-de7fba858ec55a6c](../../evidence/parameters-sets-017.md#p-de7fba858ec55a6c) · [状态效果 S-776f3b614995d336](../../evidence/state_effects-sets-025.md#s-776f3b614995d336)

### path-062999

```text
(config)# do-exec test ipv6 rib path add clone <prefix:dynamic> <address> <interface> <interface> <cr>
```

Handler ` RVA 0x1230C860 `；selector ` 0 `；EOL ` RVA 0x357EF460 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c6db5d3c6470ede6](../../evidence/conditions-sets-077.md#c-c6db5d3c6470ede6) · [缺口 G-30fcf680cee6b2b0](../../evidence/gaps-sets-002.md#g-30fcf680cee6b2b0) · [参数 P-0f0200380bef9f0b](../../evidence/parameters-sets-002.md#p-0f0200380bef9f0b) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062927

```text
(config)# do-exec test ipv6 rib path add foreign <number:1..16> <prefix:dynamic> <address> <interface> <cr>
```

Handler ` RVA 0x1230B900 `；selector ` 0 `；EOL ` RVA 0x357EDA00 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-cdd0e52fa5d391b8](../../evidence/conditions-sets-079.md#c-cdd0e52fa5d391b8) · [缺口 G-25b92b0a47ab8ce1](../../evidence/gaps-sets-002.md#g-25b92b0a47ab8ce1) · [参数 P-56f0ec8311f47521](../../evidence/parameters-sets-007.md#p-56f0ec8311f47521) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-063002

```text
(config)# do-exec test ipv6 rib path add primary <number:1..16> <prefix:dynamic> <address> <interface> <address> <interface> <number:1..255> <number:1..255> <cr>
```

Handler ` RVA 0x1230C050 `；selector ` 0 `；EOL ` RVA 0x357EEA10 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-071d51b50dde22b2](../../evidence/conditions-sets-003.md#c-071d51b50dde22b2) · [缺口 G-80dd46fdf6d1f397](../../evidence/gaps-sets-005.md#g-80dd46fdf6d1f397) · [参数 P-ef0442f2797d35e1](../../evidence/parameters-sets-018.md#p-ef0442f2797d35e1) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062936

```text
(config)# do-exec test ipv6 rib path add repair <number:1..16> <prefix:dynamic> <address> <interface> <number:1..255> <number:1..255> <cr>
```

Handler ` RVA 0x1230C5A0 `；selector ` 0 `；EOL ` RVA 0x357EDF68 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0eecdd067a6d5ee4](../../evidence/conditions-sets-006.md#c-0eecdd067a6d5ee4) · [缺口 G-330cd16605a65ef4](../../evidence/gaps-sets-002.md#g-330cd16605a65ef4) · [参数 P-b15a2736acb0c202](../../evidence/parameters-sets-013.md#p-b15a2736acb0c202) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062940

```text
(config)# do-exec test ipv6 rib path add tilfa-primary <number:1..16> <prefix:dynamic> <address> <interface> <number:16777217..33554430> <number:1..255> <number:1..255> <cr>
```

Handler ` RVA 0x1230BAA0 `；selector ` 0 `；EOL ` RVA 0x357EEF98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5aae242d94afdebf](../../evidence/conditions-sets-036.md#c-5aae242d94afdebf) · [缺口 G-7594a8d475db56be](../../evidence/gaps-sets-005.md#g-7594a8d475db56be) · [参数 P-6f87358eaf7e38de](../../evidence/parameters-sets-009.md#p-6f87358eaf7e38de) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062668

```text
(config)# do-exec test ipv6 rib path add tilfa-repair <number:1..16> <prefix:dynamic> <number:16777217..33554430> <number:1..255> <number:1..255> <cr>
```

Handler ` RVA 0x1230C340 `；selector ` 0 `；EOL ` RVA 0x357EE438 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7a97d73dde6ba714](../../evidence/conditions-sets-048.md#c-7a97d73dde6ba714) · [缺口 G-5a8a83a4d2c3b5e0](../../evidence/gaps-sets-004.md#g-5a8a83a4d2c3b5e0) · [参数 P-d385be79b243bc1c](../../evidence/parameters-sets-016.md#p-d385be79b243bc1c) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062928

```text
(config)# do-exec test ipv6 rib path del foreign <number:1..16> <prefix:dynamic> <address> <interface> <cr>
```

Handler ` RVA 0x1230CAA0 `；selector ` 0 `；EOL ` RVA 0x357EF998 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-60478ffa664840d0](../../evidence/conditions-sets-037.md#c-60478ffa664840d0) · [缺口 G-e8ceecf22fc1d3d3](../../evidence/gaps-sets-008.md#g-e8ceecf22fc1d3d3) · [参数 P-feab6951d2a3654a](../../evidence/parameters-sets-019.md#p-feab6951d2a3654a) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062935

```text
(config)# do-exec test ipv6 rib path del primary <number:1..16> <prefix:dynamic> <address> <interface> <number:1..255> <number:1..255> <cr>
```

Handler ` RVA 0x1230BD80 `；selector ` 0 `；EOL ` RVA 0x357EFE68 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-239a5ce68b34d88d](../../evidence/conditions-sets-014.md#c-239a5ce68b34d88d) · [缺口 G-fd97ce8ba817775f](../../evidence/gaps-sets-009.md#g-fd97ce8ba817775f) · [参数 P-11bbc1be4c4d98b5](../../evidence/parameters-sets-002.md#p-11bbc1be4c4d98b5) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-059190

```text
(config)# do-exec test ipv6 rib pdb add <number:1..16> <number:1..255> <number:0..1> <cr>
```

Handler ` RVA 0x1230B4F0 `；selector ` 0 `；EOL ` RVA 0x357ED4E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-155649a3af50aea7](../../evidence/conditions-sets-008.md#c-155649a3af50aea7) · [参数 P-ebee9a394e927907](../../evidence/parameters-sets-018.md#p-ebee9a394e927907) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-053393

```text
(config)# do-exec test ipv6 rib pdb del <number:1..16> <cr>
```

Handler ` RVA 0x1230B640 `；selector ` 0 `；EOL ` RVA 0x357ED140 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-155649a3af50aea7](../../evidence/conditions-sets-008.md#c-155649a3af50aea7) · [参数 P-4d58cc23e6e79a5d](../../evidence/parameters-sets-006.md#p-4d58cc23e6e79a5d) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062937

```text
(config)# do-exec test ipv6 rib prefix add <number:1..16> <prefix:dynamic> <address> <interface> <number:1..255> <number:1..255> <number:1..32000> <cr>
```

Handler ` RVA 0x1230CC40 `；selector ` 0 `；EOL ` RVA 0x357F0558 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` id；` prefix_dynamic ` prefix；` address ` neighbour；` unsigned_number ` admin；` unsigned_number ` metric；` unsigned_number ` repeat。

[条件 C-fdeba5129a6cfaeb](../../evidence/conditions-sets-098.md#c-fdeba5129a6cfaeb) · [缺口 G-dddb4ff58b516f68](../../evidence/gaps-sets-008.md#g-dddb4ff58b516f68) · [参数 P-094ffc8e7bffbfe6](../../evidence/parameters-sets-001.md#p-094ffc8e7bffbfe6) · [状态效果 S-5cc19b878e0b70bf](../../evidence/state_effects-sets-020.md#s-5cc19b878e0b70bf)

### path-062507

```text
(config)# do-exec test ipv6 rib prefix del <number:1..16> <prefix:dynamic> <address> <cr>
```

Handler ` RVA 0x1230CF80 `；selector ` 0 `；EOL ` RVA 0x357F0970 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f42682c60e97b62d](../../evidence/conditions-sets-094.md#c-f42682c60e97b62d) · [缺口 G-7e61500914191c1c](../../evidence/gaps-sets-005.md#g-7e61500914191c1c) · [参数 P-acc2a8881e66193c](../../evidence/parameters-sets-013.md#p-acc2a8881e66193c) · [状态效果 S-5cc19b878e0b70bf](../../evidence/state_effects-sets-020.md#s-5cc19b878e0b70bf)

### path-045776

```text
(config)# do-exec test ipv6 rib queue start <cr>
```

Handler ` RVA 0x1230B430 `；selector ` 0 `；EOL ` RVA 0x357EC420 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-155649a3af50aea7](../../evidence/conditions-sets-008.md#c-155649a3af50aea7) · [状态效果 S-90f1fb7f9b7ae43a](../../evidence/state_effects-sets-031.md#s-90f1fb7f9b7ae43a)

### path-045835

```text
(config)# do-exec test ipv6 rib suspend start <cr>
```

Handler ` RVA 0x1230B490 `；selector ` 0 `；EOL ` RVA 0x357EC780 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-155649a3af50aea7](../../evidence/conditions-sets-008.md#c-155649a3af50aea7) · [状态效果 S-0358f55d60cde49d](../../evidence/state_effects-sets-001.md#s-0358f55d60cde49d)

### path-061968

```text
(config)# do-exec test ipv6 rmap associate <string> <interface> <cr>
```

Handler ` RVA 0x118C0490 `；selector ` 0 `；EOL ` RVA 0x3559F648 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` rmap name to (dis)associate。

[条件 C-237c48fb485f3d06](../../evidence/conditions-sets-014.md#c-237c48fb485f3d06) · [缺口 G-65650b17e6d858a4](../../evidence/gaps-sets-004.md#g-65650b17e6d858a4) · [参数 P-52665bfba48ca87a](../../evidence/parameters-sets-007.md#p-52665bfba48ca87a) · [状态效果 S-66cf9e759d4de3d8](../../evidence/state_effects-sets-022.md#s-66cf9e759d4de3d8)

### path-053855

```text
(config)# do-exec test ipv6 rmap associate <string> local <cr>
```

Handler ` RVA 0x118C0490 `；selector ` 0 `；EOL ` RVA 0x3559F648 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` rmap name to (dis)associate。

[条件 C-dce18dac73d2d613](../../evidence/conditions-sets-085.md#c-dce18dac73d2d613) · [参数 P-ea229d8e07f52d10](../../evidence/parameters-sets-018.md#p-ea229d8e07f52d10) · [状态效果 S-75e3e2bedd0b34c8](../../evidence/state_effects-sets-025.md#s-75e3e2bedd0b34c8)

### path-053631

```text
(config)# do-exec test ipv6 rmap create <number:1..7> <string> <cr>
```

Handler ` RVA 0xE202AC0 `；selector ` 0 `；EOL ` RVA 0x3559CF80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Application: 1 - AAA；` string ` application specific string。

[条件 C-155649a3af50aea7](../../evidence/conditions-sets-008.md#c-155649a3af50aea7) · [参数 P-700266de357f47fd](../../evidence/parameters-sets-009.md#p-700266de357f47fd) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-053873

```text
(config)# do-exec test ipv6 rmap delete <string> <number:0..4294967295> <cr>
```

Handler ` RVA 0xE202FB0 `；selector ` 0 `；EOL ` RVA 0x3559EEE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle。

[条件 C-3da3f7c7f476935d](../../evidence/conditions-sets-024.md#c-3da3f7c7f476935d) · [参数 P-e1f9c2e256f45292](../../evidence/parameters-sets-017.md#p-e1f9c2e256f45292) · [状态效果 S-7aa80cee46c799bf](../../evidence/state_effects-sets-026.md#s-7aa80cee46c799bf)

### path-059802

```text
(config)# do-exec test ipv6 rmap delete <string> <number:0..4294967295> match acl <string> <cr>
```

Handler ` RVA 0x118BCAF0 `；selector ` 0 `；EOL ` RVA 0x3559D768 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` string ` acl name。

[条件 C-54893d9a658412db](../../evidence/conditions-sets-033.md#c-54893d9a658412db) · [参数 P-131b5c4417a1f1af](../../evidence/parameters-sets-002.md#p-131b5c4417a1f1af) · [状态效果 S-7aa80cee46c799bf](../../evidence/state_effects-sets-026.md#s-7aa80cee46c799bf)

### path-060050

```text
(config)# do-exec test ipv6 rmap delete <string> <number:0..4294967295> match length <number:0..2147483647> <number:0..2147483647> <cr>
```

Handler ` RVA 0xE2036F0 `；selector ` 0 `；EOL ` RVA 0x3559DA70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` unsigned_number ` Minimum packet length；` unsigned_number ` Maximum packet length。

[条件 C-54893d9a658412db](../../evidence/conditions-sets-033.md#c-54893d9a658412db) · [参数 P-43c97c6f77edf50d](../../evidence/parameters-sets-006.md#p-43c97c6f77edf50d) · [状态效果 S-7aa80cee46c799bf](../../evidence/state_effects-sets-026.md#s-7aa80cee46c799bf)

### path-059279

```text
(config)# do-exec test ipv6 rmap delete <string> <number:0..4294967295> set global <cr>
```

Handler ` RVA 0xE204CB0 `；selector ` 0 `；EOL ` RVA 0x3559E720 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle。

[条件 C-cab10ed150ee7567](../../evidence/conditions-sets-078.md#c-cab10ed150ee7567) · [参数 P-e1f9c2e256f45292](../../evidence/parameters-sets-017.md#p-e1f9c2e256f45292) · [状态效果 S-7aa80cee46c799bf](../../evidence/state_effects-sets-026.md#s-7aa80cee46c799bf)

### path-062616

```text
(config)# do-exec test ipv6 rmap delete <string> <number:0..4294967295> set interface <interface> <cr>
```

Handler ` RVA 0x118BD3B0 `；selector ` 0 `；EOL ` RVA 0x3559EA90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle。

[条件 C-2652efebcfe80f98](../../evidence/conditions-sets-015.md#c-2652efebcfe80f98) · [缺口 G-b6faf044e3dba0a4](../../evidence/gaps-sets-006.md#g-b6faf044e3dba0a4) · [参数 P-e127611f1cbf4d17](../../evidence/parameters-sets-017.md#p-e127611f1cbf4d17) · [状态效果 S-94626a38e0538bfc](../../evidence/state_effects-sets-031.md#s-94626a38e0538bfc)

### path-059809

```text
(config)# do-exec test ipv6 rmap delete <string> <number:0..4294967295> set next-hop <address> <cr>
```

Handler ` RVA 0x118BCDA0 `；selector ` 0 `；EOL ` RVA 0x3559DE00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` address ` IPv6 address of next-hop。

[条件 C-d2283e6ae4fff89a](../../evidence/conditions-sets-081.md#c-d2283e6ae4fff89a) · [参数 P-9c64443c07b0a179](../../evidence/parameters-sets-012.md#p-9c64443c07b0a179) · [状态效果 S-2d36694e8c37a746](../../evidence/state_effects-sets-010.md#s-2d36694e8c37a746)

### path-059818

```text
(config)# do-exec test ipv6 rmap delete <string> <number:0..4294967295> set precedence <number:0..7> <cr>
```

Handler ` RVA 0x118BD130 `；selector ` 0 `；EOL ` RVA 0x3559E1B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` unsigned_number ` Value of precedence。

[条件 C-cab10ed150ee7567](../../evidence/conditions-sets-078.md#c-cab10ed150ee7567) · [参数 P-ce115e51ed785080](../../evidence/parameters-sets-016.md#p-ce115e51ed785080) · [状态效果 S-7aa80cee46c799bf](../../evidence/state_effects-sets-026.md#s-7aa80cee46c799bf)

### path-059824

```text
(config)# do-exec test ipv6 rmap delete <string> <number:0..4294967295> set vrf <string> <cr>
```

Handler ` RVA 0xE204A00 `；selector ` 0 `；EOL ` RVA 0x3559E4A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` string ` VRF name。

[条件 C-cab10ed150ee7567](../../evidence/conditions-sets-078.md#c-cab10ed150ee7567) · [参数 P-0f25ae5261c5ab19](../../evidence/parameters-sets-002.md#p-0f25ae5261c5ab19) · [状态效果 S-7aa80cee46c799bf](../../evidence/state_effects-sets-026.md#s-7aa80cee46c799bf)

### path-053781

```text
(config)# do-exec test ipv6 rmap delete <string> permit <cr>
```

Handler ` RVA 0xE202DC0 `；selector ` 0 `；EOL ` RVA 0x3559F180 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` routemap tag。

[条件 C-54893d9a658412db](../../evidence/conditions-sets-033.md#c-54893d9a658412db) · [参数 P-afea805b9cc43465](../../evidence/parameters-sets-013.md#p-afea805b9cc43465) · [状态效果 S-830b23b7fd509436](../../evidence/state_effects-sets-028.md#s-830b23b7fd509436)

### path-046119

```text
(config)# do-exec test ipv6 rmap register <number:1..7> <cr>
```

Handler ` RVA 0xE2028D0 `；selector ` 0 `；EOL ` RVA 0x3559CBF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Application。

[条件 C-155649a3af50aea7](../../evidence/conditions-sets-008.md#c-155649a3af50aea7) · [参数 P-ffc4586fce516f90](../../evidence/parameters-sets-019.md#p-ffc4586fce516f90) · [状态效果 S-fe5ad0546e810dd6](../../evidence/state_effects-sets-054.md#s-fe5ad0546e810dd6)

### path-053663

```text
(config)# do-exec test ipv6 rmap remove <string> <number:1..7> <cr>
```

Handler ` RVA 0xE202C80 `；selector ` 0 `；EOL ` RVA 0x3559D2A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` application specific string；` unsigned_number ` Application: 1 - AAA。

[条件 C-155649a3af50aea7](../../evidence/conditions-sets-008.md#c-155649a3af50aea7) · [参数 P-6ee64968fd4901d6](../../evidence/parameters-sets-009.md#p-6ee64968fd4901d6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-045887

```text
(config)# do-exec test ipv6 static limit <number:0..32> <cr>
```

Handler ` RVA 0x12310D00 `；selector ` 0 `；EOL ` RVA 0x357F0F90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-155649a3af50aea7](../../evidence/conditions-sets-008.md#c-155649a3af50aea7) · [参数 P-f007846cc54b8f35](../../evidence/parameters-sets-018.md#p-f007846cc54b8f35) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-036406

```text
(config)# do-exec test ipv6 static policy <cr>
```

Handler ` RVA 0x12310CC0 `；selector ` 0 `；EOL ` RVA 0x357F0CA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-155649a3af50aea7](../../evidence/conditions-sets-008.md#c-155649a3af50aea7) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-037827

```text
(config)# do-exec test isis case <number:0..4294967295> <cr>
```

Handler ` RVA 0x10743F90 `；selector ` 4 `；EOL ` RVA 0x34B9ACE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` test number。

[条件 C-ff6e6c05c47f5f01](../../evidence/conditions-sets-098.md#c-ff6e6c05c47f5f01) · [参数 P-648cc8ff7d755148](../../evidence/parameters-sets-008.md#p-648cc8ff7d755148) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061445

```text
(config)# do-exec test isis case <number:0..4294967295> <interface> <cr>
```

Handler ` RVA 0x10743F90 `；selector ` 4 `；EOL ` RVA 0x34B9ACE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` test number。

[条件 C-fb227293c1e6d430](../../evidence/conditions-sets-097.md#c-fb227293c1e6d430) · [缺口 G-f88f15910f0bda41](../../evidence/gaps-sets-009.md#g-f88f15910f0bda41) · [参数 P-fca7330218061f69](../../evidence/parameters-sets-019.md#p-fca7330218061f69) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-037515

```text
(config)# do-exec test isis clear counters <cr>
```

Handler ` RVA 0x10743F90 `；selector ` 5 `；EOL ` RVA 0x34B792E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-030696

```text
(config)# do-exec test isis debug <cr>
```

Handler ` RVA 0x10743F90 `；selector ` 0 `；EOL ` RVA 0x34B78708 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-037541

```text
(config)# do-exec test isis ip address <cr>
```

Handler ` RVA 0x10743F90 `；selector ` 3 `；EOL ` RVA 0x34B78F58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-054298

```text
(config)# do-exec test isis lsp advertise lan-adj-sid <number:1..255> <cr>
```

Handler ` RVA 0x10743F90 `；selector ` 15 `；EOL ` RVA 0x34B9B8A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` number of items。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-555260a8b81f290e](../../evidence/parameters-sets-007.md#p-555260a8b81f290e) · [状态效果 S-a69daa4d4cd747ae](../../evidence/state_effects-sets-035.md#s-a69daa4d4cd747ae)

### path-038070

```text
(config)# do-exec test isis lsp build <cr>
```

Handler ` RVA 0x10743F90 `；selector ` 8 `；EOL ` RVA 0x34B9C870 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-037817

```text
(config)# do-exec test isis lsp id <cr>
```

Handler ` RVA 0x10743F90 `；selector ` 1 `；EOL ` RVA 0x34B9B520 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-047236

```text
(config)# do-exec test isis lsp non_pn_delay on <cr>
```

Handler ` RVA 0x10743F90 `；selector ` 13 `；EOL ` RVA 0x34B9C4E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-789410d58ba48864](../../evidence/state_effects-sets-026.md#s-789410d58ba48864)

### path-047215

```text
(config)# do-exec test isis lsp pn_delay on <cr>
```

Handler ` RVA 0x10743F90 `；selector ` 12 `；EOL ` RVA 0x34B9C188 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-e18259f9ff85e367](../../evidence/state_effects-sets-048.md#s-e18259f9ff85e367)

### path-038153

```text
(config)# do-exec test isis lsp purge <cr>
```

Handler ` RVA 0x10743F90 `；selector ` 9 `；EOL ` RVA 0x34B9D118 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-047346

```text
(config)# do-exec test isis lsp purge dr <cr>
```

Handler ` RVA 0x10743F90 `；selector ` 10 `；EOL ` RVA 0x34B9CC98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062042

```text
(config)# do-exec test isis lsp purge dr <interface> <cr>
```

Handler ` RVA 0x10743F90 `；selector ` 10 `；EOL ` RVA 0x34B9CC98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8a1e0b7dc56d5a6e](../../evidence/conditions-sets-053.md#c-8a1e0b7dc56d5a6e) · [缺口 G-ab3927d5113d2ea3](../../evidence/gaps-sets-006.md#g-ab3927d5113d2ea3) · [参数 P-dc0d6267cb42c9f0](../../evidence/parameters-sets-017.md#p-dc0d6267cb42c9f0) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-037970

```text
(config)# do-exec test isis lsp refresh <cr>
```

Handler ` RVA 0x10743F90 `；selector ` 11 `；EOL ` RVA 0x34B9BCF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-030726

```text
(config)# do-exec test isis nsap <cr>
```

Handler ` RVA 0x10743F90 `；selector ` 2 `；EOL ` RVA 0x34B78BF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-037550

```text
(config)# do-exec test isis show counters <cr>
```

Handler ` RVA 0x10743F90 `；selector ` 6 `；EOL ` RVA 0x34B795E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-030871

```text
(config)# do-exec test isis spf <cr>
```

Handler ` RVA 0x10743F90 `；selector ` 7 `；EOL ` RVA 0x34B9B0D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-037578

```text
(config)# do-exec test isis telemetry enable <cr>
```

Handler ` RVA 0x10743F90 `；selector ` 21 `；EOL ` RVA 0x34B798B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-bce26df56edc1120](../../evidence/state_effects-sets-040.md#s-bce26df56edc1120)

### path-058945

```text
(config)# do-exec test issu capability entry register <number:1..4294967295> <number:0..100> <string> <cr>
```

Handler ` RVA 0xD4C7970 `；selector ` 0 `；EOL ` RVA 0x33E62D08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` entity id；` unsigned_number ` cap entry id；` string ` Cap Type list ex: 1,3,4 - Comma needed。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-b7aee89a0684739a](../../evidence/parameters-sets-014.md#p-b7aee89a0684739a) · [状态效果 S-819ff393f7a9e855](../../evidence/state_effects-sets-027.md#s-819ff393f7a9e855)

### path-059660

```text
(config)# do-exec test issu capability group register <number:1..4294967295> <number:1..100> <number:0..1> <string> <cr>
```

Handler ` RVA 0xD4C7970 `；selector ` 0 `；EOL ` RVA 0x33E63100 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` entity id；` unsigned_number ` cap group id；` unsigned_number ` no_mandatory_entry 1=TRUE, 0=FALSE；` string ` Cap entry list ex: 1,3,4 - Comma needed。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-edb3c0f496cab6b9](../../evidence/parameters-sets-018.md#p-edb3c0f496cab6b9) · [状态效果 S-e0532f8681a07226](../../evidence/state_effects-sets-047.md#s-e0532f8681a07226)

### path-056889

```text
(config)# do-exec test issu capability type-list register <number:1..4294967295> <string> <cr>
```

Handler ` RVA 0xD4C7970 `；selector ` 0 `；EOL ` RVA 0x33E62930 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` entity id；` string ` Cap Type list ex: 1,3,4 - Comma needed。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-369daa5871e461d5](../../evidence/parameters-sets-005.md#p-369daa5871e461d5) · [状态效果 S-8964d6a88f69b2ea](../../evidence/state_effects-sets-029.md#s-8964d6a88f69b2ea)

### path-052305

```text
(config)# do-exec test issu client <number:1..9999> bits enable <cr>
```

Handler ` RVA 0xD4C7970 `；selector ` 0 `；EOL ` RVA 0x33E61080 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` client id。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-3ef334e0ec790657](../../evidence/parameters-sets-005.md#p-3ef334e0ec790657) · [状态效果 S-498becbf95a97d18](../../evidence/state_effects-sets-016.md#s-498becbf95a97d18)

### path-034555

```text
(config)# do-exec test issu client register <cr>
```

Handler ` RVA 0xD4C7970 `；selector ` 0 `；EOL ` RVA 0x33E61478 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-d1ec20e9416c90f4](../../evidence/state_effects-sets-044.md#s-d1ec20e9416c90f4)

### path-034426

```text
(config)# do-exec test issu distributed show <cr>
```

Handler ` RVA 0xD4C7970 `；selector ` 0 `；EOL ` RVA 0x33E60B18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-5bcf1588affd98e1](../../evidence/state_effects-sets-020.md#s-5bcf1588affd98e1)

### path-035042

```text
(config)# do-exec test issu divc no-test <cr>
```

Handler ` RVA 0xD4BFE40 `；selector ` 0 `；EOL ` RVA 0x33E66EA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-7289bd4a53d5695e](../../evidence/state_effects-sets-024.md#s-7289bd4a53d5695e)

### path-044371

```text
(config)# do-exec test issu entity register <number:0..4294967295> <cr>
```

Handler ` RVA 0xD4C7970 `；selector ` 0 `；EOL ` RVA 0x33E618C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` entity id。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-a8d135807cc9287b](../../evidence/parameters-sets-013.md#p-a8d135807cc9287b) · [状态效果 S-a0bc19e8d52083ee](../../evidence/state_effects-sets-034.md#s-a0bc19e8d52083ee)

### path-057000

```text
(config)# do-exec test issu injected calc_mtu <number:0..4294967295> <number:1..100> <number:1..100> <cr>
```

Handler ` RVA 0xD4BFC10 `；selector ` 0 `；EOL ` RVA 0x33E65928 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` session id；` unsigned_number ` message type；` unsigned_number ` negotiated version。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-853668705988955a](../../evidence/parameters-sets-010.md#p-853668705988955a) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-052492

```text
(config)# do-exec test issu injected capability <number:0..4294967295> <number:1..100> <cr>
```

Handler ` RVA 0xD4BFCF0 `；selector ` 0 `；EOL ` RVA 0x33E65298 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` session id；` unsigned_number ` capability entry id。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-393798d128e2709a](../../evidence/parameters-sets-005.md#p-393798d128e2709a) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-052513

```text
(config)# do-exec test issu injected comp_result <number:0..4294967295> <number:1..2> <cr>
```

Handler ` RVA 0xD4BFC80 `；selector ` 0 `；EOL ` RVA 0x33E655D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` session id；` unsigned_number ` compatible result。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-6361eb3e9623ecfb](../../evidence/parameters-sets-008.md#p-6361eb3e9623ecfb) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-058968

```text
(config)# do-exec test issu injected message <number:0..4294967295> <number:1..100> <number:1..100> <number:1..100> <cr>
```

Handler ` RVA 0xD4BFD60 `；selector ` 0 `；EOL ` RVA 0x33E64F60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` session id；` unsigned_number ` message type；` unsigned_number ` negotiated version；` unsigned_number ` message mtu。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-7510cad559f30d36](../../evidence/parameters-sets-009.md#p-7510cad559f30d36) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-044464

```text
(config)# do-exec test issu injected register <number:0..4294967295> <cr>
```

Handler ` RVA 0xD4BFDE0 `；selector ` 0 `；EOL ` RVA 0x33E64B98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` session id。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-0084d67a308f4e0e](../../evidence/parameters-sets-001.md#p-0084d67a308f4e0e) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-044431

```text
(config)# do-exec test issu lossless session setup <cr>
```

Handler ` RVA 0xD4BF540 `；selector ` 0 `；EOL ` RVA 0x33E634F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-bcc37f1a136609b5](../../evidence/state_effects-sets-040.md#s-bcc37f1a136609b5)

### path-058943

```text
(config)# do-exec test issu message group register <number:1..4294967295> <number:1..100> <string> <cr>
```

Handler ` RVA 0xD4C7970 `；selector ` 0 `；EOL ` RVA 0x33E62520 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` entity id；` unsigned_number ` msg group id；` string ` msg type list ex: 1,2,3 - Comma needed。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-5853af0f9184149a](../../evidence/parameters-sets-007.md#p-5853af0f9184149a) · [状态效果 S-8434048ead701abd](../../evidence/state_effects-sets-028.md#s-8434048ead701abd)

### path-059652

```text
(config)# do-exec test issu message type register <number:1..4294967295> <number:1..100> <number:1..5> <number:1..5> <cr>
```

Handler ` RVA 0xD4BF240 `；selector ` 0 `；EOL ` RVA 0x33E61F30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` entity id；` unsigned_number ` msg type；` unsigned_number ` low ver；` unsigned_number ` hi ver。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-c8d4fce5568ed841](../../evidence/parameters-sets-015.md#p-c8d4fce5568ed841) · [状态效果 S-07e63ca724db51c3](../../evidence/state_effects-sets-002.md#s-07e63ca724db51c3)

### path-059954

```text
(config)# do-exec test issu message type register <number:1..4294967295> <number:1..100> <number:1..5> <number:1..5> <string> <cr>
```

Handler ` RVA 0xD4BF1A0 `；selector ` 0 `；EOL ` RVA 0x33E61F08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` entity id；` unsigned_number ` msg type；` unsigned_number ` low ver；` unsigned_number ` hi ver；` string ` dummy version list, ex: 2,3,5 - Comma needed。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-5787eb47f94b9f1d](../../evidence/parameters-sets-007.md#p-5787eb47f94b9f1d) · [状态效果 S-07e63ca724db51c3](../../evidence/state_effects-sets-002.md#s-07e63ca724db51c3)

### path-034880

```text
(config)# do-exec test issu negative on <cr>
```

Handler ` RVA 0xD4C7970 `；selector ` 0 `；EOL ` RVA 0x33E66700 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-073e909ae2295249](../../evidence/state_effects-sets-002.md#s-073e909ae2295249)

### path-056987

```text
(config)# do-exec test issu nego-version config <number:1..4294967295> <number:1..100> <number:1..100> <cr>
```

Handler ` RVA 0xD4BF6C0 `；selector ` 0 `；EOL ` RVA 0x33E66400 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` session id；` unsigned_number ` Msg Type；` unsigned_number ` new negotiated version。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-84abe38d8cd95294](../../evidence/parameters-sets-010.md#p-84abe38d8cd95294) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-044497

```text
(config)# do-exec test issu negotiate <number:1..4294967295> <number:0..1> <cr>
```

Handler ` RVA 0xD4C7970 `；selector ` 0 `；EOL ` RVA 0x33E65CB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` session id；` unsigned_number ` domain id。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-e3a16036306ccf7a](../../evidence/parameters-sets-017.md#p-e3a16036306ccf7a) · [状态效果 S-7ba21e0926d4cce7](../../evidence/state_effects-sets-026.md#s-7ba21e0926d4cce7)

### path-034994

```text
(config)# do-exec test issu policy off <cr>
```

Handler ` RVA 0xD4C7970 `；selector ` 0 `；EOL ` RVA 0x33E66AD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-e861234bc9d295fc](../../evidence/state_effects-sets-049.md#s-e861234bc9d295fc)

### path-034776

```text
(config)# do-exec test issu session ipc <cr>
```

Handler ` RVA 0xD4C7970 `；selector ` 0 `；EOL ` RVA 0x33E63998 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-a154983c04ab3795](../../evidence/state_effects-sets-034.md#s-a154983c04ab3795)

### path-056938

```text
(config)# do-exec test issu shared message_session unregister <number:1..4294967295> <number:0..1> <cr>
```

Handler ` RVA 0xD4BFA00 `；selector ` 0 `；EOL ` RVA 0x33E64010 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` session id；` unsigned_number ` domain id。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-15f9d1914836288c](../../evidence/parameters-sets-002.md#p-15f9d1914836288c) · [状态效果 S-4321edc6e734f2c9](../../evidence/state_effects-sets-015.md#s-4321edc6e734f2c9)

### path-044521

```text
(config)# do-exec test issu shared nego_session register <cr>
```

Handler ` RVA 0xD4BFB40 `；selector ` 0 `；EOL ` RVA 0x33E64428 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-691aaa8d0146d2be](../../evidence/state_effects-sets-022.md#s-691aaa8d0146d2be)

### path-056952

```text
(config)# do-exec test issu shared negotiate <number:1..4294967295> <number:1..4294967295> <number:0..1> <cr>
```

Handler ` RVA 0xD4BF7A0 `；selector ` 0 `；EOL ` RVA 0x33E64818 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number `  message session id；` unsigned_number `  negotiation session id；` unsigned_number ` domain id。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-002060df6e92087d](../../evidence/parameters-sets-001.md#p-002060df6e92087d) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-052491

```text
(config)# do-exec test issu transform <number:1..4294967295> <number:1..100> <number:0..1> <cr>
```

Handler ` RVA 0xD4C7970 `；selector ` 0 `；EOL ` RVA 0x33E66040 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` session id；` unsigned_number ` Msg Type；` unsigned_number ` domain id。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-5bac2e1d7c4c7095](../../evidence/parameters-sets-007.md#p-5bac2e1d7c4c7095) · [状态效果 S-acf2c09d22558aeb](../../evidence/state_effects-sets-037.md#s-acf2c09d22558aeb)

### path-027616

```text
(config)# do-exec test l2protocol-forward <cr>
```

Handler ` RVA 0x15FD9700 `；selector ` 32 `；EOL ` RVA 0x35E87788 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-aeee0c70d98a45eb](../../evidence/conditions-sets-068.md#c-aeee0c70d98a45eb) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-060713

```text
(config)# do-exec test l2protocol-forward <interface> <cr>
```

Handler ` RVA 0x15FD93E0 `；selector ` 32 `；EOL ` RVA 0x35E87760 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c3ad2107f185256a](../../evidence/conditions-sets-076.md#c-c3ad2107f185256a) · [缺口 G-7bb168c8bbfcb9de](../../evidence/gaps-sets-005.md#g-7bb168c8bbfcb9de) · [参数 P-ea0e6cb5a4df3956](../../evidence/parameters-sets-018.md#p-ea0e6cb5a4df3956) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-027614

```text
(config)# do-exec test l2protocol-tunnel <cr>
```

Handler ` RVA 0x15FD9700 `；selector ` 31 `；EOL ` RVA 0x35E871A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ddbd1287a634e214](../../evidence/conditions-sets-085.md#c-ddbd1287a634e214) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-060712

```text
(config)# do-exec test l2protocol-tunnel <interface> <cr>
```

Handler ` RVA 0x15FD93E0 `；selector ` 31 `；EOL ` RVA 0x35E87178 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f14f71fab2ddee72](../../evidence/conditions-sets-093.md#c-f14f71fab2ddee72) · [缺口 G-5fa858f690b7f4c6](../../evidence/gaps-sets-004.md#g-5fa858f690b7f4c6) · [参数 P-a539e5e2eae972e5](../../evidence/parameters-sets-013.md#p-a539e5e2eae972e5) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-040000

```text
(config)# do-exec test lacp disable insert-seq-num <cr>
```

Handler ` RVA 0xC8D36F0 `；selector ` 0 `；EOL ` RVA 0x33B15208 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-310dc4a10d334d02](../../evidence/state_effects-sets-011.md#s-310dc4a10d334d02)

### path-039946

```text
(config)# do-exec test lacp disable recv <cr>
```

Handler ` RVA 0xC8D3680 `；selector ` 0 `；EOL ` RVA 0x33B14F60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-310dc4a10d334d02](../../evidence/state_effects-sets-011.md#s-310dc4a10d334d02)

### path-039883

```text
(config)# do-exec test lacp disable send <cr>
```

Handler ` RVA 0xC8D3610 `；selector ` 0 `；EOL ` RVA 0x33B14CB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-310dc4a10d334d02](../../evidence/state_effects-sets-011.md#s-310dc4a10d334d02)

### path-040045

```text
(config)# do-exec test lacp enable insert-seq-num <cr>
```

Handler ` RVA 0xC8D36F0 `；selector ` 0 `；EOL ` RVA 0x33B15A78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-5dca285a636ece09](../../evidence/state_effects-sets-020.md#s-5dca285a636ece09)

### path-039996

```text
(config)# do-exec test lacp enable recv <cr>
```

Handler ` RVA 0xC8D3680 `；selector ` 0 `；EOL ` RVA 0x33B157D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-5dca285a636ece09](../../evidence/state_effects-sets-020.md#s-5dca285a636ece09)

### path-039941

```text
(config)# do-exec test lacp enable send <cr>
```

Handler ` RVA 0xC8D3610 `；selector ` 0 `；EOL ` RVA 0x33B15528 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-5dca285a636ece09](../../evidence/state_effects-sets-020.md#s-5dca285a636ece09)

### path-048958

```text
(config)# do-exec test lacp multi-chassis iccp-version <number:0..65535> <cr>
```

Handler ` RVA 0xC960530 `；selector ` 0 `；EOL ` RVA 0x33B38290 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Version in ICCP connection TLV。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-1fc392fcc1ad0e26](../../evidence/parameters-sets-003.md#p-1fc392fcc1ad0e26) · [状态效果 S-4af2f930c8ffb70d](../../evidence/state_effects-sets-016.md#s-4af2f930c8ffb70d)

### path-061560

```text
(config)# do-exec test lacp sync-bit set <interface> <cr>
```

Handler ` RVA 0xC8D33C0 `；selector ` 0 `；EOL ` RVA 0x33B16328 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e9dd2b9be28fd31c](../../evidence/conditions-sets-090.md#c-e9dd2b9be28fd31c) · [缺口 G-1fc8a6c7c11b148c](../../evidence/gaps-sets-002.md#g-1fc8a6c7c11b148c) · [参数 P-a7ffa45be4f41a3b](../../evidence/parameters-sets-013.md#p-a7ffa45be4f41a3b) · [状态效果 S-f845f5800b08a2a9](../../evidence/state_effects-sets-053.md#s-f845f5800b08a2a9)

### path-062889

```text
(config)# do-exec test lacp sync-bit switch <interface> <interface> <cr>
```

Handler ` RVA 0xC8D34C0 `；selector ` 0 `；EOL ` RVA 0x33B15F30 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8a8f60aeb5b15d7c](../../evidence/conditions-sets-054.md#c-8a8f60aeb5b15d7c) · [缺口 G-272b31ada0f209f8](../../evidence/gaps-sets-002.md#g-272b31ada0f209f8) · [参数 P-c5ac7ba310175862](../../evidence/parameters-sets-015.md#p-c5ac7ba310175862) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-055249

```text
(config)# do-exec test lacp timer wait fast default <cr>
```

Handler ` RVA 0xC8D32D0 `；selector ` 0 `；EOL ` RVA 0x33B166F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-a738ab68951a435e](../../evidence/state_effects-sets-035.md#s-a738ab68951a435e)

### path-061246

```text
(config)# do-exec test license smart factory-reset clear all <cr>
```

Handler ` RVA 0xBB47540 `；selector ` 0 `；EOL ` RVA 0x33856CA0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c14aef8a7dafe2d6](../../evidence/conditions-sets-075.md#c-c14aef8a7dafe2d6) · [缺口 G-35063cd6f80afd0d](../../evidence/gaps-sets-002.md#g-35063cd6f80afd0d) · [状态效果 S-a632e645ff2dadc6](../../evidence/state_effects-sets-035.md#s-a632e645ff2dadc6)

### path-035379

```text
(config)# do-exec test license smart tech-support <cr>
```

Handler ` RVA 0xBB47540 `；selector ` 0 `；EOL ` RVA 0x33856CA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-df6437d35f0df1cc](../../evidence/conditions-sets-086.md#c-df6437d35f0df1cc) · [状态效果 S-60dde7ce47fcc3a4](../../evidence/state_effects-sets-021.md#s-60dde7ce47fcc3a4)

### path-035016

```text
(config)# do-exec test lim proximity-db enable <cr>
```

Handler ` RVA 0xC9242D0 `；selector ` 1 `；EOL ` RVA 0x33B1E4A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0875a4850114d37f](../../evidence/conditions-sets-004.md#c-0875a4850114d37f) · [状态效果 S-f38c3d09a9a8d173](../../evidence/state_effects-sets-051.md#s-f38c3d09a9a8d173)

### path-062018

```text
(config)# do-exec test mac-table-mibs get-addr-info vlan <number:dynamic> <address> <cr>
```

Handler ` RVA 0x15E77C10 `；selector ` 17 `；EOL ` RVA 0x35E4FC90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` VLAN Id value；` address ` 48 bit mac address。

[条件 C-8e2a7c0b1b41f26e](../../evidence/conditions-sets-055.md#c-8e2a7c0b1b41f26e) · [缺口 G-884350b12689720b](../../evidence/gaps-sets-005.md#g-884350b12689720b) · [参数 P-f819bcc27cd2479e](../../evidence/parameters-sets-018.md#p-f819bcc27cd2479e) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061450

```text
(config)# do-exec test mac-table-mibs get-aging vlan <number:dynamic> <cr>
```

Handler ` RVA 0x15E77C10 `；selector ` 14 `；EOL ` RVA 0x35E4F1F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` VLAN Id vlaue。

[条件 C-9e403428c88990e3](../../evidence/conditions-sets-061.md#c-9e403428c88990e3) · [缺口 G-56d51312f2024c84](../../evidence/gaps-sets-003.md#g-56d51312f2024c84) · [参数 P-cd8a702da351f59c](../../evidence/parameters-sets-016.md#p-cd8a702da351f59c) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061471

```text
(config)# do-exec test mac-table-mibs get-igmp-status vlan <number:dynamic> <cr>
```

Handler ` RVA 0x15E77C10 `；selector ` 23 `；EOL ` RVA 0x35E51308 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` VLAN Id value。

[条件 C-c2f5e857304d541a](../../evidence/conditions-sets-075.md#c-c2f5e857304d541a) · [缺口 G-6794891567c77f78](../../evidence/gaps-sets-004.md#g-6794891567c77f78) · [参数 P-37177cb18223b496](../../evidence/parameters-sets-005.md#p-37177cb18223b496) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061468

```text
(config)# do-exec test mac-table-mibs get-learned-discards vlan <number:dynamic> <cr>
```

Handler ` RVA 0x15E77C10 `；selector ` 22 `；EOL ` RVA 0x35E50FC8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` VLAN Id value。

[条件 C-e2647e59f78e2533](../../evidence/conditions-sets-087.md#c-e2647e59f78e2533) · [缺口 G-e5f0dec673e6be26](../../evidence/gaps-sets-008.md#g-e5f0dec673e6be26) · [参数 P-de85b204d9d90a05](../../evidence/parameters-sets-017.md#p-de85b204d9d90a05) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061455

```text
(config)# do-exec test mac-table-mibs get-next-addr vlan <number:dynamic> <cr>
```

Handler ` RVA 0x15E77C10 `；selector ` 16 `；EOL ` RVA 0x35E4F908 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` VLAN Id value。

[条件 C-71c47af53f3e5f6d](../../evidence/conditions-sets-044.md#c-71c47af53f3e5f6d) · [缺口 G-f1d74e17fe7b29bb](../../evidence/gaps-sets-008.md#g-f1d74e17fe7b29bb) · [参数 P-dea280cc3bb04afc](../../evidence/parameters-sets-017.md#p-dea280cc3bb04afc) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062347

```text
(config)# do-exec test mac-table-mibs get-next-staticaddr vlan <number:dynamic> port <number:0..128> <cr>
```

Handler ` RVA 0x15E77C10 `；selector ` 18 `；EOL ` RVA 0x35E50050 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` VLAN Id value；` unsigned_number ` Port Index。

[条件 C-d0644928ae375bba](../../evidence/conditions-sets-080.md#c-d0644928ae375bba) · [缺口 G-d017013f3c09b903](../../evidence/gaps-sets-007.md#g-d017013f3c09b903) · [参数 P-9bfa3904934995f3](../../evidence/parameters-sets-012.md#p-9bfa3904934995f3) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062341

```text
(config)# do-exec test mac-table-mibs set-aging vlan <number:dynamic> aging-time <number:0..1000000> <cr>
```

Handler ` RVA 0x15E77C10 `；selector ` 15 `；EOL ` RVA 0x35E4F5C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` VLAN Id value；` unsigned_number ` Aging Time Value。

[条件 C-c396a023abbc855d](../../evidence/conditions-sets-075.md#c-c396a023abbc855d) · [缺口 G-21cac691862d1024](../../evidence/gaps-sets-002.md#g-21cac691862d1024) · [参数 P-df2cbee7cad77c52](../../evidence/parameters-sets-017.md#p-df2cbee7cad77c52) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062355

```text
(config)# do-exec test mac-table-mibs set-cpu-addr <address> vlan <number:dynamic> <number:1..2> <cr>
```

Handler ` RVA 0x15E77C10 `；selector ` 24 `；EOL ` RVA 0x35E516A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` 48 bit mac address；` unsigned_number_dynamic ` VLAN Id value；` unsigned_number ` Add/Del Addr。

[条件 C-5cf36718610bb9de](../../evidence/conditions-sets-036.md#c-5cf36718610bb9de) · [缺口 G-7b004d3552174b95](../../evidence/gaps-sets-005.md#g-7b004d3552174b95) · [参数 P-e22713caaaf5ba98](../../evidence/parameters-sets-017.md#p-e22713caaaf5ba98) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062531

```text
(config)# do-exec test mac-table-mibs set-delete-status vlan <number:dynamic> port <number:0..128> <address> <cr>
```

Handler ` RVA 0x15E77C10 `；selector ` 20 `；EOL ` RVA 0x35E50878 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` VLAN Id value；` unsigned_number ` Port Index；` address ` 48 bit mac address。

[条件 C-bd7f2a321cc8fe59](../../evidence/conditions-sets-073.md#c-bd7f2a321cc8fe59) · [缺口 G-212f9ad1fa331ae1](../../evidence/gaps-sets-002.md#g-212f9ad1fa331ae1) · [参数 P-ca3a06e86fe14a13](../../evidence/parameters-sets-015.md#p-ca3a06e86fe14a13) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062532

```text
(config)# do-exec test mac-table-mibs set-invalid-status vlan <number:dynamic> port <number:0..128> <address> <cr>
```

Handler ` RVA 0x15E77C10 `；selector ` 21 `；EOL ` RVA 0x35E50C88 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` VLAN Id value；` unsigned_number ` Port Index；` address ` 48 bit mac address。

[条件 C-ed6fd294e03ede3d](../../evidence/conditions-sets-092.md#c-ed6fd294e03ede3d) · [缺口 G-cabb78a09e6ce200](../../evidence/gaps-sets-007.md#g-cabb78a09e6ce200) · [参数 P-c4d90c82d0dc9ce4](../../evidence/parameters-sets-015.md#p-c4d90c82d0dc9ce4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062530

```text
(config)# do-exec test mac-table-mibs set-permanent-status vlan <number:dynamic> port <number:0..128> <address> <cr>
```

Handler ` RVA 0x15E77C10 `；selector ` 19 `；EOL ` RVA 0x35E50468 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` VLAN Id value；` unsigned_number ` Port Index；` address ` 48 bit mac address。

[条件 C-9131966ece39d417](../../evidence/conditions-sets-056.md#c-9131966ece39d417) · [缺口 G-d1b0c674efc6b2be](../../evidence/gaps-sets-007.md#g-d1b0c674efc6b2be) · [参数 P-640d72e8c68ba40c](../../evidence/parameters-sets-008.md#p-640d72e8c68ba40c) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-060165

```text
(config)# do-exec test mdns browse regtype <string> domain <string> periodicity <number:0..4294967295> interface <number:0..4294967295> <cr>
```

Handler ` RVA 0x142AA8B0 `；selector ` 0 `；EOL ` RVA 0x35D12E90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Specify in this form _servicename._protocol；` string ` Specify Domain or 0 for NULL；` unsigned_number ` Specify Periodicity in seconds；` unsigned_number ` Specify interface Index。

[条件 C-e6b11f3ca6b60f83](../../evidence/conditions-sets-089.md#c-e6b11f3ca6b60f83) · [参数 P-a5635059931d6d21](../../evidence/parameters-sets-013.md#p-a5635059931d6d21) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-046122

```text
(config)# do-exec test mdns browse stop <number:1..4294967295> <cr>
```

Handler ` RVA 0x142AA9D0 `；selector ` 0 `；EOL ` RVA 0x35D13180 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Enter Request ID value。

[条件 C-7e3902f9c0bef28a](../../evidence/conditions-sets-049.md#c-7e3902f9c0bef28a) · [参数 P-f5e43b71021fa86d](../../evidence/parameters-sets-018.md#p-f5e43b71021fa86d) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-030444

```text
(config)# do-exec test mdns cache <cr>
```

Handler ` RVA 0x142ABBE0 `；selector ` 1 `；EOL ` RVA 0x35D14068 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bb76b8eb5b0cf5dd](../../evidence/conditions-sets-072.md#c-bb76b8eb5b0cf5dd) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-060874

```text
(config)# do-exec test mdns intf-wdraw <interface> <cr>
```

Handler ` RVA 0x142AC590 `；selector ` 10 `；EOL ` RVA 0x35D12428 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ee0ee44fb1eccb1b](../../evidence/conditions-sets-092.md#c-ee0ee44fb1eccb1b) · [缺口 G-428884fbd90f64a2](../../evidence/gaps-sets-003.md#g-428884fbd90f64a2) · [参数 P-46d1f66fe55d85f9](../../evidence/parameters-sets-006.md#p-46d1f66fe55d85f9) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-057590

```text
(config)# do-exec test mdns resolve host <string> interface <number:0..4294967295> <cr>
```

Handler ` RVA 0x142AAC10 `；selector ` 0 `；EOL ` RVA 0x35D13A58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Specify HostName to Resolve；` unsigned_number ` Specify Interface Index。

[条件 C-c62e197fc7d0055f](../../evidence/conditions-sets-076.md#c-c62e197fc7d0055f) · [参数 P-0467657afa55ba03](../../evidence/parameters-sets-001.md#p-0467657afa55ba03) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-060166

```text
(config)# do-exec test mdns resolve service <string> regtype <string> domain <string> interface <number:0..4294967295> <cr>
```

Handler ` RVA 0x142AAAF0 `；selector ` 0 `；EOL ` RVA 0x35D13670 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Service Instance Name；` string ` Specify in this form _servicename._protocol；` string ` Specify Domain name or 0 for NULL；` unsigned_number ` Specify Interface Index。

[条件 C-0c6cade41cd725aa](../../evidence/conditions-sets-005.md#c-0c6cade41cd725aa) · [参数 P-7a2f34b5b2da854f](../../evidence/parameters-sets-010.md#p-7a2f34b5b2da854f) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-030073

```text
(config)# do-exec test mdns resync <cr>
```

Handler ` RVA 0x142AC590 `；selector ` 9 `；EOL ` RVA 0x35D12098 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3f52af221f1d2920](../../evidence/conditions-sets-025.md#c-3f52af221f1d2920) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-036401

```text
(config)# do-exec test mdns srv-enum <number:0..1> <cr>
```

Handler ` RVA 0x142AC590 `；selector ` 11 `；EOL ` RVA 0x35D11E10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Enter 0 for clear and 1 for request。

[条件 C-6c2e6f89a5ff3c4e](../../evidence/conditions-sets-042.md#c-6c2e6f89a5ff3c4e) · [参数 P-79203c4ca1832bbb](../../evidence/parameters-sets-009.md#p-79203c4ca1832bbb) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-030149

```text
(config)# do-exec test mdns start <cr>
```

Handler ` RVA 0x142AC590 `；selector ` 0 `；EOL ` RVA 0x35D126E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1e602975eaca0eb1](../../evidence/conditions-sets-012.md#c-1e602975eaca0eb1) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-030181

```text
(config)# do-exec test mdns stop <cr>
```

Handler ` RVA 0x142AC590 `；selector ` 1 `；EOL ` RVA 0x35D12990 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f39ee03118cf0b29](../../evidence/conditions-sets-094.md#c-f39ee03118cf0b29) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-057558

```text
(config)# do-exec test mdns update bssid <address> client-mac <address> <cr>
```

Handler ` RVA 0x142ABAD0 `；selector ` 1 `；EOL ` RVA 0x35D14590 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` 48 bit mac address；` address ` 48 bit mac address。

[条件 C-fbff4f7f4bec12be](../../evidence/conditions-sets-097.md#c-fbff4f7f4bec12be) · [参数 P-54086fa71b463a2f](../../evidence/parameters-sets-007.md#p-54086fa71b463a2f) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-053662

```text
(config)# do-exec test mdns update query-pak bssid-mac <address> <cr>
```

Handler ` RVA 0x142ABA60 `；selector ` 1 `；EOL ` RVA 0x35D148A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` 48 bit mac address。

[条件 C-5715c0ac941bb7e4](../../evidence/conditions-sets-034.md#c-5715c0ac941bb7e4) · [参数 P-cb5e5912b30e3de5](../../evidence/parameters-sets-015.md#p-cb5e5912b30e3de5) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-026618

```text
(config)# do-exec test memory <cr>
```

Handler ` RVA 0xE8F44F0 `；selector ` 0 `；EOL ` RVA 0x3433F0E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-687391d529d2b295](../../evidence/conditions-sets-040.md#c-687391d529d2b295) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-057013

```text
(config)# do-exec test memory allocate processor <number:0..4294967294> <number:0..4294967294> <number:0..4294967294> <cr>
```

Handler ` RVA 0xD79CC10 `；selector ` 0 `；EOL ` RVA 0x33EE8290 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` alignment；` unsigned_number ` number of allocations；` unsigned_number ` size of each allocated block。

[条件 C-687391d529d2b295](../../evidence/conditions-sets-040.md#c-687391d529d2b295) · [参数 P-493f9cb9de8c2f52](../../evidence/parameters-sets-006.md#p-493f9cb9de8c2f52) · [状态效果 S-2c60d1a2ed2a8d20](../../evidence/state_effects-sets-010.md#s-2c60d1a2ed2a8d20)

### path-061267

```text
(config)# do-exec test memory chunk lock <?general_pointer_number_action@55558943eb28> <cr>
```

Handler ` RVA 0xD79B8E0 `；selector ` 0 `；EOL ` RVA 0x33EEAB90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5fbbe7294519f4af](../../evidence/conditions-sets-037.md#c-5fbbe7294519f4af) · [缺口 G-3e3424abb7c82a29](../../evidence/gaps-sets-003.md#g-3e3424abb7c82a29) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061270

```text
(config)# do-exec test memory chunk refcount <?general_pointer_number_action@55558943ee20> <cr>
```

Handler ` RVA 0xD79B950 `；selector ` 0 `；EOL ` RVA 0x33EEAE60 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5fbbe7294519f4af](../../evidence/conditions-sets-037.md#c-5fbbe7294519f4af) · [缺口 G-894740e478c6950d](../../evidence/gaps-sets-005.md#g-894740e478c6950d) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-034942

```text
(config)# do-exec test memory create dangling-reference <cr>
```

Handler ` RVA 0xD79C2F0 `；selector ` 0 `；EOL ` RVA 0x33EE8D28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-687391d529d2b295](../../evidence/conditions-sets-040.md#c-687391d529d2b295) · [状态效果 S-8e1602041082e4b3](../../evidence/state_effects-sets-030.md#s-8e1602041082e4b3)

### path-057027

```text
(config)# do-exec test memory create leak type1 <number:28..4294967295> <number:1..4294967295> <cr>
```

Handler ` RVA 0xD79C5D0 `；selector ` 0 `；EOL ` RVA 0x33EE9470 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` size of blocks to leak；` unsigned_number ` number of blocks to leak。

[条件 C-687391d529d2b295](../../evidence/conditions-sets-040.md#c-687391d529d2b295) · [参数 P-e7de55dec44fbd77](../../evidence/parameters-sets-017.md#p-e7de55dec44fbd77) · [状态效果 S-41de1eb8e2aec396](../../evidence/state_effects-sets-014.md#s-41de1eb8e2aec396)

### path-062475

```text
(config)# do-exec test memory create leak type1 chunk <?general_pointer_number_action@55558943d098> <number:1..4294967295> <cr>
```

Handler ` RVA 0xD79C7E0 `；selector ` 0 `；EOL ` RVA 0x33EE9150 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` number of chunk elements to leak。

[条件 C-687391d529d2b295](../../evidence/conditions-sets-040.md#c-687391d529d2b295) · [缺口 G-c792ef09578ce8ea](../../evidence/gaps-sets-007.md#g-c792ef09578ce8ea) · [参数 P-d9d3b29a49c1919e](../../evidence/parameters-sets-016.md#p-d9d3b29a49c1919e) · [状态效果 S-41de1eb8e2aec396](../../evidence/state_effects-sets-014.md#s-41de1eb8e2aec396)

### path-061868

```text
(config)# do-exec test memory delay-sibling-free <?general_pointer_number_action@55558943d778> <number:0..1> <number:0..1> <cr>
```

Handler ` RVA 0xD79BFE0 `；selector ` 0 `；EOL ` RVA 0x33EE9878 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` 0 for disabling and 1 for enabling；` unsigned_number ` 0 not to suspend and 1 to suspend while freeing the siblings。

[条件 C-687391d529d2b295](../../evidence/conditions-sets-040.md#c-687391d529d2b295) · [缺口 G-3ea430db00582304](../../evidence/gaps-sets-003.md#g-3ea430db00582304) · [参数 P-ddd211b15a703d3f](../../evidence/parameters-sets-017.md#p-ddd211b15a703d3f) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061255

```text
(config)# do-exec test memory destroy chunk <?general_pointer_number_action@55558943dc08> <cr>
```

Handler ` RVA 0xD79C970 `；selector ` 0 `；EOL ` RVA 0x33EE9C70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-687391d529d2b295](../../evidence/conditions-sets-040.md#c-687391d529d2b295) · [缺口 G-518a8b54e36141fe](../../evidence/gaps-sets-003.md#g-518a8b54e36141fe) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061254

```text
(config)# do-exec test memory destroy dangling-reference <?general_pointer_number_action@55558943db68> <cr>
```

Handler ` RVA 0xD79C2F0 `；selector ` 0 `；EOL ` RVA 0x33EE8D28 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-687391d529d2b295](../../evidence/conditions-sets-040.md#c-687391d529d2b295) · [缺口 G-bd47bd03979ee71a](../../evidence/gaps-sets-007.md#g-bd47bd03979ee71a) · [状态效果 S-35741078524d77d7](../../evidence/state_effects-sets-012.md#s-35741078524d77d7)

### path-035144

```text
(config)# do-exec test memory history <number:1..60> <cr>
```

Handler ` RVA 0xD79B850 `；selector ` 0 `；EOL ` RVA 0x33EEA5B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Period of history collection in minutes。

[条件 C-5fbbe7294519f4af](../../evidence/conditions-sets-037.md#c-5fbbe7294519f4af) · [参数 P-bff5968e13295850](../../evidence/parameters-sets-015.md#p-bff5968e13295850) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-028615

```text
(config)# do-exec test memory nvram-multibus <cr>
```

Handler ` RVA 0xE8F44F0 `；selector ` 0 `；EOL ` RVA 0x3433EE50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-687391d529d2b295](../../evidence/conditions-sets-040.md#c-687391d529d2b295) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061874

```text
(config)# do-exec test memory overflow <?general_pointer_number_action@55558943dfe8> <number:0..4294967294> <number:0..4294967294> <cr>
```

Handler ` RVA 0xD79CA50 `；selector ` 0 `；EOL ` RVA 0x33EEA0E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` size of the corruption in words；` unsigned_number ` corruption pattern。

[条件 C-41ee15b6e34bcc62](../../evidence/conditions-sets-026.md#c-41ee15b6e34bcc62) · [缺口 G-428e2243ef5fda03](../../evidence/gaps-sets-003.md#g-428e2243ef5fda03) · [参数 P-dae1cb7bff83826c](../../evidence/parameters-sets-016.md#p-dae1cb7bff83826c) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-060799

```text
(config)# do-exec test memory transfer <?general_pointer_number_action@55558943c6e0> <cr>
```

Handler ` RVA 0xD79CC10 `；selector ` 0 `；EOL ` RVA 0x33EE8290 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-687391d529d2b295](../../evidence/conditions-sets-040.md#c-687391d529d2b295) · [缺口 G-c83e41a6aa9aa77e](../../evidence/gaps-sets-007.md#g-c83e41a6aa9aa77e) · [状态效果 S-5c51ca617f82e09f](../../evidence/state_effects-sets-020.md#s-5c51ca617f82e09f)

### path-060221

```text
(config)# do-exec test mfib cb-support IPv4 add group <address> source <address> vrf <number:0..100> intf <number:0..255> <cr>
```

Handler ` RVA 0x11957C90 `；selector ` 1 `；EOL ` RVA 0x355AFA00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` group address；` address ` source address；` unsigned_number ` vrf id；` unsigned_number ` if_number。

[条件 C-44764a37c29fe8c0](../../evidence/conditions-sets-027.md#c-44764a37c29fe8c0) · [参数 P-f3f238ba8bd70d5c](../../evidence/parameters-sets-018.md#p-f3f238ba8bd70d5c) · [状态效果 S-10da497fa06dcbad](../../evidence/state_effects-sets-004.md#s-10da497fa06dcbad)

### path-060222

```text
(config)# do-exec test mfib cb-support IPv6 add group <address> source <address> vrf <number:0..100> intf <number:0..255> <cr>
```

Handler ` RVA 0x11957C90 `；selector ` 2 `；EOL ` RVA 0x355AFFE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` group address；` address ` source address；` unsigned_number ` vrf id；` unsigned_number ` if_number。

[条件 C-44764a37c29fe8c0](../../evidence/conditions-sets-027.md#c-44764a37c29fe8c0) · [参数 P-b9f20fac51ecc555](../../evidence/parameters-sets-014.md#p-b9f20fac51ecc555) · [状态效果 S-65b78c4fff178982](../../evidence/state_effects-sets-022.md#s-65b78c4fff178982)

### path-030924

```text
(config)# do-exec test mfib channel <cr>
```

Handler ` RVA 0x11667890 `；selector ` 0 `；EOL ` RVA 0x35524680 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-962eb28d68dcd55c](../../evidence/conditions-sets-058.md#c-962eb28d68dcd55c) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-060942

```text
(config)# do-exec test mfib channel <number:dynamic> <cr>
```

Handler ` RVA 0x11667890 `；selector ` 0 `；EOL ` RVA 0x35524680 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` linecard slot number。

[条件 C-d38f4acf0a652700](../../evidence/conditions-sets-082.md#c-d38f4acf0a652700) · [缺口 G-c4520b36bf37f288](../../evidence/gaps-sets-007.md#g-c4520b36bf37f288) · [参数 P-3f890285bd586914](../../evidence/parameters-sets-005.md#p-3f890285bd586914) · [状态效果 S-6c627f7c2fed3df9](../../evidence/state_effects-sets-023.md#s-6c627f7c2fed3df9)

### path-030742

```text
(config)# do-exec test mfib enable <cr>
```

Handler ` RVA 0x11949710 `；selector ` 0 `；EOL ` RVA 0x355AC7B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8391b26b34510a34](../../evidence/conditions-sets-051.md#c-8391b26b34510a34) · [状态效果 S-2fa9e39c856cc43b](../../evidence/state_effects-sets-011.md#s-2fa9e39c856cc43b)

### path-061454

```text
(config)# do-exec test mfib epoch new <?option@55558aafa690> <cr>
```

Handler ` RVA 0x118FAFB0 `；selector ` 0 `；EOL ` RVA 0x355A6730 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ce893d65e1912b22](../../evidence/conditions-sets-080.md#c-ce893d65e1912b22) · [缺口 G-f56498c9e9ed6be6](../../evidence/gaps-sets-008.md#g-f56498c9e9ed6be6) · [状态效果 S-8350ac2db8d0a66b](../../evidence/state_effects-sets-028.md#s-8350ac2db8d0a66b)

### path-037862

```text
(config)# do-exec test mfib epoch new <cr>
```

Handler ` RVA 0x118FAFB0 `；selector ` 0 `；EOL ` RVA 0x355A6730 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-eabfc2c1c969fe0d](../../evidence/conditions-sets-091.md#c-eabfc2c1c969fe0d) · [状态效果 S-41cca5bbbf887f6d](../../evidence/state_effects-sets-014.md#s-41cca5bbbf887f6d)

### path-030875

```text
(config)# do-exec test mfib mrib <cr>
```

Handler ` RVA 0x1196AC30 `；selector ` 0 `；EOL ` RVA 0x355AF460 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-44764a37c29fe8c0](../../evidence/conditions-sets-027.md#c-44764a37c29fe8c0) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-060931

```text
(config)# do-exec test mfib mrib <number:dynamic> <cr>
```

Handler ` RVA 0x1196AC30 `；selector ` 0 `；EOL ` RVA 0x355AF460 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` error duration (milliseconds)。

[条件 C-a244562e997be320](../../evidence/conditions-sets-063.md#c-a244562e997be320) · [缺口 G-6aeaa43c969bb7b7](../../evidence/gaps-sets-004.md#g-6aeaa43c969bb7b7) · [参数 P-b3d6337a30e0851e](../../evidence/parameters-sets-014.md#p-b3d6337a30e0851e) · [状态效果 S-5b09d83f71aca1fc](../../evidence/state_effects-sets-020.md#s-5b09d83f71aca1fc)

### path-030948

```text
(config)# do-exec test mfib reload <cr>
```

Handler ` RVA 0x11667B00 `；selector ` 0 `；EOL ` RVA 0x35524B30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e5aade789d45dbb5](../../evidence/conditions-sets-089.md#c-e5aade789d45dbb5) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-060941

```text
(config)# do-exec test mfib reload <number:dynamic> <cr>
```

Handler ` RVA 0x11667B00 `；selector ` 0 `；EOL ` RVA 0x35524B30 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` linecard slot number。

[条件 C-abe53ef2fac55a70](../../evidence/conditions-sets-066.md#c-abe53ef2fac55a70) · [缺口 G-b2ca273f657109d7](../../evidence/gaps-sets-006.md#g-b2ca273f657109d7) · [参数 P-147ef2ff33894e7e](../../evidence/parameters-sets-002.md#p-147ef2ff33894e7e) · [状态效果 S-cc3a7e3576bcdf3d](../../evidence/state_effects-sets-043.md#s-cc3a7e3576bcdf3d)

### path-029637

```text
(config)# do-exec test mgd-timer watch <cr>
```

Handler ` RVA 0xD7AD830 `；selector ` 0 `；EOL ` RVA 0x33EF0C08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-c9408e68dbc505c4](../../evidence/state_effects-sets-043.md#s-c9408e68dbc505c4)

### path-062394

```text
(config)# do-exec test mka linksec start interface <interface> preshared <cr>
```

Handler ` RVA 0x16085270 `；selector ` 8 `；EOL ` RVA 0x35EBB090 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-fb6723a9fb029257](../../evidence/conditions-sets-097.md#c-fb6723a9fb029257) · [缺口 G-c3a4d69e2c4b6087](../../evidence/gaps-sets-007.md#g-c3a4d69e2c4b6087) · [参数 P-b23d7e6994cdff39](../../evidence/parameters-sets-014.md#p-b23d7e6994cdff39) · [状态效果 S-3795ce976fad88c5](../../evidence/state_effects-sets-012.md#s-3795ce976fad88c5)

### path-039987

```text
(config)# do-exec test mka macsec-sim off <cr>
```

Handler ` RVA 0x16085270 `；selector ` 1 `；EOL ` RVA 0x35EB9D78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-dd5d51dff14980c2](../../evidence/conditions-sets-085.md#c-dd5d51dff14980c2) · [状态效果 S-81ff7f7edaf384cc](../../evidence/state_effects-sets-028.md#s-81ff7f7edaf384cc)

### path-049072

```text
(config)# do-exec test mka message-number initial-value <number:1..4294967295> <cr>
```

Handler ` RVA 0x16085270 `；selector ` 2 `；EOL ` RVA 0x35EBA128 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` 32-bit Message Number (default = 1)。

[条件 C-0e36ad791f5199a4](../../evidence/conditions-sets-006.md#c-0e36ad791f5199a4) · [参数 P-2cc60459240682de](../../evidence/parameters-sets-004.md#p-2cc60459240682de) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-049113

```text
(config)# do-exec test mka message-number window-size <number:0..4294967295> <cr>
```

Handler ` RVA 0x16085270 `；selector ` 5 `；EOL ` RVA 0x35EBA3F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` MN Window Size - # of MKPDUs (default = 0, off)。

[条件 C-0e36ad791f5199a4](../../evidence/conditions-sets-006.md#c-0e36ad791f5199a4) · [参数 P-76ba54810b928371](../../evidence/parameters-sets-009.md#p-76ba54810b928371) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-049156

```text
(config)# do-exec test mka packet-number initial-value <number:0..4294967295> <cr>
```

Handler ` RVA 0x16085270 `；selector ` 6 `；EOL ` RVA 0x35EBABB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` 32-bit Packet Number (default = 1, PendingPNExhaustion at 3221225472)。

[条件 C-0e36ad791f5199a4](../../evidence/conditions-sets-006.md#c-0e36ad791f5199a4) · [参数 P-5f2a7ac5cf4b91bf](../../evidence/parameters-sets-008.md#p-5f2a7ac5cf4b91bf) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062909

```text
(config)# do-exec test mka sak-rekey ckn <hex-string> interface <interface> <cr>
```

Handler ` RVA 0x16085270 `；selector ` 7 `；EOL ` RVA 0x35EBA838 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` hexstring ` 128-bit Hexadecimal CKN。

[条件 C-010ca8779a817a93](../../evidence/conditions-sets-001.md#c-010ca8779a817a93) · [缺口 G-1a10bfb2d00b04c4](../../evidence/gaps-sets-001.md#g-1a10bfb2d00b04c4) · [参数 P-08bbea5392940b87](../../evidence/parameters-sets-001.md#p-08bbea5392940b87) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-031362

```text
(config)# do-exec test mock btrace <cr>
```

Handler ` RVA 0x1653EB30 `；selector ` 4 `；EOL ` RVA 0x35FA0940 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a758693af815a517](../../evidence/conditions-sets-065.md#c-a758693af815a517) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-031413

```text
(config)# do-exec test mock chasfs <cr>
```

Handler ` RVA 0x1653EB30 `；selector ` 6 `；EOL ` RVA 0x35FA0E90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5c5a31e2e409d5d6](../../evidence/conditions-sets-036.md#c-5c5a31e2e409d5d6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-031382

```text
(config)# do-exec test mock chassis <cr>
```

Handler ` RVA 0x1653EB30 `；selector ` 5 `；EOL ` RVA 0x35FA0BE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-478553e14dbd2539](../../evidence/conditions-sets-028.md#c-478553e14dbd2539) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-031477

```text
(config)# do-exec test mock crypto <cr>
```

Handler ` RVA 0x1653EB30 `；selector ` 18 `；EOL ` RVA 0x35FA1930 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6f29d59c80112ff4](../../evidence/conditions-sets-043.md#c-6f29d59c80112ff4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-031427

```text
(config)# do-exec test mock cyan <cr>
```

Handler ` RVA 0x1653EB30 `；selector ` 7 `；EOL ` RVA 0x35FA1138 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-eef0a01449389c31](../../evidence/conditions-sets-092.md#c-eef0a01449389c31) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-031338

```text
(config)# do-exec test mock ei <cr>
```

Handler ` RVA 0x1653EB30 `；selector ` 8 `；EOL ` RVA 0x35FA0698 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a99faa64739f377a](../../evidence/conditions-sets-065.md#c-a99faa64739f377a) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-038390

```text
(config)# do-exec test mock infra enqueue <cr>
```

Handler ` RVA 0x1653EB30 `；selector ` 1 `；EOL ` RVA 0x35F9F7E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f07c66f4f31683c4](../../evidence/conditions-sets-093.md#c-f07c66f4f31683c4) · [状态效果 S-966b5ceecd2d3a75](../../evidence/state_effects-sets-032.md#s-966b5ceecd2d3a75)

### path-031292

```text
(config)# do-exec test mock ipc <cr>
```

Handler ` RVA 0x1653EB30 `；selector ` 11 `；EOL ` RVA 0x35FA0148 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c3ad160a58a0442b](../../evidence/conditions-sets-076.md#c-c3ad160a58a0442b) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-031266

```text
(config)# do-exec test mock mcp <cr>
```

Handler ` RVA 0x1653EB30 `；selector ` 2 `；EOL ` RVA 0x35F9FEA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f5de2f34f1177ce3](../../evidence/conditions-sets-095.md#c-f5de2f34f1177ce3) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-031319

```text
(config)# do-exec test mock misc <cr>
```

Handler ` RVA 0x1653EB30 `；selector ` 3 `；EOL ` RVA 0x35FA03F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1684677513a6c990](../../evidence/conditions-sets-009.md#c-1684677513a6c990) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-039047

```text
(config)# do-exec test mock overlayfs system-call <cr>
```

Handler ` RVA 0x1653EB30 `；selector ` 20 `；EOL ` RVA 0x35FA1EC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fbb70f28ff9e9aa1](../../evidence/conditions-sets-097.md#c-fbb70f28ff9e9aa1) · [状态效果 S-e31e6534bf6e1076](../../evidence/state_effects-sets-048.md#s-e31e6534bf6e1076)

### path-031458

```text
(config)# do-exec test mock real <cr>
```

Handler ` RVA 0x1653EB30 `；selector ` 9 `；EOL ` RVA 0x35FA1688 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-af921d3f03ebd3dc](../../evidence/conditions-sets-068.md#c-af921d3f03ebd3dc) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-031239

```text
(config)# do-exec test mock system <cr>
```

Handler ` RVA 0x1653EB30 `；selector ` 17 `；EOL ` RVA 0x35F9FBF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1361ca0ee2f133b6](../../evidence/conditions-sets-008.md#c-1361ca0ee2f133b6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-031445

```text
(config)# do-exec test mock tdl <cr>
```

Handler ` RVA 0x1653EB30 `；selector ` 10 `；EOL ` RVA 0x35FA13E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ca441ac90ac4a059](../../evidence/conditions-sets-078.md#c-ca441ac90ac4a059) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-031498

```text
(config)# do-exec test mock vaarg <cr>
```

Handler ` RVA 0x1653EB30 `；selector ` 19 `；EOL ` RVA 0x35FA1BD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-692039b231158d53](../../evidence/conditions-sets-041.md#c-692039b231158d53) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-048158

```text
(config)# do-exec test monitor clear config lock <cr>
```

Handler ` RVA 0xE4CE1F0 `；selector ` 0 `；EOL ` RVA 0x342CFCF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-030806

```text
(config)# do-exec test mrib disable <cr>
```

Handler ` RVA 0x1190F470 `；selector ` 0 `；EOL ` RVA 0x355A7AF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c2e6d5847a9b8347](../../evidence/conditions-sets-075.md#c-c2e6d5847a9b8347) · [状态效果 S-99344f1d5c959554](../../evidence/state_effects-sets-033.md#s-99344f1d5c959554)

### path-061482

```text
(config)# do-exec test mrib ip set <prefix:dynamic> <cr>
```

Handler ` RVA 0x1190F470 `；selector ` 0 `；EOL ` RVA 0x35376868 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` Group IP address/prefix length。

[条件 C-f31a09ec1f2bdb9a](../../evidence/conditions-sets-094.md#c-f31a09ec1f2bdb9a) · [缺口 G-78a7c487772b4f16](../../evidence/gaps-sets-005.md#g-78a7c487772b4f16) · [参数 P-2504edde6ede94b3](../../evidence/parameters-sets-003.md#p-2504edde6ede94b3) · [状态效果 S-4eded26a54cd877a](../../evidence/state_effects-sets-017.md#s-4eded26a54cd877a)

### path-037912

```text
(config)# do-exec test mrib ip stop <cr>
```

Handler ` RVA 0x1190F470 `；selector ` 0 `；EOL ` RVA 0x35376868 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4e4d94fe48ab7d0a](../../evidence/conditions-sets-031.md#c-4e4d94fe48ab7d0a) · [状态效果 S-4e4e0fe46cf34f7d](../../evidence/state_effects-sets-017.md#s-4e4e0fe46cf34f7d)

### path-061478

```text
(config)# do-exec test mrib ipv6 set <prefix:dynamic> <cr>
```

Handler ` RVA 0x1190F470 `；selector ` 0 `；EOL ` RVA 0x35540A50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` Group IP address/prefix length。

[条件 C-30fb05c8e529d30d](../../evidence/conditions-sets-019.md#c-30fb05c8e529d30d) · [缺口 G-f5990bffc57a8a82](../../evidence/gaps-sets-008.md#g-f5990bffc57a8a82) · [参数 P-824300904f0082a0](../../evidence/parameters-sets-010.md#p-824300904f0082a0) · [状态效果 S-972ec5327dbcb7f2](../../evidence/state_effects-sets-032.md#s-972ec5327dbcb7f2)

### path-037878

```text
(config)# do-exec test mrib ipv6 stop <cr>
```

Handler ` RVA 0x1190F470 `；selector ` 0 `；EOL ` RVA 0x35540A50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7040c83f84fac2a4](../../evidence/conditions-sets-043.md#c-7040c83f84fac2a4) · [状态效果 S-4203e61cc661cb3d](../../evidence/state_effects-sets-014.md#s-4203e61cc661cb3d)

### path-059319

```text
(config)# do-exec test mvpn ipv4 leaf-ad-recv add <address> <address> <address> <cr>
```

Handler ` RVA 0xF963F30 `；selector ` 0 `；EOL ` RVA 0x34790B08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Leaf A-D Route Key Source address；` address ` Leaf A-D Route Key Group address；` address ` Leaf A-D Originating IP address。

[条件 C-8c5641a18797689a](../../evidence/conditions-sets-054.md#c-8c5641a18797689a) · [参数 P-e7edaa477d6f924d](../../evidence/parameters-sets-017.md#p-e7edaa477d6f924d) · [状态效果 S-2e3e89c2d000e849](../../evidence/state_effects-sets-010.md#s-2e3e89c2d000e849)

### path-046948

```text
(config)# do-exec test mvpn ipv4 spt-only disable <cr>
```

Handler ` RVA 0xF963F30 `；selector ` 2 `；EOL ` RVA 0x347910B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-95ee4499abae09e7](../../evidence/conditions-sets-058.md#c-95ee4499abae09e7) · [状态效果 S-97063c6c1d4dfd74](../../evidence/state_effects-sets-032.md#s-97063c6c1d4dfd74)

### path-046910

```text
(config)# do-exec test mvpn ipv4 spt-only enable <cr>
```

Handler ` RVA 0xF963F30 `；selector ` 1 `；EOL ` RVA 0x34790E10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cf7c1e2ec741c8a8](../../evidence/conditions-sets-080.md#c-cf7c1e2ec741c8a8) · [状态效果 S-97063c6c1d4dfd74](../../evidence/state_effects-sets-032.md#s-97063c6c1d4dfd74)

### path-059327

```text
(config)# do-exec test mvpn ipv6 leaf-ad-recv add <address> <address> <address> <cr>
```

Handler ` RVA 0xF963F30 `；selector ` 0 `；EOL ` RVA 0x347916C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Leaf A-D Route Key Source address；` address ` Leaf A-D Route Key Group address；` address ` Leaf A-D Originating IP address。

[条件 C-d06722cfa05bc8f6](../../evidence/conditions-sets-080.md#c-d06722cfa05bc8f6) · [参数 P-2d64e798f1d53ea9](../../evidence/parameters-sets-004.md#p-2d64e798f1d53ea9) · [状态效果 S-3004df7d3908685d](../../evidence/state_effects-sets-011.md#s-3004df7d3908685d)

### path-046970

```text
(config)# do-exec test mvpn ipv6 spt-only disable <cr>
```

Handler ` RVA 0xF963F30 `；selector ` 2 `；EOL ` RVA 0x34791C70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e58e8f3d0772129a](../../evidence/conditions-sets-089.md#c-e58e8f3d0772129a) · [状态效果 S-f8c8eb19fc15c9b5](../../evidence/state_effects-sets-053.md#s-f8c8eb19fc15c9b5)

### path-046939

```text
(config)# do-exec test mvpn ipv6 spt-only enable <cr>
```

Handler ` RVA 0xF963F30 `；selector ` 1 `；EOL ` RVA 0x347919C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-efbb0a5413fa7fe3](../../evidence/conditions-sets-093.md#c-efbb0a5413fa7fe3) · [状态效果 S-f8c8eb19fc15c9b5](../../evidence/state_effects-sets-053.md#s-f8c8eb19fc15c9b5)

### path-035138

```text
(config)# do-exec test mvrp enable <number:0..1> <cr>
```

Handler ` RVA 0xC96A0D0 `；selector ` 2 `；EOL ` RVA 0x33B3ACD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Enable - 1, Disable - 0。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-2b2af8342a3221a3](../../evidence/parameters-sets-004.md#p-2b2af8342a3221a3) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-044806

```text
(config)# do-exec test mvrp joinin <number:1..4094> <number:1..4094> <cr>
```

Handler ` RVA 0xC96A0D0 `；selector ` 1 `；EOL ` RVA 0x33B3AA08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Starting VLAN；` unsigned_number ` VLAN count。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-347f484921822044](../../evidence/parameters-sets-004.md#p-347f484921822044) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-044764

```text
(config)# do-exec test mvrp new <number:1..4094> <number:1..4094> <cr>
```

Handler ` RVA 0xC96A0D0 `；selector ` 0 `；EOL ` RVA 0x33B3A6D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Starting VLAN；` unsigned_number ` VLAN count。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-47e3eaebeb4262d6](../../evidence/parameters-sets-006.md#p-47e3eaebeb4262d6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-029317

```text
(config)# do-exec test natmode suppress <cr>
```

Handler ` RVA 0xCF73670 `；selector ` 0 `；EOL ` RVA 0x33D44630 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-a095d3eed72fb8e3](../../evidence/state_effects-sets-034.md#s-a095d3eed72fb8e3)

### path-031652

```text
(config)# do-exec test netconf-agent history <cr>
```

Handler ` RVA 0xF3BDEF0 `；selector ` 1 `；EOL ` RVA 0x3462AA78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-031678

```text
(config)# do-exec test netconf-agent summary <cr>
```

Handler ` RVA 0xF3BDEF0 `；selector ` 3 `；EOL ` RVA 0x3462AD20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-030641

```text
(config)# do-exec test ngdns config <cr>
```

Handler ` RVA 0xD177360 `；selector ` 0 `；EOL ` RVA 0x33DA53C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e46bb5e8be877e78](../../evidence/conditions-sets-088.md#c-e46bb5e8be877e78) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-037174

```text
(config)# do-exec test ngdns lookup <string> <cr>
```

Handler ` RVA 0xD177DF0 `；selector ` 0 `；EOL ` RVA 0x33DA5878 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` lookup name。

[条件 C-e46bb5e8be877e78](../../evidence/conditions-sets-088.md#c-e46bb5e8be877e78) · [参数 P-decc2673888888d4](../../evidence/parameters-sets-017.md#p-decc2673888888d4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-037013

```text
(config)# do-exec test ngdns periodic dump <cr>
```

Handler ` RVA 0xD177180 `；selector ` 0 `；EOL ` RVA 0x33DA4720 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e46bb5e8be877e78](../../evidence/conditions-sets-088.md#c-e46bb5e8be877e78) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-060052

```text
(config)# do-exec test ngdns periodic register fqdn-name <string> type both module-id <number:1..3> <cr>
```

Handler ` RVA 0xD176ED0 `；selector ` 0 `；EOL ` RVA 0x33DA4368 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Specify FQDN；` unsigned_number ` module-id。

[条件 C-e46bb5e8be877e78](../../evidence/conditions-sets-088.md#c-e46bb5e8be877e78) · [参数 P-ed5b72c7cd03d32e](../../evidence/parameters-sets-018.md#p-ed5b72c7cd03d32e) · [状态效果 S-6cf159e09fa28a3b](../../evidence/state_effects-sets-023.md#s-6cf159e09fa28a3b)

### path-039779

```text
(config)# do-exec test ngiosd process-isolation start <cr>
```

Handler ` RVA 0x1653B780 `；selector ` 0 `；EOL ` RVA 0x35F9EE48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-9c8ad2218026dbcf](../../evidence/state_effects-sets-033.md#s-9c8ad2218026dbcf)

### path-048826

```text
(config)# do-exec test ngiosd simulation prepare-failure enable <cr>
```

Handler ` RVA 0x1653B5E0 `；selector ` 0 `；EOL ` RVA 0x35F9E6E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-90c11b1779c61d99](../../evidence/state_effects-sets-031.md#s-90c11b1779c61d99)

### path-048896

```text
(config)# do-exec test ngiosd simulation prepare-pass enable <cr>
```

Handler ` RVA 0x1653B520 `；selector ` 0 `；EOL ` RVA 0x35F9EA80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-5af7e5c13daef096](../../evidence/state_effects-sets-020.md#s-5af7e5c13daef096)

### path-039718

```text
(config)# do-exec test ngiosd simulation start <cr>
```

Handler ` RVA 0x1653B6A0 `；selector ` 0 `；EOL ` RVA 0x35F9E378 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-06c03771044dc35d](../../evidence/state_effects-sets-002.md#s-06c03771044dc35d)

### path-027373

```text
(config)# do-exec test nhrp event <number:0..1500> <cr>
```

Handler ` RVA 0x108D66C0 `；selector ` 8 `；EOL ` RVA 0x34BEAEE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` event code。

[条件 C-a45af3aa13ad14d5](../../evidence/conditions-sets-063.md#c-a45af3aa13ad14d5) · [参数 P-6c57de9d403a368b](../../evidence/parameters-sets-009.md#p-6c57de9d403a368b) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062986

```text
(config)# do-exec test nhrp redirect interface <interface> <?ipv4orv6_addr_action@55558a13efe0> <prefix:dynamic> <cr>
```

Handler ` RVA 0x108D66C0 `；selector ` 7 `；EOL ` RVA 0x34BEB060 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` IP address/&lt;length&gt; of destination, eg:192.168.0.0/16。

[条件 C-e2986571f2611a0d](../../evidence/conditions-sets-087.md#c-e2986571f2611a0d) · [缺口 G-f34972516f0c31ac](../../evidence/gaps-sets-008.md#g-f34972516f0c31ac) · [参数 P-4d6fd10b9bc76322](../../evidence/parameters-sets-006.md#p-4d6fd10b9bc76322) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-031900

```text
(config)# do-exec test notify <string> <cr>
```

Handler ` RVA 0x15A6CE70 `；selector ` 0 `；EOL ` RVA 0x35DE3AB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Virtual-service name。

[条件 C-bdb6be6e80307689](../../evidence/conditions-sets-073.md#c-bdb6be6e80307689) · [参数 P-bb63f77282b0e6a2](../../evidence/parameters-sets-014.md#p-bb63f77282b0e6a2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-047863

```text
(config)# do-exec test nvram <string> clear remote-lock <cr>
```

Handler ` RVA 0xD620830 `；selector ` 1 `；EOL ` RVA 0x33EB0A58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` URL for Nvram filesystem。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-465a9fec902c71c5](../../evidence/parameters-sets-006.md#p-465a9fec902c71c5) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-038856

```text
(config)# do-exec test nvram <string> explicit-lock <cr>
```

Handler ` RVA 0xD620830 `；selector ` 0 `；EOL ` RVA 0x33EB0CE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` URL for Nvram filesystem。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-465a9fec902c71c5](../../evidence/parameters-sets-006.md#p-465a9fec902c71c5) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-038898

```text
(config)# do-exec test nvram <string> initialize <cr>
```

Handler ` RVA 0xD620830 `；selector ` 2 `；EOL ` RVA 0x33EB0F90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` URL for Nvram filesystem。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-465a9fec902c71c5](../../evidence/parameters-sets-006.md#p-465a9fec902c71c5) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-058039

```text
(config)# do-exec test odb client <number:1..256> add-static-tlv type <number:0..65535> <cr>
```

Handler ` RVA 0x12414A30 `；selector ` 2 `；EOL ` RVA 0x35856F38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Client handle；` unsigned_number ` TLV type。

[条件 C-65c960ae397cdeca](../../evidence/conditions-sets-039.md#c-65c960ae397cdeca) · [参数 P-4937c32f8d4b15b3](../../evidence/parameters-sets-006.md#p-4937c32f8d4b15b3) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-047532

```text
(config)# do-exec test odb client <number:1..256> deregister <cr>
```

Handler ` RVA 0x12414A30 `；selector ` 1 `；EOL ` RVA 0x35856BE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Client handle。

[条件 C-bd0d4f42fd52a202](../../evidence/conditions-sets-073.md#c-bd0d4f42fd52a202) · [参数 P-9dd44be07c481a6e](../../evidence/parameters-sets-012.md#p-9dd44be07c481a6e) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-060206

```text
(config)# do-exec test odb client <number:1..256> row <number:0..4294967295> <number:0..4294967295> add-tlv type <number:0..65535> value <string> <cr>
```

Handler ` RVA 0x12414A30 `；selector ` 8 `；EOL ` RVA 0x358585E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Client handle；` unsigned_number ` Higher 32 bits of record handle；` unsigned_number ` Lower 32 bits of record handle；` unsigned_number ` TLV type；` string ` TLV value。

[条件 C-3719a4adf19f9b4e](../../evidence/conditions-sets-021.md#c-3719a4adf19f9b4e) · [参数 P-3761b49542bab2b5](../../evidence/parameters-sets-005.md#p-3761b49542bab2b5) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-059379

```text
(config)# do-exec test odb client <number:1..256> row <number:0..4294967295> <number:0..4294967295> delete <cr>
```

Handler ` RVA 0x12414A30 `；selector ` 7 `；EOL ` RVA 0x35858208 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Client handle；` unsigned_number ` Higher 32 bits of record handle；` unsigned_number ` Lower 32 bits of record handle。

[条件 C-5e3eda88e891c3c4](../../evidence/conditions-sets-037.md#c-5e3eda88e891c3c4) · [参数 P-cbbc12b169c74bfe](../../evidence/parameters-sets-015.md#p-cbbc12b169c74bfe) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-060076

```text
(config)# do-exec test odb client <number:1..256> row <number:0..4294967295> <number:0..4294967295> notify subscribe change <cr>
```

Handler ` RVA 0x12414A30 `；selector ` 9 `；EOL ` RVA 0x35858930 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Client handle；` unsigned_number ` Higher 32 bits of record handle；` unsigned_number ` Lower 32 bits of record handle。

[条件 C-3fc22bb34f143f45](../../evidence/conditions-sets-025.md#c-3fc22bb34f143f45) · [参数 P-cbbc12b169c74bfe](../../evidence/parameters-sets-015.md#p-cbbc12b169c74bfe) · [状态效果 S-705afe73d3b718d8](../../evidence/state_effects-sets-024.md#s-705afe73d3b718d8)

### path-060177

```text
(config)# do-exec test odb client <number:1..256> table <number:1..65534> add-row type <number:0..65535> value <string> <cr>
```

Handler ` RVA 0x12414A30 `；selector ` 6 `；EOL ` RVA 0x35857A20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Client handle；` unsigned_number ` Table id；` unsigned_number ` TLV type；` string ` TLV value。

[条件 C-8280f73aebce65a8](../../evidence/conditions-sets-051.md#c-8280f73aebce65a8) · [参数 P-339759b930726c8c](../../evidence/parameters-sets-004.md#p-339759b930726c8c) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-058048

```text
(config)# do-exec test odb client <number:1..256> table <number:1..65534> delete <cr>
```

Handler ` RVA 0x12414A30 `；selector ` 4 `；EOL ` RVA 0x35857648 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Client handle；` unsigned_number ` Table id。

[条件 C-0594cc0f76363c8c](../../evidence/conditions-sets-003.md#c-0594cc0f76363c8c) · [参数 P-f95d9efa001e6a73](../../evidence/parameters-sets-019.md#p-f95d9efa001e6a73) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-059862

```text
(config)# do-exec test odb client <number:1..256> table <number:1..65534> notify subscribe add <cr>
```

Handler ` RVA 0x12414A30 `；selector ` 5 `；EOL ` RVA 0x35857D70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Client handle；` unsigned_number ` Table id。

[条件 C-7de68de12eb84937](../../evidence/conditions-sets-049.md#c-7de68de12eb84937) · [参数 P-f95d9efa001e6a73](../../evidence/parameters-sets-019.md#p-f95d9efa001e6a73) · [状态效果 S-0e91dd74e79d4f97](../../evidence/state_effects-sets-003.md#s-0e91dd74e79d4f97)

### path-054513

```text
(config)# do-exec test odb client <number:1..256> table create <cr>
```

Handler ` RVA 0x12414A30 `；selector ` 3 `；EOL ` RVA 0x358572C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Client handle。

[条件 C-1035e1208b6509d2](../../evidence/conditions-sets-006.md#c-1035e1208b6509d2) · [参数 P-9dd44be07c481a6e](../../evidence/parameters-sets-012.md#p-9dd44be07c481a6e) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-047489

```text
(config)# do-exec test odb client register <string> <cr>
```

Handler ` RVA 0x12414A30 `；selector ` 0 `；EOL ` RVA 0x35856920 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Client name。

[条件 C-eada2de200bdc128](../../evidence/conditions-sets-091.md#c-eada2de200bdc128) · [参数 P-13828cb53228f29f](../../evidence/parameters-sets-002.md#p-13828cb53228f29f) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-047584

```text
(config)# do-exec test onep cli uninstall <string> <cr>
```

Handler ` RVA 0x13A82E40 `；selector ` 0 `；EOL ` RVA 0x35CAA6E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Configuration Domain。

[条件 C-aca8c656e44e8d48](../../evidence/conditions-sets-067.md#c-aca8c656e44e8d48) · [参数 P-6b00482f66f10d6d](../../evidence/parameters-sets-008.md#p-6b00482f66f10d6d) · [状态效果 S-5cc6edf49653d53b](../../evidence/state_effects-sets-020.md#s-5cc6edf49653d53b)

### path-031384

```text
(config)# do-exec test onep ctx_reg <cr>
```

Handler ` RVA 0x13A858B0 `；selector ` 0 `；EOL ` RVA 0x35CABFC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cbd2d4ca9bdda82a](../../evidence/conditions-sets-078.md#c-cbd2d4ca9bdda82a) · [状态效果 S-316778a6c777072a](../../evidence/state_effects-sets-011.md#s-316778a6c777072a)

### path-038807

```text
(config)# do-exec test onep if_ctx_event enable <cr>
```

Handler ` RVA 0x13A85820 `；selector ` 0 `；EOL ` RVA 0x35CAC308 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c1e0595157b699b1](../../evidence/conditions-sets-075.md#c-c1e0595157b699b1) · [状态效果 S-b523243b59dda501](../../evidence/state_effects-sets-038.md#s-b523243b59dda501)

### path-038470

```text
(config)# do-exec test onep internal enable <cr>
```

Handler ` RVA 0x13A82DA0 `；selector ` 0 `；EOL ` RVA 0x35CAA9D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-fe7fe148f3535b6e](../../evidence/state_effects-sets-054.md#s-fe7fe148f3535b6e)

### path-038612

```text
(config)# do-exec test onep thrift list <cr>
```

Handler ` RVA 0x13A863B0 `；selector ` 0 `；EOL ` RVA 0x35CAADE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c667348fe5b32643](../../evidence/conditions-sets-076.md#c-c667348fe5b32643) · [状态效果 S-5256e44730437386](../../evidence/state_effects-sets-018.md#s-5256e44730437386)

### path-061494

```text
(config)# do-exec test onep timing api <?option@55558b1ff1d0> <cr>
```

Handler ` RVA 0x13A86300 `；selector ` 0 `；EOL ` RVA 0x35CAB210 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b426c790022f88e1](../../evidence/conditions-sets-070.md#c-b426c790022f88e1) · [缺口 G-e77c4547d82b75c0](../../evidence/gaps-sets-008.md#g-e77c4547d82b75c0) · [状态效果 S-5cc6edf49653d53b](../../evidence/state_effects-sets-020.md#s-5cc6edf49653d53b)

### path-038684

```text
(config)# do-exec test onep version disable <cr>
```

Handler ` RVA 0x13A86260 `；selector ` 0 `；EOL ` RVA 0x35CAB5B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f0b2d46f709f2a07](../../evidence/conditions-sets-093.md#c-f0b2d46f709f2a07) · [状态效果 S-5cc6edf49653d53b](../../evidence/state_effects-sets-020.md#s-5cc6edf49653d53b)

### path-047699

```text
(config)# do-exec test onep version disable exact <cr>
```

Handler ` RVA 0x13A86210 `；selector ` 0 `；EOL ` RVA 0x35CAB588 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f0b2d46f709f2a07](../../evidence/conditions-sets-093.md#c-f0b2d46f709f2a07) · [状态效果 S-5cc6edf49653d53b](../../evidence/state_effects-sets-020.md#s-5cc6edf49653d53b)

### path-038660

```text
(config)# do-exec test onep version enable <cr>
```

Handler ` RVA 0x13A862B0 `；selector ` 0 `；EOL ` RVA 0x35CABA80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f0b2d46f709f2a07](../../evidence/conditions-sets-093.md#c-f0b2d46f709f2a07) · [状态效果 S-5cc6edf49653d53b](../../evidence/state_effects-sets-020.md#s-5cc6edf49653d53b)

### path-031363

```text
(config)# do-exec test onep xdt_buginf <cr>
```

Handler ` RVA 0x13A84B00 `；selector ` 0 `；EOL ` RVA 0x35CABD18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a860982fc8a9eb83](../../evidence/conditions-sets-065.md#c-a860982fc8a9eb83) · [状态效果 S-5cc6edf49653d53b](../../evidence/state_effects-sets-020.md#s-5cc6edf49653d53b)

### path-038048

```text
(config)# do-exec test opflex agent ha <cr>
```

Handler ` RVA 0xC482E30 `；selector ` 1 `；EOL ` RVA 0x33A939F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-058034

```text
(config)# do-exec test opflex agent service vxlan-evpn create <string> <cr>
```

Handler ` RVA 0xC494C00 `；selector ` 0 `；EOL ` RVA 0x33A97360 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Tenant name。

[条件 C-063ab9a36dd5b975](../../evidence/conditions-sets-003.md#c-063ab9a36dd5b975) · [参数 P-b42fb32a7d39d38b](../../evidence/parameters-sets-014.md#p-b42fb32a7d39d38b) · [状态效果 S-59df2c20c5a3ba0f](../../evidence/state_effects-sets-019.md#s-59df2c20c5a3ba0f)

### path-062669

```text
(config)# do-exec test opflex agent service vxlan-evpn create <string> rt-add ipv4 import <?bgp_extcomm_action@555588feb7b0> <cr>
```

Handler ` RVA 0xC494C00 `；selector ` 0 `；EOL ` RVA 0x33A97360 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Tenant name。

[条件 C-3e98026b96ce8065](../../evidence/conditions-sets-024.md#c-3e98026b96ce8065) · [缺口 G-71e809fd608046ad](../../evidence/gaps-sets-004.md#g-71e809fd608046ad) · [参数 P-b42fb32a7d39d38b](../../evidence/parameters-sets-014.md#p-b42fb32a7d39d38b) · [状态效果 S-29e9b131f3f4399d](../../evidence/state_effects-sets-009.md#s-29e9b131f3f4399d)

### path-054444

```text
(config)# do-exec test opflex agent service vxlan-evpn state <cr>
```

Handler ` RVA 0xC494F30 `；selector ` 0 `；EOL ` RVA 0x33A96FC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-054599

```text
(config)# do-exec test opssl nonblockingsession server dtls stop <cr>
```

Handler ` RVA 0x12A14A30 `；selector ` 0 `；EOL ` RVA 0x35936140 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6d1cef05085a0d2a](../../evidence/conditions-sets-042.md#c-6d1cef05085a0d2a) · [状态效果 S-4e3679429fdf7df7](../../evidence/state_effects-sets-017.md#s-4e3679429fdf7df7)

### path-030486

```text
(config)# do-exec test ospf debug <cr>
```

Handler ` RVA 0xFCD52B0 `；selector ` 0 `；EOL ` RVA 0x34894F28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-054026

```text
(config)# do-exec test ospf nsr cf error <number:0..65535> <cr>
```

Handler ` RVA 0xDACCD90 `；selector ` 10 `；EOL ` RVA 0x33FC6990 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Repeat count。

[条件 C-fc558060f3694bca](../../evidence/conditions-sets-097.md#c-fc558060f3694bca) · [参数 P-1e19628e5a2b3740](../../evidence/parameters-sets-003.md#p-1e19628e5a2b3740) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-046635

```text
(config)# do-exec test ospf nsr cf flow-off <cr>
```

Handler ` RVA 0xDACCD90 `；selector ` 9 `；EOL ` RVA 0x33FC66A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fc558060f3694bca](../../evidence/conditions-sets-097.md#c-fc558060f3694bca) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-046573

```text
(config)# do-exec test ospf nsr cf flow-on <cr>
```

Handler ` RVA 0xDACCD90 `；selector ` 8 `；EOL ` RVA 0x33FC6400 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fc558060f3694bca](../../evidence/conditions-sets-097.md#c-fc558060f3694bca) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-054022

```text
(config)# do-exec test ospf nsr cp clear <number:0..65535> <cr>
```

Handler ` RVA 0xDACCD90 `；selector ` 2 `；EOL ` RVA 0x33FC6FB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Opcode。

[条件 C-fc558060f3694bca](../../evidence/conditions-sets-097.md#c-fc558060f3694bca) · [参数 P-588a2cc36056eed0](../../evidence/parameters-sets-007.md#p-588a2cc36056eed0) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-046871

```text
(config)# do-exec test ospf nsr cp interface <cr>
```

Handler ` RVA 0xDACCD90 `；selector ` 5 `；EOL ` RVA 0x33FC78C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-54ca1d317d7f8cf8](../../evidence/conditions-sets-033.md#c-54ca1d317d7f8cf8) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061992

```text
(config)# do-exec test ospf nsr cp interface <interface> <cr>
```

Handler ` RVA 0xDACCD90 `；selector ` 5 `；EOL ` RVA 0x33FC78C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-92b9c0f8d4326ae7](../../evidence/conditions-sets-057.md#c-92b9c0f8d4326ae7) · [缺口 G-9521a88e41a22004](../../evidence/gaps-sets-005.md#g-9521a88e41a22004) · [参数 P-78822c7581dad0fd](../../evidence/parameters-sets-009.md#p-78822c7581dad0fd) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-046863

```text
(config)# do-exec test ospf nsr cp lsa <cr>
```

Handler ` RVA 0xDACCD90 `；selector ` 7 `；EOL ` RVA 0x33FC7F68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fc558060f3694bca](../../evidence/conditions-sets-097.md#c-fc558060f3694bca) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-046901

```text
(config)# do-exec test ospf nsr cp neighbor <cr>
```

Handler ` RVA 0xDACCD90 `；selector ` 6 `；EOL ` RVA 0x33FC7C90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1c82d1b2cde87f5f](../../evidence/conditions-sets-011.md#c-1c82d1b2cde87f5f) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061995

```text
(config)# do-exec test ospf nsr cp neighbor <interface> <cr>
```

Handler ` RVA 0xDACCD90 `；selector ` 6 `；EOL ` RVA 0x33FC7C90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7f28f073f140f73e](../../evidence/conditions-sets-049.md#c-7f28f073f140f73e) · [缺口 G-c92728bf805e6458](../../evidence/gaps-sets-007.md#g-c92728bf805e6458) · [参数 P-5c29a76996e4e816](../../evidence/parameters-sets-007.md#p-5c29a76996e4e816) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-046625

```text
(config)# do-exec test ospf nsr cp nop <cr>
```

Handler ` RVA 0xDACCD90 `；selector ` 1 `；EOL ` RVA 0x33FC6CA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fc558060f3694bca](../../evidence/conditions-sets-097.md#c-fc558060f3694bca) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-046773

```text
(config)# do-exec test ospf nsr cp router-id <cr>
```

Handler ` RVA 0xDACCD90 `；selector ` 4 `；EOL ` RVA 0x33FC7530 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fc558060f3694bca](../../evidence/conditions-sets-097.md#c-fc558060f3694bca) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-054063

```text
(config)# do-exec test ospf nsr cp sync <number:0..65535> <cr>
```

Handler ` RVA 0xDACCD90 `；selector ` 3 `；EOL ` RVA 0x33FC72A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Event。

[条件 C-fc558060f3694bca](../../evidence/conditions-sets-097.md#c-fc558060f3694bca) · [参数 P-1dd2c57cd27b0f0d](../../evidence/parameters-sets-003.md#p-1dd2c57cd27b0f0d) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-054020

```text
(config)# do-exec test ospf nsr recovery delay <number:0..255> <cr>
```

Handler ` RVA 0xDACCD90 `；selector ` 11 `；EOL ` RVA 0x33FC82E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Seconds to delay recovery。

[条件 C-fc558060f3694bca](../../evidence/conditions-sets-097.md#c-fc558060f3694bca) · [参数 P-56211fbc98f531aa](../../evidence/parameters-sets-007.md#p-56211fbc98f531aa) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-037274

```text
(config)# do-exec test ospf nsr unsynchronize <cr>
```

Handler ` RVA 0xDACCD90 `；selector ` 12 `；EOL ` RVA 0x33FC8580 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fc558060f3694bca](../../evidence/conditions-sets-097.md#c-fc558060f3694bca) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-030982

```text
(config)# do-exec test ospfv3 crimson <cr>
```

Handler ` RVA 0x11C027D0 `；selector ` 17 `；EOL ` RVA 0x35691980 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-f8557ab0cfe3b6d9](../../evidence/state_effects-sets-053.md#s-f8557ab0cfe3b6d9)

### path-062033

```text
(config)# do-exec test ospfv3 interface <interface> filter hello <cr>
```

Handler ` RVA 0x11C027D0 `；selector ` 3 `；EOL ` RVA 0x35691D90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6cb73a600300b577](../../evidence/conditions-sets-042.md#c-6cb73a600300b577) · [缺口 G-895fc534bcc28abc](../../evidence/gaps-sets-005.md#g-895fc534bcc28abc) · [参数 P-bca83470b4d22658](../../evidence/parameters-sets-014.md#p-bca83470b4d22658) · [状态效果 S-f8557ab0cfe3b6d9](../../evidence/state_effects-sets-053.md#s-f8557ab0cfe3b6d9)

### path-062036

```text
(config)# do-exec test ospfv3 interface <interface> filter none <cr>
```

Handler ` RVA 0x11C027D0 `；selector ` 4 `；EOL ` RVA 0x35692038 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6cb73a600300b577](../../evidence/conditions-sets-042.md#c-6cb73a600300b577) · [缺口 G-895fc534bcc28abc](../../evidence/gaps-sets-005.md#g-895fc534bcc28abc) · [参数 P-bca83470b4d22658](../../evidence/parameters-sets-014.md#p-bca83470b4d22658) · [状态效果 S-f8557ab0cfe3b6d9](../../evidence/state_effects-sets-053.md#s-f8557ab0cfe3b6d9)

### path-062352

```text
(config)# do-exec test ospfv3 interface <interface> neighbor <address> down <cr>
```

Handler ` RVA 0x11C027D0 `；selector ` 1 `；EOL ` RVA 0x35692608 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Router ID。

[条件 C-6cb73a600300b577](../../evidence/conditions-sets-042.md#c-6cb73a600300b577) · [缺口 G-895fc534bcc28abc](../../evidence/gaps-sets-005.md#g-895fc534bcc28abc) · [参数 P-7fdffd224e813f9b](../../evidence/parameters-sets-010.md#p-7fdffd224e813f9b) · [状态效果 S-1e097aa28781a7af](../../evidence/state_effects-sets-007.md#s-1e097aa28781a7af)

### path-062351

```text
(config)# do-exec test ospfv3 interface <interface> neighbor <address> up <cr>
```

Handler ` RVA 0x11C027D0 `；selector ` 0 `；EOL ` RVA 0x35692360 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Router ID。

[条件 C-6cb73a600300b577](../../evidence/conditions-sets-042.md#c-6cb73a600300b577) · [缺口 G-895fc534bcc28abc](../../evidence/gaps-sets-005.md#g-895fc534bcc28abc) · [参数 P-7fdffd224e813f9b](../../evidence/parameters-sets-010.md#p-7fdffd224e813f9b) · [状态效果 S-1e097aa28781a7af](../../evidence/state_effects-sets-007.md#s-1e097aa28781a7af)

### path-061466

```text
(config)# do-exec test ospfv3 vrf * crimson <cr>
```

Handler ` RVA 0x11C027D0 `；selector ` 17 `；EOL ` RVA 0x35691980 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-41293efedd4b57db](../../evidence/conditions-sets-025.md#c-41293efedd4b57db) · [缺口 G-98b625d87d16a99d](../../evidence/gaps-sets-006.md#g-98b625d87d16a99d) · [状态效果 S-296e38d6c6fdd070](../../evidence/state_effects-sets-009.md#s-296e38d6c6fdd070)

### path-028268

```text
(config)# do-exec test parser afs <cr>
```

Handler ` RVA 0xDF6BFD0 `；selector ` 0 `；EOL ` RVA 0x340E0AD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-49514f258a87cea4](../../evidence/conditions-sets-029.md#c-49514f258a87cea4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061220

```text
(config)# do-exec test parser chainfunc recursion <?call_action@555589600a20> <cr>
```

Handler ` RVA 0xDF33300 `；selector ` 0 `；EOL ` RVA 0x340A91E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-73c5f3fb2edd5194](../../evidence/conditions-sets-045.md#c-73c5f3fb2edd5194) · [缺口 G-d8f093436b8ebb53](../../evidence/gaps-sets-008.md#g-d8f093436b8ebb53) · [状态效果 S-934dcf01f4d5ea7d](../../evidence/state_effects-sets-031.md#s-934dcf01f4d5ea7d)

### path-034516

```text
(config)# do-exec test parser configure buffer <cr>
```

Handler ` RVA 0xDEF9430 `；selector ` 0 `；EOL ` RVA 0x340B00E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5f6508a36b1d191a](../../evidence/conditions-sets-037.md#c-5f6508a36b1d191a) · [状态效果 S-64d33135a678812c](../../evidence/state_effects-sets-022.md#s-64d33135a678812c)

### path-061235

```text
(config)# do-exec test parser configure file <url:dynamic> <cr>
```

Handler ` RVA 0xDEF9430 `；selector ` 0 `；EOL ` RVA 0x340B00E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6bd07b5f15996cc8](../../evidence/conditions-sets-042.md#c-6bd07b5f15996cc8) · [缺口 G-f6056c804542efc5](../../evidence/gaps-sets-008.md#g-f6056c804542efc5) · [参数 P-43ccf6a8c0f1694f](../../evidence/parameters-sets-006.md#p-43ccf6a8c0f1694f) · [状态效果 S-97e585927347b1ef](../../evidence/state_effects-sets-032.md#s-97e585927347b1ef)

### path-034299

```text
(config)# do-exec test parser consume-memory <number:0..2147483647> <cr>
```

Handler ` RVA 0xDEF9560 `；selector ` 0 `；EOL ` RVA 0x340ACF20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Memory size。

[条件 C-73c5f3fb2edd5194](../../evidence/conditions-sets-045.md#c-73c5f3fb2edd5194) · [参数 P-9fc98b3d0183c115](../../evidence/parameters-sets-012.md#p-9fc98b3d0183c115) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-028181

```text
(config)# do-exec test parser gmd <cr>
```

Handler ` RVA 0xDF333D0 `；selector ` 0 `；EOL ` RVA 0x340AC020 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-73c5f3fb2edd5194](../../evidence/conditions-sets-045.md#c-73c5f3fb2edd5194) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-028755

```text
(config)# do-exec test parser green-fe <cr>
```

Handler ` RVA 0xDF8E5F0 `；selector ` 0 `；EOL ` RVA 0x340AEDA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8342959d5623cf34](../../evidence/conditions-sets-051.md#c-8342959d5623cf34) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-044231

```text
(config)# do-exec test parser ngios native-green enable <cr>
```

Handler ` RVA 0xDF8EDC0 `；selector ` 0 `；EOL ` RVA 0x340AE210 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8342959d5623cf34](../../evidence/conditions-sets-051.md#c-8342959d5623cf34) · [状态效果 S-d1dd4d3e009af91f](../../evidence/state_effects-sets-044.md#s-d1dd4d3e009af91f)

### path-044266

```text
(config)# do-exec test parser ngios side-effect per-batch <cr>
```

Handler ` RVA 0xDF8ED00 `；selector ` 0 `；EOL ` RVA 0x340AE5D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8342959d5623cf34](../../evidence/conditions-sets-051.md#c-8342959d5623cf34) · [状态效果 S-8a9562df128253db](../../evidence/state_effects-sets-029.md#s-8a9562df128253db)

### path-044297

```text
(config)# do-exec test parser ngios validation enable <cr>
```

Handler ` RVA 0xDF8EC40 `；selector ` 0 `；EOL ` RVA 0x340AE9C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8342959d5623cf34](../../evidence/conditions-sets-051.md#c-8342959d5623cf34) · [状态效果 S-4f566d154a6f47fd](../../evidence/state_effects-sets-017.md#s-4f566d154a6f47fd)

### path-044335

```text
(config)# do-exec test parser ngios-meta path disable <cr>
```

Handler ` RVA 0xDF8EA80 `；selector ` 0 `；EOL ` RVA 0x340AF4E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8342959d5623cf34](../../evidence/conditions-sets-051.md#c-8342959d5623cf34) · [状态效果 S-6fc272d01d751f1d](../../evidence/state_effects-sets-024.md#s-6fc272d01d751f1d)

### path-061854

```text
(config)# do-exec test parser ngios-meta path enable <url:dynamic> <cr>
```

Handler ` RVA 0xDF8EA80 `；selector ` 0 `；EOL ` RVA 0x340AF4E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-cdf0e213490f3d1e](../../evidence/conditions-sets-079.md#c-cdf0e213490f3d1e) · [缺口 G-eb8224ee74a37d70](../../evidence/gaps-sets-008.md#g-eb8224ee74a37d70) · [参数 P-7f98c5c283d1631c](../../evidence/parameters-sets-010.md#p-7f98c5c283d1631c) · [状态效果 S-6f913f195780e569](../../evidence/state_effects-sets-024.md#s-6f913f195780e569)

### path-061840

```text
(config)# do-exec test parser opt list dyn <?option@555589609530> <cr>
```

Handler ` RVA 0xDF341F0 `；selector ` 0 `；EOL ` RVA 0x340B5598 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7834d509e67d29ff](../../evidence/conditions-sets-047.md#c-7834d509e67d29ff) · [缺口 G-7b0ca2d6822ed961](../../evidence/gaps-sets-005.md#g-7b0ca2d6822ed961) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061841

```text
(config)# do-exec test parser opt list norm <?keyword_option_list_mm_action@555589609880> <cr>
```

Handler ` RVA 0xDF34180 `；selector ` 0 `；EOL ` RVA 0x340B58C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-73c5f3fb2edd5194](../../evidence/conditions-sets-045.md#c-73c5f3fb2edd5194) · [缺口 G-c759fbaa946d2d2a](../../evidence/gaps-sets-007.md#g-c759fbaa946d2d2a) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-060767

```text
(config)# do-exec test parser pipeline <string> <cr>
```

Handler ` RVA 0xDF64E90 `；selector ` 0 `；EOL ` RVA 0x340AC498 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Enter the pipeline to run。

[条件 C-3bc1cf3091fc2823](../../evidence/conditions-sets-023.md#c-3bc1cf3091fc2823) · [缺口 G-df61d2e85006d5a8](../../evidence/gaps-sets-008.md#g-df61d2e85006d5a8) · [参数 P-4aac0968ffb2d725](../../evidence/parameters-sets-006.md#p-4aac0968ffb2d725) · [状态效果 S-0ddec861448b19d4](../../evidence/state_effects-sets-003.md#s-0ddec861448b19d4)

### path-044270

```text
(config)# do-exec test parser rc errno <number:0..2147483647> <cr>
```

Handler ` RVA 0xDEE2F90 `；selector ` 5 `；EOL ` RVA 0x340ADBA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` errno value to be mapped。

[条件 C-73c5f3fb2edd5194](../../evidence/conditions-sets-045.md#c-73c5f3fb2edd5194) · [参数 P-712d36c9f93ef0d8](../../evidence/parameters-sets-009.md#p-712d36c9f93ef0d8) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-052181

```text
(config)# do-exec test parser rc failure <number:11..211> <number:1..2> <cr>
```

Handler ` RVA 0xDEE2F90 `；selector ` 4 `；EOL ` RVA 0x340AD2F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` PRC error code；` unsigned_number ` PRC failure type。

[条件 C-73c5f3fb2edd5194](../../evidence/conditions-sets-045.md#c-73c5f3fb2edd5194) · [参数 P-0d3868e4e55310a0](../../evidence/parameters-sets-001.md#p-0d3868e4e55310a0) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-034441

```text
(config)# do-exec test parser rc invalid <cr>
```

Handler ` RVA 0xDEE2F90 `；selector ` 2 `；EOL ` RVA 0x340AD8B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-73c5f3fb2edd5194](../../evidence/conditions-sets-045.md#c-73c5f3fb2edd5194) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-052206

```text
(config)# do-exec test parser rc success <number:1..3> <number:1..4> <cr>
```

Handler ` RVA 0xDEE2F90 `；selector ` 3 `；EOL ` RVA 0x340AD630 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` PRC change type；` unsigned_number ` PRC change mode。

[条件 C-73c5f3fb2edd5194](../../evidence/conditions-sets-045.md#c-73c5f3fb2edd5194) · [参数 P-961119851006963a](../../evidence/parameters-sets-012.md#p-961119851006963a) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-034384

```text
(config)# do-exec test parser redirect small <cr>
```

Handler ` RVA 0xDF6BFD0 `；selector ` 4 `；EOL ` RVA 0x340E0E18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-66cef6ef5cfa3d6f](../../evidence/conditions-sets-040.md#c-66cef6ef5cfa3d6f) · [状态效果 S-318ff7cb721614eb](../../evidence/state_effects-sets-011.md#s-318ff7cb721614eb)

### path-034244

```text
(config)# do-exec test parser session-lock <number:0..1200> <cr>
```

Handler ` RVA 0xDF6BE30 `；selector ` 1 `；EOL ` RVA 0x340E0238 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Config session lock holdtime in seconds。

[条件 C-e58d1f8bc58f9c10](../../evidence/conditions-sets-089.md#c-e58d1f8bc58f9c10) · [参数 P-146602e89f177353](../../evidence/parameters-sets-002.md#p-146602e89f177353) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-034277

```text
(config)# do-exec test parser session-lock exit <cr>
```

Handler ` RVA 0xDF6BE30 `；selector ` 2 `；EOL ` RVA 0x340E04E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ac60a8bb88de2f75](../../evidence/conditions-sets-067.md#c-ac60a8bb88de2f75) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-034351

```text
(config)# do-exec test parser session-lock lock-break <cr>
```

Handler ` RVA 0xDF6BE30 `；selector ` 3 `；EOL ` RVA 0x340E07D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-02a7dfea128fd8c2](../../evidence/conditions-sets-001.md#c-02a7dfea128fd8c2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-028330

```text
(config)# do-exec test parser shell <cr>
```

Handler ` RVA 0xDF8E540 `；selector ` 0 `；EOL ` RVA 0x340ADE58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-73c5f3fb2edd5194](../../evidence/conditions-sets-045.md#c-73c5f3fb2edd5194) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-044309

```text
(config)# do-exec test parser syntax exclude display <cr>
```

Handler ` RVA 0xDF8F080 `；selector ` 0 `；EOL ` RVA 0x340AFC18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5f6508a36b1d191a](../../evidence/conditions-sets-037.md#c-5f6508a36b1d191a) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-052232

```text
(config)# do-exec test parser syntax exclude mode <string> <cr>
```

Handler ` RVA 0xDF8EF50 `；selector ` 0 `；EOL ` RVA 0x340AF948 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of mode or eol name。

[条件 C-5f6508a36b1d191a](../../evidence/conditions-sets-037.md#c-5f6508a36b1d191a) · [参数 P-7e1cba4935d8d80b](../../evidence/parameters-sets-010.md#p-7e1cba4935d8d80b) · [状态效果 S-569796861e08b79e](../../evidence/state_effects-sets-019.md#s-569796861e08b79e)

### path-062328

```text
(config)# do-exec test pbr unset <number:1..7> color adjacency <?general_pointer_number_action@555589d59438> <cr>
```

Handler ` RVA 0xFAE08D0 `；selector ` 0 `；EOL ` RVA 0x34805478 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Application: 1 - AAA。

[条件 C-bce912f92d39546f](../../evidence/conditions-sets-073.md#c-bce912f92d39546f) · [缺口 G-2470e7dc9a20e7a8](../../evidence/gaps-sets-002.md#g-2470e7dc9a20e7a8) · [参数 P-e311ee4f38aa4338](../../evidence/parameters-sets-017.md#p-e311ee4f38aa4338) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-056801

```text
(config)# do-exec test persistent variable api delete default <string> <cr>
```

Handler ` RVA 0xD7C8140 `；selector ` 3 `；EOL ` RVA 0x33EF6C10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Variable name string to delete。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-ff0df765d3c8d9be](../../evidence/parameters-sets-019.md#p-ff0df765d3c8d9be) · [状态效果 S-681af08da9bb4b3d](../../evidence/state_effects-sets-022.md#s-681af08da9bb4b3d)

### path-052186

```text
(config)# do-exec test persistent variable api flush default <cr>
```

Handler ` RVA 0xD7C8140 `；selector ` 4 `；EOL ` RVA 0x33EF6F58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-d0e1246d27ea02d8](../../evidence/state_effects-sets-044.md#s-d0e1246d27ea02d8)

### path-056791

```text
(config)# do-exec test persistent variable api get default <string> <cr>
```

Handler ` RVA 0xD7C8140 `；selector ` 2 `；EOL ` RVA 0x33EF67C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Variable name string to get。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-643ff067af6eb8fe](../../evidence/parameters-sets-008.md#p-643ff067af6eb8fe) · [状态效果 S-586f6916224eec39](../../evidence/state_effects-sets-019.md#s-586f6916224eec39)

### path-056786

```text
(config)# do-exec test persistent variable api isset default <string> <cr>
```

Handler ` RVA 0xD7C8140 `；selector ` 1 `；EOL ` RVA 0x33EF63E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Variable name string to determine if set。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-1e43095dccf81b7e](../../evidence/parameters-sets-003.md#p-1e43095dccf81b7e) · [状态效果 S-4679c0e7c58c783a](../../evidence/state_effects-sets-015.md#s-4679c0e7c58c783a)

### path-056783

```text
(config)# do-exec test persistent variable api set default <string> <cr>
```

Handler ` RVA 0xD7C8140 `；selector ` 0 `；EOL ` RVA 0x33EF5FF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Namevar string to set of the form &lt;name&gt;=&lt;value&gt;。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-bfff11a8e69a755d](../../evidence/parameters-sets-015.md#p-bfff11a8e69a755d) · [状态效果 S-e5404b3e3a16ad4f](../../evidence/state_effects-sets-048.md#s-e5404b3e3a16ad4f)

### path-044141

```text
(config)# do-exec test persistent variable error <string> <cr>
```

Handler ` RVA 0xD7C8140 `；selector ` 7 `；EOL ` RVA 0x33EF7960 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Error text to display。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-e6db5d0ce3e2c1f1](../../evidence/parameters-sets-017.md#p-e6db5d0ce3e2c1f1) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-044111

```text
(config)# do-exec test persistent variable media-delete <string> <cr>
```

Handler ` RVA 0xD7C8140 `；selector ` 6 `；EOL ` RVA 0x33EF76A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Full media entry string (filepath) to delete。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-ab01ede20decf82c](../../evidence/parameters-sets-013.md#p-ab01ede20decf82c) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-044084

```text
(config)# do-exec test persistent variable show cache <cr>
```

Handler ` RVA 0xD7C8140 `；selector ` 5 `；EOL ` RVA 0x33EF7340 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-3f72f6c811c5d65e](../../evidence/state_effects-sets-014.md#s-3f72f6c811c5d65e)

### path-062004

```text
(config)# do-exec test pimv6 join group <address> <interface> <cr>
```

Handler ` RVA 0x117AD0E0 `；selector ` 0 `；EOL ` RVA 0x35558540 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e13af097693dff22](../../evidence/conditions-sets-087.md#c-e13af097693dff22) · [缺口 G-6777e6402e8b1051](../../evidence/gaps-sets-004.md#g-6777e6402e8b1051) · [参数 P-9f9e8846585630cc](../../evidence/parameters-sets-012.md#p-9f9e8846585630cc) · [状态效果 S-31db03174588697c](../../evidence/state_effects-sets-011.md#s-31db03174588697c)

### path-062632

```text
(config)# do-exec test platform hardware interface <interface> plim egress max-fill hp <number:0..245760> <cr>
```

Handler ` RVA 0xE93D130 `；selector ` 0 `；EOL ` RVA 0x3434E0D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Bytes。

[条件 C-2fa2bf3da5355d54](../../evidence/conditions-sets-019.md#c-2fa2bf3da5355d54) · [缺口 G-234685bca6553a71](../../evidence/gaps-sets-002.md#g-234685bca6553a71) · [参数 P-117b59bc060fcdbd](../../evidence/parameters-sets-002.md#p-117b59bc060fcdbd) · [状态效果 S-3878e1e653a1e756](../../evidence/state_effects-sets-012.md#s-3878e1e653a1e756)

### path-056800

```text
(config)# do-exec test platform hardware poe cfg crit-limit <number:5000..15000> <cr>
```

Handler ` RVA 0x15FFE680 `；selector ` 11 `；EOL ` RVA 0x35EDE1D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Load shedding critical limit。

[条件 C-6c4a5951fac42fcb](../../evidence/conditions-sets-042.md#c-6c4a5951fac42fcb) · [参数 P-7d7edd3858492b7b](../../evidence/parameters-sets-010.md#p-7d7edd3858492b7b) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-056814

```text
(config)# do-exec test platform hardware poe cfg warn-limit <number:3000..8000> <cr>
```

Handler ` RVA 0x15FFE680 `；selector ` 12 `；EOL ` RVA 0x35EDE498 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Load shedding warning limit。

[条件 C-6c4a5951fac42fcb](../../evidence/conditions-sets-042.md#c-6c4a5951fac42fcb) · [参数 P-c98be1bcde1a0f08](../../evidence/parameters-sets-015.md#p-c98be1bcde1a0f08) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062233

```text
(config)# do-exec test platform hardware poe get <number:dynamic> global <cr>
```

Handler ` RVA 0x15FFD8E0 `；selector ` 4 `；EOL ` RVA 0x35EDCFB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Slot number。

[条件 C-edadaf6ee05ed42a](../../evidence/conditions-sets-092.md#c-edadaf6ee05ed42a) · [缺口 G-afba395f0659b4cd](../../evidence/gaps-sets-006.md#g-afba395f0659b4cd) · [参数 P-0328915490ed50f1](../../evidence/parameters-sets-001.md#p-0328915490ed50f1) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

