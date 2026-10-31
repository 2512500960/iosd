# exec · 六个基础模式的历史连接

[模式索引](README.md) · [总索引](../../README.md)

### path-016781

```text
(exec)# do-exec test parser session-lock lock-break <cr>
```

Handler ` RVA 0xDF6BE30 `；selector ` 3 `；EOL ` RVA 0x340E07D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9aab55ec3da8252f](../../evidence/conditions-sets-060.md#c-9aab55ec3da8252f) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-012905

```text
(exec)# do-exec test parser shell <cr>
```

Handler ` RVA 0xDF8E540 `；selector ` 0 `；EOL ` RVA 0x340ADE58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-916a320481e96250](../../evidence/conditions-sets-056.md#c-916a320481e96250) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-020858

```text
(exec)# do-exec test parser syntax exclude display <cr>
```

Handler ` RVA 0xDF8F080 `；selector ` 0 `；EOL ` RVA 0x340AFC18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e1fb39995fb37c72](../../evidence/conditions-sets-087.md#c-e1fb39995fb37c72) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023330

```text
(exec)# do-exec test parser syntax exclude mode <string> <cr>
```

Handler ` RVA 0xDF8EF50 `；selector ` 0 `；EOL ` RVA 0x340AF948 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Name of mode or eol name。

[条件 C-e1fb39995fb37c72](../../evidence/conditions-sets-087.md#c-e1fb39995fb37c72) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-7e1cba4935d8d80b](../../evidence/parameters-sets-010.md#p-7e1cba4935d8d80b) · [状态效果 S-bb27d0978c6745f8](../../evidence/state_effects-sets-040.md#s-bb27d0978c6745f8)

### path-024541

```text
(exec)# do-exec test persistent variable api delete default <string> <cr>
```

Handler ` RVA 0xD7C8140 `；selector ` 3 `；EOL ` RVA 0x33EF6C10 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Variable name string to delete。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-ff0df765d3c8d9be](../../evidence/parameters-sets-019.md#p-ff0df765d3c8d9be) · [状态效果 S-189dcb1c737f2d36](../../evidence/state_effects-sets-006.md#s-189dcb1c737f2d36)

### path-023320

```text
(exec)# do-exec test persistent variable api flush default <cr>
```

Handler ` RVA 0xD7C8140 `；selector ` 4 `；EOL ` RVA 0x33EF6F58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-8917458886b9f0d8](../../evidence/state_effects-sets-029.md#s-8917458886b9f0d8)

### path-024539

```text
(exec)# do-exec test persistent variable api get default <string> <cr>
```

Handler ` RVA 0xD7C8140 `；selector ` 2 `；EOL ` RVA 0x33EF67C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Variable name string to get。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-643ff067af6eb8fe](../../evidence/parameters-sets-008.md#p-643ff067af6eb8fe) · [状态效果 S-92a2a023698e8bfc](../../evidence/state_effects-sets-031.md#s-92a2a023698e8bfc)

### path-024537

```text
(exec)# do-exec test persistent variable api isset default <string> <cr>
```

Handler ` RVA 0xD7C8140 `；selector ` 1 `；EOL ` RVA 0x33EF63E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Variable name string to determine if set。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-1e43095dccf81b7e](../../evidence/parameters-sets-003.md#p-1e43095dccf81b7e) · [状态效果 S-84a42194c38c0e30](../../evidence/state_effects-sets-028.md#s-84a42194c38c0e30)

### path-024536

```text
(exec)# do-exec test persistent variable api set default <string> <cr>
```

Handler ` RVA 0xD7C8140 `；selector ` 0 `；EOL ` RVA 0x33EF5FF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Namevar string to set of the form &lt;name&gt;=&lt;value&gt;。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-bfff11a8e69a755d](../../evidence/parameters-sets-015.md#p-bfff11a8e69a755d) · [状态效果 S-ad3f38518fc7eb74](../../evidence/state_effects-sets-037.md#s-ad3f38518fc7eb74)

### path-020801

```text
(exec)# do-exec test persistent variable error <string> <cr>
```

Handler ` RVA 0xD7C8140 `；selector ` 7 `；EOL ` RVA 0x33EF7960 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Error text to display。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-e6db5d0ce3e2c1f1](../../evidence/parameters-sets-017.md#p-e6db5d0ce3e2c1f1) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-020791

```text
(exec)# do-exec test persistent variable media-delete <string> <cr>
```

Handler ` RVA 0xD7C8140 `；selector ` 6 `；EOL ` RVA 0x33EF76A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Full media entry string (filepath) to delete。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-ab01ede20decf82c](../../evidence/parameters-sets-013.md#p-ab01ede20decf82c) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-020780

```text
(exec)# do-exec test persistent variable show cache <cr>
```

Handler ` RVA 0xD7C8140 `；selector ` 5 `；EOL ` RVA 0x33EF7340 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-effed23c010a24b6](../../evidence/state_effects-sets-051.md#s-effed23c010a24b6)

### path-024540

```text
(exec)# do-exec test platform hardware poe cfg crit-limit <number:5000..15000> <cr>
```

Handler ` RVA 0x15FFE680 `；selector ` 11 `；EOL ` RVA 0x35EDE1D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Load shedding critical limit。

[条件 C-b8332689a5840f5c](../../evidence/conditions-sets-071.md#c-b8332689a5840f5c) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-7d7edd3858492b7b](../../evidence/parameters-sets-010.md#p-7d7edd3858492b7b) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024545

```text
(exec)# do-exec test platform hardware poe cfg warn-limit <number:3000..8000> <cr>
```

Handler ` RVA 0x15FFE680 `；selector ` 12 `；EOL ` RVA 0x35EDE498 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Load shedding warning limit。

[条件 C-b8332689a5840f5c](../../evidence/conditions-sets-071.md#c-b8332689a5840f5c) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-c98be1bcde1a0f08](../../evidence/parameters-sets-015.md#p-c98be1bcde1a0f08) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-020926

```text
(exec)# do-exec test platform software cef autovpn <cr>
```

Handler ` RVA 0xE5CE300 `；selector ` 5 `；EOL ` RVA 0x342FD060 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-020864

```text
(exec)# do-exec test platform software cef bgp <cr>
```

Handler ` RVA 0xE5CE300 `；selector ` 2 `；EOL ` RVA 0x342FC2C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-020908

```text
(exec)# do-exec test platform software cef off <cr>
```

Handler ` RVA 0xE5CE300 `；selector ` 1 `；EOL ` RVA 0x342FCDB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-020894

```text
(exec)# do-exec test platform software cef on <cr>
```

Handler ` RVA 0xE5CE300 `；selector ` 0 `；EOL ` RVA 0x342FCB10 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023368

```text
(exec)# do-exec test platform software cef replicate cbl_l2mc <cr>
```

Handler ` RVA 0xE5CE300 `；selector ` 4 `；EOL ` RVA 0x342FC878 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023359

```text
(exec)# do-exec test platform software cef replicate mpls <cr>
```

Handler ` RVA 0xE5CE300 `；selector ` 3 `；EOL ` RVA 0x342FC5D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021149

```text
(exec)# do-exec test platform software crimson db-write-lock <cr>
```

Handler ` RVA 0x1444AAD0 `；selector ` 28 `；EOL ` RVA 0x35D67DC8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-2149dbf4be4c381f](../../evidence/state_effects-sets-008.md#s-2149dbf4be4c381f)

### path-021167

```text
(exec)# do-exec test platform software crimson initdb <cr>
```

Handler ` RVA 0x1444AEF0 `；selector ` 17 `；EOL ` RVA 0x35D68110 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023463

```text
(exec)# do-exec test platform software crimson notification deregister <cr>
```

Handler ` RVA 0x1444A910 `；selector ` 23 `；EOL ` RVA 0x35D67A70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023458

```text
(exec)# do-exec test platform software crimson notification register <cr>
```

Handler ` RVA 0x1444A910 `；selector ` 22 `；EOL ` RVA 0x35D67770 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-025115

```text
(exec)# do-exec test platform software crimson operational add <number:0..4294967295> idbname <string> <cr>
```

Handler ` RVA 0x1444A610 `；selector ` 3 `；EOL ` RVA 0x35D6CDA0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Data to add；` string ` string to add。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-82c7b75fd84e942b](../../evidence/parameters-sets-010.md#p-82c7b75fd84e942b) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023507

```text
(exec)# do-exec test platform software crimson operational disable <cr>
```

Handler ` RVA 0x1444A610 `；selector ` 24 `；EOL ` RVA 0x35D70078 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024631

```text
(exec)# do-exec test platform software crimson operational disable idb <cr>
```

Handler ` RVA 0x1444A610 `；selector ` 25 `；EOL ` RVA 0x35D700E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024978

```text
(exec)# do-exec test platform software crimson operational disable idb filter <cr>
```

Handler ` RVA 0x1444A610 `；selector ` 26 `；EOL ` RVA 0x35D700B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023467

```text
(exec)# do-exec test platform software crimson operational init <cr>
```

Handler ` RVA 0x1444A610 `；selector ` 0 `；EOL ` RVA 0x35D6C4E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024613

```text
(exec)# do-exec test platform software crimson operational init app <cr>
```

Handler ` RVA 0x1444A610 `；selector ` 1 `；EOL ` RVA 0x35D6C218 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024611

```text
(exec)# do-exec test platform software crimson operational init eventq <cr>
```

Handler ` RVA 0x1444A610 `；selector ` 32 `；EOL ` RVA 0x35D6BF70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024619

```text
(exec)# do-exec test platform software crimson operational init idb <cr>
```

Handler ` RVA 0x1444A610 `；selector ` 2 `；EOL ` RVA 0x35D6C550 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024971

```text
(exec)# do-exec test platform software crimson operational init idb filter <cr>
```

Handler ` RVA 0x1444A610 `；selector ` 27 `；EOL ` RVA 0x35D6C528 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024628

```text
(exec)# do-exec test platform software crimson operational lock acquire <cr>
```

Handler ` RVA 0x1444A610 `；selector ` 12 `；EOL ` RVA 0x35D6F338 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024977

```text
(exec)# do-exec test platform software crimson operational lock acquire offload <cr>
```

Handler ` RVA 0x1444A610 `；selector ` 13 `；EOL ` RVA 0x35D6F310 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024632

```text
(exec)# do-exec test platform software crimson operational lock release <cr>
```

Handler ` RVA 0x1444A610 `；selector ` 14 `；EOL ` RVA 0x35D6F898 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024979

```text
(exec)# do-exec test platform software crimson operational lock release offload <cr>
```

Handler ` RVA 0x1444A610 `；selector ` 15 `；EOL ` RVA 0x35D6F870 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024630

```text
(exec)# do-exec test platform software crimson operational lock status <cr>
```

Handler ` RVA 0x1444A610 `；selector ` 16 `；EOL ` RVA 0x35D6FD68 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023500

```text
(exec)# do-exec test platform software crimson operational offload <cr>
```

Handler ` RVA 0x15711CA0 `；selector ` 5 `；EOL ` RVA 0x35D807B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2c01494c2478aadb](../../evidence/conditions-sets-017.md#c-2c01494c2478aadb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-025118

```text
(exec)# do-exec test platform software crimson operational offload add <number:0..4294967295> <number:0..4294967295> <cr>
```

Handler ` RVA 0x15711CA0 `；selector ` 1 `；EOL ` RVA 0x35D7FB40 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` table type；` unsigned_number ` start key。

[条件 C-cf4e4e31f2c7d1b7](../../evidence/conditions-sets-080.md#c-cf4e4e31f2c7d1b7) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-f2756e519af7f30b](../../evidence/parameters-sets-018.md#p-f2756e519af7f30b) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-025121

```text
(exec)# do-exec test platform software crimson operational offload delete <number:0..4294967295> <number:0..4294967295> <cr>
```

Handler ` RVA 0x15711CA0 `；selector ` 3 `；EOL ` RVA 0x35D80240 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` table type；` unsigned_number ` start key。

[条件 C-902bd60139f2589b](../../evidence/conditions-sets-056.md#c-902bd60139f2589b) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-da19aebda0fb7f04](../../evidence/parameters-sets-016.md#p-da19aebda0fb7f04) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024617

```text
(exec)# do-exec test platform software crimson operational offload register <cr>
```

Handler ` RVA 0x15711CA0 `；selector ` 0 `；EOL ` RVA 0x35D7F7C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-76923d32c91e51a8](../../evidence/conditions-sets-046.md#c-76923d32c91e51a8) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024976

```text
(exec)# do-exec test platform software crimson operational offload unregister <number:0..4294967295> <cr>
```

Handler ` RVA 0x15711CA0 `；selector ` 4 `；EOL ` RVA 0x35D80530 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` table ID。

[条件 C-2548b433c7819dc4](../../evidence/conditions-sets-015.md#c-2548b433c7819dc4) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-5b5df38e858431fe](../../evidence/parameters-sets-007.md#p-5b5df38e858431fe) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-025119

```text
(exec)# do-exec test platform software crimson operational offload update <number:0..4294967295> <number:0..4294967295> <cr>
```

Handler ` RVA 0x15711CA0 `；selector ` 2 `；EOL ` RVA 0x35D7FEC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` table type；` unsigned_number ` start key。

[条件 C-1f8745f238b3e271](../../evidence/conditions-sets-012.md#c-1f8745f238b3e271) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-95f8ffd09e1156d3](../../evidence/parameters-sets-012.md#p-95f8ffd09e1156d3) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024621

```text
(exec)# do-exec test platform software crimson operational print db <cr>
```

Handler ` RVA 0x1444A610 `；selector ` 7 `；EOL ` RVA 0x35D6E340 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024975

```text
(exec)# do-exec test platform software crimson operational print subblock <number:0..4294967295> <cr>
```

Handler ` RVA 0x1444A680 `；selector ` 21 `；EOL ` RVA 0x35D6E628 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` idb if number。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-f15aeabce5aae957](../../evidence/parameters-sets-018.md#p-f15aeabce5aae957) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024623

```text
(exec)# do-exec test platform software crimson operational remove <number:0..4294967295> <cr>
```

Handler ` RVA 0x1444A610 `；selector ` 5 `；EOL ` RVA 0x35D6DD58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Item to remove。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-20682b7bb48abe7d](../../evidence/parameters-sets-003.md#p-20682b7bb48abe7d) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024972

```text
(exec)# do-exec test platform software crimson operational remove <number:0..4294967295> update <cr>
```

Handler ` RVA 0x1444A610 `；selector ` 6 `；EOL ` RVA 0x35D6DA88 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Item to remove。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-20682b7bb48abe7d](../../evidence/parameters-sets-003.md#p-20682b7bb48abe7d) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-025124

```text
(exec)# do-exec test platform software crimson operational set <number:0..4294967295> idbstate <number:0..4294967295> <cr>
```

Handler ` RVA 0x1444A610 `；selector ` 11 `；EOL ` RVA 0x35D6EF90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Item number to set；` unsigned_number ` idbstate value。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-f7eb74ab28d3f63d](../../evidence/parameters-sets-018.md#p-f7eb74ab28d3f63d) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-025120

```text
(exec)# do-exec test platform software crimson operational set <number:0..4294967295> linestate <number:0..4294967295> <cr>
```

Handler ` RVA 0x1444A610 `；selector ` 8 `；EOL ` RVA 0x35D6E9E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Item number to set；` unsigned_number ` linestate value。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-644c4fd59bb06720](../../evidence/parameters-sets-008.md#p-644c4fd59bb06720) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-025122

```text
(exec)# do-exec test platform software crimson operational set <number:0..4294967295> namestring <string> <cr>
```

Handler ` RVA 0x1444A610 `；selector ` 9 `；EOL ` RVA 0x35D6ECD0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Item number to set；` string ` namestring to set。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-3262a3267a94e25d](../../evidence/parameters-sets-004.md#p-3262a3267a94e25d) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024973

```text
(exec)# do-exec test platform software crimson operational update <number:0..4294967295> description <cr>
```

Handler ` RVA 0x1444A610 `；selector ` 4 `；EOL ` RVA 0x35D6D748 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Data to update。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-c4f742b09c31791e](../../evidence/parameters-sets-015.md#p-c4f742b09c31791e) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024624

```text
(exec)# do-exec test platform software crimson persist restore-once disable-del <cr>
```

Handler ` RVA 0x1444AEF0 `；selector ` 34 `；EOL ` RVA 0x35D68720 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024626

```text
(exec)# do-exec test platform software crimson persist restore-once enable-del <cr>
```

Handler ` RVA 0x1444AEF0 `；selector ` 35 `；EOL ` RVA 0x35D689C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023481

```text
(exec)# do-exec test platform software crimson unreferenced <string> <cr>
```

Handler ` RVA 0x1444AEF0 `；selector ` 33 `；EOL ` RVA 0x35D68420 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Database name to check for unreferenced memory。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-6325791368bc4ff0](../../evidence/parameters-sets-008.md#p-6325791368bc4ff0) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024929

```text
(exec)# do-exec test platform software dbal batch deadline <number:1..30000> <number:1..30000> <cr>
```

Handler ` RVA 0x15733360 `；selector ` 0 `；EOL ` RVA 0x35D81CA0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Deadline of batch execution, between 1 ms and 30000 ms.；` unsigned_number ` After batch execution, sleep between 1 ms and 30000 ms.。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-8d2974dd9c14f70c](../../evidence/parameters-sets-011.md#p-8d2974dd9c14f70c) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-025177

```text
(exec)# do-exec test platform software dbal batch stress <number:1..4294967295> <number:1..2> <number:1..4294967295> <number:1..2> <cr>
```

Handler ` RVA 0x157307F0 `；selector ` 0 `；EOL ` RVA 0x35D81990 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` number of batches to test；` unsigned_number ` Defer or not in between. 1: defer, 2: do not defer；` unsigned_number ` Number of operation in a batch；` unsigned_number ` Mark batch as priority. 1: normal, 2: priority。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-55b53e298fc46ee9](../../evidence/parameters-sets-007.md#p-55b53e298fc46ee9) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023350

```text
(exec)# do-exec test platform software dbal lipc create <cr>
```

Handler ` RVA 0x15730E00 `；selector ` 0 `；EOL ` RVA 0x35D82298 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023356

```text
(exec)# do-exec test platform software dbal lipc destroy <cr>
```

Handler ` RVA 0x15731120 `；selector ` 0 `；EOL ` RVA 0x35D82540 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023355

```text
(exec)# do-exec test platform software dbal ripc create <cr>
```

Handler ` RVA 0x15731320 `；selector ` 0 `；EOL ` RVA 0x35D82818 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023341

```text
(exec)# do-exec test platform software dbal scenario <number:1..6> <cr>
```

Handler ` RVA 0x157314C0 `；selector ` 0 `；EOL ` RVA 0x35D81FA8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Type of scenario. 1: local, 2: app, 3: TDL sync, 4: TDL async with output, 5: TDL sync in async way, 6: dbal-test-server。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-c71e187408ea9439](../../evidence/parameters-sets-015.md#p-c71e187408ea9439) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023325

```text
(exec)# do-exec test platform software dbal tunnel start <cr>
```

Handler ` RVA 0x15730260 `；selector ` 0 `；EOL ` RVA 0x35D812A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023333

```text
(exec)# do-exec test platform software dbal tunnel stop <cr>
```

Handler ` RVA 0x157306C0 `；selector ` 0 `；EOL ` RVA 0x35D81550 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-020951

```text
(exec)# do-exec test platform software dta enable <cr>
```

Handler ` RVA 0xC63EF10 `；selector ` 0 `；EOL ` RVA 0x33AC6710 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-37c6848ac70ac937](../../evidence/state_effects-sets-012.md#s-37c6848ac70ac937)

### path-023384

```text
(exec)# do-exec test platform software dvlan notification off <cr>
```

Handler ` RVA 0x15761F40 `；selector ` 2 `；EOL ` RVA 0x35D88378 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023375

```text
(exec)# do-exec test platform software dvlan notification on <cr>
```

Handler ` RVA 0x15761F40 `；selector ` 3 `；EOL ` RVA 0x35D880D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021025

```text
(exec)# do-exec test platform software feature-telemetry disable <cr>
```

Handler ` RVA 0x14B5B8B0 `；selector ` 0 `；EOL ` RVA 0x35D758C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6505e995d929e959](../../evidence/conditions-sets-039.md#c-6505e995d929e959) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021045

```text
(exec)# do-exec test platform software feature-telemetry enable <cr>
```

Handler ` RVA 0x14B5B860 `；selector ` 0 `；EOL ` RVA 0x35D75B68 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a9d5171a6cf07ad8](../../evidence/conditions-sets-066.md#c-a9d5171a6cf07ad8) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024932

```text
(exec)# do-exec test platform software flow-control identifiers allocate ebfc all <cr>
```

Handler ` RVA 0xEAFA960 `；selector ` 0 `；EOL ` RVA 0x343AA958 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c316bb26dc0a8a0e](../../evidence/conditions-sets-075.md#c-c316bb26dc0a8a0e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-27b61715ec031d95](../../evidence/state_effects-sets-009.md#s-27b61715ec031d95)

### path-025113

```text
(exec)# do-exec test platform software infrastructure bipc clear fd <number:1..4294967295> <number:1..4294967295> <cr>
```

Handler ` RVA 0xE9C5930 `；selector ` 6 `；EOL ` RVA 0x34379A90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` IPC channel fd；` unsigned_number ` IPC sequence number。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-338c1b6e73df1dd9](../../evidence/parameters-sets-004.md#p-338c1b6e73df1dd9) · [状态效果 S-7f16418841cbc9b3](../../evidence/state_effects-sets-027.md#s-7f16418841cbc9b3)

### path-023459

```text
(exec)# do-exec test platform software infrastructure console on <cr>
```

Handler ` RVA 0xE9C5930 `；selector ` 7 `；EOL ` RVA 0x34379E28 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c90d9df4fa9bed6c](../../evidence/conditions-sets-077.md#c-c90d9df4fa9bed6c) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-6599e28e8fcd2e5e](../../evidence/state_effects-sets-022.md#s-6599e28e8fcd2e5e)

### path-023427

```text
(exec)# do-exec test platform software infrastructure drop-debug off <cr>
```

Handler ` RVA 0xE9C5930 `；selector ` 5 `；EOL ` RVA 0x34378A18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023432

```text
(exec)# do-exec test platform software infrastructure drop-debug on <cr>
```

Handler ` RVA 0xE9C5930 `；selector ` 4 `；EOL ` RVA 0x34378CC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023436

```text
(exec)# do-exec test platform software infrastructure pae-cssm send_packet <cr>
```

Handler ` RVA 0x1658B2C0 `；selector ` 0 `；EOL ` RVA 0x35FA4C68 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-628d63a9597ebce1](../../evidence/conditions-sets-038.md#c-628d63a9597ebce1) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024607

```text
(exec)# do-exec test platform software infrastructure session open <number:1..4294967295> <cr>
```

Handler ` RVA 0xE9C5930 `；selector ` 1 `；EOL ` RVA 0x34379680 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Session handle。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-4f1e17e220686aee](../../evidence/parameters-sets-007.md#p-4f1e17e220686aee) · [状态效果 S-2028b768beaab626](../../evidence/state_effects-sets-007.md#s-2028b768beaab626)

### path-023431

```text
(exec)# do-exec test platform software infrastructure watchdog off <cr>
```

Handler ` RVA 0xE9C5930 `；selector ` 3 `；EOL ` RVA 0x34378FC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023438

```text
(exec)# do-exec test platform software infrastructure watchdog on <cr>
```

Handler ` RVA 0xE9C5930 `；selector ` 2 `；EOL ` RVA 0x34379268 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-025099

```text
(exec)# do-exec test platform software inject bd <number:1..4096> <address> <address> ipv4 <cr>
```

Handler ` RVA 0xEA9C880 `；selector ` 1 `；EOL ` RVA 0x343994F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` BD number；` address ` Dst MAC address；` address ` Src MAC address。

[条件 C-80feb7c74f758a33](../../evidence/conditions-sets-050.md#c-80feb7c74f758a33) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-1b2ddfe043e3c48c](../../evidence/parameters-sets-003.md#p-1b2ddfe043e3c48c) · [状态效果 S-d5e9de7a70d1b56d](../../evidence/state_effects-sets-045.md#s-d5e9de7a70d1b56d)

### path-025100

```text
(exec)# do-exec test platform software inject bd-local <number:1..4096> <address> <address> ipv4 <cr>
```

Handler ` RVA 0xEA9C880 `；selector ` 2 `；EOL ` RVA 0x34399B78 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` BD number；` address ` Dst MAC address；` address ` Src MAC address。

[条件 C-7bdc232d232ad06b](../../evidence/conditions-sets-048.md#c-7bdc232d232ad06b) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-6e5d53caf4ab1776](../../evidence/parameters-sets-009.md#p-6e5d53caf4ab1776) · [状态效果 S-8c0fb68ac9b25378](../../evidence/state_effects-sets-030.md#s-8c0fb68ac9b25378)

### path-024945

```text
(exec)# do-exec test platform software inject bridge_vlan <number:1..4096> <address> <address> <cr>
```

Handler ` RVA 0xEA9C880 `；selector ` 4 `；EOL ` RVA 0x3439A9F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Bridge VLAN number；` address ` Dst MAC address；` address ` Src MAC address。

[条件 C-6a62b2b36b23b4b5](../../evidence/conditions-sets-041.md#c-6a62b2b36b23b4b5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-f32d96ee52c39e1c](../../evidence/parameters-sets-018.md#p-f32d96ee52c39e1c) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-020816

```text
(exec)# do-exec test platform software inject bypass <cr>
```

Handler ` RVA 0xEA60A60 `；selector ` 0 `；EOL ` RVA 0x34398A80 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023364

```text
(exec)# do-exec test platform software inject inject-rate <number:1..10000> <cr>
```

Handler ` RVA 0xEA9BB10 `；selector ` 0 `；EOL ` RVA 0x3439A070 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` packets/sec supported by platfform。

[条件 C-6a62b2b36b23b4b5](../../evidence/conditions-sets-041.md#c-6a62b2b36b23b4b5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-d70ce1762a244fde](../../evidence/parameters-sets-016.md#p-d70ce1762a244fde) · [状态效果 S-919081c44a9e5026](../../evidence/state_effects-sets-031.md#s-919081c44a9e5026)

### path-023416

```text
(exec)# do-exec test platform software inject ipv4 arp-trigger <cr>
```

Handler ` RVA 0xEA60A60 `；selector ` 3 `；EOL ` RVA 0x3439BAB0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a6bd1ecbb1c5c724](../../evidence/conditions-sets-064.md#c-a6bd1ecbb1c5c724) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024574

```text
(exec)# do-exec test platform software inject ipv4 nexthop <address> <cr>
```

Handler ` RVA 0xEA60A60 `；selector ` 2 `；EOL ` RVA 0x3439B830 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` IPv4 Nexthop Address。

[条件 C-a6bd1ecbb1c5c724](../../evidence/conditions-sets-064.md#c-a6bd1ecbb1c5c724) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-c9f339e88974e4e5](../../evidence/parameters-sets-015.md#p-c9f339e88974e4e5) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023413

```text
(exec)# do-exec test platform software inject ipv6 nd-trigger <cr>
```

Handler ` RVA 0xEA60A60 `；selector ` 4 `；EOL ` RVA 0x3439BD88 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a6bd1ecbb1c5c724](../../evidence/conditions-sets-064.md#c-a6bd1ecbb1c5c724) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-020821

```text
(exec)# do-exec test platform software inject keepalive <cr>
```

Handler ` RVA 0xEA60A60 `；selector ` 6 `；EOL ` RVA 0x343987D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-020829

```text
(exec)# do-exec test platform software inject off <cr>
```

Handler ` RVA 0xEA60A60 `；selector ` 1 `；EOL ` RVA 0x34398D28 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-020841

```text
(exec)# do-exec test platform software inject pak-priority <cr>
```

Handler ` RVA 0xEA60A60 `；selector ` 5 `；EOL ` RVA 0x34398FD0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024609

```text
(exec)# do-exec test platform software license expire eval <number:1..259200> <cr>
```

Handler ` RVA 0x12437380 `；selector ` 0 `；EOL ` RVA 0x35867168 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` minutes。

[条件 C-e3c66b1102dd1283](../../evidence/conditions-sets-088.md#c-e3c66b1102dd1283) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-1e0ad3d9a0d06b72](../../evidence/parameters-sets-003.md#p-1e0ad3d9a0d06b72) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023448

```text
(exec)# do-exec test platform software license metering reachability <cr>
```

Handler ` RVA 0x124373D0 `；selector ` 0 `；EOL ` RVA 0x35866E58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97a2de8a9ab82402](../../evidence/conditions-sets-059.md#c-97a2de8a9ab82402) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023349

```text
(exec)# do-exec test platform software lsmpi tx-fail-retry enable <cr>
```

Handler ` RVA 0xED2D730 `；selector ` 0 `；EOL ` RVA 0x3440C730 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d6f2c9a16121d932](../../evidence/state_effects-sets-046.md#s-d6f2c9a16121d932)

### path-024610

```text
(exec)# do-exec test platform software macsec pattern-delete name <string> <cr>
```

Handler ` RVA 0x160D7490 `；selector ` 54 `；EOL ` RVA 0x35ECA218 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` pattern name。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-2b96e7d041d5508f](../../evidence/parameters-sets-004.md#p-2b96e7d041d5508f) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-025273

```text
(exec)# do-exec test platform software macsec pattern-name name <string> is-control yes has-vlan-tag yes has-vlan-inner-tag yes vlan-id <number:0..65535> inner-vlan-id <number:0..65535> priority <number:0..15> header <string> header-length <number:0..65535> control-frame dmac dest-mac <address> <cr>
```

Handler ` RVA 0x160D7490 `；selector ` 55 `；EOL ` RVA 0x35EC94B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` pattern name；` unsigned_number ` outer vlan id；` unsigned_number ` inner vlan id；` unsigned_number ` priority level；` string ` header pattern；` unsigned_number ` header pattern length；` address ` MAC address。

[条件 C-329b24473abbc62e](../../evidence/conditions-sets-020.md#c-329b24473abbc62e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-8671486ebe6bccdf](../../evidence/parameters-sets-010.md#p-8671486ebe6bccdf) · [状态效果 S-c019f655516020c1](../../evidence/state_effects-sets-041.md#s-c019f655516020c1)

### path-020944

```text
(exec)# do-exec test platform software multicast join <cr>
```

Handler ` RVA 0xE6FA7C0 `；selector ` 1 `；EOL ` RVA 0x3430E098 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-020960

```text
(exec)# do-exec test platform software multicast leave <cr>
```

Handler ` RVA 0xE6FA7C0 `；selector ` 2 `；EOL ` RVA 0x3430E340 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023386

```text
(exec)# do-exec test platform software multicast shim dynamic <cr>
```

Handler ` RVA 0xE6FA7C0 `；selector ` 9 `；EOL ` RVA 0x3430C810 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023392

```text
(exec)# do-exec test platform software multicast shim notdl <cr>
```

Handler ` RVA 0xE6FA7C0 `；selector ` 10 `；EOL ` RVA 0x3430CAB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023367

```text
(exec)# do-exec test platform software multicast shim off <cr>
```

Handler ` RVA 0xE6FA7C0 `；selector ` 6 `；EOL ` RVA 0x3430C2C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023358

```text
(exec)# do-exec test platform software multicast shim on <cr>
```

Handler ` RVA 0xE6FA7C0 `；selector ` 7 `；EOL ` RVA 0x3430C018 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023376

```text
(exec)# do-exec test platform software multicast shim sticky <cr>
```

Handler ` RVA 0xE6FA7C0 `；selector ` 8 `；EOL ` RVA 0x3430C568 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023399

```text
(exec)# do-exec test platform software multicast shim tdl <cr>
```

Handler ` RVA 0xE6FA7C0 `；selector ` 11 `；EOL ` RVA 0x3430CD60 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-020925

```text
(exec)# do-exec test platform software multicast start <cr>
```

Handler ` RVA 0xE6FA7C0 `；selector ` 0 `；EOL ` RVA 0x3430DDF0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-020892

```text
(exec)# do-exec test platform software multicast status <cr>
```

Handler ` RVA 0xE6FA7C0 `；selector ` 4 `；EOL ` RVA 0x3430D028 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-020972

```text
(exec)# do-exec test platform software multicast stop <cr>
```

Handler ` RVA 0xE6FA7C0 `；selector ` 3 `；EOL ` RVA 0x3430E5E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-020822

```text
(exec)# do-exec test platform software peer timeout <cr>
```

Handler ` RVA 0xE9492B0 `；selector ` 0 `；EOL ` RVA 0x34350DB0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-768f0591ca6906dc](../../evidence/conditions-sets-046.md#c-768f0591ca6906dc) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021029

```text
(exec)# do-exec test platform software product-analytics fast-grace-period <cr>
```

Handler ` RVA 0x1658B060 `；selector ` 0 `；EOL ` RVA 0x35FA4068 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-675816c748cdb369](../../evidence/conditions-sets-040.md#c-675816c748cdb369) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-020990

```text
(exec)# do-exec test platform software product-analytics sa-notify-false <cr>
```

Handler ` RVA 0x1658ADB0 `；selector ` 0 `；EOL ` RVA 0x35FA3B18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5902331f63975401](../../evidence/conditions-sets-035.md#c-5902331f63975401) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021008

```text
(exec)# do-exec test platform software product-analytics sa-notify-true <cr>
```

Handler ` RVA 0x1658AFD0 `；selector ` 0 `；EOL ` RVA 0x35FA3DC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b5ff565f8fbf6b15](../../evidence/conditions-sets-070.md#c-b5ff565f8fbf6b15) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021048

```text
(exec)# do-exec test platform software product-analytics timer <cr>
```

Handler ` RVA 0x1658B100 `；selector ` 0 `；EOL ` RVA 0x35FA4310 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8ab9b7f5fa8c7370](../../evidence/conditions-sets-054.md#c-8ab9b7f5fa8c7370) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-020812

```text
(exec)# do-exec test platform software punt-keepalive ignore-fault <cr>
```

Handler ` RVA 0xEA60F20 `；selector ` 1 `；EOL ` RVA 0x3439C158 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-020827

```text
(exec)# do-exec test platform software punt-keepalive trigger-failure <cr>
```

Handler ` RVA 0xEA60F20 `；selector ` 0 `；EOL ` RVA 0x3439C400 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024950

```text
(exec)# do-exec test platform software qos statistics <number:1..50000> <number:1..100000> <number:1..100> <cr>
```

Handler ` RVA 0x10DA0020 `；selector ` 1 `；EOL ` RVA 0x34D1B8C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` dpidx from sh pl so dbidx swidb；` unsigned_number ` num queries；` unsigned_number ` num of query in parallel。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-65b36f41d2d9da61](../../evidence/parameters-sets-008.md#p-65b36f41d2d9da61) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-020899

```text
(exec)# do-exec test platform software redundancy use-vmac <cr>
```

Handler ` RVA 0x15A6EA80 `；selector ` 0 `；EOL ` RVA 0x35DE5530 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024577

```text
(exec)# do-exec test platform software rg ar_alwys_dvrt <number:0..4> <number:0..12> <cr>
```

Handler ` RVA 0xE75D020 `；selector ` 7 `；EOL ` RVA 0x3432BC80 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` action；` unsigned_number ` rg id。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-4ffd42aa3d1d5e77](../../evidence/parameters-sets-007.md#p-4ffd42aa3d1d5e77) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024954

```text
(exec)# do-exec test platform software rg notify bulksync <number:0..10> <number:0..10> <cr>
```

Handler ` RVA 0xE75D020 `；selector ` 2 `；EOL ` RVA 0x3432C378 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` rg id；` unsigned_number ` result。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-5e3b6cf8076791cc](../../evidence/parameters-sets-008.md#p-5e3b6cf8076791cc) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-025109

```text
(exec)# do-exec test platform software rg notify transport <number:0..10> <number:1..100000> <number:0..10> <cr>
```

Handler ` RVA 0xE75D020 `；selector ` 1 `；EOL ` RVA 0x3432C068 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` rg id；` unsigned_number ` handler；` unsigned_number ` state。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-769bf5d82d2ae140](../../evidence/parameters-sets-009.md#p-769bf5d82d2ae140) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-025227

```text
(exec)# do-exec test platform software rg services parameters <number:0..10> <number:0..10> <number:0..10> <number:0..1> <number:0..1> <cr>
```

Handler ` RVA 0xE75D020 `；selector ` 0 `；EOL ` RVA 0x3432B938 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` action；` unsigned_number ` rg id；` unsigned_number ` rg state；` unsigned_number ` transport request；` unsigned_number ` bulk sync request。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-7c5e56bce406174a](../../evidence/parameters-sets-010.md#p-7c5e56bce406174a) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021050

```text
(exec)# do-exec test platform software rg tc-req <cr>
```

Handler ` RVA 0xE75D020 `；selector ` 5 `；EOL ` RVA 0x3432D980 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-025247

```text
(exec)# do-exec test platform software rg transport parameters <number:1..100000> <number:0..10> <address> <address> <number:0..10> <number:0..2048> <number:0..2048> <cr>
```

Handler ` RVA 0xE75D020 `；selector ` 3 `；EOL ` RVA 0x3432C860 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` handler；` unsigned_number ` application；` address ` IPv4 src address；` address ` IPv4 dst address；` unsigned_number ` l4 protocol；` unsigned_number ` src port；` unsigned_number ` dst port。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-82c662ee053c7586](../../evidence/parameters-sets-010.md#p-82c662ee053c7586) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024964

```text
(exec)# do-exec test platform software shell command handler automore disable <cr>
```

Handler ` RVA 0xEB0C800 `；selector ` 0 `；EOL ` RVA 0x343B1310 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024961

```text
(exec)# do-exec test platform software shell command handler automore manual <cr>
```

Handler ` RVA 0xEB0C900 `；selector ` 0 `；EOL ` RVA 0x343B1068 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024599

```text
(exec)# do-exec test platform software shell command handler basic <cr>
```

Handler ` RVA 0xEB0C720 `；selector ` 0 `；EOL ` RVA 0x343B15A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024602

```text
(exec)# do-exec test platform software shell command handler null <cr>
```

Handler ` RVA 0xEB0C640 `；selector ` 0 `；EOL ` RVA 0x343B1850 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024958

```text
(exec)# do-exec test platform software shell command handler output redirect <cr>
```

Handler ` RVA 0xEB0CA90 `；selector ` 0 `；EOL ` RVA 0x343B0D70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024606

```text
(exec)# do-exec test platform software shell command handler space <cr>
```

Handler ` RVA 0xEB0C560 `；selector ` 0 `；EOL ` RVA 0x343B1AF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024591

```text
(exec)# do-exec test platform software shell command set delete <cr>
```

Handler ` RVA 0xEB0CD30 `；selector ` 0 `；EOL ` RVA 0x343B0A08 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024590

```text
(exec)# do-exec test platform software shell command set load <cr>
```

Handler ` RVA 0xEB0CCE0 `；selector ` 0 `；EOL ` RVA 0x343B0760 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024538

```text
(exec)# do-exec test platform software stdout log running-config enable <cr>
```

Handler ` RVA 0xE950340 `；selector ` 0 `；EOL ` RVA 0x34351DA0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-171e533f08adcc33](../../evidence/conditions-sets-009.md#c-171e533f08adcc33) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-ebbc7a26acb929ea](../../evidence/state_effects-sets-050.md#s-ebbc7a26acb929ea)

### path-025110

```text
(exec)# do-exec test platform software timestamp-engine oam y1731 default disable all <cr>
```

Handler ` RVA 0x15A9EA30 `；selector ` 4 `；EOL ` RVA 0x35DE78A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-84323e8725be7784](../../evidence/conditions-sets-051.md#c-84323e8725be7784) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-025105

```text
(exec)# do-exec test platform software timestamp-engine oam y1731 default enable all <cr>
```

Handler ` RVA 0x15A9EA30 `；selector ` 2 `；EOL ` RVA 0x35DE7268 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0a0f248ebabea68c](../../evidence/conditions-sets-004.md#c-0a0f248ebabea68c) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023449

```text
(exec)# do-exec test platform software uidp batch-count <number:0..1000> <cr>
```

Handler ` RVA 0x1599CE30 `；selector ` 0 `；EOL ` RVA 0x35DCF728 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Number of user sessions per batch。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-7c336c4b98660031](../../evidence/parameters-sets-010.md#p-7c336c4b98660031) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023444

```text
(exec)# do-exec test platform software uidp binding clear <cr>
```

Handler ` RVA 0x1599C3F0 `；selector ` 0 `；EOL ` RVA 0x35DCEE38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-025192

```text
(exec)# do-exec test platform software uidp binding ip-user add <address> <number:0..4294967295> <string> <cr>
```

Handler ` RVA 0x1599C4A0 `；selector ` 0 `；EOL ` RVA 0x35DCE1B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` IPv4 Address；` unsigned_number ` VPN ID；` string ` User name。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-168aba61599d0180](../../evidence/parameters-sets-002.md#p-168aba61599d0180) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-025193

```text
(exec)# do-exec test platform software uidp binding ip-user delete <address> <number:0..4294967295> <string> <cr>
```

Handler ` RVA 0x1599C4A0 `；selector ` 1 `；EOL ` RVA 0x35DCE4F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` IPv4 Address；` unsigned_number ` VPN ID；` string ` User name。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-82cd5055a6ddb96f](../../evidence/parameters-sets-010.md#p-82cd5055a6ddb96f) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024966

```text
(exec)# do-exec test platform software uidp binding user-usergroup add <string> <cr>
```

Handler ` RVA 0x1599C7F0 `；selector ` 2 `；EOL ` RVA 0x35DCE8A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` User name。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-12f4f3bbd76a04fe](../../evidence/parameters-sets-002.md#p-12f4f3bbd76a04fe) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024967

```text
(exec)# do-exec test platform software uidp binding user-usergroup delete <string> <cr>
```

Handler ` RVA 0x1599C7F0 `；selector ` 3 `；EOL ` RVA 0x35DCEBA0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` User name。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-1defe1bf1a446589](../../evidence/parameters-sets-003.md#p-1defe1bf1a446589) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023452

```text
(exec)# do-exec test platform software uidp dwnld-timer <number:100..2000> <cr>
```

Handler ` RVA 0x1599CEA0 `；selector ` 0 `；EOL ` RVA 0x35DCF9F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Pause time for downloading batch of sessions。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-72b2461fd4b2a57e](../../evidence/parameters-sets-009.md#p-72b2461fd4b2a57e) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023435

```text
(exec)# do-exec test platform software uidp user <string> <cr>
```

Handler ` RVA 0x1599CCD0 `；selector ` 4 `；EOL ` RVA 0x35DCF150 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` User name。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-0fa27b7ec79838bd](../../evidence/parameters-sets-002.md#p-0fa27b7ec79838bd) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023441

```text
(exec)# do-exec test platform software uidp user-group <string> <cr>
```

Handler ` RVA 0x1599CD80 `；selector ` 5 `；EOL ` RVA 0x35DCF440 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` User group name。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-a9f2b7b5d4e2e4fa](../../evidence/parameters-sets-013.md#p-a9f2b7b5d4e2e4fa) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024970

```text
(exec)# do-exec test platform software usb slot <number:1..4294967295> usbflash0 fake-remove <cr>
```

Handler ` RVA 0xE9C72A0 `；selector ` 0 `；EOL ` RVA 0x3437C7F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` slot/switch Number。

[条件 C-ea27f0cd7abfbb35](../../evidence/conditions-sets-090.md#c-ea27f0cd7abfbb35) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-8880f5ca265b7b86](../../evidence/parameters-sets-011.md#p-8880f5ca265b7b86) · [状态效果 S-6695152e28d59f22](../../evidence/state_effects-sets-022.md#s-6695152e28d59f22)

### path-014759

```text
(exec)# do-exec test pm <string> <cr>
```

Handler ` RVA 0x15DD1600 `；selector ` 0 `；EOL ` RVA 0x35E22898 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` ...。

[条件 C-8b704234a4206d3d](../../evidence/conditions-sets-054.md#c-8b704234a4206d3d) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-bc02e5e87b3d0fdc](../../evidence/parameters-sets-014.md#p-bc02e5e87b3d0fdc) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-018520

```text
(exec)# do-exec test policy-manager appl-event create <cr>
```

Handler ` RVA 0xE110C00 `；selector ` 0 `；EOL ` RVA 0x34205BA8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b246bbfb40a9cba1](../../evidence/conditions-sets-069.md#c-b246bbfb40a9cba1) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-8f0af1f4c015e7c8](../../evidence/state_effects-sets-030.md#s-8f0af1f4c015e7c8)

### path-018549

```text
(exec)# do-exec test policy-manager wd-timer-event create <cr>
```

Handler ` RVA 0xE110C00 `；selector ` 0 `；EOL ` RVA 0x34205F40 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-43b1e6628be5a68e](../../evidence/conditions-sets-026.md#c-43b1e6628be5a68e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-478ba465904b9869](../../evidence/state_effects-sets-016.md#s-478ba465904b9869)

### path-017913

```text
(exec)# do-exec test pppoe init-session-num <number:1..65535> <cr>
```

Handler ` RVA 0x11CB06C0 `；selector ` 12 `；EOL ` RVA 0x356B3650 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Starting PPPoE Session Number。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-465592a267d1213c](../../evidence/parameters-sets-006.md#p-465592a267d1213c) · [状态效果 S-a842e5973c256305](../../evidence/state_effects-sets-036.md#s-a842e5973c256305)

### path-021858

```text
(exec)# do-exec test pppoe session <number:1..20000> autogrant <cr>
```

Handler ` RVA 0x11CB0650 `；selector ` 2 `；EOL ` RVA 0x356B48A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` PPPoE Session Number to touch。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-7b01c122e4339bfe](../../evidence/parameters-sets-010.md#p-7b01c122e4339bfe) · [状态效果 S-a842e5973c256305](../../evidence/state_effects-sets-036.md#s-a842e5973c256305)

### path-023982

```text
(exec)# do-exec test pppoe session <number:1..20000> autogrant on <cr>
```

Handler ` RVA 0x11CB0650 `；selector ` 1 `；EOL ` RVA 0x356B45F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` PPPoE Session Number to touch。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-7b01c122e4339bfe](../../evidence/parameters-sets-010.md#p-7b01c122e4339bfe) · [状态效果 S-a842e5973c256305](../../evidence/state_effects-sets-036.md#s-a842e5973c256305)

### path-023991

```text
(exec)# do-exec test pppoe session <number:1..20000> grant-threshold <number:0..65534> <cr>
```

Handler ` RVA 0x11CB0650 `；selector ` 6 `；EOL ` RVA 0x356B56E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` PPPoE Session Number to touch；` unsigned_number ` Set grant credit unit threshold 。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-c52715e3f07536be](../../evidence/parameters-sets-015.md#p-c52715e3f07536be) · [状态效果 S-a842e5973c256305](../../evidence/state_effects-sets-036.md#s-a842e5973c256305)

### path-021839

```text
(exec)# do-exec test pppoe session <number:1..20000> headDropping <cr>
```

Handler ` RVA 0x11CB0650 `；selector ` 16 `；EOL ` RVA 0x356B3D50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` PPPoE Session Number to touch。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-7b01c122e4339bfe](../../evidence/parameters-sets-010.md#p-7b01c122e4339bfe) · [状态效果 S-a842e5973c256305](../../evidence/state_effects-sets-036.md#s-a842e5973c256305)

### path-023974

```text
(exec)# do-exec test pppoe session <number:1..20000> headDropping on <cr>
```

Handler ` RVA 0x11CB0650 `；selector ` 15 `；EOL ` RVA 0x356B3AA8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` PPPoE Session Number to touch。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-7b01c122e4339bfe](../../evidence/parameters-sets-010.md#p-7b01c122e4339bfe) · [状态效果 S-a842e5973c256305](../../evidence/state_effects-sets-036.md#s-a842e5973c256305)

### path-021846

```text
(exec)# do-exec test pppoe session <number:1..20000> inband-credits <cr>
```

Handler ` RVA 0x11CB0650 `；selector ` 14 `；EOL ` RVA 0x356B42F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` PPPoE Session Number to touch。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-7b01c122e4339bfe](../../evidence/parameters-sets-010.md#p-7b01c122e4339bfe) · [状态效果 S-a842e5973c256305](../../evidence/state_effects-sets-036.md#s-a842e5973c256305)

### path-023978

```text
(exec)# do-exec test pppoe session <number:1..20000> inband-credits on <cr>
```

Handler ` RVA 0x11CB0650 `；selector ` 13 `；EOL ` RVA 0x356B4050 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` PPPoE Session Number to touch。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-7b01c122e4339bfe](../../evidence/parameters-sets-010.md#p-7b01c122e4339bfe) · [状态效果 S-a842e5973c256305](../../evidence/state_effects-sets-036.md#s-a842e5973c256305)

### path-024002

```text
(exec)# do-exec test pppoe session <number:1..20000> local-credits <number:0..65535> <cr>
```

Handler ` RVA 0x11CB0650 `；selector ` 10 `；EOL ` RVA 0x356B5CC8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` PPPoE Session Number to touch；` unsigned_number ` local credits。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-1eb21824c744cc30](../../evidence/parameters-sets-003.md#p-1eb21824c744cc30) · [状态效果 S-a842e5973c256305](../../evidence/state_effects-sets-036.md#s-a842e5973c256305)

### path-023987

```text
(exec)# do-exec test pppoe session <number:1..20000> max-grant <number:0..65535> <cr>
```

Handler ` RVA 0x11CB0650 `；selector ` 5 `；EOL ` RVA 0x356B53F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` PPPoE Session Number to touch；` unsigned_number ` Set maximum number of credit units per grant。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-513dc72ce2a78132](../../evidence/parameters-sets-007.md#p-513dc72ce2a78132) · [状态效果 S-a842e5973c256305](../../evidence/state_effects-sets-036.md#s-a842e5973c256305)

### path-023993

```text
(exec)# do-exec test pppoe session <number:1..20000> padg <number:1..65535> <cr>
```

Handler ` RVA 0x11CB0650 `；selector ` 7 `；EOL ` RVA 0x356B50F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` PPPoE Session Number to touch；` unsigned_number ` Number of PPPoE credit units to grant。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-18fe21eb467de39c](../../evidence/parameters-sets-002.md#p-18fe21eb467de39c) · [状态效果 S-a842e5973c256305](../../evidence/state_effects-sets-036.md#s-a842e5973c256305)

### path-023988

```text
(exec)# do-exec test pppoe session <number:1..20000> padg off <cr>
```

Handler ` RVA 0x11CB0650 `；selector ` 3 `；EOL ` RVA 0x356B4E48 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` PPPoE Session Number to touch。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-7b01c122e4339bfe](../../evidence/parameters-sets-010.md#p-7b01c122e4339bfe) · [状态效果 S-a842e5973c256305](../../evidence/state_effects-sets-036.md#s-a842e5973c256305)

### path-023984

```text
(exec)# do-exec test pppoe session <number:1..20000> padg on <cr>
```

Handler ` RVA 0x11CB0650 `；selector ` 4 `；EOL ` RVA 0x356B4BA0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` PPPoE Session Number to touch。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-7b01c122e4339bfe](../../evidence/parameters-sets-010.md#p-7b01c122e4339bfe) · [状态效果 S-a842e5973c256305](../../evidence/state_effects-sets-036.md#s-a842e5973c256305)

### path-024034

```text
(exec)# do-exec test pppoe session <number:1..20000> padq receive-only <cr>
```

Handler ` RVA 0x11CB0650 `；selector ` 8 `；EOL ` RVA 0x356B6218 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` PPPoE Session Number to touch。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-7b01c122e4339bfe](../../evidence/parameters-sets-010.md#p-7b01c122e4339bfe) · [状态效果 S-878179bc855d0d9f](../../evidence/state_effects-sets-029.md#s-878179bc855d0d9f)

### path-023997

```text
(exec)# do-exec test pppoe session <number:1..20000> peer-credits <number:0..65535> <cr>
```

Handler ` RVA 0x11CB0650 `；selector ` 9 `；EOL ` RVA 0x356B59D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` PPPoE Session Number to touch；` unsigned_number ` local credit units。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-cec15d709fc4fb0a](../../evidence/parameters-sets-016.md#p-cec15d709fc4fb0a) · [状态效果 S-a842e5973c256305](../../evidence/state_effects-sets-036.md#s-a842e5973c256305)

### path-023309

```text
(exec)# do-exec test process create <number:1..5000> <number:1..10000> <number:1..5000> <cr>
```

Handler ` RVA 0xD6D2550 `；selector ` 0 `；EOL ` RVA 0x33ECDDE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Enter time to run for (ms)；` unsigned_number ` Enter time to sleep for (ms)；` unsigned_number ` Enter time to susp after (ms)。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-f57e4b11ecf3ba88](../../evidence/parameters-sets-018.md#p-f57e4b11ecf3ba88) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-016767

```text
(exec)# do-exec test process kill <number:1..4294967295> <cr>
```

Handler ` RVA 0xD6D2A10 `；selector ` 0 `；EOL ` RVA 0x33ECE140 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Pid to kill。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-cca3915cfbc7547d](../../evidence/parameters-sets-016.md#p-cca3915cfbc7547d) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-012582

```text
(exec)# do-exec test rfd <cr>
```

Handler ` RVA 0xD7C53C0 `；selector ` 0 `；EOL ` RVA 0x33EF4C90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0f5abec7b990c5a9](../../evidence/conditions-sets-006.md#c-0f5abec7b990c5a9) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021711

```text
(exec)# do-exec test rib application create <string> <cr>
```

Handler ` RVA 0xDC0CAC0 `；selector ` 5 `；EOL ` RVA 0x3400B460 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Application instance name。

[条件 C-6591baf7ee82edc1](../../evidence/conditions-sets-039.md#c-6591baf7ee82edc1) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-44a7689de98431a1](../../evidence/parameters-sets-006.md#p-44a7689de98431a1) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021698

```text
(exec)# do-exec test rib application delete <number:0..65535> <cr>
```

Handler ` RVA 0xDC0CAC0 `；selector ` 6 `；EOL ` RVA 0x3400B198 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` handle number。

[条件 C-6591baf7ee82edc1](../../evidence/conditions-sets-039.md#c-6591baf7ee82edc1) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-84485f3ce4166b87](../../evidence/parameters-sets-010.md#p-84485f3ce4166b87) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021672

```text
(exec)# do-exec test rib client create <string> <cr>
```

Handler ` RVA 0xDC0CAC0 `；selector ` 0 `；EOL ` RVA 0x34009A60 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Client name。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-6fbb31bff7eebb42](../../evidence/parameters-sets-009.md#p-6fbb31bff7eebb42) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021617

```text
(exec)# do-exec test rib client delete <number:1..2147483647> <cr>
```

Handler ` RVA 0xDC0CAC0 `；selector ` 1 `；EOL ` RVA 0x34009758 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` handle number。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-61bebf93f1ef1e6e](../../evidence/parameters-sets-008.md#p-61bebf93f1ef1e6e) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021677

```text
(exec)# do-exec test rib route show <number:1..2147483647> <cr>
```

Handler ` RVA 0xDC0CAC0 `；selector ` 3 `；EOL ` RVA 0x3400A550 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` handle number。

[条件 C-6591baf7ee82edc1](../../evidence/conditions-sets-039.md#c-6591baf7ee82edc1) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-8d99215107ac3986](../../evidence/parameters-sets-011.md#p-8d99215107ac3986) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021690

```text
(exec)# do-exec test rib table set forwarding-base <cr>
```

Handler ` RVA 0xDC0CAC0 `；selector ` 4 `；EOL ` RVA 0x3400A950 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6591baf7ee82edc1](../../evidence/conditions-sets-039.md#c-6591baf7ee82edc1) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-6a2f576c7cd10241](../../evidence/state_effects-sets-023.md#s-6a2f576c7cd10241)

### path-013775

```text
(exec)# do-exec test rib ut <cr>
```

Handler ` RVA 0xDC0CAC0 `；selector ` 8 `；EOL ` RVA 0x34009DE8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b1badac532a448c4](../../evidence/conditions-sets-069.md#c-b1badac532a448c4) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-022060

```text
(exec)# do-exec test rmi create user-type <string> <cr>
```

Handler ` RVA 0xE081680 `；selector ` 0 `；EOL ` RVA 0x341D60C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Resource User-Type Name。

[条件 C-632c0786f9acbf2f](../../evidence/conditions-sets-038.md#c-632c0786f9acbf2f) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-71c7f62eb30da67d](../../evidence/parameters-sets-009.md#p-71c7f62eb30da67d) · [状态效果 S-759b454ff3d03337](../../evidence/state_effects-sets-025.md#s-759b454ff3d03337)

### path-014626

```text
(exec)# do-exec test rmi entphyind <cr>
```

Handler ` RVA 0xD695F20 `；selector ` 0 `；EOL ` RVA 0x341D7518 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-025052

```text
(exec)# do-exec test rmon hc-alarms <number:1..65535> Low32bitvalue <number:0..4294967295> High32bitvalue <number:0..4294967295> <cr>
```

Handler ` RVA 0xC4F9D90 `；selector ` 0 `；EOL ` RVA 0x33AADCE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Hc alarm index；` unsigned_number ` Low32bitvalue；` unsigned_number ` High32bitvalue。

[条件 C-2fad28d0f75b0dcd](../../evidence/conditions-sets-019.md#c-2fad28d0f75b0dcd) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-88ec7857607f280e](../../evidence/parameters-sets-011.md#p-88ec7857607f280e) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-025148

```text
(exec)# do-exec test rsvp metadata forward <address> <address> <number:0..255> <number:0..65535> <number:0..65535> <cr>
```

Handler ` RVA 0x100784A0 `；selector ` 0 `；EOL ` RVA 0x34A3F398 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Destination address；` address ` Source address；` unsigned_number ` IP Protocol；` unsigned_number ` Destination port；` unsigned_number ` Source port。

[条件 C-41f80aa269af6c7b](../../evidence/conditions-sets-026.md#c-41f80aa269af6c7b) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-164d4baefc6af40a](../../evidence/parameters-sets-002.md#p-164d4baefc6af40a) · [状态效果 S-711e517d9ad80263](../../evidence/state_effects-sets-024.md#s-711e517d9ad80263)

### path-017815

```text
(exec)# do-exec test rsvp nsr disable <cr>
```

Handler ` RVA 0x10078B00 `；selector ` 0 `；EOL ` RVA 0x34A3ED00 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-017804

```text
(exec)# do-exec test rsvp nsr enable <cr>
```

Handler ` RVA 0x100789F0 `；selector ` 0 `；EOL ` RVA 0x34A3EA58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-017796

```text
(exec)# do-exec test rsvp nsr incr <cr>
```

Handler ` RVA 0x100788E0 `；selector ` 0 `；EOL ` RVA 0x34A3E7B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-017783

```text
(exec)# do-exec test rsvp nsr start <cr>
```

Handler ` RVA 0x100787C0 `；selector ` 0 `；EOL ` RVA 0x34A3E508 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-025258

```text
(exec)# do-exec test rsvp transport send path <address> <address> <number:0..255> <number:0..65535> <number:0..65535> <number:1..65535> <address> <number:1..65535> data <string> <cr>
```

Handler ` RVA 0x1005D100 `；selector ` 0 `；EOL ` RVA 0x34A3DFB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Destination address；` address ` Source address；` unsigned_number ` IP Protocol；` unsigned_number ` Destination port；` unsigned_number ` Source port；` unsigned_number ` Client Identifier；` address ` Initiator Id；` unsigned_number ` Instance Id；` string ` RSVP Transport message。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-c024f648c9188b95](../../evidence/parameters-sets-015.md#p-c024f648c9188b95) · [状态效果 S-61e3f70260eac3a6](../../evidence/state_effects-sets-021.md#s-61e3f70260eac3a6)

### path-018972

```text
(exec)# do-exec test rtty <number:0..4294967295> <string> <cr>
```

Handler ` RVA 0xCC38580 `；selector ` 0 `；EOL ` RVA 0x33C237D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Remote Seat ID(in hexadecimal)；` string ` Command String。

[条件 C-38a2391f4af8366c](../../evidence/conditions-sets-022.md#c-38a2391f4af8366c) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-87096cdef34360d5](../../evidence/parameters-sets-010.md#p-87096cdef34360d5) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-019047

```text
(exec)# do-exec test rtty statistics disable <cr>
```

Handler ` RVA 0xCC382E0 `；selector ` 0 `；EOL ` RVA 0x33C23D38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c3775814f8e22baa](../../evidence/conditions-sets-075.md#c-c3775814f8e22baa) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-019009

```text
(exec)# do-exec test rtty statistics enable <cr>
```

Handler ` RVA 0xCC382E0 `；selector ` 1 `；EOL ` RVA 0x33C23A90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7290dc6daf97f920](../../evidence/conditions-sets-044.md#c-7290dc6daf97f920) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-019077

```text
(exec)# do-exec test rtty statistics print <cr>
```

Handler ` RVA 0xCC38340 `；selector ` 0 `；EOL ` RVA 0x33C23FE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3f789b060de15d04](../../evidence/conditions-sets-025.md#c-3f789b060de15d04) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024851

```text
(exec)# do-exec test sasl client ip <address> port <number:0..65535> <cr>
```

Handler ` RVA 0x103D1180 `；selector ` 1 `；EOL ` RVA 0x34B14C98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` IP address for outgoing connection；` unsigned_number ` Port value for outgoing connection。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-0a6a0a313046b956](../../evidence/parameters-sets-001.md#p-0a6a0a313046b956) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-025165

```text
(exec)# do-exec test sasl client ip <address> port <number:0..65535> profile <string> <cr>
```

Handler ` RVA 0x103D1180 `；selector ` 2 `；EOL ` RVA 0x34B14F88 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` IP address for outgoing connection；` unsigned_number ` Port value for outgoing connection；` string ` SASL profile name。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-f6b83400a54cfc55](../../evidence/parameters-sets-018.md#p-f6b83400a54cfc55) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-022433

```text
(exec)# do-exec test sasl server port <number:0..65535> <cr>
```

Handler ` RVA 0x103D1180 `；selector ` 3 `；EOL ` RVA 0x34B153F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Port value for SASL listening。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-f5808002237e59f6](../../evidence/parameters-sets-018.md#p-f5808002237e59f6) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024850

```text
(exec)# do-exec test sasl server port <number:0..65535> profile <string> <cr>
```

Handler ` RVA 0x103D1180 `；selector ` 4 `；EOL ` RVA 0x34B156E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Port value for SASL listening；` string ` SASL profile name。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-7fbae1e202e71069](../../evidence/parameters-sets-010.md#p-7fbae1e202e71069) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-019121

```text
(exec)# do-exec test sasl server stop <cr>
```

Handler ` RVA 0x103D1180 `；selector ` 5 `；EOL ` RVA 0x34B15978 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-012879

```text
(exec)# do-exec test save snapshot <cr>
```

Handler ` RVA 0xD6D2B10 `；selector ` 0 `；EOL ` RVA 0x33ECE430 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-017687

```text
(exec)# do-exec test scheduler trash edisms <cr>
```

Handler ` RVA 0xD7A41D0 `；selector ` 0 `；EOL ` RVA 0x33EEE678 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-17b5add80072111f](../../evidence/conditions-sets-009.md#c-17b5add80072111f) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-27f9c672cc9c5ae9](../../evidence/state_effects-sets-009.md#s-27f9c672cc9c5ae9)

### path-013332

```text
(exec)# do-exec test scheduler watched-message <cr>
```

Handler ` RVA 0xD79FA20 `；selector ` 0 `；EOL ` RVA 0x33EED500 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5026f314b64ffa47](../../evidence/conditions-sets-031.md#c-5026f314b64ffa47) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-79f16ae13ea6d80e](../../evidence/state_effects-sets-026.md#s-79f16ae13ea6d80e)

### path-017663

```text
(exec)# do-exec test sctp association create <cr>
```

Handler ` RVA 0xCE848E0 `；selector ` 0 `；EOL ` RVA 0x33D12C40 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-013720

```text
(exec)# do-exec test sctp delete <cr>
```

Handler ` RVA 0xCE84E80 `；selector ` 0 `；EOL ` RVA 0x33D12690 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-017648

```text
(exec)# do-exec test sctp instance create <cr>
```

Handler ` RVA 0xCE828C0 `；selector ` 0 `；EOL ` RVA 0x33D12308 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021572

```text
(exec)# do-exec test sctp instance delete <number:1..65535> <cr>
```

Handler ` RVA 0xCE847D0 `；selector ` 0 `；EOL ` RVA 0x33D12668 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Local port of instance to delete。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-b7f8a9d96e4fa6a8](../../evidence/parameters-sets-014.md#p-b7f8a9d96e4fa6a8) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021679

```text
(exec)# do-exec test sctp parameters burstsize <number:1..1024> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 8 `；EOL ` RVA 0x33D0FE28 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Number of packets to burst。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-5f332658bcc3b1ba](../../evidence/parameters-sets-008.md#p-5f332658bcc3b1ba) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023958

```text
(exec)# do-exec test sctp parameters congabate <number:1..3> <number:0..65535> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 17 `；EOL ` RVA 0x33D11C18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Congestion level to define abate value；` unsigned_number ` Value for congestion abate。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-6e3b56e35279f34e](../../evidence/parameters-sets-009.md#p-6e3b56e35279f34e) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021763

```text
(exec)# do-exec test sctp parameters conglevels <number:0..3> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 15 `；EOL ` RVA 0x33D115A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Number of congestion levels to define。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-90dac4eb92412f64](../../evidence/parameters-sets-011.md#p-90dac4eb92412f64) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023954

```text
(exec)# do-exec test sctp parameters congonset <number:1..3> <number:0..65535> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 16 `；EOL ` RVA 0x33D118E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Congestion level to define onset value；` unsigned_number ` Value for congestion onset。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-07fdbf832d65708c](../../evidence/parameters-sets-001.md#p-07fdbf832d65708c) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021691

```text
(exec)# do-exec test sctp parameters delay <number:0..60000> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 9 `；EOL ` RVA 0x33D10118 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Delay (msecs) between bursts。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-a85ef6772e443ce4](../../evidence/parameters-sets-013.md#p-a85ef6772e443ce4) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-017877

```text
(exec)# do-exec test sctp parameters display <cr>
```

Handler ` RVA 0xCE6FC00 `；selector ` 0 `；EOL ` RVA 0x33D11EA0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021605

```text
(exec)# do-exec test sctp parameters fixedparams <number:0..1> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 4 `；EOL ` RVA 0x33D0F268 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Use fixed params (FALSE=0/TRUE=1)?。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-148bb4a30eac7147](../../evidence/parameters-sets-002.md#p-148bb4a30eac7147) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021700

```text
(exec)# do-exec test sctp parameters hbenabled <number:0..1> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 10 `；EOL ` RVA 0x33D10408 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Heartbeat dest addrs (FALSE=0/TRUE=1)?。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-acd27b8447a1b688](../../evidence/parameters-sets-013.md#p-acd27b8447a1b688) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021712

```text
(exec)# do-exec test sctp parameters hbtimeout <number:0..600000> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 11 `；EOL ` RVA 0x33D106F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Heartbeat timer value。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-001bdbe6024b7fc0](../../evidence/parameters-sets-001.md#p-001bdbe6024b7fc0) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021550

```text
(exec)# do-exec test sctp parameters instreams <number:1..1024> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 1 `；EOL ` RVA 0x33D0E998 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Number of inbound streams。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-f60c7b1ad05500ca](../../evidence/parameters-sets-018.md#p-f60c7b1ad05500ca) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021743

```text
(exec)# do-exec test sctp parameters maxRTO <number:300..65535> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 13 `；EOL ` RVA 0x33D10FC8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Max retrans timer value (ms)。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-656c5afea3fc72ab](../../evidence/parameters-sets-008.md#p-656c5afea3fc72ab) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021662

```text
(exec)# do-exec test sctp parameters maxoutstand <number:0..1024> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 7 `；EOL ` RVA 0x33D0FB38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Max number of packets outstanding。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-565a162e37a45ac2](../../evidence/parameters-sets-007.md#p-565a162e37a45ac2) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021639

```text
(exec)# do-exec test sctp parameters maxpackets <number:0..65535> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 6 `；EOL ` RVA 0x33D0F848 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Max number of packets to send (9999=inf)。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-7b10493dc6084a57](../../evidence/parameters-sets-010.md#p-7b10493dc6084a57) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021590

```text
(exec)# do-exec test sctp parameters maxpdusize <number:4..10000> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 3 `；EOL ` RVA 0x33D0EF78 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Pdu size of test dgrams。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-0cff93470ff98b66](../../evidence/parameters-sets-001.md#p-0cff93470ff98b66) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021732

```text
(exec)# do-exec test sctp parameters minRTO <number:300..65535> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 12 `；EOL ` RVA 0x33D10CD8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Min retrans timer value (ms)。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-f7c8c4e77b4b985e](../../evidence/parameters-sets-018.md#p-f7c8c4e77b4b985e) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021533

```text
(exec)# do-exec test sctp parameters outstreams <number:1..1024> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 0 `；EOL ` RVA 0x33D0E6A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Number of outbound streams。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-71ac10a0fbb6fc04](../../evidence/parameters-sets-009.md#p-71ac10a0fbb6fc04) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021573

```text
(exec)# do-exec test sctp parameters pdusize <number:4..10000> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 2 `；EOL ` RVA 0x33D0EC88 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Pdu size of test dgrams。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-6fa3fc9c170f9a06](../../evidence/parameters-sets-009.md#p-6fa3fc9c170f9a06) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021754

```text
(exec)# do-exec test sctp parameters rcvwin <number:1500..65535> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 14 `；EOL ` RVA 0x33D112B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Local receive window value (bytes)。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-ac176c644c368388](../../evidence/parameters-sets-013.md#p-ac176c644c368388) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021723

```text
(exec)# do-exec test sctp parameters testtype <number:0..1> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 18 `；EOL ` RVA 0x33D109E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Test type (SIMPLE=0/LOOPREQ=1)?。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-ed32cc90492c4587](../../evidence/parameters-sets-018.md#p-ed32cc90492c4587) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021619

```text
(exec)# do-exec test sctp parameters usealladdrs <number:0..1> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 5 `；EOL ` RVA 0x33D0F558 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Use all dest addrs (FALSE=0/TRUE=1)?。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-64b63411945a3011](../../evidence/parameters-sets-008.md#p-64b63411945a3011) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-018443

```text
(exec)# do-exec test sdb add <string> <cr>
```

Handler ` RVA 0xDEC82E0 `；selector ` 0 `；EOL ` RVA 0x34093138 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` name。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-5c1d0be0e07d0031](../../evidence/parameters-sets-007.md#p-5c1d0be0e07d0031) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-018471

```text
(exec)# do-exec test sdb remove <string> <cr>
```

Handler ` RVA 0xDEC8430 `；selector ` 0 `；EOL ` RVA 0x34093420 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` name。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-5c6127879750809b](../../evidence/parameters-sets-007.md#p-5c6127879750809b) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-018497

```text
(exec)# do-exec test sdb search <string> <cr>
```

Handler ` RVA 0xDEC8550 `；selector ` 0 `；EOL ` RVA 0x340936E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` name。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-427368a9e0878d44](../../evidence/parameters-sets-006.md#p-427368a9e0878d44) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-017712

```text
(exec)# do-exec test service-overlay application register <cr>
```

Handler ` RVA 0x108F5810 `；selector ` 1 `；EOL ` RVA 0x34BF7E70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ca3239a195954f20](../../evidence/conditions-sets-078.md#c-ca3239a195954f20) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-4e47bcca59b2cdd2](../../evidence/state_effects-sets-017.md#s-4e47bcca59b2cdd2)

### path-023976

```text
(exec)# do-exec test service-routing api debug <number:0..4294967295> <number:0..4294967295> <cr>
```

Handler ` RVA 0x10452690 `；selector ` 17 `；EOL ` RVA 0x34B2F8A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Service-Routing sf-client handle；` unsigned_number ` Debug flags。

[条件 C-3a6355524661c11b](../../evidence/conditions-sets-023.md#c-3a6355524661c11b) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-fc2096c688c2da52](../../evidence/parameters-sets-019.md#p-fc2096c688c2da52) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-025268

```text
(exec)# do-exec test service-routing api publish-service <number:1..4294967295> <number:0..65535> : <number:0..65535> : <number:0..4294967295> . <number:0..4294967295> . <number:0..4294967295> . <number:0..4294967295> <number:1..4294967295> <number:0..32768> <cr>
```

Handler ` RVA 0x10452690 `；selector ` 21 `；EOL ` RVA 0x34B2E0F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Service-Routing sf-client handle；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` Service-sequence；` unsigned_number ` Service-size。

[条件 C-8fe40725bca2e0f1](../../evidence/conditions-sets-056.md#c-8fe40725bca2e0f1) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-bbe7af018acbc6ac](../../evidence/parameters-sets-014.md#p-bbe7af018acbc6ac) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021793

```text
(exec)# do-exec test service-routing api register-client <number:0..4294967295> <cr>
```

Handler ` RVA 0x10452690 `；selector ` 24 `；EOL ` RVA 0x34B2D520 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Client context。

[条件 C-3a6355524661c11b](../../evidence/conditions-sets-023.md#c-3a6355524661c11b) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-c58be6cbdbca42b7](../../evidence/parameters-sets-015.md#p-c58be6cbdbca42b7) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023957

```text
(exec)# do-exec test service-routing api register-client <number:0..4294967295> <string> <cr>
```

Handler ` RVA 0x10452690 `；selector ` 23 `；EOL ` RVA 0x34B2D4F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Client context；` string ` Client name。

[条件 C-3a6355524661c11b](../../evidence/conditions-sets-023.md#c-3a6355524661c11b) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-28a8a8d90e5fc0a1](../../evidence/parameters-sets-004.md#p-28a8a8d90e5fc0a1) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-025267

```text
(exec)# do-exec test service-routing api subscribe-service <number:1..4294967295> <number:0..65535> : <number:0..65535> : <number:0..4294967295> . <number:0..4294967295> . <number:0..4294967295> . <number:0..4294967295> <number:0..255> <cr>
```

Handler ` RVA 0x10452690 `；selector ` 19 `；EOL ` RVA 0x34B2F088 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Service-Routing sf-client handle；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` Maximum-paths。

[条件 C-481470e3392e4e91](../../evidence/conditions-sets-028.md#c-481470e3392e4e91) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-7447444ab7796741](../../evidence/parameters-sets-009.md#p-7447444ab7796741) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-025263

```text
(exec)# do-exec test service-routing api unpublish-service <number:1..4294967295> <number:0..65535> : <number:0..65535> : <number:0..4294967295> . <number:0..4294967295> . <number:0..4294967295> . <number:0..4294967295> <cr>
```

Handler ` RVA 0x10452690 `；selector ` 20 `；EOL ` RVA 0x34B2E898 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Service-Routing sf-client handle；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance。

[条件 C-a2427361eb345980](../../evidence/conditions-sets-063.md#c-a2427361eb345980) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-6205f9bccb319166](../../evidence/parameters-sets-008.md#p-6205f9bccb319166) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021790

```text
(exec)# do-exec test service-routing api unregister-client <number:1..4294967295> <cr>
```

Handler ` RVA 0x10452690 `；selector ` 22 `；EOL ` RVA 0x34B2DA48 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Service-Routing sf-client handle。

[条件 C-3a6355524661c11b](../../evidence/conditions-sets-023.md#c-3a6355524661c11b) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-fd4fdd18c511da0a](../../evidence/parameters-sets-019.md#p-fd4fdd18c511da0a) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023969

```text
(exec)# do-exec test service-routing api unsubscribe-service <number:1..4294967295> <number:1..4294967295> <cr>
```

Handler ` RVA 0x10452690 `；selector ` 18 `；EOL ` RVA 0x34B2F598 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Service-Routing sf-client handle；` unsigned_number ` Subscription handle。

[条件 C-3a6355524661c11b](../../evidence/conditions-sets-023.md#c-3a6355524661c11b) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-ea16afa033846cd9](../../evidence/parameters-sets-018.md#p-ea16afa033846cd9) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-017843

```text
(exec)# do-exec test service-routing api version <cr>
```

Handler ` RVA 0x10452690 `；selector ` 25 `；EOL ` RVA 0x34B2D1A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3a6355524661c11b](../../evidence/conditions-sets-023.md#c-3a6355524661c11b) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-025039

```text
(exec)# do-exec test service-routing capabilities-manager api register <string> <string> <string> <cr>
```

Handler ` RVA 0x1045B700 `；selector ` 80 `；EOL ` RVA 0x34B34700 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Component；` string ` Capability；` string ` Capability Data。

[条件 C-3a6355524661c11b](../../evidence/conditions-sets-023.md#c-3a6355524661c11b) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-2cd42d186cef97f3](../../evidence/parameters-sets-004.md#p-2cd42d186cef97f3) · [状态效果 S-b96f3c52bcf7a447](../../evidence/state_effects-sets-039.md#s-b96f3c52bcf7a447)

### path-024758

```text
(exec)# do-exec test service-routing capabilities-manager api unregister <string> <string> <cr>
```

Handler ` RVA 0x1045B700 `；selector ` 80 `；EOL ` RVA 0x34B34A28 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Component；` string ` Capability。

[条件 C-3a6355524661c11b](../../evidence/conditions-sets-023.md#c-3a6355524661c11b) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-ca371a52bc56aa69](../../evidence/parameters-sets-015.md#p-ca371a52bc56aa69) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021775

```text
(exec)# do-exec test service-routing capabilities-manager api version <cr>
```

Handler ` RVA 0x1045B660 `；selector ` 79 `；EOL ` RVA 0x34B34CA8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3a6355524661c11b](../../evidence/conditions-sets-023.md#c-3a6355524661c11b) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024757

```text
(exec)# do-exec test service-routing xmcp client <number:0..4294967295> error-response <number:100..699> <cr>
```

Handler ` RVA 0x10472C70 `；selector ` 56 `；EOL ` RVA 0x34B37C48 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Client handle；` unsigned_number ` Error code。

[条件 C-3a6355524661c11b](../../evidence/conditions-sets-023.md#c-3a6355524661c11b) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-82ab05eb296bdede](../../evidence/parameters-sets-010.md#p-82ab05eb296bdede) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-017688

```text
(exec)# do-exec test session-mgr acct-stats start <cr>
```

Handler ` RVA 0xCAF8B40 `；selector ` 0 `；EOL ` RVA 0x33B97CF0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4c8d5440f97c91e1](../../evidence/conditions-sets-030.md#c-4c8d5440f97c91e1) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-e6aaf1e10d486695](../../evidence/state_effects-sets-049.md#s-e6aaf1e10d486695)

### path-021637

```text
(exec)# do-exec test session-mgr cga-remote-auth authc <number:1..4294967295> <cr>
```

Handler ` RVA 0xCAF8B40 `；selector ` 0 `；EOL ` RVA 0x33B98398 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Handle value。

[条件 C-4c8d5440f97c91e1](../../evidence/conditions-sets-030.md#c-4c8d5440f97c91e1) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-da2f08bdc200c03c](../../evidence/parameters-sets-016.md#p-da2f08bdc200c03c) · [状态效果 S-58ff239a19eb7c61](../../evidence/state_effects-sets-019.md#s-58ff239a19eb7c61)

### path-023908

```text
(exec)# do-exec test session-mgr crimson table mab create <cr>
```

Handler ` RVA 0xCAF8B40 `；selector ` 0 `；EOL ` RVA 0x33B98F00 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4c8d5440f97c91e1](../../evidence/conditions-sets-030.md#c-4c8d5440f97c91e1) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-34cf6f75e0e5181a](../../evidence/state_effects-sets-012.md#s-34cf6f75e0e5181a)

### path-025007

```text
(exec)# do-exec test session-mgr event send async start handle <number:1..4294967295> <cr>
```

Handler ` RVA 0xCAF8B40 `；selector ` 0 `；EOL ` RVA 0x33B96910 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Handle value。

[条件 C-de0a4b74d86f6344](../../evidence/conditions-sets-086.md#c-de0a4b74d86f6344) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-96568601ab7c7b37](../../evidence/parameters-sets-012.md#p-96568601ab7c7b37) · [状态效果 S-6cfd30bbcb0e0605](../../evidence/state_effects-sets-023.md#s-6cfd30bbcb0e0605)

### path-021676

```text
(exec)# do-exec test session-mgr fqdn-epm-notify <number:1..4294967295> <address> <cr>
```

Handler ` RVA 0xCAF8B40 `；selector ` 0 `；EOL ` RVA 0x33B98B50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Handle value；` address ` IP address to notify。

[条件 C-4c8d5440f97c91e1](../../evidence/conditions-sets-030.md#c-4c8d5440f97c91e1) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-d0e66e8ab24af0c2](../../evidence/parameters-sets-016.md#p-d0e66e8ab24af0c2) · [状态效果 S-e9d8cb6bdf52fdee](../../evidence/state_effects-sets-049.md#s-e9d8cb6bdf52fdee)

### path-017779

```text
(exec)# do-exec test session-mgr green create <cr>
```

Handler ` RVA 0xCAD3E50 `；selector ` 0 `；EOL ` RVA 0x33B99460 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4c8d5440f97c91e1](../../evidence/conditions-sets-030.md#c-4c8d5440f97c91e1) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-9495fac9398f6ed6](../../evidence/state_effects-sets-031.md#s-9495fac9398f6ed6)

### path-025034

```text
(exec)# do-exec test session-mgr identity mac <address> add ip <address> <cr>
```

Handler ` RVA 0xCAF8B40 `；selector ` 0 `；EOL ` RVA 0x33B9A048 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` MAC address；` address ` IP address。

[条件 C-4c8d5440f97c91e1](../../evidence/conditions-sets-030.md#c-4c8d5440f97c91e1) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-bb158b26fcbfa514](../../evidence/parameters-sets-014.md#p-bb158b26fcbfa514) · [状态效果 S-7a9f9550efc4bc07](../../evidence/state_effects-sets-026.md#s-7a9f9550efc4bc07)

### path-017672

```text
(exec)# do-exec test session-mgr sm-client register <cr>
```

Handler ` RVA 0xCAF8B40 `；selector ` 0 `；EOL ` RVA 0x33B97830 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4c8d5440f97c91e1](../../evidence/conditions-sets-030.md#c-4c8d5440f97c91e1) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-162a637839d61d97](../../evidence/state_effects-sets-005.md#s-162a637839d61d97)

### path-024736

```text
(exec)# do-exec test session-mgr test-vlan <string> <number:1..4095> <number:1..4> <number:1..1000> <cr>
```

Handler ` RVA 0xCAF8B40 `；selector ` 0 `；EOL ` RVA 0x33B98808 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Name of the vlan group；` unsigned_number ` Value of the vlan；` unsigned_number ` 1 to add any other value to remove；` unsigned_number ` Number of users。

[条件 C-4c8d5440f97c91e1](../../evidence/conditions-sets-030.md#c-4c8d5440f97c91e1) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-8f6fc02bc311139a](../../evidence/parameters-sets-011.md#p-8f6fc02bc311139a) · [状态效果 S-dd7c915de9fe513e](../../evidence/state_effects-sets-047.md#s-dd7c915de9fe513e)

### path-017562

```text
(exec)# do-exec test snmp cpu-stats start <cr>
```

Handler ` RVA 0xCC7C220 `；selector ` 0 `；EOL ` RVA 0x33C3C500 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e7f320a5aecb2b08](../../evidence/conditions-sets-090.md#c-e7f320a5aecb2b08) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-4f5b1de8c9ca687b](../../evidence/state_effects-sets-017.md#s-4f5b1de8c9ca687b)

### path-017697

```text
(exec)# do-exec test snmp trap config-copy <cr>
```

Handler ` RVA 0x104C05D0 `；selector ` 41 `；EOL ` RVA 0x33C3C888 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-ef946522354c21c5](../../evidence/state_effects-sets-051.md#s-ef946522354c21c5)

### path-021316

```text
(exec)# do-exec test ssm asynchronous throttling print <cr>
```

Handler ` RVA 0x10433590 `；selector ` 0 `；EOL ` RVA 0x34B25118 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-efedad924b461289](../../evidence/state_effects-sets-051.md#s-efedad924b461289)

### path-017254

```text
(exec)# do-exec test ssm counters enable <cr>
```

Handler ` RVA 0x104332C0 `；selector ` 0 `；EOL ` RVA 0x34B23798 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-cbf4c5f4959d0ee5](../../evidence/state_effects-sets-043.md#s-cbf4c5f4959d0ee5)

### path-023525

```text
(exec)# do-exec test ssm fcdb nosupport <number:1..25> <number:0..2> <cr>
```

Handler ` RVA 0x104365F0 `；selector ` 0 `；EOL ` RVA 0x34B23BB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` feature type；` unsigned_number ` nosupport action (0=ignore, 1=punt, 2=teardown seg)。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-23be321c29567b35](../../evidence/parameters-sets-003.md#p-23be321c29567b35) · [状态效果 S-70551a4f8a707616](../../evidence/state_effects-sets-024.md#s-70551a4f8a707616)

### path-017384

```text
(exec)# do-exec test ssm feature status <cr>
```

Handler ` RVA 0x10435390 `；selector ` 0 `；EOL ` RVA 0x34B24850 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-a5be2697229c5b6f](../../evidence/state_effects-sets-035.md#s-a5be2697229c5b6f)

### path-021223

```text
(exec)# do-exec test ssm repop <number:1..14> <number:0..2> <cr>
```

Handler ` RVA 0x104331B0 `；selector ` 0 `；EOL ` RVA 0x34B234A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` switch type : 1-AC/AC, 2-AC/ATOM, 3-AC/L2TP, 4-AC/VFI, 5-VFI/AToM, 6-VFI/L2TP, 7-All；` unsigned_number ` segment class type : 1-SSS, 2-HW, 3-ALL。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-53f05257c23695ba](../../evidence/parameters-sets-007.md#p-53f05257c23695ba) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021283

```text
(exec)# do-exec test ssm segment lock <number:1..4294967295> <cr>
```

Handler ` RVA 0x104332C0 `；selector ` 0 `；EOL ` RVA 0x34B24450 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` segment id。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-921027c1fa5afe65](../../evidence/parameters-sets-011.md#p-921027c1fa5afe65) · [状态效果 S-6c48f791e1247a43](../../evidence/state_effects-sets-023.md#s-6c48f791e1247a43)

### path-023539

```text
(exec)# do-exec test ssm segment support enable <number:1..41> <cr>
```

Handler ` RVA 0x104332C0 `；selector ` 0 `；EOL ` RVA 0x34B24110 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` segment type value。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-35adb604690ed821](../../evidence/parameters-sets-005.md#p-35adb604690ed821) · [状态效果 S-4d1edaf9160bb6e5](../../evidence/state_effects-sets-017.md#s-4d1edaf9160bb6e5)

### path-024646

```text
(exec)# do-exec test subscriber feature accounting accuracy throttling print <cr>
```

Handler ` RVA 0x1093B5A0 `；selector ` 0 `；EOL ` RVA 0x34C06558 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d87bd9cfcbfa1377](../../evidence/conditions-sets-083.md#c-d87bd9cfcbfa1377) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-2bf90243c0c040ce](../../evidence/state_effects-sets-010.md#s-2bf90243c0c040ce)

### path-023592

```text
(exec)# do-exec test subscriber feature timer acceleration enable <cr>
```

Handler ` RVA 0x1093F020 `；selector ` 0 `；EOL ` RVA 0x34C06130 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9dda1e763caecc9c](../../evidence/conditions-sets-061.md#c-9dda1e763caecc9c) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-1493bf30553205eb](../../evidence/state_effects-sets-005.md#s-1493bf30553205eb)

### path-023725

```text
(exec)# do-exec test subscriber policy account-logon session <number:0..4294967295> <cr>
```

Handler ` RVA 0x109D50A0 `；selector ` 0 `；EOL ` RVA 0x34C56688 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Subscriber Service Switch session id value。

[条件 C-06651ce7f985b3d5](../../evidence/conditions-sets-003.md#c-06651ce7f985b3d5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-a89542a0c784be09](../../evidence/parameters-sets-013.md#p-a89542a0c784be09) · [状态效果 S-df2cb366bee6d359](../../evidence/state_effects-sets-047.md#s-df2cb366bee6d359)

### path-023621

```text
(exec)# do-exec test subscriber policy condition-map <string> <string> <cr>
```

Handler ` RVA 0x10A59C40 `；selector ` 0 `；EOL ` RVA 0x34C749F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` The condition map to be tested for equality；` string ` The condition map to be used as the identifier source。

[条件 C-b4ffff23a5042390](../../evidence/conditions-sets-070.md#c-b4ffff23a5042390) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-10987eb1655aac27](../../evidence/parameters-sets-002.md#p-10987eb1655aac27) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-017453

```text
(exec)# do-exec test subscriber policy dummy <cr>
```

Handler ` RVA 0x109D50A0 `；selector ` 0 `；EOL ` RVA 0x34C55550 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-93d2a17b5dec9b02](../../evidence/conditions-sets-057.md#c-93d2a17b5dec9b02) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-5dd55f56e25f56c2](../../evidence/state_effects-sets-020.md#s-5dd55f56e25f56c2)

### path-025243

```text
(exec)# do-exec test subscriber policy epd accounting-req start session-guid <string> epd-flow-id <number:0..32> epd-ipaddress <address> <cr>
```

Handler ` RVA 0xFE8A740 `；selector ` 0 `；EOL ` RVA 0x34C53288 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Enter ISG Session GUID；` unsigned_number ` Enter EPD Flow Id；` address ` Enter EPD Device IP Address。

[条件 C-4763399528953cb2](../../evidence/conditions-sets-028.md#c-4763399528953cb2) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-c12bb31bafc45042](../../evidence/parameters-sets-015.md#p-c12bb31bafc45042) · [状态效果 S-f1362bdb6240807f](../../evidence/state_effects-sets-051.md#s-f1362bdb6240807f)

### path-025250

```text
(exec)# do-exec test subscriber policy epd conn_mgmt-query version <string> command <string> peer-ip <address> keepalive <number:0..3600> <cr>
```

Handler ` RVA 0xFE89ED0 `；selector ` 0 `；EOL ` RVA 0x34C54440 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Version string, only "1.0" is valid；` string ` Command string (establish, disestablish, keepalive)；` address ` IP address of the peer；` unsigned_number ` keepalive value(0 not to send)。

[条件 C-bbcb2e42ba704f3c](../../evidence/conditions-sets-073.md#c-bbcb2e42ba704f3c) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-528cd97ddb37152d](../../evidence/parameters-sets-007.md#p-528cd97ddb37152d) · [状态效果 S-8a791565af07eb86](../../evidence/state_effects-sets-029.md#s-8a791565af07eb86)

### path-024999

```text
(exec)# do-exec test subscriber policy epd conn_mgmt-ses-test <number:1..2> <number:0..30> <string> <cr>
```

Handler ` RVA 0xFE89E20 `；selector ` 0 `；EOL ` RVA 0x34C547F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` 1 - to add, 2 to remove；` unsigned_number ` conn id ；` string ` session guid string  。

[条件 C-cec82ced6be4ec31](../../evidence/conditions-sets-080.md#c-cec82ced6be4ec31) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-2f90b406a6098bc7](../../evidence/parameters-sets-004.md#p-2f90b406a6098bc7) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-025207

```text
(exec)# do-exec test subscriber policy epd handler coa-request epd-ipaddress <address> attr-list <string> <cr>
```

Handler ` RVA 0xFE7F1A0 `；selector ` 0 `；EOL ` RVA 0x34C537B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Enter Session IP Address；` string ` Attribute list name。

[条件 C-1e7275fc08b650dd](../../evidence/conditions-sets-012.md#c-1e7275fc08b650dd) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-69204721b34e1501](../../evidence/parameters-sets-008.md#p-69204721b34e1501) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-025208

```text
(exec)# do-exec test subscriber policy epd handler disconnect-request epd-ipaddress <address> attr-list <string> <cr>
```

Handler ` RVA 0xFE7F290 `；selector ` 0 `；EOL ` RVA 0x34C53B70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Enter Session IP Address；` string ` Attribute list name。

[条件 C-d6c38bbd31ca6fde](../../evidence/conditions-sets-083.md#c-d6c38bbd31ca6fde) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-c47ed38e510f496d](../../evidence/parameters-sets-015.md#p-c47ed38e510f496d) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023715

```text
(exec)# do-exec test subscriber policy epd handler stop <cr>
```

Handler ` RVA 0xFE7ECD0 `；selector ` 0 `；EOL ` RVA 0x34C53E08 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1dfdb0194b9ea2d6](../../evidence/conditions-sets-012.md#c-1dfdb0194b9ea2d6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024991

```text
(exec)# do-exec test subscriber policy epd session-mgmt-req activate-policy-req session-handle <number:0..4294967295> <cr>
```

Handler ` RVA 0xFE8A1B0 `；selector ` 0 `；EOL ` RVA 0x34C52850 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Enter ISG Session Handle。

[条件 C-200ceed63b6498f6](../../evidence/conditions-sets-012.md#c-200ceed63b6498f6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-ef7400e9df8d5866](../../evidence/parameters-sets-018.md#p-ef7400e9df8d5866) · [状态效果 S-19c1c0f8c5893d88](../../evidence/state_effects-sets-006.md#s-19c1c0f8c5893d88)

### path-025131

```text
(exec)# do-exec test subscriber policy epd session-query-req session-ipaddress <address> epd-ipaddress <address> <cr>
```

Handler ` RVA 0xFE89C40 `；selector ` 0 `；EOL ` RVA 0x34C52328 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Enter ISG Session IP Address；` address ` Enter EPD Device IP Address。

[条件 C-72b61c76aa8a7e5d](../../evidence/conditions-sets-044.md#c-72b61c76aa8a7e5d) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-995339be86ea8070](../../evidence/parameters-sets-012.md#p-995339be86ea8070) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024656

```text
(exec)# do-exec test subscriber policy epd session-terminate-req session-handle <number:0..4294967295> <cr>
```

Handler ` RVA 0xFE8A610 `；selector ` 0 `；EOL ` RVA 0x34C52DA0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Enter ISG Session Handle。

[条件 C-47af2e91d2f4da8b](../../evidence/conditions-sets-028.md#c-47af2e91d2f4da8b) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-bfaf933945c5acf1](../../evidence/parameters-sets-015.md#p-bfaf933945c5acf1) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023787

```text
(exec)# do-exec test subscriber policy insert circuit-id <string> <cr>
```

Handler ` RVA 0x109D50A0 `；selector ` 0 `；EOL ` RVA 0x34C575A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Circuit Id to be inserted for testing, enter "none" to disable。

[条件 C-efa0088ed9ef5241](../../evidence/conditions-sets-093.md#c-efa0088ed9ef5241) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-01f789955e639dbf](../../evidence/parameters-sets-001.md#p-01f789955e639dbf) · [状态效果 S-df4c1d92f4059f1b](../../evidence/state_effects-sets-047.md#s-df4c1d92f4059f1b)

### path-023670

```text
(exec)# do-exec test subscriber policy mlplink-added session <number:0..4294967295> <cr>
```

Handler ` RVA 0x109D50A0 `；selector ` 0 `；EOL ` RVA 0x34C55B88 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` MLP link Subscriber Service Switch session id value。

[条件 C-e973006d32405abe](../../evidence/conditions-sets-090.md#c-e973006d32405abe) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-eca3557bd67d1f82](../../evidence/parameters-sets-018.md#p-eca3557bd67d1f82) · [状态效果 S-827aa022b82555e5](../../evidence/state_effects-sets-028.md#s-827aa022b82555e5)

### path-025205

```text
(exec)# do-exec test subscriber policy policy-client session <number:0..4294967295> client Radius-Proxy event start <cr>
```

Handler ` RVA 0x109D50A0 `；selector ` 0 `；EOL ` RVA 0x34C550E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Subscriber Service Switch session id value。

[条件 C-e8a69ba24f434aeb](../../evidence/conditions-sets-090.md#c-e8a69ba24f434aeb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-43db9ec51cad8b99](../../evidence/parameters-sets-006.md#p-43db9ec51cad8b99) · [状态效果 S-ca820b3ac186f19e](../../evidence/state_effects-sets-043.md#s-ca820b3ac186f19e)

### path-023770

```text
(exec)# do-exec test subscriber policy send-session-log session <number:0..4294967295> <cr>
```

Handler ` RVA 0x109D50A0 `；selector ` 0 `；EOL ` RVA 0x34C57200 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Subscriber Service Switch session id value。

[条件 C-5ec07cd416f9fcdd](../../evidence/conditions-sets-037.md#c-5ec07cd416f9fcdd) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-2db34b641405b555](../../evidence/parameters-sets-004.md#p-2db34b641405b555) · [状态效果 S-8e4a2bcc296368a5](../../evidence/state_effects-sets-030.md#s-8e4a2bcc296368a5)

### path-021359

```text
(exec)# do-exec test subscriber policy service-profile-download <string> <cr>
```

Handler ` RVA 0x109D50A0 `；selector ` 0 `；EOL ` RVA 0x34C54BA0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` service profile key name。

[条件 C-adb4c1b45a70ee9a](../../evidence/conditions-sets-067.md#c-adb4c1b45a70ee9a) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-6e2772433acac708](../../evidence/parameters-sets-009.md#p-6e2772433acac708) · [状态效果 S-7cfeebb8ddbc430f](../../evidence/state_effects-sets-027.md#s-7cfeebb8ddbc430f)

### path-025004

```text
(exec)# do-exec test subscriber policy service-start session <number:0..4294967295> name <string> <cr>
```

Handler ` RVA 0x109D50A0 `；selector ` 0 `；EOL ` RVA 0x34C56E88 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Subscriber Service Switch session id value；` string ` Service name to download。

[条件 C-fef27d83fbb9a421](../../evidence/conditions-sets-098.md#c-fef27d83fbb9a421) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-9a05bf3f9bba2324](../../evidence/parameters-sets-012.md#p-9a05bf3f9bba2324) · [状态效果 S-4e0a2d538440dd5d](../../evidence/state_effects-sets-017.md#s-4e0a2d538440dd5d)

### path-025003

```text
(exec)# do-exec test subscriber policy service-stop session <number:0..4294967295> name <string> <cr>
```

Handler ` RVA 0x109D50A0 `；selector ` 0 `；EOL ` RVA 0x34C56A88 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Subscriber Service Switch session id value；` string ` Service name to download。

[条件 C-9fae708052294c4a](../../evidence/conditions-sets-062.md#c-9fae708052294c4a) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-51e8af1a53cec40c](../../evidence/parameters-sets-007.md#p-51e8af1a53cec40c) · [状态效果 S-f29b42b99236ffde](../../evidence/state_effects-sets-051.md#s-f29b42b99236ffde)

### path-023704

```text
(exec)# do-exec test subscriber policy session-deactivated session <number:0..4294967295> <cr>
```

Handler ` RVA 0x109D50A0 `；selector ` 0 `；EOL ` RVA 0x34C56310 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Subscriber Service Switch session id value。

[条件 C-72e4ae20c2fc54a9](../../evidence/conditions-sets-044.md#c-72e4ae20c2fc54a9) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-806442e5184ce743](../../evidence/parameters-sets-010.md#p-806442e5184ce743) · [状态效果 S-1b774f28c7bb0154](../../evidence/state_effects-sets-006.md#s-1b774f28c7bb0154)

### path-017475

```text
(exec)# do-exec test subscriber policy tcsession-req <cr>
```

Handler ` RVA 0x109D50A0 `；selector ` 0 `；EOL ` RVA 0x34C55830 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2d57c69eee85e66b](../../evidence/conditions-sets-018.md#c-2d57c69eee85e66b) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d64ea5c14685f952](../../evidence/state_effects-sets-045.md#s-d64ea5c14685f952)

### path-025010

```text
(exec)# do-exec test subscriber policy update session <number:0..4294967295> attr-list <string> <cr>
```

Handler ` RVA 0x109D50A0 `；selector ` 0 `；EOL ` RVA 0x34C57AD0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Subscriber Service Switch session id value；` string ` AAA attribute list name。

[条件 C-e18801909d3aaabf](../../evidence/conditions-sets-087.md#c-e18801909d3aaabf) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-2dc1c4b05030fe7a](../../evidence/parameters-sets-004.md#p-2dc1c4b05030fe7a) · [状态效果 S-12f4df4cdcb4da3d](../../evidence/state_effects-sets-004.md#s-12f4df4cdcb4da3d)

### path-017417

```text
(exec)# do-exec test sw-vlan show data <cr>
```

Handler ` RVA 0x15C8E860 `；selector ` 0 `；EOL ` RVA 0x35DFE5A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e371a26ff3529e46](../../evidence/conditions-sets-088.md#c-e371a26ff3529e46) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-5165f1d4525fabea](../../evidence/state_effects-sets-018.md#s-5165f1d4525fabea)

### path-018051

```text
(exec)# do-exec test system secure db <cr>
```

Handler ` RVA 0xE031AB0 `；selector ` 0 `；EOL ` RVA 0x3416FBB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-b6c9f8df84e4d7f1](../../evidence/state_effects-sets-039.md#s-b6c9f8df84e4d7f1)

### path-012492

```text
(exec)# do-exec test tcp delay <number:0..2147483647> <cr>
```

Handler ` RVA 0xCDFACC0 `；selector ` 2 `；EOL ` RVA 0x33CF79B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` number。

[条件 C-dd5ef0294e1185e4](../../evidence/conditions-sets-085.md#c-dd5ef0294e1185e4) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-dbbc7c51a2581030](../../evidence/parameters-sets-017.md#p-dbbc7c51a2581030) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-012488

```text
(exec)# do-exec test tcp drop <number:0..2147483647> <cr>
```

Handler ` RVA 0xCDFACC0 `；selector ` 1 `；EOL ` RVA 0x33CF7978 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` number。

[条件 C-ed009090c362d9f7](../../evidence/conditions-sets-092.md#c-ed009090c362d9f7) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-9905a3044e6cc7c3](../../evidence/parameters-sets-012.md#p-9905a3044e6cc7c3) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-012494

```text
(exec)# do-exec test tcp line <number:0..2147483647> <cr>
```

Handler ` RVA 0xCDFACC0 `；selector ` 0 `；EOL ` RVA 0x33CF7C58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` number。

[条件 C-008ede4b3776e913](../../evidence/conditions-sets-001.md#c-008ede4b3776e913) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-168d315b78b62806](../../evidence/parameters-sets-002.md#p-168d315b78b62806) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-012496

```text
(exec)# do-exec test tcp random <number:0..2147483647> <cr>
```

Handler ` RVA 0xCDFACC0 `；selector ` 3 `；EOL ` RVA 0x33CF7EF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` number。

[条件 C-255b00e0be60da3a](../../evidence/conditions-sets-015.md#c-255b00e0be60da3a) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-d316af619bb90043](../../evidence/parameters-sets-016.md#p-d316af619bb90043) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024775

```text
(exec)# do-exec test template scope global <string> bind dynamic <cr>
```

Handler ` RVA 0xD6DF7A0 `；selector ` 0 `；EOL ` RVA 0x33ED94B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Template name。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-635b9257d1a441af](../../evidence/parameters-sets-008.md#p-635b9257d1a441af) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024778

```text
(exec)# do-exec test template scope global <string> unbind dynamic <cr>
```

Handler ` RVA 0xD6DF7A0 `；selector ` 1 `；EOL ` RVA 0x33ED9780 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Template name。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-635b9257d1a441af](../../evidence/parameters-sets-008.md#p-635b9257d1a441af) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-025150

```text
(exec)# do-exec test template scope interface <string> bind static merge interface-global <cr>
```

Handler ` RVA 0xD6DAD60 `；selector ` 2 `；EOL ` RVA 0x33ED86E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Template name。

[条件 C-b1fd3797155aba51](../../evidence/conditions-sets-069.md#c-b1fd3797155aba51) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-e9b79b38c71467c5](../../evidence/parameters-sets-017.md#p-e9b79b38c71467c5) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-025152

```text
(exec)# do-exec test template scope interface <string> bind static replace interface-global <cr>
```

Handler ` RVA 0xD6DAD60 `；selector ` 3 `；EOL ` RVA 0x33ED89B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Template name。

[条件 C-b1fd3797155aba51](../../evidence/conditions-sets-069.md#c-b1fd3797155aba51) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-e9b79b38c71467c5](../../evidence/parameters-sets-017.md#p-e9b79b38c71467c5) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-025048

```text
(exec)# do-exec test template scope interface <string> unbind static interface-global <cr>
```

Handler ` RVA 0xD6DAD60 `；selector ` 4 `；EOL ` RVA 0x33ED90F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Template name。

[条件 C-b1fd3797155aba51](../../evidence/conditions-sets-069.md#c-b1fd3797155aba51) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-e9b79b38c71467c5](../../evidence/parameters-sets-017.md#p-e9b79b38c71467c5) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024006

```text
(exec)# do-exec test template scope interface nvgen interface-global <cr>
```

Handler ` RVA 0xD6DAF30 `；selector ` 0 `；EOL ` RVA 0x33ED7EB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-013983

```text
(exec)# do-exec test tenant-mgr disable-cfg <cr>
```

Handler ` RVA 0x123E7200 `；selector ` 0 `；EOL ` RVA 0x35849178 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c0aaa69a59207310](../../evidence/conditions-sets-074.md#c-c0aaa69a59207310) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-c6b89c049bf385a4](../../evidence/state_effects-sets-042.md#s-c6b89c049bf385a4)

### path-013965

```text
(exec)# do-exec test tenant-mgr enable-cfg <cr>
```

Handler ` RVA 0x123E7200 `；selector ` 0 `；EOL ` RVA 0x35848EC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c0aaa69a59207310](../../evidence/conditions-sets-074.md#c-c0aaa69a59207310) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-ff211dfe3c9f5a92](../../evidence/state_effects-sets-054.md#s-ff211dfe3c9f5a92)

### path-017162

```text
(exec)# do-exec test timer-wheel process create <cr>
```

Handler ` RVA 0xD7AC900 `；selector ` 0 `；EOL ` RVA 0x33EEEF30 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-298ec59a9772bd58](../../evidence/conditions-sets-016.md#c-298ec59a9772bd58) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-a642754b5bdea2c9](../../evidence/state_effects-sets-035.md#s-a642754b5bdea2c9)

### path-013385

```text
(exec)# do-exec test topology clients <cr>
```

Handler ` RVA 0xDB76190 `；selector ` 11 `；EOL ` RVA 0x33FE4560 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-017354

```text
(exec)# do-exec test topology create ipv6 <cr>
```

Handler ` RVA 0xDB76190 `；selector ` 1 `；EOL ` RVA 0x33FE5EF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6d7c11cfa6860d7e](../../evidence/conditions-sets-042.md#c-6d7c11cfa6860d7e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-90d46c1145819761](../../evidence/state_effects-sets-031.md#s-90d46c1145819761)

### path-017334

```text
(exec)# do-exec test topology delete ipv6 <cr>
```

Handler ` RVA 0xDB76190 `；selector ` 7 `；EOL ` RVA 0x33FE5A48 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6d7c11cfa6860d7e](../../evidence/conditions-sets-042.md#c-6d7c11cfa6860d7e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-c5552e130c9755f0](../../evidence/state_effects-sets-042.md#s-c5552e130c9755f0)

### path-017305

```text
(exec)# do-exec test topology lookup ipv6 <cr>
```

Handler ` RVA 0xDB76190 `；selector ` 2 `；EOL ` RVA 0x33FE53D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-9d641eafc81d68f4](../../evidence/state_effects-sets-033.md#s-9d641eafc81d68f4)

### path-013427

```text
(exec)# do-exec test topology walk <cr>
```

Handler ` RVA 0xDB76190 `；selector ` 14 `；EOL ` RVA 0x33FE4B80 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-46f8604fe47e8e34](../../evidence/conditions-sets-028.md#c-46f8604fe47e8e34) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023540

```text
(exec)# do-exec test track map name <string> create <cr>
```

Handler ` RVA 0xE14F560 `；selector ` 1 `；EOL ` RVA 0x34216BB0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Tracked object string。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-f066051966eee05c](../../evidence/parameters-sets-018.md#p-f066051966eee05c) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023575

```text
(exec)# do-exec test track map name <string> del <cr>
```

Handler ` RVA 0xE14F560 `；selector ` 5 `；EOL ` RVA 0x34217100 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Tracked object string。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-f066051966eee05c](../../evidence/parameters-sets-018.md#p-f066051966eee05c) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023558

```text
(exec)# do-exec test track map name <string> get <cr>
```

Handler ` RVA 0xE14F560 `；selector ` 2 `；EOL ` RVA 0x34216E58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Tracked object string。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-f066051966eee05c](../../evidence/parameters-sets-018.md#p-f066051966eee05c) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023573

```text
(exec)# do-exec test track map num <number:1..32767> del <cr>
```

Handler ` RVA 0xE14F560 `；selector ` 4 `；EOL ` RVA 0x342176D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Track number。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-57c3eb8779535685](../../evidence/parameters-sets-007.md#p-57c3eb8779535685) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023552

```text
(exec)# do-exec test track map num <number:1..32767> get <cr>
```

Handler ` RVA 0xE14F560 `；selector ` 3 `；EOL ` RVA 0x34217430 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Track number。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-57c3eb8779535685](../../evidence/parameters-sets-007.md#p-57c3eb8779535685) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-021236

```text
(exec)# do-exec test track service <string> up <cr>
```

Handler ` RVA 0xE14F670 `；selector ` 0 `；EOL ` RVA 0x34216180 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Tracked service name。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-8b58f3bab75800c0](../../evidence/parameters-sets-011.md#p-8b58f3bab75800c0) · [状态效果 S-d3d7531596494725](../../evidence/state_effects-sets-045.md#s-d3d7531596494725)

### path-013359

```text
(exec)# do-exec test track white-box <cr>
```

Handler ` RVA 0xE14F7A0 `；selector ` 0 `；EOL ` RVA 0x34215DD0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-51ab530bbb573823](../../evidence/conditions-sets-032.md#c-51ab530bbb573823) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023881

```text
(exec)# do-exec test tunnel Groups wccp <number:0..9> add <cr>
```

Handler ` RVA 0xB516500 `；selector ` 0 `；EOL ` RVA 0x33792A30 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` service group ID。

[条件 C-ce6ef86e74b6a0f0](../../evidence/conditions-sets-079.md#c-ce6ef86e74b6a0f0) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-816d5b8c6fbe0a85](../../evidence/parameters-sets-010.md#p-816d5b8c6fbe0a85) · [状态效果 S-12ab9d5f5c9bf55b](../../evidence/state_effects-sets-004.md#s-12ab9d5f5c9bf55b)

### path-025024

```text
(exec)# do-exec test tunnel Groups wccp <number:0..9> add ipv4 V1 <cr>
```

Handler ` RVA 0xB513640 `；selector ` 0 `；EOL ` RVA 0x33790108 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Overlay Group ID。

[条件 C-47a1cfc600ac9dd9](../../evidence/conditions-sets-028.md#c-47a1cfc600ac9dd9) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-f4d83aaa6eb40d39](../../evidence/parameters-sets-018.md#p-f4d83aaa6eb40d39) · [状态效果 S-6091d723f6bf305f](../../evidence/state_effects-sets-021.md#s-6091d723f6bf305f)

### path-023916

```text
(exec)# do-exec test tunnel Groups wccp <number:0..9> clear <cr>
```

Handler ` RVA 0xB513640 `；selector ` 6 `；EOL ` RVA 0x337916D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Overlay Group ID。

[条件 C-47a1cfc600ac9dd9](../../evidence/conditions-sets-028.md#c-47a1cfc600ac9dd9) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-f4d83aaa6eb40d39](../../evidence/parameters-sets-018.md#p-f4d83aaa6eb40d39) · [状态效果 S-4d95911d79fb8202](../../evidence/state_effects-sets-017.md#s-4d95911d79fb8202)

### path-023860

```text
(exec)# do-exec test tunnel Groups wccp <number:0..9> delete <cr>
```

Handler ` RVA 0xB513640 `；selector ` 1 `；EOL ` RVA 0x33790440 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Overlay Group ID。

[条件 C-47a1cfc600ac9dd9](../../evidence/conditions-sets-028.md#c-47a1cfc600ac9dd9) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-f4d83aaa6eb40d39](../../evidence/parameters-sets-018.md#p-f4d83aaa6eb40d39) · [状态效果 S-4d95911d79fb8202](../../evidence/state_effects-sets-017.md#s-4d95911d79fb8202)

### path-024742

```text
(exec)# do-exec test tunnel Groups wccp <number:0..9> df-bit set <cr>
```

Handler ` RVA 0xB513640 `；selector ` 5 `；EOL ` RVA 0x33791448 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Overlay Group ID。

[条件 C-47a1cfc600ac9dd9](../../evidence/conditions-sets-028.md#c-47a1cfc600ac9dd9) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-f4d83aaa6eb40d39](../../evidence/parameters-sets-018.md#p-f4d83aaa6eb40d39) · [状态效果 S-4d95911d79fb8202](../../evidence/state_effects-sets-017.md#s-4d95911d79fb8202)

### path-025026

```text
(exec)# do-exec test tunnel Groups wccp <number:0..9> endpoint <address> add <cr>
```

Handler ` RVA 0xB513640 `；selector ` 7 `；EOL ` RVA 0x33790AE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Overlay Group ID；` address ` IPv4 address。

[条件 C-47a1cfc600ac9dd9](../../evidence/conditions-sets-028.md#c-47a1cfc600ac9dd9) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-d106356a47c3c452](../../evidence/parameters-sets-016.md#p-d106356a47c3c452) · [状态效果 S-4d95911d79fb8202](../../evidence/state_effects-sets-017.md#s-4d95911d79fb8202)

### path-025029

```text
(exec)# do-exec test tunnel Groups wccp <number:0..9> endpoint <address> delete <cr>
```

Handler ` RVA 0xB513640 `；selector ` 8 `；EOL ` RVA 0x33790D88 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Overlay Group ID；` address ` IPv4 address。

[条件 C-47a1cfc600ac9dd9](../../evidence/conditions-sets-028.md#c-47a1cfc600ac9dd9) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-d106356a47c3c452](../../evidence/parameters-sets-016.md#p-d106356a47c3c452) · [状态效果 S-4d95911d79fb8202](../../evidence/state_effects-sets-017.md#s-4d95911d79fb8202)

### path-024731

```text
(exec)# do-exec test tunnel Groups wccp <number:0..9> source <address> <cr>
```

Handler ` RVA 0xB513640 `；selector ` 2 `；EOL ` RVA 0x33790750 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Overlay Group ID；` address ` IPv4 address。

[条件 C-47a1cfc600ac9dd9](../../evidence/conditions-sets-028.md#c-47a1cfc600ac9dd9) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-de0e272fb87adafa](../../evidence/parameters-sets-017.md#p-de0e272fb87adafa) · [状态效果 S-4d95911d79fb8202](../../evidence/state_effects-sets-017.md#s-4d95911d79fb8202)

### path-025021

```text
(exec)# do-exec test tunnel tun-to <number:0..9> add transport ipv4 none <cr>
```

Handler ` RVA 0xB51A690 `；selector ` 1 `；EOL ` RVA 0x33794348 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Tunnel-to test handle identifier。

[条件 C-7d9fb058237a4a07](../../evidence/conditions-sets-049.md#c-7d9fb058237a4a07) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-695815f3b54ec526](../../evidence/parameters-sets-008.md#p-695815f3b54ec526) · [状态效果 S-fd0d1cf1724942d9](../../evidence/state_effects-sets-054.md#s-fd0d1cf1724942d9)

### path-021578

```text
(exec)# do-exec test tunnel tun-to <number:0..9> delete <cr>
```

Handler ` RVA 0xB51A690 `；selector ` 2 `；EOL ` RVA 0x33794638 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Tunnel-to test handle identifier。

[条件 C-8c48dfc36479b2a5](../../evidence/conditions-sets-054.md#c-8c48dfc36479b2a5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-695815f3b54ec526](../../evidence/parameters-sets-008.md#p-695815f3b54ec526) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023898

```text
(exec)# do-exec test tunnel tun-to <number:0..9> display <number:0..160> <cr>
```

Handler ` RVA 0xB51A690 `；selector ` 7 `；EOL ` RVA 0x337968F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Tunnel-to test handle identifier；` unsigned_number ` Indent。

[条件 C-8c48dfc36479b2a5](../../evidence/conditions-sets-054.md#c-8c48dfc36479b2a5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-c32407e8d350360d](../../evidence/parameters-sets-015.md#p-c32407e8d350360d) · [状态效果 S-94d6be64fa157da0](../../evidence/state_effects-sets-032.md#s-94d6be64fa157da0)

### path-024723

```text
(exec)# do-exec test tunnel tun-to <number:0..9> endpoint <address> add <cr>
```

Handler ` RVA 0xB51A690 `；selector ` 13 `；EOL ` RVA 0x33795110 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Tunnel-to test handle identifier；` address ` IPv4 address。

[条件 C-8c48dfc36479b2a5](../../evidence/conditions-sets-054.md#c-8c48dfc36479b2a5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-e18f04e057ad6e28](../../evidence/parameters-sets-017.md#p-e18f04e057ad6e28) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024734

```text
(exec)# do-exec test tunnel tun-to <number:0..9> endpoint <address> delete <cr>
```

Handler ` RVA 0xB51A690 `；selector ` 14 `；EOL ` RVA 0x337953B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Tunnel-to test handle identifier；` address ` IPv4 address。

[条件 C-8c48dfc36479b2a5](../../evidence/conditions-sets-054.md#c-8c48dfc36479b2a5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-e18f04e057ad6e28](../../evidence/parameters-sets-017.md#p-e18f04e057ad6e28) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024739

```text
(exec)# do-exec test tunnel tun-to <number:0..9> feature enable post-encap <cr>
```

Handler ` RVA 0xB51A690 `；selector ` 9 `；EOL ` RVA 0x33796C50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Tunnel-to test handle identifier。

[条件 C-8c48dfc36479b2a5](../../evidence/conditions-sets-054.md#c-8c48dfc36479b2a5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-695815f3b54ec526](../../evidence/parameters-sets-008.md#p-695815f3b54ec526) · [状态效果 S-b73c4a3a62cee5ae](../../evidence/state_effects-sets-039.md#s-b73c4a3a62cee5ae)

