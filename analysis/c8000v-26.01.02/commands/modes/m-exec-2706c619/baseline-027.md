# exec · 六个基础模式的历史连接

[模式索引](README.md) · [总索引](../../README.md)

### path-024280

```text
(exec)# do-exec show ip nbar resources status <number:10..86400> <cr>
```

Handler ` RVA 0x10F219A0 `；selector ` 22 `；EOL ` RVA 0x3524CEF0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Specify age of links (to indicate which bucket)。

[条件 C-ab456b9cb3f5c3b4](../../evidence/conditions-sets-066.md#c-ab456b9cb3f5c3b4) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-49c60d7b54c4f3ee](../../evidence/parameters-sets-006.md#p-49c60d7b54c4f3ee) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-024859

```text
(exec)# do-exec show ip nbar resources status <number:10..86400> <number:1..50> <cr>
```

Handler ` RVA 0x10F21F60 `；selector ` 23 `；EOL ` RVA 0x3524CEC8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Specify age of links (to indicate which bucket)；` unsigned_number ` Number of links to view。

[条件 C-ab456b9cb3f5c3b4](../../evidence/conditions-sets-066.md#c-ab456b9cb3f5c3b4) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-d71cbaf17a27d2ca](../../evidence/parameters-sets-016.md#p-d71cbaf17a27d2ca) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-024275

```text
(exec)# do-exec show ip nbar resources status fadebucket <cr>
```

Handler ` RVA 0x10F21F60 `；selector ` 24 `；EOL ` RVA 0x3524C990 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ab456b9cb3f5c3b4](../../evidence/conditions-sets-066.md#c-ab456b9cb3f5c3b4) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-024855

```text
(exec)# do-exec show ip nbar resources status fadebucket <number:1..50> <cr>
```

Handler ` RVA 0x10F21F60 `；selector ` 25 `；EOL ` RVA 0x3524C968 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Number of links to view。

[条件 C-ab456b9cb3f5c3b4](../../evidence/conditions-sets-066.md#c-ab456b9cb3f5c3b4) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-663e50933124a4cf](../../evidence/parameters-sets-008.md#p-663e50933124a4cf) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-024270

```text
(exec)# do-exec show ip nbar resources status freebucket <cr>
```

Handler ` RVA 0x10F21F60 `；selector ` 26 `；EOL ` RVA 0x3524C438 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ab456b9cb3f5c3b4](../../evidence/conditions-sets-066.md#c-ab456b9cb3f5c3b4) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-024853

```text
(exec)# do-exec show ip nbar resources status freebucket <number:1..50> <cr>
```

Handler ` RVA 0x10F21F60 `；selector ` 27 `；EOL ` RVA 0x3524C410 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Number of links to view。

[条件 C-ab456b9cb3f5c3b4](../../evidence/conditions-sets-066.md#c-ab456b9cb3f5c3b4) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-911a5d92236ca3a7](../../evidence/parameters-sets-011.md#p-911a5d92236ca3a7) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019105

```text
(exec)# do-exec show ip nbar statistics <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 27 `；EOL ` RVA 0x3524B6C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-86effce09d7ececf](../../evidence/conditions-sets-052.md#c-86effce09d7ececf) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019061

```text
(exec)# do-exec show ip nbar version <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 1 `；EOL ` RVA 0x3524B3E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f7984553236e75b1](../../evidence/conditions-sets-096.md#c-f7984553236e75b1) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019225

```text
(exec)# do-exec show ip nhrp attribute <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 16 `；EOL ` RVA 0x347F5C28 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019277

```text
(exec)# do-exec show ip nhrp instances <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 20 `；EOL ` RVA 0x347F5F38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-acc11270165a94e0](../../evidence/conditions-sets-067.md#c-acc11270165a94e0) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019123

```text
(exec)# do-exec show ip nhrp purge <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 2 `；EOL ` RVA 0x347F3F80 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019355

```text
(exec)# do-exec show ip nhrp redirect <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 6 `；EOL ` RVA 0x347F1958 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022567

```text
(exec)# do-exec show ip nhrp redirect statistics <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 7 `；EOL ` RVA 0x347F1930 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019348

```text
(exec)# do-exec show ip nhrp shortcut <cr>
```

Handler ` RVA 0x108FE580 `；selector ` 0 `；EOL ` RVA 0x34BF8EE8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-cbbbda02548ecf09](../../evidence/state_effects-sets-043.md#s-cbbbda02548ecf09)

### path-019159

```text
(exec)# do-exec show ip nhrp traffic <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 1 `；EOL ` RVA 0x347F3670 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-015154

```text
(exec)# do-exec show ip ospf <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 7 `；EOL ` RVA 0x34892168 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e9fe8519482ec89e](../../evidence/conditions-sets-090.md#c-e9fe8519482ec89e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-018938

```text
(exec)# do-exec show ip ospf bad-checksum <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 1 `；EOL ` RVA 0x3487AD60 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019262

```text
(exec)# do-exec show ip ospf border-routers <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 17 `；EOL ` RVA 0x348788A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e2bdf75d04d89e48](../../evidence/conditions-sets-087.md#c-e2bdf75d04d89e48) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019562

```text
(exec)# do-exec show ip ospf database <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 58 `；EOL ` RVA 0x34895630 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e68542957fd6318b](../../evidence/conditions-sets-089.md#c-e68542957fd6318b) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-783079044ded522d](../../evidence/state_effects-sets-026.md#s-783079044ded522d)

### path-022708

```text
(exec)# do-exec show ip ospf database database-summary <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 60 `；EOL ` RVA 0x34896290 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-03510c5a0f8b69a0](../../evidence/conditions-sets-002.md#c-03510c5a0f8b69a0) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-783079044ded522d](../../evidence/state_effects-sets-026.md#s-783079044ded522d)

### path-024360

```text
(exec)# do-exec show ip ospf database database-summary detail <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 54 `；EOL ` RVA 0x348965B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b5be62908a105171](../../evidence/conditions-sets-070.md#c-b5be62908a105171) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-f05419f2510a4fba](../../evidence/state_effects-sets-051.md#s-f05419f2510a4fba)

### path-019377

```text
(exec)# do-exec show ip ospf delete-list <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 57 `；EOL ` RVA 0x34876370 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e2bdf75d04d89e48](../../evidence/conditions-sets-087.md#c-e2bdf75d04d89e48) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022699

```text
(exec)# do-exec show ip ospf internal forwarding-addresses <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 23 `；EOL ` RVA 0x34891EA0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e2bdf75d04d89e48](../../evidence/conditions-sets-087.md#c-e2bdf75d04d89e48) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-024339

```text
(exec)# do-exec show ip ospf internal memory cache <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 2 `；EOL ` RVA 0x34891C10 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e2bdf75d04d89e48](../../evidence/conditions-sets-087.md#c-e2bdf75d04d89e48) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019306

```text
(exec)# do-exec show ip ospf max-metric <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 10 `；EOL ` RVA 0x34879EC8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e2bdf75d04d89e48](../../evidence/conditions-sets-087.md#c-e2bdf75d04d89e48) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019271

```text
(exec)# do-exec show ip ospf maxage-list <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 9 `；EOL ` RVA 0x3487A410 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e2bdf75d04d89e48](../../evidence/conditions-sets-087.md#c-e2bdf75d04d89e48) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-024315

```text
(exec)# do-exec show ip ospf mpls traffic-eng link <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 61 `；EOL ` RVA 0x3488F830 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e2bdf75d04d89e48](../../evidence/conditions-sets-087.md#c-e2bdf75d04d89e48) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-68144bcdeac2712c](../../evidence/state_effects-sets-022.md#s-68144bcdeac2712c)

### path-019102

```text
(exec)# do-exec show ip ospf multi-area <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 68 `；EOL ` RVA 0x348775F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1b3359216e563a7c](../../evidence/conditions-sets-011.md#c-1b3359216e563a7c) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019134

```text
(exec)# do-exec show ip ospf nsf <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 14 `；EOL ` RVA 0x34877900 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e2bdf75d04d89e48](../../evidence/conditions-sets-087.md#c-e2bdf75d04d89e48) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019389

```text
(exec)# do-exec show ip ospf nsr <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 20 `；EOL ` RVA 0x33FC8EF0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e2bdf75d04d89e48](../../evidence/conditions-sets-087.md#c-e2bdf75d04d89e48) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022580

```text
(exec)# do-exec show ip ospf nsr objects <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 21 `；EOL ` RVA 0x33FC8C20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e2bdf75d04d89e48](../../evidence/conditions-sets-087.md#c-e2bdf75d04d89e48) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022602

```text
(exec)# do-exec show ip ospf nsr statistics <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 22 `；EOL ` RVA 0x33FC8EC8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e2bdf75d04d89e48](../../evidence/conditions-sets-087.md#c-e2bdf75d04d89e48) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019341

```text
(exec)# do-exec show ip ospf rib <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 19 `；EOL ` RVA 0x34879088 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2b9c1ae9fb507ea7](../../evidence/conditions-sets-017.md#c-2b9c1ae9fb507ea7) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019342

```text
(exec)# do-exec show ip ospf rib <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 18 `；EOL ` RVA 0x34879308 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f699ed62843313b6](../../evidence/conditions-sets-095.md#c-f699ed62843313b6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019055

```text
(exec)# do-exec show ip ospf sham-links <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 6 `；EOL ` RVA 0x34877308 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019311

```text
(exec)# do-exec show ip ospf statistics <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 11 `；EOL ` RVA 0x34879890 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e2bdf75d04d89e48](../../evidence/conditions-sets-087.md#c-e2bdf75d04d89e48) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019213

```text
(exec)# do-exec show ip ospf summary-address <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 8 `；EOL ` RVA 0x34878228 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e2bdf75d04d89e48](../../evidence/conditions-sets-087.md#c-e2bdf75d04d89e48) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022398

```text
(exec)# do-exec show ip ospf timers lsa-group <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 12 `；EOL ` RVA 0x34877C08 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e2bdf75d04d89e48](../../evidence/conditions-sets-087.md#c-e2bdf75d04d89e48) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022422

```text
(exec)# do-exec show ip ospf timers rate-limit <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 13 `；EOL ` RVA 0x34877EB0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e2bdf75d04d89e48](../../evidence/conditions-sets-087.md#c-e2bdf75d04d89e48) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019340

```text
(exec)# do-exec show ip ospf topology-info <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 15 `；EOL ` RVA 0x3487A778 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e2bdf75d04d89e48](../../evidence/conditions-sets-087.md#c-e2bdf75d04d89e48) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019087

```text
(exec)# do-exec show ip ospf virtual-links <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 5 `；EOL ` RVA 0x34876DC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-018909

```text
(exec)# do-exec show ip pim autorp <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 46 `；EOL ` RVA 0x34753198 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3704729e48e38e9e](../../evidence/conditions-sets-021.md#c-3704729e48e38e9e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-018944

```text
(exec)# do-exec show ip pim bsr-router <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 20 `；EOL ` RVA 0x34753440 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3704729e48e38e9e](../../evidence/conditions-sets-021.md#c-3704729e48e38e9e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019202

```text
(exec)# do-exec show ip pim gir <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 87 `；EOL ` RVA 0x34756200 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ce96bb5284c01d1b](../../evidence/conditions-sets-080.md#c-ce96bb5284c01d1b) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019415

```text
(exec)# do-exec show ip pim mdt <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 0 `；EOL ` RVA 0x3478DCC8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-cebace0dbd709755](../../evidence/conditions-sets-080.md#c-cebace0dbd709755) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3b5ba7d9867a0c1f](../../evidence/state_effects-sets-013.md#s-3b5ba7d9867a0c1f)

### path-022654

```text
(exec)# do-exec show ip pim mdt bgp <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 1 `；EOL ` RVA 0x3478BB78 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-cebace0dbd709755](../../evidence/conditions-sets-080.md#c-cebace0dbd709755) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3b5ba7d9867a0c1f](../../evidence/state_effects-sets-013.md#s-3b5ba7d9867a0c1f)

### path-024312

```text
(exec)# do-exec show ip pim mdt bgp c-mroutes <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 6 `；EOL ` RVA 0x3478B838 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e6a5239a8b5178ac](../../evidence/conditions-sets-089.md#c-e6a5239a8b5178ac) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-8a36b4de3e988064](../../evidence/state_effects-sets-029.md#s-8a36b4de3e988064)

### path-024862

```text
(exec)# do-exec show ip pim mdt history interval <number:1..71582> <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 2 `；EOL ` RVA 0x3478B440 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` in minutes, maximum is 71582 minutes (7 weeks)。

[条件 C-cebace0dbd709755](../../evidence/conditions-sets-080.md#c-cebace0dbd709755) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-e84d14ee7ea2ba12](../../evidence/parameters-sets-017.md#p-e84d14ee7ea2ba12) · [状态效果 S-3b5ba7d9867a0c1f](../../evidence/state_effects-sets-013.md#s-3b5ba7d9867a0c1f)

### path-024316

```text
(exec)# do-exec show ip pim mdt internal bier <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 10 `；EOL ` RVA 0x3478C440 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-569f850f86fa2022](../../evidence/conditions-sets-034.md#c-569f850f86fa2022) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3b5ba7d9867a0c1f](../../evidence/state_effects-sets-013.md#s-3b5ba7d9867a0c1f)

### path-024328

```text
(exec)# do-exec show ip pim mdt internal crt <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 11 `；EOL ` RVA 0x3478CEE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-58ee3c52929f8ea3](../../evidence/conditions-sets-035.md#c-58ee3c52929f8ea3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3b5ba7d9867a0c1f](../../evidence/state_effects-sets-013.md#s-3b5ba7d9867a0c1f)

### path-024311

```text
(exec)# do-exec show ip pim mdt internal gre <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 7 `；EOL ` RVA 0x3478C198 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7ec3d6e0a578a4fe](../../evidence/conditions-sets-049.md#c-7ec3d6e0a578a4fe) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3b5ba7d9867a0c1f](../../evidence/state_effects-sets-013.md#s-3b5ba7d9867a0c1f)

### path-024319

```text
(exec)# do-exec show ip pim mdt internal ir <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 9 `；EOL ` RVA 0x3478C6E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f7dc1a8cf35506de](../../evidence/conditions-sets-096.md#c-f7dc1a8cf35506de) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3b5ba7d9867a0c1f](../../evidence/state_effects-sets-013.md#s-3b5ba7d9867a0c1f)

### path-024321

```text
(exec)# do-exec show ip pim mdt internal leaf-ad <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 15 `；EOL ` RVA 0x3478C990 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b11f70c10deefc58](../../evidence/conditions-sets-068.md#c-b11f70c10deefc58) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3b5ba7d9867a0c1f](../../evidence/state_effects-sets-013.md#s-3b5ba7d9867a0c1f)

### path-024324

```text
(exec)# do-exec show ip pim mdt internal mldp <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 8 `；EOL ` RVA 0x3478CC38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9453f6b2fcd7239c](../../evidence/conditions-sets-057.md#c-9453f6b2fcd7239c) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3b5ba7d9867a0c1f](../../evidence/state_effects-sets-013.md#s-3b5ba7d9867a0c1f)

### path-024346

```text
(exec)# do-exec show ip pim mdt internal pe <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 12 `；EOL ` RVA 0x3478D498 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e3ca488222807f62](../../evidence/conditions-sets-088.md#c-e3ca488222807f62) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3b5ba7d9867a0c1f](../../evidence/state_effects-sets-013.md#s-3b5ba7d9867a0c1f)

### path-024870

```text
(exec)# do-exec show ip pim mdt internal pe all <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 14 `；EOL ` RVA 0x3478D740 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-345401d56829090e](../../evidence/conditions-sets-020.md#c-345401d56829090e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3b5ba7d9867a0c1f](../../evidence/state_effects-sets-013.md#s-3b5ba7d9867a0c1f)

### path-024334

```text
(exec)# do-exec show ip pim mdt internal replication <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 16 `；EOL ` RVA 0x3478D188 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-40847ec47738af2d](../../evidence/conditions-sets-025.md#c-40847ec47738af2d) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3b5ba7d9867a0c1f](../../evidence/state_effects-sets-013.md#s-3b5ba7d9867a0c1f)

### path-024344

```text
(exec)# do-exec show ip pim mdt internal tdb <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 13 `；EOL ` RVA 0x3478D9D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e0b68bae7bdef907](../../evidence/conditions-sets-086.md#c-e0b68bae7bdef907) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3b5ba7d9867a0c1f](../../evidence/state_effects-sets-013.md#s-3b5ba7d9867a0c1f)

### path-024304

```text
(exec)# do-exec show ip pim mdt internal vxlan <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 24 `；EOL ` RVA 0x3478BEF0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-cea9280e3f95214b](../../evidence/conditions-sets-080.md#c-cea9280e3f95214b) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3b5ba7d9867a0c1f](../../evidence/state_effects-sets-013.md#s-3b5ba7d9867a0c1f)

### path-022591

```text
(exec)# do-exec show ip pim mdt receive <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 3 `；EOL ` RVA 0x3478AEC8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-cebace0dbd709755](../../evidence/conditions-sets-080.md#c-cebace0dbd709755) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3b5ba7d9867a0c1f](../../evidence/state_effects-sets-013.md#s-3b5ba7d9867a0c1f)

### path-024293

```text
(exec)# do-exec show ip pim mdt receive detail <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 4 `；EOL ` RVA 0x3478AEA0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-cebace0dbd709755](../../evidence/conditions-sets-080.md#c-cebace0dbd709755) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3b5ba7d9867a0c1f](../../evidence/state_effects-sets-013.md#s-3b5ba7d9867a0c1f)

### path-022561

```text
(exec)# do-exec show ip pim mdt send <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 5 `；EOL ` RVA 0x3478AB90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-cebace0dbd709755](../../evidence/conditions-sets-080.md#c-cebace0dbd709755) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3b5ba7d9867a0c1f](../../evidence/state_effects-sets-013.md#s-3b5ba7d9867a0c1f)

### path-019189

```text
(exec)# do-exec show ip pim mvpn <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 52 `；EOL ` RVA 0x34752B10 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3704729e48e38e9e](../../evidence/conditions-sets-021.md#c-3704729e48e38e9e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022408

```text
(exec)# do-exec show ip pim mvpn bier <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 89 `；EOL ` RVA 0x34752840 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3704729e48e38e9e](../../evidence/conditions-sets-021.md#c-3704729e48e38e9e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022285

```text
(exec)# do-exec show ip pim mvpn crt <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 70 `；EOL ` RVA 0x34751850 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3704729e48e38e9e](../../evidence/conditions-sets-021.md#c-3704729e48e38e9e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022387

```text
(exec)# do-exec show ip pim mvpn gre <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 90 `；EOL ` RVA 0x34752598 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3704729e48e38e9e](../../evidence/conditions-sets-021.md#c-3704729e48e38e9e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022371

```text
(exec)# do-exec show ip pim mvpn ir <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 91 `；EOL ` RVA 0x347522F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3704729e48e38e9e](../../evidence/conditions-sets-021.md#c-3704729e48e38e9e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022331

```text
(exec)# do-exec show ip pim mvpn leaf-ad <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 92 `；EOL ` RVA 0x34751DA0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3704729e48e38e9e](../../evidence/conditions-sets-021.md#c-3704729e48e38e9e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022231

```text
(exec)# do-exec show ip pim mvpn mldp <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 68 `；EOL ` RVA 0x34751300 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3704729e48e38e9e](../../evidence/conditions-sets-021.md#c-3704729e48e38e9e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022254

```text
(exec)# do-exec show ip pim mvpn pe <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 69 `；EOL ` RVA 0x347515A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3704729e48e38e9e](../../evidence/conditions-sets-021.md#c-3704729e48e38e9e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022308

```text
(exec)# do-exec show ip pim mvpn replication <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 93 `；EOL ` RVA 0x34751AF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3704729e48e38e9e](../../evidence/conditions-sets-021.md#c-3704729e48e38e9e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022353

```text
(exec)# do-exec show ip pim mvpn srv6 <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 97 `；EOL ` RVA 0x34752048 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3704729e48e38e9e](../../evidence/conditions-sets-021.md#c-3704729e48e38e9e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022431

```text
(exec)# do-exec show ip pim mvpn tdb <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 94 `；EOL ` RVA 0x34752AE8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3704729e48e38e9e](../../evidence/conditions-sets-021.md#c-3704729e48e38e9e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022209

```text
(exec)# do-exec show ip pim mvpn vxlan <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 95 `；EOL ` RVA 0x34751058 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3704729e48e38e9e](../../evidence/conditions-sets-021.md#c-3704729e48e38e9e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022324

```text
(exec)# do-exec show ip pim pfp-sa announcements <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 83 `；EOL ` RVA 0x34753790 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4beb10443808ceb9](../../evidence/conditions-sets-030.md#c-4beb10443808ceb9) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022369

```text
(exec)# do-exec show ip pim pfp-sa cache <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 86 `；EOL ` RVA 0x34753CE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4beb10443808ceb9](../../evidence/conditions-sets-030.md#c-4beb10443808ceb9) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022349

```text
(exec)# do-exec show ip pim pfp-sa originator <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 84 `；EOL ` RVA 0x34753A38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4beb10443808ceb9](../../evidence/conditions-sets-030.md#c-4beb10443808ceb9) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019186

```text
(exec)# do-exec show ip pim rp <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 11 `；EOL ` RVA 0x34754BB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-61b5669da132f85e](../../evidence/conditions-sets-038.md#c-61b5669da132f85e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022378

```text
(exec)# do-exec show ip pim rp-hash <address> <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 22 `；EOL ` RVA 0x34754FF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` group address。

[条件 C-4c782013125a0eb7](../../evidence/conditions-sets-030.md#c-4c782013125a0eb7) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-c66d3e1e0ed7b695](../../evidence/parameters-sets-015.md#p-c66d3e1e0ed7b695) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-014850

```text
(exec)# do-exec show ip policy <cr>
```

Handler ` RVA 0xFAD9620 `；selector ` 0 `；EOL ` RVA 0x34804A80 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019094

```text
(exec)# do-exec show ip policy adj-subblock <cr>
```

Handler ` RVA 0xFAD9440 `；selector ` 0 `；EOL ` RVA 0x34804A58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-014537

```text
(exec)# do-exec show ip policy-list <cr>
```

Handler ` RVA 0xE218540 `；selector ` 0 `；EOL ` RVA 0x344BABE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-024820

```text
(exec)# do-exec show ip portbundle ip <address> bundle <number:1..65535> <cr>
```

Handler ` RVA 0x11C31540 `；selector ` 0 `；EOL ` RVA 0x356A5148 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Portbundle IP address；` unsigned_number ` Portbundle bundle number。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-81af61e5ba4224a6](../../evidence/parameters-sets-010.md#p-81af61e5ba4224a6) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-018438

```text
(exec)# do-exec show ip portbundle status <cr>
```

Handler ` RVA 0x11C31540 `；selector ` 1 `；EOL ` RVA 0x356A4DE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-021993

```text
(exec)# do-exec show ip portbundle status free <cr>
```

Handler ` RVA 0x11C31540 `；selector ` 2 `；EOL ` RVA 0x356A4B28 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-75262befd1ee2174](../../evidence/state_effects-sets-025.md#s-75262befd1ee2174)

### path-018504

```text
(exec)# do-exec show ip ports all <cr>
```

Handler ` RVA 0xCE51730 `；selector ` 0 `；EOL ` RVA 0x33CF6FA8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-018477

```text
(exec)# do-exec show ip ports ephemeral-max <cr>
```

Handler ` RVA 0xCDEFA80 `；selector ` 0 `；EOL ` RVA 0x33CF6D00 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-018532

```text
(exec)# do-exec show ip ports reservation <cr>
```

Handler ` RVA 0xCE518D0 `；selector ` 0 `；EOL ` RVA 0x33CF7250 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c005c5fcde583d9f](../../evidence/conditions-sets-074.md#c-c005c5fcde583d9f) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-015023

```text
(exec)# do-exec show ip prefix-list <cr>
```

Handler ` RVA 0xE2203B0 `；selector ` 0 `；EOL ` RVA 0x342832B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-88a2248132632179](../../evidence/conditions-sets-053.md#c-88a2248132632179) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3f6c20a925041212](../../evidence/state_effects-sets-014.md#s-3f6c20a925041212)

### path-024310

```text
(exec)# do-exec show ip prefix-list <string> seq <number:1..4294967295> <cr>
```

Handler ` RVA 0xE2203B0 `；selector ` 3 `；EOL ` RVA 0x34283358 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Name of a prefix list；` unsigned_number ` Sequence number。

[条件 C-88a2248132632179](../../evidence/conditions-sets-053.md#c-88a2248132632179) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-0d71bd8044f6fc2b](../../evidence/parameters-sets-001.md#p-0d71bd8044f6fc2b) · [状态效果 S-3f6c20a925041212](../../evidence/state_effects-sets-014.md#s-3f6c20a925041212)

### path-019385

```text
(exec)# do-exec show ip prefix-list detail <cr>
```

Handler ` RVA 0xE2203B0 `；selector ` 2 `；EOL ` RVA 0x34282FB0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3f6c20a925041212](../../evidence/state_effects-sets-014.md#s-3f6c20a925041212)

### path-019374

```text
(exec)# do-exec show ip prefix-list summary <cr>
```

Handler ` RVA 0xE2203B0 `；selector ` 1 `；EOL ` RVA 0x34282CA0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3f6c20a925041212](../../evidence/state_effects-sets-014.md#s-3f6c20a925041212)

### path-014554

```text
(exec)# do-exec show ip protocols <cr>
```

Handler ` RVA 0xE1F60E0 `；selector ` 0 `；EOL ` RVA 0x3422FAB0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-44f485a1fcd2161c](../../evidence/conditions-sets-027.md#c-44f485a1fcd2161c) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d312e8dfbf261b4a](../../evidence/state_effects-sets-045.md#s-d312e8dfbf261b4a)

### path-018584

```text
(exec)# do-exec show ip protocols summary <cr>
```

Handler ` RVA 0xE1F5DF0 `；selector ` 0 `；EOL ` RVA 0x3422FA88 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-44f485a1fcd2161c](../../evidence/conditions-sets-027.md#c-44f485a1fcd2161c) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d312e8dfbf261b4a](../../evidence/state_effects-sets-045.md#s-d312e8dfbf261b4a)

### path-014123

```text
(exec)# do-exec show ip redirects <cr>
```

Handler ` RVA 0xCF509C0 `；selector ` 0 `；EOL ` RVA 0x33D31570 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-018616

```text
(exec)# do-exec show ip rib database <cr>
```

Handler ` RVA 0xDC0B310 `；selector ` 1 `；EOL ` RVA 0x3422F578 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e9fa81fb0d1adae9](../../evidence/conditions-sets-090.md#c-e9fa81fb0d1adae9) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-9dc0e84618e9a387](../../evidence/state_effects-sets-034.md#s-9dc0e84618e9a387)

### path-019212

```text
(exec)# do-exec show ip rip database <cr>
```

Handler ` RVA 0xFB73AB0 `；selector ` 0 `；EOL ` RVA 0x34822820 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-265b4c12aa8f3553](../../evidence/conditions-sets-015.md#c-265b4c12aa8f3553) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019198

```text
(exec)# do-exec show ip rip neighbors <cr>
```

Handler ` RVA 0xFB52AC0 `；selector ` 0 `；EOL ` RVA 0x34822B40 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a4cf46f000210ac4](../../evidence/conditions-sets-064.md#c-a4cf46f000210ac4) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019119

```text
(exec)# do-exec show ip rip timers <cr>
```

Handler ` RVA 0xFB56CB0 `；selector ` 0 `；EOL ` RVA 0x34822428 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022119

```text
(exec)# do-exec show ip route list <number:1..199> <cr>
```

Handler ` RVA 0xE1CEA80 `；selector ` 12 `；EOL ` RVA 0x34230C38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` IP access list number。

[条件 C-6a197f9d2cce68e9](../../evidence/conditions-sets-041.md#c-6a197f9d2cce68e9) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-6f46a0106e78d96b](../../evidence/parameters-sets-009.md#p-6f46a0106e78d96b) · [状态效果 S-37eeb64e21d551e2](../../evidence/state_effects-sets-012.md#s-37eeb64e21d551e2)

### path-022156

```text
(exec)# do-exec show ip route omp-tag <number:0..4294967295> <cr>
```

Handler ` RVA 0xE1CEA80 `；selector ` 15 `；EOL ` RVA 0x34231420 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Overlay Management Protocol (OMP) Tag value。

[条件 C-1029b62c92a1bba7](../../evidence/conditions-sets-006.md#c-1029b62c92a1bba7) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-1586b2be9da07e52](../../evidence/parameters-sets-002.md#p-1586b2be9da07e52) · [状态效果 S-37eeb64e21d551e2](../../evidence/state_effects-sets-012.md#s-37eeb64e21d551e2)

### path-022155

```text
(exec)# do-exec show ip route tag <number:0..4294967295> <cr>
```

Handler ` RVA 0xE1CEA80 `；selector ` 14 `；EOL ` RVA 0x34231000 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Tag value。

[条件 C-a81cf38b82e83ad7](../../evidence/conditions-sets-065.md#c-a81cf38b82e83ad7) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-e0210763947c7838](../../evidence/parameters-sets-017.md#p-e0210763947c7838) · [状态效果 S-37eeb64e21d551e2](../../evidence/state_effects-sets-012.md#s-37eeb64e21d551e2)

### path-024102

```text
(exec)# do-exec show ip route tree <address> <address> <cr>
```

Handler ` RVA 0xE1CEA80 `；selector ` 3 `；EOL ` RVA 0x34230700 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Network to display information about；` address ` Network mask。

[条件 C-6a197f9d2cce68e9](../../evidence/conditions-sets-041.md#c-6a197f9d2cce68e9) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-3c5f288fee4ae5f4](../../evidence/parameters-sets-005.md#p-3c5f288fee4ae5f4) · [状态效果 S-37eeb64e21d551e2](../../evidence/state_effects-sets-012.md#s-37eeb64e21d551e2)

### path-018698

```text
(exec)# do-exec show ip route tree <cr>
```

Handler ` RVA 0xE1CEA80 `；selector ` 1 `；EOL ` RVA 0x342306C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6a197f9d2cce68e9](../../evidence/conditions-sets-041.md#c-6a197f9d2cce68e9) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-37eeb64e21d551e2](../../evidence/state_effects-sets-012.md#s-37eeb64e21d551e2)

### path-022105

```text
(exec)# do-exec show ip route tree summary <cr>
```

Handler ` RVA 0xE1CEA80 `；selector ` 2 `；EOL ` RVA 0x342303F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6a197f9d2cce68e9](../../evidence/conditions-sets-041.md#c-6a197f9d2cce68e9) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-37eeb64e21d551e2](../../evidence/state_effects-sets-012.md#s-37eeb64e21d551e2)

### path-018789

```text
(exec)# do-exec show ip rpf queued <cr>
```

Handler ` RVA 0xF740240 `；selector ` 0 `；EOL ` RVA 0x34750190 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3704729e48e38e9e](../../evidence/conditions-sets-021.md#c-3704729e48e38e9e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-f038e7c1e0b2d476](../../evidence/state_effects-sets-051.md#s-f038e7c1e0b2d476)

### path-015208

```text
(exec)# do-exec show ip rsvp <cr>
```

Handler ` RVA 0x10073190 `；selector ` 0 `；EOL ` RVA 0x34A3A428 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3da5c90fec893b04](../../evidence/conditions-sets-024.md#c-3da5c90fec893b04) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022565

```text
(exec)# do-exec show ip rsvp aggregation ip <cr>
```

Handler ` RVA 0x101C49F0 `；selector ` 0 `；EOL ` RVA 0x34A69C90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-024307

```text
(exec)# do-exec show ip rsvp aggregation ip endpoints <cr>
```

Handler ` RVA 0x101C42E0 `；selector ` 0 `；EOL ` RVA 0x34A69F58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-024278

```text
(exec)# do-exec show ip rsvp aggregation ip map <cr>
```

Handler ` RVA 0x101C3C20 `；selector ` 0 `；EOL ` RVA 0x34A691B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-024284

```text
(exec)# do-exec show ip rsvp aggregation ip reservation <cr>
```

Handler ` RVA 0x101C3DE0 `；selector ` 0 `；EOL ` RVA 0x34A694F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019310

```text
(exec)# do-exec show ip rsvp authentication <cr>
```

Handler ` RVA 0x10073FB0 `；selector ` 0 `；EOL ` RVA 0x34A2FFA8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2c3c055753ffd7df](../../evidence/conditions-sets-017.md#c-2c3c055753ffd7df) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019561

```text
(exec)# do-exec show ip rsvp counters <cr>
```

Handler ` RVA 0x100B61F0 `；selector ` 0 `；EOL ` RVA 0x34A35FE8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3d421029802e57df](../../evidence/conditions-sets-024.md#c-3d421029802e57df) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-abb2be437bc454a4](../../evidence/state_effects-sets-036.md#s-abb2be437bc454a4)

### path-019469

```text
(exec)# do-exec show ip rsvp handles <cr>
```

Handler ` RVA 0x10070450 `；selector ` 0 `；EOL ` RVA 0x34A34000 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4c38057bdf21f780](../../evidence/conditions-sets-030.md#c-4c38057bdf21f780) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-672610f096677e46](../../evidence/state_effects-sets-022.md#s-672610f096677e46)

### path-019587

```text
(exec)# do-exec show ip rsvp hello <cr>
```

Handler ` RVA 0x10072260 `；selector ` 0 `；EOL ` RVA 0x34A38728 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e2f8ef65d50037b1](../../evidence/conditions-sets-087.md#c-e2f8ef65d50037b1) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-024378

```text
(exec)# do-exec show ip rsvp hello bfd nbr <cr>
```

Handler ` RVA 0x10076740 `；selector ` 0 `；EOL ` RVA 0x34A37650 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7df6317d844a4a33](../../evidence/conditions-sets-049.md#c-7df6317d844a4a33) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-024881

```text
(exec)# do-exec show ip rsvp hello bfd nbr detail <cr>
```

Handler ` RVA 0x10076940 `；selector ` 0 `；EOL ` RVA 0x34A37348 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7df6317d844a4a33](../../evidence/conditions-sets-049.md#c-7df6317d844a4a33) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-024884

```text
(exec)# do-exec show ip rsvp hello client lsp detail <cr>
```

Handler ` RVA 0x10076EA0 `；selector ` 0 `；EOL ` RVA 0x34A38108 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-74faadc013aa600c](../../evidence/conditions-sets-045.md#c-74faadc013aa600c) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-024883

```text
(exec)# do-exec show ip rsvp hello client lsp summary <cr>
```

Handler ` RVA 0x10076D20 `；selector ` 0 `；EOL ` RVA 0x34A38410 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-74faadc013aa600c](../../evidence/conditions-sets-045.md#c-74faadc013aa600c) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-024381

```text
(exec)# do-exec show ip rsvp hello client nbr <cr>
```

Handler ` RVA 0x10076A40 `；selector ` 0 `；EOL ` RVA 0x34A37DA0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-74faadc013aa600c](../../evidence/conditions-sets-045.md#c-74faadc013aa600c) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-024882

```text
(exec)# do-exec show ip rsvp hello client nbr detail <cr>
```

Handler ` RVA 0x10076C10 `；selector ` 0 `；EOL ` RVA 0x34A37A98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-74faadc013aa600c](../../evidence/conditions-sets-045.md#c-74faadc013aa600c) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022757

```text
(exec)# do-exec show ip rsvp hello graceful-restart <cr>
```

Handler ` RVA 0x10073050 `；selector ` 0 `；EOL ` RVA 0x34A38700 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ef5ed1a666ba4748](../../evidence/conditions-sets-092.md#c-ef5ed1a666ba4748) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-024366

```text
(exec)# do-exec show ip rsvp hello instance internal <cr>
```

Handler ` RVA 0x10076620 `；selector ` 0 `；EOL ` RVA 0x34A368E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-692987fefc2d91e8](../../evidence/conditions-sets-041.md#c-692987fefc2d91e8) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-06f2cf717b513414](../../evidence/state_effects-sets-002.md#s-06f2cf717b513414)

### path-024370

```text
(exec)# do-exec show ip rsvp hello instance summary <cr>
```

Handler ` RVA 0x10076290 `；selector ` 0 `；EOL ` RVA 0x34A36C40 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-692987fefc2d91e8](../../evidence/conditions-sets-041.md#c-692987fefc2d91e8) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022727

```text
(exec)# do-exec show ip rsvp hello statistics <cr>
```

Handler ` RVA 0x100761D0 `；selector ` 0 `；EOL ` RVA 0x34A36F28 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-76d6906fdad99132](../../evidence/conditions-sets-046.md#c-76d6906fdad99132) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022732

```text
(exec)# do-exec show ip rsvp host receivers <cr>
```

Handler ` RVA 0x1006D010 `；selector ` 0 `；EOL ` RVA 0x34A35B98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3d421029802e57df](../../evidence/conditions-sets-024.md#c-3d421029802e57df) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-9c81b788d38fcd1f](../../evidence/state_effects-sets-033.md#s-9c81b788d38fcd1f)

### path-022721

```text
(exec)# do-exec show ip rsvp host senders <cr>
```

Handler ` RVA 0x1006D750 `；selector ` 0 `；EOL ` RVA 0x34A358A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3d421029802e57df](../../evidence/conditions-sets-024.md#c-3d421029802e57df) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-c94f2f500c2f3457](../../evidence/state_effects-sets-043.md#s-c94f2f500c2f3457)

### path-022733

```text
(exec)# do-exec show ip rsvp listeners <address> <cr>
```

Handler ` RVA 0x1006F480 `；selector ` 6 `；EOL ` RVA 0x34A35008 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Destination address。

[条件 C-3d421029802e57df](../../evidence/conditions-sets-024.md#c-3d421029802e57df) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-559a5e35800d3230](../../evidence/parameters-sets-007.md#p-559a5e35800d3230) · [状态效果 S-bec3e85018a8bfde](../../evidence/state_effects-sets-040.md#s-bec3e85018a8bfde)

### path-024362

```text
(exec)# do-exec show ip rsvp listeners <address> <number:0..255> <cr>
```

Handler ` RVA 0x1006F480 `；selector ` 4 `；EOL ` RVA 0x34A34CC8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Destination address；` unsigned_number ` IP Protocol。

[条件 C-3d421029802e57df](../../evidence/conditions-sets-024.md#c-3d421029802e57df) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-c1d702e7762de23b](../../evidence/parameters-sets-015.md#p-c1d702e7762de23b) · [状态效果 S-bec3e85018a8bfde](../../evidence/state_effects-sets-040.md#s-bec3e85018a8bfde)

### path-024871

```text
(exec)# do-exec show ip rsvp listeners <address> <number:0..255> <number:0..65535> <cr>
```

Handler ` RVA 0x1006F480 `；selector ` 0 `；EOL ` RVA 0x34A34A18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Destination address；` unsigned_number ` IP Protocol；` unsigned_number ` Destination port。

[条件 C-3d421029802e57df](../../evidence/conditions-sets-024.md#c-3d421029802e57df) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-eeed49378aa0252c](../../evidence/parameters-sets-018.md#p-eeed49378aa0252c) · [状态效果 S-bec3e85018a8bfde](../../evidence/state_effects-sets-040.md#s-bec3e85018a8bfde)

### path-019526

```text
(exec)# do-exec show ip rsvp listeners <cr>
```

Handler ` RVA 0x1006F480 `；selector ` 7 `；EOL ` RVA 0x34A352C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3d421029802e57df](../../evidence/conditions-sets-024.md#c-3d421029802e57df) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-bec3e85018a8bfde](../../evidence/state_effects-sets-040.md#s-bec3e85018a8bfde)

### path-019402

```text
(exec)# do-exec show ip rsvp metadata <cr>
```

Handler ` RVA 0x10069BC0 `；selector ` 0 `；EOL ` RVA 0x34A32250 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2c3c055753ffd7df](../../evidence/conditions-sets-017.md#c-2c3c055753ffd7df) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-188054d5950e9a8f](../../evidence/state_effects-sets-006.md#s-188054d5950e9a8f)

### path-019378

```text
(exec)# do-exec show ip rsvp neighbor <cr>
```

Handler ` RVA 0x1006DCE0 `；selector ` 0 `；EOL ` RVA 0x34A309B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2c3c055753ffd7df](../../evidence/conditions-sets-017.md#c-2c3c055753ffd7df) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-02c72299981548cb](../../evidence/state_effects-sets-001.md#s-02c72299981548cb)

### path-022589

```text
(exec)# do-exec show ip rsvp neighbor queues <cr>
```

Handler ` RVA 0x1006DB00 `；selector ` 0 `；EOL ` RVA 0x34A30C70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d435423850cf954c](../../evidence/conditions-sets-082.md#c-d435423850cf954c) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-02c72299981548cb](../../evidence/state_effects-sets-001.md#s-02c72299981548cb)

### path-022486

```text
(exec)# do-exec show ip rsvp nsr counters <cr>
```

Handler ` RVA 0x100723C0 `；selector ` 0 `；EOL ` RVA 0x34A2FBB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-494c6a7983e46592](../../evidence/conditions-sets-029.md#c-494c6a7983e46592) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022725

```text
(exec)# do-exec show ip rsvp p2mp counters <cr>
```

Handler ` RVA 0x101A72E0 `；selector ` 0 `；EOL ` RVA 0x34A3A468 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7604b9b3a99a26db](../../evidence/conditions-sets-046.md#c-7604b9b3a99a26db) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019282

```text
(exec)# do-exec show ip rsvp policy <cr>
```

Handler ` RVA 0x10113110 `；selector ` 0 `；EOL ` RVA 0x34A40A60 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7c293d3779bede94](../../evidence/conditions-sets-048.md#c-7c293d3779bede94) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-e796a86d02303146](../../evidence/state_effects-sets-049.md#s-e796a86d02303146)

### path-022548

```text
(exec)# do-exec show ip rsvp policy cops <cr>
```

Handler ` RVA 0x10113110 `；selector ` 8 `；EOL ` RVA 0x34A40AA0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5327ead3e239c79d](../../evidence/conditions-sets-033.md#c-5327ead3e239c79d) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-e796a86d02303146](../../evidence/state_effects-sets-049.md#s-e796a86d02303146)

### path-022498

```text
(exec)# do-exec show ip rsvp policy identity <cr>
```

Handler ` RVA 0x10112D90 `；selector ` 0 `；EOL ` RVA 0x34A40020 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-e796a86d02303146](../../evidence/state_effects-sets-049.md#s-e796a86d02303146)

### path-019405

```text
(exec)# do-exec show ip rsvp sender <cr>
```

Handler ` RVA 0x10069BC0 `；selector ` 0 `；EOL ` RVA 0x34A315A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2c3c055753ffd7df](../../evidence/conditions-sets-017.md#c-2c3c055753ffd7df) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-8a3d1b83e0d3ba35](../../evidence/state_effects-sets-029.md#s-8a3d1b83e0d3ba35)

### path-022782

```text
(exec)# do-exec show ip rsvp signalling blockade <cr>
```

Handler ` RVA 0x10067C20 `；selector ` 0 `；EOL ` RVA 0x34A3A0B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-be699b557581bc06](../../evidence/conditions-sets-073.md#c-be699b557581bc06) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-276bbe924d732657](../../evidence/state_effects-sets-009.md#s-276bbe924d732657)

### path-022719

```text
(exec)# do-exec show ip rsvp signalling fast-local-repair <cr>
```

Handler ` RVA 0x100713E0 `；selector ` 0 `；EOL ` RVA 0x34A38D20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-31bbd11c2e970ff0](../../evidence/conditions-sets-019.md#c-31bbd11c2e970ff0) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022716

```text
(exec)# do-exec show ip rsvp signalling rate-limit <cr>
```

Handler ` RVA 0x100712D0 `；selector ` 0 `；EOL ` RVA 0x34A38FF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-31bbd11c2e970ff0](../../evidence/conditions-sets-019.md#c-31bbd11c2e970ff0) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-024374

```text
(exec)# do-exec show ip rsvp signalling refresh interval <cr>
```

Handler ` RVA 0x10071130 `；selector ` 0 `；EOL ` RVA 0x34A39858 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-31bbd11c2e970ff0](../../evidence/conditions-sets-019.md#c-31bbd11c2e970ff0) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-024376

```text
(exec)# do-exec show ip rsvp signalling refresh misses <cr>
```

Handler ` RVA 0x100711A0 `；selector ` 0 `；EOL ` RVA 0x34A39B00 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-31bbd11c2e970ff0](../../evidence/conditions-sets-019.md#c-31bbd11c2e970ff0) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-024369

```text
(exec)# do-exec show ip rsvp signalling refresh reduction <cr>
```

Handler ` RVA 0x10071210 `；selector ` 0 `；EOL ` RVA 0x34A395B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-31bbd11c2e970ff0](../../evidence/conditions-sets-019.md#c-31bbd11c2e970ff0) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022728

```text
(exec)# do-exec show ip rsvp signalling session-timers <cr>
```

Handler ` RVA 0x10072130 `；selector ` 0 `；EOL ` RVA 0x34A392A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-31bbd11c2e970ff0](../../evidence/conditions-sets-019.md#c-31bbd11c2e970ff0) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022571

```text
(exec)# do-exec show ip rsvp transport clients <cr>
```

Handler ` RVA 0x10069BC0 `；selector ` 0 `；EOL ` RVA 0x34A31E80 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2c3c055753ffd7df](../../evidence/conditions-sets-017.md#c-2c3c055753ffd7df) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-9f6c7a78128b200c](../../evidence/state_effects-sets-034.md#s-9f6c7a78128b200c)

### path-018313

```text
(exec)# do-exec show ip rtp header-compression <cr>
```

Handler ` RVA 0xD194110 `；selector ` 0 `；EOL ` RVA 0x33DAABA0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7513642931f3ef25](../../evidence/conditions-sets-045.md#c-7513642931f3ef25) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-69c3ebce368aa96f](../../evidence/state_effects-sets-023.md#s-69c3ebce368aa96f)

### path-022255

```text
(exec)# do-exec show ip sctp association list <cr>
```

Handler ` RVA 0xCE6FC00 `；selector ` 2 `；EOL ` RVA 0x33D0DFE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-024162

```text
(exec)# do-exec show ip sctp association parameters <number:0..4294967295> <cr>
```

Handler ` RVA 0xCE6FC00 `；selector ` 3 `；EOL ` RVA 0x33D0DD58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Association ID。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-d2fce9ec1de3fa16](../../evidence/parameters-sets-016.md#p-d2fce9ec1de3fa16) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-024152

```text
(exec)# do-exec show ip sctp association statistics <number:0..4294967295> <cr>
```

Handler ` RVA 0xCE6FC00 `；selector ` 4 `；EOL ` RVA 0x33D0DA68 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Association ID。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-39686869c9f42ad0](../../evidence/parameters-sets-005.md#p-39686869c9f42ad0) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-018810

```text
(exec)# do-exec show ip sctp errors <cr>
```

Handler ` RVA 0xCE6FC00 `；selector ` 6 `；EOL ` RVA 0x33D0D6F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-018871

```text
(exec)# do-exec show ip sctp instances <cr>
```

Handler ` RVA 0xCE6FC00 `；selector ` 1 `；EOL ` RVA 0x33D0E288 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-018766

```text
(exec)# do-exec show ip sctp statistics <cr>
```

Handler ` RVA 0xCE6FC00 `；selector ` 5 `；EOL ` RVA 0x33D0D448 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-014650

```text
(exec)# do-exec show ip sdr <cr>
```

Handler ` RVA 0xF87E5A0 `；selector ` 0 `；EOL ` RVA 0x3474E828 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-172ce32b53a9055e](../../evidence/conditions-sets-009.md#c-172ce32b53a9055e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019570

```text
(exec)# do-exec show ip sla application <cr>
```

Handler ` RVA 0x102DD0E0 `；selector ` 0 `；EOL ` RVA 0x34A99F68 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019418

```text
(exec)# do-exec show ip sla authentication <cr>
```

Handler ` RVA 0x101DA830 `；selector ` 0 `；EOL ` RVA 0x34A6E750 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022711

```text
(exec)# do-exec show ip sla auto discovery <cr>
```

Handler ` RVA 0x10241B90 `；selector ` 0 `；EOL ` RVA 0x34A7ADC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022709

```text
(exec)# do-exec show ip sla auto group <cr>
```

Handler ` RVA 0x10240F70 `；selector ` 0 `；EOL ` RVA 0x34A7A360 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-6d5e37d8157e804a](../../evidence/state_effects-sets-023.md#s-6d5e37d8157e804a)

### path-022707

```text
(exec)# do-exec show ip sla auto schedule <cr>
```

Handler ` RVA 0x10241510 `；selector ` 0 `；EOL ` RVA 0x34A7A6B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-025171

```text
(exec)# do-exec show ip sla auto summary-statistics group type ip <string> <cr>
```

Handler ` RVA 0x10241ED0 `；selector ` 2 `；EOL ` RVA 0x34A7B1E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Group name。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-f84b4562b23f6845](../../evidence/parameters-sets-019.md#p-f84b4562b23f6845) · [状态效果 S-9d1ac72569545b0c](../../evidence/state_effects-sets-033.md#s-9d1ac72569545b0c)

### path-025253

```text
(exec)# do-exec show ip sla auto summary-statistics group type ip <string> ip-address <address> port <number:0..64000> <cr>
```

Handler ` RVA 0x10241ED0 `；selector ` 3 `；EOL ` RVA 0x34A7B2C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Group name；` address ` destination ip address；` unsigned_number ` destination port。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-8528621cf3b47973](../../evidence/parameters-sets-010.md#p-8528621cf3b47973) · [状态效果 S-9d1ac72569545b0c](../../evidence/state_effects-sets-033.md#s-9d1ac72569545b0c)

### path-025216

```text
(exec)# do-exec show ip sla auto summary-statistics group type ip <string> ip-address <cr>
```

Handler ` RVA 0x10241ED0 `；selector ` 1 `；EOL ` RVA 0x34A7B248 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Group name。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-f84b4562b23f6845](../../evidence/parameters-sets-019.md#p-f84b4562b23f6845) · [状态效果 S-9d1ac72569545b0c](../../evidence/state_effects-sets-033.md#s-9d1ac72569545b0c)

### path-022720

```text
(exec)# do-exec show ip sla auto template <cr>
```

Handler ` RVA 0x102415E0 `；selector ` 0 `；EOL ` RVA 0x34A7AAC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-f8a382145bafaf5a](../../evidence/state_effects-sets-053.md#s-f8a382145bafaf5a)

### path-019523

```text
(exec)# do-exec show ip sla collection-statistics <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 0 `；EOL ` RVA 0x34A97478 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019441

```text
(exec)# do-exec show ip sla configuration <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 14 `；EOL ` RVA 0x34A95AC8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019573

```text
(exec)# do-exec show ip sla distribution-statistics <cr>
```

Handler ` RVA 0x102DD820 `；selector ` 0 `；EOL ` RVA 0x34A97D28 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022726

```text
(exec)# do-exec show ip sla distribution-statistics full <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 1 `；EOL ` RVA 0x34A97A58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022715

```text
(exec)# do-exec show ip sla distribution-statistics raw <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 3 `；EOL ` RVA 0x34A977B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022739

```text
(exec)# do-exec show ip sla distribution-statistics tabular <cr>
```

Handler ` RVA 0x102DD820 `；selector ` 0 `；EOL ` RVA 0x34A97D00 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019638

```text
(exec)# do-exec show ip sla endpoint-list <cr>
```

Handler ` RVA 0x10241300 `；selector ` 0 `；EOL ` RVA 0x34A9A980 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-ec4922aa51714962](../../evidence/state_effects-sets-050.md#s-ec4922aa51714962)

### path-022731

```text
(exec)# do-exec show ip sla enhanced-history distribution-statistics <cr>
```

Handler ` RVA 0x102DD570 `；selector ` 0 `；EOL ` RVA 0x34A98318 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-8a4731b53ac598aa](../../evidence/state_effects-sets-029.md#s-8a4731b53ac598aa)

### path-022713

```text
(exec)# do-exec show ip sla ethernet-monitor configuration <cr>
```

Handler ` RVA 0x103C1120 `；selector ` 0 `；EOL ` RVA 0x34B09AE8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022694

```text
(exec)# do-exec show ip sla ethernet-monitor responder <cr>
```

Handler ` RVA 0x103C1230 `；selector ` 0 `；EOL ` RVA 0x34B09800 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019454

```text
(exec)# do-exec show ip sla event-publisher <cr>
```

Handler ` RVA 0x102759D0 `；selector ` 1 `；EOL ` RVA 0x34A890E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022665

```text
(exec)# do-exec show ip sla event-publisher detail <cr>
```

Handler ` RVA 0x102759D0 `；selector ` 2 `；EOL ` RVA 0x34A890C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022701

```text
(exec)# do-exec show ip sla group schedule <cr>
```

Handler ` RVA 0x102DD930 `；selector ` 0 `；EOL ` RVA 0x34A96958 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-024342

```text
(exec)# do-exec show ip sla group schedule details <cr>
```

Handler ` RVA 0x102DD930 `；selector ` 28 `；EOL ` RVA 0x34A96930 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019612

```text
(exec)# do-exec show ip sla history <cr>
```

Handler ` RVA 0x102DD460 `；selector ` 0 `；EOL ` RVA 0x34A98F20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022748

```text
(exec)# do-exec show ip sla history full <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 5 `；EOL ` RVA 0x34A989A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022763

```text
(exec)# do-exec show ip sla history interval-statistics <cr>
```

Handler ` RVA 0x102DDA40 `；selector ` 45 `；EOL ` RVA 0x34A98EF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022738

```text
(exec)# do-exec show ip sla history raw <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 7 `；EOL ` RVA 0x34A98700 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022756

```text
(exec)# do-exec show ip sla history tabular <cr>
```

Handler ` RVA 0x102DD460 `；selector ` 0 `；EOL ` RVA 0x34A98C50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019494

```text
(exec)# do-exec show ip sla operational-state <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 16 `；EOL ` RVA 0x34A96E98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019610

```text
(exec)# do-exec show ip sla reaction-configuration <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 17 `；EOL ` RVA 0x34A9A568 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019599

```text
(exec)# do-exec show ip sla reaction-trigger <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 12 `；EOL ` RVA 0x34A9A278 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019451

```text
(exec)# do-exec show ip sla responder <cr>
```

Handler ` RVA 0x101FD080 `；selector ` 0 `；EOL ` RVA 0x34A719E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019601

```text
(exec)# do-exec show ip sla statistics <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 18 `；EOL ` RVA 0x34A99A90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022759

```text
(exec)# do-exec show ip sla statistics aggregated <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 25 `；EOL ` RVA 0x34A99550 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-024373

```text
(exec)# do-exec show ip sla statistics aggregated details <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 26 `；EOL ` RVA 0x34A99528 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022755

```text
(exec)# do-exec show ip sla statistics details <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 22 `；EOL ` RVA 0x34A99A68 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019453

```text
(exec)# do-exec show ip sla summary <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 46 `；EOL ` RVA 0x34A95DE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019506

```text
(exec)# do-exec show ip sla totals-statistics <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 4 `；EOL ` RVA 0x34A97188 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-024353

```text
(exec)# do-exec show ip sla twamp connection requests <cr>
```

Handler ` RVA 0x1021EB60 `；selector ` 0 `；EOL ` RVA 0x34A73EC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-13f880874fe853b3](../../evidence/state_effects-sets-005.md#s-13f880874fe853b3)

### path-022691

```text
(exec)# do-exec show ip sla twamp session <cr>
```

Handler ` RVA 0x10238810 `；selector ` 0 `；EOL ` RVA 0x34A76DF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-43b1368346f523be](../../evidence/state_effects-sets-015.md#s-43b1368346f523be)

### path-022680

```text
(exec)# do-exec show ip sla twamp standards <cr>
```

Handler ` RVA 0x10238750 `；selector ` 0 `；EOL ` RVA 0x34A770A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022702

```text
(exec)# do-exec show ip sla twamp-light session <cr>
```

Handler ` RVA 0x1023AE80 `；selector ` 0 `；EOL ` RVA 0x34A79728 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-379ad248522dfa47](../../evidence/state_effects-sets-012.md#s-379ad248522dfa47)

### path-014138

```text
(exec)# do-exec show ip sockets <cr>
```

Handler ` RVA 0xCE441C0 `；selector ` 0 `；EOL ` RVA 0x33D31858 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019511

```text
(exec)# do-exec show ip source binding <cr>
```

Handler ` RVA 0x15FA8BF0 `；selector ` 0 `；EOL ` RVA 0x35E7DBE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f93d0b7b9a074084](../../evidence/conditions-sets-096.md#c-f93d0b7b9a074084) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-014132

```text
(exec)# do-exec show ip spd <cr>
```

Handler ` RVA 0xCF78E90 `；selector ` 0 `；EOL ` RVA 0x33D31AF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-014949

```text
(exec)# do-exec show ip ssh <cr>
```

Handler ` RVA 0x12360610 `；selector ` 0 `；EOL ` RVA 0x35828848 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022352

```text
(exec)# do-exec show ip static route rwatch-rib <cr>
```

Handler ` RVA 0xE2A7940 `；selector ` 0 `；EOL ` RVA 0x3428F850 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5aa975823e16c479](../../evidence/conditions-sets-036.md#c-5aa975823e16c479) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022386

```text
(exec)# do-exec show ip static route sr-polices <cr>
```

Handler ` RVA 0xE2A79D0 `；selector ` 0 `；EOL ` RVA 0x3428FB38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-dd5e5ad91a8d2392](../../evidence/conditions-sets-085.md#c-dd5e5ad91a8d2392) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022302

```text
(exec)# do-exec show ip static route summary <cr>
```

Handler ` RVA 0xE2A7770 `；selector ` 0 `；EOL ` RVA 0x3428EE60 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-015075

```text
(exec)# do-exec show ip subscriber <cr>
```

Handler ` RVA 0x11A37870 `；selector ` 0 `；EOL ` RVA 0x355CDAE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-b8a261e6d64b6f60](../../evidence/state_effects-sets-039.md#s-b8a261e6d64b6f60)

### path-018343

```text
(exec)# do-exec show ip tcp header-compression <cr>
```

Handler ` RVA 0xD194400 `；selector ` 0 `；EOL ` RVA 0x33DAB590 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7df4d3139ca6c380](../../evidence/conditions-sets-049.md#c-7df4d3139ca6c380) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-018525

```text
(exec)# do-exec show ip telnet status <cr>
```

Handler ` RVA 0xCDEFBC0 `；selector ` 0 `；EOL ` RVA 0x33D02090 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-014179

```text
(exec)# do-exec show ip traffic <cr>
```

Handler ` RVA 0xCECF560 `；selector ` 0 `；EOL ` RVA 0x33D32270 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-021889

```text
(exec)# do-exec show ip traffic topology base <cr>
```

Handler ` RVA 0xCF0ED10 `；selector ` 0 `；EOL ` RVA 0x33D31E70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-055faeefede62a5c](../../evidence/state_effects-sets-002.md#s-055faeefede62a5c)

### path-014881

```text
(exec)# do-exec show ip trigger-authentication <cr>
```

Handler ` RVA 0x10571410 `；selector ` 2 `；EOL ` RVA 0x34B5A698 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-014045

```text
(exec)# do-exec show ipam counts <cr>
```

Handler ` RVA 0xCEA9220 `；selector ` 0 `；EOL ` RVA 0x33D1B0A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-014036

```text
(exec)# do-exec show ipam pool <cr>
```

Handler ` RVA 0xCEA02D0 `；selector ` 0 `；EOL ` RVA 0x33D1B340 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-014055

```text
(exec)# do-exec show ipam queues <cr>
```

Handler ` RVA 0xCEA9160 `；selector ` 0 `；EOL ` RVA 0x33D1B5E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-014082

```text
(exec)# do-exec show ipam status <cr>
```

Handler ` RVA 0xCE9D6D0 `；selector ` 0 `；EOL ` RVA 0x33D1B890 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-013342

```text
(exec)# do-exec show ipc all <cr>
```

Handler ` RVA 0xD3B9630 `；selector ` 0 `；EOL ` RVA 0x33E2A320 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-f1cf6e26d3b77629](../../evidence/state_effects-sets-051.md#s-f1cf6e26d3b77629)

### path-013471

```text
(exec)# do-exec show ipc app <cr>
```

Handler ` RVA 0xD3BE590 `；selector ` 0 `；EOL ` RVA 0x33E2D5B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-013488

```text
(exec)# do-exec show ipc buffer <cr>
```

Handler ` RVA 0xD39FCA0 `；selector ` 0 `；EOL ` RVA 0x33E2D858 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-021172

```text
(exec)# do-exec show ipc cli <number:0..4294967295> <string> <cr>
```

Handler ` RVA 0xD38B220 `；selector ` 0 `；EOL ` RVA 0x33E2AAB0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` IPC Seatid (in hex)；` string ` Remote command string。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-d04ece3d584907a5](../../evidence/parameters-sets-016.md#p-d04ece3d584907a5) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-013435

```text
(exec)# do-exec show ipc delayed <cr>
```

Handler ` RVA 0xD3A24C0 `；selector ` 0 `；EOL ` RVA 0x33E2D018 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-013281

```text
(exec)# do-exec show ipc fc <cr>
```

Handler ` RVA 0xD3B96E0 `；selector ` 0 `；EOL ` RVA 0x33E29FA8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-013478

```text
(exec)# do-exec show ipc fragment <cr>
```

Handler ` RVA 0xD3BE5F0 `；selector ` 0 `；EOL ` RVA 0x33E2CD28 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-978af586df9caab5](../../evidence/state_effects-sets-032.md#s-978af586df9caab5)

### path-013411

```text
(exec)# do-exec show ipc hog-info <cr>
```

Handler ` RVA 0xD3B8FB0 `；selector ` 0 `；EOL ` RVA 0x33E2C938 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-017441

```text
(exec)# do-exec show ipc keepalive tx <cr>
```

Handler ` RVA 0xD3B8EC0 `；selector ` 0 `；EOL ` RVA 0x33E2E360 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-533d30bebf69d6c0](../../evidence/state_effects-sets-018.md#s-533d30bebf69d6c0)

### path-017207

```text
(exec)# do-exec show ipc mcast appclass <cr>
```

Handler ` RVA 0xD408040 `；selector ` 0 `；EOL ` RVA 0x33E42858 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-40d883997542d866](../../evidence/state_effects-sets-014.md#s-40d883997542d866)

### path-017237

```text
(exec)# do-exec show ipc mcast groups <cr>
```

Handler ` RVA 0xD407F80 `；selector ` 0 `；EOL ` RVA 0x33E42C30 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-500724098bc2f731](../../evidence/state_effects-sets-017.md#s-500724098bc2f731)

### path-021190

```text
(exec)# do-exec show ipc mcast groups <number:1..4294967295> <cr>
```

Handler ` RVA 0xD407F10 `；selector ` 0 `；EOL ` RVA 0x33E42F18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` group id。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-6d276200dc0ed569](../../evidence/parameters-sets-009.md#p-6d276200dc0ed569) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-017285

```text
(exec)# do-exec show ipc mcast sessions <cr>
```

Handler ` RVA 0xD407DA0 `；selector ` 0 `；EOL ` RVA 0x33E43368 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-a38184d301c438ed](../../evidence/state_effects-sets-035.md#s-a38184d301c438ed)

### path-021247

```text
(exec)# do-exec show ipc mcast sessions verbose <cr>
```

Handler ` RVA 0xD407DA0 `；selector ` 1 `；EOL ` RVA 0x33E43340 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-a38184d301c438ed](../../evidence/state_effects-sets-035.md#s-a38184d301c438ed)

### path-017189

```text
(exec)# do-exec show ipc mcast status <cr>
```

Handler ` RVA 0xD408100 `；selector ` 0 `；EOL ` RVA 0x33E42480 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d4e189fb131a0532](../../evidence/state_effects-sets-045.md#s-d4e189fb131a0532)

### path-013372

```text
(exec)# do-exec show ipc nodes <cr>
```

Handler ` RVA 0xD3B9570 `；selector ` 0 `；EOL ` RVA 0x33E2A748 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-33dbeae1d3a19d17](../../evidence/state_effects-sets-011.md#s-33dbeae1d3a19d17)

### path-017246

```text
(exec)# do-exec show ipc nodes capabilities <cr>
```

Handler ` RVA 0xD45A9C0 `；selector ` 0 `；EOL ` RVA 0x33E489F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-33dbeae1d3a19d17](../../evidence/state_effects-sets-011.md#s-33dbeae1d3a19d17)

### path-017231

```text
(exec)# do-exec show ipc nodes issu <cr>
```

Handler ` RVA 0xD45ADB0 `；selector ` 0 `；EOL ` RVA 0x33E48750 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-33dbeae1d3a19d17](../../evidence/state_effects-sets-011.md#s-33dbeae1d3a19d17)

### path-017247

```text
(exec)# do-exec show ipc nodes verbose <cr>
```

Handler ` RVA 0xD3B9570 `；selector ` 1 `；EOL ` RVA 0x33E27958 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-33dbeae1d3a19d17](../../evidence/state_effects-sets-011.md#s-33dbeae1d3a19d17)

### path-013428

```text
(exec)# do-exec show ipc ports <cr>
```

Handler ` RVA 0xD3B9210 `；selector ` 0 `；EOL ` RVA 0x33E2B120 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-a9d01fee5248bc66](../../evidence/state_effects-sets-036.md#s-a9d01fee5248bc66)

### path-017263

```text
(exec)# do-exec show ipc ports verbose <cr>
```

Handler ` RVA 0xD3B9210 `；selector ` 1 `；EOL ` RVA 0x33E2B3D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-a9d01fee5248bc66](../../evidence/state_effects-sets-036.md#s-a9d01fee5248bc66)

### path-013264

```text
(exec)# do-exec show ipc queue <cr>
```

Handler ` RVA 0xD3B91C0 `；selector ` 0 `；EOL ` RVA 0x33E29D00 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-017190

```text
(exec)# do-exec show ipc rmi all <cr>
```

Handler ` RVA 0xD3FE890 `；selector ` 0 `；EOL ` RVA 0x33E3F8B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-35e0ba4624807019](../../evidence/state_effects-sets-012.md#s-35e0ba4624807019)

### path-023479

```text
(exec)# do-exec show ipc rmi thresholds ru <string> <cr>
```

Handler ` RVA 0xD3FE9F0 `；selector ` 0 `；EOL ` RVA 0x33E401F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` IPC RU id(in hex)。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-1f71f90238213b0b](../../evidence/parameters-sets-003.md#p-1f71f90238213b0b) · [状态效果 S-7a2d71bdaece15c5](../../evidence/state_effects-sets-026.md#s-7a2d71bdaece15c5)

### path-013610

```text
(exec)# do-exec show ipc rpc <cr>
```

Handler ` RVA 0xD3B90F0 `；selector ` 0 `；EOL ` RVA 0x33E2E7A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-897f0e1f726ca959](../../evidence/state_effects-sets-029.md#s-897f0e1f726ca959)

### path-013522

```text
(exec)# do-exec show ipc sess-ack <cr>
```

Handler ` RVA 0xD3B92E0 `；selector ` 0 `；EOL ` RVA 0x33E2DDA8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-017282

```text
(exec)# do-exec show ipc session all <cr>
```

Handler ` RVA 0xD3B9330 `；selector ` 0 `；EOL ` RVA 0x33E2B898 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-87ea77cfe15c1307](../../evidence/state_effects-sets-029.md#s-87ea77cfe15c1307)

### path-021244

```text
(exec)# do-exec show ipc session all verbose <cr>
```

Handler ` RVA 0xD3B9330 `；selector ` 1 `；EOL ` RVA 0x33E2B870 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-87ea77cfe15c1307](../../evidence/state_effects-sets-029.md#s-87ea77cfe15c1307)

### path-017306

```text
(exec)# do-exec show ipc session tx <cr>
```

Handler ` RVA 0xD3B9450 `；selector ` 0 `；EOL ` RVA 0x33E2BF38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-89ec23bf523a0f90](../../evidence/state_effects-sets-029.md#s-89ec23bf523a0f90)

### path-021259

```text
(exec)# do-exec show ipc session tx verbose <cr>
```

Handler ` RVA 0xD3B9450 `；selector ` 1 `；EOL ` RVA 0x33E2BF10 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-89ec23bf523a0f90](../../evidence/state_effects-sets-029.md#s-89ec23bf523a0f90)

### path-013458

```text
(exec)# do-exec show ipc status <cr>
```

Handler ` RVA 0xD3B8DA0 `；selector ` 0 `；EOL ` RVA 0x33E2C640 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-534515a850faef09](../../evidence/state_effects-sets-018.md#s-534515a850faef09)

### path-013507

```text
(exec)# do-exec show ipc thread-stats <cr>
```

Handler ` RVA 0xD3985A0 `；selector ` 0 `；EOL ` RVA 0x33E2DB00 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-017314

```text
(exec)# do-exec show ipc trace <number:1..3> <cr>
```

Handler ` RVA 0xD3B9000 `；selector ` 0 `；EOL ` RVA 0x33E2D328 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Type of buffer(1. event 2. debug 3. error)。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-8efb61522b8c3136](../../evidence/parameters-sets-011.md#p-8efb61522b8c3136) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-013581

```text
(exec)# do-exec show ipc util <cr>
```

Handler ` RVA 0xD3BC620 `；selector ` 0 `；EOL ` RVA 0x33E2EA90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-013535

```text
(exec)# do-exec show ipc watermark <cr>
```

Handler ` RVA 0xD3B8F20 `；selector ` 0 `；EOL ` RVA 0x33E2E050 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-013346

```text
(exec)# do-exec show ipc zones <cr>
```

Handler ` RVA 0xD3BC120 `；selector ` 0 `；EOL ` RVA 0x33E2AD30 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-014994

```text
(exec)# do-exec show ipv6 access-list <cr>
```

Handler ` RVA 0x1217F2C0 `；selector ` 0 `；EOL ` RVA 0x357B0418 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-15ba82e1b1af0acd](../../evidence/conditions-sets-009.md#c-15ba82e1b1af0acd) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022614

```text
(exec)# do-exec show ipv6 access-list <string> dump-og-database <cr>
```

Handler ` RVA 0x1217F470 `；selector ` 0 `；EOL ` RVA 0x357B04A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` User selected string identifying this access list。

[条件 C-47044ba01fe6dceb](../../evidence/conditions-sets-028.md#c-47044ba01fe6dceb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-4019a6f8b247af69](../../evidence/parameters-sets-005.md#p-4019a6f8b247af69) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-015055

```text
(exec)# do-exec show ipv6 alias <cr>
```

Handler ` RVA 0x12303F00 `；selector ` 0 `；EOL ` RVA 0x357DF538 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019640

```text
(exec)# do-exec show ipv6 cef events <cr>
```

Handler ` RVA 0xD2CF860 `；selector ` 0 `；EOL ` RVA 0x337CE290 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-fea93fa3a2ba2841](../../evidence/conditions-sets-098.md#c-fea93fa3a2ba2841) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-bc26fde89760b4c1](../../evidence/state_effects-sets-040.md#s-bc26fde89760b4c1)

### path-024351

```text
(exec)# do-exec show ipv6 cef neighbor discovery throttling <cr>
```

Handler ` RVA 0xB671710 `；selector ` 0 `；EOL ` RVA 0x337CD4C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c63cf6e327e36988](../../evidence/conditions-sets-076.md#c-c63cf6e327e36988) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-b6a0bf2ec19990dc](../../evidence/state_effects-sets-039.md#s-b6a0bf2ec19990dc)

### path-019450

```text
(exec)# do-exec show ipv6 cef protocol-discard <cr>
```

Handler ` RVA 0xB5C2EB0 `；selector ` 73 `；EOL ` RVA 0x337D89C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019477

```text
(exec)# do-exec show ipv6 cef summary <cr>
```

Handler ` RVA 0xB670E30 `；selector ` 1 `；EOL ` RVA 0x337CD130 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c63cf6e327e36988](../../evidence/conditions-sets-076.md#c-c63cf6e327e36988) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-b6a0bf2ec19990dc](../../evidence/state_effects-sets-039.md#s-b6a0bf2ec19990dc)

### path-022730

```text
(exec)# do-exec show ipv6 cef switching statistics <cr>
```

Handler ` RVA 0xB66E5F0 `；selector ` 0 `；EOL ` RVA 0x337CDF00 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-fea93fa3a2ba2841](../../evidence/conditions-sets-098.md#c-fea93fa3a2ba2841) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-b6a0bf2ec19990dc](../../evidence/state_effects-sets-039.md#s-b6a0bf2ec19990dc)

### path-022735

```text
(exec)# do-exec show ipv6 cef traffic prefix-length <cr>
```

Handler ` RVA 0xB671680 `；selector ` 0 `；EOL ` RVA 0x337CE7E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-fea93fa3a2ba2841](../../evidence/conditions-sets-098.md#c-fea93fa3a2ba2841) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-5cc4322e8ef91cdd](../../evidence/state_effects-sets-020.md#s-5cc4322e8ef91cdd)

### path-019524

```text
(exec)# do-exec show ipv6 cef tree <cr>
```

Handler ` RVA 0xB670D30 `；selector ` 0 `；EOL ` RVA 0x337CD7E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c63cf6e327e36988](../../evidence/conditions-sets-076.md#c-c63cf6e327e36988) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-b6a0bf2ec19990dc](../../evidence/state_effects-sets-039.md#s-b6a0bf2ec19990dc)

### path-019300

```text
(exec)# do-exec show ipv6 destination-guard policy <cr>
```

Handler ` RVA 0x136B13F0 `；selector ` 0 `；EOL ` RVA 0x35C02EE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-014940

```text
(exec)# do-exec show ipv6 dhcp <cr>
```

Handler ` RVA 0x121A4390 `；selector ` 0 `；EOL ` RVA 0x357C0EC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019400

```text
(exec)# do-exec show ipv6 dhcp binding <cr>
```

Handler ` RVA 0x121CD760 `；selector ` 0 `；EOL ` RVA 0x357C6450 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019422

```text
(exec)# do-exec show ipv6 dhcp conflict <cr>
```

Handler ` RVA 0x121CD760 `；selector ` 3 `；EOL ` RVA 0x357C6D50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019354

```text
(exec)# do-exec show ipv6 dhcp database <cr>
```

Handler ` RVA 0x121CD760 `；selector ` 2 `；EOL ` RVA 0x357C5C98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-024867

```text
(exec)# do-exec show ipv6 dhcp mac-hash-table dump pool <string> <cr>
```

Handler ` RVA 0x121CD760 `；selector ` 8 `；EOL ` RVA 0x357C7158 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` pool name。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-c08b972a2d83bb8c](../../evidence/parameters-sets-015.md#p-c08b972a2d83bb8c) · [状态效果 S-7762735493e5148a](../../evidence/state_effects-sets-025.md#s-7762735493e5148a)

### path-025168

```text
(exec)# do-exec show ipv6 dhcp mac-hash-table dump pool <string> <number:0..255> <number:0..255> <cr>
```

Handler ` RVA 0x121CD760 `；selector ` 7 `；EOL ` RVA 0x357C71A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` pool name；` unsigned_number ` Lower bound of index range；` unsigned_number ` Upper bound of index range。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-6b881825297e6ab3](../../evidence/parameters-sets-008.md#p-6b881825297e6ab3) · [状态效果 S-7762735493e5148a](../../evidence/state_effects-sets-025.md#s-7762735493e5148a)

### path-022625

```text
(exec)# do-exec show ipv6 dhcp packet statistics <cr>
```

Handler ` RVA 0x121CD760 `；selector ` 6 `；EOL ` RVA 0x357C6A30 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019399

```text
(exec)# do-exec show ipv6 dhcp pool <cr>
```

Handler ` RVA 0x121CD760 `；selector ` 1 `；EOL ` RVA 0x357C6748 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022575

```text
(exec)# do-exec show ipv6 dhcp relay binding <cr>
```

Handler ` RVA 0x121B3460 `；selector ` 1 `；EOL ` RVA 0x357C33B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019243

```text
(exec)# do-exec show ipv6 dhcp statistics <cr>
```

Handler ` RVA 0x121A4390 `；selector ` 2 `；EOL ` RVA 0x357C0B28 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019248

```text
(exec)# do-exec show ipv6 eigrp accounting <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 98 `；EOL ` RVA 0x35467758 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-1f6e025fe598cf9d](../../evidence/state_effects-sets-007.md#s-1f6e025fe598cf9d)

### path-019302

```text
(exec)# do-exec show ipv6 eigrp sia-event <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 99 `；EOL ` RVA 0x35467AA0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-0f14fe87df030153](../../evidence/state_effects-sets-004.md#s-0f14fe87df030153)

### path-019338

```text
(exec)# do-exec show ipv6 eigrp sia-statistics <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 99 `；EOL ` RVA 0x35467E28 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-6128f5f2d4d3ee63](../../evidence/state_effects-sets-021.md#s-6128f5f2d4d3ee63)

### path-019170

```text
(exec)# do-exec show ipv6 eigrp timers <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 95 `；EOL ` RVA 0x35466A58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-1f6e025fe598cf9d](../../evidence/state_effects-sets-007.md#s-1f6e025fe598cf9d)

### path-019200

```text
(exec)# do-exec show ipv6 eigrp traffic <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 96 `；EOL ` RVA 0x35466D00 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-1f6e025fe598cf9d](../../evidence/state_effects-sets-007.md#s-1f6e025fe598cf9d)

### path-015070

```text
(exec)# do-exec show ipv6 enablement <cr>
```

Handler ` RVA 0x123003B0 `；selector ` 0 `；EOL ` RVA 0x357DF7E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-014586

```text
(exec)# do-exec show ipv6 errors-internal <cr>
```

Handler ` RVA 0x12304EF0 `；selector ` 0 `；EOL ` RVA 0x357E3398 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d4606ca718ceaf8b](../../evidence/conditions-sets-082.md#c-d4606ca718ceaf8b) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-018735

```text
(exec)# do-exec show ipv6 features global <cr>
```

Handler ` RVA 0x123058C0 `；selector ` 0 `；EOL ` RVA 0x357E5868 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-015044

```text
(exec)# do-exec show ipv6 general-prefix <cr>
```

Handler ` RVA 0x12303340 `；selector ` 0 `；EOL ` RVA 0x357DF290 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-018966

```text
(exec)# do-exec show ipv6 local pool <cr>
```

Handler ` RVA 0x1232CA00 `；selector ` 0 `；EOL ` RVA 0x358110E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-efaa3f25c33856a1](../../evidence/conditions-sets-093.md#c-efaa3f25c33856a1) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-015076

```text
(exec)# do-exec show ipv6 mfib <cr>
```

Handler ` RVA 0x1197C6E0 `；selector ` 0 `；EOL ` RVA 0x355BA3A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ca7cba7852ec64d8](../../evidence/conditions-sets-078.md#c-ca7cba7852ec64d8) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-8089b2d1dfd067e3](../../evidence/state_effects-sets-027.md#s-8089b2d1dfd067e3)

### path-019161

```text
(exec)# do-exec show ipv6 mfib cable <cr>
```

Handler ` RVA 0x1197DD40 `；selector ` 0 `；EOL ` RVA 0x355B8E50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-4cfae6e1f48b87a6](../../evidence/state_effects-sets-017.md#s-4cfae6e1f48b87a6)

### path-019215

```text
(exec)# do-exec show ipv6 mfib interface <cr>
```

Handler ` RVA 0x1197DBC0 `；selector ` 0 `；EOL ` RVA 0x355B9DB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8bf5a5acdfcd7d48](../../evidence/conditions-sets-054.md#c-8bf5a5acdfcd7d48) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-476a177368ac85ea](../../evidence/state_effects-sets-016.md#s-476a177368ac85ea)

### path-022344

```text
(exec)# do-exec show ipv6 mfib internal fibidb <cr>
```

Handler ` RVA 0x1197DE80 `；selector ` 0 `；EOL ` RVA 0x355B92A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-fe20a5207b9dac80](../../evidence/state_effects-sets-054.md#s-fe20a5207b9dac80)

### path-022502

```text
(exec)# do-exec show ipv6 mfib internal mem <cr>
```

Handler ` RVA 0x1197DF50 `；selector ` 0 `；EOL ` RVA 0x355B95E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-1582ab84ee0d0c1a](../../evidence/state_effects-sets-005.md#s-1582ab84ee0d0c1a)

### path-019249

```text
(exec)# do-exec show ipv6 mfib rate-list <cr>
```

Handler ` RVA 0x1197C6E0 `；selector ` 0 `；EOL ` RVA 0x355BA698 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8f188dcc50cbdf27](../../evidence/conditions-sets-055.md#c-8f188dcc50cbdf27) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-06bc08c4341fdee9](../../evidence/state_effects-sets-002.md#s-06bc08c4341fdee9)

### path-019080

```text
(exec)# do-exec show ipv6 mfib status <cr>
```

Handler ` RVA 0x1197C470 `；selector ` 0 `；EOL ` RVA 0x355B99F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-fe20a5207b9dac80](../../evidence/state_effects-sets-054.md#s-fe20a5207b9dac80)

### path-019226

```text
(exec)# do-exec show ipv6 mld acl-db <cr>
```

Handler ` RVA 0x11625660 `；selector ` 6 `；EOL ` RVA 0x3554A6F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9a72383b5b9871bd](../../evidence/conditions-sets-060.md#c-9a72383b5b9871bd) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-607298883a6cd71c](../../evidence/state_effects-sets-021.md#s-607298883a6cd71c)

### path-022418

```text
(exec)# do-exec show ipv6 mld all-vrfs traffic <cr>
```

Handler ` RVA 0x11625660 `；selector ` 4 `；EOL ` RVA 0x3554B100 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-76db2ed043998d11](../../evidence/conditions-sets-046.md#c-76db2ed043998d11) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-607298883a6cd71c](../../evidence/state_effects-sets-021.md#s-607298883a6cd71c)

### path-019294

```text
(exec)# do-exec show ipv6 mld gir <cr>
```

Handler ` RVA 0x11625660 `；selector ` 7 `；EOL ` RVA 0x3554ADE8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c040cde0ca3b9d9d](../../evidence/conditions-sets-074.md#c-c040cde0ca3b9d9d) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-607298883a6cd71c](../../evidence/state_effects-sets-021.md#s-607298883a6cd71c)

### path-019234

```text
(exec)# do-exec show ipv6 mld ssm-map <cr>
```

Handler ` RVA 0x11625660 `；selector ` 5 `；EOL ` RVA 0x3554A478 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9a72383b5b9871bd](../../evidence/conditions-sets-060.md#c-9a72383b5b9871bd) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-607298883a6cd71c](../../evidence/state_effects-sets-021.md#s-607298883a6cd71c)

### path-019167

```text
(exec)# do-exec show ipv6 mld traffic <cr>
```

Handler ` RVA 0x11625660 `；selector ` 3 `；EOL ` RVA 0x3554A168 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9a72383b5b9871bd](../../evidence/conditions-sets-060.md#c-9a72383b5b9871bd) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-607298883a6cd71c](../../evidence/state_effects-sets-021.md#s-607298883a6cd71c)

### path-019111

```text
(exec)# do-exec show ipv6 mrib client <cr>
```

Handler ` RVA 0x119BB9A0 `；selector ` 1 `；EOL ` RVA 0x3554F618 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-0c080b51c69c8ebf](../../evidence/state_effects-sets-003.md#s-0c080b51c69c8ebf)

### path-019217

```text
(exec)# do-exec show ipv6 mrib route <cr>
```

Handler ` RVA 0x119BB9A0 `；selector ` 0 `；EOL ` RVA 0x3554EB60 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-32313e0318335ac8](../../evidence/conditions-sets-020.md#c-32313e0318335ac8) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-0c080b51c69c8ebf](../../evidence/state_effects-sets-003.md#s-0c080b51c69c8ebf)

### path-022323

```text
(exec)# do-exec show ipv6 mrib route summary <cr>
```

Handler ` RVA 0x119BB9A0 `；selector ` 3 `；EOL ` RVA 0x3554E800 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-0c080b51c69c8ebf](../../evidence/state_effects-sets-003.md#s-0c080b51c69c8ebf)

### path-014970

```text
(exec)# do-exec show ipv6 mroute <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 1 `；EOL ` RVA 0x3555E458 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b9191311256f7dfc](../../evidence/conditions-sets-071.md#c-b9191311256f7dfc) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-ac8bf1786f923106](../../evidence/state_effects-sets-036.md#s-ac8bf1786f923106)

### path-019388

```text
(exec)# do-exec show ipv6 mroute active <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 18 `；EOL ` RVA 0x3555EC48 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-55987220baad4093](../../evidence/conditions-sets-034.md#c-55987220baad4093) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-fbab8e64d084e472](../../evidence/state_effects-sets-053.md#s-fbab8e64d084e472)

### path-019325

```text
(exec)# do-exec show ipv6 mroute count <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 19 `；EOL ` RVA 0x3555E878 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e5655b8c20a1c583](../../evidence/conditions-sets-088.md#c-e5655b8c20a1c583) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-1f2d16c373864a4c](../../evidence/state_effects-sets-007.md#s-1f2d16c373864a4c)

### path-014686

```text
(exec)# do-exec show ipv6 mtu <cr>
```

Handler ` RVA 0x12306750 `；selector ` 0 `；EOL ` RVA 0x357E5568 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d7088f5ef6fc7dcb](../../evidence/state_effects-sets-046.md#s-d7088f5ef6fc7dcb)

### path-014905

```text
(exec)# do-exec show ipv6 multicast <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 28 `；EOL ` RVA 0x3555F478 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2c425fa2dd43dd3e](../../evidence/conditions-sets-017.md#c-2c425fa2dd43dd3e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-c3cb80c0600a37b8](../../evidence/state_effects-sets-041.md#s-c3cb80c0600a37b8)

### path-024281

```text
(exec)# do-exec show ipv6 multicast overlay-mapping lisp <address> <cr>
```

Handler ` RVA 0x11757BB0 `；selector ` 29 `；EOL ` RVA 0x3555F698 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Overlay group address。

[条件 C-9d35ab13682ac8bd](../../evidence/conditions-sets-061.md#c-9d35ab13682ac8bd) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-b95907093bfeb6e7](../../evidence/parameters-sets-014.md#p-b95907093bfeb6e7) · [状态效果 S-c9917060da600b22](../../evidence/state_effects-sets-043.md#s-c9917060da600b22)

### path-022517

```text
(exec)# do-exec show ipv6 multicast rpf monitored <cr>
```

Handler ` RVA 0x11757B10 `；selector ` 0 `；EOL ` RVA 0x3555FAC8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9d35ab13682ac8bd](../../evidence/conditions-sets-061.md#c-9d35ab13682ac8bd) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-c3cb80c0600a37b8](../../evidence/state_effects-sets-041.md#s-c3cb80c0600a37b8)

### path-024839

```text
(exec)# do-exec show ipv6 multicast snooping limit vlan <number:1..4095> <cr>
```

Handler ` RVA 0xC361C10 `；selector ` 61 `；EOL ` RVA 0x33A5E878 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Vlan number。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-4a4b3b45291b2ba0](../../evidence/parameters-sets-006.md#p-4a4b3b45291b2ba0) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022312

```text
(exec)# do-exec show ipv6 multicast snooping summary <cr>
```

Handler ` RVA 0xC361C10 `；selector ` 71 `；EOL ` RVA 0x33A5EB78 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-024842

```text
(exec)# do-exec show ipv6 multicast snooping summary vlan <number:1..4095> <cr>
```

Handler ` RVA 0xC361C10 `；selector ` 69 `；EOL ` RVA 0x33A5EBB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Vlan number。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-7a939613dde89531](../../evidence/parameters-sets-010.md#p-7a939613dde89531) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-018958

```text
(exec)# do-exec show ipv6 nd suppress <cr>
```

Handler ` RVA 0x136B3070 `；selector ` 0 `；EOL ` RVA 0x35C058E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-06dab21e684c5791](../../evidence/conditions-sets-003.md#c-06dab21e684c5791) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-018967

```text
(exec)# do-exec show ipv6 neighbors ha <cr>
```

Handler ` RVA 0x12312380 `；selector ` 0 `；EOL ` RVA 0x35802280 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7810b73dccdb84af](../../evidence/conditions-sets-047.md#c-7810b73dccdb84af) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-597f21bb08eb93b3](../../evidence/state_effects-sets-019.md#s-597f21bb08eb93b3)

### path-019293

```text
(exec)# do-exec show ipv6 nhrp attribute <cr>
```

Handler ` RVA 0x1186E4D0 `；selector ` 16 `；EOL ` RVA 0x3556AF90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019336

```text
(exec)# do-exec show ipv6 nhrp instances <cr>
```

Handler ` RVA 0x1186E4D0 `；selector ` 20 `；EOL ` RVA 0x3556B2A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-41053804b2654dd5](../../evidence/conditions-sets-025.md#c-41053804b2654dd5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019196

```text
(exec)# do-exec show ipv6 nhrp purge <cr>
```

Handler ` RVA 0x1186E4D0 `；selector ` 2 `；EOL ` RVA 0x355692E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019368

```text
(exec)# do-exec show ipv6 nhrp redirect <cr>
```

Handler ` RVA 0x1186E4D0 `；selector ` 6 `；EOL ` RVA 0x3556B620 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019238

```text
(exec)# do-exec show ipv6 nhrp traffic <cr>
```

Handler ` RVA 0x1186E4D0 `；selector ` 1 `；EOL ` RVA 0x355689D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022441

```text
(exec)# do-exec show ipv6 pim all-vrfs traffic <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 17 `；EOL ` RVA 0x3555DF70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e3aef5a38ae89c70](../../evidence/conditions-sets-088.md#c-e3aef5a38ae89c70) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-cbf18bf23d4f8e26](../../evidence/state_effects-sets-043.md#s-cbf18bf23d4f8e26)

### path-019443

```text
(exec)# do-exec show ipv6 pim anycast-rp <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 20 `；EOL ` RVA 0x3555D920 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0dbf75005d0c9c9b](../../evidence/conditions-sets-006.md#c-0dbf75005d0c9c9b) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-cbf18bf23d4f8e26](../../evidence/state_effects-sets-043.md#s-cbf18bf23d4f8e26)

### path-022688

```text
(exec)# do-exec show ipv6 pim bsr candidate-rp <cr>
```

Handler ` RVA 0x11843E00 `；selector ` 13 `；EOL ` RVA 0x35551E10 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b4444ce0bf724afb](../../evidence/conditions-sets-070.md#c-b4444ce0bf724afb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-e9fff46e4dfb9c4c](../../evidence/state_effects-sets-050.md#s-e9fff46e4dfb9c4c)

### path-022705

```text
(exec)# do-exec show ipv6 pim bsr election <cr>
```

Handler ` RVA 0x11843E00 `；selector ` 12 `；EOL ` RVA 0x35552360 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b4444ce0bf724afb](../../evidence/conditions-sets-070.md#c-b4444ce0bf724afb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-e9fff46e4dfb9c4c](../../evidence/state_effects-sets-050.md#s-e9fff46e4dfb9c4c)

### path-022698

```text
(exec)# do-exec show ipv6 pim bsr rp-cache <cr>
```

Handler ` RVA 0x11843E00 `；selector ` 14 `；EOL ` RVA 0x355520B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b4444ce0bf724afb](../../evidence/conditions-sets-070.md#c-b4444ce0bf724afb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-e9fff46e4dfb9c4c](../../evidence/state_effects-sets-050.md#s-e9fff46e4dfb9c4c)

### path-019438

```text
(exec)# do-exec show ipv6 pim gir <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 26 `；EOL ` RVA 0x3555DBE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3768dcdfafbac72b](../../evidence/conditions-sets-022.md#c-3768dcdfafbac72b) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-cbf18bf23d4f8e26](../../evidence/state_effects-sets-043.md#s-cbf18bf23d4f8e26)

### path-019332

```text
(exec)# do-exec show ipv6 pim lisp-rloc-state <cr>
```

Handler ` RVA 0x11757BB0 `；selector ` 27 `；EOL ` RVA 0x3555BC58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-83cc795f397f9ed1](../../evidence/conditions-sets-051.md#c-83cc795f397f9ed1) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-cbf18bf23d4f8e26](../../evidence/state_effects-sets-043.md#s-cbf18bf23d4f8e26)

### path-019546

```text
(exec)# do-exec show ipv6 pim mdt <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 0 `；EOL ` RVA 0x3478A808 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b4444ce0bf724afb](../../evidence/conditions-sets-070.md#c-b4444ce0bf724afb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-cbf18bf23d4f8e26](../../evidence/state_effects-sets-043.md#s-cbf18bf23d4f8e26)

### path-022745

```text
(exec)# do-exec show ipv6 pim mdt bgp <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 1 `；EOL ` RVA 0x347886B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b4444ce0bf724afb](../../evidence/conditions-sets-070.md#c-b4444ce0bf724afb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-cbf18bf23d4f8e26](../../evidence/state_effects-sets-043.md#s-cbf18bf23d4f8e26)

### path-024364

```text
(exec)# do-exec show ipv6 pim mdt bgp c-mroutes <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 6 `；EOL ` RVA 0x34788378 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e0f4a562bd79631e](../../evidence/conditions-sets-087.md#c-e0f4a562bd79631e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-1f9f3e048348b7e0](../../evidence/state_effects-sets-007.md#s-1f9f3e048348b7e0)

### path-024872

```text
(exec)# do-exec show ipv6 pim mdt history interval <number:1..71582> <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 2 `；EOL ` RVA 0x34787F80 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` in minutes, maximum is 71582 minutes (7 weeks)。

[条件 C-b4444ce0bf724afb](../../evidence/conditions-sets-070.md#c-b4444ce0bf724afb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-957dcedf315a82c2](../../evidence/parameters-sets-011.md#p-957dcedf315a82c2) · [状态效果 S-cbf18bf23d4f8e26](../../evidence/state_effects-sets-043.md#s-cbf18bf23d4f8e26)

### path-024367

```text
(exec)# do-exec show ipv6 pim mdt internal bier <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 10 `；EOL ` RVA 0x34788F80 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-84219efcdabebf50](../../evidence/conditions-sets-051.md#c-84219efcdabebf50) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-cbf18bf23d4f8e26](../../evidence/state_effects-sets-043.md#s-cbf18bf23d4f8e26)

### path-024380

```text
(exec)# do-exec show ipv6 pim mdt internal crt <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 11 `；EOL ` RVA 0x34789A20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-346446207ebbe9b4](../../evidence/conditions-sets-020.md#c-346446207ebbe9b4) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-cbf18bf23d4f8e26](../../evidence/state_effects-sets-043.md#s-cbf18bf23d4f8e26)

### path-024363

```text
(exec)# do-exec show ipv6 pim mdt internal gre <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 7 `；EOL ` RVA 0x34788CD8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-29502a8ccf617563](../../evidence/conditions-sets-016.md#c-29502a8ccf617563) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-cbf18bf23d4f8e26](../../evidence/state_effects-sets-043.md#s-cbf18bf23d4f8e26)

### path-024371

```text
(exec)# do-exec show ipv6 pim mdt internal ir <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 9 `；EOL ` RVA 0x34789228 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c45a96432149cd82](../../evidence/conditions-sets-076.md#c-c45a96432149cd82) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-cbf18bf23d4f8e26](../../evidence/state_effects-sets-043.md#s-cbf18bf23d4f8e26)

### path-024375

```text
(exec)# do-exec show ipv6 pim mdt internal leaf-ad <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 15 `；EOL ` RVA 0x347894D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-fa3aee4f006bc09f](../../evidence/conditions-sets-097.md#c-fa3aee4f006bc09f) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-cbf18bf23d4f8e26](../../evidence/state_effects-sets-043.md#s-cbf18bf23d4f8e26)

### path-024377

```text
(exec)# do-exec show ipv6 pim mdt internal mldp <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 8 `；EOL ` RVA 0x34789778 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4d737908cf7e75f6](../../evidence/conditions-sets-030.md#c-4d737908cf7e75f6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-cbf18bf23d4f8e26](../../evidence/state_effects-sets-043.md#s-cbf18bf23d4f8e26)

### path-024385

```text
(exec)# do-exec show ipv6 pim mdt internal pe <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 12 `；EOL ` RVA 0x34789FD8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6cfe596c8a5efa8b](../../evidence/conditions-sets-042.md#c-6cfe596c8a5efa8b) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-cbf18bf23d4f8e26](../../evidence/state_effects-sets-043.md#s-cbf18bf23d4f8e26)

### path-024885

```text
(exec)# do-exec show ipv6 pim mdt internal pe all <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 14 `；EOL ` RVA 0x3478A280 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5544abd3a64524b3](../../evidence/conditions-sets-033.md#c-5544abd3a64524b3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-cbf18bf23d4f8e26](../../evidence/state_effects-sets-043.md#s-cbf18bf23d4f8e26)

### path-024382

```text
(exec)# do-exec show ipv6 pim mdt internal replication <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 16 `；EOL ` RVA 0x34789CC8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a2ecbf7d3a478420](../../evidence/conditions-sets-063.md#c-a2ecbf7d3a478420) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-cbf18bf23d4f8e26](../../evidence/state_effects-sets-043.md#s-cbf18bf23d4f8e26)

### path-024384

```text
(exec)# do-exec show ipv6 pim mdt internal tdb <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 13 `；EOL ` RVA 0x3478A510 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6f1aafbd453847f3](../../evidence/conditions-sets-043.md#c-6f1aafbd453847f3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-cbf18bf23d4f8e26](../../evidence/state_effects-sets-043.md#s-cbf18bf23d4f8e26)

### path-024359

```text
(exec)# do-exec show ipv6 pim mdt internal vxlan <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 24 `；EOL ` RVA 0x34788A30 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-dcda79b17efe1870](../../evidence/conditions-sets-085.md#c-dcda79b17efe1870) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-cbf18bf23d4f8e26](../../evidence/state_effects-sets-043.md#s-cbf18bf23d4f8e26)

### path-022700

```text
(exec)# do-exec show ipv6 pim mdt receive <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 3 `；EOL ` RVA 0x34787A08 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b4444ce0bf724afb](../../evidence/conditions-sets-070.md#c-b4444ce0bf724afb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-cbf18bf23d4f8e26](../../evidence/state_effects-sets-043.md#s-cbf18bf23d4f8e26)

### path-024340

```text
(exec)# do-exec show ipv6 pim mdt receive detail <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 4 `；EOL ` RVA 0x347879E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b4444ce0bf724afb](../../evidence/conditions-sets-070.md#c-b4444ce0bf724afb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-cbf18bf23d4f8e26](../../evidence/state_effects-sets-043.md#s-cbf18bf23d4f8e26)

### path-022678

```text
(exec)# do-exec show ipv6 pim mdt send <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 5 `；EOL ` RVA 0x347876D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b4444ce0bf724afb](../../evidence/conditions-sets-070.md#c-b4444ce0bf724afb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-cbf18bf23d4f8e26](../../evidence/state_effects-sets-043.md#s-cbf18bf23d4f8e26)

### path-022613

```text
(exec)# do-exec show ipv6 pim pfp-sa announcements <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 23 `；EOL ` RVA 0x3555C3A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-be731d8b3d956a00](../../evidence/conditions-sets-074.md#c-be731d8b3d956a00) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-cbf18bf23d4f8e26](../../evidence/state_effects-sets-043.md#s-cbf18bf23d4f8e26)

### path-022638

```text
(exec)# do-exec show ipv6 pim pfp-sa cache <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 25 `；EOL ` RVA 0x3555C8F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-be731d8b3d956a00](../../evidence/conditions-sets-074.md#c-be731d8b3d956a00) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-cbf18bf23d4f8e26](../../evidence/state_effects-sets-043.md#s-cbf18bf23d4f8e26)

### path-022627

```text
(exec)# do-exec show ipv6 pim pfp-sa originator <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 24 `；EOL ` RVA 0x3555C648 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-be731d8b3d956a00](../../evidence/conditions-sets-074.md#c-be731d8b3d956a00) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-cbf18bf23d4f8e26](../../evidence/state_effects-sets-043.md#s-cbf18bf23d4f8e26)

### path-019327

```text
(exec)# do-exec show ipv6 pim range-list <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 4 `；EOL ` RVA 0x3555A5A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b15f72033f3eb0ae](../../evidence/conditions-sets-069.md#c-b15f72033f3eb0ae) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-cbf18bf23d4f8e26](../../evidence/state_effects-sets-043.md#s-cbf18bf23d4f8e26)

### path-019261

```text
(exec)# do-exec show ipv6 pim topology <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 1 `；EOL ` RVA 0x355592E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0d057d950e6e2e7c](../../evidence/conditions-sets-005.md#c-0d057d950e6e2e7c) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-cbf18bf23d4f8e26](../../evidence/state_effects-sets-043.md#s-cbf18bf23d4f8e26)

### path-022478

```text
(exec)# do-exec show ipv6 pim topology route-count <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 6 `；EOL ` RVA 0x35559040 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a7ab8ff6af774007](../../evidence/conditions-sets-065.md#c-a7ab8ff6af774007) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-cbf18bf23d4f8e26](../../evidence/state_effects-sets-043.md#s-cbf18bf23d4f8e26)

### path-019383

```text
(exec)# do-exec show ipv6 pim traffic <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 16 `；EOL ` RVA 0x3555CB98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a6ee2bcbe1a78785](../../evidence/conditions-sets-064.md#c-a6ee2bcbe1a78785) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-cbf18bf23d4f8e26](../../evidence/state_effects-sets-043.md#s-cbf18bf23d4f8e26)

### path-015020

```text
(exec)# do-exec show ipv6 policy <cr>
```

Handler ` RVA 0x118BA0F0 `；selector ` 0 `；EOL ` RVA 0x3559C548 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-015008

```text
(exec)# do-exec show ipv6 prefix-list <cr>
```

Handler ` RVA 0xE2203B0 `；selector ` 0 `；EOL ` RVA 0x3557F168 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-94db62ffb44ba997](../../evidence/conditions-sets-058.md#c-94db62ffb44ba997) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-6ac02cbda10863e6](../../evidence/state_effects-sets-023.md#s-6ac02cbda10863e6)

### path-024303

```text
(exec)# do-exec show ipv6 prefix-list <string> seq <number:1..4294967295> <cr>
```

Handler ` RVA 0xE2203B0 `；selector ` 3 `；EOL ` RVA 0x3557F210 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Name of a prefix list；` unsigned_number ` Sequence number。

[条件 C-94db62ffb44ba997](../../evidence/conditions-sets-058.md#c-94db62ffb44ba997) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-46df89ae42bf78b4](../../evidence/parameters-sets-006.md#p-46df89ae42bf78b4) · [状态效果 S-6ac02cbda10863e6](../../evidence/state_effects-sets-023.md#s-6ac02cbda10863e6)

### path-019375

```text
(exec)# do-exec show ipv6 prefix-list detail <cr>
```

Handler ` RVA 0xE2203B0 `；selector ` 2 `；EOL ` RVA 0x3557EE68 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-6ac02cbda10863e6](../../evidence/state_effects-sets-023.md#s-6ac02cbda10863e6)

### path-019353

```text
(exec)# do-exec show ipv6 prefix-list summary <cr>
```

Handler ` RVA 0xE2203B0 `；selector ` 1 `；EOL ` RVA 0x3557EB58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-6ac02cbda10863e6](../../evidence/state_effects-sets-023.md#s-6ac02cbda10863e6)

### path-014705

```text
(exec)# do-exec show ipv6 protocols <cr>
```

Handler ` RVA 0x1230B1E0 `；selector ` 0 `；EOL ` RVA 0x357EAF78 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-014952

```text
(exec)# do-exec show ipv6 rip <cr>
```

Handler ` RVA 0x118A5B90 `；selector ` 0 `；EOL ` RVA 0x3557C408 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-aa703e0f0a1553a9](../../evidence/conditions-sets-066.md#c-aa703e0f0a1553a9) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019224

```text
(exec)# do-exec show ipv6 rip database <cr>
```

Handler ` RVA 0x118A4C60 `；selector ` 0 `；EOL ` RVA 0x3557BDF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-83b1b03eac7a0904](../../evidence/conditions-sets-051.md#c-83b1b03eac7a0904) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019246

```text
(exec)# do-exec show ipv6 rip next-hops <cr>
```

Handler ` RVA 0x118A5450 `；selector ` 0 `；EOL ` RVA 0x3557C0A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-83b1b03eac7a0904](../../evidence/conditions-sets-051.md#c-83b1b03eac7a0904) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019442

```text
(exec)# do-exec show ipv6 rpf <address> <cr>
```

Handler ` RVA 0x118E47F0 `；selector ` 0 `；EOL ` RVA 0x35538420 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` RP/Source address。

[条件 C-713c859374191240](../../evidence/conditions-sets-044.md#c-713c859374191240) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-45778e765de8f2c0](../../evidence/parameters-sets-006.md#p-45778e765de8f2c0) · [状态效果 S-26b1ef382ffbacb9](../../evidence/state_effects-sets-009.md#s-26b1ef382ffbacb9)

### path-019410

```text
(exec)# do-exec show ipv6 rpf select <cr>
```

Handler ` RVA 0x118E47F0 `；selector ` 1 `；EOL ` RVA 0x355380F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c84d32681a469f44](../../evidence/conditions-sets-077.md#c-c84d32681a469f44) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-26b1ef382ffbacb9](../../evidence/state_effects-sets-009.md#s-26b1ef382ffbacb9)

### path-019347

```text
(exec)# do-exec show ipv6 snooping events <cr>
```

Handler ` RVA 0x13688090 `；selector ` 1046 `；EOL ` RVA 0x35BED058 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2248d99683b228a0](../../evidence/conditions-sets-013.md#c-2248d99683b228a0) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019382

```text
(exec)# do-exec show ipv6 snooping features <cr>
```

Handler ` RVA 0x13688090 `；selector ` 1045 `；EOL ` RVA 0x35BED640 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2248d99683b228a0](../../evidence/conditions-sets-013.md#c-2248d99683b228a0) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022656

```text
(exec)# do-exec show ipv6 snooping internal counters <cr>
```

Handler ` RVA 0x13688090 `；selector ` 1040 `；EOL ` RVA 0x35BEEBA0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-67a686eea3248185](../../evidence/conditions-sets-040.md#c-67a686eea3248185) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019386

```text
(exec)# do-exec show ipv6 snooping messages <cr>
```

Handler ` RVA 0x13688090 `；selector ` 1047 `；EOL ` RVA 0x35BED390 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2248d99683b228a0](../../evidence/conditions-sets-013.md#c-2248d99683b228a0) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019387

```text
(exec)# do-exec show ipv6 snooping policy <cr>
```

Handler ` RVA 0x1368B750 `；selector ` 0 `；EOL ` RVA 0x35BCC410 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ee2a910a2f062bce](../../evidence/conditions-sets-092.md#c-ee2a910a2f062bce) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019324

```text
(exec)# do-exec show ipv6 source-guard policy <cr>
```

Handler ` RVA 0x136C03A0 `；selector ` 0 `；EOL ` RVA 0x35C08A38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-014992

```text
(exec)# do-exec show ipv6 spd <cr>
```

Handler ` RVA 0x12328600 `；selector ` 0 `；EOL ` RVA 0x358101A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-014701

```text
(exec)# do-exec show ipv6 traffic <cr>
```

Handler ` RVA 0x1231EF70 `；selector ` 0 `；EOL ` RVA 0x3580B3D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-014741

```text
(exec)# do-exec show ipv6 tunnel <cr>
```

Handler ` RVA 0x12321E20 `；selector ` 0 `；EOL ` RVA 0x3580EC48 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d6913a4088f01512](../../evidence/state_effects-sets-045.md#s-d6913a4088f01512)

### path-015568

```text
(exec)# do-exec show isis database <cr>
```

Handler ` RVA 0x106B7B10 `；selector ` 0 `；EOL ` RVA 0x34B630A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-91c21b0044adc86e](../../evidence/conditions-sets-056.md#c-91c21b0044adc86e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-23e68695a37eb3f2](../../evidence/state_effects-sets-008.md#s-23e68695a37eb3f2)

### path-015485

```text
(exec)# do-exec show isis hostname <cr>
```

Handler ` RVA 0x10768F10 `；selector ` 10 `；EOL ` RVA 0x34B62158 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2d965e319e53f7d6](../../evidence/conditions-sets-018.md#c-2d965e319e53f7d6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-2f616b589b1a9ad3](../../evidence/state_effects-sets-011.md#s-2f616b589b1a9ad3)

### path-015511

```text
(exec)# do-exec show isis lsp-log <cr>
```

Handler ` RVA 0x107666B0 `；selector ` 9 `；EOL ` RVA 0x34B62400 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2d965e319e53f7d6](../../evidence/conditions-sets-018.md#c-2d965e319e53f7d6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-2f616b589b1a9ad3](../../evidence/state_effects-sets-011.md#s-2f616b589b1a9ad3)

### path-022846

```text
(exec)# do-exec show isis lspgen tlv neighbor <cr>
```

Handler ` RVA 0x10780F80 `；selector ` 43 `；EOL ` RVA 0x34B652D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-91c21b0044adc86e](../../evidence/conditions-sets-056.md#c-91c21b0044adc86e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-110f0ac6b7900d60](../../evidence/state_effects-sets-004.md#s-110f0ac6b7900d60)

### path-015605

```text
(exec)# do-exec show isis mpls <cr>
```

Handler ` RVA 0x1E6FEF60 `；selector ` 21 `；EOL ` RVA 0x34B66288 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-91c21b0044adc86e](../../evidence/conditions-sets-056.md#c-91c21b0044adc86e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-2f616b589b1a9ad3](../../evidence/state_effects-sets-011.md#s-2f616b589b1a9ad3)

### path-022844

```text
(exec)# do-exec show isis mpls ldp igp-shortcuts <cr>
```

Handler ` RVA 0x1E6FEF60 `；selector ` 27 `；EOL ` RVA 0x34B66358 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-91c21b0044adc86e](../../evidence/conditions-sets-056.md#c-91c21b0044adc86e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-2f616b589b1a9ad3](../../evidence/state_effects-sets-011.md#s-2f616b589b1a9ad3)

### path-022834

```text
(exec)# do-exec show isis mpls traffic-eng adjacency-log <cr>
```

Handler ` RVA 0x1E6FECE0 `；selector ` 6 `；EOL ` RVA 0x34B65968 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-91c21b0044adc86e](../../evidence/conditions-sets-056.md#c-91c21b0044adc86e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-2f616b589b1a9ad3](../../evidence/state_effects-sets-011.md#s-2f616b589b1a9ad3)

### path-022828

```text
(exec)# do-exec show isis mpls traffic-eng advertisements <cr>
```

Handler ` RVA 0x1E6FECE0 `；selector ` 5 `；EOL ` RVA 0x34B656C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-91c21b0044adc86e](../../evidence/conditions-sets-056.md#c-91c21b0044adc86e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-2f616b589b1a9ad3](../../evidence/state_effects-sets-011.md#s-2f616b589b1a9ad3)

### path-024399

```text
(exec)# do-exec show isis mpls traffic-eng downstream-tree <string> <cr>
```

Handler ` RVA 0x1E6FECE0 `；selector ` 7 `；EOL ` RVA 0x34B65CB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` System ID in hostname or in the form of xxxx.xxxx.xxxx。

[条件 C-91c21b0044adc86e](../../evidence/conditions-sets-056.md#c-91c21b0044adc86e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-eb90314b48b3b746](../../evidence/parameters-sets-018.md#p-eb90314b48b3b746) · [状态效果 S-2f616b589b1a9ad3](../../evidence/state_effects-sets-011.md#s-2f616b589b1a9ad3)

### path-022852

```text
(exec)# do-exec show isis mpls traffic-eng tunnel <cr>
```

Handler ` RVA 0x1E6FECE0 `；selector ` 8 `；EOL ` RVA 0x34B65FB0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-91c21b0044adc86e](../../evidence/conditions-sets-056.md#c-91c21b0044adc86e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-2f616b589b1a9ad3](../../evidence/state_effects-sets-011.md#s-2f616b589b1a9ad3)

### path-015495

```text
(exec)# do-exec show isis neighbors <cr>
```

Handler ` RVA 0x1076CB60 `；selector ` 4 `；EOL ` RVA 0x34B62738 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-91c21b0044adc86e](../../evidence/conditions-sets-056.md#c-91c21b0044adc86e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-2f616b589b1a9ad3](../../evidence/state_effects-sets-011.md#s-2f616b589b1a9ad3)

### path-015645

```text
(exec)# do-exec show isis node <cr>
```

Handler ` RVA 0x106D25B0 `；selector ` 42 `；EOL ` RVA 0x34B64460 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-91c21b0044adc86e](../../evidence/conditions-sets-056.md#c-91c21b0044adc86e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-4249a5ac311008a9](../../evidence/state_effects-sets-014.md#s-4249a5ac311008a9)

### path-015530

```text
(exec)# do-exec show isis private <cr>
```

Handler ` RVA 0x1076B790 `；selector ` 16 `；EOL ` RVA 0x34B62D20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-91c21b0044adc86e](../../evidence/conditions-sets-056.md#c-91c21b0044adc86e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-2f616b589b1a9ad3](../../evidence/state_effects-sets-011.md#s-2f616b589b1a9ad3)

### path-015486

```text
(exec)# do-exec show isis timers <cr>
```

Handler ` RVA 0x10769C20 `；selector ` 11 `；EOL ` RVA 0x34B62A10 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-91c21b0044adc86e](../../evidence/conditions-sets-056.md#c-91c21b0044adc86e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-2f616b589b1a9ad3](../../evidence/state_effects-sets-011.md#s-2f616b589b1a9ad3)

### path-015554

```text
(exec)# do-exec show isis tree <cr>
```

Handler ` RVA 0x106B8630 `；selector ` 0 `；EOL ` RVA 0x34B61DA8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2d965e319e53f7d6](../../evidence/conditions-sets-018.md#c-2d965e319e53f7d6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-9141a1f8e499d52f](../../evidence/state_effects-sets-031.md#s-9141a1f8e499d52f)

### path-016198

```text
(exec)# do-exec show issu FSM <cr>
```

Handler ` RVA 0xD4B3A40 `；selector ` 16 `；EOL ` RVA 0x33E5DFD0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a7b38c09c785f353](../../evidence/conditions-sets-065.md#c-a7b38c09c785f353) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)
